"""Local teaching interface; all research calls use the existing Python runner."""

from copy import deepcopy
import csv
import html
import json
import math
from pathlib import Path
from queue import Empty, Queue
from threading import Event, Lock, Thread
from uuid import uuid4

from discussion import MODERATOR_INSTRUCTIONS, ROUND_INSTRUCTIONS, run_discussion, save_session
from urban_jury import append_experiment, build_requests, configuration, request_once


ROOT = Path(__file__).resolve().parent
ROLES = [item["id"] for item in json.loads((ROOT / "agents.json").read_text(encoding="utf-8"))["agents"]]
ACTIVE_RUN = Lock()
CONTROLS = {}


class Control:
    def __init__(self):
        self.stop = Event()
        self.continue_round = Event()
        self.guard = Lock()
        self.paused = False
        self.intervention = ""
        self.snapshot = None
        self.path = None


def plan(question, background, mode, roles, provider, model_name, rounds, moderator,
         max_tokens, temperature, seed, max_calls, budget, pause, openai_key=None):
    if not question.strip():
        raise ValueError("Enter a question.")
    model = model_name.strip()
    if not model.startswith(provider + "/"):
        raise ValueError("The model ID must start with the selected provider followed by /.")
    if not model.partition("/")[2].strip():
        raise ValueError("Enter a model name after the provider prefix.")
    single = mode == "Single model"
    if single and (rounds or moderator):
        raise ValueError("Single-model mode requires zero discussion rounds and no moderator.")
    requests = build_requests(question, background, not single, selected_roles=roles if not single else None)
    generation = {"max_tokens": int(max_tokens)}
    if generation["max_tokens"] < 1 or float(max_tokens) != int(max_tokens):
        raise ValueError("Output-token cap must be a positive whole number.")
    if temperature is not None:
        if not math.isfinite(temperature) or not 0 <= temperature <= 2:
            raise ValueError("Temperature must be between 0 and 2, or blank.")
        generation["temperature"] = temperature
    if seed is not None:
        if float(seed) != int(seed):
            raise ValueError("Seed must be a whole number, or blank.")
        generation["seed"] = int(seed)
    total = len(requests) * (1 + int(rounds)) + int(moderator)
    if max_calls is not None and (float(max_calls) != int(max_calls) or not 1 <= max_calls <= (13 if moderator else 12)):
        raise ValueError("Call cap must be a whole number from 1 to 12 (13 with moderator), or blank.")
    cap = int(max_calls) if max_calls is not None else total
    if budget is not None and (not math.isfinite(budget) or budget < 0):
        raise ValueError("Budget must be nonnegative, or blank.")
    try:
        configuration(model, openai_key if provider == "openai" else None)
        credentials = "Selected provider is configured."
    except ValueError as error:
        credentials = str(error)
    return {"question": question, "background": background, "requests": requests,
            "model": model, "generation": generation, "rounds": int(rounds),
            "moderator": moderator, "max_calls": cap, "budget_usd": budget,
            "pause": pause, "planned_calls": min(total, cap), "configuration": credentials}


def method_view(session=None, prepared=None):
    return {"prepared": prepared, "session": session,
            "discussion_instructions": {str(key): value for key, value in ROUND_INSTRUCTIONS.items()},
            "moderator_instructions": MODERATOR_INSTRUCTIONS,
            "limits": "Model roles do not represent residents or professionals. No public consent is simulated. Claims need source checking. Agreement is not corroboration. Message order and repeated own answers may influence outputs. Fixed settings do not eliminate variability. Interventions change conditions.",
            "instructions_file": json.loads(Path(__file__).with_name("agents.json").read_text(encoding="utf-8"))}


def preview(*values):
    try:
        prepared = plan(*values)
    except (ValueError, TypeError, OSError) as error:
        return None, f"Cannot preview: {error}", method_view()
    cost = ("Local Ollama: no hosted API fee; hardware and electricity unestimated."
            if prepared["model"].startswith("ollama/") else
            "Potentially billable hosted calls. Total cost is unknown; token caps are not dollar spending caps.")
    if prepared["budget_usd"] is not None and not prepared["model"].startswith("ollama/"):
        cost += " The strict budget gate will refuse hosted calls because a guaranteed next-charge bound is unavailable."
    text = (f"**Up to {prepared['planned_calls']} requests**, in fixed selected-role order; no retries. "
            f"Model: `{prepared['model']}`. Output cap: {prepared['generation']['max_tokens']} tokens per call.\n\n"
            + cost + "\n\n" + prepared["configuration"] +
            ("\n\nBackground is empty: no supplied evidence." if not prepared["background"] else "") +
            "\n\nStart runs this frozen preview. Original inputs and settings cannot change mid-session.")
    return prepared, text, method_view(prepared=prepared)


