# 4. Building a 3D Landscape in Grasshopper

[← Chapter 3: Analysing Spatial Density](03-spatial-density-qgis.md) · [Sentiment Landscapes overview](README.md)

In QGIS, we replaced thousands of overlapping Flickr photographs with a regular grid. Each cell now has a number: the count of photographs found inside it. We also exported a CSV containing the centre of every cell and its count.

In this chapter, we will use those numbers to construct a **three-dimensional landscape** in Rhino and Grasshopper. The geographical position of each grid cell determines its horizontal position; the number of photographs determines its elevation. We will connect these elevated points into a continuous surface.

![Landscape example from the original project](Images/ViewCapture20250712_174129.png)

*An archived example of the intended result. Your landscape will differ according to the study area, grid and selected height scale.*

## 4.1 Prepare Rhino, Grasshopper and Heron

We need **Rhino 8**, its visual-programming environment **Grasshopper**, and the **Heron** plugin. Heron provides tools for translating real-world geographical coordinates into Rhino coordinates. The archived definition, [`Rhino/Heron.gh`](Rhino/Heron.gh), is available for inspection; it is not necessary to open that complex file before understanding the basic process.

Install Heron through Rhino's **PackageManager** (search for `Heron`), then restart Rhino if the installation requests it. Open Grasshopper and confirm that the Heron components are available. For a reproducible exercise, note your Rhino and Heron versions.

Start a **new Rhino document** and set its units to **metres**, since we will be working with a city-sized area. Open an empty Grasshopper definition and save it in your working folder as `Sentiment-Landscape.gh`.

Heron's [project documentation](https://github.com/blueherongis/Heron) explains its geographic conversion tools. The archived definition records Heron 0.4.4 and Rhino 8.18, but these are **source-file versions**, not a newly tested compatibility combination. The exact component appearance may differ between installations.

**Checkpoint:** Grasshopper opens, the Heron tab is present, and the Rhino document units are metres.

## 4.2 Understand the input CSV

Open the `grid_centroids.csv` you created in Chapter 3 in a text editor. It should contain one row for **every grid cell**, including those with zero photographs. Its essential information is:

| Data | Meaning | How we will use it |
| --- | --- | --- |
| Longitude (X) | East–west geographic position | Locate each centroid through Heron |
| Latitude (Y) | North–south geographic position | Locate each centroid through Heron |
| `photo_count` | Photographs counted inside the cell | Determine the point's elevation |
| Row/column indices, where present | Position within the original rectangular grid | Reconstruct the correct point order |

Your CSV may contain additional fields and may name the coordinate columns differently. **Inspect the header rather than assuming fixed column numbers.** The archived `Qgis/CentrHeron3.csv`, for example, uses `p_id_count`, not our new `photo_count` name.

We need a consistent pair of lists: one list of geographic positions and one list of numerical counts. Both lists must have the same number of elements and correspond **row by row**.

## 4.3 Read the CSV into Grasshopper

Start with a small, understandable sequence of standard Grasshopper components:

1. Add **File Path** and point it to your `grid_centroids.csv`.
2. Connect it to **Read File** to read the text.
3. Separate the header row from the data rows. In a simple numeric CSV, **Text Split** can separate rows into fields using a comma.
4. Inspect the first few rows with **Panel** components. Identify which columns contain longitude, latitude and `photo_count`.
5. Extract the three columns into separate lists and convert the text values to numbers using the appropriate Grasshopper conversion components.

A standard **Text Split → List Item** arrangement can work for this controlled, numeric export. It is not a general-purpose CSV parser: quoted commas, unexpected delimiters and empty numeric fields require more care. If splitting produces incorrect columns, repair the QGIS export instead of silently dropping records.

Use three temporary panels to inspect your **longitude**, **latitude** and **count** lists. Check the first row against the CSV file. Use **List Length** to check that all three have exactly the same number of items.

