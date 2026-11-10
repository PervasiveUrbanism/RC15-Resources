# Choosing Colours with AI

*Exploring colour, building a ChatGPT assistant and testing ideas before changing a drawing*

[RC15 Resources](https://github.com/PervasiveUrbanism/RC15-Resources) · AI and research methods

**Level:** Beginner  
**You need:** ChatGPT and a drawing application such as Rhino, Illustrator or QGIS  
**Outcome:** A tested colour palette for a drawing, a family of diagrammatic Rhino materials and a simple specification for a colour assistant.

## Why do colours take so long to get right?

Choosing one colour is easy. Choosing six that work together is not. A building might look clear against a white background but disappear once the streets and landscape are coloured. A promising set of swatches can turn into a confusing map.

Finding the right combination can take hours of trial and error. It takes experience, too: a poor colour decision can undermine an otherwise convincing drawing. That risk often encourages us to stay with safe, restrained palettes. AI offers a way to explore more adventurous alternatives quickly, without committing to them before we have seen how they work.

<!-- Illustration pending: One colour seen against contrasting backgrounds. Expected file: images/01-colour-in-context.png -->

*Illustration to add: the same swatch against two different backgrounds.*

## 1. Different ways of choosing colours

Start with the story. What should the viewer notice first? Is colour describing data, distinguishing the proposal from its surroundings, or creating an atmosphere? The answer helps determine the strategy. An unusual combination can be expressive in an illustration but confusing in a land-use map. Conversely, a perfectly safe palette may make an architectural presentation rather dull.

### Colour harmony: building a coherent family

A colour wheel offers familiar starting points. **Analogous** colours sit near one another and can give a composition a calm, unified character. **Complementary** colours sit opposite each other and create strong contrast; a small complementary accent might help distinguish an intervention from its context. **Triadic** combinations use three separated hues, offering variety but requiring care so that everything does not compete for attention.

Try [Adobe Color](https://color.adobe.com/), where you can explore harmony rules, adjust individual colours and extract a theme from an image. For example, sample a photograph of weathered brick and greenery, then test whether those colours make a convincing graphic language for your drawings. An extracted palette is a starting point, not a design decision.

<!-- Illustration pending: Analogous, complementary and triadic colour examples. Expected file: images/02-colour-relationships.png -->

### Colour for information: helping people read maps

When colour represents data, it has to communicate a precise relationship. A **categorical** palette distinguishes things without suggesting an order, such as residential, industrial and civic land uses. A **sequential** palette moves from light to dark for quantities such as density or building height. A **diverging** palette separates values on either side of a meaningful midpoint, such as temperature differences above and below an average.

[ColorBrewer](https://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3) is particularly helpful here. Select the number of classes, then try its **colourblind safe**, **print friendly** and **photocopy safe** filters. The three-class blue-green scheme is a useful demonstration of ordered differences, but do not assume every palette passes every filter: verify the specific scheme. Test it in greyscale and on an ordinary printer. Different hues alone may disappear; differences in lightness often survive.

For an additional check, [Viz Palette](https://projects.susielu.com/viz-palette) previews colour sets under simulations of colour-vision deficiencies. It is useful when you need several categories to remain distinguishable.

### Contextual colour: working with what is already there

Sometimes you are not free to start from scratch. A project may already have a pale drawing background, a dominant building material or a colour that identifies an intervention. Treat those as fixed anchors and search for compatible supporting colours. The result may deliberately be restrained, with a single accent carrying the most important information.

### Curated combinations: looking beyond the expected

Not every palette has to be derived from a wheel or a data scale. Historical colour collections offer combinations that have already been carefully considered. They can be especially useful for architectural illustrations, publications and drawings where visual character matters. Sanzo Wada's collection, which we explore next, is a good example.

Whatever the approach, keep a record of your final values. **HEX** is a compact way to specify screen colours, such as `#A9B2A7`; **RGB** lists their red, green and blue components. **HSL** describes hue, saturation and lightness, useful when asking for a colour to be slightly warmer, quieter or lighter. These describe colours; they do not judge whether a combination is suitable.

## 2. An alternative to colour wheels: Sanzo Wada

The Japanese artist and colour researcher **Sanzo Wada** assembled hundreds of combinations in the early twentieth century, later republished in *A Dictionary of Color Combinations*. His palettes are a useful reminder that selecting colours is not only about rules. An unexpected combination can give a drawing a distinct character.

Explore the free [Dictionary of Color Combinations](https://colorcombinations.org/). Its [downloadable data](https://colorcombinations.org/data/) makes the historical combinations available as HEX values. The digital colours are approximations of printed originals, not exact measurements of old inks.

<!-- Illustration pending: A selection of Sanzo Wada's historic combinations. Expected file: images/03-wada-combinations.png -->

*Illustration to add: a few accurately sourced combinations, redrawn with attribution.*

### A colour test before committing

In an earlier experiment, we tested Wada combinations on an architectural map while preserving its **pink sea**. Several alternatives were explored for the buildings and ground. Some looked promising, but others introduced colours outside the chosen palette, including blue. This made the exercise useful: AI can show options quickly, yet still fail to respect a simple constraint.

<!-- Illustration pending: Original map and Wada colour variations with the pink sea preserved. Expected file: images/04-wada-pink-sea-test.png -->

*Add the original September 2026 comparison images here when recovered. The images and exact HEX values are not currently available; do not invent them.*

Try the same approach with a map of your own. Keep the geometry and legend unchanged, specify any fixed colours, and ask for three distinct palettes. Compare them side by side **before** applying one. Which option gives the intended hierarchy? Does the background compete with the subject? Can you still understand it in greyscale?

> Keep the sea exactly as it is. Using the selected Wada combination, suggest three variations for the buildings and ground. Do not add colours outside that combination. Show the colours and their HEX values first; do not edit the drawing.

The goal is not to get AI to approve a palette, but to use it to broaden the possibilities and then make a considered choice.

## 3. Make your own ChatGPT colour assistant

We often repeat the same kind of conversation: choose a palette, request HEX values, compare alternatives, then ask for a warmer or quieter version. A small specialised assistant can make this process more convenient.

The RC15 example is a custom ChatGPT **Colour Palette Assistant**. It explores several visual directions, including Wada combinations, and supports architectural uses such as plans, diagrams and material palettes. The exact plugin-building steps still need to be documented from the working version, rather than guessed.

Start by describing what your own assistant should do:

> Help me choose colours for architecture and urban design. Ask what the colours represent and whether I am designing for a screen, a printed page or a Rhino model. Offer distinct approaches, show named swatches with HEX and RGB values, and explain the differences. Let me lock colours that must not change. Check each revision against my constraints.

Even in a normal ChatGPT conversation, this gives you a useful starting point. The advantage of a dedicated plugin is a more focused, repeatable workflow and an interface for comparing colours.

<!-- Illustration pending: Screenshot of the existing Colour Palette Assistant. Expected file: images/05-colour-plugin-interface.png -->

*Screenshot needed: use the actual plugin interface and verify its construction steps before publishing instructions.*

## 4. Choosing material colours in Rhino

Colour also matters when choosing materials in Rhino. Suppose you need a convincing colour for a **slate roof** in a diagrammatic model. Pure black makes the roof look flat; a neutral mid-grey can feel lifeless. Real slate varies, with cool blue-grey, warmer charcoal and sometimes subtle green or violet undertones. We can compare these directions without trying to reproduce every physical detail.

> I need a colour for a slate roof in Rhino. Give me four plausible, restrained alternatives, from blue-grey to warm charcoal, with HEX and RGB values. Keep them suitable for a diagrammatic architectural view and suggest which works best with pale stone façades.

<!-- Illustration pending: Slate roof material colour comparisons in Rhino. Expected file: images/08-rhino-slate-variations.png -->

Apply the colours to the **same model**, keeping camera, lighting and display mode fixed. The best swatch may not be the best-looking roof. Lighting, reflectivity and roughness affect how the colour appears, so refine it in context.

## 5. Beyond colour: choosing fonts

The same workflow can help with typography. Instead of asking for a “nice font”, tell ChatGPT what the publication is for, what tone you want and which fonts are available to you. For example, ask it to compare three **Adobe Fonts** combinations for an architectural submission: one font for page titles, one for chapter headings and one for body text and captions.

Ask for a sample hierarchy with actual text, rather than just a list of font names. Compare the combinations on the same page. Do the headings establish a clear order? Is the body text comfortable to read? Are the captions still legible at print size? As with colour, the assistant helps narrow the search, but the decision is made by looking at the result.

## References

- [The Dictionary of Color Combinations](https://colorcombinations.org/)
- [Wada colour data and reuse conditions](https://colorcombinations.org/data/) (CC BY 4.0; attribution required)
- Josef Albers, *Interaction of Color*
- Johannes Itten, *The Art of Color*
- [W3C guidance on text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)

---

### Editorial notes — remove before publication

- [ ] Recover the original **27 September 2026** pink-sea Wada tests, including original images and exact palette/HEX values where available. The conversation establishes the constraints, but not the full source image or colour table.
- [ ] Inspect the actual Colour Palette Assistant and explain its real creation process.
- [ ] Capture the remaining illustrations; update the slate material image filename to `images/08-rhino-slate-variations.png`.
- [ ] Test the Wada comparison and slate material exercise on real source material.
- [ ] Create a round tutorial icon to replace the text-only navigation entry.
