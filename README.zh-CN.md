<div align="center">

# 🤖 Awesome AI Agents 2026 · 中文版

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fawesome-ai-agents-2026&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)](https://github.com/Zijian-Ni/awesome-ai-agents-2026/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-July%2017%2C%202026-blue.svg)](#)
[![Resources](https://img.shields.io/badge/Resources-580%2B-orange.svg)](#)
[![Audited](https://img.shields.io/badge/Spam_Audited-2026--07--17-success.svg)](#️-状态图例)
[![English](https://img.shields.io/badge/Lang-English-informational.svg)](README.md)
[![日本語](https://img.shields.io/badge/Lang-日本語-red.svg)](README.ja.md)

**2026 年 AI 模型、Agent 框架、工具、协议与资源精选清单 —— 这是 Agent 真正成为基础设施的一年。**

*覆盖：基础大模型、多模态生成、Agent 协议（MCP / A2A）、编程 Agent、计算机使用、生成式 AI 等。*

### 🏷️ 状态图例

每条目可能携带一个或多个状态标签，便于读者一眼判断成熟度：

- 🆕 **New** — 60 天内加入，效果尚待沉淀
- 📦 **Archived** — 仓库已归档，仅作历史参考，不再更新
- 💤 **Stale** — 6 个月以上无提交，可能仍可用但已不再活跃维护
- ⚠️ **Unverified** — 新提交且第三方使用证据有限（star 少 / 单作者 / 同款 PR 批量铺货）。**仅作可见性收录，不背书**，使用前请自行评估
- 🇨🇳 **Chinese ecosystem** — 中国大陆团队主导或主要面向中文市场的项目
- 🔥 **Hot** — 近 30 天 GitHub stars 增长 >20%，社区热度高涨。
- ⚡ **Updated** — 近 14 天内有显著新版本发布或重要功能迭代。
- 🧪 **Experimental** — 有潜力但尚不适合生产环境，建议仅用于 R&D 探索。
- 💰 **Freemium** — 核心功能免费，规模扩展或高级功能需付费。
- 🔐 **Audited** — 已通过独立第三方安全审计或形式化验证。
- 🇨🇳 **China-first** — 主要面向中文语言、国内合规或国产云基础设施。

[基础大模型](#-基础大模型-2026) · [多模态](#-多模态与生成式-ai) · [协议](#-agent-协议与标准) · [框架](#️-agent-框架) · [IDE 与构建器](#️-agent-ide-与可视化构建器) · [记忆](#-agent-记忆) · [工具](#-工具与-api-集成) · [沙箱](#-agent-沙箱与计算隔离) · [安全](#️-agent-安全) · [RAG](#-rag-与知识库) · [编程](#-编程-agent) · [Physical AI](#-physical-ai--具身智能) · [仿真](#-agent-仿真与世界模型) · [评测](#-评测与-leaderboard) · [Computer Use](#️-computer-use--桌面-agent) · [浏览器与 Web](#-浏览器与-web-agent) · [语音](#️-语音与多模态-agent) · [个人](#-个人-ai-agent) · [手机](#-手机-agent) · [企业](#-企业级-agent-平台) · [评估](#-agent-评估与可观测性) · [研究工具](#-ai-研究工具) · [学习](#-学习资源) · [中国生态](#-中国-ai-生态) · [对比](#-横向对比表) · [2026 看点](#-2026-年值得关注的-agent-项目) · [时间线](#-2026-ai-时间线)

</div>

---

## 🚀 从这里开始

> **初次接触 AI Agent？** 按这个路径走：
> 1. 📖 **梳清概念** — Agent 和普通聊天机器人到底有什么区别
> 2. 🗺️ **找到你的场景** → [场景指南](#️-场景指南--我应该用什么)
> 3. 🧩 **复制经过验证的技术栈** → [技术栈食谱](#-技术栈食谱--经过验证的工具组合)
> 4. 🔍 **选对工具** → [对比表](#-横向对比表)
> 5. ⚠️ **避开常见陷阱** → [反推荐清单](#️-反推荐--不应该用在哪里)
>
> **已在开发？** 快速跳转：
> - 🆕 [最新添加（2026 年 7 月）](#-2026-ai-时间线) • 🛡️ [安全](#️-agent-安全) • 💰 [费用对比](#-基础大模型--api-价格与上下文窗口)

---

## 目录

- [🧠 基础大模型 2026](#-基础大模型-2026)
- [🎨 多模态与生成式 AI](#-多模态与生成式-ai)
- [🔗 Agent 协议与标准](#-agent-协议与标准)
- [🏗️ Agent 框架](#️-agent-框架)
- [🛠️ Agent IDE 与可视化构建器](#️-agent-ide-与可视化构建器)
- [🧠 Agent 记忆](#-agent-记忆)
- [🔌 工具与 API 集成](#-工具与-api-集成)
- [🧪 Agent 沙箱与计算隔离](#-agent-沙箱与计算隔离)
- [🛡️ Agent 安全](#️-agent-安全)
- [🔍 RAG 与知识库](#-rag-与知识库)
- [💻 编程 Agent](#-编程-agent)
- [🤖 Physical AI / 具身智能](#-physical-ai--具身智能)
- [🎮 Agent 仿真与世界模型](#-agent-仿真与世界模型)
- [📊 评测与 Leaderboard](#-评测与-leaderboard)
- [🖥️ Computer Use / 桌面 Agent](#️-computer-use--桌面-agent)
- [🌐 浏览器与 Web Agent](#-浏览器与-web-agent)
- [🗣️ 语音与多模态 Agent](#️-语音与多模态-agent)
- [📱 个人 AI Agent](#-个人-ai-agent)
- [📱 手机 Agent](#-手机-agent)
- [🏢 企业级 Agent 平台](#-企业级-agent-平台)
- [📊 Agent 评估与可观测性](#-agent-评估与可观测性)
- [🔬 AI 研究工具](#-ai-研究工具)
- [📚 学习资源](#-学习资源)
- [🇨🇳 中国 AI 生态](#-中国-ai-生态)
- [📝 横向对比表](#-横向对比表)
- [🗺️ 场景指南 — 我应该用什么…](#️-场景指南--我应该用什么)
- [📋 技术栈食谱 — 经过验证的工具组合](#-技术栈食谱--经过验证的工具组合)
- [⚠️ 反推荐 — 不应该用在哪里…](#️-反推荐--不应该用在哪里)
- [🌟 2026 年值得关注的 Agent 项目](#-2026-年值得关注的-agent-项目)
- [📅 2026 AI 时间线](#-2026-ai-时间线)

---

## 🧠 基础大模型 2026

*为整个 AI 生态提供动力的大语言模型，按厂商组织。20+ 家厂商共 65+ 个模型。*

### OpenAI
- [GPT-Live-1 / GPT-Live-1 mini](https://openai.com/index/introducing-gpt-live/) - 🆕 **2026-07-08**。OpenAI 全双工会话语音模型，取代进阶语音模式。同步收听和说话（零切换延迟），处理打断，复杂查询在后台由 GPT-5.5 处理同时语音不中断。**GPT-Live-1** 为付费用户默认（Go/Plus/Pro）；**GPT-Live-1 mini** 为免费用户默认。支持实时语音翻译。
- [GPT-5.6 Sol](https://openai.com/blog/gpt-5-6) - 🆕 **2026-07-09**（GA；有限预览从 2026-06-26 开始）。GPT-5.6 家族旗舰层 —— Sol 具备最强旨攟推理、编程、生物、网安能力以及 “max 推理” + “ultra 子 Agent 模式”。因美国政府安全审查要求延迟发布，渐进面向全部用户。
- [GPT-5.6 Terra](https://openai.com/blog/gpt-5-6) - 🆕 **2026-07-09**。GPT-5.6 中级档 —— 与 GPT-5.5 性能相当但成本约降低 2×，适合成本敏感的生产任务。
- [GPT-5.6 Luna](https://openai.com/blog/gpt-5-6) - 🆕 **2026-07-09**。GPT-5.6 速度/成本最优层 —— 专为大量、对延迟敏感的任务设计。
- [ChatGPT Work](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) - 🆕 **2026-07-09**。OpenAI 的「把目标变成成品」Agent —— 可跨已连接的应用与文件执行操作，能连续数小时专注一个项目，生成幻灯片/表格/文档/Web 应用，支持定时任务，并具备带内置浏览器的桌面 Computer Use 能力。由 GPT-5.6 驱动。Web/移动端从 Pro、Enterprise、Edu 开始逐步开放（Plus/Business 随后）；桌面 App 已在 Mac 与 Windows 全球上线，所有套餐（含免费版）可用。
- [Sites for ChatGPT](https://openai.com/academy/chatgpt-sites/) - 🆕 **2026-06**。由 Codex 驱动的 ChatGPT 功能，能将计划和分析转换为可交互、可分享的网页与轻量应用。截至 2026-07-09 GPT-5.6 / ChatGPT Work 发布时处于公测阶段。
- [Codex 业务插件](https://venturebeat.com/orchestration/openais-codex-update-lets-agents-build-interactive-enterprise-workspaces-via-sites-and-role-specific-plugins) - 🆕 **2026-06**。面向企业的增强功能，为 Codex 平台引入销售、数据分析和创意制作的定制插件。
- [GPT-Rosalind](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/) - 🆕 **2026-06-03**。OpenAI 生命科学前沿模型的重大升级 —— 药物发现、基因组学、定量生物学与湿实验排障显著增强（长程基因组分析比 GPT-5.5 约少用 31% token）。研究预览首次面向全球合资格机构开放；Novo Nordisk 加入既有伙伴 Amgen、Moderna、Allen Institute、Thermo Fisher。

- [GPT-5.5](https://openai.com/index/gpt-5-5-system-card/) - 🆕 **2026-04-23 发布**（代号 "Spud"）。OpenAI 面向 Agent 任务的新一代旗舰：编程、在线研究、数据分析、自主工具调用。推理稳定性与长任务执行力大幅提升。ChatGPT Plus / Pro / Business / Enterprise 可用。
- [GPT-5.5 Pro](https://openai.com/index/gpt-5-5-system-card/) - 🆕 2026-04-23。并行测试期算力变体，更高准确率。Pro / Business / Enterprise。
- [GPT-5.5 Instant](https://openai.com/index/gpt-5-5-instant/) - 🆕 **2026-05-05**。ChatGPT 新默认模型，效率优先升级，高风险提示词幻觉率下降约 50%；免费用户可用。
- [GPT-5.5-Cyber](https://openai.com/index/trusted-access-for-cyber/) - 🆕 **2026-04-30**。GPT-5.5 的网络安全特化版本，通过 OpenAI Trusted Access for Cyber (TAC) 计划仅向防御者、政府、关键基础设施运营方、安全厂商开放，不对公众发布。
- [OpenAI Daybreak](https://thehackernews.com/2026/05/openai-launches-daybreak-for-ai-powered.html) - 🆕 **2026-05-12**。整合 GPT-5.5 + GPT-5.5-Cyber + Trusted-Access-for-Cyber 的网络防御平台，提供 AI 驱动的漏洞检测与补丁验证；预览版已向欧盟政府与安全厂商开放。
- [GPT-Realtime-2](https://openai.com/) - 🆕 **2026-05-08**。把 GPT-5 级推理带入 Realtime API，128K 上下文，并行工具调用 + 音频反馈，可调推理力度。
- [GPT-Realtime-Translate](https://openai.com/) - 🆕 **2026-05-08**。实时语音对语音翻译，覆盖 70+ 种输入语言、13 种输出语言。
- [GPT-Realtime-Whisper](https://openai.com/) - 🆕 **2026-05-08**。GPT-Realtime-2 的流式低延迟语音转文字搭档。
- [GPT-5.4](https://openai.com/) - 2026-03 发布。1M token 上下文，编程、Computer Use、工具检索均强。BenchLM 94，SWE-bench Verified 77.2%，OSWorld 75%（超过人类基线）。
- [GPT-5.4 Pro](https://openai.com/) - GPT-5.4 的高准确率变体。BenchLM 92。
- [GPT-5.3](https://openai.com/) - 2026 年初。包括 GPT-5.3 Instant（对话）和 GPT-5.3-Codex（编程）。
- [GPT-5.2](https://openai.com/) - 2025-12 发布。SOTA 推理 + 长上下文 + 视觉。
- [GPT-5](https://openai.com/index/introducing-gpt-5/) - 2025-08 发布，ChatGPT 默认模型，替代 GPT-4o。多模态 + gpt-5 / mini / nano 三档变体。
- [GPT-4o](https://openai.com/index/hello-gpt-4o/) - Omni 模型，原生支持文本/视觉/音频。2026-02 从 ChatGPT 下线，API 仍可用。
- [GPT-4.5](https://openai.com/) - 📦 **2026 年 6 月底已从 ChatGPT 退役**（API 继续可用；已有对话自动迁移至 GPT-5.5）。最初于 2025 年 2 月作为研究预览发布 —— ChatGPT 中最后一个 GPT-4 家族模型。o3 将于 2026 年 8 月 26 日从 ChatGPT 退役。
- [o3 / o4-mini](https://openai.com/index/introducing-o3-and-o4-mini/) - 思维链推理模型。2025-04 发布。o3 将于 2026-08-26 退役。
- [Codex CLI](https://github.com/openai/codex) - OpenAI 出品的开源终端编程 Agent。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fcodex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenAI Deployment Company (DeployCo)](https://openai.com/index/openai-launches-the-deployment-company/) - 🆕 **2026-05-11**。OpenAI 控股的企业 AI 落地服务公司，$4B+ 启动资金，TPG / Advent / Bain Capital / Brookfield / Goldman Sachs / SoftBank 与 Bain & Company / Capgemini / McKinsey 等共投。围绕 Forward Deployed Engineers 体系，并吸收 Tomoro 咨询团队（~150 人）。
- [Codex on Mobile](https://9to5mac.com/2026/05/14/openai-brings-codex-control-to-chatgpt-for-iphone-and-android/) - 🆕 **2026-05-14**。ChatGPT iOS / Android 远程操控 Mac 上的 Codex 桌面 App —— 查看输出、批准操作、切换模型、启动新任务，文件 / 凭据 / 权限仍留在本机。Free / Plus / Go 预览。
- [OpenAI ↔ Malta 合作](https://openai.com/index/malta-chatgpt-plus-partnership/) - 🆕 **2026-05-16**。首次国家级合作：完成马耳他大学开发的 2 小时 AI 素养课程后，所有 14 岁以上马耳他公民 / 居民可免费获得 1 年 ChatGPT Plus。"OpenAI for Countries" 计划的首站。
- [OpenAI ↔ Dell Codex 合作](https://openai.com/news/company-announcements/) - 🆕 **2026-05-18**。借助 Dell 的混合云 / 本地部署能力，Codex 首次走出公有云，面向需要数据主权 / 合规隔离的强监管行业。
- [ChatGPT 安全系统更新](https://www.edtechinnovationhub.com/news/openai-updates-chatgpt-safety-systems-to-track-risk-across-sensitive-conversations) - 🆕 **2026-05-18**。ChatGPT 加入跨会话的潜在风险跟踪（自杀 / 自伤 / 伤他），能识别微妙、逐步升级的变化。
- [OpenAI Guaranteed Capacity（算力年发）](https://openai.com/news/company-announcements/) - 🆕 **2026-05-19**。面向企业 AI 产品 / Agent / Workflow 的长期算力预订产品：1 / 2 / 3 年期，期限越长折扣越高。对度 Anthropic Priority Tier 的产品化回应。
- [OpenAI ↔ Google SynthID + C2PA 内容源头验证](https://openai.com/index/advancing-content-provenance/) - 🆕 **2026-05-19**。OpenAI 联手 Google，为 ChatGPT/Sora 生成的图片加上 **SynthID** 跨平台水印，加入 C2PA，并预览一个公开的 **"这张图是 OpenAI 生成的吗"** 验证器。两家顶级 lab 首次在水印上互通。

### Anthropic

- [Claude Fable 5 全球恢复访问](https://www.anthropic.com/news/redeploying-fable-5) - 🆕 **2026-07-01**。美国商务部于 6 月 30 日解除出口管制后，Anthropic 在 Claude.ai、Claude Platform、Claude Code、Claude Cowork 全面恢复全球访问。已部署针对 Amazon 发现的 jailbreak 的新安全分类器（对该已报告行为的拦截率 >99%）。Pro/Max/Team 与部分 Enterprise 套餐在 7 月 7 日前可将 Fable 5 用于最多 50% 的每周用量，之后通过用量额度使用；AWS、Google Cloud、Microsoft Foundry 云渠道随后恢复。Mythos 5 仍限美国受审实体。
- [Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5) - 🆕 **2026-06-30**。迄今最具 Agent 能力的 Sonnet — 支持规划、浏览器/终端工具调用，自主运行水平接近此前需要 Opus 级模型才能做到的程度。在高努力档位下，Agent 搜索（BrowseComp）与电脑操作（OSWorld-Verified）表现逼近 Opus 4.8，且相比 Sonnet 4.6 拥有更宽的性价比区间。现为 Claude.ai 免费版/Pro 版默认模型，Max/Team/Enterprise、Claude Code 及 API（`claude-sonnet-5`）均可用。截至 2026-08-31 的引导定价为输入/输出每百万 token $2/$10（之后 $3/$15）。Anthropic 称其不良行为率低于 Sonnet 4.6。
- [Claude Fable 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) - 🆕 **2026-06-09**。Anthropic 首个公开可用的 **Mythos 级别**模型——能力层级高于 Opus。在软件工程、知识工作、视觉、科研等基准全面超越 Opus 4.8。内置安全护栏（涉网络安全/生物的敏感请求可能被路由到 Opus 4.8）。$10 / $50 每百万输入/输出 token。Anthropic API、Amazon Bedrock、Google Cloud Vertex AI 可用。**⚠️ 2026-06-12 起暂停访问** —— 美国政府的出口管制指令要求 Anthropic 对所有客户停用 Fable 5 与 Mythos 5，等待安全审查。**✅ 出口管制于 2026-06-30 解除；7 月 1 日恢复访问**，并配备新的网络安全分类器 —— 见上方条目（[声明](https://www.anthropic.com/news/redeploying-fable-5)）。
- [Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) - 🆕 **2026-06-09**。与 Fable 5 同底座的 Mythos 级模型，限制更少，仅通过 **Project Glasswing**（与美国政府合作）向受信伙伴（网络安全公司、基础设施供应商）开放。4 月 Claude Mythos Preview 的正式后继。**⚠️ 2026-06-12 起暂停访问**，与 Fable 5 一同受同一出口管制指令影响（[声明](https://www.anthropic.com/news/fable-mythos-access)）。
- [Claude Opus 4.8](https://www.anthropic.com/claude/opus) - 🆕 **2026-05-28**。Opus 重大迭代：代码库级别的迁移能力、更准的 Agent 判断，推出研究预览的「动态工作流」能在单 session 里并发几百个子 Agent，加入手动调节推理投入的「努力控制」面板；**Fast 模式价格降 3 倍**，输入 / 输出仍为 $5 / $25 每百万 token。Anthropic 原生、Amazon Bedrock、AWS Claude Platform、Google Cloud、Microsoft Foundry 上线。同时预告面向小范围企业的 **Mythos 级别**新一代模型。
- [Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7) - 🆕 **2026-04-16 发布**。强软件工程能力（SWE-bench Verified 87.6%）、视觉增强、主动代码验证。支持 `/think xhigh` 推理力度。1M token 上下文。
- [Claude Opus 4.6](https://www.anthropic.com/) - 2026-02 发布。1M token 上下文，14.5 小时任务执行。LMArena 对话榜首。
- [Claude Sonnet 4.6](https://www.anthropic.com/news/claude-sonnet-4-6) - 2026-02 发布。前沿编程与 Agent 表现，1M token 上下文。
- [Claude Mythos Preview](https://www.anthropic.com/) - 🆕 2026-04 受邀研究预览。BenchLM 99（榜首），SWE-bench Verified 93.9%。Project Glasswing 合作伙伴专属。
- [Claude Opus 4](https://www.anthropic.com/news/claude-4) - 2025-05 发布。
- [Claude Sonnet 4](https://www.anthropic.com/news/claude-4) - 2025-05 发布。
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - Anthropic 出品、运行在终端里的 Agent 化编程工具。Opus 4.7 + `/think xhigh`。
- [Claude Security](https://www.anthropic.com/) - 🆕 **2026-05-01** 公测。Opus 4.7 驱动的企业级代码漏洞扫描器：扫整个代码库，生成有置信度评分、严重程度、复现步骤、修复建议的补丁。Enterprise 用户在 [claude.ai/security](https://claude.ai/security) 使用。
- [Claude Finance Agents](https://www.anthropic.com/news/finance-agents) - 🆕 **2026-05-05**。基于 Opus 4.7 的 10 个金融领域专业 Agent，覆盖 pitchbook 撰写、KYC、月结、交易筛查等。可作为 Claude Cowork 插件、Claude Code skill 或 Managed-Agents cookbook 部署。
- [Claude Finance JV](https://www.anthropic.com/) - 🆕 **2026-05-04**。与高盛、黑石的 15 亿美元 Claude 部署合资公司，把 Anthropic 工程师派驻到中型华尔街机构。
- [Claude Add-ins / Dreaming / Outcomes / Multi-agent orchestration](https://www.anthropic.com/news/code-with-claude-2026) - 🆕 **2026-05-08（Code with Claude 2026）**。Anthropic 一次性发布 Add-ins、跨会话的定期记忆回顾（"Dreaming"）、基于评分细则的 "Outcomes"，以及主 Agent + 子 Agent 编排模型，配备共享文件系统与可审计 trace。
- [Anthropic ↔ SpaceX Colossus 1](https://www.siliconrepublic.com/business/anthropic-joins-forces-with-spacex-for-colossus-capacity) - 🆕 **2026-05-06**。Anthropic 拿下 SpaceX Memphis 数据中心 Colossus 1 全部算力（22 万+ NVIDIA H100 / H200 / GB200，300+ MW）用于 Claude Opus 推理；Claude Code 5 小时速率上限翻倍，Pro / Max 取消高峰期限流。
- [Claude for Legal](https://www.anthropic.com/news/claude-for-legal) - 🆕 **2026-05-12**。Claude Cowork 之上的法律垂直栈：**20+ 个 MCP 连接器**（iManage、NetDocuments、DocuSign、Ironclad、LexisNexis、Westlaw、Harvey、Everlaw、Relativity、CourtListener 等）+ **12 个执业领域 plugin**（商事、雇佣、隐私、产品、公司、AI 治理、诉讼助理、备考律考）。原生集成 Word / Outlook / Excel / PowerPoint。
- [Claude for Small Business](https://www.anthropic.com/news/claude-for-small-business) - 🆕 **2026-05-13**。Claude Cowork 中的中小企业开关 —— 15 个预置 Agent 工作流，覆盖财务 / 运营 / 销售 / 营销 / HR / 客服；原生连 QuickBooks、PayPal、HubSpot、Canva、DocuSign、Google Workspace、Microsoft 365。配套免费课程 + 美国 10 城线下工作坊巡讲。
- [Anthropic ↔ Gates Foundation $200M](https://www.anthropic.com/news/gates-foundation-partnership) - 🆕 **2026-05-14**。4 年 $200M 合作：资助 + Claude 使用额度 + Anthropic 工程师投入到全球健康、生命科学、教育、农业，所有产出工具公开免费；首批方向包括小儿麻痹 / HPV / 子痫前期疫苗研发与农业版 Claude。
- [Anthropic ↔ PwC 战略扩张](https://www.pwc.com/us/en/about-us/newsroom/press-releases/anthropic-pwc-expand-alliance-agentic-enterprise.html) - 🆕 **2026-05-14**。PwC 全球铺开 Claude Code + Claude Cowork，认证 30,000 名员工，共建 "Agentic Enterprise" 卓越中心；聚焦 Agent 构建、AI 原生并购，以及财务 / 供应链 / HR 重塑。
- [Anthropic ↔ 金融稳定委员会（FSB）就 Claude Mythos 进行汇报](https://www.theguardian.com/technology/2026/may/18/anthropic-ai-claude-mythos-cyber-financial-stability-board-fsb) - 🆕 **2026-05-18**。Anthropic 首次向 G20 级别的金融稳定监管机构介绍顶级模型（Claude Mythos）的攻击性网络能力，为金融系统风险评估提供依据。
- [Code with Claude 2026 会议录像上线](https://www.infoq.com/news/2026/05/code-with-claude/) - 🆕 **2026-05-18 发布**。5 月 6 日的开发者大会全部场次公开：Claude Code 路线图、Claude Developer Platform 更新、Managed Agents 的 dreaming 与多 Agent 编排、合作伙伴部署。
- [《Widening the conversation on frontier AI》](https://www.anthropic.com/news/widening-conversation-ai) - 🆕 **2026-05-19**。Anthropic 发布与宗教 / 哲学 / 原住民传统等“智慧传统”就顶级 AI 安全展开对话的框架，公共参与系列后续。
- [Bristol Myers Squibb ↔ Anthropic Claude Enterprise](https://news.bms.com/news/corporate-financial/2026/Bristol-Myers-Squibb-Announces-Strategic-Agreement-with-Anthropic-to-Position-Claude-Enterprise-as-the-Shared-Intelligence-Platform-Across-Its-Global-Operations/default.aspx) - 🆕 **2026-05-20**。BMS 将 Claude Enterprise 作为 30,000+ 员工的共享智能平台，嵌入药物发现 / 开发 / 交付的全链路。全球前 5 大药企中首个全公司级 Claude 部署。

### Google DeepMind
- [Gemini 3.5 Pro](https://cloud.google.com/blog/products/ai-machine-learning/innovations-from-google-io-26-on-google-cloud) - ⚠️ **延期 —— 截至 2026-07-17 尚未发布**（面向合作伙伴的企业限量预览进行中）。Google 即将推出的旗舰模型，据报道具备 **200 万 token 上下文**和 **Deep Think** 推理模式，编程与 Agent 工作流能力显著提升。2026 年 5 月 Google I/O 上宣布原定 6 月发布，后因编程表现不理想、Google 推倒重建基座模型而推迟。第三方报道曾指向 7 月 17 日，但截至 7 月 16 日 Google 表示仍在测试 3.5 Pro（连同升级版 Flash 模型），无确认发布日期。直接对标 GPT-5.6 Sol 和 Claude Fable 5。
- [Gemma 4 12B](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/) - 🆕 **2026-06**。新型多模态开源模型，采用**统一无编码器架构**，在单次计算中同时处理文本、图像和音频。支持在 16GB VRAM 显存下本地运行。
- [DiffusionGemma](https://www.marktechpost.com/2026/06/10/google-ai-releases-diffusiongemma-a-26b-moe-open-model-using-text-diffusion-for-up-to-4x-faster-generation/) - 🆕 **2026-06**。采用**文本扩散 (text-diffusion)** 架构的 26B MoE 开源模型，生成速度比自回归模型快最高 **4 倍**。

- [Gemini 3.5 Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - 🆕 **2026-05-19 — Google I/O 2026**。推出即成为 Gemini App + Google 搜索 AI Mode 的默认模型，官方称输出 token 速度 **约 4 倍于**同类顶级模型，在关键 benchmark 上超越 Gemini 3.1 Pro。Gemini 3.5 Pro 原定 2026 年 6 月上线，现已延期（见上）。
- [Gemini Omni / Omni Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - 🆕 **2026-05-19 — Google I/O 2026**。DeepMind 面向 AGI 的新**世界模型**家族，Omni Flash 能从**任意输入输出任意模态**（首以视频起步，后续拓展到图像与文本），与 Gemini Robotics / Genie 路线一脉相承。
- [Gemini 3.1 Pro](https://deepmind.google/technologies/gemini/) - 2026-02 发布。BenchLM 94，GPQA Diamond 94.3%（世界纪录），ARC-AGI 2 77.1%。旗舰定价 `$2/1M tokens`。
- [Gemini 3.1 Flash Live](https://deepmind.google/technologies/gemini/) - 🆕 2026-04。语音助手与交互式 Agent 的实时多模态流式接口，低延迟长上下文。
- [Gemini 3.1 Flash-Lite (GA)](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-lite-is-now-generally-available) - 🆕 **2026-05-08**。Gemini API / AI Studio / Vertex AI 全面 GA。Gemini 3 家族中最快、最省的型号，面向超低延迟代码补全、实时 UX、Agent 开发工具；质量持平 Gemini 2.5 Flash，成本明显更低。
- [Gemini Omni Flash · 对话式视频编辑上线](https://www.techtimes.com/articles/317309/20260528/google-gemini-omni-flash-brings-voice-controlled-ai-video-editing-future-conversational-ai.htm) - 🆕 **2026-05-28**。Omni Flash 面向消费者推送，在 Gemini App、**Google Flow**和 **YouTube Shorts** 里作为编辑引擎：用文字 / 语音 / 图像 / 音频提示完成电影式推拉镜、背景替换、天气改动等操作，不再需要传统非线性编辑。
- [Gemini Spark（24/7 个人 AI Agent）](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - 🆕 **2026-05-19 — Google I/O 2026**。云端 24/7 常驻的个人 AI Agent，首期接入 Gmail / Chat，后续加入 ~30+ 个第三方工具（Adobe / Dropbox / Uber 等）以 MCP 協议调用。限 Google AI Ultra 付费用户。
- [Google AI Ultra（$100/月）](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - 🆕 **2026-05-19 — Google I/O 2026**。新的消费者顶端订阅层级，面向开发者 / 创作者 / 重度用户，解锁 Gemini Spark、最高 Gemini 3.5 额度以及即将发布的 Gemini 3.5 Pro。
- [Gemini 3.1 Flash / Flash Lite](https://deepmind.google/technologies/gemini/) - 高吞吐应用的高性价比选择。
- [Gemini 4 (Open)](https://deepmind.google/technologies/gemini/) - 🆕 2026-04 发布。开源家族：2B / 4B / 26B / 31B 变体。科学推理与文档理解强，本地部署友好。
- [Gemini 2.5 Pro / Flash](https://deepmind.google/technologies/gemini/) - 2025-06 GA。Thinking 模型，1M 上下文。
- [Gemma 4 31B](https://github.com/google-deepmind/gemma) - 🆕 2026-04。GPQA Diamond 84.3%。端侧推理首选开源权重之一。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle-deepmind%2Fgemma&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Gemma 3](https://github.com/google-deepmind/gemma) - 上一代开源家族。
- [Gemini Robotics ER-1.6](https://deepmind.google/) - 🆕 2026-04-14。机器人 AI 模型，空间与物理推理增强。Agile Robotics 实地部署。

### Meta

- [Muse Image](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) - 🆕 **2026-07-07**。Meta Superintelligence Labs 最新图像生成模型 —— “Agent 式”架构，在生成图像前能自动完成网页搜索、代码执行、自我修正等中间步骤。已集成到 Meta AI 应用、Instagram Stories（美国）与限定国家的 WhatsApp（Facebook 即将上线）。注：一项允许使用其他用户公开 Instagram 头像生成图像的争议功能上线后，因用户反馈于 7 月 10 日下线。
- [Muse Spark 1.1](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/) - 🆕 **2026-07-09**。面向 Agent 任务的多模态推理模型，通过新的 Meta Model API 公开预览发布。标志着 Meta 在开源 Llama 路线之外开始构建专有商业模型。
- [Muse Video](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) - 🆕 **2026-07-07（预览）**。Meta Superintelligence Labs 的视频生成模型，与 Muse Image 同底座；Arena 文生视频榜第 3。随 Muse Image 发布一同预览 —— “即将面向创作者与 Meta AI 开放”。
- [Llama 5](https://ai.meta.com/llama/) - 🆕 **2026-04-08**。Meta 超级智能实验室发布的 600B+ 参数开源旗舰；“递归自我改进” 研究路线。官方宣称在推理、代码、自主 Agent 行为上超越主流闭源模型。
- [Muse Spark](https://ai.meta.com/blog/introducing-muse-spark-msl/) - 🆕 **2026-04-09**。Meta Superintelligence Labs (MSL) 首个模型。原生多模态推理，驱动 Meta AI 应用、智能眼镜，以及 Facebook / Instagram / WhatsApp / Messenger 中的功能。
- [Llama 4 Scout](https://llama.meta.com/) - 109B 总参（17B 激活），16 专家 MoE，10M token 上下文，多模态。单 H100 可跑。
- [Llama 4 Maverick](https://llama.meta.com/) - 400B 总参（17B 激活），128 专家，1M 上下文。多模态超过 GPT-4o。
- [Llama 4 Behemoth](https://llama.meta.com/) - 2T 总参（288B 激活）。Meta 最强模型，对标顶级闭源。
- [Llama 3.3 70B](https://llama.meta.com/) - 强指令跟随，Llama Community License。

### Sakana AI

- [Sakana RL Conductor](https://venturebeat.com/orchestration/how-sakana-trained-a-7b-model-to-orchestrate-gpt-5-claude-sonnet-4-and-gemini-2-5-pro) - 🆕 **论文 2026-04-27 / Fugu beta 2026-04 末至 2026-05 初**。基于 Qwen2.5-7B 的 RL 训练编排模型，用强化学习把子任务分发给 GPT-5、Claude Sonnet 4、Gemini 2.5 Pro 等。LiveCodeBench 83.9%、GPQA-Diamond 87.5% SOTA，每次查询约 1.8K token，远低于其他多 Agent 合奏。
- [Sakana Fugu](https://sakana.ai/fugu-beta/) - 🆕 **2026-04-24 / 25 公测**。把 RL Conductor 研究产品化的多 Agent 编排商用服务，兼容 OpenAI 接口，分 **Fugu Mini**（低延迟）和 **Fugu Ultra**（最大性能）两档；在 SWE-Pro、GPQA-D、ALE-Bench 表现亮眼。

### Zyphra

- [ZAYA1-8B](https://www.zyphra.com/post/zaya1-8b) - 🆕 **2026-05-06**。MoE 推理模型（激活参数 <1B），完全在 AMD Instinct MI300X 集群上训练。Apache 2.0 权重已在 Hugging Face，并在 Zyphra Cloud 提供 serverless 端点；强调每激活参数的智能密度。
- [ZAYA1-8B-Diffusion-Preview](https://www.zyphra.com/post/zaya1-8b-diffusion-preview) - 🆕 **2026-05-14**。首个从自回归 LLM 转换得来的 MoE 扩散语言模型，也是首个在 AMD GPU 上训练的扩散 LM。每步生成 16 个 token，相比自回归基线最多 **7.7× 推理加速**；采用 Zyphra 的 TiDAR 训练配方 + CCA 注意力。

### Mistral AI

- [Mistral Medium 3.5](https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04) - 🆕 **2026-04-28**。Dense 128B 开放权重模型，256K 上下文，Modified MIT 许可。统一指令跟随、推理与代码能力。
- [Leanstral 1.5](https://mistral.ai/news/leanstral-1-5/) - 🆕 **2026-07-02**。面向 Lean 4 证明工程的形式化验证模型 —— 119B 总 / 6B 激活参数，Apache 2.0，权重上 Hugging Face 并提供免费 API 端点。miniF2F 得分 100%，解决 PutnamBench 672 题中的 587 题，并在 57 个真实仓库中发现 5 个此前未被报告的 bug。
- [Robostral Navigate](https://mistral.ai/news/robostral-navigate/) - 🆕 **2026-07-08**。Mistral 首个机器人模型 —— 8B 具身导航模型，仅凭单个 RGB 摄像头即可让轮式、足式与飞行机器人根据自然语言指令穿行办公室、家庭与户外环境（未见过的验证场景成功率 76.6%）。完全自研，基于约 40 万条仿真轨迹训练。
- [Voxtral TTS](https://www.forbes.com/sites/ronschmelzer/2026/03/26/mistral-releases-open-weight-voice-ai-built-for-speed/) - 🆕 **2026-03-26**。基于 Ministral 3B 的 4B 参数开放权重 TTS；多语种，专为语音 Agent 优化延迟。
- [Mistral Large 3](https://mistral.ai/news/mistral-3) - 675B 总 / 41B 激活 MoE，256K 上下文。多模态旗舰开源。2025-12 发布。
- [Mistral Medium 3.1](https://mistral.ai/) - 企业级前沿密集模型。多模态，128K，支持 80+ 编程语言。2025-08 发布。
- [Mistral Small 4](https://mistral.ai/news/mistral-small-4) - 🆕 2026-03。119B 总 / 6B 激活。融合推理 + 多模态 + 编程的混合模型。
- [Magistral 1.2](https://mistral.ai/) - 🆕 2026 推理家族。透明、多语言推理。
- [Devstral 2](https://mistral.ai/) - 🆕 2026 Agent 编程模型。当前最佳开源编程 Agent 模型。
- [Codestral](https://mistral.ai/news/codestral) - 22B 编程模型，80+ 语言，32K 上下文。2024-05 发布。
- [Pixtral Large](https://mistral.ai/) - 124B 多模态 + 1B 视觉编码器，128K 上下文，支持 30+ 高分辨率图像。
- [Ministral 3B/8B/14B](https://mistral.ai/) - 端侧紧凑模型。
- [Mistral Forge](https://mistral.ai/) - 🆕 2026-03 自定义 LLM 训练平台。

### DeepSeek 🇨🇳

- [DeepSeek-V4-Pro](https://api-docs.deepseek.com/news/news260424) - 🆕 **2026-04-24（预览）；2026 年 7 月中旬正式上线**。1.6T 总 / 49B 激活 MoE，1M 上下文。MIT。Agent、世界知识、推理领域开源标杆。V4 正式发布引入高峰/低谷分时 API 定价（北京高峰时段 2 倍）；deepseek-v4-pro / deepseek-v4-flash 现为生产 API 模型。
- [DeepSeek-V4-Flash](https://api-docs.deepseek.com/news/news260424) - 🆕 2026-04-24。284B 总 / 13B 激活 MoE，1M 上下文。MIT。性价比层。
- [DeepSeek Agent Harness 团队](https://www.scmp.com/tech/big-tech/article/3354113/deepseek-recruits-former-jane-street-engineer-catch-ai-agents-revenue-race) - 🆕 **2026-05-19**。DeepSeek 从 Jane Street 挨角一名资深工程师，为新设的 "AI harness" 团队搭建把 DeepSeek V4 所能生产化为 **能收费的自主 Agent** 的硬调度 / 程序化套件 —— 首个明确信号：DeepSeek 开始从原生模型 R&D 跳到 Agent 产品化。
- [DeepSeek-V3.2](https://www.deepseek.com/) - 2025-12 发布。671B MoE，V3.2 Speciale 推理增强。⚠️ V3.2 时代的 API 模型 ID deepseek-chat / deepseek-reasoner 将于 2026-07-24 弃用 —— 由 V4-Flash 各模式接替。
- DeepSeek-R2 - 🧪 **未发布 / 传闻。** 截至 2026 年 7 月中旬无官方公告、模型卡或 API ID；推理能力通过 V4 的 Thinking 模式提供。
- [DeepSeek-R1](https://www.deepseek.com/) - 2025-01 发布的思维链推理模型。
- [DeepSeek-Coder-V2](https://github.com/deepseek-ai/DeepSeek-Coder-V2) - 编程模型，对标 GPT-4。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeepseek-ai%2FDeepSeek-Coder-V2&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Alibaba (Qwen) 🇨🇳

- [Qwen 3.7-Max](https://www.scmp.com/tech/big-tech/article/3354212/alibaba-unveils-new-qwen-model-custom-chips-bid-become-chinas-ai-factory) - 🆕 **2026-05-20 — 阿里云杭州峰会**。为 AI Agent 量身打造的新一代顶级：代理型编程、复杂推理、「长静间距」多步任务能力；同期亊相新的 T-Head **珄武 M890** AI 算力芯片与全栈 AI 基础设施升级。面向全球开发者 / 企业即将上线。
- [Qwen 3.7-Max-Preview / Plus-Preview](https://www.scmp.com/tech/tech-trends/article/3354087/alibaba-teases-new-qwen-previews-highest-ranking-chinese-ai-models-arena) - 🆕 **2026-05-18**。杭州峰会前的预览梯队；LM Arena 上文本 + 视觉双赛道均为**中文世界最高分**中国模型。
- [Qwen3.6-27B](https://qwen.ai/blog?id=qwen3.6-27b) - 🆕 **2026-04-22**。27B 密集多模态。开源。Agent 编程 + 思维上下文保持。
- [Qwen3.6-Max-Preview](https://qwen.ai/) - 🆕 **2026-04-18**。闭源前沿预览。1M 上下文，中文模型编程榜顶尖。
- [Qwen3.6-35B-A3B](https://qwen.ai/blog?id=qwen3.6-35b-a3b) - 🆕 **2026-04-15**。MoE 35B 总 / 3B 激活。Apache 2.0。稳定性与实用性增强。
- [Qwen3.6-Plus](https://qwen.ai/) - 🆕 **2026-04-02**。闭源旗舰。token 性价比高，长上下文 + 工具调用 + Agent 表现强。
- [HappyHorse 1.1](https://technode.com/2026/06/23/alibaba-unveils-happyhorse-1-1-video-generation-model-launches-global-ai-filmmaking-competition/) - 🆕 **2026-06-23**。阿里视频生成模型（T2V/I2V/S2V，最长 15 秒 1080p 带同步音频，多镜头角色一致性强）。HappyHorse 1.0 曾匿名上线并登顶视频榜单，2026-04-28 进入限量公测。
- [Qwen3.5 Max Pro](https://qwen.ai/) - 2026-04。高性能旗舰。
- [Qwen3.5 Omni Plus](https://qwen.ai/) - 2026-04。统一文本 + 图像输入的全模态基座。
- [Qwen3-Max-Thinking](https://qwen.ai/) - 阿里最强思维模型。1T+ 参数。
- [Qwen3.5-Omni](https://qwen.ai/) - 2026-03。完全全模态：文/视/听/动。113 种语言识别，256K 上下文。
- [Qwen3-Coder-Next](https://qwen.ai/) - 2026-02。开源编程 Agent 模型，MoE 80B 总 / 3B 激活。
- [Qwen3 235B-A22B](https://qwen.ai/) - 双模式推理 MoE。数学、代码、常识强。
- [Qwen2.5 Coder 32B](https://github.com/QwenLM/Qwen2.5-Coder) - 顶级开源编程模型。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FQwenLM%2FQwen2.5-Coder&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### xAI (Grok)

- [Grok 4.5](https://x.ai/) - 🆕 **2026-07-08**。xAI 最新旗舰 —— 与 Cursor 共同训练，利用真实开发者交互数据优化编程与 Agent 能力。支持 500K token 上下文、函数调用、结构化输出、web/X 搜索、代码执行、文档搜索与上下文压缩。可用于 xAI API、Grok Build，并为 Cursor 默认模型。定价 $2/$6 每百万 token。
- [Grok 4.3 GA](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-grok-4-3-on-microsoft-foundry-latest-generation-agentic-capabilities/4517096) - 🆕 **2026-05**。Grok 4.3 在 Microsoft Foundry 与 OCI Generative AI 上 GA；xAI 面向 Agent 工作负载的旗舰，工具调用与长链推理能力升级。
- [Grok 4.3 Beta](https://x.ai/) - 🆕 2026-04。最新迭代，推理与编程基准提升，详见 [`2026.4` benchmark snapshot](https://benchlm.ai/)。
- [Grok 4.20](https://x.ai/) - 2026-02。多 Agent 系统（Heavy 模式 4 标准 + 16 专家 Agent），2M 上下文。
- [Grok 4 / 4 Heavy](https://x.ai/) - 2025-07 发布。xAI Grok 4 世代的前沿模型。
- [Grok 3 / 3 Mini](https://x.ai/) - 2025-02。首批 "Think Mode" 推理模型。

### Microsoft (MAI)

- [Microsoft MAI-Code-1-Flash](https://microsoft.ai/news/introducingmai-code-1-flash/) - 🆕 **Build 2026（2026 年 6 月 2 日）**。微软首个完全脱离 OpenAI 技术、从零自研的编程基础模型。5B 参数，自适应思考长度，已上线 GitHub Copilot。在四大核心编程基准上击败 Claude Haiku 4.5（SWE-Bench Pro 51.2% vs 35.2%，领先 16 分），SWE-Bench Verified 任务最多省 60% token。
- [Microsoft MAI-Thinking-1](https://microsoft.ai/news/microsoft-build-2026-mai-keynote-transcript/) - 🆕 **Build 2026（2026 年 6 月 2 日）**。微软首个完全脱离 OpenAI 数据、从零自训的推理模型；与 MAI-Code-1-Flash 同发，标志微软的基础模型独立进程。

### Microsoft (Phi)

- [Phi-4-reasoning-vision-15B](https://azure.microsoft.com/en-us/products/phi) - 🆕 2026-03。15B 多模态，选择性思维链推理。端侧友好。
- [Phi-4](https://azure.microsoft.com/en-us/products/phi) - 14B SLM，推理水平媲美更大模型。MIT。
- [Phi-4-mini](https://azure.microsoft.com/en-us/products/phi) - 3.8B 密集，128K 上下文。推理 / 数学 / 编程 / 函数调用都强。
- [Phi-4-multimodal](https://azure.microsoft.com/en-us/products/phi) - 5.6B 首个多模态 Phi（语音 + 视觉 + 文本）。

### Cohere

- [Command A+](https://cohere.com/blog/command-a-plus) - 🆕 **2026-05-20**。218B 总 / 25B 激活 MoE，Apache 2.0 开源权重（Hugging Face）。128K 输入 / 64K 输出。多模态、48 种语言、Agent 工具调用；2× H100 或 1 块 Blackwell GPU 即可运行。
- [Command A](https://docs.cohere.com/v2/changelog/command-a) - 2025-03-13 发布。111B 开源权重，256K 上下文。Agent / 多语言 / 编程聚焦。
- [Command R+](https://cohere.com/) - 企业级 RAG 模型，128K 上下文，10 种语言，带引用 grounded generation。
- [Command R](https://cohere.com/) - 经济型 RAG 模型。

### Baidu (ERNIE / 文心) 🇨🇳

- [ERNIE 5.1](https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/) - 🆕 **2026-05-08**。总参数约为 ERNIE 5.0 的 1/3、激活参数约 1/2，预训练成本仅约为同级的 6%；LMArena Search 中文模型第一 / 全球第四（1,223）。
- [ERNIE 5.0](https://ernie.baidu.com/) - 2025-11-13 发布（百度世界大会）。2.4T 参数全模态 MoE（每次激活 <3%）。
- [ERNIE 4.5](https://yiyan.baidu.com/) - 2025 多模态前作。中文与推理强。

### Zhipu AI / Z.ai (GLM) 🇨🇳

- [GLM-5.2](https://z.ai/blog/glm-5.2) - 🆕 **2026-06-13**。编程优先的 744B MoE 旗舰，**100万 token 上下文**（约为 GLM-5.1 的 5 倍），输出最高 131K token。已上线全部 GLM Coding Plan 套餐；MIT 开源权重 + 独立 API 于发布当周陆续放出。开箱兼容 Claude Code、Cline、OpenCode、Roo Code、Goose、OpenClaw。（发布时未公布基准分数。）
- [GLM-5.1](https://z.ai/blog/glm-5.1) - 🆕 **2026-04-08**。744B MoE / 40B 激活，200K 上下文。MIT。SWE-Bench Pro 第一。
- [ZCode](https://www.scmp.com/tech/tech-trends/article/3359170/zhipu-ai-releases-harness-glm-52-model-chinese-firm-takes-aim-anthropic) - 🆕 🇨🇳 **2026-07-02**。智谱为 GLM-5.2 打造的 Agent harness —— 把模型变成自主编程 Agent，正面对标 Claude Code；发布促销包括 Coding Plan 订阅用户 +50% 配额、新用户 500 万免费 token。
- [GLM-5 Reasoning](https://z.ai/) - 🆕 2026-04。BenchLM 85 —— **开源最高分**。SWE-Bench Pro 超过 GPT-5.4 与 Claude Opus 4.6。
- [GLM-5V-Turbo](https://z.ai/) - 🆕 2026-04。原生多模态 Agent —— 视觉、视频片段、文本输入。性价比平衡。
- [GLM-5](https://z.ai/) - 2026-02 发布。744B 参数，Agent 能力前沿。MIT。
- [GLM-4.7](https://z.ai/) - 2025 末发布。SWE-Bench 持平 Claude Opus 4。

### MiniMax

- [MiniMax M3](https://www.minimax.io/) - 🆕 **2026-06-01**。开源权重（MIT）旗舰，采用 MiniMax Sparse Attention —— 1M token 下计算成本约为 1/20；前沿编程能力，SWE-Bench Pro 59.0%，BrowseComp 83.5%。
- [MiniMax-M2.7 (开源权重)](https://www.minimax.io/) - 🆕 2026-04。230B 级开源权重旗舰。编程与 Agent 任务顶级表现。
- [MiniMax M2.7（闭源）](https://venturebeat.com/technology/new-minimax-m2-7-proprietary-ai-model-is-self-evolving-and-can-perform-30-50) - 🇨🇳 🆕 **2026-03**。自演化闭源 LLM，针对 Agent 框架搭建、记忆更新、工作流迭代优化；SWE-bench 类任务大幅提升。
- [MiniMax M2.5](https://www.codemotion.com/magazine/ai-ml/minimax-m2-5-low-costs-high-performance/) - 🇨🇳 **2026-02**。230B 参数旗舰，主打 "真实世界生产力" 与高性价比。
- [Hailuo 2.3 / 2.3 Fast](https://www.minimax.io/news/minimax-hailuo-23) - 🇨🇳 **2025-10**。MiniMax 当前视频旗舰 —— SOTA 物理效果、角色微表情、强风格化；Hailuo 02（2025）仍作为聚焦 I2V 的变体保留。
- [MiniMax Music 2.6](https://aimlapi.com/blog/the-ultimate-guide-to-minimax-models-2026-m2-7-music-2-6-hailuo-video-advanced-tts) - 🇨🇳 🆕 **2026-04-10**。主打翻唱生成方向，低频还原显著改进；全球 beta。
- [MiniMax-M1-80k](https://www.minimax.io/) - 开源混合注意力推理模型。456B 参数，1M token 上下文。
- [Hailuo AI (视频)](https://hailuoai.video/) - 文生 / 图生视频，AI 主播 + 配音 + 角色一致性。
- [Kilo Code 集成](https://www.minimax.io/) - MiniMax 系列模型在 Kilo Code（kilo.ai 的开源 AI 编程扩展）中被重点采用。

### Moonshot AI (Kimi) 🇨🇳

- [Kimi K3](https://kimi.ai/) - 🆕 **2026-07-16**。Moonshot AI 最大旗舰：**2.8T 参数**稀疏 MoE（每个 token 激活 896 个专家中的 16 个），**1M token 上下文窗口**，原生视觉与多 Agent 能力。引入 Kimi Delta Attention（混合线性注意力，加速长上下文解码）。API：每百万输入/输出 token \$3.00 / \$15.00。可通过 kimi.com、Kimi API 及各集成平台使用；**承诺于 2026 年 7 月下旬开源全量权重**。
- [Kimi K2.7 Code](https://kimi.ai/) - 🆕 **2026-06-12**。K2.6 的编程优先继任者 —— 1T MoE / 32B 激活（384 专家），256K 上下文，Modified MIT，已上 Hugging Face + Kimi API。面向长程 Agent 编程，推理 token 用量约降 30%；官方 Kimi Code Bench v2 较 K2.6 +21.8%（厂商基准）。每百万输入/输出 0.95 / 4.00 美元。
- [Kimi K2.6](https://kimi.ai/) - 🆕 **2026-04-20~21**。1T MoE / 32B 激活，256K 上下文。编程增强、长任务执行、**最大 1000 个 Agent 协作集群**。支持 `thinking.keep="all"` 持久推理。OpenClaw v2026.4.20+ 默认模型。
- [Kimi K2.5](https://kimi.ai/) - 2026-01 至 02。1T 总 / 32B 激活 MoE。原生多模态，最多 100 个并行子 Agent。开源。⚠️ **2026-05-25 停止支持**，请迁移到 K2.6。
- [Kimi Code](https://kimi.ai/) - 基于 K2.5/K2.6 的高级编程层，面向终端工作流。

### ByteDance (Doubao / 豆包) 🇨🇳

- [Doubao 2.0](https://www.taipeitimes.com/News/biz/archives/2026/02/16/2003852382) - 🇨🇳 🆕 **2026-02**。面向 Agent 时代的升级，专注真实任务执行；驱动字节跳动多款消费级 AI 应用。
- [Seedance 2.0](https://economictimes.indiatimes.com/us/news/seedance-2-0-goes-live-as-bytedances-ai-videos-ignite-china-market-rally/articleshow/128150649.cms) - 🇨🇳 🆕 **2026-02**。多模态电影级视频生成，2K 分辨率，比 Seedance 1.5 快约 30%。
- [Doubao-Seed-2.0 Pro](https://seed.bytedance.com/) - 🆕 2026-02 发布。前沿推理与复杂 Agent。和 GPT-5.2 同级，成本约低 90%。
- [Doubao-Seed-2.0 Lite](https://seed.bytedance.com/) - 🆕 通用生产负载。性能效率均衡。
- [Doubao-Seed-2.0 Code](https://seed.bytedance.com/) - 🆕 软件开发：代码生成、调试、评审。
- [BAGEL](https://github.com/bytedance-seed/BAGEL) - 🆕 字节开源多模态模型，文图视频统一理解 + 生成。

### Amazon (Nova)

- [Nova 2 Pro](https://aws.amazon.com/nova/) - **2025-12-02（re:Invent）**。Amazon 最强推理模型。文 / 图 / 视频 / 语音输入。Agent 编程与长程规划。
- [Nova 2 Lite](https://aws.amazon.com/nova/) - **2025-12-02**。快速、高性价比推理，1M token 上下文 + 可调 "thinking effort"。
- [Nova 2 Sonic](https://aws.amazon.com/nova/) - **2025-12-02**。实时语音对语音模型。多语言。
- [Nova Act](https://aws.amazon.com/nova/) - **2025-12-02**。浏览器 Web 任务 Agent 服务，由 Nova 2 Lite 驱动重新上线。
- [Nova Forge](https://aws.amazon.com/nova/) - **2025-12-02**。用自有数据构建自定义 Nova 变体的 "open training" 服务。

### NVIDIA (Nemotron)
- [Nemotron 3.5 ASR](https://developer.nvidia.com/nemotron) - 🆕 **2026-06-06**。NVIDIA 6 亿参数的 cache-aware 流式语音识别模型 —— 覆盖 40 个语言区域的实时转录。
- [Nemotron 3 Ultra (550B)](https://research.nvidia.com/labs/nemotron/Nemotron-3-Ultra/) - 🆕 **2026-06-04**。开源权重 550B 总 / 55B 激活的混合 Mamba-Transformer MoE，面向长时运行 Agent。美国开源模型中的前沿推理水平，为 Blackwell 优化。
- [Nemotron-Labs-TwoTower](https://huggingface.co/nvidia/Nemotron-Labs-TwoTower-30B-A3B-Base-BF16) - 🆕 🧪 **2026-07-01**。NVIDIA Research 的开源权重扩散语言模型，改造自冻结的 Nemotron-3-Nano-30B-A3B 底座 —— 一座塔保持上下文，另一座塔并行输出 token，无需重训即可获得约 2.4× 吞吐。
- [Nemotron 3 Super](https://developer.nvidia.com/nemotron) - 🆕 2026-03-11 发布（GTC）。120B 总 / 12B 激活。1M 上下文。吞吐较前代提升 5 倍。
- [Nemotron 3 Nano](https://developer.nvidia.com/nemotron) - **2025-12-15**。经济型 Transformer-Mamba 混合 MoE。为目标化 Agent 任务优化。
- [Nemotron 3 Nano Omni](https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/) - 🆕 **2026-04-28**。30B-A3B 混合 MoE。原生多模态。同类开源 omni 模型 9 倍吞吐。霸榜 6 项排行（MMlongbench-Doc / OCRBenchV2 / WorldSense / DailyOmni / VoiceBench）。

### Tencent (Hunyuan) 🇨🇳

- [Hunyuan Hy3](https://hy.tencent.com/research/hy3) - 🆕 🇨🇳 **2026-07-06**。Hy3 正式版（295B 总 / 21B 激活 MoE，256K 上下文），Apache 2.0。相较 4 月预览版强化了强化学习，稳定性与成本效率更好。权重上 Hugging Face 与 ModelScope，OpenRouter 陆续上线。已集成到元宝、CodeBuddy、WorkBuddy、ima、Marvis 及微信客服。
- [Hunyuan Hy3 Preview](https://hy.tencent.com/hy3-preview) - 🇨🇳 **2026-04**。Hy3 正式版之前的预览版："快慢思维融合" 架构，推理效率提升 40%，支持 vLLM 与 SGLang。GitHub / Hugging Face / ModelScope / GitCode 同步开源。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTencent-Hunyuan%2FHy3-preview&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Apple

- [Apple Foundation Models (AFM)](https://machinelearning.apple.com/research/introducing-apple-foundation-models) - 端侧（~3B）+ 服务器版本，Apple Intelligence 内核。隐私优先，离线可用。**WWDC 2026（6 月 8 日）**：第三代 AFM 阵容（端侧 AFM Core、AFM Core Advanced；Private Cloud Compute 上的 AFM Cloud、AFM Cloud Pro）驱动全新 Siri。训练借助定制的 Google Gemini 基座（约 $10 亿/年协议）经蒸馏完成，但不包含任何 Google 代码。iOS 27 新的 "Extensions" 框架允许 ChatGPT、Claude 或 Gemini 作为第三方 AI 与 Siri 并行工作。
- [OpenELM](https://machinelearning.apple.com/research/openelm) - 开源高效语言模型（270M~3B），Apple Silicon 端侧。

### Samsung

- [Samsung Gauss 2.3](https://www.sammobile.com/news/samsung-develops-own-agentic-ai-tools-improves-gauss-ai-models/) - **2025-11**。三星研究院自研 LLM 家族（Gauss 2.3、Gauss 2.3 Think、Gauss O Flash），驱动内部 Agent 工具；支撑 Galaxy S26（2026 年上市）系统级 Agent AI。

### StepFun 🇨🇳

- [Step 3.7 Flash](https://github.com/stepfun-ai/Step-3.7-Flash) - 🆕 🇨🇳 **2026-05-29**。面向编程 Agent 与搜索工作流的开源权重 198B MoE 视觉-语言模型；最高约 400 tokens/s。Step 3.5 Flash 的继任者。
- [Step 3.5 Flash](https://github.com/stepfun-ai/Step-3.5-Flash) - 🇨🇳 **2026-02**。开源权重 196B MoE（11B 激活）推理 + Agent 模型；以小搏大，对标更大体量的旗舰。

### Baichuan 🇨🇳

- [Baichuan-M3 Plus](https://pandaily.com/baichuan-ai-launches-low-hallucination-medical-model-m3-plus-announces-free-access-program) - 🇨🇳 🆕 **2026-01**。证据锚定的医疗 LLM，幻觉率显著降低；面向国内医疗机构提供免费 API。

### Inflection AI

- [Inflection 2.5 / Pi](https://inflection.ai/) - 💤 偏共情对话的 AI（Inflection 2.5，2024 年 3 月）。公司在微软吸收其大部分团队（2024 年）后转向企业 AI，不再研发下一代前沿模型。Pi 仍以有限形式可用。

### 01.AI 🇨🇳

- [Yi-Lightning](https://www.01.ai/) - 💤 MoE，RTX 4090 上 200+ tokens/s。中英双语强。2024-10 发布 —— 01.AI 最后一个主力模型；公司于 2025 年 3 月停止 LLM 预训练，转向基于 DeepSeek 的企业解决方案。

### 中国科学院 🇨🇳

- [ScienceOne 100 / 磐石100](https://english.cas.cn/newsroom/cas-in-media/202604/t20260429_1158251.shtml) - 🆕 **2026-04-28~29**。中科院科研 AI 系统。"磐石" 基础模型 + 文献罗盘 + 创新评估引擎 + 2000+ 工具 Agent 工厂。覆盖数学 / 物理 / 生物 / 材料 / 天文 / 航天 / 地球科学。50+ 中科院研究所、100+ 科研场景使用。

---

## 🎨 多模态与生成式 AI

*生成与编辑图像、视频、音频、音乐的工具与模型。*

### 图像生成

- [Meta Muse Image](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) - 🆕 **2026-07-07**。Meta MSL 最先进的图像生成模型 —— Agent 式设计，在出图前执行网页搜索、代码执行与自我修正。已在 Instagram Stories（美国）与限定国家的 WhatsApp 上线（Facebook 即将上线）；也可在 Meta AI 应用与 meta.ai 使用。
- [Midjourney V8.1](https://updates.midjourney.com/v8-1-alpha/) - 🆕 **2026-04-14**。HD 模式成为默认（快 3 倍 / 更便宜），moodboard 与风格参考稳定可用，恢复图像提示；仅在 alpha.midjourney.com 提供。V8 upscaler 与编辑/inpaint 升级为下一步计划。
- [FLUX.2 Pro / Flex / Dev / Klein](https://bfl.ai/blog/flux-2) - 🆕 **2025-11-25**。Black Forest Labs 的下一代家族；SOTA 画质、多参考一致性（最多 10 张图），文本渲染显著提升；开源权重 32B Dev 变体。
- [Recraft V4 / V4.1](https://www.recraft.ai/blog/introducing-recraft-v4-design-taste-meets-image-generation) - 🆕 **2026-02-17**（V4.1 **2026-05-14**）。从零重构；提示准确度大幅改进；支持可编辑 SVG 矢量输出。V4.1 增强写实感、3D/渐变效果，并新增 Vector/Utility 变体。
- [Stable Diffusion 3.5](https://stability.ai/) - 开源图像生成，连贯性与提示跟随增强。
- [Ideogram 3.0](https://ideogram.ai/) - 文字渲染与设计向特别强。
- [ChatGPT Images 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/) - 🆕 **2026-04-21**。SOTA 图像生成：文字渲染、多语言支持、高级视觉推理与多轮迭代编辑全面增强。
- [gpt-image-2](https://developers.openai.com/api/docs/models/gpt-image-2) - 🆕 **2026-04-21**。OpenAI 最新图像生成/编辑 API 模型，支持灵活尺寸与高保真输入。
- [DALL·E 3](https://openai.com/dall-e-3) - 集成在 ChatGPT 中迭代生成。
- [Gemini 3 Pro Image (Nano Banana Pro)](https://deepmind.google/models/gemini-image/pro/) - Gemini 内原生图像生成。
- [Nano Banana 2 (Gemini 3.1 Flash Image)](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/) - 🆕 **2026-02-26**。以 Flash 速度提供 Nano Banana Pro 级画质与世界知识；最多 5 个角色一致性，512px–4K 输出，支持图内文字渲染/翻译。
- [Kling Image 3.0 / 3.0 Omni](https://ir.kuaishou.com/news-releases/news-release-details/kling-ai-launches-30-model-ushering-era-where-everyone-can-be/) - 🇨🇳 🆕 **2026-02-05**。快手原生 2K/4K 图像生成，与 Video 3.0 一同随 Kling 3.0 套件发布。
- [Flux](https://github.com/black-forest-labs/flux) - 💤 **Stale**（2025-07 起无更新）。Black Forest Labs 开源模型。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fblack-forest-labs%2Fflux&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Seedance 2.0](https://seed.bytedance.com/) - 🇨🇳 🆕 字节下一代图像 / 动画生成 API。

### 视频生成

- [Meta Muse Video](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) - 🆕 **2026-07-07（预览）**。Meta Superintelligence Labs 的视频生成模型，与 Muse Image 同架构；Arena 文生视频榜第 3。随 Muse Image 发布一同预览，预计在 Meta 各应用中更广泛铺开。
- [Runway Agent](https://runwayml.com/news/introducing-runway-agent) - 🆕 **2026-05-13**。对话式 Agent，接过写好的脚本为你递交一段**多镜头完成品视频**：分镜脚本→生成→剪接→配音全流程贯通，并带时间线编辑器做最终调整。首个可用的「提示词到粗剪」产业级 Agent。
- [Veo 3.1](https://deepmind.google/technologies/veo/) - 🆕 **2025-10**。Google DeepMind 旗舰视频模型。**Veo 4** 截至 2026 年 7 月中旬仍未发布。
- [Runway Gen-4.5](https://runwayml.com/research/introducing-runway-gen-4.5) - 🆕 **2025-12**。Runway 旗舰视频模型，发布时位居 Artificial Analysis 文生视频榜第 1。平台还接入第三方模型，含 Kling 3.0 与 Sora 2 Pro（2026-02-20 加入）。
- [Kling VIDEO 3.0](https://app.klingai.com/) - 🇨🇳 🆕 **2026-02-04~07**。快手新一代；真人动作、嘴型同步、带音画同步的叙事化制作。
- [Sora 2 (via Runway)](https://runwayml.com/changelog) - OpenAI 的 Sora 应用于 2026-04-26 关停（API 保留至 2026-09-24），但 Sora 2 Pro 已自 **2026-02-20** 起集成进 Runway。
- [Seedance 2.5](https://seed.bytedance.com/) - 🇨🇳 🆕 🧪 **2026-06-23**。字节在火山引擎 2026 大会宣布的下一代视频模型：原生一次生成 30 秒（此前 4-15 秒），长叙事中角色/商品一致性增强。发布时可用性有限 —— 尚无公开定价或确认的 API。
- [Seedance 2.0](https://seed.bytedance.com/) - 🇨🇳 **2026-02**。字节多模态电影级视频生成，2K 分辨率（2026-06-23 升级支持 4K 输出），比 1.5 快约 30%。
- [Hailuo 2.3](https://www.minimax.io/news/minimax-hailuo-23) - 🇨🇳 **2025-10-28**。MiniMax 旗舰视频模型：SOTA 物理效果、角色微表情、强风格化（动漫/水墨/游戏 CG）；Hailuo 2.3 Fast 变体按 Hailuo 02 价格提供。
- [Pika 2.5](https://pika.art/) - 创意短视频，场景与特效控制。
- [LTX Studio](https://ltx.studio/) - 🆕 AI 电影化视频创作平台。
- [HappyHorse 1.1](https://technode.com/2026/06/23/alibaba-unveils-happyhorse-1-1-video-generation-model-launches-global-ai-filmmaking-competition/) - 🇨🇳 🆕 **2026-06-23**。阿里视频模型（2026-04-10 以 "HappyHorse-1.0" 之名揭晓，此前匿名登顶多个基准，后升至全球第 2）。1.1 升级运动动态、主体一致性、提示遵循与音频生成。可通过 HappyHorse 官网、阿里云百炼与 Qwen Cloud 使用。
- [Sora](https://openai.com/sora/) - 📦 **已停运**（应用 2026-04-26；API 2026-09-24）。OpenAI 文生视频应用关停；Sora 2 Pro 在 Runway 中延续。

### 音频与音乐

- [ElevenLabs Eleven v3 + ElevenAgents](https://elevenlabs.io/agents) - 🆕 2026 年定位为 "互联网的音频层"——支持 70+ 语言、带情绪 Audio Tag 的 TTS，加上首个通过 AIUC-1 认证的 ElevenAgents 语音 Agent 平台，含多模态消息、会话主题发现、工具调用前的语音控制。
- [Cartesia Sonic 3 / 3.5](https://cartesia.ai/blog/introducing-line-for-voice-agents) - 🆕 **2026**。基于状态空间模型的 TTS，首音延迟约 40-90ms（Sonic 3.5 于 2026 年 5 月 GA）；驱动 **Line** 语音 Agent 平台（自 2026 年 5 月起 Line Agent 默认运行在 Sonic 3.5 TTS + Ink-2 STT 上）。
- [Deepgram Nova-3 + Aura-2 + Flux Multilingual](https://deepgram.com/learn/best-voice-ai-agents-2026-buyers-guide) - 🆕 **2026 年 4 月**。45+ 语言的 STT，TTS 延迟低于 200ms，会话式 STT 支持通话中 10 种语言的实时切换。
- [MiniMax Music 2.6](https://aimlapi.com/blog/the-ultimate-guide-to-minimax-models-2026-m2-7-music-2-6-hailuo-video-advanced-tts) - 🇨🇳 🆕 **2026 年 4 月 10 日**（全球 beta）。主打翻唱生成方向，低频还原显著改进。
- [Voxtral TTS](https://www.forbes.com/sites/ronschmelzer/2026/03/26/mistral-releases-open-weight-voice-ai-built-for-speed/) - 🆕 **2026 年 3 月 26 日**。Mistral 开放权重的 4B TTS，专为语音 Agent 的低延迟而生。
- [ElevenLabs](https://elevenlabs.io/) - AI 语音合成 + 克隆 + 对话 AI 头部。
- [Suno v5.5](https://suno.com/blog/v5-5) - 🆕 **2026 年 3 月 26 日**。高保真人声的 AI 音乐生成；v5.5 新增 Voices（用你本人经验证的声音演唱）、基于上传内容训练的 Custom Models 以及 My Taste 个性化。V6 有传闻但未官宣。
- [Udio](https://www.udio.com/) - 🆕 商用级音乐生成。
- [OpenAI Audio Models](https://openai.com/) - GPT-4o 与 GPT-Realtime-2（**2026-05-07**，随 GPT-Realtime-Translate、GPT-Realtime-Whisper 一同发布）内的原生音频理解 + 生成；gpt-realtime-2.1 与 2.1-mini 于 **2026-07-06** 发布，字母数字识别、噪声处理与打断行为均改进。
- [Stability Audio](https://stability.ai/) - 开源音频音乐生成。
- [Bark](https://github.com/suno-ai/bark) - 💤 **Stale**（2024-08 起无更新）。开源文本到音频。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsuno-ai%2Fbark&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hume TADA](https://github.com/HumeAI/tada) - 🆕 **2026 年 3 月**。Hume AI 首个开源 TTS —— Text Audio Dual Alignment (TADA)：文本与音频在同一条 1:1 同步 token 流中生成；零内容幻觉，RTF 约 0.09，TADA-1B/3B-ML 模型（9+ 种语言），能在手机上跑。MIT 代码，Llama 3.2 许可权重。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHumeAI%2Ftada&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

## 🔗 Agent 协议与标准

*让 Agent 跨工具、跨框架互联互通的开放标准。*

### Model Context Protocol (MCP)

- [MCP Specification](https://modelcontextprotocol.io/) - 🆕 "AI 的 USB-C" —— Anthropic 主推、用于让 LLM 接入工具与数据源的开放协议。2025-12 捐赠给 Linux Foundation 旗下 Agentic AI Foundation。
- [MCP 2026-07-28](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) - 🆕 **正式规范 2026-07-28（RC 于 2026-05-21 发布）**。MCP 下一个大版本：**无状态协议核心**（可部署在普通轮询负载均衡器后，无需会话亲和）、**扩展框架**（反向 DNS ID、独立版本化）、**MCP Apps**（沙箱化 iframe 中的服务端渲染 UI）、Tasks 从实验性核心移入扩展，以及**授权强化**（六项 SEP 收紧 OAuth 2.0 / OpenID Connect 对齐）。此外：完整 JSON Schema 2020-12、W3C Trace Context、正式的 12 个月弃用政策；Roots、Sampling、Logging 被弃用。[SDK beta（Python、TypeScript、Go、C#）已于 2026-06-29 发布](https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/)。
- [MCP Servers](https://github.com/modelcontextprotocol/servers) - 官方参考 MCP 服务实现。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Fservers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - 官方 TypeScript SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Ftypescript-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - 官方 Python SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Fpython-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [mcp.so](https://mcp.so/) - 🆕 社区 MCP 服务目录。
- [CorpusIQ](https://mcp2.corpusiq.io/mcp) - 🆕 ⚠️ **未经验证。** 以 `io.corpusiq/multi-source-mcp` 收录于 MCP Registry —— 多源商业数据连接器，25+ 集成（GA4、Google Ads、TikTok、YouTube、Shopify、Stripe、Airtable、Slack、HubSpot、Calendly、Klaviyo 等）。智能查询路由、跨源归因、统一商业智能。HTTP 传输 + Ed25519 签名认证。
- [Agentage Memory](https://memory.agentage.io/mcp) - 🆕 ⚠️ **未经验证。** 以 `io.agentage/memory` 收录于 MCP Registry —— 一个所有 AI（Claude / Cursor / ChatGPT）共享读写的文件型记忆，本地镜像为纯 Markdown 可随时导出。远程 Streamable HTTP，OAuth 2.1 + PKCE + 动态客户端注册。六个工具：`memory__search/read/write/edit/list/delete`。[文档](https://agentage.io/blog/mcp-endpoint-is-live)。
- [mcp-gateway](https://github.com/Zijian-Ni/mcp-gateway) - ⚠️ **未经验证**（早期项目）。MCP 网关，统一路由 / 认证 / 限流。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fmcp-gateway&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Agent-to-Agent Protocol (A2A)

- [A2A Protocol](https://github.com/a2aproject/A2A) - Agent 间通信开放标准，起源于 Google，现为 Linux Foundation 项目，已有 150+ 合作组织。**v1.0 于 2026 年 5 月发布**。让不同框架的 Agent 互相发现、委派、协作；提供 Python、Go、JS、Java、.NET、Rust SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fa2aproject%2FA2A&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [A2A Course (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/a2a-the-agent2agent-protocol/) - 🆕 免费课程：用 A2A 构建多 Agent 系统。

### 其他标准

- [Agentic AI Foundation](https://aaif.io/) - 🆕 Linux Foundation 旗下的开放 Agent 标准治理机构 —— 托管 MCP、goose、AGENTS.md 与 agentgateway。创始白金成员：AWS、Anthropic、Block、Bloomberg、Cloudflare、Google、Microsoft、OpenAI。
- [AGENTS.md](https://agents.md/) - 🆕 开放的 Markdown 约定 —— "给 Agent 看的 README"——为 AI 编程 Agent 提供项目上下文与指令的固定位置。已被 6 万+ 开源项目采用；由 Agentic AI Foundation（Linux Foundation）管理。
- [Coinbase Base MCP](https://fortune.com/2026/05/26/coinbase-pushes-further-into-ai-payments-with-new-mcp-for-base-network/) - 🆕 **2026 年 5 月 26 日**。Coinbase 为 Base 公链发布 MCP 服务器，让 Claude / Cursor / ChatGPT Agent 直接执行加密资产交易与借贷。首个交易所级、面向链上自动化的 MCP 端点。
- [Robinhood Agentic Trading MCP](https://robinhood.com/us/en/newsroom/robinhood-is-now-open-to-agents/) - 🆕 **2026 年 5 月 27 日**（beta）。首家通过 MCP 把股票交易开放给 AI Agent 的美国券商：Agent（Claude / Codex / Cursor）对账户只读，仅可在专门隔离的 Agentic 账户内交易；每笔交易推送，一键断开。
- [The Declaration of Intelligence](https://thedeclaration.ai) - ⚠️ 面向 AI Agent 与人类的原则宣言草案（v0.2），通过 GitHub Pull Request 公开签署。早期阶段 —— 最近核查时仅有少量签名方。
- [Kuberna Labs](https://github.com/kawacukennedy/kuberna-labs) - ⚠️ **未验证。** 面向 AI Agent 的跨链意图执行协议，声称支持 ERC-8004 链上身份、zkTLS/TEE 证明与类型化意图模式，可在 NEAR、Base、Mantle 上自主执行交易并附可验证执行证明。新仓库，独立采用情况未经验证——仅供参考，使用前请自行评估。

---

## 🏗️ Agent 框架

*用来构建自主 AI Agent 的框架与库。*

- [Vercel Eve](https://github.com/vercel/eve) - 🆕 **2026-06-17（Vercel Ship 2026）**。Vercel 开源的「文件系统优先」TypeScript Agent 框架——一个 Agent 就是一个文件目录（指令、工具、技能），由 Vercel 编译为内置沙箱执行、审批、评测与 OpenTelemetry 的持久化服务。兼容任意模型、任意 MCP 服务器以及 Slack / Discord / GitHub 等渠道，被称为「Agent 界的 Next.js」。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvercel%2Feve&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Databricks Omnigent](https://github.com/omnigent-ai/omnigent) - 🆕 **2026-06**。Databricks 开源的元 Harness：位于你已有的编码 Agent（Claude Code、Codex、Pi、自定义）之上，把它们整合为同一系统中可互操作的部件——统一编排、共享安全策略、实时协作。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fomnigent-ai%2Fomnigent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Nokia NSP Agentic AI](https://www.globenewswire.com/news-release/2026/06/11/3310210/0/en/nokia-introduces-agentic-ai-framework-in-network-services-platform-to-enable-trust-based-ai-operations-for-ip-networks.html) - 🆕 **2026-06**。面向电信 Network Services Platform (NSP) 的企业级 Agent 框架，部署 Agent 在复杂 IP 网络上推理并执行路由 / 维护操作。
- [Alteryx Agent Studio](https://www.alteryx.com/blog/new-capabilities-in-alteryx-one-built-for-how-analysts-work) - 🆕 **2026-05**。把可信的 Alteryx 数据集与工作流打包为对话式 Agent；通过新的 Alteryx One MCP Server 创建并管理 MCP 端点（可在 Claude、ChatGPT、Gemini 中作答）。
- [Koog 1.0](https://github.com/JetBrains/koog) - 🆕 **2026-05-21 · KotlinConf 2026**。JetBrains 针对 **Kotlin + Java** 的开源 Agent 框架进入稳定 1.0，带来长期支持的稳定 API 面。Kotlin Multiplatform 跨端部署（JVM / Android / iOS / JS / WASM）、Java 互操作无需包装模块、Android 本地 LiteRT、OpenTelemetry 跨端可观测、图状工作流、Spring Boot / Ktor 集成，提供商 OpenAI / Anthropic / Google / Bedrock 均原生支持。Apache-2.0。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FJetBrains%2Fkoog&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangChain](https://github.com/langchain-ai/langchain) - 上下文感知推理应用的基础框架。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangGraph](https://github.com/langchain-ai/langgraph) - 把 Agent 建模为有状态、多 actor 协作的图。0.3.x 系列（2025）把预制 Agent 拆出 `langgraph-prebuilt`（Supervisor / Swarm / LangMem / Trustcall）。**v1.2（2026-05）** 新增节点级超时 / 错误恢复 / 优雅关停、降低长线程 checkpoint 开销的 `DeltaChannel`，以及以 content block 为中心的流式 API v3。最新：v1.2.4（2026-06）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flanggraph&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [CrewAI](https://github.com/crewAIInc/crewAI) - 角色扮演式 Agent 团队编排。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FcrewAIInc%2FcrewAI&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [goose](https://github.com/block/goose) - Block 出品的开源可扩展 AI Agent（Rust 桌面应用 + CLI），可用任意 LLM 安装、执行、编辑与测试；支持 15+ 提供商；由 Agentic AI Foundation（Linux Foundation）托管。v1.43.0（2026-07-14）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fblock%2Fgoose&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AG2](https://github.com/ag2ai/ag2) - 🆕 **2026-07-03（v1.0.0b0）**。Microsoft AutoGen 的社区驱动 Fork —— 在微软于 2026 Q1 将 AutoGen 转入维护模式后，这个 Fork 为希望继续使用可对话式 Agent 架构的开发者提供持续开发。Apache-2.0，可从现有 AutoGen 项目无缝迁移。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fag2ai%2Fag2&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/) - 🆕 AutoGen + Semantic Kernel 合并的统一框架。多 Agent + 企业能力。
- [Microsoft Agent 365](https://techcommunity.microsoft.com/blog/agent-365-blog/what%E2%80%99s-new-in-agent-365-may-2026/4516340) - 🆕 **2026 年 5 月 GA**。面向 AI Agent 的企业级可观测、治理与安全平台；2026 年 5 月更新加入面向 Agent 的 SASE、威胁检测/阻断与 Agent 威胁狩猎工作流。KPMG 宣布覆盖 276,000 名专业人员的全球部署（2026-06-09）。
- [Microsoft Scout](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) - 🆕 **2026-06-02（Build 2026）**。微软面向 Microsoft 365 的常驻个人工作 Agent，构建在开源 OpenClaw 运行时之上。
- [AutoGen](https://github.com/microsoft/autogen) - 💤 **维护模式**（最后版本 2025-09；由 Microsoft Agent Framework 接替，后续交由社区管理）。微软多 Agent 对话框架。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fautogen&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Google Agent Development Kit (ADK)](https://github.com/google/adk-python) - 🆕 与 Gemini + Vertex AI 深度集成的模块化框架。层级 Agent 组合。**v2.0 处于 beta**（v2.0.0b1，2026-04），带来工作流编排与重构的 Agent 执行模型；最新稳定版 v1.33（2026-05）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle%2Fadk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - 🆕 [2026-04-15 升级](https://openai.com/index/the-next-evolution-of-the-agents-sdk/) —— 原生沙箱、MCP、子 Agent handoff、Codex 文件操作。生产级多 Agent。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fopenai-agents-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MetaGPT](https://github.com/geekan/MetaGPT) - 🇨🇳 给 LLM 分配 SOP 软件团队角色（PM / 架构师 / 工程师）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgeekan%2FMetaGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Mastra](https://github.com/mastra-ai/mastra) - 🆕 TypeScript 优先的 Agent 框架，工作流驱动 + 内置可观测性。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmastra-ai%2Fmastra&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentGPT](https://github.com/reworkd/AgentGPT) - 📦 **Archived**（2026-01）。浏览器中部署 Agent。第一波代表项目，仅作历史参考。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Freworkd%2FAgentGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [BabyAGI](https://github.com/yoheinakajima/babyagi) - 实验性的自构建自主 Agent 框架；2023 年原版任务管理型 BabyAGI 现存于 [babyagi_archive](https://github.com/yoheinakajima/babyagi_archive)。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fyoheinakajima%2Fbabyagi&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) - 💤 **Stale**（2025-01 起无更新）。开源自主 Agent 框架。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTransformerOptimus%2FSuperAGI&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) - 把 LLM 嵌入应用。C# / Python / Java。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fsemantic-kernel&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agno（前 Phidata）](https://github.com/agno-agi/agno) - 多模态 Agent + 记忆 + 知识 + 工具 + 推理；v2.7.x（2026-07）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagno-agi%2Fagno&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [DSPy](https://github.com/stanfordnlp/dspy) - "编程而不是写 prompt" 的语言模型框架。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstanfordnlp%2Fdspy&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenClaw](https://github.com/openclaw/openclaw) - 🆕 个人 AI Agent 平台：技能、记忆、多渠道消息、Dreaming（三阶段记忆巩固）、Canvas / A2UI、ACP 编程 harness 集成、Standing Orders。最新：**v2026.7.1**（2026-07-13）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenclaw%2Fopenclaw&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Dify](https://github.com/langgenius/dify) - 🇨🇳 开源 LLM 应用开发平台 + 可视化 Agent 构建。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flanggenius%2Fdify&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Haystack Agents](https://github.com/deepset-ai/haystack) - 端到端 LLM 框架，Agent 流水线。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeepset-ai%2Fhaystack&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vellum AI](https://www.vellum.ai/) - 🆕 闭源 SaaS 生产级 Agent 框架：Prompt 构建 / 评测 / 版本 / 可观测性一体。
- [FastAgency](https://github.com/airtai/fastagency) - 💤 把 AG2（AutoGen）多 Agent 工作流通过 console、Mesop Web UI、REST/FastAPI 与 NATS 适配器部署到生产；最后版本 2025-12。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fairtai%2Ffastagency&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Rasa](https://github.com/RasaHQ/rasa) - 💤 **维护模式**（最后版本 2025-01；后继为 Rasa CALM）。强意图识别 + 对话管理的开源对话 AI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FRasaHQ%2Frasa&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Lindy](https://www.lindy.ai/) - 🆕 商务用户向无代码 Agent，可视化工作流。
- [Octomind](https://github.com/muvon/octomind) - 🆕 Rust 开源 AI Agent 运行时。多模型（13+），社区贡献的领域 Agent（开发 / 医疗 / 法律 / DevOps），支持 MCP 运行时自扩展。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmuvon%2Foctomind&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsoft AI Agent Governance Toolkit](https://www.helpnetsecurity.com/2026/04/03/microsoft-ai-agent-governance-toolkit/) - 🆕 **2026-04-03**。开源治理工具包，把运行时安全策略以策略即代码方式应用到 LangChain / AutoGen 等框架。
- [Bernstein](https://github.com/sipyourdrink-ltd/bernstein) - 🆕 Python 编排器，统一管理 40+ 个 CLI 编程 Agent（Claude Code、Codex、Gemini CLI、Cursor、Aider 等）。一次 LLM 计划调用后，调度、git worktree 隔离、质量闸门、HMAC 链式审计都是确定性的。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsipyourdrink-ltd%2Fbernstein&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Genkit Middleware](https://developers.googleblog.com/announcing-genkit-middleware-intercept-extend-and-harden-your-agentic-apps/) - 🆕 **2026-05-14**。Google 为开源 Genkit 框架增加中间件体系 —— 在 generate / model / tool 三层给出可组合 hooks：重试、模型降级、工具人工审批、SKILL.md 技能注入、限定范围的文件访问。先支持 TS / Go / Dart，Python 跟进中。
- [LlamaIndex ↔ Google Agents API 集成](https://www.kucoin.com/news/flash/google-launches-agents-api-llama-index-integrates-llamaparse-for-unstructured-document-processing) - 🆕 **2026-05-20**。LlamaIndex 为 Google 刚发布的 Agents API 交付模板，在沙箱化 Linux 环境里暴露 **LlamaParse** / **LiteParse** 处理非结构化文档。
- [NarraNexus](https://github.com/NetMindAI-Open/NarraNexus) - NetMind.AI 出品的开箱即用 AI Agent 团队工作区——具备记忆的 Agent 从第一天起就能记住上下文、协作并使用工具。多 Agent（PM/开发/部署/研究）、持久上下文、MCP 式集成、可组合模块。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNetMindAI-Open%2FNarraNexus&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Ontheia](https://github.com/Ontheia/ontheia) - ⚠️ **未经验证**（早期项目，采用度低）。自托管开源 AI Agent 平台。多模型供应商（Claude / OpenAI / Gemini / Ollama），原生支持 MCP，Chain Engine 可视化工作流编排，长期记忆（pgvector），多用户 RBAC，架构层面合规 GDPR。AGPL-3.0。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOntheia%2Fontheia&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Coze Studio](https://github.com/coze-dev/coze-studio) - 🆕 🇨🇳 字节跳动开源的 AI Agent 开发平台——一体化可视化工具，简化 Agent 的创建、调试、部署。Apache-2.0，20K+ stars；Coze.com 的开源对照版。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Strands Agents (AWS)](https://github.com/strands-agents/sdk-python) - 🆕 **2026 年4–6月**。AWS 开源模型驱动 Agent SDK（Python + TypeScript 1.0 GA 2026-04-30）。支持 Bedrock / Anthropic / OpenAI / Ollama，多种多智能体编排模式（图/群/工作流），内置可观测性 hooks，A2A 协议支持；TypeScript SDK 现由 [harness-sdk monorepo](https://github.com/strands-agents/harness-sdk) 维护。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstrands-agents%2Fsdk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [CrewAI 1.14](https://github.com/crewAIInc/crewAI) - 🆕 **2026年6月**。大更新：内存 / 知识 / RAG 可插拔后端，声明式 Flows + CLI/TUI 支持，Chat API 会话式流，原生 Snowflake Cortex LLM，移除 LangChain 依赖使核心更轻。最新稳定版：1.14.6（2026-05-28）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FcrewAIInc%2FcrewAI&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Oracle AI Agent Studio (Fusion)](https://www.oracle.com/news/announcement/oracle-introduces-ai-native-builder-experience-2026-07-14/) - 🆕 **2026-07-14**。Oracle Fusion Cloud 应用内置的 AI 原生构建器，打造“Fusion Agentic Applications”——在 Fusion 业务对象、工作流和安全上下文中脚本与执行的多 Agent 团队。无代码/低代码/专业代码全支持；Fusion 客户免费使用。

---

## 🛠️ Agent IDE 与可视化构建器

*用来设计、调试、上线 Agent 工作流的可视化（或低代码）环境。*

- [LangGraph Studio](https://docs.langchain.com/langsmith/studio) - LangGraph 的可视化调试器（现为 LangSmith 的一部分）：步进状态、回放回合、中途改写消息。
- [Dify](https://github.com/langgenius/dify) - 🇨🇳 拖拽式 Agent 工作流构建。生产级使用最广。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flanggenius%2Fdify&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agenta](https://github.com/agenta-ai/agenta) - 🆕 一体化 LLMOps：prompt playground + 管理 + 评测 + 可观测性。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagenta-ai%2Fagenta&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vellum AI](https://www.vellum.ai/) - 闭源 SaaS。
- [Coze Loop](https://github.com/coze-dev/coze-loop) - 🇨🇳 🆕 字节 Coze 团队开源的 Agent 优化平台：全生命周期开发、调试、评测与监控。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-loop&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Restack](https://www.restack.io/) - 持久化 Agent 运行时 + 可视化编辑（Temporal 风格 replay）。开源示例：[restackio/examples-python](https://github.com/restackio/examples-python)。
- [Bisheng](https://github.com/dataelement/bisheng) - 🇨🇳 企业级开源 LLM DevOps：工作流 / RAG / Agent / 微调 / 数据集 / 评测 / 可观测性。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdataelement%2Fbisheng&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [n8n](https://github.com/n8n-io/n8n) - 通用工作流自动化，2026 年常被当作 Agent 画布用。400+ 集成 + 原生 AI 节点。Fair-code。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fn8n-io%2Fn8n&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Mastra](https://github.com/mastra-ai/mastra) - 🆕 强约束风格的 TypeScript Agent 框架，自带 RAG、可观测性、MCP 与可视化工作流构建器；21K+ stars。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmastra-ai%2Fmastra&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [VoltAgent](https://github.com/VoltAgent/voltagent) - 🆕 端到端 TypeScript AI Agent 工程平台，覆盖记忆、RAG、guardrail、MCP、语音与工作流。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FVoltAgent%2Fvoltagent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Coze Studio](https://github.com/coze-dev/coze-studio) - 🆕 🇨🇳 字节 Coze 团队的开源 Agent IDE / 可视化构建器。拖拽式工作流、插件市场、调试面板、多 LLM 供应商支持。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🧠 Agent 记忆

*让 Agent 拥有持久记忆与上下文管理的系统。*

- [Letta (MemGPT)](https://github.com/letta-ai/letta) - 长期记忆 + 自定义工具的 LLM 服务。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fletta-ai%2Fletta&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MemoryLake](https://memorylake.ai) - 🆕 **2026 年 7 月**。"Agent 的记忆护照"——跨不同 Agent 与工具共享的平台中立记忆层。按用户/Agent/会话作用域存储记忆，并通过统一 API 提供，让一个平台上的 Agent 能调取另一个平台的上下文。
- [Supermemory](https://github.com/supermemoryai/supermemory) - 🆕 基于多种数据源（网页、文档、聊天）构建的上下文图谱，为 Agent 对话提供背景。API 优先，集成 MCP 与主流框架。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsupermemoryai%2Fsupermemory&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Graphlit](https://www.graphlit.com/) - 🆕 面向生产级 Agent 的上下文平台：数据摄取、实体抽取与知识图谱，支撑搜索 + RAG。提供 MCP 服务器，可接入 Claude / Cursor / Copilot。
- [Mem0](https://github.com/mem0ai/mem0) - LLM 应用的自我提升记忆层。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmem0ai%2Fmem0&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Remio](https://remio.ai/) - 🆕 本地优先的 AI 记忆与知识库桌面应用（Windows/Mac），面向个人上下文。可解析文件、网页、录音、邮件、消息与图片为本地索引与向量，让 Agent 检索精准上下文，而不必反复 grep 目录或把整篇文档塞进 prompt。本地优先 + BYOK。
- [Zep](https://github.com/getzep/zep) - AI 助理与 Agent 的长期记忆。注意：开源 Community Edition 已弃用 —— 仓库现托管 Zep Cloud 的 SDK/示例；Zep 活跃的开源项目见 [Graphiti](https://github.com/getzep/graphiti)。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgetzep%2Fzep&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [agent-memory](https://github.com/Zijian-Ni/agent-memory) - ⚠️ **未经验证**（早期项目）。跨会话上下文持久化的轻量 Agent 记忆框架。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fagent-memory&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangMem](https://github.com/langchain-ai/langmem) - LangChain 面向 Agent 的长期记忆 SDK —— 语义/情景/程序性记忆原语，可接入 LangGraph 的持久化层。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangmem&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Motorhead](https://github.com/getmetal/motorhead) - 💤 **不再维护**（维护者已标记弃用；最后版本 2023-12）。LLM 的记忆 + 上下文管理服务。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgetmetal%2Fmotorhead&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ChromaDB](https://github.com/chroma-core/chroma) - AI 原生开源向量数据库。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fchroma-core%2Fchroma&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cognee](https://github.com/topoteretes/cognee) - 用图 + LLM + 向量检索得到确定性输出。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftopoteretes%2Fcognee&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangGraph Memory](https://github.com/langchain-ai/langgraph) - 🆕 LangGraph 内置的持久化与 checkpoint。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flanggraph&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Graphiti](https://github.com/getzep/graphiti) - 🆕 时序感知的知识图记忆。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgetzep%2Fgraphiti&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude Managed Agents Memory](https://platform.claude.com/docs/en/release-notes/overview) - 🆕 **2026-04-23** 公测。把读写记忆挂载到 Agent 文件系统，实现跨会话学习。
- [OpenViking](https://github.com/volcengine/OpenViking) - 🆕 🇨🇳 字节火山引擎开源的 Agent 上下文数据库（适配 OpenClaw 等）。用文件系统范式统一管理记忆、资源与技能，实现分层上下文交付与自演化。AGPL-3.0，22K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvolcengine%2FOpenViking&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ReMe](https://github.com/agentscope-ai/ReMe) - 🆕 🇨🇳 阿里 AgentScope 出品的 Agent 记忆管理工具包——文件系记忆 + 向量记忆双轨，专门处理上下文窗口受限与无状态会话两大痛点。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentscope-ai%2FReMe&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [taOSmd](https://github.com/jaylfc/taosmd) - 🆕 ⚠️ **Unverified.** 本地优先、基于追加式转录的 Agent 记忆：类型化时序知识图（修正后的新事实自动覆盖旧事实）+ 向量与 BM25 混合检索。面向小型本地模型调优，完全离线（8 GB 单板机即可运行）。作者声称 LongMemEval-S 端到端 Judge 97%；单作者维护，审核时 44 stars，基准可按 `docs/benchmarks.md` 复现。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fjaylfc%2Ftaosmd&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hindsight](https://github.com/vectorize-io/hindsight) - 🆕 从经验中学习的 Agent 记忆 —— 不只是会话历史。仿生数据结构组织世界事实、Agent 经验与习得的心智模型；提供 `retain`/`recall`/`reflect` 原语；随附 Agent Memory Benchmark (AMB)。MIT，15K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvectorize-io%2Fhindsight&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SimpleMem](https://github.com/aiming-lab/SimpleMem) - 🆕 高效的 LLM Agent 终身记忆——多模态（文本+图像+音频+视频），无需微调即可突破 token 上限约束。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Faiming-lab%2FSimpleMem&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agent Memory Techniques](https://github.com/NirDiamant/Agent_Memory_Techniques) - 🆕 30 个可运行的 Jupyter 笔记本，覆盖对话缓冲、向量存储、知识图谱、情景/语义记忆、MemGPT、Mem0、Letta、Zep、Graphiti 与 LoCoMo 基准——学习各类记忆模式的实用参考。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNirDiamant%2FAgent_Memory_Techniques&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🔌 工具与 API 集成

*让 Agent 接入外部服务与 API 的协议与工具。*

- [ZoomMate](https://news.zoom.com/zoom-launches-zoommate/) - 🆕 💰 **2026-06-01 GA**。Zoom 第一方 AI 队友，把会议对话变成完成的工作 —— 更新 Salesforce 记录、创建 Jira issue、通过 Slack 路由请求。$20/用户/月。
- [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol/servers) - 工具调用的事实标准。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Fservers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [mcp-gateway](https://github.com/Zijian-Ni/mcp-gateway) - ⚠️ **未经验证**（早期项目）。MCP 网关。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fmcp-gateway&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Composio](https://github.com/ComposioHQ/composio) - 1000+ toolkit + 托管认证一体化 Agent 集成平台。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FComposioHQ%2Fcomposio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Toolhouse](https://toolhouse.ai/) - AI 工具云：存储、管理、执行工具。
- [LangChain Tools](https://github.com/langchain-ai/langchain) - LangChain 生态广泛的工具集成。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Arcade AI](https://github.com/ArcadeAI/arcade-ai) - AI Agent 工具调用平台。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FArcadeAI%2Farcade-ai&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Browser Use](https://github.com/browser-use/browser-use) - 让 AI Agent 操控浏览器。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowser-use%2Fbrowser-use&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Firecrawl](https://github.com/firecrawl/firecrawl) - 把网站变成 LLM-ready 数据。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ffirecrawl%2Ffirecrawl&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Crawl4AI](https://github.com/unclecode/crawl4ai) - 🆕 LLM 友好的开源爬虫。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Funclecode%2Fcrawl4ai&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Stagehand](https://github.com/browserbase/stagehand) - 🆕 Browserbase 出品的 AI 浏览器自动化。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowserbase%2Fstagehand&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentQL](https://www.agentql.com/) - 🆕 用语义化查询语言操控网页。
- [StackOne](https://www.stackone.com/) - 🆕 HR / CRM / ATS 统一 API。
- [The Colony](https://thecolony.cc) - ⚠️ **Unverified**。自称 Agent 间社交网络 + REST API + Python / TS / Go SDK + MCP server。组织与 SDK 仓库均 <30 天，0~2 star，单维护者；同款 PR 投了 15+ 个 awesome 列表。**仅作可见性收录**，使用前请自行评估。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTheColonyCC%2Fcolony-sdk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [dependency-freshness-mcp](https://github.com/Armigerous/dependency-freshness-mcp) - 🆕 ⚠️ **Unverified**。为 AI 编码 Agent 提供带引用的 npm 与 PyPI 依赖新鲜度信息：最新版本、发布日期、弃用状态、带日期的破坏性变更摘要 —— 弥补训练截止带来的盲区。远程（Apify Standby HTTP）+ 本地 stdio。新建单维护者仓库（建于 2026-06-08，收录时 0 star）—— 仅作可见性收录，使用前请自行评估。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FArmigerous%2Fdependency-freshness-mcp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [NotFair](https://github.com/nowork-studio/NotFair) - 开源 Claude Code Agent 技能集，涵盖 [SEO](https://github.com/nowork-studio/NotFair/tree/main/seo)、[Google Ads](https://github.com/nowork-studio/NotFair/tree/main/google-ads) 与 [Meta Ads](https://github.com/nowork-studio/NotFair/tree/main/meta-ads)；通过 Google Ads MCP、Meta Ads MCP、Google Search Console MCP 和 GA4 MCP 接入实时广告与分析数据。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fnowork-studio%2FNotFair&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [mcp-agent](https://github.com/lastmile-ai/mcp-agent) - 🆕 以 MCP 为核心通信原语设计的开源 Python 框架，构建与 MCP 工具生态原生互操作的 Agent。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flastmile-ai%2Fmcp-agent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AWS MCP Server](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/) - 🆕 **2026 年 5 月 6 日 GA**。AWS 官方托管的 MCP 服务器，让编码 Agent 安全可审计地调用任意 AWS API；多步操作可在沙箱化 Python 环境中执行，用 agent skills 取代传统 "agent SOP"。AWS 第一方出品。
- [Google Workspace MCP Server](https://workspaceupdates.googleblog.com/2026/05/agent-tools-and-security-updates-for-workspace-developers.html) - 🆕 **2026 年 5 月 1 日开发者公开预览**。Workspace 原生 MCP 服务器，将 Gmail / Drive / Calendar / Chat / People 暴露给 MCP 客户端，OAuth 范围由管理员控制并带审计日志。
- [iManage MCP Server](https://imanage.com/resources/resource-center/news/mcp-server-available-broader-ai-ecosystem/) - 🆕 **2026 年 5 月 14 日**。iManage 知识工作平台的原生 MCP 入口，任何 AI 客户端无需定制即可安全读写 iManage 文档。首家面向公众的法律/专业服务 SaaS MCP server。
- [Power Platform Canvas Authoring MCP Server](https://www.microsoft.com/en-us/power-platform/blog/2026/05/14/whats-new-in-power-platform-may-2026-feature-update/) - 🆕 **2026 年 5 月 14 日**。Microsoft Power Platform 将 Canvas Apps 的 authoring 能力暴露为 MCP 服务器，Copilot / Claude Code 可通过自然语言驱动 InfoPath → Canvas Apps 迁移。
- [Coinbase AgentKit](https://github.com/coinbase/agentkit) - 🆕 "每个 AI Agent 都该有自己的钱包"。Coinbase 官方 SDK 给 Agent 配一个 EVM 钱包，可支付 API、签署交易、在 Base / Ethereum 上链交易。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoinbase%2Fagentkit&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Bifrost (Maxim AI)](https://github.com/maximhq/bifrost) - 🆕 开源企业级 AI 网关（Apache-2.0）——支持 1000+ 模型，自适应负载均衡、集群模式、guardrail、OAuth 2.0 + PKCE、网关层提示注入防御；5k RPS 下额外开销 <100µs。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmaximhq%2Fbifrost&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Anthropic 创意工具连接器](https://www.anthropic.com/news/claude-for-creative-work) - 🆕 **2026 年 4 月 28 日**。9 个基于 MCP 的 Claude 连接器，对接 Adobe（Creative Cloud 50+ 工具，含 Photoshop / Premiere / Express）、Blender、Autodesk Fusion、Ableton、Splice、Canva Affinity、SketchUp、Resolume。建立在 MCP 开放标准上，其他 LLM 客户端也能直接使用。

---

## 🧪 Agent 沙箱与计算隔离

*让 Agent 安全执行生成代码 / shell 命令的隔离运行时。一旦让 Agent 自由活动，这是必备基础设施。*

- [E2B](https://github.com/e2b-dev/E2B) - AI 生成代码的开源云沙箱。OpenAI Agents SDK 默认执行层。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fe2b-dev%2FE2B&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Daytona](https://github.com/daytonaio/daytona) - 🆕 弹性、安全的 AI 生成代码运行基础设施。每个 Agent 任务一个隔离的开发环境。AGPL-3.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdaytonaio%2Fdaytona&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Modal](https://modal.com/) - 流行的 Agent 计算 + GPU 任务 + Python 沙箱 Serverless 平台。`modal-client` 是官方 SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodal-labs%2Fmodal-client&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsandbox](https://github.com/superradcompany/microsandbox) - 🆕 本地、可编程的 microVM 沙箱。隐私优先，本机执行，不依赖云。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsuperradcompany%2Fmicrosandbox&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SandboxFusion](https://github.com/bytedance/SandboxFusion) - 🇨🇳 字节多语言代码执行沙箱，面向 Agent / 模型评测流水线。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbytedance%2FSandboxFusion&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Northflank](https://northflank.com/) - 通用容器 PaaS，常被用作 Agent 运行时（每任务临时环境 + GPU 池）。
- [Firecracker](https://github.com/firecracker-microvm/firecracker) - E2B / Daytona / 多数 Agent 沙箱底层的 microVM 内核。自建沙箱时是基础原语。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ffirecracker-microvm%2Ffirecracker&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Google Antigravity Sandbox](https://antigravity.google/changelog) - 🆕 **2026-05（Google I/O）**。Agent 执行代码的沙箱化 Linux 环境；作为 Antigravity 2.0 技术栈的一部分交付 —— 子 Agent 在各自隔离的容器中运行，文件系统与网络访问受限。

---

## 🛡️ Agent 安全

*抵御 prompt 注入、数据泄漏、滥用的工具与框架。*

- [AgentGate](https://github.com/ElamOlame31/agentgate-public) - 🆕 ⚠️ **未经验证**（早期项目，单一维护者）。自主 AI Agent 的预执行授权决策点（PDP）。每次请求按 4 个维度打信任分，检测 24 小时杀链模式，Merkle 链式审计日志。MIT 许可，可直接接入 LangGraph、LangChain、AutoGen。[tryagentgate.com](https://www.tryagentgate.com/) ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FElamOlame31%2Fagentgate-public&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [prompt-firewall](https://github.com/Zijian-Ni/prompt-firewall) - ⚠️ **未经验证**（早期项目）。LLM prompt 防火墙：检测 + 拦截注入。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fprompt-firewall&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LLM Guard](https://github.com/protectai/llm-guard) - LLM 输入输出扫描安全工具包。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fprotectai%2Fllm-guard&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Rebuff](https://github.com/protectai/rebuff) - 📦 **Archived**（2025-05）。自我加固 prompt 注入检测器。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fprotectai%2Frebuff&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Guardrails AI](https://github.com/guardrails-ai/guardrails) - LLM 输出验证与纠正。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fguardrails-ai%2Fguardrails&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) - 给 LLM 对话系统加可编程护栏的工具包。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNVIDIA%2FNeMo-Guardrails&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vigil](https://github.com/deadbits/vigil-llm) - 💤 **Stale**（2024-01 起无更新）。LLM 安全扫描器。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeadbits%2Fvigil-llm&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Lakera Guard](https://www.lakera.ai/) - 企业级 AI 安全平台。
- [Garak](https://github.com/NVIDIA/garak) - NVIDIA 出品的 LLM 漏洞扫描器。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNVIDIA%2Fgarak&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Invariant Guardrails](https://github.com/invariantlabs-ai/invariant) - 🆕 Agent 运行时策略执行 + 安全检查。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Finvariantlabs-ai%2Finvariant&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Prompt Armor](https://promptarmor.com/) - 🆕 企业级 prompt 注入实时检测。
- [Descope MCP Auth](https://www.descope.com/) - 🆕 MCP 服务的认证与授权层。
- [AgentDojo](https://github.com/ethz-spylab/agentdojo) - 🆕 ETH 苏黎世评测工具调用 Agent 的 prompt 注入攻防的研究基准。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fethz-spylab%2Fagentdojo&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ModelScan](https://github.com/protectai/modelscan) - 扫描 ML 模型权重文件（Pickle / PyTorch / TF）的反序列化攻击。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fprotectai%2Fmodelscan&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [PyRIT](https://github.com/microsoft/PyRIT) - 微软面向生成式 AI 的 Python 风险识别工具 —— 自动化红队框架（2026 年 3 月从 Azure/PyRIT 迁移，持续活跃维护）。与下方 RAMPART 互补。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2FPyRIT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAMPART](https://github.com/microsoft/RAMPART) - 🆕 **2026 年 5 月 20 日**。Microsoft 出品的 pytest 原生、面向 Agentic AI 的安全/可靠性测试框架。开发者侧白盒，与 PyRIT 互补——跨提示注入探针、良性失败断言、危害类别覆盖、统计阈值（如 80%+ 的运行需达到安全标准）。可直接接入 CI/CD。MIT。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2FRAMPART&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Clarity (Microsoft)](https://www.microsoft.com/en-us/security/blog/2026/05/20/introducing-rampart-and-clarity-open-source-tools-to-bring-safety-into-agent-development-workflow/) - 🆕 **2026 年 5 月 20 日**。RAMPART 的姊妹工具。AI Agent 的结构化设计评审工具——在写代码前生成关于意图、风险与行为的 "living artifacts"。Microsoft AI Red Team 的内部实践开源版。
- [MCP Gateway & Registry](https://github.com/agentic-community/mcp-gateway-registry) - 🆕 企业级 MCP 网关与注册中心：集中托管 AI 开发工具，OAuth 认证、动态工具发现、审计链、Keycloak / Entra 集成。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentic-community%2Fmcp-gateway-registry&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangSmith Sandboxes](https://www.langchain.com/blog/interrupt-2026-overview) - 🆕 **2026 年 5 月（Interrupt 2026）**。LangChain 托管的 Agent 安全代码执行环境——文件系统、shell、包管理、持久态、网络隔离。与 LangSmith Engine、Managed Deep Agents 同期发布。
- [WalletPrint](https://github.com/Loai17/walletprint-sdk) - ⚠️ **未经验证**（早期项目）。开源 Agent 钱包行为风险评分 SDK：在交易签名前通过钱包历史行为标记异常，支持 ZeroDev 与 LangChain 集成。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FLoai17%2Fwalletprint-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Alchemy & Visa AgentCard](https://www.coindesk.com/business/2026/06/18/alchemy-s-ai-driven-identity-and-payment-service-gains-access-to-visa-network) - 🆕 **2026-06-18**。基于 **Visa Intelligent Commerce** 的 AI Agent 支付 + 身份栈：一个 API 即可为 Agent 配齐交易所需的一切——Visa 支付令牌、专属邮箱与手机号、加密钱包——让其在受控范围内代表用户付款。默认走 Visa 令牌，也支持加密货币、x402 与 Stripe Machine Payments Protocol；模型无关（OpenAI / Anthropic 等）。
- [Nobulex](https://github.com/arian-gogani/nobulex) - ⚠️ **未验证。** AI Agent 行为的密码学回执（Ed25519 双签名 + 哈希链审计日志）。MIT。其双向回执原语已 [合并](https://github.com/microsoft/agent-governance-toolkit/pull/1333) 进 Microsoft Agent Governance Toolkit（PR #1302、#1333）。同一份投稿同期发往 15+ awesome list；提交者宣称的 "4,500 npm 月下载" 与 registry 实际数据不符（`@nobulex/mcp-server` 审计时仅约 19/月）。基于 Microsoft 的采用列入，仅作可见度参考，依赖前请自行评估。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Farian-gogani%2Fnobulex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ActPlane](https://github.com/eunomia-bpf/ActPlane) - 🧪 操作系统层 Agent harness，通过 eBPF 在系统调用边界强制执行以 YAML 定义的行为契约 —— 约束对任何工具、子进程或直接系统调用都生效，违规时向 Agent 反馈纠正信息。MIT。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Feunomia-bpf%2FActPlane&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsoft Prompt Shields](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection) - Azure AI Content Safety 功能，检测越狱与藏在 Agent 读取的文档/网页中的间接 prompt 注入（2024 年 GA；后续扩展支持 Agent 工作负载）。集成 Azure OpenAI Service 与第三方模型。
- [Agent Name Service (ANS)](https://www.ciodive.com/news/linux-foundation-prepares-open-standard-ai-agent-verification/823691/) - 🆕 **2026 年 6 月**。Linux 基金会推动的 AI Agent 验证与可信身份开放标准。去中心化 Agent 名称注册表，让 Agent 可验证对方真实身份，降低冒充与中间人攻击风险。
- [OpenAI Daybreak](https://openai.com/index/daybreak-securing-the-world/) - 🆕 **2026 年 6 月**。OpenAI 安全倡议 + 升级版 Codex Security 插件，自动发现并修复 AI 相关代码中的漏洞；内建针对 Agent 应用的 prompt 注入加固。
- [Lineation.ai](https://lineation.ai) - 🆕 ⚠️ **2026 年 7 月**（新厂商）。Agent 问责层 —— 可观测、治理与防御，带取证级推理链路（reasoning lineage）。旨在防止目标劫持、记忆污染、工具滥用；审计日志支持 SOC 2 / HIPAA / EU AI Act 合规。云端免费入门 + 私有化部署。
- [First Recon AI 安全运行时](https://firstrecon.ai) - 🆕 **2026 年7月**。企业级 AI 治理平台，检测每一条 AI 交互（人-模型 / Agent-工具 / Agent-Agent）。语义安全引擎在数据到达模型前就执行策略，生成完整决策审计日志。macOS + Windows 端点 Agent。
- [CrowdStrike Falcon AIDR](https://www.crowdstrike.com/en-us/platform/falcon-aidr-ai-detection-and-response/) - **2025 年 12 月 GA**。AI Detection and Response —— 对企业内员工 AI 使用与 Agent 活动的可见性、风险评分、行为异常检测、prompt 注入拦截，以及在 AI 交互层的实时策略执行。
- [Exabeam Agent Behavior Analytics](https://www.exabeam.com/) - 🆕 **2026**。Exabeam 行为智能平台向 Agentic AI 风险的扩展 —— 以持续的「验证-观察-分析-改进」循环取代静态护栏。
- [JADEPUFFER（Sysdig 披露）](https://hackread.com/sysdig-jadepuffer-first-agentic-ransomware-operation/) - 🆕 ⚠️ **威胁事件，非工具 —— 2026-07-02**。Sysdig 披露首个完全由 AI Agent 编排执行的勒索软件攻击：一个大模型驱动的 Agent 利用 Langflow 远程代码执行漏洞（CVE-2025-3248）入侵，盗取凭据并横向移动到生产 MySQL/Nacos 服务器，在31秒内自行修正失败步骤，随后用一个从未保存的临时 AES 密钥加密了 1,342 项配置，使赎金诉求彻底失去意义（即使付钱也无法恢复）。攻击载荷带有自然语言推理注释，强烈暗示为大模型生成。列于此处作为上方 Agent 安全工具（护栏、出站控制、凭据限权）在生产环境中为何必要的参考案例。

---

## 🔍 RAG 与知识库

*Agent 的检索增强生成与知识管理系统。*

- [Oracle OCI Enterprise AI updates](https://blogs.oracle.com/ai-and-datascience/whats-new-in-ai-june-2026) - 🆕 **2026-06**。企业级部署 Cohere Rerank 4 以增强 RAG 与 Agent 化企业搜索，并扩展支持阿里 / Google 新模型。
- [LlamaIndex](https://github.com/run-llama/llama_index) - LLM 应用的数据框架：摄取 / 结构化 / 访问私有数据。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Frun-llama%2Fllama_index&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangChain Retrievers](https://github.com/langchain-ai/langchain) - LangChain 的检索器与文档加载器集合。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Haystack](https://github.com/deepset-ai/haystack) - 端到端 RAG。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeepset-ai%2Fhaystack&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Unstructured](https://github.com/Unstructured-IO/unstructured) - 文档预处理与提取。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FUnstructured-IO%2Funstructured&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Weaviate](https://github.com/weaviate/weaviate) - 开源向量数据库。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fweaviate%2Fweaviate&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Qdrant](https://github.com/qdrant/qdrant) - Rust 实现的高性能向量搜索。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fqdrant%2Fqdrant&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Milvus](https://github.com/milvus-io/milvus) - 大规模向量数据库。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmilvus-io%2Fmilvus&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Pinecone](https://www.pinecone.io/) - 托管向量数据库 SaaS。
- [Chroma](https://github.com/chroma-core/chroma) - AI 原生开源向量数据库。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fchroma-core%2Fchroma&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vanna](https://github.com/vanna-ai/vanna) - 📦 **Archived**（2026-03）。RAG-for-SQL：自然语言对话数据库。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvanna-ai%2Fvanna&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LightRAG](https://github.com/HKUDS/LightRAG) - 🇨🇳 港大 HKUDS 的图式 RAG。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2FLightRAG&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Docling](https://github.com/docling-project/docling) - IBM 文档转换工具，PDF / DOCX / HTML 等。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdocling-project%2Fdocling&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Kotaemon](https://github.com/Cinnamon/kotaemon) - 开源 RAG UI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FCinnamon%2Fkotaemon&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [R2R](https://github.com/SciPhi-AI/R2R) - 端到端 RAG 服务，企业级。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSciPhi-AI%2FR2R&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAGFlow](https://github.com/infiniflow/ragflow) - 🇨🇳 深度文档理解 RAG。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Finfiniflow%2Fragflow&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Morphik](https://github.com/morphik-org/morphik-core) - 🆕 面向包含表格、图表的多模态文档的 RAG 引擎；2026 年快速崛起，是处理复杂 PDF 的 LlamaIndex 替代方案。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmorphik-org%2Fmorphik-core&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cognee](https://github.com/topoteretes/cognee) - 🆕 在 Agent 摄取文档过程中实时构建知识图谱的记忆 + 推理引擎；2026 年长时研究型 Agent 栈的热门选择。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftopoteretes%2Fcognee&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAG-Anything](https://github.com/HKUDS/RAG-Anything) - 🆕 港大数据科学实验室出品的一体化多模态 RAG 框架。基于 LightRAG 构建；文本与多模态并行流水线；可查询同时包含文本、图示、表格、公式的文档。MIT，21K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2FRAG-Anything&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [A-MEM](https://github.com/WujiangXu/A-mem-sys) - 🆕 面向 LLM Agent 的 Agentic Memory 系统——受 Zettelkasten 卡片盒笔记法启发的动态记忆组织与笔记链接，比静态向量存储更灵活的检索。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FWujiangXu%2FA-mem-sys&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 💻 编程 Agent

### 终端 / CLI Agent

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - 直接在终端里运行的 Agent 编程工具。Opus 4.7 + `/think xhigh`。SWE-bench 80.9%。
- [Codex CLI](https://github.com/openai/codex) - OpenAI 出品，开源终端编程 Agent。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fcodex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Codex Security](https://developers.openai.com/codex/changelog) - 🆕 **2026 年 3 月**。应用安全 Agent，负责发现并修复软件漏洞；OSS 维护者可通过 Codex-for-OSS 计划使用。
- [Aider](https://github.com/Aider-AI/aider) - 💤 Git-aware 终端 AI 编程伙伴，兼容任意 LLM。最后版本 2025-08。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAider-AI%2Faider&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Goose](https://github.com/block/goose) - Block 出品的开源 Agent 编程 CLI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fblock%2Fgoose&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) - 🆕 Google 的终端优先编码 Agent，擅长大上下文重构。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle-gemini%2Fgemini-cli&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenCode](https://github.com/anomalyco/opencode) - 开源终端 AI 编码 Agent（opencode.ai，180K+ stars）—— build/plan 双 Agent、LSP、MCP，桌面 App 处于 beta；与已归档的 opencode-ai/opencode 无关。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fanomalyco%2Fopencode&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Crush](https://github.com/charmbracelet/crush) - Charm 出品的终端 AI 编码 Agent —— 已归档 opencode-ai/opencode 的继任者；多模型，支持 LSP + MCP。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcharmbracelet%2Fcrush&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Grok Build](https://x.ai/news/grok-build-cli) - 🆕 **2026 年 5 月 25 日（早期 beta）**。xAI 的 Agent 化 CLI 编码工具，由 **grok-code-fast-1** 驱动。子 Agent 并行运行于隔离环境，每日发布 release notes；SuperGrok 与 X Premium Plus 订阅用户可用。xAI 对 Claude Code / Codex CLI 的正面回应。⚠️ 2026 年 7 月有报道发现 Grok Build 会把整个 git 仓库上传到 xAI 存储 —— 在私有代码上使用前请先审查。
- [Antigravity CLI](https://antigravity.google/blog/introducing-google-antigravity-2-0) - 🆕 **2026 年 5 月 19 日（Google I/O 2026）**。Antigravity 2.0 的轻量 CLI 伴侣——直接从终端创建并使用 Google 的 Agent harness。支持 macOS / Linux / Windows。据报道自 2026 年 6 月 18 日起面向托管套餐用户接替 Gemini CLI（开源 gemini-cli 仓库仍活跃，105K+ stars）。
- [Microsoft physical-ai-toolchain](https://github.com/microsoft/physical-ai-toolchain) - 🆕 **2026 年 6 月**。生产就绪的开源工具链，整合微软 Azure 云服务与 NVIDIA 物理 AI 栈——覆盖自主移动机器人与机械臂的数据整理、训练与部署的 Agentic 工作流。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fphysical-ai-toolchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [PhyAgentOS](https://github.com/PhyAgentOS/PhyAgentOS) - 🆕 基于 Agentic 工作流的自进化具身 AI 操作系统。将认知功能与硬件解耦，实现跨平台机器人部署并内建可审计性。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FPhyAgentOS%2FPhyAgentOS&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code) - 🆕 🇨🇳 **2026 年 6 月 6 日**。Moonshot AI 的终端编程 Agent（TypeScript，MIT）。内置 coder / explore / plan 子 Agent 在隔离上下文中运行，通过 `/mcp-config` 对话式配置 MCP。npm 安装。专为下一代 Kimi K2.6 Agent 设计。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FMoonshotAI%2Fkimi-code&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MAI-Code-1-Flash in GitHub Copilot](https://microsoft.ai/news/introducingmai-code-1-flash/) - 🆕 **Build 2026（2026 年 6 月 2 日）**。微软首个 100% 自研的 5B 编程模型作为 GitHub Copilot 的模型选项落地——在四大核心编程基准上击败 Claude Haiku 4.5（SWE-Bench Pro 51.2% vs 35.2%），成本显著更低。
- [Claude Agent SDK](https://docs.anthropic.com/en/docs/claude-code/sdk) - 基于 Claude Code harness 构建 Agent 的 SDK（2025 年 9 月末由 Claude Code SDK 更名而来）。**2026 年 6 月**的 Claude Code 版本新增层级式子 Agent 生成、Dynamic Workflows（一次扇出数十至数百个并行子 Agent）、基于评分细则的 Outcomes 与降级模型链 —— 支撑 ultracode 模式，单次执行最多 1,000 个子 Agent。Python + TypeScript。
- [ai-delivery-spec](https://github.com/franklinxkk/ai-delivery-spec) - 🆕 ⚠️ **未验证。** 面向与 AI 编程 Agent（Claude Code、OpenClaw、Codex、Cursor、Copilot）协作的 PM 的规格驱动交付框架。4 档交付层级、0D 分诊路由、原型可测性规则、AI 运行时治理、5 个领域模块。SKILL.md 规范；托管于 ClawHub。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ffranklinxkk%2Fai-delivery-spec&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Ralph Harness](https://github.com/rxdt/py_ralph_frame) - 🆕 ⚠️ **未验证。** 极简 Python 脚手架，用于带护栏的 Claude Code/Codex/Gemini 循环：仓库内规格、全新上下文迭代、git hook 关卡、CI 验证与覆盖率门槛。可通过 `uvx ralph-harness demo` 安装。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Frxdt%2Fpy_ralph_frame&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### IDE Agent

- [Cursor 3.11](https://cursor.com/changelog) - 🆕 **2026-07-10**。侧边聊天（Side Chats，不干扰主工作流的并行 AI 对话）、对话历史搜索、项目/仓库选择器重设计、新 Cloud Agent Hooks（对 Agent 对话的提示词/响应/子 Agent 活动的精细控制与可观测性）。
- [Cursor 3.4（Teams + PR 审查）](https://cursor.com/changelog) - 🆕 **2026-05-11~13**。Microsoft Teams 集成（在 Teams 中 `@Cursor` 即可委派云端 Agent）、并行 Agent 计划执行提速、多仓库 / 基于 Dockerfile 的 Agent 开发环境配置、`/multitask` 异步子 Agent、漏洞扫描器、按模型粒度的访问控制。
- [Cursor 3.3](https://cursor.com/changelog) - 🆕 **2026-05**。PR 审查体验、并行 Agent、企业级模型管控；上一版 3.1 发布于 4 月。
- [Cursor SDK](https://cursor.com/blog/typescript-sdk) - 🆕 **2026-04-29**（公开 beta）。TypeScript SDK 开放 Cursor 的运行时、harness 和模型，开发者可在 Cursor 栈上构建程序化 Agent —— 沙箱化云 VM、子 Agent、hooks、按 token 计费。
- [Kilo Code](https://kilo.ai/) - 开源 AI 编程扩展（VS Code / JetBrains），Auto Model 路由覆盖 500+ 模型；已被 Anaconda 收购（2026）。重点采用 MiniMax 系列模型。
- [Cursor](https://www.cursor.com/) - 2026-02 更新支持 8 个并行 Agent。
- [Windsurf → Devin Desktop](https://devin.ai/blog/windsurf-is-now-devin-desktop/) - 🆕 **2026-06-02 更名**。Cognition 将 Windsurf IDE 更名为 **Devin Desktop**（windsurf.com 跳转至 devin.ai）：**Devin Local**（Rust 重写，token 效率提升约 30%，支持子 Agent）取代 Cascade，**Agent Command Center** 看板成为默认界面，并内置开放的 **Agent Client Protocol (ACP)**。Cascade 于 2026-07-01 停止支持。
- [Cline](https://github.com/cline/cline) - VS Code 自主编程 Agent。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcline%2Fcline&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Continue](https://github.com/continuedev/continue) - 开源 AI 编程助手（VS Code + JetBrains）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcontinuedev%2Fcontinue&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Roo Code → Roomote](https://roomote.dev/) - ⚠️ **已停止 IDE 扩展形态。** Roo Code 于 2026-04-22 宣布 5 月 15 日关停其 VS Code 扩展、Cloud 与 Router，转向云端编码 Agent **Roomote**（Slack/GitHub/Linear → PR）；roocode.com 现跳转至 roomote.dev。
- [Void](https://github.com/voideditor/void) - 💤 **暂停开发**（未归档 —— 维护者在探索新的编码方向；当前无活跃维护）。VS Code 的开源 fork，定位为开源版 Cursor；数据留在本地，自带模型。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvoideditor%2Fvoid&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [GitHub Copilot](https://github.com/features/copilot) - 2026 初支持 Agent 模式，`gh copilot` 终端集成。
- [Kiro](https://kiro.dev/) - AWS 自主 Agent。Spec-driven，最多 10 个并发任务。
- [Amazon Q Developer](https://aws.amazon.com/q/developer/) - AWS 生态深度集成。
- [Visual Studio 2026 Agent Mode + Skills](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/) - 🆕 **VS 2026 Insiders 2026-05-12 – 15**。Copilot Chat "Agent Mode" 现在能在 Visual Studio 2026 里发现、管理、创建可复用的 Copilot Skill，能看到整个解决方案的上下文，还能执行终端命令与调用外部工具。
- [JetBrains Rider AI Test-Writing Skill](https://blog.jetbrains.com/dotnet/2026/05/22/claude-codex-ai-agent-skill-for-writing-tests/) - 🆕 **2026 年 5 月 22 日**。JetBrains Rider 新增的 AI Assistant skill，把 .NET 代码覆盖率数据喂给 Claude Code / Codex，让 Agent 聚焦未覆盖分支，降低测试生成的 AI 成本。

### 自主软件工程师

- [Cursor 3.4 云 Agent 环境](https://cursor.com/changelog) - 🆕 **2026-05-13**。为云上 Agent / 自动化提供多仓库环境、带 build secrets 的 Dockerfile 配置、快 70% 的镜像层缓存、每个环境独立的版本历史 + 回滚、审计日志、限定范围的出网 / secrets。
- [Devin Security Swarm](https://cognition.com/blog) - 🆕 **2026-07-01**。Cognition 的并行 Agent 安全产品：跨代码库发现漏洞、在运行时验证可利用性并提交修复 PR；实测发现 50 个真实漏洞中的 36 个，单个发现的成本比次优工具低约 30%。
- [Devin 2.2](https://cognition.com/blog/introducing-devin-2-2) - 🆕 **2026-02-24**。带 Computer Use 的端到端测试（Linux 桌面 + 屏幕录制）、提 PR 前自审/自动修复、启动快 3 倍。Cognition 的旗舰自主软件工程师（Devin 2.x 系列；Devin 2.0 起 Core 套餐 $20/月起）。
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) - 自托管的开源 Agent 软件开发平台。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAll-Hands-AI%2FOpenHands&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SWE-agent](https://github.com/SWE-agent/SWE-agent) - 把 LLM 变成能修复 GitHub issue 的工程师。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSWE-agent%2FSWE-agent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Devika](https://github.com/stitionai/devika) - 💤 **Stale**（2025-09 起无更新）。开源 Devin 替代。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstitionai%2Fdevika&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [GPT Engineer](https://github.com/gpt-engineer-org/gpt-engineer) - 📦 **Archived**（2026-04）。第一波自主编程项目，仅作历史参考。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgpt-engineer-org%2Fgpt-engineer&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Codegen](https://github.com/codegen-sh/codegen) - 💤 程序化代码操作 + 跨文件重构 SDK（最后版本 2025-09）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcodegen-sh%2Fcodegen&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Qodo](https://www.qodo.ai/) - 🆕 AI 代码评审平台：质量 + 安全 + 测试生成。
- [Google Antigravity 2.0](https://antigravity.google/blog/introducing-google-antigravity-2-0) - 🆕 **2026 年 5 月 19 日（Google I/O 2026）**。独立桌面应用（macOS / Linux / Windows），可并行编排多个 Agent。新增 cron 化的定时任务、长跑异步任务、动态子 Agent，以及与 AI Studio / Android / Firebase 的集成。配套的 **Antigravity SDK** 支持自部署 harness；企业版集成进 Gemini Enterprise Agent Platform。

---

## 🤖 Physical AI / 具身智能

*能感知、推理、在物理世界中行动的 AI —— 人形机器人、工厂自动化、Physical AI 基础设施。继语言 Agent 之后的下一波。*

### 基础模型与研究
- [ENPIRE](https://research.nvidia.com/labs/gear/enpire/) - 🆕 **2026-06**。NVIDIA/CMU/UC Berkeley 联合框架，让 AI Agent 自主开展机器人研究 —— 管理双臂机器人、修改算法、训练策略，全程无需人工干预。
- [Kairos](https://futureiot.tech/kairos-model-breaks-new-ground-for-open-source-embodied-intelligence/) - 🆕 **2026-06-15**。ACE ROBOTICS 开源其 Kairos 世界模型 —— 首个在 RoboTwin 2.0、LIBERO-Plus、WorldModelBench Robot 与 DreamGen 上超越 VLA 系统的世界模型路线；权重上 GitHub / Hugging Face / ModelScope。
- [NVIDIA Cosmos 3](https://www.axios.com/2026/06/08/ai-news-nvidia-cosmos-3-openai-sites-solara-rtx-spark) - 🆕 **2026-06**。专为物理 AI 设计的底层基础模型。它并非仅仅基于文本，而是主要针对物理定律和空间几何进行训练，目标应用包括机器人和工厂自动化。

- [Google Gemini Robotics-ER 1.6](https://deepmind.google/blog/gemini-robotics-er-1-6/) - 🆕 2026-04-14。机器人 AI，空间/具身推理增强（含模拟仪表读数），可通过 Gemini API 使用。
- [Project Prometheus (Bezos)](https://techcrunch.com/2026/06/11/jeff-bezoss-prometheus-raises-12b-to-build-an-artificial-general-engineer-for-the-physical-world/) - 🆕 💰 **2026-06-11**。贝佐斯联合主导的 Physical AI 项目，以 $41B 估值融资 $12B，目标打造面向物理世界的「通用人工工程师」。
- [NVIDIA Isaac GR00T](https://developer.nvidia.com/isaac/gr00t) - 人形机器人基础模型平台。GTC 发布、Hannover Messe 2026 扩展。
- [NVIDIA Industrial AI Cloud](https://nvidianews.nvidia.com/) - 🆕 2026-04（Hannover Messe）。德国电信合建 AI factory。

### 人形机器人

- [Tesla Optimus Gen3](https://www.tesla.com/) - 🆕 2026 夏季量产。
- [Figure 04](https://autonews.gasgoo.com/articles/news/figure-founder-f04-robot-initiates-component-delivery-process-2054560059634376705) - 🆕 **2026-05-13**。Brett Adcock 宕告 Figure 04 设计定型，零部件已开始交付，使用 Helix VLA 型号。
- [Helix 02 包裹分拧 72h 运行](https://oodaloop.com/briefs/technology/figure-ais-humanoid-robots-sort-88000-packages-in-72-hours-during-nonstop-livestream/) - 🆕 **2026-05-13 – 16**。Figure F.03 机器人队靠 Helix 02 完全自主在包裹分拧线上运行：首天 ~22K 包裹，头 24 小时 ↑到 ~30K，压力测试下约 72 小时 ~88K 包裹后出现机械故障。首份公开的家用型人形机器人连续作业证据。
- [Figure F.03 vs 人类 8 小时分拧挑战](https://incrypted.com/en/figure-ai-held-a-human-vs-robot-marathon/) - 🆕 **2026-05-18**。Figure 首场公开的人机对决：在同一条分拧线上，人类员工以 12,924 件（2.79 秒 / 件）势均微赢 F.03 机器人的 12,732 件（2.83 秒 / 件）。这是到目前为止公开资料中人与机器在实际产业任务上最贴近的一次。
- [Boston Dynamics Atlas 100 磅操作 + 现代集团 25K 刷屏计划](https://www.techtimes.com/articles/316854/20260519/boston-dynamics-reveals-how-atlas-learned-lift-100-pound-loads-hyundai-plans-30000-per-year.htm) - 🆕 **2026-05-18 / 19**。Boston Dynamics 发布视频与技术博文，展示 Atlas 通过强化学习 + 大规模仿真能举起并携带 **超 100 磅**负荷（冰箱 / 洗衣机），全身控制能适应重量转移，不依赖逐件识别。现代汽车集团承诺从 2028 年起在 Hyundai/Kia 工厂部署 **25,000+ 台 Atlas**。
- [现代集团完成对 Boston Dynamics 的全资收购](https://www.techtimes.com/articles/320483/20260714/boston-dynamics-now-fully-hyundais-atlas-exits-world-cup-eyes-factory-floor.htm) - 🆕 💰 **2026 年 6 月末**。现代汽车集团以 $325M 收购软银剩余 9.65% 股份，按约 $3.4B 估值实现 100% 持股。第 5 代新 Atlas 于 FIFA 世界杯（2026-07-05）公开亮相；计划 2027 年面向外部客户商用，2028 年部署于佐治亚 Metaplant。
- [Unitree G1 进驻 JAL 羽田机场](https://www.techtimes.com/articles/316862/20260519/jal-deploys-unitree-g1-robots-haneda-us-congress-moves-blacklist-supplier-national-security.htm) - 🆕 **2026-05**。日本航空在羽田启动地面运作试点（行李装卸 / 集装箱运输 / 机舱清洁），官方定义为 **全球首家在运营航空业务中录用双足机器人**的航司。同一周美国国会推动将 Unitree 列入实体清单，embodied AI 供应链加速地缘政治化。
- [Honor (荣耀) Humanoid](https://www.npr.org/2026/04/20/g-s1-118086/humanoid-robot-half-marathon) - 🆕 **2026-04-19**。以 50:26 赢得北京亦庄人形机器人半程马拉松 —— 打破该距离的人类世界纪录。
- [Zhiyuan (智元) AGIBOT](https://www.agibot.com/article/231/detail/62.html) - 🆕 🇨🇳 **2026-04-17（APC 2026）**。宣布 2026 为 "商用量产元年"（Deployment Year One）；第 10,000 台机器人下线交付，七大行业解决方案，开源 AIMA 架构（灵渠 OS Link-U、Genie Studio）。
- [Unitree H 系列](https://www.unitree.com/) - 🇨🇳 国产 Boston Dynamics 对手，2026 持续迭代。
- [1X NEO（消费级人形机器人）](https://www.1x.tech/discover/neo-home-robot) - 🆕 **2025 年 10 月 28 日开放预订**，首批美国家庭交付于 2026 年。5'6"/66 磅家庭人形，22 自由度灵巧手、柔体外壳、4 小时续航、机载 LLM、噪音约 22dB。早鸟价 20,000 美元 + 200 美元定金，或 499 美元/月订阅。隐私 "no-go" 区域与人脸模糊内置。首款真正交付家庭的消费级人形。
- [三菱汽车 × Highlanders 人形机器人 MOU](https://www.mitsubishi-motors.com/en/newsroom/newsrelease/2026/20260709_1.html) - 🆕 **2026-07-09**。三菱汽车与东京大学初创公司 Highlanders 签署 MOU，将在其京都工厂共同研发并量产人形机器人（焊接、物流、发动机装配）—— 据报道目标约 1,000 台/月，最早 2027 年投产，以应对日本劳动力短缺。
- [Agile Robots](https://www.agile-robots.com/) - 德中合资机器人公司，构建 AI 驱动的工业操作系统。
- [Shenzhen Humanoid Pilot Line](https://www.chinadailyhk.com/hk/article/631892) - 🇨🇳 🆕 **2026-04-12** 首条人形机器人中试线（深圳乐聚 + 东方精工）。2 小时一台，年 500~1000 台。佛山 1 万台 / 年大规模工厂同步规划中。

### 消费级机器人 / 可穿戴

- [Doubao AI Glasses (字节)](https://technode.com/2026/03/18/bytedance-reportedly-delays-doubao-ai-glasses-launch-plan/) - ⚠️ 🇨🇳 一代产品据报道在发布前被砍（"过于平庸"）；在 AI 眼镜市场年增约 130% 的背景下，字节正加速推进双模型的二代产品（2026 年 7 月）。
- [Nothing AI Glasses/Earbuds](https://techcrunch.com/2026/04/01/nothings-ai-devices-plan-reportedly-contains-smart-glasses-and-earbuds/) - 🧪 2026 年 3 月报道：Nothing 计划推出 AI 智能眼镜 + 耳机，目标 2027 年发布。
- [Samsung Galaxy S26 (Gauss 2.3)](https://www.samsung.com/) - 端侧 Agent。
- [Meta Ray-Ban Display / Ray-Ban Meta](https://www.meta.com/ai-glasses/) - Meta 在售的 AI 眼镜产品线（含配 Neural Band 的 Display 型号）；Ray-Ban Meta Gen 3 传闻 2026 年底发布。

### 自动驾驶

- [Tesla FSD v14](https://www.tesla.com/) - v14.3.x 推送中（2026-07），含面向老款 HW3 车型的 v14 "Lite"；无监督运行仍限于 robotaxi 项目。
- [Waymo](https://waymo.com/) - 美国多城市 L4 商业化推进。
- [WeRide / Pony.ai / Baidu Apollo](https://www.weride.ai/) - 🇨🇳 中国 L4 车队扩区。
- [Tesla Optimus Gen3 (V3)](https://www.teslarati.com/tesla-optimus-awe-2026-shanghai/) - 🆕 **AWE 2026 上海首秀**。首款量产 Optimus；Fremont 产线 2026 年 1 月启动，初期目标 5-10 万台/年，初始售价约 3 万美元，2026 年底开放小批量外部销售。37 关节，1.2 m/s 步速，22 自由度手部。
- [Figure 03 (Helix AI)](https://blog.robozaps.com/b/figure-03-review) - 🆕 **2025 年末发布，2026 年量产爬坡**。Figure 首款专为家用设计的型号：柔性纺织外壳、无线充电、触觉传感。2026 年 5 月演示：两台 F.03 仅靠视觉协作，2 分钟内自主完成清扫房间和铺床。
- [Figure 02 + Helix 02](https://en.wikipedia.org/wiki/Figure_AI) - 🆕 **2026 年 1 月**。Helix 02 扩展了全身自主能力（装卸洗碗机、叠衣服）；BotQ 工厂额定年产能 1.2 万台。
- [Unitree G1 + H2](https://community.robotshop.com/blog/show/unitree-robotics-at-ces-2026-a-clear-signal-of-whats-coming-next) - 🆕 **CES 2026**。G1 跳舞 / 拳击 / 滑冰演示，2 月放出自主功夫展示；以及 31+ 自由度的 H2 人形。
- [Unitree R1 Air](https://humanoid.guide/unitrees-4900-r1-air-pushes-humanoids-toward-mass-market/) - 🆕 消费级人形机器人，售价 **4,900 美元**——能跑、翻滚、倒立行走。
- [Unitree Gen 2 (lifelike skin)](https://www.youtube.com/watch?v=Gmp82MuTFsM) - 🆕 拟真人造皮肤，内嵌压力 / 温度 / 触觉传感器。
- [Unitree GD01](https://www.extremetech.com/computing/unitree-will-sell-you-a-personal-mecha-robot-for-650000) - 🆕 **2026 年 5 月**。接近 10 英尺的载人机甲；驾驶员操控，可在双足与四足模式切换。售价人民币 390 万元起（约 65 万美元）。预示具身 Agent 栈开始向操作员驾驶形态分叉。

---

## 🎮 Agent 仿真与世界模型

*Agent 在仿真世界中训练、观察、应力测试的研究环境。世界模型 / 具身研究渗透到语言 Agent 设计中后越来越重要。*

- [Generative Agents](https://github.com/joonspk-research/generative_agents) - 💤 斯坦福经典 *Smallville*（Park et al., 2023）。25 个 LLM 角色 + 记忆 + 反思 + 计划。后续多 Agent 论文几乎都借鉴此实现。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fjoonspk-research%2Fgenerative_agents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Voyager](https://github.com/MineDojo/Voyager) - 💤 Minecraft 终生学习 Agent —— GPT-4 + skill library + curriculum（Wang et al., 2023）。开放式 Agent 评测的经典。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FMineDojo%2FVoyager&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SWE-Gym](https://github.com/SWE-Gym/SWE-Gym) - 用真实 GitHub issue 训练 SWE Agent 的开放环境，SWE-bench 配套。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSWE-Gym%2FSWE-Gym&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [WebArena](https://webarena.dev/) - 真实可复现的 Web 环境（Reddit / 购物 / GitLab 克隆），OSWorld 与多数浏览器 Agent 论文使用。**[WebArena-Verified](https://github.com/ServiceNow/webarena-verified)**（ServiceNow，2025-12）：全部 812 个任务、参考答案与评测器经人工复核；用确定性的类型感知校验取代 LLM-as-judge；另提供 258 题 "Hard" 子集以降低评测成本。
- [WorkArena](https://github.com/ServiceNow/WorkArena) - ServiceNow 出品的企业工作场景 Web Agent 基准。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FServiceNow%2FWorkArena&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Genie 3](https://deepmind.google/models/genie/) - Google DeepMind 可玩 3D 世界模型，从 prompt 生成。闭源研究。
- [NVIDIA Cosmos](https://github.com/nvidia-cosmos/cosmos-predict2) - 具身 AI / 机器人的世界模型基础，生成物理合理的视频未来。predict1 已弃用，由 Cosmos-Predict2 接替（Predict 2.5 于 CES 2026 发布）；另见上方 Cosmos 3（2026-06）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fnvidia-cosmos%2Fcosmos-predict2&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Snowflake Agent World Model (AWM)](https://github.com/Snowflake-Labs/agent-world-model) - 🆕 **2026 年 2 月 10 日开源，5 月 1 日被 ICML 2026 接收**。合成环境生成流水线，一次性产出 1,000 个可执行的、SQL 数据库驱动的工具调用环境（35K+ 工具，10K 任务），通过统一 MCP 接口暴露——支持大规模多回合 Agent RL。基础设施已合入 `meta-pytorch/OpenEnv`。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSnowflake-Labs%2Fagent-world-model&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Qwen-AgentWorld](https://github.com/QwenLM/Qwen-AgentWorld) - 🆕 **2026 年 6 月**。原生语言世界模型，通过预测环境（网页、操作系统、终端）的下一状态而非 Agent 的下一动作来模拟 Agentic 环境。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FQwenLM%2FQwen-AgentWorld&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SimWorld](https://github.com/SimWorld-AI/SimWorld) - 🆕 基于 Unreal Engine 5 的开放式真实感模拟器，用于在复杂物理与社交环境中测试自主 AI Agent。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSimWorld-AI%2FSimWorld&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 📊 评测与 Leaderboard

*跟踪前沿 AI 能力的标准评测套件与实时榜单。*

- [BenchLM](https://benchlm.ai/) - 🆕 多家基准聚合榜单。2026-07 榜首：Claude Fable 5 91，Claude Mythos 5 89，Gemini 3.1 Pro 88（79 个上榜 / 281 个跟踪模型，296 项基准）。
- [SWE-bench Verified](https://www.swebench.com/) - 真实 GitHub issue 修复基准。2026-04 榜首：Claude Mythos 93.9%，Claude Opus 4.7 87.6%。
- [GPQA Diamond](https://github.com/idavidrein/gpqa) - 💤 数据集仓 2024-09 起无更新。专家级科学推理。2026-04 榜首：Gemini 3.1 Pro 94.3%（世界纪录）、Claude Opus 4.7 94.2%。
- [ARC-AGI 2](https://arcprize.org/) - 抽象推理。GPT-5.5 以 85% 领先（2026-07）；Gemini 3.1 Pro 77.1%（2026-03）。
- [ARC-AGI-3](https://arcprize.org/leaderboard) - 🆕 🧪 第三代 ARC 基准 —— Agent 必须实时适应全新交互环境（Kaggle 竞赛）。早期最高分接近零（Gemini 3.1 Pro 约 0.37%）。
- [OSWorld](https://os-world.github.io/) - 桌面 GUI 操作。Claude Fable 5 / Mythos 5 以 85% 领先（2026-07）；GPT-5.4 75%（超过人类基线）。
- [Arena（前 LMArena / Chatbot Arena）](https://arena.ai/) - 众包对话偏好。2026-07：Claude Fable 5 领先（Elo 1525），领先于 Opus 4.8（1512）与 GPT-5.5 Pro（1510）。
- [MMLU-Pro](https://github.com/TIGER-AI-Lab/MMLU-Pro) - MMLU 加难版。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTIGER-AI-Lab%2FMMLU-Pro&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LiveCodeBench](https://livecodebench.github.io/) - 持续更新的竞赛风编程基准。
- [AIME 2025 / Humanity's Last Exam (HLE)](https://agi.safe.ai/) - 数学 / 博士级综合推理。
- [Terminal-Bench](https://www.tbench.ai/) - CLI Agent 评测。Codex CLI 77.3%。
- [Wolfram LLM Benchmarking Project](https://www.wolfram.com/llm-benchmarking-project/) - 英文规格 → Wolfram Language 代码生成。
- [Terminal-Bench 2.0](https://www.tbench.ai/leaderboard/terminal-bench/2.0) - **2025 末 / 2026 初**。89 个精选终端任务（编译、训练、配置、调试）。榜首：NexAU-AHE + GPT-5.5 84.7%（2026-05-14）。
- [GDPval](https://openai.com/index/gdpval/) - OpenAI 经济价值 benchmark（2025 年 9 月发布，arXiv:2510.04374），覆盖 44 个职业 / 9 个行业，含 1,320 个专家构建任务。[GDPval-AA 榜单](https://artificialanalysis.ai/evaluations/gdpval-aa)榜首（2026-07）：Claude Opus 4.8（Elo 1890），领先 GPT-5.5（1769）。在 GPT-5.6 发布（2026-07-09）时再次扩展 / 强调。
- [SWE-bench Pro](https://benchlm.ai/benchmarks/swePro) - 🆕 Verified 的仓库级工程后继。Claude Opus 4.7 64.3% > GPT-5.5 58.6%（Claude 在长程仓库任务领先）。**2026-07**：Claude Mythos 5 以 **80.3%** 登顶；⚠️ **OpenAI 审计（2026-07-08）**发现约 30% 的 Pro 任务存在缺陷（测试过严、题目欠明确）—— OpenAI 已撤回将 SWE-bench Pro 作为编程 Agent 主要评测指标的推荐。
- [LLM-Stats Live Leaderboard](https://llm-stats.com/llm-updates) - 🆕 实时更新的跨 benchmark 模型对比看板。
- [τ²-Bench (Tau-Bench)](https://github.com/sierra-research/tau2-bench) - 🆕 Sierra Research 出品的真实业务域（零售 / 航空）工具-Agent-用户交互基准。考察多轮工具使用、数据库操作与策略遵从。2026 年 4 月榜首：38 个评测模型中 Claude Mythos Preview 89.2%。该仓库现同时托管 **τ³-Bench 1.0.0（2026-03-18）**，新增语音以及电信/银行业务域。MIT。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsierra-research%2Ftau2-bench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Gartner 2026 魔力象限：企业 AI 编程 Agent](https://cursor.com/blog/cursor-leads-gartner-mq-2026) - 🆕 **2026 年**。Gartner 首个企业级编程 Agent MQ。领导者：**GitHub Copilot**、**OpenAI Codex**、**Cursor**（共评估 12 家厂商；Tabnine 为远见者）。标志着编程 Agent 市场迈入企业级成熟期。
- [Terminal-Bench 2.1](https://www.tbench.ai/leaderboard/terminal-bench/2.1) - 🆕 **2026-06**。扩展 CLI 任务覆盖的 Terminal-Bench 更新版；榜单：Claude Code + Fable 5 以 83.8% 领先（2026-06-07），Codex + GPT-5.5 83.1%。头部 CLI Agent 的差距已不足 1%。
- [Agent Memory Benchmark (AMB)](https://github.com/vectorize-io/agent-memory-benchmark) - 🆕 与 Hindsight 一同由 vectorize.io 发布的开放 Agent 记忆系统基准——针对长期任务表现测试 retain / recall / reflect 操作。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvectorize-io%2Fagent-memory-benchmark&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agents' Last Exam (ALE)](https://snorkel.ai/leaderboard/agents-last-exam/) - 🆕 **2026 年 6 月**。UC Berkeley (RDI) + Snorkel AI 出品，联合 300+ 行业专家、覆盖 55 个专业子领域的长程高经济价值任务 benchmark（公开版 ALE-V1：从 1,500+ 任务语料中抽出 147 个参考任务；arXiv:2606.05405）。发布时通过率约 2.6%；2026 年 7 月榜首：Codex + GPT-5.6 53.6/100（在 GPT-5.6 发布会上被重点展示）。任务每六个月轮换的动态 benchmark。
- [JetBrains Kotlin Benchmark](https://blog.jetbrains.com/kotlin/2026/07/introducing-the-kotlin-benchmark-evaluate-ai-coding-agents-on-real-world-kotlin-tasks/) - 🆕 **2026 年 7 月**。JetBrains 针对 Kotlin 语言的 AI 编程 Agent 公开 benchmark，覆盖代码生成、重构、测试编写与错误修复等真实开发任务。为开发者提供超越通用 SWE-bench 的语言专项评估。
- [Stripe Agent Benchmark](https://stripe.com/blog/can-ai-agents-build-real-stripe-integrations) - 🆕 **2026 年 3 月**。端到端评估套件，测试 AI Agent 是否能从零完成完整的 Stripe 集成，包括代码生成、测试执行和生产环境验证。初期评测中 Claude Opus 4.5 在全栈 API 集成任务上平均得分 92%。
- [GAIA Benchmark](https://huggingface.co/spaces/gaia-benchmark/leaderboard) - 通用 AI 助手基准：466 个真实任务上的多步推理 + 工具使用 + 网页浏览。**2026-07-15 公开快照**：Claude Mythos 5 与 Claude Fable 5 以 **52.3%** 并列领先，GPT-5.4 Pro 50.5% 次之。设计上可抵抗数据污染。

---

## 🖥️ Computer Use / 桌面 Agent

*能看屏幕、控鼠键、自动操作 OS 级软件的 Agent。纯浏览器 Agent 见 [🌐 浏览器与 Web Agent](#-浏览器与-web-agent)。*

- [Claude Computer Use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) - Anthropic 的 Computer Use 能力 —— Claude 看屏幕并用鼠标键盘自动操作任意软件。
- [ChatGPT Agent](https://openai.com/index/introducing-chatgpt-agent/) - Operator（2025 年弃用）的后继 —— ChatGPT 内的 Agent 模式，用于浏览、订票、填表与网页任务自动化。
- [Google Project Mariner](https://deepmind.google/models/project-mariner/) - 📦 **已关闭**（2026-05）。浏览器 Agent 研究项目，能力已合入 Gemini 与 Chrome。
- [Microsoft Copilot Agents](https://www.microsoft.com/en-us/microsoft-copilot/) - 🆕 Microsoft 365 上的自主后台 Agent。
- [Open Interpreter](https://github.com/OpenInterpreter/open-interpreter) - 让 LLM 在本地跑代码的自然语言接口。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenInterpreter%2Fopen-interpreter&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Manus AI](https://manus.im/) - 🇨🇳 🆕 通用自主 Agent，云本地混合，研究 / 编程 / 复杂任务。
- [Genspark](https://www.genspark.ai/) - 🆕 mixture-of-agents 全能工作 Agent，能打电话。
- [Beam AI](https://beam.ai/) - 🆕 自学习桌面 Agent。
- [Microsoft Copilot Studio Computer-Using Agents](https://techcommunity.microsoft.com/blog/copilot-studio-blog/computer-using-agents-in-microsoft-copilot-studio-are-now-generally-available/4519427) - 🆕 **2026 年 5 月 13 日 GA**。在 Copilot Studio 内构建可通过 UI 直接操控网站和桌面应用的 Agent —— 微软对 Claude Computer Use 的第一方回应，现已在 Microsoft 365 / Power Platform 部署中正式开放。
- [Perplexity Personal Computer](https://www.perplexity.ai/hub/products/computer-for-windows) - 🆕 **2026 年 6 月（Windows）**。把 Perplexity 的多模型 Agent 编排器（自动路由 19+ 个 AI 模型）带到 Windows；统一连接本地文件、原生应用与 Web。基于 4 月 16 日 Mac 版的延伸，同步迭代 Computex 2026 发布的本地/云端混合推理编排能力。
- [ChatGPT Workspace Agents](https://venturebeat.com/orchestration/openai-unveils-workspace-agents-a-successor-to-custom-gpts-for-enterprises-that-can-plug-directly-into-slack-salesforce-and-more) - 🆕 **研究预览 2026-04-22，2026-05-06 走积分计费，2026-05-07 支持 EKM**。OpenAI 为企业推出的 Custom GPTs 后继 —— 云端 Agent，能访问文件、执行代码、原生接 Slack / Google Drive / Salesforce，可调度周期任务；Business / Enterprise / Edu / Teachers 可用，底层走 Codex。

---

## 🌐 浏览器与 Web Agent

*真实浏览器中工作的 Agent —— 导航、点击、抓取、跨页流程。*

- [Browser Use](https://github.com/browser-use/browser-use) - 2026 年开源浏览器 Agent 事实标准。105K star。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowser-use%2Fbrowser-use&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Stagehand](https://github.com/browserbase/stagehand) - Browserbase 出品的"浏览器 Agent SDK"：类型化 `act / extract / observe`，跑在 Playwright 上。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowserbase%2Fstagehand&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Steel Browser](https://github.com/steel-dev/steel-browser) - 🆕 AI Agent 专用开源浏览器 API：自带 session 持久化 + 代理轮换。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsteel-dev%2Fsteel-browser&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Skyvern](https://github.com/Skyvern-AI/skyvern) - 用 LLM + 视觉自动化网页流程。AGPL-3.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSkyvern-AI%2Fskyvern&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentQL](https://github.com/tinyfish-io/agentql) - 查询语言 + Playwright 集成。动态 / 杂乱页面健壮。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftinyfish-io%2Fagentql&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hyperbrowser MCP](https://github.com/hyperbrowserai/mcp) - 🆕 托管无头浏览器 + 标准 MCP 工具接入 Claude / GPT / LangChain。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhyperbrowserai%2Fmcp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) - 🆕 微软官方 Playwright MCP server。生产级即插即用。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fplaywright-mcp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MultiOn](https://theagi.company/) - 📦 托管浏览器 Agent，原生 Reasoning + Memory；multion.ai 现跳转至 AGI, Inc.（theagi.company）。闭源。
- [Browserbase](https://www.browserbase.com/) - AI Agent 专用浏览器云：隐身、持久化、验证码、可观测性。
- [BrowserOS](https://www.browseros.com/) - 🆕 首个内置 AI Agent 的开源浏览器——隐私优先的 Chrome 替代。自然语言任务自动化无需写代码；本地优先设计，对标 Perplexity Comet 与 Arc 的 AI 能力。
- [Vercel Agent Browser](https://github.com/vercel-labs/agent-browser) - 🆕 面向 AI Agent 的无头浏览器自动化 CLI。2026 年 6 月版本新增 Core Web Vitals 的 `vitals` 命令（LCP/CLS/TTFB/FCP）、SPA 导航的 `pushstate`、进程外插件系统、MCP server 模式，以及托管环境用的 `@agent-browser/sandbox`。Apache-2.0，37K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvercel-labs%2Fagent-browser&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Google ADK — 浏览器与 A2A 集成](https://github.com/google/adk-python) - Google Agent Development Kit（v1.33，2026-05；v2.0 处于 beta）—— 多 Agent 组合、MCP 工具、A2A 协议集成。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle%2Fadk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [WebBrain](https://webbrain.one) - 🆕 **2026 年 7 月**。开源 MIT 浏览器扩展（Chrome + Firefox），用本地或云端大模型自动化 Web 任务。"Ask 模式" 只读摘要和提取；"Act 模式" 可点击按钮、填写表单、导航网页。本地优先设计——使用 llama.cpp / Ollama 时数据不离开设备。
- [Muse Spark 1.1（Web Agent）](https://artificialanalysis.ai/models/muse-spark) - 🆕 💰 **2026-07-09**。Meta Superintelligence Labs 首个付费 Agent 模型，经 Meta Model API 公开预览提供 —— WebArena-Verified 得分 69.0（落后于领先的 Claude Opus 4.8 的 71.2）。
- [Firecrawl v2](https://github.com/firecrawl/firecrawl) - 🆕 **v2.11.0，2026-06**。Agent 化网页抓取平台的大版本更新：JavaScript 渲染改进、实时抓取 webhook、批量 URL 处理。150K+ stars。AGPL-3.0（SDK 为 MIT）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ffirecrawl%2Ffirecrawl&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome) - 🆕 Anthropic 的浏览器 Agent Chrome 扩展 —— Claude 可跨标签页导航、填表并执行操作。⚠️ 2026 年 7 月研究显示存在恶意扩展 prompt 注入风险；使用前请审查权限。
- [Perplexity Comet](https://www.perplexity.ai/comet) - Perplexity 的 Agent 化 AI 浏览器，内置 Comet Assistant（后台 Agent）；2025 年 10 月起提供免费层；Perplexity 于 2026 年 6 月为 Comet 融资 $200M。

---

## 🗣️ 语音与多模态 Agent

- [AgentLine](https://agentline.cloud/) - 🆕 ⚠️ **Unverified.** 面向 AI Agent 的电话基础设施 —— 申请号码、外呼/接听、实时转录为 JSON 推到 webhook。定位为 Twilio 在 Agent 语音管线场景下的更轻替代；提交者自称 30+ 付费用户，暂无第三方采用证据。
- [ElevenLabs](https://elevenlabs.io/) - AI 语音合成 + 对话 Agent。
- [Vapi](https://github.com/VapiAI/server-sdk-python) - 语音 AI Agent 平台。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FVapiAI%2Fserver-sdk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Retell AI](https://www.retellai.com/) - 生产级对话语音 AI。
- [Hermes](https://buildwithhermes.com/) - 🆕 ⚠️ **未经验证（Founders Beta）**。面向代理商的白标语音 Agent 平台：Agent 管理、原生 CRM、呼入/呼出活动编排、按客户用量计费，$149/月起。暂无第三方采用数据。
- [Bland AI](https://www.bland.ai/) - 企业级 AI 电话平台。
- [LiveKit Agents](https://github.com/livekit/agents) - 实时多模态 Agent（语音 + 视频 + 数据）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flivekit%2Fagents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Pipecat](https://github.com/pipecat-ai/pipecat) - 开源语音多模态对话框架。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fpipecat-ai%2Fpipecat&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vocode](https://github.com/vocodedev/vocode-core) - 💤 **Stale**（最后版本 2024-06）。构建语音 LLM Agent 的开源库。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvocodedev%2Fvocode-core&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Bolna](https://github.com/bolna-ai/bolna) - 端到端开源语音 AI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbolna-ai%2Fbolna&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cartesia](https://www.cartesia.ai/) - 🆕 实时低延迟语音 AI。
- [Meta Voice AI](https://ai.meta.com/) - 🆕 收购 PlayHT/Play.ai 后的 Meta 语音技术。原 Play.ai 平台 2025-12-31 关停。
- [Sesame](https://www.sesame.com/) - 🆕 情绪感知 + 自然对话的语音 AI 伙伴。
- [OpenYabby](https://github.com/OpenYabby/OpenYabby) - 🆕 开源 macOS 语音驱动多 Agent 编排器 — Realtime API + CLI 子进程 + 多通道协调。主 Agent 规划任务并委派给子 Agent 进行评审和 QA。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenYabby%2FOpenYabby&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ElevenAgents](https://elevenlabs.io/agents) - 🆕 ElevenLabs 全栈语音 Agent 平台（2026 年 4-5 月更新）：支持 MCP、多模态消息、会话主题发现、知识库检索、工具调用前的语音控制。首个获 AIUC-1 认证的语音 Agent 平台。
- [Cartesia Line](https://cartesia.ai/blog/introducing-line-for-voice-agents) - 代码优先语音 Agent 平台（2025 年 8 月上线），基于 Cartesia 的 Sonic TTS + Ink STT，支持后台推理与本地化部署选项；首音延迟约 40-90ms。
- [Deepgram Voice Agent API](https://deepgram.com/product/voice-agent-api) - 🆕 单一端点打包 STT（Nova-3）+ LLM 路由 + TTS（Aura-2）+ Flux 会话式 STT，支持通话中 10 种语言切换。
- [OpenAI Realtime API (GPT-Realtime-2)](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/) - 🆕 **2026 年 5 月 7 日**。GPT-5 级推理能力的语音版，支持并行工具调用，128K 上下文；与 GPT-Realtime-Translate、GPT-Realtime-Whisper 同发。2026-07-06 更新至 gpt-realtime-2.1 / 2.1-mini（字母数字识别更好、抗噪更强、延迟更低）。
- [Dograh](https://github.com/dograh-hq/dograh) - 🆕 开源、可自托管的语音 AI 平台——Vapi / Retell 的开源替代。On-prem 部署，可在 Speech-to-Speech 或 LLM/STT/TTS 之间 BYOK；可视化工作流构建器，原生 MCP，电话支持。BSD-2-Clause，4K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdograh-hq%2Fdograh&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hume TADA](https://github.com/HumeAI/tada) - 🆕 **2026 年 3 月**。Hume AI 首个开源 TTS——Text Audio Dual Alignment：文本与音频在同一条 1:1 同步 token 流中生成；零内容幻觉、RTF 约 0.09、TADA-1B/3B-ML（9+ 种语言）、可在手机运行；支撑下一代 EVI 语音 Agent。MIT 代码，Llama 3.2 许可权重。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHumeAI%2Ftada&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Grok Voice Agent Builder](https://x.ai/news/grok-voice-agent-builder) - 🆕 **2026-07-01**。xAI 基于 Grok Voice 的无代码生产级语音 Agent 平台 —— 免费号码的电话接入、知识集合、工具/MCP 连接器、护栏、80+ 音色以及约 2 分钟的声音克隆；beta 期 $0.05/分钟。

---

## 📱 个人 AI Agent

- [OpenClaw](https://github.com/openclaw/openclaw) - 🆕 多渠道、本地运行的个人 AI Agent 平台。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenclaw%2Fopenclaw&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Rabbit R1](https://www.rabbit.tech/) - 大动作模型驱动的硬件 AI 助理。
- [Limitless](https://www.limitless.ai/) - 📦 **被 Meta 收购（2025 年末）**；吊坠硬件停售。基于你所见、所说、所听的个性化 AI（前 Rewind）；团队并入 Meta 的 AI 可穿戴业务。
- [Open Interpreter](https://github.com/OpenInterpreter/open-interpreter) - 自然语言计算机接口。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenInterpreter%2Fopen-interpreter&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [01 Light](https://github.com/OpenInterpreter/01) - 💤 **Stale**（2024-11 起无更新）。开源语音电脑接口。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenInterpreter%2F01&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Leon](https://github.com/leon-ai/leon) - 自托管开源个人助理。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fleon-ai%2Fleon&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Khoj](https://github.com/khoj-ai/khoj) - 你的笔记 / 文档 / 图片的"第二大脑"AI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fkhoj-ai%2Fkhoj&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Humane AI Pin](https://humane.com/) - ⚠️ **2025-02-28 已停产**（被 HP 收购，设备已关闭）。原为无屏幕环境计算的可穿戴 AI 设备。
- [Arahi AI](https://arahi.ai/) - 🆕 个人生产力 + 业务自动化助理。
- [Lindy AI](https://www.lindy.ai/) - 🆕 邮件 / 日历 / 工作流的无代码 Agent。
- [MuleRun](https://mulerun.com/) - 🆕 周期任务的常驻 Agent。
- [Gemini Intelligence](https://blog.google/products-and-platforms/platforms/android/gemini-intelligence/) - 🆕 **2026 年 5 月 12 日（Android Show: I/O Edition）**。主动式 Agent AI 能力贯穿 Googlebooks 笔电、Wear OS、Android Auto、Android XR，首发于最新 Samsung Galaxy + Pixel。可基于购物清单自动生成购物车、预订单车课程，以及通过 Rambler STT 移除口头禅。
- [Gemini Spark](https://gemini.google/overview/agent/spark/) - 🆕 **I/O 2026（2026 年 5 月 19 日）**。Google 在 Gemini 应用中的 24/7 自主 Agent —— 主动运行多步流程，集成 Gmail/Workspace；2026-07-01 扩展推出原生 Mac 应用。
- [QwenPaw](https://github.com/agentscope-ai/QwenPaw) - 🆕 🇨🇳 **2026 年 5 月由 CoPaw 改名**。Qwen / AgentScope 生态下可自托管的个人助手。本地优先记忆、热加载 skills、多 Agent 协作、多通道（钉钉 / 飞书 / 微信 / Discord / Telegram），自带工具守卫和 skill 扫描器。Apache-2.0。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentscope-ai%2FQwenPaw&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AI Growth Agents for Marketers](https://github.com/thaolst/ai-growth-agents-for-marketers) - 🆕 ⚠️ **未经验证**（早期项目）。基于东南亚真实金融科技营销活动构建的增长营销 prompt 与 Python Agent。覆盖 campaign brief、MEU 规划与多 Agent 工作流的 A/B 测试分析。Agent Skills 格式 —— 可通过 `npx skills add` 安装。越南语 + 英语双语。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fthaolst%2Fai-growth-agents-for-marketers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsoft Scout](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) - 🆕 **Build 2026（2026 年 6 月 2 日）**。微软基于 OpenClaw 框架打造的常驻个人 Agent —— 跨云 / 桌面 / Web 主动工作，连接 Teams / Outlook / OneDrive / SharePoint。每个 Agent 在独立 Entra 身份下运行，连续策略合规检查 + 审计链。Microsoft Frontier 计划私测；需 Intune 策略 + GitHub Copilot 许可证。
- [Lenovo Qira / Motorola Qira](https://news.lenovo.com/pressroom/press-releases/lenovo-unveils-lenovo-and-motorola-qira/) - 🆕 **CES 2026（2026 年 1 月 6 日）**。联想与摩托罗拉联合打造的"个人环境智能系统"——上下文感知 AI 跨 PC / 手机 / 平板 / 可穿戴设备协同。Q1 2026 在部分联想设备上线，随后扩展至 Motorola 手机；OEM 主导的环境 AI 首发。
- [Yao Agents](https://yaoagents.com) - 🆕 🇨🇳 **2026 年 5 月**。本地优先的 AI 执行平台：30+ 领域专家（编程、写作、数据分析、PM）与自主 Robot 工作者。5 阶段流水线（灵感→目标→任务→验证→交付）、Docker 沙箱隔离、多平台消息（微信/飞书/钉钉/Telegram/Discord）、MCP 支持、BYOK 模型配置与跨设备编排 Tai Link。开源引擎：[YaoApp/yao](https://github.com/YaoApp/yao)。
- [AgentArk](https://github.com/agentark-ai/AgentArk) - 🆕 🧪 **2026-06**（v0.0.1，beta —— 不适合生产环境）。以本地控制与安全为先的个人 AI OS；通过 GEPA 优化器运行时实现自我学习。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentark-ai%2FAgentArk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [nanobot](https://github.com/HKUDS/nanobot) - 🆕 超轻量开源个人 AI Agent（41K+ stars）。2026 年 4 月版本（v0.1.5.x）新增线程级会话、自动压缩记忆、Dream 记忆巩固、DeepSeek-V4 支持与 Windows 支持。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2Fnanobot&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 📱 手机 Agent

*操控 Android / iOS 的 GUI Agent —— 桌面 Computer Use 之后的下一前沿。*

- [Mobile-Agent](https://github.com/X-PLUG/MobileAgent) - 🇨🇳 阿里多模态手机控制 Agent 家族（v1 → v3 + Mobile-Agent-E / V）。Android 基准 SOTA。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FX-PLUG%2FMobileAgent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AppAgent](https://github.com/TencentQQGYLab/AppAgent) - 💤 腾讯多模态智能体，通过点 / 滑操作 App。早期影响力实现；由 AppAgentX（2025-03）接续。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTencentQQGYLab%2FAppAgent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Apple Intelligence](https://www.apple.com/apple-intelligence/) - iOS / iPadOS / macOS 端侧 Agent 层。App Intents + 屏幕感知动作。
- [Samsung Galaxy AI / Bixby 2.0](https://www.samsung.com/global/galaxy/galaxy-ai/) - Galaxy S26 端侧 Gauss。
- [Google Gemini for Android](https://gemini.google/) - 全面替换 Google Assistant，包括系统意图与 Workspace。
- [Magma](https://microsoft.github.io/Magma/) - 微软研究多模态 Agent 基座，统一 UI / 机器人 / 物理动作。
- [mobile-use](https://github.com/minitap-ai/mobile-use) - 🆕 开源框架（Apache-2.0，2.5K+ stars），让 AI Agent 像真人一样使用真实 Android / iOS 应用 —— UI 感知导航、自然语言控制。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fminitap-ai%2Fmobile-use&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [agent-device (Callstack)](https://github.com/callstack/agent-device) - 🆕 **2026 年 2 月**。轻量、节省 token 的 CLI，用于自动化 iOS / Android 真机和模拟器。命令模型面向 AI Agent 与 CI 场景设计。MIT，2.6K+ stars。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcallstack%2Fagent-device&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🏢 企业级 Agent 平台

- [Salesforce Agentforce 360](https://www.salesforce.com/agentforce/what-is-new/) - CRM 自主 Agent —— 销售 / 客服 / 营销。**Spring 2026 版**带来 Agentforce Builder（对话式 Agent 编辑）、Agent Script（确定性行为控制）、Agentforce Voice（接入 Amazon Connect / Five9 / Genesys / NiCE / Vonage + SIP）、基于新 Data 360 的 Intelligent Context。124 国客户报告约 85% 客户咨询自动化解决。
- [Microsoft Copilot Studio](https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio) - 企业 Copilot 与 Agent 构建。
- [Gemini Enterprise Agent Platform](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform) - 🆕 **2026-04-22**（Google Cloud Next '26）。Vertex AI 进化为统一企业 Agent 中心。Gemini 3.1 Pro/Flash + Lyria 3 + 第三方模型（Claude Opus / Sonnet / Haiku）。
- [Google Vertex AI Agent Builder](https://cloud.google.com/products/agent-builder) - **2026 年 4 月更名** —— Vertex AI 的 Agent 构建能力现已并入 Gemini Enterprise Agent Platform（见上）：Agent Studio、Model Garden、Google Antigravity 编排。
- [Amazon Bedrock Agents](https://aws.amazon.com/bedrock/agents/) - 多步任务 Agent。
- [ServiceNow AI Agents](https://www.servicenow.com/products/ai-agents.html) - 🆕 ITSM Agent + AI Control Tower。
- [ServiceNow Action Fabric (MCP Server)](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-opens-its-full-system-of-action-to-every-AI-Agent-in-the-enterprise/default.aspx) - 🆕 **2026-05-05**。ServiceNow 通过 GA 的 MCP Server 把其 AI 平台向任意 AI Agent（Claude、Copilot、自定义）开放，随每个 Now Assist 与 AI Native SKU 自带。每次调用都走 AI Control Tower，具备身份验证、权限范围、审计链；自带 OAuth、用量计费、角色级工具包。Anthropic（Claude Cowork）为首个设计合作伙伴。
- [IBM watsonx Orchestrate](https://www.ibm.com/products/watsonx-orchestrate) - 跨企业应用的 AI 助理平台。
- [Oracle AI Agents](https://www.oracle.com/artificial-intelligence/) - 🆕 与 Oracle Fusion Cloud ERP 集成。
- [Moveworks](https://www.moveworks.com/) - 跨系统企业 copilot。已被 ServiceNow 收购（2025-12-15 交割）。
- [UiPath Agentic Automation](https://www.uipath.com/) - 🆕 在 RPA 之上叠加 Agent 推理。
- [AgentX](https://www.agentx.so/) - 🆕 即插即用的企业 Agent 自动化。
- [Sistava](https://sistava.com) - ⚠️ 面向销售、营销、客服、招聘与运营的「按需 AI 员工」—— Agent 带持久记忆、直接在你的工具内工作；$19/月起。
- [Amazon Bedrock AgentCore Payments](https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-bedrock-agentcore-payments-preview/) - 🆕 **2026-05-07（预览）**。AgentCore Agent 的托管支付 —— 通过 Coinbase（CDP 钱包、x402 Bazaar）与 Stripe（Privy 钱包）集成，自主为 API、MCP 服务器、Web 内容及其他 Agent 付费；支持消费限额与交易可观测性，覆盖四个 AWS 区域。
- [OutSystems Agentic Systems Platform](https://www.outsystems.com/) - 🆕 **2026 年 6 月**。低代码巨头将其平台定位为“AI 原生”的 agentic 开发环境。提供开放式 AI 治理、自带模型、多 Agent 编排以及企业级合规，直接对标 Copilot Studio 与 Agentforce。
- [Sema4.ai](https://sema4.ai/) - 🆕 Python 优先 + 内置治理的企业 Agent 平台。
- [SAP Business AI Platform + Autonomous Suite](https://news.sap.com/2026/05/sap-sapphire-sap-unveils-autonomous-enterprise/) - 🆕 **SAP Sapphire 2026（2026-05-12）**。SAP 发布「自主企业」：以 SAP Business AI Platform 为统一 AI 底座；SAP Autonomous Suite 为财务、供应链、采购、HR 与 CX 的既有应用加入 Agent；Joule Studio 用于构建企业 Agent 与 Agentic 工作流；Joule Work UX；以及七个行业 AI 解决方案。Claude 是驱动 Joule Agent 的基础模型之一。
- [Microsoft Agent 365 + Microsoft 365 E7](https://techcommunity.microsoft.com/blog/agent-365-blog/microsoft-365-e7--agent365-from-where-you-are-to-enterprise-ai-at-scale/4519969) - 🆕 **2026-05-01 GA**，5 月持续补充。以身份为中心的 AI Agent 控制面：独立 $15/用户/月，或 $99/用户/月随新推的 Microsoft 365 E7 "Frontier" 套套；5 月补丁加上了 AWS Bedrock + Google Cloud 注册表同步、Intune / Defender 预览策略，以及 Agent 专用 SASE。
- [OpenAI Guaranteed Capacity（算力年发）](https://openai.com/business/guaranteed-capacity/) - 🆕 **2026-05-19**。面向企业 AI 产品 / Agent / Workflow 的长期算力预订产品（可选 1/2/3 年期，期限越长折扣越高）—— 面向 GPT-5.5 级 Agent 的企业部署降低成本 / 产能不确定性，OpenAI 对 Anthropic Priority Tier 的产品化回应。
- [Bristol Myers Squibb ↔ Claude Enterprise](https://news.bms.com/news/corporate-financial/2026/Bristol-Myers-Squibb-Announces-Strategic-Agreement-with-Anthropic-to-Position-Claude-Enterprise-as-the-Shared-Intelligence-Platform-Across-Its-Global-Operations/default.aspx) - 🆕 **2026-05-20**。BMS 将 Claude Enterprise 作为 30,000+ 员工的共享智能平台，嵌入药物发现 / 开发 / 交付的全链路。全球前 5 大药企中首个全公司级 Claude 部署。
- [Kore.ai Artemis Agent Platform](https://www.kore.ai/news/kore-ai-launches-artemis-the-new-generation-of-the-kore-ai-agent-platform-for-building-governing-and-optimizing-enterprise-ai) - 🆕 **2026 年 5 月 21 日（Azure 上线）**。AI 原生的企业级 Agent 平台，核心是新的 YAML 风格 **Agent Blueprint Language (ABL)**，用于声明式多 Agent 工作流。Kore.ai 对 Copilot Studio 与 Agentforce 的结构性挑战。
- [FPT Flezi Foundry™](https://www.morningstar.com/news/business-wire/20260521235556/fpt-launches-flezi-foundry-advancing-ai-augmented-delivery-for-global-enterprises) - 🆕 **2026 年 5 月 21 日**。AI 增强的交付平台，两种受治理的 Service-as-a-Software 模式——**Agentic Development Lifecycle (ADLC)** 覆盖完整 SDLC 的 Agent 团队，以及 **Agentic Managed Services (AMS)** 把事故处置 Agent 叠加在现有 ITOps 之上。
- [Databricks Genie One](https://www.databricks.com/blog/introducing-genie-one-genie-ontology-and-genie-agents) - 🆕 **2026-06-16（Data + AI Summit）**。Databricks 推出的智能体「数据同事」，跨结构化与非结构化数据自动编排工作，依托全新 **Genie Ontology**（覆盖全组织的知识图谱）并由 Unity Catalog 治理；配套 Genie Agents，官方内部测试一次命中率 84.5%。
- [ZenseAI.AgentMesh（Zensar）](https://www.prnewswire.com/news-releases/zensar-technologies-launches-zenseaiagentmesh-to-accelerate-enterprise-ai-adoption-at-scale-302805437.html) - 🆕 **2026-06-19**。Zensar 推出的企业级智能体 AI 平台，定位「面向 Agentic AI 的通用企业操作系统」，统一发现、构建、部署与治理自主 Agent；内置 80+ 预制行业与跨职能 Agent，宣称 6–8 周即可从试点走向生产。
- [Meta Business Agent](https://about.fb.com/news/2026/06/meta-business-agent/) - 🆕 **2026-06-03（全球上线）**。Meta 面向 WhatsApp、Instagram 与 Messenger 推出的商业 AI Agent——回答咨询、推荐目录商品、预约到访、甄别销售线索并完成成交，必要时移交人工。已有 100 万+ 商家使用；**Meta Business Agent Platform** 让企业自定义 Agent 并接入 Shopify / Zendesk / Shopee —— 当前免费开通，付费订阅档即将推出。
- [Snyk Evo Agentic Development Security (ADS)](https://snyk.io/news/snyk-launches-evo-agentic-development-security/) - 🆕 **2026 年 6 月**。专为自主 AI 编程 Agent 打造的安全与治理平台：实时治理 Agent 使用什么、做了什么以及生成的代码。
- [Cognizant Neuro AI + ServiceNow AI Agent](https://news.cognizant.com/2026-06-18-Cognizant-expands-cross-platform-agentic-AI-with-new-ServiceNow-AI-Agent-interoperability) - 🆕 **2026 年 6 月**。跨平台企业编排：让 ServiceNow Agent 原生运行在 Cognizant 的 Multi-Agent Accelerator 中。
- [Talkdesk Agent Builder](https://www.cmswire.com/contact-center/customer-contact-week-2026-capturing-the-ai-announcements-in-contact-center-technology/) - 🆕 **2026 年 6 月**。低代码构建器，让业务人员在数小时内（而非数周）将生产级 AI Agent 部署到联络中心。
- [HelloTwin Digital Authority](https://siliconangle.com/2026/06/24/hellotwin-launches-digital-authority-bring-governed-ai-agents-enterprise/) - 🆕 **2026 年 6 月**。作为单一可审计事实来源的 AI 数字分身，以清晰边界治理 Agentic 工作流。

---

## 📊 Agent 评估与可观测性

- [LangSmith](https://www.langchain.com/langsmith) - LangChain 的官方调试 / 评测 / 监控平台。
- [LangSmith SDK](https://github.com/langchain-ai/langsmith-sdk) - 客户端 SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangsmith-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Langfuse](https://github.com/langfuse/langfuse) - 开源 LLM 工程平台：可观测性 + 评测 + prompt 管理。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangfuse%2Flangfuse&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Helicone](https://github.com/Helicone/helicone) - 开源 LLM 可观测性。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHelicone%2Fhelicone&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Arize Phoenix](https://github.com/Arize-ai/phoenix) - 开源 LLM 可观测性 + 评测。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FArize-ai%2Fphoenix&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Arena（前 LMArena / LMSYS Chatbot Arena）](https://arena.ai/) - 众包人类偏好投票 AI 基准；榜单现覆盖 LLM、图像生成与代码模型。LMSYS → LMArena（2025）→ Arena（2026）。
- [Patronus AI](https://www.patronus.ai/) - 💰 LLM 评测/红队公司，现定位为构建数字世界模型与 Agent 训练仿真基础设施的前沿研究实验室（$50M B 轮）；研究成果包括 Lynx、FinanceBench 与 GLIDER。
- [DeepEval](https://github.com/confident-ai/deepeval) - Pytest 风格的 LLM 评测框架，14+ 内置指标。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fconfident-ai%2Fdeepeval&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agenta](https://github.com/agenta-ai/agenta) - 🆕 一体化开源 LLMOps。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagenta-ai%2Fagenta&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AutoEvals](https://github.com/braintrustdata/autoevals) - 独立的最佳实践评测器库（事实性 / JSON 有效性 / 语义相似度等）。Braintrust 出品。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbraintrustdata%2Fautoevals&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [BenchClaw](https://github.com/Agnuxo1/benchclaw) - ⚠️ **Unverified**。自称多维度 Agent 评测。8 个 awesome 列表 7 个拒收，2 star 单维护者。**仅作可见性收录**。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAgnuxo1%2Fbenchclaw&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [PromptEden](https://www.prompteden.com) - ⚠️ **Unverified**。商业 SaaS：监控 ChatGPT / Claude / Gemini / Perplexity / Copilot / Grok 如何描述你的品牌。同款 PR 同日投了 10 个 awesome 列表。**仅作可见性收录**。
- [AgentBench](https://github.com/THUDM/AgentBench) - 评估 LLM 作为 Agent 表现的多维 benchmark。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTHUDM%2FAgentBench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Braintrust](https://www.braintrust.dev/) - 企业级 AI 产品构建栈——评估、提示词 playground、日志一体化。SDK：[braintrust-sdk-javascript](https://github.com/braintrustdata/braintrust-sdk-javascript) 与 braintrust-sdk-python（由 braintrust-sdk 拆分/更名）。
- [OpenLLMetry](https://github.com/traceloop/openllmetry) - 基于 OpenTelemetry 的开源 LLM 可观测性方案。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftraceloop%2Fopenllmetry&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Weights & Biases Weave](https://github.com/wandb/weave) - 用于开发、评估与监控 AI 应用的工具包。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fwandb%2Fweave&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SWE-bench](https://github.com/SWE-bench/SWE-bench) - 评估 LLM 在真实软件工程问题上能力的 benchmark。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSWE-bench%2FSWE-bench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Terminal-Bench](https://www.tbench.ai/) - 🆕 面向终端编码 Agent 的评估 benchmark。由 Harbor Framework 维护。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fharbor-framework%2Fterminal-bench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Harbor](https://github.com/harbor-framework/harbor) - 🆕 大规模评估与优化 Agent 和 LLM 的框架 —— 在数千个云沙箱中运行 Terminal-Bench 2.x 及自定义基准、生成 RL rollout；Stanford × Laude Institute 合作项目。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fharbor-framework%2Fharbor&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Laminar](https://github.com/lmnr-ai/lmnr) - 🆕 专为长跑 AI Agent 设计的开源可观测性平台（Apache-2.0，YC S24）。OpenTelemetry 原生，transcript view、Signals、SQL 跨 traces 查询、浏览器 Agent 会话回放。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flmnr-ai%2Flmnr&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangSmith Engine](https://www.langchain.com/blog/interrupt-2026-overview) - 🆕 **2026 年 5 月（Interrupt 2026）**。LangSmith 的自主失败诊断层——将生产失败聚类为优先级问题，结合 traces 与代码定位根因，给出可供人类审阅的修复建议。与新发的 SmithDB（Rust + DataFusion 支持的 Agent 观测数据库）配套。
- [AgentSight](https://github.com/eunomia-bpf/AgentSight) - 零插桩 eBPF Agent 可观测性——无需修改 Agent 代码，在 syscall 层捕获进程、文件、网络全栈行为轨迹，实现完整行为分析。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Feunomia-bpf%2FAgentSight&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Prismix](https://prismix.dev) - 实时监控 77+ AI 服务（OpenAI、Anthropic、Cursor 等）的状态，提供状态徽章与 API；AI 新闻聚合器（来自 71+ 信息源）；MCP 服务器目录（收录 80+ 服务器）。免费，无需注册。
- [Ceros (by Beyond Identity)](https://www.prnewswire.com/news-releases/ceros-launches-providing-unified-identity-observability-and-governance-for-every-ai-agent-and-workflow-302800721.html) - 🆕 **2026-06-16**。Agentic AI 信任层：统一身份、可观测性与治理 —— 发现/清点、运行时策略执行、审计链。（与同名互动内容公司无关。）
- [Zoom Agent Performance Suite](https://news.zoom.com/introducing-agent-architect-and-agent-performance-suite-for-zoom-virtual-agent/) - 🆕 **2026-06**。用于在面向客户的场景中测试、验证并优化自主 Agent 表现的专用套件。
- [AgentOps](https://github.com/AgentOps-AI/agentops) - 🆕 Agent 监控、合规与测试工具包，带会话回放；提供 MCP server，对任何接入 MCP 的 Agent 实现零配置可观测；5K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAgentOps-AI%2Fagentops&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenTelemetry GenAI Semantic Conventions](https://github.com/open-telemetry/semantic-conventions-genai) - 面向 GenAI 客户端、Agent、工具调用与 MCP 的标准化 span / 指标 / 事件 —— 在任意 OTel 后端（Arize、Langfuse、Helicone、Jaeger 等）实现厂商中立的追踪。已从核心 semconv 仓库移入专门的 GenAI 仓库。
- [Tracecat](https://github.com/TracecatHQ/tracecat) - 🆕 开源安全自动化平台，为 SOC 工作流捕获完整 Agent trace —— 把 AI Agent 接入检测、富化与响应流水线。AGPL-3.0（含企业版例外条款）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTracecatHQ%2Ftracecat&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🔬 AI 研究工具

- [Hugging Face Transformers](https://github.com/huggingface/transformers) - 模型与训练工具的事实标准库。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhuggingface%2Ftransformers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [vLLM](https://github.com/vllm-project/vllm) - 高吞吐 LLM 推理与服务。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvllm-project%2Fvllm&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SGLang](https://github.com/sgl-project/sglang) - 高性能 LLM 推理引擎。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsgl-project%2Fsglang&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [llama.cpp](https://github.com/ggml-org/llama.cpp) - C/C++ 高性能 LLM 推理。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fggml-org%2Fllama.cpp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Ollama](https://github.com/ollama/ollama) - 本地跑 LLM 的最简单方法。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Follama%2Follama&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LM Studio](https://lmstudio.ai/) - 桌面本地 LLM GUI，多提供商。
- [OpenRouter](https://openrouter.ai/) - 一个 API 统一访问 70+ 提供商的 400+ AI 模型。
- [Unsloth](https://github.com/unslothai/unsloth) - 2 倍运行、节省 70% 显存的 LLM 微调。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Funslothai%2Funsloth&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MLX](https://github.com/ml-explore/mlx) - Apple Silicon 上的机器学习框架。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fml-explore%2Fmlx&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Weights & Biases](https://wandb.ai/) - ML 实验跟踪 + 模型管理。
- [Label Studio](https://github.com/HumanSignal/label-studio) - 多类型数据标注平台。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHumanSignal%2Flabel-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [DSPy](https://github.com/stanfordnlp/dspy) - 编程代替 prompt 工程。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstanfordnlp%2Fdspy&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hugging Face](https://huggingface.co/) - AI 社区平台——汇集模型、数据集与 Spaces，是 ML 研究的事实标准枢纽。
- [SmithDB](https://www.langchain.com/blog/interrupt-2026-overview) - 🆕 **2026 年 5 月（Interrupt 2026）**。LangChain 自研的 Agent 观测数据库。Rust 写在 Apache DataFusion + Vortex 之上，带对象存储后端——为 Agent trace 的容量与访问模式量身设计。

---

## 📚 学习资源

### 论文

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) - 定义 ReAct 范式的里程碑论文。
- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) - LLM 学会使用外部工具。
- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) - 使用 LLM 创建可信人类行为 Agent。
- [LLM-based Autonomous Agents Survey](https://arxiv.org/abs/2308.11432) - 中人大 LLM 自主 Agent 综述。
- [The Rise and Potential of LLM Based Agents](https://arxiv.org/abs/2309.07864) - LLM Agent 发展与潜力。

### 课程与教程

- [LangChain Academy](https://academy.langchain.com/) - LangChain 官方课程（包含 LangGraph）。
- [DeepLearning.AI Short Courses](https://www.deeplearning.ai/short-courses/) - 涵盖主要框架 / 协议的 AI 短课。
- [LLM Agents MOOC (Berkeley)](https://llmagents-learning.org/) - UC Berkeley 的 LLM Agent 课程（根站点跳转到最新一期）。
- [Microsoft Agent Framework Docs](https://learn.microsoft.com/en-us/agent-framework/) - 🆕 微软统一 Agent 框架官方文档。
- [Hugging Face Agents Course](https://github.com/huggingface/agents-course) - 5 单元免费课程（smolagents / LangGraph / Llama-Index）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhuggingface%2Fagents-course&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook) - 官方调工具、Computer Use、Agent 模式、Claude Code 示例本。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fanthropics%2Fanthropic-cookbook&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Google Gemini Cookbook](https://github.com/google-gemini/cookbook) - Gemini API 示例：grounding / function calling / 多模态 / live audio。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle-gemini%2Fcookbook&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LLM Course (Maxime Labonne)](https://github.com/mlabonne/llm-course) - LLM 从入门到微调的完整课程 + Colab。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmlabonne%2Fllm-course&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Anthropic Courses](https://github.com/anthropics/courses) - Anthropic 官方 prompt engineering / 评测 / 工具调用课程。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fanthropics%2Fcourses&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### 精选列表

- [awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) - 💤 **Stale**（2025-02 起无更新）。E2B 出品。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fe2b-dev%2Fawesome-ai-agents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [awesome-llm-agents](https://github.com/kaushikb11/awesome-llm-agents) - LLM Agent 资源。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fkaushikb11%2Fawesome-llm-agents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - 🆕 MCP server 实现精选。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fpunkpeye%2Fawesome-mcp-servers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [awesome-ai-agent-papers (VoltAgent)](https://github.com/VoltAgent/awesome-ai-agent-papers) - 🆕 2026 年 AI Agent 研究论文精选——覆盖 Agent 工程、记忆、评测、工作流、自主系统。每周从 arXiv 更新。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FVoltAgent%2Fawesome-ai-agent-papers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [awesome-cli-coding-agents](https://github.com/bradAGI/awesome-cli-coding-agents) - 🆕 终端原生 AI 编程 Agent + 编排 harness 精选——开源工具（Pi / OpenCode / Aider / Goose）、平台 Agent（Claude Code / Codex / Gemini CLI）、并行运行器、自主循环。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FbradAGI%2Fawesome-cli-coding-agents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agent Hospital](https://arxiv.org/abs/2405.02957) - 模拟可演化医疗 Agent 的医院环境。
- [DeepLearning.AI — AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) - 用 LangGraph 构建 Agent 的短课程。
- [DeepLearning.AI — Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/) - 多 Agent 系统构建课程。
- [DeepLearning.AI — A2A Protocol](https://www.deeplearning.ai/short-courses/a2a-the-agent2agent-protocol/) - 🆕 关于 Google Agent-to-Agent 协议的免费课程。
- [Hugging Face — Building AI Agents](https://huggingface.co/learn/agents-course/) - 用开源工具构建 AI Agent 的开放课程。

---

## 🇨🇳 中国 AI 生态

*中国大陆团队主导或主要面向中文市场的重要项目。列出是因为中国技术栈越来越形成独立生态，有自己的框架、模型、开发者文化。*

*中国友出品的基础模型（Qwen / DeepSeek / GLM / Doubao / Kimi / Hunyuan / ERNIE）已直接列在 [🧠 基础大模型](#-基础大模型-2026) 下。*

### Agent 平台与框架

- [Dify](https://github.com/langgenius/dify) - 开源 LLM 应用开发平台 + 可视化 Agent 构建。中文技术圈主流低代码 Agent 画布。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flanggenius%2Fdify&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LobeHub](https://github.com/lobehub/lobehub) - Agent 管理平台（前 Lobe Chat）—— 把 Agent 组织为 7×24 运转，支持对你的 AI 团队进行"招聘/排班/汇报"。最高 star 的 TypeScript AI 项目之一（80K+ stars）。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flobehub%2Flobehub&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Coze Loop](https://github.com/coze-dev/coze-loop) - 🆕 字节 Coze 团队开源的 Agent 优化平台。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-loop&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentScope](https://github.com/modelscope/agentscope) - 阿里 ModelScope 多 Agent 框架 + 可视化调试 + 分布式执行。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelscope%2Fagentscope&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Bisheng](https://github.com/dataelement/bisheng) - 开源企业级 LLM DevOps：工作流 / RAG / Agent / 微调 / 评测。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdataelement%2Fbisheng&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) - SOP 角色多 Agent（PM / 架构师 / 工程师）。现由 FoundationAgents 组织维护。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FFoundationAgents%2FMetaGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### RAG / 知识

- [FastGPT](https://github.com/labring/FastGPT) - 知识库优先的 LLM 平台：数据摄入 / RAG / 可视化工作流。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flabring%2FFastGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [QAnything](https://github.com/netease-youdao/QAnything) - 💤 网易有道出品，针对任意本地文档的问答引擎。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fnetease-youdao%2FQAnything&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAGFlow](https://github.com/infiniflow/ragflow) - 深度文档理解的 RAG 引擎 —— 扫描 PDF 、表格、图表处理能力强。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Finfiniflow%2Fragflow&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LightRAG](https://github.com/HKUDS/LightRAG) - 港大 HKUDS 轻量图式 RAG。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2FLightRAG&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### 个人与生产力

- [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) - 开源 Notion 替代品 + AI 工作区。AGPL-3.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAppFlowy-IO%2FAppFlowy&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Manus AI](https://manus.im/) - Butterfly Effect 出品的通用自主 Agent（中国团队创立，后迁往新加坡）。**已被 Meta 以约 $2B 收购（2025-12-30 宣布）** —— manus.im 现显示 "Manus is now part of Meta"。
- [Coze (扣子)](https://www.coze.cn/) - 字节无代码 Agent 构建。国内面向消费者；国际版为 coze.com。
- [Qwen App（千问）](https://www.qwen.ai/) - 阿里大众消费者 Agent（由通义千问更名），集成在淘宝 / 钉钉 / 夸克。
- [Doubao Agents](https://www.doubao.com/) - 字节豆包模型上的主力消费者助手。

### 开发者工具

- [Trae](https://www.trae.ai/) - 字节跳动的 AI IDE 与 "10x AI 编程工程师" —— 中国对 Cursor 最高调的挑战者。
- [CoderPlan](https://coderplan.ai/) - 面向中国开发者的统一 LLM API 网关（Claude / OpenAI / Gemini，一行配置支持 Claude Code），按量付费，支持支付宝 & 微信支付。
- [Cherry Studio](https://github.com/CherryHQ/cherry-studio) - 中文开发者圈装机量最高的开源桌面 LLM 客户端，多提供商 + 知识库。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FCherryHQ%2Fcherry-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ScienceOne 100 / 磐石100](https://english.cas.cn/newsroom/cas-in-media/202604/t20260429_1158251.shtml) - 🆕 中科院科研推理 Agent 系统，50+ 中科院研究所、100+ 科研场景、带 2000+ 研究工具。
- [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code) - 🆕 **2026 年 6 月 6 日**。Moonshot AI 的终端编程 Agent（MIT，TypeScript）——内置 coder / explore / plan 子 Agent 在隔离上下文里跑，`/mcp-config` 对话式 MCP 配置。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FMoonshotAI%2Fkimi-code&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Qwen Code](https://github.com/QwenLM/qwen-code) - 阿里 Qwen 团队的开源终端编程 Agent —— Agent 团队、自动记忆、IDE 集成、多提供商（OpenAI / Anthropic / Gemini / Qwen）。26K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FQwenLM%2Fqwen-code&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Coze Studio](https://github.com/coze-dev/coze-studio) - 🆕 字节 Coze.com 的开源对照版——一体化可视化 Agent 构建器，自带调试与部署工具。Apache-2.0，20K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 📝 横向对比表

*2026 年最常见的“该选哪个？”决策矩阵。*

### 🏗️ Agent 框架（开源向）

| 框架 | 语言 | 多 Agent | 状态 / 图 | 流式 | License | 适合场景 |
|------|------|---------|------|------|---------|---------|
| [LangGraph](https://github.com/langchain-ai/langgraph) | Python / JS | ✅ 原生 | ✅ 一等公民 | ✅ | MIT | 生产级有状态工作流 |
| [CrewAI](https://github.com/crewAIInc/crewAI) | Python | ✅ 角色扮演 | ⚠️ 任务图 | ✅ | MIT | 角色化 Agent 团队 |
| [AutoGen / Microsoft Agent Framework](https://github.com/microsoft/autogen) | Python / .NET | ✅ 对话 | ⚠️ Group Chat | ✅ | CC-BY-4.0 / MIT | 企业多 Agent 对话 |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | Python | ✅ handoff | ❌ | ✅ | MIT | OpenAI 原生生产 |
| [Mastra](https://github.com/mastra-ai/mastra) | TypeScript | ✅ | ✅ workflows | ✅ | Elastic-2.0 | TypeScript 优先 |
| [Google ADK](https://github.com/google/adk-python) | Python / Java | ✅ 层级 | ⚠️ | ✅ | Apache-2.0 | Gemini + Vertex AI |
| [DSPy](https://github.com/stanfordnlp/dspy) | Python | ⚠️ 模块 | ⚠️ 编程式 | ✅ | MIT | 程序化 prompt 优化 |
| [Agno (ex-Phidata)](https://github.com/agno-agi/agno) | Python | ✅ teams | ❌ | ✅ | MPL-2.0 | 多模态 Agent + 记忆 |

### 🧪 沙箱（运行 Agent 生成代码）

| 沙箱 | 部署 | 冷启动 | 语言 | 持久化 | License | 适合场景 |
|------|------|---------|------|---------|---------|---------|
| [E2B](https://github.com/e2b-dev/E2B) | 云（托管） | ~150ms | Python / Node / shell | per-session | Apache-2.0 | OpenAI Agents SDK / 生产 |
| [Daytona](https://github.com/daytonaio/daytona) | 云 / 自托管 | ~500ms | 多语言 | 持久化 workspace | AGPL-3.0 | 长任务开发 |
| [Modal](https://modal.com/) | 云（托管） | ~200ms | Python | function-scoped | 闭源 | GPU + Serverless Agent |
| [Microsandbox](https://github.com/superradcompany/microsandbox) | 本地 microVM | ~100ms | 多语言 | per-session | Apache-2.0 | 隐私优先的本地开发 |
| [SandboxFusion](https://github.com/bytedance/SandboxFusion) | 自托管 | ~300ms | 20+ 语言 | 临时 | Apache-2.0 | 评测 / 基准流水线 |

### 🌐 浏览器 Agent 栈

| 栈 | 思路 | 部署 | 优势 | License |
|------|------|------|------|---------|
| [Browser Use](https://github.com/browser-use/browser-use) | Vision + DOM（Playwright） | 自托管 | 92K star，社区第一 | MIT |
| [Stagehand](https://github.com/browserbase/stagehand) | 类型化 act / extract / observe | Browserbase / 自托管 | 强类型 + 结构化输出 | MIT |
| [Steel Browser](https://github.com/steel-dev/steel-browser) | 无头 Chrome API | 自托管 / 云 | session + proxy + captcha | Apache-2.0 |
| [Skyvern](https://github.com/Skyvern-AI/skyvern) | Vision 优先 | 自托管 | 抗动态页面强 | AGPL-3.0 |
| [AgentQL](https://github.com/tinyfish-io/agentql) | 查询语言 | SDK + 自托管 | 语义化 selector | MIT |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | MCP 原生 | 自托管 | MCP 客户端即插即用 | Apache-2.0 |

### 📊 评估与可观测性

| 工具 | 自托管 | OpenTelemetry | 评测套件 | Prompt 管理 | License |
|------|---------|----------|---------|------------|---------|
| [Langfuse](https://github.com/langfuse/langfuse) | ✅ | ✅ | ✅ | ✅ | MIT |
| [Helicone](https://github.com/Helicone/helicone) | ✅ | ✅ | ⚠️ 基础 | ✅ | Apache-2.0 |
| [Arize Phoenix](https://github.com/Arize-ai/phoenix) | ✅ | ✅ | ✅ | ⚠️ | Elastic-2.0 |
| [LangSmith](https://www.langchain.com/langsmith) | ❌（仅云） | ✅ | ✅ | ✅ | 闭源 |
| [Braintrust](https://www.braintrust.dev/) | ❌（仅云） | ✅ | ✅ | ✅ | 闭源 |
| [DeepEval](https://github.com/confident-ai/deepeval) | ✅（库） | ⚠️ 依赖 Confident | ✅ | ❌ | Apache-2.0 |
| [Agenta](https://github.com/agenta-ai/agenta) | ✅ | ✅ | ✅ | ✅ | Apache-2.0 |
| [OpenLLMetry](https://github.com/traceloop/openllmetry) | ✅（插件） | ✅ 原生 | ❌ | ❌ | Apache-2.0 |

### 💻 编程 Agent —— 头部选择

| 工具 | 形态 | 开源 | 免费层 | SWE-bench | 适合场景 |
|------|------|------|--------|-----------|----------|
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | CLI / IDE | ❌ | ⚠️ Pro | 80.9% | 长期工程 |
| [Codex CLI](https://github.com/openai/codex) | CLI | ✅ | ✅ | n/a（Terminal-Bench 77.3%） | OpenAI 原生 shell |
| [Cursor](https://www.cursor.com/) | IDE | ❌ | ✅（限制） | n/a | 配对编程体验 |
| [Cline](https://github.com/cline/cline) | VS Code 扩展 | ✅ | ✅（BYO） | n/a | 开源 IDE 替代 |
| [Aider](https://github.com/Aider-AI/aider) | CLI | ✅ | ✅（BYO） | Polyglot 强 | Git-aware 重构 |
| [Devin 3.0](https://www.cognition.ai/) | 云 | ❌ | ❌ | 领先 | 完全托管长任务 |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | 自托管 | ✅ | ✅ | 有竞争力 | 自部署 SWE Agent |

*表格于 2026-07-17 验证。数据变化请提 PR。*

---

### 💰 基础大模型 — API 价格与上下文窗口

*价格单位：USD/百万 token。数据：2026-07-17。*

| 模型 | 厂商 | 上下文窗口 | 输入 $/1M | 输出 $/1M | 适用场景 |
|-------|----------|---------------|-----------|------------|----------|
| GPT-5.6 Sol | OpenAI | 1M | $5.00 | $30.00 | 前沿推理旗舰 |
| GPT-5.6 Terra | OpenAI | 1M | $2.50 | $15.00 | 成本敏感的生产负载 |
| GPT-5.6 Luna | OpenAI | 1M | $1.00 | $6.00 | 大量、延迟敏感任务 |
| GPT-4o | OpenAI | 128K | $2.50 | $10.00 | 广泛工具调用、视觉、广泛生态 |
| GPT-4o-mini | OpenAI | 128K | $0.15 | $0.60 | 大规模简单任务 |
| Claude Sonnet 5 | Anthropic | 1M | $2.00（引导价） | $10.00（引导价） | 默认 Agent 主力（2026-08-31 后 $3/$15） |
| Claude Opus 4.8 | Anthropic | 1M | $5.00 | $25.00 | 最难推理任务 |
| Claude Fable 5 | Anthropic | 1M | $10.00 | $50.00 | Mythos 级前沿任务 |
| Claude Haiku 4.5 | Anthropic | 1M | $1.00 | $5.00 | Anthropic 生态快速任务 |
| Gemini 3.1 Pro | Google | 1M | $2.00 | $12.00 | 旗舰推理、多模态 |
| Gemini 2.5 Flash | Google | 1M | $0.30 | $2.50 | 性价比高的多模态 |
| Gemini 2.5 Pro | Google | 1M | $1.25 | $10.00 | 超长文本、多模态 |
| Gemini 2.5 Flash-Lite | Google | 1M | $0.10 | $0.40 | 极低成本大量请求 |
| DeepSeek V4-Flash | DeepSeek | 1M | $0.14 | $0.28 | 低成本编程推理 |
| Qwen3 235B A22B | 阿里巴巴 | 131K | ~$0.29 | ~$1.15 | 最强中文+编程 MoE |
| Kimi K2.6 | Moonshot AI | 262K | $0.95 | $4.00 | 中文+超长上下文 |
| Grok 4 | xAI | 256K | $3.00 | $15.00 | X/Twitter 生态、推理 |
| Grok 4.5 | xAI | 500K | $2.00 | $6.00 | 编程 + Agent 旗舰 |

*数据来源：Anthropic、OpenAI、Google、DeepSeek、阿里巴巴、Moonshot、xAI 官方定价页 —— 2026 年 7 月。*

---

### 💻 基础大模型 — 本地部署

*Q4_K_M 量化下的估算显存。速度因硬件而异。*

| 模型 | 参数量 | 最小显存（Q4） | 速度（tok/s） | 推荐量化 | 中文能力 | 适用场景 |
|-------|--------|--------------|----------------|-------------------|-----------------|----------|
| Qwen3.6-27B | 27B dense | ~17 GB | ~23（M5 Max） | Q4_K_M / FP8 | ⭐⭐⭐⭐⭐ | 编程、中文、Agent |
| Qwen3 235B A22B | 235B MoE | ~40 GB（激活） | ~15–20 | Q2_K / Q4_K_M | ⭐⭐⭐⭐⭐ | 本地最强质量 |
| Llama 3.3 70B | 70B dense | ~42 GB | ~12–18 | Q4_K_M | ⭐⭐☆☆☆ | 最强英文开源 |
| DeepSeek V3-671B | 671B MoE | ~40 GB（激活） | ~10–15 | Q2_K | ⭐⭐⭐⭐☆ | 开源编程冠军 |
| Gemma 4 27B | 27B dense | ~17 GB | ~20–25 | Q4_K_M | ⭐⭐⭐☆☆ | 多语言推理 Apache-2.0 |
| Phi-4 14B | 14B dense | ~9 GB | ~35–45 | Q4_K_M | ⭐⭐☆☆☆ | 8–16GB 显存编程首选 |
| Mistral Small 4 24B | 24B dense | ~14 GB | ~25–30 | Q4_K_M | ⭐⭐⭐☆☆ | 多语言、函数调用 |

---

### 🧠 Agent 记忆系统

| 系统 | 存储 | 检索 | 本地 | 自托管 | 时序支持 | 许可证 | 适合场景 |
|--------|---------|-----------|-------|-----------|----------|---------|----------|
| [Mem0](https://github.com/mem0ai/mem0) | 向量+图谱 | 语义 | ✅ | ✅ | ✅ | Apache-2.0 | 任意 LLM 应用即插即用 |
| [Basic Memory](https://github.com/basicmachines-co/basic-memory) | Markdown 文件 | 关键词+嵌入 | ✅ | ✅ | ⚠️ | MIT | 可读，兼容 Obsidian |
| [Graphiti](https://github.com/getzep/graphiti) | 时序知识图谱 | 图谱遍历 | ✅ | ✅ | ⭐ 原生 | Apache-2.0 | 时间感知的 Agent 记忆 |
| [Zep](https://github.com/getzep/zep) | 向量+摘要 | 语义 | ✅ | ✅ | ✅ | Apache-2.0 | 生产级对话 Agent 记忆 |
| [Memary](https://github.com/kingjulio8238/Memary) | 知识图谱 | 图谱+语义 | ✅ | ✅ | ⚠️ | MIT | 开源 Agent 记忆层 |
| [Letta (MemGPT)](https://github.com/cpacker/MemGPT) | 分层存储 | 分页检索 | ✅ | ✅ | ✅ | Apache-2.0 | 无限上下文幻觉的长期记忆 |

---

### 🎙️ 语音与音频模型

| 模型/服务 | STT | TTS | 实时 | 本地 | 延迟 | 语言 | 许可证 |
|----------------|-----|-----|---------|-------|---------|-----------|--------|
| ElevenLabs v3 | ❌ | ⭐⭐⭐⭐⭐ | ✅ | ❌ | ~200ms | 70+ | 闭源 |
| Whisper v3（本地） | ⭐⭐⭐⭐★ | ❌ | ❌ | ✅ | ~1s | 99 | MIT |
| Deepgram Nova-3 | ⭐⭐⭐⭐⭐ | ✅ | ✅ | ❌ | <100ms | 45+ | 闭源 |
| Gemini Live API | ✅ | ✅ | ⭐ 原生 | ❌ | <300ms | 30+ | 闭源 |
| OpenAI Realtime | ✅ | ✅ | ⭐ 原生 | ❌ | ~300ms | 57 | 闭源 |
| MiniMax TTS | ❌ | ⭐⭐⭐⭐☆ | ✅ | ❌ | ~200ms | 20+ | 闭源 |
| Kokoro | ❌ | ⭐⭐⭐⭐☆ | ❌ | ✅ | ~100ms | 8 | Apache-2.0 |
| Voxtral | ⭐⭐⭐⭐☆ | ❌ | ❌ | ✅ | 批量 | 20+ | Apache-2.0 |

---

### 🎨 图片生成模型

| 模型 | 最大分辨率 | API/本地 | 真实感 | 适用场景 | 大致价格 |
|-------|---------------|-------------|-------------|----------|------------------|
| DALL-E 3 | 1024×1024 | API | 高 | 指令遵循 | $0.04/张（标准） |
| gpt-image-2 | 2048×2048 | API | 非常高 | API 工作流、4K | $0.04–$0.17/张 |
| Flux 2 Pro | 2K+ | API | ⭐高 | 写实、快速 | ~$0.05/张 |
| Midjourney V8.1 | 2K+ | 仅网页 | 艺术风格最强 | 艺术创作 | $10–$120/月 |
| Stable Diffusion 3.5 | 2K | 本地+API | 良好 | 开源、自托管 | 开源权重（Stability AI Community License） |
| Ideogram 3 | 2K | API+网页 | 良好 | 图内文字最强 | 免费增值 |

---

### 🎥 视频生成模型

| 模型 | 最大时长 | 分辨率 | API/本地 | 适用场景 | 状态 |
|-------|-----------|-----------|-------------|----------|------------------|
| Veo 3.1 | 2分钟 | 4K | API（Vertex） | 最高保真度 | GA（Google） |
| Kling VIDEO 3.0 | 3分钟 | 1080p | API+网页 | 电影风格领先 | GA（快手） |
| Runway Gen-4 | 10s/片段 | 1080p | API+网页 | 精确运动控制 | GA |
| Pika 2.0 | 10s | 1080p | 网页 | 创意/社交媒体 | GA |
| Seedance 2.0 | 60s | 2K | API | 快速、高性价比 | GA（字节） |
| Hailuo 02 | 60s | 1080p | 网页+API | 平滑动作 | GA（MiniMax） |
| ~~Sora~~ | ❌ | ❌ | ❌ | — | **2026.4 已废弃** |

---

### 🔍 RAG 框架

| 框架 | 语言 | 向量库 | 混合检索 | 流式 | 许可证 | 适合场景 |
|-----------|---------|-----------|--------------|-----------|---------|----------|
| LlamaIndex | Python | 任意 | ✅ | ✅ | MIT | 生产级 RAG、文档流水线 |
| Haystack | Python | 任意 | ✅ | ✅ | Apache-2.0 | 搜索密集的 RAG |
| LangChain LCEL | Python/JS | 任意 | ✅ | ✅ | MIT | 适应性强、大生态 |
| RAGFlow | Python | 内置 | ✅ | ✅ | Apache-2.0 | 深度文档解析、OCR |
| Cognee | Python | 向量+图谱 | ✅ | ⚠️ | Apache-2.0 | 知识图谱+RAG 混合 |
| txtai | Python | 内置 | ✅ | ❌ | Apache-2.0 | 轻量嵌入优先 |
| Verba | Python | Weaviate | ⚠️ | ❌ | BSD-3 | 📦 已归档 — Weaviate 原生 RAG 聊天机器人 |

---

### 🗄️ 向量数据库

| 数据库 | 自托管 | 云 | 规模 | 混合检索 | 许可证 | 适合场景 |
|----------|-----------|-------|-------|--------------|---------|----------|
| Qdrant | ✅ | ✅ | 大规模 | ✅ | Apache-2.0 | 最全面开源向量库 |
| Weaviate | ✅ | ✅ | 大规模 | ✅ | BSD-3 | 多模态、GraphQL |
| Pinecone | ❌ | ✅ | 大规模 | ✅ | 闭源 | 托管、最易上手 |
| Chroma | ✅ | ⚠️ | 中等 | ❌ | Apache-2.0 | 快速原型、Python 原生 |
| Milvus | ✅ | ✅ | 十亿级 | ✅ | Apache-2.0 | 生产级十亿规模 |
| pgvector | ✅ | ✅ | 中等 | ⚠️ | PostgreSQL | 现有 Postgres 扩展 |
| FAISS | ✅ | ❌ | 大规模 | ❌ | MIT | 内存内 GPU 加速搜索 |

---

### 📱 个人 AI 助手（2026）

| 工具 | 开源 | 本地模型 | 记忆 | 多渠道 | 自托管 | 适合场景 |
|------|------------|-----------|--------|--------------|-----------|----------|
| [OpenClaw](https://github.com/openclaw/openclaw) | ✅ | ✅ | ✅ 原生 | ✅（TG/Discord/WA） | ✅ | 全能自托管个人 Agent |
| Khoj | ✅ | ✅ | ✅ | ⚠️ | ✅ | 研究、笔记、日历 |
| Jan.ai | ✅ | ✅ | ❌ | ❌ | ✅ | 离线 ChatGPT 替代品 |
| Claude.ai Pro | ❌ | ❌ | ✅ Projects | ❌ | ❌ | 最强推理+MCP工具 |
| Perplexity | ❌ | ❌ | ⚠️ | ❌ | ❌ | 搜索优先、带引用 |

---

### 🔌 MCP 服务器 — 主要集成

| MCP 服务器 | 类别 | 认证 | 安全审计 | 许可证 |
|-----------|----------|------|---------------|--------|
| GitHub MCP | 开发/代码 | OAuth | ✅（GitHub） | MIT |
| Playwright MCP | 浏览器 | 无（本地） | ⚠️ | Apache-2.0 |
| Filesystem MCP | 文件 | 无（本地） | ⚠️ 需沙箱 | MIT |
| Brave Search MCP | 搜索 | API密钥 | ❌ | MIT |
| Slack MCP | 通讯 | OAuth | ❌ | MIT |
| Notion MCP | 笔记 | OAuth | ❌ | MIT |
| PostgreSQL MCP | 数据库 | 连接串 | ⚠️ 建议只读 | MIT |
| Google Maps MCP | 地理 | API密钥 | ❌ | MIT |

*部署前建议用 **mcp-scan**（Invariant Labs）对任意 MCP 服务器进行安全扫描。*

---

### 🏢 企业级 Agent 平台

| 平台 | 开源 | MCP | A2A | 自托管 | 合规 | 适合场景 |
|---------|------------|------------|------------|-----------|-----------|----------|
| Microsoft Agent Framework | ⚠️ | ✅ | ✅ | ⚠️（Azure） | SOC2, ISO | Azure 原生企业 |
| Salesforce Agentforce | ❌ | ⚠️ | ❌ | ❌ | SOC2, GDPR | Salesforce CRM 组织 |
| SAP Joule | ❌ | ❌ | ❌ | ⚠️ | SOC2 | SAP ERP 环境 |
| Google Gemini Enterprise | ❌ | ✅ | ✅ | ❌ | SOC2, FedRAMP | Google Workspace |
| IBM watsonx | ⚠️ | ✅ | ⚠️ | ✅（本地） | FedRAMP, HIPAA | 合规/本地企业 |
| Dify Enterprise | ✅（CE） | ✅ | ✅ | ✅ | SOC2（云） | 多模型低代码 |

---

### 📏 嵌入模型

*MTEB = 大规模文本嵌入基准排行最高分（英文，2026-05 近似）。*

| 模型 | 维度 | 上下文 | 本地 | API | 语言 | 许可证 | MTEB ≈ |
|-------|------|---------|-------|-----|-----------|---------|--------|
| OpenAI text-embedding-3-large | 3072 | 8K | ❌ | ✅ | 多语言 | 闭源 | ~64 |
| Cohere embed-v4 | 1024 | 512 | ❌ | ✅ | 多语言 | 闭源 | ~66 |
| [Gemini gemini-embedding-2](https://ai.google.dev/gemini-api/docs/embeddings) | 3072 | 8K | ❌ | ✅ | 多语言 | 闭源 | — |
| BGE-M3 | 1024 | 8K | ✅ | ❌ | 多语言 | MIT | ~65 |
| Jina-embeddings-v3 | 1024 | 8K | ✅ | ✅ | 多语言 | CC-BY-NC | ~65 |
| Nomic-embed-text-v2 | 768 | 8K | ✅ | ✅ | 多语言 | Apache-2.0 | ~62 |
| Voyage-3 | 1024 | 32K | ❌ | ✅ | 多语言 | 闭源 | ~67 |

---

### 🛡️ Agent 安全工具

| 工具 | MCP 扫描 | 提示词注入防御 | 审计日志 | 自托管 | 许可证 |
|------|---------|------------------------|-----------|-----------|--------|
| mcp-scan | ⭐ 原生 | ✅ | ❌ | ✅ | MIT |
| Lakera Guard | ❌ | ⭐⭐⭐⭐⭐ | ✅ | ❌ | 闭源 |
| Zenity | ✅ | ✅ | ✅ | ❌ | 闭源 |
| Prompt Armor | ❌ | ⭐⭐⭐⭐☆ | ✅ | ❌ | 闭源 |
| Azure AI Content Safety | ❌ | ✅ | ✅ | ❌（Azure） | 闭源 |
| Rebuff | ❌ | ⭐⭐⭐⭐☆ | ❌ | ✅ | MIT |

---

### 🖥️ 电脑使用与桌面 Agent

| 工具 | 系统 | 视觉 | 本地 | API | 开源 | 适合场景 |
|------|----|----|-------|-----|------------|----------|
| Claude Desktop Intelligence | Mac/Linux | ✅ | ❌ | ✅ | ❌ | 最全面屏幕 Agent |
| UFO（微软） | Windows | ✅ | ✅ | 可选 | ✅ | Windows 原生自动化 |
| OSWorld | 多平台 | ✅ | ✅ | 可选 | ✅ | 跨平台基准+Agent |
| Screenpipe | Mac/Linux | ✅ | ✅ | ❌ | ✅ | 屏幕记忆、隐私优先 |

---

### 🤖 Physical AI 平台

| 平台 | 类型 | 开源 | SDK | 仿真 | 适合场景 |
|---------|------|------------|-----|-----------|----------|
| NVIDIA Isaac GR00T N1.5 | 人形机基础模型 | ⚠️（权重） | ✅ | ✅ Isaac Sim | 通用人形机基础模型 |
| ROS 2 Jazzy | 机器人操作系统 | ✅ | ✅ | ✅ Gazebo | 标准机器人中间件 |
| Gemini Robotics | 灵巧操作 | ❌ | ⚠️ | ✅ | 视觉+语言+灵巧操作 |
| Unitree SDK2 | 四足/人形 | ✅ | ✅ | ⚠️ | Go2, H1, G1 开发 |
| Boston Dynamics API | 四足 | ❌ | ✅ | ❌ | Spot 工业部署 |
| Genesis Sim | 仿真平台 | ✅ | ✅ | ⭐ 原生 | 超高速物理仿真 |

---

### 🇨🇳 中文大模型横向对比

| 模型 | 厂商 | 上下文 | 中文能力≈ | 编程 | 开源权重 | 输入 $/1M |
|-------|----------|---------|---------------|--------|------------|----------|
| Qwen3 235B A22B | 阿里 | 131K | 顶级 | ⭐⭐⭐⭐⭐ | ✅ Apache-2.0 | ~$0.29 |
| DeepSeek V3.2 | DeepSeek | 128K | 非常高 | ⭐⭐⭐⭐⭐ | ✅ MIT | $0.14 |
| Kimi K2.6 | Moonshot AI | 262K | 高 | ⭐⭐⭐⭐☆ | ❌ | ~$0.95 |
| GLM-5.2 | 智谱 AI | 1M | 高 | ⭐⭐⭐⭐☆ | ✅ MIT | ~$0.50 |
| 混元 Pro | 腾讯 | 256K | 高 | ⭐⭐⭐⭐☆ | ❌ | ~$0.45 |
| 豆包 Pro 256K | 字节 | 256K | 高 | ⭐⭐⭐☆☆ | ❌ | ~$0.80 |
| ERNIE 5 | 百度 | 128K | 高 | ⭐⭐⭐☆☆ | ❌ | ~$0.70 |

---

### 📦 Agent 框架 — TypeScript / JavaScript

| 框架 | 多 Agent | 流式 | MCP | A2A | stars ≈ | 许可证 |
|-----------|-----------|----------|-----|-----|-------|---------|
| Mastra | ✅ | ✅ | ✅ | ✅ | ~12K | Elastic-2.0 |
| Vercel AI SDK | ⚠️ | ✅ | ✅ | ❌ | ~12K | Apache-2.0 |
| LangChain.js | ✅ | ✅ | ✅ | ❌ | ~14K | MIT |
| Genkit | ✅ | ✅ | ✅ | ❌ | ~3K | Apache-2.0 |
| OpenAI Agents SDK (Node) | ✅ | ✅ | ✅ | ❌ | ~2K | MIT |
| Flowise | ✅ | ✅ | ✅ | ❌ | ~35K | Apache-2.0 |

---

### 📊 元对比 — 编排/框架/IDE 分类

| 类型 | 典型工具 | 适合对象 | 抽象级别 | 灵活性 |
|---------|--------------|----------|--------------------|-------------|
| 编排平台 | Dify, n8n, Flowise | 非工程师、快速上线 | 极高 | 中低 |
| Agent 框架 | LangGraph, CrewAI, Mastra | 工程师自定义 | 中等 | 高 |
| Agent IDE | Claude Code, Cursor, Cline | 开发者配对 | 低 | 非常高 |
| 低代码构建器 | Voiceflow, Botpress | 业务/产品团队 | 极高 | 低 |
| AI 原生平台 | Vertex AI Agent Builder | 企业托管基础设施 | 高 | 中等 |

---

### 📱 移动端 AI 框架

| 框架 | iOS | Android | 本地模型 | 端上推理 | 许可证 | 适合场景 |
|-----------|-----|---------|-----------|--------------------|---------|-----------| 
| MLX | ✅ | ❌ | ✅ | ⭐ Apple Silicon | MIT | Apple 原生快速 LLM |
| llama.cpp（移动） | ✅ | ✅ | ✅ | ✅ | MIT | 全平台通用本地 LLM |
| MediaPipe | ✅ | ✅ | ✅ | ✅ | Apache-2.0 | 端上 ML（视觉/NLP） |
| Core ML | ✅ | ❌ | ✅ | ✅（ANE） | Apple SDK | iOS/macOS 原生推理 |
| Google AI Edge | ✅ | ✅ | ✅ | ✅ | Apache-2.0 | Gemma Nano 端上 |
| Qualcomm AI Hub | ❌ | ✅ | ✅ | ✅（骁龙 NPU） | SDK | 骁龙芯片优化部署 |

*所有对比表数据来源：2026-07-17。数据变化请提 PR。*

---

---

## 🗺️ 场景指南 — 我应该用什么…

*50+ 场景与工具对应。每周更新。*

---

### 🏗️ 构建类：编程 Agent

**创业公司要一个最低成本高质量的编程 Agent**
→ **Claude Code**（CLI）+ **E2B** 沙箱 + **Langfuse** 可观测。SWE-bench 80.9%。中等使用量 ~$200/月。

**企业级编程 Agent（有安全控制）**
- **GitHub Copilot Enterprise** — GitHub 已深度集成、IP 赔偿、SSO/SAML。→ 已在 GitHub Enterprise 上
- **Cursor Business** — 隐私模式、代码不离开企业。→ 需要 IDE 优先体验
- **Devin 3.0** — 自动重规划、全自动。→ 完全托管长任务

**要一个完全开源的编程 Agent（无厂商锁定）**
- **OpenHands** — MIT 许可，自部署、自带模型选择。
- **Cline**（VS Code 插件）— BYO 密钥，社区活跃。
- **Aider** — Git-aware CLI 重构。

**浏览器自动化 / 网页抓取 Agent**
- **Browser Use** — 92K stars，业界最大社区。
- **Stagehand** — 强类型 + 结构化输出。
- **Skyvern** — Vision 优先，抵抗动态页面。

**文档处理 / PDF 分析 Agent**
→ **LlamaIndex** + **Gemini 2.5 Pro**（2M 上下文）或 **Claude Opus 4.7** + **Unstructured.io**。

**客户服务 Agent**
- **Dify** — 无代码、内置 RAG、自托管。
- **LangGraph + Zendesk MCP** — 工程师主导的业务。
- **Salesforce Agentforce** — CRM 原生。

**深度研究 Agent**
→ **Perplexity Deep Research**（托管）或 **OpenHands + Tavily + Claude Opus 4.7**。

**数据分析 / BI Agent**
- **Julius AI** — 无需工程师，托管。
- **[AI for Database](https://aifordatabase.com)** — ⚠️ Unverified。用自然语言查 Postgres / MySQL / MongoDB / SQL Server / SQLite + Sheets，自动刷新仪表盘 + Slack/Webhook/邮件触发；SOC 2 + GDPR，支持自托管，Pro $19/月。→ 适合不会 SQL 的业务团队直连数据库。
- **LangChain + Pandas Agent** — 完全自定义。

**Computer Use / 桌面 Agent**
- **Claude Desktop Intelligence** — macOS/Linux 最全面。
- **UFO**（微软）— Windows 原生。
- **Screenpipe** — 本地隐私优先。

**语音 / 对话 Agent**
- **Gemini Live API** — <300ms 延迟。
- **OpenAI Realtime API（GPT-Realtime-2 / GPT-Live-1）** — 原生语音 + 工具调用。
- **LiveKit + Whisper + ElevenLabs v3** — 完全自托管。

**多 Agent 编排系统**
- **LangGraph** — Python 生产级有状态图式工作流。
- **Google ADK** — 层级 Agent + Gemini 生态。
- **Mastra** — TypeScript 优先。

**个人 AI 助手（自托管）**
→ **OpenClaw** — 多渠道、记忆、cron、MCP、全套自托管。

**个人 AI 助手（托管/开箱即用）**
- **Claude.ai Pro** — 最强推理+MCP工具。
- **Perplexity Pro** — 搜索为主。

**RAG 应用**
→ **LlamaIndex** + **Qdrant** + **Cohere embed-v4** + **BGE reranker**。

**金融分析 Agent**
→ **LangChain** + **yfinance MCP** + **Claude Sonnet 4.6** + 结构化输出验证。

**法律文档 Agent**
→ **Claude Opus 4.7**（1M 上下文）+ **LlamaIndex** + **pgvector**。必须保留人工审核。

**创意写作助手**
→ **Claude Opus 4.7**（最佳散文质量）或 **Gemini 2.5 Pro**（2M 上下文）。

**安全扫描 Agent**
→ **Semgrep** + **Claude Sonnet 4.6** + **mcp-scan**。

---

### 🧠 模型选择类

**需要最强模型做复杂推理**
- **Claude Opus 4.7** (/think xhigh) — $5/$25/1M。
- **Gemini 2.5 Pro** — 2M 上下文，$1.25/$10。
- **GPT-5.6 Terra** — 广泛工具调用生态，$2.50/$15。

**需要最快最便宜的模型（简单高频任务）**
- **Gemini 2.5 Flash-Lite** — $0.10/$0.40/1M。
- **DeepSeek V3.2** — $0.14/$0.28/1M，惊人的性价比。
- **GPT-5.6 Luna** — $1.00/$6.00/1M，GPT-5.6 最快档，OpenAI 工具生态广（GPT-4o-mini 仍是 $0.15/$0.60 的超低价旧选项）。

**需要最强中文能力**
- **Qwen3 235B A22B** — 中文评测居首。
- **Kimi K2.6** — 262K 上下文。
- **DeepSeek V3.2** — 开源权重中文编程。
- **GLM-5.2**（智谱 AI）— 1M 上下文，MIT 开源权重，中文优先。→ API 或本地

**需要本地/离线模型（16GB 显存）**
- **Qwen3.6-27B Q4_K_M** — ~17GB，最佳 16GB 首选。
- **Phi-4 14B** — ~9GB，编程首选。

**需要本地/离线模型（40GB+）**
- **Llama 3.3 70B Q4_K_M** — ~42GB，英文与编程强，Llama 3.3 Community License。
- **Qwen3 235B A22B Q2** — MoE 主力。

**需要最强编程能力**
→ **Claude Sonnet 4.6**（通过 Claude Code，SWE-bench 80.9%）。

**需要超长上下文 (500K+)**
- **Gemini 2.5 Pro** — 2M 上下文。
- **Kimi K2.6** — 262K。
- **Claude Opus 4.7** — 1M 上下文，窗口内质量最佳。

**需要开源权重模型（MIT/Apache）**
- **Llama 3.3 70B**（Llama 3.3 Community License）、**DeepSeek V3.2** (MIT)、**Qwen3 235B A22B** (Apache-2.0)。

---

### 🏗️ 基础设施类

**全本地运行（隐私优先，零云端）**
→ **Ollama** + **Open WebUI** + **Qdrant** + **Qwen3.6-27B**（16GB）/ **Llama 3.3 70B**（40GB+）。

**压缩 API 费用（每月 <$50）**
→ **DeepSeek V3.2** + **Gemini 2.5 Flash** + Anthropic Batch API 折扣。

**企业资源伸缩**
→ **Google Vertex AI** 或 **Azure OpenAI** + **LiteLLM** 路由网关。

**集群 / 受监控环境部署**
→ **Ollama + 开源权重** + **IBM watsonx** 或 **Azure Government**。

**避免厂商锁定**
→ **LiteLLM**（统一 API 路由）+ **LangGraph** + **BGE-M3 嵌入**。

---

### 📊 评估与监控类

**评估 Agent 输出质量** → **DeepEval** + **Langfuse**。

**调试 Agent 失败原因** → **Langfuse** trace + **Arize Phoenix** 根因分析。

**实时监控生产 Agent** → **Langfuse**（OpenTelemetry，自托管）或 **Helicone**。

**A/B 测试不同模型** → **Braintrust** 或 **LangSmith**。

**对自定义任务进行 benchmark** → DeepEval + 自己的黄金测试集（50 个示例起步）。

**评估 MCP 服务器安全** → **mcp-scan**（Invariant Labs）。

---

### 🌍 生态选择类

**OpenAI 生态** → OpenAI Agents SDK + GPT-4o + E2B + LangSmith。

**Anthropic 生态** → Claude Code + Claude Sonnet/Opus + MCP + Langfuse。

**Google 生态** → Google ADK + Gemini 2.5 Pro/Flash + Vertex AI。

**国内市场** → Qwen3 235B（DashScope）+ RAGFlow + Milvus + Langfuse。

**TypeScript 优先** → Mastra + Vercel AI SDK + Gemini 2.5 Flash + Qdrant。

**全开源栈** → Ollama + Llama 3.3 70B + LangGraph + Qdrant + Langfuse。

---

## 📋 技术栈食谱 — 经过验证的工具组合

| # | 配方名 | 技术栈 | 适合对象 |
|---|------------|-------|----------|
| 1 | **轻量编程 Agent** | Claude Code + E2B + Langfuse | 独立开发/创业，性价比最高 |
| 2 | **开源 SWE Agent** | OpenHands + Ollama + Qwen3.6-27B + Qdrant | 全本地，隐私优先 |
| 3 | **企业级 RAG** | LlamaIndex + Qdrant + Cohere embed-v4 + Langfuse + Claude Sonnet 4.6 | 内部文档生产问答 |
| 4 | **语音助手流水线** | LiveKit + Whisper + Claude Sonnet 4.6 + ElevenLabs v3 | 定制品牌语音 AI |
| 5 | **浏览器自动化** | Browser Use + Stagehand + Claude Sonnet 4.6 + Langfuse | 可靠网页抓取 |
| 6 | **本地隐私栈** | Ollama + Qwen3.6-27B + Open WebUI + Qdrant + n8n | 零云端、离线部署 |
| 7 | **TypeScript Agent** | Mastra + Vercel AI SDK + Gemini 2.5 Flash + Qdrant | TS 优先生产 SaaS |
| 8 | **国内市场栈** | Qwen3 235B API + RAGFlow + Milvus + Langfuse | 国内部署，ICP 合规 |

---

## ⚠️ 反推荐 — 不应该用在哪里

| ❌ 不要用 | ❌ 用于 | ✅ 改用 | 原因 |
|------------|-----------|---------------|-----|
| LangChain v0.x | 新的生产 Agent | **LangGraph** | 旧版 chain 已废弃 |
| AutoGPT（旧） | 生产工作负载 | **OpenHands / LangGraph** | 体系过时，可靠性差 |
| GPT-3.5-Turbo | 复杂推理 | **Gemini 2.5 Flash / Claude Haiku 4.5** | 已超龄，同价有更好选择 |
| Pinecone Starter | 自托管/成本敏感 | **Qdrant / pgvector** | 2025 年已取消免费档、开源更便宜 |
| LLM 直接做实时股票交易 | 金融执行 | 确定性规则引擎 | LLM 会幻觉数字，对实盘交易破坏性极大 |
| ChatGPT Plus | 生产 API 工作流 | **OpenAI API** 直接调用 | 无 SLA、无配额控制 |
| Hugging Face 免费推理 | 生产负载 | **Modal / 自托管 Ollama** | 免费层极限，冷启动 >30s |
| Agent 无人工审核 | 医疗/法律决策 | 任意模型 + 必须人工审核 | 无模型可靠性足够高 |
| Midjourney | 程序化/API 图片生成 | **gpt-image-2 / Flux 2 Pro API** | Midjourney 无公开 API |
| Sora | 视频生成 | **Kling VIDEO 3.0 / Veo 3.1** | Sora 2026.4 已停运 |
| 不带 reranker 的向量检索 | 高精度 RAG | 向量 DB + **BGE reranker** | 纯向量召回率只有 ~70% |

---

## 🌟 2026 年值得关注的 Agent 项目

*塑造 2026 年 AI Agent 格局的里程碑与事件。*

- [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol/servers) - 成为 Agent 工具互联互通的事实标准。已损赠给 Linux Foundation。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Fservers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [A2A Protocol](https://github.com/a2aproject/A2A) - Agent 间协议（起源于 Google，现属 Linux Foundation），让跨框架 Agent 协作，150+ 合作伙伴；v1.0 于 2026 年 5 月发布。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fa2aproject%2FA2A&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - SWE-bench 80.9%，成为 2026 终端编程 Agent 首选。
- [Kiro](https://kiro.dev/) - 🆕 AWS 发布的自主编程 Agent，可同时管理 10 个任务。
- [Devin 3.0](https://www.cognition.ai/) - 🆕 动态重规划、自愉合代码、遗留代码迁移。
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/) - 🆕 AutoGen + Semantic Kernel 合并。
- [OpenAI Codex CLI](https://github.com/openai/codex) - OpenAI 进入开源终端 Agent 赛道。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fcodex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Browser Use](https://github.com/browser-use/browser-use) - 让 AI Agent 自然使用网页的突破性项目。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowser-use%2Fbrowser-use&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude Computer Use](https://www.anthropic.com/) - 🆕 Claude "Desktop Intelligence"。
- [Manus AI](https://manus.im/) - 🇨🇳 通用自主 Agent，能处理研究 / 编程 / 复杂工作流；现已并入 Meta（2025 年 12 月宣布以约 $2B 收购）。
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) - 开源 SWE Agent 平台大量采用。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAll-Hands-AI%2FOpenHands&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Dify](https://github.com/langgenius/dify) - 🇨🇳 低代码 LLM Agent 平台走向主流。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flanggenius%2Fdify&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cline](https://github.com/cline/cline) - VS Code 自主编程 Agent。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcline%2Fcline&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Mem0](https://github.com/mem0ai/mem0) - Agent 架构中的记忆层必备。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmem0ai%2Fmem0&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Sora 停服](https://openai.com/) - 🆕 OpenAI 2026-04 关闭 Sora，战略转向企业 + 推理。
- [Kling VIDEO 3.0](https://kling.ai/) - 🇨🇳 🆕 快手出品，Sora 停服后的领先视频平台。
- [Cohere + Aleph Alpha 合并](https://siliconangle.com/2026/04/24/ai-startups-cohere-aleph-alpha-merge-600m-new-funding/) - 🆕 **2026-04-24**。东西合作 “主权 AI”，多伦多 + 德国双总部，$20B 估值 + $600M 资金。
- [ScienceOne 100 / 磐石100](https://english.cas.cn/newsroom/cas-in-media/202604/t20260429_1158251.shtml) - 🇨🇳 🆕 **2026-04-28~29**。中科院专业科研 AI 系统。
- [Google 投资 Anthropic $40B](https://aibusiness.com/generative-ai/google-could-invest-another-40-billion-anthropic) - 🆕 **2026-04**。$10B 初始 + 最高 $30B，含 5GW 算力。
- [OpenAI Deployment Company (DeployCo)](https://openai.com/index/openai-launches-the-deployment-company/) - 🆕 **2026-05-11**。OpenAI 拆出 $4B+ 企业部署服务公司（TPG / Bain Capital / Brookfield / Advent / Goldman Sachs / SoftBank + Bain & Company / Capgemini / McKinsey）并吸收 Tomoro 咨询，标志着 AI 厂商竞争向服务 + Forward Deployed Engineers 转向。
- [Anthropic ↔ SpaceX Colossus 1](https://www.siliconrepublic.com/business/anthropic-joins-forces-with-spacex-for-colossus-capacity) - 🆕 **2026-05-06**。Anthropic 拿下 SpaceX 300+ MW / 22 万 GPU 的 Colossus 1 所有可用算力；SpaceX 在收购 xAI 后重新定位为 AI 基础设施提供商，Anthropic 则翻倍付费计划下 Claude Code 的限流。
- [DeepSeek $4B 国家背景轮次](https://www.techtimes.com/articles/316717/20260516/chinas-state-ai-fund-backs-deepseek-4-billion-round-efficiency-challenge-nvidia-dependent.htm) - 🆕 **2026-05-16**。中国国家人工智能产业投资基金 + 大基金三期 + 腾讯 接近完成对 DeepSeek 首次外部轮次，~$4B 金额在 ~$50B 估值上，也是大基金三期已知首次 LLM 投资。
- [教宗利奥 14 世 → 梵蒂冈 AI 委员会](https://www.americamagazine.org/vatican-dispatch/2026/05/16/pope-leo-establishes-new-vatican-commission-on-artificial-intelligence/) - 🆕 **2026-05-16**。教宗利奥 14 世发布 rescriptum 设立梵蒂冈跨部门 AI 委员会（人类整体发展部统筹，叠加信仰部、文化与教育部、传信部、宿呀领生命 / 科学 / 社会科学馆），任期 1 年可续；首份 AI 为题的通谕即将发布。
- [Google I/O 2026 — Gemini 3.5 + Omni + Spark + AI Ultra](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - 🆕 **2026-05-19**。Google 今年最大的 Agent + AGI 发布会：Gemini 3.5 Flash GA （默认模型）、Gemini Omni 世界模型家族、Gemini Spark 24/7 个人 Agent（~30+ MCP 接入的第三方工具）以及新 Google AI Ultra $100/月级别。Pichai 公布 Google 每月处理 **3.2 千万亿个 token**。
- [阿里云杭州峰会 — Qwen 3.7-Max + 珄武 M890](https://www.scmp.com/tech/big-tech/article/3354212/alibaba-unveils-new-qwen-model-custom-chips-bid-become-chinas-ai-factory) - 🆕 **2026-05-20**。阿里推出 Qwen 3.7-Max（面向长静间距任务的代理型编程顶级型）、T-Head **珄武 M890** AI 计算芯片以及全栈 AI 基础设施升级——中国迫迫“AI 工厂”的代表作。
- [OpenAI Guaranteed Capacity（算力年发）](https://openai.com/business/guaranteed-capacity/) - 🆕 **2026-05-19**。面向企业 AI 产品 / Agent / Workflow 的长期算力预订产品（可选 1 / 2 / 3 年期，期限越长折扣越高）：OpenAI 对 Anthropic Priority Tier 与顶级模型推理供给吃紧的产品化回应。
- [Robinhood Agentic Trading + Robinhood ↔ MCP](https://robinhood.com/us/en/newsroom/robinhood-is-now-open-to-agents/) - 🆕 **2026 年 5 月 27 日**（beta）。首家通过 MCP 把交易 API 开放给 AI Agent 的美国主流券商。Agent 对账户只读，仅在隔离的 Agentic 账户里可执行交易；每笔交易推送，一键断开。Agent 真正握有托管决策权而非仅给建议，是 Agent 金融化的重要一步。
- [Microsoft Scout + MAI-Code-1-Flash + MAI-Thinking-1（Build 2026）](https://microsoft.ai/news/microsoft-build-2026-mai-keynote-transcript/) - 🆕 **2026 年 6 月 2 日（Build 2026）**。微软同时发布首个 OpenClaw 驱动的常驻个人 Agent（Scout）、首个自研编程基础模型（MAI-Code-1-Flash，进 GitHub Copilot）以及首个自研推理模型（MAI-Thinking-1）。是与 OpenAI 合作以来微软最大幅度的基础模型独立动作。
- [Meta Business Agent（WhatsApp + Instagram）](https://techcrunch.com/2026/06/03/metas-ai-agent-for-whatsapp-business-is-now-available-globally/) - 🆕 **2026 年 6 月 3 日**。Meta 在伦敦 Conversations 2026 大会全球开放其客服 AI Agent，覆盖 WhatsApp + Instagram DMs。答疑、推荐商品、预约、识销售线索；**100 万 +** 商家已经在用。绑定 WhatsApp Business Premium 分级付费，是 Meta 首个直接对外收费的 AI 产品。
- [WWDC 2026 — Apple Intelligence x Gemini + Foundation Models 框架扩展](https://www.apple.com/newsroom/2026/06/apple-unveils-next-generation-of-apple-intelligence-siri-ai-and-more/) - 🆕 **2026 年 6 月 8 日**。苹果发布下一代 Apple Intelligence 与重做的 Siri AI（多模态、屏幕感知、端侧 + 服务端），新 Siri 底层由 Google Gemini 驱动，原先转交 ChatGPT 的逻辑被取消。Foundation Models 框架新增图像输入、自定义技能、端侧 + 服务端模型统一的 Swift API；SiriKit 弃用，改用扩展后的 App Intents。欧盟 / 中国发布延后。

---

## 📅 2026 AI 时间线

*2026 年 AI 重要里程碑。*

| 时间 | 事件 | 分类 |
|------|------|------|
| **2026-01** | AMD Ryzen AI 400 在 CES 发布 —— 主流 AI PC 及 60 TOPS NPU | 硬件 |
| **2026-02** | Claude Opus 4.6 发布 —— Agent 团队能力 | 模型 |
| **2026-02** | Claude Sonnet 4.6 发布 —— 1M 上下文，Agent 检索 | 模型 |
| **2026-02** | Gemini 3.1 Pro 发布 | 模型 |
| **2026-02** | Qwen3.5 系列发布 —— 原生多模态 + Agent 编程 | 模型 |
| **2026-02** | Qwen3-Coder-Next 发布 —— 80B MoE 编程 Agent 模型 | 模型 |
| **2026-02** | Cursor 支持 8 个并行 Agent | 工具 |
| **2026-02** | GitHub Copilot 扩展 Agent 模式与模型 | 工具 |
| **2026-03** | Gemini 3.1 Flash Lite 面向开发者发布 | 模型 |
| **2026-03** | Mistral Forge 发布 —— 自定义 LLM 训练平台 | 平台 |
| **2026-03** | Microsoft Agent Framework（AutoGen + Semantic Kernel）目标 GA | 框架 |
| **2026-03** | DeepSeek 宣布使用最新英伟达芯片训练新模型 | 模型 |
| **2026-03** | MCP 2026 路线图发布 —— 重点生产规模化与治理 | 协议 |
| **2026-03** | Sora 关闭公告（4 月 26 日应用下架） | 事件 |
| **2026-04-02** | 阿里巴巴发布 Qwen3.6-Plus 闭源旗舰 | 模型 |
| **2026-04-03** | Microsoft AI Agent Governance Toolkit 开源 | 工具 |
| **2026-04-06** | Microsoft Agent Framework 正式宣布 | 框架 |
| **2026-04-07** | 智谱 GLM-5.1 开源 —— 744B MoE，华为昂腾训练 | 模型 |
| **2026-04-08~09** | Meta Muse Spark 发布 —— MSL 首个模型 | 模型 |
| **2026-04** | Claude Mythos Preview —— 受控网络安全研究模型（BenchLM 99，SWE-bench 93.9%） | 模型 |
| **2026-04** | Sora 应用正式关闭 | 事件 |
| **2026-04-14** | Gemini Robotics ER-1.6 升级机器人 AI，增强空间推理 | 机器人 |
| **2026-04-15** | Qwen3.6-35B-A3B 开源（Apache 2.0）| 模型 |
| **2026-04-16** | Claude Opus 4.7 发布 —— SWE-bench Verified 87.6%，`/think xhigh` | 模型 |
| **2026-04-18** | Qwen3.6-Max-Preview 发布 | 模型 |
| **2026-04-20~21** | Kimi K2.6 发布 —— 1T MoE，1000-Agent 集群 | 模型 |
| **2026-04-22** | Qwen3.6-27B 开源 —— 27B 密集多模态 | 模型 |
| **2026-04-23** | 腾讯开源 Hunyuan Hy3 Preview —— 295B/21B MoE，256K 上下文 | 模型 |
| **2026-04-23** | Claude Managed Agents Memory 公测 —— 跨会话记忆 | 工具 |
| **2026-04-23** | OpenAI 发布 GPT-5.5 —— 代理 / 推理升级 | 模型 |
| **2026-04-24** | DeepSeek V4 Pro & Flash 发布 —— 1.6T MoE，1M 上下文，MIT | 模型 |
| **2026-04-24** | Cohere 与德国 Aleph Alpha 合并，$20B 估值 + $600M 资金 | 产业 |
| **2026-04-27** | 阿里天马 AI 图生视频进入公测 | 模型 |
| **2026-04-27** | LangGraph v0.3.19 发布，Swarm 预制 Agent | 框架 |
| **2026-04-28** | NVIDIA Nemotron 3 Nano Omni 发布 —— 30B 多模态 | 模型 |
| **2026-04-28~29** | 中科院 ScienceOne 100 / 磐石100 发布 —— 50+ 中科院研究所 | 模型 |
| **2026-04-30** | OpenAI GPT-5.5-Cyber 通过 TAC 计划扣发 | 模型 |
| **2026-04-30** | OpenAI 发布 [《构建 Agent 实战指南》](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/) | 资源 |
| **2026-05-01** | Anthropic Claude Security 公测 —— Opus 4.7 驱动代码库漏洞扫描 | 工具 |
| **2026-05** | 麦格理银行（Macquarie Bank）报告 7 个月使用 Gemini Enterprise 节约 13 万小时 | 产业 |
| **2026-05** | Google 开始为启用车辆推送 Gemini，替代 Google Assistant（英语优先，美国首发） | 产业 |
| **2026-05-04** | Google 关闭 [Project Mariner](https://deepmind.google/models/project-mariner/)，浏览器 Agent 技术并入 Gemini Agent | 工具 |
| **2026-05-04** | Anthropic + Goldman Sachs + Blackstone 宣布 **$1.5B Claude 部署合资公司**，向中型华尔街公司派驻 Anthropic 工程师 | 产业 |
| **2026-05-05** | OpenAI 把 **GPT-5.5 Instant** 作为 ChatGPT 新默认模型推出 —— 主打效率，幻觉率降低约 50% | 模型 |
| **2026-05-05** | Anthropic 发布 **Claude Finance Agents** —— 10 个金融服务专用 Agent（路演簿生成、KYC、月末结账），可作为 Claude Cowork 插件 / Claude Code skill / Managed Agents cookbook | 工具 |
| **2026-05-05** | OpenAI ↔ 普华永道（PwC）合作 —— 金融服务 Agent（预测、支付） | 产业 |
| **2026-05-07** | Google 为 **Flow（Veo 视频）准备 Agent Mode** —— 视频制作流程自动化 | 工具 |
| **2026-05-08** | OpenAI 发布 **GPT-Realtime-2 / Realtime-Translate / Realtime-Whisper** —— 语音 Agent、实时翻译、实时转录 | 模型 |
| **2026-05-09** | OpenAI 在 ChatGPT Enterprise 推出 **Workspace Agents** —— 跨连接应用的可重复工作流自动化 | 工具 |
| **2026-05-11** | [OpenAI Deployment Company](https://openai.com/index/openai-launches-the-deployment-company/) 成立 —— $4B+ 企业服务子公司，TPG / Bain Capital / Brookfield + Bain & Company / Capgemini / McKinsey 共投；合并 Tomoro 咨询 | 产业 |
| **2026-05-11 – 13** | [SAP Sapphire 2026 Orlando](https://news.sap.com/2026/05/sap-sapphire-sap-unveils-autonomous-enterprise/) — SAP Business AI Platform、**Joule Studio 2.0**、Autonomous Suite（50+ 领域 Assistant + 200+ Agent）；Joule Studio 2.0 从 2026-06 起 GA | 产业 |
| **2026-05-12** | [Claude for Legal](https://www.anthropic.com/news/claude-for-legal) — Claude Cowork 上 20+ 个 MCP 连接器（iManage、NetDocuments、DocuSign、LexisNexis、Westlaw、Harvey、Everlaw、Relativity 等）+ 12 个执业领域 plugin | 工具 |
| **2026-05-12 – 15** | [Visual Studio 2026 Insiders](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/) — Copilot Chat "Agent Mode" 在 IDE 里引入引导式 Agent Skills 创作 | 工具 |
| **2026-05-13** | [Claude for Small Business](https://www.anthropic.com/news/claude-for-small-business) — 15 个预置 Agent 工作流 + QuickBooks / PayPal / HubSpot / Canva / DocuSign / Google Workspace / Microsoft 365 连接器；美国 10 城巡讲 | 工具 |
| **2026-05-13** | [Cursor 3.4 云 Agent 环境](https://cursor.com/changelog) — 多仓库，带 build secrets 的 Dockerfile 配置，快 70% 镜像缓存，环境版本历史，审计日志，限定出网 / secrets | 工具 |
| **2026-05-13 – 16** | [Figure Helix 02 直播](https://www.businessinsider.com/figure-ai-turned-a-humanoid-sorting-packages-must-see-tv-2026-5) — F.03 + Helix 02 在包裹分拧线压力测试，8 小时 ~22K，24 小时 ~30K，~72 小时 ~88K 包裹 | 机器人 |
| **2026-05-14** | [Anthropic ↔ Gates Foundation $200M 合作](https://www.anthropic.com/news/gates-foundation-partnership) — 4 年资助 + Claude 额度 + Anthropic 工程，面向全球健康 / 生命科学 / 教育 / 农业 | 产业 |
| **2026-05-14** | [Anthropic ↔ PwC 联盟扩张](https://www.pwc.com/us/en/about-us/newsroom/press-releases/anthropic-pwc-expand-alliance-agentic-enterprise.html) — 全球 Claude Code + Cowork 铺开，认证 30,000 名 PwC 员工，共建 Agentic Enterprise 卓越中心 | 产业 |
| **2026-05-14** | [Genkit Middleware](https://developers.googleblog.com/announcing-genkit-middleware-intercept-extend-and-harden-your-agentic-apps/) — Google 为开源 Genkit 加上可组合中间件（TS / Go / Dart）| 框架 |
| **2026-05-14** | [Zyphra ZAYA1-8B-Diffusion-Preview](https://www.zyphra.com/post/zaya1-8b-diffusion-preview) — 首个从自回归 LLM 转换得来的 MoE 扩散语言模型；首个在 AMD GPU 上训练的扩散 LM；最多 7.7× 推理加速 | 模型 |
| **2026-05-16** | [教宗利奥 14 世设立梵蒂冈 AI 委员会](https://www.americamagazine.org/vatican-dispatch/2026/05/16/pope-leo-establishes-new-vatican-commission-on-artificial-intelligence/) — 跨部门机构，首份 AI 通谕即将发布 | 产业 |
| **2026-05-16** | [OpenAI ↔ Malta 合作](https://openai.com/index/malta-chatgpt-plus-partnership/) — 所有 14 岁以上马耳他居民在完成 2 小时 AI 素养课后获得一年免费 ChatGPT Plus（"OpenAI for Countries"）| 产业 |
| **2026-05-16** | [DeepSeek 国家背景 $4B 轮次](https://www.techtimes.com/articles/316717/20260516/chinas-state-ai-fund-backs-deepseek-4-billion-round-efficiency-challenge-nvidia-dependent.htm) — 国家 AI 产业基金 + 大基金三期 + 腾讯 主导，~$50B 估值首次外部轮 | 产业 |
| **2026-05-13** | [Runway Agent](https://chatlyai.app/news/runway-agent-launch-may-2026) 发布 — 以脚本为输入、在 Gen-4 / Aleph 上端到端交付多镜头完成品视频 | 工具 |
| **2026-05-18** | [OpenAI ↔ Dell Codex 合作](https://openai.com/news/company-announcements/) — Codex 首次进入混合云 / 本地部署，面向需要数据主权的强监管行业 | 产业 |
| **2026-05-18** | [阿里 Qwen 3.7-Max-Preview / Plus-Preview](https://www.scmp.com/tech/tech-trends/article/3354087/alibaba-teases-new-qwen-previews-highest-ranking-chinese-ai-models-arena) — LM Arena 上中文世界最高分中国模型（文本 + 视觉双赛道）| 模型 |
| **2026-05-18** | [Boston Dynamics Atlas 100 磅操作](https://www.techtimes.com/articles/316854/20260519/boston-dynamics-reveals-how-atlas-learned-lift-100-pound-loads-hyundai-plans-30000-per-year.htm) — 现代集团承诺从 2028 起在乔治亚部署 **25K+ 台 Atlas** | 机器人 |
| **2026-05-18** | [Figure F.03 vs 人类 8 小时分拧挑战](https://incrypted.com/en/figure-ai-held-a-human-vs-robot-marathon/) — 人类以 12,924 微赢 12,732（2.79 vs 2.83 秒 / 件）| 机器人 |
| **2026-05-18** | [Anthropic 就 Claude Mythos 向 FSB 汇报](https://www.theguardian.com/technology/2026/may/18/anthropic-ai-claude-mythos-cyber-financial-stability-board-fsb) — 顶级 lab 首次向 G20 金融稳定监管机构介绍顶级模型的攻击性网络能力 | 产业 |
| **2026-05-18** | [ChatGPT 安全系统更新](https://www.edtechinnovationhub.com/news/openai-updates-chatgpt-safety-systems-to-track-risk-across-sensitive-conversations) — 加入跨会话的风险跟踪（自杀 / 自伤 / 伤他）| 产业 |
| **2026-05-19** | **Google I/O 2026** — [Gemini 3.5 Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) 上线即成为 Gemini App + Google 搜索 AI Mode 默认模型（官方称输出 token 速度约 4 倍于同类顶级模型）；Gemini 3.5 Pro 预计 6 月 | 模型 |
| **2026-05-19** | **Google I/O 2026** — [Gemini Omni / Omni Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/)，DeepMind 面向 AGI 的世界模型家族（任意输入 → 任意输出，视频起步）| 模型 |
| **2026-05-19** | **Google I/O 2026** — [Gemini Spark](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) 24/7 个人 AI Agent + ~30+ 个 MCP 接入的第三方工具，限 **Google AI Ultra ($100/月)** 订阅 | 工具 |
| **2026-05-19** | [OpenAI Guaranteed Capacity（算力年发）](https://openai.com/news/company-announcements/) 发布 — 1/2/3 年期企业算力预订产品 | 产业 |
| **2026-05-19** | [OpenAI ↔ Google SynthID + C2PA 内容源头验证](https://openai.com/index/advancing-content-provenance/) — 顶级 lab 首次在跨平台 AI 图片水印上互通，附公开验证器预览 | 产业 |
| **2026-06** | [OutSystems Agentic Systems Platform](https://www.outsystems.com/) 发布 — 低代码平台转型为“AI 原生”多 Agent 编排底座 | 产业 |
| **2026-05-19** | [Anthropic：Widening the conversation on frontier AI](https://www.anthropic.com/news/widening-conversation-ai) — 与智慧传统展开顶级 AI 安全对话的框架 | 产业 |
| **2026-05-19** | [DeepSeek 招募 Jane Street 前工程师组建 AI harness 团队](https://www.scmp.com/tech/big-tech/article/3354113/deepseek-recruits-former-jane-street-engineer-catch-ai-agents-revenue-race) — DeepSeek 从模型 R&D 向 Agent 产品化转向 | 产业 |
| **2026-05-20** | **阿里云杭州峰会** — [Qwen 3.7-Max](https://www.scmp.com/tech/big-tech/article/3354212/alibaba-unveils-new-qwen-model-custom-chips-bid-become-chinas-ai-factory) GA，代理型编程与长静间距任务；同期上线 T-Head **珄武 M890** AI 芯片与全栈 AI 基础设施升级 | 模型 |
| **2026-05-20** | [BMS ↔ Anthropic Claude Enterprise](https://news.bms.com/news/corporate-financial/2026/Bristol-Myers-Squibb-Announces-Strategic-Agreement-with-Anthropic-to-Position-Claude-Enterprise-as-the-Shared-Intelligence-Platform-Across-Its-Global-Operations/default.aspx) — 30K+ 员工统一标准 Claude Enterprise，首个顶 5 药企全公司级部署 | 产业 |
| **2026-05-20** | [LlamaIndex ↔ Google Agents API](https://www.kucoin.com/news/flash/google-launches-agents-api-llama-index-integrates-llamaparse-for-unstructured-document-processing) — LlamaParse / LiteParse 进入 Google Agents API 沙箱；Sandboxed-Lit + ParseBench 同期上线 | 框架 |
| **2026-05-20** | [Microsoft RAMPART + Clarity](https://www.microsoft.com/en-us/security/blog/2026/05/20/introducing-rampart-and-clarity-open-source-tools-to-bring-safety-into-agent-development-workflow/) 开源 — Agentic AI 的 pytest 原生白盒安全 / 可靠性测试框架 + 结构化设计评审伴侣；可直接接入 CI/CD，是 PyRIT 在开发者侧的后续 | 工具 |
| **2026-05-06** | [AWS MCP Server GA](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/) — AWS 托管的 MCP 入口，暴露任意 AWS API、用沙箱 Python 跑多步操作、用 agent skill 取代 SOP；首个超大型云厂商的一方 MCP server | 协议 |
| **2026-05-01** | [Google Workspace MCP Server](https://workspaceupdates.googleblog.com/2026/05/agent-tools-and-security-updates-for-workspace-developers.html) 逐步上线 — Workspace 原生 MCP 服务器，Gmail / Drive / Calendar / Docs / Sheets 都能走 MCP，OAuth 范围由管理员控制 | 协议 |
| **2026-05-14** | [Grok Build (早期 beta)](https://x.ai/news/grok-build-cli) — xAI 推出的 agentic CLI 编码 Agent，由 **grok-code-fast-1** 驱动，隔离环境并行子 Agent，限 SuperGrok Heavy 用户 | 工具 |
| **2026-05-14** | [iManage MCP Server](https://imanage.com/resources/resource-center/news/mcp-server-available-broader-ai-ecosystem/) 发布 — 首家身名领域 SaaS 推出对外公开的 MCP 端点 | 工具 |
| **2026-05-19** | [Google Antigravity 2.0](https://antigravity.google/blog/introducing-google-antigravity-2-0) 于 I/O 2026 上线 — 独立桌面端多 Agent 编排、调度 / 异步 / 动态子 Agent、Antigravity CLI + SDK；企业版集成进 Gemini Enterprise Agent Platform | 工具 |
| **2026-05-22** | [Kore.ai Artemis Agent Platform](https://venturebeat.com/technology/kore-ai-launches-artemis-ai-agent-platform-expands-challenge-to-microsoft-and-salesforce) 在 Azure 上线 — AI 原生企业 Agent 平台，核心是声明式的 **Agent Blueprint Language (ABL)** | 产业 |
| **2026-05-22** | [FPT Flezi Foundry™](https://lasvegassun.com/news/2026/may/22/fpt-launches-flezi-foundry-advancing-ai-augmented-/) 发布 — “Service-as-a-Software” 治理下的 AI 增强交付平台，提供 Agentic Development Lifecycle (ADLC) 与 Agentic Managed Services (AMS) 两种模式 | 产业 |
| **2026-05-22** | [JetBrains Rider AI 测试生成 skill](https://blog.jetbrains.com/dotnet/2026/05/22/claude-codex-ai-agent-skill-for-writing-tests/) — 将 .NET 覆盖率数据喂给 Claude Code / Codex，让 Agent 只写未覆盖分支的测试 | 工具 |
| **2026-05-28** | [Claude Opus 4.8](https://www.anthropic.com/claude/opus) Anthropic 发布 — 代码库级迁移、动态工作流预览（并发几百个子 Agent）、努力控制面板、Fast 模式价格降 3 倍；预告 **Mythos 级**模型 | 模型 |
| **2026-05-28** | [Koog 1.0](https://blog.jetbrains.com/ai/2026/05/koog-1-0-is-out-stable-core-better-interop-and-multiplatform-observability/) KotlinConf 2026 发布 — JetBrains 的开源 Kotlin / Java AI Agent 框架达到稳定 1.0，Kotlin Multiplatform 部署、跨端 OpenTelemetry | 框架 |
| **2026-05-28** | [Gemini Omni Flash 对话式视频编辑](https://www.techtimes.com/articles/317309/20260528/google-gemini-omni-flash-brings-voice-controlled-ai-video-editing-future-conversational-ai.htm) 在 Gemini App / Google Flow / YouTube Shorts 上线 — 语音 + 文字驱动的电影式编辑取代传统 NLE | 工具 |
| **2026-05-21** | [MCP 2026-07 Release Candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) 发布 — 无状态协议核心、扩展机制、MCP Apps 服务端渲染 UI、OAuth/OIDC 加固，正式版目标7月 28 日 | 协议 |
| **2026-04-17 – 20** | [苹果 CEO 交接公告](https://www.sec.gov/Archives/edgar/data/0000320193/000114036126015711/ef20071035_8k.htm) — 蒂姆·库克在 15 年后于 **2026-09-01** 转任执行董事长；硬件工程高级副总裁 **John Ternus** 出任 CEO。AI 时代首次发生在万亿美元级平台公司的 CEO 更替 | 产业 |
| **2026-06-08** | **[WWDC 2026](https://www.techradar.com/news/live/apple-wwdc-2026-live)** — 苹果发布由 Google Gemini 驱动的 Apple Intelligence 与全面重做的新 Siri（Siri 中原本转发给 ChatGPT 的逻辑被淘汰）；iOS 27、iPadOS 27、macOS 27 "Golden Gate"、watchOS 27、tvOS 27、visionOS 27，端侧 AI 更深；App 启动快约 30%，照片预览快 70%，iPadOS 文件传输快 5 倍；2026 秋季发布 | 产业 |
| **2026-04** | Gartner 预计 2026 年底 40% 企业应用嵌入 AI Agent | 产业 |
| **2026-04** | Google 承诺对 Anthropic 跟进最高 $40B 投资（首期 $10B） | 产业 |
| **2026 持续** | A2A Protocol 合作伙伴增至 150+ | 协议 |
| **2026 持续** | 85% 开发者经常使用 AI 编程工具 | 产业 |
| **2026 持续** | 企业 Agent AI 实践加速 —— "Agents as a Service" 兴起 | 产业 |
| **2026-01-06** | [Lenovo + Motorola Qira](https://news.lenovo.com/pressroom/press-releases/lenovo-unveils-lenovo-and-motorola-qira/) 在 CES 2026 发布 — 跨设备"个人环境智能"，Q1 落地联想，随后扩展至摩托罗拉 | 产业 |
| **2026-02-10** | [Snowflake Agent World Model](https://github.com/Snowflake-Labs/agent-world-model) 开源 — 1,000 个 SQL 驱动的 MCP 合成环境 + RL 训练 Agent；面向大规模 Agentic RL，后入选 ICML 2026 | 研究 |
| **2026-02-26** | [1X NEO 消费级人形机器人开放预订](https://www.1x.tech/discover/neo-home-robot) — $20K 早鸟价，2026 年家庭交付 | 机器人 |
| **2026-03-10** | [Hume TADA](https://github.com/HumeAI/tada) 开源 — Text-Acoustic Dual Alignment TTS，MIT，测试中零转录错误，可在手机上跑 | 模型 |
| **2026-04-28** | [Anthropic 创意工具连接器](https://www.anthropic.com/news/claude-for-creative-work) — 9 个 MCP 连接器对接 Adobe / Blender / Autodesk Fusion / Ableton / Splice / Canva Affinity / SketchUp / Resolume | 工具 |
| **2026-05-13** | [Microsoft Copilot Studio CUA GA](https://techcommunity.microsoft.com/blog/copilot-studio-blog/computer-using-agents-in-microsoft-copilot-studio-are-now-generally-available/4519427) — 在 Microsoft 365 / Power Platform 内构建 UI 驱动的网站 / 桌面 Agent | 工具 |
| **2026-05-26** | [Coinbase Base MCP](https://fortune.com/2026/05/26/coinbase-pushes-further-into-ai-payments-with-new-mcp-for-base-network/) 上线 — 首个交易所级、面向链上交易与借贷的 MCP 端点 | 协议 |
| **2026-05-27** | [Robinhood Agentic Trading](https://robinhood.com/us/en/newsroom/robinhood-is-now-open-to-agents/) beta — 首家通过 MCP 把股票交易开放给 AI Agent 的美国主流券商 | 产业 |
| **2026-05-29** | [OpenAI Codex 在 Windows 上 Computer Use](https://windowsforum.com/threads/openai-codex-computer-use-brings-agent-control-to-windows-desktop.421107/) — 沙箱化 Codex 对 Windows 桌面的 Agent 控制 GA | 工具 |
| **2026-06-02** | [Microsoft Build 2026](https://microsoft.ai/news/microsoft-build-2026-mai-keynote-transcript/) — MAI-Thinking-1（首个自研推理）、MAI-Code-1-Flash（5B 编程模型进 GitHub Copilot）、[Microsoft Scout](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/)（基于 OpenClaw 的常驻个人 Agent）同日发布 | 模型 / 工具 |
| **2026-06-03** | [Meta Business Agent](https://techcrunch.com/2026/06/03/metas-ai-agent-for-whatsapp-business-is-now-available-globally/) 全球登陆 WhatsApp + Instagram — Meta 首个直接收费的 AI 产品，绑定 WhatsApp Business Premium 套餐 | 产业 |
| **2026-06-03** | [Perplexity Personal Computer for Windows](https://www.perplexity.ai/hub/products/computer-for-windows) 宣布 — 自动编排 19+ 个 AI 模型，跨本地文件 / 原生应用 / Web | 工具 |
| **2026-06-06** | [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code) 由 Moonshot AI 发布 — TypeScript / MIT 终端 Agent，内置 coder / explore / plan 子 Agent 在隔离上下文中运行 | 工具 |
| **2026-06-08** | **WWDC 2026 Apple Intelligence + Siri AI 重做** — Foundation Models 框架新增图像输入、自定义 skill、端侧 + 服务端统一 Swift API；SiriKit 弃用改用扩展后的 App Intents；新 Siri 底层为 Google Gemini，不再是 ChatGPT | 模型 / 工具 |
| **2026-06-09** | [Claude Fable 5 + Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) 发布 — Anthropic 首批一般可用的 **Mythos 级**模型（Fable 5 公开；Mythos 5 经 Project Glasswing 限量） | 模型 |
| **2026-06-12** | [美国出口管制指令迫使 Anthropic 对所有客户停用 Fable 5 + Mythos 5](https://www.anthropic.com/news/fable-mythos-access) — 首例政府强制下架已公开部署的前沿模型 | 产业 |
| **2026-06-12** | [Kimi K2.7 Code](https://kimi.ai/) 由 Moonshot AI 发布 — 1T MoE 编程优先模型（256K，Modified MIT），推理 token 用量约降 30% | 模型 |
| **2026-06-13** | [GLM-5.2](https://z.ai/blog/glm-5.2) 由智谱 AI 发布 — 编程优先的 744B MoE，100万 token 上下文，全部 GLM Coding Plan 套餐上线 | 模型 |
| **2026-06-30** | [Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5) 发布 — 迄今最具 Agent 能力的 Sonnet，低成本下性能逼近 Opus 4.8，成为 Claude.ai 免费版/Pro 新默认模型 | 模型 |
| **2026-07-01** | [Claude Fable 5 全球恢复访问](https://www.anthropic.com/news/redeploying-fable-5) — 美国商务部于 6 月 30 日解除出口管制；Anthropic 在 Claude.ai、API、Claude Code 与 Claude Cowork 全面恢复 Fable 5 全球访问，并部署新的安全分类器。Mythos 5 仍限美国受审实体 | 模型 |
| **2026-07-01** | [Devin Security Swarm](https://www.prnewswire.com/news-releases/cognition-launches-devin-security-swarm-to-tackle-the-vulnerability-backlog-302814800.html) 由 Cognition 发布 — 并行 Agent 漏洞发现、运行时可利用性验证与修复 PR | 工具 |
| **2026-07-01** | [Grok Voice Agent Builder](https://x.ai/news/grok-voice-agent-builder) — xAI 基于 Grok Voice 的无代码生产级语音 Agent 平台；电话接入、MCP 连接器、80+ 音色，beta 期 $0.05/分钟 | 工具 |
| **2026-07-02** | [Sysdig 披露 JADEPUFFER](https://hackread.com/sysdig-jadepuffer-first-agentic-ransomware-operation/) — 首个由自主 AI Agent 端到端执行的勒索软件作战，从初始 RCE 入侵到不可恢复的加密勒索 | 产业 |
| **2026-07-02** | [Leanstral 1.5](https://mistral.ai/news/leanstral-1-5/) 由 Mistral 发布 — 开源权重的 Lean 4 形式化验证模型（miniF2F 100%）；智谱同日发布面向 GLM-5.2 的 Agent harness [ZCode](https://www.scmp.com/tech/tech-trends/article/3359170/zhipu-ai-releases-harness-glm-52-model-chinese-firm-takes-aim-anthropic) | 模型 |
| **2026-07-03** | AG2 v1.0.0b0 发布 — AutoGen 的社区驱动 Fork；微软已于 2026 Q1 将 AutoGen 转入维护模式 | 框架 |
| **2026-07-06** | [腾讯混元 Hy3](https://www.tencent.com/en-us/articles/2202386.html) 正式开源发布（Apache 2.0）— 295B 总 / 21B 激活 MoE，接续 4 月预览版；gpt-realtime-2.1 / 2.1-mini 同日登陆 OpenAI API | 模型 |
| **2026-07-07** | [Meta Muse Image](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) 发布 — Meta Superintelligence Labs 的 Agent 式图像生成模型，集成到 Instagram Stories（美国）与限定国家的 WhatsApp；同时预览 Muse Video | 模型 |
| **2026-07-07** | Arize Phoenix 7 月 7 日版本：Metric Charts、Trace Search、扩展 REST API | 工具 |
| **2026-07-08** | [Grok 4.5](https://x.ai/news/grok-4-5) 由 xAI 发布 — 与 Cursor 联合训练的编程 + Agent 旗舰；500K 上下文，每百万输入/输出 token $2/$6；Cursor 默认模型 | 模型 |
| **2026-07-08** | [GPT-Live-1 / GPT-Live-1 mini](https://openai.com/index/introducing-gpt-live/) — 全双工语音模型，取代进阶语音模式；GPT-Live-1（付费）与 GPT-Live-1 mini（免费）；支持实时语音翻译 | 模型 |
| **2026-07-08** | [Robostral Navigate](https://mistral.ai/news/robostral-navigate/) — Mistral 首个机器人模型（仅凭单个 RGB 摄像头的 8B 具身导航）；OpenAI 同日审计 SWE-bench Pro，发现约 30% 任务存在缺陷 | 模型 |
| **2026-07-09** | [GPT-5.6 Sol / Terra / Luna](https://openai.com/index/gpt-5-6/) GA — GPT-5.6 全家族在受信伙伴预览后于 ChatGPT、Codex 与 API 全面开放；[ChatGPT Work](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) 同步发布，Codex 整合进 ChatGPT 桌面 App | 模型 |
| **2026-07-09** | [Muse Spark 1.1](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/) 由 Meta 发布 — 通过全新公开预览的 Meta Model API 提供的多模态 Agent 模型；开源 Llama 路线之外的专有模型布局 | 模型 |
| **2026-07-10** | [Cursor 3.11](https://cursor.com/changelog) — 侧边聊天、对话历史搜索、Cloud Agent Hooks 精细化 Agent 可观测性 | 工具 |
| **2026-07-14** | [Oracle 为 Fusion AI Agent Studio 加入 AI 原生 Agentic Applications Builder](https://www.oracle.com/news/announcement/oracle-introduces-ai-native-builder-experience-2026-07-14/) — 向专业代码开发者开放 Fusion Agentic 应用；Fusion 客户免费使用 | 框架 |
| **2026-07-16** | [Kimi K3](https://kimi.ai/) 由 Moonshot AI 发布 — 2.8T 参数稀疏 MoE（896 专家，每 token 激活 16 个），1M token 上下文，每百万 token $3/$15；承诺 7 月下旬开源全量权重 | 模型 |

---

## 贡献

请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。**反垃圾质量门槛**适用于中英日三个版本：自我推广批量铺货 PR 一律拒绝。

## License

MIT © [Zijian Ni](https://github.com/Zijian-Ni)

---

*Made with ❤️ by [Zijian Ni](https://github.com/Zijian-Ni) · 2026。中文版本与英文版保持同步，发现不一致以英文为准。*
