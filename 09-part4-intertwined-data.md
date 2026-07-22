<!-- Extracted from original_html/part_four.html -->
<!-- Canonical English source for Japanese translation -->

## IV 絡み合ったデータ（Intertwined Data）

### 目次（Contents）

- 19 S式の詩学（The Poetry of S-expressions）
- 19.1 木（Trees）
- 19.2 森（Forests）
- 19.3 S式（S-expressions）
- 19.4 絡み合ったデータでの設計（Designing with Intertwined Data）
- 19.5 プロジェクト：BST（Project: BSTs）
- 19.6 関数の単純化（Simplifying Functions）
- 20 反復的洗練（Iterative Refinement）
- 20.1 データ分析（Data Analysis）
- 20.2 データ定義の洗練（Refining Data Definitions）
- 20.3 関数の洗練（Refining Functions）
- 21 インタプリタの洗練（Refining Interpreters）
- 21.1 式の解釈（Interpreting Expressions）
- 21.2 変数の解釈（Interpreting Variables）
- 21.3 関数の解釈（Interpreting Functions）
- 21.4 すべてを解釈する（Interpreting Everything）
- 22 プロジェクト：XMLの商取引（Project: The Commerce of XML）
- 22.1 S式としてのXML（XML as S-expressions）
- 22.2 XML列挙の描画（Rendering XML Enumerations）
- 22.3 ドメイン特化言語（Domain-Specific Languages）
- 22.4 XMLの読み取り（Reading XML）
- 23 同時処理（Simultaneous Processing）
- 23.1 2つのリストを同時に処理する：場合1（Processing Two Lists Simultaneously: Case 1）
- 23.2 2つのリストを同時に処理する：場合2（Processing Two Lists Simultaneously: Case 2）
- 23.3 2つのリストを同時に処理する：場合3（Processing Two Lists Simultaneously: Case 3）
- 23.4 関数の単純化（Function Simplification）
- 23.5 2つの複雑な入力を消費する関数の設計（Designing Functions that Consume Two Complex Inputs）
- 23.6 指の体操：2つの入力（Finger Exercises: Two Inputs）
- 23.7 プロジェクト：データベース（Project: Database）
- 24 まとめ（Summary）

リストや自然数のためのデータ定義は、かなり変わったものだと思うかもしれない。これらのデータ定義は自分自身を参照しており、おそらくあなたが初めて出会った、そうした定義だろう。実際のところ、多くのデータのクラスは、これら2つよりもさらに複雑なデータ定義を必要とする。よくある一般化には、1つのデータ定義の中に多数の自己参照があるものや、互いに参照し合う一連のデータ定義がある。こうした形のデータはどこにでも現れるようになっており、したがってプログラマは任意のデータの定義の集まりに対処できるよう学ぶことが極めて重要である。そしてそれこそが、設計レシピのすべてが目指していることである。

この部は、設計レシピを一般化し、構造的なデータ定義のあらゆる形に対して機能するようにするところから始まる。次に、Projects: Lists から得た反復的洗練（iterative refinement）の概念を、厳密な基盤の上で導入する。なぜなら、複雑なデータ定義は一挙にできあがるのではなく、いくつかの段階を経て発展するからである。実際、反復的洗練を用いることは、すべてのプログラマが小さな科学者である理由の1つであり、私たちの学問がアメリカ名に「科学（science）」という言葉を使う理由でもある。最後の2つの章でこれらの考え方を例示する。1つは BSL のインタプリタの設計方法を説明し、もう1つは Web のためのデータ交換言語である XML の処理についてである。最後の章は設計レシピをさらに1度拡張し、同時に2つの複雑な引数を処理する関数向けに書き換える。

## 19 S式の詩 (The Poetry of S-expressions)

プログラミングは詩に似ている。詩人と同じく、プログラマは一見すると無意味な考えの上で技能を磨く。前章で述べたように、彼らは常に改訂と編集を繰り返す。本章は、ますます複雑なデータの形を導入する——一見すると現実世界の目的がないかのように。動機付けの背景を示す場合でも、選ばれたデータの種類は極端なまでに純粋であり、再び出会うことはまずないだろう。

それでも本章は、設計レシピの十分な力を示し、現実世界のプログラムが扱う種類のデータを紹介する。この題材をプログラマとしての人生で出会うものと結びつけるため、各節に適切な名前——木、森、XML——を付けた。最後のひとつは少し誤解を招く。実際には S式についてだからだ。S式と XML の関係は「プロジェクト: XML の商業」で明らかになる。そこでは本章と対照的に、複雑なデータの現実的な使い方にはるかに近づく。

### 19.1 木 (Trees)

誰もが家系図を持つ。家系図の描き方のひとつは、子どもが生まれるたびに要素を追加し、父親と母親の要素を結ぶことである。両親が不明な人については、結ぶ線はない。結果は祖先家系図になる。なぜなら、任意の人を与えると、その木は既知の祖先すべてを指すからである。

> **図111: A family tree**

> 原本は次の画像を含む（画像プレースホルダは図版パイプラインで埋め込み可）:
>
> [image: pict_140.png]


図111は3層の家系図を示す。Gustav は Eva と Fred の子であり、Eva は Carl と Bettina の子である。名前と家族関係に加え、木は生年と目の色も記録している。このスケッチに基づけば、何世代もさかのぼる家系図や、他の種類の情報を記録する家系図を容易に想像できる。

家系図が大きくなると、それをデータとして表現し、この種のデータを処理するプログラムを設計するのが理にかなってくる。家系図の一点は5つの情報——父親、母親、名前、生年月日、目の色——を組み合わせるので、構造体型を定義すべきである。

```racket
(define-struct child [father mother name date eyes])
```

この構造体型定義は、次のようなデータ定義を求める。

```racket
; A Child is a structure:
;   (make-child Child Child String N String)
```

このデータ定義は素直に見えるが、実は役に立たない。自分自身を参照しているが、節がひとつしかないため、適切な Child のインスタンスを作る方法がない。おおざっぱに言えば、次のように書くことになってしまう。

```racket
(make-child (make-child (make-child...)...)...)
```

終わりなく続く。このような無意味なデータ定義を避けるため、自己参照するデータ定義には複数の節があり、そのうち少なくともひとつはデータ定義へ戻って参照しないことを要求する。

データ定義は少し後回しにし、代わりに実験しよう。既存の家系図に子どもを追加しようとしており、両親の表現はすでに持っているとしよう。その場合、新しい child 構造体を単に構築できる。例えば、プログラムがすでに Carl と Bettina を表現しているとき、Adam を表すには次の child 構造体を追加すれば十分である。

```racket
(define Adam
  (make-child Carl Bettina "Adam" 1950 "hazel"))
```

ここで Carl と Bettina は Adam の両親の表現を指すとする。

一方で、図111の家系図における Bettina のように、両親が不明な場合もある。それでも、child 表現の対応する親のフィールドを埋めなければならない。どんなデータを選んでも、情報の欠如を合図しなければならない。一方では、既存の値のプールから `#false`、`"none"`、または `'()` を使える。他方では、家系図から情報が欠けていると本当に言うべきである。この目的は、適切な名前を持つ構造体型を導入するのが最もよい。

```racket
(define-struct no-parent [])
```

さて、Bettina 用の child 構造体を構築するには、次のように言う。

```racket
(make-child (make-no-parent)
            (make-no-parent)
            "Bettina" 1926 "green")
```

もちろん、情報がひとつだけ欠けているなら、そのフィールドだけにこの特別な値を入れる。

この実験から2つの洞察が得られる。第一に、求めているのは child 構造体のインスタンスの生成方法を記述するデータ定義ではなく、家系図の表現方法を記述するデータ定義である。第二に、データ定義は2つの節から成り、ひとつは未知の家系図を記述する変種、もうひとつは既知の家系図である。

```racket
(define-struct no-parent [])
(define-struct child [father mother name date eyes])
; An FT (short for family tree) is one of:
; – (make-no-parent)
; – (make-child FT FT String N String)
```

「親なし」の木はプログラムに何度も現れるので、略記として NP を定義し、データ定義を少し改訂する。

```racket
(define NP (make-no-parent))
; An FT is one of:
; – NP
; – (make-child FT FT String N String)
```

「自己参照データ定義を用いた設計」の設計レシピに従い、データ定義を使って家系図の例を作る。具体的には、図111の家系図をデータ表現に翻訳する。Carl の情報はデータへ簡単に翻訳できる。

```racket
(make-child NP NP "Carl" 1926 "green")
```

Bettina と Fred も同様の child のインスタンスで表される。Adam の場合は入れ子の children が必要で、ひとつは Carl、ひとつは Bettina 用である。

```racket
(make-child (make-child NP NP "Carl" 1926 "green")
            (make-child NP NP "Bettina" 1926 "green")
            "Adam"
            1950
            "hazel")
```

Carl と Bettina のレコードは Dave と Eva のレコードの構築にも必要なので、特定の child のインスタンスに名前を付ける定義を導入し、他の場所では変数名を使う方がよい。図112は、図111の家系図の完全なデータ表現に対するこのアプローチを示す。よく見てほしい。この木は、次の設計演習の実行例として用いる。

> **図112: A data representation of the sample family tree**

```racket
; Oldest Generation:
(define Carl (make-child NP NP "Carl" 1926 "green"))
(define Bettina (make-child NP NP "Bettina" 1926 "green"))

; Middle Generation:
(define Adam (make-child Carl Bettina "Adam" 1950 "hazel"))
(define Dave (make-child Carl Bettina "Dave" 1955 "black"))
(define Eva (make-child Carl Bettina "Eva" 1965 "blue"))
(define Fred (make-child NP NP "Fred" 1966 "pink"))

; Youngest Generation:
(define Gustav (make-child Fred Eva "Gustav" 1988 "brown"))
```


家系図に対する具体的な関数を設計する代わりに、まずそのような関数の一般的な構成を見よう。つまり、具体的な課題を念頭に置かずに、設計レシピを可能な限り進めよう。ヘッダ材料、すなわちレシピのステップ2から始める。

```racket
; FT ->???
;...
(define (fun-FT an-ftree)...)
```

関数の目的は述べていないが、家系図を消費すること、そしてこの形のデータが主入力であることは分かっている。シグネチャの「???」は、関数がどんな種類のデータを生成するか分からないことを示し、「...」は目的が分からないことを思い出させる。

目的がないので機能例は作れない。それでも、FT のデータ定義の構成を利用してテンプレートを設計できる。2つの節からなるので、テンプレートは2節の cond 式でなければならない。

```racket
(define (fun-FT an-ftree)
  (cond
    [(no-parent? an-ftree)...]
    [else...]))
```

fun-FT への引数が no-parent? を満たす場合、構造体には追加データがないので、第1節は完成である。第2節では、入力は5つのデータ片を含む。テンプレートでは5つのセレクタでそれを示す。

```racket
; FT ->???
(define (fun-FT an-ftree)
  (cond
    [(no-parent? an-ftree)...]
    [else (... (child-father an-ftree)...
... (child-mother an-ftree)...
... (child-name an-ftree)...
... (child-date an-ftree)...
... (child-eyes an-ftree)...)]))
```

テンプレートへの最後の追加は自己参照に関する。データ定義が自分自身を参照するなら、関数は再帰しやすく、テンプレートは示唆的な自然再帰でそれを示す。FT の定義には2つの自己参照があり、したがってテンプレートにも2つのそのような再帰が必要である。

```racket
; FT ->???
(define (fun-FT an-ftree)
  (cond
    [(no-parent? an-ftree)...]
    [else (... (fun-FT (child-father an-ftree))...
... (fun-FT (child-mother an-ftree))...
... (child-name an-ftree)...
... (child-date an-ftree)...
... (child-eyes an-ftree)...)]))
```

具体的には、データ定義の第2節に対応する自己参照があるので、第2の cond 節で fun-FT が父親と母親のデータ表現に適用される。

ここで具体例、blue-eyed-child? 関数に移ろう。その目的は、与えられた家系図の中に目が青の child 構造体があるかどうかを判定することである。fun-FT をコピー・貼り付け・改名してテンプレートを得てよい。「???」を Boolean に置き換え、目的文を加える。

```racket
; FT -> Boolean
; does an-ftree contain a child
; structure with "blue" in the eyes field
(define (blue-eyed-child? an-ftree)
  (cond
    [(no-parent? an-ftree)...]
    [else (... (blue-eyed-child?
                 (child-father an-ftree))...
... (blue-eyed-child?
                 (child-mother an-ftree))...
... (child-name an-ftree)...
... (child-date an-ftree)...
... (child-eyes an-ftree)...)]))
```

このやり方では、テンプレートの一般的な名前を具体的な名前に置き換えなければならない。

レシピを確認すると、定義ステップに進む前にバックトラックして例をいくつか開発する必要があることに気づく。家系図の最初の人物 Carl から始めると、Carl の家系図には目の色が `"blue"` の child が含まれないことが分かる。具体的には、Carl を表す child は目の色が `"green"` だと言い、Carl の祖先の木は空なので、それらに `"blue"` の目を持つ child が含まれるはずがない。

```racket
(check-expect (blue-eyed-child? Carl) #false)
```

対照的に、Gustav には青目の Eva のための child が含まれる。

```racket
(check-expect (blue-eyed-child? Gustav) #true)
```

これで実際の関数を定義する準備ができた。関数は2つの場合を区別する。no-parent と child である。第1の場合、例を作っていなくても答えは明らかであるはずだ。与えられた家系図には child がまったく含まれないので、目の色が `"blue"` の child も含み得ない。したがって第1の cond 節の結果は `#false` である。

第2の cond 節については、設計にはずっと多くの作業が要る。再び設計レシピに従い、まずテンプレート内の式が何を達成するかを思い起こす。

1. 関数の目的文によれば、`(blue-eyed-child? (child-father an-ftree))` は父親の FT の中のどこかの child が `"blue"` の目を持つかどうかを判定する。
2. 同様に、`(blue-eyed-child? (child-mother an-ftree))` は母親の FT の誰かが青目かどうかを判定する。
3. セレクタ式 `(child-name an-ftree)`、`(child-date an-ftree)`、`(child-eyes an-ftree)` は、与えられた child 構造体からそれぞれ名前、生年月日、目の色を取り出す。

あとはこれらの式をどう組み合わせるかを考えればよい。

明らかに、child 構造体の eyes フィールドに `"blue"` が含まれるなら、関数の答えは `#true` である。次に、名前と生年月日に関する式は無用であり、残るのは再帰呼び出しである。述べた通り、`(blue-eyed-child? (child-father an-ftree))` は父親側の木を辿り、母親側の家系図は `(blue-eyed-child? (child-mother an-ftree))` で処理される。これらの式のいずれかが `#true` を返せば、an-ftree には `"blue"` の目を持つ child が含まれる。

この分析は、次の3つの式のうちひとつが `#true` なら結果が `#true` であるべきだと示唆する。

- `(string=? (child-eyes an-ftree) "blue")`
- `(blue-eyed-child? (child-father an-ftree))`
- `(blue-eyed-child? (child-mother an-ftree))`

したがって、これらの式を or で組み合わせる必要がある。

```racket
(or (string=? (child-eyes an-ftree) "blue")
    (blue-eyed-child? (child-father an-ftree))
    (blue-eyed-child? (child-mother an-ftree)))
```

図113はすべてをひとつの定義にまとめる。

> **図113: Finding a blue-eyed child in an ancestor tree**

```racket
; FT -> Boolean
; does an-ftree contain a child
; structure with "blue" in the eyes field

(check-expect (blue-eyed-child? Carl) #false)
(check-expect (blue-eyed-child? Gustav) #true)

(define (blue-eyed-child? an-ftree)
  (cond
    [(no-parent? an-ftree) #false]
    [else (or (string=? (child-eyes an-ftree) "blue")
              (blue-eyed-child? (child-father an-ftree))
              (blue-eyed-child? (child-mother an-ftree)))]))
```


この関数は2つの再帰を使う最初の関数なので、`(blue-eyed-child? Carl)` についてステッパの動作をシミュレートし、全体がどう動くかの印象を与える。

```racket
(blue-eyed-child? Carl)
==
(blue-eyed-child?
  (make-child NP NP "Carl" 1926 "green"))
```

NP が値であるかのように扱い、child のインスタンスの略記として carl を使おう。

```racket
==
(cond
  [(no-parent?
     (make-child NP NP "Carl" 1926 "green"))
   #false]
  [else (or (string=? (child-eyes carl) "blue")
            (blue-eyed-child? (child-father carl))
            (blue-eyed-child? (child-mother carl)))])
```

最初の cond 行を落としたあと、carl をその値に置き換え、図114の3つの補助計算を行う時である。これらを使って等しいものを等しいもので置き換えると、残りの計算は容易に説明できる。

```racket
==
(or (string=? "green" "blue")
    (blue-eyed-child? (child-father carl))
    (blue-eyed-child? (child-mother carl)))
== (or #false #false #false)
== #false
```

数学の授業でこのような補助計算を見たことがあると信じているが、ステッパはこのような計算は行わないことも理解する必要がある。代わりに、絶対に必要な計算だけを実行する。

> **図114: Calculating with trees**

```racket
; (1)
(child-eyes (make-child NP NP "Carl" 1926 "green"))
==
"green"

; (2)
(blue-eyed-child?
  (child-father
    (make-child NP NP "Carl" 1926 "green")))
==
(blue-eyed-child? NP)
==
#false

; (3)
(blue-eyed-child?
  (child-mother
    (make-child NP NP "Carl" 1926 "green")))
==
(blue-eyed-child? NP)
==
#false
```


**練習問題 310.** count-persons を開発せよ。この関数は家系図を消費し、木の中の child 構造体を数える。

**練習問題 311.** 関数 average-age を開発せよ。家系図と現在の年を消費する。家系図内のすべての child 構造体の平均年齢を生成する。

**練習問題 312.** 関数 eye-colors を開発せよ。家系図を消費し、木の中のすべての目の色のリストを生成する。結果のリストでは同じ目の色が複数回現れてもよい。
**ヒント** 再帰呼び出しから得られるリストをつなぐには append を使え。

**練習問題 313.** 関数 blue-eyed-ancestor? が必要だとしよう。これは blue-eyed-child? に似ているが、与えられた child 自身ではなく、真の祖先が青目のときだけ `#true` と答える。

目標は明らかに異なるが、シグネチャは同じである。

```racket
; FT -> Boolean
(define (blue-eyed-ancestor? an-ftree)...)
```

ストップ！ この関数の目的文を定式化せよ。

違いを理解するため、Eva を見てみよう。

```racket
(check-expect (blue-eyed-child? Eva) #true)
```

Eva は青目だが、青目の祖先はいない。したがって、

```racket
(check-expect (blue-eyed-ancestor? Eva) #false)
```

対照的に、Gustav は Eva の息子であり、青目の祖先がいる。

```racket
(check-expect (blue-eyed-ancestor? Gustav) #true)
```

さて、友人が次の解を持ってきたとしよう。

```racket
(define (blue-eyed-ancestor? an-ftree)
  (cond
    [(no-parent? an-ftree) #false]
    [else
     (or
       (blue-eyed-ancestor?
         (child-father an-ftree))
       (blue-eyed-ancestor?
         (child-mother an-ftree)))]))
```

この関数がテストのひとつに失敗する理由を説明せよ。どの A を選んでも `(blue-eyed-ancestor? A)` の結果は何か。友人の解を直せるか。

**変数名と構造体名についての注** 家族関係の最初の議論は、構造体型定義の名前として child を示唆する。5つの情報は特定の両親の子どもを表す。しかし残りの展開は祖先の木についてのものである。図113のような関数定義だけに焦点を当てて章を流し読みすると、child-father、child-mother、child-eyes という名前は少し誤解を招くかもしれない。主に、関数の再帰的な性質と衝突するように見えるからである。経験のある開発者なら、おそらく DrRacket の改名機能を使って child を person に置き換えるだろう。一般に、変数の命名は、コードの読者がその背後の思考を理解するのを助けるうえで重要である。

> **注:** Check syntax を実行する。構造体の名前を右クリックする。rename を選ぶ。

### 19.2 森 (Forests)

家系図から家系の森へは短い一歩である。

```racket
; An FF (short for family forest) is one of:
; – '()
; – (cons FT FF)
; interpretation a family forest represents several
; families (say, a town) and their ancestor trees
```

図111からの木の抜粋を森として並べた例を示す。

```racket
(define ff1 (list Carl Bettina))
(define ff2 (list Fred Eva))
(define ff3 (list Fred Eva Carl))
```

最初の2つの森は互いに無関係な2つの家族を含み、3つ目は、現実の森と違って家系の森の中の木は重なり得ること示している。

さて、家系図に関するこの代表的な問題を考えよう。

> **サンプル問題** 関数 blue-eyed-child-in-forest? を設計せよ。家系の森に eyes フィールドが `"blue"` の child が含まれるかどうかを判定する。

> **図115: Finding a blue-eyed child in a family forest**

```racket
; FF -> Boolean
; does the forest contain any child with "blue" eyes

(check-expect (blue-eyed-child-in-forest? ff1) #false)
(check-expect (blue-eyed-child-in-forest? ff2) #true)
(check-expect (blue-eyed-child-in-forest? ff3) #true)

(define (blue-eyed-child-in-forest? a-forest)
  (cond
    [(empty? a-forest) #false]
    [else
     (or (blue-eyed-child? (first a-forest))
         (blue-eyed-child-in-forest? (rest a-forest)))]))
```


素直な解は図115に示されている。シグネチャ、目的文、例は自分で調べよ。ここではプログラムの構成に焦点を当てる。テンプレートについては、関数がリストを消費するので、リストのテンプレートを用いてよい。リストの各項目が eyes フィールドだけを持つ構造体なら、関数は eyes フィールドのセレクタ関数と文字列比較を使ってそれらの構造体を反復するだろう。この場合、各項目は家系図であるが、幸い家系図の処理方法はすでに知っている。

一歩下がって、図115をどう説明したかを点検しよう。出発点は、第2が第1を参照し、両方が自分自身を参照する一対のデータ定義である。結果は、第2が第1を参照し、両方が自分自身を参照する一対の関数である。言い換えると、関数定義はデータ定義が互いに参照し合うのと同じ仕方で互いに参照し合う。初期の章はこの種の関係を流していたが、いま状況は十分に複雑であり、注意を払う価値がある。

