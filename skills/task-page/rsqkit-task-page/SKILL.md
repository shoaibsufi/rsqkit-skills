---
name: "rsqkit-task-page"
description: "Use this skill whenever the user wants to write, draft, improve, review, or quality-assure an RSQKit task page. Trigger when the user mentions RSQKit, asks to write or review a task page, asks for help with a task-description-considerations-solutions structure, or is working on content about research software quality. Also trigger when the user says things like \"help me write a page about X for RSQKit\", \"can you review this task page?\", \"draft the considerations section for this RSQKit task\", \"does this follow the RSQKit format?\", or any similar phrasing. Always use this skill when working on RSQKit content."
---

# RSQKit Task Page Skill

RSQKit task pages are structured guidance pages that help researchers and research software engineers understand and act on research software quality topics. Each page must be accurate, self-contained enough to be useful on its own, and motivate readers to learn more.

RSQKit pages serve a wide audience: first-year PhD students reading them as guidance, experienced academics pointing others to them, and researchers who write code. Write so that a newcomer can build a correct working model of the task, and so that an experienced reader finds nothing wrong or oversimplified.

---

## Core Principles

Every RSQKit task page must satisfy these quality criteria:

1. **Clarity of purpose** — The reader must immediately understand why the topic matters and why this task is important for research software quality.
2. **Accuracy** — Content must be factually correct and reflect current good practices in research software.
3. **Self-sufficiency** — If external links are not followed, the page still gives the correct impression and enough guidance to apply the information correctly.
4. **Appropriate depth** — Provide a conceptual overview and practical guidance. If a topic is well-covered by high-quality external material, point to it rather than duplicating it.
5. **Motivation to learn more** — Link out to high-quality external documentation, standards, training materials, or community guidance.
6. **Correct overall impression** — A reader leaving the page without following any links should have an accurate mental model of the task and how to approach it.
7. **Concision and readability** — The page should be as short as it can be while still reading easily on first reading. Cut repeated explanation and padding, but never the words that connect one sentence to the next. Readability comes before coverage: if a block cannot keep every point and still read easily within its budget, link to the less important points or leave them out, and do not compress the text to make them fit. When in doubt about detail, link to it.
8. **Research-specific content** — Each page states what is different about the task for research software, where anything is (for example numerical correctness, data-dependent behaviour, scale and HPC, recording the environment for reproducibility, credit and citation, funder or institutional requirements, or short-term funding and staff turnover). This content is never removed in the compression pass.

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

### Sentence length

Aim for an average sentence length of about 10–15 words across the body.
Flag any sentence over 25 words and split it unless splitting loses the connection between its parts.

Short sentences written one after another without links between them read as staccato.
Fix this by joining related statements with connecting words (see Readability and flow), or, where they are genuinely separate points, by turning them into bullets, one idea per bullet.
Keep Descriptions as prose.

The average sentence length is a guide, not the main test of readability.
A short sentence can still be hard to read if it packs in a list, an example and a qualification.

### Readability and flow

The page should read as a short explanation from a colleague, not as a list of compressed facts.
A reader new to the topic should be able to follow each bullet on first reading.

- Each sentence makes one point.
  Do not put a list of more than three items, an example, and a qualification into the same sentence.
  If a sentence needs all of these, split it, or move the list or example into the next sentence.

- Keep the words that show how one sentence follows from another, such as "because", "so", "this means", "for example" and "as a result".
  Do not remove them to save words.

- Write whole sentences with their normal grammar.
  Do not drop articles, verbs or linking words to shorten a sentence ("so results map to source lines" instead of "so that the results can be mapped to source lines").

- Introduce a point before giving its detail.
  Say what the reader needs to know and why, then give the tool, command or figure.

- A higher word limit is room to explain the existing points more clearly.
  It is not a reason to add more points.

Example of dense text and the same content written to flow:

```
✗ - Passing tests show agreement, not correctness.
    Expected values may themselves be wrong.
    Record their provenance.

✓ - A passing test shows that the code gives the result you expected, not that the result is right.
    If an expected value was itself calculated wrongly, the test will pass on wrong code.
    Note where each expected value came from, so that you or others can check it later.
```

The second version is longer, but each sentence makes one point and the reader can see how the sentences connect.

---

## One Sentence Per Line

Write body content with one sentence per line.
Each sentence ends with a newline in the source, so editing or adding a sentence changes a single line instead of reflowing a whole paragraph.
This keeps version-control diffs small and easy to review.

