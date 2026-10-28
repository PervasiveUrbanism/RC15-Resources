# Python Functions and Modules

Part of **RC15 Resources**, the permanent tutorial library for Pervasive Urbanism.

**Software:** Python 3 and Jupyter Notebook  
**Format:** Short notebook with supporting Python files  
**Prerequisites:** Basic Python syntax; no additional Python packages required for the current notebook  
**Status:** Editorial revision completed; execution in a clean Jupyter environment remains to be verified.  
**Original collection:** Xtra 01 - Modularise the code

[Browse this topic](../README.md) | [Library home](../../../README.md)

## What you will learn

As code becomes longer, it helps to keep reusable functions in separate files, called **modules**. A notebook can import those functions instead of duplicating them. A related organisational question is how to provide **passwords and API keys** to a program without publishing them.

[Open the notebook — Python Functions and Modules](Xtra%20-%20Modularise%20the%20code.ipynb). Work through two short parts:

1. Import and run the functions in [`functions.py`](functions.py), then modify one function and see what happens after restarting the kernel.
2. Inspect the **dummy** credential examples in [`Passwords.py`](Passwords.py) and [`passwords.csv`](passwords.csv), then learn why separate files are **not automatically secure**. Practise reading a fictional configuration value from an environment variable without printing it.

The accompanying [`.gitignore`](.gitignore) demonstrates how to exclude **new, untracked** private configuration files and notebook caches from Git. It does not remove files that are already tracked or erase them from Git history.

**Important:** All included credential values are placeholders. Never substitute actual passwords or API keys into these tracked example files, or save real credentials in a shared notebook's output. The notebook uses only Python's standard library and the supplied helper files.

**Desktop check pending:** Open the notebook in a fresh Python/Jupyter environment, confirm imports from the same folder, edit and reload the helper module, and test the optional environment-variable demonstration. See the [editorial backlog](../../../EDITORIAL_BACKLOG.md).
