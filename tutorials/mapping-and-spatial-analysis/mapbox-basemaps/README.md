# Mapbox Basemaps in QGIS

[Library home](../../../README.md) · [Mapping and spatial analysis](../README.md) · [QGIS index](../../../software/qgis.md)

Create a quiet background map for your own spatial data, then adjust its appearance through ChatGPT.

**Level:** beginner. **You will learn:** connect a Mapbox style using WMTS, edit colours and zoom rules, and check the result in QGIS.

**You need:** QGIS, internet access, a Mapbox account with a style you can edit, and ChatGPT with permission to add custom MCP plugins for Part 2. Part 1 works independently. Mapbox usage may incur charges; check your account's usage and pricing.

**Verification:** official documentation checked 29 October 2026; no end-to-end application test or tested QGIS version yet. Menu labels may vary.

**Credits:** prepared for RC15 Resources from the official sources linked below; original teaching year and individual author unconfirmed. No project files or third-party images are supplied.

## Part 1 — Connect a Mapbox style through WMTS

A **style** describes the map's appearance. **WMTS** (Web Map Tile Service) delivers that map as image tiles. QGIS displays these beneath your data; it does not receive editable road or building features.

### 1. Prepare the style and token

1. Open [Mapbox Studio](https://console.mapbox.com/studio/). Create or duplicate a style into your own account and name it `RC15 background`. Keep an original copy for comparison. Publish your Studio changes.
2. Find its **Style URL** in the sharing options. It has this form:

   ```text
   mapbox://styles/YOUR_USERNAME/YOUR_STYLE_ID
   ```

   The username identifies the owner; the style ID identifies the design. This is different from a Studio editing link or a preview page.
3. On [Mapbox's Access Tokens page](https://console.mapbox.com/account/access-tokens/), obtain a public token (`pk.…`) with the read permissions needed for your style (`styles:read`). A token associates requests with your account. Use an owner-account token for a private style. Never put a secret write token (`sk.…`) into QGIS.
4. Replace all three placeholders below, keeping the URL on one line:

   ```text
   https://api.mapbox.com/styles/v1/YOUR_USERNAME/YOUR_STYLE_ID/wmts?access_token=YOUR_PUBLIC_ACCESS_TOKEN
   ```

The `mapbox://` address identifies the style; this HTTPS address retrieves its WMTS capabilities document. Do not paste the former into QGIS's WMTS URL field. The endpoint and access rules are documented in the [Styles API](https://docs.mapbox.com/api/maps/styles/#retrieve-a-maps-wmts-document).

Your token can be saved inside a QGIS project or exported connection. Keep personal URLs out of Git, shared project files and screenshots; recipients should configure their own token.

### 2. Add it to QGIS

1. Choose **Layer → Add Layer → Add WMS/WMTS Layer**, then **New**.
2. Enter a connection name such as `RC15 Mapbox` and paste the HTTPS WMTS URL. Leave username/password empty: the token is already in the URL.
3. Save, select the connection and click **Connect**.
4. Select the advertised WMTS layer/tileset, choose its offered Web Mercator matrix set (`EPSG:3857`) and image format, then **Add**. The exact list layout depends on QGIS version.
5. Move the basemap to the bottom of the Layers panel. Navigate to your study area and place your own data above it. Save your project locally.

**Checkpoint:** you can see the background beneath your data and it changes detail as you zoom. QGIS can reproject it for display in your project CRS; keep an appropriate local CRS for measurements.

See the [QGIS WMS/WMTS client manual](https://docs.qgis.org/3.40/en/docs/user_manual/working_with_ogc/ogc_client_support.html#wms-wmts-client) for the connection controls. This follows the workflow of the [supplied Mapbox tutorial](https://docs.mapbox.com/help/ja/tutorials/mapbox-arcgis-qgis/?step=3). That page returned little readable content during verification; the API and QGIS references above establish the connection steps.

## Part 2 — Edit the background through ChatGPT

Use **Mapbox DevKit MCP** for style editing. MCP connects ChatGPT to Mapbox's tools; it does not connect ChatGPT to your QGIS canvas.

### 1. Connect the hosted server with OAuth

1. In ChatGPT **on the web**, open **Plugins → + → Add custom MCP server**.
2. Name it `Mapbox DevKit`. Enter this Server URL under Connection:

   ```text
   https://mcp-devkit.mapbox.com/mcp
   ```

3. Choose **OAuth** authentication. Review the permissions and warning, then select **Create as a plugin**. Install the resulting plugin and enable/select it in your conversation.
4. Complete the browser sign-in to Mapbox and authorise the intended account when prompted. Ask ChatGPT to list your styles to check access.

No local Node.js installation or manually pasted Mapbox token is needed for the hosted connection. QGIS still needs the public token from Part 1. If the custom-server option is missing, check workspace permissions and current account availability. Follow [OpenAI's custom MCP setup](https://developers.openai.com/api/docs/guides/custom-mcp-server) if the interface changes.

Mapbox's [DevKit documentation](https://docs.mapbox.com/location-ai/mcp-servers/devkit-mcp-server/) confirms the endpoint, OAuth and style tools. The hosted endpoint cannot create tokens; obtain the QGIS token through Mapbox's website.

### 2. Inspect, edit and preview

Start with a precise request:

> Retrieve my RC15 background style. Confirm its owner and style ID, and identify the water, land, road and label layers. Work on a duplicate. Suggest a pale grey land colour, muted blue water and quieter roads so my analysis stands out. Preserve sources and attribution. Explain the changes before applying them.

Then ask ChatGPT to apply the agreed changes to the duplicate, validate the style and preview the same location at zooms 10, 13 and 16. DevKit can retrieve, create, update, validate and preview styles. Layer IDs vary: inspect the actual style rather than assuming a layer called `roads` exists. If it uses imported components, ask which settings are editable before changing them.

### 3. Add zoom-dependent rules

Try this request:

> On the duplicate, show minor-road labels only from zoom 14. Make major roads thin at zoom 10 and thicker at zoom 16. Identify the affected layers and check the result at both zooms and between them.

Larger Mapbox zoom numbers mean closer views. Layer `minzoom`/`maxzoom` control visibility; expressions can change appearance smoothly. For example, this **paint-property fragment** sets line width from 0.5 pixels at zoom 10 to 2 pixels at zoom 16:

```json
{
  "line-width": ["interpolate", ["linear"], ["zoom"], 10, 0.5, 16, 2]
}
```

This is not a complete style. Ask ChatGPT to apply it to a suitable line layer while preserving other properties. See [Mapbox camera expressions](https://docs.mapbox.com/style-spec/reference/expressions/#camera-expressions). QGIS scales and Mapbox zoom numbers are different controls; compare the visible result at several scales.

### 4. Refresh the result in QGIS

Ask ChatGPT whether it changed the **draft or published version** and record the resulting style URL. Studio edits need publishing. API edits can update the published style directly without updating Studio's draft; do not publish an older draft over those changes. See [Mapbox's draft behaviour](https://docs.mapbox.com/api/maps/styles/#drafts).

If you used a duplicate, make a QGIS connection with its new style ID. Otherwise retain the existing URL. Refresh the QGIS canvas and compare the same location and scale. If it still shows the old map, reconnect/re-add the layer, clear the network cache under **Settings → Options → Network**, and allow time for Mapbox's tile cache to update.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Connection fails / 401 or 403 | Token validity, read permissions and URL restrictions. A browser-restricted token can fail in desktop QGIS. Use a dedicated token suitable for this client; never substitute a secret write token. |
| Style not found / 404 | Copy the owner and style ID again; check publication and private-style access. |
| Blank map | Enable the layer, put it below your data, navigate to a known location and check the offered matrix set. Try several scales. |
| MCP cannot list or edit styles | Reconnect OAuth to the correct account and check granted access. Confirm you own the editable copy. |
| Edits disappear or do not show | Check the style ID, draft/published target and both client/server caches. |
| Zoom rule has no effect | Inspect the actual layer and any existing visibility/filter rules; compare multiple zooms. |
| Map looks soft in a large export | WMTS supplies raster tiles. Check the layout at its final size and avoid enlarging it beyond useful tile detail. |

Before sharing a map, check Mapbox and source-data attribution requirements and include the required credits in the layout. For a next exercise, use this background beneath [Network Mapping](../network-mapping/README.md) or [Sentiment Landscapes](../sentiment-landscapes/README.md).
