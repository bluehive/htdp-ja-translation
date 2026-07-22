## 4 ウィンドウ機構関数

### 目次

- 4.1 ダイアログ
- 4.2 イベントスペース
- 4.3 システムメニュー
- 4.4 グローバル・グラフィックス
- 4.5 フォント
- 4.6 その他

### 4.1 ダイアログ

これらの関数は、ユーザから入力を得たり、メッセージを表示したりします。

```
+------------------------------------------------------------------+
| [procedure]                                                      |
|                                                                  |
| (get-file                                                        |
| message: (or/c label-string? #f) = #f                           |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f       |
| directory: (or/c path-string? #f) = #f                          |
| filename: (or/c path-string? #f) = #f                           |
| extension: (or/c string? #f) = #f                               |
| style: (listof (or/c 'packages 'enter-packages 'common)) = null |
| filters: (listof (list/c string? string?)) = '(("Any" "*.*"))   |
| dialog-mixin: (make-mixin-contract path-dialog%) = (λ (x) x)    |
+------------------------------------------------------------------+
```

プラットフォーム固有の標準（モーダル）ダイアログ経由で、ユーザからファイル・パス名を得ます。`parent` が指定されていればそれを親ウィンドウとして使い、`message` が `#f` でなければダイアログ上部のメッセージとして使います。

ユーザがダイアログをキャンセルした場合の結果は `#f`、そうでなければ選ばれたパス名です。返されるパス名は存在するかどうかわかりませんが、ダイアログのスタイルは既存ファイルの選択に向けられています。

`directory` が `#f` でなければ、ファイル・セレクタの開始ディレクトリとして使われます（そうでなければ、開始ディレクトリはプラットフォーム固有の仕方で自動選択され、通常はカレント・ディレクトリと、`get-file`、`put-file` などへの以前の呼び出しでのユーザ操作に基づきます）。`filename` が `#f` でなければ、適切なときに既定のファイル名として使われ、ディレクトリ・パスの接頭辞を含んではなりません。

Windows では、`extension` が `#f` でなければ、ユーザが拡張子を与えなかったときに返されるパスがその拡張子を使います。拡張子文字列はピリオドを含んではなりません。他のプラットフォームでは拡張子は無視されます。

`style` リストに `'common` を含められると、ネイティブ・ダイアログの代わりにプラットフォーム非依存版のダイアログが使われます。Mac OS では、`style` リストに `'packages` が含まれると、ユーザはパッケージ・ディレクトリ——Finder が通常ファイルのように表示する特別な接尾辞（例：「.app」）を持つディレクトリ——を選べます。リストに `'enter-packages` が含まれると、ユーザはパッケージ・ディレクトリ内のファイルを選べます。リストに `'packages` と `'enter-packages` の両方が含まれる場合、前者は無視されます。

Windows と Unix では、`filters` がダイアログ内でユーザが選べるフィルタ集合を決めます。`filters` リストの各要素は二つの文字列を含みます。ユーザに見えるフィルタの説明と、ファイル名に対して照合されるフィルタ・パターンです。パターン文字列は単純な「グロブ」パターンか、`;` 文字で区切られた複数のグロブ・パターンです。これらのパターンは正規表現ではなく、`*` ワイルドカード文字とのみ使えます。たとえば `"*.jp*g;*.png"` です。
Unix では、`"*.*"` パターンは暗黙に `"*"` に置き換えられます。
Mac OS では、固定接尾辞に一致するすべてのグロブから接尾辞名が抽出され（例：`"*.foo;*.bar;*.baz*"` パターンから `"foo"` と `"bar"` の二つの接尾辞が抽出される）、いずれかのフィルタでこれらの接尾辞のいずれかを持つファイルが選択可能になります。`"*.*"` グロブは、すべてのファイルを選択可能にします。

`dialog-mixin` は、このダイアログ用のクラスのインスタンスを作る前に `path-dialog%` に適用されます。

より豊かなインタフェースについては `path-dialog%` も参照してください。

```
+------------------------------------------------------------------+
| [procedure]                                                      |
|                                                                  |
| (get-file-list                                                   |
| → (or/c (listof path?) #f)                                       |
| message: (or/c label-string? #f) = #f                           |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f       |
| directory: (or/c path-string? #f) = #f                          |
| filename: (or/c path-string? #f) = #f                           |
| extension: (or/c string? #f) = #f                               |
| style: (listof (or/c 'packages 'enter-packages 'common)) = null |
| filters: (listof (list/c string? string?)) = '(("Any" "*.*"))   |
| dialog-mixin: (make-mixin-contract path-dialog%) = (λ (x) x)    |
+------------------------------------------------------------------+
```

`get-file` と同様ですが、ユーザは複数のファイルを選べ、結果はファイル・パスのリストまたは `#f` です。

```
+------------------------------------------------------------------+
| [procedure]                                                      |
|                                                                  |
| (put-file                                                        |
| message: (or/c label-string? #f) = #f                           |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f       |
| directory: (or/c path-string? #f) = #f                          |
| filename: (or/c path-string? #f) = #f                           |
| extension: (or/c string? #f) = #f                               |
| style: (listof (or/c 'packages 'enter-packages 'common)) = null |
| filters: (listof (list/c string? string?)) = '(("Any" "*.*"))   |
| dialog-mixin: (make-mixin-contract path-dialog%) = (λ (x) x)    |
+------------------------------------------------------------------+
```

プラットフォーム固有の標準（モーダル）ダイアログ経由で、ユーザからファイル・パス名を得ます。`parent` が指定されていればそれを親ウィンドウとして使い、`message` が `#f` でなければダイアログ上部のメッセージとして使います。

ユーザがダイアログをキャンセルした場合の結果は `#f`、そうでなければ選ばれたパス名です。返されるパス名は存在するかどうかわかりませんが、ダイアログのスタイルは新しいファイルの作成に向けられています。

`directory` が `#f` でなければ、ファイル・セレクタの開始ディレクトリとして使われます（そうでなければ、開始ディレクトリはプラットフォーム固有の仕方で自動選択され、通常はカレント・ディレクトリと、`get-file`、`put-file` などへの以前の呼び出しでのユーザ操作に基づきます）。`filename` が `#f` でなければ、適切なときに既定のファイル名として使われ、ディレクトリ・パスの接頭辞を含んではなりません。

Windows では、`extension` が `#f` でなければ、ユーザが拡張子を与えなかったときに返されるパスは既定の拡張子を得ます。拡張子は、対応するパターンが `(string-append "*." an-extension)` の形である場合にユーザの `filters` 選択から導かれ、選択が複数のパターンを持つ場合は最初のそのようなパターンが使われます。ユーザの選択がパターン `"*.*"` で、かつ `extension` が空文字列なら、既定の拡張子は追加されません。最後に、`extension` が空文字列以外の任意の文字列で、ユーザの `filters` 選択がパターン `"*.*"` を持つ場合、`extension` が既定の拡張子として使われます。一方、`filters` 引数は `get-file` と同じ形式と補助的な役割を持ちます。特に、`filters` 内の唯一のパターンが `(string-append "*." extension)` なら、結果のパス名は `extension` に対応する拡張子を持つことが保証されます。

Mac OS 10.5 以降では、`extension` が `#f` でも `""` でもなければ、ユーザが拡張子を与えなかったときに返されるパスは既定の拡張子を得ます。`filters` に `"*.*"` パターンが含まれる場合、ユーザはシステムが認識する任意の拡張子を与えられます。そうでなければ、返されるパスの拡張子は `extension`、または `filters` 内の任意の `(string-append "*." other-extension)` パターンの `other-extension` のいずれかです。特に、`filters` 内の唯一のパターンが空か `(string-append "*." extension)` だけを含む場合、結果のパス名は `extension` に対応する拡張子を持つことが保証されます。

Mac OS の 10.5 より前の版では、返されるパスが既定の拡張子を得るのは、`extension` が `#f` でなく、`extension` が `""` でなく、かつ `filters` が `(string-append "*." extension)` だけを含む場合だけです。

Unix では `extension` は無視され、`filters` は `get-file` と同様に見えるファイルのリストをフィルタするために使われます。

`style` リストは `get-file` と同様に扱われます。

`dialog-mixin` は、このダイアログ用のクラスのインスタンスを作る前に `path-dialog%` に適用されます。

より豊かなインタフェースについては `path-dialog%` も参照してください。

```
+---------------------------------------------------------------+
| [procedure]                                                   |
|                                                               |
| (get-directory                                                |
| message: (or/c label-string? #f) = #f                        |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f    |
| directory: (or/c path-string? #f) = #f                       |
| style: (listof (or/c 'enter-packages 'common)) = null        |
| dialog-mixin: (make-mixin-contract path-dialog%) = (λ (x) x) |
+---------------------------------------------------------------+
```

プラットフォーム固有の標準（モーダル）ダイアログ経由で、ユーザからディレクトリ・パス名を得ます。`parent` が指定されていればそれを親ウィンドウとして使います。

`directory` が `#f` でなければ、一部のプラットフォームでディレクトリ・セレクタの開始ディレクトリとして使われます（そうでなければ、開始ディレクトリはプラットフォーム固有の仕方で自動選択され、通常はカレント・ディレクトリと、`get-file`、`put-file` などへの以前の呼び出しでのユーザ操作に基づきます）。

`style` 引数は `get-file` と同様に扱われますが、指定できるのは `'common` または `'enter-packages` だけです。後者は Mac OS でのみ意味を持ち、`'enter-packages` によりユーザはパッケージ・ディレクトリ、またはパッケージ内のディレクトリを選べます。パッケージは、Finder が通常ファイルのように表示する特別な接尾辞（例：「.app」）を持つディレクトリです。

`dialog-mixin` は、このダイアログ用のクラスのインスタンスを作る前に `path-dialog%` に適用されます。

より豊かなインタフェースについては `path-dialog%` も参照してください。