def all_calls(session):
    calls = [call for round_data in session.get("rounds", []) for call in round_data["calls"]]
    moderator = session.get("moderator", {}).get("call")
    return calls + ([moderator] if moderator else [])


def transcript_html(session, role="All", round_filter="All"):
    entries = []
    for round_data in session.get("rounds", []):
        for intervention in session.get("interventions", []):
            if intervention["before_round"] == round_data["number"]:
                entries.append(f"<section><h3>{html.escape(intervention['message_id'])}: researcher intervention</h3><pre style='white-space:pre-wrap'>{html.escape(intervention['text'])}</pre></section>")
        for call in round_data["calls"]:
            if role != "All" and call["agent_id"] != role:
                continue
            if round_filter != "All" and str(round_data["number"]) != round_filter:
                continue
            identifier = html.escape(call["message_id"])
            finish = ((call.get("full_response") or {}).get("choices") or [{}])[0].get("finish_reason")
            body = call["response"] if call["response"] is not None else json.dumps(call["error"])
            entries.append(f"<section id='{identifier}'><h3>{identifier} — {html.escape(call['agent_id'])}</h3><p>Finish: {html.escape(str(finish))}</p><pre style='white-space:pre-wrap'>{html.escape(body)}</pre></section>")
    return "\n".join(entries) or "<p>No responses yet.</p>"


def moderator_html(session):
    moderator = session.get("moderator", {})
    parts = []
    if moderator.get("validation_error"):
        parts.append("<p>" + html.escape(moderator["validation_error"]) + "</p>")
    for section, items in (moderator.get("summary") or {}).items():
        parts.append("<h3>" + html.escape(section.replace("_", " ")) + "</h3>")
        for item in items:
            links = " ".join(f"<a href='#{html.escape(ref)}'>{html.escape(ref)}</a>" for ref in item["references"])
            parts.append("<p>" + html.escape(item["text"]) + " " + links + "</p>")
    raw = moderator.get("call", {}).get("response")
    if raw:
        parts.append("<details><summary>Full moderator output (MOD-1)</summary><pre style='white-space:pre-wrap'>" + html.escape(raw) + "</pre></details>")
    return "\n".join(parts) or "<p>No moderator output.</p>"


USAGE_HEADERS = ["Message", "Role", "Input tokens", "Output tokens", "Estimated USD", "Error"]


def usage_rows(session):
    return [[call["message_id"], call["agent_id"], call.get("input_tokens"), call.get("output_tokens"),
             call.get("estimated_cost_usd"), (call.get("error") or {}).get("type", "")]
            for call in all_calls(session)]


def status_text(session):
    known = session.get("known_estimated_cost_usd", 0)
    remaining = max(0, session["limits"]["max_calls"] - session["attempted_calls"])
    calls = all_calls(session)
    input_total = sum(call.get("input_tokens") or 0 for call in calls)
    output_total = sum(call.get("output_tokens") or 0 for call in calls)
    missing_usage = sum(call.get("input_tokens") is None or call.get("output_tokens") is None for call in calls)
    return (f"**{session['status']}** — calls {session['attempted_calls']}; call allowance remaining {remaining}; "
            f"available input/output totals {input_total}/{output_total} tokens; calls missing counts {missing_usage}; "
            f"known cost estimates USD {known:.8f}; calls with unavailable cost {session.get('unknown_cost_calls', 0)}. "
            + (session.get("stop_reason") or "") +
            "\n\nUnknown usage/cost is not zero. Moderator references are checked for existence, not factual support.")


