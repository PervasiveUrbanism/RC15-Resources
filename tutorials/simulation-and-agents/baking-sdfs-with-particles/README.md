# Baking SDFs with Particles in vvvv

Part of **RC15 Resources**, the permanent tutorial library for Pervasive Urbanism.

**Software:** vvvv gamma, VL.Fuse, Rhino  
**Format:** Example patch with exported data  
**Software version:** The patch references vvvv 2024.6; compatibility with current versions has not been verified.  
**Original collection:** 240217_BakeSDF with Particles

[Browse this topic](../README.md) | [Library home](../../../README.md)

## About this example

A **signed distance field (SDF)** describes a shape mathematically, rather than as a fixed mesh. Particle systems can use that field to position or move points in relation to its surface. This example explores the connection between SDF operations, particle positions and the geometry we can make from those positions.

In vvvv, these positions can change as the system runs. **Baking** means capturing a particular result and saving it so it can be inspected or developed further outside the live simulation. For architectural work, this provides a bridge between procedural experiments in vvvv and modelling in Rhino.

If SDFs are new to you, start with [Signed Distance Fields](../../geometry-and-modelling/signed-distance-fields/README.md).

## Explore the example

Open **[01 Particles - BakeSDF.vl](01%20Particles%20-%20BakeSDF.vl)** in vvvv and examine the particle and SDF operations. The patch includes `ClosestPointOnSDF`, GPU buffer readback and file-writing nodes. Follow how positions are calculated, retrieved and prepared for export.

The folder also contains outputs and references to inspect:

- [Buffer.png](Buffer.png) — a supporting image.
- [Positions.txt](Positions.txt) — saved position data.
- [Positions.obj](Positions.obj) — an exchange-format geometry file.
- [Positions.3dm](Positions.3dm) — a Rhino model.

Compare the saved positions with the geometry visible in the patch or in Rhino. Consider what is gained by keeping a result as editable model data, and what is lost when a particular state of a dynamic system is fixed.

**Desktop verification pending:** The patch and its export sequence have not been run during this editorial review. Before teaching from it, check the VL.Fuse dependencies, buffer readback, output paths and formats, and the relationship between the saved files and the Rhino geometry. See the [editorial backlog](../../../EDITORIAL_BACKLOG.md).
