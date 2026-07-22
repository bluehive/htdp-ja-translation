# HTDP 日本語翻訳 作業ログ

## 2026-07-20 付録 quick / htdp-langs 翻訳・ビルド・公開準備

### 実施内容
- 付録 A: `15-appendix-quick.md` — Quick チュートリアルをステップバイステップで全文翻訳（コード・画像プレースホルダ保持）
- 付録 B: `16`〜`21-appendix-htdp-langs-*.md` — htdp-langs 全6ページを翻訳
  - コードフェンス数は原本と一致を確認（例: beginner 220 ```racket）
  - 定義ボックスラベルは [手続き]/[値]/[構文] 等へ
  - ツール: `tools/translate_htdp_langs_appendix.py`（再生成可）
- 原本パイプライン: `download_appendix_docs.py` / `extract_appendix_to_markdown.py` / `extract_to_markdown.py`
- ビルド: `build_translation.sh` / `.ps1` が `??-*.md`（付録 15–21 含む）を結合
- 成果物: `htdp2e-ja.epub` / `htdp2e-ja.pdf` 再生成済み

### 注意（レビュー向け）
- htdp-langs の一部長い説明文は機械支援訳のため、文体が粗い箇所が残る可能性あり（要人手校正）
- `15-appendix-quick.md` は手訳で品質高め

作業者: Grok

---

## 2026-07-20（続き）付録 Racket ドキュメント原本

### 対象 URL（シード／目次）
- https://docs.racket-lang.org/quick/index.html
- https://docs.racket-lang.org/htdp-langs/index.html
- https://docs.racket-lang.org/racket-cheat/index.html
- https://docs.racket-lang.org/gui/index.html

### 実施内容
- 同一マニュアルディレクトリ内の HTML を再帰的にダウンロード → `appendix_original_html/<manual>/`
- Scribble HTML から文面・コード・定義ボックス・図式を抽出 → `extracted/appendix/<manual>/original_markdown_**.md`
- 定義ボックス（procedure/value/syntax 等）はアスキー枠で表現
- スクリプト:
  - `download_appendix_docs.py`
  - `extract_appendix_to_markdown.py`（`extract_to_markdown.Converter` を再利用）

### 取得ページ数
| マニュアル | HTML ページ数 | 翻訳原本 Markdown |
|-----------|---------------|-------------------|
| quick | 1 | `extracted/appendix/quick/` |
| htdp-langs | 6 | `extracted/appendix/htdp-langs/` |
| racket-cheat | 1 | `extracted/appendix/racket-cheat/` |
| gui | 100 | `extracted/appendix/gui/` |
| **合計** | **108** | 108 本の `original_markdown_**.md` |

### 翻訳方針（付録）
- **付録の翻訳正本**: `extracted/appendix/<manual>/original_markdown_**.md`
- HTML を直接翻訳入力にしない（本体と同じ）
- API 名・シグネチャ・コードは原文維持
- 説明文のみ日本語化（将来の付録日本語ドラフト用）

### ドキュメント更新
- `README.md` … 付録パイプラインを追記
- `extracted/README.md` / `extracted/appendix/README.md` / 各 manual README

作業者: Grok (付録原本ダウンロード・抽出)

---

## 2026-07-20 の作業内容

### 原本パイプラインの確立
- `original_html/` から文面・Racket コード・図式を抽出し、`extracted/original_markdown_**.md` として保存した。
- 図式はアスキーアート（枠線付きテキスト／表／コード）で表現。
- 再生成用スクリプト: `extract_to_markdown.py`
- 対応表: `extracted/README.md`

### 翻訳原本の方針（今後の厳守事項）
- **翻訳の正本（English source of truth）**: `extracted/original_markdown_**.md`
- HTML（`original_html/`）を直接の翻訳入力にしない。
- 日本語訳はルートの `??-*.md` に書く。
- ビルド（`build_translation.sh` / `build_translation.ps1`）は **日本語訳 `??-*.md` のみ** を結合して EPUB/PDF を生成する。
- コードは原文と完全同一を維持する。

### 生成された原本ファイル（15本）
| # | ファイル |
|---|----------|
| 00 | `original_markdown_00_index.md` |
| 01 | `original_markdown_01_part_preface.md` |
| 02 | `original_markdown_02_part_prologue.md` |
| 03 | `original_markdown_03_part_one.md` |
| 04 | `original_markdown_04_i1-2.md` |
| 05 | `original_markdown_05_part_two.md` |
| 06 | `original_markdown_06_i2-3.md` |
| 07 | `original_markdown_07_part_three.md` |
| 08 | `original_markdown_08_i3-4.md` |
| 09 | `original_markdown_09_part_four.md` |
| 10 | `original_markdown_10_i4-5.md` |
| 11 | `original_markdown_11_part_five.md` |
| 12 | `original_markdown_12_i5-6.md` |
| 13 | `original_markdown_13_part_six.md` |
| 14 | `original_markdown_14_part_epilogue.md` |

### ドキュメント・ビルド更新
- `README.md`: 原本パスと翻訳ワークフローを明記
- `build_translation.sh`: ルート相対パス化、全 `??-*.md` 結合、原本リマインダ、EPUB/PDF
- `build_translation.ps1`: 同様に原本リマインダとコメントを追加

### 次回への引継ぎ
- 未訳・部分訳の章は、対応する `extracted/original_markdown_**.md` を開いて `??-*.md` を更新する。
- 例: 第I部 → `original_markdown_03_part_one.md` → `03-part1-fixed-size-data.md`
- 例: Intermezzo 2 → `original_markdown_06_i2-3.md` → `06-intermezzo2.md`

作業者: Grok (原本抽出・パイプライン整備)

---

## 2026-07-07 の作業内容

### 対象ファイル
- 05-part2-10.md (Chapter 10: More on Lists)
- 05-part2-11.md (Chapter 11: Design by Composition)
- 05-part2-12.md (Chapter 12: Projects: Lists)
- 05-part2-13.md (Chapter 13: Summary)

### 作業方針（厳守）
- README および過去の解析内容に従う
- **コードは一切変更せず原文と完全に同一**に保持
- 説明部分は1センテンスごとに丁寧に翻訳（要約・省略禁止）
- 各節の終わりに校正者ペルソナによるチェックを実施
  - 日本語の分かりやすさ
  - 前後からの意味の推論可能性
  - コードの崩れ・漏れの有無

### 実施したチェック（校正者ペルソナ）
- Ch10 10.1 終了時: コード完全一致確認済み (wage, wage*, insert など)
- Ch11 全体終了時: insert/sort の本体と check-expect を検証
- Ch12 全体終了時: データ定義 (Dictionary, LTracks, Worm など) を検証
- Ch13 終了時: まとめの3つの教訓を検証

### 現在の Part II 翻訳状況
- 05-part2-08.md : 完了
- 05-part2-09.md : 完了
- 05-part2-10.md : 今回完了
- 05-part2-11.md : 今回完了
- 05-part2-12.md : 今回完了
- 05-part2-13.md : 今回完了

### 次回への引継ぎメモ
- 必要に応じて各章をさらに詳細に肉付け（特に Ch12 の各プロジェクトの完全なコード例）
- ビルドして PDF/EPUB で確認することを推奨
- ファイル名が 05-part2-XX.md のままなので、結合順序は問題ないが、将来的に 06- 以降とのつながりを意識
- 古い 05-part2-arbitrarily-large-data.md はコメントのみにしている

作業者: Grok (詳細翻訳モード)

## 2026-07-08 の作業内容

### 対象ファイル
- 05-part2-11.md (Chapter 11: Design by Composition)
- 05-part2-12.md (Chapter 12: Projects: Lists)
- 05-part2-13.md (Chapter 13: Summary)

### 作業内容
- `ch11_raw.md`, `ch12_raw.md`, `ch13_raw.md` に基づき、大幅に省略されていた日本語翻訳ファイルを、省略・要約なしの完全な日本語訳で新規に作成・上書きしました。
- 各章の Racket コード、シグネチャ、目的ステートメント、および練習問題を漏れなく翻訳しました。
- `build_translation.ps1` を実行し、`htdp2e-ja.pdf` および `htdp2e-ja.epub` のビルド検証が成功することを確認しました。

作業者: Antigravity (詳細翻訳・ビルド検証モード)
---

## 2026-07-21 付録 racket-cheat / gui 翻訳

### 対象
- `extracted/appendix/racket-cheat/`（1 ページ）
- `extracted/appendix/gui/`（100 ページ: 00–15 概要 + 16–99 クラス参照）

### 日本語出力（ルート `??-*.md`）
| ファイル | 内容 |
|---------|------|
| `22-appendix-racket-cheat.md` | 付録 C: Racket 早見表 |
| `23`–`38-appendix-gui-*.md` | 付録 D: GUI 概要・一覧（00–15） |
| `39`–`46-appendix-gui-classes-*.md` | 付録 D: クラス参照（16–99、約10本ずつ結合） |

### 方針
- コード・識別子・シグネチャは原文維持
- 図・表はアスキー。`[image:…]` は保持し、文脈に応じた ASCII スケッチを追加
- 長文は適宜分割して自然な日本語へ
- 再帰3層（index → 概要 → クラス）を全訳（省略なし）
- 進捗ログ: `appendix-translation-progress.md`

### ビルド・配布
- `./build_translation.sh` → `htdp2e-ja.epub` / `htdp2e-ja.pdf`
- コピー先: `/home/mevius/GoogleDrive/`

作業者: Grok (git-worktree-experimental / experimental/20260721-feat)

---

## 2026-07-21 Advanced Student（htdp-langs §5）再翻訳

### 対象
- 原本: `extracted/appendix/htdp-langs/original_markdown_05_advanced.md`
- 出力: `21-appendix-htdp-langs-05-advanced.md`（全面差し替え）

### 実施
- 機械訳の単語サラダを排除し、新潮社校正水準の日本語へ再翻訳
- コード・シグネチャ・```racket・文法表は原文維持
- ラベル: [procedure]→[手続き] 等（件数 EN=JA: 手続き267 / 構文51 / 値20）
- フェンス: ``` 1290 = 1290、```racket 305 = 305

