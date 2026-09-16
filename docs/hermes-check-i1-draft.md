# Hermes / 実行エージェント 下訳チェック: Intermezzo 1

- 日時: 2026-09-16（JST）
- 対象ドラフト: `/tmp/htdp-i1-drafts/FULL.md` → 統合先 `04-intermezzo1.md`
- EN: `extracted/original_markdown_04_i1-2.md`
- 注: ThinkPad の `hermes`/`agy` 未到達のため、実行エージェントが EN 照合を実施（フォールバック）。

## 検証結果サマリ

| 項目 | 結果 |
|------|------|
| コードフェンス数 EN/JA | 76 / 76 |
| フェンス内容の完全一致 | **YES**（不一致 0） |
| Exercise 116–128 | すべて本文に存在 |
| EN ## 見出し数 / JA ## 見出し数 | 11 / 11 |
| JA サイズ | 41056 bytes / 1070 lines（旧 ~7KB から拡充） |

## 見出し対応

- EN `## Intermezzo 1: Beginning Student Language` → JA `## Intermezzo 1: Beginning Student Language（初級学生言語）`
- EN `## BSL Vocabulary` → JA `## BSL の語彙 (BSL Vocabulary)`
- EN `## BSL Grammar` → JA `## BSL の文法 (BSL Grammar)`
- EN `## BSL Meaning` → JA `## BSL の意味 (BSL Meaning)`
- EN `## Meaning and Computing` → JA `## 意味とコンピューティング (Meaning and Computing)`
- EN `## BSL Errors` → JA `## BSL のエラー (BSL Errors)`
- EN `## Boolean Expressions` → JA `## ブール式 (Boolean Expressions)`
- EN `## Constant Definitions` → JA `## 定数定義 (Constant Definitions)`
- EN `## Structure Type Definitions` → JA `## 構造型定義 (Structure Type Definitions)`
- EN `## BSL Tests` → JA `## BSL のテスト (BSL Tests)`
- EN `## BSL Error Messages` → JA `## BSL のエラーメッセージ (BSL Error Messages)`

## 省略チェック

- Contents: あり
- Figure 39–43 ASCII: フェンス経由で EN と同一
- Note ブロック: 導入・Grammar・Meaning・Computing・Errors・Boolean・Constants に意訳あり
- Error Messages 各サブ節（関数適用 / 誤データ / cond / 関数定義 / 構造型定義）: あり、表フェンス一致

## 残リスク

1. **agy/hermes 未実行**: ローカル再接続後に `hermes -z` で再検証推奨。
2. **練習問題のインライン式**: EN 抽出で空白が潰れている箇所（例: `(=yz)`）は、学習用に空白を復元した表記あり。フェンス外のためコード一致要件外。
3. **Error Messages 表内の英語説明**: DrRacket メッセージと表は EN どおり残置（UI文字列）。周辺散文のみ日本語。
4. **意訳の語感**: 公式訳ではない個人学習用。用語は既存 Part I/II（構文・意味論・ステッパ等）に合わせた。

## 判定

**統合可** — フェンス一致・Exercise 欠落なし・節カバレッジ十分。ユーザーによる内容 PR レビュー後に rebase-and-merge 想定。

