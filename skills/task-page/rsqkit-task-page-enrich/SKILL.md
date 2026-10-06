---
name: rsqkit-task-page-enrich
description: Use this skill whenever the user wants to enrich an RSQKit task page draft with additional content from external sources — text, file attachments, web pages, or links found on those pages. Trigger when the user says things like "enrich this task page", "add content from this link", "pull in information from this attachment", "can you improve this draft using these resources?", "use this page to improve the task page", or similar. Also trigger when the user provides URLs, files, or pasted text and asks for them to be incorporated into an existing RSQKit draft. Always use this skill as an enrichment pass after rsqkit-task-page has produced a draft, or when enriching an existing task page.
---

# RSQKit Task Page Enrichment Skill

This skill performs an enrichment pass on an existing RSQKit task page draft. It takes external material — pasted text, file attachments, and/or web pages — fetches and reads that material, follows links found on those pages (one level deep only), and uses the gathered content to improve the draft.

The output is still a valid RSQKit task page. The enrichment pass improves the content within the RSQKit format. It may add a new H2 block only under the conditions in **Adding a Block** below.

---

## What Enrichment Does

Enrichment improves the draft by:

- **Adding factual depth** — inserting accurate details, nuance, or context from the source material that the draft lacks.
- **Improving the Considerations section** — surfacing trade-offs, audience insights, or key points from the sources that belong there.
- **Strengthening the Solutions section** — adding actionable steps, tools, or approaches found in the sources; linking to high-quality external resources rather than reproducing them at length.
- **Replacing vague guidance with specific guidance** — if the draft says something generic that a source says more precisely, prefer the precise version.
- **Adding or improving links** — where a source is high-quality and stable, add it as a link in the appropriate section.

Enrichment does **not**:
- Change the Description → Considerations → Solutions structure within a block, or add an H2 block except as described in **Adding a Block**.
- Add content that isn't supported by the sources or existing good knowledge.
- Reproduce substantial content from external sources verbatim — summarise, frame, and link.
- Follow links from pages that the fetched pages themselves link to (one level deep only).

---

## Concision Constraints During Enrichment

Enriched output must respect the concision and readability rules in the `rsqkit-task-page` skill: its bullet budgets and bullet anatomy, its redundancy rule, its sentence-length guidance, its Readability and flow rules, its concept inventory, and its mandatory compression pass.
Do not copy those rules or their numbers into this skill; refer to `rsqkit-task-page` so the two skills cannot drift apart.

**Word budget when this skill is invoked:** the per-block budget is **350–650 words** per H2 block (excluding code blocks and Further Reading), replacing the base 250–475 budget from `rsqkit-task-page`.
This wider budget exists only because enrichment adds source-backed material; it applies only to enrichment passes and does not change the base budget for plain drafting.
It is a ceiling, not a target — if the enriched block fits in 350 words, do not grow it to 650.
Use any extra room to explain points more clearly, not to add more points or to pack more into each sentence.

**Page ceiling for multi-block pages:** try to keep the enriched page within the base page budget from `rsqkit-task-page`.
Going above it, up to 2,400 words of body text, is allowed but best avoided.
Never exceed 2,400 words.

If integrating the source material would push a block past 650 words, or the page past 2,400 words, do not exceed the budget and do not make the text denser to fit — instead cut weaker existing content to make room, move the excess behind a link, or tell the user the block or page is at capacity and let them choose what to drop.

---

## Adding a Block

Enrichment keeps the Description → Considerations → Solutions structure within each block.
It may add a new H2 block only if all of these hold:

- The source material meets the split rule in `rsqkit-task-page`: readers would arrive with a different question, and it needs its own evidence, trade-offs and actions.
- The page stays within the page ceiling above.
- The user confirms before the block is written.

When proposing a block, give its "How do you…" heading, one sentence on what it would cover, and its estimated length, then wait for the user's answer.

---

## One Sentence Per Line

Enriched output follows the same source-formatting convention as the rest of RSQKit: one sentence per line.
Each sentence ends with a newline, so a later edit touches one line instead of reflowing a paragraph, which keeps version-control diffs small and reviewable.

This is a source-formatting convention only — it does not change how the page reads.
A blank line still separates paragraphs; the single newlines between sentences within a paragraph are soft breaks, not paragraph breaks.
Do not put a blank line between sentences of the same paragraph, and do not collapse a multi-sentence paragraph onto one line.

When you rewrite or extend a section, apply this to the prose you add, and preserve it in prose you leave untouched — do not reflow existing one-sentence-per-line content back into wrapped paragraphs.
In a bullet with more than one sentence, put each sentence on its own line, indented to align with the bullet text, so it continues the same bullet; follow the List Formatting rule in `rsqkit-task-page` for markers and blank lines. Headings, code blocks, and tables are unaffected; YAML front matter is exempt (handled by the metadata skill).

Note: this assumes the site renders a single newline as a space (Kramdown `hard_wrap: false`); Jekyll's default GFM processor hard-wraps single newlines, which is a site `_config.yml` setting, not something this skill controls.

## Enrichment Process

### Step 1 — Establish the baseline draft

