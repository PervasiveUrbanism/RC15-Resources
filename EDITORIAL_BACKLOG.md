# RC15 Resources — Editorial Backlog

This is the working to-do list for the long-term development of **RC15 Resources**. The library is organised primarily by **subject and learning outcome**, not by individual software packages; software indexes provide secondary routes to the same tutorials. The main [README](README.md) is the student's entry point and should ultimately become an **illustrated table of contents**.

We will improve the library **one tutorial at a time**. Preserve useful existing material, avoid unnecessary restructuring, and keep tutorials independent of any single teaching year. A dedicated website is a possible future publication format, **not a current task**.

**Audit baseline:** 25 October 2026, `main` branch. Effort estimates below are based on an inspection of the repository structure, tutorial READMEs and selected notebooks. They are **provisional**: PDF contents and native vvvv, Rhino, Grasshopper, Arduino and QGIS projects have not yet been tested in their applications.

## How to use this backlog

- **A — Light polish:** substantial teaching content already exists; review language, illustrations, metadata, references and technical accuracy.
- **B — Moderate revision:** a useful explanation or guide exists, but the learning sequence, reproducibility or technical detail needs more work.
- **C — Major development:** valuable examples are present, but they still need a coherent, substantial tutorial.
- **Wishlist:** potential new resources, separate from improvements to existing material; scope and priority still need agreement.

**Effort is not difficulty or priority.** A sophisticated advanced exercise may be well documented; a simple patch may lack any explanatory material. Keep these separate when planning work.

For each tutorial, aim for: a clear purpose and learning outcome; prerequisites and tested software versions; an explanation of the underlying method; steps that can be reproduced; relevant **images of actual results**; working examples and data; interpretation, experimentation and troubleshooting; source/asset credits; and links back to the subject index. Follow [CONTRIBUTING.md](CONTRIBUTING.md) for the maintenance checklist.

## Immediate repository checks

These are comparatively small tasks (except any credential incident) and do not need to wait for a complete tutorial revision.

- [ ] **Check for exposed credentials** in the legacy modularisation example (`Xtra 01 - Modularise the code/`, including `Passwords.py` and `passwords.csv`). Determine whether values are dummy examples or real secrets. If real, **revoke/rotate them immediately** and plan remediation of Git history; deleting the current files alone would not remove prior exposure. Do not copy credential values into documentation.
- [ ] **Fix navigation to LED Control**: the topic/software indexes refer to `led-control/README.md` but the actual file is `Readme.md`. Standardise the filename and links, checking case sensitivity.
- [ ] **Fix image paths in Agentic Search**, where some Markdown image references use Windows backslashes instead of portable forward slashes; verify they render in GitHub.
- [ ] **Check technical statements** flagged during review: raster cell size/coordinate units in the Heatmaps tutorial, and UV mapping, geometric closure and fabrication claims in Flow Along Surface.
- [ ] Review committed `__pycache__` bytecode, `wip/` files, rendered frame sequences and backups. Decide deliberately which assets must be kept; do not delete reference files without inspection.
- [ ] Add reproducibility notes where needed: software/package versions, external data sources, hardware assumptions and file paths.
- [ ] Check links, image attribution, third-party data permissions and referenced downloads.
- [ ] **Standardise the library name**: the main README and many tutorials say “RC15 Extended Knowledge”, while the repository is “RC15 Resources”. Agree on the public-facing name before changing it throughout.
- [ ] Develop the [main README](README.md) into an **illustrated, subject-first contents page** using representative outputs from our own tutorials, while keeping the software index secondary.
- [ ] Review each [subject index](tutorials/) and [software index](software/) for clear links, logical prerequisites and useful cross-references. Maintain one authoritative copy of each tutorial.

## Existing tutorials — review and polish

The groupings below follow the **current repository structure**, not a proposed reorganisation. No item should be marked complete until its underlying example has been checked where practical.

### Mapping and spatial analysis

