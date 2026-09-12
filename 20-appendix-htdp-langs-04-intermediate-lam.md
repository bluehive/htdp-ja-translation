# 付録 B-4: Intermediate Student with lambda（#lang htdp/isl+）

**原本:** `extracted/appendix/htdp-langs/original_markdown_04_intermediate-lam.md`

初学者向けに、説明文を日本語へ翻訳しています。コード・シグネチャ・実行例は原文のまま保持します。

## 4 Intermediate Student with Lambda（lambda つき中級）

文法の記法では、X...（太字の点）という書き方で、X が任意の回数（0回、1回、またはそれ以上）現れてよいことを示します。別に、文法はテンプレートで使う識別子として ... も定義します。

```
+-----------------------+--+---+--+--------------------------------------+
| program               |  | = |  | def-or-expr...                      |
+-----------------------+--+---+--+--------------------------------------+
| def-or-expr           |  | = |  | definition                           |
|                       |  | | |  | expr                                 |
|                       |  | | |  | test-case                            |
|                       |  | | |  | library-require                      |
| definition            |  | = |  | (define (name variable variable...… |
|                       |  | | |  | (define name expr)                   |
|                       |  | | |  | (define-struct name (name...))      |
| expr                  |  | = |  | (lambda (variable variable...) exp… |
|                       |  | | |  | (λ (variable variable...) expr)     |
|                       |  | | |  | (local [definition...] expr)        |
|                       |  | | |  | (letrec ([name expr]...) expr)      |
|                       |  | | |  | (let ([name expr]...) expr)         |
|                       |  | | |  | (let* ([name expr]...) expr)        |
|                       |  | | |  | (expr expr expr...)                 |
|                       |  | | |  | (cond [expr expr]... [expr expr])   |
|                       |  | | |  | (cond [expr expr]... [else expr])   |
|                       |  | | |  | (if expr expr expr)                  |
|                       |  | | |  | (and expr expr expr...)             |
|                       |  | | |  | (or expr expr expr...)              |
|                       |  | | |  | (time expr)                          |
|                       |  | | |  | name                                 |
|                       |  | | |  | prim-op                              |
|                       |  | | |  | ’quoted                              |
|                       |  | | |  | ‘quasiquoted                         |
|                       |  | | |  | ’()                                  |
|                       |  | | |  | number                               |
|                       |  | | |  | boolean                              |
|                       |  | | |  | string                               |
|                       |  | | |  | character                            |
|                       |  | | |  | (signature signature-form)           |
| signature-declaration |  | = |  | (: name signature-form)              |
| signature-form        |  | = |  | (enum expr...)                      |
|                       |  | | |  | (mixed signature-form...)           |
|                       |  | | |  | (signature-form... -> signature-fo… |
|                       |  | | |  | (ListOf signature-form)              |
|                       |  | | |  | signature-variable                   |
|                       |  | | |  | expr                                 |
| signature-variable    |  | = |  | %name                                |
| quoted                |  | = |  | name                                 |
|                       |  | | |  | number                               |
|                       |  | | |  | string                               |
|                       |  | | |  | character                            |
|                       |  | | |  | (quoted...)                         |
|                       |  | | |  | ’quoted                              |
|                       |  | | |  | ‘quoted                              |
|                       |  | | |  | `,`quoted                            |
|                       |  | | |  | `,@`quoted                           |
| quasiquoted           |  | = |  | name                                 |
|                       |  | | |  | number                               |
|                       |  | | |  | string                               |
|                       |  | | |  | character                            |
|                       |  | | |  | (quasiquoted...)                    |
|                       |  | | |  | ’quasiquoted                         |
|                       |  | | |  | ‘quasiquoted                         |
|                       |  | | |  | `,`expr                              |
|                       |  | | |  | `,@`expr                             |
| test-case             |  | = |  | (check-expect expr expr)             |
|                       |  | | |  | (check-random expr expr)             |
|                       |  | | |  | (check-within expr expr expr)        |
|                       |  | | |  | (check-member-of expr expr...)      |
|                       |  | | |  | (check-range expr expr expr)         |
|                       |  | | |  | (check-satisfied expr expr)          |
|                       |  | | |  | (check-error expr expr)              |
|                       |  | | |  | (check-error expr)                   |
| library-require       |  | = |  | (require string)                     |
|                       |  | | |  | (require (lib string string...))    |
|                       |  | | |  | (require (planet string package))    |
| package               |  | = |  | (string string number number)        |
+-----------------------+--+---+--+--------------------------------------+
```

名前 (name) または変数 (variable) は、空白や次の文字を含まない文字の並びです。

", ' ` ( ) [ ] { } |; #

数 (number) とは、123、3/2、5.5 のような数です。

真偽値 (boolean) は #true または #false のいずれかです。

#true 定数の別表記は #t、true、#T です。同様に #f、false、#F も #false として認識されます。

シンボル (symbol) は、クォート文字に続く名前です。シンボルは 42、'()、#false などと同じく値です。

文字列 (string) は、一対の " で囲まれた文字の並びです。シンボルと違い、文字列は文字に分割したり、さまざまな関数で操作したりできます。たとえば "abcdef"、"This is a string"、および "This is a string with \" inside" はすべて文字列です。

文字 (character) は #\ で始まり、その文字の名前を持ちます。たとえば #\a、#\b、#\space は文字です。

関数呼び出しでは、開き括弧の直後に現れる関数は、define や define-struct で定義した関数、またはあらかじめ定義された関数のいずれかです。

### 4.1 あらかじめ定義された変数

```
+----------------------+
| [値]              |
|                      |
| empty: empty?       |
+----------------------+
```

空リスト。

```
+----------------------+
| [値]              |
|                      |
| true: boolean?      |
+----------------------+
```

#true の値。

```
+----------------------+
| [値]              |
|                      |
| false: boolean?     |
+----------------------+
```

#false の値。

### 4.2 テンプレート変数

```
+----------------------+
| [構文]             |
|                      |
|..                   |
+----------------------+
```

関数定義がテンプレートであることを示すためのプレースホルダ。

```
+----------------------+
| [構文]             |
|                      |
|...                  |
+----------------------+
```

関数定義がテンプレートであることを示すためのプレースホルダ。

```
+----------------------+
| [構文]             |
|                      |
|....                 |
+----------------------+
```

関数定義がテンプレートであることを示すためのプレースホルダ。

```
+----------------------+
| [構文]             |
|                      |
|.....                |
+----------------------+
```

関数定義がテンプレートであることを示すためのプレースホルダ。

```
+----------------------+
| [構文]             |
|                      |
|......               |
+----------------------+
```

関数定義がテンプレートであることを示すためのプレースホルダ。

### 4.3 lambda つき中級の構文

```
+---------------------------------------------+
| [構文]                                    |
|                                             |
| (lambda (variable variable...) expression) |
+---------------------------------------------+
```

与えられた変数と同じ個数の引数を取り、本体が expression である関数を作ります。

```
+----------------------------------------+
| [構文]                                 |
|                                        |
| (λ (variable variable...) expression) |
+----------------------------------------+
```

ギリシャ文字 λ は lambda の同義語です。

```
+----------------------------------------+
| [構文]                                 |
|                                        |
| (expression expression expression...) |
+----------------------------------------+
```

最初の expression を評価して得られる関数を呼び出します。呼び出しの値は、その関数本体の中の名前付き変数が、対応する式の値で置き換えられたときの本体の値です。

呼び出される関数は、その関数呼び出しより前に現れる定義から来るか、lambda 式から来なければなりません。引数の式の個数は、関数が期待する引数の個数と同じでなければなりません。

```
+-------------------------------------+
| [構文]                              |
|                                     |
| (local [definition...] expression) |
+-------------------------------------+
```

expression の中で使う関連する定義をまとめます。各 definition は define または define-struct のいずれかです。

local を評価するとき、各定義が順番に評価され、最後に本体の expression が評価されます。定義によって導入された名前を参照できるのは、local の内側の式だけです（定義の右辺と本体の expression を含みます）。local で定義した名前がトップレベルの束縛と同じ場合、内側のものが外側のものを「影で覆い（シャドウ）」ます。つまり、local の内側では、その名前への参照は内側の定義を指します。

```
+-----------------------------------------------+
| [構文]                                        |
|                                               |
| (letrec ([name expr-for-let]...) expression) |
+-----------------------------------------------+
```

local に似ていますが、構文がより簡単です。各 name は、対応する expr-for-let の値を持つ変数（または関数）を定義します。expr-for-let が lambda なら letrec は関数を定義し、そうでなければ変数を定義します。

```
+---------------------------------------------+
| [構文]                                      |
|                                             |
| (let* ([name expr-for-let]...) expression) |
+---------------------------------------------+
```

letrec に似ていますが、各 name は本体の expression と、その名前より後に現れる expr-for-let の中だけで使えます。

```
+--------------------------------------------+
| [構文]                                     |
|                                            |
| (let ([name expr-for-let]...) expression) |
+--------------------------------------------+
```

letrec に似ていますが、定義された名前は最後の expression の中だけで使え、名前の隣の expr-for-let の中では使えません。

```
+----------------------+
| [構文]               |
|                      |
| (time expression)    |
+----------------------+
```

expression の評価にかかった時間を測ります。expression を評価したあと、time はその評価にかかった時間（実時間、CPU 時間、空きメモリの回収に使った時間を含む）を表示します。time の値は expression の値と同じです。

### 4.4 共通の構文（Common Syntaxes）

次の構文は、*Intermediate with Lambda* レベルでも Intermediate Student レベルと同じ動きをします。

```
+--------------------------------------------------+
| [構文]                                         |
|                                                  |
| (define (name variable variable...) expression) |
+--------------------------------------------------+
```

name という名前の関数を定義します。expression は関数本体です。関数が呼ばれると、引数の値が変数の代わりに本体へ挿入されます。関数は、その新しい式の値を返します。

関数名は、他の関数や変数と同じであってはなりません。

```
+--------------------------+
| [構文]                 |
|                          |
| (define name expression) |
+--------------------------+
```

expression の値で name という変数を定義します。変数名は他の関数や変数と同じであってはならず、name 自身が expression に現れてはなりません。

```
+----------------------+
| [構文]             |
|                      |
| ’name                |
+----------------------+
```

クオートされた name はシンボルです。クオートされた部分は、入れ子のリストの略記です。

通常、このクオートは ' で書き、例えば '(apple banana) のようにしますが、quote を使って (quote (apple banana)) のように書くこともできます。

```
+----------------------+
| [構文]             |
|                      |
| ‘name                |
+----------------------+
```

quote に似ていますが、式への「アンクオート」による脱出も許します。

通常、準クオートはバッククオート ` で書き、例えば `(apple ,(+ 1 2)) のようにしますが、quasiquote を使って (quasiquote (apple ,(+ 1 2))) のように書くこともできます。

```
+----------------------+
| [構文]             |
|                      |
|,expression          |
+----------------------+
```

単一の準クオートの下では、`,expression` はクオートから脱出して、評価された式の結果を略記リストへ挿入します。

複数の準クオートの下では、`,expression` は文字どおりの `,expression` であり、expression に対する準クオートの段数を1つ減らします。

通常、アンクオートは `,` で書きますが、unquote で書くこともできます。

```
+----------------------+
| [構文]             |
|                      |
|,@expression         |
+----------------------+
```

単一の準クオートの下では、`,@expression` はクオートから脱出して、評価結果がリストである式を、略記リストへ継ぎ足します（スプライスします）。

複数の準クオートの下では、スプライシング・アンクオートはアンクオートと同様で、準クオートの段数を1つ減らします。

通常、スプライシング・アンクオートは `,@` で書きますが、unquote-splicing で書くこともできます。

```
+-------------------------------------------------+
| [構文]                                        |
|                                                 |
| (define-struct structure-name (field-name...)) |
+-------------------------------------------------+
```

structure-name という新しい構造体を定義します。構造体のフィールドは field-name たちで名付けられます。define-struct のあと、次の新しい関数が使えます。

- make-structure-name: 構造体のフィールド数と同じ個数の引数を取り、その構造体の新しいインスタンスを作ります。
- structure-name-field-name: 構造体のインスタンスを取り、field-name というフィールドの値を返します。
- structure-name?: 任意の値を取り、その値がその構造体のインスタンスなら #true を返します。

