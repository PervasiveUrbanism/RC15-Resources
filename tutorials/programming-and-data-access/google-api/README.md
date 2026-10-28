# Mapping Restaurants in Hackney with Google Places API

Part of **RC15 Resources**, the permanent teaching library for Pervasive Urbanism.

**Software:** Python 3, Jupyter Notebook, Google Places API (New) and Google Maps Static API  
**Exercise:** Find and map restaurants within **750 m of Hackney Central station**  
**Output:** One restaurant dataset in memory, one Google map and an accompanying table of cuisine, relative price level and rating  
**Status:** Draft; API requests and map rendering require a live desktop test.

[Browse this topic](../README.md) | [Library home](../../../README.md)

## The exercise

**What restaurants are found around Hackney Central, and how do their cuisines, price levels and ratings vary spatially?**

Start with **[Hackney_Restaurants_750m.ipynb](Hackney_Restaurants_750m.ipynb)**. The notebook works through a single practical question in six short stages: define the search radius, prepare an API key, request restaurants using Nearby Search (New), extract the relevant fields, place the restaurants on a Google map, and read their attributes in a table.

First read [Getting a Google Maps Platform API key](API_SETUP.md). Students need to enable **two APIs**, Places API (New) and Maps Static API. Both services require billing and may incur costs. The notebook contains no credentials and has no saved outputs.

The map uses Google's Static Maps service rather than a non-Google map, in accordance with Google's rules for displaying Places data. One Nearby Search returns **at most 20 results**, even if more restaurants exist in the neighbourhood. Cuisine is inferred from a Google place-type category and may be generic or missing; price levels and ratings may also be unavailable. The resulting sample is **not an exhaustive restaurant census**.

## Historical material

The original [2025–26 Google Maps Services notebook](Xtra%20-%20Google%20Maps%20Services.ipynb) and [supporting images and legacy JSON](assets/) remain unchanged as archival teaching material. An earlier experimental notebook, [Google_Places_API_New.ipynb](Google_Places_API_New.ipynb), is retained for now but **superseded by the focused Hackney exercise**. It is not part of the recommended learning path.

**Desktop verification still required:** Run the Nearby Search and Maps Static calls with a suitably restricted key and billing-enabled project; inspect the returned cuisine and price fields, map symbols, charges, output attribution and storage policies. Do not commit API responses, permanent datasets or map exports without reviewing Google's current terms. See [Editorial Backlog](../../../EDITORIAL_BACKLOG.md).
