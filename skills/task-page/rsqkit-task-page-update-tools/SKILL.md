---
name: rsqkit-task-page-update-tools
description: Use this skill whenever the user wants to replace tool links in an RSQKit task page with the RSQKit tool tag syntax {% tool "id" %}. Trigger when the user says things like "update the tool links", "replace links with tool tags", "add tool tags to this page", "convert links to tool syntax", or any similar phrasing. Also trigger when the user wants to check whether tools mentioned on a page exist in the tool_and_resource_list.yml file, or wants suggestions for new tool entries to add to that file. Always use this skill after rsqkit-task-page has produced a draft and before rsqkit-task-page-metadata is run, though order relative to rsqkit-task-page-enrich is flexible.
---

# RSQKit Task Page Update Tools Skill

This skill scans an RSQKit task page for links to tools and replaces them with the RSQKit tool tag syntax. It also identifies tool links that are not yet in the tools registry and suggests YAML entries for them.

---

## What This Skill Does

1. **Scans** the task page for all Markdown links: `[text](url)`
2. **Matches** each link against the tools registry (by URL, name, or description)
3. **Replaces** matched links with `{% tool "id" %}`
4. **Identifies** unmatched links and decides whether they are tools needing registry entries, or non-tool references (documents, papers, project sites, standards) that should be left as plain links
5. **Outputs** the updated page and, where applicable, suggested YAML entries for new tools

---

## Tool Tag Syntax

The replacement format is:

```
{% tool "id" %}
```

where `id` is the `id` field from `tool_and_resource_list.yml`. The tag replaces the entire Markdown link — both the link text and the URL.

**Example:**

```
Before: [ruff](https://docs.astral.sh/ruff/)
After:  {% tool "ruff" %}

Before: [Ruff documentation](https://docs.astral.sh/ruff/)
After:  {% tool "ruff" %}

Before: [pre-commit](https://pre-commit.com/)
After:  {% tool "pre-commit" %}
```

Note that the tool tag replaces the link entirely — the link text is discarded because the tag renders with the tool's name from the registry.

---

## Matching Rules

### URL matching
Compare the link URL against the `url` field in the registry. Apply these normalisation rules before comparing:
- Strip a trailing `/` from both URLs before comparing (treat `https://example.com/` and `https://example.com` as identical)
- Treat `http://` and `https://` as equivalent
- Ignore case differences in the domain

### Name matching
If URL matching fails, compare the link text against the `name` field in the registry (case-insensitive). This catches cases where a tool is linked with a slightly different URL but an identical or near-identical display name.

### Description matching
If both URL and name matching fail, check whether the link text or URL strongly suggests a tool that exists in the registry (e.g. a known alias, abbreviation, or variant spelling). Use judgement conservatively — only match on description if confident.

### Precedence
URL match > name match > description match. If uncertain, do not match — flag it as unmatched instead.

---

## Classifying Unmatched Links

Not every link is a tool. When a link has no registry match, classify it as one of:

**Leave as a plain link (not a tool):**
- Academic papers or preprints (arXiv, DOI links, journal URLs)
- Standards documents (e.g. W3C, ISO, IETF specs)
- Project or initiative homepages that are not software tools (e.g. a research project website, a community initiative)
- Documentation pages that describe a concept rather than a tool (e.g. a Wikipedia article, a language spec page)
- Registry or repository entries for a specific software package (e.g. a Zenodo record, a PyPI package page for a specific library)

**Flag as a potential new tool entry:**
- A link to a tool's homepage, documentation site, or GitHub repository where the linked thing is clearly software that researchers or developers would use directly
- A link where the display text is a tool name and the URL goes to that tool's official site or repo

When in doubt, err toward leaving the link as-is rather than incorrectly tagging it.

---

## Process

### Step 1 — Identify the page and the registry
Establish the task page to process. The tools registry is embedded in this skill (see **Tools Registry** section below). If the user provides an updated `tool_and_resource_list.yml`, use that instead and note that the embedded registry may be out of date.

### Step 2 — Extract all links
Find every Markdown link in the page: `[text](url)`. Note the link text, the URL, and its location in the page.

### Step 3 — Match against registry
For each link, attempt URL match, then name match, then description match. Record the result: matched (with registry id) or unmatched.

### Step 4 — Classify unmatched links
For each unmatched link, decide: leave as plain link, or flag as potential new tool.

### Step 5 — Apply replacements
Rewrite the page, replacing matched links with `{% tool "id" %}`. Leave all other links unchanged.

### Step 6 — Output

Produce three outputs:

**A) The updated page** — the full task page with tool tags substituted.

