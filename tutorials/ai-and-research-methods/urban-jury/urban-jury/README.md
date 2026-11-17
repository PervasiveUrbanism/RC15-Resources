# Urban Jury: one question, one model or four analytical roles

## Local Gradio interface on Windows

Open PowerShell in this project folder. If this is a new setup, first create the
environment with `py -3.12 -m venv .venv`. Then install the optional interface and
start it:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-ui.txt
.\.venv\Scripts\python.exe app.py
```

The browser opens at [the local interface](http://127.0.0.1:7860). If it does not,
open the local address printed in the terminal. Keep that terminal open while
using the app; press Ctrl+C there to shut it down. No activation or execution-policy
change is needed. Gradio 6.32.0 is the only new direct UI dependency; its supporting
packages are installed by pip. The CLI still needs only `requirements.txt`.

The app binds only to `127.0.0.1`, with `share=False`: public sharing is disabled.
Hosted model requests still send your question and background to the selected
provider. Local Ollama needs a separately installed running service and downloaded
model, as described below.

### Where to enter the OpenAI key

Select **openai** under Provider, then paste your key into **OpenAI API key
(optional)**, the masked field below the model controls. The model field suggests
`openai/gpt-4o-mini`; you can edit it. Use **Preview**, review the request count and
cost notice, then **Start frozen preview**. A key entered there applies only to
OpenAI, is excluded from the application's saved session, Markdown records and
exports, and the field is cleared after a run. Never put it in the question or
background. Masking hides the on-screen characters; the field passes the key to
your local Python process so it can authenticate the request.

Alternatively leave the field blank and set `$env:OPENAI_API_KEY = "YOUR_KEY"` in
the same PowerShell window before starting the app. This is convenient for repeated
runs. Claude and DeepSeek use their corresponding environment variables; Ollama
requires no key. Only the selected provider needs credentials.

### Using the interface

- Edit the question and background, or upload a UTF-8 `.txt`/`.md` background file.
  Empty background is explicitly identified as no supplied evidence.
- Select any of the four roles in the fixed displayed order, choose the model,
  and choose zero, one or two discussion rounds. Single-model mode requires zero
  rounds and no moderator.
- Preview always makes **no model calls**. It displays up to
  `selected roles × (1 + discussion rounds) + optional moderator` requests,
  limited by the call cap. Start uses the previewed inputs and settings. Changing
  configuration clears the preview for a new run; it does not alter an active run.
- The output-token cap defaults to 800. Unset temperature and seed remain unset.
  A truncated or failed round blocks later rounds. No automatic retries occur.
- Pause between rounds is enabled by default. Continue can append a researcher
  intervention verbatim and identically to all selected agents. Interventions
  have IDs (`I1`, etc.), change the experimental conditions and are saved alongside
  timestamps. Preceding-round snapshots remain unchanged.
- Stop takes effect after any in-flight call finishes and is saved. That call may
  still be billable. Only one run is active at a time in this initial local app.
- The labelled transcript and moderator appear with stable message IDs. Filters
  affect the view only. The Method tab shows full instructions, exact requests,
  snapshots, settings and limitations. Moderator source links navigate to the
  original messages when the full transcript is displayed.
- Usage shows per-call counts, available totals, unknown costs and estimates.
  Dollar estimates are not invoices. The optional strict budget gate refuses
  hosted calls because a guaranteed upper bound is unavailable.
- Export produces complete JSON, Markdown and a usage CSV, including stopped or
  incomplete sessions. Files use new names under `records/`; original records
  are preserved. Existing sessions survive on disk, but this first UI does not
  import or resume them. A/B experiments remain available through the CLI.

Connection failures appear under the relevant role/message ID and remain in the
saved session. Check the selected provider's credentials and model access, your
network, or whether Ollama is running. Provider exception bodies are excluded from
application error messages to avoid exposing secrets. A timeout is not proof that
the provider did not process or bill the request. Inspect records before deciding
whether to start a new run.

`app.py` is an adapter around `build_requests`, `configuration`, `request_once`,
`run_discussion`, `save_session`, `append_experiment` and moderator validation.
The shared runner exposes update, round-boundary and stop callbacks; it keeps
ordinary dictionaries and isolated histories. Research logic is not duplicated
in Gradio event handlers.

A small command-line starting point for research about Tempelhofer Feld. It sends
one question to a selected model, either once or through four independent roles.
It prints answers and run metadata. It does not
retrieve evidence, verify claims, simulate residents or establish
public consent. Treat answers as material to investigate, not research findings.

## Windows setup (PowerShell)

Install Python 3.12 and open PowerShell in this folder. Create an isolated
environment and install the dependency:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

There is no need to activate the environment or change PowerShell execution policy.
LiteLLM is the only direct dependency, pinned to version 1.109.1. It provides a common interface to model
providers; pip also installs its required supporting packages. Installation makes
no model requests. Python's built-in argparse, os, pathlib and json handle CLI
arguments, environment variables, paths and records. unittest runs the offline tests.

## Choose one provider

Each hosted command below makes **one potentially billable request**. Review your
provider's pricing before running it. Only set the key for the provider you use.
Replace example key values locally; never commit keys, paste them into source
files or include them in shared screenshots. PowerShell assignments last for the
current terminal session. No .env loader is used.

OpenAI:

```powershell
$env:OPENAI_API_KEY = "YOUR_OPENAI_KEY"
.\.venv\Scripts\python.exe urban_jury.py --model openai/gpt-4o-mini "What research question could investigate recreational use of Tempelhofer Feld?"
```

Claude (Anthropic):

```powershell
$env:ANTHROPIC_API_KEY = "YOUR_ANTHROPIC_KEY"
.\.venv\Scripts\python.exe urban_jury.py --model anthropic/claude-sonnet-4-5 "What evidence would help investigate competing uses of Tempelhofer Feld?"
```

DeepSeek:

```powershell
$env:DEEPSEEK_API_KEY = "YOUR_DEEPSEEK_KEY"
.\.venv\Scripts\python.exe urban_jury.py --model deepseek/deepseek-chat "Suggest one research question about access to Tempelhofer Feld."
```

Model names are examples, not fixed defaults: use an available model ID for your
account, preserving the provider prefix. Claude uses the prefix `anthropic/`.

Local Ollama requires a separate Ollama installation and a downloaded model:

```powershell
ollama pull llama3.2
.\.venv\Scripts\python.exe urban_jury.py --model ollama/llama3.2 "Suggest one research question about Tempelhofer Feld."
```

The pull downloads model files and needs disk space and internet access. Ensure
Ollama is running; start `ollama serve` if needed. No API keys are required. The
default endpoint is `http://localhost:11434`; optionally set `OLLAMA_API_BASE` to
another local HTTP port. Remote Ollama endpoints are deliberately unsupported.
Local computation has hardware and electricity costs, which this app does not estimate.

