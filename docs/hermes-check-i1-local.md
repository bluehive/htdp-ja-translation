# Intermezzo 1 独立検証（PR #26 / #16 / #25）

- 日時: 2026-09-17 00:47 JST
- 検証者: Grok Bot executor（box-scoped）。**このセッションでは** ThinkPad の `hermes -z` / `agy -p` に **未到達**
- ブランチ: `docs/intermezzo1-complete-ja` @ `5bb5fa821bbe25c380898e947af7e5785b6a0d81`
- JA: `04-intermezzo1.md`（59796 bytes / 41154 文字 / 1069 行 / SHA256 `f35557f9…15ef18f`）
- EN: `extracted/original_markdown_04_i1-2.md`（53229 bytes / 52961 文字 / 1340 行 / SHA256 `bd1bfcd3…720ed4e`）
- 方法: 行ベースのフェンスパーサ + 見出し/練習問題/図/注/リストの機械照合
- 方針: 省略禁止・コードフェンスは EN とバイト一致。意訳は個人学習用で許容
- hermes stdout: `/tmp/hermes-i1-check-out.txt`（`hermes: command not found`、exit 127）
- 先行: `docs/hermes-check-i1-thinkpad.md`（別セッション、ホスト mevius-ThinkPad-X240 の Hermes **合格** @ 同 SHA）

## Hermes / agy

| 項目 | 結果 |
|---|---|
| ThinkPad (`machineId` 2275484b-64af-4d20-83ab-f1a5c9b019ce / mevius-ThinkPad-X240) | **この executor からは未到達**。Shell に `machineId` を付けても hostname `cursor` / user `box` で実行される |
| `command -v hermes` / `agy` | **MISSING**（`/home/mevius/.local/bin/*` も無し） |
| `hermes -z` | **未実行**（exit 127、`hermes: command not found`） |
| `agy -p` | **未実行**（hermes 失敗のため任意の第二意見はスキップ） |
| フォールバック | 下記の Python 機械照合（ステップ 4 どおり） |

## 総合判定

**PR 維持でよい（ハードゲート合格。本文の修正はしない）**

| 必須チェック | 判定 | 要約 |
|---|---|---|
| 省略（節・Exercise 116–128・図） | **合格** | `##` 11 + `###` 1 が見出し 1 対 1。Ex 116–128 全あり。Figure 39–43、注 10、番号リスト 36、箇条書き 16、パイプ行 172 |
| コードフェンスが EN と一字一句一致 | **合格** | 76/76。言語タグ 50 `racket` + 26 空。対ごとの本文・言語タグ不一致 0。連結 SHA256 一致 |
| プレースホルダ | **合格** | TODO/FIXME/未訳/XXX/仮訳/TBD なし。ハングル 0 |

SHA256（各ブロックを ` ```lang\n ` + body + ` ```\n ` で 76 本連結）:

`c695d6bcf824c2fdb6d97e878ee84a750a1b0ffeb679b59cb69f056bc7a1757f`（JA = EN）

主張: #25 の差し戻し条件（欠落・フェンス改変）は、この HEAD にはない。
根拠: フェンス完全一致と Ex/見出し/図/注/リストの列挙。ThinkPad Hermes レポートと同 SHA。
論拠: 節ごとのフェンス数も EN と同一（Vocabulary 1, Grammar 5, Meaning 11, Computing 0, Errors 11, Boolean 4, Constants 9, Structures 11, Tests 2, Error Messages 22）。

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

Error Messages の italic サブ見出し 5 も JA に双语である。

## Exercise 116–128

すべて `練習問題 N (Exercise N)` 形式で本文にある。欠番なし。

## 本文修正について

フェンス不一致・欠番・欠節は **見つからなかった** ため、`04-intermezzo1.md` は変更しない（指示: 実欠落またはフェンスずれのみ修正）。

## 残リスク

1. **この executor から ThinkPad 上の `hermes -z` はまだ呼べない。** ブランチ上の `docs/hermes-check-i1-thinkpad.md` は別セッションの ThinkPad Hermes 合格レポート。本ファイルは box 上の機械照合の再計測。
2. Error Messages の ASCII 表はフェンス内のため英語のまま（要件どおり）。
3. 章名の英語併記や「語用論」の gloss は任意の用語揃えで、差し戻し理由にならない。
4. Grammar の DrRacket Note 二重は EN 抽出側の重複を写したもの。

マージはしない（ユーザー承認・rebase-merge 想定）。#17 は開始しない。
