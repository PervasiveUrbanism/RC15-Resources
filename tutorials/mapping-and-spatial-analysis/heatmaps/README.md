# Heatmaps in QGIS

Part of **RC15 Extended Knowledge**, a collection of tutorials and examples beyond the current curriculum.

**Software:** QGIS  
**Format:** Written tutorial  
**Software versions:** To be confirmed  
**Original collection:** Extra 07 - Heatmaps

[Browse this topic](../README.md) | [Library home](../../../README.md)

---

# Heatmaps in QGIS

## Creating Density Maps from Point Data

This tutorial explains how to create and refine heatmaps in QGIS. Heatmaps are useful for visualising spatial density, but the default output is not always suitable for presentation graphics. The techniques below show how to improve clarity and visual quality.



## What is a Heatmap?

In QGIS, heatmaps visualise the density or intensity of spatial data by creating a continuous surface from individual point locations. Each point contributes influence to the surrounding area, represented as a gradient that fades with distance.



### Two Methods for Creating Heatmaps

There are two main ways to generate heatmaps in QGIS:

| Method | Location | Characteristics |
|--------|----------|-----------------|
| **Processing Toolbox** | `Processing Toolbox → Interpolation → Heatmap` | Creates a static raster layer that can be saved and reused |
| **Layer Style** | `Layer Properties → Symbology → Heatmap` | Dynamic, but recalculates on every view change (slower with large datasets) |