def start(prepared, browser_id, openai_key=None):
    """Stream snapshots from one worker; controls remain responsive between calls."""
    if not prepared:
        raise ValueError("Preview the configuration before starting.")
    if not ACTIVE_RUN.acquire(blocking=False):
        raise ValueError("Another run is active. Stop or finish it before starting a new one.")
    control = Control()
    CONTROLS[browser_id] = control
    events = Queue()

    def on_update(session, path):
        with control.guard:
            control.snapshot, control.path = session, path
            if session["status"] == "paused" and prepared["pause"]:
                control.paused = True
        events.put(session)

    def before_round(session, number):
        if not prepared["pause"]:
            return None
        with control.guard:
            control.paused = True
        # No model call is active; continue/stop handlers release this event.
        control.continue_round.wait()
        with control.guard:
            text = control.intervention
            control.intervention = ""
            control.paused = False
            control.continue_round.clear()
        return text

    def worker():
        try:
            import litellm
            litellm.suppress_debug_info = True
            options = configuration(prepared["model"], openai_key if prepared["model"].startswith("openai/") else None)
            ROOT.joinpath("records").mkdir(exist_ok=True)
            record = ROOT / "records" / f"ui-{uuid4()}.json"
            run_discussion(litellm, options, deepcopy(prepared["requests"]), prepared["question"],
                           prepared["background"], dict(prepared["generation"]), prepared["rounds"],
                           prepared["max_calls"], prepared["budget_usd"], ROOT / "experiment-log.md", record,
                           request_once, append_experiment, moderator=prepared["moderator"],
                           on_update=on_update, before_round=before_round, should_stop=control.stop.is_set)
        except Exception:
            # Never expose provider exceptions or credentials to the browser.
            error_message = "Run stopped because configuration, execution or saving failed. Check the selected provider configuration and saved session. Do not replay paid requests just to save them."
            if control.snapshot:
                snapshot = deepcopy(control.snapshot)
                snapshot.update(status="failed", stop_reason=error_message)
                try:
                    save_session(control.path, snapshot)
                except OSError:
                    pass
                on_update(snapshot, control.path)
            else:
                events.put(error_message)
        finally:
            ACTIVE_RUN.release()
            events.put(None)

    Thread(target=worker, daemon=True).start()
    try:
        while True:
            try:
                session = events.get(timeout=0.5)
            except Empty:
                continue
            if session is None:
                break
            if isinstance(session, str):
                yield session, "", "", [], method_view(), None, False
            else:
                yield status_text(session), transcript_html(session), moderator_html(session), usage_rows(session), method_view(session), None, session["status"] in ("running", "paused", "moderating")
        if control.snapshot:
            session = control.snapshot
            yield status_text(session), transcript_html(session), moderator_html(session), usage_rows(session), method_view(session), None, False
    finally:
        # A disconnected browser must not leave an unattended paused session running.
        control.stop.set()
        control.continue_round.set()


def intervene(browser_id, text):
    control = CONTROLS.get(browser_id)
    if not control:
        return "No active session."
    with control.guard:
        if not control.paused or control.continue_round.is_set():
            return "Continue is available only while paused between rounds."
        control.intervention = text
        control.continue_round.set()
    return "Continuing; any intervention will be recorded and sent identically to all selected agents."


def stop_run(browser_id):
    control = CONTROLS.get(browser_id)
    if not control:
        return "No active session."
    control.stop.set()
    control.continue_round.set()
    return "Stop requested. Any in-flight call will finish and be saved; it may be billable."


def export_session(browser_id):
    control = CONTROLS.get(browser_id)
    if not control or not control.snapshot:
        return []
    with control.guard:
        session = deepcopy(control.snapshot)
    folder = ROOT / "records" / f"export-{uuid4()}"
    folder.mkdir()
    full = folder / "session.json"
    full.write_text(json.dumps(session, indent=2, ensure_ascii=False), encoding="utf-8")
    markdown = folder / "transcript.md"
    parts = ["# Urban Jury session export", "Research outputs, not public consent. Unknown values remain null."]
    for call in all_calls(session):
        parts.append(f"## {call['message_id']} — {call['agent_id']}")
        text = call.get("response") or json.dumps(call.get("error"))
        fence = "```"
        while fence in text:
            fence += "`"
        parts.append(f"{fence}\n{text}\n{fence}")
    payload = json.dumps(session, indent=2, ensure_ascii=False)
    fence = "```"
    while fence in payload:
        fence += "`"
    parts.append("## Full methodological record, including interventions and exact requests\n\n" + fence + "json\n" + payload + "\n" + fence)
    markdown.write_text("\n\n".join(parts), encoding="utf-8")
    usage = folder / "usage.csv"
    with usage.open("w", newline="", encoding="utf-8-sig") as output:
        writer = csv.writer(output)
        writer.writerow(USAGE_HEADERS)
        writer.writerows(usage_rows(session))
    return [str(full), str(markdown), str(usage)]


def filter_transcript(browser_id, role, number):
    control = CONTROLS.get(browser_id)
    return transcript_html(control.snapshot, role, number) if control and control.snapshot else "No session."


def upload_background(path):
    return Path(path).read_text(encoding="utf-8-sig") if path else ""


