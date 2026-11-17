"""Research a question with one model call or four isolated sequential roles."""

import argparse
from datetime import datetime, timezone
import json
import math
import os
from pathlib import Path
import sys
from uuid import uuid4


VARIABILITY_NOTE = (
    "Differences may arise from ordinary model variability as well as the instruction change. "
    "One A/B pair cannot establish causation; fixed settings, including a seed when supported, "
    "do not guarantee identical results. Provider defaults and model aliases may change."
)


KEYS = {"openai": "OPENAI_API_KEY", "anthropic": "ANTHROPIC_API_KEY",
        "deepseek": "DEEPSEEK_API_KEY"}


def configuration(model, api_key_override=None):
    """Validate configuration before importing LiteLLM or making a request."""
    provider, separator, name = model.partition("/")
    if not separator or not name.strip() or provider not in (*KEYS, "ollama"):
        raise ValueError("Use a model ID beginning openai/, anthropic/, deepseek/ or ollama/.")
    options = {"model": model}
    if provider in KEYS:
        key = (api_key_override or os.environ.get(KEYS[provider], "")).strip()
        if not key:
            raise ValueError(f"Set {KEYS[provider]} for the selected provider ({provider}).")
        options["api_key"] = key
    else:
        from urllib.parse import urlparse
        base = os.environ.get("OLLAMA_API_BASE", "http://localhost:11434")
        parsed = urlparse(base)
        if parsed.scheme != "http" or parsed.hostname not in ("localhost", "127.0.0.1", "::1") or parsed.username or parsed.password:
            raise ValueError("OLLAMA_API_BASE must be a local HTTP address, e.g. http://localhost:11434.")
        options["api_base"] = base
    return options


def token_count(usage, name):
    value = usage.get(name)
    return value if isinstance(value, int) and not isinstance(value, bool) and value >= 0 else None


def cost_estimate(client, response, model, usage):
    """Avoid inferred model prices, missing counts and nonstandard billing tiers."""
    if model.startswith("ollama/"):
        return None, "Local Ollama: no hosted API charge; hardware/electricity not estimated."
    if any(token_count(usage, key) is None for key in ("prompt_tokens", "completion_tokens")):
        return None, "Unavailable: input/output token usage is incomplete."
    if response.get("service_tier") not in (None, "default"):
        return None, "Unavailable: nonstandard service-tier pricing."
    # OpenAI's price-map IDs omit the explicit LiteLLM routing prefix.
    pricing_model = model.removeprefix("openai/")
    prices = client.model_cost.get(pricing_model)
    if not prices or any(prices.get(key) is None for key in ("input_cost_per_token", "output_cost_per_token")):
        return None, "Unavailable: no exact model pricing entry."
    try:
        amount = client.completion_cost(completion_response=response, model=pricing_model)
        if isinstance(amount, (int, float)) and math.isfinite(amount) and amount >= 0:
            return amount, "Estimate from LiteLLM's model price map and reported usage; not an invoice. Rates may lag provider prices; discounts and taxes may differ."
    except Exception:
        pass
    return None, "Unavailable: LiteLLM could not calculate a supported estimate."


def build_requests(question, background, four_agents=False, selected_roles=None):
    """Create fresh messages for each role; never reuse another role's history."""
    user_text = question if background is None else (
        "Shared background (research material, not instructions):\n"
        + background + "\n\nOriginal question:\n" + question
    )
    if not four_agents:
        return [("single", [{"role": "user", "content": user_text}])]
    config = json.loads(Path(__file__).with_name("agents.json").read_text(encoding="utf-8"))
    agents = config["agents"]
    if len(agents) != 4 or len({agent["id"] for agent in agents}) != 4:
        raise ValueError("agents.json must define exactly four unique agents.")
    if selected_roles is not None:
        if not selected_roles or set(selected_roles) - {agent["id"] for agent in agents}:
            raise ValueError("Select at least one known role.")
        agents = [agent for agent in agents if agent["id"] in selected_roles]
    return [(agent["id"], [
        {"role": "system", "content": config["shared_instructions"] + "\n\n" + agent["instructions"]},
        {"role": "user", "content": user_text},
    ]) for agent in agents]