```
+--------------------------------------------------------------------------------+
| [procedure]                                                                    |
|                                                                                |
| (message-box                                                                   |
| → (or/c 'ok 'cancel 'yes 'no)                                                  |
| title: label-string?                                                          |
| message: string?                                                              |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f                     |
| style: (listof (or/c 'ok 'ok-cancel 'yes-no 'caution 'stop 'no-icon)) = '(ok) |
| (listof (or/c 'ok 'ok-cancel 'yes-no                                           |
| 'caution 'stop 'no-icon))                                                      |
| dialog-mixin: (make-mixin-contract dialog%) = values                          |
|                                                                                |
| ```racket                                                                      |
| (listof (or/c 'ok 'ok-cancel 'yes-no                                           |
|               'caution 'stop 'no-icon))                                        |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

`message-box/custom` も参照してください。

（モーダル）ダイアログでユーザにメッセージを表示します。`parent` が指定されていればそれを親ウィンドウとして使います。ダイアログのタイトルは `title` です。`message` 文字列は任意の長さにでき、改行やキャリッジリターンを明示的に含めて行を折り返せます。

`style` は次のうちちょうど一つを含まなければなりません。

- `'ok` — ダイアログは OK ボタンだけを持ち、常に `'ok` を返します。
- `'ok-cancel` — メッセージ・ダイアログは Cancel と OK のボタンを持ちます。ユーザが Cancel をクリックすると結果は `'cancel`、そうでなければ結果は `'ok` です。
- `'yes-no` — メッセージ・ダイアログは Yes と No のボタンを持ちます。ユーザが Yes をクリックすると結果は `'yes`、そうでなければ結果は `'no` です。注：Yes/No ダイアログの代わりに、ベストプラクティスの GUI 設計では `message-box/custom` を使い、ボタンに意味のあるラベルを付け、ユーザがメッセージ・テキストを注意深く読まなくても選択できるようにします。

加えて、`style` に `'caution` を含めてダイアログにアプリケーション（または汎用の「情報」）アイコンの代わりに注意アイコンを使わせたり、`'stop` で停止アイコンを使わせたり、`'no-icon` でアイコンを抑制したりできます。`style` に `'caution`、`'stop`、`'no-icon` が複数含まれる場合、`'no-icon` が優先され、次に `'stop` が続きます。

ダイアログを実装するクラスは、引数を取らずメッセージのテキストを文字列として返す `get-message` メソッドを提供します。（ダイアログは `get-top-level-windows` 関数経由でアクセスできます。）

`message-box` 関数は、関連するイベントスペース（すなわち `parent` のイベントスペース、または `parent` が `#f` なら現在のイベントスペース）のハンドラ・スレッド以外のスレッドから呼べます。その場合、ダイアログがハンドラ・スレッドで走っているあいだ、現在のスレッドはブロックします。

`dialog-mixin` 引数は、ダイアログが作られる前にダイアログを実装するクラスに適用されます。

```
+-----------------------------------------------------------------------------+
| [procedure]                                                                 |
|                                                                             |
| (message-box/custom                                                         |
| → (if/c return-the-dialog? (is-a?/c dialog%) (or/c 1 2 3 close-result))     |
| (if/c return-the-dialog?                                                    |
| (is-a?/c dialog%)                                                           |
| (or/c 1 2 3 close-result))                                                  |
| title: label-string?                                                       |
| message: string?                                                           |
| button1-label: (or/c label-string? (is-a?/c bitmap%) #f)                   |
| button2-label: (or/c label-string? (is-a?/c bitmap%) #f)                   |
| button3-label: (or/c label-string? (is-a?/c bitmap%) #f)                   |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f                  |
| style: (listof (or/c 'stop 'caution 'no-icon 'number-order 'disallow-close |
| 'no-default 'default=1 'default=2 'default=3)) = '(no-default)              |
| (listof (or/c 'stop 'caution 'no-icon 'number-order                         |
| 'disallow-close 'no-default                                                 |
| 'default=1 'default=2 'default=3))                                          |
| close-result: any/c = #f                                                   |
| return-the-dialog?: any/c = #f                                             |
| dialog-mixin: (make-mixin-contract dialog%) = values                       |
|                                                                             |
| ```racket                                                                   |
| (if/c return-the-dialog?                                                    |
|       (is-a?/c dialog%)                                                     |
|       (or/c 1 2 3 close-result))                                            |
| ```                                                                         |
|                                                                             |
| ```racket                                                                   |
| (listof (or/c 'stop 'caution 'no-icon 'number-order                         |
|               'disallow-close 'no-default                                   |
|               'default=1 'default=2 'default=3))                            |
| ```                                                                         |
+-----------------------------------------------------------------------------+
```

（モーダル）ダイアログでユーザにメッセージを表示します。`parent` が指定されていればそれを親ウィンドウとして使います。ダイアログのタイトルは `title` です。`message` 文字列は任意の長さにでき、改行やキャリッジリターンを明示的に含めて行を折り返せます。

ダイアログは、ユーザがクリックするための最大三つのボタンを含みます。ボタンのラベルは `button1-label`、`button2-label`、`button3-label` で、ラベルが `#f` ならそのボタンは隠されます。

ユーザが `button1-label` のラベルの付いたボタンをクリックすると 1 が返され、2 と 3 についても同様です。ユーザが他の方法でダイアログを閉じた場合——`style` に `'disallow-close` が含まれないときだけ許されます——結果は `close-result` の値です。たとえば、ユーザは通常 Escape を打ってダイアログを閉じられます。ボタン 2 が Cancel ボタンであるときなど、`close-result` にはしばしば 2 が適切な値です。

`style` に `'number-order` が含まれない場合、ボタンの順序はプラットフォーム固有であり、ラベルは役割に基づいてボタンに割り当てるべきです。

- ボタン 1 は通常の操作であり、通常は既定ボタンです。たとえばダイアログに OK ボタンがあるなら、それです。Windows ではこのボタンは左端、Unix と Mac OS では右端です。（`system-position-ok-before-cancel?` も参照してください。）ボタンが一つだけのダイアログには、このボタンを使います。
- ボタン 2 はボタン 1 の隣にあり、しばしば Cancel の役割を果たします（ファイル置換の確認など、既定の操作がキャンセルである場合でも）。
- ボタン 3 は他の二つから離れる傾向があります（Mac OS ではダイアログ内で左揃えされます）。このボタンは三ボタン・ダイアログにだけ使います。

上の指針にもかかわらず、見えるボタンの任意の組み合わせがダイアログ内で許されます。

`style` に `'number-order` が含まれると、ボタンはダイアログ内で左から右へ、すべてのボタンのあいだに等間隔で表示されますが、ダイアログ内での揃え（中央または右揃え）はプラットフォーム固有です。`'number-order` は控えめに使ってください。

`style` リストは、どのボタン（もしあれば）が既定かを決めるため、`'default=1`、`'default=2`、`'default=3`、`'no-default` のうちちょうど一つを含まなければなりません。既定ボタンは、ユーザが Return を打ったときに「クリック」されます。`'default=n` が与えられてもボタン *n* にラベルがない場合、それは `'no-default` と等価です。

加えて、`style` に `'caution`、`'stop`、または `'no-icon` を含めて、ダイアログに現れるアイコンを `message-box` と同様に調整できます。

`return-the-dialog?` が真の値なら、ダイアログは表示されず、代わりに `message-box/custom` から返されます。ダイアログは、次の三つの追加メッセージに応答します（`send` 経由）。

- `get-message` — このメソッドは引数を取らず、メッセージのテキストを文字列として返します。
- `set-message` — このメソッドは一つの文字列引数を受け取り、ダイアログのメッセージをその引数に変更します。
- `show-and-return-results` — このメソッドは引数を取らず、ダイアログを表示します。ダイアログが閉じたあとに戻り、`return-the-dialog?` が `#false` だった場合に `message-box/custom` が返したであろう結果を返します。

ダイアログは `get-top-level-windows` 関数経由でもアクセスできます。

`message-box/custom` 関数は、関連するイベントスペース（すなわち `parent` のイベントスペース、または `parent` が `#f` なら現在のイベントスペース）のハンドラ・スレッド以外のスレッドから呼べます。その場合、ダイアログがハンドラ・スレッドで走っているあいだ、現在のスレッドはブロックします。

`dialog-mixin` 引数は、ダイアログが作られる前にダイアログを実装するクラスに適用されます。

`gui-lib` パッケージのバージョン 1.53 での変更：`return-the-dialog?` 引数と、ダイアログ・ボックスのメッセージを変更する能力を追加しました。

```
+-----------------------------------------------------------------------------+
| [procedure]                                                                 |
|                                                                             |
| (message+check-box                                                          |
| → (if/c return-the-dialog? (is-a?/c dialog%) (values (or/c 'ok 'cancel 'yes |
| 'no) boolean?))                                                             |
| (if/c return-the-dialog?                                                    |
| (is-a?/c dialog%)                                                           |
| (values (or/c 'ok 'cancel 'yes 'no) boolean?))                              |
| title: label-string?                                                       |
| message: string?                                                           |
| check-label: label-string?                                                 |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f                  |
| style: (listof (or/c 'ok 'ok-cancel 'yes-no 'caution 'stop 'no-icon        |
| 'checked)) = '(ok)                                                          |
| (listof (or/c 'ok 'ok-cancel 'yes-no                                        |
| 'caution 'stop 'no-icon 'checked))                                          |
| return-the-dialog?: any/c = #f                                             |
| dialog-mixin: (make-mixin-contract dialog%) = values                       |
|                                                                             |
| ```racket                                                                   |
| (if/c return-the-dialog?                                                    |
|       (is-a?/c dialog%)                                                     |
|       (values (or/c 'ok 'cancel 'yes 'no) boolean?))                        |
| ```                                                                         |
|                                                                             |
| ```racket                                                                   |
| (listof (or/c 'ok 'ok-cancel 'yes-no                                        |
|               'caution 'stop 'no-icon 'checked))                            |
| ```                                                                         |
+-----------------------------------------------------------------------------+
```

`message+check-box/custom` も参照してください。

`message-box` と同様ですが、次の点が異なります。

- ダイアログは、ラベルが `check-label` であるチェックボックスを含みます。
- 結果は二つの値です。`message-box` の結果と、ボックスがチェックされていたかどうかを示す真偽値。
- `style` に `'checked` を含めて、チェックボックスが最初にチェックされていることを示せます。
- `return-the-dialog?` が真の値なら、結果のオブジェクトは公開の `set-check-label` メソッドも持ちます。そのメソッドは単一の `label-string?` 引数を受け取り、チェックボックスのラベルをその文字列に設定します。

`gui-lib` パッケージのバージョン 1.53 での変更：`return-the-dialog?` 引数と、ダイアログ・ボックスのメッセージおよびチェック・ラベルを変更する能力を追加しました。

```
+-----------------------------------------------------------------------------+
| [procedure]                                                                 |
|                                                                             |
| (message+check-box/custom                                                   |
| → (or/c 1 2 3 (λ (x) (eq? x close-result)))                                 |
| title: label-string?                                                       |
| message: string?                                                           |
| check-label: label-string?                                                 |
| button1-label: (or/c label-string? (is-a?/c bitmap%) #f)                   |
| button2-label: (or/c label-string? (is-a?/c bitmap%) #f)                   |
| button3-label: (or/c label-string? (is-a?/c bitmap%) #f)                   |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f                  |
| style: (listof (or/c 'stop 'caution 'no-icon 'number-order 'disallow-close |
| 'no-default 'default=1 'default=2 'default=3)) = '(no-default)              |
| (listof (or/c 'stop 'caution 'no-icon 'number-order                         |
| 'disallow-close 'no-default                                                 |
| 'default=1 'default=2 'default=3))                                          |
| close-result: any/c = #f                                                   |
| dialog-mixin: (make-mixin-contract dialog%) = values                       |
|                                                                             |
| ```racket                                                                   |
| (listof (or/c 'stop 'caution 'no-icon 'number-order                         |
|               'disallow-close 'no-default                                   |
|               'default=1 'default=2 'default=3))                            |
| ```                                                                         |
+-----------------------------------------------------------------------------+
```

`message-box/custom` と同様ですが、次の点が異なります。

- ダイアログは、ラベルが `check-label` であるチェックボックスを含みます。
- 結果は二つの値です。`message-box` の結果と、ボックスがチェックされていたかどうかを示す真偽値。
- `style` に `'checked` を含めて、チェックボックスが最初にチェックされていることを示せます。

```
+------------------------------------------------------------+
| [procedure]                                                |
|                                                            |
| (get-text-from-user                                        |
| → (or/c string? #f)                                        |
| title: label-string?                                      |
| message: (or/c label-string? #f)                          |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f |
| init-val: string? = ""                                    |
| style: (listof (or/c 'password 'disallow-invalid)) = null |
| validate: (-> string? boolean?)                           |
| dialog-mixin: (make-mixin-contract dialog%) = values      |
+------------------------------------------------------------+
```

モーダル・ダイアログ経由でユーザからテキスト文字列を得ます。`parent` が指定されていればそれを親ウィンドウとして使います。ダイアログのタイトルは `title` です。ダイアログのテキストフィールドは `message` でラベル付けされ、`init-val` で初期化されます（ただし `init-val` はダイアログのサイズを決めません）。

ユーザがダイアログをキャンセルした場合の結果は `#f`、そうでなければユーザが与えた文字列です。

`style` に `'password` が含まれると、ダイアログのテキストフィールドは内容の各文字を実際の文字ではなく汎用の記号で描きます。

`validate` 関数は、テキストフィールドが変わるたびに、テキストフィールドの内容とともに呼ばれます。`#f` を返すと、テキストの背景がピンクに色付けされます。`style` に `'disallow-invalid` が含まれると、テキストの背景がピンクのあいだ Ok ボタンが無効化されます。

`dialog-mixin` 引数は、ダイアログが作られる前にダイアログを実装するクラスに適用されます。

```
+-----------------------------------------------------------------+
| [procedure]                                                     |
|                                                                 |
| (get-choices-from-user                                          |
| → (or/c (listof exact-nonnegative-integer?) #f)                 |
| title: label-string?                                           |
| message: (or/c label-string? #f)                               |
| choices: (listof label-string?)                                |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f      |
| init-choices: (listof exact-nonnegative-integer?) = null       |
| style: (listof (or/c 'single 'multiple 'extended)) = '(single) |
+-----------------------------------------------------------------+
```

モーダル・ダイアログ経由でユーザからリストボックスの選択を得ます。`parent` が指定されていればそれを親ウィンドウとして使います。ダイアログのタイトルは `title` です。ダイアログのリストボックスは `message` でラベル付けされ、`init-choices` 内の項目を選択することで初期化されます。

`style` は `'single`、`'multiple`、`'extended` のうちちょうど一つを含まなければなりません。スタイルの意味は `list-box%` オブジェクトを作るときと同じです。（単一選択スタイルでは、`init-choices` 内の最後の選択だけが意味を持ちます。）

ユーザがダイアログをキャンセルした場合の結果は `#f`、そうでなければ選択のリストです。

```
+------------------------------------------------------------+
| [procedure]                                                |
|                                                            |
| (get-color-from-user                                       |
| message: (or/c label-string? #f) = #f                     |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f |
| init-color: (or/c (is-a?/c color%) #f) = #f               |
| style: (listof 'alpha) = null                             |
+------------------------------------------------------------+
```

プラットフォーム固有の（モーダル）ダイアログを通じて、ユーザに色を選ばせます。`parent` が指定されていればそれを親ウィンドウとして使います。`message` 文字列は、可能ならダイアログ内のプロンプトとして表示されます。`init-color` が与えられると、ダイアログはその色で初期化されます。

ユーザがダイアログをキャンセルした場合の結果は `#f`、そうでなければ選ばれた色です。

`style` に `'alpha` が含まれると、結果の `color%` オブジェクトのアルファ・フィールドを埋めるためのフィールドがユーザに提示されます。含まれない場合、`init-color` のアルファ成分は無視され、結果のアルファは常に 1.0 です。

```
+------------------------------------------------------------+
| [procedure]                                                |
|                                                            |
| (get-font-from-user                                        |
| message: (or/c label-string? #f) = #f                     |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f |
| init-font: (or/c (is-a?/c font%) #f) = #f                 |
| style: null? = null                                       |
+------------------------------------------------------------+
```

プラットフォーム固有の（モーダル）ダイアログを通じて、ユーザにフォントを選ばせます。`parent` が指定されていればそれを親ウィンドウとして使います。`message` 文字列は、可能ならダイアログ内のプロンプトとして表示されます。`init-font` が与えられると、ダイアログはそのフォントで初期化されます。

`style` 引数は将来の拡張のために用意されています。現在、`style` は空リストでなければなりません。

ユーザがダイアログをキャンセルした場合の結果は `#f`、そうでなければ選ばれたフォントです。

```
+------------------------------------------------------------+
| [procedure]                                                |
|                                                            |
| (get-ps-setup-from-user                                    |
| → (or/c (is-a?/c ps-setup%) #f)                            |
| message: (or/c label-string? #f) = #f                     |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f |
| init-setup: (or/c (is-a?/c ps-setup%) #f) = #f            |
| style: null? = null                                       |
+------------------------------------------------------------+
```

（モーダル）ダイアログを通じて、ユーザに PostScript 設定を選ばせます。`parent` が指定されていればそれを親ウィンドウとして使います。`message` 文字列はダイアログ内のプロンプトとして表示されます。`init-setup` が与えられると、ダイアログはその設定で初期化され、そうでなければ `current-ps-setup` からの現在の設定が使われます。

`style` 引数は将来の拡張のために用意されています。現在、`style` は空リストでなければなりません。

ユーザがダイアログをキャンセルした場合の結果は `#f`、そうでなければ選ばれた PostScript 設定をカプセル化する `ps-setup%` オブジェクトです。

```
+------------------------------------------------------------+
| [procedure]                                                |
|                                                            |
| (get-page-setup-from-user                                  |
| → (or/c (is-a?/c ps-setup%) #f)                            |
| message: (or/c label-string? #f) = #f                     |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f |
| init-setup: (or/c (is-a?/c ps-setup%) #f) = #f            |
| style: null? = null                                       |
+------------------------------------------------------------+
```

`get-ps-setup-from-user` と同様ですが、ダイアログは `printer-dc%` によるネイティブ印刷のためのページ・レイアウトを設定します。`can-get-page-setup-from-user?` が `#t` を返す場合にだけダイアログが表示され、そうでなければダイアログは表示されず結果は `#f` です。

`parent` 引数は、指定されていればダイアログの親ウィンドウとして使われます。`message` 文字列はダイアログ内のプロンプトとして表示されることがあります。`init-setup` が与えられると、ダイアログはその設定で初期化され、そうでなければ `current-ps-setup` からの現在の設定が使われます。

`style` 引数は将来の拡張のために用意されています。現在、`style` は空リストでなければなりません。

ユーザがダイアログをキャンセルした場合の結果は `#f`、そうでなければ選ばれた設定をカプセル化する `ps-setup%` オブジェクトです。

```
+--------------------------------------------+
| [procedure]                                |
|                                            |
| (can-get-page-setup-from-user?) → boolean? |
+--------------------------------------------+
```

現在のプラットフォームが `printer-dc%` 印刷で使うページ・レイアウト・ダイアログをサポートするなら `#t` を返します。現在、すべてのプラットフォームがページ・レイアウト・ダイアログをサポートしています。

### 4.2 イベントスペース

```
+---------------------------------------------------------+
| [procedure]                                             |
|                                                         |
| (make-eventspace [#:suspend-to-kill? suspend-to-kill?]) |
| → eventspace?                                           |
| suspend-to-kill?: any/c = #f                           |
+---------------------------------------------------------+
```

新しいイベントスペース値を作って返します。新しいイベントスペースは、現在のイベントスペースの子として作られます。イベントスペースは、`current-eventspace` パラメータで現在のイベントスペースにすることで使われます。

`suspend-to-kill?` が `#f` でなければ、イベントスペースのハンドラ・スレッドは `thread/suspend-to-kill` を使って作られます。そうでなければ `thread` を使って作られます。

イベントスペースの詳細は、「イベントのディスパッチとイベントスペース」を参照してください。

`gui-lib` パッケージのバージョン 1.35 での変更：`suspend-to-kill?` 引数を追加しました。

```
+------------------------------------+
| [parameter]                        |
|                                    |
| (current-eventspace) → eventspace? |
| (current-eventspace e) → void?     |
| e: eventspace?                    |
+------------------------------------+
```

現在のイベントスペースを決めるパラメータ（Parameters を参照）です。

イベントスペースの詳細は、「イベントのディスパッチとイベントスペース」を参照してください。

```
+----------------------------+
| [procedure]                |
|                            |
| (eventspace? v) → boolean? |
| v: any/c                  |
+----------------------------+
```

`v` がイベントスペース値なら `#t`、そうでなければ `#f` を返します。

イベントスペースの詳細は、「イベントのディスパッチとイベントスペース」を参照してください。

```
+-----------------------------------------------------+
| [parameter]                                         |
|                                                     |
| (event-dispatch-handler) → (eventspace?. ->. any) |
| (event-dispatch-handler handler) → void?            |
| handler: (eventspace?. ->. any)                  |
+-----------------------------------------------------+
```

現在のイベント・ディスパッチ・ハンドラを決めるパラメータ（Parameters を参照）です。イベント・ディスパッチ・ハンドラは、イベントスペース内で処理されるキュー・ベースのイベントごとに、イベントスペースのハンドラ・スレッドから呼ばれます。ハンドラへの唯一の引数は、イベントがディスパッチされるべきイベントスペースです。イベント・ディスパッチ・ハンドラは、プログラマにイベント・ディスパッチのタイミングの制御を与えますが、単一のイベントスペース内でイベントがディスパッチされる順序は制御しません。

イベント・ディスパッチ・ハンドラは、最終的にプリミティブのイベント・ディスパッチ・ハンドラを呼ばなければなりません。イベント・ディスパッチ・ハンドラがプリミティブ・ハンドラを呼ばずに戻った場合、プリミティブ・ハンドラはイベントスペースのハンドラ・スレッドから直接呼ばれます。

```
+----------------------------------------+
| [procedure]                            |
|                                        |
| (eventspace-event-evt [e]) → evt?      |
| e: eventspace? = (current-eventspace) |
+----------------------------------------+
```

`e` 内で GUI イベント（マウスまたはキーボード操作、更新イベント、タイマ、キューされたコールバックなど）がディスパッチ待ちのときに準備完了となる、同期可能なイベント（`sync` を参照）を生成します。つまり、イベントスペース `e` に対する `(yield)` が GUI イベントをディスパッチするときに、結果のイベントは準備完了になります。同期結果はイベントスペース `e` 自体です。

```
+------------------------------+
| [procedure]                  |
|                              |
| (check-for-break) → boolean? |
+------------------------------+
```

現在のイベントスペースのイベント・キューを調べ、Shift-Ctl-C（Unix、Windows）または Cmd-.（Mac OS）のキー組み合わせを探します。そのようなイベントが見つかった場合（そしてイベントがデキューされた場合）は `#t`、そうでなければ `#f` を返します。

```
+------------------------------------------------------+
| [procedure]                                          |
|                                                      |
| (get-top-level-windows)                              |
| → (listof (or/c (is-a?/c frame%) (is-a?/c dialog%))) |
+------------------------------------------------------+
```

現在のイベントスペース内の、見えるトップレベル・フレームとダイアログのリストを返します。

```
+------------------------------------------------+
| [procedure]                                    |
|                                                |
| (get-top-level-focus-window)                   |
| → (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) |
+------------------------------------------------+
```

現在のイベントスペース内でキーボード・フォーカスを持つ（またはキーボード・フォーカスを持つウィンドウを含む）トップレベル・ウィンドウを返します。現在のイベントスペース内のどのウィンドウもフォーカスを持たなければ `#f` です。

```
+------------------------------------------------+
| [procedure]                                    |
|                                                |
| (get-top-level-edit-target-window)             |
| → (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) |
+------------------------------------------------+
```

現在のイベントスペース内で見え、最も最近キーボード・フォーカスを持っていた（またはキーボード・フォーカスを持っていたウィンドウを含む）トップレベル・ウィンドウを返します。現在のイベントスペース内に見えるウィンドウがなければ `#f` です。

```
+-----------------------------------+
| [procedure]                       |
|                                   |
| (special-control-key on?) → void? |
| on?: any/c                       |
| (special-control-key) → boolean?  |
+-----------------------------------+
```

後方互換性のためだけのものです。この関数は特別な Control キー処理（Mac OS）を有効または無効にすることを意図していましたが、現在は効果がありません。

```
+----------------------------------+
| [procedure]                      |
|                                  |
| (special-option-key on?) → void? |
| on?: any/c                      |
| (special-option-key) → boolean?  |
+----------------------------------+
```

特別な Option キー処理（Mac OS）を有効または無効にします。Option が特別なキーとして扱われるとき、Option キーが押されていると `get-key-code` と `get-other-altgr-key-code` の結果が実質的に入れ替わります。既定では Option は特別ではありません。

`on?` が `#f` として与えられると、キー・イベントは通常どおり報告されます。この設定はすべてのウィンドウとイベントスペースに影響します。

引数が与えられない場合、Option が現在特別に扱われていれば結果は `#t`、そうでなければ `#f` です。

```
+----------------------------------------+
| [procedure]                            |
|                                        |
| (any-control+alt-is-altgr on?) → void? |
| on?: any/c                            |
| (any-control+alt-is-altgr) → boolean?  |
+----------------------------------------+
```

任意の Control と Alt の組み合わせを AltGr（Windows）と等価として扱うことを有効または無効にします。対照的に、（両方を持つキーボード構成で）左手の Control と右手の Alt だけを AltGr として扱うこともできます。

`on?` が `#f` として与えられると、キー・イベントは通常どおり報告されます。この設定はすべてのウィンドウとイベントスペースに影響します。

引数が与えられない場合、Control と Alt が現在 AltGr として扱われていれば結果は `#t`、そうでなければ `#f` です。

`gui-lib` パッケージのバージョン 1.24 で追加されました。

```
+----------------------------------------------------+
| [procedure]                                        |
|                                                    |
| (queue-callback callback [high-priority?]) → void? |
| callback: (-> any)                                |
| high-priority?: any/c = #t                        |
+----------------------------------------------------+
```

現在のイベントスペースのイベント・キュー経由で呼ばれる手続きをインストールします。手続きは、メソッドを処理するためにコールバックが呼び出されるのと同じ仕方・同じ制約の下で一度呼ばれます。

第二の（省略可能な）真偽値引数は、コールバックがイベント・キューで高優先度か低優先度かを示します。イベントの優先度については、「イベントのディスパッチとイベントスペース」を参照してください。

```
+-----------------------+
| [procedure]           |
|                       |
| (yield) → boolean?    |
| (yield v) → any/c     |
| v: (or/c 'wait evt?) |
+-----------------------+
```

制御をイベント・ディスパッチへ譲ります。詳細は「イベントのディスパッチとイベントスペース」を参照してください。

`yield` への呼び出し中にシステムが呼び出したハンドラ手続きは、それ自体が `yield` を呼べ、入れ子の（しかしシングルスレッドの）イベント処理の追加の水準を作れます。

`sleep/yield` も参照してください。

引数が与えられない場合、`yield` は不特定の数のイベントをディスパッチしますが、それは現在のスレッドが現在のイベントスペースのハンドラ・スレッドである場合だけです（そうでなければ効果はありません）。結果は、イベントが処理された可能性があるなら `#t`、そうでなければ `#f` です。

`v` が `'wait` で、`yield` がイベントスペースのハンドラ・スレッドで呼ばれた場合、`yield` はそのイベントスペース内のイベント処理を次の条件まで開始します。

- イベントスペース内に見えるトップレベル・ウィンドウがない
- イベントスペース内で走っているタイマがない
- イベントスペース内にキューされたコールバックがない
- イベントスペースに対して `'root` で作られた `menu-bar%` がない（すなわち、`'root` メニューバーを作ると、イベントスペースは決してアンブロックしなくなります）

非ハンドラ・スレッドで呼ばれた場合、`yield` は直ちに戻ります。どちらの場合も結果は `#t` です。

したがって `(yield 'wait)` を評価することは `(yield (current-eventspace))` に似ていますが、`current-eventspace` パラメータの値ではなく、現在のスレッドがハンドラ・スレッドかどうかに敏感です。

`v` が Racket の意味でのイベント（GUI イベントと混同しないでください）である場合、`yield` は `sync` と同じ仕方で `v` 上でブロックしますが、`v` 上の sync を複数回開始することがあります（ただし `v` 上の sync を完了するのは高々一度です）。現在のスレッドが現在のイベントスペースのハンドラ・スレッドである場合、`v` の sync がイベント境界で成功するまでイベントがディスパッチされます。他のスレッドでは、Racket イベント付きで `yield` を呼ぶことは `sync` を呼ぶのと等価です。どちらの場合も結果は `sync` のそれと同じです。ただし、`handle-evt` 経由で `v` にラッパ手続きが関連付けられていても、それは `yield` に対する末尾位置では呼ばれません。

ビジーウェイト・ループの代わりに、常に `(yield v)` を使ってください。

```
+----------------------------------------+
| [procedure]                            |
|                                        |
| (sleep/yield secs) → void?             |
| secs: (and/c real? (not/c negative?)) |
+----------------------------------------+
```

少なくとも指定された秒数だけブロックし、そのあいだ、現在のスレッドが現在のイベントスペースのハンドラ・スレッドならイベントを処理します（そうでなければ、`sleep/yield` は `sleep` と等価です）。

```
+-------------------------------------+
| [procedure]                         |
|                                     |
| (eventspace-shutdown? e) → boolean? |
| e: eventspace?                     |
+-------------------------------------+
```

与えられたイベントスペースがカストディアンによってシャットダウンされていれば `#t`、そうでなければ `#f` を返します。シャットダウンされたイベントスペースで新しいウィンドウ、タイマ、または明示的にキューされたイベントを作ろうとすると、`exn:fail` 例外が発生します。

シャットダウンされたイベントスペース内のウィンドウやタイマの特定のメソッドを使おうとしても `exn:fail` 例外が発生しますが、`area<%>` の `get-top-level-window` と `top-level-window<%>` の `get-eventspace` メソッドは、領域のイベントスペースがシャットダウンされたあとも働きます。

```
+---------------------------------------------------+
| [procedure]                                       |
|                                                   |
| (eventspace-handler-thread e) → (or/c thread? #f) |
| e: eventspace?                                   |
+---------------------------------------------------+
```

与えられたイベントスペースのハンドラ・スレッドを返します。ハンドラ・スレッドが終了している場合（例：イベントスペースがシャットダウンされたため）、結果は `#f` です。

### 4.3 システムメニュー

```
+-----------------------------------------------------+
| [procedure]                                         |
|                                                     |
| (current-eventspace-has-standard-menus?) → boolean? |
+-----------------------------------------------------+
```

現在のイベントスペースが初期イベントスペースであるとき、Mac OS では `#t` を返します。そのイベントスペースが標準アプリケーション・メニューの対象だからです。他のどのシステムまたはイベントスペースでも、結果は `#f` です。

この手続きは、フレームのメニューに Quit、About、Preferences のメニュー項目を含めるかどうかを決めるときに使うことを意図しています。Mac OS では、アプリケーションの Quit メニューがフレームの `on-exit` メソッドの呼び出しを引き起こし、About メニュー項目は `application-about-handler` で制御され、Preferences メニュー項目は `application-preferences-handler` で制御されます。

```
+------------------------------------------------+
| [procedure]                                    |
|                                                |
| (current-eventspace-has-menu-root?) → boolean? |
+------------------------------------------------+
```

現在のイベントスペースが初期イベントスペースであるとき、Mac OS では `#t` を返します。そのイベントスペースは、フレームが見えていないときにアクティブになるメニューバーを供給できるからです。他のどのシステムまたはイベントスペースでも、結果は `#f` です。

この手続きは、親として `'root` を持つ `menu-bar%` インスタンスを作るかどうかを決めるときに使うことを意図しています。

```
+---------------------------------------------------+
| [procedure]                                       |
|                                                   |
| (application-about-handler) → (-> any)            |
| (application-about-handler handler-thunk) → void? |
| handler-thunk: (-> any)                          |
+---------------------------------------------------+
```

現在のイベントスペースが初期イベントスペースであるとき、この手続きは、Mac OS でユーザがアプリケーションの About メニュー項目を選んだときに呼ばれるサンクを取得またはインストールします。サンクは常に初期イベントスペースのハンドラ・スレッドで（コールバックとして）呼ばれます。

既定のハンドラは、汎用の Racket ダイアログを表示します。

現在のイベントスペースが初期イベントスペースでない場合、この手続きは（引数ゼロで呼ばれたとき）`void` を返すか、（ハンドラ付きで呼ばれたとき）効果を持ちません。

```
+-------------------------------------------------+
| [procedure]                                     |
|                                                 |
| (application-file-handler) → (path?. ->. any) |
| (application-file-handler handler-proc) → void? |
| handler-proc: (path?. ->. any)               |
+-------------------------------------------------+
```

現在のイベントスペースが初期イベントスペースであるとき、この手続きは、Mac OS と Windows でアプリケーションが走っており、ユーザがアプリケーション処理のファイルをダブルクリックしたり、アプリケーションのアイコンにファイルをドラッグしたりしたときに呼ばれる手続きを取得またはインストールします。手続きは常に初期イベントスペースのハンドラ・スレッドで（コールバックとして）呼ばれ、引数はファイル名です。

既定のハンドラは、主イベントスペース内で最も最近アクティブになったフレームの `on-drop-file` メソッドへのコールバックをキューします（`get-top-level-edit-target-window` を参照）。そのようなフレームが存在し、かつそのフレームでドラッグ・アンド・ドロップが有効な場合です。そうでなければ、ファイル名を保存し、アプリケーション・ファイル・ハンドラが後で変更されたとき、またはフレームがアクティブになったときにハンドラ・イベントを再キューします。

Windows では、アプリケーションが走っておらず、ユーザがアプリケーション処理のファイルをダブルクリックしたり、アプリケーションのアイコンにファイルをドラッグしたりした場合、ファイル名はアプリケーションへのコマンドライン引数として提供されます。

Mac OS では、アプリケーションがファイルなしで開始された場合、`application-start-empty-handler` 手続きが呼ばれます。

現在のイベントスペースが初期イベントスペースでない場合、この手続きは（引数ゼロで呼ばれたとき）`void` を返すか、（ハンドラ付きで呼ばれたとき）効果を持ちません。

```
+---------------------------------------------------------+
| [procedure]                                             |
|                                                         |
| (application-preferences-handler) → (or/c (-> any) #f)  |
| (application-preferences-handler handler-thunk) → void? |
| handler-thunk: (or/c (-> any) #f)                      |
+---------------------------------------------------------+
```

現在のイベントスペースが初期イベントスペースであるとき、この手続きは、Mac OS でユーザがアプリケーションの Preferences メニュー項目を選んだときに呼ばれるサンクを取得またはインストールします。サンクは常に初期イベントスペースのハンドラ・スレッドで（コールバックとして）呼ばれます。ハンドラが `#f` に設定されると、Preferences 項目は無効化されます。

既定のハンドラは `#f` です。

現在のイベントスペースが初期イベントスペースでない場合、この手続きは（引数ゼロで呼ばれたとき）`void` を返すか、（ハンドラ付きで呼ばれたとき）効果を持ちません。

```
+--------------------------------------------------+
| [procedure]                                      |
|                                                  |
| (application-quit-handler) → (-> any)            |
| (application-quit-handler handler-thunk) → void? |
| handler-thunk: (-> any)                         |
+--------------------------------------------------+
```

現在のイベントスペースが初期イベントスペースであるとき、この手続きは、ユーザがアプリケーションの終了を要求したとき（例：Mac OS の Quit メニュー項目経由、または Windows でマシンをシャットダウンするとき）に呼ばれるサンクを取得またはインストールします。サンクは常に初期イベントスペースのハンドラ・スレッドで（コールバックとして）呼ばれます。サンクの結果が `#f` なら、オペレーティング・システムにアプリケーションが終了する意図がないことが明示的に通知されます（Windows 上）。

既定のハンドラは、初期イベントスペース内で最も最近アクティブだったフレームの `can-exit?` メソッドへの呼び出しをキューし（結果が真ならその後フレームの `on-exit` メソッドを呼びます）。`on-exit` が戻ったあと、イベントスペースに開いたフレームが残っていなければ結果は `#t`、そうでなければ `#f` です。

現在のイベントスペースが初期イベントスペースでない場合、この手続きは（引数ゼロで呼ばれたとき）`void` を返すか、（ハンドラ付きで呼ばれたとき）効果を持ちません。

```
+---------------------------------------------------------+
| [procedure]                                             |
|                                                         |
| (application-start-empty-handler) → (-> any)            |
| (application-start-empty-handler handler-thunk) → void? |
| handler-thunk: (-> any)                                |
+---------------------------------------------------------+
```

現在のイベントスペースが初期イベントスペースであるとき、この手続きは、Mac OS でユーザが初期ファイルを供給せずにアプリケーションを開始したとき（例：アプリケーションが処理するファイルをダブルクリックする代わりに、アプリケーション・アイコンをダブルクリックしたとき）に呼ばれるサンクを取得またはインストールします。

既定のハンドラは、アプリケーションの start-empty ハンドラが後で変更されたときにハンドラ・イベントを再キューします。その結果、アプリケーションが `application-start-empty-handler` と `application-file-handler` の両方を設定すると、最終的にどちらか一方が呼ばれます。

現在のイベントスペースが初期イベントスペースでない場合、この手続きは（引数ゼロで呼ばれたとき）`void` を返すか、（ハンドラ付きで呼ばれたとき）効果を持ちません。

```
+-------------------------------------------------------+
| [procedure]                                           |
|                                                       |
| (application-dark-mode-handler) → (-> any)            |
| (application-dark-mode-handler handler-thunk) → void? |
| handler-thunk: (-> any)                              |
+-------------------------------------------------------+
```

現在のイベントスペースが初期イベントスペースであるとき、この手続きは、Mac OS で OS がダークモードに切り替わったりダークモードから戻ったりしたときに呼ばれるサンクを取得またはインストールします。`white-on-black-panel-scheme?` も参照してください。

既定のハンドラは何もしません。

現在のイベントスペースが初期イベントスペースでない場合、この手続きは（引数ゼロで呼ばれたとき）`void` を返すか、（ハンドラ付きで呼ばれたとき）効果を持ちません。

`gui-lib` パッケージのバージョン 1.68 で追加されました。

### 4.4 グローバル・グラフィックス

```
+-------------------------+
| [procedure]             |
|                         |
| (flush-display) → void? |
+-------------------------+
```

キャンバスのオフスクリーン描画や他の更新を画面へフラッシュします。

通常、描画は自動的に画面へフラッシュされます。表示の更新に他の操作が依存するときに画面への更新を強制するため、`flush-display` は控えめに使ってください。

```
+-------------------------------------------------+
| [procedure]                                     |
|                                                 |
| (get-display-backing-scale [#:monitor monitor]) |
| → (or/c (>/c 0.0) #f)                           |
| monitor: exact-nonnegative-integer? = 0        |
+-------------------------------------------------+
```

モニタ上で一つの描画単位に対応するピクセル数を返します。結果は通常 1.0 ですが、Mac OS の Retina 表示モードでは 2.0 で、Windows または Unix ではオペレーティング・システムのテキスト・スケールが変更されているときに 1.25、1.5、2.0 などの値になり得ます。「画面解像度とテキストのスケーリング」も参照してください。

Mac OS または Unix では、結果はいつでも変わり得ます。`top-level-window<%>` の `display-changed` も参照してください。

`monitor` が現在利用可能なモニタ数（いつでも変わり得る）未満でなければ、結果は `#f` です。`top-level-window<%>` の `display-changed` も参照してください。

`gui-lib` パッケージのバージョン 1.2 での変更：Windows での backing-scale サポートを追加しました。

```
+-----------------------------------------------+
| [procedure]                                   |
|                                               |
| (get-display-count) → exact-positive-integer? |
+-----------------------------------------------+
```

現在アクティブなモニタの数を返します。

Windows と Mac OS では、結果はいつでも変わり得ます。`top-level-window<%>` の `display-changed` も参照してください。

```
+--------------------------------------------------+
| [procedure]                                      |
|                                                  |
| (get-display-depth) → exact-nonnegative-integer? |
+--------------------------------------------------+
```

主ディスプレイの深さ（値 1 はモノクロ・ディスプレイを表す）を返します。

```
+-------------------------------------------------------------------------------+
| [procedure]                                                                   |
|                                                                               |
| (get-display-left-top-inset                                                   |
| → (if (= monitor 0) exact-nonnegative-integer? (or/c                          |
| exact-nonnegative-integer? #f))(if (= monitor 0) exact-nonnegative-integer?   |
| (or/c exact-nonnegative-integer? #f))                                         |
| (if (= monitor 0) exact-nonnegative-integer? (or/c exact-nonnegative-integer? |
| #f))                                                                          |
| (if (= monitor 0)                                                             |
| exact-nonnegative-integer?                                                    |
| (or/c exact-nonnegative-integer? #f))                                         |
| (if (= monitor 0) exact-nonnegative-integer? (or/c exact-nonnegative-integer? |
| #f))                                                                          |
| (if (= monitor 0)                                                             |
| exact-nonnegative-integer?                                                    |
| (or/c exact-nonnegative-integer? #f))                                         |
| avoid-bars?: any/c = #f                                                      |
| monitor: exact-nonnegative-integer? = 0                                      |
|                                                                               |
| ```racket                                                                     |
| (if (= monitor 0)                                                             |
|     exact-nonnegative-integer?                                                |
|     (or/c exact-nonnegative-integer? #f))                                     |
| ```                                                                           |
|                                                                               |
| ```racket                                                                     |
| (if (= monitor 0)                                                             |
|     exact-nonnegative-integer?                                                |
|     (or/c exact-nonnegative-integer? #f))                                     |
| ```                                                                           |
+-------------------------------------------------------------------------------+
```

省略可能な引数が `#f`（既定）のとき、この関数は物理モニタの左上からの `monitor` の原点のオフセットを返します。モニタ 0 については、Unix と Windows では結果は常に 0 と 0 です。Mac OS では結果は 0 とメニューバーの高さです。フレームを与えられたモニタの左上隅に位置決めするには、`get-display-left-top-inset` の結果の符号を反転したものをフレームの位置として使います。

省略可能な `avoid-bars?` 引数が真のとき、モニタ 0 について `get-display-left-top-inset` 関数は、タスクバー（Windows）またはメニューバーとドック（Mac OS）が占めるモニタ左と上の空間の量を返します。Unix では、モニタ 0 について結果は常に 0 と 0 です。モニタ 0 以外では、`avoid-bars?` は効果を持ちません。

`monitor` が現在利用可能なモニタ数（いつでも変わり得る）未満でなければ、結果は `#f` と `#f` です。`top-level-window<%>` の `display-changed` も参照してください。

「画面解像度とテキストのスケーリング」も参照してください。

```
+-------------------------------------------------------------------------------+
| [procedure]                                                                   |
|                                                                               |
| (get-display-size                                                             |
| → (if (= monitor 0) exact-nonnegative-integer? (or/c                          |
| exact-nonnegative-integer? #f))(if (= monitor 0) exact-nonnegative-integer?   |
| (or/c exact-nonnegative-integer? #f))                                         |
| (if (= monitor 0) exact-nonnegative-integer? (or/c exact-nonnegative-integer? |
| #f))                                                                          |
| (if (= monitor 0)                                                             |
| exact-nonnegative-integer?                                                    |
| (or/c exact-nonnegative-integer? #f))                                         |
| (if (= monitor 0) exact-nonnegative-integer? (or/c exact-nonnegative-integer? |
| #f))                                                                          |
| (if (= monitor 0)                                                             |
| exact-nonnegative-integer?                                                    |
| (or/c exact-nonnegative-integer? #f))                                         |
| full-screen?: any/c = #f                                                     |
| monitor: exact-nonnegative-integer? = 0                                      |
|                                                                               |
| ```racket                                                                     |
| (if (= monitor 0)                                                             |
|     exact-nonnegative-integer?                                                |
|     (or/c exact-nonnegative-integer? #f))                                     |
| ```                                                                           |
|                                                                               |
| ```racket                                                                     |
| (if (= monitor 0)                                                             |
|     exact-nonnegative-integer?                                                |
|     (or/c exact-nonnegative-integer? #f))                                     |
| ```                                                                           |
+-------------------------------------------------------------------------------+
```

指定されたモニタの物理サイズをピクセル単位で得ます。Windows では、既定でこのサイズにタスクバーは含まれません。Mac OS では、既定でこのサイズにメニューバーやドック領域は含まれません。

Windows と Mac OS では、省略可能な引数が真で `monitor` が 0 なら、タスクバー、メニューバー、ドック領域が結果に含まれます。

`monitor` が現在利用可能なモニタ数（いつでも変わり得る）未満でなければ、結果は `#f` と `#f` です。`top-level-window<%>` の `display-changed` も参照してください。

「画面解像度とテキストのスケーリング」も参照してください。

```
+--------------------------------+
| [procedure]                    |
|                                |
| (is-color-display?) → boolean? |
+--------------------------------+
```

主ディスプレイがカラーなら `#t`、そうでなければ `#f` を返します。

### 4.5 フォント

```
+-------------------------------------+
| [value]                             |
|                                     |
| menu-control-font: (is-a?/c font%) |
+-------------------------------------+
```

このフォントは `popup-menu%` オブジェクトの既定です。

Mac OS では、このフォントは `normal-control-font` よりわずかに大きいです。Windows と Unix では、`normal-control-font` と同じサイズです。

```
+---------------------------------------+
| [value]                               |
|                                       |
| normal-control-font: (is-a?/c font%) |
+---------------------------------------+
```

このフォントは、`list-box%` と `group-box-panel%` オブジェクトを除く、ほとんどのコントロールの既定です。

```
+--------------------------------------+
| [value]                              |
|                                      |
| small-control-font: (is-a?/c font%) |
+--------------------------------------+
```

このフォントは `group-box-panel%` オブジェクトの既定であり、フローティング・ウィンドウや、より小さなコントロールを必要とする他の文脈でのコントロールにも適しています。

Windows では、Windows のコントロール・フォントがすでに比較的小さいため、このフォントは `normal-control-font` と同じサイズです。Unix と Mac OS では、このフォントは `normal-control-font` よりわずかに小さいです。

```
+-------------------------------------+
| [value]                             |
|                                     |
| tiny-control-font: (is-a?/c font%) |
+-------------------------------------+
```

このフォントはごく小さなコントロール用で、すべてのプラットフォームで `small-control-font` より小さいです。

```
+-------------------------------------+
| [value]                             |
|                                     |
| view-control-font: (is-a?/c font%) |
+-------------------------------------+
```

このフォントは `list-box%` オブジェクトの既定です（ただしリストボックスのラベルは `normal-control-font` を使います）。

Mac OS では、このフォントは `normal-control-font` よりわずかに小さく、`small-control-font` よりわずかに大きいです。Windows と Unix では、`normal-control-font` と同じサイズです。

### 4.6 その他

```
+-----------------------------+
| [procedure]                 |
|                             |
| (begin-busy-cursor) → void? |
+-----------------------------+
```

現在のイベントスペース内のすべてのウィンドウのカーソルをウォッチ・カーソルに変更します。`end-busy-cursor` を使ってカーソルを以前の状態に戻します。`begin-busy-cursor` と `end-busy-cursor` への呼び出しは、任意に入れ子にできます。

`begin-busy-cursor` がインストールするカーソルは、`set-cursor` でインストールされたウィンドウ固有のカーソルを上書きします。

`is-busy?` も参照してください。

```
+----------------------+
| [procedure]          |
|                      |
| (bell) → void?       |
+----------------------+
```

システム・ベルを鳴らします。

```
+-----------------------------------+
| [procedure]                       |
|                                   |
| (dimension-integer? v) → boolean? |
| v: any/c                         |
+-----------------------------------+
```

`(integer-in 0 1000000)` と等価です。

一部のプラットフォームでは、どちらかの次元が約 32,000 より大きいウィンドウの特定の種類が悪く振る舞うことに注意してください。たとえば、ウィンドウの再描画が無効化されたり切り詰められたりすることがあります。

```
+---------------------------+
| [procedure]               |
|                           |
| (end-busy-cursor) → void? |
+---------------------------+
```

`begin-busy-cursor` を参照してください。

```
+-----------------------------------------------------------------------------+
| [procedure]                                                                 |
|                                                                             |
| (file-creator-and-type                                                      |
| filename: path?                                                            |
| creator-bytes: (and/c bytes? #rx#"^....$")                                 |
| type-bytes: (and/c bytes? #rx#"^....$")                                    |
| (file-creator-and-type filename) → (and/c bytes? #rx#"^....$")(and/c bytes? |
| #rx#"^....$")                                                               |
| (file-creator-and-type filename)                                            |
| (and/c bytes? #rx#"^....$")                                                 |
| (and/c bytes? #rx#"^....$")                                                 |
| filename: path?                                                            |
+-----------------------------------------------------------------------------+
```

Mac OS でファイルのクリエータとタイプを取得または設定します。

取得操作は、Unix または Windows では常に `#"????"` と `#"????"` を返します。設定操作は Unix または Windows では効果を持ちません。

```
+-----------------------------------------------------+
| [procedure]                                         |
|                                                     |
| (find-graphical-system-path what) → (or/c path? #f) |
| what: (or/c 'init-file 'x-display)                 |
+-----------------------------------------------------+
```

プラットフォーム固有の（および場合によりユーザまたはマシン固有の）標準ファイル名またはディレクトリを探します。`find-system-path` も参照してください。

結果は `what` に依存し、`#f` の結果は `what` が `'x-display` のときだけ可能です。

- `'init-file` は、ユーザ固有の初期化ファイル（Racket コードを含む）へのパスを返します。パスのディレクトリ部分は、Racket の `find-system-path` が `'init-dir` に対して返すのと同じパスです。ファイル名はプラットフォーム固有です。
  - Unix と Mac OS：`".gracketrc"`
  - Windows：`"gracketrc.rktl"`
- `'x-display` は、Unix で GRacket が開始するときに `-display` フラグまたは `DISPLAY` 環境変数で指定された X11 ディスプレイを識別する文字列を持つ「パス」を返します。他のプラットフォーム、または `-display` も `DISPLAY` も指定されていない場合、結果は `#f` です。

```
+--------------------------------------------------------------------------+
| [procedure]                                                              |
|                                                                          |
| (get-default-shortcut-prefix)                                            |
| → (case (system-type) [(windows) (list/c 'ctl)] [(macosx) (list/c 'cmd)] |
| [(unix) (list/c (or/c 'alt 'cmd 'meta 'ctl 'shift 'option))])            |
| (case (system-type)                                                      |
| [(windows) (list/c 'ctl)]                                                |
| [(macosx) (list/c 'cmd)]                                                 |
| [(unix) (list/c (or/c 'alt 'cmd 'meta 'ctl 'shift 'option))])            |
|                                                                          |
| ```racket                                                                |
| (case (system-type)                                                      |
|   [(windows) (list/c 'ctl)]                                              |
|   [(macosx)  (list/c 'cmd)]                                              |
|   [(unix)    (list/c (or/c 'alt 'cmd 'meta 'ctl 'shift 'option))])       |
| ```                                                                      |
+--------------------------------------------------------------------------+
```

メニュー・ショートカットの既定の接頭辞を指定する不変リストを返します。`selectable-menu-item<%>` の `get-shortcut-prefix` も参照してください。

Windows では既定は `'(ctl)` です。Mac OS では既定は `'(cmd)` です。Unix では既定は通常 `'(ctl)` ですが、`'GRacket:defaultMenuPrefix` 環境設定の低水準設定（Preferences を参照）で変更できます。

```
+-------------------------------------------+
| [procedure]                               |
|                                           |
| (get-panel-background) → (is-a?/c color%) |
+-------------------------------------------+
```

灰色の色合いを返します。

歴史的には、結果は `panel%` の背景の色と一致していましたが、一部のプラットフォームでは `panel%` の背景が変わり得るため（例：`group-box-panel%` に入れ子になったとき）、結果が `panel%` の色と関係していることはもはや保証されません。

パネル背景により近い近似については、`get-label-background-color` を参照してください。

```
+-----------------------------------------------------+
| [procedure]                                         |
|                                                     |
| (get-highlight-background-color) → (is-a?/c color%) |
+-----------------------------------------------------+
```

選択されたテキストの背後に描かれる色を返します。

```
+---------------------------------------------------------+
| [procedure]                                             |
|                                                         |
| (get-highlight-text-color) → (or/c (is-a?/c color%) #f) |
+---------------------------------------------------------+
```

選択されたテキストを描くために使われる色を返すか、選択されたテキストが通常の色で描かれる場合は `#f` を返します。

```
+-------------------------------------------------+
| [procedure]                                     |
|                                                 |
| (get-label-background-color) → (is-a?/c color%) |
+-------------------------------------------------+
```

コントロール・ラベルの背後に現れそうな色の近似を返します。一部のプラットフォームのテーマは文脈によって色を変えるため、この色はコントロールの背景の実際の色と一致しないことがあります。

`get-label-foreground-color` も参照してください。

`gui-lib` パッケージのバージョン 1.38 で追加されました。

```
+-------------------------------------------------+
| [procedure]                                     |
|                                                 |
| (get-label-foreground-color) → (is-a?/c color%) |
+-------------------------------------------------+
```

コントロール・ラベルのテキストに使われそうな色の近似を返します。一部のプラットフォームのテーマは文脈によって色を変えるため、この色はラベル・テキストの実際の色と一致しないことがあります。

`get-label-foreground-color` と `get-label-background-color` の結果を比較することは、プラットフォームの現在のテーマが「ダークモード」か「ライトモード」かを検出するのに役立ち得ます。

`gui-lib` パッケージのバージョン 1.38 で追加されました。

```
+----------------------------+
| [procedure]                |
|                            |
| (get-window-text-extent    |
| exact-nonnegative-integer? |
| exact-nonnegative-integer? |
| string: string?           |
| font: (is-a?/c font%)     |
| combine?: any/c = #f      |
+----------------------------+
```

与えられたフォントで描かれたときの、ウィンドウのラベルまたは値としての文字列のピクセル・サイズを返します。省略可能な `combine?` 引数は、`dc<%>` の `get-text-extent` と同様です。

`dc<%>` の `get-text-extent` も参照してください。

```
+-------------------------------------------------+
| [procedure]                                     |
|                                                 |
| (graphical-read-eval-print-loop                 |
| eval-eventspace: (or/c eventspace? #f) = #f    |
| redirect-ports?: any/c = (not eval-eventspace) |
+-------------------------------------------------+
```

`read-eval-print-loop` に似ていますが、`read-eval-print-loop` の設定パラメータ（`current-read` など）はどれも使われず、対話は現在の入力・出力ポートではなく GUI ウィンドウで行われます。

グラフィカルな read-eval-print ループに入力された式は、`graphical-read-eval-print-loop` ウィンドウを実装するのとは別のイベントスペース（とスレッド）で評価できます（すなわち、`graphical-read-eval-print-loop` が呼ばれたときの現在のイベントスペースとは別です）。

イベントスペースが与えられない、または `#f` が与えられる場合、評価用イベントスペースは新しいカストディアンとともに `(make-eventspace)` を使って作られます。ユーザが `graphical-read-eval-print-loop` ウィンドウを閉じると、イベントスペースとそのスレッドはシャットダウンされます。イベントスペースが与えられた場合、ウィンドウを閉じてもイベントスペースに対するシャットダウン操作は行われません。

`redirect-ports?` が真のとき、作られたイベントスペースのハンドラ・スレッドで次のパラメータが初期化されます。

- `current-output-port` — フレームへ書く
- `current-error-port` — フレームへ書く
- `current-input-port` — 常に eof を返す

read-eval-print ループのエディタのキーマップは、現在のキーマップ初期化手続き——`current-text-keymap-initializer` パラメータが決めるもの——を呼ぶことで初期化されます。

```
+-----------------------------------+
| [procedure]                       |
|                                   |
| (graphical-system-type) → symbol? |
+-----------------------------------+
```

`racket/gui` が走っているプラットフォーム・ネイティブ GUI 層を示すシンボルを返します。現在可能な値は次のとおりです。

- `'win32`（Windows）
- `'cocoa`（Mac OS）
- `'gtk2` — GTK+ バージョン 2
- `'gtk3` — GTK+ バージョン 3

`gui-lib` パッケージのバージョン 1.15 で追加されました。

```
+----------------------------------------+
| [procedure]                            |
|                                        |
| (textual-read-eval-print-loop) → void? |
+----------------------------------------+
```

`read-eval-print-loop` に似ていますが、評価は `graphical-read-eval-print-loop` のように新しく作られたイベントスペースを使います。

`current-prompt-read` パラメータが現在のスレッドで入力の読み取りに使われます。結果は、作られたイベントスペースのハンドラ・スレッドでの評価と表示のためにキューされ、そこでは `current-eval` と `current-print` が使われます。対話結果の表示が完了したあと、元のスレッドで次の式が読まれ、以下同様です。

読み取り中に元のスレッドで `exn:break` 例外が発生すると、現在の `(current-read)` への呼び出しを中断し、新しいものが開始されます。対話の完了を待っているあいだに元のスレッドで `exn:break` 例外が発生すると、作られたイベントスペースのハンドラ・スレッドへ（`break-thread` 経由で）break が送られます。

```
+---------------------------------------------------------------------------+
| [procedure]                                                               |
|                                                                           |
| (get-current-mouse-state)                                                 |
| → (is-a?/c point%)(listof (or/c 'left 'middle 'right 'shift 'control 'alt |
| 'meta 'caps))                                                             |
| (is-a?/c point%)                                                          |
| (listof (or/c 'left 'middle 'right 'shift 'control 'alt 'meta 'caps))     |
| (listof (or/c 'left 'middle 'right                                        |
| 'shift 'control 'alt 'meta 'caps))                                        |
|                                                                           |
| ```racket                                                                 |
| (listof (or/c 'left 'middle 'right                                        |
|               'shift 'control 'alt 'meta 'caps))                          |
| ```                                                                       |
+---------------------------------------------------------------------------+
```

> **注:** Mac OS 10.5 以前では、マウスボタン情報は利用できないため、第二の結果には修飾キーのシンボルだけが含まれます。

画面座標でのマウスの現在位置を返し、現在押されているマウスボタンと修飾キーのシンボルのリストを返します。

```
+-----------------------------------+
| [procedure]                       |
|                                   |
| (hide-cursor-until-moved) → void? |
+-----------------------------------+
```

ユーザがマウスを動かすかマウスボタンをクリックするまでカーソルを隠します。（一部のプラットフォームでは、カーソルが別のイベントスペースまたはアプリケーション内のウィンドウの上にある場合、カーソルは隠されません。）

```
+-----------------------+
| [procedure]           |
|                       |
| (is-busy?) → boolean? |
+-----------------------+
```

ビジー・カーソルが `begin-busy-cursor` でインストールされ、`end-busy-cursor` で取り除かれていなければ `#t` を返します。

```
+--------------------------------------+
| [procedure]                          |
|                                      |
| (label->plain-label label) → string? |
| label: string?                      |
+--------------------------------------+
```

`label` からショートカットのアンパサンドを取り除き、括弧付きのアンパサンド–文字の組み合わせと周囲の空白を削除し、タブ以降を削除します。全体として、ニーモニックをサポートしないプラットフォーム上のボタンに現れるであろうラベルを返します。

```
+----------------------------------------------------------+
| [procedure]                                              |
|                                                          |
| (make-gl-bitmap width height config) → (is-a?/c bitmap%) |
| width: exact-positive-integer?                          |
| height: exact-positive-integer?                         |
| config: (is-a?/c gl-config%)                            |
+----------------------------------------------------------+
```

通常の `dc<%>` 描画と、`dc<%>` の `get-gl-context` が返すコンテキスト経由の OpenGL 描画の両方をサポートするビットマップを作ります。

`dc<%>` 描画については、OpenGL 対応ビットマップは一部のプラットフォームでは `make-screen-bitmap` からのビットマップのように描画し、他のプラットフォームでは `bitmap%` から直接インスタンス化されたビットマップのように描画します。

Unix システムでは、GLX がビットマップへの OpenGL 描画に間接レンダリングを選ぶことがあり、機能が OpenGL 1.4 以下に制限され得ることに注意してください。

```
+-----------------------------------------+
| [procedure]                             |
|                                         |
| (make-gui-empty-namespace) → namespace? |
+-----------------------------------------+
```

`make-base-empty-namespace` と同様ですが、結果の名前空間に `racket/class` と `racket/gui/base` もアタッチされます。

```
+-----------------------------------+
| [procedure]                       |
|                                   |
| (make-gui-namespace) → namespace? |
+-----------------------------------+
```

`make-base-namespace` と同様ですが、結果の名前空間のトップレベル環境に `racket/class` と `racket/gui/base` も require されます。

```
+-------------------------------------------------------+
| [procedure]                                           |
|                                                       |
| (make-screen-bitmap width height) → (is-a?/c bitmap%) |
| width: exact-positive-integer?                       |
| height: exact-positive-integer?                      |
+-------------------------------------------------------+
```

既定構成のキャンバスへの描画と同じ仕方で描画するビットマップを作ります。

特に、Mac OS で主モニタが Retina 表示モードのとき、一つの描画単位は二つのピクセルに対応し、ビットマップ内部には `width` と `height` が要求する四倍のピクセルが含まれます。Windows では、オペレーティング・システムのテキスト・スケールを調整することでバッキング・スケールが同様に増加します。`get-display-backing-scale` も参照してください。

Portability and Bitmap Variants も参照してください。

```
+-----------------------------------------+
| [procedure]                             |
|                                         |
| (play-sound filename async?) → boolean? |
| filename: path-string?                 |
| async?: any/c                          |
+-----------------------------------------+
```

サウンド・ファイルを再生します。`async?` が偽なら、関数はサウンドが完了するまで戻りません。そうでなければ直ちに戻ります。結果は、サウンドが正常に再生されれば `#t`、そうでなければ `#f` です。

Windows では、サウンドの再生に MCI が使われるため、`".wav"` や `".mp3"` などのファイル形式がサポートされるはずです。

Mac OS では、サウンドの再生に Quicktime が使われます。最近の版の Quicktime では、ほとんどのサウンド形式（`".wav"`、`".aiff"`、`".mp3"`）がサポートされます。`".wav"` ファイルを再生するには、Quicktime 3.0（OS 7.5 以降と互換）が必要です。

Unix では、関数は外部のサウンド再生プログラムを呼び出します——既定では既知のいくつかのプログラム（`paplay`、`aplay`、`play`、`esdplay`、`sndfile-play`、`audioplay`）を探します。再生コマンドは `'GRacket:playcmd` 環境設定（Preferences を参照）で定義できます。環境設定はプログラム名、またはファイル名が置換されるべき単一の `~a` を含む書式文字列——シェル・コマンドとして使われる——を保持できます。（書式文字列とともに使われる文字列は適切にクォートされ二重引用符で包まれるため、`~s` は使わないでください。）実行が速いため、通常はプレーンなコマンド名のほうがよいです。コマンドの出力は捨てられますが、エラー・コードを返す場合はエラー出力の最後の部分が表示されます。

`gui-lib` パッケージのバージョン 1.22 での変更：Windows で、同時に複数のサウンドをサポートし、`".mp3"` などのファイル形式のサポートを追加しました。

```
+----------------------------------+
| [procedure]                      |
|                                  |
| (position-integer? v) → boolean? |
| v: any/c                        |
+----------------------------------+
```

`(integer-in -1000000 1000000)` と等価です。

```
+--------------------------------------------+
| [procedure]                                |
|                                            |
| (positive-dimension-integer? v) → boolean? |
| v: any/c                                  |
+--------------------------------------------+
```

`(integer-in 1 1000000)` と等価です。

```
+----------------------------+
| [procedure]                |
|                            |
| (register-collecting-blit  |
| canvas: (is-a?/c canvas%) |
| x: position-integer?      |
| y: position-integer?      |
| w: dimension-integer?     |
| h: dimension-integer?     |
| on: (is-a?/c bitmap%)     |
| off: (is-a?/c bitmap%)    |
| on-x: real? = 0           |
| on-y: real? = 0           |
| off-x: real? = 0          |
| off-y: real? = 0          |
+----------------------------+
```

ガベージ・コレクションの開始時と終了時に起こる「ブリット」を登録します。ガベージ・コレクションが開始すると、`canvas` が見えていれば、`canvas` 内の位置 `x` と `y` に `on` が描かれます。ガベージ・コレクションが終了すると、描画は元に戻されます。一部のプラットフォームでは描画は `off` ビットマップを描くことで元に戻され、一部のプラットフォームでは `off` ビットマップを必要とせずに自動的に元に戻されます。

`on` の背後の背景はキャンバスの通常の内容であるかどうかわからないため、`on` はソリッドな画像であるべきです。ビットマップを描くとき、キャンバスのスケールもスクロール位置も適用されません。`w` と `h` ピクセル内の `on` の部分だけが使われます。`on-x` と `on-y` が指定されていれば、描画に使われるビットマップ内のオフセットを指定します。同様に `off-x` と `off-y` は `off` 内のオフセットを指定します。

`canvas` が見えなくなりアクセス不能になると、ブリットは自動的に登録解除されます。同じキャンバスに複数の登録をインストールできます。

`unregister-collecting-blit` も参照してください。

```
+---------------------------------------------+
| [procedure]                                 |
|                                             |
| (unregister-collecting-blit canvas) → void? |
| canvas: (is-a?/c canvas%)                  |
+---------------------------------------------+
```

`register-collecting-blit` で `canvas` にインストールされたすべてのブリット要求を登録解除します。

```
+----------------------------------------------+
| [procedure]                                  |
|                                              |
| (send-message-to-window x y message) → any/c |
| x: position-integer?                        |
| y: position-integer?                        |
| message: any/c                              |
+----------------------------------------------+
```

大域座標 `(x, y)` にある最前面のトップレベル・ウィンドウを探します。ウィンドウがあれば、この関数はウィンドウの `on-message` メソッドを呼び、`message` をメソッドの引数として与えます。関数呼び出しの結果は、メソッドが返した結果です。与えられた座標に Racket ウィンドウがない、または `(x, y)` で非 Racket ウィンドウに覆われている場合、`#f` が返されます。

```
+---------------------------------+
| [procedure]                     |
|                                 |
| (spacing-integer? v) → boolean? |
| v: any/c                       |
+---------------------------------+
```

`(integer-in 0 1000)` と等価です。

```
+------------------------------------------------+
| [procedure]                                    |
|                                                |
| (system-position-ok-before-cancel?) → boolean? |
+------------------------------------------------+
```

Windows では `#t` を返します——OK と Cancel ボタンを持つダイアログは、OK ボタンを Cancel ボタンの左に置くべきであることを示します——Mac OS と Unix では `#f` を返します。

```
+----------------------------------------+
| [value]                                |
|                                        |
| the-clipboard: (is-a?/c clipboard<%>) |
+----------------------------------------+
```

`clipboard<%>` を参照してください。

```
+----------------------------------------------------+
| [value]                                            |
|                                                    |
| the-x-selection-clipboard: (is-a?/c clipboard<%>) |
+----------------------------------------------------+
```

`clipboard<%>` を参照してください。

```
+------------------------------+
| [procedure]                  |
|                              |
| (label-string? v) → boolean? |
| v: any/c                    |
+------------------------------+
```

`v` が長さ 200 以下の文字列なら `#t` を返します。

この述語は通常、GUI オブジェクトに現れる文字列の契約として使われます。`button%` や `menu-item%` オブジェクトのラベルなど、一部の場合では、文字 `&` は次の文字がキーボード・ナビゲーションに使われることを示すために特別に扱われます。そのような例の一つとして、`labelled-menu-item<%>` の `set-label` を参照してください。`frame%` のラベルなど他の場合では、`&` は特別に扱われません。

```
+---------------------------------+
| [procedure]                     |
|                                 |
| (key-code-symbol? v) → boolean? |
| v: any/c                       |
+---------------------------------+
```

引数が、`key-event%` のメソッド `get-key-code` が返し得るシンボルなら `#t` を返します。
