# HTDP 日本語翻訳 作業ログ

## 2026-07-22 追加作業 F1/F2/F3（Issue #9 再承認）

### 承認内容（オーナー）
- F1: Part III **以降**の同型 ASCII 対比を棚卸ししてまとめて修正（図88 含む）
- F2a/b/c: ゲート段階運用の文書化、warn 例、ASCII 崩れ report 検出
- F2d/e: しない
- F3: 抽出器本格修正はせず調査メモのみ
- 成果物: 再ビルド・Drive コピー・Issue/PR ログ
- master マージ: まだしない

### 実施
- `tools/fix_ascii_figures.py` 追加（公式 HTML → 二重 fence / 画像注記 / 文法表）
- Part III+（07–14）の壊れた `+---` Figure を復元。**残 0**
- 代表: 図88 `small`/`large`、図89 `inf`/`sup`、図90–104 等
- `htdp_figures.py report` に ASCII 崩れ件数を併記
- README / figures-policy にゲート段階運用と fix ツールを記載

### 引き継ぎ
- 再抽出したら `python3 tools/fix_ascii_figures.py` を再実行（根本は extract 側 follow-up）
- ゲート既定は report のまま

---

## 2026-07-22 次フェーズ（Issue #9 承認チェックリスト実行）

### オーナー承認（チェックリスト要約）

- A1 コピー先: `~/googledrive/` → 実体 `~/GoogleDrive/`
- A2 push / A3 PR **ready** → master
- B1 README 整理 / B2 trans-log 引き継ぎ
- C1 URL 設定化 / C2 ゲート / C3 図86・87 分割（直せる範囲）
- D SE 確認を Issue + PR に記載

### 実施リスト

1. [x] 承認受領コメントを Issue #9 に投稿
2. [x] C1: `HTDP_BOOK_BASE` 等で base URL 設定化（`htdp_figures.py` / `download_book.py`）
3. [x] C2: `gate --mode report|warn|error` と `FIGURES_GATE`（build 連携）
4. [x] C3: `07-part3-abstraction.md` 図86・87 を左右二重 fence 化 + 調査メモ
5. [x] B1/B2: README・figures-policy・本ログの引き継ぎ
6. [x] A1: PDF/EPUB を GoogleDrive へコピー
7. [x] D: SE 観点チェック → Issue / PR
8. [x] A2/A3: push + ready PR

### 引き継ぎチェックリスト（次作業者）

- [ ] クローン後 `python3 tools/htdp_figures.py fetch`（assets は git に無い）
- [ ] `python3 tools/htdp_figures.py gate --mode report` で missing 0 を確認
- [ ] `./build_translation.sh` で EPUB/PDF 再生成
- [ ] 代表画像（pict_237 / pict_240）を PDF または EPUB で目視
- [ ] 図86・87 以外の崩れた ASCII 対比が残っていないか、必要なら同様に分割
- [ ] 抽出器 `figure_to_ascii` の本格修正は別 Issue / 別 PR 推奨
- [ ] `FIGURES_GATE=error` は CI 導入時のみ（ローカル開発の既定は report）
- [ ] master へは **PR 経由**のみ（直 push 禁止方針）

---

## 2026-07-22 図表パイプライン p0（Issue #9 / experimental/20260722-figures）

### 方針（ユーザー承認済み）
- 主戦略: 公式 / docs.racket-lang.org の PNG を **自動取得**して PDF/EPUB に埋め込む
- 画像は **git に載せない**（`assets/htdp-figures/` を gitignore）
- ドラフト `??-*.md` の SoT は `[image: …]` のまま。展開は **ビルド時**
- 人手キャプションは例外のみ。コード例本文は改変しない

### 実施内容
- `tools/htdp_figures.py` 追加
  - `fetch` — 参照 PNG 一括取得（book / quick / htdp-langs / gui）
  - `expand` / `expand-tree` — プレースホルダ → `![](assets/htdp-figures/…)`（フェンス内の画像専用行はリフト）
  - `report` — 欠落棚卸し（report-only ゲート）
- `build_translation.sh` — fetch（任意スキップ可）→ expand → pandoc `--resource-path`
- `figures-policy.md` — 受け入れ条件と禁止事項
- `.gitignore` に `assets/htdp-figures/`
- 初回 fetch: **228 / 228 成功（failed 0）**、約 1.3MB

### 検証
- expand 後の裸 `[image:` は 0
- pandoc EPUB スモークで PNG が `EPUB/media/` に埋め込まれることを確認
- **フルビルド**（`SKIP_FIGURE_FETCH=1 ./build_translation.sh`）成功
  - inventory: present **228** / missing **0** / placeholders **287**
  - EPUB: `htdp2e-ja.epub` 約 1.4MB、埋め込み media **219** PNG
  - PDF: `htdp2e-ja.pdf` 約 17MB（typst 0.15.1）
