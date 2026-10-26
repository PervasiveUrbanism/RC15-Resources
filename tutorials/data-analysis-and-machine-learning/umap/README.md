# Introduction to UMAP

Part of **RC15 Resources**, the permanent tutorial library for Pervasive Urbanism.

**Software:** Python and Jupyter Notebook  
**Format:** Worked notebook tutorial  
**Software versions:** The notebook recommends Python 3.10–3.12; the full environment has not been retested during this editorial review.  
**Original collection:** Extra 02 - UMAP

[Browse this topic](../README.md) | [Library home](../../../README.md)

## Why learn UMAP?

Architectural and urban datasets often contain many measurements for each observation: environmental sensor readings, spatial characteristics, movement indicators or other numerical attributes. When each observation has several variables, it becomes difficult to see which observations resemble one another.

**UMAP** (*Uniform Manifold Approximation and Projection*) is a dimensionality-reduction technique. It places observations into a two- or three-dimensional representation according to patterns of similarity in the original data. This can help us explore clusters, transitions and unusual observations before deciding what they mean.

The resulting coordinates are **not geographical positions**, and the distances between points should not be interpreted as precise physical measurements. UMAP is an exploratory tool, not a substitute for understanding the original data.

## What you will do

The [UMAP notebook](UMAP.ipynb) introduces the method through the **Palmer Penguins** dataset, a small example with several measurements for each penguin. Although the subject is not architectural, the same process can later be applied to urban or environmental datasets.

Working through the notebook, you will inspect and clean tabular data, compare numerical features, standardise their scales, create **2D and 3D UMAP embeddings**, visualise the results and explore connectivity between observations. The final sections demonstrate how to export coordinates and connectivity lines to **CSV**, ready for use in other design and visualisation workflows.

The purpose is to understand the reasoning behind dimensionality reduction, not simply to reproduce a scatter plot. Pay particular attention to how the input variables and scaling affect the result.

## Getting started

You can [read the notebook directly on GitHub](UMAP.ipynb). To run and modify its code, open it in Jupyter on your computer or use [Google Colab](https://colab.research.google.com/github/PervasiveUrbanism/RC15-Resources/blob/main/tutorials/data-analysis-and-machine-learning/umap/UMAP.ipynb), which runs notebooks in a browser.

For a local installation, use a standard Python environment rather than legacy Grasshopper IronPython. The notebook lists the libraries it requires, including `numpy`, `pandas`, `scikit-learn`, `umap-learn`, `matplotlib`, `seaborn` and plotting tools such as `datashader`. Follow its installation instructions before running the cells.

Run the cells **in order**, since later steps rely on variables created earlier. The penguin dataset is loaded from an external online source, so an internet connection is needed for that step. In Colab, save a personal copy before editing; changes to your copy do not automatically update this repository.

## Files and outputs

- [UMAP.ipynb](UMAP.ipynb) — the complete explanatory notebook and worked exercise.
- [umap_digits_2d.csv](umap_digits_2d.csv) and [umap_digits_3d.csv](umap_digits_3d.csv) — sample exported 2D and 3D embedding coordinates.
- [umap_connectivity_2d.csv](umap_connectivity_2d.csv) and [umap_connectivity_3d.csv](umap_connectivity_3d.csv) — sample connectivity data for visualising relationships between points.

**Note on filenames:** the existing coordinate exports use the historical name `umap_digits_*`, while the notebook's main worked example uses penguin measurements. Treat these filenames as legacy names rather than evidence that the current exercise analyses handwritten digits.

## Taking it further

Try changing the UMAP settings, especially `n_neighbors` and `min_dist`, and compare the resulting layouts. Ask which groupings remain stable and which are sensitive to your choices. For an architectural application, the next step is to substitute an appropriate dataset and investigate what its variables actually measure.

For the underlying method and further examples, consult the [official UMAP documentation](https://umap-learn.readthedocs.io/en/latest/).

*Editorial note (26 October 2026): This README was expanded to describe the existing notebook; the notebook itself was not changed or rerun.*
