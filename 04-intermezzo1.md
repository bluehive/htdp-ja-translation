<!-- 個人学習用 AI 意訳（非公式）。原文: extracted/original_markdown_04_i1-2.md -->
<!-- コードフェンスは英語原本と一致。 -->

## Intermezzo 1: Beginning Student Language（初級学生言語）

### 目次 (Contents)

- BSL の語彙 (BSL Vocabulary)
- BSL の文法 (BSL Grammar)
- BSL の意味 (BSL Meaning)
- 意味とコンピューティング (Meaning and Computing)
- BSL のエラー (BSL Errors)
- ブール式 (Boolean Expressions)
- 定数定義 (Constant Definitions)
- 構造型定義 (Structure Type Definitions)
- BSL のテスト (BSL Tests)
- BSL のエラーメッセージ (BSL Error Messages)

第I部「固定サイズのデータ」は、BSL を自然言語であるかのように扱いました。言語の「基本的な単語」を紹介し、「単語」を「文」に組み立てる方法を示唆し、これらの「文」を直感的に理解するために代数学の知識に訴えかけました。この種の導入はある程度は機能しますが、真に効果的なコミュニケーションには、ある程度の形式的な学習が必要です。

多くの点で、第I部のアナロジーは正しいものです。プログラミング言語には語彙と文法があり、プログラマはこれらの要素を **構文 (syntax)** と呼びます。BSL における「文」は、**式 (expression)** または **定義 (definition)** です。BSL の文法は、これらの句をどのように形成するかを規定します。しかし、文法的に正しい文であっても、すべてが意味を持つわけではありません——英語でもプログラミング言語でも同じです。例えば、英語の文「the cat is round」は意味を持ちますが、「the brick is a car」は文法的には完全に正しくても意味がありません。文が意味を持つかどうかを判断するには、言語の **意味 (meaning)** を知る必要があります。プログラマはこれを **意味論 (semantics)** と呼びます。

この Intermezzo では、BSL を中学校で馴染みのある算数・代数の言語の拡張であるかのように提示します。結局のところ、計算はこの単純な数学の形式から始まるのですから、この数学とコンピューティングのつながりを理解すべきです。最初の3つの節では、BSLのかなりの部分の構文と意味論を提示します。この新しいBSLの理解に基づき、4つ目の節ではエラーの議論を再開します。残りの節はこの理解を完全な言語に拡張し、最後の節ではテストを表現するためのツールを拡張します。

> **注 (Note):** プログラマは最終的にこれらの計算の原理を理解しなければなりませんが、それらは設計の原理を補完するものです。

## BSL の語彙 (BSL Vocabulary)

図39は、BSLの基本的な語彙を紹介し定義しています。語彙は、数値や真偽値などのリテラル定数、BSLによって意味が与えられている名前（例: `cond` や `+`）、そしてプログラムが `define` や関数のパラメータを通じて意味を与えることができる名前から構成されます。

```
+--------------------------------------------------------------------------------+
| Figure 39: BSL core vocabulary                                                 |
|                                                                                |
| * A primitive is a name to which BSL assigns meaning, for
example, + or sqrt.  |
| * A variable is a name without preassigned meaning.                            |
|                                                                                |
| * A number is one of: 1, -1, 3/5, 1.22, #i1.22, 0+1i, and so on. The syntax    |
| for BSL numbers is complicated because it accommodates a range of formats:     |
| positive and negative numbers, fractions and decimal numbers, exact and        |
| inexact numbers, real and complex numbers, numbers in bases other than 10, and |
| more. Understanding the precise notation for numbers requires a thorough       |
| understanding of grammars and parsing, which is out of scope for this          |
| intermezzo.                                                                    |
| * A Boolean is one of: #true or #false.                                        |
| * A string is one of: "", "he says \"hello world\" to you", "doll", and so on. |
| In general, it is a sequence of characters enclosed by a pair of ".            |
| * An image is a png, jpg, tiff, and various other formats. We intentionally    |
| omit a precise definition.                                                     |
+--------------------------------------------------------------------------------+
```

それぞれの説明は、要素の示唆的な列挙によって集合を定義しています。これらの集まりを完全に指定することも可能ですが、ここではそれは余分と考え、直感を信頼します。ただし、これらの集合のそれぞれに追加の要素が含まれる場合があることだけは念頭に置いてください。

## BSL の文法 (BSL Grammar)

図40は、BSL文法の大部分を示しています。他の言語と比べて極めて単純です。BSLの表現力については見た目に惑わされないでください。ただし最初の課題は、このような文法の読み方を議論することです。`=` のある各行は統語範疇を導入します。`=` は「〜のいずれかである」、`|` は「または」と読むのがよいです。三点リーダ `...` があるところでは、その直前のものを好きな回数だけ繰り返すと想像してください。これは例えば、`program` が何もないか、`def-expr` が1回、または2回・3回・4回・5回……といくらでも続く列であることを意味します。この例は特に明快ではないので、2つ目の統語範疇を見てみましょう。それは `def` が次のいずれかであることを述べています。

> **注 (Note):** 文法を声に出して読むと、データ定義のように聞こえます。実際、多くのデータ定義を文法で書き下ろすこともできます。

```racket
(define (variable variable) expr)
```

なぜなら「好きな回数」にはゼロも含まれるからです。あるいは

```racket
(define (variable variable variable) expr)
```

これは1回の繰り返しです。あるいは

```racket
(define (variable variable variable variable) expr)
```

これは2回使っています。

```
+---------------------------------------------------------------+
| Figure 40: BSL core grammar                                   |
|                                                               |
| +----------+--+---+--+--------------------------------------+ |
| | program  |  | = |  | def-expr...                         | |
| +----------+--+---+--+--------------------------------------+ |
| | def-expr |  | = |  | def                                  | |
| |          |  | | |  | expr                                 | |
| | def      |  | = |  | (define (variable variable variable… | |
| | expr     |  | = |  | variable                             | |
| |          |  | | |  | value                                | |
| |          |  | | |  | (primitive expr expr...)            | |
| |          |  | | |  | (variable expr expr...)             | |
| |          |  | | |  | (cond [expr expr]... [expr expr])   | |
| |          |  | | |  | (cond [expr expr]... [else expr])   | |
| +----------+--+---+--+--------------------------------------+ |
+---------------------------------------------------------------+
```

