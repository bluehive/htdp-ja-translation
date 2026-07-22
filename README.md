# 「How to Design Programs, Second Edition」日本語翻訳プロジェクト

本書は Matthias Felleisen、Robert Bruce Findler、Matthew Flatt、Shriram Krishnamurthi による名著『How to Design Programs, Second Edition』(HTDP 2e) を日本語に翻訳する有志プロジェクトです。

## 目的
* 書籍全体（目次、序文、プロローグ、全6部、エピローグ）を日本語に翻訳
* サンプルコード（Racket / BSL / ISL など）は学習のために原文のまま厳密に保持
* 結合した成果物を PDF および EPUB 形式としてビルドし、電子書籍リーダー等で閲覧可能にする

## 翻訳の原本（重要）

**今後の翻訳作業の原本は次のファイル群です。**

### 本体（HTDP 2e）

```
extracted/original_markdown_**.md
```

### 付録（Racket 公式ドキュメント）

```
extracted/appendix/<manual>/original_markdown_**.md
```

| 段階 | パス | 役割 |
|------|------|------|
| 1a | `original_html/*.html` | HtDP 2e 公式 HTML（ダウンロード原資料） |
| 1b | `appendix_original_html/<manual>/*.html` | 付録用 Racket ドキュメント HTML（目次から再帰取得） |
| 2a | **`extracted/original_markdown_**.md`** | **本体の翻訳原本（正本）** |
| 2b | **`extracted/appendix/<manual>/original_markdown_**.md`** | **付録の翻訳原本（正本）** |
| 3 | ルートの `??-*.md`（＋将来の付録日本語ドラフト） | 日本語翻訳ドラフト |
| 4 | `htdp2e-ja.epub` / `htdp2e-ja.pdf` | ビルド成果物 |

* 翻訳するときは **HTML を直接読まず**、`original_markdown_**.md` をソースにする。
* コードブロックは原文と完全一致を保つ。
* 図式・定義ボックスは原本側でアスキーアート化済み。翻訳では枠内の説明文のみ訳し、構造は維持する。
* 対応表: `extracted/README.md` および `extracted/appendix/README.md`

### よく使うコマンド

```bash
# 英語原本の再生成
python3 extract_to_markdown.py
python3 download_appendix_docs.py && python3 extract_appendix_to_markdown.py

# 図・画像（Issue #9）— 詳細は figures-policy.md
python3 tools/htdp_figures.py fetch          # PNG 取得（git 外）
python3 tools/htdp_figures.py report         # 棚卸し
python3 tools/htdp_figures.py gate --mode report   # report|warn|error
./build_translation.sh                       # EPUB/PDF（内部で expand）
```

### 図表・画像（Issue #9）— 要点

| 項目 | 内容 |
|------|------|
| 問題 | `[image: pict_….png]` だけ残り、数式・グラフが見えない |
| 方針 | 公式 PNG を **自動取得**してビルド時に埋め込む（人手キャプションは例外のみ） |
| 置き場 | `assets/htdp-figures/`（**gitignore**。クローン後に `fetch`） |
| ドラフト | ルート `??-*.md` は `[image: …]` のまま（SoT） |
| 版 URL | `HTDP_BOOK_BASE` で上書き可（既定: `https://htdp.org/2026-5-28/Book/`） |
| ゲート | `FIGURES_GATE=report\|warn\|error`（既定 report。ビルドを止めない） |
| ポリシー全文 | [`figures-policy.md`](figures-policy.md) |

```bash
# 例: 画像版パスを変える
export HTDP_BOOK_BASE=https://htdp.org/2026-5-28/Book/
# 例: 欠けを警告だけ見る（ビルドは続行）
FIGURES_GATE=warn ./build_translation.sh
# 例: 欠けたらビルド失敗にしたいときだけ（CI 向き・既定ではない）
FIGURES_GATE=error ./build_translation.sh
# 例: 再ダウンロードを飛ばす
SKIP_FIGURE_FETCH=1 ./build_translation.sh
# 例: 崩れた ASCII 対比図を公式 HTML から復元（Part III+）
python3 tools/fix_ascii_figures.py --report-only
python3 tools/fix_ascii_figures.py
```

**ゲートの段階運用:** 日常は `report`（既定）→ 気づきたいとき `warn` → リリース/CI でだけ `error`。詳細は `figures-policy.md`。

