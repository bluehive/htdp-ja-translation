# 付録 D（続き）: GUI クラス参照（16–25）

以下は `extracted/appendix/gui/original_markdown_16` 〜 `25` の日本語訳です。

---

## add-color<%>

```
+------------------------------------+
| interfaceadd-color<%>: interface? |
+------------------------------------+
+------------------------------------+
```

`add-color<%>` オブジェクトは、`color%` オブジェクトの RGB 値を加算的に変更するために使います。`add-color<%>` オブジェクトは `style-delta%` オブジェクトの内部にのみ存在します。

`get-foreground-add` および `get-background-add` も参照してください。

```
+-------------------------------------------+
| [メソッド]                                |
|                                           |
| (send an-add-color get r g b [a]) → void? |
| r: (box/c (integer-in -1000 1000))       |
| g: (box/c (integer-in -1000 1000))       |
| b: (box/c (integer-in -1000 1000))       |
| a: (or/c (box/c real?) #f) = #f          |
+-------------------------------------------+
```

すべての加算値を取得します。

`r` ボックスには色の赤成分の加算値が格納されます。
`g` ボックスには色の緑成分の加算値が格納されます。
`b` ボックスには色の青成分の加算値が格納されます。
`a` が `#f` でない限り、`a` ボックスには色のアルファ成分の加算値が格納されます。

パッケージ `snip-lib` のバージョン 1.63 で変更: 省略可能な引数 `a` を追加。

```
+-----------------------------------+
| [メソッド]                        |
|                                   |
| (send an-add-color get-a) → real? |
+-----------------------------------+
```

色のアルファ成分の加算値を取得します。

パッケージ `snip-lib` のバージョン 1.63 で追加。

```
+-----------------------------------------------------+
| [メソッド]                                          |
|                                                     |
| (send an-add-color get-b) → (integer-in -1000 1000) |
+-----------------------------------------------------+
```

色の青成分の加算値を取得します。

```
+-----------------------------------------------------+
| [メソッド]                                          |
|                                                     |
| (send an-add-color get-g) → (integer-in -1000 1000) |
+-----------------------------------------------------+
```

色の緑成分の加算値を取得します。

```
+-----------------------------------------------------+
| [メソッド]                                          |
|                                                     |
| (send an-add-color get-r) → (integer-in -1000 1000) |
+-----------------------------------------------------+
```

色の赤成分の加算値を取得します。

```
+-------------------------------------------+
| [メソッド]                                |
|                                           |
| (send an-add-color set r g b [a]) → void? |
| r: (integer-in -1000 1000)               |
| g: (integer-in -1000 1000)               |
| b: (integer-in -1000 1000)               |
| a: real? = 0.0                           |
+-------------------------------------------+
```

すべての加算値を設定します。

パッケージ `snip-lib` のバージョン 1.63 で変更: 省略可能な引数 `a` を追加。

```
+-------------------------------------+
| [メソッド]                          |
|                                     |
| (send an-add-color set-a v) → void? |
| v: real?                           |
+-------------------------------------+
```

色のアルファ成分の加算値を設定します。

パッケージ `snip-lib` のバージョン 1.63 で追加。

```
+-------------------------------------+
| [メソッド]                          |
|                                     |
| (send an-add-color set-b v) → void? |
| v: (integer-in -1000 1000)         |
+-------------------------------------+
```

色の青成分の加算値を設定します。

```
+-------------------------------------+
| [メソッド]                          |
|                                     |
| (send an-add-color set-g v) → void? |
| v: (integer-in -1000 1000)         |
+-------------------------------------+
```

色の緑成分の加算値を設定します。

```
+-------------------------------------+
| [メソッド]                          |
|                                     |
| (send an-add-color set-r v) → void? |
| v: (integer-in -1000 1000)         |
+-------------------------------------+
```

色の赤成分の加算値を設定します。

---

## area-container-window<%>

```
+------------------------------------------------+-------------------+
| interfacearea-container-window<%>: interface? |                   |
+------------------------------------------------+-------------------+
| implements:                                    | area-container<%> |
|                                                | window<%>         |
+------------------------------------------------+-------------------+
```

二つのインタフェースを組み合わせます。

---

## area-container<%>

```
+-----------------------------------------+---------+
| interfacearea-container<%>: interface? |         |
+-----------------------------------------+---------+
| implements:                             | area<%> |
+-----------------------------------------+---------+
```

`area-container<%>` はコンテナとしての `area<%>` です。

すべての `area-container<%>` クラスは、次の名前付き生成引数を受け付けます。

- `border` — 既定値は `0`。`border` に渡される
- `spacing` — 既定値は `0`。`spacing` に渡される
- `alignment` — 既定値はクラス固有（例: `vertical-panel%` では `'(center top)`）。リストの各要素は `set-alignment` に渡される

```
+--------------------------------------------------+
| [メソッド]                                       |
|                                                  |
| (send an-area-container add-child child) → void? |
| child: (is-a?/c subwindow<%>)                   |
+--------------------------------------------------+
```

与えられたサブウィンドウを、削除されていない子の集合に追加します。`change-children` も参照してください。

```
+--------------------------------------------------------+
| [メソッド]                                             |
|                                                        |
| (send an-area-container after-new-child child) → void? |
| child: (is-a?/c subarea<%>)                           |
+--------------------------------------------------------+
```

仕様:
この領域をコンテナとして新しい被包含領域が生成された後に呼ばれます。新しい子がメソッドの引数として渡されます。

既定の実装:
何もしません。

```
+-----------------------------------------------------------+
| [メソッド]                                                |
|                                                           |
| (send an-area-container begin-container-sequence) → void? |
+-----------------------------------------------------------+
```

`end-container-sequence` が呼ばれるまで、コンテナのトップレベルウィンドウにおけるジオメトリ管理を一時停止します。`begin-container-sequence` と `end-container-sequence` は、一連のコンテナ変更を括り、結果のジオメトリを一度だけ計算するために使います。コンテナシーケンスはまた、`change-children` による表示／非表示の処理や、`show` による画面表示の部分も、シーケンスが完了するまで遅延させます。開始と終了の命令は任意の深さで入れ子にできます。

```
+----------------------------------------------------+
| [メソッド]                                         |
|                                                    |
| (send an-area-container border) → spacing-integer? |
| (send an-area-container border margin) → void?     |
| margin: spacing-integer?                          |
+----------------------------------------------------+
```

コンテナの境界マージン（ピクセル単位）を取得または設定します。このマージンは、サブ領域の位置と大きさを計算する前に、パネルのクライアント領域への挿入余白として使われます。

```
+-------------------------------------------------------------------------------+
| [メソッド]                                                                    |
|                                                                               |
| (send an-area-container change-children filter) → void?                       |
| filter: ((listof (is-a?/c subarea<%>)). ->. (listof (is-a?/c subarea<%>))) |
| ((listof (is-a?/c subarea<%>))                                                |
|. ->. (listof (is-a?/c subarea<%>)))                                         |
|                                                                               |
| ```racket                                                                     |
| ((listof (is-a?/c subarea<%>))                                                |
|. ->. (listof (is-a?/c subarea<%>)))                                        |
| ```                                                                           |
+-------------------------------------------------------------------------------+
```

フィルタ手続きを取り、コンテナの「削除されていない子」のリストを変更します。フィルタ手続きは子領域のリストを受け取り、新しい子領域のリストを返します。新しいリストは、この領域のサブ領域として生成された子だけで構成されなければなりません（つまり、`change-children` を使ってサブ領域の親を変えることはできません）。

削除されていない子の集合が変わった後、コンテナは新たに削除された子と新たに削除解除された子の集合を計算します。新たに削除されたウィンドウは非表示になります。新たに削除解除されたウィンドウは表示されます。

ウィンドウでない領域は非表示にできないため、削除することもできません。フィルタ手続きがウィンドウでないサブ領域を取り除いた場合、例外が送出され、削除されていない子の集合は変更されません。

```
+----------------------------------------------------------+
| [メソッド]                                               |
|                                                          |
| (send an-area-container container-flow-modified) → void? |
+----------------------------------------------------------+
```

`place-children` など、オーバーライドしたフロー定義メソッドの結果が変わったときにこのメソッドを呼び出します。呼び出しにより、コンテナの子の配置を再計算する必要があることをジオメトリマネージャに通知します。

`reflow-container` メソッドは、ジオメトリマネージャが前回の計算以降に配置が変わったと判断した場合にのみ、子の位置を再計算します。

