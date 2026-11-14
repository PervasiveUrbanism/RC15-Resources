# Rhino and Grasshopper Import into vvvv

Part of **RC15 Resources**, the permanent tutorial library for Pervasive Urbanism.

**Software:** Rhino, Grasshopper, vvvv gamma  
**Format:** Three example patches with Rhino and Grasshopper files  
**Software version:** The vvvv patches reference 2025.7.1; compatibility and dependencies have not been verified in a current installation.  
**Original collection:** Extra 14 - GH and Rhino Import  
**Verification status (14 November 2026):** Partially verified in practice, as confirmed by the resource maintainer. Exact coverage of the three patches and Rhino/Grasshopper connection, file paths, frame exports and current-version compatibility remain to be confirmed.

[Browse this topic](../README.md) | [Library home](../../../README.md)

## About these examples

Rhino and Grasshopper are useful for developing architectural geometry, while vvvv can bring that geometry into interactive visualisations and animation workflows. These examples explore exchanging geometry between the applications, displaying it in vvvv and exporting images.

The vvvv patches contain the implementation. Open them alongside the relevant Rhino and Grasshopper files, and follow the node groups to understand the connections.

## Explore the patches

1. **[01 Module B1 Import.vl](01%20Module%20B1%20Import.vl)** — Start with importing geometry. The patch contains `RhinoReader` and `GrasshopperReceive` nodes; explore their roles and the resulting geometry in vvvv.
2. **[02 Module B1 SaveForAnimation.vl](02%20Module%20B1%20SaveForAnimation.vl)** — Builds on the import example and includes image-writing nodes for exporting frames that can be assembled into an animation.
3. **[03 Module C1.vl](03%20%20Module%20C1.vl)** — A further geometry-import example using the Module C files.

The folder also contains [Module B1.3dm](Module%20B1.3dm), [Module B1.gh](Module%20B1.gh), [Module B2.gh](Module%20B2.gh), [Module C.3dm](Module%20C.3dm) and [Module C-1.gh](Module%20C-1.gh), together with the [frames](frames) and [ss](ss) folders and a [reference image](260621_160626_Image.png).

Download the relevant files together and check any file paths in the patches against their location on your computer. The `GrasshopperReceive` workflow may require a particular connection or setup between the applications; its precise configuration and verified scope are not yet documented.

Try changing the source geometry in Rhino or Grasshopper and observing what happens in vvvv. For the animation example, inspect the frame-writing path and settings before exporting a sequence.

**Further desktop review:** The maintainer confirms partial practical verification. The precise Rhino/Grasshopper connection, dependencies, file paths, frame export and compatibility with current vvvv versions still require documentation or testing. See the [editorial backlog](../../../EDITORIAL_BACKLOG.md).