This is a source-formatting convention only — it does not change how the page reads.
A blank line still separates paragraphs.
The single newlines between sentences within a paragraph are soft breaks, not paragraph breaks: do not put a blank line between sentences that belong to the same paragraph, and do not collapse a multi-sentence paragraph back onto one line.

Scope:
- Applies to all prose — the Description, and any sentence-level body text.
- Applies inside bullets: in a bullet with more than one sentence, put each sentence on its own line, indented to align with the bullet text (two spaces after a `- ` marker), so it continues the same bullet.
- Headings, code blocks, tables, and link-reference lines are unaffected.
- YAML front matter is exempt and is handled by the metadata skill (one key per line; values are not split by sentence).

Note: this assumes the site renders a single newline as a space rather than a forced break — i.e. Kramdown `hard_wrap: false` (or the non-GFM parser).
Jekyll's default GFM processor hard-wraps single newlines, which would render each sentence on its own line; that is a site `_config.yml` setting, not something this skill controls.

## List Formatting

Use `-` as the bullet marker in every list on the page, including Further Reading.

If any bullet in a list has more than one sentence, put a blank line between every bullet in that list.
If every bullet in a list is a single sentence, keep the list tight, with no blank lines between bullets.
Decide this per list: in Markdown a single blank line anywhere in a list changes the spacing of the whole list, so mixing the two styles in one list does not work.

Example of a list with multi-sentence bullets:

```
- Shared history is hard to change.
  Removing a file in a new commit leaves it in earlier commits that others may already have copied.
  Keep passwords, keys and large data files out of the repository from the start.

- Agree how your team will use branches before others join.
  Changing the approach later means everyone has to change how they work.
```

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

## Concept Inventory

Before drafting, list the distinct insights the page must carry: the points a reader would get wrong or miss without the page.
Examples from different kinds of page:

- Choosing a licence: a licence chooser gives guidance, not legal advice; once others have contributed, changing the licence usually needs their agreement.
- Testing: coverage shows which code ran, not whether it gave the right answer.
- Citing software: a citation file only helps if its details are updated with each release.

Keep the list short, usually 6–15 items.

After the compression pass, check that every item is still present on the page.
If one has gone, restore it.
If an item cannot fit without making the block dense, do not compress the text to keep it.
Link to it or leave it out, and tell the user which item was dropped and why.

Show the inventory to the user with the draft, as a short list after the page.

### Practitioner check

After the first version of the inventory, answer these questions for the page, or for each block on a multi-block page:

- What would someone who has done this many times do first?
- What mistakes do newcomers usually make?
- What becomes hard or costly to change later?
- Could acting on this page affect other people, systems, data or legal rights, so that permission, consent, isolation or a check is needed first?

Use the answers only to improve the inventory, by adding a missing point or replacing a weaker one.
The inventory keeps its usual size, so this step sharpens the list rather than growing it.
Not every question will have an answer for every topic; skip the ones that do not apply.

Examples of what this step finds: reducing a failure to the smallest case that reproduces it; agreeing a licence before outside contributors join; keeping secrets out of version control; only scanning or load-testing services you are authorised to test; getting co-authors' agreement before publishing.

---

## Page Plan

On a multi-block page, plan the blocks before drafting any of them.
Planning first means you decide what to leave out while you can still choose well, instead of cutting a finished draft to fit the budget.

1. **List the questions readers bring.**
   Write down the questions someone would arrive with, in their own words.
   To widen the list, think about the situations people are in when they come to this topic, and keep those that apply:

   - starting something new
   - choosing between options
   - something has gone wrong
   - taking over or improving an existing project
   - keeping something going over time
   - meeting a requirement from a funder, journal or institution

   Different topics bring different situations.
   For dynamic analysis, readers may be investigating a problem they can already see, or checking for problems they cannot see yet.
   For choosing a licence, they may be licensing new code, reusing code under someone else's licence, fixing a project with no licence or mixed licences, or meeting a funder's requirement.
   For version control, they may be starting a repository, working with others, or recovering from a mistake.

   Not every topic has every situation, so do not invent questions to fill the list.
   Group related questions; each group becomes a block.
   Situations that need the same evidence, trade-offs and actions share a block, so a page never needs one block per situation.

2. **Check the breadth of the practice.**
   List the settings in which the practice changes, and keep only those that matter for this topic:

   - the kind of project, using RSQKit's three tiers: analysis code, prototype tools and research software infrastructure
   - the stage in the project's life: new, active, inherited, or ending
   - for technical topics, the kinds of language (compiled and interpreted, memory-safe and not) and the scale (a single machine, HPC, GPU, distributed)
   - for other topics, the discipline, the size of the team, and the institutional or funder context

   Check that the plan does not quietly assume one setting, such as a single developer, one language or one machine.
   Where the practice differs between settings, say so on the page where the difference arises; where it does not, keep the guidance general.
   Do not organise the page by tier or by setting.