```
+----------------------------------------------------------------------------+
| [メソッド]                                                                 |
|                                                                            |
| (send an-area-container container-size info)                               |
| → dimension-integer? dimension-integer?                                    |
| dimension-integer?                                                         |
| info: (listof (list/c dimension-integer? dimension-integer? any/c any/c)) |
| (listof (list/c dimension-integer?                                         |
| dimension-integer?                                                         |
| any/c                                                                      |
| any/c))                                                                    |
|                                                                            |
| ```racket                                                                  |
| (listof (list/c dimension-integer?                                         |
|                 dimension-integer?                                         |
|                 any/c                                                      |
|                 any/c))                                                    |
| ```                                                                        |
+----------------------------------------------------------------------------+
```

コンテナの最小サイズを決定するために呼ばれます。詳細は Geometry Management（ジオメトリ管理）を参照してください。

```
+-----------------------------------------------------+
| [メソッド]                                          |
|                                                     |
| (send an-area-container delete-child child) → void? |
| child: (is-a?/c subwindow<%>)                      |
+-----------------------------------------------------+
```

与えられたサブウィンドウを、削除されていない子のリストから取り除きます。`change-children` も参照してください。

```
+---------------------------------------------------------+
| [メソッド]                                              |
|                                                         |
| (send an-area-container end-container-sequence) → void? |
+---------------------------------------------------------+
```

`begin-container-sequence` を参照してください。

```
+----------------------------------------------------------------+
| [メソッド]                                                     |
|                                                                |
| (send an-area-container get-alignment)                         |
| → (symbols 'right 'center 'left)(symbols 'bottom 'center 'top) |
| (symbols 'right 'center 'left)                                 |
| (symbols 'bottom 'center 'top)                                 |
+----------------------------------------------------------------+
```

コンテナの現在の整列指定を返します。詳細は `set-alignment` を参照してください。

```
+---------------------------------------+
| [メソッド]                            |
|                                       |
| (send an-area-container get-children) |
| → (listof (is-a?/c subarea<%>))       |
+---------------------------------------+
```

コンテナの削除されていない子のリストを返します（削除されていない子は、コンテナが現在管理している子です。削除された子は一般に非表示です）。リスト内の子の順序は意味を持ちます。たとえば垂直パネルでは、リストの先頭の子がパネルの上端に配置されます。

```
+----------------------------------------------------------------------------+
| [メソッド]                                                                 |
|                                                                            |
| (send an-area-container place-children                                     |
| → (listof (list/c dimension-integer? dimension-integer? dimension-integer? |
| dimension-integer?))                                                       |
| (listof (list/c dimension-integer?                                         |
| dimension-integer?                                                         |
| dimension-integer?                                                         |
| dimension-integer?))                                                       |
| info: (listof (list/c dimension-integer? dimension-integer? any/c any/c)) |
| (listof (list/c dimension-integer?                                         |
| dimension-integer?                                                         |
| any/c                                                                      |
| any/c))                                                                    |
| width: dimension-integer?                                                 |
| height: dimension-integer?                                                |
|                                                                            |
| ```racket                                                                  |
| (listof (list/c dimension-integer?                                         |
|                 dimension-integer?                                         |
|                 dimension-integer?                                         |
|                 dimension-integer?))                                       |
| ```                                                                        |
|                                                                            |
| ```racket                                                                  |
| (listof (list/c dimension-integer?                                         |
|                 dimension-integer?                                         |
|                 any/c                                                      |
|                 any/c))                                                    |
| ```                                                                        |
+----------------------------------------------------------------------------+
```

コンテナの子を配置するために呼ばれます。詳細は Geometry Management（ジオメトリ管理）を参照してください。

```
+---------------------------------------------------+
| [メソッド]                                        |
|                                                   |
| (send an-area-container reflow-container) → void? |
+---------------------------------------------------+
```

コンテナウィンドウが表示されていないとき、コンテナの子の集合の変更は、必ずしもコンテナのサイズや子のサイズ・位置の即時再計算を引き起こしません。再計算はコンテナが表示されるまで遅延され、一連の変更のあいだの冗長な計算を避けます。`reflow-container` メソッドは、コンテナとその子のサイズと位置の即時再計算を強制します。

`reflow-container` メソッドを呼んだ直後は、コンテナが非表示であっても、`get-size`、`get-client-size`、`get-width`、`get-height`、`get-x`、`get-y` は、マネージャが適用したサイズと位置をコンテナとその子について報告します。コンテナの実装は、いつでも `get-size` などの関数を呼んでウィンドウの現在の状態を取得できます（これらの関数はジオメトリ管理を起動しないためです）。

`container-flow-modified` も参照してください。

```
+----------------------------------------------+
| [メソッド]                                   |
|                                              |
| (send an-area-container set-alignment        |
| horiz-align: (symbols 'right 'center 'left) |
| vert-align: (symbols 'bottom 'center 'top)  |
+----------------------------------------------+
```

コンテナの整列指定を設定します。これは、コンテナに余白があるとき（ある次元で子が伸縮可能でないとき）に、子をどのように配置するかを決めます。

コンテナの水平整列が `'left` のとき、子はコンテナ内で左揃えされ、余白は右側に挿入されます。水平整列が `'center` のとき、各子はコンテナ内で水平方向に中央揃えされます。水平整列が `'right` のとき、余った余白は左側に挿入されます。

同様に、コンテナの垂直整列は `'top`、`'center`、`'bottom` のいずれかです。

```
+-----------------------------------------------------+
| [メソッド]                                          |
|                                                     |
| (send an-area-container spacing) → spacing-integer? |
| (send an-area-container spacing spacing) → void?    |
| spacing: spacing-integer?                          |
+-----------------------------------------------------+
```

コンテナ内のサブ領域間に使われる間隔（ピクセル単位）を取得または設定します。たとえば垂直パネルは、垂直に並ぶ各サブ領域のあいだにこの間隔を挿入します（上下端に余分な空間は付けません）。

---

## area<%>

```
+-------------------------------+
| interfacearea<%>: interface? |
+-------------------------------+
+-------------------------------+
```

`area<%>` オブジェクトは、ウィンドウであるか、あるいは他の領域の位置と大きさを管理するウィンドウレスのコンテナです。`area<%>` はコンテナでも被包含要素でも、あるいはその両方でもあり得ます。親を持たない領域はトップレベルウィンドウだけです。

すべての `area<%>` クラスは、次の名前付き生成引数を受け付けます。

- `min-width` — 既定値は初期のグラフィカル最小幅。`min-width` に渡される
- `min-height` — 既定値は初期のグラフィカル最小高さ。`min-height` に渡される
- `stretchable-width` — 既定値はクラス固有。`stretchable-width` に渡される
- `stretchable-height` — 既定値はクラス固有。`stretchable-height` に渡される

```
+-----------------------------------------+
| [メソッド]                              |
|                                         |
| (send an-area get-graphical-min-size)   |
| → dimension-integer? dimension-integer? |
| dimension-integer?                      |
+-----------------------------------------+
```

領域のグラフィカル最小サイズを二つの値として返します。最小幅と最小高さ（ピクセル単位）です。

詳細は Geometry Management（ジオメトリ管理）を参照してください。戻り値は領域の `min-width` および `min-height` の設定には依存しないことに注意してください。

```
+-----------------------------------------+
| [メソッド]                              |
|                                         |
| (send an-area get-parent)               |
| → (or/c (is-a?/c area-container<%>) #f) |
+-----------------------------------------+
```

領域の親を返します。トップレベルウィンドウは親を持たないことがあり（その場合 `#f` が返る）、あるいは別のトップレベルウィンドウを親に持つこともあります。

```
+---------------------------------------------+
| [メソッド]                                  |
|                                             |
| (send an-area get-top-level-window)         |
| → (or/c (is-a?/c frame%) (is-a?/c dialog%)) |
+---------------------------------------------+
```

領域に最も近いフレームまたはダイアログの祖先を返します。フレームまたはダイアログの領域では、そのフレームまたはダイアログ自身が返されます。

```
+-----------------------------------------------+
| [メソッド]                                    |
|                                               |
| (send an-area min-width) → dimension-integer? |
| (send an-area min-width w) → void?            |
| w: dimension-integer?                        |
+-----------------------------------------------+
```

ジオメトリ管理のための領域の最小幅（ピクセル単位）を取得または設定します。

最小幅が領域のグラフィカル最小幅より小さい場合、あるいは領域がコンテナで `container-size` が報告する幅より小さい場合、最小幅は無視されます。詳細は Geometry Management（ジオメトリ管理）を参照してください。

領域の初期最小幅は、そのグラフィカル最小幅です。`get-graphical-min-size` も参照してください。

最小幅を設定するとき、`w` が内部のハード最小値より小さい場合、`exn:fail:contract` 例外が送出されます。

```
+------------------------------------------------+
| [メソッド]                                     |
|                                                |
| (send an-area min-height) → dimension-integer? |
| (send an-area min-height h) → void?            |
| h: dimension-integer?                         |
+------------------------------------------------+
```

