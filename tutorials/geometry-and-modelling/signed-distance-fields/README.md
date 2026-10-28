# Signed Distance Fields in vvvv

Part of **RC15 Resources**, the permanent tutorial library for Pervasive Urbanism.

**Software:** vvvv gamma, VL.Fuse  
**Format:** Five example patches  
**Software version:** The patches reference vvvv 2024.6; compatibility with newer versions has not been verified.  
**Original collection:** 240208_SDF's

[Browse this topic](../README.md) | [Library home](../../../README.md)

## What is a signed distance field?

A **signed distance field (SDF)** describes a shape through a mathematical function rather than a collection of surfaces or mesh faces. At any point in space, the function returns a value related to the distance to the shape's boundary. By convention, the value is **negative inside**, **zero on the boundary** and **positive outside**.

This approach makes it possible to construct and transform shapes procedurally. Simple fields can be combined to form more complex geometry, while transformations and mathematical variations can produce effects that would be more cumbersome to model by editing individual vertices. SDFs are particularly useful for experiments with continuous, changing forms and computational visualisation.

The examples use **VL.Fuse** in vvvv to render and manipulate these fields. Unlike a conventional Rhino modelling exercise, the main result is a computed visual representation of geometry. Explore how changing the underlying functions changes the appearance of the shape.

## Explore the five patches

Open the patches in the following order:

1. **[01 Typical Pipeline.vl](01%20Typical%20Pipeline.vl)** — Introduces a basic SDF rendering pipeline.
2. **[02 SDF Primitives.vl](02%20SDF%20Primitives.vl)** — Explores fundamental SDF shapes.
3. **[03 Transforming SDF.vl](03%20Transforming%20SDF.vl)** — Demonstrates transformations and operations on a field.
4. **[04 Noisy Spheres.vl](04%20Noisy%20Spheres.vl)** — Adds procedural variation to a sphere-like form.
5. **[05 Outline.vl](05%20Outline.vl)** — Explores an outline-style visual treatment.

Work through the patches directly and experiment with the parameters. Try comparing a smooth primitive with a transformed or noisy version, and consider how a similar method might be used to explore spatial boundaries, envelopes or changing architectural forms.

Keep the supplied image assets with the examples when downloading the folder: [colour reference 1](3E95CC_65D9F1_A2E2F6_679BD4-512px.png), [colour reference 2](C7C7D7_4C4E5A_818393_6C6C74.png) and [MatCapSample01.png](MatCapSample01.png).

**Desktop verification pending:** The five patches, VL.Fuse dependencies and resulting renders have not yet been tested in a current vvvv installation. See the [editorial backlog](../../../EDITORIAL_BACKLOG.md).
