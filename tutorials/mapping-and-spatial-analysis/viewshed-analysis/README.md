# Visibility and Viewshed Analysis in QGIS

Part of **RC15 Resources**, the permanent teaching resource library for Pervasive Urbanism.

**Software:** QGIS and the Visibility Analysis plugin  
**Level:** Intermediate — familiarity with raster and vector layers is helpful  
**Format:** Practical tutorial using an existing QGIS project and processing model  
**Original collection:** `240217_ViewshedAnalysis`  
**Verification status:** The supplied files and processing model have been inspected, but the workflow has **not yet been executed in QGIS**. Desktop testing and screenshots remain to be completed.

[Browse this topic](../README.md) | [Library home](../../../README.md)

**Related exercise:** [Terrain Analysis in QGIS — Slope, Aspect and Solar Orientation](../terrain-slope-aspect/README.md) uses a separate copy of the same sample terrain to investigate buildable gradients and solar orientation.


## Introduction: What can we see from here?

Consider standing on a hill or at an observation point and looking across a landscape. Some parts of the terrain are visible; others are concealed by intervening slopes. A **viewshed** is a map of the locations that could theoretically be seen from a particular observer position.

Viewshed analysis connects a simple spatial question — *what is visible from here?* — to digital terrain data. It can support investigations into viewpoints, visual connections, landscape interventions and the potential visibility of new buildings. The result is not a photograph or a simulation of human perception. It is a geometrical calculation based on an elevation model and a set of assumptions.

In this exercise, we will use a **digital elevation model (DEM)**, a point representing the observer and a QGIS processing model to calculate and interpret a viewshed. We will then change the observer settings to see how the result responds.

### What you will learn

By the end, you should be able to distinguish a DEM from a viewshed raster, identify the role of an observer point, run or inspect a two-stage QGIS processing model, and explain how observer height, analysis radius and terrain resolution influence the result. You should also be able to identify situations in which a terrain-only viewshed would give an incomplete account of visibility.

## 1. Prepare the project

Download the complete folder and keep its contents together. Start with these files:

| File | Purpose |
| --- | --- |
| [Viewanalysis.qgz](Viewanalysis.qgz) | Original QGIS project |
| [SmallHeightMap.tif](SmallHeightMap.tif) | Elevation raster used as the terrain input |
| [Viewpoints.shp](Viewpoints.shp) | Observer-point geometry, accompanied by its `.dbf`, `.shx` and `.prj` files |
| [Bbox.shp](Bbox.shp) | Study-area boundary, also stored as a multi-file shapefile |
| [Viewshed.model3](Viewshed.model3) | Two-stage QGIS Processing model |
| [Viewshed1.zip](Viewshed1.zip) | Archived viewshed output; inspect its contents before using |
| [OutputFile.tif](OutputFile.tif) | Another supplied raster output; its role must be verified |

The [Links folder](Links) also contains `Grid.gpkg` and `ZonalStats.gpkg`. They are retained as supporting data, but their precise role in this viewshed exercise has not been established.

Open **`Viewanalysis.qgz`** in QGIS. If QGIS reports missing layers, use its repair options to point them to the files in this folder. Do not assume that the paths saved on the original computer will work on yours.

In the Layers panel, identify the terrain raster, viewpoint and study boundary. Switch individual layers on and off, and inspect their properties. Confirm that the viewpoint lies inside the relevant terrain coverage.

**Checkpoint:** You can point to the elevation raster and the observer location, and explain the difference between them.

## 2. Understand the terrain data

A DEM is a raster grid in which each cell stores an elevation value. A viewshed algorithm compares the elevation of the observer with elevations along sightlines across that grid. Intervening high ground can obstruct more distant cells.

Inspect **`SmallHeightMap.tif`** using *Layer Properties → Information*. Note its coordinate reference system (CRS), pixel size, extent, units and NoData value. Its accompanying metadata reports approximate valid elevation statistics of **26.15 to 80.18**, but these figures alone do not establish the elevation datum or the suitability of the source.