ジオメトリ管理のための領域の最小高さを取得または設定します。

最小高さが領域のグラフィカル最小高さより小さい場合、あるいは領域がコンテナで `container-size` が報告する高さより小さい場合、最小高さは無視されます。詳細は Geometry Management（ジオメトリ管理）を参照してください。

領域の初期最小高さは、そのグラフィカル最小高さです。`get-graphical-min-size` も参照してください。

最小高さ（ピクセル単位）を設定するとき、`h` が内部のハード最小値より小さい場合、`exn:fail:contract` 例外が送出されます。

```
+----------------------------------------------------+
| [メソッド]                                         |
|                                                    |
| (send an-area stretchable-height) → boolean?       |
| (send an-area stretchable-height stretch?) → void? |
| stretch?: any/c                                   |
+----------------------------------------------------+
```

ジオメトリ管理のための領域の垂直方向の伸縮可能性を取得または設定します。詳細は Geometry Management（ジオメトリ管理）を参照してください。

```
+---------------------------------------------------+
| [メソッド]                                        |
|                                                   |
| (send an-area stretchable-width) → boolean?       |
| (send an-area stretchable-width stretch?) → void? |
| stretch?: any/c                                  |
+---------------------------------------------------+
```

ジオメトリ管理のための領域の水平方向の伸縮可能性を取得または設定します。詳細は Geometry Management（ジオメトリ管理）を参照してください。

---

## button%

> [image: button.png]
```
  +------------+
  |  [ ボタン ] |
  +------------+
```

```
+-----------------------+------------+
| classbutton%: class? |            |
+-----------------------+------------+
| superclass: object%   |            |
| extends:              | control<%> |
+-----------------------+------------+
```

ユーザがボタンをクリックするたびに、ボタンのコールバック手続きが呼び出されます。コールバック手続きは、各ボタンを生成するときの初期化引数として与えます。

```
+------------------------------------------------------------------------------+
| [コンストラクタ]                                                             |
|                                                                              |
| (new button%                                                                 |
| → (is-a?/c button%)                                                          |
| label: (or/c label-string? (is-a?/c bitmap%) (list/c (is-a?/c bitmap%)      |
| label-string? (or/c 'left 'top 'right 'bottom)))                             |
| (or/c label-string?                                                          |
| (is-a?/c bitmap%)                                                            |
| (list/c (is-a?/c bitmap%)                                                    |
| label-string?                                                                |
| (or/c 'left 'top 'right 'bottom)))                                           |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c  |
| pane%))                                                                      |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                     |
| (is-a?/c panel%) (is-a?/c pane%))                                            |
| callback: ((is-a?/c button%) (is-a?/c control-event%). ->. any) = (lambda |
| (b e) (void))                                                                |
| style: (listof (or/c 'border 'multi-line 'deleted)) = null                  |
| font: (is-a?/c font%) = normal-control-font                                 |
| enabled: any/c = #t                                                         |
| vert-margin: spacing-integer? = 2                                           |
| horiz-margin: spacing-integer? = 2                                          |
| min-width: (or/c dimension-integer? #f) = #f                                |
| min-height: (or/c dimension-integer? #f) = #f                               |
| stretchable-width: any/c = #f                                               |
| stretchable-height: any/c = #f                                              |
|                                                                              |
| ```racket                                                                    |
| (or/c label-string?                                                          |
|       (is-a?/c bitmap%)                                                      |
|       (list/c (is-a?/c bitmap%)                                              |
|               label-string?                                                  |
|               (or/c 'left 'top 'right 'bottom)))                             |
| ```                                                                          |
|                                                                              |
| ```racket                                                                    |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                     |
|       (is-a?/c panel%) (is-a?/c pane%))                                      |
| ```                                                                          |
+------------------------------------------------------------------------------+
```

文字列ラベル、ビットマップラベル、またはその両方を持つボタンを生成します。`label` がビットマップで、そのビットマップにマスクがあり（`bitmap%` の `get-loaded-mask` を参照）、マスクがビットマップと同じ大きさの場合、そのマスクがラベルに使われます。ラベルとして使われているビットマップを変更した場合、表示されるラベルへの影響は未規定です。`label` がリストの場合、ボタンはビットマップと文字列の両方のラベルを持ち、記号 `'left`、`'top`、`'right`、`'bottom` は、ボタン上のテキストに対する画像の位置を指定します。

`label` に `&` が含まれる場合（`label` が文字列を含むとき）、特別に解析されます。Windows と Unix では、`&` の直後の文字が表示上のコントロールで下線付きになり、キーボードニーモニックを示します（Mac OS ではニーモニックの下線は表示されません）。下線付きのニーモニック文字は文字または数字でなければなりません。ユーザは、コントロールのトップレベルウィンドウがキーボードフォーカスを持つときにニーモニックを入力することで、事実上ボタンをクリックできます。キーボードフォーカスが通常の英数字入力を扱うコントロールにある場合は、Meta キーまたは Alt キーも押す必要があります。`&` 自体は表示前に `label` から取り除かれます。`label` 中の `&&` は `&` に変換されます（ニーモニック下線なし）。Mac OS では、括弧で囲まれたニーモニック文字は、表示前に（周囲の空白とともに）取り除かれます。非ローマ言語では括弧付きニーモニックがよく使われるためです。最後に、歴史的な理由から、タブ文字以降のテキストはすべてのプラットフォームで取り除かれます。これらの規則はすべて、メニュー項目のラベル処理（`set-label` を参照）と一致します。ニーモニックのキーボードイベントは `on-traverse-char` が処理します（Mac OS では処理しません）。

ユーザがボタンをクリックするたびに、コールバック手続きが（イベント型 `'button` で）呼ばれます。

`style` に `'border` が含まれる場合、ボタンは既定のアクションボタンであることを示す特別な枠線で描画されます（`on-traverse-char` を参照）。`style` に `'multi-line` が含まれる場合、ボタンは垂直方向に伸縮でき、テキストラベルの複数行を収容できる形で描画されます。現在のところ、このスタイルが差を生むのは Mac OS だけで、`label` が `#\newline` または `#\return` を含む文字列のときは自動的に選択されます。`style` に `'deleted` が含まれる場合、ボタンは非表示として生成され、親のジオメトリに影響しません。後から親の `add-child` メソッドを呼ぶことで有効にできます。

`font` 引数はコントロールのフォントを決めます。`enabled` 引数については `window<%>` を参照してください。`horiz-margin` と `vert-margin` については `subarea<%>` を、`min-width`、`min-height`、`stretchable-width`、`stretchable-height` については `area<%>` を参照してください。

パッケージ `gui-lib` のバージョン 1.47 で変更: `'multi-line` スタイルを追加し、`label` に `#\return` が含まれるときに自動選択するようにした。

```
+------------------------------------------------+
| [メソッド]                                     |
|                                                |
| (send a-button set-label label) → void?        |
| label: (or/c label-string? (is-a?/c bitmap%)) |
| (or/c label-string?                            |
| (is-a?/c bitmap%))                             |
|                                                |
| ```racket                                      |
| (or/c label-string?                            |
|       (is-a?/c bitmap%))                       |
| ```                                            |
+------------------------------------------------+
```

`window<%>` の `set-label` をオーバーライドします。

`label` が文字列のときは、`window<%>` の `set-label` と同じです。

それ以外の場合は、ビットマップボタンのビットマップラベルを設定します。`label` はビットマップなので、マスクがあり（`bitmap%` の `get-loaded-mask` を参照）マスクがビットマップと同じ大きさなら、そのマスクがラベルに使われます。ラベルとして使われているビットマップを変更した場合、表示されるラベルへの影響は未規定です。ビットマップラベルが設定されるのは、コントロールがもともとビットマップラベルで生成された場合だけです。

ボタンが文字列とビットマップの両方のラベルを持つ場合、どちらも `set-label` で設定できます。

---

## canvas%

```
+-----------------------+-----------+
| classcanvas%: class? |           |
+-----------------------+-----------+
| superclass: object%   |           |
| extends:              | canvas<%> |
+-----------------------+-----------+
```

`canvas%` オブジェクトは、描画とイベント処理のための汎用ウィンドウです。キャンバスへの描画については `canvas<%>` を参照してください。