- [ ] **A · [Network Mapping in QGIS](tutorials/mapping-and-spatial-analysis/network-mapping/README.md)** — Polish a strong illustrated guide; verify routing assumptions, example settings and independently obtainable street data.
- [ ] **B · [Heatmaps in QGIS](tutorials/mapping-and-spatial-analysis/heatmaps/README.md)** — Refine the technical instructions, raster-unit terminology, presentation graphics and workflow from density raster to points/contours.
- [ ] **C · [QGIS to Rhino](tutorials/mapping-and-spatial-analysis/qgis-to-rhino/README.md)** — Explain the cross-software workflow around existing QGIS, Rhino and Grasshopper files; clarify what each stage produces.
- [ ] **C · [Flickr Mapping in Rhino and Illustrator](tutorials/mapping-and-spatial-analysis/flickr-mapping/README.md)** — Turn the four Grasshopper steps and Illustrator outputs into a reproducible data-to-graphics tutorial; review data/API availability.
- [ ] **C · [Visibility and Viewshed Analysis](tutorials/mapping-and-spatial-analysis/viewshed-analysis/README.md)** — Write a tutorial using the supplied terrain data, QGIS project and processing model, with an explanation of visibility assumptions.

### Data analysis and machine learning

- [ ] **A · [Introduction to UMAP](tutorials/data-analysis-and-machine-learning/umap/README.md)** — Review the substantial notebook (conceptual explanations and worked examples), environment setup, dependencies, figures and output interpretation.
- [ ] **B · [GSR to UMAP](tutorials/data-analysis-and-machine-learning/gsr-to-umap/README.md)** — Connect the two notebooks into a clear sequence from sensor signal to features and embedding; examine assumptions, file paths and reproducibility.
- [ ] **C · [Sound Analysis in vvvv](tutorials/data-analysis-and-machine-learning/sound-analysis/README.md)** — Develop a written guide explaining the supplied patch, expected input and analysis/visual output.

### AI and research methods

- [ ] **B · [Agentic Search](tutorials/ai-and-research-methods/agentic-search/README.md)** — Retain the strong conceptual narrative, but verify product-specific instructions, avoid outdated subscription claims, fix images and strengthen source checking, feedback and output validation.

### Geometry and modelling

- [ ] **B · [Flow Along Surface in Rhino](tutorials/geometry-and-modelling/flow-along-surface/README.md)** — Preserve the illustrated walkthrough; verify the `FlowAlongSrf`/`CreateUVCrv` steps, surface parameterisation, history behaviour and claims about closed geometry.
- [ ] **C · [Reading Point Clouds](tutorials/geometry-and-modelling/reading-point-clouds/README.md)** — Explain formats, loading the sample point cloud, spatial scale, performance and visual output.
- [ ] **C · [Rhino and Grasshopper Import into vvvv](tutorials/geometry-and-modelling/rhino-grasshopper-import/README.md)** — Organise the Rhino, Grasshopper and vvvv samples into a progressive interoperability tutorial; inspect the animation frames and dependencies.
- [ ] **C · [Signed Distance Fields](tutorials/geometry-and-modelling/signed-distance-fields/README.md)** — Explain the mathematical idea and the five numbered vvvv examples, using clear diagrams of the resulting shapes and transformations.

### Visualisation and rendering

- [ ] **B (provisional) · [D5 Render](tutorials/visualisation-and-rendering/d5-render/README.md)** — Inspect the existing PDF before deciding whether it needs light revision or more extensive rewriting; verify interface and version-specific steps.
- [ ] **B (provisional) · [Circular Graphs and 2D Export](tutorials/visualisation-and-rendering/circular-graphs/README.md)** — Assess the PDF and vvvv patch, then improve the written introduction and export/graphic workflow as needed.
- [ ] **C · [Combining 2D and 3D](tutorials/visualisation-and-rendering/combining-2d-and-3d/README.md)** — Explain the supplied vvvv example, why the two rendering modes are combined and how to reproduce the result.
- [ ] **C · [Drawing Fog](tutorials/visualisation-and-rendering/fog/README.md)** — Turn the four texture-effect patches into an explanatory sequence with screenshots and parameters to experiment with.
- [ ] **C · [vvvv Graphics Fundamentals](tutorials/visualisation-and-rendering/vvvv-graphics-fundamentals/README.md)** — Give the eight examples a coherent introductory progression, including project setup, Skia/Stride distinctions, image output and dependencies.
- [ ] **C · [vvvv Extended Examples](tutorials/visualisation-and-rendering/vvvv-extended-examples/README.md)** — Audit the twenty mixed examples and decide which should become separate short tutorials or a linked learning series; avoid one overwhelming monolithic guide.

