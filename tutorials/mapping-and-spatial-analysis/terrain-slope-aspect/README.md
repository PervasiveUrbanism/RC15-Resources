# Terrain Analysis in QGIS: Slope, Aspect and Solar Orientation

Part of **RC15 Resources**, the permanent teaching library for Pervasive Urbanism.

**Software:** QGIS (GDAL Processing tools), with Andrew Marsh’s Sun-Path on Map as a solar reference  
**Level:** Introductory–intermediate  
**Format:** Two linked practical exercises using the same digital elevation model (DEM)  
**Status:** Teaching draft based on the supplied raster; QGIS processing and graphics require desktop verification.

[Mapping tutorials](../README.md) | [Library home](../../../README.md) | [Related: Viewshed Analysis](../viewshed-analysis/README.md)

## Why analyse a landscape?

An elevation map tells us how high the land is, but height alone does not explain how we might use a site. Two additional measurements help translate topography into design questions. **Slope** describes how steep the terrain is; **aspect** describes the compass direction a slope faces.

In the first exercise, we classify terrain by gradient so that a map communicates potential uses and access constraints rather than merely displaying numerical values. In the second, we reinterpret aspect in terms of possible **morning, midday and afternoon solar exposure**, and compare the result with a sun-path diagram. Both maps are *analytical starting points*, not ready-made design decisions.

The exercise reuses the elevation data from [Visibility and Viewshed Analysis](../viewshed-analysis/README.md), but is designed to work independently.

## Learning outcomes

You should be able to calculate slope and aspect from a DEM, distinguish degrees from percentage gradient, classify raster values into meaningful categories, handle NoData and nearly flat terrain, and compare terrain orientation with the sun’s changing position. You should also be able to explain why slope and aspect cannot, by themselves, establish accessibility or actual hours of sunlight.

## Files and preparation

The copied files in this folder are a self-contained **starting dataset**, not an already completed QGIS project:

| File | Purpose |
| --- | --- |
| [SmallHeightMap.tif](SmallHeightMap.tif) | Sample elevation raster, copied unchanged from Viewshed Analysis |
| [SmallHeightMap.tif.aux.xml](SmallHeightMap.tif.aux.xml) | Existing GDAL metadata for the raster |
| [Bbox.shp](Bbox.shp) | Study boundary; keep accompanying shapefile components together |
| [Viewpoints.shp](Viewpoints.shp) | Existing observation point for cross-comparison with the Viewshed tutorial |
| [Viewanalysis.qgz](Viewanalysis.qgz) | **Optional reference QGIS project** copied from the original viewshed exercise; it may include paths to other files and should not be treated as a finished project for this tutorial |

The accompanying `.dbf`, `.shx`, `.prj`, `.cpg` and `.qix` files belong to the shapefiles. Keep them together.

Open QGIS and create a **new project**. Add `SmallHeightMap.tif`, `Bbox.shp` and, if useful, `Viewpoints.shp`. Save your new project as `TerrainAnalysis.qgz` in your own working copy; do not overwrite the supplied original. Organise derived results in a new `outputs/` directory on your computer.

Before proceeding, open the DEM’s *Layer Properties → Information* and check its **CRS, horizontal cell size, elevation units and NoData value**. The existing raster metadata suggests elevations around 26–80, but this is not enough to prove the elevation units or source. Slope calculations require consistent horizontal and vertical units.

The supplied shapefiles refer to Web Mercator, which is not locally distance-preserving. For a reliable design-scale study, establish the DEM’s actual CRS and consider reprojecting the raster into an appropriate local projected CRS with metre units. Do **not** merely assign a new CRS to existing coordinates. Any reprojection should use a clearly chosen cell size and resampling method.

**Checkpoint:** The DEM and boundary align correctly, and you know what horizontal and vertical units you are using.

## Exercise 1 — Slope as a design question

### 1. Calculate percentage gradient

Slope is the steepest local inclination of the terrain, computed from neighbouring elevation cells. It is often reported as an angle (degrees), but percentage gradient is more useful when discussing paths and ramps:

**Gradient (%) = 100 × vertical rise ÷ horizontal run.**

A 5% gradient rises 5 cm over 1 m horizontally. A 100% gradient is an angle of 45°, **not** a vertical surface.

Open the *Processing Toolbox* and find **GDAL → Raster analysis → Slope** (algorithm `gdal:slope`). Select your DEM, set the ratio of vertical to horizontal units correctly (normally 1 when both are metres), and enable **Express slope as percent (instead of degrees)**. Save the result as `outputs/slope_percent.tif`.

Do not confuse this with the QGIS native Slope tool (`native:slope`), which outputs **degrees**. If you choose the native tool instead, you must convert the result before using the percentage categories below.