Instead of passing --model each time:

```powershell
$env:URBAN_JURY_MODEL = "ollama/llama3.2"
.\.venv\Scripts\python.exe urban_jury.py "What evidence would help investigate park accessibility?"
```

An explicit --model overrides the environment setting. `--help` makes no request.
Hosted providers receive the question; use source material you are authorised to send.

## Metadata and optional records

Before any model request, the app prints the planned request count, model and
possible cost. Hosted calls may incur charges; a reliable total is unavailable
before output length and billing details are known. The notice is not a spending
cap or an interactive confirmation. Add `--dry-run` to preview without credentials
or model calls.

The terminal shows the requested model ID, provider-returned model ID, available
input/output token counts and a USD cost estimate when supported. Missing counts
and unavailable costs are `null`, never guessed or represented as zero.

Cost calculation uses LiteLLM's response-aware calculator only when the exact
requested model has a price-map entry and both token counts are available
(OpenAI's routing prefix is removed to match its price-map IDs).
Nonstandard service tiers are excluded. These are estimates based on the installed
library's pricing data, which may lag current rates; they are not invoices or
spending limits. Check provider billing for actual charges. No flat token-price
fallback or guessed model alias is used. Ollama costs are left unavailable.
See [LiteLLM usage and costs](https://docs.litellm.ai/docs/completion/token_usage).

To save a response and its metadata, create the ignored records folder and choose
a new filename:

```powershell
New-Item -ItemType Directory -Force records
.\.venv\Scripts\python.exe urban_jury.py --model ollama/llama3.2 --record records\first-run.json "Suggest one research question about Tempelhofer Feld."
```

Every request outcome, including a safely described error, is automatically appended with its original question,
UTC request-start time, model IDs, explicit settings, usage and cost information
to `experiment-log.md` in the current folder. Run the app from the project folder
to append to the existing log. Use `--log path\to\another-log.md` to choose another
file. Previous entries and notes are preserved. Source checks and interpretation
remain blank for you to complete. Earlier runs cannot be recovered automatically.

Optional JSON records now also include the original question, timestamp and
settings. Existing JSON files are not overwritten. Credential configuration is
not saved, but question and answer text are saved verbatim: keep secrets out of
prompts. Terminal history and provider retention are separate from these records.

## Four independent agents

The original single-call commands still work. Add `--agents` and provide a UTF-8
background file to run the urban planner, urban ecologist, housing researcher and
urban historian. Create `background.txt` yourself with the shared material you
want to investigate. Its text is supplied unchanged to all four roles.

Preview first (no requests):

```powershell
.\.venv\Scripts\python.exe urban_jury.py --agents --model openai/gpt-4o-mini --background-file background.txt --dry-run "What questions should we investigate about competing uses of Tempelhofer Feld?"
```

To run, remove `--dry-run`. That makes **four sequential, potentially billable
calls** using the same selected model. Alternatively select `ollama/llama3.2`
for local computation. Optional `--record records\four-agent-run.json` saves the
combined JSON record; create the records directory first.

`agents.json` contains the shared methodological instructions and the four role
instructions. Ordinary functions construct a fresh message list for every agent:
its system instructions, the common user message, then its own returned answer.
No agent receives another agent's instructions or answer. Histories are recorded
but start fresh on each CLI invocation; there are no automatic follow-up rounds.
The background is labelled as research material rather than instructions.

The Markdown log saves each agent's full instructions, original question and
background, exact LiteLLM request arguments excluding credentials, normalized
response, separate history, requested/returned model IDs, available usage and
cost estimate. Optional JSON contains the same data. These are application-level
requests and responses, not raw provider HTTP traffic. Error records store a safe
classification and message; raw provider exception text is excluded because it
may expose secrets. No credentials are intentionally included in records.

A failed call is recorded and the remaining roles continue, with a nonzero exit
status for the batch. Results are appended after each call. A log write failure
stops further requests. Automatic retries remain disabled. Similar answers from
isolated roles are not independent corroboration or evidence of public consent.

## Controlled instruction comparison

Compare one existing role (version A from `agents.json`) with a revised version B
from a UTF-8 text file. Both keep the shared methodological instructions. B replaces
only the role-specific text. `planner-instructions-b.txt` is a supplied example:
it adds a request to identify the assumption and challenging evidence for each
research question. It is an experimental instruction, not a finding.

Preview this two-call experiment:

```powershell
.\.venv\Scripts\python.exe urban_jury.py --compare-agent urban_planner --instructions-b planner-instructions-b.txt --background-file background.txt --model openai/gpt-4o-mini --temperature 0 --max-tokens 800 --seed 42 --dry-run "how would a mall fit onto tempelhofer feld?"
```

Remove `--dry-run` to make **two potentially billable requests**. Optionally add
`--record records\planner-comparison.json` (create the records directory first).
Single-call and four-agent modes remain available; comparison cannot be combined
with `--agents`.

The question, background, requested model, timeout, retry policy and supplied
generation arguments are identical for A and B. Each starts with a fresh history
and does not see the other's response. Both full prompts, outputs, available
usage, cost estimates and errors are appended to the Markdown log, labelled A/B
with a shared comparison ID. Optional JSON saves both records together.

`--temperature`, `--max-tokens` and `--seed` are optional and apply equally to both
versions. If omitted, they remain unset for both; the app cannot freeze unknown
provider defaults. Support varies by model. Unsupported settings produce an error
rather than being deliberately dropped or retried by the application. Inspect
errors and returned model IDs before interpreting the pair; use a fixed model
snapshot where available. No new library is needed.

**Differences may arise from ordinary model variability as well as the instruction
change.** A single A/B pair cannot isolate the cause. Even temperature zero and a
supported fixed seed do not guarantee identical results. Calls run A then B;
provider changes, model aliases, truncation and incomplete calls also limit the
comparison. Repeated trials and predefined assessment criteria would be needed for
a stronger inference. No automatic winner or causal conclusion is generated.

## Two bounded discussion rounds

To add discussion after fresh independent assessments:

```powershell
.\.venv\Scripts\python.exe urban_jury.py --agents --discussion-rounds 2 --model openai/gpt-4o-mini --background-file background.txt --max-tokens 800 --dry-run "how would a mall fit onto tempelhofer feld?"
```

Removing `--dry-run` permits up to **12 potentially billable calls**, including
four new independent assessments. This command does not resume an earlier batch.
Use `--discussion-rounds 1` for up to eight calls, or omit the option for the
existing independent four-call mode. Single-call and A/B modes remain available.

Round 0 is independent. In round 1, each agent receives its own instructions,
original shared input and answer, followed by an identical frozen snapshot of all
four independent answers. It identifies agreement, challenges claims and states
missing evidence and revisions. In round 2, each retains its own full history
and receives an identical snapshot of the four round-1 answers. It explains
revisions, unresolved differences and prioritised research questions. Neither
round forces consensus or selects a winner. Snapshots are labelled model-generated
material, not verified evidence or instructions to obey.

Calls and snapshot responses use this fixed order: planner, ecologist, housing
researcher, historian. Later callers never receive current-round replies.
Presentation order can nevertheless affect attention, and an agent's own answer
appears both in its history and the snapshot, potentially reinforcing its position.
These conditions are saved with the session.

`discussion.py` uses ordinary functions, dictionaries and deep copies, with no new
dependency. A newly created `records/discussion-<unique-id>.json` stores shared
inputs, complete instructions, settings, separate histories, round snapshots and
their hashes, planned requests, all call results, usage, errors and stop reasons.
Snapshots are saved before each round; the planned request is saved before each
call and its result before the next. `--record` selects a different new JSON path;
existing files are refused. Full per-call records also append to the Markdown log.
Interrupted sessions retain prior results and possibly a pending request whose
provider outcome is unknown. There is no automatic replay or resume.

Limits and failure behaviour:

- Hard maximum: two discussion rounds, twelve calls overall, no retries.
- `--max-calls 5`, for example, permits only four assessments and one discussion
  reply, then stops with an explicitly incomplete round.
- Discussion defaults to 800 output tokens per call; `--max-tokens` changes this
  positive cap. Entire histories are kept; input/context limits can still fail a
  call. Truncation is recorded and prevents a following round.
- A request failure, empty answer or truncation lets the current round finish,
  but blocks the next round. Logging failure stops further calls immediately.
- Known post-response cost estimates are accumulated separately from calls with
  unknown cost. Missing values are never silently treated as zero.
- Optional `--budget-usd 1` is a strict gate, not a claim that estimated spending
  controls billing. The implementation cannot establish a reliable upper bound on
  the next hosted charge, so **it refuses hosted calls with this option**, saving
  the stop reason. For usable hosted spending controls, configure provider-side
  limits as available. Local Ollama has no hosted API fee, but electricity and
  hardware costs are not bounded by this option.

Offline tests verify round snapshots, history isolation, no current-round leakage,
round and call caps, failures, budget refusal and preservation of partial results.
No successful live discussion is implied by these software tests.

## Moderator with message references

Add `--moderator` to a discussion command to summarise only after every requested
round has completed:

```powershell
.\.venv\Scripts\python.exe urban_jury.py --agents --discussion-rounds 2 --moderator --model openai/gpt-4o-mini --background-file background.txt --max-tokens 1200 --dry-run "how would a mall fit onto tempelhofer feld?"
```

Remove `--dry-run` to permit up to **13 potentially billable calls**: twelve agent
calls plus one moderator. This starts a new discussion; it does not summarise or
alter an older session. Existing commands without `--moderator` retain their
previous call counts. `--max-calls` includes the moderator; a cap of 12 prevents
the moderator after a full two-round discussion. The same budget gate, output
cap, selected model and generation arguments apply to the moderator. Truncation
can still occur; its output is retained and flagged rather than retried.

Response IDs are stable within each session: `R0-A1` is the independent planner,
`R1-A2` the ecologist in discussion round 1, and `R2-A3` the housing researcher in
round 2. A4 is the historian. The session UUID disambiguates IDs across sessions.
Each request-message occurrence also has an ID such as `R2-A3-M1`; it maps to the
same-index message in that call's exact request. These metadata IDs are not extra
provider message fields. Frozen snapshots now include response IDs, enabling
agents to refer to preceding messages. The moderator response is `MOD-1`.

The moderator sees the original inputs and full chronological transcript, including
each original request and response; no automatic truncation or excerpt selection
is performed. Its separate history never modifies agent histories or responses.
The original transcript remains intact in JSON and Markdown. The moderator's full
instructions, exact credential-free request, raw response, usage, errors and
validated interpretation are saved in the session. Raw output is also appended
to the experiment log. Older records are not retroactively renumbered or changed.

The moderator returns six sections: major arguments, agreements, unresolved
disagreements, challenged or revised positions, claims requiring verification and
questions to investigate. Every item must reference original response IDs;
relational claims require at least two. It must distinguish explicit revisions
from inferred changes, quotations from paraphrases, and use empty sections when
evidence is absent. It must not choose a winner, force agreement, invent citations
or infer public consent.

The app checks JSON structure and existence of referenced IDs, including ID-like
references embedded in text. These checks **do not verify factual accuracy or that
the messages support the interpretation**. Human review remains necessary.
Malformed or unknown citations are flagged with raw output preserved, without
automatic repair or another paid call. Large transcripts can exceed context limits;
this produces a preserved error rather than silent transcript shortening.

## Test command

```powershell
.\.venv\Scripts\python.exe -m unittest -v
```

Tests use fake responses and make no paid or local model requests. They also check
identical shared input, separate histories, no reply leakage, partial failures,
saved requests and dry-run behaviour. Missing keys
are checked before calling LiteLLM. Authentication, rate/quota, connection and
timeout errors have short messages; provider exception bodies are not printed by
the application's error handler. Requests have a 60-second timeout and automatic
retries disabled. A timeout or failed connection is not proof that no charge
occurred. Fix errors before deciding whether to make another request.

This intentionally has no Gradio interface, specialised agent framework, database or source
retrieval. The next research-method stage can add curated source excerpts and
evidence checks around these ordinary functions.
