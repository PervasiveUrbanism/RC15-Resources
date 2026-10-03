# GSR to UMAP

Part of **RC15 Extended Knowledge**, a collection of tutorials and examples beyond the current curriculum.

**Software:** Python, vvvv  
**Format:** Written tutorial  
**Software versions:** To be confirmed  
**Original collection:** Extra 04 - GSR to UMAP

[Browse this topic](../README.md) | [Library home](../../../README.md)

---

## Introduction

This series of notebooks and sketches shows a step-by-step workflow for turning a GSR curve into spatial representations using UMAP.

The process has two main parts:

The first part is *analysis.* We work with the raw signal, transform it, and calculate new descriptions from it. The aim is to understand how behaviour over time can be expressed with numbers.

The second part is *visualisation*. After the analysis, the results are transferred into design environments where patterns and relationships can be explored visually.

The analysis is done in **Python**. The notebooks explain the logic behind each step and introduce ways of thinking about data in a structured, computational way. Once the analytical work is complete, the data can be moved into tools such as **Grasshopper** or **vvvv**.

Parts of the code and some explanations (like this text) were generated with the help of ChatGPT. However, the important decisions — what to calculate, what to compare, and how to interpret the results — remain your responsibility. It all needs to make sense. 

You can follow it exactly as written, especially if you are new to the topic. But you can also modify it, add steps, remove parts, or connect it to other methods. The goal is to make the logic understandable and once you understand the structure, you can adapt it.


## Notebook - 02_GSR to Audio

The first notebook focuses on analysing the GSR curve and extracting mathematical features.

Many of these methods come from audio analysis. Here we use them as general tools to describe how a signal changes over time. These features are being added to the inital table. 


## Notebook - 03_Audio to UMAP

The second notebook uses this expanded table. We calculate spatial distances using UMAP. And we can create both two-dimensional and three-dimensional versions.

The new coordinates are then added back into the table.
From this point on, the dataset is not only a timeline — it becomes a space.


## Visualisation environments

After spatialisation, the data can be explored in different tools. Grasshopper connects well to modelling and parametric design workflows. vvvv is strong in real-time systems, interaction, and media environments. It is graphically stronger and can handle larger datasets. 