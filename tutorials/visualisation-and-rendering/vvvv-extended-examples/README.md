# vvvv Extended Examples

Part of **RC15 Resources**, the permanent tutorial library for Pervasive Urbanism.

**Software:** vvvv gamma; some examples use Arduino or Rhino  
**Format:** Collection of 20 example patches  
**Software version:** The sampled patches reference vvvv 2024.6.7; current compatibility has not been verified.  
**Original collection:** Extra 2 - VVVV

[Browse this topic](../README.md) | [Library home](../../../README.md)

## About this collection

This is an archive of experiments rather than one continuous exercise. It brings together sensor data, 2D and 3D graphics, signed distance fields (SDFs), particle systems and geometry exchange. Select an example according to the technique you want to explore. The links below retain the original numbering so the patches remain easy to find.

Download the folder with its [Assets](Assets) and [Frames](Frames) directories intact. Some patches refer to external images, data or models and may need their file paths updated on your computer.

## Sensors, data and 2D graphics

- **[01 Arduino Read Temp and Humidity.vl](01%20Arduino%20Read%20Temp%20and%20Humidity.vl)** — Sensor data received through a serial connection.
- **[02 Simple Graph and 2D Export.vl](02%20Simple%20Graph%20and%202D%20Export.vl)** — Graphing and exporting 2D graphics.
- **[03 Circle Graph.vl](03%20Circle%20Graph.vl)** — A more developed circular graphic.

For another sensor-to-visualisation workflow, see [Arduino Sensor Input into vvvv](../../physical-computing-and-interaction/arduino-sensor-input/README.md).

## Graphics, cameras and 3D representation

- **[04 Overlay Stride and Skia.vl](04%20Overlay%20Stride%20and%20Skia.vl)** — Combining graphics from the Stride and Skia rendering systems.
- **[05 Simple Camera Animation.vl](05%20Simple%20Camera%20Animation.vl)** — Animating a camera.
- **[07 Import OBJ.vl](07%20Import%20OBJ.vl)** — Working with imported mesh geometry.
- **[18 Images in 3D.vl](18%20Images%20in%203D.vl)** — Placing images in a 3D scene.
- **[19 Materials.vl](19%20Materials.vl)** — Exploring material properties.
- **[20 Open Rhino File.vl](20%20Open%20Rhino%20File.vl)** — Reading Rhino geometry.

For a more introductory selection, see [vvvv Graphics Fundamentals](../vvvv-graphics-fundamentals/README.md). For more on Rhino interoperability, see [Rhino and Grasshopper Import into vvvv](../../geometry-and-modelling/rhino-grasshopper-import/README.md).

## Signed distance fields

- **[06 SDFs.vl](06%20SDFs.vl)** — Procedural SDF forms.
- **[08 SDF 02.vl](08%20SDF%2002.vl)** — Further SDF experiments.
- **[17 SDF.vl](17%20SDF.vl)** — Another example of SDF modelling.

Start with [Signed Distance Fields in vvvv](../../geometry-and-modelling/signed-distance-fields/README.md) for a short explanation of the underlying idea.

## Particle systems

The eight patches below form the most substantial sequence in this collection. They explore different aspects of particle-based graphics, from basic computation and emitters to custom attributes and simulation.

1. **[09 Particle Compute System.vl](09%20Particle%20Compute%20System.vl)** — Particle computation.
2. **[10 Particle Blend Methods.vl](10%20Particle%20Blend%20Methods.vl)** — Blending and visual appearance.
3. **[11 Particle Simple System.vl](11%20Particle%20Simple%20System.vl)** — A simple particle setup.
4. **[12 Particle Amount Emitter.vl](12%20Particle%20Amount%20Emitter.vl)** — Controlling emission.
5. **[13 Particle Two Emitter System.vl](13%20Particle%20Two%20Emitter%20System.vl)** — Working with two emitters.
6. **[14 Particle Many Emitter.vl](14%20Particle%20Many%20Emitter.vl)** — Extending to multiple emitters.
7. **[15 Particle Many Emitter and Custom Attribute.vl](15%20Particle%20Many%20Emitter%20and%20Custom%20Attribute.vl)** — Adding a custom particle attribute.
8. **[16 Particle System Simulation.vl](16%20Particle%20System%20Simulation.vl)** — Exploring particle simulation.

These patches use VL.Fuse particle and compute functionality. They could eventually form a separate learning sequence, but are kept here in their original collection for now.

**Desktop verification pending:** The patches have not been run during this editorial review. Check compatibility, VL.Fuse and other dependencies, external asset paths, data/serial inputs, image exports and simulation behaviour before using them in teaching. See the [editorial backlog](../../../EDITORIAL_BACKLOG.md).
