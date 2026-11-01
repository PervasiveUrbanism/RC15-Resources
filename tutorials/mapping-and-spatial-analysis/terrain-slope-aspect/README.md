# Terrain Analysis in QGIS: Slope and Accessibility

Understanding the slope of a terrain helps us identify where we might build, which areas are usable, and where roads, paths or other forms of access could be introduced. A slope analysis turns elevation data into a map of gradients. We can then interpret those gradients in relation to architectural and urban design questions.

In this tutorial, we will calculate slope from a digital elevation model (DEM) in QGIS, sample the result on a regular grid of points, and distinguish four terrain conditions: gentle ground, potential ramps, steep ground that may require stairs, and very steep areas. The final map will show these conditions over an OpenStreetMap background, so that the terrain remains legible in its geographical context.

**Software:** QGIS, including the GDAL processing tools  
**Starting point:** A georeferenced elevation raster (GeoTIFF)

[Mapping tutorials](../README.md) | [RC15 Resources](../../../README.md)

## 1. Getting elevation data

A **digital elevation model (DEM)** is a raster in which each pixel stores an elevation value. Elevation data is often distributed as a **GeoTIFF**: an image file that also contains information about its geographical position and coordinate reference system.

You can obtain elevation data from sources such as [USGS EarthExplorer](https://earthexplorer.usgs.gov/) or, for eligible UK institutions, [Digimap](https://digimap.edina.ac.uk/). Check the resolution before downloading. A raster with 30 m pixels describes terrain at a very different level of detail from one with 1 m pixels. Also check whether the dataset represents bare ground (often called a DTM) or a surface that includes buildings and vegetation (a DSM).

For this exercise, you can use the [supplied elevation raster](links/output_hh.tif) and [QGIS project](terrain-slope-aspect.qgz). The project includes intermediate results for comparison, but try to reproduce the steps yourself.

Add the elevation GeoTIFF to QGIS by dragging it into the map or using **Layer → Add Layer → Add Raster Layer**.

![Original elevation raster displayed in QGIS](images/01%20Qgis%20DSM%20Map.png)

*The elevation raster is our starting point. Its pixel values represent height, not slope.*

## 2. Check the coordinate reference system

Before calculating gradients, we need to check how the raster measures horizontal distances.

QGIS distinguishes between the **project coordinate reference system (CRS)** and the CRS of each individual layer. The project CRS controls how layers appear together in the map window. You can see it in the bottom-right corner of QGIS. In this example, the project uses **EPSG:3857**, commonly used for web maps.

The raster has its own CRS. Right-click the original elevation layer, select **Properties → Information**, and look for its coordinate reference system and pixel size.

![Elevation raster properties showing its CRS and pixel dimensions](images/01.2%20Qgis%20DSM%20Properties.png)

Our original GeoTIFF uses **EPSG:4326 (WGS 84)**. Its horizontal coordinates are longitude and latitude, measured in **degrees**, while its elevation values are assumed to be in **metres**. That difference matters: slope is calculated by comparing a vertical change with a horizontal distance. Using degrees for one and metres for the other would produce incorrect results if we left the scale factor at 1.

QGIS can display a raster in EPSG:4326 over a basemap in EPSG:3857 without difficulty. However, displaying a layer in another CRS does **not** change the coordinates stored in the raster. For slope analysis, we will create a new GeoTIFF in a projected CRS that uses metres.

## 3. Reproject the elevation raster

Open **Raster → Projections → Warp (Reproject)**.

Use the original elevation raster as the input, and set the following options:

| Parameter | Setting |
| --- | --- |
| Input layer | `output_hh` |
| Source CRS | EPSG:4326 — WGS 84 |
| Target CRS | EPSG:32636 — WGS 84 / UTM zone 36N |
| Resampling method | Bilinear |
| Output | `DEM_projected.tif` |

![Warp (Reproject) settings](images/01.3%20Wrap%201.png)

![Selecting the projected coordinate reference system](images/01.4%20Wrap%202.png)

**EPSG:32636** is suitable for this study area in Cyprus. It uses metres, but it is not the correct CRS for every location. For another site, choose an appropriate local projected coordinate system. Keep the output resolution consistent with the detail of the source data; reprojection cannot create new terrain information.

Click **Run**, then open **Properties → Information** for the new `DEM_projected` layer. Its CRS should be EPSG:32636, and its pixel dimensions should now be expressed in metres.

We therefore have three different CRS values in this project: the **project** uses EPSG:3857 for display, the **original raster** uses EPSG:4326 in degrees, and the **reprojected raster** uses EPSG:32636 in metres. We do not need to change the project CRS. The important step is to use the *reprojected raster* for the analysis.

## 4. Calculate the slope

Open the **Processing Toolbox** and search for **Slope**. Select **GDAL → Raster analysis → Slope**, rather than the similarly named tool from another provider.

Set the parameters as follows:

| Parameter | Setting |
| --- | --- |
| Input layer | `DEM_projected` |
| Band number | 1 |
| Ratio of vertical units to horizontal | 1, assuming both are metres |
| Slope expressed as percent instead of degrees | **Tick** |
| Compute edges | Leave unticked |
| Zevenbergen–Thorne formula | Leave unticked (default Horn method) |
| Output | `slope_percent.tif` |

![GDAL Slope tool configured to calculate percentages](images/02%20Slope%20Calculator.png)

Click **Run**. The new raster contains a slope percentage at each valid pixel. Unlike the original DEM, which stores elevation, this raster stores the steepness of the terrain.

A percentage gradient describes the vertical rise relative to the horizontal distance:

**Slope (%) = 100 × vertical rise ÷ horizontal distance**

For example, a rise of 5 cm over a horizontal distance of 1 m is a **5% slope**. A 100% slope corresponds to **45°**. Percentages can exceed 100%: a 200% slope corresponds to approximately 63°. Do not confuse percentage gradient with degrees or assume that 100% is the maximum.

Use QGIS's **Identify Features** tool to inspect a few pixels. Gentle ground should have values near zero; steeper areas should have higher values. If values seem implausible across the entire raster, check the input CRS and elevation units before continuing. Individual very high values may be real or may require checking against the original elevation data.

You can temporarily display the result using **Singleband pseudocolour** in the layer's Symbology settings. This helps reveal the topography, but the coloured raster also covers much of the underlying map. Instead of using the raster as our final representation, we will sample it at regular points.

<!-- @ChatGPT: Please discuss the results using the images: 03 Slope Results.png and 3.1 and 3.2. It's jus the range. and there is also the fact that the new slope map covers the map below. one can not see ot and that is not good. therefore we do a different approach: the grid where wher sample a slope value very 25 meters -->


## 5. Create a 25 m point grid

Open the **Processing Toolbox** and search for **Create grid**.

| Parameter | Setting |
| --- | --- |
| Grid type | **Point** |
| Grid extent | Calculate from layer → `DEM_projected` |
| Horizontal spacing | 25 |
| Vertical spacing | 25 |
| Grid CRS | EPSG:32636 |
| Output | `Point Grid.gpkg` |

![Creating a regular point grid in QGIS](images/04%20Point%20Grid.png)

Click **Run**. QGIS creates a regular pattern of points spaced **25 metres** apart in both directions. Because the grid uses a projected CRS in metres, the spacing has a meaningful real-world dimension.

At this stage, the points only describe locations. They do not yet contain slope values. Also remember that a 25 m point spacing does not mean the underlying elevation data has a 25 m resolution. Sampling more frequently than the original DEM's pixel size does not reveal additional terrain detail.

## 6. Sample the slope raster

In the **Processing Toolbox**, search for **Sample raster values**.

Select the new point grid as the input point layer and the **percentage slope raster** as the raster layer. Use `Slope_` as the output column prefix and save the result as `Slope Grid.gpkg`.

![Sampling raster values at the grid points](images/06%20Sample%20Raster%20Values.png)

Click **Run**, then right-click the resulting layer and select **Open Attribute Table**.

![Attribute table showing sampled slope values](images/07%20Grod%20with%20Slopes.png)

You should find a new field called `Slope_1` containing the slope percentage at each point. The tool reads the raster value at the point location; it does **not** calculate an average across a 25 × 25 m area. Points outside the valid raster coverage may have an empty (`NULL`) value.

We now have a point layer that combines geographical locations with numerical information about the terrain.

## 7. Translate slope into terrain categories

<!-- I have a very strong opiinion as to which audince the map asdreeses. so in thi case, the solpes as they are do not mean anytun to who is not an eningeer and is familar with the slopes. This it makes rnse to introiiduce catergoiies the quickly identlyi what is what. Imporant: tis makes a big difference: we started with an map that only engineers can undertasnt and we do a map that is actuuly useful for everybody. this is the diffice that is very, very impotnat,-->

Raw percentages are useful for measurement, but a design map becomes more informative when we relate them to questions about access and movement.

We will distinguish four conditions:

| Slope | Category | Design interpretation |
| --- | --- | --- |
| 0–4% | **Flat / gentle** | Relatively gentle ground for investigating paths and usable outdoor space |
| 4–8.33% | **Ramps** | Ground where ramp gradients, route length and landings deserve attention |
| 8.33–84% | **Stairs** | Steeper ground where steps or a different route may be considered |
| 84% and above | **Very steep** | Ground likely to require a substantial change in route or design strategy |

These are **exploratory categories, not accessibility or construction standards**. In particular, a terrain slope does not determine the gradient of a path that crosses it: a route following the contours may be considerably gentler than a direct uphill route. The broad “Stairs” category also contains many different terrain conditions; its label is a prompt for design investigation, not a claim that every such slope can accommodate stairs.

Right-click **Slope Grid → Properties → Symbology** and choose **Categorised**. Click the expression button beside **Value**, and paste:

```sql
CASE
  WHEN "Slope_1" IS NULL THEN NULL
  WHEN "Slope_1" < 4 THEN '1 - Flat / gentle'
  WHEN "Slope_1" < 8.33 THEN '2 - Ramps'
  WHEN "Slope_1" < 84 THEN '3 - Stairs'
  ELSE '4 - Very steep'
END
```

![Expression defining the four terrain categories](images/08.1%20Expression.png)

If you used a different column prefix, replace `Slope_1` with the name shown in your attribute table. Click **Classify** and assign one colour to each category.

For a bright, readable map, try:

| Category | Colour |
| --- | --- |
| Flat / gentle | Green — `#40C463` |
| Ramps | Yellow — `#FFD23F` |
| Stairs | Orange — `#FF8438` |
| Very steep | Red — `#E63946` |

Use circular markers of approximately **2–2.5 mm**, without outlines. Keep their size consistent so that colour, rather than symbol size, communicates the classification. Hide the original point grid and the slope raster, and remove or disable any unwanted category for `NULL` values.

![Completed slope analysis with classified points over OpenStreetMap](images/09.%20Finished.png)

*The final map shows four terrain conditions while allowing streets, buildings and landscape features to remain visible underneath.*

## 8. Interpret the result

Compare the point patterns with the roads, buildings and open spaces shown on the basemap. Where does gentle terrain coincide with existing routes? Where do steep areas interrupt potential connections? Could a longer route following the contours avoid the need for stairs?

Try sketching two possible connections across the same site: one taking a direct route uphill, and another following a gentler alignment. Use the map to develop and question your ideas, rather than treating the four categories as definitive answers.

The analysis is only as reliable as the source elevation model. A coarse DEM can miss small changes in level, while a surface model containing buildings or trees may introduce slopes that do not represent the ground. For detailed accessibility or construction decisions, you would need more precise terrain data and the relevant design standards.

<!-- Please show the last image, 10 - discuss that this is the beginnings of styling the map. it's not done, but the direction is clear. we have been using the height map to extract contour lines, Ihave switced off the flat and the not accessible parts, depending on the scale of the map. the desinty of the points/cross has to be adjusted.-->

## Troubleshooting

| Problem | What to check |
| --- | --- |
| Slope values are extremely high across most of the raster | Check that GDAL Slope uses the **reprojected** DEM and that horizontal and vertical units match. |
| The slope output appears to stop at 90 | You may have calculated slope in **degrees**, rather than ticking the percentage option. |
| Grid spacing looks wrong | Confirm that the **grid CRS** is EPSG:32636 and both spacing values are 25. |
| The sampled field is empty | Check that you sampled the slope raster and that the points overlap valid raster pixels. |
| The categories do not appear | Check the sampled field name, click **Classify**, and ensure all four symbols are enabled. |
| The map is difficult to read | Hide the slope raster and unclassified grid, then adjust point size or use a quieter basemap. |

## Further references

- [QGIS documentation](https://docs.qgis.org/) — Processing tools, raster analysis and layer symbology
- [GDAL documentation: gdaldem slope](https://gdal.org/en/stable/programs/gdaldem.html)
- [USGS EarthExplorer](https://earthexplorer.usgs.gov/)
- [Digimap](https://digimap.edina.ac.uk/)