define-struct が導入する新しい関数の名前は、他の関数や変数と同じであってはなりません。同じだと define-struct はエラーを報告します。

```
+-----------------------------------------------------------------------------+
| [構文]                                                                    |
|                                                                             |
| (cond [question-expression answer-expression]...)                          |
| (cond [question-expression answer-expression]... [else answer-expression]) |
| (cond [question-expression answer-expression]                               |
|...                                                                         |
| [else answer-expression])                                                   |
|                                                                             |
| ```racket                                                                   |
| (cond [question-expression answer-expression]                               |
|...                                                                   |
|       [else answer-expression])                                             |
| ```                                                                         |
+-----------------------------------------------------------------------------+
```

ある条件に基づいて節を選びます。cond は #true に評価される最初の question-expression を見つけ、対応する answer-expression を評価します。

どの question-expression も #true に評価されない場合、cond の値は else 節の answer-expression です。else がなければ、cond はエラーを報告します。question-expression の結果が #true でも #false でもない場合も、cond はエラーを報告します。

else は cond の外では使えません。

```
+-----------------------------+
| [構文]                    |
|                             |
| (if question-expression     |
| then-answer-expression      |
| else-answer-expression)     |
|                             |
| ```racket                   |
| (if question-expression     |
|     then-answer-expression  |
|     else-answer-expression) |
| ```                         |
+-----------------------------+
```

question-expression の値が #true のとき、if は then-answer-expression を評価します。テストが #false のとき、if は else-answer-expression を評価します。

question-expression が #true でも #false でもない場合、if はエラーを報告します。

```
+--------------------------------------------+
| [構文]                                   |
|                                            |
| (and expression expression expression...) |
+--------------------------------------------+
```

すべての expression が #true なら #true に評価されます。いずれかの expression が #false なら、and 式は #false に評価されます（その式より右の式は評価されません）。

いずれかの expression が #true でも #false でもない値に評価された場合、and はエラーを報告します。

```
+-------------------------------------------+
| [構文]                                  |
|                                           |
| (or expression expression expression...) |
+-------------------------------------------+
```

いずれかの expression が #true になった時点で #true に評価されます（その式より右の式は評価されません）。すべての expression が #false なら、or 式は #false に評価されます。

いずれかの expression が #true でも #false でもない値に評価された場合、or はエラーを報告します。

```
+-----------------------------------------------+
| [構文]                                      |
|                                               |
| (check-expect expression expected-expression) |
+-----------------------------------------------+
```

最初の expression が expected-expression と同じ値に評価されることを検査します。

```racket
(check-expect (fahrenheit->celsius 212) 100)
(check-expect (fahrenheit->celsius -40) -40)

(define (fahrenheit->celsius f)
  (* 5/9 (- f 32)))
```

check-expect 式は学生プログラムのトップレベルに置かなければなりません。また、プログラムのどこに置いてもよく、テスト対象の関数定義より前でも構いません。そこに check-expect を置くことで、プログラマは動く例を通じて将来の読者にプログラムの意図を伝え、しばしば関数定義本体そのものを読む必要をなくします。check-expect（およびすべての check 形式）の構文エラーは、意図的に実行時まで遅延されます。学生が完全な関数ヘッダを必ずしも書かずにテストを書けるようにするためです。

expr または expected-expr が不正確数や関数値を生成するのはエラーです。不正確数については、単純な等価性で比較するのは道徳的に正しくありません。代わりに両者が小さな区間内にあるかを調べます。check-within を参照してください。関数については（Intermediate 以上）、関数を比較することは証明可能なほど不可能です。

```
+-----------------------------------------------+
| [構文]                                        |
|                                               |
| (check-random expression expected-expression) |
+-----------------------------------------------+
```

最初の expression が expected-expression と同じ値に評価されることを検査します。

この形式は、両側に同じ乱数生成器を供給します。両側が同じ区間の乱数を同じ順番で要求すれば、同じ乱数を受け取ります。

ここで は simple example の where check-乱数 は useful:

```racket
(define WIDTH 100)
(define HEIGHT (* 2 WIDTH))

(define-struct player (name x y))
; A Player is (make-player String Nat Nat)

; String -> Player

(check-random (create-randomly-placed-player "David Van Horn")
              (make-player "David Van Horn" (random WIDTH) (random HEIGHT)))

(define (create-randomly-placed-player name)
  (make-player name (random WIDTH) (random HEIGHT)))
```

check-random の両側で、random が同じ数に対して同じ順番で呼ばれていることに注意してください。両側が異なる区間で random を呼ぶと、失敗しやすくなります。

```racket
; String -> Player

(check-random (create-randomly-placed-player "David Van Horn")
              (make-player "David Van Horn" (random WIDTH) (random HEIGHT)))

(define (create-randomly-placed-player name)
  (a-helper-function name (random HEIGHT)))

; String Number -> Player
(define (a-helper-function name height)
   (make-player name (random WIDTH) height))
```

a-helper-function への引数が先に評価されるため、random は最初に区間 [0,HEIGHT) で、次に [0,WIDTH) で呼ばれます。つまり、前の check-random とは異なる順番です。

expr または expected-expr が関数値や不正確数を生成するのはエラーです。詳細は check-expect の注を参照してください。

```
+----------------------------------------+
| [構文]                               |
|                                        |
| (check-satisfied expression predicate) |
+----------------------------------------+
```

最初の expression が、名前付きの predicate（1引数の関数）を満たすことを検査します。「満たす」とは「その関数が与えられた値に対して #true を生成する」という意味です。

check-satisfied の簡単な例を次に示します。

```racket
> (check-satisfied 1 odd?)
The test passed!
```

```racket
> (check-satisfied 1 even?)
Ran 1 test.                                       0 tests passed.                                   Check failures:                                                        ┌───┐                                Actual value │ 1 │ does not satisfy even?.                     └───┘                        at line 3, column 0
```

一般に check-satisfied は、プログラム設計者が定義した関数を使ってテスト一式を書き表す力を与えます。

```racket
; [cons Number [List-of Number]] -> Boolean
; a function for testing htdp-sort

(check-expect (sorted? (list 1 2 3)) #true)
(check-expect (sorted? (list 2 1 3)) #false)

(define (sorted? l)
  (cond
    [(empty? (rest l)) #true]
    [else (and (<= (first l) (second l)) (sorted? (rest l)))]))

; [List-of Number] -> [List-of Number]
; create a sorted version of the given list of numbers

(check-satisfied (htdp-sort (list 1 2 0 3)) sorted?)

(define (htdp-sort l)
  (cond
    [(empty? l) l]
    [else (insert (first l) (htdp-sort (rest l)))]))

; Number [List-of Number] -> [List-of Number]
; insert x into l at proper place
; assume l is arranged in ascending order
; the result is sorted in the same way
(define (insert x l)
  (cond
    [(empty? l) (list x)]
    [else (if (<= x (first l)) (cons x l) (cons (first l) (insert x (rest l))))]))
```

そして実際、htdp-sort の結果は sorted? 述語を満たします。

```racket
> (check-satisfied (htdp-sort (list 1 2 0 3)) sorted?)
```

```
+-----------------------------------------------------+
| [構文]                                            |
|                                                     |
| (check-within expression expected-expression delta) |
+-----------------------------------------------------+
```

expression 式の値が expected-expression 式の生成する値と構造的に等しいかを検査します。最初の式の中のすべての数は、2番目の式の対応する数から delta 以内でなければなりません。

```racket
(define-struct roots (x sqrt))
; RT is [List-of (make-roots Number Number)]

(define (root-of a)
  (make-roots a (sqrt a)))

(define (roots-table xs)
  (cond
    [(empty? xs) '()]
    [else (cons (root-of (first xs)) (roots-table (rest xs)))]))
```

入れ子のデータに不正確数が含まれるため、テストには check-within が正しい選択であり、delta が十分大きければテストは成功します。

例:

```racket
> (check-within (roots-table (list 1.0 2.0 3.0))                (list                  (make-roots 1.0 1.0)                  (make-roots 2  1.414)                  (make-roots 3  1.713))                0.1)
The test passed!
```

対照的に、delta が小さいとテストは失敗します。

例:

```racket
> (check-within (roots-table (list 2.0))                (list                  (make-roots 2  1.414))                #i1e-5)
Ran 1 test.                                                                                                                      0 tests passed.                                                                                                                  Check failures:                                                                                                                                       ┌────────────────────────────────────────┐                                      ┌─────────────────────────┐         Actual value │ '((make-roots 2.0 1.4142135623730951)) │ is not within 1e-5 of expected value │ '((make-roots 2 1.414)) │.                     └────────────────────────────────────────┘                                      └─────────────────────────┘ at line 5, column 0
```

expressions または expected-expression が関数値を生成するのはエラーです。詳細は check-expect の注を参照してください。

delta が数でない場合、check-within はエラーを報告します。

```
+-------------------------------------------------+
| [構文]                                        |
|                                                 |
| (check-error expression expected-error-message) |
| (check-error expression)                        |
+-------------------------------------------------+
```

expression がエラーを報告することを検査します。expected-error-message がある場合は、エラーメッセージがその値と一致することも検査します。

check-error の使用が求められる典型的な初学者の例を次に示します。

```racket
(define sample-table
  '(("matthias" 10)
    ("matthew"  20)
    ("robby"    -1)
    ("shriram"  18)))

; [List-of [list String Number]] String -> Number
; determine the number associated with s in table

(define (lookup table s)
  (cond
    [(empty? table) (error (string-append s " not found"))]
    [else (if (string=? (first (first table)) s)
              (second (first table))
              (lookup (rest table)))]))
```

この文脈での次の2つの例を考えてください。

例:

```racket
> (check-expect (lookup sample-table "matthew") 20)
The test passed!
```

例:

```racket
> (check-error (lookup sample-table "kathi") "kathi not found")
The test passed!
```

```
+--------------------------------------------------------+
| [構文]                                               |
|                                                        |
| (check-member-of expression expression expression...) |
+--------------------------------------------------------+
```

最初の expression の値が、続く expression のいずれかと同じであることを検査します。

```racket
; [List-of X] -> X
; pick a random element from the given list l
(define (pick-one l)
  (list-ref l (random (length l))))
```

例:

```racket
> (check-member-of (pick-one '("a" "b" "c")) "a" "b" "c")
The test passed!
```

いずれかの expression が関数値を生成するのはエラーです。詳細は check-expect の注を参照してください。

```
+---------------------------------------------------------+
| [構文]                                                |
|                                                         |
| (check-range expression low-expression high-expression) |
+---------------------------------------------------------+
```

最初の expression の値が、low-expression の値と high-expression の値の間（両端を含む）の数であることを検査します。

check-range 形式は、不正確数を計算する関数の取り得る結果の範囲を区切るのに最も適しています。

```racket
(define EPSILON 0.001)

; [Real -> Real] Real -> Real
; what is the slope of f at x?
(define (differentiate f x)
  (slope f (- x EPSILON) (+ x EPSILON)))

; [Real -> Real] Real Real -> Real
(define (slope f left right)
  (/ (- (f right) (f left))
     2 EPSILON))

(check-range (differentiate sin 0) 0.99 1.0)
```

expression、low-expression、high-expression のいずれかが関数値を生成するのはエラーです。詳細は check-expect の注を参照してください。

```
+----------------------+
| [構文]             |
|                      |
| (require string)     |
+----------------------+
```

string で指定されたモジュールの定義を、現在のモジュール（つまり現在のファイル）で使えるようにします。string は現在のファイルからの相対パスのファイルを指します。

string には、プラットフォームごとのパス規約の問題を避けるための制約がいくつかあります。/ はディレクトリ区切り、. は常に現在のディレクトリ、.. は常に親ディレクトリを意味し、パス要素に使えるのは a から z（大文字小文字どちらも）、0 から 9、-、_、. だけで、文字列は空であってはならず、先頭や末尾の / を含んではなりません。

```
+-----------------------+
| [構文]              |
|                       |
| (require module-name) |
+-----------------------+
```

インストール済みライブラリ内のファイルにアクセスします。ライブラリ名は、相対パス文字列と同じ制約を持つ識別子です（ただし引用符はありません）。さらに .. を含んではならないという制約があります。

```
+-----------------------------------+
| [構文]                          |
|                                   |
| (require (lib string string...)) |
+-----------------------------------+
```

