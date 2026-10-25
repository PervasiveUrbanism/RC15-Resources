# 2. Collecting Flickr Data in QGIS

[← Chapter 1: From Points to Landscapes](01-introduction.md) · [Sentiment Landscapes overview](README.md)

In the introduction, we discussed how thousands of overlapping geographical points can be transformed into a landscape. Our first practical task is to obtain those points.

We will use **Flickr**, a photography platform where some public photographs have geographic coordinates. With a QGIS plugin, we can collect their metadata for a chosen area and store the results as a spatial database. We are collecting **information about photographs**, not downloading an archive of full-resolution photographs.

At the end of this chapter you should have a QGIS project and a **SpatiaLite database** containing geolocated photograph records. In the next chapter we will divide the same area into a grid and count the photographs in each cell.

> **Compatibility note (October 2026):** The steps below follow the [Flickr Metadata Downloader project instructions](https://github.com/samanbey/flickrdl), the [QGIS plugin listing](https://plugins.qgis.org/plugins/flickrdl/) and QGIS documentation. The plugin's published experimental version is 0.8 (16 January 2026), listed for QGIS 3.x. This workflow has **not yet been tested in a live QGIS installation** for this tutorial. If the interface differs, record the version and the precise step that fails so the instructions can be corrected.

## 2.1 Prepare a working folder

Create a folder on your computer for this exercise. For example:

```text
Sentiment-Landscapes/
├── Sentiment-Landscapes.qgz
└── data/
    └── flickr_photos.sqlite
```

The `.qgz` project and the `.sqlite` database will be created in the following steps. Keeping them together makes it easier to move the project to another computer and reduces broken file paths.

Open **QGIS 3**, create a new project and save it as `Sentiment-Landscapes.qgz` in your working folder. The accompanying archive in this repository contains an older example project, but we will build our own rather than simply opening the finished result.

## 2.2 Install Flickr Metadata Downloader

QGIS supports additional tools called **plugins**. We will use the community-maintained [Flickr Metadata Downloader](https://plugins.qgis.org/plugins/flickrdl/), which searches Flickr for publicly available, geotagged photographs within a rectangular geographic boundary and stores metadata in a SpatiaLite database.

1. In QGIS, open **Plugins → Manage and Install Plugins…**.
2. Under **Settings**, enable the option to show **experimental plugins**. The current version of Flickr Metadata Downloader is listed as experimental.
3. Search for **Flickr Metadata Downloader** in the plugin manager.
4. Install and enable it. Look for its command under the **Web** menu, as described by the plugin author.

If it does not appear in the plugin manager, consult the [plugin's installation instructions](https://github.com/samanbey/flickrdl) and check whether your QGIS version is supported. The project's documentation also describes a manual installation route, but try the QGIS plugin manager first.

**Checkpoint:** you can find the Flickr Metadata Downloader command in QGIS. Do not proceed with a missing or disabled plugin.

## 2.3 Get a Flickr API key

An **Application Programming Interface (API)** allows one program to request information from another service. Here, the QGIS plugin sends a geographical search request to Flickr and receives information about matching photographs.

Flickr requires an **API key** to identify the application making requests. You do not need to write code to use this key with the plugin.

1. Create or sign in to a Flickr account at [flickr.com](https://www.flickr.com/).
2. Open the [Flickr API key application page](https://www.flickr.com/services/api/misc.api_keys.html).
3. Follow the application process and describe your intended **non-commercial educational use** accurately. Approval and access are controlled by Flickr.
4. Keep the issued API key available for the next step.

Flickr may also provide an API *secret*. The plugin documentation asks for an API key; do not enter the secret unless an explicitly documented field requires it.

**Keep credentials private.** Do not put your API key or secret into a public GitHub repository, screenshots, shared project files or tutorial submissions. If Flickr changes its approval process, follow its current guidance rather than assuming a key will be issued immediately.

References: [Flickr API keys](https://www.flickr.com/services/api/misc.api_keys.html) and [Flickr developer guide](https://www.flickr.com/services/developer/api/).

## 2.4 Define the area of interest

Our **area of interest (AOI)** is the part of the city we want to investigate. Start with a manageable part of London rather than the whole city. A smaller area is useful for testing the connection and checking the resulting dataset.

The plugin defines its search using a **bounding box**: a rectangle described by its southern, northern, western and eastern boundaries. The values are geographic coordinates in decimal degrees.

- **West / east** refer to **longitude**.
- **South / north** refer to **latitude**.
- West must be smaller than east, and south smaller than north.

Use QGIS to identify the approximate coordinates of your chosen rectangle and check that it covers the intended neighbourhood. Record the bounds you use: you will need them to understand and reproduce your results later.

**Checkpoint:** you can explain which part of London your four boundaries describe. A bounding box is not necessarily the same as an administrative neighbourhood boundary; we will work with the rectangle for this exercise.

## 2.5 Create an empty SpatiaLite database

Flickr Metadata Downloader stores its results in **SpatiaLite**, a spatial extension of the SQLite database format. A database can contain tables of records and geographic geometries in one file. QGIS can open these directly as map layers.

The plugin expects a SpatiaLite database to exist **before** starting the download. Simply creating an empty text file with the extension `.sqlite` will not initialise the required spatial database.

1. In QGIS, open the **Browser** panel. If it is hidden, enable it through **View → Panels → Browser**.
2. Find the **SpatiaLite** entry in the Browser.
3. Right-click and select **Create Database**.
4. Save a new database as `data/flickr_photos.sqlite` inside your working folder.
5. If necessary, right-click **SpatiaLite** again and use **New Connection** to register the database with QGIS.

You should now see the database in the Browser, even though it does not contain any downloaded photographs yet. You **do not need to create the Flickr photograph table manually**; the plugin creates its result table when it runs.

The database creation procedure is documented in the [QGIS SpatiaLite training manual](https://docs.qgis.org/3.44/en/docs/training_manual/databases/spatialite.html).

**Checkpoint:** the `flickr_photos.sqlite` file exists in your project folder and QGIS recognises it as a SpatiaLite database.

## 2.6 Download the photograph locations

Now open **Web → Flickr Metadata Downloader**. The plugin author's published workflow is:

1. Select the SpatiaLite database you created: `data/flickr_photos.sqlite`.
2. Enter your Flickr API key.
3. Enter a name for the results table if prompted, for example `flickr_london`.
4. Enter the bounding coordinates of your area of interest, paying attention to latitude versus longitude.
5. Press **Start** to download the public photograph metadata.

The plugin writes a new SpatiaLite table containing geographic point locations and attributes. According to its documentation, these include coordinates, user IDs, dates, tags and a small-thumbnail URL. The precise fields available can depend on the plugin version and returned records.

Allow the request to complete. For a first attempt, use a small area and check whether the table is created before trying a much larger search. API availability, service limits and how complete the returned records are may affect the result.

**Checkpoint:** the new table appears in your SpatiaLite database, and you can add it as a point layer in QGIS.

## 2.7 Explore what you collected

Add the new photo layer to the QGIS map if it has not been added automatically. Zoom to its extent and open its **Attribute Table**.

Look at how the data is organised. **Each row represents a photograph record**, with attributes describing that photograph and a geographic location that QGIS can display as a point.

Check the following:

- Does the layer contain records, and are points displayed in the expected geographical area?
- How many records were returned? Note the feature count; this will be important for our later grid analysis.
- Which attributes are available? Look for photo identifiers, dates, user information and geographic coordinates.
- Are some points on top of one another? Zoom in to see why a dense point map may conceal the number of observations.

Save the QGIS project after checking the layer. Record your download date, area of interest and feature count in your working notes, because the results of an online query may change over time.

![An archived view of photograph locations in QGIS](Images/Screenshot%202025-07-12%20173724.png)

*Example from the supplied archive. Your own dataset, number of points and map appearance will differ.*

## 2.8 If the download does not work

**The plugin is missing.** Check that experimental plugins are visible and that you are using a supported QGIS 3 version. Consult the [plugin listing](https://plugins.qgis.org/plugins/flickrdl/) for published versions and installation information.

**Flickr rejects the request.** Recheck your API key and whether Flickr has granted access. Do not publish the key while asking for help. Network access, API restrictions and service changes may also prevent the request from succeeding.

**No photographs are returned.** Check that west/east and south/north were entered correctly. Try a different small area with known photographic activity, and confirm that the bounds use longitude and latitude rather than projected map coordinates.

**The plugin cannot write the database.** Check that the selected file is a *created SpatiaLite database*, not an arbitrary empty SQLite file, and that you have permission to write to its folder.

**You cannot obtain an API key or the plugin is temporarily unusable.** Continue the learning pathway using the supplied example data, `london_photos.csv`, in this resource folder. The next chapter can demonstrate spatial aggregation with existing records. This fallback preserves the main objective of the tutorial without requiring everyone to solve an external service problem first.

## What you have learned

You have defined a study area, accessed a public online data source through an API, stored geographic information in a spatial database and examined the resulting point layer. At this stage, the map still displays individual photograph locations.

In **Chapter 3 — Analysing Spatial Density in QGIS**, we will create a regular grid and count how many photographs fall within each cell. That transformation turns a crowded point map into a series of numerical values from which we can build our landscape.
