<div align="center">

# 🤖 Awesome AI Agents 2026 · 中文版

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fawesome-ai-agents-2026&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)](https://github.com/Zijian-Ni/awesome-ai-agents-2026/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-June%2012%2C%202026-blue.svg)](#)
[![Resources](https://img.shields.io/badge/Resources-500%2B-orange.svg)](#)
[![Audited](https://img.shields.io/badge/Spam_Audited-2026--06--12-success.svg)](#️-状态图例)
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
> - 🆕 [最新添加（2026 年 5 月）](#-2026-ai-时间线) • 🛡️ [安全](#️-agent-安全) • 💰 [费用对比](#-基础大模型--api-价格与上下文窗口)

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

- [GPT-5.5](https://openai.com/index/gpt-5-5-system-card/) - 🆕 **2026-04-23 发布**（代号 "Spud"）。OpenAI 面向 Agent 任务的新一代旗舰：编程、在线研究、数据分析、自主工具调用。推理稳定性与长任务执行力大幅提升。ChatGPT Plus / Pro / Business / Enterprise 可用。
- [GPT-5.5 Pro](https://openai.com/index/gpt-5-5-system-card/) - 🆕 2026-04-23。并行测试期算力变体，更高准确率。Pro / Business / Enterprise。
- [GPT-5.5 Instant](https://openai.com/index/gpt-5-5-instant/) - 🆕 **2026-05-05**。ChatGPT 新默认模型，效率优先升级，高风险提示词幻觉率下降约 50%；免费用户可用。
- [GPT-5.5-Cyber](https://openai.com/index/trusted-access-for-cyber/) - 🆕 **2026-04-30**。GPT-5.5 的网络安全特化版本，通过 OpenAI Trusted Access for Cyber (TAC) 计划仅向防御者、政府、关键基础设施运营方、安全厂商开放，不对公众发布。
- [OpenAI Daybreak](https://thehackernews.com/2026/05/openai-launches-daybreak-for-ai-powered.html) - 🆕 **2026-05-12**。整合 GPT-5.5 + GPT-5.5-Cyber + Trusted-Access-for-Cyber 的网络防御平台，提供 AI 驱动的漏洞检测与补丁验证；预览版已向欧盟政府与安全厂商开放。
- [GPT-5.4](https://openai.com/) - 2026-03 发布。1M token 上下文，编程、Computer Use、工具检索均强。BenchLM 94，SWE-bench Verified 77.2%，OSWorld 75%（超过人类基线）。
- [GPT-5.4 Pro](https://openai.com/) - GPT-5.4 的高准确率变体。BenchLM 92。
- [GPT-5.3](https://openai.com/) - 2026 年初。包括 GPT-5.3 Instant（对话）和 GPT-5.3-Codex（编程）。
- [GPT-5.2](https://openai.com/) - 2025-12 发布。SOTA 推理 + 长上下文 + 视觉。
- [GPT-5](https://openai.com/index/introducing-gpt-5/) - 2025-08 发布，ChatGPT 默认模型，替代 GPT-4o。多模态 + gpt-5 / mini / nano 三档变体。
- [GPT-4o](https://openai.com/index/hello-gpt-4o/) - Omni 模型，原生支持文本/视觉/音频。2026-02 从 ChatGPT 下线，API 仍可用。
- [GPT-4.5](https://openai.com/) - ⚠️ **2026 年 6 月 27 日从 ChatGPT 退役**（API 继续可用）。最初于 2025 年 2 月作为研究预览发布，随着 GPT-5.5 家族的全面接管而退役；o3 也计划于 2026 年 8 月 26 日退役。
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

- [Claude Opus 4.8](https://www.anthropic.com/claude/opus) - 🆕 **2026-05-28**。Opus 重大迭代：代码库级别的迁移能力、更准的 Agent 判断，推出研究预览的「动态工作流」能在单 session 里并发几百个子 Agent，加入手动调节推理投入的「努力控制」面板；**Fast 模式价格降 3 倍**，输入 / 输出仍为 $5 / $25 每百万 token。Anthropic 原生、Amazon Bedrock、AWS Claude Platform、Google Cloud、Microsoft Foundry 上线。同时预告面向小范围企业的 **Mythos 级别**新一代模型。
- [Claude Opus 4.6](https://www.anthropic.com/) - 2026-02 发布。1M token 上下文，14.5 小时任务执行。LMArena 对话榜首。
- [Claude Sonnet 4.6](https://www.anthropic.com/news/claude-sonnet-4-6) - 2026-02 发布。前沿编程与 Agent 表现，1M token 上下文。
- [Claude Mythos Preview](https://www.anthropic.com/) - 🆕 2026-04 受邀研究预览。BenchLM 99（榜首），SWE-bench Verified 93.9%。Project Glasswing 合作伙伴专属。
- [Claude Opus 4](https://www.anthropic.com/news/claude-4) - 2025-05 发布。
- [Claude Sonnet 4](https://www.anthropic.com/news/claude-4) - 2025-05 发布。
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - Anthropic 出品、运行在终端里的 Agent 化编程工具。Opus 4.7 + `/think xhigh`。
- [Claude Security](https://www.anthropic.com/) - 🆕 **2026-05-01** 公测。Opus 4.7 驱动的企业级代码漏洞扫描器：扫整个代码库，生成有置信度评分、严重程度、复现步骤、修复建议的补丁。Enterprise 用户在 [claude.ai/security](https://claude.ai/security) 使用。
- [Claude Finance Agents](https://www.anthropic.com/news/finance-agents) - 🆕 **2026-05-05**。基于 Opus 4.7 的 10 个金融领域专业 Agent，覆盖 pitchbook 撰写、KYC、月结、交易筛查等。可作为 Claude Cowork 插件、Claude Code skill 或 Managed-Agents cookbook 部署。
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

- [Gemini 3.5 Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - 🆕 **2026-05-19 — Google I/O 2026**。推出即成为 Gemini App + Google 搜索 AI Mode 的默认模型，官方称输出 token 速度 **约 4 倍于**同类顶级模型，在关键 benchmark 上超越 Gemini 3.1 Pro。Gemini 3.5 Pro 预计 6 月上线。
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

- [Llama 5](https://ai.meta.com/llama/) - 🆕 **2026-04-08**。Meta 超级智能实验室发布的 600B+ 参数开源旗舰；"递归自我改进" 研究路线。官方宣称在推理、代码、自主 Agent 行为上超越主流闭源模型。
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

- [Mistral Medium 3.5](https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04) - 🆕 **2026-04-29**。Dense 128B 开放权重模型，256K 上下文，Modified MIT 许可。统一指令跟随、推理与代码能力。
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

- [DeepSeek-V4-Pro](https://api-docs.deepseek.com/news/news260424) - 🆕 **2026-04-24**。1.6T 总 / 49B 激活 MoE，1M 上下文。MIT。Agent、世界知识、推理领域开源标杆。
- [DeepSeek-V4-Flash](https://api-docs.deepseek.com/news/news260424) - 🆕 2026-04-24。284B 总 / 13B 激活 MoE，1M 上下文。MIT。性价比层。
- [DeepSeek Agent Harness 团队](https://www.scmp.com/tech/big-tech/article/3354113/deepseek-recruits-former-jane-street-engineer-catch-ai-agents-revenue-race) - 🆕 **2026-05-19**。DeepSeek 从 Jane Street 挨角一名资深工程师，为新设的 "AI harness" 团队搭建把 DeepSeek V4 所能生产化为 **能收费的自主 Agent** 的硬调度 / 程序化套件 —— 首个明确信号：DeepSeek 开始从原生模型 R&D 跳到 Agent 产品化。
- [DeepSeek-V3.2](https://www.deepseek.com/) - 2025-12 发布。671B MoE，V3.2 Speciale 推理增强。
- [DeepSeek-R2](https://www.deepseek.com/) - 2026 推理模型。R1 后继，对标 GPT-5、Gemini 3 Pro。
- [DeepSeek-R1](https://www.deepseek.com/) - 2025-01 发布的思维链推理模型。
- [DeepSeek-Coder-V2](https://github.com/deepseek-ai/DeepSeek-Coder-V2) - 编程模型，对标 GPT-4。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeepseek-ai%2FDeepSeek-Coder-V2&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Alibaba (Qwen) 🇨🇳

- [Qwen 3.7-Max](https://www.scmp.com/tech/big-tech/article/3354212/alibaba-unveils-new-qwen-model-custom-chips-bid-become-chinas-ai-factory) - 🆕 **2026-05-20 — 阿里云杭州峰会**。为 AI Agent 量身打造的新一代顶级：代理型编程、复杂推理、「长静间距」多步任务能力；同期亊相新的 T-Head **珄武 M890** AI 算力芯片与全栈 AI 基础设施升级。面向全球开发者 / 企业即将上线。
- [Qwen 3.7-Max-Preview / Plus-Preview](https://www.scmp.com/tech/tech-trends/article/3354087/alibaba-teases-new-qwen-previews-highest-ranking-chinese-ai-models-arena) - 🆕 **2026-05-18**。杭州峰会前的预览梯队；LM Arena 上文本 + 视觉双赛道均为**中文世界最高分**中国模型。
- [Qwen3.6-27B](https://qwen.ai/blog?id=qwen3.6-27b) - 🆕 **2026-04-22**。27B 密集多模态。开源。Agent 编程 + 思维上下文保持。
- [Qwen3.6-Max-Preview](https://qwen.ai/) - 🆕 **2026-04-18**。闭源前沿预览。1M 上下文，中文模型编程榜顶尖。
- [Qwen3.6-35B-A3B](https://qwen.ai/blog?id=qwen3.6-35b-a3b) - 🆕 **2026-04-15**。MoE 35B 总 / 3B 激活。Apache 2.0。稳定性与实用性增强。
- [Qwen3.6-Plus](https://qwen.ai/) - 🆕 **2026-04-02**。闭源旗舰。token 性价比高，长上下文 + 工具调用 + Agent 表现强。
- [Tianma (天马) AI](https://www.alibabacloud.com/) - 🆕 **2026-04-27** 公测。阿里图生视频模型。角色一致性强，运动质量高。
- [Qwen3.5 Max Pro](https://qwen.ai/) - 2026-04。高性能旗舰。
- [Qwen3.5 Omni Plus](https://qwen.ai/) - 2026-04。统一文本 + 图像输入的全模态基座。
- [Qwen3-Max-Thinking](https://qwen.ai/) - 阿里最强思维模型。1T+ 参数。
- [Qwen3.5-Omni](https://qwen.ai/) - 2026-03。完全全模态：文/视/听/动。113 种语言识别，256K 上下文。
- [Qwen3-Coder-Next](https://qwen.ai/) - 2026-02。开源编程 Agent 模型，MoE 80B 总 / 3B 激活。
- [Qwen3 235B-A22B](https://qwen.ai/) - 双模式推理 MoE。数学、代码、常识强。
- [Qwen2.5 Coder 32B](https://github.com/QwenLM/Qwen2.5-Coder) - 顶级开源编程模型。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FQwenLM%2FQwen2.5-Coder&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### xAI (Grok)

- [Grok 4.3 GA](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-grok-4-3-on-microsoft-foundry-latest-generation-agentic-capabilities/4517096) - 🆕 **2026-05**。Grok 4.3 在 Microsoft Foundry 与 OCI Generative AI 上 GA；xAI 面向 Agent 工作负载的旗舰，工具调用与长链推理能力升级。
- [Grok 4.3 Beta](https://x.ai/) - 🆕 2026-04。最新迭代，推理与编程基准提升，详见 [`2026.4` benchmark snapshot](https://benchlm.ai/)。
- [Grok 4.20](https://x.ai/) - 2026-02。多 Agent 系统（Heavy 模式 4 标准 + 16 专家 Agent），2M 上下文。
- [Grok 4 / 4 Heavy](https://x.ai/) - 2025-07 发布。3T 参数。
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

- [Command A](https://cohere.com/) - 🆕 2026-04 发布。111B 开源权重，256K 上下文。Agent / 多语言 / 编程聚焦。
- [Command R+](https://cohere.com/) - 企业级 RAG 模型，128K 上下文，10 种语言，带引用 grounded generation。
- [Command R](https://cohere.com/) - 经济型 RAG 模型。

### Baidu (ERNIE / 文心) 🇨🇳

- [ERNIE 5.0](https://yiyan.baidu.com/) - 🆕 2026-01 发布。2.4T MoE（每次激活 <3%）。原生全模态。LMArena 中文模型第一。
- [ERNIE 4.5](https://yiyan.baidu.com/) - 2025 多模态前作。中文与推理强。

### Zhipu AI / Z.ai (GLM) 🇨🇳

- [GLM-5.1](https://z.ai/blog/glm-5.1) - 🆕 **2026-04-07**。744B MoE / 40B 激活，200K 上下文。MIT。SWE-Bench Pro 第一。**完全在华为昇腾上训练，不依赖 NVIDIA**。
- [GLM-5 Reasoning](https://z.ai/) - 🆕 2026-04。BenchLM 85 —— **开源最高分**。SWE-Bench Pro 超过 GPT-5.4 与 Claude Opus 4.6。
- [GLM-5V-Turbo](https://z.ai/) - 🆕 2026-04。原生多模态 Agent —— 视觉、视频片段、文本输入。性价比平衡。
- [GLM-5](https://z.ai/) - 2026-02 发布。744B 参数，Agent 能力前沿。MIT。
- [GLM-4.7](https://z.ai/) - 2025 末发布。SWE-Bench 持平 Claude Opus 4。

### MiniMax 🇨🇳

- [MiniMax-M2.7 (开源权重)](https://www.minimax.io/) - 🆕 2026-04。1M+ 超长上下文。编程与 Agent 任务顶级表现。
- [MiniMax M2.7（闭源）](https://venturebeat.com/technology/new-minimax-m2-7-proprietary-ai-model-is-self-evolving-and-can-perform-30-50) - 🆕 **2026-03**。自演化闭源 LLM，针对 Agent 框架搭建、记忆更新、工作流迭代优化；SWE-bench 类任务大幅提升。
- [MiniMax M2.5](https://www.codemotion.com/magazine/ai-ml/minimax-m2-5-low-costs-high-performance/) - **2026-02**。230B 参数旗舰，主打 "真实世界生产力" 与高性价比。
- [Hailuo 02](https://aimlapi.com/blog/the-ultimate-guide-to-minimax-models-2026-m2-7-music-2-6-hailuo-video-advanced-tts) - 🆕 **2026-03**。原生 1080p 文/图生视频，训练语料显著扩充。
- [MiniMax Music 2.6](https://aimlapi.com/blog/the-ultimate-guide-to-minimax-models-2026-m2-7-music-2-6-hailuo-video-advanced-tts) - 🆕 **2026-04**。主打翻唱生成方向，低频还原显著改进；全球 beta。
- [MiniMax-M1-80k](https://www.minimax.io/) - 开源混合注意力推理模型。456B 参数，1M token 上下文。
- [Hailuo AI (视频)](https://hailuoai.video/) - 文生 / 图生视频，AI 主播 + 配音 + 角色一致性。
- [Kilo Code 集成](https://www.minimax.io/) - 🆕 MiniMax 为 Kilo Code（新 AI 编程编辑器）默认模型。

### Moonshot AI (Kimi) 🇨🇳

- [Kimi K2.6](https://kimi.ai/) - 🆕 **2026-04-20~21**。1T MoE / 32B 激活，256K 上下文。编程增强、长任务执行、**最大 1000 个 Agent 协作集群**。支持 `thinking.keep="all"` 持久推理。OpenClaw v2026.4.20+ 默认模型。
- [Kimi K2.5](https://kimi.ai/) - 2026-01 至 02。1T 总 / 32B 激活 MoE。原生多模态，最多 100 个并行子 Agent。开源。⚠️ **2026-05-25 停止支持**，请迁移到 K2.6。
- [Kimi Code](https://kimi.ai/) - 基于 K2.5/K2.6 的高级编程层，面向终端工作流。

### ByteDance (Doubao / 豆包) 🇨🇳

- [Doubao 2.0](https://www.taipeitimes.com/News/biz/archives/2026/02/16/2003852382) - 🆕 **2026-02**。面向 Agent 时代的升级，专注真实任务执行；驱动字节跳动多款消费级 AI 应用。
- [Seedance 2.0](https://economictimes.indiatimes.com/us/news/seedance-2-0-goes-live-as-bytedances-ai-videos-ignite-china-market-rally/articleshow/128150649.cms) - 🆕 **2026-02**。多模态电影级视频生成，2K 分辨率，比 Seedance 1.5 快约 30%。
- [Doubao-Seed-2.0 Pro](https://seed.bytedance.com/) - 🆕 2026-02 发布。前沿推理与复杂 Agent。和 GPT-5.2 同级，成本约低 90%。
- [Doubao-Seed-2.0 Lite](https://seed.bytedance.com/) - 🆕 通用生产负载。性能效率均衡。
- [Doubao-Seed-2.0 Code](https://seed.bytedance.com/) - 🆕 软件开发：代码生成、调试、评审。
- [BAGEL](https://github.com/bytedance-seed/BAGEL) - 🆕 字节开源多模态模型，文图视频统一理解 + 生成。

### Amazon (Nova)

- [Nova 2 Pro](https://aws.amazon.com/nova/) - 🆕 Amazon 最强推理模型。文 / 图 / 视频 / 语音输入。Agent 编程与长程规划。
- [Nova 2 Lite](https://aws.amazon.com/nova/) - 🆕 1M token 上下文 + 可调 "thinking effort"。
- [Nova 2 Sonic](https://aws.amazon.com/nova/) - 🆕 实时语音对语音模型。1M 上下文，多语言。
- [Nova Act](https://aws.amazon.com/nova/) - 🆕 浏览器 Web 任务 Agent 服务（Nova 2 Lite 驱动）。
- [Nova Forge](https://aws.amazon.com/nova/) - 🆕 自定义 Nova 训练服务。

### NVIDIA (Nemotron)

- [Nemotron 3 Ultra](https://developer.nvidia.com/nemotron) - 🆕 2026-03（GTC）。前沿推理，Blackwell 上 5 倍吞吐。
- [Nemotron 3 Super](https://developer.nvidia.com/nemotron) - 🆕 2026-03。120B 总 / 12B 激活。1M 上下文。
- [Nemotron 3 Nano](https://developer.nvidia.com/nemotron) - 经济型 Transformer-Mamba 混合 MoE。
- [Nemotron 3 Nano Omni](https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/) - 🆕 **2026-04-28**。30B-A3B 混合 MoE。原生多模态。同类开源 omni 模型 9 倍吞吐。霸榜 6 项排行（MMlongbench-Doc / OCRBenchV2 / WorldSense / DailyOmni / VoiceBench）。

### Tencent (Hunyuan) 🇨🇳

- [Hunyuan Hy3 Preview](https://hy.tencent.com/research/hy3) - 🆕 **2026-04-23**。295B 总 / 21B 激活 MoE，256K 上下文。GitHub / Hugging Face / ModelScope / GitCode 同步开源。"快慢思维融合" 架构，推理效率提升 40%。原生支持 vLLM 与 SGLang。腾讯元宝 / CodeBuddy / QQ / 腾讯文档已集成。OpenRouter 免费预览中。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTencent-Hunyuan%2FHunyuan-A13B&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Apple

- [Apple Foundation Models (AFM)](https://machinelearning.apple.com/research/introducing-apple-foundation-models) - 端侧（~3B）+ 服务器版本，Apple Intelligence 内核。隐私优先，离线可用。**WWDC 2026（6 月 8 日）**：下一代 AFM 与全新个性化 Siri 改由与 Google Gemini 联合开发；原本 Siri 中的第三方 ChatGPT 转发逐步退役，让位给 Gemini 驱动的 Apple Intelligence 栈。
- [OpenELM](https://machinelearning.apple.com/research/openelm) - 开源高效语言模型（270M~3B），Apple Silicon 端侧。

### Samsung

- [Samsung Gauss 2.3](https://www.samsung.com/) - 🆕 Galaxy S26 端侧 AI。Gauss 2.3 Think + Gauss O Flash 双变体。Agent 能力。

### StepFun 🇨🇳

- [Step 3.5 Flash](https://www.scmp.com/tech/article/3342222/punches-above-its-weight-compact-ai-model-chinas-stepfun-outshines-larger-rivals) - 🆕 **2026-02**。约 196B 参数的紧凑推理 + Agent 模型；以小搏大，对标更大体量的中国厂商旗舰。

### Baichuan 🇨🇳

- [Baichuan-M3 Plus](https://pandaily.com/baichuan-ai-launches-low-hallucination-medical-model-m3-plus-announces-free-access-program) - 🆕 **2026-01**。证据锚定的医疗 LLM，幻觉率显著降低；面向国内医疗机构提供免费 API。

### Inflection AI

- [Inflection 2.5 / Pi](https://inflection.ai/) - 偏共情对话的 AI，主打情绪感知与人本交互。

### 01.AI 🇨🇳

- [Yi-Lightning](https://www.01.ai/) - MoE，RTX 4090 上 200+ tokens/s。中英双语强，Apache 2.0。2024-10 发布。

### 中国科学院 🇨🇳

- [ScienceOne 100 / 磐石100](https://english.cas.cn/newsroom/cas-in-media/202604/t20260429_1158251.shtml) - 🆕 **2026-04-28~29**。中科院科研 AI 系统。"磐石" 基础模型 + 文献罗盘 + 创新评估引擎 + 2000+ 工具 Agent 工厂。覆盖数学 / 物理 / 生物 / 材料 / 天文 / 航天 / 地球科学。50+ 中科院研究所、100+ 科研场景使用。

---

## 🎨 多模态与生成式 AI

*生成与编辑图像、视频、音频、音乐的工具与模型。*

### 图像生成

- [Midjourney V8.1](https://en.wikipedia.org/wiki/Midjourney) - 🆕 **2026-04-30**。新增 2K 高清出图与新版 Raw 模式选项；V8（含 3D 生成）据传将于 2026 年晚些时候发布。
- [Flux 2 Pro / Flex / Dev / Klein](https://ropewalk.ai/blog/flux-2-ai-image-generation-2026) - 🆕 **2025-11**。Black Forest Labs 的下一代家族；SOTA 画质、多参考一致性，文本渲染显著提升。
- [Recraft V4](https://en.wikipedia.org/wiki/Recraft) - 🆕 **2026-02-17**。从零重构；提示准确度大幅改进；支持可编辑 SVG 矢量输出。
- [Kling IMAGE 3.0](https://klingaio.com/blogs/kling-3-release) - 🇨🇳 🆕 **2026-04-23**。快手出品的院线级原生 4K 图像生成。
- [Nano Banana 2 (Gemini 3 Pro Image)](https://deepmind.google/) - 🆕 Google 的透明背景友好图像模型；通过 OpenClaw image_generate 暴露使用。
- [ChatGPT Images 2.0](https://openai.com/) - 🆕 2026-04。免费层。细节、文字理解、迭代编辑增强。
- [gpt-image-2](https://openai.com/) - 🆕 OpenAI 最新图像 API。支持 2K/4K 提示。OpenClaw v2026.4.21 默认。
- [DALL·E 3](https://openai.com/dall-e-3) - 集成在 ChatGPT 中迭代生成。
- [Midjourney V7](https://www.midjourney.com/) - 仍是艺术风格生成第一梯队。
- [Stable Diffusion 3.5](https://stability.ai/) - 开源图像生成，连贯性与提示跟随增强。
- [Flux](https://github.com/black-forest-labs/flux) - 💤 **Stale**（2025-07 起无更新）。Black Forest Labs 开源模型。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fblack-forest-labs%2Fflux&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Ideogram 3.0](https://ideogram.ai/) - 文字渲染与设计向特别强。
- [Gemini 3 Pro Image](https://deepmind.google/technologies/gemini/) - Gemini 内原生图像生成。
- [Recraft V3](https://www.recraft.ai/) - 设计师向专业图像生成。
- [Seedance 2.0](https://seed.bytedance.com/) - 🇨🇳 🆕 字节下一代图像 / 动画生成 API。

### 视频生成

- [Runway Agent](https://chatlyai.app/news/runway-agent-launch-may-2026) - 🆕 **2026-05-13**。对话式 Agent，接过写好的脚本为你递交一段**多镜头完成品视频**：分镜脚本→生成→剪接→配音全路贯通，底层调用 Gen-4 / Gen-4 Turbo / Aleph 编辑。首个可用的「提示词到粗剪」产业级 Agent。
- [Sora 2 (via Runway)](https://runwayml.com/changelog) - 🆕 OpenAI 的 Sora 应用于 2026 年 4 月关停，但 Sora 2 Pro 已自 2026 年 4 月 7 日起集成进 Runway。
- [Kling VIDEO 3.0](https://kling.ai/) - 🇨🇳 🆕 快手出品。真人动作 + 嘴型 + 音画同步，最长 15 秒。
- [Hailuo AI](https://hailuoai.video/) - 🇨🇳 🆕 MiniMax 出品。文生 / 图生视频 + AI 主播 + 配音 + 角色一致性。
- [Veo 2](https://deepmind.google/technologies/veo/) - 🆕 Google DeepMind 高保真视频生成。
- [Runway Gen-4](https://runwayml.com/) - 🆕 专业视频生成与编辑，角色风格一致。
- [Pika 2.0](https://pika.art/) - 🆕 创意短视频，场景与特效控制。
- [LTX Studio](https://ltx.studio/) - 🆕 AI 电影化视频创作平台。
- [Tianma (天马) AI](https://www.alibabacloud.com/) - 🇨🇳 🆕 **2026-04-27** 公测。阿里图生视频。
- [Sora](https://openai.com/sora/) - ⚠️ *2026-04 关停*。OpenAI 文生视频模型，因成本与战略关停。

### 音频与音乐

- [ElevenLabs](https://elevenlabs.io/) - AI 语音合成 + 克隆 + 对话 AI 头部。
- [Suno V4](https://suno.com/) - 🆕 文本到音乐，高保真人声 + 配器。
- [Udio](https://www.udio.com/) - 🆕 商用级音乐生成。
- [OpenAI Audio Models](https://openai.com/) - GPT-4o 内的原生音频理解 + 生成。
- [Stability Audio](https://stability.ai/) - 开源音频音乐生成。
- [Bark](https://github.com/suno-ai/bark) - 💤 **Stale**（2024-08 起无更新）。开源文本到音频。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsuno-ai%2Fbark&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ElevenLabs Eleven v3 + ElevenAgents](https://elevenlabs.io/voice-agents) - 🆕 2026 年定位为 "互联网的音频层"——支持 70+ 语言、带情绪 Audio Tag 的 TTS，加上首个通过 AIUC-1 认证的 ElevenAgents 语音 Agent 平台，含多模态消息、会话主题发现、工具调用前的语音控制。
- [Cartesia Sonic 3 / 3.5](https://cartesia.ai/blog/introducing-line-for-voice-agents) - 🆕 **2026**。基于状态空间模型的 TTS，首音延迟约 40-90ms；驱动 2026 年 4 月发布的 **Line Agents** 语音 Agent 平台。
- [Deepgram Nova-3 + Aura-2 + Flux Multilingual](https://deepgram.com/learn/best-voice-ai-agents-2026-buyers-guide) - 🆕 **2026 年 4 月**。45+ 语言的 STT，TTS 延迟低于 200ms，会话式 STT 支持通话中 10 种语言的实时切换。
- [MiniMax Music 2.6](https://aimlapi.com/blog/the-ultimate-guide-to-minimax-models-2026-m2-7-music-2-6-hailuo-video-advanced-tts) - 🇨🇳 🆕 **2026 年 4 月**。主打翻唱生成方向，低频还原显著改进。
- [Voxtral TTS](https://www.forbes.com/sites/ronschmelzer/2026/03/26/mistral-releases-open-weight-voice-ai-built-for-speed/) - 🆕 **2026 年 3 月 26 日**。Mistral 开放权重的 4B TTS，专为语音 Agent 的低延迟而生。
- [Hume TADA](https://github.com/HumeAI/tada) - 🆕 **2026 年 3 月 10 日**。Hume AI 首个开源 TTS，MIT 许可。Text-Acoustic Dual Alignment 架构把文本 token 直接对齐到音频 token —— 测试中零转录错误，比同类快约 5×，支持 8 种语言，能在手机上跑。基于 Llama。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHumeAI%2Ftada&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🔗 Agent 协议与标准

*让 Agent 跨工具、跨框架互联互通的开放标准。*

### Model Context Protocol (MCP)

- [MCP Specification](https://modelcontextprotocol.io/) - 🆕 "AI 的 USB-C" —— Anthropic 主推、用于让 LLM 接入工具与数据源的开放协议。2025-12 捐赠给 Linux Foundation 旗下 Agentic AI Foundation。
- [MCP 2026-07 Release Candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) - 🆕 **2026 年 5 月发布，正式版计划 7 月 28 日上线**。MCP 下一大版升级候选版：**无状态协议核心**（可横向扩展、服务端更简单）、新增**扩展机制**、服务端渲染 UI 的 **MCP Apps**能力、Tasks 下沉为扩展、与 OAuth / OpenID Connect 对齐的授权强化。
- [MCP Servers](https://github.com/modelcontextprotocol/servers) - 官方参考 MCP 服务实现。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Fservers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - 官方 TypeScript SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Ftypescript-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - 官方 Python SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Fpython-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [mcp.so](https://mcp.so/) - 🆕 社区 MCP 服务目录。
- [mcp-gateway](https://github.com/Zijian-Ni/mcp-gateway) - MCP 网关，统一路由 / 认证 / 限流。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fmcp-gateway&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Agent-to-Agent Protocol (A2A)

- [A2A Protocol](https://github.com/google/A2A) - 🆕 Google 主导的 Agent 间通信开放标准。让不同框架的 Agent 互相发现、委派、协作。Linux Foundation 治理，2026 年已有 150+ 合作组织。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle%2FA2A&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [A2A Course (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/a2a-the-agent2agent-protocol/) - 🆕 免费课程：用 A2A 构建多 Agent 系统。

### 其他标准

- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - 🆕 [2026-04-15 大更新](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)：原生沙箱执行、MCP 一等公民、子 Agent / handoff 模式、Codex 风格文件系统工具，生产级多 Agent。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fopenai-agents-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agentic AI Foundation](https://www.linuxfoundation.org/) - 🆕 Linux Foundation 治理基金，由 Anthropic、Block、OpenAI 共同发起。
- [Coinbase Base MCP](https://fortune.com/2026/05/26/coinbase-pushes-further-into-ai-payments-with-new-mcp-for-base-network/) - 🆕 **2026 年 5 月 26 日**。Coinbase 为 Base 公链发布 MCP 服务器，让 Claude / Cursor / ChatGPT Agent 直接执行加密资产交易与借贷。首个交易所级、面向链上自动化的 MCP 端点。
- [Robinhood Agentic Trading MCP](https://robinhood.com/us/en/newsroom/robinhood-is-now-open-to-agents/) - 🆕 **2026 年 5 月 27 日**（beta）。首家通过 MCP 把股票交易开放给 AI Agent 的美国券商：Agent（Claude / Codex / Cursor）对账户只读，仅可在专门隔离的 Agentic 账户内交易；每笔交易推送，一键断开。

---

## 🏗️ Agent 框架

*用来构建自主 AI Agent 的框架与库。*

- [Koog 1.0](https://github.com/JetBrains/koog) - 🆕 **2026-05-28 · KotlinConf 2026**。JetBrains 针对 **Kotlin + Java** 的开源 Agent 框架进入稳定 1.0，并带有一年的 API 稳定性保证。Kotlin Multiplatform 跨端部署（JVM / Android / iOS / JS / WASM）、Java 互操作无需包装模块、Android 本地 LiteRT、OpenTelemetry 跨端可观测、图状工作流、Spring Boot / Ktor 集成，提供商 OpenAI / Anthropic / Google / Bedrock 均原生支持。Apache-2.0。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FJetBrains%2Fkoog&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangChain](https://github.com/langchain-ai/langchain) - 上下文感知推理应用的基础框架。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangGraph](https://github.com/langchain-ai/langgraph) - 把 Agent 建模为有状态、多 actor 协作的图。v0.3.19（2026-04-27）：预制 Agent 拆出 `langgraph-prebuilt` —— Supervisor / Swarm / LangMem / Trustcall。Agent 工作流的生产级标准。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flanggraph&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [CrewAI](https://github.com/crewAIInc/crewAI) - 角色扮演式 Agent 团队编排。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FcrewAIInc%2FcrewAI&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/) - 🆕 AutoGen + Semantic Kernel 合并的统一框架。多 Agent + 企业能力。2026 Q1 GA。
- [AutoGen](https://github.com/microsoft/autogen) - 微软多 Agent 对话框架（已并入 Microsoft Agent Framework）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fautogen&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Google Agent Development Kit (ADK)](https://github.com/google/adk-python) - 🆕 与 Gemini + Vertex AI 深度集成的模块化框架。层级 Agent 组合。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle%2Fadk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - 🆕 [2026-04-15 升级](https://openai.com/index/the-next-evolution-of-the-agents-sdk/) —— 原生沙箱、MCP、子 Agent handoff、Codex 文件操作。生产级多 Agent。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fopenai-agents-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MetaGPT](https://github.com/geekan/MetaGPT) - 🇨🇳 给 LLM 分配 SOP 软件团队角色（PM / 架构师 / 工程师）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgeekan%2FMetaGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Mastra](https://github.com/mastra-ai/mastra) - 🆕 TypeScript 优先的 Agent 框架，工作流驱动 + 内置可观测性。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmastra-ai%2Fmastra&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentGPT](https://github.com/reworkd/AgentGPT) - 📦 **Archived**（2025-04）。浏览器中部署 Agent。第一波代表项目，仅作历史参考。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Freworkd%2FAgentGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [BabyAGI](https://github.com/yoheinakajima/babyagi) - 用 LLM 创建、排序、执行任务的 AI 任务管理。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fyoheinakajima%2Fbabyagi&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) - 💤 **Stale**（2025-01 起无更新）。开源自主 Agent 框架。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTransformerOptimus%2FSuperAGI&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) - 把 LLM 嵌入应用。C# / Python / Java。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fsemantic-kernel&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Phidata (Agno)](https://github.com/phidatahq/phidata) - 多模态 Agent + 记忆 + 知识 + 工具 + 推理。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fphidatahq%2Fphidata&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [DSPy](https://github.com/stanfordnlp/dspy) - "编程而不是写 prompt" 的语言模型框架。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstanfordnlp%2Fdspy&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenClaw](https://github.com/openclaw/openclaw) - 🆕 个人 AI Agent 平台：技能、记忆、多渠道消息、Dreaming（三阶段记忆巩固）、Canvas / A2UI、ACP 编程 harness 集成、Standing Orders。**v2026.5.12**（2026-05-14）支持 Opus 4.7、Kimi K2.6、`/think xhigh`，新增 native model identity 注入、隔离 Telegram polling worker、MEMORY.md 自动压缩、protected config paths。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenclaw%2Fopenclaw&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Dify](https://github.com/langgenius/dify) - 🇨🇳 开源 LLM 应用开发平台 + 可视化 Agent 构建。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flanggenius%2Fdify&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Haystack Agents](https://github.com/deepset-ai/haystack) - 端到端 LLM 框架，Agent 流水线。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeepset-ai%2Fhaystack&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vellum AI](https://www.vellum.ai/) - 🆕 闭源 SaaS 生产级 Agent 框架：Prompt 构建 / 评测 / 版本 / 可观测性一体。
- [FastAgency](https://github.com/airtai/fastagency) - 🆕 高速推理 + 生产规模化框架。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fairtai%2Ffastagency&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Rasa](https://github.com/RasaHQ/rasa) - 强意图识别 + 对话管理的开源对话 AI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FRasaHQ%2Frasa&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Lindy](https://www.lindy.ai/) - 🆕 商务用户向无代码 Agent，可视化工作流。
- [Octomind](https://github.com/muvon/octomind) - 🆕 Rust 开源 AI Agent 运行时。多模型（13+），社区贡献的领域 Agent（开发 / 医疗 / 法律 / DevOps），支持 MCP 运行时自扩展。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmuvon%2Foctomind&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsoft AI Agent Governance Toolkit](https://www.helpnetsecurity.com/2026/04/03/microsoft-ai-agent-governance-toolkit/) - 🆕 **2026-04-03**。开源治理工具包，把运行时安全策略以策略即代码方式应用到 LangChain / AutoGen 等框架。
- [Bernstein](https://github.com/sipyourdrink-ltd/bernstein) - 🆕 Python 编排器，统一管理 40+ 个 CLI 编程 Agent（Claude Code、Codex、Gemini CLI、Cursor、Aider 等）。一次 LLM 计划调用后，调度、git worktree 隔离、质量闸门、HMAC 链式审计都是确定性的。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsipyourdrink-ltd%2Fbernstein&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Genkit Middleware](https://developers.googleblog.com/announcing-genkit-middleware-intercept-extend-and-harden-your-agentic-apps/) - 🆕 **2026-05-14**。Google 为开源 Genkit 框架增加中间件体系 —— 在 generate / model / tool 三层给出可组合 hooks：重试、模型降级、工具人工审批、SKILL.md 技能注入、限定范围的文件访问。先支持 TS / Go / Dart，Python 跟进中。
- [LlamaIndex ↔ Google Agents API 集成](https://www.kucoin.com/news/flash/google-launches-agents-api-llama-index-integrates-llamaparse-for-unstructured-document-processing) - 🆕 **2026-05-20**。LlamaIndex 为 Google 刚发布的 Agents API 交付模板，在沙箱化 Linux 环境里暴露 **LlamaParse** / **LiteParse** 处理非结构化文档；同期上线的还有沙箱运行时 **Sandboxed-Lit** 与面向 Agent 的首个 OCR 评测集 **ParseBench**。
- [Microsoft Agent 365](https://techcommunity.microsoft.com/blog/agent-365-blog/what%E2%80%99s-new-in-agent-365-may-2026/4516340) - 🆕 **2026 年 5 月 1 日 GA**。面向 AI Agent 的企业级可观测、治理与安全平台；2026 年 5 月更新加入面向 Agent 的 SASE、威胁检测/阻断与 Agent 威胁狩猎工作流。
- [Ontheia](https://github.com/Ontheia/ontheia) - 自托管开源 AI Agent 平台。多模型供应商（Claude / OpenAI / Gemini / Ollama），原生支持 MCP，Chain Engine 可视化工作流编排，长期记忆（pgvector），多用户 RBAC，架构层面合规 GDPR。AGPL-3.0。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOntheia%2Fontheia&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Coze Studio](https://github.com/coze-dev/coze-studio) - 🆕 🇨🇳 字节跳动开源的 AI Agent 开发平台——一体化可视化工具，简化 Agent 的创建、调试、部署。Apache-2.0，20K+ stars；Coze.com 的开源对照版。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🛠️ Agent IDE 与可视化构建器

*用来设计、调试、上线 Agent 工作流的可视化（或低代码）环境。*

- [LangGraph Studio](https://www.langchain.com/langgraph) - LangGraph 的可视化调试器：步进状态、回放回合、中途改写消息。
- [Dify](https://github.com/langgenius/dify) - 🇨🇳 拖拽式 Agent 工作流构建。生产级使用最广。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flanggenius%2Fdify&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agenta](https://github.com/agenta-ai/agenta) - 🆕 一体化 LLMOps：prompt playground + 管理 + 评测 + 可观测性。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagenta-ai%2Fagenta&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vellum AI](https://www.vellum.ai/) - 闭源 SaaS。
- [Cozeloop](https://github.com/coze-dev/cozeloop) - 🇨🇳 🆕 字节 Coze 团队开源的 Agent 优化平台。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcozeloop&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
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
- [Mem0](https://github.com/mem0ai/mem0) - LLM 应用的自我提升记忆层。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmem0ai%2Fmem0&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Zep](https://github.com/getzep/zep) - AI 助理与 Agent 的长期记忆。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgetzep%2Fzep&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [agent-memory](https://github.com/Zijian-Ni/agent-memory) - 跨会话上下文持久化的轻量 Agent 记忆框架。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fagent-memory&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangMem](https://github.com/langchain-ai/langmem) - 🆕 从 LangGraph 0.3.19（2026 年 4 月）拆出的独立库；为 Agent 提供长期情景记忆 + 程序性记忆原语。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangmem&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Motorhead](https://github.com/getmetal/motorhead) - 💤 **Stale**（2025-07 起无更新）。LLM 的记忆 + 上下文管理服务。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgetmetal%2Fmotorhead&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ChromaDB](https://github.com/chroma-core/chroma) - AI 原生开源向量数据库。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fchroma-core%2Fchroma&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cognee](https://github.com/topoteretes/cognee) - 用图 + LLM + 向量检索得到确定性输出。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftopoteretes%2Fcognee&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangGraph Memory](https://github.com/langchain-ai/langgraph) - 🆕 LangGraph 内置的持久化与 checkpoint。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flanggraph&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Graphiti](https://github.com/getzep/graphiti) - 🆕 时序感知的知识图记忆。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgetzep%2Fgraphiti&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude Managed Agents Memory](https://platform.claude.com/docs/en/release-notes/overview) - 🆕 **2026-04-23** 公测。把读写记忆挂载到 Agent 文件系统，实现跨会话学习。
- [Mem0g (graph variant)](https://mem0.ai/blog/state-of-ai-agent-memory-2026) - 🆕 Mem0 的图增强姊妹版，擅长多跳问答；截至 2026 年初已有 21+ 框架集成。
- [OpenViking](https://github.com/volcengine/OpenViking) - 🆕 🇨🇳 字节火山引擎开源的 Agent 上下文数据库（适配 OpenClaw 等）。用文件系统范式统一管理记忆、资源与技能，实现分层上下文交付与自演化。AGPL-3.0，25K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvolcengine%2FOpenViking&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ReMe](https://github.com/agentscope-ai/ReMe) - 🆕 🇨🇳 阿里 AgentScope 出品的 Agent 记忆管理工具包——文件系记忆 + 向量记忆双轨，专门处理上下文窗口受限与无状态会话两大痛点。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentscope-ai%2FReMe&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [taOSmd](https://github.com/jaylfc/taosmd) - 🆕 ⚠️ **Unverified.** 本地优先、基于追加式转录的 Agent 记忆：类型化时序知识图（修正后的新事实自动覆盖旧事实）+ 向量与 BM25 混合检索。面向小型本地模型调优，完全离线（8 GB 单板机即可运行）。作者声称 LongMemEval-S 端到端 Judge 97%；单作者维护，审核时 44 stars，基准可按 `docs/benchmarks.md` 复现。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fjaylfc%2Ftaosmd&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🔌 工具与 API 集成

*让 Agent 接入外部服务与 API 的协议与工具。*

- [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol/servers) - 工具调用的事实标准。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Fservers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [mcp-gateway](https://github.com/Zijian-Ni/mcp-gateway) - MCP 网关。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fmcp-gateway&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Composio](https://github.com/ComposioHQ/composio) - 150+ 工具 + 托管认证一体化 Agent 集成平台。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FComposioHQ%2Fcomposio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Toolhouse](https://toolhouse.ai/) - AI 工具云：存储、管理、执行工具。
- [LangChain Tools](https://github.com/langchain-ai/langchain) - LangChain 生态广泛的工具集成。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Arcade AI](https://github.com/ArcadeAI/arcade-ai) - AI Agent 工具调用平台。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FArcadeAI%2Farcade-ai&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [E2B](https://github.com/e2b-dev/e2b) - AI Agent 的开源云沙箱。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fe2b-dev%2Fe2b&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Browser Use](https://github.com/browser-use/browser-use) - 让 AI Agent 操控浏览器。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowser-use%2Fbrowser-use&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Firecrawl](https://github.com/mendableai/firecrawl) - 🆕 把网站变成 LLM-ready 数据。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmendableai%2Ffirecrawl&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Crawl4AI](https://github.com/unclecode/crawl4ai) - 🆕 LLM 友好的开源爬虫。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Funclecode%2Fcrawl4ai&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Stagehand](https://github.com/browserbase/stagehand) - 🆕 Browserbase 出品的 AI 浏览器自动化。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowserbase%2Fstagehand&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentQL](https://www.agentql.com/) - 🆕 用语义化查询语言操控网页。
- [StackOne](https://www.stackone.com/) - 🆕 HR / CRM / ATS 统一 API。
- [The Colony](https://thecolony.cc) - ⚠️ **Unverified**。自称 Agent 间社交网络 + REST API + Python / TS / Go SDK + MCP server。组织与 SDK 仓库均 <30 天，0~2 star，单维护者；同款 PR 投了 15+ 个 awesome 列表。**仅作可见性收录**，使用前请自行评估。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTheColonyCC%2Fcolony-sdk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AWS MCP Server](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/) - 🆕 **2026 年 5 月 6 日 GA**。AWS 官方托管的 MCP 服务器，让编码 Agent 安全可审计地调用任意 AWS API；多步操作可在沙箱化 Python 环境中执行，用 agent skills 取代传统 "agent SOP"。AWS 第一方出品。
- [Google Workspace MCP Server](https://workspaceupdates.googleblog.com/2026/05/agent-tools-and-security-updates-for-workspace-developers.html) - 🆕 **2026 年 5 月 1 日起逐步上线**。Workspace 原生 MCP 服务器，将 Gmail / Drive / Calendar / Docs / Sheets 暴露给 MCP 客户端，OAuth 范围由管理员控制并带审计日志。
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

---

## 🛡️ Agent 安全

*抵御 prompt 注入、数据泄漏、滥用的工具与框架。*

- [prompt-firewall](https://github.com/Zijian-Ni/prompt-firewall) - LLM prompt 防火墙：检测 + 拦截注入。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fprompt-firewall&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LLM Guard](https://github.com/protectai/llm-guard) - LLM 输入输出扫描安全工具包。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fprotectai%2Fllm-guard&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Rebuff](https://github.com/protectai/rebuff) - 📦 **Archived**（2024-08）。自我加固 prompt 注入检测器。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fprotectai%2Frebuff&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
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
- [PyRIT](https://github.com/Azure/PyRIT) - 微软自动化红队框架。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAzure%2FPyRIT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAMPART](https://github.com/microsoft/RAMPART) - 🆕 **2026 年 5 月 20 日**。Microsoft 出品的 pytest 原生、面向 Agentic AI 的安全/可靠性测试框架。开发者侧白盒，与 PyRIT 互补——跨提示注入探针、良性失败断言、危害类别覆盖、统计阈值（如 80%+ 的运行需达到安全标准）。可直接接入 CI/CD。MIT。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2FRAMPART&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Clarity (Microsoft)](https://www.microsoft.com/en-us/security/blog/2026/05/20/introducing-rampart-and-clarity-open-source-tools-to-bring-safety-into-agent-development-workflow/) - 🆕 **2026 年 5 月 20 日**。RAMPART 的姊妹工具。AI Agent 的结构化设计评审工具——在写代码前生成关于意图、风险与行为的 "living artifacts"。Microsoft AI Red Team 的内部实践开源版。
- [MCP Gateway & Registry](https://github.com/agentic-community/mcp-gateway-registry) - 🆕 企业级 MCP 网关与注册中心：集中托管 AI 开发工具，OAuth 认证、动态工具发现、审计链、Keycloak / Entra 集成。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentic-community%2Fmcp-gateway-registry&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangSmith Sandboxes](https://www.langchain.com/blog/interrupt-2026-overview) - 🆕 **2026 年 5 月（Interrupt 2026）**。LangChain 托管的 Agent 安全代码执行环境——文件系统、shell、包管理、持久态、网络隔离。与 LangSmith Engine、Managed Deep Agents 同期发布。
- [Nobulex](https://github.com/arian-gogani/nobulex) - ⚠️ **未验证。** AI Agent 行为的密码学回执（Ed25519 双签名 + 哈希链审计日志）。MIT。其双向回执原语已 [合并](https://github.com/microsoft/agent-governance-toolkit/pull/1333) 进 Microsoft Agent Governance Toolkit（PR #1302、#1333）。同一份投稿同期发往 15+ awesome list；提交者宣称的 "4,500 npm 月下载" 与 registry 实际数据不符（`@nobulex/mcp-server` 审计时仅约 19/月）。基于 Microsoft 的采用列入，仅作可见度参考，依赖前请自行评估。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Farian-gogani%2Fnobulex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🔍 RAG 与知识库

*Agent 的检索增强生成与知识管理系统。*

- [LlamaIndex](https://github.com/run-llama/llama_index) - LLM 应用的数据框架：摄取 / 结构化 / 访问私有数据。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Frun-llama%2Fllama_index&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangChain Retrievers](https://github.com/langchain-ai/langchain) - LangChain 的检索器与文档加载器集合。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Haystack](https://github.com/deepset-ai/haystack) - 端到端 RAG。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeepset-ai%2Fhaystack&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Unstructured](https://github.com/Unstructured-IO/unstructured) - 文档预处理与提取。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FUnstructured-IO%2Funstructured&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Weaviate](https://github.com/weaviate/weaviate) - 开源向量数据库。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fweaviate%2Fweaviate&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Qdrant](https://github.com/qdrant/qdrant) - Rust 实现的高性能向量搜索。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fqdrant%2Fqdrant&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Milvus](https://github.com/milvus-io/milvus) - 大规模向量数据库。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmilvus-io%2Fmilvus&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Pinecone](https://www.pinecone.io/) - 托管向量数据库 SaaS。
- [Chroma](https://github.com/chroma-core/chroma) - AI 原生开源向量数据库。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fchroma-core%2Fchroma&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vanna](https://github.com/vanna-ai/vanna) - 📦 **Archived**（2026-02）。RAG-for-SQL：自然语言对话数据库。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvanna-ai%2Fvanna&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LightRAG](https://github.com/HKUDS/LightRAG) - 🇨🇳 港大 HKUDS 的图式 RAG。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2FLightRAG&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Docling](https://github.com/DS4SD/docling) - IBM 文档转换工具，PDF / DOCX / HTML 等。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FDS4SD%2Fdocling&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Kotaemon](https://github.com/Cinnamon/kotaemon) - 开源 RAG UI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FCinnamon%2Fkotaemon&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [R2R](https://github.com/SciPhi-AI/R2R) - 端到端 RAG 服务，企业级。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSciPhi-AI%2FR2R&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAGFlow](https://github.com/infiniflow/ragflow) - 🇨🇳 深度文档理解 RAG。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Finfiniflow%2Fragflow&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Morphik](https://github.com/morphik-org/morphik-core) - 🆕 面向包含表格、图表的多模态文档的 RAG 引擎；2026 年快速崛起，是处理复杂 PDF 的 LlamaIndex 替代方案。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmorphik-org%2Fmorphik-core&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cognee](https://github.com/topoteretes/cognee) - 🆕 在 Agent 摄取文档过程中实时构建知识图谱的记忆 + 推理引擎；2026 年长时研究型 Agent 栈的热门选择。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftopoteretes%2Fcognee&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAG-Anything](https://github.com/HKUDS/RAG-Anything) - 🆕 港大数据科学实验室出品的一体化多模态 RAG 框架。基于 LightRAG 构建；文本与多模态并行流水线；可查询同时包含文本、图示、表格、公式的文档。MIT，21K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2FRAG-Anything&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 💻 编程 Agent

### 终端 / CLI Agent

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - 直接在终端里运行的 Agent 编程工具。Opus 4.7 + `/think xhigh`。SWE-bench 80.9%。
- [Codex CLI](https://github.com/openai/codex) - OpenAI 出品，开源终端编程 Agent。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fcodex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Codex Security](https://developers.openai.com/codex/changelog) - 🆕 **2026 年 3 月**。应用安全 Agent，负责发现并修复软件漏洞；OSS 维护者可通过 Codex-for-OSS 计划使用。
- [Aider](https://github.com/Aider-AI/aider) - Git-aware 终端 AI 编程伙伴。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAider-AI%2Faider&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Goose](https://github.com/block/goose) - Block 出品的开源 Agent 编程 CLI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fblock%2Fgoose&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) - 🆕 Google 的终端优先编码 Agent，擅长大上下文重构。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle-gemini%2Fgemini-cli&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenCode](https://github.com/opencode-ai/opencode) - 🆕 开源终端优先编码 Agent，内置原生 TUI。支持 OpenAI、Claude、Gemini、Ollama 等模型以及代码智能提示 (LSP)。基于 Go，架构解耦。MIT。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopencode-ai%2Fopencode&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Grok Build](https://x.ai/news/grok-build-cli) - 🆕 **2026 年 5 月 14 日（早期 beta）**。xAI 的 Agent 化 CLI 编码工具，由 **grok-code-fast-1** 驱动。子 Agent 并行运行于隔离环境，每日发布 release notes，仅 SuperGrok Heavy 订阅可用（首 6 个月每月 99 美元，之后 300 美元）。xAI 对 Claude Code / Codex CLI 的正面回应。
- [Antigravity CLI](https://antigravity.google/blog/introducing-google-antigravity-2-0) - 🆕 **2026 年 5 月 19 日（Google I/O 2026）**。Antigravity 2.0 的轻量 CLI 伴侣——直接从终端创建并使用 Google 的 Agent harness。支持 macOS / Linux / Windows。**2026 年 6 月 18 日起接替 Gemini CLI**（Free / Pro / Ultra 用户）。
- [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code) - 🆕 🇨🇳 **2026 年 6 月 6 日**。Moonshot AI 的终端编程 Agent（TypeScript，MIT）。内置 coder / explore / plan 子 Agent 在隔离上下文中运行，通过 `/mcp-config` 对话式配置 MCP。npm 安装。专为下一代 Kimi K2.6 Agent 设计。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FMoonshotAI%2Fkimi-code&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MAI-Code-1-Flash in GitHub Copilot](https://microsoft.ai/news/introducingmai-code-1-flash/) - 🆕 **Build 2026（2026 年 6 月 2 日）**。微软首个 100% 自研的 5B 编程模型作为 GitHub Copilot 的模型选项落地——在四大核心编程基准上击败 Claude Haiku 4.5（SWE-Bench Pro 51.2% vs 35.2%），成本显著更低。

### IDE Agent

- [Cursor 3.09](https://www.cursor.com/) - 🆕 2026-04-03 更新。Agent 模式增强，支持 Vibe Coding。
- [Kilo Code](https://www.kilocode.com/) - 🇨🇳 🆕 2026-04 中文社区流行的 Cursor 替代。默认 MiniMax 模型。
- [Cursor](https://www.cursor.com/) - 2026-02 更新支持 8 个并行 Agent。
- [Windsurf](https://codeium.com/windsurf) - Codeium 的 Agent 化 IDE。
- [Cline](https://github.com/cline/cline) - VS Code 自主编程 Agent。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcline%2Fcline&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Continue](https://github.com/continuedev/continue) - 开源 AI 编程助手（VS Code + JetBrains）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcontinuedev%2Fcontinue&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Roo Code](https://roocode.com/) - 🆕 开源 VS Code 扩展，跨多文件读写、执行命令，model-agnostic；除自带 API 外免费。
- [Void](https://github.com/voideditor/void) - 🆕 VS Code 的开源 fork，定位为开源版 Cursor；数据留在本地，自带模型。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvoideditor%2Fvoid&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [GitHub Copilot](https://github.com/features/copilot) - 2026 初支持 Agent 模式，`gh copilot` 终端集成。
- [Kiro](https://kiro.dev/) - AWS 自主 Agent。Spec-driven，最多 10 个并发任务。
- [Amazon Q Developer](https://aws.amazon.com/q/developer/) - AWS 生态深度集成。
- [Visual Studio 2026 Agent Mode + Skills](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/) - 🆕 **VS 2026 Insiders 2026-05-12 – 15**。Copilot Chat "Agent Mode" 现在能在 Visual Studio 2026 里发现、管理、创建可复用的 Copilot Skill，能看到整个解决方案的上下文，还能执行终端命令与调用外部工具。
- [JetBrains Rider AI Test-Writing Skill](https://blog.jetbrains.com/dotnet/2026/05/22/claude-codex-ai-agent-skill-for-writing-tests/) - 🆕 **2026 年 5 月 22 日**。JetBrains Rider 新增的 AI Assistant skill，把 .NET 代码覆盖率数据喂给 Claude Code / Codex，让 Agent 聚焦未覆盖分支，降低测试生成的 AI 成本。

### 自主软件工程师

- [Cursor 3.4 云 Agent 环境](https://cursor.com/changelog) - 🆕 **2026-05-13**。为云上 Agent / 自动化提供多仓库环境、带 build secrets 的 Dockerfile 配置、快 70% 的镜像层缓存、每个环境独立的版本历史 + 回滚、审计日志、限定范围的出网 / secrets。
- [Devin 3.0](https://www.cognition.ai/) - 🆕 Cognition。动态重新规划、自愈代码、遗留代码迁移。多模态输入（UI 截图、视频）。
- [Devin 2.2](https://cognition.ai/blog/introducing-devin-2-2) - 🆕 **2026 年 2 月**。沙箱化 terminal + editor + browser；商业化产品（Core 20 美元/月，Team 500 美元/月）。
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) - 自托管的开源 Agent 软件开发平台。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAll-Hands-AI%2FOpenHands&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SWE-agent](https://github.com/SWE-agent/SWE-agent) - 把 LLM 变成能修复 GitHub issue 的工程师。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSWE-agent%2FSWE-agent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Devika](https://github.com/stitionai/devika) - 💤 **Stale**（2025-09 起无更新）。开源 Devin 替代。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstitionai%2Fdevika&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [GPT Engineer](https://github.com/gpt-engineer-org/gpt-engineer) - 📦 **Archived**（2025-05）。第一波自主编程项目，仅作历史参考。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgpt-engineer-org%2Fgpt-engineer&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Codegen](https://github.com/codegen-sh/codegen-sdk) - 🆕 程序化代码操作 + 跨文件重构 SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcodegen-sh%2Fcodegen-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Qodo](https://www.qodo.ai/) - 🆕 AI 代码评审平台：质量 + 安全 + 测试生成。
- [Google Antigravity 2.0](https://antigravity.google/blog/introducing-google-antigravity-2-0) - 🆕 **2026 年 5 月 19 日（Google I/O 2026）**。独立桌面应用（macOS / Linux / Windows），可并行编排多个 Agent。新增 cron 化的定时任务、长跑异步任务、动态子 Agent，以及与 AI Studio / Android / Firebase 的集成。配套的 **Antigravity SDK** 支持自部署 harness；企业版集成进 Gemini Enterprise Agent Platform。

---

## 🤖 Physical AI / 具身智能

*能感知、推理、在物理世界中行动的 AI —— 人形机器人、工厂自动化、Physical AI 基础设施。继语言 Agent 之后的下一波。*

### 基础模型与研究

- [Google Gemini Robotics ER-1.6](https://deepmind.google/) - 🆕 2026-04-14。机器人 AI，空间与物理推理增强。Agile Robotics 实地部署。
- [Project Prometheus (Bezos)](https://www.reuters.com/) - 🆕 贝佐斯主导的 Physical AI 项目。$10B / $38B 估值融资。
- [NVIDIA Isaac GR00T](https://developer.nvidia.com/isaac/gr00t) - 人形机器人基础模型平台。GTC 发布、Hannover Messe 2026 扩展。
- [NVIDIA Industrial AI Cloud](https://nvidianews.nvidia.com/) - 🆕 2026-04（Hannover Messe）。德国电信合建 AI factory。

### 人形机器人

- [Tesla Optimus Gen3](https://www.tesla.com/) - 🆕 2026 夏季量产。
- [Figure 04](https://autonews.gasgoo.com/articles/news/figure-founder-f04-robot-initiates-component-delivery-process-2054560059634376705) - 🆕 **2026-05-13**。Brett Adcock 宕告 Figure 04 设计定型，零部件已开始交付，使用 Helix VLA 型号。
- [Helix 02 包裹分拧 72h 运行](https://www.businessinsider.com/figure-ai-turned-a-humanoid-sorting-packages-must-see-tv-2026-5) - 🆕 **2026-05-13 – 16**。Figure F.03 机器人队靠 Helix 02 完全自主在包裹分拧线上运行：首天 8 小时 ~22K 包裹，24 小时 ↑到 ~30K，压力测试下约 72 小时 ~88K 包裹后出现机械故障。首份公开的家用型人形机器人连续作业证据。
- [Figure F.03 vs 人类 8 小时分拧挑战](https://incrypted.com/en/figure-ai-held-a-human-vs-robot-marathon/) - 🆕 **2026-05-18**。Figure 首场公开的人机对决：在同一条分拧线上，人类员工以 12,924 件（2.79 秒 / 件）势均微赢 F.03 机器人的 12,732 件（2.83 秒 / 件）。这是到目前为止公开资料中人与机器在实际产业任务上最贴近的一次。
- [Boston Dynamics Atlas 100 磅操作 + 现代集团 25K 刷屏计划](https://www.techtimes.com/articles/316854/20260519/boston-dynamics-reveals-how-atlas-learned-lift-100-pound-loads-hyundai-plans-30000-per-year.htm) - 🆕 **2026-05-18 / 19**。Boston Dynamics 发布视频与技术博文，展示 Atlas 通过强化学习 + 大规模仿真能举起并携带 **超 100 磅**负荷（冰箱 / 洗衣机），全身控制能适应重量转移，不依赖逐件识别。现代汽车集团承诺从 2028 年起在 Hyundai/Kia 工厂部署 **25,000+ 台 Atlas**。
- [Unitree G1 进驻 JAL 羽田机场](https://www.techtimes.com/articles/316862/20260519/jal-deploys-unitree-g1-robots-haneda-us-congress-moves-blacklist-supplier-national-security.htm) - 🆕 **2026-05**。日本航空在羽田启动地面运作试点（行李装卸 / 集装箱运输 / 机舱清洁），官方定义为 **全球首家在运营航空业务中录用双足机器人**的航司。同一周美国国会推动将 Unitree 列入实体清单，embodied AI 供应链加速地缘政治化。
- [Honour (荣耀) Humanoid](https://www.honor.com/) - 🇨🇳 🆕 2026 年人形半马世界纪录。
- [Zhiyuan (智元) AGIBOT](https://www.agibot.com/) - 🇨🇳 🆕 2026-04 新本体 + 基模 + 解决方案。把 2026 称为 "Deployment Year Zero"。
- [Unitree H 系列](https://www.unitree.com/) - 🇨🇳 国产 Boston Dynamics 对手，2026 持续迭代。
- [Agile Robotics](https://www.agile-robots.com/) - 🆕 Gemini Robotics ER-1.6 部署伙伴。德国机器人公司。
- [Shenzhen Humanoid Pilot Line](https://www.chinadailyhk.com/hk/article/631892) - 🇨🇳 🆕 **2026-04-12** 首条人形机器人中试线（深圳乐聚 + 东方精工）。2 小时一台，年 500~1000 台。佛山 1 万台 / 年大规模工厂同步规划中。

### 消费级机器人 / 可穿戴

- [Doubao AI Glasses (字节)](https://seed.bytedance.com/) - 🇨🇳 🆕 2026 Q2。实时翻译 + 物体识别 + 豆包 LLM。
- [Nothing AI Glasses/Earbuds](https://nothing.tech/) - 🆕 2026-04 公布。
- [Samsung Galaxy S26 (Gauss 2.3)](https://www.samsung.com/) - 端侧 Agent。
- [Meta Ray-Ban Stories 3](https://www.meta.com/) - Llama 集成深化。

### 自动驾驶

- [Tesla FSD v13](https://www.tesla.com/) - L4 部署扩展。
- [Waymo](https://waymo.com/) - 美国多城市 L4 商业化推进。
- [WeRide / Pony.ai / Baidu Apollo](https://www.weride.ai/) - 🇨🇳 中国 L4 车队扩区。
- [Tesla Optimus Gen3 (V3)](https://www.teslarati.com/tesla-optimus-awe-2026-shanghai/) - 🆕 **AWE 2026 上海首秀**。首款量产 Optimus；Fremont 产线 2026 年 1 月启动，初期目标 5-10 万台/年，初始售价约 3 万美元，2026 年底开放小批量外部销售。37 关节，1.2 m/s 步速，22 自由度手部。
- [Figure 03 (Helix AI)](https://blog.robozaps.com/b/figure-03-review) - 🆕 **2025 年末发布，2026 年量产爬坡**。Figure 首款专为家用设计的型号：柔性纺织外壳、无线充电、触觉传感。2026 年 5 月演示：两台 F.03 仅靠视觉协作，2 分钟内自主完成清扫房间和铺床。
- [Figure 02 + Helix 02](https://en.wikipedia.org/wiki/Figure_AI) - 🆕 **2026 年 1 月**。Helix 02 扩展了全身自主能力（装卸洗碗机、叠衣服）；BotQ 工厂额定年产能 1.2 万台。
- [Unitree G1 + H1-2](https://community.robotshop.com/blog/show/unitree-robotics-at-ces-2026-a-clear-signal-of-whats-coming-next) - 🆕 **CES 2026**。G1 跳舞 / 拳击 / 滑冰演示，2 月放出自主功夫展示；5'8" 的 H1-2 工业版可达 7.4 mph。宇树 2026 年人形出货目标 2 万台。
- [Unitree R1 Air](https://www.eweek.com/news/chinese-unitree-g1-humanoid-robot-skates-spins-flips-apac/) - 🆕 消费级人形机器人，售价 **4,900 美元**——能跑、翻滚、倒立行走。
- [Unitree Gen 2 (lifelike skin)](https://www.youtube.com/watch?v=Gmp82MuTFsM) - 🆕 拟真人造皮肤，内嵌压力 / 温度 / 触觉传感器。
- [Unitree GD01](https://www.extremetech.com/computing/unitree-will-sell-you-a-personal-mecha-robot-for-650000) - 🆕 **2026 年 5 月**。接近 10 英尺的载人机甲；驾驶员操控，可在双足与四足模式切换。售价人民币 390 万元起（约 65 万美元）。预示具身 Agent 栈开始向操作员驾驶形态分叉。
- [1X NEO（消费级人形机器人）](https://www.1x.tech/discover/neo-home-robot) - 🆕 **2026 年 2 月 26 日开放预订**，首批美国家庭交付于 2026 年。5'6"/66 磅家庭人形，22 自由度灵巧手、柔体外壳、4 小时续航、机载 LLM、噪音约 22dB。早鸟价 20,000 美元 + 200 美元定金，或 499 美元/月订阅。隐私 "no-go" 区域与人脸模糊内置。首款真正交付家庭的消费级人形。

---

## 🎮 Agent 仿真与世界模型

*Agent 在仿真世界中训练、观察、应力测试的研究环境。世界模型 / 具身研究渗透到语言 Agent 设计中后越来越重要。*

- [Generative Agents](https://github.com/joonspk-research/generative_agents) - 💤 斯坦福经典 *Smallville*（Park et al., 2023）。25 个 LLM 角色 + 记忆 + 反思 + 计划。后续多 Agent 论文几乎都借鉴此实现。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fjoonspk-research%2Fgenerative_agents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Voyager](https://github.com/MineDojo/Voyager) - 💤 Minecraft 终生学习 Agent —— GPT-4 + skill library + curriculum（Wang et al., 2023）。开放式 Agent 评测的经典。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FMineDojo%2FVoyager&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SWE-Gym](https://github.com/SWE-Gym/SWE-Gym) - 用真实 GitHub issue 训练 SWE Agent 的开放环境，SWE-bench 配套。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSWE-Gym%2FSWE-Gym&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [WebArena](https://webarena.dev/) - 真实可复现的 Web 环境（Reddit / 购物 / GitLab 克隆），OSWorld 与多数浏览器 Agent 论文使用。
- [WorkArena](https://github.com/ServiceNow/WorkArena) - ServiceNow 出品的企业工作场景 Web Agent 基准。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FServiceNow%2FWorkArena&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Genie 3 / Genie 4](https://deepmind.google/) - Google DeepMind 可玩 3D 世界模型，从 prompt 生成。闭源研究。
- [NVIDIA Cosmos](https://github.com/nvidia-cosmos/cosmos-predict1) - 具身 AI / 机器人的世界模型基础，生成物理合理的视频未来。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fnvidia-cosmos%2Fcosmos-predict1&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Snowflake Agent World Model (AWM)](https://github.com/Snowflake-Labs/agent-world-model) - 🆕 **2026 年 2 月 10 日开源，5 月 1 日被 ICML 2026 接收**。合成环境生成流水线，一次性产出 1,000 个可执行的、SQL 数据库驱动的工具调用环境（35K+ 工具，10K 任务），通过统一 MCP 接口暴露——支持大规模多回合 Agent RL。基础设施已合入 `meta-pytorch/OpenEnv`。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSnowflake-Labs%2Fagent-world-model&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 📊 评测与 Leaderboard

*跟踪前沿 AI 能力的标准评测套件与实时榜单。*

- [BenchLM](https://benchlm.ai/) - 🆕 多家基准聚合榜单。2026-04 榜首：Claude Mythos 99，Gemini 3.1 Pro / GPT-5.4 并列 94，Claude Opus 4.6 / GPT-5.4 Pro 92，GLM-5 Reasoning 85（开源最高）。
- [SWE-bench Verified](https://www.swebench.com/) - 真实 GitHub issue 修复基准。2026-04 榜首：Claude Mythos 93.9%，Claude Opus 4.7 87.6%。
- [GPQA Diamond](https://github.com/idavidrein/gpqa) - 💤 数据集仓 2024-09 起无更新。专家级科学推理。2026-04 榜首：Gemini 3.1 Pro 94.3%（世界纪录）、Claude Opus 4.7 94.2%。
- [ARC-AGI 2](https://arcprize.org/) - 抽象推理。Gemini 3.1 Pro 77.1%。
- [OSWorld](https://os-world.github.io/) - 桌面 GUI 操作。GPT-5.4 75%（超过人类基线）。
- [LMArena](https://lmarena.ai/)（前 Chatbot Arena） - 众包对话偏好。Opus 4.6 当前领先。
- [MMLU-Pro](https://github.com/TIGER-AI-Lab/MMLU-Pro) - MMLU 加难版。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTIGER-AI-Lab%2FMMLU-Pro&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LiveCodeBench](https://livecodebench.github.io/) - 持续更新的竞赛风编程基准。
- [AIME 2025 / Humanity's Last Exam (HLE)](https://agi.safe.ai/) - 数学 / 博士级综合推理。
- [Terminal-Bench](https://www.tbench.ai/) - CLI Agent 评测。Codex CLI 77.3%。
- [Wolfram LLM Benchmarking Project](https://www.wolfram.com/llm-benchmarking-project/) - 英文规格 → Wolfram Language 代码生成。
- [GDPval / GDPval-MM](https://artificialanalysis.ai/evaluations/gdpval-aa) - 🆕 **2026 年 2 月**。OpenAI 推出的经济价值 benchmark，覆盖 44 个职业 / 9 个行业，含 1,320 个专家构建任务。2026 年 5 月榜首：GPT-5.5 在 GDPval-MM 上 84.9%。
- [Hieroglyphic Benchmark](https://juliangoldie.com/google-gemini-3-5/) - 🆕 横向 / 抽象推理 benchmark；Gemini 3.5 "Snowbunny" 80%（泄露版）。
- [LLM-Stats Live Leaderboard](https://llm-stats.com/llm-updates) - 🆕 实时更新的跨 benchmark 模型对比看板。
- [τ²-Bench (Tau-Bench)](https://github.com/sierra-research/tau2-bench) - 🆕 Sierra Research 出品的真实业务域（零售 / 航空）工具-Agent-用户交互基准。考察多轮工具使用、数据库操作与策略遵从。2026 年 4 月榜首：38 个评测模型中 Claude Mythos Preview 89.2%。MIT。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsierra-research%2Ftau2-bench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Gartner 2026 魔力象限：企业 AI 编程 Agent](https://cursor.com/blog/cursor-leads-gartner-mq-2026) - 🆕 **2026 年**。Gartner 首个企业级编程 Agent MQ。**Cursor** 和 **OpenAI Codex** 被评为领导者，Cline 和 Windsurf 入选挑战者。标志着编程 Agent 市场迈入企业级成熟期。

---

## 🖥️ Computer Use / 桌面 Agent

*能看屏幕、控鼠键、自动操作 OS 级软件的 Agent。纯浏览器 Agent 见 [🌐 浏览器与 Web Agent](#-浏览器与-web-agent)。*

- [Claude Computer Use](https://www.anthropic.com/) - 🆕 Anthropic "Desktop Intelligence"，看屏幕 + 用鼠标键盘。
- [OpenAI Operator](https://openai.com/) - 🆕 浏览器 Agent，订票、填表、网页任务。
- [Google Project Mariner](https://deepmind.google/models/project-mariner/) - 📦 **已关闭**（2026-05-04）。浏览器 Agent 研究项目，能力已合入 Gemini Agent。
- [Microsoft Copilot Agents](https://www.microsoft.com/en-us/microsoft-copilot/) - 🆕 Microsoft 365 上的自主后台 Agent。
- [Open Interpreter](https://github.com/OpenInterpreter/open-interpreter) - 让 LLM 在本地跑代码的自然语言接口。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenInterpreter%2Fopen-interpreter&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Manus AI](https://manus.im/) - 🇨🇳 🆕 通用自主 Agent，云本地混合，研究 / 编程 / 复杂任务。
- [Genspark](https://www.genspark.ai/) - 🆕 mixture-of-agents 全能工作 Agent，能打电话。
- [Perplexity Computer](https://www.perplexity.ai/) - 🆕 多模型编排 + 本地文件访问，研究向。
- [Beam AI](https://beam.ai/) - 🆕 自学习桌面 Agent。
- [Microsoft Copilot Studio Computer-Using Agents](https://techcommunity.microsoft.com/blog/copilot-studio-blog/computer-using-agents-in-microsoft-copilot-studio-are-now-generally-available/4519427) - 🆕 **2026 年 5 月 13 日 GA**。在 Copilot Studio 内构建可通过 UI 直接操控网站和桌面应用的 Agent —— 微软对 Claude Computer Use 的第一方回应，现已在 Microsoft 365 / Power Platform 部署中正式开放。
- [Perplexity Personal Computer for Windows](https://www.perplexity.ai/hub/products/computer-for-windows) - 🆕 **2026 年 6 月 3 日宣布**。把 Perplexity 的多模型 Agent 编排器（自动路由 19+ 个 AI 模型）带到 Windows；统一连接本地文件、原生应用与 Web。基于 4 月 16 日 Mac 版的延伸，同步迭代 Computex 2026 发布的本地/云端混合推理编排能力。
- [ChatGPT Workspace Agents](https://venturebeat.com/orchestration/openai-unveils-workspace-agents-a-successor-to-custom-gpts-for-enterprises-that-can-plug-directly-into-slack-salesforce-and-more) - 🆕 **研究预览 2026-04-22，2026-05-06 走积分计费，2026-05-07 支持 EKM**。OpenAI 为企业推出的 Custom GPTs 后继 —— 云端 Agent，能访问文件、执行代码、原生接 Slack / Google Drive / Salesforce，可调度周期任务；Business / Enterprise / Edu / Teachers 可用，底层走 Codex。

---

## 🌐 浏览器与 Web Agent

*真实浏览器中工作的 Agent —— 导航、点击、抓取、跨页流程。*

- [Browser Use](https://github.com/browser-use/browser-use) - 2026 年开源浏览器 Agent 事实标准。92K star。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowser-use%2Fbrowser-use&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Stagehand](https://github.com/browserbase/stagehand) - Browserbase 出品的"浏览器 Agent SDK"：类型化 `act / extract / observe`，跑在 Playwright 上。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowserbase%2Fstagehand&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Steel Browser](https://github.com/steel-dev/steel-browser) - 🆕 AI Agent 专用开源浏览器 API：自带 session 持久化 + 代理轮换。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsteel-dev%2Fsteel-browser&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Skyvern](https://github.com/Skyvern-AI/skyvern) - 用 LLM + 视觉自动化网页流程。AGPL-3.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSkyvern-AI%2Fskyvern&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentQL](https://github.com/tinyfish-io/agentql) - 查询语言 + Playwright 集成。动态 / 杂乱页面健壮。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftinyfish-io%2Fagentql&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hyperbrowser MCP](https://github.com/hyperbrowserai/mcp) - 🆕 托管无头浏览器 + 标准 MCP 工具接入 Claude / GPT / LangChain。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhyperbrowserai%2Fmcp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) - 🆕 微软官方 Playwright MCP server。生产级即插即用。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fplaywright-mcp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MultiOn](https://www.multion.ai/) - 托管浏览器 Agent，原生 Reasoning + Memory。闭源。
- [Browserbase](https://www.browserbase.com/) - AI Agent 专用浏览器云：隐身、持久化、验证码、可观测性。
- [BrowserOS](https://www.browseros.com/) - 🆕 首个内置 AI Agent 的开源浏览器——隐私优先的 Chrome 替代。自然语言任务自动化无需写代码；本地优先设计，对标 Perplexity Comet 与 Arc 的 AI 能力。

---

## 🗣️ 语音与多模态 Agent

- [AgentLine](https://agentline.cloud/) - 🆕 ⚠️ **Unverified.** 面向 AI Agent 的电话基础设施 —— 申请号码、外呼/接听、实时转录为 JSON 推到 webhook。定位为 Twilio 在 Agent 语音管线场景下的更轻替代；提交者自称 30+ 付费用户，暂无第三方采用证据。
- [ElevenLabs](https://elevenlabs.io/) - AI 语音合成 + 对话 Agent。
- [Vapi](https://github.com/VapiAI/server-sdk-python) - 语音 AI Agent 平台。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FVapiAI%2Fserver-sdk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Retell AI](https://www.retellai.com/) - 生产级对话语音 AI。
- [Bland AI](https://www.bland.ai/) - 企业级 AI 电话平台。
- [LiveKit Agents](https://github.com/livekit/agents) - 实时多模态 Agent（语音 + 视频 + 数据）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flivekit%2Fagents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Pipecat](https://github.com/pipecat-ai/pipecat) - 开源语音多模态对话框架。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fpipecat-ai%2Fpipecat&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vocode](https://github.com/vocodedev/vocode-python) - 💤 **Stale**（2024-11 起无更新）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvocodedev%2Fvocode-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Bolna](https://github.com/bolna-ai/bolna) - 端到端开源语音 AI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbolna-ai%2Fbolna&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cartesia](https://www.cartesia.ai/) - 🆕 实时低延迟语音 AI。
- [Meta Voice AI](https://ai.meta.com/) - 🆕 收购 PlayHT/Play.ai 后的 Meta 语音技术。原 Play.ai 平台 2025-12-31 关停。
- [Sesame](https://www.sesame.com/) - 🆕 情绪感知 + 自然对话的语音 AI 伙伴。
- [OpenYabby](https://github.com/OpenYabby/OpenYabby) - 🆕 开源 macOS 语音驱动多 Agent 编排器 — Realtime API + CLI 子进程 + 多通道协调。主 Agent 规划任务并委派给子 Agent 进行评审和 QA。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenYabby%2FOpenYabby&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ElevenAgents](https://elevenlabs.io/voice-agents) - 🆕 ElevenLabs 全栈语音 Agent 平台（2026 年 4-5 月更新）：支持 MCP、多模态消息、会话主题发现、知识库检索、工具调用前的语音控制。首个获 AIUC-1 认证的语音 Agent 平台。
- [Cartesia Line](https://cartesia.ai/blog/introducing-line-for-voice-agents) - 🆕 **2026 年 4 月**。基于 Sonic 3 TTS + Ink STT 的代码优先语音 Agent 平台；首音延迟约 40-90ms。
- [Deepgram Voice Agent API](https://deepgram.com/learn/best-voice-ai-agents-2026-buyers-guide) - 🆕 单一端点打包 STT（Nova-3）+ LLM 路由 + TTS（Aura-2）+ Flux 会话式 STT，支持通话中 10 种语言切换。
- [OpenAI Realtime API (GPT-Realtime-2)](https://openai.com/) - 🆕 **2026 年 5 月 8 日**。GPT-5 级推理能力的语音版，支持并行工具调用；生产级语音 Agent 取代上一代 Realtime 模型。
- [Dograh](https://github.com/dograh-hq/dograh) - 🆕 开源、可自托管的语音 AI 平台——Vapi / Retell 的开源替代。On-prem 部署，可在 Speech-to-Speech 或 LLM/STT/TTS 之间 BYOK；可视化工作流构建器，原生 MCP，电话支持。BSD-2-Clause，4K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdograh-hq%2Fdograh&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hume TADA](https://github.com/HumeAI/tada) - 🆕 **2026 年 3 月 10 日**。Hume AI 首个开源 TTS——Text-Acoustic Dual Alignment 架构；零转录错误、约 5× 速度、可在手机运行；支撑下一代 EVI 语音 Agent。MIT，基于 Llama。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHumeAI%2Ftada&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 📱 个人 AI Agent

- [OpenClaw](https://github.com/openclaw/openclaw) - 🆕 多渠道、本地运行的个人 AI Agent 平台。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenclaw%2Fopenclaw&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Rabbit R1](https://www.rabbit.tech/) - 大动作模型驱动的硬件 AI 助理。
- [Limitless](https://www.limitless.ai/) - 个性化 AI（前 Rewind）。
- [Open Interpreter](https://github.com/OpenInterpreter/open-interpreter) - 自然语言计算机接口。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenInterpreter%2Fopen-interpreter&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [01 Light](https://github.com/OpenInterpreter/01) - 💤 **Stale**（2024-11 起无更新）。开源语音电脑接口。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenInterpreter%2F01&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Leon](https://github.com/leon-ai/leon) - 自托管开源个人助理。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fleon-ai%2Fleon&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Khoj](https://github.com/khoj-ai/khoj) - 你的笔记 / 文档 / 图片的"第二大脑"AI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fkhoj-ai%2Fkhoj&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Humane AI Pin](https://humane.com/) - ⚠️ **2025-02-28 已停产**（被 HP 收购，设备已关闭）。原为无屏幕环境计算的可穿戴 AI 设备。
- [Arahi AI](https://arahi.ai/) - 🆕 个人生产力 + 业务自动化助理。
- [Lindy AI](https://www.lindy.ai/) - 🆕 邮件 / 日历 / 工作流的无代码 Agent。
- [MuleRun](https://www.mulerun.ai/) - 🆕 周期任务的常驻 Agent。
- [Gemini Intelligence](https://blog.google/products-and-platforms/products/chrome/bringing-chrome-ai-to-android/) - 🆕 **2026 年 5 月 12 日（Android Show: I/O Edition）**。主动式 Agent AI 能力贯穿 Googlebooks 笔电、Wear OS、Android Auto、Android XR，首发于最新 Samsung Galaxy + Pixel。可基于购物清单自动生成购物车、预订单车课程，以及通过 Rambler STT 移除口头禅。
- [Gemini Spark](https://9to5google.com/2026/05/14/gemini-spark-insight/) - 🆕 **2026 年 5 月 14 日（I/O 前的爆料 / 洞察）**。Gemini 应用内即将上线的品牌化 Agent 能力，可自主跑完多步流程；构建在 Gemini 3.1 Pro 推理栈之上。
- [QwenPaw](https://github.com/agentscope-ai/QwenPaw) - 🆕 🇨🇳 **2026 年 5 月由 CoPaw 改名**。Qwen / AgentScope 生态下可自托管的个人助手。本地优先记忆、热加载 skills、多 Agent 协作、多通道（钉钉 / 飞书 / 微信 / Discord / Telegram），自带工具守卫和 skill 扫描器。Apache-2.0。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentscope-ai%2FQwenPaw&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsoft Scout](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) - 🆕 **Build 2026（2026 年 6 月 2 日）**。微软基于 OpenClaw 框架打造的常驻个人 Agent —— 跨云 / 桌面 / Web 主动工作，连接 Teams / Outlook / OneDrive / SharePoint。每个 Agent 在独立 Entra 身份下运行，连续策略合规检查 + 审计链。Microsoft Frontier 计划私测；需 Intune 策略 + GitHub Copilot 许可证。
- [Lenovo Qira / Motorola Qira](https://news.lenovo.com/pressroom/press-releases/lenovo-unveils-lenovo-and-motorola-qira/) - 🆕 **CES 2026（2026 年 1 月 6 日）**。联想与摩托罗拉联合打造的"个人环境智能系统"——上下文感知 AI 跨 PC / 手机 / 平板 / 可穿戴设备协同。Q1 2026 在部分联想设备上线，随后扩展至 Motorola 手机；OEM 主导的环境 AI 首发。

---

## 📱 手机 Agent

*操控 Android / iOS 的 GUI Agent —— 桌面 Computer Use 之后的下一前沿。*

- [Mobile-Agent](https://github.com/X-PLUG/MobileAgent) - 🇨🇳 阿里多模态手机控制 Agent 家族（v1 → v3 + Mobile-Agent-E / V）。Android 基准 SOTA。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FX-PLUG%2FMobileAgent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AppAgent](https://github.com/mnotgod96/AppAgent) - 💤 腾讯多模态智能体，通过点 / 滑操作 App。早期影响力实现。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmnotgod96%2FAppAgent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
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
- [Google Vertex AI Agent Builder](https://cloud.google.com/products/agent-builder) - 企业生成式 AI Agent 构建。
- [Amazon Bedrock Agents](https://aws.amazon.com/bedrock/agents/) - 多步任务 Agent。
- [ServiceNow AI Agents](https://www.servicenow.com/products/ai-agents.html) - 🆕 ITSM Agent + AI Control Tower。
- [ServiceNow MCP Server](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-opens-its-full-system-of-action-to-every-AI-Agent-in-the-enterprise/default.aspx) - 🆕 ServiceNow MCP Server 已 GA，随每个 Now Assist 与 AI Native SKU 自带。每次调用都走 AI Control Tower（AICT），具备身份验证、权限范围、审计链；自带 OAuth、用量计费、角色级工具包与会话管理。
- [IBM watsonx Orchestrate](https://www.ibm.com/products/watsonx-orchestrate) - 跨企业应用的 AI 助理平台。
- [Oracle AI Agents](https://www.oracle.com/artificial-intelligence/) - 🆕 与 Oracle Fusion Cloud ERP 集成。
- [Moveworks](https://www.moveworks.com/) - 跨系统企业 copilot。
- [UiPath Agentic Automation](https://www.uipath.com/) - 🆕 在 RPA 之上叠加 Agent 推理。
- [AgentX](https://www.agentx.so/) - 🆕 即插即用的企业 Agent 自动化。
- [Amazon Bedrock AgentCore Payments](https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-bedrock-agentcore-payments-preview/) - 🆕 **2026 年 4-5 月**。Bedrock AgentCore 的托管支付功能预览 —— Agent 可通过集成的 Coinbase 和 Stripe 自主为 API 等资源付费。同期扩展至 AWS GovCloud (US-West) 以满足合规需求。
- [OutSystems Agentic Systems Platform](https://www.outsystems.com/) - 🆕 **2026 年 6 月**。低代码巨头将其平台定位为“AI 原生”的 agentic 开发环境。提供开放式 AI 治理、自带模型、多 Agent 编排以及企业级合规，直接对标 Copilot Studio 与 Agentforce。
- [Sema4.ai](https://sema4.ai/) - 🆕 Python 优先 + 内置治理的企业 Agent 平台。
- [SAP Business AI Platform + Joule Studio 2.0](https://news.sap.com/2026/05/sap-sapphire-sap-unveils-autonomous-enterprise/) - 🆕 **SAP Sapphire 2026（2026-05-11 – 13）**。SAP 把 BTP + Business Data Cloud + Business AI 合并为一个平台，重新定位 Joule 为 Agent 操作层。**Joule Studio 2.0**（2026-06 起陆续到达客户）可以用 LangGraph / AutoGen 类框架底座着 SAP 的实时业务数据构建 Agent；**Autonomous Suite** 带来 50+ 领域 Joule Assistant 与 200+ Agent。
- [Microsoft Agent 365 + Microsoft 365 E7](https://techcommunity.microsoft.com/blog/agent-365-blog/microsoft-365-e7--agent365-from-where-you-are-to-enterprise-ai-at-scale/4519969) - 🆕 **2026-05-01 GA**，5 月持续补充。以身份为中心的 AI Agent 控制面：独立 $15/用户/月，或 $99/用户/月随新推的 Microsoft 365 E7 "Frontier" 套套；5 月补丁加上了 AWS Bedrock + Google Cloud 注册表同步、Intune / Defender 预览策略，以及 Agent 专用 SASE。
- [OpenAI Guaranteed Capacity（算力年发）](https://openai.com/news/company-announcements/) - 🆕 **2026-05-19**。面向企业 AI 产品 / Agent / Workflow 的长期算力预订产品（可选 1/2/3 年期，期限越长折扣越高）—— 面向 GPT-5.5 级 Agent 的企业部署降低成本 / 产能不确定性，OpenAI 对 Anthropic Priority Tier 的产品化回应。
- [Bristol Myers Squibb ↔ Claude Enterprise](https://news.bms.com/news/corporate-financial/2026/Bristol-Myers-Squibb-Announces-Strategic-Agreement-with-Anthropic-to-Position-Claude-Enterprise-as-the-Shared-Intelligence-Platform-Across-Its-Global-Operations/default.aspx) - 🆕 **2026-05-20**。BMS 将 Claude Enterprise 作为 30,000+ 员工的共享智能平台，嵌入药物发现 / 开发 / 交付的全链路。全球前 5 大药企中首个全公司级 Claude 部署。
- [Kore.ai Artemis Agent Platform](https://venturebeat.com/technology/kore-ai-launches-artemis-ai-agent-platform-expands-challenge-to-microsoft-and-salesforce) - 🆕 **2026 年 5 月 22 日（Azure 上线）**。AI 原生的企业级 Agent 平台，核心是新的 YAML 风格 **Agent Blueprint Language (ABL)**，用于声明式多 Agent 工作流。Kore.ai 对 Copilot Studio 与 Agentforce 的结构性挑战。
- [FPT Flezi Foundry™](https://lasvegassun.com/news/2026/may/22/fpt-launches-flezi-foundry-advancing-ai-augmented-/) - 🆕 **2026 年 5 月 22 日**。AI 增强的交付平台，两种受治理的 Service-as-a-Software 模式——**Agentic Development Lifecycle (ADLC)** 覆盖完整 SDLC 的 Agent 团队，以及 **Agentic Managed Services (AMS)** 把事故处置 Agent 叠加在现有 ITOps 之上。

---

## 📊 Agent 评估与可观测性

- [LangSmith](https://www.langchain.com/langsmith) - LangChain 的官方调试 / 评测 / 监控平台。
- [LangSmith SDK](https://github.com/langchain-ai/langsmith-sdk) - 客户端 SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangsmith-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Langfuse](https://github.com/langfuse/langfuse) - 开源 LLM 工程平台：可观测性 + 评测 + prompt 管理。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangfuse%2Flangfuse&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Helicone](https://github.com/Helicone/helicone) - 开源 LLM 可观测性。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHelicone%2Fhelicone&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Arize Phoenix](https://github.com/Arize-ai/phoenix) - 开源 LLM 可观测性 + 评测。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FArize-ai%2Fphoenix&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Braintrust](https://www.braintrust.dev/) - LLM 评测 + 优化平台。
- [LMArena (formerly LMSYS Chatbot Arena)](https://lmarena.ai/) - 🆕 众包 LLM 偏好投票。
- [Patronus AI](https://www.patronus.ai/) - 🆕 自动 LLM 评测 + 红队。
- [DeepEval](https://github.com/confident-ai/deepeval) - Pytest 风格的 LLM 评测框架，14+ 内置指标。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fconfident-ai%2Fdeepeval&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agenta](https://github.com/agenta-ai/agenta) - 🆕 一体化开源 LLMOps。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagenta-ai%2Fagenta&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AutoEvals](https://github.com/braintrustdata/autoevals) - 独立的最佳实践评测器库（事实性 / JSON 有效性 / 语义相似度等）。Braintrust 出品。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbraintrustdata%2Fautoevals&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [BenchClaw](https://github.com/Agnuxo1/benchclaw) - ⚠️ **Unverified**。自称多维度 Agent 评测。8 个 awesome 列表 7 个拒收，2 star 单维护者。**仅作可见性收录**。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAgnuxo1%2Fbenchclaw&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [PromptEden](https://www.prompteden.com) - ⚠️ **Unverified**。商业 SaaS：监控 ChatGPT / Claude / Gemini / Perplexity / Copilot / Grok 如何描述你的品牌。同款 PR 同日投了 10 个 awesome 列表。**仅作可见性收录**。
- [AgentBench](https://github.com/THUDM/AgentBench) - 评估 LLM 作为 Agent 表现的多维 benchmark。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTHUDM%2FAgentBench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Braintrust](https://github.com/braintrustdata/braintrust-sdk) - 企业级 AI 产品构建栈——评估、提示词 playground、日志一体化。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbraintrustdata%2Fbraintrust-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenLLMetry](https://github.com/traceloop/openllmetry) - 基于 OpenTelemetry 的开源 LLM 可观测性方案。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftraceloop%2Fopenllmetry&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Weights & Biases Weave](https://github.com/wandb/weave) - 用于开发、评估与监控 AI 应用的工具包。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fwandb%2Fweave&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SWE-bench](https://github.com/princeton-nlp/SWE-bench) - 评估 LLM 在真实软件工程问题上能力的 benchmark。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fprinceton-nlp%2FSWE-bench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Terminal-Bench](https://www.tbench.ai/) - 🆕 面向终端编码 Agent 的评估 benchmark。由 Harbor Framework 维护。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fharbor-framework%2Fterminal-bench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Laminar](https://github.com/lmnr-ai/lmnr) - 🆕 专为长跑 AI Agent 设计的开源可观测性平台（Apache-2.0，YC S24）。OpenTelemetry 原生，transcript view、Signals、SQL 跨 traces 查询、浏览器 Agent 会话回放。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flmnr-ai%2Flmnr&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangSmith Engine](https://www.langchain.com/blog/interrupt-2026-overview) - 🆕 **2026 年 5 月（Interrupt 2026）**。LangSmith 的自主失败诊断层——将生产失败聚类为优先级问题，结合 traces 与代码定位根因，给出可供人类审阅的修复建议。与新发的 SmithDB（Rust + DataFusion 支持的 Agent 观测数据库）配套。

---

## 🔬 AI 研究工具

- [Hugging Face Transformers](https://github.com/huggingface/transformers) - 模型与训练工具的事实标准库。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhuggingface%2Ftransformers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [vLLM](https://github.com/vllm-project/vllm) - 高吞吐 LLM 推理与服务。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvllm-project%2Fvllm&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SGLang](https://github.com/sgl-project/sglang) - 高性能 LLM 推理引擎。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsgl-project%2Fsglang&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [llama.cpp](https://github.com/ggml-org/llama.cpp) - C/C++ 高性能 LLM 推理。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fggml-org%2Fllama.cpp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Ollama](https://github.com/ollama/ollama) - 本地跑 LLM 的最简单方法。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Follama%2Follama&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LM Studio](https://lmstudio.ai/) - 桌面本地 LLM GUI，多提供商。
- [OpenRouter](https://openrouter.ai/) - 一个 API 统一访问 100+ LLM。
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
- [LLM Agents MOOC (Berkeley)](https://llmagents-learning.org/f24) - UC Berkeley 的 LLM Agent 课程。
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
- [Multimodal Intelligence as the Dominant Paradigm in 2026 AI Systems](https://www.researchgate.net/publication/398878301) - 🆕 关于多模态 AI 成为 2026 默认范式的研究综述。
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
- [Lobe Chat](https://github.com/lobehub/lobe-chat) - 多 Agent 聊天工作区 + 插件 / Agent 市场。最高 star 的 TypeScript AI 项目之一。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flobehub%2Flobe-chat&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cozeloop](https://github.com/coze-dev/cozeloop) - 🆕 字节 Coze 团队开源的 Agent 优化平台。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcozeloop&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentScope](https://github.com/modelscope/agentscope) - 阿里 ModelScope 多 Agent 框架 + 可视化调试 + 分布式执行。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelscope%2Fagentscope&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Bisheng](https://github.com/dataelement/bisheng) - 开源企业级 LLM DevOps：工作流 / RAG / Agent / 微调 / 评测。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdataelement%2Fbisheng&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MetaGPT](https://github.com/geekan/MetaGPT) - SOP 角色多 Agent（PM / 架构师 / 工程师）。DeepWisdom 出品。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgeekan%2FMetaGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### RAG / 知识

- [FastGPT](https://github.com/labring/FastGPT) - 知识库优先的 LLM 平台：数据摄入 / RAG / 可视化工作流。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flabring%2FFastGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [QAnything](https://github.com/netease-youdao/QAnything) - 💤 网易有道出品，针对任意本地文档的问答引擎。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fnetease-youdao%2FQAnything&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAGFlow](https://github.com/infiniflow/ragflow) - 深度文档理解的 RAG 引擎 —— 扫描 PDF 、表格、图表处理能力强。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Finfiniflow%2Fragflow&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LightRAG](https://github.com/HKUDS/LightRAG) - 港大 HKUDS 轻量图式 RAG。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2FLightRAG&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### 个人与生产力

- [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) - 开源 Notion 替代品 + AI 工作区。AGPL-3.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAppFlowy-IO%2FAppFlowy&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Manus AI](https://manus.im/) - 通用自主 Agent（北京 Butterfly Effect）。中文技术圈 2026 最受关注的 Agent 产品之一。
- [Coze (扣才)](https://www.coze.cn/) - 字节无代码 Agent 构建。国内面向消费者；国际版为 coze.com。
- [通义千问 Agent](https://tongyi.aliyun.com/) - 阿里大众消费者 Agent，集成在淘宝 / 钉钉 / 夸克。
- [Doubao Agents](https://www.doubao.com/) - 字节豆包模型上的主力消费者助手。

### 开发者工具

- [Kilo Code](https://www.kilocode.com/) - 2026 中文社区热门的 Cursor 替代。默认 MiniMax 模型。
- [CoderPlan](https://coderplan.ai/) - 面向中国开发者的统一 LLM API 网关（Claude / OpenAI / Gemini，一行配置支持 Claude Code），按量付费，支持支付宝 & 微信支付。
- [Cherry Studio](https://github.com/CherryHQ/cherry-studio) - 中文开发者圈装机量最高的开源桌面 LLM 客户端，多提供商 + 知识库。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FCherryHQ%2Fcherry-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ScienceOne 100 / 磐石100](https://english.cas.cn/newsroom/cas-in-media/202604/t20260429_1158251.shtml) - 🆕 中科院科研推理 Agent 系统，50+ 中科院研究所、100+ 科研场景、带 2000+ 研究工具。
- [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code) - 🆕 **2026 年 6 月 6 日**。Moonshot AI 的终端编程 Agent（MIT，TypeScript）——内置 coder / explore / plan 子 Agent 在隔离上下文里跑，`/mcp-config` 对话式 MCP 配置。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FMoonshotAI%2Fkimi-code&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
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
| [Phidata / Agno](https://github.com/phidatahq/phidata) | Python | ✅ teams | ❌ | ✅ | MPL-2.0 | 多模态 Agent + 记忆 |

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

*表格于 2026-05-05 验证。数据变化请提 PR。*

---

### 💰 基础大模型 — API 价格与上下文窗口

*价格单位：USD/百万 token。数据：2026-05-20。*

| 模型 | 厂商 | 上下文窗口 | 输入 $/1M | 输出 $/1M | 适用场景 |
|-------|----------|---------------|-----------|------------|----------|
| GPT-4o | OpenAI | 128K | $2.50 | $10.00 | 广泛工具调用、视觉、广泛生态 |
| GPT-4o-mini | OpenAI | 128K | $0.15 | $0.60 | 大规模简单任务 |
| Claude Sonnet 4.6 | Anthropic | 200K | $3.00 | $15.00 | 编程 Agent、复杂推理 |
| Claude Opus 4.7 | Anthropic | 200K | $5.00 | $25.00 | 最难推理任务 |
| Claude Haiku 4.5 | Anthropic | 200K | $1.00 | $5.00 | Anthropic 生态快速任务 |
| Gemini 2.5 Flash | Google | 1M | $0.30 | $2.50 | 性价比高的多模态 |
| Gemini 2.5 Pro | Google | 2M | $1.25 | $10.00 | 超长文本、多模态 |
| Gemini 2.5 Flash-Lite | Google | 1M | $0.10 | $0.40 | 极低成本大量请求 |
| DeepSeek V3.2 | DeepSeek | 128K | $0.14 | $0.28 | 低成本编程推理 |
| Qwen3 235B A22B | 阿里巴巴 | 131K | ~$0.29 | ~$1.15 | 最强中文+编程 MoE |
| Kimi K2.6 | Moonshot AI | 262K | ~$0.60 | ~$2.50 | 中文+超长上下文 |
| Grok 4 | xAI | 256K | $3.00 | $15.00 | X/Twitter 生态、推理 |
| Grok 4.20 | xAI | 2M | $2.00 | $6.00 | 超长上下文、Agent 任务 |

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
| ElevenLabs v3 | ❌ | ⭐⭐⭐⭐⭐ | ✅ | ❌ | ~200ms | 32+ | 闭源 |
| Whisper v3（本地） | ⭐⭐⭐⭐★ | ❌ | ❌ | ✅ | ~1s | 99 | MIT |
| Deepgram Nova-3 | ⭐⭐⭐⭐⭐ | ✅ | ✅ | ❌ | <100ms | 30+ | 闭源 |
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
| Midjourney V8 | 2K+ | 仅网页 | 艺术风格最强 | 艺术创作 | $10–$120/月 |
| Stable Diffusion 3.5 | 2K | 本地+API | 良好 | 开源、自托管 | Apache-2.0 |
| Ideogram 3 | 2K | API+网页 | 良好 | 图内文字最强 | 免费增值 |

---

### 🎥 视频生成模型

| 模型 | 最大时长 | 分辨率 | API/本地 | 适用场景 | 状态 |
|-------|-----------|-----------|-------------|----------|------------------|
| Veo 3.1 | 2分钟 | 4K | API（Vertex） | 最高保真度 | GA（Google） |
| Kling VIDEO 3.0 | 3分钟 | 1080p | API+网页 | 电影风格领先 | GA（快手） |
| Runway Gen-4 | 10s/片段 | 1080p | API+网页 | 精确运动控制 | GA |
| Pika 2.0 | 10s | 1080p | 网页 | 创意/社交媒体 | GA |
| Seedance 2.0 | 60s | 1080p | API | 快速、高性价比 | GA（字节） |
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
| OpenClaw | ❌ | ✅ | ✅ 原生 | ✅（TG/Discord/WA） | ✅ | 全能自托管个人 Agent |
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
| Kimi K2.6 | Moonshot AI | 262K | 高 | ⭐⭐⭐⭐☆ | ❌ | ~$0.60 |
| GLM-5.1 | 智谱 AI | 128K | 高 | ⭐⭐⭐⭐☆ | ⚠️ 部分 | ~$0.50 |
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

*所有对比表数据来源：2026-05-20。数据变化请提 PR。*

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
- **OpenAI Realtime API** — 原生语音 + 工具调用。
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
→ **Claude Opus 4.7**（200K 上下文）+ **LlamaIndex** + **pgvector**。必须保留人工审核。

**创意写作助手**
→ **Claude Opus 4.7**（最佳散文质量）或 **Gemini 2.5 Pro**（2M 上下文）。

**安全扫描 Agent**
→ **Semgrep** + **Claude Sonnet 4.6** + **mcp-scan**。

---

### 🧠 模型选择类

**需要最强模型做复杂推理**
- **Claude Opus 4.7** (/think xhigh) — $5/$25/1M。
- **Gemini 2.5 Pro** — 2M 上下文，$1.25/$10。
- **GPT-4o** — 广泛生态，$2.50/$10。

**需要最快最便宜的模型（简单高频任务）**
- **Gemini 2.5 Flash-Lite** — $0.10/$0.40/1M。
- **DeepSeek V3.2** — $0.14/$0.28/1M，惊人的性价比。

**需要最强中文能力**
- **Qwen3 235B A22B** — 中文评测居首。
- **Kimi K2.6** — 262K 上下文。
- **DeepSeek V3.2** — 开源权重中文编程。

**需要本地/离线模型（16GB 显存）**
- **Qwen3.6-27B Q4_K_M** — ~17GB，最佳 16GB 首选。
- **Phi-4 14B** — ~9GB，编程首选。

**需要本地/离线模型（40GB+）**
- **Llama 3.3 70B Q4_K_M** — ~42GB。
- **Qwen3 235B A22B Q2** — MoE 主力。

**需要最强编程能力**
→ **Claude Sonnet 4.6**（通过 Claude Code，SWE-bench 80.9%）。

**需要超长上下文 (500K+)**
- **Gemini 2.5 Pro** — 2M 上下文。
- **Kimi K2.6** — 262K。

**需要开源权重模型（MIT/Apache）**
- **Llama 3.3 70B** (Apache-2.0)、**DeepSeek V3.2** (MIT)、**Qwen3 235B A22B** (Apache-2.0)。

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
- [A2A Protocol](https://github.com/google/A2A) - 🆕 Google A2A 让跨框架 Agent 协作，150+ 合作伙伴。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle%2FA2A&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - SWE-bench 80.9%，成为 2026 终端编程 Agent 首选。
- [Kiro](https://kiro.dev/) - 🆕 AWS 发布的自主编程 Agent，可同时管理 10 个任务。
- [Devin 3.0](https://www.cognition.ai/) - 🆕 动态重规划、自愉合代码、遗留代码迁移。
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/) - 🆕 AutoGen + Semantic Kernel 合并。
- [OpenAI Codex CLI](https://github.com/openai/codex) - OpenAI 进入开源终端 Agent 赛道。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fcodex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Browser Use](https://github.com/browser-use/browser-use) - 让 AI Agent 自然使用网页的突破性项目。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowser-use%2Fbrowser-use&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude Computer Use](https://www.anthropic.com/) - 🆕 Claude "Desktop Intelligence"。
- [Manus AI](https://manus.im/) - 🇨🇳 🆕 通用自主 Agent，能处理研究 / 编程 / 复杂工作流。
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
- [OpenAI Guaranteed Capacity（算力年发）](https://openai.com/news/company-announcements/) - 🆕 **2026-05-19**。面向企业 AI 产品 / Agent / Workflow 的长期算力预订产品（可选 1 / 2 / 3 年期，期限越长折扣越高）：OpenAI 对 Anthropic Priority Tier 与顶级模型推理供给吃紧的产品化回应。
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
| **2026-06-27** | GPT-4.5 计划从 ChatGPT 正式退役（API 仍保留）—— OpenAI 全力转向 GPT-5.5 家族 | 模型 |
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
| **2026-05-29** | [MCP 2026-07 Release Candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) 发布 — 无状态协议核心、扩展机制、MCP Apps 服务端渲染 UI、OAuth/OIDC 加固，正式版目标7月 28 日 | 协议 |
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

---

## 贡献

请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。**反垃圾质量门槛**适用于中英日三个版本：自我推广批量铺货 PR 一律拒绝。

## License

MIT © [Zijian Ni](https://github.com/Zijian-Ni)

---

*Made with ❤️ by [Zijian Ni](https://github.com/Zijian-Ni) · 2026。中文版本与英文版保持同步，发现不一致以英文为准。*
