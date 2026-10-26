# 5. Representing the Landscape — From Rhino to Illustrator

[← Chapter 4: Building a 3D Landscape](04-grasshopper-landscape.md) · [Sentiment Landscapes overview](README.md)

We now have a three-dimensional surface whose elevation represents the number of geolocated Flickr photographs in each grid cell. The model makes concentrations of photographic activity visible as peaks, but it does not yet show enough of the city to help viewers recognise *where* those peaks are.

In this final practical chapter, we will add geographical context, generate contour lines, prepare an accurate two-dimensional drawing and compose the results in **Adobe Illustrator**. The aim is not simply to decorate the model: the graphic should explain what the heights represent and help people locate the patterns in the city.

![Example landscape representation](Images/ViewCapture20250712_174129.png)

*An existing view from the project archive. Your result will depend on your data, study area, height scale and graphic choices.*

## 5.1 Decide what the final drawing should communicate

Before choosing colours or a background, decide which information matters most. Our primary subject is **the distribution of photograph counts**. The city map provides spatial orientation, while the surface and its contours reveal concentrations and transitions.

We will prepare two complementary views:

1. **An oblique landscape view** showing the three-dimensional peaks and their relationship to the city.
2. **A plan-based graphic** showing the positions of the contours and relevant streets or other geographical features.

Both can be assembled in Illustrator. They should use the same study boundary, dataset and height transformation, even if they employ different visual languages.

**Checkpoint:** you can describe in one sentence what a peak represents, and you know which visual elements are primary and which are only contextual.

## 5.2 Add geographical context — choose one approach

The landscape was constructed in Rhino coordinates using Heron. Any map we place beneath it must refer to **the same geographic location and coordinate reference**. An attractive map that is shifted or stretched relative to the peaks is misleading.

You do **not** need all three approaches below. Start with the first; use the others as alternative design routes.

### Option A — Export a map from QGIS (recommended for a first attempt)

Return to the QGIS project from Chapter 3. Hide analysis layers that would clutter the drawing. Style a small set of geographic features such as major roads, waterways and the study boundary. You can use an appropriately licensed basemap, or prepare your own simple vector map.

Create a **Print Layout** with the same area of interest and an explicitly chosen map extent. Export the result as a PDF for vector content or a high-resolution image for raster content. Keep a copy of the selected extent and the output dimensions.

This option is usually easiest for beginners because QGIS already knows the positions of the geographic features. **The export is not automatically aligned with the Rhino drawing**: you must establish a matching extent and scale when composing the two outputs. A particularly dependable method is to carry the same study-area boundary or registration corners into both the QGIS and Rhino drawings, and use them to align the graphics in Illustrator.

**Checkpoint:** you can identify at least two corresponding places or boundary corners in the QGIS map and in your Rhino model.

### Option B — Bring OpenStreetMap vectors into Grasshopper with Heron

**OpenStreetMap (OSM)** describes geographic features such as roads, buildings, parks and waterways. Heron can read OSM vector data and convert it into Rhino geometry.

Heron's **Import OSM** and **Import Vector** components support OSM files. A typical workflow is to provide an OSM file and a clipping boundary, examine the feature types or tags, and extract only the geometry needed for your drawing. See [Heron Import OSM](https://grasshopperdocs.com/components/heron/importOSM.html) and [Heron Import Vector](https://grasshopperdocs.com/components/heron/importVector.html).

The source archive includes `Rhino/assets/map.osm` and `assets/EastLondon.osm` as smaller examples. Other OSM downloads were deliberately omitted because of their file sizes; **a city-wide dataset is not required** for this exercise.

Check that the same Earth Anchor Point and geographic reference are used for both the imported map and the landscape. Preview a few recognisable streets or features, then compare their positions against QGIS before continuing.

OSM gives you considerable control over linework, but it also introduces decisions about feature filtering and styling. Do not import every available object merely because it exists.

**Checkpoint:** selected OSM features align with the underlying geographical footprint of the landscape.

### Option C — Use aerial imagery

An aerial image can make the relationship between the artificial topography and the physical city immediately recognisable. However, an ordinary JPEG does not automatically carry enough georeferencing information to position itself accurately.

