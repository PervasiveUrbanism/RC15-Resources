# 1. Introduction — From Points to Landscapes

[Sentiment Landscapes overview](README.md) · [Existing technical draft](TUTORIAL.md)

## Making sense of dense geographical data

Cities generate enormous quantities of geographically referenced information. Property transactions, social media posts, environmental measurements, transport activity and photographs can all be associated with specific locations. When represented on a map, these datasets allow us to investigate how different activities and conditions are distributed across space.

The simplest way to visualise this information is to place a point at each recorded location. This works well when the number of observations is relatively small. As the dataset grows, however, the map becomes increasingly difficult to read. Points overlap, dense areas become visually saturated, and patterns that might be significant are obscured.

Consider a map showing property transactions in London. Each point represents a property sale, potentially carrying information about its price, size or type. Several flats within the same building may share almost identical coordinates. On a conventional point map, these transactions would overlap, making it difficult to understand either how many properties were sold or how prices vary across the neighbourhood.

This is not simply a problem of graphic design. It is a problem of how we translate large quantities of individual observations into information that can be understood.

## From individual points to spatial patterns

There are different ways of addressing this challenge.

One approach is to change how individual points are represented. For example, proportional symbols can use the size of a dot to communicate a value. Heatmaps offer another approach, transforming concentrations of points into continuous fields of colour.

In this tutorial, we will explore a different method: **translating geographical data into a three-dimensional landscape**.

Rather than displaying every observation individually, we divide our study area into a regular grid. Each grid cell collects information from the points falling within its boundaries. We can then calculate a value for each cell, such as the number of observations or their average price.

These values become the elevations of a new landscape. Areas with higher values rise into peaks, while areas with lower values remain closer to the ground. By connecting these elevations into a continuous surface, we create a topography that expresses the geographical distribution of the data.

The resulting landscape is not a representation of the physical terrain. It is an **artificial topography constructed from information**.

## Our example: Photographing London

To explore this method, we will work with geolocated photographs from Flickr, an online photography platform.

Photographs uploaded to Flickr can contain geographical coordinates indicating where they were taken. By collecting these locations within a defined area of London, we can investigate how photographic activity is distributed across the city.

We will divide the study area into a regular grid and count how many photographs fall within each cell. These counts will determine the height of our landscape.

**A high peak will represent an area with many recorded photographs. A low area will represent relatively few.**

The result offers a different perspective on the city: one shaped not by buildings, streets or physical elevation, but by the geographical distribution of photographic activity.

This does not necessarily tell us which places are most popular or most appreciated. The distribution is influenced by who uses Flickr, what they choose to photograph and which photographs contain usable location information. Understanding these limitations is part of interpreting the landscape.

## What we will create

![Example landscape created using geographical photograph data](Images/ViewCapture20250712_174129.png)

*An example of the three-dimensional landscape developed from geographical data.*

The tutorial follows a continuous workflow across three applications.

We begin in **QGIS**, where we collect geographical data, divide our study area into a grid and calculate the number of photographs in each cell.

We then move to **Rhino and Grasshopper**, using the Heron plugin to position the geographical data and translate the recorded counts into a three-dimensional surface.

Finally, we develop the visual representation using contour lines, geographical context and **Adobe Illustrator**. The aim is to create a graphic that is both expressive and analytically meaningful.

Although we use Flickr photographs for this exercise, the method is not specific to photography. The same process could be applied to property prices, population statistics, environmental measurements or other datasets containing geographical coordinates and numerical values.

By the end of the tutorial, you will understand how to move from thousands of individual data points to a spatially organised representation, and how the decisions made during that process influence what the resulting landscape communicates.
