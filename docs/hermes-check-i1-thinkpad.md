# Hermes 独立検証（ThinkPad）: Intermezzo 1 日本語草稿

- 検証者: ローカル Hermes（grok-4.6 / xai-oauth）。ホスト `mevius-ThinkPad-X240`。agy 未使用・未読。
- 日時: 2026-09-17 00:43 JST
- ブランチ: `docs/intermezzo1-complete-ja` @ `05755b018fd930a2c21ddba2d72fee727a4e01d4`
- 対象: Issue #16 / #25、PR #26
- JA: `04-intermezzo1.md`（1069 行 / 59796 bytes / 41154 文字 / SHA256 `f35557f9…15ef18f`）
- EN: `extracted/original_markdown_04_i1-2.md`（1340 行 / 53229 bytes / 52961 文字 / SHA256 `bd1bfcd3…720ed4e`。ファイル名は i1-2 だが `## Intermezzo` は I1 のみ）
- 参考: `docs/hermes-check-i1-*.md` の見出し形式のみ。数値は本セッションで再計測。
- 方法: 行ベースのフェンス抽出と対ごとの本文比較、見出し / Exercise / Figure / Note / リストの機械抽出、JA・EN の通読。

合格

## 判定（Claim / Evidence / Warrant）

主張: PR #26 の Intermezzo 1 草稿は、必須3項（省略なし・フェンス一致・明らかな誤訳/英語取り残し/プレースホルダなし）を満たす。差し戻し理由はない。

根拠: 下記の機械照合と通読。agy の提案は見ていない。

論拠: #25 のハードゲートは「落ち」と「コードフェンス改変」である。現行草稿にはどちらもない。残るのは語感の任意修正であり、再下訳や差し戻しの対象ではない。

## 必須チェック

| 項目 | 判定 | 要約 |
|------|------|------|
| 1. 省略（段落・リスト・練習問題 116–128・図・注） | 合格 | `##` 11 対 11、`### Contents` あり。Figure 39–43 あり。`**Note:**` 10 + 文法用語注 1 を JA も保持。番号リスト 36/36。`-` リスト 16/16。パイプ行 172/172。Ex 116–128 欠番なし |
| 2. コードフェンスが EN と一字一句一致 | 合格 | 76/76。言語タグ `racket` 50 + 空 26。対ごとの本文・言語タグ不一致 0。連結 SHA256 が双方同一 |
| 3. 明らかな誤訳・英語の取り残し・プレースホルダ | 合格（残件は任意） | TODO/FIXME/未訳/XXX/仮訳/TBD は 0。未訳の英文段落は無い。フェンス内英語は要件どおり残している |

フェンス連結 SHA256（各ブロックを `` ```lang\n `` + body + `` ```\n `` で 76 本連結）:

`c695d6bcf824c2fdb6d97e878ee84a750a1b0ffeb679b59cb69f056bc7a1757f`（JA = EN）

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

節ごとの空白行区切り段落数は、Boolean が JA 18 / EN 19、Error Messages が JA 43 / EN 41。前者は Ex 123 末尾の “as a cond expression.” を指示文へ前倒しした数え差。後者は末尾の学習用免責（EN に無い追加）と改行差。内容の落ちではない。

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

フェンス外の番号付き項目は 36/36。EN 抽出が空白を潰したインライン式（例: `(+123)`）は JA が `` `(+ 1 2 3)` `` に空白を戻している。フェンス内ではないのでハードゲート外。原本 HTML の空白復元であり、項の欠落ではない。

### 図・注・リスト

- Figure 39–43: フェンス内キャプションが EN と同一。本文は「図N」＋キャプションの Figure 併記。
- `**Note:**` ブロック 10、加えて “Note on Grammatical Terminology” / 「文法用語についての注」1。Grammar の DrRacket Note 二重（JA L106 と L109）は EN L164 と L170 の重複を写したもの。
- `-` リスト 16/36 番号リスト。目次 10 項は 1 対 1。

### 節ごとのフェンス数（JA = EN）

| 節 | 数 |
|----|----|
| Vocabulary | 1 |
| Grammar | 5 |
| Meaning | 11 |
| Meaning and Computing | 0 |
| Errors | 11 |
| Boolean | 4 |
| Constant Definitions | 9 |
| Structure Type Definitions | 11 |
| Tests | 2 |
| Error Messages | 22 |
| 合計 | 76 |

## 2. コードフェンス

- 本数: JA 76、EN 76
- 言語タグ: 双方 `racket` 50、空 26
- 対 1..76 の lang 不一致 0、body 不一致 0
- 連結 SHA256 上記（双方同一）

Error Messages の ASCII 表はフェンス内のため英語のまま。これは #25 の「一字一句一致」要件どおりであり、未訳扱いしない。

## 3. 誤訳・英語取り残し・プレースホルダ

プレースホルダ検索（TODO / FIXME / XXX / 未訳 / 仮訳 / TBD）は JA 0。

通読で見た英語核は次のいずれかで、取り残しではない。

- 見出し・Exercise 番号の英語併記（#25 推奨形式）
- 章参照の英語核＋日本語（Computing with lambda、Refining Interpreters、Nameless Functions、Input Errors）
- UI 引用 `*RUN*`
- フェンス内の語彙・文法・エラー表

既指摘の用語（やり取り領域、ステッパ、チェック付きバージョン）は現行稿では 対話領域 3 / ステッパー 12 / チェック付き 1。旧形 0。

明らかな誤読は見つからなかった。EN L295 の孤立した “End” は JA L188「以上。」に対応する。

## 任意残件（差し戻しにしない）

1. Ex 123: EN はフェンス後に “as a cond expression.” が独立文。JA は「次を `cond` 式に書き換えられることを示す規則を書きなさい」へ前倒し。意味は残っている。
2. Boolean L491「たまたま 0 で割りたくない」は “don’t wish to divide by 0 accidentally” のやや弱い訳。直すなら「誤って 0 で割らないように」。
3. Boolean L484「BSL 定義の関数」は “BSL-defined functions”。直すなら「BSL があらかじめ定義した関数」。
4. L484「語用論」に英語 gloss（pragmatics）が無い。任意。
5. 末尾 L1066–1068 の学習用免責は EN に無い追加。省略ではない。
6. 練習問題の文体が「見てください／考えよ／書きなさい」で揺れる。品質の話であり落ちではない。

## 本文について

フェンス不一致・欠番・欠節は無いので、`04-intermezzo1.md` は変更しない。

マージはしない（ユーザー承認・rebase-merge 想定）。#17 は開始しない。
