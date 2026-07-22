<!-- Extracted from original_html/part_six.html -->
<!-- Canonical English source for Japanese translation -->

# VI 蓄積子（Accumulators）

### 目次（Contents）

- 31 知識の喪失（The Loss of Knowledge）
- 31.1 構造的処理の問題（A Problem with Structural Processing）
- 31.2 生成的再帰の問題（A Problem with Generative Recursion）
- 32 蓄積子スタイルの関数の設計（Designing Accumulator-Style Functions）
- 32.1 蓄積子の必要性を認識する（Recognizing the Need for an Accumulator）
- 32.2 蓄積子を追加する（Adding Accumulators）
- 32.3 関数を蓄積子スタイルに変換する（Transforming Functions into Accumulator Style）
- 32.4 グラフィカルエディタ、マウス付き（A Graphical Editor, with Mouse）
- 33 蓄積のさらなる用法（More Uses of Accumulation）
- 33.1 蓄積子と木（Accumulators and Trees）
- 33.2 蓄積子付きのデータ表現（Data Representations with Accumulators）
- 33.3 結果としての蓄積子（Accumulators as Results）
- 34 まとめ（Summary）

ISL+ に、ある関数 f を引数 a に適用するよう依頼すると、通常は何らかの値 v が得られる。
(f a) を再び評価しても、また v が得られる。実際、(f a) の評価を何度依頼しても v が得られる。
関数が初めて適用されるか 100 回目かにかかわらず、また適用が DrRacket の相互作用領域にあるか関数自身の内部にあるかにかかわらず、関係ない。
関数は目的文に従って働き、知る必要があるのはそれだけである。

> **注:** 関数適用は永遠にループしたりエラーを通知したりすることもあるが、これらの可能性は無視する。また random も無視する。これはこの規則の真の例外である。

この文脈独立性の原理は、再帰関数の設計において決定的な役割を果たす。
設計に関しては、関数がまだ定義されていなくても、目的文が約束することを計算すると仮定して自由である。
特に、再帰呼び出しの結果を使ってある関数のコード——通常はその cond 節の1つ——を組み立ててよい。
構造的再帰関数と生成的再帰関数の両方についての設計レシピのテンプレートとコーディングのステップは、この考えに依拠している。

文脈独立性は関数の設計を容易にする一方で、2つの問題を引き起こす。
一般に、文脈独立性は再帰的評価のあいだに知識の喪失を招く。
関数は、完全なリストに対して呼ばれたのか、そのリストの一部に対して呼ばれたのかを「知らない」。
構造的に再帰するプログラムでは、この知識の喪失はデータを複数回走査しなければならなくなり、性能上のコストを生じることを意味する。
生成的再帰を用いる関数では、この喪失は関数が結果をまったく計算できないことを意味することがある。
前の部は、この第2の問題を、循環グラフについて2つの節点のあいだの経路を見つけられないグラフ走査関数で示している。

この部では、この「文脈の喪失」問題に対処するための設計レシピの変種を導入する。
(f a) が、何度評価されどこで評価されようと同じ結果を返すという原理を保ちたいので、唯一の解決策は、関数呼び出しの文脈を表す引数を追加することである。
この追加の引数を蓄積子（accumulator）と呼ぶ。
データの走査のあいだ、再帰呼び出しは通常の引数を受け取り続け、蓄積子はそれらと文脈に関連して変化する。

蓄積子付きの関数を正しく設計することは、これまでの章のどの設計アプローチよりも明らかに複雑である。
鍵は、本来の引数と蓄積子の関係を理解することである。
続く章では、蓄積子付きの関数をどう設計するか、そしてそれらがどう働くかを説明する。

## 31 知識の喪失（The Loss of Knowledge）

構造的レシピに従って設計された関数も、生成的な関数も、どちらも知識の喪失に苦しむが、その仕方は異なる。
本章は、各カテゴリから1つずつの2つの例で、文脈的知識の欠如が関数の性能にどう影響するかを説明する。
第1節は構造的再帰について、第2節は生成的な領域の懸念を扱う。

### 31.1 構造的処理の問題（A Problem with Structural Processing）

一見まっすぐな例から始めよう。

> サンプル問題 道路区画の長さを測る測量チームのために働いている。
> チームは、一連の道路上の点のあいだの相対距離を、ある起点からの絶対距離へ変換するプログラムを設計してほしいと頼んできた。

たとえば、次のような線が与えられるかもしれない。

> [image: pict_273.png]

各数は2つの点のあいだの距離を指定する。必要なのは次の図で、各点に最も左の端までの距離が注記されている。

> [image: pict_274.png]

この計算を行うプログラムの設計は、構造的関数設計の単なる練習問題である。
図177に完全なプログラムがある。
与えられたリストが '() でないとき、自然な再帰は残りの点の、(rest l) の先頭への絶対距離を計算する。
その先頭は実際の原点ではなく、原点までの距離は (first l) なので、自然な再帰の結果の各数に (first l) を加えなければならない。
この第2のステップ——数のリストの各項目に数を加えること——には補助関数が必要である。

> **図177: Converting relative distances to absolute distances**

```racket
; [List-of Number] -> [List-of Number]
; converts a list of relative to absolute distances
; the first number represents the distance to the origin

(check-expect (relative->absolute '(50 40 70 30 30))
              '(50 90 160 190 220))

(define (relative->absolute l)
  (cond
    [(empty? l) '()]
    [else (local ((define rest-of-l
                    (relative->absolute (rest l)))
                  (define adjusted
                    (add-to-each (first l) rest-of-l)))
            (cons (first l) adjusted))]))

; Number [List-of Number] -> [List-of Number]
; adds n to each number on l

(check-expect (cons 50 (add-to-each 50 '(40 110 140 170)))
              '(50 90 160 190 220))

(define (add-to-each n l)
  (cond
    [(empty? l) '()]
    [else (cons (+ (first l) n) (add-to-each n (rest l)))]))
```


プログラムの設計は比較的まっすぐだが、どんどん大きなリストに使うと問題が現れる。
次の式の評価を考えてみよう。

```racket
(relative->absolute (build-list size add1))
```

size を増やすと、必要な時間はさらに速く増える。

> size 1000 2000 3000 4000 5000 6000 7000time 25 109 234 429 689 978 1365

1000 項目から 2000 項目へ進むとき、時間は倍になるのではなく4倍になる。
2000 から 4000 へ進むときも、およその関係は同じである。
間奏5: 計算のコスト（Intermezzo 5: The Cost of Computation）の用語を使うと、関数の性能は O(n²) であると言え、ここで n は与えられたリストの長さである。

> **注:** 時間はコンピュータごと、年ごとに異なる。
> これらの計測は 2017 年に OS X 10.11 を動かす MacMini で行われた。
> 前回の計測は 1998 年で、時間は 100 倍大きかった。

練習問題 489. map と lambda を使って add-to-each を再定式化せよ。

**練習問題 490.** relative->absolute の抽象的実行時間を記述する式を開発せよ。
ヒント 次の式を手で評価せよ。

```racket
(relative->absolute (build-list size add1))
```

まず size を 1、2、3 に置き換えよ。
毎回、relative->absolute と add-to-each の再帰は何回必要か。

問題の単純さからすると、プログラムが行う作業量は驚くべきである。
同じリストを手で変換するなら、総距離を集計し、線に沿って進むにつれて相対距離にそれを加えるだけだろう。
なぜプログラムはそうできないのか。

手作業の方法に近い関数の版を設計してみよう。
やはりリスト処理のテンプレートから始める。

```racket
(define (relative->absolute/a l)
  (cond
    [(empty? l)...]
    [else
     (... (first l)...
... (relative->absolute/a (rest l))...)]))
```

手評価をシミュレートしてみよう。

```racket
(relative->absolute/a (list 3 2 7))
== (cons... 3... (relative->absolute/a (list 2 7)))
== (cons... 3...
     (cons... 2...
       (relative->absolute/a (list 7))))
== (cons... 3...
     (cons... 2...
       (cons... 7...
         (relative->absolute/a '()))))
```

結果リストの最初の項目は明らかに 3 であるべきで、このリストを組み立てるのは易しい。
しかし2番目は (+ 3 2) であるべきなのに、relative->absolute/a の2番目のインスタンスは、元のリストの先頭項目が 3 であることを「知る」術がない。
「知識」が失われている。

再び、問題は再帰関数が文脈から独立していることである。
関数は (cons N L) の中の L を、(cons K L) の中と同じ仕方で処理する。
実際、L だけが与えられても、同じ仕方でリストを処理するだろう。

「知識」の喪失を補うために、関数に追加のパラメータ accu-dist を装備する。
これは蓄積された距離を表し、相対距離のリストを絶対距離のリストへ変換するときに保つ集計である。
その初期値は 0 でなければならない。
関数がリストを走査するにつれて、その数を集計に加えなければならない。

これが改訂された定義である。

```racket
(define (relative->absolute/a l accu-dist)
  (cond
    [(empty? l) '()]
    [else
     (local ((define tally (+ (first l) accu-dist)))
       (cons tally
         (relative->absolute/a (rest l) tally)))]))
```

再帰的適用は、リストの残りと、現在の点の原点への新しい絶対距離を消費する。
どちらの引数も呼び出しごとに変化するが、2番目の変化は厳密に第1引数に依存する。
関数は依然として平明なリスト処理手続きである。

実行中の例を再び評価してみよう。

```racket
(relative->absolute/a (list 3 2 7))
== (relative->absolute/a (list 3 2 7) 0)
== (cons 3 (relative->absolute/a (list 2 7) 3))
== (cons 3 (cons 5 (relative->absolute/a (list 7) 5)))
== (cons 3 (cons 5 (cons 12???)))
== (cons 3 (cons 5 (cons 12 '())))
```

やめ！ 4行目の疑問符を埋めよ。

手評価は、蓄積子の使用が変換過程をどれほど単純化するかを示す。
リストの各項目は1回だけ処理される。
relative->absolute/a が引数リストの末尾に達すると、結果は完全に決まり、これ以上の作業は不要である。
一般に、関数は N 項目のリストに対して N 回のオーダーの自然な再帰ステップを行う。

1つの問題は、relative->absolute と違い、新しい関数は引数を1つではなく2つ消費することである。
さらに悪いことに、誰かが relative->absolute/a を数のリストと 0 でない数に誤って適用するかもしれない。
どちらの問題も、local 定義を使って relative->absolute/a をカプセル化する関数定義で解ける。
図178に結果を示す。
これで relative->absolute は、入出力に関して relative->absolute.v2 と区別がつかない。

> **図178: Converting relative distances with an accumulator**

```racket
; [List-of Number] -> [List-of Number]
; converts a list of relative to absolute distances
; the first number represents the distance to the origin

(check-expect (relative->absolute.v2 '(50 40 70 30 30))
              '(50 90 160 190 220))

(define (relative->absolute.v2 l0)
  (local (
    ; [List-of Number] Number -> [List-of Number]
    (define (relative->absolute/a l accu-dist)
      (cond
        [(empty? l) '()]
        [else
          (local ((define accu (+ (first l) accu-dist)))
            (cons accu
                 (relative->absolute/a (rest l) accu)))])))
    (relative->absolute/a l0 0)))
```


この版のプログラムがどう性能を発揮するか見てみよう。
そのために次を評価する。

```racket
(relative->absolute.v2 (build-list size add1))
```

そして size のいくつかの値について結果を表にする。

> size 1000 2000 3000 4000 5000 6000 7000time 0 0 0 0 0 1 1