文法についての最後のポイントは、特別なフォントで書かれた3つの「語」——`define`、`cond`、`else`——に関するものです。BSL語彙の定義によれば、これらの3語は名前です。語彙定義が教えてくれないのは、これらの名前があらかじめ定められた意味を持つことです。BSLでは、これらの語はいくつかの複合文を他と区別するマーカーとして働き、その役割を認めて **キーワード (keywords)** と呼ばれます。

これで文法の目的を述べる準備ができました。プログラミング言語の文法は、その語彙から文をどのように形成するかを規定します。ある文は単に語彙の要素です。例えば、図40によれば `42` はBSLの文です：

- 最初の統語範疇は、プログラムが `def-expr` であることを言います。式は定義を参照できます。
- 2つ目は、`def-expr` が `def` または `expr` であることを教えます。
  > **注 (Note):** DrRacketでは、プログラムは実際には2つの異なる部分——定義領域と、対話領域の式——から成ります。
- 最後の定義は `expr` を形成するすべての方法を列挙し、その2つ目が `value` です。

> **注 (Note):** DrRacketでは、プログラムは実際には2つの異なる部分——定義領域と、対話領域の式——から成ります。

図39から `42` が値であることがわかるので、確認が取れます。

文法の興味深い部分は、他の文から組み立てられる複合文の作り方を示します。例えば、`def` の部分は、関数定義が「(」に続いてキーワード `define`、さらに「(」、少なくとも2つの変数の列、「)」、`expr`、そして最初のものと対応する閉じの「)」で形成されることを教えています。先頭のキーワード `define` が定義を式から区別することに注意してください。

式 (`expr`) には6つの種類があります：変数、定数、プリミティブ適用、(関数)適用、および2種類の条件式です。最初の2つは原子的な文で、残りの4つは複合文です。`define` と同様に、キーワード `cond` が条件式を適用から区別します。

式の例を3つ挙げます：`"all"`、`x`、そして `(f x)`。最初のものは文字列のクラスに属し、したがって式です。2つ目は変数であり、すべての変数は式です。3つ目は関数適用です。なぜなら `f` と `x` が変数だからです。

対照的に、次の括弧付きの文は合法な式ではありません：`(f define)`、`(cond x)`、`((f 2) 10)`。最初のものは関数適用の形に部分的に一致しますが、`define` を変数であるかのように使っています。2つ目は正しい `cond` 式になることに失敗します。なぜなら2番目の要素が変数であり、括弧で囲まれた式の対ではないからです。最後のものは条件式でも適用でもありません。最初の部分が式だからです。

最後に、文法が空白（スペース、タブ、改行）に言及していないことに気づくかもしれません。BSLは寛容な言語です。プログラム内の任意の列の要素の間に何らかの空白があれば、DrRacketはあなたのBSLプログラムを理解できます。しかし、優れたプログラマはあなたが書くものを好まないかもしれません。これらのプログラマは空白を使ってプログラムを読みやすくします。最も重要なのは、プログラムを処理するソフトウェア（DrRacketなど）より人間の読者を優先するスタイルを採用することです。彼らは本のコード例を注意深く読み、どのように整形されているかに注意を払うことでこのスタイルを身につけます。

> **注 (Note):** あなたのBSLプログラムを調べる読者は2種類いることを念頭に置いてください：人と DrRacket です。

**練習問題 116 (Exercise 116).** 次の文を見てください：

1. `x`
2. `(= y z)`
3. `(= (= y z) 0)`

これらが統語的に合法な式である理由を説明せよ。

**練習問題 117 (Exercise 117).** 次の文を考えよ：

1. `(3 + 4)`
2. `number?`
3. `(x)`

これらが統語的に非合法である理由を説明せよ。

**練習問題 118 (Exercise 118).** 次の文を見てください：

1. `(define (f x) x)`
2. `(define (f x) y)`
3. `(define (f x y) 3)`

これらが統語的に合法な定義である理由を説明せよ。

**練習問題 119 (Exercise 119).** 次の文を考えよ：

1. `(define (f "x") x)`
2. `(define (f x y z) (x))`

これらが統語的に非合法である理由を説明せよ。

**練習問題 120 (Exercise 120).** 合法な文と非合法な文を区別せよ：

1. `(x)`
2. `(+ 1 (not x))`
3. `(+ 1 2 3)`

なぜ合法または非合法かを説明せよ。合法なものが範疇 `expr` と `def` のどちらに属するかを判定せよ。

**文法用語についての注 (Note on Grammatical Terminology)** 複合文の構成要素には名前があります。これらの名前のいくつかは非形式的に導入してきました。図41は慣習の要約を示します。

```
+-------------------------------------------------+
| Figure 41: Syntactic naming conventions         |
|                                                 |
|; function application:                         |
| (function argument... argument)                |
|                                                 |
|; function definition:                          |
| (define (function-name parameter... parameter) |
|   function-body)                                |
|                                                 |
|; conditional expression:                       |
| (cond                                           |
|   cond-clause                                   |
|...                                           |
|   cond-clause)                                  |
|                                                 |
|; cond clause                                   |
| [condition answer]                              |
+-------------------------------------------------+
```

図41の用語に加えて、定義の第2成分を **関数ヘッダ (function header)** と呼びます。それに応じて、式の成分は **関数本体 (function body)** と呼ばれます。プログラミング言語を数学の一形態と考える人々は、ヘッダを **左辺 (left-hand side)**、本体を **右辺 (right-hand side)** と呼びます。時折、関数適用における引数を **実引数 (actual arguments)** と呼ぶこともあります。以上。


## BSL の意味 (BSL Meaning)

