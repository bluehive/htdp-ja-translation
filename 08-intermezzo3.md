# Intermezzo 3: Scope and Abstraction（スコープと抽象化）

**原本:** `extracted/original_markdown_08_i3-4.md`

### 目次

- Scope（スコープ）
- ISL for Loops（ISL のループ）
- Pattern Matching（パターンマッチ）

前部では local と lambda を非形式的に説明して済ませたが、こうした抽象化機構を導入するには、議論を進めるための追加の用語が本当に必要になる。とくに、プログラム内の領域を区切ったり、変数の特定の出現を指したりする語が要る。

このインターメッツォは、新しい用語——スコープ、束縛変数、被束縛変数——を定義する節から始まる。そしてこの新しい能力をすぐ使って、プログラミング言語によく見られる2つの抽象化機構を導入する。`for` ループとパターンマッチである。前者は map、build-list、andmap などの関数の代替であり、後者は本書の最初の3部の関数における条件式を抽象化する。どちらも関数の定義だけでなく、まったく新しい言語構成子の作成を要する。つまり、プログラマが通常、設計して自分の語彙に加えられるものではない。

## Scope（スコープ）

次の2つの定義を考えよ：

```racket
(define (f x) (+ (* x x) 25))
(define (g x) (+ (f (+ x 1)) (f (- x 1))))
```

明らかに、f における x の出現は、g の定義における x の出現とはまったく無関係である。網掛けの出現を体系的に y に置き換えても、関数はまったく同じ結果を計算する。要するに、網掛けの x の出現は f の定義の内部でのみ意味を持ち、他のどこでも意味を持たない。

同時に、f における x の最初の出現は、他の出現とは異なる。`(fn)` を評価するとき、f の出現は完全に消え、x の出現は n に置き換えられる。これら2種類の変数出現を区別するため、関数ヘッダの x を**束縛出現 (binding occurrence)**、関数本体のものを**被束縛出現 (bound occurrences)** と呼ぶ。また、x の束縛出現が f の本体におけるすべての x の出現を束縛する、とも言う。実際、プログラミング言語を研究する人々は、束縛出現が働く領域に名前さえ付けており、それが**字句スコープ (lexical scope)** である。

f と g の定義はさらに2つの名前を束縛する：f と g である。それらのスコープは**トップレベル・スコープ (top-level scope)** と呼ばれる。スコープは入れ子になっていると考えるからである（後述）。

**自由出現 (free occurrence)** という語は、いかなる束縛出現も持たない変数に当てはまる。それは定義のない名前、すなわち言語もそのティーチパックもプログラムも、何らかの値と結び付けていない名前である。たとえば、上のプログラムだけを定義領域に置いて実行し、対話領域のプロンプトで f、g、x を入力すると、最初の2つは定義されており、最後の1つは定義されていないことがわかる：

```racket
> f
f
> g
g
> x
x:this variable is not defined
```

字句スコープの説明は、f の定義の図的表現を示唆する：

> **注意:** DrRacket の
「構文チェック (Check Syntax)」機能は、このような図を描く。

> [image: pict_129.png]

トップレベル・スコープの矢印図は次のとおりである：

> [image: pict_130.png]

f のスコープには、その定義の上と下のすべての定義が含まれることに注意せよ。最初の出現の上の黒丸は、それが束縛出現であることを示す。束縛出現から被束縛出現への矢印は、値の流れを示唆する。束縛出現の値が分かると、被束縛出現はそこから値を受け取る。

同様の考え方で、これらの図は名前の付け替えがどう働くかも説明する。関数パラメータの名前を付け替えたいなら、スコープ内のすべての被束縛出現を探し、それらを置き換える。たとえば、上のプログラムで f の x を y に付け替えると、

```racket
(define (f x) (+ (* x x) 25))
(define (g x) (+ (f (+ x 1)) (f (- x 1))))
```

は x の出現のうち2つだけが変わる：

```racket
(define (f y) (+ (* y y) 25))
(define (g x) (+ (f (+ x 1)) (f (- x 1))))
```

