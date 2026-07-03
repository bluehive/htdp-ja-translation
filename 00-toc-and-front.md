# プログラムの設計方法 第二版

**How to Design Programs, Second Edition**

著者: Matthias Felleisen, Robert Bruce Findler, Matthew Flatt, Shriram Krishnamurthi

© 2014 (更新版 2026) MIT Press  
この資料は著作権保護されており、Creative Commons [CC BY-NC-ND](http://creativecommons.org/licenses/by-nc-nd/2.0/legalcode) ライセンスの下で提供されています。

---

# 目次

## 前付け

- [序文 (Preface)](part_preface.html)
  - 体系的なプログラム設計
  - DrRacket とティーチング言語
  - 移行可能なスキル
  - この本とその各部
  - 違い点
- [プロローグ: プログラムの仕方 (Prologue: How to Program)](part_prologue.html)
  - 算術と算術
  - 入力と出力
  - 計算のさまざまな方法
  - 1つのプログラム、多くの定義
  - もう1つの定義
  - あなたはもうプログラマだ
  - 違う！

## 本編

**I 固定サイズのデータ (Fixed-Size Data)**

- [1 算術](part_one.html#ch~3abasic-arithmetic)
  - 1.1 数の算術
  - 1.2 文字列の算術
  - 1.3 混ぜ合わせ
  - 1.4 画像の算術
  - 1.5 ブール値の算術
  - 1.6 ブール値と混ぜ合わせ
  - 1.7 述語: 自分のデータを知れ
- [2 関数とプログラム](part_one.html#ch~3afuncs-progs)
  - 2.1 関数
  - 2.2 計算
  - 2.3 関数の合成
  - 2.4 グローバル定数
  - 2.5 プログラム
- [3 プログラムの設計方法 (How to Design Programs)](part_one.html#ch~3ahtdp)
  - 3.1 関数の設計
  - 3.2 指の運動: 関数
  - 3.3 ドメイン知識
  - 3.4 関数からプログラムへ
  - 3.5 テストについて
  - 3.6 World プログラムの設計
  - 3.7 バーチャルペットの世界
- [4 区間、列挙、項目化 (Intervals, Enumerations, and Itemizations)](part_one.html#ch~3aintervals-enums)
  - 4.1 条件式を使ったプログラミング
  - 4.2 条件付き計算
  - 4.3 列挙
  - 4.4 区間
  - 4.5 項目化
  - 4.6 項目化を使った設計
  - 4.7 有限状態の世界
- [5 構造の追加 (Adding Structure)](part_one.html#ch~3astructure)
  - 5.1 位置から posn 構造へ
  - 5.2 posn を使った計算
  - 5.3 posn を使ったプログラミング
  - 5.4 構造型定義
  - 5.5 構造を使った計算
  - 5.6 構造を使ったプログラミング
  - 5.7 データの宇宙
  - 5.8 構造を使った設計
  - 5.9 World の中の構造
  - 5.10 グラフィカルエディタ
  - 5.11 さらに多くのバーチャルペット
- [6 項目化と構造 (Itemizations and Structures)](part_one.html#ch~3amix)
  - 6.1 再び、項目化を使った設計
  - 6.2 World を混ぜる
  - 6.3 入力エラー
  - 6.4 World の検査
  - 6.5 等価述語
- [7 まとめ](part_one.html#ch~3asummary1)

**Intermezzo 1: Beginning Student Language**  
[BSL の語彙、文法、意味、エラーなど](i1-2.html)

**II 任意サイズのデータ (Arbitrarily Large Data)**

- [8 リスト (Lists)](part_two.html#ch~3alists1)
- [9 自己参照データ定義を使った設計](part_two.html#ch~3adesign-lists)
- [10 リストの続き](part_two.html#ch~3alists2)
- [11 合成による設計 (Design by Composition)](part_two.html#ch~3alist-sort)
- [12 プロジェクト: リスト](part_two.html#ch~3aproj-lists)
  - 実世界データ: 辞書、iTunes
  - 単語ゲーム、ワーム、単純テトリス、完全宇宙戦争、有限状態機械
- [13 まとめ](part_two.html#ch~3asummary2)

**Intermezzo 2: Quote, Unquote**

**III 抽象化 (Abstraction)**

- [14 どこにでも類似点がある](part_three.html#ch~3add-similarities)
- [15 抽象化の設計](part_three.html#ch~3aabstract)
- [16 抽象化の使用](part_three.html#ch~3a3use)
- [17 無名関数 (Nameless Functions / lambda)](part_three.html#ch~3a3lambda)
- [18 まとめ](part_three.html#ch~3asummary3)

**Intermezzo 3: Scope and Abstraction**

**IV 絡み合ったデータ (Intertwined Data)**

- [19 S 式の詩 (The Poetry of S-expressions)](part_four.html#ch~3apoetry-sexp)
- [20 反復的洗練 (Iterative Refinement)](part_four.html#ch~3afiles)
- [21 インタプリタの洗練](part_four.html#ch~3aevaluator)
- [22 プロジェクト: XML の商業](part_four.html#ch~3amoney-sexp)
- [23 同時処理](part_four.html#ch~3asimu)
- [24 まとめ](part_four.html#ch~3asummary4)

**Intermezzo 4: The Nature of Numbers**

**V 生成的再帰 (Generative Recursion)**

- [25 非標準の再帰](part_five.html#ch~3astrange-recursions)
- [26 アルゴリズムの設計](part_five.html#ch~3adesign-algo)
- [27 バリエーション](part_five.html#ch~3agen-rec-samples)
- [28 数学的な例](part_five.html#ch~3agen-rec-math)
- [29 バックトラックするアルゴリズム](part_five.html#ch~3abacktrack)
- [30 まとめ](part_five.html#ch~3asummary5)

**Intermezzo 5: The Cost of Computation**

**VI 蓄積子 (Accumulators)**

- [31 知識の喪失](part_six.html#ch~3aaccumulator-samples)
- [32 蓄積子スタイル関数の設計](part_six.html#sec~3adesign-accu)
- [33 蓄積のさらなる使用](part_six.html#ch~3amore-accu)
- [34 まとめ](part_six.html#ch~3asummary6)

**エピローグ: 先へ進む (Epilogue: Moving On)**

---

*注意: 本翻訳は学習・個人利用のためのものです。サンプルコードは原文のまま保持しています。*

*原典: https://htdp.org/2026-5-28/Book/index.html*
