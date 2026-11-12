# Four color moods

These are user-facing modes within one color system, not four interchangeable source datasets. Exact reference requests always preserve the source colors. Mood adaptations are explicitly labeled as interpretations or derived colors.

| Mood | Character | Reference and application |
| --- | --- | --- |
| Wada | Expressive, balanced, unexpected combinations | `sanzo-wada-348-color-dictionary.json`; composition and harmony, with plate IDs and original color order retained. Do not automatically desaturate a Wada combination. |
| Al Ula | Warm, earthy, mineral, desert-inspired | `warm-earth-color-palette.json`; the user-confirmed AlUla set, 10 exact colors. Materials, landscape, and regional atmosphere. Preserve the resolved sixth color #ECAC7E. |
| Muted | Soft, restrained, calm | `architectural-palette-reconstructed.json`; the user's Adobe Illustrator / Architectural Palette, 43 fills and 16 lines. Use soft fills for context and layered analysis. Its line colors can remain strong; the mood does not require every color to be pale. |
| Future Systems-inspired | Fresh, bright, optimistic, bold, yet light and precise | A design direction agreed with the user from a Future Systems book cover and an interior spread, not an official or measured color standard. Use for proposals, interventions, concepts, and focal elements. |

Accept aliases: AlUla, Alula, Al Ula; muted, atmospheric, Adobe Illustrator, architectural palette; Future Systems, fresh, bright, optimistic, bold. Preserve Wada plate selection when explicitly requested. Mood adjectives do not override an explicitly selected library or exact HEX value.

## Future Systems-inspired direction

The user supplied a cover of *Future Systems* by Marcus Field, Phaidon, showing a broad lemon-yellow field, fine deep-blue lettering, cool-crimson lettering, and white; an interior spread shows hot-pink carpet and sofa against pale walls and a slender white balustrade. These observations are qualitative, based on reproductions.

Use this starting family:
- Luminous lemon yellow, almost fluorescent in appearance, rather than a muted ochre.
- Hot pink / fuchsia for energetic continuous surfaces.
- Deep cool blue, slightly cyan-leaning, for precise linework or supporting color.
- Cool crimson leaning toward magenta, distinct from hot pink and from orange-red.
- Generous white space, with restrained neutral or dark details as needed.

No canonical HEX values have yet been established for this mood. Do not invent official Future Systems codes or claim to have sampled images that are not available in the current task. For a practical palette request, generate specific HEX/RGB proposals and label them **Proposed — Future Systems-inspired**. For exact source matching, sample an available image and label the results **Sampled approximation**, with provenance; ask for an image if none is available. Newly proposed colors do not become canonical without the user's approval.

Use clear saturated colors selectively. One dominant chromatic color, one supporting color, and ample white often suffice; do not force all four colors into every drawing. A main surface may be intensely colored over a large area. Preserve freshness through white space, fine linework, and clear hierarchy, not by automatically converting bright colors to pastels. Do not impose 60/30/10 ratios. Avoid gratuitous gradients and effects in output previews; the cover's fade is not a requirement for every application.

Assignments such as blue for linework, pink for movement, or yellow for an intervention are proposed graphic roles, not documented Future Systems standards. Check readability for the actual background and line weight; vivid colors are not automatically suitable for text.

## Selection and mixing

Name the selected mood briefly, then proceed without requiring a choice. Keep Muted as the default for an unspecified ordinary architectural drawing; choose Future Systems-inspired when the brief asks for freshness, brightness, optimism, or boldness, unless an explicit palette request takes precedence.

Support mixed requests such as “Future Systems with muted context”: use muted neutrals and soft context fills for existing fabric, then selected vivid colors for proposals or movement. Identify each layer's mood and each color's source or proposed status. Similarly, a Wada combination may be adapted for soft fills and strong lines, but show the original plate separately from derived variants when relevant. Do not silently overwrite stored reference colors.

The legacy `architectural_color_palette.json` remains available for its established names and usage metadata. Ordinary Al Ula requests use the current Warm Earth set; access legacy Al Ula values only when explicitly requested as legacy, identifying differences. Existing filenames and IDs remain unchanged.