驚くべきことに、relative->absolute.v2 は、7000 個の数のリストでも、そのようなリストの処理に1秒より長くかかることは決してない。
この性能を relative->absolute のものと比べると、蓄積子は遅く走るすべてのプログラムへの奇跡の治療薬だと思うかもしれない。
残念ながらそうではないが、構造的再帰関数が自然な再帰の結果を再処理しなければならないとき、蓄積子の使用を必ず検討すべきである。
この特定の場合、性能は O(n²) から O(n) へ改善し——加えて定数も大きく減少した。

**練習問題 491.** いくらかの設計といくらかのいじりで、友人はサンプル問題に対して次の解にたどり着いた。

> **注:** Adrian German と Mardin Yadegar がこの練習問題を提案した。

```racket
(define (relative->absolute l)
 (reverse
   (foldr (lambda (element accu) (cons (+ element (first accu)) accu))
          (list (first l))
          (reverse (rest l)))))
```

この単純な解は、よく知られた ISL+ 関数 reverse と foldr を使うだけである。
ご存じの通り、lambda の使用は単なる便宜である。
また抽象化（Abstraction）から、foldr は本書の最初の2部で提示された設計レシピで設計可能であることも思い出すかもしれない。

友人の解は、この動機づけの節での複雑な設計が不要だということを意味するか。
答えは蓄積子の必要性を認識する（Recognizing the Need for an Accumulator）を見よ。ただしまず問題を熟考せよ。
ヒント reverse を自分で設計してみよ。

### 31.2 生成的再帰の問題（A Problem with Generative Recursion）

グラフ内の経路に沿って「旅する」問題を再訪しよう。

> サンプル問題 単純グラフにおいて2つの節点が連結しているかどうかを検査するアルゴリズムを設計せよ。
> そのようなグラフでは、各節点はちょうど1つの、別の節点——あるいは自分自身——への方向付き連結を持つ。

バックトラックするアルゴリズム（Algorithms that Backtrack）は、アルゴリズムが経路を発見しなければならない変種を扱う。
このサンプル問題はそれより単純である。この節はアルゴリズムの蓄積子版の設計に焦点を当てるからである。

図179のサンプルグラフを考えよ。
節点は A から F の6つで、連結は6本ある。
A から E への経路は B と C を含まなければならない。
しかし A から F へ、あるいは自分自身以外のどの節点からも F への経路はない。

> **図179: A simple graph**

```racket
(define a-sg
  '((A B)
    (B C)
    (C E)
    (D E)
    (E B)
    (F F)))
```


> 原本は次の画像を含む（画像プレースホルダは図版パイプラインで埋め込み可）:
>
> [image: pict_275.png]


図179の右側は、このグラフを入れ子のリストでどう表現するかを示す。
各節点は2つの記号のリストで表される。
第1の記号はその節点のラベル、第2は第1から到達可能な唯一の節点である。
関連するデータ定義は次の通りである。

```racket
; A SimpleGraph is a [List-of Connection]
; A Connection is a list of two items:
;   (list Node Node)
; A Node is a Symbol.
```

これらは非形式的な記述のまっすぐな翻訳である。

この問題が生成的再帰を要求することはすでに分かっており、ヘッダ材料を作るのは易しい。

```racket
; Node Node SimpleGraph -> Boolean
; is there a path from origin to destination
; in the simple graph sg

(check-expect (path-exists? 'A 'E a-sg) #true)
(check-expect (path-exists? 'A 'F a-sg) #false)

(define (path-exists? origin destination sg)
  #false)
```

必要なのは、生成的再帰のレシピの4つの基本質問への答えである。

- 問題は origin が destination と同じなら自明である。
- 自明な解は #true である。
- origin が destination と同じでないなら、できることは1つだけである。直近の隣へ進み、そこから destination を探す。
- 新しい問題の解を見つけたとき、何もする必要はない。
origin の隣が destination に連結していれば、origin もそうである。そうでなければ連結はない。

ここからはこれらの答えを ISL+ で表すだけで、本格的なプログラムが得られる。

> **図180: Finding a path in a simple graph**

```racket
; Node Node SimpleGraph -> Boolean
; is there a path from origin to destination in sg

(check-expect (path-exists? 'A 'E a-sg) #true)
(check-expect (path-exists? 'A 'F a-sg) #false)

(define (path-exists? origin destination sg)
  (cond
    [(symbol=? origin destination) #t]
    [else (path-exists? (neighbor origin sg)
                        destination
                        sg)]))

; Node SimpleGraph -> Node
; determine the node that is connected to a-node in sg
(check-expect (neighbor 'A a-sg) 'B)
(check-error (neighbor 'G a-sg) "neighbor: not a node")
(define (neighbor a-node sg)
  (cond
    [(empty? sg) (error "neighbor: not a node")]
    [else (if (symbol=? (first (first sg)) a-node)
              (second (first sg))
              (neighbor a-node (rest sg)))]))
```


図180に完全なプログラムがある。単純グラフで節点の隣を見つける関数——構造的再帰のまっすぐな練習問題——と、両方の可能な結果のテストケースも含む。
しかしプログラムを走らせてはいけない。
走らせるなら、暴走するプログラムを止めるマウスの準備をしておけ。
実際、関数をざっと見ただけでも問題があることが示唆される。
関数は origin から destination への経路がなければ #false を生成するはずなのに、プログラムのどこにも #false がない。
逆に、2つの節点のあいだに経路がないとき関数が実際に何をするかを問わなければならない。

図179をもう一度見よ。
この単純グラフでは C から D への経路はない。
C を出る連結は D のすぐそばを通り、代わりに E へ行く。
そこで手評価を見てみよう。

```racket
(path-exists? 'C 'D '((A B) [image:pict_276.png] (F F)))
== (path-exists? 'E 'D '((A B)  [image:pict_277.png] (F F)))
== (path-exists? 'B 'D '((A B)  [image:pict_278.png] (F F)))
== (path-exists? 'C 'D '((A B)  [image:pict_279.png] (F F)))
```

関数が再帰するにつれて、まったく同じ引数で自分自身を何度も呼び出すことが確認できる。
言い換えると、評価は決して止まらない。

path-exists? についての問題は、再び「知識」の喪失であり、上の relative->absolute と似ている。
relative->absolute と同様、path-exists? の設計はレシピを使い、再帰呼び出しが文脈から独立していると仮定する。
path-exists? の場合、これは特に、現在の再帰の連鎖の中で以前の適用がまったく同じ引数を受け取ったかどうかを関数が「知らない」ことを意味する。

この設計問題への解決は、前節のパターンに従う。
パラメータを1つ加え、それを seen と呼び、関数が出会ってきた開始節点の蓄積されたリストを表す——元の適用から始まる。
その初期値は '() でなければならない。
関数が特定の origin を検査しその隣へ進むにつれて、origin が seen に加えられる。

これが path-exists? の最初の改訂で、path-exists?/a と名づけた。

```racket
; Node Node SimpleGraph [List-of Node] -> Boolean
; is there a path from origin to destination
; assume there are no paths for the nodes in seen
(define (path-exists?/a origin destination sg seen)
  (cond
    [(symbol=? origin destination) #true]
    [else (path-exists?/a (neighbor origin sg)
                          destination
                          sg
                          (cons origin seen))]))
```

新しいパラメータの追加だけでは問題は解けないが、

```racket
(path-exists?/a 'C 'D '((A B) [image:pict_280.png] (F F)) '())
```

の手評価が示すように、解の基礎を与える。

```racket
== (path-exists?/a 'E 'D '((A B) [image:pict_281.png] (F F)) '(C))
== (path-exists?/a 'B 'D '((A B) [image:pict_282.png] (F F)) '(E C))
== (path-exists?/a 'C 'D '((A B) [image:pict_283.png] (F F)) '(B E C))
```

元の関数と対照的に、改訂された関数はもはやまったく同じ引数で自分自身を呼ばない。
3つの本来の引数は3回目の再帰適用でも再び同じだが、蓄積子引数は最初の適用のそれとは異なる。
'() の代わりに、今は '(B E C) である。
新しい値は、'C から 'D への経路の探索中に、関数が 'B、'E、'C を開始点として検査したことを伝える。

あとは、アルゴリズムが蓄積された知識を活用するようにするだけである。
具体的には、アルゴリズムは与えられた origin がすでに seen の項目かどうかを判定できる。
そうなら、問題もまた自明に解け、解として #false を与える。
図181に path-exists.v2? の定義がある。これは path-exists? の改訂である。
定義は ISL+ 関数 member? を参照する。

> **図181: Finding a path in a simple graph with an accumulator**

```racket
; Node Node SimpleGraph -> Boolean
; is there a path from origin to destination in sg

(check-expect (path-exists.v2? 'A 'E a-sg) #true)
(check-expect (path-exists.v2? 'A 'F a-sg) #false)

(define (path-exists.v2? origin destination sg)
  (local (; Node Node SimpleGraph [List-of Node] -> Boolean
          (define (path-exists?/a origin seen)
            (cond
              [(symbol=? origin destination) #t]
              [(member? origin seen) #f]
              [else (path-exists?/a (neighbor origin sg)
                                    (cons origin seen))])))
    (path-exists?/a origin '())))
```


path-exists.v2? の定義は、最初の改訂の2つの小さな問題も除いている。
蓄積する関数の定義を局所化することで、最初の呼び出しが常に seen の初期値として '() を使うことを保証できる。
そして path-exists.v2? は、path-exists? 関数とまったく同じシグネチャと目的文を満たす。

それでも、path-exists.v2? と relative-to-absolute2 のあいだには重要な違いがある。
後者は元の関数と等価だったが、path-exists.v2? は path-exists? を改善する。
後者はある入力に対して答えを見つけられないが、path-exists.v2? は任意の単純グラフに対して解を見つける。

練習問題 492. 図169の定義を修正し、同じ origin に2度出会っても、プログラムが #false を生成するようにせよ。

## 32 蓄積子スタイルの関数の設計（Designing Accumulator-Style Functions）

前章は、余分な知識を蓄積する必要性を2つの例で示した。一方の場合、蓄積は関数の理解を容易にし、元の版よりはるかに高速な関数を生む。他方の場合、関数が正しく動くために蓄積が必要である。ただしどちらの場合も、蓄積の必要性が明らかになるのは、きちんと設計された関数が存在してからである。

前章を一般化すると、蓄積子関数の設計には2つの大きな側面があることが分かる：

1. 関数が蓄積子から恩恵を受けることの認識、および
2. 蓄積子が何を表すかの理解。

最初の2節がこれら2つの問いを扱う。2番目は難しい話題なので、第3節は一連の例でそれを示し、通常の関数を蓄積する版へ変換する。

> **図182: Design with accumulators, a structural example**

```racket
; [List-of X] -> [List-of X]
; constructs the reverse of alox

(check-expect (invert '(a b c)) '(c b a))

(define (invert alox)
  (cond
    [(empty? alox) '()]
    [else
     (add-as-last (first alox) (invert (rest alox)))]))

; X [List-of X] -> [List-of X]
; adds an-x to the end of alox

(check-expect (add-as-last 'a '(c b)) '(c b a))

(define (add-as-last an-x alox)
  (cond
    [(empty? alox) (list an-x)]
    [else
     (cons (first alox) (add-as-last an-x (rest alox)))]))
```


### 32.1 蓄積子の必要性の認識（Recognizing the Need for an Accumulator）

蓄積子の必要性を認識するのは簡単な仕事ではない。私たちは2つの理由を見てきたが、それらが最も一般的なものである。いずれの場合も、まず従来の設計レシピに基づいて完全な関数を作ることが決定的に重要である。そのうえで関数を研究し、次のように進む：

