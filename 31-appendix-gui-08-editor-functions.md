# 8 エディタ関数

**原本:** `extracted/appendix/gui/original_markdown_08_Editor_Functions.md`  
**Source URL path:** `/gui/Editor_Functions.html`

```
+----------------------------------------------+
| [手続き]                                     |
|                                              |
| (add-editor-keymap-functions keymap) → void? |
| keymap: (is-a?/c keymap%)                   |
+----------------------------------------------+
```

与えられた `keymap%` オブジェクトに、すべての `editor<%>` オブジェクトに適用できるマップ可能関数を読み込みます。

- `"copy-clipboard"`
- `"copy-append-clipboard"`
- `"cut-clipboard"`
- `"cut-append-clipboard"`
- `"paste-clipboard"`
- `"paste-x-selection"`
- `"delete-selection"`
- `"clear-selection"`
- `"undo"`
- `"redo"`
- `"select-all"`

```
+--------------------------------------------------+
| [手続き]                                         |
|                                                  |
| (add-pasteboard-keymap-functions keymap) → void? |
| keymap: (is-a?/c keymap%)                       |
+--------------------------------------------------+
```

与えられた `keymap%` オブジェクトの表に、`pasteboard%` オブジェクトに適用できるマップ可能関数を読み込みます。現在のところ、そのような関数はありません。

`add-editor-keymap-functions` も参照してください。

```
+--------------------------------------------+
| [手続き]                                   |
|                                            |
| (add-text-keymap-functions keymap) → void? |
| keymap: (is-a?/c keymap%)                 |
+--------------------------------------------+
```

与えられた `keymap%` オブジェクトの表に、すべての `text%` オブジェクトに適用できる関数を読み込みます。

- `"forward-character"`
- `"backward-character"`
- `"previous-line"`
- `"next-line"`
- `"previous-page"`
- `"next-page"`
- `"forward-word"`
- `"backward-word"`
- `"forward-select"`
- `"backward-select"`
- `"select-down"`
- `"select-up"`
- `"select-page-up"`
- `"select-page-down"`
- `"forward-select-word"`
- `"backward-select-word"`
- `"beginning-of-file"`
- `"end-of-file"`
- `"beginning-of-line"`
- `"end-of-line"`
- `"select-to-beginning-of-file"`
- `"select-to-end-of-file"`
- `"select-to-beginning-of-line"`
- `"select-to-end-of-line"`
- `"copy-clipboard"`
- `"copy-append-clipboard"`
- `"cut-clipboard"`
- `"cut-append-clipboard"`
- `"paste-clipboard"`
- `"paste-x-selection"`
- `"delete-selection"`
- `"delete-previous-character"`
- `"delete-next-character"`
- `"clear-selection"`
- `"delete-to-end-of-line"`
- `"delete-next-word"`
- `"delete-previous-word"`
- `"delete-line"`
- `"undo"`
- `"redo"`

`add-editor-keymap-functions` も参照してください。

```
+-----------------------------------------------------+
| [手続き]                                            |
|                                                     |
| (append-editor-font-menu-items menu) → void?        |
| menu: (or/c (is-a?/c menu%) (is-a?/c popup-menu%)) |
+-----------------------------------------------------+
```

フォント面やスタイルの変更など、標準的なフォント操作の一式を実装するメニュー項目を `menu` に追加します。各メニュー項目のコールバックは、`top-level-window<%>` の `get-edit-target-object` を使います（親の連鎖を辿ってフレームに達するまで探索します）。結果が `editor<%>` オブジェクトであれば、そのエディタに対して `text%` の `change-style` または `pasteboard%` の `change-style` が呼び出されます。

```
+--------------------------------------------------------------------------------+
| [手続き]                                                                       |
|                                                                                |
| (append-editor-operation-menu-items                                            |
| → void?                                                                        |
| menu: (or/c (is-a?/c menu%) (is-a?/c popup-menu%))                            |
| text-only?: any/c = #t                                                        |
| popup-position: (or/c #f (list/c (is-a?/c text%) exact-nonnegative-integer?)) |
| = #f                                                                           |
+--------------------------------------------------------------------------------+
```

切り取りや貼り付けなど、標準的なエディタ操作を実装するメニュー項目を `menu` に追加します。各メニュー項目のコールバックは、`top-level-window<%>` の `get-edit-target-object` を使います（親の連鎖を辿ってフレームに達するまで探索します）。結果が `editor<%>` オブジェクトであれば、そのエディタに対して `editor<%>` の `do-edit-operation` が呼び出されます。

`text-only?` が `#f` のときは、テキスト以外のスニップを挿入するメニュー項目（Insert Image... など）もメニューに追加されます。

