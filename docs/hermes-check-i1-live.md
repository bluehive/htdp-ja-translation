# 独立検証（live）: Intermezzo 1 日本語草稿

- 日時: 2026-09-17 00:16 JST
- 検証者: Hermes（grok-4.6 / xai-oauth）。agy 未使用。agy 提案は参照していない。
- ブランチ: `docs/intermezzo1-complete-ja` @ `85cbce4`（`Align Intermezzo 1 terms with Part I/II after Hermes check.`）
- JA: `04-intermezzo1.md`（59796 bytes / 41154 文字 / 1070 行）
- EN: `extracted/original_markdown_04_i1-2.md`（53229 bytes / 52961 文字 / 1341 行）
- 対象は **現在の** `04-intermezzo1.md`。`docs/hermes-check-i1-draft.md` と `docs/hermes-check-i1-local.md` は照合結果の突き合わせにだけ使い、結論は再計測から出した。
- 方針: 公式訳ではない個人学習用意訳。正確さより「落ちがない」こと優先。フェンス改変は差し戻し。

## 総合判定

**合格（ハードゲートはすべて通過。残件は軽微のみ）**

| 必須チェック | 判定 | 要約 |
|---|---|---|
| 1. 省略（段落・リスト・Exercise 116–128・コード例） | **合格** | `##` 11、`### Contents`、Figure 39–43、Note 10、Ex 116–128、番号リスト 36/36、箇条書き行 52/52。フェンス外のインライン式も空白正規化後に一致 |
| 2. コードフェンスが EN と一字一句一致 | **合格** | 76/76。言語タグ込み連結 SHA256 一致。対ごとの本文不一致 0 |
| 3. 見出し対応 | **合格** | EN の `##` 11 節がすべて JA にある。Error Messages の italic サブ見出し 5 も双语である |
| 4. 誤訳・英語混在・プレースホルダ | **軽微のみ** | プレースホルダ 0。`85cbce4` で前回の用語指摘は解消済み。残るのは語用論の英語併記など |

主張: Issue #25 が差し戻し条件にしている「省略」と「フェンス改変」は、現行草稿にはない。
根拠: 下記「検証方法」の機械照合と、JA/EN の通読。
論拠: 完了条件のハードゲートは通っている。残件は学習用の用語併記であり、再下訳や差し戻しの理由にならない。

前回のローカル検証（`docs/hermes-check-i1-local.md`）は `d96c161` 時点で **要修正** とした。その後の `85cbce4` で指摘した用語・誤読は本文に入っている。本 live は **その後の HEAD** を独立に測った結果である。

---

## 検証方法

1. フェンス抽出（`` ```lang\n...\n``` ``）を JA/EN で対にし、本文・言語タグを比較。連結バイト列の SHA256 も比較。
2. `##` / `###`、`Exercise` / `練習問題`、`Figure` / `図`、blockquote Note、番号付き項目、箇条書き行数を列挙。
3. フェンスを除いた散文の段落数、プレースホルダ検索、英語 3 語以上の連続。
4. Exercise 116–128 の番号付き式を空白除去して EN と突合。
5. JA を通読し、EN 各節の論点（法則名・Note・図・テスト形式）が落ちていないかを確認。agy の出力は開いていない。

---

## 1. 省略チェック（合格）

### 見出し対応（抜けなし）

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

Error Messages の 5 サブ見出しも JA にある。

- Function Applications in BSL（L845）
- Wrong Data in BSL（L904）
- Conditionals in BSL（L934）
- Function Definitions in BSL（L980）
- Structure Type Definitions in BSL（L1029）

### 節ごとのフェンス数（JA = EN）

| 節 | EN フェンス | JA フェンス |
|---|---|---|
| Vocabulary | 1 | 1 |
| Grammar | 5 | 5 |
| Meaning | 11 | 11 |
| Meaning and Computing | 0 | 0 |
| Errors | 11 | 11 |
| Boolean | 4 | 4 |
| Constants | 9 | 9 |
| Structures | 11 | 11 |
| Tests | 2 | 2 |
| Error Messages | 22 | 22 |
| **計** | **76** | **76** |

フェンスを除いた段落数は EN 258 / JA 259。JA が 1 多いのは末尾の **免責**（EN にない追加。リポジトリ方針。省略ではない）。

