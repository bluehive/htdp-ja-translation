# 付録 B-5: Advanced Student（#lang htdp/asl）

**原題:** Advanced Student  
**原本:** `extracted/appendix/htdp-langs/original_markdown_05_advanced.md`

説明文を日本語に翻訳しています。コード・シグネチャ・実行例・文法表の識別子は原文のまま保持します。

## 5 Advanced Student（上級学生言語）

文法の記法では、X...（太字の点）という書き方で、X が任意の回数（0回、1回、またはそれ以上）現れてよいことを示します。別に、文法はテンプレートで使う識別子として ... も定義します。

```
+--------------------------------------+--+---+--+--------------------------------------+
| program                              |  | = |  | def-or-expr...                      |
+--------------------------------------+--+---+--+--------------------------------------+
| def-or-expr                          |  | = |  | definition                           |
|                                      |  | | |  | expr                                 |
|                                      |  | | |  | test-case                            |
|                                      |  | | |  | library-require                      |
|                                      |  | | |  | signature-declaration                |
| definition                           |  | = |  | (define (name variable...) expr)    |
|                                      |  | | |  | (define name expr)                   |
|                                      |  | | |  | (define-struct name (name...))      |
|                                      |  | | |  | (define-datatype name (name name..… |
| expr                                 |  | = |  | (begin expr expr...)                |
|                                      |  | | |  | (begin0 expr expr...)               |
|                                      |  | | |  | (set! variable expr)                 |
|                                      |  | | |  | (delay expr)                         |
|                                      |  | | |  | (lambda (variable...) expr)         |
|                                      |  | | |  | (λ (variable...) expr)              |
|                                      |  | | |  | (local [definition...] expr)        |
|                                      |  | | |  | (letrec ([name expr]...) expr)      |
|                                      |  | | |  | (shared ([name expr]...) expr)      |
|                                      |  | | |  | (let ([name expr]...) expr)         |
|                                      |  | | |  | (let name ([name expr]...) expr)    |
|                                      |  | | |  | (let* ([name expr]...) expr)        |
|                                      |  | | |  | (recur name ([name expr]...) expr)  |
|                                      |  | | |  | (expr expr...)                      |
|                                      |  | | |  | (cond [expr expr]... [expr expr])   |
|                                      |  | | |  | (cond [expr expr]... [else expr])   |
|                                      |  | | |  | (case expr [(choice choice...) exp… |
| (case expr [(choice choice...) exp… |  |   |  |                                      |
|            [(choice choice...) exp… |  |   |  |                                      |
|                                      |  | | |  | (case expr [(choice choice...) exp… |
| (case expr [(choice choice...) exp… |  |   |  |                                      |
|            [else expr])              |  |   |  |                                      |
|                                      |  | | |  | (match expr [pattern expr]...)      |
|                                      |  | | |  | (if expr expr expr)                  |
|                                      |  | | |  | (when expr expr)                     |
|                                      |  | | |  | (unless expr expr)                   |
|                                      |  | | |  | (and expr expr expr...)             |
|                                      |  | | |  | (or expr expr expr...)              |
|                                      |  | | |  | (time expr)                          |
|                                      |  | | |  | name                                 |
|                                      |  | | |  | ’quoted                              |
|                                      |  | | |  | ‘quasiquoted                         |
|                                      |  | | |  | ’()                                  |
|                                      |  | | |  | number                               |
|                                      |  | | |  | boolean                              |
|                                      |  | | |  | string                               |
|                                      |  | | |  | character                            |
|                                      |  | | |  | (signature signature-form)           |
| choice                               |  | = |  | name                                 |
|                                      |  | | |  | number                               |
| pattern                              |  | = |  | _                                    |
|                                      |  | | |  | name                                 |
|                                      |  | | |  | number                               |
|                                      |  | | |  | true                                 |
|                                      |  | | |  | false                                |
|                                      |  | | |  | string                               |
|                                      |  | | |  | character                            |
|                                      |  | | |  | ’quoted                              |
|                                      |  | | |  | ‘quasiquoted-pattern                 |
|                                      |  | | |  | (cons pattern pattern)               |
|                                      |  | | |  | (list pattern...)                   |
|                                      |  | | |  | (list* pattern...)                  |
|                                      |  | | |  | (struct id (pattern...))            |
|                                      |  | | |  | (vector pattern...)                 |
|                                      |  | | |  | (box pattern)                        |
| quasiquoted-pattern                  |  | = |  | name                                 |
|                                      |  | | |  | number                               |
|                                      |  | | |  | string                               |
|                                      |  | | |  | character                            |
|                                      |  | | |  | (quasiquoted-pattern...)            |
|                                      |  | | |  | ’quasiquoted-pattern                 |
|                                      |  | | |  | ‘quasiquoted-pattern                 |
|                                      |  | | |  | `,`pattern                           |
|                                      |  | | |  | `,@`pattern                          |
| signature-declaration                |  | = |  | (: name signature-form)              |
| signature-form                       |  | = |  | (enum expr...)                      |
|                                      |  | | |  | (mixed signature-form...)           |
|                                      |  | | |  | (signature-form... -> signature-fo… |
|                                      |  | | |  | (ListOf signature-form)              |
|                                      |  | | |  | signature-variable                   |
|                                      |  | | |  | expr                                 |
| signature-variable                   |  | = |  | %name                                |
| quoted                               |  | = |  | name                                 |
|                                      |  | | |  | number                               |
|                                      |  | | |  | string                               |
|                                      |  | | |  | character                            |
|                                      |  | | |  | (quoted...)                         |
|                                      |  | | |  | ’quoted                              |
|                                      |  | | |  | ‘quoted                              |
|                                      |  | | |  | `,`quoted                            |
|                                      |  | | |  | `,@`quoted                           |
| quasiquoted                          |  | = |  | name                                 |
|                                      |  | | |  | number                               |
|                                      |  | | |  | string                               |
|                                      |  | | |  | character                            |
|                                      |  | | |  | (quasiquoted...)                    |
|                                      |  | | |  | ’quasiquoted                         |
|                                      |  | | |  | ‘quasiquoted                         |
|                                      |  | | |  | `,`expr                              |
|                                      |  | | |  | `,@`expr                             |
| test-case                            |  | = |  | (check-expect expr expr)             |
|                                      |  | | |  | (check-random expr expr)             |
|                                      |  | | |  | (check-within expr expr expr)        |
|                                      |  | | |  | (check-error expr expr...)          |
|                                      |  | | |  | (check-member-of expr expr expr)     |
|                                      |  | | |  | (check-satisfied expr expr)          |
|                                      |  | | |  | (check-range expr expr)              |
|                                      |  | | |  | (check-range expr)                   |
| library-require                      |  | = |  | (require string)                     |
|                                      |  | | |  | (require (lib string string...))    |
|                                      |  | | |  | (require (planet string package))    |
| package                              |  | = |  | (string string number number)        |
+--------------------------------------+--+---+--+--------------------------------------+
```

名前 (name) または変数 (variable) は、空白や次の文字を含まない文字の並びです。

", ' `
( ) [ ]
{ } |;
#

数 (number) とは、123、3/2、5.5 のような数です。

真偽値 (boolean) は #true または #false のいずれかです。

#true 定数の別表記は #t、true、#T です。同様に #f、false、#F も #false として認識されます。

シンボル (symbol) は、クォート文字に続く名前です。シンボルは 42、'()、#false などと同じく値です。

文字列 (string) は、一対の " で囲まれた文字の並びです。シンボルと違い、文字列は文字に分割したり、さまざまな関数で操作したりできます。たとえば "abcdef"、"This is a string"、および "This is a string with \" inside" はすべて文字列です。

文字 (character) は #\ で始まり、その文字の名前を持ちます。たとえば #\a、#\b、#\space は文字です。

関数呼び出しでは、開き括弧の直後に現れる関数は、define や define-struct で定義した関数、またはあらかじめ定義された関数のいずれかです。

### 5.1 あらかじめ定義された変数

```
+----------------------+
| [値]                 |
|                      |
| empty: empty?       |
+----------------------+
```

空リスト。

```
+----------------------+
| [値]                 |
|                      |
| true: boolean?      |
+----------------------+
```

#true の値。

```
+----------------------+
| [値]                 |
|                      |
| false: boolean?     |
+----------------------+
```

#false の値。

### 5.2 テンプレート変数

```
+----------------------+
| [構文]               |
|                      |
|..                   |
+----------------------+
```

関数定義がテンプレートであることを示すためのプレースホルダ。

```
+----------------------+
| [構文]               |
|                      |
|...                  |
+----------------------+
```

関数定義がテンプレートであることを示すためのプレースホルダ。

```
+----------------------+
| [構文]               |
|                      |
|....                 |
+----------------------+
```

関数定義がテンプレートであることを示すためのプレースホルダ。

```
+----------------------+
| [構文]               |
|                      |
|.....                |
+----------------------+
```

関数定義がテンプレートであることを示すためのプレースホルダ。

```
+----------------------+
| [構文]               |
|                      |
|......               |
+----------------------+
```

関数定義がテンプレートであることを示すためのプレースホルダ。

### 5.3 上級の構文

上級学生言語（Advanced）では、set! を使って変数を破壊的更新（ミューテーション）できます。また define-struct が定義する構造体も破壊的更新が可能です。define と lambda は引数ゼロの関数を定義でき、関数呼び出しも引数ゼロの関数を呼び出せます。

```
+------------------------------------+
| [構文]                             |
|                                    |
| (lambda (variable...) expression) |
+------------------------------------+
```

与えられた変数と同じ個数の引数を取り、本体が expression である関数を作ります。

```
+-------------------------------+
| [構文]                        |
|                               |
| (λ (variable...) expression) |
+-------------------------------+
```

ギリシャ文字 λ は lambda の同義語です。

```
+-----------------------------+
| [構文]                      |
|                             |
| (expression expression...) |
+-----------------------------+
```

最初の expression を評価して得られる関数を呼び出します。呼び出しの値は、その関数本体において、各変数が対応する式の値に置き換えられたときの本体の値です。

呼び出される関数は、その関数呼び出しより前に現れる定義から来るものか、lambda 式から来るものでなければなりません。引数式の個数は、その関数が期待する引数の個数と一致している必要があります。

```
+------------------------------------------------------------------+
| [構文]                                                           |
|                                                                  |
| (define-datatype dataype-name [variant-name field-name...]...) |
+------------------------------------------------------------------+
```

関連する構造体のグループを定義するための短縮記法です。次の define-datatype:

```racket
(define-datatype datatype-name
  [variant-name field-name #,...]
...)
```

は、次と等価です。

```racket
(define (datatype-name? x)
  (or (variant-name? x)...))
(define-struct variant-name (field-name...))
...
```

```
+-----------------------------------+
| [構文]                            |
|                                   |
| (begin expression expression...) |
+-----------------------------------+
```

式を左から右の順に評価します。begin 式の値は、最後の式の値です。

```
+------------------------------------+
| [構文]                             |
|                                    |
| (begin0 expression expression...) |
+------------------------------------+
```

