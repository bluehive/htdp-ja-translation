# 付録 B-5: Advanced Student（#lang htdp/asl）

**原本:** `extracted/appendix/htdp-langs/original_markdown_05_advanced.md`

初学者向けに、説明文を日本語へ翻訳しています。コード・シグネチャ・実行例は原文のまま保持します。

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

", ' ` ( ) [ ] { } |; #

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

### 5.2 テンプレート変数

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

### 5.3 上級の構文

In Advanced, set! できる be used へ mutate 変数s, と define-struct’s 構造体s は mutatable. define と lambda できる define 関数s の zero 引数s, と 関数呼び出しs できる invoke 関数s の zero 引数s.

```
+------------------------------------+
| [構文]                           |
|                                    |
| (lambda (variable...) expression) |
+------------------------------------+
```

a function that takes as many arguments as given variables, and whose body is expression を作成します。

```
+-------------------------------+
| [構文]                      |
|                               |
| (λ (variable...) expression) |
+-------------------------------+
```

Greek letter λ は synonym のための lambda.

```
+-----------------------------+
| [構文]                    |
|                             |
| (expression expression...) |
+-----------------------------+
```

Calls the function that results from evaluating the first expression. The value of the call is the value of function’s body when every instance of name’s variables are replaced by the values of the corresponding expressions.

The function being called must come from either a definition appearing before the function call, or from a lambda expression. The number of argument expressions must be the same as the number of arguments expected by the function.

```
+------------------------------------------------------------------+
| [構文]                                                         |
|                                                                  |
| (define-datatype dataype-name [variant-name field-name...]...) |
+------------------------------------------------------------------+
```

A short-hand のための defining group の related 構造体s. following define-datatype:

```racket
(define-datatype datatype-name
  [variant-name field-name #,...]
...)
```

is equivalent to:

```racket
(define (datatype-name? x)
  (or (variant-name? x)...))
(define-struct variant-name (field-name...))
...
```

```
+-----------------------------------+
| [構文]                          |
|                                   |
| (begin expression expression...) |
+-----------------------------------+
```

the expressions in order from left to right. The value of the begin expression is the value of the last expression を評価します。

```
+------------------------------------+
| [構文]                           |
|                                    |
| (begin0 expression expression...) |
+------------------------------------+
```

the expressions in order from left to right. The value of the begin expression is the value of the first expression を評価します。

```
+----------------------------+
| [構文]                   |
|                            |
| (set! variable expression) |
+----------------------------+
```

expression, and then changes the value of the variable to have expression’s value. The variable must be defined by define, letrec, let*, let, or local を評価します。

```
+----------------------+
| [構文]             |
|                      |
| (delay expression)   |
+----------------------+
```

a “promise” to evaluate expression. The expression is not evaluated until the promise is forced with force; when the promise is forced, the result is recorded, so that any further force of the promise immediately produces the remembered value を生成します。

```
+---------------------------------------------+
| [構文]                                    |
|                                             |
| (shared ([name expression]...) expression) |
+---------------------------------------------+
```

letrec と同様ですが、when an expression next to an id is a cons, list, vector, quasiquoted expression, or make-struct-name from a define-struct, the expression can refer directly to any name, not just names defined earlier. Thus, shared can be used to create cyclic data structures。

```
+-------------------------------------------------+
| [構文]                                        |
|                                                 |
| (recur name ([name expression]...) expression) |
+-------------------------------------------------+
```

A short-hand syntax for recursive loops. The first name corresponds to the name of the recursive function. The names in the parenthesis are the function’s arguments, and each corresponding expression is a value supplied for that argument in an initial starting call of the function. The last expression is the body of the function.

More precisely, following recur:

```racket
(recur func-name ([arg-name arg-expression]...)
  body-expression)
```

is equivalent to:

```racket
(local [(define (func-name arg-name...) body-expression)]
  (func-name arg-expression...))
```