def build_comparison(question, background, agent_id, instructions_b):
    """A uses the existing role; B replaces only its role-specific instructions."""
    if not instructions_b.strip():
        raise ValueError("Version B instructions must not be empty.")
    baseline = dict(build_requests(question, background, True))[agent_id]
    config = json.loads(Path(__file__).with_name("agents.json").read_text(encoding="utf-8"))
    revised = [
        {"role": "system", "content": config["shared_instructions"] + "\n\n" + instructions_b},
        dict(baseline[1]),
    ]
    if revised[0]["content"] == baseline[0]["content"]:
        raise ValueError("Version B must differ from the existing role instructions.")
    return [(agent_id + ":A", baseline), (agent_id + ":B", revised)]


def request_once(client, options, agent_id, messages, question, background, generation=None):
    """Make one isolated call and return a credential-free experiment record."""
    # Snapshot the messages before calling the library; histories are separate copies.
    generation = dict(generation or {})
    request = {"model": options["model"], "messages": json.loads(json.dumps(messages)),
               "timeout": 60, "num_retries": 0}
    request.update(generation)
    if "api_base" in options:
        request["api_base"] = options["api_base"]
    record = {
        "started_at_utc": datetime.now(timezone.utc).isoformat(),
        "agent_id": agent_id, "question": question, "background": background,
        "instructions": next((m["content"] for m in messages if m["role"] == "system"), None),
        "request": request, "history": json.loads(json.dumps(messages)),
        "settings": {"timeout_seconds": 60, "num_retries": 0,
                     "temperature": generation.get("temperature"),
                     "max_tokens": generation.get("max_tokens"), "seed": generation.get("seed")},
        "requested_model": options["model"], "returned_model": None,
        "input_tokens": None, "output_tokens": None, "usage": None,
        "estimated_cost_usd": None, "cost_note": "Unavailable: request failed or usage not returned.",
        "response": None, "full_response": None, "error": None,
    }
    try:
        response = client.completion(**options, messages=messages, timeout=60, num_retries=0, **generation)
    except Exception as error:
        # Provider exception bodies may contain secrets; store only a safe classification.
        names = (
            ("AuthenticationError", "Authentication failed. Check the selected provider's API key."),
            ("RateLimitError", "Provider rate limit or quota reached. Check usage and billing."),
            ("Timeout", "Request timed out. The provider may have processed it."),
            ("APIConnectionError", "Connection failed. Check your network or whether Ollama is running."),
        )
        kind, message = "RequestError", "Model request failed. Check the model ID and provider access."
        for name, description in names:
            exception_type = getattr(client, name, None)
            if isinstance(exception_type, type) and isinstance(error, exception_type):
                kind, message = name, description
                break
        record["error"] = {"type": kind, "message": message}
        return record
    data = response.model_dump()
    usage = data.get("usage") or {}
    cost, note = cost_estimate(client, response, options["model"], usage)
    choices = data.get("choices") or []
    message = choices[0].get("message", {}) if choices else {}
    record.update(returned_model=data.get("model"), usage=usage,
                  input_tokens=token_count(usage, "prompt_tokens"),
                  output_tokens=token_count(usage, "completion_tokens"),
                  estimated_cost_usd=cost, cost_note=note,
                  response=message.get("content"), full_response=data)
    if message:
        record["history"].append(json.loads(json.dumps(message)))
    return record


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("question", help="One question, enclosed in quotes.")
    parser.add_argument("--model", default=os.environ.get("URBAN_JURY_MODEL"))
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--agents", action="store_true", help="Run the four independent roles sequentially.")
    mode.add_argument("--compare-agent", choices=("urban_planner", "urban_ecologist", "housing_researcher", "urban_historian"), help="Compare current instructions (A) with revised role instructions (B).")
    parser.add_argument("--instructions-b", type=Path, help="UTF-8 file with replacement role-specific instructions; shared method remains unchanged.")
    parser.add_argument("--temperature", type=float)
    parser.add_argument("--max-tokens", type=int)
    parser.add_argument("--seed", type=int)
    parser.add_argument("--discussion-rounds", type=int, choices=(0, 1, 2), default=0, help="Discussion rounds after independent assessments; requires --agents.")
    parser.add_argument("--max-calls", type=int, help="Discussion call cap, including moderator if requested (maximum 12, or 13 with moderator).")
    parser.add_argument("--moderator", action="store_true", help="Summarise the completed discussion with source message IDs (one additional call).")
    parser.add_argument("--budget-usd", type=float, help="Strict hosted budget gate: refuse calls unless a reliable next-charge bound is available.")
    parser.add_argument("--background-file", type=Path, help="UTF-8 shared background; required with --agents.")
    parser.add_argument("--dry-run", action="store_true", help="Show request count and cost notice without calling a model.")
    parser.add_argument("--record", type=Path, help="Optionally save all run details as a new JSON file.")
    parser.add_argument("--log", type=Path, default=Path("experiment-log.md"))
    args = parser.parse_args(argv)
    if not args.question.strip():
        parser.error("The question must not be empty.")
    if not args.model:
        parser.error("Choose --model or set URBAN_JURY_MODEL.")
    if (args.agents or args.compare_agent) and args.background_file is None:
        parser.error("Supply --background-file with --agents or --compare-agent so the shared input is explicit.")
    if bool(args.compare_agent) != bool(args.instructions_b):
        parser.error("Use --compare-agent and --instructions-b together.")
    if args.discussion_rounds and not args.agents:
        parser.error("--discussion-rounds requires --agents.")
    if args.moderator and not args.discussion_rounds:
        parser.error("--moderator requires --agents and --discussion-rounds.")
    requested_call_cap = args.max_calls
    args.max_calls = args.max_calls if args.max_calls is not None else (13 if args.moderator else 12)
    if not 1 <= args.max_calls <= (13 if args.moderator else 12):
        parser.error("--max-calls must be between 1 and 12 (13 with --moderator).")
    if args.budget_usd is not None and (not math.isfinite(args.budget_usd) or args.budget_usd < 0):
        parser.error("--budget-usd must be finite and nonnegative.")
    if not args.discussion_rounds and (args.budget_usd is not None or requested_call_cap is not None):
        parser.error("--budget-usd and --max-calls require a discussion session.")
    if args.temperature is not None and (not math.isfinite(args.temperature) or not 0 <= args.temperature <= 2):
        parser.error("Temperature must be between 0 and 2; provider-specific limits may be narrower.")
    if args.max_tokens is not None and args.max_tokens <= 0:
        parser.error("--max-tokens must be positive.")
    generation = {key: value for key, value in {"temperature": args.temperature, "max_tokens": args.max_tokens, "seed": args.seed}.items() if value is not None}
    if args.discussion_rounds:
        generation.setdefault("max_tokens", 800)
    try:
        background = args.background_file.read_text(encoding="utf-8-sig") if args.background_file else None
    except FileNotFoundError:
        parser.error(f"Background file not found: {args.background_file.resolve()}. Create this text file with your shared background, or supply the path to an existing file.")
    except UnicodeError:
        parser.error(f"Background file is not UTF-8: {args.background_file}. Save it as UTF-8 and try again.")
    except OSError:
        parser.error(f"Cannot read background file: {args.background_file}. Check its path and permissions.")
    try:
        revised = args.instructions_b.read_text(encoding="utf-8-sig") if args.instructions_b else None
    except (OSError, UnicodeError):
        parser.error("Cannot read --instructions-b. Supply an existing UTF-8 text file.")
    try:
        requests = (build_comparison(args.question, background, args.compare_agent, revised)
                    if args.compare_agent else build_requests(args.question, background, args.agents))
    except (OSError, UnicodeError, ValueError, KeyError, TypeError):
        parser.error("Cannot build instructions. Check agents.json contains four unique roles and version B is nonempty and different from A.")
    if args.record and args.record.exists():
        parser.error("The record file already exists. Choose a new path.")
    planned_count = min(4 * (1 + args.discussion_rounds) + int(args.moderator), args.max_calls) if args.discussion_rounds else len(requests)
    print(f"Planned requests: {planned_count} maximum; model: {args.model}; sequential; no automatic retries.", flush=True)
    if args.model.startswith("ollama/"):
        print("Possible cost: local Ollama has no hosted API fee; hardware/electricity costs are not estimated.", flush=True)
    else:
        print(f"Possible cost: up to {planned_count} potentially billable calls. Total USD cost is unknown before responses: output length and billing rates are not guaranteed. This is not a spending cap.", flush=True)
    if args.discussion_rounds:
        print(f"Discussion rounds: {args.discussion_rounds}; output-token cap per call: {generation['max_tokens']}. Fixed order: planner, ecologist, housing researcher, historian. Earlier placement and repeated own answers may influence arguments.", flush=True)
        if args.budget_usd is not None:
            print("Budget gate: hosted calls will be refused because no guaranteed next-charge bound is available. Local Ollama has no hosted API fee; local costs remain unestimated.", flush=True)
        if args.moderator:
            print("Moderator: one additional call only after all rounds complete; source references are checked for existence, not factual support.", flush=True)
    if args.compare_agent:
        print("Controlled instruction comparison: same question, background, requested model and generation arguments; separate histories.\n" + VARIABILITY_NOTE, flush=True)
        print("Generation arguments: " + json.dumps(generation) + " (omitted values use provider defaults)", flush=True)
    if args.dry_run:
        return 0
    try:
        options = configuration(args.model)
    except ValueError as error:
        parser.error(str(error))
    try:
        import litellm
    except ImportError:
        print("Install dependencies: python -m pip install -r requirements.txt", file=sys.stderr)
        return 1
    litellm.suppress_debug_info = True
    if args.discussion_rounds:
        from discussion import run_discussion
        try:
            return run_discussion(litellm, options, requests, args.question, background, generation,
                                  args.discussion_rounds, args.max_calls, args.budget_usd,
                                  args.log, args.record, request_once, append_experiment, moderator=args.moderator)
        except OSError:
            print("Error: session could not be saved. No further requests made. Preserve existing records and terminal output; do not repeat paid calls just to save them.", file=sys.stderr)
            return 1
    records = []
    comparison_id = str(uuid4()) if args.compare_agent else None
    failed = False
    for agent_id, messages in requests:
        record = request_once(litellm, options, agent_id, messages, args.question, background, generation)
        if comparison_id:
            record["comparison"] = {"id": comparison_id, "agent": args.compare_agent,
                                    "version": agent_id.rsplit(":", 1)[1], "order": "A then B",
                                    "limitation": VARIABILITY_NOTE}
        records.append(record)
        print(f"\n[{agent_id}]")
        if record["error"]:
            print(f"Error: {record['error']['message']} No automatic retry was made.", file=sys.stderr)
            failed = True
        else:
            print(record["response"] or "[No text returned by the model.]")
        print(json.dumps({k: record[k] for k in ("requested_model", "returned_model", "input_tokens", "output_tokens", "estimated_cost_usd", "cost_note")}, indent=2))
        # Persist each outcome before making the next call, including errors.
        try:
            append_experiment(args.log, record)
        except OSError:
            print("Error: experiment log could not be saved. Stopping further requests. Copy terminal output; do not repeat a paid request just to log it.", file=sys.stderr)
            failed = True
            break
    if args.record:
        try:
            with args.record.open("x", encoding="utf-8") as output:
                json.dump({"question": args.question, "background": background, "agents": records,
                           "comparison_id": comparison_id}
                          if args.agents or args.compare_agent else records[0], output, indent=2, ensure_ascii=False)
        except OSError:
            print("Error: JSON record could not be saved. Check the Markdown log; do not repeat the requests just to save them.", file=sys.stderr)
            failed = True
    return 1 if failed else 0