式を左から右の順に評価します。begin0 式の値は、最初の式の値です。

```
+----------------------------+
| [構文]                     |
|                            |
| (set! variable expression) |
+----------------------------+
```

expression を評価し、その値で variable の値を書き換えます。変数は define、letrec、let*、let、または local で定義されていなければなりません。

```
+----------------------+
| [構文]               |
|                      |
| (delay expression)   |
+----------------------+
```

expression を評価する「約束（promise）」を生成します。式は force でその約束が強制されるまで評価されません。約束が強制されると結果が記録され、それ以降の force は記憶された値を直ちに返します。

```
+---------------------------------------------+
| [構文]                                      |
|                                             |
| (shared ([name expression]...) expression) |
+---------------------------------------------+
```

letrec と同様ですが、識別子の横の式が cons、list、vector、準クォート式、あるいは define-struct 由来の make-struct-name であるとき、その式は先に定義された名前に限らず任意の name を直接参照できます。したがって shared は循環データ構造を作るのに使えます。

```
+-------------------------------------------------+
| [構文]                                          |
|                                                 |
| (recur name ([name expression]...) expression) |
+-------------------------------------------------+
```

再帰ループのための短縮構文です。最初の name は再帰関数の名前に対応します。括弧内の name は関数の引数であり、それぞれに対応する expression は、関数への最初の呼び出しでその引数に渡される値です。最後の expression は関数の本体です。

より正確には、次の recur:

```racket
(recur func-name ([arg-name arg-expression]...)
  body-expression)
```

は、次と等価です。

```racket
(local [(define (func-name arg-name...) body-expression)]
  (func-name arg-expression...))
```

```
+-----------------------------------------------+
| [構文]                                        |
|                                               |
| (let name ([name expression]...) expression) |
+-----------------------------------------------+
```

recur の別構文です。

```
+---------------------------------------------------------------------------+
| [構文]                                                                    |
|                                                                           |
| (case expression [(choice...) expression]... [(choice...) expression]) |
+---------------------------------------------------------------------------+
```

case 形式は 1 つ以上の節を含みます。各節は、選択肢（括弧内）—数または名前—と答の式を含みます。先頭の式が評価され、その値が各節の選択肢と比較されます。節は上から順に調べられます。一致する選択肢を含む最初の行が答の式を提供し、その値が case 式全体の結果になります。数は選択肢中の数と、シンボルは名前と一致します。どの行にも一致する選択肢がなければエラーです。

```
+-------------------------------------------------------------------+
| [構文]                                                            |
|                                                                   |
| (case expression [(choice...) expression]... [else expression]) |
+-------------------------------------------------------------------+
```

この形式の case は直前のものと同様ですが、どの節にも先頭の式の値と一致する選択肢がなければ、最後の else 節が使われます。

```
+---------------------------------------------+
| [構文]                                      |
|                                             |
| (match expression [pattern expression]...) |
+---------------------------------------------+
```

match 形式は、角括弧で囲まれた 1 つ以上の節を含みます。各節はパターン—値の記述—と答の式を含みます。先頭の式が評価され、その値が各節のパターンと照合されます。節は上から順に調べられます。一致するパターンを含む最初の節が答の式を提供し、その値が match 式全体の結果になります。この式は、一致したパターンで定義された識別子を参照できます。どの節にも一致するパターンがなければエラーです。

```
+--------------------------------------------+
| [構文]                                     |
|                                            |
| (when question-expression body-expression) |
+--------------------------------------------+
```

question-expression が真に評価される場合、when 式の結果は body-expression を評価した結果です。そうでなければ結果は (void) となり、body-expression は評価されません。question-expression の評価結果が真でも偽でもない場合はエラーです。

```
+----------------------------------------------+
| [構文]                                       |
|                                              |
| (unless question-expression body-expression) |
+----------------------------------------------+
```

when と同様ですが、question-expression が偽を生成するときに body-expression が評価されます（真のときではありません）。

### 5.4 共通の構文

次の構文は、*上級学生言語（Advanced）* レベルでも、中級学生言語（Lambda 付き）レベルと同じように振る舞います。

```
+-------------------------------------+
| [構文]                              |
|                                     |
| (local [definition...] expression) |
+-------------------------------------+
```

expression の中で使うための、関連する定義をまとめます。各定義は define または define-struct のいずれかです。

local を評価するとき、各定義が順に評価され、最後に本体の expression が評価されます。定義によって導入された名前を参照できるのは、local 内の式だけです（定義の右辺と本体の expression を含みます）。local で定義された名前がトップレベルの束縛と同じ場合、内側のものが外側のものを「シャドウ」します。つまり local の内側では、その名前への参照は内側のものを指します。

```
+-----------------------------------------------+
| [構文]                                        |
|                                               |
| (letrec ([name expr-for-let]...) expression) |
+-----------------------------------------------+
```

local と同様ですが、構文がより単純です。各 name は、対応する expr-for-let の値をもつ変数（または関数）を定義します。expr-for-let が lambda であれば letrec は関数を定義し、そうでなければ変数を定義します。

```
+---------------------------------------------+
| [構文]                                      |
|                                             |
| (let* ([name expr-for-let]...) expression) |
+---------------------------------------------+
```

letrec と同様ですが、各 name は expression、およびその name より後に現れる expr-for-let の中でのみ使えます。

```
+--------------------------------------------+
| [構文]                                     |
|                                            |
| (let ([name expr-for-let]...) expression) |
+--------------------------------------------+
```

letrec と同様ですが、定義された名前は最後の expression でのみ使え、名前の横の expr-for-let では使えません。

```
+----------------------+
| [構文]               |
|                      |
| (time expression)    |
+----------------------+
```

expression の評価にかかった時間を測ります。expression を評価したあと、time はその評価にかかった時間（実時間、CPU 時間、空きメモリ回収に費やした時間を含む）を表示します。time の値は expression の値と同じです。

```
+--------------------------------------------------+
| [構文]                                           |
|                                                  |
| (define (name variable variable...) expression) |
+--------------------------------------------------+
```

name という名前の関数を定義します。expression は関数の本体です。関数が呼ばれると、引数の値が変数の代わりに本体へ挿入されます。関数は、その新しい式の値を返します。

関数名は、他の関数や変数と同じであってはなりません。

```
+--------------------------+
| [構文]                   |
|                          |
| (define name expression) |
+--------------------------+
```

expression の値で name という変数を定義します。変数名は他の関数や変数と同じであってはならず、name 自身が expression に現れてはなりません。

```
+-------------------------------------------------+
| [構文]                                          |
|                                                 |
| (define-struct structure-name (field-name...)) |
+-------------------------------------------------+
```

structure-name という新しい構造体を定義します。構造体のフィールドは field-name たちで名付けられます。define-struct のあと、次の新しい関数が利用可能になります。

- make-structure-name: 構造体のフィールド数と同じ個数の引数を取り、その構造体の新しいインスタンスを作ります。
- structure-name-field-name: 構造体のインスタンスを取り、field-name で名付けられたフィールドの値を返します。
- structure-name?: 任意の値を取り、その値が構造体のインスタンスであれば #true を返します。

define-struct が導入する新しい関数の名前は、他の関数や変数と同じであってはなりません。そうでなければ define-struct はエラーを報告します。

上級学生言語（Advanced）では、define-struct は次の追加関数も導入します。

- set-structure-name-field-name!
: 構造体のインスタンスと値を取り、そのインスタンスのフィールドを与えられた値へ破壊的更新します。

```
+-----------------------------------------------------------------------------+
| [構文]                                                                      |
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
| [構文]                      |
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

question-expression の値が #true のとき、if は then-answer-expression を評価します。判定が #false のとき、if は else-answer-expression を評価します。

question-expression が #true でも #false でもない場合、if はエラーを報告します。

```
+--------------------------------------------+
| [構文]                                     |
|                                            |
| (and expression expression expression...) |
+--------------------------------------------+
```

すべての式が #true であれば #true に評価されます。いずれかの式が #false であれば、and 式は #false に評価されます（その式より右の式は評価されません）。

いずれかの式が #true でも #false でもない値に評価された場合、and はエラーを報告します。

```
+-------------------------------------------+
| [構文]                                    |
|                                           |
| (or expression expression expression...) |
+-------------------------------------------+
```

いずれかの式が #true になった時点で #true に評価されます（その式より右の式は評価されません）。すべての式が #false であれば、or 式は #false に評価されます。

いずれかの式が #true でも #false でもない値に評価された場合、or はエラーを報告します。

```
+-----------------------------------------------+
| [構文]                                        |
|                                               |
| (check-expect expression expected-expression) |
+-----------------------------------------------+
```

最初の expression が、expected-expression と同じ値に評価されることを検査します。

```racket
(check-expect (fahrenheit->celsius 212) 100)
(check-expect (fahrenheit->celsius -40) -40)

(define (fahrenheit->celsius f)
  (* 5/9 (- f 32)))
```

check-expect 式は、学生プログラムのトップレベルに置かなければなりません。また、テスト対象の関数定義より前を含め、プログラムのどこにでも現れ得ます。そこに check-expect を置くことで、プログラマは動作する例とともにプログラムの意図を将来の読者に伝えられ、関数定義本体そのものを読む必要がしばしばなくなります。check-expect（およびすべての check 形式）の構文エラーは、学生が完全な関数ヘッダを必ずしも書か*なくても*テストを書けるよう、意図的に実行時まで遅延されます。

expr または expected-expr が非正確数や関数値を生成するのはエラーです。非正確数については、素朴な等値比較を行うのは原理的に誤りです。代わりに、両者が小さな区間内にあるかを検査します。check-within を参照してください。関数については（中級以上）、関数同士を比較することは証明可能に不可能です。

```
+-----------------------------------------------+
| [構文]                                        |
|                                               |
| (check-random expression expected-expression) |
+-----------------------------------------------+
```

最初の expression が、expected-expression と同じ値に評価されることを検査します。

この形式は、両側に同じ乱数生成器を与えます。両側が同じ区間から同じ順序で乱数を要求すれば、同じ乱数を受け取ります。

check-random が役立つ単純な例を示します。

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

check-random の両側で、random が同じ数に対して同じ順序で呼ばれている点に注意してください。両側が異なる区間に対して random を呼ぶと、失敗しやすくなります。

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

a-helper-function への引数が先に評価されるため、random はまず区間 [0,HEIGHT) に対して呼ばれ、次に [0,WIDTH) に対して呼ばれます。つまり、直前の check-random とは異なる順序です。

expr または expected-expr が関数値や非正確数を生成するのはエラーです。詳細は check-expect の注を参照してください。

```
+----------------------------------------+
| [構文]                                 |
|                                        |
| (check-satisfied expression predicate) |
+----------------------------------------+
```

最初の expression が、名前付きの述語（1 引数の関数）を満たすことを検査します。「満たす」とは、「その関数が与えられた値に対して #true を生成する」という意味です。

check-satisfied の単純な例を示します。

```racket
> (check-satisfied 1 odd?)
The test passed!
```

```racket
> (check-satisfied 1 even?)
Ran 1 test.                                       0 tests passed.                                   Check failures:                                                        ┌───┐                                Actual value │ 1 │ does not satisfy even?.                     └───┘                        at line 3, column 0
```

一般に check-satisfied は、プログラム設計者が定義済み関数を使ってテスト群を定式化できるようにします。

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
| [構文]                                              |
|                                                     |
| (check-within expression expected-expression delta) |
+-----------------------------------------------------+
```