**練習問題 314.** FF のデータ定義を List-of 抽象を使って再定式化せよ。次に blue-eyed-child-in-forest? 関数についても同様にせよ。最後に、前章のリスト抽象のひとつを使って blue-eyed-child-in-forest? を定義せよ。

**練習問題 315.** 関数 average-age を設計せよ。家系の森と年 (N) を消費する。このデータから、森の中のすべての child インスタンスの平均年齢を生成する。
**注** この森の中の木が重なっていると、結果は真の平均ではない。一部の人が他の人より多く寄与するからである。この練習問題では、木は重ならないかのように扱え。

### 19.3 S式 (S-expressions)

Intermezzo 2: Quote, Unquote が非形式的に S式を導入した一方で、3つのデータ定義の組み合わせでそれらを記述することもできる。

> An S-expr is one of:
> – Atom
> – SL
>
> An SL is one of:
> – `'()`
> – `(cons S-expr SL)`
>
> An Atom is one of:
> – Number
> – String
> – Symbol

シンボルは、先頭にシングルクオートがあり、末尾にクオートのない文字列のように見えることを思い出そう。

S式の考えは John McCarthy とその Lisp 集団による。彼らは1958年に、Lisp プログラムを他の Lisp プログラムで処理できるように S式を作った。この一見循環した推論は難解に聞こえるかもしれないが、Intermezzo 2: Quote, Unquote で述べたように、S式は多用途なデータの形であり、しばしば再発見され、最近では World Wide Web への応用がある。したがって S式を扱うことは、高度に絡み合ったデータ定義向けの関数設計の議論の準備になる。

**練習問題 316.** atom? 関数を定義せよ。

本書のこの時点まで、S式のような複雑なデータ定義を要するデータはなかった。それでも、追加のヒントがひとつあれば、設計レシピに従えば S式を処理する関数を設計できる。この点を示すため、具体例を進めよう。

> **サンプル問題** 関数 count を設計せよ。ある S式の中に、あるシンボルが何回現れるかを求める。

第1ステップはデータ定義を求め、すでに完了したように見えるが、定義が複雑なときはデータ例の作成も求めることを思い出そう。

データ定義はデータの作り方の処方であるべきで、その「テスト」は使えるかどうかである。S-expr のデータ定義が述べる一点は、すべての Atom が S-expr の要素だということであり、Atom が作りやすいことは分かっている。

```racket
'hello
20.12
"world"
```

同様に、すべての SL はリストであり、かつ S-expr でもある。

```racket
'()
(cons 'hello (cons 20.12 (cons "world" '())))
(cons (cons 'hello (cons 20.12 (cons "world" '())))
      '())
```

最初の2つは明白である。3つ目はもう一度見る価値がある。2番目の S-expr を繰り返し、それを `(cons ... '())` の内側に入れ子にしている。つまり、2番目の例という単一の項目を含むリストである。list を使えば例を単純化できる。

```racket
(list (cons 'hello (cons 20.12 (cons "world" '()))))
; or
(list (list 'hello 20.12 "world"))
```

実際、Intermezzo 2: Quote, Unquote の quotation 機構を使えば、S式を書くのはさらに容易である。最後の3つは次の通り。

```racket
> '()
'()
> '(hello 20.12 "world")
(list 'hello #i20.12 "world")
> '((hello 20.12 "world"))
(list (list 'hello #i20.12 "world"))
```

助けとして、これらの例を DrRacket の対話領域で評価した。結果は quote 記法よりも上記の構築に近いことが分かる。

quote を使えば、複雑な例を作るのはかなり容易である。

```racket
> '(define (f x)     (+ x 55))
(list 'define (list 'f 'x) (list '+ 'x 55))
```

この例は BSL の定義のように見えるので奇妙に感じるかもしれないが、DrRacket との対話が示すように、それは単なるデータの断片である。もうひとつ。

```racket
> '((6 f)    (5 e)    (4 d))
(list (list 6 'f) (list 5 'e) (list 4 'd))
```

このデータ片は表のように見え、文字を数と対応づけている。最後の例は芸術作品である。

```racket
> '(wing (wing body wing) wing)
(list 'wing (list 'wing 'body 'wing) 'wing)
```

これで count のきわめて明白なヘッダを書く時である。

```racket
; S-expr Symbol -> N
; counts all occurrences of sy in sexp
(define (count sexp sy)
  0)
```

ヘッダは明白なので、機能例に進む。与えられた S-expr が `'world` で、数えるべきシンボルが `'world` なら、答えは明らかに1である。さらにいくつかの例を、すぐにテストとして定式化する。

```racket
(check-expect (count 'world 'hello) 0)
(check-expect (count '(world hello) 'hello) 1)
(check-expect (count '(((world) hello) hello) 'hello) 2)
```

テストケースでは quotation 記法がどれほど便利か分かる。しかしテンプレートについては、quote で考えるのは破滅的である。

テンプレートのステップに進む前に、設計レシピの次の一般化に備えよう。

> **ヒント**
> 絡み合ったデータ定義については、データ定義ごとに1つのテンプレートを作れ。それらを並行して作れ。データ定義が互いに参照するのと同じ仕方で、テンプレートが互いに参照することを確かめよ。終わり

このヒントは聞こえるほど複雑ではない。この問題では、3つのテンプレートが必要である。

1. count 用。S-expr 内のシンボルの出現を数える。
2. SL 内のシンボルの出現を数える関数用。
3. Atom 内のシンボルの出現を数える関数用。

そして、3つのデータ定義が示唆する条件分岐を持つ、3つの部分的テンプレートである。

> ```
> (define (count sexp sy)
>   (cond
>     [(atom? sexp)...]
>     [else...]))
> (define (count-sl sl sy)
>   (cond
>     [(empty? sl)...]
>     [else...]))
> (define (count-atom at sy)
>   (cond
>     [(number? at)...]
>     [(string? at)...]
>     [(symbol? at)...]))
> ```

count のテンプレートは2分岐の条件式を含む。S-expr のデータ定義が2節だからである。Atom の場合と SL の場合を区別するのに atom? 関数を使う。count-sl と名づけたテンプレートは SL の要素とシンボルを消費し、SL は基本的にリストなので、count-sl も2分岐の cond を含む。最後に、count-atom は Atom と Symbol の両方に対して働くことになっている。つまりそのテンプレートは、Atom のデータ定義で述べられた3つの異なるデータ形を検査する。

次のステップは、関連する節で複合データを分解することである。

> ```
> (define (count sexp sy)
>   (cond
>     [(atom? sexp)...]
>     [else...]))
> (define (count-sl sl sy)
>   (cond
>     [(empty? sl)...]
>     [else (... (first sl)...
>                ... (rest sl))]))
> (define (count-atom at sy)
>   (cond
>     [(number? at)...]
>     [(string? at)...]
>     [(symbol? at)...]))
> ```

なぜ count-sl にセレクタ式を2つだけ加えるのか。

テンプレート作成過程の最後のステップは、データ定義中の自己参照の点検を求める。我々の文脈では、これは自己参照と、あるデータ定義から別のデータ定義への参照（そして場合によっては戻る参照）を意味する。3つのテンプレートの cond 行を点検しよう。

1. count の atom? 行は S-expr の定義の第1行に対応する。ここから Atom への相互参照を示すため、`(count-atom sexp sy)` を加える。つまり sexp を Atom として解釈し、適切な関数に処理を任せる。
2. 同じ思考の流れに従い、count の第2の cond 行は `(count-sl sexp sy)` の追加を求める。
3. count-sl の empty? 行は、他のデータ定義を参照しないデータ定義の行に対応する。
4. 対照的に、else 行は2つのセレクタ式を含み、それぞれ異なる種類の値を取り出す。具体的には、`(first sl)` は S-expr の要素であり、`(count ...)` で包む。結局のところ、count は任意の S-expr の内部を数える責任を持つ。次に、`(rest sl)` は自己参照に対応し、再帰的関数呼び出しで扱う必要があることが分かっている。
5. 最後に、Atom の3つの場合はすべてアトミックな形のデータを参照する。したがって count-atom 関数は変更する必要がない。

> **図116: A template for S-expressions**
> 左右対比（崩れた ASCII 枠を二重 fence に復元。コードは公式 HTML の RktBlk より）。

**左**

```racket
(define (count sexp sy)
 (cond
   [(atom? sexp)
    (count-atom sexp sy)]
   [else
    (count-sl sexp sy)]))

(define (count-sl sl sy)
  (cond
    [(empty? sl) ...]
    [else
     (...
      (count (first sl) sy)
      ...
      (count-sl (rest sl) sy)
      ...)]))
```

**右**

```racket
(define (count-atom at sy)
  (cond
    [(number? at) ...]
    [(string? at) ...]
    [(symbol? at) ...]))
```


> **図117: A program for S-expressions**

```racket
; S-expr Symbol -> N
; counts all occurrences of sy in sexp
(define (count sexp sy)
 (cond
   [(atom? sexp) (count-atom sexp sy)]
   [else (count-sl sexp sy)]))

; SL Symbol -> N
; counts all occurrences of sy in sl
(define (count-sl sl sy)
  (cond
    [(empty? sl) 0]
    [else
     (+ (count (first sl) sy) (count-sl (rest sl) sy))]))

; Atom Symbol -> N
; counts all occurrences of sy in at
(define (count-atom at sy)
  (cond
    [(number? at) 0]
    [(string? at) 0]
    [(symbol? at) (if (symbol=? at sy) 1 0)]))
```


図116は3つの完全なテンプレートを示す。これらのテンプレートの空白を埋めるのは素直であり、図117が示す通りである。3つの定義の任意の行を説明できるはずである。例えば、

```racket
[(atom? sexp) (count-atom sexp sy)]
```

は sexp が Atom かどうかを判定し、そうなら count-atom 経由で S-expr を Atom として解釈する。

```racket
[else
 (+ (count (first sl) sy) (count-sl (rest sl) sy))]
```

は、与えられたリストが2つの部分——S-expr と SL——からなることを意味する。count と count-sl を使うことで、各部分に sy が何回現れるかを数える対応する関数が使われ、2つの数を足し合わせて——sexp 全体における sy の総数を得る。

```racket
[(symbol? at) (if (symbol=? at sy) 1 0)]
```

は、Atom が Symbol なら、それが sexp と等しければ sy は1回現れ、そうでなければまったく現れないことを教える。2つのデータ片はアトミックなので、他の可能性はない。

**練習問題 317.** 3つの接続された関数からなるプログラムは、この関係を local 式で表現すべきである。

図117のプログラムをコピーし、local を使って単一の関数に再構成せよ。改訂したコードを count のテストスイートで検証せよ。

local 関数への第2引数 sy は決して変わらない。常に元のシンボルと同じである。したがって local 関数定義からそれを削除し、走査過程全体を通じて sy が定数であることを読者に伝えてよい。

**練習問題 318.** depth を設計せよ。この関数は S式を消費し、その深さを求める。Atom の深さは1である。S式のリストの深さは、その項目の最大の深さに1を加えたものである。

**練習問題 319.** substitute を設計せよ。S式 s と2つのシンボル old と new を消費する。結果は s と同じだが、old のすべての出現が new に置き換えられている。

**練習問題 320.** データ定義から関数設計へのステップを、S-expr の定義への2つの変更で練習せよ。

第1ステップでは、S-expr のデータ定義を再定式化し、第1データ定義の第1節を Atom の3節へ展開し、第2データ定義は List-of 抽象を使うようにせよ。このデータ定義に対して count 関数を再設計せよ。

第2ステップでは、SL のデータ定義を S-expr のものに統合せよ。count を再び単純化せよ。**ヒント** lambda を使え。

**練習問題 321.** S-expr と SL のデータ定義を抽象化し、現れ得る Atom の種類を抽象するようにせよ。

### 19.4 絡み合ったデータを用いた設計 (Designing with Intertwined Data)

自己参照データ定義から、相互参照を持つデータ定義の集まりへの飛躍は、有限データ向けのデータ定義から自己参照データ定義への飛躍よりはるかに小さい。実際、自己参照データ定義向けの設計レシピ——「自己参照データ定義を用いた設計」を見よ——は、この一見複雑な状況に適用するためにわずかな調整だけでよい。

1. 「巣」のような相互に関連するデータ定義の必要性は、自己参照データ定義の必要性と似ている。問題文は多くの異なる種類の情報を扱い、ある形の情報が他の種類を参照する。そのような状況で先へ進む前に、参照と定義をつなぐ矢印を描け。図118の左側を考えよ。S-expr の定義を示し、SL と Atom への参照がそれぞれの定義へ矢印で結ばれている。同様に、SL の定義は1つの自己参照と S-expr へ戻る1つの参照を含み、再び適切な矢印で結ばれている。自己参照データ定義と同様、これらの定義の巣も妥当性確認を求める。最低限、個々の定義ごとにいくつかの例を構築できなければならない。巣の中の他のデータ定義を参照しない節から始めよ。それらから例を生成できないなら、定義は無効かもしれないことを心に留めよ。
2. 鍵となる変更は、データ定義の数だけ関数を並行して設計しなければならないことである。各関数はデータ定義のひとつに特化し、残りの引数はすべて同じままである。それに基づき、各関数についてシグネチャ、目的文、ダミー定義から始める。
3. データ定義の巣の中のすべての相互参照を使う機能例を必ず通して考えよ。
4. 各関数について、その主データ定義に従ってテンプレートを設計せよ。テンプレート作成の最後のステップまで図52に導いてもらえ。改訂された最後のステップは、すべての自己参照と相互参照の検査を求める。矢印で注記したデータ定義を使ってこのステップを導け。データ定義の各矢印について、テンプレートに矢印を含めよ。テンプレートの矢印注記版は図118の右側を見よ。

   [image: pict_141.png] [image: pict_142.png]

   **図118: データ定義とテンプレートの巣のための矢印 (Arrows for nests of data definitions and templates)**

   次に矢印を実際の関数呼び出しに置き換えよ。経験を積めば、矢印を描くステップを自然に飛ばし、関数呼び出しを直接使うようになる。

   **注** 両方の巣——データ定義の巣と関数テンプレートの巣——が4本の矢印を含むことに注意し、矢印の対が互いに対応することにも注意せよ。研究者はこの対応を対称性と呼ぶ。これは設計レシピが問題から解へ至る自然な道を提供する証拠である。
5. 本体の設計では、自然再帰や他の関数への呼び出しを含まない cond 行から始める。これらは基本ケースと呼ばれる。対応する答えは通常、定式化が容易か、すでに例として与えられている。そのあと、自己参照のケースと相互関数呼び出しのケースを扱う。図53の問答に導いてもらえ。
6. すべての定義が完成したらテストを実行せよ。補助関数が壊れていると、主関数と欠陥のある補助定義の2つのエラー報告が得られるかもしれない。一度の修正で両方とも消えるはずである。テストの実行が関数のすべての部分をカバーすることを必ず確かめよ。

最後に、ステップ5で行き詰まったら、結合関数を推測するための表に基づくアプローチを思い出そう。絡み合ったデータの場合、場合ごとの表だけでなく、場合ごと・関数ごとの表が、組み合わせを考えるために必要かもしれない。

### 19.5 プロジェクト: 二分探索木 (Project: BSTs)

プログラマはしばしば、関数の性能を改善するためにデータの木表現を扱う。特によく知られた木の形が二分探索木である。情報をすばやく格納し取り出す良い方法だからである。

具体的に、人についての情報を管理する二分木を議論しよう。家系図の child 構造体の代わりに、二分木はノードを含む。

```racket
(define-struct no-info [])
(define NONE (make-no-info))

(define-struct node [ssn name left right])
; A BT (short for BinaryTree) is one of:
; – NONE
; – (make-node Number Symbol BT BT)
```

対応するデータ定義は家系図のものに似ており、NONE が情報の欠如を示し、各ノードが社会保障番号、名前、および他の2つの二分木を記録する。後者は家系図の両親に似ているが、ノードとその左・右の木の関係は家族関係に基づかない。

次に2つの二分木がある。

> `(make-node 15 'd NONE (make-node 24 'i NONE NONE))`
>
> `(make-node 15 'd (make-node 87 'h NONE NONE) NONE)`

図119は、そのような木を図としてどう考えるべきかを示す。木は上下逆に描かれ、根が上、樹冠が下にある。各円はノードに対応し、対応する node 構造体の ssn フィールドでラベル付けされている。図は NONE を省略している。

> **図119: A binary search tree and a binary tree**

> 原本は次の画像を含む（画像プレースホルダは図版パイプラインで埋め込み可）:
>
> [image: pict_143.png]
>
> [image: pict_144.png]


**練習問題 322.** 上記の2つの木を図119の様式で描け。次に contains-bt? を設計せよ。与えられた数が与えられた BT に現れるかどうかを判定する。

**練習問題 323.** search-bt を設計せよ。この関数は数 n と BT を消費する。木が ssn フィールドが n である node 構造体を含むなら、関数はそのノードの name フィールドの値を生成する。そうでなければ、関数は `#false` を生成する。

**ヒント** まず contains-bt? で木全体を検査するか、各段階で自然再帰の結果を boolean? で検査することを検討せよ。

図119の2つの木の数を左から右へ読むと、2つの異なる列が得られる。

> tree A: 10 15 24 29 63 77 89 95 99
>
> tree B: 87 15 24 29 63 33 89 95 99

tree A の列は昇順に整列しており、B のものはそうではない。第1の種類の二分木は二分探索木である。すべての二分探索木は二分木だが、すべての二分木が二分探索木であるわけではない。より具体的には、二分探索木と二分木を区別する条件——すなわちデータ不変条件——を定式化する。

**BST 不変条件**

> BST（binary search tree の略）は、次の条件に従う BT である。
>
> - NONE は常に BST である。
> - `(make-node ssn0 name0 L R)` は、次のとき BST である。
>   - L が BST であり、
>   - R が BST であり、
>   - L 内のすべての ssn フィールドが ssn0 より小さく、
>   - R 内のすべての ssn フィールドが ssn0 より大きい。

言い換えると、BT が BST にも属するかどうかを検査するには、すべての部分木のすべての数を調べ、それらがある与えられた数より小さいか大きいかを確かめなければならない。これはデータ構築に追加の負担を課すが、次の練習問題が示すように、その価値は十分にある。

**練習問題 324.** 関数 inorder を設計せよ。二分木を消費し、木の図を見たときの左から右への現れ方に従って、木の中のすべての ssn 番号の列を生成する。

**ヒント** append を使え。リストを次のように連結する。

```racket
(append (list 1 2 3) (list 4) (list 5 6 7))
==
(list 1 2 3 4 5 6 7)
```

二分探索木に対して inorder は何を生成するか。

BST の中で与えられた ssn を持つノードを探すときは、BST 不変条件を利用してよい。BT が特定の ssn を持つノードを含むかどうかを知るには、関数は木のすべてのノードを見る必要があるかもしれない。対照的に、二分探索木が同じ ssn を含むかどうかを知るには、検査する各ノードについて2つの部分木の一方を捨ててよい。

このサンプル BST で考えを説明しよう。

```racket
(make-node 66 'a L R)
```

66 を探しているなら、探しているノードを見つけたことになる。さて、より小さい数、例えば63を探しているなら、探索を L に絞れる。ssn フィールドが66より小さいすべてのノードは L にあるからである。同様に、99を探すなら、L を無視して R に焦点を当てる。ssn が66より大きいすべてのノードは R にあるからである。

**練習問題 325.** search-bst を設計せよ。この関数は数 n と BST を消費する。木が ssn フィールドが n であるノードを含むなら、関数はそのノードの name フィールドの値を生成する。そうでなければ、関数は NONE を生成する。関数の構成は BST 不変条件を利用し、必要最小限の比較だけを行うようにしなければならない。

整列リストでの探索については練習問題189を見よ。比較せよ！

二分木を構築するのは容易である。二分探索木を構築するのは複雑である。任意の2つの BT、数、名前を与えられれば、正しい順序で make-node をこれらの値に適用するだけでよく、できあがり——新しい BT が得られる。同じ手続きは BST では失敗する。結果は通常 BST にならないからである。例えば、一方の BST が正しい順序で ssn フィールド3と5を持つノードを含み、他方が ssn フィールド2と6を含むなら、2つの木を別の社会保障番号と名前で単に組み合わせても BST にはならない。

残りの2つの練習問題は、数と名前のリストから BST を構築する方法を説明する。具体的には、第1の練習問題は、与えられた ssn0 と name0 を BST に挿入する関数を求める。つまり、与えられたものと同じ BST を生成するが、ある NONE 部分木の代わりに ssn0、name0、および NONE 部分木を含むノード構造体が挿入されている。第2の練習問題は、数と名前の完全なリストを扱える関数を求める。

**練習問題 326.** 関数 create-bst を設計せよ。BST B、数 N、シンボル S を消費する。B とちょうど同じで、ある NONE 部分木の代わりに次のノード構造体を含む BST を生成する。

```racket
(make-node N S NONE NONE)
```

設計が完了したら、図119の tree A に対してこの関数を使え。

**練習問題 327.** 関数 create-bst-from-list を設計せよ。数と名前のリストを消費し、create-bst を繰り返し適用して BST を生成する。シグネチャは次の通り。

```racket
; [List-of [List Number Symbol]] -> BST
```

完成した関数を使い、次のサンプル入力から BST を作れ。

```racket
'((99 o)
  (77 l)
  (24 i)
  (10 h)
  (95 g)
  (15 d)
  (89 c)
  (29 b)
  (63 a))
```

構造的設計レシピに従えば、結果は図119の tree A である。既存の抽象を使うと、この木が得られるかもしれないが、「反転した」木が得られるかもしれない。なぜか。

### 19.6 関数の単純化 (Simplifying Functions)

練習問題317は、絡み合った形のデータを扱う関数を整理するために local をどう使うかを示す。この整理は、データ定義が最終形だと分かったあとに関数を単純化するのにも役立つ。この点を示すため、練習問題319の解をどう単純化するかを説明する。

> **図120: A program to be simplified**

```racket
; S-expr Symbol Atom -> S-expr
; replaces all occurrences of old in sexp with new

(check-expect (substitute '(((world) bye) bye) 'bye '42)
              '(((world) 42) 42))

(define (substitute sexp old new)
  (local (; S-expr -> S-expr
          (define (for-sexp sexp)
            (cond
              [(atom? sexp) (for-atom sexp)]
              [else (for-sl sexp)]))
          ; SL -> S-expr
          (define (for-sl sl)
            (cond
              [(empty? sl) '()]
              [else (cons (for-sexp (first sl))
                          (for-sl (rest sl)))]))
          ; Atom -> S-expr
          (define (for-atom at)
            (cond
              [(number? at) at]
              [(string? at) at]
              [(symbol? at) (if (equal? at old) new at)])))
    (for-sexp sexp)))
```


