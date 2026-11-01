# Terrain Analysis in QGIS: Slope

Part of **RC15 Resources**, the permanent teaching library for Pervasive Urbanism.

**Software:** QGIS, using GDAL Slope  
**Level:** Introductory  
**Status:** Teaching draft; check the source DEM's elevation units and verify the results in QGIS.

[Mapping tutorials](../README.md) | [Library home](../../../README.md) | [Related: Viewshed Analysis](../viewshed-analysis/README.md)

## Why calculate slope?

An elevation map shows how high the ground is. A **slope map** shows how steep it is. This is useful when investigating possible paths, ramps, stairs and places where changes in level may affect a design.

In this exercise, we will calculate the gradient of a terrain model with **GDAL Slope** and then visualise that result directly in QGIS. We will then sample the slope on a 25 m point grid to keep the basemap visible. No Raster Calculator or second, classified raster is required. Although the folder retains its original name, this tutorial currently covers slope only.

A slope value is a measurement, not a design decision. We will use the map to ask where different ways of moving across the terrain might be possible.

## Files supplied

Keep the [QGIS project](terrain-slope-aspect.qgz) beside its `links/` folder. The folder contains the [original elevation raster](links/output_hh.tif), [projected raster](links/DEM_projected.tif), [percentage slope raster](links/Slope.tif), [point grid](links/Point%20Grid.gpkg) and [sampled slope grid](links/Slope%20Grid.gpkg). These are reference stages; save your own results separately.

The saved project refers to `links/slope.tif`, while the uploaded file is `links/Slope.tif`. On a case-sensitive system, repair that layer source by selecting the supplied `Slope.tif`. Online basemaps require an internet connection; configure your own connection if one is unavailable.

## 1. Open the elevation model

Start a new QGIS project and add your digital elevation model (DEM). You can use the elevation raster supplied with this tutorial or your own terrain data. Save your project before processing.

![Elevation raster displayed over a basemap in QGIS](images/01%20Qgis%20DSM%20Map.png)

*The original elevation raster provides the starting surface.*

### Check the coordinate reference system (CRS)

Before calculating slope, we need to understand how QGIS positions and measures our terrain. There are **two coordinate reference systems** to consider.

**The QGIS project CRS** determines how different layers are displayed together on the map. You can find it in the bottom-right corner of the QGIS window. In our example, the project uses **EPSG:3857**, a coordinate system commonly used for online maps such as OpenStreetMap.

**The elevation raster CRS** belongs to the GeoTIFF itself. It describes how the pixels are geographically positioned. To check it, right-click the elevation layer and select **Properties → Information**.

In our example, the elevation raster uses **EPSG:4326 (WGS 84)**.

![Raster information showing EPSG:4326 and pixel size in degrees](images/01.2%20Qgis%20DSM%20Properties.png)

*Check the raster CRS, rather than relying on the project CRS.*

EPSG:4326 uses latitude and longitude, measured in degrees. Although QGIS can display this raster correctly alongside an OpenStreetMap background, its horizontal coordinates are not measured in metres.

This becomes a problem when calculating slope. The GDAL Slope tool compares changes in elevation with horizontal distances. If our elevation values are in metres but the horizontal coordinates are in degrees, a scale factor of 1 will not give a reliable gradient. Reprojecting into a suitable local metric CRS avoids this unit mismatch.

## 2. Reproject the elevation raster

We therefore need to create a **new GeoTIFF** with a coordinate system that uses metres.

Open **Raster → Projections → Warp (Reproject)** and select the original elevation raster as the input.

| Parameter | Setting |
| --- | --- |
| Input layer | `output_hh` (EPSG:4326) |
| Source CRS | EPSG:4326 — WGS 84 |
| Target CRS | EPSG:32636 — WGS 84 / UTM zone 36N |
| Resampling method | Bilinear |
| Output | `DEM_projected.tif` |

![Warp dialog with bilinear resampling and EPSG:32636 target](images/01.3%20Wrap%201.png)

*Reproject the raster; changing the project CRS alone does not change the raster coordinates.*

![CRS selector showing WGS 84 UTM zone 36N](images/01.4%20Wrap%202.png)

*Select the local projected CRS for this example.*

The target CRS is selected according to the geographical location of the study area. **EPSG:32636** is appropriate for our example near 33° E in the Limassol area of Cyprus, but other locations require different coordinate systems.

Choose an output pixel size appropriate to the source DEM's resolution. Reprojection does not create additional terrain detail.

Run the tool. QGIS creates a new raster with its horizontal coordinates expressed in metres. To check that the reprojection worked, right-click `DEM_projected` and open **Properties → Information**. The CRS should now be EPSG:32636, with pixel dimensions expressed in metres.

We now have three CRS settings to distinguish:

- **QGIS project:** EPSG:3857 — controls how the map is displayed.
- **Original GeoTIFF:** EPSG:4326 — geographical coordinates in degrees.
- **Reprojected GeoTIFF:** EPSG:32636 — projected coordinates in metres, suitable for our slope calculation.

