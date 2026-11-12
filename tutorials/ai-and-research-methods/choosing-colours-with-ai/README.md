# Choosing Colours with AI

*Explore colour combinations, test them in your drawings and build a specialised ChatGPT assistant.*

[RC15 Resources](../../../README.md) · [AI and research methods](../README.md)

**Level:** Beginner  
**Software:** ChatGPT and a drawing application such as Rhino, Illustrator or QGIS  
**You will learn:** How to compare colour strategies, test palettes before applying them and develop a brief for your own colour assistant.

## Why is choosing colour so difficult?

A poor colour combination can ruin an otherwise excellent drawing. Finding colours that work together takes time, experimentation and experience.

Perhaps that is why architectural drawings often rely on familiar, restrained palettes. They are safe, but can also be rather dull.

AI offers an alternative. We can explore combinations quickly, draw on colour theory or historical collections, and compare different approaches before making a decision.

<!-- Illustration pending: same colour against contrasting backgrounds. File: images/01-colour-in-context.png -->

## 1. Where do we find colours?

Start with the purpose of your drawing. A land-use map needs clear distinctions. An architectural illustration might benefit from unexpected colours. A presentation needs a consistent visual identity. The right approach depends on what you want to communicate.

**Colour harmony** is a familiar starting point. Analogous colours sit close together on the colour wheel and tend to feel related. Complementary colours sit opposite each other and offer stronger contrast. Triadic combinations use three separated hues. None guarantees a good drawing, but each gives us a way to begin.

[Adobe Color](https://color.adobe.com/) lets you experiment with these relationships and extract colours from an image. Try sampling an architectural photograph, then adjusting the result into a palette for a drawing.

<!-- Illustration pending: analogous, complementary and triadic colour examples. File: images/02-colour-relationships.png -->

**Mapping data** calls for a different approach. Use categorical colours to distinguish types of things, such as residential and industrial areas. Use a sequential scale, usually progressing from light to dark, for quantities such as density. Use a diverging scale when values sit on either side of a meaningful reference point.

[ColorBrewer](https://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3) is a useful reference. It offers palettes for each purpose, with filters for colour-vision accessibility, printing and photocopying. Compare a few schemes in greyscale: colours that look distinct on screen may become indistinguishable on a poor printer. [Viz Palette](https://projects.susielu.com/viz-palette) can help you check how categorical colours appear under different colour-vision simulations.

Sometimes a project already has colours that must stay. A proposed building might have a distinctive accent, or a landscape drawing might use an established background colour. In that case, **start with those colours** and find supporting shades rather than replacing everything.

Finally, there are **curated collections**: combinations developed through artistic judgement rather than a formula. They are especially useful when you want a drawing to have a particular character. One of our favourites comes from Japan.

## 2. Sanzo Wada: colour beyond the wheel

The Japanese artist **Sanzo Wada** developed hundreds of colour combinations in the early twentieth century. They were later republished in *A Dictionary of Color Combinations*. Some pairings are subtle; others are surprisingly bold.

You can explore them at the free [Dictionary of Color Combinations](https://colorcombinations.org/), which also provides downloadable colour data. Digital HEX values are approximations of the historical printed colours.

<!-- Illustration pending: selected, accurately attributed Wada combinations. File: images/03-wada-combinations.png -->

We have already used Wada's collection to test alternatives for an architectural map. The sea was **pink**, and we wanted to keep it. We tried different colours for buildings and ground, comparing the options before making changes to the drawing.

Some AI suggestions introduced colours outside the selected combination. That included blue, despite our instruction not to use it. The mistake was useful: AI can generate options quickly, but it does not always respect the brief.

<!-- Illustration pending: original Wada map comparisons from September 2026. File: images/04-wada-pink-sea-test.png -->

Try this with your own map. Keep the geometry unchanged, choose one colour to preserve and ask for three palettes using Wada's collection. Compare them at the same scale. Which one brings out the information you care about? Which elements become too prominent?

For example:

> Keep the sea pink. Find a Wada combination that works with it, then suggest three variations for the buildings and ground. Don't introduce colours outside the chosen combination. Show the palette and colour values before I change the drawing.

Notice the order: **explore, compare, then apply**. You do not need to recolour your drawing after every suggestion.

## 3. A ChatGPT colour assistant

We can already make these requests in a normal ChatGPT conversation. But choosing colours is a task we repeat, often with the same requirements. A specialised assistant can make it easier to compare alternatives and retrieve usable colour values.

Our **Colour Palette Assistant** is an example of a custom ChatGPT plugin for this purpose. The idea is simple: describe the drawing, choose an approach, compare palettes and refine individual colours. It should also let us work with colours that must not change.

When designing an assistant of your own, start with a short specification rather than code:

> Help me find colour palettes for architectural drawings, maps and Rhino materials. Offer different approaches, including colour harmony, data palettes and Wada combinations. Show the colours with HEX and RGB values. Respect any colours I ask you to keep. Let me compare alternatives before applying them.

You can test this instruction in ChatGPT first. Building a dedicated plugin adds a more convenient interface, but it also requires deciding what the tool should display and how it should handle revisions.

<!-- @ChatGPT: RC15-Resources\tutorials\ai-and-research-methods\choosing-colours-with-ai\color-palette-assistant

here is the export of the plug in as well as the colors as json files. Obovoly free ti use, but more importantky to adapt and adjust forn your case!

Please explain a bit better how to make usefo these files ... 
-->

<!-- Illustration pending: screenshot of the actual Colour Palette Assistant. File: images/05-colour-plugin-interface.png -->

<!-- Editorial note: add verified steps from the actual plugin project before presenting a build walkthrough. Its source has not yet been inspected. -->

## 4. Colour for materials in Rhino

The same method is useful for materials. Suppose you need a colour for a **slate roof**. Pure black can look flat; a generic grey may not sit well with the rest of the model. Slate can have blue-grey, charcoal and warmer undertones.

Ask ChatGPT for several plausible shades, then compare them in the actual Rhino view:

> Suggest four restrained colours for a slate roof, from blue-grey to warm charcoal. Give me HEX and RGB values. The roof sits above pale stone façades, and the model should look diagrammatic rather than photorealistic.

<!-- Illustration pending: the same Rhino slate roof with four colour variations. File: images/08-rhino-slate-variations.png -->

Keep the camera, lighting and display mode unchanged while testing. A swatch that looks right on a white page may look different on a shaded roof. Colour is only part of a material's appearance; lighting, roughness and reflections matter too.

## 5. Beyond colour: choosing fonts

Finding a good font combination can take just as much experimentation. The approach is similar: explain the purpose, ask for alternatives and compare them in context.

For an architectural submission, you might ask ChatGPT to propose three combinations from [Adobe Fonts](https://fonts.adobe.com/): one for page titles, one for headings and one for body text and captions. Ask it to show the **same sample text** in each hierarchy, including the intended sizes.

A font list is not enough. Look at the combinations on a real page, at the size you intend to print or present. The assistant can speed up the search, but you still need to judge the result.

The wider lesson is simple: AI helps us try more possibilities without committing to every one. That leaves us more time to make the design decisions that matter.

## Further reading

- [Adobe Color](https://color.adobe.com/) — colour harmony and image-based themes
- [ColorBrewer](https://colorbrewer2.org/) — colour schemes for mapping
- [Viz Palette](https://projects.susielu.com/viz-palette) — checking categorical palettes
- [Dictionary of Color Combinations](https://colorcombinations.org/) — Sanzo Wada's historic palettes and downloadable data
- Josef Albers, *Interaction of Color*
- Johannes Itten, *The Art of Color*

---


