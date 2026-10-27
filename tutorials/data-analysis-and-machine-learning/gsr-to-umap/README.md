# GSR to UMAP

Part of **RC15 Resources**, the permanent tutorial library for Pervasive Urbanism.

**Software:** Python and Jupyter Notebook; optional visualisation in vvvv or Grasshopper  
**Format:** Two linked notebooks and a vvvv example  
**Software versions:** Not yet verified through an end-to-end run  
**Original collection:** Extra 04 - GSR to UMAP

[Browse this topic](../README.md) | [Library home](../../../README.md)

## Introduction — From a Sensor Signal to a Spatial Representation

A **Galvanic Skin Response (GSR)** sensor records changes in the electrical conductance of the skin over time. These changes can be associated with physiological arousal, but they do not tell us directly what someone feels, or whether an experience is positive or negative.

In architectural and urban research, a time-based sensor recording can be interesting in its own right: it tells a story of change, peaks, pauses and transitions. But how might we compare different moments in that recording? Can moments with similar signal characteristics be represented close together, even if they occurred at different times?

This tutorial explores one possible answer. We begin with a GSR time series and describe its changing behaviour using numerical **features**. We then use **UMAP** (*Uniform Manifold Approximation and Projection*) to place observations into a two- or three-dimensional arrangement according to similarity in those features.

The key transformation is conceptual: **a timeline becomes a space of relationships**. The resulting positions are not geographical coordinates, nor do they directly measure emotion. They offer another way to investigate the structure of recorded experience, which can subsequently inform drawings, spatial models or interactive environments.

If UMAP is new to you, begin with our [Introduction to UMAP](../umap/README.md), which explains dimensionality reduction through a simpler dataset.

## How the two notebooks connect

The workflow has two linked stages: **analysis** followed by **spatialisation**.

### 1. Analyse the GSR signal

Open [02_GSR to Audio.ipynb](02_GSR%20to%20Audio.ipynb).

The first notebook begins with the original sensor recording. It plots the signal, converts a normalised version into a WAV file, and applies techniques from audio analysis to extract numerical features describing how the signal changes over time.

These include measurements such as **RMS** (a measure of signal magnitude), spectral centroid, bandwidth and flatness. Although the algorithms come from audio processing, here they are used as mathematical descriptions of a physiological signal. Because GSR is a relatively slow signal, converting it to audio does **not** turn it into an acoustic recording or make the resulting frequency values physiological frequencies without further interpretation.

The notebook aligns the calculated feature values with the source observations and exports an expanded table, **`assets/GSR_Analysis.csv`**. This table becomes the input to the second notebook.

### 2. Create a UMAP representation

Open [03_Audio to UMAP.ipynb](03_Audio%20to%20UMAP.ipynb).

The second notebook reads `assets/GSR_Analysis.csv`, selects the original GSR values alongside several extracted features, and **standardises** their scales before applying UMAP. This is important: without scaling, features with numerically larger values could dominate comparisons.

UMAP then produces **2D and 3D coordinates** that arrange observations according to similarities in their selected measurements. The notebook plots these arrangements, examines connections between neighbouring observations and exports additional data tables for use elsewhere.

The outputs include **`assets/GSR_UMAP.csv`**, which extends the input data with UMAP coordinates, as well as **`assets/umap_connectivity_2d.csv`** and **`assets/umap_connectivity_3d.csv`**, which describe relationships between points.

These coordinates are an *embedding*: a constructed representation of similarities, not a literal reconstruction of the person's movement through physical space. Different features and UMAP settings can produce different arrangements.

## Getting started

The notebooks are intended to be read in sequence and run in a Python/Jupyter environment. Keep the original folder structure so that the notebook's relative references to `assets/` resolve correctly. The repository includes a source recording, **`assets/010RC14X.CSV`**, and intermediate/example outputs for inspecting the workflow.

Start by checking the file paths and input-column settings in the first notebook. Its initial code uses a local path that may need adjusting to your computer. Run cells in order, and compare each intermediate table and plot with your expectations before moving on. The notebooks include plotting and audio-processing dependencies, so you may need to install missing Python packages in your chosen environment.

If you are mainly reviewing the ideas, GitHub displays the notebooks without requiring Python. To run them, use Jupyter locally or a compatible hosted notebook environment, bearing in mind that file paths and dependencies may need adjustment.

## From data to geometry

The result of the Python analysis is not yet an architectural drawing. It is a set of points and relationships that can be interpreted and represented in different ways.

In **Grasshopper**, you might import the exported CSV coordinates, construct points in 2D or 3D, draw their connectivity lines and explore geometric transformations. In **vvvv**, you could animate the observations, link them back to their position in the original recording or build an interactive display. The repository includes [01 2D Umap.vl](01%202D%20Umap.vl) as a vvvv starting point; it is not a complete, documented Grasshopper workflow.

An important design decision is **what to represent**. You might preserve the chronological order of the signal, emphasise clusters of similar observations, or connect points that UMAP identifies as neighbours. These choices tell different stories. A compelling graphic should make its underlying assumptions understandable rather than implying that an abstract embedding is a measured emotional landscape.

## AI-assisted investigation

Parts of the notebooks and explanatory material were developed with assistance from ChatGPT. This is useful as a learning process, but the essential decisions remain yours: what is measured, which features are meaningful, how they are calculated, and what conclusions the visualisation can support.

Try changing one feature or UMAP parameter at a time and observe what changes. Understanding these dependencies matters more than reproducing any single final image.

*Editorial note (27 October 2026): This README has been revised to clarify the learning sequence and possible design applications. The notebooks, vvvv patch and datasets have not been changed or rerun.*