```
+-----------------------------------------------------------------------------+
| [コンストラクタ]                                                            |
|                                                                             |
| (new canvas%                                                                |
| → (is-a?/c canvas%)                                                         |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c |
| pane%))                                                                     |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                    |
| (is-a?/c panel%) (is-a?/c pane%))                                           |
| style: (listof (or/c 'border 'control-border 'combo 'vscroll 'hscroll      |
| 'resize-corner 'gl 'no-autoclear 'transparent 'no-focus 'deleted)) = null   |
| (listof (or/c 'border 'control-border 'combo                                |
| 'vscroll 'hscroll 'resize-corner                                            |
| 'gl 'no-autoclear 'transparent                                              |
| 'no-focus 'deleted))                                                        |
| paint-callback: ((is-a?/c canvas%) (is-a?/c dc<%>). ->. any) = void      |
| label: (or/c label-string? #f) = #f                                        |
| gl-config: (or/c (is-a?/c gl-config%) #f) = #f                             |
| enabled: any/c = #t                                                        |
| vert-margin: spacing-integer? = 0                                          |
| horiz-margin: spacing-integer? = 0                                         |
| min-width: (or/c dimension-integer? #f) = #f                               |
| min-height: (or/c dimension-integer? #f) = #f                              |
| stretchable-width: any/c = #t                                              |
| stretchable-height: any/c = #t                                             |
|                                                                             |
| ```racket                                                                   |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                    |
|       (is-a?/c panel%) (is-a?/c pane%))                                     |
| ```                                                                         |
|                                                                             |
| ```racket                                                                   |
| (listof (or/c 'border 'control-border 'combo                                |
|               'vscroll 'hscroll 'resize-corner                              |
|               'gl 'no-autoclear 'transparent                                |
|               'no-focus 'deleted))                                          |
| ```                                                                         |
+-----------------------------------------------------------------------------+
```

`style` 引数は、次のスタイルのうち一つ以上を示します。

- `'border` — キャンバスに細い枠線を付ける
- `'control-border` — `text-field%` コントロールに似た枠線を付ける
- `'combo` — `combo-field%` コントロールに似たコンボボタンを付ける。このスタイルは `'control-border` と組み合わせて使い、`'hscroll` や `'vscroll` とは組み合わせない意図である
- `'hscroll` — 水平スクロールを有効にする（初期は表示されるが非アクティブ）
- `'vscroll` — 垂直スクロールを有効にする（初期は表示されるが非アクティブ）
- `'resize-corner` — スクロールバーが一方だけ表示されているとき、キャンバス右下にリサイズコントロール用の余白を残す
- `'gl` — 通常の `dc<%>` 描画の代わりに OpenGL 描画用キャンバスを生成する。`get-dc` の結果に対して `get-gl-context` メソッドを呼ぶ。通常は `'no-autoclear` と組み合わせる
- `'no-autoclear` — ウィンドウ機構によるキャンバスの自動消去を防ぐ。キャンバスの再描画については `canvas<%>` を参照
- `'transparent` — ウィンドウ機構が親を透かして見せることでキャンバスを「消去」する。ウィンドウの再描画および `'transparent` とオフスクリーンバッファリングの相互作用については `canvas<%>` を参照。このフラグを `'no-autoclear` と組み合わせた場合の結果は未規定
- `'no-focus` — キャンバスがクリックされたときや `focus` メソッドが呼ばれたときに、キーボードフォーカスを受け取らないようにする
- `'deleted` — キャンバスを初期状態で非表示として生成し、親のジオメトリに影響しない。後から親の `add-child` メソッドを呼んで有効にできる

`'hscroll` と `'vscroll` スタイルは、初期には非アクティブなスクロールバー付きキャンバスを生成します。スクロールバーは `init-manual-scrollbars` または `init-auto-scrollbars` でアクティブになり、`show-scrollbars` で隠したり再表示したりできます。

`paint-callback` 引数は、既定の `on-paint` メソッドから、キャンバスと `get-dc` が返す DC を引数として呼ばれます。

`label` 引数は `get-label` 用にキャンバスに名前を付けますが、キャンバスとともに表示はされません。

`gl-config` 引数は、このキャンバスの OpenGL コンテキストの性質を決めます。コンテキストはキャンバスの描画コンテキスト経由で取得します。`get-dc` および `dc<%>` の `get-gl-context` も参照してください。

`enabled` 引数については `window<%>` を参照してください。`horiz-margin` と `vert-margin` については `subarea<%>` を、`min-width`、`min-height`、`stretchable-width`、`stretchable-height` については `area<%>` を参照してください。

```
+-----------------------------------------+
| [メソッド]                              |
|                                         |
| (send a-canvas get-gl-client-size)      |
| → dimension-integer? dimension-integer? |
| dimension-integer?                      |
+-----------------------------------------+
```

`'gl` スタイルを持つ `canvas%` インスタンスについて、OpenGL 単位でのキャンバス描画領域の寸法を返します。

結果は、`'gl` スタイルのないキャンバス、または Windows と Unix では `get-scaled-client-size` と同じです。Mac OS では、生成時に与えた `gl-config%` が高解像度モードを指定していない場合、`get-client-size` と同じになることがあります。

パッケージ `gui-lib` のバージョン 1.16 で追加。

```
+---------------------------------------+
| [メソッド]                            |
|                                       |
| (send a-canvas get-scroll-page which) |
| → positive-dimension-integer?         |
| which: (or/c 'horizontal 'vertical)  |
+---------------------------------------+
```

手動スクロールバーの現在のページステップサイズを取得します。スクロールバーが非アクティブ、または自動の場合、結果は `0` です。

`which` 引数は `'horizontal` または `'vertical` で、それぞれ水平または垂直スクロールバーのページステップサイズを取得するかを示します。

`init-manual-scrollbars` も参照してください。

```
+-----------------------------------------------------------+
| [メソッド]                                                |
|                                                           |
| (send a-canvas get-scroll-pos which) → dimension-integer? |
| which: (or/c 'horizontal 'vertical)                      |
+-----------------------------------------------------------+
```

手動スクロールバーの現在の値を取得します。スクロールバーが非アクティブ、または自動の場合、結果は常に `0` です。

`which` 引数は `'horizontal` または `'vertical` で、それぞれ水平または垂直スクロールバーの値を返すかを示します。

`init-manual-scrollbars` も参照してください。

```
+-------------------------------------------------------------+
| [メソッド]                                                  |
|                                                             |
| (send a-canvas get-scroll-range which) → dimension-integer? |
| which: (or/c 'horizontal 'vertical)                        |
+-------------------------------------------------------------+
```

手動スクロールバーの現在の最大値を取得します。スクロールバーが非アクティブ、または自動の場合、結果は常に `0` です。

`which` 引数は `'horizontal` または `'vertical` で、それぞれ水平または垂直スクロールバーの最大値を取得するかを示します。

`init-manual-scrollbars` も参照してください。

```
+-----------------------------------------+
| [メソッド]                              |
|                                         |
| (send a-canvas get-view-start)          |
| → dimension-integer? dimension-integer? |
| dimension-integer?                      |
+-----------------------------------------+
```

表示中のキャンバス部分が始まる位置を取得します。水平および垂直スクロールバーが自動として初期化されている場合（`init-auto-scrollbars` を参照）の現在値に基づきます。`get-client-size` と組み合わせることで、アプリケーションはキャンバスの可視部分だけを効率的に再描画できます。値はピクセル単位です。

スクロールバーが無効、または手動として初期化されている場合（`init-manual-scrollbars` を参照）、結果は `(values 0 0)` です。

```
+-------------------------------------------------+
| [メソッド]                                      |
|                                                 |
| (send a-canvas get-virtual-size)                |
| → (value dimension-integer? dimension-integer?) |
+-------------------------------------------------+
```

スクロール可能なキャンバス領域のデバイス単位での大きさを取得します（クライアントサイズ、すなわち現在可視のキャンバス領域とは対照的です）。スクロールバーが自動として初期化されていない限り（`init-auto-scrollbars` を参照）、これはクライアントサイズ（`get-client-size` が返すもの）と同じです。

```
+------------------------------------------------------+
| [メソッド]                                           |
|                                                      |
| (send a-canvas init-auto-scrollbars                  |
| horiz-pixels: (or/c positive-dimension-integer? #f) |
| vert-pixels: (or/c positive-dimension-integer? #f)  |
| h-value: (real-in 0.0 1.0)                          |
| v-value: (real-in 0.0 1.0)                          |
+------------------------------------------------------+
```

キャンバスの自動スクロールバーを有効にして初期化します。水平または垂直スクロールバーは、それぞれ `'hscroll` または `'vscroll` スタイルフラグで生成されたキャンバスでのみアクティブにできます。

自動スクロールバーでは、プログラマがキャンバスの望ましい仮想サイズを指定し、スクロールバーはユーザが仮想領域をスクロールできるよう自動的に扱われます。不要でもスクロールバーは自動では隠れません。`show-scrollbars` を参照してください。

マウスイベントの座標（`on-event` に渡されるもの）はスクロールバーの位置を補正しません。適切なオフセットを求めるには `get-view-start` メソッドを使ってください。