**Exercise 300.** 次は単純な ISL+ プログラムである：

```racket
(define (p1 x y)
  (+ (* x y)
     (+ (* 2 x)
        (+ (* 2 y) 22))))

(define (p2 x)
  (+ (* 55 x) (+ x 11)))

(define (p3 x)
  (+ (p1 x 0)
     (+ (p1 x 1) (p2 x))))
```

p1 の x パラメータから、そのすべての被束縛出現へ矢印を描け。p1 から p1 のすべての被束縛出現へ矢印を描け。結果を DrRacket の *CHECK SYNTAX* 機能で確かめよ。

トップレベルの関数定義とは対照的に、local 内の定義のスコープは限られている。具体的には、局所定義のスコープは *その* local 式である。local 式内の補助関数 f の定義を考えよ。それは local 式の内部のすべての出現を束縛するが、外側に現れるものは束縛しない：

> [image: pict_131.png]

local の外側の2つの出現は、f の局所定義によっては束縛されない。いつものように、関数定義のパラメータは、局所であれそうでなかれ、その関数の本体でのみ束縛される。

関数名や関数パラメータのスコープはテキスト上の領域なので、スコープを示すために箱の図も描かれる。より正確には、パラメータについては関数の本体の周りに箱が描かれる：

> [image: pict_132.png]

local の場合、箱は式全体の周りに描かれる：

> [image: pict_133.png]

この例では、箱は f と g の定義のスコープを表す。

スコープの周りに箱を描くと、local 式の内部で関数の名前を再利用することが何を意味するかも容易に理解できる：

> [image: pict_134.png]

灰色の箱は内側の f の定義のスコープを表し、白い箱は外側の f の定義のスコープである。したがって、灰色の箱内の f のすべての出現は内側の local を指し、白い箱のうち灰色を除いた部分の出現は外側の local の定義を指す。言い換えれば、灰色の箱は外側の f の定義のスコープにおける**穴 (hole)** である。

穴はパラメータ定義のスコープにも現れ得る：

> [image: pict_135.png]

この関数では、パラメータ x が2回使われている：f と g についてである。後者のスコープは、したがって前者のスコープにおける穴である。

一般に、同じ名前が関数内に複数回現れるとき、対応するスコープを表す箱は決して重ならない。箱が入れ子になる場合もあり、それが穴を生じる。それでも、絵は常に、より小さくより小さな入れ子の箱の階層である。

> **図105: Drawing lexical scope contours for exercise 301**

```racket
(define (insertion-sort alon)
  (local ((define (sort alon)
            (cond
              [(empty? alon) '()]
              [else
               (add (first alon) (sort (rest alon)))]))
          (define (add an alon)
            (cond
              [(empty? alon) (list an)]
              [else
               (cond
                 [(> an (first alon)) (cons an alon)]
                 [else (cons (first alon)
                             (add an (rest alon)))])])))
    (sort alon)))
```


Exercise 301. 図105における sort と alon の各束縛出現のスコープの周りに箱を描け。次に、sort の各出現から適切な束縛出現へ矢印を描け。今度は図106の変種についても同じ演習を繰り返せ。この2つの関数は、名前以外に違う点があるか。

> **図106: Drawing lexical scope contours for exercise 301 (version 2)**

```racket
(define (sort alon)
  (local ((define (sort alon)
            (cond
              [(empty? alon) '()]
              [else
               (add (first alon) (sort (rest alon)))]))
          (define (add an alon)
            (cond
              [(empty? alon) (list an)]
              [else
                (cond
                  [(> an (first alon)) (cons an alon)]
                  [else (cons (first alon)
                              (add an (rest alon)))])])))
    (sort alon)))
```


**Exercise 302.** 変数の各出現は、その束縛出現から値を受け取ることを思い出そう。次の定義を考えよ：

```racket
(define x (cons 1 x))
```

網掛けの x の出現はどこで束縛されているか。この定義は関数定義ではなく定数定義なので、右辺をただちに評価する必要がある。私たちの規則によれば、右辺の値はどうあるべきか。

