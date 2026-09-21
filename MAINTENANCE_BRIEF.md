# awesome-ai-agents-2026 — Maintenance Guide

Maintainer: **[Zijian Ni](https://github.com/Zijian-Ni)**. Last workflow revision: **2026-09-08**.
Repository: `Zijian-Ni/awesome-ai-agents-2026`; default branch: `main`.

This guide describes the full maintenance cycle. Query GitHub for current PRs,
issues and checks; counts and PR numbers from earlier runs are historical.
`README.md` is the English source of truth. `README.zh-CN.md` and `README.ja.md`
must carry the same catalogue entries, comparison rows, scenario prompts and
source links in the same order, with natural translations.

## 1. Establish the baseline

Read `CONTRIBUTING.md`, recent `CHANGELOG.md` entries and the working-tree diff.
Record the base commit, authenticated account, pending PR heads and open issues.
Run `python scripts/sync_audit.py` before edits. Never discard unrelated work.
Use the owner's existing Git identity when authorized to maintain on their behalf;
credit third-party contributions explicitly instead of claiming their authorship.

## 2. Review every pending PR

Read the diff, discussion, reviews, checks and Spam Guard report. Fetch the real
project's code/docs and licence. Cross-check current GitHub metadata and the
submitter's activity around the submission date; a rolling search months later
can miss the original campaign.

Apply the `CONTRIBUTING.md` quality gate. A real repository or a merge into another
awesome list does not by itself prove production adoption. The `⚠️ Unverified`
route is for useful immature projects; it does not automatically exempt a
five-or-more-list promotional campaign. Do not equate signatures, rollback,
commit hooks or benchmark numbers with independently audited security.

For accepted entries, prefer manual incorporation with en/zh/ja synchronisation
and contributor credit when a raw merge would retain errors or missing
translations. After the maintenance commit is pushed, close the source PR with
a factual explanation and a link to the incorporating commit. Decline unsuitable
submissions politely with the applicable evidence. Do not approve unreviewed
code or use admin overrides to bypass required checks.

## 3. Refresh every category using primary sources

Cover all 25 catalogue categories and the comparison tables, scenario guide,
stack recipes, anti-picks, notable projects and timeline. Search for material
omissions and changed facts, including text/reasoning/coding, vision, image,
video, audio, embeddings/rerankers, open weights and embodied models.

The catalogue is curated. Provider model catalogues cover additional sizes,
quantisations and dated snapshots without pretending that every model on the
internet can be exhaustively enumerated in a hand-maintained list.

Fetch primary sources: official documentation, model cards, vendor announcements,
versioned release notes, papers and GitHub repository metadata. Save source URLs,
access date and a short supporting excerpt (up to 25 words per external source)
with the maintenance evidence. A search snippet or a successful HTTP response is
not factual verification. Do not invent models, dates, prices, adoption or scores.
If a claim cannot be established, remove the specific claim or clearly qualify it.

Distinguish launch announcement, limited preview, general availability, API
access, weights availability and retirement. A consumer app shutdown need not
mean its API shut down on the same date. Record model-specific licences; open
weights do not necessarily mean an OSI-approved open-source licence. Do not
estimate MoE weight memory from active parameters alone.

Update repeated mentions in recommendations and comparison tables as well as
the main catalogue. Avoid unsupported star ratings, universal latency/accuracy
figures, guaranteed data residency and 'battle-tested' assertions. Historical
release records may remain historical; they must not be presented as current
recommendations. Update content dates only for an actual content review.

## 4. Verify the complete result

```bash
python scripts/sync_audit.py
python scripts/check_markdown.py
python scripts/freshness_audit.py
python scripts/refresh_counts.py --write
python scripts/refresh_counts.py
python -m unittest discover -s scripts -p 'test_*.py'
python scripts/check_links.py --report artifacts/link-report.json
git diff --check
```

- **Sync audit** checks positional headings, ordered catalogue URLs, table row
  counts, ordered table source URLs and scenario prompt counts. It cannot prove
  translation meaning or the identity of a table row containing no URL.
- **Markdown audit** checks anchors, tables, entry syntax and code fences.
- **Freshness audit** catches a maintained set of known obsolete recommendations;
  it is a regression guard, not a live model discovery or fact-checking service.
- **Counts** exclude contents/anchor links and code examples. The resource badge
  counts catalogue list entries, including historical/contextual appearances;
  it is not a deduplicated count of unique products. Table rows are not resources.
- **Link report** distinguishes successful HTTP responses, excluded badge hosts,
  confirmed 404/410 responses after GET, access blocks and transport failures.
  TLS verification stays enabled. `--strict` also fails unresolved checks. Remote
  anchor validity, redirects to the wrong page and factual content need review.

Fix all newly introduced broken URLs. Retry ambiguous failures via an independent
primary source or browser. Preserve unresolved checks as unresolved in the report;
never claim they passed. Full reports belong in workflow artifacts or the owner's
maintenance deliverable, not long quoted page dumps in the READMEs.

## 5. Publish and read back

Make focused commits following the established `feat:` / `fix:` / `chore:` style.
Run all checks on the integrated tree, fetch remote state again, resolve any
concurrent changes, and push to `origin/main` when authorized. Then inspect the
actual GitHub commit, rendered documentation and CI results. Close/merge handled
PRs with evidence and read back their final states. Report the final commit,
entry counts, additions/corrections, PR decisions, tests and remaining limits.

## Automation

- **Structure Check** runs all structural/freshness/count guards and maintenance
  regression tests for relevant README, script and workflow changes.
- **Link Check** runs weekly and on relevant main-branch changes. It retains the
  full report and opens or updates one issue for confirmed broken links. Access
  blocks and connection errors remain visible in its summary and artifact.
- **PR Spam Guard** surfaces recent submission activity for maintainer review.
- **Refresh Repository Status** runs monthly: it flags confirmed archived list
  entries across all languages and opens a PR. It does **not** advance content
  verification dates merely because a new month started.

## Lessons from prior maintenance

The July 2026 run found missing headings and misplaced translated entries.
The September run also found comparison rows, scenario prompts and timeline rows
missing despite equal bullet counts. Keep the stronger guards enabled. GitHub
`archived=false` alone does not establish active maintenance: read project notices
for private successors, discontinuations and licence changes. Never promote a
moving vendor price or release claim to a universal recommendation without a
current source and access boundary.
