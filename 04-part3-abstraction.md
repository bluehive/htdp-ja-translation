# III 抽象化 (Abstraction)

## 導入：抽象化の必要性

多くのデータ定義と関数定義は似ています。例えば、Stringのリストの定義はNumberのリストの定義と、データクラスの名前と「String」「Number」という単語の2箇所しか異なりません。同様に、Stringのリストから特定の文字列を探す関数は、Numberのリストから特定の数を探す関数とほとんど区別がつきません。

経験から、このような類似性は問題を引き起こすことがわかっています。類似性は、プログラマがコードを（物理的または精神的に）コピーすることから生じます。プログラマが別の問題に直面したとき、既存の解決策をコピーして新しい問題に合わせて修正します。この行動は「本物の」プログラミングだけでなく、スプレッドシートや数学的モデリングの世界でも見られます。

しかし、コードのコピーは以下のような問題を引き起こします：
- ミスのコピー
- 同じ修正を多くのコピーに適用する必要性
- 基礎データ定義が変更されたときにすべてのコピーを探して修正するコスト

このプロセスは高価でエラーが発生しやすく、プログラミングチームに不必要なコストを課します。

良いプログラマは、プログラミング言語が許す限り類似性を排除しようとします。

> 「プログラムはエッセイのようなものです。最初のバージョンは下書きであり、下書きには編集が必要です。」

「排除する」とは、プログラマがプログラムの最初のドラフトを書き留め、類似性（および他の問題）を見つけ、それらを取り除くことを意味します。最後のステップでは、**抽象化**を行うか、既存の（抽象化された）関数を使用します。このプロセスを何度か繰り返すことで、プログラムを満足のいく形にすることがよくあります。

このパートの前半では、関数とデータ定義の類似性を抽象化する方法を示します。プログラマはこのプロセスの結果も「抽象化」と呼びます。後半は、既存の抽象化の使用と、このプロセスを容易にする新しい言語要素についてです。このパートの例はリストの領域から取られていますが、考え方は普遍的に適用可能です。

## 14 類似性はどこにでもある (Similarities Everywhere)

Arbitrarily Large Data の演習（の一部）を解いた人は、多くの解決策が似ていることを知っているでしょう。実際、類似性は、ある問題の解決策をコピーして次の問題の解決策を作成する誘惑に駆られるかもしれません。

しかし、**thou shall not steal code**（コードを盗んではならない）、たとえ自分のコードであってもです。代わりに、類似したコード片を**抽象化**しなければなりません。この章では、その抽象化の方法を教えます。

私たちの手段は「Intermediate Student Language」（ISL）に特有のものです。

DrRacket で、「Language」メニューの「How to Design Programs」サブメニューから「Intermediate Student」を選択してください。

ほとんどすべての他のプログラミング言語も同様の手段を提供しています。オブジェクト指向言語では、追加の抽象化メカニズムが見つかるかもしれません。いずれにせよ、これらのメカニズムは本章で述べる基本的な特性を共有しており、ここで説明する設計の考え方は他の文脈でも適用されます。

### 14.1 関数における類似性 (Similarities in Functions)

設計レシピは、関数の基本的な組織を決定します。なぜなら、テンプレートは関数の目的に関係なくデータ定義から作成されるからです。したがって、同じ種類のデータを消費する関数は似ているのは当然です。

以下は2つの非常に似た関数です（図86）：

```racket
; Los -> Boolean
; does l contain "dog"
(define (contains-dog? l)
  (cond
    [(empty? l) #false]
    [else
     (or
      (string=? (first l)
                "dog")
      (contains-dog?
       (rest l)))]))
```

```racket
; Los -> Boolean
; does l contain "cat"
(define (contains-cat? l)
  (cond
    [(empty? l) #false]
    [else
     (or
      (string=? (first l)
                "cat")
      (contains-cat?
       (rest l)))]))
```

図86: 2つの類似した関数

これらの関数はほぼ区別がつきません。各々は文字列のリストを消費し、本体は2つの節を持つ cond 式で構成されます。入力が空リストなら #false を返し、or を使って最初の要素が目的の文字列かどうかを調べ、そうでなければ再帰的に残りを調べます。唯一の違いは比較する文字列です（影付きで強調）。

良いプログラマは、このような密接に関連する関数を複数定義するのを避けます。代わりに、探す文字列を追加の引数として受け取る1つの汎用関数を定義します：

```racket
; String Los -> Boolean
; determines whether l contains the string s
(define (contains? s l)
  (cond
    [(empty? l) #false]
    [else
     (or (string=? (first l) s)
         (contains? s (rest l)))]))
```

これで contains-dog? と contains-cat? は1行で定義できます：

```racket
; Los -> Boolean
; does l contain "dog"
(define (contains-dog? l)
  (contains? "dog" l))

; Los -> Boolean
; does l contain "cat"
(define (contains-cat? l)
  (contains? "cat" l))
```

図87: 2つの類似した関数、再考

これが**関数的抽象化**です。

**Exercise 235.** contains? を使って "atom", "basic", "zoo" を探す関数を定義せよ。

**Exercise 236.** 次の2つの関数のテストスイートを作成せよ：