Functions from lambda で論じたように、lambda 式は local 式の単なる省略形である。すなわち、a-new-name が exp に現れないなら、

```racket
(lambda (x-1...  x-n) exp)
```

は次の省略形である

```racket
(local ((define (a-new-name x-1... x-n) exp))
  a-new-name)
```

この省略形の説明は次を示唆する：

```racket
(lambda (x-1...  x-n) exp)
```

は x-1,..., x-n を束縛出現として導入し、パラメータのスコープは exp である。たとえば：

> [image: pict_136.png]

もちろん、exp がさらに束縛構成子（たとえば入れ子の local 式）を含むなら、変数のスコープには穴があり得る。

**Exercise 303.** 次の3つの lambda 式それぞれについて、網掛けの x の出現からその束縛出現へ矢印を描け：

1. (lambda (x y) (+ x (* x y)))
2. (lambda (x y) (+ x (local ((define x (* y y))) (+ (* 3 x) (/ 1 x)))))
3. (lambda (x y) (+ x ((lambda (x) (+ (* 3 x) (/ 1 x))) (* y y))))

また、網掛けの各 x のスコープの箱と、必要ならスコープ内の穴も描け。

## ISL for Loops（ISL のループ）

語としては一度も触れないが、Abstraction はループを導入している。抽象的に言えば、ループは複合データを走査し、

> **注意:** 定義領域に ( require 2htdp/abstraction ) を追加するか、Language メニューから Add Teachpack を選び、Preinstalled HtDP/2e Teachpack メニューから abstraction を選べ。

1片ずつ処理する。その過程で、ループはデータも合成する。たとえば、map はリストを走査し、各項目に関数を適用し、結果をリストに集める。同様に、build-list は自然数の先行者の列（0 から (-n1) まで）を列挙し、それぞれを何らかの値に写し、やはり結果をリストに集める。

ISL+ のループは、従来の言語のループと2点で異なる。第一に、従来のループは新しいデータを直接は作らない。対照的に、map や build-list のような抽象化は、走査から新しいデータを計算することそのものである。第二に、従来の言語はしばしば固定された個数のループしか提供しない。ISL+ のプログラマは必要に応じて新しいループを定義する。言い換えれば、従来の言語はループを local や cond に類する構文構成子と見なし、その導入には語彙・文法・スコープ・意味の詳細な説明が要る。

構文構成子としてのループには、前部の関数的ループに対する2つの利点がある。一方では、その形が、関数の合成よりも意図をより直接に信号する傾向がある。他方では、言語実装は通常、構文ループを関数的ループよりコンピュータ向けの高速な命令へ翻訳する。だから、関数と関数合成を強調する関数型プログラミング言語でさえ、構文ループを提供するのが一般的である。

本節では、ISL+ のいわゆる `for` ループを導入する。目標は、従来のループを言語的構成子としてどう考えるかを示し、抽象化で組み立てたプログラムが代わりにループをどう使い得るかを示すことである。図107は、選択した `for` ループの文法を、Intermezzo 1: Beginning Student Language の BSL の文法の拡張として書き下している。どのループも式であり、すべての複合構成子と同様、キーワードで印付けされる。その後にいわゆる**内包節 (comprehension clauses)** の括弧付き列と、単一の式が続く。節はいわゆる**ループ変数 (loop variables)** を導入し、末尾の式は**ループ本体 (loop body)** である。

> **図107: ISL+ extended with for loops**

```
expr
=
...
|
(
for/list
(
clause
clause
...
)
expr
)
|
(
for*/list
(
clause
clause
...
)
expr
)
|
(
for/and
(
clause
clause
...
)
expr
)
|
(
for*/and
(
clause
clause
...
)
expr
)
|
(
for/or
(
clause
clause
...
)
expr
)
|
(
for*/or
(
clause
clause
...
)
expr
)
|
(
for/sum
(
clause
clause
...
)
expr
)
|
(
for*/sum
(
clause
clause
...
)
expr
)
|
(
for/product
(
clause
clause
...
)
expr
)
|
(
for*/product
(
clause
clause
...
)
expr
)
|
(
for/string
(
clause
clause
...
)
expr
)
|
(
for*/string
(
clause
clause
...
)
expr
)
clause
=
[
variable
expr
]
```