式 expression の値が、expected-expression 式が生成する値と構造的に等しいかどうかを検査します。最初の式中の各数は、2 番目の式中の対応する数から delta 以内でなければなりません。

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

入れ子になったデータに非正確数が含まれるため、検査には check-within が正しい選択です。delta が十分に大きければ、テストは成功します。

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

expression または expected-expression が関数値を生成するのはエラーです。詳細は check-expect の注を参照してください。

delta が数でない場合、check-within はエラーを報告します。

```
+-------------------------------------------------+
| [構文]                                          |
|                                                 |
| (check-error expression expected-error-message) |
| (check-error expression)                        |
+-------------------------------------------------+
```

expression がエラーを報告することを検査します。expected-error-message がある場合は、エラーメッセージがその値と一致することも要求します。

check-error の使用を求める典型的な初学者向けの例を示します。

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

この文脈で次の 2 つの例を考えてみましょう。

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
| [構文]                                                 |
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

いずれかの式が関数値を生成するのはエラーです。詳細は check-expect の注を参照してください。

```
+---------------------------------------------------------+
| [構文]                                                  |
|                                                         |
| (check-range expression low-expression high-expression) |
+---------------------------------------------------------+
```

最初の expression の値が、low-expression の値と high-expression の値の間（両端を含む）にある数であることを検査します。

check-range 形式は、非正確数を計算する関数の可能な結果を区切るのに最適です。

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

expression、low-expression、または high-expression が関数値を生成するのはエラーです。詳細は check-expect の注を参照してください。

```
+----------------------+
| [構文]               |
|                      |
| (require string)     |
+----------------------+
```

string で指定されたモジュールの定義を、現在のモジュール（すなわち現在のファイル）で利用可能にします。string は現在のファイルからの相対パスを指します。

string には、プラットフォームごとのパス規約の違いによる問題を避けるため、いくつかの制約があります。/ はディレクトリ区切りです。. は常にカレントディレクトリを、.. は常に親ディレクトリを意味します。パス要素に使えるのは a から z（大文字・小文字）、0 から 9、-、_、. のみです。また string は空であってはならず、先頭または末尾の / を含んではなりません。

```
+-----------------------+
| [構文]                |
|                       |
| (require module-name) |
+-----------------------+
```

インストール済みライブラリ内のファイルへアクセスします。ライブラリ名は識別子で、相対パス文字列と同じ制約があります（ただし引用符は不要です）。さらに .. を含んではならないという追加の制約があります。

```
+-----------------------------------+
| [構文]                            |
|                                   |
| (require (lib string string...)) |
+-----------------------------------+
```

インストール済みライブラリ内のファイルへアクセスし、その定義を現在のモジュール（すなわち現在のファイル）で利用可能にします。最初の string はライブラリファイル名、残りの string はファイルがインストールされているコレクション（およびサブコレクションなど）の名前です。各 string には (require string) 形式と同じ制約が課されます。

```
+---------------------------------------------------------+
| [構文]                                                  |
|                                                         |
| (require (planet string (string string number number))) |
+---------------------------------------------------------+
```

インターネット上の PLaneT サーバ経由で配布されているライブラリへアクセスし、その定義を現在のモジュール（すなわち現在のファイル）で利用可能にします。

planet の require の完全な文法は Importing and Exporting: require and provide に示されていますが、構文の例を探す最良の場所は、特定のパッケージの説明がある PLaneT サーバ上です。

### 5.5 あらかじめ定義された関数

### 5.6 シグネチャ

> シグネチャはコメントである必要はありません。コードの一部にもできます。シグネチャが関数に付いているとき、DrRacket はプログラムがそのシグネチャに従って関数を使っているかを検査し、テスト結果とともにシグネチャ違反を表示します。シグネチャは通常の値であり、シグネチャ形式として指定されます。シグネチャ形式は、シグネチャ宣言およびシグネチャ式の内側でのみ働く特別な構文です。

```
+-------------------------+
| [構文]                  |
|                         |
| (: name signature-form) |
+-------------------------+
```

signature-form で指定されたシグネチャを、name の定義に付けます。プログラムのどこかに name の定義がなければなりません。

```racket
(: age Integer)
(define age 42)

(: area-of-square (Number -> Number))
(define (area-of-square len)
  (sqr len))
```

プログラムを実行すると、Racket は : で付けられたシグネチャが実際に変数の値と一致するかを検査します。一致しない場合、Racket はテスト失敗とともにシグネチャ違反を報告します。

たとえば、次のコードは:

```racket
(: age Integer)
(define age "fortytwo")
```

次の出力を生じます。

```
+--------------------------------------------------+
| `1 signature violation.`                         |
+--------------------------------------------------+
| `Signature violations:`                          |
| `got "fortytwo" at line 2, column 12, signature… |
+--------------------------------------------------+
```

なお、シグネチャ違反があっても実行中のプログラムは停止しません。

```
+----------------------------+
| [構文]                     |
|                            |
| (signature signature-form) |
+----------------------------+
```

signature-form が記述するシグネチャを値として返します。

#### 5.6.1 シグネチャ形式

> 任意の式はシグネチャ形式になれます。その場合、シグネチャはその式が返す値です。ただし、特別なシグネチャ形式がいくつかあります。シグネチャ形式の中で、% で始まる名前はシグネチャ変数であり、シグネチャの使われ方に応じて任意のシグネチャを表します。例:

```racket
(: same (%a -> %a))

(define (same x) x)
```

```
+-----------------------------------------------------+
| [構文]                                              |
|                                                     |
| (input-signature-form... -> output-signature-form) |
+-----------------------------------------------------+
```

このシグネチャ形式は、入力が input-signature-form たちで記述され、出力が output-signature-form で記述される関数を表します。

```
+----------------------+
| [構文]               |
|                      |
| (enum expr...)      |
+----------------------+
```

このシグネチャは、expr たちが返す値の列挙を記述します。

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
| [構文]                     |
|                            |
| (mixed signature-form...) |
+----------------------------+
```

このシグネチャは混合データ、すなわち各場合が signature-form で記述されるシグネチャをもつ項目化を記述します。

例:

```racket
(define SIGS (signature (mixed Aim Fired)))
```

```
+-------------------------+
| [構文]                  |
|                         |
| (ListOf signature-form) |
+-------------------------+
```

このシグネチャは、要素が signature-form で記述されるリストを記述します。

```
+------------------------+
| [構文]                 |
|                        |
| (predicate expression) |
+------------------------+
```

このシグネチャは述語を通じて値を記述します。expression は、真偽値を返す 1 引数の関数に評価されなければなりません。シグネチャは、その述語が #true を返すすべての値と一致します。

#### 5.6.2 構造体シグネチャ

> 上級学生言語の define-struct 形式は、シグネチャで使える 2 つの追加の名前を定義します。struct という構造体に対して、それらは Struct と StructOf です。これらの名前は大文字で始まることに注意してください。特に、Struct という構造体も Struct と StructOf を定義します。さらに、追加の名前を作るとき、ハイフンは取り除かれ、ハイフンの直後の各文字は大文字になります。したがって foo-bar という構造体は FooBar と FooBarOf を定義します。Struct は、この構造体型の構造体値を記述するシグネチャです。StructOf は、各フィールドのシグネチャを入力として取る関数です。それはこの構造体型の値を記述し、加えてその値のフィールドの値も記述するシグネチャを返します。

```racket
(define-struct pair [fst snd])

(: add-pair ((PairOf Number Number) -> Number))
(define (add-pair p)
  (+ (pair-fst p) (pair-snd p)))
```

以降の各節では、プログラミング言語に組み込まれている関数を列挙します。それ以外の関数はティーチパックからインポートするか、プログラム中で定義しなければなりません。

### 5.7 数: 整数・有理数・実数・複素数・正確数・非正確数

```
+----------------------+
| [手続き]          |
|                      |
| (- x y...) → number |
| x: number           |
| y: number           |
+----------------------+
```

第1引数から第2（およびそれ以降）の数を引きます。
引数が1つだけのときは、その数の符号を反転します。

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

2つ以上の（実）数について、左から順に「より小さい」関係が成り立つかを比較します。

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

2つ以上の（実）数について、左から順に「以下」の関係が成り立つかを比較します。

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

2つ以上の（実）数について、左から順に「より大きい」関係が成り立つかを比較します。

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

2つ以上の（実）数について、左から順に「以上」の関係が成り立つかを比較します。

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

実数の絶対値を求めます。

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

数の逆余弦（cos の逆関数）を計算します。

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

与えられた数に1を加えます。

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

複素数から偏角を取り出します。

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

数の逆正弦（sin の逆関数）を計算します。

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

与えられた数の逆正接を計算します。

```racket
> (atan 0)
0
> (atan 0.5)
#i0.4636476090008061
```

2引数版もあり、(atanyx) は (atan(/yx)) を計算しますが、y と x の符号によって結果の象限が決まり、境界付近では1引数版よりも精度が高くなりがちです。

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

実数より上で最も近い整数（正確数または非正確数）を求めます。round も参照してください。

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

ある値が複素数かどうかを判定します。

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

数の余弦を計算します（引数はラジアン）。

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

数の双曲線余弦を計算します。

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

現在時刻を、（プラットフォーム固有の起点からの）経過秒数として求めます。

```racket
> (current-seconds)
1779843347
```

```
+---------------------------+
| [手続き]               |
|                           |
| (denominator x) → integer |
| x: rational?             |
+---------------------------+
```

有理数の分母を計算します。

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

オイラー数。

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

ある整数（正確数または非正確数）が偶数かどうかを判定します。

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

正確数を非正確数に変換します。

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

ある数が正確数かどうかを判定します。

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

e をある数で累乗した値を求めます。

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

第1引数を第2引数で累乗します（べき乗）。

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

実数より下で最も近い整数（正確数または非正確数）を求めます。round も参照してください。

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

2つの整数（正確数または非正確数）の最大公約数を求めます。

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

複素数から虚部を取り出します。

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

非正確数を正確数で近似します。

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

ある数が非正確数かどうかを判定します。

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

与えられた正確な整数に対応する文字を、ASCII表から（あれば）調べます。

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

整数の整数平方根、または虚整数の平方根を計算します。

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

ある値が整数（正確数または非正確数）かどうかを判定します。

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

2つの整数（正確数または非正確数）の最小公倍数を求めます。

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

数の自然対数（底 e の対数）を求めます。

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

複素数の絶対値（大きさ）を求めます。

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

絶対値と偏角から複素数を作ります。

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

実部と虚部から複素数を作ります。

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

最大の数、すなわち最大値を求めます。

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

