# 図表・画像ポリシー（Issue #9）

## ゴール（p0）

訳済本文中の `[image: …]` が、**PDF / EPUB で公式と同じ PNG として見える**こと。  
人手で図ごとにキャプションを書く運用は標準にしない。

## 方針

| 項目 | 決定 |
|------|------|
| 主戦略 | 公式 / docs.racket-lang.org の PNG を **自動取得**して埋め込む |
| 画像の git | **載せない**（`assets/htdp-figures/` は `.gitignore`） |
| 再現 | `python3 tools/htdp_figures.py fetch` |
| プレースホルダ展開 | **ビルド時**（ドラフト SoT は `[image: …]`） |
| コード例 | Racket 本体は改変しない |
| ゲート | `report` → `warn` → `error`（既定 **report**） |

## URL 設定（C1）

| 変数 | 用途 | 既定 |
|------|------|------|
| `HTDP_BOOK_BASE` | 本体 Book の base（末尾 `/` 可） | `https://htdp.org/2026-5-28/Book/` |
| `HTDP_FIGURES_BASE_QUICK` 等 | 付録 manual 別 base | docs.racket-lang.org 各パス |

`download_book.py` も同じ `HTDP_BOOK_BASE` を参照する。

## ゲート（段階運用・F2）

| モード | 意味 | いつ使う |
|--------|------|----------|
| **report**（**既定**） | 一覧を出すだけ。exit 0 | 日常のビルド・開発 |
| **warn** | 画像欠落を警告。exit 0 | 手元で気づきたいとき |
| **error** | 画像欠落で exit 2 | CI やリリース前（opt-in） |

```bash
python3 tools/htdp_figures.py gate --mode report
python3 tools/htdp_figures.py gate --mode warn
python3 tools/htdp_figures.py gate --mode error
FIGURES_GATE=warn ./build_translation.sh
# 互換: FAIL_ON_MISSING_FIGURES=1 は error 相当
```

判定対象:

1. **参照 PNG がディスク上に無いか**（主ゲート）
2. **崩れた ASCII Figure 枠**（`+---` + Figure N）の残件数を report に併記（Part III 相当 07–14）

ドラフトの裸 `[image:` 件数は情報のみ（SoT として残るのが正常）。  
**既定を error にはしない**（ローカル開発が止まるため）。master 取り込み後に CI だけ error を検討。

## ディレクトリ

```
assets/htdp-figures/   # gitignored
  book/ quick/ htdp-langs/ gui/ racket-cheat/
build/
  figures-report.md figures-inventory.md expanded/
```

## コマンド

```bash
python3 tools/htdp_figures.py fetch
python3 tools/htdp_figures.py report
python3 tools/htdp_figures.py gate --mode report
./build_translation.sh
```

## 受け入れ条件（p0）

1. `fetch` 後、参照 `(source, file)` の missing **0**
2. EPUB/PDF で代表 pict（237 / 240 / cat1 等）が見える
3. プログラム例のコード文字列は原文方針を守る

## Figure 86 型（対比 ASCII）— 調査メモ（F3）

| 項目 | 内容 |
|------|------|
| 原因 | Scribble の左右対比 / 文法表 Figure を固定幅 ASCII 1 ボックスに潰したため、セル境界と改行が壊れる |
| 影響例 | 図86–104（Part III）、Intermezzo の図105–110、143–145 等 |
| 実施済み | `tools/fix_ascii_figures.py` が公式 HTML の `RktBlk`（および画像・文法表）から **二重 fence / 読みやすい枠**へ復元。Part III 以降（07–14）で `+---` 崩れ **0** を確認 |
| 本格対処（未着手） | `extract_to_markdown.py` の `figure_to_ascii` を改修し、再抽出時に壊れないようにする。ゴールデンテスト（図88 左右コード一致など）を推奨 |
| やらない | コードを「読みやすく」意訳・トークン改変 |

## やらないこと

- 全 pict を絵文字・推測キャプションだけに置換
- 確認なしの意訳一括置換
- master へ巨大バイナリを無秩序に積む
- Racket 例の中身を改変する

## 引き継ぎ（次の人へ）

1. クローン後: `python3 tools/htdp_figures.py fetch`
2. ビルド: `./build_translation.sh`
3. 成果物: `htdp2e-ja.epub` / `htdp2e-ja.pdf`
4. Drive 配布: ローカル `~/GoogleDrive/`（または指定の googledrive パス）へコピー
5. 版 URL が変わったら `HTDP_BOOK_BASE` を更新
6. ゲートを厳しくするなら CI で `FIGURES_GATE=error` を段階導入
