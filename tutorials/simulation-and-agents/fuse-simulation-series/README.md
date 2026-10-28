# VL.Fuse: SDFs and Fluid Simulation

Part of **RC15 Resources**, the permanent tutorial library for Pervasive Urbanism.

**Software:** vvvv gamma, VL.Fuse  
**Format:** Five example patches  
**Software version:** The patches reference vvvv 2025.7.1; compatibility with newer versions has not been verified.  
**Original collection:** Extra 10 - VL Fuse

[Browse this topic](../README.md) | [Library home](../../../README.md)

## About these examples

These examples introduce two related ways of working with geometry and movement in **VL.Fuse**: **signed distance fields (SDFs)** and **fluid simulation**.

An SDF describes a shape mathematically through its distance from a boundary. This makes it useful for constructing, combining and transforming procedural forms without relying on a conventional mesh. In a fluid simulation, the computer instead calculates how material moves and evolves over time. The two methods can work together: SDFs can describe obstacles and boundaries that influence the flow, but an SDF is **not** itself a fluid simulation.

In architectural experiments, this relationship allows us to investigate how moving systems interact with spatial forms, openings and constraints.

## Explore the patches

Begin with the three SDF examples, then move to the fluid experiments.

1. **[01 SDFs.vl](01%20SDFs.vl)** — Explore the basic construction and rendering of SDF geometry.
2. **[02 SDF.vl](02%20SDF.vl)** — Experiment with combining and transforming procedural forms.
3. **[03 SDF.vl](03%20SDF.vl)** — Investigate more developed shapes, including custom pipe and arch operations.
4. **[Explanation Fluid Introduction.vl](Explanation%20Fluid%20Introduction.vl)** — Examine the main parts of a fluid setup: fluid entities, obstacles and rendering.
5. **[Fluid Simulation.vl](Fluid%20Simulation.vl)** — Explore the simulation and its visual output.

Open the patches in vvvv and inspect their node groups. Try changing a primitive or obstacle and observe how the resulting form or movement changes. Consider how the same approach could help investigate relationships between geometry and dynamic environmental processes.

For a separate introduction to the underlying geometry, see [Signed Distance Fields in vvvv](../../geometry-and-modelling/signed-distance-fields/README.md).

**Desktop verification pending:** The patches and their VL.Fuse dependencies have not been tested in a current vvvv installation during this editorial review. Check the rendering, simulation and interaction with SDF obstacles before using them in teaching. See the [editorial backlog](../../../EDITORIAL_BACKLOG.md).
