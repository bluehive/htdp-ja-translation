# 付録：GUI クラス参照（76–85）

本節は Racket GUI ライブラリのクラス・インタフェース参照のうち、`readable-snip<%>` から `string-snip%` までを扱う。

ソース: `extracted/appendix/gui/original_markdown_76` … `85`。

コード、メソッド名、契約（contracts）、シグネチャは原文のまま示す。クラス名・インタフェース名もそのままとする。

---

## readable-snip<%>

```
+----------------------------------------+
| interfacereadable-snip<%>: interface? |
+----------------------------------------+
+----------------------------------------+
```

`readable-snip<%>` オブジェクトは、`open-input-text-editor` が生成するポートによって特別に扱われる。入力ストリームで `readable-snip<%>` オブジェクトに出会うと、その `read-special` メソッドが呼ばれ、スニップに対する読み取り結果が生成される。その結果は、`read-char-or-special` の意味での「特殊」値としてポートから返される。

`read` と `read-syntax` は `read-char-or-special` の上に構築されているため、スニップは `readable-snip<%>` を実装することで、そのスニップを含むストリームに対して `read` を使ったときに、S 式全体やその他の種類の値を生成できる。

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-readable-snip read-special              |
| source: any/c                                  |
| line: (or/c exact-nonnegative-integer? #f)     |
| column: (or/c exact-nonnegative-integer? #f)   |
| position: (or/c exact-nonnegative-integer? #f) |
+-------------------------------------------------+
```

引数は、カスタム入力ポートの `read-in` が返す手続きへの引数と同じである。詳細は Custom Ports を参照。結果も、`read-in` が生成する手続きの結果と同じである。

---

## scroll-event%

```
+-----------------------------+
| classscroll-event%: class? |
+-----------------------------+
| superclass: event%          |
+-----------------------------+
```

`scroll-event%` オブジェクトは、スクロールイベントに関する情報を保持する。`scroll-event%` のインスタンスは常に `on-scroll` に渡される。

スクロールイベントの種類の一覧については `get-event-type` を参照。

```
+-------------------------------------------------------------------------+
| [constructor]                                                           |
|                                                                         |
| (new scroll-event%                                                      |
| → (is-a?/c scroll-event%)                                               |
| event-type: (or/c 'top 'bottom 'line-up 'line-down 'page-up 'page-down |
| 'thumb) = 'thumb                                                        |
| (or/c 'top 'bottom 'line-up 'line-down                                  |
| 'page-up 'page-down 'thumb)                                             |
| direction: (or/c 'horizontal 'vertical) = 'vertical                    |
| position: dimension-integer? = 0                                       |
| time-stamp: exact-integer? = 0                                         |
|                                                                         |
| ```racket                                                               |
| (or/c 'top 'bottom 'line-up 'line-down                                  |
|       'page-up 'page-down 'thumb)                                       |
| ```                                                                     |
+-------------------------------------------------------------------------+
```

`event-type`、`direction`、`position`、`time-stamp` については、対応する `get-` および `set-` メソッドを参照。

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-scroll-event get-direction) |
| → (or/c 'horizontal 'vertical)      |
+-------------------------------------+
```

イベントによって変更されたスクロールバーの識別子を返す。水平スクロールバーなら `'horizontal`、垂直スクロールバーなら `'vertical`。あわせて `set-direction` も参照。

```
+----------------------------------------------------------------------+
| [method]                                                             |
|                                                                      |
| (send a-scroll-event get-event-type)                                 |
| → (or/c 'top 'bottom 'line-up 'line-down 'page-up 'page-down 'thumb) |
| (or/c 'top 'bottom 'line-up 'line-down                               |
| 'page-up 'page-down 'thumb)                                          |
|                                                                      |
| ```racket                                                            |
| (or/c 'top 'bottom 'line-up 'line-down                               |
|       'page-up 'page-down 'thumb)                                    |
| ```                                                                  |
+----------------------------------------------------------------------+
```

イベントの種類を返す。次のいずれかである。

- `'top` — ユーザが先頭へスクロールするボタンをクリックした
- `'bottom` — ユーザが末尾へスクロールするボタンをクリックした
- `'line-up` — ユーザが 1 ステップ上または左へスクロールする矢印をクリックした
- `'line-down` — ユーザが 1 ステップ下または右へスクロールする矢印をクリックした
- `'page-up` — ユーザが 1 ページ上または左へスクロールする領域をクリックした
- `'page-down` — ユーザが 1 ページ下または右へスクロールする領域をクリックした
- `'thumb` — ユーザがスクロール位置インジケータをドラッグした

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send a-scroll-event get-position) → dimension-integer? |
+---------------------------------------------------------+
```

イベントを引き起こした操作のあとでの、スクロールバーの位置を返す。あわせて `set-position` も参照。

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-scroll-event set-direction direction) → void? |
| direction: (or/c 'horizontal 'vertical)              |
+-------------------------------------------------------+
```

イベントによって変更されたスクロールバーの識別子を設定する。水平なら `'horizontal`、垂直なら `'vertical`。あわせて `get-direction` も参照。

```
+---------------------------------------------------------------------------+
| [method]                                                                  |
|                                                                           |
| (send a-scroll-event set-event-type type) → void?                         |
| type: (or/c 'top 'bottom 'line-up 'line-down 'page-up 'page-down 'thumb) |
| (or/c 'top 'bottom 'line-up 'line-down                                    |
| 'page-up 'page-down 'thumb)                                               |
|                                                                           |
| ```racket                                                                 |
| (or/c 'top 'bottom 'line-up 'line-down                                    |
|       'page-up 'page-down 'thumb)                                         |
| ```                                                                       |
+---------------------------------------------------------------------------+
```

イベントの種類を設定する。各イベント種の意味は `get-event-type` を参照。

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-scroll-event set-position position) → void? |
| position: dimension-integer?                       |
+-----------------------------------------------------+
```

イベントを引き起こした操作のあとでのスクロールバー位置を記録する（スクロールバー自体は影響を受けない）。あわせて `get-position` も参照。

---

## selectable-menu-item<%>

```
+-----------------------------------------------+-----------------------+
| interfaceselectable-menu-item<%>: interface? |                       |
+-----------------------------------------------+-----------------------+
| implements:                                   | labelled-menu-item<%> |
+-----------------------------------------------+-----------------------+
```

`selectable-menu-item<%>` オブジェクトは、ユーザが選択できる `labelled-menu-item<%>` である。キーボードショートカットを持つこともでき、そのショートカットはメニューに表示される。メニューのフレームにある既定の `on-subwindow-char` メソッドは、ショートカットキーの組み合わせが押されたときにメニュー項目へディスパッチする。

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-selectable-menu-item command event) → void? |
| event: (is-a?/c control-event%)                    |
+-----------------------------------------------------+
```

メニュー項目のコールバック手続きを呼び出す。コールバックは、`menu-item%` または `checkable-menu-item%` のインスタンスを作成するときに供給される。

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send a-selectable-menu-item get-shortcut) |
| → (or/c char? symbol? #f)                  |
+--------------------------------------------+
```

メニュー項目のキーボードショートカット文字または仮想キーを取得する。この文字またはキーは、`get-shortcut-prefix` が報告するショートカット接頭辞と組み合わせて使われる。

メニュー項目にショートカットがなければ `#f` が返る。

メニュー項目名のうちショートカット部分は、`get-label` が返すラベルには含まれない。

許可されるキーシンボルの一覧は `key-event%` の `get-key-code` を参照。ただし次は許可されない：`'shift`、`'control`、`'numlock`、`'scroll`、`'wheel-up`、`'wheel-down`、`'release`、および `'press`。

```
+--------------------------------------------------------------------------------+
| [method]                                                                       |
|                                                                                |
| (send a-selectable-menu-item get-shortcut-prefix)                              |
| → (and/c (listof (or/c 'alt 'cmd 'meta 'ctl 'shift 'option)) (λ (x) (implies   |
| (equal? 'unix (system-type)) (not (and (member 'alt x) (member 'meta x))))) (λ |
| (x) (equal? x (remove-duplicates x))))                                         |
| (and/c (listof (or/c 'alt 'cmd 'meta 'ctl                                      |
| 'shift 'option))                                                               |
| (λ (x) (implies (equal? 'unix (system-type))                                   |
| (not (and (member 'alt x)                                                      |
| (member 'meta x)))))                                                           |
| (λ (x) (equal? x (remove-duplicates x))))                                      |
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

メニュー項目のキーボードショートカットに使われるキーボード接頭辞を示すシンボルのリストを返す。リストに使えるシンボルは次のとおり。

- `'alt` — Meta（Windows および X のみ）
- `'cmd` — Command（Mac OS のみ）
- `'meta` — Meta（Unix のみ）
- `'ctl` — Control
- `'shift` — Shift
- `'option` — Option（Mac OS のみ）

Unix では、`'alt` と `'meta` のうち高々一方しか指定できない。`'alt` と `'meta` の違いは、メニュー上でのキー組み合わせの表示だけである。

既定のショートカット接頭辞は `get-default-shortcut-prefix` から取得できる。

`get-shortcut` が決めるショートカットキーは、通常報告されるキーコード、または other-Shift/AltGr キーコード（`key-event%` の `get-other-shift-key-code` などが生成するもの）のいずれかでキーイベントと照合される。ショートカットキーがキーコードシンボル、または ASCII の文字・数字である場合、ショートカットは接頭辞に列挙された修飾キーの正確な組み合わせにのみ一致する。一方、ASCII の文字・数字以外の文字ショートカットでは、接頭辞は最小限の修飾キー集合を決めるに過ぎず、その文字にアクセスするために追加の修飾キーが必要になることがある。例外として、Windows または Unix では、Alt/Meta キーの押下は接頭辞と正確に一致しなければならない（含まれるか含まれないか）。いずれの場合も、最も精密な一致が優先される。一致の順位付けについては `keymap%` の `map-function` を参照。

ショートカット接頭辞として空リストを使うこともできる。ただし、`frame%` の既定の `on-menu-char` メソッドは、キーイベントに非 Shift 修飾キーまたはファンクションキーが含まれるときにのみメニューショートカットを検査する。したがって、空のショートカット接頭辞は通常、ショートカットキーがファンクションキーである場合にのみ有用である。

```
+-------------------------------------------------------------+
| [method]                                                    |
|                                                             |
| (send a-selectable-menu-item set-shortcut shortcut) → void? |
| shortcut: (or/c char? symbol? #f)                          |
+-------------------------------------------------------------+
```

メニュー項目のキーボードショートカット文字を設定する。詳細は `get-shortcut` を参照。

ショートカット文字を `#f` に設定すると、そのメニュー項目はキーボードショートカットを持たない。

```
+-------------------------------------------------------------------------------+
| [method]                                                                      |
|                                                                               |
| (send a-selectable-menu-item set-shortcut-prefix prefix)                      |
| → void?                                                                       |
| prefix: (and/c (listof (or/c 'alt 'cmd 'meta 'ctl 'shift 'option)) (λ (x)    |
| (implies (equal? 'unix (system-type)) (not (and (member 'alt x) (member 'meta |
| x))))) (λ (x) (equal? x (remove-duplicates x))))                              |
| (and/c (listof (or/c 'alt 'cmd 'meta 'ctl                                     |
| 'shift 'option))                                                              |
| (λ (x) (implies (equal? 'unix (system-type))                                  |
| (not (and (member 'alt x)                                                     |
| (member 'meta x)))))                                                          |
| (λ (x) (equal? x (remove-duplicates x))))                                     |
|                                                                               |
| ```racket                                                                     |
| (and/c (listof (or/c 'alt 'cmd 'meta 'ctl                                     |
|                      'shift 'option))                                         |
|        (λ (x) (implies (equal? 'unix (system-type))                           |
|                        (not (and (member 'alt x)                              |
|                                  (member 'meta x)))))                         |
|        (λ (x) (equal? x (remove-duplicates x))))                              |
| ```                                                                           |
+-------------------------------------------------------------------------------+
```

メニュー項目のキーボードショートカットに使うキーボード接頭辞を示すシンボルのリストを設定する。

詳細は `get-shortcut-prefix` を参照。

---

## separator-menu-item%

```
+------------------------------------+--------------+
| classseparator-menu-item%: class? |              |
+------------------------------------+--------------+
| superclass: object%                |              |
| extends:                           | menu-item<%> |
+------------------------------------+--------------+
```

セパレータは、メニュー内の選択できない線である。親は `menu%` または `popup-menu%` でなければならない。

```
+-------------------------------------------------------+
| [constructor]                                         |
|                                                       |
| (new separator-menu-item% [parent parent])            |
| → (is-a?/c separator-menu-item%)                      |
| parent: (or/c (is-a?/c menu%) (is-a?/c popup-menu%)) |
+-------------------------------------------------------+
```

メニュー内に新しいセパレータを作成する。

---

## slider%

> [image: slider.png]

```
  +----------+
  | Label    |
  | [====| ] |  ← ハンドルをドラッグして値を変更
  +----------+
```

```
+-----------------------+------------+
| classslider%: class? |            |
+-----------------------+------------+
| superclass: object%   |            |
| extends:              | control<%> |
+-----------------------+------------+
```

スライダーオブジェクトは、ユーザがハンドルをドラッグしてコントロールの値を変更できるパネル項目である。各スライダーは固定の最小値と最大値を持つ。

ユーザがスライダーの値を変更するたびに、そのコールバック手続きが呼び出される。コールバック手続きは、各スライダーを作成するときの初期化引数として与える。

```
+------------------------------------------------------------------------------+
| [constructor]                                                                |
|                                                                              |
| (new slider%                                                                 |
| → (is-a?/c slider%)                                                          |
| label: (or/c label-string? #f)                                              |
| min-value: position-integer?                                                |
| max-value: position-integer?                                                |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c  |
| pane%))                                                                      |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                     |
| (is-a?/c panel%) (is-a?/c pane%))                                            |
| callback: ((is-a?/c slider%) (is-a?/c control-event%). ->. any) = (lambda |
| (b e) (void))                                                                |
| init-value: position-integer? = min-value                                   |
| style: (listof (or/c 'horizontal 'vertical 'upward 'plain 'vertical-label   |
| 'horizontal-label 'deleted)) = '(horizontal)                                 |
| (listof (or/c 'horizontal 'vertical 'upward 'plain                           |
| 'vertical-label 'horizontal-label                                            |
| 'deleted))                                                                   |
| font: (is-a?/c font%) = normal-control-font                                 |
| enabled: any/c = #t                                                         |
| vert-margin: spacing-integer? = 2                                           |
| horiz-margin: spacing-integer? = 2                                          |
| min-width: (or/c dimension-integer? #f) = #f                                |
| min-height: (or/c dimension-integer? #f) = #f                               |
| stretchable-width: any/c = (memq 'horizontal style)                         |
| stretchable-height: any/c = (memq 'vertical style)                          |
|                                                                              |
| ```racket                                                                    |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                     |
|       (is-a?/c panel%) (is-a?/c pane%))                                      |
| ```                                                                          |
|                                                                              |
| ```racket                                                                    |
| (listof (or/c 'horizontal 'vertical 'upward 'plain                           |
|               'vertical-label 'horizontal-label                              |
|               'deleted))                                                     |
| ```                                                                          |
+------------------------------------------------------------------------------+
```

`label` が文字列なら、それがスライダーのラベルとして使われる。そうでなければ、スライダーはラベルを表示しない。

`label` に `&` が現れる場合、`button%` と同様に特別に解析される。

`min-value` と `max-value` 引数はスライダーの範囲を（両端を含めて）指定する。`init-value` 引数は、任意にスライダーの初期値を指定する。列 `[min-value, init-value, max-value]` は非減少でなければならない。そうでなければ `exn:fail:contract` 例外が発生する。

`callback` 手続きは、ユーザがスライダーの値を変更したときに（イベント型 `'slider` で）呼ばれる。

`style` 引数は、左から右への水平スライダーなら `'horizontal`、上向きの垂直スライダーなら `'upward`、下向きの垂直スライダーなら `'vertical` のいずれかを含まなければならない（ただし `'vertical` は、上向きスライダーのみをサポートするシステムツールキットを持つ Mac OS では、誤解を招く色で描画されることがあるので注意）。`style` に `'plain` が含まれると、スライダーは範囲と現在値の数値をユーザに表示しない。`style` に `'vertical-label` が含まれると、ラベルがコントロールの上に付いたスライダーが作られる。`style` に `'vertical-label` が含まれない（任意で `'horizontal-label` を含む）場合、ラベルはスライダーの左に作られる。`style` に `'deleted` が含まれると、スライダーは非表示として作られ、親のジオメトリに影響しない。後から親の `add-child` メソッドを呼ぶことでアクティブにできる。

`font` 引数はコントロールのフォントを決める。`enabled` 引数については `window<%>` を参照。`horiz-margin` と `vert-margin` については `subarea<%>` を参照。`min-width`、`min-height`、`stretchable-width`、`stretchable-height` については `area<%>` を参照。

パッケージ `gui-lib` のバージョン 1.73 で変更: `'upward` as a possible style element. を追加。

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-slider get-value) → position-integer? |
+-----------------------------------------------+
```

現在のスライダー値を取得する。

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-slider set-value value) → void? |
| value: position-integer?               |
+-----------------------------------------+
```

スライダーの値（および表示位置）を設定する。（コントロールのコールバック手続きは呼び出されない。）`value` がスライダーの最小・最大範囲の外なら、`exn:fail:contract` 例外が発生する。

スライダーの値は、ユーザがコントロールをクリックすることでも変更でき、そのような変更はこのメソッドを経由しない。値の変化を監視するには、初期化引数として与えたコントロールのコールバック手続きを使う。

---

## snip-admin%

```
+---------------------------+
| classsnip-admin%: class? |
+---------------------------+
| superclass: object%       |
+---------------------------+
```

アドミニストレータの役割については Administrators を参照。`snip-admin%` クラスが直接インスタンス化されることはない。ほとんどのプログラマが派生クラスを通じてインスタンス化することもない。各 `text%` または `pasteboard%` オブジェクトが自身のアドミニストレータを作成する。ただし、新しい文脈でスニップを表示するためにこのクラスの新しいインスタンスを派生するのは有用な場合がある。また、所有されているスニップから既存のアドミニストレータのメソッドを呼ぶのも有用な場合がある。

新しい `snip-admin%` クラスを作るには、ここで述べるすべてのメソッドをオーバーライドしなければならない。それらはすべて、アドミニストレータのスニップから呼び出される。

`snip-admin%` オブジェクトは通常複数のスニップを所有するため、多くのメソッドは引数として `snip%` オブジェクトを要求する。

```
+-------------------------------------------+
| [constructor]                             |
|                                           |
| (new snip-admin%) → (is-a?/c snip-admin%) |
+-------------------------------------------+
```

（役に立たない）エディタアドミニストレータを作成する。

```
+--------------------------------------------------------+
| [method]                                               |
|                                                        |
| (send a-snip-admin get-dc) → (or/c (is-a?/c dc<%>) #f) |
+--------------------------------------------------------+
```

表示サイズ情報の決定に適した描画コンテキストを取得する。スニップが表示されていなければ `#f` が返る。

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-snip-admin get-editor)                 |
| → (or/c (is-a?/c text%) (is-a?/c pasteboard%)) |
+------------------------------------------------+
```

このアドミニストレータが（直接または間接に）報告する先のエディタを返す。

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-snip-admin get-view x y w h [snip]) → void?   |
| x: (or/c (box/c real?) #f)                           |
| y: (or/c (box/c real?) #f)                           |
| w: (or/c (box/c (and/c real? (not/c negative?))) #f) |
| h: (or/c (box/c (and/c real? (not/c negative?))) #f) |
| snip: (or/c (is-a?/c snip%) #f) = #f                 |
+-------------------------------------------------------+
```

仕様:
スニップ座標における、スニップの可視領域の位置とサイズを取得する。与えられたスニップがこのアドミニストレータに管理されていなければ、結果は未定義である。

`snip` が `#f` でなければ、スニップの現在の可視領域がボックス `x`、`y`、`w`、`h` に格納される。`x` と `y` の値はスニップの左上隅を基準とする。`w` と `h` の値はスニップ自体より大きくなり得る。

`snip` が `#f` なら、スニップのトップレベル表示の可視領域全体が、エディタ座標で返される。`snip` に `#f` を使うのは、`editor-admin%` の `get-view` で `full?` に `#t` を使うのと類似する。

スニップが指定されなければ、代わりにスニップのエディタの位置とサイズが、エディタ座標で返される。

あわせて `editor-admin%` の `get-view` も参照。

既定の実装:
すべてのボックスを `0.0` で埋める。

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-snip-admin get-view-size w h) → void?         |
| w: (or/c (box/c (and/c real? (not/c negative?))) #f) |
| h: (or/c (box/c (and/c real? (not/c negative?))) #f) |
+-------------------------------------------------------+
```

仕様:
アドミニストレータの表示領域の可視サイズを取得する。

表示がエディタキャンバスの場合は、`reflow-container` も参照。

既定の実装:
すべてのボックスを `0.0` で埋める。

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-snip-admin modified snip modified?) → void? |
| snip: (is-a?/c snip%)                              |
| modified?: any/c                                   |
+-----------------------------------------------------+
```

仕様:
スニップから呼ばれ、その変更状態が変更済みまたは未変更に変わったことを報告する。

既定の実装:
何もしない。

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-snip-admin needs-update     |
| snip: (is-a?/c snip%)              |
| localx: real?                      |
| localy: real?                      |
| w: (and/c real? (not/c negative?)) |
| h: (and/c real? (not/c negative?)) |
+-------------------------------------+
```

仕様:
スニップの表示の更新が必要であることを要求するためにスニップから呼ばれる。アドミニストレータが実際にいつスニップを更新するかを決める。最終的にスニップの `draw` メソッドが呼ばれる。

`localx`、`localy`、`w`、`h` 引数は、再描画するスニップの領域を（スニップ座標で）指定する。

与えられたスニップがこのアドミニストレータに管理されていなければ、更新は行われない。

既定の実装:
何もしない。

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send a-snip-admin popup-menu menu snip x y) → boolean? |
| menu: (is-a?/c popup-menu%)                            |
| snip: (is-a?/c snip%)                                  |
| x: real?                                               |
| y: real?                                               |
+---------------------------------------------------------+
```

仕様:
このスニップのエディタの表示内でポップアップメニューを開く。結果は、ポップアップが成功すれば `#t`、そうでなければ `#f`（ユーザがポップアップメニューの項目を選んだかどうかとは独立）。

メニューはスニップ座標の `x` と `y` に配置される。

メニューがポップアップされている間、そのターゲットはこのスニップのエディタの表示におけるトップレベルエディタに設定される。詳細は `get-popup-target` を参照。

既定の実装:
`#f` を返す。

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-snip-admin recounted snip refresh?) → void? |
| snip: (is-a?/c snip%)                              |
| refresh?: any/c                                    |
+-----------------------------------------------------+
```

仕様:
指定されたスニップがカウントを変更したことをアドミニストレータに通知するためにスニップから呼ばれる。スニップは通常、カウント変更後に更新が必要だが、更新を直ちに行うかどうかはスニップが決める。

`refresh?` が `#f` でなければ、スニップは直ちに更新されることを要求している。そうでなければ、最終的に `needs-update` も呼ばれなければならない。

与えられたスニップがこのアドミニストレータに管理されていなければ、メソッド呼び出しは無視される。

既定の実装:
何もしない。

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-snip-admin release-snip snip) → boolean? |
| snip: (is-a?/c snip%)                           |
+--------------------------------------------------+
```

仕様:
指定されたスニップの解放を要求する。このアドミニストレータがスニップの所有者でない、またはスニップを解放できない場合は `#f` が返る。そうでなければ `#t` が返り、スニップはもはや所有されない。

あわせて `editor<%>` の `release-snip` も参照。

与えられたスニップがこのアドミニストレータに管理されていなければ結果は `#f` である。

既定の実装:
`#f` を返す。

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send a-snip-admin resized snip refresh?) → void? |
| snip: (is-a?/c snip%)                            |
| refresh?: any/c                                  |
+---------------------------------------------------+
```

仕様:
指定されたスニップが表示サイズを変更したことをアドミニストレータに通知するためにスニップから呼ばれる。スニップは通常、リサイズ後に更新が必要だが、更新を直ちに行うかどうかはスニップが決める。

`refresh?` が `#f` でなければ、スニップは `needs-update` を呼ぶのと同様に直ちに更新されることを要求している。そうでなければ、最終的に `needs-update` も呼ばれなければならない。

与えられたスニップがこのアドミニストレータに管理されていなければ、メソッド呼び出しは無視される。

既定の実装:
何もしない。

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-snip-admin scroll-to            |
| snip: (is-a?/c snip%)                  |
| localx: real?                          |
| localy: real?                          |
| w: (and/c real? (not/c negative?))     |
| h: (and/c real? (not/c negative?))     |
| refresh?: any/c                        |
| bias: (or/c 'start 'end 'none) = 'none |
+-----------------------------------------+
```

仕様:
与えられた領域が見えるようにスクロールすることを要求するためにスニップから呼ばれる。スニップは通常、スクロール後に更新が必要だが、更新を直ちに行うかどうかはスニップが決める。

`localx`、`localy`、`w`、`h` 引数は、スクロールによって可視にするスニップの領域を（スニップ座標で）指定する。

`refresh?` が `#f` でなければ、エディタは直ちに更新されることを要求している。

`bias` 引数は次のいずれかである。

- `'start` — 範囲が可視領域に収まらない場合、左上の領域を示す
- `'none` — 特別なスクロール指示なし
- `'end` — 範囲が可視領域に収まらない場合、右下の領域を示す

結果は、エディタがスクロールされれば `#t`、そうでなければ `#f`。

与えられたスニップがこのアドミニストレータに管理されていなければ、メソッド呼び出しは無視され（結果は `#f`）、

既定の実装:
`#f` を返す。

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-snip-admin set-caret-owner          |
| snip: (is-a?/c snip%)                      |
| domain: (or/c 'immediate 'display 'global) |
+---------------------------------------------+
```

仕様:
キーボードフォーカスが指定されたスニップに割り当てられることを要求する。要求が認められると、スニップの `own-caret` メソッドが呼ばれる。

`domain` の取り得る値については `set-caret-owner` を参照。

与えられたスニップがこのアドミニストレータに管理されていなければ、メソッド呼び出しは無視される。

既定の実装:
何もしない。

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-snip-admin update-cursor) → void? |
+-------------------------------------------+
```

仕様:
このスニップのエディタの表示におけるカーソルの更新をキューに入れる。実際に使われるカーソルは、適宜スニップの `adjust-cursor` メソッドを呼んで決定される。

既定の実装:
何もしない。

```
+--------------------------------------+
| [method]                             |
|                                      |
| (send a-snip-admin get-line-spacing) |
| → (and/c real? (not/c negative?))    |
+--------------------------------------+
```

仕様:
スニップのエディタが各行の間に挿入する間隔を返す。
既定の実装:
`0.0` を返す。

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-snip-admin get-selected-text-color) |
| → (or/c (is-a?/c color%) #f)                |
+---------------------------------------------+
```

仕様:
選択されたテキストの描画に使われる色を返す。選択テキストが通常の色で描画される場合は `#f`。
既定の実装:
`#f` を返す。

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-snip-admin call-with-busy-cursor thunk) → any |
| thunk: (-> any)                                      |
+-------------------------------------------------------+
```

仕様:
現在のイベントスペース内のすべてのウィンドウのカーソルをウォッチカーソルに変えながら `thunk` を呼ぶ。

既定の実装:
何もしない。

```
+------------------------------------------------------------+
| [method]                                                   |
|                                                            |
| (send a-snip-admin get-tabs                                |
| length: (or/c (box/c exact-nonnegative-integer?) #f) = #f |
| tab-width: (or/c (box/c real?) #f) = #f                   |
| in-units: (or/c (box/c any/c) #f) = #f                    |
+------------------------------------------------------------+
```

仕様: 現在のタブ位置配列をリストとして返す。

`length` ボックスは、`length` が `#f` でなければ、タブ配列の長さ（したがって返されるリストの長さ）で埋められる。
`tab-width` ボックスは、`tab-width` が `#f` でなければ、タブ配列の末尾を超えたタブに使われる幅で埋められる。
`in-units` ボックスは、`in-units` が `#f` でなければ、タブがキャンバス単位で指定されていれば `#t`、スペース幅で指定されていれば `#f` で埋められる。

既定の実装: `null` を返す。

---

## snip-class-list<%>

```
+------------------------------------------+
| interfacesnip-class-list<%>: interface? |
+------------------------------------------+
+------------------------------------------+
```

各イベントスペースは、`(get-the-snip-class-list)` で得られる独自の `snip-class-list<%>` インスタンスを持つ。新しいインスタンスを直接作成することはできない。各インスタンスはスニップクラスのリストを保持する。このリストは、ファイルからスニップを読み込むために必要である。あわせて Snip Classes も参照。

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-snip-class-list add snipclass) → void? |
| snipclass: (is-a?/c snip-class%)              |
+------------------------------------------------+
```

スニップクラスをリストに追加する。同じ名前のクラスがすでにリストにあれば、これは追加されない。

```
+------------------------------------+
| [method]                           |
|                                    |
| (send a-snip-class-list find name) |
| → (or/c (is-a?/c snip-class%) #f)  |
| name: string?                     |
+------------------------------------+
```

与えられた名前のスニップクラスをリストから探し、見つからなければ `#f` を返す。

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-snip-class-list find-position class) |
| → exact-nonnegative-integer?                 |
| class: (is-a?/c snip-class%)                |
+----------------------------------------------+
```

指定されたクラスのリスト内インデックスを返す。

```
+-----------------------------------+
| [method]                          |
|                                   |
| (send a-snip-class-list nth n)    |
| → (or/c (is-a?/c snip-class%) #f) |
| n: exact-nonnegative-integer?    |
+-----------------------------------+
```

リストの n 番目のクラスを返す。リストのクラス数が n 以下なら `#f`。

```
+--------------------------------------------------------------+
| [method]                                                     |
|                                                              |
| (send a-snip-class-list number) → exact-nonnegative-integer? |
+--------------------------------------------------------------+
```

リスト内のスニップクラスの数を返す。

---

## snip-class%

```
+---------------------------+
| classsnip-class%: class? |
+---------------------------+
| superclass: object%       |
+---------------------------+
```

有用なスニップクラスは、`snip-class%` の派生サブクラスをインスタンス化して定義する。`snip-class%` から派生したクラスは、スニップのための一種の「メタクラス」として働き、各スニップはそのスニップクラスとして `snip-class%` のインスタンスと関連付けられる。新しいスニップクラスの派生については Implementing New Snips を参照。

```
+-------------------------------------------+
| [constructor]                             |
|                                           |
| (new snip-class%) → (is-a?/c snip-class%) |
+-------------------------------------------+
```

（役に立たない）スニップクラスを作成する。

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-snip-class get-classname) → string? |
+---------------------------------------------+
```

クラスの名前を返す。これはこのスニップクラスを一意に指定する文字列である。たとえば、標準のテキストスニップのクラス名は `"wxtext"` である。`wx` で始まる名前は予約されている。

スニップクラス名は通常、クラスのオンデマンド読み込みを可能にするために `"((lib...)\n(lib...))"` の形を取るべきである。詳細は Snip Classes を参照。

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-snip-class get-version) → exact-integer? |
+--------------------------------------------------+
```

このスニップクラスのバージョンを返す。同じクラス名だが異なるバージョンのスニップを含むファイルを読み込もうとすると、ユーザに警告が出る。

```
+--------------------------------------------------------+
| [method]                                               |
|                                                        |
| (send a-snip-class read f) → (or/c (is-a?/c snip%) #f) |
| f: (is-a?/c editor-stream-in%)                        |
+--------------------------------------------------------+
```

仕様:
与えられたストリームからスニップを読み取り、新しく作成したスニップを結果として返す。エラーがあれば `#f`。

既定の実装:
`#f` を返す。

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-snip-class read-header f) → boolean? |
| f: (is-a?/c editor-stream-in%)              |
+----------------------------------------------+
```

仕様:
このクラスで読み取るすべてのスニップに有用かもしれないヘッダ情報を読むために呼ばれる。このメソッドはエディタ読み取りセッションごとに一度だけ呼ばれ、しかもストリームにこのクラスのヘッダ情報が含まれる場合に限る。

戻り値は、読み取りエラーが起きれば `#f`、そうでなければそれ以外の値。

あわせて `write-header` も参照。

既定の実装:
`#t` を返す。

```
+-------------------------------------------------------------+
| [method]                                                    |
|                                                             |
| (send a-snip-class reading-version stream) → exact-integer? |
| stream: (is-a?/c editor-stream-in%)                        |
+-------------------------------------------------------------+
```

与えられたストリームから現在読み取られているスニップについて、このスニップクラスに指定されたバージョン番号を返す。

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-snip-class set-classname name) → void? |
| name: string?                                 |
+------------------------------------------------+
```

クラスの名前を設定する。あわせて `get-classname` も参照。

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-snip-class set-version v) → void? |
| v: exact-integer?                        |
+-------------------------------------------+
```

このクラスのバージョンを設定する。`get-version` を参照。

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-snip-class write-header stream) → boolean? |
| stream: (is-a?/c editor-stream-out%)              |
+----------------------------------------------------+
```

仕様:
このクラスで書き出すすべてのスニップに有用かもしれないヘッダ情報を書くために呼ばれる。このメソッドはエディタ書き出しセッションごとに一度だけ呼ばれ、しかもエディタにこのクラスのスニップが含まれる場合に限る。

スニップを読み戻すとき、`read-header` は `write-header` がストリームに何らかのデータを書いた場合にのみ呼ばれる。

戻り値は、書き出しエラーが起きれば `#f`、そうでなければそれ以外の値。

既定の実装:
`#t` を返す。

---

## snip%

```
+---------------------+----------+
| classsnip%: class? |          |
+---------------------+----------+
| superclass: object% |          |
| extends:            | equal<%> |
+---------------------+----------+
```

`snip%` の直接のインスタンスは面白くない。有用なスニップは派生サブクラスをインスタンス化して定義するが、`snip%` クラスは基本機能を定義する。新しいスニップクラスの派生については Implementing New Snips を参照。

```
+-------------------------------+
| [constructor]                 |
|                               |
| (new snip%) → (is-a?/c snip%) |
+-------------------------------+
```

長さ 1 の平易なスニップを、`the-style-list` の `"Basic"` スタイルで作成する。

```
+--------------------------------+
| [method]                       |
|                                |
| (send a-snip adjust-cursor     |
| → (or/c (is-a?/c cursor%) #f)  |
| dc: (is-a?/c dc<%>)           |
| x: real?                      |
| y: real?                      |
| editorx: real?                |
| editory: real?                |
| event: (is-a?/c mouse-event%) |
+--------------------------------+
```

仕様:
エディタ内でカーソルがスニップの上に移動したときに使うカーソル画像を決めるために呼ばれる。`#f` が返れば、エディタが既定のカーソルを選ぶ。（詳細は `editor<%>` の `adjust-cursor` を参照。）

既定の実装:
`#f` を返す。

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send a-snip blink-caret dc x y) → void? |
| dc: (is-a?/c dc<%>)                     |
| x: real?                                |
| y: real?                                |
+------------------------------------------+
```

スニップに選択キャレットを点滅させるよう指示する。このメソッドは、スニップのエディタの表示がキーボードフォーカスを持ち、かつスニップがエディタ局所フォーカスを持つときに、周期的に呼ばれる。

描画コンテキストと、描画コンテキスト座標におけるスニップの位置が与えられる。

```
+-------------------------------------------------------------------+
| [method]                                                          |
|                                                                   |
| (send a-snip can-do-edit-operation?                               |
| op: (or/c 'undo 'redo 'clear 'cut 'copy 'paste 'kill 'select-all |
| 'insert-text-box 'insert-pasteboard-box 'insert-image)            |
| (or/c 'undo 'redo 'clear 'cut 'copy                               |
| 'paste 'kill 'select-all                                          |
| 'insert-text-box 'insert-pasteboard-box                           |
| 'insert-image)                                                    |
| recursive?: any/c = #t                                           |
|                                                                   |
| ```racket                                                         |
| (or/c 'undo 'redo 'clear 'cut 'copy                               |
|       'paste 'kill 'select-all                                    |
|       'insert-text-box 'insert-pasteboard-box                     |
|       'insert-image)                                              |
| ```                                                               |
+-------------------------------------------------------------------+
```

`editor<%>` の `can-do-edit-operation?` を参照。

スニップのエディタのメソッドが呼ばれ、`recursive?` が `#f` でなく、かつこのスニップがキャレットを所有しているときに呼ばれる。

```
+--------------------------------------+
| [method]                             |
|                                      |
| (send a-snip copy) → (is-a?/c snip%) |
+--------------------------------------+
```

このスニップのコピーを作成して返す。`copy` メソッドは、このスニップのスタイル（`get-style` が返すもの）を新しいスニップへコピーする責任を持つ。

```
+-------------------------------------------------------------------+
| [method]                                                          |
|                                                                   |
| (send a-snip do-edit-operation                                    |
| op: (or/c 'undo 'redo 'clear 'cut 'copy 'paste 'kill 'select-all |
| 'insert-text-box 'insert-pasteboard-box 'insert-image)            |
| (or/c 'undo 'redo 'clear 'cut 'copy                               |
| 'paste 'kill 'select-all                                          |
| 'insert-text-box 'insert-pasteboard-box                           |
| 'insert-image)                                                    |
| recursive?: any/c = #t                                           |
| time: exact-integer? = 0                                         |
|                                                                   |
| ```racket                                                         |
| (or/c 'undo 'redo 'clear 'cut 'copy                               |
|       'paste 'kill 'select-all                                    |
|       'insert-text-box 'insert-pasteboard-box                     |
|       'insert-image)                                              |
| ```                                                               |
+-------------------------------------------------------------------+
```

`editor<%>` の `do-edit-operation` を参照。

スニップのエディタのメソッドが呼ばれ、`recursive?` が `#f` でなく、かつこのスニップがキャレットを所有しているときに呼ばれる。

```
+-----------------------------------------------------------------------+
| [method]                                                              |
|                                                                       |
| (send a-snip draw                                                     |
| dc: (is-a?/c dc<%>)                                                  |
| x: real?                                                             |
| y: real?                                                             |
| left: real?                                                          |
| top: real?                                                           |
| right: real?                                                         |
| bottom: real?                                                        |
| dx: real?                                                            |
| dy: real?                                                            |
| draw-caret: (or/c 'no-caret 'show-inactive-caret 'show-caret (cons/c |
| exact-nonnegative-integer? exact-nonnegative-integer?))               |
| (or/c 'no-caret 'show-inactive-caret 'show-caret                      |
| (cons/c exact-nonnegative-integer?                                    |
| exact-nonnegative-integer?))                                          |
|                                                                       |
| ```racket                                                             |
| (or/c 'no-caret 'show-inactive-caret 'show-caret                      |
|       (cons/c exact-nonnegative-integer?                              |
|               exact-nonnegative-integer?))                            |
| ```                                                                   |
+-----------------------------------------------------------------------+
```

仕様:
（エディタによって）呼ばれ、与えられた描画コンテキストへ、スニップの左上隅を DC 座標の位置 `(x, y)` に置いてスニップを描画する。

引数 `left`、`top`、`right`、`bottom` は（DC 座標の）クリッピング領域を定義し、スニップは描画の最適化に使えるが、これらの引数を無視してもよい。

`dx` と `dy` 引数は、`x` と `y` から減算するとスニップのエディタ座標での位置が得られる数を与える（描画に使う DC 座標とは対照的）。

`draw-caret` については Caret Ownership を参照。`draw-caret` がペアのときは、選択領域の背景を描かないこと。また `(get-highlight-text-color)` が（`#f` ではなく）色を返すなら、選択されたテキストやその他の選択された前景要素の描画にその色を使うこと。

このメソッドが呼ばれる前に、スニップのスタイルのフォント、テキスト色、ペン色が描画コンテキストに設定されている。（描画コンテキストは `get-extent` や `partial-offset` ではそのように構成されない。）`draw` メソッドは、クリッピング領域がすでに適切に設定されていることを除き、描画コンテキストの状態について他の仮定をしてはならない。`draw` が戻る前に、変更した描画コンテキスト設定をすべて復元しなければならない。

あわせて `editor<%>` の `on-paint` も参照。

このメソッドが呼ばれるとき、スニップのエディタは通常、書き込みとリフローについて内部ロックされている（Internal Editor Locks も参照）。また通常はリフレッシュ中である（Editors and Threads を参照）。

既定の実装:
何も描画しない。

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-snip equal-to? snip equal?) → boolean? |
| snip: (is-a?/c snip%)                         |
| equal?: (-> any/c any/c boolean?)             |
+------------------------------------------------+
```

仕様: `equal<%>` を参照。

既定の実装: マルチメソッドディスパッチを模擬するため、`snip` の `other-equal-to?` メソッドを呼ぶ。`snip` がより具体的な同値比較を提供する場合に備える。

```
+------------------------------------------------------+
| [method]                                             |
|                                                      |
| (send a-snip other-equal-to? that equal?) → boolean? |
| that: (is-a?/c snip%)                               |
| equal?: (-> any/c any/c boolean?)                   |
+------------------------------------------------------+
```

既定の実装: `(eq? a-snip that)` を返す。

```
+-------------------------------------------------------------+
| [method]                                                    |
|                                                             |
| (send a-snip equal-hash-code-of hash-code) → exact-integer? |
| hash-code: (any/c. ->. exact-integer?)                   |
+-------------------------------------------------------------+
```

仕様: `equal<%>` を参照。

既定の実装: `(eq-hash-code a-snip)` を返す。

```
+------------------------------------------------------+
| [method]                                             |
|                                                      |
| (send a-snip equal-secondary-hash-code-of hash-code) |
| → exact-integer?                                     |
| hash-code: (any/c. ->. exact-integer?)            |
+------------------------------------------------------+
```

仕様: `equal<%>` を参照。

既定の実装: `1` を返す。

```
+---------------------------------------------------------------+
| [method]                                                      |
|                                                               |
| (send a-snip find-scroll-step y) → exact-nonnegative-integer? |
| y: real?                                                     |
+---------------------------------------------------------------+
```

仕様:
スニップが複数の垂直スクロールステップを含む場合（`get-num-scroll-steps` を参照）、スニップ内の与えられた y オフセットに対するスクロールステップオフセットを求めるためにこのメソッドが呼ばれる。

既定の実装:
`0` を返す。

```
+-----------------------------------------------------------+
| [method]                                                  |
|                                                           |
| (send a-snip get-admin) → (or/c (is-a?/c snip-admin%) #f) |
+-----------------------------------------------------------+
```

このスニップのアドミニストレータを返す。（スニップが所有されていてもエディタ内で可視でなければ、アドミニストレータは `#f` になり得る。）

```
+------------------------------------------------------+
| [method]                                             |
|                                                      |
| (send a-snip get-count) → exact-nonnegative-integer? |
+------------------------------------------------------+
```

スニップのカウント（すなわち、スニップ内の項目数）を返す。

```
+---------------------------------------------------------------+
| [method]                                                      |
|                                                               |
| (send a-snip get-grapheme-count) → exact-nonnegative-integer? |
+---------------------------------------------------------------+
```

スニップ内の書記素数を返す。通常は `get-count` と同じ結果だが、連続する複数の項目が一つの書記素を形成する場合はより小さくなり得る。

パッケージ `snip-lib` のバージョン 1.4 で追加。

```
+----------------------------------------------------------------+
| [method]                                                       |
|                                                                |
| (send a-snip grapheme-position n) → exact-nonnegative-integer? |
| n: exact-nonnegative-integer?                                 |
+----------------------------------------------------------------+
```

スニップ内で最初の `n` 個の書記素を形成する項目数を返す。あるいは同等に、書記素ベースの位置から項目ベースの位置へ変換する。

`get-count` が `get-grapheme-count` と同じとき、このメソッドは `n` を返す。

パッケージ `snip-lib` のバージョン 1.4 で追加。

```
+------------------------------------------------------------------+
| [method]                                                         |
|                                                                  |
| (send a-snip get-extent                                          |
| dc: (is-a?/c dc<%>)                                             |
| x: real?                                                        |
| y: real?                                                        |
| w: (or/c (box/c (and/c real? (not/c negative?))) #f) = #f       |
| h: (or/c (box/c (and/c real? (not/c negative?))) #f) = #f       |
| descent: (or/c (box/c (and/c real? (not/c negative?))) #f) = #f |
| space: (or/c (box/c (and/c real? (not/c negative?))) #f) = #f   |
| lspace: (or/c (box/c (and/c real? (not/c negative?))) #f) = #f  |
| rspace: (or/c (box/c (and/c real? (not/c negative?))) #f) = #f  |
+------------------------------------------------------------------+
```

仕様:
スニップの幅、高さ、ディセント（ベースラインより下に描かれる高さの量）、スペース（上端の「埋め」空間としての高さの量）、および水平スペース（左右の「埋め」空間としての幅の量）を計算する。それらの値は、ボックス `w`、`h`、`descent`、`space`、`lspace`、`rspace` を埋めることで返される。

このメソッドはスニップのアドミニストレータから呼ばれる。他者が直接呼ぶことは通常ない。スニップの大きさを得るには `editor<%>` の `get-snip-location` を使う。

フォントサイズの調査のために描画コンテキストが与えられるが、描画は行ってはならない。`get-extent` と `partial-offset` メソッドは、適切にスケールされていることを除き、描画コンテキストの状態について仮定してはならない。特に、メソッドが呼ばれる前にスニップのスタイルのフォントが描画コンテキストに自動設定されることはない。（多くのスニップはサイズ情報をキャッシュするため、フォントの自動設定は無駄になる。）`get-extent` または `partial-offset` が描画コンテキストの設定を変える場合、戻る前にそれらを復元しなければならない。ただし、メソッドは描画コンテキストを変更する必要がないはずである。デバイスコンテキストからの計測結果に影響し得るのはフォント設定だけであり、`dc<%>` の `get-text-extent` は、そのデバイスコンテキストの現在フォントを上書きする `font%` 引数を受け取る。

スニップの左と上の位置が、エディタ座標の `x` と `y` として与えられる。スニップのサイズがその位置に依存する場合に備え、`x` と `y` 引数は通常は無視される。テキストエディタでは、y 座標は行の上端位置であり、スニップの実際の上端位置は高さが分かるまで未確定であり得る。

スニップが将来の応答のために結果サイズをキャッシュする場合、`size-cache-invalid` が呼ばれたときにキャッシュサイズを無効化すべきである（特にスニップのサイズが何らかのデバイスコンテキスト属性に依存する場合）。

`get-extent` への呼び出しを受けたあと、`size-cache-invalid` への呼び出しを受ける前にスニップのサイズが変わった場合、スニップはアドミニストレータにサイズ変更を通知しなければならず、アドミニストレータが派生サイズ情報を再計算できるようにする。サイズ変更の通知は、アドミニストレータの `resized` メソッドを呼んで行う。

このメソッドが呼ばれるとき、スニップのエディタは通常、書き込みとリフローについて内部ロックされている（Internal Editor Locks も参照）。

既定の実装:
すべてのボックスを `0.0` で埋める。

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send a-snip get-flags) → (listof symbol?) |
+--------------------------------------------+
```

スニップの振る舞いを定義するフラグを返す。次のシンボルのリストである。

- `'is-text` — `string-snip%` から派生したテキストスニップである。このフラグを設定してはならない
- `'can-append` — このスニップは同型の別スニップとマージできる
- `'invisible` — 改行など、ユーザには見えない不可視スニップ
- `'hard-newline` — スニップのあとに改行が続かなければならない
- `'newline` — 現在スニップのあとに改行が続いている。このフラグを設定すべきなのは所有エディタのみ
- `'handles-events` — キーボードフォーカスを持つとき、このスニップはキーボードおよびマウスイベントを処理できる
- `'handles-all-mouse-events` — キーボードフォーカスを持たなくても、スニップに触れるマウスイベント、またはスニップに触れたイベントの直後のマウスイベントを処理できる（`on-goodbye-event` も参照）
- `'handles-between-events` — スニップ内の項目の間のマウスイベントを処理する（代わりに既定でマウスクリックを位置設定や、`text%` / `pasteboard%` レベルで起きる他のイベント処理として扱うのではなく）
- `'width-depends-on-x` — このスニップの表示幅は、エディタ内でのスニップの x 位置に依存する（例: タブ）
- `'height-depends-on-y` — このスニップの表示高さは、エディタ内でのスニップの y 位置に依存する
- `'width-depends-on-y` — このスニップの表示幅は、エディタ内でのスニップの y 位置に依存する
- `'height-depends-on-x` — このスニップの表示高さは、エディタ内でのスニップの x 位置に依存する
- `'uses-editor-path` — このスニップはエディタのパス名を使い、名前が変わったときに通知を受けるべきである。通知は `set-admin` への冗長な呼び出しとして与えられる

```
+------------------------------------+
| [method]                           |
|                                    |
| (send a-snip get-num-scroll-steps) |
| → exact-nonnegative-integer?       |
+------------------------------------+
```

仕様:
スニップ内の水平スクロールステップ数を返す。ほとんどのスニップでは 1 である。埋め込みエディタスニップはこのメソッドを使い、所有エディタでのスクロールが埋め込みエディタ内の行を段階的に進むようにする。

既定の実装:
`1` を返す。

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-snip get-scroll-step-offset offset) |
| → (and/c real? (not/c negative?))           |
| offset: exact-nonnegative-integer?         |
+---------------------------------------------+
```

仕様: スニップが複数の垂直スクロールステップを含む場合（`get-num-scroll-steps` を参照）、与えられたスクロールオフセットに対するスニップ内の y オフセットを求めるためにこのメソッドが呼ばれる。

既定の実装:
`0.0` を返す。

```
+---------------------------------------------------------------+
| [method]                                                      |
|                                                               |
| (send a-snip get-snipclass) → (or/c #f (is-a?/c snip-class%)) |
+---------------------------------------------------------------+
```

スニップのクラスを返す。ファイル保存およびカット＆ペーストに使われる。

このメソッドは `set-snipclass` が格納したスニップクラスを返すため、オーバーライドする意図はない。

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-snip get-style) → (is-a?/c style<%>) |
+----------------------------------------------+
```

スニップのスタイルを返す。あわせて `set-style` も参照。

```
+----------------------------------------------------------+
| [method]                                                 |
|                                                          |
| (send a-snip get-text offset num [flattened?]) → string? |
| offset: exact-nonnegative-integer?                      |
| num: exact-nonnegative-integer?                         |
| flattened?: any/c = #f                                  |
+----------------------------------------------------------+
```

仕様:
スニップ内の位置 `offset` から始まり、合計 `num` 項目分続く、このスニップのテキストを返す。`offset` がスニップのカウントより大きければ `""` が返る。`num` がスニップのカウントからオフセットを引いた値より大きければ、オフセットからスニップ末尾までのテキストが返る。

`flattened?` が `#f` でなければ、平坦化されたテキストが返る。平坦化テキストと非平坦化テキストの議論については Flattened Text を参照。

既定の実装:
`""` を返す。

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-snip get-text!                      |
| buffer: (and/c string? (not/c immutable?)) |
| offset: exact-nonnegative-integer?         |
| num: exact-nonnegative-integer?            |
| buffer-offset: exact-nonnegative-integer?  |
+---------------------------------------------+
```

仕様:
非平坦化モードの `get-text` と同様だが、文字は新しく割り当てた文字列で返すのではなく、与えられた可変文字列に書き込む。

`buffer` 文字列は位置 `buffer-offset` から埋められる。`buffer` 文字列は少なくとも `num+buffer-offset` 文字の長さでなければならない。

既定の実装:
`get-text` を呼ぶ。ただし `string-snip%` の場合は `buffer` が直接埋められる。

```
+------------------------------------+
| [method]                           |
|                                    |
| (send a-snip is-owned?) → boolean? |
+------------------------------------+
```

このスニップに所有者がいれば `#t`、いなければ `#f` を返す。なお、スニップは挿入されたあとエディタから削除されても、まだエディタのアンドゥ履歴にあればエディタに所有され得る。

```
+--------------------------------------+
| [method]                             |
|                                      |
| (send a-snip match? snip) → boolean? |
| snip: (is-a?/c snip%)               |
+--------------------------------------+
```

仕様:
`a-snip` が `snip` に「一致」すれば `#t`、そうでなければ `#f` を返す。

既定の実装:
スニップと `a-snip` が同じクラスから来ており、同じ長さを持つなら `#t` を返す。

```
+-----------------------------------------------------------+
| [method]                                                  |
|                                                           |
| (send a-snip merge-with prev) → (or/c (is-a?/c snip%) #f) |
| prev: (is-a?/c snip%)                                    |
+-----------------------------------------------------------+
```

仕様:
`a-snip` を `prev` とマージする。スニップをマージできなければ `#f`、そうでなければ新しいマージ済みスニップを返す。このメソッドは、両スニップが同じクラスから来ており、かつ両方に `'can-append` フラグがある場合にのみ呼ばれる。

返されたスニップが期待されるカウントを持たなければ、そのカウントは強制的に修正される。返されたスニップがすでに別のアドミニストレータに所有されていれば、代理スニップが作成される。

このメソッドが呼ばれるとき、スニップのエディタは通常、読み取りについて内部ロックされている（Internal Editor Locks も参照）。

既定の実装:
`#f` を返す。

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-snip next) → (or/c (is-a?/c snip%) #f) |
+------------------------------------------------+
```

このスニップを所有するエディタ内の次のスニップを返す。これが最後のスニップなら `#f`。

テキストエディタでは、次のスニップはこのスニップの（最後の）位置に続く位置にあるスニップである。ペーストボードでは、次のスニップはこのスニップの直後の背後にあるスニップである。（ペーストボードにおけるスニップ順序については Editor Structure and Terminology を参照。）

```
+------------------------------+
| [method]                     |
|                              |
| (send a-snip on-char         |
| dc: (is-a?/c dc<%>)         |
| x: real?                    |
| y: real?                    |
| editorx: real?              |
| editory: real?              |
| event: (is-a?/c key-event%) |
+------------------------------+
```

仕様:
このスニップがキーボードフォーカスを持ち、イベントを処理できるときに、キーボードイベントを処理するために呼ばれる。描画コンテキストに加え、表示座標におけるスニップの位置（イベントは表示座標を使う）と、エディタ座標におけるスニップの位置が与えられる。

`x` と `y` 引数は表示座標におけるスニップの位置である。`editorx` と `editory` 引数はエディタ座標におけるスニップの位置である。イベントの x 位置をスニップ座標で得るには、`(send event get-x)` から `x` を引く。

あわせて `get-flags` の `'handles-events` も参照。

既定の実装:
何もしない。

```
+--------------------------------+
| [method]                       |
|                                |
| (send a-snip on-event          |
| dc: (is-a?/c dc<%>)           |
| x: real?                      |
| y: real?                      |
| editorx: real?                |
| editory: real?                |
| event: (is-a?/c mouse-event%) |
+--------------------------------+
```

仕様:
このスニップがイベントを処理でき、かつキーボードフォーカスを持つときに、スニップ上のマウスイベントを処理するために呼ばれる。引数については `on-char` を参照。

`x` と `y` 引数は表示座標におけるスニップの位置である。`editorx` と `editory` 引数はエディタ座標におけるスニップの位置である。イベントの x 位置をスニップ座標で得るには、`(send event get-x)` から `x` を引く。

あわせて `get-flags` の `'handles-events` も参照。

既定の実装:
何もしない。

```
+--------------------------------+
| [method]                       |
|                                |
| (send a-snip on-goodbye-event  |
| dc: (is-a?/c dc<%>)           |
| x: real?                      |
| y: real?                      |
| editorx: real?                |
| editory: real?                |
| event: (is-a?/c mouse-event%) |
+--------------------------------+
```

仕様:
実際には別のスニップを狙ったイベントを処理し、マウスが離れるときにこのスニップが後始末できる機会を与えるために呼ばれる。引数は `on-event` と同じ。

このメソッドは、スニップに `'handles-all-mouse-events` フラグが設定されているときにのみ呼ばれる（`get-flags` と `set-flags` を参照）。

既定の実装:
このオブジェクトの `on-event` メソッドを呼ぶ。

パッケージ `snip-lib` のバージョン 1.1 で追加。

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-snip own-caret own-it?) → void? |
| own-it?: any/c                         |
+-----------------------------------------+
```

仕様:
ある表示においてキャレット（キーボードフォーカスの所有を示す）を表示することが許される／許されないことをスニップに通知する。このメソッドは、キャレットを実際に表示または非表示にする要求として呼ばれるのではなく、すべての表示要求は `draw` メソッドが呼ばれて行われる。

`own-it?` 引数は、スニップがキーボードフォーカスを所有していれば `#t`、そうでなければ `#f`。

既定の実装:
何もしない。

```
+----------------------------------------------------------------+
| [method]                                                       |
|                                                                |
| (send a-snip position-grapheme n) → exact-nonnegative-integer? |
| n: exact-nonnegative-integer?                                 |
+----------------------------------------------------------------+
```

スニップ内で最初の `n` 項目が形成する書記素数を返す。あるいは同等に、項目ベースの位置から書記素ベースの位置へ変換する。

`get-count` が `get-grapheme-count` と同じとき、このメソッドは `n` を返す。

パッケージ `snip-lib` のバージョン 1.4 で追加。

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-snip partial-offset dc x y len) → real? |
| dc: (is-a?/c dc<%>)                            |
| x: real?                                       |
| y: real?                                       |
| len: exact-nonnegative-integer?                |
+-------------------------------------------------+
```

仕様:
最初のスニップ項目から始まり `len` 項目続く、スニップの部分幅を計算する。描画コンテキストと、エディタ座標におけるスニップの位置が与えられる。あわせて `get-extent` も参照。

このメソッドが呼ばれるとき、スニップのエディタは通常、書き込みとリフローについて内部ロックされている（Internal Editor Locks も参照）。

既定の実装:
`0.0` を返す。

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-snip previous) → (or/c (is-a?/c snip%) #f) |
+----------------------------------------------------+
```

このスニップを所有するエディタ内の前のスニップを返す。これが最初のスニップなら `#f`。

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-snip release-from-owner) → boolean? |
+---------------------------------------------+
```

仕様:
スニップに所有者からの解放を試みるよう求める。スニップが所有されていないか、解放が成功すれば `#t` が返る。そうでなければ `#f` が返り、スニップは所有されたまま残る。あわせて `is-owned?` も参照。

このメソッドは、スニップをあるエディタから別のエディタへ移すときに使う。このメソッドは、スニップの所有エディタに、他の誰かが本当にスニップの制御を欲しがっていることを通知する。エディタから削除されたスニップの「後始末」のためにこのメソッドを使う必要はない。

既定の実装:
スニップの所有アドミニストレータに低レベルの解放を要求する。

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-snip resize w h) → boolean? |
| w: (and/c real? (not/c negative?)) |
| h: (and/c real? (not/c negative?)) |
+-------------------------------------+
```

仕様:
スニップをリサイズする。スニップは `#f` を返してリサイズを拒否できる。そうでなければ、スニップはリサイズし（アドミニストレータの `resized` メソッドを呼ばなければならない）、`#t` を返す。

あわせて `pasteboard%` の `on-interactive-resize` も参照。

既定の実装:
`#f` を返す。

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-snip set-admin admin) → void?   |
| admin: (or/c (is-a?/c snip-admin%) #f) |
+-----------------------------------------+
```

スニップのアドミニストレータを設定する。このメソッドを呼ぶべきなのはアドミニストレータのみである。

既定のメソッドは、スニップの内部状態を更新してアドミニストレータを記録する。スニップがすでにアドミニストレータに所有されており、そのアドミニストレータが遷移を認めていない場合、この状態は変更されない。`text%` または `pasteboard%` のインスタンスによるこのメソッドへの敏感な呼び出しのあいだにスニップのアドミニストレータ状態が期待どおりに変更されなかった場合、内部状態は強制的に変更されるか（新しいアドミニストレータが `#f` の場合）、代理スニップが作成されることがある（スニップが新しいアドミニストレータを受け取ると期待されていた場合）。

このメソッドが呼ばれるとき、スニップの（新しい）エディタは通常、読み取りについて内部ロックされている（Internal Editor Locks も参照）。

```
+-----------------------------------+
| [method]                          |
|                                   |
| (send a-snip set-count c) → void? |
| c: (integer-in 1 100000)         |
+-----------------------------------+
```

仕様:
スニップのカウント（すなわちスニップ内の項目数）を `(max 1 c)` に設定する。スニップの書記素カウントは文字カウントと等しく設定される。

スニップのカウントは、（一貫性を保つための極端な場合に）このメソッドや `set-char-and-grapheme-count` を呼ばずにシステムによって変更されることがある。

既定の実装:
スニップのカウントを設定し、スニップのサイズが変わったことをスニップのアドミニストレータに通知する。

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send a-snip set-char-and-grapheme-count |
| char-c: exact-nonnegative-integer?      |
| grapheme-c: exact-nonnegative-integer?  |
+------------------------------------------+
```

仕様:
スニップのカウントを `(max 1 char-c)` に、書記素カウントを `(max 1 grapheme-c)` に設定する。

スニップのカウントは、（一貫性を保つための極端な場合に）このメソッドや `set-count` を呼ばずにシステムによって変更されることがある。

既定の実装: スニップのカウントを設定し、スニップのサイズが変わったことをスニップのアドミニストレータに通知する。

パッケージ `snip-lib` のバージョン 1.4 で追加。

```
+---------------------------------------+
| [method]                              |
|                                       |
| (send a-snip set-flags flags) → void? |
| flags: (listof symbol?)              |
+---------------------------------------+
```

仕様:
スニップのフラグを設定する。`get-flags` を参照。

既定の実装:
スニップのフラグを設定し、フラグが変わったことをスニップのエディタに通知する。

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-snip set-snipclass class) → void? |
| class: (is-a?/c snip-class%)             |
+-------------------------------------------+
```

ファイル保存およびカット＆ペーストに使うスニップのクラスを設定する。

このメソッドはスニップクラスを内部に格納する。他のエディタオブジェクトは、`get-snipclass` メソッドを経由せずにスニップクラスへ直接アクセスすることがある。

```
+---------------------------------------+
| [method]                              |
|                                       |
| (send a-snip set-style style) → void? |
| style: (is-a?/c style<%>)            |
+---------------------------------------+
```

どのエディタにも所有されていなければ、スニップのスタイルを設定する。あわせて `get-style` と `is-owned?` も参照。

スニップのスタイルは、このメソッドを呼ばずにシステムによって変更されることがある。

```
+--------------------------------------+
| [method]                             |
|                                      |
| (send a-snip set-unmodified) → void? |
+--------------------------------------+
```

仕様:
スニップのアドミニストレータから呼ばれ、スニップの変更が保存されたことを通知する。次にユーザがスニップの内部状態を変更したとき、状態変更を報告するために `modified` を呼ぶべきである（ただし、このメソッドが呼ばれたあとの最初の変更、またはスニップが新しいアドミニストレータを得たあとの最初の変更に限る）。

既定の実装:
何もしない。

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send a-snip size-cache-invalid) → void? |
+------------------------------------------+
```

仕様:
スニップのスタイルまたは位置が変わったため、次に尋ねられたときに表示引数（幅、高さなど）を再計算する必要があるかもしれないことをスニップに通知するために呼ばれる。

このメソッドが呼ばれるとき、スニップの（新しい）エディタは通常、リフローについて内部ロックされている（Internal Editor Locks も参照）。

既定の実装:
何もしない。

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send a-snip split position first second) → void? |
| position: exact-nonnegative-integer?             |
| first: (box/c (is-a?/c snip%))                   |
| second: (box/c (is-a?/c snip%))                  |
+---------------------------------------------------+
```

仕様: スニップを二つのスニップに分割する。スニップが複数の項目を持ち、二つの項目のあいだに何かが挿入されたときに呼ばれる。

引数は相対位置整数と二つのボックスである。位置整数は、新しい最初のスニップに与える項目数を指定し、残りは新しい二番目のスニップに行く。二つのボックスは二つの新しいスニップで埋めなければならない。（古いスニップはもう使われないので、新しいスニップとして再利用できる。）

返されたスニップが期待されるカウントを持たなければ、そのカウントは強制的に修正される。返されたスニップのいずれかがすでに別のアドミニストレータに所有されていれば、代理スニップが作成される。

このメソッドが呼ばれるとき、スニップのエディタは通常、読み取りについて内部ロックされている（Internal Editor Locks も参照）。

既定の実装:
`position` 個の要素を持つ新しい `snip%` インスタンスを作成し、`a-snip` を変更してそのカウントを `position` だけ減らす。次のスニップは `first` に、`a-snip` は `second` に格納される。

```
+----------------------------------+
| [method]                         |
|                                  |
| (send a-snip write f) → void?    |
| f: (is-a?/c editor-stream-out%) |
+----------------------------------+
```

与えられたストリームへスニップを書き出す。（スニップの読み取りはスニップクラスが扱う。）スニップに関するスタイル情報（すなわち `get-style` の内容）は自動的に保存・復元される。

---

## string-snip%

```
+----------------------------+
| classstring-snip%: class? |
+----------------------------+
| superclass: snip%          |
+----------------------------+
```

`string-snip%` のインスタンスは、テキストエディタにテキストが挿入されるときに自動的に作成される。あわせて `text%` の `on-new-string-snip` も参照。

```
+-----------------------------------------------------------------+
| [constructor]                                                   |
|                                                                 |
| (make-object string-snip% [allocsize]) → (is-a?/c string-snip%) |
| allocsize: exact-nonnegative-integer? = 0                      |
| (make-object string-snip% s) → (is-a?/c string-snip%)           |
| s: string?                                                     |
+-----------------------------------------------------------------+
```

初期内容が（与えられれば）`s`、そうでなければ空の文字列スニップを作成する。後者の場合、任意の `allocsize` 引数は、スニップがテキスト用に最初に割り当てるべき記憶領域のヒントである。

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-string-snip insert s len [pos]) → void? |
| s: string?                                     |
| len: exact-nonnegative-integer?                |
| pos: exact-nonnegative-integer? = 0            |
+-------------------------------------------------+
```

スニップ内の相対位置 `pos` に、`s`（長さ `len`）を挿入する。

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-string-snip read len f) → void? |
| len: exact-nonnegative-integer?        |
| f: (is-a?/c editor-stream-in%)         |
+-----------------------------------------+
```

与えられたストリームからスニップのデータを読み取る。

`len` 引数は読み取るテキストの最大長を指定する。（テキストスニップがファイルに書き出されるとき、最初のフィールドはスニップに含まれるテキストの長さである。）このメソッドは通常、テキストスニップクラスの `read` メソッドから呼び出される。
