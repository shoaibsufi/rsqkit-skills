# Writing RSQKit Task Pages with Skills

This guide explains how to use the RSQKit task page skills to draft, refine, and prepare new task pages for submission to the [RSQKit repository](https://github.com/EVERSE-ResearchSoftware/RSQKit).

---

## What Is in This Directory

```
skills/task-page/
├── README.md                              ← this file
├── rsqkit-task-page.skill                 ← packaged skill (zip) for uploading to Claude
├── rsqkit-task-page/
│   └── SKILL.md                           ← the same skill as plain text
├── rsqkit-task-page-enrich.skill
├── rsqkit-task-page-enrich/
│   └── SKILL.md
├── rsqkit-task-page-update-tools.skill
├── rsqkit-task-page-update-tools/
│   └── SKILL.md
├── rsqkit-task-page-metadata.skill
├── rsqkit-task-page-metadata/
│   └── SKILL.md
├── rsqkit-task-page-ref-style-links.skill
├── rsqkit-task-page-ref-style-links/
│   └── SKILL.md
└── standalone/
    └── rsqkit-task-page-system-prompt.md  ← all five skills as one system prompt, for non-Claude models
```

Each skill exists in two forms that are kept in sync and contain identical content:

- **`<name>.skill`** — a zip archive that Claude accepts as an uploadable custom skill.
- **`<name>/`** — the same archive unpacked, so the content is readable and diffable on GitHub.

The unpacked folders follow the open [Agent Skills format](https://agentskills.io/) (specification at [agentskills.io/specification](https://agentskills.io/specification)): a folder containing a `SKILL.md` file whose YAML front matter carries at least a `name` and a `description`, followed by the instructions themselves. The `description` is what an agent reads to decide when to activate the skill; the body is loaded only when it does. Skills in this format may also bundle `scripts/`, `references/`, or `assets/` folders — the five task-page skills currently need only `SKILL.md`. Because it is an open format, the same folders can be used unchanged in Claude Code and any other Agent Skills–compatible tool.

### Installing

- **Claude (claude.ai / desktop / mobile):** upload the `.skill` file as a custom skill.
- **Claude Code or another Agent Skills–compatible agent:** point it at the unpacked folder (or copy the folder into the agent's skills directory).

### Editing a skill

Edit the `SKILL.md` in the unpacked folder, then rebuild the archive from the parent directory so the internal path is preserved:

```bash
cd skills/task-page
rm rsqkit-task-page.skill
zip -r rsqkit-task-page.skill rsqkit-task-page/
```

Commit both the folder and the rebuilt `.skill` together so they stay in sync.

---

## The Skills

There are five skills in the RSQKit task page family. They are designed to be used in sequence, though some steps are optional depending on your needs.

| Skill | What it does |
|---|---|
| `rsqkit-task-page` | Writes or reviews a task page — structure, voice, length, Further Reading, and AI Disclosure |
| `rsqkit-task-page-enrich` | Enriches a draft with content from URLs, attachments, or pasted text |
| `rsqkit-task-page-update-tools` | Replaces plain Markdown tool links with `{% tool "id" %}` tags and suggests registry entries for unknown tools |
| `rsqkit-task-page-metadata` | Generates the YAML front matter block for the top of the page file |
| `rsqkit-task-page-ref-style-links` | Converts the remaining inline links to reference style, with an alphabetised definition block at the foot of the page |

### Recommended workflow

```
1. rsqkit-task-page                  — write the draft
2. rsqkit-task-page-enrich           — (optional) deepen with external sources
3. rsqkit-task-page-update-tools     — replace tool links with tool tags
4. rsqkit-task-page-metadata         — generate the front matter
5. rsqkit-task-page-ref-style-links  — convert the remaining links to reference style
```

Steps 2 and 3 can be swapped. Step 5 must come after steps 2 and 3 — tool links need to have become tool tags first, and any links added by enrichment need to exist so they are converted too. Steps 4 and 5 can be swapped: metadata touches only the front matter and the link conversion touches only link syntax, so neither disturbs the other.

---

## What the Skills Enforce

The skills encode the RSQKit conventions, so the output will look like this whether or not you ask for it. Knowing the rules up front makes reviewing the output easier.

**Structure.** Each task is an H2 heading phrased as a question to the reader (`## How do you …?`), followed by three H3 sections: `### Description`, `### Considerations`, `### Solutions`. The default is a single H2 block. The skill adds a second block only when each sub-task is independently substantial enough to justify a full Description, Considerations, and Solutions of its own; a thin sub-task is merged into its neighbour. The page ends with `## Further Reading` and then `## AI Disclosure`, both H2.

**Voice and tone.** Second person throughout ("you", "your"). Professional, direct, and approachable — like a knowledgeable colleague — but not casual: no chattiness, preambles, or reassurance softeners.

**One sentence per line.** Body prose is written with each sentence on its own line in the Markdown source, with blank lines only between paragraphs. This keeps Git diffs small. It does not affect how the page renders, provided the site uses Kramdown with `hard_wrap: false` (an RSQKit `_config.yml` setting, not something the skills control). List items are already one per line (one point per bullet, never split across lines); headings, code blocks, tables, and the YAML front matter are unaffected.

**Length.** The skills are deliberately tight. Each H2 block is budgeted at 250–475 words (excluding code and Further Reading); Description is 2–4 sentences; Considerations is 4–7 bullets; Solutions is 5–8 bullets; each bullet is one idea with at most one supporting clause. After drafting, the skill runs a mandatory compression pass that aims to cut 20–30% before showing you the result. If your team wants longer or shorter pages, the per-block word budget in `rsqkit-task-page/SKILL.md` is the main lever to adjust.

**Honest scope.** Where readers are likely to overestimate what a practice achieves, the Description states plainly what it does not guarantee — but only where that misunderstanding is genuinely likely, not as a routine disclaimer, and within the 2–4 sentence budget.

**Links.** The draft uses plain `[text](URL)` Markdown everywhere — no backticks inside link text, no nested links, no raw URLs as link text. The final step converts these to reference style (`[text][label]`) with the URLs collected at the foot of the page; see step 5.

**Further Reading.** 3–5 entries, practical and tool-focused resources first, papers and books last. Each entry is `**[Title](URL)** — one or two sentences on why it is worth the reader's time`.

**AI Disclosure.** Every page ends with a fixed sentence naming the Claude model used, for example:

> This work was produced with the assistance of Claude Sonnet 4.6, under the strict editorial control and factual verification of the human author.

If the skill cannot tell which model is active it will ask you. Check the model name is right before submitting.

**Tool-focused pages.** If the page is mainly about a specific tool, Solutions must include a minimal concrete example (a command or snippet), explicit prerequisites, and a note on when the tool is not the right choice.

**Hedged claims.** Adoption and consensus claims are softened ("widely used", "common practice") unless a source is given.

---

## Step-by-Step Guide

### Step 1 — Write the draft

Start a **new conversation** in Claude. Starting fresh keeps the context small and the cost low.

Give Claude a topic and ask it to write a task page. For example:

> "Write an RSQKit task page on how to use software containers for reproducible research."

Claude will use the `rsqkit-task-page` skill to produce a page following the conventions above, including Further Reading and AI Disclosure.

**Review the draft.** Check that the content is accurate and the balance between sections feels right. Ask Claude to adjust anything that doesn't read well or is missing something important. You can also paste in an existing page and ask for a review against the RSQKit format — the skill contains a full review checklist.

---

### Step 2 — Enrich the draft (optional)

If you have useful source material — a URL, an attached document, a paper, or pasted text — ask Claude to enrich the draft:

> "Enrich this draft using the content at [URL]."

or

> "Can you improve this draft using the attached PDF?"

Claude will fetch the URL, read the content, follow relevant links one level deep (and no further), and weave useful material into the draft without changing its structure. Ask for a summary of what changed and why if you want one.

Enrichment widens the per-block budget to 350–650 words, but treats that as a ceiling, not a target. If the source material would push a block past 650 words, Claude will cut weaker existing content, move the excess behind a link, or ask you what to drop rather than exceed it.

This step is particularly useful when:
- A topic has authoritative community guidance you want reflected
- You want to add more specific tool recommendations from a known resource
- The draft feels thin on practical detail

---

### Step 3 — Replace tool links with tool tags

Ask Claude to update the tool links:

> "Update the tool links in this page."

Claude will scan every Markdown link in the page and compare it against the tools registry embedded in the skill (a snapshot of `_data/tool_and_resource_list.yml`), matching by URL first, then by name, then conservatively by description. Links that match a registered tool are replaced with:

```
{% tool "tool-id" %}
```

The tag replaces the whole link, including the link text, because the site renders the tool's name from the registry.

Links in the **Further Reading** section and internal links to other RSQKit pages are left as they are — they are references, not tool tags. The substitution preserves the one-sentence-per-line layout so the diff stays small.

Claude will also report:
- **What was replaced** — a list of every substitution made
- **What was left as a plain link** — non-tool references (papers, standards, project sites, concept pages)
- **Potential new tool entries** — links that look like tools but aren't in the registry yet, with suggested YAML entries you can add to `_data/tool_and_resource_list.yml`

Claude never emits a tool tag for an `id` that isn't in the registry — it only suggests the YAML.

__If Claude suggests new tool entries, copy the suggested YAML and add it to `_data/tool_and_resource_list.yml` in your RSQKit repository fork (or branch) before submitting your page as a pull request.__ (otherwise the site will not build)

If you have a newer copy of `tool_and_resource_list.yml` than the skill's snapshot, attach it and Claude will use that instead.

---

### Step 4 — Generate the front matter

Ask Claude to generate the page metadata:

> "Can you suggest page metadata for this task page?"

Claude will produce a YAML block ready to paste at the top of your page file, covering:

- `title` — noun-phrase version of the task question (not the question itself)
- `description` — 1–2 sentence summary in third person, for tile/card views
- `contributors` — left as `[]` for you to fill in
- `page_id` — a unique lowercase slug with underscores, checked against the existing page IDs
- `related_pages` — 2–5 `page_id`s of related RSQKit task pages, chosen using content summaries of every existing page (not just title similarity)
- `quality_indicators` — indicator slugs (the `abbreviation` field from `quality_indicators.yml`), chosen conservatively
- `keywords` — 3–8 lowercase search terms

Front matter is standard YAML — one key per line — and is exempt from the one-sentence-per-line rule.

**Review the suggestions carefully**, particularly:

- `related_pages` — the skill only references pages from its embedded list, but that list is a dated snapshot; check that the IDs exist and consider any pages added since
- `quality_indicators` — check that the indicators listed are genuinely satisfied by following this page's guidance
- `contributors` — add your name (and any co-authors) as it appears in `_data/CONTRIBUTORS.yml`

The skill does not generate `child_pages` or `search_exclude`. If your page is a parent of other task pages, add `child_pages: [...]` yourself following `pages/tasks/TEMPLATE_task.md` in the RSQKit repository.

---

### Step 5 — Convert the remaining links to reference style

Ask Claude to tidy the links:

> "Convert the links to reference style."

Every inline link still on the page — in the body, in Further Reading, and internal links to other RSQKit pages — is converted from `[text](url)` to `[text][label]`, and the URLs are collected into a single definition block at the very bottom of the file, after the AI Disclosure:

```
Before: Follow the [README guidelines](https://example.org/readme-guide) when writing documentation.
After:  Follow the [README guidelines][readme-guide] when writing documentation.

At the bottom of the document:
[readme-guide]: https://example.org/readme-guide
```

The rules the skill applies:

- The visible link text is never changed — only the syntax around it.
- Labels are 5–20 characters, lowercase, hyphen-separated, and readable (`readme-guidelines`, not `rdme-gdl`). One label per URL, reused wherever that URL appears; collisions are disambiguated.
- Always the explicit two-bracket form `[text][label]`; never the shortcut forms `[label][]` or bare `[label]`.
- Definitions are one per line, alphabetical by label, with no heading above them (reference definitions are invisible when rendered, so a heading would render with nothing under it).
- Tool tags, image links, code blocks, inline code, and the YAML front matter are left alone.
- Line structure is preserved, so the diff shows only the converted links plus the new definition block.

Claude verifies that every label used has exactly one definition and every definition is used, then reports what was converted, which labels were reused, and what was left unchanged.

---

## Assembling the Final Page File

Once you have all the pieces, assemble them in this order:

```
[YAML front matter]
---
[page content, ending with Further Reading then AI Disclosure]
[reference-link definitions]
```

A complete page file looks like this (body prose shown one sentence per line, as the skills produce it):

```markdown
---
title: "Using software containers for reproducible research"
description: "How to use containers such as Docker and Apptainer to create reproducible software environments for research."
contributors: ["Your Name"]
page_id: using_containers
related_pages:
  tasks: [reproducible_software_environments, ci_cd, structuring_software_projects]
quality_indicators: [software_is_containerized]
keywords: ["containers", "docker", "apptainer", "reproducibility", "software environments"]
---

## How do you use software containers to make your research software reproducible?

### Description

Containers package your software together with the exact environment it needs to run.
This lets you and your collaborators run the same code on different machines and get the same result.

### Considerations

- ...

### Solutions

- Start from an official base image for your language, and pin its version.
- Build the image with {% tool "docker" %} or {% tool "apptainer" %}, following the [Docker documentation][docker-docs] for writing the build file.
- ...

## Further Reading

- **[Apptainer][apptainer-site]** — Why this resource is worth the reader's time.

## AI Disclosure

This work was produced with the assistance of Claude Sonnet 4.6, under the strict editorial control and factual verification of the human author.

[apptainer-site]: https://apptainer.org/
[docker-docs]: https://docs.docker.com/
```

---

## What Goes Where in the RSQKit Repository

Once your page file is ready, here is where each piece belongs in the [RSQKit GitHub repository](https://github.com/EVERSE-ResearchSoftware/RSQKit):

### The task page file

**Location:** `pages/tasks/`

**Filename:** `[page_id].md` — e.g. `using_containers.md`

The file goes in `pages/tasks/` alongside the other task pages. Name the file after the `page_id` in the front matter. (A few older pages have filenames that differ from their `page_id`; the `page_id` is what other pages reference, so keep the two identical for new pages.)

### New tool entries (if any)

**Location:** `_data/tool_and_resource_list.yml`

If the tool update step produced suggested YAML entries for tools not yet in the registry, add them to this file. Each entry follows this format:

```yaml
- id: tool-id
  name: Tool Name
  description: >-
    A short description of what the tool does.
  url: 'https://tool-homepage.example.com/'
  catalog: RSQKit
```

Add new entries at the end of the file. The `catalog` value should be `RSQKit` for tools you are adding as part of RSQKit content work.

### Your contributor entry (if you are new to RSQKit)

**Location:** `_data/CONTRIBUTORS.yml`

If your name is not already listed, add an entry. The minimum required fields are your full name and GitHub username:

```yaml
Your Full Name:
  git: your-github-username
  orcid: 0000-0000-0000-0000   # optional but encouraged
  role: author
  affiliation: Your Institution
```

---

## Submitting to RSQKit

RSQKit uses a standard GitHub pull request workflow.

1. Fork the [RSQKit repository](https://github.com/EVERSE-ResearchSoftware/RSQKit)
2. Create a branch for your new page
3. Add your page file to `pages/tasks/`
4. Add any new tool entries to `_data/tool_and_resource_list.yml`
5. Add your contributor entry to `_data/CONTRIBUTORS.yml` if needed
6. Open a pull request against the `main` branch
7. The RSQKit Editorial Board will review and provide feedback

See the [RSQKit Contribution Guidelines](https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/pages/contributing/contribution_guidelines.md) for more detail on the review process.

---

## Tips for Getting the Best Results

**Use a fresh conversation for each page.** The skills work best with a clean context. Long conversations with many files and prior exchanges are more expensive and can produce slightly less consistent output.

**Be specific about the topic.** The more precisely you describe the task, the better the draft. "How do you choose a software licence for research software?" will produce a better result than "software licences".

**Expect a tight page.** The skills are built to cut, not to pad. If a first draft feels too short, ask for specific additions ("add a bullet on X to Considerations") or run the enrich step with a source, rather than asking for "more" in general.

**Expect one block unless the topic really has two tasks.** The drafting skill now defaults to a single H2 block. If you believe the topic genuinely has distinct sub-tasks, say so in the prompt and explain what they are.

**Iterate on content before running later skills.** Get the draft right before running the tool update, metadata, and link conversion steps — it avoids having to redo those passes if the content changes significantly.

**Check the Further Reading links.** The skills suggest well-regarded resources, but verify that links are still live, that the resources are still current, and that references to sections are accurate before submitting. Once links are reference-style, the URLs to check are all in one block at the foot of the page.

**Review quality indicators carefully.** The metadata skill suggests indicators conservatively, but you should confirm each one is genuinely satisfied by a reader following the page's guidance.

**Check the AI Disclosure model name.** It should name the model you actually used.

---

## Keeping the Skills Up to Date

Two skills embed snapshots of RSQKit data files, and each snapshot is dated inside the skill:

- `rsqkit-task-page-update-tools` embeds the tools registry from `_data/tool_and_resource_list.yml`.
- `rsqkit-task-page-metadata` embeds the list of existing task pages (with a one-line content summary of each, used to pick `related_pages`) and the quality indicators from `_data/quality_indicators.yml`.

When those files change in the RSQKit repository, or when new task pages are merged, provide the updated files to Claude and ask it to regenerate the relevant table in the skill. Then rebuild the `.skill` archive as described above and commit both forms. In the meantime, attaching a current copy of the data file to a conversation makes the skill use that instead of its snapshot.

Whenever any of the five `SKILL.md` files changes, update the standalone system prompt to match.

---

## Use with Other Than Claude

`standalone/rsqkit-task-page-system-prompt.md` consolidates all five skills into a single, model-agnostic system prompt. Paste it into any capable instruction-following model and give it a topic (and optionally source material). It runs the whole pipeline in one pass — draft, enrich (skipped if no sources are given), tool tags, metadata, reference-style links — and returns the complete page file plus the tool-tag and link-conversion summaries and a list of open items for you (empty `contributors`, model name to confirm, proposed registry entries to review, anything dropped for budget reasons). If you ask for just one stage ("add metadata to this page"), it runs only that stage.

In practice, less capable models sometimes need a nudge to run a step they know about but skipped.
