# Network Mapping in QGIS

Part of **RC15 Extended Knowledge**, a collection of tutorials and examples beyond the current curriculum.

**Software:** QGIS  
**Format:** Written tutorial  
**Software versions:** To be confirmed  
**Original collection:** Extra 08 - Network Qgis

[Browse this topic](../README.md) | [Library home](../../../README.md)

---

# All Roads Lead Here: Network Mapping in QGIS

Create a branching map of shortest routes between one chosen location and a field of points across the city.

This exercise is inspired by moovel lab’s **Roads to Rome**, featured in [“Apparently, All Roads Do Lead to Rome” on ArchDaily](https://www.archdaily.com/893076/apparently-all-roads-do-lead-to-rome). That project traces routes from locations across Europe to Rome and gives shared routes greater visual weight. Here, we explore the same idea at an urban scale: **which streets connect the surrounding city to your site?**

![Completed map with blue routes converging at a pink focal point](assets/05%20Shortest%20Paths%20Styling.png)

The screenshots use central London. You can repeat the exercise around a station, public space, project site, or another destination in your own study area.

> This tutorial reconstructs the workflow shown in the screenshots. Grid spacing, precise site coordinates, and styling settings are not fully recorded in the images. Values suggested below are starting points, not recovered project settings.

## What you will make

You will create a focal point, generate a regular point grid, calculate routes along a street network, and use transparent blue lines to reveal shared corridors. You will finish with a map ready to export for a presentation or portfolio.

The workflow uses QGIS’s built-in processing tools. The TravelTime toolbar visible in the screenshots is not needed.

## Before you begin

You will need:

- QGIS with the **Processing Toolbox** available through **Processing → Toolbox**. Menu wording may vary between versions.
- A **line vector layer** containing streets or paths for your study area. A background map alone cannot provide a routing network.
- An optional light background map for geographical context.
- A folder for your QGIS project and saved data.

The screenshot’s network is named `gis_osm_roads_free_1`. For London, a suitable starting source is the [Geofabrik Greater London download page](https://download.geofabrik.de/europe/united-kingdom/england/greater-london.html). Download and extract the shapefile package, then load `gis_osm_roads_free_1.shp` into QGIS. Keep its accompanying files together.

This tutorial starts from a usable network; the folder containing these screenshots does not include the original road data or QGIS project. An unfiltered road extract is suitable for exploring this graphic technique, but a walking or driving study requires appropriate access and direction rules.

### Set up your project

1. Load your street network and zoom to the area around your site.
2. Save the project as `All_Roads_Lead_Here.qgz`.
3. Choose a projected coordinate reference system (CRS) suited to the study area. For London, use **EPSG:27700 — OSGB36 / British National Grid** for metre-based grid spacing.
4. If necessary, right-click the network and choose **Export → Save Features As…** to create a working copy in that CRS. A GeoPackage is convenient for saving your layers.
5. Set the project CRS to match your working layers using the CRS control at the bottom right of the QGIS window.

The screenshots display **EPSG:3857**, which you can use to follow their setup. The suggested London workflow uses EPSG:27700 so grid spacing is meaningful locally. Changing the project CRS changes the display; exporting a layer actually transforms its coordinates. Do not use **Set Layer CRS** to convert data.

Keep the network larger than the endpoint grid: a valid shortest route may need to leave the study boundary and return.

## 1. Mark your focal point

Decide which location should anchor the map. In the screenshots, a large pink cross marks this position in central London.

1. Choose **Layer → Create Layer → New GeoPackage Layer…**.
2. Create a **Point** layer named `StartPT`, using your working CRS.
3. Select the layer and enable **Toggle Editing**.
4. Use **Add Point Feature** to place one point at your chosen location, preferably on or very close to a street in your network.
5. Save the edits and turn editing off.
6. Open **Layer Properties → Symbology**. Use a pink cross marker large enough to remain visible over the routes.

The point layer records and displays your site. Later, you will also supply this location to the routing tool with its map picker.

![A pink cross marks the focal point on a pale map of central London](assets/01%20Starting%20point.png)

**Checkpoint:** you have one clearly visible focal point and a street network covering the surrounding area.

## 2. Create a grid of endpoints

A regular grid samples the city evenly. Each point will provide an endpoint for one route from your focal point.

1. Search for **Create grid** in the Processing Toolbox.
2. Open the tool and enter the settings below.
3. For **Grid extent**, use the extent selector to draw a rectangle around your study area or use the current map canvas extent.
4. Save the output, run the tool, and rename the resulting layer `End`.

| Setting | Suggested value |
| --- | --- |
| Grid type | **Point** |
| Grid extent | Your chosen study area |
| Horizontal spacing | **250 metres** for a first test |
| Vertical spacing | **250 metres** for a first test |
| Horizontal / vertical overlay | **0** |
| Grid CRS | Your working CRS, e.g. **EPSG:27700** |
| Grid output | A saved point layer named `End` |

These are suggested settings. A coarser grid produces fewer routes and is easier to check; a finer grid adds detail and takes longer to process. Halving spacing in both directions produces roughly four times as many points over the same area.

Style `End` as small pink circles, with `StartPT` above it in the Layers panel.

![Create grid dialog and a regular field of pink endpoint markers](assets/02%20End%20points.png)

> **Do not copy the 1-metre spacing shown in the dialog.** The screenshot shows an unfilled extent and default-looking spacing values, not a completed parameter record. A 1-metre grid across this area would create far too many points for this exercise.

Some grid points may fall inside buildings, parks, or the river. They sample locations; they are not verified entrances. For a more specific study, remove inappropriate points or replace the grid with actual entrances or destinations.

**Checkpoint:** the grid covers the intended study area without producing an unmanageable number of points.

## 3. Check the street network

Turn on the street layer. You should now see the network beneath the pink endpoint grid and the larger focal-point cross.

![Street network visible beneath the endpoint grid](assets/02.1%20Path%20Network.png)

Before calculating routes, inspect the network at a few important junctions and river crossings. Streets that appear to cross are not necessarily connected in the data, and a bridge must not connect to every road beneath it.

For this introductory map, treat the network as bidirectional. This is a deliberate simplification. For a transport analysis, first select streets appropriate to the mode of travel and configure the relevant restrictions.

Avoid trimming the network exactly to the grid boundary. This can remove useful connections and cause artificial detours or missing routes.

**Checkpoint:** the focal point and endpoint grid sit within a network with plausible connections.

## 4. Calculate the shortest paths

Search for **Shortest path (point to layer)** in the Processing Toolbox, under **Network analysis**.

| Parameter | What to enter |
| --- | --- |
| Vector layer representing network | Your working street layer |
| Path type to calculate | **Shortest** |
| Start point | Use the map picker to click the `StartPT` location |
| Vector layer with end points | `End` |
| Shortest path | Save as `Shortest_paths.gpkg` |
| Non-routable features, if available | Save an output to inspect failures |

Under **Advanced Parameters**, leave the direction field unset and choose **Both directions** as the default for this simplified exercise. Start with topology tolerance at **0**. A larger tolerance can connect nearby nodes, so change it only to address a known data issue.

QGIS connects the input locations to the network. If your version provides **Maximum point distance from network**, use it to limit distant connections; an unset value permits snapping at any distance. Inspect remote endpoints carefully.

Click **Run**. See the [QGIS network analysis documentation](https://docs.qgis.org/3.44/en/docs/user_manual/processing_algs/qgis/networkanalysis.html) for parameter definitions.

![Shortest path point-to-layer dialog with the End layer selected](assets/03%20Shortest%20Paths.png)

The screenshot leaves the network and start-point fields blank. Fill them before running.

### Why start at the site?

The reference project routes many locations **towards** one destination. The pictured QGIS tool routes **from** one point to many endpoints. With bidirectional streets and the same distance cost, reversing travel gives equivalent minimum-distance routes, although equal-cost alternatives may differ. With one-way restrictions, the direction matters: use **Shortest path (layer to point)** for routes travelling towards the site.

## 5. Inspect the result

Turn off the original street network temporarily and give the output a solid dark-blue line symbol. Keep the endpoints visible while checking the routes.

![Dark-blue shortest paths branching between the focal point and grid endpoints](assets/04%20Shortest%20Paths%20Result.png)

The routes should form a branching pattern around your site. Many individual route features share the same street sections. This overlap is what we will make visible in the next step.

Check several routes closely:

- Do they follow the expected streets and cross the river at plausible locations?
- Do routes meet near your chosen focal point?
- Are endpoint connections sensible, particularly near water or isolated roads?
- Are any endpoints missing a route? Inspect the processing log and non-routable output, where available.

The pink markers can remain slightly away from the route ends because the routing locations are connected to the network. Do not assume every visible gap is a routing failure.

The screenshots include `Shortest path` and `Shortest path copy`. A duplicate is optional: it can hold an alternative display style, but you only need one computed result.

## 6. Reveal shared routes with transparency

The final screenshot uses pale blue branches and stronger blue corridors. The styling dialog is not shown; the following approach produces a similar effect by drawing overlapping routes with transparent symbols.

1. Open **Shortest paths → Properties → Symbology**.
2. Choose **Single symbol** and a **Simple line**.
3. Try blue **`#008BCB`** with a width of **0.35 mm**.
4. Open the line’s **stroke colour** picker and set colour opacity to about **10%**. Keep overall **Layer rendering → Opacity** at **100%**.
5. Apply the style. Adjust colour opacity between roughly **5% and 20%** until shared corridors stand out while individual branches remain visible.
6. Hide `End`, the original network, and any opaque duplicate route layer. Keep `StartPT` visible above the routes.
7. Use a pale grey background so the blue lines remain the focus.

These are suggested styling values. QGIS distinguishes symbol settings from layer rendering settings; see the [symbol selector documentation](https://doc.qgis.org/3.44/en/docs/user_manual/style_library/symbol_selector.html).

![Final styling with transparent blue branches, stronger shared corridors, and a pink focal point](assets/05%20Shortest%20Paths%20Styling.png)

**Why this works:** one transparent route looks faint; several routes drawn over the same street accumulate colour. Apply transparency to the stroke colour so this happens as individual features are drawn. Lowering the opacity of the finished layer as a whole does not create the same overlap effect.

Keep the individual route features. Dissolving them into a single network removes the repeated geometry that produces the effect.

This is a visual indication of route overlap, not a calibrated count. Colour saturates as more routes overlap. To reproduce the reference map’s count-based line widths, you would need an additional analysis that counts route traversals on each network segment.

## 7. Save and export your map

Save the project and ensure all temporary outputs you want to keep have been saved to disk. A `.qgz` project stores references to its data; it does not automatically contain those datasets.

For a presentation image:

1. Create a layout through **Project → New Print Layout…**.
2. Add a map and frame the branching pattern around your site.
3. Add a title, scale bar, and a short explanation of the method.
4. Include attribution for your data and background map. For OpenStreetMap data, include **© OpenStreetMap contributors** and the [OpenStreetMap copyright link](https://www.openstreetmap.org/copyright).
5. Export the layout as a PNG or PDF.

Suggested caption:

> Shortest routes between a regular sampling grid and the selected site. Stronger blue indicates overlapping calculated routes. The analysis assumes bidirectional travel and distance-based routing; it does not represent observed traffic.

## Reading the map

The map reveals how the selected network channels shortest routes around a particular site. Shared bridges, connecting streets, and bottlenecks may become visually prominent.

Its pattern depends on the site location, grid extent and spacing, street data, and routing assumptions. It does not directly measure pedestrian demand, traffic volume, comfort, safety, or the routes people actually choose.

Try moving the focal point across the river or to a nearby station, while keeping the same grid and network. Which shared corridors change, and which remain important?

## Troubleshooting

| Problem | What to check |
| --- | --- |
| The grid is extremely dense or processing is slow | Increase spacing and test a smaller extent. Check CRS units; avoid the screenshot’s 1-metre default. |
| No routes appear | Confirm that the network is a line layer, both point inputs are correct, and their locations overlap the network. Read the processing log. |
| Some endpoints have no route | Check disconnected streets, direction rules, and any maximum distance setting. |
| Routes make implausible jumps or detours | Inspect snapping locations, junctions, missing links, and network coverage beyond the grid. Avoid increasing tolerance indiscriminately. |
| All blue lines look equally strong | Reduce stroke-colour opacity; hide opaque duplicates and check that the routes have not been dissolved. |
| Fine branches disappear | Increase stroke-colour opacity or line width slightly, or lighten the background. |
| Layers disappear after reopening | Save temporary layers and keep referenced data in a stable location. |



Further reference: [QGIS Create grid documentation](https://doc.qgis.org/3.44/en/docs/user_manual/processing_algs/qgis/vectorcreation.html#create-grid).