文法をざっと見ても、12個のループ構成子が6対になっていることがわかる：`list`、`and`、`or`、`sum`、`product`、`string` のそれぞれについて `for` と `for*` の変種がある。すべての `for` ループは節の変数を本体で束縛する。`for*` 変種は、後続の節でも変数を束縛する。次のほぼ同一のコード片が、これら2つのスコープ規則の違いを示す：

> **注意:** Racket 版のこれらのループは、ここで提示するものより多くの機能を備え、言語にはこれよりはるかに多くのループがある。

> [image: pict_137.png] [image: pict_138.png]

構文上の違いは、左が for/list を使い、右が for*/list を使うことである。スコープの点では、矢印が示すように2つは強く異なる。どちらもループ変数 width と height を導入するが、左は height の初期値に外部で定義された変数を使い、右は最初のループ変数を使う。

意味論的には、for/list 式は節内の式を評価して値の列を生成する。節の式が次のものに評価されるなら

- リストなら、その項目が列の値をなす；
- 自然数 n なら、列は 0、1、...、(-n1) からなる；そして
- 文字列なら、その1文字文字列が列の項目である。

次に、for/list は、生成された列の値にループ変数を順次束縛してループ本体を評価する。最後に、本体の値をリストに集める。for/list 式の評価は、最も短い列が尽きると止まる。

用語 ループ本体の各評価を**反復 (iteration)** と呼ぶ。同様に、ループはループ変数の値を**反復する (iterate over)** と言われる。

この説明に基づけば、0 から 9 までのリストを容易に生成できる：

```racket
> (for/list ([i 10])    i)
(list 0 1 2 3 4 5 6 7 8 9)
```

これは build-list ループと等価である：

```racket
> (build-list 10 (lambda (i) i))
(list 0 1 2 3 4 5 6 7 8 9)
```

第2の例は2つの列を「ジップ」する：

```racket
> (for/list ([i 2] [j '(a b)])    (list i j))
(list (list 0 'a) (list 1 'b))
```

比較のため、同じ式を素の ISL+ で書いたもの：

```racket
> (local ((define i-s (build-list 2 (lambda (i) i)))          (define j-s '(a b)))    (map list i-s j-s))
(list (list 0 'a) (list 1 'b))
```

最後の例は for/list を使った設計を強調する：

> **例題** enumerate を設計せよ。この関数はリストを消費し、同じ項目を相対的なインデックスと対にしたリストを生成する。

Stop! この関数を、ISL+ の抽象化を使い、体系的に設計せよ。

for/list を使えば、この問題には素直な解がある：

```racket
; [List-of X] -> [List-of [List N X]]
; pairs each item in lx with its index

(check-expect
  (enumerate '(a b c)) '((1 a) (2 b) (3 c)))

(define (enumerate lx)
  (for/list ([x lx] [ith (length lx)])
    (list (+ ith 1) x)))
```

関数の本体は for/list を使い、与えられたリストと、0 から (lengthlx)（マイナス1）までの数のリストを反復する。ループ本体はインデックス（プラス1）とリスト項目を組み合わせる。

意味論的な用語では、for*/list は列を入れ子状に反復し、for/list はそれらを並行に走査する。すなわち、for*/list 式は基本的にループの入れ子に展開される：

```racket
(for*/list ([i 2] [j '(a b)])
...)
```

は次の省略形である

```racket
(for/list ([i 2])
  (for/list ([j '(a b)])
...))
```

加えて、for*/list は入れ子のリストを、foldl と append で連結して単一のリストに集める。

**Exercise 304.** 次を評価せよ

```racket
(for/list ([i 2] [j '(a b)]) (list i j))
```

および

```racket
(for*/list ([i 2] [j '(a b)]) (list i j))
```

DrRacket の対話領域で。

for/list と for*/list のスコープの違いを意味の違いに変えて、探索を続けよう：