手動スクロールバーについては `init-manual-scrollbars` も参照してください。水平と垂直のスクロールバーは常に両方とも手動か両方とも自動ですが、有効化は独立です。自動スクロールバーを手動として再初期化することも、その逆も可能です。

`horiz-pixels` または `vert-pixels` のいずれかが `#f` の場合、対応する方向のスクロールバーは有効にならず、その方向のキャンバスの仮想サイズはクライアントサイズと同じになります。

`h-value` と `v-value` 引数は、スクロールバーの範囲に対する割合として初期値を指定します。`0.0` は左／上端、`1.0` は右／下端に初期化します。

この関数を再度呼ぶことで仮想サイズを調整できます。

`on-scroll` および `get-virtual-size` も参照してください。

```
+-----------------------------------------+
| [メソッド]                              |
|                                         |
| (send a-canvas init-manual-scrollbars   |
| h-length: (or/c dimension-integer? #f) |
| v-length: (or/c dimension-integer? #f) |
| h-page: positive-dimension-integer?    |
| v-page: positive-dimension-integer?    |
| h-value: dimension-integer?            |
| v-value: dimension-integer?            |
+-----------------------------------------+
```

キャンバスの手動スクロールバーを有効にして初期化します。水平または垂直スクロールバーは、それぞれ `'hscroll` または `'vscroll` スタイルフラグで生成されたキャンバスでのみアクティブにできます。

手動スクロールバーでは、スクロールバーの詳細はすべてプログラマが管理し、スクロールバーの状態はキャンバスの仮想サイズに影響しません。代わりに、キャンバスの仮想サイズはクライアントサイズと同じになります。

自動スクロールバーについては `init-auto-scrollbars` も参照してください。水平と垂直のスクロールバーは常に両方とも手動か両方とも自動ですが、有効化は独立です。自動を手動として再初期化することも、その逆も可能です。

`h-length` と `v-length` 引数は、各スクロールバーの長さをスクロールステップ（すなわち各スクロールバーの最大値）で指定します。いずれかが `#f` の場合、対応する方向のスクロールバーは無効になります。

`h-page` と `v-page` 引数は、1 ページ分のスクロールバーステップ数、すなわちスクロールバーコントロールの値インジケータの上下をクリックしたときに動く量を設定します。

`h-value` と `v-value` 引数はスクロールバーの初期値を指定します。

`h-value` が `h-length` より大きい、または `v-value` が `v-length` より大きい場合、`exn:fail:contract` 例外が送出されます（ページステップはスクロールバー全体のサイズより大きくても構いません）。

`on-scroll` および `get-virtual-size` も参照してください。

```
+--------------------------------------------------------------+
| [メソッド]                                                   |
|                                                              |
| (send a-canvas make-bitmap width height) → (is-a/c? bitmap%) |
| width: exact-positive-integer?                              |
| height: exact-positive-integer?                             |
+--------------------------------------------------------------+
```

キャンバスへの描画と同じ方法で描画するビットマップを生成します。`make-screen-bitmap` および Portability and Bitmap Variants も参照してください。

```
+----------------------------------+
| [メソッド]                       |
|                                  |
| (send a-canvas on-paint) → void? |
+----------------------------------+
```

`canvas<%>` の `on-paint` をオーバーライドします。

`canvas%` 生成時に `paint-callback` 引数として与えられた手続きを呼び出します。

```
+-----------------------------------------+
| [メソッド]                              |
|                                         |
| (send a-canvas on-scroll event) → void? |
| event: (is-a?/c scroll-event%)         |
+-----------------------------------------+
```

ユーザがキャンバスのスクロールバーの一つを変更したときに呼ばれます。`scroll-event%` 引数がスクロール操作に関する情報を提供します。

このメソッドが呼ばれるのは手動スクロールバーが変更されたときだけです（`init-manual-scrollbars` を参照）。自動スクロールバーでは、代わりに `on-paint` メソッドが呼ばれます。

```
+-------------------------------------------------------------------------+
| [メソッド]                                                              |
|                                                                         |
| (send a-canvas refresh-now                                              |
| paint-proc: ((is-a?/c dc<%>). ->. any) = (lambda (dc) (send a-canvas |
| on-paint))                                                              |
| flush?: any/c = #t                                                     |
+-------------------------------------------------------------------------+
```

キャンバスの描画コンテキストを `paint-proc` に渡して、キャンバスを直ちに更新します（`refresh` がウィンドウ機構の裁量で処理される更新要求をキューに入れるだけの点と対照的です）。

`paint-proc` が呼ばれる前に、キャンバスのフラッシュは無効化されます。また、キャンバスに `'no-autoclear` スタイルがない限り、キャンバスは消去されます。`paint-proc` が返った後、フラッシュは有効化され、`flush?` が真なら直ちに `flush` が呼ばれます。

```
+------------------------------------------------+
| [メソッド]                                     |
|                                                |
| (send a-canvas scroll h-value v-value) → void? |
| h-value: (or/c (real-in 0.0 1.0) #f)          |
| v-value: (or/c (real-in 0.0 1.0) #f)          |
+------------------------------------------------+
```

自動スクロールバーの値を設定します（手動スクロールバーには効果がありません）。

いずれかの引数が `#f` の場合、対応する方向のスクロールバー値は変更されません。

`h-value` と `v-value` はそれぞれスクロールバーの移動量の割合を指定します。`0.0` は左／上端、`1.0` は右／下端、`0.5` は中央に設定します。一般に、キャンバスの仮想サイズが `v`、クライアントサイズが `c` で `(> v c)` のとき、`p` へスクロールするとビュー開始位置は `(floor (* p (- v c)))` になります。

`init-auto-scrollbars` および `get-view-start` も参照してください。

```
+-----------------------------------------------------+
| [メソッド]                                          |
|                                                     |
| (send a-canvas set-scroll-page which value) → void? |
| which: (or/c 'horizontal 'vertical)                |
| value: positive-dimension-integer?                 |
+-----------------------------------------------------+
```

手動スクロールバーの現在のページステップサイズを設定します（自動スクロールバーには効果がありません）。

`which` は `'horizontal` または `'vertical` で、それぞれ水平または垂直スクロールバーのページステップサイズを設定するかを示します。

`init-manual-scrollbars` も参照してください。

```
+----------------------------------------------------+
| [メソッド]                                         |
|                                                    |
| (send a-canvas set-scroll-pos which value) → void? |
| which: (or/c 'horizontal 'vertical)               |
| value: dimension-integer?                         |
+----------------------------------------------------+
```

手動スクロールバーの現在の値を設定します（自動スクロールバーには効果がありません）。

`which` は `'horizontal` または `'vertical` で、それぞれ水平または垂直スクロールバーの値を設定するかを示します。

キャンバスのスクロールバーの値はユーザのスクロールによっても変わり、そのような変更はこのメソッドを経由しません。スクロールバー値の変化を監視するには `on-scroll` を使ってください。

`init-manual-scrollbars` および `scroll` も参照してください。

```
+--------------------------------------+
| [メソッド]                           |
|                                      |
| (send a-canvas set-scroll-range      |
| which: (or/c 'horizontal 'vertical) |
| value: dimension-integer?           |
+--------------------------------------+
```

手動スクロールバーの現在の最大値を設定します（自動スクロールバーには効果がありません）。

`which` は `'horizontal` または `'vertical` で、それぞれ水平または垂直スクロールバーの最大値を設定するかを示します。

`init-manual-scrollbars` も参照してください。

```
+--------------------------------+
| [メソッド]                     |
|                                |
| (send a-canvas show-scrollbars |
| show-horiz?: any/c            |
| show-vert?: any/c             |
+--------------------------------+
```

`show-horiz?` と `show-vert?` に従ってスクロールバーを表示または非表示にします。`show-horiz?` が真で、キャンバスが `'hscroll` スタイルで生成されていない場合、`exn:fail:contract` 例外が送出されます。同様に、`show-vert?` が真で `'vscroll` スタイルで生成されていない場合も例外が送出されます。

水平スクロールバーを表示できるのは `'hscroll` スタイルで生成されたキャンバスだけ、垂直スクロールバーを表示できるのは `'vscroll` スタイルで生成されたキャンバスだけです。`init-auto-scrollbars` および `init-manual-scrollbars` も参照してください。

```
+-----------------------------------------+
| [メソッド]                              |
|                                         |
| (send a-canvas swap-gl-buffers) → void? |
+-----------------------------------------+
```

このキャンバスの DC（`get-dc` が返すもの）に対する `get-gl-context` の結果について、`swap-buffers` を呼び出します。

`gl-context<%>` の `swap-buffers` メソッドは再入可能ロックを取得するため、異なるスレッドや OpenGL コンテキストでの `swap-gl-buffers` または `with-gl-context` の入れ子呼び出しはブロックしたりデッドロックしたりすることがあります。

