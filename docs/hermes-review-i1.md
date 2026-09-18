# Hermes / 実行エージェント ギャップ分析: Intermezzo 1 (#16 / #25)

- 日時: 2026-09-16（JST）
- 対象 JA: `04-intermezzo1.md`（~7KB・162行・コードフェンス 9）
- 対象 EN: `extracted/original_markdown_04_i1-2.md`（~53KB・1341行・コードフェンス 76）
- ブランチ: `docs/intermezzo1-complete-ja`
- 注: ThinkPad 上の `hermes` / `agy` には本実行環境（sand box）から到達できず。本ファイルは実行エージェントによる独自ギャップ分析（Hermes キックオフ失敗時のフォールバック）。

## 総評

現行 JA は見出し骨格＋要約のみ。EN の約 1/7 の分量。**Exercise 116–128 がすべて欠落**。図（Figure 39–41 等）の ASCII 図もほぼ欠落。Error Messages 節は特に薄い（EN 264行 vs JA 15行）。

## 節ごとの比較（## 見出し）

| # | EN 節 | EN 行数 / フェンス | JA 対応 | JA 行数 / フェンス | 状態 |
|---|-------|-------------------|---------|-------------------|------|
| 0 | Intermezzo 1: Beginning Student Language（導入+Contents） | 48 / 0 | タイトル＋導入段落のみ（Contents なし） | ~8 / 0 | 薄い。Note 欠落。Contents 欠落 |
| 1 | BSL Vocabulary | 36 / 1 | BSL の語彙 | 23 / 0 | Figure 39 全体欠落。語彙定義が要約のみ |
| 2 | BSL Grammar | 209 / 5 | BSL の文法 | 25 / 1 | 文法説明・合法/非合法例・Ex 116–120・Figure 40–41・用語注記が欠落 |
| 3 | BSL Meaning | 163 / 11 | BSL の意味 | 32 / 3 | 代数法則・関数適用・cond ステップ・Ex 121–123 が大幅欠落 |
| 4 | Meaning and Computing | 23 / 0 | 意味とコンピューティング | 4 / 0 | ほぼ1文のみ |
| 5 | BSL Errors | 153 / 11 | BSL のエラー | 6 / 0 | 構文/実行時エラー例・ステップ解説・図が欠落 |
| 6 | Boolean Expressions | 79 / 4 | ブール式 | 18 / 2 | and/or 短絡の詳細・例が不足 |
| 7 | Constant Definitions | 114 / 9 | 定数定義 | 10 / 1 | 定義の意味・展開規則・Ex 124–125 欠落 |
| 8 | Structure Type Definitions | 186 / 11 | 構造型定義 | 8 / 1 | define-struct の意味・セレクタ/述語・例・Ex 126–127 欠落 |
| 9 | BSL Tests | 62 / 2 | BSL のテスト | 12 / 1 | check-* 各種の説明・Ex 128 欠落 |
| 10 | BSL Error Messages | 264 / 22 | BSL のエラーメッセージ | 15 / 0 | メッセージ一覧・例がほぼ全滅 |

## 欠落リスト（具体）

### 導入
- [ ] Contents リスト（10項目）
- [ ] 「Note: Programmers must eventually understand…」ブロック

### BSL Vocabulary
- [ ] Figure 39（BSL core vocabulary）ASCII 図全体
- [ ] primitive / variable / number / Boolean / string / image の正式定義文

### BSL Grammar
- [ ] Figure 40（BSL core grammar）
- [ ] define の可変長引数の説明例（0/1/2 繰り返し）
- [ ] 合法式 `"all"`, `x`, `(f x)` と非合法 `(f define)`, `(cond x)`, `((f 2) 10)` の解説
- [ ] 空白・スタイルに関する段落
- [ ] **Exercise 116–120**（全文）
- [ ] Figure 41（Syntactic naming conventions）
- [ ] Grammatical Terminology 注記（header/body/left-hand side 等）

### BSL Meaning
- [ ] 算術・代数からの法則の段階的展開（多数の `==` ステップ例）
- [ ] 関数定義の意味（置換規則）
- [ ] cond の意味規則（複数ステップ）
- [ ] **Exercise 121–123**

### Meaning and Computing
- [ ] 計算＝代数と同じであることの議論全文

### BSL Errors
- [ ] 構文エラー vs 実行時エラーの例コード多数
- [ ] エラー検出タイミングの説明

### Boolean Expressions
- [ ] and/or の文法・意味（短絡）の正式記述
- [ ] 追加の評価例

### Constant Definitions
- [ ] 定数定義の文法拡張
- [ ] 展開規則と例
- [ ] **Exercise 124–125**

### Structure Type Definitions
- [ ] define-struct の意味（コンストラクタ・セレクタ・述語）
- [ ] 構造体値の扱い
- [ ] **Exercise 126–127**

### BSL Tests
- [ ] check-expect / check-within / check-error / check-member-of / check-range 等の説明
- [ ] **Exercise 128**

### BSL Error Messages
- [ ] エラーメッセージ分類と具体例（EN 最大節）
- [ ] 各メッセージに対応する不正プログラム例

## コードフェンス

| | EN | JA（旧） |
|--|----|----------|
| 合計 | 76 | 9 |

要件: フェンス内は EN と一字一句一致。図の ASCII も EN どおり。

## Exercise 一覧（EN にあり JA になし）

116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128

## agy 依頼向け分割案

`/tmp/htdp-i1-batches/`（または同内容をリポジトリ外に保持）:

1. 導入 + Vocabulary
2. Grammar（大・Ex 含む）→ 必要なら前半/後半
3. Meaning + Meaning and Computing
4. Errors
5. Boolean + Constants
6. Structures
7. Tests
8. Error Messages（大・単独）

## 次アクション

1. 各バッチを日本語意訳（省略なし・コード一致）
2. 統合して `04-intermezzo1.md` を全文置換
3. 検証レポート `docs/hermes-check-i1-draft.md`
4. PR（#16 #25 リンク、マージしない）