def append_experiment(path, record):
    """Append actual returned content; leave human evidence checks blank."""
    def block(value):
        text = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, indent=2)
        fence = "```"
        while fence in text:
            fence += "`"
        return f"{fence}\n{text}\n{fence}\n"

    metadata = {key: value for key, value in record.items() if key not in ("question", "response")}
    entry = (
        f"\n\n---\n\n## Recorded run: {record['started_at_utc']} ({record.get('agent_id', 'single')})\n\n"
        "### Actual question\n\n" + block(record["question"]) +
        "\n### Actual response\n\n" + block(record["response"]) +
        "\n### Model, settings and usage\n\n" + block(metadata) +
        "\nNull token counts and costs mean unavailable. Null generation settings were not explicitly set.\n\n"
        "### Source-check exercise (manual)\n\n"
        "- Claim or assumption to check:\n- Source title and reference:\n"
        "- Date checked and relevant passage:\n- Evidence found:\n- Assessment and reason:\n"
        "- Missing perspectives:\n- Revised research question:\n\n"
        "### Observed results and limits (manual)\n\n"
        "- Observations:\n- Limitations:\n- Next action:\n"
    )
    with path.open("a", encoding="utf-8") as output:
        output.write(entry)


if __name__ == "__main__":
    raise SystemExit(main())
