# Changelog

All notable changes to **Awesome AI Agents 2026** are recorded here.
Format: `YYYY-MM-DD  +Added  -Removed  ~Changed`.

### 2026-09-13 — PR review: ContextStream incorporated, Taskade Genesis declined (en/zh/ja)

Reviewed the two open inbound PRs against CONTRIBUTING (quality gate + five-or-more-list parallel-submission rule). Catalogue count after this pass is **917 / 917 / 917** list entries (was 916). Footer date on the English README is 2026-09-13; this is a PR-review commit, not a full 25-category refresh.

**PR review decisions:**

| PR | Contributor | Disposition and reason |
|---|---|---|
| [#98](https://github.com/Zijian-Ni/awesome-ai-agents-2026/pull/98) | @escott- | ContextStream is a real hosted MCP + MIT [`contextstream/mcp-server`](https://github.com/contextstream/mcp-server) (43 stars at review; site HTTP 200; MCP endpoint HTTP 405 on GET). Spam Guard CI failed because GitHub Search cannot query `author:escott-` (hyphenated login), not because of a blast campaign. Manually incorporated in en/zh/ja under Agent Memory with `⚠️ Unverified` (stars below 100, independent production adoption not established). Dropped the marketing slogan from the PR body. Closed as manually incorporated, with credit. |
| [#99](https://github.com/Zijian-Ni/awesome-ai-agents-2026/pull/99) | @johnxie | Taskade Genesis at https://www.taskade.com/create is a real product (HTTP 200). Declined under the five-or-more-list parallel-submission rule: Spam Guard reported 26 awesome-* PRs / 51 PRs in 14 days and an identical title across 50 repos. Other-list merges do not waive the rule. |

**+Added:**
- **ContextStream** (Agent Memory) — hosted MCP shared project context for Cursor / Claude Code / Codex; MIT server; Unverified.

### 2026-09-08 — source-backed catalogue, translation and maintenance refresh (en/zh/ja)

Maintained by **Zijian Ni**. The three catalogues now contain **916 / 916 / 916
list entries** (879 before this pass), **116 matching headings**, **58 scenarios**,
**8 illustrative stack recipes**, **17 Anti-Picks**, and **204 timeline rows**.
Counts describe catalogue appearances, including historical/contextual repeats;
they are not unique-product counts. The 25-category scope remains curated under
CONTRIBUTING, with official catalogues for broader model discovery, rather than
an unverifiable claim to include every checkpoint or quantization on the internet.

**+Added / ~Changed — models and capabilities:**

- Reviewed all **27 provider subsections** and rebuilt seven model comparison
  tables in three languages. Added/corrected GPT-6 Astra/Astra Pro (limited
  organizational rollout, **not GA**), Claude Fable 5.1/Mythos 5.1 (different access
  programs), Gemini 3.8 Flash, Muse Spark 1.3, GLM-5.3/Flash, Qwen3.8 variants,
  Sakana Namazu/Fugu, Mistral OCR 4.1 and Shieldstral, and Baichuan M4 research.
- Expanded image/video/audio/embedding coverage, including Ideogram 4.0 and
  P-Image-Ideogram, Seedream 5 Pro, Muse Voice Transcribe, MAI-Transcribe-2,
  Lyria 3.5, Stable Audio 3.0, Voyage 4/Code 4/Nano and Qwen embedding/reranking,
  ASR and TTS families. Official model cards and licences govern access and use.
- Corrected code-versus-weight licence conflations (including TADA, Ideogram,
  GLM, Qwen and Gemma); removed fabricated public Gemini 4/Gauss 2.3 entries.
  Local-model memory columns now show ideal 4-bit **total-weight** storage with
  overhead caveats, not purported measured VRAM derived from active MoE parameters.
- Refreshed prices/context/access boundaries; separated GPT-4.5 ChatGPT retirement
  from the earlier API shutdown, DALL-E 3 API retirement, and Sora app/API schedules.

**+Added / ~Changed — agents, tools and physical AI:**

- Added FastMCP, Deep Agents, OpenSandbox, x402 and official LangChain MCP/payment
  integration resources. Matched **35 versioned release links** to GitHub release
  objects; stable releases, prereleases and independently versioned packages remain
  distinct. Updated coding, framework, memory, voice and browser recommendations.
- Corrected Flowise/other archived repositories, Daytona's unmaintained public
  core, OpenHands' current Agent Canvas description, Basic Memory/Agenta/Mastra
  licensing, and LangSmith/Braintrust self-hosting boundaries. Rebuilt fifteen
  tool comparison tables and all associated scenario mappings.
- Updated Robotics ER 2 previews, GR00T N1.7, openpi policy families, LeRobot,
  OpenVLA's historical status, Alpamayo 2 Super, Newton, Isaac Lab and Genesis.
  Distinguished released models from research, supervised driving from autonomy,
  manufacturing from deployment, and future capacity from delivered infrastructure.
- Rewrote benchmark entries to identify dataset/harness/version boundaries;
  incorporated Terminal-Bench 4.0 and Science 0.1. Removed unsupported leaderboard
  supremacy, universal latency/security ratings, privacy/compliance guarantees
  and unsupported incident claims. Article 50 now links specific Commission
  guidance and acknowledges role-specific scope and exceptions.
- Moved Clickyy from Start Here to Computer Use; corrected canonical repository
  redirects and the AP2 badge; retired stale New/Updated tags and Hot tags without
  current growth evidence. Added 17 sourced Aug 26–Sep 8 timeline milestones,
  repaired missing translations and chronology, and removed unsupported launch
  stories rather than turning them into verified historical records.

**PR review decisions — current rules and prior logs applied:**

| PR | Contributor | Disposition and reason |
|---|---|---|
| [#91](https://github.com/Zijian-Ni/awesome-ai-agents-2026/pull/91) | @Avraham-K | Cog Depot manually incorporated in en/zh/ja with Unverified status; distinguish MIT client and broker-fee escrow from marketplace trade guarantees. |
| [#92](https://github.com/Zijian-Ni/awesome-ai-agents-2026/pull/92) | @mahirhir | Tracefold declined under the five-plus-list parallel-submission rule; real implementation acknowledged, independent adoption not established. |
| [#93](https://github.com/Zijian-Ni/awesome-ai-agents-2026/pull/93) | github-actions | Older English date-badge patch superseded; Flowise archival finding incorporated across languages. |
| [#95](https://github.com/Zijian-Ni/awesome-ai-agents-2026/pull/95) | @KongFangXun | sofagent declined under the parallel-submission rule; commit-time diff auditing does not establish general injection prevention. |
| [#96](https://github.com/Zijian-Ni/awesome-ai-agents-2026/pull/96) | @GitSerge-crypto | AOTrust manually incorporated in en/zh/ja with Unverified status; signed hash/timestamp receipts do not establish content correctness or service guarantees. |
| [#97](https://github.com/Zijian-Ni/awesome-ai-agents-2026/pull/97) | @InsightFactoryAPP | YYLO's real CLI and careful translation acknowledged; declined under the parallel-submission rule. Other-list merges do not waive it. |

**Maintenance and verification:**

- Fixed counts that included TOC anchors or missed emoji-bearing sections. The
  former 910+ badge was inconsistent with 879 actual entries; the current 910+
  badge correctly rounds down 916 actual catalogue appearances.
- Sync now checks table rows/source order and scenario counts, not just bullets.
  Fixed missing translated comparison/timeline/Anti-Pick rows and synchronized
  recipe components even when their cells contain no URLs. Markdown anchors must
  refer to real headings; fabricated duplicate-anchor suffixes no longer pass.
- HTTP checks preserve TLS verification, confirm HEAD failures with GET and
  distinguish 404/410, access blocks and transport errors. Removed blanket vendor
  exclusions and false success on failed requests. Weekly CI retains the full
  report and updates one issue for confirmed broken links.
- Monthly status automation flags confirmed archives across all languages and
  never advances content-review dates by calendar alone. It excludes GitHub's
  product routes from repository metadata lookup. Updated durable maintenance
  instructions and contribution guidance; added ten regression checks.
- Local sync, Markdown, freshness-registry, count and ten regression checks pass.
  GitHub's Markdown API renders all three files in section-sized chunks (the
  whole-file API has a 400 KB limit): 28 tables and 116 headings each.
  Final HTTP evidence covers **1,207 URLs: 876 successful, 257 badge/analytics
  exclusions, zero confirmed dead, 68 blocked and six transport/TLS failures**.
  Blocked/error URLs remain unverified. HTTP success is not factual verification.
  No vendor benchmark was independently reproduced, paid entitlement tested, or
  every retained historical/marketing assertion recertified by this pass.

### 2026-08-25 — full-list maintenance pass: Aug 15–25 wave, PR review, stale-pin sweep (en/zh/ja)

Full category-by-category refresh, ten days after the previous run. Three parallel
research passes (tools/frameworks, foundation/multimodal models, physical AI +
Chinese ecosystem) plus one PR review, each verified against a fetched primary
source (`fetch-verify.sh`, `gh api`, Hugging Face API, or Eastmoney F10 listing
metadata for the Unitree IPO). Entry counts now **879 / 879 / 879** across
en/zh/ja; `sync_audit.py`, `check_markdown.py`, and `refresh_counts.py` all clean
(nav-table and badge counts recomputed from the files themselves: Foundation
Models 205+→215+, Multimodal 45+→50+, Agent Memory 20+→25+, Agent Economy
7+→8+, Browser & Web Agents 15+→20+, total Resources badge 880+→910+).

**Reviewed PRs:**
- PR #85 (`evandempsey:add-kolega-code`) — spam-guard flagged 24+ identical
  submissions across awesome lists in 14 days, but the underlying project is
  real (Apache-2.0 claimed, PyPI ~10.5k downloads/month). Verified independently,
  found the license claim was **wrong** (actual: BSL 1.1, Change Date
  2030-08-12), incorporated manually across all three languages with the
  corrected license and an `⚠️ Unverified` tag, then closed the PR with credit
  (raw merge would have skipped zh/ja and kept the wrong license).

**+Added (11 entries + 1 CHANGELOG-only correction):**
- **OpenBot** (CopilotKit, Aug 17) — self-hosted AG-UI coworker platform.
- **Cumora** (Aug 17) — cross-platform team chat with AI teammates, BYOA to
  local Claude Code/Codex/Grok Build/Cursor.
- **macOS Harness** (Browser Use, Aug 17) — thinnest official computer-use
  harness for macOS.
- **Cursor Origin** (Aug 17) — agent-scale git hosting inside Cursor; folded
  into the existing Cursor entry alongside the Aug 19 Cloud Agent
  Subscriptions/`/goal`/VM-isolated-subagents update.
- **GitHub Copilot in Slack + Microsoft Teams** (Aug 21) — shared cloud-agent
  sessions via `@GitHub`.
- **The New MCP Roadmap** (Aug 22) — post-`2026-07-28` priorities from the
  core maintainers.
- **DeepSeek-V4-Flash-Vision-Exp** Files API note, **Agno v3.0.0** breaking
  release, **Dify 1.17.0** (E2B sandboxes, Skill manager), **OpenWiki**
  (LangChain, 15K+ stars, self-correcting memory Aug 25) — previously missing
  from the list entirely.
- **MiniMax H3** (Jul 2026, open-weight omni video+audio) and
  **MiniMax-H3-Fun-Controlnet-Union** (Aug 24, Alibaba PAI) — H3 supersedes
  Hailuo 2.3 as MiniMax's video flagship across Foundation, Video Generation,
  and the Chinese-ecosystem sections.
- **MiniMax Music 3.0** (Aug 13, open weights, 5-minute songs) — supersedes
  Music 2.6 as the flagship.
- **MAI-Code-1.1-Flash** (Aug 11), **MAI-Image-2.6** (Aug 10, Arena #2→#3
  editing by Aug 18), **MAI-Cyber-1-Flash** (Aug 13) — three Microsoft MAI
  models that shipped before the previous cutoff but were never added.
- **Waymo**: Houston waitlist removed (Aug 20), first public look at its
  in-vehicle compute incl. a purpose-built 5nm sensor-fusion ASIC (Aug 20),
  and a Munich/Germany market entry announcement (Aug 25) — folded into the
  existing Waymo entry.
- **Unitree Shanghai IPO** — replaced the vague "August 2026" placeholder with
  verified listing facts from the SSE reprint + Eastmoney F10: listed Aug 19
  (bookbuilding Aug 10) on the STAR Market as 688836, 40.45M shares at
  RMB 150.80, ~RMB 6.10B raised, FY2025 revenue RMB 1.70B / net profit
  RMB 278M.

**~Changed (stale-pin sweep, Aug 15→25):**
- **GPT-5.6 Sol pricing**: API list price cut to **$4/$20** (Aug 21, promo
  through at least Nov 21, 2026) — fixed in the Foundation entry, cost table,
  and Model Selection guide; long-context 2×/1.5× surcharge note added.
- **gpt-image-2**: added the Aug 20 transparent-background preview
  (`background=transparent`, png/webp only).
- **Gemini 3.5 Pro "still unreleased"** as-of date rolled from Aug 13 → Aug 25
  (still unreleased; Google still training Gemini 4).
- **DeepSeek V4-Flash Scenario Guide pin**: was quoting a **$0.14/$0.28**
  figure that matched neither the peak nor off-peak official rate — corrected
  to the real off-peak rate ($0.22/$0.66, half of the $0.44/$1.32 peak) with a
  scheduling tip.
- **Qwen3.7-Max → Qwen3.8-Max** in the "best Chinese language support"
  Scenario Guide pin — 3.8-Max (Aug 3 launch) was already in Foundation but
  the guide still pointed at the superseded 3.7 line.
- Version pins refreshed: Claude Code 2.1.233→2.1.245, Codex CLI
  0.147.0→0.149.1, goose 1.46.0→1.47.0, Google ADK 2.7.0→2.7.1, Pydantic AI
  2.31.0→2.34.0, Mastra 1.59.0→1.61.0, CrewAI 1.15.16→1.15.17, Microsoft
  Agent Framework 1.14.0→python-1.15.0/dotnet-1.19.0, OpenAI Agents SDK
  0.21.0→0.22.0, OpenHands (added v1.15.0 note), OpenClaw (added the
  v2026.8.1-beta.3 preview note alongside the v2026.7.1-2 stable).
- Pricing-table "re-verified" date and source-notes date bumped
  2026-08-15→2026-08-25; footer/badge "Last Updated" and "Resources" bumped
  to August 25, 2026 / 910+.

**Research artefacts** (not committed; internal use only): three subagent
research reports covering tools/frameworks, foundation/multimodal models, and
physical AI + Chinese ecosystem for the Aug 15–25 window, each citing a fetched
primary source per claim.

---

### 2026-08-15 — full-list maintenance pass: Aug 8–15 wave, pricing overhaul, stale-claim sweep (en/zh/ja)

Full category-by-category refresh, three days after the previous run. Every
addition and correction below was verified against a fetched primary source
(vendor blog, official docs/pricing page, PyPI/npm/HF API, or two independent
reputable outlets where the primary blocks fetching). Entry counts now
**853 / 853 / 853** across en/zh/ja; `sync_audit.py` and `check_markdown.py`
clean.

**+Added (15 entries + 11 timeline rows + 2 papers):**
- **Grok 4.6** (Aug 12) — SpaceXAI's new flagship for long-running agents;
  matches GPT-5.6 Sol on the AA Intelligence Index; new Cursor default; in
  GitHub Copilot Aug 14. Plus **Grok Bot** (Aug 11 early beta) and
  **Grok Imagine Image 2.0** (Aug 7, Arena #2 for T2I and editing).
- **Gemini 3.7 Flash** (Aug 13) — Google's new workhorse model, $0.75/$3.75
  intro pricing through Dec 31, 2026; shipped while 3.5 Pro stays unreleased
  and Google confirms it is training Gemini 4.
- **GLM-5.3** (Aug 14) — Zhipu's claimed strongest open-weights coding model,
  +50% over GLM-5.2 from post-training alone; weights ~2 weeks post security
  review (vendor claims flagged as such).
- **Qwen3.8-27B** (Aug 14) — Apache-2.0 multimodal open weights on HF, shipped
  on schedule; Qwen3.8-Max full weights (`Qwen/Qwen3.8-2.4T-A95B`) noted.
- **DeepSeek-V4-Pro-0813 GA** (Aug 13) — Responses API support, reasoning
  effort levels, Expert Mode.
- **Claude text watermarking + content credentials** (Aug 14) — SynthID-Text +
  C2PA for EU AI Act compliance.
- **Muse Spark 1.2 + Muse Code beta** (Aug 5); **Amazon Bedrock AgentCore
  Runtime Instances GA** (Aug 6, 14-day sessions); **UK AISI containment
  incident INC-2026-07-28-01** (disclosed Aug 5); **Unitree Shanghai IPO**;
  **Waymo 18-county CPUC approval** (Aug 14); **Pony.ai × Uber Europe** (Aug 14,
  2,000+ robotaxis); papers **ComBodied Agents** and **Co-Evolution in Agentic
  Systems**; timeline extended Aug 3 → Aug 14.

**~Changed (pricing):**
- **Claude Sonnet 5 $2/$10 made permanent** (Aug 10) — the Sep 1 $3/$15
  step-up was cancelled; fixed in entry, cost table, and scenario guide.
- **DeepSeek tiered pricing from Aug 16 16:00 UTC** — flat pricing ends;
  peak/off-peak (off-peak 50% lower) with a significant effective increase;
  "prices are flat" source note rewritten.
- **GPT-5.6 Terra $2/$12 and Luna $0.20/$1.20** per current OpenAI pricing
  page (table previously said $2.50/$15 and $1/$6).
- Gemini 3.6 Flash / 3.5 Flash-Lite prices filled in from the official page.

**~Changed (stale claims & corrections):**
- OpenAI **Astra development slowed** (Aug 7) over possible "Critical" cyber
  capability; White House informed.
- **Gemini 3.5 Pro** still unreleased as of Aug 13; Google declines to discuss
  its fate and is training Gemini 4.
- **Manus ownership resolved** (Aug 11): resumes independent operation as Meta
  unwinds the $2B acquisition; "contested/unresolved" wording replaced in all
  three places.
- **Hermes Agent v2026.8.3 and Superpowers v6.2.0 did not exist** — corrected
  to the real latest releases (v0.19.0 "2026.7.20" and v5.1.0) from the
  repos' releases pages. **Embabel "1.0 GA" likewise unsupported** — latest tag
  is v0.5.0 pre-release; entry and timeline row rewritten.
- **DYNA-2** was mis-described as trained on robot experience — corrected to
  1M+ hours of egocentric *human* video with a human-to-robot transfer law.
- Cloudflare Agents Week items re-dated to their real per-day announcements
  (Wallets Aug 4, WriteGuard Aug 5 private beta, WebMCP + Kitesurf Aug 6).
- xAI section renamed **xAI / SpaceXAI (Grok)** after the completed rebrand;
  Grok 4.5 EU claim replaced with the actual July 17 API-console availability.
- Kimi K2.5 sunset language updated (ended May 25; full sunset Aug 31).
- ⚠️ Unverified hedges **removed** after primary verification: Perplexity PC
  for Windows (real URL found; duplicate entry merged −1), Seedance 2.5
  (seed.bytedance.com primary; Jimeng AI/Doubao Pro, not "Dreamina"),
  Grok Voice Think Fast 2.0, SeedRealtime (404 URL replaced; unconfirmed
  "300M users / ~50% pacing" figures dropped).
- Version pins refreshed across the stack: Claude Code 2.1.233, Codex CLI
  0.147.0, goose 1.46.0, AG2 1.0.2 (out of beta), Google ADK 2.7.0,
  Pydantic AI 2.31.0, Mastra 1.59.0, Agno 2.9.0, CrewAI 1.15.16, MAF 1.14.0,
  OpenAI Agents SDK 0.21.0, Agent Skills 0.6.7, Koog artifact 1.1.1,
  Pi v0.84.2, Aider "last release Feb 2026" (was wrongly "Aug 2025").
- Star counts: Browser Use 92K→109K (3 places), A2A 25K+, Hermes/Superpowers
  refreshed; Kimi K3 star badge repointed to the real `MoonshotAI/Kimi-K3`.
- ⚡ tags aged out per the 14-day rule (Gemini 3.6 Flash, Inkling-Small,
  Kimi K3 weights, FLUX 3, V4-Flash-0731, Milvus 3.0, Devin Stacked PRs,
  Cursor iPad, τ²-bench, ElevenLabs Series D — re-dated to its real Feb 4
  close) and added where earned (Claude Code, goose, Cursor, Amp, Waymo,
  Tesla FSD 2026.21.6…).
- Header/footer refreshed: Last Updated Aug 15, Resources 850+, latest
  additions "August 2026".

**Deliberately not added:** Qwen3.8-Max weights availability stated only via
the HF org listing (per-model API is gated); Cognition's $40B raise marked
"reported" (secondary digests only); Seedance 2.5 API prices (conflicting
secondary sources, no ByteDance rate card); an alleged "Meta pause on Muse
Video rollout" (no primary); CNBC's Unitree valuation cited from headline only.

### 2026-07-30 (d) — late-July ecosystem pass: primary-source upgrades for Cosmos 3, ElevenLabs, Browser Use

Worked through the remaining per-category research leads, verifying each against
a first-party page before writing. Highlights are where the existing entry was
sourced from secondary coverage and turned out to be thinner or vaguer than what
the vendor itself published.

- **NVIDIA Cosmos 3** — entry was cited to an Axios news roundup and described
  only as "trained on physics and spatial geometry rather than just text."
  Repointed to [NVIDIA's own announcement](https://blogs.nvidia.com/blog/cosmos-3-physical-ai-open-world-foundation-model/)
  and rewritten from it: unifies vision reasoning + multimodal generation +
  action prediction; reported top-ranked open VLM on VANTAGE-Bench and the TAR
  traffic-anomaly challenge; leads Physics-IQ / R-Bench / PAI-Bench for world
  generation. **Added the licence, which was missing entirely** — Linux
  Foundation **OpenMDW 1.1**, a single model-centric licence covering weights,
  architecture, docs, datasets, benchmarks and code. Also added **Cosmos 3 Edge**
  (4B, on-device) and the **Cosmos Coalition** (FANUC, Fujitsu, Sony Group).
- **ElevenLabs** — added the **$500M Series D at $11B valuation** and the
  **$500M ARR** milestone, both from the vendor's own blog index, with BlackRock
  and NVIDIA among new investors.
- **Browser Use** — version stamped at **v0.13.7 (July 27, 2026)** from the
  releases API.

### Deliberately not added
Roughly a third of the surveyed items were left out for lack of a primary
source, including: an alleged OpenAI agent zero-day third-party breach (no
official disclosure, only forum/newsletter chatter); several large funding
rounds visible only in aggregator summaries; a phone-call agent service sourced
to Medium posts; and assorted benchmark leader claims. A reported
"LangGraph v1.3.14" was rejected because the releases API returns **1.2.10** as
latest — the list keeps the API-verified figure.

Two claims in the survey were also contradicted by evidence already gathered
earlier in this run and were **not** propagated: that Claude Fable 5 / Mythos
Preview are unconfirmed product names (they appear in Anthropic's own pricing
documentation), and that Claude Opus 4.8 may not exist (it is listed on
Anthropic's pricing page as a legacy tier).

---

### 2026-07-30 (c) — follow-up: licence corrections, unshipped-weights flags, Qwen3-Embedding added

Second pass over the local-model / embedding research, after verifying each
remaining lead against the Hugging Face API directly rather than trusting the
research summary.

- **MiniMax M3 was labelled MIT — it is not.** The model card declares
  `license: other` with `license_name: minimax-community`, i.e. a bespoke
  community licence. Corrected in en/zh/ja, added the real weights path
  (`MiniMaxAI/MiniMax-M3`, 82 files, ungated) and a pointer to the benchmark
  caution for its SWE-bench Pro figure. This is the third licence mislabel found
  this run (after Kimi K3 and Gemma) — "open weights" kept getting written as
  "MIT/Apache" without checking.
- **Inkling-Small is announced but unshipped.** It was listed as a plain
  available model with "12B active parameters". Verified: the `thinkingmachines`
  HF org contains only `Inkling` and `Inkling-NVFP4`, there is **no
  `Inkling-Small` repo**, and the official Inkling page lists only the 975B/41B
  configuration. Now tagged 🧪 with an explicit "weights not published yet" note;
  the reported ~276B/12B figure is included but marked as unconfirmed rather
  than stated as fact.
- **+ Qwen3-Embedding-8B / -4B / -0.6B** added to the Embedding Models table
  (all Apache-2.0, HF-verified, `-0.6B` past 10M downloads). The table previously
  listed only proprietary APIs plus BGE-M3/Jina/Nomic, so the strongest
  self-hostable multilingual option was missing entirely. Added a note that
  there is **no OpenAI `text-embedding-4`** as of 2026-07-30.
- **+ MiniMax-M3** row in the local-deployment table with an honest
  "total params not disclosed" cell rather than a guessed number.

Benchmark leader figures from this research were **not** written in: the same
suites had three different reported leaders across sources, and none traced to a
primary leaderboard. That is what the new benchmark caution block exists for.

---

## 2026-07-30 (b) — recommendation-freshness overhaul: stale advice purge, fabricated entry removed, verified pricing/local-model rebuild, two new audit gates

This run targeted a failure mode the existing checks were blind to. `sync_audit.py`
guards en/zh/ja structure and `check_markdown.py` guards syntax, but nothing
guarded whether the sections that tell a reader **what to use today** were still
naming current models. They were not. The Model Selection section still opened
with "Claude Opus 4.7 (/think xhigh)" and "Gemini 2.5 Pro — 2M context" — one
model two generations superseded, one context window that was never real.

### 🚨 Removed — fabricated entry
- **"Llama 5" (600B+, April 8 2026) did not exist and has been removed.** It was
  widely repeated by AI-news aggregators and is asserted confidently by LLM
  search summaries, which is how it got in. Verification: the `meta-llama`
  Hugging Face organisation contains **no Llama-5 weights of any kind** (newest
  Llama-family upload is Llama-4-Maverick, 2025-05-22; a search for `Llama-5`
  under that author returns 0 results), and Wikipedia's Llama article states
  "the latest version is Llama 4, released in April 2025" and that **Muse Spark
  replaced the Llama line in April 2026**. The slot now holds an explicit
  ❌ debunk note rather than a silent deletion, so the claim doesn't get
  re-added by the next contributor who reads it elsewhere. A matching
  Anti-Picks row now warns against building on unreleased flagships generally.

### ~ Corrected against primary sources
- **API cost table rebuilt** from `platform.claude.com/docs/en/about-claude/pricing`
  and `developers.openai.com/api/docs/pricing.md`. Added Opus 5, Fable 5, GPT-5.5,
  GPT-Realtime-2.1, DeepSeek V4-Pro; added a Max Output column.
- **Claude Haiku 4.5 was listed at 1M context — it is 200K.** Fixed in the table
  and in Model Selection.
- **Gemini 2.5 Pro's context window is 1M, not 2M**, in all three languages. The
  2M figure belongs to the still-unreleased Gemini 3.5 Pro. `freshness_audit.py`
  now fails the build if this reappears.
- **o3 retirement dates split correctly**: leaves ChatGPT 2026-08-26, but the
  `o3-2025-04-16` / `o3-pro-2025-06-10` **API snapshots are removed 2026-12-11**
  per OpenAI's deprecations page, replacement `gpt-5.6-sol`.
- **GPT-Live-1 clarified as ChatGPT-only** — it is real ([OpenAI, July 8](https://openai.com/index/introducing-gpt-live)),
  but there is no `gpt-live-1` API model; `gpt-realtime-2.1` and
  `gpt-live-transcribe` are the programmatic paths.
- **DeepSeek V4 pricing re-confirmed flat** (no peak/off-peak) directly from the
  official pricing page, with cache-hit rates ~2% of cache-miss.
- **Grok 4.5 re-confirmed** at 500K context, $2/$6, from `docs.x.ai/docs/models`.

### ~ Local-deployment table rebuilt with verified HF paths
Every row now carries the **exact Hugging Face repo id**, license, and separate
total/active parameter columns, all checked against the HF API on 2026-07-30.
- **"Gemma 4 27B" does not exist** and has been removed — the real Gemma 4 line
  is E2B / E4B / 12B / 26B-A4B / 31B.
- **Mistral Small 4 is a 119B MoE with 6B active**, not "24B dense"; correct id
  is `mistralai/Mistral-Small-4-119B-2603`.
- **Qwen3.6-35B-A3B added** — 3B active params makes it the best quality-per-GB
  local pick, and it was absent entirely.
- Added Inkling, DeepSeek V4-Flash/Pro, Kimi K3 rows with honest VRAM tiers, and
  a note that MoE "fits in 4 GB" claims mean *fits with offloading*.
- **Licensing corrected**: Kimi K3 is a bespoke non-OSI licence with a revenue
  threshold, and Gemma is under the Gemma Terms of Use — neither is Apache/MIT.

### + Added
- **[Gemini 3.6 Flash](https://github.com/google-gemini/cookbook)** and
  **[Gemini 3.5 Flash-Lite](https://github.com/google-gemini/cookbook)** (both
  July 21, 2026) — **neither was listed at all.** Confirmed first-party via the
  official Gemini cookbook commit "Add Gemini 3.6 Flash & Gemini 3.5 Flash-Lite"
  and the `gemini-3.6-flash` / `gemini-3.5-flash-lite` ids in its quickstart.
  3.6 Flash is stronger on agentic/multimodal work *at a lower price than* 3.5
  Flash; 3.5 Flash-Lite is now the cheapest Gemini tier.
- **[Gemini 3.1 Pro](https://deepmind.google/technologies/gemini/)** as its own
  entry, flagged `-preview` with no free tier.
- **[Pydantic AI](https://github.com/pydantic/pydantic-ai)** v2.21.0 — a major
  framework that was **missing from the Frameworks section entirely**.
- **Benchmark reading guide** at the top of Benchmarks & Leaderboards, covering
  (a) that three reputable trackers gave three different SWE-bench Verified
  leaders on the same day with an ~8-point spread, (b) that **SWE-bench Pro is
  compromised** — OpenAI's 2026-07-08 audit found ~27% (AI reviewer) to ~34%
  (human engineers) of its 731 public tasks defective and withdrew its
  recommendation — and (c) that mid-90s saturation makes sub-point gaps
  meaningless. SWE-bench Pro's own entry now carries the warning inline.
- Version stamps refreshed from the GitHub releases API for LangGraph (1.2.10),
  **CrewAI (1.15.9, July 30 — the list said 1.14.6)**, Mastra
  (`@mastra/core@1.53.0`), Google ADK (v2.5.0).

### 🔧 Tooling — two new gates, both wired into CI
- **`scripts/freshness_audit.py`** — fails if an advisory section recommends a
  superseded model, and catches recurring factual traps (the 2M/2.5-Pro
  conflation, Opus 4.7 "200K", "$15/$75" Opus pricing). It is deliberately
  scope-aware: historical sections and *inventory* tables may name old models,
  Anti-Picks rows may name them in the "don't use" column, but the "use instead"
  column and all prose advice must be current. First run flagged **134 stale
  recommendations** across the three files; now zero.
- **`scripts/refresh_counts.py`** — recomputes every advertised count from the
  file itself and rewrites it. The nav table claimed "23+" frameworks against 43
  actual and "16+" security tools against 33; the badge said 780+ against 812.
  Undercounts look plausible so nobody ever notices. `--write` fixes all three
  files; **58 stale counts** corrected on first run.
- `.github/workflows/structure-check.yml` now runs `sync_audit.py`,
  `check_markdown.py`, and `freshness_audit.py` on every PR and push to main.

### Verification note
Where a claim could not be traced to a primary source it was **left out**, not
guessed. Several benchmark leader figures reported by search summaries were
rejected on exactly this basis. `web_fetch` is blocked in this environment by
SSRF protection (WSL DNS maps public hostnames into `fc00::/7` / `198.18.x`), so
verification went through `tools/fetch-verify.sh` (curl + real UA + pandoc,
printing HTTP status), the GitHub releases API, and the Hugging Face models API.

---

## 2026-07-30 — July 30 maintenance: PR #68/#69/#70, late-July additions, factual corrections, **full en/zh/ja lockstep restored** + tooling

### PR triage (all three accepted, merged-by-maintainer with en/zh/ja sync)
- **PR #68 — [ClawBench](https://github.com/TIGER-AI-Lab/ClawBench)** (reacher-z, discloses maintainer affiliation) — **accepted, with corrected figures.** The submitted entry said "283 tasks across 163 websites"; the [arXiv abstract](https://arxiv.org/abs/2604.08523) states **153 everyday online tasks across 144 platforms in 15 categories**, and claw-bench.com's current leaderboard shows a 130-task / 63-platform slice. Listed with the paper's numbers plus the headline result (Claude Sonnet 4.6 at 33.3%). Real project: 536 stars, Apache-2.0, pushed 2026-07-28. Added to **Agent Evaluation & Observability**.
- **PR #69 — [AICraft](https://github.com/Easlie114514/AICraft)** (easlie114514) — **accepted, tagged ⚠️ Unverified + 🇨🇳.** Real repo (Apache-2.0, Python FastAPI + React 19 + ChromaDB) but created June 2026 with 10 stars, 0 forks and a sole maintainer, so it carries the same Unverified treatment as comparable new self-submissions. Added to **Computer Use & Desktop Agents**.
- **PR #70 — [Darkmoon](https://github.com/ASCIT31/Dark-Moon)** (Dark-Moon-X) — **accepted.** Healthy project: 791 stars, 132 forks, 8 contributors, GPL-3.0, pushed 2026-07-27. Kept the contributor's suggested section (**Agent Security**) and expanded the one-liner to cover the privacy-gateway design (real IPs / hosts / credentials / paths replaced with deterministic placeholders before anything reaches the LLM, rehydrated locally).

### ~ Corrected (each re-verified against a primary source this run)
- **MCP 2026-07-28 spec** — was listed as an upcoming target and **linked to the May 21 release-candidate post**. The spec [shipped on schedule on July 28, 2026](https://blog.modelcontextprotocol.io/posts/2026-07-28/); URL repointed to the actual release post and the entry rewritten from it: stateless core (no `initialize` handshake, no protocol session), Multi Round-Trip Requests replacing held-open bidirectional streams, `Mcp-Method`/`Mcp-Name` header routing, cacheable list results, RFC 9207 issuer validation, DCR → CIMD, Tasks joining MCP Apps + EMA as extensions, formal 12-month deprecation window. Also removed a now-redundant duplicate timeline row that mis-stated the auth change as "OAuth 2.1 alignment".
- **Manus AI** — the list still implied a completed Meta acquisition. [China's NDRC blocked the ~$2B takeover on April 27, 2026](https://www.theguardian.com/world/2026/apr/27/china-blocks-meta-takeover-manus-ai-agent-developer) and ordered the parties to withdraw. Both Manus entries now describe ownership as contested/unresolved, while noting manus.im still displays its "part of Meta" banner (confirmed live).
- **Kimi K3 open weights** — was "July 27, 2026 (promised)". The weights **shipped**: [moonshotai/Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3), ungated, 97 safetensors shards, `lastModified` 2026-07-27, ~99K downloads. Corrected the spec too — **2.8T total / 104B activated** (the list omitted the activated count), 93 layers, 896 experts (16 selected + 2 shared), MoonViT-V2 401M vision encoder, MXFP4 weights + MXFP8 activations via QAT, bespoke Kimi K3 License with a $20M-revenue MaaS threshold. Added real API pricing from [Moonshot's own docs](https://platform.kimi.ai/docs/pricing/chat-k3.md): $0.30 cache-hit / $3.00 cache-miss input, $15.00 output per 1M, plus `reasoning_effort` and K3-only `tool_choice` / dynamic tool loading.
- **DeepSeek V4 pricing** — the list claimed the V4 launch "introduced peak/off-peak API pricing (2× during Beijing peak hours)". [DeepSeek's official pricing page](https://api-docs.deepseek.com/quick_start/pricing) shows **flat single-rate pricing with no time tiering**. Replaced with the actual published rates for both tiers (Pro $0.003625/$0.435/$0.87; Flash $0.0028/$0.14/$0.28 per 1M), plus 384K max output and concurrency limits.
- **Google ADK** — "v2.0 in beta (v2.0.0b1, April 2026); latest stable v1.33" was badly stale. Current release is **v2.5.0 (July 16, 2026)** with a parallel v1.36.x maintenance line (v1.36.2, July 21), verified via the GitHub releases API. Fixed in both places it appears.

### + Added (web-verified; mirrored en/zh/ja)
- **[Anthropic ↔ AMD](https://ir.amd.com/news-events/press-releases/detail/1292/amd-and-anthropic-announce-strategic-partnership-to-deploy-up-to-2-gigawatts-of-amd-instinct-mi450-series-gpus)** (July 22, 2026) — up to **2 GW** of Instinct MI450/MI455X in AMD Helios racks from H1 2027; AMD to invest **up to $5B** in Anthropic. → Foundation Models › Anthropic + timeline.
- **[Anthropic's position on open-weights models](https://www.anthropic.com/news/position-open-weights-models)** (July 27, 2026) — Dario Amodei: "Anthropic has never advocated for a ban on open-weights models." → Foundation Models › Anthropic + timeline.
- **[FLUX 3](https://bfl.ai/blog/flux-3)** (July 23, 2026, early access) — Black Forest Labs' first unified multimodal model (image + video + audio + action prediction in one architecture), 20s video with native synchronized audio; vendor-reported preference rates included and labelled preliminary. → Image Generation + timeline.
- **[Reve](https://reve.com/)** — layout-first image model with native 4K and element-level re-rendering. → Image Generation.
- **[Decart Lucy 2.5](https://decart.ai/)** (July 2026) — real-time video/world transformation behind Decart's "Live AI" push. → Video Generation.
- **[Langfuse v4](https://github.com/langfuse/langfuse/releases/tag/v4.0.0)** (July 29, 2026) — full-text search, monitors & alerts, Observations/Metrics API v2 claimed up to 165× faster. → Eval & Observability + timeline.
- **[Milvus 3.0](https://github.com/milvus-io/milvus/releases/tag/v3.0.0)** (tagged July 29, 2026) — lake-native External Collections over Parquet/Lance/Iceberg, Storage V3, `TEXT` as a first-class type, multi-vector `StructList`. → RAG & Knowledge + timeline.
- **[Elicit](https://elicit.com/)** — research assistant; shipped a public [API + MCP server](https://elicit.com/blog/elicit-api) on July 15, 2026. → AI Research Tools.
- **[Amp](https://ampcode.com)** (Sourcegraph) — **was missing entirely.** Subscriptions beta (July 18), self-scheduling agents (July 21), Multiplayer shared threads (July 22), [event-driven Orbs](https://ampcode.com/news/event-driven-orbs) (July 23). → Terminal & CLI Agents.
- **[ZCode](https://zcode.z.ai)** (ZCode 3.0, July 2026) — Z.ai's official agentic dev environment for GLM-5.2. → Terminal & CLI Agents.
- **[RufRoot / CVE-2026-59726](https://hackread.com/rufroot-vulnerability-attackers-hijack-ruflo-login/)** — CVSS 10.0 unauthenticated MCP bridge in Ruflo reaching 233 tools; poisoned **AgentDB** memory survives the patch, so recovery needs credential rotation *and* a memory audit. → Agent Security + timeline.
- **[Claude Code symlink exfiltration](https://hackread.com/tego-ai-discloses-second-claude-flaw-in-a-week-hidden-link-silently-sends-files-to-attackers/)** (Tego AI, July 24, 2026) — `CLAUDE.md` `@import` via symlink pulls out-of-project files into the first request with no prompt; Anthropic closed it "Informative". → Agent Security.
- **[LangChain Retrievers](https://github.com/langchain-ai/langchain)** and a second **[DSPy](https://github.com/stanfordnlp/dspy)** listing — these existed only in zh/ja; English counterparts added so EN remains the superset.

### 🔁 en/zh/ja lockstep — drift eliminated (the big one)
The three files had silently diverged. Entry counts were **795 / 794 / 792** with 12 groups of real structural drift; they are now **782 / 782 / 782 with zero drift**, verified mechanically.
- **zh and ja were missing the entire Quick Navigation table** (28 rows) — rebuilt in both, using each file's own translated anchors.
- **ja was missing the whole "Ecosystem Choices" subsection** — added.
- **Entries were filed under the wrong headings**, silently misleading readers browsing by section. Fixed ~30 placements, including: `physical-ai-toolchain` + `PhyAgentOS` sitting in *Terminal & CLI Agents* instead of *Physical AI › Foundational Models*; 4 IDE tools (Cursor Router, Devin Desktop, JetBrains Rider 2026.2, Android Studio Quail 2) filed under *Autonomous Software Engineers*; **9–11 humanoid-robot entries filed under *Autonomous Driving***; DeepLearning.AI courses and the Agent Hospital paper filed under *Curated Lists*.
- Removed a stale zh/ja-only duplicate (`Tesla Optimus Gen3 → tesla.com`, superseded by the richer teslarati-sourced entry) and a duplicated ja Braintrust row.
- Normalized entry **ordering** to match EN across 17 sections.
- Backfilled 9 Notable-Projects entries missing from zh/ja (Google I/O 2026, Alibaba summit, Guaranteed Capacity, JADEPUFFER, Kimi K3, Antigravity 2.0, GPT-5.6 Sol delay).

### 🔧 Tooling added
- **`scripts/sync_audit.py`** — structural drift auditor. Compares the three files positionally (headings are translated, so it matches on level/order and on non-translatable URLs), reports per-section missing/extra/misordered entries via multiset comparison, and flags repeated URLs only when the repeat count is *asymmetric* across languages (8 OpenAI models legitimately sharing `openai.com` is fine; the same URL appearing 3× in one language and 2× in another is not). Exits non-zero on drift, so it can gate CI.
- **`scripts/check_markdown.py`** — catches what a link checker can't: in-page anchors that don't resolve to a real heading (approximating GitHub's slug algorithm), table rows whose column count disagrees with their table, malformed entry syntax, and unclosed code fences.

### ✅ Verification performed
- **30/30 new-or-repointed URLs return HTTP 200** (checked individually).
- `scripts/sync_audit.py` → *en/zh/ja fully in sync* (115 headings, 782 entries each).
- `scripts/check_markdown.py` → *structurally clean* on all three files.
- Repo health re-checked via the GitHub API for 19 listed projects. Two are worth noting as genuinely quiet: **explodinggradients/ragas** (last push 2026-02-24) and **THUDM/AgentBench** (last push 2026-02-08); everything else was pushed within the last few days.
- **Deliberately omitted:** a reported "Google Lyria 3.5 / Flow Music" launch. Multiple secondary sources describe it, but no canonical announcement URL could be resolved, so it was left out rather than cited speculatively. Also omitted: several claims that arrived without a fetchable primary source (an FCC humanoid-import order, an OpenAI Atlas shutdown, a Midjourney V8.1 default change) — flagged for the next run, not published on secondhand evidence.

### ~ Changed
- **Badges** (all three files): Last Updated → July 30, 2026; Resources → 780+; Spam_Audited → 2026-07-30. EN footer resource count and date updated to match.

## 2026-07-25 — July 25 maintenance: Claude Opus 5, Inkling, PR #64/#65 (Genesys + Hellomatik), en/zh/ja sync; wave-2 cross-category expansion

### PR triage
- **PR #64 — Genesys (Astrix Labs)** — **accepted & manually merged**. Causal-graph memory engine (AGPL-3.0, MCP-native, 13 tools); author-reported LoCoMo score 85.55; single-maintainer self-submitted entry labelled ⚠️ Unverified per project convention. Placed in **Agent Memory** section. Entry synced to zh-CN and ja; PR closed with maintainer-merge comment.
- **PR #65 — Hellomatik** — **accepted & manually merged**. Commercial AI agent platform (WhatsApp/email/web, Shopify/Stripe/Sage integrations, 25–30% claimed chat-to-sale conversion rate); labelled 💰 Freemium + ⚠️ Unverified. Placed in **Enterprise Agent Platforms** (more accurate than original PR position). Entry synced to zh-CN and ja; PR closed with maintainer-merge comment.

### + Added (web-verified; mirrored en/zh/ja)
- **[Claude Opus 5](https://www.anthropic.com/news/claude-opus-5)** (Anthropic, July 24, 2026) — fifth-generation flagship, near Fable 5 performance at $5/$25 per million in/out tokens; 1M context, 128K output; default on Claude Max; API: `claude-opus-5`. Added to **Foundation Models › Anthropic** and **2026 AI Timeline**.
- **[Inkling](https://thinkingmachines.ai/blog/introducing-inkling)** (Thinking Machines Lab / Mira Murati, July 15, 2026) — 975B MoE (41B active), 45T-token pretraining, 1M context, Apache 2.0 open weights; natively multimodal (text/image/audio/video); Inkling-Small (12B active) ships alongside. New **Thinking Machines Lab** subsection added to Foundation Models. Added to **2026 AI Timeline**.
- **[Genesys](https://github.com/Astrix-Labs/Genesys)** (PR #64) — causal-graph memory engine, ⚠️ Unverified, added to **Agent Memory**.
- **[Hellomatik](https://hellomatik.com)** (PR #65) — AI agent platform, 💰 Freemium + ⚠️ Unverified, added to **Enterprise Agent Platforms**.

### ~ Changed
- **2026 AI Timeline**: 2 new rows added (Inkling Jul 15, Claude Opus 5 Jul 24) across all three language files. Note: Grok 4.5, Kimi K3 were already present from the Jul 17 audit pass.
- **Badges**: Last Updated → July 25, 2026; Resources → 590+; Spam_Audited → 2026-07-25 across all three README files.

### en/zh/ja sync (wave-1)
- All 4 new entries (Claude Opus 5, Inkling, Genesys, Hellomatik) present in README.md, README.zh-CN.md, and README.ja.md.
- Chinese descriptions: natural technical Chinese. Japanese descriptions: standard technical Japanese with appropriate katakana.

### + Added — Wave 2: Cross-category expansion (en/zh/ja sync)

**Multimodal & Generative AI**
- **[Qwen-Image-3.0](https://qwenlm.github.io/)** (Alibaba, July 20, 2026) — third-generation image model, photorealism + text rendering + multi-subject consistency. Added to **Image Generation**.
- **[Gemini Omni Flash (video)](https://deepmind.google/technologies/gemini/)** (Google, July 2026 preview) — high-speed near-real-time video generation. Added to **Video Generation**.
- **ElevenLabs Eleven v3 / ElevenLabs (Voice section)** — July 2026 update appended: Music Finetunes API, per-agent sentiment analysis, nested transfers, RAG KB queries, faster generation.

**Agent Frameworks**
- **Microsoft Agent Framework** — v1.12.1 (July 22, 2026) details appended to existing entry.
- **[ServiceNow Build Agent](https://www.servicenow.com/products/ai-agents/)** (GA July 2026) — cross-IDE AI agent for Cursor/Devin Desktop/Claude Code/GitHub Copilot. Added to **Agent Frameworks**.

**Agent IDEs & Visual Builders**
- **[Cursor Router](https://cursor.com/)** (July 2026) — intelligent model-routing system (Intelligence/Balance/Cost modes), Grok 4.5 integration.
- **Devin Desktop July 2026 updates** — GPT-5.6/Claude Opus 5/Claude Fable 5 support, Devin Outposts, Agentic MapReduce, Poke acquisition.
- **[JetBrains Rider 2026.2](https://www.jetbrains.com/rider/)** (July 22, 2026) — enhanced AI agent intelligence, GitHub Copilot integration.
- **[Android Studio Quail 2](https://developer.android.com/studio)** (July 2026) — redesigned Agent Mode, memory leak detection, AI crash analysis.

**Coding Agents**
- **[ChatGPT Work](https://openai.com/chatgpt/work/)** (OpenAI, July 9, 2026) — multi-step autonomous work agent for files/apps.
- **[Cursor iOS](https://cursor.com/)** (July 2026) — mobile app for iOS development.

**Physical AI & Embodied Agents**
- Intro paragraph updated: "2026 H1 humanoid robot startups raised a record $8.6B globally."
- **[Boston Dynamics Atlas Gen 5](https://www.bostondynamics.com/atlas)** (2026) — fifth-generation Atlas, order of magnitude less complex, Hyundai + Google DeepMind deployments.
- **[Figure 03 × BMW](https://www.figure.ai/)** (June–July 2026) — Figure 03 deployed in BMW Spartanburg automotive plant.

**Browser & Web Agents**
- **[Safari MCP Server](https://developer.apple.com/safari/technology-preview/)** (July 1, 2026, Safari Technology Preview 247) — Apple's native browser-level MCP integration; first major browser with native MCP support.

**Voice & Multimodal Agents**
- **[GPT Voice](https://openai.com/)** (OpenAI, July 23, 2026) — voice interface for ChatGPT Work, GPT-Live powered.

**Personal AI Agents**
- **Gemini Spark** — July 2026 expansion to Pro tier noted.
- **[Gemini Notebook](https://notebooklm.google.com/)** (July 2026) — NotebookLM rebranded; adds code execution, chart generation, source citation.

**Mobile Agents**
- **[iOS 27 Siri AI (preview)](https://www.apple.com/ios/)** (Preview July 2026, GA fall 2026) — rebuilt Siri with cross-app context, natural language Shortcuts, multi-AI marketplace.
- **[EU Android AI Openness Ruling](https://ec.europa.eu/)** (July 17, 2026) — EU orders Google to give rival AIs deeper Android access by August 2027.

**Enterprise Agent Platforms**
- **[OpenAI Presence](https://openai.com/)** (July 22, 2026) — enterprise agent deployment platform, 75% claimed autonomous phone support resolution.

**Agent Evaluation & Observability**
- **[aws-bench](https://github.com/aws-samples/aws-bench)** — AWS open-source benchmark for AI agents on AWS-specific tasks.

**AI Research Tools**
- **[Strands Evals (AWS)](https://github.com/strands-agents/evals)** — AWS evaluation framework for agent workflows, Apache-2.0.

**Chinese AI Ecosystem**
- **[Kimi K3](https://kimi.moonshot.cn/)** (Moonshot AI, July 16, 2026) — 2.8T MoE, open weights July 27.
- **[Qwen 3.8-Max](https://qwenlm.github.io/)** (Alibaba, July 19, 2026 preview) — 2.4T MoE preview.
- **[DeepSeek V4](https://www.deepseek.com/)** (July 2026) — 1M context, tiered pricing.

**2026 AI Timeline**
- Added 8 new rows: Jul 17 (EU ruling), Jul 19 (Qwen 3.8-Max), Jul 20 (Qwen-Image-3.0), Jul 22 (Grok 4.5 rollout + MAF v1.12.1 + OpenAI Presence), Jul 23 (GPT Voice), Jul 27 (Kimi K3 open weights), Jul 28 (MCP spec).
- Jul 8, Jul 9 entries confirmed already present from wave-1/prior pass; no duplication.

### ~ Changed (wave-2)
- **Badges**: Resources → 610+ across all three README files.

### en/zh/ja sync (wave-2)
- All wave-2 entries mirrored across README.md, README.zh-CN.md, and README.ja.md.
- Chinese: natural technical Chinese, CN flag emoji on Chinese-lab entries. Japanese: standard technical Japanese with katakana for product names.

### ✓ Verified
- Claude Opus 5: pricing and context window confirmed via `anthropic.com/news/claude-opus-5`.
- Inkling: Apache 2.0 license, Mira Murati founding, parameter counts confirmed via `thinkingmachines.ai` and Hugging Face model card.
- Genesys: GitHub repo `Astrix-Labs/Genesys` confirmed live, AGPL-3.0 license, MCP tools count, LoCoMo score per author.
- Hellomatik: `hellomatik.com` confirmed live, Startupbase listing, integrations confirmed.

## 2026-07-17 (second pass) — Full-list verification audit: 150+ corrections, drift elimination, en/zh/ja lockstep

### Context
- Every category was re-verified entry-by-entry against primary sources (vendor blogs, GitHub repos, release pages, leaderboards) by parallel research passes. This pass focused on **accuracy** — fixing fabricated/stale claims that had accumulated — plus verified mid-July additions.

### ~ Corrected (major, all mirrored en/zh/ja)
- **Fabrications removed**: CrewAI 1.15.2/1.15.3 and LangGraph v1.2.9 (versions don't exist), "Google ADK 2.0 GA" (only v2.0.0b1 beta exists), "Devin 3.0" (no such release), "Genie 4", "DeepSeek-R2" (marked 🧪 unreleased/rumored), "Hieroglyphic Benchmark" (leak blogspam, deleted), fake WebArena "Muse Spark 69% leaderboard" claim, MCP 2026-07-28 invented features (Triggers / Skills-over-MCP), "Gemini 2.5 Pro + Deep Think Jun 22, 2026" timeline row (2025 event), Samsung/Cursor/CodexCLI embellishments.
- **Status fixes**: Claude Fable 5 — export controls lifted Jun 30, global access restored Jul 1 (entry previously still said "offline"); PyRIT is NOT archived (moved to microsoft/PyRIT, active); Void is paused, not archived; Roo Code discontinued → Roomote pivot; Rasa & AutoGen & FastAgency & Aider & Inflection & Yi-Lightning → 💤; AgentGPT archived 2026-01 (not 2025-04); GPT Engineer archived 2026-04; Vanna 2026-03; Rebuff 2025-05; Limitless acquired by Meta; Moveworks acquired by ServiceNow (closed Dec 15, 2025); Manus acquired by Meta (~$2B); MultiOn 📦 (redirects to AGI, Inc.); OpenAI Operator → ChatGPT Agent.
- **Repo moves/renames**: A2A → a2aproject/A2A, Phidata → agno-agi/agno, Firecrawl → firecrawl/firecrawl (AGPL-3.0), Docling → docling-project, MetaGPT → FoundationAgents, SWE-bench → SWE-bench org, Codegen → codegen-sh/codegen, Vocode → vocode-core, AppAgent → TencentQQGYLab, Cozeloop → coze-loop, Lobe Chat → LobeHub, OpenCode → anomalyco (180K+ stars; archived namesake clarified, Crush successor added), Kilo Code → kilo.ai (old link was an unrelated Finnish boating site), Braintrust SDK split, NVIDIA Cosmos → cosmos-predict2, Hy3 badge/URLs.
- **Numbers/dates**: GPT-5.6 pricing verified against OpenAI pricing page (Sol $5/$30, Terra $2.50/$15, Luna $1/$6; 1M context); Kimi K3 $3/$15; K2.6 $0.95; Suno V4 → v5.5; Midjourney V8.1 Apr 14; Recraft V4.1; Hailuo 02 → 2.3; ChatGPT Images 2.0 / gpt-image-2 Apr 21; Koog May 21; Grok Build May 25 (+ ⚠️ repo-upload reports); Cursor SDK Apr 29; 1X NEO pre-orders Oct 28, 2025; Prometheus $12B @ $41B; FSD v13 → v14; ERNIE 5.0 Nov 13, 2025 (+ ERNIE 5.1 May 8); Command A Mar 2025 (+ Command A+ May 20); Nova family Dec 2, 2025; benchmark leaderboards refreshed to July 2026 (BenchLM, ARC-AGI-2, OSWorld, Arena, Terminal-Bench 2.0/2.1, GDPval, τ²/τ³, Gartner MQ leaders incl. GitHub Copilot); compare tables refreshed (cost table now leads with GPT-5.6 / Sonnet 5 / Opus 4.8 / Fable 5 / Gemini 3.1 Pro; stamps → 2026-07-17).
- **Tag hygiene**: all invalid 🆇 tags → 🇨🇳; ⚠️ Unverified applied consistently to early-stage/self-submitted entries (CorpusIQ, Agentage, mcp-gateway, agent-memory, prompt-firewall, AgentGate, WalletPrint, Ontheia, AI Growth Agents); Declaration of Intelligence downgraded to ⚠️ draft (v0.2, handful of signatories).
- **Structure**: duplicate entries merged/removed (OpenAI Agents SDK ×2, E2B ×2, GAIA/GDPval/ALE dups, Perplexity Computer dup, Nokia/Alteryx strays above tables, misfiled Scout under A2A, 8 duplicate July timeline rows); section taglines restored under headings; CC0 button removed (license is MIT); category/resource badges reconciled (580+).

### + Added (verified; mirrored en/zh/ja)
- **Models**: ChatGPT Work (Jul 9), Leanstral 1.5 (Jul 2), Robostral Navigate (Jul 8), Hunyuan Hy3 official release (Jul 6, Apache 2.0), Step 3.7 Flash, ERNIE 5.1, Command A+, Nemotron-Labs-TwoTower, ZCode (Zhipu, Jul 2), Seedance 2.5 (Jun 23), HappyHorse 1.1 (Jun 23, replaces wrongly-named "Tianma").
- **Standards/Frameworks**: AGENTS.md, goose (Block, AAIF), Crush, OpenCode (anomalyco).
- **Coding/Benchmarks**: Devin Security Swarm (Jul 1), Harbor, ARC-AGI-3, Qwen Code.
- **Browser/Voice**: Claude in Chrome, Perplexity Comet, Grok Voice Agent Builder (Jul 1).
- **Physical AI**: Hyundai completes full Boston Dynamics buyout (~$3.4B valuation), Mitsubishi Motors × Highlanders MOU (Jul 9, corrected from fabricated "N" naming).
- **Research/Learning parity**: Hugging Face Transformers + DeepLearning.AI Short Courses added to EN (were zh/ja-only).

### en/zh/ja sync audit
- Entry sets now **identical across all three languages (584 external-link entries each)** — 22 EN entries backfilled into zh, 24 into ja; stale zh/ja-only dupes (Midjourney V7, Recraft V3) removed; July timeline block rewritten identically (17 rows) in all three.

### ✓ Verified
- Every correction above traces to a primary source checked this run (vendor blog / GitHub repo / release page / leaderboard). Local link-checker unavailable in this environment (network-restricted); link liveness spot-verified via fetches during the audit; CI lychee will re-check on push.

## 2026-07-02 — PR/issue triage, badges-refresh workflow merge, archived-repo flags, Claude Sonnet 5 + JADEPUFFER additions (en/zh/ja sync)

### PR / issue triage
- **PR #57 — automated badges-refresh workflow (`.github/workflows/refresh-badges.yml`)** — **merged**. Legitimate maintenance automation (cron-based star-count badge refresh), no spam flags, single-purpose diff.
- **PR #55 — cv.cm/v listing** — **closed**. Spam-guard flagged the identical `cv.cm/v` submission opened across 8 awesome-* lists within 14 days — self-promotional blast pattern per [contributing guidelines](CONTRIBUTING.md#-quality-gate--what-gets-in), independent of the product's own legitimacy.
- **PR #54 — AgentsCoin MCP listing** — **closed**. Spam-guard found 24 near-identical AgentsCoin PRs opened to awesome-* lists in the last 14 days (this repo included) — same blast pattern.
- **PR #52 — Hermes voice-agent listing** — **closed**. Spam-guard found 12 near-identical Hermes PRs opened to awesome-* / voice-agent lists within 14 days — same blast pattern.
- **Issue #56 — codex-profiles scope-check** — **closed**. Same "Scope check" issue text opened across dozens of other awesome-* / coding-agent lists within days — blast pattern, despite codex-profiles itself looking like a solid small tool (38 stars, active).
- All four closures used the standard courteous decline-with-reason template and left the door open for a single, unsolicited third-party nomination later if organic traction develops.

### + Added (real, web-verified developments; mirrored en/zh/ja)
- **Anthropic — [Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)** (June 30, 2026): most agentic Sonnet release yet — approaches Opus 4.8 on agentic search (BrowseComp) and computer use (OSWorld-Verified) at higher effort settings, wider cost-performance range than Sonnet 4.6; now default for Claude.ai Free/Pro, also on Max/Team/Enterprise/Claude Code/API (`claude-sonnet-5`); intro pricing $2/$10 per million input/output tokens through Aug 31, 2026 (then $3/$15).
- **Security — [JADEPUFFER (Sysdig disclosure)](https://hackread.com/sysdig-jadepuffer-first-agentic-ransomware-operation/)** (July 2, 2026): first documented ransomware operation executed end-to-end by an autonomous AI agent — Langflow RCE (CVE-2025-3248) → credential harvesting → lateral movement to production MySQL/Nacos → self-corrected failure in 31s → ephemeral-AES-key encryption of 1,342 config items, rendering the ransom unpayable-but-unrecoverable. Added to **Agent Security** (flagged as a threat writeup, not a tool) and the **2026 AI Timeline**.
- **Agent Security de-drift**: found and fixed a zh-CN/ja drift vs. English — **AgentGate, ActPlane, Microsoft Prompt Shields, Agent Name Service (ANS), OpenAI Daybreak (June 2026 entry)** existed in README.md but were missing from README.zh-CN.md and README.ja.md. Backfilled all five into both localized files in the same order as English.

### ~ Changed
- **Archived-upstream flags** added across all three languages: **[PyRIT](https://github.com/Azure/PyRIT)**, **[OpenCode](https://github.com/opencode-ai/opencode)**, **[Void](https://github.com/voideditor/void)**, **[Verba](https://github.com/weaviate/Verba)** are all now GitHub-archived; each entry marked 📦 **Archived** with tense adjusted (Verba backfilled into the zh-CN/ja RAG tables where it was previously missing).
- **2026 AI Timeline** — 2 new rows (Claude Sonnet 5 Jun 30, JADEPUFFER disclosure Jul 2) across all three files.

### ✓ Verified
- Claude Sonnet 5 pricing/positioning confirmed directly from `anthropic.com/news/claude-sonnet-5`.
- JADEPUFFER details confirmed via `hackread.com/sysdig-jadepuffer-first-agentic-ransomware-operation/` (HTTP 200, live).
- PyRIT/OpenCode/Void/Verba archived status confirmed via GitHub API (`archived: true`).
- All 4 closed PRs/issues cross-checked against GitHub search API for repeat-submission counts before closing.

## 2026-06-19 — June 2026 trend backfill into README.md (en) + en/zh/ja re-sync & broken-link fixes

### Context
- The 4 recently merged community items (**Prismix**, **Agentage Memory**, **NotFair**, **WalletPrint**) were already present and localized in **all three** READMEs — verified in place (MCP / Tool & API Integration / Agent Security / Agent Evaluation), no action needed.
- A prior run had added six June 2026 trends to **zh-CN + ja only** — they were **missing entirely from README.md (English)** and several were mis-categorized. This run brings English to parity and re-syncs categories across all three.

### + Added to README.md (English) — web-verified, mirrored to existing zh/ja entries
- **Agent Frameworks**: **[Vercel Eve](https://github.com/vercel/eve)** (June 17, 2026, Vercel Ship 2026 — filesystem-first open-source TS agent framework, Apache-2.0) and **[Databricks Omnigent](https://github.com/omnigent-ai/omnigent)** (June 13, 2026 — open-source meta-harness over Claude Code / Codex / Pi, Apache-2.0).
- **Enterprise Agent Platforms**: **[Databricks Genie One](https://www.databricks.com/blog/introducing-genie-one-genie-ontology-and-genie-agents)** (June 16, 2026, Data + AI Summit), **[ZenseAI.AgentMesh (Zensar)](https://www.prnewswire.com/news-releases/zensar-technologies-launches-zenseaiagentmesh-to-accelerate-enterprise-ai-adoption-at-scale-302805437.html)** (June 19, 2026), **[Meta Business Agent](https://about.fb.com/news/2026/06/meta-business-agent/)** (June 3, 2026 global rollout).
- **Agent Security**: **[Alchemy & Visa AgentCard](https://www.coindesk.com/business/2026/06/18/alchemy-s-ai-driven-identity-and-payment-service-gains-access-to-visa-network)** (June 18, 2026 — agent payments + identity on Visa Intelligent Commerce).

### ~ Changed / de-drift (zh-CN + ja)
- Relocated mis-categorized entries to match the corrected English placement: **Vercel Eve** moved out of *Agent-to-Agent Protocol* into *Agent Frameworks*; **Genie One / ZenseAI.AgentMesh / Meta Business Agent / Omnigent** moved out of the tail of *Agent Evaluation & Observability* into *Agent Frameworks* (Omnigent) and *Enterprise Agent Platforms* (the rest). Eval sections now correctly end at **Prismix**.
- **Fixed 4 broken links** introduced by the prior run (all returned HTTP 404): `vercel.com/blog/eve` → `github.com/vercel/eve`; `databricks.com/blog/introducing-genie-one` → the full `…-genie-ontology-and-genie-agents` URL; `pymnts.com/…alchemy-teams-with-visa…` → CoinDesk; `about.fb.com/…/meta-business-agent-whatsapp-instagram-messenger/` → the official `about.fb.com/news/2026/06/meta-business-agent/`.

### ✓ Verified
- All 6 new/updated URLs return **HTTP 200** (curl GET, browser UA). Each trend appears exactly once per category and is consistent across en / zh-CN / ja.

## 2026-06-16 — Weekly maintenance: PR triage + June 12–13 updates + Foundation Models de-drift (en/zh/ja sync)

### PR triage
- **PR #41 — dependency-freshness-mcp** — **merged by maintainer with en/zh/ja sync** (contributor edited English only). MCP server giving AI coding agents fresh, cited npm/PyPI facts (latest version, deprecations, dated breaking-change diffs); remote via Apify Standby + local stdio. Spam-guard: ✅ no red flags. Added to **Tool & API Integration** in all three languages tagged 🆕 ⚠️ **Unverified** (brand-new single-maintainer repo, created 2026-06-08, 0 stars at listing) — consistent with The Colony's handling. Closed with a credit/thank-you comment.
- **PR #42 — Seedream AI Studio** — **closed as out-of-scope / SEO-blast spam**. `seedream4.video` is a third-party wrapper site whose own footer states it is "not affiliated with, endorsed by, or sponsored by ByteDance" (the PR mis-described it as "by ByteDance"). Spam-guard flagged 100 PRs / 14 days, 60 to awesome-* lists, identical title to 37 repos, plus a parallel "LLC Class" affiliate-link blast; submitter disclosed an automated outreach workflow. Closed politely (no merge).

### + Added (real, web-verified June 2026 developments; mirrored en/zh/ja)
- **OpenAI — [GPT-Rosalind](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/)** (June 3, 2026): major update to OpenAI's life-sciences frontier model (drug discovery / genomics / quantitative biology / wet-lab; ≈31% fewer tokens than GPT-5.5 on long-horizon genomics); research preview opened worldwide, Novo Nordisk joins Amgen / Moderna / Allen Institute / Thermo Fisher.
- **Zhipu — [GLM-5.2](https://z.ai/blog/glm-5.2)** (June 13, 2026): coding-first 744B-MoE flagship, 1M-token context (~5× GLM-5.1), live across all GLM Coding Plan tiers; MIT open weights + API rolling out launch week (no benchmarks published at launch).
- **Moonshot — [Kimi K2.7 Code](https://kimi.ai/)** (June 12, 2026): coding-first successor to K2.6 — 1T MoE / 32B active, 256K context, Modified MIT, on Hugging Face + Kimi API; ~30% lower reasoning-token use, +21.8% on vendor Kimi Code Bench v2.
- **IDE — Windsurf → [Devin Desktop](https://devin.ai/blog/windsurf-is-now-devin-desktop/)** (June 2, 2026): Cognition rebranded the Windsurf IDE to Devin Desktop (windsurf.com → devin.ai); Devin Local (Rust rewrite) replaces Cascade, Agent Command Center default surface, open Agent Client Protocol; Cascade EOL July 1, 2026.

### ~ Changed
- **Anthropic — [Claude Fable 5 + Mythos 5](https://www.anthropic.com/news/fable-mythos-access)** marked **⚠️ Access suspended June 12, 2026** in all three languages: a US-government export-control directive (received 5:21pm ET) ordered Anthropic to disable both models for all customers — the first government-forced takedown of a publicly deployed frontier model.
- **Header badges** — `Last Updated` → **June 16, 2026**, `Spam_Audited` → **2026-06-16** (all three READMEs).
- **2026 AI Timeline** — 4 new rows (Fable 5/Mythos 5 launch Jun 9, the Jun 12 suspension, Kimi K2.7 Code Jun 12, GLM-5.2 Jun 13) across all three files.

### ~ Sync / de-drift (README.md was internally inconsistent vs the zh/ja canonical structure)
- **Foundation Models de-duplicated (README.md)** — collapsed two duplicate `### MiniMax` sections into one (9 entries, M3 deduped, stray "(extra)" editing marker removed), merged the two `### ByteDance` sections, merged the split `### Meta` / `### Meta (Llama)` (kept Llama 5), and relocated StepFun + Baichuan to after Samsung — matching the zh/ja order. EN now has the same **28 provider sub-sections in the same order** as zh-CN / ja.
- **zh-CN / ja backfill for parity** — added the three **GPT-Realtime-2 / Translate / Whisper** model entries to the OpenAI section and **Claude Opus 4.7** + **Claude Finance JV** to the Anthropic section (were present in EN only). Every Foundation Models provider now has matching entry counts across all three languages.

### ✓ Verified
- `python3 scripts/check_links.py` — 764 URLs; the 170 flagged are all pre-existing third-party bot-blockers / anti-scrape hosts (x.ai, microsoft.ai, llama.meta.com, perplexity, news.bms.com, tesla, servicenow, reuters, …). **No newly introduced broken links.**

## 2026-06-12 — Re-rank by strength / recency / popularity + readability polish (en/zh/ja sync)

### + Added (same day, third pass)
### + Added (June 2026 massive expansion)
- **Foundation Models**: Gemini 3.5 Pro, Gemma 4 12B, DiffusionGemma (Google); Nemotron 3.5 ASR, Nemotron 3 Ultra 550B (NVIDIA); MiniMax M3; OpenAI Sites, Codex Business Plugins.
- **Frameworks & A2A**: Nokia NSP Agentic AI, Alteryx Agent Studio, Microsoft Agent 365 / Scout.
- **Physical AI**: NVIDIA Cosmos 3.
- **Tools & RAG**: ZoomMate, Oracle OCI Enterprise Cohere Rerank 4.

- **Anthropic** — [Claude Fable 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) + [Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) (June 9, 2026): Anthropic's first publicly available Mythos-class model and its restricted-access Project Glasswing sibling, added to the top of the Anthropic section in all three languages (en/zh/ja).

### ~ Changed (no entries removed; ordering, placement, and sync fixes only)

**Category re-ranking — newest/strongest first** (verified against June 2026 coverage: the frontier race is GPT-5.5 vs Claude Opus 4.8 vs Gemini 3.5):
- **Anthropic** — [Claude Opus 4.8](https://www.anthropic.com/claude/opus) (May 28, flagship, leads SWE-bench-class coding) moved from bottom of section to **#1**, ahead of Opus 4.7.
- **Google DeepMind** — [Gemini 3.5 Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) + Gemini Omni / Omni Flash (I/O 2026) moved to top, ahead of Gemini 3.1 Pro.
- **OpenAI** — GPT-5.5 Instant (new ChatGPT default) promoted directly under the GPT-5.5 flagship trio.
- **xAI** — Grok 4.3 **GA** now leads the section ahead of the April beta entry.
- **DeepSeek** — V4-Pro / V4-Flash (the models) lead; the Agent-Harness hiring news follows.
- **IDE-Based Agents** — Cursor 3.4 / 3.3 / SDK (May 2026) moved above the older 3.09 entry.
- **Video Generation** — Runway Agent (May 13, first prompt-to-rough-cut production agent) leads the section.
- **MCP** — spec + 2026-07 RC restored to the top; the CorpusIQ community connector moved below official SDKs.

**Sync-drift repairs (zh-CN / ja, with README.md as source of truth):**
- De-duplicated **Claude Opus 4.8** (was listed twice in both zh-CN and ja Anthropic sections).
- Relocated ~18 entries that had piled up at the end of the 中国科学院/中国科学院 section (GPT-5.5 Instant, OpenAI Daybreak, Claude Finance Agents, Claude Add-ins/Dreaming, Mistral Medium 3.5, Voxtral TTS, Llama 5, MiniMax M2.5/M2.7/Hailuo 02/Music 2.6, Doubao 2.0, Seedance 2.0, Step 3.5 Flash, Baichuan-M3 Plus, Grok 4.3 GA) into their proper provider sections; added missing **StepFun** and **Baichuan** headings to zh-CN / ja to match README.md.
- Moved image-generation entries (Midjourney V8.1, Flux 2, Recraft V4, Kling IMAGE 3.0, Nano Banana 2, Sora 2 via Runway) that had drifted into the **Audio & Music** section of zh-CN / ja back into 图像生成 / 画像生成 and 视频生成 / 動画生成.
- Synced Coding Agents subsection placement: CLI tools (Codex Security, Gemini CLI, OpenCode, Grok Build, Antigravity CLI, Kimi Code CLI, MAI-Code-1-Flash) now live under **Terminal / CLI**, IDE tools (Roo Code, Void, JetBrains Rider skill) under **IDE**, Devin 2.2 under **Autonomous SWE** — consistent across all three languages.
- Added **Goose** (Block) to README.md Terminal & CLI Agents — it existed only in zh-CN / ja.

**Header badges** — `Last Updated` → **June 12, 2026**, `Spam_Audited` → **2026-06-12** (all three READMEs).

**Follow-up sync pass (same day)** — added the three May-2026 Cursor entries (3.4 Teams + PR review / 3.3 / SDK) to the zh-CN and ja IDE sections (now 642 / 639 entries); fixed a ja typo in the Kiro entry (「最大3だ 10 タスク」→「最大 10 タスク」, plus 驅動→駆動); realigned zh-CN / ja ordering in 图像生成・视频生成・音频与音乐 / 画像生成・動画生成・音声・音楽 to match README.md.

---

## 2026-05-30 — Weekly refresh: May 25–30 · Claude Opus 4.8 / Koog 1.0 / Gemini Omni Flash rollout / MCP 2026-07 RC

### + Added (5 new entries across 4 sections, mirrored to zh-CN / ja)

**Foundation Models — Anthropic** —
- [Claude Opus 4.8](https://www.anthropic.com/claude/opus) (May 28, 2026) — codebase-scale migrations, **dynamic workflows** research preview that fans out hundreds of parallel sub-agents in one session, a manual **effort-control** panel, and **3× cheaper Fast mode** at the same $5 / $25 per million in/out. Live on Anthropic native + Amazon Bedrock + AWS Claude Platform + Google Cloud + Microsoft Foundry. Teases a forthcoming **Mythos-class** model line for limited orgs.

**Foundation Models — Google DeepMind** —
- [Gemini Omni Flash consumer rollout](https://www.techtimes.com/articles/317309/20260528/google-gemini-omni-flash-brings-voice-controlled-ai-video-editing-future-conversational-ai.htm) (May 28, 2026) — Omni Flash starts shipping to consumers in the Gemini app, **Google Flow**, and **YouTube Shorts** as the editing engine; conversational cinematic zooms / background swaps / weather edits driven by text + voice + image + audio prompts. Replaces traditional NLEs for short-form video.

**Agent Protocols & Standards** —
- [MCP 2026-07 Release Candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) (May 2026, final July 28, 2026) — next major MCP spec revision: **stateless protocol core**, **extensions framework**, **MCP Apps** (server-rendered UI), Tasks graduated to an extension, hardened authorization aligned with OAuth / OpenID Connect.

**Agent Frameworks** —
- [Koog 1.0](https://github.com/JetBrains/koog) (May 28, 2026, KotlinConf 2026) — JetBrains' open-source **Kotlin + Java** agent framework hits stable 1.0 with a 1-year API stability guarantee. Kotlin Multiplatform deployment (JVM / Android / iOS / JS / WASM), Java interop without wrapper modules, local Android LiteRT, OpenTelemetry across all targets, graph workflows, Spring Boot / Ktor integration, OpenAI / Anthropic / Google / Bedrock providers. Apache-2.0.

**Enterprise Agent Platforms** —
- [Sistava](https://sistava.com) (merged from community PR #24) — AI agent orchestration platform for deploying multi-channel sales / marketing / finance / support agents reachable via Slack, WhatsApp, email, voice, Telegram, API, MCP, A2A, webhooks, plus on-host computer use.

### ~ Changed

- **Header badges** — `Last Updated` → `May 30, 2026`, `Spam_Audited` → `2026-05-30`, `Resources` 435+ → **440+** (all three READMEs; zh-CN / ja now also carry the Resources badge).
- **2026 AI Timeline** — 5 new May 28–29 rows added across `README.md` / `README.zh-CN.md` / `README.ja.md`.

### ✕ Not added / held for revision (anti-spam holds)

- **PR #25 — CorpusIQ MCP** — marketing registry link returned **HTTP 404** at audit time, and the submission had no public artefact (no GitHub repo, no MCP Registry listing) beyond the corpusiq.io domain. Held with reviewer comment asking for a primary source.
- **PR #26 — AgentGate** — the patch inserts the same entry twice in the Agent Security section, mixes bullet styles (`*   [...]` vs `- [...]`), and drops a bare marketing URL on its own line. Underlying project (6 stars at audit; created 2026-05-08; submitter disclosed parallel submissions to 15+ awesome lists) would land with ⚠️ **Unverified**. Held pending a clean single-bullet patch.
- **PR #27 — GreenOps Agent** — repository created 2026-05-26 (4 days old at submission) with 0 stars, branch name `greenops-zijian` shows the submission is tailored to this list rather than reflecting external adoption, patch uses a doubled bullet prefix (`- - [...]`), and the quality-checklist line for third-party adoption is checked without linked evidence. Held with reviewer comment asking for primary sources.
- **"PilotDeck" (OpenBMB)** — covered by a single Medium write-up and the upstream GitHub README; needs an independent primary source describing scope and a clear license before listing.
- **"MiniMax M3"** — only a teaser as of late May 2026; no public weights, no API, no model card. Will revisit on launch (second half of 2026 per MiniMax).
- **"ChatGPT-5.5" / "Claude 4.8" lifestyle-blog round-ups** — secondary, non-authoritative listicles; relying on first-party announcements (covered above) instead.

---

## 2026-05-25 — Weekly refresh: May 18–24 expansion + full zh-CN / ja sync

### + Added (15 new entries across 7 sections)

**Coding Agents** —
- [Grok Build](https://x.ai/news/grok-build-cli) (May 14, xAI) — agentic CLI on `grok-code-fast-1`, parallel sub-agents in isolated envs, SuperGrok Heavy gating.
- [Antigravity CLI](https://antigravity.google/blog/introducing-google-antigravity-2-0) + [Google Antigravity 2.0](https://antigravity.google/blog/introducing-google-antigravity-2-0) (May 19, Google I/O 2026) — standalone multi-agent desktop app + CLI + SDK; macOS / Linux / Windows; ecosystem integrations with AI Studio / Android / Firebase; enterprise edition inside Gemini Enterprise Agent Platform.
- [JetBrains Rider AI test-writing skill](https://blog.jetbrains.com/dotnet/2026/05/22/claude-codex-ai-agent-skill-for-writing-tests/) (May 22) — .NET coverage data exposed to Claude Code / Codex for targeted test generation.

**Tool & API Integration (MCP servers)** —
- [AWS MCP Server](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/) (GA May 6) — AWS-managed MCP endpoint with sandboxed Python + agent skills.
- [Google Workspace MCP Server](https://workspaceupdates.googleblog.com/2026/05/agent-tools-and-security-updates-for-workspace-developers.html) (May 1 rollout) — Workspace-native MCP for Gmail / Drive / Calendar / Docs / Sheets.
- [iManage MCP Server](https://imanage.com/resources/resource-center/news/mcp-server-available-broader-ai-ecosystem/) (May 14) — first major legal/PS SaaS with a public MCP endpoint.
- [Power Platform Canvas Authoring MCP Server](https://www.microsoft.com/en-us/power-platform/blog/2026/05/14/whats-new-in-power-platform-may-2026-feature-update/) (May 14) — natural-language InfoPath → Canvas Apps migration via Copilot / Claude Code.

**Agent Security** —
- [RAMPART](https://github.com/microsoft/RAMPART) (May 20, Microsoft) — pytest-native white-box safety/security testing framework for agentic AI. CI/CD-friendly developer counterpart to PyRIT. MIT.
- [Clarity](https://www.microsoft.com/en-us/security/blog/2026/05/20/introducing-rampart-and-clarity-open-source-tools-to-bring-safety-into-agent-development-workflow/) (May 20, Microsoft) — structured design-review tool for AI agents; "living artifacts" before code.

**Personal AI Agents** —
- [QwenPaw](https://github.com/agentscope-ai/QwenPaw) (May 2026 rebrand from CoPaw) 🇨🇳 — self-hostable personal assistant in the Qwen / AgentScope family; local-first memory, multi-agent collaboration, multi-channel.

**Enterprise Agent Platforms** —
- [Kore.ai Artemis Agent Platform](https://venturebeat.com/technology/kore-ai-launches-artemis-ai-agent-platform-expands-challenge-to-microsoft-and-salesforce) (May 22) — AI-native enterprise platform launched on Azure with the new **Agent Blueprint Language (ABL)**.
- [FPT Flezi Foundry™](https://lasvegassun.com/news/2026/may/22/fpt-launches-flezi-foundry-advancing-ai-augmented-/) (May 22) — AI-augmented delivery platform with ADLC + AMS modes under Service-as-a-Software governance.

**Notable Agent Projects of 2026** —
- Combined story: Google Antigravity 2.0 + Microsoft RAMPART + xAI Grok Build — three structural agent-stack shifts in one 8-day window (May 14–22).

### ~ Changed

- **Header badges** — `Last Updated` → `May 25, 2026`, `Spam_Audited` → `2026-05-25`, `Resources` 420+ → **435+** (all three READMEs).
- **Quick Navigation counts** — Tool & API 15+ → **18+**, Agent Security 14+ → **16+**, Coding Agents 24+ → **27+**, Personal AI 10+ → **11+**, Enterprise Platforms 16+ → **18+**.
- **2026 AI Timeline** — 10 new May 1–22 rows across `README.md` / `README.zh-CN.md` / `README.ja.md`.
- **zh-CN / ja full sync** — 44 EN entries previously missing in zh-CN and 47 missing in ja are now backfilled, mirroring the EN section order and entry set. All new May 18–24 entries also mirrored in zh-CN and ja with locale-appropriate phrasing (not literal MT).

### ✕ Not added (explicit anti-spam holds)

- **Fetch.ai "Agent Launch on BNB Chain"** — token-economy crypto-AI surface; out of scope (we don't curate crypto-tokenisation infrastructure).
- **Splunk MCP Server v1.1.3** — routine point release of an already-listed category; no structural change.
- **mabl local MCP server deprecation** — deprecation, not a new tool.

---

## 2026-05-20 — Mega expansion: Scenario Guide + 20 Compare tables + Start Here

### + Added
- 🗺️ **Scenario Guide** — 50+ curated scenario-to-tool mappings across 5 categories (Building / Model Selection / Infrastructure / Eval / Ecosystem)
- 🧩 **Stack Recipes** — 8 curated multi-tool combinations for common use cases
- ⚠️ **Anti-Picks** — 15 “what not to use for” recommendations based on 2026 production reality
- 🚀 **Start Here** guide for new readers (EN + zh-CN + ja)
- 📊 **20 new Compare tables**: Foundation Models API / Foundation Models Local / Agent Memory / Voice & Audio / Image Gen / Video Gen / RAG Frameworks / Vector DBs / Personal AI Assistants / MCP Servers / Enterprise Platforms / Embeddings / Security Tools / Computer Use / Physical AI / Chinese AI / TypeScript Frameworks / Meta-Comparison / Mobile AI / Anti-Picks
- 🏷️ **6 new Status badges**: 🔥 Hot / ⚡ Updated / 🧪 Experimental / 💰 Freemium / 🔐 Audited / 🇨🇳 China-first
- zh-CN / ja parity for all additions (localized, not machine-translated)

### ~ Changed
- Resources badge: 380+ → 420+
- Footer resource count updated to 420+

---

## 2026-05-20 — Weekly refresh: May 16–20 expansion (Google I/O 2026 + Alibaba Hangzhou) + zh-CN / ja sync

### + Added (≈21 new entries across 7 sections)

**Foundation Models** (this week's centre of gravity):
- **Google I/O 2026** — [Gemini 3.5 Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) GA as default Gemini app + Search AI Mode model (~4× faster, beats 3.1 Pro on key benchmarks); [Gemini Omni / Omni Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) world-model line toward AGI; [Gemini Spark](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) 24/7 personal agent with ~30+ MCP tool integrations; new [Google AI Ultra](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) $100/mo tier.
- **Alibaba Cloud Summit Hangzhou (May 20)** — [Qwen 3.7-Max](https://www.scmp.com/tech/big-tech/article/3354212/alibaba-unveils-new-qwen-model-custom-chips-bid-become-chinas-ai-factory) GA, agentic-coding flagship designed for long-horizon multi-step missions; T-Head **Zhenwu M890** AI accelerator; full-stack AI infra upgrade; preview ladder [Qwen 3.7-Max-Preview / Plus-Preview](https://www.scmp.com/tech/tech-trends/article/3354087/alibaba-teases-new-qwen-previews-highest-ranking-chinese-ai-models-arena) (May 18, top Chinese model on LM Arena text+vision).
- **OpenAI** — [OpenAI ↔ Dell Codex](https://openai.com/news/company-announcements/) (May 18, on-prem Codex distribution); [ChatGPT safety upgrade](https://www.edtechinnovationhub.com/news/openai-updates-chatgpt-safety-systems-to-track-risk-across-sensitive-conversations) (May 18, cross-session risk tracking); [OpenAI Guaranteed Capacity / Compute Annual Pass](https://openai.com/news/company-announcements/) (May 19, 1/2/3-year compute reservations); [OpenAI ↔ Google SynthID + C2PA content provenance](https://openai.com/index/advancing-content-provenance/) (May 19).
- **Anthropic** — [Bristol Myers Squibb ↔ Claude Enterprise](https://news.bms.com/news/corporate-financial/2026/Bristol-Myers-Squibb-Announces-Strategic-Agreement-with-Anthropic-to-Position-Claude-Enterprise-as-the-Shared-Intelligence-Platform-Across-Its-Global-Operations/default.aspx) (May 20, top-5 pharma); [Anthropic briefs FSB on Claude Mythos](https://www.theguardian.com/technology/2026/may/18/anthropic-ai-claude-mythos-cyber-financial-stability-board-fsb) (May 18); [Code with Claude 2026 sessions on YouTube](https://www.infoq.com/news/2026/05/code-with-claude/) (May 18); [Widening the conversation on frontier AI](https://www.anthropic.com/news/widening-conversation-ai) (May 19).
- **DeepSeek** — [Agent Harness team](https://www.scmp.com/tech/big-tech/article/3354113/deepseek-recruits-former-jane-street-engineer-catch-ai-agents-revenue-race) (May 19, Jane Street hire, signal of DeepSeek pivoting to autonomous-agent productisation).

**Physical AI** —
- [Figure F.03 vs human 8h package-sort challenge](https://incrypted.com/en/figure-ai-held-a-human-vs-robot-marathon/) (May 18, human 12,924 vs robot 12,732, narrowest published gap to date).
- [Boston Dynamics Atlas 100-lb manipulation + Hyundai 25K plan](https://www.techtimes.com/articles/316854/20260519/boston-dynamics-reveals-how-atlas-learned-lift-100-pound-loads-hyundai-plans-30000-per-year.htm) (May 18-19).
- [Unitree G1 at JAL Haneda](https://www.techtimes.com/articles/316862/20260519/jal-deploys-unitree-g1-robots-haneda-us-congress-moves-blacklist-supplier-national-security.htm) (first commercial-airline humanoid trial; US Congress moves to entity-list Unitree same week).

**Frameworks** —
- [LlamaIndex ↔ Google Agents API integration](https://www.kucoin.com/news/flash/google-launches-agents-api-llama-index-integrates-llamaparse-for-unstructured-document-processing) (May 20) — LlamaParse / LiteParse + Sandboxed-Lit runtime + ParseBench (first OCR benchmark for agents).

**Multimodal / Video** —
- [Runway Agent](https://chatlyai.app/news/runway-agent-launch-may-2026) (May 13, end-to-end "brief-to-finished-video" agent on Gen-4 / Aleph). Backfilled — missed in the May 16 cut.

**Enterprise Platforms** —
- OpenAI Guaranteed Capacity duplicated under Enterprise as a structural reply to Anthropic Priority Tier.
- Bristol Myers Squibb Claude Enterprise rollout duplicated as the year's most concrete pharma agent commitment.

**Notable Projects of 2026** — added Google I/O 2026 keynote, Alibaba Hangzhou summit, and OpenAI Guaranteed Capacity launches as the three biggest May 16–20 turning points.

### ~ Changed

- **Header badges** — `Last Updated` → `May 20, 2026`, `Spam_Audited` → `2026-05-20`, `Resources` 360+ → **380+** across all three READMEs.
- **Quick Navigation counts** — Foundation Models 75+ → **80+** (I/O 2026 + Alibaba Hangzhou), Physical AI 19+ → **22+**, Enterprise Platforms 14+ → **16+**.
- **2026 AI Timeline** — 16 new May 17–20 rows (plus a backfilled May 13 Runway Agent row) across `README.md` / `README.zh-CN.md` / `README.ja.md`; the placeholder "I/O 2026 starts" stub replaced with concrete announcements.
- **zh-CN / ja parity** — every new English entry mirrored with locale-appropriate phrasing (not literal translation).

### ✕ Not added (explicit anti-spam holds)

- **Computex 2026 NVIDIA keynote** — scheduled June 1, 2026 (Taiwan time); too early.
- **AMD Advancing AI 2026** — scheduled July 22-23, 2026; too early.
- **Microsoft Build 2026** — scheduled June 2-3, 2026; only May rollouts of Copilot Studio governance already captured under existing entries.
- **Tesla Optimus Fremont conversion** — covered as a Q3 production-line reshuffle inside the existing Optimus Gen 3 entry; no public May 17-20 product announcement of its own.
- **Unitree mecha GD01** — already added in the previous refresh (May 12 announcement).
- **Sakana / Zyphra weekly updates** — no new ship beyond the May 14 Diffusion-Preview entry.

---

## 2026-05-16 — Weekly refresh: May 11–16 expansion + zh-CN / ja sync

### + Added (≈24 new entries across 6 sections)

**Foundation Models** —
- [OpenAI Deployment Company / DeployCo](https://openai.com/index/openai-launches-the-deployment-company/) (May 11, $4B+ enterprise services unit + Tomoro acquisition).
- [Codex on Mobile](https://9to5mac.com/2026/05/14/openai-brings-codex-control-to-chatgpt-for-iphone-and-android/) (May 14, ChatGPT iOS/Android remote-control for the macOS Codex app; preview to Free / Plus / Go).
- [OpenAI ↔ Malta ChatGPT Plus partnership](https://openai.com/index/malta-chatgpt-plus-partnership/) (May 16, first country-wide deal under "OpenAI for Countries").
- [Anthropic ↔ SpaceX Colossus 1](https://www.siliconrepublic.com/business/anthropic-joins-forces-with-spacex-for-colossus-capacity) (May 6, 300+ MW / 220K GPU inference capacity, doubles Claude Code rate limits).
- [Claude for Legal](https://www.anthropic.com/news/claude-for-legal) (May 12, 20+ MCP connectors + 12 practice-area plugins; iManage, NetDocuments, DocuSign, LexisNexis, Westlaw, Harvey, Everlaw, Relativity, CourtListener…).
- [Claude for Small Business](https://www.anthropic.com/news/claude-for-small-business) (May 13, 15 pre-built workflows + connectors for QuickBooks / PayPal / HubSpot / Canva / DocuSign / Google Workspace / Microsoft 365 + 10-city US workshop tour).
- [Anthropic ↔ Gates Foundation $200M partnership](https://www.anthropic.com/news/gates-foundation-partnership) (May 14, global health + life sciences + education + agriculture).
- [Anthropic ↔ PwC strategic alliance expansion](https://www.pwc.com/us/en/about-us/newsroom/press-releases/anthropic-pwc-expand-alliance-agentic-enterprise.html) (May 14, global Claude Code + Cowork rollout, 30,000 PwC professionals certified).
- [Gemini 3.1 Flash-Lite GA](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-lite-is-now-generally-available) (May 8).
- New **Sakana AI** subsection — [Sakana RL Conductor](https://venturebeat.com/orchestration/how-sakana-trained-a-7b-model-to-orchestrate-gpt-5-claude-sonnet-4-and-gemini-2-5-pro) (paper Apr 27) + [Sakana Fugu](https://sakana.ai/fugu-beta/) (beta Apr 24-25).
- New **Zyphra** subsection — [ZAYA1-8B](https://www.zyphra.com/post/zaya1-8b) (May 6) + [ZAYA1-8B-Diffusion-Preview](https://www.zyphra.com/post/zaya1-8b-diffusion-preview) (May 14, first AR-to-MoE-diffusion conversion, 7.7× speedup on AMD).

**Agent Frameworks** — [Genkit Middleware](https://developers.googleblog.com/announcing-genkit-middleware-intercept-extend-and-harden-your-agentic-apps/) (May 14, Google's open-source agent middleware system).

**Coding Agents** — [Cursor 3.4 Cloud Agent Environments](https://cursor.com/changelog) (May 13, multi-repo, Dockerfile build secrets, 70% faster cached layers, audit logs); [Visual Studio 2026 Agent Mode + Skills](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/) (May 12-15 Insiders).

**Computer Use** — [ChatGPT Workspace Agents](https://venturebeat.com/orchestration/openai-unveils-workspace-agents-a-successor-to-custom-gpts-for-enterprises-that-can-plug-directly-into-slack-salesforce-and-more) (research preview Apr 22, credit pricing May 6, EKM support May 7).

**Enterprise Platforms** — [SAP Business AI Platform + Joule Studio 2.0 + Autonomous Suite](https://news.sap.com/2026/05/sap-sapphire-sap-unveils-autonomous-enterprise/) (SAP Sapphire 2026 May 11-13, GA from June 2026); [Microsoft Agent 365 + Microsoft 365 E7](https://techcommunity.microsoft.com/blog/agent-365-blog/microsoft-365-e7--agent365-from-where-you-are-to-enterprise-ai-at-scale/4519969) (May 1 GA + May updates).

**Physical AI** — [Figure Helix 02 package-sort 72h continuous run](https://www.businessinsider.com/figure-ai-turned-a-humanoid-sorting-packages-must-see-tv-2026-5) (May 13-16, ~88K packages over ~72h on the F.03 fleet).

**Notable Projects of 2026** — added OpenAI DeployCo, Anthropic ↔ SpaceX Colossus 1, DeepSeek $4B state-backed round, and the Vatican AI Commission announcement.

### ~ Changed

- **Header badges** — `Last Updated` and `Spam_Audited` bumped to `May 16, 2026` / `2026-05-16` across all three READMEs; `Resources` badge bumped 340+ → 360+.
- **Quick Navigation counts** — Foundation Models 65+ → 75+ (Sakana / Zyphra subsections + new Anthropic / OpenAI entries), Frameworks 22+ → 23+, Coding Agents 22+ → 24+, Physical AI 18+ → 19+, Computer Use 9+ → 10+, Enterprise 12+ → 14+.
- **2026 AI Timeline** — added 13 new May 11–16 rows across README.md / README.zh-CN.md / README.ja.md: SAP Sapphire 2026, Claude for Legal, Claude for Small Business, Cursor 3.4 environments, VS 2026 Agent Skills, Figure Helix 02 72h run, Anthropic ↔ Gates, Anthropic ↔ PwC, Genkit Middleware, Zyphra Diffusion, Pope Leo XIV's Vatican AI commission, OpenAI ↔ Malta, DeepSeek $4B raise.
- **zh-CN / ja parity** — mirrored every new English entry with locale-appropriate phrasing (not literal translation).

### ✕ Not added (explicit anti-spam holds)

- **Sakana "RL Conductor / Trinity" research paper** — listed as a model entry under the new Sakana AI section because the productised Fugu beta is in market; the underlying Conductor + Trinity research lives in the same entry rather than a separate "research only" bullet to avoid duplication.
- **Microsoft MDASH security harness** — acknowledged in the timeline (May 13) only inside the existing Microsoft Agent 365 row; not promoted to its own Security entry until a public artifact (paper / SDK) ships.
- **"OpenAI Daybreak EU expansion"** — covered by the existing May 12 Daybreak entry; no new bullet because the May 14-16 movement is incremental rollout, not a new product.

---

## 2026-05-15 — PR triage + May 11–14 expansion across 8 sections

### + Added

- **Agent Frameworks** — [Bernstein](https://github.com/sipyourdrink-ltd/bernstein) (PR #18, 358 stars, Apache-2.0, deterministic CLI agent orchestrator with HMAC-chained audit, git worktree isolation; flagged for parallel blast across 8 awesome lists 2026-05-14 but passes quality gate).
- **Voice & Multimodal Agents** — [OpenYabby](https://github.com/OpenYabby/OpenYabby) (issue #10, 29 stars, MIT, macOS voice-driven multi-agent orchestrator on the Realtime API; third-party nomination by idovmamane).

**Foundation Models** — OpenAI Daybreak (May 12 cyber-defense platform), Grok 4.3 GA on Foundry/OCI, Claude Code with Claude 2026 (Add-ins/Dreaming/Outcomes/multi-agent orchestration).

**Coding Agents** — Cursor SDK (May 4, TypeScript SDK + v2.5 security patch), Cursor 3.4 (May 11–13, Teams + parallel agents + Vulnerability Scanner + `/multitask`), Claude Code May 2026 update line (v2.1.128–2.1.141, `/goal`, agent view, plugin .zip/URL loading, Ctrl+R global history search), Codex CLI May 2026 update (Chrome extension, `codex remote-control`, **Codex on Mobile preview May 14**).

**Agent Frameworks** — LangGraph v1.2 May 2026 changelog (`DeltaChannel`, per-node timeouts, content-block streaming v3); Microsoft Agent 365 GA May 1.

**Agent Memory** — Mem0 April 2026 algorithm upgrade (single-pass add-only extraction, entity linking, multi-signal retrieval; 55K+ stars, 21+ integrations).

**Agent Evaluation & Observability** — Langfuse acquired by ClickHouse Jan 2026 + observations-centric data model + Cloud Japan + LLM-as-a-Judge API.

**Voice & Multimodal Agents** — Vapi $50M Series B + 1B platform calls (May 12) + Squads v2 / Composer / Simulations / Soniox transcriber.

**Physical AI / Embodied** — Figure 04 design finalized (May 13), Unitree GD01 (May 2026 manned mecha, ~$650K).

**Personal AI Agents** — Gemini Intelligence (May 12 Android Show: I/O Edition), Gemini Spark (May 14 pre-I/O insight).

### ~ Changed

- **OpenClaw** — refreshed from v2026.4.21 → v2026.5.12.
- **Mem0 / Langfuse / Vapi / LangGraph / Codex / Cursor / Claude Code** — updated existing entries to reflect May 2026 release lines instead of stale April-only snapshots.
- **2026 AI Timeline** — added 13 new May 1–19 rows covering the above plus Google I/O 2026 kickoff.

### ~ Changed

- **OpenClaw** — description refreshed from v2026.4.21 to **v2026.5.12** (May 14, 2026): native model identity injection, isolated Telegram polling worker, MEMORY.md auto-compaction, protected config paths for owner/exec approvals.
- **2026 AI Timeline** — added 2026-05-14 OpenClaw v2026.5.12 release entry under Tools.

### ✕ Closed without merge / list (PR & issue triage)

- **PR #19** MisarBlog — closed. Quality-gate fail: 0 GitHub stars on `mrgulshanyadav/misarblog-mcp`, single maintainer of an unknown project (sole-maintainer rule), proposed entry used a table format inconsistent with the surrounding bullet-list section. Same author has filed parallel submissions across 5+ awesome lists in the past two months (`punkpeye/awesome-mcp-servers`, `jaw9c/awesome-remote-mcp-servers`, `e2b-dev/awesome-ai-agents`, `caramaschiHG/awesome-ai-agents-2026`, etc.). Welcome to re-submit once third-party adoption is verifiable.
- **Issue #16** Nobulex (Trust Capital) — closed as duplicate. Already listed in Agent Security at line #506 with the `⚠️ Unverified` caveat covering the Microsoft AGT merge + npm download discrepancy + 15+ awesome-list blast. No new evidence in this issue.
- **Issue #20** Nobulex (Security & Governance) — closed as duplicate of #16; same submitter / project / claim already audited.

---

## 2026-05-10 — Weekly refresh, PR audit & global model expansion

### + Added (model & tool expansion across 8 sections)

**Foundation Models** — added GPT-5.5 Instant, GPT-Realtime-2 / Translate / Whisper, Claude Finance Agents, Claude Finance JV, Mistral Medium 3.5, Voxtral TTS, MiniMax M2.7 / M2.5 / Hailuo 02 / Music 2.6, Doubao 2.0, Seedance 2.0, StepFun Step 3.5 Flash, Baichuan-M3 Plus. New **Meta (Llama)** subsection with Llama 5, Meta Muse Spark.

**Image Generation** — Midjourney V8.1, Flux 2 family (Pro/Flex/Dev/Klein), Recraft V4, Nano Banana 2, Kling IMAGE 3.0; reorganised existing entries.

**Video Generation** — Veo 3.1 + Veo 4 hint, Kling VIDEO 3.0 (Feb 2026), Sora 2 via Runway, Seedance 2.0, Hailuo 02. Sora marked 📦 Discontinued.

**Audio & Music** — ElevenLabs v3 + ElevenAgents, Eleven Music + Scribe v2, Cartesia Sonic 3 / Line Agents, Deepgram Nova-3 + Aura-2 + Flux Multilingual, MiniMax Music 2.6, Voxtral TTS.

**Agent Frameworks** — Mastra (TypeScript), VoltAgent (TypeScript).

**Agent Memory** — Mem0g (graph), Graphiti, LangMem (LangGraph 0.3.19 spinout), Claude Managed Agents Memory.

**RAG & Knowledge** — Morphik (multimodal RAG), Cognee (knowledge-graph + memory).

**Coding Agents** — Codex Security, Codex Chrome extension note, Roo Code, Void (open-source Cursor alt), Cursor 3.3, Devin 2.2 with pricing.

**Physical AI / Humanoids** — Tesla Optimus V3 with mass-production specs, Figure 03 + Helix AI, Figure 02 + Helix 02, Unitree G1 + H1-2 + R1 Air + Gen 2 lifelike skin.

**Voice & Multimodal Agents** — ElevenAgents, Cartesia Line, Deepgram Voice Agent API, OpenAI Realtime API (GPT-Realtime-2).

**Benchmarks** — Terminal-Bench 2.0, GDPval / GDPval-MM, SWE-bench Pro, Hieroglyphic Benchmark (Gemini 3.5 leaks), LLM-Stats Live Leaderboard.

**Net change**: 459 → **516 entries (+57)**, 25 categories unchanged. zh-CN / ja will catch up in a separate i18n pass; Timeline and badge fields are already synced across all three.

## 2026-05-10 — Weekly refresh & PR audit

### — Closed (anti-spam policy)

Three open PRs were reviewed against the anti-spam contributor guidelines and **closed without merge**:

- **#13** *Add AI for Database* by `dann26parr69` — fork named `awesome-ai-agents-2027`; submitter account 2026-02-old, 0 followers, **20+ identical PRs across awesome-lists in 3 weeks** with multiple closures upstream; tool is a closed-source marketing site (no public repo).
- **#14** *feat: add P2PCLAW* by `Agnuxo1` — self-promotion; project description recycles previously-flagged BenchClaw, false claim of being "part of the OpenClaw family" (no relation to the listed [openclaw/openclaw](https://github.com/openclaw/openclaw)), benchmark numbers ("43× faster than PyTorch", "88.7% memory reduction") not independently reproduced.
- **#15** *Add Awesome AI Startups* by `ununununium` — fork named `awesome-ai-agents-2027`; submitter blast-PRed **20+ awesome lists in <1 hour** for `NotFair` MCP server. The proposed list itself (`nowork-studio/awesome-ai-startups`, CC0, 88 entries) is legitimate, but accepting parallel-blast PRs rewards spam behaviour. Closed per repository policy; the list may be added later by a non-spam contributor.

### + Added (timeline events for 2026-05-04 → 2026-05-09)

- **2026-05-04** — Google retires Project Mariner; tech folded into Gemini Agent.
- **2026-05-04** — Anthropic + Goldman Sachs + Blackstone announce $1.5B Claude deployment JV.
- **2026-05-05** — OpenAI rolls out **GPT-5.5 Instant** as the new default ChatGPT model.
- **2026-05-05** — Anthropic launches **Claude Finance Agents** (10 specialised agents).
- **2026-05-05** — OpenAI ↔ PwC partnership for financial-services agents.
- **2026-05-07** — Google preparing **Agent Mode for Flow** (Veo-based AI filmmaking).
- **2026-05-08** — OpenAI launches **GPT-Realtime-2 / Realtime-Translate / Realtime-Whisper**.
- **2026-05-09** — OpenAI rolls out **Workspace Agents** in ChatGPT Enterprise.

### ~ Changed

- **Google Project Mariner** moved from 🆕 New → 📦 Discontinued (2026-05-04). Browser-agent capabilities now live in Gemini Agent.
- Last-Updated and Spam-Audited badges bumped to **2026-05-10**.
- Same edits applied to all three READMEs (English, 中文, 日本語).

---

## 2026-05-05 — Spam audit & expansion pass

### + Added (new sections)

- 🧪 **Agent Sandboxing & Compute Isolation** — E2B, Daytona, Modal, Microsandbox, SandboxFusion, Northflank, Firecracker
- 🛠️ **Agent IDEs & Visual Builders** — LangGraph Studio, Dify, Agenta, Vellum, Cozeloop, Restack, Bisheng, n8n
- 🎮 **Agent Simulation & World Models** — Generative Agents, Voyager, SWE-Gym, WebArena, WorkArena, Genie 3/4, NVIDIA Cosmos
- 🌐 **Browser & Web Agents** — Browser Use, Stagehand, Steel Browser, Skyvern, AgentQL, Hyperbrowser MCP, Playwright MCP, MultiOn, Browserbase
- 📱 **Mobile Agents** — Mobile-Agent, AppAgent, Apple Intelligence, Galaxy AI, Gemini for Android, Microsoft Magma
- 🇨🇳 **Chinese AI Ecosystem** — Dify, Lobe Chat, Cozeloop, AgentScope, Bisheng, MetaGPT, FastGPT, QAnything, RAGFlow, LightRAG, AppFlowy, Manus, Coze, Tongyi, Doubao, Kilo Code, Cherry Studio, ScienceOne 100
- 📝 **Compare — Side-by-Side Tables** for Frameworks, Sandboxes, Browser stacks, Eval & Observability, and Coding Agents

### + Added (within existing sections)

- Agent Security: AgentDojo, ModelScan, PyRIT
- Evaluation & Observability: DeepEval, Agenta, LangSmith SDK, AutoEvals
- Learning Resources: Hugging Face Agents Course, Anthropic Cookbook, Google Gemini Cookbook, Maxime Labonne LLM course, Anthropic Courses

### ~ Changed

- Added a **🏷️ Status Legend** (🆕 / 📦 Archived / 💤 Stale / ⚠️ Unverified / 🇨🇳 Chinese ecosystem) directly below the badges.
- Marked **4 archived projects** so readers know they are kept for historical reference only:
  - `gpt-engineer-org/gpt-engineer` (archived 2025-05)
  - `reworkd/AgentGPT` (archived 2025-04)
  - `vanna-ai/vanna` (archived 2026-02)
  - `protectai/rebuff` (archived 2024-08)
- Marked **10 stale projects** (no commits in 6+ months): Vigil, Bark, GPQA, 01 Light, Vocode, SuperAGI, e2b-dev/awesome-ai-agents, Motorhead, Flux, Devika.
- Marked **3 unverified entries** that were merged via parallel-blast PRs across many awesome lists. They are kept (not removed) so readers can see the projects, but with explicit caveats:
  - `The Colony` — submitted to 15+ awesome lists; org and SDK repos <30 days old, 0–2 stars each.
  - `BenchClaw` — submitted to 8 awesome lists, **rejected by 7**; single-maintainer with 2 stars.
  - `PromptEden` — submitted to 10 awesome lists on the same day; commercial SaaS with no independent traction yet.
- Replaced generic `www.sz.gov.cn/` link for Shenzhen Humanoid Pilot Line with a verified news source.
- Updated Quick Navigation table to 25 categories and refreshed Contents list.

### — Closed

- PR #4 (`Add Web Agent Bridge (WAB)`) — closed as *not merged*. Description claimed `@wab/mcp-server` on npm (404), "180+ commits" (actual ~30), and the same PR was already rejected by `kyrolabs/awesome-agents`.

---

## 2026-05-04 — PR #5 merged

- `+ PromptEden` (Agent Evaluation & Observability)
- `~ feat(update)` weekly refresh

## 2026-04-30 — PR #3 merged

- `+ BenchClaw` (Agent Evaluation & Observability) — flagged as ⚠️ Unverified on 2026-05-05.

## 2026-04-29 — PR #2 merged

- `+ The Colony` (Tool & API Integration) — flagged as ⚠️ Unverified on 2026-05-05.
- Latest models update for April 29, 2026.

## 2026-04-27

- `+ The Colony` first added (later replaced by PR #2).

## 2026-04-24

- ~ Latest model refresh (GPT-5.5, Muse Spark, DeepSeek V4-Pro, Qwen3.6) + link audit.
- `+ Octomind` (Agent Frameworks).
- ~ Monthly refresh with new categories.

## 2026-04-07

- ~ Comprehensive LLM coverage — added all major models from 20+ providers.
- ~ Major content expansion — 2026 AI models, protocols, multimodal AI, 100+ new resources.

## 2026-03-24

- 🎉 Initial release.

---

## How to read this file

- **+ Added** — new entry / new section.
- **— Removed** — entry removed from the list (with reason).
- **~ Changed** — material wording, tagging, or link change.
- **Closed** — pull requests rejected (kept here for transparency).

Status tag changes (from no-tag → 📦 / 💤 / ⚠️) are documented under "Changed" so readers can see when caveats were added.

## 2026-05-05 (Part 2) — Full Chinese + Japanese parity

### + Added

- `README.zh-CN.md` (中文版) — full parallel translation, 906 lines, 451
  entries across all 25 sections + 5 comparison tables + complete 2026
  timeline. No more "see English version" stubs.
- `README.ja.md` (日本語版) — full Japanese parallel translation, 909
  lines, same parity. Native technical Japanese with proper katakana
  conventions.
- Language-switch badges in all three READMEs cross-link to each other.
- Updated CONTRIBUTING reference to mention all three language versions
  share the same anti-spam quality gate.

### Translation policy

- All status tags (🆕 / 📦 / 💤 / ⚠️ / 🇨🇳) preserved verbatim across
  languages.
- All URLs identical; only entry descriptions translated.
- Minor differences allowed for natural reading (e.g., the Quick Nav
  table header is split differently in EN to fit the badge row).
- English README remains the source of truth — divergence is resolved
  in EN's favour.
