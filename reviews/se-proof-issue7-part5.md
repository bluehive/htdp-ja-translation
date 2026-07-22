# 疑似校正メモ（Issue #7 / 第V部）

役割: 新潮社校正者ロール + 熟練 SE 処理確認  
対象: `11-part5-generative-recursion.md`  
日付: 2026-07-22

## Issue #7 条件チェック

| # | 条件 | 判定 |
|---|------|------|
| 準備 | figures worktree + experimental/20260722-figures | OK |
| 1–2 | ステップ翻訳・コード原文・省略なし | OK（racket 91/91） |
| 2b | 図 ASCII / image PNG | OK（fix_ascii_figures + #9 パイプライン） |
| 3–4 | 長文分割・意訳 / 深い再帰の説明 | OK |
| 5–6 | 進捗ログ・省略なし | OK |
| 7 | 対象 A のみ（VI 保留） | OK |
| 8 | 本メモで疑似校正 | OK |
| 9–10 | EPUB/PDF・Drive | 後続工程 |

## SE 処理確認

- [x] master 直編集なし  
- [x] コード改変なし（機械照合）  
- [x] 画像は gitignore 方針  
- [x] 見出し `# V`（H1）で TOC 階層を維持  
- [x] バッチ翻訳（25–26 / 27 / 28 / 29–30）  

## 残リスク

- 第28–29章の数式・図の人間通読推奨  
- 再抽出後は `fix_ascii_figures.py` 再実行  

## 結論

**Issue #7 翻訳条件は機械チェック上クリア。** push 可。