`popup-position` が `#f` でない場合、`append-editor-operation-menu-items` はポップアップメニュー構築のために呼ばれたものとみなされ、リストの二つの要素は、ポップアップメニューのためにマウスがクリックされた `text%` オブジェクトと、クリック位置です。その場合、クリックが `string-snip%` ではないスニップ上に落ちたとき、Copy および Cut メニューが有効になり、対応するコールバックはその一つのスニップをコピー／カットします。

```
+------------------------------------------------+
| [パラメータ]                                   |
|                                                |
| (current-text-keymap-initializer)              |
| → ((is-a?/c keymap%). ->. any/c)             |
| (current-text-keymap-initializer proc) → void? |
| proc: ((is-a?/c keymap%). ->. any/c)        |
+------------------------------------------------+
```

キーマップ初期化手続きを指定するパラメータです。この手続きは、`text-field%` オブジェクト、または `graphical-read-eval-print-loop` が作成する `text%` オブジェクトのキーマップを初期化するときに呼び出されます。

初期化子はキーマップオブジェクトを受け取り、何も返しません。既定の初期化子は、与えられたキーマップを、切り取り・コピー・貼り付け・アンドゥ・全選択のための標準的なテキストエディタ用キーボードおよびマウス束縛を実装する内部キーマップへ連鎖させます。右マウスボタンは、ボタンを離したときに編集メニューをポップアップするようマップされます。

パッケージ `gui-lib` のバージョン 1.51 で変更：既定の初期化子における Unix キー束縛を Windows に合わせ、`start-of-line` および `end-of-line` 束縛を削除しました。

```
+------------------------------------------+
| [手続き]                                 |
|                                          |
| (editor-set-x-selection-mode on) → void? |
| on: any/c                               |
+------------------------------------------+
```

Unix では、エディタの選択は X11 Windows の選択規約に従います。`on` が `#f` のとき、振る舞いは（貼り付け前に明示的にコピーが必要な）クリップボード規約のみに切り替わります。

```
+---------------------------------------+
| [手続き]                              |
|                                       |
| (get-the-editor-data-class-list)      |
| → (is-a?/c editor-data-class-list<%>) |
+---------------------------------------+
```

現在のイベントスペース用のエディタデータクラスリストのインスタンスを取得します。

```
+----------------------------------------------------------+
| [手続き]                                                 |
|                                                          |
| (get-the-snip-class-list) → (is-a?/c snip-class-list<%>) |
+----------------------------------------------------------+
```

現在のイベントスペース用のスニップクラスリストのインスタンスを取得します。

```
+---------------------------------------+
| [手続き]                              |
|                                       |
| (map-command-as-meta-key on?) → void? |
| on?: any/c                           |
| (map-command-as-meta-key) → boolean?  |
+---------------------------------------+
```

Mac OS 上での `keymap%` マッピングにおける `m:` の解釈を決めます。`keymap%` の `map-function` も参照してください。

第一の場合：

`on?` が `#t` なら、`m:` は Command キーに対応します。`on?` が `#f` なら、Mac OS 上で `m:` はどのキーにも対応しません。

第二の場合：

`m:` が Command に対応するなら `#t` を、そうでなければ `#f` を返します。

```
+----------------------------------------------------+
| [手続き]                                           |
|                                                    |
| (open-input-graphical-file filename) → input-port? |
| filename: string?                                 |
+----------------------------------------------------+
```

`filename` を（`'binary` モードで）開き、エディタ形式の「グラフィカル」ファイルに見えるかどうかを調べます。エディタファイルに見えない場合は、行数えを有効にしたファイルポートを返します。そうでなければ、ファイルをエディタに読み込み、結果ポートは `open-input-text-editor` で作成されます。

```
+---------------------------------------------------------------+
| [手続き]                                                      |
|                                                               |
| (open-input-text-editor                                       |
| → input-port                                                  |
| text-editor: (is-a?/c text%)                                 |
| start-position: exact-nonnegative-integer? = 0               |
| end-position: (or/c exact-nonnegative-integer? 'end) = 'end  |
| snip-filter: ((is-a?/c snip%). ->. any/c) = (lambda (s) s) |
| port-name: any/c = text-editor                               |
| expect-to-read-all?: any/c = #f                              |
| lock-while-reading?: any/c = #f                              |
+---------------------------------------------------------------+
```

`text-editor` から内容を取り出す入力ポートを作成します。位置 `start-position` と `end-position` のあいだのエディタ内容がポートの内容です。`end-position` が `'end` のときは、エディタ末尾までが内容です。`string-snip%` オブジェクトではないスニップが `start-position` または `end-position` をまたぐ場合、そのスニップ全体がポートに寄与します。`string-snip%` インスタンスが `start-position` をまたぐ場合は、`start-position` 以降の部分だけが寄与し、`string-snip%` オブジェクトが `end-position` をまたぐ場合は、`end-position` より前の部分だけが寄与します。