### Exercise 116–128

すべて本文にあり、番号付き項目数は EN と一致する。フェンス外のインライン式は、抽出 EN が HTML 由来で空白潰れ（例: `(=yz)`）しているのに対し、JA は学習可能な BSL として空白を戻している（`(= y z)`）。空白除去後は 116–128 の全項目が一致。フェンス内の式は潰れたままの EN を複製している。

| # | JA 行付近 | 項目数 JA/EN | フェンス JA/EN |
|---|---|---|---|
| 116 | 125 | 3/3 | 0/0 |
| 117 | 133 | 3/3 | 0/0 |
| 118 | 141 | 3/3 | 0/0 |
| 119 | 149 | 2/2 | 0/0 |
| 120 | 156 | 3/3 | 0/0 |
| 121 | 310 | 3/3 | 0/0 |
| 122 | 318 | 3/3 | 1/1 |
| 123 | 512 | 0/0（if 形はフェンス） | 1/1 |
| 124 | 578 | 0/0（プログラム3本はフェンス） | 3/3 |
| 125 | 691 | 3/3 | 0/0 |
| 126 | 699 | 5/5 | 1/1 |
| 127 | 714 | 5/5 | 1/1（本体。直後の Figure 43 は次節導入） |
| 128 | 802 | 0/0（テストはフェンス） | 1/1 |

### Figure / Note / リスト

- Figure 39–43: キャプション（フェンス内・英語のまま）と本文の「図N」参照の両方がある。
- EN blockquote `> **Note:**` 10、JA `> **注 (Note):**` 10。
- Grammar の DrRacket 2 部分 Note がリスト内と直後で重複しているのは **EN 抽出側の重複の写し**。JA の独自欠落/増補ではない。
- 箇条書き・番号リスト行: EN 52 / JA 52。番号付き項目: 36/36。
- 導入の Contents 10 項目、キーワード説明、合法/非合法例、beta / condfalse / condtrue、stuck、短絡、check-* 7 種、Error Messages 各表: 通読で落ちを見ていない。

### 通読で確認した論点（落ちなし）

- 導入: Fixed-Size Data のたとえ、syntax/semantics、cat/brick 例文、Note（設計原理の補完）
- Vocabulary: 語彙の3種、図39、集合は列挙で定義
- Grammar: `=`/`|`/`...` の読み方、define の 0/1/2 繰り返し例、キーワード、42 が文である推論、複合文、非合法3例、空白とスタイル、Ex 116–120、文法用語（header/body/left-hand side/actual arguments）
- Meaning: 算術・Boolean/string 法則、図42、beta、poly 例、cond 規則、Ex 121–122
- Meaning and Computing: ステッパー＝プレ代数の生徒、model、Computing 節の練習、刈り込み
- Errors: 構文 vs 実行時、`(/ 1 0)`、stuck、my-divide の網掛け、最も外側かつ左、checked-area-of-disk
- Boolean: 文法拡張、pragmatics/短絡、and/or の cond 省略、Ex 123
- Constants: `(define name expr)`、RADIUS/DIAMETER、AREA-OF-RADIUS 順、入れ替えエラー、Ex 124
- Structures: 合法/非合法 define-struct、コンストラクタ/セレクタ/述語、値の宇宙の拡張、等式、Ex 125–127、図43
- Tests: RUN で末尾へ移動、check-* 成功例、Ex 128（失敗するテスト）
- Error Messages: 3 部構成の説明、最悪例（`<`）、5 分類の表

---

## 2. コードフェンス（合格）

| 項目 | 値 |
|---|---|
| EN フェンス数 | 76 |
| JA フェンス数 | 76 |
| 対の本文不一致 | **0** |
| 言語タグ不一致 | **0**（`racket` 50、空 26。順序も同一） |
| フェンス全体（開始行含む）SHA256 | `5ce411a87c168969db86746194925e40fcf80cb2b3555594fe56adf6fa1d2ad1`（JA = EN） |

主張: フェンス内は英語原本と一字一句一致する（コメント含む）。
根拠: 76 対すべて `lang` と `body` が等しく、連結 SHA256 も一致。
論拠: Issue #25 の「不一致は差し戻し」条件は発火しない。

---

## 3. 誤訳・英語混在・プレースホルダ

