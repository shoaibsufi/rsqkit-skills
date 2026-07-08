---
name: rsqkit-task-page-metadata
description: Use this skill whenever the user wants to generate, suggest, review, or improve the YAML front matter metadata for an RSQKit task page. Trigger when the user asks to "add metadata", "generate the front matter", "suggest page metadata", "what should the metadata be?", "write the YAML header", or any similar phrasing. Also trigger when the user has a drafted or existing RSQKit task page and wants to make it publication-ready with correct metadata. Always use this skill when working on RSQKit page metadata, even if the user just says "can you add the metadata to this page?".
---

# RSQKit Task Page Metadata Skill

This skill generates and reviews the YAML front matter metadata block for RSQKit task pages. Metadata appears at the very top of a page file, delimited by `---` before and after it.

---

## Metadata Format

A complete task page metadata block looks like this:

```yaml
---
title: "Page title here"
description: "Short description of what this page covers, used in tile/card views."
contributors: ["Full Name One", "Full Name Two"]
page_id: page_id_slug
related_pages:
  tasks: [page_id_one, page_id_two]
quality_indicators: [indicator_abbreviation_one, indicator_abbreviation_two]
keywords: ["keyword one", "keyword two", "keyword three"]
---
```

**Line formatting.** Front matter is YAML, so the one-sentence-per-line convention used for RSQKit page *content* does not apply here.
Keep each metadata key on its own line (standard YAML mapping).
Do not split a value across lines by sentence: a multi-sentence `description` stays on its single line; only if a value genuinely must span lines, use a YAML block scalar (`>-` or `|`) rather than sentence-per-line breaks.

---

## Field-by-Field Guidance

### `title`
The full display title of the page. Used as the H1 heading in the rendered page. Should match the main Task heading of the page content closely, but as a noun phrase rather than a question.
- ✓ `"Using static analysis"`
- ✗ `"How do you use static analysis?"`

### `description`
A short, plain-prose description of what this page covers. This appears in tile/card views when pages are listed (e.g. search results, related pages). Aim for 1–2 sentences. Write in third person, not second person.
- ✓ `"How to use AI tools to assess the quality of your research software."`
- ✗ `"You should read this if you want to know about AI quality tools."`

### `contributors`
A list of contributors who authored or contributed significantly to the page. Each name must match an entry in the RSQKit `_data/CONTRIBUTORS.yml` file. If you do not know who contributed, leave this as an empty list `[]` and flag it for the user to complete.

### `page_id`
A unique slug identifier for this page. Used in `related_pages` references on other pages.
- Use lowercase letters and underscores only — no hyphens, no spaces.
- Base it on the most meaningful part of the page title.
- Examples: `static_analysis`, `ai_quality_assessment`, `creating_good_readme`, `licensing_software`
- Check existing page IDs (listed below) to avoid conflicts.

### `related_pages`
A list of `page_id`s of other RSQKit task pages that are related to this one. These appear as "Related pages" on the rendered page. The format is:

```yaml
related_pages:
  tasks: [page_id_one, page_id_two]
```

**How to select related pages**: choose pages that a reader of this page would plausibly also benefit from reading — either because the topic is a prerequisite, a natural next step, or closely overlapping. Use the **Content summary** column in the Existing Page IDs section to judge genuine topical overlap rather than relying on similarity of `title` or `page_id`. Do not list everything; be selective. A list of 2–5 is typical.

See the **Existing Page IDs** section below for all current page IDs you can reference.

### `quality_indicators`
A list of quality indicator **slugs** from the RSQKit `quality_indicators.yml` file. These are the indicators most directly relevant to the topic of the page — i.e., indicators that a reader applying this page's guidance would be helping to satisfy.

