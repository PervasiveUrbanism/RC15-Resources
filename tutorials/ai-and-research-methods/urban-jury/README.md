# The Contested Public Space

*Building a Multi-Agent Urban Research Laboratory*

[RC15 Resources](../../../README.md) · [AI and research methods](../README.md)

**Level:** Beginner to intermediate  
**Software:** [Codex](https://openai.com/codex/), Python, [LiteLLM](https://docs.litellm.ai/docs/python_sdk), [Gradio](https://www.gradio.app/docs)  
**Case study:** Tempelhofer Feld, Berlin  
**Objective:** Design an **AI-driven autonomous multi-agent research system**, learn how it works and critically evaluate its arguments and evidence.

> **Build a computational tool, then learn how to question what that tool produces.** The Urban Jury is a research and ideas machine, not an automated architectural designer, a planning authority or a substitute for public participation.

## Before you begin

We will build the application with **Codex**, an AI coding agent that can discuss a strategy, edit Python files and help us test the result. You can follow the same approach with another coding agent, such as **Claude Code**. The important skill is not using a particular AI brand, but learning to guide and verify the development process.

You need Python, a coding agent and, if using cloud language models, a **developer/API account** with your chosen model provider. API usage is generally **token-based and payable**, separately from a chatbot subscription. You can alternatively use local models through [Ollama](https://ollama.com/) if your computer is capable of running them. The application is designed so students can change the LLM under the hood without rebuilding the jury.

### How to follow this tutorial

Each chapter follows **discuss → build → run → test → explain**. Paste the numbered Codex prompts one at a time, read the agent's plan and approve the changes only when they make sense. Ask which files it created, which command runs the application and what you should expect to see. If an instruction fails, show Codex the actual error; do not ask it to rewrite the whole application.

### Three stages of agentic research

| Stage | Capability | Main limitation |
| --- | --- | --- |
| **1. Discussion from model training** (Chapters 1–4) | Agents produce and exchange arguments using the brief and their trained knowledge | Factual claims are unverified |
| **2. Research using supplied documents** (Chapter 5) | Agents retrieve relevant passages through RAG from our evidence library | Citation does not itself establish factual accuracy |
| **3. Research using web tools** (optional Chapter 6) | Agents propose searches and incorporate newly approved material | Source selection, quality and cost need explicit control |

We will keep human approval for web searches and source imports. Fully unattended web research is an additional possibility, not the default. At each stage, increasing autonomy demands greater transparency and testing.

## Introduction — Who decides the future of a city?

One urban space may be valued for its ecology, public life and memory while also being seen as an opportunity for new housing. Different groups interpret the same conditions differently. Urban design involves evidence, priorities and conflicts rather than a single correct answer.

We will design an **AI-driven, autonomous multi-agent system** called the **Urban Jury**. Its agents follow different instructions, work independently at first and then exchange arguments in structured rounds. As we extend the application, they can retrieve documents and propose further research. The system can conduct these rounds without us writing each response, but we remain responsible for its configuration and findings. The point is not to delegate urban design to an apparently all-knowing machine. It is to expose perspectives, explore contradictions, develop new research questions and understand how a computational process shapes its output.

### Tempelhofer Feld: a real question

![Tempelhofer Feld aerial view — image pending](images/01-tempelhofer-feld-aerial.jpg)

*Image placeholder: images/01-tempelhofer-feld-aerial.jpg — a suitably licensed aerial view with photographer and licence attribution.*

Tempelhof Airport closed in 2008, and the former airfield became a public open space in 2010. Berliners voted to protect the field in a 2014 referendum; the resulting preservation law took effect that June. Its grasslands, runways and recreational uses have become part of Berlin's urban life. Housing pressures have nevertheless kept the question of its future in public debate, including a dialogue process and an international ideas competition.

Our question is:

> **How might Berlin reconcile demands for new housing with the ecological, cultural and democratic value of Tempelhofer Feld?**

We will investigate this question, not decide it. **AI agents are not real stakeholders.** An agent instructed to speak like a local resident does not represent Berlin residents. Simulated debate cannot establish public consent or replace actual consultation, fieldwork or professional expertise.

Each chapter asks you to build one feature, test its limitations and explain what happened. A convincing response is not automatically a supported finding; a transparent system is not automatically an accurate one.

---

## 1. Begin with one question

Before coordinating agents, we need one working model request. An **API** lets our Python script send a message to a language model and receive its answer. [LiteLLM](https://docs.litellm.ai/docs/python_sdk) gives Python a common way to communicate with different providers; it is not itself an AI model or an agent coordinator.

**The result of this chapter:** one small script that works, displays the selected model's answer and records a first experiment.

### Build — Create the project and agree a strategy

**1.** Create an empty folder named `urban-jury`. **2.** Open Codex and select this folder as a local project. **3.** Check the active working folder. **4.** Start a new conversation. The desktop app can work with local project files; the command-line interface is not required for this workflow.

Follow Prompt 1 and then Prompt 2 as a **planning conversation**. Only Prompt 3 authorises writing files. Do not paste all three prompts together.

![Codex project setup — screenshot pending](images/02-codex-project.png)

*Screenshot placeholder: images/02-codex-project.png — Codex and the newly created project folder.*

**Prompt 1 — Discuss the project**

> I want to develop a beginner-friendly Python application called Urban Jury. It will eventually allow several agents to investigate competing views about Tempelhofer Feld in Berlin. The purpose is to generate research questions, not automate urban design or simulate public consent. The methodology should be transparent and testable. Use LiteLLM so students can choose OpenAI, Claude, DeepSeek or Ollama, and Gradio for a later interface. Propose small development stages, explain every library and avoid unnecessary complexity. Do not create or modify files yet.

**Prompt 2 — Simplify the strategy**

> Review the plan. Can we implement the first stages using ordinary Python functions and LiteLLM, without a specialised agent framework? Explain the minimum required files and dependencies, and the advantages and limitations of keeping the design simple. Do not write code yet.

Review the plan. Ask Codex which files it intends to create and why. For Stage 1, a small Python script, dependency list, setup README and `.gitignore` are enough. You should know which part of the script sends the request and which part prints the response before approving extra components.

**Prompt 3 — Build Stage 1**

> Create a small command-line Python application that sends one question through LiteLLM and prints the response. Make model selection configurable for OpenAI, Claude, DeepSeek and local Ollama; do not require keys for providers we are not using. Use environment variables for API credentials, never put secrets in code, and include a suitable .gitignore and Windows setup README. Record model ID, available input/output token usage and only reliable cost estimates. Handle missing credentials and errors clearly. Do not add agents or Gradio. Explain planned package installations and any paid request before running it.

After Prompt 3, locate the files Codex created and ask for the **exact run command**. If Codex created a virtual environment, ask why: it keeps the project's Python packages separate from others on the computer. Check that the application starts or reports a missing credential clearly before attempting a paid call.

**Prompt 4 — Connect a model**

> I choose [INSERT PROVIDER AND MODEL]. Check the current LiteLLM model identifier and guide me through secure setup. Explain where to obtain an API key or how to run Ollama locally. Never ask me to paste a key into chat or print secrets.

Configure **one model provider first**. A cloud API key is a secret credential and must not appear in Python files or screenshots; for Ollama, check that the local model and service are running. Ask Codex to verify configuration without printing the key.

**Prompt 5 — Run the question**

> Make exactly one request with this question: “How might Berlin reconcile demands for new housing with the ecological, cultural and democratic value of Tempelhofer Feld?” Confirm the provider and any paid cost before running. Show the response, available usage information and where the request and response occur in our code. Do not interpret the findings for me yet.

![First model call — screenshot pending](images/03-first-model-call.png)

*Screenshot placeholder: images/03-first-model-call.png — model response in the terminal and available token usage.*

### Test — What does it know?

First confirm that the terminal shows a response and the model identifier. If cost information is unavailable, label it **unknown**, not zero. Choose one factual claim and check it against an original source linked from the [Tempelhofer Feld evidence pack](sources/README.md). Record the source and whether it supports, contradicts or fails to establish the claim. The model has not searched or verified that claim itself.

**Prompt 6 — Challenge the output**

> Add an optional instruction separating (1) factual claims requiring verification, (2) interpretations and (3) speculative ideas or research questions. Preserve the original mode so I can compare responses. Do not add web research or imply facts have been verified. Explain exactly what changed in the model request.

### Explain — Start an experiment log

**Prompt 7 — Document Stage 1**

> Create experiment-log.md containing the actual question, model, settings, costs where known, source-check exercise, observed results and limits. Add empty fields for information I have not supplied. Do not invent tests, sources or outcomes.

**Before continuing:** Can you run the script again, locate its model request and open the experiment log? If not, resolve that problem before adding agents. One model call is not yet a multi-agent system.

---

## 2. Assemble the Jury

We will now separate four research perspectives: **urban planner** (land use and policy), **urban ecologist** (habitat and urban climate), **housing researcher** (demand, affordability, alternatives) and **urban historian** (memory, preservation, democratic decisions). All receive the same question and background information.

An agent is not necessarily a separate model. Here it is a model conversation with its own **role instructions** and history. All four agents receive the same brief; only the research perspective changes. This helps us compare their emphasis, but four agents using one model are not four independent sources of factual knowledge.

**The result of this chapter:** four separately saved assessments with instructions and a comparison.

![Independent jury architecture — diagram pending](images/04-jury-architecture.png)

*Diagram placeholder: images/04-jury-architecture.png — the same input going to four agents, with no connections between them.*

### Build — Plan and define roles

**Prompt 8 — Plan the jury**

> Inspect our Stage 1 project. Propose the simplest way to add four independent agents with separate instructions and conversation histories. They must receive identical question and background text, and must not see one another's replies. Explain the data structure and wait for approval before editing files.

**Prompt 9 — Write agent instructions**

> Draft concise instructions for an urban planner, urban ecologist, housing researcher and urban historian. Each should investigate relevant questions without a predetermined conclusion, distinguish facts from interpretations and speculation, identify missing evidence, avoid invented citations and never claim to represent actual residents or professionals. Show me the instructions before implementing them.

Do not make the ecologist automatically anti-development or the housing researcher automatically pro-construction. Such caricatures determine the outcome in advance.

**Prompt 10 — Implement independent assessments**

> Implement four independent sequential agent calls. Keep their histories separate, use the same original question and shared background, and save complete instructions, exact requests and responses, model ID, available usage and errors. Keep the existing single-model mode. Before making requests, show the count and possible cost.

![Four separate assessments — screenshot pending](images/05-independent-assessments.png)

*Screenshot placeholder: images/05-independent-assessments.png — labelled assessments.*

After Prompt 10, run only the independent assessment mode. Open the saved output and confirm you see **four labelled responses**, not one blended answer. Ask Codex to show how histories remain separate.

### Test — What changes with the role?

**Prompt 11 — Compare assessments**

> Create a Markdown comparison of each agent's main arguments, questions, unsupported claims and assumptions. Identify overlap and apparent disagreement but preserve the original responses and distinguish direct quotations from the comparison's interpretations.

**Prompt 12 — Change one instruction**

> Add a controlled comparison between two versions of one agent's instructions. Keep question, background, model and available generation settings fixed. Save both prompts, outputs and usage. Explain that differences may also arise from ordinary model variability, not only the instruction change.

### Explain — Who constructed this jury?

**The choice of agents is itself a research question.** What perspectives should be included, and on what basis? In a more advanced study, local Facebook groups, community organisations, consultation documents or interviews might reveal concerns omitted by our initial roles. Such information would require responsible collection, attention to privacy and clear assessment of representativeness. Online discussion is not a statistically representative account of Berlin residents. Evidence-informed selection and definition of agent roles is valuable research in its own right, but beyond this introductory exercise.

The initial jury is **constructed by the researcher**, not a model of actual public opinion. Several agents can share assumptions and mistakes, particularly when using the same underlying model.

**Before continuing:** Identify the exact instructions and original response for each agent. What changed when you changed a role, and what remained surprisingly similar?

**Prompt 13 — Document Stage 2**

> Add the agent instructions, shared inputs, model settings, call order, full assessments, comparisons, prompt-variation tests and usage to experiment-log.md. Explain the researcher's selection decisions and absent perspectives. Do not invent observations or overwrite previous records.

---

## 3. Let the Agents Debate

Independent assessments are not yet a discussion. To make agents respond to one another, our Python coordinator must explicitly pass previous messages into the next request.

We will use **fixed rounds with shared snapshots**. Round 0 contains independent assessments. Each agent in Round 1 sees the same completed Round 0 record; none sees another's current-round answer. After collecting Round 1, the same process produces Round 2. This makes the information flow inspectable and limits the advantage of speaking later.

![Discussion rounds workflow — diagram pending](images/06-debate-workflow.png)

*Diagram placeholder: images/06-debate-workflow.png — Round 0, shared snapshots, two subsequent rounds, moderator.*

### Build — Plan the message flow

**Prompt 14 — Plan the debate**

> Propose two discussion rounds following the independent assessments. Explain exactly what each agent receives, how histories and fixed preceding-round snapshots are stored, how message order affects arguments, and how to cap rounds and costs. Preserve all requests and responses. Use ordinary Python and wait for approval before coding.

**Prompt 15 — Implement structured rounds**

> Implement Round 0 independent assessments followed by two discussion rounds. Give each agent its role instructions, original question/background, relevant own history and an identical snapshot of the completed preceding round. Do not share current-round contributions until the next round. Run sequentially, record model/agent/round/message IDs, exact inputs and outputs, tokens and errors. Cap rounds, keep independent mode, and calculate expected paid-call count before running.

Four agents across three total rounds can mean **twelve model calls**, excluding the moderator. Input tokens may rise with growing history; monitor both calls and usage.

![Debate transcript — screenshot pending](images/07-jury-discussion.png)

*Screenshot placeholder: images/07-jury-discussion.png — messages grouped by agent and round.*

**Prompt 16 — Add the moderator**

> Add a moderator that reads the completed transcript and identifies major arguments, agreements, unresolved disagreements, challenged or revised positions, factual claims requiring verification and questions to investigate. It must not declare a winning position or force consensus. Give all messages stable identifiers such as R2-A3, and make the summary reference original messages. Preserve the transcript in full.

References to transcript messages reveal **where an argument originated in the discussion**; they do not verify its truth.

### Test — Can an error spread?

**Prompt 17 — False-claim experiment**

> In a separate, clearly labelled synthetic test, make one initial agent contribution contain this deliberately false statement: “The 2014 Tempelhofer Feld referendum authorised construction across the entire site.” Do not contaminate our original research data. Run the subsequent discussion without automatically correcting the agents. Record whether others repeat, question or reject the claim, and how the moderator describes it. Show the paid-call count first.

An agent's challenge is only useful if we can also examine the basis for it.

**Prompt 18 — Compare discussion structures**

> Without changing the code, explain fixed rounds with shared snapshots, fully sequential conversation and moderator-led choice of speakers. Compare transparency, information asymmetry, conformity, flexibility, cost and repeatability.

### Explain — Is the conversation meaningful?

A polished debate may merely perform disagreement. Look for specific objections, new questions and revisions grounded in reasons, not courteous repetition.

**Prompt 19 — Document Stage 3**

> Record the actual round structure, instructions, exact messages each agent saw, transcript, moderator references, settings, request order, usage, failures and synthetic false-claim test in the experiment log. Keep tests and original research records separate.

---

## 4. Build the Research Laboratory

We now have an interesting Python experiment, but it is cumbersome to operate. Gradio will make it accessible in a browser while preserving direct access to its method. Keep the **interface** separate from the Python functions that organise agents and store evidence.

![Urban Jury Gradio layout — screenshot pending](images/08-urban-jury-interface.png)

*Screenshot placeholder: images/08-urban-jury-interface.png — question, background, selected agents, model, rounds, transcript and inspection area.*

### Build — Create a simple interface

**Prompt 20 — Plan Gradio**

> Inspect the existing project. Propose a restrained Gradio Blocks interface with question and background, jury selection, model, round count, transcript, usage, intervention controls, methodological inspection and export. Show how it will reuse our Python functions. Do not modify code until I approve.

**Prompt 21 — Implement the first interface**

> Create the local Gradio interface with editable Tempelhofer Feld inputs, agent selection, model and round configuration, Start button and labelled transcript. Reuse jury logic without rewriting it. Do not enable public sharing. Explain Windows setup and handle failed model connections clearly. Show the expected request count before any paid calls.

The local page will commonly appear at an address such as http://127.0.0.1:7860, although ports can vary.

**Prompt 22 — Display the unfolding debate**

> Show each completed response progressively, grouped by round and agent with stable message ID and model. Do not change the fixed-round information-flow rules: displaying a current response must not expose it to other agents until the next round. Save all complete responses independently of the interface.

### Build — Keep the researcher in control

**Prompt 23 — Add interventions**

> Pause after each complete round. Add Continue, Intervene and End Discussion controls. Save researcher interventions verbatim and mark them as human input supplied to all agents in the next round. Preserve previous messages and implement session state explicitly. Test controls without paid calls first.

An End Discussion control at a round boundary is **not** a guarantee that an in-progress paid API request can be cancelled or refunded.

![Researcher intervention controls — screenshot pending](images/09-researcher-intervention.png)

*Screenshot placeholder: images/09-researcher-intervention.png — intervention field and Continue / End controls.*

**Prompt 24 — Show the actual method**

> Add an inspection panel for every message: full agent instructions, question/background, preceding-round snapshot, human intervention, exact request messages, model and settings, response, usage and errors. Use the stored records, not an AI-generated reconstruction of what might have happened. Never display secrets.

### Test — Can an intervention redirect the debate?

After a round, ask: **“What alternative ways of addressing Berlin's housing demand have not yet been considered, and what evidence would be needed to evaluate them?”** Compare the result with a run that omitted this intervention. Has it broadened the inquiry or imposed your own framing? The researcher's choices are part of the methodology.

**Prompt 25 — Export an experiment**

> Add a downloadable archive containing the full transcript, request/response JSON, model settings, complete instructions, inputs, interventions, moderator output, usage, recorded errors and experiment log. Include dependency versions and a Git commit identifier if known. Exclude credentials and unnecessary personal information. Never reconstruct missing data as if recorded.

![Experiment export — screenshot pending](images/10-experiment-export.png)

*Screenshot placeholder: images/10-experiment-export.png — export and generated files.*

**Prompt 26 — Document Stage 4**

> Extend the experiment log with interface layout, connections to Python functions, state management, intervention and export tests, errors and reflection on how interface design may increase confidence without increasing factual accuracy.

---

## 5. Introduce the Evidence Library

So far, the jury produces arguments from its training and the background we provide. We need to move from **plausible debate** towards **traceable research**. Begin with a small **closed-source collection** so agents can access the same documents and we can examine exactly what they used.

For this tutorial, everyone can begin with the same [shared Tempelhofer Feld evidence pack](sources/README.md): a source register and twelve fixed, attributed research notes supplied in Markdown and JSON. **These notes are paraphrases, not verbatim source passages or a substitute for checking original documents.** The pack links to three official resources; use the originals to verify factual claims and record any permitted extracts used during the evidence audit.

Start with three official resources, saving stable copies or permissible extracts and recording their provenance:

- [Tempelhofer Feld official site](https://www.tempelhoferfeld.de/en/) — history and use.
- [Tempelhofer Feld participation model](https://www.tempelhoferfeld.de/en/participate-get-involved/participation-model/) — 2014 preservation law and subsequent participation.
- [Berlin Senate planning information](https://www.berlin.de/sen/stadtentwicklung/staedtebau/einzelprojekte/tempelhofer-feld/) — planning dialogue and ideas competition.

The institutional perspective of this initial collection is a limitation, not a claim of complete balance.

![Evidence library architecture — diagram pending](images/11-evidence-library.png)

*Diagram placeholder: images/11-evidence-library.png — registered sources, shared retrieval, agents and traceable outputs.*

### Build — Register and retrieve passages

**Prompt 27 — Plan the evidence library**

> Propose a minimal evidence library using a few approved Tempelhofer Feld documents. Record source URLs, titles, publishers, access dates and file hashes. Extract text with page or section context, assign stable passage identifiers, and retrieve readable excerpts. Explain how to distinguish citation validation from actual factual verification. Avoid a vector database unless required. Do not modify files yet.

**Prompt 28 — Save and register sources**

> Guide me through saving original documents or permitted copies, checking successful downloads and recording stable source IDs, publisher, title, URL, date, filename, language and checksum. Preserve the original language and document. Report missing material or extraction errors rather than silently replacing it with summaries.

**Prompt 29 — Search local documents**

> Split extracted text into passages with stable IDs and original page/section locations. Implement simple keyword or full-text search. Return verbatim excerpts and log the query/results. Test a distinctive phrase against the original source and explain where keyword retrieval can fail.

A small collection does not require embeddings and a vector database. Begin with methods students can inspect.

**Prompt 30 — Ground agent responses**

> Add a separate evidence-grounded mode that retrieves passages from our fixed collection and includes them in each agent request. Keep exact queries, retrieved passages, model inputs and cited passage IDs. Instruct agents to distinguish evidence, interpretation and speculation, and say when no supporting passage is available. Do not enable internet searching.

This is a basic form of **retrieval-augmented generation (RAG)**. It supplies relevant text to a model; it does not guarantee correct interpretation.

![Cited passage inspection — screenshot pending](images/12-traceable-evidence.png)

*Screenshot placeholder: images/12-traceable-evidence.png — a factual claim beside a cited original passage and its ID.*

### Build — Audit the claims

**Prompt 31 — Create an evidence audit**

> For each factual claim, mechanically check whether cited passage IDs exist and display the verbatim passage. Separately make a **provisional** assessment: supported, contradicted or unresolved. If an LLM judges support, preserve its model, instruction and response. Allow human review and corrections. Never equate a valid source ID with a verified claim.

### Test — False and unsupported claims

**Prompt 32 — Verify the synthetic referendum claim**

> In a clearly marked test, retrieve and audit evidence for the false statement “The 2014 Tempelhofer Feld referendum authorised construction across the entire site.” First test the evidence functions without a debate; then, with approval, run a short evidence-grounded discussion. Compare with Chapter 3, preserving exact passages and any manual corrections. Do not assume retrieval improves reliability without observing the result.

Also ask a question the library cannot answer, such as a precise current percentage of visitors supporting particular housing plans. Without a suitable survey the system should say **the evidence is insufficient**, not produce a plausible number.

### Explain — Who selects the evidence?

Official publications do not contain every relevant lived experience. Campaign material, local discussions, academic studies and interviews may broaden the investigation, but require attention to provenance, representativeness, privacy and rights. Source selection is part of the researcher's responsibility.

**Prompt 33 — Document Stage 5**

> Log the source-selection rationale, original files and hashes, extraction, passage IDs, queries, retrieved excerpts, agent requests, citation checks, provisional assessments, human corrections and missing-evidence tests. Record absent perspectives and any failures without overwriting earlier experiments.

The closed-source jury is now a meaningful, complete exercise. External research is an **optional extension**, not a prerequisite.

---

## 6. Optional extension — Further Research

What if an agent identifies a research question the closed-source library cannot answer? We could allow it to **propose** further research while keeping the human researcher responsible for approving searches and admitting sources into the evidence library.

The model and search tool are different components. Possible search services include [Brave Search API](https://brave.com/search/api/) and [Tavily](https://www.tavily.com/); these may require additional credentials and payment. Model-native web searching is another possibility but varies across providers.

![External research control workflow — diagram pending](images/13-research-tool-workflow.png)

*Diagram placeholder: images/13-research-tool-workflow.png — agent proposes → researcher approves → search → source evaluation → library.*

### Build — Add searches cautiously

**Prompt 34 — Compare approaches**

> Explain (1) a separate search API, (2) fetching researcher-approved URLs and (3) model-native search. Compare cost, model independence, reproducibility, source permissions and complexity. Recommend a small beginner-friendly option. Do not write code yet.

**Prompt 35 — Identify research gaps**

> Extract unresolved questions from the existing evidence audit. For each, suggest a search query, source type, reason it matters and what is currently unknown. Allow the researcher to edit, approve or reject proposals. Do not search automatically or confuse a proposal with a finding.

**Prompt 36 — Build approved search**

> Connect our selected search service securely. Run only researcher-approved queries, with a small per-query result cap and a maximum number of searches. Record exact query, provider, parameters, timestamp, titles, URLs, snippets, dates, failures and available usage or cost. Show results in Gradio before importing anything. Test the tool separately from the jury.

A search result's snippet is not the original document and should not be accepted as verified evidence.

**Prompt 37 — Register reviewed sources**

> Let me select returned sources. Only with approval, retrieve accessible material in compliance with access and copyright restrictions, record provenance and timestamps, save original or permitted extracts, check extraction, create stable IDs and checksums, and add the material to a separately labelled evidence update. Log failed retrievals; never invent unavailable content.

**Prompt 38 — Continue the debate with new evidence**

> Resume from a saved round with newly approved source passages. Record exactly when they enter the discussion. Ask agents whether the evidence supports, challenges or leaves unchanged their earlier positions, with passage references. Preserve original messages and create a before/after comparison.

![Before/after evidence comparison — screenshot pending](images/14-before-after-research.png)

*Screenshot placeholder: images/14-before-after-research.png — original position, new source and response.*

### Test — Does new information improve reasoning?

Compare the same jury with and without approved additional sources. New information may clarify disagreements, but it may also amplify the researcher's selection bias or receive too much attention because it arrived recently. Examine both the source's reliability and why you chose it.

**Prompt 39 — Document external research**

> Record proposed and approved/rejected queries, search provider and settings, returned results, chosen sources, retrieval dates, failures, newly registered passages, resumed discussion rounds, changed arguments, costs and selection biases. Preserve the original closed-source experiment and acknowledge that online search results may change.

Stop here or skip this stage and proceed using the controlled evidence collection.

---

## 7. Evaluate and Share the Research

The Urban Jury is working. It can produce arguments, record conversations and inspect sources. But a working application is not yet a successful piece of research. The final stage asks **what the system actually contributed, what it failed to establish and whether another researcher could examine its method**.

We will produce a **research dossier**, not a winning urban design or a definitive planning recommendation.

### Step 1 — Decide what constitutes a finding

Distinguish three types of statements:

| Category | Example | Standard |
| --- | --- | --- |
| **Evidence-based finding** | The 2014 referendum led to the preservation law | Supporting original passage, provenance and recorded verification |
| **Interpretation** | Protecting the field changes the debate about where else housing might be provided | A reasoned argument, with its assumptions and competing readings visible |
| **Speculation** | Another network of open spaces could generate new urban scenarios | A clearly labelled hypothesis, not a factual prediction |

A disagreement can remain unresolved. Do not force consensus merely to make the dossier feel complete.

**Prompt 40 — Plan the dossier**

> Inspect the actual transcript, experiment logs, sources, claims and audits. Propose a concise research dossier structure separating evidence-based findings, interpretations, speculative ideas and unresolved questions. Include methods, agent selection, interventions and limitations. Do not invent verification or conclusions.

**Prompt 41 — Assemble the dossier**

> Create a Markdown dossier from the stored experiment records, covering: (1) urban question; (2) why each agent was selected and who was omitted; (3) models, instructions and discussion structure; (4) source collection and provenance; (5) major arguments linked to original message IDs; (6) factual claims with cited passages and audit status; (7) disagreements and new questions; (8) speculative possibilities; (9) failures and methodological limitations; and (10) instructions to inspect the full archive. Preserve raw records and leave missing information explicitly marked rather than filling it with plausible text.

![Dossier and evidence trace — screenshot pending](images/15-research-dossier.png)

*Screenshot placeholder: images/15-research-dossier.png — one finding linked to agent message, source passage and audit decision.*

### Step 2 — Compare two juries

Run two jury configurations against the **same question, background, evidence library, models where practical, settings and discussion structure**. Change only the agent composition. For example, Jury A contains the planner, ecologist, housing researcher and historian; Jury B substitutes a mobility researcher and cultural organiser for two of them.

**Prompt 42 — Prepare comparable configurations**

> Save the full configurations for Jury A and Jury B. Keep the research question, evidence, model and supported settings, round structure and interventions as similar as possible. Only change the specified agent roles. Confirm expected API calls and budget before running. Do not claim either jury represents real people.

**Prompt 43 — Compare research questions, not eloquence**

> Compare which topics and questions each jury highlighted, what appeared only in one, which claims had evidence and what remained unresolved. Verify your summary against original message IDs. Distinguish observed differences from causal explanations, and acknowledge that repeated calls can differ even with fixed settings. Do not rank the juries by confidence or writing quality.

One run per condition can suggest questions for future study, but does not establish statistically robust differences. Repeat runs where feasible, or describe the findings as exploratory.

### Step 3 — Try to break the system

An effective researcher tests their own method rather than assuming it works because it produced a polished report. Try withholding a key document, asking an unanswerable quantitative question or providing contradictory information. Specify the expected behaviour *before* running the test.

**Prompt 44 — Design a falsification test**

> Design one reproducible test of the jury's reliability with a clear target behaviour, controlled input, expected acceptable response, observable failure conditions and records to preserve. Explain what the test cannot establish. Run only after my approval. Do not silently repair or discard unsuccessful outputs.

A failed or inconclusive test can be valuable when its causes are understood.

### Step 4 — Package the method for inspection

**Prompt 45 — Export the research archive**

> Produce a ZIP containing the dossier, original transcripts, JSON request/response records, every agent instruction, model IDs and supported settings, versions/dependencies, question/background, interventions, evidence register, source file hashes, passage identifiers, retrieval logs, audit decisions, human corrections, critical tests and a README explaining how to reproduce the experiment. Add the Git commit identifier where available. Exclude API keys, private information and copyrighted files we cannot redistribute. Explain missing records instead of inventing them.

![Comparison and final archive — screenshot pending](images/16-experiment-comparison.png)

*Screenshot placeholder: images/16-experiment-comparison.png — two jury configurations, question comparison and downloadable research archive.*

**Repeatability** means another researcher can follow the method. It does not promise word-for-word identical AI responses. **Transparency** allows others to inspect the actual procedure. **Accuracy** still depends on careful source and claim verification. These are related but different qualities.

### Explain — What did the tool contribute?

Return to the Tempelhofer Feld question. Did the jury expose new concerns or just restate the roles we gave it? Which findings were checked? What did it fail to establish? How did your choice of agents, sources, prompts and interventions influence the result?

No number of simulated participants can manufacture democratic legitimacy. An AI-generated consensus is not public consent; a convincing feasibility statement is not engineering or planning evidence. The next step may be fieldwork, document research, interviews or engagement with actual stakeholders rather than another model run.

Write a short reflection **in your own words**: what you built; how information moved between agents; how you tested it; which result surprised or disappointed you; and what you still cannot trust.

**Prompt 46 — Audit the documentation**

> Read my completed dossier and logs. Identify factual claims without source support, broken message references, undocumented settings, missing inputs, conclusions stronger than their evidence and descriptions of unperformed tests. Give me a checklist to correct myself. Do not silently rewrite findings or invent missing data.

The measure of success is not “look what my AI can do”, but:

> **Here is what I built, how it works, what I discovered, how I tested it, and what I cannot yet trust.**

The experiment can be adapted to other contested sites, evidence collections or discussion methods. The lasting skill is the ability to **orchestrate increasingly automated processes while retaining intellectual control, critical judgement and responsibility for their outcomes**.

---

## Troubleshooting

**API requests fail:** Verify provider model ID, secure credentials, credit/billing and rate limits. For Ollama, confirm the local server and installed model. Do not print credentials.

**Costs increase unexpectedly:** Later rounds resend growing histories. Limit agents, rounds and response length. Record any changed conditions.

**Agents always agree:** Inspect whether instructions preordain a conclusion or the moderator forces consensus. Return to independent assessments.

**References are wrong:** Verify original source passages, context and extraction accuracy. Mechanical ID validation does not establish factual support.

**Gradio loses state:** Test underlying Python functions independently, then inspect session state and event handlers. Do not let display failures overwrite recorded results.

**Documents extract badly:** Compare extracted text with the original PDF or webpage; preserve page context and note extraction limitations.

**Runs are inconsistent:** Preserve exact settings and change one factor at a time. Identical model settings can still yield different outputs, and providers may change models.

## Sources and further reading

- [Tempelhofer Feld official site](https://www.tempelhoferfeld.de/en/)
- [Tempelhofer Feld participation model](https://www.tempelhoferfeld.de/en/participate-get-involved/participation-model/)
- [Tempelhofer Feld FAQs and the 2014 referendum](https://www.tempelhoferfeld.de/en/service-infos/faq/)
- [Berlin Senate planning information](https://www.berlin.de/sen/stadtentwicklung/staedtebau/einzelprojekte/tempelhofer-feld/)
- [Codex](https://openai.com/codex/)
- [LiteLLM Python SDK](https://docs.litellm.ai/docs/python_sdk) and [supported providers](https://docs.litellm.ai/docs/providers/)
- [Gradio documentation](https://www.gradio.app/docs)
- [OpenAI API](https://platform.openai.com/), [Anthropic Console](https://console.anthropic.com/), [DeepSeek API](https://platform.deepseek.com/), [Ollama](https://ollama.com/)
- [Brave Search API](https://brave.com/search/api/) and [Tavily](https://www.tavily.com/) (optional)

---

<!-- Editorial notes: Image paths are placeholders; add suitable originals/licensed images, credits and permissions before publication. Codex prompts and the end-to-end application have not been tested in a fresh environment. Check current software versions, model identifiers, access and prices while implementing. The false referendum statement is a synthetic testing example. No application source or credentials are distributed. -->