プレースホルダ（TODO / FIXME / XXX / 未訳 / 仮訳 / TBD / WIP / PLACEHOLDER）: **0 件**。

### 重大

なし。

### 軽微

1. **語用論**（JA L484）  
   EN `pragmatics`。言語学用語としては正しい。本書の syntax/semantics と並べるなら `語用論 (pragmatics)` と併記した方が Vocabulary 節の用語注と揃う。落ちではない。マージ阻止にしない。

2. **フェンス外インラインコードの空白復元**  
   抽出 EN は `(=yz)`、`(fdefine)`、`(poly35)` のように空白が潰れている。JA の練習問題本文は空白あり。フェンス内は EN どおり。#25 の必須条件外。学習用としては妥当。

3. **末尾免責**  
   EN にない追加。README 方針と一致。省略ではない。

### `85cbce4` で解消済み（本 live で再確認）

前回 `docs/hermes-check-i1-local.md` の P1–P4。現行ファイルでの出現:

| 語 | 回数 |
|---|---|
| やり取り | 0 |
| 対話領域 | 3 |
| 対話ウィンドウ | 1 |
| ステッパ（「ステッパー」を除く独立形） | 0（「ステッパー」12） |
| 検査付き | 0 |
| チェック付き | 1 |
| 定義上 | 0 |
| `this function is not defined`（L576、英語原文＋和訳） | あり |

Error Messages 冒頭は「誤りを犯すのが当たり前の初心者向け」になっており、定義フォームとの誤読は残っていない。

### 英語混在のうち許容するもの

- 見出しの `(English)` 併記（#25 推奨形式）
- フェンス内のすべて（一致済み）
- 英語の例文（`the cat is round` / `the brick is a car`）
- 識別子・キーワード（`cond`、`define-struct`、`check-expect` 等）
- DrRacket が出す英語メッセージ（表フェンスおよび L576 の引用）

---

## 注記（不合格にしない）

- **原文の重複 Note**: Grammar の DrRacket 2 部分 Note は EN L164–166 と L170–172 で重複。JA L106 と L109 も重複。抽出アーティファクト。
- **原文の節番号の言い回し**: 導入の「4つ目の節でエラー」「最後の節でテスト」は EN も同じで、実際の `##` 順（Meaning and Computing が 4 番目、Tests は Error Messages の直前）とずれる。JA の責任ではない。
- **旧ギャップ分析**: `docs/hermes-review-i1.md` の欠落リスト（Ex 116–128、Figure、Error Messages 本文）は **現行草稿では解消済み**。あのファイルは薄い要約時点のスナップショット。
- **`docs/hermes-check-i1-draft.md`**: フェンス 76 一致・Ex 全収録は再確認できた。同ファイルの「41056 bytes」は文字数でありバイト数ではない（当時の文字数。現行は 41154 文字 / 59796 bytes）。

---

## 既存レポートとの差分

| | `hermes-check-i1-draft.md` | `hermes-check-i1-local.md` | **本ファイル（live）** |
|---|---|---|---|
| 経路 | 実行エージェント（sand-box） | ローカル Hermes @ 用語修正前 | ローカル Hermes @ `85cbce4` |
| フェンス 76 一致 | YES | YES | YES（SHA256 再計測） |
| Exercise | 全収録 | 全収録 | 全収録＋空白正規化突合 |
| 用語 | 意訳の語感とだけ | P1–P4 を要修正 | P1–P4 は解消。残は軽微 |
| 判定 | 統合可 | 要修正 | **合格（軽微のみ）** |

---

## 結論（Claim / Evidence / Warrant）

主張: 現行の Intermezzo 1 草稿（`04-intermezzo1.md` @ `85cbce4`）は、省略なし・フェンス一致という #25 の完了条件を満たす。agy は使っていない。マージを止める落ち・フェンス改変はない。

根拠: フェンス 76 対 SHA256 `5ce411a8…` が JA=EN。見出し 12。Exercise 116–128。Note 10。リスト行 52。番号項目 36。通読で節の論点が対応。前回の用語指摘は `85cbce4` で消えている。

論拠: #25 は agy を信じず省略とコード改変を見るためのイシューである。その観点では差し戻し理由はない。残る語用論の英語併記は任意。rebase-and-merge はユーザー承認待ちのまま（本検証ではマージしない）。
