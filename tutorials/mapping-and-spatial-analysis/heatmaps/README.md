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
   - **Pixel size X/Y:** Set the resolution (e.g., 10 × 10 px for testing)
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

## Beyond Standard Cartography

At this point, you can see where this is heading. The next steps would involve exploring different geometries, possibly overlapping different symbols so that they form new patterns. QGIS extends this further by offering the use of .svg symbols—custom graphics that you can create in Illustrator and bring into QGIS. From here, there is quite a lot of ground to explore.

By leaving off-the-shelf visualisation behind, we move beyond conventional map representation into more sophisticated territory, exploring different, more artistic types of graphics.

Here are a few examples:

![Example 1](assets/04c66e51ec2c733b6e975e6b7a764cf4.jpg)

![Example 2](assets/04ec1342e512e354751c62bf782c4360.jpg)

![Example 3](assets/1b14d930c9747850f9f55d7c555e9d98.jpg)

![Example 4](assets/165bcdc1f5bfef7d4967916e948f300d.jpg)





