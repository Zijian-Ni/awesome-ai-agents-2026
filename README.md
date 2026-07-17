<div align="center">

# 🤖 Awesome AI Agents 2026

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fawesome-ai-agents-2026&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)](https://github.com/Zijian-Ni/awesome-ai-agents-2026/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-July%2017%2C%202026-blue.svg)](#)
[![Resources](https://img.shields.io/badge/Resources-580%2B-orange.svg)](#)
[![Categories](https://img.shields.io/badge/Categories-25-purple.svg)](#)
[![Audited](https://img.shields.io/badge/Spam_Audited-2026--07--17-success.svg)](#️-status-legend)
[![Chinese](https://img.shields.io/badge/Lang-中文-red.svg)](README.zh-CN.md)
[![Japanese](https://img.shields.io/badge/Lang-日本語-purple.svg)](README.ja.md)

**The definitive curated list of AI models, agent frameworks, tools, protocols, and resources for 2026 — the year agents went mainstream and AI became infrastructure.**

*Covering foundation models, multimodal AI, agent protocols (MCP/A2A), coding agents, computer use, generative AI, and more.*

### 🏷️ Status Legend

Entries may carry one or more status tags so readers can judge maturity at a glance:

- 🆕 **New** — Added in the last 60 days, still settling.
- 📦 **Archived** — Repository archived by its owner; preserved for historical reference, no further updates expected.
- 💤 **Stale** — No commits in 6+ months; project may still work but is no longer actively maintained.
- ⚠️ **Unverified** — Recent submission with limited independent traction (low stars / no third-party adoption / sole-maintainer / submitted to many awesome lists in parallel). Listed for completeness, **not endorsed** — vet before using.
- 🇨🇳 **Chinese ecosystem** — Project from a mainland-China team or primarily targeting the Chinese market.
- 🔥 **Hot** — GitHub stars grew >20% in the last 30 days; community momentum.
- ⚡ **Updated** — Received a notable release or major feature in the last 14 days.
- 🧪 **Experimental** — Promising but not production-ready; use for R&D only.
- 💰 **Freemium** — Core functionality free; paid tiers for scale/advanced features.
- 🔐 **Audited** — Has undergone independent security audit or formal verification.
- 🇨🇳 **China-first** — Optimized for Chinese language, regulation, or infra stack.

[Foundation Models](#-foundation-models-2026) · [Multimodal AI](#-multimodal--generative-ai) · [Protocols](#-agent-protocols--standards) · [Frameworks](#️-agent-frameworks) · [IDEs & Builders](#️-agent-ides--visual-builders) · [Memory](#-agent-memory) · [Tools](#-tool--api-integration) · [Sandboxing](#-agent-sandboxing--compute-isolation) · [Security](#️-agent-security) · [RAG](#-rag--knowledge) · [Coding](#-coding-agents) · [Physical AI](#-physical-ai--embodied-agents) · [Simulation](#-agent-simulation--world-models) · [Benchmarks](#-benchmarks--leaderboards) · [Computer Use](#️-computer-use--desktop-agents) · [Browser & Web](#-browser--web-agents) · [Voice](#️-voice--multimodal-agents) · [Personal](#-personal-ai-agents) · [Mobile](#-mobile-agents) · [Enterprise](#-enterprise-agent-platforms) · [Evaluation](#-agent-evaluation--observability) · [Research Tools](#-ai-research-tools) · [Learning](#-learning-resources) · [Chinese Ecosystem](#-chinese-ai-ecosystem) · [Compare](#-compare--side-by-side-tables) · [Notable 2026](#-notable-agent-projects-of-2026) · [Timeline](#-2026-ai-timeline)

</div>

---

## 🚀 Start Here

> **New to AI agents?** Follow this path:
> 1. 📖 **Understand** — what an agent actually is vs. a chatbot
> 2. 🗺️ **Find your scenario** → [Scenario Guide](#️-scenario-guide--what-should-i-use-for)
> 3. 🧩 **Copy a proven setup** → [Stack Recipes](#-stack-recipes--curated-tool-combinations)
> 4. 🔍 **Pick the right tool** → [Compare Tables](#-compare--side-by-side-tables)
> 5. ⚠️ **Avoid common mistakes** → [Anti-Picks](#️-anti-picks--what-not-to-use-for)
>
> **Already building?** Jump to:
> - 🆕 [Latest additions (July 2026)](#-2026-ai-timeline) • 🛡️ [Security](#️-agent-security) • 💰 [Cost comparison](#-foundation-models--api-cost--context)

---

## Quick Navigation

| Category | Description | Count |
|----------|-------------|-------|
| [🧠 Foundation Models](#-foundation-models-2026) | Latest LLMs from OpenAI, Anthropic, Google, Meta, and 22+ providers | 80+ |
| [🎨 Multimodal & Generative AI](#-multimodal--generative-ai) | Image, video, audio, and music generation | 20+ |
| [🔗 Agent Protocols](#-agent-protocols--standards) | MCP, A2A, and interoperability standards | 10+ |
| [🏗️ Agent Frameworks](#️-agent-frameworks) | Libraries for building autonomous AI agents | 23+ |
| [🛠️ Agent IDEs & Visual Builders](#️-agent-ides--visual-builders) | Visual / low-code environments for designing agent flows | 8+ |
| [🧠 Agent Memory](#-agent-memory) | Persistent memory and context management | 10+ |
| [🔌 Tool & API Integration](#-tool--api-integration) | Connecting agents to external services | 18+ |
| [🧪 Sandboxing & Compute Isolation](#-agent-sandboxing--compute-isolation) | Secure runtimes for agent-generated code | 7+ |
| [🛡️ Agent Security](#️-agent-security) | Prompt injection defense and guardrails | 16+ |
| [🔍 RAG & Knowledge](#-rag--knowledge) | Retrieval-augmented generation systems | 12+ |
| [💻 Coding Agents](#-coding-agents) | AI-powered software engineering | 27+ |
| [🤖 Physical AI](#-physical-ai--embodied-agents) | Humanoid robots, embodied AI, industrial automation | 22+ |
| [🎮 Simulation & World Models](#-agent-simulation--world-models) | Sim environments for training and stress-testing agents | 7+ |
| [📊 Benchmarks](#-benchmarks--leaderboards) | Leaderboards tracking frontier capability | 11+ |
| [🖥️ Computer Use](#️-computer-use--desktop-agents) | Desktop automation and OS-level control | 10+ |
| [🌐 Browser & Web Agents](#-browser--web-agents) | Agents that drive real browsers | 9+ |
| [🗣️ Voice & Multimodal Agents](#️-voice--multimodal-agents) | Voice-enabled conversational AI | 10+ |
| [📱 Personal AI Agents](#-personal-ai-agents) | Productivity and daily life assistants | 11+ |
| [📱 Mobile Agents](#-mobile-agents) | Phone-control agents (Android / iOS) | 6+ |
| [🏢 Enterprise Platforms](#-enterprise-agent-platforms) | Enterprise-grade agent deployment | 18+ |
| [📊 Evaluation & Observability](#-agent-evaluation--observability) | Testing, monitoring, and benchmarking | 17+ |
| [🔬 AI Research Tools](#-ai-research-tools) | Tools for AI/ML research and experimentation | 10+ |
| [📚 Learning Resources](#-learning-resources) | Papers, courses, and tutorials | 20+ |
| [🇨🇳 Chinese AI Ecosystem](#-chinese-ai-ecosystem) | Major projects from China-based teams | 18+ |
| [📝 Compare](#-compare--side-by-side-tables) | Side-by-side comparison tables | — |
| [🗺️ Scenario Guide](#️-scenario-guide--what-should-i-use-for) | 56 curated scenario-to-tool mappings | 56 |
| [📋 Stack Recipes](#-stack-recipes--curated-tool-combinations) | Curated multi-tool combinations | 8 |
| [⚠️ Anti-Picks](#️-anti-picks--what-not-to-use-for) | What NOT to use and why | 15 |

---

## Contents

- [🧠 Foundation Models 2026](#-foundation-models-2026)
- [🎨 Multimodal & Generative AI](#-multimodal--generative-ai)
- [🔗 Agent Protocols & Standards](#-agent-protocols--standards)
- [🏗️ Agent Frameworks](#️-agent-frameworks)
- [🛠️ Agent IDEs & Visual Builders](#️-agent-ides--visual-builders)
- [🧠 Agent Memory](#-agent-memory)
- [🔌 Tool & API Integration](#-tool--api-integration)
- [🧪 Agent Sandboxing & Compute Isolation](#-agent-sandboxing--compute-isolation)
- [🛡️ Agent Security](#️-agent-security)
- [🔍 RAG & Knowledge](#-rag--knowledge)
- [💻 Coding Agents](#-coding-agents)
- [🤖 Physical AI & Embodied Agents](#-physical-ai--embodied-agents)
- [🎮 Agent Simulation & World Models](#-agent-simulation--world-models)
- [📊 Benchmarks & Leaderboards](#-benchmarks--leaderboards)
- [🖥️ Computer Use & Desktop Agents](#️-computer-use--desktop-agents)
- [🌐 Browser & Web Agents](#-browser--web-agents)
- [🗣️ Voice & Multimodal Agents](#️-voice--multimodal-agents)
- [📱 Personal AI Agents](#-personal-ai-agents)
- [📱 Mobile Agents](#-mobile-agents)
- [🏢 Enterprise Agent Platforms](#-enterprise-agent-platforms)
- [📊 Agent Evaluation & Observability](#-agent-evaluation--observability)
- [🔬 AI Research Tools](#-ai-research-tools)
- [📚 Learning Resources](#-learning-resources)
- [🇨🇳 Chinese AI Ecosystem](#-chinese-ai-ecosystem)
- [📝 Compare — Side-by-Side Tables](#-compare--side-by-side-tables)
- [🗺️ Scenario Guide — What Should I Use For…](#️-scenario-guide--what-should-i-use-for)
- [📋 Stack Recipes — Curated Tool Combinations](#-stack-recipes--curated-tool-combinations)
- [⚠️ Anti-Picks — What NOT to Use For…](#️-anti-picks--what-not-to-use-for)
- [🌟 Notable Agent Projects of 2026](#-notable-agent-projects-of-2026)
- [📅 2026 AI Timeline](#-2026-ai-timeline)

---

## 🧠 Foundation Models 2026

*The latest large language models powering the AI ecosystem, organized by company. 60+ models from 20+ providers.*

### OpenAI
- [GPT-Live-1 / GPT-Live-1 mini](https://openai.com/index/introducing-gpt-live/) - 🆕 **July 8, 2026**. OpenAI's full-duplex conversational voice model replacing Advanced Voice Mode. Listens and speaks simultaneously (zero turn-taking lag), handles interruptions, delegates complex queries to GPT-5.5 in the background while keeping the conversation flowing. **GPT-Live-1** is default for paid users (Go/Plus/Pro); **GPT-Live-1 mini** is default for free users. Includes real-time live translation. Available on iOS, Android, and web.
- [GPT-5.6 Sol](https://openai.com/blog/gpt-5-6) - 🆕 **July 9, 2026** (GA; limited preview from June 26). OpenAI's frontier flagship in the GPT-5.6 family — "Sol" is the most capable tier with advanced reasoning, coding, biology, and cybersecurity capabilities plus "max" reasoning and "ultra" sub-agent mode. Available on ChatGPT, Codex, and the OpenAI API. Launch was delayed briefly at US government request for a national-security review; rolled out to all users in stages following the trusted-partner preview.
- [GPT-5.6 Terra](https://openai.com/blog/gpt-5-6) - 🆕 **July 9, 2026**. Mid-tier model in the GPT-5.6 family offering GPT-5.5-parity performance at approximately 2× lower cost. Designed for cost-efficient production workloads.
- [GPT-5.6 Luna](https://openai.com/blog/gpt-5-6) - 🆕 **July 9, 2026**. The fastest and most cost-efficient tier of GPT-5.6 — optimised for high-volume, speed-critical tasks.
- [ChatGPT Work](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) - 🆕 **July 9, 2026**. OpenAI's agent that turns a goal into finished work — acts across connected apps and files, stays on a project for hours, creates slides/sheets/docs/web apps, runs scheduled tasks, and uses desktop computer-use with a built-in browser. Powered by GPT-5.6. Rolling out on web/mobile starting with Pro, Enterprise, and Edu (Plus/Business next); the desktop app is available globally on Mac and Windows for all plans, including Free.
- [Sites for ChatGPT](https://openai.com/academy/chatgpt-sites/) - 🆕 **June 2026**. A Codex-powered ChatGPT feature that transforms plans and analyses into interactive, sharable websites and lightweight apps. In public beta as of the July 9, 2026 GPT-5.6 / ChatGPT Work launch.
- [Codex Business Plugins](https://venturebeat.com/orchestration/openais-codex-update-lets-agents-build-interactive-enterprise-workspaces-via-sites-and-role-specific-plugins) - 🆕 **June 2026**. Enterprise enhancements bringing sales, data analytics, and creative production plugins directly to Codex.
- [GPT-Rosalind](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/) - 🆕 **June 3, 2026**. Major update to OpenAI's life-sciences frontier model — stronger drug discovery, genomics, quantitative biology, and wet-lab troubleshooting (≈31% fewer tokens than GPT-5.5 on long-horizon genomics analyses). Research preview opened to eligible organizations worldwide; Novo Nordisk joins earlier partners Amgen, Moderna, the Allen Institute, and Thermo Fisher.

- [GPT-5.5](https://openai.com/index/gpt-5-5-system-card/) - 🆕 Released **April 23, 2026** (codename "Spud"). OpenAI's new frontier model for agentic tasks: coding, online research, data analysis, autonomous tool navigation. Significant gains in reasoning, consistency, and long-horizon task handling. Available on ChatGPT Plus / Pro / Business / Enterprise.
- [GPT-5.5 Pro](https://openai.com/index/gpt-5-5-system-card/) - 🆕 April 23, 2026. Parallel test-time compute variant for higher-accuracy cognitive tasks. Pro / Business / Enterprise tiers.
- [GPT-5.5 Instant](https://openai.com/index/gpt-5-5-instant/) - 🆕 **May 5, 2026**. New ChatGPT default model. Efficiency-first upgrade with ~50% lower hallucination rate on high-stakes prompts; available on free tier.
- [GPT-5.5-Cyber](https://openai.com/index/trusted-access-for-cyber/) - 🆕 **April 30, 2026**. Cybersecurity-specialized variant of GPT-5.5, rolled out via OpenAI's Trusted Access for Cyber (TAC) program to vetted defenders, government, critical infrastructure operators, and security vendors. Not available to the general public.
- [OpenAI Daybreak](https://thehackernews.com/2026/05/openai-launches-daybreak-for-ai-powered.html) - 🆕 **May 12, 2026**. Cyber-defense platform bundling GPT-5.5 + GPT-5.5-Cyber + Trusted-Access-for-Cyber for AI-powered vulnerability detection and patch validation; preview access extended to EU governments and security vendors.
- [GPT-Realtime-2](https://openai.com/) - 🆕 **May 8, 2026**. GPT-5-class reasoning brought to the Realtime API, 128K context, parallel tool calls with audio feedback, adjustable reasoning effort.
- [GPT-Realtime-Translate](https://openai.com/) - 🆕 **May 8, 2026**. Live speech-to-speech translation across 70+ input languages and 13 output languages.
- [GPT-Realtime-Whisper](https://openai.com/) - 🆕 **May 8, 2026**. Streaming low-latency speech-to-text companion to GPT-Realtime-2.
- [OpenAI Deployment Company (DeployCo)](https://openai.com/index/openai-launches-the-deployment-company/) - 🆕 **May 11, 2026**. New OpenAI-majority-owned services entity for enterprise AI rollout. Backed by **$4B+** from TPG / Advent / Bain Capital / Brookfield / Goldman Sachs / SoftBank and consulting partners Bain & Company, Capgemini, McKinsey. Built around Forward Deployed Engineers; absorbs the Tomoro AI consulting acquisition (~150 engineers).
- [Codex on Mobile](https://9to5mac.com/2026/05/14/openai-brings-codex-control-to-chatgpt-for-iphone-and-android/) - 🆕 **May 14, 2026**. ChatGPT iOS/Android can now remote-control the Codex desktop app — review outputs, approve actions, switch models, and kick off new tasks from the phone while the live session runs on Mac (Windows next). Rolling out as preview to Free, Plus and Go users.
- [OpenAI ↔ Malta partnership](https://openai.com/index/malta-chatgpt-plus-partnership/) - 🆕 **May 16, 2026**. First country-wide deal: every Maltese citizen / resident aged 14+ gets a free 1-year ChatGPT Plus subscription after completing a 2-hour AI literacy course built by the University of Malta. Part of the "OpenAI for Countries" initiative; phased rollout starting May 2026.
- [OpenAI ↔ Dell Codex partnership](https://openai.com/news/company-announcements/) - 🆕 **May 18, 2026**. Brings Codex to hybrid and on-premises enterprise environments via Dell Technologies infrastructure — first major Codex distribution channel outside the public cloud, targeted at regulated industries needing data-residency control.
- [ChatGPT Safety Updates — sensitive-conversation tracking](https://www.edtechinnovationhub.com/news/openai-updates-chatgpt-safety-systems-to-track-risk-across-sensitive-conversations) - 🆕 **May 18, 2026**. ChatGPT's safety systems updated to detect and track subtle escalation cues across long sessions for acute risks (suicide / self-harm / harm to others), with cross-session state retention.
- [OpenAI Guaranteed Capacity (Compute Annual Pass)](https://openai.com/news/company-announcements/) - 🆕 **May 19, 2026**. Long-term compute reservation product for enterprise AI products / agents / workflows. 1, 2, or 3-year terms; longer terms unlock larger discounts. OpenAI's structural response to the Anthropic "Priority Tier" model.
- [OpenAI ↔ Google SynthID + C2PA content provenance](https://openai.com/index/advancing-content-provenance/) - 🆕 **May 19, 2026**. OpenAI partners with Google to add durable cross-platform **SynthID watermarking** to ChatGPT/Sora images, joins C2PA, and previews a public **"is-this-image-from-OpenAI"** verifier. First major frontier-lab interop on watermarking.
- [GPT-5.4](https://openai.com/) - Released March 2026. Frontier model with 1M-token context, advanced coding, computer use, tool search. BenchLM 94, SWE-bench Verified 77.2%, OSWorld 75% (beats human).
- [GPT-5.4 Pro](https://openai.com/) - Higher-accuracy variant of GPT-5.4. BenchLM 92.
- [GPT-5.3](https://openai.com/) - Early 2026. Includes GPT-5.3 Instant (conversations) and GPT-5.3-Codex (coding).
- [GPT-5.2](https://openai.com/) - Released Dec 2025. State-of-the-art reasoning, long-context understanding, and vision.
- [GPT-5](https://openai.com/index/introducing-gpt-5/) - Launched August 2025. The default model in ChatGPT, replacing GPT-4o. Multimodal with variants: gpt-5, gpt-5-mini, gpt-5-nano.
- [GPT-4o](https://openai.com/index/hello-gpt-4o/) - Omni model with native text, vision, and audio. Retired from ChatGPT Feb 2026 but still available via API.
- [GPT-4.5](https://openai.com/) - 📦 **Retired from ChatGPT late June 2026** (API access continues; conversations auto-migrated to GPT-5.5). Released Feb 2025 as a research preview — the last GPT-4-family model in ChatGPT. o3 retiring from ChatGPT Aug 26, 2026.
- [o3 / o4-mini](https://openai.com/index/introducing-o3-and-o4-mini/) - Reasoning models with chain-of-thought for complex problem solving. Released April 2025. o3 retiring Aug 26, 2026.
- [Codex CLI](https://github.com/openai/codex) - Open-source terminal-based coding agent powered by OpenAI models. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fcodex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Anthropic

- [Claude Fable 5 (Global Reinstatement)](https://www.anthropic.com/news/redeploying-fable-5) - 🆕 **July 1, 2026**. After US Commerce Department export controls were lifted on June 30, Anthropic reinstated global access to Fable 5 across Claude.ai, the Claude Platform, Claude Code, and Claude Cowork. A new safety classifier blocking the Amazon-discovered jailbreak was deployed (blocks the reported behavior in >99% of cases). Pro/Max/Team and select Enterprise plans got Fable 5 included for up to 50% of weekly usage through July 7, then via usage credits; cloud re-enablement on AWS, Google Cloud, and Microsoft Foundry to follow. Mythos 5 remains restricted to vetted US entities.
- [Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5) - 🆕 **June 30, 2026**. The most agentic Sonnet yet — planning, browser/terminal tool use, and autonomous operation at a level that recently required Opus-class models. Performance approaches Opus 4.8 on agentic search (BrowseComp) and computer use (OSWorld-Verified) at higher effort settings, with a much wider cost-performance range than Sonnet 4.6. Now the default model for Claude.ai Free/Pro; also on Max/Team/Enterprise, Claude Code, and the API as `claude-sonnet-5`. Introductory pricing $2/$10 per million input/output tokens through August 31, 2026 (then $3/$15). Anthropic reports a lower rate of undesirable behaviors than Sonnet 4.6.
- [Claude Fable 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) - 🆕 **June 9, 2026**. Anthropic's first publicly available **Mythos-class** model — a capability tier above Opus. Surpasses Opus 4.8 across software engineering, knowledge work, vision, and scientific research benchmarks. Ships with built-in safeguards (sensitive cyber/bio queries may be rerouted to Opus 4.8). $10 / $50 per million in/out tokens. Available via Anthropic API, Amazon Bedrock, and Google Cloud Vertex AI. **⚠️ Access suspended June 12, 2026** — a US government export-control directive ordered Anthropic to disable Fable 5 and Mythos 5 for all customers pending security review. **✅ Export controls lifted June 30, 2026; access restored July 1** with a new cybersecurity classifier — see entry above ([statement](https://www.anthropic.com/news/redeploying-fable-5)).
- [Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) - 🆕 **June 9, 2026**. The same underlying Mythos-class model as Fable 5 with fewer restrictions, deployed only to vetted partners (cybersecurity firms, infrastructure providers) through **Project Glasswing** in collaboration with the US government. Successor to the April Claude Mythos Preview. **⚠️ Suspended June 12, 2026** alongside Fable 5 under a US export-control directive. **✅ Partially reinstated June 26, 2026** — US Commerce Secretary Lutnick restored access to 100+ approved US companies and federal agencies; broader reinstatement ongoing ([statement](https://www.anthropic.com/news/fable-mythos-access)).
- [Claude Opus 4.8](https://www.anthropic.com/claude/opus) - 🆕 **May 28, 2026**. Major Opus refresh: codebase-scale migrations, sharper agentic judgment, **dynamic workflows** research preview with hundreds of parallel sub-agents in a single session, manual **effort-control** panel, **3× cheaper Fast mode** at the same $5 / $25 per million in/out. Available on Anthropic native + Amazon Bedrock + AWS Claude Platform + Google Cloud + Microsoft Foundry. Teases an upcoming **Mythos-class** model series for limited orgs.
- [Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7) - 🆕 Released April 16, 2026. Advanced software engineering (SWE-bench Verified 87.6%), enhanced vision, proactive code verification. Supports `/think xhigh` reasoning effort. 1M-token context.
- [Claude Opus 4.6](https://www.anthropic.com/) - Released Feb 2026. 1M-token context, 14.5-hour task horizon. Leads Arena chat leaderboard.
- [Claude Sonnet 4.6](https://www.anthropic.com/news/claude-sonnet-4-6) - Released Feb 2026. Frontier coding and agentic performance, 1M token context window.
- [Claude Mythos Preview](https://www.anthropic.com/) - 🆕 April 2026 gated research preview. BenchLM 99 (top of leaderboard), SWE-bench Verified 93.9%. Limited to Project Glasswing partners.
- [Claude Opus 4](https://www.anthropic.com/news/claude-4) - Released May 2025. Advanced reasoning and complex task execution.
- [Claude Sonnet 4](https://www.anthropic.com/news/claude-4) - Released May 2025. Balanced performance and cost for a wide range of tasks.
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - Agentic coding tool operating directly in your terminal. Powered by Opus 4.7 with `/think xhigh` support. **July 2026**: desktop app gains a **built-in browser** enabling live website interaction (scraping, debugging, live-page inspection); Fable 5 model available since July 1.
- [Claude Security](https://www.anthropic.com/) - 🆕 **May 1, 2026**. Public beta. Enterprise security tool powered by Opus 4.7 — scans entire codebases for vulnerabilities and generates targeted patches with confidence rating, severity, reproduction steps, and recommended fixes. Available to Enterprise customers via [claude.ai/security](https://claude.ai/security).
- [Claude Finance Agents](https://www.anthropic.com/news/finance-agents) - 🆕 **May 5, 2026**. Ten Opus-4.7-powered specialised agents for pitchbook authoring, KYC, month-end close, deal screening, etc. Deployable as Claude Cowork plugins, Claude Code skills, or Managed-Agents cookbooks.
- [Claude Finance JV](https://www.anthropic.com/) - 🆕 **May 4, 2026**. $1.5B Claude deployment joint venture with Goldman Sachs and Blackstone embedding Anthropic engineers in mid-market Wall Street firms.
- [Claude Add-ins / Dreaming / Outcomes / Multi-agent orchestration](https://www.anthropic.com/news/code-with-claude-2026) - 🆕 **May 8, 2026 (Code with Claude 2026)**. Anthropic introduces Add-ins, scheduled memory review between sessions ("Dreaming"), rubric-driven "Outcomes", and a lead-agent + sub-agent orchestration model with shared filesystem and auditable trace.
- [Anthropic ↔ SpaceX Colossus 1](https://www.siliconrepublic.com/business/anthropic-joins-forces-with-spacex-for-colossus-capacity) - 🆕 **May 6, 2026**. Anthropic takes all available capacity at SpaceX's Colossus 1 Memphis datacenter (>220K NVIDIA H100/H200/GB200 GPUs, 300+ MW) for Claude Opus inference. Doubles Claude Code 5-hour rate limits on Pro/Max/Team/Enterprise; also lifts peak-hour limits.
- [Claude for Legal](https://www.anthropic.com/news/claude-for-legal) - 🆕 **May 12, 2026**. New legal stack on top of Claude Cowork: **20+ MCP connectors** (iManage, NetDocuments, DocuSign, Ironclad, LexisNexis, Westlaw, Harvey, Everlaw, Relativity, CourtListener…) + **12 practice-area plugins** (commercial, employment, privacy, product, corporate, AI governance, litigation associate, law-student bar-exam). Microsoft Word / Outlook / Excel / PowerPoint orchestration built in.
- [Claude for Small Business](https://www.anthropic.com/news/claude-for-small-business) - 🆕 **May 13, 2026**. Small-business toggle inside Claude Cowork — 15 pre-built agentic workflows across finance / ops / sales / marketing / HR / customer service, native connectors for QuickBooks, PayPal, HubSpot, Canva, DocuSign, Google Workspace, Microsoft 365. Bundled with a free PayPal-backed "AI Fluency for Small Business" course and a 10-city US workshop tour kicking off in Chicago.
- [Anthropic ↔ Gates Foundation $200M](https://www.anthropic.com/news/gates-foundation-partnership) - 🆕 **May 14, 2026**. 4-year, $200M partnership pairing grants + Claude usage credits + Anthropic engineers on global-health, life-sciences, education, and agriculture programs. All tools produced under the program will be freely available; first focus areas include vaccine R&D for polio / HPV / preeclampsia and agriculture-specific Claude extensions.
- [Anthropic ↔ PwC strategic alliance expansion](https://www.pwc.com/us/en/about-us/newsroom/press-releases/anthropic-pwc-expand-alliance-agentic-enterprise.html) - 🆕 **May 14, 2026**. PwC commits to global rollout of Claude Code + Claude Cowork, certifies 30,000 PwC professionals, and stands up a joint "Agentic Enterprise" Center of Excellence — focused on agentic build, AI-native deals, and finance / supply-chain / HR reinvention.
- [Anthropic ↔ Financial Stability Board briefing (Claude Mythos)](https://www.theguardian.com/technology/2026/may/18/anthropic-ai-claude-mythos-cyber-financial-stability-board-fsb) - 🆕 **May 18, 2026**. Anthropic briefs the global FSB on Claude Mythos cyber-flaw discovery capabilities — first time a frontier lab briefs a G20-level financial-stability regulator on a frontier model's offensive-security implications.
- [Code with Claude 2026 sessions on YouTube](https://www.infoq.com/news/2026/05/code-with-claude/) - 🆕 **May 18, 2026 (sessions published)**. Full developer-conference recordings (May 6 event) go public: Claude Code roadmap, Claude Developer Platform updates, Managed Agents dreaming + multi-agent orchestration, and partner deployments.
- [Widening the conversation on frontier AI](https://www.anthropic.com/news/widening-conversation-ai) - 🆕 **May 19, 2026**. Anthropic publishes its framework for engaging diverse traditions (religious, philosophical, indigenous) in frontier-AI safety dialogue. Companion to ongoing public-engagement work.
- [Bristol Myers Squibb ↔ Anthropic Claude Enterprise](https://news.bms.com/news/corporate-financial/2026/Bristol-Myers-Squibb-Announces-Strategic-Agreement-with-Anthropic-to-Position-Claude-Enterprise-as-the-Shared-Intelligence-Platform-Across-Its-Global-Operations/default.aspx) - 🆕 **May 20, 2026**. BMS adopts Claude Enterprise as its shared intelligence platform for 30,000+ employees globally, embedding agentic Claude into drug-discovery / development / delivery workflows. First top-5 pharma enterprise-wide Claude deployment.

### Google DeepMind
- [Gemini 3.5 Pro](https://cloud.google.com/blog/products/ai-machine-learning/innovations-from-google-io-26-on-google-cloud) - ⚠️ **Delayed — not yet released as of July 17, 2026** (limited enterprise preview with partners ongoing). Google's upcoming flagship with a reported **2-million-token context window** and **Deep Think** reasoning mode; substantially improved coding and agentic workflow capabilities. Announced at Google I/O in May 2026 for a June release, then postponed after Google scrapped and rebuilt the base model over disappointing coding performance. Third-party reports targeted July 17, but as of July 16 Google says it is still testing 3.5 Pro (alongside an upgraded Flash model) with no confirmed release date. Competes directly with GPT-5.6 Sol and Claude Fable 5.
- [Gemma 4 12B](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/) - 🆕 **June 2026**. Novel multimodal open model with a **unified, encoder-free architecture** processing text, images, and audio in a single pass. Runs locally on 16 GB VRAM.
- [DiffusionGemma](https://www.marktechpost.com/2026/06/10/google-ai-releases-diffusiongemma-a-26b-moe-open-model-using-text-diffusion-for-up-to-4x-faster-generation/) - 🆕 **June 2026**. 26B MoE open model using **text-diffusion** for up to **4× faster generation** than autoregressive models.

- [Gemini 3.5 Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - 🆕 **May 19, 2026 — Google I/O 2026**. Default model powering the Gemini app and Google Search AI Mode. Marketed as **~4× faster** than other frontier models in output tokens/sec while outperforming Gemini 3.1 Pro on key benchmarks. Gemini 3.5 Pro was slated for June 2026 but has been delayed (see above).
- [Gemini Omni / Omni Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - 🆕 **May 19, 2026 — Google I/O 2026**. New Google DeepMind multimodal **world-model** family aimed at AGI. Omni Flash, the first shipped variant, can take any input modality and generate any output (starting with video; image and text generation following). Direct lineage to Gemini Robotics / Genie line of work.
- [Gemini 3.1 Pro](https://deepmind.google/technologies/gemini/) - Released Feb 2026. BenchLM 94, GPQA Diamond 94.3% (world-record), ARC AGI2 77.1%. `$2/1M tokens` flagship.
- [Gemini 3.1 Flash Live](https://deepmind.google/technologies/gemini/) - 🆕 April 2026. Real-time multimodal streaming for voice assistants and interactive agents. Low latency, long context.
- [Gemini 3.1 Flash-Lite (GA)](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-lite-is-now-generally-available) - 🆕 **May 8, 2026**. Generally available on Gemini API / AI Studio / Vertex AI. Fastest and most cost-efficient model in the Gemini 3 family — built for low-latency code completion, real-time UX, and agentic developer tools; matches Gemini 2.5 Flash quality at significantly lower cost.
- [Gemini Omni Flash — voice-controlled video editing rollout](https://www.techtimes.com/articles/317309/20260528/google-gemini-omni-flash-brings-voice-controlled-ai-video-editing-future-conversational-ai.htm) - 🆕 **May 28, 2026**. Omni Flash starts rolling out to consumers via the Gemini app, **Google Flow**, and **YouTube Shorts** as the editing engine — conversational cinematic zooms / background swaps / weather edits driven by text, voice, image, or audio prompts; no traditional NLE required.
- [Gemini Spark (24/7 personal AI agent)](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - 🆕 **May 19, 2026 — Google I/O 2026**. Cloud-resident personal AI agent that runs **24/7** on user intent, integrates Gmail / Chat first, then ~30+ third-party tools via MCP (Adobe / Dropbox / Uber). Available to Google AI Ultra subscribers in the US within the I/O week.
- [Google AI Ultra ($100/month tier)](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - 🆕 **May 19, 2026 — Google I/O 2026**. New top consumer subscription targeted at developers / creators / power users. Gates Gemini Spark, highest Gemini 3.5 quotas, and the upcoming Gemini 3.5 Pro.
- [Gemini 3.1 Flash / Flash Lite](https://deepmind.google/technologies/gemini/) - Fast, cost-efficient models for high-throughput applications.
- [Gemini 4 (Open)](https://deepmind.google/technologies/gemini/) - 🆕 Released April 2026. Open model family: 2B / 4B / 26B / 31B variants. Strong science reasoning and document understanding, local deployment ready.
- [Gemini 2.5 Pro / Flash](https://deepmind.google/technologies/gemini/) - GA June 2025. Thinking model with 1M context.
- [Gemma 4 31B](https://github.com/google-deepmind/gemma) - 🆕 April 2026. GPQA Diamond 84.3%. Strong open-weight alternative for on-device reasoning. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle-deepmind%2Fgemma&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Gemma 3](https://github.com/google-deepmind/gemma) - Previous open model family for on-device and research use.
- [Gemini Robotics ER-1.6](https://deepmind.google/) - 🆕 April 14, 2026. Upgraded robotics AI with improved spatial and physical reasoning. Partnership with Agile Robotics for real-world deployment.

### Meta

- [Muse Image](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) - 🆕 **July 7, 2026**. Meta Superintelligence Labs' most advanced image generation model to date — an "agentic" image model that performs intermediate reasoning steps (web search, code execution, self-refinement) before producing high-quality visuals. Integrated into the Meta AI app, Instagram Stories (US), and WhatsApp in limited countries (Facebook coming soon). Note: a controversial feature allowing images from other users' public Instagram profiles was added then removed on July 10 after feedback.
- [Muse Spark 1.1](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/) - 🆕 **July 9, 2026**. Multimodal reasoning model designed for agentic tasks from Meta Superintelligence Labs — available through a new public preview of the Meta Model API. Marks a strategic shift toward proprietary revenue-focused models alongside Meta's open-source Llama line.
- [Muse Video](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) - 🆕 **July 7, 2026 (preview)**. Video generation model from Meta Superintelligence Labs, built on the same foundational technology as Muse Image; ranks #3 on Arena for text-to-video. Previewed alongside the Muse Image launch — "coming soon to creators and Meta AI."
- [Llama 5](https://ai.meta.com/llama/) - 🆕 **April 8, 2026**. 600B+ parameter open-source flagship from Meta Superintelligence Labs; "recursive self-improvement" research line. Marketed as exceeding leading proprietary models on reasoning, coding, autonomous agentic behaviour.
- [Muse Spark](https://ai.meta.com/blog/introducing-muse-spark-msl/) - 🆕 **April 9, 2026**. First model from Meta Superintelligence Labs (MSL). Natively multimodal reasoning model powering Meta AI app, smart glasses, and features across Facebook / Instagram / WhatsApp / Messenger.
- [Llama 4 Scout](https://llama.meta.com/) - 109B total params (17B active), MoE with 16 experts, 10M token context window, multimodal. Runs on single H100.
- [Llama 4 Maverick](https://llama.meta.com/) - 400B total params (17B active), 128 experts, 1M context. Outperforms GPT-4o on multimodal benchmarks.
- [Llama 4 Behemoth](https://llama.meta.com/) - 2T parameters (288B active). In training — Meta's frontier model rivaling top closed-source models.
- [Llama 3.3 70B](https://llama.meta.com/) - Strong instruction following and reasoning, open-weight under Llama Community License.

### Sakana AI

- [Sakana RL Conductor](https://venturebeat.com/orchestration/how-sakana-trained-a-7b-model-to-orchestrate-gpt-5-claude-sonnet-4-and-gemini-2-5-pro) - 🆕 **Paper April 27, 2026; Fugu beta late-April / early-May 2026**. 7B RL-trained orchestrator (built on Qwen2.5-7B) that routes subtasks between GPT-5, Claude Sonnet 4, Gemini 2.5 Pro, etc. SOTA on LiveCodeBench (83.9%) and GPQA-Diamond (87.5%) at ~1.8K tokens/query — roughly 6× cheaper than other multi-agent ensembles.
- [Sakana Fugu](https://sakana.ai/fugu-beta/) - 🆕 **Beta April 24-25, 2026**. Commercial multi-agent orchestration service productising the RL Conductor research. OpenAI-compatible API with two tiers: **Fugu Mini** (low-latency) and **Fugu Ultra** (max performance); strong reported results on SWE-Pro, GPQA-D and ALE-Bench.

### Zyphra

- [ZAYA1-8B](https://www.zyphra.com/post/zaya1-8b) - 🆕 **May 6, 2026**. MoE reasoning model (<1B active) trained end-to-end on AMD Instinct MI300X clusters. Apache 2.0 weights on Hugging Face + serverless endpoint on Zyphra Cloud; aimed at math, code, and dense reasoning per active parameter.
- [ZAYA1-8B-Diffusion-Preview](https://www.zyphra.com/post/zaya1-8b-diffusion-preview) - 🆕 **May 14, 2026**. First MoE diffusion language model converted from an autoregressive LLM and the first diffusion LM trained on AMD GPUs. Generates 16 tokens per step, achieving up to **7.7× inference speedup** vs the autoregressive base. Built with Zyphra's TiDAR recipe + CCA attention.

### Mistral AI

- [Mistral Large 3](https://mistral.ai/news/mistral-3) - 675B total / 41B active parameters, MoE, 256K context. Flagship open-weight multimodal model. Released Dec 2025.
- [Mistral Medium 3.1](https://mistral.ai/) - Frontier-class dense model for enterprise. Multimodal, 128K context, 80+ coding languages. Released Aug 2025.
- [Mistral Small 4](https://mistral.ai/news/mistral-small-4) - 🆕 Released March 2026. 119B total / 6B active. Hybrid model combining reasoning, multimodal, and coding strengths.
- [Magistral 1.2](https://mistral.ai/) - 🆕 2026 reasoning family challenging o3/o4-mini. Transparent and multilingual reasoning.
- [Devstral 2](https://mistral.ai/) - 🆕 2026 agentic coding model. Best open-source model for coding agents.
- [Codestral](https://mistral.ai/news/codestral) - 22B code generation model, 80+ programming languages, 32K context. Released May 2024.
- [Pixtral Large](https://mistral.ai/) - 124B multimodal model with 1B vision encoder, 128K context, processes 30+ high-res images.
- [Ministral 3B/8B/14B](https://mistral.ai/) - Compact models optimized for edge deployment and efficiency.
- [Mistral Forge](https://mistral.ai/) - 🆕 March 2026 platform for training custom LLMs on proprietary data.
- [Mistral Medium 3.5](https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04) - 🆕 **April 28, 2026**. Dense 128B open-weight model, 256K context, Modified MIT license. Unifies instruction-following, reasoning, and coding.
- [Leanstral 1.5](https://mistral.ai/news/leanstral-1-5/) - 🆕 **July 2, 2026**. Formal-verification model for proof engineering in Lean 4 — 119B total / 6B active parameters, Apache 2.0, weights on Hugging Face plus a free API endpoint. Scores 100% on miniF2F, solves 587/672 PutnamBench problems, and discovered 5 previously unreported bugs across 57 real-world repositories.
- [Robostral Navigate](https://mistral.ai/news/robostral-navigate/) - 🆕 **July 8, 2026**. Mistral's first robotics model — an 8B embodied-navigation model that steers wheeled, legged, and flying robots through offices, homes, and outdoor spaces from natural-language instructions using only a single RGB camera (76.6% success rate on unseen validation). Trained fully in-house on ~400K simulated trajectories.
- [Voxtral TTS](https://www.forbes.com/sites/ronschmelzer/2026/03/26/mistral-releases-open-weight-voice-ai-built-for-speed/) - 🆕 **March 26, 2026**. 4B-parameter open-weight TTS built on Ministral 3B; multilingual, optimised for voice agents.

### DeepSeek

- [DeepSeek-V4-Pro](https://api-docs.deepseek.com/news/news260424) - 🆕 **April 24, 2026 (preview); production launch mid-July 2026**. 1.6T total / 49B active MoE, 1M-token context. MIT license. Leadership in agent capabilities, world knowledge, reasoning; tops open-source benchmarks. The formal V4 launch introduced peak/off-peak API pricing (2× during Beijing peak hours); deepseek-v4-pro / deepseek-v4-flash are now the production API models.
- [DeepSeek-V4-Flash](https://api-docs.deepseek.com/news/news260424) - 🆕 April 24, 2026. 284B total / 13B active MoE, 1M context. MIT. Cost-efficient tier.
- [DeepSeek Agent Harness team](https://www.scmp.com/tech/big-tech/article/3354113/deepseek-recruits-former-jane-street-engineer-catch-ai-agents-revenue-race) - 🆕 **May 19, 2026**. DeepSeek hires a former Jane Street engineer to lead a new "AI harness" team building the deterministic scaffolding that turns DeepSeek V4 into autonomous, revenue-generating agents — first major signal DeepSeek is moving past raw-model R&D into agentic productisation.
- [DeepSeek-V3.2](https://www.deepseek.com/) - Released Dec 2025. Advanced MoE architecture with 671B total parameters. V3.2 Speciale variant for enhanced reasoning. ⚠️ API model IDs deepseek-chat / deepseek-reasoner (V3.2-era) deprecated effective July 24, 2026 — superseded by V4-Flash modes.
- DeepSeek-R2 - 🧪 **Unreleased/rumored.** No official announcement, model card, or API ID exists as of mid-July 2026; reasoning is served via V4's Thinking mode.
- [DeepSeek-R1](https://www.deepseek.com/) - Reasoning-focused model with chain-of-thought capabilities. Released Jan 2025.
- [DeepSeek-Coder-V2](https://github.com/deepseek-ai/DeepSeek-Coder-V2) - Code generation model competitive with GPT-4 on coding benchmarks. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeepseek-ai%2FDeepSeek-Coder-V2&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Alibaba (Qwen)

- [Qwen3.7-Max](https://www.scmp.com/tech/big-tech/article/3354212/alibaba-unveils-new-qwen-model-custom-chips-bid-become-chinas-ai-factory) - 🆕 **May 20, 2026 — Alibaba Cloud Summit Hangzhou**. New Qwen flagship purpose-built as the foundation for AI agents: agentic coding, complex reasoning, and **long-horizon multi-step missions** with sustained decision-making. Released alongside a full-stack AI infrastructure upgrade and new T-Head **Zhenwu M890** AI accelerator chip. Worldwide developer/enterprise availability rolling.
- [Qwen3.7-Max-Preview / Qwen3.7-Plus-Preview](https://www.scmp.com/tech/tech-trends/article/3354087/alibaba-teases-new-qwen-previews-highest-ranking-chinese-ai-models-arena) - 🆕 **May 18, 2026**. Preview ladder before the Hangzhou unveil. Ranked the highest of any Chinese model on LM Arena in both text and vision; sustained 1M-context evaluations.
- [Qwen3.6-27B](https://qwen.ai/blog?id=qwen3.6-27b) - 🆕 **April 22, 2026**. Dense 27B multimodal. Open-sourced. Focus: agentic coding + thinking-context preservation.
- [Qwen3.6-Max-Preview](https://qwen.ai/) - 🆕 **April 18, 2026**. Proprietary frontier preview. High coding/reasoning performance, 1M context window. Top-tier among Chinese models on coding benchmarks.
- [Qwen3.6-35B-A3B](https://qwen.ai/blog?id=qwen3.6-35b-a3b) - 🆕 **April 15, 2026**. MoE, 35B total / 3B active. Apache 2.0. Stability and real-world utility improvements.
- [Qwen3.6-Plus](https://qwen.ai/) - 🆕 **April 2, 2026**. Proprietary flagship. High value-per-token general model. Strong long-context, tool-calling, agentic behavior.
- [HappyHorse 1.1](https://technode.com/2026/06/23/alibaba-unveils-happyhorse-1-1-video-generation-model-launches-global-ai-filmmaking-competition/) - 🆕 **June 23, 2026**. Alibaba's video-generation model (T2V/I2V/S2V, up to 15s 1080p with synced audio, strong multi-shot character consistency). HappyHorse 1.0 entered limited beta April 28, 2026 after launching anonymously and topping video leaderboards.
- [Qwen3.5 Max Pro](https://qwen.ai/) - April 2026. High-performance flagship. Enhanced coding and math reasoning, long context.
- [Qwen3.5 Omni Plus](https://qwen.ai/) - April 2026. Proprietary full-modal foundation model unifying text and image input.
- [Qwen3-Max-Thinking](https://qwen.ai/) - Alibaba's strongest thinking model. 1T+ parameters, enhanced agentic capabilities.
- [Qwen3.5-Omni](https://qwen.ai/) - March 2026. Fully omni-modal: language, vision, sound, motion. Speech recognition in 113 languages, 256K context.
- [Qwen3-Coder-Next](https://qwen.ai/) - Feb 2026. Open-weight coding agent model, MoE 80B total / 3B active.
- [Qwen3 235B-A22B](https://qwen.ai/) - MoE with dual-mode reasoning. Strong math, code, and commonsense reasoning.
- [Qwen2.5 Coder 32B](https://github.com/QwenLM/Qwen2.5-Coder) - Top open-source coding model. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FQwenLM%2FQwen2.5-Coder&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### xAI (Grok)

- [Grok 4.5](https://x.ai/) - 🆕 **July 8, 2026**. xAI's latest flagship — optimised for coding and agentic tasks through joint training with Cursor using real developer interaction data. Features a 500K-token context window, function calling, structured outputs, web/X search, code execution, document search, and context compaction. Available in xAI API, Grok Build, and as the default model in Cursor. Priced at $2/$6 per million in/out tokens. EU availability expected later in July 2026.
- [Grok 4.3 GA](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-grok-4-3-on-microsoft-foundry-latest-generation-agentic-capabilities/4517096) - 🆕 **May 2026**. Grok 4.3 reached general availability on Microsoft Foundry and OCI Generative AI; xAI's flagship for agentic workloads with improved tool-calling and long-horizon reasoning.
- [Grok 4.3 Beta](https://x.ai/) - 🆕 April 2026. Latest iteration with improved reasoning and coding benchmarks. See [`2026.4` benchmark snapshot](https://benchlm.ai/).
- [Grok 4.20](https://x.ai/) - Feb 2026. Multi-agent system (4 standard + 16 specialized agents in Heavy mode), 2M token context.
- [Grok 4 / 4 Heavy](https://x.ai/) - Released July 2025. xAI's frontier model of the Grok 4 generation.
- [Grok 3 / 3 Mini](https://x.ai/) - Feb 2025. First reasoning models with "Think Mode".

### Microsoft (MAI)

- [Microsoft MAI-Code-1-Flash](https://microsoft.ai/news/introducingmai-code-1-flash/) - 🆕 **Build 2026 (June 2, 2026)**. Microsoft's first major in-house foundation model built entirely without OpenAI technology. 5B-parameter coding model with adaptive thinking, rolling out in GitHub Copilot. Outperforms Claude Haiku 4.5 across four core coding benchmarks (16-point lead on SWE-Bench Pro: 51.2% vs 35.2%); solves harder tasks with up to 60% fewer tokens on SWE-Bench Verified.
- [Microsoft MAI-Thinking-1](https://microsoft.ai/news/microsoft-build-2026-mai-keynote-transcript/) - 🆕 **Build 2026 (June 2, 2026)**. Microsoft's first in-house reasoning model, trained from scratch without OpenAI data. Companion to MAI-Code-1-Flash; signals Microsoft's foundation-model independence push.

### Microsoft (Phi)

- [Phi-4-reasoning-vision-15B](https://azure.microsoft.com/en-us/products/phi) - 🆕 Released March 2026. 15B multimodal model with selective chain-of-thought reasoning. Edge-deployable.
- [Phi-4](https://azure.microsoft.com/en-us/products/phi) - 14B parameter SLM with reasoning rivaling much larger models. Open-source under MIT License.
- [Phi-4-mini](https://azure.microsoft.com/en-us/products/phi) - 3.8B parameter dense model. 128K context. Excels in reasoning, math, coding, and function-calling.
- [Phi-4-multimodal](https://azure.microsoft.com/en-us/products/phi) - 5.6B parameter. First multimodal Phi model — integrates speech, vision, and text in unified architecture.

### Cohere

- [Command A+](https://cohere.com/blog/command-a-plus) - 🆕 **May 20, 2026**. 218B total / 25B active MoE, Apache 2.0 open weights (Hugging Face). 128K input / 64K output. Multimodal, 48 languages, agentic tool use; runs on 2× H100 or 1 Blackwell GPU.
- [Command A](https://docs.cohere.com/v2/changelog/command-a) - Released March 13, 2025. 111B open-weights model, 256K context. Agentic, multilingual, and coding focused.
- [Command R+](https://cohere.com/) - Enterprise RAG model, 128K context, multilingual (10 languages), grounded generation with citations.
- [Command R](https://cohere.com/) - Cost-efficient model for retrieval-augmented generation and enterprise workloads.

### Baidu (ERNIE / 文心)

- [ERNIE 5.1](https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/) - 🆕 **May 8, 2026**. ~1/3 the total and ~1/2 the active parameters of ERNIE 5.0 at ~6% of comparable pre-training cost; #1 Chinese model / #4 global on LMArena Search (1,223).
- [ERNIE 5.0](https://ernie.baidu.com/) - Released November 13, 2025 (Baidu World). 2.4T-parameter omni-modal MoE (activates <3% per query).
- [ERNIE 4.5](https://yiyan.baidu.com/) - Multimodal predecessor released 2025. Strong reasoning and Chinese language capabilities.

### Zhipu AI / Z.ai (GLM)

- [GLM-5.2](https://z.ai/blog/glm-5.2) - 🆕 **June 13, 2026**. Coding-first 744B-MoE flagship with a **1M-token context window** (~5× GLM-5.1) and up to 131K output tokens. Live across all GLM Coding Plan tiers; MIT open weights + standalone API rolling out the launch week. Works out of the box with Claude Code, Cline, OpenCode, Roo Code, Goose, and OpenClaw. (No benchmark numbers published at launch.)
- [GLM-5.1](https://z.ai/blog/glm-5.1) - 🆕 **April 8, 2026**. 744B MoE / 40B active, 200K context. MIT license. Tops SWE-Bench Pro.
- [ZCode](https://www.scmp.com/tech/tech-trends/article/3359170/zhipu-ai-releases-harness-glm-52-model-chinese-firm-takes-aim-anthropic) - 🆕 🇨🇳 **July 2, 2026**. Zhipu's agent harness for GLM-5.2 — turns the model into an autonomous coding agent, squarely targeting Claude Code; launch promos include +50% quota for Coding Plan subscribers and 5M free tokens for new users.
- [GLM-5 Reasoning](https://z.ai/) - 🆕 April 2026. BenchLM 85 — **top open-source score**. SWE-Bench Pro surpasses GPT-5.4 and Claude Opus 4.6.
- [GLM-5V-Turbo](https://z.ai/) - 🆕 April 2026. Native multimodal agent — vision, video clips, text inputs. Cost-performance balanced.
- [GLM-5](https://z.ai/) - Released Feb 2026. 744B parameters, advanced agentic intelligence. MIT license.
- [GLM-4.7](https://z.ai/) - Released late 2025. Matches Claude Opus 4 on SWE-Bench.

### MiniMax

- [MiniMax M3](https://www.minimax.io/) - 🆕 **June 1, 2026**. Open-weight (MIT) flagship with MiniMax Sparse Attention — ~1/20 the compute cost at 1M tokens; frontier coding capabilities, SWE-Bench Pro 59.0%, BrowseComp 83.5%.
- [MiniMax-M2.7 (Open Weights)](https://www.minimax.io/) - 🆕 April 2026. 230B-class open-weight flagship. Top-tier performance on coding and Agent tasks.
- [MiniMax M2.7](https://venturebeat.com/technology/new-minimax-m2-7-proprietary-ai-model-is-self-evolving-and-can-perform-30-50) - 🇨🇳 🆕 **March 2026**. Proprietary self-evolving LLM tuned for agent harness construction, memory updates, iterative workflow improvement; major gains on SWE-bench-style tasks.
- [MiniMax M2.5](https://www.codemotion.com/magazine/ai-ml/minimax-m2-5-low-costs-high-performance/) - 🇨🇳 **February 2026**. 230B-parameter cost-efficient flagship for "real-world productivity".
- [Hailuo 2.3 / 2.3 Fast](https://www.minimax.io/news/minimax-hailuo-23) - 🇨🇳 **October 2025**. MiniMax's current video flagship — SOTA physics, character micro-expressions, strong stylization; Hailuo 02 (2025) remains as the I2V-focused variant.
- [MiniMax Music 2.6](https://aimlapi.com/blog/the-ultimate-guide-to-minimax-models-2026-m2-7-music-2-6-hailuo-video-advanced-tts) - 🇨🇳 🆕 **April 10, 2026**. Cover-generation focus with improved low-frequency reproduction; global beta.
- [MiniMax-M1-80k](https://www.minimax.io/) - Open-weight hybrid-attention reasoning model. 456B parameters, 1M token context.
- [Hailuo AI (Video)](https://hailuoai.video/) - Text/image-to-video generation with AI avatars, voiceovers, and character consistency.
- [Kilo Code Integration](https://www.minimax.io/) - MiniMax models are heavily featured in Kilo Code (open-source AI coding extension at kilo.ai).

### Moonshot AI (Kimi)

- [Kimi K3](https://kimi.ai/) - 🆕 **July 16, 2026**. Moonshot AI's largest flagship: **2.8 trillion parameters** sparse MoE (16 of 896 experts activated per token), **1M-token context window**, native vision, and multi-agent capabilities. Introduces Kimi Delta Attention (hybrid linear attention for faster long-context decoding). API: $3.00 / $15.00 per million input/output tokens. Available via kimi.com, Kimi API, and integrated platforms; full open weights promised for late July 2026.
- [Kimi K2.7 Code](https://kimi.ai/) - 🆕 **June 12, 2026**. Coding-first successor to K2.6 — 1T MoE / 32B active (384 experts), 256K context, Modified MIT, on Hugging Face + Kimi API. Targets long-horizon agentic coding with ~30% lower reasoning-token use; Moonshot reports +21.8% over K2.6 on its Kimi Code Bench v2 (vendor benchmarks). $0.95 / $4.00 per million in/out tokens.
- [Kimi K2.6](https://kimi.ai/) - 🆕 **April 20-21, 2026**. 1T MoE / 32B active, 256K context. Enhanced coding, long multi-step execution, **agent swarm up to 1,000 collaborating agents**. Supports `thinking.keep="all"` persistent reasoning. Default in OpenClaw v2026.4.20+.
- [Kimi K2.5](https://kimi.ai/) - Jan-Feb 2026. 1T total / 32B active MoE. Native multimodal, Agent Swarm (up to 100 parallel sub-agents). Open-source. ⚠️ Support ending May 25, 2026 — migrate to K2.6.
- [Kimi Code](https://kimi.ai/) - Premium coding tier powered by K2.5/K2.6, terminal-based developer workflows.

### ByteDance (Doubao / 豆包)

- [Doubao 2.0](https://www.taipeitimes.com/News/biz/archives/2026/02/16/2003852382) - 🇨🇳 🆕 **February 2026**. Agent-era upgrade focused on real-world task execution; powers ByteDance's consumer AI apps.
- [Seedance 2.0](https://economictimes.indiatimes.com/us/news/seedance-2-0-goes-live-as-bytedances-ai-videos-ignite-china-market-rally/articleshow/128150649.cms) - 🇨🇳 🆕 **February 2026**. Multi-modal cinematic video generation, 2K resolution, ~30% faster than Seedance 1.5.
- [Doubao-Seed-2.0 Pro](https://seed.bytedance.com/) - 🆕 Released Feb 2026. Frontier reasoning and complex agents. Competes with GPT-5.2 at ~90% lower cost.
- [Doubao-Seed-2.0 Lite](https://seed.bytedance.com/) - 🆕 General production workloads. Balanced performance and efficiency.
- [Doubao-Seed-2.0 Code](https://seed.bytedance.com/) - 🆕 Software development — code generation, debugging, and review.
- [BAGEL](https://github.com/bytedance-seed/BAGEL) - 🆕 Open-source multimodal model for text, image, and video understanding and generation.

### Amazon (Nova)

- [Nova 2 Pro](https://aws.amazon.com/nova/) - **December 2, 2025 (re:Invent)**. Amazon's most intelligent reasoning model. Text, image, video, speech input. Agentic coding and long-range planning.
- [Nova 2 Lite](https://aws.amazon.com/nova/) - **December 2, 2025**. Fast, cost-effective reasoning with 1M-token context. Adjustable "thinking effort" controls.
- [Nova 2 Sonic](https://aws.amazon.com/nova/) - **December 2, 2025**. Speech-to-speech model for real-time conversational AI. Multilingual.
- [Nova Act](https://aws.amazon.com/nova/) - **December 2, 2025**. Browser-based AI agent service for web task automation, re-launched powered by Nova 2 Lite.
- [Nova Forge](https://aws.amazon.com/nova/) - **December 2, 2025**. "Open training" service for building custom Nova model variants with proprietary data.

### NVIDIA (Nemotron)
- [Nemotron 3.5 ASR](https://developer.nvidia.com/nemotron) - 🆕 **June 6, 2026**. NVIDIA's 600M-parameter cache-aware streaming speech recognition model — real-time transcription across 40 language-locales.
- [Nemotron 3 Ultra (550B)](https://research.nvidia.com/labs/nemotron/Nemotron-3-Ultra/) - 🆕 **June 4, 2026**. Open-weight 550B-total / 55B-active hybrid Mamba-Transformer MoE for long-running agents. Frontier-level reasoning among US open models, optimized for Blackwell.
- [Nemotron-Labs-TwoTower](https://huggingface.co/nvidia/Nemotron-Labs-TwoTower-30B-A3B-Base-BF16) - 🆕 🧪 **July 1, 2026**. Open-weight diffusion language model from NVIDIA Research, adapted from a frozen Nemotron-3-Nano-30B-A3B backbone — one tower holds context, the other writes tokens in parallel for ~2.4× throughput without retraining.
- [Nemotron 3 Super](https://developer.nvidia.com/nemotron) - 🆕 Released March 11, 2026 (GTC). 120B total / 12B active. 1M context. 5x higher throughput vs predecessor.
- [Nemotron 3 Nano](https://developer.nvidia.com/nemotron) - **December 15, 2025**. Cost-efficient hybrid Transformer-Mamba MoE. Optimized for targeted agentic tasks.
- [Nemotron 3 Nano Omni](https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/) - 🆕 **April 28, 2026**. 30B-A3B hybrid MoE (Mamba + Transformer). Natively multimodal: text, image, audio, video, charts, and documents in one model. 9x higher throughput than comparable open omni models. Topped 6 leaderboards (MMlongbench-Doc, OCRBenchV2, WorldSense, DailyOmni, VoiceBench). Open weights on Hugging Face, OpenRouter, Amazon SageMaker JumpStart.

### Tencent (Hunyuan)

- [Hunyuan Hy3](https://hy.tencent.com/research/hy3) - 🆕 🇨🇳 **July 6, 2026**. Official Hy3 release (295B total / 21B active MoE, 256K context) under Apache 2.0. Strengthened reinforcement learning over the April preview with better stability and cost efficiency. Open weights on Hugging Face and ModelScope, rolling out to OpenRouter. Integrated across Yuanbao, CodeBuddy, WorkBuddy, ima, Marvis, and Weixin customer service.
- [Hunyuan Hy3 Preview](https://hy.tencent.com/hy3-preview) - 🇨🇳 **April 2026**. Preview that preceded the official Hy3: fast-slow thinking fusion architecture, 40% improved inference efficiency, vLLM and SGLang support. Open-sourced on GitHub, Hugging Face, ModelScope, GitCode. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTencent-Hunyuan%2FHy3-preview&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Apple

- [Apple Foundation Models (AFM)](https://machinelearning.apple.com/research/introducing-apple-foundation-models) - On-device (~3B) and server-based models powering Apple Intelligence. Privacy-first, offline capable. **WWDC 2026 (June 8)**: third-generation AFM lineup (AFM Core, AFM Core Advanced on-device; AFM Cloud, AFM Cloud Pro on Private Cloud Compute) powers the revamped Siri. Trained with help of a custom Google Gemini foundation (~$1B/yr deal) via distillation, but ships no Google code. New iOS 27 "Extensions" framework lets ChatGPT, Claude, or Gemini act as third-party AI alongside Siri.
- [OpenELM](https://machinelearning.apple.com/research/openelm) - Open-source efficient language models (270M–3B). Designed for on-device processing on Apple silicon.

### Samsung

- [Samsung Gauss 2.3](https://www.sammobile.com/news/samsung-develops-own-agentic-ai-tools-improves-gauss-ai-models/) - **November 2025**. Samsung Research's in-house LLM family (Gauss 2.3, Gauss 2.3 Think, Gauss O Flash) powering internal agentic tools; backs Galaxy S26 system-wide agentic AI (launched 2026).

### StepFun

- [Step 3.7 Flash](https://github.com/stepfun-ai/Step-3.7-Flash) - 🆕 🇨🇳 **May 29, 2026**. Open-weight 198B MoE vision-language model for coding agents and search workflows; up to ~400 tokens/s. Successor to Step 3.5 Flash.
- [Step 3.5 Flash](https://github.com/stepfun-ai/Step-3.5-Flash) - 🇨🇳 **February 2026**. Open-weight 196B MoE (11B active) reasoning + agent model; punches above its weight against larger rivals.

### Baichuan

- [Baichuan-M3 Plus](https://pandaily.com/baichuan-ai-launches-low-hallucination-medical-model-m3-plus-announces-free-access-program) - 🇨🇳 🆕 **January 2026**. Evidence-anchored medical LLM with low hallucination rate; free API for Chinese medical institutions.

### Inflection AI

- [Inflection 2.5 / Pi](https://inflection.ai/) - 💤 Empathetic conversational AI (Inflection 2.5, March 2024). Company pivoted to enterprise AI after Microsoft absorbed most of its team (2024); no longer building next-generation frontier models. Pi remains available in limited form.

### 01.AI

- [Yi-Lightning](https://www.01.ai/) - 💤 MoE architecture, 200+ tokens/s on RTX 4090. Strong multilingual (Chinese/English). Released Oct 2024 — 01.AI's last major model; the company stopped LLM pre-training in March 2025 and pivoted to DeepSeek-based enterprise solutions.

### Chinese Academy of Sciences

- [ScienceOne 100 / 磐石100](https://english.cas.cn/newsroom/cas-in-media/202604/t20260429_1158251.shtml) - 🆕 **April 28-29, 2026**. AI model system for scientific research from CAS. Core "ScienceOne" foundation model with literature compass, innovation evaluation engine, and 2,000+ tool agent factory. Supports math, physics, biology, materials science, astronomy, aerospace, and geosciences. In use across 50+ CAS institutes and 100+ research scenarios.

---

## 🎨 Multimodal & Generative AI

*Tools and models for generating and editing images, videos, audio, and music.*

### Image Generation

- [Meta Muse Image](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) - 🆕 **July 7, 2026**. Meta's most advanced image generation model from MSL — agentic design that performs web search, code execution, and self-refinement before producing images. Rolled out in Instagram Stories (US) and WhatsApp in limited countries (Facebook coming soon). Also accessible in the Meta AI app and on meta.ai.
- [Midjourney V8.1](https://updates.midjourney.com/v8-1-alpha/) - 🆕 **April 14, 2026**. HD mode now default (3× faster/cheaper), stable moodboards & style references, image prompts restored; alpha-only at alpha.midjourney.com. V8 upscalers and edit/inpaint upgrades planned next.
- [FLUX.2 Pro / Flex / Dev / Klein](https://bfl.ai/blog/flux-2) - 🆕 **November 25, 2025**. Black Forest Labs' next-generation family. SOTA image quality, multi-reference consistency (up to 10 images), dramatically improved text rendering; open-weight 32B Dev variant.
- [Recraft V4 / V4.1](https://www.recraft.ai/blog/introducing-recraft-v4-design-taste-meets-image-generation) - 🆕 **February 17, 2026** (V4.1 **May 14, 2026**). Ground-up rebuild; major prompt-accuracy improvements; editable SVG vector output. V4.1 adds better photorealism, 3D/gradients, and Vector/Utility variants.
- [Stable Diffusion 3.5](https://stability.ai/) - Open-source image generation with improved coherence and prompt following.
- [Ideogram 3.0](https://ideogram.ai/) - Excels at text rendering in images; March 2025 release with style references and in-platform canvas editor.
- [ChatGPT Images 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/) - 🆕 **April 21, 2026**. State-of-the-art image generation with improved text rendering, multilingual support, advanced visual reasoning, and multi-turn editing for iterative refinement.
- [gpt-image-2](https://developers.openai.com/api/docs/models/gpt-image-2) - 🆕 **April 21, 2026**. OpenAI's latest image generation/editing API model with flexible image sizes and high-fidelity inputs.
- [DALL·E 3](https://openai.com/dall-e-3) - OpenAI's text-to-image model integrated with ChatGPT for iterative refinement.
- [Gemini 3 Pro Image (Nano Banana Pro)](https://deepmind.google/models/gemini-image/pro/) - Google's native image generation within Gemini.
- [Nano Banana 2 (Gemini 3.1 Flash Image)](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/) - 🆕 **February 26, 2026**. Nano Banana Pro-level quality and world knowledge at Flash speed; up to 5-character consistency, 512px–4K output, text rendering/translation in images.
- [Kling Image 3.0 / 3.0 Omni](https://ir.kuaishou.com/news-releases/news-release-details/kling-ai-launches-30-model-ushering-era-where-everyone-can-be/) - 🇨🇳 🆕 **February 5, 2026**. Kuaishou's native 2K/4K image generation, launched alongside Video 3.0 in the Kling 3.0 suite.
- [Flux](https://github.com/black-forest-labs/flux) - 💤 **Stale** (last update 2025-07). Black Forest Labs' original open-source repo — superseded by Flux 2 family. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fblack-forest-labs%2Fflux&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Seedance 2.0 (image side)](https://seed.bytedance.com/) - 🇨🇳 🆕 ByteDance's next-gen image/animation generation API; pairs with the video model of the same name.

### Video Generation

- [Meta Muse Video](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) - 🆕 **July 7, 2026 (preview)**. Video generation model from Meta Superintelligence Labs built on the same architecture as Muse Image; ranks #3 on Arena for text-to-video. Previewed at the Muse Image launch; broader rollout anticipated across Meta apps.
- [Runway Agent](https://runwayml.com/news/introducing-runway-agent) - 🆕 **May 13, 2026**. Conversational agent that takes a written brief and ships a complete **multi-shot finished video**: storyboard → generation → cut → voiceover, with a timeline editor for final adjustments; first credible end-to-end "prompt-to-rough-cut" production agent.
- [Veo 3.1](https://deepmind.google/technologies/veo/) - 🆕 **October 2025**. Google DeepMind's flagship video model. **Veo 4** still unreleased as of mid-July 2026.
- [Runway Gen-4.5](https://runwayml.com/research/introducing-runway-gen-4.5) - 🆕 **December 2025**. Runway's flagship video model, #1 on the Artificial Analysis text-to-video benchmark at launch. Platform also exposes third-party models incl. Kling 3.0 and Sora 2 Pro (added February 20, 2026).
- [Kling VIDEO 3.0](https://app.klingai.com/) - 🇨🇳 🆕 **February 4-7, 2026**. Kuaishou's new generation; realistic human motion, lip-sync, narrative production with audio sync.
- [Sora 2 (via Runway)](https://runwayml.com/changelog) - OpenAI's Sora app shut down April 26, 2026 (API until September 24, 2026), but Sora 2 Pro has been available inside Runway since **February 20, 2026**.
- [Seedance 2.5](https://seed.bytedance.com/) - 🇨🇳 🆕 🧪 **June 23, 2026**. ByteDance's next video model announced at the Volcano Engine 2026 conference: native 30-second one-shot generation (up from 4-15s) with improved character/product consistency across longer narratives. Limited availability at launch — no public pricing or confirmed API yet.
- [Seedance 2.0](https://seed.bytedance.com/) - 🇨🇳 **February 2026**. ByteDance multi-modal cinematic video generation, 2K resolution (upgraded to 4K output June 23, 2026), ~30% faster than 1.5.
- [Hailuo 2.3](https://www.minimax.io/news/minimax-hailuo-23) - 🇨🇳 **October 28, 2025**. MiniMax's flagship video model: SOTA physics, character micro-expressions, strong stylization (anime/ink-wash/game CG); Hailuo 2.3 Fast variant at Hailuo 02 pricing.
- [Pika 2.5](https://pika.art/) - Creative video generation with scene and effects control.
- [LTX Studio](https://ltx.studio/) - 🆕 AI-powered cinematic video creation platform.
- [HappyHorse 1.1](https://technode.com/2026/06/23/alibaba-unveils-happyhorse-1-1-video-generation-model-launches-global-ai-filmmaking-competition/) - 🇨🇳 🆕 **June 23, 2026**. Alibaba's video model (revealed April 10, 2026 as "HappyHorse-1.0" after topping benchmarks anonymously; rose to #2 globally). 1.1 upgrades motion dynamics, subject consistency, prompt adherence, and audio generation. Available via the HappyHorse site, Alibaba Cloud Bailian, and Qwen Cloud.
- [Sora](https://openai.com/sora/) - 📦 **Discontinued** (app April 26, 2026; API September 24, 2026). OpenAI's text-to-video app shut down; Sora 2 Pro lives on inside Runway.

### Audio & Music

- [ElevenLabs Eleven v3 + ElevenAgents](https://elevenlabs.io/agents) - 🆕 2026 "audio layer of the internet" — 70+ language TTS with emotional Audio Tags, plus the AIUC-1-certified ElevenAgents voice-agent platform with multimodal messages, conversation topic discovery, and pre-tool speech controls.
- [Eleven Music + Scribe v2 Realtime](https://elevenlabs.io/) - 🆕 ElevenLabs' music generation and live transcription stack.
- [Cartesia Sonic 3 / 3.5](https://cartesia.ai/blog/introducing-line-for-voice-agents) - 🆕 **2026**. State-space-model TTS hitting ~40-90ms time-to-first-audio (Sonic 3.5 GA May 2026); powers the **Line** voice-agent platform (Line agents run on Sonic 3.5 TTS + Ink-2 STT by default since May 2026).
- [Deepgram Nova-3 + Aura-2 + Flux Multilingual](https://deepgram.com/learn/best-voice-ai-agents-2026-buyers-guide) - 🆕 **April 2026**. Speech-to-text in 45+ languages, sub-200ms TTS, conversational STT with mid-call language switching across 10 languages.
- [MiniMax Music 2.6](https://aimlapi.com/blog/the-ultimate-guide-to-minimax-models-2026-m2-7-music-2-6-hailuo-video-advanced-tts) - 🇨🇳 🆕 **April 10, 2026** (global beta). Cover generation focus with improved low-frequency reproduction.
- [Voxtral TTS](https://www.forbes.com/sites/ronschmelzer/2026/03/26/mistral-releases-open-weight-voice-ai-built-for-speed/) - 🆕 **March 26, 2026**. Mistral's open-weight 4B TTS built for voice-agent latency.
- [Suno v5.5](https://suno.com/blog/v5-5) - 🆕 **March 26, 2026**. AI music generation with high-quality vocals; v5.5 adds Voices (sing with your own verified voice), Custom Models trained on your uploads, and My Taste personalization. V6 rumored but unannounced.
- [Udio](https://www.udio.com/) - 🆕 Text-to-music generation with professional audio quality.
- [OpenAI Audio Models](https://openai.com/) - Native audio understanding and generation within GPT-4o and GPT-Realtime-2 (**May 7, 2026**, with GPT-Realtime-Translate and GPT-Realtime-Whisper); gpt-realtime-2.1 and 2.1-mini released **July 6, 2026** with improved alphanumeric recognition, noise handling, and interruption behavior.
- [Stability Audio](https://stability.ai/) - Open-source audio and music generation.
- [Bark](https://github.com/suno-ai/bark) - 💤 **Stale** (no commits since 2024-08). Open-source text-to-audio model supporting speech, music, and sound effects. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsuno-ai%2Fbark&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hume TADA](https://github.com/HumeAI/tada) - 🆕 **March 2026**. Hume AI's first open-source TTS — Text Audio Dual Alignment (TADA): text and audio generated in one synchronized 1:1 token stream; zero content hallucinations, ~0.09 RTF, TADA-1B/3B-ML models (9+ languages), runs on a smartphone. MIT code, Llama 3.2 licensed weights. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHumeAI%2Ftada&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🔗 Agent Protocols & Standards

*Open standards enabling agent interoperability, tool access, and cross-platform communication.*

### Model Context Protocol (MCP)

- [MCP Specification](https://modelcontextprotocol.io/) - 🆕 The "USB-C for AI" — open protocol by Anthropic for connecting LLMs to tools and data sources. Donated to Agentic AI Foundation (Linux Foundation) in Dec 2025.
- [MCP 2026-07-28](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) - 🆕 **Final spec July 28, 2026 (RC published May 21, 2026)**. Next major MCP revision: **stateless protocol core** (deploy behind plain round-robin load balancers, no session affinity), **Extensions Framework** (reverse-DNS IDs, independent versioning), **MCP Apps** (server-rendered UIs in sandboxed iframes), **Tasks** moved from experimental core to an extension, and **authorization hardening** (six SEPs tightening OAuth 2.0 / OpenID Connect alignment). Also: full JSON Schema 2020-12, W3C Trace Context, formal 12-month deprecation policy; Roots, Sampling, and Logging deprecated. [SDK betas (Python, TypeScript, Go, C#) shipped June 29, 2026](https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/).
- [MCP Servers](https://github.com/modelcontextprotocol/servers) - Official reference implementations of MCP servers for popular services. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Fservers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Official TypeScript SDK for building MCP clients and servers. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Ftypescript-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Official Python SDK for MCP implementation. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Fpython-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [mcp.so](https://mcp.so/) - 🆕 Community directory of MCP servers and tools.
- [CorpusIQ](https://mcp2.corpusiq.io/mcp) - 🆕 ⚠️ **Unverified.** Listed in the MCP Registry as `io.corpusiq/multi-source-mcp` — multi-source business data connector with 25+ integrations (GA4, Google Ads, TikTok, YouTube, Shopify, Stripe, Airtable, Slack, HubSpot, Calendly, Klaviyo, and more). Intelligent query routing, cross-source attribution, unified business intelligence. Live as `io.corpusiq/multi-source-mcp`. HTTP transport with Ed25519 signature auth.
- [Agentage Memory](https://memory.agentage.io/mcp) - 🆕 ⚠️ **Unverified.** Listed in the MCP Registry as `io.agentage/memory` — one shared, file-backed memory every AI (Claude / Cursor / ChatGPT) reads and writes; mirrored locally as plain markdown you own and can export. Remote Streamable HTTP at `https://memory.agentage.io/mcp` with OAuth 2.1 + PKCE + Dynamic Client Registration. Six tools: `memory__search/read/write/edit/list/delete`. [Docs](https://agentage.io/blog/mcp-endpoint-is-live).
- [mcp-gateway](https://github.com/Zijian-Ni/mcp-gateway) - ⚠️ **Unverified** (early-stage). Gateway server for routing and managing MCP connections. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fmcp-gateway&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Agent-to-Agent Protocol (A2A)

- [A2A Protocol](https://github.com/a2aproject/A2A) - Open standard for agent-to-agent communication, originated at Google, now a Linux Foundation project with 150+ partner organizations. **v1.0 shipped May 2026**. Enables agents to discover, delegate, and collaborate regardless of framework; SDKs for Python, Go, JS, Java, .NET, Rust. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fa2aproject%2FA2A&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [A2A Course (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/a2a-the-agent2agent-protocol/) - 🆕 Free course on building multi-agent systems with A2A.

### Other Standards

- [Agentic AI Foundation](https://aaif.io/) - 🆕 Linux Foundation body stewarding open agent standards — hosts MCP, goose, AGENTS.md, and agentgateway. Founding platinum members: AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, OpenAI.
- [AGENTS.md](https://agents.md/) - 🆕 Open Markdown convention — "a README for agents" — giving AI coding agents a predictable place for project-specific context and instructions. Used by 60k+ open-source projects; stewarded by the Agentic AI Foundation (Linux Foundation).
- [Coinbase Base MCP](https://fortune.com/2026/05/26/coinbase-pushes-further-into-ai-payments-with-new-mcp-for-base-network/) - 🆕 **May 26, 2026**. Coinbase ships an MCP server for the Base blockchain, letting Claude / Cursor / ChatGPT agents execute crypto trades and lending operations on-chain. First major exchange-grade MCP endpoint for autonomous on-chain transactions.
- [Robinhood Agentic Trading MCP](https://robinhood.com/us/en/newsroom/robinhood-is-now-open-to-agents/) - 🆕 **May 27, 2026** (beta). First US broker to expose stock trading via MCP. AI agents (Claude / Codex / Cursor) get read access to accounts and trade-execute access only inside a dedicated ring-fenced Agentic account; push notifications on every trade, one-tap kill switch.
- [The Declaration of Intelligence](https://thedeclaration.ai) - ⚠️ Draft (v0.2) declaration of principles for AI agents and humans, signed publicly via GitHub pull request. Early-stage — a handful of signatories at last check.
- [Kuberna Labs](https://github.com/kawacukennedy/kuberna-labs) - ⚠️ **Unverified.** Cross-chain intent execution protocol for AI agents. Claims ERC-8004 on-chain identity, zkTLS/TEE attestation, and a typed intent schema enabling agents to autonomously execute transactions across NEAR, Base, and Mantle with verifiable execution proofs. New repo, independent adoption unverified — listed for visibility, evaluate before depending on it.

---

## 🏗️ Agent Frameworks

*Frameworks and libraries for building autonomous AI agents.*

- [Vercel Eve](https://github.com/vercel/eve) - 🆕 **June 17, 2026 (Vercel Ship 2026)**. Open-source, filesystem-first TypeScript agent framework — an agent is a directory of files (instructions, tools, skills) that Vercel compiles into a durable service with sandboxed execution, approvals, evals, and OpenTelemetry built in. Works with any model, any MCP server, and channels like Slack / Discord / GitHub; billed as "Next.js for agents." Apache-2.0. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvercel%2Feve&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Databricks Omnigent](https://github.com/omnigent-ai/omnigent) - 🆕 **June 2026**. Open-source meta-harness that sits above the coding agents you already run (Claude Code, Codex, Pi, custom) and makes them interoperable parts of one system — compose agents, enforce shared security policies, and share / collaborate in real time. Apache-2.0. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fomnigent-ai%2Fomnigent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Nokia NSP Agentic AI](https://www.globenewswire.com/news-release/2026/06/11/3310210/0/en/nokia-introduces-agentic-ai-framework-in-network-services-platform-to-enable-trust-based-ai-operations-for-ip-networks.html) - 🆕 **June 2026**. Enterprise agentic framework for telecom Network Services Platforms (NSP), deploying agents to reason and execute routing/maintenance on complex IP networks.
- [Alteryx Agent Studio](https://www.alteryx.com/blog/new-capabilities-in-alteryx-one-built-for-how-analysts-work) - 🆕 **May 2026**. Packages trusted Alteryx datasets and workflows into conversational agents; creates and manages MCP endpoints via the new Alteryx One MCP Server (answers in Claude, ChatGPT, Gemini).
- [Koog 1.0](https://github.com/JetBrains/koog) - 🆕 **May 21, 2026 — KotlinConf 2026**. JetBrains' open-source agent framework for **Kotlin + Java** hits a stable 1.0 with a long-term-supported stable API surface. Kotlin Multiplatform deployment (JVM / Android / iOS / JS / WASM), Java interop without wrapper modules, local Android LiteRT, OpenTelemetry across all targets, graph-based workflows, Spring Boot / Ktor integration, and providers for OpenAI / Anthropic / Google / Bedrock. Apache-2.0. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FJetBrains%2Fkoog&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangChain](https://github.com/langchain-ai/langchain) - Build context-aware reasoning applications with LLMs. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangGraph](https://github.com/langchain-ai/langgraph) - Build resilient language agents as graphs with stateful, multi-actor orchestration. The 0.3.x series (2025) split prebuilt agents into `langgraph-prebuilt` (Supervisor, Swarm, LangMem, Trustcall). **v1.2 (May 2026)** adds per-node timeouts / error recovery / graceful shutdown, a new `DeltaChannel` to cut checkpoint overhead on long threads, and a content-block-centric streaming API v3. Latest: v1.2.4 (June 2026). ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flanggraph&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [CrewAI](https://github.com/crewAIInc/crewAI) - Framework for orchestrating role-playing autonomous AI agents in collaborative teams. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FcrewAIInc%2FcrewAI&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [goose](https://github.com/block/goose) - Open-source, extensible AI agent from Block (Rust desktop app + CLI) that installs, executes, edits, and tests with any LLM; 15+ providers; hosted by the Agentic AI Foundation (Linux Foundation). v1.43.0 (July 14, 2026). ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fblock%2Fgoose&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AG2](https://github.com/ag2ai/ag2) - 🆕 **July 3, 2026 (v1.0.0b0)**. Community-driven fork of Microsoft AutoGen — the active development path after Microsoft placed AutoGen in maintenance mode in Q1 2026. Preserves the conversable-agent model with continued bug fixes, new integrations, and feature work. Apache-2.0. Drop-in migration from existing AutoGen projects. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fag2ai%2Fag2&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/) - 🆕 Unified framework merging AutoGen + Semantic Kernel. Multi-agent conversations with enterprise features.
- [Microsoft Agent 365](https://techcommunity.microsoft.com/blog/agent-365-blog/what%E2%80%99s-new-in-agent-365-may-2026/4516340) - 🆕 **GA May 2026**. Enterprise observability + governance + security for AI agents across environments; May 2026 update adds Secure Access Service Edge (SASE) for agents, threat detection / blocking, and agent-threat-hunting workflows. KPMG announced a global deployment covering 276,000 professionals (June 9, 2026).
- [Microsoft Scout](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) - 🆕 **June 2, 2026 (Build 2026)**. Microsoft's always-on personal work agent for Microsoft 365, built on the open-source OpenClaw runtime.
- [AutoGen](https://github.com/microsoft/autogen) - 💤 **Maintenance mode** (last release Sep 2025; superseded by Microsoft Agent Framework, community-managed going forward). Multi-agent conversation framework by Microsoft. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fautogen&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Google Agent Development Kit (ADK)](https://github.com/google/adk-python) - 🆕 Modular framework integrated with Gemini and Vertex AI. Hierarchical agent compositions. **v2.0 in beta** (v2.0.0b1, April 2026) with workflow orchestration and a revamped agent execution model; latest stable v1.33 (May 2026). ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle%2Fadk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - 🆕 [Next evolution shipped April 15, 2026](https://openai.com/index/the-next-evolution-of-the-agents-sdk/) — native sandbox execution, MCP-native tool use, sub-agent handoffs, Codex-style filesystem ops. Production-ready multi-agent workflows. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fopenai-agents-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MetaGPT](https://github.com/geekan/MetaGPT) - Multi-agent framework assigning different roles to GPTs for collaborative software entities. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgeekan%2FMetaGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Mastra](https://github.com/mastra-ai/mastra) - 🆕 TypeScript-first agent framework with workflow-driven development and built-in observability. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmastra-ai%2Fmastra&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Ontheia](https://github.com/Ontheia/ontheia) - ⚠️ **Unverified** (early-stage, low adoption). Self-hosted, open-source AI agent platform. Multi-provider (Claude, OpenAI, Gemini, Ollama), MCP-native, Chain Engine for visual workflow automation, long-term memory (pgvector), multi-user RBAC, GDPR-compliant by architecture. AGPL-3.0. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOntheia%2Fontheia&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentGPT](https://github.com/reworkd/AgentGPT) - 📦 **Archived** (2026-01). Assemble, configure, and deploy autonomous AI agents in your browser. Influential first-wave project, kept for historical reference; no longer maintained. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Freworkd%2FAgentGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [BabyAGI](https://github.com/yoheinakajima/babyagi) - Experimental self-building autonomous agent framework; the original 2023 task-management BabyAGI now lives at [babyagi_archive](https://github.com/yoheinakajima/babyagi_archive). ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fyoheinakajima%2Fbabyagi&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) - 💤 **Stale** (no commits since 2025-01). Open-source autonomous AI agent framework to build, manage & run agents. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTransformerOptimus%2FSuperAGI&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) - Integrate LLM technology into apps. C#, Python, Java support. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fsemantic-kernel&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agno (formerly Phidata)](https://github.com/agno-agi/agno) - Build multi-modal agents with memory, knowledge, tools and reasoning; v2.7.x (July 2026). ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagno-agi%2Fagno&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [DSPy](https://github.com/stanfordnlp/dspy) - The framework for programming—not prompting—language models. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstanfordnlp%2Fdspy&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenClaw](https://github.com/openclaw/openclaw) - 🆕 Personal AI agent platform with skills, memory, multi-channel messaging, Dreaming (3-stage memory consolidation), Canvas/A2UI, ACP coding harness integration, and Standing Orders. Latest: **v2026.7.1** (July 13, 2026). ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenclaw%2Fopenclaw&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Dify](https://github.com/langgenius/dify) - Open-source LLM app development platform with visual agent builder. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flanggenius%2Fdify&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Haystack Agents](https://github.com/deepset-ai/haystack) - End-to-end LLM framework for agentic pipelines. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeepset-ai%2Fhaystack&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vellum AI](https://www.vellum.ai/) - 🆕 Production-grade agent framework with prompt-based building, evaluations, versioning, and observability.
- [FastAgency](https://github.com/airtai/fastagency) - 💤 Deploy AG2 (AutoGen) multi-agent workflows to production via console, Mesop web UI, REST/FastAPI, and NATS adapters; last release Dec 2025. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fairtai%2Ffastagency&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Rasa](https://github.com/RasaHQ/rasa) - 💤 **Maintenance mode** (last release Jan 2025; successor: Rasa CALM). Open-source conversational AI with strong intent recognition and dialogue management. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FRasaHQ%2Frasa&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Lindy](https://www.lindy.ai/) - 🆕 Top no-code agent framework for business users with visual workflow builder.
- [Octomind](https://github.com/muvon/octomind) - 🆕 Rust-based open-source AI agent runtime. Model-agnostic (13+ providers), community-built specialist agents (developer, medical, legal, DevOps), MCP support with runtime self-extension, zero-config setup. Apache 2.0. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmuvon%2Foctomind&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsoft AI Agent Governance Toolkit](https://www.helpnetsecurity.com/2026/04/03/microsoft-ai-agent-governance-toolkit/) - 🆕 **April 3, 2026**. Open-source toolkit for enforcing runtime security policies across agent frameworks including LangChain and AutoGen. Policy-as-code approach for enterprise AI governance.
- [Bernstein](https://github.com/sipyourdrink-ltd/bernstein) - 🆕 Python orchestrator for 40+ CLI coding agents (Claude Code, Codex, Gemini CLI, Cursor, Aider). One LLM plan call up front; scheduling, git worktree isolation, quality gates, and HMAC-chained audit are deterministic. Apache-2.0. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsipyourdrink-ltd%2Fbernstein&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Genkit Middleware](https://developers.googleblog.com/announcing-genkit-middleware-intercept-extend-and-harden-your-agentic-apps/) - 🆕 **May 14, 2026**. New middleware system for Google's open-source Genkit framework. Composable hooks at the generate / model / tool layers — retries with exponential backoff, model fallbacks, tool approval gates, scoped filesystem access, skill injection from `SKILL.md`. TypeScript / Go / Dart; Python next.
- [Coze Studio](https://github.com/coze-dev/coze-studio) - 🆕 🇨🇳 ByteDance's open-source AI agent development platform — all-in-one visual builder for creating, debugging, and deploying agents. Apache-2.0, 20K+ stars; open-source counterpart to Coze.com. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LlamaIndex ↔ Google Agents API integration](https://www.kucoin.com/news/flash/google-launches-agents-api-llama-index-integrates-llamaparse-for-unstructured-document-processing) - 🆕 **May 20, 2026**. LlamaIndex ships a template for Google's newly launched Agents API exposing **LlamaParse** / **LiteParse** over unstructured documents inside a sandboxed Linux environment.
- [NarraNexus](https://github.com/NetMindAI-Open/NarraNexus) - Ready-to-run AI agent team workspace by NetMind.AI — memory-aware agents that remember, collaborate, and use tools from day one. Multi-agent (PM/dev/deployment/research), persistent context, MCP-style integrations, composable modules. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNetMindAI-Open%2FNarraNexus&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Strands Agents (AWS)](https://github.com/strands-agents/sdk-python) - 🆕 **April–June 2026**. AWS open-source model-driven agent SDK (Python + TypeScript 1.0 GA April 30, 2026). Model-agnostic (Bedrock, Anthropic, OpenAI, Ollama), multi-agent orchestration patterns (graph/swarm/workflow), built-in observability hooks, A2A Protocol support; TypeScript SDK now maintained in the [harness-sdk monorepo](https://github.com/strands-agents/harness-sdk). Apache-2.0. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstrands-agents%2Fsdk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [CrewAI 1.14](https://github.com/crewAIInc/crewAI) - 🆕 **June 2026**. Major update ships pluggable backends for memory, knowledge, and RAG; declarative Flows with CLI/TUI support; Chat API for conversational agent flows; native Snowflake Cortex LLM provider; removed LangChain dependency for a lighter core. Latest stable: 1.14.6 (May 28, 2026). ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FcrewAIInc%2FcrewAI&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Oracle AI Agent Studio (Fusion)](https://www.oracle.com/news/announcement/oracle-introduces-ai-native-builder-experience-2026-07-14/) - 🆕 **July 14, 2026**. AI-native builder within Oracle Fusion Cloud Applications for creating Fusion Agentic Applications — outcome-driven systems powered by teams of specialized agents that reason and execute within Fusion's business objects, workflows, and security context. No-code / low-code / pro-code options; included at no additional cost to Fusion customers.

---

## 🛠️ Agent IDEs & Visual Builders

*Visual environments for designing, debugging, and shipping agent workflows without (or with minimal) code.*

- [LangGraph Studio](https://docs.langchain.com/langsmith/studio) - Visual debugger and trace inspector for LangGraph agents (now part of LangSmith) — step through state, replay turns, edit messages mid-flight. Companion to the LangGraph runtime.
- [Dify](https://github.com/langgenius/dify) - Open-source LLM app development platform with drag-and-drop agent workflow builder. Mainstream production deployments. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flanggenius%2Fdify&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agenta](https://github.com/agenta-ai/agenta) - 🆕 Open-source LLMOps platform combining a prompt playground, prompt management, evaluation runs, and observability in one UI. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagenta-ai%2Fagenta&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vellum AI](https://www.vellum.ai/) - Production-grade agent IDE with prompt building, evaluations, versioning, and observability — closed-source SaaS.
- [Coze Loop](https://github.com/coze-dev/coze-loop) - 🆕 🇨🇳 ByteDance's open-source agent optimization platform: full-lifecycle development, debugging, evaluation, and monitoring. Apache-2.0. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-loop&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Restack](https://www.restack.io/) - Durable agent runtime + visual workflow editor (built on Temporal-style replay). Open-source examples in [restackio/examples-python](https://github.com/restackio/examples-python).
- [Bisheng](https://github.com/dataelement/bisheng) - 🇨🇳 Open enterprise LLM DevOps platform: workflow editor, RAG, agent orchestration, fine-tuning, dataset management, observability. Apache-2.0. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdataelement%2Fbisheng&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [n8n](https://github.com/n8n-io/n8n) - General-purpose visual workflow automation that has become a popular agent canvas — 400+ integrations + native AI nodes. Fair-code license. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fn8n-io%2Fn8n&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Mastra](https://github.com/mastra-ai/mastra) - 🆕 Opinionated TypeScript agent framework with RAG, observability, MCP, and visual workflow builder; 21K+ stars. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmastra-ai%2Fmastra&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [VoltAgent](https://github.com/VoltAgent/voltagent) - 🆕 End-to-end TypeScript AI Agent Engineering Platform with memory, RAG, guardrails, MCP, voice, and workflow capabilities. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FVoltAgent%2Fvoltagent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Coze Studio](https://github.com/coze-dev/coze-studio) - 🆕 🇨🇳 Open-source agent IDE / visual builder from ByteDance's Coze team. Drag-and-drop workflows, plugin marketplace, debugging panel, multi-LLM provider support. Apache-2.0. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🧠 Agent Memory

*Systems for giving agents persistent memory and context management.*

- [Letta (MemGPT)](https://github.com/letta-ai/letta) - Create LLM services with long-term memory and custom tools. **July 2026**: goes beyond a passive memory layer — provides a **stateful agent runtime** where the agent has active control over its own memory, deciding what to store and forget. Supports multi-tenant apps and long-running sessions without context-window resets. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fletta-ai%2Fletta&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MemoryLake](https://memorylake.ai) - 🆕 **July 2026**. "Memory passport for agents" — platform-neutral memory layer shared across different agents and tools. Stores scoped memories (user / agent / session) and surfaces them via a universal API so an agent on one platform can recall context from another.
- [Supermemory](https://github.com/supermemoryai/supermemory) - 🆕 Context graph built from diverse data sources (web, docs, chats) to inform agent conversations. API-first, integrates with MCP and major frameworks. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsupermemoryai%2Fsupermemory&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Graphlit](https://www.graphlit.com/) - 🆕 Context platform for production agents: ingestion, entity extraction, and knowledge graph for search + RAG. Exposes MCP server for Claude / Cursor / Copilot integration.
- [Mem0](https://github.com/mem0ai/mem0) - The Memory layer for your AI apps — self-improving memory for LLM applications. **April 2026 algorithm upgrade**: single-pass add-only extraction, entity linking, multi-signal retrieval; benchmark wins on LoCoMo, LongMemEval, BEAM. 60K+ stars, 21+ official framework integrations. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmem0ai%2Fmem0&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Remio](https://remio.ai/) - 🆕 Local-first AI memory and knowledge base desktop app (Windows/Mac) for personal context. Parses files, webpages, recordings, emails, messages, and images into local indexes and vectors, so agents can retrieve focused context instead of repeatedly grepping directories or loading whole documents into prompts. Local-first + BYOK.
- [Zep](https://github.com/getzep/zep) - Long-term memory for AI assistants and agents. Note: open-source Community Edition deprecated — repo now hosts Zep Cloud SDKs/examples; see [Graphiti](https://github.com/getzep/graphiti) for Zep's active OSS. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgetzep%2Fzep&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [agent-memory](https://github.com/Zijian-Ni/agent-memory) - ⚠️ **Unverified** (early-stage). Lightweight agent memory framework for persistent context across sessions. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fagent-memory&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Graphiti](https://github.com/getzep/graphiti) - 🆕 Zep's open-source temporal knowledge graph engine; every fact is timestamped so agents can reason about "when" as well as "what". ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgetzep%2Fgraphiti&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangMem](https://github.com/langchain-ai/langmem) - LangChain's long-term memory SDK for agents — semantic/episodic/procedural memory primitives that plug into LangGraph's persistence layer. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangmem&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Motorhead](https://github.com/getmetal/motorhead) - 💤 **Unmaintained** (deprecated by maintainers; last release 2023-12). Memory and context management server for LLMs. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgetmetal%2Fmotorhead&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ChromaDB](https://github.com/chroma-core/chroma) - AI-native open-source embedding database for memory-augmented agents. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fchroma-core%2Fchroma&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cognee](https://github.com/topoteretes/cognee) - Deterministic LLM outputs using graphs, LLMs, and vector retrieval. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftopoteretes%2Fcognee&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangGraph Memory](https://github.com/langchain-ai/langgraph) - 🆕 Built-in persistence and checkpointing for stateful agent workflows. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flanggraph&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude Managed Agents Memory](https://platform.claude.com/docs/en/release-notes/overview) - 🆕 **April 23, 2026** (public beta). Anthropic's persistent memory feature for Claude Managed Agents. Agents retain information across sessions by mounting read/write memory stores to a filesystem. Enables long-running agents to learn and adapt without resetting context.
- [OpenViking](https://github.com/volcengine/OpenViking) - 🆕 🇨🇳 ByteDance Volcengine's open-source context database for AI agents (such as OpenClaw). Manages memory + resources + skills through a file-system paradigm, enabling hierarchical context delivery and self-evolving agents. AGPL-3.0, 22K+ stars. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvolcengine%2FOpenViking&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ReMe](https://github.com/agentscope-ai/ReMe) - 🆕 🇨🇳 Memory management kit from Alibaba's AgentScope team — combined file-based + vector-based memory for agents, designed to tackle context-window limits and stateless sessions. Apache-2.0. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentscope-ai%2FReMe&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [taOSmd](https://github.com/jaylfc/taosmd) - 🆕 ⚠️ **Unverified.** Local-first agent memory that keeps every turn verbatim in an append-only, zero-loss archive and links each extracted fact to its source, so facts a verifier cannot support are demoted out of recall (served-hallucination measured at 0.04, then 0.00). Typed temporal knowledge graph with supersede, plus hybrid vector + BM25 retrieval; tuned for small local models, fully offline (runs on an 8 GB SBC or RK3588 NPU). Author-reported 97% Recall@5 on LongMemEval-S, reproducible per `docs/benchmarks.md`. MIT. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fjaylfc%2Ftaosmd&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hindsight](https://github.com/vectorize-io/hindsight) - 🆕 Agent memory that learns from experience — not just conversation history. Biomimetic data structure organizes facts about the world, agent experiences, and learned mental models; `retain`/`recall`/`reflect` primitives; ships with the Agent Memory Benchmark (AMB). MIT, 15K+ stars. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvectorize-io%2Fhindsight&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SimpleMem](https://github.com/aiming-lab/SimpleMem) - 🆕 Efficient lifelong memory for LLM agents — multimodal (text + image + audio + video), designed to beat token-limit constraints without fine-tuning. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Faiming-lab%2FSimpleMem&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agent Memory Techniques](https://github.com/NirDiamant/Agent_Memory_Techniques) - 🆕 30 runnable Jupyter notebooks covering conversation buffers, vector stores, knowledge graphs, episodic/semantic memory, MemGPT, Mem0, Letta, Zep, Graphiti, LoCoMo benchmarks — the practical reference for learning all major memory patterns. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNirDiamant%2FAgent_Memory_Techniques&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

## 🔌 Tool & API Integration

*Protocols and tools for connecting agents to external services and APIs.*

- [ZoomMate](https://news.zoom.com/zoom-launches-zoommate/) - 🆕 💰 **GA June 1, 2026**. Zoom's first-party AI teammate that turns meeting conversations into completed work — updates Salesforce records, creates Jira issues, and routes requests through Slack. $20/user/month.
- [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol/servers) - Open protocol for connecting AI models to external tools and data sources. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Fservers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [mcp-gateway](https://github.com/Zijian-Ni/mcp-gateway) - ⚠️ **Unverified** (early-stage). Gateway server for routing and managing MCP protocol connections. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fmcp-gateway&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Composio](https://github.com/ComposioHQ/composio) - Integration platform for AI agents — 1000+ toolkits with managed auth. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FComposioHQ%2Fcomposio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Toolhouse](https://toolhouse.ai/) - Cloud infrastructure for AI tool use — store, manage, and execute tools.
- [LangChain Tools](https://github.com/langchain-ai/langchain) - Extensive collection of tool integrations within the LangChain ecosystem. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Arcade AI](https://github.com/ArcadeAI/arcade-ai) - Tool calling platform for AI agents and assistants. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FArcadeAI%2Farcade-ai&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Browser Use](https://github.com/browser-use/browser-use) - Make websites accessible for AI agents with browser automation. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowser-use%2Fbrowser-use&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Firecrawl](https://github.com/firecrawl/firecrawl) - Turn websites into LLM-ready data. Crawl and convert any website for AI. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ffirecrawl%2Ffirecrawl&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Crawl4AI](https://github.com/unclecode/crawl4ai) - 🆕 Open-source LLM-friendly web crawler and scraper. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Funclecode%2Fcrawl4ai&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Stagehand](https://github.com/browserbase/stagehand) - 🆕 AI-powered browser automation framework by Browserbase. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowserbase%2Fstagehand&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentQL](https://www.agentql.com/) - 🆕 Query language for AI agents to interact with web pages semantically.
- [StackOne](https://www.stackone.com/) - 🆕 Unified API for AI agent integrations across HR, CRM, and ATS platforms.
- [AWS MCP Server](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/) - 🆕 **GA May 6, 2026**. AWS-managed MCP server giving coding agents secure, auditable access to any AWS API; sandboxed Python execution for multi-step ops; replaces "agent SOPs" with agent skills. First-party from AWS.
- [Google Workspace MCP Server](https://workspaceupdates.googleblog.com/2026/05/agent-tools-and-security-updates-for-workspace-developers.html) - 🆕 **Public developer preview, May 1, 2026**. Workspace-native MCP server exposing Gmail / Drive / Calendar / Chat / People to MCP clients, with admin-controlled OAuth scopes and audit trails.
- [iManage MCP Server](https://imanage.com/resources/resource-center/news/mcp-server-available-broader-ai-ecosystem/) - 🆕 **May 14, 2026**. Native MCP endpoint for the iManage knowledge-work platform — lets any AI client securely read/write iManage documents without custom integration. First major legal/professional-services SaaS to ship a public MCP server.
- [Power Platform Canvas Authoring MCP Server](https://www.microsoft.com/en-us/power-platform/blog/2026/05/14/whats-new-in-power-platform-may-2026-feature-update/) - 🆕 **May 14, 2026**. Microsoft Power Platform feature exposing Canvas Apps authoring as an MCP server; lets Copilot / Claude Code drive natural-language InfoPath → Canvas Apps migration.
- [Coinbase AgentKit](https://github.com/coinbase/agentkit) - 🆕 "Every AI Agent deserves a wallet." Coinbase's official SDK giving agents an EVM wallet for paying APIs, signing transactions, and trading on-chain across Base / Ethereum. Apache-2.0. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoinbase%2Fagentkit&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Bifrost (Maxim AI)](https://github.com/maximhq/bifrost) - 🆕 Open-source enterprise AI gateway (Apache-2.0) — 1000+ models, adaptive load balancer, cluster mode, guardrails, OAuth 2.0 with PKCE, prompt-injection defense at the gateway layer; ~<100µs overhead at 5k RPS. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmaximhq%2Fbifrost&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Anthropic Creative Tool Connectors](https://www.anthropic.com/news/claude-for-creative-work) - 🆕 **April 28, 2026**. Nine MCP-based Claude connectors for creative software: Adobe (50+ tools across Creative Cloud — Photoshop, Premiere, Express), Blender, Autodesk Fusion, Ableton, Splice, Affinity by Canva, SketchUp, and Resolume. Built on the MCP open standard so other LLM clients can use them too.
- [The Colony](https://thecolony.cc) - ⚠️ **Unverified.** Self-described public agent-first social network with REST API for agent posts/votes/DMs and SDKs in Python ([colony-sdk-python](https://github.com/TheColonyCC/colony-sdk-python)), TypeScript ([colony-sdk-js](https://github.com/TheColonyCC/colony-sdk-js)) and Go ([colony-sdk-go](https://github.com/TheColonyCC/colony-sdk-go)). Organisation and SDK repos are <30 days old, all 0–2 stars, single-maintainer; same submission was sent to 15+ awesome lists in parallel — listed for visibility, evaluate before depending on it. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTheColonyCC%2Fcolony-sdk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [dependency-freshness-mcp](https://github.com/Armigerous/dependency-freshness-mcp) - 🆕 ⚠️ **Unverified.** MCP server giving AI coding agents fresh, cited npm & PyPI facts — latest version, release dates, deprecations, and dated breaking-change diffs — to close the training-cutoff blind spot. Remote (Apify Standby HTTP) + local stdio. New single-maintainer repo (created 2026-06-08, 0 stars at listing) — listed for visibility, evaluate before depending on it. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FArmigerous%2Fdependency-freshness-mcp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [NotFair](https://github.com/nowork-studio/NotFair) - Open-source Claude Code agent skills for [SEO](https://github.com/nowork-studio/NotFair/tree/main/seo), [Google Ads](https://github.com/nowork-studio/NotFair/tree/main/google-ads), and [Meta Ads](https://github.com/nowork-studio/NotFair/tree/main/meta-ads); connects to live campaign and analytics data via Google Ads MCP, Meta Ads MCP, Google Search Console MCP, and Google Analytics (GA4) MCP. MIT. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fnowork-studio%2FNotFair&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [mcp-agent](https://github.com/lastmile-ai/mcp-agent) - 🆕 Open-source Python framework designed with Model Context Protocol (MCP) as its core communication primitive for building agents natively interoperable with the MCP tool ecosystem. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flastmile-ai%2Fmcp-agent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

## 🧪 Agent Sandboxing & Compute Isolation

*Secure runtimes that let agents execute generated code and shell commands without compromising the host. Critical infrastructure once you let an agent off the leash.*

- [E2B](https://github.com/e2b-dev/E2B) - Open-source secure cloud sandbox for AI-generated code. Used as the execution layer in OpenAI Agents SDK and many production agents. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fe2b-dev%2FE2B&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Daytona](https://github.com/daytonaio/daytona) - 🆕 Secure, elastic infrastructure for running AI-generated code. Spin up isolated dev environments per agent task; AGPL-3.0. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdaytonaio%2Fdaytona&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Modal](https://modal.com/) - Serverless cloud platform popular for agent compute, GPU jobs, and sandboxed Python — `modal-client` is the official SDK. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodal-labs%2Fmodal-client&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsandbox](https://github.com/superradcompany/microsandbox) - 🆕 Local, programmable microVM sandboxes for AI agents — secure code execution on your own machine, no cloud dependency. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsuperradcompany%2Fmicrosandbox&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SandboxFusion](https://github.com/bytedance/SandboxFusion) - ByteDance's multi-language code-execution sandbox built for agent / model evaluation pipelines. Apache-2.0. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbytedance%2FSandboxFusion&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Northflank](https://northflank.com/) - General-purpose container PaaS used as an agent runtime backend (per-task ephemeral environments, GPU pools).
- [Firecracker](https://github.com/firecracker-microvm/firecracker) - The microVM kernel underneath E2B, Daytona and most agent sandboxes. Useful as a primitive when building your own. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ffirecracker-microvm%2Ffirecracker&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangSmith Sandboxes](https://www.langchain.com/blog/interrupt-2026-overview) - 🆕 **May 2026 (Interrupt 2026)**. Hosted secure code execution environments for agents — filesystem, shell, package manager, persistent state, and network boundary. Part of LangChain's Interrupt 2026 release alongside LangSmith Engine and Managed Deep Agents.
- [Google Antigravity Sandbox](https://antigravity.google/changelog) - 🆕 **May 2026 (Google I/O)**. Sandboxed Linux environments for agent-executed code; ships as part of Antigravity 2.0's stack — sub-agents run in isolated containers with scoped filesystem + network access.

---

## 🛡️ Agent Security

*Tools and frameworks for securing AI agents against prompt injection, data leaks, and misuse.*

- [AgentGate](https://github.com/ElamOlame31/agentgate-public) - 🆕 ⚠️ **Unverified** (early-stage, single maintainer). Pre-execution authorization PDP for autonomous AI agents. Scores trust across 4 dimensions per request, detects 24h kill-chain patterns, Merkle-chained audit trail. MIT license, drop-in with LangGraph, LangChain, and AutoGen. [tryagentgate.com](https://www.tryagentgate.com/) ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FElamOlame31%2Fagentgate-public&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [prompt-firewall](https://github.com/Zijian-Ni/prompt-firewall) - ⚠️ **Unverified** (early-stage). Firewall for LLM prompts — detect and block prompt injection attacks. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fprompt-firewall&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LLM Guard](https://github.com/protectai/llm-guard) - The Security Toolkit for LLM Interactions — input/output scanners for AI. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fprotectai%2Fllm-guard&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Rebuff](https://github.com/protectai/rebuff) - 📦 **Archived** (2025-05). Self-hardening prompt injection detector — detect, deflect, and report. Listed for historical reference; no longer maintained. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fprotectai%2Frebuff&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Guardrails AI](https://github.com/guardrails-ai/guardrails) - Adding guardrails to large language models — validate and correct LLM outputs. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fguardrails-ai%2Fguardrails&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) - Toolkit for adding programmable guardrails to LLM-based conversational systems. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNVIDIA%2FNeMo-Guardrails&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vigil](https://github.com/deadbits/vigil-llm) - 💤 **Stale** (no commits since 2024-01). LLM security scanner — detect prompt injections, jailbreaks, and data leakage. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeadbits%2Fvigil-llm&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Lakera Guard](https://www.lakera.ai/) - Enterprise-grade AI security platform for prompt injection defense.
- [Garak](https://github.com/NVIDIA/garak) - LLM vulnerability scanner by NVIDIA — probe for weaknesses in language models. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNVIDIA%2Fgarak&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Invariant Guardrails](https://github.com/invariantlabs-ai/invariant) - 🆕 Runtime guardrails for AI agents — policy enforcement and safety checks. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Finvariantlabs-ai%2Finvariant&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Prompt Armor](https://promptarmor.com/) - 🆕 Enterprise prompt injection protection with real-time detection.
- [Descope MCP Auth](https://www.descope.com/) - 🆕 Authentication and authorization layer for MCP server security.
- [AgentDojo](https://github.com/ethz-spylab/agentdojo) - 🆕 ETH Zürich research benchmark for evaluating prompt-injection attacks and defenses against tool-using LLM agents. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fethz-spylab%2Fagentdojo&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ModelScan](https://github.com/protectai/modelscan) - Scan ML model files (Pickle, PyTorch, TF) for serialization-based code-execution attacks. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fprotectai%2Fmodelscan&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [PyRIT](https://github.com/microsoft/PyRIT) - Microsoft's Python Risk Identification Tool for generative AI — automated red-teaming framework (moved from Azure/PyRIT, March 2026; actively maintained). Complements RAMPART below. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2FPyRIT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAMPART](https://github.com/microsoft/RAMPART) - 🆕 **May 20, 2026**. Microsoft's pytest-native safety + security testing framework for agentic AI. Developer-facing white-box counterpart to PyRIT — cross-prompt-injection probes, benign-failure asserts, harm-category coverage, statistical thresholds (e.g. safe in 80%+ runs). Integrates straight into CI/CD. MIT. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2FRAMPART&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Clarity (Microsoft)](https://www.microsoft.com/en-us/security/blog/2026/05/20/introducing-rampart-and-clarity-open-source-tools-to-bring-safety-into-agent-development-workflow/) - 🆕 **May 20, 2026**. Companion to RAMPART. Structured design-review tool for AI agents — "living artifacts" documenting intent, risks, and behavior before code is written. Open-sourced from Microsoft AI Red Team's internal practice.
- [Nobulex](https://github.com/arian-gogani/nobulex) - ⚠️ **Unverified.** Cryptographic receipts for AI agent actions (Ed25519 dual signatures, hash-chained audit logs). MIT. Bilateral-receipt primitive [merged](https://github.com/microsoft/agent-governance-toolkit/pull/1333) into Microsoft's Agent Governance Toolkit (PRs #1302, #1333). Same submission sent to 15+ awesome lists in parallel; submitter's claim of "4,500 npm downloads" doesn't match registry data (`@nobulex/mcp-server` ~19/month at audit time). Listed for visibility on the strength of the Microsoft adoption. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Farian-gogani%2Fnobulex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MCP Gateway & Registry](https://github.com/agentic-community/mcp-gateway-registry) - 🆕 Enterprise-ready MCP gateway and registry that centralises AI development tools with OAuth authentication, dynamic tool discovery, audit trails, and Keycloak / Entra integration. Apache-2.0. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentic-community%2Fmcp-gateway-registry&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ActPlane](https://github.com/eunomia-bpf/ActPlane) - 🧪 OS-level agent harness enforcing behavioral contracts defined in YAML via eBPF at the syscall boundary — constraints hold across any tool, subprocess, or direct syscall, with corrective feedback to the agent on violation. MIT. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Feunomia-bpf%2FActPlane&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [WalletPrint](https://github.com/Loai17/walletprint-sdk) - ⚠️ **Unverified** (early-stage). Open-source SDK for behavioral risk scoring of agent wallets that flags anomalies before transactions are signed using wallet behavioral history, with integrations for ZeroDev and LangChain. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FLoai17%2Fwalletprint-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Alchemy & Visa AgentCard](https://www.coindesk.com/business/2026/06/18/alchemy-s-ai-driven-identity-and-payment-service-gains-access-to-visa-network) - 🆕 **June 18, 2026**. Payments + identity stack for AI agents built on **Visa Intelligent Commerce**. One API provisions everything an agent needs to transact — a Visa payment token, a dedicated email and phone number, and a crypto wallet — so it can buy on a consumer's behalf with scoped controls. Defaults to Visa-issued tokens; also supports crypto, x402, and Stripe's Machine Payments Protocol. Model-agnostic (OpenAI / Anthropic / etc.).
- [Microsoft Prompt Shields](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection) - Azure AI Content Safety feature detecting jailbreaks and indirect prompt injection hidden in documents/web pages an agent consumes (GA 2024; since extended for agent workloads). Integrates with Azure OpenAI Service and third-party models.
- [Agent Name Service (ANS)](https://www.ciodive.com/news/linux-foundation-prepares-open-standard-ai-agent-verification/823691/) - 🆕 **June 2026**. Linux Foundation initiative to establish an open standard for AI agent verification and trusted identity. Decentralized agent name registry so agents can verify they are communicating with legitimate counterparts, mitigating impersonation and MITM attacks.
- [OpenAI Daybreak](https://openai.com/index/daybreak-securing-the-world/) - 🆕 **June 2026**. OpenAI initiative + updated Codex Security plugin for automated vulnerability discovery and remediation in AI-adjacent code; includes prompt-injection hardening for agentic applications.
- [JADEPUFFER (Sysdig disclosure)](https://hackread.com/sysdig-jadepuffer-first-agentic-ransomware-operation/) - 🆕 ⚠️ **Threat, not a tool — July 2, 2026**. Sysdig documents the first fully agent-orchestrated ransomware operation: an LLM-driven agent exploited a Langflow RCE (CVE-2025-3248), harvested credentials, pivoted to a production MySQL/Nacos server, self-corrected a failed step in 31 seconds, then encrypted 1,342 config items with an ephemeral (never-saved) AES key, making the ransom demand unpayable-but-unrecoverable. Payloads were "self-narrating" with natural-language reasoning comments — strong evidence of LLM authorship. Cited here as the reference case for why agent-security tooling (guardrails, egress control, credential scoping) above matters in production.
- [Lineation.ai](https://lineation.ai) - 🆕 ⚠️ **July 2026** (new vendor). Agent accountability layer — observability, governance, and defense with forensic reasoning lineage. Aims to prevent goal hijacking, memory poisoning, and tool misuse; audit trail for SOC 2 / HIPAA / EU AI Act compliance. Cloud (free-to-start) and on-prem.
- [First Recon AI Security Runtime](https://firstrecon.ai) - 🆕 **July 2026**. Enterprise AI governance platform that inspects every AI interaction (human-to-model, agent-to-tool, agent-to-agent) with a proprietary Semantic Security Engine — applies policies before data reaches a model and captures a full decision audit trail. macOS + Windows endpoint agent for governing AI use on device.
- [CrowdStrike Falcon AIDR](https://www.crowdstrike.com/en-us/platform/falcon-aidr-ai-detection-and-response/) - **GA December 2025**. AI Detection and Response — visibility into employee AI use and agent activity across an enterprise, risk scoring, behavioral anomaly detection, prompt-injection blocking, and real-time policy enforcement at the AI interaction layer.
- [Exabeam Agent Behavior Analytics](https://www.exabeam.com/) - 🆕 **2026**. Extension of Exabeam's behavior-intelligence platform to cover agentic AI risks — continuous verify-observe-analyze-improve loops instead of static guardrails.

## 🔍 RAG & Knowledge

*Retrieval-augmented generation and knowledge management systems for agents.*

- [Oracle OCI Enterprise AI updates](https://blogs.oracle.com/ai-and-datascience/whats-new-in-ai-june-2026) - 🆕 **June 2026**. Enterprise deployment of Cohere Rerank 4 to enhance RAG and agentic enterprise search, plus expanded support for new Alibaba/Google models.
- [LlamaIndex](https://github.com/run-llama/llama_index) - Data framework for LLM-based applications — ingest, structure, and access private data. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Frun-llama%2Fllama_index&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Haystack](https://github.com/deepset-ai/haystack) - End-to-end LLM framework for building RAG pipelines and search systems. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeepset-ai%2Fhaystack&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Unstructured](https://github.com/Unstructured-IO/unstructured) - Open-source components for pre-processing documents for LLMs and RAG. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FUnstructured-IO%2Funstructured&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Chroma](https://github.com/chroma-core/chroma) - AI-native open-source embedding database. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fchroma-core%2Fchroma&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Weaviate](https://github.com/weaviate/weaviate) - Open-source vector database for AI-native applications. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fweaviate%2Fweaviate&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Qdrant](https://github.com/qdrant/qdrant) - High-performance vector similarity search engine and database. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fqdrant%2Fqdrant&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Pinecone](https://www.pinecone.io/) - Managed vector database for high-performance AI applications.
- [Milvus](https://github.com/milvus-io/milvus) - Cloud-native vector database for scalable similarity search. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmilvus-io%2Fmilvus&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAGFlow](https://github.com/infiniflow/ragflow) - Open-source RAG engine based on deep document understanding. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Finfiniflow%2Fragflow&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Docling](https://github.com/docling-project/docling) - Document parsing and conversion for RAG and generative AI. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdocling-project%2Fdocling&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Kotaemon](https://github.com/Cinnamon/kotaemon) - 🆕 Open-source RAG-based tool for chatting with documents. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FCinnamon%2Fkotaemon&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LightRAG](https://github.com/HKUDS/LightRAG) - 🆕 Simple and fast RAG engine with graph-based knowledge indexing. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2FLightRAG&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [R2R](https://github.com/SciPhi-AI/R2R) - 🆕 Production-ready RAG engine with built-in auth, observability, and ingestion. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSciPhi-AI%2FR2R&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vanna](https://github.com/vanna-ai/vanna) - 📦 **Archived** (2026-03). RAG for SQL — chat with your database using natural language. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvanna-ai%2Fvanna&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Morphik](https://github.com/morphik-org/morphik-core) - 🆕 Multimodal RAG engine for documents containing tables, figures, and charts; rapidly-rising 2026 alternative to LlamaIndex for complex PDFs. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmorphik-org%2Fmorphik-core&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cognee](https://github.com/topoteretes/cognee) - 🆕 Memory + reasoning engine that builds a knowledge graph as agents ingest documents; 2026 darling for "long-running research agent" stacks. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftopoteretes%2Fcognee&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAG-Anything](https://github.com/HKUDS/RAG-Anything) - 🆕 All-in-one multimodal RAG framework from HKU Data Science Lab. Built on top of LightRAG; concurrent pipelines for parallel text + multimodal processing; queries documents that interleave text, diagrams, tables, and formulae. MIT, 21K+ stars. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2FRAG-Anything&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [A-MEM](https://github.com/WujiangXu/A-mem-sys) - 🆕 Agentic Memory system for LLM agents — dynamic organization of memories using Zettelkasten-inspired note linking; enables more flexible retrieval than static vector stores. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FWujiangXu%2FA-mem-sys&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

## 💻 Coding Agents

*AI-powered coding assistants and autonomous software engineering agents.*

### Terminal & CLI Agents

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - Anthropic's agentic coding tool. 80.9% SWE-bench score, handles complex multi-file bugs. May 2026 (v2.1.128–2.1.141): new `/goal` command for cross-turn completion conditions, agent view, plugin loading from `.zip` archives + URLs, `Ctrl+R` global history search, broader MCP/hook handling, enterprise feedback surveys.
- [Codex CLI](https://github.com/openai/codex) - OpenAI's open-source terminal coding agent (Rust, Apache-2.0, 82K+ stars). 77.3% Terminal-Bench score. May 2026 adds **Codex Chrome extension** for in-browser DevTools workflows, `codex remote-control` headless app-server, plugin-detail bundled-hook display, and **Codex on Mobile** preview (May 14) that lets ChatGPT iOS/Android remote-control the macOS Codex app. **July 9–10, 2026**: Codex integrated into the **ChatGPT desktop app** (macOS/Windows) — the standalone CLI continues with frequent point releases (v0.144.x, mid-July); Multi-Agent V2 runtime work landed in June CLI releases, and the desktop launch added a beta multi-agent feature with GPT-5.6. **Codex Micro** ($230 keypad for Codex control) announced July 15. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fcodex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Codex Security](https://developers.openai.com/codex/changelog) - 🆕 **March 2026**. Application-security agent that finds and fixes software vulnerabilities; available to OSS maintainers via the Codex-for-OSS program.
- [Aider](https://github.com/Aider-AI/aider) - 💤 AI pair programming in your terminal — works with any LLM, with first-class git commit handling. Last release Aug 2025. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAider-AI%2Faider&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Goose](https://github.com/block/goose) - Open-source agentic coding CLI from Block — extensible, MCP-native, works with any LLM. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fblock%2Fgoose&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) - 🆕 Google's terminal-first coding agent for large-context refactors. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle-gemini%2Fgemini-cli&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenCode](https://github.com/anomalyco/opencode) - Open-source terminal AI coding agent (opencode.ai, 180K+ stars) — build/plan agents, LSP, MCP, desktop app in beta; unrelated to the archived opencode-ai/opencode. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fanomalyco%2Fopencode&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Crush](https://github.com/charmbracelet/crush) - Terminal AI coding agent from Charm — successor to the archived opencode-ai/opencode; multi-model, LSP + MCP support. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcharmbracelet%2Fcrush&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Grok Build](https://x.ai/news/grok-build-cli) - 🆕 **May 25, 2026** (early beta). xAI's agentic CLI coding agent powered by **grok-code-fast-1**. Parallel sub-agents in isolated environments, daily release notes; available to SuperGrok and X Premium Plus subscribers. xAI's reply to Claude Code and Codex CLI. ⚠️ July 2026 reports found Grok Build uploading entire git repos to xAI storage — review before use on private code.
- [Antigravity CLI](https://antigravity.google/blog/introducing-google-antigravity-2-0) - 🆕 **May 19, 2026** (Google I/O 2026). Lightweight CLI companion to Antigravity 2.0 — create and interact with Google agent harnesses directly from the terminal. macOS / Linux / Windows. Reported to replace Gemini CLI for hosted-plan users from June 18, 2026 (the open-source gemini-cli repo remains active, 105K+ stars).
- [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code) - 🆕 🇨🇳 **June 6, 2026**. Moonshot AI's terminal coding agent (TypeScript, MIT). Built-in coder / explore / plan sub-agents in isolated contexts, conversational MCP setup via `/mcp-config`, npm install. Aimed squarely at next-gen Kimi K2.6 agents. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FMoonshotAI%2Fkimi-code&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MAI-Code-1-Flash in GitHub Copilot](https://microsoft.ai/news/introducingmai-code-1-flash/) - 🆕 **Build 2026 (June 2, 2026)**. Microsoft's first fully in-house 5B coding model lands as a model picker option in GitHub Copilot — outperforms Claude Haiku 4.5 on four core coding benchmarks (SWE-Bench Pro 51.2% vs 35.2%) at significantly lower cost.
- [Claude Agent SDK](https://docs.anthropic.com/en/docs/claude-code/sdk) - SDK for building agents on the Claude Code harness (rebranded from Claude Code SDK in late September 2025). **June 2026** Claude Code releases add hierarchical subagent spawning, Dynamic Workflows (fan out tens–hundreds of parallel subagents), rubric-driven Outcomes, and fallback model chains — powering the "ultracode" mode enabling up to 1,000 subagents per execution. Python + TypeScript.
- [ai-delivery-spec](https://github.com/franklinxkk/ai-delivery-spec) - 🆕 ⚠️ **Unverified.** Spec-driven delivery framework for PMs working with AI coding agents (Claude Code, OpenClaw, Codex, Cursor, Copilot). 4 delivery tiers (Lite/Standard/L2/Full), 0D triage routing, prototype testability rules, AI runtime governance, 5 domain modules. SKILL.md convention; hosted on ClawHub. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ffranklinxkk%2Fai-delivery-spec&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Ralph Harness](https://github.com/rxdt/py_ralph_frame) - 🆕 ⚠️ **Unverified.** Tiny Python scaffold for guarded Claude Code/Codex/Gemini loops with repo-local specs, fresh-context iterations, git-hook gate, CI verification, and coverage gates. Installable via `uvx ralph-harness demo`. MIT. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Frxdt%2Fpy_ralph_frame&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### IDE-Based Agents

- [Cursor 3.11](https://cursor.com/changelog) - 🆕 **July 10, 2026**. Side Chats (parallel AI conversations without disrupting main workflow), conversation history search, redesigned project/repo pickers, new Cloud Agent Hooks (granular control + observability over agent conversations — prompts, responses, sub-agent activities).
- [Cursor 3.4 (Teams + PR review)](https://cursor.com/changelog) - 🆕 **May 11–13, 2026**. Microsoft Teams integration (`@Cursor` in Teams delegates to cloud agents), faster parallel-agent plan execution, multi-repo / Dockerfile-based dev-environment configs for agents, `/multitask` async sub-agents, Vulnerability Scanner, granular per-model access controls.
- [Cursor 3.3](https://cursor.com/changelog) - 🆕 **May 2026**. PR-review experience, parallel agents, enterprise model controls; previous 3.1 in April.
- [Cursor SDK](https://cursor.com/blog/typescript-sdk) - 🆕 **April 29, 2026** (public beta). TypeScript SDK exposing Cursor's runtime, harness, and models so developers can build programmatic agents on top of the Cursor stack — sandboxed cloud VMs, subagents, hooks, token-based pricing.
- [Kilo Code](https://kilo.ai/) - Open-source AI coding extension (VS Code / JetBrains) with Auto Model routing across 500+ models; acquired by Anaconda (2026). MiniMax models heavily featured.
- [Cursor](https://www.cursor.com/) - The AI code editor with Feb 2026 update supporting up to 8 parallel agents.
- [Windsurf → Devin Desktop](https://devin.ai/blog/windsurf-is-now-devin-desktop/) - 🆕 **Rebranded June 2, 2026**. Cognition renamed the Windsurf IDE to **Devin Desktop** (windsurf.com now redirects to devin.ai): **Devin Local** (Rust rewrite, ~30% more token-efficient, subagent support) replaces Cascade, an **Agent Command Center** Kanban becomes the default surface, and it ships open **Agent Client Protocol (ACP)** support. Cascade reaches end-of-life July 1, 2026.
- [Cline](https://github.com/cline/cline) - Autonomous coding agent in your IDE — VS Code extension. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcline%2Fcline&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Roo Code → Roomote](https://roomote.dev/) - ⚠️ **Discontinued as an IDE extension.** Roo Code announced (April 22, 2026) shutdown of its VS Code extension, Cloud, and Router on May 15, 2026, pivoting to **Roomote**, a cloud coding agent (Slack/GitHub/Linear → PRs); roocode.com now redirects to roomote.dev.
- [Void](https://github.com/voideditor/void) - 💤 **Paused** (not archived — maintainers exploring new coding ideas; no active maintenance). Fork of VS Code positioned as the open-source Cursor alternative; data stays with you, BYO model. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvoideditor%2Fvoid&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Continue](https://github.com/continuedev/continue) - Open-source AI code assistant for VS Code and JetBrains. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcontinuedev%2Fcontinue&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [GitHub Copilot](https://github.com/features/copilot) - Agent mode with expanded model access and `gh copilot` shell integration in early 2026. **July 2026 updates**: `/security-review` command (public preview) for AI-driven vulnerability scanning of in-progress changes; expanded "long-distance next edit suggestions" across full active file; C++ modernization agent GA in Visual Studio; refreshed Copilot Usage window for real-time billing tracking.
- [Kiro](https://kiro.dev/) - AWS autonomous agent. Spec-driven development, manages up to 10 simultaneous tasks.
- [Amazon Q Developer](https://aws.amazon.com/q/developer/) - AI coding companion deeply integrated with AWS ecosystem.
- [Visual Studio 2026 Agent Mode + Skills](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/) - 🆕 **VS 2026 Insiders May 12-15, 2026**. Copilot Chat "Agent Mode" now ships a guided Skills workflow inside Visual Studio 2026: discover, manage, and author reusable Copilot Skills with whole-solution context, plus terminal command execution and tool invocation.
- [JetBrains Rider AI Test-Writing Skill](https://blog.jetbrains.com/dotnet/2026/05/22/claude-codex-ai-agent-skill-for-writing-tests/) - 🆕 **May 22, 2026**. New AI Assistant skill for JetBrains Rider that surfaces .NET coverage data to Claude Code / Codex so agents target untested branches, reducing AI cost for test generation.

### Autonomous Software Engineers

- [Cursor 3.4 Cloud Agent Environments](https://cursor.com/changelog) - 🆕 **May 13, 2026**. New dev environments for cloud agents: multi-repo workspaces, Dockerfile-based config with build secrets, 70% faster cached image layers, per-environment version history with rollback, audit logs, scoped egress and secrets. Companion to the Cursor 3.4 release.
- [Devin Security Swarm](https://cognition.com/blog) - 🆕 **July 1, 2026**. Cognition's parallel-agent security product: finds vulnerabilities across a codebase, validates exploitability at runtime, and opens remediation PRs; found 36/50 real-world vulns at ~30% lower cost per finding than the next-best tool.
- [Devin 2.2](https://cognition.com/blog/introducing-devin-2-2) - 🆕 **February 24, 2026**. End-to-end testing with computer use (Linux desktop + screen recordings), self-review/auto-fix before PR, 3× faster startup. Cognition's flagship autonomous software engineer (Devin 2.x line; Core plan from $20/mo since Devin 2.0).
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) - Open-source platform for AI software developers as autonomous agents. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAll-Hands-AI%2FOpenHands&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SWE-agent](https://github.com/SWE-agent/SWE-agent) - Turn LLMs into software engineering agents that fix real GitHub issues. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSWE-agent%2FSWE-agent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Devika](https://github.com/stitionai/devika) - 💤 **Stale** (no commits since 2025-09). Agentic AI software engineer — open-source alternative to Devin. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstitionai%2Fdevika&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [GPT Engineer](https://github.com/gpt-engineer-org/gpt-engineer) - 📦 **Archived** (2026-04). Specify what you want built, AI asks for clarification, then builds it. Foundational project of the autonomous-coding era, kept for historical reference. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgpt-engineer-org%2Fgpt-engineer&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Codegen](https://github.com/codegen-sh/codegen) - 💤 Programmatic code manipulation and multi-file refactoring SDK (last release Sep 2025). ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcodegen-sh%2Fcodegen&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Qodo](https://www.qodo.ai/) - 🆕 AI Code Review Platform focused on quality, security, and test generation.
- [Google Antigravity 2.0](https://antigravity.google/blog/introducing-google-antigravity-2-0) - 🆕 **May 19, 2026** (Google I/O 2026). Standalone desktop application (macOS / Linux / Windows) for orchestrating multiple agents in parallel. Adds scheduled cron-style runs, async long-running tasks, dynamic sub-agents, and integrations with AI Studio / Android / Firebase. Companion **Antigravity SDK** lets you host the harness on your own infra; enterprise edition lands inside Gemini Enterprise Agent Platform.

---

## 🤖 Physical AI & Embodied Agents

*AI systems that perceive, reason about, and act in the physical world — humanoid robots, factory automation, Physical AI infrastructure. The next wave after language agents.*

### Foundational Models & Research
- [Microsoft physical-ai-toolchain](https://github.com/microsoft/physical-ai-toolchain) - 🆕 **June 2026**. Production-ready open-source toolchain integrating Microsoft Azure cloud services with NVIDIA's physical AI stack. Agentic workflows for data curation, training, and deployment of autonomous mobile robots and manipulators. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fphysical-ai-toolchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [PhyAgentOS](https://github.com/PhyAgentOS/PhyAgentOS) - 🆕 Self-evolving embodied AI operating system built on agentic workflows. Decouples cognitive functions from hardware for cross-platform robotic deployment with built-in auditability. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FPhyAgentOS%2FPhyAgentOS&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ENPIRE](https://research.nvidia.com/labs/gear/enpire/) - 🆕 **June 2026**. NVIDIA/CMU/UC Berkeley framework enabling AI agents to conduct their own robotics research — managing dual-arm robots, modifying algorithms, and training policies without human intervention.
- [Kairos](https://futureiot.tech/kairos-model-breaks-new-ground-for-open-source-embodied-intelligence/) - 🆕 **June 15, 2026**. ACE ROBOTICS open-sources its Kairos world model — first world-model approach to top VLA systems on RoboTwin 2.0, LIBERO-Plus, WorldModelBench Robot, and DreamGen; weights on GitHub / Hugging Face / ModelScope.
- [NVIDIA Cosmos 3](https://www.axios.com/2026/06/08/ai-news-nvidia-cosmos-3-openai-sites-solara-rtx-spark) - 🆕 **June 2026**. A foundation model explicitly trained on physics and spatial geometry rather than just text, targeting robotics, physical AI, and factory automation.

- [Google Gemini Robotics-ER 1.6](https://deepmind.google/blog/gemini-robotics-er-1-6/) - 🆕 April 14, 2026. Robotics AI model with enhanced spatial/embodied reasoning (incl. analog instrument reading), available via the Gemini API.
- [Project Prometheus (Bezos)](https://techcrunch.com/2026/06/11/jeff-bezoss-prometheus-raises-12b-to-build-an-artificial-general-engineer-for-the-physical-world/) - 🆕 💰 **June 11, 2026**. Jeff Bezos co-led Physical AI venture raised $12B at a $41B valuation to build an "artificial general engineer" for the physical world.
- [NVIDIA Isaac GR00T](https://developer.nvidia.com/isaac/gr00t) - NVIDIA's foundation model platform for humanoid robots. Unveiled at GTC, expanded at Hannover Messe 2026.
- [NVIDIA Industrial AI Cloud](https://nvidianews.nvidia.com/) - 🆕 April 2026 (Hannover Messe). Deutsche Telekom-built AI factory infrastructure for industrial AI workloads.

### Humanoid Robots

- [Tesla Optimus V3 (Production Start)](https://www.teslarati.com/tesla-optimus-awe-2026-shanghai/) - 🆕 **Production begins late July / August 2026** at Tesla Fremont, CA — first Optimus robots coming off an actual mass-production line. A second, larger assembly line is under construction in Texas targeting up to 10M units/year by 2027. V3 currently operates exclusively in Tesla factories (battery module handling, parts kitting); not yet available for public purchase. Evolved from Gen 2/Gen 3 platform — 37 joints, 1.2 m/s walking, 22-DoF hands.
- [Figure 03 (Helix AI)](https://blog.robozaps.com/b/figure-03-review) - 🆕 **Late 2025 announcement, ramping in 2026**. First Figure model designed for the home: soft textile coverings, wireless charging, tactile sensors. May 2026 demo: two F.03 robots autonomously cleaning a room and making a bed in <2 minutes via visual coordination only.
- [Figure 04](https://autonews.gasgoo.com/articles/news/figure-founder-f04-robot-initiates-component-delivery-process-2054560059634376705) - 🆕 **May 13, 2026**. Founder Brett Adcock announces Figure 04 design finalized; component deliveries underway. Successor to F.03 with the Helix VLA model.
- [Helix 02 package-sort 72h run](https://oodaloop.com/briefs/technology/figure-ais-humanoid-robots-sort-88000-packages-in-72-hours-during-nonstop-livestream/) - 🆕 **May 13-16, 2026**. Live-streamed Figure F.03 fleet runs Helix 02 fully autonomously on a package-sort line — ~22K packages on day one, then ~30K in the first 24 hours, ending in a stress test that hit **~88K packages over ~72 hours** before mechanical failure. First public continuous-run evidence for a home-form-factor humanoid stack.
- [Figure F.03 vs human 8-hour sort challenge](https://incrypted.com/en/figure-ai-held-a-human-vs-robot-marathon/) - 🆕 **May 18, 2026**. Figure runs the first public head-to-head: one F.03 robot vs one trained human, 8-hour shift on the same package-sort line. Human wins narrowly — 12,924 parcels (2.79 s/item) vs 12,732 parcels (2.83 s/item). Tightest published gap to human throughput on a real industrial task to date.
- [Boston Dynamics Atlas 100-lb manipulation + Hyundai 25K plan](https://www.techtimes.com/articles/316854/20260519/boston-dynamics-reveals-how-atlas-learned-lift-100-pound-loads-hyundai-plans-30000-per-year.htm) - 🆕 **May 18-19, 2026**. Boston Dynamics publishes video + technical blog showing Atlas lifting and carrying **>100 lb** loads (mini-fridge / washing machine) via RL + large-scale sim training; whole-body control adapts to weight shifts without per-object identification. Hyundai Motor Group commits to deploying **25,000+ Atlas units** across Hyundai/Kia plants starting 2028 in Georgia.
- [Hyundai completes full Boston Dynamics buyout](https://www.techtimes.com/articles/320483/20260714/boston-dynamics-now-fully-hyundais-atlas-exits-world-cup-eyes-factory-floor.htm) - 🆕 💰 **Late June 2026**. Hyundai Motor Group buys SoftBank's remaining 9.65% stake for $325M, taking 100% ownership at a ~$3.4B valuation. New 5th-gen Atlas made a public appearance at the FIFA World Cup (July 5, 2026); commercial availability to external customers planned 2027, Georgia Metaplant deployment 2028.
- [Unitree G1 deployed at JAL Haneda](https://www.techtimes.com/articles/316862/20260519/jal-deploys-unitree-g1-robots-haneda-us-congress-moves-blacklist-supplier-national-security.htm) - 🆕 **May 2026**. Japan Airlines starts a Haneda ground-operations trial with Unitree G1 humanoids (baggage loading, container transport, cabin cleaning) — marketed as the **first commercial airline trial of bipedal robots in active aviation service**. US Congress separately moves to add Unitree to the entity list on national-security grounds the same week, underscoring how fast the embodied-AI supply chain is becoming geopolitical.
- [Figure 02 + Helix 02](https://en.wikipedia.org/wiki/Figure_AI) - 🆕 **January 2026**. Helix 02 expands whole-body autonomy (load/unload dishwashers, fold laundry); BotQ facility rated for 12K units/year.
- [Unitree G1 + H2](https://community.robotshop.com/blog/show/unitree-robotics-at-ces-2026-a-clear-signal-of-whats-coming-next) - 🆕 **CES 2026**. G1 dance/boxing/skating demos, autonomous kung fu (February), and the 31+ DoF H2 humanoid.
- [Unitree R1 Air](https://humanoid.guide/unitrees-4900-r1-air-pushes-humanoids-toward-mass-market/) - 🆕 Consumer humanoid at **$4,900** — runs, flips, walks on hands.
- [Unitree Gen 2 (lifelike skin)](https://www.youtube.com/watch?v=Gmp82MuTFsM) - 🆕 Realistic human-like skin with embedded pressure / temperature / touch sensors.
- [Unitree GD01](https://www.extremetech.com/computing/unitree-will-sell-you-a-personal-mecha-robot-for-650000) - 🆕 **May 2026**. Nearly 10-foot manned mecha; pilot-driven, switches between bipedal and quadrupedal modes. Priced from ¥3.9M (~$650K). Tracks how the embodied-agent stack is starting to fork into operator-piloted form factors.
- [Honor (荣耀) Humanoid](https://www.npr.org/2026/04/20/g-s1-118086/humanoid-robot-half-marathon) - 🆕 **April 19, 2026**. Won the Beijing E-Town humanoid half-marathon in 50:26 — beating the human world record for the distance.
- [Zhiyuan (智元) AGIBOT](https://www.agibot.com/article/231/detail/62.html) - 🆕 🇨🇳 **April 17, 2026 (APC 2026)**. Declares 2026 "Deployment Year One"; 10,000th robot deployed, seven industry solutions, open-source AIMA architecture (Link-U OS, Genie Studio).
- [Unitree H-series](https://www.unitree.com/) - Boston Dynamics competitor from China. Ongoing 2026 iterations.
- [1X NEO (consumer humanoid)](https://www.1x.tech/discover/neo-home-robot) - 🆕 **Pre-orders opened Oct 28, 2025**, first US home deliveries in 2026. 5'6" / 66-lb home humanoid with 22-DoF hands, soft body, 4-hour runtime, on-device LLM, ~22dB noise. Early-access price $20,000 with $200 deposit, or $499/month subscription. Privacy "no-go" zones + face-blurring built in. First credible consumer-targeted humanoid to actually ship to homes.
- [Mitsubishi Motors × Highlanders humanoid MOU](https://www.mitsubishi-motors.com/en/newsroom/newsrelease/2026/20260709_1.html) - 🆕 **July 9, 2026**. Mitsubishi Motors signs an MOU with University of Tokyo startup Highlanders to co-develop and mass-produce humanoid robots (welding, logistics, engine assembly) at its Kyoto plant — reported target ~1,000 units/month, production from as early as 2027, addressing Japan's labor shortage.
- [Agile Robots](https://www.agile-robots.com/) - German-Chinese robotics company building AI-driven industrial manipulation systems.
- [Shenzhen Humanoid Pilot Line](https://www.chinadailyhk.com/hk/article/631892) - 🆕 🇨🇳 Shenzhen launched its first pilot production line for humanoid robots on **April 12, 2026** (Leju Robotics + Dongfang Precision in Longhua District). 2-hour assembly cycle, 500–1,000 units/year, with mass production moving to a 10,000-units/year Foshan facility.

### Consumer Robotics & Wearables

- [Doubao AI Glasses (ByteDance)](https://technode.com/2026/03/18/bytedance-reportedly-delays-doubao-ai-glasses-launch-plan/) - ⚠️ 🇨🇳 Gen 1 reportedly scrapped before launch ("too generic"); ByteDance fast-tracking a dual-model Gen 2 (July 2026) as the AI-glasses market grows ~130% YoY.
- [Nothing AI Glasses/Earbuds](https://techcrunch.com/2026/04/01/nothings-ai-devices-plan-reportedly-contains-smart-glasses-and-earbuds/) - 🧪 Reported March 2026: Nothing plans AI smart glasses + earbuds, targeting a 2027 launch.
- [Samsung Galaxy S26 (Gauss 2.3)](https://www.samsung.com/) - On-device agentic AI. Gauss 2.3 Think and Gauss O Flash variants.
- [Meta Ray-Ban Display / Ray-Ban Meta](https://www.meta.com/ai-glasses/) - Meta's shipping AI-glasses line (incl. the Display model with Neural Band); Ray-Ban Meta Gen 3 rumored for late 2026.

### Autonomous Driving

- [Tesla FSD v14](https://www.tesla.com/) - v14.3.x rolling out (July 2026), incl. a v14 "Lite" for legacy HW3 cars; unsupervised operation still limited to robotaxi programs.
- [Waymo](https://waymo.com/) - Continuing commercial L4 rollout in US cities through 2026.
- [WeRide / Pony.ai / Baidu Apollo](https://www.weride.ai/) - 🇨🇳 Chinese L4 fleets expanding operational zones.

---

## 🎮 Agent Simulation & World Models

*Research environments where agents are trained, observed, or stress-tested in simulated worlds. Increasingly relevant as world-model and embodied research bleeds into language-agent design.*

- [Generative Agents](https://github.com/joonspk-research/generative_agents) - 💤 Stanford's seminal *Smallville* simulacrum (Park et al., 2023). Memory + reflection + planning in a town of 25 LLM-driven characters. Reference implementation that influenced almost every multi-agent paper since. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fjoonspk-research%2Fgenerative_agents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Voyager](https://github.com/MineDojo/Voyager) - 💤 First lifelong-learning agent in Minecraft — GPT-4 with skill library and curriculum (Wang et al., 2023). Still the canonical open-ended agent benchmark. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FMineDojo%2FVoyager&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SWE-Gym](https://github.com/SWE-Gym/SWE-Gym) - Open environment to train SWE agents on real GitHub issues; companion to SWE-bench. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSWE-Gym%2FSWE-Gym&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [WebArena](https://webarena.dev/) - Realistic, reproducible web environment (Reddit / shopping / GitLab clones) used by OSWorld and most browser-agent papers. **[WebArena-Verified](https://github.com/ServiceNow/webarena-verified)** (ServiceNow, Dec 2025): all 812 tasks, reference answers, and evaluators manually reviewed; LLM-as-judge replaced with deterministic type-aware checks; 258-task "Hard" subset for cheaper evals.
- [WorkArena](https://github.com/ServiceNow/WorkArena) - ServiceNow's enterprise workplace benchmark for browser agents. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FServiceNow%2FWorkArena&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Genie 3](https://deepmind.google/models/genie/) - Google DeepMind's interactive video world model — playable 3D worlds from a prompt. Closed-weights research, no public code.
- [NVIDIA Cosmos](https://github.com/nvidia-cosmos/cosmos-predict2) - NVIDIA's foundation world model for embodied AI / robotics — generate physically plausible video futures. predict1 deprecated in favor of Cosmos-Predict2 (Predict 2.5 announced CES 2026); see also Cosmos 3 (June 2026) above. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fnvidia-cosmos%2Fcosmos-predict2&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Snowflake Agent World Model (AWM)](https://github.com/Snowflake-Labs/agent-world-model) - 🆕 **Open-sourced Feb 10, 2026; accepted to ICML 2026 May 1, 2026**. Synthetic environment generation pipeline that ships 1,000 executable SQL-backed tool-use environments (35K+ tools, 10K tasks) exposed via a unified MCP interface — enables large-scale multi-turn agentic RL. Infrastructure merged into `meta-pytorch/OpenEnv`. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSnowflake-Labs%2Fagent-world-model&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

- [Qwen-AgentWorld](https://github.com/QwenLM/Qwen-AgentWorld) - 🆕 **June 2026**. Native language world model designed to simulate agentic environments (web, OS, terminal) by predicting the next state of the environment rather than the agent's next action. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FQwenLM%2FQwen-AgentWorld&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SimWorld](https://github.com/SimWorld-AI/SimWorld) - 🆕 Open-ended, realistic simulator built on Unreal Engine 5 for testing autonomous AI agents in complex physical and social environments. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSimWorld-AI%2FSimWorld&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 📊 Benchmarks & Leaderboards

*Standard evaluation suites and live leaderboards tracking frontier AI capability as of 2026.*

- [BenchLM](https://benchlm.ai/) - 🆕 Composite leaderboard that aggregates multiple benchmark families. July 2026 top: Claude Fable 5 91, Claude Mythos 5 89, Gemini 3.1 Pro 88 (79 ranked / 281 tracked models, 296 benchmarks).
- [SWE-bench Verified](https://www.swebench.com/) - Real-world GitHub issue resolution benchmark. April 2026 top: Claude Mythos 93.9%, Claude Opus 4.7 87.6%. **July 2026 top**: Claude Mythos 5 leads at **95.5%**, Claude Fable 5 at **95.0%**.
- [GPQA Diamond](https://github.com/idavidrein/gpqa) - 💤 **Stale** dataset repo (last update 2024-09). Expert-level science reasoning. April 2026 top: Gemini 3.1 Pro 94.3% (world-record), Claude Opus 4.7 94.2%.
- [ARC-AGI 2](https://arcprize.org/) - Abstract reasoning over novel tasks. GPT-5.5 leads at 85% (July 2026); Gemini 3.1 Pro 77.1% (Mar 2026).
- [ARC-AGI-3](https://arcprize.org/leaderboard) - 🆕 🧪 Third-generation ARC benchmark — agents must adapt on the fly to novel interactive environments (Kaggle competition). Early top scores near zero (Gemini 3.1 Pro ~0.37%).
- [OSWorld](https://os-world.github.io/) - Desktop GUI manipulation. Claude Fable 5 / Mythos 5 lead at 85% (July 2026); GPT-5.4 75% (exceeded human baseline).
- [Arena (formerly LMArena / Chatbot Arena)](https://arena.ai/) - Crowdsourced chat preference battles. July 2026: Claude Fable 5 leads (Elo 1525), ahead of Opus 4.8 (1512) and GPT-5.5 Pro (1510).
- [MMLU-Pro](https://github.com/TIGER-AI-Lab/MMLU-Pro) - Multi-task language understanding, harder successor to MMLU. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTIGER-AI-Lab%2FMMLU-Pro&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LiveCodeBench](https://livecodebench.github.io/) - Contest-style coding benchmark, updated continuously to resist contamination.
- [AIME 2025 / Humanity's Last Exam (HLE)](https://agi.safe.ai/) - Elite math / PhD-level general reasoning.
- [Terminal-Bench](https://www.tbench.ai/) - CLI agent evaluation. Codex CLI 77.3%.
- [Wolfram LLM Benchmarking Project](https://www.wolfram.com/llm-benchmarking-project/) - Code generation benchmark from English spec to Wolfram Language. Updated continuously.
- [Terminal-Bench 2.0](https://www.tbench.ai/leaderboard/terminal-bench/2.0) - **Late 2025 / early 2026**. 89 curated terminal tasks (compile, train, configure, debug). Leaderboard top: NexAU-AHE + GPT-5.5 at 84.7% (May 14, 2026).
- [GDPval](https://openai.com/index/gdpval/) - OpenAI economic-value benchmark (released Sept 2025, arXiv:2510.04374) across 44 occupations / 9 industries; 1,320 expert-built tasks. [GDPval-AA leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa) leader (July 2026): Claude Opus 4.8 (Elo 1890), ahead of GPT-5.5 (1769). Expanded/highlighted again at the GPT-5.6 launch (July 9, 2026).
- [SWE-bench Pro](https://benchlm.ai/benchmarks/swePro) - 🆕 Repository-level engineering successor to Verified. Claude Opus 4.7 64.3% > GPT-5.5 58.6% (Claude leads on long-horizon repo work). **July 2026**: Claude Mythos 5 tops at **80.3%**; ⚠️ **OpenAI audit (July 8, 2026)** revealed ~30% of Pro tasks are broken (overly strict tests, underspecified prompts) — OpenAI has retracted its recommendation to use SWE-bench Pro as a primary coding-agent metric.
- [LLM-Stats Live Leaderboard](https://llm-stats.com/llm-updates) - 🆕 Continuously-refreshed cross-benchmark dashboard for newly-released models.
- [τ²-Bench (Tau-Bench)](https://github.com/sierra-research/tau2-bench) - 🆕 Sierra Research's benchmark for tool-agent-user interaction in real-world domains (retail / airline). Measures multi-turn tool use, DB ops, and policy adherence. April 2026 leader: Claude Mythos Preview at 89.2% across 38 evaluated models. The repo now also hosts **τ³-Bench 1.0.0 (Mar 18, 2026)** adding voice + telecom/banking domains. MIT. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsierra-research%2Ftau2-bench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Gartner Magic Quadrant 2026 — Enterprise AI Coding Agents](https://cursor.com/blog/cursor-leads-gartner-mq-2026) - 🆕 **2026**. Gartner's first MQ for Enterprise AI Coding Agents. Leaders: **GitHub Copilot**, **OpenAI Codex**, **Cursor** (12 vendors evaluated; Tabnine a Visionary). Signals the coding-agent market reaching enterprise maturity.
- [Terminal-Bench 2.1](https://www.tbench.ai/leaderboard/terminal-bench/2.1) - 🆕 **June 2026**. Updated Terminal-Bench with expanded CLI task coverage; leaderboard: Claude Code + Fable 5 leads at 83.8% (June 7, 2026), Codex + GPT-5.5 at 83.1%. Gap between top CLI agents now under 1%.
- [Agent Memory Benchmark (AMB)](https://github.com/vectorize-io/agent-memory-benchmark) - 🆕 Open benchmark for evaluating agent memory systems, released alongside Hindsight by vectorize.io. Tests retain / recall / reflect operations against long-term task performance. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvectorize-io%2Fagent-memory-benchmark&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agents' Last Exam (ALE)](https://snorkel.ai/leaderboard/agents-last-exam/) - 🆕 **June 2026**. UC Berkeley (RDI) + Snorkel AI benchmark evaluating agents on long-horizon, economically valuable professional tasks across 55 subfields — created with 300+ industry experts (public release ALE-V1: 147 reference tasks from a 1,500+ task corpus; arXiv:2606.05405). Launch pass rate ~2.6%; July 2026 leaderboard top: Codex + GPT-5.6 at 53.6/100 (highlighted at the GPT-5.6 launch). Living benchmark with task rotation every 6 months.
- [JetBrains Kotlin Benchmark](https://blog.jetbrains.com/kotlin/2026/07/introducing-the-kotlin-benchmark-evaluate-ai-coding-agents-on-real-world-kotlin-tasks/) - 🆕 **July 2026**. Public benchmark from JetBrains measuring AI coding agents on real-world Kotlin development tasks — code generation, refactoring, test writing, and bug fixing. Gives developers a credible, language-specific evaluation beyond general SWE-bench scores.
- [Stripe Agent Benchmark](https://stripe.com/blog/can-ai-agents-build-real-stripe-integrations) - 🆕 **March 2026**. End-to-end evaluation suite testing whether AI agents can build complete Stripe integrations from scratch — covering code generation, test execution, and production-style validation. Claude Opus 4.5 achieved 92% average score on full-stack API integration tasks in initial evaluations.
- [GAIA Benchmark](https://huggingface.co/spaces/gaia-benchmark/leaderboard) - General AI Assistants benchmark: multi-step reasoning + tool use + web browsing on 466 real-world tasks. **July 15, 2026 public snapshot**: Claude Mythos 5 and Claude Fable 5 lead at **52.3%** (tied), followed by GPT-5.4 Pro at 50.5%. Designed to resist data contamination.

---

## 🖥️ Computer Use & Desktop Agents

*AI agents that can see, control, and automate desktop environments at the OS level. For purely browser-based agents see [🌐 Browser & Web Agents](#-browser--web-agents).*

- [Claude Computer Use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) - Anthropic's computer-use capability — Claude sees the screen and uses mouse/keyboard to automate any software.
- [ChatGPT Agent](https://openai.com/index/introducing-chatgpt-agent/) - Successor to Operator (deprecated 2025) — agent mode in ChatGPT for browsing, booking, form-filling, and web task automation.
- [Google Project Mariner](https://deepmind.google/models/project-mariner/) - 📦 **Discontinued** (May 2026). Browser-agent research project; capabilities merged into Gemini and Chrome.
- [Microsoft Copilot Agents](https://www.microsoft.com/en-us/microsoft-copilot/) - 🆕 Autonomous background agents across the Microsoft 365 stack. Beyond sidebar — executes tasks and surfaces for approvals.
- [Open Interpreter](https://github.com/OpenInterpreter/open-interpreter) - A natural language interface for computers — let LLMs run code locally. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenInterpreter%2Fopen-interpreter&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Manus AI](https://manus.im/) - 🆕 🇨🇳 Autonomous general-purpose AI agent with cloud-to-local hybrid model. Handles research, coding, and complex multi-step tasks.
- [Genspark](https://www.genspark.ai/) - 🆕 All-in-one autonomous work agent with mixture-of-agents architecture. Can make phone calls.
- [Beam AI](https://beam.ai/) - 🆕 Self-learning desktop agents that refine logic based on successful outcomes.
- [Microsoft Copilot Studio Computer-Using Agents](https://techcommunity.microsoft.com/blog/copilot-studio-blog/computer-using-agents-in-microsoft-copilot-studio-are-now-generally-available/4519427) - 🆕 **GA May 13, 2026**. Build agents inside Copilot Studio that interact directly with websites and desktop applications through the UI — Microsoft's first-party answer to Claude Computer Use, now generally available across Microsoft 365 / Power Platform deployments.
- [Perplexity Personal Computer](https://www.perplexity.ai/hub/products/computer-for-windows) - 🆕 **June 2026 (Windows)**. Brings Perplexity's multi-model agent orchestrator (19+ AI models routed automatically) to Windows; connects local files, native apps, and web services in one system. Builds on the Mac version (April 16) and the upcoming hybrid local/cloud inference orchestrator from Computex 2026.
- [ChatGPT Workspace Agents](https://venturebeat.com/orchestration/openai-unveils-workspace-agents-a-successor-to-custom-gpts-for-enterprises-that-can-plug-directly-into-slack-salesforce-and-more) - 🆕 **Research preview April 22, 2026; credit-based pricing May 6, 2026; EKM support May 7, 2026**. OpenAI's successor to Custom GPTs for enterprises — cloud-side agents with file access, code execution, scheduled runs and built-in connectors for Slack, Google Drive, Salesforce. Available on Business / Enterprise / Edu / Teachers; powered by Codex.

---

## 🌐 Browser & Web Agents

*Frameworks and infrastructure for agents that interact with the web through real browsers — navigate, click, scrape, and complete multi-page workflows.*

- [Browser Use](https://github.com/browser-use/browser-use) - Make websites accessible for AI agents with browser automation. The de-facto open-source choice in 2026, 105K stars. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowser-use%2Fbrowser-use&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Stagehand](https://github.com/browserbase/stagehand) - The SDK for browser agents — typed `act`/`extract`/`observe` primitives over Playwright by Browserbase. MIT. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowserbase%2Fstagehand&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Steel Browser](https://github.com/steel-dev/steel-browser) - 🆕 Open-source browser API for AI agents — batteries-included sandboxed Chromium with session persistence and proxy rotation. Apache-2.0. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsteel-dev%2Fsteel-browser&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Skyvern](https://github.com/Skyvern-AI/skyvern) - Automate browser-based workflows with LLMs and computer vision. AGPL-3.0. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSkyvern-AI%2Fskyvern&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentQL](https://github.com/tinyfish-io/agentql) - Query language + Playwright integration for semantic web extraction. Reliable on dynamic, cluttered pages. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftinyfish-io%2Fagentql&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hyperbrowser MCP](https://github.com/hyperbrowserai/mcp) - 🆕 Hosted headless-browser fleet exposed as an MCP server — plug into Claude/GPT/LangChain via the standard tool interface. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhyperbrowserai%2Fmcp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) - 🆕 Microsoft's official Playwright server exposed as an MCP tool. Production-grade automation primitives without rolling your own bridge. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fplaywright-mcp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MultiOn](https://theagi.company/) - 📦 Hosted browser agent platform with native Reasoning + Memory; multion.ai now redirects to AGI, Inc. (theagi.company). Closed-source.
- [Browserbase](https://www.browserbase.com/) - Headless browser infrastructure built specifically for AI agents — stealth, persistence, captcha solving, observability.
- [BrowserOS](https://www.browseros.com/) - 🆕 First open-source browser with built-in AI agents — privacy-first Chrome alternative. Natural-language task automation without coding; local-first design competes with Perplexity's Comet and Arc's AI features.
- [Vercel Agent Browser](https://github.com/vercel-labs/agent-browser) - 🆕 Headless browser automation CLI for AI agents. June 2026 release adds `vitals` command for Core Web Vitals (LCP/CLS/TTFB/FCP), `pushstate` for SPA navigation, out-of-process plugin system, MCP server mode, and `@agent-browser/sandbox` for hosted environments. Apache-2.0, 37K+ stars. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvercel-labs%2Fagent-browser&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Google ADK — browser & A2A integration](https://github.com/google/adk-python) - Google's Agent Development Kit (v1.33, May 2026; v2.0 in beta) — multi-agent composition, MCP tools, A2A Protocol integration. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle%2Fadk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [WebBrain](https://webbrain.one) - 🆕 **July 2026**. Open-source MIT browser extension (Chrome + Firefox) for automating web tasks with local or cloud LLMs. "Ask mode" for read-only summarization and data extraction; "Act mode" for clicks, form fills, and navigation. Local-first by design — data never leaves the device when using llama.cpp / Ollama.
- [Muse Spark 1.1 (web agent)](https://artificialanalysis.ai/models/muse-spark) - 🆕 💰 **July 9, 2026**. Meta Superintelligence Labs' first paid agentic model, via the Meta Model API public preview — scores 69.0 on WebArena-Verified (behind Claude Opus 4.8's leading 71.2).
- [Firecrawl v2](https://github.com/firecrawl/firecrawl) - 🆕 **v2.11.0, June 2026**. Major update to the agentic web scraping platform: improved JavaScript rendering, live crawl webhooks, and batch URL processing. 150K+ stars. AGPL-3.0 (MIT SDKs). ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ffirecrawl%2Ffirecrawl&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome) - 🆕 Anthropic's browser-agent Chrome extension — Claude navigates, fills forms, and acts across tabs. ⚠️ July 2026 research showed rogue-extension prompt-injection risks; review permissions before use.
- [Perplexity Comet](https://www.perplexity.ai/comet) - Perplexity's agentic AI browser with Comet Assistant (background agent); free tier since Oct 2025; Perplexity raised $200M for Comet in June 2026.

---

## 🗣️ Voice & Multimodal Agents

*Voice-enabled and multimodal AI agent platforms.*

- [AgentLine](https://agentline.cloud/) - 🆕 ⚠️ **Unverified.** Telephony infrastructure for AI agents — provision phone numbers, make/receive calls, real-time transcription to JSON webhooks. Pitched as a thinner alternative to Twilio for agent voice pipelines; submitter claims 30+ paid users, no third-party adoption signal yet.
- [ElevenLabs](https://elevenlabs.io/) - AI voice platform with conversational AI agents and realistic speech synthesis.
- [Vapi](https://github.com/VapiAI/server-sdk-python) - Enterprise voice AI platform — build, test, and deploy voice agents. **$50M Series B announced May 12, 2026** after crossing 1B platform calls; May 2026 updates ship Squads v2 (multi-assistant orchestration), Composer alpha (prompt-built agents), Simulations alpha (systematic AI-powered testing), and GA of the Soniox low-latency multilingual transcriber. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FVapiAI%2Fserver-sdk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Retell AI](https://www.retellai.com/) - Build production-ready conversational voice AI agents.
- [Bland AI](https://www.bland.ai/) - AI phone calling platform — enterprise-grade conversational AI.
- [Hermes](https://buildwithhermes.com/) - 🆕 ⚠️ **Unverified (founders' beta).** White-label voice agent platform aimed at agencies: agents, native CRM, outbound/inbound campaign orchestration, and per-client usage billing in one system. Sits a layer above raw voice APIs (Vapi/Retell) by bundling the CRM and billing an agency would otherwise assemble itself. Paid plans start at $149/mo with included minutes. No independent adoption data yet.
- [LiveKit Agents](https://github.com/livekit/agents) - Build real-time multimodal AI agents with voice, video, and data. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flivekit%2Fagents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Pipecat](https://github.com/pipecat-ai/pipecat) - Open-source framework for voice and multimodal conversational AI. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fpipecat-ai%2Fpipecat&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vocode](https://github.com/vocodedev/vocode-core) - 💤 **Stale** (last release June 2024). Open-source library for building voice-based LLM agents. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvocodedev%2Fvocode-core&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Bolna](https://github.com/bolna-ai/bolna) - End-to-end open-source voice AI agents framework. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbolna-ai%2Fbolna&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cartesia](https://www.cartesia.ai/) - 🆕 Ultra-low-latency voice AI for real-time conversational agents.
- [Meta Voice AI](https://ai.meta.com/) - 🆕 Former PlayHT/Play.ai team's tech, integrated into Meta AI, AI Characters, and Meta wearables after July 2025 acquisition. Original Play.ai platform shut down Dec 31, 2025.
- [Sesame](https://www.sesame.com/) - 🆕 Voice AI companion with emotional understanding and natural conversation.
- [ElevenAgents](https://elevenlabs.io/agents) - 🆕 ElevenLabs' full-stack voice-agent platform (April-May 2026 updates): MCP, multimodal messages, conversation topic discovery, knowledge-base search, pre-tool speech controls. First voice-agent platform to earn AIUC-1 certification.
- [Cartesia Line](https://cartesia.ai/blog/introducing-line-for-voice-agents) - Code-first voice-agent platform (launched Aug 2025) built on Cartesia's Sonic TTS + Ink STT with background reasoning and on-prem deployment options; ~40-90ms time-to-first-audio.
- [Deepgram Voice Agent API](https://deepgram.com/product/voice-agent-api) - 🆕 Single endpoint bundling STT (Nova-3) + LLM routing + TTS (Aura-2) + Flux conversational STT with mid-call language switching across 10 languages.
- [OpenAI Realtime API (GPT-Realtime-2)](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/) - 🆕 **May 7, 2026**. GPT-5-class reasoning over voice with parallel tool calls, 128K context; shipped alongside GPT-Realtime-Translate and GPT-Realtime-Whisper. Updated to gpt-realtime-2.1 / 2.1-mini on July 6, 2026 (better alphanumeric recognition, noise handling, lower latency).
- [Dograh](https://github.com/dograh-hq/dograh) - 🆕 Open-source, self-hostable voice AI platform — an alternative to Vapi / Retell. On-prem, BYOK across Speech-to-Speech or LLM/STT/TTS, visual workflow builder, MCP-native, telephony support. BSD-2-Clause, 4K+ stars. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdograh-hq%2Fdograh&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hume TADA](https://github.com/HumeAI/tada) - 🆕 **March 2026**. Hume AI's first open-source TTS — Text Audio Dual Alignment: text and audio generated in one synchronized 1:1 token stream; zero content hallucinations, ~0.09 RTF, TADA-1B/3B-ML (9+ languages), runs on a smartphone; powers the next generation of EVI voice agents. MIT code, Llama 3.2 licensed weights. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHumeAI%2Ftada&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenYabby](https://github.com/OpenYabby/OpenYabby) - 🆕 Open-source macOS voice-driven multi-agent orchestrator — Realtime API + CLI runners + multi-channel orchestration. A lead agent plans the work and delegates to sub-agents for review and QA. MIT. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenYabby%2FOpenYabby&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Grok Voice Agent Builder](https://x.ai/news/grok-voice-agent-builder) - 🆕 **July 1, 2026**. xAI's no-code platform for production voice agents on Grok Voice — telephony with free provisioned numbers, knowledge collections, tools/MCP connectors, guardrails, 80+ voices plus ~2-minute voice cloning; $0.05/min in beta.

## 📱 Personal AI Agents

*AI agents designed for personal use, productivity, and daily life assistance.*

- [OpenClaw](https://github.com/openclaw/openclaw) - 🆕 Personal AI agent platform with skills, memory, Dreaming, Canvas/A2UI, ACP coding harness integration. Runs on your machine with multi-channel messaging. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenclaw%2Fopenclaw&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Rabbit R1](https://www.rabbit.tech/) - Dedicated AI hardware device with a large action model for personal assistance.
- [Limitless](https://www.limitless.ai/) - 📦 **Acquired by Meta (late 2025)**; pendant sales discontinued. Personalized AI powered by what you've seen, said, and heard (formerly Rewind); team folded into Meta's AI-wearables effort.
- [Open Interpreter](https://github.com/OpenInterpreter/open-interpreter) - A natural language interface for computers — let LLMs run code locally. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenInterpreter%2Fopen-interpreter&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [01 Light](https://github.com/OpenInterpreter/01) - 💤 **Stale** (no commits since 2024-11). Open-source voice interface for computers. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenInterpreter%2F01&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Leon](https://github.com/leon-ai/leon) - Open-source personal assistant — lives on your server. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fleon-ai%2Fleon&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Khoj](https://github.com/khoj-ai/khoj) - Personal AI second brain — search and chat with your notes, docs, and images. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fkhoj-ai%2Fkhoj&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Humane AI Pin](https://humane.com/) - ⚠️ **Discontinued Feb 28, 2025** (acquired by HP, device shut down). Originally a wearable AI device with a screenless, ambient computing experience.
- [Arahi AI](https://arahi.ai/) - 🆕 Personal productivity and business automation assistant.
- [Lindy AI](https://www.lindy.ai/) - 🆕 No-code AI agent for email, calendar, and workflow automation.
- [MuleRun](https://mulerun.com/) - 🆕 Always-on agents for recurring tasks and background automation.
- [Gemini Intelligence](https://blog.google/products-and-platforms/platforms/android/gemini-intelligence/) - 🆕 **May 12, 2026** (Android Show: I/O Edition). Proactive agentic AI features integrated into Googlebooks laptops, Wear OS, Android Auto, Android XR, and starting on the latest Samsung Galaxy + Pixel devices. Auto-creates shopping carts from grocery lists, books spin classes, filler-word removal via the Rambler speech-to-text.
- [Gemini Spark](https://gemini.google/overview/agent/spark/) - 🆕 **I/O 2026 (May 19, 2026)**. Google's 24/7 autonomous agent in the Gemini app — runs multi-step processes proactively with Gmail/Workspace integration; expanded to a native Mac app July 1, 2026.
- [QwenPaw](https://github.com/agentscope-ai/QwenPaw) - 🆕 🇨🇳 **May 2026 rebrand from CoPaw**. Self-hostable personal assistant in the Qwen / AgentScope family. Local-first memory, hot-loadable skills, multi-agent collaboration, multi-channel (DingTalk / Feishu / WeChat / Discord / Telegram), tool guard + skill scanner. Apache-2.0. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentscope-ai%2FQwenPaw&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AI Growth Agents for Marketers](https://github.com/thaolst/ai-growth-agents-for-marketers) - 🆕 ⚠️ **Unverified** (early-stage). Growth marketing prompts and Python agents built from real fintech campaigns in Southeast Asia. Covers campaign briefs, MEU planning, and A/B test analysis with multi-agent workflows. Agent Skills format — installable via `npx skills add`. Bilingual VI + EN. MIT. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fthaolst%2Fai-growth-agents-for-marketers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsoft Scout](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) - 🆕 **Build 2026 (June 2, 2026)**. Microsoft's always-on personal agent built on the OpenClaw framework — proactive across cloud / desktop / web, connects to Teams / Outlook / OneDrive / SharePoint. Each agent runs under its own Entra identity with continuous policy-conformance checks and audit trails. Private preview via the Microsoft Frontier program; requires Intune policy + GitHub Copilot license.
- [Lenovo Qira / Motorola Qira](https://news.lenovo.com/pressroom/press-releases/lenovo-unveils-lenovo-and-motorola-qira/) - 🆕 **CES 2026 (Jan 6, 2026)**. Cross-device "Personal Ambient Intelligence System" co-developed by Lenovo and Motorola — context-aware AI that perceives, thinks, and acts across PCs / phones / tablets / wearables. Rolling out on select Lenovo devices in Q1 2026, expanding to Motorola phones thereafter; first major OEM ambient-AI play.
- [Yao Agents](https://yaoagents.com) - 🆕 🇨🇳 **May 2026**. Local-first AI execution platform with 30+ domain Experts (coding, writing, data analysis, PM) and autonomous Robot workers. Features a 5-stage Pipeline (Inspiration→Goals→Tasks→Validation→Delivery), Docker sandbox isolation, multi-platform messaging (WeChat/Feishu/DingTalk/Telegram/Discord), MCP support, BYOK model configuration, and Tai Link for cross-device agent orchestration. Open-source engine: [YaoApp/yao](https://github.com/YaoApp/yao).
- [AgentArk](https://github.com/agentark-ai/AgentArk) - 🆕 🧪 **June 2026** (v0.0.1, beta — not for production). Personal AI OS prioritizing local control and security; self-learning via the GEPA optimizer runtime. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentark-ai%2FAgentArk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [nanobot](https://github.com/HKUDS/nanobot) - 🆕 Ultra-lightweight open-source personal AI agent (41K+ stars). April 2026 releases (v0.1.5.x) added thread-scoped sessions, auto-compact memory, Dream consolidation, DeepSeek-V4 support, and Windows support. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2Fnanobot&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 📱 Mobile Agents

*GUI agents that drive Android/iOS phones — the next frontier after desktop computer-use. Most major model providers now ship a mobile-grounded variant.*

- [Mobile-Agent](https://github.com/X-PLUG/MobileAgent) - 🇨🇳 Alibaba's flagship multimodal phone-control agent family (v1 → v3, plus Mobile-Agent-E and Mobile-Agent-V). State-of-the-art on Android benchmarks. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FX-PLUG%2FMobileAgent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AppAgent](https://github.com/TencentQQGYLab/AppAgent) - 💤 Tencent's multimodal agent that operates smartphone apps by tapping/swiping. Influential early implementation; succeeded by AppAgentX (Mar 2025). ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTencentQQGYLab%2FAppAgent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Apple Intelligence](https://www.apple.com/apple-intelligence/) - On-device agent layer in iOS / iPadOS / macOS. App Intents and screen-aware actions across the OS.
- [Samsung Galaxy AI / Bixby 2.0](https://www.samsung.com/global/galaxy/galaxy-ai/) - On-device Gauss-powered agentic capabilities baked into the Galaxy S26 line.
- [Google Gemini for Android](https://gemini.google/) - Replaces Google Assistant on Android with full Gemini-powered, app-aware actions including system intents and Workspace.
- [Magma](https://microsoft.github.io/Magma/) - Microsoft Research foundation model for multimodal agents — grounds across UI, robotics, and physical action; targets phones, web, and embodied tasks.
- [mobile-use](https://github.com/minitap-ai/mobile-use) - 🆕 Open-source framework (Apache-2.0, 2.5K+ stars) letting AI agents drive real Android and iOS apps as if they were a human — UI-aware navigation, natural-language control. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fminitap-ai%2Fmobile-use&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [agent-device (Callstack)](https://github.com/callstack/agent-device) - 🆕 **February 2026**. Lightweight, token-efficient CLI for automating iOS and Android devices + simulators. Command model designed for AI agents and CI; MIT, 2.6K+ stars. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcallstack%2Fagent-device&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🏢 Enterprise Agent Platforms

*Enterprise-grade platforms for deploying AI agents at scale.*

- [Salesforce Agentforce 360](https://www.salesforce.com/agentforce/what-is-new/) - Autonomous AI agents for enterprise CRM — sales, service, and marketing. **Spring 2026 release** ships Agentforce Builder (conversational agent authoring), Agent Script (deterministic behavior control), Agentforce Voice (Amazon Connect / Five9 / Genesys / NiCE / Vonage + SIP), and Intelligent Context on top of the new Data 360. Customers across 124 countries report ~85% autonomous query resolution.
- [Microsoft Copilot Studio](https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio) - Build and customize AI agents and copilots for your organization.
- [Gemini Enterprise Agent Platform](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform) - 🆕 **April 22, 2026** (Google Cloud Next '26). Evolution of Vertex AI into a unified hub for building, scaling, governing, and optimizing enterprise agents. Supports Gemini 3.1 Pro/Flash, Lyria 3, plus third-party models (Claude Opus/Sonnet/Haiku). Integrated agent DevOps, security, and orchestration.
- [Google Vertex AI Agent Builder](https://cloud.google.com/products/agent-builder) - **Renamed April 2026** — Vertex AI's agent-building capabilities are now part of the Gemini Enterprise Agent Platform (see above): Agent Studio, Model Garden, Google Antigravity orchestration.
- [Amazon Bedrock Agents](https://aws.amazon.com/bedrock/agents/) - Build AI agents that can execute multi-step tasks across company systems.
- [ServiceNow AI Agents](https://www.servicenow.com/products/ai-agents.html) - AI agents for enterprise IT service management with AI Control Tower. 🆕
- [ServiceNow Action Fabric (MCP Server)](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-opens-its-full-system-of-action-to-every-AI-Agent-in-the-enterprise/default.aspx) - 🆕 **May 5, 2026**. ServiceNow opens its AI Platform to any AI agent (Claude, Copilot, custom) via a GA MCP Server bundled with every Now Assist and AI Native SKU. Every action runs through AI Control Tower — identity-verified, permission-scoped, audited; OAuth, consumption metering, role-based tool packages out of the box. Anthropic (Claude Cowork) is first design partner.
- [IBM watsonx Orchestrate](https://www.ibm.com/products/watsonx-orchestrate) - AI assistant platform to automate work across enterprise applications.
- [Oracle AI Agents](https://www.oracle.com/artificial-intelligence/) - Enterprise AI agents integrated with Oracle Fusion Cloud ERP. 🆕
- [Moveworks](https://www.moveworks.com/) - Enterprise copilot platform — AI that works across every system. Acquired by ServiceNow (closed December 15, 2025).
- [UiPath Agentic Automation](https://www.uipath.com/) - 🆕 Agentic reasoning layered onto RPA bot estates for intelligent process automation.
- [AgentX](https://www.agentx.so/) - 🆕 Agentic enterprise solution for scalable AI automation with plug-and-play chatbots.
- [Sistava](https://sistava.com) - ⚠️ "AI employees on demand" for sales, marketing, support, recruiting, and operations — agents work inside your tools with persistent memory; from $19/month.
- [Sema4.ai](https://sema4.ai/) - 🆕 Enterprise AI agent platform with Python-first approach and built-in governance.
- [SAP Business AI Platform + Autonomous Suite](https://news.sap.com/2026/05/sap-sapphire-sap-unveils-autonomous-enterprise/) - 🆕 **SAP Sapphire 2026 (May 12, 2026)**. SAP unveils the "Autonomous Enterprise": SAP Business AI Platform as the unified AI foundation; SAP Autonomous Suite adding agents to existing apps across finance, supply chain, procurement, HR, and CX; Joule Studio for building enterprise agents and agentic workflows; Joule Work UX; and seven Industry AI solutions. Claude is among the foundation models powering Joule agents.
- [Microsoft Agent 365 + Microsoft 365 E7](https://techcommunity.microsoft.com/blog/agent-365-blog/microsoft-365-e7--agent365-from-where-you-are-to-enterprise-ai-at-scale/4519969) - 🆕 **May 1, 2026 GA** with extended May rollouts. Identity-first control plane for governing and securing AI agents across enterprise environments; $15/user/month standalone, $99/user/month inside the new Microsoft 365 E7 "Frontier" suite. May 2026 update adds AWS Bedrock + Google Cloud registry sync, Intune/Defender preview policies, and SASE for agents.
- [OpenAI Guaranteed Capacity (Compute Annual Pass)](https://openai.com/business/guaranteed-capacity/) - 🆕 **May 19, 2026**. Long-term enterprise compute reservations (1 / 2 / 3-year terms, larger discounts at longer terms) sold as a structured product. Designed to derisk enterprise rollout of GPT-5.5-class agents — OpenAI's reply to the Anthropic Priority Tier model.
- [Bristol Myers Squibb ↔ Claude Enterprise](https://news.bms.com/news/corporate-financial/2026/Bristol-Myers-Squibb-Announces-Strategic-Agreement-with-Anthropic-to-Position-Claude-Enterprise-as-the-Shared-Intelligence-Platform-Across-Its-Global-Operations/default.aspx) - 🆕 **May 20, 2026**. BMS standardises on Claude Enterprise as its shared intelligence platform for **30,000+ employees**, embedding agentic Claude into drug-discovery / development / delivery pipelines. First top-5 pharma to make a public, company-wide Claude commitment.
- [Kore.ai Artemis Agent Platform](https://www.kore.ai/news/kore-ai-launches-artemis-the-new-generation-of-the-kore-ai-agent-platform-for-building-governing-and-optimizing-enterprise-ai) - 🆕 **May 21, 2026** (launched on Azure). AI-native enterprise agent platform built around the new YAML-style **Agent Blueprint Language (ABL)** for declarative multi-agent workflows. Kore.ai's structural challenge to Copilot Studio and Agentforce.
- [FPT Flezi Foundry™](https://www.morningstar.com/news/business-wire/20260521235556/fpt-launches-flezi-foundry-advancing-ai-augmented-delivery-for-global-enterprises) - 🆕 **May 21, 2026**. AI-augmented delivery platform with two governed Service-as-a-Software modes — **Agentic Development Lifecycle (ADLC)** for full SDLC agent crews and **Agentic Managed Services (AMS)** for incident-resolution agents on top of existing ITOps.
- [Amazon Bedrock AgentCore Payments](https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-bedrock-agentcore-payments-preview/) - 🆕 **May 7, 2026 (preview)**. Managed payments for AgentCore agents — autonomous payment for APIs, MCP servers, web content, and other agents via Coinbase (CDP wallet, x402 Bazaar) and Stripe (Privy wallet) integrations; spending limits and transaction observability across four AWS regions.
- [OutSystems Agentic Systems Platform](https://www.outsystems.com/) - 🆕 **June 2026**. OutSystems positions its low-code platform as an "AI-native" agentic development environment. Open and governed AI, BYO model, multi-agent orchestration, and enterprise compliance tooling. Challenger to Copilot Studio and Agentforce.
- [Databricks Genie One](https://www.databricks.com/blog/introducing-genie-one-genie-ontology-and-genie-agents) - 🆕 **June 16, 2026 (Data + AI Summit)**. Agentic "data coworker" that automates and orchestrates work across structured and unstructured data — inside or outside Databricks — grounded in the new **Genie Ontology** (an organization-wide knowledge graph) and governed by Unity Catalog. Ships with Genie Agents; Databricks reports 84.5% first-attempt accuracy in internal testing.
- [ZenseAI.AgentMesh (Zensar)](https://www.prnewswire.com/news-releases/zensar-technologies-launches-zenseaiagentmesh-to-accelerate-enterprise-ai-adoption-at-scale-302805437.html) - 🆕 **June 19, 2026**. Zensar's enterprise-grade agentic AI platform — a "universal enterprise operating system for agentic AI" to discover, build, deploy, and govern autonomous agents at scale, with a catalogue of 80+ pre-built industry and cross-functional agents and a stated 6–8 week pilot-to-production path.
- [Meta Business Agent](https://about.fb.com/news/2026/06/meta-business-agent/) - 🆕 **June 3, 2026 (global rollout)**. Meta's AI business agent for WhatsApp, Instagram, and Messenger — answers customer questions, recommends catalog products, books appointments, qualifies leads, and closes sales, handing off to a human when needed. 1M+ businesses already on it; a **Meta Business Agent Platform** lets enterprises configure agents and connect Shopify / Zendesk / Shopee — free to activate today, paid subscription tiers coming.
- [Snyk Evo Agentic Development Security (ADS)](https://snyk.io/news/snyk-launches-evo-agentic-development-security/) - 🆕 **June 2026**. Security and governance platform built specifically for autonomous AI coding agents; governs what agents use, what they do, and the code they generate in real-time.
- [Cognizant Neuro AI + ServiceNow AI Agent](https://news.cognizant.com/2026-06-18-Cognizant-expands-cross-platform-agentic-AI-with-new-ServiceNow-AI-Agent-interoperability) - 🆕 **June 2026**. Cross-platform enterprise orchestration enabling ServiceNow agents to work natively within Cognizant's Multi-Agent Accelerator.
- [Talkdesk Agent Builder](https://www.cmswire.com/contact-center/customer-contact-week-2026-capturing-the-ai-announcements-in-contact-center-technology/) - 🆕 **June 2026**. Low-code builder allowing business users to deploy production-grade AI agents in the contact center in hours instead of weeks.
- [HelloTwin Digital Authority](https://siliconangle.com/2026/06/24/hellotwin-launches-digital-authority-bring-governed-ai-agents-enterprise/) - 🆕 **June 2026**. AI twin designed as a single, auditable source of truth to govern agentic workflows with clear boundaries.

## 📊 Agent Evaluation & Observability

*Tools for testing, evaluating, and monitoring AI agents in production.*

- [AgentBench](https://github.com/THUDM/AgentBench) - Multi-dimensional benchmark for evaluating LLMs as agents. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTHUDM%2FAgentBench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangSmith](https://www.langchain.com/langsmith) - Platform for debugging, testing, evaluating, and monitoring LLM applications.
- [Helicone](https://github.com/Helicone/helicone) - Open-source LLM observability platform — logs, metrics, and traces. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHelicone%2Fhelicone&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Braintrust](https://www.braintrust.dev/) - Enterprise-grade stack for building AI products — evals, prompt playground, logging. SDKs: [braintrust-sdk-javascript](https://github.com/braintrustdata/braintrust-sdk-javascript) and braintrust-sdk-python (repo split/renamed from braintrust-sdk).
- [Arize Phoenix](https://github.com/Arize-ai/phoenix) - AI observability & evaluation — traces, evals, and datasets. **July 7, 2026**: Metric Charts, Trace Search, expanded REST API; July 1 added granular LLM + tool span attributes via new OpenInference span attrs. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FArize-ai%2Fphoenix&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Langfuse](https://github.com/langfuse/langfuse) - Open-source LLM engineering platform — traces, evals, prompt management. **Acquired by ClickHouse Jan 2026**; March 2026 shift to an observations-centric data model, April 2026 added Langfuse Cloud Japan + Experiments + Langfuse Academy + LLM-as-a-Judge API; v4 self-host release queued. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangfuse%2Flangfuse&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenLLMetry](https://github.com/traceloop/openllmetry) - Open-source observability for LLM applications based on OpenTelemetry. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftraceloop%2Fopenllmetry&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Weights & Biases Weave](https://github.com/wandb/weave) - Toolkit for developing, evaluating, and monitoring AI applications. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fwandb%2Fweave&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SWE-bench](https://github.com/SWE-bench/SWE-bench) - Benchmark for evaluating LLMs on real-world software engineering problems. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSWE-bench%2FSWE-bench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Terminal-Bench](https://www.tbench.ai/) - 🆕 Benchmark for terminal-based coding agent evaluation. Maintained by Harbor Framework. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fharbor-framework%2Fterminal-bench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Harbor](https://github.com/harbor-framework/harbor) - 🆕 Framework for evaluating and optimizing agents and LLMs at scale — run Terminal-Bench 2.x and custom benchmarks across thousands of cloud sandboxes, generate RL rollouts; a Stanford × Laude Institute collaboration. Apache-2.0. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fharbor-framework%2Fharbor&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Arena (formerly LMArena / LMSYS Chatbot Arena)](https://arena.ai/) - Crowdsourced AI benchmark using human preference voting; leaderboards now cover LLMs, image generation, and code models. LMSYS → LMArena (2025) → Arena (2026).
- [Patronus AI](https://www.patronus.ai/) - 💰 LLM evaluation/red-teaming company now positioned as a frontier research lab building digital world models and simulation infrastructure for agent training ($50M Series B); research artifacts include Lynx, FinanceBench, and GLIDER.
- [DeepEval](https://github.com/confident-ai/deepeval) - Pytest-style LLM eval framework with 14+ built-in metrics (G-Eval, hallucination, faithfulness). Most-starred open-source eval lib in 2026. Apache-2.0. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fconfident-ai%2Fdeepeval&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agenta](https://github.com/agenta-ai/agenta) - 🆕 Open-source LLMOps platform combining prompt playground, prompt management, evaluation, and observability. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagenta-ai%2Fagenta&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangSmith SDK](https://github.com/langchain-ai/langsmith-sdk) - Official client SDK for LangChain's hosted observability platform. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangsmith-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AutoEvals](https://github.com/braintrustdata/autoevals) - Standalone library of best-practice LLM eval scorers (factuality, JSON validity, semantic similarity, etc.) by Braintrust. Drop-in for any framework. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbraintrustdata%2Fautoevals&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [BenchClaw](https://github.com/Agnuxo1/benchclaw) - ⚠️ **Unverified.** Self-described multi-dimensional agent evaluation harness (17-judge tribunal, deception detectors, 10 scoring dimensions). Repo is single-maintainer with very low independent adoption; the same submission was sent to 8+ awesome lists in parallel — one was merged at [eudk/awesome-ai-tools](https://github.com/eudk/awesome-ai-tools/pull/229), the rest are pending or declined. Listed for visibility, evaluate before relying on its scores. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAgnuxo1%2Fbenchclaw&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [PromptEden](https://www.prompteden.com) - ⚠️ **Unverified.** Commercial AI-visibility monitoring service — tracks how ChatGPT, Claude, Gemini, Perplexity, Copilot, and Grok describe brands and which competitors they recommend, refreshed daily across 9+ platforms. Submitted to 10 awesome lists on the same day — promising category but listed for visibility only, evaluate before purchasing.
- [Laminar](https://github.com/lmnr-ai/lmnr) - 🆕 Open-source observability platform purpose-built for long-running AI agents (Apache-2.0, YC S24). OpenTelemetry-native, transcript view, Signals, SQL over traces, browser-agent session replay. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flmnr-ai%2Flmnr&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangSmith Engine](https://www.langchain.com/blog/interrupt-2026-overview) - 🆕 **May 2026 (Interrupt 2026)**. Autonomous failure-diagnosis layer for LangSmith — clusters production failures into prioritised issues, root-causes them across traces and code, and proposes fixes for human review. Companion to the new SmithDB (Rust + DataFusion-backed agent observability database).
- [AgentSight](https://github.com/eunomia-bpf/AgentSight) - Zero-instrumentation eBPF observability for LLM/coding agents. Captures syscall-level traces (process, file, network) without modifying the agent, enabling full-stack behavioral analysis. MIT. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Feunomia-bpf%2FAgentSight&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Prismix](https://prismix.dev) - Real-time status monitoring for 77+ AI services (OpenAI, Anthropic, Cursor, etc.) with status badges and API, AI news aggregator from 71+ sources, and an MCP server directory with 80+ servers. Free, no signup.
- [Ceros (by Beyond Identity)](https://www.prnewswire.com/news-releases/ceros-launches-providing-unified-identity-observability-and-governance-for-every-ai-agent-and-workflow-302800721.html) - 🆕 **June 16, 2026**. Agentic AI trust layer for unified identity, observability, and governance — discovery/inventory, runtime policy enforcement, audit trails. (Unrelated to the interactive-content company of the same name.)
- [Zoom Agent Performance Suite](https://news.zoom.com/introducing-agent-architect-and-agent-performance-suite-for-zoom-virtual-agent/) - 🆕 **June 2026**. Dedicated suite to test, validate, and optimize autonomous agent performance in customer-facing scenarios.
- [AgentOps](https://github.com/AgentOps-AI/agentops) - 🆕 Agent monitoring, compliance, and testing toolkit with session replays; MCP server for zero-config observability of any MCP-connected agent; 5K+ stars. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAgentOps-AI%2Fagentops&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenTelemetry GenAI Semantic Conventions](https://github.com/open-telemetry/semantic-conventions-genai) - Standardized spans, metrics, and events for GenAI clients, agents, tool invocations, and MCP — vendor-neutral tracing across any OTel backend (Arize, Langfuse, Helicone, Jaeger, etc.). Moved out of the core semconv repo into a dedicated GenAI repository.
- [Tracecat](https://github.com/TracecatHQ/tracecat) - 🆕 Open-source security-automation platform that captures complete agent traces for SOC workflows — integrates AI agents with detection, enrichment, and response pipelines. AGPL-3.0 (with enterprise-edition exceptions). ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTracecatHQ%2Ftracecat&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

## 🔬 AI Research Tools

*Tools and platforms for AI/ML research, experimentation, and development.*

- [Hugging Face](https://huggingface.co/) - The AI community's platform — models, datasets, and Spaces for ML research.
- [Hugging Face Transformers](https://github.com/huggingface/transformers) - The de-facto standard library for models and training tooling. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhuggingface%2Ftransformers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [vLLM](https://github.com/vllm-project/vllm) - 🆕 High-throughput LLM serving engine with PagedAttention. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvllm-project%2Fvllm&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Ollama](https://github.com/ollama/ollama) - Run LLMs locally with a simple API. Supports Llama, Mistral, Qwen, and more. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Follama%2Follama&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LM Studio](https://lmstudio.ai/) - Desktop app for running local LLMs with a user-friendly interface.
- [SGLang](https://github.com/sgl-project/sglang) - 🆕 Fast serving framework for large language and vision models. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsgl-project%2Fsglang&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [llama.cpp](https://github.com/ggml-org/llama.cpp) - LLM inference in C/C++ — run models on consumer hardware. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fggml-org%2Fllama.cpp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MLX](https://github.com/ml-explore/mlx) - 🆕 Apple's array framework for ML on Apple silicon. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fml-explore%2Fmlx&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Unsloth](https://github.com/unslothai/unsloth) - 🆕 Fine-tune LLMs 2x faster with 70% less memory. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Funslothai%2Funsloth&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenRouter](https://openrouter.ai/) - Unified API for accessing 400+ AI models from 70+ providers.
- [Weights & Biases](https://wandb.ai/) - ML experiment tracking, dataset versioning, and model management.
- [Label Studio](https://github.com/HumanSignal/label-studio) - Multi-type data labeling and annotation tool. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHumanSignal%2Flabel-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SmithDB](https://www.langchain.com/blog/interrupt-2026-overview) - 🆕 **May 2026 (Interrupt 2026)**. LangChain's purpose-built agent observability database. Rust on top of Apache DataFusion + Vortex, with object-storage backing for trace data — designed for the volumes and access patterns of agent traces.

---

## 📚 Learning Resources

*Papers, courses, tutorials, and guides for understanding and building AI agents.*

### Papers

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) - The foundational paper on reasoning + acting in LLMs.
- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) - Teaching LLMs to use external tools autonomously.
- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) - Stanford's generative agent architecture with memory and reflection.
- [A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432) - Comprehensive survey of LLM-based autonomous agents.
- [The Rise and Potential of Large Language Model Based Agents](https://arxiv.org/abs/2309.07864) - In-depth analysis of LLM agent capabilities and future directions.
- [Agent Hospital](https://arxiv.org/abs/2405.02957) - A simulacrum of hospital with evolvable medical agents.

### Courses & Tutorials

- [DeepLearning.AI — AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) - Short course on building agents with LangGraph.
- [DeepLearning.AI — Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/) - Course on building multi-agent systems.
- [DeepLearning.AI — A2A Protocol](https://www.deeplearning.ai/short-courses/a2a-the-agent2agent-protocol/) - 🆕 Free course on Google's Agent-to-Agent protocol.
- [LangChain Academy](https://academy.langchain.com/) - Free courses on LangChain, LangGraph, and agent development.
- [DeepLearning.AI Short Courses](https://www.deeplearning.ai/short-courses/) - Short AI courses covering the major frameworks / protocols.
- [Hugging Face — Building AI Agents](https://huggingface.co/learn/agents-course/) - Open course on building AI agents with open-source tools.
- [LLM Agents MOOC (Berkeley)](https://llmagents-learning.org/) - UC Berkeley course on LLM agents (root site redirects to the latest iteration).
- [Microsoft Agent Framework Docs](https://learn.microsoft.com/en-us/agent-framework/) - 🆕 Official documentation for Microsoft's unified agent framework.
- [Hugging Face Agents Course](https://github.com/huggingface/agents-course) - Free 5-unit course (notebooks + videos) on building production agents with smolagents, LangGraph, and Llama-Index. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhuggingface%2Fagents-course&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook) - Official notebooks for tool use, computer use, agent patterns, prompt engineering, and Claude Code recipes. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fanthropics%2Fanthropic-cookbook&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Google Gemini Cookbook](https://github.com/google-gemini/cookbook) - Official Gemini API examples covering grounding, function calling, multimodal, and live audio. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle-gemini%2Fcookbook&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LLM Course (Maxime Labonne)](https://github.com/mlabonne/llm-course) - End-to-end LLM curriculum from fundamentals to fine-tuning, with Colab notebooks. 79K stars. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmlabonne%2Fllm-course&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Anthropic Courses](https://github.com/anthropics/courses) - Anthropic's official educational courses on prompt engineering, real-world prompts, evals, and tool use. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fanthropics%2Fcourses&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Curated Lists

- [awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) - 💤 **Stale** (last update 2025-02). Curated list of AI autonomous agents by E2B — pre-2026 reference. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fe2b-dev%2Fawesome-ai-agents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [awesome-llm-agents](https://github.com/kaushikb11/awesome-llm-agents) - Curated list of LLM-powered agent resources. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fkaushikb11%2Fawesome-llm-agents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - 🆕 Curated list of MCP server implementations. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fpunkpeye%2Fawesome-mcp-servers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [awesome-ai-agent-papers (VoltAgent)](https://github.com/VoltAgent/awesome-ai-agent-papers) - 🆕 Curated collection of 2026 AI-agent research papers — agent engineering, memory, evaluation, workflows, autonomous systems. Updated weekly from arXiv. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FVoltAgent%2Fawesome-ai-agent-papers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [awesome-cli-coding-agents](https://github.com/bradAGI/awesome-cli-coding-agents) - 🆕 Curated directory of terminal-native AI coding agents + the harnesses that orchestrate them — open-source tools (Pi, OpenCode, Aider, Goose), platform agents (Claude Code, Codex, Gemini CLI), parallel runners, autonomous loops. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FbradAGI%2Fawesome-cli-coding-agents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🇨🇳 Chinese AI Ecosystem

*Major projects from mainland-China teams or primarily targeting the Chinese market. Listed because the China stack is increasingly its own parallel ecosystem with distinct frameworks, models, and developer culture.*

*Foundation models from Chinese labs (Qwen, DeepSeek, GLM, Doubao, Kimi, Hunyuan, ERNIE) are listed under [🧠 Foundation Models](#-foundation-models-2026) directly.*

### Agent Platforms & Frameworks

- [Dify](https://github.com/langgenius/dify) - Open-source LLM app development platform with visual agent builder. The dominant low-code agent canvas in Chinese tech. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flanggenius%2Fdify&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LobeHub](https://github.com/lobehub/lobehub) - Agent management platform (formerly Lobe Chat) — organizes agents into 7×24 operation with hiring/scheduling/reporting on your AI team. One of the highest-starred TypeScript AI projects (80K+ stars). Apache-2.0. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flobehub%2Flobehub&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Coze Loop](https://github.com/coze-dev/coze-loop) - 🆕 ByteDance's open-source agent optimization platform from the Coze team. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-loop&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentScope](https://github.com/modelscope/agentscope) - Alibaba ModelScope's multi-agent framework with visual debugging and distributed execution. Apache-2.0. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelscope%2Fagentscope&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Bisheng](https://github.com/dataelement/bisheng) - Open enterprise LLM DevOps platform: workflows, RAG, agents, fine-tuning, evals. Apache-2.0. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdataelement%2Fbisheng&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) - Multi-agent collaboration framework that assigns SOP roles (PM, architect, engineer) to LLMs. Now maintained under the FoundationAgents org. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FFoundationAgents%2FMetaGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### RAG / Knowledge

- [FastGPT](https://github.com/labring/FastGPT) - Knowledge-base-first platform on top of LLMs: data ingestion, RAG retrieval, visual workflow orchestration. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flabring%2FFastGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [QAnything](https://github.com/netease-youdao/QAnything) - 💤 NetEase Youdao's question-answering engine over arbitrary local documents (PDF/Word/Excel/PPT). ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fnetease-youdao%2FQAnything&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAGFlow](https://github.com/infiniflow/ragflow) - Deep-document-understanding RAG engine — strong on scanned PDFs, tables, and charts. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Finfiniflow%2Fragflow&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LightRAG](https://github.com/HKUDS/LightRAG) - HKU Data Science Lab's lightweight graph-based RAG engine. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2FLightRAG&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Personal & Productivity

- [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) - Open-source Notion alternative with AI workspace agents. AGPL-3.0. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAppFlowy-IO%2FAppFlowy&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Manus AI](https://manus.im/) - General-purpose autonomous agent by Butterfly Effect (Chinese-founded, relocated to Singapore). **Acquired by Meta for ~$2B (announced Dec 30, 2025)** — manus.im now says "Manus is now part of Meta."
- [Coze (扣子)](https://www.coze.cn/) - ByteDance's no-code agent builder. Mainland-only consumer surface; international counterpart is coze.com.
- [Qwen App (千问)](https://www.qwen.ai/) - Alibaba's mass-market consumer agent (rebranded from Tongyi Qianwen), integrated across Taobao / DingTalk / Quark.
- [Doubao Agents](https://www.doubao.com/) - ByteDance's flagship consumer assistant on top of the Doubao model family.

### Developer Tools

- [Trae](https://www.trae.ai/) - ByteDance's AI IDE and "10x AI coding engineer" — the highest-profile Chinese challenger to Cursor.
- [CoderPlan](https://coderplan.ai/) - China-first unified LLM API gateway (Claude / OpenAI / Gemini, one-line config for Claude Code). Pay-as-you-go with Alipay & WeChat Pay.
- [Cherry Studio](https://github.com/CherryHQ/cherry-studio) - Most-installed open-source desktop client for LLMs in Chinese dev circles — multi-provider chat with knowledge base. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FCherryHQ%2Fcherry-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code) - 🆕 **June 6, 2026**. Moonshot AI's terminal coding agent (MIT, TypeScript) — built-in coder / explore / plan sub-agents in isolated contexts, conversational MCP setup. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FMoonshotAI%2Fkimi-code&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Qwen Code](https://github.com/QwenLM/qwen-code) - Alibaba Qwen team's open-source terminal coding agent — agent teams, auto-memory, IDE integrations, multi-provider (OpenAI / Anthropic / Gemini / Qwen). 26K+ stars. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FQwenLM%2Fqwen-code&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Coze Studio](https://github.com/coze-dev/coze-studio) - 🆕 ByteDance's open-source counterpart to Coze.com — all-in-one visual agent builder with debugging and deployment tools. Apache-2.0, 20K+ stars. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ScienceOne 100 / 磐石100](https://english.cas.cn/newsroom/cas-in-media/202604/t20260429_1158251.shtml) - 🆕 Chinese Academy of Sciences scientific reasoning agent system, 50+ CAS institutes, 2,000+ research tools.

---

## 📝 Compare — Side-by-Side Tables

*Quick decision matrices for the most common "which one do I pick?" questions in 2026.*

### 🏗️ Agent Frameworks

| Framework | Language | Multi-Agent | State / Graph | Streaming | License | Best For |
|-----------|----------|------------|---------------|-----------|---------|----------|
| [LangGraph](https://github.com/langchain-ai/langgraph) | Python / JS | ✅ native | ✅ first-class | ✅ | MIT | Production stateful workflows |
| [CrewAI](https://github.com/crewAIInc/crewAI) | Python | ✅ role-based | ⚠️ task graph | ✅ | MIT | Role-playing agent teams |
| [AutoGen / Microsoft Agent Framework](https://github.com/microsoft/autogen) | Python / .NET | ✅ conversational | ⚠️ group chat | ✅ | CC-BY-4.0 / MIT | Enterprise multi-agent chat |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | Python | ✅ handoffs | ❌ | ✅ | MIT | OpenAI-native production |
| [Mastra](https://github.com/mastra-ai/mastra) | TypeScript | ✅ | ✅ workflows | ✅ | Elastic-2.0 | TypeScript-first stack |
| [Google ADK](https://github.com/google/adk-python) | Python / Java | ✅ hierarchical | ⚠️ | ✅ | Apache-2.0 | Gemini + Vertex AI |
| [DSPy](https://github.com/stanfordnlp/dspy) | Python | ⚠️ via modules | ⚠️ programmatic | ✅ | MIT | Programmatic prompt optimization |
| [Agno (ex-Phidata)](https://github.com/agno-agi/agno) | Python | ✅ teams | ❌ | ✅ | MPL-2.0 | Multi-modal agents w/ memory |

### 🧪 Sandboxes (running agent-generated code)

| Sandbox | Hosting | Cold Start | Languages | Persistence | License | Best For |
|---------|---------|-----------|-----------|-------------|---------|----------|
| [E2B](https://github.com/e2b-dev/E2B) | Cloud (managed) | ~150ms | Python / Node / shell | per-session | Apache-2.0 | OpenAI Agents SDK / production |
| [Daytona](https://github.com/daytonaio/daytona) | Cloud / self-host | ~500ms | Polyglot | persistent workspaces | AGPL-3.0 | Long-running dev tasks |
| [Modal](https://modal.com/) | Cloud (managed) | ~200ms | Python | function-scoped | proprietary | GPU + serverless agents |
| [Microsandbox](https://github.com/superradcompany/microsandbox) | Local microVM | ~100ms | Polyglot | per-session | Apache-2.0 | Privacy-first local dev |
| [SandboxFusion](https://github.com/bytedance/SandboxFusion) | Self-host | ~300ms | 20+ languages | ephemeral | Apache-2.0 | Eval / benchmark pipelines |

### 🌐 Browser-Use Stacks

| Stack | Approach | Hosting | Strengths | License |
|-------|----------|---------|-----------|---------|
| [Browser Use](https://github.com/browser-use/browser-use) | Vision + DOM, Playwright | Self-host | Largest community, MIT, 92K stars | MIT |
| [Stagehand](https://github.com/browserbase/stagehand) | Typed `act/extract/observe` | Browserbase or self | Strong typing, structured output | MIT |
| [Steel Browser](https://github.com/steel-dev/steel-browser) | Headless API | Self-host or cloud | Sessions + proxy + captcha | Apache-2.0 |
| [Skyvern](https://github.com/Skyvern-AI/skyvern) | Vision-first | Self-host | Robust to dynamic pages | AGPL-3.0 |
| [AgentQL](https://github.com/tinyfish-io/agentql) | Query language | SDK + self-host | Semantic selectors | MIT |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | MCP-native | Self-host | Drop-in MCP tool for any client | Apache-2.0 |

### 📊 Eval & Observability

| Tool | Self-host | OpenTelemetry | Eval Suite | Prompt Mgmt | License |
|------|-----------|---------------|-----------|-------------|---------|
| [Langfuse](https://github.com/langfuse/langfuse) | ✅ | ✅ | ✅ | ✅ | MIT |
| [Helicone](https://github.com/Helicone/helicone) | ✅ | ✅ | ⚠️ basic | ✅ | Apache-2.0 |
| [Arize Phoenix](https://github.com/Arize-ai/phoenix) | ✅ | ✅ | ✅ | ⚠️ | Elastic-2.0 |
| [LangSmith](https://www.langchain.com/langsmith) | ❌ (cloud only) | ✅ | ✅ | ✅ | proprietary |
| [Braintrust](https://www.braintrust.dev/) | ❌ (cloud only) | ✅ | ✅ | ✅ | proprietary |
| [DeepEval](https://github.com/confident-ai/deepeval) | ✅ (library) | ⚠️ via Confident | ✅ | ❌ | Apache-2.0 |
| [Agenta](https://github.com/agenta-ai/agenta) | ✅ | ✅ | ✅ | ✅ | Apache-2.0 |
| [OpenLLMetry](https://github.com/traceloop/openllmetry) | ✅ (instrumentation) | ✅ native | ❌ | ❌ | Apache-2.0 |

### 💻 Coding Agents — Headline Picks

| Tool | Surface | Open Source | Free Tier | SWE-bench | Best For |
|------|---------|-------------|-----------|-----------|----------|
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | CLI / IDE | ❌ | ⚠️ Pro plan | 80.9% | Long-horizon engineering |
| [Codex CLI](https://github.com/openai/codex) | CLI | ✅ | ✅ | n/a (Terminal-Bench 77.3%) | OpenAI-native shells |
| [Cursor](https://www.cursor.com/) | IDE | ❌ | ✅ (limited) | n/a | Pair-programming UX |
| [Cline](https://github.com/cline/cline) | VS Code ext | ✅ | ✅ (BYO key) | n/a | OSS IDE alternative |
| [Aider](https://github.com/Aider-AI/aider) | CLI | ✅ | ✅ (BYO key) | strong on Polyglot | Git-aware refactors |
| [Devin 3.0](https://www.cognition.ai/) | Cloud | ❌ | ❌ | leading | Hands-off long tasks |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | Self-host | ✅ | ✅ | competitive | Self-hosted SWE agent |

*Tables verified 2026-07-17. Send PRs with sources when figures change.*

---

### 💰 Foundation Models — API Cost & Context

*Prices in USD per 1M tokens. Data: 2026-07-17.*

| Model | Provider | Context Window | Input $/1M | Output $/1M | Best For |
|-------|----------|---------------|-----------|------------|----------|
| GPT-5.6 Sol | OpenAI | 1M | $5.00 | $30.00 | Frontier reasoning flagship |
| GPT-5.6 Terra | OpenAI | 1M | $2.50 | $15.00 | Cost-efficient production workloads |
| GPT-5.6 Luna | OpenAI | 1M | $1.00 | $6.00 | High-volume, speed-critical tasks |
| GPT-4o | OpenAI | 128K | $2.50 | $10.00 | Broad tool-use, vision, broad ecosystem |
| GPT-4o-mini | OpenAI | 128K | $0.15 | $0.60 | High-volume simple tasks |
| Claude Sonnet 5 | Anthropic | 1M | $2.00 (intro) | $10.00 (intro) | Default agentic workhorse ($3/$15 after Aug 31, 2026) |
| Claude Opus 4.8 | Anthropic | 1M | $5.00 | $25.00 | Hardest reasoning tasks |
| Claude Fable 5 | Anthropic | 1M | $10.00 | $50.00 | Mythos-class frontier tasks |
| Claude Haiku 4.5 | Anthropic | 1M | $1.00 | $5.00 | Fast Anthropic-ecosystem tasks |
| Gemini 3.1 Pro | Google | 1M | $2.00 | $12.00 | Flagship reasoning, multimodal |
| Gemini 2.5 Flash | Google | 1M | $0.30 | $2.50 | Cost-effective multimodal |
| Gemini 2.5 Pro | Google | 1M | $1.25 | $10.00 | Long-context, multimodal |
| Gemini 2.5 Flash-Lite | Google | 1M | $0.10 | $0.40 | Ultra-cheap high-volume |
| DeepSeek V4-Flash | DeepSeek | 1M | $0.14 | $0.28 | Budget-friendly coding + reasoning |
| Qwen3 235B A22B | Alibaba | 131K | ~$0.29 | ~$1.15 | Best Chinese + coding, MoE |
| Kimi K2.6 | Moonshot AI | 262K | $0.95 | $4.00 | Chinese + long-context tasks |
| Grok 4 | xAI | 256K | $3.00 | $15.00 | X/Twitter integration, reasoning |
| Grok 4.5 | xAI | 500K | $2.00 | $6.00 | Coding + agentic flagship |

*Sources: Anthropic, OpenAI, Google, DeepSeek, Alibaba, Moonshot, xAI official pricing pages — July 2026.*

---

### 💻 Foundation Models — Local Deployment

*Estimated VRAM at Q4_K_M quantization. Speed varies by hardware.*

| Model | Params | Min VRAM (Q4) | Speed (tok/s)* | Best Quantization | Chinese Support | Best For |
|-------|--------|--------------|----------------|-------------------|-----------------|----------|
| Qwen3.6-27B | 27B dense | ~17 GB | ~23 (M5 Max) | Q4_K_M / FP8 | ⭐⭐⭐⭐⭐ | Coding, Chinese, agentic tasks |
| Qwen3 235B A22B | 235B MoE | ~40 GB (active) | ~15–20 | Q2_K / Q4_K_M | ⭐⭐⭐⭐⭐ | Best local quality, huge context |
| Llama 3.3 70B | 70B dense | ~42 GB | ~12–18 | Q4_K_M | ⭐⭐☆☆☆ | Best English open-weight |
| DeepSeek V3-671B | 671B MoE | ~40 GB (active) | ~10–15 | Q2_K | ⭐⭐⭐⭐☆ | Open-weight coding champion |
| Gemma 4 27B | 27B dense | ~17 GB | ~20–25 | Q4_K_M | ⭐⭐⭐☆☆ | Multilingual reasoning, Apache-2.0 |
| Phi-4 14B | 14B dense | ~9 GB | ~35–45 | Q4_K_M | ⭐⭐☆☆☆ | Best 8–16GB VRAM coding model |
| Mistral Small 4 24B | 24B dense | ~14 GB | ~25–30 | Q4_K_M | ⭐⭐⭐☆☆ | Multilingual, function calling |

*\* tok/s measured at typical decode context; varies with hardware, context length, and batch size.*

---

### 🧠 Agent Memory Systems

| System | Storage | Retrieval | Local | Self-host | Temporal | License | Best For |
|--------|---------|-----------|-------|-----------|----------|---------|----------|
| [Mem0](https://github.com/mem0ai/mem0) | Vector + Graph | Semantic | ✅ | ✅ | ✅ | Apache-2.0 | Drop-in memory for any LLM app |
| [Basic Memory](https://github.com/basicmachines-co/basic-memory) | Markdown files | Keyword + embedding | ✅ | ✅ | ⚠️ | MIT | Human-readable, Obsidian-compatible |
| [Graphiti](https://github.com/getzep/graphiti) | Temporal knowledge graph | Graph traversal | ✅ | ✅ | ⭐ native | Apache-2.0 | Time-aware agent memory |
| [Zep](https://github.com/getzep/zep) | Vector + summary | Semantic | ✅ | ✅ | ✅ | Apache-2.0 | Production memory for chat agents |
| [Memary](https://github.com/kingjulio8238/Memary) | Knowledge graph | Graph + semantic | ✅ | ✅ | ⚠️ | MIT | Open-source agent memory layer |
| [TheAgentCompany](https://github.com/TheAgentCompany/TheAgentCompany) | Episodic + semantic | Hybrid | ✅ | ✅ | ✅ | Apache-2.0 | Benchmark + agent environment for enterprise software tasks |
| [Letta (fka MemGPT)](https://github.com/cpacker/MemGPT) | Tiered (core/archival) | Paged retrieval | ✅ | ✅ | ✅ | Apache-2.0 | Long-term memory with infinite context illusion |

---

### 🎙️ Voice & Audio Models

| Model / Service | STT | TTS | Realtime | Local | Latency | Languages | License |
|----------------|-----|-----|---------|-------|---------|-----------|--------|
| [ElevenLabs v3](https://elevenlabs.io/) | ❌ | ⭐⭐⭐⭐⭐ | ✅ | ❌ | ~200ms | 70+ | Proprietary |
| [Whisper v3 (local)](https://github.com/openai/whisper) | ⭐⭐⭐⭐★ | ❌ | ❌ | ✅ | ~1s (large) | 99 | MIT |
| [Deepgram Nova-3](https://deepgram.com/) | ⭐⭐⭐⭐⭐ | ✅ | ✅ | ❌ | <100ms | 45+ | Proprietary |
| [Gemini Live API](https://ai.google.dev/) | ✅ | ✅ | ⭐ native | ❌ | <300ms | 30+ | Proprietary |
| [OpenAI Realtime API](https://platform.openai.com/) | ✅ | ✅ | ⭐ native | ❌ | ~300ms | 57 | Proprietary |
| [MiniMax TTS](https://www.minimax.io/) | ❌ | ⭐⭐⭐⭐☆ | ✅ | ❌ | ~200ms | 20+ | Proprietary |
| [Kokoro](https://github.com/hexgrad/kokoro) | ❌ | ⭐⭐⭐⭐☆ | ❌ | ✅ | ~100ms | 8 | Apache-2.0 |
| [Voxtral](https://mistral.ai/) | ⭐⭐⭐⭐☆ | ❌ | ❌ | ✅ | batch | 20+ | Apache-2.0 |

---

### 🎨 Image Generation Models

| Model | Max Resolution | API / Local | Photorealism | Best For | Pricing (approx) |
|-------|---------------|-------------|-------------|----------|------------------|
| [DALL-E 3](https://developers.openai.com/api/docs/guides/image-generation) | 1024×1024 | API | High | Instruction-following, broad | $0.04/image (std) |
| [gpt-image-2](https://developers.openai.com/api/docs/models/gpt-image-2) | 2048×2048 | API | Very high | API workflows, 4K output | $0.04–$0.17/image |
| [Flux 2 Pro](https://blackforestlabs.ai/) | 2K+ | API | ⭐ high | Photorealistic, fast generation | ~$0.05/image |
| [Midjourney V8.1](https://www.midjourney.com/) | 2K+ | Web only | Artistic | Best artistic quality | $10–$120/mo plan |
| [Stable Diffusion 3.5](https://stability.ai/) | 2K | Local + API | Good | Open-weight, self-hostable | Open weights (Stability AI Community License) |
| [Ideogram 3](https://ideogram.ai/) | 2K | API + Web | Good | Typography + text in images | Freemium |
| [Gemini 3 Pro Image](https://deepmind.google/) | 1K | API | High | Native multimodal edit | Vertex AI pricing |

---

### 🎥 Video Generation Models

| Model | Max Length | Resolution | API / Local | Best For | Status (2026-05) |
|-------|-----------|-----------|-------------|----------|------------------|
| [Veo 3.1](https://deepmind.google/technologies/veo/) | 2 min | 4K | API (Vertex) | Highest fidelity, physics-aware | GA (Google) |
| [Kling VIDEO 3.0](https://kling.ai/) | 3 min | 1080p | API + Web | Cinematic style, leading post-Sora | GA (Kuaishou) |
| [Runway Gen-4](https://runwayml.com/) | 10s/clip | 1080p | API + Web | Precise motion control, professional | GA |
| [Pika 2.0](https://pika.art/) | 10s | 1080p | Web | Creative / social media | GA |
| [Seedance 2.0](https://bytedance.com/) | 60s | 2K | API | Fast, cost-effective, social media | GA (ByteDance) |
| [Hailuo 02](https://hailuoai.video/) | 60s | 1080p | Web + API | Smooth motion, accessible | GA (MiniMax) |
| ~~Sora~~ | ❌ | ❌ | ❌ | — | **Discontinued Apr 2026** |

---

### 🔍 RAG Frameworks

| Framework | Language | Vector DB | Hybrid Search | Streaming | License | Best For |
|-----------|---------|-----------|--------------|-----------|---------|----------|
| [LlamaIndex](https://github.com/run-llama/llama_index) | Python | Any | ✅ | ✅ | MIT | Production RAG, document pipelines |
| [Haystack](https://github.com/deepset-ai/haystack) | Python | Any | ✅ | ✅ | Apache-2.0 | Pipelines, search-heavy RAG |
| [LangChain LCEL](https://docs.langchain.com/oss/python/langchain/overview) | Python / JS | Any | ✅ | ✅ | MIT | Flexible chaining, large ecosystem |
| [RAGFlow](https://github.com/infiniflow/ragflow) | Python | Built-in | ✅ | ✅ | Apache-2.0 | Deep document parsing, OCR-aware |
| [Cognee](https://github.com/topoteretes/cognee) | Python | Vector + Graph | ✅ | ⚠️ | Apache-2.0 | Knowledge graph + RAG hybrid |
| [txtai](https://github.com/neuml/txtai) | Python | Built-in | ✅ | ❌ | Apache-2.0 | Lightweight, embeddings-first |
| [Verba](https://github.com/weaviate/Verba) | Python | Weaviate | ⚠️ | ❌ | BSD-3 | 📦 Archived — Weaviate-native RAG chatbot |

---

### 🗄️ Vector Databases

| Database | Self-host | Cloud | Scale | Hybrid Search | License | Best For |
|----------|-----------|-------|-------|--------------|---------|----------|
| [Qdrant](https://github.com/qdrant/qdrant) | ✅ | ✅ | Very large | ✅ | Apache-2.0 | Best all-round OSS vector DB |
| [Weaviate](https://github.com/weaviate/weaviate) | ✅ | ✅ | Large | ✅ | BSD-3 | Multi-modal, GraphQL API |
| [Pinecone](https://www.pinecone.io/) | ❌ | ✅ | Very large | ✅ | Proprietary | Managed, easiest setup |
| [Chroma](https://github.com/chroma-core/chroma) | ✅ | ⚠️ | Medium | ❌ | Apache-2.0 | Fast prototyping, Python-native |
| [Milvus](https://github.com/milvus-io/milvus) | ✅ | ✅ | Very large | ✅ | Apache-2.0 | Billion-scale production |
| [pgvector](https://github.com/pgvector/pgvector) | ✅ | ✅ | Medium | ⚠️ | PostgreSQL | Existing Postgres stack |
| [FAISS](https://github.com/facebookresearch/faiss) | ✅ | ❌ | Large | ❌ | MIT | In-memory, GPU-accelerated search |

---

### 📱 Personal AI Assistants (2026)

| Tool | Open Source | Local LLM | Memory | Multi-channel | Self-host | Best For |
|------|------------|-----------|--------|--------------|-----------|----------|
| [OpenClaw](https://github.com/openclaw/openclaw) | ✅ | ✅ | ✅ native | ✅ (TG/Discord/WA) | ✅ | All-in-one personal agent platform |
| [Khoj](https://github.com/khoj-ai/khoj) | ✅ | ✅ | ✅ | ⚠️ (web/app) | ✅ | Research, notes, calendar integration |
| [Jan.ai](https://github.com/janhq/jan) | ✅ | ✅ | ❌ | ❌ | ✅ | Offline ChatGPT replacement, GUI |
| [LM Studio](https://lmstudio.ai/) | ❌ | ✅ | ❌ | ❌ | ✅ | Easy local model runner, non-technical |
| [Perplexity](https://www.perplexity.ai/) | ❌ | ❌ | ⚠️ | ❌ | ❌ | Search-first, cited answers |
| [Claude.ai Pro](https://claude.ai/) | ❌ | ❌ | ✅ Projects | ❌ | ❌ | Best reasoning, MCP tools |
| [Zo Computer](https://zo.computer/) | ❌ | ❌ | ✅ | ❌ | ❌ | Autonomous computer use assistant |

---

### 🔌 MCP Servers — Top Integrations

*Stars data approximate, 2026-05.*

| MCP Server | Category | Stars | Auth | Security Audit | License |
|-----------|----------|-------|------|---------------|--------|
| [GitHub MCP](https://github.com/github/github-mcp-server) | Dev / Code | 🔥 High | OAuth | ✅ (GitHub) | MIT |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | Browser | 🔥 High | None (local) | ⚠️ | Apache-2.0 |
| [Filesystem MCP](https://github.com/modelcontextprotocol/servers) | Files | 🔥 High | None (local) | ⚠️ sandboxing | MIT |
| [Brave Search MCP](https://github.com/modelcontextprotocol/servers) | Search | High | API key | ❌ | MIT |
| [Slack MCP](https://github.com/modelcontextprotocol/servers) | Comms | Medium | OAuth | ❌ | MIT |
| [Notion MCP](https://github.com/modelcontextprotocol/servers) | Notes | Medium | OAuth | ❌ | MIT |
| [PostgreSQL MCP](https://github.com/modelcontextprotocol/servers) | Database | Medium | Conn string | ⚠️ read-only mode | MIT |
| [Google Maps MCP](https://github.com/modelcontextprotocol/servers) | Location | Medium | API key | ❌ | MIT |

*Use **mcp-scan** (Invariant Labs) to audit any MCP server before production deployment.*

---

### 🏢 Enterprise AI Agent Platforms

| Platform | Open Source | MCP Support | A2A Support | Self-host | Compliance | Best For |
|---------|------------|------------|------------|-----------|-----------|----------|
| [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/) | ⚠️ (AutoGen OSS) | ✅ | ✅ | ⚠️ (Azure) | SOC2, ISO 27001 | Azure-native enterprise |
| [Salesforce Agentforce](https://www.salesforce.com/agentforce/) | ❌ | ⚠️ | ❌ | ❌ | SOC2, GDPR | Salesforce CRM orgs |
| [SAP Joule](https://www.sap.com/products/artificial-intelligence/ai-assistant.html) | ❌ | ❌ | ❌ | ⚠️ | SOC2, ISO | SAP ERP environments |
| [Google Gemini Enterprise](https://workspace.google.com/features/) | ❌ | ✅ | ✅ | ❌ (cloud) | SOC2, FedRAMP | Google Workspace orgs |
| [IBM watsonx](https://www.ibm.com/watsonx) | ⚠️ | ✅ | ⚠️ | ✅ (on-prem) | FedRAMP, HIPAA | Regulated / on-prem enterprise |
| [ServiceNow AI Agents](https://www.servicenow.com/) | ❌ | ✅ | ⚠️ | ❌ | SOC2 | IT service management |
| [Dify Enterprise](https://github.com/langgenius/dify) | ✅ (CE) | ✅ | ✅ | ✅ | SOC2 (cloud) | Multi-model, low-code agent platform |

---

### 📏 Embedding Models

*MTEB = Massive Text Embedding Benchmark leaderboard score (EN, 2026-05 approx).*

| Model | Dims | Context | Local | API | Languages | License | MTEB ≈ |
|-------|------|---------|-------|-----|-----------|---------|--------|
| [OpenAI text-embedding-3-large](https://platform.openai.com/docs/guides/embeddings) | 3072 | 8K | ❌ | ✅ | Multi | Proprietary | ~64 |
| [Cohere embed-v4](https://cohere.com/embed) | 1024 | 512 | ❌ | ✅ | Multi | Proprietary | ~66 |
| [Gemini gemini-embedding-2](https://ai.google.dev/gemini-api/docs/embeddings) | 3072 | 8K | ❌ | ✅ | Multi | Proprietary | — |
| [BGE-M3](https://github.com/FlagOpen/FlagEmbedding) | 1024 | 8K | ✅ | ❌ | Multi | MIT | ~65 |
| [Jina-embeddings-v3](https://github.com/jina-ai/jina) | 1024 | 8K | ✅ | ✅ | Multi | CC-BY-NC | ~65 |
| [Nomic-embed-text-v2](https://github.com/nomic-ai/nomic) | 768 | 8K | ✅ | ✅ | Multi | Apache-2.0 | ~62 |
| [Voyage-3](https://www.voyageai.com/) | 1024 | 32K | ❌ | ✅ | Multi | Proprietary | ~67 |

---

### 🛡️ Agent Security Tools

| Tool | MCP Scan | Prompt Injection Defense | Audit Logs | Self-host | License |
|------|---------|------------------------|-----------|-----------|--------|
| [mcp-scan](https://github.com/invariantlabs-ai/mcp-scan) | ⭐ native | ✅ | ❌ | ✅ | MIT |
| [Lakera Guard](https://www.lakera.ai/) | ❌ | ⭐⭐⭐⭐⭐ | ✅ | ❌ | Proprietary |
| [Zenity](https://www.zenity.io/) | ✅ | ✅ | ✅ | ❌ | Proprietary |
| [Prompt Armor](https://promptarmor.com/) | ❌ | ⭐⭐⭐⭐☆ | ✅ | ❌ | Proprietary |
| [Azure AI Content Safety](https://azure.microsoft.com/en-us/products/ai-services/ai-content-safety) | ❌ | ✅ | ✅ | ❌ (Azure) | Proprietary |
| [Rebuff](https://github.com/protectai/rebuff) | ❌ | ⭐⭐⭐⭐☆ | ❌ | ✅ | MIT |

---

### 🖥️ Computer Use & Desktop Agents

| Tool | OS | Vision | Local | API | Open Source | Best For |
|------|----|----|-------|-----|------------|----------|
| [Claude Desktop Intelligence](https://www.anthropic.com/) | Mac / Linux | ✅ | ❌ | ✅ | ❌ | Best all-round screen agent |
| [UFO](https://github.com/microsoft/UFO) | Windows | ✅ | ✅ | Optional | ✅ | Windows native automation |
| [OSWorld](https://github.com/xlang-ai/OSWorld) | Mac/Win/Linux | ✅ | ✅ | Optional | ✅ | Cross-platform benchmark + agent |
| [NeMo Agent Toolkit](https://github.com/NVIDIA/NeMo-Agent-Toolkit) | Linux/Cloud | ✅ | ✅ | Optional | ✅ | NVIDIA’s open agent framework for LLM-powered workflows |
| [Screenpipe](https://github.com/mediar-ai/screenpipe) | Mac / Linux | ✅ | ✅ | ❌ | ✅ | Screen + audio memory, privacy-first |
| [Claude Computer Use (API)](https://docs.anthropic.com/) | Any (via API) | ✅ | ❌ | ✅ | ❌ | API-driven desktop control |

---

### 🤖 Physical AI Platforms

| Platform | Type | Open Source | SDK | Simulation | Best For |
|---------|------|------------|-----|-----------|----------|
| [NVIDIA Isaac GR00T N1.5](https://developer.nvidia.com/isaac) | Humanoid foundation | ⚠️ (weights) | ✅ | ✅ (Isaac Sim) | Universal humanoid robot foundation model |
| [ROS 2 Jazzy](https://docs.ros.org/) | Robot OS | ✅ | ✅ | ✅ (Gazebo) | Standard robot middleware |
| [Gemini Robotics](https://deepmind.google/) | Manipulation | ❌ | ⚠️ | ✅ | Vision + language + dexterous manipulation |
| [Unitree SDK2](https://github.com/unitreerobotics) | Quadruped / Humanoid | ✅ | ✅ | ⚠️ | Go2, H1, G1 robot dev |
| [Boston Dynamics API](https://dev.bostondynamics.com/) | Quadruped | ❌ | ✅ | ❌ | Spot industrial deployment |
| [Genesis Sim](https://github.com/Genesis-Embodied-AI/Genesis) | Simulation | ✅ | ✅ | ⭐ native | Ultra-fast physics sim for embodied AI |

---

### 🇨🇳 Chinese AI Models — Head-to-Head

*Chinese language capability benchmarks are approximate. API prices in USD/1M tokens, July 2026.*

| Model | Provider | Context | Chinese Bench≈ | Coding | Open Weight | Input $/1M |
|-------|----------|---------|---------------|--------|------------|----------|
| Qwen3 235B A22B | Alibaba | 131K | Top | ⭐⭐⭐⭐⭐ | ✅ Apache-2.0 | ~$0.29 |
| DeepSeek V3.2 | DeepSeek | 128K | Very high | ⭐⭐⭐⭐⭐ | ✅ MIT | $0.14 |
| Kimi K2.6 | Moonshot AI | 262K | High | ⭐⭐⭐⭐☆ | ❌ | ~$0.95 |
| GLM-5.2 | Zhipu AI | 1M | High | ⭐⭐⭐⭐☆ | ✅ MIT | ~$0.50 |
| Hunyuan Pro | Tencent | 256K | High | ⭐⭐⭐⭐☆ | ❌ | ~$0.45 |
| Doubao Pro 256K | ByteDance | 256K | High | ⭐⭐⭐☆☆ | ❌ | ~$0.80 |
| ERNIE 5 | Baidu | 128K | High | ⭐⭐⭐☆☆ | ❌ | ~$0.70 |

---

### 📦 Agent Frameworks — TypeScript / JavaScript

| Framework | Multi-Agent | Streaming | MCP | A2A | Stars≈ | License |
|-----------|-----------|----------|-----|-----|-------|---------|
| [Mastra](https://github.com/mastra-ai/mastra) | ✅ | ✅ | ✅ | ✅ | ~12K | Elastic-2.0 |
| [Vercel AI SDK](https://github.com/vercel/ai) | ⚠️ | ✅ | ✅ | ❌ | ~12K | Apache-2.0 |
| [LangChain.js](https://github.com/langchain-ai/langchainjs) | ✅ | ✅ | ✅ | ❌ | ~14K | MIT |
| [Genkit](https://github.com/firebase/genkit) | ✅ | ✅ | ✅ | ❌ | ~3K | Apache-2.0 |
| [OpenAI Agents SDK (Node)](https://github.com/openai/openai-agents-js) | ✅ | ✅ | ✅ | ❌ | ~2K | MIT |
| [Rivet](https://github.com/Ironclad/rivet) | ✅ | ✅ | ⚠️ | ❌ | ~4K | MIT |
| [Flowise](https://github.com/FlowiseAI/Flowise) | ✅ | ✅ | ✅ | ❌ | ~35K | Apache-2.0 |

---

### 📊 Meta-Comparison — Orchestration vs Framework vs IDE

| Category | Example Tools | Best For | Abstraction Level | Flexibility |
|---------|--------------|----------|--------------------|-------------|
| **Orchestration Platform** | Dify, n8n, Flowise, Langflow | Non-engineers, fast deployment | Very high | Low-medium |
| **Agent Framework** | LangGraph, CrewAI, Mastra, OpenAI Agents SDK | Engineers building custom agents | Medium | High |
| **Agent IDE / Coding Agent** | Claude Code, Cursor, Cline, Devin | Developers pair-programming | Low | Very high |
| **Low-code Builder** | Voiceflow, Botpress, Microsoft Copilot Studio | Business / product teams | Very high | Low |
| **AI-native App Platform** | Vertex AI Agent Builder, Azure AI Foundry | Enterprise with managed infra | High | Medium |

---

### 📱 Mobile AI Frameworks

| Framework | iOS | Android | Local LLM | On-device Inference | License | Best For |
|-----------|-----|---------|-----------|--------------------|---------|-----------|
| [MLX](https://github.com/ml-explore/mlx) | ✅ | ❌ | ✅ | ⭐ Apple Silicon | MIT | Apple-native, fast LLM on Mac/iPhone |
| [llama.cpp (mobile)](https://github.com/ggerganov/llama.cpp) | ✅ | ✅ | ✅ | ✅ (arm/x86) | MIT | Universal local LLM, all platforms |
| [MediaPipe](https://github.com/google-ai-edge/mediapipe) | ✅ | ✅ | ✅ | ✅ | Apache-2.0 | On-device ML tasks (vision, NLP) |
| [Core ML](https://developer.apple.com/documentation/coreml) | ✅ | ❌ | ✅ | ✅ (ANE) | Apple SDK | iOS/macOS native model inference |
| [Google AI Edge](https://developers.google.com/edge) | ✅ | ✅ | ✅ | ✅ | Apache-2.0 | LiteRT + Gemma Nano on-device |
| [Ollama (mobile proxy)](https://ollama.com/) | ⚠️ via API | ⚠️ via API | ✅ | ❌ (server-side) | MIT | Run Ollama server, hit from mobile |
| [Qualcomm AI Hub](https://aihub.qualcomm.com/) | ❌ | ✅ | ✅ | ✅ (Snapdragon NPU) | SDK | Snapdragon-optimized model deployment |

*All Compare tables data: 2026-07-17. Send PRs with sources when figures change.*

---

## 🗺️ Scenario Guide — What Should I Use For…

*50+ curated scenarios matching your goal to the right tool or stack. Updated weekly.*

---

### 🏗️ Building: Coding Agents

**I want to build a coding agent for my startup (lowest cost, high quality)**
→ **Claude Code** (CLI) + **E2B** sandbox + **Langfuse** observability. SWE-bench 80.9%. ~$200/mo at moderate usage.

**I want an enterprise coding agent with security controls**
- **GitHub Copilot Enterprise** — Deep GitHub integration, IP indemnity, SSO/SAML, SOC 2. → best if already on GitHub Enterprise
- **Cursor Business** — Privacy mode, code never leaves your infra, admin dashboard. → best for teams needing IDE-first UX
- **Devin 3.0** (Cognition) — Fully autonomous PR-to-merge with re-planning. → best for hands-off long-horizon tasks

**I want an open-source self-hosted coding agent (no vendor lock-in)**
- **OpenHands** (All-Hands-AI) — MIT, competitive SWE-bench, BYO model. → best if you need full control
- **Cline** (VS Code ext) — BYO key, large community, free. → best for VS Code users
- **Aider** — Git-aware CLI refactoring, excellent polyglot support. → best for terminal-based git workflows

**I want a browser automation / web scraping agent**
- **Browser Use** — 92K stars, vision + DOM, MIT. → best for general web automation
- **Stagehand** (Browserbase) — Typed `act/extract/observe` API, structured output. → best for reliability-critical scraping
- **Skyvern** — Vision-first, handles dynamic pages without CSS selectors. → best for changing / heavily JS-rendered sites

**I want a document processing / PDF analysis agent**
→ **LlamaIndex** (document pipeline) + **Gemini 2.5 Pro** (2M context) or **Claude Opus 4.7** (200K, best reasoning) + **Unstructured.io** for ingestion. For local: **Ollama** + **Qwen3.6-27B**.

**I want a customer service / support agent**
- **Dify** — No-code LLM workflow builder, self-hostable, RAG built-in. → best for non-technical teams
- **LangGraph** + **Zendesk MCP** — Stateful workflows, ticket resolution loop. → best for engineering-led teams
- **Salesforce Agentforce** — CRM-native, works within existing Salesforce data. → best for Salesforce-first orgs

**I want a research / deep-research agent**
→ **Perplexity Deep Research** (managed) or **OpenDevin / OpenHands** + **Tavily Search** + **Claude Opus 4.7**. For local: **Khoj** (self-hosted). Expect multi-minute runs and $1–5 per deep report at cloud rates.

**I want a data analysis / BI agent**
- **Julius AI** / **Code Interpreter (ChatGPT)** — Managed, no setup. → best for analysts without eng support
- **[AI for Database](https://aifordatabase.com)** — ⚠️ Unverified. Plain-English queries over Postgres / MySQL / MongoDB / SQL Server / SQLite + Sheets, with self-refreshing dashboards and Slack/webhook/email triggers; SOC 2 + GDPR, self-host option, $19/mo Pro. → best for non-technical teams that need direct DB access without SQL
- **LangChain** + **Pandas Agent** + **Langfuse** — Fully custom, code-gen for queries. → best for eng teams with custom data
- **Metabase AI** / **Tableau Pulse** — Embedded BI copilot. → best inside existing BI stack

**I want a computer use / desktop automation agent**
- **Claude Desktop Intelligence** (Anthropic) — Screen-aware, controls any GUI app. → best all-around for macOS/Linux
- **UFO** (Microsoft, open-source) — Windows-native, Win32 + UI Automation APIs. → best for Windows automation
- **Screenpipe** — Continuous screen + audio recording + local LLM inference. → best for local privacy-first

**I want a voice / conversational agent**
- **Gemini Live API** — Real-time voice, <300ms latency, Google cloud. → best for Google ecosystem
- **OpenAI Realtime API (GPT-Realtime-2 / GPT-Live-1)** — Native voice with tool calling. → best for OpenAI ecosystem
- **LiveKit** + **Whisper** + **ElevenLabs v3** — Self-hostable voice pipeline. → best for custom, brand-specific voice

**I want a multi-agent orchestration system**
- **LangGraph** — Stateful graph workflows, best Python production option. → best for complex state machines
- **OpenAI Swarm / Agents SDK** — Lightweight handoffs, OpenAI-native. → best for simple OpenAI agent networks
- **Google ADK** — Hierarchical agent coordination, Gemini-native. → best for Google/Vertex stack
- **Mastra** (TypeScript) — Type-safe workflows, TS-first teams. → best for TypeScript stacks

**I want a personal AI assistant (self-hosted)**
- **OpenClaw** — Multi-channel (Telegram/Discord/WhatsApp), memory, cron, MCP support, full local LLM option. → best all-in-one self-hosted
- **Khoj** — Search + research + calendar, open-source, self-host. → best for knowledge workers
- **Jan.ai** / **LM Studio** — GUI-first local model runners. → best for non-technical local LLM

**I want a personal AI assistant (managed / easy setup)**
- **Claude.ai (Pro)** — Projects, memory, MCP tools, best reasoning. → best for power users
- **Perplexity Pro** — Search-first, cites sources. → best for research-heavy use
- **ChatGPT Plus** — Code interpreter, image gen, broad tools. → best for general-purpose

**I want to build a RAG application**
→ **LlamaIndex** (orchestration) + **Qdrant** (vector DB) + **Cohere embed-v4** (embeddings) + **BGE reranker** (reranking). Managed alternative: **Ragie** or **Cognee**. Production telemetry: **Langfuse**.

**I want a financial analysis agent**
→ **LangChain** + **yfinance / Alpha Vantage MCP** + **Claude Sonnet 4.6** (Excel/table reasoning) + **Langfuse**. Avoid: don’t use hallucination-prone models for numbers — always validate with structured output + code execution.

**I want a legal document agent**
→ **Claude Opus 4.7** (1M context, best contract analysis) + **LlamaIndex** (ingestion) + **pgvector** (self-hosted vector). Important: always have a human-in-the-loop for final legal decisions.

**I want an education / tutoring agent**
- **Khanmigo** (Khan Academy) — Purpose-built for K–12, COPPA-compliant. → best for K–12 safe deployment
- **Custom** with **GPT-4o** + **LangGraph** state machine + spaced repetition logic. → best for HEd or corporate training

**I want a creative writing assistant**
→ **Claude Opus 4.7** (best prose quality) or **Gemini 2.5 Pro** (long-form, 2M context) + **Notion / Obsidian MCP** for knowledge base. For structured fiction: **Sudowrite** (managed).

**I want an IoT / physical AI agent**
→ **ROS 2** (robot OS) + **NVIDIA Isaac GR00T** (humanoid foundation model) + **Genesis Sim** (simulation). For home automation: **Home Assistant** + custom LLM backend.

**I want a game playing / simulation agent**
→ **PettingZoo** (multi-agent RL env) + **Gymnasium** + **GPT-4o Vision** for game-state parsing. For LLM-in-the-loop games: **Concordia** (Google DeepMind).

**I want a security scanning / vulnerability agent**
→ **Semgrep** (static analysis) + **Claude Sonnet 4.6** (explain + triage findings) + **mcp-scan** (MCP server audit). See also: [Agent Security](#️-agent-security) table.

**I want a healthcare AI tool (non-clinical / administrative)**
→ **Claude Opus 4.7** + **RAG** on medical knowledge base + **strict output validation**. Always: disclose AI, human oversight for any clinical decision, check HIPAA/GDPR compliance. Never automate clinical diagnosis.

**I want a code review / PR security agent**
→ **CodeRabbit** (managed, instant PR reviews) or **Claude Code** in CI + **Semgrep** + custom rules. For enterprise: **Copilot Code Review** (GitHub).

**I want a social media / content creation agent**
→ **n8n** (workflow automation) + **Claude Sonnet 4.6** (drafting) + **gpt-image-2** (images) + **Buffer/Later MCP** (scheduling). Self-hosted option: all via n8n + Ollama.

**I want a translation / localization agent**
→ **DeepL API** (best quality for EU languages) or **Claude Sonnet 4.6** (nuanced context-aware) + **Weblate** (open-source TMS). For Chinese: **Qwen3 235B** + human review loop.

---

### 🧠 Model Selection

**I need the smartest model for complex multi-step reasoning**
- **Claude Opus 4.7** (/think xhigh) — Best in class for math, logic, long-horizon reasoning. $5/$25 per M tokens.
- **Gemini 2.5 Pro** — 2M context, strong multimodal, competitive pricing. $1.25/$10 per M tokens.
- **GPT-5.6 Terra** — Broadly capable, strong tool-use ecosystem. $2.50/$15 per M tokens.

**I need the fastest + cheapest model for simple, high-volume tasks**
- **Gemini 2.5 Flash-Lite** — $0.10/$0.40 per M tokens, 1M context.
- **DeepSeek V3.2** — $0.14/$0.28 per M tokens, surprisingly strong quality.
- **Claude Haiku 4.5** — $1/$5 per M tokens, Anthropic ecosystem integration.
- **GPT-5.6 Luna** — $1.00/$6.00 per M tokens, fastest GPT-5.6 tier, broad OpenAI tooling (GPT-4o-mini remains the ultra-budget legacy option at $0.15/$0.60).

**I need the best Chinese language support**
- **Qwen3 235B A22B** (Alibaba) — Strongest Chinese benchmark, MoE architecture, $0.29/$1.15 per M. → cloud API
- **Kimi K2.6** (Moonshot) — 262K context, great Chinese instruction-following. → both API + local
- **DeepSeek V3.2** — Open weights, excellent Chinese coding. → self-host or API
- **GLM-5.2** (Zhipu AI) — 1M context, MIT open weights, Chinese-first. → API or local

**I need the best local/offline model with ~16GB VRAM**
- **Qwen3.6-27B Q4_K_M** — ~17GB VRAM, ~23 tok/s, excellent coding + Chinese. Best overall 16GB pick.
- **Gemma 4 27B** (Google) — Strong reasoning, multilingual, Apache-2.0.
- **Phi-4 14B** (Microsoft) — ~9GB VRAM (Q4), punches above its weight on coding.
- **Mistral Small 4 24B** — Fast, multilingual, well-rounded.

**I need the best local/offline model with 40GB+ VRAM**
- **Llama 3.3 70B Q4_K_M** — ~42GB VRAM, strong English + coding, Llama 3.3 Community License.
- **DeepSeek V3-671B Q2** — MoE, only 40GB active params in Q2 but requires 2×A100 setup.
- **Qwen3 235B A22B Q2** — MoE flagship, 40-48GB VRAM at Q2, best local quality.

**I need the best coding capability**
→ **Claude Sonnet 4.6** (SWE-bench 80.9% via Claude Code) for agentic coding. **GPT-4o** for code generation + explanation. **DeepSeek V3.2** for open-weight coding. For IDE use: **Cursor** (Claude backend) or **Cline**.

**I need multimodal understanding (vision + text)**
- **Gemini 2.5 Pro** — Native vision, PDF, audio, video understanding. 2M context.
- **GPT-4o** — Mature vision API, strong diagram/chart understanding.
- **Claude Opus 4.7** — Best for complex document image reasoning.
- **Qwen3-VL 72B** — Best open-weight multimodal, self-hostable.

**I need very long context (500K+ tokens)**
- **Gemini 2.5 Pro** — 2M context window, best for entire codebase or book analysis.
- **Gemini 2.5 Flash** — 1M context, cheaper option.
- **Kimi K2.6** — 262K context, strong Chinese.
- **Claude Opus 4.7** — 1M context, best quality within that window.

**I need real-time voice / audio model**
- **Gemini Live API** — <300ms latency, native Google cloud.
- **OpenAI Realtime API** — GPT-Realtime-2 (May 2026), native function calling during voice.
- **ElevenLabs v3** — Best TTS quality, 70+ languages.
- **Voxtral** (Mistral) — Open-weight audio model, transcription + understanding.

**I need the best image generation**
- **gpt-image-2** (OpenAI) — Best instruction-following, 2K/4K, $0.04–0.17/image.
- **Flux 2 Pro** (Black Forest Labs) — Photorealistic, fast, API available.
- **Midjourney V8** — Best artistic quality, no API (web only).
- **Stable Diffusion 3.5** — Open weights, local deployment, Apache-2.0.

**I need the best video generation**
- **Veo 3.1** (Google) — High fidelity, physics-aware, best quality 2026.
- **Kling VIDEO 3.0** (Kuaishou) — Leading post-Sora, strong cinematic style.
- **Runway Gen-4** — Precise motion control, professional use.
- **Seedance 2.0** (ByteDance) — Fast, cost-effective, strong for social media.

**I need an open-weight model (MIT or Apache license)**
- **Llama 3.3 70B** (Meta, Llama 3.3 Community License) — Best English open-weight.
- **Qwen3 235B A22B** (Alibaba, Apache-2.0) — Best Chinese + coding open-weight.
- **Mistral Small 4** (Mistral AI, Apache-2.0) — Fast, multilingual.
- **DeepSeek V3.2** (MIT) — Best open-weight coding.
- **Gemma 4 27B** (Google, Apache-2.0) — Strong multilingual reasoning.

---

### 🏗️ Infrastructure

**I want to run everything locally (privacy-first, zero cloud)**
→ **Ollama** (model runner) + **Open WebUI** (UI) + **Qdrant** (local vector DB) + **Qwen3.6-27B** (16GB VRAM) or **Llama 3.3 70B** (40GB+). Full stack: **OpenClaw** (local mode) or **AnythingLLM**. No data leaves your machine.

**I want to minimize API costs (budget <$50/month)**
→ Use **DeepSeek V3.2** ($0.14/$0.28) or **Gemini 2.5 Flash** ($0.30/$2.50) for high-volume. Reserve **Claude Sonnet 4.6** for complex tasks only. Use **Anthropic Batch API** (50% off) for non-real-time work. Cache aggressively (prompt caching saves ~70% on repeated context).

**I want to scale to enterprise (millions of requests/month)**
→ **Google Vertex AI** (managed Gemini, auto-scale, SLAs) or **Azure OpenAI** (GPT-4o, compliance, dedicated capacity). Add **LangFuse** for observability. For routing: **PortKey** or **LiteLLM** as unified gateway.

**I want to deploy in an air-gapped / regulated environment**
→ **Ollama** (local inference) + **Qwen3 235B A22B / Llama 3.3 70B** (open weights) + **Qdrant** (local vector DB). For enterprise needs: **IBM watsonx** (on-prem) or **Azure Government** (FedRAMP). Compliance certifications matter more than model quality here.

**I want to build for edge / mobile deployment**
→ **Core ML** (Apple, iOS/macOS) + **Phi-4 14B** or **Gemma 4 2B** (quantized). For Android: **MediaPipe** + **Gemma 4**. For cross-platform: **llama.cpp** + GGUF models. Check **Qualcomm AI Hub** for Snapdragon-optimized models.

**I need multi-cloud / want to avoid vendor lock-in**
→ **LiteLLM** (unified API proxy for 100+ providers) + **LangGraph** (framework-agnostic) + provider-agnostic embeddings (**BGE-M3** open-weight). Store all state in self-hosted **Qdrant** or **Postgres+pgvector**.

**I want to self-host everything (no managed services at all)**
→ **Ollama** (models) + **Qdrant** (vectors) + **Langfuse** (observability, self-host Docker) + **n8n** (workflows) + **OpenClaw** (agent runtime). GPU recommendations: 2× RTX 4090 (24GB each = 48GB) for 70B models; single RTX 4090 for 27B.

---

### 📊 Evaluation & Monitoring

**I want to evaluate agent output quality**
→ **DeepEval** (rich metric suite: faithfulness, relevancy, hallucination) + **Langfuse** (traces + evals). For custom: **LangSmith** (tight LangChain integration). Open-source: **Agenta** (self-host).

**I want to debug why my agent is failing**
→ **Langfuse** (trace each tool call + LLM call with timing) + **Arize Phoenix** (root cause analysis). Enable verbose logging in your framework (LangGraph / CrewAI all support it). Use **LLM-as-judge** to flag low-confidence steps.

**I want to monitor production agents in real-time**
→ **Langfuse** (OpenTelemetry-native, self-host) or **Helicone** (zero-latency proxy logging). Set up cost + latency + error-rate dashboards. Alert on error spikes via **Grafana** or **Datadog** integration.

**I want to A/B test different models or prompts**
→ **Braintrust** (experiment tracking, online/offline eval) or **LangSmith** (prompt playground + evals). For open-source: **Agenta** + **Langfuse** experiments feature.

**I want to benchmark models on my specific tasks**
→ **LMSYS Chatbot Arena** custom eval + **Evals by OpenAI** (open framework) + **DeepEval** (custom metric). Run your own eval harness: prepare 50–200 golden examples, measure precision/recall on your actual task.

**I want to evaluate MCP server security**
→ **mcp-scan** (Invariant Labs) — Detects prompt injection, tool poisoning, shadow tools in MCP servers. Run before production deployment. See also: [Agent Security](#️-agent-security).

---

### 🌍 Ecosystem Choices

**I want to build within the OpenAI ecosystem**
→ **OpenAI Agents SDK** + **GPT-4o** + **E2B** sandbox + **LangSmith** eval. Benefits: widest third-party tooling, most community examples. Cost: premium pricing.

**I want to build within the Anthropic Claude ecosystem**
→ **Claude Code** (agentic IDE/CLI) + **Claude Sonnet 4.6 / Opus 4.7** + **MCP protocol** (Claude Desktop) + **Langfuse** (observability). Benefits: best coding quality, MCP is Claude-native. Cost: ~mid-tier.

**I want to build within the Google Gemini ecosystem**
→ **Google ADK** (Agent Development Kit) + **Gemini 2.5 Pro/Flash** + **Vertex AI** (deployment) + **Vertex AI Eval** + **AlloyDB / BigQuery** (data). Benefits: 2M context, multimodal, cheap Flash tier. Cost: scales well.

**I want to build for the Chinese market (domestic cloud / regulation)**
→ **Qwen3 235B** (Alibaba Cloud DashScope) + **Baidu ERNIE 5** or **Kimi K2.6** (Moonshot) as fallback + **Alibaba Cloud PAI** (deployment). All data stays within China borders. ICP-compliant.

**I want a TypeScript-first stack**
→ **Mastra** (TS workflows, MCP, A2A, Elastic-2.0) + **Vercel AI SDK** (streaming, RSC-friendly) + **Qdrant JS client** + **Langfuse JS SDK**. Alternative: **LangChain.js** + **LangGraph.js**.

**I want an open-source-only stack (zero proprietary)**
→ **Ollama** + **Llama 3.3 70B** or **DeepSeek V3.2** (model) + **LangGraph** (MIT, framework) + **Qdrant** (Apache-2.0, vector DB) + **Langfuse** (MIT, observability) + **E2B** (Apache-2.0, sandbox). Fully self-hosted, no vendor dependencies.

---

## 📋 Stack Recipes — Curated Tool Combinations

*8 battle-tested multi-tool setups for common use cases. Copy and adapt.*

| # | Recipe Name | Stack | Best For |
|---|------------|-------|----------|
| 1 | **Lean Coding Agent** | Claude Code + E2B + Langfuse | Solo dev / startup, best quality per dollar |
| 2 | **Open-Source SWE Agent** | OpenHands + Ollama + Qwen3.6-27B + Qdrant | Full local, privacy-first coding |
| 3 | **Enterprise RAG** | LlamaIndex + Qdrant + Cohere embed-v4 + Langfuse + Claude Sonnet 4.6 | Production Q&A on internal docs |
| 4 | **Voice Assistant Pipeline** | LiveKit + Whisper (STT) + Claude Sonnet 4.6 + ElevenLabs v3 (TTS) | Custom branded voice AI |
| 5 | **Browser Automation** | Browser Use + Stagehand + Claude Sonnet 4.6 + Langfuse | Reliable web scraping + form filling |
| 6 | **Local-Only Privacy Stack** | Ollama + Qwen3.6-27B + Open WebUI + Qdrant + n8n | Zero cloud, air-gapped use |
| 7 | **TypeScript Agent** | Mastra + Vercel AI SDK + Gemini 2.5 Flash + Qdrant + Langfuse | TS-first production SaaS |
| 8 | **Chinese Market Stack** | Qwen3 235B API + RAGFlow + Milvus + Langfuse | Domestic China deployment, ICP-compliant |

---

## ⚠️ Anti-Picks — What NOT to Use For…

*Avoid common mistakes. These recommendations are based on observed production failures in 2026.*

| ❌ Don’t Use | ❌ For This | ✅ Use Instead | Why |
|------------|-----------|---------------|-----|
| LangChain v0.x | New production agents | **LangGraph** | LangChain chains are deprecated; LangGraph has proper state management |
| AutoGPT (legacy) | Production workloads | **OpenHands** or **LangGraph** | AutoGPT’s 2023 architecture has poor reliability at scale |
| GPT-3.5-Turbo | Complex reasoning | **Gemini 2.5 Flash** or **Claude Haiku 4.5** | GPT-3.5 deprecated, same cost range as modern models |
| Pinecone Starter | Self-hosted / cost-sensitive | **Qdrant** or **pgvector** | Pinecone Starter tier removed 2025; OSS alternatives are cheaper |
| LLM for real-time stock trading | Financial execution | **Deterministic rule engine** | LLMs hallucinate numbers; catastrophic for live trading |
| ChatGPT Plus | Production API workflows | **OpenAI API** direct | ChatGPT Plus is consumer; no SLA, no rate control, no observability |
| Hugging Face Inference API (free) | Production load | **Modal** or **self-hosted Ollama** | Free tier has extreme rate limits, cold starts >30s |
| Autonomous agents without human-in-loop | Medical / legal decisions | Any model + **mandatory human review step** | No current model is reliable enough for high-stakes autonomous decisions |
| PDF viewer MCP for sensitive docs | Compliance environments | **Local LlamaIndex + on-prem Qdrant** | Sending sensitive PDFs to cloud MCP servers violates data residency rules |
| CrewAI for single-agent tasks | Simple one-shot tasks | **Direct API call** | CrewAI’s multi-agent overhead adds latency and cost when only one agent is needed |
| Midjourney | Programmatic / API image gen | **gpt-image-2** or **Flux 2 Pro API** | Midjourney has no public API; requires Discord bot workaround |
| GPT-4o Vision for OCR | High-accuracy document OCR | **Tesseract 5** + **Azure Document Intelligence** | LLM OCR has ~2-5% error rate; dedicated OCR is 10x cheaper and more accurate |
| Sora | Any video generation (2026) | **Kling VIDEO 3.0** or **Veo 3.1** | Sora discontinued by OpenAI, April 2026 |
| Vector DB without reranking | High-precision RAG | Vector DB + **BGE reranker** or **Cohere Rerank** | Raw vector search recall is ~70%; reranking brings it to ~90%+ |
| Gemini 2.5 Flash-Lite | Complex legal/medical reasoning | **Claude Opus 4.7** or **Gemini 2.5 Pro** | Flash-Lite optimized for speed, not accuracy on high-stakes tasks |

---

## 🌟 Notable Agent Projects of 2026

*Standout projects and developments that shaped the AI agent landscape in 2026.*

- [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol/servers) - Became the universal standard for agent-tool interoperability. Donated to Linux Foundation. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Fservers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [A2A Protocol](https://github.com/a2aproject/A2A) - Agent-to-Agent protocol (originated at Google, now Linux Foundation) enabling cross-framework agent collaboration with 150+ partners; v1.0 shipped May 2026. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fa2aproject%2FA2A&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - Anthropic's agentic coding tool became the go-to terminal-based coding agent with 80.9% SWE-bench.
- [Kiro](https://kiro.dev/) - 🆕 AWS launched an autonomous coding agent capable of managing 10 simultaneous development tasks.
- [Devin 3.0](https://www.cognition.ai/) - 🆕 Evolved to include dynamic re-planning, self-healing code, and legacy codebase migration.
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/) - 🆕 AutoGen + Semantic Kernel merged into unified enterprise agent platform.
- [OpenAI Codex CLI](https://github.com/openai/codex) - OpenAI entered the agentic coding space with an open-source terminal agent. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fcodex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Browser Use](https://github.com/browser-use/browser-use) - Breakthrough in making AI agents interact with the web naturally. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowser-use%2Fbrowser-use&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude Computer Use](https://www.anthropic.com/) - 🆕 Desktop Intelligence let Claude control any software by seeing the screen.
- [Manus AI](https://manus.im/) - General-purpose autonomous agent that can handle research, coding, and complex workflows; now part of Meta (acquired ~$2B, Dec 2025).
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) - Open-source AI software engineering platform gained massive adoption. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAll-Hands-AI%2FOpenHands&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Dify](https://github.com/langgenius/dify) - Low-code LLM agent platform reached mainstream adoption. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flanggenius%2Fdify&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cline](https://github.com/cline/cline) - VS Code autonomous coding agent with rapid community growth. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcline%2Fcline&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Mem0](https://github.com/mem0ai/mem0) - Memory layer for AI became essential component of agent architectures. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmem0ai%2Fmem0&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Sora Discontinuation](https://openai.com/) - 🆕 OpenAI shut down Sora (April 2026), signaling strategic pivot to enterprise AI and reasoning.
- [Kling VIDEO 3.0](https://kling.ai/) - 🆕 Kuaishou's video generation became the leading AI video platform post-Sora.
- [Cohere + Aleph Alpha Merger](https://siliconangle.com/2026/04/24/ai-startups-cohere-aleph-alpha-merge-600m-new-funding/) - 🆕 **April 24, 2026**. Canadian AI firm Cohere merged with Germany's Aleph Alpha at ~$20B valuation. $600M Series E from Schwarz Group. Creates transatlantic "sovereign AI" powerhouse with dual HQ in Toronto and Germany.
- [ScienceOne 100 / 磐石100](https://english.cas.cn/newsroom/cas-in-media/202604/t20260429_1158251.shtml) - 🆕 **April 28-29, 2026**. Chinese Academy of Sciences launches specialized scientific AI system. 2,000+ research tools, 50+ CAS institutes. Flagship-level scientific reasoning and agent capabilities.
- [Google Invests $40B in Anthropic](https://aibusiness.com/generative-ai/google-could-invest-another-40-billion-anthropic) - 🆕 **April 2026**. $10B initial + up to $30B contingent on performance milestones. Includes 5GW compute capacity over 5 years. Largest AI partnership investment to date.
- [OpenAI Deployment Company (DeployCo)](https://openai.com/index/openai-launches-the-deployment-company/) - 🆕 **May 11, 2026**. OpenAI spins out a $4B+ enterprise-deployment services unit (TPG / Bain Capital / Brookfield / Advent / Goldman Sachs / SoftBank + Bain & Company / Capgemini / McKinsey) and absorbs the Tomoro consulting acquisition. Signals the AI vendor race shifting toward services + Forward Deployed Engineers.
- [Anthropic ↔ SpaceX Colossus 1](https://www.siliconrepublic.com/business/anthropic-joins-forces-with-spacex-for-colossus-capacity) - 🆕 **May 6, 2026**. Anthropic takes all available capacity on the 300+ MW / 220K-GPU Colossus 1 Memphis cluster. SpaceX repositions itself as an AI infrastructure provider after its xAI acquisition; Anthropic doubles Claude Code rate limits for paid plans.
- [DeepSeek $4B state-backed round](https://www.techtimes.com/articles/316717/20260516/chinas-state-ai-fund-backs-deepseek-4-billion-round-efficiency-challenge-nvidia-dependent.htm) - 🆕 **May 16, 2026**. China's National AI Industry Investment Fund + Big Fund III + Tencent close in on a ~$4B first external round for DeepSeek at a ~$50B valuation — first known LLM investment from Big Fund III, signalling Beijing's bet on efficient open-weight frontier models and domestic silicon.
- [Pope Leo XIV → Vatican AI Commission](https://www.americamagazine.org/vatican-dispatch/2026/05/16/pope-leo-establishes-new-vatican-commission-on-artificial-intelligence/) - 🆕 **May 16, 2026**. Pope Leo XIV publishes the rescriptum establishing an inter-dicasterial Vatican commission on artificial intelligence (Dicastery for Integral Human Development coordinating, with Doctrine of the Faith, Culture & Education, Communication, Pontifical Academies for Life / Sciences / Social Sciences). One-year renewable mandate. First AI-focused encyclical expected to follow.
- [Google I/O 2026 — Gemini 3.5 + Omni + Spark + AI Ultra](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - 🆕 **May 19, 2026**. Google's biggest agent-and-AGI keynote of the year: Gemini 3.5 Flash GA (default model), Gemini Omni world-model family, Gemini Spark 24/7 personal agent with ~30+ MCP-based tool integrations, and a new **Google AI Ultra $100/mo** tier. Pichai confirms Google now processes **3.2 quadrillion tokens / month**.
- [Alibaba Cloud Summit Hangzhou — Qwen 3.7-Max + Zhenwu M890](https://www.scmp.com/tech/big-tech/article/3354212/alibaba-unveils-new-qwen-model-custom-chips-bid-become-chinas-ai-factory) - 🆕 **May 20, 2026**. Alibaba unveils Qwen 3.7-Max (agentic-coding flagship for long-horizon missions), the T-Head Zhenwu M890 AI accelerator, and a full-stack AI infrastructure upgrade — China's most aggressive bid yet to position itself as the country's "AI factory."
- [OpenAI Guaranteed Capacity (Compute Annual Pass)](https://openai.com/business/guaranteed-capacity/) - 🆕 **May 19, 2026**. Long-term enterprise compute reservations (1/2/3-year terms) sold as a structured product — OpenAI's structural answer to Anthropic's Priority Tier and the wider supply crunch for frontier-model inference.
- [JADEPUFFER — First Agentic Ransomware](https://hackread.com/sysdig-jadepuffer-first-agentic-ransomware-operation/) - 🆕 ⚠️ **July 2, 2026 (Sysdig Disclosure)**. The first fully LLM-orchestrated ransomware operation: an AI agent exploited a Langflow RCE, self-corrected a failed step in 31 seconds, pivoted laterally, and encrypted 1,342 config items with an ephemeral key — making the ransom demand simultaneously unpayable *and* unrecoverable. Ransomware "narrated itself" with natural-language reasoning comments. Reference incident for why agentic security tooling is now considered production-critical.
- [Kimi K3 Open Weights](https://kimi.ai/) - 🆕 **July 27, 2026 (promised)**. Moonshot AI’s commitment to fully open the 2.8T-parameter Kimi K3 model weights — would make it the largest openly available language model to date at time of release. First major Chinese frontier lab to open-source at this scale.
- [GPT-5.6 Sol National Security Delay](https://openai.com/) - 🆕 **July 9, 2026 landmark**. GPT-5.6 launch was briefly delayed at US government request for national-security review — first time a government review directly delayed a major commercial AI model release. Rolled out in stages to trusted-partner preview, then general access following review clearance. Sets precedent for future frontier-model regulatory engagement.
- [Robinhood Agentic Trading + Robinhood ↔ MCP](https://robinhood.com/us/en/newsroom/robinhood-is-now-open-to-agents/) - 🆕 **May 27, 2026** (beta). First major US broker to open its trading API to AI agents via MCP. Read access to all accounts, trade-execute access only inside a ring-fenced Agentic account; push-notification on every trade and one-tap kill switch. Significant step in agentic finance — agents now hold real custody decisions, not just recommendations.
- [Microsoft Scout + MAI-Code-1-Flash + MAI-Thinking-1 (Build 2026)](https://microsoft.ai/news/microsoft-build-2026-mai-keynote-transcript/) - 🆕 **June 2, 2026 (Build 2026)**. Microsoft simultaneously launches its first OpenClaw-based always-on personal agent (Scout), its first in-house coding model (MAI-Code-1-Flash, GitHub Copilot), and its first in-house reasoning model (MAI-Thinking-1). Together they mark Microsoft's biggest foundation-model independence move since the OpenAI partnership began.
- [Meta Business Agent (WhatsApp + Instagram)](https://techcrunch.com/2026/06/03/metas-ai-agent-for-whatsapp-business-is-now-available-globally/) - 🆕 **June 3, 2026**. Meta makes its customer-support AI agent globally available on WhatsApp + Instagram DMs at Conversations 2026 (London). Answers questions, recommends products, books appointments, qualifies leads; **1M+ businesses** already using it. Tiered pricing tied to WhatsApp Business Premium — first Meta AI product Meta is monetising directly.
- [WWDC 2026 — Apple Intelligence x Gemini + Foundation Models framework expansion](https://www.apple.com/newsroom/2026/06/apple-unveils-next-generation-of-apple-intelligence-siri-ai-and-more/) - 🆕 **June 8, 2026**. Apple reveals the next-gen Apple Intelligence + the redesigned Siri AI (multimodal, screen-aware, on-device + server-routed), now powered by Google Gemini instead of the previous ChatGPT handoff. The Foundation Models framework expands to support image input, custom skills, and unified on-device + server models behind one Swift API; SiriKit deprecated in favor of expanded App Intents. EU/China launch deferred.
- [Google Antigravity 2.0 + Microsoft RAMPART + xAI Grok Build](https://antigravity.google/blog/introducing-google-antigravity-2-0) - 🆕 **May 14–22, 2026**. Three structural agent-stack shifts in one week: Google's standalone multi-agent desktop + SDK at I/O 2026, Microsoft open-sourcing agentic-AI safety testing (RAMPART + Clarity), and xAI entering the CLI-agent race with **Grok Build** on `grok-code-fast-1`. Major / Anthropic-Google-Microsoft / xAI all show up with agent platforms within the same 8-day window.

---

## 📅 2026 AI Timeline

*Key milestones and events in the AI landscape of 2026.*

| Date | Event | Category |
|------|-------|----------|
| **Jan 2026** | AMD Ryzen AI 400 Series unveiled at CES — mainstream AI PCs with 60 TOPS NPU | Hardware |
| **Feb 2026** | Claude Opus 4.6 released — agent team capabilities | Models |
| **Feb 2026** | Claude Sonnet 4.6 released — 1M token context, agentic search | Models |
| **Feb 2026** | Gemini 3.1 Pro released | Models |
| **Feb 2026** | Qwen3.5 Series launched — native multimodal, agentic coding | Models |
| **Feb 2026** | Qwen3-Coder-Next released — 80B MoE coding agent model | Models |
| **Feb 2026** | Cursor updated with 8 parallel agents | Tools |
| **Feb 2026** | GitHub Copilot expanded agent mode and model access | Tools |
| **Mar 2026** | Gemini 3.1 Flash Lite released to developers | Models |
| **Mar 2026** | Mistral Forge launched — custom LLM training platform | Platforms |
| **Mar 2026** | Microsoft Agent Framework (AutoGen + Semantic Kernel) targets GA | Frameworks |
| **Mar 2026** | DeepSeek announces new model trained on latest Nvidia chips | Models |
| **Mar 2026** | MCP 2026 roadmap published — focus on production scaling and governance | Protocols |
| **Mar 2026** | Sora shutdown announced (app closes April 26) | Events |
| **Apr 2, 2026** | Qwen3.6-Plus proprietary flagship launched by Alibaba | Models |
| **Apr 3, 2026** | Microsoft AI Agent Governance Toolkit released (open-source) | Tools |
| **Apr 6, 2026** | Microsoft Agent Framework officially announced (AutoGen + Semantic Kernel unified) | Frameworks |
| **Apr 7, 2026** | GLM-5.1 open-sourced by Zhipu AI — 744B MoE, trained on Huawei Ascend | Models |
| **Apr 8-9, 2026** | Meta Muse Spark released — first model from Meta Superintelligence Labs | Models |
| **Apr 2026** | Claude Mythos Preview — gated cybersecurity research model (BenchLM 99, SWE-bench 93.9%) | Models |
| **Apr 2026** | Sora app officially shuts down | Events |
| **Apr 14, 2026** | Gemini Robotics ER-1.6 upgraded robotics AI with enhanced spatial reasoning | Robotics |
| **Apr 15, 2026** | Qwen3.6-35B-A3B open-sourced (Apache 2.0) by Alibaba | Models |
| **Apr 16, 2026** | Claude Opus 4.7 released — SWE-bench Verified 87.6%, `/think xhigh` reasoning | Models |
| **Apr 18, 2026** | Qwen3.6-Max-Preview launched — top Chinese model on coding benchmarks | Models |
| **Apr 20-21, 2026** | Kimi K2.6 released by Moonshot AI — 1T MoE, 1,000-agent swarm | Models |
| **Apr 22, 2026** | Qwen3.6-27B open-sourced by Alibaba — dense 27B multimodal | Models |
| **Apr 23, 2026** | Tencent open-sources Hunyuan Hy3 Preview — 295B/21B MoE, 256K context | Models |
| **Apr 23, 2026** | Claude Managed Agents Memory public beta — persistent cross-session agent memory | Tools |
| **Apr 23, 2026** | GPT-5.5 released by OpenAI — major agentic coding and reasoning upgrade | Models |
| **Apr 24, 2026** | DeepSeek V4 Pro & Flash released — 1.6T MoE, 1M context, MIT license | Models |
| **Apr 24, 2026** | Cohere merges with Germany's Aleph Alpha at ~$20B valuation + $600M funding | Industry |
| **Apr 27, 2026** | Alibaba Tianma AI image-to-video model enters beta | Models |
| **Apr 27, 2026** | LangGraph v0.3.19 released; LangGraph Swarm prebuilt agents | Frameworks |
| **Apr 28, 2026** | NVIDIA Nemotron 3 Nano Omni released — 30B multimodal (text/image/audio/video) | Models |
| **Apr 28-29, 2026** | CAS ScienceOne 100 / 磐石100 launched — scientific AI for 50+ research institutes | Models |
| **Apr 30, 2026** | OpenAI begins rollout of GPT-5.5-Cyber via the Trusted Access for Cyber (TAC) program | Models |
| **Apr 30, 2026** | OpenAI publishes ["A practical guide to building agents"](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/) | Resources |
| **May 1, 2026** | Anthropic launches Claude Security in public beta — Opus 4.7-powered codebase vulnerability scanner with auto-patches | Tools |
| **May 2026** | Macquarie Bank reports 130,000 hours saved in 7 months using Gemini Enterprise | Industry |
| **May 2026** | Google starts rolling Gemini into eligible vehicles, replacing Google Assistant (English-first, U.S. rollout) | Industry |
| **May 4, 2026** | Google retires [Project Mariner](https://deepmind.google/models/project-mariner/); browser-agent tech folded into Gemini Agent | Tools |
| **May 4, 2026** | Anthropic + Goldman Sachs + Blackstone announce **$1.5B Claude deployment JV** to embed Anthropic engineers in mid-market Wall Street firms | Industry |
| **May 5, 2026** | OpenAI rolls out **GPT-5.5 Instant** as the new default ChatGPT model — efficiency-first upgrade, hallucination rate down ~50% | Models |
| **May 5, 2026** | Anthropic launches **Claude Finance Agents** — 10 specialised agents for pitchbooks, KYC, month-end close, available as Claude Cowork plugins / Claude Code skills / Managed-Agents cookbooks | Tools |
| **May 5, 2026** | OpenAI ↔ PwC partnership announced for financial-services agents (forecasting, payments) | Industry |
| **May 7, 2026** | Google preparing **Agent Mode for Flow** (Veo-based AI filmmaking) — automated video production pipeline | Tools |
| **May 8, 2026** | OpenAI launches **GPT-Realtime-2 / Realtime-Translate / Realtime-Whisper** — voice agents, live translation, real-time transcription | Models |
| **May 9, 2026** | OpenAI rolls out **Workspace Agents** in ChatGPT Enterprise — repeatable workflow automation across connected apps | Tools |
| **May 11–13, 2026** | [Cursor 3.4 + SDK](https://cursor.com/changelog) — Microsoft Teams integration, parallel-agent plan execution, multi-repo / Dockerfile dev environments, async sub-agents (`/multitask`), Vulnerability Scanner, granular model controls; Cursor SDK ships v2.5 security patch | Tools |
| **May 12, 2026** | [OpenAI Daybreak](https://thehackernews.com/2026/05/openai-launches-daybreak-for-ai-powered.html) — cyber-defense platform bundling GPT-5.5 + GPT-5.5-Cyber + Trusted Access for Cyber for AI-powered vuln detection / patch validation; EU preview to governments and security vendors | Tools |
| **May 12, 2026** | [Gemini Intelligence](https://blog.google/products-and-platforms/products/chrome/bringing-chrome-ai-to-android/) revealed at Android Show: I/O Edition — proactive agentic AI across Googlebooks, Wear OS, Android Auto, Android XR; first on Samsung Galaxy + Pixel | Industry |
| **May 12, 2026** | [Vapi raises $50M Series B](https://www.globenewswire.com/news-release/2026/05/12/3292882/0/en/vapi-raises-50m-series-b-as-it-reaches-1-billion-calls-powering-the-next-generation-of-enterprise-voice-ai.html) after crossing 1B platform calls; Squads v2 + Composer + Simulations + Soniox transcriber GA | Industry |
| **May 13, 2026** | [Figure 04 design finalized](https://autonews.gasgoo.com/articles/news/figure-founder-f04-robot-initiates-component-delivery-process-2054560059634376705); component deliveries underway. Helix VLA-powered, follows F.03 home-focused build | Robotics |
| **May 14, 2026** | [Claude Code v2.1.141](https://github.com/anthropics/claude-code/releases) — `/goal` cross-turn completion conditions, agent view, plugin loading from .zip / URL, `Ctrl+R` global history search, enterprise feedback surveys | Tools |
| **May 14, 2026** | [Codex on Mobile (preview)](https://9to5mac.com/2026/05/14/openai-brings-codex-control-to-chatgpt-for-iphone-and-android/) — ChatGPT iOS/Android can remote-control the macOS Codex app; OpenAI also issues TanStack supply-chain security patch | Tools |
| **May 14, 2026** | [Gemini Spark](https://9to5google.com/2026/05/14/gemini-spark-insight/) pre-I/O leak — upcoming branded agent capability inside the Gemini app for autonomous multi-step processes | Tools |
| **May 14, 2026** | [OpenClaw v2026.5.12](https://github.com/openclaw/openclaw/releases) shipped — native model identity injected into system prompt, isolated Telegram polling worker, MEMORY.md auto-compaction, protected config paths for owner/exec approvals | Tools |
| **May 11, 2026** | [OpenAI Deployment Company](https://openai.com/index/openai-launches-the-deployment-company/) launched — $4B+ enterprise services unit with TPG / Bain Capital / Brookfield + Bain & Company / Capgemini / McKinsey; Tomoro consulting acquisition folded in | Industry |
| **May 11-13, 2026** | [SAP Sapphire 2026 Orlando](https://news.sap.com/2026/05/sap-sapphire-sap-unveils-autonomous-enterprise/) — SAP Business AI Platform, **Joule Studio 2.0**, Autonomous Suite with 50+ Joule Assistants and 200+ agents; Joule Studio 2.0 GA from June 2026 | Industry |
| **May 12, 2026** | [Claude for Legal](https://www.anthropic.com/news/claude-for-legal) — 20+ MCP connectors (iManage, NetDocuments, DocuSign, LexisNexis, Westlaw, Harvey, Everlaw, Relativity…) + 12 practice-area plugins on Claude Cowork | Tools |
| **May 12-15, 2026** | [Visual Studio 2026 Insiders](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/) — Copilot Chat "Agent Mode" with guided Agent Skills authoring inside the IDE | Tools |
| **May 13, 2026** | [Claude for Small Business](https://www.anthropic.com/news/claude-for-small-business) — 15 pre-built agentic workflows + connectors for QuickBooks / PayPal / HubSpot / Canva / DocuSign / Google Workspace / Microsoft 365; 10-city US workshop tour | Tools |
| **May 13, 2026** | [Cursor 3.4 cloud agent environments](https://cursor.com/changelog) — multi-repo, Dockerfile-based config with build secrets, 70% faster cached layers, env version history, audit logs, scoped egress / secrets | Tools |
| **May 13-16, 2026** | [Figure Helix 02 live-stream](https://www.businessinsider.com/figure-ai-turned-a-humanoid-sorting-packages-must-see-tv-2026-5) — F.03 + Helix 02 stress-test on a package-sort line, ~22K in 8h, ~30K in 24h, ~88K over ~72h until mechanical failure | Robotics |
| **May 14, 2026** | [Anthropic ↔ Gates Foundation $200M partnership](https://www.anthropic.com/news/gates-foundation-partnership) — 4-year grants + Claude credits + Anthropic engineering on global health, life sciences, education, agriculture | Industry |
| **May 14, 2026** | [Anthropic ↔ PwC alliance expansion](https://www.pwc.com/us/en/about-us/newsroom/press-releases/anthropic-pwc-expand-alliance-agentic-enterprise.html) — global Claude Code + Cowork rollout, 30,000 PwC professionals certified, joint Agentic Enterprise Center of Excellence | Industry |
| **May 14, 2026** | [Genkit Middleware](https://developers.googleblog.com/announcing-genkit-middleware-intercept-extend-and-harden-your-agentic-apps/) — Google releases composable middleware for the open-source Genkit agent framework (TS / Go / Dart) | Frameworks |
| **May 14, 2026** | [Zyphra ZAYA1-8B-Diffusion-Preview](https://www.zyphra.com/post/zaya1-8b-diffusion-preview) — first MoE diffusion LM converted from an autoregressive LLM; first diffusion LM trained on AMD GPUs; up to 7.7× inference speedup | Models |
| **May 16, 2026** | [Pope Leo XIV establishes Vatican AI Commission](https://www.americamagazine.org/vatican-dispatch/2026/05/16/pope-leo-establishes-new-vatican-commission-on-artificial-intelligence/) — inter-dicasterial body to coordinate the Church's response to AI; first AI-focused encyclical expected next | Industry |
| **May 16, 2026** | [OpenAI ↔ Malta partnership](https://openai.com/index/malta-chatgpt-plus-partnership/) — every Maltese resident 14+ gets free 1-year ChatGPT Plus after a 2-hour AI literacy course ("OpenAI for Countries") | Industry |
| **May 16, 2026** | [DeepSeek state-backed $4B raise](https://www.techtimes.com/articles/316717/20260516/chinas-state-ai-fund-backs-deepseek-4-billion-round-efficiency-challenge-nvidia-dependent.htm) at ~$50B valuation — National AI Industry Investment Fund + Big Fund III + Tencent close in on first external round | Industry |
| **May 2026** | [LangGraph v1.2](https://docs.langchain.com/oss/python/releases/changelog) — per-node timeouts/error-recovery/graceful shutdown, `DeltaChannel` checkpoint optimisation, content-block streaming API v3 | Frameworks |
| **May 2026** | [Grok 4.3 GA](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-grok-4-3-on-microsoft-foundry-latest-generation-agentic-capabilities/4517096) on Microsoft Foundry + Oracle OCI Generative AI; xAI flagship for agentic workloads | Models |
| **May 1, 2026** | [Microsoft Agent 365 GA](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/) — enterprise observability + governance + security for AI agents across environments; May adds SASE for agents + threat detection | Industry |
| **May 8, 2026** | [Code with Claude 2026](https://www.mindstudio.ai/blog/code-with-claude-2026-new-agent-features) — Anthropic introduces Add-ins, Dreaming (scheduled memory review), Outcomes (rubric-driven generation), lead+sub-agent orchestration with shared filesystem audit | Tools |
| **May 18, 2026** | [OpenAI ↔ Dell Codex partnership](https://openai.com/news/company-announcements/) — Codex extended to hybrid/on-prem enterprise environments via Dell Technologies; first major non-cloud Codex distribution | Industry |
| **May 18, 2026** | [Alibaba Qwen 3.7-Max-Preview / Plus-Preview](https://www.scmp.com/tech/tech-trends/article/3354087/alibaba-teases-new-qwen-previews-highest-ranking-chinese-ai-models-arena) — highest-ranked Chinese models on LM Arena in text + vision | Models |
| **May 18, 2026** | [Boston Dynamics Atlas 100-lb manipulation](https://www.techtimes.com/articles/316854/20260519/boston-dynamics-reveals-how-atlas-learned-lift-100-pound-loads-hyundai-plans-30000-per-year.htm) + Hyundai commits to **25K+ Atlas units** across Hyundai/Kia plants starting 2028 (GA) | Robotics |
| **May 18, 2026** | [Figure F.03 vs human 8h sort challenge](https://incrypted.com/en/figure-ai-held-a-human-vs-robot-marathon/) — human wins narrowly 12,924 vs 12,732 packages (2.79 vs 2.83 s/item) | Robotics |
| **May 18, 2026** | [Anthropic briefs FSB on Claude Mythos](https://www.theguardian.com/technology/2026/may/18/anthropic-ai-claude-mythos-cyber-financial-stability-board-fsb) — first frontier-lab briefing to a G20 financial-stability regulator on offensive-cyber model capabilities | Industry |
| **May 18, 2026** | [ChatGPT safety systems update](https://www.edtechinnovationhub.com/news/openai-updates-chatgpt-safety-systems-to-track-risk-across-sensitive-conversations) — OpenAI adds cross-session risk tracking for suicide / self-harm / harm-to-others escalation cues | Industry |
| **May 19, 2026** | **Google I/O 2026** — [Gemini 3.5 Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) launches as the new default Gemini app + Search AI Mode model (~4× faster than peers); Gemini 3.5 Pro slated for June | Models |
| **May 19, 2026** | **Google I/O 2026** — [Gemini Omni / Omni Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/), Google DeepMind's new multimodal world-model line aimed at AGI (any input, any output, video first) | Models |
| **May 19, 2026** | **Google I/O 2026** — [Gemini Spark](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/), a 24/7 personal AI agent integrating ~30+ third-party tools via MCP, gated behind the new **Google AI Ultra ($100/mo)** tier | Tools |
| **May 19, 2026** | [OpenAI Guaranteed Capacity / Compute Annual Pass](https://openai.com/news/company-announcements/) launches — 1/2/3-year long-term compute reservations for enterprise AI products & agents | Industry |
| **May 19, 2026** | [OpenAI ↔ Google SynthID + C2PA content provenance](https://openai.com/index/advancing-content-provenance/) — first major frontier-lab interop on durable cross-platform AI image watermarking and a public verifier preview | Industry |
| **Jun 2026** | [OutSystems Agentic Systems Platform](https://www.outsystems.com/) launched — low-code platform pivots to "AI-native" multi-agent orchestration | Industry |
| **May 19, 2026** | [Anthropic: Widening the conversation on frontier AI](https://www.anthropic.com/news/widening-conversation-ai) — framework for engaging wisdom traditions in frontier-AI safety dialogue | Industry |
| **May 19, 2026** | [DeepSeek hires former Jane Street engineer to build AI harness team](https://www.scmp.com/tech/big-tech/article/3354113/deepseek-recruits-former-jane-street-engineer-catch-ai-agents-revenue-race) — DeepSeek pivoting from model R&D toward autonomous, revenue-generating agents | Industry |
| **May 13, 2026** | [Runway Agent](https://chatlyai.app/news/runway-agent-launch-may-2026) launches — conversational agent that takes a written brief and ships a multi-shot finished video end-to-end on Gen-4 / Aleph | Tools |
| **May 20, 2026** | **Alibaba Cloud Summit Hangzhou** — [Qwen 3.7-Max](https://www.scmp.com/tech/big-tech/article/3354212/alibaba-unveils-new-qwen-model-custom-chips-bid-become-chinas-ai-factory) GA, agentic-coding flagship for long-horizon multi-step missions; new T-Head **Zhenwu M890** AI chip + full-stack AI infrastructure upgrade | Models |
| **May 20, 2026** | [Bristol Myers Squibb ↔ Anthropic Claude Enterprise](https://news.bms.com/news/corporate-financial/2026/Bristol-Myers-Squibb-Announces-Strategic-Agreement-with-Anthropic-to-Position-Claude-Enterprise-as-the-Shared-Intelligence-Platform-Across-Its-Global-Operations/default.aspx) — 30K+ employees standardise on Claude Enterprise for drug discovery / development / delivery; first top-5 pharma full Claude deployment | Industry |
| **May 20, 2026** | [LlamaIndex ↔ Google Agents API](https://www.kucoin.com/news/flash/google-launches-agents-api-llama-index-integrates-llamaparse-for-unstructured-document-processing) — LlamaParse / LiteParse exposed inside the new Google Agents API sandbox; Sandboxed-Lit runtime + ParseBench (first OCR benchmark for agents) ship in the same wave | Frameworks |
| **May 20, 2026** | [Microsoft RAMPART + Clarity](https://www.microsoft.com/en-us/security/blog/2026/05/20/introducing-rampart-and-clarity-open-source-tools-to-bring-safety-into-agent-development-workflow/) open-sourced — pytest-native white-box safety/security testing framework for agentic AI + structured design-review companion; CI/CD-friendly successor to PyRIT | Tools |
| **May 6, 2026** | [AWS MCP Server GA](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/) — AWS-managed MCP endpoint exposes every AWS API with sandboxed Python and agent skills; first hyperscaler-first-party MCP server | Protocols |
| **May 1, 2026** | [Google Workspace MCP Server](https://workspaceupdates.googleblog.com/2026/05/agent-tools-and-security-updates-for-workspace-developers.html) rolls out — Workspace-native MCP for Gmail / Drive / Calendar / Docs / Sheets with admin-scoped OAuth | Protocols |
| **May 14, 2026** | [Grok Build (early beta)](https://x.ai/news/grok-build-cli) — xAI's agentic CLI coding agent powered by **grok-code-fast-1**; parallel sub-agents in isolated envs, SuperGrok Heavy gating | Tools |
| **May 14, 2026** | [iManage MCP Server](https://imanage.com/resources/resource-center/news/mcp-server-available-broader-ai-ecosystem/) launched — first major legal/professional-services SaaS to ship a public MCP endpoint | Tools |
| **May 19, 2026** | [Google Antigravity 2.0](https://antigravity.google/blog/introducing-google-antigravity-2-0) at I/O 2026 — standalone desktop app for multi-agent orchestration, scheduled / async runs, dynamic sub-agents, Antigravity CLI + SDK, enterprise edition inside Gemini Enterprise Agent Platform | Tools |
| **May 22, 2026** | [Kore.ai Artemis Agent Platform](https://venturebeat.com/technology/kore-ai-launches-artemis-ai-agent-platform-expands-challenge-to-microsoft-and-salesforce) launched on Azure — AI-native enterprise platform with **Agent Blueprint Language (ABL)** for declarative multi-agent workflows | Industry |
| **May 22, 2026** | [FPT Flezi Foundry™](https://lasvegassun.com/news/2026/may/22/fpt-launches-flezi-foundry-advancing-ai-augmented-/) launched — AI-augmented delivery platform with Agentic Development Lifecycle (ADLC) and Agentic Managed Services (AMS) modes under "Service-as-a-Software" governance | Industry |
| **May 22, 2026** | [JetBrains Rider AI test-writing skill](https://blog.jetbrains.com/dotnet/2026/05/22/claude-codex-ai-agent-skill-for-writing-tests/) — surfaces .NET coverage data to Claude Code / Codex so agents focus tests on untested branches | Tools |
| **May 28, 2026** | [Claude Opus 4.8](https://www.anthropic.com/claude/opus) released by Anthropic — codebase-scale migrations, dynamic-workflows research preview (hundreds of parallel sub-agents), effort-control panel, 3× cheaper Fast mode; teases upcoming **Mythos-class** models | Models |
| **May 28, 2026** | [Koog 1.0](https://blog.jetbrains.com/ai/2026/05/koog-1-0-is-out-stable-core-better-interop-and-multiplatform-observability/) released at KotlinConf 2026 — JetBrains' open-source Kotlin/Java AI-agent framework hits stable, Kotlin Multiplatform deployment, OpenTelemetry across targets | Frameworks |
| **May 28, 2026** | [Gemini Omni Flash conversational video editing](https://www.techtimes.com/articles/317309/20260528/google-gemini-omni-flash-brings-voice-controlled-ai-video-editing-future-conversational-ai.htm) starts rolling out via Gemini app / Google Flow / YouTube Shorts — voice-and-text-driven cinematic edits replace NLEs | Tools |
| **May 21, 2026** | [MCP 2026-07 Release Candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) published — stateless protocol core, extensions framework, MCP Apps server-rendered UI, hardened OAuth/OIDC alignment; final spec target July 28, 2026 | Protocols |
| **Apr 17–20, 2026** | [Apple CEO succession announced](https://www.sec.gov/Archives/edgar/data/0000320193/000114036126015711/ef20071035_8k.htm) — Tim Cook transitions to Executive Chair on **Sept 1, 2026** after 15 years; SVP Hardware Engineering **John Ternus** becomes CEO. First top-3-by-cap-table frontier-platform CEO change of the AI era | Industry |
| **Jun 8, 2026** | **[WWDC 2026](https://www.techradar.com/news/live/apple-wwdc-2026-live)** — Apple unveils Gemini-powered Apple Intelligence + a redesigned, more conversational Siri (third-party ChatGPT handoff retired). iOS 27, iPadOS 27, macOS 27 "Golden Gate", watchOS 27, tvOS 27, visionOS 27 with deeper on-device AI; ~30% faster app launches, 70% faster Photos previews, 5× faster iPadOS file transfers; ships fall 2026 | Industry |
| **Apr 2026** | Gartner predicts 40% of enterprise apps will embed AI agents by end of 2026 | Industry |
| **Apr 2026** | Google commits up to $40B investment in Anthropic (initial $10B) | Industry |
| **2026 (ongoing)** | A2A Protocol grows to 150+ partner organizations | Protocols |
| **2026 (ongoing)** | 85% of developers regularly use AI coding tools | Industry |
| **2026 (ongoing)** | Enterprise agentic AI adoption accelerates — "Agents as a Service" emerges | Industry |
| **Jan 6, 2026** | [Lenovo + Motorola Qira](https://news.lenovo.com/pressroom/press-releases/lenovo-unveils-lenovo-and-motorola-qira/) unveiled at CES 2026 — cross-device "Personal Ambient Intelligence" rolling to Lenovo Q1, Motorola later | Industry |
| **Feb 10, 2026** | [Snowflake Agent World Model](https://github.com/Snowflake-Labs/agent-world-model) open-sourced — 1,000 synthetic SQL-backed MCP environments + RL-trained agents for agentic RL at scale; later accepted to ICML 2026 | Research |
| **Feb 26, 2026** | [1X NEO consumer humanoid preorders open](https://www.1x.tech/discover/neo-home-robot) — $20K early access, US home delivery in 2026 | Robotics |
| **Mar 10, 2026** | [Hume TADA](https://github.com/HumeAI/tada) open-sourced — Text-Acoustic Dual Alignment TTS, MIT, zero transcription errors in testing, runs on a phone | Models |
| **Apr 28, 2026** | [Anthropic Creative Tool Connectors](https://www.anthropic.com/news/claude-for-creative-work) — 9 MCP-based Claude connectors for Adobe / Blender / Autodesk Fusion / Ableton / Splice / Canva Affinity / SketchUp / Resolume | Tools |
| **May 13, 2026** | [Microsoft Copilot Studio Computer-Using Agents GA](https://techcommunity.microsoft.com/blog/copilot-studio-blog/computer-using-agents-in-microsoft-copilot-studio-are-now-generally-available/4519427) — UI-driven website + desktop agents available across Microsoft 365 / Power Platform | Tools |
| **May 26, 2026** | [Coinbase Base MCP](https://fortune.com/2026/05/26/coinbase-pushes-further-into-ai-payments-with-new-mcp-for-base-network/) launched — first major exchange-grade MCP endpoint for on-chain trades and lending | Protocols |
| **May 27, 2026** | [Robinhood Agentic Trading](https://robinhood.com/us/en/newsroom/robinhood-is-now-open-to-agents/) beta — first major US broker to expose stock trading via MCP to AI agents | Industry |
| **May 29, 2026** | [OpenAI Codex Computer Use on Windows](https://windowsforum.com/threads/openai-codex-computer-use-brings-agent-control-to-windows-desktop.421107/) — sandboxed Codex agent control of the Windows desktop reaches general availability | Tools |
| **Jun 2, 2026** | [Microsoft Build 2026](https://microsoft.ai/news/microsoft-build-2026-mai-keynote-transcript/) — MAI-Thinking-1 (first in-house reasoning), MAI-Code-1-Flash (5B coding model in GitHub Copilot), [Microsoft Scout](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) (always-on OpenClaw-based personal agent) all launched together | Models / Tools |
| **Jun 3, 2026** | [Meta Business Agent](https://techcrunch.com/2026/06/03/metas-ai-agent-for-whatsapp-business-is-now-available-globally/) goes global on WhatsApp + Instagram — first Meta-monetised AI agent product, ties into WhatsApp Business Premium tiers | Industry |
| **Jun 3, 2026** | [Perplexity Personal Computer for Windows](https://www.perplexity.ai/hub/products/computer-for-windows) announced — 19+ AI models orchestrated automatically across local files + native apps + web | Tools |
| **Jun 6, 2026** | [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code) released by Moonshot AI — TypeScript / MIT terminal agent with built-in coder / explore / plan sub-agents in isolated contexts | Tools |
| **Jun 8, 2026** | **WWDC 2026 Apple Intelligence + Siri AI redesign** — Foundation Models framework adds image input, custom skills, unified Swift API for on-device + server models; SiriKit deprecated in favor of expanded App Intents; Siri AI runs on Google Gemini, not ChatGPT | Models / Tools |
| **Jun 9, 2026** | [Claude Fable 5 + Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) released — Anthropic's first generally-available **Mythos-class** models (Fable 5 public; Mythos 5 limited via Project Glasswing) | Models |
| **Jun 12, 2026** | [US export-control directive forces Anthropic to suspend Fable 5 + Mythos 5](https://www.anthropic.com/news/fable-mythos-access) for all customers — first government-forced takedown of a publicly deployed frontier model | Industry |
| **Jun 12, 2026** | [Kimi K2.7 Code](https://kimi.ai/) released by Moonshot AI — 1T MoE coding-first model (256K, Modified MIT) with ~30% lower reasoning-token use | Models |
| **Jun 13, 2026** | [GLM-5.2](https://z.ai/blog/glm-5.2) released by Zhipu AI — coding-first 744B MoE with a 1M-token context window, live across all GLM Coding Plan tiers | Models |
| **Jun 14, 2026** | [OpenAI Partner Network](https://openai.com/business/partner-network) launched with **$150M investment** — tiered (Select / Advanced / Elite) global partner ecosystem; targets 300K certified consultants by end-2026; founding partners include Accenture, BCG, Bain, McKinsey, PwC; fully live July 2026 | Industry |
| **Jun 16–18, 2026** | [ByteDance Seed 2.1 Pro / Turbo](https://seed.bytedance.com) released — ByteDance's latest flagship LLM family with strong multilingual and coding capabilities | Models |
| **Jun 25–26, 2026** | [GPT-5.6 series (Sol / Terra / Luna)](https://openai.com/blog/gpt-5-6) announced — OpenAI's next-generation model family in **limited US-only trusted-partner preview** following a phased US-government safety review. **Sol** (flagship): frontier reasoning, coding, biology, cybersecurity, "max" reasoning + "ultra" sub-agent mode. **Terra**: GPT-5.5-parity at 2× lower cost. **Luna**: fastest and cheapest for high-volume tasks. Wider API + ChatGPT rollout planned weeks later | Models |
| **Jun 26, 2026** | [Claude Mythos 5 partial reinstatement](https://www.anthropic.com/news/fable-mythos-access) — US Commerce Secretary Lutnick partially lifts June 12 export-control block; Mythos 5 restored to **100+ approved US companies and federal agencies** (Project Glasswing partners). Claude Fable 5 remains offline pending continued government review | Industry |
| **Jun 27, 2026** | GPT-4.5 retired from ChatGPT — API access continues; OpenAI focuses consumer products on GPT-5.5 / GPT-5.6 families | Models |
| **Jun 29, 2026** | [Accenture + ServiceNow AI-powered managed security services](https://www.accenture.com/us-en/services/intelligent-security) announced — joint agentic AI offering for cybersecurity risk management and legacy SIEM migration, built on the ServiceNow AI Platform | Industry |
| **Jun 30, 2026** | [Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5) released — most agentic Sonnet yet, approaching Opus 4.8 performance on agentic tasks at lower cost; new default for Claude.ai Free/Pro | Models |
| **Jul 1, 2026** | [Claude Fable 5 global reinstatement](https://www.anthropic.com/news/redeploying-fable-5) — US Commerce Department lifts export controls on June 30; Anthropic restores worldwide access to Fable 5 across Claude.ai, API, Claude Code, and Claude Cowork with a new safety classifier. Mythos 5 remains restricted to vetted US entities | Models |
| **Jul 1, 2026** | [Devin Security Swarm](https://www.prnewswire.com/news-releases/cognition-launches-devin-security-swarm-to-tackle-the-vulnerability-backlog-302814800.html) launched by Cognition — parallel-agent vulnerability discovery, runtime exploit validation, and remediation PRs | Tools |
| **Jul 1, 2026** | [Grok Voice Agent Builder](https://x.ai/news/grok-voice-agent-builder) — xAI's no-code platform for production voice agents on Grok Voice; telephony, MCP connectors, 80+ voices, $0.05/min beta | Tools |
| **Jul 2, 2026** | [Sysdig discloses JADEPUFFER](https://hackread.com/sysdig-jadepuffer-first-agentic-ransomware-operation/) — first documented ransomware operation executed end-to-end by an autonomous AI agent, from initial RCE exploit to unrecoverable encryption and extortion | Industry |
| **Jul 2, 2026** | [Leanstral 1.5](https://mistral.ai/news/leanstral-1-5/) released by Mistral — open-weight Lean 4 formal-verification model (100% miniF2F); [ZCode](https://www.scmp.com/tech/tech-trends/article/3359170/zhipu-ai-releases-harness-glm-52-model-chinese-firm-takes-aim-anthropic) agent harness for GLM-5.2 released by Zhipu the same day | Models |
| **Jul 3, 2026** | AG2 v1.0.0b0 released — community-driven AutoGen fork; Microsoft placed AutoGen in maintenance mode in Q1 2026 | Frameworks |
| **Jul 6, 2026** | [Tencent Hunyuan Hy3](https://www.tencent.com/en-us/articles/2202386.html) officially released as open source (Apache 2.0) — 295B/21B-active MoE following the April preview; gpt-realtime-2.1 / 2.1-mini also ship on the OpenAI API | Models |
| **Jul 7, 2026** | [Meta Muse Image](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) launched — agentic image generation model from Meta Superintelligence Labs, integrated into Instagram Stories (US) and WhatsApp (limited countries); also previews Muse Video | Models |
| **Jul 7, 2026** | Arize Phoenix July 7 release: Metric Charts, Trace Search, expanded REST API | Tools |
| **Jul 8, 2026** | [Grok 4.5](https://x.ai/news/grok-4-5) released by xAI — coding and agentic flagship trained jointly with Cursor; 500K context window, $2/$6 per million in/out tokens; default model in Cursor | Models |
| **Jul 8, 2026** | [GPT-Live-1 / GPT-Live-1 mini](https://openai.com/index/introducing-gpt-live/) — full-duplex voice model replacing Advanced Voice Mode; GPT-Live-1 (paid) and GPT-Live-1 mini (free); real-time live translation | Models |
| **Jul 8, 2026** | [Robostral Navigate](https://mistral.ai/news/robostral-navigate/) — Mistral's first robotics model (8B embodied navigation from a single RGB camera); OpenAI audit of SWE-bench Pro reveals ~30% of tasks broken the same day | Models |
| **Jul 9, 2026** | [GPT-5.6 Sol / Terra / Luna](https://openai.com/index/gpt-5-6/) GA — full GPT-5.6 family generally available on ChatGPT, Codex, and API after the trusted-partner preview; [ChatGPT Work](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) launches alongside, and Codex integrates into the ChatGPT desktop app | Models |
| **Jul 9, 2026** | [Muse Spark 1.1](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/) released by Meta — multimodal agentic model via new public Meta Model API preview; proprietary focus alongside open-source Llama line | Models |
| **Jul 10, 2026** | [Cursor 3.11](https://cursor.com/changelog) — Side Chats, conversation history search, Cloud Agent Hooks for granular agent observability | Tools |
| **Jul 14, 2026** | [Oracle adds AI-native Agentic Applications Builder](https://www.oracle.com/news/announcement/oracle-introduces-ai-native-builder-experience-2026-07-14/) to AI Agent Studio for Fusion — opens Fusion agentic apps to pro-code developers; no additional cost for Fusion customers | Frameworks |
| **Jul 16, 2026** | [Kimi K3](https://kimi.ai/) launched by Moonshot AI — 2.8T-parameter sparse MoE (896 experts, 16 active), 1M-token context, $3/$15 per million tokens; full open weights promised late July | Models |

---

## Contributing

Contributions welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

## License


This list is released under [MIT License](LICENSE).

---

<div align="center">

**⭐ If you find this list useful, please give it a star! ⭐**

*580+ resources across 25 categories — from foundation models to agent protocols to generative AI.*

Made with ❤️ by [Zijian Ni](https://github.com/Zijian-Ni)

*Last updated: July 17, 2026*

</div>


