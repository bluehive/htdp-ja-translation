<!-- Appendix manual: racket-cheat -->
<!-- Source URL path: /racket-cheat/index.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/racket-cheat/index.html -->
<!-- Canonical English source for Japanese translation -->

# Racket Cheat Sheet

Jay McCarthy

```
+-----------+--------------------------------------------------+
| Sites     | main ⏎ download ⏎ docs ⏎ git                     |
+-----------+--------------------------------------------------+
| Community | packages ⏎ Discourse ⏎ Discord ⏎ more...         |
| Running   | Put #langracket"Hello, world!" in `hello.rkt` a… |
+-----------+--------------------------------------------------+
```

## Numbers

```
+---------------+--------------------------------------------------+
| Literals      | integer 1 rational 1/2 complex 1+2i floating 3.… |
+---------------+--------------------------------------------------+
| Arithmetic    | +-*/quotientremaindermoduloadd1sub1maxminroundf… |
| Compare       | =<<=>>=                                          |
| Bitwise       | bitwise-iorbitwise-andbitwise-xorbitwise-notari… |
| Format        | number->stringstring->numberreal->decimal-string |
| Test          | number?complex?...exact-nonnegative-integer?...… |
| Misc          | random                                           |
| Match Pattern | (? number? n) 42                                 |
+---------------+--------------------------------------------------+
```

## Strings

```
+---------------+--------------------------------------------------+
| Literals      | "Racket" quoting "a \" approaches!" unicode "λx… |
+---------------+--------------------------------------------------+
| Create        | make-stringstringstring-appendbuild-stringstrin… |
| Observe       | string-lengthstring-refsubstringstring-splitin-… |
| Modify        | string-downcasestring-upcasestring-trim          |
| Test          | string?string=?string<=?string-ci<=?             |
| Regexp        | #rx"a|b"#rx"^c(a|d)+r$"regexp-quoteregexp-match… |
| Match Pattern | (? string? s) "Banana?"                          |
+---------------+--------------------------------------------------+
```

## Bytes

```
+---------------+--------------------------------------------------+
| Literals      | #"rawbytes\0"                                    |
+---------------+--------------------------------------------------+
| Create        | make-bytesbytes                                  |
| Numbers       | integer->integer-bytesreal->floating-point-bytes |
| Observe       | bytes-lengthbytes-refsubbytesin-bytes            |
| Modify        | bytes-set!bytes-copy!bytes-fill!                 |
| Conversion    | bytes->string/utf-8 ⏎ string->bytes/utf-8        |
| Test          | bytes?bytes=?                                    |
| Match Pattern | (? bytes? b) #"0xDEADBEEF"                       |
+---------------+--------------------------------------------------+
```

## Other

```
+------------+--------------------------------------------------+
| Booleans   | #t#fnotequal?                                    |
+------------+--------------------------------------------------+
| Characters | #\a#\tab#\λchar?char->integerinteger->charchar<… |
| Symbols    | 'Racketsymbol?eq?string->symbolgensym            |
| Boxes      | box?boxunboxset-box!box-cas!                     |
| Procedures | procedure?applycomposecompose1keyword-applyproc… |
| Void       | void?void                                        |
| Undefined  | undefined                                        |
+------------+--------------------------------------------------+
```

## Lists

```
+---------------+--------------------------------------------------+
| Create        | emptylistlist*build-listfor/list                 |
+---------------+--------------------------------------------------+
| Observe       | empty?list?pair?lengthlist-refmembercountargmin… |
| Use           | appendreversemapandmapormapfoldrin-list          |
| Modify        | filterremove...sorttakedropsplit-atpartitionrem… |
| Match Pattern | (list a b c) (list* a b more) (list top more..… |
+---------------+--------------------------------------------------+
```

## Immutable Hash

```
+---------+--------------------------------------------------+
| Create  | hashhasheq                                       |
+---------+--------------------------------------------------+
| Observe | hash?hash-refhash-has-key?hash-countin-hashin-h… |
| Modify  | hash-sethash-updatehash-remove                   |
+---------+--------------------------------------------------+
```

## Vector

```
+---------------+------------------------------------------------+
| Create        | build-vectorvectormake-vectorlist->vector      |
+---------------+------------------------------------------------+
| Observe       | vector?vector-lengthvector-refin-vector        |
| Modify        | vector-set!vector-fill!vector-copy!vector-map! |
| Match Pattern | (vector x y z) (vector x y calabi–yau...)     |
+---------------+------------------------------------------------+
```

## Streams

```
+---------+-----------------------------------------------+
| Create  | streamstream*empty-stream                     |
+---------+-----------------------------------------------+
| Observe | stream-empty?stream-firststream-restin-stream |
+---------+-----------------------------------------------+
```