- コミット: `7ea37c8`（ツール・ポリシー）、成果物は後続コミット

作業場所: worktree `/home/mevius/my-worktree-20260722-figures`（メインリポジトリ未変更）

作業者: Grok

---

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

---

## 2026-07-22 Issue #4: 第III部 抽象化の全文完成

### Issue
- https://github.com/bluehive/htdp-ja-translation/issues/4
- タイトル: [p1] 第三章の翻訳（本文は第III部 Abstraction の完成）
- ユーザー承認: **全文完成（推奨）**

### 準備
- worktree `/home/mevius/my-worktree` / branch `experimental/20260721-feat`

### 実施前
- `07-part3-abstraction.md` 約959行 / fence 122（EN 4201行 / 334）
- 第16章欠落、第17–18章は薄い

### 実施後
- 導入＋第14–18章を原本から全文翻訳して差し替え
- fence **EN 334 = JA 334**
- 進捗: `part3-translation-progress.md`

### ビルド・配布・Git
- `./build_translation.sh`（Typst）: epub ~800KB / pdf ~15MB
- Drive: `/home/mevius/GoogleDrive/htdp2e-ja.{epub,pdf}`
- SE: `reviews/se-review-issue4-part3.md` PASS
- 次回引き継ぎ: Intermezzo 2–5・第IV部以降はプレースホルダのまま