キーボードのリターンキーを押して DrRacket に式の評価を依頼すると、DrRacket は算数と代数の法則を使って値を求めます。これまでに扱った BSL の変種については、図39が文法的に値とは何かを定義しています——値の集合は、すべての式の部分集合にすぎません。この集合には真偽値 (Boolean)、文字列 (String)、画像 (Image) が含まれます。

評価の規則は2つのカテゴリに分かれます。無限個の規則——算術の規則のようなもの——が、プリミティブ操作を値に適用した結果の値の求め方を説明します：

```racket
(+ 1 1) == 2
(- 2 1) == 1
...
```

`==` は、BSL の計算法則に従って2つの式が等しいことを表すことを思い出してください。しかし BSL の算術は単なる数値の処理より一般的です。真偽値や文字列などを扱う規則も含まれます：

```racket
(not #true)        == #false
(string=? "a" "a") == #true
...
```

そして代数と同様に、等しいものは常に等しいもので置き換えられます。図42に計算の例があります。

```
+----------------------------------------------------------+
| Figure 42: Replacing equals by equals                    |
|                                                          |
| (boolean? (= (string-length (string-append "h" "w"))     |
|           (+ 1 3)))                                      |
| ==                                                       |
| (boolean? (= (string-length (string-append "h" "w")) 4)) |
| ==                                                       |
| (boolean? (= (string-length "hw") 4))                    |
| ==                                                       |
| (boolean? (= 2 4))                                       |
| ==                                                       |
| (boolean? #false)                                        |
| == #true                                                 |
+----------------------------------------------------------+
```

第二に、関数を引数に適用することを理解するために、代数からの規則が必要です。プログラムに次の定義が含まれているとします：

```racket
(define (f x-1... x-n)
  f-body)
```

すると、関数適用は次の法則に支配されます：

```racket
(f v-1... v-n) == f-body
; with all occurrences of x-1... x-n
; replaced with v-1... v-n, respectively
```

BSL のような言語の歴史のため、この規則を **ベータ (beta)** または **ベータ値 (beta-value)** 規則と呼びます。

> **注 (Note):** この規則の詳細は lambda を使った計算 (Computing with lambda) を参照してください。

この規則はできるだけ一般的に定式化されているので、具体例を見るのが最善です。定義が

```racket
(define (poly x y)
  (+ (expt 2 x) y))
```

であり、DrRacket に式 `(poly 3 5)` が与えられたとします。すると式の評価の最初のステップはベータ規則を使います：

```racket
(poly 3 5) == (+ (expt 2 3) 5)... == (+ 8 5) == 13
```

ベータに加えて、`cond` 式の値を決める規則も必要です。これらの規則は代数的ですが、標準カリキュラムの一部として明示的に教えられるとは限りません。最初の条件が `#false` のとき、最初の `cond` 行は消え、残りの行はそのまま残ります：

```racket
(cond                    == (cond
  [#false...]; first line removed
  [condition2 answer2]       [condition2 answer2]
...)...)
```

この規則の名前は **condfalse** です。こちらが **condtrue** です：

```racket
(cond                    == answer-1
  [#true answer-1]
  [condition2 answer2]
...)
```

最初の条件が `else` のときにもこの規則は適用されます。

次の評価を考えてください：

```racket
(cond
  [(zero? 3) 1]
  [(= 3 3) (+ 1 1)]
  [else 3])
==; by plain arithmetic and equals-for-equals
(cond
  [#false 1]
  [(= 3 3) (+ 1 1)]
  [else 3])
==; by rule condfalse
(cond
  [(= 3 3) (+ 1 1)]
  [else 3])

==; by plain arithmetic and equals-for-equals
(cond
  [#true (+ 1 1)]
  [else 3])
==; by rule condtrue
(+ 1 1)
```

この計算は、通常の算術の規則、等しいものの置き換え、および両方の `cond` 規則を示しています。

**練習問題 121 (Exercise 121).** 次の式をステップごとに評価せよ：

1. `(+ (* (/ 12 8) 2/3) (- 20 (sqrt 4)))`
2. `(cond [(= 0 0) #false] [(> 0 1) (string=? "a" "a")] [else (= (/ 1 0) 9)])`
3. `(cond [(= 2 0) #false] [(> 2 1) (string=? "a" "a")] [else (= (/ 1 2) 9)])`

DrRacket のステッパーで計算を確認せよ。

**練習問題 122 (Exercise 122).** プログラムに次の定義が含まれているとする：

```racket
(define (f x y)
  (+ (* 3 x) (* y y)))
```

次の式を DrRacket がどのようにステップごとに評価するかを示せ：

1. `(+ (f 1 2) (f 2 1))`
2. `(f 1 (* 2 3))`
3. `(f (f 1 (* 2 3)) 19)`

DrRacket のステッパーで計算を確認せよ。

## 意味とコンピューティング (Meaning and Computing)

DrRacket のステッパーツールは、プレ代数の授業の生徒を模倣します。あなたと違って、ステッパーはここで述べた算数と代数の法則を適用することに極めて優れており、極めて高速でもあります。

> **注 (Note):** 科学者はステッパーを DrRacket の評価機構の **モデル (model)** と呼びます。Refining Interpreters（インタプリタの洗練）は別のモデル、インタプリタを提示します。

新しい言語構成子の働きがわからないときは、ステッパーを使うことができますし、使うべきです。計算 (Computing) に関する各節はこの目的の練習を提案していますが、自分で例を作り、ステッパーに通し、なぜ特定のステップを踏むのかを熟考することもできます。

最後に、プログラムが計算した結果に驚いたときにもステッパーを使いたくなるかもしれません。この使い方でステッパーを効果的に使うには練習が必要です。例えば、しばしばプログラムをコピーして不要な部分を刈り込むことになります。しかし、この方法でステッパーをうまく使うことを一度理解すれば、この手順が実行時エラーやプログラムの論理的な誤りをはっきり説明してくれることがわかるでしょう。

## BSL のエラー (BSL Errors)

DrRacket が、ある括弧で囲まれた句が BSL に属さないと発見すると、**構文エラー (syntax error)** を通知します。完全に括弧付けされたプログラムが統語的に合法かどうかを判定するために、DrRacket は図40の文法を使い、上で説明した方針に沿って推論します。しかし、統語的に合法なプログラムのすべてが意味を持つわけではありません。