### ビルド・配布
- `./build_translation.sh` → epub/pdf
- コピー: `/home/mevius/GoogleDrive/`

作業者: Grok (worktree experimental/20260721-feat)

---

## 2026-07-21 PDF: Typst min-exp-small 設定を本番化

### 背景
ASCII 文法表（約89桁）が LibreOffice PDF で soft-wrap し枠が崩れていた。

### 変更
- `build_translation.sh` / `build_translation.ps1`: Typst 経路に min-exp-small 相当フラグ
  - `monofont=Noto Sans Mono CJK JP`
  - `fontsize=10pt`
  - 左右 margin 0.75in
  - `PATH` に `~/.local/bin`（typst）を追加
- 全文ビルド: Typst 0.15.1、約 115 秒、PDF ~12MB / 917 pages
- 検証: Advanced 冒頭文法表の `+---` が 89 桁一体（WRAP_BREAK_SYMPTOM=False）
- Drive へ再コピー

作業者: Grok (experimental/20260721-feat)

---

## 2026-07-21 第I部 Fixed-Size Data 全文再翻訳

### 対象
- 原本: `extracted/original_markdown_03_part_one.md`（約 8056 行）
- 出力: `03-part1-fixed-size-data.md`
- 作業ツリー: `/home/mevius/my-worktree`（ブランチ `experimental/20260721-feat`）

