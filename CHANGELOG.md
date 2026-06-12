# Changelog

All notable changes to **Awesome AI Agents 2026** are recorded here.
Format: `YYYY-MM-DD  +Added  -Removed  ~Changed`.

## 2026-06-12 — Re-rank by strength / recency / popularity + readability polish (en/zh/ja sync)

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
