# Intermezzo 1 独立検証（PR #26 / #16 / #25）

- 日時: 2026-09-17 00:38 JST
- 検証者: Grok Bot executor（box-scoped）。ThinkPad の `hermes -z` / `agy -p` には **未到達**
- ブランチ: `docs/intermezzo1-complete-ja` @ `5dfd946`
- JA: `04-intermezzo1.md`（59796 bytes / 41154 文字 / 1070 行）
- EN: `extracted/original_markdown_04_i1-2.md`（53229 bytes / 52961 文字 / 1341 行）
- 方法: 行ベースのフェンスパーサ + 見出し/練習問題/図/注/リストの機械照合 + 短い節の通読
- 方針: 省略禁止・コードフェンスは EN とバイト一致。意訳は個人学習用で許容

## Hermes / agy

| 項目 | 結果 |
|---|---|
| ThinkPad (`machineId` 2275484b-64af-4d20-83ab-f1a5c9b019ce / mevius-ThinkPad-X240) | **未到達**。この executor の Shell/Read は `machineId` をスキーマに持たず、パラメータは落ちて box で実行される |
| `hermes -z` | **未実行**（バイナリなし・stdout なし） |
| `agy -p` | **未実行**（任意・時間制約のためスキップ） |
| フォールバック | 下記の Python 機械照合（ステップ 4 どおり） |

## 総合判定

**PR 維持でよい（ハードゲート合格。本文の修正はしない）**

| 必須チェック | 判定 | 要約 |
|---|---|---|
| 省略（節・Exercise 116–128・図） | **合格** | `##`/`###` 12 見出しが 1 対 1。Ex 116–128 全あり。Figure 39–43、注 10、番号リスト 36、箇条書き 16、パイプ行 168 |
| コードフェンスが EN と一字一句一致 | **合格** | 76/76。言語タグ 50 `racket` + 26 空。本文+言語タグ不一致 0。連結 SHA256 一致 |
| プレースホルダ | **合格** | TODO/FIXME/未訳なし。「省略」は *omit/abbreviation* の正当な訳 |

SHA256（`` ```lang\n`` + body + `` ```\n `` を 76 本連結）:

`c695d6bcf824c2fdb6d97e878ee84a750a1b0ffeb679b59cb69f056bc7a1757f`（JA = EN）

主張: #25 の差し戻し条件（欠落・フェンス改変）は、この HEAD にはない。
根拠: フェンス完全一致と Ex/見出しの列挙。
論拠: 短い節（導入、Meaning and Computing）も EN 段落を圧縮した意訳で、落ちではない。

## 見出し対応

| EN | JA |
|---|---|
| Intermezzo 1: Beginning Student Language | Intermezzo 1: Beginning Student Language（初級学生言語） |
| Contents | 目次 (Contents) |
| BSL Vocabulary | BSL の語彙 (BSL Vocabulary) |
| BSL Grammar | BSL の文法 (BSL Grammar) |
| BSL Meaning | BSL の意味 (BSL Meaning) |
| Meaning and Computing | 意味とコンピューティング (Meaning and Computing) |
| BSL Errors | BSL のエラー (BSL Errors) |
| Boolean Expressions | ブール式 (Boolean Expressions) |
| Constant Definitions | 定数定義 (Constant Definitions) |
| Structure Type Definitions | 構造型定義 (Structure Type Definitions) |
| BSL Tests | BSL のテスト (BSL Tests) |
| BSL Error Messages | BSL のエラーメッセージ (BSL Error Messages) |

Error Messages の 5 分類（Function Applications / Wrong Data / Conditionals / Function Definitions / Structure Type Definitions）は JA に双语で残っている。

## Exercise 116–128

すべて `練習問題 N (Exercise N)` 形式で本文にある。フェンス外の Racket 式（例: Ex 121 の `cond`）は EN 同様にインラインコードのまま。

## 本文修正について

フェンス不一致・欠番・欠節は **見つからなかった** ため、`04-intermezzo1.md` は変更しない（指示: 実欠落またはフェンスずれのみ修正）。

## 残リスク

1. **ThinkPad 上の本物の `hermes -z` はまだ一度も成功していない。** 本レポートは box 上の機械照合である。再接続後にローカル Hermes で散文品質を見る余地はある。
2. Error Messages の ASCII 表はフェンス内のため英語のまま（要件どおり）。
3. 章名の英語併記（Refining Interpreters など）や「語用論」の gloss は任意の用語揃えで、差し戻し理由にならない。
4. Grammar の DrRacket Note 二重は EN 抽出側の重複を写したもの。

マージはしない（ユーザー承認・rebase-merge 想定）。#17 は開始しない。