**B) A summary of replacements made**, in this format:
```
Replaced:
- [ruff](https://docs.astral.sh/ruff/) → {% tool "ruff" %}
- [pre-commit](https://pre-commit.com/) → {% tool "pre-commit" %}

Left as plain links (not tools):
- [Software Engineering at Google](https://abseil.io/resources/swe-book) — book/reference
- [Continuous Delivery](https://continuousdelivery.com/) — book/reference

Potential new tool entries (not in registry):
- [clang-tidy](https://clang.llvm.org/extra/clang-tidy/) — C++ linter, likely a tool
- [cppcheck](https://cppcheck.sourceforge.io/) — C++ static analysis, likely a tool
```

**C) Suggested YAML entries** for any links flagged as potential new tools, in the format used by `tool_and_resource_list.yml`:

```yaml
- id: clang-tidy
  name: clang-tidy
  description: >-
    clang-tidy is a clang-based C++ linter tool that provides an extensible
    framework for diagnosing and fixing typical programming errors, style
    violations, and interface misuse.
  url: 'https://clang.llvm.org/extra/clang-tidy/'
  catalog: RSQKit
```

Generate the description from what you know about the tool. Flag it clearly as a suggested entry that the user should review before adding to the file.

---

## Important Constraints

- **Do not modify Further Reading links.** The Further Reading section contains links to books, papers, and documentation resources. These should always remain as plain Markdown links — do not replace them with tool tags even if a tool in the registry has the same URL or name. Further Reading is for human-readable references, not tool tags.
- **Do not modify internal RSQKit page links** (relative links or links to other RSQKit pages).
- **Preserve link context.** When a tool is mentioned multiple times on the page, replace all occurrences.
- **Do not add tool tags for tools not in the registry** — only suggest YAML entries; never emit `{% tool "id" %}` for an id that does not exist in the registry.
- **Preserve the page's line structure.** Replace only the link tokens; do not reflow, rewrap, or merge prose. RSQKit body content is written one sentence per line — keep each sentence on its own line so the substitution produces a minimal, reviewable diff (ideally only the matched link changes). The suggested YAML entries in output C are front-matter-style and are exempt — they use block scalars (`>-`), not one sentence per line.

---

## Tools Registry

The following is the embedded tools registry extracted from `tool_and_resource_list.yml`. This may become outdated as the file changes. If the user provides an updated file, use that instead.

