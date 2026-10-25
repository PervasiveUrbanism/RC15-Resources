# Initial transfer notes

The existing repository tree was inspected before import: no Sentiment Landscapes project was present. All 68 eligible source files (359,646,369 bytes) were copied without edits, preserving their relative paths. Seven files above 100 MB were omitted. Source-internal duplicates were intentionally retained.

## QGIS source paths

Inspection of the QGZ project found relative references to the included CentrHeron CSV files, CornerPts, CountBy200Grid, CountBy200GridPT, Grid100m and Grid200m GeoPackages, and `../london_photos.csv`. It also references the omitted `./PhotoPTS.gpkg` and `./FlickrImages.sqlite`; restore those from Drive if required.

An absolute path to `BBox.gpkg` under the original author's Dropbox portfolio directory is embedded in the project. That file is absent from the supplied Drive folder and is not included here. Locate a suitable original and relink it if that layer is required.

A remote Mapbox WMTS layer and its original public access token are embedded in the unchanged project. Availability and access were not tested; configure your own authorised basemap if necessary. No credentials are copied into these notes.

Grasshopper definitions are preserved as supplied; paths and plug-in requirements have not been execution-tested. Illustrator linked-asset resolution also remains to be checked in the application.

## Verification boundary

The transfer manifest records Drive metadata sizes, source links and SHA-256 checksums of the downloaded files. All downloads matched Drive sizes. Git blob hashes are compared with the remote committed tree after upload. These integrity checks do not establish application compatibility or validate data licences. Tutorial review and polishing remain separate.
