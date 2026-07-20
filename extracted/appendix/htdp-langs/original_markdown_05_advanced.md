<!-- Appendix manual: htdp-langs -->
<!-- Source URL path: /htdp-langs/advanced.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/htdp-langs/advanced.html -->
<!-- Canonical English source for Japanese translation -->

## 5 Advanced Student

The grammar notation uses the notation X... (bold
dots) to indicate that X may occur an arbitrary number of times
(zero, one, or more). Separately, the grammar also defines... as an
identifier to be used in templates.

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

A name or a variable is a sequence of characters
not including a space or one of the following:

", ' `
( ) [ ]
{ } |;
#

A number is a number such as 123, 3/2, or
5.5.

A boolean is one of: #true or #false.

Alternative spellings for the #true constant are #t,
true, and #T. Similarly, #f, false, or
#F are also recognized as #false.

A symbol is a quote character followed by a name. A
symbol is a value, just like 42, '(), or #false.

A string is a sequence of characters enclosed by a pair of ". Unlike
symbols, strings may be split into characters and manipulated by a
variety of functions. For example, "abcdef",
"This is a string", and "This is a string with \" inside" are all strings.

A character begins with #\ and has the
name of the character. For example, #\a, #\b,
and #\space are characters.

In function calls, the function appearing
immediately after the open parenthesis can be any functions defined
with define or define-struct, or any one of the
pre-defined functions.

### 5.1 Pre-defined Variables

```
+----------------------+
| [value]              |
|                      |
| empty: empty?       |
+----------------------+
```

The empty list.

```
+----------------------+
| [value]              |
|                      |
| true: boolean?      |
+----------------------+
```

The #true value.

```
+----------------------+
| [value]              |
|                      |
| false: boolean?     |
+----------------------+
```

The #false value.

### 5.2 Template Variables

```
+----------------------+
| [syntax]             |
|                      |
|..                   |
+----------------------+
```

A placeholder for indicating that a function definition is a template.

```
+----------------------+
| [syntax]             |
|                      |
|...                  |
+----------------------+
```

A placeholder for indicating that a function definition is a template.

```
+----------------------+
| [syntax]             |
|                      |
|....                 |
+----------------------+
```

A placeholder for indicating that a function definition is a template.

```
+----------------------+
| [syntax]             |
|                      |
|.....                |
+----------------------+
```

A placeholder for indicating that a function definition is a template.

```
+----------------------+
| [syntax]             |
|                      |
|......               |
+----------------------+
```

A placeholder for indicating that a function definition is a template.

### 5.3 Syntax for Advanced

In Advanced, set! can be used to mutate variables, and
define-struct’s structures are mutatable. define and
lambda can define functions of zero arguments, and function calls can
invoke functions of zero arguments.

```
+------------------------------------+
| [syntax]                           |
|                                    |
| (lambda (variable...) expression) |
+------------------------------------+
```

Creates a function that takes as many arguments as given variables,
and whose body is expression.

```
+-------------------------------+
| [syntax]                      |
|                               |
| (λ (variable...) expression) |
+-------------------------------+
```

The Greek letter λ is a synonym for lambda.

```
+-----------------------------+
| [syntax]                    |
|                             |
| (expression expression...) |
+-----------------------------+
```

Calls the function that results from evaluating the first
expression. The value of the call is the value of function’s body when
every instance of name’s variables are replaced by the values of the
corresponding expressions.

The function being called must come from either a definition appearing before the
function call, or from a lambda expression. The number of argument
expressions must be the same as the number of arguments expected by
the function.

```
+------------------------------------------------------------------+
| [syntax]                                                         |
|                                                                  |
| (define-datatype dataype-name [variant-name field-name...]...) |
+------------------------------------------------------------------+
```

A short-hand for defining a group of related structures. The following define-datatype:

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
| [syntax]                          |
|                                   |
| (begin expression expression...) |
+-----------------------------------+
```

Evaluates the expressions in order from left to right. The value of
the begin expression is the value of the last expression.

```
+------------------------------------+
| [syntax]                           |
|                                    |
| (begin0 expression expression...) |
+------------------------------------+
```

Evaluates the expressions in order from left to right. The value of
the begin expression is the value of the first expression.

```
+----------------------------+
| [syntax]                   |
|                            |
| (set! variable expression) |
+----------------------------+
```

Evaluates expression, and then changes the value of the variable
to have expression’s value. The variable must be defined
by define, letrec, let*, let, or local.

```
+----------------------+
| [syntax]             |
|                      |
| (delay expression)   |
+----------------------+
```

Produces a “promise” to evaluate expression. The expression
is not evaluated until the promise is forced with force; when
the promise is forced, the result is recorded, so that any further
force of the promise immediately produces the remembered value.

```
+---------------------------------------------+
| [syntax]                                    |
|                                             |
| (shared ([name expression]...) expression) |
+---------------------------------------------+
```

Like letrec, but when an expression next to an id
is a cons, list, vector, quasiquoted
expression, or make-struct-name from a
define-struct, the expression can refer directly to any
name, not just names defined earlier. Thus,
shared can be used to create cyclic data structures.

```
+-------------------------------------------------+
| [syntax]                                        |
|                                                 |
| (recur name ([name expression]...) expression) |
+-------------------------------------------------+
```

A short-hand syntax for recursive loops. The first name corresponds to
the name of the recursive function. The names in the parenthesis are
the function’s arguments, and each corresponding expression is a
value supplied for that argument in an initial starting call of the
function. The last expression is the body of the function.

More precisely, the following recur:

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
| [syntax]                                      |
|                                               |
| (let name ([name expression]...) expression) |
+-----------------------------------------------+
```

An alternate syntax for recur.

```
+---------------------------------------------------------------------------+
| [syntax]                                                                  |
|                                                                           |
| (case expression [(choice...) expression]... [(choice...) expression]) |
+---------------------------------------------------------------------------+
```

A case form contains one or more clauses. Each clause contains a
choices (in parentheses)—either numbers or names—and an answer
expression. The initial expression is evaluated, and its
value is compared to the choices in each clause, where the lines are considered
in order. The first line that contains a matching choice provides an answer
expression whose value is the result of the whole case
expression. Numbers match with the numbers in the choices, and symbols match
with the names. If none of the lines contains a matching choice, it is an
error.

```
+-------------------------------------------------------------------+
| [syntax]                                                          |
|                                                                   |
| (case expression [(choice...) expression]... [else expression]) |
+-------------------------------------------------------------------+
```

This form of case is similar to the prior one, except that the final
else clause is taken if no clause contains a choice matching the value
of the initial expression.

```
+---------------------------------------------+
| [syntax]                                    |
|                                             |
| (match expression [pattern expression]...) |
+---------------------------------------------+
```

A match form contains one or more clauses that are surrounded by
square brackets. Each clause contains a pattern—a description of a value—and
an answer expression. The initial expression is evaluated,
and its value is matched against the pattern in each clause, where the clauses are
considered in order. The first clause that contains a matching pattern provides
an answer expression whose value is the result of the whole
match expression. This expression may reference identifiers
defined in the matching pattern. If none of the clauses contains a matching
pattern, it is an error.

```
+--------------------------------------------+
| [syntax]                                   |
|                                            |
| (when question-expression body-expression) |
+--------------------------------------------+
```

If question-expression evaluates to true, the result of the
when expression is the result of evaluating the
body-expression, otherwise the result is (void) and the
body-expression is not evaluated. If the result of evaluating the
question-expression is neither true nor false, it is an
error.

```
+----------------------------------------------+
| [syntax]                                     |
|                                              |
| (unless question-expression body-expression) |
+----------------------------------------------+
```

Like when, but the body-expression is evaluated when the
question-expression produces false instead of true.

### 5.4 Common Syntaxes

The following syntaxes behave the same in the *Advanced*
level as they did in the Intermediate Student with Lambda level.

```
+-------------------------------------+
| [syntax]                            |
|                                     |
| (local [definition...] expression) |
+-------------------------------------+
```

Groups related definitions for use in expression. Each
definition can be either a define or a
define-struct.

When evaluating local, each definition is evaluated
in order, and finally the body expression is
evaluated. Only the expressions within the local (including
the right-hand-sides of the definitions and the
expression) may refer to the names defined by the
definitions. If a name defined in the local is the
same as a top-level binding, the inner one “shadows” the outer
one. That is, inside the local, any references to that name
refer to the inner one.

```
+-----------------------------------------------+
| [syntax]                                      |
|                                               |
| (letrec ([name expr-for-let]...) expression) |
+-----------------------------------------------+
```

Like local, but with a simpler syntax. Each name
defines a variable (or a function) with the value of the
corresponding expr-for-let. If expr-for-let is a
lambda, letrec defines a function, otherwise it
defines a variable.

```
+---------------------------------------------+
| [syntax]                                    |
|                                             |
| (let* ([name expr-for-let]...) expression) |
+---------------------------------------------+
```

Like letrec, but each name can only be used in
expression, and in expr-for-lets occuring after
that name.

```
+--------------------------------------------+
| [syntax]                                   |
|                                            |
| (let ([name expr-for-let]...) expression) |
+--------------------------------------------+
```

Like letrec, but the defined names can be used only
in the last expression, not the expr-for-lets
next to the names.

```
+----------------------+
| [syntax]             |
|                      |
| (time expression)    |
+----------------------+
```

Measures the time taken to evaluate expression. After
evaluating expression, time prints out the time
taken by the evaluation (including real time, time taken by the
CPU, and the time spent collecting free memory). The value of
time is the same as that of expression.

```
+--------------------------------------------------+
| [syntax]                                         |
|                                                  |
| (define (name variable variable...) expression) |
+--------------------------------------------------+
```

Defines a function named name. The expression is the body
of the function. When the function is called,
the values of the arguments are inserted into the body in place of the
variables. The function returns the value of that new expression.

The function name’s cannot be the same as that of another function or
variable.

```
+--------------------------+
| [syntax]                 |
|                          |
| (define name expression) |
+--------------------------+
```

Defines a variable called name with the the value of
expression. The variable name’s cannot be the same as that of
another function or variable, and name itself must not appear in
expression.

```
+-------------------------------------------------+
| [syntax]                                        |
|                                                 |
| (define-struct structure-name (field-name...)) |
+-------------------------------------------------+
```

Defines a new structure called structure-name. The structure’s fields are
named by the field-names. After the define-struct, the following new
functions are available:

- make-structure-name: takes a number of
arguments equal to the number of fields in the structure,
and creates a new instance of that structure.
- structure-name-field-name: takes an
instance of the structure and returns the value in the field named by
field-name.
- structure-name?: takes any value, and returns
#true if the value is an instance of the structure.

The name of the new functions introduced by define-struct
must not be the same as that of other functions or variables,
otherwise define-struct reports an error.

In Advanced, define-struct introduces one additional function:

- set-structure-name-field-name!
: takes an instance of the structure and a value, and
mutates the instance’s field to the given value.

```
+-----------------------------------------------------------------------------+
| [syntax]                                                                    |
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

Chooses a clause based on some condition. cond finds the first
question-expression that evaluates to #true, then
evaluates the corresponding answer-expression.

If none of the question-expressions evaluates to #true,
cond’s value is the answer-expression of the
else clause. If there is no else, cond reports
an error. If the result of a question-expression is neither
#true nor #false, cond also reports an error.

else cannot be used outside of cond.

```
+-----------------------------+
| [syntax]                    |
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

When the value of the question-expression is #true,
if evaluates the then-answer-expression. When the test is
#false, if evaluates the else-answer-expression.

If the question-expression is neither #true nor
#false, if reports an error.

```
+--------------------------------------------+
| [syntax]                                   |
|                                            |
| (and expression expression expression...) |
+--------------------------------------------+
```

Evaluates to #true if all the expressions are
#true. If any expression is #false, the and
expression evaluates to #false (and the expressions to the
right of that expression are not evaluated.)

If any of the expressions evaluate to a value other than #true or
#false, and reports an error.

```
+-------------------------------------------+
| [syntax]                                  |
|                                           |
| (or expression expression expression...) |
+-------------------------------------------+
```

Evaluates to #true as soon as one of the
expressions is #true (and the expressions to the right of that
expression are not evaluated.) If all of the expressions are #false,
the or expression evaluates to #false.

If any of the expressions evaluate to a value other than #true or
#false, or reports an error.

```
+-----------------------------------------------+
| [syntax]                                      |
|                                               |
| (check-expect expression expected-expression) |
+-----------------------------------------------+
```

Checks that the first expression evaluates to the same value as the
expected-expression.

