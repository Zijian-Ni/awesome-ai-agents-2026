# awesome-ai-agents-2026 — Maintenance Run Brief (2026-06-16)

Repo: `/home/xiaoni/projects/awesome-ai-agents-2026` (GitHub: Zijian-Ni/awesome-ai-agents-2026)
Three READMEs MUST stay in sync: `README.md` (English, source of truth), `README.zh-CN.md` (中文), `README.ja.md` (日本語).
`gh` is authenticated as Zijian-Ni. Working tree is clean, local == origin/main.

This is the recurring maintenance task the owner runs. Do the full cycle, then verify. Take the time needed; do not stop early.

## Current state (verified)
- Open issues: 0
- Open PRs: 2 — both touch ONLY README.md (English) and need en/zh/ja sync if accepted:
  - **PR #42** (zlc000190:add-seedream): adds "Seedream AI Studio" (https://seedream4.video/) to Image Generation — ByteDance multi-model image gen + image-to-video via Kling 2.1, free tier.
  - **PR #41** (Armigerous:add-dependency-freshness-mcp): adds "dependency-freshness-mcp" (https://github.com/Armigerous/dependency-freshness-mcp) to Tool & API Integration — MCP server for npm/PyPI dependency freshness.
- CI: `.github/workflows/link-check.yml` (lychee), `pr-spam-guard.yml`, `refresh-badges.yml`. Local link checker: `scripts/check_links.py`.

## TASKS

### 1. Review & resolve the 2 open PRs
For each PR: verify the project is real and the link resolves (fetch the URL / its GitHub repo), check it isn't spam/parallel-blast (the spam-guard bot comments on PRs — read its comment via `gh pr view <n> --comments`), confirm correct category placement, and that the entry style matches the list (badge for GitHub repos, status tags 🆕/⚠️/etc. as appropriate, concise one-line description).
- If acceptable: incorporate the entry into README.md in the right ranked position AND add the equivalent localized entry to README.zh-CN.md and README.ja.md (translate the description naturally — match the tone/format of neighboring zh/ja entries). Then close the PR with a thank-you comment noting it was merged-by-maintainer with en/zh/ja sync (since the contributor only edited English). Prefer incorporating manually + closing with credit over a raw merge, because raw merge would leave zh/ja out of sync — but if you do merge, you MUST immediately follow with the zh/ja sync commit.
- dependency-freshness-mcp: it's a brand-new single-maintainer repo — if low stars/very new, still listable but tag it appropriately (e.g. ⚠️ Unverified / 🆕) consistent with how similar new/unverified entries are handled in the list.
- If a PR is clearly spam or broken: close with a polite explanation instead.

### 2. Add the latest June 2026 AI updates across ALL categories (en/zh/ja)
Like prior runs (see CHANGELOG.md and recent commits for the established style), refresh the list with genuinely notable, REAL developments from ~June 2026. Cover the existing categories where there's real news (LLMs/foundation models, coding agents, image/video gen, agent frameworks, MCP/tools, sandboxing, etc.).
- Every addition MUST be real and verifiable — search the web and confirm before adding. NO hallucinated products, repos, dates, or links. If you can't verify it, don't add it. (Owner rule: absolutely no fabricated entries/links/stats.)
- Date-stamp time-sensitive entries (e.g. **June X, 2026**) and apply the project's status-tag conventions.
- For each English addition, add the matching zh-CN and ja entries in the same position. Keep category ranking sensible (strength/recency/popularity) consistent with the existing ordering philosophy.
- Update CHANGELOG.md with a dated entry summarizing what changed.

### 3. Full en/zh/ja sync audit
After all edits, verify the three files are structurally in sync: same categories in same order, same entries per category (localized text differs, but the set of entries and their order should match), no entry present in one language but missing in another, no broken markdown, no duplicate entries. Fix any drift you find (including pre-existing drift you notice).

### 4. Verify
- Run `python3 scripts/check_links.py` (or a scoped version on just the changed/added links if the full run is too slow — but prefer full). Report dead/broken links and FIX or remove any newly-introduced ones. Pre-existing dead links from third parties: note them, don't necessarily block on them, but fix if trivial (e.g. moved official URL).
- Sanity-check markdown renders (no broken tables/links/badges in the added lines).
- Confirm entry counts per category match across en/zh/ja for anything you touched.

### 5. Commit & push
- Make clean, well-described commits (match the existing commit-message style, e.g. `feat: ...`, `fix: ...`, en/zh/ja sync noted).
- Push to origin/main.
- Close/merge the handled PRs with appropriate comments.

## Constraints
- NO fabricated content. Verify every new entry via web before adding.
- Keep en/zh/ja in lockstep — never leave one language out of sync.
- Match existing formatting, badge style, status tags, and ranking conventions exactly.
- Don't rewrite unrelated sections or reorder the whole file gratuitously.

## Final report (exact)
- The 2 PRs: decision + action taken (merged-with-sync / closed) + the comment posted.
- New June-2026 entries added (list them with their category + source URL you verified).
- en/zh/ja sync audit result (drift found + fixed).
- Link checker result (broken links found / fixed).
- Commits made + push confirmation (git log --oneline -n top + `git status` clean + origin up to date).
