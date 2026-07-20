# 付録 A: Quick — 絵で学ぶ Racket 入門

**原題:** Quick: An Introduction to Racket with Pictures  
**著者:** Matthew Flatt  
**原本:** `extracted/appendix/quick/original_markdown_00_index.md`

このチュートリアルは、絵を描くライブラリのひとつを使って、Racket プログラミング言語への短い入門を提供します。たとえ芸術的な目的で Racket を使うつもりがなくても、絵のライブラリは興味深く、理解を深める例を支えてくれます。結局のところ、一枚の絵は五百個の「hello world」に匹敵するのです。

同様に、例は DrRacket で実行することを想定しています。DrRacket は、たとえ最終的に Emacs や vi、その他のエディタで Racket を使うとしても、言語とシステムの感触をつかむいちばん速い方法です。

## 1 用意……

Racket をダウンロードしてインストールし、DrRacket を起動してください。

## 2 セット……

> **注:** DrRacket のドキュメントを見ると、DrRacket IDE の概要がわかります。

絵を描くには、まず絵用の関数を読み込む必要があります。それらはスライド発表を作るためのライブラリの一部です。次を **定義エリア**（DrRacket で見える上側のテキスト領域）にコピーしてください。

```racket
#lang slideshow
```

それから **Run** ボタンをクリックします。テキストキャレットが下側のテキスト領域——**対話エリア（interactions area）**——へ移るのが見えるはずです。

以前に DrRacket を使ったことがある場合は、Run をクリックする前に、メニュー **Language | Choose Language...** から「ソースに宣言された言語を使う」ように DrRacket をリセットする必要があるかもしれません。

## 3 スタート！

対話ウィンドウの `>` のあとに式を打ち、Enter を押すと、DrRacket はその式を評価して結果を表示します。式は単なる値でもよく、たとえば数値 `5` や文字列 `"art gallery"` です。

```racket
> 5
5
> "art gallery"
"art gallery"
```

式は関数呼び出しでもかまいません。関数を呼ぶには、関数名の前に開き括弧を置き、続けて引数となる式を書き、閉じ括弧を置きます。次のようにします。

```racket
> (circle 10)
[image:pict.png]
```

`circle` 関数の結果は **絵（picture）の値** で、数値や文字列と同様に、式の結果として表示されます。`circle` への引数は、円の大きさ（ピクセル単位）を決めます。予想どおり、`rectangle` 関数もあり、こちらは引数を1つではなく2つ取ります。

```racket
> (rectangle 10 20)
[image:pict_2.png]
```

わざと `circle` に誤った個数の引数を与えて、何が起きるか試してみてください。

```racket
> (circle 10 20)
circle: arity mismatch;
 the expected number of arguments does not match the given
number
  expected: 1 plus optional arguments with keywords
#:border-color and #:border-width
  given: 2
  arguments...:
   10
   20
```

DrRacket は、エラーを引き起こした式をピンクで強調表示します（ただし、このドキュメントではピンクの強調は示されていません）。

`circle` や `rectangle` のような基本的な絵の構築子に加え、絵を組み合わせる `hc-append` 関数があります。Racket で関数呼び出しを入れ子にし始めると、次のようになります。

```racket
> (hc-append (circle 10) (rectangle 10 20))
[image:pict_3.png]
```

名前 `hc-append` のハイフンは識別子の一部です。`hc` マイナス `append` ではありません。関数名が `h` で始まるのは絵を **水平（horizontal）** に組み合わせるからで、次の文字が `c` なのは絵を **垂直方向の中央（center）** に揃えるからです。

他にどんな関数があるか——たとえば絵を垂直に積み、左揃えにする方法は？——と気になったら、DrRacket でテキストキャレットを `hc-append` という名前の上に置き、**F1** キーを押してください。ブラウザが開き、`hc-append` のドキュメントへのリンクが表示されます。リンクをクリックすると、他にもたくさんの関数が見つかります。

