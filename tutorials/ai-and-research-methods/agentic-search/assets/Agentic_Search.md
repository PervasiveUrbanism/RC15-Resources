# Agentic Search
### RC15 – Pervasive Urbanism



## What Is Agentic Search?

For most of the history of computing, search meant something precise and bounded. You submitted a query, the system matched it against a defined index, and returned a ranked list. The logic was deterministic — the same input, the same output. A well-organised answer to a well-formed question. Google, at its core, still works this way.

Agentic search occupies a different position. It still searches the web, but you don't define the sources, the path, or the method in advance. Instead, you give the agent a task and a perspective — a brief. It decides where to look, judges what it finds, and filters results accordingly. The instructions are not a fixed procedure. They define an intention, and the agent figures out the rest.

This puts agentic search somewhere between retrieval and simulation. It doesn't just fetch what exists — it interprets, on behalf of a particular point of view. And because it can run repeatedly, adapting to new information each time, it moves with the world rather than describing it from a fixed moment.

For urban research, this distinction is significant. A static dataset gives you a snapshot. An agent gives you something closer to a living reading — one shaped by a specific perspective, at a specific time. It shifts the question from *what exists* in a city to *what becomes possible for someone, here, today*. Less a search tool, more a device for simulating behaviour.



## How It Works

An agent has three components: a reasoning engine (typically a large language model), memory (to retain context across runs), and tools (the actions it's permitted to take). In our setup, the main tool is web search, though agents can also read emails, check timetables, access files, or interact with online services.

What drives the agent is the **brief** — a document you write that defines who the agent represents, what it's looking for, and how it should judge relevance. But the brief does more than describe a task. It also governs how the agent responds.

This is where format becomes part of the instruction. You can ask the agent to return plain text, a structured CSV with specific column headers, a bullet-pointed summary, or any format in between. If you need the output to feed into a map, a spreadsheet, or a simulation, you define that structure in the brief — and the agent will follow it consistently across every run. This is sometimes called **governance**: the brief doesn't just tell the agent what to find, it tells the agent how to behave and how to report back.

Because the agent runs repeatedly, the brief can evolve. You refine it as you understand better what kinds of results you're after — adjusting not only the task, but the shape of the answer.



## From Brief to Behaviour

Writing a brief means taking a position. You decide who is acting, what they want, and how results should be presented.

A teenager reads the city differently from an elderly resident. A tourist looks for landmarks; a local might search for novelty within the familiar. Budget, mobility, and social habits all change what the city offers. Once you define these parameters, the agent filters the world accordingly.

But the brief itself doesn't have to be written by hand. An LLM can generate it. You can describe a persona in loose terms and ask the model to produce a fully structured brief — complete with behaviour, filters, and output format. This opens up something interesting: if brief-writing can be automated, so can agent-creation.

Imagine feeding a set of Facebook groups, travel blogs, or nationality-specific guides into a language model and asking it to extract distinct personas from them — the budget backpacker, the expat family, the elderly cruise tourist, the local student. Each becomes a brief. Each brief becomes an agent. Suddenly you're not running one search, you're running many, simultaneously, each reading the city from a different position.

The format of the output matters here too. A structured, consistent output can feed directly into maps, diagrams, or simulations — turning a prompt into something durable and replicable. And because the briefs share a common structure, their outputs can be compared, layered, and analysed together.

This is where agentic search starts to feel less like a tool and more like a method — a way of systematically multiplying perspectives on the same place.



## Case Study: A Daily Routine in Castello, Venice

To make this concrete, we construct a daily agent for a fictional young resident.

**Tomaso** is eighteen. He lives in Castello and moves through the city on foot. His budget is tight. He likes spending time with friends, listening to music, and being near the energy of the city — not formal exhibitions or expensive events, but whatever is actually happening around him.

Each morning at 9:00, the agent asks: *What might attract Tomaso today? Where could he realistically go?* The output is not a comprehensive cultural calendar — it's a selective reading filtered by walkability, cost, and atmosphere. A small proposal for how the city might unfold for one particular life.



## Setting Up an Agent in ChatGPT

There are many tools that support agentic workflows — n8n, Zapier, Make, or OpenClaw, to name a few. These platforms offer powerful automation and integration capabilities, but they come with a steeper learning curve and more technical setup. For this exercise, we keep the technical side minimal and work directly inside ChatGPT.

Before getting started, it's worth understanding the two main ways to access these systems. The **consumer model** — which is what we use here — means a fixed monthly subscription. ChatGPT Plus costs a flat fee regardless of how much you use it. The workflow is more manual, but the costs are predictable and the interface is accessible without any programming knowledge. The **developer model** works differently: you pay per use, through an API. This unlocks more automation and scalability, but costs become harder to predict and the setup requires technical knowledge.

We choose the consumer route deliberately. It delivers around 80% of the results for 20% of the effort — and for the purposes of understanding agentic search conceptually, that trade-off is exactly right.

It's also worth noting that ChatGPT is not the only option. Claude (Anthropic) and Gemini (Google) offer comparable capabilities and could be used in the same way. The principles of the brief, the governance, and the output structure remain identical regardless of which system you choose.

> **Note:** To follow this exercise you will need a **ChatGPT Plus** subscription.

### Step 1 — Write the Brief

The brief is the core of the agent. It defines who the agent represents, what conditions shape their world, what would count as a useful result, and how the output should be structured. Everything the agent does flows from this document.

Here is the brief we use for Tomaso:

```
## Agent Brief – Daily Life in Castello, Venice

This agent represents a fictional resident called Tomaso.

Tomaso is eighteen years old. He lives in Castello and moves through the city on foot. His budget is limited. He enjoys meeting friends, listening to music, and spending time where other young people are. Traditional museums or formal cultural events are usually less attractive to him, but he likes to stay aware of what is happening around him.

Its task is to identify situations, events, or places that Tomaso could realistically visit today. The goal is not to create a complete overview of Venice. The goal is to filter the city according to Tomaso's life conditions, interests, and mobility.

The agent should prefer places that are reachable by walking, financially accessible, and socially relevant for someone of his age.

The result should read like a proposal for how his day could unfold.

---

## Expected Output

Return results as a CSV block using exactly these headers:

name,category,time,latitude,longitude,why_it_fits_tomaso

- name: name of the place or event
- category: concert / hangout / public event / street performance / outdoor / other
- time: time or time range if known, otherwise "flexible"
- latitude / longitude: geographic coordinates
- why_it_fits_tomaso: one or two sentences from Tomaso's perspective

Return between 5 and 8 entries. Do not add commentary outside the CSV block.

---

## Attitude of the Agent

The agent is not neutral or universal. It speaks from Tomaso's perspective.
It should make assumptions, prioritise, and filter.
The aim is to simulate how the city becomes meaningful for a specific person.

---

## Feedback from previous runs

Use the following annotated results to refine your judgement.

name,category,time,latitude,longitude,why_it_fits_tomaso,feedback
"Via Garibaldi","hangout","afternoon","45.4326","12.3542","Local strip, young crowd","good - keep this type"
"Museo Correr","museum","10:00–18:00","45.4341","12.3358","Central location","too formal - exclude museums"
```

Save the brief as a versioned file:

```
Agent_Brief_Tomaso_v1.md
```

### Step 2 — Create a Scheduled Task

> *The following workflow reflects ChatGPT Plus as of spring 2026. The interface may change over time.*

To set up the agent, open a new chat in ChatGPT Plus and ask it to create a scheduled task. Paste the brief directly into the conversation — this becomes the instruction. Set the task to run once daily at a chosen time. ChatGPT will execute it automatically, search the web, and return a structured CSV response each morning.

To refine the task over time, go to **Settings** and find your scheduled tasks. Open the task and update the brief directly there — adjusting the persona, the filters, or pasting in an updated feedback CSV with your annotations from previous runs. This is how the agent improves: not automatically, but through your own observations folded back into the instructions.

---

## Reading the Output

The agent's response is intentionally limited. It doesn't aim for completeness — it aims for relevance. Each entry in the CSV describes a place, event, or situation Tomaso could plausibly engage with today, along with a short justification written from his perspective.

```csv
name,category,time,latitude,longitude,why_it_fits_tomaso
"Regata de Carneval su Mascarete a due remi","public event","09:30–11:00","45.4322517","12.3365389","Sunday morning energy, costumes, people watching — free to watch, easy to join as a walk-by."
"Palco di Piazza San Marco","street show","11:00–19:00","45.434185","12.337817","Big crowd, constant activity — good for meeting friends without committing to anything."
"Venice Carnival Street Shows","street performances","varies","45.4369000","12.3411000","Wander with friends, follow noise and crowds, catch short acts — no ticket, no pressure."
"Via Garibaldi","hangout / social street","late morning–afternoon","45.4326000","12.3542000","Castello's most local-feeling strip — friends, cheap drinks, young people passing through."
"Giardini della Biennale","outdoor / park break","afternoon","45.428818","12.356828","When Carnival gets too intense: space to sit, talk, and reset without spending money."
"Arsenale Water Show","night show","18:45 or 21:00","45.433188","12.351705","Big spectacle right next to Castello — get a good spot early with friends."
"Parco Villa Groggia","low-key hangout","late afternoon","45.4480183","12.3276783","Calmer option if the group splits — local, relaxed, very non-touristy."
```

When information is incomplete, the agent still makes a reasonable judgement. The result reads less like a schedule and more like a proposal.

---

## Refining and Scaling

The first output is rarely the final one. After seeing results, you refine the brief — sharpening interests, adjusting constraints, shifting priorities. Each change alters the agent's behaviour, sometimes subtly, sometimes dramatically. The process becomes one of designing a perspective.

Once you're comfortable with a single persona, the method scales. Change the age, mobility, or daily rhythm and the same city reads completely differently — through the eyes of a tourist encountering it for the first time, a young parent navigating it with a child, or a long-term resident negotiating familiarity and change.

What you're building, ultimately, is not a search tool. It's a method for multiplying viewpoints on the city.

---

*When you start constructing your own agents, you'll quickly notice how sensitive the outcomes are to initial assumptions. Small adjustments in age, interest, or mobility can reorganise the entire landscape of possibilities. To design an agent is to articulate a position — to decide how the world should be read.*
