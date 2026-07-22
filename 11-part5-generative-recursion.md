<!-- Extracted from original_html/part_five.html -->
<!-- Canonical English source for Japanese translation -->

# V 生成的再帰（Generative Recursion）

### 目次（Contents）

- 25 非標準の再帰（Non-standard Recursion）
- 25.1 構造なしの再帰（Recursion without Structure）
- 25.2 構造を無視する再帰（Recursion that Ignores Structure）
- 26 アルゴリズムの設計（Designing Algorithms）
- 26.1 設計レシピの適応（Adapting the Design Recipe）
- 26.2 停止（Termination）
- 26.3 構造的再帰と生成的再帰（Structural versus Generative Recursion）
- 26.4 選択を行う（Making Choices）
- 27 テーマの変奏（Variations on the Theme）
- 27.1 フラクタル、最初の味（Fractals, a First Taste）
- 27.2 二分探索（Binary Search）
- 27.3 構文解析の瞥見（A Glimpse at Parsing）
- 28 数学の例（Mathematical Examples）
- 28.1 ニュートン法（Newton’s Method）
- 28.2 数値積分（Numeric Integration）
- 28.3 プロジェクト：ガウス消去法（Project: Gaussian Elimination）
- 29 バックトラックするアルゴリズム（Algorithms that Backtrack）
- 29.1 グラフの走査（Traversing Graphs）
- 29.2 プロジェクト：バックトラック（Project: Backtracking）
- 30 まとめ（Summary）

最初の4部の設計レシピに従えば、ドメインの知識をコードに移すか、データ定義の構造を利用してコードを組み立てるかのどちらかになる。
後者の関数は、典型的には引数をその直近の構造的構成要素に分解し、それらの構成要素を処理する。これらの直近の構成要素の1つが入力と同じデータのクラスに属するなら、その関数は構造的再帰である。構造的に設計された関数は世界のコードの圧倒的多数を占めるが、構造的な設計アプローチでは解けない問題もある。

> **注:** 一部の関数は、そのような関数を組み合わせるだけである。それらも「構造的」なグループに含める。

そうした複雑な問題を解くために、プログラマは生成的再帰を使う。これは構造的再帰より厳密に強力な再帰の一形態である。生成的再帰の研究は数学と同じくらい古く、しばしばアルゴリズムの研究と呼ばれる。アルゴリズムの入力は問題を表す。アルゴリズムは問題をいくつかの問題の集合に並べ替え、それらを解き、その解を1つの全体解に組み合わせる傾向がある。新たに生成された問題のいくつかが与えられた問題と同じ種類であることがよくあり、その場合アルゴリズムを再利用してそれらを解ける。こうした場合、アルゴリズムは再帰的だが、その再帰は入力データの直近の部分ではなく、新たに生成されたデータを用いる。

生成的再帰のこの記述からだけでも、生成的再帰関数の設計は、構造的再帰関数の設計より場当たり的な活動であることが分かる。それでも、一般的な設計レシピの多くの要素はアルゴリズムの設計にも当てはまり、本書のこの部は、設計レシピがどのように、またどれほど役立つかを示す。アルゴリズム設計の鍵は「生成」のステップであり、それはしばしば問題を分割することを意味する。問題を分割する新しい方法を見つけるには洞察が必要である。
ときにはほとんど洞察は要らない。たとえば、文字の並びをどう区切るかについての常識だけで足りることもある。またあるときには、数に関する深い数学的定理に頼ることもある。実際には、プログラマは単純なアルゴリズムを自分で設計し、複雑なものはドメインの専門家に頼る。どちらについても、プログラマは背後にある考え方を十分に理解し、アルゴリズムをコードに落とし、将来の読者とプログラムが意思疎通できるようにしなければならない。この考え方に親しむ最善の方法は、幅広い例を研究し、現実世界に現れうる生成的再帰の種類への感覚を養うことである。

> **注:** ギリシア語では「eureka!」である。

## 25 非標準の再帰（Non-standard Recursion）

ここまでに、構造的再帰を用いる関数を数多く設計してきた。関数を設計するとき、主要な入力のデータ定義を見る必要があると分かっている。その入力が自己参照するデータ定義で記述されていれば、データ定義が自分自身を参照するところと基本的に同じところで自分自身を参照する関数に行き着く。

本章は、再帰を異なる仕方で使う2つのサンプルプログラムを提示する。これらは、「eureka」（ひらめき）——明らかな考えから洗練された洞察まで——を必要とする問題を例示する。

### 25.1 構造なしの再帰（Recursion without Structure）

DrRacket チームに参加したとしよう。チームはプログラマどうしの共同作業を支える共有サービスに取り組んでいる。具体的には、次の改訂版 DrRacket は、ISL プログラマが複数のコンピュータにまたがって DrRacket の定義領域の内容を共有できるようにする。あるプログラマがバッファを変更するたびに、改訂版 DrRacket は定義領域の内容を、共有セッションに参加している DrRacket のインスタンスへブロードキャストする。

> サンプル問題 あなたの課題は、ブロードキャストのために定義領域の内容を準備する関数 bundle を設計することである。DrRacket は内容を 1String のリストとして渡す。関数の仕事は、個々の「文字」のまとまりをチャンクに束ね、与えられた長さ——チャンクサイズと呼ばれる——の文字列のリスト——チャンクと呼ばれる——を生成することである。

見ての通り、問題は基本的にシグネチャを言い表しており、問題固有のデータ定義は不要である。

```racket
; [List-of 1String] N -> [List-of String]
; bundles chunks of s into strings of length n
(define (bundle s n)
  '())
```

目的文は、問題文の文の断片を言い直し、ダミー関数ヘッダの引数を使う。

第3ステップは関数の例を求める。ここに 1String のリストがある。

```racket
(list "a" "b" "c" "d" "e" "f" "g" "h")
```

bundle にこのリストを対に束ねるよう指示する——すなわち n が 2——なら、次のリストが期待される結果である。

```racket
(list "ab" "cd" "ef" "gh")
```

今度は n が 3 だと、余った「文字」が1つ残る。問題文はどの文字が余るか述べていないので、少なくとも2つの妥当なシナリオが想像できる。

- 関数は (list"abc""def""g") を生成する。すなわち、最後の文字を余りと見なす。
- あるいは (list"a""bcd""efg") を生成し、先頭の文字を単独の文字列に詰める。

やめ！ 少なくとももう1つの選択を考えよ。

話を単純にするため、最初の選択を望ましい結果として選び、対応するテストを書いてそう述べる。

```racket
(check-expect (bundle (explode "abcdefg") 3)
              (list "abc" "def" "g"))
```

explode の使用に注意。テストを読みやすくする。

例とテストは、データ定義の境界で何が起きるかも記述しなければならない。この文脈では、境界は明らかに、bundle に与えられたチャンクサイズに対して短すぎるリストが与えられることを意味する。

```racket
(check-expect (bundle '("a" "b") 3) (list "ab"))
```

また、bundle に '() が与えられたとき何が起きるかも考えなければならない。単純のため、望ましい結果として '() を選ぶ。

```racket
(check-expect (bundle '() 3) '())
```

自然な代替は '("") を求めることである。他にも見えるか。

> **図146: Useless templates for breaking up strings into chunks**

```racket
; N as compound, s considered atomic
; (Processing Two Lists Simultaneously: Case 1)
(define (bundle s n)
  (cond
    [(zero? n) (...)]
    [else (... s ... n ... (bundle s (sub1 n)))]))

; [List-of 1String] as compound, n atomic
; (Processing Two Lists Simultaneously: Case 1)
(define (bundle s n)
  (cond
    [(empty? s) (...)]
    [else (... s ... n ... (bundle (rest s) n))]))

; [List-of 1String] and N are on equal footing
; (Processing Two Lists Simultaneously: Case 2)
(define (bundle s n)
  (cond
    [(and (empty? s) (zero? n)) (...)]
    [else (... s ... n ... (bundle (rest s) (sub1 n)))]))

; consider all possibilities
; (Processing Two Lists Simultaneously: Case 3)
(define (bundle s n)
  (cond
    [(and (empty? s) (zero? n)) (...)]
    [(and (cons? s) (zero? n)) (...)]
    [(and (empty? s) (positive? n)) (...)]
    [else (... (bundle s (sub1 n)) ...
           ... (bundle (rest s) n) ...)]))
```


テンプレートのステップは、構造的アプローチではうまくいかないことを明らかにする。図146は4つの可能なテンプレートを示す。bundle への両方の引数が複雑なので、最初の2つは引数の一方を原子的と見なす。関数は各引数を分解しなければならないので、それが明らかに当てはまらない。第3のテンプレートは、2つの引数が足並みをそろえて処理されるという仮定に基づく。それは近い——ただし、bundle は明らかにチャンクサイズを定期的に元の値へリセットしなければならない。最後のテンプレートは、2つの引数が独立に処理されると言う。すなわち各段階で進み方が4通りある。この最終設計は引数を過度に切り離す。リストと数え上げの数は一緒に処理されなければならないからである。要するに、構造的テンプレートはこの設計問題には無用に見えると認めざるを得ない。

> **図147: Generative recursion**

```racket
; [List-of 1String] N -> [List-of String]
; bundles chunks of s into strings of length n
; idea take n items and drop n at a time
(define (bundle s n)
  (cond
    [(empty? s) '()]
    [else
     (cons (implode (take s n)) (bundle (drop s n) n))]))

; [List-of X] N -> [List-of X]
; keeps the first n items from l if possible or everything
(define (take l n)
  (cond
    [(zero? n) '()]
    [(empty? l) '()]
    [else (cons (first l) (take (rest l) (sub1 n)))]))

; [List-of X] N -> [List-of X]
; removes the first n items from l if possible or everything
(define (drop l n)
  (cond
    [(zero? n) l]
    [(empty? l) l]
    [else (drop (rest l) (sub1 n))]))
```


図147は bundle の完全な定義を示す。定義は練習問題395で求められた drop と take 関数を使う。これらの関数は標準ライブラリでも利用できる。完全のため、図にはそれらの定義も付く。drop はリストの先頭から最大 n 個の項目を取り除き、take は最大その個数の項目を返す。これらの関数を使えば、bundle を定義するのはかなり直截である。

1. 与えられたリストが '() なら、結果は決定した通り '() である。
2. そうでなければ、bundle は take を使い、s から先頭の n 個の 1String を取り、implode して普通の String にする。
3. 次に n 個分短くしたリストで再帰する。これは drop で達成される。
4. 最後に、cons が 2 の文字列と 3 の文字列のリストを組み合わせ、完全なリストに対する結果を作る。

箇条3が、bundle と本書の最初の4部のどの関数との間の鍵となる違いを際立たせる。List-of の定義は項目をリストに cons して別のリストを作るので、最初の4部のすべての関数は空でないリストを分解するのに first と rest を使う。対照的に、bundle は drop を使い、一度に1個ではなく n 個の項目を取り除く。

bundle の定義は普通でないが、背後の考え方は直観的で、これまで見てきた関数とそれほど違わない。実際、チャンクサイズ n が 1 なら、bundle は構造的再帰の定義に特殊化される。また、drop は与えられたリストの一部である部分を生成することが保証されており、任意に並べ替えた版ではない。そしてこの考えこそが、次節が提示するものである。