def create_app():
    import gradio as gr
    with gr.Blocks(title="Urban Jury", analytics_enabled=False) as demo:
        browser_id = gr.State(lambda: str(uuid4()))
        prepared = gr.State(None)
        gr.Markdown("# Urban Jury\nGenerate research questions from analytical perspectives. These agents do not represent residents or professionals, and agreement does not establish public consent.")
        with gr.Row():
            question = gr.Textbox(label="Research question", lines=3, value="What research questions would help investigate a proposed shopping mall at Tempelhofer Feld?")
            background = gr.Textbox(label="Shared background — evidence to examine", lines=6, placeholder="Paste source excerpts and references here. Empty means no supplied evidence.")
        upload = gr.File(label="Optional UTF-8 background file", file_types=[".txt", ".md"], type="filepath")
        with gr.Row():
            mode = gr.Radio(["Jury", "Single model"], value="Jury", label="Mode")
            roles = gr.CheckboxGroup(ROLES, value=ROLES, label="Jury — fixed order shown")
        with gr.Row():
            provider = gr.Dropdown(["openai", "anthropic", "deepseek", "ollama"], value="ollama", label="Provider")
            model = gr.Textbox(value="ollama/llama3.2", label="Full model ID")
            rounds = gr.Dropdown([0, 1, 2], value=0, label="Discussion rounds after independent assessments")
            moderator = gr.Checkbox(value=False, label="Moderator (+1 call)")
        openai_key = gr.Textbox(type="password", label="OpenAI API key (optional)",
                               placeholder="Paste your replacement OpenAI key here, or leave blank to use OPENAI_API_KEY",
                               info="Used only for OpenAI calls in this run. Excluded from experiment records and exports. Cleared after the run. Other providers use environment variables.")
        with gr.Accordion("Generation settings and limits", open=False):
            with gr.Row():
                max_tokens = gr.Number(value=800, precision=0, label="Maximum output tokens per call")
                temperature = gr.Number(value=None, label="Temperature (blank = unset)")
                seed = gr.Number(value=None, label="Seed (blank = unset)")
                max_calls = gr.Number(value=None, label="Maximum calls (blank = planned total)")
                budget = gr.Number(value=None, label="Strict USD gate (blank = off; hosted calls refused if set)")
        pause = gr.Checkbox(value=True, label="Pause between discussion rounds")
        with gr.Row():
            preview_button = gr.Button("Preview")
            start_button = gr.Button("Start frozen preview", variant="primary")
            stop_button = gr.Button("Stop after current call")
        preview_text = gr.Markdown("Preview before starting. Enter an OpenAI key only in the masked field, or use environment variables. Never put keys in questions or background.")
        status = gr.Markdown("Ready.")
        with gr.Row():
            intervention = gr.Textbox(label="Researcher intervention — only between rounds", lines=2)
            continue_button = gr.Button("Continue with intervention (or leave blank)")
        control_status = gr.Markdown()
        with gr.Tabs():
            with gr.Tab("Transcript and moderator"):
                with gr.Row():
                    role_filter = gr.Dropdown(["All", *ROLES, "single"], value="All", label="View role")
                    round_filter = gr.Dropdown(["All", "0", "1", "2"], value="All", label="View round")
                gr.Markdown("Filters affect the view only. Select All to navigate every moderator reference.")
                transcript = gr.HTML("No responses yet.")
                summary = gr.HTML("No moderator output.")
            with gr.Tab("Usage"):
                usage = gr.Dataframe(headers=USAGE_HEADERS, interactive=False)
            with gr.Tab("Method"):
                method = gr.JSON(value=method_view(), label="Instructions, inputs, snapshots, exact requests and limitations")
            with gr.Tab("Export"):
                export_button = gr.Button("Export current saved snapshot")
                files = gr.File(label="Full JSON, Markdown and usage CSV", file_count="multiple")
        inputs = [question, background, mode, roles, provider, model, rounds, moderator,
                  max_tokens, temperature, seed, max_calls, budget, pause]
        preview_button.click(preview, [*inputs, openai_key], [prepared, preview_text, method], queue=False)
        for component in inputs:
            component.change(lambda: (None, "Configuration changed. Preview again before starting a new session."), None, [prepared, preview_text], queue=False)
        upload.change(upload_background, upload, background, queue=False)
        provider.change(lambda selected: {"openai": "openai/gpt-4o-mini", "anthropic": "anthropic/claude-sonnet-4-5", "deepseek": "deepseek/deepseek-chat", "ollama": "ollama/llama3.2"}[selected], provider, model, queue=False)

        def stream(configuration_snapshot, key, api_key):
            for status_value, transcript_value, summary_value, rows, inspection, unused, busy in start(configuration_snapshot, key, api_key):
                yield status_value, transcript_value, summary_value, rows, inspection, gr.update(interactive=not busy), gr.skip() if busy else ""

        start_button.click(stream, [prepared, browser_id, openai_key], [status, transcript, summary, usage, method, start_button, openai_key], concurrency_limit=1)
        stop_button.click(stop_run, browser_id, control_status, queue=False)
        continue_button.click(intervene, [browser_id, intervention], control_status, queue=False)
        export_button.click(export_session, browser_id, files, queue=False)
        role_filter.change(filter_transcript, [browser_id, role_filter, round_filter], transcript, queue=False)
        round_filter.change(filter_transcript, [browser_id, role_filter, round_filter], transcript, queue=False)
    return demo.queue(default_concurrency_limit=1, max_size=1)


if __name__ == "__main__":
    create_app().launch(server_name="127.0.0.1", share=False, inbrowser=True)