`text-editor` 内の `string-snip%` のインスタンスは、結果ポートに文字列を生成します。それ以外の種類のスニップは `snip-filter` に渡され、ポート用の「特殊」値を得ます。`snip-filter` の第一結果としてスニップが返り、かつそれが `readable-snip<%>` のインスタンスなら、そのスニップは `read-special` メソッドを通じてポート用の特殊値を生成します。`snip-filter` が他の種類のスニップを返す場合は、特殊結果のためにコピーされます。最後に、`snip-filter` の第一結果がスニップでない場合は、その値が特殊結果として直接使われます。

`port-name` 引数は入力ポートの名前に使われます。`expect-to-read-all?` 引数は性能上のヒントで、ポートのストリーム全体を読む場合は `#t` を使ってください。

結果ポートは、`text-editor` が次のいずれかで変化した場合には使ってはなりません。スニップの挿入（`after-insert` を参照）、スニップの削除（`after-delete` を参照）、スニップの分割（`after-split-snip` を参照）、スニップの併合（`after-merge-snips` を参照）、またはスニップのカウント変更（稀です。`recounted` を参照）。これらの変化は `get-revision-number` メソッドで検出できます。

そのような誤用を防ぐ助けとして、`lock-while-reading?` 引数が真値なら、`open-input-text-editor` は返す前に `text-editor` をロックし `begin-edit-sequence` を呼び、上記メソッドを安全に使えるようになったあとでロックを外し `end-edit-sequence` を呼びます。（場合によっては、それらのメソッドを常に安全に使えるときは、エディタをロックしたり編集シーケンスに入れたりしません。）

```
+-------------------------------------------------------------------------+
| [手続き]                                                                |
|                                                                         |
| (open-output-text-editor                                                |
| text-editor: (is-a?/c text%)                                           |
| start-position: (or/c exact-nonnegative-integer? (one/of 'end)) = 'end |
| special-filter: (any/c. ->. any/c) = (lambda (x) x)                  |
| port-name: any/c = text-editor                                         |
| eventspace: (or/c eventspace? #f) = (current-eventspace)               |
+-------------------------------------------------------------------------+
```

内容を `text-editor` へ届ける出力ポートを作成します。内容は位置 `start-position` から `text-editor` に書き込まれます。`'end` は、テキストエディタの現在の末尾位置から出力を始めることを示します。

`special-filter` が与えられた場合、`write-special` でポートに書き込まれた任意の値にそれが適用され、結果がその場に挿入されます。特殊値が `snip%` オブジェクトなら、エディタに挿入されます。そうでなければ、特殊値はエディタへ表示されます。

結果の出力ポートで行数えが有効な場合、ポートは、データが書き込まれるエディタ内の行、行先頭からのオフセット、位置を報告します。

`eventspace` が `#f` でないとき、出力ポートが `eventspace` のハンドラスレッド以外のスレッドで使われると、内容は `eventspace` 内の低優先度コールバックを通じて `text-editor` へ届けられます。したがって、`eventspace` がエディタの表示のイベントスペースに対応していれば、どのスレッドからでも出力ポートへの書き込みは安全です。

`eventspace` が `#f` の場合、ポートは弱い意味でのスレッド安全性しか持たないことに注意してください。内容は編集シーケンス内で `text-editor` に届けられますが、たとえばエディタが有効な `editor-canvas%` に表示されている場合、編集シーケンスだけでは同期として不十分です。詳細は Editors and Threads を参照してください。

```
+-------------------------------------------+
| [手続き]                                  |
|                                           |
| (read-editor-global-footer in) → boolean? |
| in: (is-a?/c editor-stream-in%)          |
+-------------------------------------------+
```

`read-editor-global-header` を参照してください。`read-editor-global-header` が `#f` を返した場合でも、`read-editor-global-footer` を呼び出してください。

```
+-------------------------------------------+
| [手続き]                                  |
|                                           |
| (read-editor-global-header in) → boolean? |
| in: (is-a?/c editor-stream-in%)          |
+-------------------------------------------+
```

`in` からデータを読み取り、ストリームからエディタを読むための初期化を行います。読み取りが成功すれば戻り値は `#t`、そうでなければ `#f` です。

一つ以上のエディタは、エディタの `read-from-file` メソッドを呼び出すことでストリームから読めます。（読むエディタの個数は、あらかじめアプリケーションが知っている必要があります。）すべてのエディタを読み終えたら、`read-editor-global-footer` を呼び出します。`read-editor-global-header` と `read-editor-global-footer` の呼び出しは、`read-from-file` の任意の呼び出しを挟まなければならず、これらのメソッド、または `write-editor-global-header` と `write-editor-global-footer` を使って同時に読み書きできるストリームは一つだけです。

