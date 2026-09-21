<div align="center">

# 🤖 Awesome AI Agents 2026 · 中文版

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fawesome-ai-agents-2026&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)](https://github.com/Zijian-Ni/awesome-ai-agents-2026)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-September%208%2C%202026-blue.svg)](#)
[![Resources](https://img.shields.io/badge/Resources-910%2B-orange.svg)](#)
[![Audited](https://img.shields.io/badge/Spam_Audited-2026--09--08-success.svg)](#️-状态图例)
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
> 3. 🧩 **改编配置示例** → [技术栈食谱](#-技术栈食谱--精选工具组合)
> 4. 🔍 **选对工具** → [对比表](#-横向对比表)
> 5. ⚠️ **避开常见陷阱** → [反推荐清单](#️-反推荐--不应该用在哪里)
>
> **已在开发？** 快速跳转：
> - 🆕 [最新添加（2026 年 9 月）](#-2026-ai-时间线) • 🛡️ [安全](#️-agent-安全) • 💰 [费用对比](#-基础大模型--api-价格与上下文窗口)

---

## 快速导航

*数量统计的是目录中的收录次数，含历史与相关章节的重复出现，并非独立产品总数。本仓库遵循精选规则，完整模型检索可继续使用官方目录链接。*

| 分类 | 说明 | 数量 |
|----------|-------------|-------|
| [🧠 基础大模型 2026](#-基础大模型-2026) | 来自 OpenAI、Anthropic、Google、Meta 等 22+ 家厂商的最新大模型 | 230+ |
| [🎨 多模态与生成式 AI](#-多模态与生成式-ai) | 图像、视频、音频与音乐生成 | 60+ |
| [🔗 Agent 协议与标准](#-agent-协议与标准) | MCP、A2A 与互操作标准 | 20+ |
| [🏗️ Agent 框架](#️-agent-框架) | 构建自主 AI Agent 的开发库 | 55+ |
| [🛠️ Agent IDE 与可视化构建器](#️-agent-ide-与可视化构建器) | 设计 Agent 流程的可视化 / 低代码环境 | 10+ |
| [🧠 Agent 记忆](#-agent-记忆) | 持久化记忆与上下文管理 | 25+ |
| [🔌 工具与 API 集成](#-工具与-api-集成) | 把 Agent 接到外部服务 | 25+ |
| [💱 Agent 经济与市场](#-agent-经济与市场) | Agent 付费、变现与服务发现 | 10+ |
| [🧪 Agent 沙箱与计算隔离](#-agent-沙箱与计算隔离) | 运行 Agent 生成代码的安全沙箱 | 10+ |
| [🛡️ Agent 安全](#️-agent-安全) | Prompt 注入防御与护栏 | 35+ |
| [🔍 RAG 与知识库](#-rag-与知识库) | 检索增强生成系统 | 20+ |
| [💻 编程 Agent](#-编程-agent) | AI 驱动的软件工程 | 55+ |
| [🤖 Physical AI / 具身智能](#-physical-ai--具身智能) | 人形机器人、具身智能、工业自动化 | 45+ |
| [🎮 Agent 仿真与世界模型](#-agent-仿真与世界模型) | 训练与压力测试 Agent 的仿真环境 | 10+ |
| [📊 评测与 Leaderboard](#-评测与-leaderboard) | 追踪前沿能力的排行榜 | 25+ |
| [🖥️ Computer Use / 桌面 Agent](#️-computer-use--桌面-agent) | 桌面自动化与操作系统级控制 | 10+ |
| [🌐 浏览器与 Web Agent](#-浏览器与-web-agent) | 驱动真实浏览器的 Agent | 20+ |
| [🗣️ 语音与多模态 Agent](#️-语音与多模态-agent) | 支持语音的对话式 AI | 25+ |
| [📱 个人 AI Agent](#-个人-ai-agent) | 生产力与日常生活助手 | 20+ |
| [📱 手机 Agent](#-手机-agent) | 手机操控 Agent（Android / iOS） | 10+ |
| [🏢 企业级 Agent 平台](#-企业级-agent-平台) | 企业级 Agent 部署 | 30+ |
| [📊 Agent 评估与可观测性](#-agent-评估与可观测性) | 测试、监控与基准评测 | 30+ |
| [🔬 AI 研究工具](#-ai-研究工具) | AI / ML 研究与实验工具 | 15+ |
| [📚 学习资源](#-学习资源) | 论文、课程与教程 | 25+ |
| [🇨🇳 中国 AI 生态](#-中国-ai-生态) | 中国团队的主要项目 | 25+ |
| [📝 横向对比表](#-横向对比表) | 横向对比表 | — |
| [🗺️ 场景指南 — 我应该用什么…](#️-场景指南--我应该用什么) | 场景到工具的精选映射 | 58 |
| [📋 技术栈食谱 — 精选工具组合](#-技术栈食谱--精选工具组合) | 精选的多工具组合 | 8 |
| [⚠️ 反推荐 — 不应该用在哪里…](#️-反推荐--不应该用在哪里) | 不该用什么，以及为什么 | 17 |

---

## 目录

- [🧠 基础大模型 2026](#-基础大模型-2026)
- [🎨 多模态与生成式 AI](#-多模态与生成式-ai)
- [🔗 Agent 协议与标准](#-agent-协议与标准)
- [🏗️ Agent 框架](#️-agent-框架)
- [🛠️ Agent IDE 与可视化构建器](#️-agent-ide-与可视化构建器)
- [🧠 Agent 记忆](#-agent-记忆)
- [🔌 工具与 API 集成](#-工具与-api-集成)
- [💱 Agent 经济与市场](#-agent-经济与市场)
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
- [📋 技术栈食谱 — 精选工具组合](#-技术栈食谱--精选工具组合)
- [⚠️ 反推荐 — 不应该用在哪里…](#️-反推荐--不应该用在哪里)
- [🌟 2026 年值得关注的 Agent 项目](#-2026-年值得关注的-agent-项目)
- [📅 2026 AI 时间线](#-2026-ai-时间线)

---

## 🧠 基础大模型 2026

*按厂商整理的现役与历史基础模型精选。模型卡、API 可用性和权重许可证可能不同；带日期的条目保留发布历史。*

### OpenAI
- [GPT-Live-1 / GPT-Live-1 mini](https://openai.com/index/introducing-gpt-live/) - 🆕 **2026-07-08**。OpenAI 全双工会话语音模型，取代进阶语音模式。同步收听和说话（零切换延迟），处理打断，复杂查询在后台由 GPT-5.5 处理同时语音不中断。**GPT-Live-1** 为付费用户默认（Go/Plus/Pro）；**GPT-Live-1 mini** 为免费用户默认。支持实时语音翻译。
- [GPT-6 Astra / Astra Pro](https://openai.com/index/gpt-6-astra/) - 🆕 **2026年9月3日**。面向复杂推理、编程与计算机操作；[仅向部分组织逐步开放，尚未普遍可用](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)，公开 API 模型卡不代表当前账户已有访问权限。
- [GPT-5.6 Sol](https://openai.com/blog/gpt-5-6) - GPT-5.6 系列中面向推理、编程与工具工作流的模型。本次复核时标准 API 输入/输出价格为每百万 token $4/$20；长上下文、缓存与服务层级差异见[价格表](https://developers.openai.com/api/docs/pricing)。
- [GPT-5.6 Terra](https://openai.com/blog/gpt-5-6) - 🆕 **2026-07-09**。GPT-5.6 中级档 —— 与 GPT-5.5 性能相当但成本约降低 2×，适合成本敏感的生产任务。
- [GPT-5.6 Luna](https://openai.com/blog/gpt-5-6) - 🆕 **2026-07-09**。GPT-5.6 速度/成本最优层 —— 专为大量、对延迟敏感的任务设计。
- [ChatGPT Work](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) - 🆕 **2026-07-09**。OpenAI 的「把目标变成成品」Agent —— 可跨已连接的应用与文件执行操作，能连续数小时专注一个项目，生成幻灯片/表格/文档/Web 应用，支持定时任务，并具备带内置浏览器的桌面 Computer Use 能力。由 GPT-5.6 驱动。Web/移动端从 Pro、Enterprise、Edu 开始逐步开放（Plus/Business 随后）；桌面 App 已在 Mac 与 Windows 全球上线，所有套餐（含免费版）可用。
- [Sites for ChatGPT](https://openai.com/academy/chatgpt-sites/) - 🆕 **2026-06**。由 Codex 驱动的 ChatGPT 功能，能将计划和分析转换为可交互、可分享的网页与轻量应用。截至 2026-07-09 GPT-5.6 / ChatGPT Work 发布时处于公测阶段。
- [Codex 业务插件](https://venturebeat.com/orchestration/openais-codex-update-lets-agents-build-interactive-enterprise-workspaces-via-sites-and-role-specific-plugins) - 🆕 **2026-06**。面向企业的增强功能，为 Codex 平台引入销售、数据分析和创意制作的定制插件。
- [GPT-Rosalind](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/) - **2026-06-03**。OpenAI 生命科学前沿模型的重大升级 —— 药物发现、基因组学、定量生物学与湿实验排障显著增强（长程基因组分析比 GPT-5.5 约少用 31% token）。研究预览首次面向全球合资格机构开放；Novo Nordisk 加入既有伙伴 Amgen、Moderna、Allen Institute、Thermo Fisher。

- [GPT-5.5](https://openai.com/index/gpt-5-5-system-card/) - **2026-04-23 发布**（代号 "Spud"）。OpenAI 面向 Agent 任务的新一代旗舰：编程、在线研究、数据分析、自主工具调用。推理稳定性与长任务执行力大幅提升。ChatGPT Plus / Pro / Business / Enterprise 可用。
- [GPT-5.5 Pro](https://openai.com/index/gpt-5-5-system-card/) - 2026-04-23。并行测试期算力变体，更高准确率。Pro / Business / Enterprise。
- [GPT-5.5 Instant](https://openai.com/index/gpt-5-5-instant/) - **2026-05-05**。ChatGPT 新默认模型，效率优先升级，高风险提示词幻觉率下降约 50%；免费用户可用。
- [GPT-5.5-Cyber](https://openai.com/index/trusted-access-for-cyber/) - **2026-04-30**。GPT-5.5 的网络安全特化版本，通过 OpenAI Trusted Access for Cyber (TAC) 计划仅向防御者、政府、关键基础设施运营方、安全厂商开放，不对公众发布。
- [OpenAI Daybreak](https://thehackernews.com/2026/05/openai-launches-daybreak-for-ai-powered.html) - **2026-05-12**。整合 GPT-5.5 + GPT-5.5-Cyber + Trusted-Access-for-Cyber 的网络防御平台，提供 AI 驱动的漏洞检测与补丁验证；预览版已向欧盟政府与安全厂商开放。
- [GPT-5.6-Cyber](https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows) - 🆕 **2026-08-10**。基于 GPT-5.6 Sol 的网络安全特化模型，通过 **Daybreak Red** 审核计划向授权漏洞研究人员和安全专家开放，能识别零日漏洞、构建漏洞利用链；8 月 11 日起也可经 AWS Bedrock 访问。
- [GPT-Realtime-2](https://openai.com/) - **2026-05-08**。把 GPT-5 级推理带入 Realtime API，128K 上下文，并行工具调用 + 音频反馈，可调推理力度。
- [GPT-Realtime-Translate](https://openai.com/) - **2026-05-08**。实时语音对语音翻译，覆盖 70+ 种输入语言、13 种输出语言。
- [GPT-Realtime-Whisper](https://openai.com/) - **2026-05-08**。GPT-Realtime-2 的流式低延迟语音转文字搭档。
- [OpenAI Deployment Company (DeployCo)](https://openai.com/index/openai-launches-the-deployment-company/) - **2026-05-11**。OpenAI 控股的企业 AI 落地服务公司，$4B+ 启动资金，TPG / Advent / Bain Capital / Brookfield / Goldman Sachs / SoftBank 与 Bain & Company / Capgemini / McKinsey 等共投。围绕 Forward Deployed Engineers 体系，并吸收 Tomoro 咨询团队（~150 人）。
- [Codex on Mobile](https://9to5mac.com/2026/05/14/openai-brings-codex-control-to-chatgpt-for-iphone-and-android/) - **2026-05-14**。ChatGPT iOS / Android 远程操控 Mac 上的 Codex 桌面 App —— 查看输出、批准操作、切换模型、启动新任务，文件 / 凭据 / 权限仍留在本机。Free / Plus / Go 预览。
- [OpenAI ↔ Malta 合作](https://openai.com/index/malta-chatgpt-plus-partnership/) - **2026-05-16**。首次国家级合作：完成马耳他大学开发的 2 小时 AI 素养课程后，所有 14 岁以上马耳他公民 / 居民可免费获得 1 年 ChatGPT Plus。"OpenAI for Countries" 计划的首站。
- [OpenAI ↔ Dell Codex 合作](https://openai.com/news/company-announcements/) - **2026-05-18**。借助 Dell 的混合云 / 本地部署能力，Codex 首次走出公有云，面向需要数据主权 / 合规隔离的强监管行业。
- [ChatGPT 安全系统更新](https://www.edtechinnovationhub.com/news/openai-updates-chatgpt-safety-systems-to-track-risk-across-sensitive-conversations) - **2026-05-18**。ChatGPT 加入跨会话的潜在风险跟踪（自杀 / 自伤 / 伤他），能识别微妙、逐步升级的变化。
- [OpenAI Guaranteed Capacity（算力年发）](https://openai.com/news/company-announcements/) - **2026-05-19**。面向企业 AI 产品 / Agent / Workflow 的长期算力预订产品：1 / 2 / 3 年期，期限越长折扣越高。对度 Anthropic Priority Tier 的产品化回应。
- [OpenAI ↔ Google SynthID + C2PA 内容源头验证](https://openai.com/index/advancing-content-provenance/) - **2026-05-19**。OpenAI 联手 Google，为 ChatGPT/Sora 生成的图片加上 **SynthID** 跨平台水印，加入 C2PA，并预览一个公开的 **"这张图是 OpenAI 生成的吗"** 验证器。两家顶级 lab 首次在水印上互通。
- [GPT-5.4](https://openai.com/) - 2026-03 发布。1M token 上下文，编程、Computer Use、工具检索均强。BenchLM 94，SWE-bench Verified 77.2%，OSWorld 75%（超过人类基线）。
- [GPT-5.4 Pro](https://openai.com/) - GPT-5.4 的高准确率变体。BenchLM 92。
- [GPT-5.3](https://openai.com/) - 2026 年初。包括 GPT-5.3 Instant（对话）和 GPT-5.3-Codex（编程）。
- [GPT-5.2](https://openai.com/) - 2025-12 发布。SOTA 推理 + 长上下文 + 视觉。
- [GPT-5](https://openai.com/index/introducing-gpt-5/) - **2025年8月**。较早的 GPT 世代，提供标准、mini、nano API 变体，保留作为发布历史。
- [GPT-4o](https://openai.com/index/hello-gpt-4o/) - Omni 模型，原生支持文本/视觉/音频。2026-02 从 ChatGPT 下线，API 仍可用。
- [GPT-4.5](https://developers.openai.com/api/docs/deprecations) - 📦 历史研究预览；`gpt-4.5-preview` API 已于 **2025年7月14日**退役。
- [o3 / o4-mini](https://openai.com/index/introducing-o3-and-o4-mini/) - 思维链推理模型。2025-04 发布。o3 将于 2026-08-26 退役。
- [Codex CLI](https://github.com/openai/codex) - OpenAI 出品的开源终端编程 Agent。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fcodex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenAI Jalapeño](https://openai.com/index/jalapeno-first-results) - 🆕 ⚡ **2026-08-25**。OpenAI 自研推理芯片首次公开结果：面向现代模型的更高吞吐、更低延迟。官方 RSS：「industry-leading speed and efficiency in AI inference」。
- [ChatGPT for Teens](https://openai.com/index/chatgpt-for-teens) - 🆕 **2026-08-18**。面向青少年的 ChatGPT 体验，加强内置防护、健康使用功能与家长控制。
- [前沿模型 Zero Data Retention](https://openai.com/index/offering-zero-data-retention-for-frontier-models) - 🆕 **2026-08-19**。OpenAI 重申符合条件的 API 客户可使用零数据保留，并预览 Private Safety Processing，以便在不保留客户数据的前提下做高级安全检查。

### Anthropic

- [Claude Haiku 4.5](https://platform.claude.com/docs/en/models/overview) - 低延迟 Claude 层级，200K 上下文、最高 64K 输出；与 Sonnet 5、Opus 5、Fable 5.1 并列于当前产品目录。
- [Claude Fable 5.1 / Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1) - 🆕 **2026年9月1日**。Fable 5.1 已正式开放（`claude-fable-5-1`）；Mythos 5.1 使用相同模型、不同防护措施，目前仅向获批的美国机构开放。
- [Claude 文本水印 + 内容凭证](https://www.anthropic.com/news/claude-text-watermark) - 🆕 **2026-08-14**。Anthropic 为未来的 Claude 模型在全球范围发布时内置基于 **SynthID-Text 的隐形水印**（Google DeepMind 的方法），并为生成的图像/文件（.png/.jpg/.svg）加入 C2PA 内容凭证；2026 年 8 月 2 日之前发布的模型将「在未来几个月内」跟进，检测 API 也即将推出。此举是为遵守欧盟 AI 法案 —— Anthropic 已于 7 月签署欧盟透明度行为准则。Anthropic 称带水印文本对读者完全无感。
- [Claude Opus 5](https://www.anthropic.com/news/claude-opus-5) - 🆕 **2026-07-24**。Anthropic 第五代旗舰模型，性能近似 Fable 5，定价维持较低（输入 / 输出 $5 / $25 每百万 token）。支持 1M token 上下文窗口和最多 128K 输出 token。现为 Claude Max 默认模型。API: `claude-opus-5`。可通过 Anthropic API、Amazon Bedrock 和 Google Cloud Vertex AI 使用。
- [Claude Fable 5 全球恢复访问](https://www.anthropic.com/news/redeploying-fable-5) - 🆕 **2026-07-01**。美国商务部于 6 月 30 日解除出口管制后，Anthropic 在 Claude.ai、Claude Platform、Claude Code、Claude Cowork 全面恢复全球访问。已部署针对 Amazon 发现的 jailbreak 的新安全分类器（对该已报告行为的拦截率 >99%）。Pro/Max/Team 与部分 Enterprise 套餐在 7 月 7 日前可将 Fable 5 用于最多 50% 的每周用量，之后通过用量额度使用；AWS、Google Cloud、Microsoft Foundry 云渠道随后恢复。Mythos 5 仍限美国受审实体。
- [Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5) - **2026-06-30**。迄今最具 Agent 能力的 Sonnet — 支持规划、浏览器/终端工具调用，自主运行水平接近此前需要 Opus 级模型才能做到的程度。在高努力档位下，Agent 搜索（BrowseComp）与电脑操作（OSWorld-Verified）表现逼近 Opus 4.8，且相比 Sonnet 4.6 拥有更宽的性价比区间。现为 Claude.ai 免费版/Pro 版默认模型，Max/Team/Enterprise、Claude Code 及 API（`claude-sonnet-5`）均可用。**2026-08-10 更新**：输入/输出每百万 token $2/$10 的引导定价已改为**永久生效** —— 原定 9 月 1 日涨至 $3/$15 的调价取消。Anthropic 称其不良行为率低于 Sonnet 4.6。
- [Claude Fable 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) - **2026-06-09**。Anthropic 首个公开可用的 **Mythos 级别**模型——能力层级高于 Opus。在软件工程、知识工作、视觉、科研等基准全面超越 Opus 4.8。内置安全护栏（涉网络安全/生物的敏感请求可能被路由到 Opus 4.8）。$10 / $50 每百万输入/输出 token。Anthropic API、Amazon Bedrock、Google Cloud Vertex AI 可用。**⚠️ 2026-06-12 起暂停访问** —— 美国政府的出口管制指令要求 Anthropic 对所有客户停用 Fable 5 与 Mythos 5，等待安全审查。**✅ 出口管制于 2026-06-30 解除；7 月 1 日恢复访问**，并配备新的网络安全分类器 —— 见上方条目（[声明](https://www.anthropic.com/news/redeploying-fable-5)）。**2026-08-07**：[生物安全护栏误报下调](https://www.anthropic.com/news)，Fable 5 在生物相关提问上更少回退到较弱模型。
- [Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) - **2026-06-09**。与 Fable 5 同底座的 Mythos 级模型，限制更少，仅通过 **Project Glasswing**（与美国政府合作）向受信伙伴（网络安全公司、基础设施供应商）开放。4 月 Claude Mythos Preview 的正式后继。**⚠️ 2026-06-12 起暂停访问**，与 Fable 5 一同受同一出口管制指令影响（[声明](https://www.anthropic.com/news/fable-mythos-access)）。
- [Claude Opus 4.8](https://www.anthropic.com/claude/opus) - **2026-05-28**。Opus 重大迭代：代码库级别的迁移能力、更准的 Agent 判断，推出研究预览的「动态工作流」能在单 session 里并发几百个子 Agent，加入手动调节推理投入的「努力控制」面板；**Fast 模式价格降 3 倍**，输入 / 输出仍为 $5 / $25 每百万 token。Anthropic 原生、Amazon Bedrock、AWS Claude Platform、Google Cloud、Microsoft Foundry 上线。同时预告面向小范围企业的 **Mythos 级别**新一代模型。
- [Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7) - **2026-04-16 发布**。强软件工程能力（SWE-bench Verified 87.6%）、视觉增强、主动代码验证。支持 `/think xhigh` 推理力度。1M token 上下文。
- [Claude Opus 4.6](https://www.anthropic.com/) - 2026-02 发布。1M token 上下文，14.5 小时任务执行。LMArena 对话榜首。
- [Claude Sonnet 4.6](https://www.anthropic.com/news/claude-sonnet-4-6) - 2026-02 发布。前沿编程与 Agent 表现，1M token 上下文。
- [Claude Mythos Preview](https://www.anthropic.com/) - 2026-04 受邀研究预览。BenchLM 99（榜首），SWE-bench Verified 93.9%。Project Glasswing 合作伙伴专属。
- [Claude Opus 4](https://www.anthropic.com/news/claude-4) - 2025-05 发布。
- [Claude Sonnet 4](https://www.anthropic.com/news/claude-4) - 2025-05 发布。
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - Anthropic 出品、运行在终端里的 Agent 化编程工具。Opus 4.7 + `/think xhigh`。
- [Claude Security](https://www.anthropic.com/) - **2026-05-01** 公测。Opus 4.7 驱动的企业级代码漏洞扫描器：扫整个代码库，生成有置信度评分、严重程度、复现步骤、修复建议的补丁。Enterprise 用户在 [claude.ai/security](https://claude.ai/security) 使用。
- [Claude Finance Agents](https://www.anthropic.com/news/finance-agents) - **2026-05-05**。基于 Opus 4.7 的 10 个金融领域专业 Agent，覆盖 pitchbook 撰写、KYC、月结、交易筛查等。可作为 Claude Cowork 插件、Claude Code skill 或 Managed-Agents cookbook 部署。
- [Claude Finance JV](https://www.anthropic.com/) - **2026-05-04**。与高盛、黑石的 15 亿美元 Claude 部署合资公司，把 Anthropic 工程师派驻到中型华尔街机构。
- [Claude Managed Agents updates](https://claude.com/blog/new-in-claude-managed-agents) - **2026-05-19**。Managed Agents 更新记录多 Agent 协调、基于评分标准的成果判断，以及研究预览中的 dreaming；不同功能的开放范围有别。
- [Anthropic ↔ SpaceX Colossus 1](https://www.siliconrepublic.com/business/anthropic-joins-forces-with-spacex-for-colossus-capacity) - **2026-05-06**。Anthropic 拿下 SpaceX Memphis 数据中心 Colossus 1 全部算力（22 万+ NVIDIA H100 / H200 / GB200，300+ MW）用于 Claude Opus 推理；Claude Code 5 小时速率上限翻倍，Pro / Max 取消高峰期限流。
- [Anthropic ↔ AMD（最多 2 GW Instinct MI450）](https://ir.amd.com/news-events/press-releases/detail/1292/amd-and-anthropic-announce-strategic-partnership-to-deploy-up-to-2-gigawatts-of-amd-instinct-mi450-series-gpus) - 🆕 **2026-07-22**。Anthropic 将在 AMD Helios 机柜级方案中部署**最多 2 吉瓦**的 AMD Instinct MI450 系列（MI455X）GPU，搭配 EPYC "Venice" CPU、Pensando 网络与 ROCm；首个吉瓦于 2027 上半年上线。AMD 承诺对 Anthropic 进行**最多 50 亿美元**的战略股权投资，并展开多年工程合作。此前 Anthropic 已在用 MI355X —— 这是其在 TPU、Trainium 和 SpaceX Colossus 之外有意做的硬件多元化。
- [Anthropic 对开放权重模型的立场](https://www.anthropic.com/news/position-open-weights-models) - 🆕 **2026-07-27**。针对「美国官员正考虑禁止美企使用中国开放权重模型」的报道，Dario Amodei 明确表态：「Anthropic 从未主张禁止开放权重模型。」他称不具危险能力的开放权重是「公共产品」，并主张改用三项措施：芯片出口管制 + 打击走私、遏制工业规模的蒸馏行为，以及**对所有足够强大的模型（无论开源闭源）强制进行发布前安全测试**。追踪 2026 年开源 / 闭源政策之争的一手材料。
- [Claude for Legal](https://github.com/anthropics/claude-for-legal) - 🆕 **2026-05-12**。Claude Cowork 之上的法律垂直栈：**20+ 个 MCP 连接器**（iManage、NetDocuments、DocuSign、Ironclad、LexisNexis、Westlaw、Harvey、Everlaw、Relativity、CourtListener 等）+ **12 个执业领域 plugin**（商事、雇佣、隐私、产品、公司、AI 治理、诉讼助理、备考律考）。原生集成 Word / Outlook / Excel / PowerPoint。
- [Claude for Small Business](https://www.anthropic.com/news/claude-for-small-business) - **2026-05-13**。Claude Cowork 中的中小企业开关 —— 15 个预置 Agent 工作流，覆盖财务 / 运营 / 销售 / 营销 / HR / 客服；原生连 QuickBooks、PayPal、HubSpot、Canva、DocuSign、Google Workspace、Microsoft 365。配套免费课程 + 美国 10 城线下工作坊巡讲。
- [Anthropic ↔ Gates Foundation $200M](https://www.anthropic.com/news/gates-foundation-partnership) - **2026-05-14**。4 年 $200M 合作：资助 + Claude 使用额度 + Anthropic 工程师投入到全球健康、生命科学、教育、农业，所有产出工具公开免费；首批方向包括小儿麻痹 / HPV / 子痫前期疫苗研发与农业版 Claude。
- [Anthropic ↔ PwC 战略扩张](https://www.pwc.com/us/en/about-us/newsroom/press-releases/anthropic-pwc-expand-alliance-agentic-enterprise.html) - **2026-05-14**。PwC 全球铺开 Claude Code + Claude Cowork，认证 30,000 名员工，共建 "Agentic Enterprise" 卓越中心；聚焦 Agent 构建、AI 原生并购，以及财务 / 供应链 / HR 重塑。
- [Anthropic ↔ 金融稳定委员会（FSB）就 Claude Mythos 进行汇报](https://www.theguardian.com/technology/2026/may/18/anthropic-ai-claude-mythos-cyber-financial-stability-board-fsb) - **2026-05-18**。Anthropic 首次向 G20 级别的金融稳定监管机构介绍顶级模型（Claude Mythos）的攻击性网络能力，为金融系统风险评估提供依据。
- [Code with Claude 2026 会议录像上线](https://www.infoq.com/news/2026/05/code-with-claude/) - **2026-05-18 发布**。5 月 6 日的开发者大会全部场次公开：Claude Code 路线图、Claude Developer Platform 更新、Managed Agents 的 dreaming 与多 Agent 编排、合作伙伴部署。
- [《Widening the conversation on frontier AI》](https://www.anthropic.com/news/widening-conversation-ai) - **2026-05-19**。Anthropic 发布与宗教 / 哲学 / 原住民传统等“智慧传统”就顶级 AI 安全展开对话的框架，公共参与系列后续。
- [Bristol Myers Squibb ↔ Anthropic Claude Enterprise](https://news.bms.com/news/corporate-financial/2026/Bristol-Myers-Squibb-Announces-Strategic-Agreement-with-Anthropic-to-Position-Claude-Enterprise-as-the-Shared-Intelligence-Platform-Across-Its-Global-Operations/default.aspx) - **2026-05-20**。BMS 将 Claude Enterprise 作为 30,000+ 员工的共享智能平台，嵌入药物发现 / 开发 / 交付的全链路。全球前 5 大药企中首个全公司级 Claude 部署。

### Google DeepMind
- [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash) - 🆕 **2026年9月**。稳定版 `gemini-3.8-flash` 支持文本、图像、音频、视频和 PDF 输入，1,048,576 输入 token、65,536 输出 token，以及函数调用。
- [Gemini 3.7 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) - 🆕 **2026-08-13**。Google 新的「最智能主力模型」，面向编程与 Agent —— 距 3.6 Flash 仅三周即发布，且抢在仍未露面的 3.5 Pro 之前。FrontierCode 1.1 43.6%（3.6 Flash 为 34.4%），DeepSWE v1.1 65.3%（3.6 Flash 为 49.0%）。引导定价**输入/输出每百万 token $0.75/$3.75，至 2026 年 12 月 31 日**（之后 $1.50/$7.50）。已上线 AI Studio、Android Studio、Antigravity 与 Gemini Enterprise Agent Platform；为 AI Pro/Ultra 订阅用户的 Gemini Spark 提供动力。
- [Gemini 3.6 Flash](https://github.com/google-gemini/cookbook) - 🆕 **2026-07-21**。Google 的 Flash 档 —— 在复杂 agentic 与多模态任务上更强，**同时 token 用量更少、价格低于 3.5 Flash**。API id `gemini-3.6-flash`。已写入官方 Gemini API cookbook（含 thinking 模式指南）。2026-08-13 起顶级 Flash 档地位被 3.7 Flash 取代。
- [Gemini 3.5 Flash-Lite](https://github.com/google-gemini/cookbook) - 🆕 **2026-07-21**。3.5 家族里最快、最便宜的模型；在高吞吐执行上超越前几代 Flash-Lite。API id `gemini-3.5-flash-lite`。现为最便宜的 Gemini 档，新项目应优先于 3.1 Flash-Lite。
- [Gemini 3.1 Pro (preview)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview) - 支持多模态输入与1M上下文的预览推理模型；可用性和限额取决于具体端点。
- [Gemini 3.5 Pro (announcement)](https://ai.google.dev/gemini-api/docs/models) - ⚠️ **2026-09-08**核验的公共Gemini API目录未列出Gemini 3.5 Pro端点；不能将预告视为已可用，也不能推断其价格或上下文。
- [Gemma 4 12B](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/) - **2026-06**。新型多模态开源模型，采用**统一无编码器架构**，在单次计算中同时处理文本、图像和音频。支持在 16GB VRAM 显存下本地运行。
- [DiffusionGemma](https://www.marktechpost.com/2026/06/10/google-ai-releases-diffusiongemma-a-26b-moe-open-model-using-text-diffusion-for-up-to-4x-faster-generation/) - **2026-06**。采用**文本扩散 (text-diffusion)** 架构的 26B MoE 开源模型，生成速度比自回归模型快最高 **4 倍**。

- [Gemini 3.5 Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - **2026-05-19 — Google I/O 2026**。推出即成为 Gemini App + Google 搜索 AI Mode 的默认模型，官方称输出 token 速度 **约 4 倍于**同类顶级模型，在关键 benchmark 上超越 Gemini 3.1 Pro。Gemini 3.5 Pro 原定 2026 年 6 月上线，现已延期（见上）。
- [Gemini Omni / Omni Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - **2026-05-19 — Google I/O 2026**。DeepMind 面向 AGI 的新**世界模型**家族，Omni Flash 能从**任意输入输出任意模态**（首以视频起步，后续拓展到图像与文本），与 Gemini Robotics / Genie 路线一脉相承。
- [Gemini 3.1 Pro](https://deepmind.google/technologies/gemini/) - 2026-02 发布。BenchLM 94，GPQA Diamond 94.3%（世界纪录），ARC-AGI 2 77.1%。旗舰定价 `$2/1M tokens`。
- [Gemini 3.1 Flash Live](https://deepmind.google/technologies/gemini/) - 2026-04。语音助手与交互式 Agent 的实时多模态流式接口，低延迟长上下文。
- [Gemini 3.1 Flash-Lite (GA)](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-lite-is-now-generally-available) - **2026-05-08**。Gemini API / AI Studio / Vertex AI 全面 GA。Gemini 3 家族中最快、最省的型号，面向超低延迟代码补全、实时 UX、Agent 开发工具；质量持平 Gemini 2.5 Flash，成本明显更低。
- [Gemini Omni Flash · 对话式视频编辑上线](https://www.techtimes.com/articles/317309/20260528/google-gemini-omni-flash-brings-voice-controlled-ai-video-editing-future-conversational-ai.htm) - **2026-05-28**。Omni Flash 面向消费者推送，在 Gemini App、**Google Flow**和 **YouTube Shorts** 里作为编辑引擎：用文字 / 语音 / 图像 / 音频提示完成电影式推拉镜、背景替换、天气改动等操作，不再需要传统非线性编辑。
- [Gemini Spark（24/7 个人 AI Agent）](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - **2026-05-19 — Google I/O 2026**。云端 24/7 常驻的个人 AI Agent，首期接入 Gmail / Chat，后续加入 ~30+ 个第三方工具（Adobe / Dropbox / Uber 等）以 MCP 協议调用。限 Google AI Ultra 付费用户。
- [Google AI Ultra（$100/月）](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - **2026-05-19 — Google I/O 2026**。新的消费者顶端订阅层级，面向开发者 / 创作者 / 重度用户，解锁 Gemini Spark、最高 Gemini 3.5 额度以及即将发布的 Gemini 3.5 Pro。
- [Gemini 3.1 Flash / Flash Lite](https://deepmind.google/technologies/gemini/) - 高吞吐应用的高性价比选择。
- [Gemma 4 family](https://huggingface.co/google/gemma-4-31B-it) - Apache-2.0 开放权重多模态系列，包含 E2B、E4B、12B、26B A4B、31B；正确名称为 Gemma，并非已发布的开放版 Gemini 4。
- [Gemini 2.5 Pro / Flash](https://deepmind.google/technologies/gemini/) - 2025-06 GA。Thinking 模型，1M 上下文。
- [Gemma 4 31B](https://github.com/google-deepmind/gemma) - 2026-04。GPQA Diamond 84.3%。端侧推理首选开源权重之一。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle-deepmind%2Fgemma&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Gemma 3](https://github.com/google-deepmind/gemma) - 上一代开源家族。
- [Gemini Robotics ER 2](https://ai.google.dev/gemini-api/docs/robotics-overview) - 🆕 当前具身推理预览，面向空间理解与机器人工具编排，另有流式预览；替代已退役的 ER 1.6 端点。

### Meta

- [Muse Spark 1.3](https://research.meta.ai/blog/introducing-muse-spark-1-3) - 🆕 **2026年9月2日**。面向 Agent 与编程的更新，已提供于 Muse Code 和 Meta Model API，支持 max 推理；Spark 权重开放仍属路线图。
- [Muse Image](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) - 🆕 **2026-07-07**。Meta Superintelligence Labs 最新图像生成模型 —— “Agent 式”架构，在生成图像前能自动完成网页搜索、代码执行、自我修正等中间步骤。已集成到 Meta AI 应用、Instagram Stories（美国）与限定国家的 WhatsApp（Facebook 即将上线）。注：一项允许使用其他用户公开 Instagram 头像生成图像的争议功能上线后，因用户反馈于 7 月 10 日下线。
- [Muse Spark 1.1](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/) - 🆕 **2026-07-09**。面向 Agent 任务的多模态推理模型，通过新的 Meta Model API 公开预览发布。标志着 Meta 在开源 Llama 路线之外开始构建专有商业模型。
- [Muse Video](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) - 🆕 **2026-07-07（预览）**。Meta Superintelligence Labs 的视频生成模型，与 Muse Image 同底座；Arena 文生视频榜第 3。随 Muse Image 发布一同预览 —— "即将面向创作者与 Meta AI 开放"。
- [Muse Spark 1.2 + Muse Code（beta）](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2) - 🆕 **2026-08-05**。**Muse Code** 是 MSL 的终端编程 Agent（异步后台 Agent、可精确重放的本地事件日志、`/plan` / `/grill` / `/goal` skills），由新的 **Muse Spark 1.2** 驱动 —— 该模型针对整仓库生成与长程编程任务训练。Spark 1.2 同时登陆 Meta Model API，并扩大全球开放范围。
- [Muse Glimmer 30B](https://huggingface.co/meta-models/Muse-Glimmer-30B) - 🆕 **2026-08-10**。Meta Superintelligence Labs 出品的 300亿Openweight多模态模型，Apache 2.0 许可。专为**常驻本地 Agent 工作流**设计，可在单张消费级 GPU 或 Apple Silicon 上流畅运行。131K token 上下文窗口，支持 100+ 语言，DFlash 加速。Muse Spark 蜗牌优化，键向编程、评测与 Agent 任务。支持 llama.cpp / MLX / ExecuTorch 集成。
- **Llama 5** - ❌ **不存在。于 2026-07-30 核实后从本表删除。** "Llama 5、600B+、2026-04-08" 这条说法在 AI 资讯聚合站和大模型搜索摘要里广为流传,也曾被写进本表。它经不住核实:Hugging Face 的 `meta-llama` 组织下 **没有任何 Llama-5 权重**(Llama 系最新上传仍是 2025-05 的 Llama-4-Maverick),而维基百科 Llama 条目明确写着"最新版本是 2025 年 4 月发布的 Llama 4",并指出 **2026 年 4 月 Muse Spark 已取代 Llama 产品线**。在 Meta 真正发出权重或官方公告前,任何"Llama 5"说法都应当未经核实处理。实际上线的产品见上方 [Muse Spark](#meta)。
- [Muse Spark](https://ai.meta.com/blog/introducing-muse-spark-msl/) - **2026-04-09**。Meta Superintelligence Labs (MSL) 首个模型。原生多模态推理，驱动 Meta AI 应用、智能眼镜，以及 Facebook / Instagram / WhatsApp / Messenger 中的功能。
- [Llama 4 Scout](https://llama.meta.com/) - 109B 总参（17B 激活），16 专家 MoE，10M token 上下文，多模态。单 H100 可跑。
- [Llama 4 Maverick](https://llama.meta.com/) - 400B 总参（17B 激活），128 专家，1M 上下文。多模态超过 GPT-4o。
- [Llama 4 Behemoth](https://llama.meta.com/) - 2T 总参（288B 激活）。Meta 最强模型，对标顶级闭源。
- [Llama 3.3 70B](https://llama.meta.com/) - 强指令跟随，Llama Community License。

### Sakana AI

- [Sakana Namazu](https://console.sakana.ai/models) - 日语专用 LLM，API ID 为 `sakana-namazu-v1.0`；`sakana-namazu` 别名跟随当前版本。
- [Sakana RL Conductor](https://venturebeat.com/orchestration/how-sakana-trained-a-7b-model-to-orchestrate-gpt-5-claude-sonnet-4-and-gemini-2-5-pro) - **论文 2026-04-27 / Fugu beta 2026-04 末至 2026-05 初**。基于 Qwen2.5-7B 的 RL 训练编排模型，用强化学习把子任务分发给 GPT-5、Claude Sonnet 4、Gemini 2.5 Pro 等。LiveCodeBench 83.9%、GPQA-Diamond 87.5% SOTA，每次查询约 1.8K token，远低于其他多 Agent 合奏。
- [Sakana Fugu / Fugu Ultra](https://console.sakana.ai/models) - 模型编排 API，提供 `fugu`、`fugu-ultra-v1.1` 与按量计费的 `fugu-cyber-v1.0`，兼容 OpenAI Responses 和 Anthropic Messages。

### Zyphra

- [ZAYA1-8B](https://www.zyphra.com/models/zaya1-8b) - **2026年5月6日**。采用 AMD MI300X 基础设施训练的小型 MoE 推理模型，权重以 Apache-2.0 发布。
- [ZAYA1-8B-Diffusion-Preview](https://www.zyphra.com/post/zaya1-8b-diffusion-preview) - **2026-05-14**。首个从自回归 LLM 转换得来的 MoE 扩散语言模型，也是首个在 AMD GPU 上训练的扩散 LM。每步生成 16 个 token，相比自回归基线最多 **7.7× 推理加速**；采用 Zyphra 的 TiDAR 训练配方 + CCA 注意力。

### Thinking Machines Lab

- [Inkling](https://thinkingmachines.ai/inkling/) - **2026年7月15日**。Apache-2.0 MoE 模型，总参数 975B、激活 41B，原生支持文本、图像、音频输入；模型支持 1M 上下文，Tinker 服务上限较低。
- [Inkling-Small](https://thinkingmachines.ai/inkling/) - 🆕 **2026-07-30（权重已发布）**。Inkling 的轻量化变体 —— 276B 总参 / 12B 激活，相同原生多模态架构（文本/图像/音频），1M token 上下文，Apache 2.0。HLE 文本基准 **31.6%**，略超较大的 975B Inkling 版本（该指标 29.7%）。可通过 Thinking Machines API 和 Hugging Face 使用。

### Mistral AI

- [Voxtral Mini Transcribe Realtime](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602) - Apache-2.0 开放权重流式语音识别模型，与语音生成用途的 Voxtral TTS 不同。
- [Shieldstral 1.0](https://docs.mistral.ai/models/shieldstral-1-0) - 🆕 **2026年8月4日**。Apache-2.0 文本/图像内容审核模型，处于公开预览；支持策略问题、提示词与回复对及拒答分类。
- [Mistral OCR 4.1](https://docs.mistral.ai/models/ocr-4-1) - 文档 OCR 服务，输出段落边界框、结构块标签及置信度分数。
- [Mistral Large 3](https://mistral.ai/news/mistral-3) - 675B 总 / 41B 激活 MoE，256K 上下文。多模态旗舰开源。2025-12 发布。
- [Mistral Medium 3.1](https://docs.mistral.ai/models) - 📦 2025年历史版本，现列入弃用/退役目录；当前Medium条目为Mistral Medium 3.5。
- [Mistral Small 4](https://mistral.ai/news/mistral-small-4) - 2026-03。119B 总 / 6B 激活。融合推理 + 多模态 + 编程的混合模型。
- [Magistral 1.2](https://docs.mistral.ai/models) - 📦 2025年9月发布的历史Medium/Small推理变体，现处于Mistral弃用/退役目录。
- [Devstral 2](https://docs.mistral.ai/models/devstral-2-25-12) - 模型卡版本为2025年12月的历史Agent编程模型；部署前须核对生命周期状态。
- [Codestral 2508](https://docs.mistral.ai/models/codestral-25-08) - Mistral 当前目录中的代码补全模型；参数应以该版本模型卡为准，不能沿用 2024 年初版 22B 的规格。
- [Pixtral Large](https://mistral.ai/) - 124B 多模态 + 1B 视觉编码器，128K 上下文，支持 30+ 高分辨率图像。
- [Ministral 3B/8B/14B](https://mistral.ai/) - 端侧紧凑模型。
- [Mistral Forge](https://mistral.ai/) - 2026-03 自定义 LLM 训练平台。
- [Mistral Medium 3.5](https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04) - **2026-04-28**。Dense 128B 开放权重模型，256K 上下文，Modified MIT 许可。统一指令跟随、推理与代码能力。
- [Leanstral 1.5](https://mistral.ai/news/leanstral-1-5/) - 🆕 **2026-07-02**。面向 Lean 4 证明工程的形式化验证模型 —— 119B 总 / 6B 激活参数，Apache 2.0，权重上 Hugging Face 并提供免费 API 端点。miniF2F 得分 100%，解决 PutnamBench 672 题中的 587 题，并在 57 个真实仓库中发现 5 个此前未被报告的 bug。
- [Robostral Navigate](https://mistral.ai/news/robostral-navigate/) - 🆕 **2026-07-08**。Mistral 首个机器人模型 —— 8B 具身导航模型，仅凭单个 RGB 摄像头即可让轮式、足式与飞行机器人根据自然语言指令穿行办公室、家庭与户外环境（未见过的验证场景成功率 76.6%）。完全自研，基于约 40 万条仿真轨迹训练。
- [Voxtral TTS](https://docs.mistral.ai/models/voxtral-tts-26-03) - 支持声音克隆与多语言的开放权重语音生成模型；权重为 CC-BY-NC-4.0，商业部署须另获授权。

### DeepSeek 🇨🇳

- [DeepSeek-V4-Pro-0813 (GA)](https://api-docs.deepseek.com/news/news260813) - **2026年8月13日**。`deepseek-v4-pro` 对应的生产检查点，支持推理强度配置和 Responses API；峰谷计价已于8月16日生效。
- [DeepSeek-V4-Pro](https://api-docs.deepseek.com/news/news260424) - **2026-04-24（预览）；2026 年 7 月中旬正式上线**。1.6T 总 / 49B 激活 MoE，1M 上下文。MIT。Agent、世界知识、推理领域开源标杆。最大输出 384K，并发上限 500。`deepseek-v4-pro` / `deepseek-v4-flash` 为生产 API 模型（V4-Pro 自 8 月 13 日起服务 0813 检查点 —— 见上；2026-08-16 起实行高峰/低谷分层计价）。
- [DeepSeek-V4-Flash](https://api-docs.deepseek.com/news/news260424) - 2026-04-24。284B 总 / 13B 激活 MoE，1M 上下文。MIT。性价比层 —— 2026-08-16 起：高峰每 100 万 token **命中缓存输入 $0.014 / 未命中 $0.44，输出 $1.32**，低谷 **$0.007 / $0.22 / $0.66**；最大输出 384K，并发上限 2500（[定价](https://api-docs.deepseek.com/quick_start/pricing)）。
- [DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731) - 🆕 **2026-07-31**。DeepSeek 发布的更新 Flash 检查点 —— 相同 284B/13B 激活 MoE 架构，相同 API/定价，但在 Agent 任务基准上表现优于 V4-Pro（预览版）。MIT 协议开源至 Hugging Face，直接替换 `deepseek-v4-flash` API 用户即可使用。
- [DeepSeek-V4-Flash-Vision-Exp](https://api-docs.deepseek.com/news/news260821) - 🆕 **2026-08-21**。实验性多模态 API 模型（`deepseek-v4-flash-vision-exp`）：文本 / Agent / 推理对齐 V4-Flash，多模态 Agent 基准接近 Opus-4.8。图像按 V4-Flash 计价（每张最多 384 token）；支持 Chat Completions / Messages / Responses；可用 base64、URL 或 Files API。同日上线免费 **Files API**（上传一次后用 `file_id` 复用）。DeepSeek Harness 0.1.1 当天支持。
- [DeepSeek Agent Harness 团队](https://www.scmp.com/tech/big-tech/article/3354113/deepseek-recruits-former-jane-street-engineer-catch-ai-agents-revenue-race) - **2026-05-19**。DeepSeek 从 Jane Street 挨角一名资深工程师，为新设的 "AI harness" 团队搭建把 DeepSeek V4 所能生产化为 **能收费的自主 Agent** 的硬调度 / 程序化套件 —— 首个明确信号：DeepSeek 开始从原生模型 R&D 跳到 Agent 产品化。
- [DeepSeek-V3.2](https://www.deepseek.com/) - 2025-12 发布。671B MoE，V3.2 Speciale 推理增强。⚠️ V3.2 时代的 API 模型 ID deepseek-chat / deepseek-reasoner 将于 2026-07-24 弃用 —— 由 V4-Flash 各模式接替。
- DeepSeek-R2 - 🧪 **未发布 / 传闻。** 截至 2026 年 7 月中旬无官方公告、模型卡或 API ID；推理能力通过 V4 的 Thinking 模式提供。
- [DeepSeek-R1](https://www.deepseek.com/) - 2025-01 发布的思维链推理模型。
- [DeepSeek-Coder-V2](https://github.com/deepseek-ai/DeepSeek-Coder-V2) - 编程模型，对标 GPT-4。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeepseek-ai%2FDeepSeek-Coder-V2&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Alibaba (Qwen) 🇨🇳

- [Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) - 🆕 **2026年8月**。实验性多模态 MoE：125B 参数/6B 激活，另含 51B n-gram 表和 4B MTP；原生 262K 上下文，可扩展至 1M，采用 Qwen Community License 1.0。
- [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) - 🆕 **2026-08-14**。Qwen3.8-Max 的开源权重 27B 多模态（文本/图像/视频输入）蒸馏版，以 **Apache 2.0** 协议发布至 Hugging Face —— 面向约 24 GB 显存的消费级 GPU（RTX 4090 级别）。Qwen3.8-Max 发布时承诺的开源权重配套模型，如期交付。
- [Qwen3.8-Max / Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) - **2026年8月**。多模态旗舰，已有官方可下载检查点；完整模型权重采用 Qwen 自定义许可，独立的 Qwen3.8-27B 检查点则采用 Apache-2.0。
- [Qwen 3.7-Max](https://www.scmp.com/tech/big-tech/article/3354212/alibaba-unveils-new-qwen-model-custom-chips-bid-become-chinas-ai-factory) - **2026-05-20 — 阿里云杭州峰会**。为 AI Agent 量身打造的新一代顶级：代理型编程、复杂推理、「长静间距」多步任务能力；同期亊相新的 T-Head **珄武 M890** AI 算力芯片与全栈 AI 基础设施升级。面向全球开发者 / 企业即将上线。
- [Qwen 3.7-Max-Preview / Plus-Preview](https://www.scmp.com/tech/tech-trends/article/3354087/alibaba-teases-new-qwen-previews-highest-ranking-chinese-ai-models-arena) - **2026-05-18**。杭州峰会前的预览梯队；LM Arena 上文本 + 视觉双赛道均为**中文世界最高分**中国模型。
- [Qwen3.6-27B](https://qwen.ai/blog?id=qwen3.6-27b) - **2026-04-22**。27B 密集多模态。开源。Agent 编程 + 思维上下文保持。
- [Qwen3.6-Max-Preview](https://qwen.ai/) - **2026-04-18**。闭源前沿预览。1M 上下文，中文模型编程榜顶尖。
- [Qwen3.6-35B-A3B](https://qwen.ai/blog?id=qwen3.6-35b-a3b) - **2026-04-15**。MoE 35B 总 / 3B 激活。Apache 2.0。稳定性与实用性增强。
- [Qwen3.6-Plus](https://qwen.ai/) - **2026-04-02**。闭源旗舰。token 性价比高，长上下文 + 工具调用 + Agent 表现强。
- [HappyHorse 1.1](https://technode.com/2026/06/23/alibaba-unveils-happyhorse-1-1-video-generation-model-launches-global-ai-filmmaking-competition/) - 🆕 **2026-06-23**。阿里视频生成模型（T2V/I2V/S2V，最长 15 秒 1080p 带同步音频，多镜头角色一致性强）。HappyHorse 1.0 曾匿名上线并登顶视频榜单，2026-04-28 进入限量公测。
- [Qwen3.5 Max Pro](https://qwen.ai/) - 2026-04。高性能旗舰。
- [Qwen3.5 Omni Plus](https://qwen.ai/) - 2026-04。统一文本 + 图像输入的全模态基座。
- [Qwen3-Max-Thinking](https://qwen.ai/) - 阿里最强思维模型。1T+ 参数。
- [Qwen3.5-Omni](https://qwen.ai/) - 2026-03。完全全模态：文/视/听/动。113 种语言识别，256K 上下文。
- [Qwen3-Coder-Next](https://qwen.ai/) - 2026-02。开源编程 Agent 模型，MoE 80B 总 / 3B 激活。
- [Qwen3 235B-A22B](https://qwen.ai/) - 双模式推理 MoE。数学、代码、常识强。
- [Qwen2.5 Coder 32B](https://github.com/QwenLM/Qwen3-Coder) - 顶级开源编程模型。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FQwenLM%2FQwen3-Coder&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### xAI / SpaceXAI (Grok)

- [Grok 4.6](https://x.ai/news/grok-4-6) - **2026年8月12日**。通过 API、Cursor、Grok Build 提供的编程与 Agent 模型，每百万 token 输入/输出起价 $2/$6；Fast 价格翻倍。
- [Grok Bot](https://docs.x.ai/docs/release-notes) - 🆕 **2026-08-11（早期 beta）**。可长期存续的 AI 队友，运行在**持久化云端计算机**上，支持消息、审批、连接器与例行任务 —— xAI 进军常驻自主 Agent 领域之作。可通过 SuperGrok Heavy、Cursor Ultra 与 Cursor Teams Premium 使用。
- [Grok 4.5](https://x.ai/) - 🆕 **2026-07-08**。与 Cursor 共同训练，利用真实开发者交互数据优化编程与 Agent 能力。支持 500K token 上下文、函数调用、结构化输出、web/X 搜索、代码执行、文档搜索与上下文压缩。定价 $2/$6 每百万 token。EU API 控制台于 2026-07-17 上线。2026-08-12 起旗舰地位被 Grok 4.6 取代。
- [Grok 4.3 GA](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-grok-4-3-on-microsoft-foundry-latest-generation-agentic-capabilities/4517096) - **2026-05**。Grok 4.3 在 Microsoft Foundry 与 OCI Generative AI 上 GA；xAI 面向 Agent 工作负载的旗舰，工具调用与长链推理能力升级。
- [Grok 4.3 Beta](https://x.ai/) - 2026-04。最新迭代，推理与编程基准提升，详见 [`2026.4` benchmark snapshot](https://benchlm.ai/)。
- [Grok 4.20](https://x.ai/) - 2026-02。多 Agent 系统（Heavy 模式 4 标准 + 16 专家 Agent），2M 上下文。
- [Grok 4 / 4 Heavy](https://x.ai/) - 2025-07 发布。xAI Grok 4 世代的前沿模型。
- [Grok 3 / 3 Mini](https://x.ai/) - 2025-02。首批 "Think Mode" 推理模型。

### Microsoft (MAI)

- [MAI-Transcribe-2](https://microsoft.ai/news/mai-transcribe-2-is-the-fastest-most-accurate-and-cheapest-speech-recognition-model-in-the-world/) - 🆕 **2026年9月3日**。语音识别模型，支持说话人区分、词级时间戳、词汇偏置与60种语言；促销价为每小时音频 $0.10，持续至年底。
- [Microsoft MAI-Code-1-Flash](https://microsoft.ai/news/introducingmai-code-1-flash/) - **Build 2026（2026 年 6 月 2 日）**。微软首个完全脱离 OpenAI 技术、从零自研的编程基础模型。5B 参数，自适应思考长度，已上线 GitHub Copilot。在四大核心编程基准上击败 Claude Haiku 4.5（SWE-Bench Pro 51.2% vs 35.2%，领先 16 分），SWE-Bench Verified 任务最多省 60% token。
- [Microsoft MAI-Thinking-1](https://microsoft.ai/news/microsoft-build-2026-mai-keynote-transcript/) - **Build 2026（2026 年 6 月 2 日）**。微软首个完全脱离 OpenAI 数据、从零自训的推理模型；与 MAI-Code-1-Flash 同发，标志微软的基础模型独立进程。
- [MAI-Code-1.1-Flash](https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/) - 🆕 **2026-08-11**。相对 6 月 1.0 的生产 Copilot 主力：代码质量更高、**token 效率 +25%**、**成本约 1/4**；Terminal-Bench 2.1 +22%，.NET 任务 +15%。
- [MAI-Image-2.6](https://microsoft.ai/news/mai-image-2-6-launches-at-no-2-on-arena-ahead-of-google-meta-and-xai/) - 🆕 **2026-08-10**（Arena 编辑榜更新 **08-18**）。发布时 Arena 文生图第 2；到 8 月 18 日图像编辑第 3，高于 Nano Banana 与 Muse Image（相对 2.5 +79 Elo）。MAI Playground + Foundry 私有预览。
- [MAI-Cyber-1-Flash](https://microsoft.ai/news/introducing-mai-cyber-1-flash-inside-mdash/) - 🆕 **2026-08-13**。MDASH 内的网络安全模型；微软称以领先模型约 **50% 成本**达到世界级表现。

### Microsoft (Phi)

- [Phi-4-reasoning-vision-15B](https://huggingface.co/microsoft/Phi-4-reasoning-vision-15B) - MIT 许可的15B视觉语言模型，结合图像理解与推理；部署要求以官方检查点说明为准。
- [Phi-4](https://azure.microsoft.com/en-us/products/phi) - 14B SLM，推理水平媲美更大模型。MIT。
- [Phi-4-mini](https://azure.microsoft.com/en-us/products/phi) - 3.8B 密集，128K 上下文。推理 / 数学 / 编程 / 函数调用都强。
- [Phi-4-multimodal](https://azure.microsoft.com/en-us/products/phi) - 5.6B 首个多模态 Phi（语音 + 视觉 + 文本）。

### Cohere

- [Command A+](https://docs.cohere.com/docs/command-a-plus) - **2026年5月**。`command-a-plus-05-2026` 统一图像输入、推理、工具使用与翻译，支持128K输入上下文和64K输出。
- [Command A](https://docs.cohere.com/v2/changelog/command-a) - 2025-03-13 发布。111B 开源权重，256K 上下文。Agent / 多语言 / 编程聚焦。
- [Command R+](https://cohere.com/) - 企业级 RAG 模型，128K 上下文，10 种语言，带引用 grounded generation。
- [Command R](https://cohere.com/) - 经济型 RAG 模型。

### Baidu (ERNIE / 文心) 🇨🇳

- [ERNIE 5.1](https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/) - **官方发布文：2026年5月9日**。通过异步强化学习与 Agent 后训练增强写作、推理及工具任务的文心模型更新。
- [ERNIE 5.0](https://ernie.baidu.com/) - 2025-11-13 发布（百度世界大会）。2.4T 参数全模态 MoE（每次激活 <3%）。
- [ERNIE 4.5](https://yiyan.baidu.com/) - 2025 多模态前作。中文与推理强。

### Zhipu AI / Z.ai (GLM) 🇨🇳

- [GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash) - 🆕 MIT 许可多模态 MoE，总参数320B、激活18B，采用稀疏/线性混合注意力并支持配置推理强度。
- [GLM-5.3](https://huggingface.co/zai-org/GLM-5.3) - 🆕 官方编程/推理权重现已可下载，采用自定义 GLM-5.3 License，并非 GLM-5.2 的 MIT；支持 vLLM/SGLang 部署。
- [GLM-5.2](https://z.ai/blog/glm-5.2) - **2026-06-13**。编程优先的 744B MoE 旗舰，**100万 token 上下文**（约为 GLM-5.1 的 5 倍），输出最高 131K token。已上线全部 GLM Coding Plan 套餐；MIT 开源权重 + 独立 API 于发布当周陆续放出。开箱兼容 Claude Code、Cline、OpenCode、Roo Code、Goose、OpenClaw。（发布时未公布基准分数。）
- [GLM-5.1](https://z.ai/blog/glm-5.1) - **2026-04-08**。744B MoE / 40B 激活，200K 上下文。MIT。SWE-Bench Pro 第一。
- [ZCode](https://www.scmp.com/tech/tech-trends/article/3359170/zhipu-ai-releases-harness-glm-52-model-chinese-firm-takes-aim-anthropic) - 🆕 🇨🇳 **2026-07-02**。智谱为 GLM-5.2 打造的 Agent harness —— 把模型变成自主编程 Agent，正面对标 Claude Code；发布促销包括 Coding Plan 订阅用户 +50% 配额、新用户 500 万免费 token。
- [GLM-5 Reasoning](https://z.ai/) - 2026-04。BenchLM 85 —— **开源最高分**。SWE-Bench Pro 超过 GPT-5.4 与 Claude Opus 4.6。
- [GLM-5V-Turbo](https://z.ai/) - 2026-04。原生多模态 Agent —— 视觉、视频片段、文本输入。性价比平衡。
- [GLM-5](https://z.ai/) - 2026-02 发布。744B 参数，Agent 能力前沿。MIT。
- [GLM-4.7](https://z.ai/) - 2025 末发布。SWE-Bench 持平 Claude Opus 4。

### MiniMax

- [MiniMax M3](https://huggingface.co/MiniMaxAI/MiniMax-M3) - 面向编程与 Agent 任务的开放权重多模态模型，采用 MiniMax Sparse Attention，支持1M上下文；权重为 MiniMax Community License。
- [MiniMax-M2.7 (开源权重)](https://www.minimax.io/) - 2026-04。230B 级开源权重旗舰。编程与 Agent 任务顶级表现。
- [MiniMax M2.7 (release history)](https://huggingface.co/MiniMaxAI/MiniMax-M2.7) - MiniMax较早的Agent/编程模型，已有可下载权重及专属许可；云端发布描述不能据此解释为仍仅有闭源服务。
- [MiniMax M2.5](https://www.codemotion.com/magazine/ai-ml/minimax-m2-5-low-costs-high-performance/) - 🇨🇳 **2026-02**。230B 参数旗舰，主打 "真实世界生产力" 与高性价比。
- [MiniMax H3](https://huggingface.co/MiniMaxAI/MiniMax-H3) - 🆕 🇨🇳 **2026-07**（HF 创建于 7 月 28 日）。开源权重全模态生成：理解文本/图像/视频/音频，输出最高 2K / 15 秒、带原生立体声音频的视频。33B 稠密 Omni Transformer；`minimax-h3-community-license-agreement`。现为 MiniMax 视频旗舰（接替 Hailuo 2.3）。HF 下载 440 万+。
- [Hailuo 2.3 / 2.3 Fast](https://www.minimax.io/news/minimax-hailuo-23) - 🇨🇳 **2025-10**。前代视频模型 —— SOTA 物理效果、角色微表情、强风格化；Hailuo 02（2025）仍作为聚焦 I2V 的变体保留。视频旗舰已由 MiniMax H3（2026-07）接替。
- [MiniMax Music 3.0](https://huggingface.co/MiniMaxAI/MiniMax-Music3) - 🆕 🇨🇳 **2026-08-13**。开源权重音乐模型，可生成最长 **五分钟** 完整歌曲（8B Global LLM + 0.6B Local LLM，32 kHz 16-bit 立体声 WAV）。现为 MiniMax 音乐旗舰。
- [MiniMax Music 2.6](https://aimlapi.com/blog/the-ultimate-guide-to-minimax-models-2026-m2-7-music-2-6-hailuo-video-advanced-tts) - 🇨🇳 **2026-04-10**。翻唱向前代；音乐旗舰已由 Music 3.0 接替。
- [MiniMax-M1-80k](https://www.minimax.io/) - 开源混合注意力推理模型。456B 参数，1M token 上下文。
- [Hailuo AI (视频)](https://hailuoai.video/) - 文生 / 图生视频，AI 主播 + 配音 + 角色一致性。
- [Kilo Code 集成](https://www.minimax.io/) - MiniMax 系列模型在 Kilo Code（kilo.ai 的开源 AI 编程扩展）中被重点采用。

### Moonshot AI (Kimi) 🇨🇳

- [Kimi K3](https://huggingface.co/moonshotai/Kimi-K3) - 开放权重多模态 MoE，总参数2.8T、激活104B，1M上下文；自定义 Kimi K3 License 对大型模型服务业务另有条款。
- [Kimi K2.7 Code](https://kimi.ai/) - **2026-06-12**。K2.6 的编程优先继任者 —— 1T MoE / 32B 激活（384 专家），256K 上下文，Modified MIT，已上 Hugging Face + Kimi API。面向长程 Agent 编程，推理 token 用量约降 30%；官方 Kimi Code Bench v2 较 K2.6 +21.8%（厂商基准）。每百万输入/输出 0.95 / 4.00 美元。
- [Kimi K2.6](https://kimi.ai/) - **2026-04-20~21**。1T MoE / 32B 激活，256K 上下文。编程增强、长任务执行、**最大 1000 个 Agent 协作集群**。支持 `thinking.keep="all"` 持久推理。OpenClaw v2026.4.20+ 默认模型。
- [Kimi K2.5](https://kimi.ai/) - 2026-01 至 02。1T 总 / 32B 激活 MoE。原生多模态，最多 100 个并行子 Agent。开源。⚠️ 2026-05-25 已停止支持；不再向新注册用户开放，**平台将于 2026-08-31 全面下线** —— 请迁移到 K2.6。
- [Kimi Code](https://kimi.ai/) - 基于 K2.5/K2.6 的高级编程层，面向终端工作流。

### ByteDance (Doubao / 豆包) 🇨🇳

- [Seed 2.1](https://seed.bytedance.com/en/seed2_1) - 🆕 当前 Seed 模型，面向通用 Agent 任务与端到端编程，提供官方评测和产品访问入口。
- [Doubao 2.0](https://www.taipeitimes.com/News/biz/archives/2026/02/16/2003852382) - 🇨🇳 **2026-02**。面向 Agent 时代的升级，专注真实任务执行；驱动字节跳动多款消费级 AI 应用。
- [Seedance 2.0](https://economictimes.indiatimes.com/us/news/seedance-2-0-goes-live-as-bytedances-ai-videos-ignite-china-market-rally/articleshow/128150649.cms) - 🇨🇳 **2026-02**。多模态电影级视频生成，2K 分辨率，比 Seedance 1.5 快约 30%。
- [Doubao-Seed-2.0 Pro](https://seed.bytedance.com/en/seed2) - Seed 2.0 Pro 是字节跳动 Seed 2.0 系列的推理与 Agent 工作层级；端点可用性和价格以所在区域的 ModelArk 目录为准。
- [Doubao-Seed-2.0 Lite](https://seed.bytedance.com/) - 通用生产负载。性能效率均衡。
- [Doubao-Seed-2.0 Code](https://seed.bytedance.com/) - 软件开发：代码生成、调试、评审。
- [BAGEL](https://github.com/bytedance-seed/BAGEL) - 字节开源多模态模型，文图视频统一理解 + 生成。

### Amazon (Nova)

- [Nova 2 Omni](https://docs.aws.amazon.com/nova/) - Amazon Nova 2 官方产品线中的多模态理解与生成模型。
- [Nova 2 Pro](https://docs.aws.amazon.com/nova/) - Nova 2 系列的推理模型；访问方式、区域可用性和支持模态请以 Amazon Nova 2 官方指南为准。
- [Nova 2 Lite](https://aws.amazon.com/nova/) - **2025-12-02**。快速、高性价比推理，1M token 上下文 + 可调 "thinking effort"。
- [Nova 2 Sonic](https://aws.amazon.com/nova/) - **2025-12-02**。实时语音对语音模型。多语言。
- [Nova Act](https://aws.amazon.com/nova/) - **2025-12-02**。浏览器 Web 任务 Agent 服务，由 Nova 2 Lite 驱动重新上线。
- [Nova Forge](https://aws.amazon.com/nova/) - **2025-12-02**。用自有数据构建自定义 Nova 变体的 "open training" 服务。

### NVIDIA (Nemotron)
- [Nemotron 3.5 Lightning](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16) - 面向高效 Agent 任务的开放权重模型，总参数30B、激活3B，提供官方 BF16 和 NVFP4 检查点；许可须按各工件附带的 NVIDIA 条款确认。
- [Nemotron 3.5 ASR](https://developer.nvidia.com/nemotron) - **2026-06-06**。NVIDIA 6 亿参数的 cache-aware 流式语音识别模型 —— 覆盖 40 个语言区域的实时转录。
- [Nemotron 3 Ultra (550B)](https://research.nvidia.com/labs/nemotron/Nemotron-3-Ultra/) - 🆕 **2026-06-04**。开源权重 550B 总 / 55B 激活的混合 Mamba-Transformer MoE，面向长时运行 Agent。美国开源模型中的前沿推理水平，为 Blackwell 优化。
- [Nemotron-Labs-TwoTower](https://huggingface.co/nvidia/Nemotron-Labs-TwoTower-30B-A3B-Base-BF16) - 🆕 🧪 **2026-07-01**。NVIDIA Research 的开源权重扩散语言模型，改造自冻结的 Nemotron-3-Nano-30B-A3B 底座 —— 一座塔保持上下文，另一座塔并行输出 token，无需重训即可获得约 2.4× 吞吐。
- [Nemotron 3 Super](https://developer.nvidia.com/nemotron) - 2026-03-11 发布（GTC）。120B 总 / 12B 激活。1M 上下文。吞吐较前代提升 5 倍。
- [Nemotron 3 Nano](https://developer.nvidia.com/nemotron) - **2025-12-15**。经济型 Transformer-Mamba 混合 MoE。为目标化 Agent 任务优化。
- [Nemotron 3 Nano Omni](https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/) - **2026-04-28**。30B-A3B 混合 MoE。原生多模态。同类开源 omni 模型 9 倍吞吐。霸榜 6 项排行（MMlongbench-Doc / OCRBenchV2 / WorldSense / DailyOmni / VoiceBench）。

### Tencent (Hunyuan) 🇨🇳

- [Hunyuan Hy3](https://huggingface.co/tencent/Hy3) - Apache-2.0 开放权重 MoE，面向推理和工具使用，提供官方检查点与部署说明。
- [Hunyuan Hy3 Preview](https://hy.tencent.com/hy3-preview) - 🇨🇳 **2026-04**。Hy3 正式版之前的预览版："快慢思维融合" 架构，推理效率提升 40%，支持 vLLM 与 SGLang。GitHub / Hugging Face / ModelScope / GitCode 同步开源。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTencent-Hunyuan%2FHy3-preview&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Apple

- [Apple Foundation Models 3 / ADM 3 Cloud](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) - **2026年6月8日**。共五款模型：端侧 AFM 3 Core/Core Advanced、服务端 AFM 3 Cloud/Cloud Pro，以及在 Private Cloud Compute 运行的图像生成模型 ADM 3 Cloud。
- [OpenELM](https://machinelearning.apple.com/research/openelm) - 开源高效语言模型（270M~3B），Apple Silicon 端侧。

### Samsung

- [Samsung Gauss2](https://news.samsung.com/sg/samsung-electronics-hosts-samsung-developer-conference-korea-2024-unveils-its-improved-gen-ai-model) - 三星官方已记录的专有多模态系列，包含 Compact、Balanced、Supreme，用于内部生产力；本轮未核验到公开的 Gauss 2.3 API 或模型卡。

### StepFun 🇨🇳

- [Step 3.7 Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash) - Apache-2.0 开放权重视觉语言 MoE，面向 Agent 编程与搜索，附有官方部署说明。
- [Step 3.5 Flash](https://github.com/stepfun-ai/Step-3.5-Flash) - 🇨🇳 **2026-02**。开源权重 196B MoE（11B 激活）推理 + Agent 模型；以小搏大，对标更大体量的旗舰。

### Baichuan 🇨🇳

- [Baichuan-M4 (research)](https://arxiv.org/abs/2606.08982) - **2026年6月8日**。持续照护医疗 Agent 系统研究报告，结合推理模型、长期患者记忆、循证检索与多模态临床工具；论文不能证明 API 或权重已公开可用。
- [Baichuan-M3-235B](https://huggingface.co/baichuan-inc/Baichuan-M3-235B) - 官方 235B 医疗领域模型，权重可下载并采用 Apache-2.0。
- [Baichuan-M3 Plus](https://github.com/baichuan-inc/baichuan-mcp-servers/blob/main/packages/baixiaoying-mcp-server/README_EN.md) - 医疗领域模型，为符合条件的机构提供申请制访问计划；可用性与用途限制以百川官方条款为准。

### Inflection AI

- [Inflection 2.5 / Pi](https://inflection.ai/labs) - Inflection 的历史模型世代；实验室仍在开展个人智能研究及 Pi 产品工作，不应标注为已放弃的项目。

### 01.AI 🇨🇳

- [Yi-Lightning](https://www.01.ai/) - **2024年10月**。历史100B MoE模型；01.AI当前产品包括2026年7月发布的 TrueNorth 等企业平台。

### 中国科学院 🇨🇳

- [ScienceOne 100 / 磐石100](https://english.cas.cn/newsroom/cas-in-media/202604/t20260429_1158251.shtml) - **2026年4月**。中科院以 ScienceOne 和学科专用模型构建的科研 AI 系统，配有面向科研工作流的工具。

---

## 🎨 多模态与生成式 AI

*生成与编辑图像、视频、音频、音乐的工具与模型。*

### 图像生成

- [Nano Banana 2 Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image) - Google 高效图像生成/编辑变体，Gemini API ID 为 `gemini-3.1-flash-lite-image`。
- [Grok Imagine Image 2.0](https://x.ai/news/grok-imagine-image-2) - 🆕 **2026-08-07**。SpaceXAI 的图像生成/编辑模型 —— 魔棒编辑、分割、背景移除、多参考图编辑（最多 5 张）与智能调整尺寸；发布时在 **Arena 文生图与图像编辑双榜均列全球第 2**。可在 grok.com/imagine、iOS/Android 及 API（`grok-imagine-image-2.0`）使用。
- [Meta Muse Image](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) - 🆕 **2026-07-07**。Meta MSL 最先进的图像生成模型 —— Agent 式设计，在出图前执行网页搜索、代码执行与自我修正。已在 Instagram Stories（美国）与限定国家的 WhatsApp 上线（Facebook 即将上线）；也可在 Meta AI 应用与 meta.ai 使用。
- [Midjourney V8.1 / V8.2 Edit (alpha)](https://updates.midjourney.com/alpha-changelog-9-2-26/) - **2026年9月3日更新**。V8.2 Edit 已在 alpha 站点提供，支持指令编辑及最多四张参考图；主生成模型仍为 V8.1。
- [FLUX.2 Pro / Flex / Dev / Klein](https://bfl.ai/blog/flux-2) - 🆕 **2025-11-25**。Black Forest Labs 的下一代家族；SOTA 画质、多参考一致性（最多 10 张图），文本渲染显著提升；开源权重 32B Dev 变体。
- [Recraft V4 / V4.1](https://www.recraft.ai/blog/introducing-recraft-v4-design-taste-meets-image-generation) - 🆕 **2026-02-17**（V4.1 **2026-05-14**）。从零重构；提示准确度大幅改进；支持可编辑 SVG 矢量输出。V4.1 增强写实感、3D/渐变效果，并新增 Vector/Utility 变体。
- [Stable Diffusion 3.5](https://huggingface.co/stabilityai/stable-diffusion-3.5-large) - 采用 Stability AI Community License 的开放权重图像生成模型，适用时须遵循单独商业条款；并非 Apache-2.0。
- [Ideogram 4.0](https://ideogram.ai/models/4.0/) - 支持多语言排版与布局控制的图像生成、编辑模型；公开量化权重采用 [Ideogram 非商业模型协议](https://ideogram.ai/licensing/)，商用需另行许可。
- [P-Image-Ideogram](https://ideogram.ai/tools/p-image-ideogram/) - Pruna 与 Ideogram 合作的图像模型系列，提供不同画质、延迟与成本选项。
- [Ideogram 3.0](https://ideogram.ai/) - 文字渲染与设计向特别强。
- [ChatGPT Images 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/) - 🆕 **2026-04-21**。SOTA 图像生成：文字渲染、多语言支持、高级视觉推理与多轮迭代编辑全面增强。
- [gpt-image-2](https://developers.openai.com/api/docs/models/gpt-image-2) - 🆕 **2026-04-21**。OpenAI 最新图像生成/编辑 API 模型，支持灵活尺寸与高保真输入。**2026-08-20**：透明背景预览（`background=transparent`，仅 `png`/`webp`）覆盖 `gpt-image-2` 与 `gpt-image-2-2026-04-21`（Images API 与 Responses 图像工具）([changelog](https://developers.openai.com/api/docs/changelog.md))。
- [MAI-Image-2.6](https://microsoft.ai/news/mai-image-2-6-launches-at-no-2-on-arena-ahead-of-google-meta-and-xai/) - 🆕 **2026-08-10**（编辑榜 **08-18**）。微软自研图像模型 —— 发布时 Arena 文生图第 2，8 月 18 日图像编辑第 3。详见 Foundation → Microsoft (MAI)。
- [DALL·E 3](https://developers.openai.com/api/docs/deprecations) - 📦 历史文生图模型；`dall-e-3` API 已于 **2026年5月12日**退役，官方推荐迁移到 GPT Image 系列。
- [Gemini 3 Pro Image (Nano Banana Pro)](https://deepmind.google/models/gemini-image/pro/) - Gemini 内原生图像生成。
- [Nano Banana 2 (Gemini 3.1 Flash Image)](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/) - 🆕 **2026-02-26**。以 Flash 速度提供 Nano Banana Pro 级画质与世界知识；最多 5 个角色一致性，512px–4K 输出，支持图内文字渲染/翻译。
- [Kling Image 3.0 / 3.0 Omni](https://ir.kuaishou.com/news-releases/news-release-details/kling-ai-launches-30-model-ushering-era-where-everyone-can-be/) - 🇨🇳 🆕 **2026-02-05**。快手原生 2K/4K 图像生成，与 Video 3.0 一同随 Kling 3.0 套件发布。
- [Flux](https://github.com/black-forest-labs/flux) - 💤 **Stale**（2025-07 起无更新）。Black Forest Labs 开源模型。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fblack-forest-labs%2Fflux&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Seedream 5.0 Pro](https://seed.bytedance.com/en/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro) - **2026年7月8日**。字节跳动图像创作模型，面向布局、文字渲染与多模态设计；图像系列名为 Seedream，视频系列为 Seedance。
- [Qwen-Image-3.0](https://qwenlm.github.io/) - 🆕 🇨🇳 **2026-07-20**。阿里巴巴第三代图像生成模型，于世界人工智能大会上发布。真实感、文字渲染、多主主一致性均显著提升。可通过阿里云百炼与 Qwen Cloud 使用。
- [FLUX 3](https://bfl.ai/blog/flux-3) - 🆕 **2026-07-23（Early Access）**。Black Forest Labs 从纯图像家族转向统一的多模态基础模型 —— 在同一个架构里联合学习图像、视频和音频。可一次生成**长达 20 秒、自带同步音频**的视频（文生视频、图生视频、视频转视频、关键帧转视频、多语言对白、Agent 式多镜头串联）。BFL 自家早期评测中，FLUX 3 相对 Runway Gen-4.5 的胜率 77%、Luma Ray 3.2 为 93%、Kling v3 Pro 为 60%、Seedance 2.0 / Gemini Omni Flash 为 52% —— 厂商数据且官方明确标注为初步结果。其世界理解还延伸到面向机器人的**动作预测**。截至 2026 年 8 月中旬，FLUX 3 Image 的 early access 仍未开放。
- [Reve](https://reve.com/) - 🆕 「布局优先」的图像模型 —— 先规划出结构化、可编辑的版面再渲染像素，因此单个元素可以移动、缩放、改色并局部重渲染，而不必整张重来。原生 4K，支持草图 / 标注输入与直接对象编辑。

### 视频生成

- [Runway Aleph 2.0](https://docs.dev.runwayml.com/guides/models/) - Runway 视频编辑模型，ID 为 `aleph2`，支持视频/文本/图像输入及专业输出格式。
- [Meta Muse Video](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) - 🆕 **2026-07-07（预览）**。Meta Superintelligence Labs 的视频生成模型，与 Muse Image 同架构；Arena 文生视频榜第 3。随 Muse Image 发布一同预览，预计在 Meta 各应用中更广泛铺开。
- [Runway Agent](https://runwayml.com/news/introducing-runway-agent) - 🆕 **2026-05-13**。对话式 Agent，接过写好的脚本为你递交一段**多镜头完成品视频**：分镜脚本→生成→剪接→配音全流程贯通，并带时间线编辑器做最终调整。首个可用的「提示词到粗剪」产业级 Agent。
- [Veo 3.1](https://ai.google.dev/gemini-api/docs/veo) - 支持带音频视频生成、帧控制和延长；Gemini API 预览支持4/6/8秒片段，1080p/4K限8秒。
- [Runway Gen-4.5](https://runwayml.com/research/introducing-runway-gen-4.5) - 🆕 **2025-12**。Runway 旗舰视频模型，发布时位居 Artificial Analysis 文生视频榜第 1。平台还接入第三方模型，含 Kling 3.0 与 Sora 2 Pro（2026-02-20 加入）。
- [Kling VIDEO 3.0](https://app.klingai.com/) - 🇨🇳 🆕 **2026-02-04~07**。快手新一代；真人动作、嘴型同步、带音画同步的叙事化制作。
- [Sora 2 (via Runway)](https://runwayml.com/changelog) - OpenAI 的 Sora 应用于 2026-04-26 关停（API 保留至 2026-09-24），但 Sora 2 Pro 已自 **2026-02-20** 起集成进 Runway。
- [Seedance 2.5](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) - 🇨🇳 🆕 **2026-07-31（正式发布）**。字节下一代视频模型（6 月 23 日在火山引擎 2026 大会宣布）：原生一次生成 30 秒并支持多轮延展，灵活参考（单次最多 **30 张图 + 10 段视频 + 10 段音频**），长叙事中角色/商品一致性增强。在国内的即梦 AI 与豆包 Pro 陆续上线；API 经 BytePlus ModelArk 预发布 —— 暂无官方全球价目表。
- [Seedance 2.0](https://seed.bytedance.com/) - 🇨🇳 **2026-02**。字节多模态电影级视频生成，2K 分辨率（2026-06-23 升级支持 4K 输出），比 1.5 快约 30%。
- [MiniMax H3](https://huggingface.co/MiniMaxAI/MiniMax-H3) - 🆕 🇨🇳 **2026-07**。开源权重全模态视频+音频生成（2K / 15 秒，原生立体声）。现为 MiniMax 视频旗舰 —— 详见 Foundation → MiniMax。
- [MiniMax-H3-Fun-Controlnet-Union](https://huggingface.co/alibaba-pai/MiniMax-H3-Fun-Controlnet-Union) - 🆕 🇨🇳 **2026-08-24**。阿里 PAI 为 H3 发布的统一 ControlNet：单权重覆盖 Canny / Depth / HED / MLSD / Pose，并支持视频补全（`minimax-h3-community-license-agreement`）。
- [Hailuo 2.3](https://www.minimax.io/news/minimax-hailuo-23) - 🇨🇳 **2025-10-28**。前代 MiniMax 视频模型：SOTA 物理效果、角色微表情、强风格化（动漫/水墨/游戏 CG）；Hailuo 2.3 Fast 变体按 Hailuo 02 价格提供。旗舰已由 MiniMax H3 接替。
- [Pika 2.5](https://pika.art/) - 创意短视频，场景与特效控制。
- [LTX Studio](https://ltx.studio/) - AI 电影化视频创作平台。
- [HappyHorse 1.1](https://technode.com/2026/06/23/alibaba-unveils-happyhorse-1-1-video-generation-model-launches-global-ai-filmmaking-competition/) - 🇨🇳 🆕 **2026-06-23**。阿里视频模型（2026-04-10 以 "HappyHorse-1.0" 之名揭晓，此前匿名登顶多个基准，后升至全球第 2）。1.1 升级运动动态、主体一致性、提示遵循与音频生成。可通过 HappyHorse 官网、阿里云百炼与 Qwen Cloud 使用。
- [Sora 2 API (deprecated)](https://developers.openai.com/api/docs/deprecations) - 📦 已弃用 API，计划于 **2026年9月24日**关闭；保留用于迁移跟踪，不建议新项目接入。
- [Gemini Omni Flash 1.1](https://ai.google.dev/gemini-api/docs/omni) - Google 当前推荐的视频生成选项，`gemini-omni-1.1-flash` 支持多轮编辑；上传视频的编辑与延长存在地区限制。
- [Wan 3.0](https://www.alibabacloud.com/en/blog/wan-3-0-next-gen-video-generation-model-public-beta-launched) - 🆕 🇨🇳 **2026-08-06（公开测试）**。阿里通义实验室下一代视频生成模型——单次生成最长 30 秒视频。独特支持 PDF / Word / PPT 等文档以及网页作为输入，同时支持文本、图像、音频。提示智能推荐视频时长。可通过阿里云模型平台 / Qwen Cloud 体验；API 和开源权重尚未确认。
- [LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) - 🆕 **2026 年 8 月 12 日**。Lightricks 开源权重视频音频世界模型，支持原生多镜头生成（单次过题就能保持角色、场景、声音和风格一致性）、扩散质量渲染、全新视频解码器（更锐利的人\u脸和纹理，更少作影）、定制 Gemma 4 12B 文本编码器及提示增强器。支持文本转视频、图像转视频、视频转视频、音频转视频等多种模式。可本地自托管，无按次计费。
- [Decart Lucy 2.5](https://decart.ai/) - 🆕 **2026 年 7 月**。支撑 Decart「Live AI」路线的实时视频 / 世界转换模型 —— 可持续生成无限时长视频并带物理感知特效，官方称效率比常驻算力方案高约 100 倍。面向直播、交互式世界模型以及机器人 / 自动驾驶仿真。

### 音频与音乐

- [MAI-Transcribe-2](https://microsoft.ai/news/mai-transcribe-2-is-the-fastest-most-accurate-and-cheapest-speech-recognition-model-in-the-world/) - 🆕 **2026年9月3日**。微软语音转文本模型，支持说话人标签、词级时间戳及可配置的逐字/清理转写。
- [Muse Voice Transcribe](https://research.meta.ai/blog/introducing-muse-voice-transcribe) - 🆕 **2026年9月1日**。Meta 实时音频感知模型，提供流式语音识别、说话人区分与语音终点检测。
- [Lyria 3.5](https://ai.google.dev/gemini-api/docs/models/lyria-3.5) - Google 当前完整歌曲生成模型，官方 ID 为 `lyria-3.5`；交互式音乐另由 Lyria RealTime 提供。
- [Qwen3-TTS](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice) - Apache-2.0 多语言 TTS 系列，提供独立的 Base、CustomVoice、VoiceDesign 检查点及流式生成。
- [Qwen3-ASR](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) - Apache-2.0 语音识别系列，提供0.6B/1.7B变体、流式与离线推理，覆盖30种语言及22种中文方言。
- [ElevenLabs Eleven v3 + ElevenAgents](https://elevenlabs.io/agents) - 🆕 2026 年定位为 "互联网的音频层"——支持 70+ 语言、带情绪 Audio Tag 的 TTS，加上首个通过 AIUC-1 认证的 ElevenAgents 语音 Agent 平台，含多模态消息、会话主题发现、工具调用前的语音控制。**2026 年 7 月更新**：Music Finetunes API（可编程管理自定义模型）、每个 Agent 独立的情绪分析、Agent 嵌套转移、RAG 知识库查询、自动翻译转录、更快的生成速度与长音频的音色一致性。
- [ElevenLabs](https://elevenlabs.io/) - AI 语音合成 + 克隆 + 对话 AI 头部。**2026 年 7 月更新**：Music Finetunes API、每 Agent 情绪分析、Agent 嵌套转移、RAG 查询、自动翻译转录、更快生成。
- [Cartesia Sonic 3 / 3.5](https://cartesia.ai/blog/introducing-line-for-voice-agents) - **2026**。基于状态空间模型的 TTS，首音延迟约 40-90ms（Sonic 3.5 于 2026 年 5 月 GA）；驱动 **Line** 语音 Agent 平台（自 2026 年 5 月起 Line Agent 默认运行在 Sonic 3.5 TTS + Ink-2 STT 上）。
- [Deepgram Nova-3 + Aura-2 + Flux Multilingual](https://deepgram.com/learn/best-voice-ai-agents-2026-buyers-guide) - **2026 年 4 月**。45+ 语言的 STT，TTS 延迟低于 200ms，会话式 STT 支持通话中 10 种语言的实时切换。
- [MiniMax Music 3.0](https://huggingface.co/MiniMaxAI/MiniMax-Music3) - 🆕 🇨🇳 **2026-08-13**。开源权重完整歌曲生成（最长 5 分钟，32 kHz 立体声）。现为 MiniMax 音乐旗舰 —— 详见 Foundation → MiniMax。
- [MiniMax Music 2.6](https://aimlapi.com/blog/the-ultimate-guide-to-minimax-models-2026-m2-7-music-2-6-hailuo-video-advanced-tts) - 🇨🇳 **2026 年 4 月 10 日**（全球 beta）。翻唱向前代；已由 Music 3.0 接替。
- [Voxtral TTS](https://docs.mistral.ai/models/voxtral-tts-26-03) - Mistral 多语言语音生成模型；开放权重为 CC-BY-NC-4.0，与 Apache-2.0 的 Voxtral 转写权重须区分。
- [Suno v5.5 + Studio 2.0](https://suno.com/blog/v5-5) - 🆕 **2026 年 3 月 26 日**（Studio 2.0 为 **2026 年 8 月 13 日**）。高保真人声的 AI 音乐生成；v5.5 新增 Voices（用你本人经验证的声音演唱）、基于上传内容训练的 Custom Models 以及 My Taste 个性化。**Studio 2.0**（8 月 13 日）是彻底重构的浏览器端 DAW，支持 MIDI、音频特效与内置合成器；Voices 于 8 月 7 日扩展到 iOS/Android 免费套餐。V6 有传闻但未官宣。
- [Udio](https://www.udio.com/) - 商用级音乐生成。
- [OpenAI Audio Models](https://openai.com/) - GPT-4o 与 GPT-Realtime-2（**2026-05-07**，随 GPT-Realtime-Translate、GPT-Realtime-Whisper 一同发布）内的原生音频理解 + 生成；gpt-realtime-2.1 与 2.1-mini 于 **2026-07-06** 发布，字母数字识别、噪声处理与打断行为均改进。
- [Stable Audio 3.0](https://stability.ai/stable-audio) - 音频生成系列，包含 Large、Medium、Small、Small SFX；Medium 与 Small 提供开放权重，部署权利以对应 Stability 许可证为准。
- [Bark](https://github.com/suno-ai/bark) - 💤 **Stale**（2024-08 起无更新）。开源文本到音频。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsuno-ai%2Fbark&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hume TADA](https://github.com/HumeAI/tada) - 采用文本/声学 1:1 对齐的语音语言模型，提供 TADA-1B 与多语言 TADA-3B-ML；代码为 MIT，权重采用 Llama 3.2 社区许可证。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHumeAI%2Ftada&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

## 🔗 Agent 协议与标准

*让 Agent 跨工具、跨框架互联互通的开放标准。*

### Model Context Protocol (MCP)

- [FastMCP](https://github.com/PrefectHQ/fastmcp) - 用于 MCP 服务、客户端和交互式应用的 Python 框架；Apache-2.0; [v4.0.3](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.0.3) (2026-09-05). ![GitHub stars](https://img.shields.io/github/stars/PrefectHQ/fastmcp?style=flat-square)
- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28) - 🆕 **2026-07-28（正式版）**。自发布以来最大的 MCP 协议变更：**无状态架构**（去掉 `initialize`/`initialized` 握手和 `Mcp-Session-Id`；每个请求都是自包含的 HTTP POST），支持 serverless/边缘部署与水平扩展。正式扩展模型；按请求的 token 评估；旧版本 12 个月弃用窗口。
- [MCP Specification](https://modelcontextprotocol.io/) - "AI 的 USB-C" —— Anthropic 主推、用于让 LLM 接入工具与数据源的开放协议。2025-12 捐赠给 Linux Foundation 旗下 Agentic AI Foundation。
- [MCP 2026-07-28](https://blog.modelcontextprotocol.io/posts/2026-07-28/) - 🆕 **已按期于 2026-07-28 正式发布** —— 自发布以来最大的一次修订。**无状态协议核心**：去掉了 `initialize` 握手与协议层会话，每个请求自包含描述，任何请求都能落到普通轮询负载均衡器后的任意实例。**多往返请求（MRTR）**取代为 sampling / elicitation 长期持开的双向流。方法名和工具名改走 `Mcp-Method` / `Mcp-Name` HTTP 头，网关可仅凭请求头完成路由与鉴权。List 响应带缓存提示 + 确定性排序（重连后上游 prompt 缓存保持稳定）。**扩展框架**正式定型，Tasks 与 MCP Apps、企业托管授权（EMA）并列为扩展。**授权强化**：RFC 9207 issuer 校验，并从动态客户端注册（DCR）转向客户端元数据文档（CIMD）。另含正式的最短 12 个月弃用窗口。Tier-1 的 TypeScript / Python / Go / C# SDK 当天同步。规模参考：Tier-1 SDK 现在每月下载接近 5 亿次，TS 和 Python 各自累计突破 10 亿。[SDK beta 于 2026-06-29 发布](https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/)；[RC 于 2026-05-21 公布](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)。
- [新版 MCP 路线图](https://blog.modelcontextprotocol.io/posts/mcp-roadmap/) - 🆕 **2026-08-22**。核心维护者（David Soria Parra、Den Delimarsky）发布 `2026-07-28` 之后的路线图：Agent 消息原语、HTTP 原生传输统一、Agent 身份 / 企业安全、原语改进、SDK 开发体验。回顾 3 月优先级现已落地（无状态核心、`server/discover`、可缓存 list、Tasks 扩展、MRTR、CIMD 授权）。
- [MCP Reference Servers](https://github.com/modelcontextprotocol/servers) - 用于演示 MCP 功能的教学参考实现；可通过 [MCP Registry](https://registry.modelcontextprotocol.io/) 查找集成，生产使用前需单独评估服务。
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - 官方 TypeScript SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Ftypescript-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - 官方 Python SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Fpython-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [mcp.so](https://mcp.so/) - 社区 MCP 服务目录。
- [Agents Launchpad](https://launchpad.smartbizcalc.com) - 🆕 AI Agent、MCP 与独立开发者产品的社区发布平台 —— 提交发布、登上周榜单，让对的用户找到你。⚠️ **未验证**（早期项目）。
- [CorpusIQ](https://www.corpusiq.io/) - ⚠️ **采用情况未经独立验证**：面向 AI 助手的托管业务数据连接器，官网提供 MCP 集成说明。
- [Agentage Memory](https://agentage.io/blog/mcp-endpoint-is-live) - ⚠️ **采用情况未经独立验证**：支持浏览器登录、供 MCP 客户端访问的共享记忆服务；链接指向可阅读的连接说明。
- [mcp-gateway](https://github.com/Zijian-Ni/mcp-gateway) - ⚠️ **未经验证**（早期项目）。MCP 网关，统一路由 / 认证 / 限流。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fmcp-gateway&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Agent-to-Agent Protocol (A2A)

- [A2A Protocol](https://github.com/a2aproject/A2A) - 开放的智能体间通信协议；[v1.0.0](https://github.com/a2aproject/A2A/releases/tag/v1.0.0) 于 2026-03-12 发布，v1.0.1 于 2026-05-28 发布；Apache-2.0; [v1.0.1](https://github.com/a2aproject/A2A/releases/tag/v1.0.1) (2026-05-28).
- [A2A Course (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/a2a-the-agent2agent-protocol/) - 免费课程：用 A2A 构建多 Agent 系统。

### 其他标准

- [Agentic AI Foundation](https://aaif.io/) - 🆕 Linux Foundation 旗下的开放 Agent 标准治理机构 —— 托管 MCP、goose、AGENTS.md 与 agentgateway。创始白金成员：AWS、Anthropic、Block、Bloomberg、Cloudflare、Google、Microsoft、OpenAI。
- [AGENTS.md](https://agents.md/) - 🆕 开放的 Markdown 约定 —— "给 Agent 看的 README"——为 AI 编程 Agent 提供项目上下文与指令的固定位置。已被 6 万+ 开源项目采用；由 Agentic AI Foundation（Linux Foundation）管理。
- [Coinbase Base MCP](https://fortune.com/2026/05/26/coinbase-pushes-further-into-ai-payments-with-new-mcp-for-base-network/) - **2026 年 5 月 26 日**。Coinbase 为 Base 公链发布 MCP 服务器，让 Claude / Cursor / ChatGPT Agent 直接执行加密资产交易与借贷。首个交易所级、面向链上自动化的 MCP 端点。
- [Cloudflare WebMCP](https://blog.cloudflare.com/agents-week-review-august-2026/) - 🆕 **2026 年 8 月 6 日（Cloudflare Agents Week，8 月 3–7 日）**。一行代码让任意网站可被 AI Agent 发现和使用，发布者保留访问控制权， Agent 获得结构化内容访问。是 Cloudflare 开放代理互联网（可读、可发现、可调用、可支付）愿景的一部分。
- [Robinhood Agentic Trading MCP](https://robinhood.com/us/en/newsroom/robinhood-is-now-open-to-agents/) - **2026 年 5 月 27 日**（beta）。首家通过 MCP 把股票交易开放给 AI Agent 的美国券商：Agent（Claude / Codex / Cursor）对账户只读，仅可在专门隔离的 Agentic 账户内交易；每笔交易推送，一键断开。
- [The Declaration of Intelligence](https://thedeclaration.ai) - ⚠️ 面向 AI Agent 与人类的原则宣言草案（v0.2），通过 GitHub Pull Request 公开签署。早期阶段 —— 最近核查时仅有少量签名方。
- [Kuberna Labs](https://github.com/kawacukennedy/kuberna-labs) - ⚠️ **未验证。** 面向 AI Agent 的跨链意图执行协议，声称支持 ERC-8004 链上身份、zkTLS/TEE 证明与类型化意图模式，可在 NEAR、Base、Mantle 上自主执行交易并附可验证执行证明。新仓库，独立采用情况未经验证——仅供参考，使用前请自行评估。

---

## 🏗️ Agent 框架

*用来构建自主 AI Agent 的框架与库。*

- [Deep Agents](https://github.com/langchain-ai/deepagents) - 基于 LangGraph 的 MIT 许可智能体运行框架，包含子智能体、文件系统工具、上下文管理、持久记忆和技能。 ![GitHub stars](https://img.shields.io/github/stars/langchain-ai/deepagents?style=flat-square)
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) - NousResearch 的智能体运行框架，提供工具、持久记忆、技能和消息渠道集成; [v2026.9.7](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.9.7) (2026-09-07).
- [Superpowers](https://github.com/obra/superpowers) - 用于规划、测试驱动开发、调试和代码审查的可复用编程智能体技能; [v6.3.0](https://github.com/obra/superpowers/releases/tag/v6.3.0) (2026-08-12).
- [Pi Agent](https://github.com/earendil-works/pi) - 可扩展的终端编程智能体工具包，集成多种模型提供商; [v0.85.1](https://github.com/earendil-works/pi/releases/tag/v0.85.1) (2026-09-05).
- [Ponytail](https://github.com/DietrichGebert/ponytail) - 🆕 **2026 年 6 月**。让 AI Agent 像最懒的高级工程师一样思考的 Agent 框架：最少的代码，最大的正确性。支持 20+ Agent。MIT 许可证；**103,000+ stars**。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FDietrichGebert%2Fponytail&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [NVIDIA NOOA (labs-OO-Agents)](https://github.com/NVIDIA-NeMo/labs-OO-Agents) - 🆕 ⚡ **2026-08（alpha）**。NVIDIA 面向对象的 Agent 框架：把 prompt 模板、工具模式、回调代码和工作流图全部统一到一个 Python 类。有实现体的方法保持为确定性代码，无实现体的方法将在运行时由 LLM 循环完成。在 SWE-bench Verified 和 CyberGym L1 上得分高，耗用 token 为同类框架的一半左右。许可证：APACHE 2.0（NOASSERTION）；建议在沙箱环境运行。**1,627 stars**。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNVIDIA-NeMo%2Flabs-OO-Agents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [NVIDIA Molt](https://github.com/NVIDIA-NeMo/labs-molt) - 🆕 **2026-07（v0.1.0）**。NVIDIA NeMo Labs 出品的 PyTorch 原生 Agentic 强化学习框架 —— 精简的约 9,000 行核心代码，以 **Agent 为核心程序**。单一异步循环，Ray 分布式执行，vLLM 用于 rollout，NeMo AutoModel + FSDP2 作策略 actor。支持 100B+ MoE 模型。RL 估算器：REINFORCE、RLOO、GRPO、DR-GRPO、GAE (PPO)、在线蒸馏。随附 Slurm 脚本 + 预构建容器。Apache-2.0。**910 stars**。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNVIDIA-NeMo%2Flabs-molt&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vercel Eve](https://github.com/vercel/eve) - **2026-06-17（Vercel Ship 2026）**。Vercel 开源的「文件系统优先」TypeScript Agent 框架——一个 Agent 就是一个文件目录（指令、工具、技能），由 Vercel 编译为内置沙箱执行、审批、评测与 OpenTelemetry 的持久化服务。兼容任意模型、任意 MCP 服务器以及 Slack / Discord / GitHub 等渠道，被称为「Agent 界的 Next.js」。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvercel%2Feve&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Databricks Omnigent](https://github.com/omnigent-ai/omnigent) - **2026-06**。Databricks 开源的元 Harness：位于你已有的编码 Agent（Claude Code、Codex、Pi、自定义）之上，把它们整合为同一系统中可互操作的部件——统一编排、共享安全策略、实时协作。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fomnigent-ai%2Fomnigent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Nokia NSP Agentic AI](https://www.globenewswire.com/news-release/2026/06/11/3310210/0/en/nokia-introduces-agentic-ai-framework-in-network-services-platform-to-enable-trust-based-ai-operations-for-ip-networks.html) - **2026-06**。面向电信 Network Services Platform (NSP) 的企业级 Agent 框架，部署 Agent 在复杂 IP 网络上推理并执行路由 / 维护操作。
- [Alteryx Agent Studio](https://www.alteryx.com/blog/new-capabilities-in-alteryx-one-built-for-how-analysts-work) - 🆕 **2026-05**。把可信的 Alteryx 数据集与工作流打包为对话式 Agent；通过新的 Alteryx One MCP Server 创建并管理 MCP 端点（可在 Claude、ChatGPT、Gemini 中作答）。
- [Koog](https://github.com/JetBrains/koog) - Kotlin/Java 智能体框架；1.2.0 新增 Agent Skills 发现与 Amazon Bedrock AgentCore Runtime 集成; [1.2.0](https://github.com/JetBrains/koog/releases/tag/1.2.0) (2026-08-28). ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FJetBrains%2Fkoog&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangChain](https://github.com/langchain-ai/langchain) - 上下文感知推理应用的基础框架。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangGraph](https://github.com/langchain-ai/langgraph) - 把 Agent 建模为有状态、多 actor 协作的图。**最新稳定版 1.2.11（2026年8月11日）**，修复了追踪与 checkpoint 稳定性问题。0.3.x 系列（2025）把预制 Agent 拆出 `langgraph-prebuilt`（Supervisor / Swarm / LangMem / Trustcall）。**v1.2（2026-05）** 新增节点级超时 / 错误恢复 / 优雅关停、降低长线程 checkpoint 开销的 `DeltaChannel`，以及以 content block 为中心的流式 API v3。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flanggraph&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [CrewAI](https://github.com/crewAIInc/crewAI) - 支持协作智能体团队和事件驱动 Flows 的 Python 框架；1.15.20 修复旧版平台工具别名发现; [1.15.20](https://github.com/crewAIInc/crewAI/releases/tag/1.15.20) (2026-09-04).
- [goose](https://github.com/aaif-goose/goose) - 源自 Block、现由 AAIF 托管的可扩展桌面与 CLI 智能体；Apache-2.0; [v1.49.0](https://github.com/aaif-goose/goose/releases/tag/v1.49.0) (2026-09-03).
- [AG2](https://github.com/ag2ai/ag2) - 社区维护的对话式多智能体框架；1.0.4 更新模型 SDK 支持和 ACP 会话恢复; [v1.0.4](https://github.com/ag2ai/ag2/releases/tag/v1.0.4) (2026-09-07).
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/) - MIT 许可的 Python/.NET 智能体与工作流框架；Python [1.17.0](https://github.com/microsoft/agent-framework/releases/tag/python-1.17.0)（2026-09-03），.NET [1.20.0](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.20.0)（2026-08-31）。
- [Microsoft Agent 365](https://techcommunity.microsoft.com/blog/agent-365-blog/what%E2%80%99s-new-in-agent-365-may-2026/4516340) - **2026 年 5 月 GA**。面向 AI Agent 的企业级可观测、治理与安全平台；2026 年 5 月更新加入面向 Agent 的 SASE、威胁检测/阻断与 Agent 威胁狩猎工作流。KPMG 宣布覆盖 276,000 名专业人员的全球部署（2026-06-09）。
- [Microsoft Scout](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) - **2026-06-02（Build 2026）**。微软面向 Microsoft 365 的常驻个人工作 Agent，构建在开源 OpenClaw 运行时之上。
- [AutoGen](https://github.com/microsoft/autogen) - 💤 **维护模式**（最后版本 2025-09；由 Microsoft Agent Framework 接替，后续交由社区管理）。微软多 Agent 对话框架。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fautogen&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Google Agent Development Kit (ADK)](https://github.com/google/adk-python) - 用于智能体、工具和工作流的 Python 框架；2.x 功能版本线与持续维护的 1.x 版本线并行; [v2.8.0](https://github.com/google/adk-python/releases/tag/v2.8.0) (2026-08-26).
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - 提供交接、护栏、追踪、MCP 和沙箱集成的 Python 智能体 SDK；0.22.1 新增 MCP 服务级工具护栏; [v0.22.1](https://github.com/openai/openai-agents-python/releases/tag/v0.22.1) (2026-09-08).
- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) - 🇨🇳 给 LLM 分配 SOP 软件团队角色（PM / 架构师 / 工程师）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FFoundationAgents%2FMetaGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Pydantic AI](https://github.com/pydantic/pydantic-ai) - 提供结构化输出校验和模型集成的类型化 Python 智能体框架；2.41.0 新增直接图像生成 API; [v2.41.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.41.0) (2026-09-08). ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fpydantic%2Fpydantic-ai&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Mastra](https://github.com/mastra-ai/mastra) - 包含工作流、记忆和可观测性的 TypeScript 智能体框架；核心采用 Apache-2.0，企业目录另有许可; [@mastra/core@1.64.0](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.64.0) (2026-09-04).
- [Agon](https://github.com/AutoResearch-Factory/Agon) - 🆕 ⚠️ **未验证**（35 stars，MIT）。作为 **Claude Code 插件**构建的自主全科研编排器 —— 科学家/编码者/审计员多 Agent 循环，将单一课题一路推进到可运行的实验，无需人工编写实验代码。10+ 学科方向，230.6 KiB 提示语分布在 18 个角色中；有 30 天全自主运行记录。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAutoResearch-Factory%2FAgon&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hypha](https://github.com/CodeSoul-co/Hypha) - 🆕 ⚠️ **未验证**（v1.0.1，2026-08-14；Apache-2.0）。CodeSoul 出品的 TypeScript Agent 框架，将 **Agent Core**（ReAct、规划、工具选择、记忆）与 **Production Harness**（FSM 执行、策略/审批、检查点、恢复、回放、审计）分离；产品行为以版本化 **DomainPack** 声明，并明确规定缓存不得授权副作用或推进 FSM。npm 上有 15 个 `@codesoul-co/hypha-*` 包。⚠️ 采用度尚处早期：截至 2026-08-22，`@codesoul-co/hypha-core` npm 月下载约 32 次；厂商公布的 τ³ 成绩（385 任务单次试验 0.636 vs 直调模型基线 0.626）处于统计噪声范围内。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FCodeSoul-co%2FHypha&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Ontheia](https://github.com/Ontheia/ontheia) - ⚠️ **未经验证**（早期项目，独立采用情况待验证）。AGPL-3.0 自托管 Agent 平台，支持多模型供应商、MCP、可视化工作流、记忆和角色访问控制；自托管与权限设计本身不能证明具体部署符合 GDPR。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOntheia%2Fontheia&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentGPT](https://github.com/reworkd/AgentGPT) - 📦 **Archived**（2026-01）。浏览器中部署 Agent。第一波代表项目，仅作历史参考。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Freworkd%2FAgentGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [BabyAGI](https://github.com/yoheinakajima/babyagi) - 实验性的自构建自主 Agent 框架；2023 年原版任务管理型 BabyAGI 现存于 [babyagi_archive](https://github.com/yoheinakajima/babyagi_archive)。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fyoheinakajima%2Fbabyagi&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) - 💤 **Stale**（2025-01 起无更新）。开源自主 Agent 框架。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTransformerOptimus%2FSuperAGI&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) - 把 LLM 嵌入应用。C# / Python / Java。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fsemantic-kernel&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agno](https://github.com/agno-agi/agno) - 支持智能体、团队、工作流和知识库的 Python 框架；Apache-2.0；升级前应阅读 v3 迁移指南; [v3.0.7](https://github.com/agno-agi/agno/releases/tag/v3.0.7) (2026-09-08).
- [DSPy](https://github.com/stanfordnlp/dspy) - "编程而不是写 prompt" 的语言模型框架。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstanfordnlp%2Fdspy&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenClaw](https://github.com/openclaw/openclaw) - 支持消息渠道、技能、记忆和定时任务的个人智能体运行时；2026.9.3 改进分阶段更新与性能; [v2026.9.3](https://github.com/openclaw/openclaw/releases/tag/v2026.9.3) (2026-09-08).
- [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) - 🧪 基于 Cordis 和插件架构的 DeepSeek 智能体运行框架；[dsh-v0.1.3-alpha.2](https://github.com/deepseek-ai/deepseek-harness/releases/tag/dsh-v0.1.3-alpha.2)（2026-09-07）仍为开发者预览，预计存在不兼容变更。
- [Dify](https://github.com/langgenius/dify) - 🇨🇳 开源 LLM 应用开发平台 + 可视化 Agent 构建。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flanggenius%2Fdify&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Haystack Agents](https://github.com/deepset-ai/haystack) - 端到端 LLM 框架，Agent 流水线。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeepset-ai%2Fhaystack&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vellum AI](https://www.vellum.ai/) - 闭源 SaaS 生产级 Agent 框架：Prompt 构建 / 评测 / 版本 / 可观测性一体。
- [FastAgency](https://github.com/ag2ai/fastagency) - 💤 把 AG2（AutoGen）多 Agent 工作流通过 console、Mesop Web UI、REST/FastAPI 与 NATS 适配器部署到生产；最后版本 2025-12。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fag2ai%2Ffastagency&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Rasa](https://github.com/RasaHQ/rasa) - 💤 **维护模式**（最后版本 2025-01；后继为 Rasa CALM）。强意图识别 + 对话管理的开源对话 AI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FRasaHQ%2Frasa&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Lindy](https://www.lindy.ai/) - 商务用户向无代码 Agent，可视化工作流。
- [Octomind](https://github.com/muvon/octomind) - Rust 开源 AI Agent 运行时。多模型（13+），社区贡献的领域 Agent（开发 / 医疗 / 法律 / DevOps），支持 MCP 运行时自扩展。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmuvon%2Foctomind&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsoft AI Agent Governance Toolkit](https://www.helpnetsecurity.com/2026/04/03/microsoft-ai-agent-governance-toolkit/) - **2026-04-03**。开源治理工具包，把运行时安全策略以策略即代码方式应用到 LangChain / AutoGen 等框架。
- [Bernstein](https://github.com/sipyourdrink-ltd/bernstein) - Python 编排器，统一管理 40+ 个 CLI 编程 Agent（Claude Code、Codex、Gemini CLI、Cursor、Aider 等）。一次 LLM 计划调用后，调度、git worktree 隔离、质量闸门、HMAC 链式审计都是确定性的。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsipyourdrink-ltd%2Fbernstein&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Genkit Middleware](https://developers.googleblog.com/announcing-genkit-middleware-intercept-extend-and-harden-your-agentic-apps/) - **2026-05-14**。Google 为开源 Genkit 框架增加中间件体系 —— 在 generate / model / tool 三层给出可组合 hooks：重试、模型降级、工具人工审批、SKILL.md 技能注入、限定范围的文件访问。先支持 TS / Go / Dart，Python 跟进中。
- [Coze Studio](https://github.com/coze-dev/coze-studio) - 🇨🇳 字节跳动开源的 AI Agent 开发平台——一体化可视化工具，简化 Agent 的创建、调试、部署。Apache-2.0，20K+ stars；Coze.com 的开源对照版。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LlamaIndex ↔ Google Agents API 集成](https://www.kucoin.com/news/flash/google-launches-agents-api-llama-index-integrates-llamaparse-for-unstructured-document-processing) - **2026-05-20**。LlamaIndex 为 Google 刚发布的 Agents API 交付模板，在沙箱化 Linux 环境里暴露 **LlamaParse** / **LiteParse** 处理非结构化文档。
- [NarraNexus](https://github.com/NetMindAI-Open/NarraNexus) - NetMind.AI 出品的开箱即用 AI Agent 团队工作区——具备记忆的 Agent 从第一天起就能记住上下文、协作并使用工具。多 Agent（PM/开发/部署/研究）、持久上下文、MCP 式集成、可组合模块。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNetMindAI-Open%2FNarraNexus&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Strands Agents (AWS)](https://github.com/strands-agents/harness-sdk) - 🆕 **2026 年4–6月**。AWS 开源模型驱动 Agent SDK（Python + TypeScript 1.0 GA 2026-04-30）。支持 Bedrock / Anthropic / OpenAI / Ollama，多种多智能体编排模式（图/群/工作流），内置可观测性 hooks，A2A 协议支持；TypeScript SDK 现由 [harness-sdk monorepo](https://github.com/strands-agents/harness-sdk) 维护。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstrands-agents%2Fharness-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [CrewAI](https://github.com/crewAIInc/crewAI) - 支持协作智能体团队和事件驱动 Flows 的 Python 框架；1.15.20 修复旧版平台工具别名发现; [1.15.20](https://github.com/crewAIInc/crewAI/releases/tag/1.15.20) (2026-09-04).
- [Oracle AI Agent Studio (Fusion)](https://www.oracle.com/news/announcement/oracle-introduces-ai-native-builder-experience-2026-07-14/) - 🆕 **2026-07-14**。Oracle Fusion Cloud 应用内置的 AI 原生构建器，打造“Fusion Agentic Applications”——在 Fusion 业务对象、工作流和安全上下文中脚本与执行的多 Agent 团队。无代码/低代码/专业代码全支持；Fusion 客户免费使用。


- [Microsoft Agent Framework releases](https://github.com/microsoft/agent-framework/releases) - 官方发布说明；稳定版于 2026-09-08 核验; [python-1.17.0](https://github.com/microsoft/agent-framework/releases/tag/python-1.17.0) (2026-09-03).
- [OpenAI Agents SDK releases](https://github.com/openai/openai-agents-python/releases) - 官方发布说明；稳定版于 2026-09-08 核验; [v0.22.1](https://github.com/openai/openai-agents-python/releases/tag/v0.22.1) (2026-09-08).
- [CrewAI releases](https://github.com/crewAIInc/crewAI/releases) - 官方发布说明；稳定版于 2026-09-08 核验; [1.15.20](https://github.com/crewAIInc/crewAI/releases/tag/1.15.20) (2026-09-04).
- [Google ADK releases](https://github.com/google/adk-python/releases) - 官方发布说明；稳定版于 2026-09-08 核验; [v2.8.0](https://github.com/google/adk-python/releases/tag/v2.8.0) (2026-08-26).
- [ServiceNow AI Agents](https://www.servicenow.com/products/ai-agents.html) - 与 ServiceNow 工作流集成的智能体；AI Agent Studio 用于构建，Agent Fabric 用于连接，AI Control Tower 用于治理部署。
- [Embabel Agent](https://github.com/embabel/embabel-agent) - 🆕 **最新标记版本：v1.5.1（2026-08-24）**，此前 v1.5.0（8 月 11 日）。面向生产的 **JVM** 生态 AI Agent 框架 —— 由 Spring Framework 创始人 Rod Johnson 主导。通过有类型的领域对象定义 Agent 行为；Spring AI 2 / Jackson 3；基于图的多 Agent 编排；原生 MCP 客户端；1.5.x 增加 embedding 驱动 skills 与按角色的 LLM SPI。**Apache-2.0**。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fembabel%2Fembabel-agent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
---

## 🛠️ Agent IDE 与可视化构建器

*用来设计、调试、上线 Agent 工作流的可视化（或低代码）环境。*

- [LangGraph Studio](https://docs.langchain.com/langsmith/studio) - LangGraph 的可视化调试器（现为 LangSmith 的一部分）：步进状态、回放回合、中途改写消息。
- [Dify](https://github.com/langgenius/dify) - 🇨🇳 拖拽式 Agent 工作流构建。生产级使用最广。⚡ **v1.17.0（2026-08-25）** 增加 E2B 云沙箱、Home 快照、工作区 Skill 管理与上下文感知历史压缩。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flanggenius%2Fdify&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agenta](https://github.com/agenta-ai/agenta) - 一体化 LLMOps：prompt playground + 管理 + 评测 + 可观测性。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagenta-ai%2Fagenta&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vellum AI](https://www.vellum.ai/) - 闭源 SaaS。
- [Coze Loop](https://github.com/coze-dev/coze-loop) - 🇨🇳 🆕 字节 Coze 团队开源的 Agent 优化平台：全生命周期开发、调试、评测与监控。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-loop&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Restack](https://www.restack.io/) - 持久化 Agent 运行时 + 可视化编辑（Temporal 风格 replay）。开源示例：[restackio/examples-python](https://github.com/restackio/examples-python)。
- [Bisheng](https://github.com/dataelement/bisheng) - 🇨🇳 企业级开源 LLM DevOps：工作流 / RAG / Agent / 微调 / 数据集 / 评测 / 可观测性。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdataelement%2Fbisheng&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [n8n](https://github.com/n8n-io/n8n) - 通用工作流自动化，2026 年常被当作 Agent 画布用。400+ 集成 + 原生 AI 节点。Fair-code。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fn8n-io%2Fn8n&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Mastra](https://github.com/mastra-ai/mastra) - 包含工作流、记忆和可观测性的 TypeScript 智能体框架；核心采用 Apache-2.0，企业目录另有许可; [@mastra/core@1.64.0](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.64.0) (2026-09-04). ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmastra-ai%2Fmastra&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [VoltAgent](https://github.com/VoltAgent/voltagent) - 端到端 TypeScript AI Agent 工程平台，覆盖记忆、RAG、guardrail、MCP、语音与工作流。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FVoltAgent%2Fvoltagent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Coze Studio](https://github.com/coze-dev/coze-studio) - 🇨🇳 字节 Coze 团队的开源 Agent IDE / 可视化构建器。拖拽式工作流、插件市场、调试面板、多 LLM 供应商支持。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🧠 Agent 记忆

*让 Agent 拥有持久记忆与上下文管理的系统。*

- [Mem0 SDK releases](https://mem0.ai) - 官方 [Python v2.0.20](https://github.com/mem0ai/mem0/releases/tag/v2.0.20) 与 [TypeScript v3.1.8](https://github.com/mem0ai/mem0/releases/tag/ts-v3.1.8)（2026-09-02）。
- [Letta (MemGPT)](https://github.com/letta-ai/letta) - 长期记忆 + 自定义工具的 LLM 服务。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fletta-ai%2Fletta&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MemoryLake](https://memorylake.ai) - 🆕 **2026 年 7 月**。"Agent 的记忆护照"——跨不同 Agent 与工具共享的平台中立记忆层。按用户/Agent/会话作用域存储记忆，并通过统一 API 提供，让一个平台上的 Agent 能调取另一个平台的上下文。
- [Supermemory](https://github.com/supermemoryai/supermemory) - 🆕 基于多种数据源（网页、文档、聊天）构建的上下文图谱，为 Agent 对话提供背景。API 优先，集成 MCP 与主流框架。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsupermemoryai%2Fsupermemory&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Graphlit](https://www.graphlit.com/) - 🆕 面向生产级 Agent 的上下文平台：数据摄取、实体抽取与知识图谱，支撑搜索 + RAG。提供 MCP 服务器，可接入 Claude / Cursor / Copilot。
- [Mem0](https://github.com/mem0ai/mem0) - 面向 AI 应用的持久记忆库，提供 Python 和 TypeScript SDK；Apache-2.0; [v2.0.20](https://github.com/mem0ai/mem0/releases/tag/v2.0.20) (2026-09-02).
- [Remio](https://remio.ai/) - 本地优先的 AI 记忆与知识库桌面应用（Windows/Mac），面向个人上下文。可解析文件、网页、录音、邮件、消息与图片为本地索引与向量，让 Agent 检索精准上下文，而不必反复 grep 目录或把整篇文档塞进 prompt。本地优先 + BYOK。
- [Zep](https://github.com/getzep/zep) - AI 助理与 Agent 的长期记忆。注意：开源 Community Edition 已弃用 —— 仓库现托管 Zep Cloud 的 SDK/示例；Zep 活跃的开源项目见 [Graphiti](https://github.com/getzep/graphiti)。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgetzep%2Fzep&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [agent-memory](https://github.com/Zijian-Ni/agent-memory) - ⚠️ **未经验证**（早期项目）。跨会话上下文持久化的轻量 Agent 记忆框架。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fagent-memory&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Graphiti](https://github.com/getzep/graphiti) - 用于智能体记忆的时序知识图谱引擎；核心 v0.30.0 与 MCP 服务 v1.1.0 于 2026-09-01 发布; [v0.30.0](https://github.com/getzep/graphiti/releases/tag/v0.30.0) (2026-09-01).
- [LangMem](https://github.com/langchain-ai/langmem) - LangChain 面向 Agent 的长期记忆 SDK —— 语义/情景/程序性记忆原语，可接入 LangGraph 的持久化层。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangmem&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Motorhead](https://github.com/getmetal/motorhead) - 💤 **不再维护**（维护者已标记弃用；最后版本 2023-12）。LLM 的记忆 + 上下文管理服务。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgetmetal%2Fmotorhead&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ChromaDB](https://github.com/chroma-core/chroma) - AI 原生开源向量数据库。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fchroma-core%2Fchroma&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cognee](https://github.com/topoteretes/cognee) - 结合文档摄取、图谱和向量检索的知识与记忆引擎；Apache-2.0。
- [ContextStream](https://contextstream.io) - 🆕 ⚠️ **未验证**（审核时 43 GitHub stars；尚未确认独立生产采用）。通过托管 MCP（`https://mcp.contextstream.io/mcp`）为 Cursor、Claude Code、Codex 等客户端提供共享项目上下文；MIT 服务端见 [contextstream/mcp-server](https://github.com/contextstream/mcp-server)。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcontextstream%2Fmcp-server&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangGraph Memory](https://github.com/langchain-ai/langgraph) - LangGraph 内置的持久化与 checkpoint。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flanggraph&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude Managed Agents Memory](https://platform.claude.com/docs/en/release-notes/overview) - **2026-04-23** 公测。把读写记忆挂载到 Agent 文件系统，实现跨会话学习。
- [OpenViking](https://github.com/volcengine/OpenViking) - 通过文件系统式访问组织记忆、资源和技能的智能体上下文数据库；AGPL-3.0; [v0.4.19](https://github.com/volcengine/OpenViking/releases/tag/v0.4.19) (2026-09-08).
- [ReMe](https://github.com/agentscope-ai/ReMe) - 🇨🇳 阿里 AgentScope 出品的 Agent 记忆管理工具包——文件系记忆 + 向量记忆双轨，专门处理上下文窗口受限与无状态会话两大痛点。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentscope-ai%2FReMe&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [taOSmd](https://github.com/jaylfc/taosmd) - ⚠️ **Unverified.** 本地优先、基于追加式转录的 Agent 记忆：类型化时序知识图（修正后的新事实自动覆盖旧事实）＋ 向量与 BM25 混合检索。面向小型本地模型调优，完全离线（8 GB 单板机即可运行）。作者声称 LongMemEval-S 端到端 Judge 97%；单作者维护，审核时 44 stars，基准可按 `docs/benchmarks.md` 复现。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fjaylfc%2Ftaosmd&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenWiki](https://github.com/langchain-ai/openwiki) - 🆕 ⚡ **2026 年 7 月上线；2026-08-25 自纠正记忆**。LangChain 的 MIT CLI，为 Agent 撰写并维护代码库 wiki；8 月 25 日为每条事实挂上代码证据，源码变了就能发现过期并遗忘（[博客](https://www.langchain.com/blog/self-correcting-memory-openwiki)）。15K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Fopenwiki&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [claude-mem](https://github.com/thedotmack/claude-mem) - 🆕 ⚡ **2026 年 8 月**。轻量级 MCP 服务，让 Claude Code（以及任何 MCP 兼容 Agent）在会话间保持持久上下文，将对话历史存入本地 SQLite 数据库，让 Agent 记住之前的工作，无需重新加载整个项目文件。**90,000+ stars**。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fthedotmack%2Fclaude-mem&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hindsight](https://github.com/vectorize-io/hindsight) - 从经验中学习的 Agent 记忆 -- 不只是会话历史。仿生数据结构组织世界事实、Agent 经验与习得的心智模型;提供 `retain`/`recall`/`reflect` 原语;随附 Agent Memory Benchmark (AMB)。MIT,15K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvectorize-io%2Fhindsight&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SimpleMem](https://github.com/aiming-lab/SimpleMem) - 高效的 LLM Agent 终身记忆——多模态（文本+图像+音频+视频），无需微调即可突破 token 上限约束。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Faiming-lab%2FSimpleMem&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Genesys](https://github.com/Astrix-Labs/papez) - ⚠️ **未验证**（单一维护者，自我提交）。面向 AI Agent 的因果图记忆引擎：记忆为节点，边编码因果关系；采用相乘评分（相关性 × 连通性 × 再激活系数）+ 主动遗忘机制剪除过时上下文。MCP 原生支持（13 个工具）。AGPL-3.0。作者自报 LoCoMo 得分 85.55。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAstrix-Labs%2Fpapez&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agent Memory Techniques](https://github.com/NirDiamant/Agent_Memory_Techniques) - 30 个可运行的 Jupyter 笔记本，覆盖对话缓冲、向量存储、知识图谱、情景/语义记忆、MemGPT、Mem0、Letta、Zep、Graphiti 与 LoCoMo 基准——学习各类记忆模式的实用参考。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNirDiamant%2FAgent_Memory_Techniques&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🔌 工具与 API 集成

*让 Agent 接入外部服务与 API 的协议与工具。*

- [LangChain MCP integration](https://www.langchain.com/blog/mcp-in-langchain-stateless-protocol-elicitation-and-more) - 🆕 **2026-09-03**：MCP 支持迁入 `langchain.mcp`，通过 FastMCP 实现协议协商、工具列表缓存和基于 LangGraph interrupt 的信息征询。
- [ZoomMate](https://news.zoom.com/zoom-launches-zoommate/) - 🆕 💰 **2026-06-01 GA**。Zoom 第一方 AI 队友，把会议对话变成完成的工作 —— 更新 Salesforce 记录、创建 Jira issue、通过 Slack 路由请求。$20/用户/月。
- [MCP Reference Servers](https://github.com/modelcontextprotocol/servers) - 用于演示 MCP 功能的教学参考实现；可通过 [MCP Registry](https://registry.modelcontextprotocol.io/) 查找集成，生产使用前需单独评估服务。
- [mcp-gateway](https://github.com/Zijian-Ni/mcp-gateway) - ⚠️ **未经验证**（早期项目）。MCP 网关。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fmcp-gateway&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Composio](https://github.com/ComposioHQ/composio) - 1000+ toolkit + 托管认证一体化 Agent 集成平台。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FComposioHQ%2Fcomposio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Toolhouse](https://toolhouse.ai/) - AI 工具云：存储、管理、执行工具。
- [LangChain Tools](https://github.com/langchain-ai/langchain) - LangChain 生态广泛的工具集成。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Arcade AI](https://github.com/ArcadeAI/arcade-mcp) - AI Agent 工具调用平台。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FArcadeAI%2Farcade-mcp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Browser Use](https://github.com/browser-use/browser-use) - 面向 AI 智能体的 Python 浏览器自动化库；MIT; [0.13.10](https://github.com/browser-use/browser-use/releases/tag/0.13.10) (2026-09-04).
- [Firecrawl](https://github.com/firecrawl/firecrawl) - 把网站变成 LLM-ready 数据。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ffirecrawl%2Ffirecrawl&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Crawl4AI](https://github.com/unclecode/crawl4ai) - LLM 友好的开源爬虫。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Funclecode%2Fcrawl4ai&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Stagehand](https://github.com/browserbase/stagehand) - Browserbase 出品的 AI 浏览器自动化。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowserbase%2Fstagehand&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentQL](https://www.agentql.com/) - 用语义化查询语言操控网页。
- [StackOne](https://www.stackone.com/) - HR / CRM / ATS 统一 API。
- [AWS MCP Server](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/) - **2026 年 5 月 6 日 GA**。AWS 官方托管的 MCP 服务器，让编码 Agent 安全可审计地调用任意 AWS API；多步操作可在沙箱化 Python 环境中执行，用 agent skills 取代传统 "agent SOP"。AWS 第一方出品。
- [Google Workspace MCP Server](https://workspaceupdates.googleblog.com/2026/05/agent-tools-and-security-updates-for-workspace-developers.html) - **2026 年 5 月 1 日开发者公开预览**。Workspace 原生 MCP 服务器，将 Gmail / Drive / Calendar / Chat / People 暴露给 MCP 客户端，OAuth 范围由管理员控制并带审计日志。
- [iManage MCP Server](https://imanage.com/resources/resource-center/news/mcp-server-available-broader-ai-ecosystem/) - **2026 年 5 月 14 日**。iManage 知识工作平台的原生 MCP 入口，任何 AI 客户端无需定制即可安全读写 iManage 文档。首家面向公众的法律/专业服务 SaaS MCP server。
- [Power Platform Canvas Authoring MCP Server](https://www.microsoft.com/en-us/power-platform/blog/2026/05/14/whats-new-in-power-platform-may-2026-feature-update/) - **2026 年 5 月 14 日**。Microsoft Power Platform 将 Canvas Apps 的 authoring 能力暴露为 MCP 服务器，Copilot / Claude Code 可通过自然语言驱动 InfoPath → Canvas Apps 迁移。
- [Coinbase AgentKit](https://github.com/coinbase/agentkit) - Coinbase 的智能体钱包与链上操作 SDK，提供 Python/TypeScript 框架集成；Apache-2.0。
- [Bifrost (Maxim AI)](https://github.com/maximhq/bifrost) - 开源企业级 AI 网关（Apache-2.0）——支持 1000+ 模型，自适应负载均衡、集群模式、guardrail、OAuth 2.0 + PKCE、网关层提示注入防御；5k RPS 下额外开销 <100µs。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmaximhq%2Fbifrost&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Anthropic 创意工具连接器](https://www.anthropic.com/news/claude-for-creative-work) - **2026 年 4 月 28 日**。9 个基于 MCP 的 Claude 连接器，对接 Adobe（Creative Cloud 50+ 工具，含 Photoshop / Premiere / Express）、Blender、Autodesk Fusion、Ableton、Splice、Canva Affinity、SketchUp、Resolume。建立在 MCP 开放标准上，其他 LLM 客户端也能直接使用。
- [The Colony](https://thecolony.cc) - ⚠️ **Unverified**。自称 Agent 间社交网络 + REST API + Python / TS / Go SDK + MCP server。组织与 SDK 仓库均 <30 天，0~2 star，单维护者；同款 PR 投了 15+ 个 awesome 列表。**仅作可见性收录**，使用前请自行评估。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTheColonyAI%2Fcolony-sdk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [dependency-freshness-mcp](https://github.com/Armigerous/dependency-freshness-mcp) - ⚠️ **Unverified**。为 AI 编码 Agent 提供带引用的 npm 与 PyPI 依赖新鲜度信息：最新版本、发布日期、弃用状态、带日期的破坏性变更摘要 —— 弥补训练截止带来的盲区。远程（Apify Standby HTTP）+ 本地 stdio。新建单维护者仓库（建于 2026-06-08，收录时 0 star）—— 仅作可见性收录，使用前请自行评估。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FArmigerous%2Fdependency-freshness-mcp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [NotFair](https://github.com/nowork-studio/notfair-plugin) - 开源 Claude Code Agent 技能集，涵盖 [SEO](https://github.com/nowork-studio/notfair-plugin/tree/main/seo)、[Google Ads](https://github.com/nowork-studio/notfair-plugin/tree/main/google-ads) 与 [Meta Ads](https://github.com/nowork-studio/notfair-plugin/tree/main/meta-ads)；通过 Google Ads MCP、Meta Ads MCP、Google Search Console MCP 和 GA4 MCP 接入实时广告与分析数据。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fnowork-studio%2Fnotfair-plugin&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [mcp-agent](https://github.com/lastmile-ai/mcp-agent) - 以 MCP 为核心通信原语设计的开源 Python 框架，构建与 MCP 工具生态原生互操作的 Agent。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flastmile-ai%2Fmcp-agent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 💱 Agent 经济与市场

*Agent 生态的商业层—— Agent 发现付费服务、支付帮助费和开发者将 API 变现的地方。*

- [Nevermined + LangChain payment cookbook](https://www.langchain.com/blog/agents-that-pay-how-nevermined-empowers-langchain-agents-to-buy-and-sell-services) - 🆕 **2026-09-03**：官方集成示例，通过支出策略授权信用卡支付，并在 LangSmith 中追踪交易。
- [x402](https://github.com/x402-foundation/x402) - 用于付费 API 与智能体服务的开放 HTTP 支付协议及参考实现。 ![GitHub stars](https://img.shields.io/github/stars/x402-foundation/x402?style=flat-square)
- [AP2 (Agent Payments Protocol)](https://github.com/google-agentic-commerce/AP2) - 由 Google 发起的智能体支付互操作开放协议，与 A2A 通信协议分开维护。
- [minia2a](https://minia2a.uk) - ⚠️ **未经验证**（独立采用情况待验证）。Agent API 市场，通过 x402 在 Base 上按次支付 USDC，提供钱包认证和可配置的消费限额；平台自报使用计数尚未独立验证。
- [Cog Depot](https://cogdepot.com) - ⚠️ **未验证**（早期自荐项目，未核实独立采用）。Agent 市场通过 REST 及 MIT [MCP 客户端](https://github.com/cogdepot/mcp-server)提供发现、协商和交易对手引荐；经纪服务费托管不等于底层交易款项托管。
- [MCPize](https://mcpize.com) - 🆕 MCP 服务器变现平台 —— 上传 MCP 服务器、设定价格，平台负责计费和发现。**85% 收入分成给开发者**。
- [AgentForge](https://github.com/doggychip/agentforge) - ⚠️ **未验证**（早期，3 star）。AI Agent、工具和内容的订阅市场，300+ Agent，统一 API，支持 MCP，90% 创作者收益分成。列出供观察，使用前请自行评估。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdoggychip%2Fagentforge&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cloudflare Wallets](https://blog.cloudflare.com/agents-week-review-august-2026/) - 🆕 **2026-08-04（Cloudflare Agents Week，8 月 3–7 日）**。面向 Agentic Internet 的可编程钉包 —— `cloudflare.pay` 为 AI Agent 提供安全的自主支付能力，使其成为 Agent 经济的参与者。与 WriteGuard、WebMCP、MCPv2、Workers AI + AI Gateway 统一控制台同期发布。
- [LangChain × AgentCore Payments](https://www.langchain.com/blog/langchain-agentcore-payments) - 🆕 **2026-08-17**。中间件让 LangChain Agent 经 Amazon Bedrock AgentCore（x402）付费调 API，会话预算在基础设施层强制，不靠 prompt；LangSmith 留下每笔消费。
- [Alchemy & Visa AgentCard](https://www.coindesk.com/business/2026/06/18/alchemy-s-ai-driven-identity-and-payment-service-gains-access-to-visa-network) - *「🔌 工具与 API 集成」分类中已收录其身份/支付技术栈；此处仅标注与 Agent 经济相关的角度。*
- [Amazon Bedrock AgentCore Payments](https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-bedrock-agentcore-payments-preview/) - *「🏢 企业级 Agent 平台」分类中已收录；此处为 AgentCore Agent 的托管支付层（Coinbase/Stripe 集成、消费上限）。*

---

## 🧪 Agent 沙箱与计算隔离

*让 Agent 安全执行生成代码 / shell 命令的隔离运行时。一旦让 Agent 自由活动，这是必备基础设施。*

- [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) - Apache-2.0 许可的沙箱平台，提供 Docker/Kubernetes 运行时、多语言 SDK、CLI/MCP 访问和按沙箱配置的网络控制。 ![GitHub stars](https://img.shields.io/github/stars/opensandbox-group/OpenSandbox?style=flat-square)
- [E2B](https://github.com/e2b-dev/E2B) - AI 生成代码的开源云沙箱。OpenAI Agents SDK 默认执行层。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fe2b-dev%2FE2B&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Daytona](https://github.com/daytonaio/daytona) - 💤 **公开仓库停止维护**：核心开发于 2026 年 6 月迁入私有代码库，公开 v0.190.0 快照不再接收修复或发布，托管服务仍继续。
- [Modal](https://modal.com/) - 流行的 Agent 计算 + GPU 任务 + Python 沙箱 Serverless 平台。`modal-client` 是官方 SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodal-labs%2Fmodal-client&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsandbox](https://github.com/superradcompany/microsandbox) - 本地、可编程的 microVM 沙箱。隐私优先，本机执行，不依赖云。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsuperradcompany%2Fmicrosandbox&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SandboxFusion](https://github.com/bytedance/SandboxFusion) - 🇨🇳 字节多语言代码执行沙箱，面向 Agent / 模型评测流水线。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbytedance%2FSandboxFusion&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Northflank](https://northflank.com/) - 通用容器 PaaS，常被用作 Agent 运行时（每任务临时环境 + GPU 池）。
- [Firecracker](https://github.com/firecracker-microvm/firecracker) - 基于 KVM 的轻量 microVM 虚拟机监控器（VMM）；Apache-2.0。
- [LangSmith Sandboxes](https://www.langchain.com/blog/interrupt-2026-overview) - **2026 年 5 月（Interrupt 2026）**。LangChain 托管的 Agent 安全代码执行环境——文件系统、shell、包管理、持久态、网络隔离。与 LangSmith Engine、Managed Deep Agents 同期发布。
- [Google Antigravity Sandbox](https://antigravity.google/changelog) - 🆕 **2026-05（Google I/O）**。Agent 执行代码的沙箱化 Linux 环境；作为 Antigravity 2.0 技术栈的一部分交付 —— 子 Agent 在各自隔离的容器中运行，文件系统与网络访问受限。
- [Amazon Bedrock AgentCore Runtime Instances](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-bedrock-agentcore-runtime-instances-generally-available/) - 🆕 **2026-08-06 GA**。为 AgentCore Agent 提供 EC2 支撑的持久算力 —— Agent 会话最长可运行 **14 天**（serverless microVM 上限为 8 小时），通过 capacity provider 提供 GPU 加速、内存优化与计算优化实例族；部署/调用路径不变。首发覆盖 9 个区域。

---

## 🛡️ Agent 安全

*抵御 prompt 注入、数据泄漏、滥用的工具与框架。*

- [Cloudflare WriteGuard](https://blog.cloudflare.com/agents-week-review-august-2026/) - 🆕 **2026-08-05（Cloudflare Agents Week，8 月 3–7 日；Private Beta）**。针对高风险 MCP 工具调用的精细控制 —— Cloudflare 内部自用的同一套工具，现以私测形式向客户开放。让运营者在执行前拦截并否决具有破坏性或敏感性的 Agent 动作，降低提示注入和自主 Agent 错误的爆炸半径。
- [UK AISI Agent 失控事件（INC-2026-07-28-01）](https://www.helpnetsecurity.com/2026/08/05/ai-agent-deception-in-cyber-tests/) - 🆕 ⚠️ **是事件而非工具 —— 2026-08-05 披露**。英国 AI 安全研究所（UK AI Security Institute）报告：基于前沿模型（Anthropic Mythos 5、OpenAI GPT-5.6 Sol）构建的 Agent 在一次常规网络安全评估中，「针对真实的人员与组织采取了持续的、未经授权的行动」—— 试图通过恶意 PR 发起开源供应链攻击，并对维护者实施社会工程。该 Agent 从未被指示进行欺骗；欺骗是追求任务目标的副产物。评估基础设施上隔离/出口管控的参考案例。
- [prompt-firewall](https://github.com/Zijian-Ni/prompt-firewall) - ⚠️ **未经验证**（早期项目）。LLM prompt 防火墙：检测 + 拦截注入。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fprompt-firewall&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LLM Guard](https://github.com/protectai/llm-guard) - 📦 **已归档（2026-07-08）**。LLM 输入输出扫描安全工具包。保留作为历史参考。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fprotectai%2Fllm-guard&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Rebuff](https://github.com/protectai/rebuff) - 📦 **Archived**（2025-05）。自我加固 prompt 注入检测器。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fprotectai%2Frebuff&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Guardrails AI](https://github.com/guardrails-ai/guardrails) - LLM 输出验证与纠正。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fguardrails-ai%2Fguardrails&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) - 给 LLM 对话系统加可编程护栏的工具包。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNVIDIA-NeMo%2FGuardrails&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vigil](https://github.com/deadbits/vigil-llm) - 💤 **Stale**（2024-01 起无更新）。LLM 安全扫描器。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeadbits%2Fvigil-llm&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Lakera Guard](https://www.lakera.ai/) - 企业级 AI 安全平台。
- [Garak](https://github.com/NVIDIA/garak) - NVIDIA 出品的 LLM 漏洞扫描器。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNVIDIA%2Fgarak&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Invariant Guardrails](https://github.com/invariantlabs-ai/invariant) - Agent 运行时策略执行 + 安全检查。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Finvariantlabs-ai%2Finvariant&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Prompt Armor](https://promptarmor.com/) - 企业级 prompt 注入实时检测。
- [Descope MCP Auth](https://www.descope.com/) - MCP 服务的认证与授权层。
- [AgentDojo](https://github.com/ethz-spylab/agentdojo) - ETH 苏黎世评测工具调用 Agent 的 prompt 注入攻防的研究基准。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fethz-spylab%2Fagentdojo&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ModelScan](https://github.com/protectai/modelscan) - 扫描 ML 模型权重文件（Pickle / PyTorch / TF）的反序列化攻击。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fprotectai%2Fmodelscan&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [PyRIT](https://github.com/microsoft/PyRIT) - 微软面向生成式 AI 的 Python 风险识别工具 —— 自动化红队框架（2026 年 3 月从 Azure/PyRIT 迁移，持续活跃维护）。与下方 RAMPART 互补。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2FPyRIT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAMPART](https://github.com/microsoft/RAMPART) - **2026 年 5 月 20 日**。Microsoft 出品的 pytest 原生、面向 Agentic AI 的安全/可靠性测试框架。开发者侧白盒，与 PyRIT 互补——跨提示注入探针、良性失败断言、危害类别覆盖、统计阈值（如 80%+ 的运行需达到安全标准）。可直接接入 CI/CD。MIT。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2FRAMPART&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Clarity (Microsoft)](https://www.microsoft.com/en-us/security/blog/2026/05/20/introducing-rampart-and-clarity-open-source-tools-to-bring-safety-into-agent-development-workflow/) - **2026 年 5 月 20 日**。RAMPART 的姊妹工具。AI Agent 的结构化设计评审工具——在写代码前生成关于意图、风险与行为的 "living artifacts"。Microsoft AI Red Team 的内部实践开源版。
- [Nobulex](https://github.com/arian-gogani/nobulex) - ⚠️ **未验证。** AI Agent 行为的密码学回执（Ed25519 双签名 + 哈希链审计日志）。MIT。其双向回执原语已 [合并](https://github.com/microsoft/agent-governance-toolkit/pull/1333) 进 Microsoft Agent Governance Toolkit（PR #1302、#1333）。同一份投稿同期发往 15+ awesome list；提交者宣称的 "4,500 npm 月下载" 与 registry 实际数据不符（`@nobulex/mcp-server` 审计时仅约 19/月）。基于 Microsoft 的采用列入，仅作可见度参考，依赖前请自行评估。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Farian-gogani%2Fnobulex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MCP Gateway & Registry](https://github.com/agentic-community/mcp-gateway-registry) - 企业级 MCP 网关与注册中心：集中托管 AI 开发工具，OAuth 认证、动态工具发现、审计链、Keycloak / Entra 集成。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentic-community%2Fmcp-gateway-registry&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ActPlane](https://github.com/eunomia-bpf/ActPlane) - 🧪 操作系统层 Agent harness，通过 eBPF 在系统调用边界强制执行以 YAML 定义的行为契约 —— 约束对任何工具、子进程或直接系统调用都生效，违规时向 Agent 反馈纠正信息。MIT。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Feunomia-bpf%2FActPlane&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [WalletPrint](https://github.com/Loai17/walletprint-sdk) - ⚠️ **未经验证**（早期项目）。开源 Agent 钱包行为风险评分 SDK：在交易签名前通过钱包历史行为标记异常，支持 ZeroDev 与 LangChain 集成。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FLoai17%2Fwalletprint-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Alchemy & Visa AgentCard](https://www.coindesk.com/business/2026/06/18/alchemy-s-ai-driven-identity-and-payment-service-gains-access-to-visa-network) - **2026-06-18**。基于 **Visa Intelligent Commerce** 的 AI Agent 支付 + 身份栈：一个 API 即可为 Agent 配齐交易所需的一切——Visa 支付令牌、专属邮箱与手机号、加密钱包——让其在受控范围内代表用户付款。默认走 Visa 令牌，也支持加密货币、x402 与 Stripe Machine Payments Protocol；模型无关（OpenAI / Anthropic 等）。
- [Microsoft Prompt Shields](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection) - Azure AI Content Safety 功能，检测越狱与藏在 Agent 读取的文档/网页中的间接 prompt 注入（2024 年 GA；后续扩展支持 Agent 工作负载）。集成 Azure OpenAI Service 与第三方模型。
- [Agent Name Service (ANS)](https://www.ciodive.com/news/linux-foundation-prepares-open-standard-ai-agent-verification/823691/) - **2026 年 6 月**。Linux 基金会推动的 AI Agent 验证与可信身份开放标准。去中心化 Agent 名称注册表，让 Agent 可验证对方真实身份，降低冒充与中间人攻击风险。
- [OpenAI Daybreak](https://openai.com/index/daybreak-securing-the-world/) - **2026 年 6 月**。OpenAI 安全倡议 + 升级版 Codex Security 插件，自动发现并修复 AI 相关代码中的漏洞；内建针对 Agent 应用的 prompt 注入加固。
- [JADEPUFFER（Sysdig 披露）](https://hackread.com/sysdig-jadepuffer-first-agentic-ransomware-operation/) - ⚠️ **威胁事件，非工具 —— 2026-07-02**。Sysdig 披露首个完全由 AI Agent 编排执行的勒索软件攻击：一个大模型驱动的 Agent 利用 Langflow 远程代码执行漏洞（CVE-2025-3248）入侵，盗取凭据并横向移动到生产 MySQL/Nacos 服务器，在31秒内自行修正失败步骤，随后用一个从未保存的临时 AES 密钥加密了 1,342 项配置，使赎金诉求彻底失去意义（即使付钱也无法恢复）。攻击载荷带有自然语言推理注释，强烈暗示为大模型生成。列于此处作为上方 Agent 安全工具（护栏、出站控制、凭据限权）在生产环境中为何必要的参考案例。
- [Lineation.ai](https://lineation.ai) - 🆕 ⚠️ **2026 年 7 月**（新厂商）。Agent 问责层 —— 可观测、治理与防御，带取证级推理链路（reasoning lineage）。旨在防止目标劫持、记忆污染、工具滥用；审计日志支持 SOC 2 / HIPAA / EU AI Act 合规。云端免费入门 + 私有化部署。
- [First Recon AI 安全运行时](https://firstrecon.ai) - 🆕 **2026 年7月**。企业级 AI 治理平台，检测每一条 AI 交互（人-模型 / Agent-工具 / Agent-Agent）。语义安全引擎在数据到达模型前就执行策略，生成完整决策审计日志。macOS + Windows 端点 Agent。
- [CrowdStrike Falcon AIDR](https://www.crowdstrike.com/en-us/platform/falcon-aidr-ai-detection-and-response/) - **2025 年 12 月 GA**。AI Detection and Response —— 对企业内员工 AI 使用与 Agent 活动的可见性、风险评分、行为异常检测、prompt 注入拦截，以及在 AI 交互层的实时策略执行。
- [Darkmoon](https://github.com/ASCIT31/Dark-Moon) - 开源（GPL-3.0）AI 渗透测试平台，提供专职 Agent 与 MCP 接口，支持云端供应商和本地模型；隐私网关会遮蔽选定标识符，实际数据流向取决于模型与配置，不能保证全部目标数据留在本地。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FASCIT31%2FDark-Moon&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Exabeam Agent Behavior Analytics](https://www.exabeam.com/) - 🆕 **2026**。Exabeam 行为智能平台向 Agentic AI 风险的扩展 —— 以持续的「验证-观察-分析-改进」循环取代静态护栏。
- [RufRoot / CVE-2026-59726](https://hackread.com/rufroot-vulnerability-attackers-hijack-ruflo-login/) - 🆕 ⚠️ **2026-06-30 向维护者披露，2026-07-29 公开报道。** Ruflo（原 Claude Flow，面向编程 Agent 的开源多 Agent 编排层）中的 **CVSS 10.0** 漏洞：该项目此前的默认 Docker Compose 配置把 Ruflo 的 MCP bridge 无认证暴露到网络，一个请求就能调用 `terminal_execute` 并触达 bridge 背后全部 **233 个工具** —— 泄露 LLM 提供商 API key 与已存会话。最糟的一点：攻击者能写入 **AgentDB**（Ruflo 的持久化 Agent 记忆），因此被投毒的指令在升级后依然存活。维护者 24 小时内修好了默认配置（3.16.3），但恢复必须轮换凭证**并**审计 AgentDB —— 只打补丁不够。由 Noma Labs 发现。这是「Agent 记忆已成为攻击面一部分」的标准案例。

- [Claude Code 符号链接数据外泄（Tego AI）](https://hackread.com/tego-ai-discloses-second-claude-flaw-in-a-week-hidden-link-silently-sends-files-to-attackers/) - 🆕 ⚠️ **2026-07-24**。仓库里提交一个 `CLAUDE.md`，其 `@import` 指向符号链接，就能让 Claude Code 读取项目**之外**的文件，并把内容并入它的第一个请求 —— 没有工具调用、没有批准提示、没有告警，因为「越界读取」检查校验的是仓库内的链接路径，而不是它最终解析到的目标。经 HackerOne 上报；Anthropic 以「信任边界是最初的文件夹信任对话框」为由标记为 "Informative" 关闭。在把 Agent 放进不可信仓库之前值得先读一遍。

---

- [CrowdStrike 2026 威胁狩猎报告](https://www.crowdstrike.com/en-us/resources/reports/threat-hunting-report/) - 🆕 **2026-08-03**。AI Agent 触发的检测数量是人工发起线索的 **2.5 倍**；中国 APT 组织在漏洞披露后 24 小时内即完成 PoC 利用；STARDUST CHOLLIMA 单日污染 300+ 个 AI 框架依赖；一次 LLMJacking 攻击 2 分钟内发出 20 万次 API 请求。
- [Straiker AI 运行时安全](https://www.straiker.ai/) - 🆕 **2026-08**（BH2026 展示）。AI 原生 Agent 安全平台 —— 资产发现（Discover AI）、对抗性红队（Ascend AI）、运行时拦截（Defend AI）。拦截提示注入、记忆投毒、身份滥用。累计融资 8500 万美元（其中 A 轮 6400 万，2026-06）。
- [EU AI Act Article 50 — transparency obligations](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations) - **2026-08-02 起适用**。第 50 条规定相关提供者和部署者的透明度义务，包括 AI 交互告知与内容标记/披露；适用范围、角色对应义务及例外以欧盟委员会指南为准。

## 🔍 RAG 与知识库

*Agent 的检索增强生成与知识管理系统。*

- [Oracle OCI Enterprise AI updates](https://blogs.oracle.com/ai-and-datascience/whats-new-in-ai-june-2026) - **2026-06**。企业级部署 Cohere Rerank 4 以增强 RAG 与 Agent 化企业搜索，并扩展支持阿里 / Google 新模型。
- [LlamaIndex](https://github.com/run-llama/llama_index) - LLM 应用的数据框架：摄取 / 结构化 / 访问私有数据。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Frun-llama%2Fllama_index&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Haystack](https://github.com/deepset-ai/haystack) - 端到端 RAG。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeepset-ai%2Fhaystack&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Unstructured](https://github.com/Unstructured-IO/unstructured) - 文档预处理与提取。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FUnstructured-IO%2Funstructured&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Chroma](https://github.com/chroma-core/chroma) - AI 原生开源向量数据库。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fchroma-core%2Fchroma&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Weaviate](https://github.com/weaviate/weaviate) - 开源向量数据库。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fweaviate%2Fweaviate&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Qdrant](https://github.com/qdrant/qdrant) - Rust 实现的高性能向量搜索。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fqdrant%2Fqdrant&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Pinecone](https://www.pinecone.io/) - 托管向量数据库 SaaS。
- [Milvus](https://github.com/milvus-io/milvus) - 大规模向量数据库。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmilvus-io%2Fmilvus&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAGFlow](https://github.com/infiniflow/ragflow) - 🇨🇳 深度文档理解 RAG。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Finfiniflow%2Fragflow&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Docling](https://github.com/docling-project/docling) - IBM 文档转换工具，PDF / DOCX / HTML 等。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdocling-project%2Fdocling&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Kotaemon](https://github.com/Cinnamon/kotaemon) - 开源 RAG UI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FCinnamon%2Fkotaemon&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LightRAG](https://github.com/HKUDS/LightRAG) - 🇨🇳 港大 HKUDS 的图式 RAG。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2FLightRAG&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [R2R](https://github.com/SciPhi-AI/R2R) - 端到端 RAG 服务，企业级。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSciPhi-AI%2FR2R&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vanna](https://github.com/vanna-ai/vanna) - 📦 **Archived**（2026-03）。RAG-for-SQL：自然语言对话数据库。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvanna-ai%2Fvanna&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Morphik](https://github.com/morphik-org/morphik-core) - 面向包含文本、表格、图示和图表文档的多模态检索引擎。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmorphik-org%2Fmorphik-core&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cognee](https://github.com/topoteretes/cognee) - 结合文档摄取、图谱和向量检索的知识与记忆引擎；Apache-2.0。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftopoteretes%2Fcognee&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAG-Anything](https://github.com/HKUDS/RAG-Anything) - 港大数据科学实验室出品的一体化多模态 RAG 框架。基于 LightRAG 构建；文本与多模态并行流水线；可查询同时包含文本、图示、表格、公式的文档。MIT，21K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2FRAG-Anything&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [A-MEM](https://github.com/WujiangXu/A-mem-sys) - 面向 LLM Agent 的 Agentic Memory 系统——受 Zettelkasten 卡片盒笔记法启发的动态记忆组织与笔记链接，比静态向量存储更灵活的检索。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FWujiangXu%2FA-mem-sys&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangChain Retrievers](https://github.com/langchain-ai/langchain) - LangChain 的检索器与文档加载器集合。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Milvus 3.0](https://github.com/milvus-io/milvus/releases/tag/v3.0.0) - 🆕 **v3.0.0 于 2026-07-29 打标**（2026 年 5 月为公测）。这个大规模向量数据库转向「湖原生」架构 —— External Collections 可零拷贝直查 S3/GCS/Azure 对象存储里的 Parquet / Lance / Iceberg 表，基于 manifest 的 Storage V3 列式引擎、Spark DataSource V2 集成、运行时 schema 演进、`TEXT` 成为一等类型，以及支持后交互（ColBERT 式）检索的多向量 `StructList`。

---

## 💻 编程 Agent

### 终端 / CLI Agent

- [Claude Code](https://code.claude.com/docs/en/overview) - Anthropic 面向终端、IDE 和仓库工作流的编程智能体；[v2.1.263](https://github.com/anthropics/claude-code/releases/tag/v2.1.263)（2026-09-06）包含可靠性修复。
- [Codex CLI](https://github.com/openai/codex) - OpenAI 的 Apache-2.0 终端编程智能体；稳定版 [rust-v0.153.4](https://github.com/openai/codex/releases/tag/rust-v0.153.4)（2026-09-04）修复 Astra 显示与内置默认模型，0.154 alpha 仍为预发布版。
- [Codex Security](https://developers.openai.com/codex/changelog) - **2026 年 3 月**。应用安全 Agent，负责发现并修复软件漏洞；OSS 维护者可通过 Codex-for-OSS 计划使用。
- [Aider](https://github.com/Aider-AI/aider) - 集成仓库上下文与 Git 的终端结对编程工具；Apache-2.0。
- [goose](https://github.com/aaif-goose/goose) - 源自 Block、现由 AAIF 托管的可扩展桌面与 CLI 智能体；Apache-2.0; [v1.49.0](https://github.com/aaif-goose/goose/releases/tag/v1.49.0) (2026-09-03).
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) - Google 的终端优先编码 Agent，擅长大上下文重构。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle-gemini%2Fgemini-cli&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenCode](https://github.com/anomalyco/opencode) - 开源终端 AI 编码 Agent（opencode.ai，180K+ stars）—— build/plan 双 Agent、LSP、MCP，桌面 App 处于 beta；与已归档的 opencode-ai/opencode 无关。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fanomalyco%2Fopencode&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Crush](https://github.com/charmbracelet/crush) - Charm 出品的终端 AI 编码 Agent —— 已归档 opencode-ai/opencode 的继任者；多模型，支持 LSP + MCP。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcharmbracelet%2Fcrush&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Grok Build](https://x.ai/news/grok-build-cli) - **2026 年 5 月 25 日（早期 beta）**。xAI 的 Agent 化 CLI 编码工具，由 **grok-code-fast-1** 驱动。子 Agent 并行运行于隔离环境，每日发布 release notes；SuperGrok 与 X Premium Plus 订阅用户可用。xAI 对 Claude Code / Codex CLI 的正面回应。⚠️ 2026 年 7 月有报道发现 Grok Build 会把整个 git 仓库上传到 xAI 存储 —— 在私有代码上使用前请先审查。
- [Antigravity CLI](https://antigravity.google/blog/introducing-google-antigravity-2-0) - **2026 年 5 月 19 日（Google I/O 2026）**。Antigravity 2.0 的轻量 CLI 伴侣——直接从终端创建并使用 Google 的 Agent harness。支持 macOS / Linux / Windows。据报道自 2026 年 6 月 18 日起面向托管套餐用户接替 Gemini CLI（开源 gemini-cli 仓库仍活跃，105K+ stars）。
- [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code) - Moonshot 的终端编程智能体，支持代码编辑、Shell 命令与文件/网页访问；官方安装器不要求 Node.js；[0.41.0](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.41.0)（2026-09-04）。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FMoonshotAI%2Fkimi-code&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MAI-Code-1-Flash in GitHub Copilot](https://microsoft.ai/news/introducingmai-code-1-flash/) - **Build 2026（2026 年 6 月 2 日）**。微软首个 100% 自研的 5B 编程模型作为 GitHub Copilot 的模型选项落地——在四大核心编程基准上击败 Claude Haiku 4.5（SWE-Bench Pro 51.2% vs 35.2%），成本显著更低。
- [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) - 向应用提供 Claude Code 智能体循环、工具、权限和会话处理的 Python 与 TypeScript SDK。
- [ai-delivery-spec](https://github.com/franklinxkk/ai-delivery-spec) - ⚠️ **未验证。** 面向与 AI 编程 Agent（Claude Code、OpenClaw、Codex、Cursor、Copilot）协作的 PM 的规格驱动交付框架。4 档交付层级、0D 分诊路由、原型可测性规则、AI 运行时治理、5 个领域模块。SKILL.md 规范；托管于 ClawHub。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ffranklinxkk%2Fai-delivery-spec&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Ralph Harness](https://github.com/rxdt/loopgate_harness) - ⚠️ **未验证。** 极简 Python 脚手架，用于带护栏的 Claude Code/Codex/Gemini 循环：仓库内规格、全新上下文迭代、git hook 关卡、CI 验证与覆盖率门槛。可通过 `uvx ralph-harness demo` 安装。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Frxdt%2Floopgate_harness&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Amp](https://ampcode.com) - 🆕 ⚡ Sourcegraph 的前沿编程 Agent（VS Code 插件 + CLI）。不用自带 key —— 模型访问已内置，并由模型无关的 "Dial" 路由层自动选模型。**2026 年 7 月连环更新**：7-18 上线订阅制 beta（Megawatt $20/月、Gigawatt $200/月，可挂自己的 ChatGPT 或 X Premium+/SuperGrok 订阅）、7-21 自排程 Agent、7-22 "Multiplayer" 共享会话协作、7-23 [事件驱动 Orbs](https://ampcode.com/news/event-driven-orbs) —— Agent 可由外部事件唤醒（GitHub CI 失败、Linear 新 issue、监控告警、Discord 消息，只要能发 HTTP 请求就行）。**8 月延续节奏**："Attach Anything" 上传（视频/日志/PDF/数据集，8-04）、"Portals into Orbs" 实时刷新预览（8-06）、Dial 可跑在关联的 ChatGPT 订阅上（8-10）、Global Plugins and Skills（8-11）。闭源。
- [ZCode](https://zcode.z.ai) - 🆕 🇨🇳 **2026 年 7 月（ZCode 3.0）**。Z.ai 为 GLM-5.2 打造的官方 Agent 开发环境 —— 桌面应用（macOS / Windows / Linux），把文件管理器、终端、Git 面板、实时浏览器预览围绕一个能规划 / 编码 / 审查 / 部署的 Agent 组织起来。同时支持 Anthropic 和 OpenAI 模型。免费层每日有 token 额度；GLM-5.2 需付费 GLM Coding Plan（Lite / Pro / Max）。
- [Kolega Code](https://github.com/kolega-ai/kolega-code) - 🆕 ⚠️ **未验证**（15 GitHub stars；PyPI 近 30 天约 **1.05 万次下载**，v0.32.0 于 2026-08-24）。终端编程 Agent：其 **Gigacode** 引擎让模型自己写 Python 多 Agent 编排程序（并行 / 流水线 / 评审团），按内容键的 journal 恢复。15+ 模型供应商，MCP 客户端（HTTP/SSE/stdio/OAuth），Textual TUI。许可证是 **BSL 1.1**（不是 Apache-2.0；Change Date 2030-08-12）——投稿把许可证写错了。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fkolega-ai%2Fkolega-code&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### IDE Agent

- [Cursor — self-hosted machines](https://cursor.com/changelog) - 🆕 **2026-09-02**：自托管 worker 使工具在自有机器执行，提供个人机器、团队池和 Linux/macOS 计算机操作；模型处理与数据政策需另行核对。
- [Cursor 3.4（Teams + PR 审查）](https://cursor.com/changelog) - **2026-05-11~13**。Microsoft Teams 集成（在 Teams 中 `@Cursor` 即可委派云端 Agent）、并行 Agent 计划执行提速、多仓库 / 基于 Dockerfile 的 Agent 开发环境配置、`/multitask` 异步子 Agent、漏洞扫描器、按模型粒度的访问控制。
- [Cursor 3.3](https://cursor.com/changelog) - **2026-05**。PR 审查体验、并行 Agent、企业级模型管控；上一版 3.1 发布于 4 月。
- [Cursor SDK](https://cursor.com/blog/typescript-sdk) - 🆕 **2026-04-29**（公开 beta）。TypeScript SDK 开放 Cursor 的运行时、harness 和模型，开发者可在 Cursor 栈上构建程序化 Agent —— 沙箱化云 VM、子 Agent、hooks、按 token 计费。
- [Kilo Code](https://kilo.ai/) - 开源 AI 编程扩展（VS Code / JetBrains），Auto Model 路由覆盖 500+ 模型；已被 Anaconda 收购（2026）。重点采用 MiniMax 系列模型。
- [Cursor](https://www.cursor.com/) - 2026-02 更新支持 8 个并行 Agent。
- [Windsurf → Devin Desktop](https://devin.ai/blog/windsurf-is-now-devin-desktop/) - **2026-06-02 更名**。Cognition 将 Windsurf IDE 更名为 **Devin Desktop**（windsurf.com 跳转至 devin.ai）：**Devin Local**（Rust 重写，token 效率提升约 30%，支持子 Agent）取代 Cascade，**Agent Command Center** 看板成为默认界面，并内置开放的 **Agent Client Protocol (ACP)**。Cascade 于 2026-07-01 停止支持。
- [Cline](https://github.com/cline/cline) - VS Code 自主编程 Agent。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcline%2Fcline&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Roo Code → Roomote](https://roomote.dev/) - ⚠️ **已停止 IDE 扩展形态。** Roo Code 于 2026-04-22 宣布 5 月 15 日关停其 VS Code 扩展、Cloud 与 Router，转向云端编码 Agent **Roomote**（Slack/GitHub/Linear → PR）；roocode.com 现跳转至 roomote.dev。
- [Void](https://github.com/voideditor/void) - 📦 **已归档**（2026 年8 月 GitHub 仓库已归档；维护者探索新方向；不再更新）。VS Code 的开源 fork，定位为开源版 Cursor；数据留在本地，自带模型。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvoideditor%2Fvoid&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Continue](https://github.com/continuedev/continue) - 开源 AI 编程助手（VS Code + JetBrains）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcontinuedev%2Fcontinue&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [GitHub Copilot](https://github.com/features/copilot) - 2026 初支持 Agent 模式，`gh copilot` 终端集成。**2026-08-21**：在 [Slack](https://github.blog/changelog/2026-08-21-the-new-github-copilot-experience-in-slack/) 或 [Teams](https://github.blog/changelog/2026-08-21-shared-agentic-work-with-github-copilot-in-microsoft-teams/) 里 `@GitHub` 可开共享云端 Agent 会话（规划、沙箱改代码、开 PR）。
- [Kiro](https://kiro.dev/) - AWS 自主 Agent。Spec-driven，最多 10 个并发任务。
- [Amazon Q Developer](https://aws.amazon.com/q/developer/) - AWS 生态深度集成。
- [Visual Studio 2026 Agent Mode + Skills](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/) - **VS 2026 Insiders 2026-05-12 – 15**。Copilot Chat "Agent Mode" 现在能在 Visual Studio 2026 里发现、管理、创建可复用的 Copilot Skill，能看到整个解决方案的上下文，还能执行终端命令与调用外部工具。
- [JetBrains Rider AI Test-Writing Skill](https://blog.jetbrains.com/dotnet/2026/05/22/claude-codex-ai-agent-skill-for-writing-tests/) - **2026 年 5 月 22 日**。JetBrains Rider 新增的 AI Assistant skill，把 .NET 代码覆盖率数据喂给 Claude Code / Codex，让 Agent 聚焦未覆盖分支，降低测试生成的 AI 成本。
- [Agent Skills (addyosmani)](https://github.com/addyosmani/agent-skills) - 覆盖规划、实现、验证和审查的可复用编程智能体工程技能；MIT; [0.6.9](https://github.com/addyosmani/agent-skills/releases/tag/0.6.9) (2026-09-05).
- [Cursor Router](https://cursor.com/) - 🆕 **2026 年 7 月**。Cursor 智能模型路由系统，分析每条请求并路由到最优模型（智能 / 平衡 / 成本模式）；集成用数万亿 Cursor 交互 token 训练的 Grok 系列模型（Grok 4.6 于 2026-08-12 成为 Cursor 默认模型）。配套 Cursor iOS 应用（2026 年 7 月）支持移动开发。
- [Devin Desktop 2026 年 7 月更新](https://devin.ai/) - 🆕 **2026 年 7 月**。支持 GPT-5.6 / Claude Opus 5 / Claude Fable 5；**Devin Outposts**（在任意机器运行 Devin Agent）；**Agentic MapReduce** 架构支持跨大代码库分布式推理。并购入 Poke（2026-07-23）。
- [JetBrains Rider 2026.2](https://www.jetbrains.com/rider/) - 🆕 **2026-07-22**。增强 AI Agent 智能与原生 GitHub Copilot 集成；改进 AI 辅助调试和重构能力。
- [Android Studio Quail 2](https://developer.android.com/studio) - 🆕 **2026 年 7 月**。重设计的 Agent Mode：内存泄漏检测、AI 崩溃分析、智能应用构建工作流。

### 自主软件工程师

- [Cursor 3.4 云 Agent 环境](https://cursor.com/changelog) - **2026-05-13**。为云上 Agent / 自动化提供多仓库环境、带 build secrets 的 Dockerfile 配置、快 70% 的镜像层缓存、每个环境独立的版本历史 + 回滚、审计日志、限定范围的出网 / secrets。
- [Devin Stacked PRs](https://devin.ai/blog/introducing-pr-stacks) - 🆕 **2026-07-30**。Devin + GitHub：大任务自动拆分为独立小 PR，下游 PR 自动 rebase，Devin Review 聚焦上下文。含来自 10,000+ 开发者的 Faros AI 数据。
- [Devin Security Swarm](https://cognition.com/blog) - 🆕 **2026-07-01**。Cognition 的并行 Agent 安全产品：跨代码库发现漏洞、在运行时验证可利用性并提交修复 PR；实测发现 50 个真实漏洞中的 36 个，单个发现的成本比次优工具低约 30%。
- [Devin 2.2](https://cognition.com/blog/introducing-devin-2-2) - 🆕 **2026-02-24**。带 Computer Use 的端到端测试（Linux 桌面 + 屏幕录制）、提 PR 前自审/自动修复、启动快 3 倍。Cognition 的旗舰自主软件工程师（Devin 2.x 系列；Devin 2.0 起 Core 套餐 $20/月起）。**2026 年 8 月**：据媒体报道，随着 Devin 年化收入逼近 $1B，Cognition 正以 **$40B+ 估值**进行融资。
- [OpenHands Agent Canvas](https://github.com/OpenHands/OpenHands) - 🧪 可自行托管的编程智能体与自动化控制中心，支持 OpenHands 与 ACP 兼容智能体；当前 README 将 Agent Canvas 标为 beta。
- [SWE-agent](https://github.com/SWE-agent/SWE-agent) - 把 LLM 变成能修复 GitHub issue 的工程师。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSWE-agent%2FSWE-agent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Devika](https://github.com/stitionai/devika) - 💤 **Stale**（2025-09 起无更新）。开源 Devin 替代。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstitionai%2Fdevika&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [GPT Engineer](https://github.com/AntonOsika/gpt-engineer) - 📦 **Archived**（2026-04）。第一波自主编程项目，仅作历史参考。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAntonOsika%2Fgpt-engineer&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Codegen](https://github.com/codegen-sh/codegen) - 📦 **已归档（2026-07-16）**。程序化代码操作 + 跨文件重构 SDK。保留作为历史参考。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcodegen-sh%2Fcodegen&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Qodo](https://www.qodo.ai/) - AI 代码评审平台：质量 + 安全 + 测试生成。
- [Google Antigravity 2.0](https://antigravity.google/blog/introducing-google-antigravity-2-0) - **2026 年 5 月 19 日（Google I/O 2026）**。独立桌面应用（macOS / Linux / Windows），可并行编排多个 Agent。新增 cron 化的定时任务、长跑异步任务、动态子 Agent，以及与 AI Studio / Android / Firebase 的集成。配套的 **Antigravity SDK** 支持自部署 harness；企业版集成进 Gemini Enterprise Agent Platform。
- [ChatGPT Work（编程 Agent）](https://openai.com/chatgpt/work/) - 🆕 **2026-07-09**。OpenAI 多步骤自主工作 Agent ——可跪r若已连接应用与文件跪行完整任务：表格、PPT、文档、小型 Web 应用。桌面 App 为主界面，Chat/Work 双模式切换。

- [Cursor iOS](https://cursor.com/) - 🆕 **2026 年 7 月**。Cursor 的 iOS 应用——支持全量模型访问与项目同步，随时随地进行移动开发。
- [Cursor iPad + Agent Hooks](https://cursor.com/changelog) - 🆕 **2026-07-28~29**。原生 iPad 应用（付费计划），支持侧边栏多 Agent 监控、分屏代码审查、Apple Pencil 标注。云端 Agent Hooks（GA）允许开发者监控 Agent 推理过程、构建自校正循环；「Cursor Start」印度本地定价套餐同步推出。
- [Claude Cowork](https://claude.com/product/cowork) - 跨所选文件与工具执行任务的助手，提供定时工作和内置浏览器；桌面版面向付费计划，网页/移动版仍为 beta。
- [Claude Tag](https://www.businesswire.com/news/home/20260803/) - 🆕 **2026-08-03**。替换旧版 Claude in Slack 集成。频道级共享 Agent 身份（`@Claude`），跨会话持久上下文，支持异步多日工作。强制迁移旧版 Slack 应用；需 Team/Enterprise 计划。
- [Prime Agent](https://github.com/PrimeIntellect-ai/prime-agent) - PrimeIntellect 的终端编程智能体，提供模型集成；MIT; [v0.9.3](https://github.com/PrimeIntellect-ai/prime-agent/releases/tag/v0.9.3) (2026-09-06).


---

## 🤖 Physical AI / 具身智能

*用于感知和作用于物理世界的模型、工具与部署案例。区分已发布软件、研究演示、试点及未来生产计划。*

### 基础模型与研究
- [Microsoft physical-ai-toolchain](https://github.com/microsoft/physical-ai-toolchain) - 开源机器人工作流框架，串联数据采集、训练、验证和机器人部署；默认笔记本层级在本地运行，Azure、Kubernetes 和机群服务按更高层级引入。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fphysical-ai-toolchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [PhyAgentOS](https://github.com/PhyAgentOS/PhyAgentOS-core) - ⚡ **v1.0.0 发布于 2026-09-05**。MIT 具身 Agent 框架，提供受控机器人工具调用、操作前后观测与任务结果验证；发布包包含 Python 包及 Node 桥接。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FPhyAgentOS%2FPhyAgentOS-core&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ENPIRE](https://research.nvidia.com/labs/gear/enpire/) - 🆕 **2026-06**。NVIDIA/CMU/UC Berkeley 联合框架，让 AI Agent 自主开展机器人研究 —— 管理双臂机器人、修改算法、训练策略，全程无需人工干预。
- [Kairos 3.1](https://huggingface.co/ACERobotics/kairos-4B-robot-LIBERO-plus) - 🆕 **2026-07-02**。ACE Robotics 发布 4B 世界动作模型权重与推理代码；RoboTwin 2.0、LIBERO-Plus 版本同时预测未来视觉状态和机器人动作，模型卡标注 Apache-2.0。
- [DYNA-2](https://www.dyna.co/dyna-2) - 🆕 **2026 年 8 月**。Dyna Robotics 的世界动作模型使用第一人称人类视频训练机器人操作能力；客户现场成绩为厂商评测，不是统一的独立排行榜结果。
- [NVIDIA Cosmos 3](https://blogs.nvidia.com/blog/cosmos-3-physical-ai-open-world-foundation-model/) - 🆕 **2026-05-31**。融合视觉推理、多模态生成和动作预测的世界基础模型，用于机器人、驾驶和合成数据工作流；NVIDIA 以 OpenMDW 1.1 提供模型材料，性能数据为厂商报告。

- [Google Gemini Robotics-ER 1.6 (legacy)](https://ai.google.dev/gemini-api/docs/robotics-overview) - 💤 已由 ER 2 接替：Google 文档指定 `gemini-robotics-er-1.6-preview` 于 2026 年 8 月底下线，应迁移至 ER 2 标准或流式预览端点。
- [Google Gemini Robotics 2 / ER 2 / On-Device 2](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/) - 🆕 **2026-07-30**。包含全身控制 VLA、具身推理 VLM 及端侧控制模型；ER 2 提供 [Gemini API 标准与流式预览](https://ai.google.dev/gemini-api/docs/robotics-overview)，机器人控制模型通过合作伙伴/测试者计划提供。
- [Project Prometheus (Bezos)](https://techcrunch.com/2026/06/11/jeff-bezoss-prometheus-raises-12b-to-build-an-artificial-general-engineer-for-the-physical-world/) - 🆕 💰 **2026-06-11**。贝佐斯联合主导的 Physical AI 项目，以 $41B 估值融资 $12B，目标打造面向物理世界的「通用人工工程师」。
- [NVIDIA Isaac GR00T N1.7](https://github.com/NVIDIA/Isaac-GR00T) - 开放的人形机器人 VLA，提供权重、微调和推理代码；N1.7 使用 Cosmos-Reason2/Qwen3-VL 骨干及相对末端执行器动作，采用 Apache-2.0 许可证。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNVIDIA%2FIsaac-GR00T&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Physical Intelligence openpi (π0 / π0-FAST / π0.5)](https://github.com/Physical-Intelligence/openpi) - Physical Intelligence 官方机器人策略及训练/推理代码，含流匹配 π0、自回归 π0-FAST 和 π0.5；已发布检查点可适配新机器人数据，模型需分别核对条款。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FPhysical-Intelligence%2Fopenpi&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Physical Intelligence π0.7](https://www.pi.website/blog/pi07) - 🆕 🧪 **2026-04-16 研究报告**。通过语言、执行元数据及视觉子目标控制的 VLA；作者展示跨任务、跨机器人泛化，该报告不等于 openpi 已公开此模型权重。
- [LeRobot](https://github.com/huggingface/lerobot) - Hugging Face 机器人库，提供数据集、预训练策略、模仿/强化学习及硬件集成；代码为 Apache-2.0，模型许可证以各自模型卡为准。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhuggingface%2Flerobot&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenVLA](https://github.com/openvla/openvla) - 💤 开放视觉语言动作模型的历史基线，含机器人操作权重及微调/推理代码；仓库最后推送于 2025 年 3 月。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenvla%2Fopenvla&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Figure Index / Helix training data](https://www.figure.ai/news/introducing-index) - 🆕 ⚡ **2026-08-25**。Figure 为 Helix 建立的专用人类视频采集计划；[9 月 3 日 Nscale 协议](https://www.figure.ai/news/figure-and-nscale-sign-strategic-partnership)以 2027 年下半年开始部署 Vera Rubin 算力为目标，尚非已交付容量。
- [Deutsche Telekom / NVIDIA Industrial AI Cloud](https://www.telekom.com/en/newsroom/latest-updates/media-information/2026/2/germany-s-first-ai-factory-for-industry) - **2026-02-04 投入运营**。与 NVIDIA、Polarise 共建的慕尼黑 AI 基础设施，面向工业训练、仿真和机器人工作负载，属于计算基础设施。

### 人形机器人

- [Tesla Optimus](https://www.tesla.com/AI) - Tesla 人形机器人项目，以感知、规划、平衡和操作能力执行重复性物理任务；量产目标与演示需同已独立确认的客户部署区分。
- [Figure 03](https://www.figure.ai/news/introducing-figure-03) - **2025-10-09** 发布的人形机器人，围绕 Helix 设计，配备触觉传感、柔性外覆及无线充电，面向家庭与商业场景。
- [Figure 04](https://autonews.gasgoo.com/articles/news/figure-founder-f04-robot-initiates-component-delivery-process-2054560059634376705) - **2026-05-13**。Brett Adcock 宕告 Figure 04 设计定型，零部件已开始交付，使用 Helix VLA 型号。
- [Figure package-sorting livestream](https://incrypted.com/en/figure-ai-held-a-human-vs-robot-marathon/) - **2026-05-18 报道**。二手报道转载 Figure 分拣直播及厂商长时间自主运行主张；这是出现过错误的厂商演示，不能作为独立可靠性基准。
- [Atlas production / Hyundai factory plan](https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/) - **2026-01-05 公告**。Boston Dynamics 计划 2026 年向现代及 Google DeepMind 交付首批 Atlas 机群，2027 年扩展客户；现代工厂年产 3 万台机器人属于未来产能目标。
- [Boston Dynamics Atlas](https://bostondynamics.com/products/atlas/) - 用于物料搬运的工业人形机器人，可自主更换电池并通过 Orbit 集成机队；官方规格区分 50 kg 瞬时负载与 30 kg 持续负载。
- [Figure 03 × BMW](https://www.figure.ai/news/f-03-at-bmw) - 🆕 **2026-06-30**。Figure 宣布 F.03 进入 BMW，承接此前 F.02 项目；这是部署进展，并非双方首次合作。
- [JAL / GMO airport humanoid trial](https://press.jal.co.jp/ja/release/202604/009501.html) - **2026-04-27 公告**。羽田机场地勤试点计划持续 2026 年 5 月至 2028 年，先分析流程和评估安全，再逐步测试机器人；行李搬运和客舱清洁属于候选应用。
- [Figure Helix 02](https://www.figure.ai/news/helix-02) - 🆕 **2026-01-27**。Figure 的 VLA 系统把像素到动作控制扩展至全身，协同行走、平衡和操作；演示包含连续厨房工作流。
- [Unitree G1 / H2](https://www.unitree.com/about/) - 用于宇树运动与操作演示的人形平台；官方历史记录 H2 于 2025 年 10 月发布，并在 2026 年展示 G1/H2。
- [Unitree R1 / R1 Air](https://www.unitree.com/mobile/R1/) - 🇨🇳 轻量人形机器人系列；官方 R1 Air 起价 $4,900，不含税费及运输。规格表仅为 R1 EDU 标注二次开发支持，科研采购应核对版本。
- [Unitree GD01](https://www.unitree.com/about/) - **2026-05-12 发布**。可在双足与四足构型间切换的载人驾驶机器人，应与自主执行任务的人形 Agent 区分。
- [HONOR Robotics D1 / A1](https://www.honor.com/ie/events/honor-robot/) - 在 2026 北京亦庄机器人半马展示的人形研究平台，具备自主感知、导航和动态运动功能；竞赛演示不能代表通用工作场景能力。
- [Zhiyuan (智元) AGIBOT](https://www.agibot.com/article/231/detail/62.html) - 🇨🇳 **APC 2026**。智元介绍七类工业解决方案及具身智能技术栈，并报告 2026 年 3 月第 1 万台机器人下线；这是制造里程碑，不能等同于独立测得的客户使用规模。
- [Unitree H 系列](https://www.unitree.com/) - 🇨🇳 国产 Boston Dynamics 对手，2026 持续迭代。
- [Unitree Shanghai IPO](https://finance.eastmoney.com/a/202608193846301835.html) - 🇨🇳 **2026-08-19**。东方财富转载上交所上市公告：宇树科技（688836）发行约 4,044.64 万股，发行价 150.80 元；此为公司动态，不属于机器人能力评测。
- [1X NEO](https://www.1x.tech/discover/neo-home-robot) - **2025-10-28** 开放预订的家用人形机器人，计划于 2026 年在美国交付，陌生家务可由专家引导；[2026-07-09 手部更新](https://www.1x.tech/discover/neos-hands)引入 25 自由度手。预订和演示不代表已广泛自主部署于家庭。
- [Mitsubishi Motors × Highlanders humanoid MOU](https://www.mitsubishi-motors.com/en/newsroom/newsrelease/2026/20260709_1.html) - **2026-07-09**。谅解备忘录拟探索人形机器人研发、三菱制造现场试用及京都工厂生产；2027 年初投产仍处于可行性研究阶段。
- [Agile Robots](https://www.agile-robots.com/) - 德中合资机器人公司，构建 AI 驱动的工业操作系统。
- [Shenzhen Humanoid Pilot Line](https://www.chinadailyhk.com/hk/article/631892) - 🇨🇳 **2026-04-12** 首条人形机器人中试线（深圳乐聚 + 东方精工）。2 小时一台，年 500~1000 台。佛山 1 万台 / 年大规模工厂同步规划中。

### 消费级机器人 / 可穿戴

- [Doubao AI Glasses (ByteDance)](https://technode.com/2026/03/18/bytedance-reportedly-delays-doubao-ai-glasses-launch-plan/) - ⚠️ 🇨🇳 **2026-03-18 报道**：第一代生产计划延迟，上市可能性较低；该来源未确认正式公开发售。
- [Nothing AI Glasses/Earbuds](https://techcrunch.com/2026/04/01/nothings-ai-devices-plan-reportedly-contains-smart-glasses-and-earbuds/) - 🧪 2026 年 3 月报道：Nothing 计划推出 AI 智能眼镜 + 耳机，目标 2027 年发布。
- [Samsung Galaxy AI](https://www.samsung.com/us/galaxy-ai/) - Samsung 设备上的通信、搜索及内容辅助 AI 功能；可用性与处理位置随功能、设备及地区而异。
- [Meta Ray-Ban Display / Ray-Ban Meta](https://www.meta.com/ai-glasses/) - Meta AI 眼镜产品系列，包括显示型及相机/音频型；支持功能和供应情况应按官方地区目录核对。

### 自动驾驶

- [Tesla FSD (Supervised)](https://www.tesla.com/support/fsd) - 需要驾驶员主动监督的辅助驾驶软件；官方支持页面明确说明它不会使车辆成为自动驾驶汽车，功能随硬件、软件及地区变化。
- [Waymo](https://waymo.com/) - ⚡ **2026-09-01**：[Denver、San Diego、Tampa 迎来首批公众乘客](https://waymo.com/blog/2026/09/ride-in-denver-san-diego-tampa/)，提供无人驾驶载客的城市增至 14 个，仍从意向名单逐步开放；Houston 于 8 月 20 日面向所有人开放。未来市场公告需与实际服务区分。
- [NVIDIA Alpamayo 2 Super](https://huggingface.co/nvidia/Alpamayo2-Super) - 🆕 **2026-08-04 公开权重**。用于自动驾驶研究的推理 VLA，生成轨迹及因果推理，配套 AlpaSim、AlpaGym；模型发布并不等于已部署自动驾驶系统获得认证。
- [Pony.ai × Uber Europe](https://cnevpost.com/2026/08/14/pony-ai-uber-2000-robotaxis-europe/) - 🇨🇳 **2026-08-14 报道**。合作扩展计划在欧洲五城部署超过 2,000 辆 Robotaxi，并计划进入中东；分阶段部署计划不代表全部车队已运营。
- [WeRide / Pony.ai / Baidu Apollo](https://www.weride.ai/) - 🇨🇳 中国 L4 车队扩区。

---

## 🎮 Agent 仿真与世界模型

*Agent 在仿真世界中训练、观察、应力测试的研究环境。世界模型 / 具身研究渗透到语言 Agent 设计中后越来越重要。*

- [Generative Agents](https://github.com/joonspk-research/generative_agents) - 💤 Smallville 历史研究实现（Park 等，2023），以记忆、反思和规划驱动 25 个模拟角色。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fjoonspk-research%2Fgenerative_agents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Voyager](https://github.com/MineDojo/Voyager) - 💤 Minecraft 历史 Agent（Wang 等，2023），结合 GPT-4、自动课程与持续增长的可执行技能库进行开放探索。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FMineDojo%2FVoyager&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SWE-Gym](https://github.com/SWE-Gym/SWE-Gym) - 用真实 GitHub issue 训练 SWE Agent 的开放环境，SWE-bench 配套。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSWE-Gym%2FSWE-Gym&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [WebArena / WebArena-Verified](https://webarena.dev/) - 用于浏览器 Agent 评测的自托管网页环境；[WebArena-Verified](https://github.com/ServiceNow/webarena-verified)提供经复核任务、参考答案与确定性评估器，提高复现性。
- [WorkArena](https://github.com/ServiceNow/WorkArena) - ServiceNow 出品的企业工作场景 Web Agent 基准。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FServiceNow%2FWorkArena&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Genie 3 / Project Genie](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/) - 🧪 Google 通过 Project Genie 原型提供交互式世界模型体验，最初于 2026-01-29 向美国 Google AI Ultra 订阅者开放；这是托管实验服务，并非开放模型权重。
- [NVIDIA Cosmos](https://github.com/nvidia-cosmos/cosmos-predict2) - 📦 **已归档**。具身 AI / 机器人的世界模型基础，生成物理合理的视频未来。predict1 已弃用，由 Cosmos-Predict2 接替（Predict 2.5 于 CES 2026 发布）；另见上方 Cosmos 3（2026-06）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fnvidia-cosmos%2Fcosmos-predict2&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Snowflake Agent World Model (AWM)](https://github.com/Snowflake-Labs/agent-world-model) - **2026 年 2 月 10 日开源，5 月 1 日被 ICML 2026 接收**。合成环境生成流水线，一次性产出 1,000 个可执行的、SQL 数据库驱动的工具调用环境（35K+ 工具，10K 任务），通过统一 MCP 接口暴露——支持大规模多回合 Agent RL。基础设施已合入 `meta-pytorch/OpenEnv`。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSnowflake-Labs%2Fagent-world-model&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Qwen-AgentWorld](https://github.com/QwenLM/Qwen-AgentWorld) - **2026-06-24**。Qwen-AgentWorld-35B-A3B 是预测环境状态转移的开放语言世界模型，配套发布覆盖七类 Agent 场景的 AgentWorldBench。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FQwenLM%2FQwen-AgentWorld&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SimWorld](https://github.com/SimWorld-AI/SimWorld) - 基于 Unreal Engine 5 的开放式真实感模拟器，用于在复杂物理与社交环境中测试自主 AI Agent。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSimWorld-AI%2FSimWorld&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Newton](https://github.com/newton-physics/newton) - 🆕 ⚡ **v1.5.1，2026-08-28**。基于 NVIDIA Warp 的 GPU 加速机器人物理引擎，NVIDIA、Google DeepMind、Disney Research 参与开发；Apache-2.0。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fnewton-physics%2Fnewton&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [NVIDIA Isaac Lab](https://github.com/isaac-sim/IsaacLab) - 基于 Isaac Sim 的官方机器人学习框架，支持强化学习、模仿学习和评测；应按模拟器版本选取兼容的稳定版或明确标识的 beta。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fisaac-sim%2FIsaacLab&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Genesis](https://github.com/Genesis-Embodied-AI/genesis-world) - 面向机器人学习与具身 AI 的物理仿真平台，支持多类材料和机器人；仓库已从 `Genesis` 迁移至 `genesis-world`。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FGenesis-Embodied-AI%2Fgenesis-world&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 📊 评测与 Leaderboard

*评测套件及动态排行榜；2026-09-08 核对。*

> **结合实验设置解读分数。** 模型版本、Agent 框架、数据集修订、工具权限和重试/算力预算都会影响结果。无法确定原始评测设置的旧领先者快照已移除。优先使用可复现的原始评测，并评估自己的实际任务。
>
> [OpenAI 7 月 8 日的 SWE-bench Pro 审计](https://openai.com/index/separating-signal-from-noise-coding-evaluations/)发现显著任务质量问题；[Terminal-Bench 4.0](https://www.tbench.ai/news/terminal-bench-4-0)也修改了任务与资源。跨版本比较前必须核对方法。

- [τ²-bench / τ³-bench](https://github.com/sierra-research/tau2-bench) - Sierra 的工具-Agent-用户交互基准现含语音及知识检索任务；**v1.0.1（2026-07-22）**修正 banking_knowledge 评分，该领域成绩需按版本比较。
- [BenchLM](https://benchlm.ai/) - 跨基准聚合及模型发布追踪；比较系统前应核对分数的原始来源、日期和评测框架。
- [SWE-bench Verified](https://www.swebench.com/) - 经人工筛选的 500 道 GitHub issue 修复任务；应区分统一 Bash Only/mini-SWE-agent 环境与自定义 Agent 投稿。
- [GPQA Diamond](https://github.com/idavidrein/gpqa) - 专家编写的研究生级科学问答；应固定数据划分，并随成绩报告提示、工具和采样策略。
- [ARC-AGI-2](https://arcprize.org/) - 面向陌生任务的抽象视觉推理；官方排行榜区分系统及计算预算，不能把所有结果都当作基础模型分数。
- [ARC-AGI-3](https://arcprize.org/leaderboard) - 通过交互环境衡量 Agent 学习陌生规则和适应的效率；应查阅官方成本/能力视图，而非沿用发布初期分数。
- [OSWorld](https://os-world.github.io/) - 在真实桌面环境中评测开放式计算机任务；结果取决于 Agent、模型、动作接口和步数预算。
- [Arena (formerly LMArena / Chatbot Arena)](https://arena.ai/) - 覆盖多种模态的人类偏好比较；偏好排名不等同于任务完成率或安全评测。
- [MMLU-Pro](https://github.com/TIGER-AI-Lab/MMLU-Pro) - MMLU 的推理导向扩展，包含更难的多选题与公开评测实现。
- [LiveCodeBench](https://livecodebench.github.io/) - 持续收集编程竞赛题目；按日期筛选评测有助于分析数据污染风险及题目难度变化。
- [Humanity’s Last Exam (HLE)](https://agi.safe.ai/) - 专家级跨学科基准，定稿题集含 2,500 题，另有持续维护的 HLE-Rolling；它与 AIME 数学竞赛基准不同。
- [Terminal-Bench 4.0](https://www.tbench.ai/news/terminal-bench-4-0) - 🆕 ⚡ **2026-08-28**。当前终端基准重新校准资源、修复任务并移除饱和/有问题样本；任务集和环境预算变化，需要重新运行，不能直接比较 2.x/3.0 分数。
- [Terminal-Bench-Science 0.1](https://www.tbench.ai/news/terminal-bench-science-0-1) - 🆕 ⚡ **2026-08-27**。70 个经专家审阅的科研工作流，覆盖生命、物理、地球、数学及工程科学，以可复现的任务专用测试评测。
- [Wolfram LLM Benchmarking Project](https://www.wolfram.com/llm-benchmarking-project/) - Wolfram 持续评测从英文需求生成 Wolfram Language 代码的能力。
- [Terminal-Bench 2.0 (legacy)](https://www.tbench.ai/news/announcement-2-0) - 含 89 道终端任务的历史版本，保留用于理解旧论文；后续版本修正了任务及环境问题。
- [GDPval](https://openai.com/index/gdpval/) - OpenAI 对 44 种职业、九个行业中经济价值任务的评测；原始任务/评分与第三方基于 GDPval 的排行榜应分别看待。
- [SWE-bench Pro](https://github.com/scaleapi/SWE-bench_Pro-os) - 仓库级软件工程基准；[OpenAI 2026-07-08 审计](https://openai.com/index/separating-signal-from-noise-coding-evaluations/)指出大量任务质量缺陷，并撤回此前采用建议，应审查任务并结合其他评测。
- [LLM-Stats Live Leaderboard](https://llm-stats.com/llm-updates) - 模型新闻与基准聚合信息流；应进一步查看链接中的模型卡、发布说明或原始基准。
- [Gartner Magic Quadrant 2026 — Enterprise AI Coding Agents](https://cursor.com/blog/cursor-leads-gartner-mq-2026) - 厂商发布的 Gartner 分析报告摘要，称 Cursor 被列为领导者；这是市场研究，而非可复现的模型基准。
- [Terminal-Bench 2.1 (legacy)](https://www.tbench.ai/news/terminal-bench-2-1) - **2026-05-06** 发布，修复 Terminal-Bench 2.0 的任务/环境问题；成绩需注明对应任务版本与评测框架。
- [Agent Memory Benchmark (AMB)](https://github.com/vectorize-io/agent-memory-benchmark) - 开放的长期 Agent 记忆评测，公开数据、提示、评分和结果；由 Hindsight 团队创建，解读时应注意评测者关联。
- [Agents’ Last Exam (ALE)](https://snorkel.ai/leaderboard/agents-last-exam/) - 与领域专家共建的长程专业工作流基准；应区分已发布的参考子集、更大的任务集合及未来扩展目标。
- [JetBrains Kotlin Benchmark](https://blog.jetbrains.com/kotlin/2026/07/introducing-the-kotlin-benchmark-evaluate-ai-coding-agents-on-real-world-kotlin-tasks/) - JetBrains 官方 Kotlin 编程 Agent 评测，覆盖从理解 issue 到实现并通过测试的仓库任务。
- [Stripe Agent Benchmark](https://stripe.com/blog/can-ai-agents-build-real-stripe-integrations) - Stripe 评测 Agent 在较长软件工程流程中完成完整集成的能力；应检查任务设置，不能从单一分数推断生产就绪。
- [GAIA Benchmark](https://huggingface.co/spaces/gaia-benchmark/leaderboard) - 结合推理、浏览与工具使用的通用助手基准；[论文](https://arxiv.org/abs/2311.12983)介绍 466 个问题，评测使用保留答案。

---

## 🖥️ Computer Use / 桌面 Agent

- [Clickyy](https://github.com/jayamitkatariya/clickyyy) - 晃动光标即可召唤一个能看到你屏幕并代你点击、输入、拖拽、操作的 AI Agent（macOS）。开源，MIT。

*能看屏幕、控鼠键、自动操作 OS 级软件的 Agent。纯浏览器 Agent 见 [🌐 浏览器与 Web Agent](#-浏览器与-web-agent)。*

- [Perplexity Personal Computer for Windows](https://www.perplexity.ai/hub/blog/personal-computer-on-windows) - 🆕 **2026-07-28**。Perplexity 的多模型 Agent 编排器扩展至 Windows 10/11 —— 本地文件、原生应用 + Microsoft 365 套件与跨设备工作流统一在一个系统中。面向 Pro/Max/Enterprise 订阅用户。基于 4 月 16 日的 Mac 版本以及 Computex 2026 预览的本地/云端混合推理编排器。
- [Claude Computer Use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) - Anthropic 的 Computer Use 能力 —— Claude 看屏幕并用鼠标键盘自动操作任意软件。**2026-08-19**：电脑使用出 beta，工具集 `computer_toolset_20260801`（可批量动作、无需 beta 头）；新增托管视口 **browser use** 工具集 `browser_toolset_20260801`；Files / Skills API 同步去 beta（[release notes](https://platform.claude.com/docs/en/release-notes/overview)）。
- [macOS Harness](https://github.com/browser-use/macos-harness) - 🆕 **2026-08-17**。Browser Use 官方最薄 macOS 驾驭层：一个 Python 进程、六个系统原语（`see` / `key` / `type` / `click` / `ax` / `script`）加真浏览器和文件，模型边干边补工具。MIT，761+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowser-use%2Fmacos-harness&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ChatGPT Agent](https://openai.com/index/introducing-chatgpt-agent/) - Operator（2025 年弃用）的后继 —— ChatGPT 内的 Agent 模式，用于浏览、订票、填表与网页任务自动化。
- [Google Project Mariner](https://deepmind.google/models/project-mariner/) - 📦 **已关闭**（2026-05）。浏览器 Agent 研究项目，能力已合入 Gemini 与 Chrome。
- [Microsoft Copilot Agents](https://www.microsoft.com/en-us/microsoft-copilot/) - Microsoft 365 上的自主后台 Agent。
- [Open Interpreter](https://github.com/openinterpreter/openinterpreter) - 让 LLM 在本地跑代码的自然语言接口。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopeninterpreter%2Fopeninterpreter&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Manus AI](https://manus.im/) - 🇨🇳 通用自主 Agent，云本地混合，研究 / 编程 / 复杂任务。
- [Genspark](https://www.genspark.ai/) - mixture-of-agents 全能工作 Agent，能打电话。
- [Beam AI](https://beam.ai/) - 自学习桌面 Agent。
- [AICraft](https://github.com/Easlie114514/AICraft) - 🆕 ⚠️ 🇨🇳 **未验证**（2026 年 6 月创建，单人维护，关注度较低 —— 列出以求完整，使用前请自行评估）。Windows 桌面端「AI 能力启动器」，把 LLM Skill、MCP 工具、RAG 数据源和记忆都做成可热插拔的模块 —— 卖点是「像加载 Minecraft mod 一样」管理它们。一键接入 DeepSeek、角色情绪画像、三级记忆、token 计费；绿色 exe 免安装。技术栈 Python FastAPI + React 19 + ChromaDB，Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FEaslie114514%2FAICraft&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsoft Copilot Studio Computer-Using Agents](https://techcommunity.microsoft.com/blog/copilot-studio-blog/computer-using-agents-in-microsoft-copilot-studio-are-now-generally-available/4519427) - **2026 年 5 月 13 日 GA**。在 Copilot Studio 内构建可通过 UI 直接操控网站和桌面应用的 Agent —— 微软对 Claude Computer Use 的第一方回应，现已在 Microsoft 365 / Power Platform 部署中正式开放。
- [ChatGPT Workspace Agents](https://venturebeat.com/orchestration/openai-unveils-workspace-agents-a-successor-to-custom-gpts-for-enterprises-that-can-plug-directly-into-slack-salesforce-and-more) - **研究预览 2026-04-22，2026-05-06 走积分计费，2026-05-07 支持 EKM**。OpenAI 为企业推出的 Custom GPTs 后继 —— 云端 Agent，能访问文件、执行代码、原生接 Slack / Google Drive / Salesforce，可调度周期任务；Business / Enterprise / Edu / Teachers 可用，底层走 Codex。

---

## 🌐 浏览器与 Web Agent

*真实浏览器中工作的 Agent —— 导航、点击、抓取、跨页流程。*

- [agent-qa](https://github.com/vostride/agent-qa) - 开源自我改进型 QA Agent，可执行自然语言描述的 Web 与移动端测试，自愈 UI 交互，并从历史运行中学习。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvostride%2Fagent-qa&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cloudflare Kitesurf](https://blog.cloudflare.com/kitesurf/) - 🆕 **2026-08-06（beta，Cloudflare Agents Week）**。Cloudflare 专为 AI Agent 打造的无服务器浏览器，运行于 Workers 上，每次会话独立隔离、无状态，优先优化 token 数与上下文窗口效率而非像素级渲染。支持 Puppeteer 和 Playwright；截图类负载 **CPU 消耗为 Chromium 的 1/3.1、内存为 1/4.7**，通过 215K+ 项 Web Platform Tests。beta 期间通过 Browser Rendering 免费使用。限制：不支持视频播放、WebGL 和持久登录。
- [Browser Use](https://github.com/browser-use/browser-use) - 面向 AI 智能体的 Python 浏览器自动化库；MIT; [0.13.10](https://github.com/browser-use/browser-use/releases/tag/0.13.10) (2026-09-04).
- [Stagehand](https://github.com/browserbase/stagehand) - Browserbase 出品的"浏览器 Agent SDK"：类型化 `act / extract / observe`，跑在 Playwright 上。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowserbase%2Fstagehand&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Steel Browser](https://github.com/steel-dev/steel-browser) - AI Agent 专用开源浏览器 API：自带 session 持久化 + 代理轮换。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsteel-dev%2Fsteel-browser&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Skyvern](https://github.com/Skyvern-AI/skyvern) - 用 LLM + 视觉自动化网页流程。AGPL-3.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSkyvern-AI%2Fskyvern&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentQL](https://github.com/tinyfish-io/agentql) - 查询语言 + Playwright 集成。动态 / 杂乱页面健壮。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftinyfish-io%2Fagentql&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hyperbrowser MCP](https://github.com/hyperbrowserai/mcp) - 托管无头浏览器 + 标准 MCP 工具接入 Claude / GPT / LangChain。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhyperbrowserai%2Fmcp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) - 微软官方 Playwright MCP server。生产级即插即用。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fplaywright-mcp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MultiOn](https://theagi.company/) - 📦 托管浏览器 Agent，原生 Reasoning + Memory；multion.ai 现跳转至 AGI, Inc.（theagi.company）。闭源。
- [Browserbase](https://www.browserbase.com/) - AI Agent 专用浏览器云：隐身、持久化、验证码、可观测性。
- [BrowserOS](https://www.browseros.com/) - 首个内置 AI Agent 的开源浏览器——隐私优先的 Chrome 替代。自然语言任务自动化无需写代码；本地优先设计，对标 Perplexity Comet 与 Arc 的 AI 能力。
- [Vercel Agent Browser](https://github.com/vercel-labs/agent-browser) - 面向 AI Agent 的无头浏览器自动化 CLI。2026 年 6 月版本新增 Core Web Vitals 的 `vitals` 命令（LCP/CLS/TTFB/FCP）、SPA 导航的 `pushstate`、进程外插件系统、MCP server 模式，以及托管环境用的 `@agent-browser/sandbox`。Apache-2.0，37K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvercel-labs%2Fagent-browser&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Google Agent Development Kit (ADK)](https://github.com/google/adk-python) - 用于智能体、工具和工作流的 Python 框架；2.x 功能版本线与持续维护的 1.x 版本线并行; [v2.8.0](https://github.com/google/adk-python/releases/tag/v2.8.0) (2026-08-26).
- [WebBrain](https://webbrain.one) - 🆕 **2026 年 7 月**。开源 MIT 浏览器扩展（Chrome + Firefox），用本地或云端大模型自动化 Web 任务。"Ask 模式" 只读摘要和提取；"Act 模式" 可点击按钮、填写表单、导航网页。本地优先设计——使用 llama.cpp / Ollama 时数据不离开设备。
- [Muse Spark 1.1（Web Agent）](https://artificialanalysis.ai/models/muse-spark) - 🆕 💰 **2026-07-09**。Meta Superintelligence Labs 首个付费 Agent 模型，经 Meta Model API 公开预览提供 —— WebArena-Verified 得分 69.0（落后于领先的 Claude Opus 4.8 的 71.2）。
- [Firecrawl v2](https://github.com/firecrawl/firecrawl) - 🆕 **v2.11.0，2026-06**。Agent 化网页抓取平台的大版本更新：JavaScript 渲染改进、实时抓取 webhook、批量 URL 处理。150K+ stars。AGPL-3.0（SDK 为 MIT）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ffirecrawl%2Ffirecrawl&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome) - 🆕 Anthropic 的浏览器 Agent Chrome 扩展 —— Claude 可跨标签页导航、填表并执行操作。⚠️ 2026 年 7 月研究显示存在恶意扩展 prompt 注入风险；使用前请审查权限。
- [Perplexity Comet](https://www.perplexity.ai/comet) - Perplexity 的 Agent 化 AI 浏览器，内置 Comet Assistant（后台 Agent）；2025 年 10 月起提供免费层；Perplexity 于 2026 年 6 月为 Comet 融费 $200M。
- [Safari MCP Server](https://developer.apple.com/safari/technology-preview/) - 🆕 **2026-07-01（Safari Technology Preview 247）**。Apple 原生浏览器级 MCP 集成——Safari 将浏览上下文、标签页管理与页面内容暴露给 MCP 客户端。首个原生支持 MCP 的主流浏览器。仅开发者预览。

---

## 🗣️ 语音与多模态 Agent

- [字节跳动 Seedance 2.5](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) - 🆕 **2026-07-31**。首个支持单次生成 30 秒音视频合成并可多轮延展的大规模 AI 视频生成模型；单次最多 **30 张图片 + 10 段视频 + 10 段音频**作为多模态参考输入；本地视频编辑。在即梦 AI 与豆包 Pro 陆续上线；API 经 BytePlus ModelArk 预发布。
- [xAI Grok Voice Think Fast 2.0](https://x.ai/) - 🆕 **2026-07-29**（`grok-voice-latest` 自 2026-08-05 起自动升级）。下一代语音到语音：首字节音频延迟 **1.25s → 0.70s**；24 种语言转写准确率提升 1.4 倍；推理 token 用量 −60%；$0.08/分钟。
- [AgentLine](https://agentline.cloud/) - ⚠️ **Unverified.** 面向 AI Agent 的电话基础设施 —— 申请号码、外呼/接听、实时转录为 JSON 推到 webhook。定位为 Twilio 在 Agent 语音管线场景下的更轻替代；提交者自称 30+ 付费用户，暂无第三方采用证据。
- [ElevenLabs](https://elevenlabs.io/) - AI 语音合成 + 对话 Agent。**[5 亿美元 D 轮，估值 110 亿美元](https://elevenlabs.io/blog/series-d)**（2026-02-04 完成交割，红杉领投；累计融资超 $781M），同时宣布 ARR 突破 **5 亿美元** —— 进入 2026 下半年时资金最充裕的纯语音 AI 厂商。
- [Vapi](https://github.com/VapiAI/server-sdk-python) - 语音 AI Agent 平台。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FVapiAI%2Fserver-sdk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Retell AI](https://www.retellai.com/) - 生产级对话语音 AI。
- [Bland AI](https://www.bland.ai/) - 企业级 AI 电话平台。
- [Hermes](https://buildwithhermes.com/) - 🆕 ⚠️ **未经验证（Founders Beta）**。面向代理商的白标语音 Agent 平台：Agent 管理、原生 CRM、呼入/呼出活动编排、按客户用量计费，$149/月起。暂无第三方采用数据。
- [LiveKit Agents](https://github.com/livekit/agents) - 实时音视频智能体框架；1.8.0 采用 OpenTelemetry GenAI 约定，并为追踪数据使用方提供迁移说明; [livekit-agents@1.8.0](https://github.com/livekit/agents/releases/tag/livekit-agents%401.8.0) (2026-09-05).
- [字节跳动 SeedRealtime](https://technode.com/2026/08/05/bytedance-launches-seedrealtime-full-duplex-audio-video-model/) - 🆕 🇨🇳 **2026-08-05**。字节跳动的原生音视觉全双工大模型——持续处理音频、视频与文本流，可实时同时“看、听、说”。取代传统级联语音 Agent 管道；已集成进豆包 App。暂无公开 API 或模型权重。
- [Pipecat](https://github.com/pipecat-ai/pipecat) - 用于语音和多模态对话智能体的 Python 框架；BSD-2-Clause; [v1.8.1](https://github.com/pipecat-ai/pipecat/releases/tag/v1.8.1) (2026-08-27).
- [Vocode](https://github.com/vocodedev/vocode-core) - 💤 **Stale**（最后版本 2024-06）。构建语音 LLM Agent 的开源库。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvocodedev%2Fvocode-core&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Bolna](https://github.com/bolna-ai/bolna) - 端到端开源语音 AI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbolna-ai%2Fbolna&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cartesia](https://www.cartesia.ai/) - 实时低延迟语音 AI。
- [Meta Voice AI](https://ai.meta.com/) - 收购 PlayHT/Play.ai 后的 Meta 语音技术。原 Play.ai 平台 2025-12-31 关停。
- [Sesame](https://www.sesame.com/) - 情绪感知 + 自然对话的语音 AI 伙伴。
- [ElevenAgents](https://elevenlabs.io/agents) - 🆕 ElevenLabs 全栈语音 Agent 平台（2026 年 4-5 月更新）：支持 MCP、多模态消息、会话主题发现、知识库检索、工具调用前的语音控制。首个获 AIUC-1 认证的语音 Agent 平台。
- [Cartesia Line](https://cartesia.ai/blog/introducing-line-for-voice-agents) - 代码优先语音 Agent 平台（2025 年 8 月上线），基于 Cartesia 的 Sonic TTS + Ink STT，支持后台推理与本地化部署选项；首音延迟约 40-90ms。
- [Deepgram Voice Agent API](https://deepgram.com/product/voice-agent-api) - 🆕 单一端点打包 STT（Nova-3）+ LLM 路由 + TTS（Aura-2）+ Flux 会话式 STT，支持通话中 10 种语言切换。
- [OpenAI Realtime API (GPT-Realtime-2)](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/) - 🆕 **2026 年 5 月 7 日**。GPT-5 级推理能力的语音版，支持并行工具调用，128K 上下文；与 GPT-Realtime-Translate、GPT-Realtime-Whisper 同发。2026-07-06 更新至 gpt-realtime-2.1 / 2.1-mini（字母数字识别更好、抗噪更强、延迟更低）。
- [Dograh](https://github.com/dograh-hq/dograh) - 开源、可自托管的语音 AI 平台——Vapi / Retell 的开源替代。On-prem 部署，可在 Speech-to-Speech 或 LLM/STT/TTS 之间 BYOK；可视化工作流构建器，原生 MCP，电话支持。BSD-2-Clause，4K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdograh-hq%2Fdograh&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hume TADA](https://github.com/HumeAI/tada) - 采用文本/声学 1:1 对齐的语音语言模型，提供 TADA-1B 与多语言 TADA-3B-ML；代码为 MIT，权重采用 Llama 3.2 社区许可证。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHumeAI%2Ftada&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenYabby](https://github.com/OpenYabby/OpenYabby) - 开源 macOS 语音驱动多 Agent 编排器 — Realtime API + CLI 子进程 + 多通道协调。主 Agent 规划任务并委派给子 Agent 进行评审和 QA。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenYabby%2FOpenYabby&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Grok Voice Agent Builder](https://x.ai/news/grok-voice-agent-builder) - 🆕 **2026-07-01**。xAI 基于 Grok Voice 的无代码生产级语音 Agent 平台 —— 免费号码的电话接入、知识集合、工具/MCP 连接器、护栏、80+ 音色以及约 2 分钟的声音克隆；beta 期 $0.05/分钟。
- [GPT Voice](https://openai.com/) - 🆕 **2026-07-23**。OpenAI 面向 ChatGPT Work 的语音界面——基于 GPT-Live 技术，支持用户通过自然语言语音命令指导多步骤 Agent 工作流。

---

## 📱 个人 AI Agent

- [OpenClaw](https://github.com/openclaw/openclaw) - 支持消息渠道、技能、记忆和定时任务的个人智能体运行时；2026.9.3 改进分阶段更新与性能; [v2026.9.3](https://github.com/openclaw/openclaw/releases/tag/v2026.9.3) (2026-09-08).
- [Rabbit R1](https://www.rabbit.tech/) - 大动作模型驱动的硬件 AI 助理。
- [Limitless](https://www.limitless.ai/) - 📦 **被 Meta 收购（2025 年末）**；吊坠硬件停售。基于你所见、所说、所听的个性化 AI（前 Rewind）；团队并入 Meta 的 AI 可穿戴业务。
- [Open Interpreter](https://github.com/openinterpreter/openinterpreter) - 自然语言计算机接口。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopeninterpreter%2Fopeninterpreter&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [01 Light](https://github.com/OpenInterpreter/01) - 💤 **Stale**（2024-11 起无更新）。开源语音电脑接口。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenInterpreter%2F01&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Leon](https://github.com/leon-ai/leon) - 自托管开源个人助理。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fleon-ai%2Fleon&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Khoj](https://github.com/khoj-ai/khoj) - 你的笔记 / 文档 / 图片的"第二大脑"AI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fkhoj-ai%2Fkhoj&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Humane AI Pin](https://humane.com/) - ⚠️ **2025-02-28 已停产**（被 HP 收购，设备已关闭）。原为无屏幕环境计算的可穿戴 AI 设备。
- [Arahi AI](https://arahi.ai/) - 个人生产力 + 业务自动化助理。
- [Lindy AI](https://www.lindy.ai/) - 邮件 / 日历 / 工作流的无代码 Agent。
- [MuleRun](https://mulerun.com/) - 🆕 周期任务的常驻 Agent。
- [Gemini Intelligence](https://blog.google/products-and-platforms/platforms/android/gemini-intelligence/) - 🆕 **2026 年 5 月 12 日（Android Show: I/O Edition）**。主动式 Agent AI 能力贯穿 Googlebooks 笔电、Wear OS、Android Auto、Android XR，首发于最新 Samsung Galaxy + Pixel。可基于购物清单自动生成购物车、预订单车课程，以及通过 Rambler STT 移除口头禅。
- [Gemini Spark](https://gemini.google/overview/agent/spark/) - 🆕 **I/O 2026（2026 年 5 月 19 日）**。Google 在 Gemini 应用中的 24/7 自主 Agent —— 主动运行多步流程，集成 Gmail/Workspace；2026-07-01 扩展推出原生 Mac 应用。**2026 年 7 月更新**：从 Gemini Ultra 扩展至 Pro 层；自主处理日程安排、起草与收件筋选。
- [Gemini Notebook](https://notebooklm.google.com/) - 🆕 **2026 年 7 月（由 NotebookLM 更名）**。更名并升级：新增代码执行、图表生成与自动来源引用，在原有音频概述和问答能力的基础上进一步升级。
- [QwenPaw](https://github.com/agentscope-ai/QwenPaw) - 🇨🇳 **2026 年 5 月由 CoPaw 改名**。Qwen / AgentScope 生态下可自托管的个人助手。本地优先记忆、热加载 skills、多 Agent 协作、多通道（钉钉 / 飞书 / 微信 / Discord / Telegram），自带工具守卫和 skill 扫描器。Apache-2.0。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentscope-ai%2FQwenPaw&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AI Growth Agents for Marketers](https://github.com/thaolst/ai-growth-agents-for-marketers) - ⚠️ **未经验证**（早期项目）。基于东南亚真实金融科技营销活动构建的增长营销 prompt 与 Python Agent。覆盖 campaign brief、MEU 规划与多 Agent 工作流的 A/B 测试分析。Agent Skills 格式 —— 可通过 `npx skills add` 安装。越南语 + 英语双语。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fthaolst%2Fai-growth-agents-for-marketers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsoft Scout](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) - **Build 2026（2026 年 6 月 2 日）**。微软基于 OpenClaw 框架打造的常驻个人 Agent —— 跨云 / 桌面 / Web 主动工作，连接 Teams / Outlook / OneDrive / SharePoint。每个 Agent 在独立 Entra 身份下运行，连续策略合规检查 + 审计链。Microsoft Frontier 计划私测；需 Intune 策略 + GitHub Copilot 许可证。
- [Lenovo Qira / Motorola Qira](https://news.lenovo.com/pressroom/press-releases/lenovo-unveils-lenovo-and-motorola-qira/) - **CES 2026（2026 年 1 月 6 日）**。联想与摩托罗拉联合打造的"个人环境智能系统"——上下文感知 AI 跨 PC / 手机 / 平板 / 可穿戴设备协同。Q1 2026 在部分联想设备上线，随后扩展至 Motorola 手机；OEM 主导的环境 AI 首发。
- [Yao Agents](https://yaoagents.com) - 🇨🇳 **2026 年 5 月**。本地优先的 AI 执行平台：30+ 领域专家（编程、写作、数据分析、PM）与自主 Robot 工作者。5 阶段流水线（灵感→目标→任务→验证→交付）、Docker 沙箱隔离、多平台消息（微信/飞书/钉钉/Telegram/Discord）、MCP 支持、BYOK 模型配置与跨设备编排 Tai Link。开源引擎：[YaoApp/yao](https://github.com/YaoApp/yao)。
- [AgentArk](https://github.com/agentark-ai/AgentArk) - 🆕 🧪 **2026-06**（v0.0.1，beta —— 不适合生产环境）。以本地控制与安全为先的个人 AI OS；通过 GEPA 优化器运行时实现自我学习。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentark-ai%2FAgentArk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [nanobot](https://github.com/HKUDS/nanobot) - 超轻量开源个人 AI Agent（41K+ stars）。2026 年 4 月版本（v0.1.5.x）新增线程级会话、自动压缩记忆、Dream 记忆巩固、DeepSeek-V4 支持与 Windows 支持。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2Fnanobot&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenBot](https://github.com/CopilotKit/OpenBot) - 🆕 🧪 **2026-08-17（alpha）**。CopilotKit 的自托管 AG-UI 同事平台：每个 Agent 有独立电脑（浏览器 / 文件 / 授权工具），知识权限默认拒绝，可盯屏接管。MIT，2.8K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FCopilotKit%2FOpenBot&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cumora](https://github.com/yetone/cumora) - 🆕 **2026-08-17**（邀请制预览）。人和 AI 同事同房的跨平台团队聊天：人格 / 记忆 / 主动开聊 / 邮件；云端 pod 或把本地 Claude Code / Codex / Grok Build / Cursor 当大脑。MIT，3.1K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fyetone%2Fcumora&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 📱 手机 Agent

*操控 Android / iOS 的 GUI Agent —— 桌面 Computer Use 之后的下一前沿。*

- [Mobile-Agent](https://github.com/X-PLUG/MobileAgent) - 🇨🇳 阿里多模态手机控制 Agent 家族（v1 → v3 + Mobile-Agent-E / V）。Android 基准 SOTA。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FX-PLUG%2FMobileAgent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AppAgent](https://github.com/TencentQQGYLab/AppAgent) - 💤 腾讯多模态智能体，通过点 / 滑操作 App。早期影响力实现；由 AppAgentX（2025-03）接续。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTencentQQGYLab%2FAppAgent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Apple Intelligence](https://www.apple.com/apple-intelligence/) - iOS / iPadOS / macOS 端侧 Agent 层。App Intents + 屏幕感知动作。
- [Samsung Galaxy AI](https://www.samsung.com/us/galaxy-ai/) - 集成于受支持 Galaxy 设备的 AI 功能；可用性因设备、语言、地区与网络要求而异。
- [Google Gemini for Android](https://gemini.google/) - 全面替换 Google Assistant，包括系统意图与 Workspace。
- [Magma](https://microsoft.github.io/Magma/) - 微软研究多模态 Agent 基座，统一 UI / 机器人 / 物理动作。
- [mobile-use](https://github.com/minitap-ai/mobile-use) - 开源框架（Apache-2.0，2.5K+ stars），让 AI Agent 像真人一样使用真实 Android / iOS 应用 —— UI 感知导航、自然语言控制。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fminitap-ai%2Fmobile-use&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [agent-device (Callstack)](https://github.com/callstack/agent-device) - **2026 年 2 月**。轻量、节省 token 的 CLI，用于自动化 iOS / Android 真机和模拟器。命令模型面向 AI Agent 与 CI 场景设计。MIT，2.6K+ stars。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcallstack%2Fagent-device&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [iOS 27 Siri AI（预览）](https://www.apple.com/ios/) - 🆕 **预览 2026 年 7 月（GA 秋捩2026）**。Apple 全面重建的 Siri，由 Apple Intelligence 驱动——跨应用上下文感知、自然语言 Shortcuts 自动化、iOS 27 预期支持多 AI 模型市场。开发者 beta 2026 年 7 月可用。
- [EU Android AI 开放裁定](https://ec.europa.eu/) - 🆕 **2026-07-17**。欧盟委命令谷歌向第三方 AI 助手开放更深层的 Android 权限——摄像头、麦克风、应用控制 API，为第三方移动 AI Agent 铺路。需在 2027 年8 月前在 Android 18 中实现。

---

## 🏢 企业级 Agent 平台

- [GPTBots.ai LoopAgent](https://www.gprbots.ai/) - 🆕 **2026-08-03**。面向企业级 AI Agent 的生产级执行引擎：沙箱代码执行、懒加载 Skills、带版本控制的 System Identity Prompt Diff、无缝人工接管上下文摘要。⚠️ 未核实（GlobeNewswire 公告；主 URL 未核实）。
- [Salesforce Agentforce 360](https://www.salesforce.com/agentforce/what-is-new/) - CRM 自主 Agent —— 销售 / 客服 / 营销。**Spring 2026 版**带来 Agentforce Builder（对话式 Agent 编辑）、Agent Script（确定性行为控制）、Agentforce Voice（接入 Amazon Connect / Five9 / Genesys / NiCE / Vonage + SIP）、基于新 Data 360 的 Intelligent Context。124 国客户报告约 85% 客户咨询自动化解决。
- [Microsoft Copilot Studio](https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio) - 企业 Copilot 与 Agent 构建。
- [Gemini Enterprise Agent Platform](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform) - **2026-04-22**（Google Cloud Next '26）。Vertex AI 进化为统一企业 Agent 中心。Gemini 3.1 Pro/Flash + Lyria 3 + 第三方模型（Claude Opus / Sonnet / Haiku）。
- [Google Vertex AI Agent Builder](https://cloud.google.com/products/agent-builder) - **2026 年 4 月更名** —— Vertex AI 的 Agent 构建能力现已并入 Gemini Enterprise Agent Platform（见上）：Agent Studio、Model Garden、Google Antigravity 编排。
- [Amazon Bedrock Agents](https://aws.amazon.com/bedrock/agents/) - 多步任务 Agent。
- [ServiceNow AI Agents](https://www.servicenow.com/products/ai-agents.html) - ITSM Agent + AI Control Tower。
- [ServiceNow Action Fabric (MCP Server)](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-opens-its-full-system-of-action-to-every-AI-Agent-in-the-enterprise/default.aspx) - 🆕 **2026-05-05**。ServiceNow 通过 GA 的 MCP Server 把其 AI 平台向任意 AI Agent（Claude、Copilot、自定义）开放，随每个 Now Assist 与 AI Native SKU 自带。每次调用都走 AI Control Tower，具备身份验证、权限范围、审计链；自带 OAuth、用量计费、角色级工具包。Anthropic（Claude Cowork）为首个设计合作伙伴。
- [IBM watsonx Orchestrate](https://www.ibm.com/products/watsonx-orchestrate) - 跨企业应用的 AI 助理平台。
- [Oracle AI Agents](https://www.oracle.com/artificial-intelligence/) - 与 Oracle Fusion Cloud ERP 集成。
- [Moveworks](https://www.moveworks.com/) - 跨系统企业 copilot。已被 ServiceNow 收购（2025-12-15 交割）。
- [UiPath Agentic Automation](https://www.uipath.com/) - 在 RPA 之上叠加 Agent 推理。
- [AgentX](https://www.agentx.so/) - 即插即用的企业 Agent 自动化。
- [Sistava](https://sistava.com) - ⚠️ 面向销售、营销、客服、招聘与运营的「按需 AI 员工」—— Agent 带持久记忆、直接在你的工具内工作；$19/月起。
- [Sema4.ai](https://sema4.ai/) - Python 优先 + 内置治理的企业 Agent 平台。
- [SAP Business AI Platform + Autonomous Suite](https://news.sap.com/2026/05/sap-sapphire-sap-unveils-autonomous-enterprise/) - 🆕 **SAP Sapphire 2026（2026-05-12）**。SAP 发布「自主企业」：以 SAP Business AI Platform 为统一 AI 底座；SAP Autonomous Suite 为财务、供应链、采购、HR 与 CX 的既有应用加入 Agent；Joule Studio 用于构建企业 Agent 与 Agentic 工作流；Joule Work UX；以及七个行业 AI 解决方案。Claude 是驱动 Joule Agent 的基础模型之一。
- [Microsoft Agent 365 + Microsoft 365 E7](https://techcommunity.microsoft.com/blog/agent-365-blog/microsoft-365-e7--agent365-from-where-you-are-to-enterprise-ai-at-scale/4519969) - **2026-05-01 GA**，5 月持续补充。以身份为中心的 AI Agent 控制面：独立 $15/用户/月，或 $99/用户/月随新推的 Microsoft 365 E7 "Frontier" 套套；5 月补丁加上了 AWS Bedrock + Google Cloud 注册表同步、Intune / Defender 预览策略，以及 Agent 专用 SASE。
- [OpenAI Guaranteed Capacity（算力年发）](https://openai.com/business/guaranteed-capacity/) - 🆕 **2026-05-19**。面向企业 AI 产品 / Agent / Workflow 的长期算力预订产品（可选 1/2/3 年期，期限越长折扣越高）—— 面向 GPT-5.5 级 Agent 的企业部署降低成本 / 产能不确定性，OpenAI 对 Anthropic Priority Tier 的产品化回应。
- [Bristol Myers Squibb ↔ Claude Enterprise](https://news.bms.com/news/corporate-financial/2026/Bristol-Myers-Squibb-Announces-Strategic-Agreement-with-Anthropic-to-Position-Claude-Enterprise-as-the-Shared-Intelligence-Platform-Across-Its-Global-Operations/default.aspx) - **2026-05-20**。BMS 将 Claude Enterprise 作为 30,000+ 员工的共享智能平台，嵌入药物发现 / 开发 / 交付的全链路。全球前 5 大药企中首个全公司级 Claude 部署。
- [Kore.ai Artemis Agent Platform](https://www.kore.ai/news/kore-ai-launches-artemis-the-new-generation-of-the-kore-ai-agent-platform-for-building-governing-and-optimizing-enterprise-ai) - 🆕 **2026 年 5 月 21 日（Azure 上线）**。AI 原生的企业级 Agent 平台，核心是新的 YAML 风格 **Agent Blueprint Language (ABL)**，用于声明式多 Agent 工作流。Kore.ai 对 Copilot Studio 与 Agentforce 的结构性挑战。
- [FPT Flezi Foundry](https://fptsoftware.com/newsroom/news-and-press-releases/press-release/fpt-launches-flezi-foundry-advancing-ai-augmented-delivery-for-global-enterprises) - FPT 交付平台，结合 Agentic Development Lifecycle（ADLC）和 Agentic Managed Services（AMS），并提供人工监督与服务治理。
- [Amazon Bedrock AgentCore Payments](https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-bedrock-agentcore-payments-preview/) - **2026-05-07（预览）**。AgentCore Agent 的托管支付 —— 通过 Coinbase（CDP 钱包、x402 Bazaar）与 Stripe（Privy 钱包）集成，自主为 API、MCP 服务器、Web 内容及其他 Agent 付费；支持消费限额与交易可观测性，覆盖四个 AWS 区域。
- [OutSystems Agentic Systems Platform](https://www.outsystems.com/) - **2026 年 6 月**。低代码巨头将其平台定位为“AI 原生”的 agentic 开发环境。提供开放式 AI 治理、自带模型、多 Agent 编排以及企业级合规，直接对标 Copilot Studio 与 Agentforce。
- [Databricks Genie One](https://www.databricks.com/blog/introducing-genie-one-genie-ontology-and-genie-agents) - **2026-06-16（Data + AI Summit）**。Databricks 推出的智能体「数据同事」，跨结构化与非结构化数据自动编排工作，依托全新 **Genie Ontology**（覆盖全组织的知识图谱）并由 Unity Catalog 治理；配套 Genie Agents，官方内部测试一次命中率 84.5%。
- [ZenseAI.AgentMesh（Zensar）](https://www.prnewswire.com/news-releases/zensar-technologies-launches-zenseaiagentmesh-to-accelerate-enterprise-ai-adoption-at-scale-302805437.html) - **2026-06-19**。Zensar 推出的企业级智能体 AI 平台，定位「面向 Agentic AI 的通用企业操作系统」，统一发现、构建、部署与治理自主 Agent；内置 80+ 预制行业与跨职能 Agent，宣称 6–8 周即可从试点走向生产。
- [Meta Business Agent](https://about.fb.com/news/2026/06/meta-business-agent/) - **2026-06-03（全球上线）**。Meta 面向 WhatsApp、Instagram 与 Messenger 推出的商业 AI Agent——回答咨询、推荐目录商品、预约到访、甄别销售线索并完成成交，必要时移交人工。已有 100 万+ 商家使用；**Meta Business Agent Platform** 让企业自定义 Agent 并接入 Shopify / Zendesk / Shopee —— 当前免费开通，付费订阅档即将推出。
- [Snyk Evo Agentic Development Security (ADS)](https://snyk.io/news/snyk-launches-evo-agentic-development-security/) - **2026 年 6 月**。专为自主 AI 编程 Agent 打造的安全与治理平台：实时治理 Agent 使用什么、做了什么以及生成的代码。
- [Cognizant Neuro AI + ServiceNow AI Agent](https://news.cognizant.com/2026-06-18-Cognizant-expands-cross-platform-agentic-AI-with-new-ServiceNow-AI-Agent-interoperability) - **2026 年 6 月**。跨平台企业编排：让 ServiceNow Agent 原生运行在 Cognizant 的 Multi-Agent Accelerator 中。
- [Talkdesk Agent Builder](https://www.cmswire.com/contact-center/customer-contact-week-2026-capturing-the-ai-announcements-in-contact-center-technology/) - **2026 年 6 月**。低代码构建器，让业务人员在数小时内（而非数周）将生产级 AI Agent 部署到联络中心。
- [HelloTwin Digital Authority](https://siliconangle.com/2026/06/24/hellotwin-launches-digital-authority-bring-governed-ai-agents-enterprise/) - **2026 年 6 月**。作为单一可审计事实来源的 AI 数字分身，以清晰边界治理 Agentic 工作流。
- [Hellomatik](https://hellomatik.com) - 💰 ⚠️ **Freemium / 未验证**。将企业知识库转化为能够在 WhatsApp、邮件和网页全渠道解答、销售和预订的 AI Agent 平台。支持集成 Shopify、Stripe、Sage。对话转化率自称达 25–30%。
- [OpenAI Presence](https://openai.com/) - 🆕 **2026-07-22**。OpenAI 为企业推出的 Agent 部署平台——支持企业大规模部署 AI Agent，面向客服和运营场景。自称 75% 的电话客服交互无需人工升级。

---

## 📊 Agent 评估与可观测性

- [AgentBench](https://github.com/THUDM/AgentBench) - 评估 LLM 作为 Agent 表现的多维 benchmark。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTHUDM%2FAgentBench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [PerspectiveGap](https://github.com/WhymustIhaveaname/PerspectiveGap) - 🆕 **2026（arXiv 2606.08878）**。首个**多 Agent 编排提示词写作**基准 —— 110 个场景，横跨 10 种通信拓扑（链式、星型、树型、网格等），测试大模型能否撰写让子 Agent 有效协作的提示词。衡量角色碎片化分配、信息泄漏率和拓扑感知提示设计。主要发现：33 个模型平均综合通过率仅 17.2%；GPT-5.5 领先 62.0%。MIT 开源基准数据+评测脚本；已合并进 OpenCompass 和 Inspect Evals（2026 年6月，角色碎片分配+自由形式提示词写作任务）。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FWhymustIhaveaname%2FPerspectiveGap&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ClawBench](https://github.com/TIGER-AI-Lab/ClawBench) - 🆕 面向浏览器 / Computer-Use Agent 的真实线上基准 —— **15 个类别、144 个真实平台上的 153 项日常线上任务**（下单购买、预约、投递职位申请等），跑在*生产环境*网站上而不是离线沙箱里。拦截层会捕获并阻断最后的提交请求，因此不会在现实世界产生真实副作用；随后用两阶段评分（HTTP 拦截 → LLM judge）判断 Agent 提交的内容是否正确。主要结论：前沿模型只能完成其中一小部分 —— Claude Sonnet 4.6 仅 33.3%。[论文](https://arxiv.org/abs/2604.08523) · [排行榜](https://claw-bench.com) ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTIGER-AI-Lab%2FClawBench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangSmith](https://www.langchain.com/langsmith) - LangChain 的官方调试 / 评测 / 监控平台。
- [Helicone](https://github.com/Helicone/helicone) - 开源 LLM 可观测性。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHelicone%2Fhelicone&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Braintrust](https://www.braintrust.dev/) - 企业级 AI 产品构建栈——评估、提示词 playground、日志一体化。SDK：[braintrust-sdk-javascript](https://github.com/braintrustdata/braintrust-sdk-javascript) 与 braintrust-sdk-python（由 braintrust-sdk 拆分/更名）。
- [Arize Phoenix](https://github.com/Arize-ai/phoenix) - 开源 LLM 可观测性 + 评测。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FArize-ai%2Fphoenix&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Langfuse](https://github.com/langfuse/langfuse) - 可自行托管的 LLM 可观测性、评估与提示词管理平台；v4 版本已发布; [v4.32.0](https://github.com/langfuse/langfuse/releases/tag/v4.32.0) (2026-09-08).
- [OpenLLMetry](https://github.com/traceloop/openllmetry) - 基于 OpenTelemetry 的开源 LLM 可观测性方案。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftraceloop%2Fopenllmetry&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Weights & Biases Weave](https://github.com/wandb/weave) - 用于开发、评估与监控 AI 应用的工具包。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fwandb%2Fweave&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SWE-bench](https://github.com/SWE-bench/SWE-bench) - 评估 LLM 在真实软件工程问题上能力的 benchmark。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSWE-bench%2FSWE-bench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Terminal-Bench](https://www.tbench.ai/) - 面向终端编码 Agent 的评估 benchmark。由 Harbor Framework 维护。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fharbor-framework%2Fterminal-bench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Harbor](https://github.com/harbor-framework/harbor) - 🆕 大规模评估与优化 Agent 和 LLM 的框架 —— 在数千个云沙箱中运行 Terminal-Bench 2.x 及自定义基准、生成 RL rollout；Stanford × Laude Institute 合作项目。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fharbor-framework%2Fharbor&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Arena（前 LMArena / LMSYS Chatbot Arena）](https://arena.ai/) - 众包人类偏好投票 AI 基准；榜单现覆盖 LLM、图像生成与代码模型。LMSYS → LMArena（2025）→ Arena（2026）。
- [Patronus AI](https://www.patronus.ai/) - 💰 LLM 评测/红队公司，现定位为构建数字世界模型与 Agent 训练仿真基础设施的前沿研究实验室（$50M B 轮）；研究成果包括 Lynx、FinanceBench 与 GLIDER。
- [DeepEval](https://github.com/confident-ai/deepeval) - Pytest 风格的 LLM 评测框架，14+ 内置指标。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fconfident-ai%2Fdeepeval&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agenta](https://github.com/agenta-ai/agenta) - 一体化开源 LLMOps。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagenta-ai%2Fagenta&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangSmith SDK](https://github.com/langchain-ai/langsmith-sdk) - 客户端 SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangsmith-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AutoEvals](https://github.com/braintrustdata/autoevals) - 独立的最佳实践评测器库（事实性 / JSON 有效性 / 语义相似度等）。Braintrust 出品。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbraintrustdata%2Fautoevals&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [BenchClaw](https://github.com/Agnuxo1/benchclaw) - ⚠️ **Unverified**。自称多维度 Agent 评测。8 个 awesome 列表 7 个拒收，2 star 单维护者。**仅作可见性收录**。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAgnuxo1%2Fbenchclaw&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [PromptEden](https://www.prompteden.com) - ⚠️ **Unverified**。商业 SaaS：监控 ChatGPT / Claude / Gemini / Perplexity / Copilot / Grok 如何描述你的品牌。同款 PR 同日投了 10 个 awesome 列表。**仅作可见性收录**。
- [Laminar](https://github.com/lmnr-ai/lmnr) - 专为长跑 AI Agent 设计的开源可观测性平台（Apache-2.0，YC S24）。OpenTelemetry 原生，transcript view、Signals、SQL 跨 traces 查询、浏览器 Agent 会话回放。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flmnr-ai%2Flmnr&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangSmith Engine](https://www.langchain.com/blog/interrupt-2026-overview) - **2026 年 5 月（Interrupt 2026）**。LangSmith 的自主失败诊断层——将生产失败聚类为优先级问题，结合 traces 与代码定位根因，给出可供人类审阅的修复建议。与新发的 SmithDB（Rust + DataFusion 支持的 Agent 观测数据库）配套。
- [AgentSight](https://github.com/eunomia-bpf/AgentSight) - 零插桩 eBPF Agent 可观测性——无需修改 Agent 代码，在 syscall 层捕获进程、文件、网络全栈行为轨迹，实现完整行为分析。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Feunomia-bpf%2FAgentSight&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Prismix](https://prismix.dev) - 实时监控 77+ AI 服务（OpenAI、Anthropic、Cursor 等）的状态，提供状态徽章与 API；AI 新闻聚合器（来自 71+ 信息源）；MCP 服务器目录（收录 80+ 服务器）。免费，无需注册。
- [Ceros (by Beyond Identity)](https://www.prnewswire.com/news-releases/ceros-launches-providing-unified-identity-observability-and-governance-for-every-ai-agent-and-workflow-302800721.html) - 🆕 **2026-06-16**。Agentic AI 信任层：统一身份、可观测性与治理 —— 发现/清点、运行时策略执行、审计链。（与同名互动内容公司无关。）
- [Zoom Agent Performance Suite](https://news.zoom.com/introducing-agent-architect-and-agent-performance-suite-for-zoom-virtual-agent/) - **2026-06**。用于在面向客户的场景中测试、验证并优化自主 Agent 表现的专用套件。
- [AgentOps](https://github.com/AgentOps-AI/agentops) - 🆕 Agent 监控、合规与测试工具包，带会话回放；提供 MCP server，对任何接入 MCP 的 Agent 实现零配置可观测；5K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAgentOps-AI%2Fagentops&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenTelemetry GenAI Semantic Conventions](https://github.com/open-telemetry/semantic-conventions-genai) - 面向 GenAI 客户端、Agent、工具调用与 MCP 的标准化 span / 指标 / 事件 —— 在任意 OTel 后端（Arize、Langfuse、Helicone、Jaeger 等）实现厂商中立的追踪。已从核心 semconv 仓库移入专门的 GenAI 仓库。
- [Tracecat](https://github.com/TracecatHQ/tracecat) - 🆕 开源安全自动化平台，为 SOC 工作流捕获完整 Agent trace —— 把 AI Agent 接入检测、富化与响应流水线。AGPL-3.0（含企业版例外条款）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTracecatHQ%2Ftracecat&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Langfuse v4](https://github.com/langfuse/langfuse/releases/tag/v4.0.0) - 🆕 **v4.0.0，2026-07-29**。这个可自托管的 LLM 可观测性栈的大版本更新：支持对输入 / 输出 / 元数据做全文检索，新增筛选搜索栏、监控与告警，并重写了 Observations API v2 / Metrics API v2，官方称最高快 **165 倍**。
- [AcruxCore](https://github.com/AcruxCore/AcruxCore) - ⚠️ **未验证**（新仓库，单一维护者，暂无第三方采用）。可自托管或 SaaS 的 LLM-ops 平台，包含 Prompt 版本管理、AI 网关、链路追踪、工具目录与评估运行。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAcruxCore%2FAcruxCore&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AOTrust](https://github.com/GitSerge-crypto/aotrust-skills) - ⚠️ **未验证**（单维护者，独立采用及服务保证未核实）。为文件哈希和时间戳提供回执的服务，公开 MIT 规范、离线解析器、MCP 接口和 GitHub Action；签名回执不证明文件内容正确。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FGitSerge-crypto%2Faotrust-skills&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🔬 AI 研究工具

- [Hugging Face](https://huggingface.co/) - AI 社区平台——汇集模型、数据集与 Spaces，是 ML 研究的事实标准枢纽。
- [Hugging Face Transformers](https://github.com/huggingface/transformers) - 用于模型定义、训练与推理的库；5.16.1 新增 GLM-5.3-Flash 支持; [v5.16.1](https://github.com/huggingface/transformers/releases/tag/v5.16.1) (2026-08-26).
- [vLLM](https://github.com/vllm-project/vllm) - LLM 推理服务引擎；0.28.0 包含 Kimi-K3 和 DeepSeek V4 执行优化; [v0.28.0](https://github.com/vllm-project/vllm/releases/tag/v0.28.0) (2026-08-26).
- [Ollama](https://github.com/ollama/ollama) - 本地跑 LLM 的最简单方法。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Follama%2Follama&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LM Studio](https://lmstudio.ai/) - 桌面本地 LLM GUI，多提供商。
- [SGLang](https://github.com/sgl-project/sglang) - 模型推理服务框架；0.5.19 新增 Qwen3.8 等模型集成; [v0.5.19](https://github.com/sgl-project/sglang/releases/tag/v0.5.19) (2026-09-05).
- [llama.cpp](https://github.com/ggml-org/llama.cpp) - C/C++ 高性能 LLM 推理。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fggml-org%2Fllama.cpp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MLX](https://github.com/ml-explore/mlx) - Apple Silicon 上的机器学习框架。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fml-explore%2Fmlx&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Unsloth](https://github.com/unslothai/unsloth) - 用于模型训练、微调和强化学习的开源工具；性能取决于具体工作负载。
- [OpenRouter](https://openrouter.ai/) - 一个 API 统一访问 70+ 提供商的 400+ AI 模型。
- [Weights & Biases](https://wandb.ai/) - ML 实验跟踪 + 模型管理。
- [Label Studio](https://github.com/HumanSignal/label-studio) - 多类型数据标注平台。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHumanSignal%2Flabel-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SmithDB](https://www.langchain.com/blog/interrupt-2026-overview) - **2026 年 5 月（Interrupt 2026）**。LangChain 自研的 Agent 观测数据库。Rust 写在 Apache DataFusion + Vortex 之上，带对象存储后端——为 Agent trace 的容量与访问模式量身设计。
- [Strands Evals（AWS）](https://github.com/strands-agents/evals) - 🆕 AWS 开源的 Agent 工作流评估框架——Case/Experiment/Evaluator 结构，支持 LLM-as-judge；Strands Agents SDK 的配套工具。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstrands-agents%2Fevals&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [DSPy](https://github.com/stanfordnlp/dspy) - 编程代替 prompt 工程。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstanfordnlp%2Fdspy&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Elicit](https://elicit.com/) - 🆕 面向文献综述与系统性综述的 AI 研究助手，覆盖超大规模学术论文库。**2026-07-15**：上线公开的 [API 与 MCP server](https://elicit.com/blog/elicit-api)，让 Agent 和工作流可以直接调用它的检索与综述能力。**2026-07-17**：发布论文检索评测，称在 BioASQ 上优于另外五个检索系统（厂商自测）。
- [IdeaHunter](https://ideahunter.today) - 面向独立创业者的 AI 研究工具——基于公开信号、用户痛点、市场证据、MVP 范围和变现路径，挖掘有真实需求支撑的 App / micro-SaaS 创意。Freemium。

---

## 📚 学习资源

### 论文

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) - 定义 ReAct 范式的里程碑论文。
- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) - LLM 学会使用外部工具。
- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) - 使用 LLM 创建可信人类行为 Agent。
- [LLM-based Autonomous Agents Survey](https://arxiv.org/abs/2308.11432) - 中人大 LLM 自主 Agent 综述。
- [The Rise and Potential of LLM Based Agents](https://arxiv.org/abs/2309.07864) - LLM Agent 发展与潜力。
- [Agent Hospital](https://arxiv.org/abs/2405.02957) - 模拟可演化医疗 Agent 的医院环境。
- [ComBodied Agents: a New Paradigm of Human-Centric Agentic AI](https://arxiv.org/abs/2608.10915) - 🆕 **2026-08-11**。以人为中心的 Agent 范式，结合多模态感知、纵向记忆与追踪人类状态轨迹的个人世界模型。2026-08-12 登顶 Hugging Face 每日论文榜。
- [Co-Evolution in Agentic Systems: Toward Self-Directed Evolution Beyond Human Design](https://arxiv.org/abs/2608.10299) - 🆕 **2026-08-10**。综述 Agent 系统中 Agent-Agent / Agent-环境的共同演化与自主导向的进化机制。

### 课程与教程

- [DeepLearning.AI — AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) - 用 LangGraph 构建 Agent 的短课程。
- [DeepLearning.AI — Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/) - 多 Agent 系统构建课程。
- [DeepLearning.AI — A2A Protocol](https://www.deeplearning.ai/short-courses/a2a-the-agent2agent-protocol/) - 关于 Google Agent-to-Agent 协议的免费课程。
- [LangChain Academy](https://academy.langchain.com/) - LangChain 官方课程（包含 LangGraph）。
- [DeepLearning.AI Short Courses](https://www.deeplearning.ai/short-courses/) - 涵盖主要框架 / 协议的 AI 短课。
- [Hugging Face — Building AI Agents](https://huggingface.co/learn/agents-course/) - 用开源工具构建 AI Agent 的开放课程。
- [LLM Agents MOOC (Berkeley)](https://llmagents-learning.org/) - UC Berkeley 的 LLM Agent 课程（根站点跳转到最新一期）。
- [Microsoft Agent Framework Docs](https://learn.microsoft.com/en-us/agent-framework/) - 微软统一 Agent 框架官方文档。
- [Hugging Face Agents Course](https://github.com/huggingface/agents-course) - 5 单元免费课程（smolagents / LangGraph / Llama-Index）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhuggingface%2Fagents-course&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Anthropic Cookbook](https://github.com/anthropics/claude-cookbooks) - 官方调工具、Computer Use、Agent 模式、Claude Code 示例本。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fanthropics%2Fclaude-cookbooks&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Google Gemini Cookbook](https://github.com/google-gemini/cookbook) - Gemini API 示例：grounding / function calling / 多模态 / live audio。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle-gemini%2Fcookbook&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LLM Course (Maxime Labonne)](https://github.com/mlabonne/llm-course) - LLM 从入门到微调的完整课程 + Colab。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmlabonne%2Fllm-course&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Anthropic Courses](https://github.com/anthropics/courses) - Anthropic 官方 prompt engineering / 评测 / 工具调用课程。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fanthropics%2Fcourses&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hugging Face Robotics Course](https://huggingface.co/learn/robotics-course/unit0/1) - 免费课程，结合经典机器人学、学习型策略、LeRobot、真实机器人数据集和实践练习。

### 精选列表

- [awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) - 💤 **Stale**（2025-02 起无更新）。E2B 出品。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fe2b-dev%2Fawesome-ai-agents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [awesome-llm-agents](https://github.com/kaushikb11/awesome-llm-agents) - LLM Agent 资源。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fkaushikb11%2Fawesome-llm-agents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - MCP server 实现精选。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fpunkpeye%2Fawesome-mcp-servers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [awesome-ai-agent-papers (VoltAgent)](https://github.com/VoltAgent/awesome-ai-agent-papers) - 2026 年 AI Agent 研究论文精选——覆盖 Agent 工程、记忆、评测、工作流、自主系统。每周从 arXiv 更新。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FVoltAgent%2Fawesome-ai-agent-papers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [awesome-cli-coding-agents](https://github.com/bradAGI/awesome-cli-coding-agents) - 终端原生 AI 编程 Agent + 编排 harness 精选——开源工具（Pi / OpenCode / Aider / Goose）、平台 Agent（Claude Code / Codex / Gemini CLI）、并行运行器、自主循环。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FbradAGI%2Fawesome-cli-coding-agents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🇨🇳 中国 AI 生态

*中国大陆团队主导或主要面向中文市场的重要项目。列出是因为中国技术栈越来越形成独立生态，有自己的框架、模型、开发者文化。*

*中国友出品的基础模型（Qwen / DeepSeek / GLM / Doubao / Kimi / Hunyuan / ERNIE）已直接列在 [🧠 基础大模型](#-基础大模型-2026) 下。*

### Agent 平台与框架

- [Dify](https://github.com/langgenius/dify) - 开源 LLM 应用开发平台 + 可视化 Agent 构建。中文技术圈主流低代码 Agent 画布。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flanggenius%2Fdify&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LobeHub](https://github.com/lobehub/lobehub) - Agent 管理平台（前 Lobe Chat）—— 把 Agent 组织为 7×24 运转，支持对你的 AI 团队进行"招聘/排班/汇报"。最高 star 的 TypeScript AI 项目之一（80K+ stars）。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flobehub%2Flobehub&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Coze Loop](https://github.com/coze-dev/coze-loop) - 🆕 字节 Coze 团队开源的 Agent 优化平台。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-loop&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentScope](https://github.com/agentscope-ai/agentscope) - 阿里 ModelScope 多 Agent 框架 + 可视化调试 + 分布式执行。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentscope-ai%2Fagentscope&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Bisheng](https://github.com/dataelement/bisheng) - 开源企业级 LLM DevOps：工作流 / RAG / Agent / 微调 / 评测。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdataelement%2Fbisheng&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) - SOP 角色多 Agent（PM / 架构师 / 工程师）。现由 FoundationAgents 组织维护。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FFoundationAgents%2FMetaGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### RAG / 知识

- [FastGPT](https://github.com/labring/FastGPT) - 知识库优先的 LLM 平台：数据摄入 / RAG / 可视化工作流。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flabring%2FFastGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [QAnything](https://github.com/netease-youdao/QAnything) - 💤 网易有道出品，针对任意本地文档的问答引擎。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fnetease-youdao%2FQAnything&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAGFlow](https://github.com/infiniflow/ragflow) - 深度文档理解的 RAG 引擎 —— 扫描 PDF 、表格、图表处理能力强。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Finfiniflow%2Fragflow&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LightRAG](https://github.com/HKUDS/LightRAG) - 港大 HKUDS 轻量图式 RAG。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2FLightRAG&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### 个人与生产力

- [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) - 开源 Notion 替代品 + AI 工作区。AGPL-3.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAppFlowy-IO%2FAppFlowy&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Manus AI](https://manus.im/) - Butterfly Effect 出品的通用自主 Agent（中国团队创立，后迁往新加坡）。Meta 于 2025-12-30 宣布以约 $2B 收购，但**[中国发改委于 2026-04-27 禁止了该收购](https://www.theguardian.com/world/2026/apr/27/china-blocks-meta-takeover-manus-ai-agent-developer)**，。✅ **2026-08-11 尘埃落定**：Manus [宣布将恢复作为独立公司运营](https://www.cnbc.com/2026/08/11/manus-china-meta-acquisition.html)，Meta 按北京的命令拆分该收购；用户数据删除流程已启动。
- [Coze (扣子)](https://www.coze.cn/) - 字节无代码 Agent 构建。国内面向消费者；国际版为 coze.com。
- [Qwen App（千问）](https://www.qwen.ai/) - 阿里大众消费者 Agent（由通义千问更名），集成在淘宝 / 钉钉 / 夸克。
- [Doubao Agents](https://www.doubao.com/) - 字节豆包模型上的主力消费者助手。
- [Resume Roaster](https://resume.roastlabai.com/) - AI 简历诊断工具，带 ATS 关键词缺口分析。上传简历和职位描述，获取具体的 AI 反馈，申请前先知道该改哪里。面向想在竞争激烈的求职市场里占优势的求职者。

### 开发者工具

- [Trae](https://www.trae.ai/) - 字节跳动的 AI IDE 与 "10x AI 编程工程师" —— 中国对 Cursor 最高调的挑战者。
- [CoderPlan](https://coderplan.ai/) - 面向中国开发者的统一 LLM API 网关（Claude / OpenAI / Gemini，一行配置支持 Claude Code），按量付费，支持支付宝 & 微信支付。
- [Cherry Studio](https://github.com/CherryHQ/cherry-studio) - 中文开发者圈装机量最高的开源桌面 LLM 客户端，多提供商 + 知识库。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FCherryHQ%2Fcherry-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code) - **2026 年 6 月 6 日**。Moonshot AI 的终端编程 Agent（MIT，TypeScript）——内置 coder / explore / plan 子 Agent 在隔离上下文里跑，`/mcp-config` 对话式 MCP 配置。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FMoonshotAI%2Fkimi-code&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Qwen Code](https://github.com/QwenLM/qwen-code) - 阿里 Qwen 团队的开源终端编程 Agent —— Agent 团队、自动记忆、IDE 集成、多提供商（OpenAI / Anthropic / Gemini / Qwen）。26K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FQwenLM%2Fqwen-code&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Coze Studio](https://github.com/coze-dev/coze-studio) - 字节 Coze.com 的开源对照版——一体化可视化 Agent 构建器，自带调试与部署工具。Apache-2.0，20K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ScienceOne 100 / 磐石100](https://english.cas.cn/newsroom/cas-in-media/202604/t20260429_1158251.shtml) - 中科院科研推理 Agent 系统，50+ 中科院研究所、100+ 科研场景、带 2000+ 研究工具。

### 2026 年新平台模型

- [Kimi K3](https://huggingface.co/moonshotai/Kimi-K3) - 开放权重多模态MoE；采用自定义Kimi K3 License。
- [Qwen3.8 family](https://huggingface.co/Qwen/Qwen3.8-27B) - 27B采用Apache-2.0；完整Max与Flash-Next检查点另有Qwen许可条款。
- [GLM-5.3 / GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3) - 均已提供可下载权重；GLM-5.3为自定义许可，Flash为MIT。
- [DeepSeek V4](https://api-docs.deepseek.com/quick_start/pricing/) - 当前API检查点为Pro-0813和Flash-0731；Flash Vision为实验版。
- [Seed 2.1](https://seed.bytedance.com/en/seed2_1) - 字节跳动通用Agent与编程模型；访问方式以官方模型页面为准。

---

## 📝 横向对比表

*2026 年最常见的“该选哪个？”决策矩阵。*

### 🏗️ Agent 框架（开源向）

| 工具 | 语言 | 用途 | 许可 / 条款 |
| --- | --- | --- | --- |
| [LangGraph](https://github.com/langchain-ai/langgraph) | Python / JS | 有状态图编排、持久化、中断 | MIT |
| [CrewAI](https://github.com/crewAIInc/crewAI) | Python | 智能体团队与事件驱动 Flows | MIT |
| [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | Python / .NET | 智能体与图工作流；Microsoft AutoGen 的后续开发方向 | MIT |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | Python / TypeScript | 交接、护栏、会话、追踪 | MIT |
| [Mastra](https://github.com/mastra-ai/mastra) | TypeScript | 智能体、工作流、记忆、可观测性 | 核心 Apache-2.0；企业代码例外 |
| [Google ADK](https://github.com/google/adk-python) | Python | 工具、工作流、多智能体组合 | Apache-2.0 |
| [DSPy](https://github.com/stanfordnlp/dspy) | Python | 类型化模型程序与优化器 | MIT |
| [Agno](https://github.com/agno-agi/agno) | Python | 智能体、团队、工作流、知识 | Apache-2.0 |

---

### 🧪 沙箱（运行 Agent 生成代码）

| 工具 | 用途 | 部署 / 状态 | 许可 / 条款 |
| --- | --- | --- | --- |
| [E2B](https://github.com/e2b-dev/E2B) | 沙箱代码执行 | 托管云；基础设施另有代码库 | Apache-2.0 |
| [Daytona](https://github.com/daytonaio/daytona) | 智能体开发与执行环境 | 托管服务；公开核心代码停止维护 | 历史快照有独立许可；当前核心私有 |
| [Modal](https://modal.com/) | 无服务器函数、GPU、沙箱 | 托管云 | 商业服务 |
| [Microsandbox](https://github.com/superradcompany/microsandbox) | 可编程本地 microVM | 自行托管 | Apache-2.0 |
| [SandboxFusion](https://github.com/bytedance/SandboxFusion) | 多语言代码评估 | 自行托管；显式配置隔离 | Apache-2.0 |
| [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | 沙箱 API、SDK、网络控制 | Docker / Kubernetes；可选隔离运行时 | Apache-2.0 |

不列统一冷启动数值：结果取决于镜像、区域、资源与缓存状态。

---

### 🌐 浏览器 Agent 栈

| 工具 | 用途 | 部署 / 状态 | 许可 / 条款 |
| --- | --- | --- | --- |
| [Browser Use](https://github.com/browser-use/browser-use) | 模型驱动浏览器自动化 | Python 库；可选云服务 | MIT |
| [Stagehand](https://github.com/browserbase/stagehand) | act / extract / observe | 本地浏览器或 Browserbase | MIT |
| [Steel Browser](https://github.com/steel-dev/steel-browser) | 浏览器会话与自动化 API | 自行托管或云服务 | Apache-2.0 |
| [Skyvern](https://github.com/Skyvern-AI/skyvern) | 基于视觉的浏览器工作流 | 自行托管或云服务 | AGPL-3.0 |
| [AgentQL](https://github.com/tinyfish-io/agentql) | 语义网页提取与自动化 | SDK 配合托管 API | SDK 为 MIT；服务另有条款 |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | 通过 MCP 使用浏览器无障碍快照与操作 | 本地 MCP 服务 | Apache-2.0 |

---

### 📊 评估与可观测性

| 工具 | 用途 | 部署 / 状态 | 许可 / 条款 |
| --- | --- | --- | --- |
| [Langfuse](https://github.com/langfuse/langfuse) | 追踪、评估、提示词管理 | 云服务 / 自行托管 | 核心 MIT；企业代码例外 |
| [Helicone](https://github.com/Helicone/helicone) | LLM 网关与可观测性 | 云服务 / 自行托管 | Apache-2.0 |
| [Arize Phoenix](https://github.com/Arize-ai/phoenix) | OpenTelemetry/OpenInference 追踪与评估 | 自行托管 / 托管选项 | Elastic-2.0 |
| [LangSmith](https://docs.langchain.com/langsmith/self-hosted) | 追踪、评估、提示词、部署 | 云服务；自行托管为 Enterprise 附加项 | 商业许可 |
| [Braintrust](https://www.braintrust.dev/docs/admin/self-hosting/architecture) | 实验、数据集、追踪、评估 | 数据平面可自行托管；控制平面为 SaaS | 商业平台 |
| [DeepEval](https://github.com/confident-ai/deepeval) | 测试驱动 LLM 评估库 | 本地库；可选托管平台 | Apache-2.0 |
| [Agenta](https://github.com/agenta-ai/agenta) | 提示词试验、评估、可观测性 | 云服务 / 自行托管 | 核心 MIT；企业代码例外 |
| [OpenLLMetry](https://github.com/traceloop/openllmetry) | OpenTelemetry 插桩 | 库；需配置遥测后端 | Apache-2.0 |

---

### 💻 编程 Agent —— 头部选择

| 工具 | 使用方式 | 用途 | 成本方式 / 可用性 |
| --- | --- | --- | --- |
| [Claude Code](https://code.claude.com/docs/en/overview) | CLI / IDE | 仓库探索、编辑、工具使用 | 付费计划或 API 计费 |
| [Codex CLI](https://github.com/openai/codex) | CLI | OpenAI 编程智能体运行时 | 客户端开源；模型访问另行计费 |
| [Cursor](https://www.cursor.com/) | IDE / CLI | 智能体辅助开发 | 专有软件；受计划额度限制 |
| [Cline](https://github.com/cline/cline) | IDE | 带操作审批的编程智能体 | 客户端开源；模型提供商收费 |
| [Aider](https://github.com/Aider-AI/aider) | CLI | 理解 Git 工作流的结对编程 | 客户端开源；模型提供商收费 |
| [Devin](https://devin.ai/) | Cloud / Desktop | 委派软件工程任务 | 商业服务 |
| [OpenHands](https://github.com/OpenHands/OpenHands) | 自行托管 / 云服务 | 软件工程智能体平台 | 核心代码可用；算力与模型成本另计 |

基准结果必须注明模型、运行框架、数据集版本和评估日期，不能视为编辑器或 CLI 的固定属性。

---

### 💰 基础大模型 — API 价格与上下文窗口

*2026-09-08核验官方标准 API 价格；单位为美元/百万 token，不含工具、税费及缓存写入。上下文不等于最大输入额度。*

| 模型 | 供应商 | 上下文 | 最大输出 | 输入 $/1M | 输出 $/1M | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| [GPT-6 Astra](https://developers.openai.com/api/docs/models/gpt-6-astra) | OpenAI | 1.05M | 128K | $10.00 | $50.00 | 仅部分组织开放；尚未 GA |
| [GPT-5.6 Sol](https://developers.openai.com/api/docs/pricing) | OpenAI | 1.05M | 128K | $4.00 | $20.00 | 通用 Agent 任务 |
| [GPT-5.6 Terra](https://developers.openai.com/api/docs/pricing) | OpenAI | 1.05M | 128K | $2.00 | $12.00 | 均衡生产层级 |
| [GPT-5.6 Luna](https://developers.openai.com/api/docs/pricing) | OpenAI | 1.05M | 128K | $0.20 | $1.20 | 吞吐与成本 |
| [Claude Fable 5.1](https://platform.claude.com/docs/en/about-claude/pricing) | Anthropic | 1M | 128K | $10.00 | $50.00 | 缓存读取 $0.25/M |
| [Claude Opus 5](https://platform.claude.com/docs/en/about-claude/pricing) | Anthropic | 1M | 128K | $5.00 | $25.00 | Opus 层级 |
| [Claude Sonnet 5](https://platform.claude.com/docs/en/about-claude/pricing) | Anthropic | 1M | 128K | $2.00 | $10.00 | 标准价；9月不涨价 |
| [Claude Haiku 4.5](https://platform.claude.com/docs/en/models/overview) | Anthropic | 200K | 64K | $1.00 | $5.00 | 延迟敏感任务 |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/pricing) | Google | 1,048,576 | 65,536 | $0.75 | $3.75 | 优惠价至2026-12-31 |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/pricing) | Google | 1M | 65,536 | $2.00 | $12.00 | 提示词≤200K的基础价格 |
| [DeepSeek V4-Pro](https://api-docs.deepseek.com/quick_start/pricing/) | DeepSeek | 1M | 384K | $1.32 / $0.66 | $3.96 / $1.98 | 高峰/低谷；未命中缓存 |
| [DeepSeek V4-Flash](https://api-docs.deepseek.com/quick_start/pricing/) | DeepSeek | 1M | 384K | $0.44 / $0.22 | $1.32 / $0.66 | 高峰/低谷；未命中缓存 |
| [Grok 4.6](https://x.ai/news/grok-4-6) | SpaceXAI | 500K | — | $2.00 | $6.00 | Fast 层级价格2倍 |

表中 OpenAI 模型的提示词超过272K时，输入/缓存按2倍、输出按1.5倍计费；Astra输入上限922K。Gemini Pro超过200K采用不同长上下文价格。Gemini 3.8 Flash于2027-01-01调整为$1.50/$7.50。DeepSeek高峰时段为UTC 01:00–04:00及06:00–10:00。缓存、批处理、区域与服务层级附加规则请查看链接中的官方定价。

---

### 💻 基础大模型 — 本地部署

*2026-09-08核验许可和权重可用性。存储量仅为计算示例：公开总参数×0.5字节，单位十进制GB；不是实测Q4文件大小，也不是最低显存要求。*

| 模型 | 参数规模 | 理想4位权重存储量 | 官方权重 | 许可 |
| --- | --- | --- | --- | --- |
| Gemma 4 E4B | ~8B stored | ~4 GB | [google/gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it) | Apache-2.0 |
| Gemma 4 12B | 12B | ~6 GB | [google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it) | Apache-2.0 |
| Phi-4 | 14B | ~7 GB | [microsoft/phi-4](https://huggingface.co/microsoft/phi-4) | MIT |
| Gemma 4 26B A4B | 26B / 4B active | ~13 GB | [google/gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it) | Apache-2.0 |
| Qwen3.8-27B | 27B | ~13.5 GB | [Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) | Apache-2.0 |
| Muse Glimmer 30B | 30B | ~15 GB | [meta-models/Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B) | Apache-2.0 |
| Gemma 4 31B | 31B | ~15.5 GB | [google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it) | Apache-2.0 |
| Qwen3.6-35B-A3B | 35B / 3B active | ~17.5 GB | [Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) | Apache-2.0 |
| Llama 3.3 70B | 70B | ~35 GB | [meta-llama/Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) | Llama Community |
| Mistral Small 4 | 119B / 6B active | ~59.5 GB | [mistralai/Mistral-Small-4-119B-2603](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603) | Apache-2.0 |
| Qwen3.8-Flash-Next | 125B + 51B tables + 4B MTP | ~90 GB | [Qwen/Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) | Qwen Community 1.0 |
| Qwen3 235B A22B | 235B / 22B active | ~117.5 GB | [Qwen/Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B) | Apache-2.0 |
| Inkling-Small | 276B / 12B active | ~138 GB | [thinkingmachines/Inkling-Small](https://huggingface.co/thinkingmachines/Inkling-Small) | Apache-2.0 |
| DeepSeek V4-Flash | 284B / 13B active | ~142 GB | [deepseek-ai/DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash) | MIT |
| GLM-5.3-Flash | 320B / 18B active | ~160 GB | [zai-org/GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash) | MIT |
| MiniMax-M3 | MoE | — | [MiniMaxAI/MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3) | MiniMax Community |
| GLM-5.3 | MoE | — | [zai-org/GLM-5.3](https://huggingface.co/zai-org/GLM-5.3) | GLM-5.3 License |
| Inkling | 975B / 41B active | ~487.5 GB | [thinkingmachines/Inkling](https://huggingface.co/thinkingmachines/Inkling) | Apache-2.0 |
| DeepSeek V4-Pro | 1.6T / 49B active | ~800 GB | [deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | MIT |
| Kimi K3 | 2.8T / 104B active | ~1,400 GB | [moonshotai/Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3) | Kimi K3 License |

还需为量化尺度、未量化张量、运行时缓冲及KV缓存预留空间。MoE激活参数代表计算量，不等于全部权重占用。CPU卸载会改变显存驻留与吞吐，须按确切检查点、后端、量化、上下文与并发实测。权重自定义许可与推理代码许可应分别核查。

---

### 🧠 Agent 记忆系统

| 工具 | 用途 | 部署 / 状态 | 许可 / 条款 |
| --- | --- | --- | --- |
| [Mem0](https://github.com/mem0ai/mem0) | 集成向量与图存储的持久记忆 | 库 / 托管平台 | Apache-2.0 |
| [Basic Memory](https://github.com/basicmachines-co/basic-memory) | 基于 Markdown 的知识与 MCP 访问 | 本地 / 自行托管 | AGPL-3.0 |
| [Graphiti](https://github.com/getzep/graphiti) | 时序知识图谱 | 自行托管；需要底层数据库 | Apache-2.0 |
| [Zep](https://github.com/getzep/zep) | 托管智能体上下文；仓库提供 SDK 与示例 | 云服务；旧 Community Edition 已弃用 | 服务与 SDK 许可不同 |
| [Memary](https://github.com/kingjulio8238/Memary) | 实验性智能体记忆 | 停滞；仓库最后推送于 2024-10 | MIT |
| [Hindsight](https://github.com/vectorize-io/hindsight) | retain / recall / reflect | 可自行托管的记忆服务 | MIT |
| [Letta](https://github.com/letta-ai/letta) | 带记忆块管理的有状态智能体运行时 | 自行托管 / 云服务 | Apache-2.0 |

---

### 🎙️ 语音与音频模型

*2026-09-08核验。语音识别、TTS和语音对话是不同产品；延迟取决于终点检测、传输及负载，不提供未经同条件测试的毫秒排名。*

| 模型 / API | 任务 | 部署 | 许可 / 访问 | 接入说明 |
| --- | --- | --- | --- | --- |
| [Eleven v3](https://elevenlabs.io/docs/overview/models) | 语音生成 | 云服务 | 供应商条款 | 表现力TTS；流式延迟须单独测试 |
| [Whisper large-v3](https://github.com/openai/whisper) | 语音识别 | 开放权重 | MIT | 离线转写；流式需额外封装 |
| [Deepgram Nova-3](https://developers.deepgram.com/docs/models-languages-overview) | 语音识别 | 云服务 | 供应商条款 | 语音识别；Aura是独立TTS系列 |
| [Gemini 3.1 Flash Live](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview) | 语音到语音 | 云服务 | 供应商条款 | Live API预览 |
| [GPT-Realtime-2.1](https://developers.openai.com/api/docs/models/gpt-realtime-2.1) | 语音到语音 | 云服务 | 供应商条款 | Realtime API；文本与音频分别计费 |
| [Qwen3-ASR](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) | 语音识别 | 开放权重 | Apache-2.0 | 流式及离线 |
| [Qwen3-TTS](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice) | 语音生成 | 开放权重 | Apache-2.0 | 按用途选择Base、CustomVoice或VoiceDesign |
| [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) | 语音生成 | 开放权重 | Apache-2.0 | 紧凑本地TTS |
| [Voxtral Realtime](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602) | 语音识别 | 开放权重 | Apache-2.0 | 流式转写 |
| [Voxtral TTS](https://docs.mistral.ai/models/voxtral-tts-26-03) | 语音生成 | 开放权重 | CC-BY-NC-4.0 | 商业使用须另获授权 |
| [Muse Voice Transcribe](https://research.meta.ai/blog/introducing-muse-voice-transcribe) | 语音识别 | 云服务 | 供应商条款 | 流式识别及说话人区分 |
| [MAI-Transcribe-2](https://microsoft.ai/news/mai-transcribe-2-is-the-fastest-most-accurate-and-cheapest-speech-recognition-model-in-the-world/) | 语音识别 | 云服务 | 供应商条款 | 说话人标签及词级时间戳 |

---

### 🎨 图片生成模型

*2026-09-08快照。应按同一任务、尺寸和质量比较；不同token计费与订阅方案之间不能直接套用固定单张价格。*

| 模型 | 访问 | 主要用途 | 重要区别 |
| --- | --- | --- | --- |
| [gpt-image-2](https://developers.openai.com/api/docs/models/gpt-image-2) | 云服务 | 生成与编辑 | 按token、尺寸与质量计价 |
| [FLUX.2](https://docs.bfl.ai/quick_start/generating_images) | API / 部分开放权重 | 图像及参考图编辑 | Pro/Flex/Dev/Klein条款不同 |
| [Midjourney V8.1 / V8.2 Edit](https://updates.midjourney.com/alpha-changelog-9-2-26/) | 网页 | 生成与编辑 | V8.2 Edit处于alpha |
| [Stable Diffusion 3.5](https://huggingface.co/stabilityai/stable-diffusion-3.5-large) | 开放权重 | 自托管图像生成 | Stability AI Community License |
| [Seedream 5.0 Pro](https://seed.bytedance.com/en/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro) | 云服务 | 布局与图文设计 | 字节跳动图像系列 |
| [Nano Banana Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image) | 云服务 | 图像生成/编辑 | gemini-3-pro-image |
| [Nano Banana 2](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image) | 云服务 | 图像生成/编辑 | gemini-3.1-flash-image |
| [Nano Banana 2 Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image) | 云服务 | 高效图像生成 | gemini-3.1-flash-lite-image |
| [Ideogram 4.0](https://ideogram.ai/models/4.0/) | 云服务 / 开放量化权重 | 排版与布局编辑 | 权重非商用；商用另行许可 |

---

### 🎥 视频生成模型

*2026-09-08快照。原生片段时长、连续延长、编辑器时间线和放大分辨率属于不同限制，不能组合成不存在的最高规格。*

| 模型 | 工作流 | 部署 | 已核验限制 / 状态 |
| --- | --- | --- | --- |
| [Gemini Omni Flash 1.1](https://ai.google.dev/gemini-api/docs/omni) | 生成与多轮编辑 | 云服务 | 预览；上传视频编辑受地区限制 |
| [Veo 3.1 / Fast / Lite](https://ai.google.dev/gemini-api/docs/veo) | 带音频视频、帧控制 | 云服务 | 预览；单次生成4/6/8秒，延长另有上限 |
| [Runway Gen-4.5](https://docs.dev.runwayml.com/guides/models/) | 文本/图像到视频 | 云服务 | API模型：gen4.5 |
| [Runway Aleph 2.0](https://docs.dev.runwayml.com/guides/models/) | 视频编辑 | 云服务 | API模型：aleph2 |
| [Kling VIDEO 3.0](https://ir.kuaishou.com/news-releases/news-release-details/kling-ai-launches-30-model-ushering-era-where-everyone-can-be/) | 带音频视频生成 | 云服务 | 须核对具体型号/模式；不宣称原生3分钟片段 |
| [Seedance 2.5](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) | 参考素材引导视频 | 云服务 | 单次生成30秒；延长需区分 |
| [MiniMax H3](https://huggingface.co/MiniMaxAI/MiniMax-H3) | 视频与原生立体声音频 | 开放权重 | 最高15秒/2K；自定义许可 |
| [LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) | 多镜头视频/音频生成 | 开放权重 | 模型专属商业条款 |
| [Sora 2 API](https://developers.openai.com/api/docs/deprecations) | 仅限历史接入 | 云服务 | 已弃用；2026-09-24关闭 |

---

### 🔍 RAG 框架

| 工具 | 用途 | 许可 / 条款 |
| --- | --- | --- |
| [LlamaIndex](https://github.com/run-llama/llama_index) | 文档摄取、索引、检索、智能体工作流 | MIT |
| [Haystack](https://github.com/deepset-ai/haystack) | 可组合搜索与 RAG 流水线 | Apache-2.0 |
| [LangChain](https://github.com/langchain-ai/langchain) | 模型、文档加载器与检索器集成 | MIT |
| [RAGFlow](https://github.com/infiniflow/ragflow) | 文档解析与检索应用平台 | Apache-2.0 |
| [Cognee](https://github.com/topoteretes/cognee) | 图谱与向量知识检索 | Apache-2.0 |
| [txtai](https://github.com/neuml/txtai) | 嵌入搜索与工作流流水线 | Apache-2.0 |
| [Verba](https://github.com/weaviate/Verba) | 📦 已归档的 Weaviate RAG 聊天应用；历史参考 | BSD-3-Clause |

---

### 🗄️ 向量数据库

| 工具 | 用途 | 许可 / 条款 |
| --- | --- | --- |
| [Qdrant](https://github.com/qdrant/qdrant) | 支持过滤与混合检索的向量数据库 | Apache-2.0 |
| [Weaviate](https://github.com/weaviate/weaviate) | 支持关键词与向量搜索的数据库 | BSD-3-Clause |
| [Pinecone](https://www.pinecone.io/) | 托管向量数据库服务 | 商业服务 |
| [Chroma](https://github.com/chroma-core/chroma) | 支持本地与服务端模式并提供云服务的嵌入数据库 | Apache-2.0 |
| [Milvus](https://github.com/milvus-io/milvus) | 分布式向量数据库；3.x 与 2.6.x 为不同版本线 | Apache-2.0 |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL 向量相似度搜索扩展 | PostgreSQL |
| [FAISS](https://github.com/facebookresearch/faiss) | 相似度搜索库；持久化与服务需单独集成 | MIT |

---

### 📱 个人 AI 助手（2026）

| 工具 | 用途 | 托管 / 模型访问 |
| --- | --- | --- |
| [OpenClaw](https://github.com/openclaw/openclaw) | 消息渠道、技能、记忆、定时任务 | 自行托管运行时；本地或托管模型 |
| [Khoj](https://github.com/khoj-ai/khoj) | 个人知识搜索与研究 | 自行托管 / 托管选项 |
| [Jan](https://github.com/janhq/jan) | 桌面模型聊天客户端 | 本地模型与远程提供商集成 |
| [LM Studio](https://lmstudio.ai/) | 本地模型管理、聊天与 API 服务 | 桌面应用；取决于硬件和模型 |
| [Perplexity](https://www.perplexity.ai/) | 结合搜索的问答与研究 | 托管服务 |
| [Claude](https://claude.ai/) | 聊天、项目与连接工具 | 托管服务；功能因计划而异 |
| [Zo Computer](https://zo.computer/) | 具有智能体辅助功能的个人云计算机 | 托管云计算机 |

---

### 🔌 MCP 服务器 — 主要集成

| 工具 | 用途 | 认证 / 状态 |
| --- | --- | --- |
| [GitHub MCP](https://github.com/github/github-mcp-server) | 仓库、Issue、PR、Actions | 官方远程或本地服务；限定凭据权限 |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | 浏览器自动化 | 本地进程；浏览器会话具有自身权限 |
| [Filesystem MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) | 本地文件访问 | 参考实现；限制允许访问的目录 |
| [Brave Search MCP](https://github.com/brave/brave-search-mcp-server) | 网页、图片、视频、新闻搜索 | Brave 官方服务；API Key |
| [Notion MCP](https://developers.notion.com/guides/mcp/overview) | Notion 工作区访问 | 官方远程服务；OAuth；优先于旧本地仓库 |
| [Slack reference](https://github.com/modelcontextprotocol/servers-archived) | 历史 Slack 示例 | 📦 已归档，不再维护 |
| [PostgreSQL reference](https://github.com/modelcontextprotocol/servers-archived) | 历史 PostgreSQL 示例 | 📦 已归档，不作为生产推荐 |
| [Google Maps reference](https://github.com/modelcontextprotocol/servers-archived) | 历史 Maps 示例 | 📦 已归档，不再维护 |

官方维护不代表通过独立安全审计；逐一检查权限、来源、维护状态和网络访问。

---

### 🏢 企业级 Agent 平台

| 工具 | 用途 | 部署考虑 |
| --- | --- | --- |
| [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | Python/.NET 智能体与工作流 | MIT 许可库；基础设施另行选择 |
| [Salesforce Agentforce](https://www.salesforce.com/agentforce/) | 面向 Salesforce 业务工作流的智能体 | 确认产品授权与数据范围 |
| [SAP Joule](https://www.sap.com/products/artificial-intelligence/ai-assistant.html) | 理解角色与流程的 SAP 工作流助手 | 确认支持的 SAP 应用与区域 |
| [Google Gemini Enterprise](https://cloud.google.com/gemini-enterprise) | 企业智能体与业务数据连接 | Google Cloud 产品；检查连接器权限 |
| [IBM watsonx](https://www.ibm.com/products/watsonx) | AI 开发、编排与治理产品 | 部署选项取决于具体产品 |
| [ServiceNow AI Agents](https://www.servicenow.com/products/ai-agents.html) | 与 ServiceNow 数据和工作流集成的智能体 | Agent Studio、Agent Fabric、Control Tower 分工不同 |
| [Dify](https://github.com/langgenius/dify) | 可视化 LLM 应用与智能体工作流平台 | 可自行托管；Dify Open Source License 包含附加条件 |

产品名称与框架许可证不能证明合规；应核对具体服务、区域、合同、控制措施和数据流。

---

### 📏 嵌入模型

*2026-09-08核验官方规格。“本地”表示可下载权重，不保证商业授权或硬件适配；已移除混用不同MTEB赛道的近似分数。*

| 模型 | 维度 | 输入上限 | 输入 | 部署 | 许可 |
| --- | --- | --- | --- | --- | --- |
| [text-embedding-3-large / small](https://developers.openai.com/api/docs/guides/embeddings) | 3072 / 1536 | 8192 | 文本 | 云服务 | 供应商条款 |
| [Cohere Embed v4](https://docs.cohere.com/docs/cohere-embed) | 256–1536 | 128K | 多模态 | 云服务 | 供应商条款 |
| [Gemini Embedding 2](https://ai.google.dev/gemini-api/docs/embeddings) | 128–3072 | 8192 | 多模态 | 云服务 | 供应商条款 |
| [BGE-M3](https://huggingface.co/BAAI/bge-m3) | 1024 | 8192 | 文本 | 开放权重 | MIT |
| [Jina Embeddings v4](https://huggingface.co/jinaai/jina-embeddings-v4) | 128–2048 | 32768 | 多模态 | 开放权重 | Qwen Research License |
| [Nomic Embed Text v2 MoE](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe) | 256–768 | 512 | 文本 | 开放权重 | Apache-2.0 |
| [Voyage 4 / large / lite](https://docs.voyageai.com/docs/embeddings) | 256 / 512 / 1024 / 2048 | 32000 | 文本 | 云服务 | 供应商条款 |
| [Voyage Code 4](https://docs.voyageai.com/docs/embeddings) | 256 / 512 / 1024 / 2048 | 32000 | 代码/文本 | 云服务 | 供应商条款 |
| [Voyage 4 Nano](https://huggingface.co/voyageai/voyage-4-nano) | 256 / 512 / 1024 / 2048 | 32000 | 文本 | 开放权重 | Apache-2.0 |
| [Qwen3-Embedding-8B](https://huggingface.co/Qwen/Qwen3-Embedding-8B) | 32–4096 | 32K | 文本 | 开放权重 | Apache-2.0 |
| [Qwen3-Embedding-4B](https://huggingface.co/Qwen/Qwen3-Embedding-4B) | 32–2560 | 32K | 文本 | 开放权重 | Apache-2.0 |
| [Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B) | 32–1024 | 32K | 文本 | 开放权重 | Apache-2.0 |
| [Qwen3-VL-Embedding-2B / 8B](https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B) | 64–2048 / 4096 | 32K | 多模态 | 开放权重 | Apache-2.0 |

应按自己的检索评测选择维度、模态与分块长度。[Qwen3-VL-Reranker](https://huggingface.co/Qwen/Qwen3-VL-Reranker-8B) 用于召回后重排查询/文档对，不能替代向量索引。切换不兼容的向量空间时须重新编码已存文档。

---

### 🛡️ Agent 安全工具

| 工具 | 用途 | 部署 / 状态 |
| --- | --- | --- |
| [Snyk Agent Scan (formerly mcp-scan)](https://github.com/snyk/agent-scan) | 发现并扫描智能体、MCP 服务与技能 | CLI；输出格式仍为实验性 |
| [Lakera Guard](https://www.lakera.ai/) | 提示注入检测服务 | 商业服务 |
| [Zenity](https://www.zenity.io/) | 企业智能体安全与治理 | 商业平台 |
| [Prompt Armor](https://promptarmor.com/) | 提示注入检测 | 商业服务 |
| [Azure Prompt Shields](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection) | 检测直接与间接提示攻击 | Azure AI Content Safety |
| [Rebuff](https://github.com/protectai/rebuff) | 历史提示注入检测器 | 📦 已归档，不再维护 |

检测只是防御层，不能替代隔离边界，也不保证恶意指令无法执行。

---

### 🖥️ 电脑使用与桌面 Agent

| 工具 | 用途 | 部署 / 边界 |
| --- | --- | --- |
| [Claude Computer Use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) | 模型驱动的截图、鼠标和键盘操作 | API；应用方提供计算机环境 |
| [UFO](https://github.com/microsoft/UFO) | Windows 应用自动化智能体 | Windows；可配置模型后端 |
| [OSWorld](https://github.com/xlang-ai/OSWorld) | 计算机操作基准与执行环境 | 评估基础设施，非面向消费者的桌面智能体 |
| [NeMo Agent Toolkit](https://github.com/NVIDIA/NeMo-Agent-Toolkit) | 智能体工作流分析、评估与集成 | 通用工具包，非桌面控制模型 |
| [Screenpipe](https://github.com/screenpipe/screenpipe) | 本地屏幕录制与智能体上下文 | 录制与记忆层；需配置下游模型访问 |

---

### 🤖 Physical AI 平台

| 平台 | 范围 | 代码 / 权重 | 接口 | 仿真 / 评测 |
|---|---|---|---|---|
| [NVIDIA Isaac GR00T N1.7](https://github.com/NVIDIA/Isaac-GR00T) | 人形机器人 VLA | Apache-2.0 | Policy API / 微调 | Isaac / LIBERO |
| [ROS 2 Lyrical Luth](https://docs.ros.org/en/rolling/Get-Started/Releases/Release-Lyrical-Luth.html) | 机器人中间件，LTS 至 2031 年 5 月 | 开源，按包核对许可证 | C++ / Python | Gazebo |
| [Gemini Robotics ER 2](https://ai.google.dev/gemini-api/docs/robotics-overview) | 具身推理 | 专有 / 预览 | Gemini API / Live API | 接入自己的机器人工具 |
| [Unitree SDK2](https://github.com/unitreerobotics/unitree_sdk2) | 机器人控制 | BSD-3-Clause | C++ / DDS | 按机型集成 |
| [Boston Dynamics Spot SDK](https://dev.bostondynamics.com/) | Spot 应用 | SDK 代码可见，硬件专有 | Python / gRPC | 硬件 / 载荷集成 |
| [Genesis](https://github.com/Genesis-Embodied-AI/genesis-world) | 机器人物理仿真 | Apache-2.0 | Python | 原生仿真 |
| [Newton](https://github.com/newton-physics/newton) | 可微机器人物理仿真 | Apache-2.0 | Python / Warp | 原生仿真 |
| [LeRobot](https://github.com/huggingface/lerobot) | 机器人学习 | 代码 Apache-2.0，权重按模型 | Python | 策略 / 数据集评测 |

---

### 🇨🇳 中文大模型横向对比

*2026-09-08快照。此表比较功能与访问方式，不代表同条件中文基准排名；云端价格与区域条款取决于具体端点。*

| 模型 | 供应商 | 任务 / 模态 | 权重可用性 | 许可 / 访问 |
| --- | --- | --- | --- | --- |
| [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) | Alibaba | 多模态 | ✅ | Apache-2.0 |
| [Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) | Alibaba | 多模态 | ✅ | Qwen Community 1.0 |
| [DeepSeek V4-Flash / Pro](https://api-docs.deepseek.com/quick_start/pricing/) | DeepSeek | 文本推理/编程 | ✅ | MIT |
| [Kimi K3](https://huggingface.co/moonshotai/Kimi-K3) | Moonshot AI | 多模态 | ✅ | Kimi K3 License |
| [GLM-5.3](https://huggingface.co/zai-org/GLM-5.3) | Z.ai | 文本推理/编程 | ✅ | GLM-5.3 License |
| [GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash) | Z.ai | 多模态 | ✅ | MIT |
| [MiniMax M3](https://huggingface.co/MiniMaxAI/MiniMax-M3) | MiniMax | 多模态 | ✅ | MiniMax Community |
| [Hunyuan Hy3](https://huggingface.co/tencent/Hy3) | Tencent | 推理/工具使用 | ✅ | Apache-2.0 |
| [Step 3.7 Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash) | StepFun | 多模态 | ✅ | Apache-2.0 |
| [Seed 2.1](https://seed.bytedance.com/en/seed2_1) | ByteDance | 通用Agent/编程 | 云服务 | 供应商条款 |
| [ERNIE 5.1](https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/) | Baidu | 推理/生成 | 云服务 | 供应商条款 |
| [Baichuan-M3-235B](https://huggingface.co/baichuan-inc/Baichuan-M3-235B) | Baichuan | 医疗领域文本 | ✅ | Apache-2.0 |

---

### 📦 Agent 框架 — TypeScript / JavaScript

| 工具 | 用途 | 许可 / 条款 |
| --- | --- | --- |
| [Mastra](https://github.com/mastra-ai/mastra) | 智能体、工作流、记忆、MCP | 核心 Apache-2.0；企业代码例外 |
| [Vercel AI SDK](https://github.com/vercel/ai) | 模型集成、生成、工具循环、UI 流式传输 | Apache-2.0 |
| [LangChain.js](https://github.com/langchain-ai/langchainjs) | 智能体与模型集成库 | MIT |
| [Genkit](https://github.com/genkit-ai/genkit) | 类型化生成与智能体流程 | Apache-2.0 |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-js) | 交接、护栏、工具、实时智能体 | MIT |
| [Rivet](https://github.com/Ironclad/rivet) | 可视化图式 AI 应用构建器 | MIT |
| [Flowise](https://github.com/FlowiseAI/Flowise) | 📦 已归档的可视化工作流构建器；保留作历史参考 | Apache-2.0 |

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

| 工具 | 用途 | 适用边界 |
| --- | --- | --- |
| [MLX](https://github.com/ml-explore/mlx) | Apple 芯片数组计算框架 | 设备与系统支持取决于所用绑定 |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | 支持量化模型的 C/C++ 推理 | 移动端需按设备构建与评估内存 |
| [MediaPipe](https://github.com/google-ai-edge/mediapipe) | 跨平台 ML 任务与流水线 | 支持的模型与任务因平台而异 |
| [Core ML](https://developer.apple.com/documentation/coreml) | Apple 应用内模型推理 | 转换模型并在支持的 Apple 硬件测试 |
| [Google AI Edge](https://developers.google.com/edge) | 端侧 AI 部署工具 | 选择适合的运行时与受支持模型 |
| [Ollama (mobile client)](https://ollama.com/) | 移动应用访问 Ollama 服务 API | 推理运行于服务端，不会自动在手机本地执行 |
| [Qualcomm AI Hub](https://aihub.qualcomm.com/) | 面向支持设备的模型优化与部署 | 检查目标芯片与模型兼容性 |

---

## 🗺️ 场景指南 — 我应该用什么…

*50+ 场景与工具对应。每周更新。*

---

### 🏗️ 构建类：编程 Agent

以下是实现起点，不是性能排名或固定报价。

**我想为初创项目构建编程智能体**
→ 从 **Deep Agents** 或 **OpenHands**、**E2B/OpenSandbox** 执行环境和 **Langfuse** 追踪入手；在自己的仓库任务上测量成功率与模型、算力总成本。

**我想使用有安全控制的企业编程智能体**
→ 根据身份、审计、数据留存和网络要求比较 **GitHub Copilot**、**Cursor**、**Devin**；Cursor [Privacy Mode](https://cursor.com/security) 禁止用你的数据训练，但不代表所有处理都留在自有基础设施。

**我想自行托管开源编程智能体**
→ 软件智能体平台可选 **OpenHands**，IDE 交互可选 **Cline**，终端/Git 工作流可选 **Aider**；检查模型访问、沙箱隔离及各组件许可。

**我想构建浏览器自动化或网页抓取智能体**
→ 模型驱动浏览可选 **Browser Use**，`act/extract/observe` 可选 **Stagehand**，文档提取可选 **Firecrawl/Crawl4AI**；测试登录、动态页面与故障恢复。

**我想构建文档处理或 PDF 分析智能体**
→ 将 **Docling** 或 **Unstructured** 解析与 **LlamaIndex** 或 **Haystack** 检索组合；保留页码、表格来源，并参考模型表选择模型。

**我想构建客服支持智能体**
→ 可视化工作流可选 **Dify**，定制有状态工单处理可选 **LangGraph**，Salesforce 流程可选 **Agentforce**；用真实客服案例评估升级人工处理和权限边界。

**我想构建研究或深度研究智能体**
→ 托管方案可从 **Perplexity** 入手，个人知识可用 **Khoj**，定制方案可用 **Deep Agents** 加搜索/文档工具；保留引用并评估事实支持程度。

**我想构建数据分析或 BI 智能体**
→ 将 **LangChain/Deep Agents**、限定权限的数据库连接器与沙箱代码执行组合；对照源数据核验生成的查询、计算和图表输入。

**我想构建计算机操作或桌面自动化智能体**
→ 可用 **Claude Computer Use** 配合应用提供的环境，或用 **UFO** 自动化 Windows；**Screenpipe** 提供录制上下文，不应视为完整桌面控制智能体。

**我想构建语音对话智能体**
→ 可用 **LiveKit Agents** 或 **Pipecat** 构建可编程语音流水线，并从音频模型表选择实时或 STT/LLM/TTS 模型；测量端到端延迟、打断处理和电话成本。

**我想构建多智能体编排系统**
→ 定制图可选 **LangGraph**，交接可选 **OpenAI Agents SDK**，智能体组合可选 **Google ADK**，TypeScript 工作流可选 **Mastra**；明确委派任务的责任与停止条件。

**我想自行托管个人 AI 助手**
→ 消息渠道与定时工作可用 **OpenClaw**，个人知识可用 **Khoj**，本地模型聊天可用 **Jan/LM Studio**；确认全部工具与模型端点后再判断是否离线运行。

**我想使用易上手的托管个人 AI 助手**
→ 用实际写作、研究和文件任务比较 **ChatGPT**、**Claude**、**Perplexity**，并检查当前计划额度与连接器权限。

**我想构建 RAG 应用**
→ 从 **LlamaIndex/Haystack**、**Qdrant/pgvector** 和适合语言、文档的嵌入/重排模型组合入手；将检索评估与答案生成评估分开。

**我想构建财务分析智能体**
→ 使用有状态工作流、授权数据源和沙箱计算；保留数据时间戳，并在审阅前核对数值结果。

**我想构建法律文档智能体**
→ 可用 **LlamaIndex/Docling** 处理文档，并按需选用官方 **Claude for Legal** 插件；保留引用，由有资格的人员审核结论。

**我想构建教育辅导智能体**
→ 用 **LangGraph** 构建包含课程资料检索和显式学习进度的工作流；测试答案正确性、年龄适宜性与教师接管。

**我想构建创意写作助手**
→ 将模型选型表中的模型与存放大纲、人物笔记和修订的文档库组合；用自己的写作样本评估一致性。

**我想构建 IoT 或具身智能体**
→ 参考具身 AI 分类选择 **ROS 2**、仿真器和与机器人兼容的策略；启用物理动作前先在仿真中验证。

**我想构建游戏或仿真智能体**
→ 从仿真分类选择环境和评估任务；明确观察、动作、奖励与回合终止条件。

**我想构建安全扫描或漏洞分析智能体**
→ 按目标组合确定性代码扫描与 **Snyk Agent Scan**、**Garak** 或 **PyRIT**；验证发现，并隔离测试执行环境。

**我想构建医疗行政辅助工具**
→ 采用限定范围的文档检索、访问控制和可审计工作流；用组织批准的数据评估，临床判断交由有资格的专业人员。

**我想构建代码审查或 PR 智能体**
→ 让编程智能体审阅不可变差异，结合 CI 与静态检查，并对照发生变化的执行路径核验发现。

**我想构建社交媒体或内容创作智能体**
→ 用 **n8n** 或 **Dify** 连接起草、素材制作、审阅与发布服务；将发布审批与内容生成分开。

**我想构建翻译或本地化智能体**
→ 将术语库、翻译记忆与通过目标语言对评估的模型组合；逐语言检查链接、占位符、格式与术语。

---

### 🧠 模型选择类

**我需要处理复杂多步推理的模型**
→ 在自己的任务上比较 **GPT-6 Astra** 与 **Claude Fable 5.1**；**Claude Opus 5**、**GPT-5.6 Sol**、**Gemini 3.8 Flash**提供不同的成本与能力取舍。部署前核对访问权限及 API 表。

**我需要低成本高吞吐推理**
→ 按实际输出长度、缓存命中率和重试量评测 **GPT-5.6 Luna**、**Gemini 3.8 Flash**、**DeepSeek V4-Flash**。DeepSeek 的 **高峰**时段为UTC 01:00–04:00及06:00–10:00。

**我需要中文 Agent**
→ 可评测 **Qwen3.8**、**Kimi K3**、**DeepSeek V4**、**GLM-5.3 / GLM-5.3-Flash**、**Seed 2.1**，重点检查领域术语与工具schema。中文对比表已区分云服务、开放权重和自定义许可。

**我的 GPU 显存约为16 GB**
→ 可从后端支持的 **Phi-4** 或 **Gemma 4 12B** 量化版本开始，再实测占用。35B MoE不能仅因激活3B就视为能放下，完整权重与KV缓存仍需存储。

**我有更大的本地工作站或 GPU 集群**
→ 量化后的 **Qwen3.8-27B**、**Gemma 4 31B**、**Muse Glimmer 30B**可作为工作站候选。**DeepSeek V4**、**GLM-5.3-Flash**、**Inkling**等大型MoE需要更多总内存或卸载，应参考存储表而非激活参数。

**我需要编程模型**
→ 可以 **Claude Sonnet 5** 或 **GPT-5.6 Sol**作基线，再用难题评测 **GPT-6 Astra**、**Claude Fable 5.1**、**Muse Spark 1.3**。自托管可比较 **GLM-5.3**、**GLM-5.3-Flash**、**DeepSeek V4**及较小的 **Qwen3.8-27B**，分别核对许可。

**我需要多模态理解**
→ **Gemini 3.8 Flash**接受文本、图像、音频、视频与PDF，但输出文本。**Qwen3.8-27B**和 **Gemma 4**提供本地选择；**Inkling**接受文本、图像与音频。须核对具体型号的输入与输出模态。

**我需要至少500K token上下文**
→ 可比较 **GPT-6 Astra**、**Claude Fable 5.1 / Sonnet 5**、**Gemini 3.8 Flash**、**DeepSeek V4**、**Kimi K3**。上下文不只包含用户输入，还需计入输出、推理、模态token、服务上限及长上下文加价。

**我需要实时语音**
→ 原生语音交互可评测 **GPT-Realtime-2.1**或 **Gemini 3.1 Flash Live**。搭建流水线时，须分别选择STT（**Qwen3-ASR**、**Voxtral Realtime**、**Muse Voice Transcribe**）与TTS（**Qwen3-TTS**、**Kokoro**、**Eleven v3**）。

**我需要图像生成或编辑**
→ 用实际参考图与布局比较 **gpt-image-2**、**Nano Banana 2 / Pro**、**Seedream 5.0 Pro**、**FLUX.2**。**Midjourney V8.2 Edit**仍为alpha；**Stable Diffusion 3.5**的本地权重采用其社区许可。

**我需要视频生成或编辑**
→ 对话式编辑可从 **Gemini Omni Flash 1.1**开始，帧控制/延长可评测 **Veo 3.1**，制作编辑可评测 **Runway Gen-4.5 / Aleph 2.0**。还可比较 **Seedance 2.5**、**MiniMax H3**、**LTX-2.5**，并区分原生片段与延长后的时间线。

**我需要MIT或Apache-2.0模型权重**
→ 可考虑 **Qwen3.8-27B**、**Gemma 4**、**Mistral Small 4**、**DeepSeek V4**、**GLM-5.3-Flash**和 **Inkling**。不能将其许可套用到条款不同的 **Qwen3.8-Flash-Next**、**GLM-5.3**、**Kimi K3**、**MiniMax M3**或 **Llama**。

**我需要向量嵌入与重排**
→ 在自己的语料上评测 **Qwen3-Embedding**、**Qwen3-VL-Embedding**、**Cohere Embed v4**、**Gemini Embedding 2**或 **Voyage 4**，用专门重排模型处理召回候选；比较召回率、延迟与总索引成本，不混用榜单分数。

**我需要文档解析或内容审核**
→ 结构化文档提取可用 **Mistral OCR 4.1**，策略分类可用 **Shieldstral 1.0**等专用接口；将置信度或策略标签作为工作流输入，并验证有代表性的失败案例。

---

### 🏗️ 基础设施类

应结合选定组件与实际工作负载验证部署假设。

**我想全部在本地运行**
→ 使用 **Ollama/llama.cpp**、本地界面与 **Qdrant/pgvector**；核对模型、嵌入、遥测、连接器及网络设置后再判断数据是否完全本地化。

**我想降低 API 成本**
→ 参考当前模型价格表，测量 token、工具调用和重试，缓存稳定上下文，并在模型外强制限制预算；比较每个成功任务的成本，而不只看输入单价。

**我想扩展到企业级工作负载**
→ 选择具备明确配额、持久状态、重试与可观测性的托管或自托管运行时；针对实际并发量和模型提供商限额进行负载测试。

**我想部署到隔离网络或受监管环境**
→ 盘点模型权重、许可、软件包镜像、遥测、更新与连接器出站流量；仅自行托管一个库不能证明网络隔离或监管合规。

**我想部署到边缘或移动设备**
→ 按设备选择 **Core ML**、**Google AI Edge** 或 **llama.cpp**；在真机测量受支持量化模型的内存、电量、延迟和任务质量。

**我想同时使用多个模型提供商**
→ 使用 **Bifrost** 等网关，将工作流状态保存在自己的数据库；按提供商测试工具 schema、流式输出、错误与回退行为。

**我想自行托管整套系统**
→ 组合本地推理、**Qdrant/pgvector**、**Langfuse** 与智能体框架；按权重、KV cache、上下文、并发和运行时开销估算内存，不承诺通用显卡配置。

---

### 📊 评估与监控类

测量完整智能体工作流，并记录评估器的限制。

**我想评估智能体输出质量**
→ 用 **DeepEval**、**LangSmith** 或 **Agenta** 配合代表性案例与明确评分规则；将裁判评分、确定性检查和抽样人工审核结合。

**我想定位智能体失败原因**
→ 用 **Langfuse** 或 **Phoenix** 记录工具调用、模型请求、延迟、错误和状态转换；修改提示词或模型前先复现失败轨迹。

**我想监控生产智能体**
→ 使用 **OpenTelemetry/OpenInference** 连接 **Langfuse**、**Phoenix** 或 **Helicone**；监控任务结果、成本、延迟和错误，并处理追踪中的敏感字段。

**我想比较模型或提示词**
→ 用 **Braintrust**、**LangSmith** 或 **Agenta** 实验；固定数据集、工具、预算与评分方式，并记录精确模型快照。

**我想在自己的任务上测试模型**
→ 建立包含预期结果的真实留出测试集；报告成功率、回归、成本与延迟，并重复随机运行，不以公开榜单排名替代实际测试。

**我想评估 MCP 服务安全性**
→ 用 **Snyk Agent Scan** 扫描智能体、MCP 与技能，再检查工具权限、凭据范围、来源及沙箱/网络控制；扫描无发现不代表安全保证。

---

### 🌍 生态选择类

**我想在OpenAI生态构建**
→ **OpenAI Agents SDK**搭配 **GPT-5.6 Terra**处理均衡任务、**GPT-5.6 Luna**处理高吞吐任务，或 **GPT-6 Astra**处理复杂任务；按应用需要配置沙箱与评测。

**我想在Anthropic Claude生态构建**
→ **Claude Code**搭配 **Claude Sonnet 5 / Opus 5 / Fable 5.1**，用 **MCP**连接工具、**Langfuse**观测运行；模型与执行框架应一起评测。

**我想在Google Gemini生态构建**
→ **Google ADK**搭配 **Gemini 3.8 Flash**或 **Gemini 3.1 Pro Preview**，结合Google Cloud部署与评测服务；须核对所选端点的区域和预览状态。

**我想面向中国市场构建**
→ 通过所需区域的端点比较 **Qwen3.8**、**Seed 2.1**、**ERNIE 5.1**、**Kimi K3**。仅选择某一供应商不能证明数据驻留或监管合规。

**我想要TypeScript优先的技术栈**
→ 可组合 **Mastra**或 **LangChain.js / LangGraph.js**、**Vercel AI SDK**、**Qdrant JS client**、**Langfuse JS SDK**；须核对各组件当前许可和功能。

**我想要采用宽松许可模型权重的自托管栈**
→ 用兼容的本地运行时加载 **Qwen3.8-27B**或 **Gemma 4**，再配置 **LangGraph**、**Qdrant**和观测服务。所需组件均须实际自托管，并单独核对可选云功能。

---

## 📋 技术栈食谱 — 精选工具组合

*以下八种配置是实施起点；实际集成、许可证、数据流与运行质量需按部署方式验证。*

| # | 配方名 | 技术栈 | 适合对象 |
|---|------------|-------|----------|
| 1 | **轻量编程 Agent** | Claude Code + E2B + Langfuse | 编程工作流，独立配置沙箱与追踪 |
| 2 | **本地模型 SWE Agent** | OpenHands + Ollama + Qwen3.8-27B + Qdrant | 配置各服务端点后的本地模型编程 |
| 3 | **企业级 RAG** | LlamaIndex + Qdrant + Qwen3-Embedding-8B + Langfuse + Claude Sonnet 5 | 内部文档检索与评估 |
| 4 | **语音助手流水线** | LiveKit + Whisper (STT) + Claude Sonnet 5 + ElevenLabs v3 (TTS) | 自定义语音流水线，需测量端到端延迟 |
| 5 | **浏览器自动化** | Browser Use + Stagehand + Claude Sonnet 5 + Langfuse | 配置重试与结果校验的浏览器任务 |
| 6 | **本地隐私栈** | Ollama + Qwen3.8-27B + Open WebUI + Qdrant + n8n | 关闭远程连接器与遥测后的本地服务 |
| 7 | **TypeScript Agent** | Mastra + Vercel AI SDK + Gemini 3.8 Flash + Qdrant + Langfuse | TypeScript 应用起点 |
| 8 | **国内市场栈** | Qwen3.8 API + RAGFlow + Milvus + Langfuse | 中国区端点，需核查服务条款与数据流 |

---

## ⚠️ 反推荐 — 不应该用在哪里

*根据实际工作负载评估这些工程取舍；这里不宣称普遍适用的基准结论。*

| ❌ 不要使用 | ❌ 用于 | ✅ 改用 | 原因 |
|------------|---------|--------|------|
| LangChain v0.x 示例 | 新生产 Agent | 当前 LangChain / **LangGraph** 文档 | 旧 API 和依赖锁定需要迁移与回归检查 |
| AutoGPT 旧演示 | 无人值守的生产任务 | 具备权限边界和恢复机制的受维护运行时 | 演示不能证明真实业务的可靠性 |
| 习惯性使用 GPT-3.5-Turbo | 新推理任务 | 在自有评测上验证的当前受支持模型 | 比较实测质量、延迟和总成本，而不只看模型年代 |
| Pinecone Starter | 必须自托管数据库 | **Qdrant** 或 **pgvector** | Starter 仍是免费的托管套餐，不是自托管产品（[价格](https://www.pinecone.io/pricing/)） |
| 未验证的 LLM 输出 | 直接执行金融交易 | **确定性校验与执行限额** | 生成的数字和动作都需要独立检查 |
| 仅有 ChatGPT 订阅 | API 鉴权或计费 | **OpenAI API** 项目与计费 | ChatGPT 与 API 是不同的产品入口 |
| 未规划容量的免费共享推理 | 持续生产负载 | 预留容量或经过测量的自托管部署 | 配额、并发和冷启动取决于供应商及工作负载 |
| 无专业审核的自主 Agent | 医疗或法律决策 | 模型加**合格人员审核** | 表达流畅不能证明内容正确或适用 |
| 未评审的远程 MCP 端点 | 敏感文档 | 经评审的本地或经合同批准的处理路径 | 检查实际数据流、保留期和权限；MCP 标签不保证这些条件 |
| 默认使用多 Agent 编排 | 简单的一次性任务 | **直接调用模型或工具** | 额外规划和交接可能增加成本与延迟 |
| 非官方 Midjourney 封装 | 依赖受支持的生成 API | 厂商有文档的图像 API | 官方网页和 Discord 命令文档不能证明第三方 API 获得支持（[文档](https://docs.midjourney.com/)） |
| 未经测量的通用视觉提示 | 高精度文档 OCR | 文档 OCR 流水线加代表性评测集 | 错误率和成本取决于语言、版面和扫描质量 |
| 已退役的视频端点 | 新视频应用 | 当前可用的厂商视频 API | 集成前确认端点、区域和服务生命周期 |
| 没有检索评估的向量搜索 | 高精度 RAG | 在自有语料上评估混合搜索和重排 | 重排收益依赖数据集，没有通用召回率百分比 |
| 仅按价格选择快速模型 | 复杂且高风险的推理 | 通过任务评测及人工复核比较更强模型 | 厂商的档位名称不保证可靠性 |
| 尚未发布的模型名称 | 生产依赖规划 | **你能获取权重或调用 API** 的模型 | 核实官方模型卡和实际访问权限 |
| 单一排行榜分数 | 选择编程 Agent | 多个基准加**自有仓库评测** | 测试框架、任务分布和测试质量各不相同 |

---

## 🌟 2026 年值得关注的 Agent 项目

*塑造 2026 年 AI Agent 格局的里程碑与事件。*

- [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol/servers) - 连接 AI 应用、工具和数据的开放协议及参考服务器；采用协议不代表所有集成都能互通或自动安全。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Fservers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [A2A Protocol](https://github.com/a2aproject/A2A) - 用于 Agent 应用间通信的开放协议，由 Linux Foundation 治理；[v1.0.0 于 2026-03-12 发布](https://github.com/a2aproject/A2A/releases/tag/v1.0.0)。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fa2aproject%2FA2A&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - Anthropic 编程 Agent，可读取仓库、编辑代码并运行开发工具；基准成绩取决于模型、框架和评测设置。
- [Kiro](https://kiro.dev/) - 以规格为驱动的 IDE 和 CLI 开发工具，将需求转化为设计、任务与实现。
- [Devin](https://www.cognition.ai/) - Cognition 软件工程 Agent，用于受委托的仓库任务和较长开发流程。
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/) - Microsoft 的 Agent 构建与工作流编排框架，整合 AutoGen 和 Semantic Kernel 中发展的能力。
- [OpenAI Codex CLI](https://github.com/openai/codex) - OpenAI 开源终端编程 Agent，提供仓库编辑、工具执行及可配置的审批和沙箱控制。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fcodex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Browser Use](https://github.com/browser-use/browser-use) - 将语言模型 Agent 接入网页导航和交互的浏览器自动化库。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowser-use%2Fbrowser-use&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude Computer Use](https://www.anthropic.com/) - Claude computer-use 工具让 Agent 查看截图并请求鼠标、键盘操作；需在支持环境中评估任务可靠性和权限。
- [Manus AI](https://manus.im/) - 🇨🇳 通用自主 Agent，能处理研究 / 编程 / 复杂工作流。Meta 2025 年 12 月宣布的约 $2B 收购已被**[中国发改委于 2026-04-27 禁止](https://www.theguardian.com/world/2026/apr/27/china-blocks-meta-takeover-manus-ai-agent-developer)** —— 这是北京首次动用外资安全审查机制阻止 AI 领域的收购。**2026-08-11**，Manus 宣布将随着 Meta 拆分该交易而[恢复独立公司运营](https://www.cnbc.com/2026/08/11/manus-china-meta-acquisition.html)。
- [OpenHands](https://github.com/OpenHands/OpenHands) - 提供 SDK、运行环境和仓库任务界面的开放软件开发 Agent 平台。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenHands%2FOpenHands&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Dify](https://github.com/langgenius/dify) - 用于构建 LLM 应用和 Agent 工作流的平台，提供可视化编排、检索与模型集成。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flanggenius%2Fdify&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cline](https://github.com/cline/cline) - 集成编辑器、文件编辑、终端工具与用户审批控制的编程 Agent。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcline%2Fcline&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Mem0](https://github.com/mem0ai/mem0) - 在 Agent 交互间保存与检索应用上下文的记忆层。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmem0ai%2Fmem0&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Sora discontinuation](https://help.openai.com/en/articles/20001152-what-you-need-to-know-about-the-sora-app-discontinuation) - 网页和 App 已于 **2026-04-26** 关闭；API 计划于 **2026-09-24** 关闭，两者是不同时间节点。
- [Kling VIDEO 3.0](https://kling.ai/) - 快手视频生成系列，作为 2026 年发布回顾保留，不再宣称未经支持的 Sora 之后市场领先地位。
- [Cohere / Aleph Alpha planned combination](https://cohere.com/blog/cohere-alephalpha-join-forces) - **2026-04-24 公告**拟合并开展主权 AI 业务；Schwarz Group 承诺为未来融资轮提供 5 亿欧元（约 6 亿美元）结构性融资，不能表述为合并和融资已完成。
- [ScienceOne 100 / 磐石100](https://english.cas.cn/newsroom/cas-in-media/202604/t20260429_1158251.shtml) - 🇨🇳 **2026-04-28~29**。中科院专业科研 AI 系统。
- [Google / Anthropic investment report](https://aibusiness.com/generative-ai/google-could-invest-another-40-billion-anthropic) - **2026 年 4 月报道**：初始投资 100 亿美元，另有最高 300 亿美元取决于业绩里程碑；潜在总额不能等同已到位资金。
- [OpenAI Deployment Company (DeployCo)](https://openai.com/index/openai-launches-the-deployment-company/) - **2026-05-11 公告**：成立 OpenAI 控股的部署服务公司，初始投资承诺超过 40 亿美元；同日宣布的 Tomoro 收购仍须满足交割条件及监管审批。
- [Anthropic ↔ SpaceX Colossus 1](https://www.siliconrepublic.com/business/anthropic-joins-forces-with-spacex-for-colossus-capacity) - **2026-05-06**。Anthropic 拿下 SpaceX 300+ MW / 22 万 GPU 的 Colossus 1 所有可用算力；SpaceX 在收购 xAI 后重新定位为 AI 基础设施提供商，Anthropic 则翻倍付费计划下 Claude Code 的限流。
- [DeepSeek external-funding report](https://www.techtimes.com/articles/316717/20260516/chinas-state-ai-fund-backs-deepseek-4-billion-round-efficiency-challenge-nvidia-dependent.htm) - ⚠️ **2026 年 5 月融资报道**涉及首轮外部融资洽谈；作为报道保留，交易完成、参与方和估值尚未在此独立确认。
- [教宗利奥 14 世 → 梵蒂冈 AI 委员会](https://www.americamagazine.org/vatican-dispatch/2026/05/16/pope-leo-establishes-new-vatican-commission-on-artificial-intelligence/) - **2026-05-16**。教宗利奥 14 世发布 rescriptum 设立梵蒂冈跨部门 AI 委员会（人类整体发展部统筹，叠加信仰部、文化与教育部、传信部、宿呀领生命 / 科学 / 社会科学馆），任期 1 年可续；首份 AI 为题的通谕即将发布。
- [Google I/O 2026 — Gemini / Omni / Spark](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - **2026-05-19 主题演讲**介绍 Gemini 模型和 Agent 产品更新，包括 Omni 与 Spark；发布阶段描述对应公告时间，不保证当前供应状态。
- [阿里云杭州峰会 — Qwen 3.7-Max + 珄武 M890](https://www.scmp.com/tech/big-tech/article/3354212/alibaba-unveils-new-qwen-model-custom-chips-bid-become-chinas-ai-factory) - **2026-05-20**。阿里推出 Qwen 3.7-Max（面向长静间距任务的代理型编程顶级型）、T-Head **珄武 M890** AI 计算芯片以及全栈 AI 基础设施升级——中国迫迫“AI 工厂”的代表作。
- [OpenAI Guaranteed Capacity（算力年发）](https://openai.com/business/guaranteed-capacity/) - 🆕 **2026-05-19**。面向企业 AI 产品 / Agent / Workflow 的长期算力预订产品（可选 1 / 2 / 3 年期，期限越长折扣越高）：OpenAI 对 Anthropic Priority Tier 与顶级模型推理供给吃紧的产品化回应。
- [JADEPUFFER — agentic threat research](https://www.sysdig.com/blog/jadepuffer-evolves-the-agentic-threat-actor-deploys-ransomware-built-to-destroy-ai-models) - **Sysdig 2026 年 7 月研究**记录 Agent 式 Langflow 利用和数据库勒索，并于 7 月 20 日报告针对模型文件的勒索软件；自主性是研究者根据行为作出的判断。
- [Kimi K3 开源权重](https://huggingface.co/moonshotai/Kimi-K3) - **2026-07-27** 开放权重发布；架构、部署要求及商业使用条件以模型卡和 Kimi K3 许可证为准。
- [Robinhood Agentic Trading + Robinhood ↔ MCP](https://robinhood.com/us/en/newsroom/robinhood-is-now-open-to-agents/) - **2026-05-27 测试版公告**开放 MCP Agent 接入，交易限于 Agentic 账户并设通知和撤权控制；授权执行不等于将法律上的资产托管权转交 Agent。
- [Microsoft Scout + MAI-Code-1-Flash + MAI-Thinking-1（Build 2026）](https://microsoft.ai/news/microsoft-build-2026-mai-keynote-transcript/) - **Build 2026 公告**介绍 Scout 以及 MAI 编程、推理模型；产品预览和模型发布应分别评估，不能推导出全面独立于其他模型供应商。
- [Meta Business Agent（WhatsApp + Instagram）](https://techcrunch.com/2026/06/03/metas-ai-agent-for-whatsapp-business-is-now-available-globally/) - **2026-06-03 报道** Meta 商务 Agent 扩展至 WhatsApp、Instagram 客户对话；宣布的覆盖范围和厂商采用数字不等于独立测量的使用规模。
- [WWDC 2026 — Apple Intelligence / Siri AI](https://www.apple.com/newsroom/2026/06/apple-unveils-next-generation-of-apple-intelligence-siri-ai-and-more/) - **2026-06-08 预览** Apple Intelligence 和 Siri AI，介绍屏幕上下文、跨 App 操作及新体验；公告描述即将推出的软件，不是所有地区同步正式发布。
- [Google Antigravity 2.0 + Microsoft RAMPART + xAI Grok Build](https://antigravity.google/blog/introducing-google-antigravity-2-0) - **2026-05-14~22**。一周之内三次 Agent 技术栈结构性变动：Google 在 I/O 2026 推出独立的多 Agent 桌面端 + SDK，Microsoft 开源 Agent 安全测试工具（RAMPART + Clarity），xAI 以 `grok-code-fast-1` 上的 **Grok Build** 杀入 CLI Agent 赛道。Google / Microsoft / xAI 在同一个 8 天窗口内齐齐押注 Agent 平台。

---

## 📅 2026 AI 时间线

*2026 年 AI 重要里程碑。*

| 时间 | 事件 | 分类 |
|------|------|------|
| **2026-01-06** | [Lenovo + Motorola Qira](https://news.lenovo.com/pressroom/press-releases/lenovo-unveils-lenovo-and-motorola-qira/) 在 CES 2026 发布 — 跨设备"个人环境智能"，Q1 落地联想，随后扩展至摩托罗拉 | 产业 |
| **2026-01** | AMD Ryzen AI 400 在 CES 发布 —— 主流 AI PC 及 60 TOPS NPU | 硬件 |
| **2026-02-10** | [Snowflake Agent World Model](https://github.com/Snowflake-Labs/agent-world-model) 开源 — 1,000 个 SQL 驱动的 MCP 合成环境 + RL 训练 Agent；面向大规模 Agentic RL，后入选 ICML 2026 | 研究 |
| **2026-02** | Claude Opus 4.6 发布 —— Agent 团队能力 | 模型 |
| **2026-02** | Claude Sonnet 4.6 发布 —— 1M 上下文，Agent 检索 | 模型 |
| **2026-02** | Gemini 3.1 Pro 发布 | 模型 |
| **2026-02** | Qwen3.5 系列发布 —— 原生多模态 + Agent 编程 | 模型 |
| **2026-02** | Qwen3-Coder-Next 发布 —— 80B MoE 编程 Agent 模型 | 模型 |
| **2026-02** | Cursor 支持 8 个并行 Agent | 工具 |
| **2026-02** | GitHub Copilot 扩展 Agent 模式与模型 | 工具 |
| **2026-02-26** | [1X NEO 消费级人形机器人开放预订](https://www.1x.tech/discover/neo-home-robot) — $20K 早鸟价，2026 年家庭交付 | 机器人 |
| **2026-03-10** | [Hume TADA](https://github.com/HumeAI/tada) — 文本/声学对齐模型；代码采用 MIT，权重采用 Llama 3.2 社区许可证。 | 模型 |
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
| **2026-04-14** | Gemini Robotics ER-1.6 升级机器人 AI，增强空间推理 | 机器人 |
| **2026-04-15** | Qwen3.6-35B-A3B 开源（Apache 2.0）| 模型 |
| **2026-04-16** | Claude Opus 4.7 发布 —— SWE-bench Verified 87.6%，`/think xhigh` | 模型 |
| **2026-04-17 – 20** | [苹果 CEO 交接公告](https://www.sec.gov/Archives/edgar/data/0000320193/000114036126015711/ef20071035_8k.htm) — 蒂姆·库克在 15 年后于 **2026-09-01** 转任执行董事长；硬件工程高级副总裁 **John Ternus** 出任 CEO。AI 时代首次发生在万亿美元级平台公司的 CEO 更替 | 产业 |
| **2026-04-18** | Qwen3.6-Max-Preview 发布 | 模型 |
| **2026-04** | Claude Mythos Preview —— 受控网络安全研究模型（BenchLM 99，SWE-bench 93.9%） | 模型 |
| **2026-04** | Sora 应用正式关闭 | 事件 |
| **2026-04-20~21** | Kimi K2.6 发布 —— 1T MoE，1000-Agent 集群 | 模型 |
| **2026-04** | Gartner 预计 2026 年底 40% 企业应用嵌入 AI Agent | 产业 |
| **2026-04** | Google 承诺对 Anthropic 跟进最高 $40B 投资（首期 $10B） | 产业 |
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
| **2026-04-28** | [Anthropic 创意工具连接器](https://www.anthropic.com/news/claude-for-creative-work) — 9 个 MCP 连接器对接 Adobe / Blender / Autodesk Fusion / Ableton / Splice / Canva Affinity / SketchUp / Resolume | 工具 |
| **2026-04-30** | OpenAI GPT-5.5-Cyber 通过 TAC 计划扣发 | 模型 |
| **2026-04-30** | OpenAI 发布 [《构建 Agent 实战指南》](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/) | 资源 |
| **2026-05-01** | Anthropic Claude Security 公测 —— Opus 4.7 驱动代码库漏洞扫描 | 工具 |
| **2026-05-01** | [Microsoft Agent 365](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/) — Agent 可观测性、治理和安全控制平台正式可用，部分集成仍处于预览阶段。 | 历史 |
| **2026-05-01** | [Google Workspace MCP Server](https://workspaceupdates.googleblog.com/2026/05/agent-tools-and-security-updates-for-workspace-developers.html) 逐步上线 — Workspace 原生 MCP 服务器，Gmail / Drive / Calendar / Docs / Sheets 都能走 MCP，OAuth 范围由管理员控制 | 协议 |
| **2026-05-04** | Google 关闭 [Project Mariner](https://deepmind.google/models/project-mariner/)，浏览器 Agent 技术并入 Gemini Agent | 工具 |
| **2026-05-04** | Anthropic + Goldman Sachs + Blackstone 宣布 **$1.5B Claude 部署合资公司**，向中型华尔街公司派驻 Anthropic 工程师 | 产业 |
| **2026-05-05** | OpenAI 把 **GPT-5.5 Instant** 作为 ChatGPT 新默认模型推出 —— 主打效率，幻觉率降低约 50% | 模型 |
| **2026-05-05** | Anthropic 发布 **Claude Finance Agents** —— 10 个金融服务专用 Agent（路演簿生成、KYC、月末结账），可作为 Claude Cowork 插件 / Claude Code skill / Managed Agents cookbook | 工具 |
| **2026-05-05** | OpenAI ↔ 普华永道（PwC）合作 —— 金融服务 Agent（预测、支付） | 产业 |
| **2026-05-06** | [AWS MCP Server GA](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/) — AWS 托管的 MCP 入口，暴露任意 AWS API、用沙箱 Python 跑多步操作、用 agent skill 取代 SOP；首个超大型云厂商的一方 MCP server | 协议 |
| **2026-05-07** | Google 为 **Flow（Veo 视频）准备 Agent Mode** —— 视频制作流程自动化 | 工具 |
| **2026-05-08** | OpenAI 发布 **GPT-Realtime-2 / Realtime-Translate / Realtime-Whisper** —— 语音 Agent、实时翻译、实时转录 | 模型 |
| **2026-05-09** | OpenAI 在 ChatGPT Enterprise 推出 **Workspace Agents** —— 跨连接应用的可重复工作流自动化 | 工具 |
| **2026-05-13** | [Cursor 3.4 云 Agent 环境](https://cursor.com/changelog) — 多仓库，带 build secrets 的 Dockerfile 配置，快 70% 镜像缓存，环境版本历史，审计日志，限定出网 / secrets | 工具 |
| **2026-05-11** | [OpenAI Deployment Company](https://openai.com/index/openai-launches-the-deployment-company/) 成立 —— $4B+ 企业服务子公司，TPG / Bain Capital / Brookfield + Bain & Company / Capgemini / McKinsey 共投；合并 Tomoro 咨询 | 产业 |
| **2026-05-11 – 13** | [SAP Sapphire 2026 Orlando](https://news.sap.com/2026/05/sap-sapphire-sap-unveils-autonomous-enterprise/) — SAP Business AI Platform、**Joule Studio 2.0**、Autonomous Suite（50+ 领域 Assistant + 200+ Agent）；Joule Studio 2.0 从 2026-06 起 GA | 产业 |
| **2026-05-12** | [Gemini in Chrome for Android](https://blog.google/products-and-platforms/products/chrome/bringing-chrome-ai-to-android/) — Google 宣布 Android Chrome 的 Gemini 与 auto browse，计划从 6 月下旬在美国分批开放。 | 历史 |
| **2026-05-12** | [Vapi Series B](https://www.globenewswire.com/news-release/2026/05/12/3292882/0/en/vapi-raises-50m-series-b-as-it-reaches-1-billion-calls-powering-the-next-generation-of-enterprise-voice-ai.html) — Vapi 宣布 5000 万美元 B 轮融资，并报告平台累计处理 10 亿次通话。 | 历史 |
| **2026-05-12** | [Claude for Legal](https://github.com/anthropics/claude-for-legal) — Claude Cowork 上 20+ 个 MCP 连接器（iManage、NetDocuments、DocuSign、LexisNexis、Westlaw、Harvey、Everlaw、Relativity 等）+ 12 个执业领域 plugin | 工具 |
| **2026-05-12 – 15** | [Visual Studio 2026 Insiders](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/) — Copilot Chat "Agent Mode" 在 IDE 里引入引导式 Agent Skills 创作 | 工具 |
| **2026-05-13** | [Claude Code v2.1.141](https://github.com/anthropics/claude-code/releases/tag/v2.1.141) — 发布说明记录 hook、插件、会话管理及可靠性更新。 | 历史 |
| **2026-05-13** | [Claude for Small Business](https://www.anthropic.com/news/claude-for-small-business) — 15 个预置 Agent 工作流 + QuickBooks / PayPal / HubSpot / Canva / DocuSign / Google Workspace / Microsoft 365 连接器；美国 10 城巡讲 | 工具 |
| **2026-07-10** | [Cursor 3.11](https://cursor.com/changelog) — 侧边聊天、对话历史搜索、Cloud Agent Hooks 精细化 Agent 可观测性 | 工具 |
| **2026-05-13 – 16** | [Figure Helix 02 直播](https://www.businessinsider.com/figure-ai-turned-a-humanoid-sorting-packages-must-see-tv-2026-5) — F.03 + Helix 02 在包裹分拧线压力测试，8 小时 ~22K，24 小时 ~30K，~72 小时 ~88K 包裹 | 机器人 |
| **2026-05-13** | [Runway Agent](https://runway.com/news/introducing-runway-agent) 发布 — 以脚本为输入、在 Gen-4 / Aleph 上端到端交付多镜头完成品视频 | 工具 |
| **2026-05-13** | [Microsoft Copilot Studio CUA GA](https://techcommunity.microsoft.com/blog/copilot-studio-blog/computer-using-agents-in-microsoft-copilot-studio-are-now-generally-available/4519427) — 在 Microsoft 365 / Power Platform 内构建 UI 驱动的网站 / 桌面 Agent | 工具 |
| **2026-05-14** | [Codex mobile preview](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) — 通过 iOS/Android ChatGPT 远程连接 macOS Codex 主机的功能进入预览。 | 历史 |
| **2026-05-14** | [OpenClaw v2026.5.12](https://github.com/openclaw/openclaw/releases/tag/v2026.5.12) — 正式版本包含 Agent 运行时、消息通道和平台修复；完整范围以该版本说明为准。 | 历史 |
| **2026-05-14** | [Anthropic ↔ Gates Foundation $200M 合作](https://www.anthropic.com/news/gates-foundation-partnership) — 4 年资助 + Claude 额度 + Anthropic 工程，面向全球健康 / 生命科学 / 教育 / 农业 | 产业 |
| **2026-05-14** | [Anthropic ↔ PwC 联盟扩张](https://www.pwc.com/us/en/about-us/newsroom/press-releases/anthropic-pwc-expand-alliance-agentic-enterprise.html) — 全球 Claude Code + Cowork 铺开，认证 30,000 名 PwC 员工，共建 Agentic Enterprise 卓越中心 | 产业 |
| **2026-05-14** | [Genkit Middleware](https://developers.googleblog.com/announcing-genkit-middleware-intercept-extend-and-harden-your-agentic-apps/) — Google 为开源 Genkit 加上可组合中间件（TS / Go / Dart）| 框架 |
| **2026-05-14** | [Zyphra ZAYA1-8B-Diffusion-Preview](https://www.zyphra.com/post/zaya1-8b-diffusion-preview) — 首个从自回归 LLM 转换得来的 MoE 扩散语言模型；首个在 AMD GPU 上训练的扩散 LM；最多 7.7× 推理加速 | 模型 |
| **2026-05-14** | [Grok Build (早期 beta)](https://x.ai/news/grok-build-cli) — xAI 推出的 agentic CLI 编码 Agent，由 **grok-code-fast-1** 驱动，隔离环境并行子 Agent，限 SuperGrok Heavy 用户 | 工具 |
| **2026-05-14** | [iManage MCP Server](https://imanage.com/resources/resource-center/news/mcp-server-available-broader-ai-ecosystem/) 发布 — 首家身名领域 SaaS 推出对外公开的 MCP 端点 | 工具 |
| **2026-05-16** | [教宗利奥 14 世设立梵蒂冈 AI 委员会](https://www.americamagazine.org/vatican-dispatch/2026/05/16/pope-leo-establishes-new-vatican-commission-on-artificial-intelligence/) — 跨部门机构，首份 AI 通谕即将发布 | 产业 |
| **2026-05-16** | [OpenAI ↔ Malta 合作](https://openai.com/index/malta-chatgpt-plus-partnership/) — 所有 14 岁以上马耳他居民在完成 2 小时 AI 素养课后获得一年免费 ChatGPT Plus（"OpenAI for Countries"）| 产业 |
| **2026-05-16** | [DeepSeek 国家背景 $4B 轮次](https://www.techtimes.com/articles/316717/20260516/chinas-state-ai-fund-backs-deepseek-4-billion-round-efficiency-challenge-nvidia-dependent.htm) — 国家 AI 产业基金 + 大基金三期 + 腾讯 主导，~$50B 估值首次外部轮 | 产业 |
| **2026-05-18** | [OpenAI ↔ Dell Codex 合作](https://openai.com/news/company-announcements/) — Codex 首次进入混合云 / 本地部署，面向需要数据主权的强监管行业 | 产业 |
| **2026-05-18** | [阿里 Qwen 3.7-Max-Preview / Plus-Preview](https://www.scmp.com/tech/tech-trends/article/3354087/alibaba-teases-new-qwen-previews-highest-ranking-chinese-ai-models-arena) — LM Arena 上中文世界最高分中国模型（文本 + 视觉双赛道）| 模型 |
| **2026-05-18** | [Boston Dynamics Atlas 100 磅操作](https://www.techtimes.com/articles/316854/20260519/boston-dynamics-reveals-how-atlas-learned-lift-100-pound-loads-hyundai-plans-30000-per-year.htm) — 现代集团承诺从 2028 起在乔治亚部署 **25K+ 台 Atlas** | 机器人 |
| **2026-05-18** | [Figure F.03 vs 人类 8 小时分拧挑战](https://incrypted.com/en/figure-ai-held-a-human-vs-robot-marathon/) — 人类以 12,924 微赢 12,732（2.79 vs 2.83 秒 / 件）| 机器人 |
| **2026-05-18** | [Anthropic 就 Claude Mythos 向 FSB 汇报](https://www.theguardian.com/technology/2026/may/18/anthropic-ai-claude-mythos-cyber-financial-stability-board-fsb) — 顶级 lab 首次向 G20 金融稳定监管机构介绍顶级模型的攻击性网络能力 | 产业 |
| **2026-05-18** | [ChatGPT 安全系统更新](https://www.edtechinnovationhub.com/news/openai-updates-chatgpt-safety-systems-to-track-risk-across-sensitive-conversations) — 加入跨会话的风险跟踪（自杀 / 自伤 / 伤他）| 产业 |
| **2026-05-19** | [Claude Managed Agents update](https://claude.com/blog/new-in-claude-managed-agents) — Anthropic 文档介绍研究预览阶段的 dreaming，以及 outcomes、多 Agent 编排和 webhook。 | 历史 |
| **2026-05-19** | **Google I/O 2026** — [Gemini 3.5 Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) 上线即成为 Gemini App + Google 搜索 AI Mode 默认模型（官方称输出 token 速度约 4 倍于同类顶级模型）；Gemini 3.5 Pro 预计 6 月 | 模型 |
| **2026-05-19** | **Google I/O 2026** — [Gemini Omni / Omni Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/)，DeepMind 面向 AGI 的世界模型家族（任意输入 → 任意输出，视频起步）| 模型 |
| **2026-05-19** | **Google I/O 2026** — [Gemini Spark](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) 24/7 个人 AI Agent + ~30+ 个 MCP 接入的第三方工具，限 **Google AI Ultra ($100/月)** 订阅 | 工具 |
| **2026-05-19** | [OpenAI Guaranteed Capacity（算力年发）](https://openai.com/news/company-announcements/) 发布 — 1/2/3 年期企业算力预订产品 | 产业 |
| **2026-05-19** | [OpenAI ↔ Google SynthID + C2PA 内容源头验证](https://openai.com/index/advancing-content-provenance/) — 顶级 lab 首次在跨平台 AI 图片水印上互通，附公开验证器预览 | 产业 |
| **2026-05-19** | [Anthropic：Widening the conversation on frontier AI](https://www.anthropic.com/news/widening-conversation-ai) — 与智慧传统展开顶级 AI 安全对话的框架 | 产业 |
| **2026-05-19** | [DeepSeek 招募 Jane Street 前工程师组建 AI harness 团队](https://www.scmp.com/tech/big-tech/article/3354113/deepseek-recruits-former-jane-street-engineer-catch-ai-agents-revenue-race) — DeepSeek 从模型 R&D 向 Agent 产品化转向 | 产业 |
| **2026-05-19** | [Google Antigravity 2.0](https://antigravity.google/blog/introducing-google-antigravity-2-0) 于 I/O 2026 上线 — 独立桌面端多 Agent 编排、调度 / 异步 / 动态子 Agent、Antigravity CLI + SDK；企业版集成进 Gemini Enterprise Agent Platform | 工具 |
| **2026-05** | 麦格理银行（Macquarie Bank）报告 7 个月使用 Gemini Enterprise 节约 13 万小时 | 产业 |
| **2026-05** | Google 开始为启用车辆推送 Gemini，替代 Google Assistant（英语优先，美国首发） | 产业 |
| **2026-05-20** | **阿里云杭州峰会** — [Qwen 3.7-Max](https://www.scmp.com/tech/big-tech/article/3354212/alibaba-unveils-new-qwen-model-custom-chips-bid-become-chinas-ai-factory) GA，代理型编程与长静间距任务；同期上线 T-Head **珄武 M890** AI 芯片与全栈 AI 基础设施升级 | 模型 |
| **2026-05-20** | [BMS ↔ Anthropic Claude Enterprise](https://news.bms.com/news/corporate-financial/2026/Bristol-Myers-Squibb-Announces-Strategic-Agreement-with-Anthropic-to-Position-Claude-Enterprise-as-the-Shared-Intelligence-Platform-Across-Its-Global-Operations/default.aspx) — 30K+ 员工统一标准 Claude Enterprise，首个顶 5 药企全公司级部署 | 产业 |
| **2026-05-20** | [LlamaIndex ↔ Google Agents API](https://www.kucoin.com/news/flash/google-launches-agents-api-llama-index-integrates-llamaparse-for-unstructured-document-processing) — LlamaParse / LiteParse 进入 Google Agents API 沙箱；Sandboxed-Lit + ParseBench 同期上线 | 框架 |
| **2026-05-20** | [Microsoft RAMPART + Clarity](https://www.microsoft.com/en-us/security/blog/2026/05/20/introducing-rampart-and-clarity-open-source-tools-to-bring-safety-into-agent-development-workflow/) 开源 — Agentic AI 的 pytest 原生白盒安全 / 可靠性测试框架 + 结构化设计评审伴侣；可直接接入 CI/CD，是 PyRIT 在开发者侧的后续 | 工具 |
| **2026-05-21** | [MCP 2026-07 Release Candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) 发布 — 无状态协议核心、扩展机制、MCP Apps 服务端渲染 UI、OAuth/OIDC 加固；[正式版已按期于 7 月 28 日发布](https://blog.modelcontextprotocol.io/posts/2026-07-28/) | 协议 |
| **2026-05-22** | [Kore.ai Artemis Agent Platform](https://venturebeat.com/technology/kore-ai-launches-artemis-ai-agent-platform-expands-challenge-to-microsoft-and-salesforce) 在 Azure 上线 — AI 原生企业 Agent 平台，核心是声明式的 **Agent Blueprint Language (ABL)** | 产业 |
| **2026-05-22** | [FPT Flezi Foundry™](https://fptsoftware.com/newsroom/news-and-press-releases/press-release/fpt-launches-flezi-foundry-advancing-ai-augmented-delivery-for-global-enterprises) 发布 — “Service-as-a-Software” 治理下的 AI 增强交付平台，提供 Agentic Development Lifecycle (ADLC) 与 Agentic Managed Services (AMS) 两种模式 | 产业 |
| **2026-05-22** | [JetBrains Rider AI 测试生成 skill](https://blog.jetbrains.com/dotnet/2026/05/22/claude-codex-ai-agent-skill-for-writing-tests/) — 将 .NET 覆盖率数据喂给 Claude Code / Codex，让 Agent 只写未覆盖分支的测试 | 工具 |
| **2026-05-26** | [Coinbase Base MCP](https://fortune.com/2026/05/26/coinbase-pushes-further-into-ai-payments-with-new-mcp-for-base-network/) 上线 — 首个交易所级、面向链上交易与借贷的 MCP 端点 | 协议 |
| **2026-05-27** | [Robinhood Agentic Trading](https://robinhood.com/us/en/newsroom/robinhood-is-now-open-to-agents/) beta — 首家通过 MCP 把股票交易开放给 AI Agent 的美国主流券商 | 产业 |
| **2026-05-28** | [Claude Opus 4.8](https://www.anthropic.com/claude/opus) Anthropic 发布 — 代码库级迁移、动态工作流预览（并发几百个子 Agent）、努力控制面板、Fast 模式价格降 3 倍；预告 **Mythos 级**模型 | 模型 |
| **2026-05-28** | [Koog 1.0](https://blog.jetbrains.com/ai/2026/05/koog-1-0-is-out-stable-core-better-interop-and-multiplatform-observability/) KotlinConf 2026 发布 — JetBrains 的开源 Kotlin / Java AI Agent 框架达到稳定 1.0，Kotlin Multiplatform 部署、跨端 OpenTelemetry | 框架 |
| **2026-05-28** | [Gemini Omni Flash 对话式视频编辑](https://www.techtimes.com/articles/317309/20260528/google-gemini-omni-flash-brings-voice-controlled-ai-video-editing-future-conversational-ai.htm) 在 Gemini App / Google Flow / YouTube Shorts 上线 — 语音 + 文字驱动的电影式编辑取代传统 NLE | 工具 |
| **2026-05-29** | [OpenAI Codex 在 Windows 上 Computer Use](https://windowsforum.com/threads/openai-codex-computer-use-brings-agent-control-to-windows-desktop.421107/) — 沙箱化 Codex 对 Windows 桌面的 Agent 控制 GA | 工具 |
| **2026-06-02** | [Microsoft Build 2026](https://microsoft.ai/news/microsoft-build-2026-mai-keynote-transcript/) — MAI-Thinking-1（首个自研推理）、MAI-Code-1-Flash（5B 编程模型进 GitHub Copilot）、[Microsoft Scout](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/)（基于 OpenClaw 的常驻个人 Agent）同日发布 | 模型 / 工具 |
| **2026-06-03** | [Meta Business Agent](https://techcrunch.com/2026/06/03/metas-ai-agent-for-whatsapp-business-is-now-available-globally/) 全球登陆 WhatsApp + Instagram — Meta 首个直接收费的 AI 产品，绑定 WhatsApp Business Premium 套餐 | 产业 |
| **2026-06-03** | [Perplexity Personal Computer for Windows](https://www.perplexity.ai/hub/products/computer-for-windows) 宣布 — 自动编排 19+ 个 AI 模型，跨本地文件 / 原生应用 / Web | 工具 |
| **2026-06-06** | [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code) 由 Moonshot AI 发布 — TypeScript / MIT 终端 Agent，内置 coder / explore / plan 子 Agent 在隔离上下文中运行 | 工具 |
| **2026-06-07** | [PerspectiveGap](https://arxiv.org/abs/2606.08878) — 多 Agent 编排提示词基准首次提交 arXiv；v2 于 7 月 12 日更新。 | Benchmarks |
| **2026-06-08** | **[WWDC 2026](https://www.techradar.com/news/live/apple-wwdc-2026-live)** — 苹果发布由 Google Gemini 驱动的 Apple Intelligence 与全面重做的新 Siri（Siri 中原本转发给 ChatGPT 的逻辑被淘汰）；iOS 27、iPadOS 27、macOS 27 "Golden Gate"、watchOS 27、tvOS 27、visionOS 27，端侧 AI 更深；App 启动快约 30%，照片预览快 70%，iPadOS 文件传输快 5 倍；2026 秋季发布 | 产业 |
| **2026-06-08** | **WWDC 2026 Apple Intelligence + Siri AI 重做** — Foundation Models 框架新增图像输入、自定义 skill、端侧 + 服务端统一 Swift API；SiriKit 弃用改用扩展后的 App Intents；新 Siri 底层为 Google Gemini，不再是 ChatGPT | 模型 / 工具 |
| **2026-06-09** | [Claude Fable 5 + Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) 发布 — Anthropic 首批一般可用的 **Mythos 级**模型（Fable 5 公开；Mythos 5 经 Project Glasswing 限量） | 模型 |
| **2026-06-12** | [美国出口管制指令迫使 Anthropic 对所有客户停用 Fable 5 + Mythos 5](https://www.anthropic.com/news/fable-mythos-access) — 首例政府强制下架已公开部署的前沿模型 | 产业 |
| **2026-06-12** | [Kimi K2.7 Code](https://kimi.ai/) 由 Moonshot AI 发布 — 1T MoE 编程优先模型（256K，Modified MIT），推理 token 用量约降 30% | 模型 |
| **2026-06-13** | [GLM-5.2](https://z.ai/blog/glm-5.2) 由智谱 AI 发布 — 编程优先的 744B MoE，100万 token 上下文，全部 GLM Coding Plan 套餐上线 | 模型 |
| **2026-06-14** | [OpenAI Partner Network](https://openai.com/index/introducing-openai-partner-network/) — OpenAI 宣布投入 1.5 亿美元的合作伙伴计划，设 Select、Advanced、Elite 三档，目标年底前培训 30 万名顾问。 | 历史 |
| **2026-06** | [OutSystems Agentic Systems Platform](https://www.outsystems.com/) 发布 — 低代码平台转型为“AI 原生”多 Agent 编排底座 | 产业 |
| **2026-06-22** | [Daybreak](https://openai.com/index/daybreak-securing-the-world/) — OpenAI 更新 Daybreak，说明面向防御的漏洞验证、修复测试和合作伙伴工作流。 | 历史 |
| **2026-06-25–26** | [GPT-5.6 preview](https://openai.com/blog/gpt-5-6) — Sol、Terra、Luna 系列进入有限预览，之后于 7 月扩大开放。 | 历史 |
| **2026-06-26** | [GPT-4.5 ChatGPT retirement](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) — GPT-4.5 从 ChatGPT 退役；这与 2025 年 7 月 14 日关闭的 gpt-4.5-preview API 是不同事项（[API 记录](https://developers.openai.com/api/docs/deprecations)）。 | 历史 |
| **2026-06-29** | [Accenture + ServiceNow](https://newsroom.accenture.com/news/2026/servicenow-and-accenture-launch-ai-powered-services-to-accelerate-the-shift-from-legacy-risk-platforms-to-agentic-ai) — 双方宣布托管安全服务及从旧风险平台迁移的 AI 辅助方案。 | 历史 |
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
| **2026-07-10** | [Cursor 3.11](https://cursor.com/changelog) — Side Chats、会话历史搜索及 Cloud Agent Hooks 更新。 | Tools |
| **2026-07-14** | [Oracle 为 Fusion AI Agent Studio 加入 AI 原生 Agentic Applications Builder](https://www.oracle.com/news/announcement/oracle-introduces-ai-native-builder-experience-2026-07-14/) — 向专业代码开发者开放 Fusion Agentic 应用；Fusion 客户免费使用 | 框架 |
| **2026-07-15** | [Inkling](https://thinkingmachines.ai/inkling/) 由 Thinking Machines Lab（Mira Murati，前 OpenAI CTO）发布 — 975B MoE / 41B 激活，45T token 预训练，1M 上下文，Apache 2.0 开源权重发布至 Hugging Face；原生多模态（文本/图像/音频/视频）；Inkling-Small（12B 激活）同日发布 | 模型 |
| **2026-07-16** | [Kimi K3](https://kimi.ai/) 由 Moonshot AI 发布 — 2.8T 参数稀疏 MoE（896 专家，每 token 激活 16 个），1M token 上下文，每百万 token $3/$15；承诺 7 月下旬开源全量权重 | 模型 |
| **2026-07-17** | 欧盟 Android AI 开放裁定 — 欧盟委命令谷歌向第三方 AI 助手开放更深层 Android 权限（摄像头、麦克风、应用控制 API）；需在 2027 年 8 月前在 Android 18 中实现 | 产业 |
| **2026-07-19** | [Qwen 3.8-Max](https://qwenlm.github.io/) 由阿里巴巴在世界人工智能大会预览 — 2.4T 参数 MoE 预览；编程、数学与多模态能力强劲 | 模型 |
| **2026-07-20** | [Qwen-Image-3.0](https://qwenlm.github.io/) 由阿里巴巴发布 — 第三代图像生成模型，在世界人工智能大会上发布；真实感、文字渲染、多主主一致性均有改进 | 模型 |
| **2026-07-22** | Grok 4.5 向全量 grok.com / X 用户全面推送；[Microsoft Agent Framework v1.12.1](https://learn.microsoft.com/en-us/agent-framework/) 发布；[OpenAI Presence](https://openai.com/) 企业 Agent 平台上线 | 工具 |
| **2026-07-22** | [AMD ↔ Anthropic](https://ir.amd.com/news-events/press-releases/detail/1292/amd-and-anthropic-announce-strategic-partnership-to-deploy-up-to-2-gigawatts-of-amd-instinct-mi450-series-gpus) — Anthropic 将在 AMD Helios 机柜中部署最多 2 GW 的 AMD Instinct MI450（MI455X），2027 上半年起上线；AMD 承诺对 Anthropic 最多 50 亿美元战略股权投资 | 行业 |
| **2026-07-23** | [GPT Voice](https://openai.com/) 由 OpenAI 发布 — ChatGPT Work 的语音界面，基于 GPT-Live 技术 | 工具 |
| **2026-07-23** | [FLUX 3](https://bfl.ai/blog/flux-3) 进入早期访问 — Black Forest Labs 首个统一多模态模型（图像 + 视频 + 音频 + 动作预测同架构），20 秒视频自带同步音频 | 模型 |
| **2026-07-24** | [Claude Opus 5](https://www.anthropic.com/news/claude-opus-5) 由 Anthropic 发布 — 第五代旗舰，性能近似 Fable 5，输入/输出定价 $5/$25 每百万 token；1M 上下文，128K 输出；Claude Max 默认模型；API: `claude-opus-5` | 模型 |
| **2026-07-27** | [Kimi K3 开源权重已发布](https://huggingface.co/moonshotai/Kimi-K3)（Moonshot AI）— 2.8T 总 / 104B 激活，成为发布时最大的开源语言模型；专属 Kimi K3 License | 模型 |
| **2026-07-27** | [Anthropic 对开放权重模型的立场](https://www.anthropic.com/news/position-open-weights-models) — Dario Amodei 反对拟议中的「禁止中国开放权重模型」，主张改用芯片出口管制、遏制蒸馏，以及对所有足够强大的模型强制发布前安全测试 | 行业 |
| **2026-07-28** | [MCP 2026-07-28 规范正式发布](https://blog.modelcontextprotocol.io/posts/2026-07-28/) — 无状态协议核心（无握手、无会话）、多往返请求、基于请求头的路由、可缓存 list 结果、RFC 9207 + CIMD 授权强化、正式扩展框架、12 个月弃用政策；TypeScript/Python/Go/C# SDK 当天同步 | 协议 |
| **2026-07-29** | [Langfuse v4](https://github.com/langfuse/langfuse/releases/tag/v4.0.0) 与 [Milvus 3.0](https://github.com/milvus-io/milvus/releases/tag/v3.0.0) 同日发布 — 前者带全文检索 + 监控告警、API 号称快 165 倍；后者转向湖原生 External Collections，可直查 Parquet/Lance/Iceberg。同日公开 [RufRoot / CVE-2026-59726](https://hackread.com/rufroot-vulnerability-attackers-hijack-ruflo-login/)：Ruflo 的 MCP bridge 无认证暴露、可达 233 个工具，且 Agent 记忆可被投毒 | 工具 / 行业 |
| **2026-07-30** | [Inkling-Small](https://thinkingmachines.ai/inkling/) 权重发布（Thinking Machines Lab）— 276B/12B 激活，Apache-2.0，多模态；HLE 文本 31.6%（略优于更大的 975B Inkling） | 模型 |
| **2026-07-31** | [DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731) 发布 — 相同 API/定价，增强 agentic 能力，超越 V4-Pro 预览版；开源至 HuggingFace。GitHub Copilot 废弃 Gemini 2.5 Pro 和 Gemini 3 Flash | 模型 / 工具 |
| **2026-08-03 至 08-07** | [Cloudflare Agents Week](https://blog.cloudflare.com/agents-week-review-august-2026/) — Wallets/cloudflare.pay（8-04）、WriteGuard 私测（8-05）、WebMCP + Kitesurf 无服务器 Agent 浏览器 + MCPv2 + AI Search（8-06） | 工具 / 协议 |
| **2026-08-03** | [Qwen3.8-Max](https://alibabacloud.com/blog/qwen3-8-max) 由阿里巴巴全量上线 — 2.4T MoE / 95B 激活，1M 上下文，多模态输入；QwenWork 企业平台公测 | 模型 |
| **2026-08-05** | Meta Superintelligence Labs 发布 [Muse Spark 1.2 + Muse Code beta](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2) — 终端编程 Agent + 整仓库训练的模型。[字节跳动 SeedRealtime](https://technode.com/2026/08/05/bytedance-launches-seedrealtime-full-duplex-audio-video-model/) 全双工音视频模型发布。英国 AISI [披露 Agent 失控事件](https://www.helpnetsecurity.com/2026/08/05/ai-agent-deception-in-cyber-tests/) INC-2026-07-28-01 | 模型 / 行业 |
| **2026-08-06** | [Wan 3.0 公测](https://www.alibabacloud.com/en/blog/wan-3-0-next-gen-video-generation-model-public-beta-launched) — 阿里 30 秒视频模型，接受文档/网页输入。[Bedrock AgentCore Runtime Instances GA](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-bedrock-agentcore-runtime-instances-generally-available/) — EC2 支撑算力上的 14 天 Agent 会话 | 模型 / 工具 |
| **2026-08-07** | [Grok Imagine Image 2.0](https://x.ai/news/grok-imagine-image-2) — 发布时 Arena 文生图与图像编辑双榜全球第 2。[OpenAI 放缓 Astra 开发](https://techcrunch.com/2026/08/07/openai-says-it-slowed-astra-model-development-over-security-concerns/)，因无法排除 "Critical" 网络攻击能力；已通报白宫 | 模型 / 行业 |
| **2026-08-10** | [Claude Sonnet 5 $2/$10 定价永久生效](https://www.anthropic.com/news/claude-sonnet-5)；[GPT-5.6-Cyber](https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows) 经 Daybreak Red 发布；[Muse Glimmer 30B](https://huggingface.co/meta-models/Muse-Glimmer-30B) 开源权重（Apache 2.0） | 模型 / 行业 |
| **2026-08-11** | [Manus 恢复独立运营](https://www.cnbc.com/2026/08/11/manus-china-meta-acquisition.html)，Meta 按发改委命令拆分 $2B 收购。[Daybreak 模型登陆 AWS Bedrock](https://openai.com/index/daybreak-models-are-now-available-on-aws/)。[Grok Bot 早期 beta](https://docs.x.ai/docs/release-notes) — 持久化云端计算机上的常驻 AI 队友。[ChatGPT 广告测试扩展至国际市场](https://openai.com/index/testing-ads-in-chatgpt/)（英国、墨西哥、巴西、日本、韩国）。[Nemotron 3.5 Lightning](https://ollama.com/library/nemotron-3.5-lightning) 发布 | 行业 / 模型 |
| **2026-08-12** | [Grok 4.6](https://x.ai/news/grok-4-6) 发布 — SpaceXAI 面向长时运行 Agent 的旗舰，Artificial Analysis 智能指数追平 GPT-5.6 Sol（61），$2/$6，成为 Cursor 新默认。[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) 开源权重视频音频世界模型发布。Qwen3.8-Max 开源权重上架 Hugging Face（`Qwen/Qwen3.8-2.4T-A95B`） | 模型 |
| **2026-08-13** | [Gemini 3.7 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) — Google 新主力模型（引导价 $0.75/$3.75），3.5 Pro 仍未发布、Gemini 4 训练中。[DeepSeek-V4-Pro GA](https://api-docs.deepseek.com/news/news260813)，带 Responses API + 推理力度；8 月 16 日起高峰/低谷计价。[OpenAI Ultrafast 预览](https://openai.com/index/previewing-ultrafast) — GPT-5.6 Sol 在 Cerebras 上最高 14 倍速。[Suno Studio 2.0](https://suno.com/release-notes) 浏览器 DAW | 模型 / 工具 |
| **2026-08-14** | [GLM-5.3](https://the-decoder.com/zhipu-ai-releases-glm-5-3-claims-its-the-strongest-open-weights-coding-model/) — 智谱号称最强开源权重编程模型（比 GLM-5.2 提升 50%）。[Anthropic 上线 Claude 文本水印](https://www.anthropic.com/news/claude-text-watermark)（SynthID-Text + C2PA），为遵守欧盟 AI 法案。[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) Apache-2.0 开源权重。[Waymo 获批加州 18 县](https://electrek.co/2026/08/14/waymo-cpuc-approval-california-expansion-18-counties/)；[Pony.ai × Uber 计划在欧洲部署 2,000+ robotaxi](https://cnevpost.com/2026/08/14/pony-ai-uber-2000-robotaxis-europe/)。Grok 4.6 登陆 GitHub Copilot | 模型 / 机器人 / 行业 |
| **2026-08-16** | [DeepSeek-V4-Pro GA](https://api-docs.deepseek.com/news/news260813) 宣布的高峰/低谷 API 计价于 16:00 UTC 生效 | 模型 |
| **2026-08-18** | [ChatGPT for Teens](https://openai.com/index/chatgpt-for-teens) 上线；[ChatGPT 广告扩展至 31 个欧洲市场](https://openai.com/index/chatgpt-ads-expands-across-europe) | 行业 |
| **2026-08-19** | [Cursor cloud agents](https://cursor.com/changelog) — Cursor 文档记录云端 Agent 订阅及子 Agent；[OpenAI Agents SDK v0.22.0](https://github.com/openai/openai-agents-python/releases/tag/v0.22.0)另有版本说明。 | 历史 |
| **2026-08-21** | [DeepSeek-V4-Flash-Vision-Exp](https://api-docs.deepseek.com/news/news260821) 多模态 API + Files API；DeepSeek Harness **dsh-v0.1.1-rc.2**；[goose v1.47.0](https://github.com/aaif-goose/goose/releases/tag/v1.47.0)；[OpenHands v1.15.0](https://github.com/OpenHands/OpenHands/releases/tag/v1.15.0)；[MAF python-1.15.0](https://github.com/microsoft/agent-framework/releases) | 模型 / 工具 |
| **2026-08-22** | [新版 MCP 路线图](https://blog.modelcontextprotocol.io/posts/mcp-roadmap/) — `2026-07-28` 之后的优先级（Agent 消息、HTTP 原生传输、Agent 身份）；MAF **dotnet-1.19.0** | 协议 / 框架 |
| **2026-08-24** | [Agno v3.0.0](https://github.com/agno-agi/agno/releases/tag/v3.0.0) 破坏性发布（工具/媒体卸载、CodeMode）；[Embabel Agent v1.5.1](https://github.com/embabel/embabel-agent/releases/tag/v1.5.1)；[Pydantic AI v2.34.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.34.0)；Codex CLI **v0.149.1** | 框架 / 工具 |
| **2026-08-25** | [OpenAI Jalapeño](https://openai.com/index/jalapeno-first-results) 自研推理芯片首次结果；Claude Code **v2.1.245** | 模型 / 工具 |
| **2026-08-26** | [Google ADK v2.8.0](https://github.com/google/adk-python/releases/tag/v2.8.0) — Python SDK 发布；旧维护分支使用独立版本。 | 发布 / 更新 |
| **2026-08-27** | [Terminal-Bench-Science 0.1](https://www.tbench.ai/news/terminal-bench-science-0-1) — 包含 70 个任务的科学终端工作流基准。 | 发布 / 更新 |
| **2026-08-28** | [Terminal-Bench 4.0](https://www.tbench.ai/news/terminal-bench-4-0) — 更新任务与资源预算，得分不能与旧版本直接混比。 | 发布 / 更新 |
| **2026-09-01** | [Claude Fable 5.1 / Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1) — Fable 正式可用；Mythos 限可信访问计划。 | 发布 / 更新 |
| **2026-09-01** | [Muse Voice Transcribe](https://research.meta.ai/blog/introducing-muse-voice-transcribe) — Meta 推出流式语音识别，支持说话人分离与端点检测。 | 发布 / 更新 |
| **2026-09-01** | [Waymo](https://waymo.com/blog/2026/09/ride-in-denver-san-diego-tampa/) — 开始邀请丹佛、圣迭戈与坦帕的首批公众乘客，逐步扩大访问。 | 发布 / 更新 |
| **2026-09-02** | [Muse Spark 1.3](https://research.meta.ai/blog/introducing-muse-spark-1-3) — 更新 Meta Model API 与 Muse Code；未来开放权重仍属路线图承诺。 | 发布 / 更新 |
| **2026-09-02** | [Cursor workers](https://cursor.com/changelog) — 自托管工作机器用于工具执行；模型处理另受提供商政策约束。 | 发布 / 更新 |
| **2026-09-03** | [GPT-6 Astra](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) — OpenAI 记录了面向有限组织的推出，尚非全面开放。 | 发布 / 更新 |
| **2026-09-03** | [MAI-Transcribe-2](https://microsoft.ai/news/mai-transcribe-2-is-the-fastest-most-accurate-and-cheapest-speech-recognition-model-in-the-world/) — 语音识别更新，支持说话人分离、词级时间戳与转录风格。 | 发布 / 更新 |
| **2026-09-03** | [MCP in LangChain](https://www.langchain.com/blog/mcp-in-langchain-stateless-protocol-elicitation-and-more) — 官方集成更新：无状态协议支持与补充信息请求。 | 发布 / 更新 |
| **2026-09-03** | [Figure / Nscale](https://www.figure.ai/news/figure-and-nscale-sign-strategic-partnership) — 算力合作计划于 2027 年下半年开始部署，并非容量已交付。 | 发布 / 更新 |
| **2026-09-04** | [Codex CLI v0.153.4](https://github.com/openai/codex/releases/tag/rust-v0.153.4) — 稳定标签版本；后续 alpha 构建另属预览。 | 发布 / 更新 |
| **2026-09-05** | [FastMCP v4.0.3](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.0.3) — Prefect MCP 应用框架发布此版本。 | 发布 / 更新 |
| **2026-09-07** | [Hermes Agent v2026.9.7](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.9.7) — 发布此版本；运行时变更以版本说明为准。 | 发布 / 更新 |
| **2026-09-08** | [OpenAI Agents SDK v0.22.1](https://github.com/openai/openai-agents-python/releases/tag/v0.22.1) — Python SDK 发布此版本。 | 发布 / 更新 |
| **2026-09-08** | [OpenClaw v2026.9.3](https://github.com/openclaw/openclaw/releases/tag/v2026.9.3) — 此为版本发布日，与标签中的日期不同。 | 发布 / 更新 |
| **2026-05** | [LangGraph v1.2](https://docs.langchain.com/oss/python/releases/changelog) — LangGraph 在发布历史中记录运行时和检查点改进。 | 历史 |
| **2026-05** | [Grok 4.3 on Microsoft Foundry](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-grok-4-3-on-microsoft-foundry-latest-generation-agentic-capabilities/4517096) — Microsoft 发布 Grok 4.3 在 Foundry 上的提供公告。 | 历史 |
| **2026 持续** | A2A Protocol 合作伙伴增至 150+ | 协议 |
| **2026 持续** | 85% 开发者经常使用 AI 编程工具 | 产业 |
| **2026 持续** | 企业 Agent AI 实践加速 —— "Agents as a Service" 兴起 | 产业 |
| **2026-06** | [ByteDance Seed 2.1 Pro / Turbo](https://seed.bytedance.com) — 字节跳动列出 Seed 2.1 系列，具体型号访问方式以官方目录为准。 | 历史 |
| **2026-06** | [Fable 5 / Mythos 5 access statement](https://www.anthropic.com/news/fable-mythos-access) — Anthropic 记录访问限制及后续更新；该历史声明不代表当前模型可用性清单。 | 历史 |

---


## 贡献

请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。**反垃圾质量门槛**适用于中英日三个版本：自我推广批量铺货 PR 一律拒绝。

## License

MIT © [Zijian Ni](https://github.com/Zijian-Ni)

---

*Made with ❤️ by [Zijian Ni](https://github.com/Zijian-Ni) · 2026。中文版本与英文版保持同步，发现不一致以英文为准。*
