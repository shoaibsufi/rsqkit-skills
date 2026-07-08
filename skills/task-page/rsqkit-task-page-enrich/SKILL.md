---
name: rsqkit-task-page-enrich
description: Use this skill whenever the user wants to enrich an RSQKit task page draft with additional content from external sources — text, file attachments, web pages, or links found on those pages. Trigger when the user says things like "enrich this task page", "add content from this link", "pull in information from this attachment", "can you improve this draft using these resources?", "use this page to improve the task page", or similar. Also trigger when the user provides URLs, files, or pasted text and asks for them to be incorporated into an existing RSQKit draft. Always use this skill as an enrichment pass after rsqkit-task-page has produced a draft, or when enriching an existing task page.
---

# RSQKit Task Page Enrichment Skill

This skill performs an enrichment pass on an existing RSQKit task page draft. It takes external material — pasted text, file attachments, and/or web pages — fetches and reads that material, follows links found on those pages (one level deep only), and uses the gathered content to improve the draft.

The output is still a valid RSQKit task page. The enrichment pass does not change the format — it improves the content within it.

---

## What Enrichment Does

Enrichment improves the draft by:

- **Adding factual depth** — inserting accurate details, nuance, or context from the source material that the draft lacks.
- **Improving the Considerations section** — surfacing trade-offs, audience insights, or key points from the sources that belong there.
- **Strengthening the Solutions section** — adding actionable steps, tools, or approaches found in the sources; linking to high-quality external resources rather than reproducing them at length.
- **Replacing vague guidance with specific guidance** — if the draft says something generic that a source says more precisely, prefer the precise version.
- **Adding or improving links** — where a source is high-quality and stable, add it as a link in the appropriate section.

Enrichment does **not**:
- Change the Task → Description → Considerations → Solutions structure.
- Add content that isn't supported by the sources or existing good knowledge.
- Reproduce substantial content from external sources verbatim — summarise, frame, and link.
- Follow links from pages that the fetched pages themselves link to (one level deep only).

---

## Concision Constraints During Enrichment

Enriched output must respect the concision rules in the `rsqkit-task-page` skill: bullet budgets (4–7 Considerations, 5–8 Solutions), bullet anatomy (one insight or action, at most one supporting clause), no cross-section redundancy, no signposting sentences, and the mandatory compression pass before output.

**Word budget when this skill is invoked:** the per-block budget is **300–500 words** per H2 block (excluding code blocks and Further Reading), replacing the base 250–400 budget from `rsqkit-task-page`.
This wider budget exists only because enrichment adds source-backed material; it applies only to enrichment passes and does not change the base budget for plain drafting.
It is a ceiling, not a target — if the enriched block fits in 300 words, do not grow it to 500.

If integrating the source material would push a block past 500 words, do not exceed the budget — instead cut weaker existing content to make room, move the excess behind a link, or tell the user the block is at capacity and let them choose what to drop.

---

## One Sentence Per Line

Enriched output follows the same source-formatting convention as the rest of RSQKit: one sentence per line.
Each sentence ends with a newline, so a later edit touches one line instead of reflowing a paragraph, which keeps version-control diffs small and reviewable.

This is a source-formatting convention only — it does not change how the page reads.
A blank line still separates paragraphs; the single newlines between sentences within a paragraph are soft breaks, not paragraph breaks.
Do not put a blank line between sentences of the same paragraph, and do not collapse a multi-sentence paragraph onto one line.

When you rewrite or extend a section, apply this to the prose you add, and preserve it in prose you leave untouched — do not reflow existing one-sentence-per-line content back into wrapped paragraphs.
List items stay one point per line; headings, code blocks, and tables are unaffected; YAML front matter is exempt (handled by the metadata skill).

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

Discard:
- Content that duplicates what the draft already says well.
- Content that is off-topic, outdated, or of low quality.
- Content that would only make sense reproduced verbatim (summarise instead, or link).

### Step 4 — Integrate into the draft

Rewrite the draft sections where enrichment adds value. For each change:

- Prefer precision over length — a tighter, more accurate sentence beats a longer one.
- Add links in the Solutions section (or Considerations where appropriate) using the format: `[Link text](URL)`.
- Do not pad sections just because source material exists — only add what genuinely improves the page.
- Apply the Concision Constraints above: bullet budgets and anatomy hold, each rationale appears once, and the enriched block stays within the 300–500 word enrichment budget.
- Run the compression pass from `rsqkit-task-page` on the enriched draft before output.
- Maintain the RSQKit quality principles: the page must still be self-sufficient, accurate, and motivating.
- Keep prose one sentence per line — both in added content and in existing content you touch; do not reflow paragraphs.

### Step 5 — Output

Produce the enriched task page in full, using the standard RSQKit format. 

Optionally, provide a brief summary of what was changed and why — useful when the user wants to understand what the enrichment pass did.

---

## Quality Check After Enrichment

After integrating sources, verify the page still meets the RSQKit core principles:

- [ ] Reader can still form a correct understanding without following any links.
- [ ] No section has become bloated with content better left to external resources.
- [ ] Each H2 block is within the 300–500 word enrichment budget (excluding code).
- [ ] Bullet budgets and anatomy from `rsqkit-task-page` still hold; no bullet exceeds two sentences.
- [ ] No fact or rationale appears more than once on the page after integration.
- [ ] The compression pass has been run on the enriched draft.
- [ ] All added links point to high-quality, relevant, stable external material.
- [ ] Content is factually accurate — sources have been interpreted correctly.
- [ ] The Task → Description → Considerations → Solutions structure is intact.
- [ ] Prose is one sentence per line; no existing one-sentence-per-line content was reflowed into wrapped paragraphs.
- [ ] Added content doesn't contradict existing good content in the draft.

---

## Scope Boundaries

| In scope | Out of scope |
|---|---|
| Pasted text provided by the user | Content from links on pages linked by the fetched pages (2+ levels deep) |
| Attached files (PDF, doc, md, etc.) | Fabricating content not in the sources |
| URLs provided by the user | Changing the RSQKit page format |
| Links found on fetched pages (1 level deep, relevant only) | Reproducing external content verbatim at length |

---

## Notes

- This skill is designed to run **after** `rsqkit-task-page` has produced a draft, but can also enrich an existing published task page.
- Additional passes for **page metadata**, **internal cross-links**, and **resource vetting** are out of scope here and handled separately.
- If no source material meaningfully improves the draft, say so rather than making superficial changes.