この文書を HTML で読んでいる場合は、`hc-append` や、このチュートリアルで使われている他のインポートされた識別子をクリックしてもかまいません。

## 4 定義

特定の円や長方形の絵を何度も使うなら、名前を付けるほうが簡単です。定義エリア（上側）に戻り、次の2つの定義を追加して、定義エリア全体が次のようになるようにしてください。

```racket
#lang slideshow
(define c (circle 10))
(define r (rectangle 10 20))
```

もう一度 **Run** をクリックします。これで、単に `c` や `r` と打てます。

```racket
> r
[image:pict_4.png]
> (hc-append c r)
[image:pict_5.png]
> (hc-append 20 c r c)
[image:pict_6.png]
```

見てのとおり、`hc-append` は絵の引数の前に **省略可能な数値引数** を受け取り、また任意個数の絵の引数を受け取ります。数値が与えられたとき、それは絵と絵の間に入れる間隔を指定します。

`c` と `r` の `define` 形式は、定義エリアではなく対話エリアで評価することもできました。ただし実際には、**定義エリアがプログラム本体**——保存するファイル——であり、対話エリアは一時的な探索やデバッグ用です。

プログラムに **関数定義** を追加しましょう。関数定義も図形の定義と同じく `define` を使いますが、関数名の前に開き括弧を置き、対応する閉じ括弧の前に引数名を書きます。

```racket
(define (square n)
; A semi-colon starts a line comment.
; The expression below is the function body.
  (filled-rectangle n n))
```

（コメント: セミコロン `;` は行コメントの開始です。その下の式が関数本体です。）

定義の構文は、関数呼び出しの構文と対応しています。

```racket
> (square 10)
[image:pict_7.png]
```

定義を対話エリアで評価できるのと同様に、式を定義エリアに書くこともできます。プログラムを実行すると、定義エリアにある式の結果が対話エリアに表示されます。これ以降、例の定義と式はまとめて書きますので、好きなエリアに置いてください。ただし例は互いに積み重なるので、少なくとも定義は定義エリアに置くのがよいです。

## 5 局所束縛

`define` 形式は、局所的な束縛を作るために、いくつかの場所で使えます。たとえば関数本体の内側でも使えます。

```racket
(define (four p)
  (define two-p (hc-append p p))
  (vc-append two-p two-p))
```

Racketeer（Racket 使い）は、局所束縛に `let` や `let*` 形式を使うこともあります。`let` の利点は、任意の式の位置で使えることです。また、識別子ごとに別々の `define` を書く必要がなく、一度に多くの識別子を束縛できます。

```racket
(define (checker p1 p2)
  (let ([p12 (hc-append p1 p2)]
        [p21 (hc-append p2 p1)])
    (vc-append p12 p21)))
```

`let` 形式は複数の識別子を **同時に** 束縛するので、束縛どうしが互いに参照し合うことはできません。対照的に `let*` 形式は、後の束縛が前の束縛を使うことを許します。

```racket
(define (checkerboard p)
  (let* ([rp (colorize p "red")]
         [bp (colorize p "black")]
         [c (checker rp bp)]
         [c4 (four c)])
    (four c4)))
```

## 6 関数は値である

`circle` を関数として呼び出す代わりに、式として単に `circle` を評価してみてください。

```racket
> circle
#<procedure:circle>
```

つまり識別子 `circle` は関数（別名「手続き」）に束縛されており、ちょうど `c` が円の絵に束縛されているのと同じです。円の絵と違って関数を完全に表示する簡単な方法はないので、DrRacket は単に `#<procedure:circle>` と表示します。

この例は、関数も数値や絵と同じく **値** であることを示します（表示がきれいではないとしても）。関数は値なので、他の関数を引数として受け取る関数を定義できます。

```racket
(define (series mk)
  (hc-append 4 (mk 5) (mk 10) (mk 20)))
```

関数を引数として受け取る関数を呼ぶとき、引数となる関数が他のどこでも必要ないことがよくあります。そのたびに `define` で関数を書くのは面倒です。名前を考え、定義を置く場所を見つけなければならないからです。代わりに `lambda` を使うと、**無名関数** を作れます。