Identify the current RSQKit task page draft. This may be:
- The output of the most recent `rsqkit-task-page` skill run in this conversation.
- A draft pasted in by the user.
- A draft in an attached file.

If no draft is clearly identifiable, ask the user to provide or confirm it before proceeding.

### Step 2 — Gather source material

Collect all provided sources:

**Pasted text** — Use as-is. Note the origin if the user has described it.

**File attachments** — Read any attached files (PDFs, docs, markdown, etc.). Extract relevant content.

**Web pages (URLs)** — Fetch each URL provided by the user using the web fetch tool. Read the full page content.

**One level of links** — From each fetched web page, identify links that look relevant to the task page topic. Fetch those linked pages too. Do not follow links from those second-level pages — stop there.

> **Link relevance filter**: Only follow links that are plausibly relevant to the task page topic. Skip navigational links, unrelated content, login pages, and anything that looks like it won't add value. Use judgement — the goal is depth on the topic, not exhaustive crawling.

### Step 3 — Extract relevant content

From all gathered material, identify:

- Facts, definitions, or explanations that add depth to the Description.
- Insights, trade-offs, audience considerations, or key points for the Considerations section.
- Actionable steps, tools, methods, or approaches for the Solutions section.
- High-quality resources worth linking to directly.

Compare the source material with the page's concept inventory (from `rsqkit-task-page`; if the draft has none, build one from the draft first).
List any insight in the sources that the page lacks, and propose adding it to the inventory.
Show the user the proposed additions.

Discard:
- Content that duplicates what the draft already says well.
- Content that is off-topic, outdated, or of low quality.
- Content that would only make sense reproduced verbatim (summarise instead, or link).

### Step 4 — Integrate into the draft

Rewrite the draft sections where enrichment adds value. For each change:

- Prefer precision, but not at the cost of readability. Follow the Readability and flow rules in `rsqkit-task-page`: one point per sentence, connecting words kept, normal grammar. Do not make a sentence more precise by packing more into it, and keep the average sentence length within the range set in `rsqkit-task-page`.
- Add links in the Solutions section (or Considerations where appropriate) using the format: `[Link text](URL)`.
- Do not pad sections just because source material exists — only add what genuinely improves the page.
- Apply the Concision Constraints above: the bullet budgets, bullet anatomy, redundancy rule and sentence-length guidance from `rsqkit-task-page` hold, each block stays within the 350–650 word enrichment budget, and the page stays within its ceiling.
- Run the compression pass from `rsqkit-task-page` on the enriched draft before output.
- Maintain the RSQKit quality principles: the page must still be self-sufficient, accurate, and motivating.
- Keep prose one sentence per line — both in added content and in existing content you touch; do not reflow paragraphs.

### Step 5 — Output

Produce the enriched task page in full, using the standard RSQKit format. 

Optionally, provide a brief summary of what was changed and why — useful when the user wants to understand what the enrichment pass did. The summary lists which concept inventory items were added and which existing content was cut to make room.

---

## Quality Check After Enrichment

After integrating sources, verify the page still meets the RSQKit core principles:

- [ ] Reader can still form a correct understanding without following any links.
- [ ] No section has become bloated with content better left to external resources.
- [ ] Each H2 block is within the 350–650 word enrichment budget (excluding code).
- [ ] A multi-block page is within 2,400 words of body text, and preferably within the base page budget from `rsqkit-task-page`.
- [ ] Added content follows the Readability and flow rules in `rsqkit-task-page`; the enriched text is no denser than the draft it started from.
- [ ] Bullet budgets and anatomy from `rsqkit-task-page` still hold.
- [ ] The redundancy rule from `rsqkit-task-page` holds: within a block each fact or rationale appears once, and nothing is repeated in three or more blocks.
- [ ] Every item in the concept inventory is still present, including any added in this pass.
- [ ] Any readability scores reported before enrichment have not worsened, unless the added content explains it.
- [ ] Any new H2 block was confirmed by the user before it was written.
- [ ] The compression pass has been run on the enriched draft.
- [ ] All added links point to high-quality, relevant, stable external material.
- [ ] Content is factually accurate — sources have been interpreted correctly.
- [ ] Each block keeps the Description → Considerations → Solutions structure.
- [ ] Prose is one sentence per line; no existing one-sentence-per-line content was reflowed into wrapped paragraphs.
- [ ] Added content doesn't contradict existing good content in the draft.

---

## Scope Boundaries

| In scope | Out of scope |
|---|---|
| Pasted text provided by the user | Content from links on pages linked by the fetched pages (2+ levels deep) |
| Attached files (PDF, doc, md, etc.) | Fabricating content not in the sources |
| URLs provided by the user | Changing the RSQKit page format (adding a block is allowed only as described in Adding a Block) |
| Links found on fetched pages (1 level deep, relevant only) | Reproducing external content verbatim at length |

---

## Notes

- This skill is designed to run **after** `rsqkit-task-page` has produced a draft, but can also enrich an existing published task page.
- Additional passes for **page metadata**, **internal cross-links**, and **resource vetting** are out of scope here and handled separately.
- If no source material meaningfully improves the draft, say so rather than making superficial changes.