> **注 (Note):** エラーメッセージのほぼ完全な一覧は、この Intermezzo の最後の節を参照してください。

DrRacket が統語的に合法なプログラムを評価し、ある操作が誤った種類の値に使われていることを発見すると、**実行時エラー (run-time error)** を上げます。統語的に合法な式 `(/ 1 0)` を考えてください。これは数学からわかるように値を持ちません。BSL の計算は数学と一貫していなければならないので、DrRacket はエラーを通知します：

```racket
> (/ 1 0)
/:division by zero
```

もちろん、`(/ 1 0)` のような式が別の式の奥深くに入れ子になっているときにもエラーを通知します：

```racket
> (+ (* 20 2) (/ 1 (- 10 10)))
/:division by zero
```

DrRacket の振る舞いは、私たちの計算では次のように翻訳されます。値ではない式を見つけ、評価規則がこれ以上の簡約を許さないとき、計算は **行き詰まった (stuck)** と言います。この行き詰まりの概念が実行時エラーに対応します。例えば、上の式の値を計算すると行き詰まり状態に至ります：

```racket
(+ (* 20 2) (/ 1 (- 10 10)))
==
(+ (* 20 2) (/ 1 0))
==
(+ 40 (/ 1 0))
```

この計算が示すのは、DrRacket がエラーを通知するときに行き詰まった式の文脈を取り除くということです。この具体例では、行き詰まった式 `(/ 1 0)` への 40 の加算を取り除きます。

入れ子になった行き詰まり式のすべてがエラー通知に終わるわけではありません。プログラムに次の定義が含まれているとします：

```racket
(define (my-divide n)
  (cond
    [(= n 0) "inf"]
    [else (/ 1 n)]))
```

ここで `my-divide` を 0 に適用すると、DrRacket は次のように計算します：

```racket
(my-divide 0)
==
(cond
  [(= 0 0) "inf"]
  [else (/ 1 0)])
```

網掛けの部分式の評価がそれを示唆するとしても、関数がいまゼロ除算エラーを通知すると言うのは明らかに誤りです。理由は `(= 0 0)` が `#true` に評価され、したがって2番目の `cond` 節は何の役割も果たさないからです：

```racket
(my-divide 0)
==
(cond
  [(= 0 0) "inf"]
  [else (/ 1 0)])
==
(cond
  [#true "inf"]
  [else (/ 1 0)])
== "inf"
```

幸い、私たちの評価法則はこれらの状況を自動的に処理します。法則がいつ適用されるかを覚えておくだけでよいのです。例えば、

```racket
(+ (* 20 2) (/ 20 2))
```

では、乗算や除算の前に加算は行えません。同様に、

```racket
(cond
  [(= 0 0) "inf"]
  [else (/ 1 0)])
```

の網掛けの除算は、対応する行が `cond` の最初の条件になるまで、完全な `cond` 式の代わりにはなりません。

経験則として、次を心に留めておくのが最善です：

> 評価の準備ができた、最も外側で最も左の入れ子式を常に選べ。

この指針は単純に見えるかもしれませんが、BSL の結果を常に説明します。

場合によっては、プログラマもエラーを上げる関数を定義したいことがあります。入力エラー (Input Errors) からのチェック付きバージョン `area-of-disk` を思い出してください：

```racket
(define (checked-area-of-disk v)
  (cond
    [(number? v) (area-of-disk v)]
    [else (error "number expected")]))
```

ここで `checked-area-of-disk` を文字列に適用することを想像してください：

```racket
(- (checked-area-of-disk "a")
   (checked-area-of-disk 10))
==
(- (cond
     [(number? "a") (area-of-disk "a")]
     [else (error "number expected")])
   (checked-area-of-disk 10))
==
(- (cond
     [#false (area-of-disk "a")]
     [else (error "number expected")])
    (checked-area-of-disk 10))
==
(- (error "number expected")
   (checked-area-of-disk 10))
```

この時点で2番目の式を評価しようと試みるかもしれませんが、その結果がおよそ 314 だとわかったとしても、計算は最終的に `error` 式を扱わねばならず、それは行き詰まり式と同じです。要するに、計算は次で終わります：

```racket
(error "number expected")
```


## ブール式 (Boolean Expressions)

現在の BSL の定義は `or` と `and` 式を省略しています。これらを追加することは、新しい言語構成子をどう学ぶかのケーススタディになります。まず構文を理解し、次に意味論を理解しなければなりません。

こちらが改訂された式の文法です：

```
+------+--+---+--+-----------------+
| expr |  | = |  |...             |
+------+--+---+--+-----------------+
|      |  | | |  | (and expr expr) |
|      |  | | |  | (or expr expr)  |
+------+--+---+--+-----------------+
```

この文法は、`and` と `or` がキーワードであり、それぞれに2つの式が続くことを述べています。それらは関数適用ではありません。

なぜ `and` と `or` が BSL 定義の関数ではないのかを理解するには、まずその語用論を見なければなりません。`(/ 1 n)` が `r` であるかどうかを判定する条件を定式化する必要があるとします：

```racket
(define (check n r)
  (and (not (= n 0)) (= (/ 1 n) r)))
```

条件を `and` の組み合わせとして定式化します。なぜなら、たまたま 0 で割りたくないからです。ここで `check` を 0 と 1/5 に適用しましょう：

```racket
(check 0 1/5)
== (and (not (= 0 0)) (= (/ 1 0) 1/5))
```

もし `and` が普通の操作であれば、両方の部分式を評価しなければならず、そうするとエラーが引き起こされます。代わりに、`and` は最初の式が `#false` のとき単に2番目の式を評価しません。つまり、`and` は評価を **短絡 (short-circuits)** します。

`and` と `or` の評価規則を定式化するのは簡単でしょう。意味を説明する別の方法は、他の式へ翻訳することです：

