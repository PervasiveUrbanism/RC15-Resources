# vvvv Graphics Fundamentals

Part of **RC15 Resources**, the permanent tutorial library for Pervasive Urbanism.

**Software:** vvvv gamma; example assets include Rhino geometry  
**Format:** Eight example patches  
**Software versions:** The patches reference vvvv versions from 2023.5.3 to 2025.7; current compatibility has not been verified.  
**Original collection:** Extra 03 - vvvv

[Browse this topic](../README.md) | [Library home](../../../README.md)

## About these examples

This collection introduces different ways of creating and exporting graphics in **vvvv**. Two important graphics systems appear in the examples: **Skia**, commonly used for drawing and composing 2D graphics, and **Stride**, which supports 3D scenes, materials and rendering. The examples can be opened individually, but the following grouping provides a useful starting point.

Keep the [Assets folder](Assets) together with the patches when downloading them. Several examples use external images, meshes or other data, and their file paths may need adjusting on your computer.

## 1. Getting started

**[01 Bare Bones.vl](01%20Bare%20Bones.vl)** — Explore the basic structure of a vvvv patch and how nodes and connections organise a computation. Start here if you are unfamiliar with the environment.

## 2. Rendering and exporting images

**[02 Stride Export Image.vl](02%20Stride%20Export%20Image.vl)** and **[03 Skia Export Image.vl](03%20Skia%20Export%20Image.vl)** — Compare image output from 3D-oriented Stride and 2D-oriented Skia workflows. Pay attention to the output dimensions, file format and destination path.

## 3. 3D geometry and visual effects

- **[04 Stride Images in 3D Space.vl](04%20Stride%20Images%20in%203D%20Space.vl)** — Explore images as elements in a 3D scene.
- **[05 Stride Animate Materials.vl](05%20Stride%20Animate%20Materials.vl)** — Experiment with changing material properties over time.
- **[06 Import OBJ Mesh.vl](06%20Import%20OBJ%20Mesh.vl)** — Work with external mesh geometry, including the supplied [OBJ asset](Assets/FinalBaseMesh.obj).
- **[07 Render Styles Textures.vl](07%20Render%20Styles%20Textures.vl)** — Explore different surface appearances and texture-based rendering.
- **[08 Fog.vl](08%20Fog.vl)** — Investigate a fog-like atmospheric graphic effect.

Open the patches and examine their node groups before modifying parameters. Compare the results: what changes when a graphic is treated as a 2D drawing, a texture in a 3D scene or a material on geometry?

**Desktop check pending:** These patches were authored across different vvvv versions and may have different dependencies. Image exports, asset paths, 3D rendering and compatibility need verification in a current installation; see the [editorial backlog](../../../EDITORIAL_BACKLOG.md).