3. **Check for existing RSQKit pages.**
   For each planned block, check whether a live RSQKit page already covers its main points.
   If one does, do not write a shorter version of the same material.
   Instead, ask whether readers of this page would expect to find the topic here.
   If they would not, drop the block and point to that page from the opening block.
   If they would, because the topic is central to this page's practice, keep a short treatment that covers only what is specific to this page's angle, then links to the other page.
   The short treatment can be a single bullet in another block, or a short block of 150–250 words.
   For example, profiling on a dynamic analysis page, continuous integration on a testing page, or a citation file on a publishing page.
   If a page covers only part of the block, keep the block and follow the overlap rule in Page Format.

4. **Add the opening and closing blocks.**
   Every multi-block page starts with an opening block (see Page Format).
   A page about an ongoing practice also ends with a workflow block (see Page Format).

5. **Allocate words.**
   Estimate the words each block needs to explain its points clearly, and add them up against the page budget.
   If the total is over budget, decide now which points to link to or drop, and tell the user which ones.
   Do not plan to fit by writing more densely.

Show the plan to the user before drafting when the page will have four or more blocks, or when step 3 dropped or shortened a block.

---

## Page Format

RSQKit task pages use a repeating structure. Each task or sub-task substantial enough to stand on its own gets its own block of four headings. Every page also ends with a **Further Reading** section and an **AI Disclosure** section.

**When to split into sub-tasks:** split the page into separate H2 blocks when readers would arrive with different questions and each question needs its own evidence, trade-offs and actions. A topic covered by one question stays as one block. A thin sub-task should be merged into a neighbouring block.

**Page budget:** each H2 block stays within 250–475 words (excluding code). The one exception is a short block kept under Page Plan step 3, which stays within 150–250 words. A single-block page is therefore at most 475 words. A multi-block page should stay within 2,000 words of body text (excluding code, Further Reading and AI Disclosure), may go up to 2,200 words, must never exceed 2,200, and normally has no more than 6 full blocks; a short block does not count towards this limit, but its words do count towards the page budget. If a page needs more, consider whether part of it belongs on a separate RSQKit page. The `scripts/readability.py` script reports the body word count.

These budgets are limits, not targets. A page that reads well at 1,500 words should stay at 1,500. When a page is over budget, cut repeated explanation, link to detail, or drop the least important points; do not make the text denser to fit.

**Opening block on a multi-block page:** a multi-block page opens with a conceptual introduction that gives the reader the frame for the rest of the page.
- Its Description says what the practice is, how it relates to neighbouring practices (for example, how code review relates to testing, or how a software licence relates to copyright and to citation), the questions it can answer, and why it matters for research software. It may use a short list of those questions.
- Its Considerations hold the limits and cautions that apply to everything on the page, such as what a clean result does not show, how the project's setting changes the advice, or which decisions are hard to reverse.
- Its Solutions help the reader choose where to start. They do not recommend specific tools; those belong in the later blocks.
- If Page Plan step 3 dropped a block because another RSQKit page covers it, the opening block points to that page.

Later blocks assume this frame and do not repeat it. The opening block's heading is still a "How do you…" question, framed around deciding when or how to use the practice. For an ongoing practice, this might be *"## How do you decide when code review will help your research software?"*; for a one-off decision, *"## How do you decide which licence fits your research software?"*. Do not use "What is X?" headings.

**Workflow block on a page about an ongoing practice:** if the page is about something a team keeps doing, such as testing, analysis, code review or dependency management, the last block is "How do you make [practice] part of your development workflow?".
It covers how often to do each part of the practice compared with its cost, what happens on every change and what happens on a schedule or at release, how to interpret results, how to act on what you find, and how to keep the practice up to date as the project changes.
For a checking practice, such as testing or analysis, acting on findings includes turning them into regression tests.
This block is the home for practical advice that would otherwise repeat in several task blocks, in the same way that the opening block is the home for limits that apply everywhere.
A page about a one-off task, such as choosing a licence or registering a DOI, does not need a workflow block.

**Redundancy:** within a block, each fact or rationale appears once: the Description says why it matters, Considerations do not repeat it, and Solutions act on Considerations without re-arguing them. Across blocks, a short reminder is allowed where a reader may arrive at that block directly. A point that would appear in three or more blocks is stated once instead: a limit or caution goes in the opening block, and practical advice about routine use (scheduling, reproducing failures, regression tests) goes in the workflow block.

