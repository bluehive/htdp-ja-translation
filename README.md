# 「How to Design Programs, Second Edition」日本語翻訳プロジェクト

## 目的
- 目次を含め、書籍全体をステップバイステップで日本語に翻訳
- サンプルコード（Racket / BSL）は原文のまま保持
- 完成した翻訳を PDF として生成し、ローカルPCに保存

## 現在の状態（2026-06-25）
- 目次 (TOC) 完全翻訳済み
- 序文 (Preface) 主要部翻訳済み
- プロローグ冒頭部翻訳済み
- 第3章「プログラムの設計方法」核心（設計レシピ）翻訳済み
- 完全版に向けて継続中

生成されたPDF:
- `/home/mevius/ダウンロード/プログラムの設計方法_第二版_日本語訳_partial.pdf`
- ソース: htdp2e-ja.pdf (552KB)

## 翻訳の進め方（ステップバイステップ）
1. `download_book.py` で原典HTMLを一括ダウンロード済み（`original_html/`）
2. 各パート・章ごとに `.md` ファイルを新規作成（コードブロックは原文コピー）
3. `build_translation.sh` または同等のコマンドで md を結合 → ODT → PDF 生成
4. 進捗を追跡しながら全章をカバー

## ツール
- pandoc 3.6.4 (ローカル)
- LibreOffice (soffice) で PDF 変換（日本語フォント Noto Serif CJK JP 等対応済み）

## 注意
- 原典ライセンス: CC BY-NC-ND （個人学習用翻訳として生成）
- 原典: https://htdp.org/2026-5-28/Book/index.html

## 次のステップ例
- Part I の残り章（算術、関数、Worldプログラム）
- Part II リストと自己参照データ
- 以降の全パート

スクリプトを拡張して全自動化も可能。

## 2026-06-25 更新
- **第三章をコードを除いて完全日本語翻訳完了**
  - 3.1 関数の設計（情報とデータ、設計プロセス全6ステップ、例）
  - 3.2 指の運動: 関数（練習問題多数）
  - 3.3 ドメイン知識
  - 3.4 関数からプログラムへ
  - 3.5 テストについて（check-expect）
  - 3.6 World プログラムの設計
  - 3.7 バーチャルペットの世界（演習45〜47など）
- 新PDF生成: 「プログラムの設計方法_第二版_第三章完全日本語訳.pdf」（17ページ）
- すべてのコードブロックは原文のRacket/BSLを厳密に保持

## 2026-06-25 Part III 更新
- https://htdp.org/2026-5-28/Book/part_three.html の **III Abstraction** をすべて日本語翻訳
  - 14 Similarities Everywhere（関数・データ定義の類似性抽象化、contains? 例など）
  - 15 Designing Abstractions
  - 16 Using Abstractions（local, map/filter など）
  - 17 Nameless Functions（lambda）
  - 18 Summary
- 新PDF生成: プログラムの設計方法_第二版_III抽象化_日本語訳.pdf （23ページ）
- すべてのコードは原文のRacket/ISLを厳密保持
- 結合ドキュメント: htdp2e-up-to-part3-ja.pdf

## 2026-06-25 更新（ステップバイステップ版）
- ユーザーの要望により、**完全ステップバイステップ翻訳**を実施中。
- 現在の進捗: 導入 + Chapter 14 (Similarities Everywhere) の主要部分を詳細に翻訳済み。
- PDF: プログラムの設計方法_第二版_III抽象化_日本語訳_進行中.pdf （最新版）
- 計画に従って残りの章（15〜18）を順次追加予定。

抽出ファイル: extracted/part3_full_clean.txt （171k chars）
## 2026-06-25 更新: Chapter 15 & 17 ステップバイステップ翻訳完了
- Chapter 15 "Designing Abstractions" 完全翻訳（15.1 例からの抽象化, 15.2 署名, 15.3 単一制御点, 15.4 テンプレートから）
- Chapter 17 "Nameless Functions" 完全翻訳（lambda 全節）
- PDF更新: プログラムの設計方法_第二版_III抽象化_Ch15_Ch17_更新.pdf （899KB, 23ページ）
- すべてのサンプルコードは原文Racketのまま厳密保持
- ソース: 04-part3-abstraction.md 更新済み
