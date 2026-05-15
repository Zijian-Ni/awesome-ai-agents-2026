# Changelog

All notable changes to **Awesome AI Agents 2026** are recorded here.
Format: `YYYY-MM-DD  +Added  -Removed  ~Changed`.

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
