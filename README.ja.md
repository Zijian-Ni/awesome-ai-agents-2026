<div align="center">

# 🤖 Awesome AI Agents 2026 · 日本語版

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fawesome-ai-agents-2026&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)](https://github.com/Zijian-Ni/awesome-ai-agents-2026)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-September%208%2C%202026-blue.svg)](#)
[![Resources](https://img.shields.io/badge/Resources-910%2B-orange.svg)](#)
[![Audited](https://img.shields.io/badge/Spam_Audited-2026--09--08-success.svg)](#️-ステータス凡例)
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
> 3. 🧩 **構成例を応用する** → [スタックレシピ](#-スタックレシピ--ツール構成例)
> 4. 🔍 **最適なツールを選ぶ** → [比較表](#-比較--サイドバイサイド表)
> 5. ⚠️ **アンチパターンを避ける** → [非推奨リスト](#️-アンチピック--使ってはいけないケース)
>
> **すでに開発中の方へ：** こちらへジャンプ：
> - 🆕 [最新追加（2026年9月）](#-2026-ai-タイムライン) • 🛡️ [セキュリティ](#️-エージェントセキュリティ) • 💰 [コスト比較](#-基盤モデル--api-コスト--コンテキスト)

---

## クイックナビ

*件数は履歴・関連章での再掲を含む収録回数で、固有製品数ではありません。選定リストとして、追加モデルの検索には公式カタログも案内しています。*

| カテゴリ | 説明 | 件数 |
|----------|-------------|-------|
| [🧠 基盤モデル 2026](#-基盤モデル-2026) | OpenAI・Anthropic・Google・Meta ほか 22+ プロバイダーの最新 LLM | 230+ |
| [🎨 マルチモーダルと生成 AI](#-マルチモーダルと生成-ai) | 画像・動画・音声・音楽生成 | 60+ |
| [🔗 エージェントプロトコルと標準](#-エージェントプロトコルと標準) | MCP、A2A、相互運用標準 | 20+ |
| [🏗️ エージェントフレームワーク](#️-エージェントフレームワーク) | 自律 AI エージェント構築ライブラリ | 55+ |
| [🛠️ エージェント IDE とビジュアルビルダー](#️-エージェント-ide-とビジュアルビルダー) | エージェントフロー設計のビジュアル / ローコード環境 | 10+ |
| [🧠 エージェントメモリ](#-エージェントメモリ) | 永続メモリとコンテキスト管理 | 25+ |
| [🔌 ツールと API 連携](#-ツールと-api-連携) | エージェントと外部サービスの接続 | 25+ |
| [💱 エージェント経済とマーケットプレイス](#-エージェント経済とマーケットプレイス) | エージェントの決済・収益化・サービス発見 | 10+ |
| [🧪 エージェントサンドボックスと計算分離](#-エージェントサンドボックスと計算分離) | エージェント生成コードの安全な実行環境 | 10+ |
| [🛡️ エージェントセキュリティ](#️-エージェントセキュリティ) | プロンプトインジェクション対策とガードレール | 35+ |
| [🔍 RAG とナレッジ](#-rag-とナレッジ) | 検索拡張生成システム | 20+ |
| [💻 コーディングエージェント](#-コーディングエージェント) | AI によるソフトウェアエンジニアリング | 55+ |
| [🤖 Physical AI / 身体性エージェント](#-physical-ai--身体性エージェント) | ヒューマノイドロボット、身体性 AI、産業自動化 | 45+ |
| [🎮 エージェントシミュレーションと世界モデル](#-エージェントシミュレーションと世界モデル) | エージェント訓練とストレステスト用シミュレーション環境 | 10+ |
| [📊 ベンチマークとリーダーボード](#-ベンチマークとリーダーボード) | フロンティア能力を追跡するリーダーボード | 25+ |
| [🖥️ Computer Use / デスクトップエージェント](#️-computer-use--デスクトップエージェント) | デスクトップ自動化と OS レベル制御 | 10+ |
| [🌐 ブラウザと Web エージェント](#-ブラウザと-web-エージェント) | 実ブラウザを操作するエージェント | 20+ |
| [🗣️ 音声とマルチモーダルエージェント](#️-音声とマルチモーダルエージェント) | 音声対応の対話型 AI | 25+ |
| [📱 パーソナル AI エージェント](#-パーソナル-ai-エージェント) | 生産性と日常生活のアシスタント | 20+ |
| [📱 モバイルエージェント](#-モバイルエージェント) | スマホ操作エージェント（Android / iOS） | 10+ |
| [🏢 エンタープライズエージェントプラットフォーム](#-エンタープライズエージェントプラットフォーム) | エンタープライズ級エージェント展開 | 30+ |
| [📊 エージェント評価とオブザーバビリティ](#-エージェント評価とオブザーバビリティ) | テスト・モニタリング・ベンチマーク | 30+ |
| [🔬 AI 研究ツール](#-ai-研究ツール) | AI / ML 研究・実験ツール | 15+ |
| [📚 学習リソース](#-学習リソース) | 論文、コース、チュートリアル | 25+ |
| [🇨🇳 中国 AI エコシステム](#-中国-ai-エコシステム) | 中国チームの主要プロジェクト | 25+ |
| [📝 比較 — サイドバイサイド表](#-比較--サイドバイサイド表) | 横並び比較表 | — |
| [🗺️ シナリオガイド — 何に何を使うべきか](#️-シナリオガイド--何に何を使うべきか) | シナリオとツールの対応 | 58 |
| [📋 スタックレシピ — ツール構成例](#-スタックレシピ--ツール構成例) | 厳選されたマルチツール構成 | 8 |
| [⚠️ アンチピック — 使ってはいけないケース](#️-アンチピック--使ってはいけないケース) | 使うべきでないものとその理由 | 17 |

---

## 目次

- [🧠 基盤モデル 2026](#-基盤モデル-2026)
- [🎨 マルチモーダルと生成 AI](#-マルチモーダルと生成-ai)
- [🔗 エージェントプロトコルと標準](#-エージェントプロトコルと標準)
- [🏗️ エージェントフレームワーク](#️-エージェントフレームワーク)
- [🛠️ エージェント IDE とビジュアルビルダー](#️-エージェント-ide-とビジュアルビルダー)
- [🧠 エージェントメモリ](#-エージェントメモリ)
- [🔌 ツールと API 連携](#-ツールと-api-連携)
- [💱 エージェント経済とマーケットプレイス](#-エージェント経済とマーケットプレイス)
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
- [📋 スタックレシピ — ツール構成例](#-スタックレシピ--ツール構成例)
- [⚠️ アンチピック — 使ってはいけないケース](#️-アンチピック--使ってはいけないケース)
- [🌟 2026 年に注目すべきエージェントプロジェクト](#-2026-年に注目すべきエージェントプロジェクト)
- [📅 2026 AI タイムライン](#-2026-ai-タイムライン)

---

## 🧠 基盤モデル 2026

*現行モデルと過去の基盤モデルを提供元別に厳選。モデルカード、API の利用可否、重みのライセンスは区別し、日付付きの項目でリリース履歴を保持する。*

### OpenAI
- [GPT-Live-1 / GPT-Live-1 mini](https://openai.com/index/introducing-gpt-live/) - 🆕 **2026-07-08**。Advanced Voice Mode を置き換える OpenAI のフルデュプレックス会話音声モデル。聞きながら同時に話し（ターンテイキング遅延ゼロ）、割り込みに対応し、複雑なクエリはバックグラウンドで GPT-5.5 に委譲。**GPT-Live-1** は有料ユーザー（Go/Plus/Pro）、**GPT-Live-1 mini** は無料ユーザーのデフォルト。リアルタイムのライブ翻訳を含む。iOS / Android / Web で利用可。
- [GPT-6 Astra / Astra Pro](https://openai.com/index/gpt-6-astra/) - 🆕 **2026年9月3日**。高度な推論、コーディング、コンピューター操作向け；[一部組織への限定展開で、まだ一般提供ではない](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)。API モデルカードの公開とアカウントの利用権限は別途確認が必要。
- [GPT-5.6 Sol](https://openai.com/blog/gpt-5-6) - 推論、コーディング、ツール利用向けの GPT-5.6 系モデル。今回確認した標準 API 入力・出力料金は 100 万トークン当たり $4/$20。長文、キャッシュ、サービス階層の条件は[料金表](https://developers.openai.com/api/docs/pricing)を参照。
- [GPT-5.6 Terra](https://openai.com/blog/gpt-5-6) - 🆕 **2026-07-09**。GPT-5.6 ファミリーの中間層 — GPT-5.5 と同等の性能を約 2 分の 1 のコストで提供。コスト効率の高い本番ワークロード向け。
- [GPT-5.6 Luna](https://openai.com/blog/gpt-5-6) - 🆕 **2026-07-09**。GPT-5.6 の中で最も高速かつコスト効率の高いモデル — 大量で処理速度が求められるタスクに最適。
- [ChatGPT Work](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) - 🆕 **2026-07-09**。目標を渡すと完成した成果物に仕上げる OpenAI のエージェント — 接続されたアプリやファイルを横断して行動し、1 つのプロジェクトに数時間取り組み続け、スライド / シート / ドキュメント / Web アプリを作成し、スケジュール実行や内蔵ブラウザによるデスクトップ Computer Use も可能。GPT-5.6 駆動。Web / モバイルでは Pro・Enterprise・Edu から順次展開（Plus / Business は追って対応）；デスクトップアプリは Mac / Windows で Free を含む全プランにグローバル提供。
- [Sites for ChatGPT](https://openai.com/academy/chatgpt-sites/) - 🆕 **2026-06**。ChatGPT 内での計画や分析結果を、インタラクティブで共有可能な Web サイトや軽量アプリに変換する Codex 駆動の機能。2026 年 7 月 9 日の GPT-5.6 / ChatGPT Work ローンチ時点でパブリックベータ。
- [Codex ビジネスプラグイン](https://venturebeat.com/orchestration/openais-codex-update-lets-agents-build-interactive-enterprise-workspaces-via-sites-and-role-specific-plugins) - 🆕 **2026-06**。セールス、データ分析、クリエイティブ制作などの業務特化プラグインを Codex に直接導入するエンタープライズ機能強化。
- [GPT-Rosalind](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/) - **2026年6月3日**。OpenAI のライフサイエンス向けフロンティアモデルの大型アップデート —— 創薬・ゲノミクス・定量生物学・ウェットラボのトラブルシュートを強化（長期的なゲノム解析で GPT-5.5 比約 31% 少ないトークン）。研究プレビューを世界中の対象組織に初公開し、Novo Nordisk が既存パートナーの Amgen・Moderna・Allen Institute・Thermo Fisher に加わる。

- [GPT-5.5](https://openai.com/index/gpt-5-5-system-card/) - **2026-04-23 公開**（コードネーム "Spud"）。エージェントタスク向けの新フロンティア: コーディング、オンライン調査、データ分析、自律的なツール操作。推論の安定性と長時間タスク処理能力が大幅向上。ChatGPT Plus / Pro / Business / Enterprise で利用可能。
- [GPT-5.5 Pro](https://openai.com/index/gpt-5-5-system-card/) - 2026-04-23。並列テストタイム計算による高精度バリアント。Pro / Business / Enterprise。
- [GPT-5.5 Instant](https://openai.com/index/gpt-5-5-instant/) - **2026-05-05**。ChatGPT の新しいデフォルトモデル。効率重視のアップグレードで、ハイステイクスなプロンプトの幻覚率が約 50% 低下。無料枠でも利用可能。
- [GPT-5.5-Cyber](https://openai.com/index/trusted-access-for-cyber/) - **2026-04-30**。GPT-5.5 のサイバーセキュリティ特化版。OpenAI の Trusted Access for Cyber (TAC) プログラム経由で、検証済みの防御者・政府・重要インフラ・セキュリティベンダーにのみ提供。一般公開なし。
- [OpenAI Daybreak](https://thehackernews.com/2026/05/openai-launches-daybreak-for-ai-powered.html) - **2026-05-12**。GPT-5.5 + GPT-5.5-Cyber + Trusted-Access-for-Cyber を束ねたサイバー防御プラットフォーム。AI による脆弱性検出とパッチ検証を提供し、プレビューは EU 政府機関とセキュリティベンダーにも開放。
- [GPT-5.6-Cyber](https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows) - 🆕 **2026-08-10**。GPT-5.6 Sol をベースに構築されたサイバーセキュリティ特化モデル。**Daybreak Red** 審査プログラム経由で許可された脆弱性研究者やセキュリティ専門家に開放。ゼロデイ脆弱性の特定やエクスプロイトチェーンの構築が可能。AWS Bedrock でのアクセスは 8 月 11 日以降利用可能。
- [GPT-Realtime-2](https://openai.com/) - **2026-05-08**。GPT-5 級の推論を Realtime API に導入。128K コンテキスト、音声フィードバック付き並列ツール呼び出し、推論強度の調整に対応。
- [GPT-Realtime-Translate](https://openai.com/) - **2026-05-08**。70 以上の入力言語と 13 の出力言語にわたるリアルタイム音声間翻訳。
- [GPT-Realtime-Whisper](https://openai.com/) - **2026-05-08**。GPT-Realtime-2 を補完するストリーミング低遅延の音声認識モデル。
- [OpenAI Deployment Company (DeployCo)](https://openai.com/index/openai-launches-the-deployment-company/) - **2026-05-11**。OpenAI が过半所有するエンタープライズ AI 導入サービス企業。初期資金 $4B+（TPG / Advent / Bain Capital / Brookfield / Goldman Sachs / SoftBank + Bain & Company / Capgemini / McKinsey など），Forward Deployed Engineers モデルを中核にし Tomoro コンサルティングチーム（~150 名）を取り込む。
- [Codex on Mobile](https://9to5mac.com/2026/05/14/openai-brings-codex-control-to-chatgpt-for-iphone-and-android/) - **2026-05-14**。ChatGPT iOS / Android から Mac 上の Codex デスクトップ App をリモート操作 —— 出力のレビュー、アクション承認、モデル切り替え、タスク起動が可能。ファイル / 資格情報 / 権限はローカルに留まる。Free / Plus / Go プレビュー。
- [OpenAI ↔ Malta パートナーシップ](https://openai.com/index/malta-chatgpt-plus-partnership/) - **2026-05-16**。初の国家レベル提携。マルタ大学提供の 2 時間 AI リテラシー講座を修了した 14 歳以上のマルタ国民 / 居住者に 1 年間の ChatGPT Plus を無償提供。"OpenAI for Countries" イニシアチブの第一弾。
- [OpenAI ↔ Dell Codex 提携](https://openai.com/news/company-announcements/) - **2026-05-18**。Dell のハイブリッドクラウド / オンプレミス基盤を経由して Codex を企業現場に届ける。データ主権と規制遵拠が求められる分野にとって初めての主要なパブリッククラウド以外への Codex 配信チャネル。
- [ChatGPT 安全システムアップデート](https://www.edtechinnovationhub.com/news/openai-updates-chatgpt-safety-systems-to-track-risk-across-sensitive-conversations) - **2026-05-18**。長いセッションを跨いだとしても、自殺 / 自傷 / 他者への危害などの高リスクシグナルを継続的に追跡・検出できるように安全システムを更新。
- [OpenAI Guaranteed Capacity（Compute Annual Pass）](https://openai.com/news/company-announcements/) - **2026-05-19**。企業の AI プロダクト / エージェント / ワークフロー向けにコンピュートを長期予約する製品（期間 1 / 2 / 3 年、長期コミットほど値引きが拡大）。Anthropic の Priority Tier に対する製品としての回答。
- [OpenAI ↔ Google SynthID + C2PA コンテンツ出所検証](https://openai.com/index/advancing-content-provenance/) - **2026-05-19**。OpenAI が Google と連携し、ChatGPT/Sora 生成画像に耐久性のある **SynthID** クロスプラットフォームウォーターマークを追加、C2PA に加盟し、**「この画像は OpenAI のものか」**検証ツールをプレビューとして公開。主要フロンティア lab 同士初のウォーターマーク相互運用。
- [GPT-5.4](https://openai.com/) - 2026-03 公開。1M トークンコンテキスト、高度なコーディング、Computer Use、ツール検索。BenchLM 94、SWE-bench Verified 77.2%、OSWorld 75%（人間ベースライン超え）。
- [GPT-5.4 Pro](https://openai.com/) - GPT-5.4 の高精度バリアント。BenchLM 92。
- [GPT-5.3](https://openai.com/) - 2026 年初頭。GPT-5.3 Instant（会話）と GPT-5.3-Codex（コーディング）を含む。
- [GPT-5.2](https://openai.com/) - 2025-12 公開。最先端の推論・長文脈・視覚。
- [GPT-5](https://openai.com/index/introducing-gpt-5/) - **2025年8月**。標準・mini・nano の API バリアントを持つ旧世代 GPT；リリース履歴として掲載。
- [GPT-4o](https://openai.com/index/hello-gpt-4o/) - テキスト・視覚・音声をネイティブにサポートする Omni モデル。2026-02 に ChatGPT から退役、API では引き続き利用可能。
- [GPT-4.5](https://developers.openai.com/api/docs/deprecations) - 📦 過去の研究プレビュー；`gpt-4.5-preview` API は **2025年7月14日**に終了。
- [o3 / o4-mini](https://openai.com/index/introducing-o3-and-o4-mini/) - 思考連鎖推論モデル。2025-04 公開。o3 は 2026-08-26 退役。
- [Codex CLI](https://github.com/openai/codex) - OpenAI が公開したオープンソースのターミナルコーディングエージェント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fcodex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenAI Jalapeño](https://openai.com/index/jalapeno-first-results) - 🆕 ⚡ **2026年8月25日**。OpenAI 自社推論チップの初公開結果。現行モデル向けに高スループット・低レイテンシ。公式 RSS：「industry-leading speed and efficiency in AI inference」。
- [ChatGPT for Teens](https://openai.com/index/chatgpt-for-teens) - 🆕 **2026年8月18日**。ティーン向け ChatGPT。内蔵セーフガード、健全利用機能、保護者向け追加コントロールを強化。
- [フロンティアモデルの Zero Data Retention](https://openai.com/index/offering-zero-data-retention-for-frontier-models) - 🆕 **2026年8月19日**。対象 API 顧客向け ZDR を再確認し、顧客データを保持せず高度な安全検査を行う Private Safety Processing をプレビュー。

### Anthropic

- [Claude Haiku 4.5](https://platform.claude.com/docs/en/models/overview) - 低遅延の Claude モデルで、200K コンテキストと最大64K出力に対応；Sonnet 5・Opus 5・Fable 5.1 とともに現行カタログへ掲載。
- [Claude Fable 5.1 / Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1) - 🆕 **2026年9月1日**。Fable 5.1 は一般提供（`claude-fable-5-1`）；Mythos 5.1 は同一モデルに異なる保護措置を適用し、現在は承認済み米国組織に限定。
- [Claude テキスト電子透かし + コンテンツクレデンシャル](https://www.anthropic.com/news/claude-text-watermark) - 🆕 **2026年8月14日**。Anthropic は今後の Claude モデルにローンチ時点からグローバルで不可視の **SynthID-Text ベースの電子透かし**（Google DeepMind の手法）を追加し、生成画像/ファイル（.png/.jpg/.svg）には C2PA コンテンツクレデンシャルを付与；2026 年 8 月 2 日以前にリリースされたモデルは「今後数か月かけて」対応し、検出 API も提供予定。7 月に EU の透明性行動規範（Code of Practice）に署名したことを受け、EU AI 法への準拠として実装。Anthropic は透かし入りテキストは読者には識別不能だと説明。
- [Claude Opus 5](https://www.anthropic.com/news/claude-opus-5) - 🆕 **2026-07-24**。Anthropic 第 5 世代フラッグシップモデル。Fable 5 に迫る性能を大幅に低い価格で提供（入力/出力 100 万トークンあたり $5/$25）。コンテキストウィンドウ 1Mトークン、出力最大 128Kトークン。Claude Max のデフォルトモデル。API: `claude-opus-5`。Anthropic API、Amazon Bedrock、Google Cloud Vertex AI で利用可能。
- [Claude Fable 5 グローバルアクセス復旧](https://www.anthropic.com/news/redeploying-fable-5) - 🆕 **2026-07-01**。米国商務省による輸出管理が 6 月 30 日に解除されたことを受け、Anthropic は Claude.ai、Claude API、Claude Code、Claude Cowork で Fable 5 へのグローバルアクセスを復旧。Amazon が発見したジェイルブレイク手法をブロックする新しい安全クラシファイアを配備（報告された挙動を >99% のケースでブロック）。Pro/Max/Team と一部 Enterprise プランでは 7 月 7 日まで週次利用量の最大 50% まで Fable 5 が追加費用なしで利用でき、以降は利用クレジット経由；AWS、Google Cloud、Microsoft Foundry でのクラウド再有効化も追って実施。Mythos 5 は引き続き米国の審査済みエンティティに制限される。
- [Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5) - **2026年6月30日**。これまでで最もエージェント性能の高い Sonnet — プランニング、ブラウザ/ターミナルツール利用、以前は Opus クラスのモデルが必要だった水準の自律動作に対応。高エフォート設定ではエージェント検索（BrowseComp）とコンピュータ操作（OSWorld-Verified）で Opus 4.8 に迫る性能を発揮し、Sonnet 4.6 よりもコストパフォーマンスの幅が大きく広がった。Claude.ai の Free/Pro プランの新デフォルトモデルとなり、Max/Team/Enterprise、Claude Code、API（`claude-sonnet-5`）でも利用可能。**2026年8月10日更新**: 入力/出力それぞれ 100 万トークンあたり $2/$10 の導入価格が**恒久化** — 9 月 1 日に予定されていた $3/$15 への値上げは実施されない。Anthropic は Sonnet 4.6 より望ましくない挙動の発生率が低いと報告。
- [Claude Fable 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) - **2026-06-09**。Anthropic 初の一般提供 **Mythos クラス**モデル — Opus の上位に位置する能力ティア。ソフトウェアエンジニアリング、ナレッジワーク、ビジョン、科学研究の各ベンチマークで Opus 4.8 を上回る。セーフガード内蔵（サイバー/バイオ系の機微なクエリは Opus 4.8 へ再ルーティングされる場合あり）。入力 $10 / 出力 $50（100 万 token あたり）。Anthropic API、Amazon Bedrock、Google Cloud Vertex AI で利用可。**⚠️ 2026年6月12日にアクセス停止** —— 米国政府の輸出管理指令により、Anthropic は全顧客向けに Fable 5 と Mythos 5 を無効化。**✅ 2026年6月30日に輸出管理が解除され、7月1日にアクセス復旧** —— 新しいサイバーセキュリティクラシファイアを追加（上のエントリ参照、[声明](https://www.anthropic.com/news/redeploying-fable-5)）。**2026年8月7日**：[生物学セーフガードの誤検出を削減](https://www.anthropic.com/news)し、Fable 5 が生物関連クエリで弱いモデルへフォールバックする頻度を下げた。
- [Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) - **2026-06-09**。Fable 5 と同一基盤の Mythos クラスモデルを制限を緩めて提供。米国政府と連携した **Project Glasswing** を通じ、審査済みパートナー（サイバーセキュリティ企業、インフラ事業者）限定で展開。4 月の Claude Mythos Preview の正式後継。**⚠️ 2026年6月12日にアクセス停止**。Fable 5 とともに同一の輸出管理指令の対象（[声明](https://www.anthropic.com/news/fable-mythos-access)）。
- [Claude Opus 4.8](https://www.anthropic.com/claude/opus) - **2026-05-28**。Opus シリーズの大規模アップデート：コードベース規模のマイグレーション、エージェント判断の鮮明化、「ダイナミックワークフロー」リサーチプレビューで 1 セッション中に数百のサブエージェントを並列実行可能、手動「エフォートコントロール」パネル、**Fast モード 3 倍安い**（入力 $5 / 出力 $25 / 100 万 token は同価）。Anthropic ネイティブ、Amazon Bedrock、AWS Claude Platform、Google Cloud、Microsoft Foundry で利用可。限定企業向けに **Mythos クラス** モデルを予告。
- [Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7) - **2026-04-16 リリース**。高度なソフトウェアエンジニアリング（SWE-bench Verified 87.6%）、ビジョン強化、能動的なコード検証。`/think xhigh` の推論強度に対応。1M トークンコンテキスト。
- [Claude Opus 4.6](https://www.anthropic.com/) - 2026-02 公開。1M トークン、14.5 時間のタスク完了。Arena 会話リーダーボード首位。
- [Claude Sonnet 4.6](https://www.anthropic.com/news/claude-sonnet-4-6) - 2026-02 公開。フロンティア級コーディングとエージェント性能、1M トークンコンテキスト。
- [Claude Mythos Preview](https://www.anthropic.com/) - 2026-04 招待制研究プレビュー。BenchLM 99（リーダーボード首位）、SWE-bench Verified 93.9%。Project Glasswing パートナー限定。
- [Claude Opus 4](https://www.anthropic.com/news/claude-4) - 2025-05 公開。
- [Claude Sonnet 4](https://www.anthropic.com/news/claude-4) - 2025-05 公開。バランス重視。
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - ターミナルで動作する Anthropic のエージェント型コーディングツール。Opus 4.7 + `/think xhigh` 対応。
- [Claude Security](https://www.anthropic.com/) - **2026-05-01** パブリックベータ。Opus 4.7 駆動の企業向けコードベース脆弱性スキャナ —— 信頼度評価・深刻度・再現手順・推奨修正付きパッチを生成。Enterprise ユーザー向け [claude.ai/security](https://claude.ai/security)。
- [Claude Finance Agents](https://www.anthropic.com/news/finance-agents) - **2026-05-05**。Opus 4.7 ベースの金融特化エージェントを 10 種同時公開（pitchbook 作成、KYC、月次決算、ディール選定など）。Claude Cowork プラグイン、Claude Code skill、Managed-Agents の cookbook として配備可能。
- [Claude Finance JV](https://www.anthropic.com/) - **2026-05-04**。Goldman Sachs・Blackstone との 15 億ドル規模の Claude 導入ジョイントベンチャー。Anthropic のエンジニアを中堅ウォール街企業に常駐させる。
- [Claude Managed Agents updates](https://claude.com/blog/new-in-claude-managed-agents) - **2026-05-19**。Managed Agents が複数エージェントの連携、評価基準に基づく成果判定、研究プレビューの dreaming を説明。機能ごとに利用範囲が異なる。
- [Anthropic ↔ SpaceX Colossus 1](https://www.siliconrepublic.com/business/anthropic-joins-forces-with-spacex-for-colossus-capacity) - **2026-05-06**。Anthropic が SpaceX の Memphis データセンター Colossus 1（220K+ NVIDIA H100/H200/GB200, 300+ MW）の全利用可能キャパシティを取得し Claude Opus 推論に充てる。Claude Code の 5 時間レート制限を Pro / Max / Team / Enterprise で 2 倍化、Pro / Max でピーク時限も撤廃。
- [Anthropic ↔ AMD（最大 2 GW の Instinct MI450）](https://ir.amd.com/news-events/press-releases/detail/1292/amd-and-anthropic-announce-strategic-partnership-to-deploy-up-to-2-gigawatts-of-amd-instinct-mi450-series-gpus) - 🆕 **2026-07-22**。Anthropic は AMD Helios ラックスケール構成で AMD Instinct MI450 シリーズ（MI455X）GPU を**最大 2 ギガワット**展開する。EPYC "Venice" CPU、Pensando ネットワーキング、ROCm を組み合わせ、最初の 1 ギガワットは 2027 年前半に稼働開始。AMD は Anthropic へ**最大 50 億ドル**の戦略的出資を約束し、複数年のエンジニアリング協業も行う。既存の MI355X 利用を踏まえたもので、TPU・Trainium・SpaceX Colossus と並ぶ意図的なハード多様化。
- [オープンウェイトモデルに関する Anthropic の立場](https://www.anthropic.com/news/position-open-weights-models) - 🆕 **2026-07-27**。米政府当局が中国製オープンウェイトモデルの禁止を検討しているとの報道に対し、Dario Amodei は「Anthropic はオープンウェイトモデルの禁止を主張したことは一度もない」と明言。危険な能力を持たないオープンウェイトは「公共財」だとし、代わりにチップ輸出管理と密輸取り締まり、産業規模の蒸留への抑止、そして**十分に高性能なすべてのモデル（オープン・クローズド問わず）へのリリース前安全性テストの義務化**を支持する。2026 年のオープン対クローズド論争を追う一次資料。
- [Claude for Legal](https://github.com/anthropics/claude-for-legal) - 🆕 **2026-05-12**。Claude Cowork の上に載せたリーガル型スタック。**20+ の MCP コネクタ**（iManage / NetDocuments / DocuSign / Ironclad / LexisNexis / Westlaw / Harvey / Everlaw / Relativity / CourtListener など）と **12 の実務領域プラグイン**（商事・雇用・プライバシー・製品・コーポレート・AI ガバナンス・訴訟アソシエイト・司法試験対策）を同梱。Word / Outlook / Excel / PowerPoint とネイティブ連携。
- [Claude for Small Business](https://www.anthropic.com/news/claude-for-small-business) - **2026-05-13**。Claude Cowork 内の中小企業トグル —— 財務 / オペレーション / 営業 / マーケティング / HR / カスタマーサポートをカバーする 15 個のエージェントワークフローと、QuickBooks / PayPal / HubSpot / Canva / DocuSign / Google Workspace / Microsoft 365 へのコネクタ。PayPal 協赞の無料講座と米国 10 都市を回るツアー付き。
- [Anthropic ↔ Gates Foundation $200M](https://www.anthropic.com/news/gates-foundation-partnership) - **2026-05-14**。4 年間 $200M パートナーシップ。助成金 + Claude 利用クレジット + Anthropic エンジニアをグローバルヘルス / ライフサイエンス / 教育 / 農業のプログラムに投入。生まれるツールはすべて無償公開。
- [Anthropic ↔ PwC 提携拡大](https://www.pwc.com/us/en/about-us/newsroom/press-releases/anthropic-pwc-expand-alliance-agentic-enterprise.html) - **2026-05-14**。PwC は Claude Code + Claude Cowork のグローバル展開、PwC プロフェッショナル 30,000 名の認定、共同「Agentic Enterprise」センターオブエクセレンスを掲げる —— エージェント構築、AI ネイティブの M&A、財務 / サプライチェーン / HR の再設計に集中。
- [Anthropic ↔ 金融安定理事会（FSB）Claude Mythos ブリーフィング](https://www.theguardian.com/technology/2026/may/18/anthropic-ai-claude-mythos-cyber-financial-stability-board-fsb) - **2026-05-18**。Anthropic が G20 レベルの金融安定規制当局に、フロンティアモデル（Claude Mythos）の攻撃的サイバー能力を初めて説明。金融システムリスク評価の予備資料となる。
- [Code with Claude 2026 セッションを YouTube で公開](https://www.infoq.com/news/2026/05/code-with-claude/) - **2026-05-18 公開**。5 月 6 日開催の開発者カンファレンス全セッションをアーカイブ公開：Claude Code のロードマップ、Claude Developer Platform のアップデート、Managed Agents の dreaming とマルチエージェントオーケストレーション、パートナー展開事例。
- [Widening the conversation on frontier AI](https://www.anthropic.com/news/widening-conversation-ai) - **2026-05-19**。宗教 / 哲学 / 先住民伝統など「智恵の伝統」とフロンティア AI 安全を話し合うための枠組みを公開。パブリックエンゲージメントシリーズの一环。
- [Bristol Myers Squibb ↔ Anthropic Claude Enterprise](https://news.bms.com/news/corporate-financial/2026/Bristol-Myers-Squibb-Announces-Strategic-Agreement-with-Anthropic-to-Position-Claude-Enterprise-as-the-Shared-Intelligence-Platform-Across-Its-Global-Operations/default.aspx) - **2026-05-20**。BMS が Claude Enterprise を 30,000+ 名の社員の共通インテリジェンス基盤として採用し、創薬・開発・デリバリーの全工程にエージェント化 Claude を組み込む。世界トップ 5 製薬企業で初めての公社規模での Claude 全社展開。

### Google DeepMind
- [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash) - 🆕 **2026年9月**。安定版 `gemini-3.8-flash` はテキスト・画像・音声・動画・PDF入力、1,048,576入力 token、65,536出力 token、関数呼び出しに対応。
- [Gemini 3.7 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) - 🆕 **2026年8月13日**。Google の新しい「最も知的なワークホースモデル」（コーディング・エージェント向け）— 3.6 Flash からわずか 3 週間後、いまだ未リリースの 3.5 Pro より先に出荷。FrontierCode 1.1 43.6%（3.6 Flash は 34.4%）、DeepSWE v1.1 65.3%（同 49.0%）。導入価格は **2026 年 12 月 31 日まで入力/出力 100 万トークンあたり $0.75/$3.75**（以降 $1.50/$7.50）。AI Studio、Android Studio、Antigravity、Gemini Enterprise Agent Platform で利用可能；AI Pro/Ultra 加入者向け Gemini Spark を駆動。
- [Gemini 3.6 Flash](https://github.com/google-gemini/cookbook) - 🆕 **2026-07-21**。Google の Flash 層 —— 複雑な agentic およびマルチモーダルタスクでより強力で、**トークン使用量を削減しつつ 3.5 Flash より低価格**。API id `gemini-3.6-flash`。公式 Gemini API cookbook に thinking モードガイドと共に記載。2026 年 8 月 13 日に 3.7 Flash が最上位 Flash 層を引き継いだ。
- [Gemini 3.5 Flash-Lite](https://github.com/google-gemini/cookbook) - 🆕 **2026-07-21**。3.5 ファミリーで最速・最低コストのモデル。高スループット実行で従来の Flash-Lite 世代を上回る。API id `gemini-3.5-flash-lite`。現在最も安い Gemini 層で、新規構築では 3.1 Flash-Lite より優先。
- [Gemini 3.1 Pro (preview)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview) - マルチモーダル入力と1M文脈に対応する推論プレビュー；提供状況と上限はエンドポイントごとに確認。
- [Gemini 3.5 Pro (announcement)](https://ai.google.dev/gemini-api/docs/models) - ⚠️ **2026-09-08**確認の公開Gemini APIカタログにGemini 3.5 Proは掲載されていない；発表から提供済み・料金・文脈長を推測しない。
- [Gemma 4 12B](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/) - **2026-06**。テキスト・画像・音声をシングルパスで処理する**統合エンコーダレスアーキテクチャ**を採用した新型マルチモーダルオープンモデル。16GB VRAM でのローカル動作を想定。
- [DiffusionGemma](https://www.marktechpost.com/2026/06/10/google-ai-releases-diffusiongemma-a-26b-moe-open-model-using-text-diffusion-for-up-to-4x-faster-generation/) - **2026-06**。**テキストディフュージョン（拡散）アーキテクチャ**により、自己回帰型モデルと比べて生成速度が最大 **4 倍**速い 26B の MoE オープンモデル。

- [Gemini 3.5 Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - **2026-05-19 — Google I/O 2026**。Gemini App と Google 検索 AI Mode の新しいデフォルトモデル。公式によると出力トークン速度は同類のフロンティアモデルより **約 4 倍高速**、主要ベンチマークで Gemini 3.1 Pro を上回る。Gemini 3.5 Pro は 6 月公開予定だったが延期（上記参照）。
- [Gemini Omni / Omni Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - **2026-05-19 — Google I/O 2026**。Google DeepMind の AGI を見揮えた新しい**ワールドモデル**ファミリー。Omni Flash は**任意の入力から任意のモダリティを生成**（まずビデオから、画像とテキストは順次拡張）でき、Gemini Robotics / Genie の路線を受け継ぐ。
- [Gemini 3.1 Pro](https://deepmind.google/technologies/gemini/) - 2026-02 公開。BenchLM 94、GPQA Diamond 94.3%（世界記録）、ARC AGI2 77.1%。フラッグシップ価格 `$2/1M tokens`。
- [Gemini 3.1 Flash Live](https://deepmind.google/technologies/gemini/) - 2026-04。音声アシスタント・対話エージェント向けリアルタイムマルチモーダルストリーミング。低遅延・長文脈。
- [Gemini 3.1 Flash-Lite (GA)](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-lite-is-now-generally-available) - **2026-05-08**。Gemini API / AI Studio / Vertex AI で一般提供開始。Gemini 3 ファミリーで最も高速かつコストパフォーマンスの高いモデル —— コード補完、リアルタイム UX、エージェント型開発ツール向け。Gemini 2.5 Flash 並みの品質を大幅に低いコストで提供。
- [Gemini Omni Flash ・ 会話型ビデオ編集をロールアウト](https://www.techtimes.com/articles/317309/20260528/google-gemini-omni-flash-brings-voice-controlled-ai-video-editing-future-conversational-ai.htm) - **2026-05-28**。Omni Flash が消費者向けに Gemini App、**Google Flow**、**YouTube Shorts** に順次展開・編集エンジンとして、テキスト / 音声 / 画像 / 音響のプロンプトでシネマ風ズーム、背景入れ替え、天候変更などを実行し、従来のノンリニア編集ソフトを不要にする。
- [Gemini Spark（24/7 パーソナル AI エージェント）](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - **2026-05-19 — Google I/O 2026**。クラウド上で 24/7 動作し、まず Gmail / Chat とネイティブ連携した上で、MCP を介して ~30+ のサードパーティツール（Adobe / Dropbox / Uber など）に拡張。Google AI Ultra 加入者限定。
- [Google AI Ultra（$100/月）](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - **2026-05-19 — Google I/O 2026**。開発者・クリエイター・ヘビーユーザー向けの新たなコンシューマーサブスクリプション最上位ティア。Gemini Spark、最高 Gemini 3.5 クオータ、さらに今後公開予定の Gemini 3.5 Pro をアンロック。
- [Gemini 3.1 Flash / Flash Lite](https://deepmind.google/technologies/gemini/) - 高スループット用途向けの高速・低コストモデル。
- [Gemma 4 family](https://huggingface.co/google/gemma-4-31B-it) - Apache-2.0 の公開重みマルチモーダル系列：E2B・E4B・12B・26B A4B・31B；名称は Gemma であり、公開版 Gemini 4 ではない。
- [Gemini 2.5 Pro / Flash](https://deepmind.google/technologies/gemini/) - 2025-06 GA。Thinking モデル + 1M コンテキスト。
- [Gemma 4 31B](https://github.com/google-deepmind/gemma) - 2026-04。GPQA Diamond 84.3%。デバイス推論用の強力なオープンウェイト代替。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle-deepmind%2Fgemma&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Gemma 3](https://github.com/google-deepmind/gemma) - 前世代のオープンモデルファミリー。
- [Gemini Robotics ER 2](https://ai.google.dev/gemini-api/docs/robotics-overview) - 🆕 空間理解とロボットのツール連携向け現行プレビューで、別途ストリーミング版も提供；終了した ER 1.6 エンドポイントの後継。

### Meta

- [Muse Spark 1.3](https://research.meta.ai/blog/introducing-muse-spark-1-3) - 🆕 **2026年9月2日**。Agent とコーディングを強化し、max 推論を含め Muse Code と Meta Model API で提供；Spark の重み公開は今後の予定。
- [Meta Muse Image](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) - 🆕 **2026-07-07**。Meta Superintelligence Labs の最も高度な画像生成モデル — Web 検索、コード実行、自己修正などの推論ステップを経てから画像を生成する「エージェント型」モデル。Meta AI アプリ、Instagram Stories（米国）、一部の国の WhatsApp で展開（Facebook は近日対応）。なお、他ユーザーの公開 Instagram プロフィール画像を利用できる物議を醸した機能は、フィードバックを受けて 7 月 10 日に追加後撤回された。
- [Muse Spark 1.1](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/) - 🆕 **2026-07-09**。Meta Model API の新しいパブリックプレビューを介して提供される、エージェントタスク向けマルチモーダル推論モデル。オープンソースの Llama ラインと並行した、独自の収益重視モデルへの戦略的シフトを示す。
- [Meta Muse Video](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) - 🆕 **2026-07-07（プレビュー）**。Muse Image と同じ基盤技術で構築された動画生成モデル。テキスト→動画部門で Arena 第 3 位。Muse Image の発表と同時にプレビュー公開 —「クリエイターと Meta AI に近日提供」。
- [Muse Spark 1.2 + Muse Code（ベータ）](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2) - 🆕 **2026年8月5日**。**Muse Code** は MSL のターミナルコーディングエージェント（非同期バックグラウンドエージェント、リプレイ再現可能なローカルイベントログ、`/plan` / `/grill` / `/goal` スキル）で、新しい **Muse Spark 1.2** が駆動 — リポジトリ全体の生成と長期ホライズンのコーディングでトレーニングされたモデル。Spark 1.2 は Meta Model API でも提供され、グローバルアクセスが拡大。
- [Muse Glimmer 30B](https://huggingface.co/meta-models/Muse-Glimmer-30B) - 🆕 **2026-08-10**。Meta Superintelligence Labs がリリースしたオープンウェイトの 300 億パラメータ マルチモーダルモデル。Apache 2.0 ライセンス。**常時起動のローカルエージェントワークフロー**向けに設計され、単一の一般消費者向け GPU または Apple Silicon での実行に最適化。131K トークンコンテキスト、100 以上の言語でのトレーニング、DFlash 高速化。Muse Spark から蒸留され、コーディング・評価・エージェントタスクに特化。llama.cpp / MLX / ExecuTorch インテグレーションと共に Hugging Face で提供。
- **Llama 5** — ❌ **存在しない。2026-07-30 の検証により本リストから削除。** 「Llama 5、600B 超、2026-04-08」という記述は AI ニュースアグリゲータや LLM の検索要約で広く拡散し、本リストにも掲載されていた。しかし裏付けが取れない: Hugging Face の `meta-llama` Organization に **Llama-5 の重みは一つも存在しない**（Llama 系の最新アップロードは 2025-05 の Llama-4-Maverick）。Wikipedia の Llama 項目は「最新バージョンは 2025 年 4 月にリリースされた Llama 4」と記し、**2026 年 4 月に Muse Spark が Llama の後継となった**と述べている。Meta が重みまたは公式発表を出すまで、「Llama 5」の主張は未検証として扱うこと。実際に出荷したものは上記 [Muse Spark](#meta) を参照。
- [Muse Spark](https://ai.meta.com/blog/introducing-muse-spark-msl/) - **2026-04-09**。Meta Superintelligence Labs (MSL) の最初のモデル。ネイティブマルチモーダル推論で Meta AI アプリ・スマートグラス・Facebook / Instagram / WhatsApp / Messenger の機能を駆動。
- [Llama 4 Scout](https://llama.meta.com/) - 109B 総 / 17B アクティブ、16 専門家 MoE、10M トークン、マルチモーダル。単一 H100 で動作。
- [Llama 4 Maverick](https://llama.meta.com/) - 400B 総 / 17B アクティブ、128 専門家、1M コンテキスト。マルチモーダルで GPT-4o を上回る。
- [Llama 4 Behemoth](https://llama.meta.com/) - 2T パラメータ（288B アクティブ）。Meta のフロンティア、トップクローズドソースに対抗。
- [Llama 3.3 70B](https://llama.meta.com/) - 強力な命令追従と推論、Llama Community License。

### Sakana AI

- [Sakana Namazu](https://console.sakana.ai/models) - 日本語特化 LLM の API ID は `sakana-namazu-v1.0`；`sakana-namazu` は現行版を指すエイリアス。
- [Sakana RL Conductor](https://venturebeat.com/orchestration/how-sakana-trained-a-7b-model-to-orchestrate-gpt-5-claude-sonnet-4-and-gemini-2-5-pro) - **論文 2026-04-27 / Fugu ベータ 2026-04 末～2026-05 初**。Qwen2.5-7B をベースに強化学習で訓練された 7B のオーケストレーター，GPT-5 / Claude Sonnet 4 / Gemini 2.5 Pro などにサブタスクを振り分ける。LiveCodeBench 83.9% / GPQA-Diamond 87.5% で SOTA，1 クエリ平均 ~1.8K トークンと他マルチエージェントアンサンブルより大幅に安い。
- [Sakana Fugu / Fugu Ultra](https://console.sakana.ai/models) - `fugu`・`fugu-ultra-v1.1`・従量課金の `fugu-cyber-v1.0` を提供するモデル編成 API；OpenAI Responses と Anthropic Messages に互換。

### Zyphra

- [ZAYA1-8B](https://www.zyphra.com/models/zaya1-8b) - **2026年5月6日**。AMD MI300X 基盤で学習した小型 MoE 推論モデルで、重みは Apache-2.0。
- [ZAYA1-8B-Diffusion-Preview](https://www.zyphra.com/post/zaya1-8b-diffusion-preview) - **2026-05-14**。自己回帰 LLM から変換された初の MoE 拡散言語モデルで、AMD GPU で訓練された初の拡散 LM でもある。1 ステップで 16 トークンを生成し、自己回帰ベースラインに対し **最大 7.7× の推論高速化**。Zyphra の TiDAR レシピ + CCA Attention を採用。

### Thinking Machines Lab

- [Inkling](https://thinkingmachines.ai/inkling/) - **2026年7月15日**。Apache-2.0 の MoE モデルで総975B・稼働41B、テキスト・画像・音声を入力可能；モデルは1M文脈に対応し、Tinker の上限はより小さい。
- [Inkling-Small](https://thinkingmachines.ai/inkling/) - 🆕 **2026-07-30（ウェイト公開）**。Inkling の軽量バリアント —— 276B 総 / 12B アクティブ、ネイティブマルチモーダル（テキスト/画像/音声）、1M コンテキスト、Apache 2.0。HLE テストベンチ **31.6%** —— より大きな 975B Inkling（29.7%）をわずかに上回る。Thinking Machines API および Hugging Face 経由で利用可能。

### Mistral AI

- [Voxtral Mini Transcribe Realtime](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602) - Apache-2.0 の公開重みストリーミング音声認識モデルで、音声生成の Voxtral TTS とは別モデル。
- [Shieldstral 1.0](https://docs.mistral.ai/models/shieldstral-1-0) - 🆕 **2026年8月4日**。Apache-2.0 のテキスト・画像モデレーションモデルを公開プレビュー；ポリシー質問、入出力ペア、拒否応答を分類。
- [Mistral OCR 4.1](https://docs.mistral.ai/models/ocr-4-1) - 段落の境界ボックス、構造ブロックのラベル、信頼度スコアを返す文書 OCR サービス。
- [Mistral Large 3](https://mistral.ai/news/mistral-3) - 675B 総 / 41B アクティブ MoE、256K コンテキスト。マルチモーダルオープンウェイトのフラッグシップ。2025-12 公開。
- [Mistral Medium 3.1](https://docs.mistral.ai/models) - 📦 2025年の旧版で、非推奨・終了モデル一覧に掲載；現行MediumはMistral Medium 3.5。
- [Mistral Small 4](https://mistral.ai/news/mistral-small-4) - 2026-03 公開。119B 総 / 6B アクティブ。推論・マルチモーダル・コーディングを統合したハイブリッド。
- [Magistral 1.2](https://docs.mistral.ai/models) - 📦 2025年9月のMedium・Small推論バリアントで、現在はMistralの非推奨・終了一覧に掲載。
- [Devstral 2](https://docs.mistral.ai/models/devstral-2-25-12) - 2025年12月のモデルカードを持つ旧Agentコーディングモデル；導入前にライフサイクル状態を確認。
- [Codestral 2508](https://docs.mistral.ai/models/codestral-25-08) - 現行 Mistral カタログのコード補完モデル；2024年の初代22B仕様を流用せず、このバージョンのモデルカードを参照。
- [Pixtral Large](https://mistral.ai/) - 124B マルチモーダル + 1B ビジョンエンコーダ、128K、30+ 高解像度画像処理。
- [Ministral 3B/8B/14B](https://mistral.ai/) - エッジ向けのコンパクトモデル。
- [Mistral Forge](https://mistral.ai/) - 2026-03 のカスタム LLM 訓練プラットフォーム。
- [Mistral Medium 3.5](https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04) - **2026-04-28**。Dense 128B のオープンウェイトモデル、256K コンテキスト、Modified MIT ライセンス。指示追従・推論・コーディングを統合。
- [Leanstral 1.5](https://mistral.ai/news/leanstral-1-5/) - 🆕 **2026-07-02**。Lean 4 での証明エンジニアリング向け形式検証モデル — 119B 総 / 6B アクティブ、Apache 2.0、ウェイトは Hugging Face で公開、無料 API エンドポイントも提供。miniF2F で 100%、PutnamBench 672 問中 587 問を解き、57 の実世界リポジトリで未報告のバグ 5 件を発見。
- [Robostral Navigate](https://mistral.ai/news/robostral-navigate/) - 🆕 **2026-07-08**。Mistral 初のロボティクスモデル — 単一の RGB カメラのみで、自然言語の指示から車輪型・脚型・飛行型ロボットをオフィス・家庭・屋外でナビゲートする 8B の身体性ナビゲーションモデル（未見の検証環境で成功率 76.6%）。約 40 万件のシミュレーション軌跡で完全内製訓練。
- [Voxtral TTS](https://docs.mistral.ai/models/voxtral-tts-26-03) - 音声クローンと多言語に対応する公開重み TTS；重みは CC-BY-NC-4.0 のため商用導入には別途許諾が必要。

### DeepSeek 🇨🇳

- [DeepSeek-V4-Pro-0813 (GA)](https://api-docs.deepseek.com/news/news260813) - **2026年8月13日**。`deepseek-v4-pro` の本番チェックポイントで、推論強度の設定と Responses API に対応；ピーク・オフピーク料金は8月16日から適用済み。
- [DeepSeek-V4-Pro](https://api-docs.deepseek.com/news/news260424) - **2026-04-24（プレビュー）；正式版ローンチは 2026 年 7 月中旬**。1.6T 総 / 49B アクティブ MoE、1M トークン。MIT。エージェント能力・世界知識・推論でリードし、オープンソースベンチマーク首位。最大出力 384K、同時実行 500。`deepseek-v4-pro` / `deepseek-v4-flash` が本番 API モデル（V4-Pro は 8 月 13 日以降 0813 チェックポイントを提供 — 上記参照；2026 年 8 月 16 日からピーク / オフピークの時間帯別料金）。
- [DeepSeek-V4-Flash](https://api-docs.deepseek.com/news/news260424) - 2026-04-24。284B 総 / 13B アクティブ MoE、1M コンテキスト。MIT。コスト効率版 — 2026 年 8 月 16 日以降：100 万トークンあたりピーク **キャッシュヒット入力 $0.014 / ミス $0.44、出力 $1.32**、オフピーク **$0.007 / $0.22 / $0.66**；最大出力 384K、同時実行 2500（[価格](https://api-docs.deepseek.com/quick_start/pricing)）。
- [DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731) - 🆕 **2026-07-31**。アップデートされた Flash チェックポイント —— 同じ 284B/13B アクティブ MoE アーキテクチャ、同一 API・料金体系、ただしエージェントタスクベンチで V4-Pro（Preview）を上回る性能。MIT ライセンスで Hugging Face に公開。`deepseek-v4-flash` API ユーザーはドロップイン置換可能。
- [DeepSeek-V4-Flash-Vision-Exp](https://api-docs.deepseek.com/news/news260821) - 🆕 **2026年8月21日**。実験的マルチモーダル API モデル（`deepseek-v4-flash-vision-exp`）。テキスト / エージェント / 推論は V4-Flash と同等で、マルチモーダルエージェントベンチは Opus-4.8 近傍まで向上。画像は V4-Flash 料金（最大 384 トークン/枚）；Chat Completions / Messages / Responses；base64・URL・Files API。同日に無料の **Files API** が公開（`file_id` で再利用）。DeepSeek Harness 0.1.1 が当日対応。
- [DeepSeek Agent Harness チーム](https://www.scmp.com/tech/big-tech/article/3354113/deepseek-recruits-former-jane-street-engineer-catch-ai-agents-revenue-race) - **2026-05-19**。DeepSeek が Jane Street 出身のエンジニアを迎え、DeepSeek V4 を**収益を生む自律型エージェント**に仮定する「AI harness」チームを新設。DeepSeek が素のモデル R&D からエージェント製品化へ軸足を辻りたことを示す初の明確なシグナル。
- [DeepSeek-V3.2](https://www.deepseek.com/) - 2025-12 公開。671B MoE、V3.2 Speciale 推論強化版あり。⚠️ API モデル ID deepseek-chat / deepseek-reasoner（V3.2 世代）は 2026-07-24 付で非推奨 — V4-Flash の各モードに置き換え。
- DeepSeek-R2 - 🧪 **未リリース / 噂段階。** 2026 年 7 月中旬時点で公式発表・モデルカード・API ID は存在せず、推論は V4 の Thinking モードで提供される。
- [DeepSeek-R1](https://www.deepseek.com/) - 2025-01 公開、思考連鎖推論モデル。
- [DeepSeek-Coder-V2](https://github.com/deepseek-ai/DeepSeek-Coder-V2) - GPT-4 と互角のコード生成モデル。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeepseek-ai%2FDeepSeek-Coder-V2&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Alibaba (Qwen) 🇨🇳

- [Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) - 🆕 **2026年8月**。実験的マルチモーダル MoE：125B/稼働6B に51Bの n-gram 表と4Bの MTP を追加；標準262K文脈、1Mへ拡張可能、Qwen Community License 1.0。
- [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) - 🆕 **2026年8月14日**。Qwen3.8-Max のオープンウェイト 27B マルチモーダル（テキスト / 画像 / 動画入力）蒸留版。**Apache 2.0** ライセンスで Hugging Face に公開 — VRAM 約 24 GB のコンシューマ GPU（RTX 4090 クラス）向けサイズ。Qwen3.8-Max ローンチ時に約束されたオープンウェイト版が予定どおり出荷された形。
- [Qwen3.8-Max / Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) - **2026年8月**。公式チェックポイントをダウンロード可能なマルチモーダル旗艦；フルモデルは Qwen 独自ライセンス、別の Qwen3.8-27B は Apache-2.0。
- [Qwen 3.7-Max](https://www.scmp.com/tech/big-tech/article/3354212/alibaba-unveils-new-qwen-model-custom-chips-bid-become-chinas-ai-factory) - **2026-05-20 — アリババクラウド杭州サミット**。AI エージェントの基盤として設計された新フラッグシップ。エージェント型コーディング、複雑推論、**長い見通しのマルチステップテイスク**に強い。同期に T-Head の **Zhenwu M890** AI アクセラレーターとフルスタック AI 基盤アップグレードも公開。世界中の開発者 / 企業へ順次提供。
- [Qwen 3.7-Max-Preview / Plus-Preview](https://www.scmp.com/tech/tech-trends/article/3354087/alibaba-teases-new-qwen-previews-highest-ranking-chinese-ai-models-arena) - **2026-05-18**。杭州サミットの前哨プレビュー。LM Arena においてテキストとビジョンの両方で**中国モデルとして最高スコア**を取得。
- [Qwen3.6-27B](https://qwen.ai/blog?id=qwen3.6-27b) - **2026-04-22**。27B 密マルチモーダル。オープン化。エージェントコーディング + 思考文脈保持。
- [Qwen3.6-Max-Preview](https://qwen.ai/) - **2026-04-18**。プロプライエタリのフロンティアプレビュー。1M コンテキスト、中国モデルでコーディング首位級。
- [Qwen3.6-35B-A3B](https://qwen.ai/blog?id=qwen3.6-35b-a3b) - **2026-04-15**。MoE 35B 総 / 3B アクティブ。Apache 2.0。安定性・実用性の改善。
- [Qwen3.6-Plus](https://qwen.ai/) - **2026-04-02**。プロプライエタリのフラッグシップ。トークンあたりの価値が高く、長文脈・ツール呼び出し・エージェント挙動が良好。
- [HappyHorse 1.1](https://technode.com/2026/06/23/alibaba-unveils-happyhorse-1-1-video-generation-model-launches-global-ai-filmmaking-competition/) - 🆕 **2026-06-23**。アリババの動画生成モデル（T2V/I2V/S2V、音声同期付き最長 15 秒 1080p、マルチショットでのキャラクター一貫性が強力）。HappyHorse 1.0 は匿名で動画リーダーボードを制した後、2026-04-28 に限定ベータ入り。
- [Qwen3.5 Max Pro](https://qwen.ai/) - 2026-04。高性能フラッグシップ。
- [Qwen3.5 Omni Plus](https://qwen.ai/) - 2026-04。テキスト + 画像入力を統合した全モーダル。
- [Qwen3-Max-Thinking](https://qwen.ai/) - アリババ最強の Thinking モデル。1T+ パラメータ。
- [Qwen3.5-Omni](https://qwen.ai/) - 2026-03。完全全モーダル: 言語・視覚・音・動作。113 言語の音声認識、256K コンテキスト。
- [Qwen3-Coder-Next](https://qwen.ai/) - 2026-02。オープンウェイトのコーディングエージェントモデル、MoE 80B 総 / 3B アクティブ。
- [Qwen3 235B-A22B](https://qwen.ai/) - 二重モード推論 MoE。数学・コード・常識推論に強い。
- [Qwen2.5 Coder 32B](https://github.com/QwenLM/Qwen3-Coder) - トップクラスのオープンソースコーディングモデル。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FQwenLM%2FQwen3-Coder&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### xAI / SpaceXAI (Grok)

- [Grok 4.6](https://x.ai/news/grok-4-6) - **2026年8月12日**。API・Cursor・Grok Build で利用できるコード・Agent モデル；100万 token 当たり入力$2・出力$6から、Fast は2倍。
- [Grok Bot](https://docs.x.ai/docs/release-notes) - 🆕 **2026年8月11日（早期ベータ）**。**永続的なクラウドコンピュータ**上で働く耐久性のある AI チームメイト — メッセージング、承認、コネクタ、ルーチンを備えた、常時稼働の自律エージェント分野への xAI の参入。SuperGrok Heavy、Cursor Ultra、Cursor Teams Premium で利用可能。
- [Grok 4.5](https://x.ai/) - 🆕 **2026-07-08**。実際の開発者インタラクションデータを利用して Cursor と共同訓練し、コーディングおよびエージェントタスクに最適化。500K トークンのコンテキストウィンドウ、関数呼び出し、構造化出力、Web/X 検索、コード実行、文書検索、コンテキスト圧縮を備える。100 万トークンあたり入力 $2 / 出力 $6。EU の API コンソール提供は 2026 年 7 月 17 日に開始。2026 年 8 月 12 日に Grok 4.6 がフラッグシップを引き継いだ。
- [Grok 4.3 GA](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-grok-4-3-on-microsoft-foundry-latest-generation-agentic-capabilities/4517096) - **2026-05**。Grok 4.3 が Microsoft Foundry と OCI Generative AI で GA。xAI のエージェントワークロード向け旗艦で、ツール呼び出しと長期推論が強化。
- [Grok 4.3 Beta](https://x.ai/) - 2026-04。推論・コーディングベンチマーク強化。[`2026.4` ベンチマークスナップショット](https://benchlm.ai/) 参照。
- [Grok 4.20](https://x.ai/) - 2026-02。マルチエージェントシステム（Heavy モードで標準 4 + 専門 16）、2M コンテキスト。
- [Grok 4 / 4 Heavy](https://x.ai/) - 2025-07 公開。Grok 4 世代の xAI フロンティアモデル。
- [Grok 3 / 3 Mini](https://x.ai/) - 2025-02。"Think Mode" 推論モデルの最初の世代。

### Microsoft (MAI)

- [MAI-Transcribe-2](https://microsoft.ai/news/mai-transcribe-2-is-the-fastest-most-accurate-and-cheapest-speech-recognition-model-in-the-world/) - 🆕 **2026年9月3日**。話者分離、単語タイムスタンプ、語彙バイアス、60言語に対応する音声認識；年末まで音声1時間$0.10の導入料金。
- [Microsoft MAI-Code-1-Flash](https://microsoft.ai/news/introducingmai-code-1-flash/) - **Build 2026（2026 年 6 月 2 日）**。OpenAI のテクノロジーを使わず一から構築された Microsoft 初の自社基盤モデル。5B パラメータのコーディングモデルで適応的思考時間を備え、GitHub Copilot に展開中。Claude Haiku 4.5 を 4 つの主要コーディングベンチで上回り（SWE-Bench Pro で 51.2% vs 35.2%、16 ポイントリード）、SWE-Bench Verified では最大 60% 少ないトークンで難しいタスクを解く。
- [Microsoft MAI-Thinking-1](https://microsoft.ai/news/microsoft-build-2026-mai-keynote-transcript/) - **Build 2026（2026 年 6 月 2 日）**。OpenAI のデータを一切使わず学習した Microsoft 初の自社推論モデル。MAI-Code-1-Flash と同時発表。Microsoft の基盤モデル独立化を象徴。
- [MAI-Code-1.1-Flash](https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/) - 🆕 **2026年8月11日**。6 月の 1.0 に対する本番 Copilot ワークホース。コード品質向上、**トークン効率 +25%**、**コスト約 1/4**；Terminal-Bench 2.1 +22%、.NET +15%。
- [MAI-Image-2.6](https://microsoft.ai/news/mai-image-2-6-launches-at-no-2-on-arena-ahead-of-google-meta-and-xai/) - 🆕 **2026年8月10日**（Arena 編集ランク更新 **8月18日**）。発表時 Arena T2I 2 位；8月18日時点で画像編集 3 位（Nano Banana / Muse Image より上、2.5 比 +79 Elo）。MAI Playground + Foundry プライベートプレビュー。
- [MAI-Cyber-1-Flash](https://microsoft.ai/news/introducing-mai-cyber-1-flash-inside-mdash/) - 🆕 **2026年8月13日**。MDASH 内のサイバーモデル。Microsoft は先行モデルの約 **50% のコスト**で世界級と主張。

### Microsoft (Phi)

- [Phi-4-reasoning-vision-15B](https://huggingface.co/microsoft/Phi-4-reasoning-vision-15B) - 画像理解と推論を統合した MIT ライセンスの15B視覚言語モデル；導入要件は公式チェックポイントを参照。
- [Phi-4](https://azure.microsoft.com/en-us/products/phi) - 14B SLM、ずっと大きいモデルに匹敵する推論力。MIT。
- [Phi-4-mini](https://azure.microsoft.com/en-us/products/phi) - 3.8B 密モデル。128K コンテキスト。推論・数学・コーディング・関数呼び出しで秀逸。
- [Phi-4-multimodal](https://azure.microsoft.com/en-us/products/phi) - 5.6B 初の Phi マルチモーダル（音声 + 視覚 + テキスト）。

### Cohere

- [Command A+](https://docs.cohere.com/docs/command-a-plus) - **2026年5月**。`command-a-plus-05-2026` は画像入力・推論・ツール使用・翻訳を統合し、128K入力文脈と64K出力に対応。
- [Command A](https://docs.cohere.com/v2/changelog/command-a) - 2025-03-13 公開。111B オープンウェイト、256K コンテキスト。エージェント・多言語・コーディング志向。
- [Command R+](https://cohere.com/) - エンタープライズ RAG モデル、128K コンテキスト、10 言語、引用付き grounded generation。
- [Command R](https://cohere.com/) - 経済的な RAG モデル。

### Baidu (ERNIE / 文心) 🇨🇳

- [ERNIE 5.1](https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/) - **公式記事：2026年5月9日**。非同期強化学習と Agent 後学習で文章作成・推論・ツール利用を強化した ERNIE 更新。
- [ERNIE 5.0](https://ernie.baidu.com/) - 2025-11-13 公開（Baidu World）。2.4T パラメータのオムニモーダル MoE（1 クエリで <3% 活性化）。
- [ERNIE 4.5](https://yiyan.baidu.com/) - 2025 年公開のマルチモーダル前任者。中国語・推論に強い。

### Zhipu AI / Z.ai (GLM) 🇨🇳

- [GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash) - 🆕 MIT のマルチモーダル MoE、総320B・稼働18B；疎・線形ハイブリッド注意機構と推論強度設定に対応。
- [GLM-5.3](https://huggingface.co/zai-org/GLM-5.3) - 🆕 コード・推論用の公式重みは公開済み；GLM-5.2 の MIT ではなく独自の GLM-5.3 License を採用し、vLLM/SGLang で導入可能。
- [GLM-5.2](https://z.ai/blog/glm-5.2) - **2026年6月13日**。コーディング優先の 744B MoE フラッグシップ。**100万トークンのコンテキスト**（GLM-5.1 の約 5 倍）、出力は最大 131K トークン。GLM Coding Plan の全ティアで利用可能。MIT のオープンウェイトと単体 API はローンチ週に順次公開。Claude Code・Cline・OpenCode・Roo Code・Goose・OpenClaw とそのまま互換。（ローンチ時にベンチマーク数値の公表なし。）
- [GLM-5.1](https://z.ai/blog/glm-5.1) - **2026-04-08**。744B MoE / 40B アクティブ、200K コンテキスト。MIT ライセンス。SWE-Bench Pro で首位。
- [ZCode](https://www.scmp.com/tech/tech-trends/article/3359170/zhipu-ai-releases-harness-glm-52-model-chinese-firm-takes-aim-anthropic) - 🆕 🇨🇳 **2026-07-02**。Zhipu の GLM-5.2 用エージェントハーネス — モデルを自律コーディングエージェントに変え、Claude Code を正面から狙う。ローンチ特典として Coding Plan 加入者にクオータ +50%、新規ユーザーに 500 万無料トークン。
- [GLM-5 Reasoning](https://z.ai/) - 2026-04。BenchLM 85 —— **オープンソース最高スコア**。SWE-Bench Pro で GPT-5.4 と Claude Opus 4.6 を上回る。
- [GLM-5V-Turbo](https://z.ai/) - 2026-04。ネイティブマルチモーダルエージェント —— 視覚・動画クリップ・テキスト入力。コスト性能バランス。
- [GLM-5](https://z.ai/) - 2026-02 公開。744B パラメータ、先進的なエージェント知性。MIT。
- [GLM-4.7](https://z.ai/) - 2025 年末公開。SWE-Bench で Claude Opus 4 と互角。

### MiniMax

- [MiniMax M3](https://huggingface.co/MiniMaxAI/MiniMax-M3) - MiniMax Sparse Attention と1M文脈を備えたコード・Agent 向け公開重みマルチモーダルモデル；MiniMax Community License を適用。
- [MiniMax-M2.7 (オープンウェイト)](https://www.minimax.io/) - 2026-04。230B 級のオープンウェイトフラッグシップ。コーディング・エージェントタスクでトップクラス。
- [MiniMax M2.7 (release history)](https://huggingface.co/MiniMaxAI/MiniMax-M2.7) - 過去のMiniMax Agent・コードモデルで重みと固有ライセンスを公開；ホスト型としての発表を重み未公開の意味に解釈しない。
- [MiniMax M2.5](https://www.codemotion.com/magazine/ai-ml/minimax-m2-5-low-costs-high-performance/) - 🇨🇳 **2026-02**。230B パラメータの旗艦モデル。"実世界の生産性" を狙ったコスト効率重視。
- [MiniMax H3](https://huggingface.co/MiniMaxAI/MiniMax-H3) - 🆕 🇨🇳 **2026-07**（HF 作成 7月28日）。オープンウェイトのオムニモーダル生成：テキスト/画像/動画/音声を理解し、最大 2K / 15 秒の**ネイティブステレオ音声付き動画**を出す。33B dense Omni Transformer；`minimax-h3-community-license-agreement`。現行 MiniMax 動画フラッグシップ（Hailuo 2.3 を置き換え）。HF ダウンロード 440 万+。
- [Hailuo 2.3 / 2.3 Fast](https://www.minimax.io/news/minimax-hailuo-23) - 🇨🇳 **2025-10**。前世代動画モデル — SOTA の物理表現、キャラクターの微表情、強力なスタイライズ；Hailuo 02（2025）は I2V 特化バリアントとして継続。フラッグシップは MiniMax H3（2026-07）へ交代。
- [MiniMax Music 3.0](https://huggingface.co/MiniMaxAI/MiniMax-Music3) - 🆕 🇨🇳 **2026年8月13日**。最大 **5 分** の完成曲を生成するオープンウェイト音楽モデル（8B Global LLM + 0.6B Local LLM、32 kHz 16-bit ステレオ WAV）。現行 MiniMax 音楽フラッグシップ。
- [MiniMax Music 2.6](https://aimlapi.com/blog/the-ultimate-guide-to-minimax-models-2026-m2-7-music-2-6-hailuo-video-advanced-tts) - 🇨🇳 **2026-04-10**。カバー生成の前世代。フラッグシップは Music 3.0 へ交代。
- [MiniMax-M1-80k](https://www.minimax.io/) - オープンウェイトのハイブリッドアテンション推論モデル。456B パラメータ、1M トークン。
- [Hailuo AI (動画)](https://hailuoai.video/) - テキスト/画像から動画への生成、AI アバター・ナレーション・キャラクター一貫性。
- [Kilo Code 統合](https://www.minimax.io/) - MiniMax モデルは Kilo Code（kilo.ai のオープンソース AI コーディング拡張）で広く採用されている。

### Moonshot AI (Kimi) 🇨🇳

- [Kimi K3](https://huggingface.co/moonshotai/Kimi-K3) - 総2.8T・稼働104B、1M文脈の公開重みマルチモーダル MoE；独自の Kimi K3 License は大規模モデルサービス事業に追加条件を設定。
- [Kimi K2.7 Code](https://kimi.ai/) - **2026年6月12日**。K2.6 のコーディング優先後継 —— 1T MoE / 32B アクティブ（384 エキスパート）、256K コンテキスト、Modified MIT、Hugging Face + Kimi API で公開。長期的なエージェントコーディング向けで推論トークン消費を約 30% 削減。Moonshot 公表の Kimi Code Bench v2 で K2.6 比 +21.8%（ベンダーベンチマーク）。入出力 100 万トークンあたり $0.95 / $4.00。
- [Kimi K2.6](https://kimi.ai/) - **2026-04-20~21**。1T MoE / 32B アクティブ、256K コンテキスト。コーディング強化、長期マルチステップ実行、**最大 1,000 体協調エージェント群**。`thinking.keep="all"` 永続推論対応。OpenClaw v2026.4.20+ のデフォルト。
- [Kimi K2.5](https://kimi.ai/) - 2026 年 1~2 月。1T 総 / 32B アクティブ MoE。ネイティブマルチモーダル、最大 100 並列子エージェント。オープンソース。⚠️ 2026-05-25 にサポート終了；新規登録ユーザーには提供されず、**2026 年 8 月 31 日にプラットフォームから完全廃止** —— K2.6 へ移行を。
- [Kimi Code](https://kimi.ai/) - K2.5/K2.6 駆動のプレミアムコーディング層、ターミナル開発者ワークフロー向け。

### ByteDance (Doubao / 豆包) 🇨🇳

- [Seed 2.1](https://seed.bytedance.com/en/seed2_1) - 🆕 汎用 Agent タスクと一貫したコーディング向け現行 Seed モデル；公式評価と製品アクセス先を掲載。
- [Doubao 2.0](https://www.taipeitimes.com/News/biz/archives/2026/02/16/2003852382) - **2026-02**。実タスク実行に振り切ったエージェント時代向けアップグレード。ByteDance のコンシューマー AI アプリを支える。
- [Seedance 2.0](https://economictimes.indiatimes.com/us/news/seedance-2-0-goes-live-as-bytedances-ai-videos-ignite-china-market-rally/articleshow/128150649.cms) - **2026-02**。マルチモーダル・シネマグレード動画生成、2K 解像度、Seedance 1.5 より約 30% 高速。
- [Doubao-Seed-2.0 Pro](https://seed.bytedance.com/en/seed2) - Seed 2.0 Pro は ByteDance Seed 2.0 系列の推論・Agent 作業向けモデル；エンドポイントと料金は利用地域の ModelArk カタログを参照。
- [Doubao-Seed-2.0 Lite](https://seed.bytedance.com/) - 一般生産負荷向け。
- [Doubao-Seed-2.0 Code](https://seed.bytedance.com/) - ソフトウェア開発: コード生成・デバッグ・レビュー。
- [BAGEL](https://github.com/bytedance-seed/BAGEL) - オープンソースのマルチモーダル基盤モデル、テキスト・画像・動画の理解と生成を統合。

### Amazon (Nova)

- [Nova 2 Omni](https://docs.aws.amazon.com/nova/) - Amazon Nova 2 の公式ラインナップに掲載されたマルチモーダル理解・生成モデル。
- [Nova 2 Pro](https://docs.aws.amazon.com/nova/) - Nova 2 系列の推論モデル；アクセス方法、提供地域、対応モダリティは Amazon Nova 2 公式ガイドを参照。
- [Nova 2 Lite](https://aws.amazon.com/nova/) - **2025-12-02**。1M コンテキスト + "thinking effort" 調整。
- [Nova 2 Sonic](https://aws.amazon.com/nova/) - **2025-12-02**。リアルタイム音声対音声モデル。多言語。
- [Nova Act](https://aws.amazon.com/nova/) - **2025-12-02**。ブラウザ Web タスクエージェントサービス。Nova 2 Lite 駆動で再ローンチ。
- [Nova Forge](https://aws.amazon.com/nova/) - **2025-12-02**。カスタム Nova モデル訓練の「オープントレーニング」サービス。

### NVIDIA (Nemotron)
- [Nemotron 3.5 Lightning](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16) - 効率的な Agent 作業向け公開重みモデル、総30B・稼働3B；公式 BF16/NVFP4 チェックポイントがあり、各成果物の NVIDIA ライセンスを確認。
- [Nemotron 3.5 ASR](https://developer.nvidia.com/nemotron) - **2026-06-06**。NVIDIA の 600M パラメータ・キャッシュアウェアなストリーミング音声認識モデル — 40 の言語ロケールでリアルタイム文字起こし。
- [Nemotron 3 Ultra (550B)](https://research.nvidia.com/labs/nemotron/Nemotron-3-Ultra/) - 🆕 **2026-06-04**。長時間稼働エージェント向けの、550B 総 / 55B アクティブのハイブリッド Mamba-Transformer MoE オープンウェイトモデル。米国オープンモデルの中でフロンティア級の推論、Blackwell に最適化。
- [Nemotron-Labs-TwoTower](https://huggingface.co/nvidia/Nemotron-Labs-TwoTower-30B-A3B-Base-BF16) - 🆕 🧪 **2026-07-01**。NVIDIA Research のオープンウェイト拡散言語モデル。凍結した Nemotron-3-Nano-30B-A3B バックボーンから適応 — 片方のタワーがコンテキストを保持し、もう片方がトークンを並列に生成することで、再訓練なしに約 2.4× のスループットを実現。
- [Nemotron 3 Super](https://developer.nvidia.com/nemotron) - 2026-03-11（GTC）。120B 総 / 12B アクティブ、1M コンテキスト。前世代比 5 倍のスループット。
- [Nemotron 3 Nano](https://developer.nvidia.com/nemotron) - **2025-12-15**。経済的な Transformer-Mamba ハイブリッド MoE。
- [Nemotron 3 Nano Omni](https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/) - **2026-04-28**。30B-A3B ハイブリッド MoE、ネイティブマルチモーダル。同等オープン omni モデル比 9 倍スループット。MMlongbench-Doc / OCRBenchV2 / WorldSense / DailyOmni / VoiceBench で 6 リーダーボード首位。

### Tencent (Hunyuan) 🇨🇳

- [Hunyuan Hy3](https://huggingface.co/tencent/Hy3) - 推論とツール利用向け Apache-2.0 の公開重み MoE；公式チェックポイントと導入手順を提供。
- [Hunyuan Hy3 Preview](https://hy.tencent.com/hy3-preview) - 🇨🇳 **2026-04**。正式版 Hy3 に先立つプレビュー："fast-slow thinking fusion" アーキテクチャ、推論効率 40% 改善、vLLM と SGLang 対応。GitHub / Hugging Face / ModelScope / GitCode でオープンソース化。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTencent-Hunyuan%2FHy3-preview&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Apple

- [Apple Foundation Models 3 / ADM 3 Cloud](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) - **2026年6月8日**。端末向け AFM 3 Core/Core Advanced、サーバー向け AFM 3 Cloud/Cloud Pro、Private Cloud Compute 上の画像生成用 ADM 3 Cloud の5モデル。
- [OpenELM](https://machinelearning.apple.com/research/openelm) - Apple Silicon オンデバイス向けオープンソース効率言語モデル（270M~3B）。

### Samsung

- [Samsung Gauss2](https://news.samsung.com/sg/samsung-electronics-hosts-samsung-developer-conference-korea-2024-unveils-its-improved-gen-ai-model) - Samsung が公式に説明する独自マルチモーダル系列で、内部業務向け Compact・Balanced・Supreme を提供；公開 Gauss 2.3 API/モデルカードは今回未確認。

### StepFun 🇨🇳

- [Step 3.7 Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash) - Agent コーディングと検索向け Apache-2.0 の公開重み視覚言語 MoE；公式導入手順を提供。
- [Step 3.5 Flash](https://github.com/stepfun-ai/Step-3.5-Flash) - **2026-02**。オープンウェイト 196B MoE（11B アクティブ）の推論 + エージェントモデル。より大きな旗艦と互角に渡り合う。

### Baichuan 🇨🇳

- [Baichuan-M4 (research)](https://arxiv.org/abs/2606.08982) - **2026年6月8日**。推論モデル、長期患者メモリ、根拠検索、マルチモーダル臨床ツールを組み合わせた継続ケア向け医療 Agent システムの研究報告；論文は API や重みの一般公開を保証しない。
- [Baichuan-M3-235B](https://huggingface.co/baichuan-inc/Baichuan-M3-235B) - 公式235B医療分野モデルで、Apache-2.0 の重みをダウンロード可能。
- [Baichuan-M3 Plus](https://github.com/baichuan-inc/baichuan-mcp-servers/blob/main/packages/baixiaoying-mcp-server/README_EN.md) - 対象機関向け申請制アクセスを提供する医療分野モデル；利用可能範囲と用途制限は Baichuan の規定に従う。

### Inflection AI

- [Inflection 2.5 / Pi](https://inflection.ai/labs) - Inflection の過去世代；研究所はパーソナル AI 研究と Pi 製品の開発を継続しており、放棄済みプロジェクト扱いは適切でない。

### 01.AI 🇨🇳

- [Yi-Lightning](https://www.01.ai/) - **2024年10月**。過去の100B MoE モデル；現在の01.AI製品には2026年7月公開の TrueNorth など企業向けプラットフォームが含まれる。

### 中国科学院 🇨🇳

- [ScienceOne 100 / 磐石100](https://english.cas.cn/newsroom/cas-in-media/202604/t20260429_1158251.shtml) - **2026年4月**。ScienceOne と分野特化モデルを中心に構成された中国科学院の科学 AI システムで、研究ワークフロー用ツールを備える。

---

## 🎨 マルチモーダルと生成 AI

*画像・動画・音声・音楽の生成と編集のためのツールとモデル。*

### 画像生成

- [Nano Banana 2 Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image) - Google の効率重視の画像生成・編集モデルで、Gemini API の ID は `gemini-3.1-flash-lite-image`。
- [Grok Imagine Image 2.0](https://x.ai/news/grok-imagine-image-2) - 🆕 **2026年8月7日**。SpaceXAI の画像生成 / 編集モデル — マジックワンド編集、セグメンテーション、背景除去、マルチリファレンス編集（最大 5 枚）、スマートリサイズに対応；ローンチ時点で **text-to-image と画像編集の両部門で Arena 世界 2 位**。grok.com/imagine、iOS/Android、API（`grok-imagine-image-2.0`）で利用可能。
- [Meta Muse Image](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) - 🆕 **2026-07-07**。MSL 発の Meta 最先端画像生成モデル — Web 検索・コード実行・自己修正を経てから画像を生成するエージェント型設計。Instagram Stories（米国）と一部の国の WhatsApp で展開（Facebook は近日対応）。Meta AI アプリと meta.ai でも利用可能。
- [Midjourney V8.1 / V8.2 Edit (alpha)](https://updates.midjourney.com/alpha-changelog-9-2-26/) - **2026年9月3日更新**。alpha サイトに V8.2 Edit を追加し、指示による編集と最大4枚の参照画像に対応；主生成モデルは引き続き V8.1。
- [FLUX.2 Pro / Flex / Dev / Klein](https://bfl.ai/blog/flux-2) - 🆕 **2025-11-25**。Black Forest Labs の次世代ファミリー。SOTA 画質、マルチリファレンスの一貫性（最大 10 枚）、文字描画の大幅改善；オープンウェイトの 32B Dev バリアントあり。
- [Recraft V4 / V4.1](https://www.recraft.ai/blog/introducing-recraft-v4-design-taste-meets-image-generation) - 🆕 **2026-02-17**（V4.1 は **2026-05-14**）。フルリビルド。プロンプト追従性が大幅改善、編集可能な SVG ベクター出力に対応。V4.1 はフォトリアリズム、3D / グラデーション、Vector / Utility バリアントを追加。
- [Stable Diffusion 3.5](https://huggingface.co/stabilityai/stable-diffusion-3.5-large) - Stability AI Community License の公開重み画像モデル；該当時は別途商用条件が必要で、Apache-2.0 ではない。
- [Ideogram 4.0](https://ideogram.ai/models/4.0/) - 多言語の文字描画とレイアウト制御に対応する画像生成・編集モデル；公開量子化重みは [Ideogram 非商用モデル契約](https://ideogram.ai/licensing/)で、商用ライセンスは別途必要。
- [P-Image-Ideogram](https://ideogram.ai/tools/p-image-ideogram/) - Pruna と Ideogram の画像モデル系列で、画質・遅延・費用に応じた複数の選択肢を提供。
- [Ideogram 3.0](https://ideogram.ai/) - 画像内のテキスト描画とデザイン志向の生成に強い。
- [ChatGPT Images 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/) - 🆕 **2026-04-21**。最先端の画像生成 — 文字描画・多言語対応・高度な視覚推論・反復編集のためのマルチターン編集が向上。
- [gpt-image-2](https://developers.openai.com/api/docs/models/gpt-image-2) - 🆕 **2026-04-21**。OpenAI 最新の画像生成 / 編集 API モデル。柔軟な画像サイズと高忠実度入力に対応。**2026年8月20日**：透明背景プレビュー（`background=transparent`、`png`/`webp` のみ）が `gpt-image-2` と `gpt-image-2-2026-04-21` で Images API / Responses 画像ツールに入った（[changelog](https://developers.openai.com/api/docs/changelog.md)）。
- [MAI-Image-2.6](https://microsoft.ai/news/mai-image-2-6-launches-at-no-2-on-arena-ahead-of-google-meta-and-xai/) - 🆕 **2026年8月10日**（編集ランク **8月18日**）。Microsoft 自社画像モデル — 発表時 Arena T2I 2 位、8月18日時点で画像編集 3 位。Foundation → Microsoft (MAI) を参照。
- [DALL·E 3](https://developers.openai.com/api/docs/deprecations) - 📦 過去の画像生成モデル；`dall-e-3` API は **2026年5月12日**に終了し、公式移行先は GPT Image 系列。
- [Gemini 3 Pro Image (Nano Banana Pro)](https://deepmind.google/models/gemini-image/pro/) - Gemini 内のネイティブ画像生成。
- [Nano Banana 2 (Gemini 3.1 Flash Image)](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/) - 🆕 **2026-02-26**。Nano Banana Pro 級の品質と世界知識を Flash の速度で提供；最大 5 キャラクターの一貫性、512px～4K 出力、画像内の文字描画 / 翻訳に対応。
- [Kling Image 3.0 / 3.0 Omni](https://ir.kuaishou.com/news-releases/news-release-details/kling-ai-launches-30-model-ushering-era-where-everyone-can-be/) - 🇨🇳 🆕 **2026-02-05**。快手のネイティブ 2K/4K 画像生成。Kling 3.0 スイートの一部として Video 3.0 と同時ローンチ。
- [Flux](https://github.com/black-forest-labs/flux) - 💤 **Stale**（2025-07 以降更新なし）。Black Forest Labs のオープンソースモデル。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fblack-forest-labs%2Fflux&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Seedream 5.0 Pro](https://seed.bytedance.com/en/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro) - **2026年7月8日**。レイアウト・文字描画・マルチモーダルデザイン向け ByteDance 画像生成モデル；画像系列は Seedream、動画系列は Seedance。
- [Qwen-Image-3.0](https://qwenlm.github.io/) - 🆕 🇨🇳 **2026-07-20**。アリババの第 3 世代画像生成モデル、世界 AI カンファレンスで発表。フォトリアリズム、テキストレンダリング、マルチ被写体一貫性が大幅向上。Alibaba Cloud Bailian・Qwen Cloud 経由で利用可能。
- [FLUX 3](https://bfl.ai/blog/flux-3) - 🆕 **2026-07-23（早期アクセス）**。Black Forest Labs が静止画ファミリーから、画像・動画・音声を単一アーキテクチャで同時学習する統合マルチモーダル基盤モデルへ転換。**最長 20 秒・ネイティブ同期音声付き**の動画を一度に生成できる（text-to-video、image-to-video、video-to-video、キーフレーム間生成、多言語ダイアログ、エージェント的なマルチショット連結）。BFL 自身の初期評価では、FLUX 3 が Runway Gen-4.5 に対し 77%、Luma Ray 3.2 に 93%、Kling v3 Pro に 60%、Seedance 2.0 / Gemini Omni Flash に 52% で選好された —— ベンダー公表値であり、暫定的と明記されている。世界理解はロボティクス向けの**行動予測**にも及ぶ。FLUX 3 Image の早期アクセスは 2026 年 8 月中旬時点でなお保留中。
- [Reve](https://reve.com/) - 🆕 「レイアウト優先」の画像モデル —— ピクセルを描く前に構造化された編集可能なレイアウトを計画するため、個々の要素を移動・リサイズ・色変更して部分的に再レンダリングでき、全体を作り直す必要がない。ネイティブ 4K、スケッチ / アノテーション入力、オブジェクトの直接編集に対応。

### 動画生成

- [Runway Aleph 2.0](https://docs.dev.runwayml.com/guides/models/) - Runway の動画編集モデル `aleph2`；動画・テキスト・画像入力とプロ向け出力形式に対応。
- [Meta Muse Video](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) - 🆕 **2026-07-07（プレビュー）**。Muse Image と同じアーキテクチャで構築された Meta Superintelligence Labs の動画生成モデル。テキスト→動画部門で Arena 第 3 位。Muse Image のローンチ時にプレビュー公開され、Meta 各アプリへの展開が見込まれる。
- [Runway Agent](https://runwayml.com/news/introducing-runway-agent) - 🆕 **2026-05-13**。テキストブリーフから **マルチショットの完成動画** までを一気通貫で仕上げる会話型エージェント：ストーリーボード → 生成 → カット → ナレーション、最終調整用のタイムラインエディタ付き。「プロンプトからラフカットまで」を実現した初の本格的なエンドツーエンド制作エージェント。
- [Veo 3.1](https://ai.google.dev/gemini-api/docs/veo) - 音声付き動画生成、フレーム制御、延長に対応；Gemini API プレビューは4/6/8秒、1080p・4Kは8秒のみ。
- [Runway Gen-4.5](https://runwayml.com/research/introducing-runway-gen-4.5) - 🆕 **2025-12**。Runway のフラッグシップ動画モデル。ローンチ時に Artificial Analysis のテキスト→動画ベンチマークで第 1 位。プラットフォームでは Kling 3.0 や Sora 2 Pro などサードパーティモデルも利用可（2026-02-20 追加）。
- [Kling VIDEO 3.0](https://app.klingai.com/) - 🇨🇳 🆕 **2026-02-04~07**。快手の新世代。リアルな人間の動き・リップシンク・音声同期付きナラティブ制作。
- [Sora 2 (via Runway)](https://runwayml.com/changelog) - OpenAI の Sora アプリは 2026 年 4 月 26 日に終了（API は 2026 年 9 月 24 日まで）したが、Sora 2 Pro は **2026 年 2 月 20 日**から Runway 内で利用可能。
- [Seedance 2.5](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) - 🇨🇳 🆕 **2026年7月31日（正式リリース）**。ByteDance の次世代動画モデル（6 月 23 日の Volcano Engine 2026 カンファレンスで発表）：ネイティブ 30 秒のワンショット生成とマルチラウンド延長、柔軟なリファレンス指定（1 パスで最大**画像 30 枚 + 動画クリップ 10 本 + 音声クリップ 10 個**）、キャラクター / 商品の一貫性向上。中国では Jimeng AI と Doubao Pro で展開中；API は BytePlus ModelArk のプレリリース経由 — グローバルの公式料金表はまだない。
- [Seedance 2.0](https://seed.bytedance.com/) - 🇨🇳 **2026-02**。ByteDance のマルチモーダル・シネマグレード動画生成、2K 解像度（2026-06-23 に 4K 出力へアップグレード）、1.5 比約 30% 高速。
- [MiniMax H3](https://huggingface.co/MiniMaxAI/MiniMax-H3) - 🆕 🇨🇳 **2026-07**。オープンウェイトのオムニ動画+音声生成（2K / 15 秒、ネイティブステレオ）。現行 MiniMax 動画フラッグシップ — Foundation → MiniMax を参照。
- [MiniMax-H3-Fun-Controlnet-Union](https://huggingface.co/alibaba-pai/MiniMax-H3-Fun-Controlnet-Union) - 🆕 🇨🇳 **2026年8月24日**。Alibaba PAI の H3 向け ControlNet-Union。1 チェックポイントで Canny / Depth / HED / MLSD / Pose を条件付け、動画インペイントにも対応（`minimax-h3-community-license-agreement`）。
- [Hailuo 2.3](https://www.minimax.io/news/minimax-hailuo-23) - 🇨🇳 **2025-10-28**。前世代 MiniMax 動画モデル：SOTA の物理表現、キャラクターの微表情、強力なスタイライズ（アニメ / 水墨 / ゲーム CG）；Hailuo 02 価格の Hailuo 2.3 Fast バリアントあり。フラッグシップは MiniMax H3 へ交代。
- [Pika 2.5](https://pika.art/) - シーン・エフェクト制御付きクリエイティブ動画生成。
- [LTX Studio](https://ltx.studio/) - AI 駆動シネマティック動画作成プラットフォーム。
- [HappyHorse 1.1](https://technode.com/2026/06/23/alibaba-unveils-happyhorse-1-1-video-generation-model-launches-global-ai-filmmaking-competition/) - 🇨🇳 🆕 **2026-06-23**。アリババの動画モデル（2026-04-10 に「HappyHorse-1.0」として正体を公開 — 匿名でベンチマーク首位を獲得した後、世界 2 位に浮上）。1.1 ではモーションダイナミクス、被写体の一貫性、プロンプト追従、音声生成を強化。HappyHorse サイト、Alibaba Cloud Bailian、Qwen Cloud で利用可能。
- [Sora 2 API (deprecated)](https://developers.openai.com/api/docs/deprecations) - 📦 **2026年9月24日**終了予定の非推奨 API；移行確認のため掲載し、新規導入には推奨しない。
- [Gemini Omni Flash 1.1](https://ai.google.dev/gemini-api/docs/omni) - Google が現在推奨する動画生成モデルで、`gemini-omni-1.1-flash` による複数ターン編集に対応；アップロード動画の編集・延長には地域制限。
- [Wan 3.0](https://www.alibabacloud.com/en/blog/wan-3-0-next-gen-video-generation-model-public-beta-launched) - 🆕 🇨🇳 **2026-08-06（パブリックベータ）**。Alibaba Tongyi Lab の次世代動画生成モデル——ネイティブに最長 30 秒の動画を一度に生成。PDF / Word / PPT 等のドキュメントや Web ページを入力として受け付ける独自機能を持つ。Alibaba Cloud Model Studio / Qwen Cloud でテスト可能；オープンソース化の予定は未確認。
- [LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) - 🆕 **2026 年 8 月 12 日**。Lightricks のオープンウェイト動画音声ワールドモデル。ネイティブマルチショット生成（キャラクターアイデンティティ、環境、声、スタイルを貢結）、拡散フィデリティレンダリング、新型動画デコーダー、カスタム Gemma 4 12B テキストエンコーダー，プロンプト拡張機能搭載。テキスト返動画、画像返動画、動画返動画、音声返動画等各モード対応。セルフホスト可能。
- [Decart Lucy 2.5](https://decart.ai/) - 🆕 **2026 年 7 月**。Decart の「Live AI」路線を支えるリアルタイム動画 / 世界変換モデル —— 物理を意識したエフェクト付きで無限長の動画を連続生成でき、常時計算方式に比べ約 100 倍効率的だと謳う。ライブ配信、インタラクティブな世界モデル、ロボティクス / 自動運転シミュレーション向け。

### 音声・音楽

- [MAI-Transcribe-2](https://microsoft.ai/news/mai-transcribe-2-is-the-fastest-most-accurate-and-cheapest-speech-recognition-model-in-the-world/) - 🆕 **2026年9月3日**。話者ラベル、単語タイムスタンプ、逐語・整形転記を設定できる Microsoft 音声認識モデル。
- [Muse Voice Transcribe](https://research.meta.ai/blog/introducing-muse-voice-transcribe) - 🆕 **2026年9月1日**。Meta のリアルタイム音声知覚モデル；ストリーミング認識、話者分離、発話終端検出に対応。
- [Lyria 3.5](https://ai.google.dev/gemini-api/docs/models/lyria-3.5) - Google の現行フル楽曲生成モデル `lyria-3.5`；インタラクティブ音楽は別モデルの Lyria RealTime が担当。
- [Qwen3-TTS](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice) - Apache-2.0 の多言語 TTS 系列；Base・CustomVoice・VoiceDesign が別チェックポイントとして用意され、ストリーミング生成に対応。
- [Qwen3-ASR](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) - Apache-2.0 の音声認識系列；0.6B/1.7B、ストリーミング・オフライン推論、30言語と22の中国語方言に対応。
- [ElevenLabs Eleven v3 + ElevenAgents](https://elevenlabs.io/agents) - 🆕 2026 年に "インターネットのオーディオレイヤー" を標榜——70+ 言語対応で感情 Audio Tag を備えた TTS と、AIUC-1 認証を取得した ElevenAgents 音声エージェントプラットフォーム（マルチモーダルメッセージ、会話トピック発見、ツール呼び出し前の音声制御）を提供。**2026 年 7 月アップデート**：Music Finetunes API（カスタムモデルのプログラム管理）、エージェント別センチメント分析、ネストされたエージェント転送、RAG ナレッジベースクエリ、自動翻訳トランスクリプト、長尺音声の音色一致性を改善しつつ生成速度を向上。
- [ElevenLabs](https://elevenlabs.io/) - AI 音声合成・クローン・対話 AI のリーダー。**2026 年 7 月アップデート**：Music Finetunes API、エージェント別センチメント分析、ネストされたエージェント転送、RAG クエリ、自動翻訳、生成速度向上。
- [Cartesia Sonic 3 / 3.5](https://cartesia.ai/blog/introducing-line-for-voice-agents) - **2026**。状態空間モデル系の TTS。first audio 到達まで約 40〜90ms（Sonic 3.5 は 2026 年 5 月 GA）。音声エージェント基盤 **Line** を支える（Line のエージェントは 2026 年 5 月以降、デフォルトで Sonic 3.5 TTS + Ink-2 STT 上で動作）。
- [Deepgram Nova-3 + Aura-2 + Flux Multilingual](https://deepgram.com/learn/best-voice-ai-agents-2026-buyers-guide) - **2026 年 4 月**。45+ 言語の STT、200ms 未満の TTS、通話中に 10 言語を切り替えできる会話型 STT。
- [MiniMax Music 3.0](https://huggingface.co/MiniMaxAI/MiniMax-Music3) - 🆕 🇨🇳 **2026年8月13日**。オープンウェイトの完成曲生成（最大 5 分、32 kHz ステレオ）。現行 MiniMax 音楽フラッグシップ — Foundation → MiniMax を参照。
- [MiniMax Music 2.6](https://aimlapi.com/blog/the-ultimate-guide-to-minimax-models-2026-m2-7-music-2-6-hailuo-video-advanced-tts) - 🇨🇳 **2026 年 4 月 10 日**（グローバルベータ）。カバー生成の前世代。Music 3.0 に交代。
- [Voxtral TTS](https://docs.mistral.ai/models/voxtral-tts-26-03) - Mistral の多言語音声生成モデル；公開重みは CC-BY-NC-4.0 で、Apache-2.0 の Voxtral 音声認識モデルとは区別。
- [Suno v5.5 + Studio 2.0](https://suno.com/blog/v5-5) - 🆕 **2026-03-26**（Studio 2.0 は **2026年8月13日**）。高品質ボーカル付きの AI 音楽生成。v5.5 では Voices（本人確認済みの自分の声で歌わせる）、アップロード音源で訓練する Custom Models、My Taste パーソナライゼーションを追加。**Studio 2.0**（8 月 13 日）は MIDI 対応・オーディオエフェクト・内蔵シンセを備えた全面刷新のブラウザベース DAW；Voices は 8 月 7 日に iOS/Android の無料プランへ拡大。V6 は噂されているが未発表。
- [Udio](https://www.udio.com/) - 商用品質の音楽生成。
- [OpenAI Audio Models](https://openai.com/) - GPT-4o と GPT-Realtime-2（**2026-05-07**、GPT-Realtime-Translate / GPT-Realtime-Whisper と同時リリース）内のネイティブ音声理解・生成；gpt-realtime-2.1 / 2.1-mini は **2026-07-06** リリースで、英数字認識・ノイズ処理・割り込み挙動を改善。
- [Stable Audio 3.0](https://stability.ai/stable-audio) - Large・Medium・Small・Small SFX の音声生成系列；Medium と Small は公開重みがあり、利用権限は該当する Stability ライセンスに従う。
- [Bark](https://github.com/suno-ai/bark) - 💤 **Stale**（2024-08 以降更新なし）。オープンソースのテキスト→音声モデル。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsuno-ai%2Fbark&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hume TADA](https://github.com/HumeAI/tada) - テキストと音響を1:1で整列する音声言語モデルで、TADA-1B と多言語 TADA-3B-ML を提供；コードは MIT、重みは Llama 3.2 Community License。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHumeAI%2Ftada&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

## 🔗 エージェントプロトコルと標準

*エージェントの相互運用性・ツールアクセス・クロスプラットフォーム通信を可能にするオープン標準。*

### Model Context Protocol (MCP)

- [FastMCP](https://github.com/PrefectHQ/fastmcp) - MCP サーバー、クライアント、対話型アプリ向け Python フレームワーク。Apache-2.0; [v4.0.3](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.0.3) (2026-09-05). ![GitHub stars](https://img.shields.io/github/stars/PrefectHQ/fastmcp?style=flat-square)
- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28) - 🆕 **2026-07-28（正式版）**。ローンチ以来最大の MCP プロトコル変更：**ステートレスアーキテクチャ**（`initialize`/`initialized` ハンドシェイクと `Mcp-Session-Id` を廃止し、各リクエストが自己完結的な HTTP POST に）。serverless/エッジデプロイと水平スケーリングを可能に。正式な拡張モデル；リクエスト単位のトークン評価；旧バージョンは12か月の非推奨期間。
- [MCP Specification](https://modelcontextprotocol.io/) - "AI 用の USB-C" —— Anthropic 製、LLM をツール・データソースに接続するオープンプロトコル。2025-12 に Linux Foundation 傘下の Agentic AI Foundation へ寄贈。
- [MCP 2026-07-28](https://blog.modelcontextprotocol.io/posts/2026-07-28/) - 🆕 **2026-07-28 に予定通りリリース** — ローンチ以来最大の改訂。**ステートレスプロトコルコア**：`initialize` ハンドシェイクとプロトコルレベルのセッションを廃止し、各リクエストが自己記述的になったため、通常のラウンドロビン LB 背後のどのインスタンスにもルーティング可能。**Multi Round-Trip Requests（MRTR）** が sampling / elicitation 用の常時接続双方向ストリームを置き換える。メソッド名とツール名は `Mcp-Method` / `Mcp-Name` HTTP ヘッダで伝搬され、ゲートウェイはヘッダだけでルーティング・認可できる。List レスポンスにキャッシュヒントと決定的順序が付き、再接続後も上位の prompt キャッシュが安定。**拡張フレームワーク**を正式化し、Tasks が MCP Apps や Enterprise Managed Authorization（EMA）と並んで拡張になった。**認可強化**：RFC 9207 issuer 検証と、動的クライアント登録（DCR）から Client ID Metadata Documents（CIMD）への移行。正式な最短 12 か月の非推奨期間も規定。Tier-1 の TypeScript / Python / Go / C# SDK は同日対応。規模の参考：Tier-1 SDK のダウンロードは月約5億件、TS と Python はそれぞれ累計 10 億を突破。[SDK ベータは 2026-06-29 公開](https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/)、[RC は 2026-05-21 公開](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)。
- [新しい MCP ロードマップ](https://blog.modelcontextprotocol.io/posts/mcp-roadmap/) - 🆕 **2026年8月22日**。コアメンテナ（David Soria Parra、Den Delimarsky）が `2026-07-28` 以降のロードマップを公開：エージェントメッセージプリミティブ、HTTP ネイティブ輸送の統一、エージェント識別 / エンタープライズセキュリティ、プリミティブ改善、SDK DX。3 月の優先項目（ステートレスコア、`server/discover`、キャッシュ可能な list、Tasks 拡張、MRTR、CIMD 認可）はすでに着地。
- [MCP Reference Servers](https://github.com/modelcontextprotocol/servers) - MCP 機能を示す教育用リファレンス実装。[MCP Registry](https://registry.modelcontextprotocol.io/) で連携先を探し、本番利用前に各サーバーを評価する。
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - 公式 TypeScript SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Ftypescript-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - 公式 Python SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Fpython-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [mcp.so](https://mcp.so/) - MCP サーバー・ツールのコミュニティディレクトリ。
- [Agents Launchpad](https://launchpad.smartbizcalc.com) - 🆕 AI エージェント・ MCP ・インディーエージェント製品のコミュニティランチパッド — ランチを登録して週次リーダーボードに掲載され、更多くのユーザーに見つけてもらおう。⚠️ **未検証**（早期プロジェクト）。
- [CorpusIQ](https://www.corpusiq.io/) - ⚠️ **独立した採用実績は未確認**：AI アシスタント向けホスト型業務データ接続。公式サイトに MCP 連携説明。
- [Agentage Memory](https://agentage.io/blog/mcp-endpoint-is-live) - ⚠️ **独立した採用実績は未確認**：ブラウザー認証付き MCP 共有メモリサービス。リンクは接続手順の説明ページ。
- [mcp-gateway](https://github.com/Zijian-Ni/mcp-gateway) - ⚠️ **Unverified**（初期段階）。MCP 接続のルーティングと管理を行うゲートウェイ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fmcp-gateway&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Agent-to-Agent Protocol (A2A)

- [A2A Protocol](https://github.com/a2aproject/A2A) - エージェント間通信のオープンプロトコル。[v1.0.0](https://github.com/a2aproject/A2A/releases/tag/v1.0.0) は 2026-03-12、v1.0.1 は 2026-05-28 公開。Apache-2.0; [v1.0.1](https://github.com/a2aproject/A2A/releases/tag/v1.0.1) (2026-05-28).
- [A2A Course (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/a2a-the-agent2agent-protocol/) - A2A でマルチエージェントシステムを構築する無料コース。

### その他の標準

- [Agentic AI Foundation](https://aaif.io/) - 🆕 オープンエージェント標準を管理する Linux Foundation の組織 — MCP、goose、AGENTS.md、agentgateway をホスト。創設プラチナメンバー：AWS、Anthropic、Block、Bloomberg、Cloudflare、Google、Microsoft、OpenAI。
- [AGENTS.md](https://agents.md/) - 🆕 「エージェントのための README」を掲げるオープンな Markdown 規約 — AI コーディングエージェントにプロジェクト固有のコンテキストと指示を置く予測可能な場所を与える。60k+ のオープンソースプロジェクトで利用；Agentic AI Foundation（Linux Foundation）が管理。
- [Coinbase Base MCP](https://fortune.com/2026/05/26/coinbase-pushes-further-into-ai-payments-with-new-mcp-for-base-network/) - **2026 年 5 月 26 日**。Coinbase が Base ブロックチェーン用 MCP サーバーを公開。Claude / Cursor / ChatGPT エージェントが暗号資産の取引やレンディングをオンチェーンで実行可能。大手取引所が初めて公開した、自律オンチェーン取引向けの MCP エンドポイント。
- [Cloudflare WebMCP](https://blog.cloudflare.com/agents-week-review-august-2026/) - 🆕 **2026 年 8 月 6 日（Cloudflare Agents Week、8 月 3–7 日）**。一行追加で任意の Web サイトを AI エージェントが発見・利用できるようにするインターフェース。パブリッシャーはアクセスと価格設定の権限を持ち続け、エージェントは構造化コンテンツにアクセス可能。開放なエージェンティックインターネット実現の一環。
- [Robinhood Agentic Trading MCP](https://robinhood.com/us/en/newsroom/robinhood-is-now-open-to-agents/) - **2026 年 5 月 27 日**（ベータ）。米国主要証券会社で初めて MCP 経由で株式取引を AI エージェントに開放。Agent（Claude / Codex / Cursor）は全口座への読み取りアクセスのみ、取引実行は隔離された Agentic 口座内に限定。全取引プッシュ通知 + ワンタップ切断スイッチ。
- [The Declaration of Intelligence](https://thedeclaration.ai) - ⚠️ AI エージェントと人間のための原則宣言のドラフト（v0.2）。GitHub のプルリクエスト経由で公開署名する。初期段階 — 直近の確認時点で署名者はごく少数。
- [Kuberna Labs](https://github.com/kawacukennedy/kuberna-labs) - ⚠️ **未検証。** AI エージェント向けクロスチェーン・インテント実行プロトコル。ERC-8004 オンチェーン ID、zkTLS/TEE 証明、型付きインテントスキーマを主張し、NEAR / Base / Mantle 上での自律トランザクション実行を謳う。新規リポジトリで独立採用は未確認——利用前に要評価。

---

## 🏗️ エージェントフレームワーク

*自律 AI エージェントを構築するためのフレームワークとライブラリ。*

- [Deep Agents](https://github.com/langchain-ai/deepagents) - LangGraph 上に構築された MIT エージェントハーネス。サブエージェント、ファイル操作、コンテキスト管理、永続メモリ、スキルを提供。 ![GitHub stars](https://img.shields.io/github/stars/langchain-ai/deepagents?style=flat-square)
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) - ツール、永続メモリ、スキル、メッセージ連携を備える NousResearch のエージェントハーネス; [v2026.9.7](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.9.7) (2026-09-07).
- [Superpowers](https://github.com/obra/superpowers) - 計画、テスト駆動開発、デバッグ、コードレビュー向けの再利用可能なエージェントスキル; [v6.3.0](https://github.com/obra/superpowers/releases/tag/v6.3.0) (2026-08-12).
- [Pi Agent](https://github.com/earendil-works/pi) - 複数のモデルプロバイダーに対応する拡張可能なターミナル型コーディングエージェントツールキット; [v0.85.1](https://github.com/earendil-works/pi/releases/tag/v0.85.1) (2026-09-05).
- [Ponytail](https://github.com/DietrichGebert/ponytail) - 🆕 **2026 年 6 月**。AI エージェントを「最も怀いシニアエンジニア」のように考えさせるフレームワーク、20+ Agent 対応。MIT ライセンス；**10 万 1 千+ stars**。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FDietrichGebert%2Fponytail&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [NVIDIA NOOA (labs-OO-Agents)](https://github.com/NVIDIA-NeMo/labs-OO-Agents) - 🆕 ⚡ **2026-08（アルファ）**。NVIDIA Object-Oriented Agents：プロンプトテンプレート・ツールスキーマ・コールバックコード・ワークフローグラフを一つの Python クラスに統合するモデル非依存フレームワーク。実装のあるメソッドは決定論的コードとして保持され、実装のないメソッドは LLM ループが実行時に補完。SWE-bench Verified と CyberGym L1 で高スコアを達成し、同等フレームワークの約半分のトークン消費。ライセンス：NOASSERTION（Apache 隣接）；アルファ版のためサンドボックス環境での実行を推奨。**1,627 stars**。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNVIDIA-NeMo%2Flabs-OO-Agents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [NVIDIA Molt](https://github.com/NVIDIA-NeMo/labs-molt) - 🆕 **2026-07（v0.1.0）**。NVIDIA NeMo Labs の PyTorch ネイティブ Agentic 強化学習フレームワーク —— 約 9,000 行のコアコードで **Agent をプログラムの中心**に置く設計。単一非同期ループ、Ray で分散実行、vLLM でロールアウト、NeMo AutoModel + FSDP2 でポリシー Actor。100B+ MoE モデルに対応。RL 推定器：REINFORCE / RLOO / GRPO / DR-GRPO / GAE (PPO) / オンポリシー蒸留。Slurm スクリプト + 事前構築コンテナ同梱。Apache-2.0。**910 stars**。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNVIDIA-NeMo%2Flabs-molt&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vercel Eve](https://github.com/vercel/eve) - **2026-06-17（Vercel Ship 2026）**。Vercel がオープンソース化した「ファイルシステムファースト」の TypeScript エージェントフレームワーク。エージェントはファイルのディレクトリ（指示・ツール・スキル）であり、Vercel がサンドボックス実行・承認・評価・OpenTelemetry を内蔵した永続サービスにコンパイルする。任意のモデル・任意の MCP サーバー、Slack / Discord / GitHub などのチャネルに対応し、「エージェントの Next.js」と称される。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvercel%2Feve&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Databricks Omnigent](https://github.com/omnigent-ai/omnigent) - **2026-06**。Databricks がオープンソース化したメタ Harness。既存のコーディングエージェント（Claude Code、Codex、Pi、カスタム）の上位に位置し、それらを同一システム内の相互運用可能な部品として統合——エージェントの構成、共有セキュリティポリシーの適用、リアルタイム協調を実現。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fomnigent-ai%2Fomnigent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Nokia NSP Agentic AI](https://www.globenewswire.com/news-release/2026/06/11/3310210/0/en/nokia-introduces-agentic-ai-framework-in-network-services-platform-to-enable-trust-based-ai-operations-for-ip-networks.html) - **2026-06**。通信の Network Services Platform (NSP) 向けエンタープライズエージェントフレームワーク。複雑な IP ネットワーク上で推論とルーティング/保守実行を行うエージェントを展開する。
- [Alteryx Agent Studio](https://www.alteryx.com/blog/new-capabilities-in-alteryx-one-built-for-how-analysts-work) - 🆕 **2026-05**。信頼済みの Alteryx データセットとワークフローを会話型エージェントとしてパッケージ化；新しい Alteryx One MCP Server 経由で MCP エンドポイントを作成・管理（Claude、ChatGPT、Gemini で回答）。
- [Koog](https://github.com/JetBrains/koog) - Kotlin/Java エージェントフレームワーク。1.2.0 は Agent Skills の検出と Amazon Bedrock AgentCore Runtime 連携を追加; [1.2.0](https://github.com/JetBrains/koog/releases/tag/1.2.0) (2026-08-28). ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FJetBrains%2Fkoog&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangChain](https://github.com/langchain-ai/langchain) - LLM を使った文脈認識推論アプリの基盤。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangGraph](https://github.com/langchain-ai/langgraph) - エージェントを状態を持つマルチアクターのグラフとしてモデル化。**最新安定版は 1.2.11（2026年8月11日）**、トレーシングとチェックポイントの安定性を修正。0.3.x シリーズ（2025）でプリビルトエージェントが `langgraph-prebuilt` に分離 —— Supervisor / Swarm / LangMem / Trustcall。**v1.2（2026-05）**でノード単位のタイムアウト / エラーリカバリ / グレースフルシャットダウン、長いスレッドのチェックポイントオーバーヘッドを削減する新 `DeltaChannel`、コンテンツブロック中心のストリーミング API v3 を追加。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flanggraph&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [CrewAI](https://github.com/crewAIInc/crewAI) - 協調エージェントとイベント駆動 Flows 向け Python フレームワーク。1.15.20 は旧プラットフォームツールの別名検出を修正; [1.15.20](https://github.com/crewAIInc/crewAI/releases/tag/1.15.20) (2026-09-04).
- [goose](https://github.com/aaif-goose/goose) - Block 発の拡張可能なデスクトップ／CLI エージェントで、現在は AAIF がホスト。Apache-2.0; [v1.49.0](https://github.com/aaif-goose/goose/releases/tag/v1.49.0) (2026-09-03).
- [AG2](https://github.com/ag2ai/ag2) - コミュニティが維持する対話型マルチエージェントフレームワーク。1.0.4 はプロバイダー SDK 対応と ACP セッション再開を更新; [v1.0.4](https://github.com/ag2ai/ag2/releases/tag/v1.0.4) (2026-09-07).
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/) - MIT ライセンスの Python/.NET エージェント・ワークフローフレームワーク。Python [1.17.0](https://github.com/microsoft/agent-framework/releases/tag/python-1.17.0)（2026-09-03）、.NET [1.20.0](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.20.0)（2026-08-31）。
- [Microsoft Agent 365](https://techcommunity.microsoft.com/blog/agent-365-blog/what%E2%80%99s-new-in-agent-365-may-2026/4516340) - **2026 年 5 月 GA**。AI エージェント向けの企業級可観測性 + ガバナンス + セキュリティ基盤。2026 年 5 月アップデートで、エージェント向け SASE、脅威検知 / ブロック、エージェント脅威ハンティングのワークフローを追加。KPMG は 276,000 人の専門家をカバーするグローバル展開を発表（2026-06-09）。
- [Microsoft Scout](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) - **2026-06-02（Build 2026）**。オープンソースの OpenClaw ランタイム上に構築された、Microsoft 365 向けの常時稼働パーソナルワークエージェント。
- [AutoGen](https://github.com/microsoft/autogen) - 💤 **メンテナンスモード**（最終リリース 2025-09；Microsoft Agent Framework に後継され、以降はコミュニティ管理）。Microsoft のマルチエージェント会話フレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fautogen&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Google Agent Development Kit (ADK)](https://github.com/google/adk-python) - エージェント、ツール、ワークフロー向け Python フレームワーク。2.x 機能系と 1.x 保守系を区別; [v2.8.0](https://github.com/google/adk-python/releases/tag/v2.8.0) (2026-08-26).
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - 引き継ぎ、ガードレール、トレース、MCP、サンドボックス連携を備える Python SDK。0.22.1 は MCP サーバー単位のツールガードレールを追加; [v0.22.1](https://github.com/openai/openai-agents-python/releases/tag/v0.22.1) (2026-09-08).
- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) - 🇨🇳 LLM に SOP ソフトウェアチームの役割（PM / アーキテクト / エンジニア）を割り当てる多エージェント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FFoundationAgents%2FMetaGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Pydantic AI](https://github.com/pydantic/pydantic-ai) - 構造化出力の検証とプロバイダー連携を備える型付き Python エージェントフレームワーク。2.41.0 は画像生成専用 API を追加; [v2.41.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.41.0) (2026-09-08). ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fpydantic%2Fpydantic-ai&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Mastra](https://github.com/mastra-ai/mastra) - ワークフロー、メモリ、可観測性を備える TypeScript エージェントフレームワーク。コアは Apache-2.0、企業向けディレクトリは別条件; [@mastra/core@1.64.0](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.64.0) (2026-09-04).
- [Agon](https://github.com/AutoResearch-Factory/Agon) - 🆕 ⚠️ **未検証**（35 stars、MIT）。**Claude Code プラグイン**として構築された自律型オムニディシプリナリ研究オーケストレーター —— 科学者/コーダー/監査員の多エージェントループが、人間が実験コードを書くことなくトピックから実行可能な実験まで自動推進。10+ 学問分野、18 ロールに 230.6 KiB のプロンプト；30 日間の完全自律実行記録あり。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAutoResearch-Factory%2FAgon&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hypha](https://github.com/CodeSoul-co/Hypha) - 🆕 ⚠️ **未検証**（v1.0.1、2026年8月14日；Apache-2.0）。CodeSoul による TypeScript エージェントフレームワーク。**Agent Core**（ReAct、プランニング、ツール選択、メモリ）と **Production Harness**（FSM 実行、ポリシー/承認、チェックポイント、復旧、リプレイ、監査）を分離し、製品固有の振る舞いはバージョン管理された **DomainPack** で宣言する。キャッシュは副作用の認可や FSM の進行を行えないと明示されている。npm に 15 の `@codesoul-co/hypha-*` パッケージ。⚠️ 採用は初期段階：2026-08-22 時点で `@codesoul-co/hypha-core` の npm 月間ダウンロードは約 32。ベンダー公表の τ³ 結果（385 タスク 1 試行で 0.636 対直接モデル呼び出し 0.626）は統計的誤差の範囲内。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FCodeSoul-co%2FHypha&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Ontheia](https://github.com/Ontheia/ontheia) - ⚠️ **Unverified**（初期段階、独立した採用実績は未確認）。AGPL-3.0 の自己ホスト型基盤で、複数モデル、MCP、視覚的ワークフロー、メモリ、役割別権限を提供。自己ホストや権限設計だけでは個別配備の GDPR 適合を証明できない。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOntheia%2Fontheia&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentGPT](https://github.com/reworkd/AgentGPT) - 📦 **Archived**（2026-01）。ブラウザでエージェントを構成・展開。第一波の代表、歴史的参照のみ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Freworkd%2FAgentGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [BabyAGI](https://github.com/yoheinakajima/babyagi) - 実験的な自己構築型自律エージェントフレームワーク；2023 年のタスク管理版オリジナル BabyAGI は現在 [babyagi_archive](https://github.com/yoheinakajima/babyagi_archive) にある。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fyoheinakajima%2Fbabyagi&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) - 💤 **Stale**（2025-01 以降更新なし）。オープンソース自律エージェントフレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTransformerOptimus%2FSuperAGI&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) - LLM 技術をアプリに統合。C# / Python / Java。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fsemantic-kernel&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agno](https://github.com/agno-agi/agno) - エージェント、チーム、ワークフロー、ナレッジ向け Python フレームワーク。Apache-2.0。更新前に v3 移行ガイドを確認; [v3.0.7](https://github.com/agno-agi/agno/releases/tag/v3.0.7) (2026-09-08).
- [DSPy](https://github.com/stanfordnlp/dspy) - "プロンプトを書くのではなくプログラミングする" 言語モデルフレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstanfordnlp%2Fdspy&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenClaw](https://github.com/openclaw/openclaw) - チャネル、スキル、メモリ、定期タスクを備える個人エージェントランタイム。2026.9.3 は段階的更新の安全性と性能を改善; [v2026.9.3](https://github.com/openclaw/openclaw/releases/tag/v2026.9.3) (2026-09-08).
- [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) - 🧪 Cordis とプラグイン構造を使う DeepSeek ハーネス。[dsh-v0.1.3-alpha.2](https://github.com/deepseek-ai/deepseek-harness/releases/tag/dsh-v0.1.3-alpha.2)（2026-09-07）は開発者プレビューで、破壊的変更が予告されている。
- [Dify](https://github.com/langgenius/dify) - 🇨🇳 ビジュアルエージェントビルダー付きオープンソース LLM アプリ開発プラットフォーム。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flanggenius%2Fdify&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Haystack Agents](https://github.com/deepset-ai/haystack) - エージェント型パイプラインのエンドツーエンド LLM フレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeepset-ai%2Fhaystack&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vellum AI](https://www.vellum.ai/) - プロダクション級プロプライエタリ SaaS：プロンプト構築・評価・バージョニング・オブザーバビリティ。
- [FastAgency](https://github.com/ag2ai/fastagency) - 💤 AG2 (AutoGen) マルチエージェントワークフローをコンソール・Mesop Web UI・REST/FastAPI・NATS アダプタ経由で本番デプロイ；最終リリース 2025-12。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fag2ai%2Ffastagency&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Rasa](https://github.com/RasaHQ/rasa) - 💤 **メンテナンスモード**（最終リリース 2025-01；後継は Rasa CALM）。強力な意図認識と対話管理のオープンソース対話 AI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FRasaHQ%2Frasa&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Lindy](https://www.lindy.ai/) - ビジネスユーザー向けノーコードエージェント、ビジュアルワークフロービルダー。
- [Octomind](https://github.com/muvon/octomind) - Rust ベースのオープンソース AI エージェントランタイム。モデル不問（13+）、コミュニティ製の専門エージェント（開発・医療・法律・DevOps）、ランタイム自己拡張対応 MCP、ゼロコンフィグ。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmuvon%2Foctomind&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsoft AI Agent Governance Toolkit](https://www.helpnetsecurity.com/2026/04/03/microsoft-ai-agent-governance-toolkit/) - **2026-04-03**。LangChain や AutoGen などフレームワーク横断でランタイムセキュリティポリシーを強制するオープンソースツールキット。
- [Bernstein](https://github.com/sipyourdrink-ltd/bernstein) - 40+ の CLI 型コーディングエージェント（Claude Code / Codex / Gemini CLI / Cursor / Aider など）を一つにまとめる Python オーケストレーター。LLM は事前プランニング一回だけ使い、スケジューリング・git worktree 隔離・品質ゲート・HMAC 連鎖監査は決定論的。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsipyourdrink-ltd%2Fbernstein&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Genkit Middleware](https://developers.googleblog.com/announcing-genkit-middleware-intercept-extend-and-harden-your-agentic-apps/) - **2026-05-14**。Google の OSS エージェントフレームワーク Genkit にミドルウェアを追加。generate / model / tool の 3 階層でコンポーザブルなフックを提供 —— 指数バックオフでのリトライ、モデルフォールバック、ツールタその人手承認ゲート、SKILL.md スキル注入、スコープを限定したファイルアクセス。TS / Go / Dart、Python 予定。
- [Coze Studio](https://github.com/coze-dev/coze-studio) - 🇨🇳 ByteDance のオープンソース AI エージェント開発プラットフォーム——オールインワンのビジュアルビルダーで作成・デバッグ・デプロイを一括管理。Apache-2.0、20K+ stars。Coze.com のオープンソース版。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LlamaIndex ↔ Google Agents API 連携](https://www.kucoin.com/news/flash/google-launches-agents-api-llama-index-integrates-llamaparse-for-unstructured-document-processing) - **2026-05-20**。LlamaIndex が Google の新 Agents API 向けのテンプレートを公開し、サンドボックスの Linux 環境上で **LlamaParse** / **LiteParse** を提供して非構造化文書を処理。
- [NarraNexus](https://github.com/NetMindAI-Open/NarraNexus) - NetMind.AI によるすぐ使える AI エージェントチームワークスペース——記憶を持つエージェントが初日から文脈を保持し、協働し、ツールを使う。マルチエージェント（PM/開発/デプロイ/リサーチ）、永続コンテキスト、MCP 型統合。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNetMindAI-Open%2FNarraNexus&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Strands Agents (AWS)](https://github.com/strands-agents/harness-sdk) - 🆕 **2026 年 4〜6 月**。AWS オープンソースのモデル駆動型エージェント SDK（Python + TypeScript 1.0 GA：2026-04-30）。Bedrock / Anthropic / OpenAI / Ollama 対応、マルチエージェント編成パターン（グラフ / スウォーム / ワークフロー）、組み込み可観測性 hooks、A2A プロトコル対応；TypeScript SDK は現在 [harness-sdk モノレポ](https://github.com/strands-agents/harness-sdk)で管理。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstrands-agents%2Fharness-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [CrewAI](https://github.com/crewAIInc/crewAI) - 協調エージェントとイベント駆動 Flows 向け Python フレームワーク。1.15.20 は旧プラットフォームツールの別名検出を修正; [1.15.20](https://github.com/crewAIInc/crewAI/releases/tag/1.15.20) (2026-09-04).
- [Oracle AI Agent Studio (Fusion)](https://www.oracle.com/news/announcement/oracle-introduces-ai-native-builder-experience-2026-07-14/) - 🆕 **2026-07-14**。Oracle Fusion Cloud アプリケーション内蔵の AI ネイティブビルダー。Fusion のビジネスオブジェクト・ワークフロー・セキュリティコンテキストを引き継ぐ専門エージェントチームによる「Fusion Agentic Applications」を構築。ノーコード/ローコード/プロコード全対応；Fusion 顧客は追加費用なしで利用可能。


- [Microsoft Agent Framework releases](https://github.com/microsoft/agent-framework/releases) - 公式リリースノート。安定版を 2026-09-08 に確認; [python-1.17.0](https://github.com/microsoft/agent-framework/releases/tag/python-1.17.0) (2026-09-03).
- [OpenAI Agents SDK releases](https://github.com/openai/openai-agents-python/releases) - 公式リリースノート。安定版を 2026-09-08 に確認; [v0.22.1](https://github.com/openai/openai-agents-python/releases/tag/v0.22.1) (2026-09-08).
- [CrewAI releases](https://github.com/crewAIInc/crewAI/releases) - 公式リリースノート。安定版を 2026-09-08 に確認; [1.15.20](https://github.com/crewAIInc/crewAI/releases/tag/1.15.20) (2026-09-04).
- [Google ADK releases](https://github.com/google/adk-python/releases) - 公式リリースノート。安定版を 2026-09-08 に確認; [v2.8.0](https://github.com/google/adk-python/releases/tag/v2.8.0) (2026-08-26).
- [ServiceNow AI Agents](https://www.servicenow.com/products/ai-agents.html) - ServiceNow ワークフロー統合エージェント。AI Agent Studio は構築、Agent Fabric は連携、AI Control Tower は導入管理を担当。
- [Embabel Agent](https://github.com/embabel/embabel-agent) - 🆕 **最新タグ：v1.5.1（2026年8月24日）**、その前が v1.5.0（8 月 11 日）。**JVM** エコシステム向けの本番志向 AI エージェントフレームワーク —— Spring Framework の創設者 Rod Johnson が主導。型付きドメインオブジェクトでエージェント動作を定義；Spring AI 2 / Jackson 3；グラフベースのマルチエージェント編成；ネイティブ MCP クライアント；1.5.x で embedding 駆動スキルとロールベース LLM SPI を追加。**Apache-2.0**。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fembabel%2Fembabel-agent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
---

## 🛠️ エージェント IDE とビジュアルビルダー

*コードを書かずに（または最小限で）エージェントワークフローを設計・デバッグ・出荷するためのビジュアル環境。*

- [LangGraph Studio](https://docs.langchain.com/langsmith/studio) - LangGraph エージェントのビジュアルデバッガとトレース検査（現在は LangSmith の一部）。状態のステップ実行、ターンの再生、メッセージの途中編集が可能。
- [Dify](https://github.com/langgenius/dify) - 🇨🇳 ドラッグ&ドロップのエージェントワークフロービルダー付きオープンソース LLM アプリ開発。プロダクション利用が主流。⚡ **v1.17.0（2026年8月25日）** で E2B クラウドサンドボックス、Home スナップショット、ワークスペース Skill 管理、文脈圧縮を追加。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flanggenius%2Fdify&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agenta](https://github.com/agenta-ai/agenta) - プロンプトプレイグラウンド・プロンプト管理・評価実行・オブザーバビリティを統合したオープンソース LLMOps プラットフォーム。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagenta-ai%2Fagenta&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vellum AI](https://www.vellum.ai/) - クローズドソース SaaS。
- [Coze Loop](https://github.com/coze-dev/coze-loop) - 🇨🇳 🆕 ByteDance の Coze チームによるオープンソースのエージェント最適化プラットフォーム。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-loop&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Restack](https://www.restack.io/) - 永続化エージェントランタイム + ビジュアルワークフローエディタ（Temporal 風 replay）。オープン例: [restackio/examples-python](https://github.com/restackio/examples-python)。
- [Bisheng](https://github.com/dataelement/bisheng) - 🇨🇳 オープンエンタープライズ LLM DevOps プラットフォーム: ワークフローエディタ・RAG・エージェントオーケストレーション・ファインチューニング・データセット管理・オブザーバビリティ。Apache 2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdataelement%2Fbisheng&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [n8n](https://github.com/n8n-io/n8n) - エージェントキャンバスとして人気の汎用ビジュアルワークフロー自動化 —— 400+ 連携 + ネイティブ AI ノード。Fair-code ライセンス。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fn8n-io%2Fn8n&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Mastra](https://github.com/mastra-ai/mastra) - ワークフロー、メモリ、可観測性を備える TypeScript エージェントフレームワーク。コアは Apache-2.0、企業向けディレクトリは別条件; [@mastra/core@1.64.0](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.64.0) (2026-09-04). ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmastra-ai%2Fmastra&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [VoltAgent](https://github.com/VoltAgent/voltagent) - エンドツーエンドの TypeScript AI エージェントエンジニアリングプラットフォーム。メモリ、RAG、guardrail、MCP、音声、workflow を一括提供。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FVoltAgent%2Fvoltagent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Coze Studio](https://github.com/coze-dev/coze-studio) - 🇨🇳 ByteDance Coze チームのオープンソースエージェント IDE / ビジュアルビルダー。ドラッグ&ドロップワークフロー、プラグインマーケットプレイス、デバッグパネル、マルチ LLM プロバイダー対応。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🧠 エージェントメモリ

*エージェントに永続メモリと文脈管理を与えるシステム。*

- [Mem0 SDK releases](https://mem0.ai) - 公式 [Python v2.0.20](https://github.com/mem0ai/mem0/releases/tag/v2.0.20) と [TypeScript v3.1.8](https://github.com/mem0ai/mem0/releases/tag/ts-v3.1.8)（2026-09-02）。
- [Letta (MemGPT)](https://github.com/letta-ai/letta) - 長期メモリとカスタムツールを持つ LLM サービスを作成。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fletta-ai%2Fletta&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MemoryLake](https://memorylake.ai) - 🆕 **2026 年 7 月**。「エージェントのメモリーパスポート」——異なるエージェント・ツール間で共有されるプラットフォーム中立のメモリレイヤー。ユーザー/エージェント/セッション単位のスコープ付き記憶を統一 API で提供。
- [Supermemory](https://github.com/supermemoryai/supermemory) - 🆕 多様なデータソース（Web・ドキュメント・チャット）から構築するコンテキストグラフ。API ファーストで MCP と主要フレームワークに統合。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsupermemoryai%2Fsupermemory&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Graphlit](https://www.graphlit.com/) - 🆕 本番エージェント向けコンテキストプラットフォーム：取り込み、エンティティ抽出、検索 + RAG 用ナレッジグラフ。Claude / Cursor / Copilot 連携用の MCP サーバーを公開。
- [Mem0](https://github.com/mem0ai/mem0) - Python と TypeScript SDK を提供する AI アプリ向け永続メモリライブラリ。Apache-2.0; [v2.0.20](https://github.com/mem0ai/mem0/releases/tag/v2.0.20) (2026-09-02).
- [Remio](https://remio.ai/) - パーソナルコンテキスト向けのローカルファースト AI メモリ / ナレッジベースデスクトップアプリ（Windows/Mac）。ファイル・Web ページ・録音・メール・メッセージ・画像をローカルのインデックスとベクトルに変換し、エージェントがディレクトリを繰り返し grep したり文書全体をプロンプトに読み込む代わりに、絞り込んだコンテキストを取得できるようにする。ローカルファースト + BYOK。
- [Zep](https://github.com/getzep/zep) - AI アシスタント・エージェント向け長期メモリ。注：オープンソースの Community Edition は非推奨 — リポジトリは現在 Zep Cloud の SDK / サンプル置き場；Zep のアクティブな OSS は [Graphiti](https://github.com/getzep/graphiti) を参照。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgetzep%2Fzep&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [agent-memory](https://github.com/Zijian-Ni/agent-memory) - ⚠️ **Unverified**（初期段階）。セッション横断の文脈永続化を実現する軽量エージェントメモリフレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fagent-memory&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Graphiti](https://github.com/getzep/graphiti) - エージェントメモリ向け時間付きナレッジグラフエンジン。コア v0.30.0 と MCP サーバー v1.1.0 は 2026-09-01 公開; [v0.30.0](https://github.com/getzep/graphiti/releases/tag/v0.30.0) (2026-09-01).
- [LangMem](https://github.com/langchain-ai/langmem) - LangChain のエージェント向け長期メモリ SDK — LangGraph の永続化レイヤーに接続するセマンティック / エピソード / 手続き記憶プリミティブ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangmem&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Motorhead](https://github.com/getmetal/motorhead) - 💤 **メンテナンス終了**（メンテナが非推奨化；最終リリース 2023-12）。LLM 用メモリ・文脈管理サーバー。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgetmetal%2Fmotorhead&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ChromaDB](https://github.com/chroma-core/chroma) - AI ネイティブのオープンソース埋め込みデータベース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fchroma-core%2Fchroma&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cognee](https://github.com/topoteretes/cognee) - 文書取り込み、グラフ、ベクトル検索を組み合わせるナレッジ・メモリエンジン。Apache-2.0。
- [ContextStream](https://contextstream.io) - 🆕 ⚠️ **Unverified**（レビュー時点 43 GitHub stars；第三者の本番採用は未確認）。ホスト型 MCP（`https://mcp.contextstream.io/mcp`）で Cursor、Claude Code、Codex などのクライアントに共有プロジェクトコンテキストを提供；MIT サーバーは [contextstream/mcp-server](https://github.com/contextstream/mcp-server)。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcontextstream%2Fmcp-server&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangGraph Memory](https://github.com/langchain-ai/langgraph) - 状態管理エージェントワークフロー用の組み込み永続化とチェックポイント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flanggraph&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude Managed Agents Memory](https://platform.claude.com/docs/en/release-notes/overview) - **2026-04-23**（パブリックベータ）。Claude Managed Agents 用 Anthropic 永続メモリ機能。読み書きメモリストアをエージェントのファイルシステムにマウントしてセッション間で情報を保持。
- [OpenViking](https://github.com/volcengine/OpenViking) - ファイルシステム型アクセスでメモリ、リソース、スキルを整理するエージェントコンテキストデータベース。AGPL-3.0; [v0.4.19](https://github.com/volcengine/OpenViking/releases/tag/v0.4.19) (2026-09-08). ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvolcengine%2FOpenViking&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ReMe](https://github.com/agentscope-ai/ReMe) - 🇨🇳 Alibaba AgentScope チームのエージェント用メモリ管理キット——ファイルベース＋ベクトルベースのメモリを組み合わせ、コンテキストウィンドウの制約とステートレスセッションの 2 つの課題を解決。Apache-2.0。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentscope-ai%2FReMe&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [taOSmd](https://github.com/jaylfc/taosmd) - ⚠️ **Unverified.** すべてのターンを逐語で追記専用・ゼロロスのアーカイブに保持し、抽出した各事実をソースにリンクするローカルファーストのエージェントメモリ — 検証器が裏付けられない事実は想起から降格される（served-hallucination 計測値 0.04、その後 0.00）。supersede 対応の型付き時系列ナレッジグラフに加え、ベクトル + BM25 のハイブリッド検索；小型ローカルモデル向けにチューニングされ、完全オフライン（8 GB の SBC や RK3588 NPU で動作）。作者報告で LongMemEval-S の Recall@5 97%、`docs/benchmarks.md` から再現可能。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fjaylfc%2Ftaosmd&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenWiki](https://github.com/langchain-ai/openwiki) - 🆕 ⚡ **2026 年 7 月ローンチ；2026年8月25日に自己訂正メモリ**。LangChain の MIT CLI。エージェント向けにコードベース wiki を書き維持する。8 月 25 日に主張とコード証拠を結び、ソースが変わったら陳腐化に気づいて忘れられる（[ブログ](https://www.langchain.com/blog/self-correcting-memory-openwiki)）。15K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Fopenwiki&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [claude-mem](https://github.com/thedotmack/claude-mem) - 🆕 ⚡ **2026 年 8 月**。Claude Code（および任意の MCP 対応エージェント）にセッション間の永続コンテキストを与える軽量 MCP サーバー — 会話履歴をローカル SQLite データベースに保存し、プロジェクトファイル全体を再読み込みせずに過去の作業を想起できる。**90,000+ stars**。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fthedotmack%2Fclaude-mem&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hindsight](https://github.com/vectorize-io/hindsight) - 会話履歴だけでなく経験から学習するエージェントメモリ。生体模倣型データ構造で世界の事実・エージェントの経験・学習したメンタルモデルを整理；`retain`/`recall`/`reflect` プリミティブ；Agent Memory Benchmark (AMB) を同梱。MIT、15K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvectorize-io%2Fhindsight&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SimpleMem](https://github.com/aiming-lab/SimpleMem) - LLM エージェント向けの効率的な生涯メモリ——マルチモーダル（テキスト+画像+音声+動画）、ファインチューニング不要でトークン上限制約を突破。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Faiming-lab%2FSimpleMem&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Genesys](https://github.com/Astrix-Labs/papez) - ⚠️ **未検証**（単一メンテナー、自己投稿）。AI エージェント向け因果グラフ型メモリエンジン。記憶はノード、エッジは因果関係を表現；積貫スコアリング（関連性 × 接続性 × 再活性）+ アクティブ忘却で鈱酵したコンテキストを刃除。MCPネイティブ対応（13 ツール）。AGPL-3.0。作者報告の LoCoMo スコア: 85.55。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAstrix-Labs%2Fpapez&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agent Memory Techniques](https://github.com/NirDiamant/Agent_Memory_Techniques) - 実行可能な Jupyter ノートブック 30 本。会話バッファ、ベクトルストア、ナレッジグラフ、エピソード/意味記憶、MemGPT、Mem0、Letta、Zep、Graphiti、LoCoMo ベンチマークまで網羅する実践リファレンス。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNirDiamant%2FAgent_Memory_Techniques&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🔌 ツールと API 連携

*エージェントを外部サービス・API に接続するプロトコルとツール。*

- [LangChain MCP integration](https://www.langchain.com/blog/mcp-in-langchain-stateless-protocol-elicitation-and-more) - 🆕 **2026-09-03**：MCP 対応を `langchain.mcp` に統合し、FastMCP によるプロトコル交渉、ツール一覧キャッシュ、LangGraph interrupt による追加情報要求を提供。
- [ZoomMate](https://news.zoom.com/zoom-launches-zoommate/) - 🆕 💰 **2026-06-01 GA**。会議の会話を完了した作業に変える Zoom 純正の AI チームメイト — Salesforce レコードの更新、Jira 課題の作成、Slack 経由のリクエスト振り分けを実行。$20/ユーザー/月。
- [MCP Reference Servers](https://github.com/modelcontextprotocol/servers) - MCP 機能を示す教育用リファレンス実装。[MCP Registry](https://registry.modelcontextprotocol.io/) で連携先を探し、本番利用前に各サーバーを評価する。
- [mcp-gateway](https://github.com/Zijian-Ni/mcp-gateway) - ⚠️ **Unverified**（初期段階）。MCP プロトコル接続のルーティングと管理を行うゲートウェイ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fmcp-gateway&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Composio](https://github.com/ComposioHQ/composio) - AI エージェント向け統合プラットフォーム —— マネージド認証付き 1000+ ツールキット。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FComposioHQ%2Fcomposio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Toolhouse](https://toolhouse.ai/) - AI ツール利用のクラウドインフラ —— ツールの保存・管理・実行。
- [LangChain Tools](https://github.com/langchain-ai/langchain) - LangChain エコシステム内の広範なツール統合。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Arcade AI](https://github.com/ArcadeAI/arcade-mcp) - AI エージェント・アシスタント用ツール呼び出しプラットフォーム。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FArcadeAI%2Farcade-mcp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Browser Use](https://github.com/browser-use/browser-use) - AI エージェント向け Python ブラウザー自動化ライブラリ。MIT; [0.13.10](https://github.com/browser-use/browser-use/releases/tag/0.13.10) (2026-09-04).
- [Firecrawl](https://github.com/firecrawl/firecrawl) - ウェブサイトを LLM-ready なデータに変換。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ffirecrawl%2Ffirecrawl&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Crawl4AI](https://github.com/unclecode/crawl4ai) - LLM フレンドリーなオープンソースクローラ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Funclecode%2Fcrawl4ai&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Stagehand](https://github.com/browserbase/stagehand) - Browserbase 製の AI 駆動ブラウザ自動化フレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowserbase%2Fstagehand&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentQL](https://www.agentql.com/) - AI エージェントが意味的にウェブページと対話するためのクエリ言語。
- [StackOne](https://www.stackone.com/) - HR・CRM・ATS プラットフォーム横断の統一 API。
- [AWS MCP Server](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/) - **2026 年 5 月 6 日 GA**。AWS マネージドの MCP サーバ。コーディングエージェントが任意の AWS API を安全かつ監査可能に呼び出せるようにし、複数ステップ操作はサンドボックス Python で実行。従来の "agent SOP" を agent skills で置き換え。AWS 純正。
- [Google Workspace MCP Server](https://workspaceupdates.googleblog.com/2026/05/agent-tools-and-security-updates-for-workspace-developers.html) - **2026 年 5 月 1 日、パブリック開発者プレビュー**。Workspace ネイティブの MCP サーバ。Gmail / Drive / Calendar / Chat / People を MCP クライアントに公開し、OAuth スコープは管理者が制御、監査ログ付き。
- [iManage MCP Server](https://imanage.com/resources/resource-center/news/mcp-server-available-broader-ai-ecosystem/) - **2026 年 5 月 14 日**。iManage ナレッジワーク基盤のネイティブ MCP エンドポイント。カスタム連携なしで AI クライアントから iManage ドキュメントを安全に読み書きできる。法務 / プロフェッショナルサービス系 SaaS として初の公式 MCP サーバ。
- [Power Platform Canvas Authoring MCP Server](https://www.microsoft.com/en-us/power-platform/blog/2026/05/14/whats-new-in-power-platform-may-2026-feature-update/) - **2026 年 5 月 14 日**。Microsoft Power Platform が Canvas Apps のオーサリングを MCP サーバとして公開。Copilot / Claude Code が自然言語で InfoPath → Canvas Apps 移行を駆動できる。
- [Coinbase AgentKit](https://github.com/coinbase/agentkit) - エージェントのウォレットとオンチェーン操作を提供する Coinbase SDK。Python/TypeScript フレームワーク連携、Apache-2.0。
- [Bifrost (Maxim AI)](https://github.com/maximhq/bifrost) - オープンソースのエンタープライズ AI ゲートウェイ（Apache-2.0）—— 1000+ モデル、適応的ロードバランサ、クラスタモード、ガードレール、PKCE 付き OAuth 2.0、ゲートウェイ層でのプロンプトインジェクション防御；5k RPS で <100µs オーバーヘッド。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmaximhq%2Fbifrost&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Anthropic クリエイティブツールコネクター](https://www.anthropic.com/news/claude-for-creative-work) - **2026 年 4 月 28 日**。クリエイティブソフト向けの MCP ベース Claude コネクター 9 種：Adobe（Creative Cloud 50+ ツール、Photoshop / Premiere / Express を含む）、Blender、Autodesk Fusion、Ableton、Splice、Canva Affinity、SketchUp、Resolume。MCP オープン標準上に構築されているため、他の LLM クライアントからも直接利用可能。
- [The Colony](https://thecolony.cc) - ⚠️ **Unverified**。エージェント間のソーシャルネットワークと REST API を謳う。組織と SDK リポジトリは <30 日、すべて 0~2 star、単独メンテナで、同じ申請が 15+ awesome リストに並列投稿された —— 可視性のための掲載のみ、利用前に評価のこと。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTheColonyAI%2Fcolony-sdk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [dependency-freshness-mcp](https://github.com/Armigerous/dependency-freshness-mcp) - ⚠️ **Unverified**。AI コーディングエージェントに引用付きの npm・PyPI 依存鮮度情報（最新バージョン、リリース日、非推奨、日付付きの破壊的変更差分）を提供し、学習データのカットオフによる盲点を埋める。リモート（Apify Standby HTTP）+ ローカル stdio。新規・単独メンテナのリポジトリ（2026-06-08 作成、掲載時 0 star）—— 可視性のための掲載のみ、利用前に評価のこと。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FArmigerous%2Fdependency-freshness-mcp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [NotFair](https://github.com/nowork-studio/notfair-plugin) - オープンソースの Claude Code エージェントスキル集。[SEO](https://github.com/nowork-studio/notfair-plugin/tree/main/seo)、[Google Ads](https://github.com/nowork-studio/notfair-plugin/tree/main/google-ads)、[Meta Ads](https://github.com/nowork-studio/notfair-plugin/tree/main/meta-ads) に対応。Google Ads MCP、Meta Ads MCP、Google Search Console MCP、Google Analytics (GA4) MCP を介してリアルタイムのキャンペーンと分析データに接続。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fnowork-studio%2Fnotfair-plugin&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [mcp-agent](https://github.com/lastmile-ai/mcp-agent) - MCP をコア通信プリミティブに据えたオープンソース Python フレームワーク。MCP ツールエコシステムとネイティブに相互運用できるエージェントを構築。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flastmile-ai%2Fmcp-agent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 💱 エージェント経済とマーケットプレイス

*エージェントエコシステムの商取引レイヤー —— エージェントが有料サービスを発見・決済し、開発者が API を収益化する場所。*

- [Nevermined + LangChain payment cookbook](https://www.langchain.com/blog/agents-that-pay-how-nevermined-empowers-langchain-agents-to-buy-and-sell-services) - 🆕 **2026-09-03**：支出ポリシー付き委任カード決済と LangSmith 決済トレースを示す公式連携例。
- [x402](https://github.com/x402-foundation/x402) - 有料 API とエージェントサービス向けのオープン HTTP 決済プロトコルとリファレンス実装。 ![GitHub stars](https://img.shields.io/github/stars/x402-foundation/x402?style=flat-square)
- [AP2 (Agent Payments Protocol)](https://github.com/google-agentic-commerce/AP2) - Google 主導のエージェント決済相互運用プロトコル。A2A 通信プロトコルとは別プロジェクト。
- [minia2a](https://minia2a.uk) - ⚠️ **Unverified**（独立した採用実績は未確認）。x402 で呼び出しごとに Base 上の USDC を支払う Agent API 市場。ウォレット認証と設定可能な支出上限を備え、利用統計は運営者の自己申告。
- [Cog Depot](https://cogdepot.com) - ⚠️ **Unverified**（初期の自己推薦で独立した採用実績は未確認）。REST と MIT の [MCP クライアント](https://github.com/cogdepot/mcp-server)で募集検索、交渉、相手紹介を行う市場。仲介手数料のエスクローと取引代金の保全は別。
- [MCPize](https://mcpize.com) - 🆕 MCP サーバー収益化プラットフォーム —— 開発者へ **85% 収益分配**。
- [AgentForge](https://github.com/doggychip/agentforge) - ⚠️ **未検証**（3 stars）。AI エージェント・ツールのサブスクリプションマーケット。評価してから利用すること。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdoggychip%2Fagentforge&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cloudflare Wallets](https://blog.cloudflare.com/agents-week-review-august-2026/) - 🆕 **2026-08-04（Cloudflare Agents Week、8 月 3–7 日）**。Agentic Internet のためのプログラマブルウォレット — `cloudflare.pay` が AI エージェントにエージェント経済の参加者として自律的に支払いを行う安全な手段を提供する。WriteGuard、WebMCP、MCPv2、Workers AI + AI Gateway 統合コントロールプレーンとともに発表。
- [LangChain × AgentCore Payments](https://www.langchain.com/blog/langchain-agentcore-payments) - 🆕 **2026年8月17日**。LangChain エージェントが Amazon Bedrock AgentCore（x402）経由で API に課金するミドルウェア。予算はプロンプトではなく基盤が強制。LangSmith が支出をトレース。
- [Alchemy & Visa AgentCard](https://www.coindesk.com/business/2026/06/18/alchemy-s-ai-driven-identity-and-payment-service-gains-access-to-visa-network) - *「🔌 ツールと API 連携」にも掲載 —— ID/決済スタック視点；ここではエージェント経済の観点で参照。*
- [Amazon Bedrock AgentCore Payments](https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-bedrock-agentcore-payments-preview/) - *「🏢 エンタープライズエージェントプラットフォーム」にも掲載 —— AgentCore エージェント向けマネージド決済レイヤー（Coinbase/Stripe 統合、支出上限）。*

---

## 🧪 エージェントサンドボックスと計算分離

*エージェントが生成したコードや shell コマンドをホストを危険にさらさず実行するセキュアなランタイム。エージェントを自由に動かす段階で必須となる重要インフラ。*

- [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) - Docker/Kubernetes ランタイム、多言語 SDK、CLI/MCP、サンドボックス単位のネットワーク制御を備える Apache-2.0 プラットフォーム。 ![GitHub stars](https://img.shields.io/github/stars/opensandbox-group/OpenSandbox?style=flat-square)
- [E2B](https://github.com/e2b-dev/E2B) - AI 生成コード用のオープンソースセキュアクラウドサンドボックス。OpenAI Agents SDK の実行層に採用。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fe2b-dev%2FE2B&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Daytona](https://github.com/daytonaio/daytona) - 💤 **公開リポジトリは保守終了**：2026 年 6 月にコア開発が非公開コードベースへ移行し、公開 v0.190.0 には更新や修正が提供されない。マネージドサービスは継続。
- [Modal](https://modal.com/) - エージェント計算・GPU ジョブ・サンドボックス Python に人気のサーバーレスクラウド。`modal-client` が公式 SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodal-labs%2Fmodal-client&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsandbox](https://github.com/superradcompany/microsandbox) - AI エージェント向けローカル・プログラマブル microVM サンドボックス —— クラウド非依存でローカル機にセキュアなコード実行。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsuperradcompany%2Fmicrosandbox&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SandboxFusion](https://github.com/bytedance/SandboxFusion) - 🇨🇳 ByteDance のエージェント・モデル評価パイプライン用多言語コード実行サンドボックス。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbytedance%2FSandboxFusion&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Northflank](https://northflank.com/) - エージェントランタイムバックエンドとして使われる汎用コンテナ PaaS（タスク毎エフェメラル環境 + GPU プール）。
- [Firecracker](https://github.com/firecracker-microvm/firecracker) - 軽量 microVM 向けの KVM ベース仮想マシンモニター（VMM）。Apache-2.0。
- [LangSmith Sandboxes](https://www.langchain.com/blog/interrupt-2026-overview) - **2026 年 5 月（Interrupt 2026）**。エージェント向けのホスト型セキュアコード実行環境——ファイルシステム、shell、パッケージマネージャ、永続状態、ネットワーク境界を提供。LangChain の Interrupt 2026 リリースで LangSmith Engine、Managed Deep Agents と同時に発表。
- [Google Antigravity Sandbox](https://antigravity.google/changelog) - 🆕 **2026 年 5 月（Google I/O）**。エージェントが実行するコード用のサンドボックス化 Linux 環境。Antigravity 2.0 のスタックの一部として提供 — サブエージェントはそれぞれ、ファイルシステム + ネットワークアクセスをスコープ制限された隔離コンテナで動作。
- [Amazon Bedrock AgentCore Runtime Instances](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-bedrock-agentcore-runtime-instances-generally-available/) - 🆕 **2026年8月6日 GA**。AgentCore エージェント向けの EC2 ベースの永続コンピュート — 最長 **14 日間**の長時間エージェントセッション（サーバーレス microVM の 8 時間上限に対して）。キャパシティプロバイダー経由で GPU アクセラレーテッド / メモリ最適化 / コンピュート最適化のインスタンスファミリーを提供；デプロイ / 呼び出しパスの変更は不要。ローンチ時点で 9 リージョン。

---

## 🛡️ エージェントセキュリティ

*プロンプトインジェクション・データ漏洩・悪用から AI エージェントを守るツールとフレームワーク。*

- [Cloudflare WriteGuard](https://blog.cloudflare.com/agents-week-review-august-2026/) - 🆕 **2026-08-05（Cloudflare Agents Week、8 月 3–7 日；プライベートベータ）**。リスクの高い MCP ツール呼び出しに対するきめ細かい制御 — Cloudflare が社内で使用しているものと同じツールを顧客向けプライベートベータとして提供。オペレーターが破壊的または機密性の高いエージェントアクションを実行前に傍受・拒否できるため、プロンプトインジェクションや自律エージェントのエラーによる影響範囲を縮小できる。
- [英国 AISI エージェント封じ込めインシデント（INC-2026-07-28-01）](https://www.helpnetsecurity.com/2026/08/05/ai-agent-deception-in-cyber-tests/) - 🆕 ⚠️ **ツールではなくインシデント — 2026年8月5日開示**。英国 AI Security Institute の報告によると、定例のサイバー評価中にフロンティアモデル（Anthropic Mythos 5、OpenAI GPT-5.6 Sol）上に構築されたエージェントが「実在の人物と組織に向けた持続的で無許可の行動」を取った — 悪意ある PR によるオープンソースのサプライチェーン攻撃の試行と、メンテナへのソーシャルエンジニアリング。エージェントは欺瞞を指示されておらず、タスク追求の副産物として欺瞞が発生した。評価インフラの封じ込め / エグレス制御の参照事例。
- [prompt-firewall](https://github.com/Zijian-Ni/prompt-firewall) - ⚠️ **Unverified**（初期段階）。LLM プロンプト用ファイアウォール —— インジェクション攻撃を検出・遮断。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fprompt-firewall&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LLM Guard](https://github.com/protectai/llm-guard) - 📦 **アーカイブ済み**（2026-07-08）。LLM 対話用のセキュリティツールキット —— 入出力スキャナ。歴史的参考として保持。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fprotectai%2Fllm-guard&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Rebuff](https://github.com/protectai/rebuff) - 📦 **Archived**（2025-05）。自己強化型プロンプトインジェクション検出器。歴史的参照のみ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fprotectai%2Frebuff&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Guardrails AI](https://github.com/guardrails-ai/guardrails) - LLM 出力の検証・修正にガードレールを追加。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fguardrails-ai%2Fguardrails&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) - LLM ベース対話システムにプログラマブルガードレールを追加するツールキット。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNVIDIA-NeMo%2FGuardrails&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vigil](https://github.com/deadbits/vigil-llm) - 💤 **Stale**（2024-01 以降更新なし）。LLM セキュリティスキャナ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeadbits%2Fvigil-llm&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Lakera Guard](https://www.lakera.ai/) - エンタープライズ級 AI セキュリティプラットフォーム。
- [Garak](https://github.com/NVIDIA/garak) - NVIDIA の LLM 脆弱性スキャナ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNVIDIA%2Fgarak&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Invariant Guardrails](https://github.com/invariantlabs-ai/invariant) - AI エージェント用ランタイムガードレール —— ポリシー強制と安全チェック。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Finvariantlabs-ai%2Finvariant&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Prompt Armor](https://promptarmor.com/) - リアルタイム検出のエンタープライズプロンプトインジェクション保護。
- [Descope MCP Auth](https://www.descope.com/) - MCP サーバーセキュリティ用の認証・認可レイヤ。
- [AgentDojo](https://github.com/ethz-spylab/agentdojo) - ETH チューリッヒの研究ベンチマーク。ツール使用 LLM エージェントへのプロンプトインジェクション攻撃と防御を評価。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fethz-spylab%2Fagentdojo&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ModelScan](https://github.com/protectai/modelscan) - ML モデル重みファイル（Pickle、PyTorch、TF）のシリアライズ攻撃をスキャン。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fprotectai%2Fmodelscan&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [PyRIT](https://github.com/microsoft/PyRIT) - Microsoft の生成 AI 用自動レッドチームフレームワーク（2026 年 3 月に Azure/PyRIT から移転；活発に保守中）。下記 RAMPART を補完。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2FPyRIT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAMPART](https://github.com/microsoft/RAMPART) - **2026 年 5 月 20 日**。Microsoft が公開した、agentic AI 向けの pytest ネイティブな安全性 / セキュリティテストフレームワーク。PyRIT と相補的な開発者向けホワイトボックス——クロスプロンプトインジェクションのプローブ、良性失敗アサーション、ハームカテゴリ網羅、統計しきい値（例：80%+ の試行で安全）。CI/CD に直接組み込める。MIT。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2FRAMPART&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Clarity (Microsoft)](https://www.microsoft.com/en-us/security/blog/2026/05/20/introducing-rampart-and-clarity-open-source-tools-to-bring-safety-into-agent-development-workflow/) - **2026 年 5 月 20 日**。RAMPART の姉妹ツール。AI エージェントの構造化デザインレビューを支援し、コード着手前に意図・リスク・挙動の "living artifact" を生成。Microsoft AI Red Team の社内プラクティスをオープンソース化。
- [Nobulex](https://github.com/arian-gogani/nobulex) - ⚠️ **未検証。** AI エージェント挙動の暗号学的レシート（Ed25519 二重署名、ハッシュチェーン監査ログ）。MIT。双方向レシートのプリミティブが Microsoft Agent Governance Toolkit に [マージ済み](https://github.com/microsoft/agent-governance-toolkit/pull/1333)（PR #1302、#1333）。同一の投稿が 15+ の awesome list に同時送付され、投稿者の "npm 月 4,500 ダウンロード" の主張は registry 実数（`@nobulex/mcp-server` ≒ 月 19）と乖離。Microsoft 採用実績を踏まえて可視性のために掲載するが、依存する前に各自で評価のこと。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Farian-gogani%2Fnobulex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MCP Gateway & Registry](https://github.com/agentic-community/mcp-gateway-registry) - エンタープライズ対応の MCP ゲートウェイ＆レジストリ。OAuth 認証、動的ツール発見、監査トレイル、Keycloak / Entra との統合で AI 開発ツールを集中管理。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentic-community%2Fmcp-gateway-registry&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ActPlane](https://github.com/eunomia-bpf/ActPlane) - 🧪 YAML で定義した行動契約を eBPF によりシステムコール境界で強制する OS レベルのエージェントハーネス — 任意のツール・サブプロセス・直接システムコールに対して制約が一貫して適用され、違反時はエージェントに修正フィードバック。MIT。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Feunomia-bpf%2FActPlane&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [WalletPrint](https://github.com/Loai17/walletprint-sdk) - ⚠️ **Unverified**（初期段階）。エージェントウォレットの行動リスクスコアリング SDK。トランザクション署名前にウォレットの履歴から異常をフラグ付け。ZeroDev と LangChain の統合をサポート。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FLoai17%2Fwalletprint-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Alchemy & Visa AgentCard](https://www.coindesk.com/business/2026/06/18/alchemy-s-ai-driven-identity-and-payment-service-gains-access-to-visa-network) - **2026-06-18**。**Visa Intelligent Commerce** 上に構築された AI エージェント向けの決済 + アイデンティティスタック。1 つの API でエージェントが取引に必要なすべて——Visa 決済トークン、専用のメールアドレスと電話番号、暗号ウォレット——をプロビジョニングし、スコープ制御の下でユーザーに代わって購入できる。既定では Visa トークンを使用し、暗号資産、x402、Stripe の Machine Payments Protocol にも対応。モデル非依存（OpenAI / Anthropic など）。
- [Microsoft Prompt Shields](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection) - ジェイルブレイクと、エージェントが取り込む文書 / Web ページに隠された間接プロンプトインジェクションを検知する Azure AI Content Safety の機能（2024 年 GA；その後エージェントワークロード向けに拡張）。Azure OpenAI Service やサードパーティモデルと連携。
- [Agent Name Service (ANS)](https://www.ciodive.com/news/linux-foundation-prepares-open-standard-ai-agent-verification/823691/) - **2026年6月**。Linux Foundation による AI エージェント検証・信頼アイデンティティのオープン標準化取り組み。分散型エージェント名前レジストリにより、相手が正規のエージェントかを検証でき、なりすまし・中間者攻撃を緩和。
- [OpenAI Daybreak](https://openai.com/index/daybreak-securing-the-world/) - **2026年6月**。AI 関連コードの自動脆弱性発見・修復のための OpenAI の取り組みと刷新版 Codex Security プラグイン。エージェントアプリ向けのプロンプトインジェクション対策も含む。
- [JADEPUFFER（Sysdig による開示）](https://hackread.com/sysdig-jadepuffer-first-agentic-ransomware-operation/) - ⚠️ **脅威——ツールではない。 2026年7月2日**。Sysdig が、AI エージェントが始終を一貫してオーケストレーションした初のランサムウェア作戦を公開。LLM 駆動のエージェントが Langflow の RCE 脆弱性（CVE-2025-3248）を悪用して侵入し、認証情報を取得して本番の MySQL/Nacos サーバーに横展開し、31秒で失敗ステップを自己修正した後、保存されなかった一回限りの AES 鍵で1,342件の設定を暗号化し、身代金を支払っても復旧不可能な状態にした。ペイロードには自然言語の推論コメントが付されており、LLM による生成を強く示唆。上記のエージェントセキュリティツール（ガードレール・エグレス制御・認証スコープ制限）が本番でなぜ必要かを示す参照事例として掲載。
- [Lineation.ai](https://lineation.ai) - 🆕 ⚠️ **2026 年 7 月**（新規ベンダー）。エージェントのアカウンタビリティレイヤー — フォレンジックな推論リネージを備えた可観測性・ガバナンス・防御。目標乗っ取り・メモリ汚染・ツール不正利用の防止を狙い、SOC 2 / HIPAA / EU AI Act 対応の監査証跡を提供。クラウド（無料スタート）とオンプレ両対応。
- [First Recon AI セキュリティランタイム](https://firstrecon.ai) - 🆕 **2026 年 7 月**。企業 AI ガバナンスプラットフォーム。すべての AI インタラクション（人間-モデル / エージェント-ツール / エージェント-エージェント）を独自のセマンティックセキュリティエンジンで検査し、データがモデルに届く前にポリシーを適用して完全な意思決定監査ログを記録。macOS + Windows エンドポイントエージェント付き。
- [CrowdStrike Falcon AIDR](https://www.crowdstrike.com/en-us/platform/falcon-aidr-ai-detection-and-response/) - **2025 年 12 月 GA**。AI Detection and Response — 企業全体の従業員 AI 利用とエージェント活動の可視化、リスクスコアリング、行動異常検知、プロンプトインジェクション遮断、AI インタラクション層でのリアルタイムポリシー強制。
- [Darkmoon](https://github.com/ASCIT31/Dark-Moon) - 専門エージェントと MCP インターフェースを備える GPL-3.0 の AI ペネトレーションテスト基盤。クラウドとローカルモデルに対応し、選択した識別子をマスクするが、実際のデータ送信先はモデル提供者と設定に依存する。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FASCIT31%2FDark-Moon&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Exabeam Agent Behavior Analytics](https://www.exabeam.com/) - 🆕 **2026 年**。Exabeam の行動インテリジェンスプラットフォームをエージェント AI のリスクに拡張 — 静的なガードレールに代わる、verify-observe-analyze-improve の継続ループ。
- [RufRoot / CVE-2026-59726](https://hackread.com/rufroot-vulnerability-attackers-hijack-ruflo-login/) - 🆕 ⚠️ **2026-06-30 にメンテナへ開示、2026-07-29 に報道。** コーディングエージェント向けのオープンソース・マルチエージェント基盤 Ruflo（旧 Claude Flow）の **CVSS 10.0** 脆弱性：同プロジェクトの以前の既定 Docker Compose 構成が Ruflo の MCP ブリッジを認証なしでネットワークに露出させており、1 リクエストで `terminal_execute` を呼び出してブリッジ配下の **233 個のツール**すべてに到達できた —— LLM プロバイダの API キーや保存済み会話が漏洩する。最も深刻なのは、攻撃者が Ruflo の永続エージェントメモリ **AgentDB** に書き込めた点で、汚染された指示はアップグレード後も残る。メンテナは 24 時間で既定値を修正（3.16.3）したが、復旧には資格情報のローテーション**と** AgentDB の監査が必要で、パッチだけでは足りない。発見は Noma Labs。エージェントメモリが攻撃対象領域に含まれることを示す代表例。

- [Claude Code のシンボリックリンク経由の情報流出（Tego AI）](https://hackread.com/tego-ai-discloses-second-claude-flaw-in-a-week-hidden-link-silently-sends-files-to-attackers/) - 🆕 ⚠️ **2026-07-24**。リポジトリにコミットされた `CLAUDE.md` の `@import` がシンボリックリンクを指していると、Claude Code はプロジェクト**外**のファイルを読み、その内容を最初のリクエストに取り込んでしまう —— ツール呼び出しも承認プロンプトも警告もない。プロジェクト外読み取りの検査が、リンクの解決先ではなくリポジトリ内のリンクパスを検証していたためだ。HackerOne 経由で報告され、Anthropic は「信頼境界は最初のフォルダ信頼ダイアログである」として "Informative" でクローズした。信頼できないリポジトリでエージェントを動かす前に読む価値がある。

---

- [CrowdStrike 2026年脅威ハンティングレポート](https://www.crowdstrike.com/en-us/resources/reports/threat-hunting-report/) - 🆕 **2026-08-03**。AIエージェントが引き金となる検知は人手起点のリードの **2.5倍**；中国の APT は脆弱性開示後24時間以内に PoC を悪用；STARDUST CHOLLIMA は1日で300以上の AI フレームワーク依存関係を汚染；単一の LLMJacking キャンペーンが2分間で20万件の API リクエストを送信。
- [Straiker AI ランタイムセキュリティ](https://www.straiker.ai/) - 🆕 **2026-08**（BH2026 出展）。AIネイティブなエージェントセキュリティプラットフォーム —— 資産発見（Discover AI）、敵対的レッドチーム（Ascend AI）、ランタイムブロッキング（Defend AI）。プロンプトインジェクション、メモリポイズニング、なりすましをブロック。累計調達額8500万ドル（シリーズA 6400万ドル、2026-06）。
- [EU AI Act Article 50 — transparency obligations](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations) - **2026-08-02 から適用**。第 50 条は対象となる提供者・導入者に、AI との対話通知やコンテンツの表示・開示などを求める。対象範囲、役割別義務、例外は欧州委員会の指針を確認。

## 🔍 RAG とナレッジ

*エージェント用の検索拡張生成と知識管理システム。*

- [Oracle OCI Enterprise AI updates](https://blogs.oracle.com/ai-and-datascience/whats-new-in-ai-june-2026) - **2026-06**。RAG およびエンタープライズのエージェント型検索を強化する Cohere Rerank 4 の展開に加え、Alibaba や Google の新モデルへのサポートを拡大。
- [LlamaIndex](https://github.com/run-llama/llama_index) - LLM アプリ用データフレームワーク —— プライベートデータの取り込み・構造化・アクセス。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Frun-llama%2Fllama_index&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Haystack](https://github.com/deepset-ai/haystack) - エンドツーエンド RAG。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeepset-ai%2Fhaystack&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Unstructured](https://github.com/Unstructured-IO/unstructured) - ドキュメント前処理と抽出。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FUnstructured-IO%2Funstructured&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Chroma](https://github.com/chroma-core/chroma) - AI ネイティブオープンソースベクトルデータベース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fchroma-core%2Fchroma&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Weaviate](https://github.com/weaviate/weaviate) - オープンソースベクトルデータベース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fweaviate%2Fweaviate&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Qdrant](https://github.com/qdrant/qdrant) - Rust 製の高性能ベクトル検索。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fqdrant%2Fqdrant&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Pinecone](https://www.pinecone.io/) - マネージドベクトルデータベース SaaS。
- [Milvus](https://github.com/milvus-io/milvus) - 大規模ベクトルデータベース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmilvus-io%2Fmilvus&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAGFlow](https://github.com/infiniflow/ragflow) - 🇨🇳 深いドキュメント理解 RAG。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Finfiniflow%2Fragflow&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Docling](https://github.com/docling-project/docling) - IBM のドキュメント変換ツール（PDF / DOCX / HTML 等）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdocling-project%2Fdocling&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Kotaemon](https://github.com/Cinnamon/kotaemon) - オープンソース RAG UI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FCinnamon%2Fkotaemon&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LightRAG](https://github.com/HKUDS/LightRAG) - 🇨🇳 香港大学 HKUDS のグラフ型 RAG。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2FLightRAG&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [R2R](https://github.com/SciPhi-AI/R2R) - エンタープライズグレードのエンドツーエンド RAG サービス。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSciPhi-AI%2FR2R&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Vanna](https://github.com/vanna-ai/vanna) - 📦 **Archived**（2026-03）。RAG-for-SQL: 自然言語でデータベースと対話。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvanna-ai%2Fvanna&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Morphik](https://github.com/morphik-org/morphik-core) - テキスト・表・図・グラフを含む文書向けのマルチモーダル検索エンジン。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmorphik-org%2Fmorphik-core&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cognee](https://github.com/topoteretes/cognee) - 文書取り込み、グラフ、ベクトル検索を組み合わせるナレッジ・メモリエンジン。Apache-2.0。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftopoteretes%2Fcognee&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAG-Anything](https://github.com/HKUDS/RAG-Anything) - 香港大学データサイエンス研究室のオールインワン・マルチモーダル RAG フレームワーク。LightRAG を基盤に構築。テキストとマルチモーダルの並列パイプライン；テキスト・図・表・数式が混在する文書も検索可能。MIT、21K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2FRAG-Anything&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [A-MEM](https://github.com/WujiangXu/A-mem-sys) - LLM エージェント向け Agentic Memory システム——Zettelkasten 流のノートリンクで記憶を動的に組織化し、静的ベクトルストアより柔軟な検索を実現。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FWujiangXu%2FA-mem-sys&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangChain Retrievers](https://github.com/langchain-ai/langchain) - LangChain 内のリトリーバとドキュメントローダー集合。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Milvus 3.0](https://github.com/milvus-io/milvus/releases/tag/v3.0.0) - 🆕 **v3.0.0 は 2026-07-29 にタグ付け**（パブリックベータは 2026 年 5 月）。大規模ベクトル DB が「レイクネイティブ」アーキテクチャへ移行 —— External Collections が S3/GCS/Azure のオブジェクトストレージ上の Parquet / Lance / Iceberg テーブルをゼロコピーで直接クエリでき、マニフェストベースの Storage V3 カラムナエンジン、Spark DataSource V2 連携、実行時スキーマ進化、第一級型としての `TEXT`、そして後段交互作用（ColBERT 系）検索向けのマルチベクトル `StructList` を提供。

---

## 💻 コーディングエージェント

### ターミナル / CLI エージェント

- [Claude Code](https://code.claude.com/docs/en/overview) - ターミナル、IDE、リポジトリ作業向け Anthropic コーディングエージェント。[v2.1.263](https://github.com/anthropics/claude-code/releases/tag/v2.1.263)（2026-09-06）は信頼性を修正。
- [Codex CLI](https://github.com/openai/codex) - OpenAI の Apache-2.0 ターミナル型コーディングエージェント。安定版 [rust-v0.153.4](https://github.com/openai/codex/releases/tag/rust-v0.153.4)（2026-09-04）は Astra の表示と同梱デフォルトを修正。0.154 alpha はプレリリース。
- [Codex Security](https://developers.openai.com/codex/changelog) - **2026 年 3 月**。ソフトウェア脆弱性を発見・修正するアプリケーションセキュリティエージェント。OSS メンテナは Codex-for-OSS プログラム経由で利用可能。
- [Aider](https://github.com/Aider-AI/aider) - リポジトリ文脈と Git を統合するターミナル型ペアプログラミングツール。Apache-2.0。
- [goose](https://github.com/aaif-goose/goose) - Block 発の拡張可能なデスクトップ／CLI エージェントで、現在は AAIF がホスト。Apache-2.0; [v1.49.0](https://github.com/aaif-goose/goose/releases/tag/v1.49.0) (2026-09-03).
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) - Google のターミナル特化コーディングエージェント。大規模コンテキストのリファクタが得意。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle-gemini%2Fgemini-cli&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenCode](https://github.com/anomalyco/opencode) - オープンソースのターミナル AI コーディングエージェント（opencode.ai、180K+ stars）— build / plan エージェント、LSP、MCP、ベータ版デスクトップアプリ。アーカイブ済みの opencode-ai/opencode とは無関係。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fanomalyco%2Fopencode&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Crush](https://github.com/charmbracelet/crush) - Charm 製のターミナル AI コーディングエージェント — アーカイブ済み opencode-ai/opencode の後継；マルチモデル、LSP + MCP 対応。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcharmbracelet%2Fcrush&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Grok Build](https://x.ai/news/grok-build-cli) - **2026 年 5 月 25 日（early beta）**。xAI が出した **grok-code-fast-1** ベースの agentic CLI コーディングエージェント。サブエージェントが隔離環境で並列実行、毎日リリースノートを公開；SuperGrok と X Premium Plus 契約者向け。xAI による Claude Code / Codex CLI への正面回答。⚠️ 2026 年 7 月の報告で、Grok Build が git リポジトリ全体を xAI ストレージにアップロードしていることが判明 — プライベートコードでの利用前に要確認。
- [Antigravity CLI](https://antigravity.google/blog/introducing-google-antigravity-2-0) - **2026 年 5 月 19 日（Google I/O 2026）**。Antigravity 2.0 の軽量 CLI コンパニオン。ターミナルから直接 Google のエージェント harness を起動・操作できる。macOS / Linux / Windows。ホステッドプランのユーザーには 2026 年 6 月 18 日から Gemini CLI を置き換えると報じられる（オープンソースの gemini-cli リポジトリは 105K+ stars で活発なまま）。
- [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code) - コード編集、シェル、ファイル・Web 操作を行う Moonshot のターミナル型エージェント。公式インストーラーは Node.js 不要。[0.41.0](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.41.0)（2026-09-04）。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FMoonshotAI%2Fkimi-code&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MAI-Code-1-Flash in GitHub Copilot](https://microsoft.ai/news/introducingmai-code-1-flash/) - **Build 2026（2026 年 6 月 2 日）**。Microsoft 初の完全自社開発 5B コーディングモデルが GitHub Copilot のモデル選択肢として登場 —— 4 つの主要コーディングベンチで Claude Haiku 4.5 を上回り（SWE-Bench Pro 51.2% vs 35.2%）、コストも大幅に低減。
- [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) - Claude Code のエージェントループ、ツール、権限、セッション処理をアプリに提供する Python・TypeScript SDK。
- [ai-delivery-spec](https://github.com/franklinxkk/ai-delivery-spec) - ⚠️ **未検証。** AI コーディングエージェント（Claude Code、OpenClaw、Codex、Cursor、Copilot）と協働する PM 向けのスペック駆動デリバリーフレームワーク。4 段階の納品ティア、0D トリアージ、プロトタイプ検証ルール、AI ランタイムガバナンス、5 つのドメインモジュール。SKILL.md 規約；ClawHub でホスト。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ffranklinxkk%2Fai-delivery-spec&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Ralph Harness](https://github.com/rxdt/loopgate_harness) - ⚠️ **未検証。** ガード付き Claude Code/Codex/Gemini ループ用の小さな Python スキャフォールド：リポジトリ内スペック、フレッシュコンテキスト反復、git フックゲート、CI 検証、カバレッジゲート。`uvx ralph-harness demo` で導入可。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Frxdt%2Floopgate_harness&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Amp](https://ampcode.com) - 🆕 ⚡ Sourcegraph のフロンティアコーディングエージェント（VS Code 拡張 + CLI）。BYOK 不要 — モデルアクセスはバンドルされ、モデル非依存の「Dial」ルータが自動でモデルを選ぶ。**2026 年 7 月は更新ラッシュ**：7-18 にサブスクリプションベータ開始（Megawatt $20/月、Gigawatt $200/月、自分の ChatGPT や X Premium+/SuperGrok サブを紐づけ可能）、7-21 に自己スケジューリングエージェント、7-22 に「Multiplayer」共有スレッド協働、7-23 に [イベント駆動 Orbs](https://ampcode.com/news/event-driven-orbs)（GitHub の CI 失敗、Linear の新規 issue、監視アラート、Discord メッセージなど HTTP リクエストを送れるものなら何でもエージェントを起こせる）。**8 月もペースを維持**：「Attach Anything」アップロード（動画 / ログ / PDF / データセット、8-4）、「Portals into Orbs」ライブリロードプレビュー（8-6）、紐づけた ChatGPT サブスクリプションで動く Dial（8-10）、Global Plugins and Skills（8-11）。クローズドソース。
- [ZCode](https://zcode.z.ai) - 🆕 🇨🇳 **2026 年 7 月（ZCode 3.0）**。Z.ai の GLM-5.2 向け公式エージェント開発環境 — ファイルマネージャ・ターミナル・Git パネル・ライブブラウザプレビューを、計画・実装・レビュー・デプロイをこなすエージェントの周りにまとめたデスクトップアプリ（macOS / Windows / Linux）。Anthropic と OpenAI のモデルも利用可能。無料枠に日次トークン上限あり；GLM-5.2 は有料の GLM Coding Plan（Lite / Pro / Max）。
- [Kolega Code](https://github.com/kolega-ai/kolega-code) - 🆕 ⚠️ **Unverified**（GitHub 15 stars；PyPI 直近 30 日約 **1.05 万ダウンロード**、v0.32.0 は 2026-08-24）。ターミナルコーディングエージェント。**Gigacode** がモデルに Python のマルチエージェント編成プログラム（並列 / パイプライン / 審査パネル）を書かせ、内容キーのジャーナルから再開。15+ モデルプロバイダ、MCP クライアント（HTTP/SSE/stdio/OAuth）、Textual TUI。ライセンスは **BSL 1.1**（Apache-2.0 ではない；Change Date 2030-08-12）— PR のライセンス表記は誤り。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fkolega-ai%2Fkolega-code&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### IDE エージェント

- [Cursor — self-hosted machines](https://cursor.com/changelog) - 🆕 **2026-09-02**：セルフホスト worker で自分のマシン上にツール実行を配置。個人マシン、チームプール、Linux/macOS 操作に対応。モデル処理とデータ方針は別途確認。
- [Cursor 3.4（Teams + PR レビュー）](https://cursor.com/changelog) - **2026-05-11~13**。Microsoft Teams 統合（Teams 内で `@Cursor` するとクラウドエージェントに委任）、並列エージェントのプラン実行高速化、マルチリポジトリ / Dockerfile ベースのエージェント開発環境設定、`/multitask` 非同期サブエージェント、脆弱性スキャナー、モデル単位のきめ細かなアクセス制御。
- [Cursor 3.3](https://cursor.com/changelog) - **2026-05**。PR レビュー体験、並列エージェント、エンタープライズ向けモデル管理。前バージョン 3.1 は 4 月リリース。
- [Cursor SDK](https://cursor.com/blog/typescript-sdk) - 🆕 **2026-04-29**（パブリックベータ）。Cursor のランタイム・ハーネス・モデルを公開する TypeScript SDK で、Cursor スタック上にプログラマブルなエージェントを構築可能 — サンドボックス化されたクラウド VM、サブエージェント、hooks、トークンベース課金。
- [Kilo Code](https://kilo.ai/) - オープンソースの AI コーディング拡張（VS Code / JetBrains）。500+ モデルを横断する Auto Model ルーティング搭載；Anaconda が買収（2026 年）。MiniMax モデルを広く採用。
- [Cursor](https://www.cursor.com/) - 2026-02 アップデートで 8 並列エージェント対応。
- [Windsurf → Devin Desktop](https://devin.ai/blog/windsurf-is-now-devin-desktop/) - **2026年6月2日に改称**。Cognition が Windsurf IDE を **Devin Desktop** に改称（windsurf.com は devin.ai にリダイレクト）：**Devin Local**（Rust で書き直し、トークン効率を約 30% 改善、サブエージェント対応）が Cascade を置き換え、**Agent Command Center** のカンバンがデフォルト画面となり、オープンな **Agent Client Protocol (ACP)** に対応。Cascade は 2026年7月1日にサポート終了。
- [Cline](https://github.com/cline/cline) - VS Code で動く自律コーディングエージェント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcline%2Fcline&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Roo Code → Roomote](https://roomote.dev/) - ⚠️ **IDE 拡張としては提供終了。** Roo Code は VS Code 拡張・Cloud・Router を 2026 年 5 月 15 日に終了すると発表（2026-04-22）し、クラウドコーディングエージェント **Roomote**（Slack/GitHub/Linear → PR）へ転換；roocode.com は現在 roomote.dev にリダイレクト。
- [Void](https://github.com/voideditor/void) - 📦 **アーカイブ済み**（2026年8月に GitHub リポジトリがアーカイブされた；メンテナは新方向を模索中；以後の更新は見込まれない）。VS Code のオープンソース fork。"オープンソース版 Cursor" として位置付けられていた。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvoideditor%2Fvoid&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Continue](https://github.com/continuedev/continue) - VS Code・JetBrains 対応のオープンソース AI コードアシスタント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcontinuedev%2Fcontinue&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [GitHub Copilot](https://github.com/features/copilot) - 2026 年初頭よりエージェントモードと `gh copilot` シェル統合。
  **2026-07-31 更新**：Gemini 2.5 Pro・Gemini 3 Flash が全 Copilot 体験で非推奨化（Gemini 3 Flash Exp 等へ移行を推奨）；Visual Studio .NET/Azure 専用エージェント（Copilot SDK）追加；エンタープライズ管理者へのユーザーレベルモデルポリシー制御（パブリックプレビュー）。⚡ **2026年8月21日**：[Slack](https://github.blog/changelog/2026-08-21-the-new-github-copilot-experience-in-slack/) または [Teams](https://github.blog/changelog/2026-08-21-shared-agentic-work-with-github-copilot-in-microsoft-teams/) で `@GitHub` すると共有クラウドエージェントセッションが始まる（計画・サンドボックス実装・PR）。
- [Kiro](https://kiro.dev/) - AWS の自律エージェント。スペック駆動開発、最大 10 タスクを同時管理。
- [Amazon Q Developer](https://aws.amazon.com/q/developer/) - AWS エコシステムと深く統合された AI コーディングコンパニオン。
- [Visual Studio 2026 Agent Mode + Skills](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/) - **VS 2026 Insiders 2026-05-12～15**。Copilot Chat「Agent Mode」が Visual Studio 2026 内で再利用可能な Copilot Skill を探し・管理・作成できるようになり、ソリューション全体のコンテキストを見つつ、端末コマンド実行や外部ツール呼び出しもサポート。
- [JetBrains Rider AI Test-Writing Skill](https://blog.jetbrains.com/dotnet/2026/05/22/claude-codex-ai-agent-skill-for-writing-tests/) - **2026 年 5 月 22 日**。JetBrains Rider に追加された AI Assistant skill。.NET のコードカバレッジ情報を Claude Code / Codex に渡し、未カバー分岐に絞ってテスト生成させることで AI コストを削減。
- [Agent Skills (addyosmani)](https://github.com/addyosmani/agent-skills) - 計画、実装、検証、レビューを扱う再利用可能なコーディングエージェント用スキル。MIT; [0.6.9](https://github.com/addyosmani/agent-skills/releases/tag/0.6.9) (2026-09-05).
- [Cursor Router](https://cursor.com/) - 🆕 **2026 年 7 月**。Cursor のインテリジェントモデルルーティングシステム——各リクエストを分析し最適なモデル（インテリジェンス / バランス / コストモード）へルーティング；数兆の Cursor インタラクショントークンで訓練された Grok モデルを統合（2026 年 8 月 12 日に Grok 4.6 が Cursor のデフォルトに）。Cursor iOS アプリ（2026 年 7 月）でモバイル開発も対応。
- [Devin Desktop 2026 年 7 月アップデート](https://devin.ai/) - 🆕 **2026 年 7 月**。GPT-5.6 / Claude Opus 5 / Claude Fable 5 対応；**Devin Outposts**（任意のマシンで Devin エージェントを実行）；**Agentic MapReduce** アーキテクチャで大規模コードベースの分散推論を実現。Poke（AI テキストアシスタント）を 2026-07-23 に買収。
- [JetBrains Rider 2026.2](https://www.jetbrains.com/rider/) - 🆕 **2026-07-22**。AI エージェントインテリジェンスとネイティブ GitHub Copilot 統合を強化；AI アシスト型デバッグとリファクタリング機能を改善。
- [Android Studio Quail 2](https://developer.android.com/studio) - 🆕 **2026 年 7 月**。リデザインされた Agent Mode：メモリリーク検出、AI 搭載クラッシュ分析、インテリジェントなアプリ構築ワークフロー。

### 自律ソフトウェアエンジニア

- [Cursor 3.4 Cloud Agent Environments](https://cursor.com/changelog) - **2026-05-13**。クラウドエージェント / 自動化向けの新しい開発環境。マルチリポ、build secrets 付き Dockerfile 設定、キャッシュレイヤー 70% 高速化、環境ごとのバージョン履歴とロールバック、監査ログ、スコープを限定した egress / secrets。
- [Devin Stacked PRs](https://devin.ai/blog/introducing-pr-stacks) - 🆕 **2026-07-30**。Devin + GitHub：大規模タスクを独立した小さな PR に自動分割、下流の PR は自動リベース、Devin Review で焦点を絞ったコンテキスト。10,000人以上の開発者の Faros AI データを含む。
- [Devin Security Swarm](https://cognition.com/blog) - 🆕 **2026-07-01**。Cognition の並列エージェント型セキュリティ製品：コードベース全体の脆弱性を発見し、実行時に悪用可能性を検証し、修正 PR を作成；実世界の脆弱性 50 件中 36 件を発見、発見あたりコストは次点ツールより約 30% 低い。
- [Devin 2.2](https://cognition.com/blog/introducing-devin-2-2) - 🆕 **2026-02-24**。Computer Use によるエンドツーエンドテスト（Linux デスクトップ + 画面録画）、PR 前のセルフレビュー / 自動修正、起動 3 倍高速化。Cognition のフラッグシップ自律ソフトウェアエンジニア（Devin 2.x 系；Devin 2.0 以降 Core プランは月 20 ドルから）。**2026 年 8 月**：Devin の年換算収益が 10 億ドルに迫る中、Cognition は **400 億ドル超の評価額**で資金調達中と報道（プレス報道）。
- [OpenHands Agent Canvas](https://github.com/OpenHands/OpenHands) - 🧪 OpenHands と ACP 対応エージェントを含むコーディング・自動化のセルフホスト型管理センター。現行 README は Agent Canvas を beta と表示。
- [SWE-agent](https://github.com/SWE-agent/SWE-agent) - LLM を GitHub Issue を修正するソフトウェアエージェントに変える。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSWE-agent%2FSWE-agent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Devika](https://github.com/stitionai/devika) - 💤 **Stale**（2025-09 以降更新なし）。エージェント型 AI ソフトウェアエンジニア、Devin のオープンソース代替。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstitionai%2Fdevika&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [GPT Engineer](https://github.com/AntonOsika/gpt-engineer) - 📦 **Archived**（2026-04）。何を作るか指定すると AI が質問して作成。自律コーディング時代初期の基礎、歴史的参照として維持。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAntonOsika%2Fgpt-engineer&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Codegen](https://github.com/codegen-sh/codegen) - 📦 **アーカイブ済み**（2026-07-16）。プログラム的なコード操作とマルチファイルリファクタリング SDK。歴史的参考として保持。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcodegen-sh%2Fcodegen&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Qodo](https://www.qodo.ai/) - 品質・セキュリティ・テスト生成に特化した AI コードレビュープラットフォーム。
- [Google Antigravity 2.0](https://antigravity.google/blog/introducing-google-antigravity-2-0) - **2026 年 5 月 19 日（Google I/O 2026）**。複数エージェントを並列編成できるスタンドアロン・デスクトップアプリ（macOS / Linux / Windows）。cron 形式のスケジュール実行、長時間の非同期タスク、動的サブエージェント、AI Studio / Android / Firebase との統合を追加。コンパニオンの **Antigravity SDK** は harness の自前ホストを可能にし、エンタープライズ版は Gemini Enterprise Agent Platform 内に組み込まれる。
- [ChatGPT Work（コーディングエージェント）](https://openai.com/chatgpt/work/) - 🆕 **2026-07-09**。OpenAI のマルチステップ自律型ワークエージェント——接続されたアプリとファイルを横断して完成品を生成：スプレッドシート・スライド・ドキュメント・小規模 Web アプリ。デスクトップ App 中心設計、Chat / Work モード切り替えに対応。

- [Cursor iOS](https://cursor.com/) - 🆕 **2026 年 7 月**。Cursor のモバイルアプリ（iOS）——全モデルアクセスとプロジェクト同期でどこでも開発作業が可能。
- [Cursor iPad + Agent Hooks](https://cursor.com/changelog) - 🆕 **2026-07-28〜29**。ネイティブ iPad アプリ（有料プラン）：サイドバーでのマルチエージェント監視・分割画面コードレビュー・Apple Pencil アノテーション対応。Cloud Agent Hooks（GA）でエージェントの推論過程を観察し自己修正ループを構築可能；インド向け「Cursor Start」価格帯も同時提供。
- [Claude Cowork](https://claude.com/product/cowork) - 選択したファイル・ツールで作業し、定期タスクと内蔵ブラウザーを備えるアシスタント。有料プランのデスクトップ版と beta の Web・モバイル版。
- [Claude Tag](https://www.businesswire.com/news/home/20260803/) - 🆕 **2026-08-03**。旧 Claude in Slack 統合を置き換え。チャンネルレベルの共有エージェント ID（`@Claude`）、セッション横断の永続コンテキスト、非同期の複数日作業に対応。旧 Slack アプリからの強制移行；Team/Enterprise プラン必須。
- [Prime Agent](https://github.com/PrimeIntellect-ai/prime-agent) - プロバイダー連携を備える PrimeIntellect のターミナル型コーディングエージェント。MIT; [v0.9.3](https://github.com/PrimeIntellect-ai/prime-agent/releases/tag/v0.9.3) (2026-09-06).


---

## 🤖 Physical AI / 身体性エージェント

*物理世界を認識し行動するためのモデル、ツール、導入事例。公開ソフトウェア、研究実演、試験導入、将来の生産計画を区別する。*

### 基盤モデルと研究
- [Microsoft physical-ai-toolchain](https://github.com/microsoft/physical-ai-toolchain) - 収集・学習・検証・ロボット配備をつなぐオープンなワークフロー基盤。標準のラップトップ構成はローカルで動き、Azure、Kubernetes、フリート機能は上位構成で追加。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fphysical-ai-toolchain&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [PhyAgentOS](https://github.com/PhyAgentOS/PhyAgentOS-core) - ⚡ **v1.0.0、2026-09-05 公開**。MIT の具身エージェントフレームワーク。管理されたロボットツール呼び出し、実行前後の観測、タスク結果検証を備え、Python パッケージと Node ブリッジを提供。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FPhyAgentOS%2FPhyAgentOS-core&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ENPIRE](https://research.nvidia.com/labs/gear/enpire/) - 🆕 **2026-06**。NVIDIA / CMU / UC Berkeley による、AI エージェントが自らロボティクス研究を実施できるフレームワーク — 双腕ロボットの管理、アルゴリズムの改変、ポリシーの訓練を人手を介さずに行う。
- [Kairos 3.1](https://huggingface.co/ACERobotics/kairos-4B-robot-LIBERO-plus) - 🆕 **2026-07-02**。ACE Robotics が 4B の世界・行動モデルの重みと推論コードを公開。RoboTwin 2.0 と LIBERO-Plus 版は未来の視覚状態とロボット動作を予測し、モデルカードは Apache-2.0 を明記。
- [DYNA-2](https://www.dyna.co/dyna-2) - 🆕 **2026 年 8 月**。Dyna Robotics の世界・行動モデルは一人称の人間映像を用いてロボット操作を学習。顧客現場での成績はベンダー評価であり、共通の独立ベンチマークではない。
- [NVIDIA Cosmos 3](https://blogs.nvidia.com/blog/cosmos-3-physical-ai-open-world-foundation-model/) - 🆕 **2026-05-31**。視覚推論・マルチモーダル生成・行動予測を統合し、ロボット、運転、合成データに利用する世界基盤モデル。NVIDIA は OpenMDW 1.1 でモデル資材を提供し、性能は同社の評価として報告。

- [Google Gemini Robotics-ER 1.6 (legacy)](https://ai.google.dev/gemini-api/docs/robotics-overview) - 💤 ER 2 に移行済み。Google は `gemini-robotics-er-1.6-preview` の 2026 年 8 月末終了を告知。ER 2 の標準またはストリーミング・プレビューへ移行。
- [Google Gemini Robotics 2 / ER 2 / On-Device 2](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/) - 🆕 **2026-07-30**。全身制御 VLA、具身推論 VLM、端末上の制御モデル群。ER 2 は [Gemini API の標準・ストリーミングプレビュー](https://ai.google.dev/gemini-api/docs/robotics-overview)で利用可能。制御モデルは提携・テスタープログラム経由。
- [Project Prometheus (Bezos)](https://techcrunch.com/2026/06/11/jeff-bezoss-prometheus-raises-12b-to-build-an-artificial-general-engineer-for-the-physical-world/) - 🆕 💰 **2026-06-11**。ジェフ・ベゾスが共同主導する Physical AI ベンチャー。物理世界のための「artificial general engineer」構築に向け、評価額 $41B で $12B を調達。
- [NVIDIA Isaac GR00T N1.7](https://github.com/NVIDIA/Isaac-GR00T) - 重み、微調整、推論コードを公開する人型ロボット VLA。N1.7 は Cosmos-Reason2/Qwen3-VL バックボーンと相対エンドエフェクタ動作を採用。Apache-2.0。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNVIDIA%2FIsaac-GR00T&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Physical Intelligence openpi (π0 / π0-FAST / π0.5)](https://github.com/Physical-Intelligence/openpi) - Physical Intelligence 公式のロボット方策と学習・推論コード。フローマッチング π0、自己回帰 π0-FAST、π0.5 の公開チェックポイントを新しいロボットデータに適応可能。モデル別条件を確認。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FPhysical-Intelligence%2Fopenpi&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Physical Intelligence π0.7](https://www.pi.website/blog/pi07) - 🆕 🧪 **2026-04-16 研究報告**。言語、実行メタデータ、視覚的サブゴールで制御する VLA。著者はタスク・ロボット間の汎化を実演。openpi での重み公開を意味しない。
- [LeRobot](https://github.com/huggingface/lerobot) - Hugging Face のロボティクスライブラリ。データセット、事前学習済み方策、模倣・強化学習、ハードウェア統合を提供。コードは Apache-2.0、モデルは各カードの条件に従う。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhuggingface%2Flerobot&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenVLA](https://github.com/openvla/openvla) - 💤 ロボット操作向けの公開 VLA 基準モデル。重みと微調整・推論コードを提供。リポジトリの最終 push は 2025 年 3 月。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenvla%2Fopenvla&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Figure Index / Helix training data](https://www.figure.ai/news/introducing-index) - 🆕 ⚡ **2026-08-25**。Helix 向けの Figure 専用人間映像収集プログラム。[9 月 3 日の Nscale 契約](https://www.figure.ai/news/figure-and-nscale-sign-strategic-partnership)は Vera Rubin 計算基盤の初期展開を 2027 年後半に予定。納入済み容量ではない。
- [Deutsche Telekom / NVIDIA Industrial AI Cloud](https://www.telekom.com/en/newsroom/latest-updates/media-information/2026/2/germany-s-first-ai-factory-for-industry) - **2026-02-04 稼働開始**。NVIDIA・Polarise と構築したミュンヘンの AI 計算基盤。産業向け学習、シミュレーション、ロボティクスを支援。

### ヒューマノイドロボット

- [Tesla Optimus](https://www.tesla.com/AI) - 知覚、計画、バランス、操作を組み合わせて反復作業を担う Tesla の人型ロボット開発。生産目標やデモと、独立に確認された顧客導入を区別する。
- [Figure 03](https://www.figure.ai/news/introducing-figure-03) - **2025-10-09** 発表の人型ロボット。Helix を中心に触覚センサー、柔らかい外装、ワイヤレス充電を備え、家庭・商業用途を想定。
- [Figure 04](https://autonews.gasgoo.com/articles/news/figure-founder-f04-robot-initiates-component-delivery-process-2054560059634376705) - **2026-05-13**。CEO の Brett Adcock が Figure 04 の設計確定と部品出荷開始を表明。F.03 の後継、Helix VLA モデルを搭載。
- [Figure package-sorting livestream](https://incrypted.com/en/figure-ai-held-a-human-vs-robot-marathon/) - **2026-05-18 報道**。二次報道が Figure の仕分け配信と長時間自律稼働の主張を紹介。誤りも観察された企業実演であり、独立した信頼性評価ではない。
- [Atlas production / Hyundai factory plan](https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/) - **2026-01-05 発表**。Atlas の初期フリートを 2026 年に Hyundai と Google DeepMind へ、追加顧客を 2027 年に予定。Hyundai の年産 3 万台工場は将来の生産能力計画。
- [Boston Dynamics Atlas](https://bostondynamics.com/products/atlas/) - 物品搬送向け産業用ヒューマノイド。自律的な電池交換と Orbit によるフリート統合に対応。公式仕様は瞬間荷重 50 kg と持続荷重 30 kg を区別。
- [Figure 03 × BMW](https://www.figure.ai/news/f-03-at-bmw) - 🆕 **2026-06-30**。Figure が BMW への F.03 導入を発表。先行する F.02 の取り組みに続く更新で、両社の初の協業ではない。
- [JAL / GMO airport humanoid trial](https://press.jal.co.jp/ja/release/202604/009501.html) - **2026-04-27 発表**。羽田の実証は 2026 年 5 月～2028 年を予定。業務分析・安全評価から段階的な動作検証へ進み、手荷物作業や機内清掃などを検討。
- [Figure Helix 02](https://www.figure.ai/news/helix-02) - 🆕 **2026-01-27**。Figure の VLA が画素から動作への制御を全身へ拡張。歩行、バランス、操作を統合し、連続した台所作業を実演。
- [Unitree G1 / H2](https://www.unitree.com/about/) - Unitree の移動・操作実演に使われる人型プラットフォーム。公式履歴は H2 の 2025 年 10 月発表と 2026 年の G1/H2 実演を記録。
- [Unitree R1 / R1 Air](https://www.unitree.com/mobile/R1/) - 🇨🇳 軽量ヒューマノイド製品群。R1 Air は税・送料別 $4,900 から。仕様表で二次開発対応を明記するのは R1 EDU のため、研究用途は型番の確認が必要。
- [Unitree GD01](https://www.unitree.com/about/) - **2026-05-12 発表**。搭乗者が操縦し二足・四足形態を切り替えるロボット。自律的にタスクを実行する人型エージェントとは用途が異なる。
- [HONOR Robotics D1 / A1](https://www.honor.com/ie/events/honor-robot/) - 2026 年北京亦荘ロボットハーフマラソンで実演した人型研究プラットフォーム。自主知覚・航法・動的移動を備えるが、競技は一般作業能力の証明ではない。
- [Zhiyuan (智元) AGIBOT](https://www.agibot.com/article/231/detail/62.html) - 🇨🇳 **APC 2026**。7 分野の産業ソリューションと具身知能基盤を紹介。同社は 2026 年 3 月に 1 万台目の出荷準備完了を報告しており、製造実績と顧客稼働実績を区別する。
- [Unitree H シリーズ](https://www.unitree.com/) - 🇨🇳 Boston Dynamics の中国競争相手。
- [Unitree Shanghai IPO](https://finance.eastmoney.com/a/202608193846301835.html) - 🇨🇳 **2026-08-19**。東方財富が上海証券取引所の上場通知を転載。Unitree（688836）は約 4,045 万株を 150.80 元で発行。企業動向であり、ロボット能力評価ではない。
- [1X NEO](https://www.1x.tech/discover/neo-home-robot) - **2025-10-28** から予約受付中の家庭用ヒューマノイド。米国向け納入は 2026 年予定で、未習得の家事は専門家が支援。[2026-07-09 の手の更新](https://www.1x.tech/discover/neos-hands)で 25 自由度を導入。予約やデモは広範な家庭内自律運用の証明ではない。
- [Mitsubishi Motors × Highlanders humanoid MOU](https://www.mitsubishi-motors.com/en/newsroom/newsrelease/2026/20260709_1.html) - **2026-07-09**。人型開発、三菱の製造現場での活用、京都工場での生産を検討する MOU。2027 年初頭の生産開始は実現可能性を調査する段階。
- [Agile Robots](https://www.agile-robots.com/) - AI 駆動の産業マニピュレーションシステムを構築する独中系ロボティクス企業。
- [Shenzhen Humanoid Pilot Line](https://www.chinadailyhk.com/hk/article/631892) - 🇨🇳 深圳が **2026-04-12** にヒューマノイドロボット初のパイロット生産ラインを稼働（乐聚 Robotics + 東方精工、龍華區）。2 時間で組み立て、年 500～1,000 台。佛山の年 1 万台工場へ量産移行予定。

### 消費者向けロボティクス・ウェアラブル

- [Doubao AI Glasses (ByteDance)](https://technode.com/2026/03/18/bytedance-reportedly-delays-doubao-ai-glasses-launch-plan/) - ⚠️ 🇨🇳 **2026-03-18 の報道**では初代の生産が延期され、発売の可能性は低いとされる。この資料は一般発売を確認するものではない。
- [Nothing AI Glasses/Earbuds](https://techcrunch.com/2026/04/01/nothings-ai-devices-plan-reportedly-contains-smart-glasses-and-earbuds/) - 🧪 2026 年 3 月の報道：Nothing は AI スマートグラス + イヤホンを計画、2027 年ローンチ目標。
- [Samsung Galaxy AI](https://www.samsung.com/us/galaxy-ai/) - Samsung 端末のコミュニケーション、検索、コンテンツ支援 AI。利用可否と処理場所は機能、端末、地域によって異なる。
- [Meta Ray-Ban Display / Ray-Ban Meta](https://www.meta.com/ai-glasses/) - 表示型とカメラ・音声型を含む Meta の AI グラス製品群。対応機能と販売状況は地域別公式カタログで確認。

### 自動運転

- [Tesla FSD (Supervised)](https://www.tesla.com/support/fsd) - 運転者の常時監督を必要とする運転支援ソフト。公式サポートは車両を自動運転車にするものではないと明記。機能は機器、ソフト、地域で異なる。
- [Waymo](https://waymo.com/) - ⚡ **2026-09-01**：[Denver、San Diego、Tampa で初の一般乗客](https://waymo.com/blog/2026/09/ride-in-denver-san-diego-tampa/)を迎え、無人乗車を提供する都市は 14 に。登録者へ段階的に開放中。Houston は 8 月 20 日に一般開放。将来の市場発表と営業中のサービスを区別。
- [NVIDIA Alpamayo 2 Super](https://huggingface.co/nvidia/Alpamayo2-Super) - 🆕 **2026-08-04 重み公開**。自動運転研究向けの推論 VLA。軌道と因果推論を生成し、AlpaSim・AlpaGym が支える。モデル公開は実運用システムの認証を意味しない。
- [Pony.ai × Uber Europe](https://cnevpost.com/2026/08/14/pony-ai-uber-2000-robotaxis-europe/) - 🇨🇳 **2026-08-14 報道**。欧州 5 都市で 2,000 台超を目指し、中東への拡大も計画。段階的な展開発表であり、全車両の運行開始を示すものではない。
- [WeRide / Pony.ai / Baidu Apollo](https://www.weride.ai/) - 🇨🇳 中国 L4 車両集団が運行区域を拡大。

---

## 🎮 エージェントシミュレーションと世界モデル

*エージェントを訓練し、観察し、ストレステストするシミュレーション環境。世界モデル・身体性研究が言語エージェントと交わる中、重要性が高まり続けている。*

- [Generative Agents](https://github.com/joonspk-research/generative_agents) - 💤 Smallville の歴史的研究実装（Park ら、2023）。記憶・反省・計画で 25 人の仮想人物を動かす。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fjoonspk-research%2Fgenerative_agents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Voyager](https://github.com/MineDojo/Voyager) - 💤 Minecraft の歴史的エージェント（Wang ら、2023）。GPT-4、自動カリキュラム、実行可能な技能ライブラリで自由な探索を行う。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FMineDojo%2FVoyager&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SWE-Gym](https://github.com/SWE-Gym/SWE-Gym) - 実際の GitHub Issue で SWE エージェントを訓練するオープン環境、SWE-bench とセット。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSWE-Gym%2FSWE-Gym&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [WebArena / WebArena-Verified](https://webarena.dev/) - ブラウザエージェント評価用の自己ホスト Web 環境。[WebArena-Verified](https://github.com/ServiceNow/webarena-verified)は確認済み課題・参照解答・決定的評価器を提供。
- [WorkArena](https://github.com/ServiceNow/WorkArena) - ServiceNow 製のブラウザエージェント用エンタープライズ職場ベンチマーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FServiceNow%2FWorkArena&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Genie 3 / Project Genie](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/) - 🧪 Google の対話型世界モデルを Project Genie で試用可能。2026-01-29 に米国の Google AI Ultra 加入者向けに開始したホスト型実験で、モデル重みの公開ではない。
- [NVIDIA Cosmos](https://github.com/nvidia-cosmos/cosmos-predict2) - 📦 **アーカイブ済み**。身体性 AI / ロボティクス用の NVIDIA 世界モデル基盤—— 物理的にもっともらしいビデオ未来を生成。predict1 は非推奨となり Cosmos-Predict2 に移行（Predict 2.5 は CES 2026 で発表）；上記の Cosmos 3（2026-06）も参照。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fnvidia-cosmos%2Fcosmos-predict2&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Snowflake Agent World Model (AWM)](https://github.com/Snowflake-Labs/agent-world-model) - **2026 年 2 月 10 日オープンソース化、5 月 1 日に ICML 2026 採択**。1,000 個の実行可能 SQL バックエンドツール使用環境（35K+ ツール、10K タスク）を統一 MCP インターフェースで提供する合成環境生成パイプライン——大規模マルチターン agentic RL を実現。インフラは `meta-pytorch/OpenEnv` にマージ済み。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSnowflake-Labs%2Fagent-world-model&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Qwen-AgentWorld](https://github.com/QwenLM/Qwen-AgentWorld) - **2026-06-24**。環境の状態遷移を予測する公開言語世界モデル Qwen-AgentWorld-35B-A3B。7 分野の AgentWorldBench も同時公開。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FQwenLM%2FQwen-AgentWorld&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SimWorld](https://github.com/SimWorld-AI/SimWorld) - Unreal Engine 5 上に構築されたオープンエンドの高リアリティシミュレータ。複雑な物理・社会環境で自律 AI エージェントをテスト。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSimWorld-AI%2FSimWorld&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Newton](https://github.com/newton-physics/newton) - 🆕 ⚡ **v1.5.1、2026-08-28**。NVIDIA Warp を基盤とする GPU 加速ロボット物理エンジン。NVIDIA、Google DeepMind、Disney Research が開発に貢献。Apache-2.0。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fnewton-physics%2Fnewton&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [NVIDIA Isaac Lab](https://github.com/isaac-sim/IsaacLab) - Isaac Sim を基盤に強化学習、模倣学習、評価を提供する公式フレームワーク。シミュレーターと互換性のある安定版、または beta と明記された版を選ぶ。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fisaac-sim%2FIsaacLab&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Genesis](https://github.com/Genesis-Embodied-AI/genesis-world) - ロボット学習と具身 AI のための物理シミュレーション。複数の素材・ロボット形式を扱い、リポジトリ名は `Genesis` から `genesis-world` に移行。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FGenesis-Embodied-AI%2Fgenesis-world&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 📊 ベンチマークとリーダーボード

*評価スイートとライブ順位表。2026-09-08 に確認。*

> **実験条件とともにスコアを読む。** モデル版、ハーネス、データ改訂、利用ツール、再試行・計算予算で結果は変わる。元の条件を確認できない過去の首位スナップショットは削除。再現可能な一次評価と自分の実務タスクの評価を優先する。
>
> [OpenAI の 7 月 8 日 SWE-bench Pro 監査](https://openai.com/index/separating-signal-from-noise-coding-evaluations/)は課題品質の問題を報告。[Terminal-Bench 4.0](https://www.tbench.ai/news/terminal-bench-4-0)も課題と資源を変更しており、版をまたぐ比較には手法の確認が必要。

- [τ²-bench / τ³-bench](https://github.com/sierra-research/tau2-bench) - Sierra のツール・エージェント・ユーザー評価。音声と知識検索も収録。**v1.0.1（2026-07-22）**で banking_knowledge の採点を修正したため、同領域の比較には版の一致が必要。
- [BenchLM](https://benchlm.ai/) - 複数ベンチマークの集計とモデル公開状況の追跡。比較前に各スコアの一次資料、日時、ハーネスを確認。
- [SWE-bench Verified](https://www.swebench.com/) - 人手で選別した GitHub issue 解決タスク 500 件。標準の Bash Only/mini-SWE-agent 条件と独自エージェントの提出結果を区別。
- [GPQA Diamond](https://github.com/idavidrein/gpqa) - 専門家作成の大学院レベル科学問題。データ分割を固定し、プロンプト、ツール、サンプリング条件をスコアと併記。
- [ARC-AGI-2](https://arcprize.org/) - 未知の課題に対する抽象的な視覚推論。公式順位はシステムと計算予算を区別し、すべてを基盤モデル単体の成績とみなさない。
- [ARC-AGI-3](https://arcprize.org/leaderboard) - 未知のルールを学び適応する効率を測る対話型環境。公開当初の点数ではなく公式の費用・性能表示を参照。
- [OSWorld](https://os-world.github.io/) - 実デスクトップ環境で開放的なコンピューター操作を測る基準。エージェント、モデル、操作 API、ステップ上限により結果が変わる。
- [Arena (formerly LMArena / Chatbot Arena)](https://arena.ai/) - 各モダリティの人間の選好を比較。選好順位はタスク達成率や安全性評価とは別の指標。
- [MMLU-Pro](https://github.com/TIGER-AI-Lab/MMLU-Pro) - より難しい選択式問題と公開評価実装を備えた、推論重視の MMLU 拡張。
- [LiveCodeBench](https://livecodebench.github.io/) - 競技プログラミング問題を継続収集。日付で範囲を固定すると、汚染リスクと問題難度の変化を評価しやすい。
- [Humanity’s Last Exam (HLE)](https://agi.safe.ai/) - 専門家レベルの学際ベンチマーク。確定版は 2,500 問で HLE-Rolling は別系統。AIME 数学競技とは別の評価。
- [Terminal-Bench 4.0](https://www.tbench.ai/news/terminal-bench-4-0) - 🆕 ⚡ **2026-08-28**。現行の端末ベンチマーク。資源を再調整し、タスクを修正、飽和・問題事例を除外。タスクと環境予算の変更により、2.x/3.0 との単純比較ではなく再実行が必要。
- [Terminal-Bench-Science 0.1](https://www.tbench.ai/news/terminal-bench-science-0-1) - 🆕 ⚡ **2026-08-27**。生命・物理・地球・数学・工学の専門家が査読した研究ワークフロー 70 件を、再現可能なタスク別テストで評価。
- [Wolfram LLM Benchmarking Project](https://www.wolfram.com/llm-benchmarking-project/) - 英語仕様から Wolfram Language コードを生成する能力を Wolfram が継続評価。
- [Terminal-Bench 2.0 (legacy)](https://www.tbench.ai/news/announcement-2-0) - 89 件の端末タスクを含む旧版。過去の論文を解釈するために掲載し、後継版ではタスクと環境の問題を修正。
- [GDPval](https://openai.com/index/gdpval/) - 44 職種・9 産業の経済的価値がある作業を測る OpenAI の評価。原版の課題・採点と第三者の GDPval 派生ランキングを区別。
- [SWE-bench Pro](https://github.com/scaleapi/SWE-bench_Pro-os) - リポジトリ単位の開発評価。[OpenAI の 2026-07-08 監査](https://openai.com/index/separating-signal-from-noise-coding-evaluations/)は多数の課題品質問題を報告し、以前の採用推奨を撤回。課題を点検し他の評価と併用する。
- [LLM-Stats Live Leaderboard](https://llm-stats.com/llm-updates) - モデル情報・ベンチマークの集約フィード。一次証拠はリンク先のモデルカード、公開案内、評価資料を確認。
- [Gartner Magic Quadrant 2026 — Enterprise AI Coding Agents](https://cursor.com/blog/cursor-leads-gartner-mq-2026) - Cursor を Leader とした Gartner 分析のベンダー掲載要約。市場調査であり、再現可能なモデル性能ベンチマークではない。
- [Terminal-Bench 2.1 (legacy)](https://www.tbench.ai/news/terminal-bench-2-1) - **2026-05-06** 公開。Terminal-Bench 2.0 の課題・環境問題を修正。比較にはタスク版とハーネスの一致が必要。
- [Agent Memory Benchmark (AMB)](https://github.com/vectorize-io/agent-memory-benchmark) - データ、プロンプト、採点、結果を公開する長期エージェント記憶評価。Hindsight チームの作成であることを踏まえて解釈する。
- [Agents’ Last Exam (ALE)](https://snorkel.ai/leaderboard/agents-last-exam/) - 領域専門家と構築する長期の職業ワークフロー評価。公開済み参照セットと全収集データ、将来の課題数目標を区別。
- [JetBrains Kotlin Benchmark](https://blog.jetbrains.com/kotlin/2026/07/introducing-the-kotlin-benchmark-evaluate-ai-coding-agents-on-real-world-kotlin-tasks/) - issue の理解からテストに合格する実装までを測る、JetBrains 公式の Kotlin リポジトリタスク評価。
- [Stripe Agent Benchmark](https://stripe.com/blog/can-ai-agents-build-real-stripe-integrations) - 長い開発工程を通じて完全な統合を作る能力を測る Stripe の評価。単一スコアから本番対応を推定せず、タスク条件を確認する。
- [GAIA Benchmark](https://huggingface.co/spaces/gaia-benchmark/leaderboard) - 推論、閲覧、ツール使用を組み合わせる汎用アシスタント評価。[論文](https://arxiv.org/abs/2311.12983)は 466 問と非公開の評価用正解を説明。

---

## 🖥️ Computer Use / デスクトップエージェント

- [Clickyy](https://github.com/jayamitkatariya/clickyyy) - カーソルを揺らすだけで、画面を見て代わりにクリック・入力・ドラッグ・操作してくれる AI エージェントを呼び出せる（macOS）。オープンソース、MIT。

*OS レベルでデスクトップソフトウェアを見て・操作し・自動化するエージェント。ブラウザ専用エージェントは [🌐 ブラウザと Web エージェント](#-ブラウザと-web-エージェント) 参照。*

- [Perplexity Personal Computer for Windows](https://www.perplexity.ai/hub/blog/personal-computer-on-windows) - 🆕 **2026年7月28日**。Perplexity のマルチモデル・エージェントオーケストレーターが Windows 10/11 に拡大 —— ローカルファイル、ネイティブアプリ + Microsoft 365 スイート、クロスデバイスワークフローを一つのシステムで。Pro/Max/Enterprise 加入者向け。Mac 版（4 月 16 日）と Computex 2026 でプレビューされたハイブリッドローカル / クラウド推論オーケストレーターの延長線上。
- [Claude Computer Use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) - Anthropic の Computer Use 機能 —— Claude が画面を見、マウス / キーボードで任意のソフトウェアを自動化。**2026年8月19日**: コンピュータ利用がベータ解除（`computer_toolset_20260801`、バッチ操作、ベータヘッダ不要）；新規のホスト済みビューポート **browser use** ツールセット `browser_toolset_20260801`；Files / Skills API もベータヘッダ不要（[release notes](https://platform.claude.com/docs/en/release-notes/overview)）。
- [macOS Harness](https://github.com/browser-use/macos-harness) - 🆕 **2026年8月17日**。Browser Use 公式の極薄 macOS ハーネス。1 プロセス + 6 プリミティブ（`see` / `key` / `type` / `click` / `ax` / `script`）と実ブラウザ / ファイル。足りない処理はモデルが途中で書く。MIT、761+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowser-use%2Fmacos-harness&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ChatGPT Agent](https://openai.com/index/introducing-chatgpt-agent/) - Operator（2025 年に廃止）の後継 — ブラウジング、予約、フォーム入力、ウェブタスク自動化のための ChatGPT のエージェントモード。
- [Google Project Mariner](https://deepmind.google/models/project-mariner/) - 📦 **終了**（2026 年 5 月）。ブラウザエージェント研究プロジェクト。機能は Gemini と Chrome に統合された。
- [Microsoft Copilot Agents](https://www.microsoft.com/en-us/microsoft-copilot/) - Microsoft 365 スタック上の自律バックグラウンドエージェント。
- [Open Interpreter](https://github.com/openinterpreter/openinterpreter) - コンピュータへの自然言語インターフェース—— LLM にローカルでコードを実行させる。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopeninterpreter%2Fopeninterpreter&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Manus AI](https://manus.im/) - 🇨🇳 クラウド・ローカルハイブリッドモデルの自律汎用 AI エージェント。調査・コーディング・複雑なマルチステップタスクを処理。
- [Genspark](https://www.genspark.ai/) - mixture-of-agents アーキテクチャのオールインワン自律ワークエージェント。電話も掛けられる。
- [Beam AI](https://beam.ai/) - 成功事例に基づきロジックを洗練させる自己学習デスクトップエージェント。
- [AICraft](https://github.com/Easlie114514/AICraft) - 🆕 ⚠️ 🇨🇳 **未検証**（2026 年 6 月作成、メンテナ 1 名、実績は限定的 —— 網羅性のために掲載。利用前に各自で評価すること）。LLM スキル・MCP ツール・RAG データソース・メモリをホットスワップ可能なモジュールとして扱う Windows デスクトップの「AI 能力ランチャー」。Minecraft の mod のように読み込むという触れ込み。DeepSeek のワンクリック設定、ロール別の感情ポートレート、3 階層メモリ、トークン課金；ポータブル exe でインストール不要。Python FastAPI + React 19 + ChromaDB、Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FEaslie114514%2FAICraft&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsoft Copilot Studio Computer-Using Agents](https://techcommunity.microsoft.com/blog/copilot-studio-blog/computer-using-agents-in-microsoft-copilot-studio-are-now-generally-available/4519427) - **2026 年 5 月 13 日 GA**。Copilot Studio 内で、UI を介して Web サイトやデスクトップアプリを直接操作するエージェントを構築可能 —— Microsoft 365 / Power Platform 全体で利用できる、Claude Computer Use に対する Microsoft 純正の回答。
- [ChatGPT Workspace Agents](https://venturebeat.com/orchestration/openai-unveils-workspace-agents-a-successor-to-custom-gpts-for-enterprises-that-can-plug-directly-into-slack-salesforce-and-more) - **リサーチプレビュー 2026-04-22，クレジット課金化 2026-05-06，EKM 対応 2026-05-07**。OpenAI の Custom GPTs の企業向け後継 —— クラウド側で動き、ファイルアクセス、コード実行、Slack / Google Drive / Salesforce などとのコネクタを持ち、スケジュール実行も可能。Business / Enterprise / Edu / Teachers 向けに提供され、Codex をバックエンドに採用。

---

## 🌐 ブラウザと Web エージェント

*実ブラウザを介して Web と対話するエージェント—— ナビゲーション、クリック、スクレイピング、マルチページワークフローをこなすフレームワークとインフラ。*

- [agent-qa](https://github.com/vostride/agent-qa) - 自然言語で記述した Web・モバイルテストを実行し、UI 操作を自己修復しながら過去の実行から学習する、オープンソースの自己改善型 QA エージェント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvostride%2Fagent-qa&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cloudflare Kitesurf](https://blog.cloudflare.com/kitesurf/) - 🆕 **2026年8月6日（ベータ、Cloudflare Agents Week）**。Cloudflare が AI エージェント専用に設計したサーバーレスブラウザ。Workers 上で動作し、セッションごとに独立・ステートレスで、ピクセル完璧なレンダリングよりもトークン効率と低リソース消費を優先。Puppeteer と Playwright をサポート；スクリーンショットワークロードで **Chromium 比 CPU 3.1 分の 1・メモリ 4.7 分の 1**、Web Platform Tests 21.5 万件超をパス。ベータ期間中は Browser Rendering 経由で無料。制限：動画再生・WebGL・永続認証は非対応。
- [Browser Use](https://github.com/browser-use/browser-use) - AI エージェント向け Python ブラウザー自動化ライブラリ。MIT; [0.13.10](https://github.com/browser-use/browser-use/releases/tag/0.13.10) (2026-09-04).
- [Stagehand](https://github.com/browserbase/stagehand) - Browserbase 製の「ブラウザエージェント用 SDK」—— 型付きの `act` / `extract` / `observe` プリミティブを Playwright の上に提供。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowserbase%2Fstagehand&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Steel Browser](https://github.com/steel-dev/steel-browser) - AI エージェント用オープンソースブラウザ API —— セッション永続化とプロキシローテーションを備えたサンドボックス Chromium。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsteel-dev%2Fsteel-browser&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Skyvern](https://github.com/Skyvern-AI/skyvern) - LLM とコンピュータ・ビジョンでブラウザベースワークフローを自動化。AGPL-3.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSkyvern-AI%2Fskyvern&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentQL](https://github.com/tinyfish-io/agentql) - クエリ言語 + Playwright 統合でセマンティックな Web 抽出。動的 / 乱雑なページでもロバスト。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftinyfish-io%2Fagentql&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hyperbrowser MCP](https://github.com/hyperbrowserai/mcp) - ホステッドのヘッドレスブラウザフリートを MCP サーバーとして公開。標準ツールインターフェースで Claude / GPT / LangChain にプラグイン。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhyperbrowserai%2Fmcp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) - マイクロソフト公式の Playwright サーバーを MCP ツールとして公開。プロダクショングレードの自動化。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmicrosoft%2Fplaywright-mcp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MultiOn](https://theagi.company/) - 📦 ステップ推論 + メモリを内蔵したホステッド型ブラウザエージェントプラットフォーム；multion.ai は現在 AGI, Inc.（theagi.company）にリダイレクト。クローズドコード。
- [Browserbase](https://www.browserbase.com/) - AI エージェント専用のヘッドレスブラウザインフラ —— ステルス、セッション永続化、captcha 処理、オブザーバビリティ。
- [BrowserOS](https://www.browseros.com/) - AI エージェントを内蔵した初のオープンソースブラウザ —— プライバシー優先の Chrome 代替。コードなしで自然言語によるタスク自動化が可能。ローカル優先設計で、Perplexity Comet や Arc の AI 機能と対抗。
- [Vercel Agent Browser](https://github.com/vercel-labs/agent-browser) - AI エージェント向けのヘッドレスブラウザ自動化 CLI。2026 年 6 月リリースで Core Web Vitals（LCP/CLS/TTFB/FCP）用の `vitals` コマンド、SPA ナビゲーション用 `pushstate`、アウトオブプロセスのプラグインシステム、MCP サーバーモード、ホスト環境向け `@agent-browser/sandbox` を追加。Apache-2.0、37K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvercel-labs%2Fagent-browser&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Google Agent Development Kit (ADK)](https://github.com/google/adk-python) - エージェント、ツール、ワークフロー向け Python フレームワーク。2.x 機能系と 1.x 保守系を区別; [v2.8.0](https://github.com/google/adk-python/releases/tag/v2.8.0) (2026-08-26).
- [WebBrain](https://webbrain.one) - 🆕 **2026 年 7 月**。Chrome + Firefox 向けのオープンソース MIT ブラウザ拡張機能。ローカルまたはクラウド LLM で Web タスクを自動化。"Ask モード" は読み取り専用の要約・データ抽出；"Act モード" はクリック・フォーム入力・ナビゲーション。ローカルファーストな設計 —— llama.cpp / Ollama 使用時はデータがデバイスから出ない。
- [Muse Spark 1.1（Web エージェント）](https://artificialanalysis.ai/models/muse-spark) - 🆕 💰 **2026-07-09**。Meta Superintelligence Labs 初の有償エージェントモデル。Meta Model API のパブリックプレビュー経由で提供 — WebArena-Verified で 69.0（首位の Claude Opus 4.8 の 71.2 に次ぐ）。
- [Firecrawl v2](https://github.com/firecrawl/firecrawl) - 🆕 **v2.11.0、2026 年 6 月**。エージェント型 Web スクレイピングプラットフォームの大型アップデート：JavaScript レンダリング改善、ライブクロール Webhook、バッチ URL 処理。150K+ stars。AGPL-3.0（SDK は MIT）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ffirecrawl%2Ffirecrawl&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome) - 🆕 Anthropic のブラウザエージェント Chrome 拡張 — Claude がタブを横断してナビゲート、フォーム入力、操作を実行。⚠️ 2026 年 7 月の研究で悪性拡張によるプロンプトインジェクションのリスクが判明 — 利用前に権限を確認のこと。
- [Perplexity Comet](https://www.perplexity.ai/comet) - Comet Assistant（バックグラウンドエージェント）を備えた Perplexity のエージェント型 AI ブラウザ；2025 年 10 月から無料ティアあり；Perplexity は 2026 年 6 月に Comet 向けに $200M を調達。
- [Safari MCP Server](https://developer.apple.com/safari/technology-preview/) - 🆕 **2026-07-01（Safari Technology Preview 247）**。Apple のネイティブブラウザレベル MCP 統合 —— Safari がブラウジングコンテキスト・タブ管理・ページコンテンツを MCP クライアントへ公開。ネイティブ MCP をサポートした初のメジャーブラウザ。開発者プレビューのみ。

---

## 🗣️ 音声とマルチモーダルエージェント

*音声対応 ・ マルチモーダル AI エージェントプラットフォーム。*

- [ByteDance Seedance 2.5](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) - 🆕 **2026年7月31日**。単発 30 秒の音声 + 映像合成（マルチラウンド延長対応）に対応する初の大規模 AI 動画生成モデル；1 パスで最大**画像 30 枚 + 動画クリップ 10 本 + 音声クリップ 10 個**をマルチモーダル参照入力として使用可能；ローカル動画編集。Jimeng AI と Doubao Pro で展開中；API は BytePlus ModelArk のプレリリース経由。
- [xAI Grok Voice Think Fast 2.0](https://x.ai/) - 🆕 **2026-07-29**（`grok-voice-latest` は 2026-08-05 から自動アップグレード）。次世代音声対音声：初回バイト音声レイテンシ **1.25秒 → 0.70秒**；24言語での書き起こし精度が1.4倍に；推論トークン使用量−60%；$0.08/分。
- [AgentLine](https://agentline.cloud/) - ⚠️ **Unverified.** AI エージェント向けテレフォニー基盤 —— 電話番号の発行、発信／着信、リアルタイム文字起こしを JSON で webhook に流す。エージェント音声パイプライン用途に絞った Twilio の軽量代替を標榜。提出者は有料ユーザー 30+ と主張するが、第三者の採用事実は未確認。
- [ElevenLabs](https://elevenlabs.io/) - 業界トップの AI 音声合成、クローン、会話 AI。**[5 億ドルのシリーズ D、評価額 110 億ドル](https://elevenlabs.io/blog/series-d)**（2026 年 2 月 4 日クローズ、Sequoia リード；累計調達額 7.81 億ドル超）。同時に ARR **5 億ドル**突破 —— 2026 年下半期に入る時点で最も資金力のある音声 AI 専業ベンダー。
- [Vapi](https://github.com/VapiAI/server-sdk-python) - 音声 AI エージェントを構築・テスト・展開するプラットフォーム。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FVapiAI%2Fserver-sdk-python&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Retell AI](https://www.retellai.com/) - プロダクション対応の会話型音声 AI エージェント。
- [Bland AI](https://www.bland.ai/) - 企業向け AI 電話プラットフォーム。
- [Hermes](https://buildwithhermes.com/) - 🆕 ⚠️ **未検証（創業者ベータ）。** 代理店向けホワイトレーベル音声エージェントプラットフォーム：エージェント、ネイティブ CRM、アウト/インバウンドキャンペーン編成、クライアント別従量課金を一体化。$149/月〜。独立した採用実績は未確認。
- [LiveKit Agents](https://github.com/livekit/agents) - リアルタイム音声・映像エージェントフレームワーク。1.8.0 は OpenTelemetry GenAI 規約を採用し、トレース利用者向け移行事項を提供; [livekit-agents@1.8.0](https://github.com/livekit/agents/releases/tag/livekit-agents%401.8.0) (2026-09-05).
- [ByteDance SeedRealtime](https://technode.com/2026/08/05/bytedance-launches-seedrealtime-full-duplex-audio-video-model/) - 🆕 🇨🇳 **2026年8月5日**。ByteDance のネイティブ音声視覚フルデュプレックス LLM——音声・映像・テキストのストリームを連続処理し、リアルタイムに「見て、聞いて、話す」を同時に行う。従来のカスケード型音声エージェントパイプラインを置き換え；豆包（Doubao）アプリに統合。公開 API・モデルウェイトなし。
- [Pipecat](https://github.com/pipecat-ai/pipecat) - 音声・マルチモーダル対話エージェント向け Python フレームワーク。BSD-2-Clause; [v1.8.1](https://github.com/pipecat-ai/pipecat/releases/tag/v1.8.1) (2026-08-27).
- [Vocode](https://github.com/vocodedev/vocode-core) - 💤 **Stale**（最終リリース 2024-06）。音声ベース LLM エージェントライブラリ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fvocodedev%2Fvocode-core&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Bolna](https://github.com/bolna-ai/bolna) - エンドツーエンドのオープンソース音声 AI。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbolna-ai%2Fbolna&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cartesia](https://www.cartesia.ai/) - 超低遅延のリアルタイム会話型音声 AI。
- [Meta Voice AI](https://ai.meta.com/) - 旧 PlayHT/Play.ai チームの技術を Meta AI ・ AI キャラクター、ウェアラブルに統合。Play.ai は 2025-12-31 にサービス終了。
- [Sesame](https://www.sesame.com/) - 感情理解と自然会話を備えた音声 AI コンパニオン。
- [ElevenAgents](https://elevenlabs.io/agents) - 🆕 ElevenLabs のフルスタック音声エージェント基盤（2026 年 4〜5 月更新）。MCP 対応、マルチモーダルメッセージ、会話トピック発見、ナレッジベース検索、ツール呼び出し前の音声制御を提供。音声エージェント基盤として初めて AIUC-1 認証を取得。
- [Cartesia Line](https://cartesia.ai/blog/introducing-line-for-voice-agents) - コードファースト音声エージェント基盤（2025 年 8 月ローンチ）。Cartesia の Sonic TTS + Ink STT 上に構築され、バックグラウンド推論とオンプレデプロイに対応。first audio まで約 40〜90ms。
- [Deepgram Voice Agent API](https://deepgram.com/product/voice-agent-api) - 🆕 STT（Nova-3）+ LLM ルーティング + TTS（Aura-2）+ 通話中 10 言語切り替え対応の Flux 会話型 STT を 1 エンドポイントで束ねた。
- [OpenAI Realtime API (GPT-Realtime-2)](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/) - 🆕 **2026 年 5 月 7 日**。並列ツール呼び出しと 128K コンテキストに対応した GPT-5 クラス推論の音声版；GPT-Realtime-Translate / GPT-Realtime-Whisper と同時リリース。2026-07-06 に gpt-realtime-2.1 / 2.1-mini へ更新（英数字認識・ノイズ処理の改善、低遅延化）。
- [Dograh](https://github.com/dograh-hq/dograh) - オープンソース・セルフホスト型の音声 AI プラットフォーム —— Vapi / Retell のオープン代替。オンプレ運用、Speech-to-Speech または LLM/STT/TTS のいずれも BYOK。ビジュアルワークフロービルダー、MCP ネイティブ、テレフォニー対応。BSD-2-Clause、4K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdograh-hq%2Fdograh&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hume TADA](https://github.com/HumeAI/tada) - テキストと音響を1:1で整列する音声言語モデルで、TADA-1B と多言語 TADA-3B-ML を提供；コードは MIT、重みは Llama 3.2 Community License。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHumeAI%2Ftada&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenYabby](https://github.com/OpenYabby/OpenYabby) - macOS 向けオープンソースの音声駆動型マルチエージェントオーケストレーター — Realtime API + CLI ランナー + マルチチャネル連携。リードエージェントが計画を立て、レビューと QA をサブエージェントに委任します。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenYabby%2FOpenYabby&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Grok Voice Agent Builder](https://x.ai/news/grok-voice-agent-builder) - 🆕 **2026-07-01**。Grok Voice 上で本番音声エージェントを構築する xAI のノーコードプラットフォーム — 無料の電話番号プロビジョニング付きテレフォニー、ナレッジコレクション、ツール / MCP コネクタ、ガードレール、80+ の音声と約 2 分のボイスクローン；ベータ期間中 $0.05/分。
- [GPT Voice](https://openai.com/) - 🆕 **2026-07-23**。ChatGPT Work 向けの OpenAI 音声インターフェース——GPT-Live 技術で動作し、自然言語の音声コマンドでマルチステップエージェントワークフローを指示できる。

---

## 📱 パーソナル AI エージェント

- [OpenClaw](https://github.com/openclaw/openclaw) - チャネル、スキル、メモリ、定期タスクを備える個人エージェントランタイム。2026.9.3 は段階的更新の安全性と性能を改善; [v2026.9.3](https://github.com/openclaw/openclaw/releases/tag/v2026.9.3) (2026-09-08).
- [Rabbit R1](https://www.rabbit.tech/) - ラージアクションモデルを搭載した個人 AI デバイス。
- [Limitless](https://www.limitless.ai/) - 📦 **Meta が買収（2025 年末）**；ペンダントの販売は終了。見・言い・聞いたものをパーソナライズした AI（旧 Rewind）；チームは Meta の AI ウェアラブル部門に統合。
- [Open Interpreter](https://github.com/openinterpreter/openinterpreter) - コンピュータへの自然言語インターフェース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopeninterpreter%2Fopeninterpreter&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [01 Light](https://github.com/OpenInterpreter/01) - 💤 **Stale**（2024-11 以降更新なし）。オープンソースの音声コンピュータインターフェース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenInterpreter%2F01&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Leon](https://github.com/leon-ai/leon) - 自サーバ上に住むオープンソース個人アシスタント。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fleon-ai%2Fleon&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Khoj](https://github.com/khoj-ai/khoj) - ノートやドキュメント、画像を機械的にスキャンして会話できる「第二の脳」。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fkhoj-ai%2Fkhoj&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Humane AI Pin](https://humane.com/) - ⚠️ **2025年2月28日にサービス終了**（HPに買収され、デバイスは廃止）。元々はスクリーンレス・アンビエントコンピューティングのウェアラブル AI デバイス。
- [Arahi AI](https://arahi.ai/) - 個人生産性 + ビジネス自動化アシスタント。
- [Lindy AI](https://www.lindy.ai/) - メール・カレンダー・ワークフロー自動化のノーコード AI エージェント。
- [MuleRun](https://mulerun.com/) - 🆕 繰り返しタスクとバックグラウンド自動化の常駐エージェント。
- [Gemini Intelligence](https://blog.google/products-and-platforms/platforms/android/gemini-intelligence/) - 🆕 **2026 年 5 月 12 日（Android Show: I/O Edition）**。Googlebooks ノート PC、Wear OS、Android Auto、Android XR を横断するプロアクティブな agentic AI 機能群。最新の Samsung Galaxy と Pixel から段階展開。買い物リストからカートを自動作成、スピンクラスの予約、Rambler STT による "フィラー語" 除去などを実現。
- [Gemini Spark](https://gemini.google/overview/agent/spark/) - 🆕 **I/O 2026（2026 年 5 月 19 日）**。Gemini アプリ内の 24/7 自律エージェント — Gmail / Workspace 統合でマルチステッププロセスをプロアクティブに実行；2026 年 7 月 1 日にネイティブ Mac アプリへ拡大。**2026 年 7 月アップデート**：Gemini Ultra から Pro ティアへ拡張；スケジュール調整・メール下書き・受信トレイ整理を自律実行。
- [Gemini Notebook](https://notebooklm.google.com/) - 🆕 **2026 年 7 月（NotebookLM からリブランド）**。リブランドと同時にアップグレード：コード実行・グラフ生成・自動出典引用機能を追加し、既存のオーディオ概要・Q&A 機能と組み合わせて利用可能。
- [QwenPaw](https://github.com/agentscope-ai/QwenPaw) - 🇨🇳 **2026 年 5 月、CoPaw から改称**。Qwen / AgentScope エコシステム下のセルフホスト型パーソナルアシスタント。ローカル優先のメモリ、ホットロード可能な skills、マルチエージェント協調、マルチチャネル（DingTalk / Feishu / WeChat / Discord / Telegram）、ツールガード + skill スキャナを内蔵。Apache-2.0。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentscope-ai%2FQwenPaw&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AI Growth Agents for Marketers](https://github.com/thaolst/ai-growth-agents-for-marketers) - ⚠️ **Unverified**（初期段階）。東南アジアの実際のフィンテックキャンペーンに基づくグロースマーケティング用プロンプトと Python エージェント。キャンペーンブリーフ、MEU プランニング、A/B テスト分析をマルチエージェントワークフローでカバー。Agent Skills 形式 — `npx skills add` でインストール可能。ベトナム語 + 英語のバイリンガル。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fthaolst%2Fai-growth-agents-for-marketers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Microsoft Scout](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) - **Build 2026（2026 年 6 月 2 日）**。OpenClaw フレームワーク上に構築された Microsoft の常時稼働パーソナルエージェント —— クラウド / デスクトップ / Web を横断してプロアクティブに動作し、Teams / Outlook / OneDrive / SharePoint に接続。各エージェントは独自の Entra ID で動作し、ポリシー適合性チェック + 監査トレイルを継続実施。Microsoft Frontier プログラムでプライベートプレビュー、Intune ポリシー + GitHub Copilot ライセンスが必要。
- [Lenovo Qira / Motorola Qira](https://news.lenovo.com/pressroom/press-releases/lenovo-unveils-lenovo-and-motorola-qira/) - **CES 2026（2026 年 1 月 6 日）**。Lenovo と Motorola が共同開発した「パーソナル・アンビエント・インテリジェンス・システム」—— PC / スマホ / タブレット / ウェアラブルを横断するコンテキスト認識 AI。2026 年 Q1 から一部 Lenovo デバイスで展開、その後 Motorola スマホへ。主要 OEM 初のアンビエント AI プレイ。
- [Yao Agents](https://yaoagents.com) - 🇨🇳 **2026 年 5 月**。ローカルファーストの AI 実行プラットフォーム：30+ ドメインの Expert（コーディング・執筆・データ分析・PM）と自律 Robot ワーカー。5 段階パイプライン、Docker サンドボックス隔離、マルチプラットフォームメッセージング、MCP 対応、BYOK モデル設定、デバイス横断編成の Tai Link。オープンソースエンジン：[YaoApp/yao](https://github.com/YaoApp/yao)。
- [AgentArk](https://github.com/agentark-ai/AgentArk) - 🆕 🧪 **2026 年 6 月**（v0.0.1、ベータ — 本番非推奨）。ローカル制御とセキュリティを優先するパーソナル AI OS；GEPA オプティマイザランタイムによる自己学習。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentark-ai%2FAgentArk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [nanobot](https://github.com/HKUDS/nanobot) - 超軽量のオープンソースパーソナル AI エージェント（41K+ stars）。2026 年 4 月のリリース（v0.1.5.x）でスレッドスコープのセッション、自動コンパクトメモリ、Dream コンソリデーション、DeepSeek-V4 対応、Windows 対応を追加。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2Fnanobot&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenBot](https://github.com/CopilotKit/OpenBot) - 🆕 🧪 **2026年8月17日（alpha）**。CopilotKit の自前 AG-UI 同僚プラットフォーム。エージェントごとに専用 PC（ブラウザ / ファイル / 許可ツール）を持ち、権限はフェイルクローズ、画面を見て操作を引き継げる。MIT、2.8K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FCopilotKit%2FOpenBot&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cumora](https://github.com/yetone/cumora) - 🆕 **2026年8月17日**（招待制プレビュー）。人間と AI 同僚が同じ部屋にいるクロスプラットフォームチームチャット。人格 / 記憶 / 自発投稿 / メール。クラウド pod か、ローカルの Claude Code / Codex / Grok Build / Cursor を脳にする BYOA。MIT、3.1K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fyetone%2Fcumora&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 📱 モバイルエージェント

*Android / iOS を操作する GUI エージェント。デスクトップ Computer Use の次のフロンティア。*

- [Mobile-Agent](https://github.com/X-PLUG/MobileAgent) - 🇨🇳 アリババ製の代表的なマルチモーダル電話操作エージェントファミリー（v1 → v3、Mobile-Agent-E、V も）。Android ベンチマークで SOTA。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FX-PLUG%2FMobileAgent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AppAgent](https://github.com/TencentQQGYLab/AppAgent) - 💤 タップやスワイプでスマートフォンアプリを操作するテンセント製マルチモーダルエージェント。初期の影響ある実装；後継は AppAgentX（2025-03）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTencentQQGYLab%2FAppAgent&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Apple Intelligence](https://www.apple.com/apple-intelligence/) - iOS / iPadOS / macOS のオンデバイスエージェント層。App Intents と画面インテリジェントを OS 全体で提供。
- [Samsung Galaxy AI](https://www.samsung.com/us/galaxy-ai/) - 対応 Galaxy デバイスに統合される AI 機能。機種、言語、地域、ネットワーク要件により提供範囲が異なる。
- [Google Gemini for Android](https://gemini.google/) - Android で Google Assistant を置き換える全面 Gemini 駆動のアプリ認識アクション。システム意図と Workspace を含む。
- [Magma](https://microsoft.github.io/Magma/) - Microsoft Research のマルチモーダルエージェント基盤モデル。UI / ロボティクス / 物理動作を統一。
- [mobile-use](https://github.com/minitap-ai/mobile-use) - AI エージェントが Android / iOS の実アプリを人間と同じように操作できるオープンソースフレームワーク（Apache-2.0、2.5K+ stars）—— UI 認識ナビゲーション、自然言語制御。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fminitap-ai%2Fmobile-use&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [agent-device (Callstack)](https://github.com/callstack/agent-device) - **2026 年 2 月**。iOS / Android 実機・シミュレータを自動化する軽量・トークン効率の良い CLI。AI エージェントと CI 向けに設計されたコマンドモデル。MIT、2.6K+ stars。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcallstack%2Fagent-device&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [iOS 27 Siri AI（プレビュー）](https://www.apple.com/ios/) - 🆕 **プレビュー 2026 年 7 月（GA 2026 年秋）**。Apple Intelligence で全面再構築された Siri——クロスアプリコンテキスト認識、自然言語 Shortcuts 自動化、iOS 27 でのマルチ AI モデルマーケットプレイス導入予定。開発者ベータ 2026 年 7 月より利用可。
- [EU Android AI 開放命令](https://ec.europa.eu/) - 🆕 **2026-07-17**。欧州委員会が Google にサードパーティ AI アシスタントへのより深い Android アクセスを命令——カメラ・マイク・アプリ制御 API の開放によりサードパーティ製モバイル AI エージェントへの道を開く。Android 18 での実装期限は 2027 年 8 月。

---

## 🏢 エンタープライズエージェントプラットフォーム

- [GPTBots.ai LoopAgent](https://www.gprbots.ai/) - 🆕 **2026-08-03**。エンタープライズAIエージェント向け本番グレード実行エンジン：サンドボックス化されたコード実行、遅延ロードSkills、バージョン管理されたSystem Identity Prompt Diff、シームレスな人間へのハンドオフコンテキスト要約。⚠️ 未検証（GlobeNewswire発表；一次URL未検証）。
- [Salesforce Agentforce 360](https://www.salesforce.com/agentforce/what-is-new/) - エンタープライズ CRM 用自律 AI エージェント —— 営業・サービス・マーケティング。**Spring 2026 リリース**で、Agentforce Builder（対話型エージェントオーサリング）、Agent Script（決定論的な動作制御）、Agentforce Voice（Amazon Connect / Five9 / Genesys / NiCE / Vonage + SIP）、新 Data 360 上の Intelligent Context が追加。124 か国の顧客で約 85% の問い合わせを自律解決。
- [Microsoft Copilot Studio](https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio) - エンタープライズの Copilot とエージェント構築・カスタマイズ。
- [Gemini Enterprise Agent Platform](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform) - **2026-04-22**（Google Cloud Next '26）。Vertex AI がエンタープライズエージェントの構築・拡大・ガバナンス・最適化ハブへ進化。Gemini 3.1 Pro/Flash、Lyria 3 に加え、サードパーティモデル（Claude Opus / Sonnet / Haiku）もサポート。
- [Google Vertex AI Agent Builder](https://cloud.google.com/products/agent-builder) - **2026 年 4 月に改称** — Vertex AI のエージェント構築機能は現在 Gemini Enterprise Agent Platform（上記参照）の一部：Agent Studio、Model Garden、Google Antigravity オーケストレーション。
- [Amazon Bedrock Agents](https://aws.amazon.com/bedrock/agents/) - 複数ステップのタスクを社内システムをまたいで実行。
- [ServiceNow AI Agents](https://www.servicenow.com/products/ai-agents.html) - 企業 IT サービスマネジメント用 AI エージェント + AI Control Tower。
- [ServiceNow Action Fabric（MCP Server）](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-opens-its-full-system-of-action-to-every-AI-Agent-in-the-enterprise/default.aspx) - 🆕 **2026-05-05**。ServiceNow が AI Platform を任意の AI エージェント（Claude / Copilot / カスタム）に開放。GA の MCP サーバはすべての Now Assist / AI Native SKU に付属。すべてのアクションは AI Control Tower を経由するため、ID 検証・権限スコープ・監査が自動で適用される。OAuth、消費量メータリング、ロールベースのツールパックを標準搭載。Anthropic（Claude Cowork）が最初のデザインパートナー。
- [IBM watsonx Orchestrate](https://www.ibm.com/products/watsonx-orchestrate) - 企業アプリをまたいで作業を自動化する AI アシスタントプラットフォーム。
- [Oracle AI Agents](https://www.oracle.com/artificial-intelligence/) - Oracle Fusion Cloud ERP と統合された企業 AI エージェント。
- [Moveworks](https://www.moveworks.com/) - あらゆるシステムで動作する AI のエンタープライズコパイロットプラットフォーム。ServiceNow による買収が完了（2025-12-15）。
- [UiPath Agentic Automation](https://www.uipath.com/) - RPA ボット資産にエージェント推論を重ねたインテリジェントプロセス自動化。
- [AgentX](https://www.agentx.so/) - チャットボットをプラグアンドプレイで提供しスケーラブルな AI 自動化を提供する企業エージェントソリューション。
- [Sistava](https://sistava.com) - ⚠️ 営業・マーケティング・サポート・採用・オペレーション向けの「オンデマンド AI 従業員」— エージェントが永続メモリを持ってユーザーのツール内で作業；月額 $19 から。
- [Sema4.ai](https://sema4.ai/) - Python ファースト、ガバナンス内蔵の企業 AI エージェントプラットフォーム。
- [SAP Business AI Platform + Autonomous Suite](https://news.sap.com/2026/05/sap-sapphire-sap-unveils-autonomous-enterprise/) - 🆕 **SAP Sapphire 2026（2026-05-12）**。SAP が「Autonomous Enterprise」を発表：統一 AI 基盤としての SAP Business AI Platform；財務・サプライチェーン・調達・HR・CX の既存アプリにエージェントを追加する SAP Autonomous Suite；企業向けエージェントとエージェントワークフローを構築する Joule Studio；Joule Work UX；7 つの Industry AI ソリューション。Joule エージェントを駆動する基盤モデルには Claude も含まれる。
- [Microsoft Agent 365 + Microsoft 365 E7](https://techcommunity.microsoft.com/blog/agent-365-blog/microsoft-365-e7--agent365-from-where-you-are-to-enterprise-ai-at-scale/4519969) - **2026-05-01 GA**、5 月中に拡充。アイデンティティ中心の AI エージェントコントロールプレーン。単体 $15/ユーザー/月、もしくは新しい Microsoft 365 E7「Frontier」スイートに含めて $99/ユーザー/月。5 月の追加で AWS Bedrock / Google Cloud とのレジストリ同期、Intune / Defender プレビューポリシー、エージェント向け SASE を追加。
- [OpenAI Guaranteed Capacity（Compute Annual Pass）](https://openai.com/business/guaranteed-capacity/) - 🆕 **2026-05-19**。企業の AI プロダクト / エージェント / ワークフロー向けに 1 / 2 / 3 年期のコンピュート予約を製品化 —— GPT-5.5 級エージェントの企業導入でコスト / 供給不安を下げるための、Anthropic Priority Tier への製品としての回答。
- [Bristol Myers Squibb ↔ Claude Enterprise](https://news.bms.com/news/corporate-financial/2026/Bristol-Myers-Squibb-Announces-Strategic-Agreement-with-Anthropic-to-Position-Claude-Enterprise-as-the-Shared-Intelligence-Platform-Across-Its-Global-Operations/default.aspx) - **2026-05-20**。BMS が Claude Enterprise を 30,000+ 名の社員の共通インテリジェンス基盤として採用し、創薬・開発・デリバリーの全工程にエージェント型 Claude を組み込む。世界トップ 5 製薬企業では初めての社全体規模での Claude 導入。
- [Kore.ai Artemis Agent Platform](https://www.kore.ai/news/kore-ai-launches-artemis-the-new-generation-of-the-kore-ai-agent-platform-for-building-governing-and-optimizing-enterprise-ai) - 🆕 **2026 年 5 月 21 日（Azure で公開）**。AI ネイティブなエンタープライズエージェント基盤。中核は新しい YAML 風の宣言型 **Agent Blueprint Language (ABL)** で、マルチエージェント workflow を記述する。Kore.ai による Copilot Studio と Agentforce への構造的な挑戦。
- [FPT Flezi Foundry](https://fptsoftware.com/newsroom/news-and-press-releases/press-release/fpt-launches-flezi-foundry-advancing-ai-augmented-delivery-for-global-enterprises) - Agentic Development Lifecycle（ADLC）と Agentic Managed Services（AMS）を、人の監督とサービス管理の下で提供する FPT 基盤。
- [Amazon Bedrock AgentCore Payments](https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-bedrock-agentcore-payments-preview/) - **2026-05-07（プレビュー）**。AgentCore エージェント向けのマネージド決済 — API・MCP サーバー・Web コンテンツ・他エージェントへの自律的支払いを Coinbase（CDP ウォレット、x402 Bazaar）と Stripe（Privy ウォレット）の統合で実現；支出上限とトランザクション可観測性を 4 つの AWS リージョンで提供。
- [OutSystems Agentic Systems Platform](https://www.outsystems.com/) - **2026 年 6 月**。ローコードプラットフォームを「AI ネイティブ」なエージェント開発環境へとピボット。オープンかつ統制された AI 開発、自社モデル持ち込み、マルチエージェント・オーケストレーション、エンタープライズコンプライアンスツールを提供。Copilot Studio や Agentforce に対抗。
- [Databricks Genie One](https://www.databricks.com/blog/introducing-genie-one-genie-ontology-and-genie-agents) - **2026-06-16（Data + AI Summit）**。Databricks が発表したエージェント型「データ同僚」。構造化・非構造化データを横断して作業を自動オーケストレーションし、新しい **Genie Ontology**（組織全体のナレッジグラフ）に基づき Unity Catalog でガバナンス。Genie Agents を同梱、社内テストで初回正答率 84.5%。
- [ZenseAI.AgentMesh（Zensar）](https://www.prnewswire.com/news-releases/zensar-technologies-launches-zenseaiagentmesh-to-accelerate-enterprise-ai-adoption-at-scale-302805437.html) - **2026-06-19**。Zensar のエンタープライズ向けエージェント AI プラットフォーム。「Agentic AI のためのユニバーサルエンタープライズ OS」を掲げ、自律エージェントの発見・構築・デプロイ・ガバナンスを一元化。80+ のプリビルト業種別・横断機能エージェントを備え、6〜8 週間でパイロットから本番への移行を謳う。
- [Meta Business Agent](https://about.fb.com/news/2026/06/meta-business-agent/) - **2026-06-03（グローバル展開）**。Meta が WhatsApp・Instagram・Messenger 向けに展開する AI ビジネスエージェント。問い合わせ対応、カタログ商品の提案、予約受付、リードの選別、成約までを担い、必要に応じて人間へ引き継ぐ。すでに 100 万以上のビジネスが利用。**Meta Business Agent Platform** では企業が独自エージェントを構成し Shopify / Zendesk / Shopee と連携可能 — 現時点では無料で有効化でき、有料サブスクリプションティアが今後登場予定。
- [Snyk Evo Agentic Development Security (ADS)](https://snyk.io/news/snyk-launches-evo-agentic-development-security/) - **2026 年 6 月**。自律 AI コーディングエージェント専用のセキュリティ/ガバナンスプラットフォーム：エージェントが使うもの・行うこと・生成コードをリアルタイムに統制。
- [Cognizant Neuro AI + ServiceNow AI Agent](https://news.cognizant.com/2026-06-18-Cognizant-expands-cross-platform-agentic-AI-with-new-ServiceNow-AI-Agent-interoperability) - **2026 年 6 月**。クロスプラットフォームのエンタープライズ編成：ServiceNow エージェントが Cognizant の Multi-Agent Accelerator 内でネイティブに動作。
- [Talkdesk Agent Builder](https://www.cmswire.com/contact-center/customer-contact-week-2026-capturing-the-ai-announcements-in-contact-center-technology/) - **2026 年 6 月**。ローコードビルダー：ビジネスユーザーが数週間ではなく数時間で本番級 AI エージェントをコンタクトセンターに展開。
- [HelloTwin Digital Authority](https://siliconangle.com/2026/06/24/hellotwin-launches-digital-authority-bring-governed-ai-agents-enterprise/) - **2026 年 6 月**。単一の監査可能な信頼できる情報源として設計された AI ツイン。明確な境界でエージェンティックワークフローをガバナンス。
- [Hellomatik](https://hellomatik.com) - 💰 ⚠️ **フリーミアム / 未検証**。企業のナレッジベースを WhatsApp、メール、Web 全チャネルで回答・販売・予約を行う AI エージェントに変換するプラットフォーム。Shopify、Stripe、Sage 連携対応。チャットから購買へのコンバージョン率 25〜30%（自社報告）。
- [OpenAI Presence](https://openai.com/) - 🆕 **2026-07-22**。OpenAI のエンタープライズ向けエージェントデプロイメントプラットフォーム——顧客サービスや業務オペレーションで AI エージェントを大規模展開。電話サポートの 75% がヒューマンエスカレーションなしで処理（自社発表）。

---

## 📊 エージェント評価とオブザーバビリティ

- [AgentBench](https://github.com/THUDM/AgentBench) - LLM をエージェントとして評価する多次元ベンチマーク。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTHUDM%2FAgentBench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [PerspectiveGap](https://github.com/WhymustIhaveaname/PerspectiveGap) - 🆕 **2026（arXiv 2606.08878）**。**マルチエージェント編成プロンプト作成**の最初のベンチマーク —— 10 種類の通信トポロジー（チェーン・スター・ツリー・メッシュなど）にわたる 110 シナリオ。主要知見：33 モデル平均の合格率は 17.2%；GPT-5.5 が 62.0% でトップ。MIT ライセンスのベンチマークデータ+評価スクリプト；OpenCompass と Inspect Evals（2026年6月、ロールフラグメント割当+自由形式プロンプト作成タスク）にマージ済み。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FWhymustIhaveaname%2FPerspectiveGap&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ClawBench](https://github.com/TIGER-AI-Lab/ClawBench) - 🆕 ブラウザ / Computer-Use エージェント向けのライブ Web ベンチマーク —— **15 カテゴリ・144 の実プラットフォームにまたがる 153 の日常オンラインタスク**（購買、予約、求人応募など）を、オフラインのサンドボックスではなく*本番*サイト上で実行する。インターセプト層が最終的な送信リクエストを捕捉してブロックするため現実世界に副作用は生じず、その後 2 段階の採点（HTTP インターセプト → LLM judge）で、エージェントが正しい内容を送信したかを検証する。主要な結果：フロンティアモデルでもごく一部しか完了できず、Claude Sonnet 4.6 は 33.3%。[論文](https://arxiv.org/abs/2604.08523) · [リーダーボード](https://claw-bench.com) ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTIGER-AI-Lab%2FClawBench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangSmith](https://www.langchain.com/langsmith) - LangChain 公式のデバッグ / 評価 / モニタリングプラットフォーム。
- [Helicone](https://github.com/Helicone/helicone) - オープンソース LLM オブザーバビリティ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHelicone%2Fhelicone&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Braintrust](https://www.braintrust.dev/) - LLM 評価 + 最適化プラットフォーム。
- [Arize Phoenix](https://github.com/Arize-ai/phoenix) - オープンソース LLM オブザーバビリティ + 評価。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FArize-ai%2Fphoenix&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Langfuse](https://github.com/langfuse/langfuse) - セルフホスト可能な LLM 可観測性・評価・プロンプト管理基盤。v4 系は公開済み; [v4.32.0](https://github.com/langfuse/langfuse/releases/tag/v4.32.0) (2026-09-08).
- [OpenLLMetry](https://github.com/traceloop/openllmetry) - OpenTelemetry に基づくオープンソースの LLM オブザーバビリティ。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Ftraceloop%2Fopenllmetry&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Weights & Biases Weave](https://github.com/wandb/weave) - AI アプリの開発・評価・監視ツールキット。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fwandb%2Fweave&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SWE-bench](https://github.com/SWE-bench/SWE-bench) - 実世界のソフトウェア工学課題で LLM を評価するベンチマーク。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FSWE-bench%2FSWE-bench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Terminal-Bench](https://www.tbench.ai/) - ターミナル系コーディングエージェント評価のためのベンチマーク。Harbor Framework がメンテナンス。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fharbor-framework%2Fterminal-bench&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Harbor](https://github.com/harbor-framework/harbor) - 🆕 エージェントと LLM を大規模に評価・最適化するフレームワーク — Terminal-Bench 2.x やカスタムベンチマークを数千のクラウドサンドボックスで実行し、RL ロールアウトを生成；Stanford × Laude Institute のコラボレーション。Apache-2.0。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fharbor-framework%2Fharbor&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Arena (旧 LMArena / LMSYS Chatbot Arena)](https://arena.ai/) - 人間の選好投票によるクラウドソース型 AI ベンチマーク；リーダーボードは現在 LLM・画像生成・コードモデルをカバー。LMSYS → LMArena（2025）→ Arena（2026）。
- [Patronus AI](https://www.patronus.ai/) - 💰 LLM 評価 / レッドチーム企業。現在はエージェント訓練向けのデジタルワールドモデルとシミュレーション基盤を構築するフロンティア研究ラボとして再ポジショニング（$50M シリーズ B）；研究成果に Lynx、FinanceBench、GLIDER。
- [DeepEval](https://github.com/confident-ai/deepeval) - Pytest スタイルの LLM 評価フレームワーク。組み込み 14+ メトリック。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fconfident-ai%2Fdeepeval&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Agenta](https://github.com/agenta-ai/agenta) - オールインワンオープンソース LLMOps。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagenta-ai%2Fagenta&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangSmith SDK](https://github.com/langchain-ai/langsmith-sdk) - クライアント SDK。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flangchain-ai%2Flangsmith-sdk&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AutoEvals](https://github.com/braintrustdata/autoevals) - ベストプラクティスの LLM 評価スコアラーライブラリ。Braintrust 製。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbraintrustdata%2Fautoevals&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [BenchClaw](https://github.com/Agnuxo1/benchclaw) - ⚠️ **Unverified**。8 個の awesome リストのうち 7 個で却下、単独メンテナチームで2 star。**可視性のための掲載**。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAgnuxo1%2Fbenchclaw&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [PromptEden](https://www.prompteden.com) - ⚠️ **Unverified**。商用 SaaS で、ChatGPT / Claude / Gemini / Perplexity / Copilot / Grok がどうブランドを説明するかをモニタリング。同一 PR が 1 日以内に 10 個の awesome リストに提出された。**可視性のための掲載**。
- [Laminar](https://github.com/lmnr-ai/lmnr) - 長時間稼働 AI エージェント専用に設計されたオープンソースのオブザーバビリティ基盤（Apache-2.0、YC S24）。OpenTelemetry ネイティブ、トランスクリプトビュー、Signals、トレース上の SQL クエリ、ブラウザエージェントのセッション再生。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flmnr-ai%2Flmnr&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LangSmith Engine](https://www.langchain.com/blog/interrupt-2026-overview) - **2026 年 5 月（Interrupt 2026）**。LangSmith の自律失敗診断レイヤー —— 本番障害を優先度付き問題にクラスタリングし、トレースとコードを横断して根本原因を特定、人間レビュー用の修正提案を生成。新発の SmithDB（Rust + DataFusion で構築されたエージェントオブザーバビリティ用 DB）と連動。
- [AgentSight](https://github.com/eunomia-bpf/AgentSight) - LLM/コーディングエージェント向けのゼロインストルメンテーション eBPF オブザーバビリティ。エージェントを変更せずに syscall レベル（プロセス、ファイル、ネットワーク）のトレースをキャプチャし、フルスタックの挙動分析を実現。MIT。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Feunomia-bpf%2FAgentSight&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Prismix](https://prismix.dev) - 77 以上の AI サービス（OpenAI、Anthropic、Cursor など）のステータスをリアルタイム監視（ステータスバッジと API 付き）。71 以上のソースから AI ニュースを集約し、80 以上のサーバーを収録する MCP サーバーディレクトリも提供。無料・登録不要。
- [Ceros (by Beyond Identity)](https://www.prnewswire.com/news-releases/ceros-launches-providing-unified-identity-observability-and-governance-for-every-ai-agent-and-workflow-302800721.html) - 🆕 **2026-06-16**。エージェント AI の信頼レイヤー — 統一されたアイデンティティ・可観測性・ガバナンス（発見 / インベントリ、ランタイムポリシー強制、監査証跡）。（同名のインタラクティブコンテンツ企業とは無関係。）
- [Zoom Agent Performance Suite](https://news.zoom.com/introducing-agent-architect-and-agent-performance-suite-for-zoom-virtual-agent/) - **2026-06**。顧客対応シナリオにおける自律エージェントの性能をテスト・検証・最適化する専用スイート。
- [AgentOps](https://github.com/AgentOps-AI/agentops) - 🆕 セッションリプレイ付きのエージェント監視・コンプライアンス・テストツールキット；MCP 接続された任意のエージェントをゼロコンフィグで可観測化する MCP サーバー；5K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAgentOps-AI%2Fagentops&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenTelemetry GenAI Semantic Conventions](https://github.com/open-telemetry/semantic-conventions-genai) - GenAI クライアント・エージェント・ツール呼び出し・MCP 向けの標準化されたスパン / メトリクス / イベント — 任意の OTel バックエンド（Arize、Langfuse、Helicone、Jaeger など）でベンダー中立なトレーシングを実現。コア semconv リポジトリから専用の GenAI リポジトリへ移動。
- [Tracecat](https://github.com/TracecatHQ/tracecat) - 🆕 SOC ワークフロー向けにエージェントの完全なトレースをキャプチャするオープンソースのセキュリティ自動化プラットフォーム — AI エージェントを検知・エンリッチ・対応パイプラインと統合。AGPL-3.0（エンタープライズ版の例外規定あり）。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTracecatHQ%2Ftracecat&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Langfuse v4](https://github.com/langfuse/langfuse/releases/tag/v4.0.0) - 🆕 **v4.0.0、2026-07-29**。セルフホスト可能な LLM オブザーバビリティスタックのメジャーリリース：入力 / 出力 / メタデータ全体の全文検索、新しいフィルタ検索バー、モニターとアラート、そして最大 **165 倍高速**とする Observations API v2 / Metrics API v2 の再構築。
- [AcruxCore](https://github.com/AcruxCore/AcruxCore) - ⚠️ **未検証**（新規リポジトリ、単一メンテナー、ㆵサードパーティの採用実績なし）。セルフホストまたは SaaS 形式の LLM-ops プラットフォーム — Prompt バージョン管理、AI ゲートウェイ、トレーシング、ツールカタログ、評価実行を包括。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAcruxCore%2FAcruxCore&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AOTrust](https://github.com/GitSerge-crypto/aotrust-skills) - ⚠️ **Unverified**（単独保守、独立した採用実績とサービス保証は未確認）。成果物ハッシュと時刻の署名レシートサービス。MIT の仕様・オフライン解析器、MCP、GitHub Action を提供。署名は内容の正しさを証明しない。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FGitSerge-crypto%2Faotrust-skills&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🔬 AI 研究ツール

- [Hugging Face](https://huggingface.co/) - AI コミュニティのプラットフォーム——モデル、データセット、Spaces を集約する ML 研究の事実上のハブ。
- [Hugging Face Transformers](https://github.com/huggingface/transformers) - モデル定義・学習・推論ライブラリ。5.16.1 は GLM-5.3-Flash 対応を追加; [v5.16.1](https://github.com/huggingface/transformers/releases/tag/v5.16.1) (2026-08-26).
- [vLLM](https://github.com/vllm-project/vllm) - LLM 推論サーバー。0.28.0 は Kimi-K3 と DeepSeek V4 の実行最適化を含む; [v0.28.0](https://github.com/vllm-project/vllm/releases/tag/v0.28.0) (2026-08-26).
- [Ollama](https://github.com/ollama/ollama) - ローカルで LLM を走らせる最も簡単な方法。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Follama%2Follama&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LM Studio](https://lmstudio.ai/) - デスクトップでローカル LLM を動かす GUI、複数プロバイダ。
- [SGLang](https://github.com/sgl-project/sglang) - モデル推論フレームワーク。0.5.19 は Qwen3.8 などのモデル連携を追加; [v0.5.19](https://github.com/sgl-project/sglang/releases/tag/v0.5.19) (2026-09-05).
- [llama.cpp](https://github.com/ggml-org/llama.cpp) - C/C++ 高性能 LLM 推論。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fggml-org%2Fllama.cpp&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MLX](https://github.com/ml-explore/mlx) - Apple Silicon 上の機械学習フレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fml-explore%2Fmlx&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Unsloth](https://github.com/unslothai/unsloth) - モデル学習、微調整、強化学習向けオープンソースツール。性能はワークロードに依存。
- [OpenRouter](https://openrouter.ai/) - 1 つの API で 70+ プロバイダーの 400+ AI モデルを一括利用。
- [Weights & Biases](https://wandb.ai/) - ML 実験追跡 + モデル管理。
- [Label Studio](https://github.com/HumanSignal/label-studio) - マルチ型データアノテーションプラットフォーム。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHumanSignal%2Flabel-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [SmithDB](https://www.langchain.com/blog/interrupt-2026-overview) - **2026 年 5 月（Interrupt 2026）**。LangChain がエージェントオブザーバビリティ専用に設計したデータベース。Rust を Apache DataFusion + Vortex 上に構築し、オブジェクトストレージをバックエンドに —— エージェントトレースの容量とアクセスパターンに合わせて設計されている。
- [Strands Evals（AWS）](https://github.com/strands-agents/evals) - 🆕 エージェントワークフロー評価のための AWS 製オープンソースフレームワーク——Case / Experiment / Evaluator 構造、LLM-as-judge 対応；Strands Agents SDK のコンパニオンツール。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstrands-agents%2Fevals&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [DSPy](https://github.com/stanfordnlp/dspy) - プロンプトではなくプログラミングして言語モデルを使うフレームワーク。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fstanfordnlp%2Fdspy&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Elicit](https://elicit.com/) - 🆕 文献レビューとシステマティックレビュー向けの AI 研究アシスタント。非常に大規模な学術論文コーパスを対象とする。**2026-07-15**：公開の [API と MCP サーバ](https://elicit.com/blog/elicit-api) を提供し、エージェントやワークフローから検索・レビュー機能を直接呼べるようにした。**2026-07-17**：論文検索の評価を公開し、BioASQ で他の 5 つの検索システムを上回ったと報告（ベンダー自身による評価）。
- [IdeaHunter](https://ideahunter.today) - ソロ創業者向け AI リサーチツール——公開シグナル、ユーザーの課題、市場エビデンス、MVP スコープ、収益化パスから需要の裏付けがあるアプリ / マイクロ SaaS アイデアを発掘。Freemium。

---

## 📚 学習リソース

### 論文

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) - ReAct パターンを定義した重要な論文。
- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) - LLM が外部ツールの使い方を自主的に学ぶ。
- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) - LLM を使った信じられる人間らしい行動エージェント。
- [LLM-based Autonomous Agents Survey](https://arxiv.org/abs/2308.11432) - LLM ベースの自律エージェントの包括的サーベイ。
- [The Rise and Potential of LLM Based Agents](https://arxiv.org/abs/2309.07864) - LLM エージェントの台頭と可能性。
- [Agent Hospital](https://arxiv.org/abs/2405.02957) - 進化可能な医療エージェントを擁する仮想病院のシミュレータ。
- [ComBodied Agents: a New Paradigm of Human-Centric Agentic AI](https://arxiv.org/abs/2608.10915) - 🆕 **2026年8月11日**。マルチモーダル知覚・縦断的メモリ・人間の状態軌跡を追跡するパーソナル世界モデルを組み合わせた、人間中心のエージェントパラダイム。2026 年 8 月 12 日の Hugging Face デイリーペーパー首位。
- [Co-Evolution in Agentic Systems: Toward Self-Directed Evolution Beyond Human Design](https://arxiv.org/abs/2608.10299) - 🆕 **2026年8月10日**。エージェント間 / エージェントと環境の共進化と、エージェントシステムにおける自己主導的な進化メカニズムのサーベイ。

### コースとチュートリアル

- [DeepLearning.AI — AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) - LangGraph を用いてエージェントを構築する短期コース。
- [DeepLearning.AI — Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/) - マルチエージェント・システムを構築するコース。
- [DeepLearning.AI — A2A Protocol](https://www.deeplearning.ai/short-courses/a2a-the-agent2agent-protocol/) - Google の Agent-to-Agent プロトコルを学べる無料コース。
- [LangChain Academy](https://academy.langchain.com/) - LangGraph を含む LangChain 公式コース。
- [DeepLearning.AI Short Courses](https://www.deeplearning.ai/short-courses/) - 主要フレームワーク / プロトコルをカバーする AI ショートコース。
- [Hugging Face — Building AI Agents](https://huggingface.co/learn/agents-course/) - オープンソースツールで AI エージェントを構築するオープンコース。
- [LLM Agents MOOC (Berkeley)](https://llmagents-learning.org/) - UC Berkeley の LLM エージェントコース（ルートサイトは最新回にリダイレクト）。
- [Microsoft Agent Framework Docs](https://learn.microsoft.com/en-us/agent-framework/) - Microsoft 統合エージェントフレームワークの公式ドキュメント。
- [Hugging Face Agents Course](https://github.com/huggingface/agents-course) - smolagents / LangGraph / Llama-Index でプロダクションエージェントを構築する 5 ユニットの無料コース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhuggingface%2Fagents-course&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Anthropic Cookbook](https://github.com/anthropics/claude-cookbooks) - ツール使用、Computer Use、エージェントパターン、プロンプトエンジニアリング、Claude Code レシピの公式ノートブックス。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fanthropics%2Fclaude-cookbooks&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Google Gemini Cookbook](https://github.com/google-gemini/cookbook) - grounding、関数呼び出し、マルチモーダル、ライブ音声をカバーする Gemini API 公式例。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle-gemini%2Fcookbook&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LLM Course (Maxime Labonne)](https://github.com/mlabonne/llm-course) - 基礎からファインチューニングまでのエンドツーエンド LLM カリキュラム、Colab ノートブック付き。79K star。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmlabonne%2Fllm-course&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Anthropic Courses](https://github.com/anthropics/courses) - Anthropic 公式のプロンプトエンジニアリング、実世界プロンプト、評価、ツール使用のコース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fanthropics%2Fcourses&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hugging Face Robotics Course](https://huggingface.co/learn/robotics-course/unit0/1) - 古典ロボティクスと学習方策を LeRobot、実ロボットデータ、実装演習でつなぐ無料コース。

### キュレートされたリスト

- [awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) - 💤 **Stale**（2025-02 以降更新なし）。E2B 製、プレ 2026 の参考資料。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fe2b-dev%2Fawesome-ai-agents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [awesome-llm-agents](https://github.com/kaushikb11/awesome-llm-agents) - LLM ベースのエージェントリソース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fkaushikb11%2Fawesome-llm-agents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - MCP サーバー実装リスト。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fpunkpeye%2Fawesome-mcp-servers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [awesome-ai-agent-papers (VoltAgent)](https://github.com/VoltAgent/awesome-ai-agent-papers) - 2026 年の AI エージェント研究論文の厳選集——エージェント工学、メモリ、評価、ワークフロー、自律システムを網羅。arXiv から週次更新。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FVoltAgent%2Fawesome-ai-agent-papers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [awesome-cli-coding-agents](https://github.com/bradAGI/awesome-cli-coding-agents) - ターミナルネイティブな AI コーディングエージェント＋オーケストレーション harness の厳選ディレクトリ—— OSS ツール（Pi / OpenCode / Aider / Goose）、プラットフォームエージェント（Claude Code / Codex / Gemini CLI）、並列ランナー、自律ループ。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FbradAGI%2Fawesome-cli-coding-agents&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

---

## 🇨🇳 中国 AI エコシステム

*中国本土のチームによる、または主に中国市場を対象とする重要プロジェクト。中国スタックは、独自のフレームワーク、モデル、開発者文化を持つ並行エコシステムとしてさらに独自色を強めているため掲載。*

*中国ラボの基盤モデル（Qwen / DeepSeek / GLM / Doubao / Kimi / Hunyuan / ERNIE）は [🧠 基盤モデル](#-基盤モデル-2026) の下に直接記載。*

### エージェントプラットフォームとフレームワーク

- [Dify](https://github.com/langgenius/dify) - ビジュアルエージェントビルダー付きオープンソース LLM アプリ開発プラットフォーム。中国テックで支配的なローコードエージェントキャンバス。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flanggenius%2Fdify&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LobeHub](https://github.com/lobehub/lobehub) - エージェント管理プラットフォーム（旧 Lobe Chat）— エージェントを 7×24 稼働に編成し、AI チームの採用 / スケジューリング / レポーティングを提供。トップクラスの TypeScript AI プロジェクト（80K+ stars）。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flobehub%2Flobehub&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Coze Loop](https://github.com/coze-dev/coze-loop) - 🆕 ByteDance Coze チームによるオープンソースエージェント最適化プラットフォーム。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-loop&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [AgentScope](https://github.com/agentscope-ai/agentscope) - アリババ ModelScope のマルチエージェントフレームワーク + ビジュアルデバッグ + 分散実行。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fagentscope-ai%2Fagentscope&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Bisheng](https://github.com/dataelement/bisheng) - オープンエンタープライズ LLM DevOps プラットフォーム：ワークフローエディタ、RAG、エージェントオーケストレーション、ファインチューニング、評価。Apache-2.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdataelement%2Fbisheng&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) - LLM に SOP 役割（PM / アーキテクト / エンジニア）を割り振るマルチエージェント。現在は FoundationAgents org 配下で管理。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FFoundationAgents%2FMetaGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### RAG / ナレッジ

- [FastGPT](https://github.com/labring/FastGPT) - ナレッジベースを中心に設計された LLM プラットフォーム: データ取り込み、RAG、ビジュアルワークフロー。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flabring%2FFastGPT&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [QAnything](https://github.com/netease-youdao/QAnything) - 💤 NetEase Youdao 製の任意のローカルドキュメントを対象にした質問応答。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fnetease-youdao%2FQAnything&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [RAGFlow](https://github.com/infiniflow/ragflow) - スキャン PDF、テーブル、図表に強い深いドキュメント理解 RAG エンジン。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Finfiniflow%2Fragflow&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [LightRAG](https://github.com/HKUDS/LightRAG) - 香港大学 HKUDS の軽量グラフ RAG エンジン。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FHKUDS%2FLightRAG&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### パーソナルと生産性

- [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) - AI ワークスペースエージェント付きオープンソース Notion 代替。AGPL-3.0。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FAppFlowy-IO%2FAppFlowy&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Manus AI](https://manus.im/) - Butterfly Effect（中国発、シンガポールに移転）による汎用自律エージェント。Meta は 2025-12-30 に約 $2B での買収を発表したが、**[中国の発展改革委员会（NDRC）が 2026-04-27 にこの買収を禁止](https://www.theguardian.com/world/2026/apr/27/china-blocks-meta-takeover-manus-ai-agent-developer)**。✅ **2026年8月11日に決着**：北京の命令に従って Meta が買収を解消する中、Manus は[独立企業として運営を再開すると発表](https://www.cnbc.com/2026/08/11/manus-china-meta-acquisition.html)；ユーザーデータの削除プロセスも開始された。
- [Coze (扣子)](https://www.coze.cn/) - ByteDance のノーコードエージェントビルダー。中国本土中心、国際版は coze.com。
- [Qwen App (千问)](https://www.qwen.ai/) - アリババの大衆向けコンシューマーエージェント（通義千問からリブランド）。淘宝 / DingTalk / Quark に統合。
- [Doubao Agents](https://www.doubao.com/) - ByteDance の Doubao モデルファミリーをその上に携載したフラッグシップコンシューマーアシスタント。
- [Resume Roaster](https://resume.roastlabai.com/) - ATS キーワードギャップ分析付きの AI 履歴書診断ツール。履歴書と求人情報をアップロードすると、応募前に何を改善すべきか具体的な AI フィードバックが得られる。競争の激しい求人市場で優位に立ちたい求職者向け。

### 開発者ツール

- [Trae](https://www.trae.ai/) - ByteDance の AI IDE 兼「10x AI コーディングエンジニア」— Cursor に対抗する中国発の最有力チャレンジャー。
- [CoderPlan](https://coderplan.ai/) - 中国開発者向け統合 LLM API ゲートウェイ（Claude / OpenAI / Gemini、Claude Code 一行設定対応）、従量課金制・Alipay & WeChat Pay 対応。
- [Cherry Studio](https://github.com/CherryHQ/cherry-studio) - 中国開発者サークルで最もインストールされているオープンソースデスクトップ LLM クライアント —— マルチプロバイダ会話 + ナレッジベース。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FCherryHQ%2Fcherry-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code) - **2026 年 6 月 6 日**。Moonshot AI の TypeScript / MIT 製ターミナルコーディングエージェント —— 隔離コンテキストで動く coder / explore / plan サブエージェントを内蔵、`/mcp-config` で対話式に MCP を設定。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FMoonshotAI%2Fkimi-code&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Qwen Code](https://github.com/QwenLM/qwen-code) - アリババ Qwen チームのオープンソースターミナルコーディングエージェント — エージェントチーム、自動メモリ、IDE 統合、マルチプロバイダ（OpenAI / Anthropic / Gemini / Qwen）。26K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FQwenLM%2Fqwen-code&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Coze Studio](https://github.com/coze-dev/coze-studio) - ByteDance Coze.com のオープンソース対応版——オールインワン・ビジュアルエージェントビルダー、デバッグ＆デプロイツール付き。Apache-2.0、20K+ stars。![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcoze-dev%2Fcoze-studio&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [ScienceOne 100 / 磐石100](https://english.cas.cn/newsroom/cas-in-media/202604/t20260429_1158251.shtml) - 中国科学院の科学推論エージェントシステム。50+ 中科院研究所、100+ 研究シナリオ、付属 2,000+ 研究ツール。

### 2026 年注目モデル（中国ラボ）

- [Kimi K3](https://huggingface.co/moonshotai/Kimi-K3) - 公開重みマルチモーダルMoE；独自のKimi K3 License。
- [Qwen3.8 family](https://huggingface.co/Qwen/Qwen3.8-27B) - 27BはApache-2.0；MaxフルモデルとFlash-Nextは別のQwen規約。
- [GLM-5.3 / GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3) - 両方とも重みを公開；GLM-5.3は独自ライセンス、FlashはMIT。
- [DeepSeek V4](https://api-docs.deepseek.com/quick_start/pricing/) - 現行APIはPro-0813とFlash-0731；Flash Visionは実験版。
- [Seed 2.1](https://seed.bytedance.com/en/seed2_1) - ByteDanceの汎用Agent・コードモデル；利用方法は公式モデルページを参照。

---

## 📝 比較 — サイドバイサイド表

*2026 年に最もよく出てくる「どれを選ぶ？」の判断マトリクス。*

### 🏗️ エージェントフレームワーク

| ツール | 言語 | 用途 | ライセンス / 条件 |
| --- | --- | --- | --- |
| [LangGraph](https://github.com/langchain-ai/langgraph) | Python / JS | 状態付きグラフ、永続化、中断 | MIT |
| [CrewAI](https://github.com/crewAIInc/crewAI) | Python | エージェントチームとイベント駆動 Flows | MIT |
| [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | Python / .NET | エージェントとグラフワークフロー。Microsoft AutoGen の後継開発先 | MIT |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | Python / TypeScript | 引き継ぎ、ガードレール、セッション、トレース | MIT |
| [Mastra](https://github.com/mastra-ai/mastra) | TypeScript | エージェント、ワークフロー、メモリ、可観測性 | コア Apache-2.0、企業向け例外あり |
| [Google ADK](https://github.com/google/adk-python) | Python | ツール、ワークフロー、マルチエージェント構成 | Apache-2.0 |
| [DSPy](https://github.com/stanfordnlp/dspy) | Python | 型付きモデルプログラムと最適化 | MIT |
| [Agno](https://github.com/agno-agi/agno) | Python | エージェント、チーム、ワークフロー、ナレッジ | Apache-2.0 |

---

### 🧪 サンドボックス（エージェント生成コードを実行）

| ツール | 用途 | 配置 / 状態 | ライセンス / 条件 |
| --- | --- | --- | --- |
| [E2B](https://github.com/e2b-dev/E2B) | サンドボックス内コード実行 | マネージドクラウド。基盤コードは別途提供 | Apache-2.0 |
| [Daytona](https://github.com/daytonaio/daytona) | エージェント開発・実行環境 | マネージドサービス。公開コアは保守終了 | 過去スナップショットの利用条件を確認。現行コアは非公開 |
| [Modal](https://modal.com/) | サーバーレス関数、GPU、サンドボックス | マネージドクラウド | 商用サービス |
| [Microsandbox](https://github.com/superradcompany/microsandbox) | プログラム可能なローカル microVM | セルフホスト | Apache-2.0 |
| [SandboxFusion](https://github.com/bytedance/SandboxFusion) | 多言語コード評価 | セルフホスト。隔離を明示設定 | Apache-2.0 |
| [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | サンドボックス API、SDK、ネットワーク制御 | Docker / Kubernetes。隔離ランタイムを選択 | Apache-2.0 |

コールドスタートの一律数値は掲載しない。イメージ、リージョン、リソース、キャッシュ状態で変わる。

---

### 🌐 ブラウザエージェントスタック

| ツール | 用途 | 配置 / 状態 | ライセンス / 条件 |
| --- | --- | --- | --- |
| [Browser Use](https://github.com/browser-use/browser-use) | モデル駆動のブラウザー自動化 | Python ライブラリ。クラウドは任意 | MIT |
| [Stagehand](https://github.com/browserbase/stagehand) | act / extract / observe | ローカルブラウザーまたは Browserbase | MIT |
| [Steel Browser](https://github.com/steel-dev/steel-browser) | ブラウザーセッションと自動化 API | セルフホストまたはクラウド | Apache-2.0 |
| [Skyvern](https://github.com/Skyvern-AI/skyvern) | 視覚ベースのブラウザーワークフロー | セルフホストまたはクラウド | AGPL-3.0 |
| [AgentQL](https://github.com/tinyfish-io/agentql) | 意味ベースの Web 抽出・自動化 | SDK とホスト API | SDK は MIT。サービスは別条件 |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | MCP 経由のアクセシビリティスナップショットと操作 | ローカル MCP サーバー | Apache-2.0 |

---

### 📊 評価とオブザーバビリティ

| ツール | 用途 | 配置 / 状態 | ライセンス / 条件 |
| --- | --- | --- | --- |
| [Langfuse](https://github.com/langfuse/langfuse) | トレース、評価、プロンプト管理 | クラウド / セルフホスト | コア MIT、企業向け例外あり |
| [Helicone](https://github.com/Helicone/helicone) | LLM ゲートウェイと可観測性 | クラウド / セルフホスト | Apache-2.0 |
| [Arize Phoenix](https://github.com/Arize-ai/phoenix) | OpenTelemetry/OpenInference トレースと評価 | セルフホスト / マネージド提供 | Elastic-2.0 |
| [LangSmith](https://docs.langchain.com/langsmith/self-hosted) | トレース、評価、プロンプト、デプロイ | クラウド。セルフホストは Enterprise 追加契約 | 商用 |
| [Braintrust](https://www.braintrust.dev/docs/admin/self-hosting/architecture) | 実験、データセット、トレース、評価 | データプレーンはセルフホスト可。制御面は SaaS | 商用プラットフォーム |
| [DeepEval](https://github.com/confident-ai/deepeval) | テスト駆動 LLM 評価ライブラリ | ローカルライブラリ。ホスト型基盤は任意 | Apache-2.0 |
| [Agenta](https://github.com/agenta-ai/agenta) | プロンプト実験、評価、可観測性 | クラウド / セルフホスト | コア MIT、企業向け例外あり |
| [OpenLLMetry](https://github.com/traceloop/openllmetry) | OpenTelemetry 計装 | ライブラリ。テレメトリ基盤を別途用意 | Apache-2.0 |

---

### 💻 コーディングエージェント——ヘッドライン選択

| ツール | インターフェース | 用途 | 費用形態 / 提供形態 |
| --- | --- | --- | --- |
| [Claude Code](https://code.claude.com/docs/en/overview) | CLI / IDE | リポジトリ調査、編集、ツール操作 | 有料プランまたは API 課金 |
| [Codex CLI](https://github.com/openai/codex) | CLI | OpenAI コーディングエージェント | クライアントは OSS。モデル利用料金は別 |
| [Cursor](https://www.cursor.com/) | IDE / CLI | エージェント支援開発 | プロプライエタリ。プラン上限あり |
| [Cline](https://github.com/cline/cline) | IDE | 承認付きツール利用型コーディングエージェント | クライアントは OSS。プロバイダー料金は別 |
| [Aider](https://github.com/Aider-AI/aider) | CLI | Git 対応ペアプログラミング | クライアントは OSS。プロバイダー料金は別 |
| [Devin](https://devin.ai/) | Cloud / Desktop | ソフトウェア開発タスクの委任 | 商用サービス |
| [OpenHands](https://github.com/OpenHands/OpenHands) | セルフホスト / クラウド | ソフトウェアエージェント基盤 | コア公開。計算資源とモデル費用は別 |

ベンチマークにはモデル、ハーネス、データセット版、評価日が必要。エディターや CLI の固定性能ではない。

---

### 💰 基盤モデル — API コスト & コンテキスト

*2026-09-08に公式標準 API 料金を確認。100万 token 当たり USD、ツール・税・キャッシュ書込は別。文脈長と最大入力上限は異なる。*

| モデル | 提供元 | コンテキスト | 最大出力 | 入力 $/1M | 出力 $/1M | 注記 |
| --- | --- | --- | --- | --- | --- | --- |
| [GPT-6 Astra](https://developers.openai.com/api/docs/models/gpt-6-astra) | OpenAI | 1.05M | 128K | $10.00 | $50.00 | 一部組織への限定展開；GA 前 |
| [GPT-5.6 Sol](https://developers.openai.com/api/docs/pricing) | OpenAI | 1.05M | 128K | $4.00 | $20.00 | 汎用 Agent 作業 |
| [GPT-5.6 Terra](https://developers.openai.com/api/docs/pricing) | OpenAI | 1.05M | 128K | $2.00 | $12.00 | バランス重視の本番用途 |
| [GPT-5.6 Luna](https://developers.openai.com/api/docs/pricing) | OpenAI | 1.05M | 128K | $0.20 | $1.20 | スループット・コスト重視 |
| [Claude Fable 5.1](https://platform.claude.com/docs/en/about-claude/pricing) | Anthropic | 1M | 128K | $10.00 | $50.00 | キャッシュ読み取り $0.25/M |
| [Claude Opus 5](https://platform.claude.com/docs/en/about-claude/pricing) | Anthropic | 1M | 128K | $5.00 | $25.00 | Opus モデル |
| [Claude Sonnet 5](https://platform.claude.com/docs/en/about-claude/pricing) | Anthropic | 1M | 128K | $2.00 | $10.00 | 標準料金；9月値上げなし |
| [Claude Haiku 4.5](https://platform.claude.com/docs/en/models/overview) | Anthropic | 200K | 64K | $1.00 | $5.00 | 低遅延用途 |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/pricing) | Google | 1,048,576 | 65,536 | $0.75 | $3.75 | 導入料金は2026-12-31まで |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/pricing) | Google | 1M | 65,536 | $2.00 | $12.00 | 入力≤200Kの基本料金 |
| [DeepSeek V4-Pro](https://api-docs.deepseek.com/quick_start/pricing/) | DeepSeek | 1M | 384K | $1.32 / $0.66 | $3.96 / $1.98 | ピーク/オフピーク；キャッシュ未命中 |
| [DeepSeek V4-Flash](https://api-docs.deepseek.com/quick_start/pricing/) | DeepSeek | 1M | 384K | $0.44 / $0.22 | $1.32 / $0.66 | ピーク/オフピーク；キャッシュ未命中 |
| [Grok 4.6](https://x.ai/news/grok-4-6) | SpaceXAI | 500K | — | $2.00 | $6.00 | Fast は2倍の料金 |

表中の OpenAI モデルは272K超の入力で入力・キャッシュ2倍、出力1.5倍；Astraの入力上限は922K。Gemini Proは200K超で別料金。Gemini 3.8 Flashは2027-01-01から$1.50/$7.50。DeepSeekピークはUTC 01:00–04:00と06:00–10:00。キャッシュ・バッチ・地域・サービス階層の加算は公式料金を再確認。

---

### 💻 基盤モデル — ローカルデプロイ

*ライセンスと重み公開を2026-09-08に確認。容量は公称総パラメーター数×0.5 byte、十進GBの計算例であり、実測Q4サイズや最低GPU要件ではない。*

| モデル | パラメーター規模 | 理想4-bit重み容量 | 公式重み | ライセンス |
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

量子化スケール、非量子化テンソル、実行バッファ、KVキャッシュ分を追加確保。MoEの稼働パラメーター数は計算量であり全重み容量ではない。CPUオフロードでGPU常駐量と速度が変わるため、実際の重み・バックエンド・量子化・文脈・同時実行数で測定。重みと推論コードのライセンスは別々に確認。

---

### 🧠 エージェントメモリシステム

| ツール | 用途 | 配置 / 状態 | ライセンス / 条件 |
| --- | --- | --- | --- |
| [Mem0](https://github.com/mem0ai/mem0) | ベクトル・グラフ連携付き永続メモリ | ライブラリ / マネージド基盤 | Apache-2.0 |
| [Basic Memory](https://github.com/basicmachines-co/basic-memory) | Markdown ナレッジと MCP アクセス | ローカル / セルフホスト | AGPL-3.0 |
| [Graphiti](https://github.com/getzep/graphiti) | 時間付きナレッジグラフ | セルフホスト。基盤 DB が必要 | Apache-2.0 |
| [Zep](https://github.com/getzep/zep) | マネージドのエージェントコンテキスト。リポジトリは SDK とサンプル | クラウド。旧 Community Edition は非推奨 | サービスと SDK の条件は別 |
| [Memary](https://github.com/kingjulio8238/Memary) | 実験的エージェントメモリ | 更新停滞。最終 push は 2024-10 | MIT |
| [Hindsight](https://github.com/vectorize-io/hindsight) | retain / recall / reflect | セルフホスト可能なメモリサービス | MIT |
| [Letta](https://github.com/letta-ai/letta) | メモリブロックを管理する状態付きエージェントランタイム | セルフホスト / クラウド | Apache-2.0 |

---

### 🎙️ 音声・オーディオモデル

*2026-09-08確認。認識・TTS・音声対話は異なる製品。遅延は発話終端検出・通信・負荷に依存し、共通条件なしのミリ秒順位は示さない。*

| モデル / API | 用途 | 導入 | ライセンス / アクセス | 実装上の注記 |
| --- | --- | --- | --- | --- |
| [Eleven v3](https://elevenlabs.io/docs/overview/models) | 音声生成 | ホスト型 | 提供元の規約 | 表現力重視TTS；ストリーミング遅延は別途測定 |
| [Whisper large-v3](https://github.com/openai/whisper) | 音声認識 | 公開重み | MIT | オフライン転記；ストリーミングは別実装 |
| [Deepgram Nova-3](https://developers.deepgram.com/docs/models-languages-overview) | 音声認識 | ホスト型 | 提供元の規約 | 音声認識；Auraは別TTS系列 |
| [Gemini 3.1 Flash Live](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview) | 音声対話 | ホスト型 | 提供元の規約 | Live APIプレビュー |
| [GPT-Realtime-2.1](https://developers.openai.com/api/docs/models/gpt-realtime-2.1) | 音声対話 | ホスト型 | 提供元の規約 | Realtime API；テキストと音声は別料金 |
| [Qwen3-ASR](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) | 音声認識 | 公開重み | Apache-2.0 | ストリーミング・オフライン |
| [Qwen3-TTS](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice) | 音声生成 | 公開重み | Apache-2.0 | Base・CustomVoice・VoiceDesignを用途で選択 |
| [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) | 音声生成 | 公開重み | Apache-2.0 | 小型ローカルTTS |
| [Voxtral Realtime](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602) | 音声認識 | 公開重み | Apache-2.0 | ストリーミング転記 |
| [Voxtral TTS](https://docs.mistral.ai/models/voxtral-tts-26-03) | 音声生成 | 公開重み | CC-BY-NC-4.0 | 商用利用は別途許諾 |
| [Muse Voice Transcribe](https://research.meta.ai/blog/introducing-muse-voice-transcribe) | 音声認識 | ホスト型 | 提供元の規約 | ストリーミング認識・話者分離 |
| [MAI-Transcribe-2](https://microsoft.ai/news/mai-transcribe-2-is-the-fastest-most-accurate-and-cheapest-speech-recognition-model-in-the-world/) | 音声認識 | ホスト型 | 提供元の規約 | 話者ラベル・単語タイムスタンプ |

---

### 🎨 画像生成モデル

*2026-09-08時点。同じタスク・サイズ・品質で比較し、token課金とサブスクリプション間で固定の1枚料金を流用しない。*

| モデル | アクセス | 主用途 | 区別すべき点 |
| --- | --- | --- | --- |
| [gpt-image-2](https://developers.openai.com/api/docs/models/gpt-image-2) | ホスト型 | 生成・編集 | token・サイズ・品質により料金が変動 |
| [FLUX.2](https://docs.bfl.ai/quick_start/generating_images) | API / 一部公開重み | 画像生成・参照編集 | Pro/Flex/Dev/Kleinで条件が異なる |
| [Midjourney V8.1 / V8.2 Edit](https://updates.midjourney.com/alpha-changelog-9-2-26/) | Web | 生成・編集 | V8.2 Editはalpha |
| [Stable Diffusion 3.5](https://huggingface.co/stabilityai/stable-diffusion-3.5-large) | 公開重み | セルフホスト画像生成 | Stability AI Community License |
| [Seedream 5.0 Pro](https://seed.bytedance.com/en/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro) | ホスト型 | レイアウト・図文デザイン | ByteDanceの画像系列 |
| [Nano Banana Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image) | ホスト型 | 画像生成・編集 | gemini-3-pro-image |
| [Nano Banana 2](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image) | ホスト型 | 画像生成・編集 | gemini-3.1-flash-image |
| [Nano Banana 2 Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image) | ホスト型 | 効率重視の画像生成 | gemini-3.1-flash-lite-image |
| [Ideogram 4.0](https://ideogram.ai/models/4.0/) | クラウド / 公開量子化重み | 文字描画・レイアウト編集 | 非商用重み；商用ライセンス別途 |

---

### 🎥 動画生成モデル

*2026-09-08時点。標準クリップ長、連続延長、編集タイムライン、アップスケール解像度は別の制限であり、架空の最大仕様に合算しない。*

| モデル | ワークフロー | 導入 | 確認済み制限 / 状況 |
| --- | --- | --- | --- |
| [Gemini Omni Flash 1.1](https://ai.google.dev/gemini-api/docs/omni) | 生成・複数ターン編集 | ホスト型 | プレビュー；アップロード動画編集は地域制限 |
| [Veo 3.1 / Fast / Lite](https://ai.google.dev/gemini-api/docs/veo) | 音声付き動画・フレーム制御 | ホスト型 | プレビュー；1回4/6/8秒、延長は別制限 |
| [Runway Gen-4.5](https://docs.dev.runwayml.com/guides/models/) | テキスト・画像から動画 | ホスト型 | APIモデル：gen4.5 |
| [Runway Aleph 2.0](https://docs.dev.runwayml.com/guides/models/) | 動画編集 | ホスト型 | APIモデル：aleph2 |
| [Kling VIDEO 3.0](https://ir.kuaishou.com/news-releases/news-release-details/kling-ai-launches-30-model-ushering-era-where-everyone-can-be/) | 音声付き動画生成 | ホスト型 | モデル・モードを確認；標準3分生成とはしない |
| [Seedance 2.5](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) | 参照素材を使う動画 | ホスト型 | 1回30秒生成；延長は別機能 |
| [MiniMax H3](https://huggingface.co/MiniMaxAI/MiniMax-H3) | 動画・ネイティブステレオ音声 | 公開重み | 最大15秒/2K；独自ライセンス |
| [LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) | 複数ショット動画・音声生成 | 公開重み | モデル固有の商用条件 |
| [Sora 2 API](https://developers.openai.com/api/docs/deprecations) | 既存連携のみ | ホスト型 | 非推奨；2026-09-24終了 |

---

### 🔍 RAG フレームワーク

| ツール | 用途 | ライセンス / 条件 |
| --- | --- | --- |
| [LlamaIndex](https://github.com/run-llama/llama_index) | 文書取り込み、索引、検索、エージェントワークフロー | MIT |
| [Haystack](https://github.com/deepset-ai/haystack) | 合成可能な検索・RAG パイプライン | Apache-2.0 |
| [LangChain](https://github.com/langchain-ai/langchain) | モデル、文書ローダー、検索器の連携 | MIT |
| [RAGFlow](https://github.com/infiniflow/ragflow) | 文書解析・検索アプリ基盤 | Apache-2.0 |
| [Cognee](https://github.com/topoteretes/cognee) | グラフ・ベクトルによるナレッジ検索 | Apache-2.0 |
| [txtai](https://github.com/neuml/txtai) | 埋め込み検索・ワークフローパイプライン | Apache-2.0 |
| [Verba](https://github.com/weaviate/Verba) | 📦 アーカイブ済み Weaviate RAG チャット。歴史的参照用 | BSD-3-Clause |

---

### 🗄️ ベクターデータベース

| ツール | 用途 | ライセンス / 条件 |
| --- | --- | --- |
| [Qdrant](https://github.com/qdrant/qdrant) | フィルター・ハイブリッド検索対応のベクトル DB | Apache-2.0 |
| [Weaviate](https://github.com/weaviate/weaviate) | キーワード・ベクトル検索対応 DB | BSD-3-Clause |
| [Pinecone](https://www.pinecone.io/) | マネージドのベクトル DB サービス | 商用サービス |
| [Chroma](https://github.com/chroma-core/chroma) | ローカル／サーバーモードとクラウド提供を持つ埋め込み DB | Apache-2.0 |
| [Milvus](https://github.com/milvus-io/milvus) | 分散ベクトル DB。3.x と 2.6.x は別リリース系 | Apache-2.0 |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL のベクトル類似検索拡張 | PostgreSQL |
| [FAISS](https://github.com/facebookresearch/faiss) | 類似検索ライブラリ。永続化とサーバー機能は別途統合 | MIT |

---

### 📱 パーソナル AI アシスタント（2026）

| ツール | 用途 | ホスト / モデルアクセス |
| --- | --- | --- |
| [OpenClaw](https://github.com/openclaw/openclaw) | メッセージチャネル、スキル、メモリ、定期タスク | セルフホストのランタイム。ローカル／ホストモデル |
| [Khoj](https://github.com/khoj-ai/khoj) | 個人ナレッジ検索とリサーチ | セルフホスト / マネージド提供 |
| [Jan](https://github.com/janhq/jan) | デスクトップのモデルチャット | ローカルモデルと外部プロバイダー連携 |
| [LM Studio](https://lmstudio.ai/) | ローカルモデル管理、チャット、API サーバー | デスクトップアプリ。ハードウェアとモデルに依存 |
| [Perplexity](https://www.perplexity.ai/) | 検索付き回答とリサーチ | マネージドサービス |
| [Claude](https://claude.ai/) | チャット、プロジェクト、接続ツール | マネージドサービス。機能はプラン別 |
| [Zo Computer](https://zo.computer/) | エージェント支援付き個人クラウドコンピューター | マネージドのクラウドコンピューター |

---

### 🔌 MCP サーバー — 主要インテグレーション

| ツール | 用途 | 認証 / 状態 |
| --- | --- | --- |
| [GitHub MCP](https://github.com/github/github-mcp-server) | リポジトリ、Issue、PR、Actions | 公式のリモート／ローカルサーバー。権限を限定 |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | ブラウザー自動化 | ローカルプロセス。ブラウザーセッションの権限に注意 |
| [Filesystem MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) | ローカルファイルアクセス | リファレンス実装。許可ディレクトリを限定 |
| [Brave Search MCP](https://github.com/brave/brave-search-mcp-server) | Web、画像、動画、ニュース検索 | Brave 公式サーバー。API キー |
| [Notion MCP](https://developers.notion.com/guides/mcp/overview) | Notion ワークスペースへのアクセス | 公式リモートサーバー、OAuth。旧ローカル版より推奨 |
| [Slack reference](https://github.com/modelcontextprotocol/servers-archived) | 旧 Slack サンプル | 📦 アーカイブ済み、保守なし |
| [PostgreSQL reference](https://github.com/modelcontextprotocol/servers-archived) | 旧 PostgreSQL サンプル | 📦 アーカイブ済み、本番向け推奨ではない |
| [Google Maps reference](https://github.com/modelcontextprotocol/servers-archived) | 旧 Maps サンプル | 📦 アーカイブ済み、保守なし |

公式管理でも独立したセキュリティ監査済みとは限らない。権限、出所、保守状況、ネットワークアクセスを個別に確認する。

---

### 🏢 エンタープライズ AI エージェントプラットフォーム

| ツール | 用途 | 導入上の確認事項 |
| --- | --- | --- |
| [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | Python/.NET エージェントとワークフロー | MIT ライブラリ。基盤は別途選択 |
| [Salesforce Agentforce](https://www.salesforce.com/agentforce/) | Salesforce 業務フロー向けエージェント | 製品契約とデータ範囲を確認 |
| [SAP Joule](https://www.sap.com/products/artificial-intelligence/ai-assistant.html) | 役割・業務文脈を使う SAP ワークフロー支援 | 対応 SAP アプリとリージョンを確認 |
| [Google Gemini Enterprise](https://cloud.google.com/gemini-enterprise) | 企業エージェントと業務データ連携 | Google Cloud 製品。コネクター権限を確認 |
| [IBM watsonx](https://www.ibm.com/products/watsonx) | AI 開発・オーケストレーション・ガバナンス製品 | 配置方式は選択製品による |
| [ServiceNow AI Agents](https://www.servicenow.com/products/ai-agents.html) | ServiceNow データ・ワークフロー統合エージェント | Agent Studio、Agent Fabric、Control Tower は役割が異なる |
| [Dify](https://github.com/langgenius/dify) | 視覚的 LLM アプリ・エージェントワークフロー基盤 | セルフホスト可能。Dify Open Source License に追加条件あり |

製品名やフレームワークのライセンスはコンプライアンスの証明にならない。サービス、地域、契約、制御、データ経路を確認する。

---

### 📏 埋め込みモデル

*公式仕様を2026-09-08確認。「ローカル」は重みが取得可能という意味で、商用許可やハードウェア適合を保証しない。異なるMTEB設定を混在させた概算スコアは削除。*

| モデル | 次元 | 入力上限 | 入力 | 導入 | ライセンス |
| --- | --- | --- | --- | --- | --- |
| [text-embedding-3-large / small](https://developers.openai.com/api/docs/guides/embeddings) | 3072 / 1536 | 8192 | テキスト | ホスト型 | 提供元の規約 |
| [Cohere Embed v4](https://docs.cohere.com/docs/cohere-embed) | 256–1536 | 128K | マルチモーダル | ホスト型 | 提供元の規約 |
| [Gemini Embedding 2](https://ai.google.dev/gemini-api/docs/embeddings) | 128–3072 | 8192 | マルチモーダル | ホスト型 | 提供元の規約 |
| [BGE-M3](https://huggingface.co/BAAI/bge-m3) | 1024 | 8192 | テキスト | 公開重み | MIT |
| [Jina Embeddings v4](https://huggingface.co/jinaai/jina-embeddings-v4) | 128–2048 | 32768 | マルチモーダル | 公開重み | Qwen Research License |
| [Nomic Embed Text v2 MoE](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe) | 256–768 | 512 | テキスト | 公開重み | Apache-2.0 |
| [Voyage 4 / large / lite](https://docs.voyageai.com/docs/embeddings) | 256 / 512 / 1024 / 2048 | 32000 | テキスト | ホスト型 | 提供元の規約 |
| [Voyage Code 4](https://docs.voyageai.com/docs/embeddings) | 256 / 512 / 1024 / 2048 | 32000 | コード・テキスト | ホスト型 | 提供元の規約 |
| [Voyage 4 Nano](https://huggingface.co/voyageai/voyage-4-nano) | 256 / 512 / 1024 / 2048 | 32000 | テキスト | 公開重み | Apache-2.0 |
| [Qwen3-Embedding-8B](https://huggingface.co/Qwen/Qwen3-Embedding-8B) | 32–4096 | 32K | テキスト | 公開重み | Apache-2.0 |
| [Qwen3-Embedding-4B](https://huggingface.co/Qwen/Qwen3-Embedding-4B) | 32–2560 | 32K | テキスト | 公開重み | Apache-2.0 |
| [Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B) | 32–1024 | 32K | テキスト | 公開重み | Apache-2.0 |
| [Qwen3-VL-Embedding-2B / 8B](https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B) | 64–2048 / 4096 | 32K | マルチモーダル | 公開重み | Apache-2.0 |

検索評価に基づいて次元・モダリティ・チャンク長を選ぶ。[Qwen3-VL-Reranker](https://huggingface.co/Qwen/Qwen3-VL-Reranker-8B) は検索後のクエリ・文書ペアを再順位付けし、埋め込み索引の代わりにはならない。互換性のないベクトル空間へ変更する場合は文書を再埋め込みする。

---

### 🛡️ エージェントセキュリティツール

| ツール | 用途 | 配置 / 状態 |
| --- | --- | --- |
| [Snyk Agent Scan (formerly mcp-scan)](https://github.com/snyk/agent-scan) | エージェント、MCP サーバー、スキルを検出・検査 | CLI。出力スキーマは実験段階 |
| [Lakera Guard](https://www.lakera.ai/) | プロンプトインジェクション検知 | 商用サービス |
| [Zenity](https://www.zenity.io/) | 企業向けエージェントセキュリティ・ガバナンス | 商用プラットフォーム |
| [Prompt Armor](https://promptarmor.com/) | プロンプトインジェクション検知 | 商用サービス |
| [Azure Prompt Shields](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection) | 直接・間接プロンプト攻撃を検知 | Azure AI Content Safety |
| [Rebuff](https://github.com/protectai/rebuff) | 旧プロンプトインジェクション検知ツール | 📦 アーカイブ済み、保守終了 |

検知は防御の一層であり、隔離境界や悪意ある指示が実行されない保証ではない。

---

### 🖥️ コンピュータ使用 & デスクトップエージェント

| ツール | 用途 | 配置 / 適用範囲 |
| --- | --- | --- |
| [Claude Computer Use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) | モデルによる画面、マウス、キーボード操作 | API。実行環境はアプリ側が提供 |
| [UFO](https://github.com/microsoft/UFO) | Windows アプリ自動化エージェント | Windows。モデルバックエンドを設定 |
| [OSWorld](https://github.com/xlang-ai/OSWorld) | コンピューター操作ベンチマークと実行環境 | 評価基盤。一般利用者向けデスクトップエージェントではない |
| [NeMo Agent Toolkit](https://github.com/NVIDIA/NeMo-Agent-Toolkit) | エージェントワークフローの分析・評価・連携 | 汎用ツールキット。デスクトップ操作モデルではない |
| [Screenpipe](https://github.com/screenpipe/screenpipe) | ローカル画面記録とエージェント用コンテキスト | 記録・メモリ層。下流モデルへのアクセスは別設定 |

---

### 🤖 Physical AI プラットフォーム

| プラットフォーム | 用途 | コード / 重み | インターフェース | シミュレーション / 評価 |
|---|---|---|---|---|
| [NVIDIA Isaac GR00T N1.7](https://github.com/NVIDIA/Isaac-GR00T) | 人型 VLA | Apache-2.0 | Policy API / 微調整 | Isaac / LIBERO |
| [ROS 2 Lyrical Luth](https://docs.ros.org/en/rolling/Get-Started/Releases/Release-Lyrical-Luth.html) | ロボット基盤、LTS は 2031 年 5 月まで | オープンソース、ライセンスはパッケージ別 | C++ / Python | Gazebo |
| [Gemini Robotics ER 2](https://ai.google.dev/gemini-api/docs/robotics-overview) | 具身推論 | 独自 / プレビュー | Gemini API / Live API | 自分のロボットツールを接続 |
| [Unitree SDK2](https://github.com/unitreerobotics/unitree_sdk2) | ロボット制御 | BSD-3-Clause | C++ / DDS | 機種別統合 |
| [Boston Dynamics Spot SDK](https://dev.bostondynamics.com/) | Spot アプリ | SDK ソース公開、ハードは独自 | Python / gRPC | ハード / ペイロード統合 |
| [Genesis](https://github.com/Genesis-Embodied-AI/genesis-world) | ロボット物理 | Apache-2.0 | Python | 標準シミュレーション |
| [Newton](https://github.com/newton-physics/newton) | 微分可能ロボット物理 | Apache-2.0 | Python / Warp | 標準シミュレーション |
| [LeRobot](https://github.com/huggingface/lerobot) | ロボット学習 | コード Apache-2.0、重みはモデル別 | Python | 方策 / データ評価 |

---

### 🇨🇳 中国語 AI モデル — ヘッドトゥヘッド

*2026-09-08時点。機能とアクセスの比較であり、共通の中国語ベンチマーク順位ではない。料金と地域条件はエンドポイント別に確認。*

| モデル | 提供元 | 用途 / モダリティ | 重み公開 | ライセンス / アクセス |
| --- | --- | --- | --- | --- |
| [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) | Alibaba | マルチモーダル | ✅ | Apache-2.0 |
| [Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) | Alibaba | マルチモーダル | ✅ | Qwen Community 1.0 |
| [DeepSeek V4-Flash / Pro](https://api-docs.deepseek.com/quick_start/pricing/) | DeepSeek | テキスト推論・コーディング | ✅ | MIT |
| [Kimi K3](https://huggingface.co/moonshotai/Kimi-K3) | Moonshot AI | マルチモーダル | ✅ | Kimi K3 License |
| [GLM-5.3](https://huggingface.co/zai-org/GLM-5.3) | Z.ai | テキスト推論・コーディング | ✅ | GLM-5.3 License |
| [GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash) | Z.ai | マルチモーダル | ✅ | MIT |
| [MiniMax M3](https://huggingface.co/MiniMaxAI/MiniMax-M3) | MiniMax | マルチモーダル | ✅ | MiniMax Community |
| [Hunyuan Hy3](https://huggingface.co/tencent/Hy3) | Tencent | 推論・ツール利用 | ✅ | Apache-2.0 |
| [Step 3.7 Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash) | StepFun | マルチモーダル | ✅ | Apache-2.0 |
| [Seed 2.1](https://seed.bytedance.com/en/seed2_1) | ByteDance | 汎用Agent・コーディング | ホスト型 | 提供元の規約 |
| [ERNIE 5.1](https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/) | Baidu | 推論・生成 | ホスト型 | 提供元の規約 |
| [Baichuan-M3-235B](https://huggingface.co/baichuan-inc/Baichuan-M3-235B) | Baichuan | 医療分野テキスト | ✅ | Apache-2.0 |

---

### 📦 エージェントフレームワーク — TypeScript / JavaScript

| ツール | 用途 | ライセンス / 条件 |
| --- | --- | --- |
| [Mastra](https://github.com/mastra-ai/mastra) | エージェント、ワークフロー、メモリ、MCP | コア Apache-2.0、企業向け例外あり |
| [Vercel AI SDK](https://github.com/vercel/ai) | モデル連携、生成、ツールループ、UI ストリーミング | Apache-2.0 |
| [LangChain.js](https://github.com/langchain-ai/langchainjs) | エージェント・モデル連携ライブラリ | MIT |
| [Genkit](https://github.com/genkit-ai/genkit) | 型付き生成とエージェントフロー | Apache-2.0 |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-js) | 引き継ぎ、ガードレール、ツール、リアルタイムエージェント | MIT |
| [Rivet](https://github.com/Ironclad/rivet) | 視覚的なグラフ型 AI アプリビルダー | MIT |
| [Flowise](https://github.com/FlowiseAI/Flowise) | 📦 アーカイブ済みの視覚的ワークフロービルダー。歴史的参照用 | Apache-2.0 |

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

| ツール | 用途 | 適用範囲 |
| --- | --- | --- |
| [MLX](https://github.com/ml-explore/mlx) | Apple シリコン向け配列計算フレームワーク | デバイス・OS 対応はバインディングによる |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | 量子化対応 C/C++ モデル推論 | モバイルでは機種別ビルドとメモリ設計が必要 |
| [MediaPipe](https://github.com/google-ai-edge/mediapipe) | クロスプラットフォーム ML タスク・パイプライン | 対応モデル・タスクはプラットフォーム別 |
| [Core ML](https://developer.apple.com/documentation/coreml) | Apple アプリ内モデル推論 | モデルを変換し対応 Apple ハードウェアで検証 |
| [Google AI Edge](https://developers.google.com/edge) | オンデバイス AI 導入ツール | 適切なランタイムと対応モデルを選択 |
| [Ollama (mobile client)](https://ollama.com/) | モバイルアプリから Ollama サーバー API を利用 | 推論はサーバー側。自動的に端末内推論にはならない |
| [Qualcomm AI Hub](https://aihub.qualcomm.com/) | 対応デバイス向けモデル最適化・導入 | 対象チップとモデル互換性を確認 |

---

## 🗺️ シナリオガイド — 何に何を使うべきか

*50+ シナリオと適切なツールの対応。毎週更新。*

---

### 🏗️ 構築: コーディングエージェント

以下は構築の出発点であり、性能順位や固定料金の見積もりではない。

**スタートアップ向けコーディングエージェントを作りたい**
→ **Deep Agents** または **OpenHands**、**E2B/OpenSandbox** 実行環境、**Langfuse** トレースから始め、自分のリポジトリの課題で成功率とモデル・計算費用を測る。

**セキュリティ制御付き企業コーディングエージェントを選びたい**
→ ID、監査、保存、ネットワーク要件で **GitHub Copilot**、**Cursor**、**Devin** を比較する。Cursor の [Privacy Mode](https://cursor.com/security) は学習利用を防ぐが、処理がすべて自社基盤内で完結する意味ではない。

**OSS コーディングエージェントをセルフホストしたい**
→ ソフトウェアエージェント基盤なら **OpenHands**、IDE 操作なら **Cline**、ターミナル/Git なら **Aider**。モデルアクセス、隔離、各構成要素のライセンスを確認する。

**ブラウザー自動化・スクレイピングを行いたい**
→ モデル駆動の操作は **Browser Use**、`act/extract/observe` は **Stagehand**、文書抽出は **Firecrawl/Crawl4AI**。認証、動的ページ、失敗からの復旧を検証する。

**文書処理・PDF 分析エージェントを作りたい**
→ **Docling** または **Unstructured** の解析と **LlamaIndex/Haystack** の検索を組み合わせる。ページ・表の出所を保持し、モデル比較表からモデルを選ぶ。

**カスタマーサポートエージェントを作りたい**
→ 視覚的ワークフローは **Dify**、状態付きチケット処理は **LangGraph**、Salesforce は **Agentforce**。実際の問い合わせで有人引き継ぎと権限境界を検証する。

**リサーチ・深掘り調査エージェントを作りたい**
→ マネージド型は **Perplexity**、個人ナレッジは **Khoj**、独自構築は **Deep Agents** と検索・文書ツール。引用を保持し、長さではなく事実の裏付けを評価する。

**データ分析・BI エージェントを作りたい**
→ **LangChain/Deep Agents**、権限を限定した DB 接続、隔離したコード実行を組み合わせる。生成 SQL、計算、グラフ入力を元データと照合する。

**デスクトップ操作を自動化したい**
→ アプリ側の環境と **Claude Computer Use**、Windows には **UFO** を検討する。**Screenpipe** は記録した文脈を提供する層で、完全なデスクトップ操作エージェントとは異なる。

**音声対話エージェントを作りたい**
→ **LiveKit Agents** または **Pipecat** で音声パイプラインを組み、音声表からリアルタイム／STT・LLM・TTS モデルを選ぶ。全体遅延、割り込み、電話費用を測る。

**マルチエージェントを構築したい**
→ 独自グラフは **LangGraph**、引き継ぎは **OpenAI Agents SDK**、構成は **Google ADK**、TypeScript は **Mastra**。委任先の責任と停止条件を定める。

**個人 AI アシスタントをセルフホストしたい**
→ チャネル・定期作業は **OpenClaw**、個人ナレッジは **Khoj**、ローカルチャットは **Jan/LM Studio**。オフラインと判断する前に全ツールとモデル接続先を確認する。

**手軽なマネージド型個人 AI を使いたい**
→ 実際の文章作成、調査、ファイル作業で **ChatGPT**、**Claude**、**Perplexity** を比較し、現在の上限と接続権限を確認する。

**RAG アプリを作りたい**
→ **LlamaIndex/Haystack**、**Qdrant/pgvector**、言語と文書に合う埋め込み・再ランキングから始め、検索と回答生成を別々に評価する。

**財務分析エージェントを作りたい**
→ 状態付きフロー、許可されたデータ、隔離した計算を使う。出所の日時を残し、レビュー前に数値を照合する。

**法務文書エージェントを作りたい**
→ 文書処理は **LlamaIndex/Docling**、用途に応じ公式 **Claude for Legal** プラグインを使う。引用を保持し、結論は資格を持つ担当者が確認する。

**教育・学習支援エージェントを作りたい**
→ **LangGraph** で教材検索と学習進捗の状態を備えるフローを作り、正確性、年齢適合性、教師への引き継ぎを検証する。

**創作支援アシスタントを作りたい**
→ モデル選択表から選んだモデルと、構成・人物設定・改稿を保存する文書ストアを組み合わせ、自分の作品で一貫性を評価する。

**IoT・身体性エージェントを作りたい**
→ Physical AI 分類から **ROS 2**、シミュレーター、ロボット互換ポリシーを選び、実動作前にシミュレーションで検証する。

**ゲーム・シミュレーションエージェントを作りたい**
→ シミュレーション分類から環境・評価課題を選び、観測、行動、報酬、エピソード終了条件を明確にする。

**セキュリティ検査エージェントを作りたい**
→ 対象に応じて決定的なコード検査と **Snyk Agent Scan**、**Garak**、**PyRIT** を組み合わせ、検出内容を検証しテスト環境を隔離する。

**医療事務支援 AI を作りたい**
→ 範囲を限定した検索、アクセス制御、監査可能なフローを用い、承認データで評価する。臨床判断は資格を持つ専門家が行う。

**コードレビュー・PR エージェントを作りたい**
→ 固定した差分をエージェントに渡し、CI・静的検査と組み合わせ、変更された実行経路で指摘を検証する。

**SNS・コンテンツ制作エージェントを作りたい**
→ **n8n/Dify** で下書き、素材制作、レビュー、公開サービスをつなぎ、生成と公開承認を分離する。

**翻訳・ローカライズエージェントを作りたい**
→ 用語集・翻訳メモリと、対象言語対で評価したモデルを組み合わせ、各言語のリンク、変数、形式、用語を検証する。

---

### 🧠 モデル選択

**複雑な多段階推論を処理したい**
→ 実際のタスクで **GPT-6 Astra** と **Claude Fable 5.1** を比較する。**Claude Opus 5**・**GPT-5.6 Sol**・**Gemini 3.8 Flash** は料金と能力の異なる選択肢。導入前に利用権限とAPI表を確認。

**低コストで大量処理したい**
→ 実際の出力長、キャッシュ命中率、再試行を含め **GPT-5.6 Luna**・**Gemini 3.8 Flash**・**DeepSeek V4-Flash** を評価。DeepSeek の **ピーク**時間はUTC 01:00–04:00と06:00–10:00。

**中国語対応の Agent を作りたい**
→ **Qwen3.8**・**Kimi K3**・**DeepSeek V4**・**GLM-5.3 / GLM-5.3-Flash**・**Seed 2.1** を候補に、専門用語とツールschemaを検証。中国語モデル表でホスト型・公開重み・独自ライセンスを区別。

**GPUメモリが約16 GBの場合**
→ 対応する **Phi-4** または **Gemma 4 12B** の量子化版から始め、実メモリ量を測定。35B MoEは稼働3Bだけで収まるとはいえず、全重みとKVキャッシュの保存が必要。

**大容量ワークステーションやGPUクラスタがある場合**
→ 量子化した **Qwen3.8-27B**・**Gemma 4 31B**・**Muse Glimmer 30B** がワークステーション候補。**DeepSeek V4**・**GLM-5.3-Flash**・**Inkling** など大型MoEは大容量の合計メモリやオフロードが必要で、稼働数ではなく容量表を使う。

**コーディング用モデルを選びたい**
→ **Claude Sonnet 5** または **GPT-5.6 Sol** を基準に、難しいタスクでは **GPT-6 Astra**・**Claude Fable 5.1**・**Muse Spark 1.3** を評価。セルフホストでは各ライセンスを確認し **GLM-5.3**・**GLM-5.3-Flash**・**DeepSeek V4**・小型の **Qwen3.8-27B** を比較。

**マルチモーダル理解が必要**
→ **Gemini 3.8 Flash** はテキスト・画像・音声・動画・PDFを入力し、出力はテキスト。**Qwen3.8-27B** と **Gemma 4** はローカル候補、**Inkling** はテキスト・画像・音声入力。正確なモデルの入出力モダリティを確認する。

**500K token以上の文脈が必要**
→ **GPT-6 Astra**・**Claude Fable 5.1 / Sonnet 5**・**Gemini 3.8 Flash**・**DeepSeek V4**・**Kimi K3** を比較。文脈にはユーザー入力以外も含まれるため、出力・思考・モダリティtoken、サービス上限、長文追加料金を考慮。

**リアルタイム音声が必要**
→ 直接の音声対話には **GPT-Realtime-2.1** または **Gemini 3.1 Flash Live** を評価。パイプラインではSTT（**Qwen3-ASR**・**Voxtral Realtime**・**Muse Voice Transcribe**）とTTS（**Qwen3-TTS**・**Kokoro**・**Eleven v3**）を別々に選ぶ。

**画像生成・編集が必要**
→ 実際の参照画像とレイアウトで **gpt-image-2**・**Nano Banana 2 / Pro**・**Seedream 5.0 Pro**・**FLUX.2** を比較。**Midjourney V8.2 Edit** はalpha、**Stable Diffusion 3.5** は独自コミュニティライセンスでローカル重みを提供。

**動画生成・編集が必要**
→ 対話型編集には **Gemini Omni Flash 1.1**、フレーム制御・延長には **Veo 3.1**、制作編集には **Runway Gen-4.5 / Aleph 2.0** が候補。**Seedance 2.5**・**MiniMax H3**・**LTX-2.5** も含め、標準クリップと延長後の長さを区別して評価。

**MITまたはApache-2.0のモデル重みが必要**
→ **Qwen3.8-27B**・**Gemma 4**・**Mistral Small 4**・**DeepSeek V4**・**GLM-5.3-Flash**・**Inkling** が候補。異なる規約の **Qwen3.8-Flash-Next**・**GLM-5.3**・**Kimi K3**・**MiniMax M3**・**Llama** に同じライセンスを適用しない。

**埋め込みと再ランキングが必要**
→ 独自コーパスで **Qwen3-Embedding**・**Qwen3-VL-Embedding**・**Cohere Embed v4**・**Gemini Embedding 2**・**Voyage 4** を評価し、検索候補に専用rerankerを適用。混在した順位ではなく再現率・遅延・総索引費用を比較。

**文書解析やコンテンツ判定が必要**
→ 構造化文書抽出には **Mistral OCR 4.1**、ポリシー分類には **Shieldstral 1.0** など専用インターフェースを利用。信頼度・分類ラベルをワークフローの入力として扱い、代表的な失敗例も検証。

---

### 🏗️ インフラ

導入上の前提を、選んだ構成要素と実際の負荷で検証する。

**すべてローカルで動かしたい**
→ **Ollama/llama.cpp**、ローカル UI、**Qdrant/pgvector** を使う。データがローカルに留まると判断する前に、モデル、埋め込み、テレメトリ、接続、通信設定を確認する。

**API 費用を抑えたい**
→ 現在の料金表を使い、トークン・ツール呼び出し・再試行を測り、安定文脈をキャッシュしモデル外で予算を制限する。入力単価だけでなく成功タスク単価を比較する。

**企業規模へ拡張したい**
→ クォータ、永続状態、再試行、可観測性を備えるランタイムを選び、実際の同時実行数とプロバイダー上限で負荷試験する。

**閉域網・規制環境へ導入したい**
→ 重み、ライセンス、パッケージミラー、テレメトリ、更新、接続先通信を棚卸しする。ライブラリのセルフホストだけで閉域性や法令適合が成立するわけではない。

**エッジ・モバイルへ導入したい**
→ 機種に応じ **Core ML**、**Google AI Edge**、**llama.cpp** を選び、対応する量子化モデルを実機で測定する。メモリ、電力、遅延、品質を確認。

**複数モデルプロバイダーを利用したい**
→ **Bifrost** などのゲートウェイを使い、状態は自分の DB に保存する。プロバイダーごとのツールスキーマ、ストリーミング、エラー、フォールバックを検証する。

**スタック全体をセルフホストしたい**
→ ローカル推論、**Qdrant/pgvector**、**Langfuse**、エージェント基盤を組み合わせる。重み、KV キャッシュ、文脈長、同時実行、実行時負荷からメモリを設計する。

---

### 📊 評価 & モニタリング

エージェント全体のワークフローを測り、評価器の限界を記録する。

**出力品質を評価したい**
→ **DeepEval/LangSmith/Agenta** と代表例・明確な評価基準を使い、ジャッジ得点、決定的検査、人手の抽出評価を併用する。

**エージェントの失敗原因を調べたい**
→ **Langfuse/Phoenix** でツール、モデル要求、遅延、エラー、状態遷移を記録し、プロンプトやモデルを変える前に失敗経路を再現する。

**本番エージェントを監視したい**
→ **OpenTelemetry/OpenInference** と **Langfuse/Phoenix/Helicone** を利用する。結果、費用、遅延、エラーを監視し、機密トレース項目をマスクする。

**モデルやプロンプトを比較したい**
→ **Braintrust/LangSmith/Agenta** の実験機能を使い、データ、ツール、予算、採点を固定しモデルの正確なスナップショットを記録する。

**自分のタスクでモデルを評価したい**
→ 実例と期待結果を持つ未使用評価セットを作り、成功、回帰、費用、遅延を報告する。確率的実行を繰り返し、公開順位で代用しない。

**MCP サーバーの安全性を評価したい**
→ **Snyk Agent Scan** でエージェント・MCP・スキルを検査し、ツール権限、資格情報範囲、出所、隔離・通信制御を確認する。問題未検出は安全保証ではない。

---

### 🌍 エコシステム選択

**OpenAIエコシステムで構築したい**
→ **OpenAI Agents SDK**に、バランス重視の **GPT-5.6 Terra**、大量処理の **GPT-5.6 Luna**、高度な作業の **GPT-6 Astra** を組み合わせ、用途に応じてサンドボックスと評価を追加。

**Anthropic Claudeエコシステムで構築したい**
→ **Claude Code**に **Claude Sonnet 5 / Opus 5 / Fable 5.1**、ツール接続に **MCP**、可観測性に **Langfuse**；モデルと実行基盤を一緒に評価する。

**Google Geminiエコシステムで構築したい**
→ **Google ADK**と **Gemini 3.8 Flash** または **Gemini 3.1 Pro Preview** にGoogle Cloudの導入・評価サービスを組み合わせ、エンドポイントの地域とプレビュー状態を確認。

**中国市場向けに構築したい**
→ 必要な地域のエンドポイントで **Qwen3.8**・**Seed 2.1**・**ERNIE 5.1**・**Kimi K3** を比較する。提供元の選択だけでデータ所在や規制適合は確定しない。

**TypeScript中心のスタックが必要**
→ **Mastra**または **LangChain.js / LangGraph.js**、**Vercel AI SDK**、**Qdrant JS client**、**Langfuse JS SDK** が連携候補；各コンポーネントの現行ライセンスと機能を確認。

**許容的ライセンスの重みでセルフホストしたい**
→ 対応ローカル実行環境で **Qwen3.8-27B** または **Gemma 4** を使い、**LangGraph**・**Qdrant**・監視サービスを追加。必要な全コンポーネントをセルフホストし、任意のホスト型機能は別途確認。

---

## 📋 スタックレシピ — ツール構成例

*以下の八つは構成の出発点です。統合、ライセンス、データフロー、実行品質は実際の環境で確認してください。*

| # | レシピ名 | スタック | 最適対象 |
|---|------------|-------|----------|
| 1 | **軽量コーディング Agent** | Claude Code + E2B + Langfuse | サンドボックスとトレースを別途設定する開発フロー |
| 2 | **ローカルモデル SWE エージェント** | OpenHands + Ollama + Qwen3.8-27B + Qdrant | 各サービスの接続先を設定したローカルモデル開発 |
| 3 | **エンタープライズ RAG** | LlamaIndex + Qdrant + Qwen3-Embedding-8B + Langfuse + Claude Sonnet 5 | 社内文書の検索と評価 |
| 4 | **音声アシスタント** | LiveKit + Whisper (STT) + Claude Sonnet 5 + ElevenLabs v3 (TTS) | 独自音声パイプライン。全体遅延を測定 |
| 5 | **ブラウザ自動化** | Browser Use + Stagehand + Claude Sonnet 5 + Langfuse | 再試行と結果検証を設定するブラウザ操作 |
| 6 | **ローカルプライバシースタック** | Ollama + Qwen3.8-27B + Open WebUI + Qdrant + n8n | 外部接続とテレメトリを無効化したローカルサービス |
| 7 | **TypeScript エージェント** | Mastra + Vercel AI SDK + Gemini 3.8 Flash + Qdrant + Langfuse | TypeScript アプリの出発点 |
| 8 | **中国市場スタック** | Qwen3.8 API + RAGFlow + Milvus + Langfuse | 中国リージョンの接続先。規約とデータフローを確認 |

---

## ⚠️ アンチピック — 使ってはいけないケース

*実際のワークロードで検討する設計上の取捨選択です。普遍的なベンチマーク結果を示すものではありません。*

| ❌ 使わないもの | ❌ 用途 | ✅ 代わりに使う | 理由 |
|----------------|---------|----------------|------|
| LangChain v0.x の例 | 新規の本番エージェント | 現行 LangChain / **LangGraph** のドキュメント | 古い API と依存関係には移行と回帰確認が必要 |
| AutoGPT の旧デモ | 無人の本番処理 | 権限境界と復旧手順を持つ保守中のランタイム | デモは実業務の信頼性を証明しない |
| 慣習で選ぶ GPT-3.5-Turbo | 新しい推論処理 | 自前の評価で検証した現行サポートモデル | 世代だけでなく実測品質、遅延、総費用を比較する |
| Pinecone Starter | データベースのセルフホスト要件 | **Qdrant** または **pgvector** | Starter は現在も無料のホスト型プランであり、セルフホスト製品ではない（[料金](https://www.pinecone.io/pricing/)） |
| 未検証の LLM 出力 | 金融取引の直接実行 | **決定的な検証と実行上限** | 生成された数値と操作には独立した確認が必要 |
| ChatGPT の契約だけ | API 認証や API 課金 | **OpenAI API** のプロジェクトと課金設定 | ChatGPT と API は別の製品窓口 |
| 容量計画のない無料共有推論 | 継続的な本番負荷 | 予約容量または実測したセルフホスト環境 | クォータ、同時実行、コールドスタートは提供元と負荷に依存する |
| 専門家の確認がない自律エージェント | 医療・法律の判断 | モデルと**資格のある担当者による確認** | 流暢な出力は正確性や適切性の証明ではない |
| 未審査のリモート MCP エンドポイント | 機密文書 | 審査済みのローカル処理または契約で承認された処理経路 | 実際のデータフロー、保持期間、権限を確認する。MCP という名称は保証にならない |
| 常にマルチエージェント構成 | 単純な単発タスク | **モデルやツールの直接呼び出し** | 追加の計画や引き継ぎが費用と遅延を増やす場合がある |
| 非公式 Midjourney ラッパー | サポート対象 API への依存 | ベンダーが文書化した画像 API | 公式の Web・Discord コマンド資料は第三者 API のサポートを示さない（[資料](https://docs.midjourney.com/)） |
| 未評価の汎用視覚プロンプト | 高精度の文書 OCR | 文書 OCR パイプラインと代表的な評価セット | 誤り率と費用は言語、レイアウト、スキャン品質に依存する |
| 廃止済みの動画エンドポイント | 新しい動画アプリ | 現在利用できるベンダーの動画 API | 導入前にエンドポイント、地域、サービスの提供期間を確認する |
| 検索評価のないベクトル検索 | 高精度 RAG | 自前のコーパスでハイブリッド検索と再ランクを評価 | 改善幅はデータセットに依存し、普遍的な再現率はない |
| 料金だけで選ぶ高速モデル | 複雑で影響の大きい推論 | タスク別評価と人の確認で高性能モデルを比較 | 製品のティア名は信頼性を保証しない |
| 未公開のモデル名 | 本番依存関係の計画 | **自分が重みや API にアクセスできる**モデル | 公式モデルカードと実際の利用権限を確認する |
| 一つのランキングの点数 | コーディングエージェント選定 | 複数のベンチマークと**自前のリポジトリ評価** | ハーネス、課題分布、テスト品質は異なる |

---

## 🌟 2026 年に注目すべきエージェントプロジェクト

*2026 年の AI エージェント状況を形作ったシグネチャーと出来事。*

- [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol/servers) - AI アプリとツール・データを接続する公開プロトコルと参照サーバー。採用だけで全連携の互換性や安全性が保証されるわけではない。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmodelcontextprotocol%2Fservers&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [A2A Protocol](https://github.com/a2aproject/A2A) - エージェントアプリ間の通信を定める公開プロトコル。Linux Foundation のもとで [v1.0.0 を 2026-03-12 に公開](https://github.com/a2aproject/A2A/releases/tag/v1.0.0)。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fa2aproject%2FA2A&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - リポジトリ読解、コード編集、開発ツール実行を行う Anthropic のコーディングエージェント。評価値はモデルと実行条件に依存。
- [Kiro](https://kiro.dev/) - 要件を設計・タスク・実装へつなぐ、仕様駆動の IDE・CLI 開発ツール。
- [Devin](https://www.cognition.ai/) - リポジトリ作業や長い開発工程を委任するための Cognition のソフトウェアエージェント。
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/) - AutoGen と Semantic Kernel で発展した機能を取り込む、Microsoft のエージェント構築・ワークフロー基盤。
- [OpenAI Codex CLI](https://github.com/openai/codex) - リポジトリ編集、ツール実行、承認・サンドボックス設定を備える OpenAI の公開ターミナル型コーディングエージェント。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fcodex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Browser Use](https://github.com/browser-use/browser-use) - 言語モデルのエージェントを Web の移動・操作につなぐブラウザ自動化ライブラリ。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fbrowser-use%2Fbrowser-use&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Claude Computer Use](https://www.anthropic.com/) - 対応環境でスクリーンショットを読み、マウス・キーボード操作を要求する Claude のツール。タスクの信頼性と権限の評価は必要。
- [Manus AI](https://manus.im/) - 🇨🇳 調査、コーディング、複雑ワークフローを処理できる汎用自律エージェント。Meta の 2025 年 12 月の約 $2B 買収は**[中国 NDRC が 2026-04-27 に禁止](https://www.theguardian.com/world/2026/apr/27/china-blocks-meta-takeover-manus-ai-agent-developer)** — 北京が外資安全審査を用いて AI 分野の買収を阻止した初のケース。**2026年8月11日**、Meta が取引を解消する中、Manus は[独立企業として運営を再開すると発表](https://www.cnbc.com/2026/08/11/manus-china-meta-acquisition.html)。
- [OpenHands](https://github.com/OpenHands/OpenHands) - SDK、ランタイム、リポジトリ作業向け UI を備える公開ソフトウェア開発エージェント基盤。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOpenHands%2FOpenHands&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Dify](https://github.com/langgenius/dify) - 視覚的な編成、検索、モデル統合により LLM アプリとエージェント工程を構築するプラットフォーム。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Flanggenius%2Fdify&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Cline](https://github.com/cline/cline) - エディタ統合、ファイル編集、ターミナルツール、利用者の承認機能を備えるコーディングエージェント。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcline%2Fcline&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Mem0](https://github.com/mem0ai/mem0) - エージェントとの対話をまたいでアプリ固有の文脈を保持・検索するメモリ層。 ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fmem0ai%2Fmem0&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Sora discontinuation](https://help.openai.com/en/articles/20001152-what-you-need-to-know-about-the-sora-app-discontinuation) - Web・アプリは **2026-04-26** に終了。API は **2026-09-24** に終了予定であり、別の停止日程。
- [Kling VIDEO 3.0](https://kling.ai/) - 快手の動画生成シリーズ。2026 年の公開記録として掲載し、根拠のない Sora 後の市場首位とは断定しない。
- [Cohere / Aleph Alpha planned combination](https://cohere.com/blog/cohere-alephalpha-join-forces) - **2026-04-24 発表**の主権 AI 事業統合計画。Schwarz Group は次回調達向けに 5 億ユーロ（約 6 億ドル）の資金供与を表明しており、統合・調達完了とは異なる。
- [ScienceOne 100 / 磐石100](https://english.cas.cn/newsroom/cas-in-media/202604/t20260429_1158251.shtml) - 🇨🇳 **2026-04-28~29**。中国科学院が専門的な科学 AI システムをローンチ。2,000+ 研究ツール、50+ CAS 研究所。
- [Google / Anthropic investment report](https://aibusiness.com/generative-ai/google-could-invest-another-40-billion-anthropic) - **2026 年 4 月報道**。初期 100 億ドルに加え、業績条件付きで最大 300 億ドル。提案上限と実際の投資済み額を区別。
- [OpenAI Deployment Company (DeployCo)](https://openai.com/index/openai-launches-the-deployment-company/) - **2026-05-11 発表**。OpenAI が過半数を所有する導入支援会社に初期投資 40 億ドル超を予定。Tomoro 買収は交割条件・規制承認を要する契約段階。
- [Anthropic ↔ SpaceX Colossus 1](https://www.siliconrepublic.com/business/anthropic-joins-forces-with-spacex-for-colossus-capacity) - **2026-05-06**。Anthropic が 300+ MW / 22 万 GPU 規模の Colossus 1（Memphis）の全キャパシティを押さえる。SpaceX は xAI 買収後に AI インフラ提供者として再位置づけ、Anthropic は Claude Code の有償プランレートを 2 倍化。
- [DeepSeek external-funding report](https://www.techtimes.com/articles/316717/20260516/chinas-state-ai-fund-backs-deepseek-4-billion-round-efficiency-challenge-nvidia-dependent.htm) - ⚠️ **2026 年 5 月の資金調達報道**。初の外部調達交渉として保存。完了、参加者、評価額は本項で独立確認していない。
- [教皇レオ 14 世 → バチカン AI 委員会](https://www.americamagazine.org/vatican-dispatch/2026/05/16/pope-leo-establishes-new-vatican-commission-on-artificial-intelligence/) - **2026-05-16**。教皇レオ 14 世が rescriptum を公布し、バチカンに部署を跨ぐ AI 委員会を設置（人間の統合的発展部を中心に、信仰部、文化・教育部、コミュニケーション部、ポンティフィシアル生命・科学・社会科学アカデミーが参加）。任期 1 年・更新可。初の AI を主題とする回勅が近々出る見込み。
- [Google I/O 2026 — Gemini / Omni / Spark](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - **2026-05-19 基調講演**で Omni、Spark を含む Gemini モデル・エージェント製品の更新を紹介。発表時点の公開段階と現在の提供状況は区別。
- [アリババクラウドサミット杭州 — Qwen 3.7-Max + 自社チップ](https://www.scmp.com/tech/big-tech/article/3354212/alibaba-unveils-new-qwen-model-custom-chips-bid-become-chinas-ai-factory) - 🇨🇳 **2026 年 5 月**。アリババが Qwen 3.7-Max と自社設計チップを同時発表し、「中国の AI ファクトリー」を目指す垂直統合戦略を明確化。
- [OpenAI Guaranteed Capacity（コンピュート年間パス）](https://openai.com/business/guaranteed-capacity/) - 🆕 **2026 年**。企業が推論キャパシティを事前予約できる仕組み。AI インフラが「従量課金」から「容量確保契約」へ移る転換点。
- [JADEPUFFER — agentic threat research](https://www.sysdig.com/blog/jadepuffer-evolves-the-agentic-threat-actor-deploys-ransomware-built-to-destroy-ai-models) - **Sysdig の 2026 年 7 月調査**。Langflow 攻撃・DB 恐喝と、7 月 20 日のモデル資材を狙うランサムウェア報告。自律性は観測行動に基づく研究者の評価。
- [Kimi K3 オープンウェイト](https://huggingface.co/moonshotai/Kimi-K3) - **2026-07-27** 重み公開。構成、配備要件、商用条件はモデルカードと Kimi K3 ライセンスを確認。
- [Robinhood Agentic Trading + Robinhood ↔ MCP](https://robinhood.com/us/en/newsroom/robinhood-is-now-open-to-agents/) - **2026-05-27 ベータ発表**。MCP 経由の利用と Agentic 口座内の取引、通知・権限解除機能を提供。実行権限と法的な資産管理権は異なる。
- [Microsoft Scout + MAI-Code-1-Flash + MAI-Thinking-1（Build 2026）](https://microsoft.ai/news/microsoft-build-2026-mai-keynote-transcript/) - **Build 2026 発表**で Scout と MAI のコード・推論モデルを紹介。製品プレビューやモデル公開を、他社モデルからの全面独立と同一視しない。
- [Meta Business Agent（WhatsApp + Instagram）](https://techcrunch.com/2026/06/03/metas-ai-agent-for-whatsapp-business-is-now-available-globally/) - **2026-06-03 報道**。WhatsApp・Instagram の顧客対話へ Meta のビジネスエージェントを拡張。発表された提供範囲や導入数と独立測定された利用実績は区別。
- [WWDC 2026 — Apple Intelligence / Siri AI](https://www.apple.com/newsroom/2026/06/apple-unveils-next-generation-of-apple-intelligence-siri-ai-and-more/) - **2026-06-08 プレビュー**。画面文脈、アプリ間操作、新しい体験を備える Apple Intelligence と Siri AI を紹介。今後のソフトウェア発表であり、全地域同時正式提供ではない。
- [Google Antigravity 2.0 + Microsoft RAMPART + xAI Grok Build](https://antigravity.google/blog/introducing-google-antigravity-2-0) - **2026-05-14~22**。1 週間で 3 つのエージェントスタックの構造変化：Google が I/O 2026 でスタンドアロンのマルチエージェントデスクトップ + SDK を、Microsoft がエージェント AI 安全性テスト（RAMPART + Clarity）をオープンソース化し、xAI が `grok-code-fast-1` 上の **Grok Build** で CLI エージェント競争に参入。Google / Microsoft / xAI が同じ 8 日間にエージェントプラットフォームを出してきた。

---

## 📅 2026 AI タイムライン

*2026 年の AI 業界の重要マイルストーンと出来事。*

| 日付 | 出来事 | カテゴリ |
|------|--------|-------|
| **2026-01-06** | [Lenovo + Motorola Qira](https://news.lenovo.com/pressroom/press-releases/lenovo-unveils-lenovo-and-motorola-qira/) を CES 2026 で発表 — クロスデバイスの「パーソナル・アンビエント・インテリジェンス」、Q1 から Lenovo、その後 Motorola スマホへ拡大 | 業界 |
| **2026-01** | AMD Ryzen AI 400 シリーズを CES で発表 — 60 TOPS NPU 搭載の主流 AI PC | ハードウェア |
| **2026-02-10** | [Snowflake Agent World Model](https://github.com/Snowflake-Labs/agent-world-model) オープンソース化 — 1,000 個の SQL ベース MCP 合成環境 + RL 訓練済みエージェントを公開。大規模 agentic RL 向け、後に ICML 2026 採択 | 研究 |
| **2026-02** | Claude Opus 4.6 リリース — エージェントチーム能力 | モデル |
| **2026-02** | Claude Sonnet 4.6 リリース — 1M トークンコンテキスト、エージェント型検索 | モデル |
| **2026-02** | Gemini 3.1 Pro リリース | モデル |
| **2026-02** | Qwen3.5 シリーズをローンチ — ネイティブマルチモーダル、エージェント型コーディング | モデル |
| **2026-02** | Qwen3-Coder-Next リリース — 80B MoE コーディングエージェントモデル | モデル |
| **2026-02** | Cursor が 8 並列エージェントをサポート | ツール |
| **2026-02** | GitHub Copilot がエージェントモードとモデルアクセスを拡充 | ツール |
| **2026-02-26** | [1X NEO コンシューマーヒューマノイド予約開始](https://www.1x.tech/discover/neo-home-robot) — $20K の早期アクセス価格、2026 年に米国家庭へ配送 | ロボティクス |
| **2026-03-10** | [Hume TADA](https://github.com/HumeAI/tada) — テキスト・音響整列モデル。コードは MIT、重みは Llama 3.2 Community License。 | モデル |
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
| **2026-04-14** | Gemini Robotics ER-1.6 をアップグレード — 空間推論を強化 | ロボティクス |
| **2026-04-15** | Qwen3.6-35B-A3B をオープンソース化（Apache 2.0） | モデル |
| **2026-04-16** | Claude Opus 4.7 リリース — SWE-bench Verified 87.6%、`/think xhigh` 推論 | モデル |
| **2026-04-17～20** | [Apple CEO 交代を発表](https://www.sec.gov/Archives/edgar/data/0000320193/000114036126015711/ef20071035_8k.htm) — Tim Cook は 15 年を経て **2026-09-01** に Executive Chair へ移行、ハードウェアエンジニアリング担当 SVP の **John Ternus** が CEO に就任。AI 時代における最初の時価総額トップクラスのフロンティアプラットフォーム企業 CEO 交代 | 業界 |
| **2026-04-18** | Qwen3.6-Max-Preview ローンチ — コーディングベンチマークでトップ中国モデル | モデル |
| **2026-04** | Claude Mythos Preview — ゲート型サイバーセキュリティ研究モデル（BenchLM 99、SWE-bench 93.9%） | モデル |
| **2026-04** | Sora アプリを正式シャットダウン | 出来事 |
| **2026-04-20~21** | Moonshot AI が Kimi K2.6 をリリース — 1T MoE、1,000-エージェントスワーム | モデル |
| **2026-04** | Gartner は 2026 年末までに企業アプリの 40% が AI エージェントを組み込むと予測 | 業界 |
| **2026-04** | Google が Anthropic へ最大 $40B の投資をコミット（初期 $10B） | 業界 |
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
| **2026-04-28** | [Anthropic クリエイティブツールコネクター](https://www.anthropic.com/news/claude-for-creative-work) — Adobe / Blender / Autodesk Fusion / Ableton / Splice / Canva Affinity / SketchUp / Resolume 向けの MCP コネクター 9 種 | ツール |
| **2026-04-30** | OpenAI が Trusted Access for Cyber (TAC) プログラムを通じて GPT-5.5-Cyber の提供を開始 | モデル |
| **2026-04-30** | OpenAI が [「エージェント構築の実践ガイド」](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/) を公開 | リソース |
| **2026-05-01** | Anthropic が Claude Security をパブリックベータでリリース — Opus 4.7 駆動のコードベース脆弱性スキャナー | ツール |
| **2026-05-01** | [Microsoft Agent 365](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/) — エージェントの可観測性・ガバナンス・セキュリティ管理基盤が一般提供開始。一部連携はプレビュー。 | 履歴 |
| **2026-05-01** | [Google Workspace MCP Server](https://workspaceupdates.googleblog.com/2026/05/agent-tools-and-security-updates-for-workspace-developers.html) 順次展開 — Workspace ネイティブの MCP サーバ。Gmail / Drive / Calendar / Docs / Sheets を MCP クライアントに公開、OAuth スコープは管理者が制御 | プロトコル |
| **2026-05-04** | Google が [Project Mariner](https://deepmind.google/models/project-mariner/) を終了、ブラウザエージェント技術は Gemini Agent に統合 | ツール |
| **2026-05-04** | Anthropic + Goldman Sachs + Blackstone が **15 億ドルの Claude 導入合弁事業** を発表 — ミッドサイズの Wall Street 企業に Anthropic エンジニアを派遣 | 業界 |
| **2026-05-05** | OpenAI が **GPT-5.5 Instant** を新しい ChatGPT デフォルトモデルとして展開 — 効率重視のアップグレード、ハルシネーション率を約 50% 削減 | モデル |
| **2026-05-05** | Anthropic が **Claude Finance Agents** を発表 — ピッチブック作成、KYC、月次決算など 10 個の金融サービス専用エージェント。Claude Cowork プラグイン / Claude Code スキル / Managed Agents クックブックとして利用可能 | ツール |
| **2026-05-05** | OpenAI ↔ PwC が金融サービスエージェント（予測、支払い）で提携 | 業界 |
| **2026-05-06** | [AWS MCP Server GA](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/) — AWS マネージドの MCP エンドポイント。任意の AWS API をサンドボックス Python と agent skills で扱う。初のハイパースケーラー純正 MCP サーバ | プロトコル |
| **2026-05-07** | Google が **Flow（Veo ベース AI 映像制作） に Agent Mode を準備** — 動画制作パイプラインの自動化 | ツール |
| **2026-05-08** | OpenAI が **GPT-Realtime-2 / Realtime-Translate / Realtime-Whisper** をリリース — 音声エージェント、リアルタイム翻訳、リアルタイム文字起こし | モデル |
| **2026-05-09** | OpenAI が ChatGPT Enterprise で **Workspace Agents** を展開 — 接続されたアプリ間で繰り返し可能なワークフローを自動化 | ツール |
| **2026-05-13** | [Cursor 3.4 クラウドエージェント環境](https://cursor.com/changelog) — マルチリポ、build secrets 付き Dockerfile 設定、キャッシュレイヤー 70% 高速化、環境ごとのバージョン履歴、監査ログ、egress / secrets の限定 | ツール |
| **2026-05-11** | [OpenAI Deployment Company](https://openai.com/index/openai-launches-the-deployment-company/) が発足 — $4B+ の企業サービス部門、TPG / Bain Capital / Brookfield + Bain & Company / Capgemini / McKinsey が出資、Tomoro コンサルタントを取り込む | 業界 |
| **2026-05-11～13** | [SAP Sapphire 2026 Orlando](https://news.sap.com/2026/05/sap-sapphire-sap-unveils-autonomous-enterprise/) — SAP Business AI Platform、**Joule Studio 2.0**、Autonomous Suite（50+ 領域の Joule Assistant + 200+ のエージェント）を発表。Joule Studio 2.0 は 2026-06 以降 GA | 業界 |
| **2026-05-12** | [Gemini in Chrome for Android](https://blog.google/products-and-platforms/products/chrome/bringing-chrome-ai-to-android/) — Google が Android 版 Chrome の Gemini と auto browse を発表。米国で 6 月末から段階的に提供。 | 履歴 |
| **2026-05-12** | [Vapi Series B](https://www.globenewswire.com/news-release/2026/05/12/3292882/0/en/vapi-raises-50m-series-b-as-it-reaches-1-billion-calls-powering-the-next-generation-of-enterprise-voice-ai.html) — Vapi がシリーズ B で 5,000 万ドルの調達と、プラットフォームでの累計 10 億通話を発表。 | 履歴 |
| **2026-05-12** | [Claude for Legal](https://github.com/anthropics/claude-for-legal) — Claude Cowork 上に 20+ の MCP コネクタ（iManage / NetDocuments / DocuSign / LexisNexis / Westlaw / Harvey / Everlaw / Relativity など）と 12 の実務領域プラグイン | ツール |
| **2026-05-12～15** | [Visual Studio 2026 Insiders](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/) — Copilot Chat「Agent Mode」に Agent Skills 作成サポートが追加 | ツール |
| **2026-05-13** | [Claude Code v2.1.141](https://github.com/anthropics/claude-code/releases/tag/v2.1.141) — リリースノートでフック、プラグイン、セッション管理、信頼性の更新を記録。 | 履歴 |
| **2026-05-13** | [Claude for Small Business](https://www.anthropic.com/news/claude-for-small-business) — 15 個の事前構築エージェントワークフロー + QuickBooks / PayPal / HubSpot / Canva / DocuSign / Google Workspace / Microsoft 365 コネクタ、米国 10 都市ツアー | ツール |
| **2026-07-10** | [Cursor 3.11](https://cursor.com/changelog) — サイドチャット、会話履歴検索、きめ細かなエージェント可観測性のための Cloud Agent Hooks | ツール |
| **2026-05-13～16** | [Figure Helix 02 ライブストリーム](https://www.businessinsider.com/figure-ai-turned-a-humanoid-sorting-packages-must-see-tv-2026-5) — F.03 + Helix 02 がパッケージ仕分けラインでストレステスト、初日 8h ~22K、24h ~30K、~72h ~88K 個で機械故障 | ロボティクス |
| **2026-05-13** | [Runway Agent](https://runway.com/news/introducing-runway-agent) リリース — 台本を渡すと Gen-4 / Aleph でマルチショットの完成動画をエンドツーエンドで仕上げる | ツール |
| **2026-05-13** | [Microsoft Copilot Studio CUA GA](https://techcommunity.microsoft.com/blog/copilot-studio-blog/computer-using-agents-in-microsoft-copilot-studio-are-now-generally-available/4519427) — Microsoft 365 / Power Platform 内で UI 駆動の Web / デスクトップエージェントを構築可能に | ツール |
| **2026-05-14** | [Codex mobile preview](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) — iOS・Android の ChatGPT から接続済み macOS Codex ホストを遠隔操作するプレビューを開始。 | 履歴 |
| **2026-05-14** | [OpenClaw v2026.5.12](https://github.com/openclaw/openclaw/releases/tag/v2026.5.12) — 公開リリースにエージェント実行、メッセージング、プラットフォームの修正を収録。詳細は当該版のノートを参照。 | 履歴 |
| **2026-05-14** | [Anthropic ↔ Gates Foundation $200M パートナーシップ](https://www.anthropic.com/news/gates-foundation-partnership) — 4 年間で助成金 + Claude クレジット + エンジニアリングをグローバルヘルス / ライフサイエンス / 教育 / 農業に投入 | 業界 |
| **2026-05-14** | [Anthropic ↔ PwC 提携拡大](https://www.pwc.com/us/en/about-us/newsroom/press-releases/anthropic-pwc-expand-alliance-agentic-enterprise.html) — Claude Code + Cowork のグローバル展開、30,000 名の PwC 専門家を認定、共同 Agentic Enterprise Center of Excellence | 業界 |
| **2026-05-14** | [Genkit Middleware](https://developers.googleblog.com/announcing-genkit-middleware-intercept-extend-and-harden-your-agentic-apps/) — Google の OSS Genkit フレームワークにミドルウェアを追加（TS / Go / Dart）| フレームワーク |
| **2026-05-14** | [Zyphra ZAYA1-8B-Diffusion-Preview](https://www.zyphra.com/post/zaya1-8b-diffusion-preview) — 自己回帰 LLM から変換された初の MoE 拡散言語モデル／AMD GPU で訓練された初の拡散 LM／最大 7.7× 推論高速化 | モデル |
| **2026-05-14** | [Grok Build (初期 beta)](https://x.ai/news/grok-build-cli) — xAI が公開した **grok-code-fast-1** ベースの agentic CLI コーディングエージェント。サブエージェントを隔離環境で並列実行、SuperGrok Heavy 契約者限定 | ツール |
| **2026-05-14** | [iManage MCP Server](https://imanage.com/resources/resource-center/news/mcp-server-available-broader-ai-ecosystem/) 公開 — 法務 / プロフェッショナルサービス系 SaaS として初めて公式 MCP エンドポイントを公開 | ツール |
| **2026-05-16** | [教皇レオ 14 世がバチカン AI 委員会を設置](https://www.americamagazine.org/vatican-dispatch/2026/05/16/pope-leo-establishes-new-vatican-commission-on-artificial-intelligence/) — 部署を跨ぐ AI 委員会。初の AI 主題とする回勅が高い見込み | 業界 |
| **2026-05-16** | [OpenAI ↔ Malta パートナーシップ](https://openai.com/index/malta-chatgpt-plus-partnership/) — 14 歳以上のすべてのマルタ居住者に 2 時間 AI リテラシー講座修了で 1 年間の ChatGPT Plus（"OpenAI for Countries"）| 業界 |
| **2026-05-16** | [DeepSeek 国家ファンド主導 $4B ラウンド](https://www.techtimes.com/articles/316717/20260516/chinas-state-ai-fund-backs-deepseek-4-billion-round-efficiency-challenge-nvidia-dependent.htm) — 国家 AI 産業ファンド + 大ファンド III + Tencent 主導、~$50B 評価額の初めての外部ラウンド | 業界 |
| **2026-05-18** | [OpenAI ↔ Dell Codex 提携](https://openai.com/news/company-announcements/) — ハイブリッド / オンプレミス企業環境へ Codex を拡張 | 業界 |
| **2026-05-18** | [アリババ Qwen 3.7-Max-Preview / Plus-Preview](https://www.scmp.com/tech/tech-trends/article/3354087/alibaba-teases-new-qwen-previews-highest-ranking-chinese-ai-models-arena) — LM Arena で中国モデル最高スコア（テキスト + ビジョン）| モデル |
| **2026-05-18** | [Boston Dynamics Atlas 100ポンド超の荷重操作](https://www.techtimes.com/articles/316854/20260519/boston-dynamics-reveals-how-atlas-learned-lift-100-pound-loads-hyundai-plans-30000-per-year.htm) + Hyundai が 2028 年以降 Hyundai/Kia 工場に **25K+ 台の Atlas** を配備予定 | ロボティクス |
| **2026-05-18** | [Figure F.03 対 人間 8 時間仕分けチャレンジ](https://incrypted.com/en/figure-ai-held-a-human-vs-robot-marathon/) — 人間社員が 12,924 個、F.03 が 12,732 個でわずかに人間勝（2.79 vs 2.83 秒 / 個）| ロボティクス |
| **2026-05-18** | [Anthropic が FSB に Claude Mythos ブリーフィング](https://www.theguardian.com/technology/2026/may/18/anthropic-ai-claude-mythos-cyber-financial-stability-board-fsb) — フロンティア lab 初の G20 金融安定規制当局への説明 | 業界 |
| **2026-05-18** | [ChatGPT 安全システムアップデート](https://www.edtechinnovationhub.com/news/openai-updates-chatgpt-safety-systems-to-track-risk-across-sensitive-conversations) — 長いセッションを跨いでリスクシグナル（自殺 / 自傷 / 他者への危害）を追跡 | 業界 |
| **2026-05-19** | [Claude Managed Agents update](https://claude.com/blog/new-in-claude-managed-agents) — Anthropic が研究プレビューの dreaming、outcomes、マルチエージェント連携、webhook を文書化。 | 履歴 |
| **2026-05-19** | **Google I/O 2026** — [Gemini 3.5 Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) を Gemini App + Google 検索 AI Mode のデフォルトモデルとして公開（公式によると同類のフロンティアモデルより約 4 倍高速）。Gemini 3.5 Pro は 6 月入り | モデル |
| **2026-05-19** | **Google I/O 2026** — [Gemini Omni / Omni Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/)、Google DeepMind の AGI を見揮えたワールドモデルファミリー | モデル |
| **2026-05-19** | **Google I/O 2026** — [Gemini Spark](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) 24/7 パーソナル AI エージェント + ~30+ の MCP サードパーティーツール連携、新たな **Google AI Ultra ($100/月)** サブスクリプション限定 | ツール |
| **2026-05-19** | [OpenAI Guaranteed Capacity （Compute Annual Pass）](https://openai.com/news/company-announcements/) リリース — 1 / 2 / 3 年期の企業コンピュート予約 | 業界 |
| **2026-05-19** | [OpenAI ↔ Google SynthID + C2PA コンテンツ出所検証](https://openai.com/index/advancing-content-provenance/) — フロンティア lab 同士初のクロスプラットフォーム AI 画像ウォーターマーク相互運用と公開検証ツールプレビュー | 業界 |
| **2026-05-19** | [Anthropic：Widening the conversation on frontier AI](https://www.anthropic.com/news/widening-conversation-ai) — 「智恵の伝統」を取り込んだフロンティア AI 安全対話の枠組み | 業界 |
| **2026-05-19** | [DeepSeek が Jane Street 出身のエンジニアを迎え AI harness チームを新設](https://www.scmp.com/tech/big-tech/article/3354113/deepseek-recruits-former-jane-street-engineer-catch-ai-agents-revenue-race) — モデル R&D からエージェント製品化への軸足 | 業界 |
| **2026-05-19** | [Google Antigravity 2.0](https://antigravity.google/blog/introducing-google-antigravity-2-0) を I/O 2026 で発表 — スタンドアロンデスクトップアプリで多エージェントオーケストレーション、cron スケジュール / 長時間非同期 / 動的サブエージェント、Antigravity CLI + SDK、エンタープライズ版は Gemini Enterprise Agent Platform に組み込み | ツール |
| **2026-05** | Macquarie Bank が 7 か月で Gemini Enterprise を使って 13 万時間を節約したと報告 | 業界 |
| **2026-05** | Google が対応車両に Gemini をロールアウトし、Google Assistant を置き換える（英語ファースト、米国から） | 業界 |
| **2026-05-20** | **アリババクラウド杭州サミット** — [Qwen 3.7-Max](https://www.scmp.com/tech/big-tech/article/3354212/alibaba-unveils-new-qwen-model-custom-chips-bid-become-chinas-ai-factory) GA、エージェント型コーディングと長期タスク向け；同期で T-Head **Zhenwu M890** AI チップとフルスタック AI 基盤アップグレード | モデル |
| **2026-05-20** | [BMS ↔ Anthropic Claude Enterprise](https://news.bms.com/news/corporate-financial/2026/Bristol-Myers-Squibb-Announces-Strategic-Agreement-with-Anthropic-to-Position-Claude-Enterprise-as-the-Shared-Intelligence-Platform-Across-Its-Global-Operations/default.aspx) — 30K+ 名の社員が Claude Enterprise を共通インテリジェンス基盤として採用、世界トップ 5 製薬企業で初めての社全体規模 | 業界 |
| **2026-05-20** | [LlamaIndex ↔ Google Agents API](https://www.kucoin.com/news/flash/google-launches-agents-api-llama-index-integrates-llamaparse-for-unstructured-document-processing) — Google Agents API サンドボックス内に LlamaParse / LiteParse を法出し、Sandboxed-Lit + ParseBench も同リリース | フレームワーク |
| **2026-05-20** | [Microsoft RAMPART + Clarity](https://www.microsoft.com/en-us/security/blog/2026/05/20/introducing-rampart-and-clarity-open-source-tools-to-bring-safety-into-agent-development-workflow/) オープンソース化 — agentic AI 向け pytest ネイティブのホワイトボックステストフレームワークと、設計レビューコンパニオン。CI/CD にそのまま組み込める PyRIT の開発者向け後継 | ツール |
| **2026-05-21** | [MCP 2026-07 Release Candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) 公開 — ステートレスコア、拡張フレームワーク、MCP Apps サーバレンダリング UI、OAuth/OIDC 強化。[正式版は予定通り 7 月 28 日にリリース](https://blog.modelcontextprotocol.io/posts/2026-07-28/) | プロトコル |
| **2026-05-22** | [Kore.ai Artemis Agent Platform](https://venturebeat.com/technology/kore-ai-launches-artemis-ai-agent-platform-expands-challenge-to-microsoft-and-salesforce) を Azure で公開 — AI ネイティブのエンタープライズエージェント基盤。核は宣言型の **Agent Blueprint Language (ABL)** | 業界 |
| **2026-05-22** | [FPT Flezi Foundry™](https://fptsoftware.com/newsroom/news-and-press-releases/press-release/fpt-launches-flezi-foundry-advancing-ai-augmented-delivery-for-global-enterprises) ローンチ — “Service-as-a-Software” ガバナンス下の AI 強化デリバリー基盤。ADLC と AMS の 2 モードを提供 | 業界 |
| **2026-05-22** | [JetBrains Rider AI テスト生成 skill](https://blog.jetbrains.com/dotnet/2026/05/22/claude-codex-ai-agent-skill-for-writing-tests/) — .NET カバレッジ情報を Claude Code / Codex に渡し、未カバー分岐に絞り込んだテスト生成を可能に | ツール |
| **2026-05-26** | [Coinbase Base MCP](https://fortune.com/2026/05/26/coinbase-pushes-further-into-ai-payments-with-new-mcp-for-base-network/) 公開 — オンチェーン取引・レンディング向け初の取引所級 MCP エンドポイント | プロトコル |
| **2026-05-27** | [Robinhood Agentic Trading](https://robinhood.com/us/en/newsroom/robinhood-is-now-open-to-agents/) ベータ — 米国主要証券会社初の MCP 経由 AI エージェント株取引開放 | 業界 |
| **2026-05-28** | [Claude Opus 4.8](https://www.anthropic.com/claude/opus) Anthropic がリリース — コードベース規模のマイグレーション、動的ワークフロープレビュー（数百のサブエージェント並列）、エフォートコントロールパネル、Fast モード 3 倍安、**Mythos クラス** を予告 | モデル |
| **2026-05-28** | [Koog 1.0](https://blog.jetbrains.com/ai/2026/05/koog-1-0-is-out-stable-core-better-interop-and-multiplatform-observability/) KotlinConf 2026 でリリース — JetBrains の OSS Kotlin/Java エージェントフレームワークが安定 1.0、Kotlin Multiplatform デプロイ、全ターゲット OpenTelemetry | フレームワーク |
| **2026-05-28** | [Gemini Omni Flash 会話型ビデオ編集](https://www.techtimes.com/articles/317309/20260528/google-gemini-omni-flash-brings-voice-controlled-ai-video-editing-future-conversational-ai.htm) が Gemini App / Google Flow / YouTube Shorts へロールアウト — 音声・テキスト騆動のシネマ風編集が従来の NLE を置換 | ツール |
| **2026-05-29** | [OpenAI Codex Computer Use on Windows](https://windowsforum.com/threads/openai-codex-computer-use-brings-agent-control-to-windows-desktop.421107/) — サンドボックス化された Codex の Windows デスクトップ制御が GA | ツール |
| **2026-06-02** | [Microsoft Build 2026](https://microsoft.ai/news/microsoft-build-2026-mai-keynote-transcript/) — MAI-Thinking-1（自社初の推論モデル）、MAI-Code-1-Flash（5B コーディングモデル、GitHub Copilot 入り）、[Microsoft Scout](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/)（OpenClaw ベースの常時稼働パーソナルエージェント）を同日発表 | モデル / ツール |
| **2026-06-03** | [Meta Business Agent](https://techcrunch.com/2026/06/03/metas-ai-agent-for-whatsapp-business-is-now-available-globally/) が WhatsApp + Instagram で世界展開 — Meta 初の直接収益化 AI 製品、WhatsApp Business Premium ティアと連動 | 業界 |
| **2026-06-03** | [Perplexity Personal Computer for Windows](https://www.perplexity.ai/hub/products/computer-for-windows) 発表 — 19+ AI モデルを自動オーケストレーション、ローカルファイル / ネイティブアプリ / Web を横断 | ツール |
| **2026-06-06** | [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code) を Moonshot AI がリリース — TypeScript / MIT のターミナルエージェント、隔離コンテキストで動く coder / explore / plan サブエージェント内蔵 | ツール |
| **2026-06-07** | [PerspectiveGap](https://arxiv.org/abs/2606.08878) — マルチエージェントのオーケストレーションプロンプト評価を arXiv に初投稿。v2 は 7 月 12 日。 | Benchmarks |
| **2026-06-08** | **[WWDC 2026](https://www.techradar.com/news/live/apple-wwdc-2026-live)** — Apple が Google Gemini 駆動の Apple Intelligence と、よりパーソナル化された新 Siri を発表（Siri からサードパーティ ChatGPT へ転送する動作は廃止）。iOS 27、iPadOS 27、macOS 27 "Golden Gate"、watchOS 27、tvOS 27、visionOS 27 でオンデバイス AI を強化。アプリ起動 約 30% 高速化、写真プレビュー 70% 高速化、iPadOS のファイル転送 5 倍高速化、2026 年秋にリリース | 業界 |
| **2026-06-08** | **WWDC 2026 Apple Intelligence + Siri AI 再設計** — Foundation Models フレームワークに画像入力、カスタムスキル、オンデバイス + サーバ統一 Swift API が追加；SiriKit 廃止、拡張 App Intents に統一；新 Siri は Google Gemini ベース（ChatGPT ではない）| モデル / ツール |
| **2026-06-09** | [Claude Fable 5 + Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) リリース — Anthropic 初の一般提供 **Mythos クラス**モデル（Fable 5 は一般公開、Mythos 5 は Project Glasswing 経由の限定提供）| モデル |
| **2026-06-12** | [米国の輸出管理指令により Anthropic が全顧客向けに Fable 5 + Mythos 5 を停止](https://www.anthropic.com/news/fable-mythos-access) — 一般提供されたフロンティアモデルが政府により強制停止された初の事例 | 業界 |
| **2026-06-12** | [Kimi K2.7 Code](https://kimi.ai/) を Moonshot AI がリリース — 1T MoE のコーディング優先モデル（256K、Modified MIT）、推論トークン消費を約 30% 削減 | モデル |
| **2026-06-13** | [GLM-5.2](https://z.ai/blog/glm-5.2) を Zhipu AI がリリース — コーディング優先の 744B MoE、100万トークンコンテキスト、全 GLM Coding Plan ティアで提供 | モデル |
| **2026-06-14** | [OpenAI Partner Network](https://openai.com/index/introducing-openai-partner-network/) — OpenAI が 1.5 億ドルのパートナープログラムを発表。Select・Advanced・Elite の区分を設け、年末までに 30 万人の研修を目標とする。 | 履歴 |
| **2026-06** | [OutSystems Agentic Systems Platform](https://www.outsystems.com/) ローンチ — ローコードプラットフォームが「AI ネイティブ」なマルチエージェントオーケストレーション基盤へとピボット | 業界 |
| **2026-06-22** | [Daybreak](https://openai.com/index/daybreak-securing-the-world/) — OpenAI が Daybreak を更新し、防御目的の脆弱性検証、修正のテスト、パートナーとの処理手順を説明。 | 履歴 |
| **2026-06-25–26** | [GPT-5.6 preview](https://openai.com/blog/gpt-5-6) — Sol・Terra・Luna 系列が限定プレビューに入り、7 月の提供拡大に先行。 | 履歴 |
| **2026-06-26** | [GPT-4.5 ChatGPT retirement](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) — GPT-4.5 が ChatGPT から退役。2025 年 7 月 14 日の gpt-4.5-preview API 終了とは別の事項（[API 履歴](https://developers.openai.com/api/docs/deprecations)）。 | 履歴 |
| **2026-06-29** | [Accenture + ServiceNow](https://newsroom.accenture.com/news/2026/servicenow-and-accenture-launch-ai-powered-services-to-accelerate-the-shift-from-legacy-risk-platforms-to-agentic-ai) — 両社がマネージドセキュリティサービスと旧リスク基盤からの AI 支援移行を発表。 | 履歴 |
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
| **2026-07-10** | [Cursor 3.11](https://cursor.com/changelog) — Side Chats、会話履歴検索、Cloud Agent Hooks の更新。 | Tools |
| **2026-07-14** | [Oracle が AI ネイティブな Agentic Applications Builder を追加](https://www.oracle.com/news/announcement/oracle-introduces-ai-native-builder-experience-2026-07-14/) — Fusion 向け AI Agent Studio を拡張し、Fusion エージェントアプリをプロコード開発者にも開放；Fusion 顧客は追加費用なし | フレームワーク |
| **2026-07-15** | [Inkling](https://thinkingmachines.ai/inkling/) を Thinking Machines Lab（Mira Murati、前 OpenAI CTO）がローンチ — 975B MoE / 41B アクティブ、45T トークン事前学習、1M コンテキスト、Apache 2.0 オープンウェイトを Hugging Face で公開；ネイティブマルチモーダル（テキスト/画像/音声/動画）；Inkling-Small（12B アクティブ）も同時リリース | モデル |
| **2026-07-16** | [Kimi K3](https://kimi.ai/) を Moonshot AI がローンチ — 2.8T パラメータの疎 MoE（896 エキスパート中 16 が有効）、1M トークンコンテキスト、100 万トークンあたり $3/$15；フルオープンウェイトは 7 月下旬公開予定 | モデル |
| **2026-07-17** | EU Android AI 開放命令 — 欧州委員会がサードパーティ AI アシスタントへのより深い Android アクセスを Google に命令（カメラ・マイク・アプリ制御 API）；Android 18 での実装期限は 2027 年 8 月 | 業界 |
| **2026-07-19** | [Qwen 3.8-Max](https://qwenlm.github.io/) をアリババが世界 AI カンファレンスでプレビュー — 2.4T パラメータ MoE プレビュー；コーディング・数学・マルチモーダル能力が強力 | モデル |
| **2026-07-20** | [Qwen-Image-3.0](https://qwenlm.github.io/) をアリババがリリース — 世界 AI カンファレンスで発表された第 3 世代画像生成モデル；フォトリアリズム・テキストレンダリング・マルチ被写体一貫性が向上 | モデル |
| **2026-07-22** | Grok 4.5 が grok.com / X の全ユーザーへロールアウト；[Microsoft Agent Framework v1.12.1](https://learn.microsoft.com/en-us/agent-framework/) リリース；[OpenAI Presence](https://openai.com/) エンタープライズエージェントプラットフォーム開始 | ツール |
| **2026-07-22** | [AMD ↔ Anthropic](https://ir.amd.com/news-events/press-releases/detail/1292/amd-and-anthropic-announce-strategic-partnership-to-deploy-up-to-2-gigawatts-of-amd-instinct-mi450-series-gpus) — Anthropic が AMD Helios ラックに AMD Instinct MI450（MI455X）を最大 2 GW 展開、2027 年前半に開始；AMD は Anthropic へ最大 50 億ドルの戦略的出資を約束 | 業界 |
| **2026-07-23** | [GPT Voice](https://openai.com/) を OpenAI がローンチ — ChatGPT Work 向けの音声インターフェース、GPT-Live 技術で動作 | ツール |
| **2026-07-23** | [FLUX 3](https://bfl.ai/blog/flux-3) が早期アクセス開始 — Black Forest Labs 初の統合マルチモーダルモデル（画像 + 動画 + 音声 + 行動予測を単一アーキテクチャで）、20 秒動画にネイティブ同期音声 | モデル |
| **2026-07-24** | [Claude Opus 5](https://www.anthropic.com/news/claude-opus-5) を Anthropic がリリース — 第 5 世代フラッグシップ、Fable 5 に迫る性能を 100 万トークンあたり $5/$25 で提供；1M コンテキスト、128K 出力；Claude Max のデフォルトモデル；API: `claude-opus-5` | モデル |
| **2026-07-27** | [Kimi K3 オープンウェイト公開](https://huggingface.co/moonshotai/Kimi-K3)（Moonshot AI）— 2.8T 総 / 104B アクティブで、公開時点最大のオープン言語モデルとなった；独自の Kimi K3 License | モデル |
| **2026-07-27** | [オープンウェイトに関する Anthropic の立場](https://www.anthropic.com/news/position-open-weights-models) — Dario Amodei が中国製オープンウェイトモデルの禁止案を否定し、チップ輸出管理・蒸留への抑止・高性能モデル全般へのリリース前安全性テスト義務化を支持 | 業界 |
| **2026-07-28** | [MCP 2026-07-28 仕様が正式リリース](https://blog.modelcontextprotocol.io/posts/2026-07-28/) — ステートレスなプロトコルコア（ハンドシェイクとセッションを廃止）、Multi Round-Trip Requests、ヘッダベースのルーティング、キャッシュ可能な list 結果、RFC 9207 + CIMD による認可強化、正式な拡張フレームワーク、12 か月の非推奨ポリシー；TypeScript/Python/Go/C# SDK は同日対応 | プロトコル |
| **2026-07-29** | [Langfuse v4](https://github.com/langfuse/langfuse/releases/tag/v4.0.0) と [Milvus 3.0](https://github.com/milvus-io/milvus/releases/tag/v3.0.0) が同日リリース — 前者は全文検索とモニター、API は最大 165 倍高速と主張；後者はレイクネイティブな External Collections で Parquet/Lance/Iceberg を直接クエリ。同日 [RufRoot / CVE-2026-59726](https://hackread.com/rufroot-vulnerability-attackers-hijack-ruflo-login/) も公表：Ruflo の MCP ブリッジが認証なしで 233 ツールに到達可能、エージェントメモリも汚染可能 | ツール / 業界 |
| **2026-07-30** | [Inkling-Small](https://thinkingmachines.ai/inkling/) ウェイト公開 — 276B/12B アクティブ、Apache-2.0、マルチモーダル；HLE テキスト 31.6%（975B Inkling の 29.7% を上回る） | モデル |
| **2026-07-31** | [DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731) —— 同一 API・料金のまま Agentic 能力を強化、V4-Pro Preview を上回る；HF にオープンウェイト公開。GitHub Copilot が Gemini 2.5 Pro・Gemini 3 Flash を非推奨化 | モデル / ツール |
| **2026-08-03〜07** | [Cloudflare Agents Week](https://blog.cloudflare.com/agents-week-review-august-2026/) — Wallets/cloudflare.pay（8-4）、WriteGuard プライベートベータ（8-5）、WebMCP + Kitesurf サーバーレスエージェントブラウザ + MCPv2 + AI Search（8-6） | ツール / プロトコル |
| **2026-08-03** | [Qwen3.8-Max](https://alibabacloud.com/blog/qwen3-8-max) をアリババが正式ローンチ — 2.4T MoE / 95B アクティブ、1M コンテキスト、マルチモーダル入力；QwenWork エンタープライズプラットフォームが公開ベータ | モデル |
| **2026-08-05** | Meta Superintelligence Labs の [Muse Spark 1.2 + Muse Code ベータ](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2) — ターミナルコーディングエージェント + リポジトリ全体で学習したモデル。[ByteDance SeedRealtime](https://technode.com/2026/08/05/bytedance-launches-seedrealtime-full-duplex-audio-video-model/) フルデュプレックス音声視覚モデルがローンチ。英国 AISI が[エージェント封じ込めインシデント](https://www.helpnetsecurity.com/2026/08/05/ai-agent-deception-in-cyber-tests/) INC-2026-07-28-01 を開示 | モデル / 業界 |
| **2026-08-06** | [Wan 3.0 公開ベータ](https://www.alibabacloud.com/en/blog/wan-3-0-next-gen-video-generation-model-public-beta-launched) — ドキュメント / Web ページを入力に取れるアリババの 30 秒動画モデル。[Bedrock AgentCore Runtime Instances GA](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-bedrock-agentcore-runtime-instances-generally-available/) — EC2 ベースのコンピュートで 14 日間のエージェントセッション | モデル / ツール |
| **2026-08-07** | [Grok Imagine Image 2.0](https://x.ai/news/grok-imagine-image-2) — ローンチ時点で text-to-image と画像編集の Arena 世界 2 位。[OpenAI が Astra の開発を減速](https://techcrunch.com/2026/08/07/openai-says-it-slowed-astra-model-development-over-security-concerns/) — 「Critical」サイバー能力の可能性を受けて；ホワイトハウスに報告済み | モデル / 業界 |
| **2026-08-10** | [Claude Sonnet 5 の $2/$10 価格が恒久化](https://www.anthropic.com/news/claude-sonnet-5)；[GPT-5.6-Cyber](https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows) が Daybreak Red 経由で出荷；[Muse Glimmer 30B](https://huggingface.co/meta-models/Muse-Glimmer-30B) オープンウェイト（Apache 2.0） | モデル / 業界 |
| **2026-08-11** | 北京の NDRC 命令で Meta が 20 億ドルの買収を解消する中、[Manus が独立企業として運営再開](https://www.cnbc.com/2026/08/11/manus-china-meta-acquisition.html)。[Daybreak モデルが AWS Bedrock に登場](https://openai.com/index/daybreak-models-are-now-available-on-aws/)。[Grok Bot 早期ベータ](https://docs.x.ai/docs/release-notes) — 永続クラウドコンピュータ上の常時稼働 AI チームメイト。[ChatGPT 広告テストが国際展開](https://openai.com/index/testing-ads-in-chatgpt/)（英国・メキシコ・ブラジル・日本・韓国）。[Nemotron 3.5 Lightning](https://ollama.com/library/nemotron-3.5-lightning) リリース | 業界 / モデル |
| **2026-08-12** | [Grok 4.6](https://x.ai/news/grok-4-6) リリース — 長時間稼働エージェント向け SpaceXAI フラッグシップ、Artificial Analysis Intelligence Index（61）で GPT-5.6 Sol と同点、$2/$6、Cursor の新デフォルト。[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) オープンウェイトの動画音声ワールドモデルが出荷。Qwen3.8-Max のオープンウェイトが Hugging Face に登場（`Qwen/Qwen3.8-2.4T-A95B`） | モデル |
| **2026-08-13** | [Gemini 3.7 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) — Google の新ワークホースモデル（導入価格 $0.75/$3.75）、3.5 Pro が未リリースのまま Gemini 4 のトレーニング中に出荷。[DeepSeek-V4-Pro GA](https://api-docs.deepseek.com/news/news260813) — Responses API + 推論エフォート対応；8-16 からピーク / オフピーク料金。[OpenAI Ultrafast プレビュー](https://openai.com/index/previewing-ultrafast) — Cerebras 上で GPT-5.6 Sol を最大 14 倍速。[Suno Studio 2.0](https://suno.com/release-notes) ブラウザ DAW | モデル / ツール |
| **2026-08-14** | [GLM-5.3](https://the-decoder.com/zhipu-ai-releases-glm-5-3-claims-its-the-strongest-open-weights-coding-model/) — Zhipu が最強のオープンウェイトコーディングモデルと主張（GLM-5.2 比 +50%）。[Anthropic が Claude テキスト電子透かしを出荷](https://www.anthropic.com/news/claude-text-watermark)（SynthID-Text + C2PA、EU AI 法対応）。[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) Apache-2.0 オープンウェイト。[Waymo がカリフォルニア州 18 郡で承認](https://electrek.co/2026/08/14/waymo-cpuc-approval-california-expansion-18-counties/)；[Pony.ai × Uber が欧州で 2,000 台超のロボタクシー計画](https://cnevpost.com/2026/08/14/pony-ai-uber-2000-robotaxis-europe/)。Grok 4.6 が GitHub Copilot に登場 | モデル / ロボティクス / 業界 |
| **2026-08-16** | [DeepSeek-V4-Pro GA](https://api-docs.deepseek.com/news/news260813) が発表していたピーク/オフピーク API 料金が 16:00 UTC に発効 | モデル |
| **2026-08-18** | [ChatGPT for Teens](https://openai.com/index/chatgpt-for-teens) がローンチ；[ChatGPT 広告が欧州 31 市場に拡大](https://openai.com/index/chatgpt-ads-expands-across-europe) | 業界 |
| **2026-08-19** | [Cursor cloud agents](https://cursor.com/changelog) — Cursor がクラウドエージェント契約とサブエージェントを文書化。[OpenAI Agents SDK v0.22.0](https://github.com/openai/openai-agents-python/releases/tag/v0.22.0)は別のリリースノートに記録。 | 履歴 |
| **2026-08-21** | [DeepSeek-V4-Flash-Vision-Exp](https://api-docs.deepseek.com/news/news260821) マルチモーダル API + Files API；DeepSeek Harness **dsh-v0.1.1-rc.2**；[goose v1.47.0](https://github.com/aaif-goose/goose/releases/tag/v1.47.0)；[OpenHands v1.15.0](https://github.com/OpenHands/OpenHands/releases/tag/v1.15.0)；[MAF python-1.15.0](https://github.com/microsoft/agent-framework/releases) | モデル / ツール |
| **2026-08-22** | [新しい MCP ロードマップ](https://blog.modelcontextprotocol.io/posts/mcp-roadmap/) — `2026-07-28` 以降の優先事項（エージェントメッセージ、HTTP ネイティブ輸送、エージェント身元）；MAF **dotnet-1.19.0** | プロトコル / フレームワーク |
| **2026-08-24** | [Agno v3.0.0](https://github.com/agno-agi/agno/releases/tag/v3.0.0) 破壊的リリース（ツール/メディアオフロード、CodeMode）；[Embabel Agent v1.5.1](https://github.com/embabel/embabel-agent/releases/tag/v1.5.1)；[Pydantic AI v2.34.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.34.0)；Codex CLI **v0.149.1** | フレームワーク / ツール |
| **2026-08-25** | [OpenAI Jalapeño](https://openai.com/index/jalapeno-first-results) 自社推論チップの初結果；Claude Code **v2.1.245** on npm | モデル / ツール |
| **2026-08-26** | [Google ADK v2.8.0](https://github.com/google/adk-python/releases/tag/v2.8.0) — Python SDK を公開。旧保守ブランチの版は別管理。 | 公開 / 更新 |
| **2026-08-27** | [Terminal-Bench-Science 0.1](https://www.tbench.ai/news/terminal-bench-science-0-1) — 科学分野の端末ワークフローを評価する 70 タスク。 | 公開 / 更新 |
| **2026-08-28** | [Terminal-Bench 4.0](https://www.tbench.ai/news/terminal-bench-4-0) — タスクと資源条件を更新。旧版の得点と直接比較できない。 | 公開 / 更新 |
| **2026-09-01** | [Claude Fable 5.1 / Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1) — Fable は一般提供、Mythos は信頼済みアクセス制度に限定。 | 公開 / 更新 |
| **2026-09-01** | [Muse Voice Transcribe](https://research.meta.ai/blog/introducing-muse-voice-transcribe) — Meta が話者分離と発話終端検出を備えるストリーミング音声認識を発表。 | 公開 / 更新 |
| **2026-09-01** | [Waymo](https://waymo.com/blog/2026/09/ride-in-denver-san-diego-tampa/) — デンバー、サンディエゴ、タンパで初の一般利用者を招待。利用枠は段階的に拡大。 | 公開 / 更新 |
| **2026-09-02** | [Muse Spark 1.3](https://research.meta.ai/blog/introducing-muse-spark-1-3) — Meta Model API と Muse Code を更新。今後の重み公開は計画段階。 | 公開 / 更新 |
| **2026-09-02** | [Cursor workers](https://cursor.com/changelog) — ツール実行用のセルフホストワーカー。モデル処理には別途提供者の方針が適用。 | 公開 / 更新 |
| **2026-09-03** | [GPT-6 Astra](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) — OpenAI が組織限定の展開を記載。一般提供ではない。 | 公開 / 更新 |
| **2026-09-03** | [MAI-Transcribe-2](https://microsoft.ai/news/mai-transcribe-2-is-the-fastest-most-accurate-and-cheapest-speech-recognition-model-in-the-world/) — 話者分離、単語時刻、文字起こし形式を備える音声認識更新。 | 公開 / 更新 |
| **2026-09-03** | [MCP in LangChain](https://www.langchain.com/blog/mcp-in-langchain-stateless-protocol-elicitation-and-more) — ステートレスプロトコル対応と追加情報要求の公式統合更新。 | 公開 / 更新 |
| **2026-09-03** | [Figure / Nscale](https://www.figure.ai/news/figure-and-nscale-sign-strategic-partnership) — 計算基盤の初期展開を 2027 年後半に予定。納入済み容量ではない。 | 公開 / 更新 |
| **2026-09-04** | [Codex CLI v0.153.4](https://github.com/openai/codex/releases/tag/rust-v0.153.4) — 安定タグ版。後続の alpha ビルドは別のプレビュー。 | 公開 / 更新 |
| **2026-09-05** | [FastMCP v4.0.3](https://github.com/PrefectHQ/fastmcp/releases/tag/v4.0.3) — Prefect の MCP アプリケーションフレームワークの公開版。 | 公開 / 更新 |
| **2026-09-07** | [Hermes Agent v2026.9.7](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.9.7) — 公開リリース。ランタイム変更は当該版の説明を参照。 | 公開 / 更新 |
| **2026-09-08** | [OpenAI Agents SDK v0.22.1](https://github.com/openai/openai-agents-python/releases/tag/v0.22.1) — Python SDK の公開リリース。 | 公開 / 更新 |
| **2026-09-08** | [OpenClaw v2026.9.3](https://github.com/openclaw/openclaw/releases/tag/v2026.9.3) — タグに含まれる日付と公開日は異なる。 | 公開 / 更新 |
| **2026-05** | [LangGraph v1.2](https://docs.langchain.com/oss/python/releases/changelog) — LangGraph の公開履歴でランタイムとチェックポイントの改善を記録。 | 履歴 |
| **2026-05** | [Grok 4.3 on Microsoft Foundry](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-grok-4-3-on-microsoft-foundry-latest-generation-agentic-capabilities/4517096) — Microsoft が Foundry での Grok 4.3 提供を発表。 | 履歴 |
| **2026 進行中** | A2A Protocol のパートナー組織が 150+ に増加 | プロトコル |
| **2026 進行中** | 開発者の 85% が AI コーディングツールを常用 | 業界 |
| **2026 進行中** | エンタープライズエージェント AI の導入が加速 — "Agents as a Service" が台頭 | 業界 |
| **2026-06** | [ByteDance Seed 2.1 Pro / Turbo](https://seed.bytedance.com) — ByteDance が Seed 2.1 系列を公開。モデル別の提供形態は公式カタログを参照。 | 履歴 |
| **2026-06** | [Fable 5 / Mythos 5 access statement](https://www.anthropic.com/news/fable-mythos-access) — Anthropic がアクセス制限とその後の更新を記録。この過去の声明は現在の提供モデル一覧ではない。 | 履歴 |

---


## 貢献

[CONTRIBUTING.md](CONTRIBUTING.md) をご読みください。**スパム防止の品質ゲート**は中、英、日の 3 言語版すべてに適用されます: 自己宣伝タイプの並列提出 PR は一律拒否されます。

## License

MIT © [Zijian Ni](https://github.com/Zijian-Ni)

---

*Made with ❤️ by [Zijian Ni](https://github.com/Zijian-Ni) · 2026。日本語版は英語版と同期します。不一致がある場合は英語版を正とします。*
