# Creative Coding and Interactive Systems — vvvv

[Library home](../README.md) · [Browse all resources by topic](../README.md#browse-by-topic)

**Software:** vvvv gamma, with Rhino, Grasshopper or Arduino in some examples  
**Starting level:** Beginner, progressing to more specialised examples  
**Formats:** Example patches, selected written guides and project collections

vvvv is a visual programming environment in which nodes and connections describe how data, geometry, graphics and interaction work together. It is particularly useful for exploring real-time visual systems, animation and connections to external devices.

These resources are distributed across several subjects in RC15 Resources because their applications differ. **This page offers a route through them without moving or duplicating the original files.** It is a recommended sequence, not a course that must be completed in full.

Many entries are **example collections**, not step-by-step tutorials. Begin with a small patch, change one parameter, observe the result and trace the connections that produced it. Several patches were created with earlier versions of vvvv gamma and have not been verified in a current installation. Preserve accompanying assets and check package dependencies and file paths.

## Start here — Understand a patch

1. **[vvvv Graphics Fundamentals](../tutorials/visualisation-and-rendering/vvvv-graphics-fundamentals/README.md)** — *Beginner · Eight example patches.* Begin with **01 Bare Bones** to understand nodes and connections. Then compare Skia and Stride image export. The other examples introduce imported geometry, animated materials and fog.
2. **[Circular Graphs and 2D Export](../tutorials/visualisation-and-rendering/circular-graphs/README.md)** — *Intermediate · PDF guide and example patch.* Follow data into a circular composition, alter its styling, then examine image and PDF export.
3. **[vvvv Extended Examples](../tutorials/visualisation-and-rendering/vvvv-extended-examples/README.md)** — *Exploration · Twenty example patches.* A reference collection rather than a single lesson. Choose an example after becoming familiar with the basics.

**A useful first experiment:** Open a simple graphics patch, identify where values enter the network, change one input and save a before-and-after image. Explain which nodes produced the visible difference.

## Explore according to your interest

| Interest | Resources | What to investigate |
| --- | --- | --- |
| **Drawing and visual effects** | [Combining 2D and 3D](../tutorials/visualisation-and-rendering/combining-2d-and-3d/README.md) · [Drawing Fog](../tutorials/visualisation-and-rendering/fog/README.md) | Layering Skia and Stride, textures and atmospheric effects. *Example patches.* |
| **Procedural geometry** | [Signed Distance Fields](../tutorials/geometry-and-modelling/signed-distance-fields/README.md) · [Reading Point Clouds](../tutorials/geometry-and-modelling/reading-point-clouds/README.md) | Building implicit shapes and importing spatial data. *Example sequences.* |
| **Rhino and Grasshopper** | [Rhino and Grasshopper Import into vvvv](../tutorials/geometry-and-modelling/rhino-grasshopper-import/README.md) · [Rhino and vvvv: Geometry, Particles and Moving People](../tutorials/simulation-and-agents/rhino-vvvv-series/README.md) | Transferring geometry into real-time systems and examining movement. *Example projects.* |
| **Simulation** | [Baking SDFs with Particles](../tutorials/simulation-and-agents/baking-sdfs-with-particles/README.md) · [VL.Fuse: SDFs and Fluid Simulation](../tutorials/simulation-and-agents/fuse-simulation-series/README.md) | Particle positions, distance fields and fluid behaviour. *Advanced examples.* |
| **Sound and data** | [Sound Analysis in vvvv](../tutorials/data-analysis-and-machine-learning/sound-analysis/README.md) · [GSR to UMAP](../tutorials/data-analysis-and-machine-learning/gsr-to-umap/README.md) | Extracting features from sound and turning sensor signals into spatial representations. *Example project and notebooks.* |
| **Sensors and interaction** | [Arduino Sensor Input into vvvv](../tutorials/physical-computing-and-interaction/arduino-sensor-input/README.md) · [LED Control with vvvv and Arduino](../tutorials/physical-computing-and-interaction/led-control/Readme.md) | Reading sensor values and sending serial commands to physical outputs. *Example project and guided tutorial.* |

## Choosing a resource

A **guided tutorial** explains a sequence of actions and decisions. An **example patch** is a working document to explore, but may need additional interpretation, packages or updated file paths. A **collection** groups several patches; it is often better to open one relevant example than to attempt every file.

If you are new to vvvv, begin with Graphics Fundamentals even if another example looks more exciting. Once you understand how data moves between nodes, choose a branch based on what you want to make.

For an overview of the same material by subject rather than software, return to the [RC15 Resources catalogue](../README.md#browse-by-topic).
