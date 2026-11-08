# Investigating Cities from Space
*Google Earth Engine, Python and AI-assisted coding*

[Mapping tutorials](../README.md) | [RC15 Resources](../../../README.md)

**Software:** [Google Earth Engine Code Editor](https://code.earthengine.google.com/), ChatGPT; optional QGIS and Google Colab  
**Study area:** Berlin, with a closer look at Tempelhofer Feld  
**Starting point:** No previous knowledge of the Earth Engine API or JavaScript required

> **Screenshot to add:** Finished vegetation-change map of Berlin.

Satellite imagery allows us to investigate a city beyond what we can see in an ordinary aerial photograph. We can explore vegetation, surface temperature, water and urban growth, and compare observations from different years. [Google Earth Engine](https://earthengine.google.com/) provides access to extensive collections of satellite data and processes them on Google's servers.

This tutorial is also an experiment in **AI-assisted coding**. Rather than learning every command in advance, we will discuss a spatial question with ChatGPT, copy the resulting code into Earth Engine, inspect what happens and ask follow-up questions. The goal is not to produce code as quickly as possible. It is to develop an investigation through conversation and gradually understand the decisions behind it.

We will begin in the **Earth Engine Code Editor**, which has a built-in map. Once the investigation works, we will export a georeferenced raster for QGIS and briefly look at how the same approach can continue in Python through Google Colab.

## 1. Getting started in the Code Editor

### Open Earth Engine

Visit [code.earthengine.google.com](https://code.earthengine.google.com/). Sign in with your Google account and follow the prompts to register for Earth Engine and select or create a Google Cloud project with Earth Engine enabled. Google may ask you about the intended use and project eligibility. These steps and screens can change; follow the current instructions in the browser.

The Code Editor runs JavaScript. That is fine even if you have never written JavaScript: ChatGPT can help us generate and explain each small piece of code.

> **Screenshot to add:** Code Editor, identifying script panel, Run button, map, Layers control, Console and Tasks.

### Our first map

Begin with a question you can ask ChatGPT:

> I am new to Google Earth Engine. I want to investigate Berlin using the Code Editor. Can you give me the smallest JavaScript example that centres the map on Berlin and displays the satellite basemap? Explain what each line does.

Paste the following into the Code Editor and click **Run**:

~~~javascript
// Our first map of Berlin
var berlin = ee.Geometry.Point([13.405, 52.52]);

Map.centerObject(berlin, 11);
Map.setOptions('SATELLITE');
~~~

The map moves to Berlin. This is Google's prepared satellite **basemap**: useful for orientation, but not yet an analysis of a dataset from the Earth Engine archive.

> **Screenshot to add:** Satellite basemap centred on Berlin.

### Display a satellite dataset

Now ask ChatGPT:

> Can we display an actual Sentinel-2 satellite image from summer 2026 instead of the default basemap? Please explain how the bands and colour display work.

Replace the script with:

~~~javascript
// Sentinel-2 summer image of Berlin
var berlin = ee.Geometry.Point([13.405, 52.52]);

var images = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
  .filterBounds(berlin)
  .filterDate('2026-06-01', '2026-09-01')
  .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20));

var image = images.median();

Map.centerObject(berlin, 11);
Map.addLayer(image, {
  bands: ['B4', 'B3', 'B2'],
  min: 0,
  max: 3000
}, 'Berlin – Sentinel-2');
~~~

Here, **B4, B3 and B2** are the red, green and blue bands. The display settings convert satellite measurements into screen colours, so the result may look more saturated than a conventional aerial photograph. The median combines observations from the selected period; the scene-level cloud filter alone does not remove every cloudy pixel.

The imagery is processed remotely. We do not need to download every original satellite scene.

> **Screenshot to add:** Sentinel-2 natural-colour composite of Berlin.

## 2. Investigating vegetation change in Berlin

### From a photograph to a measurement

Sentinel-2 records wavelengths beyond visible light. Plants typically absorb red light and reflect near-infrared light. We can use these measurements to calculate the **Normalized Difference Vegetation Index (NDVI)**:

**NDVI = (near-infrared − red) / (near-infrared + red)**

NDVI usually ranges between −1 and +1. High positive values often indicate active vegetation; values near zero commonly correspond to bare or built surfaces, while negative values can occur over water. NDVI is a measure of spectral greenness, **not** a direct count of trees or an exact measure of green-space area.

Ask ChatGPT:

> Can we calculate NDVI for the Berlin satellite image and show it in shades from brown to green? What do bands B8 and B4 represent?

Starting from the **Sentinel-2 script above**, add these lines at the bottom:

~~~javascript
var ndvi = image.normalizedDifference(['B8', 'B4']);

Map.addLayer(ndvi, {
  min: 0,
  max: 0.8,
  palette: ['#8c510a', '#f6e8c3', '#a6d96a', '#1a9850']
}, 'Vegetation – NDVI');
~~~

Use the **Layers** control to compare NDVI with the satellite image beneath it. Look for Tiergarten, Tempelhofer Feld and the smaller green spaces scattered across the city.

> **Screenshot to add:** NDVI map of Berlin, ideally with the Layers control visible.

### Compare two summers

A single map tells us little about change. Let's compare **summer 2018** with **summer 2025**, keeping the same months and colour scale. Ask ChatGPT:

> Can you adapt the analysis so I can compare summer NDVI in 2018 and 2025? Please filter likely clouds and cloud shadows, and let me switch between the years.

For this experiment, **replace the full previous script** with:

~~~javascript
// Berlin vegetation: 2018 versus 2025
var berlin = ee.Geometry.Point([13.405, 52.52]);

// Mask likely clouds, shadows, snow and invalid pixels.
function maskClouds(image) {
  var scl = image.select('SCL');
  var clear = scl.neq(0)
    .and(scl.neq(1))
    .and(scl.neq(3))
    .and(scl.neq(8))
    .and(scl.neq(9))
    .and(scl.neq(10))
    .and(scl.neq(11));

  return image.updateMask(clear);
}

// Calculate a summer NDVI composite for one year.
function summerNDVI(year) {
  var images = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
    .filterBounds(berlin)
    .filterDate(year + '-06-01', year + '-09-01')
    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 60))
    .map(maskClouds);

  return images.map(function(image) {
    return image.normalizedDifference(['B8', 'B4'])
      .rename('NDVI');
  }).median();
}

