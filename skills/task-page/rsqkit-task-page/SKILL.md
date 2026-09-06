---
name: rsqkit-task-page
description: "Use this skill whenever the user wants to write, draft, improve, review, or quality-assure an RSQKit task page. Trigger when the user mentions RSQKit, asks to write or review a task page, asks for help with a task-description-considerations-solutions structure, or is working on content about research software quality. Also trigger when the user says things like \"help me write a page about X for RSQKit\", \"can you review this task page?\", \"draft the considerations section for this RSQKit task\", \"does this follow the RSQKit format?\", or any similar phrasing. Always use this skill when working on RSQKit content."
---

# RSQKit Task Page Skill

RSQKit task pages are structured guidance pages that help researchers and research software engineers understand and act on research software quality topics. Each page must be accurate, self-contained enough to be useful on its own, and motivate readers to learn more.

---

## Core Principles

Every RSQKit task page must satisfy these quality criteria:

1. **Clarity of purpose** — The reader must immediately understand why the topic matters and why this task is important for research software quality.
2. **Accuracy** — Content must be factually correct and reflect current good practices in research software.
3. **Self-sufficiency** — If external links are not followed, the page still gives the correct impression and enough guidance to apply the information correctly.
4. **Appropriate depth** — Provide a conceptual overview and practical guidance. If a topic is well-covered by high-quality external material, point to it rather than duplicating it.
5. **Motivation to learn more** — Link out to high-quality external documentation, standards, training materials, or community guidance.
6. **Correct overall impression** — A reader leaving the page without following any links should have an accurate mental model of the task and how to approach it.
7. **Concision** — The page should be the shortest version that still leaves a correct impression. Self-sufficiency means correct, not comprehensive. When in doubt, cut and link.

---

## Voice and Tone

All RSQKit task pages are written in the **second person** ("you", "your"). Address the reader directly throughout — in the Task heading, the Description, the Considerations bullets, and the Solutions steps. This is the established convention for RSQKit pages.

Examples:
- ✓ "How do you use static analysis to improve the quality of your research software?"
- ✗ "How to use static analysis to improve research software quality"
- ✓ "When you are working on research software where correctness is critical..."
- ✗ "For research software where correctness is critical..."
- ✓ "You and your team should agree on which rules to enable."
- ✗ "Teams should agree on which rules to enable."

The tone is professional, direct, and approachable — it should read like a knowledgeable colleague explaining something to you at your desk: someone who knows the material, respects your time, and wants you to actually act on it.

**Approachable means:** plain vocabulary in place of jargon, with a brief gloss when a technical term is unavoidable; acknowledging when something is genuinely hard or involves a real trade-off, rather than presenting every step as trivial; and phrasing that reads as helpful rather than clipped or bureaucratic.

**Approachable does not mean casual, and does not mean longer.** Avoid slang, chattiness, conversational preambles ("Let's dive in", "Now for the fun part"), and reassurance softeners ("don't worry", "it's actually quite simple"). These add words without adding value and pull the page towards marketing or hand-holding, both of which it must avoid. Approachability is a matter of word choice and framing, not word count — it must not lengthen the page or relax the no-padding rules elsewhere in this skill.

Examples:
- ✓ "Static analysis can feel noisy at first — you will often see more warnings than real problems. Start with a small rule set and expand it as you go."
- ✗ "Don't worry if static analysis feels overwhelming at first! It's totally normal and everyone goes through this. Let's walk through it together."
- ✓ "Choose a linter that fits your language and team. If you are unsure, start with a widely used option for your stack and adjust later."
- ✗ "Picking a linter is honestly one of the trickiest parts, but stick with us and we'll get there!"

---

## One Sentence Per Line

Write body content with one sentence per line.
Each sentence ends with a newline in the source, so editing or adding a sentence changes a single line instead of reflowing a whole paragraph.
This keeps version-control diffs small and easy to review.