最小の数、すなわち最小値を求めます。

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

第1の数を第2の数で割った剰余を求めます。

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

ある実数が0より真に小さいかどうかを判定します。

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

数を文字列に変換します。

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

数 `x` を、指定された桁数の文字列に変換します。

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

有理数の分子を計算します。

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

ある整数（正確数または非正確数）が奇数かどうかを判定します。

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

円周の直径に対する比（円周率）。

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

ある実数が0より真に大きいかどうかを判定します。

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

第1の整数（被除数）を第2の整数（除数）で割り、商を求めます。

```racket
> (quotient 9 2)
4
> (quotient 3 4)
0
```

```
+----------------------+
| [手続き]          |
|                      |
| (random x) → natural |
| x: natural          |
+----------------------+
```

乱数を生成します。引数が1つのとき、`random` はその自然数未満の自然数を返します。ASLでは、引数なしのとき、0.0 と 1.0 のあいだ（両端を含まない）の非正確な乱数を生成します。

```racket
> (random)
#i0.3731303691424236
```

```racket
> (random)
#i0.7347732274403869
```

```racket
> (random 42)
6
```

```racket
> (random 42)
25
```

```
+--------------------------+
| [手続き]              |
|                          |
| (rational? x) → boolean? |
| x: any/c                |
+--------------------------+
```

ある値が有理数かどうかを判定します。

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

対話例が示すとおり、教育用言語は予想より多くの数を有理数とみなします。とくに `pi` は、数学上の π の有限近似にすぎないため有理数です。`rational?` は、これらの数を分数として考えてみるよう促す、と理解するとよいでしょう。

```
+----------------------+
| [手続き]          |
|                      |
| (real-part x) → real |
| x: number           |
+----------------------+
```

複素数から実部を取り出します。

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

ある値が実数かどうかを判定します。

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

第1の整数を第2の整数（正確数または非正確数）で割った剰余を求めます。

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

実数を整数に丸めます（ちょうど中間のときは偶数に丸めます）。floor と ceiling も参照してください。

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

実数の符号を求めます。

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

数の正弦を計算します（引数はラジアン）。

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

数の双曲線正弦を計算します。

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

数の2乗を計算します。

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

数の平方根を計算します。

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

与えられた数から1を引きます。

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

数の正接を計算します（引数はラジアン）。

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

ある数が0かどうかを判定します。

```racket
> (zero? 2)
#false
```

### 5.8 真偽値

```
+------------------------------+
| [手続き]                  |
|                              |
| (boolean->string x) → string |
| x: boolean?                 |
+------------------------------+
```

与えられた真偽値に対応する文字列を生成します。

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

2つの真偽値が等しいかどうかを判定します。

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

ある値が真偽値かどうかを判定します。

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

ある値が偽かどうかを判定します。

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

### 5.9 シンボル

```
+-----------------------------+
| [手続き]                 |
|                             |
| (symbol->string x) → string |
| x: symbol                  |
+-----------------------------+
```

シンボルを文字列に変換します。

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

2つのシンボルが等しいかどうかを判定します。

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

ある値がシンボルかどうかを判定します。

```racket
> (symbol? 'a)
#true
```

### 5.10 リスト

```
+-------------------------------+
| [手続き]                         |
|                               |
| (append l...) → (listof any) |
| l: (listof any)              |
+-------------------------------+
```

複数のリストを結合して1つのリストを作ります。
ASL では、list* は循環リストにも対応します。

```
+-------------------------------------------+
| [手続き]                                     |
|                                           |
| (assoc x l) → (union (listof any) #false) |
| x: any/c                                 |
| l: (listof any)                          |
+-------------------------------------------+
```

l 上で first が x と equal? である最初のペアを返します。
見つからなければ #false を返します。

```racket
> (assoc "hello" '(("world" 2) ("hello" 3) ("good" 0)))
(list "hello" 3)
```

```
+-----------------------------------+
| [手続き]                             |
|                                   |
| (assq x l) → (union #false cons?) |
| x: any/c                         |
| l: list?                         |
+-----------------------------------+
```

ペアのリストの中に、first が指定の項目と一致するペアがあるかどうかを調べます
（項目の比較には eq? を用います）。

```racket
> a
(list (list 'a 22) (list 'b 8) (list 'c 70))
> (assq 'b a)
(list 'b 8)
```

```
+----------------------+
| [手続き]                |
|                      |
| (caaar x) → any/c    |
| x: list?            |
+----------------------+
```

LISP 風の選択子: (car(car(carx)))。

```racket
> w
(list (list (list (list "bye") 3) #true) 42)
> (caaar w)
(list "bye")
```

```
+----------------------+
| [手続き]                |
|                      |
| (caadr x) → any/c    |
| x: list?            |
+----------------------+
```

LISP 風の選択子: (car(car(cdrx)))。

```racket
> (caadr (cons 1 (cons (cons 'a '()) (cons (cons 'd '()) '()))))
'a
```

```
+----------------------+
| [手続き]                |
|                      |
| (caar x) → any/c     |
| x: list?            |
+----------------------+
```

LISP 風の選択子: (car(carx))。

```racket
> y
(list (list (list 1 2 3) #false "world"))
> (caar y)
(list 1 2 3)
```

```
+----------------------+
| [手続き]                |
|                      |
| (cadar x) → any/c    |
| x: list?            |
+----------------------+
```

LISP 風の選択子: (car(cdr(carx)))。

```racket
> w
(list (list (list (list "bye") 3) #true) 42)
> (cadar w)
#true
```

```
+----------------------+
| [手続き]                |
|                      |
| (cadddr x) → any/c   |
| x: list?            |
+----------------------+
```

LISP 風の選択子: (car(cdr(cdr(cdrx))))。

```racket
> v
(list 1 2 3 4 5 6 7 8 9 'A)
> (cadddr v)
4
```

```
+----------------------+
| [手続き]                |
|                      |
| (caddr x) → any/c    |
| x: list?            |
+----------------------+
```

LISP 風の選択子: (car(cdr(cdrx)))。

```racket
> x
(list 2 "hello" #true)
> (caddr x)
#true
```

```
+----------------------+
| [手続き]                |
|                      |
| (cadr x) → any/c     |
| x: list?            |
+----------------------+
```

LISP 風の選択子: (car(cdrx))。

```racket
> x
(list 2 "hello" #true)
> (cadr x)
"hello"
```

```
+----------------------+
| [手続き]                |
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
| [手続き]                |
|                      |
| (cdaar x) → any/c    |
| x: list?            |
+----------------------+
```

LISP 風の選択子: (cdr(car(carx)))。

```racket
> w
(list (list (list (list "bye") 3) #true) 42)
> (cdaar w)
(list 3)
```

```
+----------------------+
| [手続き]                |
|                      |
| (cdadr x) → any/c    |
| x: list?            |
+----------------------+
```

LISP 風の選択子: (cdr(car(cdrx)))。

```racket
> (cdadr (list 1 (list 2 "a") 3))
(list "a")
```

```
+----------------------+
| [手続き]                |
|                      |
| (cdar x) → list?     |
| x: list?            |
+----------------------+
```

LISP 風の選択子: (cdr(carx))。

```racket
> y
(list (list (list 1 2 3) #false "world"))
> (cdar y)
(list #false "world")
```

```
+----------------------+
| [手続き]                |
|                      |
| (cddar x) → any/c    |
| x: list?            |
+----------------------+
```

LISP 風の選択子: (cdr(cdr(carx)))

```racket
> w
(list (list (list (list "bye") 3) #true) 42)
> (cddar w)
'()
```

```
+----------------------+
| [手続き]                |
|                      |
| (cdddr x) → any/c    |
| x: list?            |
+----------------------+
```

LISP 風の選択子: (cdr(cdr(cdrx)))。

```racket
> v
(list 1 2 3 4 5 6 7 8 9 'A)
> (cdddr v)
(list 4 5 6 7 8 9 'A)
```

```
+----------------------+
| [手続き]                |
|                      |
| (cddr x) → list?     |
| x: list?            |
+----------------------+
```

LISP 風の選択子: (cdr(cdrx))。

```racket
> x
(list 2 "hello" #true)
> (cddr x)
(list #true)
```

```
+----------------------+
| [手続き]                |
|                      |
| (cdr x) → any/c      |
| x: cons?            |
+----------------------+
```

空でないリストの残りを取り出します。

```racket
> x
(list 2 "hello" #true)
> (cdr x)
(list "hello" #true)
```

```
+-------------------------+
| [手続き]                   |
|                         |
| (cons x l) → (listof X) |
| x: X                   |
| l: (listof X)          |
+-------------------------+
```

リストを構築します。
ASL では、cons は変更可能なリストを作ります。

```
+----------------------+
| [手続き]                |
|                      |
| (cons? x) → boolean? |
| x: any/c            |
+----------------------+
```

値が cons によって構築されたリストかどうかを判定します。

```racket
> (cons? (cons 1 '()))
#true
> (cons? 42)
#false
```

```
+----------------------+
| [手続き]                |
|                      |
| (eighth x) → any/c   |
| x: list?            |
+----------------------+
```

空でないリストの8番目の要素を取り出します。

```racket
> v
(list 1 2 3 4 5 6 7 8 9 'A)
> (eighth v)
8
```

```
+-----------------------+
| [手続き]                 |
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
| [手続き]                |
|                      |
| (fifth x) → any/c    |
| x: list?            |
+----------------------+
```

空でないリストの5番目の要素を取り出します。

```racket
> v
(list 1 2 3 4 5 6 7 8 9 'A)
> (fifth v)
5
```

```
+----------------------+
| [手続き]                |
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
+----------------------------+
| [手続き]                      |
|                            |
| (for-each f l...) → void? |
| f: (any... -> any)       |
| l: (listof any)           |
+----------------------------+
```

1つ以上のリストの各要素に対して、副作用のみを目的として関数を適用します。

```racket
(for-each f (list x-1... x-n)) = (begin (f x-1)... (f x-n))
```

```racket
> (for-each (lambda (x) (begin (display x) (newline))) '(1 2 3))
123
```

```
+----------------------+
| [手続き]                |
|                      |
| (fourth x) → any/c   |
| x: list?            |
+----------------------+
```

空でないリストの4番目の要素を取り出します。

```racket
> v
(list 1 2 3 4 5 6 7 8 9 'A)
> (fourth v)
4
```

```
+-----------------------+
| [手続き]                 |
|                       |
| (length l) → natural? |
| l: list?             |
+-----------------------+
```

リスト上の要素数を求めます。

```racket
> x
(list 2 "hello" #true)
> (length x)
3
```

```
+----------------------+
| [手続き]                |
|                      |
| (list x...) → list? |
| x: any/c            |
+----------------------+
```

与えられた引数からなるリストを構築します。

```racket
> (list 1 2 3 4 5 6 7 8 9 0)
(cons 1 (cons 2 (cons 3 (cons 4 (cons 5 (cons 6 (cons 7 (cons 8 (cons 9 (cons 0 '()))))))))))
```