```
+-----------------------------------------------+
| [構文]                                      |
|                                               |
| (let name ([name expression]...) expression) |
+-----------------------------------------------+
```

An alternate syntax のための recur.

```
+---------------------------------------------------------------------------+
| [構文]                                                                  |
|                                                                           |
| (case expression [(choice...) expression]... [(choice...) expression]) |
+---------------------------------------------------------------------------+
```

A case form contains one or more clauses. Each clause contains a choices (in parentheses)—either numbers or names—and an answer expression. The initial expression is evaluated, and its value is compared to the choices in each clause, where the lines are considered in order. The first line that contains a matching choice provides an answer expression whose value is the result of the whole case expression. Numbers match with the numbers in the choices, and symbols match with the names. If none of the lines contains a matching choice, it is an error.

```
+-------------------------------------------------------------------+
| [構文]                                                          |
|                                                                   |
| (case expression [(choice...) expression]... [else expression]) |
+-------------------------------------------------------------------+
```

これ form の case は similar へ prior one, except という final else 節 は taken もし no 節 contains choice matching 値 の initial 式.

```
+---------------------------------------------+
| [構文]                                    |
|                                             |
| (match expression [pattern expression]...) |
+---------------------------------------------+
```

A match form contains one or more clauses that are surrounded by square brackets. Each clause contains a pattern—a description of a value—and an answer expression. The initial expression is evaluated, and its value is matched against the pattern in each clause, where the clauses are considered in order. The first clause that contains a matching pattern provides an answer expression whose value is the result of the whole match expression. This expression may reference identifiers defined in the matching pattern. If none of the clauses contains a matching pattern, it is an error.

```
+--------------------------------------------+
| [構文]                                   |
|                                            |
| (when question-expression body-expression) |
+--------------------------------------------+
```

If question-expression evaluates to true, the result of the when expression is the result of evaluating the body-expression, otherwise the result is (void) and the body-expression is not evaluated. If the result of evaluating the question-expression is neither true nor false, it is an error.

```
+----------------------------------------------+
| [構文]                                     |
|                                              |
| (unless question-expression body-expression) |
+----------------------------------------------+
```

when と同様ですが、the body-expression is evaluated when the question-expression produces false instead of true。

### 5.4 共通の構文

following syntaxes behave same の中の *Advanced* level として they did の中の Intermediate Student とともに Lambda level.

```
+-------------------------------------+
| [構文]                            |
|                                     |
| (local [definition...] expression) |
+-------------------------------------+
```

Groups related 定義s のための use の中の 式. Each 定義 できる be either define または define-struct.

When evaluating local, each definition is evaluated in order, and finally the body expression is evaluated. Only the expressions within the local (including the right-hand-sides of the definitions and the expression) may refer to the names defined by the definitions. If a name defined in the local is the same as a top-level binding, the inner one “shadows” the outer one. That is, inside the local, any references to that name refer to the inner one.

```
+-----------------------------------------------+
| [構文]                                      |
|                                               |
| (letrec ([name expr-for-let]...) expression) |
+-----------------------------------------------+
```

local と同様ですが、with a simpler syntax. Each name defines a variable (or a function) with the value of the corresponding expr-for-let. If expr-for-let is a lambda, letrec defines a function, otherwise it defines a variable。

```
+---------------------------------------------+
| [構文]                                    |
|                                             |
| (let* ([name expr-for-let]...) expression) |
+---------------------------------------------+
```

letrec と同様ですが、each name can only be used in expression, and in expr-for-lets occuring after that name。

```
+--------------------------------------------+
| [構文]                                   |
|                                            |
| (let ([name expr-for-let]...) expression) |
+--------------------------------------------+
```

letrec と同様ですが、the defined names can be used only in the last expression, not the expr-for-lets next to the names。

```
+----------------------+
| [構文]             |
|                      |
| (time expression)    |
+----------------------+
```

