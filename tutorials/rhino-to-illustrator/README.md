# From Rhino to Illustrator: drawing with vectors

[RC15 Resources](../../README.md) · [Visualisation and rendering](../visualisation-and-rendering/README.md)

A Rhino model is useful for exploring space, but the drawing you want to present may need more control than a viewport screenshot can offer. You might want a particular line-weight hierarchy, selective colour, a carefully composed axonometric or a diagram in which some elements recede while others stand out.

One way to achieve this is to prepare the geometry in Rhino and finish the drawing in Adobe Illustrator. Rhino determines **what is drawn and from which view**; Illustrator lets you decide **how the drawing reads**. Unlike a screenshot, the exported lines remain vectors: they can be selected, recoloured and edited without losing sharpness.

In this exercise, we will work with an existing Rhino model, create a two-dimensional projection with `Make2D`, export the result to Illustrator and develop a simple graphic hierarchy.

**You need:** Rhino and Adobe Illustrator. Download the four example files in this folder. Start with [Example File Illustrator.3dm](Example%20File%20Illustrator.3dm); the three `.ai` files are references for comparing exported and edited linework.

## 1. Start with the drawing, not the export

Open `Example File Illustrator.3dm` in Rhino and inspect the geometry. Switch between Perspective, Top and an axonometric view. Think about what each view communicates: a plan explains spatial arrangement, while an axonometric can reveal relationships between elements at different heights.

Choose a view that makes the model understandable. If you use a parallel projection, the lines do not converge towards vanishing points, which often makes architectural diagrams easier to measure and compare. In Rhino, you can change the active viewport's projection from Perspective to Parallel and then adjust the view.

Before continuing, check which objects and layers are visible. Hide geometry that does not belong in the final drawing. You can always return to the model and generate another projection, so avoid spending time manually deleting unwanted lines after export.

## 2. Make a two-dimensional drawing

Select the geometry you want to project and run:

```text
Make2D
```

Use the **Current View** option if you want to preserve the projection you have just composed. Rhino creates flat curves representing the visible edges of the model, rather than exporting the shaded surfaces themselves. Depending on the options you choose, the result can also contain hidden lines and other curve types.

Keep the resulting curves on identifiable layers. If you include hidden lines, separate them from visible outlines so you can give them a lighter or dashed appearance later. Inspect the result in Top view: the new drawing should be flat, and its geometry should match the chosen projection.

**Why use Make2D?** Exporting the 3D model directly does not give Illustrator the same controlled set of projected curves. Make2D turns the view into linework that can be edited as a conventional vector drawing.

### Add a frame

Draw a rectangle around the projected geometry in Rhino. The original workshop calls this **Make 2D with Frame**: the frame gives the drawing a known boundary that can help with positioning and consistent composition when transferring it between applications.

Place the frame on its own layer. Make it large enough to enclose the entire drawing, but not so large that the geometry appears tiny on the Illustrator artboard. If you prepare several views, use frames of the same dimensions to make them easier to align.

## 3. Export the linework

Select the Make2D curves **and the frame**, then use **File → Export Selected**. Choose **Adobe Illustrator (`.ai`)** as the file type. In the export options, pay attention to the drawing scale and units: the relationship between Rhino model units and Illustrator document units determines the physical size of the exported artwork.

For a diagram, you may choose to adjust the size later in Illustrator. For a scaled architectural drawing, establish the intended scale before export and verify a known dimension after import. Do not assume that an Illustrator artboard automatically represents a particular architectural scale.

Save the export under a new name, leaving the supplied reference files untouched.

## 4. Open the drawing in Illustrator

Open your exported `.ai` file in Illustrator. You should find editable paths rather than a single raster image. Zoom in and select a few lines to confirm that they are individual vector objects.

Compare your export with the supplied files:

- [LINEWORK.AI](LINEWORK.AI) and [LINEWORK2.AI](LINEWORK2.AI) are examples of Illustrator-format linework exported by Rhinoceros.
- [Example 01.ai](Example%2001.ai) is another reference Illustrator document from the original exercise.

The supplied files are useful for comparison, but their exact layer organisation and intended sequence have not yet been verified in Illustrator.

Find the frame and check that the drawing fits inside it. Keep it temporarily while you organise the artwork, then hide or remove it from the final composition if it is not meant to be visible.

## 5. Give the drawing a graphic hierarchy

A Make2D export is a geometric description, not yet a finished drawing. Start by making the main outlines legible. Use a stronger stroke for the elements that define the principal form, a thinner stroke for secondary edges and a lighter treatment for hidden or background information.

Avoid making every line equally dark. In an architectural drawing, line weight can help communicate which surfaces are in front, which elements belong together and what the viewer should notice first.

If your Rhino layers were carried through to Illustrator, use them to organise the changes. Otherwise, select related paths and group them. You can add a restrained colour palette, filled shapes or annotations once the linework reads clearly in black and white.

Work at the size at which the drawing will be presented. A line that looks delicate at 400% zoom may disappear when printed or placed on a presentation board.

## 6. Test the workflow

Return to Rhino and change the view or hide one element. Run Make2D again and export a second drawing. Open it in Illustrator alongside the first.

Compare the two. Which decisions were easier to make in Rhino, and which were easier in Illustrator? Could you have avoided some Illustrator editing by organising the Rhino layers and visibility more carefully?

The aim is to develop a repeatable workflow: **model and projection in Rhino; visual hierarchy and composition in Illustrator**.

## If something does not work

| Problem | What to check |
| --- | --- |
| The export is empty or incomplete | Check that you selected the Make2D curves, not only the original 3D geometry or the frame. |
| The drawing is unexpectedly small or large | Review Rhino model units, Illustrator export scale and the dimensions of the frame. |
| Lines overlap or look too heavy | Inspect duplicate curves and overlapping visible/hidden linework before adjusting strokes. |
| The drawing is difficult to edit | Check whether the imported objects are grouped or nested, and whether paths can be selected individually. |
| Hidden lines appear as solid outlines | Keep hidden curves separate and apply their dash or colour treatment explicitly. |
| A different view is exported | Confirm the active viewport and the Make2D projection option before generating the drawing. |

---

**Editorial status:** First draft, based on the original workshop outline and the supplied files. The Rhino file is confirmed as a Rhino 7 model, and the `LINEWORK` Illustrator files identify Rhinoceros as their creator. The exact geometry, layer structure, Illustrator appearance and application-specific export settings still need visual verification. Screenshots and a final illustrated result should be added after reviewing the exercise in Rhino and Illustrator.