var ndvi2018 = summerNDVI(2018);
var ndvi2025 = summerNDVI(2025);

var colours = {
  min: 0,
  max: 0.8,
  palette: ['#8c510a', '#f6e8c3', '#a6d96a', '#1a9850']
};

Map.centerObject(berlin, 11);
Map.addLayer(ndvi2018, colours, 'Summer 2018', false);
Map.addLayer(ndvi2025, colours, 'Summer 2025', true);
~~~

A **function** lets us apply the same calculation to more than one year, rather than writing the entire script twice. The **SCL** band identifies likely cloud, shadow and other scene classes; excluding these helps, but it does not guarantee that every pixel is cloud-free. We have also kept the same summer months and visualisation range for a more consistent comparison.

Switch the two layers on and off. Do you see differences in Tempelhofer Feld, around Tiergarten, or in residential streets?

> **Screenshot to add:** Comparison of 2018 and 2025 using the same legend.

### Map the difference directly

Switching layers is useful, but Earth Engine can calculate the difference for us. Ask ChatGPT:

> Can we subtract the 2018 NDVI from the 2025 NDVI? Please make decreases red, little change white and increases green.

**Add** this code to the end of the 2018/2025 script:

~~~javascript
var change = ndvi2025.subtract(ndvi2018);

Map.addLayer(change, {
  min: -0.3,
  max: 0.3,
  palette: ['#b2182b', '#f7f7f7', '#1a9850']
}, 'Vegetation change 2018–2025');
~~~

A pixel changing from NDVI 0.3 to 0.6 produces **+0.3** (green); one changing from 0.6 to 0.3 produces **−0.3** (red). The colour range is a display choice, not a threshold that defines vegetation loss.

> **Screenshot to add:** Red–white–green NDVI difference map, focused on Tempelhofer Feld.

**Stop and interpret.** A difference map shows a change in the satellite-derived vegetation signal. It does not automatically prove that trees were planted, buildings replaced a park, or green space disappeared. Rainfall, irrigation, mowing, crop or grass cycles, atmospheric effects and the selection of images can all influence NDVI. Before making strong claims, investigate several years, check the available observations and compare the result with independent sources.

Try asking ChatGPT: *Could the difference be caused by a particularly dry summer? How could we test that?*

### Export the analysis

Now we will take the result out of Earth Engine. A **GeoTIFF** stores pixel values together with information about their geographic position. Unlike a screenshot, it remains useful for spatial analysis in other software.

Ask ChatGPT:

> How can I export the actual NDVI difference values around Tempelhofer Feld as a GeoTIFF to Google Drive? I want to open the data in QGIS, not just save a coloured image.

**Add** this code below the difference-map code:

~~~javascript
// Export an area around Tempelhofer Feld.
var tempelhof = ee.Geometry.Point([13.403, 52.473])
  .buffer(4000)
  .bounds();

Map.centerObject(tempelhof, 12);

Export.image.toDrive({
  image: change.rename('NDVI_change'),
  description: 'Berlin_NDVI_Change_2018_2025',
  folder: 'EarthEngine',
  region: tempelhof,
  scale: 10,
  fileFormat: 'GeoTIFF',
  maxPixels: 1e9
});
~~~

Click **Run**, open the **Tasks** tab, then start the export task and confirm its settings. When processing finishes, find the resulting TIFF in the **EarthEngine** folder in Google Drive and download it. The export is limited to an area around Tempelhofer Feld to keep the file manageable; the 10 m export scale does not create detail beyond that available in the source observations.