```
+--------------------------------+
| [手続き]                          |
|                                |
| (list* x... l) → (listof any) |
| x: any                        |
| l: (listof any)               |
+--------------------------------+
```

複数の項目をリストに付け加えてリストを構築します。
ASL では、list* は循環リストにも対応します。

```
+------------------------+
| [手続き]                  |
|                        |
| (list-ref x i) → any/c |
| x: list?              |
| i: natural?           |
+------------------------+
```

リストから、指定されたインデックスの要素を取り出します。

```racket
> v
(list 1 2 3 4 5 6 7 8 9 'A)
> (list-ref v 9)
'A
```

```
+----------------------+
| [手続き]                |
|                      |
| (list? x) → boolean? |
| x: any/c            |
+----------------------+
```

与えられた値がリストかどうかを調べます。

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
| [手続き]                   |
|                         |
| (make-list i x) → list? |
| i: natural?            |
| x: any/c               |
+-------------------------+
```

x を i 個並べたリストを構築します。

```racket
> (make-list 3 "hello")
(cons "hello" (cons "hello" (cons "hello" '())))
```

```
+-------------------------+
| [手続き]                   |
|                         |
| (member x l) → boolean? |
| x: any/c               |
| l: list?               |
+-------------------------+
```

値がリスト上にあるかどうかを判定します（値の比較には equal? を用います）。

```racket
> x
(list 2 "hello" #true)
> (member "hello" x)
#true
```

```
+--------------------------+
| [手続き]                    |
|                          |
| (member? x l) → boolean? |
| x: any/c                |
| l: list?                |
+--------------------------+
```

値がリスト上にあるかどうかを判定します（値の比較には equal? を用います）。

```racket
> x
(list 2 "hello" #true)
> (member? "hello" x)
#true
```

```
+-----------------------+
| [手続き]                 |
|                       |
| (memq x l) → boolean? |
| x: any/c             |
| l: list?             |
+-----------------------+
```

値 x がリスト l 上にあるかどうかを判定します。
x と l の各要素の比較には eq? を用います。

```racket
> x
(list 2 "hello" #true)
> (memq (list (list 1 2 3)) x)
#false
```

```
+------------------------+
| [手続き]                  |
|                        |
| (memq? x l) → boolean? |
| x: any/c              |
| l: list?              |
+------------------------+
```

値 x がリスト l 上にあるかどうかを判定します。
x と l の各要素の比較には eq? を用います。

```racket
> x
(list 2 "hello" #true)
> (memq? (list (list 1 2 3)) x)
#false
```

```
+---------------------------------+
| [手続き]                           |
|                                 |
| (memv x l) → (or/c #false list) |
| x: any/c                       |
| l: list?                       |
+---------------------------------+
```

値がリスト上にあるかどうかを判定します。ある場合はその x で始まるリストの
接尾部分を返し、ない場合は false を返します
（値の比較には eqv? 述語を用います）。

```racket
> x
(list 2 "hello" #true)
> (memv (list (list 1 2 3)) x)
#false
```

```
+----------------------+
| [値]                  |
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
| [手続き]                |
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
| [手続き]                          |
|                                |
| (range start end step) → list? |
| start: number                 |
| end: number                   |
| step: number                  |
+--------------------------------+
```

start から end まで step ずつ進んだ数のリストを構築します。

```racket
> (range 0 10 2)
(cons 0 (cons 2 (cons 4 (cons 6 (cons 8 '())))))
```

```
+----------------------+
| [手続き]                |
|                      |
| (remove x l) → list? |
| x: any/c            |
| l: list?            |
+----------------------+
```

与えられたリストと同じで、指定された項目の最初の出現だけを除いた
リストを構築します（値の比較には equal? を用います）。

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
| [手続き]                    |
|                          |
| (remove-all x l) → list? |
| x: any/c                |
| l: list?                |
+--------------------------+
```

与えられたリストと同じで、指定された項目のすべての出現を除いた
リストを構築します（値の比較には equal? を用います）。

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
| [手続き]                |
|                      |
| (rest x) → any/c     |
| x: cons?            |
+----------------------+
```

空でないリストの残りを取り出します。

```racket
> x
(list 2 "hello" #true)
> (rest x)
(list "hello" #true)
```

```
+----------------------+
| [手続き]                |
|                      |
| (reverse l) → list   |
| l: list?            |
+----------------------+
```

リストを逆順にしたものを作ります。

```racket
> x
(list 2 "hello" #true)
> (reverse x)
(list #true "hello" 2)
```

```
+----------------------+
| [手続き]                |
|                      |
| (second x) → any/c   |
| x: list?            |
+----------------------+
```

空でないリストの2番目の要素を取り出します。

```racket
> x
(list 2 "hello" #true)
> (second x)
"hello"
```

```
+----------------------+
| [手続き]                |
|                      |
| (seventh x) → any/c  |
| x: list?            |
+----------------------+
```

空でないリストの7番目の要素を取り出します。

```racket
> v
(list 1 2 3 4 5 6 7 8 9 'A)
> (seventh v)
7
```

```
+----------------------+
| [手続き]                |
|                      |
| (sixth x) → any/c    |
| x: list?            |
+----------------------+
```

空でないリストの6番目の要素を取り出します。

```racket
> v
(list 1 2 3 4 5 6 7 8 9 'A)
> (sixth v)
6
```

```
+----------------------+
| [手続き]                |
|                      |
| (third x) → any/c    |
| x: list?            |
+----------------------+
```

空でないリストの3番目の要素を取り出します。

```racket
> x
(list 2 "hello" #true)
> (third x)
#true
```

### 5.11 Posn（位置）

```
+------------------------+
| [手続き]                  |
|                        |
| (make-posn x y) → posn |
| x: any/c              |
| y: any/c              |
+------------------------+
```

任意の2つの値から posn（位置）を構築します。

```racket
> (make-posn 3 3)
(make-posn 3 3)
> (make-posn "hello" #true)
(make-posn "hello" #true)
```

```
+----------------------+
| [手続き]                |
|                      |
| (posn-x p) → any/c   |
| p: posn             |
+----------------------+
```

posn（位置）の x 成分を取り出します。

```racket
> p
(make-posn 2 -3)
> (posn-x p)
2
```

```
+----------------------+
| [手続き]                |
|                      |
| (posn-y p) → any/c   |
| p: posn             |
+----------------------+
```

posn（位置）の y 成分を取り出します。

```racket
> p
(make-posn 2 -3)
> (posn-y p)
-3
```

```
+----------------------+
| [手続き]                |
|                      |
| (posn? x) → boolean? |
| x: any/c            |
+----------------------+
```

入力が posn（位置）かどうかを判定します。

```racket
> q
(make-posn "bye" 2)
> (posn? q)
#true
> (posn? 42)
#false
```

```
+---------------------------+
| [手続き]                     |
|                           |
| (set-posn-x! p x) → void? |
| p: posn                  |
| x: any                   |
+---------------------------+
```

posn（位置）の x 成分を更新します。

```racket
> p
(make-posn 2 -3)
> (set-posn-x! p 678)
> p
(make-posn 678 -3)
```

```
+--------------------------+
| [手続き]                    |
|                          |
| (set-posn-y! p x) → void |
| p: posn                 |
| x: any                  |
+--------------------------+
```

posn（位置）の y 成分を更新します。

```racket
> q
(make-posn "bye" 2)
> (set-posn-y! q 678)
> q
(make-posn "bye" 678)
```

### 5.12 文字

```
+-----------------------------+
| [手続き]                       |
|                             |
| (char->integer c) → integer |
| c: char                    |
+-----------------------------+
```

与えられた文字に対応する数を ASCII 表から調べます（該当するものがある場合）。

```racket
> (char->integer #\a)
97
> (char->integer #\z)
122
```

```
+---------------------------------+
| [手続き]                           |
|                                 |
| (char-alphabetic? c) → boolean? |
| c: char                        |
+---------------------------------+
```

文字がアルファベット文字を表すかどうかを判定します。

```racket
> (char-alphabetic? #\Q)
#true
```

```
+-----------------------------------+
| [手続き]                             |
|                                   |
| (char-ci<=? c d e...) → boolean? |
| c: char                          |
| d: char                          |
| e: char                          |
+-----------------------------------+
```

文字が大文字小文字を区別せずに昇順（非減少）に並んでいるかどうかを判定します。

```racket
> (char-ci<=? #\b #\B)
#true
> (char<=? #\b #\B)
#false
```

```
+----------------------------------+
| [手続き]                            |
|                                  |
| (char-ci<? c d e...) → boolean? |
| c: char                         |
| d: char                         |
| e: char                         |
+----------------------------------+
```

文字が大文字小文字を区別せずに狭義の昇順に並んでいるかどうかを判定します。

```racket
> (char-ci<? #\B #\c)
#true
> (char<? #\b #\B)
#false
```

```
+----------------------------------+
| [手続き]                            |
|                                  |
| (char-ci=? c d e...) → boolean? |
| c: char                         |
| d: char                         |
| e: char                         |
+----------------------------------+
```

2つの文字が大文字小文字を区別せずに等しいかどうかを判定します。

```racket
> (char-ci=? #\b #\B)
#true
```

```
+-----------------------------------+
| [手続き]                             |
|                                   |
| (char-ci>=? c d e...) → boolean? |
| c: char                          |
| d: char                          |
| e: char                          |
+-----------------------------------+
```

文字が大文字小文字を区別せずに降順（非増加）に並んでいるかどうかを判定します。

```racket
> (char-ci>=? #\b #\C)
#false
> (char>=? #\b #\C)
#true
```

```
+----------------------------------+
| [手続き]                            |
|                                  |
| (char-ci>? c d e...) → boolean? |
| c: char                         |
| d: char                         |
| e: char                         |
+----------------------------------+
```

文字が大文字小文字を区別せずに狭義の降順に並んでいるかどうかを判定します。

```racket
> (char-ci>? #\b #\B)
#false
> (char>? #\b #\B)
#true
```

```
+--------------------------+
| [手続き]                    |
|                          |
| (char-downcase c) → char |
| c: char                 |
+--------------------------+
```

対応する小文字の文字を返します。

```racket
> (char-downcase #\T)
#\t
```

```
+---------------------------------+
| [手続き]                           |
|                                 |
| (char-lower-case? c) → boolean? |
| c: char                        |
+---------------------------------+
```

文字が小文字かどうかを判定します。

```racket
> (char-lower-case? #\T)
#false
```

```
+------------------------------+
| [手続き]                        |
|                              |
| (char-numeric? c) → boolean? |
| c: char                     |
+------------------------------+
```

文字が数字を表すかどうかを判定します。

```racket
> (char-numeric? #\9)
#true
```

```
+------------------------+
| [手続き]                  |
|                        |
| (char-upcase c) → char |
| c: char               |
+------------------------+
```

対応する大文字の文字を返します。

```racket
> (char-upcase #\t)
#\T
```

```
+---------------------------------+
| [手続き]                           |
|                                 |
| (char-upper-case? c) → boolean? |
| c: char                        |
+---------------------------------+
```

文字が大文字かどうかを判定します。

```racket
> (char-upper-case? #\T)
#true
```

```
+---------------------------------+
| [手続き]                           |
|                                 |
| (char-whitespace? c) → boolean? |
| c: char                        |
+---------------------------------+
```

文字が空白を表すかどうかを判定します。

```racket
> (char-whitespace? #\tab)
#true
```

```
+--------------------------------+
| [手続き]                          |
|                                |
| (char<=? c d e...) → boolean? |
| c: char                       |
| d: char                       |
| e: char                       |
+--------------------------------+
```

文字が昇順（非減少）に並んでいるかどうかを判定します。

```racket
> (char<=? #\a #\a #\b)
#true
```

```
+-------------------------------+
| [手続き]                         |
|                               |
| (char<? x d e...) → boolean? |
| x: char                      |
| d: char                      |
| e: char                      |
+-------------------------------+
```

文字が狭義の昇順に並んでいるかどうかを判定します。

```racket
> (char<? #\a #\b #\c)
#true
```

```
+-------------------------------+
| [手続き]                         |
|                               |
| (char=? c d e...) → boolean? |
| c: char                      |
| d: char                      |
| e: char                      |
+-------------------------------+
```

文字が等しいかどうかを判定します。

```racket
> (char=? #\b #\a)
#false
```

```
+--------------------------------+
| [手続き]                          |
|                                |
| (char>=? c d e...) → boolean? |
| c: char                       |
| d: char                       |
| e: char                       |
+--------------------------------+
```

文字が降順（非増加）に並んでいるかどうかを判定します。

```racket
> (char>=? #\b #\b #\a)
#true
```

```
+-------------------------------+
| [手続き]                         |
|                               |
| (char>? c d e...) → boolean? |
| c: char                      |
| d: char                      |
| e: char                      |
+-------------------------------+
```

文字が狭義の降順に並んでいるかどうかを判定します。

```racket
> (char>? #\A #\z #\a)
#false
```

```
+----------------------+
| [手続き]                |
|                      |
| (char? x) → boolean? |
| x: any/c            |
+----------------------+
```

値が文字かどうかを判定します。

```racket
> (char? "a")
#false
> (char? #\a)
#true
```

### 5.13 文字列

```
+-------------------------------+
| [手続き]                   |
|                               |
| (explode s) → (listof string) |
| s: string                    |
+-------------------------------+
```

文字列を、1文字ずつの文字列からなるリストに変換します。

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

文字列を整形します。値を埋め込むこともできます。

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

1文字ずつの文字列からなるリストを、1つの文字列に連結します。

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

[0,55295] または [57344 1114111] の範囲の整数を、1文字の文字列に変換します。

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

文字のリストを文字列に変換します。

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

文字 c を i 個並べた、長さ i の文字列を生成します。

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

文字列 s を i 回繰り返します。

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

与えられた文字から文字列を構築します。

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

1文字の文字列を、[0,55295] または [57344, 1114111] の範囲の整数に変換します。

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

文字列を文字のリストに変換します。

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

文字列を数に変換します。変換できない場合は false を返します。

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

文字列をシンボルに変換します。

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

文字列中の「文字」がすべてアルファベットであるかどうかを判定します。

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

第1の文字列が第2の文字列に、大文字小文字の区別なく現れるかどうかを判定します。

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

第1の文字列が第2の文字列に、そのままの形で現れるかどうかを判定します。

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

文字列をコピーします。

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

与えられた文字列の「文字」をすべて小文字にした文字列を生成します。

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

文字列 s から、i 番目の1文字の部分文字列を取り出します。

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

文字列の長さを求めます。

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

文字列中の「文字」がすべて小文字であるかどうかを判定します。

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

文字列中の「文字」がすべて数字であるかどうかを判定します。

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

文字列 s から、i 番目の文字を取り出します。

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

与えられた文字列の「文字」をすべて大文字にした文字列を生成します。

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

文字列中の「文字」がすべて大文字であるかどうかを判定します。

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

文字列中の「文字」がすべて空白であるかどうかを判定します。

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

値が文字列であるかどうかを判定します。

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

文字列の位置 i から j まで（j を省略した場合は末尾まで）の部分文字列を取り出します。

```racket
> (substring "hello world" 1 5)
"ello"
> (substring "hello world" 1 8)
"ello wo"
> (substring "hello world" 4)
"o world"
```

### 5.14 画像

```
+--------------------------+
| [手続き]              |
|                          |
| (image=? i j) → boolean? |
| i: image                |
| j: image                |
+--------------------------+
```

2つの画像が等しいかどうかを判定します。

```racket
> c1
[image:pict_13.png]
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

値が画像であるかどうかを判定します。

```racket
> c1
[image:pict_14.png]
> (image? c1)
#true
```

### 5.15 その他

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

x と y が互いに eps 以内にあるかどうかを検査します。

```racket
> (=~ 1.01 1.0 0.1)
#true
> (=~ 1.01 1.5 0.1)
#false
```

```
+----------------------------------------+
| [手続き]                            |
|                                        |
| (current-milliseconds) → exact-integer |
+----------------------------------------+
```

現在の「時刻」を fixnum のミリ秒（負の値もありうる）で返します。

```racket
> (current-milliseconds)
1779843342996
```

```
+----------------------+
| [値]              |
|                      |
| eof: eof-object?    |
+----------------------+
```

ファイルの終わりを表す値：

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

ある値がファイル終端の値であるかどうかを判定します。

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

2つの値がコンピュータの視点から同等であるかどうか（内包的）を判定します。

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

2つの値が構造的に等しいかどうかを判定します。基本値の比較には eqv? 述語を用います。

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

x と y を equal? と同様に比較しますが、数の場合は =~ を用います。

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

2つの値が、それに適用できるすべての関数の視点から同等であるかどうか（外延的）を判定します。

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

エラーを通知します。与えられた値を組み合わせてエラーメッセージにします。値の表示表現が長すぎる場合は切り詰め、「...」を文字列に入れます。最初の値がシンボルの場合はコロンを付けたうえで、その結果をエラーメッセージの先頭に付加します。

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

(exit) を評価すると、実行中のプログラムを終了します。

```
+----------------------+
| [手続き]          |
|                      |
| (force v) → any      |
| v: any              |
+----------------------+
```

遅延された値を取り出します。delay も参照してください。

```
+----------------------+
| [手続き]          |
|                      |
| (gensym) → symbol?   |
+----------------------+
```

プログラム中のどのシンボルとも異なる、新しいシンボルを生成します。

```racket
> (gensym)
'g8579052
```

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
[image:pict_15.png]
> (identity "hello")
"hello"
```

```
+-------------------------+
| [手続き]             |
|                         |
| (promise? x) → boolean? |
| x: any                 |
+-------------------------+
```

値が遅延されているかどうかを判定します。

```
+----------------------+
| [手続き]          |
|                      |
| (sleep sec) → void   |
| sec: positive-num   |
+----------------------+
```

指定した秒数だけプログラムをスリープさせます。

```
+------------------------+
| [手続き]            |
|                        |
| (struct? x) → boolean? |
| x: any/c              |
+------------------------+
```

ある値が構造体であるかどうかを判定します。

```racket
> (struct? (make-posn 1 2))
#true
> (struct? 43)
#false
```

```
+----------------------+
| [手続き]          |
|                      |
| (void) → void?       |
+----------------------+
```

void 値を生成します。

```racket
> (void)
```

```
+----------------------+
| [手続き]          |
|                      |
| (void? x) → boolean? |
| x: any              |
+----------------------+
```

値が void であるかどうかを判定します。

```racket
> (void? (void))
#true
> (void? 42)
#false
```

### 5.16 シグネチャ

```
+----------------------+
| [値]              |
|                      |
| Any: signature?     |
+----------------------+
```

任意の値に対するシグネチャです。

```
+----------------------+
| [値]              |
|                      |
| Boolean: signature? |
+----------------------+
```

真偽値に対するシグネチャです。

```
+----------------------+
| [値]              |
|                      |
| Char: signature?    |
+----------------------+
```

文字に対するシグネチャです。

```
+------------------------------------------+
| [手続き]                              |
|                                          |
| (ConsOf first-sig rest-sig) → signature? |
| first-sig: signature?                   |
| rest-sig: signature?                    |
+------------------------------------------+
```

cons 対に対するシグネチャです。

```
+------------------------+
| [値]                |
|                        |
| EmptyList: signature? |
+------------------------+
```

空リストに対するシグネチャです。

```
+----------------------+
| [値]              |
|                      |
| False: signature?   |
+----------------------+
```

false のみに対するシグネチャです。

```
+----------------------+
| [値]              |
|                      |
| Integer: signature? |
+----------------------+
```

整数に対するシグネチャです。

```
+----------------------+
| [値]              |
|                      |
| Natural: signature? |
+----------------------+
```

自然数に対するシグネチャです。

```
+----------------------+
| [値]              |
|                      |
| Number: signature?  |
+----------------------+
```

任意の数に対するシグネチャです。

```
+-----------------------+
| [値]               |
|                       |
| Rational: signature? |
+-----------------------+
```

有理数に対するシグネチャです。

```
+----------------------+
| [値]              |
|                      |
| Real: signature?    |
+----------------------+
```

実数に対するシグネチャです。

```
+----------------------+
| [値]              |
|                      |
| String: signature?  |
+----------------------+
```

文字列に対するシグネチャです。

```
+----------------------+
| [値]              |
|                      |
| Symbol: signature?  |
+----------------------+
```

シンボルに対するシグネチャです。

```
+----------------------+
| [値]              |
|                      |
| True: signature?    |
+----------------------+
```

true のみに対するシグネチャです。

### 5.17 数（緩和条件）

### 5.18 文字列（緩和条件）

```
+--------------------------------+
| [手続き]                    |
|                                |
| (string-append s...) → string |
| s: string                     |
+--------------------------------+
```

複数の文字列の文字を連結します。

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

文字列が大文字小文字を区別せずに字句順の昇順（非減少）に並んでいるかどうかを判定します。

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

文字列が大文字小文字を区別せずに字句順の狭義の昇順に並んでいるかどうかを判定します。

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

すべての文字列が、大文字小文字を区別せず文字単位で等しいかどうかを判定します。

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

文字列が大文字小文字を区別せずに字句順の降順（非増加）に並んでいるかどうかを判定します。

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

文字列が大文字小文字を区別せずに字句順の狭義の降順に並んでいるかどうかを判定します。

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

文字列が字句順の昇順（非減少）に並んでいるかどうかを判定します。

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

文字列が字句順の狭義の昇順に並んでいるかどうかを判定します。

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

すべての文字列が文字単位で等しいかどうかを判定します。

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

文字列が字句順の降順（非増加）に並んでいるかどうかを判定します。

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

文字列が字句順の狭義の降順に並んでいるかどうかを判定します。

```racket
> (string>?  "zoo" "world" "hello")
#true
```

### 5.19 Posn（位置）

```
+----------------------+
| [手続き]          |
|                      |
| (posn) → signature   |
+----------------------+
```

posn に対するシグネチャです。

### 5.20 高階関数

### 5.21 数（緩和条件・追加）

```
+----------------------+
| [手続き]          |
|                      |
| (* x...) → number   |
| x: number           |
+----------------------+
```

与えられたすべての数を掛け合わせます。
ISL 以上では、引数が1つだけの場合や引数がない場合でも * は動作します。

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

与えられたすべての数を足し合わせます。
ISL 以上では、引数が1つだけの場合や引数がない場合でも + は動作します。

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

最初の数を残りのすべての数で割ります。
ISL 以上では、引数が1つのとき / は逆数を計算します。

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

数の相等を比較します。
ISL 以上では、引数が1つだけの場合でも = は動作します。

```racket
> (= 10 10)
#true
> (= 11)
#true
> (= 0)
#true
```

### 5.22 高階関数（ラムダつき）

```
+---------------------------+
| [手続き]               |
|                           |
| (andmap p? [l]) → boolean |
| p?: (X... -> boolean)   |
| l: (listof X) =...      |
+---------------------------+
```

l のすべての要素について p? が成り立つかどうかを判定する:

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

リストの要素を引数として関数を適用する:

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

関数の出力を最大にするリストの（最初の）要素を求める。

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

関数の出力を最小にするリストの（最初の）要素を求める。

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

0 から (-n1) までの数に f を適用してリストを構築する:

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

0 から
(-n1) までの数に f を適用して文字列を構築する:

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

一連の手続きを合成して、単一の手続きにする:

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

リスト上の要素のうち、述語が成り立つものすべてからリストを構築する。

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
| (map f l...) → (listof Z) |
| f: (X... -> Z)           |
| l: (listof X)             |
+----------------------------+
```

1 つ以上の既存のリストの各要素に関数を適用して、新しいリストを構築する:

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
tag-with-a:this name was defined previously and cannot be re-defined
```

```racket
> (map tag-with-a (list 3 -4.01 2/5))
(list (list "a" 4) (list "a" #i-3.01) (list "a" 1.4))
```

```racket
> (define (add-and-multiply x y)    (+ x (* x y)))
add-and-multiply:this name was defined previously and cannot be re-defined
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

l 上のすべての要素について p? が偽を生成する場合は #false を生成する。
l 上のいずれかの要素について p? が #true を生成する場合、
memf はその要素から始まる部分リストを返す。

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

l の少なくとも 1 つの要素について p? が成り立つかどうかを判定する:

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

値が手続きであれば真を生成する。

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

comp に従った順序で l 上の要素を整列する（クイックソート
アルゴリズムを用いる）。

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

comp に従った順序で l 上の要素を整列する。

```racket
> (sort '(6 7 2 1 3 4 0 5 9 8) <)
(list 0 1 2 3 4 5 6 7 8 9)
```

### 5.23 読み取りと表示

```
+----------------------+
| [手続き]          |
|                      |
| (display x) → void   |
| x: any              |
+----------------------+
```

引数を標準出力へ表示する（シンボルや文字列などに引用符は付けない、など）。

```racket
> (display 10)
10
> (display "hello")
hello
> (display 'hello)
hello
```

```
+----------------------+
| [手続き]          |
|                      |
| (newline) → void     |
+----------------------+
```

改行を表示する。

```
+-------------------------+
| [手続き]             |
|                         |
| (pretty-print x) → void |
| x: any                 |
+-------------------------+
```

S 式を整形表示する（write と同様）。

```racket
> (pretty-print '((1 2 3) ((a) ("hello world" #true) (((false "good bye"))))))
((1 2 3) ((a) ("hello world" #true) (((false "good bye")))))
> (pretty-print (build-list 10 (lambda (i) (build-list 10 (lambda (j) (= i j))))))
((#true #false #false #false #false #false #false #false #false #false) (#false #true #false #false #false #false #false #false #false #false) (#false #false #true #false #false #false #false #false #false #false) (#false #false #false #true #false #false #false #false #false #false) (#false #false #false #false #true #false #false #false #false #false) (#false #false #false #false #false #true #false #false #false #false) (#false #false #false #false #false #false #true #false #false #false) (#false #false #false #false #false #false #false #true #false #false) (#false #false #false #false #false #false #false #false #true #false) (#false #false #false #false #false #false #false #false #false #true))
```

```
+----------------------+
| [手続き]          |
|                      |
| (print x) → void     |
| x: any              |
+----------------------+
```

引数を値として表示する。

```racket
> (print 10)
10
> (print "hello")
"hello"
> (print 'hello)
'hello
```

```
+-------------------------+
| [手続き]             |
|                         |
| (printf f x...) → void |
| f: string              |
| x: any                 |
+-------------------------+
```

第 1 引数に従って残りの引数を整形し、それを表示する。

```
+----------------------+
| [手続き]          |
|                      |
| (read) → sexp        |
+----------------------+
```

ユーザからの入力を読み取る。

```
+----------------------------------+
| [手続き]                      |
|                                  |
| (with-input-from-file f p) → any |
| f: string                       |
| p: (-> any)                     |
+----------------------------------+
```

名前付き入力ファイル f を開き、p がそのファイルから読み取れるようにする。

```
+------------------------------------+
| [手続き]                        |
|                                    |
| (with-input-from-string s p) → any |
| s: string                         |
| p: (-> any)                       |
+------------------------------------+
```

s を p 内の read 操作の入力に変える。

```racket
> (with-input-from-string "hello" read)
'hello
> (string-length (symbol->string (with-input-from-string "hello" read)))
5
```

```
+---------------------------------+
| [手続き]                     |
|                                 |
| (with-output-to-file f p) → any |
| f: string                      |
| p: (-> any)                    |
+---------------------------------+
```

名前付き出力ファイル f を開き、p がそのファイルへ書き込めるようにする。

```
+---------------------------------+
| [手続き]                     |
|                                 |
| (with-output-to-string p) → any |
| p: (-> any)                    |
+---------------------------------+
```

p 内のすべての write／display／print 操作から文字列を生成する。

```racket
> (with-output-to-string (lambda () (display 10)))
"10"
```

```
+----------------------+
| [手続き]          |
|                      |
| (write x) → void     |
| x: any              |
+----------------------+
```

引数を標準出力へ表示する（print と display の中間あたりの、
伝統的なスタイルで）。

```racket
> (write 10)
10
> (write "hello")
"hello"
> (write 'hello)
hello
```

### 5.24 ベクタ

```
+-----------------------------------+
| [手続き]                       |
|                                   |
| (build-vector n f) → (vectorof X) |
| n: nat                           |
| f: (nat -> X)                    |
+-----------------------------------+
```

0 から
(-n1) までの数に f を適用してベクタを構築する。

```racket
> (build-vector 5 add1)
(vector 1 2 3 4 5)
```

```
+---------------------------------+
| [手続き]                     |
|                                 |
| (list->vector l) → (vectorof X) |
| l: (listof X)                  |
+---------------------------------+
```

l をベクタに変換する。

```racket
> (list->vector (list "hello" "world" "good" "bye"))
(vector "hello" "world" "good" "bye")
```

```
+----------------------------------+
| [手続き]                      |
|                                  |
| (make-vector n x) → (vectorof X) |
| n: number                       |
| x: X                            |
+----------------------------------+
```

x のコピー n 個からなるベクタを構築する。

```racket
> (make-vector 5 0)
(vector 0 0 0 0 0)
```

```
+---------------------------------+
| [手続き]                     |
|                                 |
| (vector x...) → (vector X...) |
| x: X                           |
+---------------------------------+
```

与えられた値からベクタを構築する。

```racket
> (vector 1 2 3 -1 -2 -3)
(vector 1 2 3 -1 -2 -3)
```

```
+-------------------------------+
| [手続き]                   |
|                               |
| (vector->list v) → (listof X) |
| v: (vectorof X)              |
+-------------------------------+
```

v をリストに変換する。

```racket
> (vector->list (vector 'a 'b 'c))
(list 'a 'b 'c)
```

```
+-------------------------+
| [手続き]             |
|                         |
| (vector-length v) → nat |
| v: (vector X)          |
+-------------------------+
```

v の長さを求める。

```racket
> v
(vector "a" "b" "c" "d" "e")
> (vector-length v)
5
```

```
+----------------------+
| [手続き]          |
|                      |
| (vector-ref v n) → X |
| v: (vector X)       |
| n: nat              |
+----------------------+
```

v から n 番目の要素を取り出す。

```racket
> v
(vector "a" "b" "c" "d" "e")
> (vector-ref v 3)
"d"
```

```
+----------------------------+
| [手続き]                |
|                            |
| (vector-set! v n x) → void |
| v: (vectorof X)           |
| n: nat                    |
| x: X                      |
+----------------------------+
```

位置 n の v を x に更新する。

```racket
> v
(vector "a" "b" "c" "d" "e")
> (vector-set! v 3 77)
> v
(vector "a" "b" "c" 77 "e")
```

```
+-----------------------+
| [手続き]           |
|                       |
| (vector? x) → boolean |
| x: any               |
+-----------------------+
```

値がベクタかどうかを判定する。

```racket
> v
(vector "a" "b" "c" 77 "e")
> (vector? v)
#true
> (vector? 42)
#false
```

### 5.25 ボックス

```
+----------------------+
| [手続き]          |
|                      |
| (box x) → box?       |
| x: any/c            |
+----------------------+
```

ボックスを構築する。

```racket
> (box 42)
(box 42)
```

```
+----------------------+
| [手続き]          |
|                      |
| (box? x) → boolean?  |
| x: any/c            |
+----------------------+
```

値がボックスかどうかを判定する。

```racket
> b
(box 33)
> (box? b)
#true
> (box? 42)
#false
```

```
+-----------------------+
| [手続き]           |
|                       |
| (set-box! b x) → void |
| b: box?              |
| x: any/c             |
+-----------------------+
```

ボックスを更新する。

```racket
> b
(box 33)
> (set-box! b 31)
> b
(box 31)
```

```
+----------------------+
| [手続き]          |
|                      |
| (unbox b) → any      |
| b: box?             |
+----------------------+
```

ボックスに入っている値を取り出す。

```racket
> b
(box 31)
> (unbox b)
31
```

### 5.26 ハッシュ表

```
+----------------------+
| [手続き]          |
|                      |
| (hash-copy h) → hash |
| h: hash             |
+----------------------+
```

ハッシュ表をコピーする。

```
+--------------------------+
| [手続き]              |
|                          |
| (hash-count h) → integer |
| h: hash                 |
+--------------------------+
```

ハッシュ表が対応付けているキーの個数を求める。

```racket
> ish
(make-immutable-hash (list (list 'b 69) (list 'r 999) (list 'c 42) (list 'e 61)))
> (hash-count ish)
4
```

```
+------------------------+
| [手続き]            |
|                        |
| (hash-eq? h) → boolean |
| h: hash               |
+------------------------+
```

ハッシュ表が比較に eq? を用いるかどうかを判定する。

```racket
> hsh
(make-hash (list (list 'c 42) (list 'r 999) (list 'b 69) (list 'e 61)))
> (hash-eq? hsh)
#false
> heq
(make-hasheq (list (list 'b 69) (list 'r 999) (list 'c 42) (list 'e 61)))
> (hash-eq? heq)
#true
```

```
+---------------------------+
| [手続き]               |
|                           |
| (hash-equal? h) → boolean |
| h: hash?                 |
+---------------------------+
```

ハッシュ表が比較に equal? を用いるかどうかを判定する。

```racket
> ish
(make-immutable-hash (list (list 'b 69) (list 'r 999) (list 'c 42) (list 'e 61)))
> (hash-equal? ish)
#true
> ieq
(make-immutable-hasheq (list (list 'b 69) (list 'r 999) (list 'c 42) (list 'e 61)))
> (hash-equal? ieq)
#false
```

```
+-------------------------+
| [手続き]             |
|                         |
| (hash-eqv? h) → boolean |
| h: hash                |
+-------------------------+
```

ハッシュ表が比較に eqv? を用いるかどうかを判定する。

```racket
> heq
(make-hasheq (list (list 'b 69) (list 'r 999) (list 'c 42) (list 'e 61)))
> (hash-eqv? heq)
#false
> heqv
(make-hasheqv (list (list 'b 69) (list 'r 999) (list 'c 42) (list 'e 61)))
> (hash-eqv? heqv)
#true
```

```
+-----------------------------+
| [手続き]                 |
|                             |
| (hash-for-each h f) → void? |
| h: (hash X Y)              |
| f: (X Y -> any)            |
+-----------------------------+
```

副作用のためだけに、ハッシュ表の各対応付けに関数を適用する。

```racket
> hsh
(make-hash (list (list 'c 42) (list 'r 999) (list 'b 69) (list 'e 61)))
> (hash-for-each hsh (lambda (ky vl) (hash-set! hsh ky (+ vl 1))))
> hsh
(make-hash (list (list 'c 43) (list 'r 1000) (list 'b 70) (list 'e 62)))
```

```
+-------------------------------+
| [手続き]                   |
|                               |
| (hash-has-key? h x) → boolean |
| h: (hash X Y)                |
| x: X                         |
+-------------------------------+
```

キーがハッシュ表で値と対応付けられているかどうかを判定する。

```racket
> ish
(make-immutable-hash (list (list 'b 69) (list 'r 999) (list 'c 42) (list 'e 61)))
> (hash-has-key? ish 'b)
#true
> hsh
(make-hash (list (list 'c 43) (list 'r 1000) (list 'b 70) (list 'e 62)))
> (hash-has-key? hsh 'd)
#false
```

```
+-----------------------------+
| [手続き]                 |
|                             |
| (hash-map h f) → (listof Z) |
| h: (hash X Y)              |
| f: (X Y -> Z)              |
+-----------------------------+
```

ハッシュ表の各対応付けに関数を適用して、新しいリストを構築する。

```racket
> ish
(make-immutable-hash (list (list 'b 69) (list 'r 999) (list 'c 42) (list 'e 61)))
> (hash-map ish list)
(list (list 'b 69) (list 'r 999) (list 'c 42) (list 'e 61))
```

```
+----------------------+
| [手続き]          |
|                      |
| (hash-ref h k) → Y   |
| h: (hash X Y)       |
| k: X                |
+----------------------+
```

ハッシュ表からキーに対応する値を取り出す。3 引数の場合は、
既定値または既定値の計算を指定できる。

```racket
> hsh
(make-hash (list (list 'c 43) (list 'r 1000) (list 'b 70) (list 'e 62)))
> (hash-ref hsh 'b)
70
```

```
+-----------------------+
| [手続き]           |
|                       |
| (hash-ref! h k v) → Y |
| h: (hash X Y)        |
| k: X                 |
| v: Y                 |
+-----------------------+
```

可変ハッシュ表からキーに対応する値を取り出す。キーに
対応付けがない場合、第 3 引数を値として用いる（またはその値を計算するために用い）、
そのキーに対応付けてハッシュ表へ追加する。

```racket
> hsh
(make-hash (list (list 'c 43) (list 'r 1000) (list 'b 70) (list 'e 62)))
> (hash-ref! hsh 'd 99)
99
> hsh
(make-hash (list (list 'c 43) (list 'd 99) (list 'r 1000) (list 'b 70) (list 'e 62)))
```

```
+--------------------------------+
| [手続き]                    |
|                                |
| (hash-remove h k) → (hash X Y) |
| h: (hash X Y)                 |
| k: X                          |
+--------------------------------+
```

既存の不変ハッシュ表より対応付けが 1 つ少ない、
不変ハッシュ表を構築する。

```racket
> ish
(make-immutable-hash (list (list 'b 69) (list 'r 999) (list 'c 42) (list 'e 61)))
> (hash-remove ish 'b)
(make-immutable-hash (list (list 'c 42) (list 'r 999) (list 'e 61)))
```

```
+---------------------------+
| [手続き]               |
|                           |
| (hash-remove! h x) → void |
| h: (hash X Y)            |
| x: X                     |
+---------------------------+
```

可変ハッシュ表から対応付けを取り除く。

```racket
> hsh
(make-hash (list (list 'c 43) (list 'd 99) (list 'r 1000) (list 'b 70) (list 'e 62)))
> (hash-remove! hsh 'r)
> hsh
(make-hash (list (list 'c 43) (list 'd 99) (list 'b 70) (list 'e 62)))
```

```
+-------------------------------+
| [手続き]                   |
|                               |
| (hash-set h k v) → (hash X Y) |
| h: (hash X Y)                |
| k: X                         |
| v: Y                         |
+-------------------------------+
```

既存の不変ハッシュ表から、新しい対応付けを 1 つ加えた
不変ハッシュ表を構築する。

```racket
> (hash-set ish 'a 23)
(make-immutable-hash (list (list 'b 69) (list 'r 999) (list 'c 42) (list 'a 23) (list 'e 61)))
```

```
+---------------------------+
| [手続き]               |
|                           |
| (hash-set! h k v) → void? |
| h: (hash X Y)            |
| k: X                     |
| v: Y                     |
+---------------------------+
```

可変ハッシュ表を新しい対応付けで更新する。

```racket
> hsh
(make-hash (list (list 'c 43) (list 'd 99) (list 'b 70) (list 'e 62)))
> (hash-set! hsh 'a 23)
> hsh
(make-hash (list (list 'c 43) (list 'a 23) (list 'd 99) (list 'b 70) (list 'e 62)))
```

```
+----------------------------------+
| [手続き]                      |
|                                  |
| (hash-update h k f) → (hash X Y) |
| h: (hash X Y)                   |
| k: X                            |
| f: (Y -> Y)                     |
+----------------------------------+
```

hash-ref と hash-set を組み合わせて既存の対応付けを更新する。第 3
引数は新しい対応付けの値を計算するのに用い、第 4
引数は hash-ref の第 3 引数として用いる。

```racket
> (hash-update ish 'b (lambda (old-b) (+ old-b 1)))
(make-immutable-hash (list (list 'b 70) (list 'r 999) (list 'c 42) (list 'e 61)))
```

```
+------------------------------+
| [手続き]                  |
|                              |
| (hash-update! h k f) → void? |
| h: (hash X Y)               |
| k: X                        |
| f: (Y -> Y)                 |
+------------------------------+
```

hash-ref と hash-set! を組み合わせて既存の対応付けを更新する。
第 3 引数は新しい対応付けの値を計算するのに用い、第 4
引数は hash-ref の第 3 引数として用いる。

```racket
> hsh
(make-hash (list (list 'c 43) (list 'a 23) (list 'd 99) (list 'b 70) (list 'e 62)))
> (hash-update! hsh 'b (lambda (old-b) (+ old-b 1)))
> hsh
(make-hash (list (list 'c 43) (list 'a 23) (list 'd 99) (list 'b 71) (list 'e 62)))
```

```
+----------------------+
| [手続き]          |
|                      |
| (hash? x) → boolean  |
| x: any              |
+----------------------+
```

値がハッシュ表かどうかを判定する。

```racket
> ish
(make-immutable-hash (list (list 'b 69) (list 'r 999) (list 'c 42) (list 'e 61)))
> (hash? ish)
#true
> (hash? 42)
#false
```

```
+--------------------------+
| [手続き]              |
|                          |
| (make-hash) → (hash X Y) |
+--------------------------+
```

比較に equal? を用いる、任意個の対応付けのリストから
可変ハッシュ表を構築する。

```racket
> (make-hash)
(make-hash)
> (make-hash '((b 69) (e 61) (i 999)))
(make-hash (list (list 'i 999) (list 'b 69) (list 'e 61)))
```

```
+----------------------------+
| [手続き]                |
|                            |
| (make-hasheq) → (hash X Y) |
+----------------------------+
```

比較に eq? を用いる、任意個の対応付けのリストから
可変ハッシュ表を構築する。

```racket
> (make-hasheq)
(make-hasheq)
> (make-hasheq '((b 69) (e 61) (i 999)))
(make-hasheq (list (list 'i 999) (list 'b 69) (list 'e 61)))
```

```
+-----------------------------+
| [手続き]                 |
|                             |
| (make-hasheqv) → (hash X Y) |
+-----------------------------+
```

比較に eqv? を用いる、任意個の対応付けのリストから
可変ハッシュ表を構築する。

```racket
> (make-hasheqv)
(make-hasheqv)
> (make-hasheqv '((b 69) (e 61) (i 999)))
(make-hasheqv (list (list 'i 999) (list 'b 69) (list 'e 61)))
```

```
+------------------------------------+
| [手続き]                        |
|                                    |
| (make-immutable-hash) → (hash X Y) |
+------------------------------------+
```

比較に equal? を用いる、任意個の対応付けのリストから
不変ハッシュ表を構築する。

```racket
> (make-immutable-hash)
(make-immutable-hash)
> (make-immutable-hash '((b 69) (e 61) (i 999)))
(make-immutable-hash (list (list 'b 69) (list 'e 61) (list 'i 999)))
```

```
+--------------------------------------+
| [手続き]                          |
|                                      |
| (make-immutable-hasheq) → (hash X Y) |
+--------------------------------------+
```

比較に eq? を用いる、任意個の対応付けのリストから
不変ハッシュ表を構築する。

```racket
> (make-immutable-hasheq)
(make-immutable-hasheq)
> (make-immutable-hasheq '((b 69) (e 61) (i 999)))
(make-immutable-hasheq (list (list 'b 69) (list 'e 61) (list 'i 999)))
```

```
+---------------------------------------+
| [手続き]                           |
|                                       |
| (make-immutable-hasheqv) → (hash X Y) |
+---------------------------------------+
```

比較に eqv? を用いる、任意個の対応付けのリストから
不変ハッシュ表を構築する。

```racket
> (make-immutable-hasheqv)
(make-immutable-hasheqv)
> (make-immutable-hasheqv '((b 69) (e 61) (i 999)))
(make-immutable-hasheqv (list (list 'b 69) (list 'e 61) (list 'i 999)))
```
