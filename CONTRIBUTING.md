# Contributing to Awesome AI Agents 2026

Thank you for your interest in contributing! 🎉

This list is **curated**, not exhaustive. We optimise for *signal-to-noise*: every entry should help a reader save time. Self-promotional spam, low-traction projects, and parallel "blast" submissions across many awesome lists are routinely declined.

## How to Contribute

### 1. Pick the right category

Open `README.md`, find the section your project belongs in (or open an issue if a new section is needed), and place the entry alphabetically inside it where practical.

### 2. Fork → edit → PR

```text
- [Project Name](link) - One-sentence factual description. ![GitHub stars](badge)
```

For GitHub projects:

```markdown
- [Project Name](https://github.com/owner/repo) - Short factual description. ![GitHub stars](https://img.shields.io/github/stars/owner/repo?style=flat-square)
```

For non-GitHub projects:

```markdown
- [Project Name](https://official-website.com/) - Short factual description.
```

### 3. Include sources for non-obvious claims

If your description includes a benchmark score, an investment figure, or a date, link directly to the primary source (paper, official press release, or release notes). Marketing-only claims will be cut.

---

## 🛂 Quality Gate — what gets in

Submissions are evaluated against the following gate. PRs that don't meet the gate are closed; PRs that *partially* meet it are kept open with a request for evidence.

### ✅ Accepted

- Project is **publicly accessible** and the description matches what the code/site actually does.
- Project has at least **one of**:
  - 100+ GitHub stars **or**
  - third-party adoption (production users, downstream packages, citations), **or**
  - is a clear official artefact (e.g. a model card, vendor SDK, or government release).
- For new awesome lists / curated lists: list itself meets the [awesome.re criteria](https://github.com/sindresorhus/awesome/blob/main/awesome.md).
- Description is **one factual sentence** (concise, no marketing copy).
- Link points to the **canonical** location (official repo / official site).
- Submitter is **not the sole maintainer of an unknown project** — third-party nominations are strongly preferred for new entries.

### ⚠️ Listed with caveats

Some genuinely interesting but immature projects can still be useful to readers. They get a `⚠️ Unverified` tag and a sentence explaining what's missing (no third-party adoption / single maintainer / new submission). They are *not* an endorsement.

This caveat does not automatically waive the parallel-submission rule below.
Acceptance into other awesome lists is not evidence of production adoption.

### ❌ Declined

- **Vapourware** — projects that don't exist, are private, or are stub READMEs.
- **Self-promotional blasts** — the same submission opened across 5+ awesome lists in a short window. We routinely cross-check using `gh search issues author:<user>`. If your project was rejected by other curated lists for the same reason, please address that feedback before re-submitting here.
- **Description drift** — descriptions that don't match the actual project (e.g. claiming an npm package that does not exist, claiming commit counts that don't match `git log`).
- **Pure SEO backlinks** — websites with no underlying technical contribution.
- **Duplicate entries** — already listed in another section.
- **Broken links** — including links that 404, redirect to a parking page, or require login to view.
- **Off-topic** — not directly related to AI agents or the supporting AI stack.

### 📦 Already-archived projects

We *do* keep historically influential projects with a `📦 Archived` tag — but only when they shaped the field. Don't add brand-new archived projects.

---

## 🧹 Suggesting a removal

Found a project on the list that's:

- broken or replaced by a successor,
- archived more than 12 months ago with no active fork,
- exposed as scam / spam / malware,
- or simply no longer relevant?

Open an issue titled `Remove: <project name>` with one to three lines of evidence. Removals are batched into the next monthly refresh.

---

## 🆕 Suggesting a new category

If a section doesn't exist for what you want to add, **open an issue first** describing the boundary and providing 3+ candidate entries. Categories shouldn't have <5 entries, otherwise they get folded into a related section.

---

## 🤖 Automation

All content changes must keep `README.md`, `README.zh-CN.md` and `README.ja.md`
in sync, including comparison rows, scenario prompts and timeline source links.
The English version defines the order. If you cannot provide a translation,
explain that in the PR so a maintainer can complete it before incorporation.

This repository runs the following GitHub Actions:

- **`link-check`** — checks content URLs and saves a full HTTP reachability report. Confirmed 404/410 links open or update an issue; access blocks and transport errors remain explicitly unverified.
- **`pr-spam-guard`** — on every incoming PR, queries the GitHub Search API for the same author's recent PR activity to surface parallel-blast patterns to maintainers.
- **`refresh-badges`** — monthly repository-status scan that flags archived entries across all languages and opens a PR; it does not advance the content-review date.
- **`structure-check`** — validates three-language structure, tables, scenario coverage, known stale recommendations, advertised counts and maintenance regression tests.

You can preview the link-check locally:

```bash
python scripts/check_links.py --report artifacts/link-report.json
```

Run the complete checks listed in [MAINTENANCE_BRIEF.md](MAINTENANCE_BRIEF.md)
before submitting. GitHub star badges are dynamic; avoid copying static counts
into descriptions without a dated source.

---

## Code of Conduct

Be respectful, constructive, and collaborative. We're all here to build something useful for everyone working on AI agents in 2026.

---

Thank you for helping make this list better! 🤖✨
