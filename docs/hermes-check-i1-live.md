# 独立検証（live）: Intermezzo 1 日本語草稿

- 日時: 2026-09-17 01:22 JST
- 検証者: Hermes（grok-4.6 / xai-oauth）。agy 未使用。agy 下訳・`docs/agy-check-i1.md` は開いていない。
- ブランチ: `docs/intermezzo1-complete-ja` @ `fe0569cd0293a1f77a85be6bda422b9eae00ca77`
- 本文の最終コミット: `85cbce4`（用語揃え）。本 HEAD は検証メモの追加のみ。
- JA: `04-intermezzo1.md`（59796 bytes / 1069 行、SHA256 `f35557f93d7901f8c90335a374015f4d8b76e1c2105b7067a264514ec15ef18f`）
- EN: `extracted/original_markdown_04_i1-2.md`（53229 bytes / 1340 行、SHA256 `bd1bfcd3d611ef312e53acef83cdf9e065927ec402ba8ee2a8622ea9a720ed4e`）
- Issue: #16 / 作業指示 #25 / PR #26
- 判定基準: #25（省略禁止、フェンス一字一句、見出しは「日本語 (English)」推奨、章・Exercise 番号は原本どおり）。公式訳ではない個人学習用意訳。
- 方法: フェンス・見出し・リスト・Exercise を Python で抽出して突合。両ファイルを節ごとに通読。既存 `docs/hermes-review-i1.md` / `docs/hermes-check-i1-draft.md` / 旧 live は突き合わせ後に対照しただけ。結論は再計測から出した。

## 主張 / 根拠 / 論拠

主張: 現行草稿は #25 の差し戻し条件（段落・リスト・Exercise の省略、コードフェンス改変）を満たさない。ハードゲートは合格。明らかな誤訳は 1 件（「accidentally」）で、落ちではない。

根拠: 下表の機械照合と、節ごとの通読（Boolean の段落差は練習問題 123 の指示文の位置、Error Messages の段落差は JA 末尾の免責追加）。

論拠: 完了条件は「落ちがない」こととフェンス一致。意訳による文結合は欠落としない。agy フォールバック草稿は根拠に使っていない。

## 必須チェック

| 項目 | 判定 | 要約 |
|---|---|---|
| 1. 省略（段落・リスト・Exercise 116–128） | **合格** | `##` 11/11。リスト 52/52（番号付き 36、箇条書き 16）。Figure 39–43。`> **注 (Note):**` 10 + 文法用語注 1。Ex 116–128 欠番なし |
| 2. コードフェンスが EN と一字一句一致 | **合格** | 76/76。言語タグ込み連結 SHA256 が JA=EN。対ごとの本文不一致 0。言語タグ: `racket` 50 + 空 26 |
| 3. 見出し・練習番号 | **合格**（章タイトル 1 件だけ推奨形式と逆） | 節見出しは `日本語 (English)`。章タイトルのみ English 先行。Exercise は `練習問題 N (Exercise N)` で 116–128 |
| 4. 明らかな誤訳・欠落・プレースホルダ | **軽微〜中が少数** | プレースホルダ 0。旧指摘（やり取り領域 / ステッパ / 検査付き版 / 定義上誤り）は現行にない。中 1 件は L491 |

### 見出し対応

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

Error Messages の italic サブ見出し 5 も双语で残っている。

### 節ごとのフェンス数（JA = EN）

| 節 | フェンス |
|---|---|
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

### Exercise 116–128

| N | EN 形式 | JA | 項目 |
|---|---|---|---|
| 116 | 合法な式 3 | あり | 3 |
| 117 | 非合法な式 3 | あり | 3 |
| 118 | 合法な定義 3 | あり | 3 |
| 119 | 非合法な定義 2 | あり | 2 |
| 120 | 合法/非合法の判別 3 | あり | 3 |
| 121 | ステップ評価 3 + ステッパー | あり | 3 |
| 122 | 定義 + 式 3 + ステッパー | あり | 3 |
| 123 | `if` → `cond` 規則（フェンス 1） | あり（指示をフェンス前に吸収） | フェンス 1 |
| 124 | プログラム 3 + ステッパー | あり | フェンス 3 |
| 125 | define-struct 3 | あり | 3 |
| 126 | 値の特定 5 | あり | 5 |
| 127 | 評価予測 5 + 対話領域/ステッパー | あり | 5 |
| 128 | 失敗テスト フェンス 1 | あり | フェンス 1 |

`docs/hermes-review-i1.md` が旧草稿（~7KB）に対して挙げた欠落（Contents、Note、Figure 39–43、Ex 116–128、Error Messages 本文）は、現行 JA では解消済み。

## 1. 省略（詳細）

空行分割の段落数は Boolean 以外ほぼ一致。

- Boolean: EN 18 / JA 17。差は練習問題 123。EN はフェンス後に独立文 `as a cond expression.` がある。JA は「次を `cond` 式に書き換えられることを示す規則を書きなさい」へ吸収。課題内容は落ちていない。
- Error Messages: EN 40 / JA 42。差は JA 末尾の `---` と免責（追加であり省略ではない）。
- リスト行: 番号付き 36/36、`-` 16/16。
- blockquote 行: EN 20 / JA 18。差は同一引用の改行（指針 2 行→1 行、値の定義 3 行→2 行）であり、Note の欠落ではない。
- Grammar の DrRacket Note（定義領域／対話領域）は EN 抽出が二重。JA も二重のまま。省略ではない。
- 通読で確認した論点: 導入 3 段落、Vocabulary 図後、Grammar のキーワード／合法例／非合法例、Meaning の beta / condfalse / condtrue、Computing のステッパー 3 段落、Errors の stuck / 最左最外指針 / `error`、Boolean の and/or 短絡と同値、Constants の定義順エラー、Structures の constructor/selector/predicate、Tests の RUN 移動、Error Messages 導入と 5 区分。いずれも対応段落あり。