```racket
> (series (lambda (size) (checkerboard (square size))))
[image:pict_13.png]
```

`lambda` の直後の括弧付きの名前が関数の引数で、そのあとの式が関数本体です。「function」や「procedure」ではなく「lambda」という言葉を使うのは、Racket の歴史と文化の一部です。

関数用の `define` 形式は、実際には、値として `lambda` を使う単純な `define` の省略形です。たとえば `series` の定義は次のようにも書けます。

```racket
(define series
  (lambda (mk)
    (hc-append 4 (mk 5) (mk 10) (mk 20))))
```

多くの Racketeer は、`lambda` に展開するより、`define` の省略形の関数形式を好みます。

## 7 レキシカルスコープ

Racket は **レキシカルスコープ** の言語です。つまり、識別子が式として使われるとき、その式の **テキスト上の環境** の何かが、識別子の束縛を決めます。この規則は `lambda` 本体の中の識別子にも、他のどこでも同様に当てはまります。

次の `rgb-series` 関数では、各 `lambda` 形式の中の `mk` の使用は、`rgb-series` の引数を指します。それがテキスト上スコープにある束縛だからです。

```racket
(define (rgb-series mk)
  (vc-append
   (series (lambda (sz) (colorize (mk sz) "red")))
   (series (lambda (sz) (colorize (mk sz) "green")))
   (series (lambda (sz) (colorize (mk sz) "blue")))))
```

別の例です。`rgb-maker` は関数を受け取り、元の関数を覚えて使う新しい関数を返します。

```racket
(define (rgb-maker mk)
  (lambda (sz)
    (vc-append (colorize (mk sz) "red")
               (colorize (mk sz) "green")
               (colorize (mk sz) "blue"))))
```

`rgb-maker` で関数を合成すると、`rgb-series` を使う場合と比べて、絵の中のオブジェクトの並び方が違うことに注意してください。

## 8 リスト

Racket は、もともと「LISt Processor」を意味した言語 Lisp から多くのスタイルを受け継いでおり、リストはいまも Racket の重要な一部です。

`list` 関数は任意個数の引数を取り、与えられた値を含むリストを返します。

```racket
> (list "red" "green" "blue")
'("red" "green" "blue")
> (list (circle 10) (square 10))
'([image:pict_18.png] [image:pict_19.png])
```

見てのとおり、リストは **単一引用符** のあとに、リスト要素の表示を囲む一対の括弧として表示されます。ここには混乱の余地があります。括弧は `(circle 10)` のような **式** にも、`'("red" "green" "blue")` のような **表示結果** にも使われるからです。違いの鍵は引用符で、別のところで議論されています。違いを強調するため、ドキュメントと DrRacket では、結果の括弧は式の括弧と異なり青で表示されます。

リストがあれば、いつか各要素に何かしたくなるでしょう。`map` 関数はリストと、リストの各要素に適用する関数を取り、その関数の結果を組み合わせた新しいリストを返します。

```racket
(define (rainbow p)
  (map (lambda (color)
         (colorize p color))
       (list "red" "orange" "yellow" "green" "blue" "purple")))
```

リストと一緒に使える別の関数が `apply` です。`map` と同様、関数とリストを取りますが、`apply` に与える関数は、要素を一つずつではなく、**すべての引数を一度に** 受け取るべきです。`apply` は、任意個数の引数を取る関数——たとえば `vc-append`——と特に相性がよいです。

```racket
> (apply vc-append (rainbow (square 5)))
[image:pict_26.png]
```

`(vc-append (rainbow (square 5)))` ではうまくいかないことに注意してください。`vc-append` は引数としてリストを欲しがらず、引数として **絵** を欲しがり、しかも任意個数受け取れるからです。`apply` は、「多くの引数を欲しがる関数」と「それらの引数のリストという単一の値」のあいだの橋渡しをします。

