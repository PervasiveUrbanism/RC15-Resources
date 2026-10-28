# Google Maps Services API — Python

Part of **RC15 Resources**, the permanent teaching library for Pervasive Urbanism.

**Software:** Python / Jupyter; Google Maps Platform (original exercise)  
**Format:** Original example notebook and supporting JSON/image assets  
**Status:** Original teaching material transferred; editorial and technical review pending.  
**Original collection:** Xtra 02 — Google API (RC15 Skills 2025–26)

[Browse this topic](../README.md) | [Library home](../../../README.md)

## Start here

Open **[Xtra - Google Maps Services.ipynb](Xtra%20-%20Google%20Maps%20Services.ipynb)**, copied from the [original 2025–26 RC15 Skills exercise](https://github.com/PervasiveUrbanism/PervasiveUrbanism_25-26/blob/main/Skills%20Module%201%20Cartographies%20of%20Affect/Skills%201%20-%20Day%202%20Datamining%20Python/Xtra%2002%20-%20Google%20API/Xtra%20-%20Google%20Maps%20Services.ipynb). It is retained unchanged so we can review and refine the existing tutorial rather than write a duplicate from scratch.

The [assets folder](assets/) contains a sample Google Places JSON response and example photographs from the original exercise. These files were already present in RC15 Resources, so they have not been duplicated.

## Set up Google Places API (New)

Start with **[How to obtain and restrict a Google API key](API_SETUP.md)**. The new guide covers Google Cloud project creation, billing, enabling Places API (New), key restrictions, environment variables, a small modern Python Text Search request, and the differences from the archived API response.

**Important compatibility finding (October 2026):** Google no longer enables Places API (Legacy) for newly created projects. The supplied `assets/sample.json` uses the legacy response format. Therefore, the historic example cannot be assumed to run unchanged for a student with a new Google Cloud project. The current API requires different endpoints, requests and field masks.

**Review status:** Google's current API documentation has been checked, but the original 10.8 MB notebook could not be retrieved as complete readable cell text through the connected GitHub interface. Individual code cells and their saved outputs are **not yet audited or executed**, so no claim is made that the notebook has been fully validated.

## Before running the notebook

This is an **unverified historical example**, not yet a current installation guide. Google's Places APIs, authentication, billing, data-retention policies and photo licensing may have changed since the original exercise. In particular, the archived JSON uses an older response format; do not assume every endpoint, field or API call in the notebook is still supported.

Read through the notebook before executing its cells. **Do not enter real API keys into a notebook that might be committed or shared**, and do not publish saved outputs containing credentials or personal data. Review any hard-coded paths and dependencies.

## Editorial work remaining

We will review the notebook together, identify its learning sequence, update the API methods and key-handling guidance where necessary, and decide which existing example images and outputs to retain. We should also verify the terms for reuse of any Google Places photos. See the [editorial backlog](../../../EDITORIAL_BACKLOG.md).