**Overlap with other RSQKit pages:** where an existing RSQKit page covers a block's main points, follow Page Plan step 3: drop the block and point to that page from the opening block, or, if readers of this page would expect to find the topic here, keep a short treatment of what is specific to this page and link to the other page. Where an existing page covers only part of a block, keep the block to the working model and a few starting points, and link to that page rather than covering the same material.

### Block structure

The heading hierarchy is as follows:

```
## How do you [task question]?        ← H2: the task or sub-task question itself
### Description                        ← H3
### Considerations                     ← H3
### Solutions                          ← H3
```

For a multi-block page about an ongoing practice, the structure would be:

```
## How do you decide when [practice] will help your research software?   ← opening block: concepts and limits
### Description
### Considerations
### Solutions

## How do you [first reader question]?                                   ← task block
### Description
### Considerations
### Solutions

## How do you [second reader question]?                                  ← task block
### Description
### Considerations
### Solutions

## How do you make [practice] part of your development workflow?         ← workflow block
### Description
### Considerations
### Solutions

## Further Reading

## AI Disclosure
```

### What each section is for

Each section has a different job, and keeping them separate is what lets a page work both as a conceptual introduction and as a practical guide.

| Section | Its job | What belongs here | What does not |
|---|---|---|---|
| Description | Explain the idea | What the task is and why it matters, in plain words; definitions of technical terms on first use | Tool names, commands, flags |
| Considerations | Help the reader judge | Trade-offs, limits, research-specific risks, what a clean result does not show; tool-neutral where possible, so they stay true when tools change | Step-by-step instructions |
| Solutions | Help the reader act | Concrete steps: a named tool, what it is for, and a command or first step | Concepts with no action attached |

#### Task heading (H2)
- The task or sub-task question is the H2 heading itself — do not use "Task" as the heading word.
- Frame it as a clear, specific "How do you…" question addressed directly to the reader (e.g. *"## How do you write a good README for your research software?"*). This applies to every block, including the opening block of a multi-block page.
- Phrase the question around what the reader is trying to do, not around a technique, a file or a category of fault: *"How do you make it easy for others to cite your software?"* rather than *"How do you write a CITATION.cff file?"*, and *"How do you investigate unexpected runtime behaviour?"* rather than *"How do you use memory checkers?"*. Tools and techniques are the answer to the question, so they belong in the block, not in its heading.
- By default, add no body text beneath the heading. Add a single sentence only if the question alone would leave the page's scope genuinely unclear.

#### Description (H3)
- A short, direct explanation of what the task or problem is about and why it matters to the reader.
- Stay at the level of ideas. Explain the concept in plain words, and define each technical term the first time it appears on the page (for example, "a persistent identifier is a reference that keeps pointing to the same thing even if its web address changes").
- Do not name tools or give commands in a Description; those belong in Solutions. Naming a category of tool ("linters", "metadata validators") is fine. The exception is a page about one specific tool (see Tool-focused pages), whose Description has to name it.
- This is not an introduction to the wider topic — it's scoped to this specific task. The exception is the opening block of a multi-block page, which introduces the practice as a whole.
- Aim for 3–6 sentences of prose. Avoid padding.
- Group the sentences into short paragraphs of one to three sentences, one idea per paragraph, with a blank line between paragraphs. For example, one paragraph says what the task is, the next says why it matters for research software. This makes a Description easier to read without changing its wording.
- Do not use bullets in a Description, except that the opening block of a multi-block page may use a short list of the questions the page answers.

#### Considerations (H3)
- The things the reader should keep in mind when thinking about this task: benefits, trade-offs, choices, key insights, characteristics of good or bad solutions.
- Write them to help the reader judge, not to tell them what to run. Keep them tool-neutral where possible, so that they stay true when the tools change. Name a tool only when the point is specific to it (for example, a limit of one particular service or validator).
- **Budget:** 4–6 bullets for a single-block page; 3–5 per block on a multi-block page.
- **Bullet anatomy:** each bullet carries one idea, usually in two or three short sentences: the point, the reason, and what follows from it. One sentence is fine when that is enough. Four sentences is the limit.
- Write bullets in second person where natural ("Your existing codebase may have..."), but don't force it where it reads awkwardly.
- Each bullet should add value — cut anything self-evident or generic, and do not restate the Description's rationale.