```
+--------------------------------------------+
| [メソッド]                                 |
|                                            |
| (send a-canvas with-gl-context             |
| thunk: (-> any)                           |
| fail: (-> any) = (lambda () (error....)) |
+--------------------------------------------+
```

与えられた thunk を、このキャンバスの DC（`get-dc` が返すもの）に対する `get-gl-context` の結果の `call-as-current` に渡します。`get-gl-context` が `#f` を返す場合は、代わりに `fail` が呼ばれます。

`gl-context<%>` の `call-as-current` メソッドは再入可能ロックを取得するため、異なるスレッドや OpenGL コンテキストでの `with-gl-context` または `swap-gl-buffers` の入れ子呼び出しはブロックしたりデッドロックしたりすることがあります。

---

## canvas<%>

```
+---------------------------------+--------------+
| interfacecanvas<%>: interface? |              |
+---------------------------------+--------------+
| implements:                     | subwindow<%> |
+---------------------------------+--------------+
```

キャンバスは、グラフィックスとテキストを描画できるサブウィンドウです。キャンバスはマウスとキーボードのイベントも受け取ります。

`canvas<%>` インタフェースは次の二つのクラスによって実装されます。

- `canvas%` — 任意の描画とイベント処理のためのキャンバス
- `editor-canvas%` — `editor<%>` オブジェクトを表示するためのキャンバス

キャンバスへ描画するには、`get-dc` でデバイスコンテキストを取得します。キャンバスを更新する基本的な方法は二つあります。

- 描画は通常、キャンバスの `on-paint` コールバック中に行われます。`canvas%` クラスは、既定の `on-paint` メソッドから呼ばれる初期化引数 `paint-callback` をサポートします。キャンバスの `on-paint` メソッドは、キャンバスが最初に表示されたときやリサイズされたときなど、ウィンドウ機構がキャンバスの更新が必要と判断したときに、イベントとして自動的に呼ばれます。ウィンドウ機構から `on-paint` 呼び出しを明示的に起こすには `refresh` メソッドを使います（`on-paint` が呼ばれる前の複数の `refresh` 要求は、単一の `on-paint` 呼び出しにまとめられます）。ウィンドウ機構が `on-paint` を呼ぶ前に、キャンバスのスタイル（例: `canvas%` の `style` 初期化引数）に応じてキャンバスの背景を消去する（`erase` を参照）ことがあります。キャンバスのスタイルが明示的なクリアを抑止していても、ウィンドウの移動やリサイズ操作によってキャンバスが消去されることがあります。透明キャンバスでは、「消去」とは親ウィンドウが透けて見えることを意味します。
- 描画は、ウィンドウ機構からの `on-paint` 呼び出しの外でも、キャンバスのイベントスペースのハンドラスレッド以外のスレッドからでも、いつでも行えます。システムからの `on-paint` コールバック外での描画は、ウィンドウ操作がキャンバスを消去し得るという意味で一時的ですが、ウィンドウの再描画が必要になるまでは永続します。`on-paint` メソッドを直接呼ぶことは、ウィンドウ機構からの `on-paint` コールバック外で描画するのと同じです。`canvas%` では、`refresh-now` を使って、`refresh` で更新を要求するのと似た形でキャンバス内容の即時更新を強制できます。

キャンバスの描画コンテキストへの描画は、実際にはオフスクリーンバッファへレンダリングされます。バッファは非同期に、あるいは `flush` メソッドや `flush-display` により明示的に、画面へ自動フラッシュされます——キャンバスのフラッシュが無効化されていない限り。`suspend-flush` メソッドは、対応する `resume-flush` が呼ばれるまでキャンバスのフラッシュを一時停止します。`suspend-flush` と `resume-flush` の呼び出しは入れ子にでき、その場合、最も外側の `suspend-flush` が `resume-flush` で釣り合うまでフラッシュは停止します。ウィンドウ機構からの `on-paint` 呼び出しは暗黙に `suspend-flush` と `resume-flush` で包まれ、`refresh-now` による描画手続きの呼び出しも同様です。

透明キャンバスの場合、線やテキストのスムージングは、キャンバスの背景となるウィンドウに依存することがあります。たとえば、対象コンテキストが白か灰色かで、スムージングがピクセルを異なる色にする場合があります。ただし、背景に敏感なスムージングがサポートされるのは、キャンバスのオフスクリーンバッファに記録される描画コマンドが比較的少数の場合に限られます。

```
+----------------------------------------------+
| [メソッド]                                   |
|                                              |
| (send a-canvas accept-tab-focus) → boolean?  |
| (send a-canvas accept-tab-focus on?) → void? |
| on?: any/c                                  |
+----------------------------------------------+
```

キャンバスのタブフォーカスが有効かどうかを取得または設定します（キャンバスが `canvas%` の `'no-focus` スタイルで生成されていないと仮定）。タブフォーカスが有効なとき、ユーザが Tab キーや矢印キーでフレームまたはダイアログのコントロール間を移動する際に、キャンバスはキーボードフォーカスを受け取れます。既定ではタブフォーカスは無効です。

`canvas%` オブジェクトでタブフォーカスが有効な場合、Tab、矢印、Enter、Escape のキーボードイベントはフレームの既定の `on-traverse-char` メソッドに消費されます（加えて、ダイアログの既定メソッドは Escape キーイベントを消費します）。それ以外の場合、`on-traverse-char` はキーボードイベントをキャンバスへ伝播させます。

`editor-canvas%` オブジェクトでは、Tab、矢印、Enter、Escape キーボードイベントの扱いは `allow-tab-exit` メソッドによって決まります。

```
+-------------------------------+
| [メソッド]                    |
|                               |
| (send a-canvas flush) → void? |
+-------------------------------+
```

`flush-display` に似ていますが、可能ならキャンバスに限定します。

```
+---------------------------------------+
| [メソッド]                            |
|                                       |
| (send a-canvas get-canvas-background) |
| → (or/c (is-a?/c color%) #f)          |
+---------------------------------------+
```

`on-paint` が呼ばれる前にキャンバス内容を「消去」するために現在使われている色を返します。`set-canvas-background` も参照してください。

キャンバスが `'transparent` スタイルで生成された場合、結果は `#f` です。それ以外は常に `color%` オブジェクトです。

```
+------------------------------------------+
| [メソッド]                               |
|                                          |
| (send a-canvas get-dc) → (is-a?/c dc<%>) |
+------------------------------------------+
```

キャンバスのデバイスコンテキストを取得します。描画の詳細は `dc<%>` を参照してください。

```
+-----------------------------------------+
| [メソッド]                              |
|                                         |
| (send a-canvas get-scaled-client-size)  |
| → dimension-integer? dimension-integer? |
| dimension-integer?                      |
+-----------------------------------------+
```

キャンバスの描画領域の寸法を、スケールされていないピクセルで返します——つまり、キャンバスのサイズと内容に暗黙に適用されるスケーリング（Screen Resolution and Text Scaling を参照）なしです。

たとえば Mac OS で Retina ディスプレイ上のキャンバスはバッキングスケール 2 を持ち、`get-scaled-client-size` の結果は `get-client-size` の約 2 倍になります。同じキャンバスのフレームを非 Retina 画面へドラッグすると、バッキングスケールが 1 に変わり、`get-scaled-client-size` と `get-client-size` が同じ値を返すことがあります。キャンバスのバッキングスケールが変わり得るかはプラットフォームに依存します。

`get-scaled-client-size` が報告するサイズは、`'gl` スタイルの `canvas%` インスタンスでの OpenGL 描画のビューポートサイズと一致することがあります。ただし Mac OS では、キャンバスが `set-hires-mode` で高解像度モードに調整された `gl-config%` 指定で生成されない限り、ビューポートはスケール後のサイズと一致します。`canvas%` の `get-gl-client-size` も参照してください。

パッケージ `gui-lib` のバージョン 1.13 で追加。

```
+--------------------------------------------------------+
| [メソッド]                                             |
|                                                        |
| (send a-canvas min-client-height) → dimension-integer? |
| (send a-canvas min-client-height h) → void?            |
| h: dimension-integer?                                 |
+--------------------------------------------------------+
```

ジオメトリ管理のためのキャンバスの最小高さを、フルサイズではなくクライアントサイズに基づいて取得または設定します。クライアント高さは `area<%>` の `min-height` 経由で取得または変更され、必要に応じて枠線とスクロールバーのサイズが加算または減算されます。

最小高さがキャンバスのグラフィカル最小高さより小さい場合は無視されます。詳細は Geometry Management（ジオメトリ管理）を参照してください。