The slug is the `abbreviation` value from the YAML (identical to the final path segment of each indicator's `@id`). Always put the slug in this field — e.g. `software_has_license` — never the descriptive text.

Leave as `[]` if no indicators clearly apply.

See the **Quality Indicators Reference** section below for all current slugs and their descriptions

### `keywords`
A list of lowercase keyword strings related to the topic. Used to power search within RSQKit and to connect to external training registries (e.g. TeSS). 

Guidelines:
- Reuse keywords already used on related pages where appropriate — this helps build a consistent folksonomy across RSQKit.
- Include the core topic term(s), common synonyms, and any tool names or standards that are central to the page.
- Aim for 3–8 keywords. Avoid padding with generic terms like "software" or "research" unless they are genuinely distinctive.
- All lowercase.

---

## Existing Page IDs

Use these when populating `related_pages`, and to check `page_id` uniqueness. These are all current RSQKit task pages.

The **Content summary** column captures what each page actually covers in its body (a content fingerprint drawn from its section structure and prose), and is deliberately distinct from the front-matter `description:` tagline. Use it to match pages by **topical overlap**, not just by similarity of `title` or `page_id` — two pages can be closely related while having quite different names.

**Caution:** the key is the `page_id`, which is not always the same as the file name. Where they differ it is noted under the table. Always reference the `page_id`.

| page_id | Title | Content summary |
|---|---|---|
| `archiving_software` | Archiving software | Why code-hosting platforms are insufficient for long-term preservation, and how to archive research software: capturing execution environments, build reproducibility, versioning/provenance, emulation/containers, and DOI-backed deposit via Software Heritage, Zenodo, ReproZip, Guix/Nix and RO-Crate metadata. |
| `ci_cd` | Continuous Integration and Continuous Delivery/Deployment | Defines CI vs continuous delivery vs continuous deployment and the practices they automate (builds, automated testing, code-quality checks, deployment pipelines, monitoring, rollback), plus the tool categories — VCS-integrated CI services, pipeline runners, testing tools, artefact registries, containerisation/orchestration, IaC. Parent page for tool- and org-specific CI sub-tasks. |
| `ci_testing_matrices` | Managing complex CI testing matrices for research software | Testing efficiently across large matrices of compilers, library versions, architectures and platforms — taming combinatorial explosion with pairwise testing (allpairspy) and exclusion rules, optimising pipeline performance via container strategies, layer caching and wave scheduling, managing multi-platform/HPC hardware diversity and performance-regression detection, and a phased adoption plan (with a resource/energy sustainability note). |
| `citing_software` | Citing software | What software citation is and why it matters (reproducibility, credit, impact tracking), the elements of a citation, and the Citation File Format — creating and validating a CITATION.cff file with cffinit/cffconvert so humans and tools (GitHub, Zenodo, Zotero) can reuse the metadata. |
| `code_review` | Performing a code review | What code review is and why it matters for research software (early error detection, knowledge sharing, reproducibility, onboarding), what to focus on (correctness, testing, documentation, modularity) versus what to avoid (style nitpicking, rewrites, blame), and supporting practices/tools — pull requests, linters, CI, CODECHECK. |
| `complete_bibliographic_metadata_codemeta` | Creating bibliographic metadata with CodeMeta | Creating and maintaining a codemeta.json file for discoverability and citation — required fields and good practice (persistent identifiers/DOIs, ORCID iDs, SPDX licence, linking the reference publication, funder IDs), generation tools (CodeMeta Generator, SOMEF, auto-codemeta) and JSON-LD validation, with a worked example. |
| `computational_workflows` | Computational workflows | What computational workflows are (actions, workflow definition languages, management systems), their benefits (reproducibility, automation, scaling, provenance, modularity), choosing a system by domain/facility/community, discovering and registering workflows (WorkflowHub, Galaxy, Dockstore, nf-core, REANA), describing them with Workflow RO-Crate, and FAIR alignment. |
| `creating_good_readme` | Creating a good README | Why a README is a project's entry point and how a good one drives adoption, transparency and maintenance, plus the key sections — description, requirements, installation, configuration, usage, contribution, acknowledgements, citation, licence — with research-specific additions (reproducing experiments, linking outputs) and automated metadata extraction via SOMEF. |
| `credit_recognition_research_software` | Credit and recognition for research software and people who write it | Two linked tasks: making contributions visible, citable and verifiable (CRediT/CRO roles, ORCID, DOIs, CITATION.cff/codemeta.json, recognition platforms APICURON and BIP! Scholar); and building the career-progression evidence base (pairing metrics with narrative, linking releases to ORCID, documenting adoption/reuse, peer recognition via HiddenREF/SSI Fellowships). |
| `documenting_code` | Documenting code | Internal documentation of how code works for developers/maintainers (distinct from user-facing project docs) — audiences and types (product vs process), comments and docstrings, meaningful error messages, usage examples, quickstarts/tutorials, documenting CLIs/APIs, version-controlling docs, and automated generators (Sphinx, Doxygen, Roxygen, JSDoc, MkDocs). |
| `documenting_software_project` | Documenting software project | User- and collaborator-facing documentation of a project as a whole (distinct from internal code docs) — audience and purpose, structure, keeping it current and accessible for reproducibility, and the standard file set: README, INSTALL, LICENSE, CITATION, CONTRIBUTING, CODE_OF_CONDUCT, contributor lists, roadmap, changelog. |
| `documenting_software_readthedocs` | Documenting software using 'Read The Docs' | Using Read the Docs to publish and host documentation — how it relates to Sphinx/MkDocs source and GitHub/GitLab CI, and step-by-step setup: generating doc sources, hosting in Git, importing the project, configuring `.readthedocs.yaml`, wiring CI webhooks for automatic builds, and publishing. |
| `fair_rs` | Adopting FAIR research software practices | What FAIR research software means in practice (Findable, Accessible, Interoperable, Reusable) with concrete actions per principle — metadata standards (CodeMeta), persistent identifiers/DOIs, public repositories/registries, licensing, citation, documentation — how FAIR relates to broader quality and reproducibility, and FAIRness assessment tools (FAIR checklist, FAIRsoft Evaluator, howfairis, CODECHECK, RSFC). |
| `improving_environmental_sustainability` | Improving environmental sustainability | Measuring and reducing software's environmental impact — the Green Software Foundation's energy-efficiency, hardware-efficiency and carbon-awareness aspects and the GREENER principles, plus practical routes: training and certification (GreenDiSC), the Software Carbon Intensity framework, and emissions-monitoring tools (CodeCarbon, Green Algorithms, carbontracker, Greenspector, Ecograder). |
| `languages_tools_infrastructures` | Choosing languages, tools & infrastructures | Choosing programming languages, tools/frameworks and infrastructures — the decision factors (community practice and local expertise, language/ecosystem fit, lifecycle stage from rapid prototyping to joining an existing project), an opinionated set of good default languages by purpose (Python, C++, JS/TS, R, Fortran, Julia, Rust, CUDA/OpenCL, shell), and starting from community templates. |
| `licensing_software` | Licensing software | Copyright and licensing for research software — why a licence is essential for reuse (the 'R' in FAIR) and the IP/ownership considerations (employer and funder rights, third-party code), the main licence families and trade-offs (public domain, permissive MIT/BSD/Apache, copyleft GPL/LGPL/AGPL, Creative Commons for non-code), and how to apply a licence including per-file with REUSE; tools choosealicense, SPDX, reuse. |
| `maintaining_research_software` | Maintaining research software | Two linked tasks: keeping research software functioning, understandable and usable over time (treating maintenance as ongoing, managing dependencies as a liability, automated testing and scheduled CI, documentation upkeep, versioning and changelogs, reducing the bus factor, recruiting help, securing maintenance funding, and archiving/deprecating gracefully); and tracking and managing technical debt (recording it visibly, allocating protected time, refactoring incrementally with tests, and using static analysis). |
| `org_gitlab_ci_infra_for_github_project` | Using organisational GitLab CI infrastructure for your GitHub project | Running CI for a GitHub-hosted project on an organisation's own GitLab runners when GitHub's free tier lacks the hardware (GPUs, alternative architectures) or capacity — repository and fork mirroring, bidirectional CI status reporting back to GitHub, access/security management, configuring and tagging specialised runners, and the monitoring, reliability (webhooks, token rotation, redundancy) and workflow-complexity trade-offs of a hybrid setup. |
| `packaging_software` | Packaging software | Preparing software so others can install and reuse it — distinguishing packaging from publishing and releasing, what packaging involves (standard structure, config/build files, metadata, simple install), and three distribution routes: code-hosting platforms, language-specific package registries (PyPI, CRAN, npm, Maven), and container/workflow registries (Docker, Singularity, WorkflowHub, Dockstore). |
| `publishing_software` | Publishing software | Umbrella/landing page for publishing research software so others can find, understand, use and cite it — framing the constituent steps in suggested order (documentation, metadata, identifiers, citation, packaging, releasing, archiving with a DOI) and linking the dedicated sub-task pages. (Index page: no H3 sub-sections; summary derived from intro and child-page list.) |
| `releasing_software` | Releasing software | How to create code releases — what a release and changelog are, versioning schemes (semantic vs calendar versioning), and practical steps to publish a release on a code-hosting platform (worked GitHub example) including automatic DOI minting via Zenodo integration. |
| `reproducible_software_environments` | Reproducible software environments | What reproducible software environments are and the approaches to creating them — language-specific virtual environments, containers (Docker, Singularity/Apptainer), system-level tools (Vagrant, NixOS, Packer) and computational-workflow environments — with a focus on per-project virtual development environments: why they matter for dependency isolation, portability and sharing, and the package/environment managers per language (pip/venv, poetry, uv, conda for Python; renv for R; Pkg.jl, Conan, Maven, Bundler; Spack/Nix/Guix). |
| `software_documentation` | Software documentation | Umbrella/landing page introducing software documentation and its two main aspects — project documentation (the software as a whole, for users and collaborators) and code documentation (how the code works internally, for developers and maintainers) — and why both matter for understandability, reusability and sustainability; links to the dedicated sub-task pages. (Index page: no H3 sub-sections; summary derived from intro and child-page list.) |
| `software_identifiers` | Software identifiers | Why and how to uniquely identify software and its versions — the reasons (compatibility, security fixes, reproducibility, collaboration, CI/CD) and the identifier methods with their trade-offs (semantic versioning, DOIs, cryptographic hashes/checksums, UUIDs, Git commit hashes), then a practical guide to obtaining and using DOIs via Zenodo (concept vs release DOIs, GitHub integration, the GitLab route with codemeta + eossr/gitlab2zenodo) and adding the DOI badge to your repository. |
| `software_management_planning` | Software Management Planning | Preparing a Software Management Plan (SMP) — what it is and the core areas it covers (reproducibility/reusability, funding and milestones, community standards, accessibility, crediting and impact), key considerations (a living document, stakeholder engagement, engineering best practices plus governance and long-term maintenance, tailoring rigour to software type per the EVERSE three-tier view, and being both human-readable and machine-actionable), and the available templates, tools and guides (ELIXIR SMP, Software Management Wizard, maSMP, SSI guide and checklist, and others). |
| `software_metadata` | Software metadata | What software metadata is and why it matters for discoverability, reuse and interoperability — the attributes it captures and which matter for which use case (citation vs replication vs discovery), the main standards (CodeMeta, SPDX, Dublin Core, Schema.org/BioSchemas; build/package metadata like pyproject.toml, pom.xml, package.json; container/deployment metadata like SBOM, OCI, Dockerfile), and a focused guide to CodeMeta — what it is, who consumes it, and how to create a codemeta.json (CodeMeta Generator, SOMEF, or manually). |
| `structuring_software_projects` | Software project structure | Why a clear, consistent directory structure matters for navigation, collaboration and reproducibility, and good practices for organising a project — a single well-named directory, top-level metadata files (README, LICENSE, CITATION.cff, codemeta.json), labelled sub-directories (code/src, data with raw/processed separation, results, doc, figures), file/directory naming conventions, putting the project under version control, and example layouts (generic, and a Python src layout via fair-python-cookiecutter or Poetry). |
| `task_automation_github_actions` | Task automation using GitHub Actions | Setting up GitHub Actions for task automation (CI/CD) on a repository — what Actions and workflows are, the prerequisites and concepts (the .github/workflows directory, YAML syntax, event triggers, the Marketplace, runner OS options, secrets), and worked steps: creating a basic workflow, reusing pre-built Marketplace actions (e.g. setup-python), and automating testing with pytest. |
| `task_automation_gitlab_ci_cd` | Task automation using GitLab CI/CD | Setting up GitLab CI/CD for a GitLab repository — what it is (the GitLab equivalent of GitHub Actions, with migration pointers) and what it automates (testing, builds, Docker images, documentation deployment, packaging, dependency checks), the prerequisites and concepts (runners, the .gitlab-ci.yml file, the Pipelines view, the CI/CD Catalog), and a worked pipeline example explaining stages and jobs. |
| `testing_software` | Testing software | What software testing is and why it matters for research credibility and reusability (early bug detection, better code structure, confidence to share openly under FAIR), the types of tests — functional (unit, integration, system, acceptance, regression) and non-functional (performance, usability, security, compatibility) plus tactics like black-box/white-box and TDD — and how to test in practice, from informal/manual testing through writing test functions to automated test frameworks (pytest, testthat, JUnit, Test.jl) and running them in CI (GitHub Actions, GitLab CI/CD). |
| `using_containers` | Using containers | Why and how to use containers for research software — what containers are and when they help (specific dependencies/versions, multi-platform execution, CI/CD integration, long-term reproducibility), their benefits over building for a single environment (portability, easy setup, versioning, automation-friendliness, lightweight vs VMs), and worked Python examples with Docker (Dockerfile, build/run, ports, registry push/pull, CI/CD use) and Apptainer/Singularity for HPC (.sif files, CI/CD use). |
| `using_version_control` | Using version control | Two linked tasks: choosing a version control system for a research project (the decision factors — project/team size, file types, large-binary handling, institutional policies — with Git as the default and alternatives like Git-LFS/Perforce, Mercurial and Subversion for specific needs); and implementing version control in a research workflow (establishing a branching strategy and commit/review guidelines, integrating with IDEs and CI, training the team, tagging versions for reproducibility, and maintaining the repository). |
| `writing_readable_code` | Writing readable code | Why source-code readability matters for reusability (the 'R' in FAIR) and future maintenance, and the practices that improve it — consistent formatting, modular structure, descriptive names, well-placed comments and docstrings, following a community style guide (PEP8, R, Google), design patterns, type annotations with a checker (mypy), automated formatters (black) and linters (pylint), informative directory structure, and reusing well-tested libraries. |
| `writing_research_software_story` | Writing a Research Software Story | What a Research Software Story is — a structured narrative capturing the context and role of a research software project (the problem it addresses, the community around it, and the practices and tools that support it, rather than how to run it) — who benefits (new contributors, project leaders, funders/reviewers) and the reflective value of writing one, the template sections it follows, and practical ways to produce a version-zero draft (working through the template, a paired interview, or LLM-assisted structured prompting), plus refinement tips and seminar resources. |

*Note: this list reflects the live RSQKit task pages as of 22 June 2026 — 34 pages. New pages may have been added since; ask the user to confirm if you are unsure whether a related page exists.*

*File-name vs `page_id` mismatches in the current set (always key on the `page_id`): `software_maintenance.md` → `maintaining_research_software`; `software_project_structure.md` → `structuring_software_projects` (this page was previously `organising_software_projects` — treat that old ID as stale); `writing_research_software_stories.md` → `writing_research_software_story` (singular).*

---

## Quality Indicators Reference

When populating `quality_indicators`, match the page's content against the **descriptions** below and select the indicators that a reader applying the page's guidance would be helping to satisfy. Be conservative — a short, accurate list beats a long, speculative one.

**Put the slug — the back-ticked identifier at the start of each bullet — in the `quality_indicators` field. Never use the descriptive text.** Each slug is the verbatim `abbreviation` from `quality_indicators.yml` (identical to the final path segment of that indicator's `@id`). The description exists only to help you decide *which* slugs apply; it is never what goes into the metadata.

- `archived_in_scholarly_repository` — The source code repository is archived in a scholarly repository (e.g Zenodo, HAL) to ensure that software can be found and accessed in a scholarly context.
- `archived_in_software_heritage` — The source code repository is found in the universal source code archive, Software Heritage, to ensure long-term access to the full development history.
- `code_churn_ok` — The code churn (how much a source code has changed over time) of the project's source code is maintained within a reasonable level according to the community's standards and conventions. An example of how to calculate it would be code churn = added lines + deleted lines.
- `code_documentation_coverage_ok` — This check tries to determine if the project's codebase is mostly documented according to community conventions and standards (i.e. docstrings).
- `code_duplication_ok` — The code duplication ratio is maintained at a reasonable level according to community's standards and conventions. Code duplication ratio is the percentage of code within a code base or project that is syntactically identical, often measured using code blocks. An example for calculating it may be (lines_duplicated/lines_of_code)*100.
- `code_smells_ok` — The code smell ratio is maintained at a reasonable level according to community standards and conventions. Code smells are indicators of possible design problems mainly for maintainability of the code (i.e. functions too large, code that is hard to read, too many input parameters for a function, etc.). The density of code smells can be estimated with the code smell ratio, an estimator of code smells within a codebase of project often measured using rule-based checks (i.e. Sonarqube). An example for calculating it could be (code_smells/lines_of_code)*1000.
- `codemeta_completeness` — This indicator checks that the codemeta file is sufficiently complete (according to community expectations). That is, the percentage of properties that are filled with metadata is above an acceptable threshold established by a target community. This indicator does not assess the quality of the metadata fields available.
- `coupling_between_objects_ok` — The coupling between objects (CBO) ratio is maintained at a reasonable level according to the community's standards or expectations
- `cyclomatic_complexity_ok` — Cyclomatic complexity (i.e., the number of linearly independent paths through a program’s source code) of the whole software component or modules/components/classes/functions/methods should follow the conventions established by the community responsible for maintaining the tool. Cyclomatic complexity is created by calculating the number of different code paths in the flow of the program. A program that has complex control flow requires more tests to achieve good code coverage and is less maintainable.
- `dependency_management` — Reviews how external libraries and dependencies are managed to ensure compatibility and security.
- `descriptive_metadata` — This indicator aims to determine if a software component comes with descriptive metadata that provides information. This includes, but is not limited to: name, domain, programming language, date created, date of first publication, keywords, related links, etc..
- `functional_correctness` — For analysis code specifically, is there a quantifiable measure of the functional correctness of the software output. This indicator focuses on computational/statistical correctness. For example, in an ML model software context, the indicator measures whether the repository reports metrics like Accuracy, F1-score, or ROC-AUC to prove the model performs as intended. However other performance metrics may also address the indicator. Evaluation metrics may be provided through documentation, tables or scripts available in the source code of the target tool.
- `has_active_communication_channels` — The project has communication channels (i.e. Slack, Gitter, etc.) where users and developers can discuss project-related matters and also be up to date with updates, notices and other relevant information.
- `has_active_contributors` — Contributions and/or other additions/updates to the project aren't centralised on only the core maintainers, but also other contributors.
- `has_ci-tests` — This indicator aims to determine if the project runs tests before pull requests are merged.
- `has_contribution_guidelines` — The software repository provides contribution guidelines in case someone wants to contribute to the project.
- `has_no_binary_artifacts` — The repository does not contain binary artifacts. Binary artifacts are files generated by compilation or packaging tools that contain code that is no longer human-readable (i.e. .class, .jar, .war, .pyc, etc.).
- `has_no_linting_issues` — The project addresses or resolves warnings identified by compilers, safe modes, or linters.
- `has_published_package` — This indicator aims to determine if a software project is published as a downloadable package.
- `has_releases` — To enable collaborative review, the project's source repository MUST include interim versions for review between releases; it MUST NOT include only final releases. This indicator determines if a software project has releases. This can be achieved by looking for tags or using software that retrieves related data.
- `human_code_review_requirement` — This indicator aims to determine if a software project requires human code review before pull requests.
- `internal_cohesion_ok` — The cohesion among methods/functions of a module is maintained to a reasonable level according to community expectations and standards. Cohesion describes how related the functions within a single module are. Low cohesion implies that a given module performs tasks which are not very related to each other and hence can create problems as the module becomes large
- `lines_of_code_ok` — Number of lines of code for the whole software project or components/modules/classes/functions/methods should follow the conventions established by the community responsible for maintaining the source code
- `listed_in_registry` — The target source code repository is in a disciplinary or community registry (e.g ascl.net, bio.tools, swMath, RRID portal, RSD, WikiData, DataCite, etc.) to ensure that software can be found and accessed.
- `maintainability_index_ok` — The maintainability index (i.e., degree of effectiveness and efficiency with which a product or system can be modified by the intended maintainers) should follow conventions and standards established by the community responsible for maintaining the source code or system. The maintainability index depends on 3 main factors: cyclomatic complexity, lines of code and halstead volume (amount of information that needs to be processed to understand the code). An example for calculating it could be MAX(0,(171 - 5.2 * ln(Halstead Volume) - 0.23 * (Cyclomatic Complexity) - 16.2 * ln(Lines of Code))*100 / 171).
- `metadata_is_up_to_date` — Metadata information reflects the current description of a software project. This indicator ensures that the current project metadata provides up to date, accurate and relevant information about a software component.
- `no_critical_vulnerability` — Checks if reported critical vulnerabilities have been fixed
- `no_leaked_credentials` — Checks if hardcoded secrets like passwords, API keys, and tokens is stored in the public git repository
- `passed_tests_ok` — The software tool passes all the tests provided within its own repository.
- `persistent_and_unique_identifier` — This indicator tries to determine if the software identifier is based on a suitable identifier scheme, and test it can be resolved. This is done by checking if the identifier uses an identifier scheme contained in a list of globally unique identifier schemes
- `project_is_active` — This indicator aims to determine if a project's repository is maintained by its corresponding maintainers (i.e. commiting within a reasonable time window or having a status of "Active").
- `repository_workflows` — This indicator aims to determine if a software project makes use of workflows to automate processes like testing and deployment.
- `requirements_specified` — This indicator tries to determine if the project specifies what is required to use the software.
- `response_timeframe_ok` — The maintainers of the project's repository respond to issues and/or pull requests within a defined time frame that follows the related community's conventions.
- `software_has_citation` — This indicator aims to determine if the project uses a citation to reference contributors and authors (e.g., through a CFF file, in the README, etc).
- `software_has_documentation` — This indicator aims to determine if a software project comes with many forms of documentation like readme or readthedocs
- `software_has_license` — This check tries to determine if the project has published a license
- `software_has_license_for_file_types` — This indicator determines if the project has an appropriate licenses for its different file types (e.g., documentation, images, code, tests, etc.). The REUSE specification defines good practices for accomplishing this task.
- `software_has_tests` — Evaluates the extent to which the software has been tested, including unit tests, integration tests, and system tests, to ensure reliability and correctness.
- `software_is_containerized` — The project's repository where its source code is hosted includes a container build file to containerize it (i.e. Dockerfile, Podman, Apptainer, etc.).
- `software_test_coverage` — Indicates that the test suite covers most (or ideally all) the code branches, input fields, and functionality
- `static_analysis_common_vulnerabilities` — At least one static code analysis tool used includes rules or techniques to detect common vulnerabilities specific to the language or environment.
- `support_issue_tracking` — The software project offers an accessible issue tracking system (e.g., GitHub/GitLab Issues or a helpdesk) that is used to report, document, and manage bugs, enhancement requests, and user-facing operational issues.
- `uses_fuzzing` — This indicator checks that the software produced by the project includes software written using a memory-unsafe language (e.g., C or C++), then at least one dynamic tool (e.g., a fuzzer or web application scanner) be routinely used in combination with a mechanism to detect memory safety problems such as buffer overwrites.
- `uses_tool_for_warnings_and_mistakes` — This indicator checks that the project enables one or more compiler warning flags, a "safe" language mode, or uses a separate "linter" tool to look for code quality errors or common simple mistakes, if there is at least one FLOSS tool that can implement this criterion in the selected language.
- `version_control_use` — This indicator aims to determine if a software project uses version control.
- `versioning_standards_use` — This indicator aims to determine if the version (or versions) of a software tool follows an established community convention like semantic versioning (SemVer) or calendar versioning (CalVer).

*Note: the descriptions above are copied verbatim from `quality_indicators.yml` (with a few obvious source typos corrected). The file changes over time — if the user supplies an updated version, regenerate this list from it: one bullet per entry, slug taken from `abbreviation`, text taken from `description`, alphabetical by slug.*

---

## Process for Generating Metadata

When asked to generate metadata for a task page:

1. **Read the page content** — understand the topic, the task(s) covered, and the tools or practices discussed.

2. **Derive `title`** — use a noun-phrase version of the main Task heading.

3. **Write `description`** — one or two sentences summarising what the page covers, in third person.

4. **Set `contributors`** — ask the user if not clear from context; do not invent names.

5. **Generate `page_id`** — lowercase slug from the most meaningful part of the title. Check against the existing page IDs list to avoid conflicts.

6. **Select `related_pages`** — scan the Existing Page IDs table, using the **Content summary** column to judge topical overlap (not just `title` or `page_id` similarity), and select 2–5 pages that are genuinely related. Reason briefly about why each is included if it is not obvious.

7. **Select `quality_indicators`** — scan the indicators reference list, matching the page's content against the descriptions, and select those the page's guidance directly helps to satisfy. Put the **slug** (the back-ticked identifier) in the field — never the description text. Be conservative — a short accurate list is better than a long speculative one.

8. **Choose `keywords`** — include the core topic term(s), tool names or standards covered, and any synonyms likely to be used in search. Check keywords used on related pages and reuse where appropriate.

9. **Output the complete metadata block**, delimited by `---`, ready to be placed at the top of the page file.

---

## Common Mistakes to Avoid

- **Inventing page IDs** — only reference page IDs from the existing page IDs list; do not guess.
- **Over-populating quality_indicators** — only include indicators the page's content directly helps satisfy, not every vaguely related one.
- **Putting descriptions instead of slugs in `quality_indicators`** — the field takes the slug (e.g. `software_has_license`), never the indicator's descriptive text.
- **Title as a question** — the `title` field should be a noun phrase, not the second-person question used in the Task heading.
- **description in second person** — the `description` field is used in tile views and should be in third person, unlike the page body.
- **Keywords with capital letters** — all keywords should be lowercase.
- **Splitting metadata values by sentence** — the content one-sentence-per-line rule does not apply to front matter; keep one key per line and do not break a value (e.g. `description`) across lines by sentence.