1. 構造的再帰関数が、自然な再帰の結果を補助的な再帰関数でたどるなら、蓄積子パラメータの使用を検討せよ。図182の invert の定義を見よ。再帰適用の結果は、リストの残りを反転したものを生成する。add-as-last を使って、この反転リストに先頭項目を加え、リスト全体の反転を作る。この第2の補助関数も再帰的である。こうして蓄積子の候補を特定した。A Problem with Structural Processing でのように、手評価をいくつか行い、蓄積子が役立つかどうかを調べるときである。次を考えよ：
(invert '(a b c))== (add-as-last 'a (invert '(b c)))== (add-as-last 'a (add-as-last 'b (invert '(c))))==...== (add-as-last 'a (add-as-last 'b '(c)))== (add-as-last 'a '(c b))== '(c b a)やめ！ 点線を欠けている2ステップで置き換えよ。すると、invert は結局、与えられたリストの末尾に到達する——add-as-last と同様——ことが分かり、そこに置くべき項目を知っていれば、補助関数は不要になる。
2. 生成的再帰に基づく関数を扱っている場合、はるかに難しい課題に直面する。目標は、結果を期待する入力についてアルゴリズムが結果を生成できないかどうかを理解することである。そうなら、知識を蓄積するパラメータを加えることが助けになるかもしれない。これらの状況は複雑なので、例の議論は More Uses of Accumulation に先送りする。

練習問題 493. Intermezzo 5: The Cost of Computation の用語で、与えられたリストが n 個の項目からなるとき、invert が O(n2) 時間を消費することを論ぜよ。

練習問題 494. Auxiliary Functions that Recur の insertion sort> 関数は蓄積子を必要とするか。必要ならなぜか。不要ならなぜか。

### 32.2 蓄積子の追加（Adding Accumulators）

既存の関数に蓄積子を装備すべきだと決めたら、次の2ステップを取れ：

- 蓄積子が表す知識、どんな種類のデータを使うか、そしてその知識がデータとしてどう獲得されるかを決定せよ。たとえば、相対距離を絶対距離へ変換する場合には、これまでに出会った総距離を蓄積すれば足りる。関数が相対距離のリストを処理するにつれ、見つかった新しい相対距離を蓄積子の現在値に加える。経路問題では、蓄積子は出会ったすべてのノードを覚える。パス検査関数がグラフをたどるにつれ、新しいノードをそれぞれ蓄積子の先頭に cons する。一般に、次のように進むとよい。
蓄積子テンプレートを作れ：
;Domain -> Range(define (function d0) (local (;Domain AccuDomain -> Range;accumulator... (define (function/a d a)...)) (function/a d0 a0)))function の適用の手評価をスケッチし、蓄積子の性質を理解せよ。蓄積子が追跡するデータの種類を決定せよ。補助関数 function/a の引数 d と元の引数 d0 のあいだの関係として蓄積子を説明する文を書き落とせ。
注 この関係は評価の過程を通じて一定であり、不変条件（invariant）とも呼ばれる。この性質のため、蓄積子文はしばしば不変条件と呼ばれる。
不変条件を使い、a の初期値 a0 を決定せよ。また不変条件を活用し、function/a の定義内の再帰的関数呼び出しについて、蓄積子をどう計算するかを決定せよ。
- 蓄積子の知識を function/a の設計に活用せよ。構造的再帰関数では、蓄積子の値は典型的には基底場合、すなわち再帰しない cond 節で使われる。生成的再帰関数を使う関数では、蓄積された知識は既存の基底場合、新しい基底場合、あるいは生成的再帰を扱う cond 節で使われることがある。

ご覧のとおり、鍵は蓄積子の役割の正確な記述である。したがって、この技能を練習することが重要である。

invert の例を見てみよう：

```racket
(define (invert.v2 alox0)
  (local (; [List-of X]??? -> [List-of X]
; constructs the reverse of alox
; accumulator...
          (define (invert/a alox a)
            (cond
              [(empty? alox)...]
              [else
               (invert/a (rest alox)... a...)])))
    (invert/a alox0...)))
```

前節で示したように、このテンプレートだけで、次のような例の手評価をスケッチするのに十分である：

```racket
(invert '(a b c))
```

考えは次のとおり：

```racket
== (invert/a '(a b c) a0)
== (invert/a '(b c)... 'a... a0)
== (invert/a '(c)... 'b... 'a... a0)
== (invert/a '()... 'c... 'b... 'a... a0)
```

このスケッチは、invert/a がこれまでに見たすべての項目を、alox0 と a の差を逆順で追跡するリストに保持できることを示唆する。初期値は明らかに '() であり、invert/a の内部で cons で蓄積子を更新すると、invert/a が '() に到達したときちょうど望ましい値が得られる。

これらの洞察を含む洗練されたテンプレートを次に示す：

```racket
(define (invert.v2 alox0)
  (local (; [List-of X] [List-of X] -> [List-of X]
; constructs the reverse of alox
; accumulator a is the list of all those
; items on alox0 that precede alox
; in reverse order
          (define (invert/a alox a)
            (cond
              [(empty? alox) a]
              [else
               (invert/a (rest alox)
                         (cons (first alox) a))])))
    (invert/a alox0 '())))
```

local 定義の本体は蓄積子を '() で初期化する一方、再帰呼び出しは cons を使って alox の現在の先頭を蓄積子に加える。基底場合では、invert/a は蓄積子内の知識、すなわち反転されたリストを使う。

再び注意せよ。invert.v2 はリストを単にたどるだけである。対照的に、invert は自然な再帰のすべての結果を add-as-last で再処理する。やめ！ invert.v2 が invert よりどれだけ速く動くかを測定せよ。

用語 プログラマは、蓄積子パラメータを使う関数を議論するために、蓄積子スタイル（accumulator-style）関数という言い回しを使う。蓄積子スタイルの関数の例は、relative->absolute/a、invert/a、および path-exists?/a である。

### 32.3 関数を蓄積子スタイルへ変換する（Transforming Functions into Accumulator Style）

蓄積子文を明確に述べるのは難しいが、良い不変条件を定式化しなければ、蓄積子スタイルの関数を理解することは不可能である。プログラマの目標は、後から来る他者がコードを容易に理解できるようにすることなので、この技能を練習することが決定的に重要である。そして不変条件の定式化は、多くの練習に値する。

本節の目標は、3つのケーススタディで蓄積子文の定式化を研究することである：総和関数、階乗関数、および木の走査関数である。各ケースは、構造的再帰関数を蓄積子スタイルへ変換することに関する。実際にはどれも蓄積子パラメータの使用を求めない。しかしそれらは容易に理解でき、他のすべての気を散らす要素を除くことで、こうした例を使い、蓄積子不変条件の明確化に集中できる。

最初の例として、sum 関数のこれらの定義を考えよ：

```racket
(define (sum.v1 alon)
  (cond
    [(empty? alon) 0]
    [else (+ (first alon) (sum.v1 (rest alon)))]))
```

蓄積子版への最初のステップを次に示す：

```racket
(define (sum.v2 alon0)
  (local (; [List-of Number]??? -> Number
; computes the sum of the numbers on alon
; accumulator...
          (define (sum/a alon a)
            (cond
              [(empty? alon)...]
              [else (... (sum/a (rest alon)
...... a...)...)])))
    (sum/a alon0...)))
```

やめ！ 両方で動くシグネチャとテストケースを与えよ。

最初のステップが示唆するように、sum/a のテンプレートを local 定義の中に置き、蓄積子パラメータを加え、sum のパラメータの名前を変えた。

> **図183: Calculating with accumulator-style templates**
> 左右対比（崩れた ASCII 枠を二重 fence に復元。コードは公式 HTML の RktBlk より）。

**左**

```racket
(sum.v1 '(10 4))
== (+ 10 (sum.v1 '(4)))
== (+ 10 (+ 4 (sum.v1 '())))
== (+ 10 (+ 4 (+ 0)))
...
== 14
```

**右**

```racket
(sum.v2 '(10 4))
== (sum/a '(10 4) a0)
== (sum/a '(4) ... 10 ... a0)
== (sum/a '() ... 4 ... 10 ... a0)
...
== 14
```


図183は手評価の2つの並びのスケッチを示す。比較はすぐに中心的な考えを示唆する。すなわち、sum/a は蓄積子を使い、出会った数を足し合わせることができる、ということである。蓄積子不変条件については、計算は a がこれまでに出会った数の和を表すことを示唆する：

> a は alon が alon0 から欠けている数の和である

たとえば、不変条件は次の関係が成り立つことを強制する：

> alon0 が '(1046) '(1046) '(1046) であり、alon が '(46) '(6) '() なら、a は 10 14 20 であるべきである

この正確な不変条件が与えられれば、設計の残りは素直である：

```racket
(define (sum.v2 alon0)
  (local (; [List-of Number] Number -> Number
; computes the sum of the numbers on alon
; accumulator a is the sum of the numbers
; that alon lacks from alon0
          (define (sum/a alon a)
            (cond
              [(empty? alon) a]
              [else (sum/a (rest alon)
                           (+ (first alon) a))])))
    (sum/a alon0 0)))
```

alon が '() なら、sum/a は a を返す。それが alon 上のすべての数の和を表すからである。不変条件はまた、0 が a0 の初期値であり、+ が「忘れられようとしている」数——(firstalon)——を蓄積子 a に加えて蓄積子を更新することも含意する。

練習問題 495. 図183の (sum/a'(104)0) の手評価を完成させよ。こうすると、sum と sum.v2 が与えられた数を逆順で足し合わせることが分かる。sum は数を右から左へ足し合わせる一方、蓄積子スタイルの版は左から右へ足し合わせる。

数についての注 厳密数については、この違いが最終結果に影響しないことを思い出せ。非厳密数については、違いは重大であり得る。Intermezzo 5: The Cost of Computation の末尾の練習問題を見よ。

第2の例として、よく知られた階乗関数に移る：

> **注:** 階乗関数はアルゴリズムの分析に有用である。

```racket
; N -> N
; computes (* n (- n 1) (- n 2)... 1)
(check-expect (!.v1 3) 6)
(define (!.v1 n)
  (cond
    [(zero? n) 1]
    [else (* n (!.v1 (sub1 n)))]))
```

relative-2-absolute と invert がリストを処理した一方、階乗関数は自然数で働き、そのテンプレートがそれを反映する。

これまでどおり、蓄積子スタイル版のテンプレートから進む：

```racket
(define (!.v2 n0)
  (local (; N??? -> N
; computes (* n (- n 1) (- n 2)... 1)
; accumulator...
          (define (!/a n a)
            (cond
              [(zero? n)...]
              [else (... (!/a (sub1 n)
... a...)...)])))
    (!/a n0...)))
```

続けて手評価のスケッチである：

> (!.v1 3)== (* 3 (!.v1 2))== (* 3 (* 2 (!.v1 1)))...== 6 (!.v2 3)== (!/a 3 a0)== (!/a 2... 3... a0)...== 6

左の列は元の版がどう動くかを示し、右の列は蓄積子スタイルの関数がどう進むかをスケッチする。どちらも構造的に自然数をたどり、0 に到達するまで続ける。元の版は乗算だけを予定するのに対し、蓄積子は構造的走査が与えられた自然数を下りていくにつれ、各数を追跡する。

これらの数を掛け合わせるという目標が与えられれば、!/a は蓄積子を使い、数を即座に掛け合わせられる：

> a は区間 [n0,n) 内の自然数の積である。

特に、n0 が 3 で n が 1 のとき、a は 6 である。

練習問題 496. n0 が 10 で n が 8 のとき、a の値はどうあるべきか。

この不変条件を使えば、a の初期値を容易に選べる——それは 1 である——そして、現在の蓄積子に n を掛けることが適切な更新操作だと分かる：

```racket
(define (!.v2 n0)
  (local (; N N -> N
; computes (* n (- n 1) (- n 2)... 1)
; accumulator a is the product of the
; natural numbers in the interval [n0,n)
          (define (!/a n a)
            (cond
              [(zero? n) a]
              [else (!/a (sub1 n) (* n a))])))
    (!/a n0 1)))
```

蓄積子文からも、n が 0 のとき蓄積子は n から 1 までの積であり、すなわち望ましい結果であることが従う。したがって sum と同様、!/a はこの場合 a を返し、第2の場合では再帰の結果を使う。

練習問題 497. sum と同様、!.v1 は原始的な計算——この場合は乗算——を逆順で行う。驚くべきことに、これは関数の性能に否定的な影響を与える。

(!.v120) を 1,000 回評価するのにどれだけかかるかを測定せよ。(timean-expression) 関数が an-expression の実行にかかる時間を決めることを思い出せ。

第3で最後の例として、単純化した二分木の高さを測る関数を使う。この例は、蓄積子スタイルのプログラミングが、単一の自己参照で定義されたデータだけでなく、あらゆる種類のデータに適用されることを示す。実際、リストや自然数と同様に、複雑なデータ定義にも一般に使われる。

関連する定義を次に示す：

```racket
(define-struct node [left right])
; A Tree is one of:
; – '()
; – (make-node Tree Tree)
(define example
  (make-node (make-node '() (make-node '() '())) '()))
```

これらの木は情報を持たない。葉は '() である。それでも、図184が示すように多くの異なる木があり、図はまた、これらのデータ片が木としてどう見えるかを伝える示唆的な図形も使う。

計算したい性質の1つが、そのような木の高さである：

```racket
(define (height abt)
  (cond
    [(empty? abt) 0]
    [else (+ (max (height (node-left abt))
                  (height (node-right abt))) 1)]))
```

やめ！ シグネチャとテストを与えよ。
図184の表は木の高さをどう測るかを示すが、概念はいくらか曖昧なままである：木の根から最も高い葉までのノード数か、あるいはそのような道上の接続の数かである。height 関数は第2の選択に従う。

> **図184: Some stripped-down binary trees**

```racket
(make-node
  (make-node '()
             (make-node '() '()))
  '())
```


> 原本は次の画像を含む（画像プレースホルダは図版パイプラインで埋め込み可）:
>
> [image: pict_284.png]
>
> [image: pict_285.png]
>
> [image: pict_286.png]


この関数を蓄積子スタイルの関数へ変換するため、標準の道筋に従う。適切なテンプレートから始める：

```racket
(define (height.v2 abt0)
  (local (; Tree??? -> N
; measures the height of abt
; accumulator...
          (define (height/a abt a)
            (cond
              [(empty? abt)...]
              [else
                (... (height/a (node-left abt)
... a...)...
... (height/a (node-right abt)
... a...)...)])))
    (height/a abt0...)))
```

いつものように、問題は蓄積子がどの知識を表すかを決めることである。明白な選択の1つは、たどった枝の数である：

> a は abt0 から abt に到達するのにかかるステップ数である。

この蓄積子不変条件を示すには、図による例が最適である。図184を再度見よ。一番下の木には2つの注釈があり、それぞれ1つの部分木を指している：

1. abt0 が完全な木で、abt が丸で囲んだ 1 が指す部分木なら、蓄積子の値は 1 でなければならない。abt の根から abt0 の根へ行くのにちょうど1ステップかかるからである。
2. 同じ精神で、2 とラベルされた部分木については、蓄積子は 2 である。この場所に到達するのに2ステップかかるからである。

前の2例と同様、不変条件は蓄積子の設計レシピの残りにどう従うかを基本的に命じる：a の初期値は 0、更新操作は add1、基底場合は蓄積された知識を返して使う。これをコードに翻訳すると、次の骨格定義が得られる：

```racket
(define (height.v2 abt0)
  (local (; Tree N -> N
; measures the height of abt
; accumulator a is the number of steps
; it takes to reach abt from abt0
          (define (height/a abt a)
            (cond
              [(empty? abt) a]
              [else
                (... (height/a (node-left abt)
                               (+ a 1))...
... (height/a (node-right abt)
                               (+ a 1))...)])))
    (height/a abt0 0)))
```

しかし、最初の2例とは対照的に、a は最終結果ではない。第2の cond 節では、2つの再帰呼び出しが2つの値を生む。構造的関数の設計レシピは、この場合の答えを定式化するためにそれらを組み合わせるよう命じる。上の点線は、これらの値を組み合わせる操作をまだ選ぶ必要があることを示す。

> **図185: The accumulator-style version of height**

```racket
; Tree -> N
; measures the height of abt0
(check-expect (height.v2 example) 3)
(define (height.v2 abt0)
  (local (; Tree N -> N
          ; measures the height of abt
          ; accumulator a is the number of steps
          ; it takes to reach abt from abt0
          (define (height/a abt a)
            (cond
              [(empty? abt) a]
              [else
               (max
                 (height/a (node-left abt)  (+ a 1))
                 (height/a (node-right abt) (+ a 1)))])))
    (height/a abt0 0)))
```


設計レシピに従うと、適切な関数を見つけるために2つの値を解釈する必要があることも分かる。height/a の目的文によれば、第1の値は左部分木の高さであり、第2は右部分木の高さである。abt 自体の高さに関心があり、高さは葉に到達するのにかかる最大のステップ数であることから、max 関数を使って適切なものを選ぶ。完全な定義は図185を見よ。

代替設計についての注 あるノードに到達するのにかかるステップ数を数えることに加え、蓄積子関数はこれまでに出会った最大の高さを保持することもできる。設計の考えに対する蓄積子文を次に示す：

> 第1の蓄積子は、abt0（の根）から abt に到達するのにかかるステップ数を表す。第2の蓄積子は、abt0 のうち abt の厳密に左側にある部分の高さを表す。

明らかに、この文は2つの蓄積子パラメータを持つテンプレートを仮定しており、これはこれまで出会ったことがない：

```racket
...; Tree N N -> N
; measures the height of abt
; accumulator s is the number of steps
; it takes to reach abt from abt0
; accumulator m is the maximal height of
; the part of abt0 that is to the left of abt
    (define (h/a abt s m)
      (cond
        [(empty? abt)...]
        [else
         (... (h/a (node-left abt)
... s...... m...)...
... (h/a (node-right abt)
... s...... m...)...)]))...
```

練習問題 498. height.v3 を完成させよ。
ヒント 図184の一番下の木は、1 と印された部分木の左側に部分木を含まない。2 と印された部分木の左側の部分には、根から木への完全な道が1つ含まれる。この道は2ステップからなる。

この第2の設計は、第1のものより複雑な蓄積子不変条件を持つ。その含意として、実装には第1のものより注意が必要である。同時に、明白な利点は伴わない。

私たちの論点は、異なる蓄積子不変条件が異なる変種を生むということである。同じ設計レシピに従い、両方の変種を体系的に設計できる。完全な関数定義ができたら、結果を比較対照し、証拠に基づいてどちらを残すかを決められる。終わり

練習問題 499. product の蓄積子スタイル版を設計せよ。これは数のリストの積を計算する関数である。蓄積子不変条件を定式化し、誰かにそれを検査してもらったら止めよ。

product の性能は、リストの長さを n として O(n) である。蓄積子版はこれを改善するか。

練習問題 500. how-many の蓄積子スタイル版を設計せよ。これはリスト上の項目数を決める関数である。不変条件を定式化し、誰かにそれを検査してもらったら止めよ。

how-many の性能は、リストの長さを n として O(n) である。蓄積子版はこれを改善するか。

(how-manysome-non-empty-list) を手評価するとき、関数が '() に到達するまでに n 回の add1 の適用が保留になる——ここで n はリスト上の項目数である。計算機科学者はときに、how-many がこれらの保留中の関数適用を表すために O(n) の空間を必要とすると言う。蓄積子は結果を計算するのに必要な空間量を減らすか。

> **注:** 計算機科学者はこの空間をスタック空間と呼ぶが、今のところこの用語は安全に無視してよい。

**練習問題 501. add-to-pi の蓄積子スタイル版を設計せよ。この関数は + を使わずに自然数を pi に加える：**

```racket
; N -> Number
; adds n to pi without using +
(check-within (add-to-pi 2) (+ 2 pi) 0.001)
(define (add-to-pi n)
  (cond
    [(zero? n) pi]
    [else (add1 (add-to-pi (sub1 n)))]))
```

蓄積子不変条件を定式化し、誰かにそれを検査してもらったら止めよ。

練習問題 502. 関数 palindrome を設計せよ。これは非空のリストを受け取り、最後の項目を中心にリストを鏡映して回文を構成する。(explode"abc") が与えられたとき、(explode"abcba") を生成する。

ヒント 関数合成で設計した解を次に示す：

```racket
; [NEList-of 1String] -> [NEList-of 1String]
; creates a palindrome from s0
(check-expect
  (mirror (explode "abc")) (explode "abcba"))
(define (mirror s0)
  (append (all-but-last s0)
          (list (last s0))
          (reverse (all-but-last s0))))
```

last については Auxiliary Functions that Generalize を見よ。all-but-last は同様の仕方で設計せよ。

この解は s0 を4回たどる：

1. all-but-last 経由、
2. last 経由、
3. 再び all-but-last 経由、および
4. reverse 経由。これは ISL+ 版の invert である。

all-but-last の結果に local 定義を使っても、関数は3回の走査を必要とする。これらの走査は「積み重なって」いないので関数の性能に壊滅的な影響はないが、蓄積子版は同じ結果を1回の走査で計算できる。

**練習問題 503. 練習問題 467 は暗黙に、Matrix を最初の行の最初の係数が 0 と異なるまで回転する関数の設計を求める。練習問題 467 の文脈では、解は生成的再帰関数を呼び、先頭位置に 0 を見つけると最初の行を末尾へずらして新しい行列を作る。解を次に示す：**

```racket
; Matrix -> Matrix
; finds a row that doesn't start with 0 and
; uses it as the first one
; generative moves the first row to last place
; no termination if all rows start with 0
(check-expect (rotate '((0 4 5) (1 2 3)))
              '((1 2 3) (0 4 5)))
(define (rotate M)
  (cond
    [(not (= (first (first M)) 0)) M]
    [else
     (rotate (append (rest M) (list (first M))))]))
```

やめ！ すべての行が 0 で始まるときエラーを合図するよう、この関数を修正せよ。

大きな Matrix のインスタンスでこの関数を測ると、驚くべき結果が得られる：

> M の行数 1000 2000 3000 4000 5000rotate 17 66 151 272 436

行数が 1,000 から 5,000 へ増えるにつれ、rotate が費やす時間は5倍ではなく20倍に増える。

問題は、rotate が append を使うことである。append は (restM) のようなまったく新しいリストを作り、末尾に (firstM) を加えるだけである。M が 1,000 行からなり、最後の行だけが非 0 係数を持つなら、およそ

> [image: pict_287.png]

個のリストになる。M が 5,000 行からなるなら、いくつのリストが得られるか。

さて、蓄積子スタイル版が生成的な版より速いと推測したとしよう。rotate の構造的再帰版の蓄積子テンプレートを次に示す：

```racket
(define (rotate.v2 M0)
  (local (; Matrix... -> Matrix
; accumulator...
          (define (rotate/a M seen)
            (cond
              [(empty? (rest M))...]; Can this be simplified to (empty? M)
              [else (... (rotate/a (rest M)
... seen...)
...)])))
    (rotate/a M0...)))
```

目標は、先頭係数が 0 のとき最初の行を覚え、再帰ごとに append を使わないことである。

蓄積子文を定式化せよ。それから蓄積子設計レシピに従い、上記の関数を完成させよ。先頭が 0 の行からなり、最後の行だけが例外である Matrix での実行速度を測定せよ。設計を正しく完了すれば、関数はかなり速い。

練習問題 504. to10 を設計せよ。数字のリストを消費し、対応する数を生成する。リストの最初の項目が最上位桁である。したがって '(102) に適用すると 102 を生成する。

領域知識 小学校で、結果は次で決まることを思い出すかもしれない：
[image: pict_288.png]

練習問題 505. 関数 is-prime を設計せよ。これは自然数を消費し、素数なら #true を、そうでなければ #false を返す。

領域知識 数 n は、n - 1 と 2 のあいだのどの数でも割り切れないとき素数である。

ヒント N [>=1] の設計レシピは次のテンプレートを示唆する：

```racket
; N [>=1] -> Boolean
; determines whether n is a prime number
(define (is-prime? n)
  (cond
    [(= n 1)...]
    [else (... (is-prime? (sub1 n))...)]))
```

このテンプレートはすぐに、関数が再帰するにつれ初期引数 n を忘れることを告げる。n が (-n1)、(-n2) などで割り切れるかどうかを決めるには n が間違いなく必要なので、蓄積子スタイルの関数が必要だと分かる。

速度についての注 蓄積子スタイルの関数に初めて出会うプログラマは、それらが常に平易な対応物より速いという印象をしばしば受ける。そこで練習問題 497 の解を見てみよう：

> **注:** これらの時間の説明は
本書の範囲を超える。

>!.v1 5.760 5.780 5.800 5.820 5.870 5.806!.v2 5.970 5.940 5.980 5.970 6.690 6.111

表の上の行は (!.v120) の5回の実行の秒数を示し、下の行は (!.v220) の実行時間を列挙する。最後の列は平均を示す。要するに、表は人々が早まった結論に飛びつくことを示す。少なくとも1つの蓄積子スタイル関数の性能は元のものより悪い。偏見を信じるな。代わりに、自分のプログラムの性能特性を自分で測定せよ。終わり

練習問題 506. map の蓄積子スタイル版を設計せよ。

**練習問題 507. 練習問題 257 は、本書の最初の2部の設計レシピと指針で foldl をどう設計するかを説明する：**

```racket
(check-expect (f*ldl + 0 '(1 2 3))
              (foldl + 0 '(1 2 3)))
(check-expect (f*ldl cons '() '(a b c))
              (foldl cons '() '(a b c)))

; version 1
(define (f*ldl f i l)
  (foldr f i (reverse l)))
```

すなわち、foldl は与えられたリストを反転し、その中間リストに対して foldr で与えられた関数を畳み込む結果である。

f*ldl 関数は明らかにリストを2回たどるが、すべての関数を設計すると、どれだけ余分に働かなければならないかが明らかになる：

```racket
; version 2
(define (f*ldl f i l)
  (local ((define (reverse l)
            (cond
              [(empty? l) '()]
              [else (add-to-end (first l)
                                (reverse (rest l)))]))
          (define (add-to-end x l)
            (cond
              [(empty? l) (list x)]
              [else (cons (first l)
                          (add-to-end x (rest l)))]))
          (define (foldr l)
            (cond
              [(empty? l) i]
              [else (f (first l) (foldr (rest l)))])))
    (foldr (reverse l))))
```

reverse がリスト上の各項目についてリストを1回たどらなければならないと分かっている。つまり f*ldl は実際、長さ n のリストに対して
[image: pict_289.png] 回の走査を行う。幸い、蓄積子でこのボトルネックをどう除くかを知っている：

```racket
; version 3
(define (f*ldl f i l)
  (local ((define (reverse/a l a)
            (cond
              [(empty? l) a]
              [else (reverse/a (rest l)
                              (cons (first l) a))]))
          (define (foldr l)
            (cond
              [(empty? l) i]
              [else
               (f (first l) (foldr (rest l)))])))
    (foldr (reverse/a l '()))))
```

reverse が蓄積子を使うと、実際にはリストの2回の走査という見かけの性能が得られる。問いは、局所的に定義された foldr に蓄積子を加えることで、これを改善できるかである：

```racket
; version 4
(define (f*ldl f i l0)
  (local ((define (foldr/a a l)
            (cond
              [(empty? l) a]
              [else
               (foldr/a (f (first l) a) (rest l))])))
    (foldr/a i l0)))
```

関数に蓄積子を装備するとリストがたどられる順序が逆になるので、リストの初期の反転は余分である。

課題 1 foldl のシグネチャを思い出せ：

```racket
; [X Y] [X Y -> Y] Y [List-of X] -> Y
```

これは f*ldl のシグネチャでもある。foldr/a のシグネチャとその蓄積子不変条件を定式化せよ。ヒント l0 と l の差が (listx1x2x3) だと仮定せよ。そのとき a は何か。

foldr/a がこの珍しい順序——まず蓄積子、次にリスト——で引数を消費する理由も疑問に思うかもしれない。この順序の理由を理解するには、代わりに foldr/a が f も——第1引数として——消費すると想像せよ。この時点で、foldr/a が foldl であることは十分に明らかになる：

```racket
; version 5
(define (f*ldl f i l)
  (cond
    [(empty? l) i]
    [else (f*ldl f (f (first l) i) (rest l))]))
```

課題 2 蓄積子スタイルのアプローチで build-l*st を設計せよ。関数は次のテストを満たさなければならない：

```racket
(check-expect (build-l*st n f) (build-list n f))
```

任意の自然数 n と関数 f について。

### 32.4 マウス付きグラフィカル・エディタ（A Graphical Editor, with Mouse）

A Graphical Editor は1行エディタの概念を導入し、グラフィカル・エディタの作成についての一連の練習問題を提示する。思い出すと、グラフィカル・エディタはキーイベントを文字列上の編集動作として解釈する対話プログラムである。特に、利用者が左右の矢印キーを押すとカーソルが左右に動き、同様に削除キーを押すと編集中のテキストから 1String が取り除かれる。エディタ・プログラムは、構造体の中で2つの文字列を組み合わせるデータ表現を使う。A Graphical Editor, Revisited はこれらの練習問題を再開し、同じプログラムが、2つの文字列を組み合わせる別のデータ構造から大きく恩恵を受け得ることを示す。

これらの節はどちらも、ナビゲーションのためのマウス動作を扱わない。現代の応用はすべてこの機能を支えるにもかかわらずである。マウスイベントの基本的な難しさは、カーソルを適切な位置に置くことである。プログラムが1行のテキストを扱うので、(x,y) でのマウスクリックは明らかに、x 位置に、またはその付近に見える文字のあいだにカーソルを置こうとする。本節がその隙間を埋める。

A Graphical Editor, Revisited からの関連定義を思い出せ：

```racket
(define FONT-SIZE 11)
(define FONT-COLOR "black")

; [List-of 1String] -> Image
; renders a string as an image for the editor
(define (editor-text s)
  (text (implode s) FONT-SIZE FONT-COLOR))

(define-struct editor [pre post])
; An Editor is a structure:
;   (make-editor [List-of 1String] [List-of 1String])
; interpretation if (make-editor p s) is the state of
; an interactive editor, (reverse p) corresponds to
; the text to the left of the cursor and s to the
; text on the right
```

**練習問題 508. 構造的設計レシピを使い、split-structural を設計せよ。この関数は 1String のリスト ed と自然数 x を消費する。前者はある Editor 内の完全な文字列を表し、後者はマウスクリックの x 座標である。関数は次を生成する**

```racket
(make-editor p s)
```

ただし (1) p と s が ed をなし、(2) x が p の画像より大きく、s 上の最初の 1String（もしあれば）を p に延ばした画像より小さい。

第1の条件を ISL+ 式で表すと次のとおり：

```racket
(string=? (string-append p s) ed)
```

第2は

```racket
(<= (image-width (editor-text p))
    x
    (image-width (editor-text (append p (first s)))))
```

であり、(cons?s) を仮定する。

ヒント (1) x 座標は左からの距離を測る。したがって関数は、ed のますます大きな接頭辞が与えられた幅に収まるかを検査しなければならない。収まらない最初のものが望ましい Editor の pre フィールドに対応し、ed の残りが post フィールドに対応する。

(2) この関数の設計は、例とテストを徹底的に開発することを求める。Intervals, Enumerations, and Itemizations を見よ。

練習問題 509. 関数 split を設計せよ。蓄積子設計レシピを使い、練習問題 508 の結果を改善せよ。結局のところ、ヒントはすでに、関数が正しい分割点を見つけたときリストの両方の部分が必要であり、一方は再帰のため明らかに失われることを指摘している。

この練習問題を解いたら、A Graphical Editor, Revisited の主関数にマウスクリックの節を装備せよ。マウスクリックでカーソルを動かして実験すると、他の機器で使う応用とまったく同じようには振る舞わないことに気づくだろう——split がすべてのテストに通るにもかかわらずである。

エディタのようなグラフィカル・プログラムは、最良の「ルック・アンド・フィール」体験を生み出すために実験を求める。この場合、エディタはカーソルの配置が単純すぎる。コンピュータ上の応用は分割点を決めたあと、どの文字の区切りが x 座標に近いかも決め、そこにカーソルを置く。

## 33 蓄積のさらなる使用（More Uses of Accumulation）

本章では、蓄積子のさらに3つの使い方を示す。第1節は、木を処理する関数と組み合わせた蓄積子の使用を扱う。ISL+ のコンパイルを例として用いる。第2節では、データ表現の内側に蓄積子を置きたいことがある理由と、その置き方を説明する。最後の節は、フラクタルの描画に関する議論を再開する。

### 33.1 蓄積子と木（Accumulators and Trees）

DrRacket に ISL+ プログラムを実行するよう求めると、DrRacket はプログラムを、あなたの特定のコンピュータ向けの命令に翻訳する。この過程はコンパイルと呼ばれ、その作業を行う DrRacket の部分はコンパイラと呼ばれる。コンパイラが ISL+ プログラムを翻訳する前に、すべての変数が define、define-struct、または lambda を介して宣言されていることを検査する。

やめ！ 完全な ISL+ プログラムとして x、(lambda(y)x)、および (x5) を DrRacket に入力し、それぞれを実行するよう求めよ。何が見えると予想するか。

この考えをサンプル問題として定式化しよう：

> サンプル問題 あなたは ISL+ コンパイラの一部を再作成するよう雇われた。具体的には、次の言語断片を扱うのが任務である。これは多くのプログラミング言語マニュアルが用いるいわゆる文法記法で指定されている：
> expression=variable|(λ (variable) expression)|(expression expression)インターメッツォ1から思い出してほしいが、文法は = を「のいずれかである」に、| を「または」に置き換えて声に出して読める。λ 式は名前のない関数であることを思い出せ。それらは本体の中でパラメータを束縛する。逆に、変数の出現は、同じ名前をパラメータとして指定する周囲の λ によって宣言される。同じ問題をプログラマの視点から扱う Intermezzo 3: Scope and Abstraction を再訪するとよい。「束縛出現（binding occurrence）」「被束縛出現（bound occurrence）」「自由（free）」という用語を探せ。上記の言語断片のデータ表現を開発せよ。変数には記号を使え。次に、宣言されていないすべての変数を '*undeclared に置き換える関数を設計せよ。

> **注:** ギリシャ文字 λ を lambda の代わりに用いるのは、この練習問題が ISL+ を単なるプログラミング言語としてではなく、研究対象として扱うことを示すためである。

この問題は翻訳過程の多くのステップを代表しており、同時に、蓄積子スタイルの関数についての優れたケーススタディでもある。

問題に深入りする前に、このミニ言語のいくつかの例を見て、lambda について知っていることを思い出そう：

- (λ(x)x) は、与えられたものをそのまま返す関数であり、恒等関数としても知られる。
- (λ(x)y) は、引数が何であれ y を返す関数のように見えるが、y は宣言されていない。
- (λ(y)(λ(x)y)) は、ある値 v を与えられると、常に v を返す関数を生成する関数である。
- ((λ(x)x)(λ(x)x)) は恒等関数をそれ自身に適用する。
- ((λ(x)(xx))(λ(x)(xx))) は短い無限ループである。
- (((λ(y)(λ(x)y))(λ(z)z))(λ(w)w)) は複雑な式であり、停止するかどうかを確かめるには ISL+ で実行するのが最善である。

実際、上記の ISL+ 式はすべて DrRacket で実行でき、それらについて書かれたことを確認できる。

練習問題 511. 上記の例における各束縛出現のスコープを説明せよ。被束縛出現から束縛出現へ矢印を描け。

言語のデータ表現を開発するのは簡単である。特に、その記述が文法記法を用いているからである。1つの可能性は次のとおり：

```racket
; A Lam is one of:
; – a Symbol
; – (list 'λ (list Symbol) Lam)
; – (list Lam Lam)
```

quote のおかげで、このデータ表現は ISL+ の部分集合における式のデータ表現を簡単に作れる：

```racket
(define ex1 '(λ (x) x))
(define ex2 '(λ (x) y))
(define ex3 '(λ (y) (λ (x) y)))
(define ex4 '((λ (x) (x x)) (λ (x) (x x))))
```

これら4つのデータ例は、上記の式の一部の表現である。やめ！ 残りの例のデータ表現を作れ。

練習問題 512. is-var?、is-λ?、および is-app? を定義せよ。すなわち、変数と λ 式と適用とを区別する述語である。

また次も定義せよ：

- λ-para。λ 式からパラメータを取り出す。
- λ-body。λ 式から本体を取り出す。
- app-fun。適用から関数を取り出す。
- app-arg。適用から引数を取り出す。

これらの述語とセレクタがあれば、実質的に構造指向のデータ表現を定義したかのように振る舞える。

declareds を設計せよ。これは λ 項の中で λ のパラメータとして使われるすべての記号のリストを生成する。重複する記号は気にしなくてよい。

練習問題 513. 同じ ISL+ の部分集合について、リストの代わりに構造体を使うデータ表現を開発せよ。また、データ定義に従い、ex1、ex2、および ex3 のデータ表現を提供せよ。

構造的設計レシピに従う。ステップ2と3の成果物は次のとおり：

```racket
; Lam -> Lam
; replaces all symbols s in le with '*undeclared
; if they do not occur within the body of a λ
; expression whose parameter is s

(check-expect (undeclareds ex1) ex1)
(check-expect (undeclareds ex2) '(λ (x) *undeclared))
(check-expect (undeclareds ex3) ex3)
(check-expect (undeclareds ex4) ex4)

(define (undeclareds le0)
  le0)
```

undeclareds が ex4 を処理することを期待していることに注意せよ。実行するとその式は永遠にループするが、コンパイラはプログラムを実行するのではなく、読み取り、別のものを生成する。

目的文をよく見ると、この関数に蓄積子が必要であることが直接示唆される。undeclareds のテンプレートを調べると、さらに明確になる：

```racket
(define (undeclareds le)
  (cond
    [(is-var? le)...]
    [(is-λ? le) (... (undeclareds (λ-body le))...)]
    [(is-app? le)
     (... (undeclareds (app-fun le))
... (undeclareds (app-arg le))...)]))
```

undeclareds が λ 式（の表現）の本体に対して再帰するとき、(λ-parale)、すなわち宣言された変数を忘れてしまう。

そこで、蓄積子スタイルのテンプレートから始めよう：

```racket
(define (undeclareds le0)
  (local
    (; Lam??? -> Lam
; accumulator a represents...
     (define (undeclareds/a le a)
       (cond
         [(is-var? le)...]
         [(is-λ? le)
          (... (undeclareds/a (λ-body le)
... a...)...)]
         [(is-app? le)
          (... (undeclareds/a (app-fun le)
... a...)
... (undeclareds/a (app-arg le)
... a...)...)])))
    (undeclareds/a le0...)))
```

この文脈で、蓄積子不変条件を定式化できる：

> a は、le0 の頂部から le の頂部への経路上で出会った λ パラメータのリストを表す。

たとえば、le0 が

```racket
'(((λ (y) (λ (x) y)) (λ (z) z)) (λ (w) w))
```

であり、le が強調された部分木であるとき、a は y を含む。図186の左側は、同じ例の図による説明を示す。Lam 式を逆さまの木として示している。すなわち、根が上にある。`@` ノードは2つの子孫を持つ適用を表し、他のノードは自明である。この木の図では、太字の経路が le0 から le へ、単一の変数宣言を通ってつながっている。

同様に、同じデータの別の部分木を選ぶと、

```racket
'(((λ (y) (λ (x) y)) (λ (z) z)) (λ (w) w))
```

蓄積子は 'y と 'x の両方を含む。図186の右側は、この点を再び示している。ここでは太字の経路が2つの 'λ ノードを通って枠で囲まれた部分木へ至り、蓄積子は太字の経路に沿って宣言された変数のリストである。

> **図186: Lam terms as trees**

> 原本は次の画像を含む（画像プレースホルダは図版パイプラインで埋め込み可）:
>
> [image: pict_290.png]
>
> [image: pict_291.png]


蓄積子のデータ表現とその不変条件が定まったので、残りの設計上の問いに答えられる：

- 初期蓄積子の値として '() を選ぶ。
- (λ-parale) を a に加えるのに cons を使う。
- undeclareds/a が変数を扱う節で蓄積子を活用する。具体的には、その変数が宣言のスコープ内にあるかを蓄積子で検査する。

図187は、これらの考えを完全な関数定義へどう翻訳するかを示す。蓄積子の名前 declareds に注意せよ。蓄積子不変条件の背後にある鍵となる考えを伝え、プログラマが定義を理解する助けになる。基底の場合は ISL+ の member? を使い、変数 le が declareds にあるかどうかを判定し、なければ '*undeclared に置き換える。2番目の cond 節は local を使い、拡張された蓄積子 newd を導入する。para は式の再構築にも使われるので、独自の local 定義を持つ。最後に、最後の節は関数適用に関するものであり、変数を宣言せず、直接使うこともない。その結果、3つの節のうち圧倒的に最も単純である。

> **図187: Finding undeclared variables**

```racket
; Lam -> Lam
(define (undeclareds le0)
  (local (; Lam [List-of Symbol] -> Lam
          ; accumulator declareds is a list of all λ
          ; parameters on the path from le0 to le
          (define (undeclareds/a le declareds)
            (cond
              [(is-var? le)
               (if (member? le declareds) le '*undeclared)]
              [(is-λ? le)
               (local ((define para (λ-para le))
                       (define body (λ-body le))
                       (define newd (cons para declareds)))
                 (list 'λ (list para)
                   (undeclareds/a body newd)))]
              [(is-app? le)
               (local ((define fun (app-fun le))
                       (define arg (app-arg le)))
               (list (undeclareds/a fun declareds)
                     (undeclareds/a arg declareds)))])))
    (undeclareds/a le0 '())))
```


練習問題 514. x が自由でも被束縛でも現れる ISL+ 式を作れ。それを Lam の要素として定式化せよ。undeclareds はあなたの式で正しく動くか。

**練習問題 515. 次の式を考えよ：**

```racket
(λ (*undeclared) ((λ (x) (x *undeclared)) y))
```

そう、これは *undeclared を変数として使っている。これを Lam で表現し、この式に対して undeclareds が何を生成するかを確認せよ。

undeclareds を修正し、'x の自由な出現を

```racket
(list '*undeclared 'x)
```

に置き換え、被束縛の 'y を

```racket
(list '*declared 'y)
```

に置き換えるようにせよ。

こうすると問題箇所が一義的に識別され、DrRacket のようなプログラム開発環境がエラーを強調表示するのに使える。

注 変数の出現を適用の表現で置き換える技巧はぎこちなく感じる。気に入らなければ、代わりに記号 '*undeclared:x と 'declared:y を合成することを検討せよ。

練習問題 516. 練習問題513の構造体ベースのデータ表現向けに、undeclareds 関数を再設計せよ。

> **図188: Static distances**

> 原本は次の画像を含む（画像プレースホルダは図版パイプラインで埋め込み可）:
>
> [image: pict_292.png]
>
> [image: pict_293.png]


**練習問題 517. static-distance を設計せよ。この関数は変数のすべての出現を、宣言している λ がどれだけ離れているかを表す自然数に置き換える。図188は、次の項についてこの考えを示す：**

```racket
'((λ (x) ((λ (y) (y x)) x)) (λ (z) z))
```

グラフィカルな形で示している。変数の出現から対応する変数宣言へ向かう点線の矢印を含む。右側では、矢印のない同じ形の木を示す。'λ ノードには名前がなく、変数の出現はどの 'λ が変数を宣言するかを指定する自然数に置き換えられている。各自然数 n は、束縛出現が n ステップ上——Lam 木の根に向かって——にあることを言う。値 0 は根への経路上の最初の 'λ を、1 は2番目のものを表す、といった具合である。

ヒント undeclareds/a の undeclareds 蓄積子は、le から le0 への経路上のすべてのパラメータのリストであり、逆順——最後に見たものがリストの先頭——である。

### 33.2 蓄積子付きのデータ表現（Data Representations with Accumulators）

Intermezzo 5: The Cost of Computation の終わりは、`*SL` がコンテナ、たとえばリストのサイズを、それらを走査して測ることを説明し、他のプログラミング言語がサイズを計算するのに異なる、より安価な方法を使うことをほのめかしている。本節では、データ表現への蓄積子の追加によって、この考えをどう実装するかを示す。

> **注:** この考えの早い例については Finite State Machines を見よ。

`*SL` における遍在するリストを考えよ。すべてのリストは cons と '() から構成される。たとえば quote や list のような操作は、これら2つに対する単なる略記である。What Is '(), What Is cons が示すように、適切な構造体型と関数定義によって BSL でリストを模倣することも可能である。

> **図189: An implementation of lists in BSL**

```racket
(define-struct pair [left right])
; ConsOrEmpty is one of:
; – '()
; – (make-pair Any ConsOrEmpty)

; Any ConsOrEmpty -> ConsOrEmpty
(define (our-cons a-value a-list)
  (cond
    [(empty? a-list) (make-pair a-value a-list)]
    [(pair? a-list) (make-pair a-value a-list)]
    [else (error "our-cons: ...")]))

; ConsOrEmpty -> Any
; extracts the left part of the given pair
(define (our-first mimicked-list)
  (if (empty? mimicked-list)
      (error "our-first: ...")
      (pair-left mimicked-list)))
```


図189は基本的な考えを思い出させる。やめ！ いま our-rest を定義できるか。

鍵となる洞察は、pair の構造体型定義に第3のフィールドを加えられることである：

```racket
(define-struct cpair [count left right])
; A [MyList X] is one of:
; – '()
; – (make-cpair (tech "N") X [MyList X])
; accumulator the count field is the number of cpairs
```

蓄積子の文が述べるように、追加のフィールドは、リストを作るのに使われた cpair インスタンスの数を追跡するのに使われる。すなわち、リストの構築についての事実を覚えている。このような種類の構造体フィールドをデータ蓄積子と呼ぶ。

主要なリスト構成子にフィールドを加えるのは無料ではない。まず、実際にプログラムが利用できる検査付き版の構成子の変更が必要である：

```racket
; data definitions, via a constructor-function
(define (our-cons f r)
  (cond
    [(empty? r) (make-cpair 1 f r)]
    [(cpair? r) (make-cpair (+ (cpair-count r) 1) f r)]
    [else (error "our-cons:...")]))
```

拡張されるリストが '() なら、count は 1 で埋められる。そうでなければ、関数は与えられた cpair から長さを計算する。

これで our-length の関数定義は明白である：

```racket
; Any -> N
; how many items does l contain
(define (our-length l)
  (cond
    [(empty? l) 0]
    [(cpair? l) (cpair-count l)]
    [else (error "my-length:...")]))
```

この関数は任意の種類の値を消費する。'() と cpair のインスタンスについては自然数を生成し、そうでなければエラーを合図する。

count フィールドの追加に関する第2の問題は性能である。実際、懸念は2つある。一方では、すべてのリスト構成に追加フィールドが付くので、メモリ消費が33%増加する。他方では、フィールドの追加は our-cons がリストを構成する速さを下げる。拡張されるリストが '() か cpair のインスタンスであるかの検査に加えて、構成子はいまリストのサイズを計算する。この計算は一定量の時間しか消費しないが、our-cons のあらゆる使用に課される——そして本書が cons をどれほど頻繁に使い、結果のリストの長さを決して計算しないかを考えてみよ！

練習問題 518. our-cons が、入力のサイズに関係なく、結果を計算するのに一定量の時間を要することを論ぜよ。

練習問題 519. length を定数時間の関数にするために、すべてのプログラムに対して cons に追加コストを課すのは受け入れられるか。

リストへの count フィールドの追加は疑問の余地があるが、データ蓄積子が解を見つけるうえで決定的な役割を果たすこともある。次の例は、いわゆる人工知能をボードゲームをプレイするプログラムに加えることについてであり、そのデータ蓄積子は絶対的な必要性である。

ボードゲームをしたりパズルを解いたりするとき、各段階で可能な手について考える傾向がある。上達すると、この第1手のあとの可能性まで想像することもあるかもしれない。結果はいわゆるゲーム木であり、ルールが許すすべての可能な手の木（の一部）である。問題から始めよう：

> サンプル問題 上司が次の話をしてくる。「昔々、3人の人食い人種が3人の宣教師をジャングルの中で案内していた。彼らは最寄りの宣教所へ向かう途中だった。しばらくして、致命的な蛇や魚で満ちた広い川に着いた。船なしに川を渡る方法はなかった。幸い、短い捜索のあと、2本のオール付きの手漕ぎボートを見つけた。不幸なことに、そのボートは全員を運ぶには小さすぎた。一度にせいぜい2人しか運べなかった。さらに悪いことに、川の幅のせいで誰かがボートを漕いで戻らなければならなかった。「宣教師は人食い人種を信頼できなかったので、6人全員を安全に川を渡らせる計画を考えなければならなかった。問題は、ある場所で人食い人種が宣教師より多くなるとすぐに、これらの人食い人種が宣教師を殺して食べることだった。我々の宣教師は、川のどちらの岸でも宣教師が少数派にならないことを保証する計画を考案しなければならなかった。ただし、人食い人種はそれ以外では協力すると信頼できた。具体的には、潜在的な食料を見捨てることはなく、宣教師も潜在的な改宗者を見捨てることはなかった。」上司は特定の設計課題を割り当てないが、会社がそのようなパズルを解くプログラムを設計（して販売）できるかどうかを探りたいと思っている。

パズルはボードゲームではないが、このプログラムはゲーム木の考えを、可能な限り最も直接的な仕方で例示する。

原理的には、このようなパズルを手で解くのはかなり素直である。大まかな考えは次のとおり。問題の状態の図による表現を選ぶ。我々のものは3部構成の箱からなる。左側は宣教師と人食い人種を表し、中央は川とボートを組み合わせ、第3部は川の右岸である。次の初期状態の表現を見よ：

> [image: pict_294.png]

黒い円は宣教師、白い円は人食い人種を表す。全員が左岸にいる。ボートも左側にある。右側には誰もいない。さらに2つの状態がある：

> [image: pict_295.png]
>
> [image: pict_296.png]

1つ目は最終状態で、全員とボートが川の右岸にいる。2つ目は中間状態を描いており、2人がボートと共に左側に、4人が右側にいる。

> **図190: Creating a game tree**

> 原本は次の画像を含む（画像プレースホルダは図版パイプラインで埋め込み可）:
>
> [image: pict_297.png]


パズルの状態を書き下す方法ができたので、各段階での可能性について考えられる。そうすると、可能な手の木が得られる。図190は、そのような木の最初の2層半をスケッチしている。最も左の状態が初期状態である。ボートは最大2人しか運べず、少なくとも1人が漕がなければならないので、探るべき可能性は5つある：人食い人種が1人で渡る、人食い人種が2人で渡る、宣教師1人と人食い人種1人が行く、宣教師が1人で渡る、または宣教師が2人で渡る。これらの可能性は、初期状態から5つの中間状態へ向かう5本の矢印で表される。

これら5つの中間状態のそれぞれについて、同じゲームを再びプレイできる。図190では、新しい状態のうち中央（3番目）のものについてゲームがどう続くかを見る。右岸には2人しかいないので、可能性は3つある：人食い人種が戻る、宣教師が戻る、または両方が戻る。したがって、3本の矢印が中央の状態を、木の右側の3つの状態につなぐ。この可能性の木を体系的に描き続ければ、やがて最終状態を発見する。

図190を改めて見ると、可能性の木を生成するこの素朴なアプローチには2つの問題があることがわかる。1つ目は、右側の中央の状態を初期状態につなぐ破線の矢印である。これは、右側から左側へ2人を漕いで戻すとパズルが初期状態に戻ることを示し、つまりやり直しになることを意味し、明らかに望ましくない。2つ目の問題は、右上隅に星印のある状態に関する。どちらの場合も、左岸に白い円の人食い人種が黒い円の宣教師より多くおり、人食い人種が宣教師を食べることになる。再び、そのような状態を避けるのが目標であり、これらの手は望ましくない。

このパズルをプログラムに変える1つの方法は、ある与えられた状態から何らかの最終状態——ここではその最終状態——に到達可能かどうかを判定する関数を設計することである。適切な関数定義は次のとおり：

```racket
; PuzzleState -> PuzzleState
; is the final state reachable from state0
; generative creates a tree of possible boat rides
; termination???

(check-expect (solve initial-puzzle) final-puzzle)

(define (solve state0)
  (local (; [List-of PuzzleState] -> PuzzleState
; generative generates the successors of los
          (define (solve* los)
            (cond
              [(ormap final? los)
               (first (filter final? los))]
              [else
               (solve* (create-next-states los))])))
    (solve* (list state0))))
```

補助関数は生成的再帰を使い、可能性のリストが与えられたとき、すべての新しい可能性を生成する。与えられた可能性の1つが最終状態なら、関数はそれを返す。

明らかに、solve はかなり汎用的である。PuzzleStates の集まり、最終状態を認識する関数、およびすべての「後続」状態を作る関数を定義するかぎり、solve はあなたのパズルで動ける。

練習問題 520. solve* 関数は、n + 1 回のボート移動を要する状態を見る前に、n 回のボート移動で到達可能なすべての状態を生成する。たとえそれらのボート移動の一部が以前に出会った状態に戻るとしてもである。この体系的な木の走査の仕方のおかげで、solve* は無限ループに入れない。なぜか。用語 木やグラフをこのように探索する方法は、幅優先探索と呼ばれる。

練習問題 521. 宣教師と人食い人種のパズルの状態の表現を開発せよ。図による表現と同様に、データ表現は川の各岸の宣教師と人食い人種の人数、およびボートの位置を記録しなければならない。

PuzzleState の記述は新しい構造体型を求める。上記の初期、中間、および最終状態を、あなたの表現で表せ。

与えられた状態で全員が川の右岸にいるかどうかを検出する関数 final? を設計せよ。

宣教師と人食い人種のパズルの状態を画像に写像する関数 render-mc を設計せよ。

問題は、最終状態を返しても、プレイヤーが初期状態から最終状態へどう到達できるかについては何も述べないことである。言い換えると、create-next-states は、与えられた状態から返される状態へどう到達するかを忘れてしまう。そしてこの状況は明らかに蓄積子を求めるが、同時に、蓄積された知識は solve* や他のどの関数ではなく、個々の PuzzleState ごとに関連付けるのが最善である。

練習問題 522. 練習問題521の表現を修正し、状態がそこに至るまでに辿った状態の列を記録するようにせよ。状態のリストを使え。

追加フィールドを説明する蓄積子の文を、データ定義とともに明確に述べ、書き残せ。

必要に応じて、この表現向けに final? または render-mc を修正せよ。

練習問題 523. create-next-states 関数を設計せよ。宣教師と人食い人種の状態のリストを消費し、ボートの移動で到達できるすべての状態のリストを生成する。

create-next-states の最初の草稿では蓄積子を無視せよ。ただし、人食い人種が宣教師を食べられる状態を生成しないようにせよ。

2番目の設計では、状態構造体の蓄積子フィールドを更新し、現在の状態に至る途中で出会った状態を除外するのに使え。

練習問題 524. 蓄積子指向のデータ表現を活用して solve を修正せよ。改訂した関数は、初期 PuzzleState から最終状態へ至る状態のリストを生成する。

また、このリストから、render-mc を使って画像を生成し、ムービーを作ることも検討せよ。run-movie を使ってムービーを表示せよ。

### 33.3 結果としての蓄積子（Accumulators as Results）

図156をもう一度見よ。シェルピンスキーの三角形と、それをどう作るかの提案を表示している。具体的には、右側の画像は過程の背後にある生成的な考えの1つの版を説明する：

> 与えられた問題は三角形である。三角形がそれ以上分割するには小さすぎるとき、アルゴリズムは何もしない。そうでなければ、3辺の中点を見つけ、外側の3つの三角形を再帰的に扱う。

対照的に、Fractals, a First Taste はシェルピンスキーの三角形を代数的に合成する方法を示しており、その過程はこの記述に対応しない。

大半のプログラマは、「描く」が何らかのキャンバスに三角形を加える動作を意味すると期待する。2htdp/image ティーチパックの scene+line 関数が、この考えを具体化する。この関数は画像 s と2点の座標を消費し、これら2点を通る線を s に加える。scene+line から add-triangle へ、そしてそこから add-sierpinski へ一般化するのは簡単である：

> サンプル問題 add-sierpinski 関数を設計せよ。画像と、三角形を記述する3つの Posn を消費する。後者を使い、この画像にシェルピンスキーの三角形を加える。

この問題が、シェルピンスキーの三角形をどう描くかについての上記の過程の記述を暗黙に参照していることに注意せよ。言い換えると、古典的な生成的再帰の問題に直面しており、生成的再帰の古典的なテンプレートと4つの中心的な設計の問いから始められる：

- 三角形が分割するには小さすぎるとき、問題は自明である。
- 自明な場合、関数は与えられた画像を返す。
- そうでなければ、与えられた三角形の辺の中点を求めて別の三角形を加える。各「外側」の三角形は、その後再帰的に処理される。
- これらの再帰ステップのそれぞれが画像を生成する。残る問いは、これらの画像をどう組み合わせるかである。

> **図191: Accumulators as results of generative recursions, a skeleton**

```racket
; Image Posn Posn Posn -> Image
; generative adds the triangle (a, b, c) to scene0,
; subdivides it into three triangles by taking the
; midpoints of its sides; stop if (a, b, c) is too small
(define (add-sierpinski scene0 a b c)
  (cond
    [(too-small? a b c) scene0]
    [else
     (local
       ((define scene1 (add-triangle scene0 a b c))
        (define mid-a-b (mid-point a b))
        (define mid-b-c (mid-point b c))
        (define mid-c-a (mid-point c a))
        (define scene2
          (add-sierpinski scene0 a mid-a-b mid-c-a))
        (define scene3
          (add-sierpinski scene0 b mid-b-c mid-a-b))
        (define scene4
          (add-sierpinski scene0 c mid-c-a mid-b-c)))
       ; —IN—
       (... scene1 ... scene2 ... scene3 ... scene4 ...))]))
```


図191は、これらの答えを骨格定義に翻訳した結果を示す。各中点は2回使われるので、骨格は local を使い、生成的ステップを ISL+ で定式化する。local 式は3つの新しい中点と、add-sierpinski の3つの再帰適用を導入する。本体の点は、シーンの組み合わせを示唆する。

**練習問題 525. 骨格が含意する願望リストに取り組め：**

```racket
; Image Posn Posn Posn -> Image
; adds the black triangle a, b, c to scene
(define (add-triangle scene a b c) scene)

; Posn Posn Posn -> Boolean
; is the triangle a, b, c too small to be divided
(define (too-small? a b c)
  #false)

; Posn Posn -> Posn
; determines the midpoint between a and b
(define (mid-point a b)
  a)
```

3つの関数を設計せよ。

領域知識 (1) too-small? 関数については、2点間の距離を測り、選んだ閾値、たとえば10より下かどうかを検査すれば十分である。(x0,y0) と (x1,y1) の間の距離は

> [image: pict_298.png]

すなわち、(x0 - x1,y0 - y1) の原点からの距離である。

点 (x0,y0) と (x1,y1) の中点は、それぞれの x 座標と y 座標の中点を座標として持つ：

> [image: pict_299.png]

補助関数がすべて揃ったので、再帰呼び出しが作る3つの画像を組み合わせる問題に戻るときである。明白な推測は overlay または underlay 関数を使うことだが、DrRacket の対話領域での評価は、これらの関数が下にある三角形を隠すことを示す。

具体的には、3つの再帰呼び出しが、適切な位置に1つの三角形が加えられた次の空のシーンを生成すると想像せよ：

```racket
> scene1
[image:pict_300.png]
> scene2
[image:pict_301.png]
> scene3
[image:pict_302.png]
```

組み合わせは、この図のように見えるはずである：

> [image: pict_303.png]

しかし、これらの形を overlay または underlay で組み合わせても、望ましい形は得られない：

```racket
> (overlay scene1 scene2 scene3)
[image:pict_304.png]
> (underlay scene1 scene2 scene3)
[image:pict_305.png]
```

実際、ISL+ の image ティーチパックは、これらのシーンを適切な仕方で組み合わせる関数をサポートしていない。

これらの対話をもう一度見よう。scene1 が与えられたシーンに上の三角形を加えた結果であり、scene2 が左下に三角形を加えた結果であるなら、2番目の再帰呼び出しは第1の呼び出しの結果に三角形を加えるべきかもしれない。そうすると次が得られる：

> [image: pict_306.png]

そしてこのシーンを3番目の再帰呼び出しに渡せば、まさに望むものが得られる：

> [image: pict_307.png]

> **図192: Accumulators as results of generative recursion, the function**

```racket
; Image Posn Posn Posn -> Image
; generative adds the triangle (a, b, c) to scene0,
; subdivides it into three triangles by taking the
; midpoints of its sides; stop if (a, b, c) is too small
; accumulator the function accumulates the triangles of scene0
(define (add-sierpinski scene0 a b c)
  (cond
    [(too-small? a b c) scene0]
    [else
     (local
       ((define scene1 (add-triangle scene0 a b c))
        (define mid-a-b (mid-point a b))
        (define mid-b-c (mid-point b c))
        (define mid-c-a (mid-point c a))
        (define scene2
          (add-sierpinski scene1 a mid-a-b mid-c-a))
        (define scene3
          (add-sierpinski scene2 b mid-b-c mid-a-b)))
       ; —IN—
       (add-sierpinski scene3 c mid-c-a mid-b-c))]))
```


図192は、この洞察に基づく再定式化を示す。3つの強調箇所が鍵となる設計の考えを特定する。すべて、三角形が十分大きく、与えられたシーンに加えられる場合に関わる。辺が分割されたら、第1の外側の三角形は、与えられた三角形を加えた結果である scene1 を使って再帰的に処理される。同様に、この第1の再帰の結果、scene2 と名付けられたものが、第2の再帰——第2の三角形の処理——に使われる。最後に、scene3 が第3の再帰呼び出しに流れ込む。要するに、新規性は、蓄積子が同時に引数であり、知識を集める道具であり、関数の結果でもあることである。

add-sierpinski を探るには、正三角形と、十分に大きな余白を残す画像から始めるのが最善である。これら2つの基準を満たす定義は次のとおり：

```racket
(define MT (empty-scene 400 400))
(define A (make-posn 200  50))
(define B (make-posn  27 350))
(define C (make-posn 373 350))

(add-sierpinski MT A B C)
```

このコード断片がどのようなシェルピンスキー・フラクタルを届けるかを確認せよ。練習問題525の定義を実験し、最初のものより疎らな、および密なシェルピンスキーの三角形を作れ。

練習問題 526. 正三角形のシェルピンスキー三角形の端点を計算するには、円を描き、円上で120度ずつ離れた3点を選べ。たとえば120、240、360。

関数 circle-pt を設計せよ：

```racket
(define CENTER (make-posn 200 200))
(define RADIUS 200); the radius in pixels

; Number -> Posn
; determines the point on the circle with CENTER
; and RADIUS whose angle is

; examples
; what are the x and y coordinates of the desired
; point, when given: 120/360, 240/360, 360/360

(define (circle-pt factor)
  (make-posn 0 0))
```

領域知識 この設計問題は数学の知識を求める。問題の1つの見方は、複素数を極座標表現から Posn 表現へ変換することである。ISL+ で make-polar、real-part、および imag-part について読め。もう1つの方法は、三角関数 sin と cos を使って座標を求めることである。この道を選ぶなら、これらの三角関数が正弦と余弦を度ではなくラジアンで計算することを思い出せ。また、画面上の位置は上方向ではなく下方向に増えることも心に留めよ。

**練習問題 527. 次の2つの画像を見よ：**

> [image: pict_308.png] [image: pict_309.png]

これらは、図156がシェルピンスキーの三角形をどう描くかを示すのと同じ仕方で、フラクタルなサバンナの木をどう生成するかを示す。左の画像はフラクタルなサバンナの木がどう見えるかを示し、右の画像は生成的な構成ステップを説明する。

関数 add-savannah を設計せよ。この関数は画像と4つの数を消費する：(1) 線の基点の x 座標、(2) 線の基点の y 座標、(3) 線の長さ、(4) 線の角度。与えられた画像にフラクタルなサバンナの木を加える。

線が短すぎないかぎり、関数は指定された線を画像に加える。次に線を3つの線分に分割する。2つの中間点を、2本の線の新しい始点として再帰的に使う。2本の枝の長さと角度は固定の仕方で変わるが、互いに独立である。これらの変化を定義する定数を使い、木が十分気に入るまでそれらで作業せよ。

ヒント 各左の枝を少なくとも3分の1短くし、少なくとも0.15度左へ回転させて実験せよ。各右の枝については、少なくとも20%短くし、反対方向に0.2度回転させよ。

**練習問題 528. グラフィックスのプログラマは、しばしば2点を滑らかな曲線でつなぐ必要がある。ここで「滑らか」はある視点に相対的である。
次に2つのスケッチがある：**

> **注:** Géraldine Morin がこの練習問題を提案した。

> [image: pict_310.png] [image: pict_311.png]

左は点 A と C をつなぐ滑らかな曲線を示し、右は視点 B と観測者の角度を与える。

そのような曲線を描く1つの方法はベジェによるものである。これは生成的再帰の好例であり、次の列がアルゴリズムの背後にある eureka!（ひらめき）を説明する：

> [image: pict_312.png] [image: pict_313.png] [image: pict_314.png]

左の画像を考えよ。3つの与えられた点が三角形を定め、A から C への接続がアルゴリズムの焦点であることを思い出させる。目標は、A から C への線を B へ向けて引っ張り、滑らかな曲線に変えることである。

次に中央の画像に目を向けよ。生成的ステップの本質的な考えを説明する。アルゴリズムは2本の観測線 A-B と B-C 上の中点、およびそれらの中点 A-B-C を求める。

最後に、最も右の画像は、これら3つの新しい点がどう2つの異なる再帰呼び出しを生成するかを示す。1つは左側の新しい三角形を扱い、もう1つは右側の三角形を扱う。より正確には、A-B と B-C が新しい観測点となり、A から A-B-C へ、および C から A-B-C への線が2つの再帰呼び出しの焦点になる。

三角形が十分小さいとき、自明に解ける場合になる。アルゴリズムは単に三角形を描き、それは与えられた画像上の点として現れる。このアルゴリズムを実装するとき、「十分小さい」という概念を実験し、曲線が滑らかに見えるようにする必要がある。

## 34 まとめ（Summary）

本書のこの最後の部は、蓄積子を用いた設計についてである。蓄積子は、データ構造の走査のあいだに知識を集める仕組みである。蓄積子を加えると、性能上の欠陥を直し、停止の問題を除くことができる。この部から持ち帰るべき設計上の教訓は、2つ半である：

1. 第1のステップは、蓄積子を導入する必要を認識することである。走査は、引数の1片から次の片へ進むとき、引数の断片を「忘れる」。そのような知識が関数の設計を単純にし得ると分かったら、蓄積子の導入を検討せよ。その第1ステップは、蓄積子テンプレートへ切り替えることである。
2. 鍵となるステップは、蓄積子文を定式化することである。後者は、蓄積子がどのような知識をどのような種類のデータとして集めるかを表さなければならない。ほとんどの場合、蓄積子文は元の引数と現在の引数との差を記述する。
3. 第3のステップは小さなもので、蓄積子文から (a) 初期の蓄積子の値は何か、(b) 走査の各ステップでそれをどう維持するか、(c) その知識をどう活用するかを導くことである。

知識を累積するという考えはどこにでもあり、多くの異なる形と姿で現れる。ISL+ のようないわゆる関数型言語では広く使われる。命令型言語を使うプログラマは、蓄積子に別の仕方で出会う。主に、値を返せない素朴なループ構成子の中の代入文を通じてである。そうした命令型の蓄積子プログラムの設計は、ここでの蓄積子関数の設計と同じように進むが、細部は体系的なプログラム設計についてのこの最初の本の範囲を超える。