### Simulation and agents

- [ ] **C · [Baking SDFs with Particles](tutorials/simulation-and-agents/baking-sdfs-with-particles/README.md)** — Explain the method, supplied geometry/data and expected result.
- [ ] **C · [VL.Fuse: SDFs and Fluid Simulation](tutorials/simulation-and-agents/fuse-simulation-series/README.md)** — Develop a conceptual introduction and reproduce the progression from signed distance fields to a fluid experiment.
- [ ] **C · [Rhino and vvvv: Geometry, Particles and Moving People](tutorials/simulation-and-agents/rhino-vvvv-series/README.md)** — Document the four-part series, cross-software prerequisites and movement/agent concepts; consider breaking it into linked stages.

### Physical computing and interaction

- [ ] **C · [Arduino Sensor Input into vvvv](tutorials/physical-computing-and-interaction/arduino-sensor-input/README.md)** — Add hardware setup, code/patch explanation, serial communication, testing and troubleshooting.
- [ ] **B · [LED Control with vvvv and Arduino](tutorials/physical-computing-and-interaction/led-control/Readme.md)** — Polish the already illustrated tutorial; verify hardware, code, serial protocol, example patterns and failure cases.

## Legacy material outside the tutorial structure

These three collections exist at the repository root and are **not yet fully integrated** into the topic indexes.

- [ ] **B · [File Access in Google Colab](Xtra%2000%20-%20File%20access%20in%20google%20colab/)** — Review the existing instructional notebook; clarify environments, Drive access, example data and a permanent place in the library.
- [ ] **B · [Modularise the Code](Xtra%2001%20-%20Modularise%20the%20code/)** — Preserve the useful introduction to modules/functions; revise the handling of secrets, hard-coded local paths and working examples. **Complete the credential check above first.**
- [ ] **C · [Google API](Xtra%2002%20-%20Google%20API/)** — Currently mostly example assets and JSON; determine the intended teaching outcome and whether a new, fully written tutorial is warranted.

## Wishlist — potential new resources

These are ideas from previous teaching discussions, **not yet approved as individual tutorials**. Before starting, check whether source materials already exist in annual RC15 repositories, and decide the learning outcome and appropriate topic.

- [ ] **Rhino and Grasshopper fundamentals** — Reusable introductory modelling/computational geometry pathway.
- [ ] **Python and Jupyter fundamentals** — Beginner-friendly notebooks, code concepts, environment setup and reading/writing files.
- [ ] **Arduino foundations, sensors and physical data logging** — Adapt the existing annual teaching material into permanent tutorials.
- [ ] **LLM-assisted programming, debugging and verification** — Formulating problems, evaluating generated code and retaining intellectual control.
- [ ] **Illustrator, mapping graphics and colour** — Graphic representation and post-production across software tools.
- [ ] **Urban datasets, APIs and data preparation** — Acquisition, file formats, cleaning, provenance and reproducibility.
- [ ] **GitHub and managing computational design projects** — Version control, folders, documentation, reproducibility and collaboration.
- [ ] **Real-time graphics and interactive systems** — Extend selected vvvv workflows into a coherent learning pathway.

Additional wishlist ideas should be added here as they arise, without forcing immediate implementation.

## Suggested working sequence

1. **Resolve urgent problems** (especially possible credentials and broken links) without waiting for the overall redesign.
2. **Establish the tutorial editorial standard** using a comparatively mature resource, such as Network Mapping in QGIS.
3. **Review missing foundations** before revising advanced tutorials that rely on them.
4. **Develop one tutorial at a time**, choosing the next item by teaching value as well as effort.
5. **Improve topic pages and illustrations alongside the tutorials** so the main README always points towards useful material.
6. **Review the wishlist periodically**, keeping year-specific teaching briefs and assessments outside the permanent library.

When a tutorial is finished, tick its item, add a brief note or link to the relevant commit if useful, and record the tested versions and last verification date in that tutorial itself.
