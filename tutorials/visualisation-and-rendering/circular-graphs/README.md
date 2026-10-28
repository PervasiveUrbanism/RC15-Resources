# Circular Graphs and 2D Export in vvvv

Part of **RC15 Resources**, the permanent tutorial library for Pervasive Urbanism.

**Software:** vvvv gamma (Skia)  
**Format:** Example patch, supplied data and PDF guide  
**Software version:** The patch references vvvv 2024.6; compatibility with newer releases has not been verified.  
**Original collection:** 240229_Circular Graph and 2d Export

[Browse this topic](../README.md) | [Library home](../../../README.md)

## About this example

Circular graphs can turn numerical data into a spatial composition. Values might determine the location, size or appearance of marks arranged around a centre. This can create a visually engaging representation, but the design of the graph also affects how easily its data can be understood.

This vvvv example uses **Skia** for 2D graphics. The patch contains sections for circular layouts, graph construction and styling, including gradients, averages and glow effects. It also includes nodes for **PDF and image export** so the output can be developed further in a graphic-design application such as Illustrator or InDesign.

## Explore the example

Start with the [existing PDF guide](Export.pdf), then open [240229_Circular Graph and 2d Export.vl](240229_Circular%20Graph%20and%202d%20Export.vl) in vvvv. Keep the [supplied text data](211215_004RC16M_shp.txt) in the same folder and check any local file paths within the patch.

Follow the data from the file-reading nodes through the circular graph layout and graphic styling. Experiment with one parameter at a time: for example, compare the legibility of an uncluttered graph with a version using stronger effects. Ask what each visual feature communicates about the underlying values.

Finally, inspect the patch's **PDFWriter**, **ImageWriter** and off-screen rendering components. Set a suitable output path, test an export and compare the resulting PDF and image. The export controls and output formats need verification in vvvv; do not assume that every effect will reproduce identically across formats.

The folder also includes an [example image](Image.png) to examine alongside your own result.

**Desktop and document verification pending:** The existing PDF guide has not yet been reviewed in full, and the example has not been run in vvvv during this editorial pass. Check data paths, Skia rendering, the graph's interpretation and PDF/image export in a current installation. See the [editorial backlog](../../../EDITORIAL_BACKLOG.md).
