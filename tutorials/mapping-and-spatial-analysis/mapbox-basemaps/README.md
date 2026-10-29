# A better background map: Mapbox and QGIS

[RC15 Resources](../../../README.md) · [Mapping and spatial analysis](../README.md)

A map background can do two very different things. It can help us locate our data, or it can compete with it. When we bring an analysis into QGIS, the default streets, labels and land-use colours are not always what we need. A quiet background might be more useful for showing pedestrian routes; a stronger distinction between land and water might help explain an urban edge.

<!-- @ChatGPT: this intro is a bit off. in most cases you just need a nice looking background fairy quickly. open stree maps works well in workmode but hardly presentations. online backgrounds that you can customise offer an alternative. mapbox offer custom webmaps for example and they are free for the low usage we use-->

In this exercise we will bring a Mapbox basemap into QGIS, then change its appearance using ChatGPT. The aim is not to make a finished cartographic design, but to learn how to choose and control the background against which our own information is presented.

**You need:** QGIS, a [Mapbox account](https://www.mapbox.com/), and an internet connection. The second part uses ChatGPT with access to the **Mapbox DevKit** plugin. Mapbox services have usage limits and may incur charges.

## 1. Bring a Mapbox map into QGIS
<!-- add an images -->
Start in [Mapbox Studio](https://console.mapbox.com/studio/), where you can explore ready-made map styles. A *style* defines the appearance of a map: the colours of roads and water, which labels are visible and how much detail appears at different scales. Choose a style that would make a useful background for one of your QGIS projects.

You can use an existing style or duplicate one to make your own version. For the moment, don't spend time adjusting individual colours. We want to see it working in QGIS first.

### Find your style and access token

Open the style in Mapbox Studio and locate its **Style URL**. It will look like this:

```text
mapbox://styles/YOUR_USERNAME/YOUR_STYLE_ID
```

We need the username and style ID from this address. We also need a **public access token** from the [Mapbox Access Tokens page](https://console.mapbox.com/account/access-tokens/). Tokens allow applications such as QGIS to request maps from your Mapbox account. Use a token with suitable read permissions; do not use a secret write token.

QGIS cannot use the `mapbox://` address directly as a WMTS connection. Instead, substitute your username, style ID and token into this address:

```text
https://api.mapbox.com/styles/v1/YOUR_USERNAME/YOUR_STYLE_ID/wmts?access_token=YOUR_PUBLIC_ACCESS_TOKEN
```

This URL gives QGIS access to the map through **WMTS** (Web Map Tile Service). In simple terms, Mapbox renders the background and sends it to QGIS as a series of map tiles. We can display those tiles beneath our own spatial data, but they are not editable road or building geometries inside QGIS.

### Connect QGIS

In QGIS, open **Layer → Add Layer → Add WMS/WMTS Layer**. Select **New**, name the connection `Mapbox background`, and paste the URL above. Save the connection, click **Connect**, select the available layer and choose **Add**.

<!-- add an images -->

Move the new layer to the bottom of the **Layers** panel, beneath your own data. Navigate to an area you know and zoom in and out. Notice how roads, labels and buildings change as you move between scales.

**You now have a Mapbox basemap inside QGIS.** The background is being supplied by Mapbox; your analytical layers remain in QGIS. Save your QGIS project.

*Suggested illustration:* QGIS screenshot showing the WMS/WMTS connection dialog, followed by the same map with a custom Mapbox background beneath a simple analysis layer.

## 2. What if the background is too dominant?

Look at the map with your own data switched on. Are major roads drawing too much attention? Do place labels obscure your information? Are the land and water colours suitable for the graphic you want to make?

You could go back to Mapbox Studio and change the style manually. 

<!-- add an images  @chatgpt:say that i have been doing that for the last ten years. eventouh it is a vey intuition interfaces, it taka time. so the new lid in the block is ChatGPT or claude mcp to get the colors and settings ringt and to play more with colours -->

Here we'll try another route: asking ChatGPT to work with the style through **Mapbox DevKit MCP**.

**MCP**, or *Model Context Protocol*, lets an AI assistant use tools provided by another application. Mapbox DevKit exposes tools for inspecting, creating and editing styles. It does **not** edit your QGIS layers or control QGIS itself. We change the map's appearance in Mapbox, then inspect that change in QGIS.

### Connect Mapbox DevKit

Mapbox provides a [hosted DevKit MCP server](https://docs.mapbox.com/location-ai/mcp-servers/devkit-mcp-server/), so there is no separate software to install on your computer.

In ChatGPT, open the **Plugins** area and look for the option to add a custom MCP server. If your account or workspace supports custom connections, use:

```text
https://mcp-devkit.mapbox.com/mcp
```

Name the connection **Mapbox DevKit** and follow the Mapbox **OAuth** sign-in. This grants the connection access to the Mapbox account you authorise. The precise ChatGPT menus may change; use the [official Mapbox setup guide](https://docs.mapbox.com/location-ai/mcp-servers/devkit-mcp-server/) if they differ from those shown here.

Once connected, begin with a simple request:

> List the Mapbox styles in my account. Identify the style I used in QGIS, and tell me whether it can be edited. Do not change anything yet.

This first request is important. It establishes which Mapbox account, style and version we're working with before we make changes.

### Make a lighter version

Rather than altering your original style, ask ChatGPT to **create an editable copy**. Then try a request like this:

> Create a lighter version of this basemap for an urban analysis drawing. Use a warm off-white land colour, pale blue water and restrained grey roads. Keep the labels readable but less prominent. Show me a preview before making further changes.

The assistant can inspect the style's layers and use DevKit to propose or apply changes. Review the preview critically. A colour that looks good at city scale can become muddy or overly prominent at street scale, because map styles can use different rules for different **zoom levels**.

Compare the result at three scales: a broad neighbourhood view, a street-level view and a close detail. If the background becomes darker or busier as you zoom, ask the assistant to inspect the relevant layers and zoom-dependent colour or visibility rules. Be specific about what you want to preserve, and check which style was actually changed.

*Suggested illustration:* Three views of the same location: original style, lighter edited style, and the edited style beneath a QGIS analysis layer.

## 3. Return to QGIS

Once you are satisfied with the edited style, make sure you are using its **published** version. Copy the username and style ID of the new style and create another WMS/WMTS connection in QGIS using the same URL pattern as before. If you edited an existing published style instead, refresh or reconnect its layer.

Keep both basemaps in the project. Toggle between them while leaving your own data visible. Which background makes the analysis easier to read? What happens when you zoom in? The point is not simply to produce a prettier map, but to recognise that the background influences what the viewer notices.

**The exercise ends here:** one map in QGIS, two alternative backgrounds, and a decision about which better supports your information.

## If something doesn't work

| Problem | First thing to check |
| --- | --- |
| QGIS cannot connect | Confirm the WMTS URL, style ID and public token. Check that the token can access the style. |
| The background is blank | Check layer visibility, map location and whether the Mapbox style has been published. |
| ChatGPT cannot see your styles | Confirm that Mapbox DevKit is connected and authorised for the intended Mapbox account. |
| The edited map doesn't appear in QGIS | Check whether ChatGPT edited a copy, a draft or the published style. A copy has a different style ID; cached map tiles may also delay updates. |
| The colour changes unexpectedly as you zoom | Ask DevKit to inspect the relevant style layers, expressions and zoom-dependent rules; compare several scales. |

Two details are worth remembering. **QGIS receives raster map tiles**, not the editable Mapbox style. And Mapbox Studio can have a **draft** that differs from the published style delivered to QGIS; changes made through the Styles API may affect the published version without changing Studio's draft. Always check which version you're viewing. <https://docs.mapbox.com/api/maps/styles/#drafts>

Before distributing a final map, retain the required Mapbox and data-source attribution. Avoid publishing your personal access token in shared project files or screenshots.

---

**Further reference:** [Mapbox: using a map in ArcGIS and QGIS](https://docs.mapbox.com/help/ja/tutorials/mapbox-arcgis-qgis/?step=3) · [Mapbox Styles API and WMTS endpoint](https://docs.mapbox.com/api/maps/styles/#retrieve-a-maps-wmts-document) · [Mapbox DevKit MCP](https://docs.mapbox.com/location-ai/mcp-servers/devkit-mcp-server/)

**Editorial status:** Revised tutorial draft. The sequence is based on documented Mapbox and QGIS functionality, but the full workflow and interface screenshots still need desktop verification. No live account changes were made while preparing this tutorial.
