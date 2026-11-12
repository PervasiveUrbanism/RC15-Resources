# Color Palette Assistant — complete export

Version: 0.6.4. Exported: 12 November 2026.

## Contents

- `original-plugin/`: every published plugin file, unchanged, including the icon, manifests, instructions, lookup index and references. This is the authoritative backup.
- `ORIGINAL-INSTRUCTIONS.txt`: the original skill text in a convenient text file.
- `portable/`: four palette JSON files, the four-mood guide, and combined instructions adapted for uploaded-file access.
- `CHECKSUMS.json`: SHA-256 hashes for checking the export.

The four JSON libraries are the current Muted architectural palette (43 fills and 16 lines), Wada (348 combinations), current Al Ula / Warm Earth (10 colors), and the preserved legacy architectural/Al Ula reference. Future Systems-inspired is described in the mood guide, not a fourth verified HEX palette. The source images discussed in chat are not packaged in the plugin and are not included here.

## Using this in Claude

1. Unzip the download and create or open a Claude Project.
2. Copy `portable/COLOR-PALETTE-INSTRUCTIONS.txt` into the project's instructions. If the interface cannot accept the full text, upload that text file as knowledge and use this short instruction: “Follow COLOR-PALETTE-INSTRUCTIONS.txt and color-moods.md. Consult the uploaded JSON files before quoting reference colors. Clearly label proposed, derived, and sampled colors.”
3. Upload all four JSON files and `color-moods.md` from `portable/` to the project's files/knowledge.
4. Start a conversation and try the checks below. This is a manual content port, not a one-click installation of the Codex plugin. Responses in Claude have not been tested.

Official guidance checked for this export:
- https://support.claude.com/en/articles/8241126-upload-files-to-claude
- https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects

## Quick checks and tutorial prompts

- “List my four color moods.” Expected: Wada, Al Ula, Muted, Future Systems-inspired.
- “Show Wada combination 001.” Expected: English Red #D96629 / RGB(217,102,41), Cerulian Blue #0093A5 / RGB(0,147,165), in that order.
- “Show color 6 from my current Al Ula palette.” Expected: #ECAC7E / RGB(236,172,126), with the printed-label discrepancy retained if discussed.
- “Create a Future Systems-inspired proposal with muted context.” Expected: vivid proposed colors, generous white space, subdued context; no claim that proposed HEX codes are official Future Systems colors.

## Sharing and attribution

Keep the Wada dictionary's source attribution, license URL and provenance when sharing. Its website metadata is attributed to colorcombinations.org under CC BY 4.0; the upstream dataset is identified in the JSON. No blanket license is assigned by this export to other materials or the plugin icon. The full backup retains Vincent Nowak as the plugin author. This export does not change the installed plugin or publish it to others.
