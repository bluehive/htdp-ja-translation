# III 抽象化 (Abstraction)

## 導入：抽象化の必要性

多くのデータ定義と関数定義は似ています。例えば、Stringのリストの定義はNumberのリストの定義と、データクラスの名前と「String」「Number」という単語の2箇所しか異なりませ。同様に、Stringのリストから特定の文字列を探す関数は、Number of listsから特定の数を探す関数とほとんど区別がつきません。

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

---

## 14 類似性はどこにでもある (Similarities Everywhere)

Arbitrarily Large Data の演習（の一部）を解いた人は、多くの解決策が似ていることを知っているでしょう。実際、類似性は、ある問題の解決策をコピーして次の問題の解決策を作成する誘惑に駆られるかもしれません。

しかし、**thou shall not steal code**（コードを盗んてはならない）、たとえ自分のコードであってもです。代わりに、類似したコード片を**抽象化**しなければなりません。この章では、その抽象化の方法を教えます。

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
      (string=? (first l) "dog")
      (contains-dog? (rest l)))]))
```

```racket
; Los -> Boolean
; does l contain "cat"
(define (contains-cat? l)
  (cond
    [(empty? l) #false]
    [else
     (or
      (string=? (first l) "cat")
      (contains-cat? (rest l)))]))
```

図86: 2つの類似した関数

これらの関数はほぼ区別がつきません。各々は文字列のリストを消費し、本体は2つの節を持つ cond 式で構成されます。入力が空リストなら #false を返し、or を使って最初の要素が目的の文字列かどうかを調べ、そうでなければ再帰的に残りを調べます。唯一の違いは比較する文字列です（図86の "dog" と "cat"）。

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

これが**関数的抽象化 (Functional Abstraction)** です。異なるバージョンの関数を抽象化することは、プログラムから類似性を排除する一つの方法であり、類似性を排除することで、長期にわたってプログラムを健全に維持することが容易になります。

**Exercise 235.** `contains?` を使って "atom", "basic", "zoo" を探す関数を定義せよ。

**Exercise 236.** 次の2つの関数のテストスイートを作成せよ：

```racket
; Lon -> Lon
; adds 1 to each item on l
(define (add1* l)
  (cond
    [(empty? l) '()]
    [else
     (cons (add1 (first l)) (add1* (rest l)))]))
```

```racket
; Lon -> Lon
; adds 5 to each item on l
(define (plus5 l)
  (cond
    [(empty? l) '()]
    [else
     (cons (+ (first l) 5) (plus5 (rest l)))]))
```

これらを抽象化せよ。抽象化した関数を使って上記2つを1行で再定義し、テストで確認せよ。最後に、各数から2を引く関数を設計せよ。

### 14.2 異なる類似性 (Different Similarities)

`contains-dog?` と `contains-cat?` のケースでは抽象化は簡単に見えました。2つの関数定義を比較し、リテラル文字列を関数パラメータに置き換え、元の関数が抽象関数を使って簡単に定義できることを確認するだけでした。この種の抽象化は非常に自然なため、本書の前半2つのパートでも特に断ることなく登場していました。

本節では、これと同じ原理が、より強力な抽象化の形態をどのように生み出すかを示します。図88を見てください。どちらの関数も数値のリストと閾値を消費します。左側は閾値未満のすべての数値のリストを生成し、右側は閾値を超えるすべての数値のリストを生成します。

```racket
; Lon Number -> Lon
; select those numbers on l
; that are below t
(define (small l t)
  (cond
    [(empty? l) '()]
    [else
     (cond
       [(< (first l) t) (cons (first l) (small (rest l) t))]
       [else (small (rest l) t)])]))
```

```racket
; Lon Number -> Lon
; select those numbers on l
; that are above t
(define (large l t)
  (cond
    [(empty? l) '()]
    [else
     (cond
       [(> (first l) t) (cons (first l) (large (rest l) t))]
       [else (large (rest l) t)])]))
```

図88: さらに2つの類似した関数

この2つの関数は、与えられたリストの数値が結果の一部になるべきかどうかを決定する「比較演算子」の1箇所だけが異なります。左側の関数は `<` を使用し、右側は `>` を使用しています。それ以外は、関数名を除いて2つの関数は同一です。

最初の例に従って、追加のパラメータを使ってこれら2つの関数を抽象化しましょう。今回は、追加のパラメータは文字列ではなく、比較演算子（関数）を表します：

```racket
(define (extract R l t)
  (cond
    [(empty? l) '()]
    [else
     (cond
       [(R (first l) t)
        (cons (first l) (extract R (rest l) t))]
       [else
        (extract R (rest l) t)])]))
```

この新しい関数を適用するには、3つの引数を指定する必要があります：2つの数値を比較する関数 `R`、数値のリスト `l`、そして閾値 `t` です。この関数は、`(R i t)` が `#true` に評価される `l` 内のすべての要素 `i` を抽出します。

> [!NOTE]
> ここで、この定義が意味をなすのか疑問に思うかもしれません。私たちは何の苦労もなく、「関数を消費する関数」を作成しました。微分演算や不定積分を学んだことがあるなら、これらが関数を消費して関数を生成する関数であることを知っているでしょう。しかし、本コースではその知識を仮定しません。私たちの単純な学習言語 ISL はこのような関数をサポートしており、このような関数を定義することは優れたプログラマの最も強力なツールの1つです。

テストを実行すると、`(extract < l t)` が `(small l t)` と同じ結果を計算することがわかります：

```racket
(check-expect (extract < '() 5) (small '() 5))
(check-expect (extract < '(3) 5) (small '(3) 5))
(check-expect (extract < '(1 6 4) 5) (small '(1 6 4) 5))
```

同様に、`(extract > l t)` は `(large l t)` と同じ結果を生成します。つまり、元の2つの関数を次のように再定義できます：

```racket
; Lon Number -> Lon
(define (small-1 l t) (extract < l t))

; Lon Number -> Lon
(define (large-1 l t) (extract > l t))
```

重要な洞察は、`small-1` と `large-1` が1行で定義できることだけではありません。`extract` のような抽象関数があれば、他の場所でも有効に活用できます：
*   `(extract = l t)`: `l` 内の `t` と等しい数値をすべて抽出します。
*   `(extract <= l t)`: `l` 内の `t` 以下の数値をすべて抽出します。
*   `(extract >= l t)`: `l` 内の `t` 以上の数値をすべて抽出します。

実際、`extract` の第1引数は ISL の定義済み演算である必要はありません。2つの引数を消費して真偽値を生成する任意の関数を使用できます。次の例を考えてみましょう：

```racket
; Number Number -> Boolean
; is the area of a square with side x larger than c
(define (squared>? x c)
  (> (* x x) c))
```

すなわち、`squared>?` は平方 $x^2 > c$ が成り立つかどうかを検査し、`extract` で使用できます：

```racket
(extract squared>? (list 3 4 5) 10)
```

この適用により、`(list 3 4 5)` の中で平方した値が 10 より大きい数値（この場合は 4 と 5）が抽出されます。

**Exercise 237.** DrRacket で `(squared>? 3 10)` と `(squared>? 4 10)` を評価せよ。`(squared>? 5 10)` はどうなるか。

抽象化された関数定義は、元の関数よりも便利になり得ることがわかりました。たとえば、`contains?` は `contains-dog?` や `contains-cat?` よりも便利であり、`extract` は `small` や `large` よりも便利です。抽象化のこれらの利点は、文書作成、スプレッドシート、小さなアプリ、大規模な産業プロジェクトなど、あらゆるレベルのプログラミングで得られます。

また、抽象化のもう1つの重要な側面は、これらの関数に対して**単一の制御点 (Single Point of Control)** を持てることです。抽象関数に間違いがあることが判明した場合、その定義を修正するだけで、他のすべての定義も修正されます。同様に、抽象関数の計算を高速化する方法を見つければ、この関数を使用して定義されたすべての関数が追加の労力なしに改善されます。

```racket
; Nelon -> Number
; determines the smallest number on l
(define (inf l)
  (cond
    [(empty? (rest l)) (first l)]
    [else
     (if (< (first l) (inf (rest l)))
         (first l)
         (inf (rest l)))]))
```

```racket
; Nelon -> Number
; determines the largest number on l
(define (sup l)
  (cond
    [(empty? (rest l)) (first l)]
    [else
     (if (> (first l) (sup (rest l)))
         (first l)
         (sup (rest l)))]))
```

図89: リスト内の最小値（inf）と最大値（sup）の探索

**Exercise 238.** 図89の2つの関数を1つの関数に抽象化せよ。どちらも空でない数値のリスト（Nelon）を消費し、1つの数値を生成します。左側はリスト内の最小値を生成し、右側は最大値を生成します。

抽象関数を用いて `inf-1` と `sup-1` を定義せよ。以下の2つのリストでテストせよ：

```racket
(list 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1)
(list 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25)
```

なぜこれらの関数は長いリストの一部で遅くなるのか。
元の関数を `min`（2つの数値から小さい方を選択）および `max`（大きい方を選択）を使って修正せよ。その後、再度抽象化し、`inf-2` と `sup-2` を定義して、同じ入力でテストせよ。なぜこれらのバージョンははるかに高速になるのか。

### 14.3 データ定義における類似性 (Similarities in Data Definitions)

ここで、次の2つのデータ定義を詳しく見てみましょう：

```racket
; An Lon (List-of-numbers) is one of:
; – '()
; – (cons Number Lon)
```

```racket
; An Los (List-of-strings) is one of:
; – '()
; – (cons String Los)
```

左側は数値のリストを導入し、右側は文字列のリストを記述しています。そして、これら2つのデータ定義は非常に似ています。類似した関数と同様に、2つのデータ定義は異なる名前を使用していますが、名前は任意であるためこれは重要ではありません。唯一の本当の違いは、2番目の節の `cons` の最初の位置にあり、リストがどのような種類の要素を含むかを指定している点です。

この1つの違いを抽象化するために、データ定義を関数であるかのように扱います。パラメータを導入し、異なる型（要素）を参照していた場所にこのパラメータを使用します：

```racket
; A [List-of ITEM] is one of:
; – '()
; – (cons ITEM [List-of ITEM])
```

このような抽象的なデータ定義を**パラメータ化されたデータ定義 (Parametric Data Definitions)** と呼びます。大雑把に言えば、パラメータ化されたデータ定義は、関数が特定の値から抽象化するのと同様に、特定のデータコレクションへの参照から抽象化します。

問題は、もちろん、これらのパラメータがどのような範囲をとるかです。関数のパラメータが「未知の値」を表すのに対し、データ定義のパラメータは「データのクラス全体（型）」を表します。パラメータ化されたデータ定義に具体的なデータコレクションの名前を割り当てるプロセスを**インスタンス化 (Instantiation)** と呼びます。以下は `List-of` 抽象化のサンプルインスタンス化です：
*   `[List-of Number]` と書くとき、`ITEM` が `Number` を表すため、これは `List-of-numbers` の別名になります。
*   同様に、`[List-of String]` は `List-of-strings` と同じデータクラスを定義します。
*   以下のような在庫レコード `IR` のクラスを定義した場合：
    ```racket
    (define-struct IR [name price])
    ; An IR is a structure: (make-IR String Number)
    ```
    `[List-of IR]` は在庫レコードのリストの名前になります。

慣例として、データ定義のパラメータには大文字の名前（例：`ITEM`, `X`, `Y`）を使用します。

この抽象データ定義が正当であることを確認するには、パラメータ `ITEM` に実際のデータ定義名（たとえば `Number`）を代入し、自己参照（再帰）を展開してみます。得られる定義は従来の数値リストの定義と完全に一致します。

2番目の例として、次の構造体定義から始めましょう：

```racket
(define-struct point [hori veri])
```

この構造体タイプを使用する2つの異なるデータ定義を示します：

```racket
; A Pair-boolean-string is a structure:
;    (make-point Boolean String)

; A Pair-number-image is a structure:
;    (make-point Number Image)
```

この場合、データ定義は2箇所で異なります。`hori` フィールドに対応する違いと、`veri` フィールドに対応する違いです。したがって、抽象データ定義を作成するには2つのパラメータを導入する必要があります：

```racket
; A [CP H V] is a structure:
;    (make-point H V)
```

ここで、`H` は `hori` フィールドのデータコレクション用のパラメータであり、`V` は `veri` フィールドに表示されるデータコレクション用のパラメータです。

2つのパラメータを持つデータ定義をインスタンス化するには、データコレクションの2つの名前が必要です。パラメータに `Number` と `Image` を使用すると、数値と画像を組み合わせたポイント構造体のコレクションを記述する `[CP Number Image]` が得られます。対照的に、`[CP Boolean String]` は真偽値と文字列をポイント構造体で組み合わせます。

**Exercise 239.** 2つの要素のリストは、ISLプログラミングで頻繁に使用されるもう1つのデータ形式です。以下は、2つのパラメータを持つデータ定義です：

```racket
; A [List X Y] is a list:
;    (cons X (cons Y '()))
```

この定義をインスタンス化して、以下のデータクラスを記述せよ：
1.  数値のペア（`Number` と `Number`）
2.  数値と1Stringのペア
3.  文字列と真偽値のペア

また、これら3つのデータ定義のそれぞれについて、具体的な例を1つずつ作成せよ。

パラメータ化されたデータ定義が得られたら、それらを組み合わせて大きな効果を得ることができます。次の定義を考えてみましょう：

```racket
; [List-of [CP Boolean Image]]
```

最も外側の表記は `[List-of ...]` であり、これはリストを扱っていることを意味します。このリストがどのようなデータを含むかという問いに答えるには、内部の式を調べる必要があります：`[CP Boolean Image]`。これは真偽値と画像をポイント内で組み合わせたものです。含意として、上記は真偽値と画像を組み合わせたポイントのリストです。同様に、

```racket
; [CP Number [List-of Image]]
```

は、1つの数値と画像のリストを組み合わせた `CP` のインスタンス化です。

**Exercise 240.** 奇妙ですが類似した次の2つのデータ定義があります：

```racket
; An LStr is one of:
; – String
; – (make-layer LStr)
```

```racket
; An LNum is one of:
; – Number
; – (make-layer LNum)
```

どちらのデータ定義も、次の構造体定義に依存しています：

```racket
(define-struct layer [stuff])
```

両者について具体例を作成せよ。2つを抽象化したデータ定義を作成せよ。そして、抽象定義をインスタンス化して元の定義を復元せよ。

**Exercise 241.** `NEList-of-temperatures` と `NEList-of-Booleans` の定義を比較せよ。そして、空でないリストを表す抽象データ定義 `NEList-of` を策定せよ。

**Exercise 242.** 以下は、もう1つのパラメータ化されたデータ定義です：

```racket
; A [Maybe X] is one of:
; – #false
; – X
```

これらのデータ定義を解釈せよ：`[Maybe String]`, `[Maybe [List-of String]]`, `[List-of [Maybe String]]`。

次の関数署名は何を意味するか：

```racket
; String [List-of String] -> [Maybe [List-of String]]
; returns the remainder of los starting with s
; #false otherwise
(check-expect (occurs "a" (list "b" "a" "d" "e")) (list "d" "e"))
(check-expect (occurs "a" (list "b" "c" "d")) #false)
(define (occurs s los) los)
```

設計レシピの残りのステップを実行せよ。

### 14.4 関数は値である (Functions Are Values)

本パートの関数は、プログラムの評価に関する私たちの理解を拡張します。関数が数値だけでなく、文字列や画像を消費することは理解しやすいでしょう。構造体やリストは少し拡張が必要ですが、結局のところ有限の「もの」です。しかし、関数を消費する関数は奇妙に思えます。実際、このアイデア自体が最初のインターメッツォ（BSL）の規則に2つの方法で違反しています：
1.  プリミティブや関数の名前が、適用式の引数として使用されている。
2.  パラメータが、適用式の「関数位置」で使用されている。

問題を詳しく説明すると、ISLの文法がBSLとどのように異なるかがわかります。第1に、式言語は定義内の関数名とプリミティブ演算の名前を含めるべきです。第2に、適用式の最初の位置は、関数名やプリミティブ演算以外のもの（変数や関数のパラメータなど）を許容しなければなりません。

文法への変更は評価規則への変更を要求するように見えますが、変更されるのは「値の集合」だけです。具体的には、関数を関数の引数として受け入れるために、最も単純な変更は「関数やプリミティブ演算もまた値である」とすることです。

**Exercise 243.** DrRacket の定義領域に以下が含まれていると仮定します：

```racket
(define (f x) x)
```

以下の式のうち、値（値の定義を満たすもの）を特定せよ：
1.  `(cons f '())`
2.  `(f f)`
3.  `(cons f (cons 10 (cons (f 10) '())))`

なぜそれらが値である（または値でない）のかを説明せよ。

**Exercise 244.** 次の記述がISLにおいて合法（文法的に正しい）である理由を論じよ：
1.  `(define (f x) (x 10))`
2.  `(define (f x) (x f))`
3.  `(define (f x y) (x 'a y 'b))`

あなたの推論を説明せよ。

**Exercise 245.** `function=at-1.2-3-and-5.775?` 関数を設計せよ。数値から数値への2つの関数が与えられたとき、この関数は、1.2、3、および -5.775 に対して2つの関数が同じ結果を生成するかどうかを判定します。

数学者は、同じ入力が与えられたときに同じ結果を計算する場合、2つの関数は等しいと言います。数値から数値への2つの関数が等しいかどうかを判定する一般関数 `function=?` を定義することは可能でしょうか。もし可能なら定義せよ。不可能なら、その理由を説明し、これが「簡単に定義できるアイデアであるにもかかわらず、その関数を定義できない最初の例」に遭遇したことを意味するインプリケーションを考慮せよ。

### 14.5 関数を使った計算 (Computing with Functions)

BSL+ から ISL への移行により、関数を引数として使用し、適用式の最初の位置にパラメータ名を使用できるようになりました。DrRacket はこれらの位置にある名前を他の場所と同様に処理しますが、当然ながら結果として関数を期待します。驚くべきことに、代数の法則を単純に適用するだけで、ISL プログラムを評価することができます。

`extract` の評価がどのように機能するかを見てみましょう。明らかに、

```racket
(extract < '() 5) == '()
```

が成り立ちます。「Intermezzo 1」の代入モデルを使用して、関数の本体で計算を続けることができます。パラメータ `R`, `l`, `t` が、引数 `<`, `'()`, `5` にそれぞれ置き換えられます。ここからは、条件式の評価から始まるプレーンな計算です：

```racket
==
(cond
  [(empty? '()) '()]
  [else
   (cond
     [(< (first '()) 5)
      (cons (first '()) (extract < (rest '()) 5))]
     [else (extract < (rest '()) 5)])])
==
(cond
  [#true '()]
  [else
   (cond
     [(< (first '()) 5)
      (cons (first '()) (extract < (rest '()) 5))]
     [else (extract < (rest '()) 5)])])
== '()
```

次に、要素が1つのリストを考えます：

```racket
(extract < (cons 4 '()) 5)
```

リストの唯一の要素は 4 であり、`(< 4 5)` は真であるため、結果は `(cons 4 '())` になるはずです。評価の最初のステップは次のようになります：

```racket
(extract < (cons 4 '()) 5)
==
(cond
  [(empty? (cons 4 '())) '()]
  [else
   (cond
     [(< (first (cons 4 '())) 5)
      (cons (first (cons 4 '()))
            (extract < (rest (cons 4 '())) 5))]
     [else (extract < (rest (cons 4 '())) 5)])])
```

やはり、`R` は `<`, `l` は `(cons 4 '())`, `t` は `5` に置き換えられます。残りは簡単です：

```racket
(cond
  [(empty? (cons 4 '())) '()]
  [else
   (cond
     [(< (first (cons 4 '())) 5)
      (cons (first (cons 4 '()))
            (extract < (rest (cons 4 '())) 5))]
     [else (extract < (rest (cons 4 '())) 5)])])
==
(cond
  [#false '()]
  [else
   (cond
     [(< (first (cons 4 '())) 5)
      (cons (first (cons 4 '()))
            (extract < (rest (cons 4 '())) 5))]
     [else (extract < (rest (cons 4 '())) 5)])])
==
(cond
  [(< (first (cons 4 '())) 5)
   (cons (first (cons 4 '()))
         (extract < (rest (cons 4 '())) 5))]
  [else (extract < (rest (cons 4 '())) 5)])
==
(cond
  [(< 4 5)
   (cons (first (cons 4 '()))
         (extract < (rest (cons 4 '())) 5))]
  [else (extract < (rest (cons 4 '())) 5)])
```

ここが重要なステップであり、代入された位置で `<` が実際に使用されています。そして、計算が続きます：

```racket
==
(cond
  [#true
   (cons (first (cons 4 '()))
         (extract < (rest (cons 4 '())) 5))]
  [else (extract < (rest (cons 4 '())) 5)])
==
(cons 4 (extract < (rest (cons 4 '())) 5))
==
(cons 4 (extract < '() 5))
==
(cons 4 '())
```

最後の例は、2つの要素のリストへの適用です：

```racket
(extract < (cons 6 (cons 4 '())) 5)
== (extract < (cons 4 '()) 5)
== (cons 4 (extract < '() 5))
== (cons 4 '())
```

ステップ 1 は、閾値未満でない場合に `extract` がリストの最初の要素を除外するケースを扱っています。

**Exercise 246.** DrRacket の Stepper（ステップ実行）を使用して、最後の計算のステップ 1 を確認せよ。

**Exercise 247.** DrRacket の Stepper を使用して `(extract < (cons 8 (cons 4 '())) 5)` を評価せよ。

**Exercise 248.** DrRacket の Stepper で `(squared>? 3 10)` と `(squared>? 4 10)` を評価せよ。

次の対話を考えてみます：
```racket
> (extract squared>? (list 3 4 5) 10)
(list 4 5)
```
Stepper が示すステップの一部を以下に示します：
```racket
(extract squared>? (list 3 4 5) 10)
; (1) ==
(cond
  [(empty? (list 3 4 5)) '()]
  [else
   (cond
     [(squared>? (first (list 3 4 5)) 10)
      (cons (first (list 3 4 5)) (extract squared>? (rest (list 3 4 5)) 10))]
     [else (extract squared>? (rest (list 3 4 5)) 10)])])

; (2) == ... ==
(cond
  [(squared>? 3 10)
   (cons (first (list 3 4 5)) (extract squared>? (rest (list 3 4 5)) 10))]
  [else (extract squared>? (rest (list 3 4 5)) 10)])
```
Stepper を使用して、行 (1) から (2) へのステップを確認せよ。さらにステップを進めて、ステップ (2) から最終結果までの隙間を埋めよ。各ステップを代入モデルや関数の評価ルールを用いて説明せよ。

**Exercise 249.** 関数は「値」であり、引数、結果、リストの要素になり得ます。以下の定義と式を DrRacket の定義ウィンドウに入力し、Stepper を使ってこのプログラムがどのように動作するかを調べよ：

```racket
(define (f x) x)
(cons f '())
(f f)
(cons f (cons 10 (cons (f 10) '())))
```

---

## 15 抽象化の設計 (Designing Abstractions)

本質的に、抽象化とは「具体的なものをパラメータに変換すること」です。前章でもこれを行いました。類似した関数定義を抽象化するには、定義内の具体的な値を置き換えるパラメータを追加します。類似したデータ定義を抽象化するには、パラメータ化されたデータ定義を作成します。他のプログラミング言語に触れると、その抽象化メカニズムもパラメータの導入を必要とすることを目にするでしょう（それが関数の引数であるとは限りませんが）。

### 15.1 例からの抽象化 (Abstractions from Examples)

あなたが足し算を初めて学んだとき、具体的な例を使って作業しました。親はおそらく指を使って小さな2つの数を足すことを教えたでしょう。後になって、任意の2つの数を足す方法を学びました。そこで初めてある種の抽象化に触れました。さらに後で、摂氏から華氏への温度変換や、与えられた速度と時間で車が移動する距離を計算する式を定式化することを学びました。要するに、非常に具体的な例から抽象的な関係へと移行したのです。

```racket
; List-of-numbers -> List-of-numbers
; converts a list of Celsius temperatures to Fahrenheit
(define (cf* l)
  (cond
    [(empty? l) '()]
    [else
     (cons (C2F (first l)) (cf* (rest l)))]))
```

```racket
; Inventory -> List-of-strings
; extracts the names of toys from an inventory
(define (names i)
  (cond
    [(empty? i) '()]
    [else
     (cons (IR-name (first i)) (names (rest i)))]))
```

```racket
; Number -> Number
; converts one Celsius temperature to Fahrenheit
(define (C2F c)
  (+ (* 9/5 c) 32))
```

```racket
(define-struct IR [name price])
; An IR is a structure: (make-IR String Number)
; An Inventory is one of:
; – '()
; – (cons IR Inventory)
```

図90: 似た2つの関数

本節では、例から抽象化を作成するための設計レシピを紹介します。抽象化を作成すること自体は簡単ですが、既存の抽象化を見つけて利用するという「難しい部分」は次の節に譲ります。

「類似性はどこにでもある」のエッセンスを思い出してください。2つの具体的な定義から始め、それらを比較し、違いをマークし、そして抽象化します。抽象化を作成する手順は、ほとんどこれだけです：
1.  **類似点と相違点の比較 (Compare)**
    ほぼ同じで、名前と特定の位置にある具体的な値だけが異なる2つの関数定義を見つけたら、それらを比較して相違点をマークします。もし違いが複数箇所にある場合は、対応する違い同士を結びつけます。
    図90は、類似した関数定義のペアを示しています。2つの関数はリストを処理し、各要素に関数を適用しています。違いは「どの関数を要素に適用するか」という点だけです。
2.  **パラメータ化 (Parameterize)**
    相違点としてマークした部分を新しいパラメータ名（引数）に置き換え、パラメータリストに追加します。図90の例では、相違点を `g` という名前に置き換えます。これにより本質的な違いが排除されます。
    次に、非本質的な違い（関数名やリスト引数の名前など）を統一します。関数名を `map1`、リストパラメータを `k` と呼ぶことにすると、図91のように、完全に同一の関数定義が得られます。
    ```racket
    (define (map1 k g)
      (cond
        [(empty? k) '()]
        [else
         (cons (g (first k)) (map1 (rest k) g))]))
    ```
    図91: 抽象化された同一の関数定義

    違いが複数ある場合は、対応する違いのラインごとに1つの追加パラメータを導入します。そして、すべての再帰呼び出し部分にも追加パラメータを忘れずに引き渡すように変更します。
3.  **検証と再定義 (Validate)**
    新しい抽象関数が、元の関数の正しい抽象化であることを検証します。これは、元の関数を抽象関数を使って定義し直し、既存のテストスイートが正常に通るか確認することを意味します。
    元の関数が `f-original` で引数を1つ消費し、抽象関数が `abstract` であるとします。`f-original` が他方と `val` という値の使用において異なる場合、次の定義を行います：
    ```racket
    (define (f-from-abstract x)
      (abstract x val))
    ```
    この `f-from-abstract` が `f-original` と同等であることをテストします。
    先ほどの例に戻ると：
    ```racket
    (define (cf*-from-map1 l) (map1 l C2F))
    (define (names-from-map1 i) (map1 i IR-name))
    ```
    元のテストケースが以下のように定義されていたとします：
    ```racket
    (check-expect (cf* (list 100 0 -40)) (list 212 32 -40))
    (check-expect (names (list (make-IR "doll" 21.0) (make-IR "bear" 13.0)))
                  (list "doll" "bear"))
    ```
    これらを次のように書き換えて実行し、成功を確認します：
    ```racket
    (check-expect (cf*-from-map1 (list 100 0 -40)) (list 212 32 -40))
    (check-expect (names-from-map1 (list (make-IR "doll" 21.0) (make-IR "bear" 13.0)))
                  (list "doll" "bear"))
    ```
4.  **署名の定式化 (Signature)**
    新しい抽象関数に署名（Signature）を与えます。これについては 15.2 で詳しく扱います。

新しい抽象化を行ったら、他に使える用途がないか確認します。用途が多ければ、その抽象化は本当に有用です。たとえば、`map1` を使って数値リストの各要素に 1 を加える関数は以下のように定義できます：

```racket
; List-of-numbers -> List-of-numbers
(define (add1-to-each l)
  (map1 l add1))
```

このような汎用的な関数がすでに言語の一部として提供されていることもよくあります（Chapter 16を参照）。

```racket
; Number -> [List-of Number]
; tabulates sin between n and 0 (incl.) in a list
(define (tab-sin n)
  (cond
    [(= n 0) (list (sin 0))]
    [else (cons (sin n) (tab-sin (sub1 n)))]))
```

```racket
; Number -> [List-of Number]
; tabulates sqrt between n and 0 (incl.) in a list
(define (tab-sqrt n)
  (cond
    [(= n 0) (list (sqrt 0))]
    [else (cons (sqrt n) (tab-sqrt (sub1 n)))]))
```

図92: 演習250のための類似した関数

```racket
; [List-of Number] -> Number
; computes the sum of the numbers on l
(define (sum l)
  (cond
    [(empty? l) 0]
    [else (+ (first l) (sum (rest l)))]))
```

```racket
; [List-of Number] -> Number
; computes the product of the numbers on l
(define (product l)
  (cond
    [(empty? l) 1]
    [else (* (first l) (product (rest l)))]))
```

図93: 演習251のための類似した関数

**Exercise 250.** 図92の2つの関数の抽象化である `tabulate` を設計せよ。設計が完了したら、それを使って `sqr`（平方）と `tan` の表を作成する関数を定義せよ。

**Exercise 251.** 図93の2つの関数の抽象化である `fold1` を設計せよ。

**Exercise 252.** 図94の2つの関数の抽象化である `fold2` を設計せよ。この演習と演習251を比較せよ。どちらも `product` 関数を含んでいますが、この演習は2番目の関数 `image*` が `Posn` のリストを消費して `Image` を生成するため、難易度が高くなっています。得られた設計と前演習の設計を比較し、署名の抽象化についての洞察を得よ。

```racket
; [List-of Number] -> Number
(define (product l)
  (cond
    [(empty? l) 1]
    [else (* (first l) (product (rest l)))]))

; [List-of Posn] -> Image
(define (image* l)
  (cond
    [(empty? l) emt]
    [else (place-dot (first l) (image* (rest l)))]))

; Posn Image -> Image
(define (place-dot p img)
  (place-image dot (posn-x p) (posn-y p) img))

; 描画用定数
(define emt (empty-scene 100 100))
(define dot (circle 3 "solid" "red"))
```

図94: 演習252のための類似した関数

### 15.2 署名における類似性 (Similarities in Signatures)

関数の署名（Signature）は、その再利用の鍵となります。したがって、抽象化された関数を表現するのに十分な「最も一般的な署名」を記述する方法を学ぶ必要があります。

基本的に、署名はデータ定義と同じです。どちらもデータのクラスを指定しますが、データ定義はクラスに名前を付けるのに対し、署名はそうしません。それでも、以下のコード：

```racket
; Number Boolean -> String
(define (f n b) "hello world")
```

の最初の行は、`Number` と `Boolean` を消費して `String` を生成するすべての関数のクラスを表しています。

したがって、抽象化の設計レシピは署名にも適用できます。類似した署名を比較し、相違点を強調し、それらをパラメータで置き換えます。

`cf*` と `names` の元の署名を比較してみましょう：
*   `cf*` : `[List-of Number] -> [List-of Number]`
*   `names` : `[List-of IR] -> [List-of String]`

比較すると、矢印の左側で `Number` と `IR` が異なり、右側で `Number` と `String` が異なります。
これら2つの相違点をパラメータ `X` と `Y` に置き換えると、次のようになります：

```racket
; [List-of X] -> [List-of Y]
```

このシグネチャに現れる変数 `X` と `Y` は、データ定義のパラメータ（ Chapter 14.3 ）と同じようにデータのクラス全体を表します。
これらをインスタンス化（代入）すると、元の署名が得られます：
*   `X` と `Y` に `Number` を代入すると、`cf*` の署名になります。
*   `X` に `IR`、`Y` に `String` を代入すると、`names` の署名になります。

次に、追加の関数引数を受け取る `map1` の署名を考えます。`map1` の署名は次のようになります：

```racket
; [X Y] [List-of X] [X -> Y] -> [List-of Y]
```

具体的には、`map1` は `X` という型に属する要素のリストを消費します。また、`X` の要素を消費して `Y` という（また別の）型の要素を生成する関数を消費します。そして、結果として `Y` のリストを返します。

もう1つの例として、演習252の `product` と `image*` の署名を抽象化します：
*   `product` の署名： `[List-of Number] Number [Number Number -> Number] -> Number`
*   `image*` の署名： `[List-of Posn] Image [Posn Image -> Image] -> Image`

これらを比較すると、すべての `Number` が一様に対応しているわけではなく：
1.  ある `Number` は `Posn` に対応している（リストの要素）。
2.  別の `Number` は `Image` に対応している（ベースケースと結果の型）。

したがって、2つのパラメータ `X` と `Y` を導入し、`fold2` の署名は次のようになります：

```racket
; [X Y] [List-of X] Y [X Y -> Y] -> Y
```

`X` と `Y` の両方に `Number` を代入すると `product` の署名が得られ、`X` に `Posn`、`Y` に `Image` を代入すると `image*` の署名が得られることを確認してください。

署名を抽象化するためのステップを以下にまとめます：
1.  **シグネチャの比較**: 2つの類似した関数の具体的な署名を比較し、相違点をマークします。
2.  **パラメータの抽出**: 抽象化によって追加されたパラメータが何を表しているかを特定し、対応するプレースホルダーを割り当てます。
3.  **変数の置き換え**: 相違点を表す型パラメータ（`X`, `Y`など）を導入し、統一された汎用的な署名を作成します。
4.  **検証**: 型パラメータに具体的な型を代入し、元の個々の署名が正しく復元されることを確認します。

**Exercise 253.** 以下のそれぞれの署名は関数のクラスを表しています：
1.  `[Number -> Boolean]`
2.  `[Boolean String -> Boolean]`
3.  `[Number Number Number -> Number]`
4.  `[Number -> [List-of Number]]`
5.  `[[List-of Number] -> Boolean]`

それぞれのクラスに属する具体的な関数の例を ISL で記述せよ。

**Exercise 254.** 以下の関数の署名を策定せよ：
*   `sort-n`: 数値のリストと、2つの数値を比較して真偽値を返す関数を消費し、ソートされた数値のリストを生成する。
*   `sort-s`: 文字列のリストと、2つの文字列を比較して真偽値を返す関数を消費し、ソートされた文字列のリストを生成する。

その後、2つの署名を抽象化せよ。さらに、一般化された署名が、在庫レコード（`IR`）のリストをソートする関数の署名としてインスタンス化できることを示せ。

**Exercise 255.** 以下の関数の署名を策定せよ：
*   `map-n`: 数値のリストと、数値から数値への関数を消費し、数値のリストを生成する。
*   `map-s`: 文字列のリストと、文字列から文字列への関数を消費し、文字列のリストを生成する。

その後、2つの署名を抽象化せよ。また、一般化された署名が上記 `map1` の署名としてインスタンス化できることを示せ。

### 15.3 単一の制御点 (Single Point of Control)

プログラムは文章の下書き（ドラフト）のようなものです。誤字の修正、文法エラーの修正、文章の一貫性の確保、そして重複の排除などの編集作業は、文章を良くするために不可欠です。誰も同じことを何度も繰り返す文章を読みたくはありませんし、そのようなプログラムも読みたくはありません。

重複を排除して抽象化を作成することには、多くの利点があります。定義がシンプルになり、既存の関数の潜在的な不具合（境界の不一致など）が明らかになります。しかし、最も重要な利点は、共通の機能に対して**単一の制御点 (Single Point of Control)** を作ることです。

機能の定義を1箇所にまとめることで、プログラムのメンテナンスが非常に容易になります：
*   バグ（間違い）を発見したとき、1箇所だけを修正すればよくなります。
*   新しいデータ形式に対応する必要が生じたとき、1箇所にコードを追加するだけで済みます。
*   アルゴリズムを改善したり高速化したりしたとき、1箇所の変更ですべての利用箇所が恩恵を受けます。

もしコードをコピー＆ペーストしていた場合、すべてのコピー箇所を探し出して修正しなければならず、ミスの修正漏れが発生する危険性が非常に高くなります。

したがって、次のガイドラインを強く推奨します：

> [!IMPORTANT]
> **コードをコピーして修正する代わりに、抽象化を作成せよ。**

抽象化の構築はプログラミングスキルを高めるための最も強力な練習の1つです。優れたプログラマは、重複を見つけると積極的にプログラムをリファクタリング（編集）し、新しい抽象化を構築して制御点を1箇所に集中させます。

### 15.4 テンプレートからの抽象化 (Abstractions from Templates)

リストを処理する多くの関数は、データ定義から自動的に導かれる共通のテンプレートに従っています。したがって、関数が互いに似通った形になるのは必然です。

実は、私たちは個々の関数からだけでなく、**テンプレートそのものから直接抽象化を作成する**ことができます。リストを走査する関数の基本テンプレートを思い出してください：

```racket
(define (fun-for-l l)
  (cond
    [(empty? l) ...]
    [else (... (first l) ... (fun-for-l (rest l)) ...)]))
```

このテンプレートには、各節に1つずつ、合計2つの「空欄 (gap)」があります。リスト処理関数を定義するとき、最初の節の空欄をベース値で埋め、2番目の節の空欄を「組み合わせる（結合する）関数」で埋めます。この結合関数は、リストの最初の要素と、残りのリストに対する再帰呼び出しの結果を組み合わせます。

この仕組みをパラメータ化して抽象関数を定義すると、次のようになります：

```racket
; [X Y] [List-of X] Y [X Y -> Y] -> Y
(define (reduce l base combine)
  (cond
    [(empty? l) base]
    [else
     (combine (first l)
              (reduce (rest l) base combine))]))
```

この `reduce` を使うと、リスト処理関数の多くを1行で定義できるようになります。たとえば、数値のリストの総和 `sum` と総乗 `product` は次のように再定義できます：

```racket
; [List-of Number] -> Number
(define (sum lon) (reduce lon 0 +))

; [List-of Number] -> Number
(define (product lon) (reduce lon 1 *))
```

`sum` では、空リストの場合のベース値は 0 であり、組み合わせる関数は `+` です。`product` では、ベース値は 1 であり、組み合わせる関数は `*` です。このように、多くのリスト処理関数が `reduce` を使って簡潔に再定義できます。

---

## 17 無名関数 (Nameless Functions)

### 17.1 lambda から生まれる関数 (Functions from lambda)

`lambda` の構文は次のとおりです：

```racket
(lambda (variable-1 ... variable-N) expression)
```

特徴はキーワード `lambda` です。続いて括弧で囲まれた変数列、そして結果を計算する式があります。

例（1引数）：

```racket
(lambda (x) (expt 10 x))
(lambda (x) (if (> x 0) x (- 0 x)))
(lambda (x) (string-append "hello " x))
```

これらは無名関数です。インタラクションエリアで直接使用できます。

### 17.2 lambda を使った計算 (Computing with lambda)

`lambda` 式は関数値として評価されます。

### 17.3 lambda を使った抽象化 (Abstracting with lambda)

`lambda` を使ってその場で関数を作成し、`map` や `filter` と組み合わせます。

```racket
(map (lambda (x) (* x x)) (list 1 2 3))
```

### 17.4 lambda を使った仕様 (Specifying with lambda)

テストケースや目的文で `lambda` を使って動作を指定できます。

### 17.5 lambda を使った表現 (Representing with lambda)

`lambda` は関数を値として表現するための強力な手段です。
