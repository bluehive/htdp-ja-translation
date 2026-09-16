# ローカル Hermes 独立検証: Intermezzo 1（#16 / #25 / PR #26）

- 日時: 2026-09-17 00:09 JST
- 検証者: Hermes（grok-4.6 / xai-oauth、ThinkPad ローカル `hermes -z`）
- ブランチ: `docs/intermezzo1-complete-ja` @ `d91061a`
- JA: `04-intermezzo1.md`（59610 bytes / 41056 文字 / 1070 行）
- EN: `extracted/original_markdown_04_i1-2.md`（53229 bytes / 52961 文字 / 1341 行）
- 参考: `docs/hermes-review-i1.md`（ギャップ分析）、`docs/hermes-check-i1-draft.md`（実行エージェント側の照合。本ファイルはそれとは別経路）
- 方針: agy 下訳ではなく実行エージェント草稿なので、省略・フェンス・用語を厳しく見た。必須3項目のうち 1・2 は機械照合、3 は通読。

## 総合判定

**要修正**（必須の省略・フェンスは合格。マージ前に用語と数箇所の誤読を直す）

| 必須チェック | 判定 | 要約 |
|---|---|---|
| 1. 省略（節・段落・Exercise 116–128・例） | **合格** | `##` 11 + `### Contents`、Figure 39–43、Note 10、Exercise 116–128、リスト行 52/52 |
| 2. コードフェンスが EN と一字一句一致 | **合格** | 76/76。言語タグ込み SHA256 一致。不一致 0 |
| 3. 誤訳・英語混在・プレースホルダ | **要修正** | プレースホルダなし。既存 Part I/II 用語と衝突する訳語、引用エラーメッセージの和訳、章参照の英語放置 |

主張: Issue #25 が差し戻し条件にしている「省略」と「フェンス改変」は、この草稿にはない。
根拠: 下記「検証方法」の機械照合と通読。
論拠: 完了条件のハードゲートは通っている。残るのは既存訳との用語揃えと、読者が誤読する散文数箇所であり、全文差し戻しではない。

---

## 検証方法

1. フェンス抽出（正規表現 `` ```lang\\n...``` ``）を JA/EN で対にして本文・言語タグを比較。連結バイト列の SHA256 も比較。
2. `##` / `###` 見出し、`Exercise` / `練習問題` 行、`Figure`、blockquote Note、箇条書き行数を列挙。
3. プレースホルダ（TODO / 未訳 / FIXME 等）を JA 散文から検索。
4. JA を通読し、EN と突き合わせて誤訳・英語混在・既存章の用語を確認。

`docs/hermes-check-i1-draft.md` の「76 完全一致・Ex 全収録」は再確認できた。ただし同ファイルの「41056 bytes」は **文字数** でありバイト数ではない（実バイトは 59610）。

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

Error Messages の 5 サブ見出し（Function Applications / Wrong Data / Conditionals / Function Definitions / Structure Type Definitions）も JA に双语である。

### Exercise 116–128（すべて本文に存在）

| # | JA 行 | 内容の有無 |
|---|---|---|
| 116–120 | 125–162 | 合法/非合法の文。番号付き例あり |
| 121–122 | 310–331 | ステップ評価。定義フェンスあり（122） |
| 123 | 512–516 | `if` → `cond` 規則。フェンスあり |
| 124 | 578–605 | 定数定義3本。フェンス3つ |
| 125–127 | 691–728 | define-struct 合法判定・値判定・評価予測 |
| 128 | 802–814 | 失敗するテストのコピー。フェンスあり |

### Figure

EN の Figure 39–43 キャプションと ASCII フェンスはすべて JA にある。キャプション行そのものはフェンス内のため英語のまま（要件どおり）。

### Note

EN の blockquote `> **Note:**` は 10 個。JA の `> **注 (Note):**` も 10 個。Grammar の「DrRacket ではプログラムは2部分」Note がリスト内と直後で重複しているのは **EN 抽出側の重複を忠実に写したもの** であり、JA の独自欠落/増補ではない。

### 段落・リスト

- 箇条書き・番号リスト行は EN 52 / JA 52。
- 各 `##` 節に対応する JA 散文がある。文字数比はおおむね 0.5–0.63（日本語の文字数が英語より少ない典型域）。Vocabulary の 0.51 も、2 段落の内容は対応しており要約落ちではない。
- 末尾の **免責** ブロックは EN にない追加（リポジトリ方針。省略ではない）。

