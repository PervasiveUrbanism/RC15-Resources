# File Access in Google Colab

Part of **RC15 Resources**, the permanent tutorial library for Pervasive Urbanism.

**Software:** Google Colab, Python  
**Format:** Short practical Jupyter notebook  
**Prerequisites:** Basic familiarity with running a Python code cell; a Google account to use Colab  
**Software versions:** Colab is a hosted service and may change; the notebook has not been rerun during this editorial review.

[Browse this topic](../README.md) | [Library home](../../../README.md)

## Why this matters

In architectural and urban research, we often work with external datasets: sensor recordings, tables of locations, images or other files. Before Python can analyse those files, it needs to know where to find them.

**Google Colab runs Python on a remote computer**, not directly on your laptop. This makes it convenient to start programming without installing Python locally, but also means that the notebook cannot automatically read files stored on your own computer.

This short exercise introduces three everyday ways of bringing data into a Colab session. Understanding the differences will help you organise your work and avoid losing files when a runtime disconnects.

## What you will learn

| Method | When it is useful | What to remember |
| --- | --- | --- |
| **Upload from your computer** | A quick experiment with one or a few local files | Files placed in the runtime are temporary; upload again when starting a fresh runtime |
| **Mount Google Drive** | Ongoing projects whose datasets should remain accessible between sessions | Authorise access deliberately; files saved in Drive persist, but the mounted connection may need reconnecting |
| **Download from a URL** | Public datasets hosted on a website or repository | The download requires a valid URL and network access; a file downloaded into the runtime is temporary unless saved elsewhere |

The key distinction is between **temporary runtime storage** and **persistent storage** such as Google Drive. Saving a notebook does not automatically save every file created or downloaded in its runtime.

## Follow the notebook

[**Open the exercise in Google Colab**](https://colab.research.google.com/github/PervasiveUrbanism/RC15-Resources/blob/main/tutorials/programming-and-data-access/file-access-in-google-colab/Xtra%20-%20File%20access%20in%20google%20colab.ipynb)

You can also [read the notebook directly on GitHub](Xtra%20-%20File%20access%20in%20google%20colab.ipynb) without running Python.

Open it in Colab and work through its sections in order. Run each code cell using the play button, read the result and inspect the **Files** panel to see what appears in your runtime.

1. **Upload:** Choose a small CSV or text file from your computer and run the `files.upload()` example. Look for the file in Colab's working directory.
2. **Google Drive:** Run the `drive.mount('/content/drive')` example and follow the authorisation process. Find a file stored in your Drive. Only grant the access you are comfortable giving to this notebook.
3. **URL:** Run the `requests.get()` example, which retrieves a public example CSV. Check that the downloaded file is available in the runtime.

Try restarting or disconnecting the runtime afterwards. Notice which files are no longer present and which remain in Google Drive.

To keep any edits to a notebook opened from GitHub, use **File → Save a copy in Drive**. Your personal copy will not overwrite the RC15 Resources repository.

## A small experiment

Use one CSV dataset of your choice and try bringing it into Colab in two different ways. Read it with `pandas.read_csv()`, then compare the paths and the steps required. Which approach makes the most sense for a quick exercise, and which would you prefer for a project you will revisit next week?

This exercise is about **file access**, rather than analysing the contents of the dataset. You can build on it in later Python and data-analysis tutorials.

## Practical notes

If the file cannot be found, confirm its exact name, extension and location in the runtime's Files panel. Paths are case-sensitive in Colab. When mounting Drive, look under `/content/drive/` rather than assuming your Drive is the current working directory.

Be selective about mounting a personal Google Drive in shared or untrusted notebooks. Only run code you understand and only share datasets you have permission to use. A public URL may also disappear or change over time.

For further information, see the [official Google Colab FAQ](https://research.google.com/colaboratory/faq.html).

*Editorial review: 27 October 2026. The README was expanded and two small wording corrections were made to the notebook. The notebook's exercises were preserved, but the code has not been rerun in Colab during this review.*