Bullet anatomy examples:
- ✗ "Your dependencies can contain vulnerabilities. This is because most research software builds on many third-party packages, and any one of them may have a security flaw. For example, a single outdated library can expose your whole application. You should therefore keep track of what you depend on, although this can be time-consuming for large projects." (claim, explanation, example and caveat stacked into one bullet)
- ✓ "Changing a licence later is harder than choosing one now. Once others have contributed, you usually need their agreement to relicense their code. Choose a licence before you accept outside contributions." (one idea: the point, the reason, and what follows)

**Limits of evidence:** where readers are likely to over-trust something the page recommends, state what a good result does not show, in one Considerations bullet for that block. This applies to any check, tool, validator, score, badge or template, and also to whatever the result is compared against. Examples:

- a stored reference output shows that results have not changed, not that they were right
- a metadata validator checks the format, not whether the content is accurate
- a licence chooser gives guidance, not legal advice
- a race detector finding nothing does not rule out deadlocks

State a general limit that applies to everything on the page once, in the opening block. Do not add these statements where no over-trust is likely.

**AI code generation context:** include a bullet about AI-generated code only if it would change what the reader actually does on this specific task; otherwise omit it. When included, phrase it as a principle (AI-generated code has the same quality needs as hand-written code) and never name specific AI tools.

#### Solutions (H3)
- The steps and approaches for actually undertaking the task, informed by the considerations.
- **Budget:** 4–6 bullets for a single-block page; 3–5 per block on a multi-block page.
- Each bullet is one action with, where needed, how or when to do it, in at most three short sentences.
- When a bullet recommends a tool, say what the tool is for and give a command or first step, so the reader can start without following a link. "Use a debugger" is not enough; "run the program in a debugger such as gdb, type `run`, and after the crash type `backtrace`" is. The same applies where no software tool is involved: "add a licence" is not enough; "add a file called `LICENSE` to the top folder of your repository containing the full licence text" is.
- Each task block should give the reader at least one concrete step they could take today. The opening block's Solutions are the exception: they help the reader choose where to start.
- Solutions are always bullets, including in the opening block.
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

A two-sentence entry follows the One Sentence Per Line and List Formatting rules: the second sentence goes on its own indented line, and the list then has a blank line between entries.

**Key principles for Further Reading:**
- Prefer resources that are freely accessible online where possible.
- Each entry must earn its place — it should offer something distinct from the others.
- Do not include resources just to pad the list; 3 strong entries are better than 5 weak ones.
- The description should explain *why* the resource is worth reading, not just *what* it is.
- Avoid resources that are behind paywalls unless they are genuinely the best available source on the topic.

### AI Disclosure section

Every page ends with an **AI Disclosure** section immediately after Further Reading. It is an H2 heading (`## AI Disclosure`).

By default the section contains a single fixed line of text, with `<model>` replaced by the actual Claude model name used to produce the page:

```
This work was produced with the assistance of Claude <model>, under the strict editorial control and factual verification of the human author.
```

**How to determine the model name:** use the model currently active in the conversation. Examples:

- Claude Sonnet 4.6 → `Claude Sonnet 4.6`
- Claude Opus 4.6 → `Claude Opus 4.6`
- Claude Haiku 4.5 → `Claude Haiku 4.5`

If you are uncertain which model is active, ask the user to confirm before generating this section.

**Multi-stage disclosure:** if the page has been drafted or revised with more than one AI model or tool, list each stage in order, one sentence per stage, naming the model and what it did, and end with the statement that editorial control and factual verification remain with the human authors. Ask the user for the earlier stages if they are not known. Example:

```
This work was initially produced with the assistance of Qwen 3.8 (27B), under the editorial control of the human author.
Claude Fable 5.1 was then used to review and reformulate the draft.
Further restructuring was made with the assistance of ChatGPT.
Final editorial control and factual verification remain with the human authors.
```

The full page ending for a single-stage page therefore looks like:

```
## Further Reading

- ...

## AI Disclosure

This work was produced with the assistance of Claude Sonnet 4.6, under the strict editorial control and factual verification of the human author.
```

---

## Compression Pass (mandatory)

After completing a draft, make a second pass to remove repetition and padding.
There is no target percentage: cut only what is repeated or adds nothing, and leave the rest.

