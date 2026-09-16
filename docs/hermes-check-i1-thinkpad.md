# Intermezzo 1 独立検証（ThinkPad / ローカル Hermes）

- 日時: 2026-09-17 02:31 JST
- ホスト: `mevius-ThinkPad-X240`
- 報告者: Hermes (grok-4.6 / xai-oauth)
- 作業ディレクトリ: `/home/mevius/my-project/htdp-ja-translation`
- ブランチ: `docs/intermezzo1-complete-ja`（HEAD `bb610131151f3942d01a842265a10813fee3aa54` = `origin/docs/intermezzo1-complete-ja`）
- JA: `04-intermezzo1.md`（sha256 `858e64c8a22e982b6aab3fa18d8ddbc3a26dc5b4a86340aa38b8186d52015193`、1069 行 / 59795 バイト）
- EN: `extracted/original_markdown_04_i1-2.md`（sha256 `bd1bfcd3d611ef312e53acef83cdf9e065927ec402ba8ee2a8622ea9a720ed4e`、1340 行 / 53229 バイト）
- 関連: GitHub #16 / #25 / PR #26
- 既定: 公式訳ではない個人学習用 AI 意訳。agy 下訳・既存 `docs/hermes-check-*.md` は根拠にしていない。判定は 2 ファイルの直接照合。本文は直していない。マージもしていない。

## 主張 / 根拠 / 論拠

主張: 現行の統合草稿は、Issue #25 の差し戻し条件（段落・リスト・Exercise の省略、コードフェンス改変）を満たさない。ハードゲートは合格。明らかな誤訳として以前指摘されていた accidentally（「たまたま 0 で割りたくない」）は HEAD `bb61013` で直済み。残るのは構造差と任意の用語・語感のみ。

根拠:

1. コードフェンス 76 本を Python で抽出（`` ```lang\\n...``` ``、DOTALL）。順序つき全文比較。不一致 0。言語タグ `racket` 50 + 空 26。フェンスはすべて閉じている（生 `` ``` `` は EN/JA とも 152）。結合 sha256（各フェンスの ` ```lang\\nbody``` ` を連結）は EN/JA とも `5ce411a87c168969db86746194925e40fcf80cb2b3555594fe56adf6fa1d2ad1`。
2. Exercise 116–128 が JA に 13 件すべてある（見出し `練習問題 N (Exercise N)`）。番号付きリスト項目は EN 36 / JA 36（内訳 1×11, 2×11, 3×10, 4×2, 5×2）。
3. `##` 節 11/11。目次 `-` 10/10。フェンス除去後の `-` 16/16。Figure 39–43 はフェンス内のため 1 と同一根拠で原本一致。本文の「図39」～「図43」言及も欠落なし。`*RUN*` 5/5。エラー小見出し 5 は英語名併記で残っている。
4. 空行分割の段落数は Boolean 以外一致。Boolean は EN 18 / JA 17（練習問題 123 のフェンス後独立文を課題文へ吸収。課題内容は落ちていない）。Error Messages は EN 40 / JA 42（JA 末尾の `---` と免責は追加であり省略ではない）。
5. accidentally の現行文は JA L491「誤って 0 で割らないためです。」（EN L667–668 “we don’t wish to divide by 0 accidentally”）。

論拠: 依頼の重大条件はフェンス一字一句と Exercise/段落/リストの落ち。今回それらは観測されなかった。公式用語の精度は README / #25 どおり判定対象外。agy の結論は使っていない。

`04-intermezzo1.md` 本文は直していない。

## 検証方法（再現）

対象 2 ファイルを開き、次を機械実行したうえで節を通読した。

- フェンス: `re.compile(r"```([^\\n]*)\\n(.*?)```", re.DOTALL)` で 76 対を順序比較。`full` 文字列（言語タグ行含む）の等価。
- Exercise / Figure / 見出し / Note / 番号リスト / `*RUN*` を正規表現で数え、JA 側の行を突合。
- 識別子スポット（フェンス内外の合計）: `define-struct` 37=37、`check-expect` 3=3、`check-within` 5=5、`check-member-of` 4=4、`check-error` 3=3、`check-random` 4=4、`check-satisfied` 4=4、`check-range` 4=4、`my-divide` 4=4、`checked-area-of-disk` 7=7、`fahrenheit->celsius` 2=2、`AREA-OF-RADIUS` 3=3、`average` 16=16。
- 導入の英語例 `"the cat is round"` / `"the brick is a car"`、相互参照 `Computing with lambda` / `Refining Interpreters` / `Nameless Functions` / `Input Errors` が JA 本文に残っていることを目視。
- 通読した論点: 導入 3 段落、Vocabulary、Grammar のキーワード／合法例／非合法例、Meaning の beta / condfalse / condtrue、Computing のステッパー 3 段落、Errors の stuck / 最左最外指針 / `error`、Boolean の and/or 短絡と同値、Constants の定義順エラー、Structures の constructor/selector/predicate、Tests の RUN 移動、Error Messages 導入と 5 区分。

## 1. 省略（段落・リスト・Exercise 116–128）

判定: **合格。落ちなし。**

| 項目 | EN | JA | 結果 |
|---|---|---|---|
| コードフェンス | 76 | 76、全文一致 | 合格 |
| 目次 | 10 | 10（英語名併記） | 合格 |
| BSL Vocabulary … Error Messages | 10 節 + 章タイトル | 10 節（日本語 (English)）+ 章タイトル | 合格 |
| Figure 39–43 | フェンス内 5 図 | 同一フェンス | 合格 |
| Exercise 116–128 | 13 | 13 | 合格 |
| 番号リスト項目 | 36 | 36 | 合格 |
| 箇条書き `-`（フェンス除去後） | 16 | 16 | 合格 |
| Note（blockquote および文法用語注） | 導入1 + Grammar 重複含む + Meaning/Computing/Errors/Boolean/Constants | 対応して残存 | 合格 |
| エラー小見出し | 5 | 5（英語名併記） | 合格 |
| `*RUN*` | 5 | 5 | 合格 |