```
+-------------------------------------------------------+
| [メソッド]                                            |
|                                                       |
| (send a-canvas min-client-width) → dimension-integer? |
| (send a-canvas min-client-width w) → void?            |
| w: dimension-integer?                                |
+-------------------------------------------------------+
```

ジオメトリ管理のためのキャンバスの最小幅を、フルサイズではなくクライアントサイズに基づいて取得または設定します。クライアント幅は `area<%>` の `min-width` 経由で取得または変更され、必要に応じて枠線とスクロールバーのサイズが加算または減算されます。

最小幅がキャンバスのグラフィカル最小幅より小さい場合は無視されます。詳細は Geometry Management（ジオメトリ管理）を参照してください。

```
+------------------------------------+
| [メソッド]                         |
|                                    |
| (send a-canvas on-char ch) → void? |
| ch: (is-a?/c key-event%)          |
+------------------------------------+
```

仕様:
キャンバスがキーボードイベントを受け取ったときに呼ばれます。Mouse and Keyboard Events も参照してください。

既定の実装:
何もしません。

```
+----------------------------------------+
| [メソッド]                             |
|                                        |
| (send a-canvas on-event event) → void? |
| event: (is-a?/c mouse-event%)         |
+----------------------------------------+
```

仕様:
キャンバスがマウスイベントを受け取ったときに呼ばれます。Mouse and Keyboard Events も参照してください。特に、特定のマウスイベントは落とされ得ることに注意してください。

既定の実装:
何もしません。

```
+----------------------------------+
| [メソッド]                       |
|                                  |
| (send a-canvas on-paint) → void? |
+----------------------------------+
```

仕様:
キャンバスが露出したりリサイズされたりして、キャンバス内の画像を再描画する必要があるときに呼ばれます。

システム露出イベントに応じて `on-paint` が呼ばれ、キャンバスの一部だけが新たに露出した場合、`on-paint` が行う描画操作は新たに露出した領域にクリップされます。ただし、`get-clipping-region` が報告するクリップ領域は変わりません。

既定の実装:
何もしません。

```
+-----------------------------------+
| [メソッド]                        |
|                                   |
| (send a-canvas on-tab-in) → void? |
+-----------------------------------+
```

仕様:
キーボードナビゲーションイベントによりキーボードフォーカスがキャンバスに入ったときに呼ばれます。フォーカス変更時と同様に `on-focus` メソッドも呼ばれます。ナビゲーションイベントによりキーボードフォーカスがキャンバスを離れるときは、`on-focus` だけが呼ばれます。

`accept-tab-focus` および `top-level-window<%>` の `on-traverse-char` も参照してください。

既定の実装:
何もしません。

```
+--------------------------------------+
| [メソッド]                           |
|                                      |
| (send a-canvas resume-flush) → void? |
+--------------------------------------+
```

キャンバスのフラッシュについては `canvas<%>` を参照してください。

```
+-----------------------------------------------------+
| [メソッド]                                          |
|                                                     |
| (send a-canvas set-canvas-background color) → void? |
| color: (is-a?/c color%)                            |
+-----------------------------------------------------+
```

`on-paint` が呼ばれる前にキャンバス内容を「消去」するために使う色を設定します（この色は通常キャンバスに低レベルで関連付けられるため、他の活動でキャンバスの完全な再描画が遅延されても使われます）。

キャンバスが `'transparent` スタイルで生成された場合、`exn:fail:contract` 例外が送出されます。

```
+-----------------------------------------------+
| [メソッド]                                    |
|                                               |
| (send a-canvas set-resize-corner on?) → void? |
| on?: any/c                                   |
+-----------------------------------------------+
```

Mac OS では、スクロールバーが一方だけ表示されているとき、キャンバス右下のリサイズタブ用の余白を有効または無効にします。Windows と Unix では効果がありません。両方またはどちらのスクロールバーも表示されていないときも効果がありません。リサイズコーナーは既定で無効ですが、キャンバスを `'resize-corner` スタイルで生成するときに有効にできます。

```
+---------------------------------------+
| [メソッド]                            |
|                                       |
| (send a-canvas suspend-flush) → void? |
+---------------------------------------+
```

キャンバスのフラッシュについては `canvas<%>` を参照してください。

キャンバスのフラッシュを一時停止すると、一部のプラットフォームでは同じフレーム内の他のウィンドウの再描画が抑制されることがあるので注意してください。

---

## check-box%

> [image: check-box.png]
```
  +------------------+
  | [x] チェックボックス |
  +------------------+
```

```
+--------------------------+------------+
| classcheck-box%: class? |            |
+--------------------------+------------+
| superclass: object%      |            |
| extends:                 | control<%> |
+--------------------------+------------+
```

チェックボックスは、チェック済みまたは未チェックのいずれかである、ラベル付きの箱です。

ユーザがチェックボックスをクリックするたびに、チェックボックスの値がトグルされ、そのコールバック手続きが呼び出されます。コールバック手続きは、各チェックボックスを生成するときの初期化引数として与えます。

```
+-----------------------------------------------------------------------------+
| [コンストラクタ]                                                            |
|                                                                             |
| (new check-box%                                                             |
| → (is-a?/c check-box%)                                                      |
| label: (or/c label-string? (is-a?/c bitmap%))                              |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c |
| pane%))                                                                     |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                    |
| (is-a?/c panel%) (is-a?/c pane%))                                           |
| callback: ((is-a?/c check-box%) (is-a?/c control-event%). ->. any) =     |
| (lambda (c e) (void))                                                       |
| ((is-a?/c check-box%) (is-a?/c control-event%)                              |
|. ->. any)                                                                 |
| style: (listof (or/c 'deleted)) = null                                     |
| value: any/c = #f                                                          |
| font: (is-a?/c font%) = normal-control-font                                |
| enabled: any/c = #t                                                        |
| vert-margin: spacing-integer? = 2                                          |
| horiz-margin: spacing-integer? = 2                                         |
| min-width: (or/c dimension-integer? #f) = #f                               |
| min-height: (or/c dimension-integer? #f) = #f                              |
| stretchable-width: any/c = #f                                              |
| stretchable-height: any/c = #f                                             |
|                                                                             |
| ```racket                                                                   |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                    |
|       (is-a?/c panel%) (is-a?/c pane%))                                     |
| ```                                                                         |
|                                                                             |
| ```racket                                                                   |
| ((is-a?/c check-box%) (is-a?/c control-event%)                              |
|. ->. any)                                                                |
| ```                                                                         |
+-----------------------------------------------------------------------------+
```

文字列またはビットマップのラベルを持つチェックボックスを生成します。`label` がビットマップで、マスクがあり（`bitmap%` の `get-loaded-mask` を参照）マスクがビットマップと同じ大きさの場合、そのマスクがラベルに使われます。ラベルとして使われているビットマップを変更した場合、表示されるラベルへの影響は未規定です。

`label` が文字列で `&` が含まれる場合、`button%` と同様に特別に解析されます。

ユーザがチェックボックスをクリックするたびに、コールバック手続きが（イベント型 `'check-box` で）呼ばれます。

`style` に `'deleted` が含まれる場合、チェックボックスは非表示として生成され、親のジオメトリに影響しません。後から親の `add-child` メソッドを呼ぶことで有効にできます。

`value` が真の場合、`set-value` に渡されて、最初からチェックされた状態になります。

`font` 引数はコントロールのフォントを決めます。`enabled` 引数については `window<%>` を参照してください。`horiz-margin` と `vert-margin` については `subarea<%>` を、`min-width`、`min-height`、`stretchable-width`、`stretchable-height` については `area<%>` を参照してください。

```
+-----------------------------------------+
| [メソッド]                              |
|                                         |
| (send a-check-box get-value) → boolean? |
+-----------------------------------------+
```

チェックボックスの状態を取得します。チェック済みなら `#t`、そうでなければ `#f` です。

```
+------------------------------------------------+
| [メソッド]                                     |
|                                                |
| (send a-check-box set-label label) → void?     |
| label: (or/c label-string? (is-a?/c bitmap%)) |
+------------------------------------------------+
```

`window<%>` の `set-label` をオーバーライドします。

`label` が文字列のときは、`window<%>` の `set-label` と同じです。

それ以外の場合は、ビットマップチェックボックスのビットマップラベルを設定します。`label` はビットマップなので、マスクがあり（`bitmap%` の `get-loaded-mask` を参照）マスクがビットマップと同じ大きさなら、そのマスクがラベルに使われます。ラベルとして使われているビットマップを変更した場合、表示されるラベルへの影響は未規定です。ビットマップラベルが設定されるのは、コントロールがもともとビットマップラベルで生成された場合だけです。

```
+--------------------------------------------+
| [メソッド]                                 |
|                                            |
| (send a-check-box set-value state) → void? |
| state: any/c                              |
+--------------------------------------------+
```