Measures the time taken to evaluate expression. After evaluating expression, time prints out the time taken by the evaluation (including real time, time taken by the CPU, and the time spent collecting free memory). The value of time is the same as that of expression.

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
+-------------------------------------------------+
| [構文]                                        |
|                                                 |
| (define-struct structure-name (field-name...)) |
+-------------------------------------------------+
```

Defines new 構造体 called 構造体-name. 構造体’s fields は named によって field-names. のあと define-struct, following new 関数s は available:

- make-structure-name: takes a number of
arguments equal to the number of fields in the structure,
and creates a new instance of that structure.
- structure-name-field-name: takes an
instance of the structure and returns the value in the field named by
field-name.
- structure-name?: takes any value, and returns
#true if the value is an instance of the structure.

name の new 関数s introduced によって define-struct 〜してはならない be same として という の other 関数s または 変数s, そうでなければ define-struct reports エラー.

（説明）In Advanced, define-struct introduces one additional 関数:

- set-structure-name-field-name!
: takes an instance of the structure and a value, and
mutates the instance’s field to the given value.

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

Chooses 節 based 上の ある 条件. cond finds first question-式 という 評価結果は #true, then 評価する corresponding answer-式.

If none of the question-expressions evaluates to #true, cond’s value is the answer-expression of the else clause. If there is no else, cond reports an error. If the result of a question-expression is neither #true nor #false, cond also reports an error.

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

とき: 値 の question-式 は #true, もし 評価する then-answer-式. とき: test は #false, もし 評価する else-answer-式.

もし question-式 は neither #true nor #false, もし reports エラー.

```
+--------------------------------------------+
| [構文]                                   |
|                                            |
| (and expression expression expression...) |
+--------------------------------------------+
```

Evaluates へ #true もし すべての 式s は #true. もし 任意の 式 は #false, と 式 評価結果は #false (and 式s へ right の という 式 は ない evaluated.)

もし 任意の の 式s evaluate へ 値 other than #true または #false, と reports エラー.

```
+-------------------------------------------+
| [構文]                                  |
|                                           |
| (or expression expression expression...) |
+-------------------------------------------+
```

to #true as soon as one of the expressions is #true (and the expressions to the right of that expression are not evaluated.) If all of the expressions are #false, the or expression evaluates to #false を評価します。

もし 任意の の 式s evaluate へ 値 other than #true または #false, または reports エラー.

```
+-----------------------------------------------+
| [構文]                                      |
|                                               |
| (check-expect expression expected-expression) |
+-----------------------------------------------+
```

that the first expression evaluates to the same value as the expected-expression を検査します。

```racket
(check-expect (fahrenheit->celsius 212) 100)
(check-expect (fahrenheit->celsius -40) -40)

(define (fahrenheit->celsius f)
  (* 5/9 (- f 32)))
