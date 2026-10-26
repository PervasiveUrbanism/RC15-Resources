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

- [ ] **Check for exposed credentials** in the legacy modularisation example (`tutorials/programming-and-data-access/modularise-the-code/`, including `Passwords.py` and `passwords.csv`). Determine whether values are dummy examples or real secrets. If real, **revoke/rotate them immediately** and plan remediation of Git history; deleting the current files alone would not remove prior exposure. Do not copy credential values into documentation.
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

- [ ] **B · [Sentiment Landscapes](tutorials/mapping-and-spatial-analysis/sentiment-landscapes/README.md)** — **Status: five chapters drafted; final review necessary.** Add relevant screenshots and explanatory images throughout the QGIS, Grasshopper and Illustrator steps, using existing project assets where suitable. Perform a final editorial and technical review, including end-to-end testing of the Flickr/QGIS → Heron/Grasshopper → Illustrator workflow, before marking complete.
- [x] **A · [Network Mapping in QGIS](tutorials/mapping-and-spatial-analysis/network-mapping/README.md)** — **DONE — FINISHED. No further action necessary.** Final editorial changes completed and approved on 26 October 2026: download instructions, routing assumptions and before/after illustration. This item is closed; do not schedule further review unless a specific new issue arises.
- [x] **B · [Heatmaps in QGIS](tutorials/mapping-and-spatial-analysis/heatmaps/README.md)** — **DONE — FINISHED. No further action necessary.** Reviewed and approved by the user; corrected raster cell-size terminology to specify map units rather than screen pixels. Closed on 26 October 2026; reopen only if a specific new issue arises.
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

- [x] **B · [Flow Along Surface in Rhino](tutorials/geometry-and-modelling/flow-along-surface/README.md)** — **DONE — FINISHED. No further action necessary.** Approved by the user on 26 October 2026. Expanded the introduction to `Flow` and `FlowAlongSrf`, clarified NURBS and Grasshopper, and corrected UV mapping, fabrication and History explanations. Closed; only reopen if a specific new issue arises.
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

- [ ] **B · [File Access in Google Colab](tutorials/programming-and-data-access/file-access-in-google-colab/)** — Review the existing instructional notebook; clarify environments, Drive access, example data and a permanent place in the library.
- [ ] **B · [Modularise the Code](tutorials/programming-and-data-access/modularise-the-code/)** — Preserve the useful introduction to modules/functions; revise the handling of secrets, hard-coded local paths and working examples. **Complete the credential check above first.**
- [ ] **C · [Google API](tutorials/programming-and-data-access/google-api/)** — Currently mostly example assets and JSON; determine the intended teaching outcome and whether a new, fully written tutorial is warranted.

## Wishlist — potential new resources

These are ideas from previous teaching discussions, **not yet approved as individual tutorials**. Before starting, check whether source materials already exist in annual RC15 repositories, and decide the learning outcome and appropriate topic.