```racket
> (define width 2)
> (for/list ([width 3][height width])    (list width height))
(list (list 0 0) (list 1 1))
> (for*/list ([width 3][height width])    (list width height))
(list (list 1 0) (list 2 0) (list 2 1))
```

最初の対話を理解するには、for/list が2つの列を並行に走査し、短い方が尽きると止まることを思い出そう。ここでの2つの列は

> width = 0, 1, 2height = 0, 1body = (list00) (list11)

最初の2行は2つのループ変数の値を示し、それらは連動して変わる。最後の行は各反復の結果を示し、それが最初の結果と、2 を含む対が無いことを説明する。

今度はこれを for*/list と対比せよ：

> width = 0 1 2height = 0 0, 1body = (list10) (list20) (list21)

最初の行は for/list の場合と同様だが、2行目は今やセル内に数の列を表示する。for*/list の暗黙の入れ子は、各反復が特定の width の値について height を再計算し、したがって height の値の別個の列を作ることを意味する。これが、height の値の最初のセルが空である理由を説明する。結局のところ、0（含む）と 0（含まない）の間に自然数はない。最後に、入れ子の各 `for` ループは対の列を生み、それが単一の対のリストに集められる。

次の問題は、文脈における for*/list のこの使い方を示す：

> **例題** cross を設計せよ。この関数は2つのリスト l1 と l2 を消費し、これらのリストのすべての項目の対を生成する。

Stop! 既存の抽象化を使い、この関数の設計に少し時間を取れ。

cross を設計するとき、次のような表を埋めていく：

