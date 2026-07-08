# Tutorial: Drafting RSQKit task pages with Claude AI

**Tutorial · approximately 1 hour · works in Claude.ai desktop**

> [!NOTE]  
> **Free plan users:** the free Claude plan typically allows around 5–7 messages per session before hitting the usage limit. 
> To get through all four skills you may have to spread the work across multiple short sessions or ask a colleague to continue with queries on their machine.

> [!IMPORTANT]  
> **Prefer not to use AI tools?** No problem — you can draft your task page manually. 
> Start by writing in a collaborative document such as [Google Docs](https://docs.google.com), following the [RSQKit page structure]() - see the [template](https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/pages/tasks/TEMPLATE_task.md) and [example task pages](https://everse.software/RSQKit/tasks). 
> When your draft is ready for review, fork the [RSQKit repository](https://github.com/EVERSE-ResearchSoftware/RSQKit), add your page file to `pages/tasks/`, and open a pull request against the `main` branch. The editorial board will review it from there.

## Objectives

Overall aim of the contentathon is to create drafts of task pages for inclusion into RSQKit.
Drafts can either be created manually from scratch or with the help of an AI which will then need to be reviewed manually by the authors (in the first instance) and then the RSQKit Editorial Board.

Objectives of this tutorial are learn how to use **Claude desktop app** and pre-prepared Claude AI `skills` (which embed a pre-defined set of rules, structure and style for task pages) to guide task page draft generation. 

## What are RSQKit task pages?

Tasks are typical activities undertaken throughout research software lifecycle around engineering, development, sharing, publishing, deploying and maintenance of research software.
Each task offers a list of considerations to be taken into account when performing the task, good practices and guidelines, relevant tools and resources recommended by communities and links to training materials relevant for the task.
It typically does not offer an in depth instructions on how to perform the task - instead it give a high level overview of why the task is important and should be embedded in the lifecycle with pointers to official documentation and tutorials for further learning.

See existing pages at: https://everse.software/RSQKit/tasks.

## What are Claude skills?

Skills are instruction files that tell Claude how to do a specific task — consistently, every time. You install them once into the Claude desktop app (under Custimise → Skills), and Claude automatically uses the right one when you describe what you want. 

## Prerequsites

### Account with Claude.ai
An account with [Anthropic's Claude.ai](https://claude.ai/login) can be opened for free. With the free account, some usage limits apply (see the note above).

### Claude desktop app
Claude.ai skills require the Claude desktop app (Mac or Windows) - download it at [claude.ai/download](https://claude.ai/download) and sign in. 

### Four task page skill files
Download the four skill files from [github.com/shoaibsufi/rsqkit-task-page-skills](https://github.com/shoaibsufi/rsqkit-task-page-skills/tree/main/skills) and install each one via `Customise → Skills → Add skill` in Claude.ai desktop app. 

### Fork the RSQKit repository
You will submit your draft task page via a pull request. Fork [EVERSE-ResearchSoftware/RSQKit](https://github.com/EVERSE-ResearchSoftware/RSQKit) now so it is ready when you need it.

## Four Claude.ai skills for RSQKit task page

There are four skills in the RSQKit task page family, designed to be used in sequence: you write a draft task page, optionally enrich it with sources, tidy up tool links mentioned in the task page, then generate task page metadata.

Some steps in the sequence are optional depending on your needs - details provided in the table below.


| Step | Skill | What it does | Required? |
|------|-------|-------------|-----------|
| 1 | `rsqkit-task-page` | Writes the full draft: structure, voice, content, and further reading | Required |
| 2 | `rsqkit-task-page-enrich` | Deepens the draft with content from URLs, files, or pasted text | Optional |
| 3 | `rsqkit-task-page-update-tools` | Replaces plain tool links with `{% tool "id" %}` tags from the registry | Required |
| 4 | `rsqkit-task-page-metadata` | Generates the YAML front matter block for the top of your page file | Required |

### Recommended workflow

```
1. rsqkit-task-page              — write the draft
2. rsqkit-task-page-enrich       — (optional) deepen with external sources
3. rsqkit-task-page-update-tools — replace tool links with tool tags
4. rsqkit-task-page-metadata     — generate the front matter
```

Steps 2 and 3 can be swapped. Step 4 can run any time after step 1. 

Always start a fresh Claude conversation for each new page — it keeps context small and output consistent.

## What each skill does

### Step 1 — `rsqkit-task-page`: write the draft

This is the core skill. Give Claude a topic and it will produce a complete task page: one or more Task Questions (as H2 headings), each with Description, Considerations, and Solutions sub-sections, plus a Further Reading section. It writes in the second person throughout and uses plain Markdown links.

If the topic naturally breaks into two or more distinct sub-tasks, Claude will produce multiple H2 blocks automatically. Review the draft carefully — check that the content is accurate and the balance between sections feels right before moving on.

Example prompts:
- *"Write an RSQKit task page on how to use software containers for reproducible research."*
- *"Write an RSQKit task page on choosing a software licence for research software."*

### Step 2 — `rsqkit-task-page-enrich`: enrich with sources (optional)

If you have useful source material — a URL, an attached document, a paper, or pasted text — this skill weaves it into the existing draft without changing its structure. Claude fetches the URL, reads the content, follows relevant links one level deep, and summarises what changed and why.

This is particularly useful when a topic has authoritative community guidance you want reflected, when you want more specific tool recommendations from a known resource, or when the draft feels thin on practical detail.

Example prompts:
- *"Enrich this draft using the content at https://example.org/guide."*
- *"Enrich this page with references to relevant lessons in the Carpentries Incubator (https://github.com/carpentries-incubator)."*

### Step 3 — `rsqkit-task-page-update-tools`: replace tool links

This skill scans every Markdown link in the page and compares it against the RSQKit tools registry. Links that match a registered tool are replaced with the `{% tool "id" %}` tag syntax the site requires. Links in the Further Reading section are left as plain Markdown links.

Claude will also report what was replaced, what was left as a plain link, and any potential new tool entries for tools not yet in the registry. If Claude suggests new entries, copy the YAML and add it to `_data/tool_and_resource_list.yml` in your fork before submitting — otherwise the site will not build.

Example prompts:
- *"Update the tool links in this page."*
- *"Replace tool links with tool tags."*

### Step 4 — `rsqkit-task-page-metadata`: generate front matter

This skill produces the YAML block that goes at the top of your page file: `title`, `description`, `page_id`, `related_pages`, `quality_indicators`, `keywords`, and the EVERSE TeSS training entry. The `contributors` field is left empty for you to fill in manually.

Review the suggestions carefully — especially `related_pages` (check those IDs exist in RSQKit) and `quality_indicators` (check each one is genuinely satisfied by following the page's guidance). Add your name to `contributors` as it appears in `_data/CONTRIBUTORS.yml`.

Example prompts:
- *"Can you suggest page metadata for this task page?"*
- *"Generate the YAML front matter for this page."*

## Step-by-step install guide

1. **Download the skill files.** Go to [github.com/shoaibsufi/rsqkit-task-page-skills](https://github.com/shoaibsufi/rsqkit-task-page-skills/tree/main/skills/task-page) and download the four `.skills` files that you will feed into Claude.ai desktop app. Skill files are binary files (basically .zip archives) containing is a single human-readable Markdown file describing the skill. The `SKILL.md` files can also be found in the same folder and can be downloaded and fed in Claude.ai instead. 

2. **Open the Claude desktop app.** Go to Customise → Skills. If you don't see this menu, make sure you're signed in. It may also look different depending on your app version.

3. **Add each skill file.** Click Add skill and point Claude at each `SKILL.md` file in turn. Do this four times — once per skill. Claude will read the file and make the skill available in all future conversations.

4. **Verify the install.** Start a new conversation and type: *"List the RSQKit skills you have available."* Claude should name all four. If any are missing, re-add them from Settings.

5. **Write your first page.** Start a new conversation. Give Claude a specific topic, then work through the four skills in order. When done, assemble the YAML front matter and page content into a single `.md` file and submit it as a pull request to the RSQKit repository.

## Tips for getting the best results

- **Use a fresh conversation for each page.** The skills work best with a clean context. Long conversations with many files and prior exchanges can produce less consistent output.
- **Be specific about the topic.** The more precisely you describe the task, the better the draft. *"How do you choose a software licence for research software?"* will produce a better result than *"software licences"*.
- **Iterate on content before running later skills.** Get the draft right before running the tool update and metadata steps — it avoids having to redo those passes if the content changes significantly.
- **Check the Further Reading links.** The skills suggest well-regarded resources, but verify that links are still live and references to sections are accurate before submitting.
- **Review quality indicators carefully.** The metadata skill suggests indicators conservatively, but confirm each one is genuinely satisfied by a reader following the page's guidance.

> [!NOTE]  
> **Note:** after running steps 3 and 4, Claude may suggest new tool registry entries or flag contributor details to fill in manually. Always review `related_pages` and `quality_indicators` in the generated metadata before submitting.

## Resources

- Skills and full workflow documentation: [github.com/shoaibsufi/rsqkit-task-page-skills](https://github.com/shoaibsufi/rsqkit-task-page-skills)
- RSQKit repository: [github.com/EVERSE-ResearchSoftware/RSQKit](https://github.com/EVERSE-ResearchSoftware/RSQKit)
- RSQKit contribution guidelines: [EVERSE-ResearchSoftware/RSQKit — contribution guidelines](https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/pages/contributing/contribution_guidelines.md)
- RSQKit task page template: [EVERSE-ResearchSoftware/RSQKit — task pages guidelines](https://github.com/EVERSE-ResearchSoftware/RSQKit/blob/main/pages/tasks/TEMPLATE_task.md)