## 9 モジュール

定義ウィンドウのプログラムが次で始まるので、

```racket
#lang slideshow
```

定義ウィンドウに書くコードはすべて **モジュール** の内側にあります。さらに、そのモジュールは最初に `slideshow` が指すモジュールからすべてをインポートします。`slideshow` は絵を作る関数に加え、`list` や `map` のようなよく使う関数もエクスポートします。

追加のライブラリをインポートするには `require` 形式を使います。たとえばライブラリ `pict/flash` は `filled-flash` 関数を提供します。

```racket
> (filled-flash 40 30)
[image:pict_27.png]
```

モジュールの名前付けと配布にはさまざまな方法があります。

- 一部のモジュールは Racket 配布に同梱されているか、そうでなければ **コレクション** の階層にインストールされます。たとえばモジュール名 `pict/flash` は、「`"pict"` コレクション内のファイル `"flash.rkt"` で実装されたモジュール」を意味します。モジュール名にスラッシュが含まれない場合は、`"main.rkt"` ファイルを指します。
- 一部のモジュールの集まりは **パッケージ** として配布されます。パッケージは DrRacket の **File** メニューの **Install Package...** からインストールできるほか、コマンドラインツール `raco pkg` でもインストールできます。たとえば `"avl"` パッケージを入れると `avl` モジュールが使えます。パッケージは https://pkgs.racket-lang.org/ に登録することも、Git リポジトリ・Web サイト・ファイル・ディレクトリから直接入れることもできます。詳細は *Package Management in Racket* を参照してください。
- 一部のモジュールは、特定のコレクションやパッケージに属さず、他のモジュールに対する **相対位置** に置かれます。たとえば DrRacket で、ここまでの定義をファイル `"quick.rkt"` に保存し、次の行を追加したとします。

```racket
(provide rainbow square)
```

すると、同じディレクトリに新しいタブまたはウィンドウを開き、次の新しいプログラム `"use.rkt"` を書けます。

```racket
#lang racket
(require "quick.rkt")
(rainbow (square 5))
```

`"use.rkt"` を実行すると、正方形の虹色リストが出力になります。`"use.rkt"` は初期インポートとして `racket` を使っており、それ自体は絵を作る関数を供給しませんが、`require` と関数呼び出し構文は提供します。

> **注:** 定義を保存するには、DrRacket の **Save Definitions** メニュー項目を使います。

Racketeer は通常、新しいプログラムやライブラリを、相対パスとコレクションベースのパスで互いにインポートし合うモジュールとして書きます。こうして開発したプログラムやライブラリが他の人にも有用そうなら、特に実装が Git リポジトリでホストされている場合、パッケージとして登録できます。

## 10 マクロ

試してみる別のライブラリです。

```racket
> (code (circle 10))
[image:img0.png]
```

結果は円そのものではなく、式として使えば円を生成する **コードの絵** です。言い換えると、`code` は関数ではなく、絵を作るための **新しい構文形式** です。`code` 付きの開き括弧のあいだにある部分は式ではなく、`code` 構文形式によって操作されます。

これは前節で「`racket` は `require` と関数呼び出し構文を提供する」と言った意味を説明する助けになります。ライブラリは関数のような **値** のエクスポートに限られず、新しい構文形式も定義できます。この意味で、Racket は厳密には「ひとつの言語」ではなく、言語を拡張したり全く新しい言語を作ったりできるように言語を構造化する **アイデア** に近いものです。

新しい構文形式を導入する一つの方法が、`define-syntax` と `syntax-rules` です。

```racket
(define-syntax pict+code
  (syntax-rules ()
    [(pict+code expr)
     (hc-append 10
                expr
                (code expr))]))
```

この種の定義は **マクロ** です。`(pict+code expr)` の部分はマクロの使用パターンで、プログラム中のそのパターンの出現は、対応するテンプレート `(hc-append 10 expr (code expr))` の出現に置き換えられます。特に `(pict+code (circle 10))` は `expr` が `(circle 10)` としてパターンに一致するので、`(hc-append 10 (circle 10) (code (circle 10)))` に置き換えられます。