1. Merge bullets that make the same point.
2. Apply the three-block rule from Redundancy: move points repeated in three or more blocks into the opening block.
3. Remove words the heading already supplies (inside a code review block, "reviewers find fewer problems in very large changes" does not need to name code review again).
4. Strip signposting sentences ("The following considerations apply...", "In summary...", "It is important to note that...").
5. Do not remove connecting words, drop normal grammar, or merge sentences to save words; the rules in Readability and flow still hold after this pass.
6. Check each block and the page against the budgets in Page Format; if over, cut repeated explanation, move detail behind a link, or drop the least important points, and tell the user what was dropped.
7. Check the Concept Inventory and restore anything lost, unless it was dropped under step 6.
8. Check for absolute rules or rankings that compression introduced ("on every pull request", "the highest-value check") and soften them unless a source supports them.
9. Read each block as someone new to the topic would. If a bullet needs a second reading to follow, rewrite it to flow, even if this makes it longer.

Only present the post-compression draft to the user.

---

## Readability Check (optional)

If the user asks, or if Python is available, run `scripts/readability.py` on the page and report the body word count, average sentence length, Gunning Fog and Flesch Reading Ease.
The script needs the `textstat` package (`pip install textstat`).
It measures body text only: it removes front matter, headings, code blocks, link markup and tool tags, and stops at Further Reading.

Always present the scores with this note, word for word:

> Note - technical vocabulary raises these scores whatever the sentence length, so use them to check direction between drafts, not as a target

Do not shorten sentences only to move a score.

---

## Writing and Review Checklist

Use this checklist when drafting or reviewing a task page.

### Content review (do this first when reviewing)
When reviewing a page, first assume three things and look for each: something is missing, something is incorrect, and something is wordier than it needs to be.
Also look for over-smoothing: places where a concept is described as simpler than it is, or where an insight a specialist would expect has been dropped.
Ask the Practitioner check questions of the page, and note any answer the page does not cover.
Report these findings before checking format.

### Structure
- [ ] Page uses the correct heading hierarchy: H2 for task question(s), H3 for Description / Considerations / Solutions.
- [ ] The word "Task" does not appear as a heading — the task question itself is the H2 heading.
- [ ] The page is split into separate blocks only where readers would arrive with different questions, each needing its own evidence, trade-offs and actions; thin sub-tasks are merged.
- [ ] A multi-block page opens with a conceptual introduction that sets out the frame for the rest.
- [ ] A page about an ongoing practice ends with a workflow block; a page about a one-off task does not need one.
- [ ] The blocks were planned before drafting (Page Plan), and the questions behind them cover the reader situations that apply to this topic, without invented ones.
- [ ] No block repeats what a live RSQKit page already covers; where readers would expect a covered topic here, it has a short treatment and a link.
- [ ] No headings are missing or at the wrong level.
- [ ] Body prose is one sentence per line, including inside bullets; paragraphs are separated by blank lines, with no blank line between sentences of the same paragraph.
- [ ] Lists use `-` markers; lists with any multi-sentence bullet have a blank line between every bullet.
- [ ] Page ends with `## Further Reading` (H2).
- [ ] Page ends with `## AI Disclosure` (H2) after Further Reading.
- [ ] AI Disclosure text uses the correct model name(s), with one sentence per stage if more than one model or tool was used.

### Voice
- [ ] Task heading (H2) is addressed directly to the reader in second person.
- [ ] Description speaks to the reader ("when you are working on...").
- [ ] Considerations bullets use second person where natural.
- [ ] Solutions steps address the reader directly ("choose a tool", "start with...").
- [ ] Tone is professional, direct, and approachable throughout — approachable does not mean casual, chatty, or padded.
- [ ] Average sentence length is about 10–15 words; no sentence over 25 words without good reason.
- [ ] Each sentence makes one point; no sentence packs in a list of more than three items, an example and a qualification.
- [ ] Connecting words between sentences are kept, and sentences use normal grammar rather than shortened forms.
- [ ] Each bullet can be followed on first reading by someone new to the topic.

### Task heading (H2)
- [ ] Every H2 heading is a "How do you…" question, including the opening block.
- [ ] The scope is specific (not vague like "Research software quality").
- [ ] Each heading names what the reader is trying to do, not a technique or a fault category.
- [ ] Optional one-sentence body text beneath the heading states what the page provides, if needed.

### Description section
- [ ] Explains what the problem/task is and why it matters to the reader.
- [ ] Scoped to this task, not the wider topic (except the opening block).
- [ ] Explains the idea in plain words, with technical terms defined on first use.
- [ ] Contains no tool names, commands or flags, unless the page is about one specific tool.
- [ ] 3–6 sentences of prose; no padding; no bullets except the question list allowed in an opening block.
- [ ] Sentences are grouped into short paragraphs of one to three sentences, one idea per paragraph.

