# GitHub Beyond Coding

*Build a library of teaching resources, research, notes and ideas that you can develop across computers, your phone and AI tools.*

[← Programming and data access](../README.md) · [RC15 Resources home](../../../README.md)

**Level:** Beginner, with optional intermediate sections  
**Time:** Approximately 2–3 hours to explore the chapters and two exercises; further exploration is open-ended  
**Software:** A GitHub account, [GitHub Desktop](https://desktop.github.com/) (Windows or macOS); for later chapters, a text editor, optionally [Obsidian](https://obsidian.md/), [Working Copy](https://workingcopy.app/) and [iA Writer](https://ia.net/writer) (iPhone/iPad), and optionally ChatGPT or Claude  
**Prerequisites:** Basic experience with files and folders; no programming or command-line knowledge required  
**Teaching context:** RC15 – Pervasive Urbanism, Bartlett School of Architecture, UCL. Permanent resource, not tied to a particular teaching year  
**Author:** RC15 Resources teaching team  
**Last reviewed against documentation:** November 2026. Screenshots and app-specific steps should be checked in class; the complete cross-device workflow has not been independently tested as a single sequence.

## Why use GitHub if you are not a programmer?

Git was developed for software projects, where many people need to work on the same code without losing one another's changes. A project may have several contributors experimenting with alternative solutions, fixing problems or developing new features at the same time. Git records how the files change; GitHub provides a place to share those changes, compare alternatives and discuss which ones should become part of the main project.

<!-- @ChatGPT: Say that Git and Github are two diffetn things. Explain-->

This was originally a tool for programmers, and its strengths still reflect that history. Git works best with **text-based files**, including code, notes, instructions and Markdown documents. It can show precisely which lines someone has changed. It is less suitable for large binary files, such as detailed 3D models, videos or extensive collections of high-resolution images. GitHub also imposes file-size limits: files over 50 MB trigger a warning, and files over 100 MB are blocked in ordinary Git repositories. For larger design assets, shared storage or other specialist systems are usually more appropriate.

For architecture and urban design students, this distinction is useful. Renderings, large models and drawing packages need not be moved into GitHub. But scripts, research notes, tutorial instructions and the text surrounding a design project are good candidates. The [RC15 Resources library](https://github.com/PervasiveUrbanism/RC15-Resources) demonstrates this: its tutorials, code examples and links can be maintained and improved over time.

The rise of large language models (LLMs) and AI-assisted coding makes this approach even more relevant. ChatGPT, Claude and other assistants can help develop and edit text or code, while Git lets you see what has changed, compare versions and keep control of the result. We will start by using the RC15 library, then create our own repository, and finally explore how the same workflow can be used away from a desktop computer.

<!-- @ChatGPT: Yes, for the chapter above. please say that the repo structuure is somehting tht many LLM like working with. there is somewhat a natual fit. 
say also that github is intetesting for you can not only host code and markdown files but also fully feated htlm websides that somewhat rnder your contne nicer. -->

### Learning outcomes

By the end, you should be able to explain what Git and GitHub do; clone and update RC15 Resources with GitHub Desktop; recognise the difference between saving, committing, pushing and pulling; create Markdown notes and include images; establish your own private repository; explore Obsidian and AI-supported editing; and work with the same files on an iPhone.

### The three chapters

1. [GitHub and the RC15 Resources library](#1-github-and-the-rc15-resources-library)
2. [Your own repository: Markdown, Obsidian and AI](#2-your-own-repository-markdown-obsidian-and-ai)
3. [AI Writing and editing on an iPhone](#3-writing-and-editing-on-an-iphone)

---

## 1. GitHub and the RC15 Resources library

### Git, GitHub and repositories

**Git** runs on your computer and tracks versions of files. A **repository**, often shortened to *repo*, is a project folder whose history Git manages. **GitHub** can host a copy of that repository online, called the *remote*. Your computer holds a *local* copy. You do not need to be connected to the internet to write or make local commits.

A **commit** is a recorded snapshot of selected changes, accompanied by a short explanation. Unlike repeatedly saving files named `final-v2-revised.docx`, commits build a traceable history. A **branch** is an independent line of development; beginners can remain on the default branch, usually called `main`. A **pull request** proposes changes from one branch or fork for review before they are merged. You will not need to create one in the first exercise.

Git works particularly well with text: it can show which lines were added, removed or rewritten. Images can be stored too, but Git cannot compare their contents line by line as it does with text.

![RC15 Resources repository on GitHub](images/01-rc15-github-home.png)

*The RC15 GitHub page, with all repositories*

### Explore the RC15 repository

Open [RC15 Resources](https://github.com/PervasiveUrbanism/RC15-Resources). Its main `README.md` is the illustrated table of contents. Tutorials live inside topic folders, usually with their own `README.md`, images and example files.

Explore one of the mapping tutorials. Notice how links between Markdown files form a navigable library without needing a separate website. GitHub renders Markdown into readable pages, but the underlying files are still ordinary text.

A useful distinction: the annual RC15 Skills repository contains teaching work for a specific academic year, while **RC15 Resources** aims to remain useful across years.

### Install GitHub Desktop and clone the library

Install [GitHub Desktop](https://desktop.github.com/) and sign in to your GitHub account. On the RC15 Resources GitHub page, select **Code** and copy the HTTPS repository URL:

```text
https://github.com/PervasiveUrbanism/RC15-Resources.git
```

In GitHub Desktop choose **File → Clone repository → URL**, paste the address and choose a local folder. Click **Clone**. The repository is now present on your computer. Use **Repository → Show in Explorer** (Windows) or **Show in Finder** (macOS) to open the files. If GitHub Desktop offers to open the project in an editor, you can choose your preferred editor instead.

You can also download a ZIP from the GitHub website. A ZIP is useful for obtaining example files once, but it does not preserve a working Git connection for pulling updates or recording commits.

![Code menu and clone URL on GitHub](images/02-github-code-clone.png)

*Copy the repository URL using the Code menu.*

![Clone a repository in GitHub Desktop](images/03-desktop-clone-dialog.png)



![Additional GitHub Desktop clone step](images/03.1-desktop-clone-dialog%20Extra.png)

*Select the repository URL and its destination on your computer.*

![GitHub repository on the local computer](images/GithubOnMyPC.png)

*The cloned repository is available as a local folder on your computer.*

### Save, commit, push and pull are different operations

This distinction is central to using Git confidently.

| Operation | Where does it happen? | What does it do? |
| --- | --- | --- |
| **Save** | In the editor, on your device | Changes the file on disk |
| **Commit** | In your local Git repository | Records selected changes and a message in the local history |
| **Push** | From local repository to GitHub | Uploads commits to the remote repository |
| **Fetch** | From GitHub to your computer | Checks and downloads remote changes without applying them to your working branch |
| **Pull** | From GitHub to your local branch | Fetches and integrates remote changes into the local branch |

For example, saving a Markdown note does not automatically update GitHub. Committing it records your work locally, but another device will not see that commit until you push it. Conversely, if someone has updated the online repository, you must pull those changes to see them in your local folder.

GitHub Desktop normally shows **Fetch origin**, **Pull origin** or **Push origin** depending on the state of the repository. Fetch first if you are unsure whether there have been online changes.

![Changes and commit in GitHub Desktop](images/04-desktop-changes-and-commit.png)

*Review changed files before recording a commit.*

![Fetch origin in GitHub Desktop](images/05-desktop-fetch.png)

*Fetch checks the remote repository for new commits.*

![Push origin in GitHub Desktop](images/05.1-desktop-push.png)

*Push uploads your local commits to GitHub. Pull becomes available when there are remote updates to integrate.*

### Read-only access, contributions and branches

Cloning a repository does **not** give you permission to publish changes to it. You can read RC15 Resources and pull updates, but pushing changes to its shared remote requires write access. If you would like to suggest a change, discuss it with the teaching team. Depending on the contribution workflow, you may use a fork and pull request, or be invited to contribute on a separate branch. Do not experiment by committing directly to the shared `main` branch.

A **fork** is your own GitHub-hosted copy of another repository. A **branch** is a parallel line of work within a repository. A pull request presents proposed changes for comparison and review.

### Exercise 1 — Obtain and explore RC15 Resources

Clone RC15 Resources using GitHub Desktop. Open the folder in your file manager, locate a tutorial's `README.md` and open it in a text editor. Return to GitHub Desktop and locate the repository history. Try **Fetch origin** to check whether there are updates; use **Pull origin** if updates are available. You do not need to change or commit anything in the shared library.

To practise making a commit safely, wait until Chapter 2 and use a repository you own. The outcome of this first exercise is understanding how a public or shared teaching resource becomes a usable local library.

---

## 2. Your own repository: Markdown, Obsidian and AI

GitHub becomes much more interesting when the collection belongs to you. A private repository might hold research notebooks, architectural precedents, travel observations, reading notes, recipes, photographs of memorable meals, or sketches for future projects. It can grow gradually without requiring you to choose one specialised app for all your material.

### Create a personal private repository

On GitHub, choose **New repository**. Give it a descriptive name such as `field-notes` or `personal-library`, set its visibility to **Private**, and initialise it with a README. Create the repository, then clone it through GitHub Desktop.

*Private* means that the repository is not normally visible to the public, not that its contents are end-to-end encrypted. Do not store passwords, API keys, confidential client material or information you are not authorised to upload. Keep an independent backup of anything important: version history and backups serve different purposes.

A possible folder structure is:

```text
personal-library/
├── README.md
├── research/
│   └── public-space.md
├── places/
│   └── berlin-notes.md
└── recipes/
    ├── roast-chicken.md
    └── images/
        └── roast-chicken.jpg
```

Do not worry about finding the perfect structure. Start small and rearrange it when you understand how you use the collection. Keep filenames descriptive and use consistent naming. Photos and other binary files can make a repository grow quickly, so avoid importing an entire camera library.

> **Screenshot placeholder — `images/06-create-private-repository.png`**  
> Show GitHub's new repository form, with name, Private visibility and README initialisation.

### Markdown: writing without committing to one application

Markdown is a lightweight way to structure plain text. A few characters indicate a title, heading, list, link or image. GitHub, VS Code, iA Writer and Obsidian can all work with Markdown, although they may display it differently.

The [GitHub Markdown formatting guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) is a useful reference for headings, emphasis, links, lists, tables and images.

Markdown is no longer limited to specialist writing applications. [Google Docs also supports Markdown](https://support.google.com/docs/answer/12014036): it can recognise selected Markdown syntax, paste or copy content as Markdown, and import and export `.md` files. Google also documents [opening and editing Markdown files in Docs without converting their file type](https://support.google.com/docs/answer/18289341). Not every Google Docs feature has a Markdown equivalent, however, so check formatting when moving a document between applications.

Create a file called `public-space.md` inside your new repository:

```markdown
# Public Space Observations

## Location

A square near the station.

## Questions

- Who uses the square in the morning?
- Which spaces are shaded?
- Where do people stop?

[RC15 Resources](https://github.com/PervasiveUrbanism/RC15-Resources)

![Sketch of the square](images/square-sketch.jpg)
```

The first line is a title, the second-level headings divide the text, dashes create a list, square brackets with a URL create a link, and an exclamation mark before a link displays an image. The image path is **relative to the Markdown file**: the example expects `images/square-sketch.jpg` next to `public-space.md` in an `images` subfolder.

The special name `README.md` is useful because GitHub automatically shows it when you open the corresponding folder. You can create a small table of contents in your repository's main README and link to individual notes.

![Markdown writing and preview](images/07.1-markdown-source-preview.png)



### Make your first commit

Edit your note, then return to GitHub Desktop. The **Changes** tab shows the files that changed; for text files, it highlights added and removed lines. Read the difference carefully. Enter a meaningful commit message, for example `Add initial public space observation`, then select **Commit to main**. This records the changes locally.

Now select **Push origin** to send the commit to GitHub. Open the repository in a browser to confirm that the file appears. If you edit the same repository from another device later, pull before making new changes.

A good commit message describes the change rather than saying `update` or `stuff`. Several small, understandable commits are often more useful than one enormous commit after weeks of work.



### Obsidian: a different way to navigate the same notes

[Obsidian](https://obsidian.md/) uses a *vault*, which is simply a local folder of Markdown notes. Open Obsidian, choose **Open folder as vault** and select your cloned personal repository. Obsidian does not replace Git: it provides writing, search, links between notes and optional graph views, while GitHub Desktop manages the version history and synchronisation.

You can link notes with syntax such as `[[Berlin Notes]]`. This is convenient inside Obsidian, but ordinary Markdown links such as `[Berlin notes](../places/berlin-notes.md)` are more portable and work on GitHub. Decide which style suits the intended audience. Obsidian also creates an `.obsidian` settings folder; review whether you want to track those preferences in Git.

You do not need a Git synchronisation plugin to start. Continue committing and pushing through GitHub Desktop. Automatic synchronisation can be added later, once you understand how changes and conflicts are handled.

![Repository opened in Obsidian](images/09-obsidian-repository-vault.png)

*How to open a folder as Obsidian Vault*

### Working with ChatGPT or Claude

An AI assistant can help you research, outline a note, improve its clarity, reorganise sections or examine inconsistencies. There are **two distinct workflows** worth understanding.

**A. Conversational co-writing.** You paste a section into ChatGPT or Claude, explain the intended audience and ask for a revision. You review the response, then copy the text back into your Markdown file. This is simple and gives you direct control over each change. It can be used without granting the assistant access to your repository.

**B. Editing with access to repository files.** Some AI environments can access a repository through a connector or by working in a local project folder. You can then request changes across multiple Markdown files. The exact capabilities depend on the application, permissions and account configuration; ordinary chat by itself does not automatically have access to files on your computer. An AI may also need explicit permission before committing or pushing. Never assume an instruction to “update GitHub” has been carried out until you inspect the repository.

For example, a useful request is:

> Read `research/public-space.md`. Improve the structure for an architecture student, preserve my observations, distinguish evidence from interpretation, and propose changes rather than inventing new facts. Tell me exactly which files you changed.

### Instructions *inside* Markdown files

You can also leave editorial directions within the document itself. HTML comments are particularly useful: they are visible in the raw Markdown file but hidden in GitHub's rendered view.

```markdown
# Notes on Public Space

<!--
EDITORIAL NOTE FOR AI REVIEW:
Keep the original observations.
Group the notes by time of day.
Do not invent sources, measurements or quotations.
Suggest changes first; do not publish automatically.
-->

## Observations

People gather along the sunny edge of the square.
```

These are **notes for a future editing process**, not commands automatically executed by GitHub. They will only influence an AI if the model is given the raw file and asked to follow them. Comments also remain in the repository's source and may be read by collaborators, so do not put secrets in them.

For repeated project-wide guidance, some AI tools support special instruction files such as `AGENTS.md` or `CLAUDE.md`. These are **tool-specific conventions**, not a universal GitHub feature. Use them only after understanding which tool reads which file and whether the instructions actually apply.

Crucially, an AI-generated revision is a proposal. Read the resulting Markdown and the Git diff. Check all claims, links and citations, and avoid automatically accepting extensive rewrites you cannot explain. Commit only changes you are satisfied with.

![Reviewing AI-assisted Markdown changes](images/10-ai-markdown-diff-review.png)

*This syntax ensures that it's not visible, but it's another way to leave more specific instructions to the LLM*

### Exercise 2 — Start a personal knowledge library

Create a private GitHub repository with a README. Add one Markdown note about a place, reading, design question or recipe, and link to it from the README. Open the repository as an Obsidian vault if you wish. Ask ChatGPT or Claude for a focused editorial suggestion, optionally using an HTML comment in the note. Review the change in GitHub Desktop, make a descriptive commit and push it.

The outcome should be a small, readable collection that is yours to develop, rather than a demonstration of how much text AI can generate.

---

## 3. Writing and editing on an iPhone

You do not need to sit in front of a desktop computer to develop a text or code project. A phone can be a convenient place to discuss an idea with an AI assistant, refine a paragraph or correct a tutorial while travelling. Much of the written material in RC15 Skills and Resources has been developed with AI assistance, partly on desktop and often on the phone. The important thing is to keep working on the same files rather than leaving successive drafts scattered between applications and chat conversations.

Two apps make this practical on iPhone. **[Working Copy](https://workingcopy.app/)** gives you a local Git repository and handles synchronisation with GitHub. It is free to download, but pushing and several other features require a paid Pro unlock; eligible students can obtain Pro features through the [GitHub Student Developer Pack](https://workingcopy.app/education/). **[iA Writer](https://ia.net/writer)** is a focused Markdown editor and a paid app on iOS. These are the tools used in this example, not the only possible mobile workflow. They serve different purposes: Working Copy manages versions, while iA Writer provides a comfortable writing environment.

A useful pattern is to discuss the structure of a tutorial with ChatGPT or Claude on your phone, open its Markdown file in iA Writer for careful editing, and use Working Copy to commit and push the result. You can continue the work later on a computer without having to reconstruct it from chat messages.

### Clone a repository in Working Copy

Install [Working Copy](https://workingcopy.app/) and sign in or authorise access to GitHub. Clone your *own* private repository using its URL or the repository picker. Make sure you can see its folders and README.

Working Copy integrates with the iOS Files app. If its location is not shown, open Files → Browse, use the options menu to edit locations and enable Working Copy. The exact labels can vary with iOS version.


### Write in iA Writer

In iA Writer, use its file browser or the Files document picker to open a Markdown file from the Working Copy location, **editing the original file in place** where supported. This avoids maintaining a separate copy that never reaches the Git repository.

Write a short addition, then return to Working Copy and examine the changes. If they do not appear, confirm that the editor really saved back into Working Copy rather than another location; you may need to use Share or Save to Working Copy depending on the app and version.

You can now commit the edit on your phone and push it to GitHub, just as you did on desktop. As explained above, pushing to a remote repository requires Working Copy Pro or an eligible educational entitlement.

A note can include links and small supporting images just as it would on a desktop. Keep photographs and other assets in the repository only when they are relevant and reasonably small; Git is not a substitute for a large media archive.

### Return to your computer

After pushing from the iPhone, open the same personal repository in GitHub Desktop on your computer and **Fetch origin**, then **Pull origin**. The updated Markdown file should appear locally. Open it in Obsidian or another editor and confirm that the changes are present.

Try the reverse direction too: edit on desktop, commit and push, then pull the latest changes in Working Copy before editing on your phone.



## Sustainable Git habits and iterative AI writing

A reliable Git routine is straightforward: **pull before beginning on another device; work in your preferred editor; review changes; commit with a meaningful message; and push when you want the updated work available elsewhere.** For shared repositories, discuss substantial restructuring before making changes that affect other contributors.

Writing with an LLM is similarly incremental. The first generated version is rarely the best one. A more effective method is to work through many small decisions and revisions, checking the result at each stage rather than asking an assistant to produce a polished final text immediately.

For example, begin by **discussing the purpose and audience** of a tutorial. What should the reader understand or be able to do? Once that is clear, agree on the **table of contents** and the sequence of ideas. Then develop an **outline for each chapter**, deciding where explanations, exercises and screenshots belong. Only after this structure has been tested should you begin writing the full text. Read it critically, improve examples, remove repetition and correct technical mistakes over several iterations.

Git helps make that process visible. You can commit a first outline, then a developed chapter, then a set of editorial corrections. The history shows how the document evolved, and it offers a way to recover earlier wording if an AI-assisted rewrite moves in the wrong direction. An HTML comment inside a Markdown file can also leave a precise instruction for the next revision, provided the AI is actually given access to that comment.

The aim is not to delegate authorship to a machine. It is to use conversation, drafting and version control to develop an argument while retaining editorial judgement. The same principle applies to coding: establish what the project is meant to achieve, divide the problem into manageable pieces, and test each change before moving on.

The wider value of GitHub lies in that combination of **portable files, recorded revisions and deliberate collaboration**. You can use different editors and different devices without losing sight of the development of your work.

## Further reading and official documentation

- [GitHub Desktop documentation](https://docs.github.com/en/desktop) — installation, cloning, commits and synchronisation
- [Cloning and forking repositories](https://docs.github.com/en/desktop/adding-and-cloning-repositories/cloning-and-forking-repositories-from-github-desktop) — local copies, forks and permissions
- [GitHub's basic Markdown syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Working Copy user guide](https://workingcopy.app/manual.html) — Git on iOS, Files integration and external editors
- [Obsidian: how notes are stored](https://obsidian.md/help/data-storage) — Markdown vaults and local files
- [VS Code custom instructions reference](https://code.visualstudio.com/docs/agents/reference/custom-instructions-reference) — examples of tool-specific AI instruction files