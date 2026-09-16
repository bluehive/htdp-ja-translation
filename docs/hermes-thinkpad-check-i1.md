# Intermezzo 1 独立検証（ThinkPad Hermes）

- 日時: 2026-09-17 01:11 JST
- ホスト: `mevius-ThinkPad-X240`
- リポジトリ: `bluehive/htdp-ja-translation`
- ブランチ: `docs/intermezzo1-complete-ja` @ `089b0c69bc77134c669ba37780eca0671548c246`
- JA: `04-intermezzo1.md`（59796 bytes、SHA256 `f35557f93d7901f8c90335a374015f4d8b76e1c2105b7067a264514ec15ef18f`、最終本文コミット `85cbce4`）
- EN: `extracted/original_markdown_04_i1-2.md`（53229 bytes、SHA256 `bd1bfcd3d611ef312e53acef83cdf9e065927ec402ba8ee2a8622ea9a720ed4e`）
- 対象 Issue: #16（翻訳） / #25（作業指示） / PR #26
- 方法: agy / 既存 `docs/hermes-check-*.md` / `docs/agy-check-i1.md` は根拠に使っていない。2ファイルを Python でフェンス・見出し・リスト・Exercise 抽出し、節ごとの段落対応を目視した。
- 判定基準: Issue #25（省略禁止、フェンス一字一句一致、見出し「日本語 (English)」推奨、章・Exercise 番号は原本どおり）

## 主張 / 根拠 / 論拠

主張: 現行草稿は Issue #25 の差し戻し条件（段落・リスト・Exercise の省略、コードフェンス改変）を満たさない。ハードゲートは合格。重大なコード不一致はないため `04-intermezzo1.md` は未修正。push もしていない。

根拠: 下表の機械照合と、節ごとの段落対応（Boolean Expressions の差は Exercise 123 の指示文の位置、Error Messages の差は JA 末尾の免責追加）。

論拠: 公式訳としての用語精度は本報告の判定対象外（README / Issue #25 の個人学習用 AI 意訳）。落ちとフェンス一致を優先する。

## 必須チェック

| 項目 | 判定 | 根拠 |
|---|---|---|
| 省略（節・段落・リスト・Figure・Note・Exercise 116–128） | 合格 | `##` 11/11 対応。リスト 52/52（番号付き 36、箇条書き 16）。Figure 39–43 本文参照あり。`> **注 (Note):**` 10 + 「文法用語についての注」1。Ex 116–128 欠番なし |
| コードフェンス EN 一字一句一致 | 合格 | 76/76。言語タグ込み連結 SHA256 `5ce411a87c168969db86746194925e40fcf80cb2b3555594fe56adf6fa1d2ad1` が JA=EN。不一致 0。言語タグ: `racket` 50 + 空 26 |
| 見出し「日本語 (English)」と章・Exercise 番号 | 合格（章タイトル1件だけ推奨形式と逆） | 節見出し 10 は `日本語 (English)`。章タイトルのみ English 先行。Exercise は `練習問題 N (Exercise N)` で 116–128 |

### 節対応（`##`）

| EN | JA |
|---|---|
| Intermezzo 1: Beginning Student Language | Intermezzo 1: Beginning Student Language（初級学生言語） |
| BSL Vocabulary | BSL の語彙 (BSL Vocabulary) |
| BSL Grammar | BSL の文法 (BSL Grammar) |
| BSL Meaning | BSL の意味 (BSL Meaning) |
| Meaning and Computing | 意味とコンピューティング (Meaning and Computing) |
| BSL Errors | BSL のエラー (BSL Errors) |
| Boolean Expressions | ブール式 (Boolean Expressions) |
| Constant Definitions | 定数定義 (Constant Definitions) |
| Structure Type Definitions | 構造型定義 (Structure Type Definitions) |
| BSL Tests | BSL のテスト (BSL Tests) |
| BSL Error Messages | BSL のエラーメッセージ (BSL Error Messages) |

空行分割の段落数は Boolean 以外ほぼ一致（JA 18 / EN 19 と Error Messages JA 43 / EN 41）。後者は JA 末尾の `---` と免責の追加。前者は次節。

## 問題リスト

重大度: 重大 = 差し戻し（省略またはフェンス不一致） / 中 = マージ前に直したいが落ちではない / 軽微 = 任意 / 情報 = 落ちではない観測。

| ID | 重大度 | 修正要否 | 場所 | 問題 |
|---|---|---|---|---|
| P1 | 軽微 | 任意 | L4 章タイトル | 推奨形式は「日本語 (English)」。現行は `## Intermezzo 1: Beginning Student Language（初級学生言語）`（English 先行・全角括弧）。節見出しは推奨形式 |
| P2 | 軽微 | 任意 | 練習問題 123 | EN はフェンス後に独立文 `as a cond expression.`。JA はフェンス前の「次を `cond` 式に書き換えられることを示す規則を書きなさい。」に吸収。課題内容は落ちていない。構造を揃えるならフェンス後に一文を残す |
| P3 | 軽微 | 任意 | 導入 L19, L21 | EN `Fixed-Size Data` を「第I部「固定サイズのデータ」」とした。同ファイル内の `入力エラー (Input Errors)` / `無名関数 (Nameless Functions)` / `lambda を使った計算 (Computing with lambda)` は英語併記あり。導入だけ英語が無い |
| P4 | 軽微 | 任意 | ブール式 L484 | EN `pragmatics` → JA `語用論` のみ。syntax/semantics は初出で英語併記している |
| I1 | 情報 | 不要 | L1066–1068 | JA のみ `---` と免責。省略ではなく追加 |
| I2 | 情報 | 不要 | フェンス外の番号付き式 | EN 抽出は空白が潰れている（例: `(=yz)`）。JA は `(= y z)` に復元。フェンス内は EN どおり空白維持 |
| I3 | 情報 | 不要 | Grammar の DrRacket Note | EN 抽出が同一 Note を二重に持つ。JA も二重のまま。省略ではない |

プレースホルダ（TODO / FIXME / 未訳 / `[訳`）: 0。

## 総合

- ハードゲート: 合格
- 総合: 合格（軽微4は任意。本文は直していない）
- `04-intermezzo1.md` の修正: なし（重大なコード不一致なし）
- git commit / push: 本報告ファイル以外は触っていない。push なし
- マージ: しない（ユーザー承認待ち、rebase-and-merge）

## 検証コマンド（再実行用）

Python 3 で JA/EN を読み、` ``` ` フェンス 76 本の言語タグ＋本文を逐次比較。Exercise は `**Exercise N.` と `**練習問題 N (Exercise N).` で 116–128 を抽出。リストはフェンス除去後の `^[-*]|\d+\.`。