This is a source-formatting convention only — it does not change how the page reads.
A blank line still separates paragraphs.
The single newlines between sentences within a paragraph are soft breaks, not paragraph breaks: do not put a blank line between sentences that belong to the same paragraph, and do not collapse a multi-sentence paragraph back onto one line.

Scope:
- Applies to all prose — the optional sentence under the Task heading, the Description, and any sentence-level body text.
- List items are already one per line: keep one point per bullet, and do not split a single bullet across lines.
- Headings, code blocks, tables, and link-reference lines are unaffected.
- YAML front matter is exempt and is handled by the metadata skill (one key per line; values are not split by sentence).

Note: this assumes the site renders a single newline as a space rather than a forced break — i.e. Kramdown `hard_wrap: false` (or the non-GFM parser).
Jekyll's default GFM processor hard-wraps single newlines, which would render each sentence on its own line; that is a site `_config.yml` setting, not something this skill controls.

## Link Formatting

**All links must use simple standard Markdown link syntax — no exceptions:**

```
[Link text](URL)
```

Link text should be descriptive and human-readable: a tool name, a document title, or a short phrase. Never use backticks inside link text, and never nest a link inside another link.

- ✓ `[ruff](https://docs.astral.sh/ruff/)`
- ✓ `[Ruff documentation](https://docs.astral.sh/ruff/)`
- ✓ `[pre-commit](https://pre-commit.com/)`
- ✗ backtick-wrapped text inside a link: the backticks belong outside or not at all
- ✗ a link nested inside another link: one URL, one label, one pair of brackets

This rule applies everywhere on the page — Solutions bullets, Considerations, Further Reading entries, and body text. Never expose raw URLs as link text; always use a human-readable label.

---

## Page Format

RSQKit task pages use a repeating structure. Each task or sub-task substantial enough to stand on its own gets its own block of four headings. Repeat the full block for an additional sub-task only when it is independently substantial (see "When to split into sub-tasks" below); otherwise keep the page to a single block. Every page also ends with a **Further Reading** section.

**Length budget:** aim for 250–475 words per H2 block, excluding code blocks and the Further Reading section. If a block wants to be much longer, either the task is really two tasks, or the excess content belongs behind a link.

**When to split into sub-tasks:** default to a single H2 block. Add a second (or further) H2 block only when each sub-task is independently substantial — each must be able to justify a full Description, Considerations, and Solutions of its own. A thin sub-task generates three sections of scaffolding for little content — merge it into a neighbouring block instead.

**No cross-section redundancy:** each fact or rationale appears exactly once on the page. The Description explains why the task matters; Considerations must not re-explain it. Considerations raise the trade-offs; Solutions must not restate them before acting on them.

### Block structure

The heading hierarchy is as follows:

```
## How do you [task question]?        ← H2: the task or sub-task question itself
### Description                        ← H3
### Considerations                     ← H3
### Solutions                          ← H3
```

For a page with two sub-tasks, the structure would be:

```
## How do you [first sub-task question]?
### Description
### Considerations
### Solutions

## How do you [second sub-task question]?
### Description
### Considerations
### Solutions

## Further Reading
```

#### Task heading (H2)
- The task or sub-task question is the H2 heading itself — do not use "Task" as the heading word.
- Frame it as a clear, specific question addressed directly to the reader (e.g. *"## How do you write a good README for your research software?"*).
- By default, add no body text beneath the heading. Add a single sentence only if the question alone would leave the page's scope genuinely unclear.

#### Description (H3)
- A short, direct explanation of what the task or problem is about and why it matters to the reader.
- This is not an introduction to the wider topic — it's scoped to this specific task.
- If readers are likely to overestimate what the practice achieves, state plainly what it does not guarantee — but only where that misunderstanding is genuinely likely, not as a routine disclaimer, and within the 2–4 sentence budget rather than on top of it.
- Aim for 2–4 sentences. Avoid padding.