The supplied viewpoint and boundary shapefiles use a projected **Web Mercator** CRS with coordinates expressed in metres. A projected CRS is essential for this plugin: using longitude and latitude directly as if they were distances would make the analysis invalid. However, Web Mercator is not locally distance-preserving, so an appropriate local projected CRS may be preferable for accuracy-sensitive studies. Before changing the CRS, verify the raster's native projection and reproject the relevant layers properly rather than merely assigning a different CRS label.

**Checkpoint:** You know which layer supplies elevations and whether its coordinate units are appropriate for a distance-based analysis.

## 3. Install the Visibility Analysis plugin

The original model uses **Visibility Analysis**, developed by **Zoran Čučković**. This is a third-party QGIS plugin, not a standard built-in Processing algorithm.

Install it through *Plugins → Manage and Install Plugins…*, search for **Visibility Analysis**, and enable it. Then open the *Processing Toolbox* and look for the visibility algorithms.

The official [QGIS plugin listing](https://plugins.qgis.org/plugins/ViewshedAnalysis/) distinguishes versions for QGIS 3 and 4. At the time of this review, **1.9.2** is listed for QGIS 3 and **1.9.3** for QGIS 4. Choose a compatible release rather than assuming the newest version will work with an older QGIS installation.

For the plugin's explanation of its algorithm and settings, consult the [developer's documentation](https://www.zoran-cuckovic.from.hr/QGIS-visibility-analysis/help_qgis3.html).

**Checkpoint:** The Processing Toolbox exposes **Create observer points** (or a closely equivalent label) and **Viewshed** from the Visibility Analysis provider. If they are absent, check that the plugin is installed, enabled and compatible before opening the model.

## 4. Understand the supplied processing model

A **Processing model** connects several GIS operations into a repeatable workflow. The supplied [`Viewshed.model3`](Viewshed.model3) contains two linked algorithms:

**Input DEM + input viewpoint → Create viewpoints → Viewshed → output raster**

The first operation, `visibility:createviewpoints`, prepares the observer point with standardised visibility parameters. The second, `visibility:viewshed`, calculates visibility over the elevation raster using that prepared observer. The output is a raster rather than a collection of vector polygons.

The model contains these settings:

| Parameter | Value saved in the model | Meaning |
| --- | --- | --- |
| Observer height | **1.6 m** | Eye height above the terrain at the viewpoint |
| Target height | **0 m** | Visibility assessed at the terrain surface, rather than at the top of an object |
| Analysis radius | **800 m** | Maximum distance around the observer considered |
| Earth curvature | **Off** | Curvature correction is disabled |
| Refraction | **0.13** | Stored in the model, but not applied when curvature correction is off |

The viewshed step also stores numerical options for analysis and aggregation. Their interface labels and resulting behaviour should be confirmed in the installed plugin before interpreting the output as definitively binary or cumulative.

Notice that **1.6 m is added to the terrain elevation at the observer**, not measured from sea level. Likewise, increasing the target height changes what must be visible: a rooftop might be visible from a viewpoint even when the ground beneath it is hidden.

### Open and run the model

In QGIS, choose *Processing → Graphical Modeler* (the name may vary slightly by version), then open [`Viewshed.model3`](Viewshed.model3). Inspect both operations and how their inputs and outputs are connected. If QGIS shows unavailable algorithms, resolve the Visibility Analysis plugin dependency before proceeding.

Run the model with **`SmallHeightMap.tif`** as the DEM and **`Viewpoints.shp`** as the input point layer. Choose a new output filename, such as `viewshed_test.tif`, so that the original example data remains unchanged. Run the process and inspect the messages for errors.

**Checkpoint:** You have an output raster layer and can distinguish successfully calculated cells from NoData cells.

## 5. Read and represent the result

A basic *binary viewshed* distinguishes **visible** from **not visible** areas. It does not measure the quality of a view, and its colours do not have a natural meaning: you choose the symbology.

Inspect the output raster's unique values and NoData settings before styling it. If it is binary, give visible terrain a clear colour, leave non-visible terrain subdued and display the DEM underneath as a hillshade or elevation background. Make sure the legend distinguishes **not visible** from **not assessed / NoData**.

The plugin can also combine visibility from several observer points into a cumulative raster, where the meaning of the values differs from a single-observer result. Always establish which output mode was actually used before interpreting raster values.

Compare your result with the supplied [`Viewshed1.zip`](Viewshed1.zip) only after extracting and checking its contents. The existing `Viewshed1.tif.aux.xml` metadata suggests that a 0–1 raster was produced previously, but an XML metadata file on its own is **not proof that the archived raster matches the current model**.

**Checkpoint:** Your map has a labelled observer, a scale bar, a clear legend and an explanation of what counts as visible.

## 6. Experiment with the assumptions

A useful viewshed exercise goes beyond pressing *Run*. Repeat the analysis with one change at a time:

1. **Move the observer** from a lower location to higher ground. Does the visible area increase everywhere, or does the shape of the terrain matter more than simple elevation?
2. **Change the observer height** from 1.6 m to, for example, 10 m. Which previously hidden locations become visible?
3. **Change the target height** to represent the top of a proposed feature rather than ground level. Does this change your conclusion?
4. **Change the analysis radius**, recording the value used in each output. Do not confuse a smaller search radius with reduced visibility caused by terrain.

Keep the same DEM and symbology when comparing the results. If you change several parameters at once, you will not know which assumption caused the difference.

As a small architectural investigation, choose two possible observation points or building locations and prepare a pair of comparable viewshed maps. Explain which location has the more relevant visual connections for your design question, not simply which produces the largest coloured area.

## 7. Interpret the limits critically

A result is only as good as the model behind it. In particular:

- **Terrain is not the entire city.** A DEM may omit buildings and trees. To account for those obstructions you would need suitable surface-height data, such as a digital surface model (DSM), and an appropriately tested method.
- **Resolution matters.** Small ridges, walls or parapets may be absent from a coarse elevation grid.
- **Curvature, distance and projection matter.** Curvature is disabled in the supplied model; changing study scale or CRS may require revisiting that assumption.
- **Visibility is not perception.** A theoretically visible location may be distant, obscured by weather, visually insignificant or difficult to recognise.
- **Observer and target heights are design decisions.** A pedestrian viewpoint, a roof terrace and a tall structure pose different questions.

A good analytical drawing therefore states its observer position, heights, radius, terrain source, CRS and important exclusions. It should not present a coloured viewshed as an objective measure of visual experience.

## Troubleshooting

**Model algorithms are missing:** Confirm that **Visibility Analysis** is installed and enabled, and that its version matches your QGIS installation. The model uses `visibility:createviewpoints` and `visibility:viewshed`.

**Layers cannot be found:** Relink the raster and vector files. A shapefile depends on its accompanying `.shp`, `.shx`, `.dbf` and `.prj` files; keep them together.

**Unexpectedly small or empty result:** Check that the viewpoint falls within valid DEM coverage, confirm coordinate reference systems and units, inspect NoData areas and check the radius.

**The map looks entirely one colour:** Inspect the actual raster value range and NoData mask before changing symbology. Do not assume that 0, 1 and NoData are interchangeable.

**Different computers produce different results:** Record QGIS and plugin versions, input sources, CRS, raster resolution and saved parameters, then compare the Processing log.

## Files, references and next steps

The original project, model and assets are retained in this folder. QGIS project files and raster outputs should be reviewed in the desktop application before this tutorial is considered technically complete.

Useful references:

- [Visibility Analysis — official QGIS plugin directory](https://plugins.qgis.org/plugins/ViewshedAnalysis/)
- [Visibility Analysis — developer's QGIS 3 documentation](https://www.zoran-cuckovic.from.hr/QGIS-visibility-analysis/help_qgis3.html)
- [QGIS Processing Model Designer documentation](https://docs.qgis.org/latest/en/docs/user_manual/processing/modeler.html)

**Outstanding desktop work:** Load the QGIS project; verify raster properties, CRS and source paths; install the plugin and run the supplied model; check the saved output files and model settings; capture actual screenshots of the terrain, model, viewshed and comparison exercise. Only then confirm a tested QGIS/plugin version and finalise the illustrations.