> **Keep all zero-count cells.** Deleting them would create gaps in the rectangular lattice and could prevent Grasshopper from generating a correct surface.

**Checkpoint:** the lists contain the same number of records, and you can identify a known CSV row correctly in Grasshopper.

## 4.4 Position the points geographically with Heron

The CSV uses **EPSG:4326**, a geographical coordinate system in which longitude and latitude are expressed in decimal degrees. Rhino geometry, by contrast, works in a flat local coordinate system and needs numerical X/Y positions in its document units.

Heron provides the conversion between these systems.

1. Add Heron's **Set EarthAnchorPoint** component. Define a sensible geographic anchor near the centre of the study area, using the documented latitude/longitude inputs. This establishes the relationship between the Rhino model and a location on Earth.
2. Add Heron's **Decimal Degrees to XY** component.
3. Connect the **latitude list to its Latitude (LAT) input** and the **longitude list to its Longitude (LON) input**. Do not swap them: a London longitude is around zero, while latitude is around 51 degrees.
4. Connect the resulting `xyPoint` output to a **Point** parameter or a preview so you can inspect the positions in Rhino.

[Heron's documentation](https://github.com/blueherongis/Heron) notes that setting the Earth Anchor Point is important for its geographic tools. Its **Decimal Degrees to XY** component expects WGS84 longitude and latitude, so the EPSG:4326 export from QGIS was deliberate.

At this point, **all points should lie on a flat plane**. Zoom to the geometry in Rhino. You should recognise the rectangular extent of the study area, even though only the cell centres are visible. Measure a few neighbouring distances; for a 200-metre grid they should be approximately 200 metres apart in a correctly configured metre-based model. Projection and Earth Anchor settings can introduce small differences, so do not assume exactly 200.000 metres.

**Checkpoint:** you can see a regularly spaced, planar point grid in Rhino. Fix unexpected geographic positions *before* adding height.

## 4.5 Turn photograph counts into elevation

The counts are meaningful as **data values**, but they are not physical heights. A cell containing 500 photographs does not imply a 500-metre hill. We need to choose how the numbers are **mapped** to a suitable height range.

In Grasshopper:

1. Connect the `photo_count` list to **Bounds** to discover the minimum and maximum count.
2. Add **Remap Numbers**, using the count values and their source domain.
3. Create a target domain, for example **0 to 200 metres**, and connect it to the remapping component.
4. Use **Unit Z** with the remapped values to create vertical movement vectors.
5. Connect the planar Heron points and these vectors to **Move**.

The result is an elevated point field: each cell centre remains at the correct X/Y location, but its Z coordinate now expresses its count on the chosen visual scale.

**The 0–200-metre example is a graphic exaggeration**, not a measured elevation. You can make the resulting landscape flatter or more dramatic by changing the target domain. Label the transformation when presenting the result.

For a first exercise, preserve **zero counts as zero elevation**. Depending on the output of `Bounds`, you may need to construct the source domain starting at zero rather than letting the minimum positive count map to the lowest height. If all counts are identical, there is no meaningful numerical range to remap: give the points a constant height instead.

**Checkpoint:** compare a high-count cell and a zero-count cell. Their elevations should reflect the chosen mapping, while their X/Y positions should not change.

## 4.6 Arrange the grid before creating the surface

We now have the right *number* of points, but one more condition matters: **their order**.

A surface generated from a point grid needs to know which points are neighbours. If the input list zigzags between rows, the surface may twist or fold even though all the coordinates are correct.

Think of a small grid with **four columns and three rows**:

```text
  1 —  2 —  3 —  4
  5 —  6 —  7 —  8
  9 — 10 — 11 — 12
```

This is a conceptual example, not a required indexing system. The exact list direction depends on the intended Grasshopper surface U direction. The essential point is to use **one consistent traversal** of the rectangle.

If the CSV contains `row_index` and `column_index`, sort or reconstruct the list using those identifiers. Do not trust the original QGIS export order without checking it. If your file lacks these fields, return to QGIS and generate or retain explicit row/column identifiers, or develop a carefully checked spatial sort using the grid positions. Do not rely on a simple latitude sort where the geographic conversion introduces small offsets.

Preview numbered points or join a sample row with a **Polyline** to confirm that successive list items follow one logical direction across the grid.

The number of points should equal:

```text
number of columns × number of rows
```

The archived `CentrHeron3.csv` has **2,847 positions, arranged 73 × 39**. That is an example of a complete rectangular lattice, but your dataset may have different dimensions.

**Checkpoint:** every expected grid position exists, the list order is regular, and the number of points matches the product of the row and column counts.

## 4.7 Fit a continuous surface

Grasshopper's **Surface From Points** component creates a surface from a regularly arranged point grid.

1. Add **Surface From Points**.
2. Connect the **ordered, elevated points** to its **Points (P)** input.
3. Set **U Count (U)** to the number of points in the surface's U direction. This depends on the traversal you established, not simply on which dimension is larger.
4. Try **Interpolate (I) = True** to construct a surface that follows the input sample points.
5. Preview the resulting surface in Rhino and hide temporary point previews if necessary.

If the points are ordered row by row, test the U count against your actual list orientation. If the surface twists or refuses to build, inspect the point order, count and Grasshopper data-tree structure before changing the heights. A successful surface requires a complete, ordered point grid; **Flatten** may be appropriate if the points are currently divided into branches, but only after verifying their intended sequence.

Reference: [Surface From Points — inputs and outputs](https://grasshopperdocs.com/components/grasshoppersurface/surfaceFromPoints.html).

The surface creates a continuous shape **between discrete sample locations**. It is a modelled visualisation of aggregated counts, not a measured elevation surface and not a claim about precise values at unsampled locations.

## 4.8 Experiment with the shape

Now try three small changes and observe their effects:

- **Height scale:** switch between target ranges such as 0–50, 0–200 and 0–500 metres, leaving the footprint unchanged.
- **Grid resolution:** compare results from your 200-metre and 400-metre QGIS grids, rebuilding the point arrangement and dimensions for each.
- **Outliers:** inspect whether a small number of exceptionally high-count cells dominate the surface. Consider an explicitly labelled capped or logarithmic height transformation as an experiment, not as a hidden correction.

These choices strongly influence the appearance of the landscape. Smaller cells may produce sharper local changes, while larger cells generally create broader shapes. Taller vertical exaggeration can make a difference look more dramatic than its original numerical scale.

Keep the **original counts unchanged** in the CSV. Any visual remapping should remain visible in the Grasshopper definition so you can adjust it and explain it.

## 4.9 Save the working landscape

Save your Grasshopper definition and Rhino document in your own project folder. Keep `grid_centroids.csv` alongside them, and record the file paths, Earth Anchor Point, grid size, count field and height range you used.

The original archive provides [`Rhino/Heron.gh`](Rhino/Heron.gh) for further study. It also includes mapping, preview, contours and baking branches. It may reference old absolute file paths and plugins such as Human or MeshEdit; **do not assume it will open as a fully functioning classroom definition without relinking and testing**. It is best used as a visual reference after constructing the simpler sequence yourself.

If your definition fails, check the workflow in stages: **CSV values → geographic conversion → flat points → elevated points → surface**. A problem at an earlier stage cannot be fixed reliably by adding components later.

## What comes next

We now have a three-dimensional surface whose height reflects the **number of recorded photographs per geographical grid cell**.

In **Chapter 5 — Representing the Landscape**, we will explore ways of bringing the city back into the image: a QGIS map export, OpenStreetMap vectors through Heron or aerial imagery. We will also generate contour curves, bake the geometry into Rhino, prepare a 2D drawing and bring it into Illustrator for the final graphic composition.

The central principle remains the same: **location determines X/Y, aggregated data determines Z, and our representation choices determine how the resulting landscape is perceived**.