> **注 (Note):** `expr-2` が真偽値に評価されることを確実にするため、これらの省略形は単に `expr-2` の代わりに `(if expr-2 #true #false)` を使うべきです。ここではこの詳細を省略します。

> `(and expr-1 expr-2)` は `(cond [expr-1 expr-2] [else #false])` の省略です

そして

> `(or expr-1 expr-2)` は `(cond [expr-1 #true] [else expr-2])` の省略です

したがって、`and` や `or` 式の評価の仕方に疑いがあるときは、上の同値を使って計算してください。しかし、これらの操作を直感的に理解していると信じており、それでほぼ常に十分です。

**練習問題 123 (Exercise 123).** `if` の使用は別の意味で驚かせたかもしれません。なぜならこの Intermezzo は他の場所でこの形に言及していないからです。要するに、Intermezzo は説明のない形で `and` を説明しているように見えます。この時点では、`if` を `cond` の省略形として直感的に理解していることに頼っています。次を `cond` 式に書き換えられることを示す規則を書きなさい。

```racket
(if expr-test expr-then expr-else)
```

## 定数定義 (Constant Definitions)

プログラムは関数定義だけでなく定数定義からも成りますが、これらは最初の文法には含まれていませんでした。そこで定数定義を含む拡張文法を示します：

> definition = ... | (define name expr)

定数定義の形は関数定義の形に似ています。キーワード `define` は定数定義を式から区別しますが、関数定義との区別はしません。そのためには、人間の読者が定義の第2成分を見なければなりません。

> **注 (Note):** 実のところ、DrRacket には関数定義を扱う別の方法もあります。無名関数 (Nameless Functions) を参照してください。

次に、定数定義が何を意味するかを理解しなければなりません。右辺がリテラル定数である定数定義、例えば

```racket
(define RADIUS 5)
```

では、変数はその値の単なる省略形です。評価中に DrRacket が `RADIUS` に出会うところではどこでも、それを 5 で置き換えます。

右辺がきちんとした式である定義、例えば

```racket
(define DIAMETER (* 2 RADIUS))
```

では、直ちにその式の値を求めなければなりません。この過程は、この定数定義より前にある定義をすべて使います。したがって、

```racket
(define RADIUS 5)
(define DIAMETER (* 2 RADIUS))
```

は次と等価です：

```racket
(define RADIUS 5)
(define DIAMETER 10)
```

この過程は関数定義が関与するときにも働きます：

```racket
(define RADIUS 10)
(define DIAMETER (* 2 RADIUS))
(define (area r) (* 3.14 (* r r)))
(define AREA-OF-RADIUS (area RADIUS))
```

DrRacket がこの定義の列をステップ実行するとき、まず `RADIUS` が 10 を、`DIAMETER` が 20 を表し、`area` が関数の名前であることを判定します。最後に `(area RADIUS)` を 314 に評価し、`AREA-OF-RADIUS` をその値と関連付けます。

定数定義と関数定義を混ぜると、新しい種類の実行時エラーも生じます。次のプログラムを見てください：

```racket
(define RADIUS 10)
(define DIAMETER (* 2 RADIUS))
(define AREA-OF-RADIUS (area RADIUS))
(define (area r) (* 3.14 (* r r)))
```

これは上のものと最後の2つの定義が入れ替わっている点を除いて同じです。最初の2つの定義については、評価は前と同様に進みます。しかし3つ目については評価がうまくいきません。過程は `(area RADIUS)` の評価を要求します。`RADIUS` の定義はこの式より前にありますが、`area` の定義にはまだ出会っていません。このプログラムを DrRacket で評価すると、「this function is not defined」（この関数は定義されていない）と説明するエラーが出ます。したがって、定数定義の中で関数を使うのは、それらが定義されているとわかっているときに限るよう注意してください。

**練習問題 124 (Exercise 124).** 次のプログラムをステップごとに評価せよ：

```racket
(define PRICE 5)
(define SALES-TAX (* 0.08 PRICE))
(define TOTAL (+ PRICE SALES-TAX))
```

次のプログラムの評価はエラーを通知するか？

```racket
(define COLD-F 32)
(define COLD-C (fahrenheit->celsius COLD-F))
(define (fahrenheit->celsius f)
 (* 5/9 (- f 32)))
```

次のはどうか？

```racket
(define LEFT -100)
(define RIGHT 100)
(define (f x) (+ (* 5 (expt x 2)) 10))
(define f@LEFT (f LEFT))
(define f@RIGHT (f RIGHT))
```

DrRacket のステッパーで計算を確認せよ。

## 構造型定義 (Structure Type Definitions)

想像できるように、`define-struct` は最も複雑な BSL 構成子です。そのため説明を最後に残しました。文法は次のとおりです：

> definition = ... | (define-struct name [name ...])

構造型定義は定義の第3の形です。キーワードが関数定義とも定数定義とも区別します。

簡単な例です：

```racket
(define-struct point [x y z])
```

`point`、`x`、`y`、`z` は変数であり、括弧は文法パターンに従って置かれているので、これは構造型の適切な定義です。対照的に、次の2つの括弧付き文

```racket
(define-struct [point x y z])
(define-struct point x y z)
```

は非合法な定義です。なぜなら `define-struct` の後に単一の変数名と、括弧内の変数の列が続いていないからです。

`define-struct` の構文は素直ですが、その意味を評価規則で書き下ろすのは難しいです。何度か述べたように、`define-struct` 定義は一度にいくつかの関数を定義します：コンストラクタ、いくつかのセレクタ、および述語です。したがって

```racket
(define-struct c [s-1... s-n])
```

の評価は、プログラムに次の関数を導入します：

1. `make-c`：コンストラクタ；
2. `c-s-1` … `c-s-n`：一連のセレクタ；および
3. `c?`：述語。

これらの関数は `+`、`-`、`*` と同じ地位を持ちます。しかしこれらの新しい関数を支配する規則を理解する前に、値の定義に戻らなければなりません。結局のところ、`define-struct` の目的の1つは、既存のすべての値と区別される値のクラスを導入することだからです。