作業者: Grok (Issue #4 / experimental/20260721-feat)

---

## 2026-07-22 全体構成の整理と未訳部の引き継ぎ

### 目的
Intermezzo 2–5 および第IV部以降について、英語原本の中身と日本語側の状態を整理し、README に「本書の構成」として反映した。以下は **進捗** と **次回以降の引き継ぎ**。

### 進捗（本体）

| 区分 | 日本語 | 状態 |
|------|--------|------|
| 00–04 前付け・序・プロローグ・I・I1 | `00`…`04` | **訳了** |
| 第I部（第1–7章） | `03-part1-fixed-size-data.md` | **訳了**（fence 整合） |
| 第II部（第8–13章） | `05-part2-00` + `08`…`13` | **訳了**（導入の結合順も修正済み） |
| 第III部（第14–18章） | `07-part3-abstraction.md` | **訳了**（Issue #4） |
| Intermezzo 2 | `06-intermezzo2.md` | **未訳**（プレースホルダ） |
| Intermezzo 3 | `08-intermezzo3.md` | **未訳** |
| 第IV部 | `09-part4-intertwined-data.md` | **未訳** |
| Intermezzo 4 | `10-intermezzo4.md` | **未訳** |
| 第V部 | `11-part5-generative-recursion.md` | **未訳** |
| Intermezzo 5 | `12-intermezzo5.md` | **未訳** |
| 第VI部 | `13-part6-accumulators.md` | **未訳** |
| エピローグ | `14-epilogue.md` | **未訳** |

付録 A–D はルートに日本語ドラフトあり（gui クラス参照・一部 htdp-langs は品質ドラフト扱い）。

### 未訳部に「何が書いてあるか」（英語原本の要約）

| 単位 | 原本ファイル | 規模の目安 | 内容 |
|------|--------------|------------|------|
| **I2** Quote, Unquote | `original_markdown_06_i2-3.md` | ~526行 / fence~50 | `quote`・準クォート・unquote splice、シンボル。BSL+ 以上 |
| **I3** Scope and Abstraction | `…_08_i3-4.md` | ~908行 / ~66 | スコープ／束縛、`for` ループ、パターンマッチ |
| **IV** Intertwined Data | `…_09_part_four.md` | **~5060行 / ~388** | 第19 S式・木・BST、20 反復的洗練、21 インタープリタ、22 XML、23 2入力・DB、24 まとめ。**未訳最大** |
| **I4** Nature of Numbers | `…_10_i4-5.md` | ~622行 / ~52 | 固定幅数、overflow/underflow、教材言語の数 |
| **V** Generative Recursion | `…_11_part_five.md` | **~3690行 / ~242** | 生成的再帰・停止性、フラクタル、探索、ニュートン／積分、バックトラック |
| **I5** Cost of Computation | `…_12_i5-6.md` | ~634行 / ~36 | 具体時間と抽象時間、オーダー、述語・セレクタのコスト |
| **VI** Accumulators | `…_13_part_six.md` | **~2590行 / ~162** | 文脈喪失、蓄積子の設計、木・エディタ、まとめ |
| **Epilogue** | `…_14_part_epilogue.md` | ~191行 / 0 | 計算・設計の総括と「これから」 |

未訳本体の英語合計: おおよそ **1.4 万行・フェンス約 1000**。

### 引き継ぎ（次にやる人向け）

1. **作業場所**  
   - 推奨: git worktree `/home/mevius/my-worktree`、ブランチ `experimental/…`  
   - メイン `master` を直接壊さない。

2. **翻訳の正本**  
   - 上表の `extracted/original_markdown_*.md` のみ。HTML を直接訳さない。  
   - コード・フェンスは原文維持。図は ASCII／`[image:]` は文脈から絵文字等可（プロジェクト慣例）。

3. **推奨する着手順（負荷の現実）**  
   - **短い橋渡しから:** I2 → I3 → I4 → I5 → エピローグ（学習曲線・分量とも軽い）  
   - **本体の大物:** 第IV部 → 第V部 → 第VI部（分量順でも、IV→V→VI の読順を崩さないならこの順）  
   - 1 Issue = 1 単位（例: Intermezzo 1本、または第IV部1本）にするとレビューしやすい。

4. **ビルド時の注意**  
   - ルート `??-*.md` の **ファイル名ソート** が EPUB/PDF のページ順。  
   - 第II部のように複数ファイルに割る場合は、導入が章の後ろに行かないよう **番号プレフィックス**（例: `09-part4-00-…`）を先に設計する。  
   - PDF は Typst 推奨（`build_translation.sh`）。広い ASCII 表は monofont + 左右 0.75in 設定済み。

5. **完了時の定型**  
   - `README.md` の構成表の「翻訳」列を更新  
   - 本 `trans-log.md` に実施内容を追記  
   - `./build_translation.sh` → 必要なら `/home/mevius/GoogleDrive/` へコピー  
   - commit →（必要なら）SE 確認 → push  
   - 対応 Issue へコメント

6. **README**  
   - 上記の構成・未訳トピックは README「本書の構成」に同期済み。詳細ログは本ファイルを正とする。

作業者: Grok（構成整理・解析のドキュメント化のみ／翻訳実装なし）

---

## 2026-07-22 Issue #5: Intermezzo 2–5 とエピローグの翻訳

### Issue
- https://github.com/bluehive/htdp-ja-translation/issues/5
- タイトル: [p1] Intermezzo 2–5 を翻訳
- ユーザー承認: **一括実行（I2–I5 + エピローグ）**／第IV–VI部は保留

### 準備チェック
- [x] worktree: `/home/mevius/my-worktree`
- [x] branch: `experimental/20260721-feat`

### 実施した翻訳（A）
| 単位 | 出力 | fence |
|------|------|-------|
| Intermezzo 2 Quote, Unquote | `06-intermezzo2.md` | 50=50 |
| Intermezzo 3 Scope and Abstraction | `08-intermezzo3.md` | 66=66 |
| Intermezzo 4 Nature of Numbers | `10-intermezzo4.md` | 52=52 |
| Intermezzo 5 Cost of Computation | `12-intermezzo5.md` | 36=36 |
| エピローグ Moving On | `14-epilogue.md` | 0=0 |
| 進捗ログ | `intermezzo-epilogue-progress.md` | — |

### 今回保留（B）
| 単位 | ファイル | 備考 |
|------|----------|------|
| 第IV部 Intertwined Data | `09-part4-intertwined-data.md` | 未訳・最大分量 |
| 第V部 Generative Recursion | `11-part5-generative-recursion.md` | 未訳 |
| 第VI部 Accumulators | `13-part6-accumulators.md` | 未訳 |

### 進捗・引き継ぎ（リスト）

**今回やったこと**
1. Intermezzo 2–5 全文翻訳（fence 整合）
2. エピローグ全文翻訳
3. `intermezzo-epilogue-progress.md` 作成
4. README 構成表・進捗の一目を更新
5. epub/pdf 再生成（Typst）→ `/home/mevius/GoogleDrive/` へコピー
6. SE: `reviews/se-review-issue5-intermezzo-epilogue.md` PASS
7. commit / push / Issue #5 コメント

**次回やること（保留 B）**
1. 第IV部 Intertwined Data（`09-part4-…` / 原本 `…_09_part_four.md`）— 最大分量
2. 第V部 Generative Recursion（`11-part5-…`）
3. 第VI部 Accumulators（`13-part6-…`）
4. いずれもプレースホルダのまま。1 Issue = 1 部推奨

作業者: Grok (Issue #5 / experimental/20260721-feat)