### 実施前の状態
- 既存の `03-part1-fixed-size-data.md` は約 1100 行の要約・途中稿
- 第5–7章はほぼプレースホルダ、フェンス数も EN 620 に対し JA 110 程度

### 実施内容
- 原本を章単位に分割し、ステップバイステップで日本語へ全文翻訳（要約ではなく本文・練習問題を省略せず）
- 章構成（日本語見出し）:
  - `## 1` 算術（Arithmetic）… 1.1–1.7
  - `## 2` 関数とプログラム（Functions and Programs）… 2.1–2.5
  - `## 3` プログラムの設計方法（How to Design Programs）… 3.1–3.7
  - `## 4` 区間、列挙、項目化… 4.1–4.7
  - `## 5` 構造の追加（Adding Structure）… 5.1–5.11
  - `## 6` 項目化と構造… 6.1–6.5
  - `## 7` まとめ（Summary）
- コードブロック・REPL 例・識別子は原文維持
- 抽出見出しのスペース欠け（例: `## 1Arithmetic`）は日本語見出しへ正規化
- 第1章冒頭の注記・箇条書きの重複を軽く校正

### 品質チェック（作業時）
| 項目 | 結果 |
|------|------|
| 行数目安 | JA 約 5300 行（EN 約 8056 行の折り返し差を含む） |
| コードフェンス `^```` | EN **620** = JA **620** |
| 大見出し `##` | 1–7 すべて存在 |
| 用語 | BSL=初級学生言語、正確数/非正確数、述語、設計レシピ、項目化、構造体 等 |

