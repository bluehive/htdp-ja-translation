# 第IV部 Intertwined Data 翻訳進捗（Issue #6）

## 対象

| 項目 | パス |
|------|------|
| 英語原本 | `extracted/original_markdown_09_part_four.md` |
| 日本語 | `09-part4-intertwined-data.md` |
| worktree | `/home/mevius/my-worktree-20260722-figures` |
| ブランチ | `experimental/20260722-figures` |

## 章別状況

| 章 | 内容 | 状態 |
|----|------|------|
| 導入 | IV 絡み合ったデータ | 完了 |
| 19 | S式の詩（木・森・S式・BST 等） | 完了 |
| 20 | 反復的洗練 | 完了 |
| 21 | インタープリタの洗練 | 完了 |
| 22 | プロジェクト：XML | 完了 |
| 23 | 同時処理・DB | 完了 |
| 24 | まとめ | 完了 |

## 検証（機械）

| 指標 | 英語 | 日本語 |
|------|------|--------|
| ```racket ブロック | 163 | 198（図復元で二重 fence 増加） |
| EN racket が JA に完全保持 | — | **163/163（欠落 0）** |
| `[image:` | 19 | 15+（図復元で一部 HTML 画像参照へ） |
| 壊れた `+---` Figure（00–14） | — | **0**（`fix_ascii_figures`） |

## 作業メモ

- スライス: `build/part4_slices/en_*.md` → `ja_*.md` を章別翻訳後結合
- コードフェンスは原文一致を優先。図の ASCII 崩れは Issue #9 ツールで公式 HTML から復元
- 第V・VI部は Issue 指定どおり **未着手（保留）**

## 疑似校正（新潮社校正者ロール）— サマリ

別ファイル: `reviews/se-proof-issue6-part4.md`