Exercise 対応（JA 行）: 116@125, 117@133, 118@141, 119@149, 120@156, 121@310, 122@318, 123@512, 124@578, 125@691, 126@699, 127@714, 128@802。

各練習の項目:

| N | EN | JA | 項目 |
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

Grammar の DrRacket Note（定義領域／対話領域）は EN 抽出が L164–166 と L170–172 で二重。JA も L106 と L109 で二重のまま。省略ではない。

プレースホルダ（TODO / FIXME / TBD / XXX / 未訳 / `[訳` / agy）: 0。

## 2. コードフェンス（原本一致）

判定: **合格。不一致箇所なし（0 件）。**

列挙すべき差分はない。76 対すべて言語タグ＋本文が EN と同一。

必須ルールの対象はフェンス内のみ。フェンス外の番号付き式は EN 抽出で空白が潰れている（例: `(=yz)`、`(define(fx)x)`、`(define-structoops[])`）。JA は `(= y z)` のように空白を戻しバッククォートで囲んでいる。省略ではなく可読化。フェンスには触っていない。

Error Messages 表の右列説明は英語のまま。フェンス一致規則のため翻訳禁止。EN 抽出時点で既に省略記号付き。

## 3. 誤訳・用語ゆれ

重大度: 重大 = 差し戻し（省略またはフェンス不一致） / 中 = 意味の歪みでマージ前に直したいが落ちではない / 軽微 = 任意 / 情報 = 落ちではない観測。

### 重大（差し戻し）

なし。件数 0。

### 中

なし。件数 0。

HEAD `bb61013` で直ったもの（現行では問題に数えない）:

- JA L491 / EN L667–668: “divide by 0 accidentally” を「誤って 0 で割らないためです。」に修正済み。同コミットで「BSL で定義された関数」「語用論 (pragmatics)」も入っている。

### 軽微（リストのみ。本文未修正）

1. **練習問題 123 の後段がフェンス前に吸収されている**
   場所: EN L702–713 / JA L512–516。
   EN はフェンス後に独立行 `as a cond expression.` がある。JA は課題文側に「次を `cond` 式に書き換えられることを示す規則を書きなさい。」と折り込み、フェンス直後が `## 定数定義`。課題内容自体は落ちていない。構造差のみ。

2. **「in another way」→「別の意味で」**
   場所: JA L512 / EN L702–703。
   EN は “surprised you in another way”（別の点で／別の仕方で）。「意味」に寄せると cond の meaning 節と紛らわしい。任意: 「別の点で」。

3. **「proper expression」→「きちんとした式」**
   場所: JA L536 / EN L743。
   リテラルでない計算式の意。任意: 「通常の式」または「リテラルでない式」。

4. **章タイトルが推奨形式と逆**
   場所: JA L4。
   推奨は「日本語 (English)」。現行は `## Intermezzo 1: Beginning Student Language（初級学生言語）`（English 先行・全角括弧）。節見出し 10 は推奨形式。

5. **導入の `Fixed-Size Data` に英語核がない**
   場所: JA L19, L21。
   「第I部「固定サイズのデータ」」とした。同ファイル内の `入力エラー (Input Errors)` / `無名関数 (Nameless Functions)` / `lambda を使った計算 (Computing with lambda)` は英語併記あり。

6. **番号付き練習のインラインコードに空白を復元している**
   場所: 練習 116–120, 125–127 のリスト。
   フェンス規則の対象外。学習用としては原本 HTML に近い。変更しないことを推奨。

### 観察（問題に数えない）

- JA 先頭 HTML コメントと末尾「免責」は原本にない追加。省略ではない。
- EN L923 は `#true if the value is of kind c and #false` で行頭 `#` のため見出し誤認しうる抽出アーティファクト。JA L675 は同一内容を通常段落にまとめている。
- `beta` の英単語出現は EN 4 / JA 2。JA は「ベータ (beta)」「ベータ値 (beta-value)」と訳出。概念の落ちではない。
- 用語は既存稿と概ね揃っている: `対話領域`（prologue / part2 と同じ。`やり取り領域` は 0）、`ステッパー`（`ステッパ` 単独は 0）、`チェック付きバージョン`（part1 の `チェック付きバージョン` と一致。`検査付き` は 0）。
- `構文`（syntax 名詞・構文エラー）と `統語的`（syntactically legal / syntactic category の「統語範疇」）の使い分けがある。ゆれというより対応訳。`署名` / `シグネチャ` はこの章では未使用（原本にも signature なし）。
- 残っている英語は未訳段落ではない: 見出し・練習番号の併記、書籍内参照、DrRacket 引用 `"this function is not defined"`、文法 blockquote、英語の例文、フェンス内。

## 総合

- ハードゲート: **合格**
- 総合: **合格**（軽微は任意。本文は直していない）
- `04-intermezzo1.md` の修正: なし
- git commit / push / マージ: しない（ユーザー承認待ち、rebase-and-merge）

## やらなかったこと

- 本文修正
- マージ、PR クローズ、PR へのレビュー投稿
- 公式用語としての全面 copystyle チェック、BSL 実行による意味検証（落ちの判定が主）
- agy 下訳の再読

## 問題件数

- 重大: 0
- 中: 0
- 軽微: 6
- 合計（リスト掲載）: 6