## Mutable Hash

```
+---------+--------------------------------------------------+
| Create  | make-hashmake-hasheq                             |
+---------+--------------------------------------------------+
| Observe | hash?hash-refhash-has-key?hash-countin-hashin-h… |
| Modify  | hash-set!hash-ref!hash-update!hash-remove!       |
+---------+--------------------------------------------------+
```

## Input/Output

```
+-----------------+--------------------------------------------------+
| Formatting      | ~a~v~s~e~rpretty-format                          |
+-----------------+--------------------------------------------------+
| Input           | readread-bytespeek-byte                          |
| Output          | writewrite-bytesdisplaydisplaylnpretty-print     |
| Ports and Files | with-input-from-filewith-output-to-fileflush-ou… |
+-----------------+--------------------------------------------------+
```

## Files

```
+-------+--------------------------------------------------+
| Paths | build-pathbytes->pathpath->bytespath-replace-su… |
+-------+--------------------------------------------------+
| Files | file-exists?rename-file-or-directorycopy-direct… |
+-------+--------------------------------------------------+
```

## Miscellaneous

```
+----------------------+--------------------------------------------------+
| Time                 | current-secondscurrent-inexact-millisecondsdate… |
+----------------------+--------------------------------------------------+
| Command-Line Parsing | command-line                                     |
| FFI                  | ffi-lib_uint32..._funmallocfree                  |
+----------------------+--------------------------------------------------+
```

## Networking

```
+-----------+--------------------------------------------------+
| TCP       | tcp-listentcp-connecttcp-accepttcp-close         |
+-----------+--------------------------------------------------+
| HTTP      | http-connhttp-conn-open!http-conn-send!http-con… |
| URLs      | string->urlurl->stringurl-query                  |
| Email     | smtp-send-messageimap-connect...                 |
| JSON      | write-jsonread-json                              |
| XML       | read-xmlwrite-xmlwrite-xexpr                     |
| Databases | postgresql-connectmysql-connectsqlite3-connectq… |
+-----------+--------------------------------------------------+
```

## Security

```
+------------+--------------------------------------------------+
| Custodians | make-custodiancustodian-shutdown-allcurrent-cus… |
+------------+--------------------------------------------------+
| Sandboxes  | make-evaluatormake-module-evaluator              |
+------------+--------------------------------------------------+
```

## Concurrency

```
+----------------+--------------------------------------------------+
| Threads        | threadkill-threadthread-waitmake-thread-group    |
+----------------+--------------------------------------------------+
| Events         | syncchoice-evtwrap-evthandle-evtalarm-evt...     |
| Channels       | make-channelchannel-getchannel-put               |
| Semaphores     | make-semaphoresemaphore-postsemaphore-wait       |
| Async Channels | make-async-channelasync-channel-getasync-channe… |
+----------------+--------------------------------------------------+
```

## Parallelism

```
+-----------+--------------------------------------------------+
| Futures   | futuretouchprocessor-countmake-fsemaphore...     |
+-----------+--------------------------------------------------+
| Places    | dynamic-placeplaceplace-waitplace-waitplace-cha… |
| Processes | subprocesssystem*                                |
+-----------+--------------------------------------------------+
```

## Basics

