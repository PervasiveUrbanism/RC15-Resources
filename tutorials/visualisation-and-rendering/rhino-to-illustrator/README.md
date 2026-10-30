# From Rhino to Illustrator: working with vector drawings

[RC15 Resources](../../README.md) · [Visualisation and rendering](../visualisation-and-rendering/README.md)

Rhino and Adobe Illustrator are both excellent tools for working with vector geometry, but they have different strengths. Rhino offers precise control over drawing and manipulating curves, including the ability to generate two-dimensional drawings from 3D models using Make2D. Surprisingly, if you come from a CAD background, even relatively simple operations with lines and curves can feel cumbersome in Illustrator. However, Illustrator offers much greater flexibility when it comes to graphic appearance, colours, line weights and visual composition.

Combining the two allows us to take advantage of both applications. Moving geometry from Rhino to Illustrator is straightforward: select the objects and export them as an Adobe Illustrator (`.ai`) file. The challenge begins when we want to continue working on the drawing.

As a project develops, we may need to add geometry in Rhino, remove unwanted lines, update an existing drawing or bring elements back from Illustrator. If each exchange requires manually repositioning, rotating or scaling the artwork, the process quickly becomes frustrating and introduces inaccuracies.

This tutorial introduces a simple workflow for transferring vector drawings between Rhino and Illustrator while **preserving their position, orientation and scale**. By organising the geometry and establishing a consistent reference, we can move between the two applications without having to realign the drawing each time.