```racket
; Lon -> Lon
; adds 1 to each item on l
(define (add1* l)
  (cond
    [(empty? l) '()]
    [else
     (cons
      (add1 (first l))
      (add1* (rest l)))]))
```

```racket
; Lon -> Lon
; adds 5 to each item on l
(define (plus5 l)
  (cond
    [(empty? l) '()]
    [else
     (cons
      (+ (first l) 5)
      (plus5 (rest l)))]))
```

これらを抽象化せよ。抽象化した関数を使って上記2つを1行で再定義し、テストで確認せよ。最後に、各数から2を引く関数を設計せよ。

（以下、14.2 Different Similarities、14.3 Similarities in Data Definitions、14.4 Functions Are Values、14.5 Computing with Functions の詳細な説明と例が続きます。）

### 14.2 異なる類似性

（本文の続き：異なるパターンの類似性についても同様に抽象化を適用。）

### 14.3 データ定義における類似性

Los と Lon のようなデータ定義の類似性も抽象化の対象です。パラメータ化されたデータ定義 `[List-of X]` を作成することで、汎用的に扱えます。

### 14.4 関数は値である

ISL では関数は値として扱えます。これにより関数を引数に渡す高階関数が可能になります。

### 14.5 関数を使った計算

（関数を値として扱う際の計算モデルと評価の説明。）


## 15 抽象化の設計 (Designing Abstractions)

### 15.1 例からの抽象化 (Abstractions from Examples)

足し算を初めて学んだとき、あなたは具体的な例を使って作業しました。親はおそらく指を使って小さな2つの数を足すことを教えたでしょう。後になって、任意の2つの数を足す方法を学びました。そこで初めてある種の抽象化に触れました。さらに後で、摂氏から華氏への温度変換や、与えられた速度と時間で車が移動する距離を計算する式を定式化することを学びました。要するに、非常に具体的な例から抽象的な関係へと移行したのです。

```racket
; List-of-numbers -> List-of-numbers
; converts a list of Celsius 
; temperatures to Fahrenheit 
(define (cf* l)
  (cond
    [(empty? l) '()]
    [else
     (cons
      (C2F (first l))
      (cf* (rest l)))]))
```

```racket
; Inventory -> List-of-strings
; extracts the names of 
; toys from an inventory
(define (names i)
  (cond
    [(empty? i) '()]
    [else
     (cons
      (IR-name (first i))
      (names (rest i)))]))
```

```racket
; Number -> Number
; converts one Celsius 
; temperature to Fahrenheit 
(define (C2F c)
  (+ (* 9/5 c) 32))
```

```racket
(define-struct IR
  [name price])
; An IR is a structure:
;   (make-IR String Number)
; An Inventory is one of: 
; – '()
; – (cons IR Inventory)
```

図90: 似た2つの関数

（類似した2つの関数 cf* と names を観察し、共通のパターンを見つける。）

2つの関数はリストを処理し、各要素に関数を適用して cons で新しいリストを作っています。この共通性を抽出します。

```racket
(define (cf* l g)
  (cond
    [(empty? l) '()]
    [else
     (cons
      (g (first l))
      (cf* (rest l) g))]))
```

```racket
(define (names i g)
  (cond
    [(empty? i) '()]
    [else
     (cons
      (g (first i))
      (names (rest i) g))]))
```

```racket
(define (map1 k g)
  (cond
    [(empty? k) '()]
    [else
     (cons
      (g (first k))
      (map1 (rest k) g))]))
```

図91: 同じ2つの似た関数を抽象化したもの

この節では、例から抽象化を作成するための設計レシピを紹介します。

### 15.2 署名における類似性 (Similarities in Signatures)

抽象化の過程で、関数の署名にも類似性が見られます。これにより、どの部分が共通でどの部分が異なるかを明確にできます。

### 15.3 単一の制御点 (Single Point of Control)

抽象化の利点の一つは、コードの変更箇所を1箇所に集中できることです。これによりメンテナンスが容易になります。

### 15.4 テンプレートからの抽象化 (Abstractions from Templates)

データ定義から導かれるテンプレートは、似たデータ構造に対する関数で共通のパターンを示します。このテンプレートを基に抽象化を設計します。


## 17 無名関数 (Nameless Functions)

### 17.1 lambda から生まれる関数 (Functions from lambda)

lambda の構文は次のとおりです：

```racket
(lambda (variable-1 ... variable-N) expression)
```

特徴はキーワード `lambda` です。続いて括弧で囲まれた変数列、そして結果を計算する式があります。

例（1引数）：

```racket
(lambda (x) (expt 10 x))
```

```racket
(lambda (x) (if (> x 0) x (- 0 x)))
```

```racket
(lambda (x) (string-append "hello " x))
```

これらは無名関数です。インタラクションエリアで直接使用できます。

### 17.2 lambda を使った計算 (Computing with lambda)

lambda 式は関数値として評価されます。

### 17.3 lambda を使った抽象化 (Abstracting with lambda)

lambda を使ってその場で関数を作成し、map や filter と組み合わせます。

```racket
(map (lambda (x) (* x x)) (list 1 2 3))
```

### 17.4 lambda を使った仕様 (Specifying with lambda)

テストケースや目的文で lambda を使って動作を指定できます。

### 17.5 lambda を使った表現 (Representing with lambda)

lambda は関数を値として表現するための強力な手段です。

