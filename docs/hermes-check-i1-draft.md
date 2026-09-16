# Hermes 独立検証: Intermezzo 1 日本語草稿

- 検証者: ローカル Hermes（本セッション。agy / 他エージェント / 既存 `hermes-check-i1-draft.md` のフォールバック文面は未使用）
- 日時: 2026-09-17 00:19 JST
- ブランチ: `docs/intermezzo1-complete-ja`（`85cbce4` 時点の作業ツリー）
- JA: `04-intermezzo1.md`（1069 行 / 59796 bytes）
- EN: `extracted/original_markdown_04_i1-2.md`（1340 行 / 53229 bytes。ファイル名は i1-2 だが `## Intermezzo` は I1 のみ）
- 方法: フェンス抽出の SHA 照合、見出し・Exercise・Figure・Note・番号付きリストの機械抽出、節ごとの段落数、本文の通読

## 判定

**統合可**

欠落・フェンス不一致・見出し欠落は見つからなかった。下の「残リスク」は統合を止めない。

## 検証結果サマリ

| 項目 | 結果 |
|------|------|
| コードフェンス数 EN / JA | 76 / 76 |
| フェンス本文 + 言語タグ | 完全一致（連結 SHA256 先頭 `27cff5b40b821a07` が双方同一） |
| Exercise 116–128 | 13 題とも本文に存在（番号欠番なし） |
| `##` 見出し | EN 11 / JA 11、1対1対応 |
| `###` | EN `Contents` → JA `目次 (Contents)` のみ |
| Figure 39–43 | 双方フェンス内に同一キャプション |
| blockquote Note | 双方 9（うち DrRacket 定義/対話領域の Note は EN 抽出の重複を JA も保持） |
| 番号付きリスト項目 | 双方 36 |
| `-` リスト項目 | 双方 16 |
| 節ごとの非フェンス段落数 | Boolean が EN 14 / JA 13（後述 Exercise 123）。Error Messages は JA が免責で +2。他は一致 |

## 見出し対応

- EN `## Intermezzo 1: Beginning Student Language` → JA `## Intermezzo 1: Beginning Student Language（初級学生言語）`
- EN `## BSL Vocabulary` → JA `## BSL の語彙 (BSL Vocabulary)`
- EN `## BSL Grammar` → JA `## BSL の文法 (BSL Grammar)`
- EN `## BSL Meaning` → JA `## BSL の意味 (BSL Meaning)`
- EN `## Meaning and Computing` → JA `## 意味とコンピューティング (Meaning and Computing)`
- EN `## BSL Errors` → JA `## BSL のエラー (BSL Errors)`
- EN `## Boolean Expressions` → JA `## ブール式 (Boolean Expressions)`
- EN `## Constant Definitions` → JA `## 定数定義 (Constant Definitions)`
- EN `## Structure Type Definitions` → JA `## 構造型定義 (Structure Type Definitions)`
- EN `## BSL Tests` → JA `## BSL のテスト (BSL Tests)`
- EN `## BSL Error Messages` → JA `## BSL のエラーメッセージ (BSL Error Messages)`

Error Messages の 5 サブ見出し（Function Applications / Wrong Data / Conditionals / Function Definitions / Structure Type Definitions）も対応する日本語＋英語括弧あり。

## 省略チェック

通読した範囲で、EN の導入3段落、Vocabulary 図後の集合説明、Grammar のキーワード説明・合法/非合法例、Meaning の beta / condfalse / condtrue、Computing のステッパー3段落、Errors の stuck / 短絡評価指針 / `error`、Boolean の and/or 短絡と同値、Constants の定義順エラー、Structures のコンストラクタ/セレクタ/述語等式、Tests の RUN 移動説明、Error Messages 導入と 5 区分はいずれも対応段落がある。

Exercise 本文の対応:

| 番号 | EN 行付近 | JA 行付近 | 項目数 |
|------|-----------|-----------|--------|
| 116 | 222 | 125 | 3 |
| 117 | 230 | 133 | 3 |
| 118 | 238 | 141 | 3 |
| 119 | 246 | 149 | 2 |
| 120 | 253 | 156 | 3 |
| 121 | 437 | 310 | 3 |
| 122 | 445 | 318 | 3（定義フェンス＋式3） |
| 123 | 702 | 512 | `if` フェンス |
| 124 | 799 | 578 | プログラム3本 |
| 125 | 941 | 691 | 3 |
| 126 | 950 | 699 | 5 |
| 127 | 967 | 714 | 5 |
| 128 | 1063 | 802 | 失敗テストフェンス |

JA 末尾の免責と先頭 HTML コメントは原本に無い追加であり、省略ではない。

## コード

フェンス 76 個は言語タグ込みで EN とバイト一致。Figure ASCII、評価トレース、Error Messages 表、`check-*` 例を含む。

フェンス外のインライン式は EN 抽出が空白を潰している（例: Grammar 練習 `(=yz)`、`(define(fx)x)`、`(poly35)`）。JA は空白を復元してバッククォートしている（例: `(= y z)`、`(define (f x) x)`、`(poly 3 5)`）。フェンス一致要件の対象外。学習用としては原本 HTML に近い。

## 明らかな誤訳・英語の取り残し

コード以外に、未訳のまま残った英文段落は無い。残っている英語は次のいずれか:

- 見出し・練習番号の英語併記（Issue #25 の推奨形式）
- 書籍内参照名: `Computing with lambda`、`Refining Interpreters`、`Nameless Functions`、`Input Errors`（日本語を併記）
- DrRacket メッセージの引用（「this function is not defined」）とフェンス内 UI 文字列
- 文法断片の blockquote（`definition = ... | (define name expr)` など）

軽微で統合を止めないもの:

- Boolean Expressions: EN “we don’t wish to divide by 0 accidentally” を「たまたま 0 で割りたくない」としている。意図は「誤って 0 除算しない」寄り。
- Exercise 123: EN はフェンス後に “as a cond expression.” と続く。JA は指示文側に「`cond` 式に書き換えられることを示す規則」と前倒ししており、内容は落ちていない（これが Boolean 節の段落数差 14 vs 13）。

## 残リスク

1. Error Messages 表の右列説明はフェンス内のため英語のまま（DrRacket 文言と抽出表を動かさない方針）。表自体は EN 抽出時点で既に省略記号付き。
2. Grammar の DrRacket Note（定義領域と対話領域）は EN 抽出で二重。JA も二重。原本 HTML の重複かどうかは本検証の範囲外。
3. フェンス外練習式の空白復元は EN markdown とは一字一句一致しない。フェンス要件とは別。
4. 公式訳ではなく個人学習用意訳。用語は Part I/II 寄せ（構文・意味論・ステッパ等）。

## 判定（再掲）

**統合可** — フェンス一致、Exercise 116–128 欠落なし、`##` 11 対応、段落カバレッジは Boolean の 123 指示位置以外一致。内容 PR はユーザー承認後の rebase-and-merge 想定。
