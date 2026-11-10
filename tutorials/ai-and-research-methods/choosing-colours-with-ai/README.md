# Choosing Colours with AI

*Exploring colour, building a ChatGPT assistant and testing ideas before changing a drawing*

[RC15 Resources](https://github.com/PervasiveUrbanism/RC15-Resources) · AI and research methods

**Level:** Beginner  
**You need:** ChatGPT and a drawing application such as Rhino, Illustrator or QGIS  
**Outcome:** A tested colour palette for a drawing, a family of diagrammatic Rhino materials and a simple specification for a colour assistant.

## Why do colours take so long to get right?

Choosing one colour is easy. Choosing six that work together is not. A building might look clear against a white background but disappear once the streets and landscape are coloured. A promising set of swatches can turn into a confusing map.

Designers have always relied on colour references, samples and repeated tests. AI makes the exploration quicker. We can ask for several alternatives, preserve colours we already like and adjust individual shades without having to start again. But the assistant cannot know whether a palette communicates our intention until we test it in the actual drawing.

<!-- Illustration pending: One colour seen against contrasting backgrounds. Expected file: images/01-colour-in-context.png -->

*Illustration to add: the same swatch against two different backgrounds.*

## 1. Start with the purpose

Before asking for colours, decide what they need to do. An urban map might need to distinguish different land uses. An architectural diagram might need to emphasise the proposed building while keeping the context quiet. A Rhino model might use deliberately abstract material colours to establish a coherent atmosphere.

Different purposes call for different approaches.

| Approach | What it does | Try it for |
| --- | --- | --- |
| **Colour relationships** | Uses related or contrasting hues, such as analogous and complementary colours | Diagrams and graphic identities |
| **Curated combinations** | Starts with a palette someone has carefully composed | Illustrations, publications and conceptual work |
| **Data palettes** | Uses categorical, sequential or diverging scales to represent information | Land use, density and environmental maps |
| **Contextual palettes** | Builds around colours or materials already present in a project | Existing/proposed drawings and Rhino materials |

A little vocabulary helps. **RGB** records red, green and blue values for screen colour. **HEX** is a compact way of writing an RGB colour, such as `#A9B2A7`. **HSL** describes hue, saturation and lightness, making it useful when we want to ask for something warmer, lighter or less saturated. These are ways to describe colours; they do not tell us which combinations work best.

<!-- Illustration pending: Analogous, complementary and triadic colour examples. Expected file: images/02-colour-relationships.png -->

## 2. An alternative to colour wheels: Sanzo Wada

The Japanese artist and colour researcher **Sanzo Wada** assembled hundreds of combinations in the early twentieth century, later republished in *A Dictionary of Color Combinations*. His palettes are a useful reminder that selecting colours is not only about rules. An unexpected combination can give a drawing a distinct character.

Explore the free [Dictionary of Color Combinations](https://colorcombinations.org/). Its [downloadable data](https://colorcombinations.org/data/) makes the historical combinations available as HEX values. The digital colours are approximations of printed originals, not exact measurements of old inks.

<!-- Illustration pending: A selection of Sanzo Wada's historic combinations. Expected file: images/03-wada-combinations.png -->

*Illustration to add: a few accurately sourced combinations, redrawn with attribution.*

### A real colour test: keep the pink sea

In an earlier colour experiment, we used Wada's combinations to reconsider the colours in an architectural map. **The sea was already pink, and that colour needed to stay.** The problem was the colours of the buildings and other elements around it.

We explored further combinations, but some suggestions introduced colours that were not part of the selected reference. At one point, blue appeared even though the instruction was to stay strictly within the chosen palette. This is a revealing AI failure: the new colours might be attractive, but the assistant has ignored the design brief.

The better workflow was to fix the sea colour first, find compatible Wada combinations and change only the remaining categories. More options were useful, but only when they respected the constraint.

<!-- Illustration pending: Original map and Wada colour variations with the pink sea preserved. Expected file: images/04-wada-pink-sea-test.png -->

*Image needed: recover the original September 2026 map tests. Do not reconstruct the palette or invent its exact HEX values. Show the initial scheme, an unsuitable alternative and a corrected one if those images are available.*

You can use the same idea in your own work:

> I already have a pink sea and want to keep its exact colour. Find Wada combinations that work with it. Suggest alternatives for buildings, ground and connections, but don't introduce colours outside the chosen combination. Show me the options before I change the drawing.

This is more helpful than simply asking AI to “make my map look better”.

## 3. Make your own ChatGPT colour assistant

We often repeat the same kind of conversation: choose a palette, request HEX values, compare alternatives, then ask for a warmer or quieter version. A small specialised assistant can make this process more convenient.

The RC15 example is a custom ChatGPT **Colour Palette Assistant**. It explores several visual directions, including Wada combinations, and supports architectural uses such as plans, diagrams and material palettes. The exact plugin-building steps still need to be documented from the working version, rather than guessed.

Start by describing what your own assistant should do:

> Help me choose colours for architecture and urban design. Ask what the colours represent and whether I am designing for a screen, a printed page or a Rhino model. Offer distinct approaches, show named swatches with HEX and RGB values, and explain the differences. Let me lock colours that must not change. Check each revision against my constraints.

Even in a normal ChatGPT conversation, this gives you a useful starting point. The advantage of a dedicated plugin is a more focused, repeatable workflow and an interface for comparing colours.

<!-- Illustration pending: Screenshot of the existing Colour Palette Assistant. Expected file: images/05-colour-plugin-interface.png -->

*Screenshot needed: use the actual plugin interface and verify its construction steps before publishing instructions.*

## 4. Exercise: compare three versions of an urban map

Choose a map with buildings, streets, landscape and one important feature you want to emphasise. Keep the geometry, line weights and legend fixed. We want to see what changing **only the colours** achieves.

<!-- Illustration pending: Reference urban map before colour testing. Expected file: images/06-urban-map-original.png -->

Ask the assistant for three directions: a restrained analytical palette, a Wada-based combination and a contextual architectural palette. Give it the precise categories and tell it which existing colours must remain unchanged.

> Here is my urban map. Existing buildings should be quiet; the proposal should stand out. Suggest three different palettes, with HEX values for every category. Keep the geometry and colour assignments consistent so I can compare them fairly. Don't apply changes yet.

<!-- Illustration pending: Three colour variations of the same urban map. Expected file: images/07-urban-map-three-tests.png -->

Compare the results at the same scale. What do you notice first? Do streets compete with the proposal? Do neighbouring categories remain distinct? Try looking at the maps in greyscale, and check important differences for colour-vision accessibility. A pleasing palette is not necessarily a legible one.

Choose the strongest option and refine **one colour at a time**. Record the final values before applying them to the original drawing.

## 5. Exercise: abstract material colours in Rhino

Colour is also useful when nothing is being measured or classified. For a diagrammatic Rhino view, you may want concrete to feel like concrete without making every surface neutral grey. A little green, sand, blue or rose in the material colour can give a model a more deliberate visual identity.

Try asking:

> Suggest four muted concrete colours for a diagrammatic Rhino model: warm, green-grey, blue-grey and rose-grey. Keep them fairly close in lightness. Add compatible colours for paving and painted metal, and give me HEX and RGB values.

<!-- Illustration pending: One Rhino model with four abstract concrete palettes. Expected file: images/08-rhino-concrete-variations.png -->

Test the alternatives using the **same camera, lighting and display mode**. Material appearance depends on reflections, roughness and illumination as well as the colour value. Adjust the palette while looking at the actual model, not only the swatches.

## 6. What can go wrong?

AI is good at suggesting options, but it may forget constraints, change colours you wanted to preserve, introduce too many strong accents or recommend a palette that only looks good as swatches. A Wada combination may have a beautiful mood and still be unsuitable for a data map.

Keep a record of the values you accept. Tell the assistant explicitly which colours are locked. Compare alternatives in context before making changes. For printed work, check a proof: RGB colours on screen do not necessarily match the printed result.

The same method also works for typography. A **font assistant** could help compare Adobe Fonts for headings, body text and captions, then show them in the same sample layout. The point is not to let AI make the final choice. It is to make comparison and iteration easier, so we can spend more time deciding what communicates well.

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
- [ ] Capture illustrations using the eight filenames given above.
- [ ] Test the map and Rhino exercises on real source material.
- [ ] Create a round tutorial icon to replace the text-only navigation entry.
