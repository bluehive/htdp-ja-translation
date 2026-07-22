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
* 本体の再生成: `python3 extract_to_markdown.py`
* 付録の再取得: `python3 download_appendix_docs.py`（目次リンクを同一マニュアル内で再帰）
* 付録の再抽出: `python3 extract_appendix_to_markdown.py`
* 対応表: `extracted/README.md` および `extracted/appendix/README.md`

#### 付録マニュアル一覧

| マニュアル | 元 URL | ローカル原本 |
|-----------|--------|--------------|
| quick | https://docs.racket-lang.org/quick/index.html | `extracted/appendix/quick/` |
| htdp-langs | https://docs.racket-lang.org/htdp-langs/index.html | `extracted/appendix/htdp-langs/` |
| racket-cheat | https://docs.racket-lang.org/racket-cheat/index.html | `extracted/appendix/racket-cheat/` |
| gui | https://docs.racket-lang.org/gui/index.html | `extracted/appendix/gui/` |

## 翻訳手法
本プロジェクトの翻訳は、AI アシスタントを用いて行われています。原文の論理的な構造やプログラムの仕様を完全に崩さず、日本語として読みやすく自然な表現に仕上げています。

## 現在の進捗状況
* **前付け・目次 (00)**: 翻訳完了
* **序文・プロローグ (01-02)**: 翻訳完了
* **第I部 固定サイズのデータ (03)**: 全文翻訳（第1–7章）
* **第II部 (05-part2-*)**: 第8〜13章あり（Issue #3: 第10–13章を原本から補完、第8–9は既存維持）
* **第III部 抽象化 (07)**: 一部章の翻訳あり
* **付録 A Quick (15)**: 翻訳あり
* **付録 B htdp-langs (16–21)**: 翻訳あり（機械支援ドラフト箇所あり）
* **付録 C racket-cheat (22)**: 翻訳あり
* **付録 D gui (23–46)**: 翻訳あり（概要 00–15 は校正済み寄り。クラス参照 39–46 は機械支援ドラフト）

その他の部・章・Intermezzoは、`extracted/original_markdown_**.md` を原本として順次翻訳する。

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
