# Reading Point Clouds in vvvv

Part of **RC15 Resources**, the permanent tutorial library for Pervasive Urbanism.

**Software:** vvvv gamma, VL.Fuse  
**Format:** Example patch with sample data  
**Software version:** The patch references vvvv 2024.6; compatibility with newer versions has not been verified.  
**Original collection:** 240305_Read Point Clouds

[Browse this topic](../README.md) | [Library home](../../../README.md)

## About this example

A **point cloud** represents a scanned or measured environment as a collection of points in three-dimensional space. Unlike a conventional surface model, it can retain the irregularities and gaps of the original scan, offering a different way to investigate existing buildings and urban spaces.

This vvvv example explores how to read **PLY** point-cloud data and display the resulting points in a 3D scene. The patch uses a PLY reader alongside particle attributes and Stride rendering.

## Explore the example

Download the [vvvv patch](240305_Read%20ply.vl) and the [sample data archive](pointclouds/EveryPoint_20201123_175926_graff_tunnel.zip). Extract the ZIP archive before using the data, and keep track of where the extracted files are stored.

Open the patch in vvvv and check the **file path** supplied to its PLY reader. It may need updating to match the extracted dataset on your computer. Once the points are displayed, experiment with the camera, point size and colour to see how these choices affect the legibility of the scanned environment.

The supplied dataset is relatively large (the ZIP alone is approximately 42 MB), so loading and rendering performance may depend on your hardware.

**Desktop check pending:** The patch, the contents of the archive and the required VL.Fuse dependencies have not yet been tested together in a current vvvv installation. This is recorded in the [editorial backlog](../../../EDITORIAL_BACKLOG.md).