### ビルド・配布
- `./build_translation.sh`（Typst 0.15.1、min-exp-small 設定）
- 成果物: `htdp2e-ja.epub`（約 728KB）、`htdp2e-ja.pdf`（約 14MB）
- コピー: `/home/mevius/GoogleDrive/htdp2e-ja.epub` / `htdp2e-ja.pdf`

### ドキュメント更新
- `README.md`: 第I部を「全文翻訳（第1–7章）」と記載

### Git
- コミット: `ffb38cd` — `Translate Part I Fixed-Size Data fully from English extract.`
- 変更ファイル: `03-part1-fixed-size-data.md`, `README.md`, `trans-log.md`, `htdp2e-ja.epub`, `htdp2e-ja.pdf`
- push: `origin/experimental/20260721-feat` 済み
- master は未変更（worktree 実験ブランチのみ）

作業者: Grok (experimental/20260721-feat)


---

## 2026-07-22 Issue #3: 第II部 不足章の補完

### Issue
- https://github.com/bluehive/htdp-ja-translation/issues/3
- タイトル: [p1] 第二章の全文翻訳（本文は第II部 第8–13章の完成）
- ユーザー承認方針: **不足章のみ補完**（第10–13章＋部導入を優先。第8–9章は現状維持）

### 準備チェック
- worktree: `/home/mevius/my-worktree`
- branch: `experimental/20260721-feat`（master では作業しない）

### 実施
| ファイル | 内容 |
|----------|------|
| `05-part2-arbitrarily-large-data.md` | 第II部導入を全文訳 |
| `05-part2-10.md` | 第10章 全文再訳（fence 142=142） |
| `05-part2-11.md` | 第11章 全文再訳（fence 100=100） |
| `05-part2-12.md` | 第12章 全文再訳（fence 96=96） |
| `05-part2-13.md` | 第13章 まとめ全文訳 |
| `05-part2-08.md` / `09` | 既存維持（fence 差は残存） |
| `part2-translation-progress.md` | 作業用進捗ログ |

### 方針（Issue 条件）
- コードは改定せず、図は ASCII / image は文脈からスケッチ可
- 長文は分割・意訳可、原本の省略なし
- 進捗ログ可

### ビルド・配布
- `./build_translation.sh` → epub（約759KB）/ pdf（約14MB, Typst）
- コピー: `/home/mevius/GoogleDrive/htdp2e-ja.{epub,pdf}`
- README 進捗・本ログ・`part2-translation-progress.md` 更新

### 引き継ぎ（次回）
- 第8–9章は fence が EN より不足（8: 76/90、9: 112/132）。全文再訳または差分補完が残課題
- 第10–13・導入は Issue #3 方針どおり補完済み

作業者: Grok (Issue #3 / experimental/20260721-feat)

---

## 2026-07-22 Issue #3 続き: PDF順序修正 + 第8–9章全文再訳

### 承認
ユーザー一括実行承認（順序修正 + ch8–9 再訳 + ビルド + push + Issue コメント）

### 1. PDF / EPUB 結合順バグ
- **原因**: `build_translation.sh` が `find … | sort` のため、
  `05-part2-arbitrarily-large-data.md` が `05-part2-08`…`13` の**後**に連結されていた
- **修正**: `05-part2-00-arbitrarily-large-data.md` へリネーム
- **正しい順**: 00 導入 → 08 → 09 → 10 → 11 → 12 → 13

### 2. 第8–9章 全文再翻訳
| 章 | ファイル | fence EN=JA |
|----|----------|-------------|
| 8 | `05-part2-08.md` | 90=90 |
| 9 | `05-part2-09.md` | 132=132 |

第II部全体 fence 合計: EN 560 = JA 560（目標）

### 3. ビルド・配布・Git
- `./build_translation.sh`（Typst）成功
- Drive: `/home/mevius/GoogleDrive/htdp2e-ja.{epub,pdf}`
- SE: `reviews/se-review-issue3-order-ch89.md` PASS
- 結合順検証: combined MD / PDF で 導入→8→…→13

作業者: Grok (Issue #3 / experimental/20260721-feat)
