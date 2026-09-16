# Hermes 独立検証（CLI）: Intermezzo 1 日本語草稿

- 検証者: Hermes（grok-4.6 / xai-oauth）。agy 未使用。agy の提案は読んでいない。
- 日時: 2026-09-17 00:27 JST
- ブランチ: `docs/intermezzo1-complete-ja` @ `53f5786`
- JA: `04-intermezzo1.md`（1069 行 / 59796 bytes / 41154 文字）
- EN: `extracted/original_markdown_04_i1-2.md`（1340 行 / 53229 bytes。ファイル名は i1-2 だが `## Intermezzo` は I1 のみ）
- 参考にした既存メモ: `docs/hermes-check-i1-*.md` の**見出し形式だけ**。数値・判定は本セッションで再計測。
- 方法: フェンス抽出の対比較と SHA256、見出し / Exercise / Figure / Note / リストの機械抽出、JA・EN の通読。

合格

## 判定（Claim / Evidence / Warrant）

主張: PR #26 の Intermezzo 1 草稿は、必須3項（省略なし・フェンス一致・明らかな誤訳/英語取り残し/プレースホルダなし）を満たす。差し戻し理由はない。マージを止める要修正もない。

根拠: 下記の機械照合と通読。

論拠: 完了条件のハードゲートは「落ち」と「コード改変」である。現行草稿にはどちらもない。残るのは語感の任意修正であり、再下訳や差し戻しの対象ではない。

## 必須チェック

| 項目 | 判定 | 要約 |
|------|------|------|
| 1. 省略（段落・リスト・練習問題 116–128・コード例） | 合格 | `##` 11 対 11。`### Contents` あり。Figure 39–43 あり。Note 9+重複1 を JA も保持。番号リスト 36/36。`-` リスト 16/16。Ex 116–128 欠番なし |
| 2. コードフェンスが EN と一字一句一致 | 合格 | 76/76。言語タグ `racket` 50 + 空 26。対ごとの本文不一致 0。言語タグ+本文の連結 SHA256 `8cd49e9abd41f2f0…b695a4` が双方同一 |
| 3. 明らかな誤訳・英語の取り残し・プレースホルダ | 合格（残件は任意） | TODO/FIXME/未訳/XXX/仮訳は 0。未訳の英文段落は無い。フェンス内英語は要件どおり残している |

## 1. 省略

### 見出し

| EN | JA |
|----|----|
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

Error Messages の italic サブ見出し 5 も双语で対応する。

- Function Applications in BSL（JA L845）
- Wrong Data in BSL（JA L904）
- Conditionals in BSL（JA L934）
- Function Definitions in BSL（JA L980）
- Structure Type Definitions in BSL（JA L1029）

### 練習問題 116–128

| 番号 | JA 行付近 | 対応 |
|------|-----------|------|
| 116 | 125 | 合法式 3 項 |
| 117 | 133 | 非合法 3 項 |
| 118 | 141 | 合法定義 3 項 |
| 119 | 149 | 非合法定義 2 項 |
| 120 | 156 | 合法/非合法 3 項 + 範疇判定 |
| 121 | 310 | ステップ評価 3 項 |
| 122 | 318 | 定義フェンス + 式 3 項 |
| 123 | 512 | `if` フェンス |
| 124 | 578 | プログラム 3 本 |
| 125 | 691 | define-struct 3 項 |
| 126 | 699 | 値判定 5 項 |
| 127 | 714 | 評価予測 5 項 |
| 128 | 802 | 失敗テストフェンス |

### 節ごとのフェンス数（JA = EN）

| 節 | 数 |
|----|----|
| Vocabulary | 1 |
| Grammar | 5 |
| Meaning | 11 |
| Meaning and Computing | 0 |
| Errors | 11 |
| Boolean | 4 |
| Constants | 9 |
| Structures | 11 |
| Tests | 2 |
| Error Messages | 22 |
| 合計 | 76 |

Boolean 節の非フェンスブロック数が EN 14 / JA 13 なのは、EN 抽出の Exercise 123 が改行で割れているだけ。本文（`if` 説明・フェンス）は JA にある。Error Messages が JA +2 なのは末尾免責と HTML コメントであり、省略ではない。

Grammar の DrRacket 2 部分 Note がリスト内（JA L106）と直後（JA L109）で重複しているのは、EN 抽出 L164–172 の重複を写したもの。JA の独自欠落/増補ではない。

## 2. コードフェンス

- 76 対すべて、開始行の言語タグとフェンス本文がバイト一致。
- Figure 39–43 の ASCII、評価トレース、Error Messages 表、`check-*` 例を含む。
- フェンス外のインライン式は、EN 抽出が HTML 由来で空白を潰している（例: `(=yz)`、`(define(fx)x)`、`(poly35)`）。JA は学習可能な BSL として空白を戻している（`(= y z)`、`(define (f x) x)`、`(poly 3 5)`）。これはフェンス一致要件の対象外。

## 3. 誤訳・英語・プレースホルダ

コード以外に、未訳のまま残った英文段落は無い。残っている英語は次のいずれか。

- 見出しの `(English)` 併記
- フェンス内（要件どおり EN 複製）
- 英語の例文（`"the cat is round"` / `"the brick is a car"`）
- 識別子・キーワード（`cond`、`define-struct`、`check-expect` 等）
- DrRacket が出す引用 `"this function is not defined"`（JA L576 は英語原文＋括弧内和訳）
- 章参照の英語併記: `lambda を使った計算 (Computing with lambda)`、`入力エラー (Input Errors)`、`無名関数 (Nameless Functions)`。`Refining Interpreters（インタプリタの洗練）` は既訳が無いので英語＋括弧

以前のローカル検証（`d91061a`）が挙げた P1–P4（やり取り領域、ステッパ、検査付き版、定義上誤り、メッセージ和訳、章名英語放置）は、現行 `53f5786` の本文では解消済み。`やり取り` 0、`ステッパ` は `ステッパー` のみ、L818 は「誤りを犯すのが当たり前の初心者」、L576 は英語引用付き。

### 残リスク（合格を覆さない）

任意。直すなら外科的に。フェンスは触らない。

1. `04-intermezzo1.md` L491（Boolean Expressions）
   - 現状: `たまたま 0 で割りたくない`
   - EN: `we don’t wish to divide by 0 accidentally`
   - 修正案: `誤って 0 で割らないようにするため`

2. `04-intermezzo1.md` L484（同節）
   - 現状: `BSL 定義の関数` / `語用論`
   - EN: `BSL-defined functions` / `pragmatics`
   - 「BSL 定義」は「プログラマが BSL で定義した関数」にも読める。修正案: `BSL があらかじめ定義した関数`。語用論は初出なので `語用論 (pragmatics)` 併記でもよい。

導入の「4つ目の節でエラーの議論を再開」「最後の節でテスト」は EN も TOC とずれる。翻訳の責任ではない。

## 既存チェックとの関係

`docs/hermes-check-i1-draft.md` / `live.md` / `local.md` は見たが、数値は再計測した。フェンス 76 一致と Ex 116–128 収録は再確認できた。本ファイルの判定はそれらの文面をコピーしていない。
