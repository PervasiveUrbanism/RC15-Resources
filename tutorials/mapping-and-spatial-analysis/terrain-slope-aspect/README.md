# Terrain Analysis in QGIS: Slope

Part of **RC15 Resources**, the permanent teaching library for Pervasive Urbanism.

**Software:** QGIS, using GDAL Slope  
**Level:** Introductory  
**Status:** Teaching draft; check the source DEM's elevation units and verify the results in QGIS.

[Mapping tutorials](../README.md) | [Library home](../../../README.md) | [Related: Viewshed Analysis](../viewshed-analysis/README.md)

## Why calculate slope?

An elevation map shows how high the ground is. A **slope map** shows how steep it is. This is useful when investigating possible paths, ramps, stairs and places where changes in level may affect a design.

In this exercise, we will calculate the gradient of a terrain model with **GDAL Slope** and then visualise that result directly in QGIS. We will not use the Raster Calculator or create a second, classified raster.

A slope value is a measurement, not a design decision. We will use the map to ask where different ways of moving across the terrain might be possible.

## 1. Open the elevation model

Start a new QGIS project and add your digital elevation model (DEM). You can use the elevation raster supplied with this tutorial or your own terrain data. Save your project before processing.

Right-click the DEM and open **Properties → Information**. Check the **Coordinate Reference System (CRS)**, pixel size, NoData value and, if known, the elevation units.

A DEM often stores elevations in **metres**, but its horizontal coordinates may be in **degrees**. This distinction is important: slope compares vertical height with horizontal distance, so the two must use compatible units.

## 2. Reproject the DEM if necessary

In the example discussed in class, the elevation raster `output_hh` uses **EPSG:4326**. Its horizontal coordinates are longitude and latitude in degrees. We should reproject it before running GDAL Slope with a unit ratio of 1.

Open **Raster → Projections → Warp (Reproject)** (or find **GDAL → Raster projections → Warp (reproject)** in the Processing Toolbox).

- **Input layer:** your elevation raster, such as `output_hh`.
- **Target CRS:** an appropriate *local projected CRS* with metre units. For the example location near 33° E, 34–35° N, **EPSG:32636 (WGS 84 / UTM zone 36N)** is a suitable candidate; confirm the location before choosing it.
- **Resampling method:** **Bilinear**, appropriate for a continuous elevation surface.
- **Output:** save as `DEM_projected.tif`.

Choose an appropriate output pixel size in metres, consistent with the source DEM's resolution. Do not invent finer terrain detail by choosing extremely small pixels.

Click **Run**. The new raster should appear in the same geographic location. Check **Properties → Information** again: the new raster should have a projected CRS and horizontal pixel dimensions expressed in metres.

**Important:** Changing the QGIS *project* CRS does not reproject the raster data. Use **Warp (Reproject)** to create a new raster.

## 3. Calculate slope with GDAL

Open the **Processing Toolbox** and search for **Slope**. Choose **GDAL → Raster analysis → Slope** (`gdal:slope`).

Use these settings:

| Setting | Value |
| --- | --- |
| Input layer | `DEM_projected` |
| Band number | Band 1 |
| Ratio of vertical units to horizontal | **1**, provided elevation and horizontal distances are both in metres |
| Slope expressed as percent instead of degrees | **Ticked** |
| Compute edges | Leave unticked for this exercise |
| Zevenbergen–Thorne formula | Leave unticked; use the default Horn method |
| Output | `slope_percent.tif` |

Click **Run** and add the resulting raster to the project.

The output expresses the steepest local terrain gradient as a **percentage**:

**Gradient (%) = 100 × vertical rise ÷ horizontal run**

For example, a 5% slope rises 5 cm over 1 m horizontally. A 100% gradient corresponds to 45°, not a vertical wall.

**Checkpoint:** Use the **Identify Features** tool to inspect some cells in `slope_percent`. Nearly flat areas should have values close to zero, while steeper hillsides should have larger values. If the whole raster shows unexpectedly enormous values, check the DEM's CRS and units before continuing.

## 4. Visualise the slope raster

Right-click `slope_percent` and choose **Properties → Symbology** (or open the Layer Styling panel).

Select **Singleband pseudocolour**, not **Paletted / Unique values**. The GDAL result contains continuous percentage values, not pre-assigned category numbers.

Choose **Discrete** interpolation and create four colour intervals using the following boundaries. Adjust the upper limit to cover the actual maximum in your raster:

| Slope (%) | Suggested map label |
| --- | --- |
| **0–4** | Flat or gentle slope — paths without landings |
| **4–8.33** | Ramps — steeper paths that may require landings |
| **8.33–84** | Stairs — terrain too steep for a direct ramp |
| **Above 84** | Very steep terrain — neither conventional ramps nor stairs are straightforward |

In the colour-ramp editor, use a restrained progression from light green through yellow and orange to dark red. Set the class boundaries manually rather than using equal intervals or quantiles. **Apply** the symbology and check the legend.

This is a **visual classification of the original GDAL slope raster**. It does not change the underlying pixel values and requires no Raster Calculator expression.

The thresholds are deliberately illustrative, not construction standards. In particular, 84% is approximately 40°, but 40° is not an absolute upper limit for stairs. A steep hillside may also be crossed by a more gradual route following the contours.

## 5. Read the map as a designer

The point of this exercise is not simply to colour a raster. We have chosen four categories because they help us think about **how people might move across the terrain**.

Sketch two possible routes between the same points. One could climb directly uphill; the other might follow a gentler path across the contours. Compare the terrain they cross.

Remember that the slope raster measures the **steepest gradient of the terrain at each cell**, not the gradient of a proposed path. The map is a starting point for design investigation, not an accessibility assessment.

## Troubleshooting

| Problem | What to check |
| --- | --- |
| Almost everything appears in the steepest category | You may have classified elevation instead of slope, or calculated slope on a DEM in degrees rather than metres. |
| The GDAL output shows extreme percentages | Check the input DEM's CRS and whether horizontal and vertical units match. |
| Only two colours appear | Inspect actual slope values and confirm you used **Singleband pseudocolour** with manually set intervals. |
| The raster appears in the wrong place | Check the source and target CRS in Warp (Reproject); assigning a CRS is not the same as transforming coordinates. |
| Empty pixels appear around the edges | Check the input NoData and the GDAL Slope edge-processing setting. |

## Reference

- [QGIS documentation — GDAL Raster Analysis (Slope)](https://docs.qgis.org/3.44/en/docs/user_manual/processing_algs/gdal/rasteranalysis.html)

**To verify on desktop:** confirm the actual source DEM and elevation units, test the reprojection and GDAL Slope settings, and add screenshots of Warp (Reproject), GDAL Slope and the final discrete colour legend.
