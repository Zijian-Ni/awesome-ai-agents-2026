<div align="center">

# 🤖 Awesome AI Agents 2026 · 日本語版

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fawesome-ai-agents-2026&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)](https://github.com/Zijian-Ni/awesome-ai-agents-2026/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-July%2017%2C%202026-blue.svg)](#)
[![Resources](https://img.shields.io/badge/Resources-580%2B-orange.svg)](#)
[![Audited](https://img.shields.io/badge/Spam_Audited-2026--07--17-success.svg)](#️-ステータス凡例)
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
> - 🆕 [最新追加（2026年7月）](#-2026-ai-タイムライン) • 🛡️ [セキュリティ](#️-エージェントセキュリティ) • 💰 [コスト比較](#-基盤モデル--api-コスト--コンテキスト)

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
- [GPT-Live-1 / GPT-Live-1 mini](https://openai.com/index/introducing-gpt-live/) - 🆕 **2026-07-08**。Advanced Voice Mode を置き換える OpenAI のフルデュプレックス会話音声モデル。聞きながら同時に話し（ターンテイキング遅延ゼロ）、割り込みに対応し、複雑なクエリはバックグラウンドで GPT-5.5 に委譲。**GPT-Live-1** は有料ユーザー（Go/Plus/Pro）、**GPT-Live-1 mini** は無料ユーザーのデフォルト。リアルタイムのライブ翻訳を含む。iOS / Android / Web で利用可。
- [GPT-5.6 Sol](https://openai.com/blog/gpt-5-6) - 🆕 **2026-07-09**（GA；一部プレビュー 6月26日～）。GPT-5.6 ファミリーのフロンティアフラッグシップ — 高度な推論、コーディング、生物学、サイバーセキュリティ機能に加え、「最大（max）」推論と「ウルトラ（ultra）」サブエージェントモードを備える最高性能モデル。ChatGPT、Codex、OpenAI API で利用可能。米国政府による安全審査のため発表が遅れたが、段階的に展開中。
- [GPT-5.6 Terra](https://openai.com/blog/gpt-5-6) - 🆕 **2026-07-09**。GPT-5.6 ファミリーの中間層 — GPT-5.5 と同等の性能を約 2 分の 1 のコストで提供。コスト効率の高い本番ワークロード向け。
- [GPT-5.6 Luna](https://openai.com/blog/gpt-5-6) - 🆕 **2026-07-09**。GPT-5.6 の中で最も高速かつコスト効率の高いモデル — 大量で処理速度が求められるタスクに最適。
- [ChatGPT Work](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) - 🆕 **2026-07-09**。目標を渡すと完成した成果物に仕上げる OpenAI のエージェント — 接続されたアプリやファイルを横断して行動し、1 つのプロジェクトに数時間取り組み続け、スライド / シート / ドキュメント / Web アプリを作成し、スケジュール実行や内蔵ブラウザによるデスクトップ Computer Use も可能。GPT-5.6 駆動。Web / モバイルでは Pro・Enterprise・Edu から順次展開（Plus / Business は追って対応）；デスクトップアプリは Mac / Windows で Free を含む全プランにグローバル提供。
- [Sites for ChatGPT](https://openai.com/academy/chatgpt-sites/) - 🆕 **2026-06**。ChatGPT 内での計画や分析結果を、インタラクティブで共有可能な Web サイトや軽量アプリに変換する Codex 駆動の機能。2026 年 7 月 9 日の GPT-5.6 / ChatGPT Work ローンチ時点でパブリックベータ。
- [Codex ビジネスプラグイン](https://venturebeat.com/orchestration/openais-codex-update-lets-agents-build-interactive-enterprise-workspaces-via-sites-and-role-specific-plugins) - 🆕 **2026-06**。セールス、データ分析、クリエイティブ制作などの業務特化プラグインを Codex に直接導入するエンタープライズ機能強化。
- [GPT-Rosalind](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/) - 🆕 **2026年6月3日**。OpenAI のライフサイエンス向けフロンティアモデルの大型アップデート —— 創薬・ゲノミクス・定量生物学・ウェットラボのトラブルシュートを強化（長期的なゲノム解析で GPT-5.5 比約 31% 少ないトークン）。研究プレビューを世界中の対象組織に初公開し、Novo Nordisk が既存パートナーの Amgen・Moderna・Allen Institute・Thermo Fisher に加わる。

- [GPT-5.5](https://openai.com/index/gpt-5-5-system-card/) - 🆕 **2026-04-23 公開**（コードネーム "Spud"）。エージェントタスク向けの新フロンティア: コーディング、オンライン調査、データ分析、自律的なツール操作。推論の安定性と長時間タスク処理能力が大幅向上。ChatGPT Plus / Pro / Business / Enterprise で利用可能。
- [GPT-5.5 Pro](https://openai.com/index/gpt-5-5-system-card/) - 🆕 2026-04-23。並列テストタイム計算による高精度バリアント。Pro / Business / Enterprise。
- [GPT-5.5 Instant](https://openai.com/index/gpt-5-5-instant/) - 🆕 **2026-05-05**。ChatGPT の新しいデフォルトモデル。効率重視のアップグレードで、ハイステイクスなプロンプトの幻覚率が約 50% 低下。無料枠でも利用可能。
- [GPT-5.5-Cyber](https://openai.com/index/trusted-access-for-cyber/) - 🆕 **2026-04-30**。GPT-5.5 のサイバーセキュリティ特化版。OpenAI の Trusted Access for Cyber (TAC) プログラム経由で、検証済みの防御者・政府・重要インフラ・セキュリティベンダーにのみ提供。一般公開なし。
- [OpenAI Daybreak](https://thehackernews.com/2026/05/openai-launches-daybreak-for-ai-powered.html) - 🆕 **2026-05-12**。GPT-5.5 + GPT-5.5-Cyber + Trusted-Access-for-Cyber を束ねたサイバー防御プラットフォーム。AI による脆弱性検出とパッチ検証を提供し、プレビューは EU 政府機関とセキュリティベンダーにも開放。
- [GPT-Realtime-2](https://openai.com/) - 🆕 **2026-05-08**。GPT-5 級の推論を Realtime API に導入。128K コンテキスト、音声フィードバック付き並列ツール呼び出し、推論強度の調整に対応。
- [GPT-Realtime-Translate](https://openai.com/) - 🆕 **2026-05-08**。70 以上の入力言語と 13 の出力言語にわたるリアルタイム音声間翻訳。
- [GPT-Realtime-Whisper](https://openai.com/) - 🆕 **2026-05-08**。GPT-Realtime-2 を補完するストリーミング低遅延の音声認識モデル。
- [GPT-5.4](https://openai.com/) - 2026-03 公開。1M トークンコンテキスト、高度なコーディング、Computer Use、ツール検索。BenchLM 94、SWE-bench Verified 77.2%、OSWorld 75%（人間ベースライン超え）。
- [GPT-5.4 Pro](https://openai.com/) - GPT-5.4 の高精度バリアント。BenchLM 92。
- [GPT-5.3](https://openai.com/) - 2026 年初頭。GPT-5.3 Instant（会話）と GPT-5.3-Codex（コーディング）を含む。
- [GPT-5.2](https://openai.com/) - 2025-12 公開。最先端の推論・長文脈・視覚。
- [GPT-5](https://openai.com/index/introducing-gpt-5/) - 2025-08 公開。ChatGPT のデフォルトモデル、GPT-4o の後継。マルチモーダル、gpt-5 / mini / nano の 3 段階。
- [GPT-4o](https://openai.com/index/hello-gpt-4o/) - テキスト・視覚・音声をネイティブにサポートする Omni モデル。2026-02 に ChatGPT から退役、API では引き続き利用可能。
- [GPT-4.5](https://openai.com/) - 📦 **2026年6月末に ChatGPT から退役済み**（API 利用は継続；会話は GPT-5.5 に自動移行）。2025年2月に研究プレビューとしてリリースされた、ChatGPT 最後の GPT-4 系モデル。o3 は 2026年8月26日に ChatGPT から退役予定。
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

- [Claude Fable 5 グローバルアクセス復旧](https://www.anthropic.com/news/redeploying-fable-5) - 🆕 **2026-07-01**。米国商務省による輸出管理が 6 月 30 日に解除されたことを受け、Anthropic は Claude.ai、Claude API、Claude Code、Claude Cowork で Fable 5 へのグローバルアクセスを復旧。Amazon が発見したジェイルブレイク手法をブロックする新しい安全クラシファイアを配備（報告された挙動を >99% のケースでブロック）。Pro/Max/Team と一部 Enterprise プランでは 7 月 7 日まで週次利用量の最大 50% まで Fable 5 が追加費用なしで利用でき、以降は利用クレジット経由；AWS、Google Cloud、Microsoft Foundry でのクラウド再有効化も追って実施。Mythos 5 は引き続き米国の審査済みエンティティに制限される。
- [Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5) - 🆕 **2026年6月30日**。これまでで最もエージェント性能の高い Sonnet — プランニング、ブラウザ/ターミナルツール利用、以前は Opus クラスのモデルが必要だった水準の自律動作に対応。高エフォート設定ではエージェント検索（BrowseComp）とコンピュータ操作（OSWorld-Verified）で Opus 4.8 に迫る性能を発揮し、Sonnet 4.6 よりもコストパフォーマンスの幅が大きく広がった。Claude.ai の Free/Pro プランの新デフォルトモデルとなり、Max/Team/Enterprise、Claude Code、API（`claude-sonnet-5`）でも利用可能。2026年8月31日までの導入価格は入力/出力それぞれ 100 万トークンあたり $2/$10（以降 $3/$15）。Anthropic は Sonnet 4.6 より望ましくない挙動の発生率が低いと報告。
- [Claude Fable 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) - 🆕 **2026-06-09**。Anthropic 初の一般提供 **Mythos クラス**モデル — Opus の上位に位置する能力ティア。ソフトウェアエンジニアリング、ナレッジワーク、ビジョン、科学研究の各ベンチマークで Opus 4.8 を上回る。セーフガード内蔵（サイバー/バイオ系の機微なクエリは Opus 4.8 へ再ルーティングされる場合あり）。入力 $10 / 出力 $50（100 万 token あたり）。Anthropic API、Amazon Bedrock、Google Cloud Vertex AI で利用可。**⚠️ 2026年6月12日にアクセス停止** —— 米国政府の輸出管理指令により、Anthropic は全顧客向けに Fable 5 と Mythos 5 を無効化。**✅ 2026年6月30日に輸出管理が解除され、7月1日にアクセス復旧** —— 新しいサイバーセキュリティクラシファイアを追加（上のエントリ参照、[声明](https://www.anthropic.com/news/redeploying-fable-5)）。
- [Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) - 🆕 **2026-06-09**。Fable 5 と同一基盤の Mythos クラスモデルを制限を緩めて提供。米国政府と連携した **Project Glasswing** を通じ、審査済みパートナー（サイバーセキュリティ企業、インフラ事業者）限定で展開。4 月の Claude Mythos Preview の正式後継。**⚠️ 2026年6月12日にアクセス停止**。Fable 5 とともに同一の輸出管理指令の対象（[声明](https://www.anthropic.com/news/fable-mythos-access)）。
- [Claude Opus 4.8](https://www.anthropic.com/claude/opus) - 🆕 **2026-05-28**。Opus シリーズの大規模アップデート：コードベース規模のマイグレーション、エージェント判断の鮮明化、「ダイナミックワークフロー」リサーチプレビューで 1 セッション中に数百のサブエージェントを並列実行可能、手動「エフォートコントロール」パネル、**Fast モード 3 倍安い**（入力 $5 / 出力 $25 / 100 万 token は同価）。Anthropic ネイティブ、Amazon Bedrock、AWS Claude Platform、Google Cloud、Microsoft Foundry で利用可。限定企業向けに **Mythos クラス** モデルを予告。
- [Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7) - 🆕 **2026-04-16 リリース**。高度なソフトウェアエンジニアリング（SWE-bench Verified 87.6%）、ビジョン強化、能動的なコード検証。`/think xhigh` の推論強度に対応。1M トークンコンテキスト。
- [Claude Opus 4.6](https://www.anthropic.com/) - 2026-02 公開。1M トークン、14.5 時間のタスク完了。Arena 会話リーダーボード首位。
- [Claude Sonnet 4.6](https://www.anthropic.com/news/claude-sonnet-4-6) - 2026-02 公開。フロンティア級コーディングとエージェント性能、1M トークンコンテキスト。
- [Claude Mythos Preview](https://www.anthropic.com/) - 🆕 2026-04 招待制研究プレビュー。BenchLM 99（リーダーボード首位）、SWE-bench Verified 93.9%。Project Glasswing パートナー限定。
- [Claude Opus 4](https://www.anthropic.com/news/claude-4) - 2025-05 公開。
- [Claude Sonnet 4](https://www.anthropic.com/news/claude-4) - 2025-05 公開。バランス重視。
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - ターミナルで動作する Anthropic のエージェント型コーディングツール。Opus 4.7 + `/think xhigh` 対応。
- [Claude Security](https://www.anthropic.com/) - 🆕 **2026-05-01** パブリックベータ。Opus 4.7 駆動の企業向けコードベース脆弱性スキャナ —— 信頼度評価・深刻度・再現手順・推奨修正付きパッチを生成。Enterprise ユーザー向け [claude.ai/security](https://claude.ai/security)。
- [Claude Finance Agents](https://www.anthropic.com/news/finance-agents) - 🆕 **2026-05-05**。Opus 4.7 ベースの金融特化エージェントを 10 種同時公開（pitchbook 作成、KYC、月次決算、ディール選定など）。Claude Cowork プラグイン、Claude Code skill、Managed-Agents の cookbook として配備可能。
- [Claude Finance JV](https://www.anthropic.com/) - 🆕 **2026-05-04**。Goldman Sachs・Blackstone との 15 億ドル規模の Claude 導入ジョイントベンチャー。Anthropic のエンジニアを中堅ウォール街企業に常駐させる。
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
- [Gemini 3.5 Pro](https://cloud.google.com/blog/products/ai-machine-learning/innovations-from-google-io-26-on-google-cloud) - ⚠️ **延期 — 2026年7月17日時点で未リリース**（パートナー限定のエンタープライズプレビューは継続中）。**200 万トークンのコンテキストウィンドウ**（報道値）と **Deep Think** 推論モードを備えるとされる Google の次期フラッグシップ。コーディングとエージェント型ワークフロー機能が大幅に向上。2026 年 5 月の Google I/O で 6 月リリースと発表されたが、コーディング性能の不振によりベースモデルを作り直したため延期。サードパーティ報道は 7 月 17 日を目標としていたが、7 月 16 日時点で Google は 3.5 Pro（およびアップグレード版 Flash）をまだテスト中とし、リリース日は未確定。GPT-5.6 Sol や Claude Fable 5 と直接競合。
- [Gemma 4 12B](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/) - 🆕 **2026-06**。テキスト・画像・音声をシングルパスで処理する**統合エンコーダレスアーキテクチャ**を採用した新型マルチモーダルオープンモデル。16GB VRAM でのローカル動作を想定。
- [DiffusionGemma](https://www.marktechpost.com/2026/06/10/google-ai-releases-diffusiongemma-a-26b-moe-open-model-using-text-diffusion-for-up-to-4x-faster-generation/) - 🆕 **2026-06**。**テキストディフュージョン（拡散）アーキテクチャ**により、自己回帰型モデルと比べて生成速度が最大 **4 倍**速い 26B の MoE オープンモデル。

- [Gemini 3.5 Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - 🆕 **2026-05-19 — Google I/O 2026**。Gemini App と Google 検索 AI Mode の新しいデフォルトモデル。公式によると出力トークン速度は同類のフロンティアモデルより **約 4 倍高速**、主要ベンチマークで Gemini 3.1 Pro を上回る。Gemini 3.5 Pro は 6 月公開予定だったが延期（上記参照）。
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

- [Meta Muse Image](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) - 🆕 **2026-07-07**。Meta Superintelligence Labs の最も高度な画像生成モデル — Web 検索、コード実行、自己修正などの推論ステップを経てから画像を生成する「エージェント型」モデル。Meta AI アプリ、Instagram Stories（米国）、一部の国の WhatsApp で展開（Facebook は近日対応）。なお、他ユーザーの公開 Instagram プロフィール画像を利用できる物議を醸した機能は、フィードバックを受けて 7 月 10 日に追加後撤回された。
- [Muse Spark 1.1](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/) - 🆕 **2026-07-09**。Meta Model API の新しいパブリックプレビューを介して提供される、エージェントタスク向けマルチモーダル推論モデル。オープンソースの Llama ラインと並行した、独自の収益重視モデルへの戦略的シフトを示す。
- [Meta Muse Video](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) - 🆕 **2026-07-07（プレビュー）**。Muse Image と同じ基盤技術で構築された動画生成モデル。テキスト→動画部門で Arena 第 3 位。Muse Image の発表と同時にプレビュー公開 —「クリエイターと Meta AI に近日提供」。
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

- [Mistral Medium 3.5](https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04) - 🆕 **2026-04-28**。Dense 128B のオープンウェイトモデル、256K コンテキスト、Modified MIT ライセンス。指示追従・推論・コーディングを統合。
- [Leanstral 1.5](https://mistral.ai/news/leanstral-1-5/) - 🆕 **2026-07-02**。Lean 4 での証明エンジニアリング向け形式検証モデル — 119B 総 / 6B アクティブ、Apache 2.0、ウェイトは Hugging Face で公開、無料 API エンドポイントも提供。miniF2F で 100%、PutnamBench 672 問中 587 問を解き、57 の実世界リポジトリで未報告のバグ 5 件を発見。
- [Robostral Navigate](https://mistral.ai/news/robostral-navigate/) - 🆕 **2026-07-08**。Mistral 初のロボティクスモデル — 単一の RGB カメラのみで、自然言語の指示から車輪型・脚型・飛行型ロボットをオフィス・家庭・屋外でナビゲートする 8B の身体性ナビゲーションモデル（未見の検証環境で成功率 76.6%）。約 40 万件のシミュレーション軌跡で完全内製訓練。
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

- [DeepSeek-V4-Pro](https://api-docs.deepseek.com/news/news260424) - 🆕 **2026-04-24（プレビュー）；正式版ローンチは 2026 年 7 月中旬**。1.6T 総 / 49B アクティブ MoE、1M トークン。MIT。エージェント能力・世界知識・推論でリードし、オープンソースベンチマーク首位。正式な V4 ローンチではピーク / オフピークの API 価格制（北京時間ピーク帯は 2 倍）を導入；deepseek-v4-pro / deepseek-v4-flash が現在の本番 API モデル。
- [DeepSeek-V4-Flash](https://api-docs.deepseek.com/news/news260424) - 🆕 2026-04-24。284B 総 / 13B アクティブ MoE、1M コンテキスト。MIT。コスト効率版。
- [DeepSeek Agent Harness チーム](https://www.scmp.com/tech/big-tech/article/3354113/deepseek-recruits-former-jane-street-engineer-catch-ai-agents-revenue-race) - 🆕 **2026-05-19**。DeepSeek が Jane Street 出身のエンジニアを迎え、DeepSeek V4 を**収益を生む自律型エージェント**に仮定する「AI harness」チームを新設。DeepSeek が素のモデル R&D からエージェント製品化へ軸足を辻りたことを示す初の明確なシグナル。
- [DeepSeek-V3.2](https://www.deepseek.com/) - 2025-12 公開。671B MoE、V3.2 Speciale 推論強化版あり。⚠️ API モデル ID deepseek-chat / deepseek-reasoner（V3.2 世代）は 2026-07-24 付で非推奨 — V4-Flash の各モードに置き換え。
- DeepSeek-R2 - 🧪 **未リリース / 噂段階。** 2026 年 7 月中旬時点で公式発表・モデルカード・API ID は存在せず、推論は V4 の Thinking モードで提供される。
- [DeepSeek-R1](https://www.deepseek.com/) - 2025-01 公開、思考連鎖推論モデル。
- [DeepSeek-Coder-V2](https://github.com/deepseek-ai/DeepSeek-Coder-V2) - GPT-4 と互角のコード生成モデル。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeepseek-ai%2FDeepSeek-Coder-V2&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Alibaba (Qwen) 🇨🇳

- [Qwen 3.7-Max](https://www.scmp.com/tech/big-tech/article/3354212/alibaba-unveils-new-qwen-model-custom-chips-bid-become-chinas-ai-factory) - 🆕 **2026-05-20 — アリババクラウド杭州サミット**。AI エージェントの基盤として設計された新フラッグシップ。エージェント型コーディング、複雑推論、**長い見通しのマルチステップテイスク**に強い。同期に T-Head の **Zhenwu M890** AI アクセラレーターとフルスタック AI 基盤アップグレードも公開。世界中の開発者 / 企業へ順次提供。
- [Qwen 3.7-Max-Preview / Plus-Preview](https://www.scmp.com/tech/tech-trends/article/3354087/alibaba-teases-new-qwen-previews-highest-ranking-chinese-ai-models-arena) - 🆕 **2026-05-18**。杭州サミットの前哨プレビュー。LM Arena においてテキストとビジョンの両方で**中国モデルとして最高スコア**を取得。
- [Qwen3.6-27B](https://qwen.ai/blog?id=qwen3.6-27b) - 🆕 **2026-04-22**。27B 密マルチモーダル。オープン化。エージェントコーディング + 思考文脈保持。
- [Qwen3.6-Max-Preview](https://qwen.ai/) - 🆕 **2026-04-18**。プロプライエタリのフロンティアプレビュー。1M コンテキスト、中国モデルでコーディング首位級。
- [Qwen3.6-35B-A3B](https://qwen.ai/blog?id=qwen3.6-35b-a3b) - 🆕 **2026-04-15**。MoE 35B 総 / 3B アクティブ。Apache 2.0。安定性・実用性の改善。
- [Qwen3.6-Plus](https://qwen.ai/) - 🆕 **2026-04-02**。プロプライエタリのフラッグシップ。トークンあたりの価値が高く、長文脈・ツール呼び出し・エージェント挙動が良好。
- [HappyHorse 1.1](https://technode.com/2026/06/23/alibaba-unveils-happyhorse-1-1-video-generation-model-launches-global-ai-filmmaking-competition/) - 🆕 **2026-06-23**。アリババの動画生成モデル（T2V/I2V/S2V、音声同期付き最長 15 秒 1080p、マルチショットでのキャラクター一貫性が強力）。HappyHorse 1.0 は匿名で動画リーダーボードを制した後、2026-04-28 に限定ベータ入り。
- [Qwen3.5 Max Pro](https://qwen.ai/) - 2026-04。高性能フラッグシップ。
- [Qwen3.5 Omni Plus](https://qwen.ai/) - 2026-04。テキスト + 画像入力を統合した全モーダル。
- [Qwen3-Max-Thinking](https://qwen.ai/) - アリババ最強の Thinking モデル。1T+ パラメータ。
- [Qwen3.5-Omni](https://qwen.ai/) - 2026-03。完全全モーダル: 言語・視覚・音・動作。113 言語の音声認識、256K コンテキスト。
- [Qwen3-Coder-Next](https://qwen.ai/) - 2026-02。オープンウェイトのコーディングエージェントモデル、MoE 80B 総 / 3B アクティブ。
- [Qwen3 235B-A22B](https://qwen.ai/) - 二重モード推論 MoE。数学・コード・常識推論に強い。
- [Qwen2.5 Coder 32B](https://github.com/QwenLM/Qwen2.5-Coder) - トップクラスのオープンソースコーディングモデル。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FQwenLM%2FQwen2.5-Coder&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### xAI (Grok)

- [Grok 4.5](https://x.ai/) - 🆕 **2026-07-08**。xAI の最新フラッグシップ —— 実際の開発者インタラクションデータを利用して Cursor と共同訓練し、コーディングおよびエージェントタスクに最適化。500K トークンのコンテキストウィンドウ、関数呼び出し、構造化出力、Web/X 検索、コード実行、文書検索、コンテキスト圧縮を備える。xAI API、Grok Build、および Cursor のデフォルトモデルとして提供。100 万トークンあたり入力 $2 / 出力 $6。EU での提供は 7 月後半を予定。
- [Grok 4.3 GA](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-grok-4-3-on-microsoft-foundry-latest-generation-agentic-capabilities/4517096) - 🆕 **2026-05**。Grok 4.3 が Microsoft Foundry と OCI Generative AI で GA。xAI のエージェントワークロード向け旗艦で、ツール呼び出しと長期推論が強化。
- [Grok 4.3 Beta](https://x.ai/) - 🆕 2026-04。推論・コーディングベンチマーク強化。[`2026.4` ベンチマークスナップショット](https://benchlm.ai/) 参照。
- [Grok 4.20](https://x.ai/) - 2026-02。マルチエージェントシステム（Heavy モードで標準 4 + 専門 16）、2M コンテキスト。
- [Grok 4 / 4 Heavy](https://x.ai/) - 2025-07 公開。Grok 4 世代の xAI フロンティアモデル。
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

- [Command A+](https://cohere.com/blog/command-a-plus) - 🆕 **2026-05-20**。218B 総 / 25B アクティブ MoE、Apache 2.0 のオープンウェイト（Hugging Face）。入力 128K / 出力 64K。マルチモーダル、48 言語、エージェント型ツール使用；H100 2 枚または Blackwell GPU 1 枚で動作。
- [Command A](https://docs.cohere.com/v2/changelog/command-a) - 2025-03-13 公開。111B オープンウェイト、256K コンテキスト。エージェント・多言語・コーディング志向。
- [Command R+](https://cohere.com/) - エンタープライズ RAG モデル、128K コンテキスト、10 言語、引用付き grounded generation。
- [Command R](https://cohere.com/) - 経済的な RAG モデル。

### Baidu (ERNIE / 文心) 🇨🇳

- [ERNIE 5.1](https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/) - 🆕 **2026-05-08**。総パラメータは ERNIE 5.0 の約 1/3、アクティブは約 1/2 で、同等の事前学習コストの約 6% を実現；LMArena Search で中国モデル首位 / 世界 4 位（1,223）。
- [ERNIE 5.0](https://ernie.baidu.com/) - 2025-11-13 公開（Baidu World）。2.4T パラメータのオムニモーダル MoE（1 クエリで <3% 活性化）。
- [ERNIE 4.5](https://yiyan.baidu.com/) - 2025 年公開のマルチモーダル前任者。中国語・推論に強い。

### Zhipu AI / Z.ai (GLM) 🇨🇳

- [GLM-5.2](https://z.ai/blog/glm-5.2) - 🆕 **2026年6月13日**。コーディング優先の 744B MoE フラッグシップ。**100万トークンのコンテキスト**（GLM-5.1 の約 5 倍）、出力は最大 131K トークン。GLM Coding Plan の全ティアで利用可能。MIT のオープンウェイトと単体 API はローンチ週に順次公開。Claude Code・Cline・OpenCode・Roo Code・Goose・OpenClaw とそのまま互換。（ローンチ時にベンチマーク数値の公表なし。）
- [GLM-5.1](https://z.ai/blog/glm-5.1) - 🆕 **2026-04-08**。744B MoE / 40B アクティブ、200K コンテキスト。MIT ライセンス。SWE-Bench Pro で首位。
- [ZCode](https://www.scmp.com/tech/tech-trends/article/3359170/zhipu-ai-releases-harness-glm-52-model-chinese-firm-takes-aim-anthropic) - 🆕 🇨🇳 **2026-07-02**。Zhipu の GLM-5.2 用エージェントハーネス — モデルを自律コーディングエージェントに変え、Claude Code を正面から狙う。ローンチ特典として Coding Plan 加入者にクオータ +50%、新規ユーザーに 500 万無料トークン。
- [GLM-5 Reasoning](https://z.ai/) - 🆕 2026-04。BenchLM 85 —— **オープンソース最高スコア**。SWE-Bench Pro で GPT-5.4 と Claude Opus 4.6 を上回る。
- [GLM-5V-Turbo](https://z.ai/) - 🆕 2026-04。ネイティブマルチモーダルエージェント —— 視覚・動画クリップ・テキスト入力。コスト性能バランス。
- [GLM-5](https://z.ai/) - 2026-02 公開。744B パラメータ、先進的なエージェント知性。MIT。
- [GLM-4.7](https://z.ai/) - 2025 年末公開。SWE-Bench で Claude Opus 4 と互角。

### MiniMax

- [MiniMax M3](https://www.minimax.io/) - 🆕 **2026-06-01**。MiniMax Sparse Attention を備えたオープンウェイト（MIT）フラッグシップ — 1M トークン時の計算コストが約 1/20；フロンティア級のコーディング能力、SWE-Bench Pro 59.0%、BrowseComp 83.5%。
- [MiniMax-M2.7 (オープンウェイト)](https://www.minimax.io/) - 🆕 2026-04。230B 級のオープンウェイトフラッグシップ。コーディング・エージェントタスクでトップクラス。
- [MiniMax M2.7（クローズド）](https://venturebeat.com/technology/new-minimax-m2-7-proprietary-ai-model-is-self-evolving-and-can-perform-30-50) - 🇨🇳 🆕 **2026-03**。自己進化型のクローズド LLM。エージェントハーネスの構築、メモリ更新、ワークフローの反復改善に最適化され、SWE-bench 系タスクで大幅な性能向上。
- [MiniMax M2.5](https://www.codemotion.com/magazine/ai-ml/minimax-m2-5-low-costs-high-performance/) - 🇨🇳 **2026-02**。230B パラメータの旗艦モデル。"実世界の生産性" を狙ったコスト効率重視。
- [Hailuo 2.3 / 2.3 Fast](https://www.minimax.io/news/minimax-hailuo-23) - 🇨🇳 **2025-10**。MiniMax の現行動画フラッグシップ — SOTA の物理表現、キャラクターの微表情、強力なスタイライズ；Hailuo 02（2025）は I2V 特化バリアントとして継続。
- [MiniMax Music 2.6](https://aimlapi.com/blog/the-ultimate-guide-to-minimax-models-2026-m2-7-music-2-6-hailuo-video-advanced-tts) - 🇨🇳 🆕 **2026-04-10**。カバー生成に特化し、低音域の再現性を改善。グローバル beta。
- [MiniMax-M1-80k](https://www.minimax.io/) - オープンウェイトのハイブリッドアテンション推論モデル。456B パラメータ、1M トークン。
- [Hailuo AI (動画)](https://hailuoai.video/) - テキスト/画像から動画への生成、AI アバター・ナレーション・キャラクター一貫性。
- [Kilo Code 統合](https://www.minimax.io/) - MiniMax モデルは Kilo Code（kilo.ai のオープンソース AI コーディング拡張）で広く採用されている。

### Moonshot AI (Kimi) 🇨🇳

- [Kimi K3](https://kimi.ai/) - 🆕 **2026-07-16**。Moonshot AI 最大のフラッグシップ: **2.8T パラメータ**疎 MoE (896 エキスパート中 16 が有効)、**1M トークンコンテキスト**、ネイティブビジョン、マルチエージェント機能。Kimi Delta Attention（長文脈デコードを高速化するハイブリッド線形アテンション）を導入。API は入出力 100 万トークンあたり $3.00 / $15.00。kimi.com、Kimi API、統合プラットフォームで利用可；フルオープンウェイトは 2026 年 7 月下旬公開予定。
- [Kimi K2.7 Code](https://kimi.ai/) - 🆕 **2026年6月12日**。K2.6 のコーディング優先後継 —— 1T MoE / 32B アクティブ（384 エキスパート）、256K コンテキスト、Modified MIT、Hugging Face + Kimi API で公開。長期的なエージェントコーディング向けで推論トークン消費を約 30% 削減。Moonshot 公表の Kimi Code Bench v2 で K2.6 比 +21.8%（ベンダーベンチマーク）。入出力 100 万トークンあたり $0.95 / $4.00。
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

- [Nova 2 Pro](https://aws.amazon.com/nova/) - **2025-12-02（re:Invent）**。Amazon の最強推論モデル。テキスト・画像・動画・音声入力。エージェントコーディングと長期計画。
- [Nova 2 Lite](https://aws.amazon.com/nova/) - **2025-12-02**。1M コンテキスト + "thinking effort" 調整。
- [Nova 2 Sonic](https://aws.amazon.com/nova/) - **2025-12-02**。リアルタイム音声対音声モデル。多言語。
- [Nova Act](https://aws.amazon.com/nova/) - **2025-12-02**。ブラウザ Web タスクエージェントサービス。Nova 2 Lite 駆動で再ローンチ。
- [Nova Forge](https://aws.amazon.com/nova/) - **2025-12-02**。カスタム Nova モデル訓練の「オープントレーニング」サービス。

### NVIDIA (Nemotron)
- [Nemotron 3.5 ASR](https://developer.nvidia.com/nemotron) - 🆕 **2026-06-06**。NVIDIA の 600M パラメータ・キャッシュアウェアなストリーミング音声認識モデル — 40 の言語ロケールでリアルタイム文字起こし。
- [Nemotron 3 Ultra (550B)](https://research.nvidia.com/labs/nemotron/Nemotron-3-Ultra/) - 🆕 **2026-06-04**。長時間稼働エージェント向けの、550B 総 / 55B アクティブのハイブリッド Mamba-Transformer MoE オープンウェイトモデル。米国オープンモデルの中でフロンティア級の推論、Blackwell に最適化。
- [Nemotron-Labs-TwoTower](https://huggingface.co/nvidia/Nemotron-Labs-TwoTower-30B-A3B-Base-BF16) - 🆕 🧪 **2026-07-01**。NVIDIA Research のオープンウェイト拡散言語モデル。凍結した Nemotron-3-Nano-30B-A3B バックボーンから適応 — 片方のタワーがコンテキストを保持し、もう片方がトークンを並列に生成することで、再訓練なしに約 2.4× のスループットを実現。
- [Nemotron 3 Super](https://developer.nvidia.com/nemotron) - 🆕 2026-03-11（GTC）。120B 総 / 12B アクティブ、1M コンテキスト。前世代比 5 倍のスループット。
- [Nemotron 3 Nano](https://developer.nvidia.com/nemotron) - **2025-12-15**。経済的な Transformer-Mamba ハイブリッド MoE。
- [Nemotron 3 Nano Omni](https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/) - 🆕 **2026-04-28**。30B-A3B ハイブリッド MoE、ネイティブマルチモーダル。同等オープン omni モデル比 9 倍スループット。MMlongbench-Doc / OCRBenchV2 / WorldSense / DailyOmni / VoiceBench で 6 リーダーボード首位。

### Tencent (Hunyuan) 🇨🇳

- [Hunyuan Hy3](https://hy.tencent.com/research/hy3) - 🆕 🇨🇳 **2026-07-06**。Hy3 の正式リリース（295B 総 / 21B アクティブ MoE、256K コンテキスト）、Apache 2.0。4 月のプレビューから強化学習を強化し、安定性とコスト効率を改善。オープンウェイトは Hugging Face と ModelScope で公開、OpenRouter にも順次展開。元宝、CodeBuddy、WorkBuddy、ima、Marvis、Weixin カスタマーサービスに統合。
- [Hunyuan Hy3 Preview](https://hy.tencent.com/hy3-preview) - 🇨🇳 **2026-04**。正式版 Hy3 に先立つプレビュー："fast-slow thinking fusion" アーキテクチャ、推論効率 40% 改善、vLLM と SGLang 対応。GitHub / Hugging Face / ModelScope / GitCode でオープンソース化。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTencent-Hunyuan%2FHy3-preview&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Apple

- [Apple Foundation Models (AFM)](https://machinelearning.apple.com/research/introducing-apple-foundation-models) - Apple Intelligence の中核となるオンデバイス（~3B）+ サーバーモデル。プライバシー優先、オフライン対応。**WWDC 2026（6 月 8 日）**: 第 3 世代 AFM ラインナップ（オンデバイスの AFM Core / AFM Core Advanced、Private Cloud Compute 上の AFM Cloud / AFM Cloud Pro）が刷新された Siri を駆動。カスタム Google Gemini 基盤（年間約 $1B の契約）を用いた蒸留の支援を受けて訓練されているが、Google のコードは搭載しない。iOS 27 の新しい「Extensions」フレームワークにより、ChatGPT / Claude / Gemini が Siri と並ぶサードパーティ AI として動作可能。
- [OpenELM](https://machinelearning.apple.com/research/openelm) - Apple Silicon オンデバイス向けオープンソース効率言語モデル（270M~3B）。

### Samsung

- [Samsung Gauss 2.3](https://www.sammobile.com/news/samsung-develops-own-agentic-ai-tools-improves-gauss-ai-models/) - **2025-11**。Samsung Research の自社 LLM ファミリー（Gauss 2.3、Gauss 2.3 Think、Gauss O Flash）。社内のエージェントツール群を駆動し、Galaxy S26（2026 年発売）のシステム全体のエージェント AI を支える。

### StepFun 🇨🇳

- [Step 3.7 Flash](https://github.com/stepfun-ai/Step-3.7-Flash) - 🆕 **2026-05-29**。コーディングエージェントと検索ワークフロー向けの、オープンウェイト 198B MoE ビジョン言語モデル；最大 ~400 tokens/s。Step 3.5 Flash の後継。
- [Step 3.5 Flash](https://github.com/stepfun-ai/Step-3.5-Flash) - **2026-02**。オープンウェイト 196B MoE（11B アクティブ）の推論 + エージェントモデル。より大きな旗艦と互角に渡り合う。

### Baichuan 🇨🇳

- [Baichuan-M3 Plus](https://pandaily.com/baichuan-ai-launches-low-hallucination-medical-model-m3-plus-announces-free-access-program) - 🆕 **2026-01**。証拠に基づく低幻覚率の医療 LLM。中国国内の医療機関向けに無料 API を提供。

### Inflection AI

- [Inflection 2.5 / Pi](https://inflection.ai/) - 💤 共感的会話 AI（Inflection 2.5、2024 年 3 月）。Microsoft がチームの大半を吸収した後（2024 年）エンタープライズ AI に転換し、次世代フロンティアモデルの開発は行っていない。Pi は限定的な形で提供が続く。

### 01.AI 🇨🇳

- [Yi-Lightning](https://www.01.ai/) - 💤 MoE、RTX 4090 で 200+ tokens/s。中英多言語に強い。2024-10 公開 — 01.AI 最後の主要モデルで、同社は 2025 年 3 月に LLM の事前学習を停止し、DeepSeek ベースのエンタープライズソリューションに転換。

### 中国科学院 🇨🇳

- [ScienceOne 100 / 磐石100](https://english.cas.cn/newsroom/cas-in-media/202604/t20260429_1158251.shtml) - 🆕 **2026-04-28~29**。中国科学院の科学研究 AI 系統。コアの "ScienceOne" 基盤モデル + 文献コンパス + 革新評価エンジン + 2,000+ ツールエージェントファクトリー。数学・物理・生物・材料・天文・宇宙・地球科学を網羅。50+ CAS 研究所、100+ 研究シナリオで使用。

---

## 🎨 マルチモーダルと生成 AI

*画像・動画・音声・音楽の生成と編集のためのツールとモデル。*

### 画像生成

- [Meta Muse Image](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) - 🆕 **2026-07-07**。MSL 発の Meta 最先端画像生成モデル — Web 検索・コード実行・自己修正を経てから画像を生成するエージェント型設計。Instagram Stories（米国）と一部の国の WhatsApp で展開（Facebook は近日対応）。Meta AI アプリと meta.ai でも利用可能。
- [Midjourney V8.1](https://updates.midjourney.com/v8-1-alpha/) - 🆕 **2026-04-14**。HD モードがデフォルトに（3 倍高速・低コスト）、ムードボードとスタイルリファレンスの安定化、画像プロンプト復活；alpha.midjourney.com のみ。V8 アップスケーラーと編集 / インペイントの強化が次の予定。
- [FLUX.2 Pro / Flex / Dev / Klein](https://bfl.ai/blog/flux-2) - 🆕 **2025-11-25**。Black Forest Labs の次世代ファミリー。SOTA 画質、マルチリファレンスの一貫性（最大 10 枚）、文字描画の大幅改善；オープンウェイトの 32B Dev バリアントあり。
- [Recraft V4 / V4.1](https://www.recraft.ai/blog/introducing-recraft-v4-design-taste-meets-image-generation) - 🆕 **2026-02-17**（V4.1 は **2026-05-14**）。フルリビルド。プロンプト追従性が大幅改善、編集可能な SVG ベクター出力に対応。V4.1 はフォトリアリズム、3D / グラデーション、Vector / Utility バリアントを追加。
- [Stable Diffusion 3.5](https://stability.ai/) - 一貫性・プロンプト追従が改善されたオープンソース画像生成。
- [Ideogram 3.0](https://ideogram.ai/) - 画像内のテキスト描画とデザイン志向の生成に強い。
- [ChatGPT Images 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/) - 🆕 **2026-04-21**。最先端の画像生成 — 文字描画・多言語対応・高度な視覚推論・反復編集のためのマルチターン編集が向上。
- [gpt-image-2](https://developers.openai.com/api/docs/models/gpt-image-2) - 🆕 **2026-04-21**。OpenAI 最新の画像生成 / 編集 API モデル。柔軟な画像サイズと高忠実度入力に対応。
- [DALL·E 3](https://openai.com/dall-e-3) - ChatGPT に統合された OpenAI のテキスト → 画像モデル。
- [Gemini 3 Pro Image (Nano Banana Pro)](https://deepmind.google/models/gemini-image/pro/) - Gemini 内のネイティブ画像生成。
- [Nano Banana 2 (Gemini 3.1 Flash Image)](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/) - 🆕 **2026-02-26**。Nano Banana Pro 級の品質と世界知識を Flash の速度で提供；最大 5 キャラクターの一貫性、512px～4K 出力、画像内の文字描画 / 翻訳に対応。
- [Kling Image 3.0 / 3.0 Omni](https://ir.kuaishou.com/news-releases/news-release-details/kling-ai-launches-30-model-ushering-era-where-everyone-can-be/) - 🇨🇳 🆕 **2026-02-05**。快手のネイティブ 2K/4K 画像生成。Kling 3.0 スイートの一部として Video 3.0 と同時ローンチ。
- [Flux](https://github.com/black-forest-labs/flux) - 💤 **Stale**（2025-07 以降更新なし）。Black Forest Labs のオープンソースモデル。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fblack-forest-labs%2Fflux&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Seedance 2.0](https://seed.bytedance.com/) - 🇨🇳 🆕 ByteDance の次世代画像/アニメーション生成 API。

### 動画生成

- [Meta Muse Video](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) - 🆕 **2026-07-07（プレビュー）**。Muse Image と同じアーキテクチャで構築された Meta Superintelligence Labs の動画生成モデル。テキスト→動画部門で Arena 第 3 位。Muse Image のローンチ時にプレビュー公開され、Meta 各アプリへの展開が見込まれる。
- [Runway Agent](https://runwayml.com/news/introducing-runway-agent) - 🆕 **2026-05-13**。テキストブリーフから **マルチショットの完成動画** までを一気通貫で仕上げる会話型エージェント：ストーリーボード → 生成 → カット → ナレーション、最終調整用のタイムラインエディタ付き。「プロンプトからラフカットまで」を実現した初の本格的なエンドツーエンド制作エージェント。
- [Veo 3.1](https://deepmind.google/technologies/veo/) - 🆕 **2025-10**。Google DeepMind のフラッグシップ動画モデル。**Veo 4** は 2026 年 7 月中旬時点で未リリース。
- [Runway Gen-4.5](https://runwayml.com/research/introducing-runway-gen-4.5) - 🆕 **2025-12**。Runway のフラッグシップ動画モデル。ローンチ時に Artificial Analysis のテキスト→動画ベンチマークで第 1 位。プラットフォームでは Kling 3.0 や Sora 2 Pro などサードパーティモデルも利用可（2026-02-20 追加）。
- [Kling VIDEO 3.0](https://app.klingai.com/) - 🇨🇳 🆕 **2026-02-04~07**。快手の新世代。リアルな人間の動き・リップシンク・音声同期付きナラティブ制作。
- [Sora 2 (via Runway)](https://runwayml.com/changelog) - OpenAI の Sora アプリは 2026 年 4 月 26 日に終了（API は 2026 年 9 月 24 日まで）したが、Sora 2 Pro は **2026 年 2 月 20 日**から Runway 内で利用可能。
- [Seedance 2.5](https://seed.bytedance.com/) - 🇨🇳 🆕 🧪 **2026-06-23**。Volcano Engine 2026 カンファレンスで発表された ByteDance の次期動画モデル：ネイティブ 30 秒のワンショット生成（従来 4〜15 秒）と、長いナラティブでのキャラクター / 商品の一貫性向上。ローンチ時は限定提供 — 公開価格や API は未確定。
- [Seedance 2.0](https://seed.bytedance.com/) - 🇨🇳 **2026-02**。ByteDance のマルチモーダル・シネマグレード動画生成、2K 解像度（2026-06-23 に 4K 出力へアップグレード）、1.5 比約 30% 高速。
- [Hailuo 2.3](https://www.minimax.io/news/minimax-hailuo-23) - 🇨🇳 **2025-10-28**。MiniMax のフラッグシップ動画モデル：SOTA の物理表現、キャラクターの微表情、強力なスタイライズ（アニメ / 水墨 / ゲーム CG）；Hailuo 02 価格の Hailuo 2.3 Fast バリアントあり。
- [Pika 2.5](https://pika.art/) - シーン・エフェクト制御付きクリエイティブ動画生成。
- [LTX Studio](https://ltx.studio/) - 🆕 AI 駆動シネマティック動画作成プラットフォーム。
- [HappyHorse 1.1](https://technode.com/2026/06/23/alibaba-unveils-happyhorse-1-1-video-generation-model-launches-global-ai-filmmaking-competition/) - 🇨🇳 🆕 **2026-06-23**。アリババの動画モデル（2026-04-10 に「HappyHorse-1.0」として正体を公開 — 匿名でベンチマーク首位を獲得した後、世界 2 位に浮上）。1.1 ではモーションダイナミクス、被写体の一貫性、プロンプト追従、音声生成を強化。HappyHorse サイト、Alibaba Cloud Bailian、Qwen Cloud で利用可能。
- [Sora](https://openai.com/sora/) - 📦 **提供終了**（アプリ 2026-04-26；API 2026-09-24）。OpenAI のテキスト→動画アプリは終了；Sora 2 Pro は Runway 内で存続。

### 音声・音楽

- [ElevenLabs Eleven v3 + ElevenAgents](https://elevenlabs.io/agents) - 🆕 2026 年に "インターネットのオーディオレイヤー" を標榜——70+ 言語対応で感情 Audio Tag を備えた TTS と、AIUC-1 認証を取得した ElevenAgents 音声エージェントプラットフォーム（マルチモーダルメッセージ、会話トピック発見、ツール呼び出し前の音声制御）を提供。
- [Cartesia Sonic 3 / 3.5](https://cartesia.ai/blog/introducing-line-for-voice-agents) - 🆕 **2026**。状態空間モデル系の TTS。first audio 到達まで約 40〜90ms（Sonic 3.5 は 2026 年 5 月 GA）。音声エージェント基盤 **Line** を支える（Line のエージェントは 2026 年 5 月以降、デフォルトで Sonic 3.5 TTS + Ink-2 STT 上で動作）。
- [Deepgram Nova-3 + Aura-2 + Flux Multilingual](https://deepgram.com/learn/best-voice-ai-agents-2026-buyers-guide) - 🆕 **2026 年 4 月**。45+ 言語の STT、200ms 未満の TTS、通話中に 10 言語を切り替えできる会話型 STT。
- [MiniMax Music 2.6](https://aimlapi.com/blog/the-ultimate-guide-to-minimax-models-2026-m2-7-music-2-6-hailuo-video-advanced-tts) - 🇨🇳 🆕 **2026 年 4 月 10 日**（グローバルベータ）。カバー生成に特化し、低音域の再現性が向上。
- [Voxtral TTS](https://www.forbes.com/sites/ronschmelzer/2026/03/26/mistral-releases-open-weight-voice-ai-built-for-speed/) - 🆕 **2026 年 3 月 26 日**。Mistral の音声エージェント向け、4B オープンウェイト TTS。
- [ElevenLabs](https://elevenlabs.io/) - AI 音声合成・クローン・対話 AI のリーダー。
- [Suno v5.5](https://suno.com/blog/v5-5) - 🆕 **2026-03-26**。高品質ボーカル付きの AI 音楽生成。v5.5 では Voices（本人確認済みの自分の声で歌わせる）、アップロード音源で訓練する Custom Models、My Taste パーソナライゼーションを追加。V6 は噂されているが未発表。
- [Udio](https://www.udio.com/) - 🆕 商用品質の音楽生成。
- [OpenAI Audio Models](https://openai.com/) - GPT-4o と GPT-Realtime-2（**2026-05-07**、GPT-Realtime-Translate / GPT-Realtime-Whisper と同時リリース）内のネイティブ音声理解・生成；gpt-realtime-2.1 / 2.1-mini は **2026-07-06** リリースで、英数字認識・ノイズ処理・割り込み挙動を改善。
- [Stability Audio](https://stability.ai/) - オープンソース音声・音楽生成。
- [Bark](https://github.com/suno-ai/bark) - 💤 **Stale**（2024-08 以降更新なし）。オープンソースのテキスト→音声モデル。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsuno-ai%2Fbark&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hume TADA](https://github.com/HumeAI/tada) - 🆕 **2026 年 3 月**。Hume AI 初のオープンソース TTS — Text Audio Dual Alignment (TADA)：テキストと音声を 1:1 に同期した単一トークンストリームで生成。コンテンツの幻覚ゼロ、RTF 約 0.09、TADA-1B/3B-ML モデル（9+ 言語）、スマートフォンで動作。コードは MIT、ウェイトは Llama 3.2 ライセンス。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHumeAI%2Ftada&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

## 🔗 エージェントプロトコルと標準

*エージェントの相互運用性・ツールアクセス・クロスプラットフォーム通信を可能にするオープン標準。*

### Model Context Protocol (MCP)

- [MCP Specification](https://modelcontextprotocol.io/) - 🆕 "AI 用の USB-C" —— Anthropic 製、LLM をツール・データソースに接続するオープンプロトコル。2025-12 に Linux Foundation 傘下の Agentic AI Foundation へ寄贈。
- [MCP 2026-07-28](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) - 🆕 **正式版 2026-07-28（RC は 2026-05-21 公開）**。MCP 次期メジャーリビジョン：**ステートレスプロトコルコア**（セッションアフィニティ不要で通常のラウンドロビン LB の背後にデプロイ可能）、**拡張フレームワーク**（逆 DNS ID、独立バージョニング）、**MCP Apps**（サンドボックス化 iframe でのサーバレンダリング UI）、Tasks の実験的コアから拡張への移行、**認可強化**（OAuth 2.0 / OpenID Connect との整合を締める 6 つの SEP）。加えて JSON Schema 2020-12 の完全対応、W3C Trace Context、正式な 12 か月非推奨ポリシー；Roots・Sampling・Logging は非推奨に。[SDK ベータ（Python / TypeScript / Go / C#）は 2026-06-29 に公開](https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/)。
- [MCP Servers](https://github.com/modelcontextprotocol/servers) - MCP サーバーの公式リファレンス実装集。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Fservers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - 公式 TypeScript SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Ftypescript-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - 公式 Python SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Fpython-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [mcp.so](https://mcp.so/) - 🆕 MCP サーバー・ツールのコミュニティディレクトリ。
- [CorpusIQ](https://mcp2.corpusiq.io/mcp) - 🆕 ⚠️ **Unverified。** MCP Registry に `io.corpusiq/multi-source-mcp` として掲載 — 25+ の統合（GA4、Google Ads、TikTok、YouTube、Shopify、Stripe、Airtable、Slack、HubSpot、Calendly、Klaviyo など）を備えるマルチソースビジネスデータコネクタ。インテリジェントなクエリルーティング、クロスソースアトリビューション、統合ビジネスインテリジェンス。`io.corpusiq/multi-source-mcp` として稼働中。Ed25519 署名認証付き HTTP トランスポート。
- [Agentage Memory](https://memory.agentage.io/mcp) - 🆕 ⚠️ **Unverified。** MCP Registry に `io.agentage/memory` として掲載 —— すべての AI（Claude / Cursor / ChatGPT）が共有・読み書き可能なファイルベースのメモリ。ローカルでマークダウンとして同期されエクスポート可能。リモート Streamable HTTP (OAuth 2.1 + PKCE + Dynamic Client Registration)。6つのツール（`memory__search/read/write/edit/list/delete`）を提供。[ドキュメント](https://agentage.io/blog/mcp-endpoint-is-live)。
- [mcp-gateway](https://github.com/Zijian-Ni/mcp-gateway) - ⚠️ **Unverified**（初期段階）。MCP 接続のルーティングと管理を行うゲートウェイ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fmcp-gateway&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Agent-to-Agent Protocol (A2A)

- [A2A Protocol](https://github.com/a2aproject/A2A) - Google 発のエージェント間通信オープン標準。現在は Linux Foundation プロジェクトで 150+ パートナー組織。**v1.0 は 2026 年 5 月に公開**。フレームワーク不問でエージェントの発見・委譲・協調を可能にする；Python / Go / JS / Java / .NET / Rust の SDK あり。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fa2aproject%2FA2A&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [A2A Course (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/a2a-the-agent2agent-protocol/) - 🆕 A2A でマルチエージェントシステムを構築する無料コース。

### その他の標準

- [Agentic AI Foundation](https://aaif.io/) - 🆕 オープンエージェント標準を管理する Linux Foundation の組織 — MCP、goose、AGENTS.md、agentgateway をホスト。創設プラチナメンバー：AWS、Anthropic、Block、Bloomberg、Cloudflare、Google、Microsoft、OpenAI。
- [AGENTS.md](https://agents.md/) - 🆕 「エージェントのための README」を掲げるオープンな Markdown 規約 — AI コーディングエージェントにプロジェクト固有のコンテキストと指示を置く予測可能な場所を与える。60k+ のオープンソースプロジェクトで利用；Agentic AI Foundation（Linux Foundation）が管理。
- [Coinbase Base MCP](https://fortune.com/2026/05/26/coinbase-pushes-further-into-ai-payments-with-new-mcp-for-base-network/) - 🆕 **2026 年 5 月 26 日**。Coinbase が Base ブロックチェーン用 MCP サーバーを公開。Claude / Cursor / ChatGPT エージェントが暗号資産の取引やレンディングをオンチェーンで実行可能。大手取引所が初めて公開した、自律オンチェーン取引向けの MCP エンドポイント。
- [Robinhood Agentic Trading MCP](https://robinhood.com/us/en/newsroom/robinhood-is-now-open-to-agents/) - 🆕 **2026 年 5 月 27 日**（ベータ）。米国主要証券会社で初めて MCP 経由で株式取引を AI エージェントに開放。Agent（Claude / Codex / Cursor）は全口座への読み取りアクセスのみ、取引実行は隔離された Agentic 口座内に限定。全取引プッシュ通知 + ワンタップ切断スイッチ。
- [The Declaration of Intelligence](https://thedeclaration.ai) - ⚠️ AI エージェントと人間のための原則宣言のドラフト（v0.2）。GitHub のプルリクエスト経由で公開署名する。初期段階 — 直近の確認時点で署名者はごく少数。
- [Kuberna Labs](https://github.com/kawacukennedy/kuberna-labs) - ⚠️ **未検証。** AI エージェント向けクロスチェーン・インテント実行プロトコル。ERC-8004 オンチェーン ID、zkTLS/TEE 証明、型付きインテントスキーマを主張し、NEAR / Base / Mantle 上での自律トランザクション実行を謳う。新規リポジトリで独立採用は未確認——利用前に要評価。

---

## 🏗️ エージェントフレームワーク

*自律 AI エージェントを構築するためのフレームワークとライブラリ。*

- [Vercel Eve](https://github.com/vercel/eve) - 🆕 **2026-06-17（Vercel Ship 2026）**。Vercel がオープンソース化した「ファイルシステムファースト」の TypeScript エージェントフレームワーク。エージェントはファイルのディレクトリ（指示・ツール・スキル）であり、Vercel がサンドボックス実行・承認・評価・OpenTelemetry を内蔵した永続サービスにコンパイルする。任意のモデル・任意の MCP サーバー、Slack / Discord / GitHub などのチャネルに対応し、「エージェントの Next.js」と称される。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvercel%2Feve&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Databricks Omnigent](https://github.com/omnigent-ai/omnigent) - 🆕 **2026-06**。Databricks がオープンソース化したメタ Harness。既存のコーディングエージェント（Claude Code、Codex、Pi、カスタム）の上位に位置し、それらを同一システム内の相互運用可能な部品として統合——エージェントの構成、共有セキュリティポリシーの適用、リアルタイム協調を実現。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fomnigent-ai%2Fomnigent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Nokia NSP Agentic AI](https://www.globenewswire.com/news-release/2026/06/11/3310210/0/en/nokia-introduces-agentic-ai-framework-in-network-services-platform-to-enable-trust-based-ai-operations-for-ip-networks.html) - 🆕 **2026-06**。通信の Network Services Platform (NSP) 向けエンタープライズエージェントフレームワーク。複雑な IP ネットワーク上で推論とルーティング/保守実行を行うエージェントを展開する。
- [Alteryx Agent Studio](https://www.alteryx.com/blog/new-capabilities-in-alteryx-one-built-for-how-analysts-work) - 🆕 **2026-05**。信頼済みの Alteryx データセットとワークフローを会話型エージェントとしてパッケージ化；新しい Alteryx One MCP Server 経由で MCP エンドポイントを作成・管理（Claude、ChatGPT、Gemini で回答）。
- [Koog 1.0](https://github.com/JetBrains/koog) - 🆕 **2026-05-21 · KotlinConf 2026**。JetBrains による **Kotlin + Java** 向けオープンソースエージェントフレームワークが安定版 1.0 に到達し、長期サポート対象の安定 API サーフェスを提供。Kotlin Multiplatform でのクロスデプロイ（JVM / Android / iOS / JS / WASM）、ラッパー不要の Java 相互運用、Android ローカル LiteRT、全ターゲットでの OpenTelemetry、グラフベースワークフロー、Spring Boot / Ktor 連携、OpenAI / Anthropic / Google / Bedrock プロバイダーをサポート。Apache-2.0。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FJetBrains%2Fkoog&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangChain](https://github.com/langchain-ai/langchain) - LLM を使った文脈認識推論アプリの基盤。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangGraph](https://github.com/langchain-ai/langgraph) - エージェントを状態を持つマルチアクターのグラフとしてモデル化。0.3.x シリーズ（2025）でプリビルトエージェントが `langgraph-prebuilt` に分離 —— Supervisor / Swarm / LangMem / Trustcall。**v1.2（2026-05）**でノード単位のタイムアウト / エラーリカバリ / グレースフルシャットダウン、長いスレッドのチェックポイントオーバーヘッドを削減する新 `DeltaChannel`、コンテンツブロック中心のストリーミング API v3 を追加。最新は v1.2.4（2026-06）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flanggraph&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [CrewAI](https://github.com/crewAIInc/crewAI) - ロールプレイ型自律エージェントチームのオーケストレーションフレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FcrewAIInc%2FcrewAI&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [goose](https://github.com/block/goose) - Block 発のオープンソースで拡張可能な AI エージェント（Rust 製デスクトップアプリ + CLI）。任意の LLM でインストール・実行・編集・テストを行う；15+ プロバイダー対応；Agentic AI Foundation（Linux Foundation）がホスト。v1.43.0（2026-07-14）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fblock%2Fgoose&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AG2](https://github.com/ag2ai/ag2) - 🆕 **2026-07-03 (v1.0.0b0)**。Microsoft AutoGen のコミュニティ主導 Fork — AutoGen がメンテナンスモードになった後も開発継続。Apache-2.0。既存 AutoGen プロジェクトから移行容易。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fag2ai%2Fag2&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/) - 🆕 AutoGen + Semantic Kernel を統合した新フレームワーク。マルチエージェント + エンタープライズ機能。
- [Microsoft Agent 365](https://techcommunity.microsoft.com/blog/agent-365-blog/what%E2%80%99s-new-in-agent-365-may-2026/4516340) - 🆕 **2026 年 5 月 GA**。AI エージェント向けの企業級可観測性 + ガバナンス + セキュリティ基盤。2026 年 5 月アップデートで、エージェント向け SASE、脅威検知 / ブロック、エージェント脅威ハンティングのワークフローを追加。KPMG は 276,000 人の専門家をカバーするグローバル展開を発表（2026-06-09）。
- [Microsoft Scout](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) - 🆕 **2026-06-02（Build 2026）**。オープンソースの OpenClaw ランタイム上に構築された、Microsoft 365 向けの常時稼働パーソナルワークエージェント。
- [AutoGen](https://github.com/microsoft/autogen) - 💤 **メンテナンスモード**（最終リリース 2025-09；Microsoft Agent Framework に後継され、以降はコミュニティ管理）。Microsoft のマルチエージェント会話フレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fautogen&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Google Agent Development Kit (ADK)](https://github.com/google/adk-python) - 🆕 Gemini + Vertex AI と密接に統合したモジュラーフレームワーク。階層エージェント構成。**v2.0 はベータ**（v2.0.0b1、2026-04）でワークフローオーケストレーションと刷新されたエージェント実行モデルを搭載；最新安定版は v1.33（2026-05）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle%2Fadk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - 🆕 [2026-04-15 進化](https://openai.com/index/the-next-evolution-of-the-agents-sdk/) —— ネイティブサンドボックス、MCP ネイティブ、サブエージェント handoff、Codex 風ファイル操作。プロダクション級マルチエージェント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fopenai-agents-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MetaGPT](https://github.com/geekan/MetaGPT) - 🇨🇳 LLM に SOP ソフトウェアチームの役割（PM / アーキテクト / エンジニア）を割り当てる多エージェント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgeekan%2FMetaGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Mastra](https://github.com/mastra-ai/mastra) - 🆕 TypeScript 優先のエージェントフレームワーク、ワークフロー駆動 + オブザーバビリティ内蔵。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmastra-ai%2Fmastra&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentGPT](https://github.com/reworkd/AgentGPT) - 📦 **Archived**（2026-01）。ブラウザでエージェントを構成・展開。第一波の代表、歴史的参照のみ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Freworkd%2FAgentGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [BabyAGI](https://github.com/yoheinakajima/babyagi) - 実験的な自己構築型自律エージェントフレームワーク；2023 年のタスク管理版オリジナル BabyAGI は現在 [babyagi_archive](https://github.com/yoheinakajima/babyagi_archive) にある。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fyoheinakajima%2Fbabyagi&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) - 💤 **Stale**（2025-01 以降更新なし）。オープンソース自律エージェントフレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTransformerOptimus%2FSuperAGI&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) - LLM 技術をアプリに統合。C# / Python / Java。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fsemantic-kernel&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agno (旧 Phidata)](https://github.com/agno-agi/agno) - メモリ・知識・ツール・推論つきマルチモーダルエージェント；v2.7.x（2026-07）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagno-agi%2Fagno&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [DSPy](https://github.com/stanfordnlp/dspy) - "プロンプトを書くのではなくプログラミングする" 言語モデルフレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstanfordnlp%2Fdspy&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenClaw](https://github.com/openclaw/openclaw) - 🆕 スキル・メモリ・マルチチャネルメッセージング・Dreaming（3 段階メモリ統合）・Canvas/A2UI・ACP コーディング harness 統合・Standing Orders を備えた個人向け AI エージェントプラットフォーム。最新版: **v2026.7.1**（2026-07-13）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenclaw%2Fopenclaw&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Dify](https://github.com/langgenius/dify) - 🇨🇳 ビジュアルエージェントビルダー付きオープンソース LLM アプリ開発プラットフォーム。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flanggenius%2Fdify&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Haystack Agents](https://github.com/deepset-ai/haystack) - エージェント型パイプラインのエンドツーエンド LLM フレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeepset-ai%2Fhaystack&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vellum AI](https://www.vellum.ai/) - 🆕 プロダクション級プロプライエタリ SaaS：プロンプト構築・評価・バージョニング・オブザーバビリティ。
- [FastAgency](https://github.com/airtai/fastagency) - 💤 AG2 (AutoGen) マルチエージェントワークフローをコンソール・Mesop Web UI・REST/FastAPI・NATS アダプタ経由で本番デプロイ；最終リリース 2025-12。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fairtai%2Ffastagency&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Rasa](https://github.com/RasaHQ/rasa) - 💤 **メンテナンスモード**（最終リリース 2025-01；後継は Rasa CALM）。強力な意図認識と対話管理のオープンソース対話 AI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FRasaHQ%2Frasa&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Lindy](https://www.lindy.ai/) - 🆕 ビジネスユーザー向けノーコードエージェント、ビジュアルワークフロービルダー。
- [Octomind](https://github.com/muvon/octomind) - 🆕 Rust ベースのオープンソース AI エージェントランタイム。モデル不問（13+）、コミュニティ製の専門エージェント（開発・医療・法律・DevOps）、ランタイム自己拡張対応 MCP、ゼロコンフィグ。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmuvon%2Foctomind&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsoft AI Agent Governance Toolkit](https://www.helpnetsecurity.com/2026/04/03/microsoft-ai-agent-governance-toolkit/) - 🆕 **2026-04-03**。LangChain や AutoGen などフレームワーク横断でランタイムセキュリティポリシーを強制するオープンソースツールキット。
- [Bernstein](https://github.com/sipyourdrink-ltd/bernstein) - 🆕 40+ の CLI 型コーディングエージェント（Claude Code / Codex / Gemini CLI / Cursor / Aider など）を一つにまとめる Python オーケストレーター。LLM は事前プランニング一回だけ使い、スケジューリング・git worktree 隔離・品質ゲート・HMAC 連鎖監査は決定論的。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsipyourdrink-ltd%2Fbernstein&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Genkit Middleware](https://developers.googleblog.com/announcing-genkit-middleware-intercept-extend-and-harden-your-agentic-apps/) - 🆕 **2026-05-14**。Google の OSS エージェントフレームワーク Genkit にミドルウェアを追加。generate / model / tool の 3 階層でコンポーザブルなフックを提供 —— 指数バックオフでのリトライ、モデルフォールバック、ツールタその人手承認ゲート、SKILL.md スキル注入、スコープを限定したファイルアクセス。TS / Go / Dart、Python 予定。
- [LlamaIndex ↔ Google Agents API 連携](https://www.kucoin.com/news/flash/google-launches-agents-api-llama-index-integrates-llamaparse-for-unstructured-document-processing) - 🆕 **2026-05-20**。LlamaIndex が Google の新 Agents API 向けのテンプレートを公開し、サンドボックスの Linux 環境上で **LlamaParse** / **LiteParse** を提供して非構造化文書を処理。
- [NarraNexus](https://github.com/NetMindAI-Open/NarraNexus) - NetMind.AI によるすぐ使える AI エージェントチームワークスペース——記憶を持つエージェントが初日から文脈を保持し、協働し、ツールを使う。マルチエージェント（PM/開発/デプロイ/リサーチ）、永続コンテキスト、MCP 型統合。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNetMindAI-Open%2FNarraNexus&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Ontheia](https://github.com/Ontheia/ontheia) - ⚠️ **Unverified**（初期段階・採用実績少）。セルフホスト型のオープンソース AI エージェントプラットフォーム。マルチプロバイダ（Claude / OpenAI / Gemini / Ollama）、MCP ネイティブ、ビジュアル workflow 自動化のための Chain Engine、長期メモリ（pgvector）、マルチユーザ RBAC、アーキテクチャレベルでの GDPR 適合。AGPL-3.0。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOntheia%2Fontheia&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Coze Studio](https://github.com/coze-dev/coze-studio) - 🆕 🇨🇳 ByteDance のオープンソース AI エージェント開発プラットフォーム——オールインワンのビジュアルビルダーで作成・デバッグ・デプロイを一括管理。Apache-2.0、20K+ stars。Coze.com のオープンソース版。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Strands Agents (AWS)](https://github.com/strands-agents/sdk-python) - 🆕 **2026 年 4〜6 月**。AWS オープンソースのモデル駆動型エージェント SDK（Python + TypeScript 1.0 GA：2026-04-30）。Bedrock / Anthropic / OpenAI / Ollama 対応、マルチエージェント編成パターン（グラフ / スウォーム / ワークフロー）、組み込み可観測性 hooks、A2A プロトコル対応；TypeScript SDK は現在 [harness-sdk モノレポ](https://github.com/strands-agents/harness-sdk)で管理。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstrands-agents%2Fsdk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [CrewAI 1.14](https://github.com/crewAIInc/crewAI) - 🆕 **2026 年 6 月**。メモリ・ナレッジ・RAG のプラグイン可能バックエンド、宣言型 Flows + CLI/TUI サポート、会話型フロー用 Chat API、ネイティブ Snowflake Cortex LLM、LangChain 依存を除去し軽量化。最新安定版: 1.14.6（2026-05-28）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FcrewAIInc%2FcrewAI&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Oracle AI Agent Studio (Fusion)](https://www.oracle.com/news/announcement/oracle-introduces-ai-native-builder-experience-2026-07-14/) - 🆕 **2026-07-14**。Oracle Fusion Cloud アプリケーション内蔵の AI ネイティブビルダー。Fusion のビジネスオブジェクト・ワークフロー・セキュリティコンテキストを引き継ぐ専門エージェントチームによる「Fusion Agentic Applications」を構築。ノーコード/ローコード/プロコード全対応；Fusion 顧客は追加費用なしで利用可能。

---

## 🛠️ エージェント IDE とビジュアルビルダー

*コードを書かずに（または最小限で）エージェントワークフローを設計・デバッグ・出荷するためのビジュアル環境。*

- [LangGraph Studio](https://docs.langchain.com/langsmith/studio) - LangGraph エージェントのビジュアルデバッガとトレース検査（現在は LangSmith の一部）。状態のステップ実行、ターンの再生、メッセージの途中編集が可能。
- [Dify](https://github.com/langgenius/dify) - 🇨🇳 ドラッグ&ドロップのエージェントワークフロービルダー付きオープンソース LLM アプリ開発。プロダクション利用が主流。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flanggenius%2Fdify&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agenta](https://github.com/agenta-ai/agenta) - 🆕 プロンプトプレイグラウンド・プロンプト管理・評価実行・オブザーバビリティを統合したオープンソース LLMOps プラットフォーム。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagenta-ai%2Fagenta&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vellum AI](https://www.vellum.ai/) - クローズドソース SaaS。
- [Coze Loop](https://github.com/coze-dev/coze-loop) - 🇨🇳 🆕 ByteDance の Coze チームによるオープンソースのエージェント最適化プラットフォーム。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-loop&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
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
- [MemoryLake](https://memorylake.ai) - 🆕 **2026 年 7 月**。「エージェントのメモリーパスポート」——異なるエージェント・ツール間で共有されるプラットフォーム中立のメモリレイヤー。ユーザー/エージェント/セッション単位のスコープ付き記憶を統一 API で提供。
- [Supermemory](https://github.com/supermemoryai/supermemory) - 🆕 多様なデータソース（Web・ドキュメント・チャット）から構築するコンテキストグラフ。API ファーストで MCP と主要フレームワークに統合。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsupermemoryai%2Fsupermemory&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Graphlit](https://www.graphlit.com/) - 🆕 本番エージェント向けコンテキストプラットフォーム：取り込み、エンティティ抽出、検索 + RAG 用ナレッジグラフ。Claude / Cursor / Copilot 連携用の MCP サーバーを公開。
- [Mem0](https://github.com/mem0ai/mem0) - LLM アプリ用の自己改善型メモリ層。**2026 年 4 月のアルゴリズム刷新**：シングルパスの追加専用抽出、エンティティリンク、マルチシグナル検索；LoCoMo・LongMemEval・BEAM でベンチマーク首位。60K+ stars、21+ の公式フレームワーク統合。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmem0ai%2Fmem0&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Remio](https://remio.ai/) - 🆕 パーソナルコンテキスト向けのローカルファースト AI メモリ / ナレッジベースデスクトップアプリ（Windows/Mac）。ファイル・Web ページ・録音・メール・メッセージ・画像をローカルのインデックスとベクトルに変換し、エージェントがディレクトリを繰り返し grep したり文書全体をプロンプトに読み込む代わりに、絞り込んだコンテキストを取得できるようにする。ローカルファースト + BYOK。
- [Zep](https://github.com/getzep/zep) - AI アシスタント・エージェント向け長期メモリ。注：オープンソースの Community Edition は非推奨 — リポジトリは現在 Zep Cloud の SDK / サンプル置き場；Zep のアクティブな OSS は [Graphiti](https://github.com/getzep/graphiti) を参照。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgetzep%2Fzep&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [agent-memory](https://github.com/Zijian-Ni/agent-memory) - ⚠️ **Unverified**（初期段階）。セッション横断の文脈永続化を実現する軽量エージェントメモリフレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fagent-memory&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangMem](https://github.com/langchain-ai/langmem) - LangChain のエージェント向け長期メモリ SDK — LangGraph の永続化レイヤーに接続するセマンティック / エピソード / 手続き記憶プリミティブ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangmem&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Motorhead](https://github.com/getmetal/motorhead) - 💤 **メンテナンス終了**（メンテナが非推奨化；最終リリース 2023-12）。LLM 用メモリ・文脈管理サーバー。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgetmetal%2Fmotorhead&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ChromaDB](https://github.com/chroma-core/chroma) - AI ネイティブのオープンソース埋め込みデータベース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fchroma-core%2Fchroma&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cognee](https://github.com/topoteretes/cognee) - グラフ + LLM + ベクトル検索による決定論的 LLM 出力。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftopoteretes%2Fcognee&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangGraph Memory](https://github.com/langchain-ai/langgraph) - 🆕 状態管理エージェントワークフロー用の組み込み永続化とチェックポイント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flanggraph&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Graphiti](https://github.com/getzep/graphiti) - 🆕 時間意識を備えたエージェントメモリ用知識グラフ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgetzep%2Fgraphiti&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude Managed Agents Memory](https://platform.claude.com/docs/en/release-notes/overview) - 🆕 **2026-04-23**（パブリックベータ）。Claude Managed Agents 用 Anthropic 永続メモリ機能。読み書きメモリストアをエージェントのファイルシステムにマウントしてセッション間で情報を保持。
- [OpenViking](https://github.com/volcengine/OpenViking) - 🆕 🇨🇳 ByteDance Volcengine のオープンソース・エージェント用コンテキストデータベース（OpenClaw などに対応）。メモリ・リソース・スキルをファイルシステムパラダイムで統合管理し、階層的コンテキスト配信と自己進化を実現。AGPL-3.0、22K+ stars。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvolcengine%2FOpenViking&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ReMe](https://github.com/agentscope-ai/ReMe) - 🆕 🇨🇳 Alibaba AgentScope チームのエージェント用メモリ管理キット——ファイルベース＋ベクトルベースのメモリを組み合わせ、コンテキストウィンドウの制約とステートレスセッションの 2 つの課題を解決。Apache-2.0。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentscope-ai%2FReMe&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [taOSmd](https://github.com/jaylfc/taosmd) - 🆕 ⚠️ **Unverified.** すべてのターンを逐語で追記専用・ゼロロスのアーカイブに保持し、抽出した各事実をソースにリンクするローカルファーストのエージェントメモリ — 検証器が裏付けられない事実は想起から降格される（served-hallucination 計測値 0.04、その後 0.00）。supersede 対応の型付き時系列ナレッジグラフに加え、ベクトル + BM25 のハイブリッド検索；小型ローカルモデル向けにチューニングされ、完全オフライン（8 GB の SBC や RK3588 NPU で動作）。作者報告で LongMemEval-S の Recall@5 97%、`docs/benchmarks.md` から再現可能。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fjaylfc%2Ftaosmd&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hindsight](https://github.com/vectorize-io/hindsight) - 🆕 会話履歴だけでなく経験から学習するエージェントメモリ。生体模倣型データ構造で世界の事実・エージェントの経験・学習したメンタルモデルを整理；`retain`/`recall`/`reflect` プリミティブ；Agent Memory Benchmark (AMB) を同梱。MIT、15K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvectorize-io%2Fhindsight&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SimpleMem](https://github.com/aiming-lab/SimpleMem) - 🆕 LLM エージェント向けの効率的な生涯メモリ——マルチモーダル（テキスト+画像+音声+動画）、ファインチューニング不要でトークン上限制約を突破。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Faiming-lab%2FSimpleMem&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agent Memory Techniques](https://github.com/NirDiamant/Agent_Memory_Techniques) - 🆕 実行可能な Jupyter ノートブック 30 本。会話バッファ、ベクトルストア、ナレッジグラフ、エピソード/意味記憶、MemGPT、Mem0、Letta、Zep、Graphiti、LoCoMo ベンチマークまで網羅する実践リファレンス。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNirDiamant%2FAgent_Memory_Techniques&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🔌 ツールと API 連携

*エージェントを外部サービス・API に接続するプロトコルとツール。*

- [ZoomMate](https://news.zoom.com/zoom-launches-zoommate/) - 🆕 💰 **2026-06-01 GA**。会議の会話を完了した作業に変える Zoom 純正の AI チームメイト — Salesforce レコードの更新、Jira 課題の作成、Slack 経由のリクエスト振り分けを実行。$20/ユーザー/月。
- [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol/servers) - AI モデルを外部ツール・データソースに接続するオープンプロトコル。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Fservers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [mcp-gateway](https://github.com/Zijian-Ni/mcp-gateway) - ⚠️ **Unverified**（初期段階）。MCP プロトコル接続のルーティングと管理を行うゲートウェイ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fmcp-gateway&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Composio](https://github.com/ComposioHQ/composio) - AI エージェント向け統合プラットフォーム —— マネージド認証付き 1000+ ツールキット。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FComposioHQ%2Fcomposio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Toolhouse](https://toolhouse.ai/) - AI ツール利用のクラウドインフラ —— ツールの保存・管理・実行。
- [LangChain Tools](https://github.com/langchain-ai/langchain) - LangChain エコシステム内の広範なツール統合。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Arcade AI](https://github.com/ArcadeAI/arcade-ai) - AI エージェント・アシスタント用ツール呼び出しプラットフォーム。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FArcadeAI%2Farcade-ai&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Browser Use](https://github.com/browser-use/browser-use) - AI エージェント用のブラウザ自動化。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowser-use%2Fbrowser-use&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Firecrawl](https://github.com/firecrawl/firecrawl) - ウェブサイトを LLM-ready なデータに変換。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ffirecrawl%2Ffirecrawl&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Crawl4AI](https://github.com/unclecode/crawl4ai) - 🆕 LLM フレンドリーなオープンソースクローラ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Funclecode%2Fcrawl4ai&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Stagehand](https://github.com/browserbase/stagehand) - 🆕 Browserbase 製の AI 駆動ブラウザ自動化フレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowserbase%2Fstagehand&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentQL](https://www.agentql.com/) - 🆕 AI エージェントが意味的にウェブページと対話するためのクエリ言語。
- [StackOne](https://www.stackone.com/) - 🆕 HR・CRM・ATS プラットフォーム横断の統一 API。
- [The Colony](https://thecolony.cc) - ⚠️ **Unverified**。エージェント間のソーシャルネットワークと REST API を謳う。組織と SDK リポジトリは <30 日、すべて 0~2 star、単独メンテナで、同じ申請が 15+ awesome リストに並列投稿された —— 可視性のための掲載のみ、利用前に評価のこと。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTheColonyCC%2Fcolony-sdk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [dependency-freshness-mcp](https://github.com/Armigerous/dependency-freshness-mcp) - 🆕 ⚠️ **Unverified**。AI コーディングエージェントに引用付きの npm・PyPI 依存鮮度情報（最新バージョン、リリース日、非推奨、日付付きの破壊的変更差分）を提供し、学習データのカットオフによる盲点を埋める。リモート（Apify Standby HTTP）+ ローカル stdio。新規・単独メンテナのリポジトリ（2026-06-08 作成、掲載時 0 star）—— 可視性のための掲載のみ、利用前に評価のこと。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FArmigerous%2Fdependency-freshness-mcp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [NotFair](https://github.com/nowork-studio/NotFair) - オープンソースの Claude Code エージェントスキル集。[SEO](https://github.com/nowork-studio/NotFair/tree/main/seo)、[Google Ads](https://github.com/nowork-studio/NotFair/tree/main/google-ads)、[Meta Ads](https://github.com/nowork-studio/NotFair/tree/main/meta-ads) に対応。Google Ads MCP、Meta Ads MCP、Google Search Console MCP、Google Analytics (GA4) MCP を介してリアルタイムのキャンペーンと分析データに接続。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fnowork-studio%2FNotFair&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [mcp-agent](https://github.com/lastmile-ai/mcp-agent) - 🆕 MCP をコア通信プリミティブに据えたオープンソース Python フレームワーク。MCP ツールエコシステムとネイティブに相互運用できるエージェントを構築。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flastmile-ai%2Fmcp-agent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AWS MCP Server](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/) - 🆕 **2026 年 5 月 6 日 GA**。AWS マネージドの MCP サーバ。コーディングエージェントが任意の AWS API を安全かつ監査可能に呼び出せるようにし、複数ステップ操作はサンドボックス Python で実行。従来の "agent SOP" を agent skills で置き換え。AWS 純正。
- [Google Workspace MCP Server](https://workspaceupdates.googleblog.com/2026/05/agent-tools-and-security-updates-for-workspace-developers.html) - 🆕 **2026 年 5 月 1 日、パブリック開発者プレビュー**。Workspace ネイティブの MCP サーバ。Gmail / Drive / Calendar / Chat / People を MCP クライアントに公開し、OAuth スコープは管理者が制御、監査ログ付き。
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
- [Google Antigravity Sandbox](https://antigravity.google/changelog) - 🆕 **2026 年 5 月（Google I/O）**。エージェントが実行するコード用のサンドボックス化 Linux 環境。Antigravity 2.0 のスタックの一部として提供 — サブエージェントはそれぞれ、ファイルシステム + ネットワークアクセスをスコープ制限された隔離コンテナで動作。

---

## 🛡️ エージェントセキュリティ

*プロンプトインジェクション・データ漏洩・悪用から AI エージェントを守るツールとフレームワーク。*

- [AgentGate](https://github.com/ElamOlame31/agentgate-public) - 🆕 ⚠️ **Unverified**（初期段階・単独メンテナ）。自律 AI エージェント向けの実行前認可 PDP。リクエストごとに 4 次元で信頼スコアを算出し、24時間のキルチェーンパターンを検知し、Merkle チェーンの監査ログを保持。MIT ライセンスで LangGraph、LangChain、AutoGen にドロップイン対応。[tryagentgate.com](https://www.tryagentgate.com/) ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FElamOlame31%2Fagentgate-public&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [prompt-firewall](https://github.com/Zijian-Ni/prompt-firewall) - ⚠️ **Unverified**（初期段階）。LLM プロンプト用ファイアウォール —— インジェクション攻撃を検出・遮断。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fprompt-firewall&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LLM Guard](https://github.com/protectai/llm-guard) - LLM 対話用のセキュリティツールキット —— 入出力スキャナ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fprotectai%2Fllm-guard&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Rebuff](https://github.com/protectai/rebuff) - 📦 **Archived**（2025-05）。自己強化型プロンプトインジェクション検出器。歴史的参照のみ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fprotectai%2Frebuff&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
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
- [PyRIT](https://github.com/microsoft/PyRIT) - Microsoft の生成 AI 用自動レッドチームフレームワーク（2026 年 3 月に Azure/PyRIT から移転；活発に保守中）。下記 RAMPART を補完。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2FPyRIT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAMPART](https://github.com/microsoft/RAMPART) - 🆕 **2026 年 5 月 20 日**。Microsoft が公開した、agentic AI 向けの pytest ネイティブな安全性 / セキュリティテストフレームワーク。PyRIT と相補的な開発者向けホワイトボックス——クロスプロンプトインジェクションのプローブ、良性失敗アサーション、ハームカテゴリ網羅、統計しきい値（例：80%+ の試行で安全）。CI/CD に直接組み込める。MIT。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2FRAMPART&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Clarity (Microsoft)](https://www.microsoft.com/en-us/security/blog/2026/05/20/introducing-rampart-and-clarity-open-source-tools-to-bring-safety-into-agent-development-workflow/) - 🆕 **2026 年 5 月 20 日**。RAMPART の姉妹ツール。AI エージェントの構造化デザインレビューを支援し、コード着手前に意図・リスク・挙動の "living artifact" を生成。Microsoft AI Red Team の社内プラクティスをオープンソース化。
- [MCP Gateway & Registry](https://github.com/agentic-community/mcp-gateway-registry) - 🆕 エンタープライズ対応の MCP ゲートウェイ＆レジストリ。OAuth 認証、動的ツール発見、監査トレイル、Keycloak / Entra との統合で AI 開発ツールを集中管理。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentic-community%2Fmcp-gateway-registry&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Nobulex](https://github.com/arian-gogani/nobulex) - ⚠️ **未検証。** AI エージェント挙動の暗号学的レシート（Ed25519 二重署名、ハッシュチェーン監査ログ）。MIT。双方向レシートのプリミティブが Microsoft Agent Governance Toolkit に [マージ済み](https://github.com/microsoft/agent-governance-toolkit/pull/1333)（PR #1302、#1333）。同一の投稿が 15+ の awesome list に同時送付され、投稿者の "npm 月 4,500 ダウンロード" の主張は registry 実数（`@nobulex/mcp-server` ≒ 月 19）と乖離。Microsoft 採用実績を踏まえて可視性のために掲載するが、依存する前に各自で評価のこと。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Farian-gogani%2Fnobulex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ActPlane](https://github.com/eunomia-bpf/ActPlane) - 🧪 YAML で定義した行動契約を eBPF によりシステムコール境界で強制する OS レベルのエージェントハーネス — 任意のツール・サブプロセス・直接システムコールに対して制約が一貫して適用され、違反時はエージェントに修正フィードバック。MIT。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Feunomia-bpf%2FActPlane&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsoft Prompt Shields](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection) - ジェイルブレイクと、エージェントが取り込む文書 / Web ページに隠された間接プロンプトインジェクションを検知する Azure AI Content Safety の機能（2024 年 GA；その後エージェントワークロード向けに拡張）。Azure OpenAI Service やサードパーティモデルと連携。
- [Agent Name Service (ANS)](https://www.ciodive.com/news/linux-foundation-prepares-open-standard-ai-agent-verification/823691/) - 🆕 **2026年6月**。Linux Foundation による AI エージェント検証・信頼アイデンティティのオープン標準化取り組み。分散型エージェント名前レジストリにより、相手が正規のエージェントかを検証でき、なりすまし・中間者攻撃を緩和。
- [OpenAI Daybreak](https://openai.com/index/daybreak-securing-the-world/) - 🆕 **2026年6月**。AI 関連コードの自動脆弱性発見・修復のための OpenAI の取り組みと刷新版 Codex Security プラグイン。エージェントアプリ向けのプロンプトインジェクション対策も含む。
- [Lineation.ai](https://lineation.ai) - 🆕 ⚠️ **2026 年 7 月**（新規ベンダー）。エージェントのアカウンタビリティレイヤー — フォレンジックな推論リネージを備えた可観測性・ガバナンス・防御。目標乗っ取り・メモリ汚染・ツール不正利用の防止を狙い、SOC 2 / HIPAA / EU AI Act 対応の監査証跡を提供。クラウド（無料スタート）とオンプレ両対応。
- [First Recon AI セキュリティランタイム](https://firstrecon.ai) - 🆕 **2026 年 7 月**。企業 AI ガバナンスプラットフォーム。すべての AI インタラクション（人間-モデル / エージェント-ツール / エージェント-エージェント）を独自のセマンティックセキュリティエンジンで検査し、データがモデルに届く前にポリシーを適用して完全な意思決定監査ログを記録。macOS + Windows エンドポイントエージェント付き。
- [CrowdStrike Falcon AIDR](https://www.crowdstrike.com/en-us/platform/falcon-aidr-ai-detection-and-response/) - **2025 年 12 月 GA**。AI Detection and Response — 企業全体の従業員 AI 利用とエージェント活動の可視化、リスクスコアリング、行動異常検知、プロンプトインジェクション遮断、AI インタラクション層でのリアルタイムポリシー強制。
- [Exabeam Agent Behavior Analytics](https://www.exabeam.com/) - 🆕 **2026 年**。Exabeam の行動インテリジェンスプラットフォームをエージェント AI のリスクに拡張 — 静的なガードレールに代わる、verify-observe-analyze-improve の継続ループ。
- [JADEPUFFER（Sysdig による開示）](https://hackread.com/sysdig-jadepuffer-first-agentic-ransomware-operation/) - 🆕 ⚠️ **脅威——ツールではない。 2026年7月2日**。Sysdig が、AI エージェントが始終を一貫してオーケストレーションした初のランサムウェア作戦を公開。LLM 駆動のエージェントが Langflow の RCE 脆弱性（CVE-2025-3248）を悪用して侵入し、認証情報を取得して本番の MySQL/Nacos サーバーに横展開し、31秒で失敗ステップを自己修正した後、保存されなかった一回限りの AES 鍵で1,342件の設定を暗号化し、身代金を支払っても復旧不可能な状態にした。ペイロードには自然言語の推論コメントが付されており、LLM による生成を強く示唆。上記のエージェントセキュリティツール（ガードレール・エグレス制御・認証スコープ制限）が本番でなぜ必要かを示す参照事例として掲載。
- [WalletPrint](https://github.com/Loai17/walletprint-sdk) - ⚠️ **Unverified**（初期段階）。エージェントウォレットの行動リスクスコアリング SDK。トランザクション署名前にウォレットの履歴から異常をフラグ付け。ZeroDev と LangChain の統合をサポート。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FLoai17%2Fwalletprint-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Alchemy & Visa AgentCard](https://www.coindesk.com/business/2026/06/18/alchemy-s-ai-driven-identity-and-payment-service-gains-access-to-visa-network) - 🆕 **2026-06-18**。**Visa Intelligent Commerce** 上に構築された AI エージェント向けの決済 + アイデンティティスタック。1 つの API でエージェントが取引に必要なすべて——Visa 決済トークン、専用のメールアドレスと電話番号、暗号ウォレット——をプロビジョニングし、スコープ制御の下でユーザーに代わって購入できる。既定では Visa トークンを使用し、暗号資産、x402、Stripe の Machine Payments Protocol にも対応。モデル非依存（OpenAI / Anthropic など）。

---

## 🔍 RAG とナレッジ

*エージェント用の検索拡張生成と知識管理システム。*

- [Oracle OCI Enterprise AI updates](https://blogs.oracle.com/ai-and-datascience/whats-new-in-ai-june-2026) - 🆕 **2026-06**。RAG およびエンタープライズのエージェント型検索を強化する Cohere Rerank 4 の展開に加え、Alibaba や Google の新モデルへのサポートを拡大。
- [LlamaIndex](https://github.com/run-llama/llama_index) - LLM アプリ用データフレームワーク —— プライベートデータの取り込み・構造化・アクセス。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Frun-llama%2Fllama_index&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangChain Retrievers](https://github.com/langchain-ai/langchain) - LangChain 内のリトリーバとドキュメントローダー集合。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Haystack](https://github.com/deepset-ai/haystack) - エンドツーエンド RAG。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeepset-ai%2Fhaystack&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Unstructured](https://github.com/Unstructured-IO/unstructured) - ドキュメント前処理と抽出。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FUnstructured-IO%2Funstructured&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Weaviate](https://github.com/weaviate/weaviate) - オープンソースベクトルデータベース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fweaviate%2Fweaviate&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Qdrant](https://github.com/qdrant/qdrant) - Rust 製の高性能ベクトル検索。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fqdrant%2Fqdrant&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Milvus](https://github.com/milvus-io/milvus) - 大規模ベクトルデータベース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmilvus-io%2Fmilvus&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Pinecone](https://www.pinecone.io/) - マネージドベクトルデータベース SaaS。
- [Chroma](https://github.com/chroma-core/chroma) - AI ネイティブオープンソースベクトルデータベース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fchroma-core%2Fchroma&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vanna](https://github.com/vanna-ai/vanna) - 📦 **Archived**（2026-03）。RAG-for-SQL: 自然言語でデータベースと対話。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvanna-ai%2Fvanna&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LightRAG](https://github.com/HKUDS/LightRAG) - 🇨🇳 香港大学 HKUDS のグラフ型 RAG。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2FLightRAG&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Docling](https://github.com/docling-project/docling) - IBM のドキュメント変換ツール（PDF / DOCX / HTML 等）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdocling-project%2Fdocling&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Kotaemon](https://github.com/Cinnamon/kotaemon) - オープンソース RAG UI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FCinnamon%2Fkotaemon&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [R2R](https://github.com/SciPhi-AI/R2R) - エンタープライズグレードのエンドツーエンド RAG サービス。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSciPhi-AI%2FR2R&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAGFlow](https://github.com/infiniflow/ragflow) - 🇨🇳 深いドキュメント理解 RAG。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Finfiniflow%2Fragflow&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Morphik](https://github.com/morphik-org/morphik-core) - 🆕 表や図を含む文書向けのマルチモーダル RAG エンジン。複雑な PDF 処理の LlamaIndex 代替として 2026 年に急浮上。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmorphik-org%2Fmorphik-core&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cognee](https://github.com/topoteretes/cognee) - 🆕 エージェントが文書を取り込む過程でナレッジグラフを構築するメモリ + 推論エンジン。2026 年の "長期リサーチエージェント" 系スタックの定番。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftopoteretes%2Fcognee&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAG-Anything](https://github.com/HKUDS/RAG-Anything) - 🆕 香港大学データサイエンス研究室のオールインワン・マルチモーダル RAG フレームワーク。LightRAG を基盤に構築。テキストとマルチモーダルの並列パイプライン；テキスト・図・表・数式が混在する文書も検索可能。MIT、21K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2FRAG-Anything&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [A-MEM](https://github.com/WujiangXu/A-mem-sys) - 🆕 LLM エージェント向け Agentic Memory システム——Zettelkasten 流のノートリンクで記憶を動的に組織化し、静的ベクトルストアより柔軟な検索を実現。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FWujiangXu%2FA-mem-sys&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 💻 コーディングエージェント

### ターミナル / CLI エージェント

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - 端末で動く Anthropic のエージェント型コーディングツール。Opus 4.7 + `/think xhigh`。SWE-bench 80.9%。
- [Codex CLI](https://github.com/openai/codex) - OpenAI 製のオープンソースターミナルコーディングエージェント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fcodex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Codex Security](https://developers.openai.com/codex/changelog) - 🆕 **2026 年 3 月**。ソフトウェア脆弱性を発見・修正するアプリケーションセキュリティエージェント。OSS メンテナは Codex-for-OSS プログラム経由で利用可能。
- [Aider](https://github.com/Aider-AI/aider) - 💤 Git アウェアなターミナル AI ペアプログラミングパートナー。最終リリース 2025-08。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAider-AI%2Faider&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Goose](https://github.com/block/goose) - Block 製のオープンソースエージェントコーディング CLI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fblock%2Fgoose&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) - 🆕 Google のターミナル特化コーディングエージェント。大規模コンテキストのリファクタが得意。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle-gemini%2Fgemini-cli&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenCode](https://github.com/anomalyco/opencode) - オープンソースのターミナル AI コーディングエージェント（opencode.ai、180K+ stars）— build / plan エージェント、LSP、MCP、ベータ版デスクトップアプリ。アーカイブ済みの opencode-ai/opencode とは無関係。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fanomalyco%2Fopencode&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Crush](https://github.com/charmbracelet/crush) - Charm 製のターミナル AI コーディングエージェント — アーカイブ済み opencode-ai/opencode の後継；マルチモデル、LSP + MCP 対応。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcharmbracelet%2Fcrush&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Grok Build](https://x.ai/news/grok-build-cli) - 🆕 **2026 年 5 月 25 日（early beta）**。xAI が出した **grok-code-fast-1** ベースの agentic CLI コーディングエージェント。サブエージェントが隔離環境で並列実行、毎日リリースノートを公開；SuperGrok と X Premium Plus 契約者向け。xAI による Claude Code / Codex CLI への正面回答。⚠️ 2026 年 7 月の報告で、Grok Build が git リポジトリ全体を xAI ストレージにアップロードしていることが判明 — プライベートコードでの利用前に要確認。
- [Antigravity CLI](https://antigravity.google/blog/introducing-google-antigravity-2-0) - 🆕 **2026 年 5 月 19 日（Google I/O 2026）**。Antigravity 2.0 の軽量 CLI コンパニオン。ターミナルから直接 Google のエージェント harness を起動・操作できる。macOS / Linux / Windows。ホステッドプランのユーザーには 2026 年 6 月 18 日から Gemini CLI を置き換えると報じられる（オープンソースの gemini-cli リポジトリは 105K+ stars で活発なまま）。
- [Microsoft physical-ai-toolchain](https://github.com/microsoft/physical-ai-toolchain) - 🆕 **2026 年 6 月**。Microsoft Azure クラウドと NVIDIA のフィジカル AI スタックを統合した本番対応オープンソースツールチェーン——自律移動ロボット/マニピュレータのデータキュレーション・学習・デプロイをエージェンティックに。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fphysical-ai-toolchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [PhyAgentOS](https://github.com/PhyAgentOS/PhyAgentOS) - 🆕 エージェンティックワークフローに基づく自己進化型の身体性 AI OS。認知機能をハードウェアから分離し、監査可能性を組み込んだクロスプラットフォームのロボット展開を実現。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FPhyAgentOS%2FPhyAgentOS&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code) - 🆕 🇨🇳 **2026 年 6 月 6 日**。Moonshot AI の TypeScript / MIT 製ターミナルコーディングエージェント。隔離コンテキストで動く coder / explore / plan サブエージェントを内蔵し、`/mcp-config` で対話式に MCP を設定。npm インストール対応。次世代 Kimi K2.6 エージェント向け設計。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FMoonshotAI%2Fkimi-code&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MAI-Code-1-Flash in GitHub Copilot](https://microsoft.ai/news/introducingmai-code-1-flash/) - 🆕 **Build 2026（2026 年 6 月 2 日）**。Microsoft 初の完全自社開発 5B コーディングモデルが GitHub Copilot のモデル選択肢として登場 —— 4 つの主要コーディングベンチで Claude Haiku 4.5 を上回り（SWE-Bench Pro 51.2% vs 35.2%）、コストも大幅に低減。
- [Claude Agent SDK](https://docs.anthropic.com/en/docs/claude-code/sdk) - Claude Code ハーネス上にエージェントを構築する SDK（2025 年 9 月末に Claude Code SDK からリブランド）。**2026 年 6 月**の Claude Code リリースで、階層的サブエージェント生成、Dynamic Workflows（数十〜数百の並列サブエージェントをファンアウト）、ルーブリック駆動の Outcomes、フォールバックモデルチェーンを追加 — 最大 1,000 サブエージェントの "ultracode" モードを実現。Python + TypeScript。
- [ai-delivery-spec](https://github.com/franklinxkk/ai-delivery-spec) - 🆕 ⚠️ **未検証。** AI コーディングエージェント（Claude Code、OpenClaw、Codex、Cursor、Copilot）と協働する PM 向けのスペック駆動デリバリーフレームワーク。4 段階の納品ティア、0D トリアージ、プロトタイプ検証ルール、AI ランタイムガバナンス、5 つのドメインモジュール。SKILL.md 規約；ClawHub でホスト。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ffranklinxkk%2Fai-delivery-spec&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Ralph Harness](https://github.com/rxdt/py_ralph_frame) - 🆕 ⚠️ **未検証。** ガード付き Claude Code/Codex/Gemini ループ用の小さな Python スキャフォールド：リポジトリ内スペック、フレッシュコンテキスト反復、git フックゲート、CI 検証、カバレッジゲート。`uvx ralph-harness demo` で導入可。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Frxdt%2Fpy_ralph_frame&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### IDE エージェント

- [Cursor 3.11](https://cursor.com/changelog) - 🆕 **2026-07-10**。サイドチャット（メインワークフローを妨げない並列 AI 会話）、会話履歴検索、再設計されたプロジェクト / リポジトリピッカー、新しい Cloud Agent Hooks（プロンプト・応答・サブエージェント活動などエージェント会話へのきめ細かな制御と可観測性）。
- [Cursor 3.4（Teams + PR レビュー）](https://cursor.com/changelog) - 🆕 **2026-05-11~13**。Microsoft Teams 統合（Teams 内で `@Cursor` するとクラウドエージェントに委任）、並列エージェントのプラン実行高速化、マルチリポジトリ / Dockerfile ベースのエージェント開発環境設定、`/multitask` 非同期サブエージェント、脆弱性スキャナー、モデル単位のきめ細かなアクセス制御。
- [Cursor 3.3](https://cursor.com/changelog) - 🆕 **2026-05**。PR レビュー体験、並列エージェント、エンタープライズ向けモデル管理。前バージョン 3.1 は 4 月リリース。
- [Cursor SDK](https://cursor.com/blog/typescript-sdk) - 🆕 **2026-04-29**（パブリックベータ）。Cursor のランタイム・ハーネス・モデルを公開する TypeScript SDK で、Cursor スタック上にプログラマブルなエージェントを構築可能 — サンドボックス化されたクラウド VM、サブエージェント、hooks、トークンベース課金。
- [Kilo Code](https://kilo.ai/) - オープンソースの AI コーディング拡張（VS Code / JetBrains）。500+ モデルを横断する Auto Model ルーティング搭載；Anaconda が買収（2026 年）。MiniMax モデルを広く採用。
- [Cursor](https://www.cursor.com/) - 2026-02 アップデートで 8 並列エージェント対応。
- [Windsurf → Devin Desktop](https://devin.ai/blog/windsurf-is-now-devin-desktop/) - 🆕 **2026年6月2日に改称**。Cognition が Windsurf IDE を **Devin Desktop** に改称（windsurf.com は devin.ai にリダイレクト）：**Devin Local**（Rust で書き直し、トークン効率を約 30% 改善、サブエージェント対応）が Cascade を置き換え、**Agent Command Center** のカンバンがデフォルト画面となり、オープンな **Agent Client Protocol (ACP)** に対応。Cascade は 2026年7月1日にサポート終了。
- [Cline](https://github.com/cline/cline) - VS Code で動く自律コーディングエージェント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcline%2Fcline&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Continue](https://github.com/continuedev/continue) - VS Code・JetBrains 対応のオープンソース AI コードアシスタント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcontinuedev%2Fcontinue&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Roo Code → Roomote](https://roomote.dev/) - ⚠️ **IDE 拡張としては提供終了。** Roo Code は VS Code 拡張・Cloud・Router を 2026 年 5 月 15 日に終了すると発表（2026-04-22）し、クラウドコーディングエージェント **Roomote**（Slack/GitHub/Linear → PR）へ転換；roocode.com は現在 roomote.dev にリダイレクト。
- [Void](https://github.com/voideditor/void) - 💤 **休止中**（アーカイブではない — メンテナは新しいコーディングアイデアを模索中；活発な保守なし）。VS Code のオープンソース fork。"オープンソース版 Cursor" として位置付けられていた。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvoideditor%2Fvoid&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [GitHub Copilot](https://github.com/features/copilot) - 2026 年初頭よりエージェントモードと `gh copilot` シェル統合。
- [Kiro](https://kiro.dev/) - AWS の自律エージェント。スペック駆動開発、最大 10 タスクを同時管理。
- [Amazon Q Developer](https://aws.amazon.com/q/developer/) - AWS エコシステムと深く統合された AI コーディングコンパニオン。
- [Visual Studio 2026 Agent Mode + Skills](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/) - 🆕 **VS 2026 Insiders 2026-05-12～15**。Copilot Chat「Agent Mode」が Visual Studio 2026 内で再利用可能な Copilot Skill を探し・管理・作成できるようになり、ソリューション全体のコンテキストを見つつ、端末コマンド実行や外部ツール呼び出しもサポート。
- [JetBrains Rider AI Test-Writing Skill](https://blog.jetbrains.com/dotnet/2026/05/22/claude-codex-ai-agent-skill-for-writing-tests/) - 🆕 **2026 年 5 月 22 日**。JetBrains Rider に追加された AI Assistant skill。.NET のコードカバレッジ情報を Claude Code / Codex に渡し、未カバー分岐に絞ってテスト生成させることで AI コストを削減。

### 自律ソフトウェアエンジニア

- [Cursor 3.4 Cloud Agent Environments](https://cursor.com/changelog) - 🆕 **2026-05-13**。クラウドエージェント / 自動化向けの新しい開発環境。マルチリポ、build secrets 付き Dockerfile 設定、キャッシュレイヤー 70% 高速化、環境ごとのバージョン履歴とロールバック、監査ログ、スコープを限定した egress / secrets。
- [Devin Security Swarm](https://cognition.com/blog) - 🆕 **2026-07-01**。Cognition の並列エージェント型セキュリティ製品：コードベース全体の脆弱性を発見し、実行時に悪用可能性を検証し、修正 PR を作成；実世界の脆弱性 50 件中 36 件を発見、発見あたりコストは次点ツールより約 30% 低い。
- [Devin 2.2](https://cognition.com/blog/introducing-devin-2-2) - 🆕 **2026-02-24**。Computer Use によるエンドツーエンドテスト（Linux デスクトップ + 画面録画）、PR 前のセルフレビュー / 自動修正、起動 3 倍高速化。Cognition のフラッグシップ自律ソフトウェアエンジニア（Devin 2.x 系；Devin 2.0 以降 Core プランは月 20 ドルから）。
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) - 自律エージェントとして AI ソフトウェア開発者を使うオープンソースプラットフォーム。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAll-Hands-AI%2FOpenHands&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SWE-agent](https://github.com/SWE-agent/SWE-agent) - LLM を GitHub Issue を修正するソフトウェアエージェントに変える。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSWE-agent%2FSWE-agent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Devika](https://github.com/stitionai/devika) - 💤 **Stale**（2025-09 以降更新なし）。エージェント型 AI ソフトウェアエンジニア、Devin のオープンソース代替。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstitionai%2Fdevika&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [GPT Engineer](https://github.com/gpt-engineer-org/gpt-engineer) - 📦 **Archived**（2026-04）。何を作るか指定すると AI が質問して作成。自律コーディング時代初期の基礎、歴史的参照として維持。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgpt-engineer-org%2Fgpt-engineer&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Codegen](https://github.com/codegen-sh/codegen) - 💤 プログラム的なコード操作とマルチファイルリファクタリング SDK（最終リリース 2025-09）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcodegen-sh%2Fcodegen&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Qodo](https://www.qodo.ai/) - 🆕 品質・セキュリティ・テスト生成に特化した AI コードレビュープラットフォーム。
- [Google Antigravity 2.0](https://antigravity.google/blog/introducing-google-antigravity-2-0) - 🆕 **2026 年 5 月 19 日（Google I/O 2026）**。複数エージェントを並列編成できるスタンドアロン・デスクトップアプリ（macOS / Linux / Windows）。cron 形式のスケジュール実行、長時間の非同期タスク、動的サブエージェント、AI Studio / Android / Firebase との統合を追加。コンパニオンの **Antigravity SDK** は harness の自前ホストを可能にし、エンタープライズ版は Gemini Enterprise Agent Platform 内に組み込まれる。

---

## 🤖 Physical AI / 身体性エージェント

*物理世界を知覚し推論し行動する AI —— ヒューマノイドロボット、工場自動化、Physical AI インフラ。言語エージェントの次の波。*

### 基盤モデルと研究
- [ENPIRE](https://research.nvidia.com/labs/gear/enpire/) - 🆕 **2026-06**。NVIDIA / CMU / UC Berkeley による、AI エージェントが自らロボティクス研究を実施できるフレームワーク — 双腕ロボットの管理、アルゴリズムの改変、ポリシーの訓練を人手を介さずに行う。
- [Kairos](https://futureiot.tech/kairos-model-breaks-new-ground-for-open-source-embodied-intelligence/) - 🆕 **2026-06-15**。ACE ROBOTICS が Kairos ワールドモデルをオープンソース化 — RoboTwin 2.0、LIBERO-Plus、WorldModelBench Robot、DreamGen で VLA システムを制した初のワールドモデルアプローチ；ウェイトは GitHub / Hugging Face / ModelScope で公開。
- [NVIDIA Cosmos 3](https://www.axios.com/2026/06/08/ai-news-nvidia-cosmos-3-openai-sites-solara-rtx-spark) - 🆕 **2026-06**。単なるテキストではなく、物理法則と空間幾何学に基づいて学習された物理 AI 向け基盤モデル。ロボット工学や工場自動化をターゲットとする。

- [Google Gemini Robotics-ER 1.6](https://deepmind.google/blog/gemini-robotics-er-1-6/) - 🆕 2026-04-14。空間・身体性推論を強化したロボティクス AI モデル（アナログ計器の読み取りを含む）。Gemini API 経由で利用可能。
- [Project Prometheus (Bezos)](https://techcrunch.com/2026/06/11/jeff-bezoss-prometheus-raises-12b-to-build-an-artificial-general-engineer-for-the-physical-world/) - 🆕 💰 **2026-06-11**。ジェフ・ベゾスが共同主導する Physical AI ベンチャー。物理世界のための「artificial general engineer」構築に向け、評価額 $41B で $12B を調達。
- [NVIDIA Isaac GR00T](https://developer.nvidia.com/isaac/gr00t) - NVIDIA のヒューマノイドロボット用基盤モデルプラットフォーム。GTC で発表、Hannover Messe 2026 で拡充。
- [NVIDIA Industrial AI Cloud](https://nvidianews.nvidia.com/) - 🆕 2026-04（Hannover Messe）。ドイツテレコムと共同構築した産業 AI ワークロード用 AI 工場。

### ヒューマノイドロボット

- [Tesla Optimus Gen3](https://www.tesla.com/) - 🆕 2026 年夏量産。汎用タスク向けの高度ヒューマノイド。
- [Figure 04](https://autonews.gasgoo.com/articles/news/figure-founder-f04-robot-initiates-component-delivery-process-2054560059634376705) - 🆕 **2026-05-13**。CEO の Brett Adcock が Figure 04 の設計確定と部品出荷開始を表明。F.03 の後継、Helix VLA モデルを搭載。
- [Helix 02 パッケージ仕分け 72h 連続運転](https://oodaloop.com/briefs/technology/figure-ais-humanoid-robots-sort-88000-packages-in-72-hours-during-nonstop-livestream/) - 🆕 **2026-05-13～16**。Figure F.03 フリートが Helix 02 でパッケージ仕分けラインを完全自律で運転 —— 初日に ~22K 個、最初の 24 時間で ~30K 個、ストレステストでは機械故障まで約 72 時間で ~88K 個を処理。初めて公開された家庭型ヒューマノイドの長時間稼働データ。
- [Figure F.03 対 人間 8 時間仕分けチャレンジ](https://incrypted.com/en/figure-ai-held-a-human-vs-robot-marathon/) - 🆕 **2026-05-18**。Figure 初の公開人間 vs ロボット対決。同じライン上で 8 時間、人間社員が 12,924 個（2.79 秒 / 個）と F.03 の 12,732 個（2.83 秒 / 個）をわずかに上回り勝利。実業務で公開されたうち人間に最も迫ったスループット。
- [Boston Dynamics Atlas 100ポンド操作 + Hyundai 25K 台計画](https://www.techtimes.com/articles/316854/20260519/boston-dynamics-reveals-how-atlas-learned-lift-100-pound-loads-hyundai-plans-30000-per-year.htm) - 🆕 **2026-05-18 / 19**。Boston Dynamics が Atlas が強化学習 + 大規模シミュレーションで **100 ポンド超**の荷重（冷蔵庫 / 洗濯機）を持ち上げて運ぶ動画と技術ブログを公開。Hyundai Motor Group は 2028 年ジョージアのアセンブリエ工場を手始めに、Hyundai/Kia 工場へ **25,000+ 台の Atlas** を配備する計画を発表。
- [Hyundai が Boston Dynamics を完全買収](https://www.techtimes.com/articles/320483/20260714/boston-dynamics-now-fully-hyundais-atlas-exits-world-cup-eyes-factory-floor.htm) - 🆕 💰 **2026 年 6 月末**。Hyundai Motor Group が SoftBank の残り 9.65% の持分を $325M で買い取り、評価額約 $3.4B で 100% 所有に。新型第 5 世代 Atlas は FIFA ワールドカップ（2026-07-05）で一般公開；外部顧客への商用提供は 2027 年、ジョージア Metaplant への配備は 2028 年を予定。
- [Unitree G1 を JAL 羽田に導入](https://www.techtimes.com/articles/316862/20260519/jal-deploys-unitree-g1-robots-haneda-us-congress-moves-blacklist-supplier-national-security.htm) - 🆕 **2026-05**。日本航空が羽田の地上業務（获物積み込み / コンテナ輸送 / 機内清掝）で Unitree G1 ヒューマノイドの実証を開始し、**隊位性を保つロボットを現役投入する世界初の商用航空例**としてアピール。同週、米連邦議会は Unitree をエンティティリストに加える動きを見せ、embodied AI サプライチェーンのジオポリティクス化が進む。
- [Honor (荣耀) Humanoid](https://www.npr.org/2026/04/20/g-s1-118086/humanoid-robot-half-marathon) - 🆕 **2026-04-19**。北京亦荘（E-Town）のヒューマノイドハーフマラソンで 50 分 26 秒で優勝 — この距離の人間の世界記録を上回った。
- [Zhiyuan (智元) AGIBOT](https://www.agibot.com/article/231/detail/62.html) - 🆕 🇨🇳 **2026-04-17（APC 2026）**。2026 年を「Deployment Year One」と宣言；10,000 台目のロボットを配備、7 つの業界ソリューション、オープンソースの AIMA アーキテクチャ（Link-U OS、Genie Studio）。
- [Unitree H シリーズ](https://www.unitree.com/) - 🇨🇳 Boston Dynamics の中国競争相手。
- [Agile Robots](https://www.agile-robots.com/) - AI 駆動の産業マニピュレーションシステムを構築する独中系ロボティクス企業。
- [Shenzhen Humanoid Pilot Line](https://www.chinadailyhk.com/hk/article/631892) - 🇨🇳 🆕 深圳が **2026-04-12** にヒューマノイドロボット初のパイロット生産ラインを稼働（乐聚 Robotics + 東方精工、龍華區）。2 時間で組み立て、年 500～1,000 台。佛山の年 1 万台工場へ量産移行予定。

### 消費者向けロボティクス・ウェアラブル

- [Doubao AI Glasses (ByteDance)](https://technode.com/2026/03/18/bytedance-reportedly-delays-doubao-ai-glasses-launch-plan/) - ⚠️ 🇨🇳 第 1 世代は「汎用的すぎる」としてローンチ前に廃案と報道；AI グラス市場が前年比約 130% 成長する中、ByteDance はデュアルモデルの第 2 世代（2026 年 7 月）を急ピッチで開発中。
- [Nothing AI Glasses/Earbuds](https://techcrunch.com/2026/04/01/nothings-ai-devices-plan-reportedly-contains-smart-glasses-and-earbuds/) - 🧪 2026 年 3 月の報道：Nothing は AI スマートグラス + イヤホンを計画、2027 年ローンチ目標。
- [Samsung Galaxy S26 (Gauss 2.3)](https://www.samsung.com/) - オンデバイスのエージェント AI。Gauss 2.3 Think と Gauss O Flash。
- [Meta Ray-Ban Display / Ray-Ban Meta](https://www.meta.com/ai-glasses/) - Meta の出荷中 AI グラスライン（Neural Band 付き Display モデルを含む）；Ray-Ban Meta 第 3 世代は 2026 年後半と噂される。

### 自動運転

- [Tesla FSD v14](https://www.tesla.com/) - v14.3.x が展開中（2026 年 7 月）、レガシー HW3 車向けの v14 "Lite" を含む；無監督運転は依然としてロボタクシープログラム限定。
- [Waymo](https://waymo.com/) - 2026 年を通じて米国都市で商用 L4 を展開中。
- [WeRide / Pony.ai / Baidu Apollo](https://www.weride.ai/) - 🇨🇳 中国 L4 車両集団が運行区域を拡大。
- [Tesla Optimus Gen3 (V3)](https://www.teslarati.com/tesla-optimus-awe-2026-shanghai/) - 🆕 **AWE 2026 上海でお披露目**。初の量産 Optimus。Fremont ラインが 2026 年 1 月に稼働、初期目標は年 5〜10 万台、初期価格は約 3 万ドル、2026 年後半に小規模な外販を予定。37 関節、歩行速度 1.2 m/s、22 自由度のハンド。
- [Figure 03 (Helix AI)](https://blog.robozaps.com/b/figure-03-review) - 🆕 **2025 年末発表、2026 年に量産立ち上げ**。Figure 初の家庭用設計：柔らかいテキスタイル外装、ワイヤレス充電、触覚センサー。2026 年 5 月のデモでは、F.03 が 2 台で視覚協調のみによって 2 分以内に部屋掃除とベッドメイクを自律実行。
- [Figure 02 + Helix 02](https://en.wikipedia.org/wiki/Figure_AI) - 🆕 **2026 年 1 月**。Helix 02 で全身自律性が拡張（食洗機の出し入れ、洗濯物たたみ）。BotQ 工場は年 1.2 万台の生産能力。
- [Unitree G1 + H2](https://community.robotshop.com/blog/show/unitree-robotics-at-ces-2026-a-clear-signal-of-whats-coming-next) - 🆕 **CES 2026**。G1 のダンス / ボクシング / スケートのデモ、2 月には自律カンフー演武、そして 31+ 自由度のヒューマノイド H2。
- [Unitree R1 Air](https://humanoid.guide/unitrees-4900-r1-air-pushes-humanoids-toward-mass-market/) - 🆕 価格 **4,900 ドル** のコンシューマー人型ロボット。走行、バックフリップ、手歩きまでこなす。
- [Unitree Gen 2 (lifelike skin)](https://www.youtube.com/watch?v=Gmp82MuTFsM) - 🆕 圧力 / 温度 / 触覚センサーを埋め込んだ、人肌に近い外皮を採用。
- [Unitree GD01](https://www.extremetech.com/computing/unitree-will-sell-you-a-personal-mecha-robot-for-650000) - 🆕 **2026 年 5 月**。約 10 フィートの有人メカ。パイロット操縦で二足歩行と四足歩行を切り替え可能。価格は人民元 390 万元〜（約 65 万ドル）。身体性エージェントの形態が操縦型にも分岐し始めた証左。
- [1X NEO（コンシューマー型ヒューマノイド）](https://www.1x.tech/discover/neo-home-robot) - 🆕 **2025 年 10 月 28 日に予約開始**、米国家庭への初回配送は 2026 年内。5'6"/66 ポンドの家庭用ヒューマノイドで、22-DoF ハンド、ソフトボディ、4 時間稼働、オンボード LLM、騒音約 22dB。早期アクセス価格 20,000 ドル + 200 ドル預金、または月額 499 ドルのサブスク。プライバシー "no-go" ゾーンと顔ぼかしを内蔵。家庭に実際に配送される最初の本格的なコンシューマー型ヒューマノイド。
- [三菱自動車 × Highlanders ヒューマノイド MOU](https://www.mitsubishi-motors.com/en/newsroom/newsrelease/2026/20260709_1.html) - 🆕 **2026-07-09**。三菱自動車が東京大学発スタートアップ Highlanders と MOU を締結し、ヒューマノイドロボット（溶接、物流、エンジン組立）を京都工場で共同開発・量産へ — 報道によると月産約 1,000 台を目標に、早ければ 2027 年から生産開始。日本の労働力不足に対応。

---

## 🎮 エージェントシミュレーションと世界モデル

*エージェントを訓練し、観察し、ストレステストするシミュレーション環境。世界モデル・身体性研究が言語エージェントと交わる中、重要性が高まり続けている。*

- [Generative Agents](https://github.com/joonspk-research/generative_agents) - 💤 スタンフォードの名著 *Smallville*（Park et al., 2023）。25 体の LLM 駆動キャラクターをメモリ + 反省 + 計画で連携させるコストチューム。後続の多くのマルチエージェント論文に影響。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fjoonspk-research%2Fgenerative_agents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Voyager](https://github.com/MineDojo/Voyager) - 💤 Minecraft の生涯学習エージェント—— GPT-4 にスキルライブラリとカリキュラム（Wang et al., 2023）。オープンエンド型エージェント評価の古典。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FMineDojo%2FVoyager&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SWE-Gym](https://github.com/SWE-Gym/SWE-Gym) - 実際の GitHub Issue で SWE エージェントを訓練するオープン環境、SWE-bench とセット。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSWE-Gym%2FSWE-Gym&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [WebArena](https://webarena.dev/) - 現実的で再現可能なウェブ環境（Reddit、ショッピング、GitLab クローン）。OSWorld や多くのブラウザエージェント論文で使用される。**[WebArena-Verified](https://github.com/ServiceNow/webarena-verified)**（ServiceNow、2025-12）：全 812 タスク・参照解答・評価器を人手でレビュー；LLM-as-judge を決定論的な型認識チェックに置き換え；低コスト評価用に 258 タスクの "Hard" サブセットあり。
- [WorkArena](https://github.com/ServiceNow/WorkArena) - ServiceNow 製のブラウザエージェント用エンタープライズ職場ベンチマーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FServiceNow%2FWorkArena&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Genie 3](https://deepmind.google/models/genie/) - Google DeepMind の対話型ビデオ世界モデル—— プロンプトからプレイ可能な 3D 世界を生成。クローズドコード研究。
- [NVIDIA Cosmos](https://github.com/nvidia-cosmos/cosmos-predict2) - 身体性 AI / ロボティクス用の NVIDIA 世界モデル基盤—— 物理的にもっともらしいビデオ未来を生成。predict1 は非推奨となり Cosmos-Predict2 に移行（Predict 2.5 は CES 2026 で発表）；上記の Cosmos 3（2026-06）も参照。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fnvidia-cosmos%2Fcosmos-predict2&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Snowflake Agent World Model (AWM)](https://github.com/Snowflake-Labs/agent-world-model) - 🆕 **2026 年 2 月 10 日オープンソース化、5 月 1 日に ICML 2026 採択**。1,000 個の実行可能 SQL バックエンドツール使用環境（35K+ ツール、10K タスク）を統一 MCP インターフェースで提供する合成環境生成パイプライン——大規模マルチターン agentic RL を実現。インフラは `meta-pytorch/OpenEnv` にマージ済み。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSnowflake-Labs%2Fagent-world-model&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Qwen-AgentWorld](https://github.com/QwenLM/Qwen-AgentWorld) - 🆕 **2026 年 6 月**。エージェントの次アクションではなく環境（Web・OS・ターミナル）の次状態を予測してエージェント環境をシミュレートするネイティブ言語世界モデル。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FQwenLM%2FQwen-AgentWorld&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SimWorld](https://github.com/SimWorld-AI/SimWorld) - 🆕 Unreal Engine 5 上に構築されたオープンエンドの高リアリティシミュレータ。複雑な物理・社会環境で自律 AI エージェントをテスト。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSimWorld-AI%2FSimWorld&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 📊 ベンチマークとリーダーボード

*フロンティア AI 能力を追跡する標準評価スイートとライブリーダーボード。*

- [BenchLM](https://benchlm.ai/) - 🆕 複数のベンチマークファミリーを集約したリーダーボード。2026-07 首位: Claude Fable 5 91、Claude Mythos 5 89、Gemini 3.1 Pro 88（ランク対象 79 / 追跡 281 モデル、296 ベンチマーク）。
- [SWE-bench Verified](https://www.swebench.com/) - 実世界の GitHub Issue 解決ベンチマーク。2026-04 首位: Claude Mythos 93.9%、Claude Opus 4.7 87.6%。
- [GPQA Diamond](https://github.com/idavidrein/gpqa) - 💤 データセットリポは 2024-09 以降更新なし。専門家レベルの科学推論。2026-04 首位: Gemini 3.1 Pro 94.3%（世界記録）、Claude Opus 4.7 94.2%。
- [ARC-AGI 2](https://arcprize.org/) - 新規タスクの抽象推論。GPT-5.5 が 85% で首位（2026-07）；Gemini 3.1 Pro 77.1%（2026-03）。
- [ARC-AGI-3](https://arcprize.org/leaderboard) - 🆕 🧪 第 3 世代 ARC ベンチマーク — エージェントが未知のインタラクティブ環境にその場で適応する必要がある（Kaggle コンペ）。初期のトップスコアはほぼゼロ（Gemini 3.1 Pro 約 0.37%）。
- [OSWorld](https://os-world.github.io/) - デスクトップ GUI 操作。Claude Fable 5 / Mythos 5 が 85% で首位（2026-07）；GPT-5.4 75%（人間ベースライン超え）。
- [Arena (旧 LMArena / Chatbot Arena)](https://arena.ai/) - クラウドソース型の会話選好バトル。2026-07: Claude Fable 5 が首位（Elo 1525）、Opus 4.8（1512）と GPT-5.5 Pro（1510）が続く。
- [MMLU-Pro](https://github.com/TIGER-AI-Lab/MMLU-Pro) - MMLU の難化后継者。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTIGER-AI-Lab%2FMMLU-Pro&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LiveCodeBench](https://livecodebench.github.io/) - コンテスト形式のコーディングベンチマーク、汚染耐性のため継続的に更新。
- [AIME 2025 / Humanity's Last Exam (HLE)](https://agi.safe.ai/) - エリート数学 / 博士レベルの一般推論。
- [Terminal-Bench](https://www.tbench.ai/) - CLI エージェント評価。Codex CLI 77.3%。
- [Wolfram LLM Benchmarking Project](https://www.wolfram.com/llm-benchmarking-project/) - 英語仕様から Wolfram Language へのコード生成。
- [Terminal-Bench 2.0](https://www.tbench.ai/leaderboard/terminal-bench/2.0) - **2025 年末 / 2026 年初**。89 の厳選ターミナルタスク（コンパイル、訓練、設定、デバッグ）。リーダーボード首位: NexAU-AHE + GPT-5.5 の 84.7%（2026-05-14）。
- [GDPval](https://openai.com/index/gdpval/) - OpenAI の経済価値ベンチマーク（2025 年 9 月公開、arXiv:2510.04374）。44 職種 / 9 業界、1,320 の専門家作問タスクを収録。[GDPval-AA リーダーボード](https://artificialanalysis.ai/evaluations/gdpval-aa)の首位（2026-07）は Claude Opus 4.8（Elo 1890）で、GPT-5.5（1769）を上回る。GPT-5.6 ローンチ（2026-07-09）で再び拡充・注目された。
- [SWE-bench Pro](https://benchlm.ai/benchmarks/swePro) - 🆕 Verified の後継となるリポジトリレベルのエンジニアリングベンチマーク。Claude Opus 4.7 64.3% > GPT-5.5 58.6%（長期のリポジトリ作業では Claude がリード）。**2026-07**: Claude Mythos 5 が **80.3%** で首位；⚠️ **OpenAI の監査（2026-07-08）**で Pro タスクの約 30% に不備（過度に厳格なテスト、仕様不足のプロンプト）があると判明 — OpenAI は SWE-bench Pro をコーディングエージェントの主要指標として使う推奨を撤回。
- [LLM-Stats Live Leaderboard](https://llm-stats.com/llm-updates) - 🆕 新しくリリースされたモデルを横断ベンチで継続更新するライブダッシュボード。
- [τ²-Bench (Tau-Bench)](https://github.com/sierra-research/tau2-bench) - 🆕 Sierra Research のツール-エージェント-ユーザー対話ベンチマーク（リテール / 航空ドメイン）。マルチターンのツール使用・DB 操作・ポリシー遵守を計測。2026 年 4 月の首位は 38 評価モデル中 Claude Mythos Preview の 89.2%。同リポジトリは現在、音声 + 通信 / 銀行ドメインを追加した **τ³-Bench 1.0.0（2026-03-18）** もホストする。MIT。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsierra-research%2Ftau2-bench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Gartner 2026 マジッククアドラント: エンタープライズ AI コーディングエージェント](https://cursor.com/blog/cursor-leads-gartner-mq-2026) - 🆕 **2026 年**。エンタープライズ向け AI コーディングエージェントに関する初の MQ。リーダーは **GitHub Copilot**・**OpenAI Codex**・**Cursor**（評価対象 12 ベンダー；Tabnine はビジョナリー）。コーディングエージェント市場がエンタープライズの成熟期に入ったことを示す。
- [Terminal-Bench 2.1](https://www.tbench.ai/leaderboard/terminal-bench/2.1) - 🆕 **2026 年 6 月**。CLI タスクカバレッジを拡充した Terminal-Bench 更新版；リーダーボード: Claude Code + Fable 5 が 83.8% で首位（2026-06-07）、Codex + GPT-5.5 が 83.1%。トップ CLI エージェント間の差は 1% 未満に。
- [Agent Memory Benchmark (AMB)](https://github.com/vectorize-io/agent-memory-benchmark) - 🆕 vectorize.io が Hindsight と同時公開したエージェントメモリ評価のオープンベンチマーク——retain / recall / reflect 操作を長期タスク性能で検証。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvectorize-io%2Fagent-memory-benchmark&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agents' Last Exam (ALE)](https://snorkel.ai/leaderboard/agents-last-exam/) - 🆕 **2026 年 6 月**。UC Berkeley (RDI) + Snorkel AI が 300 人以上の業界専門家と共同で作成した、55 の専門サブ分野にまたがる長期・経済価値の高いプロフェッショナルタスクの benchmark（公開版 ALE-V1 は 1,500+ タスクコーパスからの参照タスク 147 件；arXiv:2606.05405）。ローンチ時の合格率は約 2.6%；2026 年 7 月のリーダーボード首位は Codex + GPT-5.6 の 53.6/100（GPT-5.6 ローンチで特集）。6 ヶ月ごとにタスクを入れ替える生きた benchmark。
- [JetBrains Kotlin Benchmark](https://blog.jetbrains.com/kotlin/2026/07/introducing-the-kotlin-benchmark-evaluate-ai-coding-agents-on-real-world-kotlin-tasks/) - 🆕 **2026 年 7 月**。JetBrains が公開した Kotlin 言語向け AI コーディングエージェント benchmark。コード生成・リファクタリング・テスト作成・バグ修正などの実際の開発タスクを評価。汎用 SWE-bench を超えた言語特化型評価を開発者に提供。
- [Stripe Agent Benchmark](https://stripe.com/blog/can-ai-agents-build-real-stripe-integrations) - 🆕 **2026 年 3 月**。AI エージェントがゼロから完全な Stripe 統合を構築できるかをテストするエンドツーエンド評価スイート。コード生成・テスト実行・本番スタイルの検証をカバー。初期評価ではフルスタック API 統合タスクで Claude Opus 4.5 が平均 92% を達成。
- [GAIA Benchmark](https://huggingface.co/spaces/gaia-benchmark/leaderboard) - 汎用 AI アシスタントベンチマーク：466 の実タスクでの多段推論 + ツール使用 + Web ブラウジング。**2026-07-15 公開スナップショット**：Claude Mythos 5 と Claude Fable 5 が **52.3%** で首位タイ、GPT-5.4 Pro が 50.5%。データ汚染耐性を重視した設計。

---

## 🖥️ Computer Use / デスクトップエージェント

*OS レベルでデスクトップソフトウェアを見て・操作し・自動化するエージェント。ブラウザ専用エージェントは [🌐 ブラウザと Web エージェント](#-ブラウザと-web-エージェント) 参照。*

- [Claude Computer Use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) - Anthropic の Computer Use 機能 —— Claude が画面を見、マウス / キーボードで任意のソフトウェアを自動化。
- [ChatGPT Agent](https://openai.com/index/introducing-chatgpt-agent/) - Operator（2025 年に廃止）の後継 — ブラウジング、予約、フォーム入力、ウェブタスク自動化のための ChatGPT のエージェントモード。
- [Google Project Mariner](https://deepmind.google/models/project-mariner/) - 📦 **終了**（2026 年 5 月）。ブラウザエージェント研究プロジェクト。機能は Gemini と Chrome に統合された。
- [Microsoft Copilot Agents](https://www.microsoft.com/en-us/microsoft-copilot/) - 🆕 Microsoft 365 スタック上の自律バックグラウンドエージェント。
- [Open Interpreter](https://github.com/OpenInterpreter/open-interpreter) - コンピュータへの自然言語インターフェース—— LLM にローカルでコードを実行させる。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenInterpreter%2Fopen-interpreter&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Manus AI](https://manus.im/) - 🇨🇳 🆕 クラウド・ローカルハイブリッドモデルの自律汎用 AI エージェント。調査・コーディング・複雑なマルチステップタスクを処理。
- [Genspark](https://www.genspark.ai/) - 🆕 mixture-of-agents アーキテクチャのオールインワン自律ワークエージェント。電話も掛けられる。
- [Beam AI](https://beam.ai/) - 🆕 成功事例に基づきロジックを洗練させる自己学習デスクトップエージェント。
- [Microsoft Copilot Studio Computer-Using Agents](https://techcommunity.microsoft.com/blog/copilot-studio-blog/computer-using-agents-in-microsoft-copilot-studio-are-now-generally-available/4519427) - 🆕 **2026 年 5 月 13 日 GA**。Copilot Studio 内で、UI を介して Web サイトやデスクトップアプリを直接操作するエージェントを構築可能 —— Microsoft 365 / Power Platform 全体で利用できる、Claude Computer Use に対する Microsoft 純正の回答。
- [Perplexity Personal Computer](https://www.perplexity.ai/hub/products/computer-for-windows) - 🆕 **2026 年 6 月（Windows）**。Perplexity のマルチモデル・エージェントオーケストレーター（19+ AI モデルを自動ルーティング）を Windows へ展開；ローカルファイル・ネイティブアプリ・Web サービスを一つのシステムで接続。Mac 版（4 月 16 日）の延長線上で、Computex 2026 発表のハイブリッドローカル / クラウド推論オーケストレーターとも連動。
- [ChatGPT Workspace Agents](https://venturebeat.com/orchestration/openai-unveils-workspace-agents-a-successor-to-custom-gpts-for-enterprises-that-can-plug-directly-into-slack-salesforce-and-more) - 🆕 **リサーチプレビュー 2026-04-22，クレジット課金化 2026-05-06，EKM 対応 2026-05-07**。OpenAI の Custom GPTs の企業向け後継 —— クラウド側で動き、ファイルアクセス、コード実行、Slack / Google Drive / Salesforce などとのコネクタを持ち、スケジュール実行も可能。Business / Enterprise / Edu / Teachers 向けに提供され、Codex をバックエンドに採用。

---

## 🌐 ブラウザと Web エージェント

*実ブラウザを介して Web と対話するエージェント—— ナビゲーション、クリック、スクレイピング、マルチページワークフローをこなすフレームワークとインフラ。*

- [Browser Use](https://github.com/browser-use/browser-use) - 2026 年にオープンソースブラウザエージェントの事実上の標準。105K star。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowser-use%2Fbrowser-use&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Stagehand](https://github.com/browserbase/stagehand) - Browserbase 製の「ブラウザエージェント用 SDK」—— 型付きの `act` / `extract` / `observe` プリミティブを Playwright の上に提供。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowserbase%2Fstagehand&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Steel Browser](https://github.com/steel-dev/steel-browser) - 🆕 AI エージェント用オープンソースブラウザ API —— セッション永続化とプロキシローテーションを備えたサンドボックス Chromium。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsteel-dev%2Fsteel-browser&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Skyvern](https://github.com/Skyvern-AI/skyvern) - LLM とコンピュータ・ビジョンでブラウザベースワークフローを自動化。AGPL-3.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSkyvern-AI%2Fskyvern&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentQL](https://github.com/tinyfish-io/agentql) - クエリ言語 + Playwright 統合でセマンティックな Web 抽出。動的 / 乱雑なページでもロバスト。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftinyfish-io%2Fagentql&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hyperbrowser MCP](https://github.com/hyperbrowserai/mcp) - 🆕 ホステッドのヘッドレスブラウザフリートを MCP サーバーとして公開。標準ツールインターフェースで Claude / GPT / LangChain にプラグイン。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhyperbrowserai%2Fmcp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) - 🆕 マイクロソフト公式の Playwright サーバーを MCP ツールとして公開。プロダクショングレードの自動化。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fplaywright-mcp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MultiOn](https://theagi.company/) - 📦 ステップ推論 + メモリを内蔵したホステッド型ブラウザエージェントプラットフォーム；multion.ai は現在 AGI, Inc.（theagi.company）にリダイレクト。クローズドコード。
- [Browserbase](https://www.browserbase.com/) - AI エージェント専用のヘッドレスブラウザインフラ —— ステルス、セッション永続化、captcha 処理、オブザーバビリティ。
- [BrowserOS](https://www.browseros.com/) - 🆕 AI エージェントを内蔵した初のオープンソースブラウザ —— プライバシー優先の Chrome 代替。コードなしで自然言語によるタスク自動化が可能。ローカル優先設計で、Perplexity Comet や Arc の AI 機能と対抗。
- [WebBrain](https://webbrain.one) - 🆕 **2026 年 7 月**。Chrome + Firefox 向けのオープンソース MIT ブラウザ拡張機能。ローカルまたはクラウド LLM で Web タスクを自動化。"Ask モード" は読み取り専用の要約・データ抽出；"Act モード" はクリック・フォーム入力・ナビゲーション。ローカルファーストな設計 —— llama.cpp / Ollama 使用時はデータがデバイスから出ない。
- [Vercel Agent Browser](https://github.com/vercel-labs/agent-browser) - 🆕 AI エージェント向けのヘッドレスブラウザ自動化 CLI。2026 年 6 月リリースで Core Web Vitals（LCP/CLS/TTFB/FCP）用の `vitals` コマンド、SPA ナビゲーション用 `pushstate`、アウトオブプロセスのプラグインシステム、MCP サーバーモード、ホスト環境向け `@agent-browser/sandbox` を追加。Apache-2.0、37K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvercel-labs%2Fagent-browser&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Google ADK — ブラウザ & A2A 連携](https://github.com/google/adk-python) - Google の Agent Development Kit（v1.33、2026-05；v2.0 はベータ）— マルチエージェント構成、MCP ツール、A2A プロトコル統合。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle%2Fadk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Muse Spark 1.1（Web エージェント）](https://artificialanalysis.ai/models/muse-spark) - 🆕 💰 **2026-07-09**。Meta Superintelligence Labs 初の有償エージェントモデル。Meta Model API のパブリックプレビュー経由で提供 — WebArena-Verified で 69.0（首位の Claude Opus 4.8 の 71.2 に次ぐ）。
- [Firecrawl v2](https://github.com/firecrawl/firecrawl) - 🆕 **v2.11.0、2026 年 6 月**。エージェント型 Web スクレイピングプラットフォームの大型アップデート：JavaScript レンダリング改善、ライブクロール Webhook、バッチ URL 処理。150K+ stars。AGPL-3.0（SDK は MIT）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ffirecrawl%2Ffirecrawl&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome) - 🆕 Anthropic のブラウザエージェント Chrome 拡張 — Claude がタブを横断してナビゲート、フォーム入力、操作を実行。⚠️ 2026 年 7 月の研究で悪性拡張によるプロンプトインジェクションのリスクが判明 — 利用前に権限を確認のこと。
- [Perplexity Comet](https://www.perplexity.ai/comet) - Comet Assistant（バックグラウンドエージェント）を備えた Perplexity のエージェント型 AI ブラウザ；2025 年 10 月から無料ティアあり；Perplexity は 2026 年 6 月に Comet 向けに $200M を調達。

---

## 🗣️ 音声とマルチモーダルエージェント

*音声対応 ・ マルチモーダル AI エージェントプラットフォーム。*

- [AgentLine](https://agentline.cloud/) - 🆕 ⚠️ **Unverified.** AI エージェント向けテレフォニー基盤 —— 電話番号の発行、発信／着信、リアルタイム文字起こしを JSON で webhook に流す。エージェント音声パイプライン用途に絞った Twilio の軽量代替を標榜。提出者は有料ユーザー 30+ と主張するが、第三者の採用事実は未確認。
- [ElevenLabs](https://elevenlabs.io/) - 業界トップの AI 音声合成、クローン、会話 AI。
- [Vapi](https://github.com/VapiAI/server-sdk-python) - 音声 AI エージェントを構築・テスト・展開するプラットフォーム。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FVapiAI%2Fserver-sdk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Retell AI](https://www.retellai.com/) - プロダクション対応の会話型音声 AI エージェント。
- [Bland AI](https://www.bland.ai/) - 企業向け AI 電話プラットフォーム。
- [Hermes](https://buildwithhermes.com/) - 🆕 ⚠️ **未検証（創業者ベータ）。** 代理店向けホワイトレーベル音声エージェントプラットフォーム：エージェント、ネイティブ CRM、アウト/インバウンドキャンペーン編成、クライアント別従量課金を一体化。$149/月〜。独立した採用実績は未確認。
- [LiveKit Agents](https://github.com/livekit/agents) - 音声・ビデオ・データを含むリアルタイムマルチモーダル AI エージェント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flivekit%2Fagents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Pipecat](https://github.com/pipecat-ai/pipecat) - 音声・マルチモーダル会話 AI のオープンソースフレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fpipecat-ai%2Fpipecat&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vocode](https://github.com/vocodedev/vocode-core) - 💤 **Stale**（最終リリース 2024-06）。音声ベース LLM エージェントライブラリ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvocodedev%2Fvocode-core&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Bolna](https://github.com/bolna-ai/bolna) - エンドツーエンドのオープンソース音声 AI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbolna-ai%2Fbolna&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cartesia](https://www.cartesia.ai/) - 🆕 超低遅延のリアルタイム会話型音声 AI。
- [Meta Voice AI](https://ai.meta.com/) - 🆕 旧 PlayHT/Play.ai チームの技術を Meta AI ・ AI キャラクター、ウェアラブルに統合。Play.ai は 2025-12-31 にサービス終了。
- [Sesame](https://www.sesame.com/) - 🆕 感情理解と自然会話を備えた音声 AI コンパニオン。
- [OpenYabby](https://github.com/OpenYabby/OpenYabby) - 🆕 macOS 向けオープンソースの音声駆動型マルチエージェントオーケストレーター — Realtime API + CLI ランナー + マルチチャネル連携。リードエージェントが計画を立て、レビューと QA をサブエージェントに委任します。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenYabby%2FOpenYabby&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ElevenAgents](https://elevenlabs.io/agents) - 🆕 ElevenLabs のフルスタック音声エージェント基盤（2026 年 4〜5 月更新）。MCP 対応、マルチモーダルメッセージ、会話トピック発見、ナレッジベース検索、ツール呼び出し前の音声制御を提供。音声エージェント基盤として初めて AIUC-1 認証を取得。
- [Cartesia Line](https://cartesia.ai/blog/introducing-line-for-voice-agents) - コードファースト音声エージェント基盤（2025 年 8 月ローンチ）。Cartesia の Sonic TTS + Ink STT 上に構築され、バックグラウンド推論とオンプレデプロイに対応。first audio まで約 40〜90ms。
- [Deepgram Voice Agent API](https://deepgram.com/product/voice-agent-api) - 🆕 STT（Nova-3）+ LLM ルーティング + TTS（Aura-2）+ 通話中 10 言語切り替え対応の Flux 会話型 STT を 1 エンドポイントで束ねた。
- [OpenAI Realtime API (GPT-Realtime-2)](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/) - 🆕 **2026 年 5 月 7 日**。並列ツール呼び出しと 128K コンテキストに対応した GPT-5 クラス推論の音声版；GPT-Realtime-Translate / GPT-Realtime-Whisper と同時リリース。2026-07-06 に gpt-realtime-2.1 / 2.1-mini へ更新（英数字認識・ノイズ処理の改善、低遅延化）。
- [Dograh](https://github.com/dograh-hq/dograh) - 🆕 オープンソース・セルフホスト型の音声 AI プラットフォーム —— Vapi / Retell のオープン代替。オンプレ運用、Speech-to-Speech または LLM/STT/TTS のいずれも BYOK。ビジュアルワークフロービルダー、MCP ネイティブ、テレフォニー対応。BSD-2-Clause、4K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdograh-hq%2Fdograh&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hume TADA](https://github.com/HumeAI/tada) - 🆕 **2026 年 3 月**。Hume AI 初のオープンソース TTS —— Text Audio Dual Alignment：テキストと音声を 1:1 に同期した単一トークンストリームで生成。コンテンツの幻覚ゼロ、RTF 約 0.09、TADA-1B/3B-ML（9+ 言語）、スマホで動作。次世代 EVI 音声エージェントの基盤。コードは MIT、ウェイトは Llama 3.2 ライセンス。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHumeAI%2Ftada&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Grok Voice Agent Builder](https://x.ai/news/grok-voice-agent-builder) - 🆕 **2026-07-01**。Grok Voice 上で本番音声エージェントを構築する xAI のノーコードプラットフォーム — 無料の電話番号プロビジョニング付きテレフォニー、ナレッジコレクション、ツール / MCP コネクタ、ガードレール、80+ の音声と約 2 分のボイスクローン；ベータ期間中 $0.05/分。

---

## 📱 パーソナル AI エージェント

- [OpenClaw](https://github.com/openclaw/openclaw) - 🆕 スキル・メモリ・マルチチャネルメッセージング、Dreaming、Canvas/A2UI、ACP コーディング harness を備えた個人向け AI エージェントプラットフォーム。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenclaw%2Fopenclaw&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Rabbit R1](https://www.rabbit.tech/) - ラージアクションモデルを搭載した個人 AI デバイス。
- [Limitless](https://www.limitless.ai/) - 📦 **Meta が買収（2025 年末）**；ペンダントの販売は終了。見・言い・聞いたものをパーソナライズした AI（旧 Rewind）；チームは Meta の AI ウェアラブル部門に統合。
- [Open Interpreter](https://github.com/OpenInterpreter/open-interpreter) - コンピュータへの自然言語インターフェース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenInterpreter%2Fopen-interpreter&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [01 Light](https://github.com/OpenInterpreter/01) - 💤 **Stale**（2024-11 以降更新なし）。オープンソースの音声コンピュータインターフェース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenInterpreter%2F01&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Leon](https://github.com/leon-ai/leon) - 自サーバ上に住むオープンソース個人アシスタント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fleon-ai%2Fleon&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Khoj](https://github.com/khoj-ai/khoj) - ノートやドキュメント、画像を機械的にスキャンして会話できる「第二の脳」。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fkhoj-ai%2Fkhoj&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Humane AI Pin](https://humane.com/) - ⚠️ **2025年2月28日にサービス終了**（HPに買収され、デバイスは廃止）。元々はスクリーンレス・アンビエントコンピューティングのウェアラブル AI デバイス。
- [Arahi AI](https://arahi.ai/) - 🆕 個人生産性 + ビジネス自動化アシスタント。
- [Lindy AI](https://www.lindy.ai/) - 🆕 メール・カレンダー・ワークフロー自動化のノーコード AI エージェント。
- [MuleRun](https://mulerun.com/) - 🆕 繰り返しタスクとバックグラウンド自動化の常駐エージェント。
- [Gemini Intelligence](https://blog.google/products-and-platforms/platforms/android/gemini-intelligence/) - 🆕 **2026 年 5 月 12 日（Android Show: I/O Edition）**。Googlebooks ノート PC、Wear OS、Android Auto、Android XR を横断するプロアクティブな agentic AI 機能群。最新の Samsung Galaxy と Pixel から段階展開。買い物リストからカートを自動作成、スピンクラスの予約、Rambler STT による "フィラー語" 除去などを実現。
- [Gemini Spark](https://gemini.google/overview/agent/spark/) - 🆕 **I/O 2026（2026 年 5 月 19 日）**。Gemini アプリ内の 24/7 自律エージェント — Gmail / Workspace 統合でマルチステッププロセスをプロアクティブに実行；2026 年 7 月 1 日にネイティブ Mac アプリへ拡大。
- [QwenPaw](https://github.com/agentscope-ai/QwenPaw) - 🆕 🇨🇳 **2026 年 5 月、CoPaw から改称**。Qwen / AgentScope エコシステム下のセルフホスト型パーソナルアシスタント。ローカル優先のメモリ、ホットロード可能な skills、マルチエージェント協調、マルチチャネル（DingTalk / Feishu / WeChat / Discord / Telegram）、ツールガード + skill スキャナを内蔵。Apache-2.0。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentscope-ai%2FQwenPaw&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AI Growth Agents for Marketers](https://github.com/thaolst/ai-growth-agents-for-marketers) - 🆕 ⚠️ **Unverified**（初期段階）。東南アジアの実際のフィンテックキャンペーンに基づくグロースマーケティング用プロンプトと Python エージェント。キャンペーンブリーフ、MEU プランニング、A/B テスト分析をマルチエージェントワークフローでカバー。Agent Skills 形式 — `npx skills add` でインストール可能。ベトナム語 + 英語のバイリンガル。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fthaolst%2Fai-growth-agents-for-marketers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsoft Scout](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) - 🆕 **Build 2026（2026 年 6 月 2 日）**。OpenClaw フレームワーク上に構築された Microsoft の常時稼働パーソナルエージェント —— クラウド / デスクトップ / Web を横断してプロアクティブに動作し、Teams / Outlook / OneDrive / SharePoint に接続。各エージェントは独自の Entra ID で動作し、ポリシー適合性チェック + 監査トレイルを継続実施。Microsoft Frontier プログラムでプライベートプレビュー、Intune ポリシー + GitHub Copilot ライセンスが必要。
- [Lenovo Qira / Motorola Qira](https://news.lenovo.com/pressroom/press-releases/lenovo-unveils-lenovo-and-motorola-qira/) - 🆕 **CES 2026（2026 年 1 月 6 日）**。Lenovo と Motorola が共同開発した「パーソナル・アンビエント・インテリジェンス・システム」—— PC / スマホ / タブレット / ウェアラブルを横断するコンテキスト認識 AI。2026 年 Q1 から一部 Lenovo デバイスで展開、その後 Motorola スマホへ。主要 OEM 初のアンビエント AI プレイ。
- [Yao Agents](https://yaoagents.com) - 🆕 🇨🇳 **2026 年 5 月**。ローカルファーストの AI 実行プラットフォーム：30+ ドメインの Expert（コーディング・執筆・データ分析・PM）と自律 Robot ワーカー。5 段階パイプライン、Docker サンドボックス隔離、マルチプラットフォームメッセージング、MCP 対応、BYOK モデル設定、デバイス横断編成の Tai Link。オープンソースエンジン：[YaoApp/yao](https://github.com/YaoApp/yao)。
- [AgentArk](https://github.com/agentark-ai/AgentArk) - 🆕 🧪 **2026 年 6 月**（v0.0.1、ベータ — 本番非推奨）。ローカル制御とセキュリティを優先するパーソナル AI OS；GEPA オプティマイザランタイムによる自己学習。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentark-ai%2FAgentArk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [nanobot](https://github.com/HKUDS/nanobot) - 🆕 超軽量のオープンソースパーソナル AI エージェント（41K+ stars）。2026 年 4 月のリリース（v0.1.5.x）でスレッドスコープのセッション、自動コンパクトメモリ、Dream コンソリデーション、DeepSeek-V4 対応、Windows 対応を追加。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2Fnanobot&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 📱 モバイルエージェント

*Android / iOS を操作する GUI エージェント。デスクトップ Computer Use の次のフロンティア。*

- [Mobile-Agent](https://github.com/X-PLUG/MobileAgent) - 🇨🇳 アリババ製の代表的なマルチモーダル電話操作エージェントファミリー（v1 → v3、Mobile-Agent-E、V も）。Android ベンチマークで SOTA。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FX-PLUG%2FMobileAgent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AppAgent](https://github.com/TencentQQGYLab/AppAgent) - 💤 タップやスワイプでスマートフォンアプリを操作するテンセント製マルチモーダルエージェント。初期の影響ある実装；後継は AppAgentX（2025-03）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTencentQQGYLab%2FAppAgent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
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
- [Google Vertex AI Agent Builder](https://cloud.google.com/products/agent-builder) - **2026 年 4 月に改称** — Vertex AI のエージェント構築機能は現在 Gemini Enterprise Agent Platform（上記参照）の一部：Agent Studio、Model Garden、Google Antigravity オーケストレーション。
- [Amazon Bedrock Agents](https://aws.amazon.com/bedrock/agents/) - 複数ステップのタスクを社内システムをまたいで実行。
- [ServiceNow AI Agents](https://www.servicenow.com/products/ai-agents.html) - 🆕 企業 IT サービスマネジメント用 AI エージェント + AI Control Tower。
- [ServiceNow Action Fabric（MCP Server）](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-opens-its-full-system-of-action-to-every-AI-Agent-in-the-enterprise/default.aspx) - 🆕 **2026-05-05**。ServiceNow が AI Platform を任意の AI エージェント（Claude / Copilot / カスタム）に開放。GA の MCP サーバはすべての Now Assist / AI Native SKU に付属。すべてのアクションは AI Control Tower を経由するため、ID 検証・権限スコープ・監査が自動で適用される。OAuth、消費量メータリング、ロールベースのツールパックを標準搭載。Anthropic（Claude Cowork）が最初のデザインパートナー。
- [IBM watsonx Orchestrate](https://www.ibm.com/products/watsonx-orchestrate) - 企業アプリをまたいで作業を自動化する AI アシスタントプラットフォーム。
- [Oracle AI Agents](https://www.oracle.com/artificial-intelligence/) - 🆕 Oracle Fusion Cloud ERP と統合された企業 AI エージェント。
- [Moveworks](https://www.moveworks.com/) - あらゆるシステムで動作する AI のエンタープライズコパイロットプラットフォーム。ServiceNow による買収が完了（2025-12-15）。
- [UiPath Agentic Automation](https://www.uipath.com/) - 🆕 RPA ボット資産にエージェント推論を重ねたインテリジェントプロセス自動化。
- [AgentX](https://www.agentx.so/) - チャットボットをプラグアンドプレイで提供しスケーラブルな AI 自動化を提供する企業エージェントソリューション。
- [Sistava](https://sistava.com) - ⚠️ 営業・マーケティング・サポート・採用・オペレーション向けの「オンデマンド AI 従業員」— エージェントが永続メモリを持ってユーザーのツール内で作業；月額 $19 から。
- [Amazon Bedrock AgentCore Payments](https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-bedrock-agentcore-payments-preview/) - 🆕 **2026-05-07（プレビュー）**。AgentCore エージェント向けのマネージド決済 — API・MCP サーバー・Web コンテンツ・他エージェントへの自律的支払いを Coinbase（CDP ウォレット、x402 Bazaar）と Stripe（Privy ウォレット）の統合で実現；支出上限とトランザクション可観測性を 4 つの AWS リージョンで提供。
- [OutSystems Agentic Systems Platform](https://www.outsystems.com/) - 🆕 **2026 年 6 月**。ローコードプラットフォームを「AI ネイティブ」なエージェント開発環境へとピボット。オープンかつ統制された AI 開発、自社モデル持ち込み、マルチエージェント・オーケストレーション、エンタープライズコンプライアンスツールを提供。Copilot Studio や Agentforce に対抗。
- [Sema4.ai](https://sema4.ai/) - 🆕 Python ファースト、ガバナンス内蔵の企業 AI エージェントプラットフォーム。
- [SAP Business AI Platform + Autonomous Suite](https://news.sap.com/2026/05/sap-sapphire-sap-unveils-autonomous-enterprise/) - 🆕 **SAP Sapphire 2026（2026-05-12）**。SAP が「Autonomous Enterprise」を発表：統一 AI 基盤としての SAP Business AI Platform；財務・サプライチェーン・調達・HR・CX の既存アプリにエージェントを追加する SAP Autonomous Suite；企業向けエージェントとエージェントワークフローを構築する Joule Studio；Joule Work UX；7 つの Industry AI ソリューション。Joule エージェントを駆動する基盤モデルには Claude も含まれる。
- [Microsoft Agent 365 + Microsoft 365 E7](https://techcommunity.microsoft.com/blog/agent-365-blog/microsoft-365-e7--agent365-from-where-you-are-to-enterprise-ai-at-scale/4519969) - 🆕 **2026-05-01 GA**、5 月中に拡充。アイデンティティ中心の AI エージェントコントロールプレーン。単体 $15/ユーザー/月、もしくは新しい Microsoft 365 E7「Frontier」スイートに含めて $99/ユーザー/月。5 月の追加で AWS Bedrock / Google Cloud とのレジストリ同期、Intune / Defender プレビューポリシー、エージェント向け SASE を追加。
- [OpenAI Guaranteed Capacity（Compute Annual Pass）](https://openai.com/business/guaranteed-capacity/) - 🆕 **2026-05-19**。企業の AI プロダクト / エージェント / ワークフロー向けに 1 / 2 / 3 年期のコンピュート予約を製品化 —— GPT-5.5 級エージェントの企業導入でコスト / 供給不安を下げるための、Anthropic Priority Tier への製品としての回答。
- [Bristol Myers Squibb ↔ Claude Enterprise](https://news.bms.com/news/corporate-financial/2026/Bristol-Myers-Squibb-Announces-Strategic-Agreement-with-Anthropic-to-Position-Claude-Enterprise-as-the-Shared-Intelligence-Platform-Across-Its-Global-Operations/default.aspx) - 🆕 **2026-05-20**。BMS が Claude Enterprise を 30,000+ 名の社員の共通インテリジェンス基盤として採用し、創薬・開発・デリバリーの全工程にエージェント型 Claude を組み込む。世界トップ 5 製薬企業では初めての社全体規模での Claude 導入。
- [Kore.ai Artemis Agent Platform](https://www.kore.ai/news/kore-ai-launches-artemis-the-new-generation-of-the-kore-ai-agent-platform-for-building-governing-and-optimizing-enterprise-ai) - 🆕 **2026 年 5 月 21 日（Azure で公開）**。AI ネイティブなエンタープライズエージェント基盤。中核は新しい YAML 風の宣言型 **Agent Blueprint Language (ABL)** で、マルチエージェント workflow を記述する。Kore.ai による Copilot Studio と Agentforce への構造的な挑戦。
- [FPT Flezi Foundry™](https://www.morningstar.com/news/business-wire/20260521235556/fpt-launches-flezi-foundry-advancing-ai-augmented-delivery-for-global-enterprises) - 🆕 **2026 年 5 月 21 日**。"Service-as-a-Software" のガバナンスを敷いた AI 強化型デリバリープラットフォーム。SDLC 全体をエージェント隊で回す **Agentic Development Lifecycle (ADLC)** と、既存 ITOps の上にインシデント解決エージェントを重ねる **Agentic Managed Services (AMS)** の 2 モードで提供。
- [Databricks Genie One](https://www.databricks.com/blog/introducing-genie-one-genie-ontology-and-genie-agents) - 🆕 **2026-06-16（Data + AI Summit）**。Databricks が発表したエージェント型「データ同僚」。構造化・非構造化データを横断して作業を自動オーケストレーションし、新しい **Genie Ontology**（組織全体のナレッジグラフ）に基づき Unity Catalog でガバナンス。Genie Agents を同梱、社内テストで初回正答率 84.5%。
- [ZenseAI.AgentMesh（Zensar）](https://www.prnewswire.com/news-releases/zensar-technologies-launches-zenseaiagentmesh-to-accelerate-enterprise-ai-adoption-at-scale-302805437.html) - 🆕 **2026-06-19**。Zensar のエンタープライズ向けエージェント AI プラットフォーム。「Agentic AI のためのユニバーサルエンタープライズ OS」を掲げ、自律エージェントの発見・構築・デプロイ・ガバナンスを一元化。80+ のプリビルト業種別・横断機能エージェントを備え、6〜8 週間でパイロットから本番への移行を謳う。
- [Meta Business Agent](https://about.fb.com/news/2026/06/meta-business-agent/) - 🆕 **2026-06-03（グローバル展開）**。Meta が WhatsApp・Instagram・Messenger 向けに展開する AI ビジネスエージェント。問い合わせ対応、カタログ商品の提案、予約受付、リードの選別、成約までを担い、必要に応じて人間へ引き継ぐ。すでに 100 万以上のビジネスが利用。**Meta Business Agent Platform** では企業が独自エージェントを構成し Shopify / Zendesk / Shopee と連携可能 — 現時点では無料で有効化でき、有料サブスクリプションティアが今後登場予定。
- [Snyk Evo Agentic Development Security (ADS)](https://snyk.io/news/snyk-launches-evo-agentic-development-security/) - 🆕 **2026 年 6 月**。自律 AI コーディングエージェント専用のセキュリティ/ガバナンスプラットフォーム：エージェントが使うもの・行うこと・生成コードをリアルタイムに統制。
- [Cognizant Neuro AI + ServiceNow AI Agent](https://news.cognizant.com/2026-06-18-Cognizant-expands-cross-platform-agentic-AI-with-new-ServiceNow-AI-Agent-interoperability) - 🆕 **2026 年 6 月**。クロスプラットフォームのエンタープライズ編成：ServiceNow エージェントが Cognizant の Multi-Agent Accelerator 内でネイティブに動作。
- [Talkdesk Agent Builder](https://www.cmswire.com/contact-center/customer-contact-week-2026-capturing-the-ai-announcements-in-contact-center-technology/) - 🆕 **2026 年 6 月**。ローコードビルダー：ビジネスユーザーが数週間ではなく数時間で本番級 AI エージェントをコンタクトセンターに展開。
- [HelloTwin Digital Authority](https://siliconangle.com/2026/06/24/hellotwin-launches-digital-authority-bring-governed-ai-agents-enterprise/) - 🆕 **2026 年 6 月**。単一の監査可能な信頼できる情報源として設計された AI ツイン。明確な境界でエージェンティックワークフローをガバナンス。

---

## 📊 エージェント評価とオブザーバビリティ

- [LangSmith](https://www.langchain.com/langsmith) - LangChain 公式のデバッグ / 評価 / モニタリングプラットフォーム。
- [LangSmith SDK](https://github.com/langchain-ai/langsmith-sdk) - クライアント SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangsmith-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Langfuse](https://github.com/langfuse/langfuse) - オープンソース LLM エンジニアリングプラットフォーム: オブザーバビリティ + 評価 + プロンプト管理。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangfuse%2Flangfuse&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Helicone](https://github.com/Helicone/helicone) - オープンソース LLM オブザーバビリティ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHelicone%2Fhelicone&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Arize Phoenix](https://github.com/Arize-ai/phoenix) - オープンソース LLM オブザーバビリティ + 評価。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FArize-ai%2Fphoenix&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Braintrust](https://www.braintrust.dev/) - LLM 評価 + 最適化プラットフォーム。
- [Arena (旧 LMArena / LMSYS Chatbot Arena)](https://arena.ai/) - 人間の選好投票によるクラウドソース型 AI ベンチマーク；リーダーボードは現在 LLM・画像生成・コードモデルをカバー。LMSYS → LMArena（2025）→ Arena（2026）。
- [Patronus AI](https://www.patronus.ai/) - 💰 LLM 評価 / レッドチーム企業。現在はエージェント訓練向けのデジタルワールドモデルとシミュレーション基盤を構築するフロンティア研究ラボとして再ポジショニング（$50M シリーズ B）；研究成果に Lynx、FinanceBench、GLIDER。
- [DeepEval](https://github.com/confident-ai/deepeval) - Pytest スタイルの LLM 評価フレームワーク。組み込み 14+ メトリック。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fconfident-ai%2Fdeepeval&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agenta](https://github.com/agenta-ai/agenta) - 🆕 オールインワンオープンソース LLMOps。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagenta-ai%2Fagenta&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AutoEvals](https://github.com/braintrustdata/autoevals) - ベストプラクティスの LLM 評価スコアラーライブラリ。Braintrust 製。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbraintrustdata%2Fautoevals&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [BenchClaw](https://github.com/Agnuxo1/benchclaw) - ⚠️ **Unverified**。8 個の awesome リストのうち 7 個で却下、単独メンテナチームで2 star。**可視性のための掲載**。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAgnuxo1%2Fbenchclaw&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [PromptEden](https://www.prompteden.com) - ⚠️ **Unverified**。商用 SaaS で、ChatGPT / Claude / Gemini / Perplexity / Copilot / Grok がどうブランドを説明するかをモニタリング。同一 PR が 1 日以内に 10 個の awesome リストに提出された。**可視性のための掲載**。
- [AgentBench](https://github.com/THUDM/AgentBench) - LLM をエージェントとして評価する多次元ベンチマーク。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTHUDM%2FAgentBench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Braintrust](https://www.braintrust.dev/) - エンタープライズ級 AI プロダクト構築スタック——評価、プロンプト playground、ロギングを一体化。SDK: [braintrust-sdk-javascript](https://github.com/braintrustdata/braintrust-sdk-javascript) と braintrust-sdk-python（braintrust-sdk から分割 / 改名）。
- [OpenLLMetry](https://github.com/traceloop/openllmetry) - OpenTelemetry に基づくオープンソースの LLM オブザーバビリティ。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftraceloop%2Fopenllmetry&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Weights & Biases Weave](https://github.com/wandb/weave) - AI アプリの開発・評価・監視ツールキット。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fwandb%2Fweave&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SWE-bench](https://github.com/SWE-bench/SWE-bench) - 実世界のソフトウェア工学課題で LLM を評価するベンチマーク。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSWE-bench%2FSWE-bench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Terminal-Bench](https://www.tbench.ai/) - 🆕 ターミナル系コーディングエージェント評価のためのベンチマーク。Harbor Framework がメンテナンス。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fharbor-framework%2Fterminal-bench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Harbor](https://github.com/harbor-framework/harbor) - 🆕 エージェントと LLM を大規模に評価・最適化するフレームワーク — Terminal-Bench 2.x やカスタムベンチマークを数千のクラウドサンドボックスで実行し、RL ロールアウトを生成；Stanford × Laude Institute のコラボレーション。Apache-2.0。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fharbor-framework%2Fharbor&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Laminar](https://github.com/lmnr-ai/lmnr) - 🆕 長時間稼働 AI エージェント専用に設計されたオープンソースのオブザーバビリティ基盤（Apache-2.0、YC S24）。OpenTelemetry ネイティブ、トランスクリプトビュー、Signals、トレース上の SQL クエリ、ブラウザエージェントのセッション再生。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flmnr-ai%2Flmnr&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangSmith Engine](https://www.langchain.com/blog/interrupt-2026-overview) - 🆕 **2026 年 5 月（Interrupt 2026）**。LangSmith の自律失敗診断レイヤー —— 本番障害を優先度付き問題にクラスタリングし、トレースとコードを横断して根本原因を特定、人間レビュー用の修正提案を生成。新発の SmithDB（Rust + DataFusion で構築されたエージェントオブザーバビリティ用 DB）と連動。
- [AgentSight](https://github.com/eunomia-bpf/AgentSight) - LLM/コーディングエージェント向けのゼロインストルメンテーション eBPF オブザーバビリティ。エージェントを変更せずに syscall レベル（プロセス、ファイル、ネットワーク）のトレースをキャプチャし、フルスタックの挙動分析を実現。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Feunomia-bpf%2FAgentSight&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Prismix](https://prismix.dev) - 77 以上の AI サービス（OpenAI、Anthropic、Cursor など）のステータスをリアルタイム監視（ステータスバッジと API 付き）。71 以上のソースから AI ニュースを集約し、80 以上のサーバーを収録する MCP サーバーディレクトリも提供。無料・登録不要。
- [Ceros (by Beyond Identity)](https://www.prnewswire.com/news-releases/ceros-launches-providing-unified-identity-observability-and-governance-for-every-ai-agent-and-workflow-302800721.html) - 🆕 **2026-06-16**。エージェント AI の信頼レイヤー — 統一されたアイデンティティ・可観測性・ガバナンス（発見 / インベントリ、ランタイムポリシー強制、監査証跡）。（同名のインタラクティブコンテンツ企業とは無関係。）
- [Zoom Agent Performance Suite](https://news.zoom.com/introducing-agent-architect-and-agent-performance-suite-for-zoom-virtual-agent/) - 🆕 **2026-06**。顧客対応シナリオにおける自律エージェントの性能をテスト・検証・最適化する専用スイート。
- [AgentOps](https://github.com/AgentOps-AI/agentops) - 🆕 セッションリプレイ付きのエージェント監視・コンプライアンス・テストツールキット；MCP 接続された任意のエージェントをゼロコンフィグで可観測化する MCP サーバー；5K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAgentOps-AI%2Fagentops&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenTelemetry GenAI Semantic Conventions](https://github.com/open-telemetry/semantic-conventions-genai) - GenAI クライアント・エージェント・ツール呼び出し・MCP 向けの標準化されたスパン / メトリクス / イベント — 任意の OTel バックエンド（Arize、Langfuse、Helicone、Jaeger など）でベンダー中立なトレーシングを実現。コア semconv リポジトリから専用の GenAI リポジトリへ移動。
- [Tracecat](https://github.com/TracecatHQ/tracecat) - 🆕 SOC ワークフロー向けにエージェントの完全なトレースをキャプチャするオープンソースのセキュリティ自動化プラットフォーム — AI エージェントを検知・エンリッチ・対応パイプラインと統合。AGPL-3.0（エンタープライズ版の例外規定あり）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTracecatHQ%2Ftracecat&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🔬 AI 研究ツール

- [Hugging Face Transformers](https://github.com/huggingface/transformers) - モデルとトレーニングツールの事実上の標準ライブラリ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhuggingface%2Ftransformers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [vLLM](https://github.com/vllm-project/vllm) - 高スループット LLM 推論・サービング。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvllm-project%2Fvllm&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SGLang](https://github.com/sgl-project/sglang) - 高性能 LLM 推論エンジン。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsgl-project%2Fsglang&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [llama.cpp](https://github.com/ggml-org/llama.cpp) - C/C++ 高性能 LLM 推論。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fggml-org%2Fllama.cpp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Ollama](https://github.com/ollama/ollama) - ローカルで LLM を走らせる最も簡単な方法。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Follama%2Follama&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LM Studio](https://lmstudio.ai/) - デスクトップでローカル LLM を動かす GUI、複数プロバイダ。
- [OpenRouter](https://openrouter.ai/) - 1 つの API で 70+ プロバイダーの 400+ AI モデルを一括利用。
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
- [LLM Agents MOOC (Berkeley)](https://llmagents-learning.org/) - UC Berkeley の LLM エージェントコース（ルートサイトは最新回にリダイレクト）。
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
- [LobeHub](https://github.com/lobehub/lobehub) - エージェント管理プラットフォーム（旧 Lobe Chat）— エージェントを 7×24 稼働に編成し、AI チームの採用 / スケジューリング / レポーティングを提供。トップクラスの TypeScript AI プロジェクト（80K+ stars）。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flobehub%2Flobehub&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Coze Loop](https://github.com/coze-dev/coze-loop) - 🆕 ByteDance Coze チームによるオープンソースエージェント最適化プラットフォーム。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-loop&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentScope](https://github.com/modelscope/agentscope) - アリババ ModelScope のマルチエージェントフレームワーク + ビジュアルデバッグ + 分散実行。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelscope%2Fagentscope&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Bisheng](https://github.com/dataelement/bisheng) - オープンエンタープライズ LLM DevOps プラットフォーム：ワークフローエディタ、RAG、エージェントオーケストレーション、ファインチューニング、評価。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdataelement%2Fbisheng&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) - LLM に SOP 役割（PM / アーキテクト / エンジニア）を割り振るマルチエージェント。現在は FoundationAgents org 配下で管理。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FFoundationAgents%2FMetaGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### RAG / ナレッジ

- [FastGPT](https://github.com/labring/FastGPT) - ナレッジベースを中心に設計された LLM プラットフォーム: データ取り込み、RAG、ビジュアルワークフロー。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flabring%2FFastGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [QAnything](https://github.com/netease-youdao/QAnything) - 💤 NetEase Youdao 製の任意のローカルドキュメントを対象にした質問応答。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fnetease-youdao%2FQAnything&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAGFlow](https://github.com/infiniflow/ragflow) - スキャン PDF、テーブル、図表に強い深いドキュメント理解 RAG エンジン。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Finfiniflow%2Fragflow&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LightRAG](https://github.com/HKUDS/LightRAG) - 香港大学 HKUDS の軽量グラフ RAG エンジン。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2FLightRAG&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### パーソナルと生産性

- [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) - AI ワークスペースエージェント付きオープンソース Notion 代替。AGPL-3.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAppFlowy-IO%2FAppFlowy&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Manus AI](https://manus.im/) - Butterfly Effect（中国発、シンガポールに移転）による汎用自律エージェント。**Meta が約 $2B で買収（2025-12-30 発表）** — manus.im には現在 "Manus is now part of Meta" と表示。
- [Coze (扣子)](https://www.coze.cn/) - ByteDance のノーコードエージェントビルダー。中国本土中心、国際版は coze.com。
- [Qwen App (千问)](https://www.qwen.ai/) - アリババの大衆向けコンシューマーエージェント（通義千問からリブランド）。淘宝 / DingTalk / Quark に統合。
- [Doubao Agents](https://www.doubao.com/) - ByteDance の Doubao モデルファミリーをその上に携載したフラッグシップコンシューマーアシスタント。

### 開発者ツール

- [Trae](https://www.trae.ai/) - ByteDance の AI IDE 兼「10x AI コーディングエンジニア」— Cursor に対抗する中国発の最有力チャレンジャー。
- [CoderPlan](https://coderplan.ai/) - 中国開発者向け統合 LLM API ゲートウェイ（Claude / OpenAI / Gemini、Claude Code 一行設定対応）、従量課金制・Alipay & WeChat Pay 対応。
- [Cherry Studio](https://github.com/CherryHQ/cherry-studio) - 中国開発者サークルで最もインストールされているオープンソースデスクトップ LLM クライアント —— マルチプロバイダ会話 + ナレッジベース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FCherryHQ%2Fcherry-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ScienceOne 100 / 磐石100](https://english.cas.cn/newsroom/cas-in-media/202604/t20260429_1158251.shtml) - 🆕 中国科学院の科学推論エージェントシステム。50+ 中科院研究所、100+ 研究シナリオ、付属 2,000+ 研究ツール。
- [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code) - 🆕 **2026 年 6 月 6 日**。Moonshot AI の TypeScript / MIT 製ターミナルコーディングエージェント —— 隔離コンテキストで動く coder / explore / plan サブエージェントを内蔵、`/mcp-config` で対話式に MCP を設定。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FMoonshotAI%2Fkimi-code&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Qwen Code](https://github.com/QwenLM/qwen-code) - アリババ Qwen チームのオープンソースターミナルコーディングエージェント — エージェントチーム、自動メモリ、IDE 統合、マルチプロバイダ（OpenAI / Anthropic / Gemini / Qwen）。26K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FQwenLM%2Fqwen-code&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Coze Studio](https://github.com/coze-dev/coze-studio) - 🆕 ByteDance Coze.com のオープンソース対応版——オールインワン・ビジュアルエージェントビルダー、デバッグ＆デプロイツール付き。Apache-2.0、20K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 📝 比較 — サイドバイサイド表

*2026 年に最もよく出てくる「どれを選ぶ？」の判断マトリクス。*

### 🏗️ エージェントフレームワーク

| フレームワーク | 言語 | マルチエージェント | 状態 / グラフ | ストリーミング | License | 適している用途 |
|------------|------|------------|----------------|----------------|---------|----------|
| [LangGraph](https://github.com/langchain-ai/langgraph) | Python / JS | ✅ ネイティブ | ✅ 一級社会 | ✅ | MIT | プロダクションステートフルワークフロー |
| [CrewAI](https://github.com/crewAIInc/crewAI) | Python | ✅ ロールベース | ⚠️ タスクグラフ | ✅ | MIT | ロールプレイエージェントチーム |
| [AutoGen / Microsoft Agent Framework](https://github.com/microsoft/autogen) | Python / .NET | ✅ 会話型 | ⚠️ Group Chat | ✅ | CC-BY-4.0 / MIT | エンタープライズマルチエージェント |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | Python | ✅ handoff | ❌ | ✅ | MIT | OpenAI ネイティブ本番 |
| [Mastra](https://github.com/mastra-ai/mastra) | TypeScript | ✅ | ✅ workflows | ✅ | Elastic-2.0 | TypeScript ファースト |
| [Google ADK](https://github.com/google/adk-python) | Python / Java | ✅ 階層 | ⚠️ | ✅ | Apache-2.0 | Gemini + Vertex AI |
| [DSPy](https://github.com/stanfordnlp/dspy) | Python | ⚠️ モジュール経由 | ⚠️ プログラム型 | ✅ | MIT | プログラム的プロンプト最適化 |
| [Agno (旧 Phidata)](https://github.com/agno-agi/agno) | Python | ✅ teams | ❌ | ✅ | MPL-2.0 | メモリ付きマルチモーダルエージェント |

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

*表は 2026-07-17 に検証済み。数値の変更はソース付きで PR を送付してください。*

---

### 💰 基盤モデル — API コスト & コンテキスト

*価格は USD/100万トークン。データ：2026-07-17。*

| モデル | プロバイダー | コンテキスト | 入力 $/1M | 出力 $/1M | 最適用途 |
|-------|----------|---------------|-----------|------------|----------|
| GPT-5.6 Sol | OpenAI | 1M | $5.00 | $30.00 | フロンティア推論フラッグシップ |
| GPT-5.6 Terra | OpenAI | 1M | $2.50 | $15.00 | コスト効率の高い本番ワークロード |
| GPT-5.6 Luna | OpenAI | 1M | $1.00 | $6.00 | 大量・速度重視タスク |
| GPT-4o | OpenAI | 128K | $2.50 | $10.00 | 幅広いツール利用・ビジョン |
| GPT-4o-mini | OpenAI | 128K | $0.15 | $0.60 | 大量の単純タスク |
| Claude Sonnet 5 | Anthropic | 1M | $2.00（導入価格） | $10.00（導入価格） | デフォルトのエージェントワークホース（2026-08-31 以降 $3/$15） |
| Claude Opus 4.8 | Anthropic | 1M | $5.00 | $25.00 | 最難度推論タスク |
| Claude Fable 5 | Anthropic | 1M | $10.00 | $50.00 | Mythos クラスのフロンティアタスク |
| Claude Haiku 4.5 | Anthropic | 1M | $1.00 | $5.00 | Anthropic エコシステムの高速タスク |
| Gemini 3.1 Pro | Google | 1M | $2.00 | $12.00 | フラッグシップ推論・マルチモーダル |
| Gemini 2.5 Flash | Google | 1M | $0.30 | $2.50 | コスパ重視マルチモーダル |
| Gemini 2.5 Pro | Google | 1M | $1.25 | $10.00 | 超長文・マルチモーダル |
| Gemini 2.5 Flash-Lite | Google | 1M | $0.10 | $0.40 | 超低コスト大量リクエスト |
| DeepSeek V4-Flash | DeepSeek | 1M | $0.14 | $0.28 | 低コストコーディング推論 |
| Qwen3 235B A22B | Alibaba | 131K | ~$0.29 | ~$1.15 | 最強中国語+コーディング MoE |
| Kimi K2.6 | Moonshot AI | 262K | $0.95 | $4.00 | 中国語+超長コンテキスト |
| Grok 4 | xAI | 256K | $3.00 | $15.00 | X/Twitter エコシステム推論 |
| Grok 4.5 | xAI | 500K | $2.00 | $6.00 | コーディング+エージェントのフラッグシップ |

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
| ElevenLabs v3 | ❌ | ⭐⭐⭐⭐⭐ | ✅ | ❌ | ~200ms | 70+ | プロプライエタリ |
| Whisper v3（ローカル） | ⭐⭐⭐⭐★ | ❌ | ❌ | ✅ | ~1s | 99 | MIT |
| Deepgram Nova-3 | ⭐⭐⭐⭐⭐ | ✅ | ✅ | ❌ | <100ms | 45+ | プロプライエタリ |
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
| Midjourney V8.1 | 2K+ | Web のみ | 芸術的品質最高 | アート制作 | $10–$120/月 |
| Stable Diffusion 3.5 | 2K | ローカル+API | 良好 | OSS・セルフホスト | オープンウェイト（Stability AI Community License） |
| Ideogram 3 | 2K | API+Web | 良好 | 画像内テキスト最強 | フリーミアム |

---

### 🎥 動画生成モデル

| モデル | 最大長 | 解像度 | API/ローカル | 最適用途 | ステータス |
|-------|-----------|-----------|-------------|----------|------------------|
| Veo 3.1 | 2分 | 4K | API（Vertex） | 最高忠実度 | GA（Google） |
| Kling VIDEO 3.0 | 3分 | 1080p | API+Web | 映画スタイル先頭 | GA（Kuaishou） |
| Runway Gen-4 | 10s/クリップ | 1080p | API+Web | 精密モーション制御 | GA |
| Seedance 2.0 | 60s | 2K | API | 高速・コスパ良好 | GA（ByteDance） |
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
| Verba | Python | Weaviate | ⚠️ | ❌ | BSD-3 | 📦 アーカイブ済み — Weaviate ネイティブ RAG チャットボット |

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
| [OpenClaw](https://github.com/openclaw/openclaw) | ✅ | ✅ | ✅ ネイティブ | ✅（TG/Discord/WA） | ✅ | オールインワン個人エージェント |
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
| Gemini gemini-embedding-2 | 3072 | 8K | ❌ | ✅ | 多言語 | プロプライエタリ | — |
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
| Kimi K2.6 | Moonshot AI | 262K | 高い | ⭐⭐⭐⭐☆ | ❌ | ~$0.95 |
| GLM-5.2 | Zhipu AI | 1M | 高い | ⭐⭐⭐⭐☆ | ✅ MIT | ~$0.50 |
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

*全比較表データ：2026-07-17。数値変更は PR でご報告を。*

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
→ **Claude Opus 4.7**（1M コンテキスト）+ **LlamaIndex** + **pgvector**。人間によるレビューを必ず残すこと。

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
- **Llama 3.3 70B**（Meta、Llama 3.3 Community License）、**DeepSeek V3.2** (MIT)、**Qwen3 235B A22B** (Apache-2.0)。

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
- [A2A Protocol](https://github.com/a2aproject/A2A) - A2A プロトコル（Google 発、現在は Linux Foundation）が 150+ パートナーとのクロスフレームワークエージェント連携を可能に；v1.0 は 2026 年 5 月に公開。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fa2aproject%2FA2A&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - SWE-bench 80.9% で 2026 年のターミナル型コーディングエージェントの選択肢となった。
- [Kiro](https://kiro.dev/) - 🆕 AWS が 10 タスク同時管理可能な自律コーディングエージェントをローンチ。
- [Devin 3.0](https://www.cognition.ai/) - 🆕 動的再プラン、自己修復コード、レガシーコードベース移行を含む進化。
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/) - 🆕 AutoGen + Semantic Kernel が統一企業エージェントプラットフォームとして統合。
- [OpenAI Codex CLI](https://github.com/openai/codex) - OpenAI のオープンソースターミナルエージェント参入。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fcodex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Browser Use](https://github.com/browser-use/browser-use) - AI エージェントが Web と自然に対話できるようにしたブレイクスルー。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowser-use%2Fbrowser-use&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude Computer Use](https://www.anthropic.com/) - 🆕 Desktop Intelligence により Claude が画面を見てあらゆるソフトウェアをコントロール。
- [Manus AI](https://manus.im/) - 🇨🇳 調査、コーディング、複雑ワークフローを処理できる汎用自律エージェント；現在は Meta の一部（約 $2B で買収、2025-12）。
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
| **2026-06-27** | GPT-4.5 が ChatGPT から退役（API は継続）—— OpenAI はコンシューマー製品を GPT-5.5 / GPT-5.6 ファミリーに集中 | モデル |
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
| **2026-05-21** | [MCP 2026-07 Release Candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) 公開 — ステートレスコア、拡張フレームワーク、MCP Apps サーバレンダリング UI、OAuth/OIDC 強化。正式版は 7 月 28 日予定 | プロトコル |
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
| **2026-06-09** | [Claude Fable 5 + Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) リリース — Anthropic 初の一般提供 **Mythos クラス**モデル（Fable 5 は一般公開、Mythos 5 は Project Glasswing 経由の限定提供）| モデル |
| **2026-06-12** | [米国の輸出管理指令により Anthropic が全顧客向けに Fable 5 + Mythos 5 を停止](https://www.anthropic.com/news/fable-mythos-access) — 一般提供されたフロンティアモデルが政府により強制停止された初の事例 | 業界 |
| **2026-06-12** | [Kimi K2.7 Code](https://kimi.ai/) を Moonshot AI がリリース — 1T MoE のコーディング優先モデル（256K、Modified MIT）、推論トークン消費を約 30% 削減 | モデル |
| **2026-06-13** | [GLM-5.2](https://z.ai/blog/glm-5.2) を Zhipu AI がリリース — コーディング優先の 744B MoE、100万トークンコンテキスト、全 GLM Coding Plan ティアで提供 | モデル |
| **2026-06-30** | [Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5) リリース — これまでで最もエージェント性能の高い Sonnet。低コストで Opus 4.8 に近い性能を発揮し、Claude.ai の Free/Pro の新デフォルトモデルに | モデル |
| **2026-07-01** | [Claude Fable 5 グローバルアクセス復旧](https://www.anthropic.com/news/redeploying-fable-5) — 米国商務省が 6 月 30 日に輸出管理を解除；Anthropic が新しい安全クラシファイア付きで Claude.ai・API・Claude Code・Claude Cowork の Fable 5 への世界的アクセスを復旧。Mythos 5 は引き続き米国の審査済みエンティティに制限 | モデル |
| **2026-07-01** | [Devin Security Swarm](https://www.prnewswire.com/news-releases/cognition-launches-devin-security-swarm-to-tackle-the-vulnerability-backlog-302814800.html) を Cognition がローンチ — 並列エージェントによる脆弱性発見、実行時の悪用可能性検証、修正 PR 作成 | ツール |
| **2026-07-01** | [Grok Voice Agent Builder](https://x.ai/news/grok-voice-agent-builder) — Grok Voice 上の本番音声エージェント向け xAI ノーコードプラットフォーム；テレフォニー、MCP コネクタ、80+ 音声、ベータ $0.05/分 | ツール |
| **2026-07-02** | [Sysdig が JADEPUFFER を開示](https://hackread.com/sysdig-jadepuffer-first-agentic-ransomware-operation/) — 自律 AI エージェントが初期 RCE から復旧不可能な暗号化・恐喝までを一貫して実行した初のランサムウェア作戦 | 業界 |
| **2026-07-02** | [Leanstral 1.5](https://mistral.ai/news/leanstral-1-5/) を Mistral がリリース — オープンウェイトの Lean 4 形式検証モデル（miniF2F 100%）；同日 Zhipu が GLM-5.2 用エージェントハーネス [ZCode](https://www.scmp.com/tech/tech-trends/article/3359170/zhipu-ai-releases-harness-glm-52-model-chinese-firm-takes-aim-anthropic) を公開 | モデル |
| **2026-07-03** | AG2 v1.0.0b0 リリース — AutoGen のコミュニティ主導 Fork；Microsoft は 2026 年 Q1 に AutoGen をメンテナンスモードに移行 | フレームワーク |
| **2026-07-06** | [Tencent Hunyuan Hy3](https://www.tencent.com/en-us/articles/2202386.html) が正式にオープンソース公開（Apache 2.0）— 4 月プレビューに続く 295B/21B アクティブ MoE；同日 OpenAI API に gpt-realtime-2.1 / 2.1-mini も登場 | モデル |
| **2026-07-07** | [Meta Muse Image](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) ローンチ — Meta Superintelligence Labs のエージェント型画像生成モデル。Instagram Stories（米国）と一部の国の WhatsApp に統合；Muse Video もプレビュー | モデル |
| **2026-07-07** | Arize Phoenix 7 月 7 日リリース：Metric Charts、Trace Search、REST API 拡充 | ツール |
| **2026-07-08** | [Grok 4.5](https://x.ai/news/grok-4-5) を xAI がリリース — Cursor と共同訓練したコーディング / エージェントのフラッグシップ；500K コンテキスト、入出力 100 万トークンあたり $2/$6；Cursor のデフォルトモデル | モデル |
| **2026-07-08** | [GPT-Live-1 / GPT-Live-1 mini](https://openai.com/index/introducing-gpt-live/) — Advanced Voice Mode を置き換えるフルデュプレックス音声モデル；GPT-Live-1（有料）と GPT-Live-1 mini（無料）；リアルタイムのライブ翻訳 | モデル |
| **2026-07-08** | [Robostral Navigate](https://mistral.ai/news/robostral-navigate/) — Mistral 初のロボティクスモデル（単一 RGB カメラからの 8B 身体性ナビゲーション）；同日 OpenAI の監査で SWE-bench Pro のタスク約 30% に不備があると判明 | モデル |
| **2026-07-09** | [GPT-5.6 Sol / Terra / Luna](https://openai.com/index/gpt-5-6/) GA — トラステッドパートナープレビューを経て GPT-5.6 ファミリーが ChatGPT・Codex・API で一般提供；[ChatGPT Work](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) も同時ローンチし、Codex が ChatGPT デスクトップアプリに統合 | モデル |
| **2026-07-09** | [Muse Spark 1.1](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/) を Meta がリリース — 新しいパブリック Meta Model API プレビュー経由のマルチモーダル・エージェントモデル；オープンソースの Llama ラインと並行するプロプライエタリ路線 | モデル |
| **2026-07-10** | [Cursor 3.11](https://cursor.com/changelog) — サイドチャット、会話履歴検索、きめ細かなエージェント可観測性のための Cloud Agent Hooks | ツール |
| **2026-07-14** | [Oracle が AI ネイティブな Agentic Applications Builder を追加](https://www.oracle.com/news/announcement/oracle-introduces-ai-native-builder-experience-2026-07-14/) — Fusion 向け AI Agent Studio を拡張し、Fusion エージェントアプリをプロコード開発者にも開放；Fusion 顧客は追加費用なし | フレームワーク |
| **2026-07-16** | [Kimi K3](https://kimi.ai/) を Moonshot AI がローンチ — 2.8T パラメータの疎 MoE（896 エキスパート中 16 が有効）、1M トークンコンテキスト、100 万トークンあたり $3/$15；フルオープンウェイトは 7 月下旬公開予定 | モデル |

---

## 貢献

[CONTRIBUTING.md](CONTRIBUTING.md) をご読みください。**スパム防止の品質ゲート**は中、英、日の 3 言語版すべてに適用されます: 自己宣伝タイプの並列提出 PR は一律拒否されます。

## License

MIT © [Zijian Ni](https://github.com/Zijian-Ni)

---

*Made with ❤️ by [Zijian Ni](https://github.com/Zijian-Ni) · 2026。日本語版は英語版と同期します。不一致がある場合は英語版を正とします。*

