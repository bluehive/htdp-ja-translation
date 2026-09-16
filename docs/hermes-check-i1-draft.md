# Hermes 独立検証: Intermezzo 1 日本語草稿

- 検証者: Hermes（本セッション、ThinkPad ローカル。agy 未使用。既存 `docs/hermes-review-i1.md` / 旧 `hermes-check-i1-draft.md` は判定前に読まず、突き合わせ後に対照しただけ）
- 日時: 2026-09-17 00:37 JST
- HEAD: `5dfd946`（`docs/intermezzo1-complete-ja`、`origin` と ff 同期）
- JA: `04-intermezzo1.md`（1069 行 / 59796 bytes）
- EN: `extracted/original_markdown_04_i1-2.md`（1340 行 / 53229 bytes）
- 方法: フェンス抽出の完全一致（言語タグ＋本文）、SHA256、見出し / Exercise 116–128 / リスト / Figure / Note の機械抽出、両ファイル全文通読

## 判定

**合格**

必須ゲート（省略なし・フェンス一字一句・見出しと練習番号）は通過。差し戻し理由なし。残件は統合を止めない低重大度のみ。

## 問題リスト

重大度: 重大（差し戻し） / 中（マージ前に直す） / 低（任意）

| ID | 重大度 | 場所 | 問題 | 修正提案 |
|----|--------|------|------|----------|
| P1 | 低 | JA 512–516 / EN 702–713（Exercise 123） | EN はフェンス後に独立文 `as a cond expression.` がある。JA は指示をフェンス前に「次を `cond` 式に書き換えられることを示す規則を書きなさい」へ吸収しており、**意味は落ちていない**が、Boolean 節の非フェンス段落数が EN 14 / JA 13。 | 任意: フェンス後に「を `cond` 式として。」を残し、指示文は「次を書き換えられる規則を書け」に戻す。必須ではない。 |
| P2 | 低 | JA 105–109 / EN 164–172 | DrRacket の定義領域／対話領域 Note がリスト内と直後で二重。JA の新作ではなく **EN 抽出の重複を忠実に保持**。 | 原本 HTML で重複か確認してから片方を落とす。本検証の範囲外。 |
| P3 | 低 | フェンス外の練習式（Ex 116–120, 125–127 など） | EN markdown は HTML 抽出で空白が潰れている（`( =yz)`、`(define(fx)x)`）。JA は空白復元＋バッククォート。**フェンス要件の対象外**。学習用としては原本に近い。 | 変更しない（推奨）。フェンスに触れない。 |
| P4 | 低 | JA 491 | EN “we don’t wish to divide by 0 accidentally” を「たまたま 0 で割りたくない」。意図は「誤って 0 除算しない」。 | 任意: 「誤って 0 で割らないため」。意訳として許容。 |
| P5 | 低 | JA 484 | `語用論` に英語併記 `(pragmatics)` がない。他用語（構文 / 意味論）は併記あり。 | 任意: `語用論 (pragmatics)`。 |
| P6 | 情報 | Error Messages 表（フェンス 55–76 付近） | 右列説明は英語のまま。**フェンス一致規則のため翻訳禁止**。EN 抽出時点で既に省略記号付き。 | 触らない。 |

重大・中: **0 件**。

## 必須ルール照合

### 1. 省略（段落・リスト・Exercise 116–128）

主張: 必須内容の欠落はない。

根拠:

- Exercise 116–128: 13 題とも JA 本文に存在（番号欠番なし）。項目数は EN と一致（116–118:3、119:2、120:3、121:3、122:3、123: `if` フェンス、124: プログラム3本、125:3、126:5、127:5、128: 失敗テストフェンス）。
- `##` 見出し EN 11 / JA 11、1対1。
- リスト行 52 / 52。番号付き項目 36 / 36。`-` 項目 16 / 16。
- Figure 39–43: 双方フェンス内に同一キャプション。
- blockquote `**Note:**` 相当: EN 10 + Grammatical Terminology 1。JA `**注` 10 + 文法用語注 1。
- 通読: 導入3段落、Vocabulary 図後、Grammar キーワード／合法例／非合法例、Meaning の beta / condfalse / condtrue、Computing ステッパー3段落、Errors の stuck / 最左最外指針 / `error`、Boolean の and/or 短絡と同値、Constants の定義順エラー、Structures の constructor/selector/predicate、Tests の RUN 移動、Error Messages 導入と5区分 — いずれも対応段落あり。

論拠: 省略判定は「EN の情報単位が JA に残っているか」であり、意訳による文結合（P1）は欠落としない。JA 先頭 HTML コメントと末尾免責は追加であり省略ではない。

### 2. コードフェンス（一字一句）

主張: 76 本すべて、言語タグ＋本文が EN とバイト一致。

根拠:

- 抽出: 正規表現 `` ```([^\n]*)\n(.*?)``` ``（DOTALL）。JA 76 / EN 76。
- 各フェンスを順に比較し、差分 0。
- 連結 SHA256（各フェンスを `lang + "\n" + body` として連結）:
  `8cd49e9abd41f2f02da91764125106cd3d9c1f6d22ad408313da1b0766b695a4`
  （JA = EN）。

論拠: 必須ルール2の対象はフェンス内のみ。インライン式の空白復元（P3）は対象外。

### 3. 見出し・練習問題番号

主張: 原本の英語見出し核と Exercise 番号は保持されている。

根拠（対応）:

- `## Intermezzo 1: Beginning Student Language` → 同文＋`（初級学生言語）`
- `## BSL Vocabulary` → `## BSL の語彙 (BSL Vocabulary)`（Grammar / Meaning / Errors / Tests / Error Messages も同型）
- `## Meaning and Computing` → `## 意味とコンピューティング (Meaning and Computing)`
- `## Boolean Expressions` → `## ブール式 (Boolean Expressions)`
- `## Constant Definitions` / `## Structure Type Definitions` も英語核を括弧で残す
- `### Contents` → `### 目次 (Contents)`
- Error Messages の5サブ見出しも日本語＋英語括弧
- 練習は `**練習問題 NNN (Exercise NNN).**` で 116–128

論拠: 個人学習用意訳として英語核の併記は可。番号の欠番・繰り上げなし。

### 4. 公式訳ではない

JA 先頭コメントと末尾免責がそれを明示。読みやすさのための空白復元・用語併記はルール4の範囲。

## プレースホルダ / 既知の用語直し

- `TODO` / `FIXME` / `TBD` / `XXX` / `未訳`: なし
- 旧指摘 `やり取り領域` / `検査付き版` / 「定義上誤り」: 現行 JA になし
- `対話領域` 3、`ステッパー` 12、`チェック付きバージョン` 1

残っている英語は次のみ（未訳段落ではない）:

- 見出し・練習番号の英語併記
- 書籍内参照: `Computing with lambda`、`Refining Interpreters`、`Nameless Functions`、`Input Errors`（日本語併記あり）
- DrRacket 引用 `"this function is not defined"` とフェンス内 UI
- 文法 blockquote（`definition = ... | (define name expr)` など）

## 判定（再掲）

**合格** — フェンス 76/76 一致、Exercise 116–128 欠落なし、`##` 11 対応、必須内容の省略なし。P1–P5 は任意。
