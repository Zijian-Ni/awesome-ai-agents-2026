<div align="center">

# 🤖 Awesome AI Agents 2026 · 日本語版

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fawesome-ai-agents-2026&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)](https://github.com/Zijian-Ni/awesome-ai-agents-2026/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-June%2012%2C%202026-blue.svg)](#)
[![Resources](https://img.shields.io/badge/Resources-500%2B-orange.svg)](#)
[![Audited](https://img.shields.io/badge/Spam_Audited-2026--06--12-success.svg)](#️-ステータス凡例)
[![English](https://img.shields.io/badge/Lang-English-informational.svg)](README.md)
[![中文](https://img.shields.io/badge/Lang-中文-red.svg)](README.zh-CN.md)

**2026 年の AI モデル・エージェントフレームワーク・ツール・プロトコル・リソースを厳選したリスト —— エージェントが本格的にインフラ化した一年。**

*基盤大規模言語モデル、マルチモーダル生成、エージェントプロトコル（MCP / A2A）、コーディングエージェント、Computer Use、生成 AI までカバー。*

### 🏷️ ステータス凡例

各エントリには成熟度を一目で判断できるよう、以下のタグが付くことがあります:

- 🆕 **New** — 60 日以内に追加。実績はまだ確定していない
- 📦 **Archived** — リポジトリがアーカイブ済み。歴史的参照のためのみ残す
- 💤 **Stale** — 6 か月以上コミットなし。動作はするかもしれないが活発な保守はない
- ⚠️ **Unverified** — 提出は新しく、第三者の利用実績が乏しい（star が少ない / 単独メンテナ / 同じ PR を多数の awesome リストに同時投稿）。**可視性のための掲載で推奨ではない** —— 利用前に各自で評価すること
- 🇨🇳 **Chinese ecosystem** — 中国本土のチームによる、または主に中国市場を対象とするプロジェクト
- 🔥 **Hot** — 直近30日間の GitHub stars成長率が20%超，コミュニティ勢い。
- ⚡ **Updated** — 直近14日以内に注目リリースまたは主要機能が追加された。
- 🧪 **Experimental** — 潜在能力はあるが本番環境向けではない；R&D探索のみ推奨。
- 💰 **Freemium** — 基本機能は無料，スケール拡張・高度な機能は有料。
- 🔐 **Audited** — 第三者機関によるセキュリティ監査または形式検証済み。
- 🇨🇳 **China-first** — 中国語・国内規制・中国クラウドインフラに最適化されたプロジェクト。

[基盤モデル](#-基盤モデル-2026) · [マルチモーダル](#-マルチモーダルと生成-ai) · [プロトコル](#-エージェントプロトコルと標準) · [フレームワーク](#️-エージェントフレームワーク) · [IDE & ビジュアル](#️-エージェント-ide-とビジュアルビルダー) · [メモリ](#-エージェントメモリ) · [ツール](#-ツールと-api-連携) · [サンドボックス](#-エージェントサンドボックスと計算分離) · [セキュリティ](#️-エージェントセキュリティ) · [RAG](#-rag-とナレッジ) · [コーディング](#-コーディングエージェント) · [Physical AI](#-physical-ai--身体性エージェント) · [シミュレーション](#-エージェントシミュレーションと世界モデル) · [ベンチマーク](#-ベンチマークとリーダーボード) · [Computer Use](#️-computer-use--デスクトップエージェント) · [ブラウザ & Web](#-ブラウザと-web-エージェント) · [音声](#️-音声とマルチモーダルエージェント) · [パーソナル](#-パーソナル-ai-エージェント) · [モバイル](#-モバイルエージェント) · [エンタープライズ](#-エンタープライズエージェントプラットフォーム) · [評価](#-エージェント評価とオブザーバビリティ) · [研究ツール](#-ai-研究ツール) · [学習](#-学習リソース) · [中国エコシステム](#-中国-ai-エコシステム) · [比較](#-比較--サイドバイサイド表) · [2026 注目](#-2026-年に注目すべきエージェントプロジェクト) · [タイムライン](#-2026-ai-タイムライン)

</div>

---

## 🚀 はじめに

> **AI エージェントを初めて使う方へ：** このパスで学びましょう。
> 1. 📖 **概念を理解する** — エージェントとチャットボットの差異
> 2. 🗺️ **シナリオを探す** → [シナリオガイド](#️-シナリオガイド--何に何を使うべきか)
> 3. 🧩 **実証済みの構成をコピー** → [スタックレシピ](#-スタックレシピ--実証済みツール組み合わせ)
> 4. 🔍 **最適なツールを選ぶ** → [比較表](#-比較--サイドバイサイド表)
> 5. ⚠️ **アンチパターンを避ける** → [非推奨リスト](#️-アンチピック--使ってはいけないケース)
>
> **已に開発中の方へ：** こちらへジャンプ：
> - 🆕 [最新追加（2026年5月）](#-2026-ai-タイムライン) • 🛡️ [セキュリティ](#️-エージェントセキュリティ) • 💰 [コスト比較](#-基盤モデル--api-コスト--コンテキスト)

---

## 目次

- [🧠 基盤モデル 2026](#-基盤モデル-2026)
- [🎨 マルチモーダルと生成 AI](#-マルチモーダルと生成-ai)
- [🔗 エージェントプロトコルと標準](#-エージェントプロトコルと標準)
- [🏗️ エージェントフレームワーク](#️-エージェントフレームワーク)
- [🛠️ エージェント IDE とビジュアルビルダー](#️-エージェント-ide-とビジュアルビルダー)
- [🧠 エージェントメモリ](#-エージェントメモリ)
- [🔌 ツールと API 連携](#-ツールと-api-連携)
- [🧪 エージェントサンドボックスと計算分離](#-エージェントサンドボックスと計算分離)
- [🛡️ エージェントセキュリティ](#️-エージェントセキュリティ)
- [🔍 RAG とナレッジ](#-rag-とナレッジ)
- [💻 コーディングエージェント](#-コーディングエージェント)
- [🤖 Physical AI / 身体性エージェント](#-physical-ai--身体性エージェント)
- [🎮 エージェントシミュレーションと世界モデル](#-エージェントシミュレーションと世界モデル)
- [📊 ベンチマークとリーダーボード](#-ベンチマークとリーダーボード)
- [🖥️ Computer Use / デスクトップエージェント](#️-computer-use--デスクトップエージェント)
- [🌐 ブラウザと Web エージェント](#-ブラウザと-web-エージェント)
- [🗣️ 音声とマルチモーダルエージェント](#️-音声とマルチモーダルエージェント)
- [📱 パーソナル AI エージェント](#-パーソナル-ai-エージェント)
- [📱 モバイルエージェント](#-モバイルエージェント)
- [🏢 エンタープライズエージェントプラットフォーム](#-エンタープライズエージェントプラットフォーム)
- [📊 エージェント評価とオブザーバビリティ](#-エージェント評価とオブザーバビリティ)
- [🔬 AI 研究ツール](#-ai-研究ツール)
- [📚 学習リソース](#-学習リソース)
- [🇨🇳 中国 AI エコシステム](#-中国-ai-エコシステム)
- [📝 比較 — サイドバイサイド表](#-比較--サイドバイサイド表)
- [🗺️ シナリオガイド — 何に何を使うべきか](#️-シナリオガイド--何に何を使うべきか)
- [📋 スタックレシピ — 実証済みツール組み合わせ](#-スタックレシピ--実証済みツール組み合わせ)
- [⚠️ アンチピック — 使ってはいけないケース](#️-アンチピック--使ってはいけないケース)
- [🌟 2026 年に注目すべきエージェントプロジェクト](#-2026-年に注目すべきエージェントプロジェクト)
- [📅 2026 AI タイムライン](#-2026-ai-タイムライン)

---

## 🧠 基盤モデル 2026

*AI エコシステムを動かす最新の大規模言語モデル群、ベンダー別。20+ ベンダーから 65+ モデル。*

### OpenAI

- [GPT-5.5](https://openai.com/index/gpt-5-5-system-card/) - 🆕 **2026-04-23 公開**（コードネーム "Spud"）。エージェントタスク向けの新フロンティア: コーディング、オンライン調査、データ分析、自律的なツール操作。推論の安定性と長時間タスク処理能力が大幅向上。ChatGPT Plus / Pro / Business / Enterprise で利用可能。
- [GPT-5.5 Pro](https://openai.com/index/gpt-5-5-system-card/) - 🆕 2026-04-23。並列テストタイム計算による高精度バリアント。Pro / Business / Enterprise。
- [GPT-5.5 Instant](https://openai.com/index/gpt-5-5-instant/) - 🆕 **2026-05-05**。ChatGPT の新しいデフォルトモデル。効率重視のアップグレードで、ハイステイクスなプロンプトの幻覚率が約 50% 低下。無料枠でも利用可能。
- [GPT-5.5-Cyber](https://openai.com/index/trusted-access-for-cyber/) - 🆕 **2026-04-30**。GPT-5.5 のサイバーセキュリティ特化版。OpenAI の Trusted Access for Cyber (TAC) プログラム経由で、検証済みの防御者・政府・重要インフラ・セキュリティベンダーにのみ提供。一般公開なし。
- [OpenAI Daybreak](https://thehackernews.com/2026/05/openai-launches-daybreak-for-ai-powered.html) - 🆕 **2026-05-12**。GPT-5.5 + GPT-5.5-Cyber + Trusted-Access-for-Cyber を束ねたサイバー防御プラットフォーム。AI による脆弱性検出とパッチ検証を提供し、プレビューは EU 政府機関とセキュリティベンダーにも開放。
- [GPT-5.4](https://openai.com/) - 2026-03 公開。1M トークンコンテキスト、高度なコーディング、Computer Use、ツール検索。BenchLM 94、SWE-bench Verified 77.2%、OSWorld 75%（人間ベースライン超え）。
- [GPT-5.4 Pro](https://openai.com/) - GPT-5.4 の高精度バリアント。BenchLM 92。
- [GPT-5.3](https://openai.com/) - 2026 年初頭。GPT-5.3 Instant（会話）と GPT-5.3-Codex（コーディング）を含む。
- [GPT-5.2](https://openai.com/) - 2025-12 公開。最先端の推論・長文脈・視覚。
- [GPT-5](https://openai.com/index/introducing-gpt-5/) - 2025-08 公開。ChatGPT のデフォルトモデル、GPT-4o の後継。マルチモーダル、gpt-5 / mini / nano の 3 段階。
- [GPT-4o](https://openai.com/index/hello-gpt-4o/) - テキスト・視覚・音声をネイティブにサポートする Omni モデル。2026-02 に ChatGPT から退役、API では引き続き利用可能。
- [GPT-4.5](https://openai.com/) - ⚠️ **2026年6月27日に ChatGPT から退役**（API 利用は継続）。2025年2月に研究プレビューとしてリリースされ、GPT-5.5 ファミリーへの完全移行に伴い退役。o3 も 2026年8月26日に退役予定。
- [o3 / o4-mini](https://openai.com/index/introducing-o3-and-o4-mini/) - 思考連鎖推論モデル。2025-04 公開。o3 は 2026-08-26 退役。
- [Codex CLI](https://github.com/openai/codex) - OpenAI が公開したオープンソースのターミナルコーディングエージェント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fcodex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenAI Deployment Company (DeployCo)](https://openai.com/index/openai-launches-the-deployment-company/) - 🆕 **2026-05-11**。OpenAI が过半所有するエンタープライズ AI 導入サービス企業。初期資金 $4B+（TPG / Advent / Bain Capital / Brookfield / Goldman Sachs / SoftBank + Bain & Company / Capgemini / McKinsey など），Forward Deployed Engineers モデルを中核にし Tomoro コンサルティングチーム（~150 名）を取り込む。
- [Codex on Mobile](https://9to5mac.com/2026/05/14/openai-brings-codex-control-to-chatgpt-for-iphone-and-android/) - 🆕 **2026-05-14**。ChatGPT iOS / Android から Mac 上の Codex デスクトップ App をリモート操作 —— 出力のレビュー、アクション承認、モデル切り替え、タスク起動が可能。ファイル / 資格情報 / 権限はローカルに留まる。Free / Plus / Go プレビュー。
- [OpenAI ↔ Malta パートナーシップ](https://openai.com/index/malta-chatgpt-plus-partnership/) - 🆕 **2026-05-16**。初の国家レベル提携。マルタ大学提供の 2 時間 AI リテラシー講座を修了した 14 歳以上のマルタ国民 / 居住者に 1 年間の ChatGPT Plus を無償提供。"OpenAI for Countries" イニシアチブの第一弾。
- [OpenAI ↔ Dell Codex 提携](https://openai.com/news/company-announcements/) - 🆕 **2026-05-18**。Dell のハイブリッドクラウド / オンプレミス基盤を経由して Codex を企業現場に届ける。データ主権と規制遵拠が求められる分野にとって初めての主要なパブリッククラウド以外への Codex 配信チャネル。
- [ChatGPT 安全システムアップデート](https://www.edtechinnovationhub.com/news/openai-updates-chatgpt-safety-systems-to-track-risk-across-sensitive-conversations) - 🆕 **2026-05-18**。長いセッションを跨いだとしても、自殺 / 自傷 / 他者への危害などの高リスクシグナルを継続的に追跡・検出できるように安全システムを更新。
- [OpenAI Guaranteed Capacity（Compute Annual Pass）](https://openai.com/news/company-announcements/) - 🆕 **2026-05-19**。企業の AI プロダクト / エージェント / ワークフロー向けにコンピュートを長期予約する製品（期間 1 / 2 / 3 年、長期コミットほど値引きが拡大）。Anthropic の Priority Tier に対する製品としての回答。
- [OpenAI ↔ Google SynthID + C2PA コンテンツ出所検証](https://openai.com/index/advancing-content-provenance/) - 🆕 **2026-05-19**。OpenAI が Google と連携し、ChatGPT/Sora 生成画像に耐久性のある **SynthID** クロスプラットフォームウォーターマークを追加、C2PA に加盟し、**「この画像は OpenAI のものか」**検証ツールをプレビューとして公開。主要フロンティア lab 同士初のウォーターマーク相互運用。

### Anthropic

- [Claude Opus 4.8](https://www.anthropic.com/claude/opus) - 🆕 **2026-05-28**。Opus シリーズの大規模アップデート：コードベース規模のマイグレーション、エージェント判断の鮮明化、「ダイナミックワークフロー」リサーチプレビューで 1 セッション中に数百のサブエージェントを並列実行可能、手動「エフォートコントロール」パネル、**Fast モード 3 倍安い**（入力 $5 / 出力 $25 / 100 万 token は同価）。Anthropic ネイティブ、Amazon Bedrock、AWS Claude Platform、Google Cloud、Microsoft Foundry で利用可。限定企業向けに **Mythos クラス** モデルを予告。
- [Claude Opus 4.6](https://www.anthropic.com/) - 2026-02 公開。1M トークン、14.5 時間のタスク完了。Arena 会話リーダーボード首位。
- [Claude Sonnet 4.6](https://www.anthropic.com/news/claude-sonnet-4-6) - 2026-02 公開。フロンティア級コーディングとエージェント性能、1M トークンコンテキスト。
- [Claude Mythos Preview](https://www.anthropic.com/) - 🆕 2026-04 招待制研究プレビュー。BenchLM 99（リーダーボード首位）、SWE-bench Verified 93.9%。Project Glasswing パートナー限定。
- [Claude Opus 4](https://www.anthropic.com/news/claude-4) - 2025-05 公開。
- [Claude Sonnet 4](https://www.anthropic.com/news/claude-4) - 2025-05 公開。バランス重視。
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - ターミナルで動作する Anthropic のエージェント型コーディングツール。Opus 4.7 + `/think xhigh` 対応。
- [Claude Security](https://www.anthropic.com/) - 🆕 **2026-05-01** パブリックベータ。Opus 4.7 駆動の企業向けコードベース脆弱性スキャナ —— 信頼度評価・深刻度・再現手順・推奨修正付きパッチを生成。Enterprise ユーザー向け [claude.ai/security](https://claude.ai/security)。
- [Claude Finance Agents](https://www.anthropic.com/news/finance-agents) - 🆕 **2026-05-05**。Opus 4.7 ベースの金融特化エージェントを 10 種同時公開（pitchbook 作成、KYC、月次決算、ディール選定など）。Claude Cowork プラグイン、Claude Code skill、Managed-Agents の cookbook として配備可能。
- [Claude Add-ins / Dreaming / Outcomes / Multi-agent orchestration](https://www.anthropic.com/news/code-with-claude-2026) - 🆕 **2026-05-08（Code with Claude 2026）**。Anthropic が Add-ins、セッション間の定期メモリ整理（"Dreaming"）、ルーブリック駆動の "Outcomes"、そして共有ファイルシステムと監査可能な trace を備えた主エージェント + サブエージェント編成モデルをまとめて発表。
- [Anthropic ↔ SpaceX Colossus 1](https://www.siliconrepublic.com/business/anthropic-joins-forces-with-spacex-for-colossus-capacity) - 🆕 **2026-05-06**。Anthropic が SpaceX の Memphis データセンター Colossus 1（220K+ NVIDIA H100/H200/GB200, 300+ MW）の全利用可能キャパシティを取得し Claude Opus 推論に充てる。Claude Code の 5 時間レート制限を Pro / Max / Team / Enterprise で 2 倍化、Pro / Max でピーク時限も撤廃。
- [Claude for Legal](https://www.anthropic.com/news/claude-for-legal) - 🆕 **2026-05-12**。Claude Cowork の上に載せたリーガル型スタック。**20+ の MCP コネクタ**（iManage / NetDocuments / DocuSign / Ironclad / LexisNexis / Westlaw / Harvey / Everlaw / Relativity / CourtListener など）と **12 の実務領域プラグイン**（商事・雇用・プライバシー・製品・コーポレート・AI ガバナンス・訴訟アソシエイト・司法試験対策）を同梱。Word / Outlook / Excel / PowerPoint とネイティブ連携。
- [Claude for Small Business](https://www.anthropic.com/news/claude-for-small-business) - 🆕 **2026-05-13**。Claude Cowork 内の中小企業トグル —— 財務 / オペレーション / 営業 / マーケティング / HR / カスタマーサポートをカバーする 15 個のエージェントワークフローと、QuickBooks / PayPal / HubSpot / Canva / DocuSign / Google Workspace / Microsoft 365 へのコネクタ。PayPal 協赞の無料講座と米国 10 都市を回るツアー付き。
- [Anthropic ↔ Gates Foundation $200M](https://www.anthropic.com/news/gates-foundation-partnership) - 🆕 **2026-05-14**。4 年間 $200M パートナーシップ。助成金 + Claude 利用クレジット + Anthropic エンジニアをグローバルヘルス / ライフサイエンス / 教育 / 農業のプログラムに投入。生まれるツールはすべて無償公開。
- [Anthropic ↔ PwC 提携拡大](https://www.pwc.com/us/en/about-us/newsroom/press-releases/anthropic-pwc-expand-alliance-agentic-enterprise.html) - 🆕 **2026-05-14**。PwC は Claude Code + Claude Cowork のグローバル展開、PwC プロフェッショナル 30,000 名の認定、共同「Agentic Enterprise」センターオブエクセレンスを掲げる —— エージェント構築、AI ネイティブの M&A、財務 / サプライチェーン / HR の再設計に集中。
- [Anthropic ↔ 金融安定理事会（FSB）Claude Mythos ブリーフィング](https://www.theguardian.com/technology/2026/may/18/anthropic-ai-claude-mythos-cyber-financial-stability-board-fsb) - 🆕 **2026-05-18**。Anthropic が G20 レベルの金融安定規制当局に、フロンティアモデル（Claude Mythos）の攻撃的サイバー能力を初めて説明。金融システムリスク評価の予備資料となる。
- [Code with Claude 2026 セッションを YouTube で公開](https://www.infoq.com/news/2026/05/code-with-claude/) - 🆕 **2026-05-18 公開**。5 月 6 日開催の開発者カンファレンス全セッションをアーカイブ公開：Claude Code のロードマップ、Claude Developer Platform のアップデート、Managed Agents の dreaming とマルチエージェントオーケストレーション、パートナー展開事例。
- [Widening the conversation on frontier AI](https://www.anthropic.com/news/widening-conversation-ai) - 🆕 **2026-05-19**。宗教 / 哲学 / 先住民伝統など「智恵の伝統」とフロンティア AI 安全を話し合うための枠組みを公開。パブリックエンゲージメントシリーズの一环。
- [Bristol Myers Squibb ↔ Anthropic Claude Enterprise](https://news.bms.com/news/corporate-financial/2026/Bristol-Myers-Squibb-Announces-Strategic-Agreement-with-Anthropic-to-Position-Claude-Enterprise-as-the-Shared-Intelligence-Platform-Across-Its-Global-Operations/default.aspx) - 🆕 **2026-05-20**。BMS が Claude Enterprise を 30,000+ 名の社員の共通インテリジェンス基盤として採用し、創薬・開発・デリバリーの全工程にエージェント化 Claude を組み込む。世界トップ 5 製薬企業で初めての公社規模での Claude 全社展開。

### Google DeepMind

- [Gemini 3.5 Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - 🆕 **2026-05-19 — Google I/O 2026**。Gemini App と Google 検索 AI Mode の新しいデフォルトモデル。公式によると出力トークン速度は同類のフロンティアモデルより **約 4 倍高速**、主要ベンチマークで Gemini 3.1 Pro を上回る。Gemini 3.5 Pro は 6 月以降に公開予定。
- [Gemini Omni / Omni Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - 🆕 **2026-05-19 — Google I/O 2026**。Google DeepMind の AGI を見揮えた新しい**ワールドモデル**ファミリー。Omni Flash は**任意の入力から任意のモダリティを生成**（まずビデオから、画像とテキストは順次拡張）でき、Gemini Robotics / Genie の路線を受け継ぐ。
- [Gemini 3.1 Pro](https://deepmind.google/technologies/gemini/) - 2026-02 公開。BenchLM 94、GPQA Diamond 94.3%（世界記録）、ARC AGI2 77.1%。フラッグシップ価格 `$2/1M tokens`。
- [Gemini 3.1 Flash Live](https://deepmind.google/technologies/gemini/) - 🆕 2026-04。音声アシスタント・対話エージェント向けリアルタイムマルチモーダルストリーミング。低遅延・長文脈。
- [Gemini 3.1 Flash-Lite (GA)](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-lite-is-now-generally-available) - 🆕 **2026-05-08**。Gemini API / AI Studio / Vertex AI で一般提供開始。Gemini 3 ファミリーで最も高速かつコストパフォーマンスの高いモデル —— コード補完、リアルタイム UX、エージェント型開発ツール向け。Gemini 2.5 Flash 並みの品質を大幅に低いコストで提供。
- [Gemini Omni Flash ・ 会話型ビデオ編集をロールアウト](https://www.techtimes.com/articles/317309/20260528/google-gemini-omni-flash-brings-voice-controlled-ai-video-editing-future-conversational-ai.htm) - 🆕 **2026-05-28**。Omni Flash が消費者向けに Gemini App、**Google Flow**、**YouTube Shorts** に順次展開・編集エンジンとして、テキスト / 音声 / 画像 / 音響のプロンプトでシネマ風ズーム、背景入れ替え、天候変更などを実行し、従来のノンリニア編集ソフトを不要にする。
- [Gemini Spark（24/7 パーソナル AI エージェント）](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - 🆕 **2026-05-19 — Google I/O 2026**。クラウド上で 24/7 動作し、まず Gmail / Chat とネイティブ連携した上で、MCP を介して ~30+ のサードパーティツール（Adobe / Dropbox / Uber など）に拡張。Google AI Ultra 加入者限定。
- [Google AI Ultra（$100/月）](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - 🆕 **2026-05-19 — Google I/O 2026**。開発者・クリエイター・ヘビーユーザー向けの新たなコンシューマーサブスクリプション最上位ティア。Gemini Spark、最高 Gemini 3.5 クオータ、さらに今後公開予定の Gemini 3.5 Pro をアンロック。
- [Gemini 3.1 Flash / Flash Lite](https://deepmind.google/technologies/gemini/) - 高スループット用途向けの高速・低コストモデル。
- [Gemini 4 (Open)](https://deepmind.google/technologies/gemini/) - 🆕 2026-04 公開。オープンモデル: 2B / 4B / 26B / 31B。科学推論と文書理解、ローカル展開向け。
- [Gemini 2.5 Pro / Flash](https://deepmind.google/technologies/gemini/) - 2025-06 GA。Thinking モデル + 1M コンテキスト。
- [Gemma 4 31B](https://github.com/google-deepmind/gemma) - 🆕 2026-04。GPQA Diamond 84.3%。デバイス推論用の強力なオープンウェイト代替。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle-deepmind%2Fgemma&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Gemma 3](https://github.com/google-deepmind/gemma) - 前世代のオープンモデルファミリー。
- [Gemini Robotics ER-1.6](https://deepmind.google/) - 🆕 2026-04-14。空間・物理推論を強化したロボティクス AI。Agile Robotics と提携し実機展開。

### Meta

- [Llama 5](https://ai.meta.com/llama/) - 🆕 **2026-04-08**。Meta Superintelligence Labs 発の 600B 超パラメータ・オープンソース旗艦。"再帰的自己改善" を掲げる研究ライン。推論・コーディング・自律的なエージェント挙動で主要クローズドモデルを上回ると主張。
- [Muse Spark](https://ai.meta.com/blog/introducing-muse-spark-msl/) - 🆕 **2026-04-09**。Meta Superintelligence Labs (MSL) の最初のモデル。ネイティブマルチモーダル推論で Meta AI アプリ・スマートグラス・Facebook / Instagram / WhatsApp / Messenger の機能を駆動。
- [Llama 4 Scout](https://llama.meta.com/) - 109B 総 / 17B アクティブ、16 専門家 MoE、10M トークン、マルチモーダル。単一 H100 で動作。
- [Llama 4 Maverick](https://llama.meta.com/) - 400B 総 / 17B アクティブ、128 専門家、1M コンテキスト。マルチモーダルで GPT-4o を上回る。
- [Llama 4 Behemoth](https://llama.meta.com/) - 2T パラメータ（288B アクティブ）。Meta のフロンティア、トップクローズドソースに対抗。
- [Llama 3.3 70B](https://llama.meta.com/) - 強力な命令追従と推論、Llama Community License。

### Sakana AI

- [Sakana RL Conductor](https://venturebeat.com/orchestration/how-sakana-trained-a-7b-model-to-orchestrate-gpt-5-claude-sonnet-4-and-gemini-2-5-pro) - 🆕 **論文 2026-04-27 / Fugu ベータ 2026-04 末～2026-05 初**。Qwen2.5-7B をベースに強化学習で訓練された 7B のオーケストレーター，GPT-5 / Claude Sonnet 4 / Gemini 2.5 Pro などにサブタスクを振り分ける。LiveCodeBench 83.9% / GPQA-Diamond 87.5% で SOTA，1 クエリ平均 ~1.8K トークンと他マルチエージェントアンサンブルより大幅に安い。
- [Sakana Fugu](https://sakana.ai/fugu-beta/) - 🆕 **ベータ 2026-04-24 / 25**。RL Conductor 研究をプロダクト化したマルチエージェントオーケストレーションサービス。OpenAI 互換 API で提供され、**Fugu Mini**（低遅延）と **Fugu Ultra**（高性能）の 2 構成。SWE-Pro、GPQA-D、ALE-Bench で出色の結果。

### Zyphra

- [ZAYA1-8B](https://www.zyphra.com/post/zaya1-8b) - 🆕 **2026-05-06**。アクティブパラメータ <1B の MoE 推論モデル。すべて AMD Instinct MI300X クラスター上で訓練され、Apache 2.0 で Hugging Face にウェイトを公開。Zyphra Cloud でサーバーレス推論も提供。
- [ZAYA1-8B-Diffusion-Preview](https://www.zyphra.com/post/zaya1-8b-diffusion-preview) - 🆕 **2026-05-14**。自己回帰 LLM から変換された初の MoE 拡散言語モデルで、AMD GPU で訓練された初の拡散 LM でもある。1 ステップで 16 トークンを生成し、自己回帰ベースラインに対し **最大 7.7× の推論高速化**。Zyphra の TiDAR レシピ + CCA Attention を採用。

### Mistral AI

- [Mistral Medium 3.5](https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04) - 🆕 **2026-04-29**。Dense 128B のオープンウェイトモデル、256K コンテキスト、Modified MIT ライセンス。指示追従・推論・コーディングを統合。
- [Voxtral TTS](https://www.forbes.com/sites/ronschmelzer/2026/03/26/mistral-releases-open-weight-voice-ai-built-for-speed/) - 🆕 **2026-03-26**。Ministral 3B を土台にした 4B パラメータのオープンウェイト TTS。多言語対応で、音声エージェントのレイテンシ最適化。
- [Mistral Large 3](https://mistral.ai/news/mistral-3) - 675B 総 / 41B アクティブ MoE、256K コンテキスト。マルチモーダルオープンウェイトのフラッグシップ。2025-12 公開。
- [Mistral Medium 3.1](https://mistral.ai/) - 企業向けフロンティア級密モデル。マルチモーダル、128K、80+ プログラミング言語。2025-08 公開。
- [Mistral Small 4](https://mistral.ai/news/mistral-small-4) - 🆕 2026-03 公開。119B 総 / 6B アクティブ。推論・マルチモーダル・コーディングを統合したハイブリッド。
- [Magistral 1.2](https://mistral.ai/) - 🆕 2026 年の推論ファミリー。透過的で多言語の推論。
- [Devstral 2](https://mistral.ai/) - 🆕 2026 年のエージェントコーディングモデル。コーディングエージェントに最適なオープンソース。
- [Codestral](https://mistral.ai/news/codestral) - 22B コード生成モデル、80+ プログラミング言語、32K コンテキスト。2024-05 公開。
- [Pixtral Large](https://mistral.ai/) - 124B マルチモーダル + 1B ビジョンエンコーダ、128K、30+ 高解像度画像処理。
- [Ministral 3B/8B/14B](https://mistral.ai/) - エッジ向けのコンパクトモデル。
- [Mistral Forge](https://mistral.ai/) - 🆕 2026-03 のカスタム LLM 訓練プラットフォーム。

### DeepSeek 🇨🇳

- [DeepSeek-V4-Pro](https://api-docs.deepseek.com/news/news260424) - 🆕 **2026-04-24**。1.6T 総 / 49B アクティブ MoE、1M トークン。MIT。エージェント能力・世界知識・推論でリード。オープンソースベンチマーク首位。
- [DeepSeek-V4-Flash](https://api-docs.deepseek.com/news/news260424) - 🆕 2026-04-24。284B 総 / 13B アクティブ MoE、1M コンテキスト。MIT。コスト効率版。
- [DeepSeek Agent Harness チーム](https://www.scmp.com/tech/big-tech/article/3354113/deepseek-recruits-former-jane-street-engineer-catch-ai-agents-revenue-race) - 🆕 **2026-05-19**。DeepSeek が Jane Street 出身のエンジニアを迎え、DeepSeek V4 を**収益を生む自律型エージェント**に仮定する「AI harness」チームを新設。DeepSeek が素のモデル R&D からエージェント製品化へ軸足を辻りたことを示す初の明確なシグナル。
- [DeepSeek-V3.2](https://www.deepseek.com/) - 2025-12 公開。671B MoE、V3.2 Speciale 推論強化版あり。
- [DeepSeek-R2](https://www.deepseek.com/) - 2026 年の推論モデル。R1 後継、GPT-5・Gemini 3 Pro と競合。
- [DeepSeek-R1](https://www.deepseek.com/) - 2025-01 公開、思考連鎖推論モデル。
- [DeepSeek-Coder-V2](https://github.com/deepseek-ai/DeepSeek-Coder-V2) - GPT-4 と互角のコード生成モデル。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeepseek-ai%2FDeepSeek-Coder-V2&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Alibaba (Qwen) 🇨🇳

- [Qwen 3.7-Max](https://www.scmp.com/tech/big-tech/article/3354212/alibaba-unveils-new-qwen-model-custom-chips-bid-become-chinas-ai-factory) - 🆕 **2026-05-20 — アリババクラウド杭州サミット**。AI エージェントの基盤として設計された新フラッグシップ。エージェント型コーディング、複雑推論、**長い見通しのマルチステップテイスク**に強い。同期に T-Head の **Zhenwu M890** AI アクセラレーターとフルスタック AI 基盤アップグレードも公開。世界中の開発者 / 企業へ順次提供。
- [Qwen 3.7-Max-Preview / Plus-Preview](https://www.scmp.com/tech/tech-trends/article/3354087/alibaba-teases-new-qwen-previews-highest-ranking-chinese-ai-models-arena) - 🆕 **2026-05-18**。杭州サミットの前哨プレビュー。LM Arena においてテキストとビジョンの両方で**中国モデルとして最高スコア**を取得。
- [Qwen3.6-27B](https://qwen.ai/blog?id=qwen3.6-27b) - 🆕 **2026-04-22**。27B 密マルチモーダル。オープン化。エージェントコーディング + 思考文脈保持。
- [Qwen3.6-Max-Preview](https://qwen.ai/) - 🆕 **2026-04-18**。プロプライエタリのフロンティアプレビュー。1M コンテキスト、中国モデルでコーディング首位級。
- [Qwen3.6-35B-A3B](https://qwen.ai/blog?id=qwen3.6-35b-a3b) - 🆕 **2026-04-15**。MoE 35B 総 / 3B アクティブ。Apache 2.0。安定性・実用性の改善。
- [Qwen3.6-Plus](https://qwen.ai/) - 🆕 **2026-04-02**。プロプライエタリのフラッグシップ。トークンあたりの価値が高く、長文脈・ツール呼び出し・エージェント挙動が良好。
- [Tianma (天馬) AI](https://www.alibabacloud.com/) - 🆕 **2026-04-27** ベータ。アリババの画像から動画への生成モデル。キャラクター一貫性と動きの品質が高い。
- [Qwen3.5 Max Pro](https://qwen.ai/) - 2026-04。高性能フラッグシップ。
- [Qwen3.5 Omni Plus](https://qwen.ai/) - 2026-04。テキスト + 画像入力を統合した全モーダル。
- [Qwen3-Max-Thinking](https://qwen.ai/) - アリババ最強の Thinking モデル。1T+ パラメータ。
- [Qwen3.5-Omni](https://qwen.ai/) - 2026-03。完全全モーダル: 言語・視覚・音・動作。113 言語の音声認識、256K コンテキスト。
- [Qwen3-Coder-Next](https://qwen.ai/) - 2026-02。オープンウェイトのコーディングエージェントモデル、MoE 80B 総 / 3B アクティブ。
- [Qwen3 235B-A22B](https://qwen.ai/) - 二重モード推論 MoE。数学・コード・常識推論に強い。
- [Qwen2.5 Coder 32B](https://github.com/QwenLM/Qwen2.5-Coder) - トップクラスのオープンソースコーディングモデル。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FQwenLM%2FQwen2.5-Coder&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### xAI (Grok)

- [Grok 4.3 GA](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-grok-4-3-on-microsoft-foundry-latest-generation-agentic-capabilities/4517096) - 🆕 **2026-05**。Grok 4.3 が Microsoft Foundry と OCI Generative AI で GA。xAI のエージェントワークロード向け旗艦で、ツール呼び出しと長期推論が強化。
- [Grok 4.3 Beta](https://x.ai/) - 🆕 2026-04。推論・コーディングベンチマーク強化。[`2026.4` ベンチマークスナップショット](https://benchlm.ai/) 参照。
- [Grok 4.20](https://x.ai/) - 2026-02。マルチエージェントシステム（Heavy モードで標準 4 + 専門 16）、2M コンテキスト。
- [Grok 4 / 4 Heavy](https://x.ai/) - 2025-07 公開。3T パラメータ。
- [Grok 3 / 3 Mini](https://x.ai/) - 2025-02。"Think Mode" 推論モデルの最初の世代。

### Microsoft (MAI)

- [Microsoft MAI-Code-1-Flash](https://microsoft.ai/news/introducingmai-code-1-flash/) - 🆕 **Build 2026（2026 年 6 月 2 日）**。OpenAI のテクノロジーを使わず一から構築された Microsoft 初の自社基盤モデル。5B パラメータのコーディングモデルで適応的思考時間を備え、GitHub Copilot に展開中。Claude Haiku 4.5 を 4 つの主要コーディングベンチで上回り（SWE-Bench Pro で 51.2% vs 35.2%、16 ポイントリード）、SWE-Bench Verified では最大 60% 少ないトークンで難しいタスクを解く。
- [Microsoft MAI-Thinking-1](https://microsoft.ai/news/microsoft-build-2026-mai-keynote-transcript/) - 🆕 **Build 2026（2026 年 6 月 2 日）**。OpenAI のデータを一切使わず学習した Microsoft 初の自社推論モデル。MAI-Code-1-Flash と同時発表。Microsoft の基盤モデル独立化を象徴。

### Microsoft (Phi)

- [Phi-4-reasoning-vision-15B](https://azure.microsoft.com/en-us/products/phi) - 🆕 2026-03。15B マルチモーダル + 選択的思考連鎖推論。エッジ展開可能。
- [Phi-4](https://azure.microsoft.com/en-us/products/phi) - 14B SLM、ずっと大きいモデルに匹敵する推論力。MIT。
- [Phi-4-mini](https://azure.microsoft.com/en-us/products/phi) - 3.8B 密モデル。128K コンテキスト。推論・数学・コーディング・関数呼び出しで秀逸。
- [Phi-4-multimodal](https://azure.microsoft.com/en-us/products/phi) - 5.6B 初の Phi マルチモーダル（音声 + 視覚 + テキスト）。

### Cohere

- [Command A](https://cohere.com/) - 🆕 2026-04 公開。111B オープンウェイト、256K コンテキスト。エージェント・多言語・コーディング志向。
- [Command R+](https://cohere.com/) - エンタープライズ RAG モデル、128K コンテキスト、10 言語、引用付き grounded generation。
- [Command R](https://cohere.com/) - 経済的な RAG モデル。

### Baidu (ERNIE / 文心) 🇨🇳

- [ERNIE 5.0](https://yiyan.baidu.com/) - 🆕 2026-01 公開。2.4T MoE（1 クエリで <3% 活性化）。ネイティブ全モーダル。LMArena で中国モデル首位。
- [ERNIE 4.5](https://yiyan.baidu.com/) - 2025 年公開のマルチモーダル前任者。中国語・推論に強い。

### Zhipu AI / Z.ai (GLM) 🇨🇳

- [GLM-5.1](https://z.ai/blog/glm-5.1) - 🆕 **2026-04-07**。744B MoE / 40B アクティブ、200K コンテキスト。MIT ライセンス。SWE-Bench Pro で首位。**完全に華為昇騰で訓練**（NVIDIA 不使用）。
- [GLM-5 Reasoning](https://z.ai/) - 🆕 2026-04。BenchLM 85 —— **オープンソース最高スコア**。SWE-Bench Pro で GPT-5.4 と Claude Opus 4.6 を上回る。
- [GLM-5V-Turbo](https://z.ai/) - 🆕 2026-04。ネイティブマルチモーダルエージェント —— 視覚・動画クリップ・テキスト入力。コスト性能バランス。
- [GLM-5](https://z.ai/) - 2026-02 公開。744B パラメータ、先進的なエージェント知性。MIT。
- [GLM-4.7](https://z.ai/) - 2025 年末公開。SWE-Bench で Claude Opus 4 と互角。

### MiniMax 🇨🇳

- [MiniMax-M2.7 (オープンウェイト)](https://www.minimax.io/) - 🆕 2026-04。1M+ の超長文脈ウィンドウ。コーディング・エージェントタスクでトップクラス。
- [MiniMax M2.7（クローズド）](https://venturebeat.com/technology/new-minimax-m2-7-proprietary-ai-model-is-self-evolving-and-can-perform-30-50) - 🆕 **2026-03**。自己進化型のクローズド LLM。エージェントハーネスの構築、メモリ更新、ワークフローの反復改善に最適化され、SWE-bench 系タスクで大幅な性能向上。
- [MiniMax M2.5](https://www.codemotion.com/magazine/ai-ml/minimax-m2-5-low-costs-high-performance/) - **2026-02**。230B パラメータの旗艦モデル。"実世界の生産性" を狙ったコスト効率重視。
- [Hailuo 02](https://aimlapi.com/blog/the-ultimate-guide-to-minimax-models-2026-m2-7-music-2-6-hailuo-video-advanced-tts) - 🆕 **2026-03**。ネイティブ 1080p のテキスト / 画像 → 動画モデル。学習コーパスが大幅に拡張。
- [MiniMax Music 2.6](https://aimlapi.com/blog/the-ultimate-guide-to-minimax-models-2026-m2-7-music-2-6-hailuo-video-advanced-tts) - 🆕 **2026-04**。カバー生成に特化し、低音域の再現性を改善。グローバル beta。
- [MiniMax-M1-80k](https://www.minimax.io/) - オープンウェイトのハイブリッドアテンション推論モデル。456B パラメータ、1M トークン。
- [Hailuo AI (動画)](https://hailuoai.video/) - テキスト/画像から動画への生成、AI アバター・ナレーション・キャラクター一貫性。
- [Kilo Code 統合](https://www.minimax.io/) - 🆕 MiniMax は新しい AI コーディングエディタ Kilo Code のデフォルトモデル。

### Moonshot AI (Kimi) 🇨🇳

- [Kimi K2.6](https://kimi.ai/) - 🆕 **2026-04-20~21**。1T MoE / 32B アクティブ、256K コンテキスト。コーディング強化、長期マルチステップ実行、**最大 1,000 体協調エージェント群**。`thinking.keep="all"` 永続推論対応。OpenClaw v2026.4.20+ のデフォルト。
- [Kimi K2.5](https://kimi.ai/) - 2026 年 1~2 月。1T 総 / 32B アクティブ MoE。ネイティブマルチモーダル、最大 100 並列子エージェント。オープンソース。⚠️ 2026-05-25 サポート終了 —— K2.6 へ移行を。
- [Kimi Code](https://kimi.ai/) - K2.5/K2.6 駆動のプレミアムコーディング層、ターミナル開発者ワークフロー向け。

### ByteDance (Doubao / 豆包) 🇨🇳

- [Doubao 2.0](https://www.taipeitimes.com/News/biz/archives/2026/02/16/2003852382) - 🆕 **2026-02**。実タスク実行に振り切ったエージェント時代向けアップグレード。ByteDance のコンシューマー AI アプリを支える。
- [Seedance 2.0](https://economictimes.indiatimes.com/us/news/seedance-2-0-goes-live-as-bytedances-ai-videos-ignite-china-market-rally/articleshow/128150649.cms) - 🆕 **2026-02**。マルチモーダル・シネマグレード動画生成、2K 解像度、Seedance 1.5 より約 30% 高速。
- [Doubao-Seed-2.0 Pro](https://seed.bytedance.com/) - 🆕 2026-02 公開。フロンティア推論と複雑エージェント。GPT-5.2 と互角でコストは約 90% 低減。
- [Doubao-Seed-2.0 Lite](https://seed.bytedance.com/) - 🆕 一般生産負荷向け。
- [Doubao-Seed-2.0 Code](https://seed.bytedance.com/) - 🆕 ソフトウェア開発: コード生成・デバッグ・レビュー。
- [BAGEL](https://github.com/bytedance-seed/BAGEL) - 🆕 オープンソースのマルチモーダル基盤モデル、テキスト・画像・動画の理解と生成を統合。

### Amazon (Nova)

- [Nova 2 Pro](https://aws.amazon.com/nova/) - 🆕 Amazon の最強推論モデル。テキスト・画像・動画・音声入力。エージェントコーディングと長期計画。
- [Nova 2 Lite](https://aws.amazon.com/nova/) - 🆕 1M コンテキスト + "thinking effort" 調整。
- [Nova 2 Sonic](https://aws.amazon.com/nova/) - 🆕 リアルタイム音声対音声モデル。1M コンテキスト、多言語。
- [Nova Act](https://aws.amazon.com/nova/) - 🆕 ブラウザ Web タスクエージェントサービス（Nova 2 Lite 駆動）。
- [Nova Forge](https://aws.amazon.com/nova/) - 🆕 カスタム Nova モデル訓練サービス。

### NVIDIA (Nemotron)

- [Nemotron 3 Ultra](https://developer.nvidia.com/nemotron) - 🆕 2026-03（GTC）。フロンティア級推論、Blackwell で 5 倍スループット。
- [Nemotron 3 Super](https://developer.nvidia.com/nemotron) - 🆕 2026-03。120B 総 / 12B アクティブ、1M コンテキスト。
- [Nemotron 3 Nano](https://developer.nvidia.com/nemotron) - 経済的な Transformer-Mamba ハイブリッド MoE。
- [Nemotron 3 Nano Omni](https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/) - 🆕 **2026-04-28**。30B-A3B ハイブリッド MoE、ネイティブマルチモーダル。同等オープン omni モデル比 9 倍スループット。MMlongbench-Doc / OCRBenchV2 / WorldSense / DailyOmni / VoiceBench で 6 リーダーボード首位。

### Tencent (Hunyuan) 🇨🇳

- [Hunyuan Hy3 Preview](https://hy.tencent.com/research/hy3) - 🆕 **2026-04-23**。295B 総 / 21B アクティブ MoE、256K コンテキスト。GitHub / Hugging Face / ModelScope / GitCode 同時オープンソース化。"Fast-slow thinking fusion" アーキテクチャ、推論効率 40% 改善。vLLM と SGLang 対応。元宝 / CodeBuddy / QQ / 騰訊文档に統合済み。OpenRouter で無料プレビュー中。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTencent-Hunyuan%2FHunyuan-A13B&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Apple

- [Apple Foundation Models (AFM)](https://machinelearning.apple.com/research/introducing-apple-foundation-models) - Apple Intelligence の中核となるオンデバイス（~3B）+ サーバーモデル。プライバシー優先、オフライン対応。**WWDC 2026（6 月 8 日）**: 次世代 AFM とよりパーソナルな新 Siri は Google Gemini と共同開発。Siri からサードパーティ ChatGPT へ転送する従来動作は段階的に廃止され、Gemini ベースの Apple Intelligence スタックに置き換わる。
- [OpenELM](https://machinelearning.apple.com/research/openelm) - Apple Silicon オンデバイス向けオープンソース効率言語モデル（270M~3B）。

### Samsung

- [Samsung Gauss 2.3](https://www.samsung.com/) - 🆕 Galaxy S26 用オンデバイス AI。Gauss 2.3 Think + Gauss O Flash の 2 バリアント。エージェント機能対応。

### StepFun 🇨🇳

- [Step 3.5 Flash](https://www.scmp.com/tech/article/3342222/punches-above-its-weight-compact-ai-model-chinas-stepfun-outshines-larger-rivals) - 🆕 **2026-02**。約 196B パラメータの軽量推論 + エージェントモデル。より大きな中国製旗艦と互角に渡り合う。

### Baichuan 🇨🇳

- [Baichuan-M3 Plus](https://pandaily.com/baichuan-ai-launches-low-hallucination-medical-model-m3-plus-announces-free-access-program) - 🆕 **2026-01**。証拠に基づく低幻覚率の医療 LLM。中国国内の医療機関向けに無料 API を提供。

### Inflection AI

- [Inflection 2.5 / Pi](https://inflection.ai/) - 共感的会話 AI、感情知能と人間中心インタラクションで知られる。

### 01.AI 🇨🇳

- [Yi-Lightning](https://www.01.ai/) - MoE、RTX 4090 で 200+ tokens/s。中英多言語に強く、Apache 2.0。2024-10 公開。

### 中国科学院 🇨🇳

- [ScienceOne 100 / 磐石100](https://english.cas.cn/newsroom/cas-in-media/202604/t20260429_1158251.shtml) - 🆕 **2026-04-28~29**。中国科学院の科学研究 AI 系統。コアの "ScienceOne" 基盤モデル + 文献コンパス + 革新評価エンジン + 2,000+ ツールエージェントファクトリー。数学・物理・生物・材料・天文・宇宙・地球科学を網羅。50+ CAS 研究所、100+ 研究シナリオで使用。

---

## 🎨 マルチモーダルと生成 AI

*画像・動画・音声・音楽の生成と編集のためのツールとモデル。*

### 画像生成

- [Midjourney V8.1](https://en.wikipedia.org/wiki/Midjourney) - 🆕 **2026-04-30**。2K HD 出力対応、新 Raw モードのオプション追加。V8（3D 生成含む）は 2026 年後半とされている。
- [Flux 2 Pro / Flex / Dev / Klein](https://ropewalk.ai/blog/flux-2-ai-image-generation-2026) - 🆕 **2025-11**。Black Forest Labs の次世代ファミリー。SOTA 画質、マルチリファレンスの一貫性、文字描画の大幅改善。
- [Recraft V4](https://en.wikipedia.org/wiki/Recraft) - 🆕 **2026-02-17**。フルリビルド。プロンプト追従性が大幅改善、編集可能な SVG ベクター出力に対応。
- [Kling IMAGE 3.0](https://klingaio.com/blogs/kling-3-release) - 🇨🇳 🆕 **2026-04-23**。快手のシネマグレード・ネイティブ 4K 画像生成。
- [Nano Banana 2 (Gemini 3 Pro Image)](https://deepmind.google/) - 🆕 Google の透過背景対応に強い画像モデル。OpenClaw image_generate 経由で利用可能。
- [ChatGPT Images 2.0](https://openai.com/) - 🆕 2026-04。無料層対応。ディテール・テキスト理解・反復編集が向上。
- [gpt-image-2](https://openai.com/) - 🆕 OpenAI 最新の画像生成 API。2K/4K 解像度ヒント対応。OpenClaw v2026.4.21 のデフォルト。
- [DALL·E 3](https://openai.com/dall-e-3) - ChatGPT に統合された OpenAI のテキスト → 画像モデル。
- [Midjourney V7](https://www.midjourney.com/) - フォトリアル・芸術風スタイルの第一線。
- [Stable Diffusion 3.5](https://stability.ai/) - 一貫性・プロンプト追従が改善されたオープンソース画像生成。
- [Flux](https://github.com/black-forest-labs/flux) - 💤 **Stale**（2025-07 以降更新なし）。Black Forest Labs のオープンソースモデル。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fblack-forest-labs%2Fflux&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Ideogram 3.0](https://ideogram.ai/) - 画像内のテキスト描画とデザイン志向の生成に強い。
- [Gemini 3 Pro Image](https://deepmind.google/technologies/gemini/) - Gemini 内のネイティブ画像生成。
- [Recraft V3](https://www.recraft.ai/) - プロのデザイナー向け AI 画像生成。
- [Seedance 2.0](https://seed.bytedance.com/) - 🇨🇳 🆕 ByteDance の次世代画像/アニメーション生成 API。

### 動画生成

- [Runway Agent](https://chatlyai.app/news/runway-agent-launch-may-2026) - 🆕 **2026-05-13**。テキストブリーフから完成動画までを一気通貫で仕上げる会話型エージェント。Gen-4 / Aleph を基盤とする。
- [Sora 2 (via Runway)](https://runwayml.com/changelog) - 🆕 OpenAI の Sora アプリは 2026 年 4 月に終了したが、Sora 2 Pro は 2026 年 4 月 7 日以降 Runway に統合済み。
- [Kling VIDEO 3.0](https://kling.ai/) - 🇨🇳 🆕 快手製。リアルな動き・リップシンク・音声同期付きナラティブ。最大 15 秒。
- [Hailuo AI](https://hailuoai.video/) - 🇨🇳 🆕 MiniMax 製。テキスト/画像から動画、AI アバター・ナレーション・キャラクター一貫性。
- [Veo 2](https://deepmind.google/technologies/veo/) - 🆕 Google DeepMind の高忠実度動画生成。
- [Runway Gen-4](https://runwayml.com/) - 🆕 プロ向け動画生成・編集、キャラクター・スタイル一貫性。
- [Pika 2.0](https://pika.art/) - 🆕 シーン・エフェクト制御付きクリエイティブ動画生成。
- [LTX Studio](https://ltx.studio/) - 🆕 AI 駆動シネマティック動画作成プラットフォーム。
- [Tianma (天馬) AI](https://www.alibabacloud.com/) - 🇨🇳 🆕 **2026-04-27** ベータ。アリババの画像→動画モデル。
- [Sora](https://openai.com/sora/) - ⚠️ *2026-04 サービス終了*。OpenAI のテキスト→動画モデル、コストと戦略転換のため停止。

### 音声・音楽

- [ElevenLabs](https://elevenlabs.io/) - AI 音声合成・クローン・対話 AI のリーダー。
- [Suno V4](https://suno.com/) - 🆕 高品質ボーカル・楽器付きの AI 音楽生成。
- [Udio](https://www.udio.com/) - 🆕 商用品質の音楽生成。
- [OpenAI Audio Models](https://openai.com/) - GPT-4o 内のネイティブ音声理解・生成。
- [Stability Audio](https://stability.ai/) - オープンソース音声・音楽生成。
- [Bark](https://github.com/suno-ai/bark) - 💤 **Stale**（2024-08 以降更新なし）。オープンソースのテキスト→音声モデル。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsuno-ai%2Fbark&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ElevenLabs Eleven v3 + ElevenAgents](https://elevenlabs.io/voice-agents) - 🆕 2026 年に "インターネットのオーディオレイヤー" を標榜——70+ 言語対応で感情 Audio Tag を備えた TTS と、AIUC-1 認証を取得した ElevenAgents 音声エージェントプラットフォーム（マルチモーダルメッセージ、会話トピック発見、ツール呼び出し前の音声制御）を提供。
- [Cartesia Sonic 3 / 3.5](https://cartesia.ai/blog/introducing-line-for-voice-agents) - 🆕 **2026**。状態空間モデル系の TTS。first audio 到達まで約 40〜90ms。2026 年 4 月公開の **Line Agents** 音声エージェント基盤を支える。
- [Deepgram Nova-3 + Aura-2 + Flux Multilingual](https://deepgram.com/learn/best-voice-ai-agents-2026-buyers-guide) - 🆕 **2026 年 4 月**。45+ 言語の STT、200ms 未満の TTS、通話中に 10 言語を切り替えできる会話型 STT。
- [MiniMax Music 2.6](https://aimlapi.com/blog/the-ultimate-guide-to-minimax-models-2026-m2-7-music-2-6-hailuo-video-advanced-tts) - 🇨🇳 🆕 **2026 年 4 月**。カバー生成に特化し、低音域の再現性が向上。
- [Voxtral TTS](https://www.forbes.com/sites/ronschmelzer/2026/03/26/mistral-releases-open-weight-voice-ai-built-for-speed/) - 🆕 **2026 年 3 月 26 日**。Mistral の音声エージェント向け、4B オープンウェイト TTS。
- [Hume TADA](https://github.com/HumeAI/tada) - 🆕 **2026 年 3 月 10 日**。Hume AI 初のオープンソース TTS、MIT ライセンス。Text-Acoustic Dual Alignment アーキテクチャでテキストトークンと音声トークンを直接アライン——テストで転記エラーゼロ、同種より約 5× 高速、8 言語対応、スマートフォンで動作。Llama ベース。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHumeAI%2Ftada&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🔗 エージェントプロトコルと標準

*エージェントの相互運用性・ツールアクセス・クロスプラットフォーム通信を可能にするオープン標準。*

### Model Context Protocol (MCP)

- [MCP Specification](https://modelcontextprotocol.io/) - 🆕 "AI 用の USB-C" —— Anthropic 製、LLM をツール・データソースに接続するオープンプロトコル。2025-12 に Linux Foundation 傘下の Agentic AI Foundation へ寄贈。
- [MCP 2026-07 Release Candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) - 🆕 **2026-05 公開、正式版は 2026-07-28 予定**。MCP 次月メジャーリビジョンの RC：**ステートレスプロトコルコア**（スケーラビリティ・サーバ実装の簡素化）、**拡張フレームワーク**、サーバ側レンダリング UI をサポートする **MCP Apps**、Tasks の拡張へのグラデュエート、OAuth / OpenID Connect と整合した認可強化を含む。
- [MCP Servers](https://github.com/modelcontextprotocol/servers) - MCP サーバーの公式リファレンス実装集。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Fservers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - 公式 TypeScript SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Ftypescript-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - 公式 Python SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Fpython-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [mcp.so](https://mcp.so/) - 🆕 MCP サーバー・ツールのコミュニティディレクトリ。
- [mcp-gateway](https://github.com/Zijian-Ni/mcp-gateway) - MCP 接続のルーティングと管理を行うゲートウェイ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fmcp-gateway&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Agent-to-Agent Protocol (A2A)

- [A2A Protocol](https://github.com/google/A2A) - 🆕 Google が主導するエージェント間通信のオープン標準。フレームワーク不問でエージェントの発見・委譲・協調を可能にする。Linux Foundation 統治、150+ パートナー。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle%2FA2A&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [A2A Course (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/a2a-the-agent2agent-protocol/) - 🆕 A2A でマルチエージェントシステムを構築する無料コース。

### その他の標準

- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - 🆕 [2026-04-15 大型アップデート](https://openai.com/index/the-next-evolution-of-the-agents-sdk/): ネイティブサンドボックス実行、第一級 MCP 統合、サブエージェント / handoff パターン、Codex 風ファイルシステムツール。プロダクション級マルチエージェントワークフロー。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fopenai-agents-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agentic AI Foundation](https://www.linuxfoundation.org/) - 🆕 Anthropic、Block、OpenAI が共同設立した Linux Foundation のオープンエージェント標準統治基金。
- [Coinbase Base MCP](https://fortune.com/2026/05/26/coinbase-pushes-further-into-ai-payments-with-new-mcp-for-base-network/) - 🆕 **2026 年 5 月 26 日**。Coinbase が Base ブロックチェーン用 MCP サーバーを公開。Claude / Cursor / ChatGPT エージェントが暗号資産の取引やレンディングをオンチェーンで実行可能。大手取引所が初めて公開した、自律オンチェーン取引向けの MCP エンドポイント。
- [Robinhood Agentic Trading MCP](https://robinhood.com/us/en/newsroom/robinhood-is-now-open-to-agents/) - 🆕 **2026 年 5 月 27 日**（ベータ）。米国主要証券会社で初めて MCP 経由で株式取引を AI エージェントに開放。Agent（Claude / Codex / Cursor）は全口座への読み取りアクセスのみ、取引実行は隔離された Agentic 口座内に限定。全取引プッシュ通知 + ワンタップ切断スイッチ。

---

## 🏗️ エージェントフレームワーク

*自律 AI エージェントを構築するためのフレームワークとライブラリ。*

- [Koog 1.0](https://github.com/JetBrains/koog) - 🆕 **2026-05-28 · KotlinConf 2026**。JetBrains による **Kotlin + Java** 向けオープンソースエージェントフレームワークが安定版 1.0 に到達し、1 年間の API 安定保証付き。Kotlin Multiplatform でのクロスデプロイ（JVM / Android / iOS / JS / WASM）、ラッパー不要の Java 相互運用、Android ローカル LiteRT、全ターゲットでの OpenTelemetry、グラフベースワークフロー、Spring Boot / Ktor 連携、OpenAI / Anthropic / Google / Bedrock プロバイダーをサポート。Apache-2.0。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FJetBrains%2Fkoog&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangChain](https://github.com/langchain-ai/langchain) - LLM を使った文脈認識推論アプリの基盤。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangGraph](https://github.com/langchain-ai/langgraph) - エージェントを状態を持つマルチアクターのグラフとしてモデル化。v0.3.19（2026-04-27）: プリビルトエージェントが `langgraph-prebuilt` に分離 —— Supervisor / Swarm / LangMem / Trustcall。エージェントワークフローのプロダクション標準。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flanggraph&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [CrewAI](https://github.com/crewAIInc/crewAI) - ロールプレイ型自律エージェントチームのオーケストレーションフレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FcrewAIInc%2FcrewAI&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/) - 🆕 AutoGen + Semantic Kernel を統合した新フレームワーク。マルチエージェント + エンタープライズ機能。2026 Q1 GA。
- [AutoGen](https://github.com/microsoft/autogen) - Microsoft のマルチエージェント会話フレームワーク（Microsoft Agent Framework に統合）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fautogen&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Google Agent Development Kit (ADK)](https://github.com/google/adk-python) - 🆕 Gemini + Vertex AI と密接に統合したモジュラーフレームワーク。階層エージェント構成。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle%2Fadk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - 🆕 [2026-04-15 進化](https://openai.com/index/the-next-evolution-of-the-agents-sdk/) —— ネイティブサンドボックス、MCP ネイティブ、サブエージェント handoff、Codex 風ファイル操作。プロダクション級マルチエージェント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fopenai-agents-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MetaGPT](https://github.com/geekan/MetaGPT) - 🇨🇳 LLM に SOP ソフトウェアチームの役割（PM / アーキテクト / エンジニア）を割り当てる多エージェント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgeekan%2FMetaGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Mastra](https://github.com/mastra-ai/mastra) - 🆕 TypeScript 優先のエージェントフレームワーク、ワークフロー駆動 + オブザーバビリティ内蔵。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmastra-ai%2Fmastra&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentGPT](https://github.com/reworkd/AgentGPT) - 📦 **Archived**（2025-04）。ブラウザでエージェントを構成・展開。第一波の代表、歴史的参照のみ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Freworkd%2FAgentGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [BabyAGI](https://github.com/yoheinakajima/babyagi) - LLM でタスクを作成・優先順位付け・実行する AI タスクマネジメント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fyoheinakajima%2Fbabyagi&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) - 💤 **Stale**（2025-01 以降更新なし）。オープンソース自律エージェントフレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTransformerOptimus%2FSuperAGI&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) - LLM 技術をアプリに統合。C# / Python / Java。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fsemantic-kernel&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Phidata (Agno)](https://github.com/phidatahq/phidata) - メモリ・知識・ツール・推論つきマルチモーダルエージェント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fphidatahq%2Fphidata&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [DSPy](https://github.com/stanfordnlp/dspy) - "プロンプトを書くのではなくプログラミングする" 言語モデルフレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstanfordnlp%2Fdspy&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenClaw](https://github.com/openclaw/openclaw) - 🆕 スキル・メモリ・マルチチャネルメッセージング・Dreaming（3 段階メモリ統合）・Canvas/A2UI・ACP コーディング harness 統合・Standing Orders を備えた個人向け AI エージェントプラットフォーム。**v2026.5.12**（2026-05-14）で Opus 4.7・Kimi K2.6・`/think xhigh`に加え、ネイティブモデルアイデンティティ注入、隔離 Telegram polling worker、MEMORY.md 自動コンパクション、Protected Config Paths に対応。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenclaw%2Fopenclaw&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Dify](https://github.com/langgenius/dify) - 🇨🇳 ビジュアルエージェントビルダー付きオープンソース LLM アプリ開発プラットフォーム。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flanggenius%2Fdify&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Haystack Agents](https://github.com/deepset-ai/haystack) - エージェント型パイプラインのエンドツーエンド LLM フレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeepset-ai%2Fhaystack&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vellum AI](https://www.vellum.ai/) - 🆕 プロダクション級プロプライエタリ SaaS：プロンプト構築・評価・バージョニング・オブザーバビリティ。
- [FastAgency](https://github.com/airtai/fastagency) - 🆕 高速推論 + プロダクションスケーリングフレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fairtai%2Ffastagency&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Rasa](https://github.com/RasaHQ/rasa) - 強力な意図認識と対話管理のオープンソース対話 AI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FRasaHQ%2Frasa&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Lindy](https://www.lindy.ai/) - 🆕 ビジネスユーザー向けノーコードエージェント、ビジュアルワークフロービルダー。
- [Octomind](https://github.com/muvon/octomind) - 🆕 Rust ベースのオープンソース AI エージェントランタイム。モデル不問（13+）、コミュニティ製の専門エージェント（開発・医療・法律・DevOps）、ランタイム自己拡張対応 MCP、ゼロコンフィグ。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmuvon%2Foctomind&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsoft AI Agent Governance Toolkit](https://www.helpnetsecurity.com/2026/04/03/microsoft-ai-agent-governance-toolkit/) - 🆕 **2026-04-03**。LangChain や AutoGen などフレームワーク横断でランタイムセキュリティポリシーを強制するオープンソースツールキット。
- [Bernstein](https://github.com/sipyourdrink-ltd/bernstein) - 🆕 40+ の CLI 型コーディングエージェント（Claude Code / Codex / Gemini CLI / Cursor / Aider など）を一つにまとめる Python オーケストレーター。LLM は事前プランニング一回だけ使い、スケジューリング・git worktree 隔離・品質ゲート・HMAC 連鎖監査は決定論的。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsipyourdrink-ltd%2Fbernstein&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Genkit Middleware](https://developers.googleblog.com/announcing-genkit-middleware-intercept-extend-and-harden-your-agentic-apps/) - 🆕 **2026-05-14**。Google の OSS エージェントフレームワーク Genkit にミドルウェアを追加。generate / model / tool の 3 階層でコンポーザブルなフックを提供 —— 指数バックオフでのリトライ、モデルフォールバック、ツールタその人手承認ゲート、SKILL.md スキル注入、スコープを限定したファイルアクセス。TS / Go / Dart、Python 予定。
- [LlamaIndex ↔ Google Agents API 連携](https://www.kucoin.com/news/flash/google-launches-agents-api-llama-index-integrates-llamaparse-for-unstructured-document-processing) - 🆕 **2026-05-20**。LlamaIndex が Google の新 Agents API 向けのテンプレートを公開し、サンドボックスの Linux 環境上で **LlamaParse** / **LiteParse** を提供して非構造化文書を処理。同リリースにはサンドボックスランタイム **Sandboxed-Lit** とエージェント向け初の OCR ベンチマーク **ParseBench** も含まれる。
- [Microsoft Agent 365](https://techcommunity.microsoft.com/blog/agent-365-blog/what%E2%80%99s-new-in-agent-365-may-2026/4516340) - 🆕 **2026 年 5 月 1 日 GA**。AI エージェント向けの企業級可観測性 + ガバナンス + セキュリティ基盤。2026 年 5 月アップデートで、エージェント向け SASE、脅威検知 / ブロック、エージェント脅威ハンティングのワークフローを追加。
- [Ontheia](https://github.com/Ontheia/ontheia) - セルフホスト型のオープンソース AI エージェントプラットフォーム。マルチプロバイダ（Claude / OpenAI / Gemini / Ollama）、MCP ネイティブ、ビジュアル workflow 自動化のための Chain Engine、長期メモリ（pgvector）、マルチユーザ RBAC、アーキテクチャレベルでの GDPR 適合。AGPL-3.0。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOntheia%2Fontheia&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Coze Studio](https://github.com/coze-dev/coze-studio) - 🆕 🇨🇳 ByteDance のオープンソース AI エージェント開発プラットフォーム——オールインワンのビジュアルビルダーで作成・デバッグ・デプロイを一括管理。Apache-2.0、20K+ stars。Coze.com のオープンソース版。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🛠️ エージェント IDE とビジュアルビルダー

*コードを書かずに（または最小限で）エージェントワークフローを設計・デバッグ・出荷するためのビジュアル環境。*

- [LangGraph Studio](https://www.langchain.com/langgraph) - LangGraph エージェントのビジュアルデバッガとトレース検査。状態のステップ実行、ターンの再生、メッセージの途中編集が可能。
- [Dify](https://github.com/langgenius/dify) - 🇨🇳 ドラッグ&ドロップのエージェントワークフロービルダー付きオープンソース LLM アプリ開発。プロダクション利用が主流。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flanggenius%2Fdify&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agenta](https://github.com/agenta-ai/agenta) - 🆕 プロンプトプレイグラウンド・プロンプト管理・評価実行・オブザーバビリティを統合したオープンソース LLMOps プラットフォーム。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagenta-ai%2Fagenta&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vellum AI](https://www.vellum.ai/) - クローズドソース SaaS。
- [Cozeloop](https://github.com/coze-dev/cozeloop) - 🇨🇳 🆕 ByteDance の Coze チームによるオープンソースのエージェント最適化プラットフォーム。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcozeloop&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Restack](https://www.restack.io/) - 永続化エージェントランタイム + ビジュアルワークフローエディタ（Temporal 風 replay）。オープン例: [restackio/examples-python](https://github.com/restackio/examples-python)。
- [Bisheng](https://github.com/dataelement/bisheng) - 🇨🇳 オープンエンタープライズ LLM DevOps プラットフォーム: ワークフローエディタ・RAG・エージェントオーケストレーション・ファインチューニング・データセット管理・オブザーバビリティ。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdataelement%2Fbisheng&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [n8n](https://github.com/n8n-io/n8n) - エージェントキャンバスとして人気の汎用ビジュアルワークフロー自動化 —— 400+ 連携 + ネイティブ AI ノード。Fair-code ライセンス。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fn8n-io%2Fn8n&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Mastra](https://github.com/mastra-ai/mastra) - 🆕 強い思想を持つ TypeScript エージェントフレームワーク。RAG、可観測性、MCP、ビジュアル workflow ビルダーを内蔵。21K+ stars。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmastra-ai%2Fmastra&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [VoltAgent](https://github.com/VoltAgent/voltagent) - 🆕 エンドツーエンドの TypeScript AI エージェントエンジニアリングプラットフォーム。メモリ、RAG、guardrail、MCP、音声、workflow を一括提供。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FVoltAgent%2Fvoltagent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Coze Studio](https://github.com/coze-dev/coze-studio) - 🆕 🇨🇳 ByteDance Coze チームのオープンソースエージェント IDE / ビジュアルビルダー。ドラッグ&ドロップワークフロー、プラグインマーケットプレイス、デバッグパネル、マルチ LLM プロバイダー対応。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🧠 エージェントメモリ

*エージェントに永続メモリと文脈管理を与えるシステム。*

- [Letta (MemGPT)](https://github.com/letta-ai/letta) - 長期メモリとカスタムツールを持つ LLM サービスを作成。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fletta-ai%2Fletta&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Mem0](https://github.com/mem0ai/mem0) - LLM アプリ用の自己改善型メモリ層。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmem0ai%2Fmem0&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Zep](https://github.com/getzep/zep) - AI アシスタント・エージェント向け長期メモリ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgetzep%2Fzep&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [agent-memory](https://github.com/Zijian-Ni/agent-memory) - セッション横断の文脈永続化を実現する軽量エージェントメモリフレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fagent-memory&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangMem](https://github.com/langchain-ai/langmem) - 🆕 LangGraph 0.3.19（2026 年 4 月）からスピンアウト。エージェント向けの長期エピソード記憶＋手続き記憶プリミティブ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangmem&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Motorhead](https://github.com/getmetal/motorhead) - 💤 **Stale**（2025-07 以降更新なし）。LLM 用メモリ・文脈管理サーバー。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgetmetal%2Fmotorhead&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ChromaDB](https://github.com/chroma-core/chroma) - AI ネイティブのオープンソース埋め込みデータベース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fchroma-core%2Fchroma&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cognee](https://github.com/topoteretes/cognee) - グラフ + LLM + ベクトル検索による決定論的 LLM 出力。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftopoteretes%2Fcognee&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangGraph Memory](https://github.com/langchain-ai/langgraph) - 🆕 状態管理エージェントワークフロー用の組み込み永続化とチェックポイント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flanggraph&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Graphiti](https://github.com/getzep/graphiti) - 🆕 時間意識を備えたエージェントメモリ用知識グラフ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgetzep%2Fgraphiti&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude Managed Agents Memory](https://platform.claude.com/docs/en/release-notes/overview) - 🆕 **2026-04-23**（パブリックベータ）。Claude Managed Agents 用 Anthropic 永続メモリ機能。読み書きメモリストアをエージェントのファイルシステムにマウントしてセッション間で情報を保持。
- [Mem0g (graph variant)](https://mem0.ai/blog/state-of-ai-agent-memory-2026) - 🆕 Mem0 のグラフ強化派生で、マルチホップ質問に強い。2026 年初時点で 21+ のフレームワーク統合あり。
- [OpenViking](https://github.com/volcengine/OpenViking) - 🆕 🇨🇳 ByteDance Volcengine のオープンソース・エージェント用コンテキストデータベース（OpenClaw などに対応）。メモリ・リソース・スキルをファイルシステムパラダイムで統合管理し、階層的コンテキスト配信と自己進化を実現。AGPL-3.0、25K+ stars。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvolcengine%2FOpenViking&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ReMe](https://github.com/agentscope-ai/ReMe) - 🆕 🇨🇳 Alibaba AgentScope チームのエージェント用メモリ管理キット——ファイルベース＋ベクトルベースのメモリを組み合わせ、コンテキストウィンドウの制約とステートレスセッションの 2 つの課題を解決。Apache-2.0。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentscope-ai%2FReMe&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [taOSmd](https://github.com/jaylfc/taosmd) - 🆕 ⚠️ **Unverified.** ローカル優先・追記型トランスクリプトに基づくエージェントメモリ。型付きの時系列ナレッジグラフ（修正後の新事実が旧事実を上書き）と、ベクトル + BM25 のハイブリッド検索を組み合わせる。小型ローカルモデル向けにチューニングされ、完全オフライン（8 GB の SBC で動作）。作者報告で LongMemEval-S の end-to-end Judge 97%。単独メンテナで監査時点 44 stars、ベンチマークは `docs/benchmarks.md` から再現可能。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fjaylfc%2Ftaosmd&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🔌 ツールと API 連携

*エージェントを外部サービス・API に接続するプロトコルとツール。*

- [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol/servers) - AI モデルを外部ツール・データソースに接続するオープンプロトコル。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Fservers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [mcp-gateway](https://github.com/Zijian-Ni/mcp-gateway) - MCP プロトコル接続のルーティングと管理を行うゲートウェイ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fmcp-gateway&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Composio](https://github.com/ComposioHQ/composio) - AI エージェント向け統合プラットフォーム —— マネージド認証付き 150+ ツール。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FComposioHQ%2Fcomposio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Toolhouse](https://toolhouse.ai/) - AI ツール利用のクラウドインフラ —— ツールの保存・管理・実行。
- [LangChain Tools](https://github.com/langchain-ai/langchain) - LangChain エコシステム内の広範なツール統合。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Arcade AI](https://github.com/ArcadeAI/arcade-ai) - AI エージェント・アシスタント用ツール呼び出しプラットフォーム。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FArcadeAI%2Farcade-ai&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [E2B](https://github.com/e2b-dev/e2b) - AI エージェント用オープンソースクラウドランタイム —— セキュアなサンドボックス環境。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fe2b-dev%2Fe2b&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Browser Use](https://github.com/browser-use/browser-use) - AI エージェント用のブラウザ自動化。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowser-use%2Fbrowser-use&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Firecrawl](https://github.com/mendableai/firecrawl) - 🆕 ウェブサイトを LLM-ready なデータに変換。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmendableai%2Ffirecrawl&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Crawl4AI](https://github.com/unclecode/crawl4ai) - 🆕 LLM フレンドリーなオープンソースクローラ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Funclecode%2Fcrawl4ai&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Stagehand](https://github.com/browserbase/stagehand) - 🆕 Browserbase 製の AI 駆動ブラウザ自動化フレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowserbase%2Fstagehand&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentQL](https://www.agentql.com/) - 🆕 AI エージェントが意味的にウェブページと対話するためのクエリ言語。
- [StackOne](https://www.stackone.com/) - 🆕 HR・CRM・ATS プラットフォーム横断の統一 API。
- [The Colony](https://thecolony.cc) - ⚠️ **Unverified**。エージェント間のソーシャルネットワークと REST API を謳う。組織と SDK リポジトリは <30 日、すべて 0~2 star、単独メンテナで、同じ申請が 15+ awesome リストに並列投稿された —— 可視性のための掲載のみ、利用前に評価のこと。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTheColonyCC%2Fcolony-sdk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AWS MCP Server](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/) - 🆕 **2026 年 5 月 6 日 GA**。AWS マネージドの MCP サーバ。コーディングエージェントが任意の AWS API を安全かつ監査可能に呼び出せるようにし、複数ステップ操作はサンドボックス Python で実行。従来の "agent SOP" を agent skills で置き換え。AWS 純正。
- [Google Workspace MCP Server](https://workspaceupdates.googleblog.com/2026/05/agent-tools-and-security-updates-for-workspace-developers.html) - 🆕 **2026 年 5 月 1 日から順次展開**。Workspace ネイティブの MCP サーバ。Gmail / Drive / Calendar / Docs / Sheets を MCP クライアントに公開し、OAuth スコープは管理者が制御、監査ログ付き。
- [iManage MCP Server](https://imanage.com/resources/resource-center/news/mcp-server-available-broader-ai-ecosystem/) - 🆕 **2026 年 5 月 14 日**。iManage ナレッジワーク基盤のネイティブ MCP エンドポイント。カスタム連携なしで AI クライアントから iManage ドキュメントを安全に読み書きできる。法務 / プロフェッショナルサービス系 SaaS として初の公式 MCP サーバ。
- [Power Platform Canvas Authoring MCP Server](https://www.microsoft.com/en-us/power-platform/blog/2026/05/14/whats-new-in-power-platform-may-2026-feature-update/) - 🆕 **2026 年 5 月 14 日**。Microsoft Power Platform が Canvas Apps のオーサリングを MCP サーバとして公開。Copilot / Claude Code が自然言語で InfoPath → Canvas Apps 移行を駆動できる。
- [Coinbase AgentKit](https://github.com/coinbase/agentkit) - 🆕 「すべての AI エージェントにウォレットを」。Coinbase 公式 SDK でエージェントに EVM ウォレットを付与し、API への支払い、トランザクション署名、Base / Ethereum 上での取引を可能にする。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoinbase%2Fagentkit&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Bifrost (Maxim AI)](https://github.com/maximhq/bifrost) - 🆕 オープンソースのエンタープライズ AI ゲートウェイ（Apache-2.0）—— 1000+ モデル、適応的ロードバランサ、クラスタモード、ガードレール、PKCE 付き OAuth 2.0、ゲートウェイ層でのプロンプトインジェクション防御；5k RPS で <100µs オーバーヘッド。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmaximhq%2Fbifrost&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Anthropic クリエイティブツールコネクター](https://www.anthropic.com/news/claude-for-creative-work) - 🆕 **2026 年 4 月 28 日**。クリエイティブソフト向けの MCP ベース Claude コネクター 9 種：Adobe（Creative Cloud 50+ ツール、Photoshop / Premiere / Express を含む）、Blender、Autodesk Fusion、Ableton、Splice、Canva Affinity、SketchUp、Resolume。MCP オープン標準上に構築されているため、他の LLM クライアントからも直接利用可能。

---

## 🧪 エージェントサンドボックスと計算分離

*エージェントが生成したコードや shell コマンドをホストを危険にさらさず実行するセキュアなランタイム。エージェントを自由に動かす段階で必須となる重要インフラ。*

- [E2B](https://github.com/e2b-dev/E2B) - AI 生成コード用のオープンソースセキュアクラウドサンドボックス。OpenAI Agents SDK の実行層に採用。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fe2b-dev%2FE2B&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Daytona](https://github.com/daytonaio/daytona) - 🆕 AI 生成コードを実行するセキュアで弾力的なインフラ。エージェントタスク毎に隔離された開発環境を起動。AGPL-3.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdaytonaio%2Fdaytona&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Modal](https://modal.com/) - エージェント計算・GPU ジョブ・サンドボックス Python に人気のサーバーレスクラウド。`modal-client` が公式 SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodal-labs%2Fmodal-client&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsandbox](https://github.com/superradcompany/microsandbox) - 🆕 AI エージェント向けローカル・プログラマブル microVM サンドボックス —— クラウド非依存でローカル機にセキュアなコード実行。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsuperradcompany%2Fmicrosandbox&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SandboxFusion](https://github.com/bytedance/SandboxFusion) - 🇨🇳 ByteDance のエージェント・モデル評価パイプライン用多言語コード実行サンドボックス。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbytedance%2FSandboxFusion&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Northflank](https://northflank.com/) - エージェントランタイムバックエンドとして使われる汎用コンテナ PaaS（タスク毎エフェメラル環境 + GPU プール）。
- [Firecracker](https://github.com/firecracker-microvm/firecracker) - E2B、Daytona、ほとんどのエージェントサンドボックスの基盤となる microVM カーネル。自前のサンドボックスを組むときの基本要素。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ffirecracker-microvm%2Ffirecracker&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangSmith Sandboxes](https://www.langchain.com/blog/interrupt-2026-overview) - 🆕 **2026 年 5 月（Interrupt 2026）**。エージェント向けのホスト型セキュアコード実行環境——ファイルシステム、shell、パッケージマネージャ、永続状態、ネットワーク境界を提供。LangChain の Interrupt 2026 リリースで LangSmith Engine、Managed Deep Agents と同時に発表。

---

## 🛡️ エージェントセキュリティ

*プロンプトインジェクション・データ漏洩・悪用から AI エージェントを守るツールとフレームワーク。*

- [prompt-firewall](https://github.com/Zijian-Ni/prompt-firewall) - LLM プロンプト用ファイアウォール —— インジェクション攻撃を検出・遮断。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fprompt-firewall&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LLM Guard](https://github.com/protectai/llm-guard) - LLM 対話用のセキュリティツールキット —— 入出力スキャナ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fprotectai%2Fllm-guard&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Rebuff](https://github.com/protectai/rebuff) - 📦 **Archived**（2024-08）。自己強化型プロンプトインジェクション検出器。歴史的参照のみ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fprotectai%2Frebuff&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Guardrails AI](https://github.com/guardrails-ai/guardrails) - LLM 出力の検証・修正にガードレールを追加。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fguardrails-ai%2Fguardrails&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) - LLM ベース対話システムにプログラマブルガードレールを追加するツールキット。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNVIDIA%2FNeMo-Guardrails&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vigil](https://github.com/deadbits/vigil-llm) - 💤 **Stale**（2024-01 以降更新なし）。LLM セキュリティスキャナ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeadbits%2Fvigil-llm&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Lakera Guard](https://www.lakera.ai/) - エンタープライズ級 AI セキュリティプラットフォーム。
- [Garak](https://github.com/NVIDIA/garak) - NVIDIA の LLM 脆弱性スキャナ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNVIDIA%2Fgarak&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Invariant Guardrails](https://github.com/invariantlabs-ai/invariant) - 🆕 AI エージェント用ランタイムガードレール —— ポリシー強制と安全チェック。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Finvariantlabs-ai%2Finvariant&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Prompt Armor](https://promptarmor.com/) - 🆕 リアルタイム検出のエンタープライズプロンプトインジェクション保護。
- [Descope MCP Auth](https://www.descope.com/) - 🆕 MCP サーバーセキュリティ用の認証・認可レイヤ。
- [AgentDojo](https://github.com/ethz-spylab/agentdojo) - 🆕 ETH チューリッヒの研究ベンチマーク。ツール使用 LLM エージェントへのプロンプトインジェクション攻撃と防御を評価。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fethz-spylab%2Fagentdojo&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ModelScan](https://github.com/protectai/modelscan) - ML モデル重みファイル（Pickle、PyTorch、TF）のシリアライズ攻撃をスキャン。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fprotectai%2Fmodelscan&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [PyRIT](https://github.com/Azure/PyRIT) - Microsoft の生成 AI 用自動レッドチームフレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAzure%2FPyRIT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAMPART](https://github.com/microsoft/RAMPART) - 🆕 **2026 年 5 月 20 日**。Microsoft が公開した、agentic AI 向けの pytest ネイティブな安全性 / セキュリティテストフレームワーク。PyRIT と相補的な開発者向けホワイトボックス——クロスプロンプトインジェクションのプローブ、良性失敗アサーション、ハームカテゴリ網羅、統計しきい値（例：80%+ の試行で安全）。CI/CD に直接組み込める。MIT。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2FRAMPART&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Clarity (Microsoft)](https://www.microsoft.com/en-us/security/blog/2026/05/20/introducing-rampart-and-clarity-open-source-tools-to-bring-safety-into-agent-development-workflow/) - 🆕 **2026 年 5 月 20 日**。RAMPART の姉妹ツール。AI エージェントの構造化デザインレビューを支援し、コード着手前に意図・リスク・挙動の "living artifact" を生成。Microsoft AI Red Team の社内プラクティスをオープンソース化。
- [MCP Gateway & Registry](https://github.com/agentic-community/mcp-gateway-registry) - 🆕 エンタープライズ対応の MCP ゲートウェイ＆レジストリ。OAuth 認証、動的ツール発見、監査トレイル、Keycloak / Entra との統合で AI 開発ツールを集中管理。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentic-community%2Fmcp-gateway-registry&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Nobulex](https://github.com/arian-gogani/nobulex) - ⚠️ **未検証。** AI エージェント挙動の暗号学的レシート（Ed25519 二重署名、ハッシュチェーン監査ログ）。MIT。双方向レシートのプリミティブが Microsoft Agent Governance Toolkit に [マージ済み](https://github.com/microsoft/agent-governance-toolkit/pull/1333)（PR #1302、#1333）。同一の投稿が 15+ の awesome list に同時送付され、投稿者の "npm 月 4,500 ダウンロード" の主張は registry 実数（`@nobulex/mcp-server` ≒ 月 19）と乖離。Microsoft 採用実績を踏まえて可視性のために掲載するが、依存する前に各自で評価のこと。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Farian-gogani%2Fnobulex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🔍 RAG とナレッジ

*エージェント用の検索拡張生成と知識管理システム。*

- [LlamaIndex](https://github.com/run-llama/llama_index) - LLM アプリ用データフレームワーク —— プライベートデータの取り込み・構造化・アクセス。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Frun-llama%2Fllama_index&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangChain Retrievers](https://github.com/langchain-ai/langchain) - LangChain 内のリトリーバとドキュメントローダー集合。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Haystack](https://github.com/deepset-ai/haystack) - エンドツーエンド RAG。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeepset-ai%2Fhaystack&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Unstructured](https://github.com/Unstructured-IO/unstructured) - ドキュメント前処理と抽出。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FUnstructured-IO%2Funstructured&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Weaviate](https://github.com/weaviate/weaviate) - オープンソースベクトルデータベース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fweaviate%2Fweaviate&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Qdrant](https://github.com/qdrant/qdrant) - Rust 製の高性能ベクトル検索。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fqdrant%2Fqdrant&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Milvus](https://github.com/milvus-io/milvus) - 大規模ベクトルデータベース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmilvus-io%2Fmilvus&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Pinecone](https://www.pinecone.io/) - マネージドベクトルデータベース SaaS。
- [Chroma](https://github.com/chroma-core/chroma) - AI ネイティブオープンソースベクトルデータベース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fchroma-core%2Fchroma&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vanna](https://github.com/vanna-ai/vanna) - 📦 **Archived**（2026-02）。RAG-for-SQL: 自然言語でデータベースと対話。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvanna-ai%2Fvanna&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LightRAG](https://github.com/HKUDS/LightRAG) - 🇨🇳 香港大学 HKUDS のグラフ型 RAG。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2FLightRAG&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Docling](https://github.com/DS4SD/docling) - IBM のドキュメント変換ツール（PDF / DOCX / HTML 等）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FDS4SD%2Fdocling&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Kotaemon](https://github.com/Cinnamon/kotaemon) - オープンソース RAG UI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FCinnamon%2Fkotaemon&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [R2R](https://github.com/SciPhi-AI/R2R) - エンタープライズグレードのエンドツーエンド RAG サービス。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSciPhi-AI%2FR2R&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAGFlow](https://github.com/infiniflow/ragflow) - 🇨🇳 深いドキュメント理解 RAG。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Finfiniflow%2Fragflow&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Morphik](https://github.com/morphik-org/morphik-core) - 🆕 表や図を含む文書向けのマルチモーダル RAG エンジン。複雑な PDF 処理の LlamaIndex 代替として 2026 年に急浮上。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmorphik-org%2Fmorphik-core&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cognee](https://github.com/topoteretes/cognee) - 🆕 エージェントが文書を取り込む過程でナレッジグラフを構築するメモリ + 推論エンジン。2026 年の "長期リサーチエージェント" 系スタックの定番。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftopoteretes%2Fcognee&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAG-Anything](https://github.com/HKUDS/RAG-Anything) - 🆕 香港大学データサイエンス研究室のオールインワン・マルチモーダル RAG フレームワーク。LightRAG を基盤に構築。テキストとマルチモーダルの並列パイプライン；テキスト・図・表・数式が混在する文書も検索可能。MIT、21K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2FRAG-Anything&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 💻 コーディングエージェント

### ターミナル / CLI エージェント

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - 端末で動く Anthropic のエージェント型コーディングツール。Opus 4.7 + `/think xhigh`。SWE-bench 80.9%。
- [Codex CLI](https://github.com/openai/codex) - OpenAI 製のオープンソースターミナルコーディングエージェント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fcodex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Codex Security](https://developers.openai.com/codex/changelog) - 🆕 **2026 年 3 月**。ソフトウェア脆弱性を発見・修正するアプリケーションセキュリティエージェント。OSS メンテナは Codex-for-OSS プログラム経由で利用可能。
- [Aider](https://github.com/Aider-AI/aider) - Git アウェアなターミナル AI ペアプログラミングパートナー。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAider-AI%2Faider&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Goose](https://github.com/block/goose) - Block 製のオープンソースエージェントコーディング CLI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fblock%2Fgoose&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) - 🆕 Google のターミナル特化コーディングエージェント。大規模コンテキストのリファクタが得意。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle-gemini%2Fgemini-cli&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenCode](https://github.com/opencode-ai/opencode) - 🆕 ターミナル向けのオープンソース AI コーディングエージェント。ネイティブ TUI 搭載。OpenAI、Claude、Gemini、Ollama（ローカル）をサポートし、LSP によるコード解析にも対応。Go 言語製、MIT。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopencode-ai%2Fopencode&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Grok Build](https://x.ai/news/grok-build-cli) - 🆕 **2026 年 5 月 14 日（early beta）**。xAI が出した **grok-code-fast-1** ベースの agentic CLI コーディングエージェント。サブエージェントが隔離環境で並列実行、毎日リリースノートを公開、SuperGrok Heavy 契約者のみ利用可（最初 6 か月は月 99 ドル、以降 300 ドル）。xAI による Claude Code / Codex CLI への正面回答。
- [Antigravity CLI](https://antigravity.google/blog/introducing-google-antigravity-2-0) - 🆕 **2026 年 5 月 19 日（Google I/O 2026）**。Antigravity 2.0 の軽量 CLI コンパニオン。ターミナルから直接 Google のエージェント harness を起動・操作できる。macOS / Linux / Windows。**Free / Pro / Ultra ユーザーには 2026 年 6 月 18 日から Gemini CLI の後継として展開**。
- [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code) - 🆕 🇨🇳 **2026 年 6 月 6 日**。Moonshot AI の TypeScript / MIT 製ターミナルコーディングエージェント。隔離コンテキストで動く coder / explore / plan サブエージェントを内蔵し、`/mcp-config` で対話式に MCP を設定。npm インストール対応。次世代 Kimi K2.6 エージェント向け設計。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FMoonshotAI%2Fkimi-code&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MAI-Code-1-Flash in GitHub Copilot](https://microsoft.ai/news/introducingmai-code-1-flash/) - 🆕 **Build 2026（2026 年 6 月 2 日）**。Microsoft 初の完全自社開発 5B コーディングモデルが GitHub Copilot のモデル選択肢として登場 —— 4 つの主要コーディングベンチで Claude Haiku 4.5 を上回り（SWE-Bench Pro 51.2% vs 35.2%）、コストも大幅に低減。

### IDE エージェント

- [Cursor 3.09](https://www.cursor.com/) - 🆕 2026-04-03 アップデート。Vibe Coding ワークフロー向けにエージェントモードを強化。
- [Kilo Code](https://www.kilocode.com/) - 🇨🇳 🆕 2026-04 中国コミュニティで人気の Cursor 代替。デフォルトモデル: MiniMax。
- [Cursor](https://www.cursor.com/) - 2026-02 アップデートで 8 並列エージェント対応。
- [Windsurf](https://codeium.com/windsurf) - Codeium 製のエージェント型 IDE。
- [Cline](https://github.com/cline/cline) - VS Code で動く自律コーディングエージェント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcline%2Fcline&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Continue](https://github.com/continuedev/continue) - VS Code・JetBrains 対応のオープンソース AI コードアシスタント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcontinuedev%2Fcontinue&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Roo Code](https://roocode.com/) - 🆕 オープンソースの VS Code 拡張。複数ファイルを跨いで読み書きし、コマンド実行が可能、model-agnostic。自前の LLM API 以外は無料。
- [Void](https://github.com/voideditor/void) - 🆕 VS Code のオープンソース fork。"オープンソース版 Cursor" として位置付け、データはローカルに残り、モデルは持ち込み。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvoideditor%2Fvoid&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [GitHub Copilot](https://github.com/features/copilot) - 2026 年初頭よりエージェントモードと `gh copilot` シェル統合。
- [Kiro](https://kiro.dev/) - AWS の自律エージェント。スペック驅動開発、最大3だ 10 タスクを同時管理。
- [Amazon Q Developer](https://aws.amazon.com/q/developer/) - AWS エコシステムと深く統合された AI コーディングコンパニオン。
- [Visual Studio 2026 Agent Mode + Skills](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/) - 🆕 **VS 2026 Insiders 2026-05-12～15**。Copilot Chat「Agent Mode」が Visual Studio 2026 内で再利用可能な Copilot Skill を探し・管理・作成できるようになり、ソリューション全体のコンテキストを見つつ、端末コマンド実行や外部ツール呼び出しもサポート。
- [JetBrains Rider AI Test-Writing Skill](https://blog.jetbrains.com/dotnet/2026/05/22/claude-codex-ai-agent-skill-for-writing-tests/) - 🆕 **2026 年 5 月 22 日**。JetBrains Rider に追加された AI Assistant skill。.NET のコードカバレッジ情報を Claude Code / Codex に渡し、未カバー分岐に絞ってテスト生成させることで AI コストを削減。

### 自律ソフトウェアエンジニア

- [Cursor 3.4 Cloud Agent Environments](https://cursor.com/changelog) - 🆕 **2026-05-13**。クラウドエージェント / 自動化向けの新しい開発環境。マルチリポ、build secrets 付き Dockerfile 設定、キャッシュレイヤー 70% 高速化、環境ごとのバージョン履歴とロールバック、監査ログ、スコープを限定した egress / secrets。
- [Devin 3.0](https://www.cognition.ai/) - 🆕 Cognition 製。動的再プランニング、自己修復コード、レガシーコードベース移行、マルチモーダル入力（UI モックアップ、ビデオ録画）。
- [Devin 2.2](https://cognition.ai/blog/introducing-devin-2-2) - 🆕 **2026 年 2 月**。サンドボックス化された terminal + editor + browser を備える商用プロダクト（Core 月 20 ドル、Team 月 500 ドル）。
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) - 自律エージェントとして AI ソフトウェア開発者を使うオープンソースプラットフォーム。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAll-Hands-AI%2FOpenHands&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SWE-agent](https://github.com/SWE-agent/SWE-agent) - LLM を GitHub Issue を修正するソフトウェアエージェントに変える。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSWE-agent%2FSWE-agent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Devika](https://github.com/stitionai/devika) - 💤 **Stale**（2025-09 以降更新なし）。エージェント型 AI ソフトウェアエンジニア、Devin のオープンソース代替。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstitionai%2Fdevika&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [GPT Engineer](https://github.com/gpt-engineer-org/gpt-engineer) - 📦 **Archived**（2025-05）。何を作るか指定すると AI が質問して作成。自律コーディング時代初期の基礎、歴史的参照として維持。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgpt-engineer-org%2Fgpt-engineer&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Codegen](https://github.com/codegen-sh/codegen-sdk) - 🆕 プログラム的なコード操作とマルチファイルリファクタリング SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcodegen-sh%2Fcodegen-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Qodo](https://www.qodo.ai/) - 🆕 品質・セキュリティ・テスト生成に特化した AI コードレビュープラットフォーム。
- [Google Antigravity 2.0](https://antigravity.google/blog/introducing-google-antigravity-2-0) - 🆕 **2026 年 5 月 19 日（Google I/O 2026）**。複数エージェントを並列編成できるスタンドアロン・デスクトップアプリ（macOS / Linux / Windows）。cron 形式のスケジュール実行、長時間の非同期タスク、動的サブエージェント、AI Studio / Android / Firebase との統合を追加。コンパニオンの **Antigravity SDK** は harness の自前ホストを可能にし、エンタープライズ版は Gemini Enterprise Agent Platform 内に組み込まれる。

---

## 🤖 Physical AI / 身体性エージェント

*物理世界を知覚し推論し行動する AI —— ヒューマノイドロボット、工場自動化、Physical AI インフラ。言語エージェントの次の波。*

### 基盤モデルと研究

- [Google Gemini Robotics ER-1.6](https://deepmind.google/) - 🆕 2026-04-14。空間・物理推論が強化されたロボティクス AI モデル。Agile Robotics と提携して実機で展開。
- [Project Prometheus (Bezos)](https://www.reuters.com/) - 🆕 ジェフ・ベゾス主導の Physical AI ベンチャー。評価額 $38B、$10B を調達。
- [NVIDIA Isaac GR00T](https://developer.nvidia.com/isaac/gr00t) - NVIDIA のヒューマノイドロボット用基盤モデルプラットフォーム。GTC で発表、Hannover Messe 2026 で拡充。
- [NVIDIA Industrial AI Cloud](https://nvidianews.nvidia.com/) - 🆕 2026-04（Hannover Messe）。ドイツテレコムと共同構築した産業 AI ワークロード用 AI 工場。

### ヒューマノイドロボット

- [Tesla Optimus Gen3](https://www.tesla.com/) - 🆕 2026 年夏量産。汎用タスク向けの高度ヒューマノイド。
- [Figure 04](https://autonews.gasgoo.com/articles/news/figure-founder-f04-robot-initiates-component-delivery-process-2054560059634376705) - 🆕 **2026-05-13**。CEO の Brett Adcock が Figure 04 の設計確定と部品出荷開始を表明。F.03 の後継、Helix VLA モデルを搭載。
- [Helix 02 パッケージ仕分け 72h 連続運転](https://www.businessinsider.com/figure-ai-turned-a-humanoid-sorting-packages-must-see-tv-2026-5) - 🆕 **2026-05-13～16**。Figure F.03 フリートが Helix 02 でパッケージ仕分けラインを完全自律で運転 —— 初日 8 時間で ~22K 個、最初の 24 時間で ~30K 個、ストレステストでは機械故障まで約 72 時間で ~88K 個を処理。初めて公開された家庭型ヒューマノイドの長時間稼働データ。
- [Figure F.03 対 人間 8 時間仕分けチャレンジ](https://incrypted.com/en/figure-ai-held-a-human-vs-robot-marathon/) - 🆕 **2026-05-18**。Figure 初の公開人間 vs ロボット対決。同じライン上で 8 時間、人間社員が 12,924 個（2.79 秒 / 個）と F.03 の 12,732 個（2.83 秒 / 個）をわずかに上回り勝利。実業務で公開されたうち人間に最も迫ったスループット。
- [Boston Dynamics Atlas 100ポンド操作 + Hyundai 25K 台計画](https://www.techtimes.com/articles/316854/20260519/boston-dynamics-reveals-how-atlas-learned-lift-100-pound-loads-hyundai-plans-30000-per-year.htm) - 🆕 **2026-05-18 / 19**。Boston Dynamics が Atlas が強化学習 + 大規模シミュレーションで **100 ポンド超**の荷重（冷蔵庫 / 洗濯機）を持ち上げて運ぶ動画と技術ブログを公開。Hyundai Motor Group は 2028 年ジョージアのアセンブリエ工場を手始めに、Hyundai/Kia 工場へ **25,000+ 台の Atlas** を配備する計画を発表。
- [Unitree G1 を JAL 羽田に導入](https://www.techtimes.com/articles/316862/20260519/jal-deploys-unitree-g1-robots-haneda-us-congress-moves-blacklist-supplier-national-security.htm) - 🆕 **2026-05**。日本航空が羽田の地上業務（获物積み込み / コンテナ輸送 / 機内清掝）で Unitree G1 ヒューマノイドの実証を開始し、**隊位性を保つロボットを現役投入する世界初の商用航空例**としてアピール。同週、米連邦議会は Unitree をエンティティリストに加える動きを見せ、embodied AI サプライチェーンのジオポリティクス化が進む。
- [Honour (荣耀) Humanoid](https://www.honor.com/) - 🇨🇳 🆕 2026 ハーフマラソンで人型ロボット世界記録。
- [Zhiyuan (智元) AGIBOT](https://www.agibot.com/) - 🇨🇳 🆕 2026-04。新しいヒューマノイドボディ、基盤モデル、ソリューションスイート。「展開元年」と表現。
- [Unitree H シリーズ](https://www.unitree.com/) - 🇨🇳 Boston Dynamics の中国競争相手。
- [Agile Robotics](https://www.agile-robots.com/) - 🆕 Gemini Robotics ER-1.6 の展開パートナー。ドイツのロボティクス企業。
- [Shenzhen Humanoid Pilot Line](https://www.chinadailyhk.com/hk/article/631892) - 🇨🇳 🆕 深圳が **2026-04-12** にヒューマノイドロボット初のパイロット生産ラインを稼働（乐聚 Robotics + 東方精工、龍華區）。2 時間で組み立て、年 500～1,000 台。佛山の年 1 万台工場へ量産移行予定。

### 消費者向けロボティクス・ウェアラブル

- [Doubao AI Glasses (ByteDance)](https://seed.bytedance.com/) - 🇨🇳 🆕 2026 年第 2 四半期ローンチ。リアルタイム翻訳、物体認識、豆包 LLM 統合。
- [Nothing AI Glasses/Earbuds](https://nothing.tech/) - 🆕 2026-04 発表。AI 統合スマートウェアラブル。
- [Samsung Galaxy S26 (Gauss 2.3)](https://www.samsung.com/) - オンデバイスのエージェント AI。Gauss 2.3 Think と Gauss O Flash。
- [Meta Ray-Ban Stories 3](https://www.meta.com/) - Llama 統合を継続的に深化。

### 自動運転

- [Tesla FSD v13](https://www.tesla.com/) - 主要市場で L4 対応展開を拡充。
- [Waymo](https://waymo.com/) - 2026 年を通じて米国都市で商用 L4 を展開中。
- [WeRide / Pony.ai / Baidu Apollo](https://www.weride.ai/) - 🇨🇳 中国 L4 車両集団が運行区域を拡大。
- [Tesla Optimus Gen3 (V3)](https://www.teslarati.com/tesla-optimus-awe-2026-shanghai/) - 🆕 **AWE 2026 上海でお披露目**。初の量産 Optimus。Fremont ラインが 2026 年 1 月に稼働、初期目標は年 5〜10 万台、初期価格は約 3 万ドル、2026 年後半に小規模な外販を予定。37 関節、歩行速度 1.2 m/s、22 自由度のハンド。
- [Figure 03 (Helix AI)](https://blog.robozaps.com/b/figure-03-review) - 🆕 **2025 年末発表、2026 年に量産立ち上げ**。Figure 初の家庭用設計：柔らかいテキスタイル外装、ワイヤレス充電、触覚センサー。2026 年 5 月のデモでは、F.03 が 2 台で視覚協調のみによって 2 分以内に部屋掃除とベッドメイクを自律実行。
- [Figure 02 + Helix 02](https://en.wikipedia.org/wiki/Figure_AI) - 🆕 **2026 年 1 月**。Helix 02 で全身自律性が拡張（食洗機の出し入れ、洗濯物たたみ）。BotQ 工場は年 1.2 万台の生産能力。
- [Unitree G1 + H1-2](https://community.robotshop.com/blog/show/unitree-robotics-at-ces-2026-a-clear-signal-of-whats-coming-next) - 🆕 **CES 2026**。G1 のダンス / ボクシング / スケートのデモ、2 月には自律カンフー演武。5'8" の H1-2 産業機は 7.4 mph。2026 年の人型ロボット出荷目標は 2 万台。
- [Unitree R1 Air](https://www.eweek.com/news/chinese-unitree-g1-humanoid-robot-skates-spins-flips-apac/) - 🆕 価格 **4,900 ドル** のコンシューマー人型ロボット。走行、バックフリップ、手歩きまでこなす。
- [Unitree Gen 2 (lifelike skin)](https://www.youtube.com/watch?v=Gmp82MuTFsM) - 🆕 圧力 / 温度 / 触覚センサーを埋め込んだ、人肌に近い外皮を採用。
- [Unitree GD01](https://www.extremetech.com/computing/unitree-will-sell-you-a-personal-mecha-robot-for-650000) - 🆕 **2026 年 5 月**。約 10 フィートの有人メカ。パイロット操縦で二足歩行と四足歩行を切り替え可能。価格は人民元 390 万元〜（約 65 万ドル）。身体性エージェントの形態が操縦型にも分岐し始めた証左。
- [1X NEO（コンシューマー型ヒューマノイド）](https://www.1x.tech/discover/neo-home-robot) - 🆕 **2026 年 2 月 26 日に予約開始**、米国家庭への初回配送は 2026 年内。5'6"/66 ポンドの家庭用ヒューマノイドで、22-DoF ハンド、ソフトボディ、4 時間稼働、オンボード LLM、騒音約 22dB。早期アクセス価格 20,000 ドル + 200 ドル預金、または月額 499 ドルのサブスク。プライバシー "no-go" ゾーンと顔ぼかしを内蔵。家庭に実際に配送される最初の本格的なコンシューマー型ヒューマノイド。

---

## 🎮 エージェントシミュレーションと世界モデル

*エージェントを訓練し、観察し、ストレステストするシミュレーション環境。世界モデル・身体性研究が言語エージェントと交わる中、重要性が高まり続けている。*

- [Generative Agents](https://github.com/joonspk-research/generative_agents) - 💤 スタンフォードの名著 *Smallville*（Park et al., 2023）。25 体の LLM 駆動キャラクターをメモリ + 反省 + 計画で連携させるコストチューム。後続の多くのマルチエージェント論文に影響。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fjoonspk-research%2Fgenerative_agents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Voyager](https://github.com/MineDojo/Voyager) - 💤 Minecraft の生涯学習エージェント—— GPT-4 にスキルライブラリとカリキュラム（Wang et al., 2023）。オープンエンド型エージェント評価の古典。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FMineDojo%2FVoyager&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SWE-Gym](https://github.com/SWE-Gym/SWE-Gym) - 実際の GitHub Issue で SWE エージェントを訓練するオープン環境、SWE-bench とセット。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSWE-Gym%2FSWE-Gym&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [WebArena](https://webarena.dev/) - 現実的で再現可能なウェブ環境（Reddit、ショッピング、GitLab クローン）。OSWorld や多くのブラウザエージェント論文で使用される。
- [WorkArena](https://github.com/ServiceNow/WorkArena) - ServiceNow 製のブラウザエージェント用エンタープライズ職場ベンチマーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FServiceNow%2FWorkArena&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Genie 3 / Genie 4](https://deepmind.google/) - Google DeepMind の対話型ビデオ世界モデル—— プロンプトからプレイ可能な 3D 世界を生成。クローズドコード研究。
- [NVIDIA Cosmos](https://github.com/nvidia-cosmos/cosmos-predict1) - 身体性 AI / ロボティクス用の NVIDIA 世界モデル基盤—— 物理的にもっともらしいビデオ未来を生成。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fnvidia-cosmos%2Fcosmos-predict1&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Snowflake Agent World Model (AWM)](https://github.com/Snowflake-Labs/agent-world-model) - 🆕 **2026 年 2 月 10 日オープンソース化、5 月 1 日に ICML 2026 採択**。1,000 個の実行可能 SQL バックエンドツール使用環境（35K+ ツール、10K タスク）を統一 MCP インターフェースで提供する合成環境生成パイプライン——大規模マルチターン agentic RL を実現。インフラは `meta-pytorch/OpenEnv` にマージ済み。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSnowflake-Labs%2Fagent-world-model&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 📊 ベンチマークとリーダーボード

*フロンティア AI 能力を追跡する標準評価スイートとライブリーダーボード。*

- [BenchLM](https://benchlm.ai/) - 🆕 複数のベンチマークファミリーを集約したリーダーボード。2026-04 首位: Claude Mythos Preview 99、Gemini 3.1 Pro / GPT-5.4 同点 94、Claude Opus 4.6 / GPT-5.4 Pro 92、GLM-5 Reasoning 85（オープン首位）。
- [SWE-bench Verified](https://www.swebench.com/) - 実世界の GitHub Issue 解決ベンチマーク。2026-04 首位: Claude Mythos 93.9%、Claude Opus 4.7 87.6%。
- [GPQA Diamond](https://github.com/idavidrein/gpqa) - 💤 データセットリポは 2024-09 以降更新なし。専門家レベルの科学推論。2026-04 首位: Gemini 3.1 Pro 94.3%（世界記録）、Claude Opus 4.7 94.2%。
- [ARC-AGI 2](https://arcprize.org/) - 抽象推論。Gemini 3.1 Pro 77.1%。
- [OSWorld](https://os-world.github.io/) - デスクトップ GUI 操作。GPT-5.4 75%（人間ベースライン超え）。
- [LMArena (旧 Chatbot Arena)](https://lmarena.ai/) - クラウドソース型の会話選好バトル。Opus 4.6 が現在トップ。
- [MMLU-Pro](https://github.com/TIGER-AI-Lab/MMLU-Pro) - MMLU の難化后継者。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTIGER-AI-Lab%2FMMLU-Pro&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LiveCodeBench](https://livecodebench.github.io/) - コンテスト形式のコーディングベンチマーク、汚染耐性のため継続的に更新。
- [AIME 2025 / Humanity's Last Exam (HLE)](https://agi.safe.ai/) - エリート数学 / 博士レベルの一般推論。
- [Terminal-Bench](https://www.tbench.ai/) - CLI エージェント評価。Codex CLI 77.3%。
- [Wolfram LLM Benchmarking Project](https://www.wolfram.com/llm-benchmarking-project/) - 英語仕様から Wolfram Language へのコード生成。
- [GDPval / GDPval-MM](https://artificialanalysis.ai/evaluations/gdpval-aa) - 🆕 **2026 年 2 月**。OpenAI が公開した経済価値ベンチマーク。44 職種 / 9 業界、1,320 の専門家作問タスクを収録。2026 年 5 月時点の首位は GPT-5.5 の GDPval-MM 84.9%。
- [Hieroglyphic Benchmark](https://juliangoldie.com/google-gemini-3-5/) - 🆕 横断的 / 抽象推論のベンチマーク。Gemini 3.5 "Snowbunny" が 80%（リーク）。
- [LLM-Stats Live Leaderboard](https://llm-stats.com/llm-updates) - 🆕 新しくリリースされたモデルを横断ベンチで継続更新するライブダッシュボード。
- [τ²-Bench (Tau-Bench)](https://github.com/sierra-research/tau2-bench) - 🆕 Sierra Research のツール-エージェント-ユーザー対話ベンチマーク（リテール / 航空ドメイン）。マルチターンのツール使用・DB 操作・ポリシー遵守を計測。2026 年 4 月の首位は 38 評価モデル中 Claude Mythos Preview の 89.2%。MIT。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsierra-research%2Ftau2-bench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Gartner 2026 マジッククアドラント: エンタープライズ AI コーディングエージェント](https://cursor.com/blog/cursor-leads-gartner-mq-2026) - 🆕 **2026 年**。エンタープライズ向け AI コーディングエージェントに関する初の MQ。**Cursor** と **OpenAI Codex** がリーダー、Cline と Windsurf がチャレンジャーとして選出され、コーディングエージェント市場がエンタープライズの成熟期に入ったことを示す。

---

## 🖥️ Computer Use / デスクトップエージェント

*OS レベルでデスクトップソフトウェアを見て・操作し・自動化するエージェント。ブラウザ専用エージェントは [🌐 ブラウザと Web エージェント](#-ブラウザと-web-エージェント) 参照。*

- [Claude Computer Use](https://www.anthropic.com/) - 🆕 Anthropic の「Desktop Intelligence」—— Claude が画面を見、マウス / キーボードで任意のソフトウェアを自動化。
- [OpenAI Operator](https://openai.com/) - 🆕 予約、フォーム入力、ウェブタスク自動化用のブラウザエージェント。
- [Google Project Mariner](https://deepmind.google/models/project-mariner/) - 📦 **終了**（2026-05-04）。ブラウザエージェント研究プロジェクト。機能は Gemini Agent に統合された。
- [Microsoft Copilot Agents](https://www.microsoft.com/en-us/microsoft-copilot/) - 🆕 Microsoft 365 スタック上の自律バックグラウンドエージェント。
- [Open Interpreter](https://github.com/OpenInterpreter/open-interpreter) - コンピュータへの自然言語インターフェース—— LLM にローカルでコードを実行させる。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenInterpreter%2Fopen-interpreter&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Manus AI](https://manus.im/) - 🇨🇳 🆕 クラウド・ローカルハイブリッドモデルの自律汎用 AI エージェント。調査・コーディング・複雑なマルチステップタスクを処理。
- [Genspark](https://www.genspark.ai/) - 🆕 mixture-of-agents アーキテクチャのオールインワン自律ワークエージェント。電話も掛けられる。
- [Perplexity Computer](https://www.perplexity.ai/) - 🆕 マルチモデルオーケストレーションとローカルファイルアクセスを備えた調査向けデスクトップエージェント。
- [Beam AI](https://beam.ai/) - 🆕 成功事例に基づきロジックを洗練させる自己学習デスクトップエージェント。
- [Microsoft Copilot Studio Computer-Using Agents](https://techcommunity.microsoft.com/blog/copilot-studio-blog/computer-using-agents-in-microsoft-copilot-studio-are-now-generally-available/4519427) - 🆕 **2026 年 5 月 13 日 GA**。Copilot Studio 内で、UI を介して Web サイトやデスクトップアプリを直接操作するエージェントを構築可能 —— Microsoft 365 / Power Platform 全体で利用できる、Claude Computer Use に対する Microsoft 純正の回答。
- [Perplexity Personal Computer for Windows](https://www.perplexity.ai/hub/products/computer-for-windows) - 🆕 **2026 年 6 月 3 日発表**。Perplexity のマルチモデル・エージェントオーケストレーター（19+ AI モデルを自動ルーティング）を Windows へ展開；ローカルファイル・ネイティブアプリ・Web サービスを一つのシステムで接続。Mac 版（4 月 16 日）の延長線上で、Computex 2026 発表のハイブリッドローカル / クラウド推論オーケストレーターとも連動。
- [ChatGPT Workspace Agents](https://venturebeat.com/orchestration/openai-unveils-workspace-agents-a-successor-to-custom-gpts-for-enterprises-that-can-plug-directly-into-slack-salesforce-and-more) - 🆕 **リサーチプレビュー 2026-04-22，クレジット課金化 2026-05-06，EKM 対応 2026-05-07**。OpenAI の Custom GPTs の企業向け後継 —— クラウド側で動き、ファイルアクセス、コード実行、Slack / Google Drive / Salesforce などとのコネクタを持ち、スケジュール実行も可能。Business / Enterprise / Edu / Teachers 向けに提供され、Codex をバックエンドに採用。

---

## 🌐 ブラウザと Web エージェント

*実ブラウザを介して Web と対話するエージェント—— ナビゲーション、クリック、スクレイピング、マルチページワークフローをこなすフレームワークとインフラ。*

- [Browser Use](https://github.com/browser-use/browser-use) - 2026 年にオープンソースブラウザエージェントの事実上の標準。92K star。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowser-use%2Fbrowser-use&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Stagehand](https://github.com/browserbase/stagehand) - Browserbase 製の「ブラウザエージェント用 SDK」—— 型付きの `act` / `extract` / `observe` プリミティブを Playwright の上に提供。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowserbase%2Fstagehand&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Steel Browser](https://github.com/steel-dev/steel-browser) - 🆕 AI エージェント用オープンソースブラウザ API —— セッション永続化とプロキシローテーションを備えたサンドボックス Chromium。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsteel-dev%2Fsteel-browser&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Skyvern](https://github.com/Skyvern-AI/skyvern) - LLM とコンピュータ・ビジョンでブラウザベースワークフローを自動化。AGPL-3.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSkyvern-AI%2Fskyvern&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentQL](https://github.com/tinyfish-io/agentql) - クエリ言語 + Playwright 統合でセマンティックな Web 抽出。動的 / 乱雑なページでもロバスト。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftinyfish-io%2Fagentql&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hyperbrowser MCP](https://github.com/hyperbrowserai/mcp) - 🆕 ホステッドのヘッドレスブラウザフリートを MCP サーバーとして公開。標準ツールインターフェースで Claude / GPT / LangChain にプラグイン。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhyperbrowserai%2Fmcp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) - 🆕 マイクロソフト公式の Playwright サーバーを MCP ツールとして公開。プロダクショングレードの自動化。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fplaywright-mcp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MultiOn](https://www.multion.ai/) - ステップ推論 + メモリを内蔵したホステッド型ブラウザエージェントプラットフォーム。クローズドコード。
- [Browserbase](https://www.browserbase.com/) - AI エージェント専用のヘッドレスブラウザインフラ —— ステルス、セッション永続化、captcha 処理、オブザーバビリティ。
- [BrowserOS](https://www.browseros.com/) - 🆕 AI エージェントを内蔵した初のオープンソースブラウザ —— プライバシー優先の Chrome 代替。コードなしで自然言語によるタスク自動化が可能。ローカル優先設計で、Perplexity Comet や Arc の AI 機能と対抗。

---

## 🗣️ 音声とマルチモーダルエージェント

*音声対応 ・ マルチモーダル AI エージェントプラットフォーム。*

- [AgentLine](https://agentline.cloud/) - 🆕 ⚠️ **Unverified.** AI エージェント向けテレフォニー基盤 —— 電話番号の発行、発信／着信、リアルタイム文字起こしを JSON で webhook に流す。エージェント音声パイプライン用途に絞った Twilio の軽量代替を標榜。提出者は有料ユーザー 30+ と主張するが、第三者の採用事実は未確認。
- [ElevenLabs](https://elevenlabs.io/) - 業界トップの AI 音声合成、クローン、会話 AI。
- [Vapi](https://github.com/VapiAI/server-sdk-python) - 音声 AI エージェントを構築・テスト・展開するプラットフォーム。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FVapiAI%2Fserver-sdk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Retell AI](https://www.retellai.com/) - プロダクション対応の会話型音声 AI エージェント。
- [Bland AI](https://www.bland.ai/) - 企業向け AI 電話プラットフォーム。
- [LiveKit Agents](https://github.com/livekit/agents) - 音声・ビデオ・データを含むリアルタイムマルチモーダル AI エージェント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flivekit%2Fagents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Pipecat](https://github.com/pipecat-ai/pipecat) - 音声・マルチモーダル会話 AI のオープンソースフレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fpipecat-ai%2Fpipecat&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vocode](https://github.com/vocodedev/vocode-python) - 💤 **Stale**（2024-11 以降更新なし）。音声ベース LLM エージェントライブラリ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvocodedev%2Fvocode-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Bolna](https://github.com/bolna-ai/bolna) - エンドツーエンドのオープンソース音声 AI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbolna-ai%2Fbolna&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cartesia](https://www.cartesia.ai/) - 🆕 超低遅延のリアルタイム会話型音声 AI。
- [Meta Voice AI](https://ai.meta.com/) - 🆕 旧 PlayHT/Play.ai チームの技術を Meta AI ・ AI キャラクター、ウェアラブルに統合。Play.ai は 2025-12-31 にサービス終了。
- [Sesame](https://www.sesame.com/) - 🆕 感情理解と自然会話を備えた音声 AI コンパニオン。
- [OpenYabby](https://github.com/OpenYabby/OpenYabby) - 🆕 macOS 向けオープンソースの音声驅動型マルチエージェントオーケストレーター — Realtime API + CLI ランナー + マルチチャネル連携。リードエージェントが計画を立て、レビューと QA をサブエージェントに委任します。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenYabby%2FOpenYabby&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ElevenAgents](https://elevenlabs.io/voice-agents) - 🆕 ElevenLabs のフルスタック音声エージェント基盤（2026 年 4〜5 月更新）。MCP 対応、マルチモーダルメッセージ、会話トピック発見、ナレッジベース検索、ツール呼び出し前の音声制御を提供。音声エージェント基盤として初めて AIUC-1 認証を取得。
- [Cartesia Line](https://cartesia.ai/blog/introducing-line-for-voice-agents) - 🆕 **2026 年 4 月**。Sonic 3 TTS + Ink STT 上に構築されたコードファースト音声エージェント基盤。first audio まで約 40〜90ms。
- [Deepgram Voice Agent API](https://deepgram.com/learn/best-voice-ai-agents-2026-buyers-guide) - 🆕 STT（Nova-3）+ LLM ルーティング + TTS（Aura-2）+ 通話中 10 言語切り替え対応の Flux 会話型 STT を 1 エンドポイントで束ねた。
- [OpenAI Realtime API (GPT-Realtime-2)](https://openai.com/) - 🆕 **2026 年 5 月 8 日**。並列ツール呼び出しに対応した GPT-5 クラス推論の音声版。本番音声エージェント用途で従来の Realtime モデルを置き換える。
- [Dograh](https://github.com/dograh-hq/dograh) - 🆕 オープンソース・セルフホスト型の音声 AI プラットフォーム —— Vapi / Retell のオープン代替。オンプレ運用、Speech-to-Speech または LLM/STT/TTS のいずれも BYOK。ビジュアルワークフロービルダー、MCP ネイティブ、テレフォニー対応。BSD-2-Clause、4K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdograh-hq%2Fdograh&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hume TADA](https://github.com/HumeAI/tada) - 🆕 **2026 年 3 月 10 日**。Hume AI 初のオープンソース TTS —— Text-Acoustic Dual Alignment アーキテクチャ。転記エラーゼロ、約 5× 高速、スマホで動作。次世代 EVI 音声エージェントの基盤。MIT、Llama ベース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHumeAI%2Ftada&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 📱 パーソナル AI エージェント

- [OpenClaw](https://github.com/openclaw/openclaw) - 🆕 スキル・メモリ・マルチチャネルメッセージング、Dreaming、Canvas/A2UI、ACP コーディング harness を備えた個人向け AI エージェントプラットフォーム。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenclaw%2Fopenclaw&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Rabbit R1](https://www.rabbit.tech/) - ラージアクションモデルを搭載した個人 AI デバイス。
- [Limitless](https://www.limitless.ai/) - 見・言い・聞いたものをパーソナライズした AI（旧 Rewind）。
- [Open Interpreter](https://github.com/OpenInterpreter/open-interpreter) - コンピュータへの自然言語インターフェース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenInterpreter%2Fopen-interpreter&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [01 Light](https://github.com/OpenInterpreter/01) - 💤 **Stale**（2024-11 以降更新なし）。オープンソースの音声コンピュータインターフェース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenInterpreter%2F01&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Leon](https://github.com/leon-ai/leon) - 自サーバ上に住むオープンソース個人アシスタント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fleon-ai%2Fleon&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Khoj](https://github.com/khoj-ai/khoj) - ノートやドキュメント、画像を機械的にスキャンして会話できる「第二の脳」。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fkhoj-ai%2Fkhoj&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Humane AI Pin](https://humane.com/) - ⚠️ **2025年2月28日にサービス終了**（HPに買収され、デバイスは廃止）。元々はスクリーンレス・アンビエントコンピューティングのウェアラブル AI デバイス。
- [Arahi AI](https://arahi.ai/) - 🆕 個人生産性 + ビジネス自動化アシスタント。
- [Lindy AI](https://www.lindy.ai/) - 🆕 メール・カレンダー・ワークフロー自動化のノーコード AI エージェント。
- [MuleRun](https://www.mulerun.ai/) - 🆕 繰り返しタスクとバックグラウンド自動化の常駐エージェント。
- [Gemini Intelligence](https://blog.google/products-and-platforms/products/chrome/bringing-chrome-ai-to-android/) - 🆕 **2026 年 5 月 12 日（Android Show: I/O Edition）**。Googlebooks ノート PC、Wear OS、Android Auto、Android XR を横断するプロアクティブな agentic AI 機能群。最新の Samsung Galaxy と Pixel から段階展開。買い物リストからカートを自動作成、スピンクラスの予約、Rambler STT による "フィラー語" 除去などを実現。
- [Gemini Spark](https://9to5google.com/2026/05/14/gemini-spark-insight/) - 🆕 **2026 年 5 月 14 日（I/O 前のリーク / インサイト）**。Gemini アプリ内で多段プロセスを自律実行するブランド化されたエージェント機能。Gemini 3.1 Pro の推論スタックの上に乗る。
- [QwenPaw](https://github.com/agentscope-ai/QwenPaw) - 🆕 🇨🇳 **2026 年 5 月、CoPaw から改称**。Qwen / AgentScope エコシステム下のセルフホスト型パーソナルアシスタント。ローカル優先のメモリ、ホットロード可能な skills、マルチエージェント協調、マルチチャネル（DingTalk / Feishu / WeChat / Discord / Telegram）、ツールガード + skill スキャナを内蔵。Apache-2.0。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentscope-ai%2FQwenPaw&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsoft Scout](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) - 🆕 **Build 2026（2026 年 6 月 2 日）**。OpenClaw フレームワーク上に構築された Microsoft の常時稼働パーソナルエージェント —— クラウド / デスクトップ / Web を横断してプロアクティブに動作し、Teams / Outlook / OneDrive / SharePoint に接続。各エージェントは独自の Entra ID で動作し、ポリシー適合性チェック + 監査トレイルを継続実施。Microsoft Frontier プログラムでプライベートプレビュー、Intune ポリシー + GitHub Copilot ライセンスが必要。
- [Lenovo Qira / Motorola Qira](https://news.lenovo.com/pressroom/press-releases/lenovo-unveils-lenovo-and-motorola-qira/) - 🆕 **CES 2026（2026 年 1 月 6 日）**。Lenovo と Motorola が共同開発した「パーソナル・アンビエント・インテリジェンス・システム」—— PC / スマホ / タブレット / ウェアラブルを横断するコンテキスト認識 AI。2026 年 Q1 から一部 Lenovo デバイスで展開、その後 Motorola スマホへ。主要 OEM 初のアンビエント AI プレイ。

---

## 📱 モバイルエージェント

*Android / iOS を操作する GUI エージェント。デスクトップ Computer Use の次のフロンティア。*

- [Mobile-Agent](https://github.com/X-PLUG/MobileAgent) - 🇨🇳 アリババ製の代表的なマルチモーダル電話操作エージェントファミリー（v1 → v3、Mobile-Agent-E、V も）。Android ベンチマークで SOTA。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FX-PLUG%2FMobileAgent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AppAgent](https://github.com/mnotgod96/AppAgent) - 💤 タップやスワイプでスマートフォンアプリを操作するテンセント製マルチモーダルエージェント。初期の影響ある実装。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmnotgod96%2FAppAgent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Apple Intelligence](https://www.apple.com/apple-intelligence/) - iOS / iPadOS / macOS のオンデバイスエージェント層。App Intents と画面インテリジェントを OS 全体で提供。
- [Samsung Galaxy AI / Bixby 2.0](https://www.samsung.com/global/galaxy/galaxy-ai/) - Galaxy S26 に携載された Gauss 駆動のオンデバイスエージェント機能。
- [Google Gemini for Android](https://gemini.google/) - Android で Google Assistant を置き換える全面 Gemini 駆動のアプリ認識アクション。システム意図と Workspace を含む。
- [Magma](https://microsoft.github.io/Magma/) - Microsoft Research のマルチモーダルエージェント基盤モデル。UI / ロボティクス / 物理動作を統一。
- [mobile-use](https://github.com/minitap-ai/mobile-use) - 🆕 AI エージェントが Android / iOS の実アプリを人間と同じように操作できるオープンソースフレームワーク（Apache-2.0、2.5K+ stars）—— UI 認識ナビゲーション、自然言語制御。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fminitap-ai%2Fmobile-use&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [agent-device (Callstack)](https://github.com/callstack/agent-device) - 🆕 **2026 年 2 月**。iOS / Android 実機・シミュレータを自動化する軽量・トークン効率の良い CLI。AI エージェントと CI 向けに設計されたコマンドモデル。MIT、2.6K+ stars。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcallstack%2Fagent-device&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🏢 エンタープライズエージェントプラットフォーム

- [Salesforce Agentforce 360](https://www.salesforce.com/agentforce/what-is-new/) - エンタープライズ CRM 用自律 AI エージェント —— 営業・サービス・マーケティング。**Spring 2026 リリース**で、Agentforce Builder（対話型エージェントオーサリング）、Agent Script（決定論的な動作制御）、Agentforce Voice（Amazon Connect / Five9 / Genesys / NiCE / Vonage + SIP）、新 Data 360 上の Intelligent Context が追加。124 か国の顧客で約 85% の問い合わせを自律解決。
- [Microsoft Copilot Studio](https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio) - エンタープライズの Copilot とエージェント構築・カスタマイズ。
- [Gemini Enterprise Agent Platform](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform) - 🆕 **2026-04-22**（Google Cloud Next '26）。Vertex AI がエンタープライズエージェントの構築・拡大・ガバナンス・最適化ハブへ進化。Gemini 3.1 Pro/Flash、Lyria 3 に加え、サードパーティモデル（Claude Opus / Sonnet / Haiku）もサポート。
- [Google Vertex AI Agent Builder](https://cloud.google.com/products/agent-builder) - Google Cloud で企業要件の生成 AI エージェントを構築・展開。
- [Amazon Bedrock Agents](https://aws.amazon.com/bedrock/agents/) - 複数ステップのタスクを社内システムをまたいで実行。
- [ServiceNow AI Agents](https://www.servicenow.com/products/ai-agents.html) - 🆕 企業 IT サービスマネジメント用 AI エージェント + AI Control Tower。
- [ServiceNow MCP Server](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-opens-its-full-system-of-action-to-every-AI-Agent-in-the-enterprise/default.aspx) - 🆕 ServiceNow の MCP サーバが GA となり、すべての Now Assist / AI Native SKU に付属。すべてのアクションは AI Control Tower (AICT) を経由するため、ID 検証・権限スコープ・監査が自動で適用される。OAuth、消費量メータリング、ロールベースのツールパック、セッション管理を標準搭載。
- [IBM watsonx Orchestrate](https://www.ibm.com/products/watsonx-orchestrate) - 企業アプリをまたいで作業を自動化する AI アシスタントプラットフォーム。
- [Oracle AI Agents](https://www.oracle.com/artificial-intelligence/) - 🆕 Oracle Fusion Cloud ERP と統合された企業 AI エージェント。
- [Moveworks](https://www.moveworks.com/) - あらゆるシステムで動作する AI のエンタープライズコパイロットプラットフォーム。
- [UiPath Agentic Automation](https://www.uipath.com/) - 🆕 RPA ボット資産にエージェント推論を重ねたインテリジェントプロセス自動化。
- [AgentX](https://www.agentx.so/) - チャットボットをプラグアンドプレイで提供しスケーラブルな AI 自動化を提供する企業エージェントソリューション。
- [Amazon Bedrock AgentCore Payments](https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-bedrock-agentcore-payments-preview/) - 🆕 **2026 年 4-5 月**。Bedrock AgentCore エージェント向けのマネージド決済機能のプレビュー版。エージェントが Coinbase や Stripe の統合を通じて API などのリソースに自律的に支払うことが可能。コンプライアンス要件の高い AWS GovCloud (US-West) にも拡張。
- [OutSystems Agentic Systems Platform](https://www.outsystems.com/) - 🆕 **2026 年 6 月**。ローコードプラットフォームを「AI ネイティブ」なエージェント開発環境へとピボット。オープンかつ統制された AI 開発、自社モデル持ち込み、マルチエージェント・オーケストレーション、エンタープライズコンプライアンスツールを提供。Copilot Studio や Agentforce に対抗。
- [Sema4.ai](https://sema4.ai/) - 🆕 Python ファースト、ガバナンス内蔵の企業 AI エージェントプラットフォーム。
- [SAP Business AI Platform + Joule Studio 2.0](https://news.sap.com/2026/05/sap-sapphire-sap-unveils-autonomous-enterprise/) - 🆕 **SAP Sapphire 2026（2026-05-11～13）**。SAP は BTP + Business Data Cloud + Business AI を 1 つのプラットフォームに統合し、Joule をエージェントのオペレーティングレイヤーとして再定義。**Joule Studio 2.0**（2026-06 以降顺次顧客に提供）は LangGraph / AutoGen スタイルのフレームワークで SAP データに乗りたエージェントを構築。**Autonomous Suite** は 50+ 領域の Joule Assistant と 200+ のエージェントを導入。
- [Microsoft Agent 365 + Microsoft 365 E7](https://techcommunity.microsoft.com/blog/agent-365-blog/microsoft-365-e7--agent365-from-where-you-are-to-enterprise-ai-at-scale/4519969) - 🆕 **2026-05-01 GA**、5 月中に拡充。アイデンティティ中心の AI エージェントコントロールプレーン。単体 $15/ユーザー/月、もしくは新しい Microsoft 365 E7「Frontier」スイートに含めて $99/ユーザー/月。5 月の追加で AWS Bedrock / Google Cloud とのレジストリ同期、Intune / Defender プレビューポリシー、エージェント向け SASE を追加。
- [OpenAI Guaranteed Capacity（Compute Annual Pass）](https://openai.com/news/company-announcements/) - 🆕 **2026-05-19**。企業の AI プロダクト / エージェント / ワークフロー向けに 1 / 2 / 3 年期のコンピュート予約を製品化 —— GPT-5.5 級エージェントの企業導入でコスト / 供給不安を下げるための、Anthropic Priority Tier への製品としての回答。
- [Bristol Myers Squibb ↔ Claude Enterprise](https://news.bms.com/news/corporate-financial/2026/Bristol-Myers-Squibb-Announces-Strategic-Agreement-with-Anthropic-to-Position-Claude-Enterprise-as-the-Shared-Intelligence-Platform-Across-Its-Global-Operations/default.aspx) - 🆕 **2026-05-20**。BMS が Claude Enterprise を 30,000+ 名の社員の共通インテリジェンス基盤として採用し、創薬・開発・デリバリーの全工程にエージェント型 Claude を組み込む。世界トップ 5 製薬企業では初めての社全体規模での Claude 導入。
- [Kore.ai Artemis Agent Platform](https://venturebeat.com/technology/kore-ai-launches-artemis-ai-agent-platform-expands-challenge-to-microsoft-and-salesforce) - 🆕 **2026 年 5 月 22 日（Azure で公開）**。AI ネイティブなエンタープライズエージェント基盤。中核は新しい YAML 風の宣言型 **Agent Blueprint Language (ABL)** で、マルチエージェント workflow を記述する。Kore.ai による Copilot Studio と Agentforce への構造的な挑戦。
- [FPT Flezi Foundry™](https://lasvegassun.com/news/2026/may/22/fpt-launches-flezi-foundry-advancing-ai-augmented-/) - 🆕 **2026 年 5 月 22 日**。"Service-as-a-Software" のガバナンスを敷いた AI 強化型デリバリープラットフォーム。SDLC 全体をエージェント隊で回す **Agentic Development Lifecycle (ADLC)** と、既存 ITOps の上にインシデント解決エージェントを重ねる **Agentic Managed Services (AMS)** の 2 モードで提供。

---

## 📊 エージェント評価とオブザーバビリティ

- [LangSmith](https://www.langchain.com/langsmith) - LangChain 公式のデバッグ / 評価 / モニタリングプラットフォーム。
- [LangSmith SDK](https://github.com/langchain-ai/langsmith-sdk) - クライアント SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangsmith-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Langfuse](https://github.com/langfuse/langfuse) - オープンソース LLM エンジニアリングプラットフォーム: オブザーバビリティ + 評価 + プロンプト管理。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangfuse%2Flangfuse&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Helicone](https://github.com/Helicone/helicone) - オープンソース LLM オブザーバビリティ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHelicone%2Fhelicone&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Arize Phoenix](https://github.com/Arize-ai/phoenix) - オープンソース LLM オブザーバビリティ + 評価。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FArize-ai%2Fphoenix&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Braintrust](https://www.braintrust.dev/) - LLM 評価 + 最適化プラットフォーム。
- [LMArena (旧 LMSYS Chatbot Arena)](https://lmarena.ai/) - 🆕 クラウドソース型 LLM ベンチマーク。
- [Patronus AI](https://www.patronus.ai/) - 🆕 自動 LLM 評価 + レッドチームプラットフォーム。
- [DeepEval](https://github.com/confident-ai/deepeval) - Pytest スタイルの LLM 評価フレームワーク。組み込み 14+ メトリック。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fconfident-ai%2Fdeepeval&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agenta](https://github.com/agenta-ai/agenta) - 🆕 オールインワンオープンソース LLMOps。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagenta-ai%2Fagenta&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AutoEvals](https://github.com/braintrustdata/autoevals) - ベストプラクティスの LLM 評価スコアラーライブラリ。Braintrust 製。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbraintrustdata%2Fautoevals&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [BenchClaw](https://github.com/Agnuxo1/benchclaw) - ⚠️ **Unverified**。8 個の awesome リストのうち 7 個で却下、単独メンテナチームで2 star。**可視性のための掲載**。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAgnuxo1%2Fbenchclaw&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [PromptEden](https://www.prompteden.com) - ⚠️ **Unverified**。商用 SaaS で、ChatGPT / Claude / Gemini / Perplexity / Copilot / Grok がどうブランドを説明するかをモニタリング。同一 PR が 1 日以内に 10 個の awesome リストに提出された。**可視性のための掲載**。
- [AgentBench](https://github.com/THUDM/AgentBench) - LLM をエージェントとして評価する多次元ベンチマーク。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTHUDM%2FAgentBench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Braintrust](https://github.com/braintrustdata/braintrust-sdk) - エンタープライズ級 AI プロダクト構築スタック——評価、プロンプト playground、ロギングを一体化。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbraintrustdata%2Fbraintrust-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenLLMetry](https://github.com/traceloop/openllmetry) - OpenTelemetry に基づくオープンソースの LLM オブザーバビリティ。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftraceloop%2Fopenllmetry&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Weights & Biases Weave](https://github.com/wandb/weave) - AI アプリの開発・評価・監視ツールキット。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fwandb%2Fweave&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SWE-bench](https://github.com/princeton-nlp/SWE-bench) - 実世界のソフトウェア工学課題で LLM を評価するベンチマーク。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fprinceton-nlp%2FSWE-bench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Terminal-Bench](https://www.tbench.ai/) - 🆕 ターミナル系コーディングエージェント評価のためのベンチマーク。Harbor Framework がメンテナンス。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fharbor-framework%2Fterminal-bench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Laminar](https://github.com/lmnr-ai/lmnr) - 🆕 長時間稼働 AI エージェント専用に設計されたオープンソースのオブザーバビリティ基盤（Apache-2.0、YC S24）。OpenTelemetry ネイティブ、トランスクリプトビュー、Signals、トレース上の SQL クエリ、ブラウザエージェントのセッション再生。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flmnr-ai%2Flmnr&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangSmith Engine](https://www.langchain.com/blog/interrupt-2026-overview) - 🆕 **2026 年 5 月（Interrupt 2026）**。LangSmith の自律失敗診断レイヤー —— 本番障害を優先度付き問題にクラスタリングし、トレースとコードを横断して根本原因を特定、人間レビュー用の修正提案を生成。新発の SmithDB（Rust + DataFusion で構築されたエージェントオブザーバビリティ用 DB）と連動。

---

## 🔬 AI 研究ツール

- [Hugging Face Transformers](https://github.com/huggingface/transformers) - モデルとトレーニングツールの事実上の標準ライブラリ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhuggingface%2Ftransformers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [vLLM](https://github.com/vllm-project/vllm) - 高スループット LLM 推論・サービング。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvllm-project%2Fvllm&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SGLang](https://github.com/sgl-project/sglang) - 高性能 LLM 推論エンジン。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsgl-project%2Fsglang&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [llama.cpp](https://github.com/ggml-org/llama.cpp) - C/C++ 高性能 LLM 推論。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fggml-org%2Fllama.cpp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Ollama](https://github.com/ollama/ollama) - ローカルで LLM を走らせる最も簡単な方法。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Follama%2Follama&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LM Studio](https://lmstudio.ai/) - デスクトップでローカル LLM を動かす GUI、複数プロバイダ。
- [OpenRouter](https://openrouter.ai/) - 1 つの API で 100+ LLM を一括利用。
- [Unsloth](https://github.com/unslothai/unsloth) - 2 倍高速、VRAM 70% 削減して LLM をファインチューニング。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Funslothai%2Funsloth&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MLX](https://github.com/ml-explore/mlx) - Apple Silicon 上の機械学習フレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fml-explore%2Fmlx&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Weights & Biases](https://wandb.ai/) - ML 実験追跡 + モデル管理。
- [Label Studio](https://github.com/HumanSignal/label-studio) - マルチ型データアノテーションプラットフォーム。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHumanSignal%2Flabel-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [DSPy](https://github.com/stanfordnlp/dspy) - プロンプトではなくプログラミングして言語モデルを使うフレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstanfordnlp%2Fdspy&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hugging Face](https://huggingface.co/) - AI コミュニティのプラットフォーム——モデル、データセット、Spaces を集約する ML 研究の事実上のハブ。
- [SmithDB](https://www.langchain.com/blog/interrupt-2026-overview) - 🆕 **2026 年 5 月（Interrupt 2026）**。LangChain がエージェントオブザーバビリティ専用に設計したデータベース。Rust を Apache DataFusion + Vortex 上に構築し、オブジェクトストレージをバックエンドに —— エージェントトレースの容量とアクセスパターンに合わせて設計されている。

---

## 📚 学習リソース

### 論文

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) - ReAct パターンを定義した重要な論文。
- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) - LLM が外部ツールの使い方を自主的に学ぶ。
- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) - LLM を使った信じられる人間らしい行動エージェント。
- [LLM-based Autonomous Agents Survey](https://arxiv.org/abs/2308.11432) - LLM ベースの自律エージェントの包括的サーベイ。
- [The Rise and Potential of LLM Based Agents](https://arxiv.org/abs/2309.07864) - LLM エージェントの台頭と可能性。

### コースとチュートリアル

- [LangChain Academy](https://academy.langchain.com/) - LangGraph を含む LangChain 公式コース。
- [DeepLearning.AI Short Courses](https://www.deeplearning.ai/short-courses/) - 主要フレームワーク / プロトコルをカバーする AI ショートコース。
- [LLM Agents MOOC (Berkeley)](https://llmagents-learning.org/f24) - UC Berkeley の LLM エージェントコース。
- [Microsoft Agent Framework Docs](https://learn.microsoft.com/en-us/agent-framework/) - 🆕 Microsoft 統合エージェントフレームワークの公式ドキュメント。
- [Hugging Face Agents Course](https://github.com/huggingface/agents-course) - smolagents / LangGraph / Llama-Index でプロダクションエージェントを構築する 5 ユニットの無料コース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhuggingface%2Fagents-course&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook) - ツール使用、Computer Use、エージェントパターン、プロンプトエンジニアリング、Claude Code レシピの公式ノートブックス。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fanthropics%2Fanthropic-cookbook&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Google Gemini Cookbook](https://github.com/google-gemini/cookbook) - grounding、関数呼び出し、マルチモーダル、ライブ音声をカバーする Gemini API 公式例。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle-gemini%2Fcookbook&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LLM Course (Maxime Labonne)](https://github.com/mlabonne/llm-course) - 基礎からファインチューニングまでのエンドツーエンド LLM カリキュラム、Colab ノートブック付き。79K star。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmlabonne%2Fllm-course&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Anthropic Courses](https://github.com/anthropics/courses) - Anthropic 公式のプロンプトエンジニアリング、実世界プロンプト、評価、ツール使用のコース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fanthropics%2Fcourses&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### キュレートされたリスト

- [awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) - 💤 **Stale**（2025-02 以降更新なし）。E2B 製、プレ 2026 の参考資料。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fe2b-dev%2Fawesome-ai-agents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [awesome-llm-agents](https://github.com/kaushikb11/awesome-llm-agents) - LLM ベースのエージェントリソース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fkaushikb11%2Fawesome-llm-agents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - 🆕 MCP サーバー実装リスト。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fpunkpeye%2Fawesome-mcp-servers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [awesome-ai-agent-papers (VoltAgent)](https://github.com/VoltAgent/awesome-ai-agent-papers) - 🆕 2026 年の AI エージェント研究論文の厳選集——エージェント工学、メモリ、評価、ワークフロー、自律システムを網羅。arXiv から週次更新。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FVoltAgent%2Fawesome-ai-agent-papers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [awesome-cli-coding-agents](https://github.com/bradAGI/awesome-cli-coding-agents) - 🆕 ターミナルネイティブな AI コーディングエージェント＋オーケストレーション harness の厳選ディレクトリ—— OSS ツール（Pi / OpenCode / Aider / Goose）、プラットフォームエージェント（Claude Code / Codex / Gemini CLI）、並列ランナー、自律ループ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FbradAGI%2Fawesome-cli-coding-agents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agent Hospital](https://arxiv.org/abs/2405.02957) - 進化可能な医療エージェントを擁する仮想病院のシミュレータ。
- [Multimodal Intelligence as the Dominant Paradigm in 2026 AI Systems](https://www.researchgate.net/publication/398878301) - 🆕 マルチモーダル AI が 2026 年のデフォルトパラダイムになるという研究レビュー。
- [DeepLearning.AI — AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) - LangGraph を用いてエージェントを構築する短期コース。
- [DeepLearning.AI — Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/) - マルチエージェント・システムを構築するコース。
- [DeepLearning.AI — A2A Protocol](https://www.deeplearning.ai/short-courses/a2a-the-agent2agent-protocol/) - 🆕 Google の Agent-to-Agent プロトコルを学べる無料コース。
- [Hugging Face — Building AI Agents](https://huggingface.co/learn/agents-course/) - オープンソースツールで AI エージェントを構築するオープンコース。

---

## 🇨🇳 中国 AI エコシステム

*中国本土のチームによる、または主に中国市場を対象とする重要プロジェクト。中国スタックは、独自のフレームワーク、モデル、開発者文化を持つ並行エコシステムとしてさらに独自色を強めているため掲載。*

*中国ラボの基盤モデル（Qwen / DeepSeek / GLM / Doubao / Kimi / Hunyuan / ERNIE）は [🧠 基盤モデル](#-基盤モデル-2026) の下に直接記載。*

### エージェントプラットフォームとフレームワーク

- [Dify](https://github.com/langgenius/dify) - ビジュアルエージェントビルダー付きオープンソース LLM アプリ開発プラットフォーム。中国テックで支配的なローコードエージェントキャンバス。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flanggenius%2Fdify&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Lobe Chat](https://github.com/lobehub/lobe-chat) - マルチエージェントチャットワークスペース + プラグイン / エージェントマーケットプレイス。トップクラスの TypeScript AI プロジェクト。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flobehub%2Flobe-chat&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cozeloop](https://github.com/coze-dev/cozeloop) - 🆕 ByteDance Coze チームによるオープンソースエージェント最適化プラットフォーム。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcozeloop&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentScope](https://github.com/modelscope/agentscope) - アリババ ModelScope のマルチエージェントフレームワーク + ビジュアルデバッグ + 分散実行。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelscope%2Fagentscope&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Bisheng](https://github.com/dataelement/bisheng) - オープンエンタープライズ LLM DevOps プラットフォーム：ワークフローエディタ、RAG、エージェントオーケストレーション、ファインチューニング、評価。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdataelement%2Fbisheng&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MetaGPT](https://github.com/geekan/MetaGPT) - LLM に SOP 役割（PM / アーキテクト / エンジニア）を割り振るマルチエージェント。DeepWisdom。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgeekan%2FMetaGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### RAG / ナレッジ

- [FastGPT](https://github.com/labring/FastGPT) - ナレッジベースを中心に設計された LLM プラットフォーム: データ取り込み、RAG、ビジュアルワークフロー。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flabring%2FFastGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [QAnything](https://github.com/netease-youdao/QAnything) - 💤 NetEase Youdao 製の任意のローカルドキュメントを対象にした質問応答。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fnetease-youdao%2FQAnything&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAGFlow](https://github.com/infiniflow/ragflow) - スキャン PDF、テーブル、図表に強い深いドキュメント理解 RAG エンジン。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Finfiniflow%2Fragflow&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LightRAG](https://github.com/HKUDS/LightRAG) - 香港大学 HKUDS の軽量グラフ RAG エンジン。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2FLightRAG&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### パーソナルと生産性

- [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) - AI ワークスペースエージェント付きオープンソース Notion 代替。AGPL-3.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAppFlowy-IO%2FAppFlowy&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Manus AI](https://manus.im/) - 汎用自律エージェント（北京 Butterfly Effect）。2026 年中国テックで最も注目されたエージェント製品の一つ。
- [Coze (扣才)](https://www.coze.cn/) - ByteDance のノーコードエージェントビルダー。中国本土中心、国際版は coze.com。
- [通义千問 Agent](https://tongyi.aliyun.com/) - アリババの大衆向けコンシューマーエージェント。淘宝 / DingTalk / Quark に統合。
- [Doubao Agents](https://www.doubao.com/) - ByteDance の Doubao モデルファミリーをその上に携載したフラッグシップコンシューマーアシスタント。

### 開発者ツール

- [Kilo Code](https://www.kilocode.com/) - 2026 中国コミュニティで人気の Cursor 代替。デフォルトモデル: MiniMax。
- [CoderPlan](https://coderplan.ai/) - 中国開発者向け統合 LLM API ゲートウェイ（Claude / OpenAI / Gemini、Claude Code 一行設定対応）、従量課金制・Alipay & WeChat Pay 対応。
- [Cherry Studio](https://github.com/CherryHQ/cherry-studio) - 中国開発者サークルで最もインストールされているオープンソースデスクトップ LLM クライアント —— マルチプロバイダ会話 + ナレッジベース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FCherryHQ%2Fcherry-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ScienceOne 100 / 磐石100](https://english.cas.cn/newsroom/cas-in-media/202604/t20260429_1158251.shtml) - 🆕 中国科学院の科学推論エージェントシステム。50+ 中科院研究所、100+ 研究シナリオ、付属 2,000+ 研究ツール。
- [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code) - 🆕 **2026 年 6 月 6 日**。Moonshot AI の TypeScript / MIT 製ターミナルコーディングエージェント —— 隔離コンテキストで動く coder / explore / plan サブエージェントを内蔵、`/mcp-config` で対話式に MCP を設定。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FMoonshotAI%2Fkimi-code&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Coze Studio](https://github.com/coze-dev/coze-studio) - 🆕 ByteDance Coze.com のオープンソース対応版——オールインワン・ビジュアルエージェントビルダー、デバッグ＆デプロイツール付き。Apache-2.0、20K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 📝 比較 — サイドバイサイド表

*2026 年に最もよく出てくる「どれを選ぶ？」の判断マトリクス。*

### 🏗️ エージェントフレームワーク（オープンソース向け）

| フレームワーク | 言語 | マルチエージェント | 状態 / グラフ | ストリーミング | License | 適している用途 |
|------------|------|------------|----------------|----------------|---------|----------|
| [LangGraph](https://github.com/langchain-ai/langgraph) | Python / JS | ✅ ネイティブ | ✅ 一級社会 | ✅ | MIT | プロダクションステートフルワークフロー |
| [CrewAI](https://github.com/crewAIInc/crewAI) | Python | ✅ ロールベース | ⚠️ タスクグラフ | ✅ | MIT | ロールプレイエージェントチーム |
| [AutoGen / Microsoft Agent Framework](https://github.com/microsoft/autogen) | Python / .NET | ✅ 会話型 | ⚠️ Group Chat | ✅ | CC-BY-4.0 / MIT | エンタープライズマルチエージェント |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | Python | ✅ handoff | ❌ | ✅ | MIT | OpenAI ネイティブ本番 |
| [Mastra](https://github.com/mastra-ai/mastra) | TypeScript | ✅ | ✅ workflows | ✅ | Elastic-2.0 | TypeScript ファースト |
| [Google ADK](https://github.com/google/adk-python) | Python / Java | ✅ 階層 | ⚠️ | ✅ | Apache-2.0 | Gemini + Vertex AI |
| [DSPy](https://github.com/stanfordnlp/dspy) | Python | ⚠️ モジュール経由 | ⚠️ プログラム型 | ✅ | MIT | プログラム的プロンプト最適化 |
| [Phidata / Agno](https://github.com/phidatahq/phidata) | Python | ✅ teams | ❌ | ✅ | MPL-2.0 | メモリ付きマルチモーダルエージェント |

### 🧪 サンドボックス（エージェント生成コードを実行）

| サンドボックス | ホスティング | コールドスタート | 言語 | 永続化 | License | 適している用途 |
|--------------|--------------|------|------|---------|---------|----------|
| [E2B](https://github.com/e2b-dev/E2B) | クラウド（マネージド） | ~150ms | Python / Node / shell | セッション単位 | Apache-2.0 | OpenAI Agents SDK / 本番 |
| [Daytona](https://github.com/daytonaio/daytona) | クラウド / セルフ | ~500ms | 多言語 | 永続ワークスペース | AGPL-3.0 | 長期実行型タスク |
| [Modal](https://modal.com/) | クラウド（マネージド） | ~200ms | Python | 関数単位 | プロプラエタリ | GPU + サーバーレスエージェント |
| [Microsandbox](https://github.com/superradcompany/microsandbox) | ローカル microVM | ~100ms | 多言語 | セッション単位 | Apache-2.0 | プライバシー重視ローカル |
| [SandboxFusion](https://github.com/bytedance/SandboxFusion) | セルフ | ~300ms | 20+ 言語 | 一時的 | Apache-2.0 | 評価 / ベンチマークパイプライン |

### 🌐 ブラウザエージェントスタック

| スタック | アプローチ | ホスティング | 強み | License |
|----------|------------|--------------|------|---------|
| [Browser Use](https://github.com/browser-use/browser-use) | Vision + DOM（Playwright） | セルフ | 92K star、最大コミュニティ | MIT |
| [Stagehand](https://github.com/browserbase/stagehand) | 型付き act/extract/observe | Browserbase / セルフ | 型・構造化出力 | MIT |
| [Steel Browser](https://github.com/steel-dev/steel-browser) | ヘッドレス API | セルフ / クラウド | セッション・プロキシ・キャプチャ対応 | Apache-2.0 |
| [Skyvern](https://github.com/Skyvern-AI/skyvern) | ビジョンファースト | セルフ | 動的ページに強い | AGPL-3.0 |
| [AgentQL](https://github.com/tinyfish-io/agentql) | クエリ言語 | SDK + セルフ | セマンティックなセレクタ | MIT |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | MCP ネイティブ | セルフ | MCP クライアントでプラグイン | Apache-2.0 |

### 📊 評価とオブザーバビリティ

| ツール | セルフ | OpenTelemetry | 評価スイート | プロンプト管理 | License |
|------|--------|----------|------------|------------|---------|
| [Langfuse](https://github.com/langfuse/langfuse) | ✅ | ✅ | ✅ | ✅ | MIT |
| [Helicone](https://github.com/Helicone/helicone) | ✅ | ✅ | ⚠️ 基本 | ✅ | Apache-2.0 |
| [Arize Phoenix](https://github.com/Arize-ai/phoenix) | ✅ | ✅ | ✅ | ⚠️ | Elastic-2.0 |
| [LangSmith](https://www.langchain.com/langsmith) | ❌（クラウドのみ） | ✅ | ✅ | ✅ | プロプラエタリ |
| [Braintrust](https://www.braintrust.dev/) | ❌（クラウドのみ） | ✅ | ✅ | ✅ | プロプラエタリ |
| [DeepEval](https://github.com/confident-ai/deepeval) | ✅（ライブラリ） | ⚠️ Confident 経由 | ✅ | ❌ | Apache-2.0 |
| [Agenta](https://github.com/agenta-ai/agenta) | ✅ | ✅ | ✅ | ✅ | Apache-2.0 |
| [OpenLLMetry](https://github.com/traceloop/openllmetry) | ✅（計装） | ✅ ネイティブ | ❌ | ❌ | Apache-2.0 |

### 💻 コーディングエージェント——ヘッドライン選択

| ツール | サーフェース | オープンソース | 無料層 | SWE-bench | 適している用途 |
|------|----------|------------|--------|-----------|----------|
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | CLI / IDE | ❌ | ⚠️ Pro | 80.9% | 長期エンジニアリング |
| [Codex CLI](https://github.com/openai/codex) | CLI | ✅ | ✅ | n/a（Terminal-Bench 77.3%） | OpenAI ネイティブ shell |
| [Cursor](https://www.cursor.com/) | IDE | ❌ | ✅（限定的） | n/a | ペアプログラミング体験 |
| [Cline](https://github.com/cline/cline) | VS Code 拡張 | ✅ | ✅（BYO） | n/a | OSS IDE 代替 |
| [Aider](https://github.com/Aider-AI/aider) | CLI | ✅ | ✅（BYO） | Polyglot で強い | Git 意識リファクタリング |
| [Devin 3.0](https://www.cognition.ai/) | クラウド | ❌ | ❌ | トップ | ハンズオフ長期タスク |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | セルフ | ✅ | ✅ | 競争力あり | セルフ型 SWE エージェント |

*表は 2026-05-05 に検証済み。数値の変更はソース付きで PR を送付してください。*

---

### 💰 基盤モデル — API コスト & コンテキスト

*価格は USD/100万トークン。データ：2026-05-20。*

| モデル | プロバイダー | コンテキスト | 入力 $/1M | 出力 $/1M | 最適用途 |
|-------|----------|---------------|-----------|------------|----------|
| GPT-4o | OpenAI | 128K | $2.50 | $10.00 | 幅広いツール利用・ビジョン |
| GPT-4o-mini | OpenAI | 128K | $0.15 | $0.60 | 大量の単純タスク |
| Claude Sonnet 4.6 | Anthropic | 200K | $3.00 | $15.00 | コーディングエージェント・複雑推論 |
| Claude Opus 4.7 | Anthropic | 200K | $5.00 | $25.00 | 最難度推論タスク |
| Claude Haiku 4.5 | Anthropic | 200K | $1.00 | $5.00 | Anthropic エコシステムの高速タスク |
| Gemini 2.5 Flash | Google | 1M | $0.30 | $2.50 | コスパ重視マルチモーダル |
| Gemini 2.5 Pro | Google | 2M | $1.25 | $10.00 | 超長文・マルチモーダル |
| Gemini 2.5 Flash-Lite | Google | 1M | $0.10 | $0.40 | 超低コスト大量リクエスト |
| DeepSeek V3.2 | DeepSeek | 128K | $0.14 | $0.28 | 低コストコーディング推論 |
| Qwen3 235B A22B | Alibaba | 131K | ~$0.29 | ~$1.15 | 最強中国語+コーディング MoE |
| Kimi K2.6 | Moonshot AI | 262K | ~$0.60 | ~$2.50 | 中国語+超長コンテキスト |
| Grok 4 | xAI | 256K | $3.00 | $15.00 | X/Twitter エコシステム推論 |
| Grok 4.20 | xAI | 2M | $2.00 | $6.00 | 超長コンテキスト・エージェントタスク |

---

### 💻 基盤モデル — ローカルデプロイ

*Q4_K_M 量子化での推定 VRAM。速度はハードウェアにより変動。*

| モデル | パラメータ | 最小 VRAM（Q4） | 速度（tok/s） | 推奨量子化 | 中国語対応 | 最適用途 |
|-------|--------|--------------|----------------|-------------------|-----------------|----------|
| Qwen3.6-27B | 27B dense | ~17 GB | ~23（M5 Max） | Q4_K_M / FP8 | ⭐⭐⭐⭐⭐ | コーディング・中国語・エージェント |
| Qwen3 235B A22B | 235B MoE | ~40 GB（アクティブ） | ~15–20 | Q2_K / Q4_K_M | ⭐⭐⭐⭐⭐ | ローカル最高品質 |
| Llama 3.3 70B | 70B dense | ~42 GB | ~12–18 | Q4_K_M | ⭐⭐☆☆☆ | 最強英語オープンウェイト |
| DeepSeek V3-671B | 671B MoE | ~40 GB（アクティブ） | ~10–15 | Q2_K | ⭐⭐⭐⭐☆ | オープンウェイトコーディング |
| Gemma 4 27B | 27B dense | ~17 GB | ~20–25 | Q4_K_M | ⭐⭐⭐☆☆ | 多言語推論 Apache-2.0 |
| Phi-4 14B | 14B dense | ~9 GB | ~35–45 | Q4_K_M | ⭐⭐☆☆☆ | 8–16GB VRAM コーディング |
| Mistral Small 4 24B | 24B dense | ~14 GB | ~25–30 | Q4_K_M | ⭐⭐⭐☆☆ | 多言語・関数呼び出し |

---

### 🧠 エージェントメモリシステム

| システム | ストレージ | 検索 | ローカル | セルフホスト | 時系列 | ライセンス | 最適用途 |
|--------|---------|-----------|-------|-----------|----------|---------|----------|
| Mem0 | ベクター+グラフ | セマンティック | ✅ | ✅ | ✅ | Apache-2.0 | 任意 LLM アプリへの即時メモリ |
| Basic Memory | Markdown ファイル | キーワード+埋め込み | ✅ | ✅ | ⚠️ | MIT | 人間が読める、Obsidian 互換 |
| Graphiti | 時系列知識グラフ | グラフ走査 | ✅ | ✅ | ⭐ ネイティブ | Apache-2.0 | 時間認識エージェントメモリ |
| Zep | ベクター+要約 | セマンティック | ✅ | ✅ | ✅ | Apache-2.0 | 本番チャットエージェントメモリ |
| Letta (MemGPT) | 階層ストレージ | ページ検索 | ✅ | ✅ | ✅ | Apache-2.0 | 無限コンテキスト錯覚メモリ |

---

### 🎙️ 音声・オーディオモデル

| モデル/サービス | STT | TTS | リアルタイム | ローカル | レイテンシ | 言語 | ライセンス |
|----------------|-----|-----|---------|-------|---------|-----------|--------|
| ElevenLabs v3 | ❌ | ⭐⭐⭐⭐⭐ | ✅ | ❌ | ~200ms | 32+ | プロプライエタリ |
| Whisper v3（ローカル） | ⭐⭐⭐⭐★ | ❌ | ❌ | ✅ | ~1s | 99 | MIT |
| Deepgram Nova-3 | ⭐⭐⭐⭐⭐ | ✅ | ✅ | ❌ | <100ms | 30+ | プロプライエタリ |
| Gemini Live API | ✅ | ✅ | ⭐ ネイティブ | ❌ | <300ms | 30+ | プロプライエタリ |
| OpenAI Realtime API | ✅ | ✅ | ⭐ ネイティブ | ❌ | ~300ms | 57 | プロプライエタリ |
| Kokoro | ❌ | ⭐⭐⭐⭐☆ | ❌ | ✅ | ~100ms | 8 | Apache-2.0 |
| Voxtral | ⭐⭐⭐⭐☆ | ❌ | ❌ | ✅ | バッチ | 20+ | Apache-2.0 |

---

### 🎨 画像生成モデル

| モデル | 最大解像度 | API/ローカル | フォトリアリズム | 最適用途 | 価格目安 |
|-------|---------------|-------------|-------------|----------|------------------|
| DALL-E 3 | 1024×1024 | API | 高 | 命令追従 | $0.04/枚（標準） |
| gpt-image-2 | 2048×2048 | API | 非常に高い | API ワークフロー・4K | $0.04–$0.17/枚 |
| Flux 2 Pro | 2K+ | API | ⭐高い | フォトリアル・高速 | ~$0.05/枚 |
| Midjourney V8 | 2K+ | Web のみ | 芸術的品質最高 | アート制作 | $10–$120/月 |
| Stable Diffusion 3.5 | 2K | ローカル+API | 良好 | OSS・セルフホスト | Apache-2.0 |
| Ideogram 3 | 2K | API+Web | 良好 | 画像内テキスト最強 | フリーミアム |

---

### 🎥 動画生成モデル

| モデル | 最大長 | 解像度 | API/ローカル | 最適用途 | ステータス |
|-------|-----------|-----------|-------------|----------|------------------|
| Veo 3.1 | 2分 | 4K | API（Vertex） | 最高忠実度 | GA（Google） |
| Kling VIDEO 3.0 | 3分 | 1080p | API+Web | 映画スタイル先頭 | GA（Kuaishou） |
| Runway Gen-4 | 10s/クリップ | 1080p | API+Web | 精密モーション制御 | GA |
| Seedance 2.0 | 60s | 1080p | API | 高速・コスパ良好 | GA（ByteDance） |
| ~~Sora~~ | ❌ | ❌ | ❌ | — | **2026年4月廃止** |

---

### 🔍 RAG フレームワーク

| フレームワーク | 言語 | ベクター DB | ハイブリッド検索 | ストリーミング | ライセンス | 最適用途 |
|-----------|---------|-----------|--------------|-----------|---------|----------|
| LlamaIndex | Python | 任意 | ✅ | ✅ | MIT | 本番 RAG・ドキュメントパイプライン |
| Haystack | Python | 任意 | ✅ | ✅ | Apache-2.0 | 検索重視 RAG |
| LangChain LCEL | Python/JS | 任意 | ✅ | ✅ | MIT | 柔軟・大きなエコシステム |
| RAGFlow | Python | 内蔵 | ✅ | ✅ | Apache-2.0 | 深いドキュメント解析・OCR |
| Cognee | Python | ベクター+グラフ | ✅ | ⚠️ | Apache-2.0 | 知識グラフ+RAG ハイブリッド |
| txtai | Python | 内蔵 | ✅ | ❌ | Apache-2.0 | 軽量埋め込み重視 |

---

### 🗄️ ベクターデータベース

| DB | セルフホスト | クラウド | スケール | ハイブリッド検索 | ライセンス | 最適用途 |
|----------|-----------|-------|-------|--------------|---------|----------|
| Qdrant | ✅ | ✅ | 大規模 | ✅ | Apache-2.0 | 最も優れた OSS ベクター DB |
| Weaviate | ✅ | ✅ | 大規模 | ✅ | BSD-3 | マルチモーダル・GraphQL |
| Pinecone | ❌ | ✅ | 大規模 | ✅ | プロプライエタリ | マネージド・最も簡単 |
| Chroma | ✅ | ⚠️ | 中規模 | ❌ | Apache-2.0 | 高速プロトタイプ・Python |
| Milvus | ✅ | ✅ | 10億スケール | ✅ | Apache-2.0 | 本番10億スケール |
| pgvector | ✅ | ✅ | 中規模 | ⚠️ | PostgreSQL | 既存 Postgres 拡張 |

---

### 📱 パーソナル AI アシスタント（2026）

| ツール | OSS | ローカル LLM | メモリ | マルチチャネル | セルフホスト | 最適用途 |
|------|------------|-----------|--------|--------------|-----------|----------|
| OpenClaw | ❌ | ✅ | ✅ ネイティブ | ✅（TG/Discord/WA） | ✅ | オールインワン個人エージェント |
| Khoj | ✅ | ✅ | ✅ | ⚠️ | ✅ | 調査・ノート・カレンダー |
| Jan.ai | ✅ | ✅ | ❌ | ❌ | ✅ | オフライン ChatGPT 代替 |
| Claude.ai Pro | ❌ | ❌ | ✅ Projects | ❌ | ❌ | 最高推論+MCPツール |
| Perplexity | ❌ | ❌ | ⚠️ | ❌ | ❌ | 検索優先・引用付き |

---

### 🔌 MCP サーバー — 主要インテグレーション

| MCP サーバー | カテゴリ | 認証 | セキュリティ監査 | ライセンス |
|-----------|----------|------|---------------|--------|
| GitHub MCP | 開発/コード | OAuth | ✅（GitHub） | MIT |
| Playwright MCP | ブラウザ | なし（ローカル） | ⚠️ | Apache-2.0 |
| Filesystem MCP | ファイル | なし（ローカル） | ⚠️ サンドボックス要 | MIT |
| Brave Search MCP | 検索 | API キー | ❌ | MIT |
| Slack MCP | 通信 | OAuth | ❌ | MIT |
| Notion MCP | ノート | OAuth | ❌ | MIT |
| PostgreSQL MCP | DB | 接続文字列 | ⚠️ 読み取り専用推奨 | MIT |

*本番デプロイ前に **mcp-scan**（Invariant Labs）で全 MCP サーバーを監査してください。*

---

### 🏢 エンタープライズ AI エージェントプラットフォーム

| プラットフォーム | OSS | MCP | A2A | セルフホスト | コンプライアンス | 最適用途 |
|---------|------------|------------|------------|-----------|-----------|----------|
| Microsoft Agent Framework | ⚠️ | ✅ | ✅ | ⚠️（Azure） | SOC2, ISO | Azure ネイティブ企業 |
| Salesforce Agentforce | ❌ | ⚠️ | ❌ | ❌ | SOC2, GDPR | Salesforce CRM 組織 |
| Google Gemini Enterprise | ❌ | ✅ | ✅ | ❌ | SOC2, FedRAMP | Google Workspace |
| IBM watsonx | ⚠️ | ✅ | ⚠️ | ✅（オンプレ） | FedRAMP, HIPAA | 規制/オンプレ企業 |
| Dify Enterprise | ✅（CE） | ✅ | ✅ | ✅ | SOC2（クラウド） | マルチモデル低コード |

---

### 📏 埋め込みモデル

| モデル | 次元 | コンテキスト | ローカル | API | 言語 | ライセンス | MTEB ≈ |
|-------|------|---------|-------|-----|-----------|---------|--------|
| OpenAI text-embedding-3-large | 3072 | 8K | ❌ | ✅ | 多言語 | プロプライエタリ | ~64 |
| Cohere embed-v4 | 1024 | 512 | ❌ | ✅ | 多言語 | プロプライエタリ | ~66 |
| BGE-M3 | 1024 | 8K | ✅ | ❌ | 多言語 | MIT | ~65 |
| Jina-embeddings-v3 | 1024 | 8K | ✅ | ✅ | 多言語 | CC-BY-NC | ~65 |
| Nomic-embed-text-v2 | 768 | 8K | ✅ | ✅ | 多言語 | Apache-2.0 | ~62 |
| Voyage-3 | 1024 | 32K | ❌ | ✅ | 多言語 | プロプライエタリ | ~67 |

---

### 🛡️ エージェントセキュリティツール

| ツール | MCP スキャン | プロンプトインジェクション防御 | 監査ログ | セルフホスト | ライセンス |
|------|---------|------------------------|-----------|-----------|--------|
| mcp-scan | ⭐ ネイティブ | ✅ | ❌ | ✅ | MIT |
| Lakera Guard | ❌ | ⭐⭐⭐⭐⭐ | ✅ | ❌ | プロプライエタリ |
| Zenity | ✅ | ✅ | ✅ | ❌ | プロプライエタリ |
| Azure AI Content Safety | ❌ | ✅ | ✅ | ❌（Azure） | プロプライエタリ |
| Rebuff | ❌ | ⭐⭐⭐⭐☆ | ❌ | ✅ | MIT |

---

### 🖥️ コンピュータ使用 & デスクトップエージェント

| ツール | OS | ビジョン | ローカル | API | OSS | 最適用途 |
|------|----|----|-------|-----|------------|----------|
| Claude Desktop Intelligence | Mac/Linux | ✅ | ❌ | ✅ | ❌ | 最も優れたスクリーンエージェント |
| UFO（Microsoft） | Windows | ✅ | ✅ | オプション | ✅ | Windows ネイティブ自動化 |
| OSWorld | Mac/Win/Linux | ✅ | ✅ | オプション | ✅ | クロスプラットフォームベンチマーク |
| Screenpipe | Mac/Linux | ✅ | ✅ | ❌ | ✅ | スクリーンメモリ・プライバシー重視 |

---

### 🤖 Physical AI プラットフォーム

| プラットフォーム | タイプ | OSS | SDK | シミュレーション | 最適用途 |
|---------|------|------------|-----|-----------|----------|
| NVIDIA Isaac GR00T N1.5 | ヒューマノイド基盤 | ⚠️（重み） | ✅ | ✅ Isaac Sim | 汎用ヒューマノイド基盤モデル |
| ROS 2 Jazzy | ロボット OS | ✅ | ✅ | ✅ Gazebo | 標準ロボットミドルウェア |
| Gemini Robotics | 巧みな操作 | ❌ | ⚠️ | ✅ | 視覚+言語+巧みな操作 |
| Unitree SDK2 | 四足/ヒューマノイド | ✅ | ✅ | ⚠️ | Go2, H1, G1 開発 |
| Genesis Sim | シミュレーション | ✅ | ✅ | ⭐ ネイティブ | 超高速物理シミュレーション |

---

### 🇨🇳 中国語 AI モデル — ヘッドトゥヘッド

| モデル | プロバイダー | コンテキスト | 中国語能力≈ | コーディング | オープン重み | 入力 $/1M |
|-------|----------|---------|---------------|--------|------------|----------|
| Qwen3 235B A22B | Alibaba | 131K | トップ | ⭐⭐⭐⭐⭐ | ✅ Apache-2.0 | ~$0.29 |
| DeepSeek V3.2 | DeepSeek | 128K | 非常に高い | ⭐⭐⭐⭐⭐ | ✅ MIT | $0.14 |
| Kimi K2.6 | Moonshot AI | 262K | 高い | ⭐⭐⭐⭐☆ | ❌ | ~$0.60 |
| GLM-5.1 | Zhipu AI | 128K | 高い | ⭐⭐⭐⭐☆ | ⚠️ 部分 | ~$0.50 |
| Hunyuan Pro | Tencent | 256K | 高い | ⭐⭐⭐⭐☆ | ❌ | ~$0.45 |
| Doubao Pro | ByteDance | 256K | 高い | ⭐⭐⭐☆☆ | ❌ | ~$0.80 |
| ERNIE 5 | Baidu | 128K | 高い | ⭐⭐⭐☆☆ | ❌ | ~$0.70 |

---

### 📦 エージェントフレームワーク — TypeScript / JavaScript

| フレームワーク | マルチエージェント | ストリーミング | MCP | A2A | スター≈ | ライセンス |
|-----------|-----------|----------|-----|-----|-------|---------| 
| Mastra | ✅ | ✅ | ✅ | ✅ | ~12K | Elastic-2.0 |
| Vercel AI SDK | ⚠️ | ✅ | ✅ | ❌ | ~12K | Apache-2.0 |
| LangChain.js | ✅ | ✅ | ✅ | ❌ | ~14K | MIT |
| Genkit | ✅ | ✅ | ✅ | ❌ | ~3K | Apache-2.0 |
| OpenAI Agents SDK (Node) | ✅ | ✅ | ✅ | ❌ | ~2K | MIT |
| Flowise | ✅ | ✅ | ✅ | ❌ | ~35K | Apache-2.0 |

---

### 📊 メタ比較 — オーケストレーション vs フレームワーク vs IDE

| カテゴリ | 代表ツール | 最適対象 | 抽象レベル | 柔軟性 |
|---------|--------------|----------|--------------------|-------------|
| オーケストレーションプラットフォーム | Dify, n8n, Flowise | 非エンジニア・高速展開 | 非常に高い | 低〜中 |
| エージェントフレームワーク | LangGraph, CrewAI, Mastra | エンジニアカスタム | 中程度 | 高い |
| エージェント IDE | Claude Code, Cursor, Cline | 開発者ペアプロ | 低い | 非常に高い |
| ローコードビルダー | Voiceflow, Botpress | ビジネス/プロダクト | 非常に高い | 低い |
| AI ネイティブプラットフォーム | Vertex AI Agent Builder | エンタープライズ管理 | 高い | 中程度 |

---

### 📱 モバイル AI フレームワーク

| フレームワーク | iOS | Android | ローカル LLM | オンデバイス推論 | ライセンス | 最適用途 |
|-----------|-----|---------|-----------|--------------------|---------|-----------| 
| MLX | ✅ | ❌ | ✅ | ⭐ Apple Silicon | MIT | Apple ネイティブ高速 LLM |
| llama.cpp（モバイル） | ✅ | ✅ | ✅ | ✅ | MIT | 全プラットフォーム汎用ローカル LLM |
| MediaPipe | ✅ | ✅ | ✅ | ✅ | Apache-2.0 | オンデバイス ML |
| Core ML | ✅ | ❌ | ✅ | ✅（ANE） | Apple SDK | iOS/macOS ネイティブ推論 |
| Google AI Edge | ✅ | ✅ | ✅ | ✅ | Apache-2.0 | Gemma Nano オンデバイス |
| Qualcomm AI Hub | ❌ | ✅ | ✅ | ✅（Snapdragon NPU） | SDK | Snapdragon 最適化展開 |

*全比較表データ：2026-05-20。数値変更は PR でご報告を。*

---

---

## 🗺️ シナリオガイド — 何に何を使うべきか

*50+ シナリオと適切なツールの対応。毎週更新。*

---

### 🏗️ 構築: コーディングエージェント

**スタートアップに最も低コスト・高品質なコーディングエージェントを作りたい**
→ **Claude Code**（CLI）+ **E2B** サンドボックス + **Langfuse** 可観測性。SWE-bench 80.9%。~$200/月。

**エンタープライズ向けセキュリティ付きコーディングエージェント**
- **GitHub Copilot Enterprise** — GitHub 深い統合・IP 補償・SSO/SAML。
- **Cursor Business** — プライバシーモード・コードが社外に出ない。
- **Devin 3.0** — 自動再計画・完全自律。

**オープンソースのセルフホストコーディングエージェント**
- **OpenHands** — MIT、セルフホスト、モデル選択自由。
- **Cline**（VS Code 拡張）— BYO キー、活発なコミュニティ。
- **Aider** — Git 対応 CLI リファクタリング。

**ブラウザ自動化 / Web スクレイピングエージェント**
- **Browser Use** — 92K スター、最大コミュニティ。
- **Stagehand** — 強い型付け + 構造化出力。
- **Skyvern** — ビジョン優先、動的ページに強い。

**ドキュメント処理 / PDF 分析エージェント**
→ **LlamaIndex** + **Gemini 2.5 Pro**（2M コンテキスト）または **Claude Opus 4.7** + **Unstructured.io**。

**カスタマーサービスエージェント**
- **Dify** — ノーコード・内蔵 RAG・セルフホスト可能。
- **LangGraph + Zendesk MCP** — エンジニア主導。
- **Salesforce Agentforce** — CRM ネイティブ。

**深い調査エージェント**
→ **Perplexity Deep Research**（マネージド）または **OpenHands + Tavily + Claude Opus 4.7**。

**データ分析 / BI エージェント**
- **Julius AI** — エンジニア不要、マネージド。
- **[AI for Database](https://aifordatabase.com)** — ⚠️ Unverified。自然言語で Postgres / MySQL / MongoDB / SQL Server / SQLite + Sheets を直接クエリ、自己更新ダッシュボードと Slack / Webhook / メールトリガー。SOC 2 + GDPR、セルフホスト可、Pro $19/月。→ SQL を書けない非エンジニアチーム向け。
- **LangChain + Pandas Agent** — 完全カスタム。

**コンピュータ使用 / デスクトップエージェント**
- **Claude Desktop Intelligence** — macOS/Linux で最も全面的。
- **UFO**（Microsoft）— Windows ネイティブ。
- **Screenpipe** — ローカルプライバシー優先。

**音声 / 会話エージェント**
- **Gemini Live API** — <300ms 遅延。
- **OpenAI Realtime API** — ネイティブ音声+ツール呼び出し。
- **LiveKit + Whisper + ElevenLabs v3** — 完全セルフホスト。

**マルチエージェントオーケストレーション**
- **LangGraph** — Python 本番ステートフルグラフ。
- **Google ADK** — 階層エージェント + Gemini。
- **Mastra** — TypeScript ファースト。

**パーソナル AI アシスタント（セルフホスト）**
→ **OpenClaw** — マルチチャネル・メモリ・cron・MCP・完全セルフホスト。

**パーソナル AI アシスタント（マネージド）**
- **Claude.ai Pro** — 最高推論+MCPツール。
- **Perplexity Pro** — 検索優先。

**RAG アプリケーション**
→ **LlamaIndex** + **Qdrant** + **Cohere embed-v4** + **BGE リランカー**。

**金融分析エージェント**
→ **LangChain** + **yfinance MCP** + **Claude Sonnet 4.6** + 構造化出力検証。

**法律文書エージェント**
→ **Claude Opus 4.7**（200K コンテキスト）+ **LlamaIndex** + **pgvector**。人間によるレビューを必ず残すこと。

**セキュリティスキャンエージェント**
→ **Semgrep** + **Claude Sonnet 4.6** + **mcp-scan**。

---

### 🧠 モデル選択

**最も難しい推論タスクに最高のモデルが必要**
- **Claude Opus 4.7** (/think xhigh) — $5/$25/1M。
- **Gemini 2.5 Pro** — 2M コンテキスト、$1.25/$10。

**最速・最安モデル（シンプルな大量タスク）**
- **Gemini 2.5 Flash-Lite** — $0.10/$0.40/1M。
- **DeepSeek V3.2** — $0.14/$0.28/1M。

**最高の中国語対応**
- **Qwen3 235B A22B** — 中国語ベンチマーク首位。
- **Kimi K2.6** — 262K コンテキスト。

**16GB VRAM でのローカルモデル**
- **Qwen3.6-27B Q4_K_M** — ~17GB、最良の 16GB 選択肢。

**40GB+ VRAM でのローカルモデル**
- **Llama 3.3 70B Q4_K_M** — ~42GB。
- **Qwen3 235B A22B Q2** — MoE フラグシップ。

**オープンウェイトモデル（MIT/Apache）**
- **Llama 3.3 70B** (Apache-2.0)、**DeepSeek V3.2** (MIT)、**Qwen3 235B A22B** (Apache-2.0)。

---

### 🏗️ インフラ

**完全ローカル実行（プライバシー優先）**
→ **Ollama** + **Open WebUI** + **Qdrant** + **Qwen3.6-27B** or **Llama 3.3 70B**。

**API コストを最小化（月 <$50）**
→ **DeepSeek V3.2** + **Gemini 2.5 Flash** + Anthropic Batch API 割引。

**ベンダーロックインを避ける**
→ **LiteLLM** + **LangGraph** + **BGE-M3 埋め込み**。

---

### 📊 評価 & モニタリング

**エージェント出力品質の評価** → **DeepEval** + **Langfuse**。

**エージェント失敗原因のデバッグ** → **Langfuse** トレース + **Arize Phoenix**。

**本番エージェントのリアルタイム監視** → **Langfuse** または **Helicone**。

**MCP サーバーのセキュリティ評価** → **mcp-scan**（Invariant Labs）。

---

## 📋 スタックレシピ — 実証済みツール組み合わせ

| # | レシピ名 | スタック | 最適対象 |
|---|------------|-------|----------|
| 1 | **軽量コーディング Agent** | Claude Code + E2B + Langfuse | 個人開発/スタートアップ |
| 2 | **OSS SWE エージェント** | OpenHands + Ollama + Qwen3.6-27B + Qdrant | 完全ローカル・プライバシー重視 |
| 3 | **エンタープライズ RAG** | LlamaIndex + Qdrant + Cohere embed-v4 + Langfuse | 社内文書 Q&A |
| 4 | **音声アシスタント** | LiveKit + Whisper + Claude Sonnet 4.6 + ElevenLabs v3 | カスタム音声 AI |
| 5 | **ブラウザ自動化** | Browser Use + Stagehand + Claude Sonnet 4.6 | 信頼性の高い Web スクレイピング |
| 6 | **ローカルプライバシースタック** | Ollama + Qwen3.6-27B + Open WebUI + Qdrant + n8n | ゼロクラウド・オフライン |
| 7 | **TypeScript エージェント** | Mastra + Vercel AI SDK + Gemini 2.5 Flash + Qdrant | TS ファースト本番 SaaS |
| 8 | **中国市場スタック** | Qwen3 235B API + RAGFlow + Milvus + Langfuse | 国内デプロイ・ICP 対応 |

---

## ⚠️ アンチピック — 使ってはいけないケース

| ❌ 使わない | ❌ このために | ✅ 代わりに | 理由 |
|------------|-----------|---------------|-----|
| LangChain v0.x | 新しい本番エージェント | **LangGraph** | 旧 chain は廃止済み |
| AutoGPT（レガシー） | 本番ワークロード | **OpenHands / LangGraph** | アーキテクチャが古く信頼性が低い |
| GPT-3.5-Turbo | 複雑な推論 | **Gemini 2.5 Flash / Claude Haiku 4.5** | 廃止済み、同価格帯により良い選択肢がある |
| Pinecone Starter | セルフホスト/コスト重視 | **Qdrant / pgvector** | 2025 年に無料プラン廃止 |
| LLM で実時間株取引 | 金融執行 | 確定的ルールエンジン | LLM は数値を幻覚する；実取引では壊滅的 |
| ChatGPT Plus | 本番 API ワークフロー | **OpenAI API** 直接 | SLA なし・レート制御なし |
| Midjourney | プログラマティック画像生成 | **gpt-image-2 / Flux 2 Pro API** | 公開 API なし |
| Sora | 動画生成 | **Kling VIDEO 3.0 / Veo 3.1** | 2026年4月廃止 |
| リランカーなしのベクター検索 | 高精度 RAG | ベクター DB + **BGE リランカー** | 純ベクター検索の再現率は ~70% のみ |

---

## 🌟 2026 年に注目すべきエージェントプロジェクト

*2026 年の AI エージェント状況を形作ったシグネチャーと出来事。*

- [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol/servers) - エージェントツール連携のユニバーサル標準となった。Linux Foundation へ寄贈された。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Fservers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [A2A Protocol](https://github.com/google/A2A) - 🆕 Google の A2A プロトコルで 150+ パートナーとクロスフレームワーク連携を可能にした。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle%2FA2A&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - SWE-bench 80.9% で 2026 年のターミナル型コーディングエージェントの選択肢となった。
- [Kiro](https://kiro.dev/) - 🆕 AWS が 10 タスク同時管理可能な自律コーディングエージェントをローンチ。
- [Devin 3.0](https://www.cognition.ai/) - 🆕 動的再プラン、自己修復コード、レガシーコードベース移行を含む進化。
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/) - 🆕 AutoGen + Semantic Kernel が統一企業エージェントプラットフォームとして統合。
- [OpenAI Codex CLI](https://github.com/openai/codex) - OpenAI のオープンソースターミナルエージェント参入。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fcodex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Browser Use](https://github.com/browser-use/browser-use) - AI エージェントが Web と自然に対話できるようにしたブレイクスルー。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowser-use%2Fbrowser-use&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude Computer Use](https://www.anthropic.com/) - 🆕 Desktop Intelligence により Claude が画面を見てあらゆるソフトウェアをコントロール。
- [Manus AI](https://manus.im/) - 🇨🇳 🆕 調査、コーディング、複雑ワークフローを処理できる汎用自律エージェント。
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) - オープンソース AI ソフトウェアエンジニアリングプラットフォームが広く採用された。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAll-Hands-AI%2FOpenHands&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Dify](https://github.com/langgenius/dify) - 🇨🇳 ローコード LLM エージェントプラットフォームが主流に達した。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flanggenius%2Fdify&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cline](https://github.com/cline/cline) - VS Code の自律コーディングエージェントがコミュニティで急長。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcline%2Fcline&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Mem0](https://github.com/mem0ai/mem0) - AI のメモリ層がエージェントアーキテクチャの不可欠な要素になった。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmem0ai%2Fmem0&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Sora サービス終了](https://openai.com/) - 🆕 OpenAI が 2026 年 4 月に Sora を停止、エンタープライズ AI と推論への戦略転換を示した。
- [Kling VIDEO 3.0](https://kling.ai/) - 🇨🇳 🆕 快手製動画生成が Sora 停止後の AI 動画プラットフォームをリード。
- [Cohere + Aleph Alpha 合併](https://siliconangle.com/2026/04/24/ai-startups-cohere-aleph-alpha-merge-600m-new-funding/) - 🆕 **2026-04-24**。カナダとドイツの AI 企業が約 $20B 評価額で合併、Schwarz Group から $600M シリーズ E。跨大西洋「主権 AI」パワーハウス。
- [ScienceOne 100 / 磐石100](https://english.cas.cn/newsroom/cas-in-media/202604/t20260429_1158251.shtml) - 🇨🇳 🆕 **2026-04-28~29**。中国科学院が専門的な科学 AI システムをローンチ。2,000+ 研究ツール、50+ CAS 研究所。
- [Google が Anthropic に $40B 投資](https://aibusiness.com/generative-ai/google-could-invest-another-40-billion-anthropic) - 🆕 **2026-04**。初期 $10B + 業績に応じて最大 $30B。5 年間で 5GW の計算キャパシティを含む。
- [OpenAI Deployment Company (DeployCo)](https://openai.com/index/openai-launches-the-deployment-company/) - 🆕 **2026-05-11**。OpenAI が $4B+ をぶん上げた企業 AI 導入サービス会社をスピンオフ（TPG / Bain Capital / Brookfield / Advent / Goldman Sachs / SoftBank + Bain & Company / Capgemini / McKinsey）し、Tomoro コンサルタントも取り込む。AI ベンダー競争がサービス + Forward Deployed Engineers へ軽車していることを示唆。
- [Anthropic ↔ SpaceX Colossus 1](https://www.siliconrepublic.com/business/anthropic-joins-forces-with-spacex-for-colossus-capacity) - 🆕 **2026-05-06**。Anthropic が 300+ MW / 22 万 GPU 規模の Colossus 1（Memphis）の全キャパシティを押さえる。SpaceX は xAI 買収後に AI インフラ提供者として再位置づけ、Anthropic は Claude Code の有償プランレートを 2 倍化。
- [DeepSeek 国家ファンド主導 $4B ラウンド](https://www.techtimes.com/articles/316717/20260516/chinas-state-ai-fund-backs-deepseek-4-billion-round-efficiency-challenge-nvidia-dependent.htm) - 🆕 **2026-05-16**。中国の国家人工知能産業投資ファンド + 大ファンド III + Tencent と DeepSeek の初めての外部資金調達 ~$4B／企業価値 ~$50B がもうすぐクローズ。大ファンド III にとって初の LLM 投資。
- [教皇レオ 14 世 → バチカン AI 委員会](https://www.americamagazine.org/vatican-dispatch/2026/05/16/pope-leo-establishes-new-vatican-commission-on-artificial-intelligence/) - 🆕 **2026-05-16**。教皇レオ 14 世が rescriptum を公布し、バチカンに部署を跨ぐ AI 委員会を設置（人間の統合的発展部を中心に、信仰部、文化・教育部、コミュニケーション部、ポンティフィシアル生命・科学・社会科学アカデミーが参加）。任期 1 年・更新可。初の AI を主題とする回勅が近々出る見込み。
- [Robinhood Agentic Trading + Robinhood ↔ MCP](https://robinhood.com/us/en/newsroom/robinhood-is-now-open-to-agents/) - 🆕 **2026 年 5 月 27 日**（ベータ）。米国主要証券会社で初めて株式取引 API を MCP 経由で AI エージェントに開放。Agent はすべての口座への読み取りのみ、取引実行は隔離された Agentic 口座内に限定。全取引プッシュ通知 + ワンタップ切断。エージェントが推薦ではなく実際の取引保管権を持つ、エージェント型金融の重要な一歩。
- [Microsoft Scout + MAI-Code-1-Flash + MAI-Thinking-1（Build 2026）](https://microsoft.ai/news/microsoft-build-2026-mai-keynote-transcript/) - 🆕 **2026 年 6 月 2 日（Build 2026）**。Microsoft が同時に OpenClaw ベースの常時稼働パーソナルエージェント（Scout）、自社初のコーディング基盤モデル（MAI-Code-1-Flash、GitHub Copilot 内）、自社初の推論モデル（MAI-Thinking-1）を発表。OpenAI 提携開始以来最大の基盤モデル独立化への動き。
- [Meta Business Agent（WhatsApp + Instagram）](https://techcrunch.com/2026/06/03/metas-ai-agent-for-whatsapp-business-is-now-available-globally/) - 🆕 **2026 年 6 月 3 日**。Meta がロンドンの Conversations 2026 で顧客サポート AI エージェントを WhatsApp + Instagram DM 上に世界展開。質問対応、商品レコメンド、予約、リード見極めを実行；**100 万社超**がすでに利用。WhatsApp Business Premium ティアと連動した段階制課金 —— Meta 初の直接収益化 AI 製品。
- [WWDC 2026 — Apple Intelligence × Gemini + Foundation Models フレームワーク拡張](https://www.apple.com/newsroom/2026/06/apple-unveils-next-generation-of-apple-intelligence-siri-ai-and-more/) - 🆕 **2026 年 6 月 8 日**。Apple が次世代 Apple Intelligence と再設計された新 Siri AI（マルチモーダル、画面認識、オンデバイス + サーバルーティング）を発表。新 Siri は ChatGPT 引き継ぎではなく Google Gemini が駆動。Foundation Models フレームワークが画像入力、カスタムスキル、オンデバイス + サーバモデル統一の Swift API に対応；SiriKit は廃止、拡張された App Intents に統一。EU / 中国でのローンチは延期。

---

## 📅 2026 AI タイムライン

*2026 年の AI 業界の重要マイルストーンと出来事。*

| 日付 | 出来事 | カテゴリ |
|------|--------|-------|
| **2026-01** | AMD Ryzen AI 400 シリーズを CES で発表 — 60 TOPS NPU 搭載の主流 AI PC | ハードウェア |
| **2026-02** | Claude Opus 4.6 リリース — エージェントチーム能力 | モデル |
| **2026-02** | Claude Sonnet 4.6 リリース — 1M トークンコンテキスト、エージェント型検索 | モデル |
| **2026-02** | Gemini 3.1 Pro リリース | モデル |
| **2026-02** | Qwen3.5 シリーズをローンチ — ネイティブマルチモーダル、エージェント型コーディング | モデル |
| **2026-02** | Qwen3-Coder-Next リリース — 80B MoE コーディングエージェントモデル | モデル |
| **2026-02** | Cursor が 8 並列エージェントをサポート | ツール |
| **2026-02** | GitHub Copilot がエージェントモードとモデルアクセスを拡充 | ツール |
| **2026-03** | Gemini 3.1 Flash Lite を開発者向けにリリース | モデル |
| **2026-03** | Mistral Forge ローンチ — カスタム LLM トレーニングプラットフォーム | プラットフォーム |
| **2026-03** | Microsoft Agent Framework（AutoGen + Semantic Kernel）が GA ターゲット | フレームワーク |
| **2026-03** | DeepSeek が最新 NVIDIA チップで訓練された新モデルを発表 | モデル |
| **2026-03** | MCP 2026 ロードマップを公開 — プロダクションスケーリングとガバナンスに重点 | プロトコル |
| **2026-03** | Sora サービス終了を予告（アプリは 4 月 26 日に閉鎖） | 出来事 |
| **2026-04-02** | Qwen3.6-Plus プロプラエタリフラッグシップをアリババがローンチ | モデル |
| **2026-04-03** | Microsoft AI Agent Governance Toolkit をリリース（オープンソース） | ツール |
| **2026-04-06** | Microsoft Agent Framework を正式発表（AutoGen + Semantic Kernel 統合） | フレームワーク |
| **2026-04-07** | Zhipu AI が GLM-5.1 をオープンソース化 — 744B MoE、華為昂騰で訓練 | モデル |
| **2026-04-08~09** | Meta Muse Spark をリリース — Meta Superintelligence Labs の最初のモデル | モデル |
| **2026-04** | Claude Mythos Preview — ゲート型サイバーセキュリティ研究モデル（BenchLM 99、SWE-bench 93.9%） | モデル |
| **2026-04** | Sora アプリを正式シャットダウン | 出来事 |
| **2026-04-14** | Gemini Robotics ER-1.6 をアップグレード — 空間推論を強化 | ロボティクス |
| **2026-04-15** | Qwen3.6-35B-A3B をオープンソース化（Apache 2.0） | モデル |
| **2026-04-16** | Claude Opus 4.7 リリース — SWE-bench Verified 87.6%、`/think xhigh` 推論 | モデル |
| **2026-04-18** | Qwen3.6-Max-Preview ローンチ — コーディングベンチマークでトップ中国モデル | モデル |
| **2026-04-20~21** | Moonshot AI が Kimi K2.6 をリリース — 1T MoE、1,000-エージェントスワーム | モデル |
| **2026-04-22** | Qwen3.6-27B をアリババがオープンソース化 — 27B 密マルチモーダル | モデル |
| **2026-04-23** | Tencent が Hunyuan Hy3 Preview をオープンソース化 — 295B/21B MoE、256K コンテキスト | モデル |
| **2026-04-23** | Claude Managed Agents Memory パブリックベータ — セッションを越えたエージェントメモリ | ツール |
| **2026-04-23** | OpenAI が GPT-5.5 をリリース — エージェント型コーディングと推論の大幅アップグレード | モデル |
| **2026-04-24** | DeepSeek V4 Pro および Flash をリリース — 1.6T MoE、1M コンテキスト、MIT ライセンス | モデル |
| **2026-04-24** | Cohere がドイツの Aleph Alpha と約 $20B 評価額で合併 + $600M 資金調達 | 業界 |
| **2026-04-27** | アリババ Tianma AI 画像-動画生成モデルがベータ入り | モデル |
| **2026-04-27** | LangGraph v0.3.19 リリース、LangGraph Swarm 事前ビルドエージェント | フレームワーク |
| **2026-04-28** | NVIDIA Nemotron 3 Nano Omni をリリース — 30B マルチモーダル | モデル |
| **2026-04-28~29** | CAS ScienceOne 100 / 磐石100 ローンチ — 50+ 研究所向け科学 AI | モデル |
| **2026-04-30** | OpenAI が Trusted Access for Cyber (TAC) プログラムを通じて GPT-5.5-Cyber の提供を開始 | モデル |
| **2026-04-30** | OpenAI が [「エージェント構築の実践ガイド」](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/) を公開 | リソース |
| **2026-05-01** | Anthropic が Claude Security をパブリックベータでリリース — Opus 4.7 駆動のコードベース脆弱性スキャナー | ツール |
| **2026-05** | Macquarie Bank が 7 か月で Gemini Enterprise を使って 13 万時間を節約したと報告 | 業界 |
| **2026-05** | Google が対応車両に Gemini をロールアウトし、Google Assistant を置き換える（英語ファースト、米国から） | 業界 |
| **2026-05-04** | Google が [Project Mariner](https://deepmind.google/models/project-mariner/) を終了、ブラウザエージェント技術は Gemini Agent に統合 | ツール |
| **2026-05-04** | Anthropic + Goldman Sachs + Blackstone が **15 億ドルの Claude 導入合弁事業** を発表 — ミッドサイズの Wall Street 企業に Anthropic エンジニアを派遣 | 業界 |
| **2026-05-05** | OpenAI が **GPT-5.5 Instant** を新しい ChatGPT デフォルトモデルとして展開 — 効率重視のアップグレード、ハルシネーション率を約 50% 削減 | モデル |
| **2026-05-05** | Anthropic が **Claude Finance Agents** を発表 — ピッチブック作成、KYC、月次決算など 10 個の金融サービス専用エージェント。Claude Cowork プラグイン / Claude Code スキル / Managed Agents クックブックとして利用可能 | ツール |
| **2026-05-05** | OpenAI ↔ PwC が金融サービスエージェント（予測、支払い）で提携 | 業界 |
| **2026-05-07** | Google が **Flow（Veo ベース AI 映像制作） に Agent Mode を準備** — 動画制作パイプラインの自動化 | ツール |
| **2026-05-08** | OpenAI が **GPT-Realtime-2 / Realtime-Translate / Realtime-Whisper** をリリース — 音声エージェント、リアルタイム翻訳、リアルタイム文字起こし | モデル |
| **2026-05-09** | OpenAI が ChatGPT Enterprise で **Workspace Agents** を展開 — 接続されたアプリ間で繰り返し可能なワークフローを自動化 | ツール |
| **2026-05-11** | [OpenAI Deployment Company](https://openai.com/index/openai-launches-the-deployment-company/) が発足 — $4B+ の企業サービス部門、TPG / Bain Capital / Brookfield + Bain & Company / Capgemini / McKinsey が出資、Tomoro コンサルタントを取り込む | 業界 |
| **2026-05-11～13** | [SAP Sapphire 2026 Orlando](https://news.sap.com/2026/05/sap-sapphire-sap-unveils-autonomous-enterprise/) — SAP Business AI Platform、**Joule Studio 2.0**、Autonomous Suite（50+ 領域の Joule Assistant + 200+ のエージェント）を発表。Joule Studio 2.0 は 2026-06 以降 GA | 業界 |
| **2026-05-12** | [Claude for Legal](https://www.anthropic.com/news/claude-for-legal) — Claude Cowork 上に 20+ の MCP コネクタ（iManage / NetDocuments / DocuSign / LexisNexis / Westlaw / Harvey / Everlaw / Relativity など）と 12 の実務領域プラグイン | ツール |
| **2026-05-12～15** | [Visual Studio 2026 Insiders](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/) — Copilot Chat「Agent Mode」に Agent Skills 作成サポートが追加 | ツール |
| **2026-05-13** | [Claude for Small Business](https://www.anthropic.com/news/claude-for-small-business) — 15 個の事前構築エージェントワークフロー + QuickBooks / PayPal / HubSpot / Canva / DocuSign / Google Workspace / Microsoft 365 コネクタ、米国 10 都市ツアー | ツール |
| **2026-05-13** | [Cursor 3.4 クラウドエージェント環境](https://cursor.com/changelog) — マルチリポ、build secrets 付き Dockerfile 設定、キャッシュレイヤー 70% 高速化、環境ごとのバージョン履歴、監査ログ、egress / secrets の限定 | ツール |
| **2026-05-13～16** | [Figure Helix 02 ライブストリーム](https://www.businessinsider.com/figure-ai-turned-a-humanoid-sorting-packages-must-see-tv-2026-5) — F.03 + Helix 02 がパッケージ仕分けラインでストレステスト、初日 8h ~22K、24h ~30K、~72h ~88K 個で機械故障 | ロボティクス |
| **2026-05-14** | [Anthropic ↔ Gates Foundation $200M パートナーシップ](https://www.anthropic.com/news/gates-foundation-partnership) — 4 年間で助成金 + Claude クレジット + エンジニアリングをグローバルヘルス / ライフサイエンス / 教育 / 農業に投入 | 業界 |
| **2026-05-14** | [Anthropic ↔ PwC 提携拡大](https://www.pwc.com/us/en/about-us/newsroom/press-releases/anthropic-pwc-expand-alliance-agentic-enterprise.html) — Claude Code + Cowork のグローバル展開、30,000 名の PwC 専門家を認定、共同 Agentic Enterprise Center of Excellence | 業界 |
| **2026-05-14** | [Genkit Middleware](https://developers.googleblog.com/announcing-genkit-middleware-intercept-extend-and-harden-your-agentic-apps/) — Google の OSS Genkit フレームワークにミドルウェアを追加（TS / Go / Dart）| フレームワーク |
| **2026-05-14** | [Zyphra ZAYA1-8B-Diffusion-Preview](https://www.zyphra.com/post/zaya1-8b-diffusion-preview) — 自己回帰 LLM から変換された初の MoE 拡散言語モデル／AMD GPU で訓練された初の拡散 LM／最大 7.7× 推論高速化 | モデル |
| **2026-05-16** | [教皇レオ 14 世がバチカン AI 委員会を設置](https://www.americamagazine.org/vatican-dispatch/2026/05/16/pope-leo-establishes-new-vatican-commission-on-artificial-intelligence/) — 部署を跨ぐ AI 委員会。初の AI 主題とする回勅が高い見込み | 業界 |
| **2026-05-16** | [OpenAI ↔ Malta パートナーシップ](https://openai.com/index/malta-chatgpt-plus-partnership/) — 14 歳以上のすべてのマルタ居住者に 2 時間 AI リテラシー講座修了で 1 年間の ChatGPT Plus（"OpenAI for Countries"）| 業界 |
| **2026-05-16** | [DeepSeek 国家ファンド主導 $4B ラウンド](https://www.techtimes.com/articles/316717/20260516/chinas-state-ai-fund-backs-deepseek-4-billion-round-efficiency-challenge-nvidia-dependent.htm) — 国家 AI 産業ファンド + 大ファンド III + Tencent 主導、~$50B 評価額の初めての外部ラウンド | 業界 |
| **2026-05-13** | [Runway Agent](https://chatlyai.app/news/runway-agent-launch-may-2026) リリース — 台本を渡すと Gen-4 / Aleph でマルチショットの完成動画をエンドツーエンドで仕上げる | ツール |
| **2026-05-18** | [OpenAI ↔ Dell Codex 提携](https://openai.com/news/company-announcements/) — ハイブリッド / オンプレミス企業環境へ Codex を拡張 | 業界 |
| **2026-05-18** | [アリババ Qwen 3.7-Max-Preview / Plus-Preview](https://www.scmp.com/tech/tech-trends/article/3354087/alibaba-teases-new-qwen-previews-highest-ranking-chinese-ai-models-arena) — LM Arena で中国モデル最高スコア（テキスト + ビジョン）| モデル |
| **2026-05-18** | [Boston Dynamics Atlas 100ポンド超の荷重操作](https://www.techtimes.com/articles/316854/20260519/boston-dynamics-reveals-how-atlas-learned-lift-100-pound-loads-hyundai-plans-30000-per-year.htm) + Hyundai が 2028 年以降 Hyundai/Kia 工場に **25K+ 台の Atlas** を配備予定 | ロボティクス |
| **2026-05-18** | [Figure F.03 対 人間 8 時間仕分けチャレンジ](https://incrypted.com/en/figure-ai-held-a-human-vs-robot-marathon/) — 人間社員が 12,924 個、F.03 が 12,732 個でわずかに人間勝（2.79 vs 2.83 秒 / 個）| ロボティクス |
| **2026-05-18** | [Anthropic が FSB に Claude Mythos ブリーフィング](https://www.theguardian.com/technology/2026/may/18/anthropic-ai-claude-mythos-cyber-financial-stability-board-fsb) — フロンティア lab 初の G20 金融安定規制当局への説明 | 業界 |
| **2026-05-18** | [ChatGPT 安全システムアップデート](https://www.edtechinnovationhub.com/news/openai-updates-chatgpt-safety-systems-to-track-risk-across-sensitive-conversations) — 長いセッションを跨いでリスクシグナル（自殺 / 自傷 / 他者への危害）を追跡 | 業界 |
| **2026-05-19** | **Google I/O 2026** — [Gemini 3.5 Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) を Gemini App + Google 検索 AI Mode のデフォルトモデルとして公開（公式によると同類のフロンティアモデルより約 4 倍高速）。Gemini 3.5 Pro は 6 月入り | モデル |
| **2026-05-19** | **Google I/O 2026** — [Gemini Omni / Omni Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/)、Google DeepMind の AGI を見揮えたワールドモデルファミリー | モデル |
| **2026-05-19** | **Google I/O 2026** — [Gemini Spark](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) 24/7 パーソナル AI エージェント + ~30+ の MCP サードパーティーツール連携、新たな **Google AI Ultra ($100/月)** サブスクリプション限定 | ツール |
| **2026-05-19** | [OpenAI Guaranteed Capacity （Compute Annual Pass）](https://openai.com/news/company-announcements/) リリース — 1 / 2 / 3 年期の企業コンピュート予約 | 業界 |
| **2026-05-19** | [OpenAI ↔ Google SynthID + C2PA コンテンツ出所検証](https://openai.com/index/advancing-content-provenance/) — フロンティア lab 同士初のクロスプラットフォーム AI 画像ウォーターマーク相互運用と公開検証ツールプレビュー | 業界 |
| **2026-06-27** | GPT-4.5 が ChatGPT から正式に退役予定（API は継続）—— OpenAI は GPT-5.5 ファミリーへ完全移行 | モデル |
| **2026-06** | [OutSystems Agentic Systems Platform](https://www.outsystems.com/) ローンチ — ローコードプラットフォームが「AI ネイティブ」なマルチエージェントオーケストレーション基盤へとピボット | 業界 |
| **2026-05-19** | [Anthropic：Widening the conversation on frontier AI](https://www.anthropic.com/news/widening-conversation-ai) — 「智恵の伝統」を取り込んだフロンティア AI 安全対話の枠組み | 業界 |
| **2026-05-19** | [DeepSeek が Jane Street 出身のエンジニアを迎え AI harness チームを新設](https://www.scmp.com/tech/big-tech/article/3354113/deepseek-recruits-former-jane-street-engineer-catch-ai-agents-revenue-race) — モデル R&D からエージェント製品化への軸足 | 業界 |
| **2026-05-20** | **アリババクラウド杭州サミット** — [Qwen 3.7-Max](https://www.scmp.com/tech/big-tech/article/3354212/alibaba-unveils-new-qwen-model-custom-chips-bid-become-chinas-ai-factory) GA、エージェント型コーディングと長期タスク向け；同期で T-Head **Zhenwu M890** AI チップとフルスタック AI 基盤アップグレード | モデル |
| **2026-05-20** | [BMS ↔ Anthropic Claude Enterprise](https://news.bms.com/news/corporate-financial/2026/Bristol-Myers-Squibb-Announces-Strategic-Agreement-with-Anthropic-to-Position-Claude-Enterprise-as-the-Shared-Intelligence-Platform-Across-Its-Global-Operations/default.aspx) — 30K+ 名の社員が Claude Enterprise を共通インテリジェンス基盤として採用、世界トップ 5 製薬企業で初めての社全体規模 | 業界 |
| **2026-05-20** | [LlamaIndex ↔ Google Agents API](https://www.kucoin.com/news/flash/google-launches-agents-api-llama-index-integrates-llamaparse-for-unstructured-document-processing) — Google Agents API サンドボックス内に LlamaParse / LiteParse を法出し、Sandboxed-Lit + ParseBench も同リリース | フレームワーク |
| **2026-05-20** | [Microsoft RAMPART + Clarity](https://www.microsoft.com/en-us/security/blog/2026/05/20/introducing-rampart-and-clarity-open-source-tools-to-bring-safety-into-agent-development-workflow/) オープンソース化 — agentic AI 向け pytest ネイティブのホワイトボックステストフレームワークと、設計レビューコンパニオン。CI/CD にそのまま組み込める PyRIT の開発者向け後継 | ツール |
| **2026-05-06** | [AWS MCP Server GA](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/) — AWS マネージドの MCP エンドポイント。任意の AWS API をサンドボックス Python と agent skills で扱う。初のハイパースケーラー純正 MCP サーバ | プロトコル |
| **2026-05-01** | [Google Workspace MCP Server](https://workspaceupdates.googleblog.com/2026/05/agent-tools-and-security-updates-for-workspace-developers.html) 順次展開 — Workspace ネイティブの MCP サーバ。Gmail / Drive / Calendar / Docs / Sheets を MCP クライアントに公開、OAuth スコープは管理者が制御 | プロトコル |
| **2026-05-14** | [Grok Build (初期 beta)](https://x.ai/news/grok-build-cli) — xAI が公開した **grok-code-fast-1** ベースの agentic CLI コーディングエージェント。サブエージェントを隔離環境で並列実行、SuperGrok Heavy 契約者限定 | ツール |
| **2026-05-14** | [iManage MCP Server](https://imanage.com/resources/resource-center/news/mcp-server-available-broader-ai-ecosystem/) 公開 — 法務 / プロフェッショナルサービス系 SaaS として初めて公式 MCP エンドポイントを公開 | ツール |
| **2026-05-19** | [Google Antigravity 2.0](https://antigravity.google/blog/introducing-google-antigravity-2-0) を I/O 2026 で発表 — スタンドアロンデスクトップアプリで多エージェントオーケストレーション、cron スケジュール / 長時間非同期 / 動的サブエージェント、Antigravity CLI + SDK、エンタープライズ版は Gemini Enterprise Agent Platform に組み込み | ツール |
| **2026-05-22** | [Kore.ai Artemis Agent Platform](https://venturebeat.com/technology/kore-ai-launches-artemis-ai-agent-platform-expands-challenge-to-microsoft-and-salesforce) を Azure で公開 — AI ネイティブのエンタープライズエージェント基盤。核は宣言型の **Agent Blueprint Language (ABL)** | 業界 |
| **2026-05-22** | [FPT Flezi Foundry™](https://lasvegassun.com/news/2026/may/22/fpt-launches-flezi-foundry-advancing-ai-augmented-/) ローンチ — “Service-as-a-Software” ガバナンス下の AI 強化デリバリー基盤。ADLC と AMS の 2 モードを提供 | 業界 |
| **2026-05-22** | [JetBrains Rider AI テスト生成 skill](https://blog.jetbrains.com/dotnet/2026/05/22/claude-codex-ai-agent-skill-for-writing-tests/) — .NET カバレッジ情報を Claude Code / Codex に渡し、未カバー分岐に絞り込んだテスト生成を可能に | ツール |
| **2026-05-28** | [Claude Opus 4.8](https://www.anthropic.com/claude/opus) Anthropic がリリース — コードベース規模のマイグレーション、動的ワークフロープレビュー（数百のサブエージェント並列）、エフォートコントロールパネル、Fast モード 3 倍安、**Mythos クラス** を予告 | モデル |
| **2026-05-28** | [Koog 1.0](https://blog.jetbrains.com/ai/2026/05/koog-1-0-is-out-stable-core-better-interop-and-multiplatform-observability/) KotlinConf 2026 でリリース — JetBrains の OSS Kotlin/Java エージェントフレームワークが安定 1.0、Kotlin Multiplatform デプロイ、全ターゲット OpenTelemetry | フレームワーク |
| **2026-05-28** | [Gemini Omni Flash 会話型ビデオ編集](https://www.techtimes.com/articles/317309/20260528/google-gemini-omni-flash-brings-voice-controlled-ai-video-editing-future-conversational-ai.htm) が Gemini App / Google Flow / YouTube Shorts へロールアウト — 音声・テキスト騆動のシネマ風編集が従来の NLE を置換 | ツール |
| **2026-05-29** | [MCP 2026-07 Release Candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) 公開 — ステートレスコア、拡張フレームワーク、MCP Apps サーバレンダリング UI、OAuth/OIDC 強化。正式版は 7 月 28 日予定 | プロトコル |
| **2026-04-17～20** | [Apple CEO 交代を発表](https://www.sec.gov/Archives/edgar/data/0000320193/000114036126015711/ef20071035_8k.htm) — Tim Cook は 15 年を経て **2026-09-01** に Executive Chair へ移行、ハードウェアエンジニアリング担当 SVP の **John Ternus** が CEO に就任。AI 時代における最初の時価総額トップクラスのフロンティアプラットフォーム企業 CEO 交代 | 業界 |
| **2026-06-08** | **[WWDC 2026](https://www.techradar.com/news/live/apple-wwdc-2026-live)** — Apple が Google Gemini 駆動の Apple Intelligence と、よりパーソナル化された新 Siri を発表（Siri からサードパーティ ChatGPT へ転送する動作は廃止）。iOS 27、iPadOS 27、macOS 27 "Golden Gate"、watchOS 27、tvOS 27、visionOS 27 でオンデバイス AI を強化。アプリ起動 約 30% 高速化、写真プレビュー 70% 高速化、iPadOS のファイル転送 5 倍高速化、2026 年秋にリリース | 業界 |
| **2026-04** | Gartner は 2026 年末までに企業アプリの 40% が AI エージェントを組み込むと予測 | 業界 |
| **2026-04** | Google が Anthropic へ最大 $40B の投資をコミット（初期 $10B） | 業界 |
| **2026 進行中** | A2A Protocol のパートナー組織が 150+ に増加 | プロトコル |
| **2026 進行中** | 開発者の 85% が AI コーディングツールを常用 | 業界 |
| **2026 進行中** | エンタープライズエージェント AI の導入が加速 — "Agents as a Service" が台頭 | 業界 |
| **2026-01-06** | [Lenovo + Motorola Qira](https://news.lenovo.com/pressroom/press-releases/lenovo-unveils-lenovo-and-motorola-qira/) を CES 2026 で発表 — クロスデバイスの「パーソナル・アンビエント・インテリジェンス」、Q1 から Lenovo、その後 Motorola スマホへ拡大 | 業界 |
| **2026-02-10** | [Snowflake Agent World Model](https://github.com/Snowflake-Labs/agent-world-model) オープンソース化 — 1,000 個の SQL ベース MCP 合成環境 + RL 訓練済みエージェントを公開。大規模 agentic RL 向け、後に ICML 2026 採択 | 研究 |
| **2026-02-26** | [1X NEO コンシューマーヒューマノイド予約開始](https://www.1x.tech/discover/neo-home-robot) — $20K の早期アクセス価格、2026 年に米国家庭へ配送 | ロボティクス |
| **2026-03-10** | [Hume TADA](https://github.com/HumeAI/tada) オープンソース化 — Text-Acoustic Dual Alignment TTS、MIT、テストで転記エラーゼロ、スマホで動作 | モデル |
| **2026-04-28** | [Anthropic クリエイティブツールコネクター](https://www.anthropic.com/news/claude-for-creative-work) — Adobe / Blender / Autodesk Fusion / Ableton / Splice / Canva Affinity / SketchUp / Resolume 向けの MCP コネクター 9 種 | ツール |
| **2026-05-13** | [Microsoft Copilot Studio CUA GA](https://techcommunity.microsoft.com/blog/copilot-studio-blog/computer-using-agents-in-microsoft-copilot-studio-are-now-generally-available/4519427) — Microsoft 365 / Power Platform 内で UI 駆動の Web / デスクトップエージェントを構築可能に | ツール |
| **2026-05-26** | [Coinbase Base MCP](https://fortune.com/2026/05/26/coinbase-pushes-further-into-ai-payments-with-new-mcp-for-base-network/) 公開 — オンチェーン取引・レンディング向け初の取引所級 MCP エンドポイント | プロトコル |
| **2026-05-27** | [Robinhood Agentic Trading](https://robinhood.com/us/en/newsroom/robinhood-is-now-open-to-agents/) ベータ — 米国主要証券会社初の MCP 経由 AI エージェント株取引開放 | 業界 |
| **2026-05-29** | [OpenAI Codex Computer Use on Windows](https://windowsforum.com/threads/openai-codex-computer-use-brings-agent-control-to-windows-desktop.421107/) — サンドボックス化された Codex の Windows デスクトップ制御が GA | ツール |
| **2026-06-02** | [Microsoft Build 2026](https://microsoft.ai/news/microsoft-build-2026-mai-keynote-transcript/) — MAI-Thinking-1（自社初の推論モデル）、MAI-Code-1-Flash（5B コーディングモデル、GitHub Copilot 入り）、[Microsoft Scout](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/)（OpenClaw ベースの常時稼働パーソナルエージェント）を同日発表 | モデル / ツール |
| **2026-06-03** | [Meta Business Agent](https://techcrunch.com/2026/06/03/metas-ai-agent-for-whatsapp-business-is-now-available-globally/) が WhatsApp + Instagram で世界展開 — Meta 初の直接収益化 AI 製品、WhatsApp Business Premium ティアと連動 | 業界 |
| **2026-06-03** | [Perplexity Personal Computer for Windows](https://www.perplexity.ai/hub/products/computer-for-windows) 発表 — 19+ AI モデルを自動オーケストレーション、ローカルファイル / ネイティブアプリ / Web を横断 | ツール |
| **2026-06-06** | [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code) を Moonshot AI がリリース — TypeScript / MIT のターミナルエージェント、隔離コンテキストで動く coder / explore / plan サブエージェント内蔵 | ツール |
| **2026-06-08** | **WWDC 2026 Apple Intelligence + Siri AI 再設計** — Foundation Models フレームワークに画像入力、カスタムスキル、オンデバイス + サーバ統一 Swift API が追加；SiriKit 廃止、拡張 App Intents に統一；新 Siri は Google Gemini ベース（ChatGPT ではない）| モデル / ツール |

---

## 貢献

[CONTRIBUTING.md](CONTRIBUTING.md) をご読みください。**スパム防止の品質ゲート**は中、英、日の 3 言語版すべてに適用されます: 自己宣伝タイプの並列提出 PR は一律拒否されます。

## License

MIT © [Zijian Ni](https://github.com/Zijian-Ni)

---

*Made with ❤️ by [Zijian Ni](https://github.com/Zijian-Ni) · 2026。日本語版は英語版と同期します。不一致がある場合は英語版を正とします。*