#### 付録マニュアル一覧

| マニュアル | 元 URL | ローカル原本 |
|-----------|--------|--------------|
| quick | https://docs.racket-lang.org/quick/index.html | `extracted/appendix/quick/` |
| htdp-langs | https://docs.racket-lang.org/htdp-langs/index.html | `extracted/appendix/htdp-langs/` |
| racket-cheat | https://docs.racket-lang.org/racket-cheat/index.html | `extracted/appendix/racket-cheat/` |
| gui | https://docs.racket-lang.org/gui/index.html | `extracted/appendix/gui/` |

## 翻訳手法
本プロジェクトの翻訳は、AI アシスタントを用いて行われています。原文の論理的な構造やプログラムの仕様を完全に崩さず、日本語として読みやすく自然な表現に仕上げています。

## 本書の構成（本体 + 付録）

ビルドはルートの `??-*.md` をファイル名ソートで結合する。第II部だけは導入を `05-part2-00-…` にして **導入 → 第8–13章** の順になるよう揃えている。

### 本体（HtDP 2e）

| 区分 | 日本語ファイル | 英語原本 (`extracted/`) | 内容の要約 | 翻訳 |
|------|----------------|-------------------------|------------|------|
| 前付け | `00-toc-and-front.md` | `original_markdown_00_index.md` 等 | 目次・前付け | 完了 |
| 序文 | `01-preface.md` | `…_01_part_preface.md` | 序文 | 完了 |
| プロローグ | `02-prologue.md` | `…_02_part_prologue.md` | プロローグ | 完了 |
| **第I部** Fixed-Size Data | `03-part1-fixed-size-data.md` | `…_03_part_one.md` | 第1–7章：原子データ・関数・設計レシピ・条件・構造体 | **完了** |
| Intermezzo 1 | `04-intermezzo1.md` | （第I部周辺） | BSL の言語ノート | 完了 |
| **第II部** Arbitrarily Large Data | `05-part2-00-arbitrarily-large-data.md` → `05-part2-08`…`13.md` | `…_05_part_two.md` | 第8–13章：リスト・自己参照設計・プロジェクト | **完了** |
| Intermezzo 2 | `06-intermezzo2.md` | `…_06_i2-3.md` | **Quote, Unquote** — `quote` / 準クォート / `,@`、シンボル | **完了**（Issue #5） |
| **第III部** Abstraction | `07-part3-abstraction.md` | `…_07_part_three.md` | 第14–18章：類似性の抽象・ISL 抽象・`local`・`lambda` | **完了** |
| Intermezzo 3 | `08-intermezzo3.md` | `…_08_i3-4.md` | **Scope and Abstraction** — スコープ、`for` ループ、パターンマッチ | **完了**（Issue #5） |
| **第IV部** Intertwined Data | `09-part4-intertwined-data.md` | `…_09_part_four.md` | 第19–24章：S式・木、反復的洗練、インタープリタ、XML、2入力・DB | **未訳**（最大分量） |
| Intermezzo 4 | `10-intermezzo4.md` | `…_10_i4-5.md` | **The Nature of Numbers** — 固定幅数、overflow/underflow、\*SL の数 | **完了**（Issue #5） |
| **第V部** Generative Recursion | `11-part5-generative-recursion.md` | `…_11_part_five.md` | 第25–30章：生成的再帰・アルゴリズム、フラクタル、数値法、バックトラック | **未訳** |
| Intermezzo 5 | `12-intermezzo5.md` | `…_12_i5-6.md` | **The Cost of Computation** — 時間の見積り、オーダー、述語/セレクタ | **完了**（Issue #5） |
| **第VI部** Accumulators | `13-part6-accumulators.md` | `…_13_part_six.md` | 第31–34章：知識の喪失、蓄積子スタイルの設計と応用 | **未訳** |
| エピローグ | `14-epilogue.md` | `…_14_part_epilogue.md` | Moving On — 計算・設計のまとめと次の一歩 | **完了**（Issue #5） |

#### 未訳本体の英語側トピック（詳細）

