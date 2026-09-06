---
name: rsqkit-task-page-ref-style-links
description: Use this skill whenever the user wants to convert inline Markdown links on an RSQKit task page to reference-style links. Trigger when the user says things like "convert links to reference style", "move the URLs to the bottom", "tidy up the links", "make the links reference-style", "add link definitions at the end", or any similar phrasing. Also trigger when the user wants link definitions collected, deduplicated, or alphabetised at the bottom of a page. Always use this skill after rsqkit-task-page-update-tools has run (so tool links have already become tool tags), and after any rsqkit-task-page-enrich pass (so newly added links are also converted). Order relative to rsqkit-task-page-metadata is flexible, since that skill touches only the front matter.
---

# RSQKit Task Page Reference-Style Links Skill

This skill converts the remaining inline Markdown links on an RSQKit task page to reference-style links, collecting all link definitions in an alphabetised block at the bottom of the document.

It runs after `rsqkit-task-page-update-tools`, so tool links have already been replaced with `{% tool "id" %}` tags — everything left as `[text](url)` is a candidate for conversion.

---

## What This Skill Does

1. **Scans** the task page for all remaining inline links: `[text](url)`
2. **Converts** each to the explicit reference form: `[text][label]`
3. **Generates** a meaningful label for each distinct URL
4. **Collects** all `[label]: url` definitions in a single block at the bottom of the document, in alphabetical order by label
5. **Outputs** the updated page and a summary of conversions

---

## Link Form

Always use the explicit two-bracket form, preserving the original hyperlinked text:

```
Before: Follow the [README guidelines](https://example.org/readme-guide) when writing documentation.
After:  Follow the [README guidelines][readme-guide] when writing documentation.

At the bottom of the document:
[readme-guide]: https://example.org/readme-guide
```

**Never use the implicit shortcut forms** `[label][]` or bare `[label]`. Because the hyperlinked text is preserved verbatim, the label always appears explicitly in the second bracket pair, even when the text and label happen to match.

Omit the optional `"title"` attribute in definitions unless the user asks for titles.

---

## Label Rules

- **Length:** 5–20 characters.
- **Style:** lowercase words separated by hyphens, derived from the link text or destination.
- **Meaningful over terse:** err on the side of readability — `[readme-guidelines]` not `[rdme-gdl]`. Abbreviate only when needed to stay within 20 characters, and keep the result recognisable.
- **Case consistency:** labels are case-insensitive in Markdown, but usage and definition must use identical casing. If the body uses `[text][readme-guide]`, the definition is `[readme-guide]:` — never `[Readme-Guide]:`.
- **One label per URL:** if the same URL is linked more than once, reuse the same label everywhere and emit a single definition.
- **No collisions:** if two different URLs would produce the same label, disambiguate with a distinguishing word (e.g. `[cff-spec]` and `[cff-tutorial]`), still within 20 characters.

---

## Definition Block

Place all definitions at the very bottom of the document, after all content (including Further Reading and the AI Disclosure), separated from the preceding content by one blank line:

```
[cff-spec]: https://citation-file-format.github.io/
[readme-guide]: https://example.org/readme-guide
[ssi-website]: https://www.software.ac.uk/
```

- One definition per line.
- Alphabetical order by label.
- No heading above the block — reference definitions are invisible when rendered, and a heading would render with nothing under it.

---

## Process

### Step 1 — Extract inline links
Find every inline link `[text](url)` in the page body. Skip the YAML front matter, fenced code blocks, and inline code spans.

### Step 2 — Handle existing reference-style links
If the page already contains reference-style links, keep them but normalise them to comply with this skill: expand any `[label][]` or bare `[label]` shortcut forms to the explicit `[text][label]` form, bring labels within the label rules, and merge their definitions into the single alphabetised block.

### Step 3 — Generate labels
Assign each distinct URL a label following the Label Rules. Deduplicate by URL first, then check for label collisions.

### Step 4 — Apply conversions
Replace each `[text](url)` with `[text][label]`, leaving the hyperlinked text untouched.

### Step 5 — Append the definition block
Add the alphabetised `[label]: url` block at the bottom of the document.

### Step 6 — Verify
Check that: every label used in the body has exactly one definition; every definition is used at least once; no `[label][]` or bare `[label]` shortcut form remains; usage and definition casing match; definitions are in alphabetical order.

### Step 7 — Output

Produce two outputs:

**A) The updated page** — the full task page with reference-style links and the definition block.

**B) A summary of conversions**, in this format:

```
Converted:
- [README guidelines](https://example.org/readme-guide) → [README guidelines][readme-guide]
- [Citation File Format](https://citation-file-format.github.io/) → [Citation File Format][cff-spec]

Reused labels (same URL linked more than once):
- [readme-guide] × 3

Left unchanged:
- ![workflow diagram](images/workflow.png) — image, left inline
- {% tool "ruff" %} — tool tag, not a link
```

---

## Important Constraints

- **Preserve the hyperlinked text exactly.** Conversion changes only the link syntax, never the visible text.
- **Do not touch tool tags.** `{% tool "id" %}` tags are not links and must pass through unchanged.
- **Leave image links inline.** Do not convert `![alt](url)` unless the user explicitly asks.
- **Skip front matter, code blocks, and inline code.** Link-like text in these regions is not a link.
- **Preserve the page's line structure.** RSQKit body content is written one sentence per line — replace only the link tokens in place; do not reflow, rewrap, or merge prose. The diff should show only the converted links plus the new definition block.
- **Convert internal RSQKit links too.** Relative links to other RSQKit pages are still inline links and convert the same way, unless the user asks to leave them.
- **Never emit an unused or missing definition.** The Step 6 verification is mandatory before output.