```racket
(check-expect (fahrenheit->celsius 212) 100)
(check-expect (fahrenheit->celsius -40) -40)

(define (fahrenheit->celsius f)
  (* 5/9 (- f 32)))
```

A check-expect expression must be placed at the top-level of a
student program. Also it may show up anywhere in the program, including
ahead of the tested function definition. By placing check-expects
there, a programmer conveys to a future reader the intention behind the
program with working examples, thus making it often superfluous to read
the function definition proper. Syntax errors in
check-expect (and all check forms)
are intentionally delayed to run time so that students can write tests
*without* necessarily writing complete function headers.

It is an error for expr or expected-expr to produce an
inexact number or a function value. As for inexact numbers, it is
morally wrong to compare them for plain equality. Instead one
tests whether they are both within a small interval; see
check-within. As for functions (see Intermediate and up), it is
provably impossible to compare functions.

```
+-----------------------------------------------+
| [syntax]                                      |
|                                               |
| (check-random expression expected-expression) |
+-----------------------------------------------+
```

Checks that the first expression evaluates to the same value as the
expected-expression.

The form supplies the same random-number generator to both parts. If both
parts request random numbers from the same interval in the same
order, they receive the same random numbers.

Here is a simple example of where check-random is useful:

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

Note how random is called on the same numbers in the same order in
both parts of check-random. If the two parts call random
for different intervals, they are likely to fail:

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

Because the argument to a-helper-function is evaluated first,
random is first called for the interval [0,HEIGHT) and then
for [0,WIDTH), that is, in a different order than in the preceding
check-random.

It is an error for expr or expected-expr to produce a function
value or an inexact number; see note on check-expect for details.

```
+----------------------------------------+
| [syntax]                               |
|                                        |
| (check-satisfied expression predicate) |
+----------------------------------------+
```

Checks that the first expression satisfies the named
predicate (function of one argument). Recall that
“satisfies” means “the function produces #true for the given
value.”

Here are simple examples for check-satisfied:

```racket
> (check-satisfied 1 odd?)
The test passed!
```

```racket
> (check-satisfied 1 even?)
Ran 1 test.                                       0 tests passed.                                   Check failures:                                                        ┌───┐                                Actual value │ 1 │ does not satisfy even?.                     └───┘                        at line 3, column 0
```

In general check-satisfied empowers program designers to use
defined functions to formulate test suites:

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

And yes, the results of htdp-sort satisfy the sorted? predicate:

```racket
> (check-satisfied (htdp-sort (list 1 2 0 3)) sorted?)
```

```
+-----------------------------------------------------+
| [syntax]                                            |
|                                                     |
| (check-within expression expected-expression delta) |
+-----------------------------------------------------+
```

Checks whether the value of the expression expression is
structurally equal to the value produced by the
expected-expression expression; every number in the first
expression must be within delta of the corresponding number in
the second expression.

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

Due to the presence of inexact numbers in nested data, check-within is the
correct choice for testing, and the test succeeds if delta is reasonably
large:

Example:

```racket
> (check-within (roots-table (list 1.0 2.0 3.0))                (list                  (make-roots 1.0 1.0)                  (make-roots 2  1.414)                  (make-roots 3  1.713))                0.1)
The test passed!
```

In contrast, when delta is small, the test fails:

Example:

```racket
> (check-within (roots-table (list 2.0))                (list                  (make-roots 2  1.414))                #i1e-5)
Ran 1 test.                                                                                                                      0 tests passed.                                                                                                                  Check failures:                                                                                                                                       ┌────────────────────────────────────────┐                                      ┌─────────────────────────┐         Actual value │ '((make-roots 2.0 1.4142135623730951)) │ is not within 1e-5 of expected value │ '((make-roots 2 1.414)) │.                     └────────────────────────────────────────┘                                      └─────────────────────────┘ at line 5, column 0
```

It is an error for expressions or expected-expression
to produce a function value; see note on check-expect for details.

If delta is not a number, check-within reports an error.

```
+-------------------------------------------------+
| [syntax]                                        |
|                                                 |
| (check-error expression expected-error-message) |
| (check-error expression)                        |
+-------------------------------------------------+
```

Checks that the expression reports an error, where the error messages
matches the value of expected-error-message, if it is present.

Here is a typical beginner example that calls for a use of check-error:

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

Consider the following two examples in this context:

Example:

```racket
> (check-expect (lookup sample-table "matthew") 20)
The test passed!
```

Example:

```racket
> (check-error (lookup sample-table "kathi") "kathi not found")
The test passed!
```

```
+--------------------------------------------------------+
| [syntax]                                               |
|                                                        |
| (check-member-of expression expression expression...) |
+--------------------------------------------------------+
```

Checks that the value of the first expression is that of
one of the following expressions.

```racket
; [List-of X] -> X
; pick a random element from the given list l
(define (pick-one l)
  (list-ref l (random (length l))))
```

Example:

```racket
> (check-member-of (pick-one '("a" "b" "c")) "a" "b" "c")
The test passed!
```

It is an error for any of expressions to produce a function value; see
note on check-expect for details.

```
+---------------------------------------------------------+
| [syntax]                                                |
|                                                         |
| (check-range expression low-expression high-expression) |
+---------------------------------------------------------+
```

Checks that the value of the first expression is a number in
between the value of the low-expression and the
high-expression, inclusive.

A check-range form is best used to delimit the possible results of
functions that compute inexact numbers:

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

It is an error for expression, low-expression, or
high-expression to produce a function value;
see note on check-expect for details.

```
+----------------------+
| [syntax]             |
|                      |
| (require string)     |
+----------------------+
```

Makes the definitions of the module specified by string
available in the current module (i.e., the current file), where
string refers to a file relative to the current file.

The string is constrained in several ways to avoid
problems with different path conventions on different platforms: a
/ is a directory separator,. always means the
current directory,.. always means the parent directory,
path elements can use only a through z
(uppercase or lowercase), 0 through 9,
-, _, and., and the string cannot be
empty or contain a leading or trailing /.

```
+-----------------------+
| [syntax]              |
|                       |
| (require module-name) |
+-----------------------+
```

Accesses a file in an installed library. The library name is an
identifier with the same constraints as for a relative-path string
(though without the quotes), with the additional constraint that it
must not contain a..

```
+-----------------------------------+
| [syntax]                          |
|                                   |
| (require (lib string string...)) |
+-----------------------------------+
```

Accesses a file in an installed library, making its definitions
available in the current module (i.e., the current file). The first
string names the library file, and the remaining
strings name the collection (and sub-collection, and so on)
where the file is installed. Each string is constrained in the same
way as for the (requirestring) form.

```
+---------------------------------------------------------+
| [syntax]                                                |
|                                                         |
| (require (planet string (string string number number))) |
+---------------------------------------------------------+
```

Accesses a library that is distributed on the internet via the
PLaneT server, making it definitions available in the current module
(i.e., current file).

The full grammar for planet requires is given in
Importing and Exporting: require and provide, but
the best place to find examples of the syntax is on the
the PLaneT server, in the
description of a specific package.

### 5.5 Pre-Defined Functions

### 5.6 Signatures

> Signatures do not have to be comment: They can also be part of the
> code. When a signature is attached to a function, DrRacket will check
> that program uses the function in accordance with the signature and
> display signature violations along with the test results.A signature is a regular value, and is specified as a
> signature form, a
> special syntax that only works with: signature declarations
> and inside signature expressions.

```
+-------------------------+
| [syntax]                |
|                         |
| (: name signature-form) |
+-------------------------+
```

This attaches the signature specified by signature-form to
the definition of name.
There must be a definition of name somewhere in the program.

```racket
(: age Integer)
(define age 42)

(: area-of-square (Number -> Number))
(define (area-of-square len)
  (sqr len))
```

On running the program, Racket checks whether the signatures attached
with: actually match the value of the variable. If they
don’t, Racket reports signature violation along with test failures.

For example, this piece of code:

```racket
(: age Integer)
(define age "fortytwo")
```

Yields this output:

```
+--------------------------------------------------+
| `1 signature violation.`                         |
+--------------------------------------------------+
| `Signature violations:`                          |
| `got "fortytwo" at line 2, column 12, signature… |
+--------------------------------------------------+
```

Note that a signature violation does not stop the running program.

```
+----------------------------+
| [syntax]                   |
|                            |
| (signature signature-form) |
+----------------------------+
```

This returns the signature described by signature-form as a value.

#### 5.6.1 Signature Forms

> Any expression can be a signature form, in which case the signature is
> the value returned by that expression. There are a few special
> signature forms, however:In a signature form, any name that starts with a % is a
> signature variable that stands for any signature depending on how
> the signature is used.Example:

```racket
(: same (%a -> %a))

(define (same x) x)
```

```
+-----------------------------------------------------+
| [syntax]                                            |
|                                                     |
| (input-signature-form... -> output-signature-form) |
+-----------------------------------------------------+
```

This signature form describes a function with inputs described by the
input-signature-forms and output described by
output-signature-form.

```
+----------------------+
| [syntax]             |
|                      |
| (enum expr...)      |
+----------------------+
```

This signature describes an enumeration of the values returned by the exprs.

Example:

```racket
(: cute? ((enum "cat" "snake") -> Boolean))