> **Screenshots to add:** Earth Engine Tasks panel; resulting GeoTIFF in Google Drive.

### Display the result in QGIS

Open QGIS and drag the downloaded GeoTIFF onto the map. You can use **Layer Properties → Symbology → Singleband pseudocolor** to create a diverging colour ramp: red for negative values, white around zero, green for positive values. Set the range approximately to **−0.3 to +0.3**, with **0** at the centre, as in Earth Engine. Add a suitable basemap to see streets, neighbourhoods and park boundaries beneath the analysis.

The raster contains numbers such as −0.18 or +0.12, not red or green colours. QGIS decides how those numbers are displayed. Use the Identify tool to inspect a pixel, and check **Layer Properties → Information** for the layer's CRS, extent and pixel size. QGIS can reproject layers for display, but that does not alter the underlying data.

> **Screenshot to add:** Exported raster styled over a Berlin basemap in QGIS.

We have moved from a research question to a satellite-derived dataset that can be combined with our existing mapping and design workflows. For more detail about QGIS raster display and coordinate reference systems, see the other [mapping tutorials](../README.md).

## 3. Continuing in Python with Google Colab

The Earth Engine Code Editor is a useful starting point because the script and map sit together. Once we understand the investigation, we can use the **same Earth Engine datasets and operations** through Python in a [Google Colab notebook](https://colab.research.google.com/).

This is a change of programming interface, not a new satellite data source. Python can be convenient when we want to combine geospatial work with data tables, charts or other analysis libraries. Unlike the Code Editor, Colab requires explicit Earth Engine authentication and initialisation with an Earth Engine-enabled Cloud project.

For now, we do not need to reproduce the whole tutorial. Start with a new Colab notebook and ask ChatGPT:

> We have compared summer NDVI in Berlin using JavaScript in the Google Earth Engine Code Editor. Can you help me translate the analysis to Python in Google Colab, one cell at a time? Begin with authentication and showing a map. Explain differences from JavaScript only when they matter.

A starting cell is:

~~~python
import ee

ee.Authenticate()
ee.Initialize(project='YOUR_CLOUD_PROJECT_ID')
~~~

Replace the placeholder with the ID of your own Earth Engine-enabled Google Cloud project. Follow the authentication prompts. To display an interactive map, ask ChatGPT to introduce a notebook mapping library such as **geemap**, including any installation steps required for your Colab session.

> **Screenshot to add (optional):** Colab notebook with code and an interactive map.

For help moving data between Colab, Google Drive and your computer, see [File Access in Google Colab](../../programming-and-data-access/file-access-in-google-colab/README.md).

## 4. Where could we go next?

We have only begun to explore Earth Engine. The most interesting next step is not necessarily another command; it is **another question**. Here are some directions worth investigating with ChatGPT:

- **Animated vegetation time series.** Instead of comparing two summers, calculate NDVI for many years and animate the maps. Does an apparent trend persist, or does it fluctuate with the weather? Ask how to export an animation and how to keep its colour scale consistent.
- **Urban surface temperature.** Use a suitable Landsat thermal product to compare parks and built-up areas. Remember that satellite-derived *land surface temperature* is not the same as air temperature.
- **Water and flooding.** Explore changing water extent with optical imagery or Sentinel-1 radar. Investigate why radar can be helpful when clouds obscure the ground.
- **Urban expansion.** Compare built-up or land-cover datasets over time, then examine what their spatial resolution can and cannot show.
- **Seasonal change.** Compare spring, summer and autumn vegetation in the same year. How much of what looked like long-term change is actually seasonal?
- **Compare cities.** Repeat an analysis for London, Berlin or another city, while considering whether the same methods and time windows are appropriate.
- **Measure and chart.** Instead of only producing coloured maps, calculate average NDVI inside a defined area and plot a time series. How does the result change if the study boundary changes?

The [Earth Engine Data Catalog](https://developers.google.com/earth-engine/datasets/catalog) is a useful place to discover other datasets. You do not have to read it cover to cover. Use it when a particular question makes a dataset relevant, and ask ChatGPT to help you assess its resolution, time coverage and limitations.

### Working with ChatGPT

You do not need to memorise every Earth Engine command or read endless documentation before starting. Describe what you want to investigate, run a small example, show ChatGPT the outcome or error, and continue the discussion. Ask for explanations whenever the code introduces an unfamiliar idea.

But **working code is not the same as reliable evidence**. Check what a dataset measures, whether the time periods are comparable, how missing or cloudy observations are handled, and whether the visualisation supports your interpretation. The conversation can help you ask better questions; it cannot replace your judgement about the answers.

---

**Useful links:** [Earth Engine Code Editor](https://code.earthengine.google.com/) · [Earth Engine Data Catalog](https://developers.google.com/earth-engine/datasets/catalog) · [Earth Engine Guides](https://developers.google.com/earth-engine/guides) · [Google Colab](https://colab.research.google.com/)

*This resource is designed as a starting point for experimentation. Screenshots will be added to illustrate the stages of the workflow.*