**You need:** Rhino and Adobe Illustrator. Start with [Example File Illustrator.3dm](Example%20File%20Illustrator.3dm); the three supplied Illustrator files are references. You can also use the separate [2D Rhino Template (Concept Design)](https://github.com/PervasiveUrbanism/2D-Rhino-Template-Concept-Design), which includes A3 frames, scale factors, layers and drawing styles.

## 1. Establish an A3 reference frame

Before exporting, draw a rectangle in Rhino representing the physical sheet at your chosen drawing scale. This **reference frame** is the basis for every exchange between the two applications: it defines the sheet extent, provides a consistent registration reference and lets you check that the exported geometry is correctly scaled.

An A3 sheet measures **420 × 297 mm**. When the Rhino model is drawn in **metres**, an A3 drawing at 1:1000 covers 420 × 297 metres in model space. At a larger drawing scale, the frame covers a smaller area of the model.

| Intended A3 scale | Frame in Rhino (model units: metres) |
| --- | --- |
| 1:1000 | 420 × 297 m |
| 1:500 | 210 × 148.5 m |
| 1:200 | 84 × 59.4 m |
| 1:100 | 42 × 29.7 m |

You can start with the 420 × 297 m rectangle at 1:1000 and use Rhino's `Scale` command with a factor of **0.5** for 1:500 or **0.2** for 1:200. Equivalently, divide the original dimensions by two or five. The sheet in Illustrator remains A3; only the area of the model represented by that sheet changes.

Use `Rectangle` to create the frame in Rhino's **Top** construction plane and place it on a dedicated layer, such as `REFERENCE FRAME`. Decide on its orientation and position, and keep them fixed. For the first exercise, use a landscape A3 frame and keep all exported geometry in the same Top-plane coordinate system. This is especially important if your starting point is a 3D model: generate the projected curves with `Make2D`, then arrange the resulting 2D geometry within the frame.

The [2D Rhino Template](https://github.com/PervasiveUrbanism/2D-Rhino-Template-Concept-Design) already provides A3 frames and a scale-factor table, alongside a simple layer system. You can use it instead of constructing the setup from scratch.

## 2. Export the drawing at the correct scale

Select **both the geometry and the reference frame** in Rhino, then choose **File → Export Selected** and the **Adobe Illustrator (`.ai`)** format. Including the complete frame in every export is essential: if you export only the changed lines, the bounding box of the file can change and Illustrator may place the new artwork differently.

In Rhino's Illustrator export options, set the model-to-Illustrator scale to match your drawing. The important relationship is between the units on each side, not simply the ratio written on the drawing. For example, for a model in metres at **1:1000**, **1 metre in Rhino must become 1 millimetre in Illustrator**. At 1:500, 1 metre in Rhino becomes 2 mm in Illustrator; at 1:200, it becomes 5 mm.

| Intended scale | Illustrator size of 1 m in Rhino |
| --- | --- |
| 1:1000 | 1 mm |
| 1:500 | 2 mm |
| 1:200 | 5 mm |
| 1:100 | 10 mm |

Rhino's export dialogue may express this relationship using its own unit labels and scale fields. Check the labels rather than entering `1:1000` without considering the model units. The definitive test is the frame: when opened in Illustrator, it must measure **420 × 297 mm**.

Open the exported `.ai` file in Illustrator, select the frame and check its width and height in the **Transform** panel. If they are not 420 and 297 mm, correct the export settings in Rhino and export again. Do not fix the drawing by dragging a corner until it looks approximately right. Once the scale is correct, keep the reference frame in the Illustrator document on a clearly named layer.

## 3. Update the drawing without realigning it

Now make a small change in Rhino: add a few lines, or remove an element from the 2D drawing. Keep the reference frame exactly where it was. Export the updated geometry **together with the same frame**, using the same Illustrator scale settings.

Open the new export in Illustrator. Copy the updated artwork **including its frame** into the original Illustrator document. Align the two frames exactly using Illustrator's alignment controls, with the original frame as the fixed reference. Once the frames coincide, the drawing geometry will also coincide; you do not need to rotate, rescale or visually nudge individual lines. Remove or hide the duplicate frame afterwards.

**Important:** the frame makes exact alignment *possible*, but it does not by itself force Illustrator to paste separate exports at the same coordinates. Do not rely on ordinary paste placement. Use the matching frame as a registration object, and verify the two frames coincide before deleting or replacing old linework. If your Illustrator version and workflow support pasting in place between documents, you can test that as a shortcut, but the frame remains the reliable check.

The same principle applies in reverse when bringing vector geometry from Illustrator back into Rhino: preserve the reference frame, import the Illustrator artwork with consistent units, and check the frame against the existing Rhino rectangle before incorporating the lines. Some Illustrator objects, such as complex appearances or effects, may need to be expanded or simplified before they can be used as Rhino curves.

## 4. Develop the graphic in Illustrator

Once the geometry is correctly positioned, Illustrator is where you can refine the graphic hierarchy. Make the principal outlines stronger, keep secondary lines lighter, and introduce colour or fills where they improve the drawing's clarity. The drawing remains vector-based, so the paths can be edited without the loss of quality associated with raster screenshots.

Keep the frame and the drawing geometry separate from annotations, colours and other graphic elements. This makes it easier to replace one set of Rhino lines without rebuilding the entire Illustrator composition.

## 5. Try it with the supplied files

Open [Example File Illustrator.3dm](Example%20File%20Illustrator.3dm) in Rhino and prepare a 2D projection or drawing within an A3 reference frame. Export it and verify the frame dimensions in Illustrator. Then change the Rhino geometry and repeat the export, using the unchanged frame to register the updated linework.

The folder also contains [Example 01.ai](Example%2001.ai), [LINEWORK.AI](LINEWORK.AI) and [LINEWORK2.AI](LINEWORK2.AI). These are reference files from the original exercise. Their precise graphic content and layer structure have not yet been checked visually, so compare them with your own export rather than assuming they represent consecutive stages.

## If something does not work

| Problem | First thing to check |
| --- | --- |
| The frame is not 420 × 297 mm in Illustrator | Check the Rhino model units and the model-to-Illustrator export scale. |
| Updated geometry appears in a different position | Include the unchanged frame in both exports and align the two frames, not the individual lines. |
| The drawing has rotated | Keep the 2D geometry and frame in the same Top-plane orientation for every export. |
| Some lines are missing | Confirm that the intended Make2D curves are visible and included in Export Selected. |
| The exported drawing contains overlapping lines | Check for duplicate curves or overlapping Make2D results in Rhino. |
| Illustrator graphics do not import cleanly into Rhino | Simplify or expand complex Illustrator appearances and check imported units and frame dimensions. |

---

**Editorial status:** Revised tutorial draft. The A3 frame and scale calculations follow the existing RC15 2D Rhino Template. The precise export dialogue settings, repeated-import behaviour and Illustrator-to-Rhino round trip still require desktop verification and screenshots.