#### Considerations (H3)
- The things the reader should keep in mind when thinking about this task: benefits, trade-offs, choices, key insights, characteristics of good or bad solutions.
- **Budget: 4–7 bullets.** Each bullet is one sentence — two at most — following the anatomy *one insight, optionally one clause of consequence*. Never stack claim + explanation + example + caveat in a single bullet.
- Write bullets in second person where natural ("Your existing codebase may have..."), but don't force it where it reads awkwardly.
- Each bullet should add value — cut anything self-evident or generic, and do not restate the Description's rationale.

Bullet anatomy example:
- ✗ "Your dependencies can contain vulnerabilities. This is because most research software builds on many third-party packages, and any one of them may have a security flaw. For example, a single outdated library can expose your whole application. You should therefore keep track of what you depend on, although this can be time-consuming for large projects."
- ✓ "Most vulnerabilities enter through third-party dependencies rather than your own code, so knowing what you depend on matters more than auditing every line you write."

**AI code generation context:** include a bullet about AI-generated code only if it would change what the reader actually does on this specific task; otherwise omit it. When included, phrase it as a principle (AI-generated code has the same quality needs as hand-written code) and never name specific AI tools.

#### Solutions (H3)
- The steps and approaches for actually undertaking the task, informed by the considerations.
- **Budget: 5–8 bullets.** Each bullet is one action, optionally one clause of how or when.
- Prefer actionable steps. Include conceptual framing only where a step is meaningless without it — do not write a conceptual counterpart for every action.
- Do not re-justify points already made in Considerations — act on them, don't re-argue them.
- Where high-quality external resources exist, link to them here rather than reproducing their content at length.

**Tool-focused pages:** if the page is primarily about using a specific tool, the Solutions section should include a minimal concrete example (a command, snippet, or step), explicit prerequisites, and a note on when the tool is not the right choice. Do not leave the reader with only abstract guidance about a tool's existence.

**Pages with multiple valid approaches:** if the topic has several valid approaches rather than one recommended practice, frame them as contextually appropriate choices rather than a progression. Avoid language that implies readers should advance from simpler to more complex options. Different approaches suit different project types, team sizes, and risk levels — say so plainly.

### Further Reading section

Further Reading is an H2 heading (`## Further Reading`), sitting at the same level as the task heading(s). Every page ends with it. This is a curated list of 3–5 authoritative and highly regarded external resources — tools, documentation, books, papers, or guides — that a reader can follow to go deeper on the topic.

**Ordering:** list practical and tool-focused resources first (documentation, guides, frameworks), then broader or more theoretical resources (papers, books) at the end.

**Format for each entry:**
```
- **[Title](URL)** — A 1–2 sentence description covering what the resource is and why it is worth the reader's time. Do not pad to two sentences if one does the job.
```

**Key principles for Further Reading:**
- Prefer resources that are freely accessible online where possible.
- Each entry must earn its place — it should offer something distinct from the others.
- Do not include resources just to pad the list; 3 strong entries are better than 5 weak ones.
- The description should explain *why* the resource is worth reading, not just *what* it is.
- Avoid resources that are behind paywalls unless they are genuinely the best available source on the topic.

### AI Disclosure section

Every page ends with an **AI Disclosure** section immediately after Further Reading. It is an H2 heading (`## AI Disclosure`).

The section contains a single fixed line of text, with `<model>` replaced by the actual Claude model name used to produce the page:

```
This work was produced with the assistance of Claude <model>, under the strict editorial control and factual verification of the human author.
```

**How to determine the model name:** use the model currently active in the conversation. Examples:

- Claude Sonnet 4.6 → `Claude Sonnet 4.6`
- Claude Opus 4.6 → `Claude Opus 4.6`
- Claude Haiku 4.5 → `Claude Haiku 4.5`

If you are uncertain which model is active, ask the user to confirm before generating this section.

The full page ending therefore looks like:

```
## Further Reading

- ...

## AI Disclosure

This work was produced with the assistance of Claude Sonnet 4.6, under the strict editorial control and factual verification of the human author.
```

---

## Compression Pass (mandatory)

After completing a draft, make a second pass whose only goal is to shorten it by 20–30% without losing information:

1. Merge bullets that make overlapping points.
2. Delete any sentence that restates a rationale already given elsewhere on the page.
3. Strip signposting sentences ("The following considerations apply...", "In summary...", "It is important to note that...").
4. Tighten every bullet to the anatomy above: one insight or action, at most one supporting clause.
5. Check each H2 block against the 250–475 word budget; if over, cut or move content behind a link.

Only present the post-compression draft to the user.

---

## Writing and Review Checklist

Use this checklist when drafting or reviewing a task page.

### Structure
- [ ] Page uses the correct heading hierarchy: H2 for task question(s), H3 for Description / Considerations / Solutions.
- [ ] The word "Task" does not appear as a heading — the task question itself is the H2 heading.
- [ ] The page uses more than one H2 block only where each sub-task is independently substantial; a single task stays as one block.
- [ ] Where there are genuinely substantial sub-tasks, each has its own full H2 block (not crammed into one block).
- [ ] No headings are missing or at the wrong level.
- [ ] Body prose is one sentence per line; paragraphs are separated by blank lines, with no blank line between sentences of the same paragraph.
- [ ] Page ends with `## Further Reading` (H2).
- [ ] Page ends with `## AI Disclosure` (H2) after Further Reading.
- [ ] AI Disclosure text uses the correct model name for the current conversation.

### Voice
- [ ] Task heading (H2) is addressed directly to the reader in second person.
- [ ] Description speaks to the reader ("when you are working on...").
- [ ] Considerations bullets use second person where natural.
- [ ] Solutions steps address the reader directly ("choose a tool", "start with...").
- [ ] Tone is professional, direct, and approachable throughout — approachable does not mean casual, chatty, or padded.

### Task heading (H2)
- [ ] The H2 heading is the task question itself, not the word "Task".
- [ ] The scope is specific (not vague like "Research software quality").
- [ ] Optional one-sentence body text beneath the heading states what the page provides, if needed.

### Description section
- [ ] Explains what the problem/task is and why it matters to the reader.
- [ ] Scoped to this task, not the wider topic.
- [ ] 2–4 sentences; no padding.
- [ ] Where a common misunderstanding is likely, the Description states what the practice does not guarantee (and omits it otherwise).

### Considerations section
- [ ] Lists things the reader genuinely needs to keep in mind.
- [ ] Includes relevant trade-offs, characteristics, key insights.
- [ ] No filler bullets; each point earns its place.

### Solutions section
- [ ] Actionable and/or conceptually useful.
- [ ] Distinguishes guidance from steps where appropriate.
- [ ] Links to high-quality external resources rather than reproducing their content.
- [ ] Does not leave the reader with nothing actionable.

### Further Reading section
- [ ] Contains 3–5 entries; no more, no fewer unless quality demands it.
- [ ] Practical/tool-focused resources appear before theoretical/book resources.
- [ ] Each entry has a description explaining why it is worth reading and what value it offers.
- [ ] All resources are freely accessible online where possible.
- [ ] No padding — every entry is there for a reason.

### Concision
- [ ] No bullet exceeds two sentences; most are one.
- [ ] No fact or rationale appears more than once on the page.
- [ ] Each H2 block is within the 250–475 word budget (excluding code).
- [ ] No signposting or summary sentences.
- [ ] The compression pass has been run before presenting the draft.

### Overall quality
- [ ] Reader can form a correct understanding without following any links.
- [ ] Links present are to high-quality, stable, relevant external material.
- [ ] Content is factually accurate and reflects current good practice.
- [ ] No adoption claims or consensus statements appear without a source or hedging — "widely used" rather than "the most widely adopted"; "common practice" rather than "the standard".
- [ ] No unnecessary duplication of content that external resources handle better.
- [ ] Tone is direct and practical — not academic, not marketing.