## 2. コードフェンス

- 抽出: 正規表現 `` ```([^\n]*)\n(.*?)``` ``（DOTALL）。
- 各フェンスを順に比較し、言語タグ＋本文の差分 0。
- 連結 SHA256（各フェンスを `lang + "\n" + body` として連結）:
  `8cd49e9abd41f2f02da91764125106cd3d9c1f6d22ad408313da1b0766b695a4`
  （JA = EN）。

必須ルール 2 の対象はフェンス内のみ。フェンス外の番号付き式は EN 抽出で空白が潰れている（例: `(=yz)`、`(define(fx)x)`）。JA は空白復元＋バッククォート。学習用としては原本に近い。フェンスには触っていない。

Error Messages 表の右列説明は英語のまま。フェンス一致規則のため翻訳禁止。EN 抽出時点で既に省略記号付き。

## 問題リスト

重大度: 重大 = 差し戻し（省略またはフェンス不一致） / 中 = 意味の歪みでマージ前に直したいが落ちではない / 軽微 = 任意 / 情報 = 落ちではない観測。

| ID | 重大度 | 場所 | 問題 | 修正提案 |
|----|--------|------|------|----------|
| P1 | 中 | JA 491 / EN 667–668 | EN “we don’t wish to divide by 0 accidentally” を「たまたま 0 で割りたくない」。accidentally は偶然ではなく「誤って 0 除算しない」。 | 「誤って 0 で割らないため」 |
| P2 | 軽微 | JA 512–516 / EN 702–713（練習問題 123） | フェンス後の独立文をフェンス前に吸収。意味は落ちていない。 | 任意: フェンス後に「を `cond` 式として。」を残す |
| P3 | 軽微 | JA 484 | `語用論` に英語併記 `(pragmatics)` がない。構文 / 意味論は初出で併記あり。 | 任意: `語用論 (pragmatics)` |
| P4 | 軽微 | JA 4 章タイトル | 推奨形式は「日本語 (English)」。現行は English 先行・全角括弧。節見出しは推奨形式。 | 任意 |
| P5 | 軽微 | JA 19, 21 | EN `Fixed-Size Data` を「第I部「固定サイズのデータ」」。同ファイル内の `入力エラー (Input Errors)` 等は英語併記あり。導入だけ英語核が無い。 | 任意 |
| P6 | 軽微 | JA 484 | “BSL-defined functions” → 「BSL 定義の関数」。読みにくい。 | 任意: 「BSL で定義された関数」 |
| P7 | 軽微 | JA 536 | “proper expression” → 「きちんとした式」。リテラルでない計算式の意。 | 任意: 「通常の式」または「リテラルでない式」 |
| P8 | 軽微 | JA 512 | “in another way” → 「別の意味で」。仕方／点のずれ。 | 任意: 「別の点で」 |
| I1 | 情報 | JA 1066–1068 | JA のみ `---` と免責。省略ではなく追加。 | 触らない |
| I2 | 情報 | フェンス外の番号付き式 | EN 抽出の空白潰れを JA が復元。フェンス要件の対象外。 | 変更しない（推奨） |
| I3 | 情報 | Grammar の DrRacket Note | EN 抽出の二重を JA も保持。 | 原本 HTML 確認は範囲外 |
| I4 | 情報 | Error Messages 表 | 右列は英語のまま（フェンス）。 | 触らない |

重大: **0 件**。

プレースホルダ（TODO / FIXME / TBD / XXX / 未訳 / `[訳`）: 0。

残っている英語は次のみ（未訳段落ではない）:

- 見出し・練習番号の英語併記
- 書籍内参照: `Computing with lambda`、`Refining Interpreters`、`Nameless Functions`、`Input Errors`（日本語併記あり）
- DrRacket 引用 `"this function is not defined"` とフェンス内 UI
- 文法 blockquote（`definition = ... | (define name expr)` など）
- 英語の例文 `"the cat is round"` / `"the brick is a car"`（言語例として原文保持）

## 総合

- ハードゲート: **合格**
- 総合: **合格**（P1 は任意〜推奨。全文差し戻しではない）
- `04-intermezzo1.md` の修正: 本検証ではしていない
- git commit / push / マージ: しない（ユーザー承認待ち、rebase-and-merge）

## 検証コマンド（再実行用）

Python 3 で JA/EN を読み、`` ``` `` フェンス 76 本の言語タグ＋本文を逐次比較。Exercise は EN `**Exercise N.` と JA `**練習問題 N (Exercise N).` で 116–128 を抽出。リストはフェンス除去後の `^[-*]|\\d+\\.`。

## フォローアップ（校正github-chan, 2026-09-17）

ThinkPad 上の live 検証後、P1（accidentally）を「誤って 0 で割らないため」に修正。あわせて P3（語用論 (pragmatics)）と P6（BSL で定義された関数）も適用。フェンスは未変更。commit / マージはユーザー確認待ち。