**Checkpoint:** Inspect several raster cells. Almost-level areas should be near 0%; visibly steeper terrain should have larger values. Check edge and NoData areas.

### 2. Translate slope into accessible categories

Instead of displaying a continuous rainbow, classify the raster into five **architectural interpretation bands**:

| Gradient | Map label | Design interpretation |
| --- | --- | --- |
| **0–2%** | Nearly level | Potentially suitable for level uses such as gathering or parking, subject to drainage, surface and detailed design |
| **2–5%** | Gentle slope | Shallow approaches and pedestrian routes may be feasible |
| **5–8.33%** | Ramp-sensitive | More demanding gradients; accessible ramps require strict limits on rise, length and landings |
| **8.33–50%** | Steep terrain | A direct accessible ramp is unlikely; consider alignment across the slope, switchbacks, steps, terracing or lifts |
| **Over 50%** | Very steep | Likely to need significant earthworks, structures or a different route; investigate conditions carefully |

These are **interpretive teaching categories**, not statutory thresholds for the terrain itself. The 5% and 8.33% breakpoints are useful references to ramp design, but compliance cannot be established by colouring DEM pixels. UK Approved Document M, Volume 2, relates maximum ramp gradient to flight length and rise (for example 1:20 over 10 m, 1:15 over 5 m and 1:12 over 2 m). Parking and vehicle routes require their own criteria. The **50% threshold is deliberately provisional**, for discussing substantial intervention; it is *not* a universal limit beyond which stairs become impossible.

In *Raster → Raster Calculator* (or the corresponding QGIS raster calculator), use the following nested expression, replacing `slope_percent@1` with your actual raster layer/band name:

~~~text
if("slope_percent@1" < 2, 1,
  if("slope_percent@1" < 5, 2,
    if("slope_percent@1" < 8.33, 3,
      if("slope_percent@1" <= 50, 4, 5)
    )
  )
)
~~~

Choose the slope raster as the reference for **extent, resolution and CRS**. Save as `outputs/slope_classes.tif`. The expression assigns class numbers 1–5; invalid / NoData cells should remain NoData rather than being described as a terrain category. Check the output values before styling.

Set the layer’s symbology to a **Paletted / Unique values** renderer with five distinct, ordered colours and meaningful labels. A restrained progression from pale to dark is more legible than a rainbow. Keep the DEM hillshade or contours faintly visible underneath to show landform.

**Checkpoint:** A reader should be able to identify nearly level ground and steep terrain from the legend without knowing how raster slope is calculated.

### 3. Test the architectural interpretation

Choose two possible routes between the same points. One may take the shortest line up a steep slope; another might traverse the contour more gradually. Compare the classified terrain under each route.

The raster reports the **maximum local terrain slope**, not necessarily the slope *along a designed path*. A diagonal route can be gentler than the hillside it crosses. In addition, accessible design depends on continuity, crossfall, landing geometry, surface, drainage and users’ needs. Treat the map as a screening tool, not a pass/fail accessibility assessment.

## Exercise 2 — Aspect as a solar question

### 4. Calculate aspect

**Aspect** is the compass direction a slope faces. For a conventional north-referenced aspect raster, **0°/360° is north, 90° east, 180° south and 270° west**.

Find **GDAL → Raster analysis → Aspect** (`gdal:aspect`), using the same DEM as for slope. Keep its default **azimuth** convention: do **not** activate the option to return a trigonometric angle, which would change the directional reference. Save the result as `outputs/aspect_degrees.tif`.

Aspect is unreliable on completely flat terrain, because a horizontal surface has no meaningful downslope direction. It is also prone to noisy changes where very small height differences dominate. We will mask nearly level areas using the slope raster.

**Checkpoint:** Inspect the aspect values and confirm they follow compass directions clockwise from north.

### 5. Reclassify aspect into daily solar orientations

For a **northern-hemisphere** site, we can use four broad orientations to start a conversation about sunlight:

| Aspect azimuth | Category | Approximate interpretation |
| --- | --- | --- |
| 45°–135° | East | More favourable orientation towards morning sun |
| 135°–225° | South | More favourable orientation towards midday sun |
| 225°–315° | West | More favourable orientation towards afternoon / evening sun |
| 315°–360° **or** 0°–45° | North | Generally lower direct solar exposure in many seasons |

These are **orientations**, not clock-time bands and not measured sunlight durations. At different times of year the sun rises and sets in different directions; during summer even some northern orientations can receive low-angle direct sunlight.

Use a Raster Calculator expression to assign values **0 = nearly flat**, **1 = east**, **2 = south**, **3 = west**, **4 = north**. It uses both layers, which must share the **same grid alignment, pixel size and extent**:

~~~text
if("slope_percent@1" < 2, 0,
  if("aspect_degrees@1" < 45, 4,
    if("aspect_degrees@1" < 135, 1,
      if("aspect_degrees@1" < 225, 2,
        if("aspect_degrees@1" < 315, 3, 4)
      )
    )
  )
)
~~~

Save as `outputs/aspect_solar_classes.tif` and use a **categorical colour legend**. Display class 0 in a neutral grey rather than implying it has a north-facing orientation. Preserve any NoData areas and check that the output doesn’t classify cells beyond the original raster coverage.

**Checkpoint:** You can explain which parts of the terrain face east, south and west, while recognising that the map does not calculate actual sunlight received.

## Exercise 3 — Read aspect against the sun’s path

### 6. Use Andrew Marsh’s Sun-Path on Map

Open **[Andrew Marsh — Sun-Path on Map](https://andrewmarsh.com/software/sunpath-on-map-web/)**. Set the location of your study area and examine the sun’s **azimuth** (compass direction) and **altitude** (angle above the horizon) on different dates.

Compare at least three times on the same day: morning, solar noon and afternoon. Repeat the comparison for a winter and a summer date. Note that **solar noon is not always 12:00 on the clock**, particularly where daylight-saving time is used.

For a comparative presentation, you can place a **clearly labelled screenshot or redrawn sun-path diagram beside your aspect map**, or overlay it on the map after aligning **true north**, location and scale. A circular sun-path diagram conveys directions and solar altitude, not an automatic ground-level illumination map. If exporting a screenshot from Andrew Marsh’s tool, retain appropriate attribution and check permission for reuse or publication.

Suggested figure composition: the classified aspect map on the left, a matching north-oriented sun-path diagram on the right, and three arrows indicating the sun direction at selected times. If overlaid, keep the aspect map legible and show the sun-path diagram as a separate explanatory layer.

### 7. Consider shadow and season

Compare an east-facing and west-facing slope. Which might experience morning or late-afternoon sun? How could that affect where people gather, or where one might favour outdoor activity?

Then ask a harder question: **Would the slope actually be illuminated at that time?** Aspect alone cannot answer, because other hills, trees or buildings may block the sun. A future extension could use a **digital surface model (DSM)** and sun-angle-based shading analysis to estimate shadows and solar exposure. This exercise deliberately stops at directional interpretation.

## Suggested submission and interpretation

Produce **two maps** of the same study area and a small annotated solar diagram:

1. A classified **slope map** with five meaningful gradient bands and a brief note identifying possible routes, level uses and steep constraints.
2. A classified **aspect map** showing east, south, west, north and nearly flat areas, with a north arrow and the same map extent.
3. An **Andrew Marsh sun-path comparison** for one winter and one summer date, with morning, solar-noon and afternoon directions labelled.

Include your DEM source, CRS, resolution, vertical units, classification thresholds and the dates/times used for the solar diagram. Write a short paragraph distinguishing what your maps **measure** from what you **infer** about architectural possibilities.

## Troubleshooting and limitations

- **Unexpected slope values:** Confirm horizontal versus elevation units, CRS, whether you requested degrees or percentage, and how the DEM was resampled.
- **Aspect appears rotated:** Verify the tool used azimuth measured clockwise from north, not its optional trigonometric convention.
- **Speckled aspect on flat land:** Mask nearly level cells or consider DEM smoothing, documenting any change in scale or resolution.
- **Class raster shows a continuous gradient:** Render it as **Paletted / Unique values**, not Singleband pseudocolour.
- **Output doesn't line up:** Match raster extent, pixel dimensions and CRS; merely assigning another CRS does not transform coordinates.
- **Design categories seem misleading:** Revisit the thresholds, the chosen route alignment and applicable local accessibility/parking guidance. Neither slope nor aspect automatically defines buildability or regulatory compliance.

## References and verification

- [QGIS GDAL Raster Analysis — Slope and Aspect](https://docs.qgis.org/3.44/en/docs/user_manual/processing_algs/gdal/rasteranalysis.html)
- [QGIS Raster Calculator](https://docs.qgis.org/3.44/en/docs/user_manual/working_with_raster/raster_analysis.html)
- [Andrew Marsh — Sun-Path on Map](https://andrewmarsh.com/software/sunpath-on-map-web/)
- [Approved Document M, Volume 2 (England) — ramped access](https://www.gov.uk/government/publications/access-to-and-use-of-buildings-approved-document-m)

**Desktop checklist:** Confirm the raster’s real CRS, units, extent and suitability; test both GDAL algorithms and expressions; check raster alignment, class symbology and NoData; try the exercise with the supplied data; add genuine QGIS screenshots and a properly attributed sun-path illustration; decide whether the provisional slope classes need refinement. The files are a starting point, not verified outputs.
