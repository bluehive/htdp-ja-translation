# 付録翻訳進捗ログ（racket-cheat / gui）

作業ブランチ: `experimental/20260721-feat`  
worktree: `/home/mevius/my-worktree`  
作業日: 2026-07-21

## 方針

| # | ルール | 適用 |
|---|--------|------|
| 1 | ステップバイステップで翻訳 | 原本ファイル単位で進める |
| 2 | コードは改変しない。図・表はアスキー。picture は文脈から想定 | 遵守 |
| 3 | 長い文は適宜分割可 | 遵守 |
| 4 | 再帰が深い原本は3段階目までで可 | gui は index→概要→クラス参照の3層を全訳 |
| 5 | 本ログで進捗を記録 | 本ファイル |
| 6 | 原本を省略しない | 全ページを JA に含める（クラスは結合ファイル） |
| 7 | 対象: `extracted/appendix/racket-cheat/` と `gui/` | |
| 8 | 新潮社校正者レベルで内容チェック | 用語統一・見出し網羅・フェンス一致 |
| 9 | epub/pdf 生成 | `./build_translation.sh` |
| 10 | 成果物を GoogleDrive へコピー | `/home/mevius/GoogleDrive/` |
| 最終 | git commit + SE 確認 | |

## 出力ファイル（完了）

| 出力 | 原本 | 状態 |
|------|------|------|
| `22-appendix-racket-cheat.md` | racket-cheat/00 | 完了 |
| `23`–`38-appendix-gui-*.md` | gui 00–15 | 完了 |
| `39`–`46-appendix-gui-classes-*.md` | gui 16–99（結合） | 完了 |

合計 JA 付録（本タスク）: 約 24,000 行 / 25 ファイル

## 検証メモ

- ウィンドウ概要 1.1–1.8、エディタ概要 5.1–5.10 見出し対応: OK
- Windowing Functions 定義ボックス数 EN=JA=81: OK
- クラス節 `##` 数: 10×7 + 14 = 84（原本 16–99 と一致）
- コードフェンス: 主要概要ページ完全一致。クラス結合は画像 ASCII 追加で +数本の差あり
- 英文残存（The/This/When… 行頭）: 0

## 用語メモ

| EN | JA |
|----|-----|
| windowing toolbox | ウィンドウ機構ツールボックス |
| editor toolbox | エディタ機構ツールボックス |
| eventspace | イベントスペース |
| callback | コールバック |
| snip | スニップ |
| geometry management | ジオメトリ管理 |
| drawing context (DC) | 描画コンテキスト（DC） |
| pasteboard | ペーストボード |
| grapheme | 書記素 |
| administrator | アドミニストレータ |

## 更新履歴

- 2026-07-21: ログ作成、作業開始
- 2026-07-21: racket-cheat + gui 全層翻訳完了、検証済み