- [ ] **Rhino and Grasshopper fundamentals** — Reusable introductory modelling/computational geometry pathway.
- [ ] **Python and Jupyter fundamentals** — Beginner-friendly notebooks, code concepts, environment setup and reading/writing files.
- [ ] **UMAP directly from Grasshopper via a local Flask/Python service** — Follow-on to [Introduction to UMAP](tutorials/data-analysis-and-machine-learning/umap/README.md). Build an end-to-end Grasshopper definition in which students **prepare and retain their dataset in Grasshopper**, send numerical data to a **locally running Flask API** for UMAP computation, then receive coordinates (and optional neighbourhood/connectivity information) back into Grasshopper for geometry and visualisation. Avoid an intermediate CSV/Excel/Jupyter export: keep the workflow live, with Grasshopper as the user-facing environment. **Teaching requirement:** show several small, clearly named Grasshopper components/clusters with explicit inputs and outputs (for example: data preparation, validation/normalisation, API request, returned-data parsing, geometry/visualisation) rather than one large opaque Python component. Explain the request/response structure and separate Flask server, with practical guidance for installation, starting/stopping the service, handling errors and preventing unnecessary recomputation. **Architectural caveat:** the UMAP calculation technically runs in a separate local Python process, not inside Grasshopper itself; data should nevertheless remain in the Grasshopper workflow without intermediate saved files. Verify Rhino/Grasshopper Python environment compatibility, Flask communication and UMAP package versions when developing; do not assume this design has been tested.
- [ ] **Real-time skeleton tracking with MediaPipe (Python; optional Flask integration)** — Proposed tutorial, assuming 'media server' refers to **Google MediaPipe** (confirm later if a different media-server platform was intended). Start with webcam/video input, detect human pose landmarks with MediaPipe Pose Landmarker, then visualise tracked joints and connected skeleton lines. Explain landmark coordinates, confidence/visibility, camera calibration limits, frame rates, smoothing and tracking limitations. Explore an architectural/interactive outcome (e.g. a body-driven spatial graphic or installation). **Optional follow-on:** send structured landmark data to Grasshopper and/or vvvv from a separate Python process. Evaluate **Flask as a simple HTTP/JSON bridge for initial tests**, but compare it with WebSockets, OSC or UDP for continuous low-latency streaming; do not make Flask a prerequisite. Prefer small understandable stages (camera input → pose detection → coordinate processing → transmission → design-tool visualisation) instead of one opaque script. Include consent/privacy considerations for recorded/live camera footage, along with tested versions and performance guidance. **Starting reference:** [official MediaPipe Pose Landmarker Python guide](https://developers.google.com/edge/mediapipe/solutions/vision/pose_landmarker/python).
- [ ] **Arduino foundations, sensors and physical data logging** — Adapt the existing annual teaching material into permanent tutorials.
- [ ] **LLM-assisted programming, debugging and verification** — Formulating problems, evaluating generated code and retaining intellectual control.
- [ ] **Illustrator, mapping graphics and colour** — Graphic representation and post-production across software tools.
- [ ] **Urban datasets, APIs and data preparation** — Acquisition, file formats, cleaning, provenance and reproducibility.
- [ ] **Pedestrian isochrones for different users (inclusive walkability)** — Research and develop a **pedestrian-only** mapping exercise comparing reachability for distinct users, e.g. an adult, an older person, a child and someone pushing a pram (potentially also wheelchair users). The key teaching question is how **the same city becomes differently accessible** through walking speed, slopes, stairs, kerbs, crossings, path surfaces, safety and other barriers. Compare the isochrones on one network rather than treating an average walker as universal. **Original visual reference seen in October 2026 not yet identified confidently; investigate.** Related references discovered during preliminary search:
  - [02Route 3D QGIS plugin](https://plugins.qgis.org/plugins/zero2route3d/) — supports adult, senior, child, stroller and wheelchair profiles with profile-aware isochrones (closest match for the list of user types; not confirmed as the original map).
  - [Ulrike Jehle, *User-specific walking accessibility* (TUM, 2025), Figure 44 (p. 151)](https://mediatum.ub.tum.de/download/1753499/1753499.pdf) — compares 5-minute pedestrian isochrones for children, seniors, women and wheelchair users, incorporating perceived walkability.
  - [Berlin walking isochrones — capan/isochrone](https://github.com/capan/isochrone) — maps reachable pedestrian network for walking, stroller and wheelchair profiles, including stairs and surfaces.
  - [CAT: Comfort-based Accessibility Tool (TUM / InclusiveSpaces)](https://inclusive-spaces.vercel.app/) — user-adjustable walking time, speed and environmental comfort factors.
  - **When developing:** assess local sidewalk-data coverage and modelling assumptions; differentiate empirically supported restrictions from illustrative persona settings, and do not imply age or gender alone dictates individual ability.
- [ ] **Evaluate YouTube video as a source for a new written tutorial** — [Video supplied for review](https://youtu.be/J7ea0ZQaEDI). Parked at the user's request (26 October 2026). Obtain a usable transcript and inspect any essential on-screen steps, then assess whether the subject adds value to RC15 Resources or duplicates an existing resource. If worthwhile, propose a beginner-friendly, independently explained tutorial with verified technical steps and appropriate attribution. **Do not draft or publish yet.**
- [ ] **Mapbox background maps in QGIS** — New standalone beginner tutorial: add a Mapbox basemap to QGIS (for example via an XYZ tile connection), configure a style and geographic extent, and prepare it for map layouts and exports. Explain account/access-token requirements, safe handling of tokens, tile usage and attribution. Verify Mapbox's current supported endpoints and QGIS behaviour before writing; cross-link from mapping tutorials without duplicating them.
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