インストール済みライブラリ内のファイルにアクセスし、その定義を現在のモジュール（つまり現在のファイル）で使えるようにします。最初の string がライブラリファイル名で、残りの string がファイルがインストールされているコレクション（およびサブコレクションなど）の名前です。各 string は (require string) 形式と同じ制約を受けます。

```
+---------------------------------------------------------+
| [構文]                                                |
|                                                         |
| (require (planet string (string string number number))) |
+---------------------------------------------------------+
```

インターネット上の PLaneT サーバ経由で配布されているライブラリにアクセスし、その定義を現在のモジュール（つまり現在のファイル）で使えるようにします。

planet の require の完全な文法は Importing and Exporting: require and provide にありますが、構文の例を探すのにいちばんよい場所は、PLaneT サーバ上の特定のパッケージの説明です。

### 4.5 あらかじめ定義された関数

### 4.6 シグネチャ

> Signatures do not have to be comment: They can also be part of the > code. When a signature is attached to a function, DrRacket will check > that program uses the function in accordance with the signature and > display signature violations along with the test results.A signature is a regular value, and is specified as a > signature form, a > special syntax that only works with: signature declarations > and inside signature expressions.

```
+-------------------------+
| [構文]                |
|                         |
| (: name signature-form) |
+-------------------------+
```

これ attaches シグネチャ specified によって シグネチャ-form へ 定義 の name. There でなければならない 定義 の name somewhere の中の プログラム.

```racket
(: age Integer)
(define age 42)

(: area-of-square (Number -> Number))
(define (area-of-square len)
  (sqr len))
```

On running プログラム, Racket checks whether シグネチャs attached with: actually match 値 の 変数. もし they don’t, Racket reports シグネチャ violation along とともに test failures.

たとえば、 この piece の code:

```racket
(: age Integer)
(define age "fortytwo")
```

Yields この output:

```
+--------------------------------------------------+
| `1 signature violation.`                         |
+--------------------------------------------------+
| `Signature violations:`                          |
| `got "fortytwo" at line 2, column 12, signature… |
+--------------------------------------------------+
```

Note という シグネチャ violation does ない stop running プログラム.

```
+----------------------------+
| [構文]                   |
|                            |
| (signature signature-form) |
+----------------------------+
```

これ 返す シグネチャ described によって シグネチャ-form として 値.

#### 4.6.1 シグネチャ形式

> Any expression can be a signature form, in which case the signature is > the value returned by that expression. There are a few special > signature forms, however:In a signature form, any name that starts with a % is a > signature variable that stands for any signature depending on how > the signature is used.Example:

```racket
(: same (%a -> %a))

(define (same x) x)
```

```
+-----------------------------------------------------+
| [構文]                                            |
|                                                     |
| (input-signature-form... -> output-signature-form) |
+-----------------------------------------------------+
```

これ シグネチャ form describes 関数 とともに inputs described によって input-シグネチャ-forms と output described によって output-シグネチャ-form.

```
+----------------------+
| [構文]             |
|                      |
| (enum expr...)      |
+----------------------+
```

これ シグネチャ describes enumeration の 値s returned によって exprs.

例:

```racket
(: cute? ((enum "cat" "snake") -> Boolean))