端的に言えば、`define-struct` の使用は値の宇宙を拡張します。まず、それは複数の値を1つに複合する構造体も含むようになります。プログラムに `define-struct` 定義が含まれると、その評価は値の定義を次のように変更します：

> 値とは次のいずれかである：数、真偽値、文字列、画像、または構造体値：
> `(make-c _value-1 ... _value-n)`（構造型 `c` が定義されていると仮定）

例えば、`point` の定義は次の形の値を追加します：

```racket
(make-point 1 2 -1)
(make-point "one" "hello" "world")
(make-point 1 "one" (make-point 1 2 -1))
...
```

これで新しい関数の評価規則を理解する立場になりました。`c-s-1` が `c` 構造体に適用されると、値の第1成分を返します。同様に、第2セレクタは第2成分を取り出し、第3セレクタは第3成分を、といった具合です。新しいデータコンストラクタとセレクタの関係は、BSL の規則に追加される n 個の等式で最もよく特徴づけられます：

```racket
(c-s-1 (make-c V-1... V-n)) == V-1
(c-s-n (make-c V-1... V-n)) == V-n
```

実行中の例では、次の具体的な等式が得られます：

```racket
(point-x (make-point V U W)) == V
(point-y (make-point V U W)) == U
(point-z (make-point V U W)) == W
```

DrRacket が `(point-y (make-point 3 4 5))` を見ると、式を 4 で置き換えます。一方 `(point-x (make-point (make-point 1 2 3) 4 5))` は `(make-point 1 2 3)` に評価されます。

述語 `c?` は任意の値に適用できます。値が種類 `c` なら `#true` を、そうでなければ `#false` を返します。両方の部分を2つの等式に翻訳できます：

```racket
(c? (make-c V-1... V-n)) == #true
(c? V)                    == #false
```

ただし `V` は `make-c` で構築されていない値です。再び、等式は例で理解するのが最善です：

```racket
(point? (make-point U V W)) == #true
(point? X)                  == #false
```

ただし `X` は値だが `point` 構造体ではない場合です。

**練習問題 125 (Exercise 125).** 合法な文と非合法な文を区別せよ：

1. `(define-struct oops [])`
2. `(define-struct child [parents dob date])`
3. `(define-struct (child person) [dob date])`

なぜ合法または非合法かを説明せよ。

**練習問題 126 (Exercise 126).** 定義領域に次の構造型定義があるとして、次の式のうち値であるものを特定せよ：

```racket
(define-struct point [x y z])
(define-struct none  [])
```

1. `(make-point 1 2 3)`
2. `(make-point (make-point 1 2 3) 4 5)`
3. `(make-point (+ 1 2) 3 4)`
4. `(make-none)`
5. `(make-point (point-x (make-point 1 2 3)) 4 5)`

なぜ値である／でないかを説明せよ。

**練習問題 127 (Exercise 127).** プログラムに次が含まれるとする：

```racket
(define-struct ball [x y speed-x speed-y])
```

次の式を評価した結果を予測せよ：

1. `(number? (make-ball 1 2 3 4))`
2. `(ball-speed-y (make-ball (+ 1 2) (+ 3 3) 2 3))`
3. `(ball-y (make-ball (+ 1 2) (+ 3 3) 2 3))`
4. `(ball-x (make-posn 1 2))`
5. `(ball-speed-y 5)`

対話領域とステッパーで予測を確認せよ。

```
+-----------------------------------------------------------------+
| Figure 43: BSL, full grammar                                    |
|                                                                 |
| +------------+--+---+--+--------------------------------------+ |
| | def-expr   |  | = |  | definition                           | |
| +------------+--+---+--+--------------------------------------+ |
| |            |  | | |  | expr                                 | |
| |            |  | | |  | test-case                            | |
| | definition |  | = |  | (define (name variable variable...… | |
| |            |  | | |  | (define name expr)                   | |
| |            |  | | |  | (define-struct name [name...])      | |
| | expr       |  | = |  | (name expr expr...)                 | |
| |            |  | | |  | (cond [expr expr]... [expr expr])   | |
| |            |  | | |  | (cond [expr expr]... [else expr])   | |
| |            |  | | |  | (and expr expr expr...)             | |
| |            |  | | |  | (or expr expr expr...)              | |
| |            |  | | |  | name                                 | |
| |            |  | | |  | number                               | |
| |            |  | | |  | string                               | |
| |            |  | | |  | image                                | |
| | test-case  |  | = |  | (check-expect expr expr)             | |
| |            |  | | |  | (check-within expr expr expr)        | |
| |            |  | | |  | (check-member-of expr expr...)      | |
| |            |  | | |  | (check-range expr expr expr)         | |
| |            |  | | |  | (check-error expr)                   | |
| |            |  | | |  | (check-random expr expr)             | |
| |            |  | | |  | (check-satisfied expr name)          | |
| +------------+--+---+--+--------------------------------------+ |
+-----------------------------------------------------------------+
```


## BSL のテスト (BSL Tests)

図43は BSL 全体に加え、いくつかのテスト形式を示しています。

テスト式の一般的な意味は説明しやすいです。*RUN* ボタンをクリックすると、DrRacket はすべてのテスト式を集め、現れた順序を保ったままプログラムの末尾へ移します。その後、定義領域の内容を評価します。各テストはその各片を評価し、何らかの述語を介して期待される結果と比較します。それに加えて、テストは統計とテスト失敗の表示方法に関する情報を集めるために DrRacket と通信します。

詳細はこれらのテスト形式のドキュメントを読んでください。以下は説明的な例です：

```racket
; check-expect compares the outcome and the expected value with equal?
(check-expect 3 3)

; check-member-of compares the outcome and the expected values with equal?
; if one of them yields #true, the test succeeds
(check-member-of "green" "red" "yellow" "green")

; check-within compares the outcome and the expected value with a predicate
;  like equal? but allows for a tolerance of epsilon for each inexact number
(check-within (make-posn #i1.0 #i1.1) (make-posn #i0.9 #i1.2) 0.2)

; check-range is like check-within
; but allows for a specification of an interval
(check-range 0.9 #i0.6 #i1.0)

; check-error checks whether an expression signals (any) error
(check-error (/ 1 0))

; check-random evaluates the sequences of calls to random in the
; two expressions such that they yield the same number
(check-random (make-posn (random 3) (random 9))
              (make-posn (random 3) (random 9)))

; check-satisfied determines whether a predicate produces #true
; when applied to the outcome, that is, whether outcome has a certain property
(check-satisfied 4 even?)
```