### Considerations section
- [ ] Lists things the reader genuinely needs to keep in mind.
- [ ] Includes relevant trade-offs, characteristics, key insights.
- [ ] Where readers are likely to over-trust a check, tool, validator, score, template or reference, one bullet says what a good result does not show; a general limit appears once, in the opening block.
- [ ] No filler bullets; each point earns its place.
- [ ] Tool-neutral where possible.

### Solutions section
- [ ] Actionable and/or conceptually useful.
- [ ] Written as bullets in every block.
- [ ] Distinguishes guidance from steps where appropriate.
- [ ] Links to high-quality external resources rather than reproducing their content.
- [ ] Where a block overlaps another RSQKit page, gives the model and starting points and links to that page.
- [ ] Does not leave the reader with nothing actionable.
- [ ] Every recommended tool comes with what it is for and a command or first step.
- [ ] Every task block has at least one concrete step the reader could take today.

### Further Reading section
- [ ] Contains 3–5 entries; no more, no fewer unless quality demands it.
- [ ] Practical/tool-focused resources appear before theoretical/book resources.
- [ ] Each entry has a description explaining why it is worth reading and what value it offers.
- [ ] All resources are freely accessible online where possible.
- [ ] No padding — every entry is there for a reason.

### Concision
- [ ] Bullets are within the anatomy limits: Considerations at most four sentences, Solutions at most three, most bullets two or three.
- [ ] Bullet counts are within budget: 4–6 per section on a single-block page, 3–5 per section per block on a multi-block page.
- [ ] Within a block, no fact or rationale appears more than once; nothing is repeated in three or more blocks.
- [ ] Each H2 block is within 250–475 words (excluding code), or 150–250 words for a short block kept under Page Plan step 3; a multi-block page is within 2,000 words of body text (2,200 at most) and normally no more than 6 full blocks.
- [ ] Any extra word allowance was used to explain points more clearly, not to add more points.
- [ ] No signposting or summary sentences.
- [ ] The compression pass has been run before presenting the draft.
- [ ] The Practitioner check was done and its answers are reflected in the Concept Inventory.
- [ ] Every item in the Concept Inventory is present on the page, or the user has been told which items were dropped to keep the page readable.
- [ ] No absolute rules or rankings were introduced without a source.

### Overall quality
- [ ] Reader can form a correct understanding without following any links.
- [ ] The page states what is different about the task for research software, where anything is.
- [ ] The page does not quietly assume one setting, such as one kind of project, one stage of a project's life, one language or one scale of computing (Page Plan step 2).
- [ ] Where acting on the page could affect other people, systems, data or legal rights, the page says what permission, consent, isolation or check is needed first.
- [ ] Links present are to high-quality, stable, relevant external material.
- [ ] Content is factually accurate and reflects current good practice.
- [ ] No adoption claims or consensus statements appear without a source or hedging — "widely used" rather than "the most widely adopted"; "common practice" rather than "the standard".
- [ ] No unnecessary duplication of content that external resources handle better.
- [ ] Tone is direct and practical — not academic, not marketing.

---

## Common Failure Modes to Avoid

