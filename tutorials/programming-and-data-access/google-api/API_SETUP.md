# Setting up Google Places API (New)

This guide accompanies the [Google Maps Services API tutorial](README.md). It describes the current setup for students starting a **new Google Cloud project**. It does not claim that the original 2025–26 notebook works unchanged.

## What is an API key?

An **API (application programming interface)** lets a program request structured information from a remote service. Google Maps Platform uses a key to identify the project responsible for a request and its usage charges. An API key is **not a free-access password**: using the service may incur costs.

The old exercise includes a response from **Places API (Legacy)**. Google's documentation states that, from **October 2026**, new Cloud projects cannot enable Places API (Legacy). Existing projects may continue to use it, but new students should use **Places API (New)**.

## Obtain a key

1. Open the [Google Cloud Console](https://console.cloud.google.com/), sign in, and create a new **project**. Use a descriptive name such as *RC15 Places Exercise*. A project groups APIs, credentials and charges.
2. Under **Billing**, link a billing account to that project. Review Google's [current Places pricing](https://developers.google.com/maps/documentation/places/web-service/usage-and-billing), any applicable free usage, and project budgets before requesting live data. A budget alert is **not** a hard spending cap: monitor usage and quotas as well.
3. From **APIs & Services → Library**, find and **enable Places API (New)**. The service identifier is `places.googleapis.com`. The older *Places API (Legacy)* is not the right choice for a new project.
4. Open **Google Maps Platform → Keys & Credentials**, choose **Create credentials → API key**, and create a key for the project.
5. **Restrict the key** so its *API restrictions* allow only **Places API (New)**. Configure an appropriate *application restriction* for your environment. A key used by a student laptop or local notebook must not be assumed safe just because it is stored outside the notebook; consult Google's guidance for server-side key security and supported application restrictions.
6. Keep the key private. **Do not paste it into the notebook source, commit it to GitHub, include it in screenshots or display it in notebook outputs.** If exposed, rotate or revoke it in the Cloud Console.

You can check the steps against [Google's official Places API (New) setup guide](https://developers.google.com/maps/documentation/places/web-service/get-api-key). The Console interface may change.

## Read a key from the environment

In **PowerShell**, start a new shell and enter the following command, substituting your own key locally. Start Jupyter from **that same PowerShell session** so the notebook inherits it:

```powershell
$env:GOOGLE_MAPS_API_KEY = "YOUR_KEY_HERE"
jupyter lab
```

On **macOS or Linux**, the equivalent for a terminal session is:

```bash
export GOOGLE_MAPS_API_KEY="YOUR_KEY_HERE"
jupyter lab
```

A shell assignment can remain in command history, and other local processes with suitable privileges may access environment variables. These simple steps are suitable for an introductory local exercise, not a substitute for managed secrets in production. Never put a real key in a shared teaching document.

To check whether the notebook can read a key **without revealing it**:

```python
import os

api_key = os.getenv("GOOGLE_MAPS_API_KEY")
print("API key available:", bool(api_key))
```

## A small current API example

The following Python code uses **Text Search (New)** to request a place name, address and coordinates. The exact fields requested determine some of the billing charges. The example does **not** run until you deliberately call `search_places()`, and it sends a billable request if you do so.

```python
import json
import os
from urllib.request import Request, urlopen

def search_places(text_query):
    api_key = os.environ["GOOGLE_MAPS_API_KEY"]

    request = Request(
        "https://places.googleapis.com/v1/places:searchText",
        data=json.dumps({"textQuery": text_query, "pageSize": 3}).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "X-Goog-Api-Key": api_key,
            "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.location",
        },
        method="POST",
    )
    with urlopen(request, timeout=20) as response:
        return json.load(response)

# After enabling the API and checking billing:
# result = search_places("public libraries in London")
# for place in result.get("places", []):
#     print(place.get("displayName", {}).get("text"), place.get("location"))
```

This example follows the documented **Places API (New)** request structure and uses only Python's standard library. **It has not been live-tested with a billed Google account**. A valid key, enabled API, billing account, access permissions and appropriate restrictions are required.

## How this differs from the historical exercise

| Original Places API (Legacy) | Places API (New) |
| --- | --- |
| Legacy paths such as `/maps/api/place/...` | Versioned endpoints such as `/v1/places:searchText` |
| Older place detail structure commonly wrapped in `result` | Text Search returns a `places` array |
| Fields such as `name`, `geometry.location.lat/lng`, `photo_reference` | Fields such as `displayName.text`, `location.latitude/longitude`, photo resource `name` |
| Some calls did not require explicit lists of fields | **Field masks are mandatory** for relevant Places API (New) searches/details |
| Legacy photo-reference workflow | New photo resource names, with specific attribution and caching restrictions |

Google's migration documentation describes the differences between the two APIs. Do not mechanically rename fields without also updating endpoints, request methods, authentication headers, the response parsing and photo handling.

## Learn from sample data before making requests

The existing [`assets/sample.json`](assets/sample.json) is useful for practising JSON inspection **without an API key or billable requests**. It is explicitly an **archived legacy response**; its field structure does not demonstrate the modern API. The supplied photographs also require a review of image-use permissions, attribution and storage restrictions before they are reused in a publicly distributed teaching resource.

## References

- [Set up Places API (New)](https://developers.google.com/maps/documentation/places/web-service/get-api-key)
- [Text Search (New)](https://developers.google.com/maps/documentation/places/web-service/text-search)
- [Migrate from Places API (Legacy)](https://developers.google.com/maps/documentation/places/web-service/legacy/overview-legacy)
- [Place Photos (New)](https://developers.google.com/maps/documentation/places/web-service/place-photos)

**Status: Documentation-checked, but not live-tested.** This setup guide is a starting point for our review of the original notebook, not a declaration that the historic notebook is compatible.