**References:**
- [QGIS Documentation: Heatmap (Kernel Density Estimation)](https://docs.qgis.org/3.40/en/docs/user_manual/processing_algs/qgis/interpolation.html) — Processing Toolbox method
- [QGIS Documentation: Heatmap Renderer](https://docs.qgis.org/3.40/en/docs/user_manual/working_with_vector/vector_properties.html#heatmap-renderer) — Layer Style method

> **Note:** This tutorial uses the Processing Toolbox method because it is more stable and efficient when preparing graphics.



## Example: Mapping Pharmacy Density

In this example, we visualise the density of pharmacies in South East London using a point layer of pharmacy locations.

![Pharmacies in London](assets/Pharmacies%20in%20London.png)

### Key Parameters

Before generating the heatmap, understand these two critical settings:

- **Radius** – Defines how far the influence of each point spreads. A larger radius produces smoother, more generalised results; a smaller radius highlights local clusters.
- **Resolution** – Determines the size of the raster cells. Higher resolution creates more detail but increases processing time and file size.

### Step-by-Step: Creating the Heatmap

1. Open the **Processing Toolbox** (`Processing → Toolbox` or press `Ctrl+Alt+T`)
2. Search for **Heatmap** and select `Interpolation → Heatmap (Kernel Density Estimation)`
3. Configure the settings:
   - **Input layer:** Select your point layer (e.g., pharmacies)
   - **Radius:** Set an appropriate search radius (e.g., 1000 m)
   - **Pixel size X/Y:** Set the raster cell dimensions in the layer's map units (e.g. 10 × 10 metres when using a projected CRS measured in metres), **not screen pixels**
   - **Output raster:** Choose a filename and location
4. Click **Run**

![Heatmap Settings](assets/Heatmap%20Settings.png)

The result is a raster layer showing density values across the study area:

![Raw Heatmap Output](assets/Raw%20Heatmap.png)

> **Tip:** Start with a lower resolution (larger pixel size) for testing. Increase resolution for finer graphics.



## Improving the Graphics

Once the heatmap is created, there are several ways to improve its visual quality for presentation.

### 1. Editing the Colour Gradient

The simplest improvement is to adjust the colour gradient.

**Steps:**

1. Right-click the heatmap layer and select **Properties**
2. Go to the **Symbology** tab
3. Select **Singleband pseudocolor** as the render type
4. Choose or customise a colour ramp
5. Adjust the **Min/Max** values and **Mode** (e.g., Equal Interval, Quantile)
6. Set transparency for low values to hide areas with minimal density
7. Click **Apply** to preview, then **OK**

![Heatmap Colour Ramp](assets/Heatmap%20Ramp.png)

**Styling tips:**

- Often you see a sequential colour ramp (e.g., white → yellow → red) for density. And often it looks too much. 
- Set the minimum value slightly above zero to create transparency in low-density areas
- Experiment with blending modes. 

### 2. Adding Contours

Contours show lines of equal density and help clarify spatial structure.

**Steps:**

1. Open the **Processing Toolbox**
2. Search for **Contour** and select `Raster extraction → Contour`
3. Configure the settings:
   - **Input layer:** Select your heatmap raster
   - **Interval between contour lines:** Set a value (e.g., 0.0001 depending on your data range)
   - **Output:** Choose a filename
4. Click **Run**

The resulting vector layer can be styled independently:

- Adjust line weight and colour
- Label contour values
- Use different line styles for major/minor intervals

> **Tip:** The Processing Toolbox (`Ctrl+Alt+T`) provides access to all analytical tools including raster extraction, interpolation, and contour generation.

> **Tip:** You can reach the same effect as layer style

![Heatmap Colour Ramp](assets/Contours.png)

### 3. Discrete Sample Points

Instead of relying on the continuous raster surface, sampling values at regular grid points allows more flexible styling and cleaner graphics for publications.

#### Step 1 – Create a Grid

1. Open the **Processing Toolbox**
2. Search for **Create Grid** and select `Vector creation → Create Grid`
3. Configure the settings:
   - **Grid type:** Point
   - **Grid extent:** Match your study area or use layer extent
   - **Horizontal/Vertical spacing:** Set the point interval (e.g., 150 m)
4. Click **Run**

![Create Grid Settings](assets/Greare%20grid.png)

The result is a regular grid of points:

![Resulting Grid](assets/resulting%20Grid.png)

#### Step 2 – Extract Raster Values

1. Open the **Processing Toolbox**
2. Search for **Sample Raster Values** and select `Raster analysis → Sample Raster Values`
3. Configure the settings:
   - **Input layer:** Your grid points
   - **Raster layer:** Your heatmap raster
   - **Output column prefix:** Name for the value column (e.g., "density")
4. Click **Run**

![Sample Raster Values](assets/Sample%20Raster%20Values.png)

Each point now contains the heatmap value at that location:

![Raster with Sample Values](assets/RasterWithSampleValues.png)

#### Step 3 – Style the Points

With values attached to each point, you can create various visualisations:

- **Proportional symbols** – Size points by density value
- **Colour classes** – Categorise points by density ranges
- **Dot density maps** – Filter to show only high-value points

![Dot Map Example](assets/DotMap.png)

For rule-based styling with multiple conditions:

![Rule Based Styling](assets/Rule%20Based.png)

---


## Custom SVG symbols from Rhino and Grasshopper

<img src="assets/Icon.jpg" width="800" alt="Custom SVG map symbols and Truchet tile patterns">

The sampled point grid gives us more freedom than a conventional heatmap. Instead of displaying each value as a coloured dot, we can use **custom vector symbols** to create a spatial pattern. This exercise develops that idea using Rhino, Grasshopper and QGIS. The example draws on *Truchet tiles*: simple geometric elements that form more complex patterns when repeated, rotated or combined.

![Truchet tile pattern](assets/05%20Truchet%20Tiles.png)

The aim is to understand the connection between **data, geometry and representation**. QGIS decides *which* symbol appears at each point; Rhino and Grasshopper determine *what that symbol looks like*.

### 1. Prepare the drawing in Rhino

Open the supplied [Rhino template](assets/SVG%20Template.3dm) and [Grasshopper definition](assets/SVG%20Export%20from%20rhino.gh) in Rhino 8. The definition contains a Python 3 component for exporting curves as SVG.

Work in the **World XY plane**, inside a fixed **100 × 100 drawing area centred on the origin**: X and Y each run from −50 to +50. This square is a construction guide, **not a curve that needs to be exported**. Unlike an exporter that fits every drawing to its bounding box, the fixed canvas preserves the relative size and position of your geometry.

The exporter uses the following conventions:

| Rhino geometry | SVG interpretation |
| --- | --- |
| Open line or curve | Stroke, without fill |
| Closed planar curve | Filled shape with outline |
| Nested closed curves | Transparent opening within a filled shape, using even-odd filling |
| Curved geometry | Polyline approximation in the SVG |

These are **export rules**, not Rhino object types: a closed polyline does not become a hatch in Rhino. It becomes filled because the generated SVG path has a fill property. Polylines should retain their original vertices so corners remain sharp. Smooth curves are approximated, so inspect their appearance at the intended symbol size.

![Grasshopper SVG export definition](assets/01%20Heatmap%20Grasshopper%20SVG%20export.png)

### 2. Export the SVG from Grasshopper

The Python component takes curves, an output file path and an export trigger. Connect the curves you want to export to its **C** input, set that input to **List Access**, and flatten the data if you want all curves in one symbol. Supply a full `.svg` file path and press the button to write the file.

The SVG uses a fixed `viewBox="0 0 100 100"`. Rhino's centre (0, 0) becomes SVG coordinate (50, 50), and the vertical axis is reversed because SVG coordinates increase downwards. **There is no automatic scaling or centring.** A shape occupying 50 units in Rhino occupies half the SVG canvas width.

The export is intended to support QGIS-controlled styling through SVG parameters:

```xml
fill="param(fill) #B7DFF2"
stroke="param(outline) #334155"
stroke-width="param(outline-width) 0.5"
```

The parameter names allow QGIS to control the fill, outline colour and outline width, provided they are present in the exported file. If the stroke-width control is disabled in QGIS, inspect the SVG for a fixed `stroke-width` instead of `param(outline-width)`. The supplied Grasshopper definition is the working starting point; check its exported SVG before assuming all three parameters are available.

### 3. Load the SVG as a QGIS point marker

In QGIS, right-click the sampled point layer and open **Properties → Symbology**. Select a **SVG Marker** symbol layer, browse to your exported file, and adjust its size and colours.

The SVG's **100 × 100 coordinate system does not mean 100 metres on the map**. QGIS determines the displayed marker dimensions. For graphic symbols, millimetres or pixels are often convenient. If the symbol represents an actual distance, choose **Metres at Scale** and verify the result in the map's coordinate reference system.

In particular, a project using **EPSG:3857** may give different results when measured in Cartesian map coordinates versus ellipsoidal ground distance. When checking the marker's width, distinguish between these measurement methods. Also remember that a stroke extends around its path and may slightly affect the visible extent.

### 4. Choose different SVG symbols from point data

The example point layer contains a numeric field called `p_id_count`. We can use this field to assign one of four custom SVG symbols, rather than showing all points identically.

In **Layer Properties → Symbology**, choose **Categorised**. Open the expression editor beside **Value** and enter:

```sql
CASE
  WHEN "p_id_count" IS NULL THEN 'No data'
  WHEN "p_id_count" <= 6 THEN '1 - Low'
  WHEN "p_id_count" <= 31 THEN '2 - Medium'
  WHEN "p_id_count" <= 118 THEN '3 - High'
  ELSE '4 - Very high'
END
```

Click **Classify**, then double-click each category's symbol and choose a different **SVG Marker**. You can use the supplied [OneQuarter.svg](assets/OneQuarter.svg), [TwoQuarter.svg](assets/TwoQuarter.svg), [ThreeQuarter.svg](assets/ThreeQuarter.svg) and [FourQuarter.svg](assets/FourQuarter.svg), or export your own variations.

| `p_id_count` | Category | Suggested symbol |
| --- | --- | --- |
| 0–6 | Low | One-quarter |
| 7–31 | Medium | Two-quarter |
| 32–118 | High | Three-quarter |
| 119 and above | Very high | Four-quarter |

These thresholds are **specific to this example**, not universal density thresholds. Check the distribution of values in your own data before choosing breaks. `NULL` is treated separately from a genuine count of zero.

For more control, you can alternatively use a **data-defined SVG file path** driven by a `CASE` expression. Categorised symbology is easier to understand at first because each symbol and its legend entry remain visible in the layer settings.

### 5. Develop the pattern

![Truchet tile variation](assets/04%20Truchet%20Tiles%20Variation%2001.png)

![Truchet tile variation](assets/06%20Truchet%20Tiles%20Variation%2002.png)

![Additional tile variation](assets/07%20Truchet%20Tiles%20Variation.png)

Once the data selects the symbol, experiment with **rotation, line thickness, spacing and repetition**. A small set of simple SVGs can generate a complex visual field. Compare the outcome with the original heatmap: where does the tile pattern reveal structure, and where does it make the data harder to interpret?

The challenge is not simply to produce an attractive image. Each graphic decision should have a legible relationship to the underlying data. If neighbouring symbols merge into continuous lines or shapes, consider whether that visual continuity communicates something meaningful or merely creates an accidental effect.

**Exercise:** Export four related symbols from Rhino, assign them to the four `p_id_count` classes, and produce two map versions: one emphasising data legibility, the other exploring a more experimental pattern. Include a legend and a short explanation of what the symbols represent.

## Beyond Standard Cartography

The custom SVG exercise demonstrates how a map can move beyond conventional colour ramps and proportional dots. Repetition, rotation and overlapping geometry can create unexpected visual relationships, but they also raise questions about legibility and interpretation. Compare your own results with the graphic references below. Which approaches could help communicate a spatial pattern, and which might obscure it?

Here are a few references for further experimentation:

![Example 1](assets/04c66e51ec2c733b6e975e6b7a764cf4.jpg)

![Example 2](assets/04ec1342e512e354751c62bf782c4360.jpg)

![Example 3](assets/1b14d930c9747850f9f55d7c555e9d98.jpg)

![Example 4](assets/165bcdc1f5bfef7d4967916e948f300d.jpg)