図120は substitute 関数の完全な定義を示す。定義はデータ定義が示唆する通り、local と3つの補助関数を使う。下で提案する各編集のあとで関数を再テストできるよう、図はテストケースを含む。ストップ！ 追加のテストケースを開発せよ。1つではほとんど十分ではない。

**練習問題 328.** 図120を DrRacket にコピー＆ペーストし、テストスイートを含めよ。テストスイートを検証せよ。本節の残りを読み進めるあいだ、編集を行い、テストスイートを再実行して我々の議論の妥当性を確認せよ。

> **図121: Program simplification, step 1**

```racket
(define (substitute sexp old new)
  (local (; S-expr -> S-expr
          (define (for-sexp sexp)
            (cond
              [(atom? sexp) (for-atom sexp)]
              [else (for-sl sexp)]))
          ; SL -> S-expr
          (define (for-sl sl)
            (map for-sexp sl))
          ; Atom -> S-expr
          (define (for-atom at)
            (cond
              [(number? at) at]
              [(string? at) at]
              [(symbol? at) (if (equal? at old) new at)])))
    (for-sexp sexp)))
```


SL が S-expr のリストを記述することが分かっているので、for-sl を単純化するのに map を使える。結果は図121を見よ。元のプログラムは for-sexp が sl 上のすべての項目に適用されると述べるが、改訂された定義は同じ考えを map でより簡潔に表現する。

第2の単純化ステップでは、equal? が任意の2つの値を比較することを思い出してもらう必要がある。これを念頭に置くと、第3の local 関数は1行になる。図122がこの第2の単純化を示す。

> **図122: Program simplification, steps 2 and 3**

```racket
(define (substitute sexp old new)
  (local (; S-expr -> S-expr
          (define (for-sexp sexp)
            (cond
              [(atom? sexp) (for-atom sexp)]
              [else (for-sl sexp)]))
          ; SL -> S-expr
          (define (for-sl sl) (map for-sexp sl))
          ; Atom -> S-expr
          (define (for-atom at)
            (if (equal? at old) new at)))
    (for-sexp sexp)))

(define (substitute.v3 sexp old new)
  (local (; S-expr -> S-expr
          (define (for-sexp sexp)
            (cond
              [(atom? sexp)
               (if (equal? sexp old) new sexp)]
              [else
               (map for-sexp sexp)])))
    (for-sexp sexp)))
```


この時点で、最後の2つの local 定義はそれぞれ1行からなる。さらに、どちらの定義も再帰的ではない。したがって for-sexp の中に関数をインライン化できる。インライン化とは、`(for-atom sexp)` を `(if (equal? sexp old) new sexp)` に置き換えることを意味する。つまりパラメータ at を実際の引数 sexp に置き換える。同様に、`(for-sl sexp)` については `(map for-sexp sexp)` を入れる。図121の下半分を見よ。残るのは、1つの local 関数を導入し、同じ主引数に対してそれを呼び出す関数定義だけである。他の2つの引数を体系的に供給したとすれば、局所的に定義された関数を外側の関数の代わりに使えることが直ちに分かるだろう。

> **注:** sexp もパラメータだが、この置換は本当に許容できる。それも実際の値の代わりをしているからである。

この最後の考えをコードに翻訳した結果は次の通り。

```racket
(define (substitute sexp old new)
  (cond
    [(atom? sexp) (if (equal? sexp old) new sexp)]
    [else
     (map (lambda (s) (substitute s old new)) sexp)]))
```

ストップ！ この最後の単純化で lambda を使わなければならなかった理由を説明せよ。

## 20 反復的洗練（Iterative Refinement）

現実世界のプログラムを開発するとき、複雑な形の情報に直面し、それをデータで表現するという問題にぶつかることがある。この課題に取り組む最善の戦略は、よく知られた科学的プロセスである反復的洗練を使うことである。科学者の課題は、何らかの形の数学を用いて現実世界の一部を表現することである。その努力の結果はモデルと呼ばれる。科学者は次に、そのモデルをさまざまな方法で検証する。とりわけ、実験の結果を予測することによってである。予測と測定の食い違いが大きすぎる場合は、予測を改善することを目標としてモデルを洗練する。この反復的なプロセスは、予測が十分に正確になるまで続く。

ロケットの飛行経路を予測したい物理学者を考えてみよう。「ロケットを点として」表す表現は単純だが、たとえば空気摩擦を考慮しないなど、かなり不正確でもある。それに応じて、物理学者はロケットの大まかな外形を加え、摩擦を表すのに必要な数学を導入するかもしれない。この第2のモデルは、第1のモデルの洗練である。一般に、科学者はこのプロセスを——プログラマの言い方では反復して——繰り返し、モデルがロケットの飛行経路を十分に正確に予測するまで続ける。

コンピュータ科学科で訓練を受けたプログラマは、この物理学者のように進めるべきである。鍵は、現実世界の情報の正確なデータ表現と、それらを適切に処理する関数を見つけることである。複雑な状況では、十分なデータ表現と適切な関数にたどり着くために洗練のプロセスが必要になる。プロセスは情報の本質的な部分から始まり、必要に応じて他のものを加えていく。ときには、プログラムが配備されたあとに、利用者が追加の機能を求めるために、プログラマがモデルを洗練しなければならないこともある。

ここまで私たちは、複雑な形のデータに関しては、あなたに代わって反復的洗練を使ってきた。本章は、コンピュータのファイルシステム（の一部）の表現と処理という拡張された例を通して、プログラム開発の原則としての反復的洗練を示す。まずファイルシステムについての簡潔な議論から始め、それから3つのデータ表現を反復的に開発する。その途中で、設計レシピが既存のプログラムの修正にもどう役立つかが見えるよう、いくつかのプログラミング練習問題を提案する。

### 20.1 データ分析（Data Analysis）

DrRacket を終了する前に、作業がすべてどこかに安全にしまってあることを確かめたい。そうしなければ、次に DrRacket を起動したときに、すべてを再入力しなければならなくなる。そこで、プログラムとデータをファイルに保存するようコンピュータに依頼する。ファイルは大まかに言えば文字列である。

> **注:** ファイルは実際にはバイトの列であり、1つずつ並んでいる。ファイルのクラスを定義してみよ。

> **図123: A sample directory tree**

> 原本は次の画像を含む（画像プレースホルダは図版パイプラインで埋め込み可）:
>
> [image: pict_145.png]


ほとんどのコンピュータシステムでは、ファイルはディレクトリあるいはフォルダに整理されている。大まかに言えば、ディレクトリはいくつかのファイルと、さらにいくつかのディレクトリを含む。後者はサブディレクトリと呼ばれ、さらにサブディレクトリとファイルを含むことがある。この階層のために、ディレクトリ木と呼ぶ。

図123は小さなディレクトリ木の図解スケッチを含み、その絵はなぜコンピュータ科学者がそれを木と呼ぶかを説明している。コンピュータ科学での慣例に反して、図は木が上向きに成長する様子を示しており、ルートディレクトリの名前は `TS` である。ルートディレクトリは1つのファイル `read!` と、2つのサブディレクトリ `Text` と `Libs` を含む。最初のサブディレクトリ `Text` は3つのファイルだけを含み、後者の `Libs` は2つのサブディレクトリだけを含み、そのそれぞれが少なくとも1つのファイルを含む。最後に、各箱には2種類の注釈のどちらかがある。ディレクトリには `DIR`、ファイルには数（そのサイズ）が付けられている。

練習問題 329. ディレクトリ木 `TS` の中で、ファイル名 `read!` は何回現れるか。ルートディレクトリからその出現へのパスを記述できるか。木の中のすべてのファイルの合計サイズは何か。各ディレクトリノードのサイズを1としたとき、木の合計サイズは何か。何レベルのディレクトリを含むか。

### 20.2 データ定義の洗練（Refining Data Definitions）

練習問題329は、利用者がディレクトリについて日常的に尋ねる質問のいくつかを列挙している。そうした質問に答えるために、コンピュータのオペレーティングシステムはそれらに答えられるプログラムを提供する。そのようなプログラムを設計したいなら、ディレクトリ木のデータ表現を開発する必要がある。

本節では、反復的洗練を使って、そのようなデータ表現を3つ開発する。各段階で、どの属性を含め、どれを無視するかを決めなければならない。図123のディレクトリ木を考え、それがどう作られるかを想像してみよ。利用者が最初にディレクトリを作るとき、それは空である。時間が経つにつれて、利用者はファイルとディレクトリを追加する。一般に、利用者はファイルを名前で参照するが、ディレクトリは主に入れ物として考える。

モデル1 私たちの思考実験は、最初のモデルは、ファイルを名前を持つ原子的な実体として、ディレクトリを入れ物として扱うことに焦点を当てるべきだと示唆する。ここに、ディレクトリをリストとして、ファイルを文字列——すなわちその名前——として扱うデータ定義がある。

```racket
; A Dir.v1 (short for directory) is one of:
; – '()
; – (cons File.v1 Dir.v1)
; – (cons Dir.v1 Dir.v1)

; A File.v1 is a String.
```

名前には、将来の洗練と区別するための .v1 接尾辞が付いている。

練習問題 330. 図123のディレクトリ木を、モデル1に従ったデータ表現に翻訳せよ。

練習問題 331. 与えられた Dir.v1 がいくつのファイルを含むかを判定する関数 how-many を設計せよ。設計レシピに従うことを忘れずに。練習問題330がデータ例を提供する。

モデル2 練習問題331を解いたなら、この最初のデータ定義がまだかなり単純であることを知っている。しかし、それはディレクトリの本質も曖昧にしている。この最初の表現では、与えられたディレクトリのサブディレクトリの名前をすべて列挙することはできないだろう。ディレクトリを単なる入れ物よりも忠実にモデル化するには、名前と入れ物を組み合わせる構造体型を導入しなければならない。

```racket
(define-struct dir [name content])
```

この新しい構造体型は、次のデータ定義の改訂を示唆する。

```racket
; A Dir.v2 is a structure:
;   (make-dir String LOFD)

; An LOFD (short for list of files and directories) is one of:
; – '()
; – (cons File.v2 LOFD)
; – (cons Dir.v2 LOFD)

; A File.v2 is a String.
```

Dir.v2 のデータ定義が LOFD の定義を参照し、LOFD の定義が Dir.v2 の定義を参照し返すことに注意せよ。2つの定義は相互再帰的である。

練習問題 332. 図123のディレクトリ木を、モデル2に従ったデータ表現に翻訳せよ。

練習問題 333. 与えられた Dir.v2 がいくつのファイルを含むかを判定する関数 how-many を設計せよ。練習問題332がデータ例を提供する。結果を練習問題331のものと比較せよ。

練習問題 334. ディレクトリにさらに2つの属性——size と readability——を装備する方法を示せ。前者は、ディレクトリ自体（内容ではなく）がどれだけの空間を消費するかを測る。後者は、利用者以外の誰かがディレクトリの内容を閲覧してよいかどうかを指定する。

モデル3 ディレクトリと同様に、ファイルにも属性がある。これらを導入するには、上と同じように進める。まず、ファイル用の構造体を定義する。

```racket
(define-struct file [name size content])
```

次に、データ定義を与える。

```racket
; A File.v3 is a structure:
;   (make-file String N String)
```

フィールド名が示すように、文字列はファイルの名前を、自然数はそのサイズを、文字列はその内容を表す。

最後に、ディレクトリの content フィールドを2つの部分——ファイルのリストとサブディレクトリのリスト——に分けよう。この変更は、構造体型定義の改訂を要求する。

```racket
(define-struct dir.v3 [name dirs files])
```

ここに洗練されたデータ定義がある。

```racket
; A Dir.v3 is a structure:
;   (make-dir.v3 String Dir* File*)

; A Dir* is one of:
; – '()
; – (cons Dir.v3 Dir*)

; A File* is one of:
; – '()
; – (cons File.v3 File*)
```

コンピュータ科学での慣例に従い、名前の末尾に * を使うことは「多数」を示唆し、似た名前——File.v3 と Dir.v3——から区別する印である。

練習問題 335. 図123のディレクトリ木を、モデル3に従ったデータ表現に翻訳せよ。ファイルの内容には "" を使え。

練習問題 336. 与えられた Dir.v3 がいくつのファイルを含むかを判定する関数 how-many を設計せよ。練習問題335がデータ例を提供する。結果を練習問題333のものと比較せよ。

データ定義の複雑さを考えると、誰がどうやって正しい関数を設計できるのかを熟考せよ。how-many が正しい結果を生成することに自信があるのはなぜか。

練習問題 337. List-of を使ってデータ定義 Dir.v3 を単純化せよ。それから ISL+ の図95と図96のリスト処理関数を使って、練習問題336の解の関数定義を単純化せよ。

第1モデルの単純な表現から始め、ステップごとに洗練していくことで、ディレクトリ木について十分に正確なデータ表現を開発してきた。実際、この第3のデータ表現は、最初の2つよりもはるかに忠実にディレクトリ木の本質を捉えている。このモデルに基づいて、コンピュータのオペレーティングシステムが利用者から期待される他の多くの関数を作ることができる。

### 20.3 関数の洗練（Refining Functions）

次の練習問題をいくらか現実的にするために、DrRacket には本書の初版からの dir.rkt ティーチパックが付属している。このティーチパックはモデル3の2つの構造体型定義を導入するが、.v3 接尾辞は付けない。さらに、ティーチパックはコンピュータ上のディレクトリ木の表現を作る関数を提供する。

> **注:** 定義領域に ( require htdp/dir ) を追加せよ。

```racket
; String -> Dir.v3
; creates a representation of the a-path directory
(define (create-dir a-path)...)
```

たとえば、DrRacket を開き、定義領域に次の3行を入力するとする。

```racket
(define O (create-dir "/Users/...")); on OS X
(define L (create-dir "/var/log/")); on Linux
(define W (create-dir "C:\\Users\\...")); on Windows
```

プログラムを保存して実行したあと、コンピュータ上のディレクトリのデータ表現が得られる。実際、create-dir を使ってコンピュータ上のファイルシステム全体を Dir.v3 のインスタンスに写像することもできる。

警告 (1) 大きなディレクトリ木では、DrRacket が表現を構築するのに多くの時間を要するかもしれない。まず小さなディレクトリ木で create-dir を使え。(2) 自分で dir 構造体型を定義してはならない。ティーチパックがすでにそれらを定義しており、構造体型を2度定義してはならない。

create-dir が届けるのはディレクトリ木の表現だけだが、そのレベルでプログラムを設計するとはどのようなことかを感じるには十分に現実的である。次の練習問題はこの点を示す。これらはディレクトリ木のデータ表現という一般的な考えを指すために Dir を使う。それぞれの練習問題を完了できる、最も単純な Dir のデータ定義を使え。練習問題337のデータ定義と、図95と図96の関数を自由に使ってよい。

練習問題 338. create-dir を使って、自分のディレクトリのいくつかを ISL+ のデータ表現に変えよ。それから練習問題336の how-many を使って、それらがいくつのファイルを含むかを数えよ。これらのディレクトリについて how-many が正しい結果を生成することに自信があるのはなぜか。

練習問題 339. find? を設計せよ。この関数は Dir とファイル名を消費し、この名前のファイルがディレクトリ木に現れるかどうかを判定する。

練習問題 340. 与えられた Dir の中のすべてのファイルとディレクトリの名前を列挙する関数 ls を設計せよ。

練習問題 341. Dir を消費し、ディレクトリ木全体のすべてのファイルの合計サイズを計算する関数 du を設計せよ。Dir 構造体にディレクトリを格納するコストはファイル記憶単位で1であると仮定せよ。現実世界では、ディレクトリは基本的に特別なファイルであり、そのサイズは関連するディレクトリがどれだけ大きいかに依存する。

残りの練習問題はパスの概念に依存する。私たちの目的では、パスは名前のリストである。

```racket
; A Path is [List-of String].
; interpretation directions into a directory tree
```

図123をもう一度見てみよ。その図では、`TS` から `part1` へのパスは (list"TS""Text""part1") である。同様に、`TS` から `Code` へのパスは (list"TS""Libs""Code") である。

練習問題 342. find を設計せよ。この関数はディレクトリ d とファイル名 f を消費する。(find?df) が #true なら、find は名前 f のファイルへのパスを生成する。そうでなければ #false を生成する。

ヒント ファイル名がディレクトリ木に現れるかどうかをまず調べたくなるが、すべてのサブディレクトリについてそうしなければならなくなる。したがって、find? と find の機能を組み合わせる方がよい。

チャレンジ find 関数は、図123の中の `read!` という名前の2つのファイルのうち1つだけを発見する。find を一般化し、d の中で f に至るすべてのパスのリストを生成する find-all を設計せよ。(find?df) が #false のとき、find-all は何を生成すべきか。この部分は、基本問題と比べて本当にチャレンジだろうか。

練習問題 343. 与えられた Dir に含まれるすべてのファイルへのパスを列挙する関数 ls-R を設計せよ。

練習問題 344. 練習問題343の ls-R を使って、練習問題342の find-all を再設計せよ。これは合成による設計であり、練習問題342のチャレンジ部分を解いたなら、新しい関数はディレクトリも見つけられる。

## 21 インタープリタの洗練（Refining Interpreters）

DrRacket はプログラムである。それは多くの異なる種類のデータを扱う複雑なプログラムである。ほとんどの複雑なプログラムと同様に、DrRacket も多くの関数から成る。プログラマがテキストを編集できるようにする関数、相互作用領域のように振る舞う関数、定義と式が「文法的」かどうかを検査する関数、などである。

本章では、相互作用領域の中核を実装する関数をどう設計するかを示す。当然ながら、この設計プロジェクトには反復的洗練を使う。実際、DrRacket のこの側面に焦点を当てるという考え自体も、洗練のもう1つの例である。すなわち、機能の1つだけを実装するという明らかなものである。

簡単に言えば、相互作用領域は、入力した式の値を求める仕事を行う。*RUN* をクリックしたあと、相互作用領域はすべての定義について知っている。その後、これらの定義を参照してもよい式を受け付け、その式の値を求め、このサイクルを望むだけ繰り返す準備ができている。このため、多くの人は相互作用領域を read-eval-print ループとも呼ぶ。ここで eval は評価器（evaluator）の略であり、インタープリタとも呼ばれる関数である。

本書と同様に、私たちの洗練プロセスは数値の BSL 式から始まる。それらは単純で、定義の理解を前提とせず、5年生の妹でもその値を求められる。この最初のステップを理解すれば、BSL 式とその表現の違いがわかる。次に変数を含む式に進む。最後のステップは定義を追加することである。

### 21.1 式の解釈（Interpreting Expressions）

最初の課題は、BSL プログラムのデータ表現について合意することである。つまり、BSL 式を BSL データの1片としてどう表すかを明らかにしなければならない。最初は奇妙で普通でないように聞こえるが、難しくはない。とりあえず数、加算、乗算だけを表現したいとしよう。明らかに、数は数を表せる。しかし加算式は複合データを要求する。2つの式を含み、乗算式と区別されるからである。乗算式もまたデータ表現を必要とする。

「構造の追加（Adding Structure）」に従い、加算と乗算を表現する素直な方法は、それぞれ2つのフィールドを持つ2つの構造体型を定義することである。

```racket
(define-struct add [left right])
(define-struct mul [left right])
```

意図は、left フィールドが一方のオペランド——演算子の「左」にあるもの——を含み、right フィールドがもう一方のオペランドを含むことである。次の表は3つの例を示す。

> BSL expression representation of BSL expression3 3(+ 1 1) (make-add 1 1)(* 300001 100000) (make-mul 300001 100000)

次の問題は、部分式を持つ式についてである。

```racket
(+ (* 3 3) (* 4 4))
```

驚くほど単純な答えは、フィールドは任意の値を含んでよい、ということである。この特定の場合、left と right は式の表現を含んでよく、望みの深さまで入れ子にしてもよい。追加の例は図124を見よ。

> **図124: Representing BSL expressions in BSL**
> 左右対比（崩れた ASCII 枠を二重 fence に復元。コードは公式 HTML の RktBlk より）。

**左**

```racket
(+ (* 3 3)
   (* 4 4))
```

**右**

```racket
(make-add (make-mul 3 3)
          (make-mul 4 4))
```

**ブロック3**

```racket
(+ (* (+ 1 2) 3)
   (* (* (+ 1 1)
         2)
      4))
```

**ブロック4**

```racket
(make-add (make-mul (make-add 1 2) 3)
          (make-mul (make-mul
                       (make-add 1 1)
                       2)
                    4))
```


練習問題 345. add と mul の構造体型定義に基づき、BSL 式の表現のためのデータ定義を定式化せよ。新しいデータのクラスには、S-expr との類推で BSL-expr を使おう。

次の式をデータに翻訳せよ。

1. (+10-10)
2. (+(*203)33)
3. (+(*3.14(*23))(*3.14(*-1-9)))

次のデータを式として解釈せよ。

1. (make-add-12)
2. (make-add(make-mul-2-3)33)
  > **注:** ここでの「解釈する」は「データから情報へ翻訳する」という意味である。対照的に、本章のタイトルの「インタープリタ」は、プログラムの表現を消費しその値を生成するプログラムを指す。2つの考えは関連しているが、同じものではない。
3. (make-mul(make-add1(make-mul23))3.14)

> **注:** ここでの「解釈する」は「データから情報へ翻訳する」という意味である。対照的に、本章のタイトルの「インタープリタ」は、プログラムの表現を消費しその値を生成するプログラムを指す。2つの考えは関連しているが、同じものではない。

BSL プログラムのデータ表現ができたので、評価器を設計する時である。この関数は BSL 式の表現を消費し、その値を生成する。再び、この関数はこれまで設計したどの関数とも異なり、例で実験する価値がある。このために、算術の規則を使って式の値を求めてもよいし、DrRacket の相互作用領域で「遊んで」もよい。例についての次の表を見てみよ。

> BSL expression its representation its value3 3 3(+ 1 1) (make-add 1 1) 2(* 3 10) (make-mul 3 10) 30(+ (* 1 1) 10) (make-add (make-mul 1 1) 10) 11

