# Obtain a Google Maps Platform API key

This short setup accompanies [Mapping Restaurants in Hackney](README.md). It uses **Google Places API (New)** to retrieve restaurant information and **Google Maps Static API** to draw the results on a Google map.

## 1. Create a project and enable the two services

1. Sign in at the [Google Cloud Console](https://console.cloud.google.com/) and create a project, for example `RC15 Restaurant Mapping`.
2. Open **Billing** and link an eligible billing account. Review [Places API pricing](https://developers.google.com/maps/documentation/places/web-service/usage-and-billing) and [Maps Static API pricing](https://developers.google.com/maps/documentation/maps-static/usage-and-billing) **before running the notebook**. Budgets and alerts help monitor spending but are not hard cost caps.
3. Open **APIs & Services → Library** and enable **Places API (New)** (`places.googleapis.com`).
4. In the same API library, enable **Maps Static API** (`static-maps-backend.googleapis.com`).
5. Go to **APIs & Services → Credentials** and create an **API key**.

Google regularly revises the Cloud Console interface. If a menu has moved, use the Console's search function and follow the [official API-key documentation](https://developers.google.com/maps/documentation/places/web-service/get-api-key).

## 2. Protect the key

Under **API restrictions**, select **Restrict key** and allow only **Places API (New)** and **Maps Static API**. Set suitable **application restrictions** for the local machine or environment; server-side IP address restrictions may be appropriate for a controlled fixed-IP environment but are not automatically suitable for laptops with changing addresses. Local scripts holding API keys are not equivalent to secure production applications.

Set sensible usage quotas and monitor your Cloud Console usage. Do not include real credentials in code, output cells, screenshots or GitHub commits. If a key is exposed, revoke or rotate it.

For the classroom exercise, both requests run in the local Python process. The Places request sends the key in an HTTP header; the Static Maps request requires it as a URL parameter. The notebook does **not** print or save the URL. Be aware that URLs and environment variables can still leak through logs or local process access.

## 3. Supply the key to Jupyter

Use a terminal to set an environment variable **before** launching Jupyter.

**Windows PowerShell:**

```powershell
$env:GOOGLE_MAPS_API_KEY = "YOUR_KEY_HERE"
jupyter lab
```

**macOS / Linux:**

```bash
export GOOGLE_MAPS_API_KEY="YOUR_KEY_HERE"
jupyter lab
```

Replace the placeholder locally; never copy the real value into a repository. Terminal histories may retain entered commands. For more secure or ongoing work, use an operating-system credential store or a dedicated secret manager instead of shell commands.

In the notebook, the following checks for a key **without revealing it**:

```python
import os
print("API key available:", bool(os.getenv("GOOGLE_MAPS_API_KEY")))
```

If it prints `False`, launch Jupyter from the terminal session in which you set the variable. If you use Jupyter inside a remotely hosted environment, its environment variables are **not** shared automatically with your local computer.

## 4. Understand costs and restrictions

Our exercise sends **one Nearby Search (New)** request when its search cell runs and **one Maps Static API** request when its map cell runs. Every rerun can create additional billable requests. The Places fields `rating` and `priceLevel` are not part of the cheapest data tier, so consult the current field-level pricing before running.

Google limits Nearby Search (New) to **20 results per request**. Its ranking does not give a complete inventory of restaurants. Google also restricts storage and redisplay of Places data: keep this exercise's dataset in memory and show it on a **Google map**, not OpenStreetMap or a Folium map.

**Sources:** [Nearby Search (New)](https://developers.google.com/maps/documentation/places/web-service/nearby-search) · [Places field masks and pricing tiers](https://developers.google.com/maps/documentation/places/web-service/data-fields) · [Maps Static API](https://developers.google.com/maps/documentation/maps-static/start) · [Places policies](https://developers.google.com/maps/documentation/places/web-service/policies).

**Verification status:** This setup follows current documentation, but has not been tested with a live billed Google Cloud project.
