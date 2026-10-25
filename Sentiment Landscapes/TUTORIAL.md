# Sentiment Landscapes: from photo locations to a drawn landscape

**First tutorial draft — 25 October 2026.** Based on inspection of the supplied project, data and Grasshopper definition. The full workflow has not yet been run in the applications.

[Resource overview](README.md) · [Files not transferred and Drive links](FILES-NOT-TRANSFERRED.md)

![Existing Rhino landscape output](Images/ViewCapture20250712_174129.png)

## What you will make

Turn a set of geolocated photographs into a grid of values, use those values to lift points into a three-dimensional landscape, and develop a final illustration with contours, colour and a map background.

By the end, you should be able to:

- Load longitude/latitude records in QGIS and check their coordinate system.
- Read and rebuild a spatial count on a regular grid.
- Pass ordered grid centres and values to Grasshopper.
- Generate a heightfield and contours, then compose a labelled illustration.

The project title is **Sentiment Landscapes**. The inspected fields contain photo locations and counts; they do not contain a sentiment score or a documented sentiment-analysis method. In this draft, height represents photographic activity. Any later interpretation of emotion needs its own method and evidence.

**Level:** intermediate. You should be comfortable opening QGIS layers and following a Grasshopper definition.

## 1. Prepare the files and software

Keep this folder's layout intact and work on copies of the original projects. Save your own outputs under a new working folder.

| Software / dependency | Evidence in the supplied files |
| --- | --- |
| QGIS | Project saved with 3.40.6 Bratislava. This identifies the source version; it is not a newly tested compatibility claim. |
| Rhino with Grasshopper and Python 3 | Grasshopper library metadata records 8.18.25100.11001; the definition contains a Python 3 Script component. Start with Rhino 8. |
| Heron | Definition records 0.4.4. |
| MeshEdit | Definition records assembly 2.0.0.0. |
| Human | Definition records assembly 1.7.3.0 and display version 1.3.1; confirm the matching installed package. Used for baking components. |
| Illustrator | Required for the supplied AI compositions; original version unconfirmed. |
| Photoshop | Optional, for editing the supplied PSD files. |
| Noise plug-in | Optional extension only: the two NoiseFieldSim definitions record a Noise assembly at 1.0.0.0. |