上のテストはすべて成功します。本書の残りの部分は、必要に応じてこれらのテスト形式を再導入します。

**練習問題 128 (Exercise 128).** 次のテストを DrRacket の定義領域にコピーせよ：

```racket
(check-member-of "green" "red" "yellow" "grey")
(check-within (make-posn #i1.0 #i1.1)
              (make-posn #i0.9 #i1.2)  0.01)
(check-range #i0.9 #i0.6 #i0.8)
(check-random (make-posn (random 3) (random 9))
              (make-posn (random 9) (random 3)))
(check-satisfied 4 odd?)
```

それらがすべて失敗することを検証し、なぜかを説明せよ。

## BSL のエラーメッセージ (BSL Error Messages)

BSL プログラムは多くの種類の構文エラーを通知することがあります。BSL とそのエラー報告は、誤りを犯すのが当たり前の初心者向けに作られていますが、メッセージ自体には慣れが必要です。

以下では出会うかもしれないエラーメッセージの種類をいくつか示します。各一覧の各項目は3つの部分から成ります：

- エラーメッセージを通知するコード片；
- エラーメッセージ；および
- 誤りを直す提案を伴う説明。

次の例を考えてください。これはおそらくこれまでに見る最悪のエラーメッセージです：

```
+--------------------------------------------------+--------------------------------------------------+
| (define (absolute n) ⏎ (cond ⏎ [< 0 (- n)] ⏎ [e… | A cond expression consists of the keyword follo… |
+--------------------------------------------------+--------------------------------------------------+
| (define (absolute n) ⏎ (cond ⏎ [< 0 (- n)] ⏎ [e… |                                                  |
| (define (absolute n)                             |                                                  |
|   (cond                                          |                                                  |
|     [< 0 (- n)]                                  |                                                  |
|     [else n]))                                   |                                                  |
| <: expected a function call, but there is no op… |                                                  |
+--------------------------------------------------+--------------------------------------------------+
```

関数定義内の `<` の強調表示がエラーを指し示しています。定義の下に、*RUN* をクリックしたときに DrRacket が対話ウィンドウに提示するエラーメッセージが見えます。右のエラー説明を調べて、このやや自己矛盾したメッセージへの対処を理解してください。そして、他のどのエラーメッセージもこれほど不透明でないことを安心してよいです。

したがって、エラーが出て助けが必要なときは、適切な図を見つけ、一致する項目を探し、その完全な項目を研究してください。

*BSL における関数適用に関するエラーメッセージ (Error Messages about Function Applications in BSL)*

定義領域に次だけが含まれていると仮定します：

```racket
; Number Number -> Number
; finds the average of x and y
(define (average x y)
  (/ (+ x y)
     2))
```

*RUN* ボタンを押します。すると以下のエラーメッセージに出会うかもしれません。

```
+--------------------------------------+--------------------------------------------------+
| (f 1)f: this function is not defined | The application names f as the function, ⏎ and … |
+--------------------------------------+--------------------------------------------------+
| (f 1)                                |                                                  |
| `f: this function is not defined`    |                                                  |
+--------------------------------------+--------------------------------------------------+
```

```
+--------------------------------------------------+--------------------------------------------------+
| (1 3 "three" #true)function call: expected a fu… | An open parenthesis must always be followed by … |
+--------------------------------------------------+--------------------------------------------------+
| (1 3 "three" #true)                              |                                                  |
| function call: expected a function after the ⏎ … |                                                  |
+--------------------------------------------------+--------------------------------------------------+
```

```
+--------------------------------------------------+--------------------------------------------------+
| (average 7)average: expects 2 arguments, but fo… | This function call applies average to ⏎ one arg… |
+--------------------------------------------------+--------------------------------------------------+
| (average 7)                                      |                                                  |
| `average: expects 2 arguments, but found only 1` |                                                  |
+--------------------------------------------------+--------------------------------------------------+
```

```
+--------------------------------------------------+--------------------------------------------------+
| (average 1 2 3)average: expects 2 arguments, bu… | Here average is applied to three numbers instea… |
+--------------------------------------------------+--------------------------------------------------+
| (average 1 2 3)                                  |                                                  |
| `average: expects 2 arguments, but found 3`      |                                                  |
+--------------------------------------------------+--------------------------------------------------+
```

