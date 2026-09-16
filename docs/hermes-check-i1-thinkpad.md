# Intermezzo 1 独立検証（ThinkPad / ローカル Hermes）

- 日時: 2026-09-17 00:47 JST
- 報告者: Hermes (grok-4.6)
- 作業ディレクトリ: `/home/mevius/my-project/htdp-ja-translation`
- ブランチ: `docs/intermezzo1-complete-ja`（HEAD `5bb5fa8` = `origin/docs/intermezzo1-complete-ja`）
- JA: `04-intermezzo1.md`（sha256 `f35557f93d7901f8c90335a374015f4d8b76e1c2105b7067a264514ec15ef18f`、1069 行）
- EN: `extracted/original_markdown_04_i1-2.md`（sha256 `bd1bfcd3d611ef312e53acef83cdf9e065927ec402ba8ee2a8622ea9a720ed4e`、1340 行）
- 関連: issue #16 / #25、PR #26（本検証ではマージもクローズもしていない）
- 既定: 公式訳ではない個人学習用 AI 意訳。正確さより落ちがないこと。agy の結論は使っていない。判定は 2 ファイルの直接照合のみ。

## 判定: 合格

主張: Intermezzo 1 日本語草稿は、差し戻し条件（コードフェンス不一致、Exercise 116–128 欠落、段落・リスト・Figure の省略）を満たさない。合格とする。

根拠:

1. コードフェンス 76 本を Python で抽出（``` 開始から閉じまで、言語タグ含む全文）。順序つき一致。不一致 0。結合 sha256 は EN/JA とも `5ce411a87c168969db86746194925e40fcf80cb2b3555594fe56adf6fa1d2ad1`。フェンスはすべて閉じている。
2. Exercise 116–128 が JA に 13 件すべて存在する（見出しは `練習問題 N (Exercise N)`）。各練習の番号付き項目数は EN と同じ（合計 36 項目）。
3. Figure 39–43 の ASCII 図はフェンス内のため、1 と同一根拠で原本一致。本文側の「図39」～「図43」言及も欠落なし。
4. 目次 10 項、節見出し 10（`##` 本体）＋ Contents、注 11（EN 抽出の重複注を含む）、エラーメッセージ小見出し 5、番号付きリスト 36、`*RUN*` 5 回が JA に対応して残っている。
5. 末尾のエラー表フェンス（Function Applications / Wrong Data / Conditionals / Function Definitions / Structure Type Definitions）も 1 の比較に含まれ、欠落なし。

論拠: 依頼の差し戻し条件はフェンス一字一句と Exercise 欠落が「重大」であり、今回それらは観測されなかった。翻訳の文体・用語の公式性は判定対象外（依頼 4）。

`04-intermezzo1.md` 本文は直していない。

## 検証方法（再現）

対象 2 ファイルを開き、次を機械実行した。

- フェンス: `re.compile(r"```([^\n]*)\n(.*?)```", re.DOTALL)` で 76 対を順序比較。`full` 文字列（言語タグ行含む）の等価。
- Exercise / Figure / 見出し / Note / 番号リスト / `*RUN*` を正規表現で数え、JA 側の行を突合。
- 識別子スポット: `define-struct` 37=37、`check-expect` 3=3、`check-within` 5=5、`check-member-of` 4=4、`check-error` 3=3、`check-random` 4=4、`check-satisfied` 4=4、`check-range` 4=4、`my-divide` 4=4、`checked-area-of-disk` 7=7、`fahrenheit->celsius` 2=2、`AREA-OF-RADIUS` 3=3、`average` 16=16。
- 導入の英語例 `"the cat is round"` / `"the brick is a car"`、相互参照 `Computing with lambda` / `Refining Interpreters` / `Nameless Functions` / `Input Errors` が JA 本文に残っていることを目視。

## 問題リスト（重大度つき）

### 重大（差し戻し）

なし。件数 0。

### 軽微（リストのみ。本文未修正）

1. **練習問題 123 の後段がフェンス前に吸収されている**
   場所: EN L702–713 / JA L512–516。
   EN はフェンス後に独立行 `as a cond expression.` がある。JA は課題文側に「次を `cond` 式に書き換えられることを示す規則を書きなさい。」と折り込み、フェンス直後が `## 定数定義`。課題内容自体は落ちていない。構造差のみ。

2. **番号付き練習のインラインコードに空白を復元している**
   場所: 練習 116–120, 125–127 のリスト。
   EN 抽出は `(=yz)`、`(define-structoops[])` のように空白が潰れている。JA は `(= y z)`、`(define-struct oops [])` のように空白を戻し、バッククォートで囲んでいる。フェンス規則の対象外。省略ではなく可読化。原本 HTML 由来の抽出ノイズに対する修正と見る。

### 観察（問題に数えない）

- JA 先頭 HTML コメントと末尾「免責」は原本にない追加。省略ではない。非公式意訳の明示として妥当。
- EN L923 は `#true if the value is of kind c and #false` で行頭 `#` のため見出し誤認しうる抽出アーティファクト。JA L675 は同一内容を通常段落にまとめている（欠落ではない）。
- EN 文法節の Note「DrRacket ではプログラムは定義領域と対話領域」は L164–166 と L170–172 で重複。JA は L106 と L109 で両方残している。
- ブロック数の見かけ差（EN list 16 / JA list 14、EN para 159 / JA para 156）は、JA が改行で分断されていた箇条書きを 1 リストにまとめたことと、日本語で段落が連結されたことによる。目次 10 項と文法の 3 箇条は両方ある。
- `beta` の英単語出現は EN 4 / JA 2。JA は「ベータ (beta)」「ベータ値 (beta-value)」と訳出しており、概念の落ちではない。

## 節・Exercise・Figure チェック表

| 項目 | EN | JA | 結果 |
|---|---|---|---|
| コードフェンス | 76 | 76、全文一致 | 合格 |
| 目次 | 10 | 10（英語名併記） | 合格 |
| BSL Vocabulary … Error Messages | 10 節 | 10 節（日本語 (English)） | 合格 |
| Figure 39–43 | フェンス内 5 図 | 同一フェンス | 合格 |
| Exercise 116–128 | 13 | 13 | 合格 |
| 番号リスト項目 | 36 | 36 | 合格 |
| Note | 11 | 11 | 合格 |
| エラー小見出し | 5 | 5（英語名併記） | 合格 |

Exercise 対応（JA 行）: 116@125, 117@133, 118@141, 119@149, 120@156, 121@310, 122@318, 123@512, 124@578, 125@691, 126@699, 127@714, 128@802。

## やらなかったこと

- `04-intermezzo1.md` の本文修正（重大な不一致がなかったため）
- マージ、PR クローズ
- 訳文の公式用語チェック、BSL 実行による意味検証（依頼範囲外。落ちの判定が主）

## 問題件数

- 重大: 0
- 軽微: 2
- 合計（リスト掲載）: 2
