# 図表・画像ポリシー（Issue #9 / experimental figures ブランチ）

## ゴール（p0）

訳済本文中の `[image: …]` プレースホルダが、**PDF / EPUB で公式と同じ PNG として見える**こと。  
人手で図ごとにキャプションを書く運用は標準にしない（数式・グラフの誤記を避ける）。

## 方針

| 項目 | 決定 |
|------|------|
| 主戦略 | 公式 / docs.racket-lang.org の PNG を **自動取得**して埋め込む |
| 画像の git 管理 | **載せない**（`assets/htdp-figures/` は `.gitignore`） |
| 再現手段 | `python3 tools/htdp_figures.py fetch` |
| プレースホルダ展開 | **ビルド時**（ドラフト `??-*.md` の SoT は `[image: …]` のまま） |
| コード例 | Racket コード本体は改変しない。フェンス内のインライン画像だけトークン化または行リフト |
| ゲート | 当面 **report only**（`htdp_figures.py report`） |

## ディレクトリ

```
assets/htdp-figures/          # gitignored
  book/                       # https://htdp.org/…/Book/
  quick/                      # docs.racket-lang.org/quick/
  htdp-langs/
  gui/
  racket-cheat/
build/
  figures-report.md           # fetch 結果
  figures-inventory.md        # report 結果
  expanded/                   # 展開後の一時 MD
```

## コマンド

```bash
# 1) 画像取得（クローン直後・欠落時）
python3 tools/htdp_figures.py fetch

# 2) 棚卸し（欠け・件数）
python3 tools/htdp_figures.py report

# 3) ビルド（内部で expand + resource-path）
./build_translation.sh
```

## 受け入れ条件（p0）

1. `fetch` 後、訳済ドラフトが参照する `(source, file)` の **404 がレポート上ゼロ**（または既知例外リストのみ）
2. ビルドした EPUB/PDF で、少なくとも本文の代表例（`pict_237` / `pict_240` / `cat1` 等）が画像として埋まる
3. プログラム例の **コード文字列は原文のまま**

## やらないこと

- 全 pict を絵文字・推測キャプションだけに置換する
- 確認なしの「意訳」一括置換
- master へ巨大バイナリを無秩序に積む
- コードフェンス内の Racket 構文を「読みやすく」改変する

## 次フェーズ（p0 後）

- 崩れた ASCII 対比 Figure（例: Figure 86）の抽出改善
- report → warn → error の段階ゲート
- 取得元 URL 版（`2026-5-28`）の設定化