```
+--------------------------------------------------+--------------------------------------------------+
| (make-posn 1)make-posn: expects 2 arguments, bu… | Functions defined by BSL must also be applied t… |
+--------------------------------------------------+--------------------------------------------------+
| (make-posn 1)                                    |                                                  |
| `make-posn: expects 2 arguments, but found only… |                                                  |
+--------------------------------------------------+--------------------------------------------------+
```

*BSL における誤ったデータに関するエラーメッセージ (Error Messages about Wrong Data in BSL)*

以下のエラーシナリオでも、定義領域に次が含まれていると仮定します：

```racket
; Number Number -> Number
; find the average of x and y
(define (average x y)...)
```

`posn` はあらかじめ定義された構造型であることを思い出してください。

```
+--------------------------------------------------+--------------------------------------------------+
| (posn-x #true)posn-x: expects a posn, given #tr… | A function must be applied to the arguments it … |
+--------------------------------------------------+--------------------------------------------------+
| (posn-x #true)                                   |                                                  |
| `posn-x: expects a posn, given #true`            |                                                  |
+--------------------------------------------------+--------------------------------------------------+
```

```
+--------------------------------------------------+--------------------------------------------------+
| (average "one" "two")+: expects a number as 1st… | A function defined to consume two ⏎ Numbers mus… |
+--------------------------------------------------+--------------------------------------------------+
| (average "one" "two")                            |                                                  |
| `+: expects a number as 1st argument, given "on… |                                                  |
+--------------------------------------------------+--------------------------------------------------+
```

*BSL における条件式に関するエラーメッセージ (Error Messages about Conditionals in BSL)*

今度は定義領域に定数定義があることを想定します：

```
+--------------------------------------------------+
|; N in [0,1,...10) ⏎ (define 0-to-9 (random 10)) |
+--------------------------------------------------+
|;N in [0,1,...10)                                |
| (define 0-to-9 (random 10))                      |
+--------------------------------------------------+
```

```
+--------------------------------------------------+--------------------------------------------------+
| (cond ⏎ [(>= 0-to-9 5)])                         | Every cond clause must consist of exactly two p… |
+--------------------------------------------------+--------------------------------------------------+
| (cond ⏎ [(>= 0-to-9 5)])                         |                                                  |
| (cond                                            |                                                  |
|   [(>= 0-to-9 5)])                               |                                                  |
| cond: expected a clause with a question and an … |                                                  |
+--------------------------------------------------+--------------------------------------------------+
```

```
+--------------------------------------------------+--------------------------------------------------+
| (cond ⏎ [(>= 0-to-9 5) ⏎ "head" ⏎ "tail"])       | In this case, the cond clause consists of three… |
+--------------------------------------------------+--------------------------------------------------+
| (cond ⏎ [(>= 0-to-9 5) ⏎ "head" ⏎ "tail"])       |                                                  |
| (cond                                            |                                                  |
|   [(>= 0-to-9 5)                                 |                                                  |
| "head"                                           |                                                  |
|    "tail"])                                      |                                                  |
| cond: expected a clause with a question and an … |                                                  |
+--------------------------------------------------+--------------------------------------------------+
```

```
+--------------------------------------------------+--------------------------------------------------+
| (cond)cond: expected a clause after cond, but n… | A conditional must come with at least one cond … |
+--------------------------------------------------+--------------------------------------------------+
| (cond)                                           |                                                  |
| `cond: expected a clause after cond, but nothin… |                                                  |
+--------------------------------------------------+--------------------------------------------------+
```

*BSL における関数定義に関するエラーメッセージ (Error Messages about Function Definitions in BSL)*

以下のエラーシナリオはすべて、コード片を定義領域に置き *RUN* を押したと仮定します。

```
+--------------------------------------------------+--------------------------------------------------+
| (define f(x) x)define: expected only one expres… | A definition consist of three parts: the ⏎ defi… |
+--------------------------------------------------+--------------------------------------------------+
| (define f(x) x)                                  |                                                  |
| define: expected only one expression after the … |                                                  |
+--------------------------------------------------+--------------------------------------------------+
```

```
+--------------------------------------------------+--------------------------------------------------+
| (define (f x x) x)define: found a variable that… | The sequence of parameters in a function ⏎ defi… |
+--------------------------------------------------+--------------------------------------------------+
| (define (f x x) x)                               |                                                  |
| `define: found a variable that is used more tha… |                                                  |
+--------------------------------------------------+--------------------------------------------------+
```

```
+--------------------------------------------------+--------------------------------------------------+
| (define (g) x)define: expected at least one var… | In BSL a function header must contain at ⏎ leas… |
+--------------------------------------------------+--------------------------------------------------+
| (define (g) x)                                   |                                                  |
| define: expected at least one variable after ⏎ … |                                                  |
+--------------------------------------------------+--------------------------------------------------+
```

```
+--------------------------------------------------+--------------------------------------------------+
| (define (f (x)) x)define: expected a variable, … | The function header contains ⏎ (x), which is no… |
+--------------------------------------------------+--------------------------------------------------+
| (define (f (x)) x)                               |                                                  |
| `define: expected a variable, but found a part`  |                                                  |
+--------------------------------------------------+--------------------------------------------------+
```

```
+--------------------------------------------------+--------------------------------------------------+
| (define (h x y) x y)define: expected only one e… | This function definition comes with two ⏎ expre… |
+--------------------------------------------------+--------------------------------------------------+
| (define (h x y) x y)                             |                                                  |
| define: expected only one expression for the fu… |                                                  |
+--------------------------------------------------+--------------------------------------------------+
```

*BSL における構造型定義に関するエラーメッセージ (Error Messages about Structure Type Definitions in BSL)*

今度は構造型定義を定義領域に置き、*RUN* を押して次のエラーを試す必要があります。

```
+--------------------------------------------------+--------------------------------------------------+
| (define-struct [x]) ⏎ (define-struct [x y])      | A structure type definition consists of three ⏎… |
+--------------------------------------------------+--------------------------------------------------+
| (define-struct [x]) ⏎ (define-struct [x y])      |                                                  |
| (define-struct [x])                              |                                                  |
| (define-struct [x y])                            |                                                  |
| define-struct: expected the structure name afte… |                                                  |
+--------------------------------------------------+--------------------------------------------------+
```

```
+--------------------------------------------------+--------------------------------------------------+
| (define-struct x ⏎ [y y])                        | The sequence of field names in a structure ⏎ ty… |
+--------------------------------------------------+--------------------------------------------------+
| (define-struct x ⏎ [y y])                        |                                                  |
| (define-struct x                                 |                                                  |
|   [y y])                                         |                                                  |
| `define-struct: found a field name that is used… |                                                  |
+--------------------------------------------------+--------------------------------------------------+
```

```
+--------------------------------------------------+--------------------------------------------------+
| (define-struct x y) ⏎ (define-struct x y z)      | These structure type definitions lack the ⏎ seq… |
+--------------------------------------------------+--------------------------------------------------+
| (define-struct x y) ⏎ (define-struct x y z)      |                                                  |
| (define-struct x y)                              |                                                  |
| (define-struct x y z)                            |                                                  |
| define-struct: expected at least one field name… |                                                  |
+--------------------------------------------------+--------------------------------------------------+
```

---

**免責:** 本ファイルは HtDP/2e の個人学習用 AI 意訳であり、公式翻訳ではありません。コードフェンス内は英語原本と一致させています。