Racket のバージョンをまたぐストリームから読むときは、この手続きの前に `read-editor-version` を使ってください。

```
+--------------------------------------------+
| [手続き]                                   |
|                                            |
| (read-editor-version                       |
| in: (is-a?/c editor-stream-in%)           |
| in-base: (is-a?/c editor-stream-in-base%) |
| parse-format?: any/c                      |
| raise-errors?: any/c = #t                 |
+--------------------------------------------+
```

`in-base` からバージョン情報を読み取ります。ここで `in-base` は `in` のベースです。`in-base` から解析されたバージョン情報は、後のバージョン依存の解析のために `in` に記録されます。バージョン情報が正しく読め、かつそのバージョンがサポートされていれば、手続きの結果は真です。

`parse-format?` が真なら、`in-base` に初期の `"WXME"` 形式標識があるかを調べます。形式振り分けコードがすでに `"WXME"` を消費しているときは `#f` を使ってください。

`raise-errors?` が真なら、読み取りエラーは `#f` 結果ではなく例外を引き起こします。

```
+------------------------------------------+
| [手続き]                                 |
|                                          |
| (text-editor-load-handler                |
| filename: path = string                 |
| expected-module-name: (or/c symbol? #f) |
+------------------------------------------+
```

この手続きは、`current-load` と共に使うためのロードハンドラです。

ハンドラは Racket エディタ形式のファイル（ファイル形式を参照）を認識し、ロードのために復号します。通常は GRacket の起動時にインストールされます（Running Racket or GRacket を参照）。

ハンドラは、ファイル先頭 12 文字が `WXME01‹digit›‹digit› ##` であることでエディタファイルを認識します。そのようなファイルは、`text%` オブジェクトを作り、`insert-file` でファイルをそのオブジェクトに読み込み、`open-input-text-editor` でエディタ内容をポートへ変換することでロード用に開かれます。こうしてポートを得たあと、内容は実質的に Racket 既定のロードハンドラと同様に読まれます。違いは、エディタが `readable-snip<%>` のインスタンスを含みうることで、それらはスニップの `read-special` メソッドを通じて「読まれ」ます。詳細は `open-input-text-editor` を参照してください。

```
+------------------------------------------------------------+
| [値]                                                       |
|                                                            |
| the-editor-wordbreak-map: (is-a?/c editor-wordbreak-map%) |
+------------------------------------------------------------+
```

`editor-wordbreak-map%` を参照してください。

```
+----------------------------------------+
| [値]                                   |
|                                        |
| the-style-list: (is-a?/c style-list%) |
+----------------------------------------+
```

`style-list%` を参照してください。

```
+---------------------------------------------+
| [手続き]                                    |
|                                             |
| (write-editor-global-footer out) → boolean? |
| out: (is-a?/c editor-stream-out%)          |
+---------------------------------------------+
```

`write-editor-global-header` を参照してください。`write-editor-global-header` が `#f` を返した場合でも、`write-editor-global-footer` を呼び出してください。

```
+---------------------------------------------+
| [手続き]                                    |
|                                             |
| (write-editor-global-header out) → boolean? |
| out: (is-a?/c editor-stream-out%)          |
+---------------------------------------------+
```

`out` へデータを書き込み、ストリームへエディタを書くための初期化を行います。書き込みが成功すれば戻り値は `#t`、そうでなければ `#f` です。

一つ以上のエディタは、エディタの `write-to-file` メソッドを呼び出すことでストリームへ書けます。すべてのエディタを書き終えたら、`write-editor-global-footer` を呼び出します。`write-editor-global-header` と `write-editor-global-footer` の呼び出しは、`write-to-file` の任意の呼び出しを挟まなければならず、これらのメソッド、または `read-editor-global-header` と `read-editor-global-footer` を使って同時に読み書きできるストリームは一つだけです。

Racket のバージョンをまたぐストリームを支えるには、この手続きの前に `write-editor-version` を使ってください。

ファイル形式も参照してください。

```
+------------------------------------------------+
| [手続き]                                       |
|                                                |
| (write-editor-version out out-base) → boolean? |
| out: (is-a?/c editor-stream-out%)             |
| out-base: (is-a?/c editor-stream-out-base%)   |
+------------------------------------------------+
```

ストリーム `out` へエディタ情報を書く準備として、`out-base` にバージョン情報を書き込みます。

現在 `out` 引数は使われませんが、`out-base` は `out` のベースであるべきです。将来、`out` は後のバージョン依存の出力のためにバージョン情報を記録するかもしれません。

書き込みが成功すれば結果は `#t`、そうでなければ `#f` です。