```
+------------------------+--------------------------------------------------+
| Modules                | (module+ main body...) ⏎ (module+ test body..… |
+------------------------+--------------------------------------------------+
| S-expressions          | quote '(a b c) quasiquote unquote `(1 2,(+ 1 2… |
| Procedure Applications | (fn arg1 arg2) ⏎ keyword args (fn arg1 #:key ar… |
| Procedures             | (lambda (x) x) (λ (x) x) ⏎ (λ (x [opt 1]) (+ x … |
| Binding                | (let ([x 1] [y 2]) (+ x y)) ⏎ (let* ([x 1] [x (… |
| Conditionals           | (if (zero? x) 0 (/ 1 x)) ⏎ (cond [(even? x) 0] … |
| Definitions            | (define x 1) ⏎ (define (f y) (+ x y))            |
| Iteration              | forfor/listfor*                                  |
| Blocks                 | beginwhenunless                                  |
| Require Sub-forms      | prefix-inonly-inexcept-inrename-infor-syntaxfor… |
| Provide Sub-forms      | all-defined-outall-from-outrename-out...contrac… |
+------------------------+--------------------------------------------------+
```

## Structures

```
+---------------+--------------------------------------------------+
| Definition    | (struct dillo (weight color))                    |
+---------------+--------------------------------------------------+
| Create        | (define danny (dillo 17.5 'purple))              |
| Observe       | (dillo? danny) (dillo-weight danny) (dillo-colo… |
| Modify        | (struct-copy dillo danny ([weight 18.0]))        |
| Match Pattern | (dillo w c)                                      |
+---------------+--------------------------------------------------+
```

## Pattern Matching

```
+-------------+--------------------------------------------------+
| Basics      | (match value [pat body]...)                     |
+-------------+--------------------------------------------------+
| Definitions | (match-define pat value)                         |
| Patterns    | (quote datum) (list lvp...) (list-no-order pat… |
+-------------+--------------------------------------------------+
```

## Basics

```
+----------------------------------+--------------------------------------------------+
| Mutation                         | set!                                             |
+----------------------------------+--------------------------------------------------+
| Exceptions                       | errorwith-handlersraiseexit                      |
| Promises                         | promise?delayforce                               |
| Continuations                    | let/cclet/ecdynamic-windcall-with-continuation-… |
| Parameters                       | make-parameterparameterize                       |
| External Files Needed at Runtime | define-runtime-path                              |
| Continuation Marks               | continuation-markswith-continuation-markcontinu… |
| Multiple Values                  | valueslet-valuesdefine-valuescall-with-values    |
+----------------------------------+--------------------------------------------------+
```

## Contracts

```
+-------------+--------------------------------------------------+
| Basics      | any/cor/cand/cfalse/cinteger-invector/clistofli… |
+-------------+--------------------------------------------------+
| Functions   | ->->*->i                                         |
| Application | contract-outrecontract-outwith-contractdefine/c… |
+-------------+--------------------------------------------------+
```

## Iteration

```
+------------+--------------------------------------------------+
| Sequences  | in-rangein-naturalsin-listin-vectorin-portin-li… |
+------------+--------------------------------------------------+
| Generators | generatoryieldin-generator                       |
+------------+--------------------------------------------------+
```

## Structures

```
+----------------+--------------------------------------------------+
| Sub-structures | (struct 2d (x y)) (struct 3d 2d (z)) (2d-x (3d … |
+----------------+--------------------------------------------------+
| Mutation       | (struct monster (type [hp #:mutable])) (define … |
| Transparency   | (struct cash ($ ¢) #:transparent) (struct->vect… |
| Printing       | (struct nickname [n v] #:methods gen:custom-wri… |
| Serialization  | (struct txn (who what where) #:prefab) (write (… |
+----------------+--------------------------------------------------+
```

## Generics

```
+---------------+--------------------------------------------------+
| Definition    | define-generics                                  |
+---------------+--------------------------------------------------+
| Instantiation | (struct even-set () #:methods gen:set [(define … |
+---------------+--------------------------------------------------+
```

## Classes

```
+---------------+--------------------------------------------------+
| Definition    | interfaceclass*                                  |
+---------------+--------------------------------------------------+
| Instantiation | make-objectnewinstantiate                        |
| Methods       | sendsend/applysend/keyword-applysend*send+       |
| Fields        | get-fieldset-field!                              |
| Mixins        | mixin                                            |
| Traits        | traittrait-sumtrait-excludetrait-rename...       |
| Contracts     | class/cinstanceof/cis-a?/cimplementation?/csubc… |
+---------------+--------------------------------------------------+
```

```
+--------------------+--------------------------------------------------+
| Definition         | define-syntaxdefine-simple-macrobegin-for-synta… |
+--------------------+--------------------------------------------------+
| Templates          | syntaxsyntax/locwith-syntax                      |
| Parsing ()-Syntax  | syntax-parsedefine-syntax-classpattern           |
| Syntax Objects     | syntax-sourcesyntax-line...syntax->datumdatum->… |
| Transformers       | make-set!-transformermake-rename-transformerloc… |
| Syntax Parameters  | define-syntax-parametersyntax-parameterizesynta… |
| Parsing Raw Syntax | lexerparsercfg-parser                            |
+--------------------+--------------------------------------------------+
```

## Packages

```
+------------+----------------------+
| Inspection | `raco pkg show`      |
+------------+----------------------+
| Finding    | pkgs.racket-lang.org |
| Installing | `raco pkg install`   |
| Updating   | `raco pkg update`    |
| Removing   | `raco pkg remove`    |
+------------+----------------------+
```

## Miscellaneous

```
+----------------------+--------------------------------------------------+
| Compiling            | `raco make program.rkt`                          |
+----------------------+--------------------------------------------------+
| Testing              | `raco test program.rkt a-directory`              |
| Building Executables | `raco exe program.rkt`                           |
| Extending DrRacket   | drracket:language:simple-module-based-language-… |
| Slides               | slidestandard-fishcode                           |
+----------------------+--------------------------------------------------+
```