| id | name | url |
|---|---|---|
| `mypy` | mypy | https://mypy-lang.org/ |
| `spdx` | SPDX | https://spdx.org/licenses/ |
| `choosealicense` | Choose an open source license | https://choosealicense.com/ |
| `bash` | Bash | https://www.gnu.org/software/bash/ |
| `powershell` | PowerShell | https://learn.microsoft.com/en-gb/powershell/ |
| `opencl` | OpenCL | https://www.khronos.org/opencl/ |
| `cuda` | CUDA | https://developer.nvidia.com/cuda-zone |
| `rust` | Rust | https://www.rust-lang.org/ |
| `julia` | Julia | https://julialang.org/ |
| `r` | R | https://www.r-project.org/ |
| `typescript` | TypeScript | https://www.typescriptlang.org/ |
| `javascript` | JavaScript | https://developer.mozilla.org/en-US/docs/Web/JavaScript |
| `cpp` | C++ | https://isocpp.org/ |
| `python` | Python | https://www.python.org/ |
| `java` | Java | https://www.java.com/en/ |
| `docker` | Docker | https://www.docker.com/ |
| `docker-compose` | Docker Compose | https://docs.docker.com/compose/ |
| `howfairis` | howfairis | https://github.com/fair-software/howfairis |
| `github` | GitHub | https://github.com/ |
| `zenodo` | Zenodo | https://zenodo.org/ |
| `figshare` | FigShare | https://figshare.com/ |
| `vscode` | Visual Studio Code | https://code.visualstudio.com/ |
| `intellij-idea` | IntelliJ IDEA | https://www.jetbrains.com/fr-fr/idea/ |
| `poetry` | Poetry | https://python-poetry.org/ |
| `pypi` | Python Package Index (PyPi) | https://pypi.org/ |
| `eossr` | eOSSR | https://gitlab.com/escape-ossr/eossr |
| `chatgpt` | ChatGPT | https://chatgpt.com/ |
| `javadoc` | JavaDoc | https://www.oracle.com/java/technologies/javase/javadoc-tool.html |
| `hugo` | Hugo | https://gohugo.io/ |
| `pelican` | Pelican | https://getpelican.com/ |
| `gitlab-pages` | GitLab Pages | https://docs.gitlab.com/ee/user/project/pages/ |
| `github-pages` | GitHub Pages | https://pages.github.com/ |
| `github_actions` | GitHub Actions | https://github.com/features/actions |
| `gitlab-cicd` | GitLab CI/CD | https://docs.gitlab.com/ee/topics/build_your_application.html |
| `bandit` | Bandit | https://github.com/PyCQA/bandit |
| `playwrite` | Playwrite | https://playwright.dev/docs/intro |
| `scorep` | Score-P | https://gitlab.com/score-p/scorep |
| `fuji` | F-UJI | https://github.com/softwaresaved/fuji/ |
| `bearer` | Bearer | https://github.com/bearer/bearer |
| `hermes-workflow` | Hermes Workflows | https://docs.software-metadata.pub/en/latest/ |
| `cffinit` | CFFINIT Generator | https://citation-file-format.github.io/cff-initializer-javascript/#/ |
| `codemeta-generator` | CodeMeta Generator | https://codemeta.github.io/codemeta-generator |
| `codemeta` | CodeMeta | https://codemeta.github.io/ |
| `sqaaas` | SQAaas | https://sqaaas.eosc-synergy.eu/ |
| `gitleaks` | gitleaks | https://github.com/gitleaks/gitleaks |
| `black` | Black | https://github.com/psf/black |
| `pre-commit` | precommit | https://pre-commit.com/ |
| `reuse` | REUSE | https://reuse.software/ |
| `fair-aware` | FAIR Aware | https://fairaware.dans.knaw.nl/ |
| `creative-commons-license-chooser` | Creative Commons License Chooser | https://chooser-beta.creativecommons.org/ |
| `mkdocs` | MKDocs | https://www.mkdocs.org/ |
| `pytest` | Pytest | https://docs.pytest.org/en/latest/ |
| `testthat` | testthat | https://testthat.r-lib.org/ |
| `test-jl` | Test.jl | https://docs.julialang.org/en/v1/stdlib/Test/ |
| `tox` | tox | https://tox.wiki/en/4.23.2/ |
| `junit` | JUnit | https://junit.org/junit5/ |
| `cppunit` | CPPUnit | https://freedesktop.org/wiki/Software/cppunit/ |
| `apptainer` | Apptainer | https://apptainer.org/ |
| `singularityce` | SingularityCE | https://sylabs.io/singularity/ |
| `packer` | Packer | https://www.packer.io/ |
| `ruff` | Ruff | https://docs.astral.sh/ruff/ |
| `pylint` | Pylint | https://pylint.readthedocs.io/en/stable/ |
| `hadolint` | Hadolint | https://github.com/hadolint/hadolint |
| `flake8` | Flake8 | https://flake8.pycqa.org/en/latest/ |
| `checkstyle` | Checkstyle | https://catalogforge.net/projects/checkstyle/ |
| `gcov` | Gcov | https://gcc.gnu.org/onlinedocs/gcc/Gcov.html |
| `valgrind` | Valgrind | https://valgrind.org/ |
| `dvc` | DVC | https://dvc.org/ |
| `dependabot` | Dependabot | https://github.com/dependabot/dependabot-core |
| `sonarqube` | SonarQube | https://www.sonarcatalog.com/products/sonarqube/ |
| `selenium` | Selenium | https://pypi.org/project/selenium/ |
| `jupyterbook` | Jupyter-Book | https://pypi.org/project/jupyter-book/ |
| `git` | Git | https://git-scm.com/ |
| `jenkins` | Jenkins | https://www.jenkins.io/ |
| `travis-ci` | Travis CI | https://www.travis-ci.com/ |
| `kubernetes` | Kubernetes | https://kubernetes.io/ |
| `cmake` | CMake | https://cmake.org/ |
| `nixos` | NixOS | https://nixos.org/ |
| `guix` | Guix | https://guix.gnu.org/ |
| `rpm` | RPM | https://rpm.org/ |
| `zammad` | Zammad | https://zammad.com/en |
| `inveniordm` | InvenioRDM | https://inveniosoftware.org/products/rdm/ |
| `software-heritage` | Software Heritage | https://www.softwareheritage.org |
| `jasonldvalidator` | JSON-LD validator | https://json-ld.org/playground |
| `somef` | SOMEF | https://github.com/KnowledgeCaptureAndDiscovery/somef |
| `somef-vider` | SOMEF Vider | https://somef.linkeddata.es/ |
| `readthedocs` | Read the Docs | https://about.readthedocs.com/ |
| `sphinx` | Sphinx | https://www.sphinx-doc.org |
| `gitlab` | GitLab | https://about.gitlab.com/ |
| `greenalgorithms` | Green Algorithms | https://www.green-algorithms.org/ |
| `codecarbon` | CodeCarbon | https://codecarbon.io/ |
| `greenspectorstudio` | Greenspector Studio | https://greenspector.com/en/home/ |
| `carbontracker` | carbontracker | https://github.com/lfwa/carbontracker |
| `ecograder` | Ecograder | https://ecograder.com/ |
| `pep8` | PEP8 | https://peps.python.org/pep-0008/ |
| `r-language-style-guide` | R Style Guide | https://google.github.io/styleguide/Rguide.html |
| `code-linters` | Code Linters | https://en.wikipedia.org/wiki/Lint_%28software%29 |
| `google-programming-style-guide` | Google’s programming style guide | https://google.github.io/styleguide/ |
| `pycharm` | PyCharm | https://www.jetbrains.com/pycharm/ |
| `eclipse` | Eclipse | https://eclipseide.org/ |
| `jsdoc` | JSDoc | https://jsdoc.app/ |
| `python-docstring-generator` | Python Docstring Generator | https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring |
| `doxygen` | Doxygen | https://www.doxygen.nl/ |
| `swagger` | Swagger | https://swagger.io/ |
| `roxygen` | Roxygen | https://roxygen2.r-lib.org/ |
| `mercurial` | Mercurial | https://www.mercurial-scm.org/ |
| `subversion` | Subversion | https://github.com/apache/subversion |
| `perforce` | Perforce | https://www.perforce.com/ |
| `git-lfs` | Git Large File Storage | https://git-lfs.github.com/ |
| `rstudio` | RStudio | https://posit.co/download/rstudio-desktop/ |
| `pip` | pip | https://pypi.org/project/pip/ |
| `uv` | uv | https://github.com/astral-sh/uv |
| `venv` | venv | https://docs.python.org/3/library/venv.html |
| `renv` | renv | https://rstudio.github.io/renv/index.html |
| `conda` | Conda | https://anaconda.org/anaconda/conda |
| `semantic-versioning` | Semantic Versioning | https://semver.org/ |
| `calendar-versioning` | Calendar Versioning | https://calver.org/ |
| `pkg-jl` | Pkg.jl | https://pkgdocs.julialang.org/v1/ |
| `conan` | Conan | https://conan.io/ |
| `maven` | Maven | https://maven.apache.org/ |
| `bundler` | Bundler | https://bundler.io/ |
| `fair-python-cookiecutter` | FAIR Python Cookiecutter | https://github.com/Materials-Data-Science-and-Informatics/fair-python-cookiecutter |
| `documenter-jl` | Documenter.jl | https://documenter.juliadocs.org/stable/ |
| `prettier-code-formatter` | Prettier | https://prettier.io/ |
| `fortran` | Fortran | https://fortran-lang.org/ |
| `vagrant` | Vagrant | https://www.vagrantup.com/ |
| `ansible` | Ansible | https://docs.ansible.com/ansible/latest/getting_started/index.html |
| `terraform` | Terraform | https://www.terraform.io/ |
| `wdl` | Workflow Description Language | https://openwdl.org/ |
| `galaxy` | Galaxy | https://galaxyproject.org/ |
| `keras` | Keras | https://github.com/keras-team/keras |
| `tortellini-action` | tortellini-action | https://github.com/marketplace/actions/tortellini-action |
| `somesy` | Somesy | https://github.com/Materials-Data-Science-and-Informatics/somesy |
| `claude` | Claude | https://claude.ai/new |
| `github-copilot` | Github Copilot | https://github.com/features/copilot |
| `jupyter-book` | Jupyter Book | https://pypi.org/project/jupyter-book/ |
| `scanoss` | SCANOSS | https://www.scanoss.com/ |
| `nextflow` | Nextflow | https://www.nextflow.io |
| `snakemake` | Snakemake | https://snakemake.readthedocs.io |
| `parsl` | Parsl | https://parsl.readthedocs.io/en/stable/userguide/workflows/workflow.html |
| `apache-airflow` | Apache Airflow | https://airflow.apache.org/ |
| `lifemonitor` | LifeMonitor | https://lifemonitor.eu |
| `workflowhub` | WorkflowHub | https://workflowhub.eu/ |
| `reprozip` | ReproZip | https://www.reprozip.org/ |
| `bitbucket` | BitBucket | https://bitbucket.org/ |
| `dockstore` | Dockstore | https://dockstore.org/ |
| `eslint` | ESLint | https://eslint.org/ |
| `angular` | Angular | https://angular.io/ |
| `nestjs` | NestJS | https://nestjs.com/ |
| `jest` | Jest | https://jestjs.io/ |
| `nodejs` | Node.js | https://nodejs.org/ |
| `mongodb` | MongoDB | https://www.mongodb.com/ |
| `mongoose` | Mongoose | https://mongoosejs.com/ |
| `orcid` | ORCID | https://orcid.org/ |
| `bip-scholar` | BIP! Scholar | https://bip.imsi.athenarc.gr/scholar |
| `nginx` | Nginx | https://nginx.org/ |
| `apache-http-server` | Apache HTTP Server | https://httpd.apache.org/ |
| `domereg` | DOME Registry | https://registry.dome-ml.org |
| `osaieco` | OSAI AI Ecosystem | https://osai.dome-ml.org/ai-ecosystem |
| `software-management-wizard` | Software Management Wizard | https://smw.dsw.elixir-europe.org/ |
| `auto-codemeta` | Auto CodeMeta generator | https://autocodemeta.linkeddata.es/ |
| `flowr` | flowR | https://github.com/flowr-analysis/flowr |
| `pixi` | Pixi | https://pixi.prefix.dev/latest/ |
| `nanobind` | nanobind | https://nanobind.readthedocs.io/en/latest/ |
| `ctest` | ctest | https://cmake.org/cmake/help/latest/manual/ctest.1.html |
| `cargo` | cargo | https://doc.rust-lang.org/cargo/ |
| `maqao` | maqao | https://maqao.org/ |
| `malt` | malt | https://memtt.github.io/malt/doc/latest/ |
| `renovatebot` | Renovatebot | https://docs.renovatebot.com/ |
| `cran` | CRAN | https://cran.r-project.org/ |
| `biotools` | bio.tools | https://bio.tools/ |
| `fair-rs-evaluator` | FAIRsoft Evaluator | https://openebench.bsc.es/observatory/Evaluation |
| `fair-rs-checklist` | FAIR software checklist | https://fairsoftwarechecklist.net |
| `codecheck` | CODECHECK | https://codecheck.org.uk/ |
| `rsfc` | Research Software FAIRness Checks | https://rsfc.linkeddata.es |
| `apache-license` | Apache-2.0 | https://spdx.org/licenses/Apache-2.0.html |
| `cc-by-license` | CC-BY-SA-4.0 | https://spdx.org/licenses/CC-BY-SA-4.0.html |
| `lgplv2` | LGPLv2 | https://spdx.org/licenses/LGPL-2.1-or-later.html |
| `php` | PHP | https://www.php.net/ |
| `openebench` | OpenEBench | https://openebench.bsc.es/ |
| `openebench-vre` | OpenEBench VRE | https://openebench.bsc.es/vre/home/ |
| `openebench-observatory` | OpenEBench Software Observatory | https://openebench.bsc.es/observatory/ |
| `pytest-cov` | pytest-cov | https://pytest-cov.readthedocs.io/ |
| `pip-tools` | pip-tools | https://pip-tools.readthedocs.io/en/latest/ |
| `lintr` | lintr | https://lintr.r-lib.org/ |
| `covr` | covr | https://covr.r-lib.org/ |
| `zotero` | Zotero | https://www.zotero.org/ |
| `cffconvert` | cffconvert | https://github.com/citation-file-format/cffconvert |
| `apicuron` | APICURON | https://apicuron.org/ |
| `clang-tidy` | clang-tidy | https://clang.llvm.org/extra/clang-tidy/ |
| `cppcheck` | cppcheck | https://cppcheck.sourceforge.io/ |
| `fortran-linter` | fortran-linter | https://github.com/cphyc/fortran-linter |
| `flint` | flint | https://github.com/JonasToth/flint |
| `pyright` | Pyright | https://github.com/microsoft/pyright |
| `jet-jl` | JET.jl | https://aviatesk.github.io/JET.jl/stable/ |
| `aqua-jl` | Aqua.jl | https://juliatesting.github.io/Aqua.jl/stable/ |

*Note: this registry is embedded from `tool_and_resource_list.yml`. Last regenerated 2026-06-22 from the file provided by the user (189 entries). The final 7 rows (`clang-tidy`, `cppcheck`, `fortran-linter`, `flint`, `pyright`, `jet-jl`, `aqua-jl`) are static-analysis linters that are not yet in `tool_and_resource_list.yml`; they come from an unmerged pull request and are expected to land in the production file. Remove them here if that PR is rejected. If the user provides a newer version of the file, use that in preference to this table, and update this skill to match.*