チェックボックスの状態を設定します（コントロールのコールバック手続きは呼び出されません）。

チェックボックスの状態はユーザのクリックによっても変わり、そのような変更はこのメソッドを経由しません。状態変化を監視するには、初期化引数として与えたコントロールのコールバック手続きを使ってください。

`state` が `#f` なら箱は未チェック、それ以外ならチェック済みになります。

---

## checkable-menu-item%

```
+------------------------------------+-------------------------+
| classcheckable-menu-item%: class? |                         |
+------------------------------------+-------------------------+
| superclass: object%                |                         |
| extends:                           | selectable-menu-item<%> |
+------------------------------------+-------------------------+
```

`checkable-menu-item%` は、チェックマークを維持する文字列ラベル付きメニュー項目です。親は `menu%` または `popup-menu%` でなければなりません。ユーザがメニュー項目を選択すると、項目のチェックマークがトグルされ、そのコールバック手続きが呼ばれます。

```
+--------------------------------------------------------------------------------+
| [コンストラクタ]                                                               |
|                                                                                |
| (new checkable-menu-item%                                                      |
| → (is-a?/c checkable-menu-item%)                                               |
| label: label-string?                                                          |
| parent: (or/c (is-a?/c menu%) (is-a?/c popup-menu%))                          |
| callback: ((is-a?/c checkable-menu-item%) (is-a?/c control-event%). ->.     |
| any) = (lambda (i e) (void))                                                   |
| ((is-a?/c checkable-menu-item%) (is-a?/c control-event%)                       |
|. ->. any)                                                                    |
| shortcut: (or/c char? symbol? #f) = #f                                        |
| help-string: (or/c label-string? #f) = #f                                     |
| demand-callback: ((is-a?/c menu-item%). ->. any) = (lambda (i) (void))      |
| checked: any/c = #f                                                           |
| shortcut-prefix: (and/c (listof (or/c 'alt 'cmd 'meta 'ctl 'shift 'option))   |
| (λ (x) (implies (equal? 'unix (system-type)) (not (and (member 'alt x) (member |
| 'meta x))))) (λ (x) (equal? x (remove-duplicates x)))) =                       |
| (get-default-shortcut-prefix)                                                  |
| (and/c (listof (or/c 'alt 'cmd 'meta 'ctl                                      |
| 'shift 'option))                                                               |
| (λ (x) (implies (equal? 'unix (system-type))                                   |
| (not (and (member 'alt x)                                                      |
| (member 'meta x)))))                                                           |
| (λ (x) (equal? x (remove-duplicates x))))                                      |
|                                                                                |
| ```racket                                                                      |
| ((is-a?/c checkable-menu-item%) (is-a?/c control-event%)                       |
|. ->. any)                                                                   |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (and/c (listof (or/c 'alt 'cmd 'meta 'ctl                                      |
|                      'shift 'option))                                          |
|        (λ (x) (implies (equal? 'unix (system-type))                            |
|                        (not (and (member 'alt x)                               |
|                                  (member 'meta x)))))                          |
|        (λ (x) (equal? x (remove-duplicates x))))                               |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

`parent` に新しいメニュー項目を生成します。項目は最初から表示され、親の末尾に追加され、未チェックです。コールバック手続きは、メニュー項目が選択されたとき（メニューバー、`window<%>` の `popup-menu`、または `editor-admin%` の `popup-menu` 経由）に（イベント型 `'menu` で）呼ばれます。

`label` 中のニーモニック `&` については `set-label` を参照してください。

`shortcut` が `#f` でない場合、項目はショートカットを持ちます。詳細は `get-shortcut` を参照してください。`shortcut-prefix` 引数はショートカットの修飾キー集合を決めます。`get-shortcut-prefix` を参照してください。

`help` が `#f` でない場合、項目はヘルプ文字列を持ちます。詳細は `get-help-string` を参照してください。

`demand-callback` 手続きは、既定の `on-demand` メソッドからオブジェクト自身を引数として呼ばれます。

既定ではメニュー項目は最初未チェックです。`checked` が真なら `check` が呼ばれ、最初からチェックされた状態になります。

```
+---------------------------------------------------+
| [メソッド]                                        |
|                                                   |
| (send a-checkable-menu-item check check?) → void? |
| check?: any/c                                    |
+---------------------------------------------------+
```

メニュー項目をチェックまたは未チェックにします。

メニュー項目のチェック状態はユーザの選択によっても変わり、そのような変更はこのメソッドを経由しません。チェック状態の変化を監視するには、初期化引数として与えたメニュー項目のコールバック手続きを使ってください。

```
+-----------------------------------------------------+
| [メソッド]                                          |
|                                                     |
| (send a-checkable-menu-item is-checked?) → boolean? |
+-----------------------------------------------------+
```

項目がチェック済みなら `#t`、そうでなければ `#f` を返します。

---

## choice%

> [image: choice.png]
```
  +------------------+-+
  | 選択項目       v |
  +------------------+-+
```

```
+-----------------------+-----------------+
| classchoice%: class? |                 |
+-----------------------+-----------------+
| superclass: object%   |                 |
| extends:              | list-control<%> |
+-----------------------+-----------------+
```

チョイス項目は、ユーザがポップアップリストから一つの文字列項目を選べるようにします。リストボックスと異なり、ユーザが選択肢メニューをポップアップするまで、現在の選択だけが見えます。

ユーザがチョイス項目の選択を変更するたびに、チョイス項目のコールバック手続きが呼び出されます。コールバック手続きは、各チョイス項目を生成するときの初期化引数として与えます。

`list-box%` も参照してください。

```
+------------------------------------------------------------------------------+
| [コンストラクタ]                                                             |
|                                                                              |
| (new choice%                                                                 |
| → (is-a?/c choice%)                                                          |
| label: (or/c label-string? #f)                                              |
| choices: (listof label-string?)                                             |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c  |
| pane%))                                                                      |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                     |
| (is-a?/c panel%) (is-a?/c pane%))                                            |
| callback: ((is-a?/c choice%) (is-a?/c control-event%). ->. any) = (lambda |
| (c e) (void))                                                                |
| style: (listof (or/c 'horizontal-label 'vertical-label 'deleted)) = null    |
| (listof (or/c 'horizontal-label 'vertical-label                              |
| 'deleted))                                                                   |
| selection: exact-nonnegative-integer? = 0                                   |
| font: (is-a?/c font%) = normal-control-font                                 |
| enabled: any/c = #t                                                         |
| vert-margin: spacing-integer? = 2                                           |
| horiz-margin: spacing-integer? = 2                                          |
| min-width: (or/c dimension-integer? #f) = #f                                |
| min-height: (or/c dimension-integer? #f) = #f                               |
| stretchable-width: any/c = #f                                               |
| stretchable-height: any/c = #f                                              |
|                                                                              |
| ```racket                                                                    |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                     |
|       (is-a?/c panel%) (is-a?/c pane%))                                      |
| ```                                                                          |
|                                                                              |
| ```racket                                                                    |
| (listof (or/c 'horizontal-label 'vertical-label                              |
|               'deleted))                                                     |
| ```                                                                          |
+------------------------------------------------------------------------------+
```

チョイス項目を生成します。`label` が文字列の場合、チョイス項目のラベルとして使われます。

`label` に `&` が含まれる場合、`button%` と同様に特別に解析されます。

`choices` リストは、コントロールの初期のユーザ選択可能項目のリストを指定します。初期の選択肢の集合が、コントロールのグラフィカル最小幅を決めます（詳細は Geometry Management を参照）。

ユーザがチョイス項目を選択したとき（または現在選択中の項目を再選択したとき）、コールバック手続きが（イベント型 `'choice` で）呼ばれます。

`style` に `'vertical-label` が含まれる場合、チョイス項目はコントロールの上にラベルを付けて生成されます。`style` に `'vertical-label` が含まれない場合（任意で `'horizontal-label` を含めてもよい）、ラベルはチョイス項目の左に生成されます。`style` に `'deleted` が含まれる場合、チョイス項目は非表示として生成され、親のジオメトリに影響しません。後から親の `add-child` メソッドを呼ぶことで有効にできます。

既定では最初の選択肢（あれば）が初期選択されます。`selection` が正の場合、`set-selection` に渡されて初期選択が設定されます。通常 `selection` は `choices` の長さ未満でなければなりませんが、`choices` が空のときは `0` でも構いません。

`font` 引数はコントロールのフォントを決めます。`enabled` 引数については `window<%>` を参照してください。`horiz-margin` と `vert-margin` については `subarea<%>` を、`min-width`、`min-height`、`stretchable-width`、`stretchable-height` については `area<%>` を参照してください。