練習問題 346. BSL 式の表現が評価され得る値のクラスのためのデータ定義を定式化せよ。

練習問題 347. eval-expression を設計せよ。この関数は BSL 式の表現を消費し、その値を計算する。

練習問題 348. #true、#false、and、or、not から構成されるブール BSL 式のためのデータ表現を開発せよ。それから eval-bool-expression を設計せよ。これは（表現としての）ブール BSL 式を消費し、その値を計算する。これらのブール式はどのような種類の値を生成するか。

便宜と構文解析 S式は、私たちのプログラミング言語で BSL 式を表現する便利な方法を提供する。

```racket
> (+ 1 1)
2
> '(+ 1 1)
(list '+ 1 1)
> (+ (* 3 3) (* 4 4))
25
> '(+ (* 3 3) (* 4 4))
(list '+ (list '* 3 3) (list '* 4 4))
```

式の前にクォートを付けるだけで、ISL+ のデータが得られる。

S式表現を解釈するのは不格好である。主に、すべての S式が BSL-expr を表すわけではないからである。たとえば、#true、"hello"、'(+x1) は BSL 式の代表ではない。その結果、S式はインタープリタの設計者にとってかなり不便である。

プログラマは、使用の便宜と実装のあいだのギャップを埋めるためにパーサを発明した。パーサは、あるデータ片がデータ定義に適合するかどうかを同時に検査し、適合するなら、選んだデータのクラスから一致する要素を構築する。後者はパース木と呼ばれる。与えられたデータが適合しない場合、パーサは「入力エラー（Input Errors）」の検査付き関数のようにエラーを知らせる。

図125は S式のための BSL パーサを示す。具体的には、parse は S-expr を消費し、BSL-expr を生成する——与えられた S式が、BSL-expr の代表を持つ BSL 式をクォートした結果であるとき、かつそのときに限る。

練習問題 349. 定義領域のすべての要素がテスト実行中にカバーされたと DrRacket が告げるまで、parse のためのテストを作成せよ。

練習問題 350. 設計レシピに関して、このプログラムの定義のどこが普通でないか。

練習問題 351. interpreter-expr を設計せよ。この関数は S式を受け付ける。parse がそれらを BSL-expr として認識するなら、その値を生成する。そうでなければ、parse と同じエラーを知らせる。

> **図125: From S-expr to BSL-expr**

```racket
; S-expr -> BSL-expr
(define (parse s)
  (cond
    [(atom? s) (parse-atom s)]
    [else (parse-sl s)]))

; SL -> BSL-expr
(define (parse-sl s)
  (cond
    [(and (consists-of-3 s) (symbol? (first s)))
     (cond
       [(symbol=? (first s) '+)
        (make-add (parse (second s)) (parse (third s)))]
       [(symbol=? (first s) '*)
        (make-mul (parse (second s)) (parse (third s)))]
       [else (error WRONG)])]
    [else (error WRONG)]))

; Atom -> BSL-expr
(define (parse-atom s)
  (cond
    [(number? s) s]
    [(string? s) (error WRONG)]
    [(symbol? s) (error WRONG)]))

; SL -> Boolean
(define (consists-of-3 s)
  (and (cons? s) (cons? (rest s)) (cons? (rest (rest s)))
       (empty? (rest (rest (rest s))))))
```


### 21.2 変数の解釈（Interpreting Variables）

最初の節は定数定義を無視しているので、変数を含む式には値がない。実際、x が何を表すかを知らなければ、(+3x) を評価しても意味がない。したがって、評価器の最初の洗練の1つは、評価したい式に変数を追加することである。仮定は、定義領域に

```racket
(define x 5)
```

のような定義があり、プログラマが相互作用領域で x を含む式を評価する、というものである。

```racket
> x
5
> (+ x 3)
8
> (* 1/2 (* x 3))
7.5
```

実際、第2の定義、たとえば (definey3) を想像し、2つの変数を含む相互作用を想像することもできる。

```racket
> (+ (* x x)     (* y y))
34
```

前節は暗黙のうちに、変数の表現として記号を提案している。結局、変数を含む式を表すのにクォートした S式を選ぶなら、記号は自然に現れるからである。

```racket
> 'x
'x
> '(* 1/2 (* x 3))
(list '* 0.5 (list '* 'x 3))
```

明白な代替は文字列であり、"x" が x を表すことになるが、本書はインタープリタの設計についての本ではないので、記号に固執する。この決定から、練習問題345のデータ定義をどう修正するかが従う。

```racket
; A BSL-var-expr is one of:
; – Number
; – Symbol
; – (make-add BSL-var-expr BSL-var-expr)
; – (make-mul BSL-var-expr BSL-var-expr)
```

データ定義に1つの節を加えるだけである。

データ例については、次の表が変数を含むいくつかの BSL 式と、その BSL-var-expr 表現を示す。