もちろん、この種の構文拡張は両刃の剣です。新しい言語を発明すると、言いたいことを言いやすくなる一方、他の人が理解しにくくなることもあります。実際、Racket の開発者は Racket コードを含む講演や論文を絶えず行っており、そうした成果物に関わる全員が `code` を知っている価値があります。

実際、このドキュメントのソースを見てみるとよいでしょう。`#lang` で始まりますが、それ以外はあまり Racket らしく見えません。それでも、私たちはソースを Racket プログラムとして実行することでこのドキュメントを組み立てています。文書を書くのに十分なほど Racket の構文を拡張するには `syntax-rules` 以上のものが必要ですが、Racket の構文拡張はかなり遠くまで連れて行ってくれます。

## 11 オブジェクト

オブジェクトシステムは、Racket ユーザーが学んで使う価値のある、洗練された言語拡張の別の例です。`lambda` があっても、ときにオブジェクトは関数より適しており、オブジェクトはグラフィカルユーザインタフェースで特にうまく働きます。Racket の GUI およびグラフィックスシステムの API は、オブジェクトとクラスの言葉で表現されています。

クラスシステム自体は `racket/class` ライブラリで実装され、`racket/gui/base` ライブラリが GUI と描画のクラスを提供します。慣例として、クラス名は `%` で終わります。

```racket
(require racket/class
         racket/gui/base)
(define f (new frame% [label "My Art"]
                      [width 300]
                      [height 300]
                      [alignment '(center center)]))
```

`new` 形式はクラスのインスタンスを作り、`label` や `width` のような初期化引数は名前付きで与えます。`send` 形式はオブジェクトのメソッド（たとえば `show`）を、メソッド名のあとの引数とともに呼び出します。この場合の引数 `#t` は真偽値定数の「真」です。

`slideshow` で生成された絵は、フレーム内のキャンバスのような描画コンテキストへ絵を描くために、グラフィックスツールボックスの描画コマンドを使う関数をカプセル化しています。`slideshow` の `make-pict-drawer` 関数は、絵の描画関数を公開します。キャンバスの描画コールバックで `make-pict-drawer` を使い、キャンバスへ絵を描けます。

```racket
(define (add-drawing p)
  (let ([drawer (make-pict-drawer p)])
    (new canvas% [parent f]
                 [style '(border)]
                 [paint-callback (lambda (self dc)
                                   (drawer dc 0 0))])))
```

> [image:img2.png]

各キャンバスはフレームの等しい部分を埋めるように伸びます。フレームがデフォルトで子をそのように管理するからです。

## 12 ここからどこへ行くか

この Racket 入門は、Lisp や Scheme を紹介・区別する伝統的な話題の多くを意図的に避けています。前置の算術記法、シンボル、リストの quote / quasiquote、`eval`、第一級継続、そしてすべての構文が実は変装した `lambda` にすぎない、という考え方です。それらはすべて Racket の一部ですが、Racket の日常的なプログラミングの主な材料ではありません。

代わりに、Racket プログラマは通常、関数、レコード、オブジェクト、例外、正規表現、モジュール、スレッドでプログラムします。つまり、Scheme がしばしば語られるような「ミニマリスト」な言語ではなく、Racket は豊富なライブラリとツールを持つ豊かな言語を提供します。

プログラミングが初めての方、あるいは教科書をじっくり進める忍耐がある方には、**How to Design Programs（プログラムの設計方法）** を読むことをおすすめします。すでに読んだ方、あるいはその本がどこへ連れて行くかを見たい方は、*Continue: Web Applications in Racket* を見てください。

経験のあるプログラマが、絵ではなくシステム寄りの視点から Racket の旅を続けるなら、次の目的地は *More: Systems Programming with Racket* です。

代わりに、完全な Racket 言語とツールを深く学び始めるなら、*The Racket Guide* へ進んでください。