---

## 2. コードフェンス（合格）

| 項目 | 値 |
|---|---|
| EN フェンス数 | 76 |
| JA フェンス数 | 76 |
| 対の本文不一致 | **0** |
| 言語タグ不一致 | **0**（`racket` 50、空 26。順序も同一） |
| フェンス全体（開始行含む）SHA256 | `5ce411a87c168969…` で JA=EN |

主張: フェンス内は英語原本と一字一句一致する。
根拠: 76 対すべて `body` と `lang` が等しく、連結 SHA256 も一致。
論拠: Issue #25 の「不一致は差し戻し」条件は、この項目については発火しない。

---

## 3. 誤訳・英語混在・プレースホルダ（要修正）

プレースホルダ（TODO / FIXME / 未訳 / XXX / 仮訳）は **0 件**。

### 問題リスト（優先度順）

#### P1. 既存訳と衝突する用語

主張: Intermezzo 1 だけ用語が割れており、読者が Prologue / Part I / II と照合できない。
根拠:

| 箇所 | 本草稿 | 既存 JA | EN |
|---|---|---|---|
| L106, L109, L728 | やり取り領域 | Prologue / Part I: **対話領域 (interactions area)** | interactions area |
| L841 | やり取りウィンドウ | 同上（window なら対話ウィンドウでも可） | interactions window |
| ステッパ 12 箇所 | ステッパ | Part II ch.8: **ステッパー**；Part I は「ステッパー（stepper）」 | stepper |
| L431 | 検査付き版 `area-of-disk` | Part I 6.3: **チェック付きバージョン** | checked version |

論拠: Issue #16 完了条件に「既存の用語（構文・意味論・署名など）に合わせる」とある。対話領域は Prologue が初出の固有名詞なので、ここだけ「やり取り」は誤訳に近い。

推奨:

- `やり取り領域` → `対話領域 (interactions area)`
- `やり取りウィンドウ` → `対話ウィンドウ`（原文が window のとき）
- `ステッパ` → `ステッパー`
- `検査付き版` → `チェック付きバージョン`

#### P2. 「定義上」の誤読（Error Messages 冒頭）

- 場所: JA L818
- EN: `novices who, by definition, make mistakes`
- JA: `定義上誤りを犯す初心者のために特別に開発しました`

主張: 「定義上」が BSL の **定義フォーム** に読める。
根拠: この節は直後から define / define-struct のエラー例が続く。英語の by definition は「初心者とは誤りを犯す存在である」という挿入句。
論拠: 学習者が「定義の誤り専用のエラーシステム」と取る余地がある。

推奨: `BSL とそのエラー報告は、誤りを犯すのが当たり前の初心者向けに作られていますが、メッセージ自体には慣れが必要です。`

#### P3. DrRacket が実際に出す英語メッセージを和訳している

- 場所: JA L576
- EN: `you would therefore get an error, explaining that “this function is not defined.”`
- JA: `「この関数は定義されていない」と説明するエラーが出ます`

主張: 引用された UI 文字列は英語のまま残すべき。
根拠: Error Messages 節の表（フェンス）では `f: this function is not defined` が英語のまま。同じメッセージを本文で和訳すると、学習者が対話領域で探す文字列と一致しない。
論拠: フェンス内は英語必須、という方針と本文の引用方針を揃える。

推奨: `「this function is not defined」（この関数は定義されていない）`

#### P4. 既訳がある章・節名が英語のまま

| JA 行 | 草稿 | 既訳（目次 / 本文） |
|---|---|---|
| 248 | Computing with lambda | 07: `lambda を使った計算 (Computing with lambda)` |
| 337 | Refining Interpreters | 目次未確認。英語併記で可 |
| 339 | Computing に関する各節 | 各章の「計算 (Computing)」節 |
| 431 | Input Errors | 03: `入力エラー (Input Errors)` |
| 526 | Nameless Functions | 07 / 目次: `無名関数 (Nameless Functions)` |

英語例文 `"the cat is round"` / `"the brick is a car"` は原文の英語例なので残してよい。Error Messages の表内英語も要件どおり。

推奨: 既訳がある参照は `日本語 (English)`。未訳の `Refining Interpreters` だけ英語+括弧で残す。

#### P5. 同一ファイル内の用語ゆれ（軽微）

