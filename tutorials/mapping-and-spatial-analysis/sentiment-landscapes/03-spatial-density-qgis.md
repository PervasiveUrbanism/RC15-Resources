# 3. Analysing Spatial Density in QGIS

[← Chapter 2: Collecting Flickr Data](02-collecting-flickr-data.md) · [Sentiment Landscapes overview](README.md)

In the previous chapter, we collected geolocated Flickr photographs. Each photograph appears as a point on the map. That is useful for showing *where* a photograph was taken, but when many points overlap it becomes difficult to judge *how many* photographs are associated with a particular area.

In this chapter we will replace the crowded point map with a regular grid. Each grid cell will receive a value: **the number of photographs located inside it**. We will then turn each cell into a single point carrying that count. These points will become the basis of our three-dimensional landscape in Grasshopper.

This process is called **spatial aggregation**. Instead of inspecting thousands of individual records, we group observations into geographical areas and calculate a summary value for each area.

By the end of this chapter, you should have a **CSV file with one row per grid cell**, containing the position of its centre and its photograph count. We will retain the QGIS grid layers as intermediate working files.

> **Before you begin:** This exercise uses QGIS 3 and its built-in Processing Toolbox. The steps are based on current QGIS documentation but have not yet been tested as a complete classroom workflow. The archived `Qgis/` folder in this repository contains example grids and centroid files, which are useful references rather than guaranteed matches for a new Flickr download.

## 3.1 Start with the photograph point layer

Open the QGIS project you saved in Chapter 2. Your SpatiaLite database should contain a point layer of geolocated Flickr photographs.

Zoom to the study area and open the layer's **Attribute Table**. Make a note of the total number of features, which we will compare against the grid counts later. Remember that every feature is a **photograph record**, not necessarily a unique photographer or a unique real-world place.

If you cannot retrieve fresh Flickr data, you can work with the supplied `london_photos.csv` instead:

1. In QGIS, choose **Layer → Add Layer → Add Delimited Text Layer**.
2. Select `london_photos.csv` from this tutorial folder.
3. Set the delimiter to **Tab** (the archived file is tab-separated despite its `.csv` extension).
4. Use `longitude` for X and `latitude` for Y.
5. Set the layer's source coordinate reference system (CRS) to **EPSG:4326 — WGS 84**.
6. Inspect the preview and add the points to the map.

The archived table contains **61,250 records**. This fallback is an alternative starting dataset; it is not the same selection used to generate all of the original example project's grid counts.

**Checkpoint:** the photograph points appear in the expected area of London, and you know how many records you are working with.

## 3.2 Choose a coordinate system suitable for the grid

We want to define a grid using dimensions such as **200 × 200 metres**. To do that sensibly, we need to work in a **projected coordinate reference system** whose units are metres. A geographic CRS such as EPSG:4326 uses longitude and latitude in degrees; a spacing of `200` in that system would not mean 200 metres.

For our London example, use **EPSG:27700 — OSGB36 / British National Grid**. It is suitable for working with metre-based distances in Great Britain.

Create a projected working copy of your photograph layer:

1. Right-click the photograph layer in the **Layers** panel.
2. Select **Export → Save Features As…**.
3. Set the output format to **GeoPackage** and save the file in your working `data/` folder, for example as `flickr_points_bng.gpkg`.
4. Set the output CRS to **EPSG:27700**.
5. Save the layer and make sure the reprojected points still appear in the correct part of the map.

Changing the **project CRS** only changes how layers are displayed together; saving a *reprojected layer* actually transforms its coordinates. We will use the reprojected copy for counting, while preserving the original Flickr data.

**Checkpoint:** the working point layer reports EPSG:27700 in **Layer Properties → Source**, and the points are still correctly located.

## 3.3 Create a regular grid

Open **Processing → Toolbox** and search for **Create grid**. This tool generates a regular set of shapes covering a defined extent.

Use these settings for a first experiment:

| Setting | Value |
| --- | --- |
| Grid type | **Rectangle (polygon)** |
| Grid extent | Draw a rectangle on the map covering your study area, or use a suitable layer extent |
| Horizontal spacing | **200** |
| Vertical spacing | **200** |
| Horizontal / vertical overlay | **0** |
| Grid CRS | **EPSG:27700** |
| Output | Save as `grid_200m.gpkg` in your `data/` folder |

The grid creates a series of rectangular **polygons**. A polygon is a closed geographical shape; in this case, each rectangle defines the area in which we will count photographs.

The 200-metre spacing is a useful starting choice, **not a universal optimum**. A small study area may benefit from smaller cells, while a city-wide study may need larger ones. Keep the boundaries of the grid slightly beyond the intended study area if you want to include all the outer cells.

**Checkpoint:** you can see a regular grid covering the study area, and its cells have dimensions of 200 projected metres on each side.

Reference: [QGIS — Create grid](https://documentation.qgis.org/3.44/en/docs/user_manual/processing_algs/qgis/vectorcreation.html#create-grid).

## 3.4 Count photographs within each cell

We now need to give every rectangle a numerical value.

In the Processing Toolbox, search for **Count points in polygon**. This tool takes a polygon layer and a point layer, then counts the points falling inside each polygon.

Configure it as follows:

| Setting | Value |
| --- | --- |
| Polygons | `grid_200m` |
| Points | Your reprojected Flickr photograph points |
| Weight field | Leave empty |
| Class field | Leave empty |
| Count field name | `photo_count` |
| Output | Save as `grid_photo_counts.gpkg` |

Run the tool and open the result's **Attribute Table**. Every grid cell now contains a `photo_count` value. Some cells may have hundreds of photographs, others only a few, and some may contain **zero**.

This is the analytical step that turns individual photograph locations into an easier-to-read spatial distribution.

![Example of an archived gridded spatial result](Images/Heightfield%201.png)

*Illustration from the source project, included for visual reference. Your own result will depend on the study area, dataset and grid resolution.*

**Checkpoint:** the new polygon layer has the same number of cells as the input grid and includes the `photo_count` field. Inspect one busy cell and one empty cell to check that their counts are plausible.

Reference: [QGIS — Count points in polygon](https://doc.qgis.org/3.44/en/docs/user_manual/processing_algs/qgis/vectoranalysis.html#count-points-in-polygon).

## 3.5 Visualise the counts in two dimensions

Before building a 3D landscape, it is helpful to inspect the aggregated data in QGIS.

Right-click `grid_photo_counts` and open **Properties → Symbology**. Change the renderer to **Graduated** and choose `photo_count` as the value field. Apply a sequential colour ramp, so that low values are visually lighter and high values are darker.

Experiment with the classification method. **Equal Interval** divides the numerical range into equal parts, whereas **Quantile** distributes features among classes with similar numbers of cells. If a small number of cells contain very large counts, these approaches can produce quite different visual impressions.

Try toggling the original Flickr point layer on and off. The grid reveals broader patterns of concentration that were obscured by overlapping symbols, but it also conceals differences *within* each cell.

**Checkpoint:** you can identify the highest-count areas and explain how the grid representation differs from the original point map.

## 3.6 Try a second grid size

Now repeat **Create grid** and **Count points in polygon** using **400 × 400 metres**, keeping the *same study extent* and *same input photographs*. Save the results separately, for example `grid_400m.gpkg` and `grid_400m_counts.gpkg`.

Compare the two maps. The 200-metre grid reveals more local variation, while the 400-metre grid combines more observations and usually produces broader zones of concentration. The latter does **not** simply rescale the former: aggregation changes the values we calculate, and changing the grid origin can also change which photographs belong together.

There is no single correct grid size. Choosing a cell size is part of your analytical and representational decision-making, not merely a display preference.

For the rest of this tutorial, select **one grid** as your working version. We will use the 200-metre example in the filenames below, but you may choose another size if it suits your area of interest.

## 3.7 Check the counts before proceeding

The sum of all `photo_count` values should broadly correspond to the number of valid input photograph points within the grid's coverage.

It may not equal the total number of records in the source database. Some photographs might lie **outside** the chosen grid extent or have missing/invalid geographic information. QGIS's **Count points in polygon** documentation also notes that points exactly on polygon boundaries are ignored; do not treat an apparent mismatch as proof that the algorithm failed.

If the totals differ unexpectedly, first inspect the grid coverage, the point layer, its CRS and any active layer filters.

Also pay attention to **zero-count cells**. A cell with zero is an actual part of the study area with no recorded photographs in this dataset. It is not a missing row. Keeping these cells matters because Grasshopper will need the complete grid to construct a correctly ordered surface.

## 3.8 Convert grid cells into centre points

Grasshopper will work with one point for each grid cell rather than the full rectangle geometry. We can use the **centroid**, the geometric centre of a shape, as a representative position for its count.

In the Processing Toolbox, search for **Centroids**:

1. Choose your final counted grid, such as `grid_photo_counts`, as the input layer.
2. Save the output as `grid_centroids.gpkg`.
3. Open the result's Attribute Table.

Each rectangle is now represented by a point at its centre. Crucially, QGIS carries over the polygon's attributes, including `photo_count`.

We are not moving the actual photograph locations. We are creating **new representative points** whose positions correspond to grid cells, and whose numerical values summarise the photographs within them.

**Checkpoint:** there is exactly one centroid per grid cell. Every centroid has a `photo_count` value, including zero where no photographs were counted.

Reference: [QGIS — Centroids](https://doc.qgis.org/3.44/en/docs/user_manual/processing_algs/qgis/vectorgeometry.html#centroids).

## 3.9 Export the centroids as a CSV for Grasshopper

We now have everything needed for the next chapter: one position and one height value per grid cell.

In the Layers panel, right-click the centroid layer and choose **Export → Save Features As…**.

1. Set **Format** to **Comma Separated Value (CSV)**.
2. Choose the filename `grid_centroids.csv` in your working `data/` folder.
3. Set the **CRS** to **EPSG:4326 — WGS 84**, which will give us longitude and latitude coordinates for Heron's geographic conversion in Grasshopper.
4. In the CSV export options, set **Geometry** to **AS_XY** (export geometry as X and Y coordinate columns). Keep the `photo_count` field and the grid's row/column indices if they are available.
5. Save the file. Open it in a text editor or spreadsheet application and verify that it contains coordinate columns alongside `photo_count`.

For geographic coordinates, **X is longitude** and **Y is latitude**. A CSV contains values but does not by itself preserve a QGIS layer's full geometry and CRS metadata, so record EPSG:4326 in your project notes.

Most importantly, **keep a predictable point order** when transferring the data to Grasshopper. A surface built through a rectangular point grid requires the positions to be arranged consistently by row and column. If your exported table includes fields such as `row_index` and `column_index`, retain them; in Grasshopper we will use these to verify the point ordering before fitting a surface. Do not remove rows with zero counts.

> **Why not create the surface directly in QGIS?** QGIS has excellent mapping and interpolation tools, but we want to explore how the same data can generate a controllable three-dimensional representation. Separating the spatial analysis from the model-building stage makes both processes easier to understand and adjust.

Reference: [QGIS — Exporting vector layers](https://docs.qgis.org/3.44/en/docs/user_manual/managing_data_source/create_layers.html).

## Your result and what comes next

You should now have three main outputs:

- **A counted polygon grid** showing the number of photographs in each cell.
- **A centroid layer** carrying the same counts as point attributes.
- **A CSV file** containing centroid positions and counts, ready for Grasshopper.

Save your QGIS project and keep the intermediate GeoPackages. They will help you diagnose any unexpected results later.

In **Chapter 4 — Building a 3D Landscape in Grasshopper**, we will use the Heron plugin to convert longitude and latitude to Rhino coordinates. Then we will use `photo_count` as an elevation value, generate a point field and fit a surface through it.

Remember the central distinction: **the peaks will represent concentrations of Flickr photographs, not actual topography or a direct measure of how much people like those places**.