Use an image with a **known geographic extent**, preferably exported from a QGIS layout or obtained as an appropriately georeferenced raster. Heron supports georeferenced raster imports, but whether an image can be positioned directly depends on its accompanying spatial information. See [Heron Import Raster](https://grasshopperdocs.com/components/heron/importRaster.html).

Place the image on a flat surface or keep it as a separate Illustrator background, ensuring that its corners match the same study-area registration points. The archive contains `Rhino/assets/aerial_0.jpg` as a visual reference, but do not assume it is georeferenced or matches a newly collected study extent.

**Checkpoint:** the aerial image matches the intended area without arbitrary stretching. Check its licence and attribution before publication.

## 5.3 Generate contour lines in Grasshopper

The surface is now ready to be translated into linework.

A **contour** is a curve joining positions that share the same elevation. For our artificial landscape, each contour corresponds to a particular value on the *remapped height scale*; it is not a physical terrain elevation.

In Grasshopper, add the **Contour** component (or the corresponding contour component available in your Grasshopper version). Connect the landscape surface as the geometry to intersect with a sequence of **horizontal cutting planes**.

The usual approach is to provide:

- The landscape **surface** as the shape to contour.
- A **horizontal base plane** (parallel to Rhino's World XY plane).
- A regular **distance or interval** between contour sections.

For example, if your remapped landscape extends from 0 to 200 Rhino metres, try contour intervals of 10 or 20 model units. These are **visualisation units** resulting from the height transformation in Chapter 4, so label them accordingly.

Preview the curves with the surface temporarily hidden. Are the contours concentrated around peaks? Do they form recognisable rings or bands? Reduce the interval for finer linework or increase it if the drawing becomes too dense.

A technical distinction matters here: **normal contour curves remain at their respective Z elevations**. They are not automatically a flat map. We will flatten or project them when preparing the two-dimensional drawing.

**Checkpoint:** changing the contour interval changes the spacing between sections, while the position and size of the underlying surface remain unchanged.

Reference: [Grasshopper Contour (ex)](https://grasshopperdocs.com/components/grasshopperintersect/contourex.html).

## 5.4 Experiment with one highlighted contour

Besides generating a complete series of contours, try extracting **one horizontal section at a chosen elevation**.

Create a horizontal cutting plane and move it vertically with a slider. Intersect that plane with the landscape surface. The resulting curve reveals where the landscape crosses that selected threshold.

Move the slider gradually and observe how the intersections change. At lower levels, the curve may encompass several nearby concentrations; at higher levels, it may split into smaller loops around the strongest peaks.

This is a useful way to create a selective graphic: one bold threshold contour can draw attention to a significant range of values without displaying every line.

**Important:** because we remapped photograph counts into heights, a plane at (for example) Z = 100 does not necessarily mean 100 photographs. Translate the selected Z value back through the chosen mapping before labelling it as a count.

Save or bake one threshold curve that contributes to your graphic. Explain why that threshold is interesting.

## 5.5 Bake the surface and curves into Rhino

Until now, most geometry exists as a **Grasshopper preview**. It can be seen in Rhino but is not necessarily ordinary, editable Rhino geometry.

**Baking** creates Rhino objects from the Grasshopper geometry. Before baking, organise the result into a few clear categories: the landscape surface, contour curves, one highlighted contour, study-area boundary and selected map context.

Create appropriately named Rhino layers, for example:

```text
01_Landscape
02_Contours
03_Highlight_Contour
04_Map_Context
05_Study_Boundary
```

Bake the geometry you actually intend to keep. In Grasshopper, the standard way is to right-click the relevant geometry parameter or component and choose **Bake**, then assign an appropriate Rhino layer. If you are using the archive's Human baking components, check their destination-layer configuration first; they are optional for this exercise.

Hide the Grasshopper previews after baking and inspect the result in Rhino. Avoid baking repeatedly into the same layers without checking for duplicates. Save your Rhino document.

**Checkpoint:** the surface and selected linework can be selected directly in Rhino after Grasshopper preview is disabled.

## 5.6 Make a two-dimensional drawing

We will now translate the three-dimensional geometry into a drawing suitable for Illustrator.

Rhino's **Make2D** command creates flat curves from selected geometry as seen from a chosen view. This is useful for generating the visible outline of the landscape from an oblique projection. According to the [Rhino 8 Make2D documentation](https://docs.mcneel.com/rhino/8/help/en-us/commands/make2d.htm), the command produces edges and silhouettes as flat curves; it is **not** a substitute for calculating analytical contour intersections.

### An oblique line drawing

1. Choose a Rhino view in which the peaks are legible. Use a **parallel projection** if you want an axonometric rather than a perspective drawing.
2. Select the baked surface and any other geometry that should be part of the projected drawing.
3. Run **`Make2D`** and select the **current view** projection.
4. Inspect visible and hidden-line options; place the resulting curves on dedicated output layers.
5. Move the generated 2D output away from the model before editing, or save a separate working copy for the drawing.

The resulting curves reflect the **chosen viewpoint**, so changing the camera can change their visual relationship. Keep one deliberate view for the final composition.

### A plan drawing of the contours

For a plan of equal-value contour lines, use the actual contour curves generated in Grasshopper. Since those curves sit at different elevations, make **flat copies projected to World XY** (or use an equivalent, checked projection workflow). Keep the original 3D contours unchanged.

This produces a top-down graphic in which the contour shapes retain their geographic X/Y positions and can align with streets or a background map. **Do not rely on Make2D alone to generate contours that were never computed.**

**Checkpoint:** you have a clean oblique drawing and/or a flat plan of contours, with no unwanted duplicate lines.

## 5.7 Export the drawing to Illustrator

Create a separate Rhino layer or file containing only the final 2D drawing geometry. Check that the linework has a sensible size and that you have included registration corners or a study-area outline if you need to align it with a QGIS export.

Export the selected 2D curves to a **vector format Illustrator can open**, such as a PDF. The exact export options may depend on your Rhino installation and whether you print to PDF or export drawing geometry. Inspect the result in Illustrator before continuing: do not assume every display colour, layer name or lineweight will transfer unchanged.

Open the exported vectors in **Adobe Illustrator**. If you prepared a separate QGIS map, place it on a background layer and use the same known extent or registration geometry to match its alignment with the contour plan. Lock the map layer once aligned so it cannot be moved accidentally.

The existing `Illustrator/` folder contains original AI compositions, including `Heron.ai` and `Heightfield [Converted].ai`. These are useful for analysing the original graphic language, but their linked resources and version compatibility should be checked before reuse.

## 5.8 Compose the final graphic

Our drawing should help the viewer read the landscape and the city at the same time. Try building the composition with a clear visual hierarchy:

- **Primary:** the landscape silhouette or contours showing the photographic concentrations.
- **Secondary:** geographical context — a restrained street network, waterways or aerial background.
- **Explanatory:** title, study-area location, data source, counting method and legend.

Avoid using a colour scheme that makes the map background compete with the peaks. Contours can be varied through lineweight, opacity or selective emphasis. A single threshold contour can be stronger than dozens of equally prominent lines.

Add a concise legend explaining that the heightfield represents **counts of geolocated Flickr photographs aggregated by grid cell**, not a measure of sentiment or the city's physical elevation. State the grid size and explain the vertical exaggeration if the drawing suggests real topographic heights.

Also include a short source note identifying Flickr as the platform and the date of collection. Credit map or imagery sources according to their licences.

![Archived image composition](Images/Heightfield%202.png)

*An archived representation from the project files; use it as a reference for graphic experimentation, not as an exact template.*

**Checkpoint:** someone unfamiliar with the exercise can recognise the study area and correctly explain what a peak represents.

## 5.9 Review what the landscape reveals — and what it does not

A concentration of photographs may indicate a recognisable landmark, a popular photographic viewpoint, an event or simply intensive participation by a small group of Flickr users. It is **not automatically a measure of popularity, appreciation or positive sentiment**.

Compare the three stages of representation: the original point map, the counted QGIS grid and the final landscape. What patterns become clearer through aggregation? What information disappears when thousands of points are combined into a single value? How different would the result look if you chose a larger grid or a less exaggerated height scale?

The final landscape is not an objective photograph of the city. It is a deliberate visual interpretation, shaped by the dataset and by your analytical and graphic choices.

## What to keep

For a reusable project, save the QGIS project and its generated grid layers, the centroid CSV, the Grasshopper definition, the Rhino file and your Illustrator working document. Keep one export of the finished illustration.

Your complete workflow is now:

**Flickr point locations → QGIS grid counts → centroid CSV → Heron X/Y coordinates → Grasshopper Z values → continuous surface → contour curves → Rhino 2D drawing → Illustrator composition.**

That same process can be adapted to other geographical datasets. An optional later extension will explore how to enrich point records with additional numerical attributes — for example, photograph favourites — and how to aggregate **averages** instead of simply counting observations.

> **Technical status:** This chapter draws on the supplied project archive and documented Rhino/Heron/Grasshopper tools. The complete combination of QGIS map alignment, OSM or raster imports, contours, Make2D and Illustrator export has **not been tested end to end** in the recorded software environment. Check the results at each stage rather than assuming that archival project settings transfer automatically.