```

A check-expect expression must be placed at the top-level of a student program. Also it may show up anywhere in the program, including ahead of the tested function definition. By placing check-expects there, a programmer conveys to a future reader the intention behind the program with working examples, thus making it often superfluous to read the function definition proper. Syntax errors in check-expect (and all check forms) are intentionally delayed to run time so that students can write tests *without* necessarily writing complete function headers.

It is an error for expr or expected-expr to produce an inexact number or a function value. As for inexact numbers, it is morally wrong to compare them for plain equality. Instead one tests whether they are both within a small interval; see check-within. As for functions (see Intermediate and up), it is provably impossible to compare functions.

```
+-----------------------------------------------+
| [構文]                                      |
|                                               |
| (check-random expression expected-expression) |
+-----------------------------------------------+
```

that the first expression evaluates to the same value as the expected-expression を検査します。

form supplies same 乱数-数 generator へ both parts. もし both parts request 乱数 数s から same interval の中の same order, they receive same 乱数 数s.

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

Note how 乱数 は called 上の same 数s の中の same order の中の both parts の check-乱数. もし two parts call 乱数 のための different intervals, they は likely へ fail:

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

Because 引数 へ a-helper-関数 は evaluated first, 乱数 は first called のための interval [0,HEIGHT) と then のための [0,WIDTH), という is, の中の different order than の中の preceding check-乱数.

それ は エラー のための expr または expected-expr へ produce 関数 値 または in正確 数; see note 上の check-expect のための details.

```
+----------------------------------------+
| [構文]                               |
|                                        |
| (check-satisfied expression predicate) |
+----------------------------------------+
```

Checks という first 式 satisfies named 述語 (関数 の one 引数). Recall という “satisfies” means “the 関数 produces #true のための given 値.”

ここで は simple examples のための check-satisfied:

```racket
> (check-satisfied 1 odd?)
The test passed!
```

```racket
> (check-satisfied 1 even?)
Ran 1 test.                                       0 tests passed.                                   Check failures:                                                        ┌───┐                                Actual value │ 1 │ does not satisfy even?.                     └───┘                        at line 3, column 0
```

In general check-satisfied empowers プログラム designers へ use defined 関数s へ formulate test suites:

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

And yes, results の htdp-sort satisfy sorted? 述語:

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

whether the value of the expression expression is structurally equal to the value produced by the expected-expression expression; every number in the first expression must be within delta of the corresponding number in the second expression を検査します。

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

Due へ presence の in正確 数s の中の nested data, check-within は correct choice のための testing, と test succeeds もし delta は reasonably large:

例:

```racket
> (check-within (roots-table (list 1.0 2.0 3.0))                (list                  (make-roots 1.0 1.0)                  (make-roots 2  1.414)                  (make-roots 3  1.713))                0.1)
The test passed!
```

対照的に、のとき delta は small, test fails:

例:

```racket
> (check-within (roots-table (list 2.0))                (list                  (make-roots 2  1.414))                #i1e-5)
Ran 1 test.                                                                                                                      0 tests passed.                                                                                                                  Check failures:                                                                                                                                       ┌────────────────────────────────────────┐                                      ┌─────────────────────────┐         Actual value │ '((make-roots 2.0 1.4142135623730951)) │ is not within 1e-5 of expected value │ '((make-roots 2 1.414)) │.                     └────────────────────────────────────────┘                                      └─────────────────────────┘ at line 5, column 0
```

それ は エラー のための 式s または expected-式 へ produce 関数 値; see note 上の check-expect のための details.

もし delta は ない 数, check-within reports エラー.

```
+-------------------------------------------------+
| [構文]                                        |
|                                                 |
| (check-error expression expected-error-message) |
| (check-error expression)                        |
+-------------------------------------------------+
```

that the expression reports an error, where the error messages matches the value of expected-error-message, if it is present を検査します。

ここで は typical beginner example という calls のための use の check-エラー:

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

Consider following two examples の中の この context:

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

that the value of the first expression is that of one of the following expressions を検査します。

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

それ は エラー のための 任意の の 式s へ produce 関数 値; see note 上の check-expect のための details.

```
+---------------------------------------------------------+
| [構文]                                                |
|                                                         |
| (check-range expression low-expression high-expression) |
+---------------------------------------------------------+
```

that the value of the first expression is a number in between the value of the low-expression and the high-expression, inclusive を検査します。

A check-range form は best used へ delimit possible results の 関数s という compute in正確 数s:

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

それ は エラー のための 式, low-式, または high-式 へ produce 関数 値; see note 上の check-expect のための details.

```
+----------------------+
| [構文]             |
|                      |
| (require string)     |
+----------------------+
```

Makes 定義s の モジュール specified によって 文字列 available の中の current モジュール (i.e., current file), where 文字列 refers へ file relative へ current file.

The string is constrained in several ways to avoid problems with different path conventions on different platforms: a / is a directory separator,. always means the current directory,.. always means the parent directory, path elements can use only a through z (uppercase or lowercase), 0 through 9, -, _, and., and the string cannot be empty or contain a leading or trailing /.

```
+-----------------------+
| [構文]              |
|                       |
| (require module-name) |
+-----------------------+
```

Accesses file の中の installed ライブラリ. ライブラリ name は 識別子 とともに same constraints として のための relative-path 文字列 (though without quotes), とともに additional constraint という it 〜してはならない contain a..

```
+-----------------------------------+
| [構文]                          |
|                                   |
| (require (lib string string...)) |
+-----------------------------------+
```

Accesses a file in an installed library, making its definitions available in the current module (i.e., the current file). The first string names the library file, and the remaining strings name the collection (and sub-collection, and so on) where the file is installed. Each string is constrained in the same way as for the (requirestring) form.

```
+---------------------------------------------------------+
| [構文]                                                |
|                                                         |
| (require (planet string (string string number number))) |
+---------------------------------------------------------+
```

Accesses ライブラリ という は distributed 上の internet via PLaneT server, making it 定義s available の中の current モジュール (i.e., current file).

full grammar のための planet requires は given の中の Importing と Exporting: require と provide, but best place へ find examples の syntax は 上の the PLaneT server, の中の description の specific package.

### 5.5 あらかじめ定義された関数

### 5.6 シグネチャ

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

#### 5.6.1 シグネチャ形式

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

これ シグネチャ describes 値s through 述語: 式 must evaluate へ 関数 の one 引数 という 返す 真偽値. シグネチャ matches すべての 値s のための であり 述語 返す #true.

#### 5.6.2 構造体シグネチャ

> A advanced form defines two additional names that can be > used in signatures. For a struct called struct, these > are Struct and StructOf. Note that > these names are capitalized. In particular, a struct called > Struct, will also define Struct and > StructOf. Moreover, when forming the additional > names, hyphens are removed, and each letter following a hyphen is > capitalized - so a struct called foo-bar will define > FooBar and FooBarOf.Struct is a signature that describes struct values > from this structure type. StructOf is a function > that takes as input a signature for each field. It returns a > signature describing values of this structure type, additionally > describing the values of the fields of the value.

```racket
(define-struct pair [fst snd])

(: add-pair ((PairOf Number Number) -> Number))
(define (add-pair p)
  (+ (pair-fst p) (pair-snd p)))
```

remaining subsections リスト それらの 関数s という は built へ プログラムming language. All other 関数s は imported から teachpack または でなければならない defined の中の プログラム.

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

Subtracts second (and following) 数(s) から first; negates 数 もし there は only one 引数.

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

Increments given 数.

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

Flips sign の imaginary part の 複素数 数.

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

Approximates in正確 数 によって 正確 one.

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

Looks up 文字 という corresponds へ given 正確 整数 の中の ASCII table (if any).

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

〜かどうかを判定する:  ある 値 は 数:

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
+----------------------+
| [手続き]          |
|                      |
| (random x) → natural |
| x: natural          |
+----------------------+
```

Generates 乱数 数. もし given one 引数 乱数 返す natural 数 less than given natural. In ASL, もし given no 引数s, 乱数 generates 乱数 in正確 数 between 0.0 と 1.0 exclusive.

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

Rounds 実数 数 へ 整数 (rounds へ even へ break ties). 参照: floor と ceiling.

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

Decrements given 数.

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

### 5.8 真偽値

```
+------------------------------+
| [手続き]                  |
|                              |
| (boolean->string x) → string |
| x: boolean?                 |
+------------------------------+
```

Produces 文字列 のための given 真偽値

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

Negates 真偽値 値.

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

### 5.10 リスト

```
+-------------------------------+
| [手続き]                   |
|                               |
| (append l...) → (listof any) |
| l: (listof any)              |
+-------------------------------+
```

a single list from several. In ASL, list* also deals with cyclic lists を作成します。

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

〜かどうかを判定する:  ある item は first item の pair の中の リスト の pairs. (それ compares items とともに eq?.)

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

LISP-style selector: (cdr(cdr(carx)))

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
+-------------------------+
| [手続き]             |
|                         |
| (cons x l) → (listof X) |
| x: X                   |
| l: (listof X)          |
+-------------------------+
```

a list. In ASL, cons creates a mutable list を構築します。

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
+----------------------------+
| [手続き]                |
|                            |
| (for-each f l...) → void? |
| f: (any... -> any)       |
| l: (listof any)           |
+----------------------------+
```

Applies 関数 へ 各 item 上の one または more リストs のための effect only:

```racket
(for-each f (list x-1... x-n)) = (begin (f x-1)... (f x-n))
```

```racket
> (for-each (lambda (x) (begin (display x) (newline))) '(1 2 3))
123
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
+--------------------------------+
| [手続き]                    |
|                                |
| (list* x... l) → (listof any) |
| x: any                        |
| l: (listof any)               |
+--------------------------------+
```

a list by adding multiple items to a list. In ASL, list* also deals with cyclic lists を構築します。

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

〜かどうかを判定する:  ある 値 は 上の リスト もし so, it produces suffix の リスト という starts とともに x もし not, it produces false. (それ compares 値s とともに eqv? 述語.)

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

Another name のための 空リスト

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

### 5.11 Posn

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

```
+---------------------------+
| [手続き]               |
|                           |
| (set-posn-x! p x) → void? |
| p: posn                  |
| x: any                   |
+---------------------------+
```

the x component of a posn を更新します。

```racket
> p
(make-posn 2 -3)
> (set-posn-x! p 678)
> p
(make-posn 678 -3)
```

```
+--------------------------+
| [手続き]              |
|                          |
| (set-posn-y! p x) → void |
| p: posn                 |
| x: any                  |
+--------------------------+
```

the y component of a posn を更新します。

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
| [手続き]                 |
|                             |
| (char->integer c) → integer |
| c: char                    |
+-----------------------------+
```

Looks up 数 という corresponds へ given 文字 の中の ASCII table (if any).

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

### 5.13 文字列

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

two images are equal かどうかを判定します。

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

a value is an image かどうかを判定します。

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

whether x and y are within eps of either other を検査します。

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

the current “time” in fixnum milliseconds (possibly negative) を返します。

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
| (force v) → any      |
| v: any              |
+----------------------+
```

the delayed value; see also delay を探します。

```
+----------------------+
| [手続き]          |
|                      |
| (gensym) → symbol?   |
+----------------------+
```

Generates new シンボル, different から すべての シンボルs の中の プログラム.

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

a value is delayed かどうかを判定します。

```
+----------------------+
| [手続き]          |
|                      |
| (sleep sec) → void   |
| sec: positive-num   |
+----------------------+
```

Causes プログラム へ sleep のための given 数 の seconds.

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

```
+----------------------+
| [手続き]          |
|                      |
| (void) → void?       |
+----------------------+
```

a void value を生成します。

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

a value is void かどうかを判定します。

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

### 5.19 Posn

```
+----------------------+
| [手続き]          |
|                      |
| (posn) → signature   |
+----------------------+
```

posns のシグネチャ。

### 5.20 高階関数

### 5.21 数（緩和条件・拡張）

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

### 5.22 高階関数（lambda つき）

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

### 5.23 読み取りと表示

```
+----------------------+
| [手続き]          |
|                      |
| (display x) → void   |
| x: any              |
+----------------------+
```

Prints 引数 へ stdout (without quotes 上の シンボルs と 文字列s, etc.).

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

Prints newline.

```
+-------------------------+
| [手続き]             |
|                         |
| (pretty-print x) → void |
| x: any                 |
+-------------------------+
```

Pretty prints S-式s (like write).

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

Prints 引数 として 値.

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

Formats rest の 引数s according へ first 引数 と print it.

```
+----------------------+
| [手続き]          |
|                      |
| (read) → sexp        |
+----------------------+
```

Reads input から user.

```
+----------------------------------+
| [手続き]                      |
|                                  |
| (with-input-from-file f p) → any |
| f: string                       |
| p: (-> any)                     |
+----------------------------------+
```

Opens named input file f と allows p へ read から it.

```
+------------------------------------+
| [手続き]                        |
|                                    |
| (with-input-from-string s p) → any |
| s: string                         |
| p: (-> any)                       |
+------------------------------------+
```

Turns s へ input のための read operations の中の p.

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

Opens named output file f と allows p へ write へ it.

```
+---------------------------------+
| [手続き]                     |
|                                 |
| (with-output-to-string p) → any |
| p: (-> any)                    |
+---------------------------------+
```

a string from all write/display/print operations in p を生成します。

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

Prints 引数 へ stdout (in traditional style という は somewhere between print と display).

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

a vector by applying f to the numbers 0 through (-n1) を構築します。

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

Transforms l へ vector.

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

a vector of n copies of x を構築します。

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

a vector from the given values を構築します。

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

Transforms v へ リスト.

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

判定する:  length の v.

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

the nth element from v を取り出します。

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

v at position n to be x を更新します。

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

a value is a vector かどうかを判定します。

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

a box を構築します。

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

a value is a box かどうかを判定します。

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

a box を更新します。

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

the boxed value を取り出します。

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

Copies hash table.

```
+--------------------------+
| [手続き]              |
|                          |
| (hash-count h) → integer |
| h: hash                 |
+--------------------------+
```

判定する:  数 の keys mapped によって hash table.

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

a hash table uses eq? for comparisons かどうかを判定します。

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

a hash table uses equal? for comparisons かどうかを判定します。

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

a hash table uses eqv? for comparisons かどうかを判定します。

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

a function to each mapping of a hash table for effect only を適用します。

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

a key is associated with a value in a hash table かどうかを判定します。

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

a new list by applying a function to each mapping of a hash table を構築します。

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

the value associated with a key from a hash table; the three argument case allows a default value or default value computation を取り出します。

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

the value associated with a key from a mutable hash table; if the key does not have an mapping, the third argument is used as the value (or used to compute the value) and is added to the hash table associated with the key を取り出します。

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

an immutable hash table with one less mapping than an existing immutable hash table を構築します。

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

Removes mapping から mutable hash table.

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

an immutable hash table with one new mapping from an existing immutable hash table を構築します。

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

a mutable hash table with a new mapping を更新します。

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

Composes hash-ref と hash-set へ update existing mapping; third 引数 は used へ compute new mapping 値; fourth 引数 は used として third 引数 へ hash-ref.

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

Composes hash-ref と hash-set! へ update existing mapping; third 引数 は used へ compute new mapping 値; fourth 引数 は used として third 引数 へ hash-ref.

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

a value is a hash table かどうかを判定します。

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

a mutable hash table from an optional list of mappings that uses equal? for comparisons を構築します。

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

a mutable hash table from an optional list of mappings that uses eq? for comparisons を構築します。

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

a mutable hash table from an optional list of mappings that uses eqv? for comparisons を構築します。

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

an immutable hash table from an optional list of mappings that uses equal? for comparisons を構築します。

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

an immutable hash table from an optional list of mappings that uses eq? for comparisons を構築します。

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

an immutable hash table from an optional list of mappings that uses eqv? for comparisons を構築します。

```racket
> (make-immutable-hasheqv)
(make-immutable-hasheqv)
> (make-immutable-hasheqv '((b 69) (e 61) (i 999)))
(make-immutable-hasheqv (list (list 'b 69) (list 'e 61) (list 'i 999)))
```