Check missing-component messages when opening a definition. Recorded versions are evidence from the archive, not a verified installation recipe. [Heron's project documentation](https://github.com/blueherongis/Heron) explains its GIS import and EarthAnchorPoint tools.

There are two useful starting routes:

- **Use existing results:** start with `Qgis/CountBy200Grid.gpkg`, `Qgis/CountBy200GridPT.gpkg` and `Qgis/CentrHeron3.csv`. These smaller files are included.
- **Rebuild the analysis:** use photo records and a grid. Restore the original databases from [Drive](FILES-NOT-TRANSFERRED.md) if you want to investigate the original counts.

The included `london_photos.csv` has 61,250 records, while the existing centroid counts sum to 517,804. Their provenance and filtering have not been reconciled. Recounting the included CSV will produce a separate analysis and should not be expected to reproduce the supplied heightfield.

## 2. Open the QGIS project and identify its layers

Open `Qgis/SenitmentLandscapes.qgz` (the filename's original spelling is preserved). Save a working copy before editing.

If QGIS reports unavailable sources, use [the missing-file note](FILES-NOT-TRANSFERRED.md). Relink included files to your local folder. Leave unavailable photo databases and the absent `BBox.gpkg` layer disabled while exploring the included results.

Inspect the included layers:

| File | Layer | Features | Purpose |
| --- | --- | ---: | --- |
| `Grid200m.gpkg` | `grid` | 2,847 | Original coarser grid |
| `Grid100m.gpkg` | `grid` | 11,310 | Original finer grid |
| `CountBy200Grid.gpkg` | `joined_layer` | 2,847 | Grid polygons with `p_id_count` |
| `CountBy200GridPT.gpkg` | `centroids` | 2,847 | Grid centres with the same value field |
| `JoinedLayerpoints.gpkg` | `countby200grid__joined_layer` | 2,847 | Point export recorded as EPSG:4326 |
| `CornerPts.gpkg` | `vertices` | 5 | Boundary vertices |

The project display CRS is EPSG:3857. Several grid layers carry a custom GeoPackage CRS identifier and the project describes them as EPSG:6871, which includes a vertical reference. The saved grid bounds step by 200 projected coordinate units; these should not be described as exact 200-metre ground distances in London.

**Checkpoint:** inspect Layer Properties and verify that layers overlap in the expected London location. A project display CRS alone does not establish that every layer's source CRS is correct. Reprojecting coordinates and assigning a CRS label are different operations.

## 3. Load the photo table

To inspect or rebuild from the included table, use QGIS's delimited-text import:

1. Select `london_photos.csv`.
2. Set the delimiter to **Tab**. Despite the extension, this file is tab-separated.
3. Choose point coordinates: X = `longitude`, Y = `latitude`.
4. Set the source geometry CRS to **EPSG:4326**.
5. Check the preview before adding the layer.

Fields include `id`, `title`, `tags`, `date_taken`, `latitude`, `longitude` and `url_s`. An initial unnamed column stores a row index. The file includes metadata and image URLs, not a local archive of all photographs.

**Checkpoint:** expect 61,250 table records. Inspect a few mapped locations and remove or investigate invalid records in your working copy. Avoid treating an empty title or tag as evidence of a particular emotion.

See the [QGIS delimited-text documentation](https://docs.qgis.org/3.40/en/docs/user_manual/managing_data_source/opening_data.html#importing-a-delimited-text-file).

![Original QGIS view of photo labels](Images/Screenshot%202025-07-12%20173724.png)

## 4. Understand or rebuild the grid count

For the existing result, style `CountBy200Grid.gpkg` with a graduated renderer using `p_id_count`. Compare a linear classification with a classification that makes smaller counts easier to see. Record your class breaks.

To build a new result from the included photo table:

1. Reproject a working copy of the photo points to an appropriate projected CRS for your study. For a new London measurement workflow, select and document a suitable local metric CRS.
2. Use **Create grid**, choosing rectangular polygons, your study extent and a documented spacing. An extent taken from a transformed copy of the included grid can provide a starting study area.
3. Run **Count points in polygon** with the new grid and photo points. Leave weighting and unique-class fields unset for a simple record count.
4. Name the result field `p_id_count` and save the output as a new GeoPackage.
5. Create polygon centroids and retain the grid ID, row/column indices and count.

This is a reconstruction exercise, not a claim about the original processing history. QGIS documents [Create grid](https://docs.qgis.org/3.40/en/docs/user_manual/processing_algs/qgis/vectorcreation.html#create-grid) and [Count points in polygon](https://docs.qgis.org/3.40/en/docs/user_manual/processing_algs/qgis/vectoranalysis.html#count-points-in-polygon).

**Checkpoint:** compare the sum of counts with the number of valid input points inside the study extent. Inspect shared-boundary cases before assuming exact equality. Explain what one counted record represents.

## 5. Inspect the centroid CSV before Grasshopper

The existing `CentrHeron3.csv` contains longitude in `X`, latitude in `Y`, grid indices and `p_id_count`. It has 2,847 data rows: **73 columns × 39 rows** of grid positions.

The file is comma-separated and has a header. Its first data row begins with:

- X: `-0.06854168471588`
- Y: `51.5443913338738`
- `p_id_count`: `70`

There are 190 blank count entries. Nonblank counts range from 1 to 21,558. The definition includes a Python conversion that substitutes 0.0 when conversion fails. For this exercise, explicitly choose how to treat blanks; replacing them with zero is a modelling assumption until their meaning is confirmed.

Keep one value per grid position. Removing blank rows would break the rectangular point lattice. When making a new export, keep longitude/latitude in EPSG:4326 for the existing Heron conversion path, and keep a predictable order using `col_index` and `row_index`. Confirm which index changes fastest against the original CSV.

## 6. Relink and inspect the Grasshopper definition

Open a new Rhino document, choose and record its units, and open `Rhino/Heron.gh`. Disable solving while repairing paths and inspecting download controls.

1. Find the File Path feeding **Read File**. Its saved path ends in `Qgis/CentrHeron3.csv`. Replace it with your local copy.
2. Locate the asset-folder panels. Replace old Dropbox paths with your local `Rhino/assets/` folder if those branches are needed.
3. Keep REST download triggers off while setting up. The data-to-heightfield exercise can be examined before fetching new map context.
4. Inspect **Set EarthAnchorPoint** and the **Decimal Degrees to XY** conversion components. Use an explicit shared geographic anchor for the point and background branches. Do not rely only on panel nicknames: some saved north/south labels disagree with their numeric ordering.
5. Enable solving and follow the CSV branch: header removal, text splitting, coordinate extraction, numeric conversion and point movement.

In the supplied CSV, the count is field index **10** when indexing from zero. The definition contains a List Item selection at 10. If you change the column order, update the selection.

**Checkpoint:** verify the first coordinate pair and count against the CSV. Confirm that all 2,847 grid locations survive parsing. Check geographic alignment before adding height.

## 7. Build the landscape and contours

Follow the existing **Move / Unit Z**, **Bounds**, **Remap Numbers**, **Surface From Points**, **Mesh FromPoints** and **Contour** components.

Inspect which numeric branch is connected to each geometry output before changing it. The archive contains values 39 and 73 for grid dimensions, a remapping domain with endpoints 50 and 6000, and a contour slider saved at 30. These are original design settings, not prescribed physical heights.

1. Preview the flat points first.
2. Inspect the count-to-height mapping and choose a vertical exaggeration suitable for your document units.
3. Preview the raised points.
4. Check point order and the U/V dimensions before generating the surface or mesh. Their product must match the point count.
5. Generate contours with a documented interval. Inspect peaks and grid edges for twisting or unexpected connections.
6. Use the gradient and preview branch to explore a colour scale that matches your legend.

Do not delete zero-count cells to improve the shape. If extreme counts dominate, compare a separate logarithmic or capped-height experiment and label that transformation clearly.

**Checkpoint:** changing the height scale should change the vertical expression without moving the geographic footprint. A twisted surface usually needs a point-order or dimension check before further styling.

## 8. Compose the illustration

Use the included OSM and aerial assets only after checking their extent and alignment with the heightfield. Restoring a large OSM file is optional for learning the data-to-surface steps. A plain background is sufficient for an initial result.

The supplied `Illustrator/` folder contains `Heron.ai`, converted variants, `Heightfield [Converted].ai` and a square hero-image composition. Open copies and inspect their layers and linked images before editing.

For your own result, bake only the geometry you want to export. The definition includes Human baking components; review their destination layer and attributes first. Export or capture a deliberate view from Rhino, then assemble linework, imagery and labels in Illustrator. The precise vector export route and Illustrator link resolution still need application testing.

Add a title, study extent, data source, count definition, colour legend and explanation of vertical exaggeration. Keep map context visually subordinate to the data. Use the existing view capture above to compare the visual language, rather than assuming your regenerated model must match it exactly.

## 9. Interpret the result

A peak shows a high count under the selected dataset and aggregation method. Consider repeated uploads, prolific contributors, platform coverage and the time span of collection before interpreting it as collective interest. Counts alone do not establish sentiment.

Submit a map of the grid values, a landscape view, a detail of the contours and a short methods caption. Include the data subset, CRS, grid spacing, blank-value rule and height transformation.

As an optional extension, inspect `NoiseFieldSim.gh` and `NoiseFieldSim2.gh`. They contain Perlin, Simplex or Worley noise components for formal experiments. Label synthetic variation separately from measured photo counts.

## Checks for the next revision

- Run the QGIS import and Grasshopper definition in the recorded software environment.
- Reconcile the original photo databases with the smaller CSV and existing counts.
- Confirm grid CRS, EarthAnchorPoint, document units and connected height-mapping branches.
- Verify the plug-in installation set and Rhino-to-Illustrator export steps.
- Establish the original data collection method, attribution and reuse terms.

The source working files remain unchanged. [Transfer notes](TRANSFER.md) and the [manifest](TRANSFER-MANIFEST.csv) record their provenance.