| 単位 | 英語タイトル | 主な節・トピック |
|------|--------------|------------------|
| I2 | Quote, Unquote | Quote / Quasiquote & Unquote / Unquote Splice |
| I3 | Scope and Abstraction | Scope / ISL for Loops / Pattern Matching |
| IV | Intertwined Data | 19 S-expressions（木・森・BST）· 20 Iterative Refinement · 21 Interpreters · 22 XML · 23 Simultaneous Processing（DB）· 24 Summary |
| I4 | The Nature of Numbers | Fixed-size arithmetic · Overflow · Underflow · \*SL Numbers |
| V | Generative Recursion | 25 Non-standard recursion · 26 Designing algorithms · 27 Fractals / binary search / parsing · 28 Newton / integration / Gaussian · 29 Backtracking · 30 Summary |
| I5 | The Cost of Computation | Concrete vs abstract time · “On the order of” · Predicates & selectors |
| VI | Accumulators | 31 Loss of knowledge · 32 Accumulator-style design · 33 Trees & representations · 34 Summary |
| Epilogue | Moving On | Computing · Program design · Onward（開発者 / 一般読者） |

未訳本体の英語原本は合計おおよそ **1.4 万行・フェンス約 1000**（第IV・V・VI部が大半）。

### 付録（Racket ドキュメント）

| 付録 | ファイル | 内容 | 翻訳 |
|------|----------|------|------|
| A Quick | `15-appendix-quick.md` | 絵で学ぶ Racket 入門 | あり（手訳寄り） |
| B htdp-langs | `16`–`21-appendix-htdp-langs-*.md` | BSL〜ASL 言語リファレンス | あり（一部機械支援ドラフトの名残に注意） |
| C racket-cheat | `22-appendix-racket-cheat.md` | Racket 早見表 | あり |
| D gui | `23`–`46-appendix-gui-*.md` | GUI 概要 + クラス参照 | あり（39–46 クラス参照はドラフト注記あり） |

### 進捗の一目

* **本体・訳了:** 前付け〜第III部、Intermezzo 1–5、エピローグ、付録 A–D  
* **本体・未訳:** 第IV–VI部のみ（プレースホルダ／Issue #5 で保留）  
* 作業ログの詳細: `trans-log.md`

## ディレクトリ構成（抜粋）

```
original_html/                      # HTDP 2e 公式 HTML
appendix_original_html/             # 付録 Racket docs HTML（再帰ダウンロード）
  quick/  htdp-langs/  racket-cheat/  gui/
extract_to_markdown.py              # 本体 HTML → original_markdown
download_appendix_docs.py           # 付録 HTML 再帰ダウンロード
extract_appendix_to_markdown.py     # 付録 HTML → original_markdown
extracted/
  original_markdown_**.md           # 本体・翻訳原本
  appendix/<manual>/original_markdown_**.md  # 付録・翻訳原本
  README.md
??-*.md                             # 日本語訳（ビルド入力）
build_translation.sh / .ps1
```

## ビルド方法

### 必要ツール
1. **Pandoc**: Markdown の結合・EPUB/PDF 生成
2. **PDF エンジン**: **Typst 推奨**（`build_translation.sh` が優先）。未導入時は XeLaTeX → LibreOffice の順。Windows は `build_translation.ps1` 既定が Typst。
   - Typst 時の設定（min-exp-small 相当）: `mainfont=Noto Serif CJK JP` / `monofont=Noto Sans Mono CJK JP` / 左右余白 0.75in — 幅広 ASCII 文法表の折り返し崩れを抑制
3. **日本語フォント**: 本文 Noto Serif CJK JP、コード用 Noto Sans Mono CJK JP（Linux）。Windows は環境に合わせて `mainfont` / monofont を調整

### ビルド実行

**Linux / macOS:**

```bash
./build_translation.sh
```

**Windows (PowerShell):**

```powershell
.\build_translation.ps1
```

実行後、ルートに次が生成されます（環境により PDF エンジンが異なる場合があります）:
* **EPUB**: `htdp2e-ja.epub`
* **PDF**: `htdp2e-ja.pdf`

> ビルド対象はルートの日本語訳 `??-*.md` です。`extracted/original_markdown_**.md` は英語原本であり、EPUB/PDF には直接含めません。

## ライセンス

* **本翻訳プロジェクトコード・翻訳文書**: **MIT License**
* **原著（英文）**: Matthias Felleisen, Robert Bruce Findler, Matthew Flatt, Shriram Krishnamurthi (CC BY-NC-ND)
  * 原典: https://htdp.org/