> BSL expression representation of BSL expressionx 'x(+ x 3) (make-add 'x 3)(* 1/2 (* x 3)) (make-mul 1/2 (make-mul 'x 3))(+ (* x x) (* y y)) (make-add (make-mul 'x 'x) (make-mul 'y 'y))

これらはすべて上の相互作用から取られており、x が5、y が3のときの結果を知っている。

変数式の値を求める1つの方法は、すべての変数をそれらが表す値で置き換えることである。これは学校の数学の授業で知っているやり方であり、まったく立派なやり方である。

練習問題 352. subst を設計せよ。この関数は BSL-var-expr ex、Symbol x、および Number v を消費する。ex と同様で、x のすべての出現が v で置き換えられた BSL-var-expr を生成する。

練習問題 353. numeric? 関数を設計せよ。BSL-var-expr が同時に BSL-expr であるかどうかを判定する。ここでは、練習問題345の解が、Symbol のない BSL-var-expr の定義であると仮定する。

練習問題 354. eval-variable を設計せよ。この検査付き関数は BSL-var-expr を消費し、入力に対して numeric? が真を返すならその値を求める。そうでなければエラーを知らせる。

一般に、プログラムは定義領域で多くの定数を定義し、式は1つより多くの変数を含む。そのような式を評価するには、一連の定数定義を含むときの定義領域の表現が必要である。この練習問題では連想リストを使う。

```racket
; An AL (short for association list) is [List-of Association].
; An Association is a list of two items:
;   (cons Symbol (cons Number '())).
```

AL の要素をいくつか作れ。

eval-variable* を設計せよ。この関数は BSL-var-expr ex と連想リスト da を消費する。ex から始め、da のすべての連想に対して subst を反復的に適用する。結果について numeric? が成り立つなら、その値を求める。そうでなければ eval-variable と同じエラーを知らせる。
ヒント 与えられた BSL-var-expr を原子的な値と考え、代わりに与えられた連想リストを走査せよ。この関数の作成には「同時処理（Simultaneous Processing）」からの設計知識が少し必要なので、このヒントを提供する。

環境モデル 練習問題354は、定数定義の数学的理解に依存している。名前がある値を表すと定義されていれば、その名前のすべての出現をその値で置き換えられる。置換は、評価プロセスが始まる前に、この置き換えを一度にすべて行う。

環境モデルと呼ばれる代替のアプローチは、必要なときに変数の値を調べることである。評価器は式の処理を直ちに始めるが、定義領域の表現も一緒に持ち運ぶ。評価器が変数に出会うたびに、定義領域でその値を調べて使う。

**練習問題 355. eval-var-lookup を設計せよ。この関数は eval-variable* と同じシグネチャを持つ。**

```racket
; BSL-var-expr AL -> Number
(define (eval-var-lookup e da)...)
```

置換を使う代わりに、この関数は BSL-var-expr の設計レシピが示唆するやり方で式を走査する。式を降りていくにつれて、da を「一緒に持ち運ぶ」。記号 x に出会ったとき、assq を使って連想リストで x の値を調べる。値がなければ、eval-var-lookup はエラーを知らせる。

### 21.3 関数の解釈（Interpreting Functions）

この時点で、定数定義と変数式からなる BSL プログラムをどう評価するかを理解している。当然、関数定義を追加して——少なくとも原理的には——BSL のすべてにどう対処するかを知りたい。

本節の目標は、「変数の解釈（Interpreting Variables）」の評価器を洗練し、関数に対処できるようにすることである。関数定義は定義領域に現れるので、洗練された評価器を言い換えると、定義領域にいくつかの関数定義があり、プログラマが相互作用領域にこれらの関数の使用を含む式を入力したときに、DrRacket をシミュレートする、ということである。

簡単のため、定義領域のすべての関数は1つの引数を消費し、そのような定義は1つだけであると仮定しよう。必要な領域知識は学校にさかのぼる。そこでは f(x) = e が関数 f の定義を表し、f(a) が f の a への適用を表し、後者を評価するには e の中の x を a で置き換える、と学んだ。実際のところ、BSL のような言語での関数適用の評価も、だいたいそのように動く。

次の練習問題に取り組む前に、間奏1で示された関数に関する用語の知識を新たにしておいてもよい。たいていの場合、代数のコースはこの数学の側面を軽く流すが、これらの問題を解きたいなら、用語の正確な使用と理解が必要である。

練習問題 356. 「変数の解釈（Interpreting Variables）」のデータ表現を拡張し、プログラマ定義の関数の適用を含めよ。関数適用は2つの部分からなることを思い出せ。名前と式である。前者は適用される関数の名前であり、後者は引数である。

これらの式を表現せよ。(k(+11))、(*5(k(+11)))、(*(i5)(k(+11)))。この新しく定義されたデータのクラスを BSL-fun-expr と呼ぶ。

**練習問題 357. eval-definition1 を設計せよ。この関数は4つの引数を消費する。**

1. BSL-fun-expr ex;
2. 関数名を表す記号 f;
3. 関数の仮引数を表す記号 x; および
4. 関数の本体を表す BSL-fun-expr b。

ex の値を求める。eval-definition1 が f のある引数への適用に出会ったとき、それは

1. 引数を評価し、
2. b の中の x を引数の値で置換し、
3. 最後に、得られた式を eval-definition1 で評価する。

関数適用の引数を arg と仮定して、ステップをコードとしてどう表すかは次のとおりである。

```racket
(local ((define value (eval-definition1 arg f x b))
        (define plugd (subst b x value)))
  (eval-definition1 plugd f x b))
```

この行が、まだ扱っていない形の再帰を使っていることに注意せよ。そのような関数の適切な設計は「生成的再帰（Generative Recursion）」で議論する。

eval-definition1 が変数に出会ったとき、練習問題354の eval-variable と同じエラーを知らせる。f 以外の関数名を参照する関数適用についてもエラーを知らせる。

警告 この未カバーの形の再帰の使用は、計算に新しい要素を導入する。非停止である。つまり、プログラムが結果を届けるかエラーを知らせる代わりに、永遠に動き続けることがある。最初の4部の設計レシピに従ったなら、そのようなプログラムは書けない。お楽しみとして、eval-definition1 が永遠に動き続けるような入力を構成せよ。プログラムを終了するには *STOP* を使え。

相互作用領域を模倣する評価器のためには、定義領域の表現が必要である。それは定義のリストであると仮定する。

**練習問題 358. 関数定義のための構造体型とデータ定義を提供せよ。そのような定義が3つの本質的な属性を持つことを思い出せ。**

1. 関数の名前。記号で表される。
2. 関数の仮引数。これも名前である。
3. 関数の本体。変数式である。

このデータのクラスを指すのに BSL-fun-def を使う。

データ定義を使って、次の BSL 関数定義を表現せよ。

1. (define(fx)(+3x))
2. (define(gy)(f(*2y)))
3. (define(hv)(+(fv)(gv)))

次に、1引数の関数定義をいくつか含む定義領域を表すクラス BSL-fun-def* を定義せよ。f、g、h を定義する定義領域をデータ表現に翻訳し、da-fgh と名づけよ。

最後に、次のウィッシュに取り組め。

```racket
; BSL-fun-def* Symbol -> BSL-fun-def
; retrieves the definition of f in da
; signals an error if there is none
(check-expect (lookup-def da-fgh 'g) g)
(define (lookup-def da f)...)
```

定義の検索は、適用の評価に必要である。

練習問題 359. eval-function* を設計せよ。この関数は BSL-fun-expr の ex と、定義領域の BSL-fun-def* 表現 da を消費する。定義領域が da を含むと仮定して、相互作用領域で ex を評価したときに DrRacket が示す結果を生成する。

この関数は練習問題357の eval-definition1 のように動く。ある関数 f の適用について、

1. 引数を評価し、
2. da の BSL-fun-def 表現で f の定義を調べる。これには仮引数と本体が付いてくる。
3. 関数の本体の中の関数仮引数を引数の値で置換し、
4. 再帰経由で新しい式を評価する。

DrRacket と同様に、eval-function* は定義領域に定義のない変数や関数名に出会ったときエラーを知らせる。

### 21.4 すべてを解釈する（Interpreting Everything）

次の BSL プログラムを見てみよ。

```racket
(define close-to-pi 3.14)

(define (area-of-circle r)
  (* close-to-pi (* r r)))

(define (volume-of-10-cylinder r)
  (* 10 (area-of-circle r)))
```

これらの定義を DrRacket の定義領域と考えよ。*RUN* をクリックしたあと、相互作用領域で close-to-pi、area-of-circle、volume-of-10-cylinder を含む式を評価できる。

```racket
> (area-of-circle 1)
#i3.14
> (volume-of-10-cylinder 1)
#i31.400000000000002
> (* 3 close-to-pi)
#i9.42
```

本節の目標は、評価器を再び洗練し、DrRacket のこの程度を模倣できるようにすることである。

練習問題 360. DrRacket の定義領域の表現のためのデータ定義を定式化せよ。具体的には、定数定義と1引数の関数定義を自由に混ぜた列についてデータ表現が動くべきである。本節の冒頭にある3つの定義からなる定義領域を表現できることを確かめよ。このデータのクラスを BSL-da-all と名づける。

lookup-con-def 関数を設計せよ。BSL-da-all da と記号 x を消費する。名前が x である定数定義の表現が da に存在するならそれを生成する。そうでなければ、そのような定数定義が見つからないというエラーを知らせる。

lookup-fun-def 関数を設計せよ。BSL-da-all da と記号 f を消費する。名前が f である関数定義の表現が da に存在するならそれを生成する。そうでなければ、そのような関数定義が見つからないというエラーを知らせる。

練習問題 361. eval-all を設計せよ。練習問題359の eval-function* と同様に、この関数は式の表現と定義領域を消費する。相互作用領域のプロンプトで式が入力され、定義領域に適切な定義があるときに DrRacket が示すのと同じ値を生成する。ヒント eval-all 関数は、与えられた式の中の変数を、練習問題355の eval-var-lookup のように処理すべきである。

練習問題 362. BSL 式と定義領域の構造体ベースのデータ表現を入力するのは面倒である。「式の解釈（Interpreting Expressions）」の終わりが示すように、式と（定義のリストを）クォートする方がはるかに簡単である。

関数 interpreter を設計せよ。S-expr と Sl を消費する。前者は式を、後者は定義のリストを表すことになっている。関数は両方を適切な構文解析関数で解析し、それから練習問題361の eval-all を使って式を評価する。ヒント 定義と定義のリストのためのパーサを作るには、練習問題350の考えを適応させなければならない。

この時点で、BSL の解釈について多くを知っている。欠けているピースには次のものがある。cond や if を持つブール、string-length や string-append のような操作を持つ文字列、'()、empty?、cons、cons?、first、rest を持つリスト、などである。評価器がこれらすべてに対処できれば、基本的に完成である。再帰的な関数をどう解釈するかは、すでに評価器が知っているからである。さて「信じてくれ、これらの洗練をどう設計するかは知っている」と言うとき、私たちは本気である。

## 22 プロジェクト：XML の流通（Project: The Commerce of XML）

XML は広く使われているデータ言語である。その用途のひとつは、異なるコンピュータ上で動くプログラム同士のメッセージ交換である。たとえば、Web ブラウザを Web サイトに向けるとき、あなたは自分のコンピュータ上のプログラムを、別のコンピュータ上のプログラムにつないでいる。後者は前者に XML データを送る。ブラウザが XML データを受け取ると、それを画像としてコンピュータのモニタに描画する。

次の対比は、この考えを具体例で示している：

> ブラウザで描画された XML データ`<ul>` `<li> hello </li>` `<li> <ul>` `<li> one </li>` `<li> two </li>` `</ul>` `</li>` `<li> world </li>` `<li> good bye </li>``</ul>` [image: xml-example.png]

左側には、Web サイトが Web ブラウザに送るかもしれない XML データの断片がある。右側には、あるよく使われるブラウザがこの断片をどのようにグラフィカルに描画するかが示されている。

本章では、絡み合ったデータ定義と反復的洗練に関するもう一つの設計演習として、XML 処理の基礎を説明する。次の節では、S式と XML データの非公式な比較から始め、それを使って本格的なデータ定義を定式化する。残りの節では、XML データの S式をどう処理するかを例で説明する。

> **注:** 2026 年には XML が古臭いと思うなら、JSON やその他の現代的なデータ交換形式で練習問題をやり直してもよい。設計原則は同じままである。

### 22.1 S式としての XML（XML as S-expressions）

最も基本的な XML データの断片は次のように見える：

> `<machine> </machine>`

これは要素（element）と呼ばれ、「machine」がその要素の名前である。要素の二つの部分は、要素の内容を区切る括弧のようなものである。二つの部分のあいだに内容がないとき——空白を除いて——XML は短縮形を許す：

> `<machine />`

しかし、ここで関心があるかぎり、この短縮形は明示的に括弧で囲んだ版と等価である。

S式の観点からは、XML 要素は、何らかの内容を囲む名前付きの括弧の対である。実際、上のものを S式で表すのはごく自然である：

> **注:** Racket の
xml ライブラリは、XML を構造体でも S式でも表す。

```racket
'(machine)
```

このデータ片は開き括弧と閉じ括弧を持ち、内容を埋め込む余地がある。

内容を持つ XML データの断片は次のとおりである：

> `<machine><action /></machine>`

`<action />` の部分は短縮形であることを思い出してほしい。つまり実際には次のデータを見ている：

> `<machine><action></action></machine>`

一般に、XML 要素の内容は一連の XML 要素である：

> `<machine><action /><action /><action /></machine>`

ちょっと待て！続ける前に、`<action />` の短縮形を展開せよ。

S式表現は引き続き単純に見える。最初のものは次のとおりである：

```racket
'(machine (action))
```

そして二つ目の表現は次である：

```racket
'(machine (action) (action) (action))
```

内容として三つの `<action />` 要素の列を持つ XML データの断片を見ると、そのような要素を互いに区別したいと思うかもしれないと気づく。そのために、XML 要素には属性（attribute）が付く。たとえば、

> `<machine initial="red"></machine>`

は、「initial」という名前で、値が文字列引用符のあいだの「red」である属性を一つ付けた「machine」要素である。入れ子の要素にも属性がある複雑な XML 要素は次のとおりである：

> `<machine initial="red">` `<action state="red"` `next="green" />` `<action state="green"` `next="yellow" />` `<action state="yellow" next="red" />``</machine>`

読みやすくするために空白、字下げ、改行を使うが、ここでの XML データにとってこの空白には意味がない。

当然ながら、これらの「machine」要素の S式は、XML の親族とよく似て見える：

> **注:** XML は S式より 40 年若い。

```racket
'(machine ((initial "red")))
```

要素に属性を加えるには、リストのリストを使う。後者の各々は二つの項目を含む：シンボルと文字列である。シンボルは属性の名前を、文字列はその値を表す。この考えは複雑な形の XML データにも自然に当てはまる：

```racket
'(machine ((initial "red"))
  (action ((state "red") (next "green")))
  (action ((state "green") (next "yellow")))
  (action ((state "yellow") (next "red"))))
```

今のところ、属性は二つの開き括弧で印付けされ、残りの（XML 要素の表現の）リストは一つの開き括弧を持つことに注意せよ。

Intermezzo 2: Quote, Unquote の考えを思い出すかもしれない。そこでは S式を使って XHTML——XML の特別な方言——を表している。とくにそのインターメッツォは、プログラマが nontrivial な XML データや、準クォートとアンクォートを使った XML 表現のテンプレートをどれほど容易に書き下せるかを示す。もちろん、「式の解釈」は、与えられた任意の S式が XML データの表現であるかどうかを判定するにはパーサが必要だと指摘する。パーサは複雑で珍しい種類の関数である。

それでも、この古い詩的な考えの実用的な有用性を示すために、S式に基づく XML の表現を選ぶ。データ定義を徐々に練り上げ、反復的洗練を働かせる。最初の試みは次のとおりである：

```racket
; An Xexpr.v0 (short for X-expression) is a one-item list:
;   (cons Symbol '())
```

これは、本節の冒頭にあった「名前付き括弧」の考えである。この要素表現に内容を付けるのは簡単である：

```racket
; An Xexpr.v1 is a list:
;   (cons Symbol [List-of Xexpr.v1])
```

シンボルの名前は、それ以外は XML 要素の代表からなるリストの先頭項目になる。

最後の洗練ステップは属性を加えることである。XML 要素の属性は省略可能なので、改訂したデータ定義は二つの節を持つ：

```racket
; An Xexpr.v2 is a list:
; – (cons Symbol Body)
; – (cons Symbol (cons [List-of Attribute] Body))
; where Body is short for [List-of Xexpr.v2]
; An Attribute is a list of two items:
;   (cons Symbol (cons String '()))
```

**練習問題 363.** Xexpr.v2 のすべての要素は Symbol で始まるが、あるものは属性のリストが続き、あるものは単に Xexpr.v2 のリストが続く。共通の始まりを切り出し、終わり方の違いを際立たせるよう、Xexpr.v2 の定義を書き直せ。

Xexpr.v2 から List-of の使用を取り除け。

**練習問題 364. 次の XML データを Xexpr.v2 の要素として表せ：**

1. `<transition from="seen-e" to="seen-f" />`
2. `<ul><li><word /><word /></li><li><word /></li></ul>`

どちらが Xexpr.v0 または Xexpr.v1 で表せるか？

**練習問題 365. 次の Xexpr.v2 の要素を XML データとして解釈せよ：**

1. '(server((name"example.org")))
2. '(carcas(board(grass))(player((name"sam"))))
3. '(start)

どれが Xexpr.v0 または Xexpr.v1 の要素か？

おおざっぱに言えば、X式（X-expression）は構造体をリスト経由でシミュレートする。このシミュレーションはプログラマにとって便利であり、キーボード入力を最小に抑える。たとえば、X式に属性リストが付かないなら、それは単に省略される。このデータ表現の選択は、そのような式を手で書くことと自動で処理することのあいだのトレードオフである。後者の問題に対処する最良の方法は、X式を構造体のように見せる関数——とくに準フィールドにアクセスする関数——を提供することである：

- xexpr-name。要素表現のタグを取り出す；
- xexpr-attr。属性のリストを取り出す；そして
- xexpr-content。内容要素のリストを取り出す。

これらの関数があれば、リストで XML を表しつつ、構造体型のインスタンスであるかのように振る舞わせられる。

これらの関数は S式を解析する。パーサの設計は難しい。だから慎重に設計しよう。いくつかのデータ例から始める：

```racket
(define a0 '((initial "X")))

(define e0 '(machine))
(define e1 `(machine,a0))
(define e2 '(machine (action)))
(define e3 '(machine () (action)))
(define e4 `(machine,a0 (action) (action)))
```

最初の定義は属性のリストを導入し、X式の構築で二度再利用される。e0 の定義は、X式が属性も内容も持たないことがあることを思い起こさせる。e2 と e3 が基本的に等価である理由を説明できるはずである。

次にシグネチャ、目的文、ヘッダを定式化する：

```racket
; Xexpr.v2 -> [List-of Attribute]
; retrieves the list of attributes of xe
(define (xexpr-attr xe) '())
```

ここでは xexpr-attr に焦点を当てる。他の二つは練習問題に残す。

機能例を作るには、属性をまったく持たない X式から属性を取り出すときの決定が要る。選んだ表現では欠けている属性を完全に省略するが、構造体に基づく XML 表現では `'()` を供給しなければならない。したがって関数は、そのような X式に対して `'()` を生成する：

```racket
(check-expect (xexpr-attr e0) '())
(check-expect (xexpr-attr e1) '((initial "X")))
(check-expect (xexpr-attr e2) '())
(check-expect (xexpr-attr e3) '())
(check-expect (xexpr-attr e4) '((initial "X")))
```

テンプレートを開発する時である。Xexpr.v2 のデータ定義は複雑なので、ゆっくり一歩ずつ進む。第一に、データ定義は二種類の X式を区別するが、両方の節はシンボルをリストに cons して構築されるデータを記述する。第二に、二つの節を分けるのはリストの残りであり、とくに属性リストの任意の有無である。この二つの洞察をテンプレートに翻訳しよう：

```racket
(define (xexpr-attr xe)
  (local ((define optional-loa+content (rest xe)))
    (cond
      [(empty? optional-loa+content)...]
      [else...])))
```

局所定義は X式の名前を切り落とし、リストの残りを残す。それは属性のリストで始まることもあれば始まらないこともある。鍵は、それが単なるリストであり、二つの cond 節がそれを示していることである。第三に、このリストは自己参照経由ではなく、いくつかの属性を（空かもしれない）X式のリストに任意に cons したものとして定義される。言い換えれば、いつもの二つの場合を区別し、いつもの断片を取り出す必要がある：

```racket
(define (xexpr-attr xe)
  (local ((define optional-loa+content (rest xe)))
    (cond
      [(empty? optional-loa+content)...]
      [else (... (first optional-loa+content)
... (rest optional-loa+content)...)])))
```

この時点で、目下の課題には再帰が要らないことがすでに分かる。そこで設計レシピの第5ステップに移る。明らかに、与えられた X式が名前以外何も持たないなら属性はない。第2節では、リストの最初の項目が属性のリストなのか単なる Xexpr.v2 なのかが問題になる。これは複雑に聞こえるので、願いを立てる：

```racket
; [List-of Attribute] or Xexpr.v2 ->???
; determines whether x is an element of [List-of Attribute]
; #false otherwise
(define (list-of-attributes? x)
  #false)
```

この関数があれば、xexpr-attr を完成させるのは簡単である。図 126 を見よ。最初の項目が属性のリストなら、関数はそれを生成する。さもなければ属性はない。

> **図126: The complete definition of xexpr-attr**

```racket
(define (xexpr-attr xe)
  (local ((define optional-loa+content (rest xe)))
    (cond
      [(empty? optional-loa+content) '()]
      [else
       (local ((define loa-or-x
                 (first optional-loa+content)))
         (if (list-of-attributes? loa-or-x)
             loa-or-x
             '()))])))
```

list-of-attributes? の設計も同じ仕方で進め、次の定義を得る：

```racket
; [List-of Attribute] or Xexpr.v2 -> Boolean
; is x a list of attributes
(define (list-of-attributes? x)
  (cond
    [(empty? x) #true]
    [else
     (local ((define possible-attribute (first x)))
       (cons? possible-attribute))]))
```

設計過程の詳細は飛ばす。特筆すべき点がないからである。特筆すべきなのはこの関数のシグネチャである。可能な入力として単一のデータ定義を指定する代わりに、シグネチャは英語の “or” で分けた二つのデータ定義を組み合わせる。ISL+ では、確定した意味を持つこのような非公式なシグネチャは、時に受け入れられる。

**練習問題 366.** xexpr-name と xexpr-content を設計せよ。

**練習問題 367.** 設計レシピは xexpr-attr のテンプレートに自己参照を要求する。この自己参照をテンプレートに加え、完成した解析関数がそれを含まない理由を説明せよ。

**練習問題 368.** list-of-attributes? 関数の定義のための非公式な “or” シグネチャを置き換えるデータ定義を定式化せよ。

**練習問題 369.** find-attr を設計せよ。この関数は属性のリストとシンボルを消費する。属性リストがそのシンボルを文字列に対応付けているなら、関数はこの文字列を取り出す。さもなければ #false を返す。assq を調べ、それを使って関数を定義せよ。

本章の残りでは、Xexpr は Xexpr.v2 を指す。また、xexpr-name、xexpr-attr、xexpr-content が定義されていると仮定する。最後に、練習問題 369 の find-attr を使って属性値を取り出す。

### 22.2 XML 列挙の描画（Rendering XML Enumerations）

XML は実際には言語の族である。人々は特定の通信チャネル向けに方言を定義する。たとえば、XHTML は Web コンテンツを XML 形式で送るための言語である。本節では、XHTML の小さな断片——具体的には本章冒頭の列挙——向けの描画関数をどう設計するかを示す。

`ul` タグはいわゆる順序なし HTML リストを囲む。このリストの各項目は `li` でタグ付けされ、そこには単語だけでなく他の要素、さらには列挙さえ含むことが多い。「順序なし HTML」とは、各項目を番号ではなく先頭の黒点（bullet）付きで描画することを意味する。

Xexpr にはプレーンな文字列が付かないので、部分集合で XHTML 列挙をどう表すかはすぐには明らかでない。一つの選択肢は、データ表現をもう一度洗練し、Xexpr が String でもあり得るようにすることである。もう一つの選択肢は、テキストの表現を導入することである：

```racket
; An XWord is '(word ((text String))).
```

ここではこの第二の選択肢を使う。ティーチング言語の派生元である Racket は、Xexpr に String を含むティーチパックを提供する。

**練習問題 370.** XWord の例を三つ作れ。ある ISL+ 値が XWord に属するかを検査する word?、および XWord のインスタンスの唯一の属性の値を取り出す word-text を設計せよ。

**練習問題 371.** プレーンな文字列である XML 要素——列挙中の項目を含む——を表せるよう、Xexpr の定義を洗練せよ。

単語の表現があれば、XHTML 風の単語の列挙を表すのは簡単である：

```racket
; An XEnum.v1 is one of:
; – (cons 'ul [List-of XItem.v1])
; – (cons 'ul (cons Attributes [List-of XItem.v1]))
; An XItem.v1 is one of:
; – (cons 'li (cons XWord '()))
; – (cons 'li (cons Attributes (cons XWord '())))
```

完全のために、データ定義は属性リストを含む。描画には影響しないが。

ちょっと待て！XEnum.v1 のすべての要素が XExpr にも属することを論ぜよ。

XEnum.v1 のサンプル要素は次のとおりである：

```racket
(define e0
  '(ul
    (li (word ((text "one"))))
    (li (word ((text "two"))))))
```

これは本章冒頭の例の内側の列挙に対応する。2htdp/image ティーチパックの助けを借りて描画すると、次のような画像になるはずである：

> [image: pict_146.png]

黒点の半径と、黒点とテキストの距離は美的な問題である。ここでは考え方が大事である。

この種の画像を作るには、次の ISL+ プログラムを使うかもしれない：

> **注:** これらの式は相互作用領域で開発した。あなたならどうするか？

```racket
(define e0-rendered
  (above/align
   'left
   (beside/align 'center BT (text "one" 12 'black))
   (beside/align 'center BT (text "two" 12 'black))))
```

ここで BT は黒点の描画であるとする。

では関数を慎重に設計しよう。データ表現が二つのデータ定義を要するので、設計レシピは二つの関数を並行して設計すべきだと教える。しかし二度目に見ると、この特定の場合では第二のデータ定義は第一から切り離されているので、別々に扱える。

さらに、XItem.v1 の定義は二つの節からなり、関数自体は二つの節を持つ cond からなるべきである。しかし XItem.v1 を Xexpr の部分言語と見るポイントは、これら二つの節を Xexpr のセレクタ関数——とくに xexpr-content——の観点から考えることである。この関数を使えば、属性の有無にかかわらず、項目のテキスト部分を取り出せる：

```racket
; XItem.v1 -> Image
; renders an item as a "word" prefixed by a bullet
(define (render-item1 i)
  (... (xexpr-content i)...))
```

一般に、xexpr-content は Xexpr のリストを取り出す。この特定の場合、リストはちょうど一つの XWord を含み、この単語は一つのテキストを含む：

```racket
(define (render-item1 i)
  (local ((define content (xexpr-content i))
          (define element (first content))
          (define a-word (word-text element)))
    (... a-word...)))
```

ここからは簡単である：

```racket
(define (render-item1 i)
  (local ((define content (xexpr-content i))
          (define element (first content))
          (define a-word (word-text element))
          (define item (text a-word 12 'black)))
    (beside/align 'center BT item)))
```

項目に描画するテキストを取り出したあと、あとはそれをテキストとして描画し、先頭に黒点を付けるだけである。この最後のステップをどう発見するかは、上の例を見よ。

**練習問題 372.** 先へ進む前に、render-item1 の定義にテストを付けよ。これらのテストが BT 定数に依存しないよう定式化せよ。次に、関数がどう働くかを説明せよ。目的文が何をするかを説明していることを念頭に置け。

次に、列挙を描画する関数の設計に焦点を当てられる。上の例を使い、設計の最初の二つのステップは簡単である：

```racket
; XEnum.v1 -> Image
; renders a simple enumeration as an image
(check-expect (render-enum1 e0) e0-rendered)
(define (render-enum1 xe) empty-image)
```

鍵となるステップはテンプレートの開発である。データ定義によれば、XEnum.v1 の要素は興味深いデータを一つ含む。すなわち（表現された）XML 要素である。最初の項目は常に 'ul なので取り出す必要はなく、任意の第二項目は属性のリストであり、これは無視する。これを踏まえ、最初のテンプレート草案は render-item1 のものと同じように見える：

```racket
(define (render-enum1 xe)
  (... (xexpr-content xe)...)); [List-of XItem.v1]
```

データ指向の設計レシピは、複雑な形のデータに出会うたびに別関数を設計すべきだと教えるが、「抽象化」の抽象化に基づく設計レシピは、可能なときは既存の抽象化——たとえば図 95 と 96 のリスト処理関数——を再利用せよと教える。render-enum1 はリストを処理し、そこから一つの画像を作るはずなので、シグネチャが合うリスト処理抽象化は foldr と foldl だけである。目的文も調べると、とくに foldr について、上の e0-rendered 例のようなパターンが見える。再利用の設計レシピに従い、使ってみよう：

```racket
(define (render-enum1 xe)
   (local ((define content (xexpr-content xe))
; XItem.v1 Image -> Image
           (define (deal-with-one item so-far)
...))
     (foldr deal-with-one empty-image content)))
```

型合わせから、次のことも分かる：

1. foldr の第一引数は二引数関数でなければならない；
2. 第二引数は画像でなければならない；そして
3. 最後の引数は XML 内容を表すリストである。

当然、empty-image が正しい出発点である。

この再利用による設計は、「折りたたまれる」関数に注意を向ける。それは一つの項目と、foldr がこれまでに作った画像を、別の画像に変える。deal-with-one のシグネチャはこの洞察を述べる。第一引数が XItem.v1 なので、それを描画する関数は render-item1 である。これで二つの画像——最初の項目の画像と残りの項目の画像——が得られ、組み合わせなければならない。積み重ねるには above を使う：

```racket
(define (render-enum1 xe)
  (local ((define content (xexpr-content xe))
; XItem.v1 Image -> Image
          (define (deal-with-one item so-far)
            (above/align 'left
                          (render-item1 item)
                          so-far)))
    (foldr deal-with-one empty-image content)))
```

> **図127: A realistic data representation of XML enumerations**

```racket
; An XItem.v2 is one of:
; – (cons 'li (cons XWord '()))
; – (cons 'li (cons [List-of Attribute] (list XWord)))
; – (cons 'li (cons XEnum.v2 '()))
; – (cons 'li (cons [List-of Attribute] (list XEnum.v2)))
;
; An XEnum.v2 is one of:
; – (cons 'ul [List-of XItem.v2])
; – (cons 'ul (cons [List-of Attribute] [List-of XItem.v2]))
```

平坦な列挙はよくあるが、本格的な場合の単純な近似でもある。現実世界では、Web ブラウザは Web 経由で届く任意に入れ子になった列挙に対処しなければならない。XML とその Web ブラウザ方言 XHTML では、入れ子は簡単である。任意の要素が任意の他の要素の内容として現れ得る。この関係を我々の限られた XHTML 表現で表すには、項目は単語か別の列挙であると言う。図 127 はデータ定義の第二改訂を示す。列挙のデータ定義の改訂も含み、第一の定義が正しい形の項目を参照するようにしている。

> **注:** 任意の入れ子がこの問題の正しい考え方かどうか疑問に思うか？そうなら、三階層の入れ子だけを許すデータ定義を開発し、それを使ってみよ。

> **図128: Refining functions to match refinements of data definitions**

```racket
(define SIZE 12) ; font size
(define COLOR "black") ; font color
(define BT ; a graphical constant
  (beside (circle 1 'solid BLACK) (text " " SIZE COLOR)))

; Image -> Image
; marks item with bullet
(define (bulletize item)
  (beside/align 'center BT item))

; XEnum.v2 -> Image
; renders an XEnum.v2 as an image
(define (render-enum xe)
  (local ((define content (xexpr-content xe))
          ; XItem.v2 Image -> Image
          (define (deal-with-one item so-far)
            (above/align 'left (render-item item) so-far)))
    (foldr deal-with-one empty-image content)))

; XItem.v2 -> Image
; renders one XItem.v2 as an image
(define (render-item an-item)
  (local ((define content (first (xexpr-content an-item))))
    (bulletize
      (cond
        [(word? content)
         (text (word-text content) SIZE BLACK)]
        [else (render-enum content)]))))
```

次の問いは、このデータ定義の変更が描画関数にどう影響するかである。言い換えれば、render-enum1 と render-item1 を改訂し、それぞれ XEnum.v2 と XItem.v2 に対処できるようにする必要がある。ソフトウェア技術者は常にこの種の問いに直面しており、設計レシピが輝くもう一つの状況である。

図 128 は完全な答えを示す。変更は XItem.v2 のデータ定義に限られるので、描画プログラムの変更が項目描画の関数に現れるのは驚くに当たらない。render-item1 は異なる形の XItem.v1 を区別する必要がないが、render-item は cond を使わざるを得ない。XItem.v2 が二種類の項目を列挙するからである。このデータ定義が現実世界のものに近いことを踏まえると、区別の特徴は `'()` 対 cons のような単純なものではなく、与えられた項目の特定の部分である。項目の内容が XWord なら、描画関数はこれまでどおり進む。さもなければ、項目は列挙を含み、その場合 render-item は render-enum を使ってそのデータを扱う。XItem.v2 のデータ定義がちょうどこの点で XEnum.v2 を参照し直すからである。

**練習問題 373.** 図 128 にはテストケースが欠けている。すべての関数のテストケースを開発せよ。

**練習問題 374.** 図 127 のデータ定義は list を使う。それらを cons を使うよう書き直せ。次にレシピを使い、XEnum.v2 と XItem.v2 向けの描画関数を一から設計せよ。図 128 と同じ定義にたどり着くはずである。

**練習問題 375. cond を**

```racket
(beside/align 'center BT...)
```

**で包むのは驚くかもしれない。** 関数定義を編集し、包みが各節に一度ずつ現れるようにせよ。変更が働くと確信できる理由は何か？どちらの版を好むか？

**練習問題 376.** XEnum.v2 のインスタンス中のすべての "hello" を数えるプログラムを設計せよ。

**練習問題 377.** 列挙中のすべての "hello" を "bye" に置き換えるプログラムを設計せよ。

### 22.3 ドメイン固有言語（Domain-Specific Languages）

技術者は日常的に、実行前に特定の文脈向けの設定（configuration）を要する大規模ソフトウェアシステムを構築する。この設定の仕事は、多くの異なるソフトウェアシステムを扱わなければならないシステム管理者に落ちがちである。「設定」とは、プログラムがコマンドラインやジェスチャ（マウスクリック、スワイプ）経由で起動されるときに主関数が必要とするデータを指す。ある意味で設定は単なる追加の引数だが、通常あまりに複雑なので、プログラム設計者はファイル経由で渡すことを好む。

ソフトウェア技術者は、システム管理者があらゆるプログラミング言語を知っているとは仮定できないので、単純で特別目的の設定言語を考案する傾向がある。これらの特別な言語はドメイン固有言語（domain-specific language、DSL）としても知られる。よく知られた XML 構文のような共通の核の周りにこれらの DSL を開発すると、システム管理者の生活が簡単になる。小さな XML 「プログラム」を書いて、起動しなければならないシステムを設定できる。

> **注:** 設定はさまざまなデータ片についてプログラムを抽象化するので、Paul Hudak は 1990 年代に、DSL が究極の抽象化であり、すなわち「抽象化」の考えを完成まで一般化したものだと論じた。

DSL の構築はしばしば上級プログラマの仕事とみなされるが、あなたはすでに、かなり複雑な DSL を理解し、評価し、実装する位置にいる。本節はそのすべてがどう働くかを説明する。まず有限状態機械（FSM）を改めて思い起こす。次に、任意の FSM をシミュレートするシステムを設定するための DSL をどう設計し、実装し、プログラムするかを示す。

**有限状態機械の再確認** 有限状態機械のテーマは計算において重要であり、本書はそれを何度も提示してきた。ここでは「有限状態機械」の例を、設定 DSL を設計・実装したいコンポーネントとして再利用する。

> **図129: Finite state machines, revisited**

```racket
; An FSM is a [List-of 1Transition]
; A 1Transition is a list of two items:
;   (cons FSM-State (cons FSM-State '()))
; An FSM-State is a String that specifies a color

; data examples
(define fsm-traffic
  '(("red" "green") ("green" "yellow") ("yellow" "red")))

; FSM-State FSM -> FSM-State
; matches the keys pressed by a player with the given FSM
(define (simulate state0 transitions)
  (big-bang state0 ; FSM-State
    [to-draw
      (lambda (current)
        (square 100 "solid" current))]
    [on-key
      (lambda (current key-event)
        (find transitions current))]))

; [X Y] [List-of [List X Y]] X -> Y
; finds the matching Y for the given X in alist
(define (find alist x)
  (local ((define fm (assoc x alist)))
    (if (cons? fm) (second fm) (error "not found"))))
```

便宜のため、図 129 はコード全体を再び示す。ただしリストだけを使い、ISL+ の全能力を用いて再定式化してある。プログラムは二つのデータ定義、一つのデータ例、二つの関数定義——simulate と find——からなる。前章の関連プログラムと違い、ここでは遷移を二つの項目のリストとして表す：現在状態と次の状態である。

主関数 simulate は遷移表と初期状態を消費する。次に big-bang 式を評価し、各キーイベントに状態遷移で反応する。状態は色付き正方形として表示される。to-draw と on-key の節は、現在状態に加え実際のキーイベントを消費し、それぞれ画像または次の状態を生成する lambda 式で指定される。

シグネチャが示すように、補助関数 find は FSM 応用から完全に独立している。二つの項目のリストのリストと一つの項目を消費するが、項目の実際の性質はパラメータ経由で指定される。このプログラムの文脈では、X と Y は FSM-States を表し、find は遷移表と状態を消費して状態を生成する。関数本体は組み込みの assoc 関数を使い、仕事のほとんどを行う。assoc のドキュメントを調べ、local の本体が if 式を使う理由を理解せよ。

**練習問題 378.** 描画関数を修正し、色付き正方形の上に状態の名前を重ねて描くようにせよ。

**練習問題 379.** find のテストケースを定式化せよ。

**練習問題 380.** 1Transition のデータ定義を書き直し、遷移を特定のキーストロークに制限できるようにせよ。find が変更なしで働き続けるよう変更を定式化せよ。完全なプログラムを動かすには他に何を変える必要があるか？設計レシピのどの部分が答えを与えるか？元の練習問題の文は練習問題 229 を見よ。

**設定** FSM シミュレーション関数は二つの引数を使い、それらが共同で機械を記述する。潜在的な「顧客」に、DrRacket で ISL+ プログラムを開いて二つの引数の関数を起動する方法を教える代わりに、simulate の「売り手」はこの製品に設定コンポーネントを添えたいかもしれない。

設定コンポーネントは二つの部分からなる。第一は、顧客がコンポーネントの主関数（たち）の初期引数を定式化するのに使う、広く使われる単純な言語である。第二は、顧客の言ったことを主関数の関数呼び出しに翻訳する関数である。FSM シミュレータについては、有限状態機械を XML でどう表すかに合意しなければならない。慎重な計画により、「S式としての XML」は課題にまさに適した一連の機械例を提示する。本節の最後の `machine` 例を思い出してほしい：

> `<machine initial="red">` `<action state="red"` `next="green" />` `<action state="green"` `next="yellow" />` `<action state="yellow" next="red" />``</machine>`

図 129 の遷移表 fsm-traffic と比較せよ。また、合意したこの例の Xexpr 表現を思い出してほしい：

```racket
(define xm0
  '(machine ((initial "red"))
     (action ((state "red") (next "green")))
     (action ((state "green") (next "yellow")))
     (action ((state "yellow") (next "red")))))
```

まだ欠けているのは、FSM の可能なすべての Xexpr 表現を記述する一般的なデータ定義である：

```racket
; An XMachine is a nested list of this shape:
;   (cons 'machine (cons `((initial,FSM-State))  [List-of X1T]))
; An X1T is a nested list of this shape:
;   `(action ((state,FSM-State) (next,FSM-State)))
```

XEnum.v2 と同様、XMachine はすべての Xexpr の部分集合を記述する。したがって、この新しい形のデータを処理する関数を設計するとき、汎用の Xexpr 関数を使って断片にアクセスし続けてよい。

**練習問題 381.** XMachine と X1T の定義は quote を使うが、これは初心のプログラム設計者にはきわめて不適切である。まず list を使うよう書き直し、次に cons を使うよう書き直せ。

**練習問題 382.** 白から黒へ、そしてキーイベントごとに戻る BW 機械の XML 設定を定式化せよ。XML 設定を XMachine 表現に翻訳せよ。プログラムとしての機械の実装は練習問題 227 を見よ。

設定問題の翻訳部分に潜る前に、それを明確に述べよう：

> サンプル問題 XMachine 設定を使って simulate を動かすプログラムを設計せよ。

この問題は我々のケースに特有だが、類似のシステムへの一般化を想像するのは簡単であり、そうすることを勧める。

問題文は完全な骨組みを示唆する：

```racket
; XMachine -> FSM-State
; simulates an FSM via the given configuration
(define (simulate-xmachine xm)
  (simulate......))
```

問題文に従い、我々の関数はこれから決める二つの引数で simulate を呼ぶ。定義を完成させるには二つの断片が要る：初期状態と遷移表である。これら二つの断片は xm の一部であり、適切な関数を願うのが最善である：

- xm-state0 は与えられた XMachine から初期状態を取り出す：
(check-expect (xm-state0 xm0) "red")
- xm->transitions は埋め込まれた X1T のリストを 1Transition のリストに翻訳する：
(check-expect (xm->transitions xm0) fsm-traffic)

> **図130: Interpreting a DSL program**

```racket
; XMachine -> FSM-State
; interprets the given configuration as a state machine
(define (simulate-xmachine xm)
  (simulate (xm-state0 xm) (xm->transitions xm)))

; XMachine -> FSM-State
; extracts and translates the transition table from xm0

(check-expect (xm-state0 xm0) "red")

(define (xm-state0 xm0)
  (find-attr (xexpr-attr xm0) 'initial))

; XMachine -> [List-of 1Transition]
; extracts the transition table from xm

(check-expect (xm->transitions xm0) fsm-traffic)

(define (xm->transitions xm)
  (local (; X1T -> 1Transition
          (define (xaction->action xa)
            (list (find-attr (xexpr-attr xa) 'state)
                  (find-attr (xexpr-attr xa) 'next))))
    (map xaction->action (xexpr-content xm))))
```

XMachine は Xexpr の部分集合なので、xm-state0 の定義は簡単である。初期状態は属性として指定されるので、xm-state0 は xexpr-attr を使って属性のリストを取り出し、次に 'initial 属性の値を取り出す。

次に xm->transitions に移ろう。これは XMachine 設定の内側の遷移を遷移表に翻訳する：

```racket
; XMachine -> [List-of 1Transition]
; extracts & translates the transition table from xm
(define (xm->transitions xm)
 '())
```

関数の名前がシグネチャを規定し、目的文を示唆する。我々の目的文は二段階の過程を記述する：(1) 遷移の Xexpr 表現を取り出し、(2) それらを [List-of 1Transition] のインスタンスに翻訳する。

取り出し部分が xexpr-content を使ってリストを得るのは明らかだが、翻訳部分にはもう少し分析が要る。XMachine のデータ定義に戻ると、Xexpr の内容は X1T のリストである。シグネチャは、遷移表が 1Transition のリストだと教える。実際、前者のリストの各項目が後者の一つの項目に翻訳されるのはかなり明らかであり、map の使用を示唆する：

```racket
(define (xm->transitions xm)
  (local (; X1T -> 1Transition
          (define (xaction->action xa)
...))
    (map xaction->action (xexpr-content xm))))
```

見てのとおり、「例による抽象化の利用」の設計の考えに従い、関数を map を本体で使う local として定式化する。xaction->action の定義は再び、Xexpr から適切な値を取り出す問題にすぎない。

図 130 は完全な解を示す。ここでは DSL から適切な関数呼び出しへの翻訳が、元のコンポーネントと同じくらい大きい。現実世界のシステムではそうではない。DSL コンポーネントは製品全体の小さな割合になる傾向があり、だからこのアプローチは人気がある。

**練習問題 383.** 図 130 のコードを、練習問題 382 の BW 機械設定で実行せよ。

> **図131: A file with a machine configuration**

```
machine-configuration.xml
<machine initial="red">
<action state="red"
next="green" />
<action state="green"
next="yellow" />
<action state="yellow" next="red" />
</machine>
```

### 22.4 XML の読み取り（Reading XML）

システム管理者は、洗練されたアプリケーションが設定プログラムをファイルから、あるいは Web 上のどこかから読むことを期待する。ISL+ では、プログラムが（ある）XML 情報を取得できる。図 132 はティーチパックからの関連する抜粋を示す。一貫性のため、図は XML 表現に `.v3` 接尾辞を使い、バージョン 2 がないデータ定義も含む：

> **注:** 本節は
2htdp/batch-io
2htdp/universe、および
2htdp/image ティーチパックを使う。

```racket
; An Xexpr.v3 is one of:
;  – Symbol
;  – String
;  – Number
;  – (cons Symbol (cons Attribute*.v3 [List-of Xexpr.v3]))
;  – (cons Symbol [List-of Xexpr.v3])
;
; An Attribute*.v3 is a [List-of Attribute.v3].
;
; An Attribute.v3 is a list of two items:
;   (list Symbol String)
```

> **図132: Reading X-expressions**

```racket
; Any -> Boolean
; is x an Xexpr.v3
; effect displays bad piece if x is not an Xexpr.v3
(define (xexpr? x) ...)

; String -> Xexpr.v3
; produces the first XML element in file f
(define (read-xexpr f) ...)

; String -> Boolean
; #false, if this url returns a '404'; #true otherwise
(define (url-exists? u) ...)

; String -> [Maybe Xexpr.v3]
; retrieves the first XML (HTML) element from URL u
; #false if (not (url-exists? u))
(define (read-plain-xexpr/web u) ...)

; String -> [Maybe Xexpr.v3]
; retrieves the first XML (HTML) element from URL u
; #false if (not (url-exists? u))
(define (read-xexpr/web u) ...)
```

図 131 のファイルがあると仮定する。2htdp/batch-io ティーチパックが required されていれば、プログラムは read-plain-xexpr で要素を読める。関数は XMachine データ定義に合う形式で XML 要素を取り出す。Web から XML 要素を取り出す関数もティーチパックにある。DrRacket で次を試せ：

```racket
> (read-plain-xexpr/web
    (string-append
       "Https://Felleisen.org/"
       "matthias/"
       "HtDP2e/Files/machine-configuration.xml"))
```

コンピュータが Web に接続されていれば、この式は標準の機械設定を取り出す。

ファイルや Web ページの読み取りは、我々の計算モデルにまったく新しい考えを導入する。「インターメッツォ 1: Beginning Student Language」が説明するように、BSL プログラムは代数で変数式を評価するのと同じ仕方で評価される。関数定義も代数と同じように扱われる。実際、ほとんどの代数コースは条件付き関数定義を導入するので、cond も難問ではない。最後に、ISL+ は関数を値として導入するが、評価モデルは基本的に同じままである。

この計算モデルの本質的な性質の一つは、関数 f をある引数 a... に何度呼んでも

```racket
(f a...)
```

答えは同じままであることである。しかし read-file、read-xexpr、およびその親族の導入は、この性質を破壊する。問題は、ファイルと Web サイトが時間とともに変わり得るため、プログラムがファイルや Web サイトを読むたびに新しい結果を得るかもしれないことである。

会社の株価を調べる考えを考えてみよ。ブラウザを `google.com/finance` や他のそのような金融 Web サイトに向け、お気に入りの会社の名前、たとえば `Ford` を入力せよ。応答として、サイトは会社の株の現在価格と他の情報——たとえば前回掲載時からの価格変化、現在時刻、その他多くの事実と広告——を表示する。重要な点は、一日や一週間にわたってこのページを再読み込みすると、この Web ページ上の情報の一部が変わることである。

そのような会社情報を手動で調べる代わりに、たとえば 15 秒ごとにそのような情報を取り出す小さなプログラムを書くこともできる。ISL ではこの課題を行う world プログラムを書ける。次のように起動するだろう：

```racket
> (stock-alert "Ford")
```

すると、次のような画像を表示する world ウィンドウが見える：

> [image: pict_147.png]

そのようなプログラムを開発するには、通常のプログラム設計を超える技能が要る。第一に、Web サイトが情報をどう整形しているかを調べる必要がある。Google の金融サービスページの場合、Web ソースコードを検査すると、上部近くに次のパターンがある：

> `<meta content="17.09" itemprop="price" />` `<meta content="+0.07" itemprop="priceChange" />` `<meta content="0.41" itemprop="priceChangePercent" />` `<meta content="2013-08-12T16:59:06Z" itemprop="quoteTime" />` `<meta content="NYSE real-time data" itemprop="dataSource" />`

Xexpr.v3 を探索し、属性値 "price" と "priceChange" を持つ（XML の表現である）`meta` 要素を取り出せる関数があれば、stock-alert の残りは簡単である。

> **図133: Web data as an event**

```racket
(define PREFIX "Https://www.google.com/finance?q=")
(define SIZE 22) ; font size

(define-struct data [price delta])
; A StockWorld is a structure: (make-data String String)

; String -> StockWorld
; retrieves the stock price of co and its change every 15s
(define (stock-alert co)
  (local ((define url (string-append PREFIX co))
          ; [StockWorld -> StockWorld]
          (define (retrieve-stock-data __w)
            (local ((define x (read-xexpr/web url)))
              (make-data (get x "price")
                         (get x "priceChange"))))
          ; StockWorld -> Image
          (define (render-stock-data w)
            (local (; [StockWorld String -> String] -> Image
                    (define (word sel col)
                      (text (sel w) SIZE col)))
              (overlay (beside (word data-price 'black)
                               (text "  " SIZE 'white)
                               (word data-delta 'red))
                       (rectangle 300 35 'solid 'white)))))
    (big-bang (retrieve-stock-data 'no-use)
      [on-tick retrieve-stock-data 15]
      [to-draw render-stock-data])))
```

> **注:** この Web サービスがもはや株価を配信しないため、この練習問題を完成させることはもはやできない。

図 133 はプログラムの核を示す。get の設計は練習問題に残す。その働きはすべて絡み合ったデータについてだからである。

図が示すように、主関数は二つの局所関数を定義する：クロックティック・ハンドラと描画関数である。big-bang 仕様は、時計が 15 秒ごとに進むよう要求する。時計が進むと、ISL+ は retrieve-stock-data を現在の世界に適用するが、関数はそれを無視する。代わりに、関数は read-xexpr/web 経由で Web サイトを訪れ、get で適切な情報を取り出す。したがって新しい世界は、局所データからではなく、Web 上で新たに得られる情報から作られる。

**練習問題 384.** 図 133 は read-xexpr/web に言及する。図 132 でそのシグネチャと目的文を見、次にドキュメントを読んで「plain」の親族との違いを判定せよ。

図 133 にはまた、いくつかの重要な断片が欠けている。とくに data の解釈と、すべての局所定義関数の目的文である。欠けている断片を定式化し、プログラムを理解できるようにせよ。

**練習問題 385.** Google の金融サービスページで、お気に入りの会社の現在の株価を調べよ。会社を特に好まないなら Ford を選べ。次に、ページのソースコードを作業ディレクトリのファイルとして保存せよ。DrRacket で read-xexpr を使い、ソースを Xexpr.v3 として見よ。

**練習問題 386. get 関数は次のとおりである：**

```racket
; Xexpr.v3 String -> String
; retrieves the value of the "content" attribute
; from a 'meta element that has attribute "itemprop"
; with value s
(check-expect
  (get '(meta ((content "+1") (itemprop "F"))) "F")
  "+1")

(define (get x s)
  (local ((define result (get-xexpr x s)))
    (if (string? result)
        result
        (error "not found"))))
```

これは get-xexpr の存在を仮定する。get-xexpr は任意の Xexpr.v3 から望む属性を探し、[Maybe String] を生成する関数である。

"F" 以外の値を探すテストケースと、get にエラーを起こさせるテストケースを定式化せよ。

get-xexpr を設計せよ。この関数の機能例を get のものから導出せ。get-xexpr が任意の Xexpr.v3 を走査できると確信できるよう、これらの例を一般化せよ。最後に、練習問題 385 で保存した Web データを使うテストを定式化せよ。

## 23 同時処理（Simultaneous Processing）

いくつかの関数は、非自明なデータ定義を持つクラスに属する2つの引数を消費しなければならない。そのような関数をどう設計するかは、引数どうしの関係に依存する。第1に、引数の一方を原子的であるかのように扱わなければならないことがある。第2に、関数が2つの引数を足並みをそろえて（lockstep で）処理することがある。最後に、関数が与えられたデータを、可能なすべての場合に従って処理することがある。本章は3つの場合を例で示し、拡張された設計レシピを与える。最後の節では、複合データの等しさについて議論する。

### 23.1 2つのリストを同時に処理する：場合1（Processing Two Lists Simultaneously: Case 1）

次のシグネチャ、目的文、ヘッダを考えよ。

```racket
; [List-of Number] [List-of Number] -> [List-of Number]
; replaces the final '() in front with end
(define (replace-eol-with front end)
  front)
```

シグネチャは、関数が2つのリストを消費することを述べている。この場合に設計レシピがどう働くかを見てみよう。

例を通して作業するところから始める。第1引数が `'()` なら、`replace-eol-with` は第2引数が何であれそれを返さなければならない。

```racket
(check-expect (replace-eol-with '() '(a b)) '(a b))
```

対照的に、第1引数が `'()` でないなら、目的文は `front` の末尾の `'()` を `end` で置き換えることを求める。

```racket
(check-expect (replace-eol-with (cons 1 '()) '(a))
              (cons 1 '(a)))
(check-expect (replace-eol-with
                (cons 2 (cons 1 '())) '(a))
              (cons 2 (cons 1 '(a))))
```

目的文と例は、第2引数がリストであるかぎり、関数はそれについて何も知る必要がないことを示唆する。したがって、そのテンプレートは、第1引数に関するリスト処理関数のものであるべきだ。

```racket
(define (replace-eol-with front end)
  (cond
    [(empty? front)...]
    [else
     (... (first front)...
... (replace-eol-with (rest front) end)...)]))
```

設計レシピの第5ステップに従い、テンプレートの空白を埋めよう。`front` が `'()` なら、`replace-eol-with` は `end` を返す。`front` が `'()` でないなら、テンプレートの式が何を計算するかを思い出す必要がある。

- `(first front)` はリストの先頭の項目に評価され、
- `(replace-eol-with (rest front) end)` は `(rest front)` の末尾の `'()` を `end` で置き換える。

やめ！ 表の方法を使い、これらの箇条が進行中の例で何を意味するかを理解せよ。

ここから完全な定義までは小さな一歩である。

```racket
(define (replace-eol-with front end)
  (cond
    [(empty? front) end]
    [else
     (cons (first front)
           (replace-eol-with (rest front) end))]))
```

練習問題 387. `cross` を設計せよ。この関数は記号のリストと数のリストを消費し、記号と数の可能なすべての順序対を生成する。すなわち、`'(a b c)` と `'(1 2)` が与えられたとき、期待される結果は `'((a 1) (a 2) (b 1) (b 2) (c 1) (c 2))` である。

### 23.2 2つのリストを同時に処理する：場合2（Processing Two Lists Simultaneously: Case 2）

Functions that Produce Lists は関数 `wages*` を提示する。これは労働時間を与えられたいくつかの労働者の週給を計算する。週あたりの労働時間を表す数のリストを消費し、対応する週給である数のリストを生成する。この問題は、すべての従業員が同じ時給を受け取ると仮定しているが、小さな会社でさえ、労働者には差のある賃金を払う。

ここでは、もう少し現実的な版を見る。関数は今や2つのリストを消費する。労働時間のリストと、対応する時給のリストである。この改訂された問題を、改訂されたヘッダに翻訳する。

```racket
; [List-of Number] [List-of Number] -> [List-of Number]
; multiplies the corresponding items on
; hours and wages/h
; assume the two lists are of equal length
(define (wages*.v2 hours wages/h)
  '())
```

例を作るのは簡単である。

```racket
(check-expect (wages*.v2 '() '()) '())
(check-expect (wages*.v2 (list 5.65) (list 40))
              (list 226.0))
(check-expect (wages*.v2 '(5.65 8.75) '(40.0 30.0))
              '(226.0 262.5))
```

要求どおり、3つの例はすべて等しい長さのリストを使う。

入力に関する仮定は、テンプレートの開発にも利用できる。より具体的には、この条件は `(empty? hours)` が真のとき `(empty? wages/h)` も真であり、さらに `(cons? hours)` が真のとき `(cons? wages/h)` も真であることを述べる。したがって、2つのリストのうち一方についてのテンプレートを使うことが許される。

```racket
(define (wages*.v2 hours wages/h)
  (cond
    [(empty? hours)...]
    [else
     (... (first hours)
... (first wages/h)...
... (wages*.v2 (rest hours) (rest wages/h)))]))
```

最初の `cond` 節では、`hours` と `wages/h` はどちらも `'()` である。したがって選択子式は不要である。第2節では、`hours` と `wages/h` はどちらも構成されたリストであり、したがって4つの選択子式が必要である。最後に、最後の2つは等しい長さのリストなので、`wages*.v2` の自然な再帰の自然な候補になる。

このテンプレートの唯一の珍しい点は、再帰的適用が2つの式からなり、どちらも2つの引数についての選択子式であることである。しかし、この考え方は仮定から直接導かれる。

ここから完全な関数定義までは短い一歩である。

```racket
(define (wages*.v2 hours wages/h)
  (cond
    [(empty? hours) '()]
    [else
     (cons
       (weekly-wage (first hours) (first wages/h))
       (wages*.v2 (rest hours) (rest wages/h)))]))
```

最初の例は、最初の `cond` 節の答えが `'()` であることを含意する。第2節では、3つの値が利用できる。

1. `(first hours)`。これは週労働時間の最初の数を表す。
2. `(first wages/h)`。これは最初の時給である。
3. `(wages*.v2 (rest hours) (rest wages/h))`。目的文によれば、これは2つのリストの残りについての週給のリストを計算する。

あとは、これらの値を組み合わせて最終的な答えを得るだけである。例が示唆するように、最初の従業員の週給を計算し、その賃金と残りの賃金からリストを構成しなければならない。

```racket
(cons (weekly-wage (first hours) (first wages/h))
      (wages*.v2 (rest hours) (rest wages/h)))
```

補助関数 `weekly-wage` は、労働時間数と時給を使い、1人の労働者の週給を計算する。

```racket
; Number Number -> Number
; computes the weekly wage from pay-rate and hours
(define (weekly-wage pay-rate hours)
  (* pay-rate hours))
```

やめ！ 1人の労働者の賃金を計算したいなら、どの関数を使う必要があるか。所得税を扱いたいなら、どの関数を変更する必要があるか。

練習問題 388. 現実世界では、`wages*.v2` は従業員構造体のリストと勤務記録のリストを消費する。従業員構造体は、従業員の名前、社会保障番号、時給を含む。勤務記録も、従業員の名前と1週間の労働時間数を含む。結果は、従業員の名前と週給を含む構造体のリストである。

この節のプログラムを修正し、これらの現実的な版のデータで動くようにせよ。必要な構造体型定義とデータ定義を与えよ。修正過程を導くために設計レシピを使え。

**練習問題 389. `zip` 関数を設計せよ。これは名前のリスト（文字列として表現）と、同じく文字列である電話番号のリストを消費する。等しい長さのそれらのリストを、電話記録のリストに組み合わせる。**

```racket
(define-struct phone-record [name number])
; A PhoneRecord is a structure:
;   (make-phone-record String String)
```

対応するリスト項目は同一人物に属すると仮定せよ。

### 23.3 2つのリストを同時に処理する：場合3（Processing Two Lists Simultaneously: Case 3）

ここに第3の種類の問題がある。

> 見本問題 記号のリスト `los` と自然数 `n` が与えられたとき、関数 `list-pick` は `los` から n 番目の記号を取り出す。そのような記号がなければ、エラーを合図する。

問題は、`list-pick` の設計にレシピがどれほどよく働くかである。

記号のリストのデータ定義は今ではかなり馴染みがある一方、Natural Numbers からの自然数のクラスを思い出せ。

```racket
; N is one of:
; – 0
; – (add1 N)
```

これで第2ステップに進める。

```racket
; [List-of Symbol] N -> Symbol
; extracts the nth symbol from l;
; signals an error if there is no such symbol
(define (list-pick l n)
  'a)
```

記号のリストも自然数も、複雑なデータ定義を持つクラスである。この組み合わせは問題を非標準的にし、設計レシピのあらゆるステップのあらゆる細部に注意を払わなければならないことを意味する。

この時点では通常、いくつかの入力例を選び、望ましい出力が何かを明らかにする。関数が完璧に働かなければならない入力から始める。`'(a b c)` と `2` である。3つの記号のリストと添字 `2` について、`list-pick` は記号を返さなければならない。問題は、それが `'b` か `'c` かである。小学校なら、1、2と数え、考えもせず `'b` を選んだだろう。しかしこれは計算機科学であり、小学校ではない。ここでは人々は 0 から数え始める。つまり `'c` も同様に適切な選択である。そして実際、私たちが使うのはこの選択である。

```racket
(check-expect (list-pick '(a b c) 2) 'c)
```

`list-pick` のこの細点を排除したので、実際の問題、すなわち入力の選択を見よう。例のステップの目標は、入力空間をできるだけ多く覆うことである。そのために、複雑な形のデータの記述の各節につき1つの入力を選ぶ。ここではこの手続きは、各データ定義が2つの節を持つので、各クラスから少なくとも2つの要素を選ぶことを示唆する。第1引数には `'()` と `(cons 'a '())` を、後者には `0` と `3` を選ぶ。引数ごとに2つの選択は、合計4つの例を意味する。結局のところ、2つの引数のあいだにすぐ明らかなつながりはなく、シグネチャに制限もない。

実際のところ、これらの組み合わせのうち適切な結果を生むのは1つだけである。残りは、リストに十分な記号が含まれないため、存在しない位置を選ぶ。

```racket
(check-error (list-pick '() 0) "list too short")
(check-expect (list-pick (cons 'a '()) 0) 'a)
(check-error (list-pick '() 3) "list too short")
```

関数はエラーを合図することが期待され、ここでお気に入りのメッセージを選ぶ。

やめ！ これらの断片を DrRacket の定義領域に置き、部分的なプログラムを実行せよ。

例についての議論は、関数の設計のために調べなければならない独立した場合が実際に4つあることを示す。これらの場合を発見する1つの方法は、各節の条件を2次元の表に並べることである。

> (empty?l) (cons?l) (=n0) (>n0)

表の水平方向は、`list-pick` がリストについて尋ねなければならない問いを列挙する。垂直方向は自然数についての問いを列挙する。この配置により、自然に4つのマスができ、各マスは水平軸と垂直軸の条件がどちらも真である場合を表す。

私たちの表は、関数テンプレートの `cond` が4つの節を持つことを示唆する。これらの各節の適切な条件は、表の各マスについて水平と垂直の条件を `and` で結ぶことでわかる。

> (empty?l) (cons?l) (=n0) (and (empty? l) (= n 0)) (and (cons? l) (= n 0))(>n0) (and (empty? l) (> n 0)) (and (cons? l) (> n 0))

テンプレートの `cond` の輪郭は、この表を条件式に翻訳したものにすぎない。

```racket
(define (list-pick l n)
  (cond
    [(and (= n 0) (empty? l))...]
    [(and (> n 0) (empty? l))...]
    [(and (= n 0) (cons? l))...]
    [(and (> n 0) (cons? l))...]))
```

いつものように、`cond` 式は4つの可能性を区別し、各 `cond` 節に選択子式を追加するときに、それぞれに個別に焦点を当てることを許す。

```racket
(define (list-pick l n)
  (cond
    [(and (= n 0) (empty? l))
...]
    [(and (> n 0) (empty? l))
     (... (sub1 n)...)]
    [(and (= n 0) (cons? l))
     (... (first l)... (rest l)...)]
    [(and (> n 0) (cons? l))
     (... (sub1 n)... (first l)... (rest l)...)]))
```

第1引数 `l` はリストであり、非空リストについてのテンプレートの `cond` 節は2つの選択子式を含む。第2引数 `n` は `N` に属し、0 でない数についてのテンプレートの `cond` 節は選択子式を1つだけ必要とする。`(empty? l)` または `(= n 0)` が成り立つ場合、それぞれの引数は原子的であり、対応する選択子式は不要である。

テンプレート構成の最終ステップは、選択子式の結果が入力と同じクラスに属するところに再帰で注釈を付けることを求める。この最初の例では、両方の引数についての選択子式を含む最後の `cond` 節に焦点を当てる。しかし、自然な再帰をどう形成するかははっきりしない。関数の目的を無視すれば、可能な再帰は3つある。

1. `(list-pick (rest l) (sub1 n))`
2. `(list-pick l (sub1 n))`
3. `(list-pick (rest l) n)`

それぞれが、利用可能な式の実行可能な組み合わせを表す。どれが重要か、あるいは3つすべてが重要かはわからないので、次の開発段階に進む。

> **図134: Indexing into a list**

```racket
; [List-of Symbol] N -> Symbol
; extracts the nth symbol from l;
; signals an error if there is no such symbol
(define (list-pick l n)
  (cond
    [(and (= n 0) (empty? l))
     (error 'list-pick "list too short")]
    [(and (> n 0) (empty? l))
     (error 'list-pick "list too short")]
    [(and (= n 0) (cons? l)) (first l)]
    [(and (> n 0) (cons? l)) (list-pick (rest l) (sub1 n))]))
```


設計レシピの第5ステップに従い、テンプレートの各 `cond` 節を分析し、適切な答えが何かを決めよう。

1. `(and (= n 0) (empty? l))` が成り立つなら、`list-pick` は空リストから最初の記号を取り出さなければならず、それは不可能である。答えはエラー信号でなければならない。
2. `(and (> n 0) (empty? l))` が成り立つなら、`list-pick` は再び空リストから記号を取り出すよう求められる。
3. `(and (= n 0) (cons? l))` が成り立つなら、`list-pick` は `l` から最初の記号を生成することになっている。選択子式 `(first l)` が答えである。
4. `(and (> n 0) (cons? l))` が成り立つなら、利用可能な式が何を計算するかを分析しなければならない。見てきたように、このステップでは既存の例を通して作業するのがよい考えである。最初の例の短縮版を選ぶ。
`(check-expect (list-pick '(a b) 1) 'b)` これらの値について、3つの自然な再帰が計算するものは次のとおりである。
`(list-pick '(b) 0)` は `'b` を生成する。`(list-pick '(a b) 0)` は `'a` に評価され、これは誤った答えである。そして `(list-pick '(b) 1)` はエラーを合図する。これから、`(list-pick (rest l) (sub1 n))` が最後の `cond` 節で望ましい答えを計算すると結論する。

**練習問題 390. 関数 `tree-pick` を設計せよ。この関数は記号の木と方向のリストを消費する。**

```racket
(define-struct branch [left right])

; A TOS is one of:
; – Symbol
; – (make-branch TOS TOS)

; A Direction is one of:
; – 'left
; – 'right

; A list of Directions is also called a path.
```

明らかに `Direction` は、関数に記号でない木で左の枝か右の枝かを選ぶかを伝える。`tree-pick` 関数の結果は何か。完全なシグネチャを定式化するのを忘れるな。関数は、記号と非空の道が与えられたときエラーを合図する。

### 23.4 関数の単純化（Function Simplification）

図134の `list-pick` 関数は、必要以上にずっと複雑である。最初の2つの `cond` 節はエラーを合図する。すなわち、

```racket
(and (= n 0) (empty? alos))
```

または

```racket
(and (> n 0) (empty? alos))
```

のどちらかが成り立つなら、答えはエラーである。この観察をコードに翻訳できる。

```racket
(define (list-pick alos n)
  (cond
    [(or (and (= n 0) (empty? alos))
         (and (> n 0) (empty? alos)))
     (error 'list-pick "list too short")]
    [(and (= n 0) (cons? alos)) (first alos)]
    [(and (> n 0) (cons? alos))
     (list-pick (rest alos) (sub1 n))]))
```

この関数をさらに単純化するには、ブールについての代数法則に親しむ必要がある。

> **注:** これらの等式はド・モルガンの法則（de Morgan’s laws）として知られる。

> (or (and bexp1 a-bexp) (and bexp2 a-bexp)) == (and (or bexp1 bexp2) a-bexp)

`and` の部分式が入れ替わった場合にも同様の法則が当てはまる。これらの法則を `list-pick` に適用すると次が得られる。

```racket
(define (list-pick n alos)
  (cond
    [(and (or (= n 0) (> n 0)) (empty? alos))
     (error 'list-pick "list too short")]
    [(and (= n 0) (cons? alos)) (first alos)]
    [(and (> n 0) (cons? alos))
     (list-pick (rest alos) (sub1 n))]))
```

さて `(or (= n 0) (> n 0))` を考えよ。`n` は `N` に属するので、これは常に `#true` である。`(and #true (empty? alos))` は `(empty? alos)` と同等なので、関数を再び書き直せる。

```racket
(define (list-pick alos n)
  (cond
    [(empty? alos) (error 'list-pick "list too short")]
    [(and (= n 0) (cons? alos)) (first alos)]
    [(and (> n 0) (cons? alos))
     (list-pick (rest alos) (sub1 n))]))
```

この最後の定義は、図134の定義よりすでにかなり単純だが、これよりさらに良くできる。最新版の `list-pick` の第1条件を、第2と第3と比較せよ。最初の `cond` 節が `alos` が空であるすべての場合を除外するので、最後の2節の `(cons? alos)` は常に `#true` に評価される。条件を `#true` に置き換え、`and` 式を再び単純化すると、`list-pick` の3行版が得られる。

> **図135: Indexing into a list, simplified**

```racket
; list-pick: [List-of Symbol] N[>= 0] -> Symbol
; determines the nth symbol from alos, counting from 0;
; signals an error if there is no nth symbol
(define (list-pick alos n)
  (cond
    [(empty? alos) (error 'list-pick "list too short")]
    [(= n 0) (first alos)]
    [(> n 0) (list-pick (rest alos) (sub1 n))]))
```


図135は `list-pick` のこの単純化された版を示す。元のものよりはるかに単純だが、元のものを体系的に設計し、確立された代数法則で第1から第2へ変換できたことを理解することが重要である。したがって、この単純な版を信頼できる。関数の単純な版を直接見つけようとすると、遅かれ早かれ分析の中のある場合の世話を怠り、欠陥のあるプログラムを生み出すことが保証される。

練習問題 391. Processing Two Lists Simultaneously: Case 3 の戦略を使い、`replace-eol-with` を設計せよ。テストから始めよ。結果を体系的に単純化せよ。

練習問題 392. 練習問題390の関数 `tree-pick` を単純化せよ。

### 23.5 2つの複雑な入力を消費する関数の設計（Designing Functions that Consume Two Complex Inputs）

2つ（またはそれ以上）の複雑な引数を持つ関数を設計する適切なアプローチは、一般のレシピに従うことである。データ分析を行い、関連するデータのクラスを定義しなければならない。`List-of` のようなパラメータ付き定義や、`'(1 b &)` のような短縮例の使用が混乱させるなら、コンストラクタが明示的になるよう展開せよ。次に関数シグネチャと目的が必要である。この時点で先を考え、次の3つの状況のどれに直面しているかを決められる。

1. パラメータの一方が支配的な役割を果たすなら、関数に関するかぎり他方を原子的なデータ片と考える。
2. パラメータが同じ値のクラスの範囲にあり、同じサイズを持たなければならない場合がある。たとえば、2つのリストは同じ長さでなければならず、あるいは2つの Web ページは同じ長さで、一方に埋め込みページが含まれるところでは他方にも含まれる、などである。2つのパラメータがこの対等な地位を持ち、目的がそれらを同期して処理することを示唆するなら、一方のパラメータを選び、その周りに関数を組織し、他方を並行してたどる。
3. 2つのパラメータのあいだに明らかなつながりがなければ、例ですべての可能な場合を分析しなければならない。そしてこの分析を使い、テンプレート、とくに再帰的な部分を開発する。

関数が第3の範疇に入ると決めたら、どの場合も漏れないよう2次元の表を開発する。この考えを再び説明するため、非自明なデータ定義の対を使おう。

>;AnLOD is one of:;–'();–(consDirectionLOD);ATID is one of:;–Symbol;–(make-binaryTIDTID);–(make-withTIDSymbolTID)

左のデータ定義はいつものリスト定義であり、右のものは `TOS` の3節変種である。2つの構造体型定義を使う。

```racket
(define-struct with [lft info rght])
(define-struct binary [lft rght])
```

関数が `LOD` と `TID` を消費すると仮定すると、思い浮かぶべき表は次の形である。

> (empty?l) (cons?l) (symbol?t) (binary?t) (with?t)

水平方向には第1パラメータ、ここでは `LOD`、の部分クラスを認識する条件を列挙し、垂直方向には第2パラメータ `TID` の条件を列挙する。

表は、関数の例と関数テンプレートの両方の開発を導く。説明したように、例は可能なすべての場合を覆わなければならない。すなわち、表の各セルにつき少なくとも1つの例がなければならない。同様に、テンプレートはセルごとに1つの `cond` 節を持たなければならない。その条件は、水平と垂直の条件を `and` 式で組み合わせる。各 `cond` 節は、順に、両方のパラメータについての実行可能なすべての選択子式を含まなければならない。パラメータの一方が原子的なら、選択子式は不要である。最後に、実行可能な自然な再帰を意識する必要がある。一般に、選択子式（および任意で原子的な引数）の可能なすべての組み合わせが、自然な再帰の候補である。どれが必要でどれがそうでないかはわからないので、コーディングのステップのためにそれらを心に留めておく。

要約すると、複数パラメータ関数の設計は、古い設計レシピの主題の変奏にすぎない。鍵となる考えは、データ定義を、実行可能で興味深いすべての組み合わせを示す表に翻訳することである。関数の例とテンプレートの開発は、表をできるだけ活用する。

### 23.6 指の体操：2つの入力（Finger Exercises: Two Inputs）

練習問題 393. 図62は有限集合についての2つのデータ定義を提示する。選んだ有限集合の表現について `union` 関数を設計せよ。2つの集合を消費し、両方の要素を含む1つを生成する。

同じ集合表現について `intersect` を設計せよ。2つの集合を消費し、両方に現れる要素だけからなる集合を生成する。

練習問題 394. `merge` を設計せよ。この関数は、昇順にソートされた2つの数のリストを消費する。両方の入力リスト上のすべての数を含む、1つのソートされた数のリストを生成する。ある数が出力に現れる回数は、2つの入力リスト上に現れる回数の合計である。

練習問題 395. `take` を設計せよ。リスト `l` と自然数 `n` を消費する。`l` から最初の `n` 個の項目を生成するか、`l` が短すぎるなら `l` 全体を生成する。

`drop` を設計せよ。リスト `l` と自然数 `n` を消費する。結果は、最初の `n` 個の項目を除いた `l`、または `l` が短すぎるならただの `'()` である。

> **図136: A simple hangman game**

```racket
; An HM-Word is a [List-of Letter or "_"]
; interpretation "_" represents a letter to be guessed

; HM-Word N -> String
; runs a simplistic hangman game, produces the current state
(define (play the-pick time-limit)
  (local ((define the-word  (explode the-pick))
          (define the-guess (make-list (length the-word) "_"))
          ; HM-Word -> HM-Word
          (define (do-nothing s) s)
          ; HM-Word KeyEvent -> HM-Word
          (define (checked-compare current-status ke)
            (if (member? ke LETTERS)
                (compare-word the-word current-status ke)
                current-status)))
    (implode
     (big-bang the-guess ; HM-Word
       [to-draw render-word]
       [on-tick do-nothing 1 time-limit]
       [on-key  checked-compare]))))

; HM-Word -> Image
(define (render-word w)
  (text (implode w) 22 "black"))
```


練習問題 396. ハングマンはよく知られた当てものゲームである。一方の選手が語を選び、他方の選手はその語が何文字含むかを知らされる。後者は文字を選び、選ばれた語にその文字が現れるか、どこに現れるかを最初の選手に尋ねる。合意した時間またはラウンド数のあとでゲームは終わる。

図136は、時間制限付き版のゲームの本質を示す。`checked-compare` が局所的に定義される理由については Local Definitions Add Expressive Power を見よ。

この練習問題の目標は、中心的な関数 `compare-word` を設計することである。当てるべき語、当て手が見つけた多寡を表す語 `s`、および現在の推測を消費する。関数は、推測が文字を明らかにしたところの `"_"` をすべて置き換えた `s` を生成する。

関数を設計したら、次のようにプログラムを実行せよ。

```racket
(define LOCATION "/usr/share/dict/words"); on OS X
(define AS-LIST (read-lines LOCATION))
(define SIZE (length AS-LIST))
(play (list-ref AS-LIST (random SIZE)) 10)
```

説明は図74を見よ。楽しんで、望むように洗練せよ！

練習問題 397. 工場では、従業員は朝の到着時と夕方の退社時にタイムカードを打つ。電子タイムカードは従業員番号を含み、週あたりの労働時間数を記録する。従業員記録は常に、従業員の名前、従業員番号、時給を含む。

`wages*.v3` を設計せよ。この関数は従業員記録のリストとタイムカード記録のリストを消費する。従業員の名前と週給を含む賃金記録のリストを生成する。タイムカードに対応する従業員記録が見つからない場合、またはその逆の場合、関数はエラーを合図する。

仮定 従業員番号あたりタイムカードは高々1つである。

**練習問題 398. 線形結合は、多くの線形項の和である。すなわち、変数と数の積の和である。後者はこの文脈では係数と呼ばれる。いくつかの例を示す。**

> [image: pict_148.png] [image: pict_149.png] [image: pict_150.png]

すべての例で、`x` の係数は 5、`y` のそれは 17、`z` のそれは 3 である。

変数の値が与えられれば、多項式の値を決められる。たとえば、`x = 10` なら、[image: pict_151.png] の値は 50 である。`x = 10` かつ `y = 1` なら、[image: pict_152.png] の値は 67 である。そして `x = 10`、`y = 1`、`z = 2` なら、[image: pict_153.png] の値は 73 である。

線形結合には多くの異なる表現がある。たとえば、関数で表現できる。別の表現は係数のリストである。上の結合は次のように表現される。

```racket
(list 5)
(list 5 17)
(list 5 17 3)
```

この表現の選択は、変数の固定された順序を仮定する。

`value` を設計せよ。この関数は等しい長さの2つのリストを消費する。線形結合と変数の値のリストである。これらの値について結合の値を生成する。

練習問題 399. Louise、Jane、Laura、Dana、Mary は、各自に1人の贈り物の受け手を割り当てるくじを行うことに決めた。Jane は開発者なので、偏りなくこの仕事を行うプログラムを書いてくれと頼む。もちろん、プログラムは姉妹の誰かを自分自身に割り当ててはならない。

Jane のプログラムの核心は次のとおりである。

```racket
; [List-of String] -> [List-of String]
; picks a random non-identity arrangement of names
(define (gift-pick names)
  (random-pick
    (non-same names (arrangements names))))

; [List-of String] -> [List-of [List-of String]]
; returns all possible permutations of names
; see exercise 213
(define (arrangements names)
...)
```

名前のリストを消費し、元のリストとどの位置でも一致しない順列のうち1つをランダムに選ぶ。

あなたの課題は、2つの補助関数を設計することである。

```racket
; [NEList-of X] -> X
; returns a random item from the list
(define (random-pick l)
  (first l))

; [List-of String] [List-of [List-of String]]
; ->
; [List-of [List-of String]]
; produces the list of those lists in ll that do
; not agree with names at any place
(define (non-same names ll)
  ll)
```

`random` が乱数を選ぶことを思い出せ。練習問題99を見よ。

練習問題 400. 関数 `DNAprefix` を設計せよ。この関数は2つの引数を取る。どちらも DNA の記述に現れる `'a`、`'c`、`'g`、`'t` のリストである。第1のリストはパターン、第2は探索文字列と呼ばれる。関数は、パターンが探索文字列の先頭部分と同一なら `#true` を返し、そうでなければ `#false` を返す。

また `DNAdelta` を設計せよ。この関数は `DNAprefix` に似ているが、パターンを超えた探索文字列の最初の項目を返す。リストが同一で、パターンを超えた DNA 文字がないなら、関数はエラーを合図する。パターンが探索文字列の先頭と一致しないなら、`#false` を返す。関数はどちらのリストも1回より多くたどってはならない。

`DNAprefix` または `DNAdelta` を単純化できるか。

**練習問題 401. 2つの S式が等しいかどうかを判定する関数 `sexp=?` を設計せよ。便宜のため、凝縮した形のデータ定義を示す。**

```racket
; An S-expr (S-expression) is one of:
; – Atom
; – [List-of S-expr]
;
; An Atom is one of:
; – Number
; – String
; – Symbol
```

`check-expect` を使うときはいつでも、2つの任意の値が等しいかどうかを調べるために `sexp=?` のような関数を使う。等しくなければ検査は失敗し、`check-expect` はそれをそのように報告する。

練習問題 402. 練習問題354を読み直せ。与えられた式をまず原子的な値と考えるという私たちのヒントの背後にある推論を説明せよ。

### 23.7 プロジェクト：データベース（Project: Database）

多くのソフトウェア応用は、データを追跡するためにデータベースを使う。大まかに言えば、データベースは、明示的に述べられた組織規則を伴う表である。前者は内容（content）であり、後者はスキーマ（schema）と呼ばれる。図137は2つの例を示す。各表は2つの部分からなる。線の上のスキーマと、下の内容である。

> **注:** この節は、本書の4つの部すべての知識を引き合わせる。

左の表に焦点を当てよう。3つの列と4つの行がある。各列には2部からなる規則が付く。

1. 左端の列の規則は、列のラベルが「Name」であり、この列のあらゆるデータ片が `String` であることを述べる。
2. 中央の列は「Age」とラベルされ、`Integer` を含む。
3. 右端のもののラベルは「Present」である。その値は `Boolean` である。

やめ！ 右の表を同じ仕方で説明せよ。

> **図137: Databases as tables**

```
Name
Age
Present
String
Integer
Boolean
"Alice"
35
#true
"Bob"
25
#false
"Carol"
30
#true
"Dave"
32
#false
Present
Description
Boolean
String
#true
"presence"
#false
"absence"
```


計算機科学者はこれらの表を関係（relation）と考える。スキーマは、関係の列と行の個々のセルを指す用語を導入する。各行は固定個の値を関係づける。すべての行の集まりが関係全体をなす。この用語では、図137の左の表の最初の行は `"Alice"` を 35 と `#true` に関係づける。さらに、行の最初のセルは「Name」セル、2番目は「Age」セル、3番目は「Present」セルと呼ばれる。

この節では、構造体とリストでデータベースを表現する。

```racket
(define-struct db [schema content])
; A DB is a structure: (make-db Schema Content)

; A Schema is a [List-of Spec]
; A Spec is a [List Label Predicate]
; A Label is a String
; A Predicate is a [Any -> Boolean]

; A (piece of) Content is a [List-of Row]
; A Row is a [List-of Cell]
; A Cell is Any
; constraint cells do not contain functions

; integrity constraint In (make-db sch con),
; for every row in con,
; (I1) its length is the same as sch's, and
; (I2) its ith Cell satisfies the ith Predicate in sch
```

やめ！ 図137のデータベースを、選んだデータ表現に翻訳せよ。表の内容はすでに ISL+ のデータを使っていることに注意。

> **図138: Databases as ISL+ data**
> 左右対比（崩れた ASCII 枠を二重 fence に復元。コードは公式 HTML の RktBlk より）。

**左**

```racket
(define school-schema
  `(("Name"    ,string?)
    ("Age"     ,integer?)
    ("Present" ,boolean?)))
```

**右**

```racket
(define presence-schema
  `(("Present"     ,boolean?)
    ("Description" ,string?)))
```

**ブロック3**

```racket
(define school-content
  `(("Alice" 35 #true)
    ("Bob"   25 #false)
    ("Carol" 30 #true)
    ("Dave"  32 #false)))
```

**ブロック4**

```racket
(define presence-content
  `((#true  "presence")
    (#false "absence")))
```

**ブロック5**

```racket
(define school-db
  (make-db school-schema
           school-content))
```

**ブロック6**

```racket
(define presence-db
  (make-db presence-schema
           presence-content))
```


図138は、図137の2つの表を `DB` としてどう表現するかを示す。左側は、図137の左の表のスキーマ、内容、データベースを表現する。右側は右の表に対応する。簡潔のため、例は準引用（quasiquote）と非引用（unquote）の記法を使う。これが、さもなければ引用されたリストの中に `boolean?` のような値を含めることを許すことを思い出せ。この記法に居心地が悪ければ、これらの例を `list` で書き直せ。

練習問題 403. `Spec` は `Label` と `Predicate` をリストに組み合わせる。許容できるが、この選択は、固定個の情報片に構造体型を使うという私たちの指針に反する。

ここに代替のデータ表現がある。

```racket
(define-struct spec [label predicate])
; Spec is a structure: (make-spec Label Predicate)
```

この代替の定義を使い、図137のデータベースを表現せよ。

**整合性検査** データベースの利用は、その整合性に決定的に依存する。ここで「整合性」は、データ定義からの制約 (I1) と (I2) を指す。データベースの整合性を検査することは、明らかに関数の仕事である。

```racket
; DB -> Boolean
; do all rows in db satisfy (I1) and (I2)

(check-expect (integrity-check school-db) #true)
(check-expect (integrity-check presence-db) #true)

(define (integrity-check db)
  #false)
```

2つの制約の文言は、与えられたデータベースの内容のすべての行について、ある関数が `#true` を生成しなければならないことを示唆する。この考えをコードで表すには、`db` の内容に対する `andmap` の使用が求められる。

```racket
(define (integrity-check db)
  (local (; Row -> Boolean
          (define (row-integrity-check row)
...))
    (andmap row-integrity-check (db-content db))))
```

既存の抽象化の利用についての設計レシピに従い、テンプレートは `local` 定義経由で補助関数を導入する。

`row-integrity-check` の設計は次から始まる。

```racket
; Row -> Boolean
; does row satisfy (I1) and (I2)
(define (row-integrity-check row)
  #false)
```

いつものように、目的文を定式化する目標は問題を理解することである。ここでは、関数が2つの条件を検査すると述べる。2つの仕事が関わるとき、設計指針は関数と、その結果の組み合わせを求める。

```racket
(and (length-of-row-check row)
     (check-every-cell row))
```

これらの関数をウィッシュリストに加えよ。その名前が目的を伝える。

これらの関数を設計する前に、望ましい値を計算するために既存の原始操作を組み合わせられるかどうかを熟考しなければならない。たとえば、`(length row)` が `row` にいくつのセルがあるかを数えることを知っている。この方向にもう少し押し進めると、明らかに次が欲しい。

```racket
(= (length row) (length (db-schema db)))
```

この条件は、`row` の長さが `db` のスキーマの長さに等しいことを検査する。

同様に、`check-every-cell` は、行のすべてのセルについてある関数が `#true` を生成することを検査することを求める。再び、`andmap` が求められているように見える。

```racket
(andmap cell-integrity-check row)
```

`cell-integrity-check` の目的は明らかに制約 (I2) を検査することである。すなわち、

> 「i 番目の Cell が、`db` のスキーマの i 番目の Predicate を満たす」かどうか。

そしてここで行き詰まる。この目的文は、与えられたセルの `row` における相対位置を参照するからである。しかし `andmap` の要点は、`cell-integrity-check` をすべてのセルに一様に適用することである。

行き詰まったら、例を通して作業しなければならない。補助関数や局所関数については、主関数の例からこれらの例を導くのが最善である。`integrity-check` の最初の例は、`school-content` が整合性制約を満たすと主張する。明らかに `school-content` のすべての行は `school-schema` と同じ長さを持つ。問題は、次のような行がなぜ

```racket
(list "Alice" 35 #true)
```

対応するスキーマの述語を満たすかである。

```racket
(list (list "Name"    string?)
      (list "Age"     integer?)
      (list "Present" boolean?))
```

答えは、3つの述語の3つのセルへの適用がすべて真を生むことである。

```racket
> (string? "Alice")
#true
> (integer? 35)
#true
> (boolean? #true)
#true
```

ここから、関数がこれら2つのリスト——`db` のスキーマと与えられた行——を並行して処理しなければならないとわかるまで、あとわずかな一歩である。

練習問題 404. 関数 `andmap2` を設計せよ。2つの値から Boolean への関数 `f` と、等しい長さの2つのリストを消費する。結果も Boolean である。具体的には、2つのリストからの対応する値の対に `f` を適用し、`f` が常に `#true` を生成するなら、`andmap2` も `#true` を生成する。そうでなければ、`andmap2` は `#false` を生成する。要するに、`andmap2` は2つのリスト用の `andmap` である。

やめ！ 先を読む前に練習問題404を解け。

ISL+ に `andmap2` があれば、`row` についての第2の条件の検査は簡単だろう。

```racket
(andmap2 (lambda (s c) [(second s) c])
         (db-schema db)
         row)
```

与えられた関数は `db` のスキーマからの `Spec` `s` を消費し、第2位置の述語を取り出し、与えられた `Cell` `c` に適用する。述語が返すものが、`lambda` 関数の結果である。

再びやめ！ `[(second s) c]` を説明せよ。

実際のところ、ISL+ の `andmap` はすでに `andmap2` のようである。

```racket
(define (integrity-check db)
  (local (; Row -> Boolean
; does row satisfy (I1) and (I2)
          (define (row-integrity-check row)
            (and (= (length row)
                    (length (db-schema db)))
                 (andmap (lambda (s c) [(second s) c])
                         (db-schema db)
                         row))))
    (andmap row-integrity-check (db-content db))))
```

最後にもう一度やめ！ `integrity-check` が失敗しなければならないテストを開発せよ。

**式の巻き上げについての注** 私たちの `integrity-check` の定義は、いくつか問題を抱えている。見えるものも、見えないものもある。明らかに、関数は `db` のスキーマを2回取り出している。既存の `local` 定義があれば、定義を導入してこの重複を避けられる。

```racket
(define (integrity-check.v2 db)
  (local ((define schema (db-schema db))
; Row -> Boolean
; does row satisfy (I1) and (I2)
          (define (row-integrity-check row)
            (and (= (length row) (length schema))
                 (andmap (lambda (s c) [(second s) c])
                         schema
                         row))))
    (andmap row-integrity-check (db-content db))))
```

Local Definitions から、そのような式を持ち上げると、整合性検査の実行に必要な時間を短くできることがあると知っている。図100の `inf` の定義と同様、`integrity-check` の元の版は、明らかに同じままであるにもかかわらず、すべての単一行について `db` からスキーマを取り出す。

> **図139: The result of systematic expression hoisting**

```racket
(define (integrity-check.v3 db)
  (local ((define schema  (db-schema db))
          (define content (db-content db))
          (define width   (length schema))
          ; Row -> Boolean
          ; does row satisfy (I1) and (I2)
          (define (row-integrity-check row)
            (and (= (length row) width)
                 (andmap (lambda (s c) [(second s) c])
                         schema
                         row))))
    (andmap row-integrity-check content)))
```


用語 計算機科学者は「式を巻き上げる（hoisting an expression）」と話す。同様に、`row-integrity-check` 関数は、呼び出されるたびに `db` のスキーマの長さを決める。結果は常に同じである。したがって、この関数の性能を改善することに関心があるなら、`local` 定義を使い、データベース内容の幅に一度だけ名前を付けられる。図139は `(length schema)` を `row-integrity-check` の外に巻き上げた結果を示す。読みやすさのため、この最終定義は `db` の `content` フィールドにも名前を付ける。終わり

**射影と選択** プログラムはデータベースからデータを取り出す必要がある。取り出しの1種は内容の選択であり、Real-World Data: iTunes で説明される。取り出しのもう1種は、縮小されたデータベースを生成する。射影（projection）と呼ばれる。より具体的には、射影は与えられたデータベースから特定の列だけを残してデータベースを構成する。

射影の記述は次を示唆する。

```racket
; DB [List-of Label] -> DB
; retains a column from db if its label is in labels
(define (project db labels) (make-db '() '()))
```

射影の複雑さを考えると、まず例を通して作業するのが最善である。図137の左のデータベースから age 列を取り除きたいとしよう。表の観点では、この変換は次のように見える。

> the original database... eliminating the “Age” columnName Age PresentString Integer Boolean"Alice" 35 #true"Bob" 25 #false"Carol" 30 #true"Dave" 32 #false Name PresentString Boolean"Alice" #true"Bob" #false"Carol" #true"Dave" #false

例をテストとして明確に述べる自然な仕方は、図138を再利用する。

```racket
(define projected-content
  `(("Alice" #true)
    ("Bob"   #false)
    ("Carol" #true)
    ("Dave"  #false)))

(define projected-schema
  `(("Name",string?) ("Present",boolean?)))

(define projected-db
  (make-db projected-schema projected-content))
;  Stop! Read this test carefully. What's wrong?
(check-expect (project school-db '("Name" "Present"))
              projected-db)
```

> **図140: A template for project**

```racket
(define (project db labels)
  (local ((define schema  (db-schema db))
          (define content (db-content db))
          ; Spec -> Boolean
          ; does this spec belong to the new schema
          (define (keep? c) ...)
          ; Row -> Row
          ; retains those columns whose name is in labels
          (define (row-project row) ...))
    (make-db (filter keep? schema)
             (map row-project content))))
```


上のテンプレートを埋め、DrRacket でコードを実行すると、DrRacket がテストが成功するかどうかさえわかる前に、次のエラーメッセージが得られる。

> `first argument of equality cannot be a function`

Functions Are Values から、関数は無限に大きなオブジェクトであり、2つの関数が同じ引数に適用されたとき常に同じ結果を生成することを保証するのは不可能であることを思い出せ。したがって、テストケースを弱める。

```racket
(check-expect
  (db-content (project school-db '("Name" "Present")))
  projected-content)
```

テンプレートについては、再び既存の抽象化を再利用する。図140を見よ。`local` 式は2つの関数を定義する。1つは与えられたデータベースのスキーマを絞り込む `filter` 用、もう1つは内容を薄くする `map` 用である。加えて、関数は再び与えられたデータベースからスキーマと内容を取り出し、名前を付ける。

ウィッシュリストに移る前に、一歩下がって、既存の抽象化の2つの再利用に進む決定を研究しよう。シグネチャは、関数が構造体を消費し `DB` の要素を生成すると述べるので、

```racket
(local ((define schema (db-schema db))
        (define content (db-content db)))
  (make-db... schema...
... content...))
```

が明らかに求められる。新しいスキーマが古いスキーマから、新しい内容が古い内容から作られることも、簡単にわかる。さらに、`project` の目的文は、第2引数で言及されたラベルだけを残すことを求める。したがって、`filter` 関数は与えられたスキーマを正しく絞り込む。対照的に、行そのものは残り、ただしそれぞれがいくつかのセルを失う。したがって、`map` が内容を処理する適切な仕方である。

さて2つの補助関数の設計に移れる。`keep?` の設計は簡単である。完全な定義は次のとおりである。

```racket
; Spec -> Boolean
; does this spec belong to the new schema
(define (keep? c)
  (member? (first c) labels))
```

関数は `Spec` に適用される。`Spec` は `Label` と `Predicate` をリストに組み合わせる。前者が `labels` に属するなら、与えられた `Spec` は残される。

`row-project` の設計については、目標は、`content` の各 `Row` のうち、その名前が与えられた `labels` のメンバーである `Cell` を残すことである。上の例を通して作業しよう。4つの行は次のとおりである。

```racket
(list "Alice" 35 #true)
(list "Bob"   25 #false)
(list "Carol" 30 #true)
(list "Dave"  32 #false)
```

これらの各行は `school-schema` と同じ長さである。

```racket
(list "Name" "Age" "Present")
```

スキーマ内の名前が、与えられた行のセルの名前を決める。したがって、`row-project` は各行の第1と第3のセルを残さなければならない。なぜなら、与えられた `labels` にあるのはそれらの名前だからである。

`Row` は再帰的に定義されるので、`Cell` の内容とその名前のあいだのこの照合過程は、`row-project` がセルの内容とラベルに適用できる再帰的ヘルパー関数を求める。ウィッシュとして仕様を述べよう。

```racket
; Row [List-of Label] -> Row
; retains those cells whose corresponding element
; in names is also in labels
(define (row-filter row names) '())
```

このウィッシュを使い、`row-project` は一行ものになる。

```racket
(define (row-project row)
  (row-filter row (map first schema)))
```

`map` 式はセルの名前を取り出し、それらの名前が、一致するセルを取り出すために `row-filter` に渡される。

練習問題 405. 関数 `row-filter` を設計せよ。`project` の例から `row-filter` の例を構成せよ。

仮定 与えられたデータベースは整合性検査を通る。すなわち、各行はスキーマと同じ長さであり、したがってその名前のリストと同じ長さである。

図141はすべての断片をまとめる。関数 `project` には接尾辞 `.v1` が付く。いくつかの改善を求めるからである。次の練習問題は、それらのいくつかを実装するよう求める。

> **図141: Database projection**

```racket
(define (project.v1 db labels)
  (local ((define schema  (db-schema db))
          (define content (db-content db))

          ; Spec -> Boolean
          ; does this column belong to the new schema
          (define (keep? c)
            (member? (first c) labels))

          ; Row -> Row
          ; retains those columns whose name is in labels
          (define (row-project row)
            (row-filter row (map first schema)))

          ; Row [List-of Label] -> Row
          ; retains those cells whose name is in labels
          (define (row-filter row names)
            (cond
              [(empty? names) '()]
              [else
               (if (member? (first names) labels)
                   (cons (first row)
                     (row-filter (rest row) (rest names)))
                   (row-filter (rest row) (rest names)))])))
    (make-db (filter keep? schema)
             (map row-project content))))
```


練習問題 406. `row-project` 関数は、データベースの内容のすべての行についてラベルを再計算する。結果は関数呼び出しごとに異なるか。異ならないなら、式を巻き上げよ。

練習問題 407. `foldr` を使って `row-filter` を再設計せよ。そうしたら、`row-project` と `row-filter` を単一の関数に統合してよい。ヒント ISL+ の `foldr` 関数は2つのリストを消費し、並行して処理してよい。

最後の観察は、`row-project` がすべての単一セルについて、ラベルが `labels` のメンバーかどうかを検査することである。異なる行の同じ列のセルについて、結果は同じになる。したがって、この計算も関数の外に巻き上げるのが理にかなう。

この形の巻き上げは、単なる式の巻き上げよりやや難しい。基本的に、

```racket
(member? label labels)
```

の結果をすべての行について事前計算し、ラベルのリストの代わりに結果を関数に渡したい。すなわち、ラベルのリストを、対応する位置のセルを残すかどうかを示す Boolean のリストで置き換える。幸い、それらの Boolean を計算することは、スキーマに対する `keep?` の別の適用にすぎない。

```racket
(map keep? schema)
```

与えられたスキーマからいくつかの `Spec` を残し他を捨てる代わりに、この式はただ決定を集める。

> **図142: Database projection**

```racket
(define (project db labels)
  (local ((define schema  (db-schema db))
          (define content (db-content db))

          ; Spec -> Boolean
          ; does this column belong to the new schema
          (define (keep? c)
            (member? (first c) labels))

          ; Row -> Row
          ; retains those columns whose name is in labels
          (define (row-project row)
            (foldr (lambda (cell m c) (if m (cons cell c) c))
                   '()
                   row
                   mask))
          (define mask (map keep? schema)))
    (make-db (filter keep? schema)
             (map row-project content))))
```


図142は `project` の最終版を示し、直前の練習問題の解を統合する。また `local` を使い、`schema` と `content` を取り出して名前を付け、ある `Spec` のラベルを残す価値があるかを検査する `keep?` も定義する。残りの2つの定義は、上で論じた Boolean のリストを表す `mask` と、改訂版の `row-project` を導入する。後者は `foldr` を使い、与えられた `row` と `mask` を並行して処理する。

この改訂された `project` の定義を、図141の `project.v1` と比較せよ。最終定義は元の版より単純かつ高速である。体系的な設計と注意深い改訂が報われる。テスト・スイートは、改訂がプログラムの機能を壊さないことを保証する。

練習問題 408. 関数 `select` を設計せよ。データベース、ラベルのリスト、行についての述語を消費する。結果は、与えられた述語を満たす行のリストで、与えられたラベルの集合に射影されたものである。

練習問題 409. `reorder` を設計せよ。この関数はデータベース `db` と `Label` のリスト `lol` を消費する。`db` に似ているが、列が `lol` に従って並べ替えられたデータベースを生成する。ヒント `list-ref` について読め。

まず、`lol` がちょうど `db` の列のラベルからなると仮定せよ。設計を終えたら、`lol` が列より少ないラベルを含む場合や、`db` の列のラベルでない文字列を含む場合に、何を変える必要があるかを研究せよ。

練習問題 410. 関数 `db-union` を設計せよ。これはまったく同じスキーマを持つ2つのデータベースを消費し、このスキーマと両方の結合された内容を持つ新しいデータベースを生成する。関数は、まったく同じ内容を持つ行を除去しなければならない。

スキーマが各列の述語について一致すると仮定せよ。

練習問題 411. `join` を設計せよ。これは2つのデータベース `db-1` と `db-2` を消費する関数である。`db-2` のスキーマは、`db-1` のスキーマが終わるのとまったく同じ `Spec` で始まる。関数は、各行の最後のセルを `db-2` におけるそのセルの翻訳で置き換えることで、`db-1` からデータベースを作る。

ここに例がある。図137のデータベースを取れ。2つはこれらの練習問題の仮定を満たす。すなわち、第1のスキーマの最後の `Spec` は第2の最初の `Spec` に等しい。したがってそれらを結合できる。

> Name Age DescriptionString Integer String"Alice" 35 "presence""Bob" 25 "absence""Carol" 30 "presence""Dave" 32 "absence"

その翻訳は `#true` を `"presence"` に、`#false` を `"absence"` に写す。

ヒント (1) 一般に、第2のデータベースはセルを1つの値だけでなく、値の行に「翻訳」してよい。`"presence"` と `"absence"` の行に追加の項を加えることで例を修正せよ。

(2) セルを複数の行に「翻訳」することもある。その場合、過程は新しいデータベースに複数の行を加える。ここに第2の例がある。図137のものからわずかに異なるデータベースの対である。

> Name Age PresentString Integer Boolean"Alice" 35 #true"Bob" 25 #false"Carol" 30 #true"Dave" 32 #false Present DescriptionBoolean String#true "presence"#true "here"#false "absence"#false "there"

左のデータベースを右のものと結合すると、8行のデータベースが得られる。

> Name Age DescriptionString Integer String"Alice" 35 "presence""Alice" 35 "here""Bob" 25 "absence""Bob" 25 "there""Carol" 30 "presence""Carol" 30 "here""Dave" 32 "absence""Dave" 32 "there"

(3) 反復的洗練を使い問題を解け。第1の反復では、「翻訳」がセルあたり1行だけ見つかると仮定せよ。第2では、その仮定を落とせ。

**仮定についての注** この練習問題とこの節全体は、主に与えられたデータベースについての非形式的に述べられた仮定に依存する。ここで、`join` の設計は「`db-2` のスキーマが、`db-1` のスキーマが終わるのとまったく同じ `Spec` で始まる」と仮定する。現実には、データベース関数は Input Errors の精神での検査付き関数でなければならない。しかし、`checked-join` を設計することはあなたには不可能だろう。`db-1` のスキーマの最後の `Spec` と `db-2` の最初のものの比較は、関数の比較を求める。実用的な解については、データベースのテキストを見よ。

## 24 まとめ（Summary）

本書の第IV部は、多数の絡み合った定義を必要とするデータの記述を処理する関数の設計についてである。こうした形のデータは現実世界のどこにでも現れる。コンピュータのローカル・ファイルシステムから、World Wide Web、アニメーション映画で使われる幾何学的な形に至るまでである。この部を注意深く学んだあとには、設計レシピがこうした形のデータにも拡張できることを知っているはずだ。

1. プログラム・データの記述が、互いに参照し合う複数のデータ定義を求めるとき、設計レシピはテンプレートの同時開発を求める。データ定義ごとに1つである。データ定義 `A` がデータ定義 `B` を参照するなら、テンプレート function-for-A は、まったく同じ場所と仕方で function-for-B を参照する。それ以外では、設計レシピはこれまでどおり、関数ごとに機能する。
2. 関数が2種類の複雑なデータを処理しなければならないとき、3つの場合を区別する必要がある。第1に、関数は引数の一方をあたかも原子的であるかのように扱ってよい。第2に、2つの引数はまったく同じ構造を持つことが期待され、関数はそれらを完全に並行してたどる。第3に、関数は可能なすべての組み合わせを別々に扱わなければならないことがある。この場合、2次元の表を作る。一方の次元には一方のデータ定義からのあらゆる種類のデータを列挙し、他方の次元では第2の種類のデータを扱う。最後に、表のセルを使って、さまざまな場合の条件と答えを定式化する。

この部は、2つの複雑な引数に対する関数を扱った。もし関数が3つの複雑なデータ片を受け取る、そうしたまれな場合に出会ったら、3次元の表が（想像上でも）必要だとわかるだろう。

これで、キャリアの過程で出会う可能性の高い、構造的データのあらゆる形を見たことになる。細部は異なるだろうが。もし行き詰まったら、設計レシピを思い出せ。それが出発点を与えてくれる。

