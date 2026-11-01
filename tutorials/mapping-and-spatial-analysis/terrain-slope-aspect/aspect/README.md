# Terrain Analysis in QGIS: Aspect and Sun Orientation

<img src="../images/Icon%20Aspect.png" width="800" alt="Aspect analysis — terrain orientation illustration">

Slope tells us how steep the ground is. **Aspect** tells us which compass direction a slope faces. Together, these measurements help us investigate terrain, outdoor spaces and the relationship between a site and the sun.

In this companion tutorial, we calculate aspect from the same digital elevation model (DEM) used in [Slope and Accessibility](../README.md). We then sample the raster on a 25 m point grid, translate the angles into compass directions, and use [Andrew Marsh's 2D Sun-Path tool](https://andrewmarsh.com/software/sunpath2d-web/) to explore how orientation relates to the sun's changing position.

**Software:** QGIS (including GDAL processing tools); web browser  
**Starting point:** [Aspect QGIS project](../Aspect.qgz), [projected DEM](../links/DEM_projected.tif), and [25 m point grid](../links/Point%20Grid.gpkg)

[Mapping tutorials](../../README.md) | [RC15 Resources](../../../../README.md)

## 1. Start with the projected elevation model

Open the supplied QGIS project or continue from the slope exercise. The DEM has already been reprojected into **EPSG:32636**, which measures horizontal distances in metres and is appropriate for this Cyprus study area. If you are using another site, choose a suitable projected coordinate reference system. The [slope tutorial](../README.md) explains why reprojection matters.

![Starting elevation model in QGIS](../images/Aspect%2001%20Start.png)

An elevation raster stores height at each pixel. To calculate aspect, QGIS compares neighbouring heights to determine the direction of the steepest descent. Unlike slope, which describes a gradient, aspect describes an **orientation**.

## 2. Calculate aspect

Open the **Processing Toolbox**, search for **Aspect**, and choose **GDAL → Raster analysis → Aspect**. QGIS may offer other tools with the same name, so check the provider.

| Parameter | Setting |
| --- | --- |
| Input layer | `DEM_projected` |
| Band number | 1 |
| Zevenbergen–Thorne formula | Leave unticked (default Horn method) |
| Return 0 for flat instead of NoData | Leave unticked |
| Compute edges | Leave unticked |
| Output | `Aspect.tif` |

![GDAL Aspect processing settings](../images/Aspect%2002%20Settings.png)

Click **Run**. GDAL normally measures aspect **clockwise from north**: 0° or 360° is north, 90° east, 180° south and 270° west. On flat ground, no downhill direction exists, so aspect is undefined. Keeping the flat-area option unticked preserves this distinction.

## 3. Read the aspect raster

![Resulting aspect raster](../images/Aspect%2003%20Results.png)

Use **Identify Features** to inspect some raster pixels. A value near 90° indicates east-facing terrain; a value near 270° indicates west-facing terrain. Be careful with the numbers: **350° and 10° are both almost north-facing**. Aspect is circular, so a conventional low-to-high colour gradient can be misleading.

A continuous raster reveals the topography, but it can also obscure roads, buildings and other features underneath. As in the slope exercise, we will use sampled points to retain that context.

## 4. Sample aspect onto the 25 m point grid

Open **Sample raster values** in the Processing Toolbox. Choose the existing `Point Grid.gpkg` as the input point layer and `Aspect.tif` as the raster layer. Set the output column prefix to `Aspect_` and save the output as `Aspect Grid.gpkg`.

![Sampling aspect raster values onto the point grid](../images/Aspect%2004%20Sample%20Raster.png)

Open the output layer's attribute table. The new field, normally named `Aspect_1`, contains the aspect in degrees at each sampled location. These are **point samples**, not averages over 25 × 25 m squares. Where the raster has no valid aspect, the sampled value may be `NULL`.

## 5. Translate angles into directions

Right-click the sampled point layer, open **Properties → Symbology**, and choose **Categorised**. Beside **Value**, open the expression editor and enter:

```sql
CASE
  WHEN "Aspect_1" IS NULL OR "Aspect_1" < 0 THEN NULL
  WHEN "Aspect_1" >= 337.5 OR "Aspect_1" < 22.5 THEN 'N'
  WHEN "Aspect_1" < 67.5 THEN 'NE'
  WHEN "Aspect_1" < 112.5 THEN 'E'
  WHEN "Aspect_1" < 157.5 THEN 'SE'
  WHEN "Aspect_1" < 202.5 THEN 'S'
  WHEN "Aspect_1" < 247.5 THEN 'SW'
  WHEN "Aspect_1" < 292.5 THEN 'W'
  ELSE 'NW'
END
```

Click **Classify**. This groups the circular range of aspect angles into eight compass sectors. If you used another field prefix, replace `Aspect_1` with the actual field name.

For the symbols, use a **cool-to-warm palette**: blue for morning-facing directions, a warm white for south-facing terrain, and orange for afternoon-facing directions.

| Direction | Suggested colour | Hex |
| --- | --- | --- |
| N | Muted blue-grey | `#8096AD` |
| NE | Cool blue | `#8FC5E8` |
| E | Light blue | `#B7DFF2` |
| SE | Very pale blue | `#DCEEF5` |
| S | Warm white | `#FAFAF5` |
| SW | Pale peach | `#F7D3AC` |
| W | Orange | `#E99555` |
| NW | Muted grey-brown | `#B9A7A0` |

The white south-facing symbols may disappear on a light basemap. Add a thin grey outline to maintain their visibility. The colours communicate an **interpretation of orientation**, not a measurement of sunlight. North and north-west are not times of day.

![Point-based aspect visualisation](../images/Aspect%2005%20Points%2001.png)

![Adjusting aspect point symbology](../images/Aspect%2005%20Points%20Style.png)

## 6. Relate aspect to the movement of the sun

A slope's orientation influences its potential exposure to sunlight, but **aspect alone does not tell us how much sunlight reaches it**. We also need to consider the date, time, latitude, slope angle, and shadows cast by terrain or buildings.

Open [Andrew Marsh's interactive 2D Sun-Path tool](https://andrewmarsh.com/software/sunpath2d-web/). The diagram allows us to examine the sun's direction and height above the horizon at a chosen location and time.

![Sun-path diagram for comparing solar directions](../images/Aspect%2004%20Sun%20Dia.png)

Set the tool to the location of your study site. Compare the sun's path around **21 June** and **21 December**, then inspect the approximate positions at **09:00, 12:00 and 15:00**. Pay attention to the difference between clock time and solar noon: the sun is not necessarily due south at exactly 12:00 on the clock.

For a site in Cyprus, east-facing slopes generally have greater potential for morning sun, west-facing slopes for afternoon sun, and south-facing slopes for sunlight when the sun is towards the southern sky. This relationship changes across the seasons, and surrounding topography may block direct sunlight altogether.

Try identifying three places on your aspect map: one facing east, one south and one west. Which might be suitable for a breakfast terrace, a winter outdoor gathering space or an afternoon-shaded route? Use the sun-path diagram to explain your reasoning rather than relying on the colours alone.

## 7. Refine and interpret the finished map

![Finished aspect map](../images/Aspect%2005%20Finished.png)

Compare the aspect map with the [slope map](../README.md). Two locations can face south but have very different gradients, and a flat location may have no meaningful aspect at all. A design decision therefore needs both measurements, as well as the site's wider geographical context.

Experiment with point size, outline, transparency and visibility of individual categories. As with the slope tutorial, the objective is not to cover the map in data, but to make the information legible alongside roads, contours, buildings and other landscape features.

The blue–white–orange scheme provides an intuitive visual narrative from morning to afternoon. It should nevertheless be labelled as **terrain orientation**, not as measured solar exposure. Calculating actual sunshine duration, shadowing or irradiation would require a separate solar analysis.

## Troubleshooting

If the aspect values look wrong, check that you used the **projected DEM** rather than the original raster in longitude and latitude. If the categories do not appear, confirm the sampled field name in the attribute table. If flat areas have an unexpected north classification, check whether the GDAL option to assign zero aspect to flat terrain was enabled. If pale symbols are difficult to see, add an outline or adjust the basemap rather than changing the underlying measurements.

## Further exploration

- [Andrew Marsh — 2D Sun-Path](https://andrewmarsh.com/software/sunpath2d-web/)
- [GDAL aspect documentation](https://gdal.org/en/stable/programs/gdaldem.html)
- [Companion tutorial: Slope and Accessibility](../README.md)