- Meaning 導入（L193）: `Boolean、String、Image` と英語のまま。Vocabulary では真偽値・文字列。EN も Booleans, Strings, Images。併記推奨: `真偽値 (Boolean)、文字列 (String)、画像 (Image)`
- L484 `語用論` ← `pragmatics`。言語学用語としては正しいが、本書の syntax/semantics/pragmatics 三分法を初出で説明していない。`語用論 (pragmatics)` と併記するか、「まず使い方（なぜ関数ではないか）を見る」程度に砕く。

### 英語混在のうち許容するもの

- 見出しの `(English)` 併記（#25 推奨形式）
- フェンス内のすべて（一致済み）
- 英語の例文（cat/brick）
- 識別子・キーワード（`cond`、`define-struct`、`check-expect` 等）

---

## 注記（不合格にはしない）

### フェンス外のインラインコード空白復元

抽出 EN は HTML 由来で空白が潰れている（例: `(=yz)`、`(fdefine)`、`(/10)`、`(poly35)`）。JA は学習可能な BSL として空白を戻している（`(= y z)`、`(f define)`、`(/ 1 0)`、`(poly 3 5)`）。

- フェンス内は潰れたままの EN を複製しており、要件どおり。
- フェンス外の復元は #25 の必須条件外。学習用としては妥当。公式に「抽出 MD の空白潰れまで再現」するなら別指示が必要。

### 原文の重複 Note

Grammar の DrRacket 2 部分 Note は EN L164–166 と L170–172 で重複。JA L106 と L109 も重複。抽出アーティファクト。翻訳の責任ではない。消すなら EN 側注記付きで。

### 原文の曖昧さ（翻訳は忠実）

導入の「4つ目の節でエラーの議論を再開」「最後の節でテスト」は EN も同様で、実際の `##` 順（Meaning and Computing が 4 番目、Tests は Error Messages の直前）とずれる。JA の責任ではない。

### 旧ギャップ分析との関係

`docs/hermes-review-i1.md` の欠落リスト（Ex 116–128、Figure 39–43、Error Messages 本文）は **現行草稿では解消済み**。あのファイルは「薄い要約」時点のスナップショット。

---

## 推奨修正（パッチ方針）

全文再生成はしない（フェンス一致を壊す）。以下のみ外科的に。

1. `やり取り領域` 4 箇所 → `対話領域`（L841 は `対話ウィンドウ` でも可）
2. `ステッパ` → `ステッパー`（12 箇所）
3. L431 `検査付き版` → `チェック付きバージョン`；`Input Errors` → `入力エラー (Input Errors)`
4. L818 の「定義上誤りを犯す初心者」を P2 の文に置換
5. L576 の和訳引用を英語原文付きに
6. L248 / L337 / L339 / L526 の章節名を既訳に合わせる
7. （任意）L193 の Boolean/String/Image を併記

修正後に再実行すべき最小チェック:

```text
フェンス SHA256 が変わっていないこと（76 対）
練習問題 116–128 の見出しが残っていること
rg やり取り → 0
rg ステッパ → ステッパーのみ
```

---

## 既存レポートとの差分

| | `docs/hermes-check-i1-draft.md` | 本ファイル |
|---|---|---|
| 経路 | 実行エージェント（sand-box フォールバック） | ローカル Hermes |
| フェンス 76 一致 | YES | YES（SHA256 でも確認） |
| Exercise | 全収録 | 全収録 |
| 用語・誤訳 | 「意訳の語感」とだけ | P1–P5 を具体列挙 |
| 判定 | 統合可 | **要修正**（ハードゲートは合格） |

---

## 結論（Claim / Evidence / Warrant）

主張: PR #26 の Intermezzo 1 草稿は、省略なし・フェンス一致という完了条件の中核は満たす。ローカル独立検証でも実行エージェントのフェンス報告は正しかった。ただし既存訳語との不一致と、Error Messages 冒頭の「定義上」誤読はマージ前に直した方がよい。

根拠: フェンス 76 対 SHA256 一致、見出し 12、Exercise 116–128、Note 10、リスト 52。通読で P1–P5。

論拠: #25 は agy を信じず省略とコード改変を見るためのイシューである。その観点では差し戻し理由はない。残件は用語表への揃えであり、再下訳ではない。

---

## 追記（2026-09-17）

上記 P1–P4 と任意の P5（Boolean/String/Image 併記）を `04-intermezzo1.md` に外科適用した。フェンス 76 対の SHA256 は変更なし（`5ce411a87c168969…`）。`やり取り` 0、`ステッパ` は `ステッパー` のみ。
