# 付録 C: Racket 早見表（Cheat Sheet）

**原題:** Racket Cheat Sheet  
**著者:** Jay McCarthy  
**原本:** `extracted/appendix/racket-cheat/original_markdown_00_index.md`

```
+-----------+--------------------------------------------------+
| サイト    | main ⏎ download ⏎ docs ⏎ git                     |
+-----------+--------------------------------------------------+
| コミュニティ | packages ⏎ Discourse ⏎ Discord ⏎ more...      |
| 実行      | Put #lang racket "Hello, world!" in `hello.rkt`  |
|           | and run with `racket hello.rkt`                  |
+-----------+--------------------------------------------------+
```

## 数値（Numbers）

```
+---------------+--------------------------------------------------+
| リテラル      | integer 1  rational 1/2  complex 1+2i            |
|               | floating 3.14  extflonum 3.14t0                  |
+---------------+--------------------------------------------------+
| 算術          | + - * / quotient remainder modulo add1 sub1      |
|               | max min round floor ceiling sqrt expt            |
| 比較          | = < <= > >=                                      |
| ビット演算    | bitwise-ior bitwise-and bitwise-xor bitwise-not  |
|               | arithmetic-shift                                 |
| 書式          | number->string string->number                    |
|               | real->decimal-string                             |
| 述語          | number? complex? ... exact-nonnegative-integer?  |
| その他        | random                                           |
| マッチパターン | (? number? n)  42                                |
+---------------+--------------------------------------------------+
```

## 文字列（Strings）

```
+---------------+--------------------------------------------------+
| リテラル      | "Racket"  quoting "a \" approaches!"             |
|               | unicode "λx.x"                                   |
+---------------+--------------------------------------------------+
| 生成          | make-string string string-append build-string    |
|               | string-join                                      |
| 観察          | string-length string-ref substring string-split  |
|               | in-string                                        |
| 変更          | string-downcase string-upcase string-trim        |
| 述語          | string? string=? string<=? string-ci<=?          |
| 正規表現      | #rx"a|b"  #rx"^c(a|d)+r$"                        |
|               | regexp-quote regexp-match regexp-replace         |
| マッチパターン | (? string? s)  "Banana?"                         |
+---------------+--------------------------------------------------+
```

## バイト列（Bytes）

```
+---------------+--------------------------------------------------+
| リテラル      | #"rawbytes\0"                                    |
+---------------+--------------------------------------------------+
| 生成          | make-bytes bytes                                 |
| 数値変換      | integer->integer-bytes                           |
|               | real->floating-point-bytes                       |
| 観察          | bytes-length bytes-ref subbytes in-bytes         |
| 変更          | bytes-set! bytes-copy! bytes-fill!               |
| 変換          | bytes->string/utf-8 ⏎ string->bytes/utf-8        |
| 述語          | bytes? bytes=?                                   |
| マッチパターン | (? bytes? b)  #"0xDEADBEEF"                      |
+---------------+--------------------------------------------------+
```

## その他の基本型（Other）

```
+------------+--------------------------------------------------+
| 真偽値     | #t  #f  not  equal?                              |
+------------+--------------------------------------------------+
| 文字       | #\a  #\tab  #\λ  char?  char->integer            |
|            | integer->char  char<? ...                        |
| シンボル   | 'Racket  symbol?  eq?  string->symbol  gensym    |
| ボックス   | box?  box  unbox  set-box!  box-cas!             |
| 手続き     | procedure?  apply  compose  compose1             |
|            | keyword-apply  procedure-rename                  |
| Void       | void?  void                                      |
| 未定義     | undefined                                        |
+------------+--------------------------------------------------+
```

## リスト（Lists）

```
+---------------+--------------------------------------------------+
| 生成          | empty  list  list*  build-list  for/list         |
+---------------+--------------------------------------------------+
| 観察          | empty?  list?  pair?  length  list-ref  member   |
|               | count  argmin  argmax  in-list                   |
| 利用          | append  reverse  map  andmap  ormap  foldr       |
|               | in-list                                          |
| 変更系        | filter  remove ...  sort  take  drop  split-at   |
|               | partition  remq ...                              |
| マッチパターン | (list a b c)  (list* a b more)                   |
|               | (list top more ...)                              |
+---------------+--------------------------------------------------+
```

