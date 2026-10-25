# Files not transferred — where to find them

All seven files below remain in the [original Sentiment Landscapes folder on Google Drive](https://drive.google.com/drive/folders/1Vne2oIm3IZLKmHETGs8oMA8x86V2IqWA). They were excluded because each exceeds 100 MB. Nothing was deleted from Drive.

Restore paths are relative to this project folder, now `tutorials/mapping-and-spatial-analysis/sentiment-landscapes/`. The original Drive folder is still named `Sentiment Landscapes`. Open a file's Drive link to download it, then place it at the listed path if needed.

| File / restore path | Approximate size | Where to look | When needed |
| --- | ---: | --- | --- |
| `assets/greater-london-latest.osm/greater-london-latest.osm` | 1.96 GB | [Drive file](https://drive.google.com/file/d/1IWMFh_kUqE9BoWqdaKF1b746MAgYjLSs/view) | Original full London OSM input; no external replacement URL verified. |
| `assets/greater-london-latest.osm.pbf` | 112.6 MB | [Drive file](https://drive.google.com/file/d/1X8aBtxc52SNWSXWUzFbI-niD3dgIaTko/view) | Compressed London OSM input. |
| `Rhino/assets/large.osm` | 141.0 MB | [Drive file](https://drive.google.com/file/d/13yCud08c6-Ul2xng_1u2dgtiEfclG9GB/view) | Original larger OSM context for Rhino. |
| `Qgis/FlickrImages.sqlite` | 245.3 MB | [Drive file](https://drive.google.com/file/d/1B6Tt1XXuQoTQBqKMNdaq1pd5nS7cILyl/view) | Original photo database referenced by the QGIS project. |
| `Qgis/PhotoPTS.gpkg` | 174.9 MB | [Drive file](https://drive.google.com/file/d/1aXWNjdYsIX8YJsLo84TNNKk5YG5ztaEZ/view) | Original photo-point layer referenced by the QGIS project. |
| `Rhino/Heron.3dm` | 480.9 MB | [Drive file](https://drive.google.com/file/d/1K4rqx5xuuKpZ0KahsIEO455y4-jl5weX/view) | Optional original model. For the tutorial's visual reference, use the [existing view capture](Images/ViewCapture20250712_174129.png). |
| `Rhino/Heron.3dmbak` | 469.7 MB | [Drive file](https://drive.google.com/file/d/1airGamHQJt_2p3F1jPsS5Cv2Pnp9k5or/view) | Backup only; unnecessary for the tutorial. |

Sizes use decimal MB/GB. Exact byte sizes are in [TRANSFER-MANIFEST.csv](TRANSFER-MANIFEST.csv).

## Other missing or external references

- **`BBox.gpkg`**: referenced by the QGIS project at an old Dropbox portfolio path, but absent from the supplied Drive folder. Its location is unknown. Use the included grid extent for the draft exercises, or locate the original separately.
- **Mapbox basemap**: the QGIS project references an external service. Availability is untested; supply your own authorised basemap if needed.
- **Original computer paths**: `Heron.gh` points to `CentrHeron3.csv` on an old drive and to an old local asset folder. Relink these to the transferred `Qgis/CentrHeron3.csv` and `Rhino/assets/` folders.

You can begin the [tutorial](TUTORIAL.md) using the included grid, centroid CSV and images, without downloading all the large dependencies.