(define (cute? pet)
  (cond
    [(string=? pet "cat") #t]
    [(string=? pet "snake") #f]))
```

```
+----------------------------+
| [syntax]                   |
|                            |
| (mixed signature-form...) |
+----------------------------+
```

This signature describes mixed data, i.e. an itemization where
each of the cases has a signature described by a signature-form.

Example:

```racket
(define SIGS (signature (mixed Aim Fired)))
```

```
+-------------------------+
| [syntax]                |
|                         |
| (ListOf signature-form) |
+-------------------------+
```

This signature describes a list where the elements are described by
signature-form.

```
+------------------------+
| [syntax]               |
|                        |
| (predicate expression) |
+------------------------+
```

This signature describes values through a predicate:
expression must evaluate to a function of one argument that
returns a boolean. The signature matches all values for which
the predicate returns #true.

#### 5.6.2 Struct Signatures

> A advanced form defines two additional names that can be
> used in signatures. For a struct called struct, these
> are Struct and StructOf. Note that
> these names are capitalized. In particular, a struct called
> Struct, will also define Struct and
> StructOf. Moreover, when forming the additional
> names, hyphens are removed, and each letter following a hyphen is
> capitalized - so a struct called foo-bar will define
> FooBar and FooBarOf.Struct is a signature that describes struct values
> from this structure type. StructOf is a function
> that takes as input a signature for each field. It returns a
> signature describing values of this structure type, additionally
> describing the values of the fields of the value.

```racket
(define-struct pair [fst snd])

(: add-pair ((PairOf Number Number) -> Number))
(define (add-pair p)
  (+ (pair-fst p) (pair-snd p)))
```

The remaining subsections list those functions that are built into the
programming language. All other functions are imported from a teachpack or
must be defined in the program.

### 5.7 Numbers: Integers, Rationals, Reals, Complex, Exacts, Inexacts

```
+----------------------+
| [procedure]          |
|                      |
| (- x y...) → number |
| x: number           |
| y: number           |
+----------------------+
```

Subtracts the second (and following) number(s) from the first;
negates the number if there is only one argument.

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
| [procedure]              |
|                          |
| (< x y z...) → boolean? |
| x: real                 |
| y: real                 |
| z: real                 |
+--------------------------+
```

Compares two or more (real) numbers for less-than.

```racket
> (< 42 2/5)
#false
```

```
+---------------------------+
| [procedure]               |
|                           |
| (<= x y z...) → boolean? |
| x: real                  |
| y: real                  |
| z: real                  |
+---------------------------+
```

Compares two or more (real) numbers for less-than or equality.

```racket
> (<= 42 2/5)
#false
```

```
+--------------------------+
| [procedure]              |
|                          |
| (> x y z...) → boolean? |
| x: real                 |
| y: real                 |
| z: real                 |
+--------------------------+
```

Compares two or more (real) numbers for greater-than.

```racket
> (> 42 2/5)
#true
```

```
+---------------------------+
| [procedure]               |
|                           |
| (>= x y z...) → boolean? |
| x: real                  |
| y: real                  |
| z: real                  |
+---------------------------+
```

Compares two or more (real) numbers for greater-than or equality.

```racket
> (>= 42 42)
#true
```

```
+----------------------+
| [procedure]          |
|                      |
| (abs x) → real       |
| x: real             |
+----------------------+
```

Determines the absolute value of a real number.

```racket
> (abs -12)
12
```

```
+----------------------+
| [procedure]          |
|                      |
| (acos x) → number    |
| x: number           |
+----------------------+
```

Computes the arccosine (inverse of cos) of a number.

```racket
> (acos 0)
#i1.5707963267948966
```

```
+----------------------+
| [procedure]          |
|                      |
| (add1 x) → number    |
| x: number           |
+----------------------+
```

Increments the given number.

```racket
> (add1 2)
3
```

```
+----------------------+
| [procedure]          |
|                      |
| (angle x) → real     |
| x: number           |
+----------------------+
```

Extracts the angle from a complex number.

```racket
> (angle (make-polar 3 4))
#i-2.2831853071795867
```

```
+----------------------+
| [procedure]          |
|                      |
| (asin x) → number    |
| x: number           |
+----------------------+
```

Computes the arcsine (inverse of sin) of a number.

```racket
> (asin 0)
0
```

```
+----------------------+
| [procedure]          |
|                      |
| (atan x) → number    |
| x: number           |
+----------------------+
```

Computes the arctangent of the given number:

```racket
> (atan 0)
0
> (atan 0.5)
#i0.4636476090008061
```

Also comes in a two-argument version where (atanyx) computes
(atan(/yx)) but the signs of y and x
determine the quadrant of the result and the result tends to be more
accurate than that of the 1-argument version in borderline cases:

```racket
> (atan 3 4)
#i0.6435011087932844
> (atan -2 -1)
#i-2.0344439357957027
```

```
+-----------------------+
| [procedure]           |
|                       |
| (ceiling x) → integer |
| x: real              |
+-----------------------+
```

Determines the closest integer (exact or inexact) above a real
number. See round.

```racket
> (ceiling 12.3)
#i13.0
```

```
+-------------------------+
| [procedure]             |
|                         |
| (complex? x) → boolean? |
| x: any/c               |
+-------------------------+
```

Determines whether some value is complex.

```racket
> (complex? 1-2i)
#true
```

```
+------------------------+
| [procedure]            |
|                        |
| (conjugate x) → number |
| x: number             |
+------------------------+
```

Flips the sign of the imaginary part of a complex number.

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
| [procedure]          |
|                      |
| (cos x) → number     |
| x: number           |
+----------------------+
```

Computes the cosine of a number (radians).

```racket
> (cos pi)
#i-1.0
```

```
+----------------------+
| [procedure]          |
|                      |
| (cosh x) → number    |
| x: number           |
+----------------------+
```

Computes the hyperbolic cosine of a number.

```racket
> (cosh 10)
#i11013.232920103324
```

```
+-----------------------------+
| [procedure]                 |
|                             |
| (current-seconds) → integer |
+-----------------------------+
```

Determines the current time in seconds elapsed (since a platform-specific starting date).

```racket
> (current-seconds)
1779843347
```

```
+---------------------------+
| [procedure]               |
|                           |
| (denominator x) → integer |
| x: rational?             |
+---------------------------+
```

Computes the denominator of a rational.

```racket
> (denominator 2/3)
3
```

```
+----------------------+
| [value]              |
|                      |
| e: real             |
+----------------------+
```

Euler’s number.

```racket
> e
#i2.718281828459045
```

```
+----------------------+
| [procedure]          |
|                      |
| (even? x) → boolean? |
| x: integer          |
+----------------------+
```

Determines if some integer (exact or inexact) is even or not.

```racket
> (even? 2)
#true
```

```
+-----------------------------+
| [procedure]                 |
|                             |
| (exact->inexact x) → number |
| x: number                  |
+-----------------------------+
```

Converts an exact number to an inexact one.

```racket
> (exact->inexact 12)
#i12.0
```

```
+-----------------------+
| [procedure]           |
|                       |
| (exact? x) → boolean? |
| x: number            |
+-----------------------+
```

Determines whether some number is exact.

```racket
> (exact? (sqrt 2))
#false
```

```
+----------------------+
| [procedure]          |
|                      |
| (exp x) → number     |
| x: number           |
+----------------------+
```

Determines e raised to a number.

```racket
> (exp -2)
#i0.1353352832366127
```

```
+----------------------+
| [procedure]          |
|                      |
| (expt x y) → number  |
| x: number           |
| y: number           |
+----------------------+
```

Computes the power of the first to the second number, which is to say, exponentiation.

```racket
> (expt 16 1/2)
4
> (expt 3 -4)
1/81
```

```
+----------------------+
| [procedure]          |
|                      |
| (floor x) → integer  |
| x: real             |
+----------------------+
```

Determines the closest integer (exact or inexact) below a real
number. See round.

```racket
> (floor 12.3)
#i12.0
```

```
+-------------------------+
| [procedure]             |
|                         |
| (gcd x y...) → integer |
| x: integer             |
| y: integer             |
+-------------------------+
```

Determines the greatest common divisor of two integers (exact or inexact).

```racket
> (gcd 6 12 8)
2
```

```
+----------------------+
| [procedure]          |
|                      |
| (imag-part x) → real |
| x: number           |
+----------------------+
```

Extracts the imaginary part from a complex number.

```racket
> (imag-part 3+4i)
4
```

```
+-----------------------------+
| [procedure]                 |
|                             |
| (inexact->exact x) → number |
| x: number                  |
+-----------------------------+
```

Approximates an inexact number by an exact one.

```racket
> (inexact->exact 12.0)
12
```

```
+-------------------------+
| [procedure]             |
|                         |
| (inexact? x) → boolean? |
| x: number              |
+-------------------------+
```

Determines whether some number is inexact.

```racket
> (inexact? 1-2i)
#false
```

```
+--------------------------+
| [procedure]              |
|                          |
| (integer->char x) → char |
| x: exact-integer?       |
+--------------------------+
```

Looks up the character that corresponds to the given exact integer in the ASCII table (if any).

```racket
> (integer->char 42)
#\*
```

```
+----------------------------+
| [procedure]                |
|                            |
| (integer-sqrt x) → complex |
| x: integer                |
+----------------------------+
```

Computes the integer or imaginary-integer square root of an integer.

```racket
> (integer-sqrt 11)
3
> (integer-sqrt -11)
0+3i
```

```
+-------------------------+
| [procedure]             |
|                         |
| (integer? x) → boolean? |
| x: any/c               |
+-------------------------+
```

Determines whether some value is an integer (exact or inexact).

```racket
> (integer? (sqrt 2))
#false
```

```
+-------------------------+
| [procedure]             |
|                         |
| (lcm x y...) → integer |
| x: integer             |
| y: integer             |
+-------------------------+
```

Determines the least common multiple of two integers (exact or inexact).

```racket
> (lcm 6 12 8)
24
```

```
+----------------------+
| [procedure]          |
|                      |
| (log x) → number     |
| x: number           |
+----------------------+
```

Determines the base-e logarithm of a number.

```racket
> (log 12)
#i2.4849066497880004
```

```
+----------------------+
| [procedure]          |
|                      |
| (magnitude x) → real |
| x: number           |
+----------------------+
```

Determines the magnitude of a complex number.

```racket
> (magnitude (make-polar 3 4))
#i2.9999999999999996
```

```
+---------------------------+
| [procedure]               |
|                           |
| (make-polar x y) → number |
| x: real                  |
| y: real                  |
+---------------------------+
```

Creates a complex from a magnitude and angle.

```racket
> (make-polar 3 4)
#i-1.960930862590836-2.2704074859237844i
```

```
+---------------------------------+
| [procedure]                     |
|                                 |
| (make-rectangular x y) → number |
| x: real                        |
| y: real                        |
+---------------------------------+
```

Creates a complex from a real and an imaginary part.

```racket
> (make-rectangular 3 4)
3+4i
```

```
+----------------------+
| [procedure]          |
|                      |
| (max x y...) → real |
| x: real             |
| y: real             |
+----------------------+
```

Determines the largest number—aka, the maximum.

```racket
> (max 3 2 8 7 2 9 0)
9
```

```
+----------------------+
| [procedure]          |
|                      |
| (min x y...) → real |
| x: real             |
| y: real             |
+----------------------+
```

Determines the smallest number—aka, the minimum.

```racket
> (min 3 2 8 7 2 9 0)
0
```

```
+------------------------+
| [procedure]            |
|                        |
| (modulo x y) → integer |
| x: integer            |
| y: integer            |
+------------------------+
```

Finds the remainder of the division of the first number by the second:

```racket
> (modulo 9 2)
1
> (modulo 3 -4)
-1
```

```
+--------------------------+
| [procedure]              |
|                          |
| (negative? x) → boolean? |
| x: real                 |
+--------------------------+
```

Determines if some real number is strictly smaller than zero.

```racket
> (negative? -2)
#true
```

```
+-----------------------------+
| [procedure]                 |
|                             |
| (number->string x) → string |
| x: number                  |
+-----------------------------+
```

Converts a number to a string.

```racket
> (number->string 42)
"42"
```

```
+--------------------------------------+
| [procedure]                          |
|                                      |
| (number->string-digits x p) → string |
| x: number                           |
| p: posint                           |
+--------------------------------------+
```

Converts a number `x` to a string with the specified number of digits.

```racket
> (number->string-digits 0.9 2)
"0.9"
> (number->string-digits pi 4)
"3.1416"
```

```
+------------------------+
| [procedure]            |
|                        |
| (number? n) → boolean? |
| n: any/c              |
+------------------------+
```

Determines whether some value is a number:

```racket
> (number? "hello world")
#false
> (number? 42)
#true
```

```
+-------------------------+
| [procedure]             |
|                         |
| (numerator x) → integer |
| x: rational?           |
+-------------------------+
```

Computes the numerator of a rational.

```racket
> (numerator 2/3)
2
```

```
+----------------------+
| [procedure]          |
|                      |
| (odd? x) → boolean?  |
| x: integer          |
+----------------------+
```

Determines if some integer (exact or inexact) is odd or not.

```racket
> (odd? 2)
#false
```

```
+----------------------+
| [value]              |
|                      |
| pi: real            |
+----------------------+
```

The ratio of a circle’s circumference to its diameter.

```racket
> pi
#i3.141592653589793
```

```
+--------------------------+
| [procedure]              |
|                          |
| (positive? x) → boolean? |
| x: real                 |
+--------------------------+
```

Determines if some real number is strictly larger than zero.

```racket
> (positive? -2)
#false
```

```
+--------------------------+
| [procedure]              |
|                          |
| (quotient x y) → integer |
| x: integer              |
| y: integer              |
+--------------------------+
```

Divides the first integer—also called dividend—by the second—known as
divisor—to obtain the quotient.

```racket
> (quotient 9 2)
4
> (quotient 3 4)
0
```

```
+----------------------+
| [procedure]          |
|                      |
| (random x) → natural |
| x: natural          |
+----------------------+
```

Generates a random number. If given one argument random returns a natural number
less than the given natural. In ASL, if given no arguments, random generates a
random inexact number between 0.0 and 1.0 exclusive.

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
| [procedure]              |
|                          |
| (rational? x) → boolean? |
| x: any/c                |
+--------------------------+
```

Determines whether some value is a rational number.

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

As the interactions show, the teaching languages considers many more
numbers as rationals than expected. In particular, pi is a
rational number because it is only a finite approximation to the
mathematical π. Think of rational? as a suggestion to think of
these numbers as fractions.

```
+----------------------+
| [procedure]          |
|                      |
| (real-part x) → real |
| x: number           |
+----------------------+
```

Extracts the real part from a complex number.

```racket
> (real-part 3+4i)
3
```

```
+----------------------+
| [procedure]          |
|                      |
| (real? x) → boolean? |
| x: any/c            |
+----------------------+
```

Determines whether some value is a real number.

```racket
> (real? 1-2i)
#false
```

```
+---------------------------+
| [procedure]               |
|                           |
| (remainder x y) → integer |
| x: integer               |
| y: integer               |
+---------------------------+
```

Determines the remainder of dividing
the first by the second integer (exact or inexact).

```racket
> (remainder 9 2)
1
> (remainder 3 4)
3
```

```
+----------------------+
| [procedure]          |
|                      |
| (round x) → integer  |
| x: real             |
+----------------------+
```

Rounds a real number to an integer (rounds to even to break ties). See
floor and ceiling.

```racket
> (round 12.3)
#i12.0
```

```
+---------------------------------------------+
| [procedure]                                 |
|                                             |
| (sgn x) → (union 1 #i1.0 0 #i0.0 -1 #i-1.0) |
| x: real                                    |
+---------------------------------------------+
```

Determines the sign of a real number.

```racket
> (sgn -12)
-1
```

```
+----------------------+
| [procedure]          |
|                      |
| (sin x) → number     |
| x: number           |
+----------------------+
```

Computes the sine of a number (radians).

```racket
> (sin pi)
#i1.2246467991473532e-16
```

```
+----------------------+
| [procedure]          |
|                      |
| (sinh x) → number    |
| x: number           |
+----------------------+
```

Computes the hyperbolic sine of a number.

```racket
> (sinh 10)
#i11013.232874703393
```

```
+----------------------+
| [procedure]          |
|                      |
| (sqr x) → number     |
| x: number           |
+----------------------+
```

Computes the square of a number.

```racket
> (sqr 8)
64
```

```
+----------------------+
| [procedure]          |
|                      |
| (sqrt x) → number    |
| x: number           |
+----------------------+
```

Computes the square root of a number.

```racket
> (sqrt 9)
3
> (sqrt 2)
#i1.4142135623730951
```

```
+----------------------+
| [procedure]          |
|                      |
| (sub1 x) → number    |
| x: number           |
+----------------------+
```

Decrements the given number.

```racket
> (sub1 2)
1
```

```
+----------------------+
| [procedure]          |
|                      |
| (tan x) → number     |
| x: number           |
+----------------------+
```

Computes the tangent of a number (radians).

```racket
> (tan pi)
#i-1.2246467991473532e-16
```

```
+----------------------+
| [procedure]          |
|                      |
| (zero? x) → boolean? |
| x: number           |
+----------------------+
```

Determines if some number is zero or not.

```racket
> (zero? 2)
#false
```

### 5.8 Booleans

```
+------------------------------+
| [procedure]                  |
|                              |
| (boolean->string x) → string |
| x: boolean?                 |
+------------------------------+
```

Produces a string for the given boolean

```racket
> (boolean->string #false)
"#false"
> (boolean->string #true)
"#true"
```

```
+----------------------------+
| [procedure]                |
|                            |
| (boolean=? x y) → boolean? |
| x: boolean?               |
| y: boolean?               |
+----------------------------+
```

Determines whether two booleans are equal.

```racket
> (boolean=? #true #false)
#false
```

```
+-------------------------+
| [procedure]             |
|                         |
| (boolean? x) → boolean? |
| x: any/c               |
+-------------------------+
```

Determines whether some value is a boolean.

```racket
> (boolean? 42)
#false
> (boolean? #false)
#true
```

```
+-----------------------+
| [procedure]           |
|                       |
| (false? x) → boolean? |
| x: any/c             |
+-----------------------+
```

Determines whether a value is false.

```racket
> (false? #false)
#true
```

```
+----------------------+
| [procedure]          |
|                      |
| (not x) → boolean?   |
| x: boolean?         |
+----------------------+
```

Negates a boolean value.

```racket
> (not #false)
#true
```

### 5.9 Symbols

```
+-----------------------------+
| [procedure]                 |
|                             |
| (symbol->string x) → string |
| x: symbol                  |
+-----------------------------+
```

Converts a symbol to a string.

```racket
> (symbol->string 'c)
"c"
```

```
+---------------------------+
| [procedure]               |
|                           |
| (symbol=? x y) → boolean? |
| x: symbol                |
| y: symbol                |
+---------------------------+
```

Determines whether two symbols are equal.

```racket
> (symbol=? 'a 'b)
#false
```

```
+------------------------+
| [procedure]            |
|                        |
| (symbol? x) → boolean? |
| x: any/c              |
+------------------------+
```

Determines whether some value is a symbol.

```racket
> (symbol? 'a)
#true
```

### 5.10 Lists

```
+-------------------------------+
| [procedure]                   |
|                               |
| (append l...) → (listof any) |
| l: (listof any)              |
+-------------------------------+
```

Creates a single list from several.
In ASL, list* also deals with cyclic lists.

```
+-------------------------------------------+
| [procedure]                               |
|                                           |
| (assoc x l) → (union (listof any) #false) |
| x: any/c                                 |
| l: (listof any)                          |
+-------------------------------------------+
```

Produces the first pair on l whose first is equal? to x;
otherwise it produces #false.

```racket
> (assoc "hello" '(("world" 2) ("hello" 3) ("good" 0)))
(list "hello" 3)
```

```
+-----------------------------------+
| [procedure]                       |
|                                   |
| (assq x l) → (union #false cons?) |
| x: any/c                         |
| l: list?                         |
+-----------------------------------+
```

Determines whether some item is the first item of a pair in a list of
pairs. (It compares the items with eq?.)

```racket
> a
(list (list 'a 22) (list 'b 8) (list 'c 70))
> (assq 'b a)
(list 'b 8)
```

```
+----------------------+
| [procedure]          |
|                      |
| (caaar x) → any/c    |
| x: list?            |
+----------------------+
```

LISP-style selector: (car(car(carx))).

```racket
> w
(list (list (list (list "bye") 3) #true) 42)
> (caaar w)
(list "bye")
```

```
+----------------------+
| [procedure]          |
|                      |
| (caadr x) → any/c    |
| x: list?            |
+----------------------+
```

LISP-style selector: (car(car(cdrx))).

```racket
> (caadr (cons 1 (cons (cons 'a '()) (cons (cons 'd '()) '()))))
'a
```

```
+----------------------+
| [procedure]          |
|                      |
| (caar x) → any/c     |
| x: list?            |
+----------------------+
```

LISP-style selector: (car(carx)).

```racket
> y
(list (list (list 1 2 3) #false "world"))
> (caar y)
(list 1 2 3)
```

```
+----------------------+
| [procedure]          |
|                      |
| (cadar x) → any/c    |
| x: list?            |
+----------------------+
```

LISP-style selector: (car(cdr(carx))).

```racket
> w
(list (list (list (list "bye") 3) #true) 42)
> (cadar w)
#true
```

```
+----------------------+
| [procedure]          |
|                      |
| (cadddr x) → any/c   |
| x: list?            |
+----------------------+
```

LISP-style selector: (car(cdr(cdr(cdrx)))).

```racket
> v
(list 1 2 3 4 5 6 7 8 9 'A)
> (cadddr v)
4
```

```
+----------------------+
| [procedure]          |
|                      |
| (caddr x) → any/c    |
| x: list?            |
+----------------------+
```

LISP-style selector: (car(cdr(cdrx))).

```racket
> x
(list 2 "hello" #true)
> (caddr x)
#true
```

```
+----------------------+
| [procedure]          |
|                      |
| (cadr x) → any/c     |
| x: list?            |
+----------------------+
```

LISP-style selector: (car(cdrx)).

```racket
> x
(list 2 "hello" #true)
> (cadr x)
"hello"
```

```
+----------------------+
| [procedure]          |
|                      |
| (car x) → any/c      |
| x: cons?            |
+----------------------+
```

Selects the first item of a non-empty list.

```racket
> x
(list 2 "hello" #true)
> (car x)
2
```

```
+----------------------+
| [procedure]          |
|                      |
| (cdaar x) → any/c    |
| x: list?            |
+----------------------+
```

LISP-style selector: (cdr(car(carx))).

```racket
> w
(list (list (list (list "bye") 3) #true) 42)
> (cdaar w)
(list 3)
```

```
+----------------------+
| [procedure]          |
|                      |
| (cdadr x) → any/c    |
| x: list?            |
+----------------------+
```

LISP-style selector: (cdr(car(cdrx))).

```racket
> (cdadr (list 1 (list 2 "a") 3))
(list "a")
```

```
+----------------------+
| [procedure]          |
|                      |
| (cdar x) → list?     |
| x: list?            |
+----------------------+
```

LISP-style selector: (cdr(carx)).

```racket
> y
(list (list (list 1 2 3) #false "world"))
> (cdar y)
(list #false "world")
```

```
+----------------------+
| [procedure]          |
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
| [procedure]          |
|                      |
| (cdddr x) → any/c    |
| x: list?            |
+----------------------+
```

LISP-style selector: (cdr(cdr(cdrx))).

```racket
> v
(list 1 2 3 4 5 6 7 8 9 'A)
> (cdddr v)
(list 4 5 6 7 8 9 'A)
```

```
+----------------------+
| [procedure]          |
|                      |
| (cddr x) → list?     |
| x: list?            |
+----------------------+
```

LISP-style selector: (cdr(cdrx)).

```racket
> x
(list 2 "hello" #true)
> (cddr x)
(list #true)
```

```
+----------------------+
| [procedure]          |
|                      |
| (cdr x) → any/c      |
| x: cons?            |
+----------------------+
```

Selects the rest of a non-empty list.

```racket
> x
(list 2 "hello" #true)
> (cdr x)
(list "hello" #true)
```

```
+-------------------------+
| [procedure]             |
|                         |
| (cons x l) → (listof X) |
| x: X                   |
| l: (listof X)          |
+-------------------------+
```

Constructs a list.
In ASL, cons creates a mutable list.

```
+----------------------+
| [procedure]          |
|                      |
| (cons? x) → boolean? |
| x: any/c            |
+----------------------+
```

Determines whether some value is a constructed list.

```racket
> (cons? (cons 1 '()))
#true
> (cons? 42)
#false
```

```
+----------------------+
| [procedure]          |
|                      |
| (eighth x) → any/c   |
| x: list?            |
+----------------------+
```

Selects the eighth item of a non-empty list.

```racket
> v
(list 1 2 3 4 5 6 7 8 9 'A)
> (eighth v)
8
```

```
+-----------------------+
| [procedure]           |
|                       |
| (empty? x) → boolean? |
| x: any/c             |
+-----------------------+
```

Determines whether some value is the empty list.

```racket
> (empty? '())
#true
> (empty? 42)
#false
```

```
+----------------------+
| [procedure]          |
|                      |
| (fifth x) → any/c    |
| x: list?            |
+----------------------+
```

Selects the fifth item of a non-empty list.

```racket
> v
(list 1 2 3 4 5 6 7 8 9 'A)
> (fifth v)
5
```

```
+----------------------+
| [procedure]          |
|                      |
| (first x) → any/c    |
| x: cons?            |
+----------------------+
```

Selects the first item of a non-empty list.

```racket
> x
(list 2 "hello" #true)
> (first x)
2
```

```
+----------------------------+
| [procedure]                |
|                            |
| (for-each f l...) → void? |
| f: (any... -> any)       |
| l: (listof any)           |
+----------------------------+
```

Applies a function to each item on one or more lists for effect only:

```racket
(for-each f (list x-1... x-n)) = (begin (f x-1)... (f x-n))
```

```racket
> (for-each (lambda (x) (begin (display x) (newline))) '(1 2 3))
123
```

```
+----------------------+
| [procedure]          |
|                      |
| (fourth x) → any/c   |
| x: list?            |
+----------------------+
```

Selects the fourth item of a non-empty list.

```racket
> v
(list 1 2 3 4 5 6 7 8 9 'A)
> (fourth v)
4
```

```
+-----------------------+
| [procedure]           |
|                       |
| (length l) → natural? |
| l: list?             |
+-----------------------+
```

Evaluates the number of items on a list.

```racket
> x
(list 2 "hello" #true)
> (length x)
3
```

```
+----------------------+
| [procedure]          |
|                      |
| (list x...) → list? |
| x: any/c            |
+----------------------+
```

Constructs a list of its arguments.

```racket
> (list 1 2 3 4 5 6 7 8 9 0)
(cons 1 (cons 2 (cons 3 (cons 4 (cons 5 (cons 6 (cons 7 (cons 8 (cons 9 (cons 0 '()))))))))))
```

```
+--------------------------------+
| [procedure]                    |
|                                |
| (list* x... l) → (listof any) |
| x: any                        |
| l: (listof any)               |
+--------------------------------+
```

Constructs a list by adding multiple items to a list.
In ASL, list* also deals with cyclic lists.

```
+------------------------+
| [procedure]            |
|                        |
| (list-ref x i) → any/c |
| x: list?              |
| i: natural?           |
+------------------------+
```

Extracts the indexed item from the list.

```racket
> v
(list 1 2 3 4 5 6 7 8 9 'A)
> (list-ref v 9)
'A
```

```
+----------------------+
| [procedure]          |
|                      |
| (list? x) → boolean? |
| x: any/c            |
+----------------------+
```

Checks whether the given value is a list.

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
| [procedure]             |
|                         |
| (make-list i x) → list? |
| i: natural?            |
| x: any/c               |
+-------------------------+
```

Constructs a list of i copies of x.

```racket
> (make-list 3 "hello")
(cons "hello" (cons "hello" (cons "hello" '())))
```

```
+-------------------------+
| [procedure]             |
|                         |
| (member x l) → boolean? |
| x: any/c               |
| l: list?               |
+-------------------------+
```

Determines whether some value is on the list (comparing values with equal?).

```racket
> x
(list 2 "hello" #true)
> (member "hello" x)
#true
```

```
+--------------------------+
| [procedure]              |
|                          |
| (member? x l) → boolean? |
| x: any/c                |
| l: list?                |
+--------------------------+
```

Determines whether some value is on the list (comparing values with equal?).

```racket
> x
(list 2 "hello" #true)
> (member? "hello" x)
#true
```

```
+-----------------------+
| [procedure]           |
|                       |
| (memq x l) → boolean? |
| x: any/c             |
| l: list?             |
+-----------------------+
```

Determines whether some value x is on some list l,
using eq? to compare x with items on l.

```racket
> x
(list 2 "hello" #true)
> (memq (list (list 1 2 3)) x)
#false
```

```
+------------------------+
| [procedure]            |
|                        |
| (memq? x l) → boolean? |
| x: any/c              |
| l: list?              |
+------------------------+
```

Determines whether some value x is on some list l,
using eq? to compare x with items on l.

```racket
> x
(list 2 "hello" #true)
> (memq? (list (list 1 2 3)) x)
#false
```

```
+---------------------------------+
| [procedure]                     |
|                                 |
| (memv x l) → (or/c #false list) |
| x: any/c                       |
| l: list?                       |
+---------------------------------+
```

Determines whether some value is on the list if so, it produces the
suffix of the list that starts with x if not, it produces false. (It
compares values with the eqv? predicate.)

```racket
> x
(list 2 "hello" #true)
> (memv (list (list 1 2 3)) x)
#false
```

```
+----------------------+
| [value]              |
|                      |
| null: list          |
+----------------------+
```

Another name for the empty list

```racket
> null
'()
```

```
+----------------------+
| [procedure]          |
|                      |
| (null? x) → boolean? |
| x: any/c            |
+----------------------+
```

Determines whether some value is the empty list.

```racket
> (null? '())
#true
> (null? 42)
#false
```

```
+--------------------------------+
| [procedure]                    |
|                                |
| (range start end step) → list? |
| start: number                 |
| end: number                   |
| step: number                  |
+--------------------------------+
```

Constructs a list of numbers by stepping from start
to end.

```racket
> (range 0 10 2)
(cons 0 (cons 2 (cons 4 (cons 6 (cons 8 '())))))
```

```
+----------------------+
| [procedure]          |
|                      |
| (remove x l) → list? |
| x: any/c            |
| l: list?            |
+----------------------+
```

Constructs a list like the given one, with the first occurrence of the
given item removed (comparing values with equal?).

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
| [procedure]              |
|                          |
| (remove-all x l) → list? |
| x: any/c                |
| l: list?                |
+--------------------------+
```

Constructs a list like the given one, with all occurrences of the
given item removed (comparing values with equal?).

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
| [procedure]          |
|                      |
| (rest x) → any/c     |
| x: cons?            |
+----------------------+
```

Selects the rest of a non-empty list.

```racket
> x
(list 2 "hello" #true)
> (rest x)
(list "hello" #true)
```

```
+----------------------+
| [procedure]          |
|                      |
| (reverse l) → list   |
| l: list?            |
+----------------------+
```

Creates a reversed version of a list.

```racket
> x
(list 2 "hello" #true)
> (reverse x)
(list #true "hello" 2)
```

```
+----------------------+
| [procedure]          |
|                      |
| (second x) → any/c   |
| x: list?            |
+----------------------+
```

Selects the second item of a non-empty list.

```racket
> x
(list 2 "hello" #true)
> (second x)
"hello"
```

```
+----------------------+
| [procedure]          |
|                      |
| (seventh x) → any/c  |
| x: list?            |
+----------------------+
```

Selects the seventh item of a non-empty list.

```racket
> v
(list 1 2 3 4 5 6 7 8 9 'A)
> (seventh v)
7
```

```
+----------------------+
| [procedure]          |
|                      |
| (sixth x) → any/c    |
| x: list?            |
+----------------------+
```

Selects the sixth item of a non-empty list.

```racket
> v
(list 1 2 3 4 5 6 7 8 9 'A)
> (sixth v)
6
```

```
+----------------------+
| [procedure]          |
|                      |
| (third x) → any/c    |
| x: list?            |
+----------------------+
```

Selects the third item of a non-empty list.

```racket
> x
(list 2 "hello" #true)
> (third x)
#true
```

### 5.11 Posns

```
+------------------------+
| [procedure]            |
|                        |
| (make-posn x y) → posn |
| x: any/c              |
| y: any/c              |
+------------------------+
```

Constructs a posn from two arbitrary values.

```racket
> (make-posn 3 3)
(make-posn 3 3)
> (make-posn "hello" #true)
(make-posn "hello" #true)
```

```
+----------------------+
| [procedure]          |
|                      |
| (posn-x p) → any/c   |
| p: posn             |
+----------------------+
```

Extracts the x component of a posn.

```racket
> p
(make-posn 2 -3)
> (posn-x p)
2
```

```
+----------------------+
| [procedure]          |
|                      |
| (posn-y p) → any/c   |
| p: posn             |
+----------------------+
```

Extracts the y component of a posn.

```racket
> p
(make-posn 2 -3)
> (posn-y p)
-3
```

```
+----------------------+
| [procedure]          |
|                      |
| (posn? x) → boolean? |
| x: any/c            |
+----------------------+
```

Determines if its input is a posn.

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
| [procedure]               |
|                           |
| (set-posn-x! p x) → void? |
| p: posn                  |
| x: any                   |
+---------------------------+
```

Updates the x component of a posn.

```racket
> p
(make-posn 2 -3)
> (set-posn-x! p 678)
> p
(make-posn 678 -3)
```

```
+--------------------------+
| [procedure]              |
|                          |
| (set-posn-y! p x) → void |
| p: posn                 |
| x: any                  |
+--------------------------+
```

Updates the y component of a posn.

```racket
> q
(make-posn "bye" 2)
> (set-posn-y! q 678)
> q
(make-posn "bye" 678)
```

### 5.12 Characters

```
+-----------------------------+
| [procedure]                 |
|                             |
| (char->integer c) → integer |
| c: char                    |
+-----------------------------+
```

Looks up the number that corresponds to the given character in the ASCII table (if any).

```racket
> (char->integer #\a)
97
> (char->integer #\z)
122
```

```
+---------------------------------+
| [procedure]                     |
|                                 |
| (char-alphabetic? c) → boolean? |
| c: char                        |
+---------------------------------+
```

Determines whether a character represents an alphabetic character.

```racket
> (char-alphabetic? #\Q)
#true
```

```
+-----------------------------------+
| [procedure]                       |
|                                   |
| (char-ci<=? c d e...) → boolean? |
| c: char                          |
| d: char                          |
| e: char                          |
+-----------------------------------+
```

Determines whether the characters are ordered in an increasing and case-insensitive manner.

```racket
> (char-ci<=? #\b #\B)
#true
> (char<=? #\b #\B)
#false
```

```
+----------------------------------+
| [procedure]                      |
|                                  |
| (char-ci<? c d e...) → boolean? |
| c: char                         |
| d: char                         |
| e: char                         |
+----------------------------------+
```

Determines whether the characters are ordered in a strictly increasing and case-insensitive manner.

```racket
> (char-ci<? #\B #\c)
#true
> (char<? #\b #\B)
#false
```

```
+----------------------------------+
| [procedure]                      |
|                                  |
| (char-ci=? c d e...) → boolean? |
| c: char                         |
| d: char                         |
| e: char                         |
+----------------------------------+
```

Determines whether two characters are equal in a case-insensitive
manner.

```racket
> (char-ci=? #\b #\B)
#true
```

```
+-----------------------------------+
| [procedure]                       |
|                                   |
| (char-ci>=? c d e...) → boolean? |
| c: char                          |
| d: char                          |
| e: char                          |
+-----------------------------------+
```

Determines whether the characters are sorted in a decreasing and case-insensitive manner.

```racket
> (char-ci>=? #\b #\C)
#false
> (char>=? #\b #\C)
#true
```

```
+----------------------------------+
| [procedure]                      |
|                                  |
| (char-ci>? c d e...) → boolean? |
| c: char                         |
| d: char                         |
| e: char                         |
+----------------------------------+
```

Determines whether the characters are sorted in a strictly decreasing and case-insensitive manner.

```racket
> (char-ci>? #\b #\B)
#false
> (char>? #\b #\B)
#true
```

```
+--------------------------+
| [procedure]              |
|                          |
| (char-downcase c) → char |
| c: char                 |
+--------------------------+
```

Produces the equivalent lower-case character.

```racket
> (char-downcase #\T)
#\t
```

```
+---------------------------------+
| [procedure]                     |
|                                 |
| (char-lower-case? c) → boolean? |
| c: char                        |
+---------------------------------+
```

Determines whether a character is a lower-case character.

```racket
> (char-lower-case? #\T)
#false
```

```
+------------------------------+
| [procedure]                  |
|                              |
| (char-numeric? c) → boolean? |
| c: char                     |
+------------------------------+
```

Determines whether a character represents a digit.

```racket
> (char-numeric? #\9)
#true
```

```
+------------------------+
| [procedure]            |
|                        |
| (char-upcase c) → char |
| c: char               |
+------------------------+
```

Produces the equivalent upper-case character.

```racket
> (char-upcase #\t)
#\T
```

```
+---------------------------------+
| [procedure]                     |
|                                 |
| (char-upper-case? c) → boolean? |
| c: char                        |
+---------------------------------+
```

Determines whether a character is an upper-case character.

```racket
> (char-upper-case? #\T)
#true
```

```
+---------------------------------+
| [procedure]                     |
|                                 |
| (char-whitespace? c) → boolean? |
| c: char                        |
+---------------------------------+
```

Determines whether a character represents space.

```racket
> (char-whitespace? #\tab)
#true
```

```
+--------------------------------+
| [procedure]                    |
|                                |
| (char<=? c d e...) → boolean? |
| c: char                       |
| d: char                       |
| e: char                       |
+--------------------------------+
```

Determines whether the characters are ordered in an increasing manner.

```racket
> (char<=? #\a #\a #\b)
#true
```

```
+-------------------------------+
| [procedure]                   |
|                               |
| (char<? x d e...) → boolean? |
| x: char                      |
| d: char                      |
| e: char                      |
+-------------------------------+
```

Determines whether the characters are ordered in a strictly increasing manner.

```racket
> (char<? #\a #\b #\c)
#true
```

```
+-------------------------------+
| [procedure]                   |
|                               |
| (char=? c d e...) → boolean? |
| c: char                      |
| d: char                      |
| e: char                      |
+-------------------------------+
```

Determines whether the characters are equal.

```racket
> (char=? #\b #\a)
#false
```

```
+--------------------------------+
| [procedure]                    |
|                                |
| (char>=? c d e...) → boolean? |
| c: char                       |
| d: char                       |
| e: char                       |
+--------------------------------+
```

Determines whether the characters are sorted in a decreasing manner.

```racket
> (char>=? #\b #\b #\a)
#true
```

```
+-------------------------------+
| [procedure]                   |
|                               |
| (char>? c d e...) → boolean? |
| c: char                      |
| d: char                      |
| e: char                      |
+-------------------------------+
```

Determines whether the characters are sorted in a strictly decreasing manner.

```racket
> (char>? #\A #\z #\a)
#false
```

```
+----------------------+
| [procedure]          |
|                      |
| (char? x) → boolean? |
| x: any/c            |
+----------------------+
```

Determines whether a value is a character.

```racket
> (char? "a")
#false
> (char? #\a)
#true
```

### 5.13 Strings

```
+-------------------------------+
| [procedure]                   |
|                               |
| (explode s) → (listof string) |
| s: string                    |
+-------------------------------+
```

Translates a string into a list of 1-letter strings.

```racket
> (explode "cat")
(list "c" "a" "t")
```

```
+---------------------------+
| [procedure]               |
|                           |
| (format f x...) → string |
| f: string                |
| x: any/c                 |
+---------------------------+
```

Formats a string, possibly embedding values.

```racket
> (format "Dear Dr. ~a:" "Flatt")
"Dear Dr. Flatt:"
> (format "Dear Dr. ~s:" "Flatt")
"Dear Dr. \"Flatt\":"
```

```
+----------------------+
| [procedure]          |
|                      |
| (implode l) → string |
| l: list?            |
+----------------------+
```

Concatenates the list of 1-letter strings into one string.

```racket
> (implode (cons "c" (cons "a" (cons "t" '()))))
"cat"
```

```
+--------------------------+
| [procedure]              |
|                          |
| (int->string i) → string |
| i: integer              |
+--------------------------+
```

Converts an integer in [0,55295] or [57344 1114111] to a 1-letter string.

```racket
> (int->string 65)
"A"
```

```
+---------------------------+
| [procedure]               |
|                           |
| (list->string l) → string |
| l: list?                 |
+---------------------------+
```

Converts a s list of characters into a string.

```racket
> (list->string (cons #\c (cons #\a (cons #\t '()))))
"cat"
```

```
+----------------------------+
| [procedure]                |
|                            |
| (make-string i c) → string |
| i: natural?               |
| c: char                   |
+----------------------------+
```

Produces a string of length i from c.

```racket
> (make-string 3 #\d)
"ddd"
```

```
+--------------------------+
| [procedure]              |
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
| [procedure]              |
|                          |
| (string c...) → string? |
| c: char                 |
+--------------------------+
```

Builds a string of the given characters.

```racket
> (string #\d #\o #\g)
"dog"
```

```
+---------------------------+
| [procedure]               |
|                           |
| (string->int s) → integer |
| s: string                |
+---------------------------+
```

Converts a 1-letter string to an integer in [0,55295] or [57344, 1114111].

```racket
> (string->int "a")
97
```

```
+----------------------------------+
| [procedure]                      |
|                                  |
| (string->list s) → (listof char) |
| s: string                       |
+----------------------------------+
```

Converts a string into a list of characters.

```racket
> (string->list "hello")
(list #\h #\e #\l #\l #\o)
```

```
+--------------------------------------------+
| [procedure]                                |
|                                            |
| (string->number s) → (union number #false) |
| s: string                                 |
+--------------------------------------------+
```

Converts a string into a number, produce false if impossible.

```racket
> (string->number "-2.03")
-2.03
> (string->number "1-2i")
1-2i
```

```
+-----------------------------+
| [procedure]                 |
|                             |
| (string->symbol s) → symbol |
| s: string                  |
+-----------------------------+
```

Converts a string into a symbol.

```racket
> (string->symbol "hello")
'hello
```

```
+-----------------------------------+
| [procedure]                       |
|                                   |
| (string-alphabetic? s) → boolean? |
| s: string                        |
+-----------------------------------+
```

Determines whether all ’letters’ in the string are alphabetic.

```racket
> (string-alphabetic? "123")
#false
> (string-alphabetic? "cat")
#true
```

```
+--------------------------------------+
| [procedure]                          |
|                                      |
| (string-contains-ci? s t) → boolean? |
| s: string                           |
| t: string                           |
+--------------------------------------+
```

Determines whether the first string appears in the second one without
regard to the case of the letters.

```racket
> (string-contains-ci? "At" "caT")
#true
```

```
+-----------------------------------+
| [procedure]                       |
|                                   |
| (string-contains? s t) → boolean? |
| s: string                        |
| t: string                        |
+-----------------------------------+
```

Determines whether the first string appears literally in the second one.

```racket
> (string-contains? "at" "cat")
#true
```

```
+--------------------------+
| [procedure]              |
|                          |
| (string-copy s) → string |
| s: string               |
+--------------------------+
```

Copies a string.

```racket
> (string-copy "hello")
"hello"
```

```
+------------------------------+
| [procedure]                  |
|                              |
| (string-downcase s) → string |
| s: string                   |
+------------------------------+
```

Produces a string like the given one with all ’letters’ as lower case.

```racket
> (string-downcase "CAT")
"cat"
> (string-downcase "cAt")
"cat"
```

```
+-----------------------------+
| [procedure]                 |
|                             |
| (string-ith s i) → 1string? |
| s: string                  |
| i: natural?                |
+-----------------------------+
```

Extracts the ith 1-letter substring from s.

```racket
> (string-ith "hello world" 1)
"e"
```

```
+-------------------------+
| [procedure]             |
|                         |
| (string-length s) → nat |
| s: string              |
+-------------------------+
```

Determines the length of a string.

```racket
> (string-length "hello world")
11
```

```
+-----------------------------------+
| [procedure]                       |
|                                   |
| (string-lower-case? s) → boolean? |
| s: string                        |
+-----------------------------------+
```

Determines whether all ’letters’ in the string are lower case.

```racket
> (string-lower-case? "CAT")
#false
```

```
+--------------------------------+
| [procedure]                    |
|                                |
| (string-numeric? s) → boolean? |
| s: string                     |
+--------------------------------+
```

Determines whether all ’letters’ in the string are numeric.

```racket
> (string-numeric? "123")
#true
> (string-numeric? "1-2i")
#false
```

```
+-------------------------+
| [procedure]             |
|                         |
| (string-ref s i) → char |
| s: string              |
| i: natural?            |
+-------------------------+
```

Extracts the ith character from s.

```racket
> (string-ref "cat" 2)
#\t
```

```
+----------------------------+
| [procedure]                |
|                            |
| (string-upcase s) → string |
| s: string                 |
+----------------------------+
```

Produces a string like the given one with all ’letters’ as upper case.

```racket
> (string-upcase "cat")
"CAT"
> (string-upcase "cAt")
"CAT"
```

```
+-----------------------------------+
| [procedure]                       |
|                                   |
| (string-upper-case? s) → boolean? |
| s: string                        |
+-----------------------------------+
```

Determines whether all ’letters’ in the string are upper case.

```racket
> (string-upper-case? "CAT")
#true
```

```
+-----------------------------------+
| [procedure]                       |
|                                   |
| (string-whitespace? s) → boolean? |
| s: string                        |
+-----------------------------------+
```

Determines whether all ’letters’ in the string are white space.

```racket
> (string-whitespace? (string-append " " (string #\tab #\newline #\return)))
#true
```

```
+------------------------+
| [procedure]            |
|                        |
| (string? x) → boolean? |
| x: any/c              |
+------------------------+
```

Determines whether a value is a string.

```racket
> (string? "hello world")
#true
> (string? 42)
#false
```

```
+----------------------------+
| [procedure]                |
|                            |
| (substring s i j) → string |
| s: string                 |
| i: natural?               |
| j: natural?               |
+----------------------------+
```

Extracts the substring starting at i up to j (or the
end if j is not provided).

```racket
> (substring "hello world" 1 5)
"ello"
> (substring "hello world" 1 8)
"ello wo"
> (substring "hello world" 4)
"o world"
```

### 5.14 Images

```
+--------------------------+
| [procedure]              |
|                          |
| (image=? i j) → boolean? |
| i: image                |
| j: image                |
+--------------------------+
```

Determines whether two images are equal.

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
| [procedure]           |
|                       |
| (image? x) → boolean? |
| x: any/c             |
+-----------------------+
```

Determines whether a value is an image.

```racket
> c1
[image:pict_14.png]
> (image? c1)
#true
```

### 5.15 Misc

```
+-------------------------+
| [procedure]             |
|                         |
| (=~ x y eps) → boolean? |
| x: number              |
| y: number              |
| eps: non-negative-real |
+-------------------------+
```

Checks
whether x and y are within eps of either other.

```racket
> (=~ 1.01 1.0 0.1)
#true
> (=~ 1.01 1.5 0.1)
#false
```

```
+----------------------------------------+
| [procedure]                            |
|                                        |
| (current-milliseconds) → exact-integer |
+----------------------------------------+
```

Returns the current “time” in fixnum milliseconds (possibly negative).

```racket
> (current-milliseconds)
1779843342996
```

```
+----------------------+
| [value]              |
|                      |
| eof: eof-object?    |
+----------------------+
```

A value that represents the end of a file:

```racket
> eof
#<eof>
```

```
+----------------------------+
| [procedure]                |
|                            |
| (eof-object? x) → boolean? |
| x: any/c                  |
+----------------------------+
```

Determines whether some value is the end-of-file value.

```racket
> (eof-object? eof)
#true
> (eof-object? 42)
#false
```

```
+----------------------+
| [procedure]          |
|                      |
| (eq? x y) → boolean? |
| x: any/c            |
| y: any/c            |
+----------------------+
```

Determines whether two values are equivalent from the computer’s perspective (intensional).

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
| [procedure]             |
|                         |
| (equal? x y) → boolean? |
| x: any/c               |
| y: any/c               |
+-------------------------+
```

Determines whether two values are structurally equal where basic values
are compared with the eqv? predicate.

```racket
> (equal? (make-posn 1 2) (make-posn (- 2 1) (+ 1 1)))
#true
```

```
+----------------------------+
| [procedure]                |
|                            |
| (equal~? x y z) → boolean? |
| x: any/c                  |
| y: any/c                  |
| z: non-negative-real      |
+----------------------------+
```

Compares x and y like equal? but uses =~ in the case of numbers.

```racket
> (equal~? (make-posn 1.01 1.0) (make-posn 1.01 0.99) 0.2)
#true
```

```
+-----------------------+
| [procedure]           |
|                       |
| (eqv? x y) → boolean? |
| x: any/c             |
| y: any/c             |
+-----------------------+
```

Determines whether two values are equivalent from the perspective of all
functions that can be applied to it (extensional).

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
| [procedure]           |
|                       |
| (error x...) → void? |
| x: any/c             |
+-----------------------+
```

Signals an error, combining the given values
into an error message. If any of the values’
printed representations is too long, it is
truncated and “...” is put into the string.
If the first value is a symbol, it is suffixed with a colon and the
result pre-pended on to the error message.

```racket
> zero
0
> (if (= zero 0) (error "can't divide by 0") (/ 1 zero))
can't divide by 0
```

```
+----------------------+
| [procedure]          |
|                      |
| (exit) → void        |
+----------------------+
```

Evaluating (exit) terminates the running program.

```
+----------------------+
| [procedure]          |
|                      |
| (force v) → any      |
| v: any              |
+----------------------+
```

Finds the delayed value; see also delay.

```
+----------------------+
| [procedure]          |
|                      |
| (gensym) → symbol?   |
+----------------------+
```

Generates a new symbol, different from all symbols in the program.

```racket
> (gensym)
'g8579052
```

```
+----------------------+
| [procedure]          |
|                      |
| (identity x) → any/c |
| x: any/c            |
+----------------------+
```

Returns x.

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
| [procedure]             |
|                         |
| (promise? x) → boolean? |
| x: any                 |
+-------------------------+
```

Determines if a value is delayed.

```
+----------------------+
| [procedure]          |
|                      |
| (sleep sec) → void   |
| sec: positive-num   |
+----------------------+
```

Causes the program to sleep for the given number of seconds.

```
+------------------------+
| [procedure]            |
|                        |
| (struct? x) → boolean? |
| x: any/c              |
+------------------------+
```

Determines whether some value is a structure.

```racket
> (struct? (make-posn 1 2))
#true
> (struct? 43)
#false
```

```
+----------------------+
| [procedure]          |
|                      |
| (void) → void?       |
+----------------------+
```

Produces a void value.

```racket
> (void)
```

```
+----------------------+
| [procedure]          |
|                      |
| (void? x) → boolean? |
| x: any              |
+----------------------+
```

Determines if a value is void.

```racket
> (void? (void))
#true
> (void? 42)
#false
```

### 5.16 Signatures

```
+----------------------+
| [value]              |
|                      |
| Any: signature?     |
+----------------------+
```

Signature for any value.

```
+----------------------+
| [value]              |
|                      |
| Boolean: signature? |
+----------------------+
```

Signature for booleans.

```
+----------------------+
| [value]              |
|                      |
| Char: signature?    |
+----------------------+
```

Signature for chararacters.

```
+------------------------------------------+
| [procedure]                              |
|                                          |
| (ConsOf first-sig rest-sig) → signature? |
| first-sig: signature?                   |
| rest-sig: signature?                    |
+------------------------------------------+
```

Signature for a cons pair.

```
+------------------------+
| [value]                |
|                        |
| EmptyList: signature? |
+------------------------+
```

Signature for the empty list.

```
+----------------------+
| [value]              |
|                      |
| False: signature?   |
+----------------------+
```

Signature for just false.

```
+----------------------+
| [value]              |
|                      |
| Integer: signature? |
+----------------------+
```

Signature for integers.

```
+----------------------+
| [value]              |
|                      |
| Natural: signature? |
+----------------------+
```

Signature for natural numbers.

```
+----------------------+
| [value]              |
|                      |
| Number: signature?  |
+----------------------+
```

Signature for arbitrary numbers.

```
+-----------------------+
| [value]               |
|                       |
| Rational: signature? |
+-----------------------+
```

Signature for rational numbers.

```
+----------------------+
| [value]              |
|                      |
| Real: signature?    |
+----------------------+
```

Signature for real numbers.

```
+----------------------+
| [value]              |
|                      |
| String: signature?  |
+----------------------+
```

Signature for strings.

```
+----------------------+
| [value]              |
|                      |
| Symbol: signature?  |
+----------------------+
```

Signature for symbols.

```
+----------------------+
| [value]              |
|                      |
| True: signature?    |
+----------------------+
```

Signature for just true.

### 5.17 Numbers (relaxed conditions)

### 5.18 String (relaxed conditions)

```
+--------------------------------+
| [procedure]                    |
|                                |
| (string-append s...) → string |
| s: string                     |
+--------------------------------+
```

Concatenates the characters of several strings.

```racket
> (string-append "hello" " " "world" " " "good bye")
"hello world good bye"
```

```
+-------------------------------------+
| [procedure]                         |
|                                     |
| (string-ci<=? s t x...) → boolean? |
| s: string                          |
| t: string                          |
| x: string                          |
+-------------------------------------+
```

Determines whether the strings are ordered in a lexicographically
increasing and case-insensitive manner.

```racket
> (string-ci<=? "hello" "WORLD" "zoo")
#true
```

```
+------------------------------------+
| [procedure]                        |
|                                    |
| (string-ci<? s t x...) → boolean? |
| s: string                         |
| t: string                         |
| x: string                         |
+------------------------------------+
```

Determines whether the strings are ordered in a lexicographically
strictly increasing and case-insensitive manner.

```racket
> (string-ci<? "hello" "WORLD" "zoo")
#true
```

```
+------------------------------------+
| [procedure]                        |
|                                    |
| (string-ci=? s t x...) → boolean? |
| s: string                         |
| t: string                         |
| x: string                         |
+------------------------------------+
```

Determines whether all strings are equal, character for character, regardless of case.

```racket
> (string-ci=?  "hello" "HellO")
#true
```

```
+-------------------------------------+
| [procedure]                         |
|                                     |
| (string-ci>=? s t x...) → boolean? |
| s: string                          |
| t: string                          |
| x: string                          |
+-------------------------------------+
```

Determines whether the strings are ordered in a lexicographically
decreasing and case-insensitive manner.

```racket
> (string-ci>?  "zoo" "WORLD" "hello")
#true
```

```
+------------------------------------+
| [procedure]                        |
|                                    |
| (string-ci>? s t x...) → boolean? |
| s: string                         |
| t: string                         |
| x: string                         |
+------------------------------------+
```

Determines whether the strings are ordered in a lexicographically
strictly decreasing and case-insensitive manner.

```racket
> (string-ci>?  "zoo" "WORLD" "hello")
#true
```

```
+----------------------------------+
| [procedure]                      |
|                                  |
| (string<=? s t x...) → boolean? |
| s: string                       |
| t: string                       |
| x: string                       |
+----------------------------------+
```

Determines whether the strings are ordered in a lexicographically increasing manner.

```racket
> (string<=? "hello" "hello" "world" "zoo")
#true
```

```
+---------------------------------+
| [procedure]                     |
|                                 |
| (string<? s t x...) → boolean? |
| s: string                      |
| t: string                      |
| x: string                      |
+---------------------------------+
```

Determines whether the strings are ordered in a lexicographically strictly increasing manner.

```racket
> (string<? "hello" "world" "zoo")
#true
```

```
+---------------------------------+
| [procedure]                     |
|                                 |
| (string=? s t x...) → boolean? |
| s: string                      |
| t: string                      |
| x: string                      |
+---------------------------------+
```

Determines whether all strings are equal, character for character.

```racket
> (string=? "hello" "world")
#false
> (string=? "bye" "bye")
#true
```

```
+----------------------------------+
| [procedure]                      |
|                                  |
| (string>=? s t x...) → boolean? |
| s: string                       |
| t: string                       |
| x: string                       |
+----------------------------------+
```

Determines whether the strings are ordered in a lexicographically decreasing manner.

```racket
> (string>=?  "zoo" "zoo" "world" "hello")
#true
```

```
+---------------------------------+
| [procedure]                     |
|                                 |
| (string>? s t x...) → boolean? |
| s: string                      |
| t: string                      |
| x: string                      |
+---------------------------------+
```

Determines whether the strings are ordered in a lexicographically strictly decreasing manner.

```racket
> (string>?  "zoo" "world" "hello")
#true
```

### 5.19 Posn

```
+----------------------+
| [procedure]          |
|                      |
| (posn) → signature   |
+----------------------+
```

Signature for posns.

### 5.20 Higher-Order Functions

### 5.21 Numbers (relaxed conditions plus)

```
+----------------------+
| [procedure]          |
|                      |
| (* x...) → number   |
| x: number           |
+----------------------+
```

Multiplies all given numbers.
In ISL and up: * works when applied to only one number or none.

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
| [procedure]          |
|                      |
| (+ x...) → number   |
| x: number           |
+----------------------+
```

Adds all given numbers.
In ISL and up: + works when applied to only one number or none.

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
| [procedure]          |
|                      |
| (/ x y...) → number |
| x: number           |
| y: number           |
+----------------------+
```

Divides the first by all remaining numbers.
In ISL and up: / computes the inverse when applied to one number.

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
| [procedure]          |
|                      |
| (= x...) → number   |
| x: number           |
+----------------------+
```

Compares numbers for equality.
In ISL and up: = works when applied to only one number.

```racket
> (= 10 10)
#true
> (= 11)
#true
> (= 0)
#true
```

### 5.22 Higher-Order Functions (with Lambda)

```
+---------------------------+
| [procedure]               |
|                           |
| (andmap p? [l]) → boolean |
| p?: (X... -> boolean)   |
| l: (listof X) =...      |
+---------------------------+
```

Determines whether p? holds for all items of l...:

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
| [procedure]              |
|                          |
| (apply f x-1... l) → Y  |
| f: (X-1... X-N -> Y)   |
| x-1: X-1                |
| l: (list X-i+1... X-N) |
+--------------------------+
```

Applies a function using items from a list as the arguments:

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
| [procedure]          |
|                      |
| (argmax f l) → X     |
| f: (X -> real)      |
| l: (listof X)       |
+----------------------+
```

Finds the (first) element of the list that maximizes the output of the function.

```racket
> (argmax second '((sam 98) (carl 78) (vincent 93) (asumu 99)))
(list 'asumu 99)
```

```
+----------------------+
| [procedure]          |
|                      |
| (argmin f l) → X     |
| f: (X -> real)      |
| l: (listof X)       |
+----------------------+
```

Finds the (first) element of the list that minimizes the output of the function.

```racket
> (argmin second '((sam 98) (carl 78) (vincent 93) (asumu 99)))
(list 'carl 78)
```

```
+-------------------------------+
| [procedure]                   |
|                               |
| (build-list n f) → (listof X) |
| n: nat                       |
| f: (nat -> X)                |
+-------------------------------+
```

Constructs a list by applying f to the numbers between 0 and (-n1):

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
| [procedure]                 |
|                             |
| (build-string n f) → string |
| n: nat                     |
| f: (nat -> char)           |
+-----------------------------+
```

Constructs a string by applying f to the numbers between 0 and
(-n1):

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
| [procedure]              |
|                          |
| (compose f g) → (X -> Z) |
| f: (Y -> Z)             |
| g: (X -> Y)             |
+--------------------------+
```

Composes a sequence of procedures into a single procedure:

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
| [procedure]                |
|                            |
| (filter p? l) → (listof X) |
| p?: (X -> boolean)        |
| l: (listof X)             |
+----------------------------+
```

Constructs a list from all those items on a list for which the predicate holds.

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
| [procedure]              |
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
| [procedure]              |
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
| [procedure]                |
|                            |
| (map f l...) → (listof Z) |
| f: (X... -> Z)           |
| l: (listof X)             |
+----------------------------+
```

Constructs a new list by applying a function to each item on one or
more existing lists:

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
| [procedure]                             |
|                                         |
| (memf p? l) → (union #false (listof X)) |
| p?: (X -> any)                         |
| l: (listof X)                          |
+-----------------------------------------+
```

Produces #false if p? produces false for all
items on l. If p? produces #true for any of
the items on l, memf returns the sub-list starting
from that item.

```racket
> (memf odd? '(2 4 6 3 8 0))
(list 3 8 0)
```

```
+------------------------+
| [procedure]            |
|                        |
| (ormap p? l) → boolean |
| p?: (X -> boolean)    |
| l: (listof X)         |
+------------------------+
```

Determines whether p? holds for at least one items of l:

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
| [procedure]               |
|                           |
| (procedure? x) → boolean? |
| x: any                   |
+---------------------------+
```

Produces true if the value is a procedure.

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
| [procedure]                     |
|                                 |
| (quicksort l comp) → (listof X) |
| l: (listof X)                  |
| comp: (X X -> boolean)         |
+---------------------------------+
```

Sorts the items on l, in an order according to comp (using the quicksort
algorithm).

```racket
> (quicksort '(6 7 2 1 3 4 0 5 9 8) <)
(list 0 1 2 3 4 5 6 7 8 9)
```

```
+----------------------------+
| [procedure]                |
|                            |
| (sort l comp) → (listof X) |
| l: (listof X)             |
| comp: (X X -> boolean)    |
+----------------------------+
```

Sorts the items on l, in an order according to comp.

```racket
> (sort '(6 7 2 1 3 4 0 5 9 8) <)
(list 0 1 2 3 4 5 6 7 8 9)
```

### 5.23 Reading and Printing

```
+----------------------+
| [procedure]          |
|                      |
| (display x) → void   |
| x: any              |
+----------------------+
```

Prints the argument to stdout (without quotes on symbols and strings, etc.).

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
| [procedure]          |
|                      |
| (newline) → void     |
+----------------------+
```

Prints a newline.

```
+-------------------------+
| [procedure]             |
|                         |
| (pretty-print x) → void |
| x: any                 |
+-------------------------+
```

Pretty prints S-expressions (like write).

```racket
> (pretty-print '((1 2 3) ((a) ("hello world" #true) (((false "good bye"))))))
((1 2 3) ((a) ("hello world" #true) (((false "good bye")))))
> (pretty-print (build-list 10 (lambda (i) (build-list 10 (lambda (j) (= i j))))))
((#true #false #false #false #false #false #false #false #false #false) (#false #true #false #false #false #false #false #false #false #false) (#false #false #true #false #false #false #false #false #false #false) (#false #false #false #true #false #false #false #false #false #false) (#false #false #false #false #true #false #false #false #false #false) (#false #false #false #false #false #true #false #false #false #false) (#false #false #false #false #false #false #true #false #false #false) (#false #false #false #false #false #false #false #true #false #false) (#false #false #false #false #false #false #false #false #true #false) (#false #false #false #false #false #false #false #false #false #true))
```

```
+----------------------+
| [procedure]          |
|                      |
| (print x) → void     |
| x: any              |
+----------------------+
```

Prints the argument as a value.

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
| [procedure]             |
|                         |
| (printf f x...) → void |
| f: string              |
| x: any                 |
+-------------------------+
```

Formats the rest of the arguments according to the first argument and print it.

```
+----------------------+
| [procedure]          |
|                      |
| (read) → sexp        |
+----------------------+
```

Reads input from the user.

```
+----------------------------------+
| [procedure]                      |
|                                  |
| (with-input-from-file f p) → any |
| f: string                       |
| p: (-> any)                     |
+----------------------------------+
```

Opens the named input file f and allows p to read from it.

```
+------------------------------------+
| [procedure]                        |
|                                    |
| (with-input-from-string s p) → any |
| s: string                         |
| p: (-> any)                       |
+------------------------------------+
```

Turns s into input for read operations in p.

```racket
> (with-input-from-string "hello" read)
'hello
> (string-length (symbol->string (with-input-from-string "hello" read)))
5
```

```
+---------------------------------+
| [procedure]                     |
|                                 |
| (with-output-to-file f p) → any |
| f: string                      |
| p: (-> any)                    |
+---------------------------------+
```

Opens the named output file f and allows p to write to it.

```
+---------------------------------+
| [procedure]                     |
|                                 |
| (with-output-to-string p) → any |
| p: (-> any)                    |
+---------------------------------+
```

Produces a string from all write/display/print operations in p.

```racket
> (with-output-to-string (lambda () (display 10)))
"10"
```

```
+----------------------+
| [procedure]          |
|                      |
| (write x) → void     |
| x: any              |
+----------------------+
```

Prints the argument to stdout (in a traditional style that is somewhere
between print and display).

```racket
> (write 10)
10
> (write "hello")
"hello"
> (write 'hello)
hello
```

### 5.24 Vectors

```
+-----------------------------------+
| [procedure]                       |
|                                   |
| (build-vector n f) → (vectorof X) |
| n: nat                           |
| f: (nat -> X)                    |
+-----------------------------------+
```

Constructs a vector by applying f to the numbers 0 through
(-n1).

```racket
> (build-vector 5 add1)
(vector 1 2 3 4 5)
```

```
+---------------------------------+
| [procedure]                     |
|                                 |
| (list->vector l) → (vectorof X) |
| l: (listof X)                  |
+---------------------------------+
```

Transforms l into a vector.

```racket
> (list->vector (list "hello" "world" "good" "bye"))
(vector "hello" "world" "good" "bye")
```

```
+----------------------------------+
| [procedure]                      |
|                                  |
| (make-vector n x) → (vectorof X) |
| n: number                       |
| x: X                            |
+----------------------------------+
```

Constructs a vector of n copies of x.

```racket
> (make-vector 5 0)
(vector 0 0 0 0 0)
```

```
+---------------------------------+
| [procedure]                     |
|                                 |
| (vector x...) → (vector X...) |
| x: X                           |
+---------------------------------+
```

Constructs a vector from the given values.

```racket
> (vector 1 2 3 -1 -2 -3)
(vector 1 2 3 -1 -2 -3)
```

```
+-------------------------------+
| [procedure]                   |
|                               |
| (vector->list v) → (listof X) |
| v: (vectorof X)              |
+-------------------------------+
```

Transforms v into a list.

```racket
> (vector->list (vector 'a 'b 'c))
(list 'a 'b 'c)
```

```
+-------------------------+
| [procedure]             |
|                         |
| (vector-length v) → nat |
| v: (vector X)          |
+-------------------------+
```

Determines the length of v.

```racket
> v
(vector "a" "b" "c" "d" "e")
> (vector-length v)
5
```

```
+----------------------+
| [procedure]          |
|                      |
| (vector-ref v n) → X |
| v: (vector X)       |
| n: nat              |
+----------------------+
```

Extracts the nth element from v.

```racket
> v
(vector "a" "b" "c" "d" "e")
> (vector-ref v 3)
"d"
```

```
+----------------------------+
| [procedure]                |
|                            |
| (vector-set! v n x) → void |
| v: (vectorof X)           |
| n: nat                    |
| x: X                      |
+----------------------------+
```

Updates v at position n to be x.

```racket
> v
(vector "a" "b" "c" "d" "e")
> (vector-set! v 3 77)
> v
(vector "a" "b" "c" 77 "e")
```

```
+-----------------------+
| [procedure]           |
|                       |
| (vector? x) → boolean |
| x: any               |
+-----------------------+
```

Determines if a value is a vector.

```racket
> v
(vector "a" "b" "c" 77 "e")
> (vector? v)
#true
> (vector? 42)
#false
```

### 5.25 Boxes

```
+----------------------+
| [procedure]          |
|                      |
| (box x) → box?       |
| x: any/c            |
+----------------------+
```

Constructs a box.

```racket
> (box 42)
(box 42)
```

```
+----------------------+
| [procedure]          |
|                      |
| (box? x) → boolean?  |
| x: any/c            |
+----------------------+
```

Determines if a value is a box.

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
| [procedure]           |
|                       |
| (set-box! b x) → void |
| b: box?              |
| x: any/c             |
+-----------------------+
```

Updates a box.

```racket
> b
(box 33)
> (set-box! b 31)
> b
(box 31)
```

```
+----------------------+
| [procedure]          |
|                      |
| (unbox b) → any      |
| b: box?             |
+----------------------+
```

Extracts the boxed value.

```racket
> b
(box 31)
> (unbox b)
31
```

### 5.26 Hash Tables

```
+----------------------+
| [procedure]          |
|                      |
| (hash-copy h) → hash |
| h: hash             |
+----------------------+
```

Copies a hash table.

```
+--------------------------+
| [procedure]              |
|                          |
| (hash-count h) → integer |
| h: hash                 |
+--------------------------+
```

Determines the number of keys mapped by a hash table.

```racket
> ish
(make-immutable-hash (list (list 'b 69) (list 'r 999) (list 'c 42) (list 'e 61)))
> (hash-count ish)
4
```

```
+------------------------+
| [procedure]            |
|                        |
| (hash-eq? h) → boolean |
| h: hash               |
+------------------------+
```

Determines if a hash table uses eq? for comparisons.

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
| [procedure]               |
|                           |
| (hash-equal? h) → boolean |
| h: hash?                 |
+---------------------------+
```

Determines if a hash table uses equal? for comparisons.

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
| [procedure]             |
|                         |
| (hash-eqv? h) → boolean |
| h: hash                |
+-------------------------+
```

Determines if a hash table uses eqv? for comparisons.

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
| [procedure]                 |
|                             |
| (hash-for-each h f) → void? |
| h: (hash X Y)              |
| f: (X Y -> any)            |
+-----------------------------+
```

Applies a function to each mapping of a hash table for effect only.

```racket
> hsh
(make-hash (list (list 'c 42) (list 'r 999) (list 'b 69) (list 'e 61)))
> (hash-for-each hsh (lambda (ky vl) (hash-set! hsh ky (+ vl 1))))
> hsh
(make-hash (list (list 'c 43) (list 'r 1000) (list 'b 70) (list 'e 62)))
```

```
+-------------------------------+
| [procedure]                   |
|                               |
| (hash-has-key? h x) → boolean |
| h: (hash X Y)                |
| x: X                         |
+-------------------------------+
```

Determines if a key is associated with a value in a hash table.

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
| [procedure]                 |
|                             |
| (hash-map h f) → (listof Z) |
| h: (hash X Y)              |
| f: (X Y -> Z)              |
+-----------------------------+
```

Constructs a new list by applying a function to each mapping of a hash
table.

```racket
> ish
(make-immutable-hash (list (list 'b 69) (list 'r 999) (list 'c 42) (list 'e 61)))
> (hash-map ish list)
(list (list 'b 69) (list 'r 999) (list 'c 42) (list 'e 61))
```

```
+----------------------+
| [procedure]          |
|                      |
| (hash-ref h k) → Y   |
| h: (hash X Y)       |
| k: X                |
+----------------------+
```

Extracts the value associated with a key from a hash table; the three
argument case allows a default value or default value computation.

```racket
> hsh
(make-hash (list (list 'c 43) (list 'r 1000) (list 'b 70) (list 'e 62)))
> (hash-ref hsh 'b)
70
```

```
+-----------------------+
| [procedure]           |
|                       |
| (hash-ref! h k v) → Y |
| h: (hash X Y)        |
| k: X                 |
| v: Y                 |
+-----------------------+
```

Extracts the value associated with a key from a mutable hash table; if
the key does not have an mapping, the third argument is used as the
value (or used to compute the value) and is added to the hash table
associated with the key.

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
| [procedure]                    |
|                                |
| (hash-remove h k) → (hash X Y) |
| h: (hash X Y)                 |
| k: X                          |
+--------------------------------+
```

Constructs an immutable hash table with one less mapping than an
existing immutable hash table.

```racket
> ish
(make-immutable-hash (list (list 'b 69) (list 'r 999) (list 'c 42) (list 'e 61)))
> (hash-remove ish 'b)
(make-immutable-hash (list (list 'c 42) (list 'r 999) (list 'e 61)))
```

```
+---------------------------+
| [procedure]               |
|                           |
| (hash-remove! h x) → void |
| h: (hash X Y)            |
| x: X                     |
+---------------------------+
```

Removes an mapping from a mutable hash table.

```racket
> hsh
(make-hash (list (list 'c 43) (list 'd 99) (list 'r 1000) (list 'b 70) (list 'e 62)))
> (hash-remove! hsh 'r)
> hsh
(make-hash (list (list 'c 43) (list 'd 99) (list 'b 70) (list 'e 62)))
```

```
+-------------------------------+
| [procedure]                   |
|                               |
| (hash-set h k v) → (hash X Y) |
| h: (hash X Y)                |
| k: X                         |
| v: Y                         |
+-------------------------------+
```

Constructs an immutable hash table with one new mapping from an
existing immutable hash table.

```racket
> (hash-set ish 'a 23)
(make-immutable-hash (list (list 'b 69) (list 'r 999) (list 'c 42) (list 'a 23) (list 'e 61)))
```

```
+---------------------------+
| [procedure]               |
|                           |
| (hash-set! h k v) → void? |
| h: (hash X Y)            |
| k: X                     |
| v: Y                     |
+---------------------------+
```

Updates a mutable hash table with a new mapping.

```racket
> hsh
(make-hash (list (list 'c 43) (list 'd 99) (list 'b 70) (list 'e 62)))
> (hash-set! hsh 'a 23)
> hsh
(make-hash (list (list 'c 43) (list 'a 23) (list 'd 99) (list 'b 70) (list 'e 62)))
```

```
+----------------------------------+
| [procedure]                      |
|                                  |
| (hash-update h k f) → (hash X Y) |
| h: (hash X Y)                   |
| k: X                            |
| f: (Y -> Y)                     |
+----------------------------------+
```

Composes hash-ref and hash-set to update an existing mapping; the third
argument is used to compute the new mapping value; the fourth
argument is used as the third argument to hash-ref.

```racket
> (hash-update ish 'b (lambda (old-b) (+ old-b 1)))
(make-immutable-hash (list (list 'b 70) (list 'r 999) (list 'c 42) (list 'e 61)))
```

```
+------------------------------+
| [procedure]                  |
|                              |
| (hash-update! h k f) → void? |
| h: (hash X Y)               |
| k: X                        |
| f: (Y -> Y)                 |
+------------------------------+
```

Composes hash-ref and hash-set! to update an existing mapping; the
third argument is used to compute the new mapping value; the fourth
argument is used as the third argument to hash-ref.

```racket
> hsh
(make-hash (list (list 'c 43) (list 'a 23) (list 'd 99) (list 'b 70) (list 'e 62)))
> (hash-update! hsh 'b (lambda (old-b) (+ old-b 1)))
> hsh
(make-hash (list (list 'c 43) (list 'a 23) (list 'd 99) (list 'b 71) (list 'e 62)))
```

```
+----------------------+
| [procedure]          |
|                      |
| (hash? x) → boolean  |
| x: any              |
+----------------------+
```

Determines if a value is a hash table.

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
| [procedure]              |
|                          |
| (make-hash) → (hash X Y) |
+--------------------------+
```

Constructs a mutable hash table from an optional list of mappings that
uses equal? for comparisons.

```racket
> (make-hash)
(make-hash)
> (make-hash '((b 69) (e 61) (i 999)))
(make-hash (list (list 'i 999) (list 'b 69) (list 'e 61)))
```

```
+----------------------------+
| [procedure]                |
|                            |
| (make-hasheq) → (hash X Y) |
+----------------------------+
```

Constructs a mutable hash table from an optional list of mappings that
uses eq? for comparisons.

```racket
> (make-hasheq)
(make-hasheq)
> (make-hasheq '((b 69) (e 61) (i 999)))
(make-hasheq (list (list 'i 999) (list 'b 69) (list 'e 61)))
```

```
+-----------------------------+
| [procedure]                 |
|                             |
| (make-hasheqv) → (hash X Y) |
+-----------------------------+
```

Constructs a mutable hash table from an optional list of mappings that
uses eqv? for comparisons.

```racket
> (make-hasheqv)
(make-hasheqv)
> (make-hasheqv '((b 69) (e 61) (i 999)))
(make-hasheqv (list (list 'i 999) (list 'b 69) (list 'e 61)))
```

```
+------------------------------------+
| [procedure]                        |
|                                    |
| (make-immutable-hash) → (hash X Y) |
+------------------------------------+
```

Constructs an immutable hash table from an optional list of mappings
that uses equal? for comparisons.

```racket
> (make-immutable-hash)
(make-immutable-hash)
> (make-immutable-hash '((b 69) (e 61) (i 999)))
(make-immutable-hash (list (list 'b 69) (list 'e 61) (list 'i 999)))
```

```
+--------------------------------------+
| [procedure]                          |
|                                      |
| (make-immutable-hasheq) → (hash X Y) |
+--------------------------------------+
```

Constructs an immutable hash table from an optional list of mappings
that uses eq? for comparisons.

```racket
> (make-immutable-hasheq)
(make-immutable-hasheq)
> (make-immutable-hasheq '((b 69) (e 61) (i 999)))
(make-immutable-hasheq (list (list 'b 69) (list 'e 61) (list 'i 999)))
```

```
+---------------------------------------+
| [procedure]                           |
|                                       |
| (make-immutable-hasheqv) → (hash X Y) |
+---------------------------------------+
```

Constructs an immutable hash table from an optional list of mappings
that uses eqv? for comparisons.

```racket
> (make-immutable-hasheqv)
(make-immutable-hasheqv)
> (make-immutable-hasheqv '((b 69) (e 61) (i 999)))
(make-immutable-hasheqv (list (list 'b 69) (list 'e 61) (list 'i 999)))
```