There is **no need to change the QGIS project CRS**. QGIS can display layers with different coordinate systems together. What matters is that we use the **reprojected GeoTIFF** as the input for GDAL Slope.

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

Click **Run** and add the resulting raster to the project. The supplied result is named `Slope.tif`; the screenshots show it as `slope`.

![GDAL Slope dialog using the projected DEM and percentage output](images/02%20Slope%20Calculator.png)

*Use the projected DEM, a scale ratio of 1 for metre units, and percentage output.*

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
| **0–4** | Flat or gentle — investigate possible paths |
| **4–8.33** | Ramp-sensitive — investigate gradients and landings |
| **8.33–84** | Steep — investigate steps or alternative routes |
| **Above 84** | Very steep — investigate structures or a different alignment |

In the colour-ramp editor, use a clear progression from green through yellow and orange to red. Set the class boundaries manually rather than using equal intervals or quantiles. **Apply** the symbology and check the legend.

This is a **visual classification of the original GDAL slope raster**. It does not change the underlying pixel values and requires no Raster Calculator expression.

The thresholds are deliberately illustrative, not construction standards. In particular, 84% is approximately 40°, but 40° is not an absolute upper limit for stairs. A steep hillside may also be crossed by a more gradual route following the contours.

## 5. Sample slope on a 25 m point grid

A point display lets the geographical context remain visible between samples. Open **Create grid** in the Processing Toolbox. Choose **Point**, set the grid CRS to **EPSG:32636**, and use the extent of `DEM_projected`, transformed into that CRS. Set both horizontal and vertical spacing to **25 metres**, with zero overlay. Save as `Point Grid.gpkg`.

![Create Grid dialog configured for points at 25 metre spacing](images/04%20Point%20Grid.png)

*Use a metre-based grid CRS; 25 in a geographic CRS would mean degrees.*

Run **Sample raster values** with `Point Grid` as the point layer and your percentage slope raster as the raster layer. Set the output column prefix to `Slope_` and save as `Slope Grid.gpkg`. Open its attribute table and check the resulting `Slope_1` field. This samples the raster at each point; it does **not** average slope across a 25 m square or increase the DEM resolution.

![Sample Raster Values dialog with point grid and slope raster inputs](images/06%20Sample%20Raster%20Values.png)

*Sample slope, not the original elevation raster.*

![Sampled grid attribute table showing the Slope_1 field](images/07%20Grod%20with%20Slopes.png)

*Check that the sampled field contains percentage gradient values.*

Open **Slope Grid → Properties → Symbology**, choose **Categorised**, and use the expression button beside **Value**:

```sql
CASE
  WHEN "Slope_1" IS NULL OR "Slope_1" < 0 THEN NULL
  WHEN "Slope_1" < 4 THEN '1 - Flat / gentle'
  WHEN "Slope_1" < 8.33 THEN '2 - Ramps'
  WHEN "Slope_1" < 84 THEN '3 - Stairs'
  ELSE '4 - Very steep'
END
```

Use the actual field name if your prefix differs. Click **Classify**. These expression labels match the screenshots; treat “Ramps” and “Stairs” as prompts for investigation, with the qualifications in section 4. The exact intervals are **0 ≤ slope < 4**, **4 ≤ slope < 8.33**, **8.33 ≤ slope < 84**, and **slope ≥ 84** percent.

![Expression builder showing four slope categories and a NULL check](images/08.1%20Expression.png)

*Handle missing values before testing slope thresholds.*

Use equal-sized circular markers, starting around **2–2.5 mm**, at full opacity with no outline. Choose saturated green, yellow, orange and red, and check legibility at your intended map scale. Disable the NULL / “all other values” category so missing samples do not appear as terrain. Enable all four valid categories: the supplied project has the first category disabled. Hide the continuous slope raster and the original unclassified point grid to reveal the basemap beneath the sampled points.

![Four slope point categories over an OpenStreetMap basemap](images/09.%20Finished.png)

*Example point-grid result. Adjust marker size and basemap contrast for the final output; retain basemap attribution.*

## 6. Read the map as a designer

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

- [QGIS documentation — Sample raster values](https://docs.qgis.org/3.44/en/docs/user_manual/processing_algs/qgis/rasteranalysis.html#sample-raster-values)
- [QGIS documentation — GDAL Raster Analysis (Slope)](https://docs.qgis.org/3.44/en/docs/user_manual/processing_algs/gdal/rasteranalysis.html)

**Verification still required:** confirm the source elevation model’s provenance, vertical units and whether it represents bare ground (DTM) or includes buildings and vegetation (DSM). The screenshots document the workflow, but do not establish those properties. A DSM may show steep changes at buildings or trees rather than ground slopes. Check the grid field, missing values and all four category visibility settings before exporting.
