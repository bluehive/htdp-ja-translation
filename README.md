# 「How to Design Programs, Second Edition」日本語訳（個人学習用）

> **宣言（先に読んでください）**  
> これは **個人の学習のために、AI で英語原文を意訳したもの** です。公式訳ではありません。  
> **正確さはありません。** 用語の揺れ、抜け、誤訳、省略、コード周りの説明の誤りがあり得ます。学習・参照のたたき台以上の用途（引用・授業・公開教材としての信頼）には使わないでください。わからない箇所は必ず [英語原典](https://htdp.org/) に戻ってください。

対象は Matthias Felleisen、Robert Bruce Findler、Matthew Flatt、Shriram Krishnamurthi による *How to Design Programs, Second Edition*（HTDP 2e）です。有志の完成訳プロジェクトではなく、自分用の下書き置き場です。

## 目的
* 自分の学習用に、書籍の日本語ドラフトを置く
* サンプルコード（Racket / BSL / ISL など）は原文のまま残す（学習のため）
* 必要なら PDF / EPUB に結合して読む

## 翻訳の原本（作業メモ）

**翻訳作業の入力は次のファイル群です。**

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
日本語ドラフトは **AI による意訳** です。前後の文脈から読みやすくしただけで、厳密な逐語訳でも校正済みの訳でもありません。上の宣言どおり **正確さはありません**。コードブロックは原文をコピーする方針ですが、抜けや改変が残っている可能性があります。

## 現在のドラフト状況（正確さは保証しない）
* **前付け・目次 (00)**: ドラフトあり
* **序文・プロローグ (01-02)**: ドラフトあり
* **第I部 固定サイズのデータ (03)**: ドラフトあり（穴埋め途中の箇所もあり）
* **第II部 (05-part2-*)**: 第8〜13章のドラフトあり（原文より薄い／欠落あり）
* **第III部 抽象化 (07)**: 一部のみドラフトあり

その他の部・章・Intermezzoは、`extracted/original_markdown_**.md` を入力に順次ドラフトする。いずれも学習用の意訳であり、完了・正確を意味しません。

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
2. **PDF エンジン**: Linux では Typst または XeLaTeX / LibreOffice 経由など。Windows では Typst（`build_translation.ps1` 既定）
3. **日本語フォント**: 例) Noto Serif CJK JP（Linux）、BIZ UDMincho（Windows）

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

* **このリポジトリのコードと日本語ドラフト**: **BSD 2-Clause License**（ルートの `LICENSE`）
* **原著（英文）**: Matthias Felleisen, Robert Bruce Findler, Matthew Flatt, Shriram Krishnamurthi（[CC BY-NC-ND](https://htdp.org/)）。日本語ドラフトは原著の代替ではありません。