(define (cute? pet)
  (cond
    [(string=? pet "cat") #t]
    [(string=? pet "snake") #f]))
```

```
+----------------------------+
| [構文]                   |
|                            |
| (mixed signature-form...) |
+----------------------------+
```

これ シグネチャ describes mixed data, i.e. itemization where 各 の cases has シグネチャ described によって シグネチャ-form.

例:

```racket
(define SIGS (signature (mixed Aim Fired)))
```

```
+-------------------------+
| [構文]                |
|                         |
| (ListOf signature-form) |
+-------------------------+
```

これ シグネチャ describes リスト where elements は described によって シグネチャ-form.

```
+------------------------+
| [構文]               |
|                        |
| (predicate expression) |
+------------------------+
```

このシグネチャは述語を通じて値を記述します。expression は1引数で真偽値を返す関数に評価されなければなりません。シグネチャは、その述語が #true を返すすべての値と一致します。

#### 4.6.2 構造体シグネチャ

> A define-struct form defines two additional names that can be > used in signatures. For a struct called struct, these > are Struct and StructOf. Note that > these names are capitalized. In particular, a struct called > Struct, will also define Struct and > StructOf. Moreover, when forming the additional > names, hyphens are removed, and each letter following a hyphen is > capitalized - so a struct called foo-bar will define > FooBar and FooBarOf.Struct is a signature that describes struct values > from this structure type. StructOf is a function > that takes as input a signature for each field. It returns a > signature describing values of this structure type, additionally > describing the values of the fields of the value.

```racket
(define-struct pair [fst snd])

(: add-pair ((PairOf Number Number) -> Number))
(define (add-pair p)
  (+ (pair-fst p) (pair-snd p)))
```

remaining subsections リスト それらの 関数s という は built へ プログラムming language. All other 関数s は imported から teachpack または でなければならない defined の中の プログラム.

### 4.7 数: 整数・有理数・実数・複素数・正確数・非正確数

```
+----------------------+
| [手続き]          |
|                      |
| (- x y...) → number |
| x: number           |
| y: number           |
+----------------------+
```

第1の数から第2（およびそれ以降）の数を引きます。引数が1つだけのときは、その数の符号を反転します。

```racket
> (- 5)
-5
> (- 5 3)
2
> (- 5 3 1)
1
```

```
+--------------------------+
| [手続き]              |
|                          |
| (< x y z...) → boolean? |
| x: real                 |
| y: real                 |
| z: real                 |
+--------------------------+
```

two or more (real) numbers for less-than を比較します。

```racket
> (< 42 2/5)
#false
```

```
+---------------------------+
| [手続き]               |
|                           |
| (<= x y z...) → boolean? |
| x: real                  |
| y: real                  |
| z: real                  |
+---------------------------+
```

two or more (real) numbers for less-than or equality を比較します。

```racket
> (<= 42 2/5)
#false
```

```
+--------------------------+
| [手続き]              |
|                          |
| (> x y z...) → boolean? |
| x: real                 |
| y: real                 |
| z: real                 |
+--------------------------+
```

two or more (real) numbers for greater-than を比較します。

```racket
> (> 42 2/5)
#true
```

```
+---------------------------+
| [手続き]               |
|                           |
| (>= x y z...) → boolean? |
| x: real                  |
| y: real                  |
| z: real                  |
+---------------------------+
```

two or more (real) numbers for greater-than or equality を比較します。

```racket
> (>= 42 42)
#true
```

```
+----------------------+
| [手続き]          |
|                      |
| (abs x) → real       |
| x: real             |
+----------------------+
```

判定する:  absolute 値 の 実数 数.

```racket
> (abs -12)
12
```

```
+----------------------+
| [手続き]          |
|                      |
| (acos x) → number    |
| x: number           |
+----------------------+
```

the arccosine (inverse of cos) of a number を計算します。

```racket
> (acos 0)
#i1.5707963267948966
```

```
+----------------------+
| [手続き]          |
|                      |
| (add1 x) → number    |
| x: number           |
+----------------------+
```

与えられた数を1増やします。

```racket
> (add1 2)
3
```

```
+----------------------+
| [手続き]          |
|                      |
| (angle x) → real     |
| x: number           |
+----------------------+
```

the angle from a complex number を取り出します。

```racket
> (angle (make-polar 3 4))
#i-2.2831853071795867
```

```
+----------------------+
| [手続き]          |
|                      |
| (asin x) → number    |
| x: number           |
+----------------------+
```

the arcsine (inverse of sin) of a number を計算します。

```racket
> (asin 0)
0
```

```
+----------------------+
| [手続き]          |
|                      |
| (atan x) → number    |
| x: number           |
+----------------------+
```

計算する:  arctangent の given 数:

```racket
> (atan 0)
0
> (atan 0.5)
#i0.4636476090008061
```

Also comes in a two-argument version where (atanyx) computes (atan(/yx)) but the signs of y and x determine the quadrant of the result and the result tends to be more accurate than that of the 1-argument version in borderline cases:

```racket
> (atan 3 4)
#i0.6435011087932844
> (atan -2 -1)
#i-2.0344439357957027
```

```
+-----------------------+
| [手続き]           |
|                       |
| (ceiling x) → integer |
| x: real              |
+-----------------------+
```

判定する:  closest 整数 (正確 または in正確) above 実数 数. 参照: round.

```racket
> (ceiling 12.3)
#i13.0
```

```
+-------------------------+
| [手続き]             |
|                         |
| (complex? x) → boolean? |
| x: any/c               |
+-------------------------+
```

some value is complex かどうかを判定します。

```racket
> (complex? 1-2i)
#true
```

```
+------------------------+
| [手続き]            |
|                        |
| (conjugate x) → number |
| x: number             |
+------------------------+
```

複素数の虚部の符号を反転します。

```racket
> (conjugate 3+4i)
3-4i
> (conjugate -2-5i)
-2+5i
> (conjugate (make-polar 3 4))
#i-1.960930862590836+2.2704074859237844i
```

```
+----------------------+
| [手続き]          |
|                      |
| (cos x) → number     |
| x: number           |
+----------------------+
```

the cosine of a number (radians) を計算します。

```racket
> (cos pi)
#i-1.0
```

```
+----------------------+
| [手続き]          |
|                      |
| (cosh x) → number    |
| x: number           |
+----------------------+
```

the hyperbolic cosine of a number を計算します。

```racket
> (cosh 10)
#i11013.232920103324
```

```
+-----------------------------+
| [手続き]                 |
|                             |
| (current-seconds) → integer |
+-----------------------------+
```

判定する:  current time の中の seconds elapsed (since platform-specific starting date).

```racket
> (current-seconds)
1779843339
```

```
+---------------------------+
| [手続き]               |
|                           |
| (denominator x) → integer |
| x: rational?             |
+---------------------------+
```

the denominator of a rational を計算します。

```racket
> (denominator 2/3)
3
```

```
+----------------------+
| [値]              |
|                      |
| e: real             |
+----------------------+
```

Euler’s 数.

```racket
> e
#i2.718281828459045
```

```
+----------------------+
| [手続き]          |
|                      |
| (even? x) → boolean? |
| x: integer          |
+----------------------+
```

some integer (exact or inexact) is even or not かどうかを判定します。

```racket
> (even? 2)
#true
```

```
+-----------------------------+
| [手続き]                 |
|                             |
| (exact->inexact x) → number |
| x: number                  |
+-----------------------------+
```

an exact number to an inexact one を変換します。

```racket
> (exact->inexact 12)
#i12.0
```

```
+-----------------------+
| [手続き]           |
|                       |
| (exact? x) → boolean? |
| x: number            |
+-----------------------+
```

some number is exact かどうかを判定します。

```racket
> (exact? (sqrt 2))
#false
```

```
+----------------------+
| [手続き]          |
|                      |
| (exp x) → number     |
| x: number           |
+----------------------+
```

判定する:  e raised へ 数.

```racket
> (exp -2)
#i0.1353352832366127
```

```
+----------------------+
| [手続き]          |
|                      |
| (expt x y) → number  |
| x: number           |
| y: number           |
+----------------------+
```

the power of the first to the second number, which is to say, exponentiation を計算します。

```racket
> (expt 16 1/2)
4
> (expt 3 -4)
1/81
```

```
+----------------------+
| [手続き]          |
|                      |
| (floor x) → integer  |
| x: real             |
+----------------------+
```

判定する:  closest 整数 (正確 または in正確) below 実数 数. 参照: round.

```racket
> (floor 12.3)
#i12.0
```

```
+-------------------------+
| [手続き]             |
|                         |
| (gcd x y...) → integer |
| x: integer             |
| y: integer             |
+-------------------------+
```

判定する:  greatest common divisor の two 整数s (正確 または in正確).

```racket
> (gcd 6 12 8)
2
```

```
+----------------------+
| [手続き]          |
|                      |
| (imag-part x) → real |
| x: number           |
+----------------------+
```

the imaginary part from a complex number を取り出します。

```racket
> (imag-part 3+4i)
4
```

```
+-----------------------------+
| [手続き]                 |
|                             |
| (inexact->exact x) → number |
| x: number                  |
+-----------------------------+
```

不正確数を正確数で近似します。

```racket
> (inexact->exact 12.0)
12
```

```
+-------------------------+
| [手続き]             |
|                         |
| (inexact? x) → boolean? |
| x: number              |
+-------------------------+
```

some number is inexact かどうかを判定します。

```racket
> (inexact? 1-2i)
#false
```

```
+--------------------------+
| [手続き]              |
|                          |
| (integer->char x) → char |
| x: exact-integer?       |
+--------------------------+
```

与えられた正確整数に対応する文字を ASCII 表から調べます（あれば）。

```racket
> (integer->char 42)
#\*
```

```
+----------------------------+
| [手続き]                |
|                            |
| (integer-sqrt x) → complex |
| x: integer                |
+----------------------------+
```

the integer or imaginary-integer square root of an integer を計算します。

```racket
> (integer-sqrt 11)
3
> (integer-sqrt -11)
0+3i
```

```
+-------------------------+
| [手続き]             |
|                         |
| (integer? x) → boolean? |
| x: any/c               |
+-------------------------+
```

some value is an integer (exact or inexact) かどうかを判定します。

```racket
> (integer? (sqrt 2))
#false
```

```
+-------------------------+
| [手続き]             |
|                         |
| (lcm x y...) → integer |
| x: integer             |
| y: integer             |
+-------------------------+
```

判定する:  least common multiple の two 整数s (正確 または in正確).

```racket
> (lcm 6 12 8)
24
```

```
+----------------------+
| [手続き]          |
|                      |
| (log x) → number     |
| x: number           |
+----------------------+
```

判定する:  base-e logarithm の 数.

```racket
> (log 12)
#i2.4849066497880004
```

```
+----------------------+
| [手続き]          |
|                      |
| (magnitude x) → real |
| x: number           |
+----------------------+
```

判定する:  magnitude の 複素数 数.

```racket
> (magnitude (make-polar 3 4))
#i2.9999999999999996
```

```
+---------------------------+
| [手続き]               |
|                           |
| (make-polar x y) → number |
| x: real                  |
| y: real                  |
+---------------------------+
```

a complex from a magnitude and angle を作成します。

```racket
> (make-polar 3 4)
#i-1.960930862590836-2.2704074859237844i
```

```
+---------------------------------+
| [手続き]                     |
|                                 |
| (make-rectangular x y) → number |
| x: real                        |
| y: real                        |
+---------------------------------+
```

a complex from a real and an imaginary part を作成します。

```racket
> (make-rectangular 3 4)
3+4i
```

```
+----------------------+
| [手続き]          |
|                      |
| (max x y...) → real |
| x: real             |
| y: real             |
+----------------------+
```

判定する:  largest 数—aka, maximum.

```racket
> (max 3 2 8 7 2 9 0)
9
```

```
+----------------------+
| [手続き]          |
|                      |
| (min x y...) → real |
| x: real             |
| y: real             |
+----------------------+
```

判定する:  smallest 数—aka, minimum.

```racket
> (min 3 2 8 7 2 9 0)
0
```

```
+------------------------+
| [手続き]            |
|                        |
| (modulo x y) → integer |
| x: integer            |
| y: integer            |
+------------------------+
```

Finds remainder の division の first 数 によって second:

```racket
> (modulo 9 2)
1
> (modulo 3 -4)
-1
```

```
+--------------------------+
| [手続き]              |
|                          |
| (negative? x) → boolean? |
| x: real                 |
+--------------------------+
```

some real number is strictly smaller than zero かどうかを判定します。

```racket
> (negative? -2)
#true
```

```
+-----------------------------+
| [手続き]                 |
|                             |
| (number->string x) → string |
| x: number                  |
+-----------------------------+
```

a number to a string を変換します。

```racket
> (number->string 42)
"42"
```

```
+--------------------------------------+
| [手続き]                          |
|                                      |
| (number->string-digits x p) → string |
| x: number                           |
| p: posint                           |
+--------------------------------------+
```

a number `x` to a string with the specified number of digits を変換します。

```racket
> (number->string-digits 0.9 2)
"0.9"
> (number->string-digits pi 4)
"3.1416"
```

```
+------------------------+
| [手続き]            |
|                        |
| (number? n) → boolean? |
| n: any/c              |
+------------------------+
```

ある値が数かどうかを判定します。

```racket
> (number? "hello world")
#false
> (number? 42)
#true
```

```
+-------------------------+
| [手続き]             |
|                         |
| (numerator x) → integer |
| x: rational?           |
+-------------------------+
```

the numerator of a rational を計算します。

```racket
> (numerator 2/3)
2
```

```
+----------------------+
| [手続き]          |
|                      |
| (odd? x) → boolean?  |
| x: integer          |
+----------------------+
```

some integer (exact or inexact) is odd or not かどうかを判定します。

```racket
> (odd? 2)
#false
```

```
+----------------------+
| [値]              |
|                      |
| pi: real            |
+----------------------+
```

ratio の circle’s circumference へ その diameter.

```racket
> pi
#i3.141592653589793
```

```
+--------------------------+
| [手続き]              |
|                          |
| (positive? x) → boolean? |
| x: real                 |
+--------------------------+
```

some real number is strictly larger than zero かどうかを判定します。

```racket
> (positive? -2)
#false
```

```
+--------------------------+
| [手続き]              |
|                          |
| (quotient x y) → integer |
| x: integer              |
| y: integer              |
+--------------------------+
```

Divides first 整数—also called dividend—by second—known として divisor—to obtain quotient.

```racket
> (quotient 9 2)
4
> (quotient 3 4)
0
```

```
+--------------------------------+
| [手続き]                    |
|                                |
| (random x) → natural?          |
| x: (and/c natural? positive?) |
+--------------------------------+
```

Generates 乱数 natural 数 less than ある given 正確 natural.

```racket
> (random 42)
27
```

```
+--------------------------+
| [手続き]              |
|                          |
| (rational? x) → boolean? |
| x: any/c                |
+--------------------------+
```

some value is a rational number かどうかを判定します。

```racket
> (rational? 1)
#true
> (rational? -2.349)
#true
> (rational? #i1.23456789)
#true
> (rational? (sqrt -1))
#false
> (rational? pi)
#true
> (rational? e)
#true
> (rational? 1-2i)
#false
```

As the interactions show, the teaching languages considers many more numbers as rationals than expected. In particular, pi is a rational number because it is only a finite approximation to the mathematical π. Think of rational? as a suggestion to think of these numbers as fractions.

```
+----------------------+
| [手続き]          |
|                      |
| (real-part x) → real |
| x: number           |
+----------------------+
```

the real part from a complex number を取り出します。

```racket
> (real-part 3+4i)
3
```

```
+----------------------+
| [手続き]          |
|                      |
| (real? x) → boolean? |
| x: any/c            |
+----------------------+
```

some value is a real number かどうかを判定します。

```racket
> (real? 1-2i)
#false
```

```
+---------------------------+
| [手続き]               |
|                           |
| (remainder x y) → integer |
| x: integer               |
| y: integer               |
+---------------------------+
```

判定する:  remainder の dividing first によって second 整数 (正確 または in正確).

```racket
> (remainder 9 2)
1
> (remainder 3 4)
3
```

```
+----------------------+
| [手続き]          |
|                      |
| (round x) → integer  |
| x: real             |
+----------------------+
```

実数を整数に丸めます（同点のときは偶数へ丸めます）。floor と ceiling も参照してください。

```racket
> (round 12.3)
#i12.0
```

```
+---------------------------------------------+
| [手続き]                                 |
|                                             |
| (sgn x) → (union 1 #i1.0 0 #i0.0 -1 #i-1.0) |
| x: real                                    |
+---------------------------------------------+
```

判定する:  sign の 実数 数.

```racket
> (sgn -12)
-1
```

```
+----------------------+
| [手続き]          |
|                      |
| (sin x) → number     |
| x: number           |
+----------------------+
```

the sine of a number (radians) を計算します。

```racket
> (sin pi)
#i1.2246467991473532e-16
```

```
+----------------------+
| [手続き]          |
|                      |
| (sinh x) → number    |
| x: number           |
+----------------------+
```

the hyperbolic sine of a number を計算します。

```racket
> (sinh 10)
#i11013.232874703393
```

```
+----------------------+
| [手続き]          |
|                      |
| (sqr x) → number     |
| x: number           |
+----------------------+
```

the square of a number を計算します。

```racket
> (sqr 8)
64
```

```
+----------------------+
| [手続き]          |
|                      |
| (sqrt x) → number    |
| x: number           |
+----------------------+
```

the square root of a number を計算します。

```racket
> (sqrt 9)
3
> (sqrt 2)
#i1.4142135623730951
```

```
+----------------------+
| [手続き]          |
|                      |
| (sub1 x) → number    |
| x: number           |
+----------------------+
```

与えられた数を1減らします。

```racket
> (sub1 2)
1
```

```
+----------------------+
| [手続き]          |
|                      |
| (tan x) → number     |
| x: number           |
+----------------------+
```

the tangent of a number (radians) を計算します。

```racket
> (tan pi)
#i-1.2246467991473532e-16
```

```
+----------------------+
| [手続き]          |
|                      |
| (zero? x) → boolean? |
| x: number           |
+----------------------+
```

some number is zero or not かどうかを判定します。

```racket
> (zero? 2)
#false
```

### 4.8 真偽値

```
+------------------------------+
| [手続き]                  |
|                              |
| (boolean->string x) → string |
| x: boolean?                 |
+------------------------------+
```

与えられた真偽値の文字列を生成します。

```racket
> (boolean->string #false)
"#false"
> (boolean->string #true)
"#true"
```

```
+----------------------------+
| [手続き]                |
|                            |
| (boolean=? x y) → boolean? |
| x: boolean?               |
| y: boolean?               |
+----------------------------+
```

two booleans are equal かどうかを判定します。

```racket
> (boolean=? #true #false)
#false
```

```
+-------------------------+
| [手続き]             |
|                         |
| (boolean? x) → boolean? |
| x: any/c               |
+-------------------------+
```

値が真偽値かどうかを判定します。

```racket
> (boolean? 42)
#false
> (boolean? #false)
#true
```

```
+-----------------------+
| [手続き]           |
|                       |
| (false? x) → boolean? |
| x: any/c             |
+-----------------------+
```

a value is false かどうかを判定します。

```racket
> (false? #false)
#true
```

```
+----------------------+
| [手続き]          |
|                      |
| (not x) → boolean?   |
| x: boolean?         |
+----------------------+
```

真偽値を否定します。

```racket
> (not #false)
#true
```

### 4.9 シンボル

```
+-----------------------------+
| [手続き]                 |
|                             |
| (symbol->string x) → string |
| x: symbol                  |
+-----------------------------+
```

a symbol to a string を変換します。

```racket
> (symbol->string 'c)
"c"
```

```
+---------------------------+
| [手続き]               |
|                           |
| (symbol=? x y) → boolean? |
| x: symbol                |
| y: symbol                |
+---------------------------+
```

two symbols are equal かどうかを判定します。

```racket
> (symbol=? 'a 'b)
#false
```

```
+------------------------+
| [手続き]            |
|                        |
| (symbol? x) → boolean? |
| x: any/c              |
+------------------------+
```

値がシンボルかどうかを判定します。

```racket
> (symbol? 'a)
#true
```

### 4.10 リスト

```
+-------------------------------+
| [手続き]                   |
|                               |
| (append l...) → (listof any) |
| l: (listof any)              |
+-------------------------------+
```

複数のリストから、要素を連結して1つのリストを作ります。ISL 以上では、append は1つのリストや0個のリストにも適用できます。

```racket
> (append (cons 1 (cons 2 '())) (cons "a" (cons "b" '())))
(list 1 2 "a" "b")
> (append)
'()
```

```
+-------------------------------------------+
| [手続き]                               |
|                                           |
| (assoc x l) → (union (listof any) #false) |
| x: any/c                                 |
| l: (listof any)                          |
+-------------------------------------------+
```

the first pair on l whose first is equal? to x; otherwise it produces #false を生成します。

```racket
> (assoc "hello" '(("world" 2) ("hello" 3) ("good" 0)))
(list "hello" 3)
```

```
+-----------------------------------+
| [手続き]                       |
|                                   |
| (assq x l) → (union #false cons?) |
| x: any/c                         |
| l: list?                         |
+-----------------------------------+
```

ある要素が、対のリストの中のある対の先頭要素かどうかを判定します（要素は eq? で比較します）。

```racket
> a
(list (list 'a 22) (list 'b 8) (list 'c 70))
> (assq 'b a)
(list 'b 8)
```

```
+----------------------+
| [手続き]          |
|                      |
| (caaar x) → any/c    |
| x: list?            |
+----------------------+
```

LISP 風の selector: (car(car(carx)))。

```racket
> w
(list (list (list (list "bye") 3) #true) 42)
> (caaar w)
(list "bye")
```

```
+----------------------+
| [手続き]          |
|                      |
| (caadr x) → any/c    |
| x: list?            |
+----------------------+
```

LISP 風の selector: (car(car(cdrx)))。

```racket
> (caadr (cons 1 (cons (cons 'a '()) (cons (cons 'd '()) '()))))
'a
```

```
+----------------------+
| [手続き]          |
|                      |
| (caar x) → any/c     |
| x: list?            |
+----------------------+
```

LISP 風の selector: (car(carx))。

```racket
> y
(list (list (list 1 2 3) #false "world"))
> (caar y)
(list 1 2 3)
```

```
+----------------------+
| [手続き]          |
|                      |
| (cadar x) → any/c    |
| x: list?            |
+----------------------+
```

LISP 風の selector: (car(cdr(carx)))。

```racket
> w
(list (list (list (list "bye") 3) #true) 42)
> (cadar w)
#true
```

```
+----------------------+
| [手続き]          |
|                      |
| (cadddr x) → any/c   |
| x: list?            |
+----------------------+
```

LISP 風の selector: (car(cdr(cdr(cdrx))))。

```racket
> v
(list 1 2 3 4 5 6 7 8 9 'A)
> (cadddr v)
4
```

```
+----------------------+
| [手続き]          |
|                      |
| (caddr x) → any/c    |
| x: list?            |
+----------------------+
```

LISP 風の selector: (car(cdr(cdrx)))。

```racket
> x
(list 2 "hello" #true)
> (caddr x)
#true
```

```
+----------------------+
| [手続き]          |
|                      |
| (cadr x) → any/c     |
| x: list?            |
+----------------------+
```

LISP 風の selector: (car(cdrx))。

```racket
> x
(list 2 "hello" #true)
> (cadr x)
"hello"
```

```
+----------------------+
| [手続き]          |
|                      |
| (car x) → any/c      |
| x: cons?            |
+----------------------+
```

空でないリストの先頭要素を取り出します。

```racket
> x
(list 2 "hello" #true)
> (car x)
2
```

```
+----------------------+
| [手続き]          |
|                      |
| (cdaar x) → any/c    |
| x: list?            |
+----------------------+
```

LISP 風の selector: (cdr(car(carx)))。

```racket
> w
(list (list (list (list "bye") 3) #true) 42)
> (cdaar w)
(list 3)
```

```
+----------------------+
| [手続き]          |
|                      |
| (cdadr x) → any/c    |
| x: list?            |
+----------------------+
```

LISP 風の selector: (cdr(car(cdrx)))。

```racket
> (cdadr (list 1 (list 2 "a") 3))
(list "a")
```

```
+----------------------+
| [手続き]          |
|                      |
| (cdar x) → list?     |
| x: list?            |
+----------------------+
```

LISP 風の selector: (cdr(carx))。

```racket
> y
(list (list (list 1 2 3) #false "world"))
> (cdar y)
(list #false "world")
```

```
+----------------------+
| [手続き]          |
|                      |
| (cddar x) → any/c    |
| x: list?            |
+----------------------+
```

LISP 風の選択子: (cdr (cdr (car x)))

```racket
> w
(list (list (list (list "bye") 3) #true) 42)
> (cddar w)
'()
```

```
+----------------------+
| [手続き]          |
|                      |
| (cdddr x) → any/c    |
| x: list?            |
+----------------------+
```

LISP 風の selector: (cdr(cdr(cdrx)))。

```racket
> v
(list 1 2 3 4 5 6 7 8 9 'A)
> (cdddr v)
(list 4 5 6 7 8 9 'A)
```

```
+----------------------+
| [手続き]          |
|                      |
| (cddr x) → list?     |
| x: list?            |
+----------------------+
```

LISP 風の selector: (cdr(cdrx))。

```racket
> x
(list 2 "hello" #true)
> (cddr x)
(list #true)
```

```
+----------------------+
| [手続き]          |
|                      |
| (cdr x) → any/c      |
| x: cons?            |
+----------------------+
```

空でないリストの残り（rest）を取り出します。

```racket
> x
(list 2 "hello" #true)
> (cdr x)
(list "hello" #true)
```

```
+----------------------+
| [手続き]          |
|                      |
| (cons x y) → list?   |
| x: any/c            |
| y: list?            |
+----------------------+
```

a list を構築します。

```racket
> (cons 1 '())
(cons 1 '())
```

```
+----------------------+
| [手続き]          |
|                      |
| (cons? x) → boolean? |
| x: any/c            |
+----------------------+
```

some value is a constructed list かどうかを判定します。

```racket
> (cons? (cons 1 '()))
#true
> (cons? 42)
#false
```

```
+----------------------+
| [手続き]          |
|                      |
| (eighth x) → any/c   |
| x: list?            |
+----------------------+
```

the eighth item of a non-empty list を選択します。

```racket
> v
(list 1 2 3 4 5 6 7 8 9 'A)
> (eighth v)
8
```

```
+-----------------------+
| [手続き]           |
|                       |
| (empty? x) → boolean? |
| x: any/c             |
+-----------------------+
```

値が空リストかどうかを判定します。

```racket
> (empty? '())
#true
> (empty? 42)
#false
```

```
+----------------------+
| [手続き]          |
|                      |
| (fifth x) → any/c    |
| x: list?            |
+----------------------+
```

the fifth item of a non-empty list を選択します。

```racket
> v
(list 1 2 3 4 5 6 7 8 9 'A)
> (fifth v)
5
```

```
+----------------------+
| [手続き]          |
|                      |
| (first x) → any/c    |
| x: cons?            |
+----------------------+
```

空でないリストの先頭要素を取り出します。

```racket
> x
(list 2 "hello" #true)
> (first x)
2
```

```
+----------------------+
| [手続き]          |
|                      |
| (fourth x) → any/c   |
| x: list?            |
+----------------------+
```

the fourth item of a non-empty list を選択します。

```racket
> v
(list 1 2 3 4 5 6 7 8 9 'A)
> (fourth v)
4
```

```
+-----------------------+
| [手続き]           |
|                       |
| (length l) → natural? |
| l: list?             |
+-----------------------+
```

the number of items on a list を評価します。

```racket
> x
(list 2 "hello" #true)
> (length x)
3
```

```
+----------------------+
| [手続き]          |
|                      |
| (list x...) → list? |
| x: any/c            |
+----------------------+
```

a list of its arguments を構築します。

```racket
> (list 1 2 3 4 5 6 7 8 9 0)
(cons 1 (cons 2 (cons 3 (cons 4 (cons 5 (cons 6 (cons 7 (cons 8 (cons 9 (cons 0 '()))))))))))
```

```
+-------------------------+
| [手続き]             |
|                         |
| (list* x... l) → list? |
| x: any/c               |
| l: list?               |
+-------------------------+
```

a list by adding multiple items to a list を構築します。

```racket
> x
(list 2 "hello" #true)
> (list* 4 3 x)
(list 4 3 2 "hello" #true)
```

```
+------------------------+
| [手続き]            |
|                        |
| (list-ref x i) → any/c |
| x: list?              |
| i: natural?           |
+------------------------+
```

the indexed item from the list を取り出します。

```racket
> v
(list 1 2 3 4 5 6 7 8 9 'A)
> (list-ref v 9)
'A
```

```
+----------------------+
| [手続き]          |
|                      |
| (list? x) → boolean? |
| x: any/c            |
+----------------------+
```

whether the given value is a list を検査します。

```racket
> (list? 42)
#false
> (list? '())
#true
> (list? (cons 1 (cons 2 '())))
#true
```

```
+-------------------------+
| [手続き]             |
|                         |
| (make-list i x) → list? |
| i: natural?            |
| x: any/c               |
+-------------------------+
```

a list of i copies of x を構築します。

```racket
> (make-list 3 "hello")
(cons "hello" (cons "hello" (cons "hello" '())))
```

```
+-------------------------+
| [手続き]             |
|                         |
| (member x l) → boolean? |
| x: any/c               |
| l: list?               |
+-------------------------+
```

値がリスト上にあるかどうかを判定します（equal? で比較）。

```racket
> x
(list 2 "hello" #true)
> (member "hello" x)
#true
```

```
+--------------------------+
| [手続き]              |
|                          |
| (member? x l) → boolean? |
| x: any/c                |
| l: list?                |
+--------------------------+
```

値がリスト上にあるかどうかを判定します（equal? で比較）。

```racket
> x
(list 2 "hello" #true)
> (member? "hello" x)
#true
```

```
+-----------------------+
| [手続き]           |
|                       |
| (memq x l) → boolean? |
| x: any/c             |
| l: list?             |
+-----------------------+
```

some value x is on some list l, using eq? to compare x with items on l かどうかを判定します。

```racket
> x
(list 2 "hello" #true)
> (memq (list (list 1 2 3)) x)
#false
```

```
+------------------------+
| [手続き]            |
|                        |
| (memq? x l) → boolean? |
| x: any/c              |
| l: list?              |
+------------------------+
```

some value x is on some list l, using eq? to compare x with items on l かどうかを判定します。

```racket
> x
(list 2 "hello" #true)
> (memq? (list (list 1 2 3)) x)
#false
```

```
+---------------------------------+
| [手続き]                     |
|                                 |
| (memv x l) → (or/c #false list) |
| x: any/c                       |
| l: list?                       |
+---------------------------------+
```

ある値がリスト上にあるかどうかを判定し、ある場合は x から始まるリストの接尾辞を生成し、ない場合は false を生成します（値は eqv? 述語で比較します）。

```racket
> x
(list 2 "hello" #true)
> (memv (list (list 1 2 3)) x)
#false
```

```
+----------------------+
| [値]              |
|                      |
| null: list          |
+----------------------+
```

空リストの別名です。

```racket
> null
'()
```

```
+----------------------+
| [手続き]          |
|                      |
| (null? x) → boolean? |
| x: any/c            |
+----------------------+
```

値が空リストかどうかを判定します。

```racket
> (null? '())
#true
> (null? 42)
#false
```

```
+--------------------------------+
| [手続き]                    |
|                                |
| (range start end step) → list? |
| start: number                 |
| end: number                   |
| step: number                  |
+--------------------------------+
```

a list of numbers by stepping from start to end を構築します。

```racket
> (range 0 10 2)
(cons 0 (cons 2 (cons 4 (cons 6 (cons 8 '())))))
```

```
+----------------------+
| [手続き]          |
|                      |
| (remove x l) → list? |
| x: any/c            |
| l: list?            |
+----------------------+
```

a list like the given one, with the first occurrence of the given item removed (comparing values with equal?) を構築します。

```racket
> x
(list 2 "hello" #true)
> (remove "hello" x)
(list 2 #true)
> hello-2
(list 2 "hello" #true "hello")
> (remove "hello" hello-2)
(list 2 #true "hello")
```

```
+--------------------------+
| [手続き]              |
|                          |
| (remove-all x l) → list? |
| x: any/c                |
| l: list?                |
+--------------------------+
```

a list like the given one, with all occurrences of the given item removed (comparing values with equal?) を構築します。

```racket
> x
(list 2 "hello" #true)
> (remove-all "hello" x)
(list 2 #true)
> hello-2
(list 2 "hello" #true "hello")
> (remove-all "hello" hello-2)
(list 2 #true)
```

```
+----------------------+
| [手続き]          |
|                      |
| (rest x) → any/c     |
| x: cons?            |
+----------------------+
```

空でないリストの残り（rest）を取り出します。

```racket
> x
(list 2 "hello" #true)
> (rest x)
(list "hello" #true)
```

```
+----------------------+
| [手続き]          |
|                      |
| (reverse l) → list   |
| l: list?            |
+----------------------+
```

a reversed version of a list を作成します。

```racket
> x
(list 2 "hello" #true)
> (reverse x)
(list #true "hello" 2)
```

```
+----------------------+
| [手続き]          |
|                      |
| (second x) → any/c   |
| x: list?            |
+----------------------+
```

the second item of a non-empty list を選択します。

```racket
> x
(list 2 "hello" #true)
> (second x)
"hello"
```

```
+----------------------+
| [手続き]          |
|                      |
| (seventh x) → any/c  |
| x: list?            |
+----------------------+
```

the seventh item of a non-empty list を選択します。

```racket
> v
(list 1 2 3 4 5 6 7 8 9 'A)
> (seventh v)
7
```

```
+----------------------+
| [手続き]          |
|                      |
| (sixth x) → any/c    |
| x: list?            |
+----------------------+
```

the sixth item of a non-empty list を選択します。

```racket
> v
(list 1 2 3 4 5 6 7 8 9 'A)
> (sixth v)
6
```

```
+----------------------+
| [手続き]          |
|                      |
| (third x) → any/c    |
| x: list?            |
+----------------------+
```

the third item of a non-empty list を選択します。

```racket
> x
(list 2 "hello" #true)
> (third x)
#true
```

### 4.11 Posn

```
+------------------------+
| [手続き]            |
|                        |
| (make-posn x y) → posn |
| x: any/c              |
| y: any/c              |
+------------------------+
```

a posn from two arbitrary values を構築します。

```racket
> (make-posn 3 3)
(make-posn 3 3)
> (make-posn "hello" #true)
(make-posn "hello" #true)
```

```
+----------------------+
| [手続き]          |
|                      |
| (posn-x p) → any/c   |
| p: posn             |
+----------------------+
```

the x component of a posn を取り出します。

```racket
> p
(make-posn 2 -3)
> (posn-x p)
2
```

```
+----------------------+
| [手続き]          |
|                      |
| (posn-y p) → any/c   |
| p: posn             |
+----------------------+
```

the y component of a posn を取り出します。

```racket
> p
(make-posn 2 -3)
> (posn-y p)
-3
```

```
+----------------------+
| [手続き]          |
|                      |
| (posn? x) → boolean? |
| x: any/c            |
+----------------------+
```

its input is a posn かどうかを判定します。

```racket
> q
(make-posn "bye" 2)
> (posn? q)
#true
> (posn? 42)
#false
```

### 4.12 文字

```
+-----------------------------+
| [手続き]                 |
|                             |
| (char->integer c) → integer |
| c: char                    |
+-----------------------------+
```

与えられた文字に対応する数を ASCII 表から調べます（あれば）。

```racket
> (char->integer #\a)
97
> (char->integer #\z)
122
```

```
+---------------------------------+
| [手続き]                     |
|                                 |
| (char-alphabetic? c) → boolean? |
| c: char                        |
+---------------------------------+
```

a character represents an alphabetic character かどうかを判定します。

```racket
> (char-alphabetic? #\Q)
#true
```

```
+-----------------------------------+
| [手続き]                       |
|                                   |
| (char-ci<=? c d e...) → boolean? |
| c: char                          |
| d: char                          |
| e: char                          |
+-----------------------------------+
```

the characters are ordered in an increasing and case-insensitive manner かどうかを判定します。

```racket
> (char-ci<=? #\b #\B)
#true
> (char<=? #\b #\B)
#false
```

```
+----------------------------------+
| [手続き]                      |
|                                  |
| (char-ci<? c d e...) → boolean? |
| c: char                         |
| d: char                         |
| e: char                         |
+----------------------------------+
```

the characters are ordered in a strictly increasing and case-insensitive manner かどうかを判定します。

```racket
> (char-ci<? #\B #\c)
#true
> (char<? #\b #\B)
#false
```

```
+----------------------------------+
| [手続き]                      |
|                                  |
| (char-ci=? c d e...) → boolean? |
| c: char                         |
| d: char                         |
| e: char                         |
+----------------------------------+
```

two characters are equal in a case-insensitive manner かどうかを判定します。

```racket
> (char-ci=? #\b #\B)
#true
```

```
+-----------------------------------+
| [手続き]                       |
|                                   |
| (char-ci>=? c d e...) → boolean? |
| c: char                          |
| d: char                          |
| e: char                          |
+-----------------------------------+
```

the characters are sorted in a decreasing and case-insensitive manner かどうかを判定します。

```racket
> (char-ci>=? #\b #\C)
#false
> (char>=? #\b #\C)
#true
```

```
+----------------------------------+
| [手続き]                      |
|                                  |
| (char-ci>? c d e...) → boolean? |
| c: char                         |
| d: char                         |
| e: char                         |
+----------------------------------+
```

the characters are sorted in a strictly decreasing and case-insensitive manner かどうかを判定します。

```racket
> (char-ci>? #\b #\B)
#false
> (char>? #\b #\B)
#true
```

```
+--------------------------+
| [手続き]              |
|                          |
| (char-downcase c) → char |
| c: char                 |
+--------------------------+
```

the equivalent lower-case character を生成します。

```racket
> (char-downcase #\T)
#\t
```

```
+---------------------------------+
| [手続き]                     |
|                                 |
| (char-lower-case? c) → boolean? |
| c: char                        |
+---------------------------------+
```

a character is a lower-case character かどうかを判定します。

```racket
> (char-lower-case? #\T)
#false
```

```
+------------------------------+
| [手続き]                  |
|                              |
| (char-numeric? c) → boolean? |
| c: char                     |
+------------------------------+
```

a character represents a digit かどうかを判定します。

```racket
> (char-numeric? #\9)
#true
```

```
+------------------------+
| [手続き]            |
|                        |
| (char-upcase c) → char |
| c: char               |
+------------------------+
```

the equivalent upper-case character を生成します。

```racket
> (char-upcase #\t)
#\T
```

```
+---------------------------------+
| [手続き]                     |
|                                 |
| (char-upper-case? c) → boolean? |
| c: char                        |
+---------------------------------+
```

a character is an upper-case character かどうかを判定します。

```racket
> (char-upper-case? #\T)
#true
```

```
+---------------------------------+
| [手続き]                     |
|                                 |
| (char-whitespace? c) → boolean? |
| c: char                        |
+---------------------------------+
```

a character represents space かどうかを判定します。

```racket
> (char-whitespace? #\tab)
#true
```

```
+--------------------------------+
| [手続き]                    |
|                                |
| (char<=? c d e...) → boolean? |
| c: char                       |
| d: char                       |
| e: char                       |
+--------------------------------+
```

the characters are ordered in an increasing manner かどうかを判定します。

```racket
> (char<=? #\a #\a #\b)
#true
```

```
+-------------------------------+
| [手続き]                   |
|                               |
| (char<? x d e...) → boolean? |
| x: char                      |
| d: char                      |
| e: char                      |
+-------------------------------+
```

the characters are ordered in a strictly increasing manner かどうかを判定します。

```racket
> (char<? #\a #\b #\c)
#true
```

```
+-------------------------------+
| [手続き]                   |
|                               |
| (char=? c d e...) → boolean? |
| c: char                      |
| d: char                      |
| e: char                      |
+-------------------------------+
```

the characters are equal かどうかを判定します。

```racket
> (char=? #\b #\a)
#false
```

```
+--------------------------------+
| [手続き]                    |
|                                |
| (char>=? c d e...) → boolean? |
| c: char                       |
| d: char                       |
| e: char                       |
+--------------------------------+
```

the characters are sorted in a decreasing manner かどうかを判定します。

```racket
> (char>=? #\b #\b #\a)
#true
```

```
+-------------------------------+
| [手続き]                   |
|                               |
| (char>? c d e...) → boolean? |
| c: char                      |
| d: char                      |
| e: char                      |
+-------------------------------+
```

the characters are sorted in a strictly decreasing manner かどうかを判定します。

```racket
> (char>? #\A #\z #\a)
#false
```

```
+----------------------+
| [手続き]          |
|                      |
| (char? x) → boolean? |
| x: any/c            |
+----------------------+
```

a value is a character かどうかを判定します。

```racket
> (char? "a")
#false
> (char? #\a)
#true
```

### 4.13 文字列

```
+-------------------------------+
| [手続き]                   |
|                               |
| (explode s) → (listof string) |
| s: string                    |
+-------------------------------+
```

Translates 文字列 へ リスト の 1-letter 文字列s.

```racket
> (explode "cat")
(list "c" "a" "t")
```

```
+---------------------------+
| [手続き]               |
|                           |
| (format f x...) → string |
| f: string                |
| x: any/c                 |
+---------------------------+
```

Formats 文字列, possibly embedding 値s.

```racket
> (format "Dear Dr. ~a:" "Flatt")
"Dear Dr. Flatt:"
> (format "Dear Dr. ~s:" "Flatt")
"Dear Dr. \"Flatt\":"
```

```
+----------------------+
| [手続き]          |
|                      |
| (implode l) → string |
| l: list?            |
+----------------------+
```

Concatenates リスト の 1-letter 文字列s へ one 文字列.

```racket
> (implode (cons "c" (cons "a" (cons "t" '()))))
"cat"
```

```
+--------------------------+
| [手続き]              |
|                          |
| (int->string i) → string |
| i: integer              |
+--------------------------+
```

an integer in [0,55295] or [57344 1114111] to a 1-letter string を変換します。

```racket
> (int->string 65)
"A"
```

```
+---------------------------+
| [手続き]               |
|                           |
| (list->string l) → string |
| l: list?                 |
+---------------------------+
```

a s list of characters into a string を変換します。

```racket
> (list->string (cons #\c (cons #\a (cons #\t '()))))
"cat"
```

```
+----------------------------+
| [手続き]                |
|                            |
| (make-string i c) → string |
| i: natural?               |
| c: char                   |
+----------------------------+
```

a string of length i from c を生成します。

```racket
> (make-string 3 #\d)
"ddd"
```

```
+--------------------------+
| [手続き]              |
|                          |
| (replicate i s) → string |
| i: natural?             |
| s: string               |
+--------------------------+
```

Replicates s i times.

```racket
> (replicate 3 "h")
"hhh"
```

```
+--------------------------+
| [手続き]              |
|                          |
| (string c...) → string? |
| c: char                 |
+--------------------------+
```

Builds 文字列 の given 文字s.

```racket
> (string #\d #\o #\g)
"dog"
```

```
+---------------------------+
| [手続き]               |
|                           |
| (string->int s) → integer |
| s: string                |
+---------------------------+
```

a 1-letter string to an integer in [0,55295] or [57344, 1114111] を変換します。

```racket
> (string->int "a")
97
```

```
+----------------------------------+
| [手続き]                      |
|                                  |
| (string->list s) → (listof char) |
| s: string                       |
+----------------------------------+
```

a string into a list of characters を変換します。

```racket
> (string->list "hello")
(list #\h #\e #\l #\l #\o)
```

```
+--------------------------------------------+
| [手続き]                                |
|                                            |
| (string->number s) → (union number #false) |
| s: string                                 |
+--------------------------------------------+
```

a string into a number, produce false if impossible を変換します。

```racket
> (string->number "-2.03")
-2.03
> (string->number "1-2i")
1-2i
```

```
+-----------------------------+
| [手続き]                 |
|                             |
| (string->symbol s) → symbol |
| s: string                  |
+-----------------------------+
```

a string into a symbol を変換します。

```racket
> (string->symbol "hello")
'hello
```

```
+-----------------------------------+
| [手続き]                       |
|                                   |
| (string-alphabetic? s) → boolean? |
| s: string                        |
+-----------------------------------+
```

all ’letters’ in the string are alphabetic かどうかを判定します。

```racket
> (string-alphabetic? "123")
#false
> (string-alphabetic? "cat")
#true
```

```
+--------------------------------------+
| [手続き]                          |
|                                      |
| (string-contains-ci? s t) → boolean? |
| s: string                           |
| t: string                           |
+--------------------------------------+
```

the first string appears in the second one without regard to the case of the letters かどうかを判定します。

```racket
> (string-contains-ci? "At" "caT")
#true
```

```
+-----------------------------------+
| [手続き]                       |
|                                   |
| (string-contains? s t) → boolean? |
| s: string                        |
| t: string                        |
+-----------------------------------+
```

the first string appears literally in the second one かどうかを判定します。

```racket
> (string-contains? "at" "cat")
#true
```

```
+--------------------------+
| [手続き]              |
|                          |
| (string-copy s) → string |
| s: string               |
+--------------------------+
```

Copies 文字列.

```racket
> (string-copy "hello")
"hello"
```

```
+------------------------------+
| [手続き]                  |
|                              |
| (string-downcase s) → string |
| s: string                   |
+------------------------------+
```

a string like the given one with all ’letters’ as lower case を生成します。

```racket
> (string-downcase "CAT")
"cat"
> (string-downcase "cAt")
"cat"
```

```
+-----------------------------+
| [手続き]                 |
|                             |
| (string-ith s i) → 1string? |
| s: string                  |
| i: natural?                |
+-----------------------------+
```

the ith 1-letter substring from s を取り出します。

```racket
> (string-ith "hello world" 1)
"e"
```

```
+-------------------------+
| [手続き]             |
|                         |
| (string-length s) → nat |
| s: string              |
+-------------------------+
```

判定する:  length の 文字列.

```racket
> (string-length "hello world")
11
```

```
+-----------------------------------+
| [手続き]                       |
|                                   |
| (string-lower-case? s) → boolean? |
| s: string                        |
+-----------------------------------+
```

all ’letters’ in the string are lower case かどうかを判定します。

```racket
> (string-lower-case? "CAT")
#false
```

```
+--------------------------------+
| [手続き]                    |
|                                |
| (string-numeric? s) → boolean? |
| s: string                     |
+--------------------------------+
```

all ’letters’ in the string are numeric かどうかを判定します。

```racket
> (string-numeric? "123")
#true
> (string-numeric? "1-2i")
#false
```

```
+-------------------------+
| [手続き]             |
|                         |
| (string-ref s i) → char |
| s: string              |
| i: natural?            |
+-------------------------+
```

the ith character from s を取り出します。

```racket
> (string-ref "cat" 2)
#\t
```

```
+----------------------------+
| [手続き]                |
|                            |
| (string-upcase s) → string |
| s: string                 |
+----------------------------+
```

a string like the given one with all ’letters’ as upper case を生成します。

```racket
> (string-upcase "cat")
"CAT"
> (string-upcase "cAt")
"CAT"
```

```
+-----------------------------------+
| [手続き]                       |
|                                   |
| (string-upper-case? s) → boolean? |
| s: string                        |
+-----------------------------------+
```

all ’letters’ in the string are upper case かどうかを判定します。

```racket
> (string-upper-case? "CAT")
#true
```

```
+-----------------------------------+
| [手続き]                       |
|                                   |
| (string-whitespace? s) → boolean? |
| s: string                        |
+-----------------------------------+
```

all ’letters’ in the string are white space かどうかを判定します。

```racket
> (string-whitespace? (string-append " " (string #\tab #\newline #\return)))
#true
```

```
+------------------------+
| [手続き]            |
|                        |
| (string? x) → boolean? |
| x: any/c              |
+------------------------+
```

a value is a string かどうかを判定します。

```racket
> (string? "hello world")
#true
> (string? 42)
#false
```

```
+----------------------------+
| [手続き]                |
|                            |
| (substring s i j) → string |
| s: string                 |
| i: natural?               |
| j: natural?               |
+----------------------------+
```

the substring starting at i up to j (or the end if j is not provided) を取り出します。

```racket
> (substring "hello world" 1 5)
"ello"
> (substring "hello world" 1 8)
"ello wo"
> (substring "hello world" 4)
"o world"
```

### 4.14 画像

```
+--------------------------+
| [手続き]              |
|                          |
| (image=? i j) → boolean? |
| i: image                |
| j: image                |
+--------------------------+
```

two images are equal かどうかを判定します。

```racket
> c1
[image:pict_10.png]
> (image=? (circle 5 "solid" "green") c1)
#false
> (image=? (circle 10 "solid" "green") c1)
#true
```

```
+-----------------------+
| [手続き]           |
|                       |
| (image? x) → boolean? |
| x: any/c             |
+-----------------------+
```

a value is an image かどうかを判定します。

```racket
> c1
[image:pict_11.png]
> (image? c1)
#true
```

### 4.15 その他

```
+-------------------------+
| [手続き]             |
|                         |
| (=~ x y eps) → boolean? |
| x: number              |
| y: number              |
| eps: non-negative-real |
+-------------------------+
```

whether x and y are within eps of either other を検査します。

```racket
> (=~ 1.01 1.0 0.1)
#true
> (=~ 1.01 1.5 0.1)
#false
```

```
+----------------------+
| [値]              |
|                      |
| eof: eof-object?    |
+----------------------+
```

A 値 という represents end の file:

```racket
> eof
#<eof>
```

```
+----------------------------+
| [手続き]                |
|                            |
| (eof-object? x) → boolean? |
| x: any/c                  |
+----------------------------+
```

some value is the end-of-file value かどうかを判定します。

```racket
> (eof-object? eof)
#true
> (eof-object? 42)
#false
```

```
+----------------------+
| [手続き]          |
|                      |
| (eq? x y) → boolean? |
| x: any/c            |
| y: any/c            |
+----------------------+
```

two values are equivalent from the computer’s perspective (intensional) かどうかを判定します。

```racket
> (eq? (cons 1 '()) (cons 1 '()))
#false
> one
(list 1)
> (eq? one one)
#true
```

```
+-------------------------+
| [手続き]             |
|                         |
| (equal? x y) → boolean? |
| x: any/c               |
| y: any/c               |
+-------------------------+
```

two values are structurally equal where basic values are compared with the eqv? predicate かどうかを判定します。

```racket
> (equal? (make-posn 1 2) (make-posn (- 2 1) (+ 1 1)))
#true
```

```
+----------------------------+
| [手続き]                |
|                            |
| (equal~? x y z) → boolean? |
| x: any/c                  |
| y: any/c                  |
| z: non-negative-real      |
+----------------------------+
```

x and y like equal? but uses =~ in the case of numbers を比較します。

```racket
> (equal~? (make-posn 1.01 1.0) (make-posn 1.01 0.99) 0.2)
#true
```

```
+-----------------------+
| [手続き]           |
|                       |
| (eqv? x y) → boolean? |
| x: any/c             |
| y: any/c             |
+-----------------------+
```

two values are equivalent from the perspective of all functions that can be applied to it (extensional) かどうかを判定します。

```racket
> (eqv? (cons 1 '()) (cons 1 '()))
#false
> one
(list 1)
> (eqv? one one)
#true
```

```
+-----------------------+
| [手続き]           |
|                       |
| (error x...) → void? |
| x: any/c             |
+-----------------------+
```

Signals an error, combining the given values into an error message. If any of the values’ printed representations is too long, it is truncated and “...” is put into the string. If the first value is a symbol, it is suffixed with a colon and the result pre-pended on to the error message.

```racket
> zero
0
> (if (= zero 0) (error "can't divide by 0") (/ 1 zero))
can't divide by 0
```

```
+----------------------+
| [手続き]          |
|                      |
| (exit) → void        |
+----------------------+
```

Evaluating (exit) terminates running プログラム.

```
+----------------------+
| [手続き]          |
|                      |
| (identity x) → any/c |
| x: any/c            |
+----------------------+
```

x を返します。

```racket
> (identity 42)
42
> (identity c1)
[image:pict_12.png]
> (identity "hello")
"hello"
```

```
+------------------------+
| [手続き]            |
|                        |
| (struct? x) → boolean? |
| x: any/c              |
+------------------------+
```

some value is a structure かどうかを判定します。

```racket
> (struct? (make-posn 1 2))
#true
> (struct? 43)
#false
```

### 4.16 シグネチャ

```
+----------------------+
| [値]              |
|                      |
| Any: signature?     |
+----------------------+
```

any value のシグネチャ。

```
+----------------------+
| [値]              |
|                      |
| Boolean: signature? |
+----------------------+
```

booleans のシグネチャ。

```
+----------------------+
| [値]              |
|                      |
| Char: signature?    |
+----------------------+
```

chararacters のシグネチャ。

```
+------------------------------------------+
| [手続き]                              |
|                                          |
| (ConsOf first-sig rest-sig) → signature? |
| first-sig: signature?                   |
| rest-sig: signature?                    |
+------------------------------------------+
```

a cons pair のシグネチャ。

```
+------------------------+
| [値]                |
|                        |
| EmptyList: signature? |
+------------------------+
```

the empty list のシグネチャ。

```
+----------------------+
| [値]              |
|                      |
| False: signature?   |
+----------------------+
```

just false のシグネチャ。

```
+----------------------+
| [値]              |
|                      |
| Integer: signature? |
+----------------------+
```

integers のシグネチャ。

```
+----------------------+
| [値]              |
|                      |
| Natural: signature? |
+----------------------+
```

natural numbers のシグネチャ。

```
+----------------------+
| [値]              |
|                      |
| Number: signature?  |
+----------------------+
```

arbitrary numbers のシグネチャ。

```
+-----------------------+
| [値]               |
|                       |
| Rational: signature? |
+-----------------------+
```

rational numbers のシグネチャ。

```
+----------------------+
| [値]              |
|                      |
| Real: signature?    |
+----------------------+
```

real numbers のシグネチャ。

```
+----------------------+
| [値]              |
|                      |
| String: signature?  |
+----------------------+
```

strings のシグネチャ。

```
+----------------------+
| [値]              |
|                      |
| Symbol: signature?  |
+----------------------+
```

symbols のシグネチャ。

```
+----------------------+
| [値]              |
|                      |
| True: signature?    |
+----------------------+
```

just true のシグネチャ。

### 4.17 数（緩和条件）

### 4.18 文字列（緩和条件）

```
+--------------------------------+
| [手続き]                    |
|                                |
| (string-append s...) → string |
| s: string                     |
+--------------------------------+
```

Concatenates 文字s の several 文字列s.

```racket
> (string-append "hello" " " "world" " " "good bye")
"hello world good bye"
```

```
+-------------------------------------+
| [手続き]                         |
|                                     |
| (string-ci<=? s t x...) → boolean? |
| s: string                          |
| t: string                          |
| x: string                          |
+-------------------------------------+
```

the strings are ordered in a lexicographically increasing and case-insensitive manner かどうかを判定します。

```racket
> (string-ci<=? "hello" "WORLD" "zoo")
#true
```

```
+------------------------------------+
| [手続き]                        |
|                                    |
| (string-ci<? s t x...) → boolean? |
| s: string                         |
| t: string                         |
| x: string                         |
+------------------------------------+
```

the strings are ordered in a lexicographically strictly increasing and case-insensitive manner かどうかを判定します。

```racket
> (string-ci<? "hello" "WORLD" "zoo")
#true
```

```
+------------------------------------+
| [手続き]                        |
|                                    |
| (string-ci=? s t x...) → boolean? |
| s: string                         |
| t: string                         |
| x: string                         |
+------------------------------------+
```

all strings are equal, character for character, regardless of case かどうかを判定します。

```racket
> (string-ci=?  "hello" "HellO")
#true
```

```
+-------------------------------------+
| [手続き]                         |
|                                     |
| (string-ci>=? s t x...) → boolean? |
| s: string                          |
| t: string                          |
| x: string                          |
+-------------------------------------+
```

the strings are ordered in a lexicographically decreasing and case-insensitive manner かどうかを判定します。

```racket
> (string-ci>?  "zoo" "WORLD" "hello")
#true
```

```
+------------------------------------+
| [手続き]                        |
|                                    |
| (string-ci>? s t x...) → boolean? |
| s: string                         |
| t: string                         |
| x: string                         |
+------------------------------------+
```

the strings are ordered in a lexicographically strictly decreasing and case-insensitive manner かどうかを判定します。

```racket
> (string-ci>?  "zoo" "WORLD" "hello")
#true
```

```
+----------------------------------+
| [手続き]                      |
|                                  |
| (string<=? s t x...) → boolean? |
| s: string                       |
| t: string                       |
| x: string                       |
+----------------------------------+
```

the strings are ordered in a lexicographically increasing manner かどうかを判定します。

```racket
> (string<=? "hello" "hello" "world" "zoo")
#true
```

```
+---------------------------------+
| [手続き]                     |
|                                 |
| (string<? s t x...) → boolean? |
| s: string                      |
| t: string                      |
| x: string                      |
+---------------------------------+
```

the strings are ordered in a lexicographically strictly increasing manner かどうかを判定します。

```racket
> (string<? "hello" "world" "zoo")
#true
```

```
+---------------------------------+
| [手続き]                     |
|                                 |
| (string=? s t x...) → boolean? |
| s: string                      |
| t: string                      |
| x: string                      |
+---------------------------------+
```

all strings are equal, character for character かどうかを判定します。

```racket
> (string=? "hello" "world")
#false
> (string=? "bye" "bye")
#true
```

```
+----------------------------------+
| [手続き]                      |
|                                  |
| (string>=? s t x...) → boolean? |
| s: string                       |
| t: string                       |
| x: string                       |
+----------------------------------+
```

the strings are ordered in a lexicographically decreasing manner かどうかを判定します。

```racket
> (string>=?  "zoo" "zoo" "world" "hello")
#true
```

```
+---------------------------------+
| [手続き]                     |
|                                 |
| (string>? s t x...) → boolean? |
| s: string                      |
| t: string                      |
| x: string                      |
+---------------------------------+
```

the strings are ordered in a lexicographically strictly decreasing manner かどうかを判定します。

```racket
> (string>?  "zoo" "world" "hello")
#true
```

### 4.19 Posn

```
+----------------------+
| [手続き]          |
|                      |
| (posn) → signature   |
+----------------------+
```

posns のシグネチャ。

### 4.20 高階関数

### 4.21 数（緩和条件・拡張）

```
+----------------------+
| [手続き]          |
|                      |
| (* x...) → number   |
| x: number           |
+----------------------+
```

Multiplies すべての given 数s. In ISL と up: * works のとき applied へ only one 数 または none.

```racket
> (* 5 3)
15
> (* 5 3 2)
30
> (* 2)
2
> (*)
1
```

```
+----------------------+
| [手続き]          |
|                      |
| (+ x...) → number   |
| x: number           |
+----------------------+
```

Adds すべての given 数s. In ISL と up: + works のとき applied へ only one 数 または none.

```racket
> (+ 2/3 1/16)
35/48
> (+ 3 2 5 8)
18
> (+ 1)
1
> (+)
0
```

```
+----------------------+
| [手続き]          |
|                      |
| (/ x y...) → number |
| x: number           |
| y: number           |
+----------------------+
```

Divides first によって すべての remaining 数s. In ISL と up: / computes inverse のとき applied へ one 数.

```racket
> (/ 12 2)
6
> (/ 12 2 3)
2
> (/ 3)
1/3
```

```
+----------------------+
| [手続き]          |
|                      |
| (= x...) → number   |
| x: number           |
+----------------------+
```

numbers for equality. In ISL and up: = works when applied to only one number を比較します。

```racket
> (= 10 10)
#true
> (= 11)
#true
> (= 0)
#true
```

### 4.22 高階関数（lambda つき）

```
+---------------------------+
| [手続き]               |
|                           |
| (andmap p? [l]) → boolean |
| p?: (X... -> boolean)   |
| l: (listof X) =...      |
+---------------------------+
```

〜かどうかを判定する:  p? holds のための すべての items の l...:

```racket
(andmap p (list x-1... x-n)) = (and (p x-1)... (p x-n))
```

```racket
(andmap p (list x-1... x-n) (list y-1... y-n)) = (and (p x-1 y-1)... (p x-n y-n))
```

```racket
> (andmap odd? '(1 3 5 7 9))
#true
> threshold
3
> (andmap (lambda (x) (< x threshold)) '(0 1 2))
#true
> (andmap even? '())
#true
> (andmap (lambda (x f) (f x)) (list 0 1 2) (list odd? even? positive?))
#false
```

```
+--------------------------+
| [手続き]              |
|                          |
| (apply f x-1... l) → Y  |
| f: (X-1... X-N -> Y)   |
| x-1: X-1                |
| l: (list X-i+1... X-N) |
+--------------------------+
```

Applies 関数 using items から リスト として 引数s:

```racket
(apply f (list x-1... x-n)) = (f x-1... x-n)
```

```racket
> a-list
(list 0 1 2 3 4 5 6 7 8 9)
> (apply max a-list)
9
```

```
+----------------------+
| [手続き]          |
|                      |
| (argmax f l) → X     |
| f: (X -> real)      |
| l: (listof X)       |
+----------------------+
```

the (first) element of the list that maximizes the output of the function を探します。

```racket
> (argmax second '((sam 98) (carl 78) (vincent 93) (asumu 99)))
(list 'asumu 99)
```

```
+----------------------+
| [手続き]          |
|                      |
| (argmin f l) → X     |
| f: (X -> real)      |
| l: (listof X)       |
+----------------------+
```

the (first) element of the list that minimizes the output of the function を探します。

```racket
> (argmin second '((sam 98) (carl 78) (vincent 93) (asumu 99)))
(list 'carl 78)
```

```
+-------------------------------+
| [手続き]                   |
|                               |
| (build-list n f) → (listof X) |
| n: nat                       |
| f: (nat -> X)                |
+-------------------------------+
```

構築する:  リスト によって applying f へ 数s between 0 と (-n1):

```racket
(build-list n f) = (list (f 0)... (f (- n 1)))
```

```racket
> (build-list 22 add1)
(list 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22)
> i
3
> (build-list 3 (lambda (j) (+ j i)))
(list 3 4 5)
> (build-list 5              (lambda (i)                (build-list 5                            (lambda (j)                              (if (= i j) 1 0)))))
(list (list 1 0 0 0 0) (list 0 1 0 0 0) (list 0 0 1 0 0) (list 0 0 0 1 0) (list 0 0 0 0 1))
```

```
+-----------------------------+
| [手続き]                 |
|                             |
| (build-string n f) → string |
| n: nat                     |
| f: (nat -> char)           |
+-----------------------------+
```

構築する:  文字列 によって applying f へ 数s between 0 と (-n1):

```racket
(build-string n f) = (string (f 0)... (f (- n 1)))
```

```racket
> (build-string 10 integer->char)
"\u0000\u0001\u0002\u0003\u0004\u0005\u0006\a\b\t"
> (build-string 26 (lambda (x) (integer->char (+ 65 x))))
"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
```

```
+--------------------------+
| [手続き]              |
|                          |
| (compose f g) → (X -> Z) |
| f: (Y -> Z)             |
| g: (X -> Y)             |
+--------------------------+
```

（説明）Composes sequence の procedures へ single procedure:

```racket
(compose f g) = (lambda (x) (f (g x)))
```

```racket
> ((compose add1 second) '(add 3))
4
> (map (compose add1 second) '((add 3) (sub 2) (mul 4)))
(list 4 3 5)
```

```
+----------------------------+
| [手続き]                |
|                            |
| (filter p? l) → (listof X) |
| p?: (X -> boolean)        |
| l: (listof X)             |
+----------------------------+
```

a list from all those items on a list for which the predicate holds を構築します。

```racket
> (filter odd? '(0 1 2 3 4 5 6 7 8 9))
(list 1 3 5 7 9)
> threshold
3
> (filter (lambda (x) (>= x threshold)) '(0 1 2 3 4 5 6 7 8 9))
(list 3 4 5 6 7 8 9)
```

```
+--------------------------+
| [手続き]              |
|                          |
| (foldl f base l...) → Y |
| f: (X... Y -> Y)       |
| base: Y                 |
| l: (listof X)           |
+--------------------------+
```

```racket
(foldl f base (list x-1... x-n)) = (f x-n... (f x-1 base))
```

```racket
(foldl f base (list x-1... x-n) (list x-1... x-n))
= (f x-n y-n... (f x-1 y-1 base))
```

```racket
> (foldl + 0 '(0 1 2 3 4 5 6 7 8 9))
45
> a-list
(list 0 1 2 3 4 5 6 7 8 9)
> (foldl (lambda (x r) (if (> x threshold) (cons (* 2 x) r) r)) '() a-list)
(list 18 16 14 12 10 8)
> (foldl (lambda (x y r) (+ x y r)) 0 '(1 2 3) '(10 11 12))
39
```

```
+--------------------------+
| [手続き]              |
|                          |
| (foldr f base l...) → Y |
| f: (X... Y -> Y)       |
| base: Y                 |
| l: (listof X)           |
+--------------------------+
```

```racket
(foldr f base (list x-1... x-n)) = (f x-1... (f x-n base))
```

```racket
(foldr f base (list x-1... x-n) (list y-1... y-n))
= (f x-1 y-1... (f x-n y-n base))
```

```racket
> (foldr + 0 '(0 1 2 3 4 5 6 7 8 9))
45
> a-list
(list 0 1 2 3 4 5 6 7 8 9)
> (foldr (lambda (x r) (if (> x threshold) (cons (* 2 x) r) r)) '() a-list)
(list 8 10 12 14 16 18)
> (foldr (lambda (x y r) (+ x y r)) 0 '(1 2 3) '(10 11 12))
39
```

```
+----------------------------+
| [手続き]                |
|                            |
| (for-each f l...) → void? |
| f: (any... -> any)       |
| l: (listof any)           |
+----------------------------+
```

a function to each item on one or more lists for effect only を適用します。

Although *Intermediate Student とともに Lambda* provides for-each 関数, it は intended へ be used の中の Advanced Student level.

```
+----------------------------+
| [手続き]                |
|                            |
| (map f l...) → (listof Z) |
| f: (X... -> Z)           |
| l: (listof X)             |
+----------------------------+
```

構築する:  new リスト によって applying 関数 へ 各 item 上の one または more existing リストs:

```racket
(map f (list x-1... x-n)) = (list (f x-1)... (f x-n))
```

```racket
(map f (list x-1... x-n) (list y-1... y-n)) = (list (f x-1 y-1)... (f x-n y-n))
```

```racket
> (map add1 (list 3 -4.01 2/5))
(list 4 #i-3.01 1.4)
```

```racket
> (define (tag-with-a x)    (list "a" (+ x 1)))
```

```racket
> (map tag-with-a (list 3 -4.01 2/5))
(list (list "a" 4) (list "a" #i-3.01) (list "a" 1.4))
```

```racket
> (define (add-and-multiply x y)    (+ x (* x y)))
```

```racket
> (map add-and-multiply (list 3 -4 2/5) '(1 2 3))
(list 6 -12 1.6)
```

```
+-----------------------------------------+
| [手続き]                             |
|                                         |
| (memf p? l) → (union #false (listof X)) |
| p?: (X -> any)                         |
| l: (listof X)                          |
+-----------------------------------------+
```

#false if p? produces false for all items on l. If p? produces #true for any of the items on l, memf returns the sub-list starting from that item を生成します。

```racket
> (memf odd? '(2 4 6 3 8 0))
(list 3 8 0)
```

```
+------------------------+
| [手続き]            |
|                        |
| (ormap p? l) → boolean |
| p?: (X -> boolean)    |
| l: (listof X)         |
+------------------------+
```

〜かどうかを判定する:  p? holds のための at least one items の l:

```racket
(ormap p (list x-1... x-n)) = (or (p x-1)... (p x-n))
```

```racket
(ormap p (list x-1... x-n) (list y-1... y-n)) = (or (p x-1 y-1)... (p x-n y-n))
```

```racket
> (ormap odd? '(1 3 5 7 9))
#true
> threshold
3
> (ormap (lambda (x) (< x threshold)) '(6 7 8 1 5))
#true
> (ormap even? '())
#false
> (ormap (lambda (x f) (f x)) (list 0 1 2) (list odd? even? positive?))
#true
```

```
+---------------------------+
| [手続き]               |
|                           |
| (procedure? x) → boolean? |
| x: any                   |
+---------------------------+
```

true if the value is a procedure を生成します。

```racket
> (procedure? cons)
#true
> (procedure? add1)
#true
> (procedure? (lambda (x) (> x 22)))
#true
```

```
+---------------------------------+
| [手続き]                     |
|                                 |
| (quicksort l comp) → (listof X) |
| l: (listof X)                  |
| comp: (X X -> boolean)         |
+---------------------------------+
```

Sorts items 上の l, の中の order according へ comp (using quicksort algorithm).

```racket
> (quicksort '(6 7 2 1 3 4 0 5 9 8) <)
(list 0 1 2 3 4 5 6 7 8 9)
```

```
+----------------------------+
| [手続き]                |
|                            |
| (sort l comp) → (listof X) |
| l: (listof X)             |
| comp: (X X -> boolean)    |
+----------------------------+
```

Sorts items 上の l, の中の order according へ comp.

```racket
> (sort '(6 7 2 1 3 4 0 5 9 8) <)
(list 0 1 2 3 4 5 6 7 8 9)
```