## 不変ハッシュ（Immutable Hash）

```
+---------+--------------------------------------------------+
| 生成    | hash  hasheq                                     |
+---------+--------------------------------------------------+
| 観察    | hash?  hash-ref  hash-has-key?  hash-count       |
|         | in-hash  in-hash-keys  in-hash-values            |
| 変更    | hash-set  hash-update  hash-remove               |
+---------+--------------------------------------------------+
```

## ベクタ（Vector）

```
+---------------+------------------------------------------------+
| 生成          | build-vector  vector  make-vector  list->vector |
+---------------+------------------------------------------------+
| 観察          | vector?  vector-length  vector-ref  in-vector  |
| 変更          | vector-set!  vector-fill!  vector-copy!        |
|               | vector-map!                                    |
| マッチパターン | (vector x y z)  (vector x y calabi–yau ...)   |
+---------------+------------------------------------------------+
```

## ストリーム（Streams）

```
+---------+-----------------------------------------------+
| 生成    | stream  stream*  empty-stream                 |
+---------+-----------------------------------------------+
| 観察    | stream-empty?  stream-first  stream-rest      |
|         | in-stream                                     |
+---------+-----------------------------------------------+
```

## 可変ハッシュ（Mutable Hash）

```
+---------+--------------------------------------------------+
| 生成    | make-hash  make-hasheq                           |
+---------+--------------------------------------------------+
| 観察    | hash?  hash-ref  hash-has-key?  hash-count       |
|         | in-hash  in-hash-keys                            |
| 変更    | hash-set!  hash-ref!  hash-update!  hash-remove! |
+---------+--------------------------------------------------+
```

## 入出力（Input/Output）

```
+-----------------+--------------------------------------------------+
| 書式化          | ~a  ~v  ~s  ~e  ~r  pretty-format                |
+-----------------+--------------------------------------------------+
| 入力            | read  read-bytes  peek-byte                      |
| 出力            | write  write-bytes  display  displayln           |
|                 | pretty-print                                     |
| ポートとファイル | with-input-from-file  with-output-to-file       |
|                 | flush-output  open-input-file  open-output-file  |
+-----------------+--------------------------------------------------+
```

## ファイル（Files）

```
+-------+--------------------------------------------------+
| パス  | build-path  bytes->path  path->bytes             |
|       | path-replace-suffix  path-add-suffix             |
+-------+--------------------------------------------------+
| ファイル | file-exists?  rename-file-or-directory        |
|       | copy-directory/files  delete-file  make-directory |
+-------+--------------------------------------------------+
```

## 雑多（Miscellaneous）

```
+----------------------+--------------------------------------------------+
| 時刻                 | current-seconds  current-inexact-milliseconds    |
|                      | date*  date->string                              |
+----------------------+--------------------------------------------------+
| コマンドライン解析   | command-line                                     |
| FFI                  | ffi-lib  _uint32 ...  _fun  malloc  free         |
+----------------------+--------------------------------------------------+
```

## ネットワーク（Networking）

```
+-----------+--------------------------------------------------+
| TCP       | tcp-listen  tcp-connect  tcp-accept  tcp-close   |
+-----------+--------------------------------------------------+
| HTTP      | http-conn  http-conn-open!  http-conn-send!      |
|           | http-conn-recv!                                  |
| URL       | string->url  url->string  url-query              |
| メール    | smtp-send-message  imap-connect ...              |
| JSON      | write-json  read-json                            |
| XML       | read-xml  write-xml  write-xexpr                 |
| データベース | postgresql-connect  mysql-connect             |
|           | sqlite3-connect  query-exec  query-rows          |
+-----------+--------------------------------------------------+
```

## セキュリティ（Security）

```
+------------+--------------------------------------------------+
| カストディアン | make-custodian  custodian-shutdown-all        |
|            | current-custodian                                |
+------------+--------------------------------------------------+
| サンドボックス | make-evaluator  make-module-evaluator        |
+------------+--------------------------------------------------+
```

## 並行性（Concurrency）