---

## Common Failure Modes to Avoid

- **Malformed links** — always use `[Link text](URL)` and nothing else. No backticks inside link text, no nested links, no raw URLs as link text.
- **"Task" used as a heading** — the word "Task" should never appear as a heading; the task question itself is the H2 heading.
- **Wrong heading levels** — task questions are H2, Description/Considerations/Solutions are H3, Further Reading is H2. Do not flatten everything to H2 or nest incorrectly.
- **Multi-sentence paragraphs on one line** — body prose must be one sentence per line; equally, do not insert blank lines between sentences of the same paragraph, which would split it into separate paragraphs.
- **Vague task framing** — "Software testing" is not a task. "How do you decide which tests to write for your research software?" is.
- **Third person voice** — writing "researchers should..." or "teams need to..." instead of addressing the reader directly as "you".
- **Approachable tipping into casual** — "you" does not license slang, chattiness, conversational preambles, or reassurance softeners; keep a professional register. Approachable means plainer language and acknowledging difficulty, not more words.
- **Description that doesn't explain why it matters** — don't just describe the topic; say why it's important for the reader's research software quality.
- **Description that oversells the practice** — where readers would plausibly assume the practice guarantees more than it does, say what it does not guarantee; leave this out when no such misunderstanding is likely.
- **Considerations that are obvious** — cut bullets like "Testing takes time" unless they lead somewhere useful.
- **Solutions that are only links** — external links are good but the reader must get something actionable even without clicking.
- **Solutions that reproduce external content at length** — summarise, frame, and link; don't copy.
- **Missing sub-task blocks** — if the topic has distinct sub-tasks, each needs its own full block.
- **Conflating guidance and steps** — be clear about what is conceptual versus what is an action to take.
- **Missing Further Reading section** — every page needs one; don't omit it.
- **Missing AI Disclosure section** — every page needs one immediately after Further Reading; don't omit it.
- **Wrong model name in AI Disclosure** — use the actual model active in the current conversation, not a placeholder or a guess.
- **Further Reading that just describes resources without explaining their value** — each entry must say why it is worth reading, not just what it is.
- **Further Reading ordered theory-first** — practical and tool-focused resources come before books and papers.
- **Tool lists without a minimal concrete example** — listing tools with links but no starting point leaves the reader knowing the tool exists without knowing how to begin. Include at least one runnable command or step in the Solutions section.
- **Tool recommendations without a dating caveat** — if specific tool options or comparisons are likely to change quickly, note that recommendations reflect a point in time and should be verified.
- **Unsupported adoption or consensus claims** — phrases like "the most widely used" or "the standard approach" need either a source or softer wording. Use "widely used" or "common practice" instead. These claims can become quietly false and undermine the page's credibility.
- **Bloated bullets** — claim + explanation + example + caveat stacked into one bullet. Keep one idea per bullet with at most one supporting clause.
- **Rationale repeated across sections** — the Description says why it matters; Considerations and Solutions must not say it again.
- **Skipping the compression pass** — first drafts are reliably 20–30% longer than they need to be; the pass is not optional.

---

## Notes on Additional Passes

RSQKit task pages may require additional passes after initial drafting, depending on context. These include:

- **Page metadata** (frontmatter, tags, category, etc.) — handled separately.
- **Internal links** (cross-references to other RSQKit pages) — handled separately.
- **External resource vetting** (checking link quality, currency, and longevity, including Further Reading entries) — may be handled by a separate skill.
- **Enrichment** (adding content from provided URLs, attachments, or text) — handled by the `rsqkit-task-page-enrich` skill.

When writing or reviewing, focus on structure, voice, and content quality. Flag where links or metadata will be needed, but do not block on them.
