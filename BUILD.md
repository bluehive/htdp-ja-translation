# EPUB / PDF ビルド手順（引き継ぎ用）

個人学習用の AI 意訳ドラフトです。正確さはありません。成果物も同じ前提です。

## いちど決めた体裁（守ること）

1. **入力の順番**（これが目次の順番になる。Pandoc はファイルを足した順で出す）
   - 表紙だけ: `00-toc-and-front.md` の「# 目次」より前
   - 本文: `01`〜`04` → 第II部見出し（スクリプトが1回だけ入れる）→ 章 `05-part2-08`〜`13` → `06`〜`14`
   - そのあと付録: `15`〜`21`（A, B, B-1…B-5）
   - **入れない:** `05-part2-arbitrarily-large-data.md`（第II部の見出しだけ。章の後ろに付くと目次が壊れる）
   - **00 の「# 目次」以降は結合しない。** 手書き目次は原典 HTML 向けリンクで、Pandoc の自動目次とぶつかる
2. **目次**は Pandoc / Typst の自動目次（深さ3）だけを正とする。タイトルは「目次」
   - 結合を `find ??-*.md | sort` にすると、以前のように第II部スタブや 00 の手書き目次が割り込み、付録と本文のページが入れ替わって見える
3. **改ページ**
   - 本文: 章（`#`）と**節（`##`）の直前**で改ページ
   - 付録: **付録ごと**（見出しに「付録」とあるもの。`#` / `##` どちらでも）。付録内部の通常の `##` では切らない
   - 実装: `tools/pagebreak.lua`
4. **フォントは Noto ゴシック**（明朝は使わない）
   - 本文・見出し: `Noto Sans CJK JP`
   - コード: `Noto Sans Mono CJK JP`
5. **結合は原子的に**（一時ファイルへ書いてから置き換え）。二重起動は flock で落とす
6. **成果物**
   - `htdp2e-ja.epub`
   - `htdp2e-ja.pdf`
   - 手元の Google Drive ルートへコピー: `~/GoogleDrive/`（`~/googledrive` と同じ）

## コマンド

リポジトリルートで:

```bash
./build_translation.sh
```

Drive へコピーしないとき:

```bash
./build_translation.sh --no-gdrive
```

## ファイル

| ファイル | 役割 |
|---|---|
| `build_translation.sh` | 結合・EPUB・PDF・Drive コピー |
| `tools/combine_book.py` | 本文→付録の結合順（正本） |
| `tools/pagebreak.lua` | 改ページ |
| `tools/epub.css` | EPUB のゴシック指定 |
| `tools/typst-header.typ` | PDF (Typst) のゴシック指定 |
| `tools/patch_typst.py` | 目次タイトル「目次」とゴシックの再指定 |
| `??-*.md` | 日本語ドラフト（ビルド入力） |
| `extracted/original_markdown_**.md` | 英語原本。EPUB/PDF には入れない |

## エンジン

- Pandoc（あれば `mypublish-books/tools/pandoc-3.6.4/bin/pandoc`）
- PDF は Typst 優先。だめなら XeLaTeX
- どちらも `Noto Sans CJK JP` / `Noto Sans Mono CJK JP`

## やってはいけないこと

- `find ??-*.md \| sort` だけで結合する
- ビルドを同時に2本走らせる
- 付録を本文の前や途中に足す
- 本文フォントを Noto Serif / 明朝に戻す