```
+----------------+--------------------------------------------------+
| スレッド       | thread  kill-thread  thread-wait                 |
|                | make-thread-group                                |
+----------------+--------------------------------------------------+
| イベント       | sync  choice-evt  wrap-evt  handle-evt           |
|                | alarm-evt ...                                    |
| チャネル       | make-channel  channel-get  channel-put           |
| セマフォ       | make-semaphore  semaphore-post  semaphore-wait   |
| 非同期チャネル | make-async-channel  async-channel-get            |
|                | async-channel-put                                |
+----------------+--------------------------------------------------+
```

## 並列性（Parallelism）

```
+-----------+--------------------------------------------------+
| Futures   | future  touch  processor-count  make-fsemaphore… |
+-----------+--------------------------------------------------+
| Places    | dynamic-place  place  place-wait  place-channel  |
|           | place-channel-get  place-channel-put             |
| プロセス  | subprocess  system*                              |
+-----------+--------------------------------------------------+
```

## 基本構文（Basics）

```
+------------------------+--------------------------------------------------+
| モジュール             | (module+ main body ...) ⏎                        |
|                        | (module+ test body ...)                          |
+------------------------+--------------------------------------------------+
| S式                    | quote  '(a b c)                                  |
|                        | quasiquote unquote  `(1 2 ,(+ 1 2))              |
| 手続き適用             | (fn arg1 arg2) ⏎                                 |
|                        | keyword args  (fn arg1 #:key arg2)               |
| 手続き                 | (lambda (x) x)  (λ (x) x) ⏎                      |
|                        | (λ (x [opt 1]) (+ x opt))                        |
|                        | (λ (x #:key [key 1]) (+ x key))                  |
| 束縛                   | (let ([x 1] [y 2]) (+ x y)) ⏎                    |
|                        | (let* ([x 1] [x (+ x 1)]) x)                     |
| 条件                   | (if (zero? x) 0 (/ 1 x)) ⏎                       |
|                        | (cond [(even? x) 0] [else 1])                    |
| 定義                   | (define x 1) ⏎  (define (f y) (+ x y))           |
| 反復                   | for  for/list  for*                              |
| ブロック               | begin  when  unless                              |
| require 副形式         | prefix-in  only-in  except-in  rename-in         |
|                        | for-syntax  for-template                         |
| provide 副形式         | all-defined-out  all-from-out  rename-out ...    |
|                        | contract-out                                     |
+------------------------+--------------------------------------------------+
```

## 構造体（Structures）

```
+---------------+--------------------------------------------------+
| 定義          | (struct dillo (weight color))                    |
+---------------+--------------------------------------------------+
| 生成          | (define danny (dillo 17.5 'purple))              |
| 観察          | (dillo? danny)  (dillo-weight danny)             |
|               | (dillo-color danny)                              |
| 変更          | (struct-copy dillo danny ([weight 18.0]))        |
| マッチパターン | (dillo w c)                                      |
+---------------+--------------------------------------------------+
```

## パターンマッチ（Pattern Matching）

```
+-------------+--------------------------------------------------+
| 基本        | (match value [pat body] ...)                     |
+-------------+--------------------------------------------------+
| 定義        | (match-define pat value)                         |
| パターン    | (quote datum)  (list lvp ...)                    |
|             | (list-no-order pat ...)  (vector lvp ...)        |
|             | (struct-id field ...)  (? expr pat)  ...         |
+-------------+--------------------------------------------------+
```

## 基本（続き）

```
+----------------------------------+--------------------------------------------------+
| 破壊的代入                       | set!                                             |
+----------------------------------+--------------------------------------------------+
| 例外                             | error  with-handlers  raise  exit                |
| 遅延評価                         | promise?  delay  force                           |
| 継続                             | let/cc  let/ec  dynamic-wind                     |
|                                  | call-with-continuation-prompt                    |
| パラメータ                       | make-parameter  parameterize                     |
| 実行時に必要な外部ファイル       | define-runtime-path                              |
| 継続マーク                       | continuation-marks                               |
|                                  | with-continuation-mark  continuation-mark-set->list |
| 多値                             | values  let-values  define-values  call-with-values |
+----------------------------------+--------------------------------------------------+
```

## 契約（Contracts）

```
+-------------+--------------------------------------------------+
| 基本        | any/c  or/c  and/c  false/c  integer-in           |
|             | vector/c  listof  list/c  cons/c  ->              |
+-------------+--------------------------------------------------+
| 関数        | ->  ->*  ->i                                     |
| 適用        | contract-out  recontract-out  with-contract      |
|             | define/contract  contract-out                    |
+-------------+--------------------------------------------------+
```

## 反復（Iteration）

```
+------------+--------------------------------------------------+
| シーケンス | in-range  in-naturals  in-list  in-vector        |
|            | in-port  in-lines  in-hash  in-directory         |
+------------+--------------------------------------------------+
| ジェネレータ | generator  yield  in-generator                  |
+------------+--------------------------------------------------+
```

## 構造体（応用）

```
+----------------+--------------------------------------------------+
| 部分構造体     | (struct 2d (x y))  (struct 3d 2d (z))            |
|                | (2d-x (3d 1 2 3))                                |
+----------------+--------------------------------------------------+
| 可変フィールド | (struct monster (type [hp #:mutable]))           |
|                | (define m (monster 'orc 10))  (set-monster-hp! m 8) |
| 透過性         | (struct cash ($ ¢) #:transparent)                |
|                | (struct->vector (cash 5 95))                     |
| 表示           | (struct nickname [n v]                           |
|                |   #:methods gen:custom-write [...])              |
| 直列化         | (struct txn (who what where) #:prefab)           |
|                | (write (txn "me" "cash" "here"))                 |
+----------------+--------------------------------------------------+
```

## ジェネリクス（Generics）

```
+---------------+--------------------------------------------------+
| 定義          | define-generics                                  |
+---------------+--------------------------------------------------+
| 実装          | (struct even-set () #:methods gen:set            |
|               |   [(define (set-member? s v) (even? v)) ...])    |
+---------------+--------------------------------------------------+
```

## クラス（Classes）

```
+---------------+--------------------------------------------------+
| 定義          | interface  class*                                |
+---------------+--------------------------------------------------+
| 生成          | make-object  new  instantiate                    |
| メソッド      | send  send/apply  send/keyword-apply  send*      |
|               | send+                                            |
| フィールド    | get-field  set-field!                            |
| ミックスイン  | mixin                                            |
| トレイト      | trait  trait-sum  trait-exclude  trait-rename…   |
| 契約          | class/c  instanceof/c  is-a?/c                   |
|               | implementation?/c  subclass?/c                   |
+---------------+--------------------------------------------------+
```

## 構文（Syntax / Macros）

```
+--------------------+--------------------------------------------------+
| 定義               | define-syntax  define-simple-macro               |
|                    | begin-for-syntax  define-for-syntax              |
+--------------------+--------------------------------------------------+
| テンプレート       | syntax  syntax/loc  with-syntax                  |
| ()-構文の解析      | syntax-parse  define-syntax-class  pattern       |
| 構文オブジェクト   | syntax-source  syntax-line ...                   |
|                    | syntax->datum  datum->syntax                     |
| 変換器             | make-set!-transformer  make-rename-transformer   |
|                    | local-expand                                     |
| 構文パラメータ     | define-syntax-parameter  syntax-parameterize     |
|                    | syntax-parameter-value                           |
| 生構文の解析       | lexer  parser  cfg-parser                        |
+--------------------+--------------------------------------------------+
```

## パッケージ（Packages）

```
+------------+----------------------+
| 確認       | `raco pkg show`      |
+------------+----------------------+
| 検索       | pkgs.racket-lang.org |
| インストール | `raco pkg install` |
| 更新       | `raco pkg update`    |
| 削除       | `raco pkg remove`    |
+------------+----------------------+
```

## 開発ツールなど（Miscellaneous）

```
+----------------------+--------------------------------------------------+
| コンパイル           | `raco make program.rkt`                          |
+----------------------+--------------------------------------------------+
| テスト               | `raco test program.rkt a-directory`              |
| 実行ファイル生成     | `raco exe program.rkt`                           |
| DrRacket 拡張        | drracket:language:simple-module-based-language-… |
| スライド             | slide  standard-fish  code                       |
+----------------------+--------------------------------------------------+
```