> cross 'a 'b 'c1 (list'a1) (list'b1) (list'c1)2 (list'a2) (list'b2) (list'c2)

最初の行は与えられた l1 を表示し、左端の列は l2 を示す。表の各セルは、生成すべき対の1つに対応する。

for*/list の目的はそうした対をすべて列挙することなので、for*/list による cross の定義は素直である：

```racket
; [List-of X] [List-of Y] -> [List-of [List X Y]]
; generates all pairs of items from l1 and l2

(check-satisfied (cross '(a b c) '(1 2))
                 (lambda (c) (= (length c) 6)))

(define (cross l1 l2)
   (for*/list ([x1 l1][x2 l2])
      (list x1 x2)))
```

check-expect の代わりに check-satisfied を使う。for*/list が対を生成する正確な順序を予測したくないからである。

> **図108: A compact definition of arrangements with for*/list**

```racket
; [List-of X] -> [List-of [List-of X]]
; creates a list of all rearrangements of the items in w
(define (arrangements w)
  (cond
    [(empty? w) '(())]
    [else (for*/list ([item w]
                      [arrangement-without-item
                       (arrangements (remove item w))])
            (cons item arrangement-without-item))]))

; [List-of X] -> Boolean
(define (all-words-from-rat? w)
  (and (member? (explode "rat") w)
       (member? (explode "art") w)
       (member? (explode "tar") w)))

(check-satisfied (arrangements '("r" "a" "t"))
                 all-words-from-rat?)
```


注意 図108は for*/list の別の文脈での使い方を示す。与えられたリスト内の文字の可能なすべての並べ替えを作る、という拡張設計問題のコンパクトな解を表示している。

Word Games, the Heart of the Problem がこの複雑なプログラムの適切な設計をスケッチする一方、図108は for*/list と再帰の珍しい形の合成力を使い、同じプログラムを5行の単一の関数定義として定義する。図はこれらの抽象化の力を示すにすぎない。根底にある設計については、とくに exercise 477 を見よ。終わり

> **注意:** この表現力の展示を提案してくれた Mark Engelberg に感謝する。

`.../list` 接尾辞は、ループ式がリストを作ることをはっきり信号する。加えて、ティーチパックは同様に示唆的な接尾辞を持つ `for` と `for*` ループを備える：

- `.../and` はすべての反復の値を and で集める：`>`(for/and ([i 10]) (> (- 9 i) 0))#false`>`(for/and ([i 10]) (if (>= i 0) i #false))9実用上、ループは最後に生成された値または #false を返す。
- `.../or` は `.../and` に似ているが、and の代わりに or を使う：
`>`(for/or ([i 10]) (if (= (- 9 i) 0) i #false))9`>`(for/or ([i 10]) (if (< i 0) i #false))#falseこれらのループは #false でない最初の値を返す。
- `.../sum` は反復が生成する数を足し合わせる：
`>`(for/sum ([c "abc"]) (string->int c))294
- `.../product` は反復が生成する数を掛け合わせる
`>`(for/product ([c "abc"]) (+ (string->int c) 1))970200
- `.../string` は 1String の列から Strings を作る：
`>`(define a (string->int "a"))`>`(for/string ([j 10]) (int->string (+ a j)))"abcdefghij"

Stop! for/fold ループがどう働くか想像せよ。

もう一度 Stop! 上のすべての例を、ISL+ の既存の抽象化を使って書き直すのは有益な演習である。そうすると、抽象関数の代わりに `for` ループで関数を設計する方法も示唆される。ヒント and-map と or-map を設計せよ。それぞれ andmap と ormap のように働くが、適切な非 #false の値を返す。

> **図109: Constructing sequences of natural numbers**

```racket
; N -> sequence?
; constructs the infinite sequence of natural numbers,
; starting from n
(define (in-naturals n) ...)

; N N N -> sequence?
; constructs the following finite sequence of natural numbers:
;   start
;   (+ start step)
;   (+ start step step)
;   ...
;  until the number exceeds end
(define (in-range start end step) ...)
```


数にわたるループは、常に 0 から (-n1) を列挙するとは限らない。しばしばプログラムは、連続でない数の列を踏む必要があり、別のときは無制限の数の供給が要る。この形のプログラミングに対応するため、Racket は列を生成する関数を備え、図109は ISL+ 用の abstraction ティーチパックが提供する2つを列挙する。

最初のものを使えば、enumerate 関数を少し簡単にできる：

```racket
(define (enumerate.v2 lx)
  (for/list ([item lx] [ith (in-naturals 1)])
    (list ith item)))
```

ここで in-naturals は 1 から始まる自然数の無限列を生成するのに使われ、`for` ループは lx が尽きると止まる。

2つ目を使えば、たとえば最初の n のうちの偶数を踏むことができる：

```racket
; N -> Number
; adds the even numbers between 0 and n (exclusive)
(check-expect (sum-evens 2) 0)
(check-expect (sum-evens 4) 2)
(define (sum-evens n)
  (for/sum ([i (in-range 0 n 2)]) i))
```

この使い方は些細に見えるかもしれないが、数学に起源を持つ多くの問題はまさにこのようなループを求め、それこそが in-range のような概念が多くのプログラミング言語に見られる理由である。

Exercise 305. ループを使って convert-euro を定義せよ。exercise 267 を見よ。

**Exercise 306.** ループを使って、次の関数を定義せよ

1. 任意の自然数 n についてリスト (list 0... (- n 1)) を作る；
2. 任意の自然数 n についてリスト (list 1... n) を作る；
3. 任意の自然数 n についてリスト (list11/2...1/n) を作る；
4. 最初の n 個の偶数のリストを作る；そして
5. 0 と 1 の対角正方形を作る；exercise 262 を見よ。

最後に、ループを使って exercise 250 の tabulate を定義せよ。

Exercise 307. find-name を定義せよ。この関数は名前と名前のリストを消費する。後者のうち、前者と等しい、または前者の拡張である最初の名前を取り出す。

ある名前のリスト上のどの名前も、ある与えられた幅を超えないことを保証する関数を定義せよ。exercise 271 と比較せよ。

## Pattern Matching（パターンマッチ）

6つの節を持つデータ定義のための関数を設計するとき、6股の cond 式を使う。cond 節の1つを定式化するとき、述語を使ってこの節が与えられた値を処理すべきかを判定し、そうならセレクタで複合値を分解する。本書の最初の3部はこの考えを繰り返し説明する。

> **注意:** 興味ある
教官は、代数的データ型を定義するための 2htdp/abstraction ティーチパックの機能を調べるとよい。

繰り返しは抽象化を呼ぶ。Abstraction はプログラマがこれらの抽象化の一部をどう作れるかを説明するが、述語–セレクタのパターンは言語設計者にしか対処できない。とくに、関数型プログラミング言語の設計者は、述語とセレクタのこうした反復的な使用を抽象化する必要性を認識してきた。したがってこれらの言語は、これらの cond 節を組み合わせて簡単にする言語的構成子として**パターンマッチ (pattern matching)** を提供する。

本節は Racket のパターンマッチャの簡略版を提示する。図110はその文法を示す。match は明らかに構文的に複雑な構成子である。その大枠は cond に似ているが、条件の代わりにパターンがあり、それらには独自の規則がある。

> **図110: ISL+ match expressions**

```
expr
=
...
|
(
match
expr
[
pattern
expr
]
...
)
pattern
=
variable
|
literal-constant
|
(
cons
pattern
pattern
)
|
(
structure-name
pattern
...
)
|
(
?
predicate-name
)
```


大ざっぱに言えば、

```racket
(match expr
  [pattern1 expr1]
  [pattern2 expr2]
...)
```

は cond 式のように進む。すなわち expr を評価し、その結果を pattern1、pattern2、... と順にマッチさせ、patterni で成功するまで続ける。その時点で expri の値を求め、それが match 式全体の結果にもなる。

鍵となる違いは、match が cond と異なり新しいスコープを導入することであり、それは DrRacket のスクリーンショットで最もよく示される：

> [image: pict_139.png]

画像が示すように、この関数の各パターン節は変数を束縛する。さらに、変数のスコープは節の本体なので、たとえ2つのパターンが同じ変数束縛を導入しても——上のコード片のように——それらの束縛は互いに干渉できない。

構文的に、パターンは入れ子の構造的データに似ており、その葉はリテラル定数、変数、または次の形の述語パターンである

```racket
(? predicate-name)
```

後者では、predicate-name はスコープ内の述語関数、すなわち1つの値を消費して Boolean を生成する関数を指さなければならない。

意味論的には、パターンは値 v にマッチされる。パターンが

- リテラル定数なら、そのリテラル定数にのみマッチする`>`(match 4 ['four 1] ["four" 2] [#true 3] [4 "hello world"])"hello world"
- 変数なら、任意の値にマッチし、対応する match 節の本体の評価中にこの値と結び付けられる`>`(match 2 [3 "one"] [x (+ x 3)])5 2 が最初のパターン（リテラル定数 3）と等しくないので、match は 2 を第2のパターン（ただの変数であり、したがって任意の値にマッチする）とマッチさせる。よって match は第2の節を選び、x が 2 を表す状態でその本体を評価する。
- (conspattern1pattern2) なら、
cons のインスタンスにのみマッチし、その第1フィールドが pattern1 にマッチし、rest が pattern2 にマッチすることを仮定する`>`(match (cons 1 '()) [(cons 1 tail) tail] [(cons head tail) head])'()`>`(match (cons 2 '()) [(cons 1 tail) tail] [(cons head tail) head])2これらの対話は、match がまず cons を分解し、次に与えられたリストの葉にリテラル定数と変数をどう使うかを示す。
- (structure-namepattern1...patternn) なら、
structure-name 構造体にのみマッチし、そのフィールド値が pattern1,..., patternn にマッチすることを仮定する`>`(define p (make-posn 3 4))`>`(match p [(posn x y) (sqrt (+ (sqr x) (sqr y)))])5明らかに、posn のインスタンスをパターンとマッチさせるのは、cons パターンとマッチさせるのと似ている。ただしパターンがコンストラクタ名ではなく posn を使う点に注意。マッチは自分で定義した構造体型定義でも働く：
`>`(define-struct phone [area switch four])`>`(match (make-phone 713 664 9993) [(phone x y z) (+ x y z)])11370ここでもパターンは構造体の名前 phone を使う。最後に、マッチは複数層の構成をまたいでも働く：
`>`(match (cons (make-phone 713 664 9993) '()) [(cons (phone area-code 664 9993) tail) area-code])713この match 式は、スイッチコードが 664 で末尾4桁が 9993 のとき、リスト内の電話番号から市外局番を取り出す。
- (?predicate-name) なら、(predicate-namev) が #true を生成するときにマッチする`>`(match (cons 1 '()) [(cons (? symbol?) tail) tail] [(cons head tail) head])1この式は第2節の結果である 1 を生成する。1 はシンボルではないからである。

Stop! 先を読む前に match を試せ。

ここで、match の有用性を示す時である：

> **例題** last-item 関数を設計せよ。これは非空リストの最後の項目を取り出す。非空リストは次のように定義されることを思い出そう：
>;A [Non-empty-list X] is one of:;–(consX'());–(consX[Non-empty-listX])

Stop! Arbitrarily Large Data がこの問題を扱う。解を調べよ。

match を使えば、設計者は cond を使った解から3つのセレクタと2つの述語を取り除ける：

```racket
; [Non-empty-list X] -> X
; retrieves the last item of ne-l
(check-expect (last-item '(a b c)) 'c)
(check-error (last-item '()))
(define (last-item ne-l)
  (match ne-l
    [(cons lst '()) lst]
    [(cons fst rst) (last-item rst)]))
```

述語とセレクタの代わりに、この解はデータ定義にあるものと同じようなパターンを使う。データ定義内の自己参照と集合パラメータの各出現について、パターンはプログラムレベルの変数を使う。match 節の本体は、セレクタでリストから関連部分を取り出さず、単にこれらの名前を参照する。以前と同様、関数は与えられた cons の rest フィールドで再帰する。データ定義がこの位置で自分自身を参照するからである。基底ケースでは、答えは lst であり、リストの最後の項目を表す変数である。

Arbitrarily Large Data からの第2の問題を見てみよう：

> **例題** depth 関数を設計せよ。これはマトリョーシカを囲む層の数を測る。データ定義を再掲する：
> (define-struct layer [color doll]);AnRD.v2 (short forRussian doll) is one of:;–"doll";–(make-layerStringRD.v2)

次は match を使った depth の定義である：

```racket
; RD.v2 -> N
; how many dolls are a part of an-rd
(check-expect (depth (make-layer "red" "doll")) 1)
(define (depth a-doll)
  (match a-doll
    ["doll" 0]
    [(layer c inside) (+ (depth inside) 1)]))
```

最初の match 節のパターンは "doll" を探すが、2つ目は任意の layer 構造体にマッチし、c を color フィールドの値に、inside を doll フィールドの値に結び付ける。要するに、match は再び関数定義を簡潔にする。

最後の問題は、一般化された UFO ゲームからの抜粋である：

> **例題** move-right 関数を設計せよ。これはキャンバス上の物体の位置を表す Posn のリストと、1つの数を消費する。関数は後者を各 x 座標に加え、これらの物体の右方向への移動を表す。

次が私たちの解であり、ISL+ の力をフルに使う：

```racket
; [List-of Posn] -> [List-of Posn]
; moves each object right by delta-x pixels

(define input  `(,(make-posn 1 1),(make-posn 10 14)))
(define expect `(,(make-posn 4 1),(make-posn 13 14)))

(check-expect (move-right input 3) expect)

(define (move-right lop delta-x)
  (for/list ((p lop))
    (match p
     [(posn x y) (make-posn (+ x delta-x) y)])))
```

Stop! テストの定式化に define を使っていることに気づいたか。データ例に define で良い名前を付け、その隣に関数が生成する期待結果を書き下ろしておけば、あとでコードを読むのが、定数だけを書き下ろした場合よりずっと容易になる。

Stop! cond とセレクタを使った解はどう比較されるか。書き出して2つを比較せよ。どちらが好きか。

Exercise 308. 関数 replace を設計せよ。電話記録のリストにおいて、市外局番 713 を 281 に置き換える。

Exercise 309. 関数 words-on-line を設計せよ。文字列のリストのリストの各項目について、String の個数を求める。