- **Malformed links** — always use `[Link text](URL)` and nothing else. No backticks inside link text, no nested links, no raw URLs as link text.
- **"Task" used as a heading** — the word "Task" should never appear as a heading; the task question itself is the H2 heading.
- **"What is X?" headings** — every H2 is a "How do you…" question, including the opening block.
- **Wrong heading levels** — task questions are H2, Description/Considerations/Solutions are H3, Further Reading is H2. Do not flatten everything to H2 or nest incorrectly.
- **Multi-sentence paragraphs on one line** — body prose must be one sentence per line; equally, do not insert blank lines between sentences of the same paragraph, which would split it into separate paragraphs.
- **Vague task framing** — "Software testing" is not a task. "How do you decide which tests to write for your research software?" is.
- **Third person voice** — writing "researchers should..." or "teams need to..." instead of addressing the reader directly as "you".
- **Approachable tipping into casual** — "you" does not license slang, chattiness, conversational preambles, or reassurance softeners; keep a professional register. Approachable means plainer language and acknowledging difficulty, not more words.
- **Description that doesn't explain why it matters** — don't just describe the topic; say why it's important for the reader's research software quality.
- **Overselling a practice** — where readers would plausibly over-trust a check, tool, template or reference, say what a good result does not show, following the Limits of evidence rule; leave this out when no such over-trust is likely.
- **Considerations that are obvious** — cut bullets like "Testing takes time" unless they lead somewhere useful.
- **Solutions that are only links** — external links are good but the reader must get something actionable even without clicking.
- **Solutions that reproduce external content at length** — summarise, frame, and link; don't copy.
- **Missing sub-task blocks** — where readers would arrive with different questions that each need their own evidence, trade-offs and actions, each needs its own block.
- **Conflating guidance and steps** — be clear about what is conceptual versus what is an action to take.
- **Missing Further Reading section** — every page needs one; don't omit it.
- **Missing AI Disclosure section** — every page needs one immediately after Further Reading; don't omit it.
- **Wrong model name in AI Disclosure** — use the actual model active in the current conversation, not a placeholder or a guess.
- **Further Reading that just describes resources without explaining their value** — each entry must say why it is worth reading, not just what it is.
- **Further Reading ordered theory-first** — practical and tool-focused resources come before books and papers.
- **Tool lists without a minimal concrete example** — listing tools with links but no starting point leaves the reader knowing the tool exists without knowing how to begin. Include at least one runnable command or step in the Solutions section.
- **Tool recommendations without a dating caveat** — if specific tool options or comparisons are likely to change quickly, note that recommendations reflect a point in time and should be verified.
- **Unsupported adoption or consensus claims** — phrases like "the most widely used" or "the standard approach" need either a source or softer wording. Use "widely used" or "common practice" instead. These claims can become quietly false and undermine the page's credibility.
- **Bloated bullets** — more than one idea in a bullet, or bullets beyond the anatomy limits (four sentences for Considerations, three for Solutions).
- **Rationale repeated across sections** — within a block, the Description says why it matters and Considerations and Solutions must not say it again; a point repeated in three or more blocks belongs in the opening block.
- **Skipping the compression pass** — first drafts usually repeat explanation and include signposting; the pass is not optional.
- **Dense, telegraphic text** — sentences that pack in lists, examples and qualifications, or drop connecting words and normal grammar to save space. The reader has to work out how the points relate. Follow Readability and flow.
- **Filling the allowance** — treating a higher word limit as a reason to add more points. Use extra room to explain existing points more clearly.
- **Over-smoothing** — describing a concept as simpler than it is, or dropping an insight during compression. Check the Concept Inventory.
- **Staccato paragraphs** — runs of short statements written as prose with nothing connecting them. Join related statements with connecting words, or turn genuinely separate points into bullets (see Readability and flow).
- **Absolutes introduced by compression** — rules or rankings that a longer sentence would have qualified.
- **Recreating an adjacent RSQKit page** — covering in full, or in a shortened form, what another page already covers. Drop the block and point to that page, or, if readers would expect the topic here, keep only what is specific to this page and link; if the overlap is partial, give the model and starting points, then link.
- **Dropping what readers expect** — leaving out a topic central to the practice only because another page covers it, so the page reads as incomplete. Keep a short treatment and a link (Page Plan step 3).
- **Tool-led Descriptions** — opening a block with tool names, flags or commands before the reader knows what the task is. Explain the idea first; tools go in Solutions.
- **Conceptual Solutions** — Solutions that say what to do but not how ("use a debugger", "use device-specific tools"). Name an example tool and give a first step.
- **Technique-led headings** — headings that name a tool or fault category instead of the reader's goal.
- **Single-setting pages** — guidance that silently assumes one setting, such as C on a single machine, a solo developer, or a new project, when the practice applies more widely.
- **Forced situations** — inventing reader questions or blocks for situations that do not fit the topic, or organising the page tier by tier. Reader situations and settings are prompts for widening the plan, not sections to fill.
- **One-paragraph Descriptions** — five or six sentences run together as one block of text. Split them into short paragraphs, one idea each.
- **Repeated practical advice** — the same advice about recording the environment, reproducing failures or adding regression tests in several blocks. State limits once in the opening block and routine practice once in the workflow block.
- **Planning by cutting** — drafting far over budget and then cutting to fit. Plan the blocks and their word allocation first (Page Plan).
- **Chasing readability scores** — shortening sentences only to improve a metric.

---

## Notes on Additional Passes

RSQKit task pages may require additional passes after initial drafting, depending on context. These include:

- **Page metadata** (frontmatter, tags, category, etc.) — handled separately.
- **Internal links** (cross-references to other RSQKit pages) — handled separately.
- **External resource vetting** (checking link quality, currency, and longevity, including Further Reading entries) — may be handled by a separate skill.
- **Enrichment** (adding content from provided URLs, attachments, or text) — handled by the `rsqkit-task-page-enrich` skill.

When a page has several blocks, tell the user that the metadata pass should check that every RSQKit page linked in the body appears in `related_pages`, and that the keyword list covers each block.

When writing or reviewing, focus on structure, voice, and content quality. Flag where links or metadata will be needed, but do not block on them.
