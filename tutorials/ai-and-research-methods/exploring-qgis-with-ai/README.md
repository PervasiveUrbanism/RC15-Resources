# Exploring QGIS with AI: From Open Data to Spatial Analysis

*Find data in an unfamiliar language, investigate it with ChatGPT and turn it into a map through Codex and QGIS.*

[RC15 Resources](../../../README.md) · [AI and research methods](../README.md)

**Level:** Beginner  
**Software:** ChatGPT, QGIS, Codex desktop, QGIS MCP, uv (Windows instructions)  
**You will learn:** How to discover and assess an unfamiliar dataset, connect an AI agent to QGIS and inspect the spatial operations it performs.  
**Tested workflow (18 November 2026):** QGIS 3.40.13, QGIS MCP plugin 0.15.3, Codex desktop on Windows. Connection, WFS loading and species-based styling were demonstrated in practice. Interface details may change.

![Berlin street trees coloured by species in QGIS](assets/images/Screenshot%202026-11-18%20224744.png)

## A city full of data — in a language you do not speak

Suppose you want to investigate the trees along Berlin's streets. The city publishes extensive open data, but much of its catalogue is written in German. You may not know the right search terms, how the data is organised or whether it can be used in QGIS.

Instead of starting with software menus, we will start with a question. ChatGPT will help us search the [Berlin Open Data catalogue](https://daten.berlin.de/), interpret its German descriptions and compare possible datasets. We will then use **Codex** to communicate with QGIS and explore the data on a map.

These are two different uses of AI. ChatGPT helps us **find and evaluate information**; Codex uses tools to **act on an open application**. Neither removes the need to understand the data or check the results.

## 1. Find a dataset with ChatGPT

Open [Berlin Open Data](https://daten.berlin.de/). You do not need to translate the whole website. Instead, open ChatGPT and describe what you are investigating:

> I'm investigating urban trees in Berlin. Explore the official Berlin Open Data website at https://daten.berlin.de/ and identify datasets that might help me understand the distribution of trees across the city.
>
> The website is in German, which I don't speak. Search using the original German terminology, but explain your findings in English.
>
> Propose several relevant datasets. For each one, explain what it contains, its geographic coverage, available formats and possible uses. Include a link to the original dataset page.

Notice that we have given ChatGPT a **research question**, not a German keyword. It needs to translate the intent of the question into terms such as *Baumbestand* (tree inventory), *Straßenbäume* (street trees) and *Anlagenbäume* (trees in managed green spaces).

During our investigation, ChatGPT identified the [Baumbestand Berlin — WFS](https://daten.berlin.de/datensaetze/baumbestand-berlin-wfs-48ad3a23) as a promising source. It describes street trees and some trees in public green spaces, rather than every tree in the city.

![Berlin's German-language tree inventory catalogue page](assets/images/Screenshot%202026-11-18%20225136.png)

### Ask what the data actually contains

A dataset's title is not enough to tell us whether it answers our question. Continue the conversation:

> Investigate the Berlin tree inventory WFS dataset. What attributes are available for each tree? Can we identify species, age, height, trunk diameter or planting year?
>
> Distinguish fields documented by the publisher from values you have verified in the actual records. Suggest three simple investigations we could carry out in QGIS.

The [publisher's field documentation](https://gdi.berlin.de/data/baumbestand/docs/Datenformatbeschreibung_Baeume.pdf) describes attributes including botanical and German species names (`art_bot`, `art_dtsch`), planting year (`pflanzjahr`), tree height (`baumhoehe`), trunk circumference (`stammumfg`) and crown diameter (`kronedurch`). Field names and their completeness should be checked against the layer that actually loads.

This distinction matters: a documented field does not mean that every tree has a value. Nor does a tree inventory measure all urban vegetation. We will begin with **species**, because it produces an immediately legible map, and return to more demanding questions later.

## 2. What is QGIS MCP?

[QGIS](https://qgis.org/) is an open-source geographic information system: it stores, displays and analyses information associated with locations. Normally you operate it through menus, tools and attribute tables.

**MCP** stands for *Model Context Protocol*. It lets an AI client discover and call tools exposed by another application. In our example, a QGIS plugin communicates with a local MCP server launched by Codex. Codex can then inspect layers, change their appearance and request other QGIS operations.

The connection has two parts: **the plugin running inside QGIS**, and **the MCP server process launched by Codex**. Installing one does not automatically configure the other.

The software can modify an open project, so begin with a new or disposable QGIS project. Keep a copy of any important work. In the prompts below, we ask Codex to inspect first and make only specific, limited changes.

## 3. Install and connect QGIS MCP

### Install the QGIS plugin

Open QGIS and choose **Plugins → Manage and Install Plugins**. Search for **QGIS MCP** by Nicolas Karasiak and install it.

![QGIS MCP in the plugin manager](assets/images/Screenshot%202026-11-18%20221651.png)

Open **QGIS MCP — Setup & Configurator** from the plugin menu. Choose **codex** as the AI client. In our test, the QGIS-side server was running on port `9876`; you may choose to start it automatically whenever QGIS opens.

![QGIS MCP configurator showing the running local server](assets/images/Screenshot%202026-11-18%20221808.png)

### Install uv on Windows

The Codex-side server is launched using `uvx`, a command supplied with the [uv Python tool manager](https://docs.astral.sh/uv/). On Windows, open PowerShell and install uv with:

```powershell
winget install --id astral-sh.uv -e
```

Close and reopen PowerShell, then check:

```powershell
uvx --version
```

A version number means Windows can find the command. You do **not** need the Codex command-line interface for the graphical setup below.

### Register the MCP server in Codex

In the Codex desktop application, open **Settings → Plugins → MCPs → Add → Custom MCP** (the exact labels may vary). Select **STDIO** and enter:

| Field | Value |
| --- | --- |
| Name | `qgis_mcp` |
| Command to launch | `uvx` |
| Argument 1 | `--from` |
| Argument 2 | `https://github.com/nkarasiak/qgis-mcp/archive/refs/heads/main.zip` |
| Argument 3 | `qgis-mcp-server` |
| Environment variables | Leave empty |

Each argument belongs in its **own field**, in the order shown. These settings reproduce the command supplied by the QGIS plugin without requiring the Codex CLI.

![Codex's STDIO MCP configuration form](assets/images/Screenshot%202026-11-18%20222605.png)

![The registered QGIS MCP command and arguments](assets/images/Screenshot%202026-11-18%20223510.png)

Save the configuration, confirm that `qgis_mcp` is enabled, and restart Codex if necessary. Keep QGIS open.

### Test the connection before editing anything

In a new Codex conversation, ask:

> Connect to my running QGIS application using the QGIS MCP tools. Check whether the connection works. Report the QGIS version, current project name, coordinate reference system (CRS) and list of loaded layers. Do not modify the project or create any layers.

In our test, Codex correctly reported QGIS **3.40.13**, the existing project and its **EPSG:3857** coordinate reference system, together with four loaded layers. This established that the tools were actually communicating with QGIS.

![Successful read-only QGIS connection test in Codex](assets/images/Screenshot%202026-11-18%20223935.png)

A **CRS** specifies how locations on the Earth are represented as coordinates. EPSG:3857 is commonly used for web maps. Later analyses involving distance or area may require a more suitable projected CRS.

### If Codex cannot see QGIS

During testing, we encountered two different problems:

- **`codex` not recognised in PowerShell.** The Codex CLI was not available. We avoided that dependency by using the desktop application's MCP configuration form instead.
- **`uvx` not recognised, or the MCP tools unavailable.** The QGIS plugin was running and the Codex entry was enabled, but the required launcher was not available. Installing uv and restarting the relevant applications resolved the connection in our test.

![PowerShell cannot find the Codex CLI](assets/images/Screenshot%202026-11-18%20221942.png)

![PowerShell cannot find uvx](assets/images/Screenshot%202026-11-18%20223553.png)

If the connection still fails, verify that QGIS is open, its plugin server is running, `uvx --version` works in a new terminal, and the Codex arguments are entered separately. A server shown as *enabled* in settings is not proof that its tools have started successfully.

## 4. Load Berlin's trees into QGIS

We can now use the dataset discovered in ChatGPT. It is provided as a **WFS** (*Web Feature Service*), which supplies geographic features and associated attributes. Unlike a **WMS** (*Web Map Service*), which primarily supplies rendered map images, a WFS can provide individual tree features for inspection and analysis.

Open a new QGIS project, then give Codex this prompt:

> Connect to my open QGIS project using QGIS MCP.
>
> Load the Berlin tree inventory from this official WFS service:
>
> https://gdi.berlin.de/services/wfs/baumbestand
>
> First inspect the available feature types and identify the layer containing individual tree locations. Then load that layer into QGIS.
>
> Do not modify any existing layers. Report the layer name, coordinate reference system, available attributes and whether the data loaded successfully. Do not apply styling yet.

In our test, the layer loaded successfully. A live WFS may take time to respond, especially for a city-wide inventory. If it is slow, ask Codex to work with a smaller extent, or use QGIS's native WFS tools to verify the connection. The AI route is a convenience, not the only way to load the data.

## 5. Map tree species

A map becomes useful when its appearance expresses an attribute of the data. **Categorised symbology** assigns a symbol to each distinct value of a field. Here, the field is the tree species.

Ask Codex:

> Using QGIS MCP, inspect the Berlin tree inventory layer currently loaded in QGIS.
>
> Identify the attribute containing tree species and calculate the ten most frequently recorded species, excluding missing or empty values.
>
> Apply categorised symbology to the layer. Give each of the ten most common species a distinct, clearly distinguishable colour. Display all remaining species in light grey. Use small circular point symbols suitable for viewing at city scale and make them slightly transparent to reduce visual clutter.
>
> Do not modify the underlying data or any other layers. Report the attribute used and the ten most common species with their feature counts.

![Berlin street trees displayed using species-based colours](assets/images/Screenshot%202026-11-18%20224744.png)

The result is a city-wide map in which species appear as different colours. At this scale, neighbouring tree symbols can merge into continuous bands along streets. This reveals a pattern, but makes individual trees difficult to distinguish.

Open the layer's **Properties → Symbology** in QGIS. Look at the categorised renderer, the selected attribute and the symbol colours. Codex has configured a standard QGIS operation, not created a mysterious AI-only visualisation. You can edit it manually.

For more on choosing colours for categorical maps, see [Choosing Colours with AI](../choosing-colours-with-ai/README.md).

## 6. Move from a city-wide map to a local question

Zooming in changes what you can observe. Try a neighbourhood around Alexanderplatz:

> Using QGIS MCP, zoom to the area around Alexanderplatz in central Berlin, approximately 1 km across.
>
> Keep the existing species-based symbology, but adjust the point sizes if necessary so individual trees can be distinguished. Do not change the underlying data.
>
> Report how many tree features are visible in the selected area and identify the three most common recorded species there.

![Closer view of the Berlin tree inventory after the neighbourhood investigation](assets/images/Screenshot%202026-11-18%20225122.png)

Ask Codex to explain **how it determined which trees were inside the area**. A count of features in the current map extent is not the same as a count inside a precisely defined 1 km boundary. If you need a defensible comparison, create a defined study-area polygon and use a spatial selection or filter.

A colourful map is a starting point, not yet an explanation. Are certain species concentrated on particular streets? Does the inventory cover all streets equally? Could planting policies, maintenance or recording practices help explain what you see?

## 7. Continue with your own investigation

The same tree inventory offers other questions. You could map planting years to investigate the distribution of older and younger recorded trees, or use crown diameter to draw approximate canopy circles. A circular buffer around a tree is **not** a measured canopy footprint; it is a geometric model based on one recorded attribute.

Alternatively, return to [Berlin Open Data](https://daten.berlin.de/) and choose a different subject: transport, noise, buildings or urban climate. Begin with a question in your own words. Ask ChatGPT to search the German catalogue, compare sources and explain their limitations. Then use Codex and QGIS MCP to explore the data, checking the operations and results as you go.

The important skill is not memorising a sequence of prompts. It is learning to **formulate a question, evaluate a source, direct a tool and take responsibility for what the map claims**.

## Sources and tools

- [Berlin Open Data catalogue](https://daten.berlin.de/)
- [Baumbestand Berlin — WFS dataset](https://daten.berlin.de/datensaetze/baumbestand-berlin-wfs-48ad3a23)
- [Berlin tree inventory field documentation (PDF)](https://gdi.berlin.de/data/baumbestand/docs/Datenformatbeschreibung_Baeume.pdf)
- [QGIS MCP by Nicolas Karasiak](https://github.com/nkarasiak/qgis-mcp)
- [QGIS documentation](https://docs.qgis.org/)
- [uv installation documentation](https://docs.astral.sh/uv/getting-started/installation/)

*The screenshots document one tested Windows session. Software interfaces, datasets and service availability may change. Check the current publisher documentation and the data returned by your own QGIS project.*
