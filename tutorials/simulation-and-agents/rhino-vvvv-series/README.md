# Rhino and vvvv: Geometry, Particles and Moving People

Part of **RC15 Resources**, the permanent tutorial library for Pervasive Urbanism.

**Software:** Rhino, Grasshopper, vvvv gamma  
**Format:** Four example folders  
**Software version:** The vvvv patches reference 2025.7.1; compatibility with newer versions has not been verified.  
**Original collection:** Extra 09 - VL Rhino

[Browse this topic](../README.md) | [Library home](../../../README.md)

## About these examples

Rhino and Grasshopper provide ways to construct and organise architectural geometry; **vvvv** can then use that geometry in real-time graphics and movement-based experiments. This collection follows a loose progression from importing a model to connecting Grasshopper and exploring dynamic representations.

Open each vvvv patch alongside the accompanying Rhino or Grasshopper files. Keep the folder structure intact and check any file paths in the patches, as they may refer to locations on the original author's computer.

## Explore the four examples

1. **[01 Import](01%20Import)** — Start with [Site Plan.vl](01%20Import/Site%20Plan.vl) and [Siteplan.3dm](01%20Import/Siteplan.3dm). The patch uses a Rhino reader to bring site-plan geometry into vvvv. The Rhino model is comparatively large (about 80 MB).

2. **[02 Grasshopper Link](02%20Grasshopper%20Link)** — Open [Link Grasshopper.vl](02%20Grasshopper%20Link/Link%20Grasshopper.vl) alongside [Surface Division.gh](02%20Grasshopper%20Link/Surface%20Division.gh) and [Surface Division.3dm](02%20Grasshopper%20Link/Surface%20Division.3dm). The vvvv patch includes `GrasshopperReceive` for transferring geometry.

3. **[03 Particles and Agents](03%20Particles%20and%20Agents)** — Explore [Particles.vl](03%20Particles%20and%20Agents/Particles.vl), [Particles.gh](03%20Particles%20and%20Agents/Particles.gh) and [Particles.3dm](03%20Particles%20and%20Agents/Particles.3dm). Investigate how geometry from Grasshopper can participate in dynamic visual systems. Bear in mind that particles and **agents** are not necessarily the same: calling a moving point an agent implies some form of behavioural rules or decision-making.

4. **[04 Moving People](04%20Moving%20People)** — Examine [Moving People.vl](04%20Moving%20People/Moving%20People.vl) with the supplied [Rhino models](04%20Moving%20People) and `ref.dwg`. This example provides a starting point for representing movement in relation to architectural geometry.

The vvvv patches are the main learning material. Try changing source geometry or inputs, then observe what changes downstream. For a separate set of interoperability examples, see [Rhino and Grasshopper Import into vvvv](../../geometry-and-modelling/rhino-grasshopper-import/README.md).

**Desktop verification pending:** The patches, geometry links and outputs have not been run during this editorial review. Check `RhinoReader`, `GrasshopperReceive`, dependencies, file paths, movement behaviour and compatibility with current vvvv versions before using the series in teaching. See the [editorial backlog](../../../EDITORIAL_BACKLOG.md).