練習問題 421. (bundle'("a""b""c")0) は bundle 関数の適切な使い方か。何を生成するか。なぜか。

練習問題 422. 関数 list->chunks を定義せよ。任意のデータのリスト l と自然数 n を消費する。関数の結果は、大きさ n のリストチャンクのリストである。各チャンクは l 中の項目の部分列を表す。

list->chunks を使い、関数合成経由で bundle を定義せよ。

練習問題 423. partition を定義せよ。String s と自然数 n を消費する。関数は大きさ n の文字列チャンクのリストを生成する。

空でない文字列 s と正の自然数 n について、

```racket
(equal? (partition s n) (bundle (explode s) n))
```

は #true である。しかしこの等しさを partition の定義として使ってはいけない。代わりに substring を使え。

ヒント partition は空文字列に対して自然な結果を生成させよ。n が 0 の場合については、練習問題421を見よ。

注 partition 関数は、協調的な DrRacket 環境が必要とするものに、bundle よりやや近い。

### 25.2 構造を無視する再帰（Recursion that Ignores Structure）

Design by Composition の sort> 関数が、数のリストを消費し、それをある順序——典型的には昇順または降順——に並べ替えることを思い出せ。それは、リストの先頭の数を、残りの整列済みリストの適切な位置に挿入することで進む。言い換えれば、自然な再帰の結果を再処理する構造的再帰関数である。

Hoare の quick-sort アルゴリズムは、リストの整列をまったく異なる仕方で行い、生成的再帰の古典的な例となっている。背後の生成ステップは、時を超えて尊重されてきた分割統治の戦略を使う。すなわち、問題の非自明なインスタンスを2つのより小さな関連する問題に分け、それらの小さな問題を解き、その解を元の問題の解に組み合わせる。quick-sort アルゴリズムの場合、中間的な目標は数のリストを2つのリストに分けることである。

- 先頭より厳密に小さい数をすべて含むもの
- および厳密に大きい項目をすべて含むもう1つ

そして2つのより小さなリストを quick-sort アルゴリズムで整列する。2つのリストが整列したら、結果を先頭の項目を真ん中に置いて合成する。その特別な役割ゆえに、リストの先頭の項目はピボット項目と呼ばれる。

> **図148: A graphical illustration of the quick-sort algorithm**

> 原本は次の画像を含む（画像プレースホルダは図版パイプラインで埋め込み可）:
>
> [image: pict_180.png]


quick-sort アルゴリズムがどう働くかの理解を深めるため、例を通して歩いてみよう。(list118147) を quick-sort する。図148はこの過程を図で示す。図は上半分の分割フェーズと、下半分の征服フェーズからなる。

分割フェーズは箱と実線の矢印で表される。各箱入りリストから3本の矢印が出て、3つの部分を持つ箱へ向かう。真ん中に丸で囲んだピボット要素、その左にピボットより小さい数の箱入りリスト、右にピボットより大きい数の箱入りリストである。これらの各ステップは少なくとも1つの数をピボットとして切り出す。すなわち隣り合う2つのリストは与えられたリストより短い。したがって全体の過程も停止する。

最初のステップを考えよ。入力は (list118147) である。ピボット項目は 11 である。リストを 11 より大きい項目と小さい項目に分割すると (list87) と (list14) が得られる。分割フェーズの残りのステップも同様に働く。分割はすべての数がピボット要素として切り出されたときに終わる。この時点で、ピボットを左から右へ読むだけで最終結果を読み取れる。

征服フェーズは破線の矢印と箱入りリストで表される。各結果箱に3本の矢印が入る。真ん中はピボットから、左はより小さい数を整列した結果の箱から、右はより大きい数を整列した結果の箱からである。各ステップは結果リストに少なくとも1つの数、すなわちピボットを加える。つまりリストは図の下に向かって成長する。一番下の箱は、一番上の与えられたリストの整列済み変種である。

最も左上の征服ステップを見よ。ピボット 7 を2つの空リストと組み合わせ、'(7) を得る。その下の1つは 8 を切り出した分割ステップに対応し、したがって '(78) を生じる。征服フェーズの各レベルは、分割フェーズの対応するレベルを鏡のように映す。結局のところ、全体の過程は再帰的である。

練習問題 424. 図148のような quick-sort 図を、(list119218121441) について描け。

quick-sort の考え方をよく理解したので、ISL+ に翻訳できる。明らかに、quick-sort< は2つの場合を区別する。入力が '() なら、すでに整列しているので '() を生成する。そうでなければ生成的再帰を行う。この場合分けは次の cond 式を示唆する。

```racket
; [List-of Number] -> [List-of Number]
; produces a sorted version of alon
(define (quick-sort< alon)
  (cond
    [(empty? alon) '()]
    [else...]))
```

第1の場合の答えは与えられている。第2の場合、quick-sort< の入力が空でないリストのとき、アルゴリズムは先頭の項目を使い、リストの残りを2つの部分リストに分割する。ピボット項目より小さいすべての項目のリストと、ピボットより大きいもののリストである。

リストの残りの大きさが未知なので、リストの分割の仕事は2つの補助関数 smallers と largers に任せる。それらはリストを処理し、ピボットよりそれぞれ小さい、大きい項目をフィルタする。したがって各補助関数は2つの引数、すなわち数のリストと数を受け取る。これら2つの関数の設計は構造的再帰の練習である。自分で試すか、図149に示す定義を読め。

> **図149: The quick-sort algorithm**

```racket
; [List-of Number] -> [List-of Number]
; produces a sorted version of alon
; assume the numbers are all distinct
(define (quick-sort< alon)
  (cond
    [(empty? alon) '()]
    [else (local ((define pivot (first alon)))
            (append (quick-sort< (smallers alon pivot))
                    (list pivot)
                    (quick-sort< (largers alon pivot))))]))

; [List-of Number] Number -> [List-of Number]
(define (largers alon n)
  (cond
    [(empty? alon) '()]
    [else (if (> (first alon) n)
              (cons (first alon) (largers (rest alon) n))
              (largers (rest alon) n))]))

; [List-of Number] Number -> [List-of Number]
(define (smallers alon n)
  (cond
    [(empty? alon) '()]
    [else (if (< (first alon) n)
              (cons (first alon) (smallers (rest alon) n))
              (smallers (rest alon) n))]))
```


これらの各リストは quick-sort< を使って別々に整列される。これは再帰の使用、具体的には次の2つの式を意味する。

1. (quick-sort<(smallersalonpivot))、これはピボットより小さい項目のリストを整列する。
2. (quick-sort<(largersalonpivot))、これはピボットより大きい項目のリストを整列する。

quick-sort< が2つのリストの整列済み版を得たなら、2つのリストとピボットを正しい順序で組み合わせなければならない。まず pivot より小さいすべての項目、次に pivot、最後に大きいものすべてである。最初と最後のリストはすでに整列しているので、quick-sort< は単に append を使える。

```racket
(append (quick-sort< (smallers alon pivot))
        (list (first alon))
        (quick-sort< (largers alon pivot)))
```

図149に完全なプログラムがある。先へ進む前に読め。

実際の関数定義ができたので、上の例を手で評価できる。

```racket
(quick-sort< (list 11 8 14 7))
==
(append (quick-sort< (list 8 7))
        (list 11)
        (quick-sort< (list 14)))
==
(append (append (quick-sort< (list 7))
                 (list 8)
                (quick-sort< '()))
        (list 11)
        (quick-sort< (list 14)))
==
(append (append (append (quick-sort< '())
                        (list 7)
                        (quick-sort< '()))
                (list 8)
                (quick-sort< '()))
        (list 11)
        (quick-sort< (list 14)))
==
(append (append (append '()
                         (list 7)
                        '())
                (list 8)
                '())
        (list 11)
        (quick-sort< (list 14)))
==
(append (append (list 7)
                (list 8)
                '())
        (list 11)
        (quick-sort< (list 14)))
...
```

この計算は整列過程の本質的なステップ、すなわち分割ステップ、再帰的整列ステップ、3つの部分の連結を示す。この計算から、quick-sort< が図148に図示された過程をどう実装するかが容易に分かる。

図148とこの計算はどちらも、quick-sort< が与えられたリストの構造を完全に無視することを示す。最初の再帰は元のリストから離れた2つの数に働き、2番目の再帰はリストの第3項目に働く。これらの再帰はランダムではないが、データ定義の構造に頼っているわけでもまったくない。

quick-sort< の構成を、Design by Composition の sort> 関数の構成と対比せよ。後者の設計は構造的設計レシピに従い、リストを項目ごとに処理するプログラムを生じる。リストを分割することで、quick-sort< はリストの整列を加速できる。ただし、素直な first と rest を使わないという代償を払う。

練習問題 425. 図149の smallers と largers の目的文を言葉で述べよ。

練習問題 426. 上の手評価を完成せよ。評価をよく見ると、quick-sort< に追加の自明な場合が示唆される。quick-sort< が1項目のリストを消費するたびに、それをそのまま返す。結局のところ、1項目のリストの整列済み版はそのリスト自身である。

この観察を活かすよう quick-sort< を修正せよ。例を再び評価せよ。改訂されたアルゴリズムは何ステップ節約するか。

練習問題 427. quick-sort< は多くの場合に問題の大きさを素早く減らすが、小さな問題には不適切に遅い。そのため人々は quick-sort< を使って問題の大きさを減らし、リストが十分小さいときに別の整列関数に切り替える。

入力の長さがある閾値を下回ったら sort<（Auxiliary Functions that Recur の sort> を適切に適応させた変種）を使う quick-sort< の版を開発せよ。

練習問題 428. quick-sort< への入力に同じ数が何度も含まれると、アルゴリズムは入力より厳密に短いリストを返す。なぜか。出力が入力と同じ長さになるよう問題を修正せよ。

練習問題 429. filter を使って smallers と largers を定義せよ。

練習問題 430. 比較関数を1つだけ、たとえば < だけ使う quick-sort< の変種を開発せよ。その分割ステップは、与えられたリスト alon を、ピボットより小さい alon の項目を含むリストと、小さくないものを含むもう1つに分ける。

local を使い、プログラムを単一の関数としてまとめよ。この関数を抽象化し、リストと比較関数を消費するようにせよ。

## 26 アルゴリズムの設計（Designing Algorithms）

この部の概観ですでに説明したように、生成的再帰関数の設計は構造的設計より場当たり的である。第1章が示すように、2つの生成的再帰は関数の処理の仕方で大きく異なりうる。bundle と quick-sort< はどちらもリストを処理するが、前者は少なくとも与えられたリストの順序を尊重するのに対し、後者は与えられたリストを勝手に並べ替える。問題は、これほど大きく異なる関数の作成に、単一の設計レシピが役立つかどうかである。

第1節は、設計レシピの過程の次元を生成的再帰へどう適応させるかを示す。第2節は別の新しい現象に焦点を当てる。アルゴリズムは一部の入力に対して答えを生成しないことがある。したがってプログラマはプログラムを分析し、設計情報に停止に関するコメントを補わなければならない。残りの節は構造的再帰と生成的再帰を対比する。

### 26.1 設計レシピの適応（Adapting the Design Recipe）

前章の例に照らして、構造的設計レシピの6つの一般的なステップを検討しよう。

- これまで通り、問題の情報を選んだプログラミング言語のデータの形で表現しなければならない。問題のデータ表現の選択は、計算過程についての考え方に影響するので、ある程度の先読みが必要である。あるいは、後戻りして異なるデータ表現を探る用意をしておく。いずれにせよ、問題の情報を分析し、データの集まりを定義しなければならない。
- またシグネチャ、関数ヘッダ、目的文も必要である。生成ステップはデータ定義の構造と結びつかないので、目的文は関数が何を計算するかを超えて、関数がどう結果を計算するかも説明しなければならない。
- 「どう」を関数の例で説明すると有用である。前章で bundle と quick-sort< を説明した仕方と同じである。すなわち、構造的な世界での関数の例は、どの入力に対してどの出力を生成するかを指定するだけなのに対し、生成的再帰の世界での例の目的は、計算過程の背後にある考え方を説明することである。bundle については、例は関数が一般に、また特定の境界の場合にどう振る舞うかを指定する。quick-sort< については、図148の例が、関数がピボット項目に関して与えられたリストをどう分割するかを示す。そのような作業例を目的文に加えることで、我々——設計者——は望ましい過程への理解を深め、このコードの将来の読者にその理解を伝える。
- 議論はアルゴリズムの一般的なテンプレートを示唆する。おおざっぱに言えば、アルゴリズムの設計は2種類の問題を区別する。自明に解けるものと、そうでないものである。与えられた問題が自明に解けるなら、アルゴリズムは対応する解を生成する。たとえば、空リストや1項目のリストを整列する問題は自明に解ける。多くの項目を持つリストは非自明な問題である。これらの非自明な問題について、アルゴリズムは一般に、与えられたものと同じ種類の新しい問題を生成し、再帰的に解き、解を全体の解に組み合わせる。このスケッチに基づけば、すべてのアルゴリズムはおおむね次の構成を持つ。
(define (generative-recursive-fun problem) (cond [(trivially-solvable? problem) (determine-solution problem)] [else (combine-solutions... problem... (generative-recursive-fun (generate-problem-1 problem))... (generative-recursive-fun (generate-problem-n problem)))]))元の問題は、新たに生成された問題の解を組み合わせるのに時折必要になる。そのため combine-solutions に渡される。
  > **注:** 本書のこの部では、「自明（trivial）」は技術用語である。
- このテンプレートは示唆的な青写真にすぎず、確定した形ではない。テンプレートの各片は、次の4つの問いについて考えるよう思い出させる。
自明に解ける問題とは何か。自明な問題はどう解かれるか。アルゴリズムは、元のものより解きやすい新しい問題をどう生成するか。生成する新しい問題は1つか、いくつかあるか。与えられた問題の解は（そのうちの）新しい問題の解と同じか。それとも、元の問題の解を作るために解を組み合わせる必要があるか。そして、もしそうなら、元の問題のデータから何かが必要か。アルゴリズムを関数として定義するには、これら4つの問いへの答えを、選んだデータ表現に関する関数と式として表現しなければならない。このステップでは、Designing with Self-Referential Data Definitions の表駆動の試みが再び役立つかもしれない。Recursion that Ignores Structure の quick-sort< の例を再考せよ。quick-sort< の中心的な考えは、与えられたリストを小さい項目のリストと大きい項目のリストに分け、それらを別々に整列することである。図150は、非自明な場合についていくつかの単純な数値例がどう働くかを示す。これらの例から、第4の問いへの答えは、より小さい数の整列済みリスト、ピボット数、より大きい数の整列済みリストを append することだと推測するのは直截であり、コードへ容易に翻訳できる。
- 関数が完成したら、テストする時である。これまで通り、テストの目標はバグを発見し取り除くことである。

> **注:** 本書のこの部では、「自明（trivial）」は技術用語である。

> **図150: The table-based guessing approach for combining solutions**

```
alon
pivot
sorted, smaller
sorted, larger
expected
'
(
2
3
1
4
)
2
'
(
1
)
'
(
3
4
)
'
(
1
2
3
4
)
'
(
2
0
1
4
)
2
'
(
0
1
)
'
(
4
)
'
(
0
1
2
4
)
'
(
3
0
1
4
)
3
'
(
0
1
)
'
(
4
)
'
(
0
1
3
4
)
```


練習問題 431. bundle 問題について4つの鍵となる問いを答えよ。quick-sort< 問題については最初の3つの問いを答えよ。generate-problem のインスタンスはいくつ必要か。

練習問題 432. 練習問題219は関数 food-create を導入する。これは Posn を消費し、与えられたものと異なることが保証されたランダムに選ばれた Posn を生成する。まず2つの関数を local を使って単一の定義として再定式化し、次に food-create の設計を正当化せよ。

### 26.2 停止（Termination）

生成的再帰は計算にまったく新しい側面を加える。非停止である。bundle のような関数は、ある入力に対して値を生成しないことも、エラーを合図しないこともある。練習問題421は (bundle'("a""b""c")0) の結果は何かと尋ねる。結果を持たない理由の説明は次の通りである。

```racket
(bundle '("a" "b" "c") 0)
==
(cons (implode (take  '("a" "b" "c") 0))
      (bundle (drop  '("a" "b" "c") 0) 0))
==
(cons (implode '())
       (bundle (drop  '("a" "b" "c") 0) 0))
== (cons "" (bundle (drop  '("a" "b" "c") 0) 0))
== (cons "" (bundle '("a" "b" "c") 0))
```

この計算は、(bundle'("a""b""c")0) の評価が、まさに同じ式の結果を持つことを要求することを示す。ISL+ の文脈では、これは評価が止まらないことを意味する。コンピュータ科学者は、第2引数が 0 のとき bundle は停止しないと言う。また関数がループする、あるいは計算が無限ループに陥ると言う。

この洞察を、最初の4部で提示された設計と対比せよ。レシピに従って設計されたすべての関数は、すべての入力に対して答えを生成するか、エラー信号を上げる。結局のところ、レシピは各自然な再帰が入力そのものではなく、入力の直近の一片を消費すると命じる。データは階層的に構築されるので、入力は各段階で縮む。最終的に関数は原子的なデータ片に適用され、再帰は止まる。

この思い出させはまた、生成的再帰関数が発散しうる理由も説明する。生成的再帰の設計レシピによれば、アルゴリズムは制限なしに新しい問題を生成しうる。設計レシピが、新しい問題が与えられたものより「小さい」という保証を要求するなら、停止するだろう。しかし、そのような制限を課すと、bundle のような関数の設計を不必要に複雑にする。

> **注:** 計算理論は実際、これらの制限をいつか引き上げなければならないことを示す。

したがって本書では、設計レシピの最初の6ステップをほとんどそのまま保ち、第7のステップである停止の議論でそれらを補う。図151は生成的再帰の設計レシピの第1部を、図152は第2部を提示する。それらは設計レシピを従来の表形式で示す。変更のないステップは活動の列にダッシュが付く。他のステップには、生成的再帰の設計レシピが構造的再帰のものとどう異なるかについてのコメントが付く。図152の最後の行はまったく新しい。

停止の議論は2つの形のどちらかで来る。第1は、各再帰呼び出しが、与えられたものより小さい問題に働く理由を論じる。しばしばこの議論は直截である。まれに、そのような議論のために数学者と組んで定理を証明する必要がある。第2の種類は、関数が停止しないことがあることを例で示す。理想的には、関数がループしうるデータのクラスも記述すべきである。まれに、コンピュータ科学がまだ十分に知らないために、どちらの議論もできないこともある。

> **注:** このクラスの述語は定義できない。さもなければ関数を修正し、常に停止することを保証できる。

> **図151: Designing algorithms (part 1)**

```
steps
outcome
activity
problem analysis
data representation and
definition
—
header
a purpose statement concerning the “how” of the function
supplement the explanation of
what
the function computes with
a one-liner on
how
it computes the result
examples
examples and tests
work through the “how” with several examples
template
fixed template
—
```


> **図152: Designing algorithms (part 2)**

```
steps
outcome
activity
definition
full-fledged function definition
formulate conditions for trivially solvable problems;
formulate answers for these trivial cases;
determine how to generate new problems for nontrivial problems,
possibly using auxiliary functions;
determine how to combine the solutions of the generated problems
into a solution for the given problem
tests
discover mistakes
—
termination
(1) a size argument for each recursive call
or
(2) examples of exceptions to termination
investigate whether the problem data for each recursive data is
smaller than the given data; find examples that cause the function to loop
```


2種類の停止の議論を例で示そう。bundle 関数については、チャンクサイズ 0 について読者に警告すれば足りる。

```racket
; [List-of 1String] N -> [List-of String]
; bundles sub-sequences of s into strings of length n
; termination (bundle s 0) loops unless s is '()
(define (bundle s n)...)
```

この場合、bundle がいつ停止するかを正確に記述する述語を定義することが可能である。quick-sort< については、鍵となる観察は、quick-sort< の各再帰的使用が alon より短いリストを受け取ることである。

```racket
; [List-of Number] -> [List-of Number]
; creates a sorted variant of alon
; termination both recursive calls to quick-sort<
; receive list that miss the pivot item
(define (quick-sort< alon)...)
```

一方の場合、リストはピボットより厳密に小さい数からなり、他方は厳密に大きい数のためのものである。

練習問題 433. すべての入力に対して停止することが保証された、検査付きの bundle の版を開発せよ。元の版がループする場合にはエラーを合図してよい。

**練習問題 434. 次の smallers の定義を考えよ。quick-sort< のための2つの「問題生成器」の1つである。**

```racket
; [List-of Number] Number -> [List-of Number]
(define (smallers l n)
  (cond
    [(empty? l) '()]
    [else (if (<= (first l) n)
              (cons (first l) (smallers (rest l) n))
              (smallers (rest l) n))]))
```

この版が Recursion that Ignores Structure の quick-sort< 定義と一緒に使われたとき、何がうまくいかなくなりうるか。

練習問題 435. 練習問題430または練習問題428に取り組んだとき、ループする解を作ったかもしれない。同様に、練習問題434は実際、quick-sort< の停止の議論がどれほど脆いかを明らかにする。いずれの場合も、議論は、smallers と largers が与えられたリストと同じ長さを最大限とするリストを生成するという考えと、どちらも与えられたピボットを結果に含まないという我々の理解に頼っている。

この説明に基づき、両方の関数が与えられたものより短いリストを受け取るように、quick-sort< の定義を修正せよ。

練習問題 436. 練習問題432の food-create についての停止の議論を定式化せよ。

### 26.3 構造的再帰と生成的再帰（Structural versus Generative Recursion）

アルゴリズムのテンプレートは非常に一般的なので、構造的再帰関数も含む。図153の左側を考えよ。このテンプレートは、1つの自明な節と1つの生成ステップを扱うよう特殊化されている。trivial? を empty? に、generate を rest に置き換えれば、リスト処理関数のテンプレートが得られる。図153の右側を見よ。

> **図153: From generative to structural recursion**
> 左右対比（崩れた ASCII 枠を二重 fence に復元。コードは公式 HTML の RktBlk より）。

**左**

```racket
(define (general P)
  (cond
    [(trivial? P) (solve P)]
    [else
     (combine-solutions
       P
       (general
         (generate P)))]))
```

**右**

```racket
(define (special P)
  (cond
    [(empty? P) (solve P)]
    [else
     (combine-solutions
       P
       (special (rest P)))]))
```


**練習問題 437. solve と combine-solutions を定義して、次のようにせよ。**

- special がその入力の長さを計算する、
- special が与えられた数のリスト上の各数を否定する、
- special が与えられた文字列のリストを大文字にする。

これらの練習問題から何を結論するか。

では、構造的再帰設計と生成的再帰の設計の間に本当の違いがあるのかと疑問に思うかもしれない。我々の答えは「場合による」である。もちろん、構造的再帰を使うすべての関数は生成的再帰の特別な場合にすぎないと言うこともできる。しかしこの「すべては等しい」という態度は、関数設計の過程を理解したいなら何の助けにもならない。それは、異なる形の知識を要求し、異なる帰結を持つ2種類の設計を混同する。一方は体系的なデータ分析に頼り、それ以上はあまり要らない。他方は問題を解く過程そのものへの深い、しばしば数学的な洞察を要求する。一方はプログラマを自然に停止する関数へ導く。他方は停止の議論を必要とする。これら2つのアプローチを混同することは助けにならない。

### 26.4 選択を行う（Making Choices）

数のリストを整列する関数 f と対話するとき、f が sort< なのか quick-sort< なのかを知ることは不可能である。2つの関数は観察可能に等価な仕方で振る舞う。これは、プログラミング言語が2つのどちらを提供すべきかという問いを提起する。より一般に、構造的再帰と生成的再帰の両方を使って関数を設計できるとき、どちらを選ぶかを見極めなければならない。

> **注:** 観察可能な等価性は、プログラミング言語の研究の中心概念である。

この選択の帰結を示すため、数学からの古典的な例を論じる。2つの正の自然数の最大公約数（gcd）を求める問題である。そのような数はすべて 1 を共通の約数として持つ。時には——たとえば 2 と 3——それが唯一の共通約数でもある。6 と 25 はどちらも複数の約数を持つ数である。

> **注:** John Stone が最大公約数を適切な例として提案した。

- 6 は 1、2、3、6 で割り切れる。
- 25 は 1、5、25 で割り切れる。

それでも、それらの最大公約数は 1 である。対照的に、18 と 24 は多くの共通約数を持ち、最大公約数は 6 である。

- 18 は 1、2、3、6、9、18 で割り切れる。
- 24 は 1、2、3、4、6、8、12、24 で割り切れる。

設計レシピの最初の3ステップを完了するのは直截である。

```racket
; N[>= 1] N[>= 1] -> N
; finds the greatest common divisor of n and m
(check-expect (gcd 6 25) 1)
(check-expect (gcd 18 24) 6)
(define (gcd n m) 42)
```

シグネチャは入力を 1 以上の自然数と指定する。

ここから構造的再帰と生成的再帰の両方の解を設計する。本書のこの部は生成的再帰についてなので、図154に構造的な解を示すだけにし、設計の考え方は練習問題に任せる。(=(remainderni)(remaindermi)0) が、n と m の両方が i で「割り切れる」という考えを符号化することだけ注意せよ。

> **図154: Finding the greatest common divisor via structural recursion**

```racket
(define (gcd-structural n m)
  (local (; N -> N
          ; determines the gcd of n and m less than i
          (define (greatest-divisor-<= i)
            (cond
              [(= i 1) 1]
              [else
               (if (= (remainder n i) (remainder m i) 0)
                   i
                   (greatest-divisor-<= (- i 1)))])))
    (greatest-divisor-<= (min n m))))
```


練習問題 438. 自分の言葉で：greatest-divisor-<= はどう働くか。設計レシピを使い、正しい言葉を見つけよ。局所的に定義された greatest-divisor-<= はなぜ (minnm) について再帰するか。

gcd-structural の設計はかなり直截だが、素朴でもある。それは単に n と m の小さい方と 1 の間のすべての数について、それが n と m の両方を割り切るかを検査し、そのような最初の数を返す。小さな n と m ではこれはうまく働く。しかし次の例を考えよ。

```racket
(gcd-structural 101135853 45014640)
```

結果は 177 である。そこに至るために、gcd-structural は 45014640、すなわち 45014640 - 177 個の剰余について「割り切れる」条件を検査する。それほど多くの剰余を——2回！——検査するのは大きな努力であり、それなりに速いコンピュータでもこの仕事を完了するのに時間がかかる。

**練習問題 439. gcd-structural を DrRacket にコピーし、**

```racket
(time (gcd-structural 101135853 45014640))
```

を対話領域で評価せよ。

数学者たちはこの構造的関数の非効率性をずっと前に認識していたので、約数を求める問題を深く研究した。本質的な洞察は次である。

> 2つの自然数、大きい方を L、小さい方を S とすると、最大公約数は S と、L を S で割った剰余との最大公約数に等しい。

この洞察を等式としてどう言い表せるかを示す。

```racket
(gcd L S) == (gcd S (remainder L S))
```

(remainderLS) は L と S の両方より小さいので、右辺の gcd の使用はまず S を消費する。

この洞察が我々の小さな例にどう当てはまるかを示す。

- 与えられた数は 18 と 24 である。
- 洞察によれば、それらは 18 と 6 と同じ gcd を持つ。
- そしてこれら2つは 6 と 0 と同じ最大公約数を持つ。

ここで 0 は予期しないので行き詰まったように見える。しかし 0 はすべての数で割り切れる。つまり答えを見つけた。6 である。

例を通して作業すると、基本的な洞察が検証されるだけでなく、洞察をアルゴリズムにどう変えるかも示唆される。

- 数の小さい方が 0 のとき、自明な場合に直面する。
- 自明な場合の解は2つの数の大きい方である。
- 新しい問題の生成には剰余演算が1回必要である。
- 上の等式は、新たに生成された問題への答えが、元の与えられた問題への答えでもあると教える。

要するに、設計レシピの4つの問いへの答えが自然に出る。

> **図155: Finding the greatest common divisor via generative recursion**

```racket
(define (gcd-generative n m)
  (local (; N[>= 1] N -> N
          ; generative recursion
          ; (gcd L S) == (gcd S (remainder L S))
          (define (clever-gcd L S)
            (cond
              [(= S 0) L]
              [else (clever-gcd S (remainder L S))])))
    (clever-gcd (max m n) (min m n))))
```


図155はアルゴリズムの定義を提示する。局所定義は関数の働き馬を導入する。clever-gcd である。その最初の cond 行は smaller を 0 と比較して自明な場合を発見し、対応する解を生成する。生成ステップは smaller を新しい第1引数、(remainderlargesmall) を clever-gcd への新しい第2引数として使う。

上の例で gcd-generative を使うと、

```racket
(gcd-generative 101135853 45014640)
```

応答がほぼ瞬時であることが分かる。手評価は、clever-gcd が解を生成する前に9回だけ再帰することを示す。

```racket
...
== (clever-gcd 101135853 45014640)
== (clever-gcd 45014640 11106573)
== (clever-gcd 11106573 588348)
== (clever-gcd 588348 516309)
== (clever-gcd 516309 72039)
== (clever-gcd 72039 12036)
== (clever-gcd 12036 11859)
== (clever-gcd 11859 177)
== (clever-gcd 177 0)
```

これはまた、剰余条件を9回だけ検査することを意味し、gcd-structural が費やす努力より明らかにずっと小さい。

**練習問題 440. gcd-generative を DrRacket の定義領域にコピーし、**

```racket
(time (gcd-generative 101135853 45014640))
```

を対話領域で評価せよ。

生成的再帰の設計が gcd 問題のはるかに速い解を発見したと考え、生成的再帰が常に正しい道だと結論するかもしれない。この判断は3つの理由で性急すぎる。第1に、うまく設計されたアルゴリズムでさえ、等価な構造的再帰関数より常に速いとは限らない。たとえば quick-sort< は大きなリストに対してのみ勝ち、小さなリストでは標準の sort< 関数の方が速い。さらに悪いことに、悪く設計されたアルゴリズムはプログラムの性能に大打撃を与えうる。第2に、構造的再帰のレシピを使って関数を設計する方が典型的には容易である。逆に、アルゴリズムの設計は新しい問題をどう生成するかの考えを要求し、そのステップはしばしば深い洞察を必要とする。最後に、関数を読むプログラマは、構造的再帰関数を、あまり文書がなくても容易に理解できる。一方、アルゴリズムの生成ステップは「eureka!」に基づいており、よい説明がなければ将来の読者——それには年を取った自分自身も含まれる——にとって理解しにくい。

経験は、プログラム中のほとんどの関数が構造的設計を用い、生成的再帰を活用するのは少数であることを示す。構造的再帰と生成的再帰のどちらのレシピも使える状況に出会ったら、最善のアプローチは構造的な版から始めることである。手元の仕事に対して結果が遅すぎることが分かったとき——そしてそのときに限って——生成的再帰の使用を探る時である。

**練習問題 441. 次を**

```racket
(quick-sort< (list 10 6 8 9 14 12 3 11 14 16 2))
```

手で評価せよ。quick-sort< への新しい再帰呼び出しを導入する行だけを示せ。quick-sort< の再帰的適用は何回必要か。append 関数の再帰的適用は何回か。長さ n のリストに対する一般規則を提案せよ。

次を

```racket
(quick-sort< (list 1 2 3 4 5 6 7 8 9 10 11 12 13 14))
```

手で評価せよ。quick-sort< の再帰的適用は何回必要か。append の再帰的適用は何回か。これは練習問題の第1部に矛盾するか。

練習問題 442. sort< と quick-sort< を定義領域に追加せよ。基本的な例で働くことを保証するよう関数をテストせよ。また、大きなテストケースをランダムに作る関数 create-tests を開発せよ。次に、さまざまなリストで各々がどれほど速く働くかを探れ。

実験は、短いリストでは素直な sort< 関数が quick-sort< にしばしば勝ち、その逆も成り立つという主張を確認するか。

クロスオーバー点を決定せよ。それを使い、大きなリストでは quick-sort< のように、このクロスオーバー点未満のリストでは sort< のように振る舞う clever-sort 関数を構築せよ。練習問題427と比較せよ。

**練習問題 443. gcd-structural のヘッダ材料が与えられたとき、設計レシピの素朴な使用は次のテンプレートやその変種を使うかもしれない。**

```racket
(define (gcd-structural n m)
  (cond
    [(and (= n 1) (= m 1))...]
    [(and (> n 1) (= m 1))...]
    [(and (= n 1) (> m 1))...]
    [else
     (... (gcd-structural (sub1 n) (sub1 m))...
... (gcd-structural (sub1 n) m)...
... (gcd-structural n (sub1 m))...)]))
```

なぜこの戦略では約数を見つけることが不可能か。

練習問題 444. 練習問題443は、gcd-structural の設計がいくらかの計画と設計-by-composition のアプローチを呼ぶことを意味する。

「最大公約数」の説明そのものが、2段階のアプローチを示唆する。まず自然数の約数のリストを計算できる関数を設計する。第2に、n の約数のリストと m の約数のリストに共通する最大の数を選ぶ関数を設計する。全体の関数は次のように見えるだろう。

> **注:** 理想的にはリストではなく集合を使うべきである。

```racket
(define (gcd-structural S L)
  (largest-common (divisors S S) (divisors S L)))

; N[>= 1] N[>= 1] -> [List-of N]
; computes the divisors of l smaller or equal to k
(define (divisors k l)
  '())

; [List-of N] [List-of N] -> N
; finds the largest number common to both k and l
(define (largest-common k l)
  1)
```

divisors が2つの数を消費するのはなぜだと思うか。両方の使用で第1引数として S を消費するのはなぜか。

## 27 テーマの変奏（Variations on the Theme）

アルゴリズムの設計は、与えられた問題よりも解きやすく、かつその解が与えられた問題の解に寄与するような問題をどう作るかという、過程の非公式な記述から始まる。こうした考えを思いつくには、ひらめき、応用領域への没入、そして多種多様な例での経験が必要である。

本章では、アルゴリズムのいくつかの例示的な事例を示す。あるものは多くのアイデアの源である数学から直接採ったものであり、あるものは計算の場面から来る。最初の例は、私たちの原理のグラフィカルな例示、すなわちシェルピンスキーの三角形である。2つ目は、関数の根を求めるという単純な数学的例で分割統治の原理を説明し、次にこの考えを、広く使われる応用である列の探索のための高速アルゴリズムにどう変えるかを示す。第3節は1Stringの列の「構文解析（parsing）」を扱い、これもまた実世界のプログラミングでよくある問題である。

### 27.1 フラクタル、最初の味見（Fractals, a First Taste）

フラクタルは計算幾何学で重要な役割を果たす。Flake は The Computational Beauty of Nature（The MIT Press, 1998）の中で次のように書いている。「幾何学は、分数次元を持つ対象を扱えるよう拡張できる。フラクタルとして知られるそうした対象は、自然に見られる形の豊かさと多様性を捉えることに非常に近づいている。フラクタルは複数の……尺度で構造的な自己相似性を持ち、フラクタルの一部分が全体と同じように見えることがしばしばある。」

> **図156: The Sierpinski triangle**

> 原本は次の画像を含む（画像プレースホルダは図版パイプラインで埋め込み可）:
>
> [image: pict_181.png]
>
> [image: pict_182.png]
>
> [image: pict_183.png]


図156は、シェルピンスキーの三角形として知られるフラクタル形状の例を示している。基本形は（正）三角形であり、中央にあるもののようなものである。この三角形を三角状に十分何度も合成すると、左端の形が得られる。

図156の右端の画像は生成ステップを説明している。それ自体を見ると、三角形が与えられたとき、各辺の中点を見つけ、それらを互いに結ぶ、と述べている。このステップは4つの三角形を生み出す。これらのうち外側の3つそれぞれについて、三角形が小さすぎない限り、この過程を繰り返す。

2htdp/image ティーチパックの図形合成関数に適した別の説明は、中央の画像から右側の画像への遷移に基づく。中央の三角形のうち2つを並べ、その2つの上にもう1つのコピーを置くことで、右側の形も得られる。

> **注:** この解は Marc Smith によるものである。

```racket
> (s-triangle 3)
[image:pict_184.png]
> (beside (s-triangle 3) (s-triangle 3))
[image:pict_185.png]
> (above (s-triangle 3)         (beside (s-triangle 3) (s-triangle 3)))
[image:pict_186.png]
```

本節ではこの別の記述を使ってシェルピンスキーのアルゴリズムを設計する。最初の記述は Accumulators as Results（結果としての累積器）で扱う。目標が正三角形の画像を生成することなので、問題を（正の）数、すなわち三角形の辺の長さで符号化する。この決定から、シグネチャ、目的文、およびヘッダが得られる。

```racket
; Number -> Image
; creates Sierpinski triangle of size side

(define (sierpinski side)
  (triangle side 'outline 'red))
```

ここで、生成的再帰の4つの問いに取り組むときである。

- 与えられた数が、その内側に三角形を描く意味がないほど小さいとき、問題は自明である。
- その場合、三角形を生成すれば十分である。
- そうでなければ、アルゴリズムは大きさ side / 2 のシェルピンスキー三角形を生成しなければならない。なぜなら、そのような三角形をどちらの方向に2つ並べても、大きさ side のものが得られるからである。
- half-sized が大きさ side / 2 のシェルピンスキー三角形なら、
(above half-sized (beside half-sized half-sized)) は大きさ side のシェルピンスキー三角形である。

> **図157: The Sierpinski algorithm**

```racket
(define SMALL 4) ; a size measure in terms of pixels

(define small-triangle (triangle SMALL 'outline 'red))

; Number -> Image
; generative creates Sierpinski Δ of size side by generating
; one for (/ side 2) and placing one copy above two copies

(check-expect (sierpinski SMALL) small-triangle)
(check-expect (sierpinski (* 2 SMALL))
              (above small-triangle
                     (beside small-triangle small-triangle)))

(define (sierpinski side)
  (cond
    [(<= side SMALL) (triangle side 'outline 'red)]
    [else
     (local ((define half-sized (sierpinski (/ side 2))))
       (above half-sized (beside half-sized half-sized)))]))
```


これらの答えがあれば、関数を定義するのは簡単である。図157が詳細を示している。「自明性条件」は、ある定数 SMALL について `(<= side SMALL)` に翻訳される。自明な答えとしては、関数は与えられた大きさの三角形を返す。再帰の場合、local 式が、指定された大きさの半分のシェルピンスキー三角形に half-sized という名前を導入する。再帰呼び出しが小さなシェルピンスキー三角形を生成したら、above と beside でこの画像を合成する。

図は他の2点も際立たせている。第1に、目的文は、関数が何を達成するかの説明として述べられている。

```racket
; creates Sierpinski triangle of size side by...
```

そして、この目標をどう達成するかとして：

```racket
;... generating one of size (/ side 2) and
; placing one copy above two composed copies
```

第2に、例は2つの可能な場合を示している。与えられた大きさが十分小さい場合と、まだ大きすぎる場合である。後者では、期待値を計算する式が、目的文の意味を正確に説明している。

sierpinski は生成的再帰に基づくので、関数を定義してテストすることが最後のステップではない。任意の合法な入力に対してアルゴリズムがなぜ停止するかも考えなければならない。sierpinski の入力は単一の正の数である。その数が SMALL より小さければ、アルゴリズムは停止する。そうでなければ、再帰呼び出しは与えられた数の半分の大きさを使う。したがって、SMALL も正であると仮定すれば、アルゴリズムはすべての正の辺について停止しなければならない。

シェルピンスキーの過程の1つの見方は、直ちに解けるまで問題を半分に分割する、というものである。少し想像力を働かせれば、この過程が、ある性質を持つ数を探すのに使えることがわかる。次の節でこの考えを詳しく説明する。

### 27.2 二分探索（Binary Search）

応用数学者は現実世界を非線形方程式でモデル化し、それを解こうとする。具体的には、問題を数から数への関数 f に翻訳し、

> f(r) = 0.

となるある数 r を探す。値 r は f の根と呼ばれる。

> **図158: A numeric function f with root in interval [ a,b ] (stage 1)**

> 原本は次の画像を含む（画像プレースホルダは図版パイプラインで埋め込み可）:
>
> [image: pict_187.png]


ここに物理の領域からの問題がある。

> **サンプル問題** ロケットが、d0 マイル離れたある目標に向かって直線上を一定速度 v マイル毎時で飛行している。その後、t 時間のあいだ、a マイル毎時の2乗の割合で加速する。いつ目標に到達するか。

物理学によれば、進んだ距離は時間の次の関数である。

> d(t) = (v * t + 1/2 * a * t2)

目標にいつ到達するかという問いは、物体が望むゴールに達する時刻 t0 を求めるよう求めている。

> d0 = (v * t0 + 1/2 * a * t02)

代数から、これは二次方程式であり、d0、a、v が一定の条件を満たせば、そのような方程式を解けることがわかる。

一般に、そうした問題は二次方程式より大きな複雑さを求める。それに応じて、数学者はここ数世紀のあいだ、さまざまな種類の関数のための根を求める方法を開発してきた。本節では、解析学の初期の結果である中間値の定理（Intermediate Value Theorem, IVT）に基づく解を学ぶ。結果として得られるアルゴリズムは、数学の定理に基づく生成的再帰の第一の例である。コンピュータ科学者はそれを二分探索アルゴリズムに一般化した。

中間値の定理は、連続関数 f が区間 [a,b] に根を持つのは、f(a) と f(b) が x 軸の反対側にあるときだ、と述べる。連続とは、「跳ばず」、隙間がなく、「滑らかな」道を進む関数を意味する。

図158は中間値の定理を図示している。関数 f は、途切れのない滑らかなグラフが示唆するように連続関数である。a では x 軸の下に、b では上にあり、実際、この区間のどこかで x 軸と交わる。図では「range 1」とラベルされている。

ここで a と b の中点を見てみよう。

> m = (a+b) / 2

これは区間 [a,b] を、等しい大きさの2つのより小さな区間に分割する。m における f の値を計算し、0 より下か上かを見ることができる。ここでは f(m) > 0 なので、中間値の定理によれば、根は左の区間 [a,m] にある。図がこれを確認する。根は図158で「range 2」とラベルされた区間の左半分にあるからである。

これで根を求める過程の鍵となるステップの記述が得られた。次に、この記述を ISL+ のアルゴリズムに翻訳する。最初の課題は、その目的を述べることである。明らかに、アルゴリズムは関数と、根が見つかると期待する区間の境界を消費する。

```racket
; [Number -> Number] Number Number ->...
(define (find-root f left right)...)
```

3つの仮引数は任意の関数と数であってはならない。find-root が動くには、次が成り立つと仮定しなければならない。

```racket
(or (<= (f left) 0 (f right))
    (<= (f right) 0 (f left)))
```

すなわち、(f left) と (f right) は x 軸の反対側になければならない。

次に、関数の結果を固定し、目的文を定式化する必要がある。簡単に言えば、find-root は根を含む区間を見つける。探索は、区間の大きさ (- right left) が許容できるほど小さくなるまで——たとえばある定数 ε より小さくなるまで——区間を分割する。その時点で、関数は3つの結果のうち1つを生成できる。左境界、右境界、または区間の表現である。どれも区間を完全に特定し、数を返す方が単純なので、左境界を選ぶ。ここに完全なヘッダ材料がある。

> **注:** DrRacket は ε のようなギリシャ記号の使用を許す。しかし代わりに EPSILON と書いてもよい。

```racket
; [Number -> Number] Number Number -> Number
; determines R such that f has a root in [R,(+ R ε)]
; assume f is continuous
; (2) (or (<= (f left) 0 (f right)) (<= (f right) 0 (f left)))
; generative divides interval in half, the root is in
; one of the two halves, picks according to (2)
(define (find-root f left right)
  0)
```

**練習問題 445.** 次の関数定義を考えよ。

```racket
; Number -> Number
(define (poly x)
  (* (- x 2) (- x 4)))
```

これは、手計算で根を求められる二項式を定義している。

```racket
> (poly 2)
0
> (poly 4)
0
```

poly を使い、find-root のための check-satisfied または check-within テストを定式化せよ。

また poly を使い、根を求める過程を例示せよ。区間 [3,6] から始め、ε = 0 について次のように情報を表にまとめよ。

> step left f left right f right mid f mid n=1 3 -1 6.00 8.00 4.50 1.25 n=2 3 -1 4.50 1.25??

次の課題は、アルゴリズム設計の4つの問いに取り組むことである。

1. 問題が解かれたときを述べる条件と、対応する答えが必要である。ここまでの議論を踏まえれば、これは簡単である。
`(<= (- right left) ε)`
2. 自明な場合の対応する結果は left である。
3. 生成の場合には、find-root のための新しい問題を生成する式が必要である。非公式な記述によれば、このステップは中点とその関数値を求めることを要する。
`(local ((define mid (/ (+ left right) 2)) (define f@m (f mid))) ...)` 中点は次に次の区間を選ぶのに使われる。IVT に従い、
`(or (<= (f left) 0 f@m) (<= f@m 0 (f left)))` なら区間 [left,mid] が次の候補であり、一方
`(or (<= f@m 0 (f right)) (<= (f right) 0 f@m))` なら再帰呼び出しに [mid,right] が使われる。コードに翻訳すると、local の本体は条件式でなければならない。
`(cond [(or (<= (f left) 0 f@m) (<= f@m 0 (f left))) (... (find-root f left mid) ...)] [(or (<= f@m 0 (f right)) (<= (f right) 0 f@m)) (... (find-root f mid right) ...)])` どちらの節でも、探索を続けるために find-root を使う。
4. 最後の問いへの答えは明らかである。find-root への再帰呼び出しが f の根を見つけるので、他にすることはない。

完成した関数は図159に示されている。続く練習問題がその設計を詳しく扱う。

> **図159: The find-root algorithm**

```racket
; [Number -> Number] Number Number -> Number
; determines R such that f has a root in [R,(+ R ε)]
; assume f is continuous
; assume (or (<= (f left) 0 (f right)) (<= (f right) 0 (f left)))
; generative divides interval in half, the root is in one of the two
; halves, picks according to assumption
(define (find-root f left right)
  (cond
    [(<= (- right left) ε) left]
    [else
      (local ((define mid (/ (+ left right) 2))
              (define f@mid (f mid)))
        (cond
          [(or (<= (f left) 0 f@mid) (<= f@mid 0 (f left)))
           (find-root f left mid)]
          [(or (<= f@mid 0 (f right)) (<= (f right) 0 f@mid))
           (find-root f mid right)]))]))
```


練習問題 446. 練習問題445からのテストを、図159のプログラムに追加せよ。ε のさまざまな値で実験せよ。

練習問題 447. poly 関数は2つの根を持つ。両方の根を含む区間と poly で find-root を使え。

練習問題 448. find-root アルゴリズムは、仮定が成り立つすべての（連続な）f、left、right について停止する。なぜか。停止性の議論を定式化せよ。

ヒント find-root の引数が大きさ S1 の区間を記述するとせよ。find-root への第1および第2の再帰呼び出しについて、left と right の距離はどれほど大きいか。何ステップのあとで (- right left) は ε 以下になるか。

練習問題 449. 図159に示されているとおり、find-root は次の区間を生成するために、各境界値について f の値を2回計算する。local を使ってこの再計算を避けよ。

さらに、find-root は再帰呼び出しをまたいで境界の値を再計算する。たとえば、(find-root f left right) は (f left) を計算し、[left,mid] が次の区間として選ばれると、find-root は再び (f left) を計算する。find-root に似ているが、各再帰段階で left と right だけでなく (f left) と (f right) も消費する補助関数を導入せよ。

この設計は、(f left) の再計算を最大で何回避けるか。
注 この補助関数への2つの追加引数は各再帰段階で変わるが、その変化は数値引数の変化と関連している。これらの引数はいわゆる累積器（accumulator）であり、Accumulators（累積器）の主題である。

練習問題 450. 関数 f は、(< a b) が成り立つときは常に `(<= (f a) (f b))` が成り立つなら、単調増加である。与えられた関数が連続であるだけでなく単調増加でもあると仮定して、find-root を単純化せよ。

**練習問題 451.** テーブルは2つのフィールドの構造体である。自然数 length と、自然数を消費し、0 から length（排他的）のあいだのものについては答えを生成する関数 array である。

> **注:** Racket を含む多くのプログラミング言語は、テーブルに似た配列やベクタをサポートしている。

```racket
(define-struct table [length array])
; A Table is a structure:
;   (make-table N [N -> Number])
```

このデータ構造はやや珍しいので、例で説明することが重要である。

```racket
(define table1 (make-table 3 (lambda (i) i)))

; N -> Number
(define (a2 i)
  (if (= i 0)
      pi
      (error "table2 is not defined for i =!= 0")))

(define table2 (make-table 1 a2))
```

ここで table1 の array 関数は、その length フィールドが許すより多くの入力について定義されている。table2 はちょうど1つの入力、すなわち 0 についてのみ定義されている。最後に、テーブル内の値を調べるための有用な関数も定義する。

```racket
; Table N -> Number
; looks up the ith value in array of t
(define (table-ref t i)
  ((table-array t) i))
```

テーブル t の根は、(table-array t) の中で 0 に近い数である。根の添字は、(table-ref t i) がテーブル t の根であるような自然数 i である。テーブル t が単調増加であるとは、(table-ref t 0) が (table-ref t 1) より小さく、(table-ref t 1) が (table-ref t 2) より小さく、といった具合であるときである。

find-linear を設計せよ。この関数は単調増加のテーブルを消費し、そのテーブルの根についての最小の添字を見つける。N のための構造的レシピを使い、0 から 1、2 と進み、与えられたテーブルの array-length まで進む。この種の根を求める過程はしばしば線形探索と呼ばれる。

find-binary を設計せよ。これも単調増加のテーブルの根についての最小の添字を見つけるが、そのために生成的再帰を使う。通常の二分探索と同様、アルゴリズムは区間を可能な限り最小の大きさまで狭め、それから添字を選ぶ。停止性の議論を定式化することを忘れずに。

ヒント 鍵となる問題は、テーブルの添字が自然数であり、単なる数ではないことである。したがって find の区間境界引数は自然数でなければならない。この観察が (1) 自明に解ける問題インスタンスの性質、(2) 中点の計算、(3) 次にどの区間を生成するかの決定をどう変えるかを考えよ。具体的にするため、1024 スロットのテーブルで根が 1023 にあると想像せよ。find-linear と find-binary では、それぞれ find への呼び出しが何回必要か。

### 27.3 構文解析の一端（A Glimpse at Parsing）

反復的洗練（Iterative Refinement）で述べたように、コンピュータにはファイルがあり、それは一種の永続メモリを提供する。私たちの観点では、ファイルはただの1Stringのリストであり、ただし特別な文字列で区切られている。

> **注:** 正確な慣習はオペレーティングシステムごとに異なるが、ここでの目的には無関係である。

```racket
; A File is one of:
; – '()
; – (cons "\n" File)
; – (cons 1String File)
; interpretation represents the content of a file
; "\n" is the newline character
```

考えは、File が行に分けられることであり、"\n" はいわゆる改行文字を表し、行の終わりを示す。先に進む前に行も導入しよう。

```racket
; A Line is a [List-of 1String].
```

多くの関数は、ファイルを行のリストとして処理する必要がある。2htdp/batch-io ティーチパックの read-lines もその1つである。具体的には、この関数はファイル

```racket
(list
  "h" "o" "w" " " "a" "r" "e" " " "y" "o" "u" "\n"
  "d" "o" "i" "n" "g" "?" "\n"
  "a" "n" "y" " " "p" "r" "o" "g" "r" "e" "s" "s" "?")
```

を3行のリストに変える。

```racket
(list
  (list "h" "o" "w" " " "a" "r" "e" " " "y" "o" "u")
  (list "d" "o" "i" "n" "g" "?")
  (list "a" "n" "y" " " "p" "r" "o" "g" "r" "e"
        "s" "s" "?"))
```

同様に、ファイル

```racket
(list "a" "b" "c" "\n" "d" "e" "\n" "f" "g" "h" "\n")
```

も3行のリストに対応する。

```racket
(list (list "a" "b" "c")
      (list "d" "e")
      (list "f" "g" "h"))
```

ちょっと待て！ 次の3つの場合について、行のリストとしての表現は何か。'()、(list "\n")、および (list "\n" "\n")。なぜこれらの例は重要なテストケースなのか。

1String の列を行のリストに変える問題は、構文解析問題（parsing problem）と呼ばれる。多くのプログラミング言語は、ファイルから行、語、数、およびいわゆるトークンと呼ばれるその他の種類のものを取り出す関数を提供する。しかし、たとえそうであっても、プログラムがこれらのトークンをさらに構文解析する必要があることはよくある。本節は、構文解析技法の一端を提供する。ただし、構文解析は十分に複雑で、本格的なソフトウェア応用の作成の中心でもあるので、ほとんどの学部課程には少なくとも1つの構文解析のコースがある。したがって、本節をマスターしたあとでも、本物の構文解析問題をきちんと扱えるとは思わないこと。

File を Line のリストに変える関数について、明白なこと——シグネチャ、目的文、上の例の1つ、およびヘッダ——を述べることから始める。

```racket
; File -> [List-of Line]
; converts a file into a list of lines

(check-expect (file->list-of-lines
                (list "a" "b" "c" "\n"
                      "d" "e" "\n"
                      "f" "g" "h" "\n"))
              (list (list "a" "b" "c")
                    (list "d" "e")
                    (list "f" "g" "h")))

(define (file->list-of-lines afile) '())
```

構造のない再帰（Recursion without Structure）での経験を踏まえれば、構文解析過程を述べるのも簡単である。

1. ファイルが '() なら、問題は自明に解ける。
2. その場合、ファイルは行を含まない。
3. そうでなければ、ファイルは少なくとも1つの "\n" または他の1String を含む。これらの項目——もしあれば最初の "\n" までを含めて——を File の残りから分離しなければならない。残りは、file->list-of-lines が解ける同じ種類の新しい問題である。
4. それから、初期セグメントを1つの行として、File の残りから得られる Line のリストに cons すれば十分である。

4つの問いは、生成的再帰関数のテンプレートの素直な具体化を示唆する。初期セグメントをファイルの残りから分離するには、任意に長い1String のリストの走査が必要なので、2つの補助関数を願望リストに載せる。first-line は、最初の "\n" の出現またはリストの終わりまで（ただしそれを含まない）すべての1String を集める。remove-first-line は、first-line が集めるのとまったく同じ項目を取り除く。

> **図160: Translating a file into a list of lines**

```racket
; File -> [List-of Line]
; converts a file into a list of lines
(define (file->list-of-lines afile)
  (cond
    [(empty? afile) '()]
    [else
     (cons (first-line afile)
           (file->list-of-lines (remove-first-line afile)))]))

; File -> Line
; retrieves the prefix of afile up to the first occurrence of NEWLINE
(define (first-line afile)
  (cond
    [(empty? afile) '()]
    [(string=? (first afile) NEWLINE) '()]
    [else (cons (first afile) (first-line (rest afile)))]))

; File -> File
; drops the prefix of afile up to the first occurrence of NEWLINE
(define (remove-first-line afile)
  (cond
    [(empty? afile) '()]
    [(string=? (first afile) NEWLINE) (rest afile)]
    [else (remove-first-line (rest afile))]))

(define NEWLINE "\n") ; the 1String
```


ここから、プログラムの残りを作るのは簡単である。file->list-of-lines では、第1節の答えは '() でなければならない。空のファイルは行を含まないからである。第2節の答えは、(first-line afile) の値を (file->list-of-lines (remove-first-line afile)) の値に cons しなければならない。第1の式が最初の行を計算し、第2の式が残りの行を計算するからである。最後に、補助関数は入力を構造的に再帰的な仕方でたどる。その開発は素直な練習問題である。図160が完全なプログラムコードを示している。

ここに、file->list-of-lines が第2のテストをどう処理するかがある。

```racket
(file->list-of-lines
  (list "a" "b" "c" "\n" "d" "e" "\n" "f" "g" "h" "\n"))
==
(cons
  (list "a" "b" "c")
  (file->list-of-lines
    (list "d" "e" "\n" "f" "g" "h" "\n")))
==
(cons
  (list "a" "b" "c")
  (cons (list "d" "e")
        (file->list-of-lines
          (list "f" "g" "h" "\n"))))
==
(cons (list "a" "b" "c")
      (cons (list "d" "e")
            (cons (list "f" "g" "h")
                  (file->list-of-lines '()))))
==
(cons (list "a" "b" "c")
      (cons (list "d" "e")
            (cons (list "f" "g" "h")
                  '())))
```

この評価は、file->list-of-lines の再帰適用の引数が、与えられたファイルの rest ではほとんどないことのもう一つのリマインダである。また、この生成的再帰が任意の与えられた File について停止することが保証される理由も示す。すべての再帰適用は、与えられたものより短いリストを消費する。つまり、再帰過程は '() に達したときに止まる。

練習問題 452. first-line と remove-first-line の両方に目的文が欠けている。適切な文をはっきり述べよ。

練習問題 453. 関数 tokenize を設計せよ。Line をトークンのリストに変える。ここでのトークンは、1String か、または小文字だけからなり他のものは含まない String のいずれかである。すなわち、すべての空白1String は落とされ、他の非文字はそのまま残り、連続する文字はすべて「語」に束ねられる。ヒント string-whitespace? 関数について読め。

**練習問題 454.** create-matrix を設計せよ。この関数は数 n と n2 個の数のリストを消費する。たとえば [image: pict_188.png] 行列を生成する。

```racket
(check-expect
  (create-matrix 2 (list 1 2 3 4))
  (list (list 1 2)
        (list 3 4)))
```

2つ目の例を自分で作れ。

## 28 数学的な例（Mathematical Examples）

数学的問題の多くの解は生成的再帰を用いる。将来のプログラマがそのような解に慣れ親しむべき理由は2つある。一方では、かなりの数のプログラミング課題は本質的に、こうした数学的アイデアをプログラムに変えることである。他方では、そのような数学的問題を練習することは、アルゴリズムの設計の着想になることが多い。本章はそうした問題を3つ扱う。

### 28.1 ニュートン法（Newton’s Method）

Binary Search は、数学関数の根を見つける1つの方法を導入する。同節の練習問題がスケッチするように、その方法は表、ベクタ、配列の中の特定の値を見つけるといった計算問題へ自然に一般化される。数学的応用では、プログラマは解析学に起源を持つ方法を用いる傾向がある。著名なものの1つがニュートンによるものである。二分探索と同様に、いわゆるニュートン法は、根の近似を「十分近い」になるまで繰り返し改善する。初期推測、たとえば r1 から始め、過程の本質は f の r1 における接線を構成し、その根を求めることである。接線は関数を近似するが、その根を求めることも簡単である。この過程を十分に繰り返すことで、アルゴリズムは (f r) が0に十分近い根 r を見つけられる。

> **注:** ニュートンはこの事実を証明した。

明らかに、この過程は接線についての2つの領域知識——その傾きと根——に依存する。非形式的には、f の点 r1 における接線は、点 (r1, f(r1)) を通り、f と同じ傾きを持つ直線である。接線の傾きを得る1つの数学的方法は、r1 から等距離にある x 軸上の近い2点を選び、それらの2点における f の値で決まる直線の傾きを使うことである。慣例として、小さな数 ε を選び、r1 + ε と r1 - ε を使う。すなわち、点は (r1 - ε, f(r1 - ε)) と (r1 + ε, f(r1 + ε)) であり、これらが直線と傾きを決める：

> [image: pict_189.png]

練習問題 455. この数式を ISL+ 関数 slope に翻訳せよ。これは関数 f と数 r1 を、f の r1 における傾きに写像する。ε はグローバル定数と仮定せよ。例には、正確な傾きが分かる関数——水平線、線形関数、そして微積分を知っていれば多項式など——を使え。

領域知識の第2の片は、接線の根に関するものである。接線は単なる直線または線形関数である。接線は (r1, f(r1)) を通り、上記の傾きを持つ。数学的には次のように定義される：

> [image: pict_190.png]

接線の根を見つけるとは、tangent(root-of-tangent) が0に等しくなる値 root-of-tangent を見つけることである：

> [image: pict_191.png]

この方程式は素直に解ける：

> [image: pict_192.png]

練習問題 456. root-of-tangent を設計せよ。これは f と r1 を、(r1,(fr1)) を通る接線の根に写像する関数である。

これで設計レシピを使い、ニュートン過程の記述を ISL+ プログラムに翻訳できる。その関数——発明者に敬意を表して newton と呼ぼう——は関数 f と数 r1 を消費する：

```racket
; [Number -> Number] Number -> Number
; finds a number r such that (f r) is small
; generative repeatedly generates improved guesses
(define (newton f r1) 1.0)
```

newton のテンプレートについては、生成的再帰の設計レシピの中心となる4つの問いに向かう：

1. (fr1) が0に十分近いなら、問題は解けている。0に近いとは、(fr1) が小さな正の数か小さな負の数であることを意味し得る。したがってその絶対値を検査する：
(<= (abs (f r1)) ε)
2. 解は r1 である。
3. アルゴリズムの生成的ステップは、f の r1 における接線の根を見つけることから成り、それが次の推測を生成する。f とこの新しい推測に newton を適用することで、過程を再開する。
4. 再帰の答えは、元の問題の答えでもある。

> **図161: The Newton process**

```racket
; [Number -> Number] Number -> Number
; finds a number r such that (<= (abs (f r)) ε)

(check-within (newton poly 1) 2 ε)
(check-within (newton poly 3.5) 4 ε)

(define (newton f r1)
  (cond
    [(<= (abs (f r1)) ε) r1]
    [else (newton f (root-of-tangent f r1))]))

; see exercise 455
(define (slope f r) ...)

; see exercise 456
(define (root-of-tangent f r) ...)
```


図161は newton を示す。Binary Search の find-root のテストから導いた2つのテストも含む。結局のところ、両関数とも関数の根を探し、poly には2つの既知の根がある。

> **図162: The graph of poly on the interval [ -1 , 5 ]**

> 原本は次の画像を含む（画像プレースホルダは図版パイプラインで埋め込み可）:
>
> [image: pict_193.png]


newton の設計はまだ終わっていない。設計レシピの新しい第7ステップは、関数の停止挙動の調査を求める。newton について、問題は poly で現れる：

```racket
; Number -> Number
(define (poly x) (* (- x 2) (- x 4)))
```

前述のとおり、その根は2と4である。図162の poly のグラフはこれらの根を確認し、また2つの根のあいだで関数が平坦になることも示す。数学に傾倒した人にとって、この形状は初期推測3に対して newton が何を計算するかという疑問を起こす：

```racket
> (poly 3)
-1
> (newton poly 3)
/:division by zero
```

説明は、slope が「悪い」値を生成し、root-of-tangent 関数がそれをエラーに変えることである：

```racket
> (slope poly 3)
0
> (root-of-tangent poly 3)
/:division by zero
```

この実行時エラーに加え、newton は停止に関してさらに2つの問題を示す。幸い、どちらも poly で示せる。第1は数の性質に関するもので、The Arithmetic of Numbers で簡単に触れた。プログラミングの多くの初学者練習問題では厳密数と非厳密数の区別を無視してよいが、数学をプログラムに翻訳する段になると、極度の注意が必要である。次を考えよ：

```racket
> (newton poly 2.9999)
```

ISL+ プログラムは 2.9999 を厳密数として扱い、newton 内の計算もそのように処理する。ただし数が整数ではないため、計算は厳密な有理分数を使う。分数の算術は非厳密数の算術よりずっと遅くなることがあるので、上記の関数呼び出しは DrRacket でかなりの時間を要する。コンピュータによっては数秒から1分以上かかることもある。この形の計算を引き起こす他の数を選んでしまうと、newton への呼び出しがまったく停止しないように見えることさえある。

第2の問題は非停止に関するものである。例を示す：

```racket
> (newton poly #i3.0)
```

初期推測として非厳密数 #i3.0 を使う。これは3と異なり、別種の問題を引き起こす。具体的には、slope 関数が poly に対して非厳密な0を生成し、root-of-tangent は無限大へ飛ぶ：

```racket
> (slope poly #i3.0)
#i0.0
> (root-of-tangent poly #i3.0)
#i+inf.0
```

その結果、評価は直ちに無限ループに落ちる。

> **注:** newton 内の計算は #i+inf.0 を +nan.0 に変える。これは「数ではない」と告げるデータの一片である。ほとんどの算術演算はこの値を伝播し、それが newton の挙動を説明する。

要するに、newton は複雑な停止挙動に関する問題の全範囲を示す。ある入力では正しい結果を生成する。別の入力ではエラーを合図する。さらに別の入力では無限ループに入るか、入ったように見える。newton のヘッダ——または他の何らかの文書——は、関数を使いたい他者や将来の読者にこれらの複雑さを警告しなければならず、一般的なプログラミング言語の良い数学ライブラリはそうしている。

練習問題 457. 関数 double-amount を設計せよ。これは貯蓄口座が月次で固定利率の利息を支払うとき、与えられた金額が2倍になるのに何ヶ月かかるかを計算する。

> **注:** この練習問題は Adrian German が提案した。

領域知識 わずかな代数的操作により、与えられた金額は無関係であることを示せる。重要なのは利率だけである。また領域の専門家は、利率 r が「小さい」かぎり、およそ 72/r ヶ月後に2倍になると知っている。

### 28.2 数値積分（Numeric Integration）

多くの物理学の問題は、曲線の下の面積を求めることに帰着する：

> サンプル問題 車が一定速度 v メートル毎秒で走る。5、10、15 秒でどれだけ進むか。ロケットが一定加速度 [image: pict_194.png] で離陸する。5、10、15 秒後にどの高さに達するか。

物理学は、一定速度 v で t 秒動く乗り物は [image: pict_195.png] メートル進むと教える。加速する乗り物では、進んだ距離は経過時間 t の二乗に依存する：

> [image: pict_196.png]

一般に、法則は距離が、時間 t にわたる速度 v(t) のグラフの下の面積に対応すると教える。

> **図163: Distance traveled with constant vs accelerating speed**

> 原本は次の画像を含む（画像プレースホルダは図版パイプラインで埋め込み可）:
>
> [image: pict_197.png]
>
> [image: pict_198.png]


図163はこの考えを図解で示す。左では2つのグラフの重ね合わせが見える。実線の平らな線は乗り物の速度、上昇する破線は進んだ距離である。素早く確認すると、後者は実際に、前者と x 軸が各時点で定める面積である。同様に、右のグラフは一定加速度で動くロケットとその到達高度の関係を示す。ある特定の区間について関数のグラフの下のこの面積を求めることは、（関数の）積分と呼ばれる。

数学者は2つのサンプル問題に対して正確な答えを与える公式を知っているが、一般問題は計算的な解を求める。問題は、曲線がしばしば図164のような複雑な形状を持つことであり、誰かが x 軸、a と b とラベル付けされた垂直線、および f のグラフのあいだの面積を知る必要があることを示唆する。応用数学者は、多くの小さな幾何学的形状の面積を足し合わせて、そのような面積を近似的に求める。したがって、これらの計算を扱うアルゴリズムを開発するのは自然である。

> **図164: Integrating a function f between a and b**

> 原本は次の画像を含む（画像プレースホルダは図版パイプラインで埋め込み可）:
>
> [image: pict_199.png]


積分アルゴリズムは3つの入力を消費する：関数 f と2つの境界 a と b である。第4の部分、x 軸は暗黙である。これは次のシグネチャを示唆する：

```racket
; [Number -> Number] Number Number -> Number
```

積分の背後にある考えを理解するには、定数関数や線形関数のような単純な例を調べるのが最善である。そこで次を考えよ：

```racket
(define (constant x) 20)
```

constant を integrate に渡し、12 と 22 を添えると、幅 10、高さ 20 の長方形が記述される。この長方形の面積は 200 であり、次のテストが得られる：

```racket
(check-expect (integrate constant 12 22) 200)
```

同様に、linear を使って第2のテストを作ろう：

```racket
(define (linear x) (* 2 x))
```

linear、0、10 を integrate と使うと、面積は底辺の幅 10、高さ 20 の三角形である。テストとしての例は次のとおり：

```racket
(check-expect (integrate linear 0 10) 100)
```

結局のところ、三角形の面積は底辺の幅と高さの積の半分である。

第3の例では、領域固有の知識を利用する。前述のとおり、数学者はある関数の下の面積を正確に求める方法を知っている。例えば、関数

> [image: pict_200.png]

の区間 [a,b] における面積は、次の公式で計算できる

> [image: pict_201.png]

この考えを具体的なテストに変える仕方は次のとおり：

```racket
(define (square x) (* 3 (sqr x)))

(check-expect (integrate square 0 10)
              (- (expt 10 3) (expt 0 3)))
```

> **図165: A generic integration function**

```racket
(define ε 0.1)

; [Number -> Number] Number Number -> Number
; computes the area under the graph of f between a and b
; assume (< a b) holds

(check-within (integrate (lambda (x) 20) 12 22) 200 ε)
(check-within (integrate (lambda (x) (* 2 x)) 0 10) 100 ε)
(check-within (integrate (lambda (x) (* 3 (sqr x))) 0 10)
              1000
              ε)

(define (integrate f a b) #i0.0)
```


図165は設計レシピの最初の3ステップの結果をまとめる。図は目的文と、2つの区間境界に関する明白な仮定を加える。check-expect の代わりに check-within を使い、このような計算における計算的近似に伴う数値的不正確さを予期している。同様に、integrate のヘッダは戻り結果として #i0.0 を指定し、関数が非厳密数を返すと期待されることを合図する。

次の2つの練習問題は、領域知識を積分関数にどう変えるかを示す。どちらの関数もかなり粗い近似を計算する。第1の設計は数学的公式だけを使い、第2は構造的設計の考えも少し活用する。これらの練習問題を解くことで、生成的再帰による積分アルゴリズムを提示する本節の核心への必要な理解が得られる。

**練習問題 458. Kepler は単純な積分方法を提案した。f の下の a と b のあいだの面積の推定を計算するには、次のように進む：**

> **注:** この方法は Kepler の公式として知られる。

1. 区間を mid = (a + b) / 2 で半分に分ける；
2. 次の2つの台形の面積を計算する：
[(a,0),(a,f(a)),(mid,0),(mid,f(mid))][(mid,0),(mid,f(mid)),(b,0),(b,f(b))]；
3. それから2つの面積を加える。

領域知識 これらの台形を見てみよう。可能な2つの形状を、煩雑さを減らすための最小限の注釈付きで示す：

> [image: pict_202.png]
>
> [image: pict_203.png]

左の形状は f(L) > f(R) を仮定し、右は f(L) < f (R) の場合を示す。非対称にもかかわらず、単一の公式でこれらの台形の面積を計算できる：

> [image: pict_204.png]

やめ！ この公式が、左の台形では三角形の面積を下側の長方形の面積に加え、右の台形では大きな長方形の面積から三角形を引くことを自分で納得せよ。

また、上記の公式が次と等しいことを示せ

> [image: pict_205.png]

これは公式の非対称性の数学的検証である。

関数 integrate-kepler を設計せよ。すなわち、数学的知識を ISL+ 関数に変えよ。図165のテストケースをこの用途に適合させよ。3つのテストのうちどれが失敗し、どれだけずれるか。

練習問題 459. もう1つの単純な積分方法は、面積を多くの小さな長方形に分ける。各長方形は固定幅を持ち、長方形の中央での関数グラフと同じ高さである。長方形の面積を足し合わせると、関数のグラフの下の面積の推定が得られる。

次を使おう

> R = 10

これは考慮する長方形の個数を表す。したがって各長方形の幅は

> [image: pict_206.png]

これらの長方形の1つの高さは、その中点における f の値である。最初の中点は明らかに a に長方形の幅の半分を加えたところ、

> [image: pict_207.png]

であり、その面積は

> [image: pict_208.png]

第2の長方形の面積を計算するには、最初の中点に1つの長方形の幅を加えなければならない：

> [image: pict_209.png]

第3のものでは

> [image: pict_210.png]

一般に、i 番目の長方形には次の公式を使える：

> [image: pict_211.png]

最初の長方形の添字は 0、最後は R - 1 である。

これらの長方形を使い、グラフの下の面積を求められる：

> [image: pict_212.png]

過程の記述を ISL+ 関数に変え、integrate-rectangles と名づけよ。図165のテストケースをこの場合に適合させよ。

アルゴリズムが使う長方形が多いほど、その推定は実際の面積に近づく。R をトップレベルの定数にし、アルゴリズムの精度が ε 値 0.1 の問題を解消するまで10の倍数で増やせ。

ε を 0.01 に減らし、失敗するテストケースがなくなるまで再び R を増やせ。結果を練習問題458と比較せよ。

練習問題458の Kepler の方法は、Binary Search で導入した二分探索のような分割統治戦略を直ちに示唆する。大まかに言えば、アルゴリズムは区間を2つに分割し、各片の面積を再帰的に計算し、2つの結果を加える。

練習問題 460. アルゴリズム integrate-dc を開発せよ。これは分割統治戦略を使い、境界 a と b のあいだで関数 f を積分する。区間が十分小さいときは Kepler の方法を使え。

練習問題460の分割統治アプローチは無駄が多い。グラフの一部で水平で、別の部分で急激に変化する関数を考えよ。具体例は図166を見よ。グラフの水平な部分では、区間を分割し続ける意味がない。2つの半分についてと同様に、完全な区間について台形を計算するのも同じくらい簡単である。しかし「波打つ」部分では、グラフの不規則性が合理的に小さくなるまで、アルゴリズムは区間の分割を続けなければならない。

> **図166: A candidate for adaptive integration**

> 原本は次の画像を含む（画像プレースホルダは図版パイプラインで埋め込み可）:
>
> [image: pict_213.png]


f が水平なときを発見するため、アルゴリズムを次のように変えられる。区間がどれだけ大きいかを検査するだけでなく、新しいアルゴリズムは3つの台形の面積を計算する：与えられたものと2つの半分である。2つの差が高さ ε、幅 [image: pict_214.png] の小さな長方形の面積より小さいなら、

> [image: pict_215.png]

全体の面積が良い近似であると仮定して安全である。言い換えれば、アルゴリズムは f が誤差マージンに影響するほど変化するかを判定する。そうなら分割統治アプローチを続け、そうでなければ停止して Kepler 近似を使う。

練習問題 461. integrate-adaptive を設計せよ。すなわち、再帰的過程の記述を ISL+ アルゴリズムに変えよ。図165のテストケースをこの用途に適合させよ。

integrate-adaptive の停止については議論しないこと。

integrate-adaptive は常に、integrate-kepler や練習問題459の integrate-rectangles より良い答えを計算するか。integrate-adaptive が改善を保証する側面は何か。

用語 このアルゴリズムは適応的積分と呼ばれる。グラフの必要な部分に自動的に時間を割り当て、他の部分にはほとんど時間を使わないからである。具体的には、水平な f の部分ではわずかな計算だけを行い、他の部分では誤差マージンを減らすために小さな区間を調べる。コンピュータ科学は多くの適応的アルゴリズムを知っており、integrate-adaptive はその1つにすぎない。

### 28.3 プロジェクト：ガウスの消去法（Project: Gaussian Elimination）

数学者は1変数の方程式の解を探すだけでなく、連立一次方程式の系全体も研究する：

> サンプル問題 物々交換の世界では、石炭 (x)、石油 (y)、ガス (z) の価値が次の交換方程式で決まる：
> [image: pict_216.png]

そのような方程式系の解は、変数ごとに1つの数の集まりから成り、変数を対応する数で置き換えると、各方程式の両辺が同じ数に評価される。実行中の例では、解は

> x = 1, y = 1, and z = 2.

である。この主張は容易に検査できる：

> [image: pict_217.png]

3つの方程式は次に帰着する

> 10 = 10, 31 = 31, and 1 =1.

> **図167: A data representation for systems of equations**

```racket
; An SOE is a non-empty Matrix.
; constraint for (list r1 ... rn), (length ri) is (+ n 1)
; interpretation represents a system of linear equations

; An Equation is a [List-of Number].
; constraint an Equation contains at least two numbers.
; interpretation if (list a1 ... an b) is an Equation,
; a1, ..., an are the left-hand-side variable coefficients
; and b is the right-hand side

; A Solution is a [List-of Number]

(define M ; an SOE
  (list (list 2 2  3 10) ; an Equation
        (list 2 5 12 31)
        (list 4 1 -2  1)))

(define S '(1 1 2)) ; a Solution
```


図167は問題領域のデータ表現を導入する。方程式系とその解の例も含む。この表現は方程式系の本質を捉える。すなわち、左辺の変数の数値係数と右辺の値である。変数の名前は役割を果たさない。関数の仮引数のようなもので、一貫して名前を付け替えれば方程式は同じ解を持つからである。

本節の残りでは、次の関数を使うと便利である：

```racket
; Equation -> [List-of Number]
; extracts the left-hand side from a row in a matrix
(check-expect (lhs (first M)) '(2 2 3))
(define (lhs e)
  (reverse (rest (reverse e))))

; Equation -> Number
; extracts the right-hand side from a row in a matrix
(check-expect (rhs (first M)) 10)
(define (rhs e)
  (first (reverse e)))
```

練習問題 462. 関数 check-solution を設計せよ。SOE と Solution を消費する。Solution からの数を SOE の Equations の変数に代入した結果、左辺の値と右辺の値が等しくなるなら結果は #true、そうでなければ関数は #false を生成する。check-solution を使い、check-satisfied でテストを定式化せよ。

ヒント まず関数 plug-in を設計せよ。Equation の左辺と Solution を消費し、解からの数を変数に代入したときの左辺の値を計算する。

ガウスの消去法は、連立一次方程式の解を見つける標準的な方法である。2つのステップから成る。第1ステップは、方程式系を形は異なるが同じ解を持つ系に変換することである。第2ステップは、一度に1つの方程式の解を見つけることである。ここでは第1ステップに焦点を当てる。生成的再帰のもう1つの興味深い例だからである。

ガウスの消去アルゴリズムの第1ステップは「三角化」と呼ばれる。結果が三角形の形の方程式系になるからである。対照的に、元の系は長方形である。この用語を理解するため、元の系を表す次のリストを見よ：

```racket
(list (list 2 2  3 10)
      (list 2 5 12 31)
      (list 4 1 -2 1))
```

三角化はこの行列を次に変換する：

```racket
(list (list 2 2  3 10)
      (list   3  9 21)
      (list      1  2))
```

約束どおり、この方程式系の形は（おおよそ）三角形である。

**練習問題 463. 次の方程式系**

> [image: pict_218.png]

**が ([image: pict_219.png]) とラベル付けされたものと同じ解を持つことを確認せよ。手計算と練習問題462の check-solution の両方で行え。**

三角化の鍵となる考えは、残りのものから最初の Equation を引くことである。1つの Equation を別のものから引くとは、2つの Equations の対応する係数を引くことである。実行中の例では、第1方程式を第2から引くと次の行列が得られる：

```racket
(list (list 2 2  3 10)
      (list 0 3  9 21)
      (list 4 1 -2  1))
```

これらの減算の目標は、最初の方程式以外のすべての第1列に0を置くことである。第3方程式について、第1位置に0を得るには、第1方程式を第3から2回引く必要がある：

```racket
(list (list 2  2  3  10)
      (list 0  3  9  21)
      (list 0 -3 -8 -19))
```

慣例に従い、最後の2方程式から先頭の0を落とす：

```racket
(list (list 2  2  3   10)
      (list    3  9   21)
      (list   -3 -8  -19))
```

すなわち、まず第1行の各項目に2を掛け、その結果を最後の行から引く。前述のとおり、これらの減算は解を変えない。すなわち、元の系の解は変換された系の解でもある。

> **注:** 数学はそのような事実の証明法を教える。私たちはそれらを使う。

**練習問題 464. 次の方程式系**

> [image: pict_220.png]

**が ([image: pict_221.png]) とラベル付けされたものと同じ解を持つことを確認せよ。再び手計算と練習問題462の check-solution の両方で行え。**

練習問題 465. subtract を設計せよ。この関数は等しい長さの2つの Equations を消費する。第1から第2の倍数を項目ごとに「引き」、結果の Equation の第1位置に0があるようにする。先頭係数は0であることが分かっているので、subtract は減算から生じるリストの残りを返す。

さて SOE の残りを考えよ：

```racket
(list (list  3  9   21)
      (list -3 -8  -19))
```

これも SOE なので、同じアルゴリズムを再び適用できる。実行中の例では、この次の減算ステップは第1 Equation を -1 倍して第2から引くことを求める。そうすると次が得られる

```racket
(list (list 3  9 21)
      (list    1  2))
```

この SOE の残りは単一の方程式であり、これ以上単純化できない。

**練習問題 466. 三角 SOE の表現は次のとおり：**

```racket
; A TM is an [NEList-of Equation]
; such that the Equations are of decreasing length:
;   n + 1, n, n - 1,..., 2.
; interpretation represents a triangular matrix
```

triangulate アルゴリズムを設計せよ：

```racket
; SOE -> TM
; triangulates the given system of equations
(define (triangulate M)
  '(1 2))
```

上記の例をテストに変え、緩い記述に基づく4つの問いへの明示的な答えを述べよ。

設計レシピの停止ステップはまだ扱わないこと。

残念ながら、練習問題466の解は、望ましい三角系を生成できないことがある。次の方程式系の表現を考えよ：

```racket
(list (list 2  3  3 8)
      (list 2  3 -2 3)
      (list 4 -2  2 4))
```

その解は x = 1, y = 1, and z = 1 である。

第1ステップは第1行を第2から引き、最後の行から2回引くことであり、次の行列が得られる：

```racket
(list (list  2  3  3   8)
      (list     0 -5  -5)
      (list    -8 -4 -12))
```

次に、三角化は行列の残りに焦点を当てる：

```racket
(list (list   0 -5  -5)
      (list  -8 -4 -12))
```

しかしこの行列の最初の項目は0である。0で割ることは不可能なので、アルゴリズムは subtract 経由でエラーを合図する。

この問題を克服するには、問題領域からのもう1つの知識を使う必要がある。数学は、方程式系の中で方程式を入れ替えても解に影響しないと教える。もちろん、方程式を入れ替えるとき、いずれは先頭係数が0でない方程式を見つけなければならない。ここでは最初の2つを単に入れ替えられる：

```racket
(list (list  -8 -4 -12)
      (list   0 -5  -5))
```

ここから以前と同様に続け、残りのものから第1方程式を0回引く。最終的な三角行列は：

```racket
(list (list 2  3  3   8)
      (list   -8 -4 -12)
      (list      -5  -5))
```

やめ！ x = 1, y = 1, and z = 1 がこれらの方程式の解のままであることを示せ。

練習問題 467. 練習問題466のアルゴリズム triangulate を改訂し、残りのものから第1方程式を引く前に、方程式を回転して先頭係数が0でないものを先に見つけるようにせよ。

このアルゴリズムは可能なすべての方程式系に対して停止するか。

ヒント 次の式は非空リスト L を回転する：

```racket
(append (rest L) (list (first L)))
```

なぜか説明せよ。

ある SOE には解がない。次を考えよ：

> [image: pict_222.png]

この SOE を三角化しようと——手で、または練習問題467の解で——すると、すべての方程式が0で始まる中間行列に至る：

> [image: pict_223.png]

練習問題 468. 練習問題467の triangulate を修正し、先頭係数がすべて0の SOE に出会ったらエラーを合図するようにせよ。

練習問題463の (*) のような三角方程式系を得たあと、方程式を1つずつ解ける。具体例では、最後の方程式は z が2だと述べる。この知識を備え、代入により第2方程式から z を消去できる：

> [image: pict_224.png]

そうすると、y の値が決まる：

> [image: pict_225.png]

z = 2 と y = 1 が分かったので、これらの値を第1方程式に代入できる：

> [image: pict_226.png]

これは再び1変数の方程式を与え、次のように解く：

> [image: pict_227.png]

これでようやく x の値が得られ、SOE 全体の完全な解が得られる。

練習問題 469. 関数 solve を設計せよ。三角 SOE を消費し、解を生成する。

ヒント 設計には構造的再帰を使え。最後の n 変数についての解が与えられたとき、n+1 変数の単一の線形方程式を解く関数の設計から始めよ。一般に、この関数は左辺の残りの値を代入し、結果を右辺から引き、第1係数で割る。この提案と上記の例で実験せよ。

挑戦 既存の抽象化と lambda を使って solve を設計せよ。

練習問題 470. gauss を定義せよ。これは練習問題468の triangulate 関数と練習問題469の solve 関数を組み合わせる。

## 29 バックトラックするアルゴリズム（Algorithms that Backtrack）

問題解決は常に一直線に進むわけではない。ある方針に従ったあと、間違った方向へ進んだために行き詰まることがある。明らかな選択肢のひとつは、運命的な決定をした地点までバックトラックし、別の方向へ進むことである。一部のアルゴリズムはまさにそのように動く。本章では2つの例を示す。第1節はグラフを走査するアルゴリズムを扱う。第2節は、チェスのパズルの文脈でバックトラックを使う拡張練習問題である。

### 29.1 グラフの走査（Traversing Graphs）

グラフは私たちの世界にもコンピューティングの世界にも遍在する。人々の集団、たとえばあなたの学校の生徒を想像せよ。名前をすべて書き出し、互いに知っている人の名前同士をつなげよ。これであなたは最初の無向グラフを作ったことになる。

さて図168を見よ。これは小さな有向グラフを示している。7つのノード——丸で囲まれた文字——と9つの辺——矢印——からなる。このグラフは電子メール・ネットワークの小さな版を表しているかもしれない。ある会社と、行き交うすべてのメールを想像せよ。全従業員のメール・アドレスを書き出せ。次に、アドレスごとに、その所有者が1週間のうちにメールを送るすべてのアドレスへ矢印を引け。こうして図168の有向グラフを作ることになるが、実際にははるかに複雑で、ほとんど見通しが利かないものになるかもしれない。

> **図168: A directed graph**

> 原本は次の画像を含む（画像プレースホルダは図版パイプラインで埋め込み可）:
>
> [image: pict_228.png]


一般に、グラフはノードの集まりと、ノードをつなぐ辺の集まりからなる。有向グラフでは、辺はノード間の一方向の接続を表す。無向グラフでは、辺はノード間の双方向の接続を表す。この文脈で、次はよくある種類の問題である。

> **注:** 社会科学者は、こうしたアルゴリズムを使って会社内の権力構造を明らかにする。同様に、メールの内容を知らなくても、人々の起こりそうな行動を予測するためにこうしたグラフを使う。

> 見本問題 大企業の有向メール・グラフにおいて、ある人を別の人に紹介する道筋を提案するアルゴリズムを設計せよ。プログラムは、確立されたメール接続を表す有向グラフと2つのメール・アドレスを消費する。最初のメールと2番目のメールをつなぐメール・アドレスの列を返す。

数理科学者は、求める列をパス（path）と呼ぶ。

図168は見本問題を具体的にする。たとえば、プログラムが C から D へのパスを見つけられるかを試したいとしよう。このパスは起点ノード C と終点ノード D からなる。対照的に、E と D をつなぎたいなら、パスは2つある：

- E から F へメールを送り、それから D へ送る。
- E から C へ送り、それから D へ送る。

2つのノードをパスでつなぐことが不可能な場合もある。図168のグラフでは、矢印に従って C から G へ進むことはできない。

図168を見れば、あまり考えなくてもあるノードから別のノードへどう行くかを簡単に分かる。そこで一瞬、図168のグラフが大きな公園だと想像せよ。また、誰かがあなたは E にいて G へ行く必要があると言ったとしよう。明らかに2つの道があり、一方は C へ、もう一方は F へ続く。最初の道を進み、E から F へ行くことも可能だと覚えておく。すると新しい問題が生まれる。すなわち、C から G へどう行くかである。重要な洞察は、この新しい問題が元の問題と同じ種類だということである。あるノードから別のノードへのパスを求めている。さらに、その問題が解けるなら、E から G へ行く方法が分かる——E から C へのステップを足せばよい。しかし C から G へのパスはない。幸い、E から F へ行くことも可能だと覚えているので、選択の余地があった地点までバックトラックし、そこから探索を再開できる。

ではこのアルゴリズムを体系的に設計しよう。一般的な設計レシピに従い、データ分析から始める。図168のグラフの、2つの簡潔なリスト表現を次に示す。

> (define sample-graph '((A (B E)) (B (E F)) (C (D)) (D ()) (E (C F)) (F (D G)) (G ()))) (define sample-graph '((A B E) (B E F) (C D) (D) (E C F) (F D G) (G)))

どちらもノードごとに1つのリストを含む。これらのリストはそれぞれ、ノードの名前で始まり、その（直接の）近傍、すなわち1本の矢印をたどって到達できるノードが続く。2つは、ノード（の名前）とその近傍をどうつなぐかが異なる。左は list を使い、右は cons を使う。たとえば、2番目のリストは、図168におけるノード B とその E および F への2本の出辺を表す。左側では `'B` が2要素リストの先頭の名前であり、右側では3要素リストの先頭の名前である。

練習問題 471. 上記の定義の一方を、list と適切な記号を使った正しいリスト形に翻訳せよ。

ノードのデータ表現は素直である：

```racket
; A Node is a Symbol.
```

任意個のノードと辺を許す、すべての Graph 表現のクラスを記述するデータ定義を定式化せよ。上記の表現のうち1つだけが Graph に属すればよい。

関数 neighbors を設計せよ。Node n と Graph g を消費し、g における n の直接の近傍のリストを生成する。

Node と Graph のデータ定義——どちらを選んでも、neighbors も設計してあるかぎり——を使い、グラフ内のパスを探索する関数 find-path のシグネチャと目的文を定式化できる：

```racket
; Node Node Graph -> [List-of Node]
; finds a path from origination to destination in G
(define (find-path origination destination G)
  '())
```

このヘッダが未定のまま残しているのは、結果の正確な形である。結果がノードのリストであることは含意しているが、どのノードを含むかは述べていない。

この曖昧さと、なぜそれが重要かを理解するため、上の例を調べよう。ISL+ では、次のように定式化できる：

```racket
(find-path 'C 'D sample-graph)
(find-path 'E 'D sample-graph)
(find-path 'C 'G sample-graph)
```

find-path への最初の呼び出しは一意なパスを返さなければならず、2番目は2つから1つを選び、3番目は sample-graph に `'C` から `'G` へのパスがないことを合図しなければならない。戻り値をどう構成するかについて、次の2つの可能性がある：

- 関数の結果は、起点ノードから終点ノードへ至るすべてのノードからなり、それら2つも含む。この場合、空のパスを使って2つのノード間にパスがないことを表せる。
  > **注:** 与えられた2つのノードの一方を飛ばすなど、他のやり方も想像しやすい。
- あるいは、呼び出し自体がすでに2つのノードを挙げているので、出力はパスの「内部」ノードだけを挙げてもよい。その場合、最初の呼び出しの答えは `'()` になる。`'D` が `'C` の直接の近傍だからである。もちろん、そのとき `'()` は失敗を合図できなくなる。

> **注:** 与えられた2つのノードの一方を飛ばすなど、他のやり方も想像しやすい。

パスがないという問題については、この概念を合図する別個の値を選ばなければならない。`#false` は別個であり、意味があり、どちらの場合にも使えるので、それを選ぶ。複数パスの問題については、今は選択を先送りし、例の節で両方の可能性を列挙する：

```racket
; A Path is a [List-of Node].
; interpretation The list of nodes specifies a sequence
; of immediate neighbors that leads from the first
; Node on the list to the last one.

; Node Node Graph -> [Maybe Path]
; finds a path from origination to destination in G
; if there is no path, the function produces #false

(check-expect (find-path 'C 'D sample-graph)
              '(C D))
(check-member-of (find-path 'E 'D sample-graph)
                 '(E F D) '(E C D))
(check-expect (find-path 'C 'G sample-graph)
              #false)

(define (find-path origination destination G)
  #false)
```

次の設計ステップは、関数の4つの本質的な部分を理解することである。すなわち「自明な問題」の条件、それに対応する解、新しい問題の生成、および組み合わせのステップである。上の探索過程の議論と3つの例の分析が答えを示唆する：

1. 与えられた2つのノードが、与えられたグラフ内で矢印によって直接つながっているなら、パスはこれら2つのノードだけからなる。しかしさらに単純な場合がある。すなわち find-path の origination 引数が destination と等しいときである。
2. その第2の場合、問題は本当に自明であり、対応する答えは `(list destination)` である。
3. 引数が異なるなら、アルゴリズムは origination のすべての直接の近傍を調べ、そのいずれかから destination へのパスがあるかを判定しなければならない。言い換えると、それらの近傍の1つを選ぶと、「パスを見つける」問題の新しいインスタンスが生成される。
4. 最後に、アルゴリズムが origination のある近傍から destination へのパスを得たなら、前者から後者への完全なパスを構成するのは簡単である——リストに origination ノードを加えればよい。

プログラミングの観点では、第3点が重要である。ノードは任意個の近傍を持ち得るので、「すべての近傍を調べる」仕事は単一の原始操作には複雑すぎる。ノードのリストを消費し、それぞれについて新しいパス問題を生成する補助関数が必要である。言い換えると、その関数は find-path のリスト向きの版である。

この補助関数を find-path/list と呼び、それに対する願望を定式化しよう：

```racket
; [List-of Node] Node Graph -> [Maybe Path]
; finds a path from some node on lo-originations to
; destination; otherwise, it produces #false
(define (find-path/list lo-originations destination G)
  #false)
```

この願望を使い、生成的再帰関数の一般的なテンプレートを埋めて find-path の最初の草案を得られる：

```racket
(define (find-path origination destination G)
  (cond
    [(symbol=? origination destination)
     (list destination)]
    [else
     (... origination...
...(find-path/list (neighbors origination G)
                         destination G)...)]))
```

これは練習問題471の neighbors と願望リストの関数 find-path/list を使い、それ以外は生成的再帰関数についての4つの問いへの答えを使っている。

設計過程の残りは、これらの関数を正しく合成する細部についてである。find-path/list のシグネチャを考えよ。find-path と同様、`[Maybe Path]` を生成する。すなわち、近傍のいずれかからパスを見つければそのパスを生成し、そうでなければ、どの近傍も destination につながっていないなら、関数は `#false` を生成する。したがって find-path の答えは find-path/list が生成する結果の種類に依存し、コードは cond 式で2つの可能な答えを区別しなければならない：

```racket
(define (find-path origination destination G)
  (cond
    [(symbol=? origination destination)
     (list destination)]
    [else
     (local ((define next (neighbors origination G))
             (define candidate
               (find-path/list next destination G)))
       (cond
         [(boolean? candidate)...]
         [(cons? candidate)...]))]))
```

2つの場合は、受け取り得る2種類の答え——Boolean またはリスト——を反映する。第1の場合、find-path/list はどの近傍から destination へのパスも見つけられず、find-path 自身もそのようなパスを構成できない。第2の場合、補助関数はパスを見つけたが、find-path はなおこのパスの先頭に origination を加えなければならない。candidate は origination の近傍の1つで始まり、上で合意したとおり origination 自身では始まらないからである。

> **図169: Finding a path in a graph**

```racket
; Node Node Graph -> [Maybe Path]
; finds a path from origination to destination in G
; if there is no path, the function produces #false
(define (find-path origination destination G)
  (cond
    [(symbol=? origination destination) (list destination)]
    [else (local ((define next (neighbors origination G))
                  (define candidate
                    (find-path/list next destination G)))
            (cond
              [(boolean? candidate) #false]
              [else (cons origination candidate)]))]))

; [List-of Node] Node Graph -> [Maybe Path]
; finds a path from some node on lo-Os to D
; if there is no path, the function produces #false
(define (find-path/list lo-Os D G)
  (cond
    [(empty? lo-Os) #false]
    [else (local ((define candidate
                    (find-path (first lo-Os) D G)))
            (cond
              [(boolean? candidate)
               (find-path/list (rest lo-Os) D G)]
              [else candidate]))]))
```


図169は find-path の完全な定義を含む。また find-path/list の定義も含む。これは第1引数を構造的再帰で処理する。リスト内の各ノードについて、find-path/list は find-path を使ってパスがあるかを調べる。find-path が実際にパスを生成すれば、それが答えである。そうでなければ、find-path/list はバックトラックする。

注 Trees は構造的な世界でのバックトラックを論じる。特によい例は、家系図の中で青目の祖先を探索する関数である。関数がノードに出会うと、まず家系図の一方の枝、たとえば父方を探索し、この探索が `#false` を生成するなら、もう一方を探索する。グラフは木を一般化するので、この関数を find-path と比較するのは有益な演習である。終わり

最後に、find-path がすべての可能な入力に対して答えを生成するかを調べる必要がある。図168のグラフと、このグラフ内の任意の2つのノードが与えられたとき、find-path が常に何らかの答えを生成することは比較的簡単に確認できる。やめ！ 先を読む前に次の練習問題を解け。

練習問題 472. 入力 `'A`、`'G`、および sample-graph について find-path のテストを開発せよ。

図168を見よ。関数はどのパスを見つけるか。なぜか。

test-on-all-nodes を設計せよ。この関数はグラフ g を消費し、すべてのノードの対のあいだにパスがあるかどうかを判定する。

> **図170: A directed graph with cycle**

> 原本は次の画像を含む（画像プレースホルダは図版パイプラインで埋め込み可）:
>
> [image: pict_229.png]


しかし他のグラフでは、find-path はあるノードの対について停止しないことがある。図170のグラフを考えよ。

やめ！ この図のグラフを表す cyclic-graph を定義せよ。

図168と比べると、この新しいグラフは C から B への辺が1本増えただけである。しかしこの一見小さな追加により、あるノードで探索を始めて同じノードに戻ることが可能になる。具体的には、B から E へ、C へ、そして B へ戻ることができる。実際、find-path を `'B`、`'D`、およびこのグラフに適用すると、手評価が確認するように停止に失敗する：

```racket
(find-path 'B 'D cyclic-graph)
==.. (find-path 'B 'D cyclic-graph)..
==.. (find-path/list (list 'E 'F) 'D cyclic-graph)..
==.. (find-path 'E 'D cyclic-graph)..
==.. (find-path/list (list 'C 'F) 'D cyclic-graph)..
==.. (find-path 'C 'D cyclic-graph)..
==.. (find-path/list (list 'B 'D) 'D cyclic-graph)..
==.. (find-path 'B 'D cyclic-graph)..
```

手評価は、find-path と find-path/list を7回適用したあと、ISL+ が開始時とまったく同じ式を評価しなければならないことを示す。同じ入力は任意の関数に対して同じ評価を引き起こすので、find-path はこれらの入力について停止しない。

> **注:** この規則の例外を1つだけ知っている。random である。

まとめると、停止性の議論は次のようになる。与えられたグラフに閉路がなければ、find-path は任意の入力に対して何らかの出力を生成する。結局のところ、どのパスも有限個のノードしか含まず、パスの数も有限である。したがって関数は、与えられたノードから始まるすべての解を網羅的に調べるか、起点から終点ノードへのパスを見つける。しかしグラフが閉路、すなわちあるノードから自分自身へのパスを含むなら、find-path はある入力について結果を生成しないことがある。

次の部は、まさにこの種の問題に対処するプログラム設計技法を提示する。特に、グラフ内の閉路に対処できる find-path の変種を提示する。

練習問題 473. 図170のグラフについて `'B`、`'C` に対して find-path をテストせよ。また練習問題472の test-on-all-nodes をこのグラフに使え。

練習問題 474. find-path プログラムを単一の関数として再設計せよ。

練習問題 475. find-path/list を再設計し、明示的な構造的再帰の代わりに図95と図96の既存のリスト抽象を使うようにせよ。ヒント Racket の ormap の文書を読め。ISL+ の ormap 関数とどう異なるか。前者はここで役立つか。

データ抽象についての注 find-path 関数が Graph の定義を知る必要がないことに気づいたかもしれない。Graph に対する正しい neighbors 関数を提供するかぎり、find-path は完全に正しく動く。要するに、find-path プログラムはデータ抽象を使う。

Abstraction が述べるとおり、データ抽象は関数抽象と同じように働く。ここで abstract-find-path という関数を作れ、それは find-path より1つ多いパラメータ、neighbors を消費する。常に abstract-find-path に Graph からのグラフ G と対応する neighbors 関数を渡せば、グラフを正しく処理する。余分なパラメータは従来の意味での抽象化を示唆するが、2つのパラメータ——G と neighbors——のあいだに要求される関係は、abstract-find-path が Graph の定義についても抽象化されていることを本当に意味する。後者はデータ定義なので、この考えはデータ抽象と呼ばれる。

プログラムが大きくなると、データ抽象はプログラムの構成要素を組み立てるための決定的な道具になる。*How to Design* シリーズの次の巻は、この考えを深く扱う。次の節は別の例でこの考えを説明する。終わり

練習問題 476. Finite State Machines は有限状態機械と文字列に関する問題を提示するが、解が生成的再帰を必要とするため、直ちに本章へ委ねる。あなたは今、その問題に取り組むために必要な設計知識を得た。

関数 fsm-match を設計せよ。有限状態機械のデータ表現と文字列を消費する。文字列中の文字の列が、有限状態機械を初期状態から最終状態へ遷移させるなら `#true` を生成する。

この問題は生成的再帰関数の設計についてなので、本質的なデータ定義とデータ例を提供する：

```racket
(define-struct transition [current key next])
(define-struct fsm [initial transitions final])

; An FSM is a structure:
;   (make-fsm FSM-State [List-of 1Transition] FSM-State)
; A 1Transition is a structure:
;   (make-transition FSM-State 1String FSM-State)
; An FSM-State is String.

; data example: see exercise 109

(define fsm-a-bc*-d
  (make-fsm
   "AA"
   (list (make-transition "AA" "a" "BC")
         (make-transition "BC" "b" "BC")
         (make-transition "BC" "c" "BC")
         (make-transition "BC" "d" "DD"))
   "DD"))
```

データ例は正規表現 `a (b|c)* d` に対応する。練習問題109で述べたように、"acbd"、"ad"、"abcd" は受理可能な文字列の例である。"da"、"aa"、"d" はマッチしない。

この文脈で、次の関数を設計している：

```racket
; FSM String -> Boolean
; does an-fsm recognize the given string
(define (fsm-match? an-fsm a-string)
  #false)
```

ヒント 必要な補助関数を fsm-match? 関数の局所に設計せよ。この文脈では、問題をパラメータの対として表せ。有限状態機械の現在状態と、残りの 1String のリストである。

> **図171: A definition of arrangements using generative recursion**

```racket
; [List-of X] -> [List-of [List-of X]]
; creates a list of all rearrangements of the items in w
(define (arrangements w)
  (cond
    [(empty? w) '(())]
    [else
      (foldr (lambda (item others)
               (local ((define without-item
                         (arrangements (remove item w)))
                       (define add-item-to-front
                         (map (lambda (a) (cons item a))
                              without-item)))
                 (append add-item-to-front others)))
        '()
        w)]))

; [List-of [List-of 1String]] -> Boolean
; are the words "rat", "art", and "tar" members of the given list?
(define (all-words-from-rat? w)
  (and (member (explode "rat") w)
       (member (explode "art") w)
       (member (explode "tar") w)))

(check-satisfied (arrangements '("r" "a" "t"))
                 all-words-from-rat?)
```


**練習問題 477. 図171の arrangements の関数定義を調べよ。この図は、Word Games, the Heart of the Problem が扱う拡張設計問題の生成的再帰による解を示している。すなわち**

> **注:** この練習問題を提案してくれた Mark Engelberg に感謝する。

> 語が与えられたとき、その文字の可能なすべての並べ替えを作れ。

拡張練習問題は、主関数と2つの補助関数の構造的再帰による設計への直接的な案内であり、後者の設計はさらに2つのヘルパー関数の作成を必要とする。対照的に、図171は生成的再帰——さらに foldr と map——の力を使い、同じプログラムを単一の関数定義として定義する。

arrangements の生成的再帰版の設計を説明せよ。生成的再帰の設計レシピが立てるすべての問いに答えよ。停止性の問いも含めて。

図171の arrangements は、Word Games, the Heart of the Problem の解と同じリストを作るか。

> **図172: A chess board with a single queen and the positions it threatens**

> 原本は次の画像を含む（画像プレースホルダは図版パイプラインで埋め込み可）:
>
> [image: pict_230.png]


### 29.2 プロジェクト：バックトラック（Project: Backtracking）

n クイーン・パズルはチェスの世界から来た有名な問題であり、バックトラックの適用可能性を自然な仕方で示す。ここでの目的では、チェス盤は n × n のマスの格子である。クイーンは、水平・垂直・斜め方向に、他の駒を「飛び越え」ずに任意の距離を動ける駒である。クイーンがあるマスを脅かすとは、そのマスにいるか、そこへ動けることをいう。図172はこの概念を図で示す。クイーンは第2列・第6行にある。クイーンから放射状に伸びる実線は、クイーンに脅かされるすべてのマスを通る。

> **注:** 本節の再定式化について Mark Engelberg に感謝する。

古典的なクイーン問題は、8 × 8 のチェス盤に8個のクイーンを、盤上のクイーン同士が互いに脅かさないように置くことである。計算機科学者は問題を一般化し、n × n のチェス盤に n 個のクイーンを、クイーン同士が互いに脅威とならないように置けるかどうかを問う。

n = 2 では、完全なパズルに明らかに解はない。4マスのいずれにクイーンを置いても、残りのすべてのマスを脅かす。

> **図173: Three queen configurations for a 3 by 3 chess board**

> 原本は次の画像を含む（画像プレースホルダは図版パイプラインで埋め込み可）:
>
> [image: pict_231.png]
>
> [image: pict_232.png]
>
> [image: pict_233.png]


n = 3 にも解はない。図173は2個のクイーンのすべての異なる配置、すなわち k = 3 かつ n = 2 の解を示す。各場合で、左のクイーンは左端の列のあるマスを占め、2番目のクイーンは1番目が脅かさない2マスの一方に置かれる。2番目のクイーンの配置は、残りの空いているすべてのマスを脅かす。つまり3番目のクイーンを置くことは不可能である。

練習問題 478. 最初のクイーンを最上行、最右列、最下行のすべてのマスにも置ける。これらの解がすべて図173に描かれた3つのシナリオと同じなのはなぜかを説明せよ。

残るは中央のマスである。3 × 3 盤の中央のマスに1つ置いたあと、2番目のクイーンさえ置くことは可能か。

> **図174: Solutions for the n queens puzzle for 4 by 4 and 5 by 5 boards**

> 原本は次の画像を含む（画像プレースホルダは図版パイプラインで埋め込み可）:
>
> [image: pict_234.png]
>
> [image: pict_235.png]


図174は n クイーン・パズルの2つの解を示す。左は n = 4、右は n = 5 である。図は、各場合で解が各行と各列に1つのクイーンを持つことを示す。これは理にかなっている。クイーンは自分のマスから放射する行全体と列全体を脅かすからである。

十分に詳細な分析を行ったので、解の段階へ進める。分析はいくつかの考えを示唆する：

1. 問題は一度に1つのクイーンを置くことである。盤にクイーンを置くとき、対応する行・列・対角線を他のクイーンには使えないものとして印を付けられる。
2. 別のクイーンについては、脅かされていない位置だけを考える。
3. この最初の位置の選択が後で問題を起こす場合に備え、このクイーンを置くのに実行可能な他のマスを覚えておく。
4. 盤にクイーンを置くよう求められているのに安全なマスが残っていないなら、あるマスを別のマスより選んだ過程の以前の地点までバックトラックし、残りのマスの1つを試す。

要するに、この解の過程は「パスを見つける」アルゴリズムに似ている。

過程の記述から設計されたアルゴリズムへ移るには、明らかに2つのデータ表現が必要である。チェス盤用と盤上の位置用である。後者から始めよう：

```racket
(define QUEENS 8)
; A QP is a structure:
;   (make-posn CI CI)
; A CI is an N in [0,QUEENS).
; interpretation (make-posn r c) denotes the square at
; the r-th row and c-th column
```

結局のところ、チェス盤が基本的にこの選択を決める。

CI の定義は `[0, QUEENS)` の代わりに `[1,QUEENS]` を使ってもよいが、2つの定義は基本的に等価であり、0から数え上げるのがプログラマのやり方である。同様に、チェス位置のいわゆる代数的記法は盤の一方の次元に `'a` から `'h` の文字を使うので、QP は CI とそうした文字を使ってもよかった。再び2つはおおむね等価であり、自然数なら ISL+ で多数の位置を作るのが文字より容易である。

練習問題 479. threatening? 関数を設計せよ。2つの QP を消費し、それぞれのマスに置かれたクイーンが互いに脅かすかどうかを判定する。

領域知識 (1) 図172を調べよ。この図のクイーンは、水平線・垂直線・対角線上のすべてのマスを脅かす。逆に、これらの線上の任意のマスにいるクイーンは、そのクイーンを脅かす。

(2) 洞察を、マスの座標同士を関係づける数学的条件に翻訳せよ。たとえば、水平線上のすべてのマスは同じ y 座標を持つ。同様に、一方の対角線上のすべてのマスは、和が同じ座標を持つ。それはどちらの対角線か。もう一方の対角線では、2つの座標の差が同じままである。この考えはどちらの対角線を記述するか。

ヒント 領域知識を把握したら、水平・垂直・対角線をカバーするテスト・スイートを定式化せよ。threatening? が `#false` を生成しなければならない引数を入れるのを忘れるな。

練習問題 480. render-queens を設計せよ。この関数は自然数 n、QP のリスト、および Image を消費する。与えられた QP に従って与えられた画像を置いた n × n のチェス盤の画像を生成する。

オンラインでチェスのクイーンの画像を探してもよいし、利用可能な画像関数で簡素なものを作ってもよい。

Board のデータ表現については、アルゴリズムが過程をどう実装するかを知るまでこのステップを先送りする。そうするのはデータ抽象のもう一つの演習である。実際、アルゴリズム本体のシグネチャを述べるのに Board のデータ定義さえ必要ない：

```racket
; N -> [Maybe [List-of QP]]
; finds a solution to the n queens problem

; data example: [List-of QP]
(define 4QUEEN-SOLUTION-2
  (list  (make-posn 0 2) (make-posn 1 0)
         (make-posn 2 3) (make-posn 3 1)))

(define (n-queens n)
  #false)
```

完全なパズルは、n × n のチェス盤に n 個のクイーンの配置を見つけることである。したがって明らかに、アルゴリズムは自然数以外を消費せず、n 個のクイーン配置の表現——解が存在するなら——を生成する。後者は QP のリストで表せるので、結果として

```racket
; [List-of QP] or #false
```

を選ぶ。当然、`#false` は解を見つけられなかったことを表す。

次のステップは例を開発し、テストとして定式化することである。n-queens は 2 または 3 が与えられたとき失敗しなければならないと分かっている。4 については、実際の盤と同一の4個のクイーンに対する解が2つある。図174は左にその1つを示し、もう1つはこれである：

> [image: pict_236.png]

しかしデータ表現の観点では、これら2つの画像を表す多くの異なる仕方がある。図175はその一部をスケッチする。残りを埋めよ。

> **図175: Solutions for the 4 queens puzzle**

```racket
; N -> [Maybe [List-of QP]]
; finds a solution to the n queens problem

(define 0-1 (make-posn 0 1))
(define 1-3 (make-posn 1 3))
(define 2-0 (make-posn 2 0))
(define 3-2 (make-posn 3 2))

(check-member-of
 (n-queens 4)
 (list 0-1 1-3 2-0 3-2)
 (list 0-1 1-3 3-2 2-0)
 (list 0-1 2-0 1-3 3-2)
 (list 0-1 2-0 3-2 1-3)
 (list 0-1 3-2 1-3 2-0)
 (list 0-1 3-2 2-0 1-3)
 ...
 (list 3-2 2-0 1-3 0-1))

(define (n-queens n)
  (place-queens (board0 n) n))
```


練習問題 481. 図175のテストはひどい。現実世界のプログラマが、これらの可能な結果をすべて書き出すことは決してない。

1つの解は、再び性質テストを使うことである。n-queens-solution? 関数を設計せよ。自然数 n を消費し、クイーン配置に対する述語を生成する。その述語は、与えられた配置が n クイーン・パズルの解かどうかを判定する：

- n クイーン・パズルの解は長さ n でなければならない。
- そのようなリスト上の QP は、他の相異なる QP を脅かすことがあってはならない。

この述語をテストしたら、それと check-satisfied を使い、n-queens のテストを定式化せよ。

代替の解は、QP のリストを集合として理解することである。2つのリストが異なる順序で同じ QP を含むなら、図が示唆するようにそれらは等価である。したがって n-queens のテストを次のように定式化できる：

```racket
; [List-of QP] -> Boolean
; is the result equal [as a set] to one of two lists
(define (is-queens-result? x)
  (or (set=? 4QUEEN-SOLUTION-1 x)
      (set=? 4QUEEN-SOLUTION-2 x)))
```

関数 set=? を設計せよ。2つのリストを消費し、順序にかかわらず同じ項目を含むかどうかを判定する。

**練習問題 482. 鍵となる考えは、すでにいくつかのクイーンを含んでいてもよいチェス盤に n 個のクイーンを置く関数を設計することである：**

```racket
; Board N -> [Maybe [List-of QP]]
; places n queens on board; otherwise, returns #false
(define (place-queens a-board n)
  #false)
```

図175はすでに n-queens の定義でこの関数を参照している。

place-queens アルゴリズムを設計せよ。Board を扱うために次の関数があると仮定せよ：

```racket
; N -> Board
; creates the initial n by n board
(define (board0 n)...)

; Board QP -> Board
; places a queen at qp on a-board
(define (add-queen a-board qp)
  a-board)

; Board -> [List-of QP]
; finds spots where it is still safe to place a queen
(define (find-open-spots a-board)
  '())
```

第1の関数は、図175で place-queens 用の初期盤表現を作るために使われる。他の2つは、アルゴリズムの生成的ステップを記述するのに必要になる。

前の練習問題の解が動くことをまだ確認できない。広範な願望リストに依存するからである。願望リスト上の3つの関数を支える Board のデータ表現を求める。これが残りの問題である。

**練習問題 483. Board のデータ定義を開発し、練習問題482で指定された3つの関数を設計せよ。次の考えを検討せよ：**

- Board は、クイーンをなお置ける位置を集める。
- Board は、クイーンが置かれた位置のリストを含む。
- Board は n × n のマスの格子であり、各マスはクイーンで占められているかもしれない。マスを表すのに3つのフィールドを持つ構造体を使え。x 用、y 用、およびマスが脅かされているかどうかを述べる第3のフィールドである。

上記の考えの1つを使ってこの練習問題を解け。

チャレンジ 3つの考えすべてを使い、Board の3つの異なるデータ表現を考え出せ。練習問題482の解を抽象化し、Board のどのデータ表現でも動くことを確認せよ。

## 30 まとめ（Summary）

本書のこの第V部は、プログラム設計に「eureka!（ひらめき）」という考えを導入する。最初の4部の構造的設計とは異なり、eureka! 設計は、プログラムが問題をどう解くべきか、あるいは問題を表すデータをどう処理すべきかについての考えから始まる。ここでの設計とは、与えられた問題に似ているがより単純な、新しい種類の問題に対して再帰関数を呼ぶ巧妙な方法を考え出すことを意味する。

心に留めておけ。私たちはこれを生成的再帰と呼んだが、大半の計算機科学者はこれらの関数をアルゴリズムと呼ぶ。

本書のこの部を終えたあと、生成的再帰の設計について次のことを理解しているはずだ：

1. 設計レシピの標準的な骨組みはそのまま有効である。
2. 大きな変更はコーディングのステップに関わる。生成的再帰の完全に一般的なテンプレートから完全な関数へ進む際の、4つの新しい問いを導入する。これらの問いのうち2つで、解の過程の「自明な」部分を仕上げ、他の2つで生成的な解のステップを仕上げる。
3. 小さな変更は、生成的再帰関数の停止挙動についてである。構造的に設計された関数とは異なり、アルゴリズムはある入力について停止しないことがある。この問題は、考えそのものに内在する限界や、考えのコードへの翻訳に起因し得る。いずれにせよ、プログラムの将来の読者は、潜在的に「悪い」入力についての警告を受けるに値する。

現実のプログラミング作業では、単純またはよく知られたアルゴリズムに出会い、対処することが期待される。真に巧妙なアルゴリズムについては、ソフトウェア企業は高給の専門家、領域の専門家、数学者を雇い、概念的な細部を仕上げてから、プログラマに概念をプログラムへ変えるよう求める。あなたもこの種の仕事に備えなければならず、最良の準備は練習である。

