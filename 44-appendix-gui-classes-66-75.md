# 付録：GUI クラス参照（66–75）

**原本範囲:** `original_markdown_66` … `original_markdown_75`  
**対象:** `menu%` … `radio-box%`  
**原本ディレクトリ:** `extracted/appendix/gui/`

コード、メソッド名、契約、シグネチャは原文のままです。クラス名も英語のままです。

---

## menu%

```
+---------------------+------------------------+
| classmenu%: class? |                        |
+---------------------+------------------------+
| superclass: object% |                        |
| extends:            | menu-item-container<%> |
|                     | labelled-menu-item<%>  |
+---------------------+------------------------+
```

`menu%` オブジェクトは menu% または popup-menu% 内のサブメニュー、あるいは menu-bar% 内のトップレベルメニューです。

```
+---------------------------------------------------------------------------+
| [constructor]                                                             |
|                                                                           |
| (new menu%                                                                |
| → (is-a?/c menu%)                                                         |
| label: label-string?                                                     |
| parent: (or/c (is-a?/c menu%) (is-a?/c popup-menu%) (is-a?/c menu-bar%)) |
| (or/c (is-a?/c menu%) (is-a?/c popup-menu%)                               |
| (is-a?/c menu-bar%))                                                      |
| help-string: (or/c label-string? #f) = #f                                |
| demand-callback: ((is-a?/c menu%). ->. any) = (lambda (m) (void))      |
|                                                                           |
| ```racket                                                                 |
| (or/c (is-a?/c menu%) (is-a?/c popup-menu%)                               |
|       (is-a?/c menu-bar%))                                                |
| ```                                                                       |
+---------------------------------------------------------------------------+
```

与えられたラベルで新しいメニューを作成します。

label に & またはタブ文字が含まれる場合、メニュー項目ラベルやボタンと同様に特別扱いされます。set-label と button% を参照してください。

help-string が #f でなければメニューにヘルプ文字列があります。詳細は get-help-string を参照してください。

demand-callback 手続きは、既定の on-demand メソッドからオブジェクト自身を引数に呼ばれます。

---

## message%

> [image: message.png]

```
+------------------------+------------+
| classmessage%: class? |            |
+------------------------+------------+
| superclass: object%    |            |
| extends:               | control<%> |
+------------------------+------------+
```

メッセージコントロールは静的な 1 行のテキストまたは静的ビットマップです。テキストまたはビットマップはメッセージのラベルに対応します（set-label を参照）。

```
+-----------------------------------------------------------------------------+
| [constructor]                                                               |
|                                                                             |
| (new message%                                                               |
| → (is-a?/c message%)                                                        |
| label: (or/c label-string? (is-a?/c bitmap%) (or/c 'app 'caution 'stop))   |
| (or/c label-string? (is-a?/c bitmap%)                                       |
| (or/c 'app 'caution 'stop))                                                 |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c |
| pane%))                                                                     |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                    |
| (is-a?/c panel%) (is-a?/c pane%))                                           |
| style: (listof (or/c 'deleted)) = null                                     |
| font: (is-a?/c font%) = normal-control-font                                |
| color: (or/c #f string? (is-a?/c color%)) = #f                             |
| enabled: any/c = #t                                                        |
| vert-margin: spacing-integer? = 2                                          |
| horiz-margin: spacing-integer? = 2                                         |
| min-width: (or/c dimension-integer? #f) = #f                               |
| min-height: (or/c dimension-integer? #f) = #f                              |
| stretchable-width: any/c = #f                                              |
| stretchable-height: any/c = #f                                             |
| auto-resize: any/c = #f                                                    |
|                                                                             |
| ```racket                                                                   |
| (or/c label-string? (is-a?/c bitmap%)                                       |
|       (or/c 'app 'caution 'stop))                                           |
| ```                                                                         |
|                                                                             |
| ```racket                                                                   |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                    |
|       (is-a?/c panel%) (is-a?/c pane%))                                     |
| ```                                                                         |
+-----------------------------------------------------------------------------+
```

label を最初に示す文字列またはビットマップメッセージを作成します。label がビットマップで同じサイズのマスクがある場合、ラベルにマスクが使われます。ラベル使用中のビットマップ変更の表示効果は未規定です。'app、'caution、'stop シンボルはアイコンを示します。

label に & が含まれると特別に解析されます。Windows と X では、& の次の文字が表示コントロール上で下線付きになりキーボードニーモニックを示します（Mac OS ではニーモニック下線は表示されません）。メッセージにとってニーモニックは（top-level-window<%> の on-traverse-char に関する限り）意味を持ちませんが、他コントロールとの一貫性のためサポートされています。

style に 'deleted があれば、メッセージは非表示で作成され親のジオメトリに影響しません。後から親の add-child で有効化できます。

font はコントロールのフォントを決めます。enabled については window<%>、horiz-margin と vert-margin については subarea<%>、min-width、min-height、stretchable-width、stretchable-height については area<%> を参照。

color 引数はテキストラベルの色を決めます。シンボルとビットマップラベルには効果がありません。#f ならシステムの既定テキスト色が使われます。文字列なら the-color-database で色が検索されます。

auto-resize が #f でなければ、自動リサイズが初期状態で有効（auto-resize を参照）で、message% オブジェクトのグラフィカル最小サイズは可能な限り小さくなります。

Changed in version 1.58 of package `gui-lib`: Added the color argument.

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send a-message auto-resize) → boolean?  |
| (send a-message auto-resize on?) → void? |
| on?: any/c                              |
+------------------------------------------+
```

set-label でラベルが変わったときに message% の min-width と min-height が自動設定されるかどうかを報告または設定します。

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-message set-label label) → void?       |
| label: (or/c label-string? (is-a?/c bitmap%)) |
+------------------------------------------------+
```

set-label in window<%> をオーバーライドします。

label が文字列のときは window<%> の set-label と同じです。

そうでなければ、ビットマップメッセージのビットマップラベルを設定します。label がビットマップで、マスク（bitmap% の get-loaded-mask を参照）がビットマップと同じサイズなら、ラベルにマスクが使われます。ラベルとして使われている間にビットマップを変更したときの表示効果は未規定です。

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-message set-color color) → void?      |
| color: (or/c #f (is-a?/c color%))            |
| (send a-message set-color color-name) → void? |
| color-name: string?                          |
+-----------------------------------------------+
```

ラベルのテキスト色を設定します。color が #f ならプラットフォーム既定にします。ラベルがシンボルまたはビットマップのときは効果がありません。

Added in version 1.58 of package `gui-lib`.
Changed in version 1.71: Added support for setting the color to the system default.

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send a-message get-color) → (or/c #f (is-a?/c color%)) |
+---------------------------------------------------------+
```

ユーザー指定のラベル色を返します。システム既定なら #f です。

Added in version 1.58 of package `gui-lib`.

---

## mouse-event%

```
+----------------------------+
| classmouse-event%: class? |
+----------------------------+
| superclass: event%         |
+----------------------------+
```

`mouse-event%` オブジェクトはマウスイベントをカプセル化します。マウスイベントは主に window<%> の on-subwindow-event と canvas<%> の on-event によって処理されます。

Mouse and Keyboard Events も参照してください。

```
+------------------------------------------------------------------------------+
| [constructor]                                                                |
|                                                                              |
| (new mouse-event%                                                            |
| → (is-a?/c mouse-event%)                                                     |
| event-type: (or/c 'enter 'leave 'left-down 'left-up 'middle-down 'middle-up |
| 'right-down 'right-up 'motion)                                               |
| (or/c 'enter 'leave 'left-down 'left-up                                      |
| 'middle-down 'middle-up                                                      |
| 'right-down 'right-up 'motion)                                               |
| left-down: any/c = #f                                                       |
| middle-down: any/c = #f                                                     |
| right-down: any/c = #f                                                      |
| x: exact-integer? = 0                                                       |
| y: exact-integer? = 0                                                       |
| shift-down: any/c = #f                                                      |
| control-down: any/c = #f                                                    |
| meta-down: any/c = #f                                                       |
| alt-down: any/c = #f                                                        |
| time-stamp: exact-integer? = 0                                              |
| caps-down: any/c = #f                                                       |
| mod3-down: any/c = #f                                                       |
| mod4-down: any/c = #f                                                       |
| mod5-down: any/c = #f                                                       |
|                                                                              |
| ```racket                                                                    |
| (or/c 'enter 'leave 'left-down 'left-up                                      |
|       'middle-down 'middle-up                                                |
|       'right-down 'right-up 'motion)                                         |
| ```                                                                          |
+------------------------------------------------------------------------------+
```

特定の型のマウスイベントを作成します。イベント型は次のとおりです。

- 'enter — マウスポインタがウィンドウに入った
- 'leave — マウスポインタがウィンドウを出た
- 'left-down — 左ボタン押下
- 'left-up — 左ボタン解放
- 'middle-down — 中ボタン押下
- 'middle-up — 中ボタン解放
- 'right-down — 右ボタン押下（Mac OS では Control クリック）
- 'right-up — 右ボタン解放（Mac OS では Control クリック）
- 'motion — マウス移動

the corresponding get- and set- methods for information about left-down, middle-down, right-down, x, y, shift-down, control-down, meta-down, alt-down, time-stamp, caps-down, mod3-down, mod4-down, and mod5-down を参照してください。

Changed in version 1.1 of package `gui-lib`: Added mod3-down, mod4-down, and mod5-down.

```
+----------------------------------------------------------+
| [method]                                                 |
|                                                          |
| (send a-mouse-event button-changed? [button]) → boolean? |
| button: (or/c 'left 'middle 'right 'any) = 'any         |
+----------------------------------------------------------+
```

マウスボタンの押下または解放イベント（型 'left-down、'left-up、'middle-down、'middle-up、'right-down、'right-up）なら #t、そうでなければ #f を返します。button-up? と button-down? も参照してください。

button が 'any でなければ、特定ボタンの押下または解放イベントのときだけ #t を返します。

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-mouse-event button-down? [button]) → boolean? |
| button: (or/c 'left 'middle 'right 'any) = 'any      |
+-------------------------------------------------------+
```

ボタン押下イベント（型 'left-down、'middle-down、'right-down）なら #t、そうでなければ #f を返します。

button が 'any でなければ、特定ボタンの押下イベントのときだけ #t を返します。

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-mouse-event button-up? [button]) → boolean? |
| button: (or/c 'left 'middle 'right 'any) = 'any    |
+-----------------------------------------------------+
```

ボタン解放イベント（型 'left-up、'middle-up、'right-up）なら #t、そうでなければ #f を返します（「マウスとキーボードイベント」で述べるとおり、解放イベントが落ちることがあります）。

button が 'any でなければ、特定ボタンの解放イベントのときだけ #t を返します。

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-mouse-event dragging?) → boolean? |
+-------------------------------------------+
```

ドラッグイベント（ボタンが押された状態での型 'motion。get-left-down 等で報告）なら #t、そうでなければ #f を返します。

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-mouse-event entering?) → boolean? |
+-------------------------------------------+
```

ウィンドウへのマウス進入イベント（型 'enter）なら #t、そうでなければ #f を返します。

マウスボタンが上がっているとき、enter/leave イベントはウィンドウがマウスイベントの受信を開始／停止することを通知します。ボタンが下がっているときは、マウスダウンを受け取ったウィンドウがボタン解放まですべてのマウスイベントを受け取り、他ウィンドウへ enter/leave は送られず、他ウィンドウでボタンが解放された場合に限り leave イベントが遅延して送られることがあります。

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-mouse-event get-alt-down) → boolean? |
+----------------------------------------------+
```

イベント時に Option（Mac OS）キーが押されていれば #t を返します。Windows で Alt が押された場合は Meta 押下として報告されます（get-meta-down を参照）。

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-mouse-event get-caps-down) → boolean? |
+-----------------------------------------------+
```

イベント時に Caps Lock がオンなら #t を返します。

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-mouse-event get-control-down) → boolean? |
+--------------------------------------------------+
```

イベント時に Control キーが押されていれば #t を返します。

Mac OS では、Control キー押下とマウスボタンクリックが組み合わさると、イベントは右ボタンクリックとして報告され、get-control-down は #f を報告します。

```
+-------------------------------------------------------------------------------+
| [method]                                                                      |
|                                                                               |
| (send a-mouse-event get-event-type)                                           |
| → (or/c 'enter 'leave 'left-down 'left-up 'middle-down 'middle-up 'right-down |
| 'right-up 'motion)                                                            |
| (or/c 'enter 'leave 'left-down 'left-up                                       |
| 'middle-down 'middle-up                                                       |
| 'right-down 'right-up 'motion)                                                |
|                                                                               |
| ```racket                                                                     |
| (or/c 'enter 'leave 'left-down 'left-up                                       |
|       'middle-down 'middle-up                                                 |
|       'right-down 'right-up 'motion)                                          |
| ```                                                                           |
+-------------------------------------------------------------------------------+
```

イベントの型を返します。各型については mouse-event% を参照。set-event-type も参照してください。

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-mouse-event get-left-down) → boolean? |
+-----------------------------------------------+
```

イベント中に左マウスボタンが下がっていた（ただし押下イベントではない）なら #t を返します。

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-mouse-event get-meta-down) → boolean? |
+-----------------------------------------------+
```

イベント時に Meta（Unix）、Alt（Windows）、または Command（Mac OS）キーが押されていれば #t を返します。

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-mouse-event get-middle-down) → boolean? |
+-------------------------------------------------+
```

イベント時に中マウスボタンが下がっていた（ただし押下ではない）なら #t を返します。Mac OS では中ボタンクリックは不可能です。

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-mouse-event get-mod3-down) → boolean? |
+-----------------------------------------------+
```

イベント時に Mod3（Unix）キーが押されていれば #t を返します。

Added in version 1.1 of package `gui-lib`.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-mouse-event get-mod4-down) → boolean? |
+-----------------------------------------------+
```

イベント時に Mod4（Unix）キーが押されていれば #t を返します。

Added in version 1.1 of package `gui-lib`.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-mouse-event get-mod5-down) → boolean? |
+-----------------------------------------------+
```

イベント時に Mod5（Unix）キーが押されていれば #t を返します。

Added in version 1.1 of package `gui-lib`.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-mouse-event get-right-down) → boolean? |
+------------------------------------------------+
```

イベント時に右マウスボタンが下がっていた（ただし押下ではない）なら #t を返します。Mac OS では Control クリックの組み合わせが右ボタンクリックとして扱われます。

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-mouse-event get-shift-down) → boolean? |
+------------------------------------------------+
```

イベント時に Shift キーが押されていれば #t を返します。

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-mouse-event get-x) → exact-integer? |
+---------------------------------------------+
```

イベント時のマウスの x 位置を、対象ウィンドウの（クライアント領域）座標系で返します。

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-mouse-event get-y) → exact-integer? |
+---------------------------------------------+
```

イベント時のマウスの y 位置を、対象ウィンドウの（クライアント領域）座標系で返します。

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send a-mouse-event leaving?) → boolean? |
+------------------------------------------+
```

ウィンドウからのマウス退出イベント（型 'leave）なら #t、そうでなければ #f を返します。

ボタンクリック中の enter/leave イベントについては entering? を参照してください。

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-mouse-event moving?) → boolean? |
+-----------------------------------------+
```

移動イベント（型 'motion）なら #t、そうでなければ #f を返します。

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-mouse-event set-alt-down down?) → void? |
| down?: any/c                                   |
+-------------------------------------------------+
```

イベント時に Option（Mac OS）キーが押されていたかどうかを設定します。Windows で Alt が押された場合は Meta 押下として報告されます（set-meta-down を参照）。

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-mouse-event set-caps-down down?) → void? |
| down?: any/c                                    |
+--------------------------------------------------+
```

イベント時に Caps Lock がオンだったかどうかを設定します。

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-mouse-event set-control-down down?) → void? |
| down?: any/c                                       |
+-----------------------------------------------------+
```

イベント時に Control キーが押されていたかどうかを設定します。

Mac OS では、Control キー押下とマウスボタンクリックが組み合わさると、イベントは右ボタンクリックとして報告され、get-control-down は #f を報告します。

```
+------------------------------------------------------------------------------+
| [method]                                                                     |
|                                                                              |
| (send a-mouse-event set-event-type event-type) → void?                       |
| event-type: (or/c 'enter 'leave 'left-down 'left-up 'middle-down 'middle-up |
| 'right-down 'right-up 'motion)                                               |
| (or/c 'enter 'leave 'left-down 'left-up                                      |
| 'middle-down 'middle-up                                                      |
| 'right-down 'right-up 'motion)                                               |
|                                                                              |
| ```racket                                                                    |
| (or/c 'enter 'leave 'left-down 'left-up                                      |
|       'middle-down 'middle-up                                                |
|       'right-down 'right-up 'motion)                                         |
| ```                                                                          |
+------------------------------------------------------------------------------+
```

イベントの型を設定します。各型については mouse-event% を参照。get-event-type も参照してください。

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-mouse-event set-left-down down?) → void? |
| down?: any/c                                    |
+--------------------------------------------------+
```

イベント中に左マウスボタンが下がっていた（ただし押下ではない）かどうかを設定します。

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-mouse-event set-meta-down down?) → void? |
| down?: any/c                                    |
+--------------------------------------------------+
```

イベント時に Meta（Unix）、Alt（Windows）、または Command（Mac OS）キーが押されていたかどうかを設定します。

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-mouse-event set-middle-down down?) → void? |
| down?: any/c                                      |
+----------------------------------------------------+
```

イベント時に中マウスボタンが下がっていた（ただし押下ではない）かどうかを設定します。Mac OS では中ボタンクリックは不可能です。

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-mouse-event set-mod3-down down?) → void? |
| down?: any/c                                    |
+--------------------------------------------------+
```

イベント時に Mod3（Unix）キーが押されていたかどうかを設定します。

Added in version 1.1 of package `gui-lib`.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-mouse-event set-mod4-down down?) → void? |
| down?: any/c                                    |
+--------------------------------------------------+
```

イベント時に Mod4（Unix）キーが押されていたかどうかを設定します。

Added in version 1.1 of package `gui-lib`.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-mouse-event set-mod5-down down?) → void? |
| down?: any/c                                    |
+--------------------------------------------------+
```

イベント時に Mod5（Unix）キーが押されていたかどうかを設定します。

Added in version 1.1 of package `gui-lib`.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send a-mouse-event set-right-down down?) → void? |
| down?: any/c                                     |
+---------------------------------------------------+
```

イベント時に右マウスボタンが下がっていた（ただし押下ではない）かどうかを設定します。Mac OS ではユーザーの Control クリック組み合わせが右ボタンクリックとして扱われます。

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send a-mouse-event set-shift-down down?) → void? |
| down?: any/c                                     |
+---------------------------------------------------+
```

イベント時に Shift キーが押されていたかどうかを設定します。

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-mouse-event set-x pos) → void? |
| pos: exact-integer?                   |
+----------------------------------------+
```

イベント時のマウスの x 位置を、対象ウィンドウの（クライアント領域）座標系で設定します。

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-mouse-event set-y pos) → void? |
| pos: exact-integer?                   |
+----------------------------------------+
```

イベント時のマウスの y 位置を、対象ウィンドウの（クライアント領域）座標系で設定します。

---

## mult-color<%>

```
+-------------------------------------+
| interfacemult-color<%>: interface? |
+-------------------------------------+
+-------------------------------------+
```

`mult-color<%>` オブジェクトは color% オブジェクトの RGB 値をスケールするために使います。mult-color<%> オブジェクトは style-delta% オブジェクト内にのみ存在します。

get-foreground-mult and get-background-mult も参照してください。

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-mult-color get r g b [a]) → void? |
| r: (box/c real?)                         |
| g: (box/c real?)                         |
| b: (box/c real?)                         |
| a: (or/c (box/c real?) #f) = #f          |
+-------------------------------------------+
```

すべてのスケール値を取得します。

r ボックスには色の赤成分のスケール値が入ります。g には緑、b には青、a にはアルファ成分のスケール値が入ります。

Changed in version 1.63 of package `snip-lib`: Added the a optional argument.

```
+-----------------------------------+
| [method]                          |
|                                   |
| (send a-mult-color get-a) → real? |
+-----------------------------------+
```

色のアルファ成分の乗法スケール値を取得します。

Added in version 1.63 of package `snip-lib`.

```
+-----------------------------------+
| [method]                          |
|                                   |
| (send a-mult-color get-b) → real? |
+-----------------------------------+
```

色の青成分の乗法スケール値を取得します。

```
+-----------------------------------+
| [method]                          |
|                                   |
| (send a-mult-color get-g) → real? |
+-----------------------------------+
```

色の緑成分の乗法スケール値を取得します。

```
+-----------------------------------+
| [method]                          |
|                                   |
| (send a-mult-color get-r) → real? |
+-----------------------------------+
```

色の赤成分の乗法スケール値を取得します。

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-mult-color set r g b [a]) → void? |
| r: real?                                 |
| g: real?                                 |
| b: real?                                 |
| a: real? = 1.0                           |
+-------------------------------------------+
```

すべてのスケール値を設定します。

Changed in version 1.63 of package `snip-lib`: Added the a optional argument.

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-mult-color set-a v) → void? |
| v: real?                           |
+-------------------------------------+
```

色のアルファ成分の乗法スケール値を設定します。

Added in version 1.63 of package `snip-lib`.

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-mult-color set-b v) → void? |
| v: real?                           |
+-------------------------------------+
```

色の青成分の乗法スケール値を設定します。

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-mult-color set-g v) → void? |
| v: real?                           |
+-------------------------------------+
```

色の緑成分の乗法スケール値を設定します。

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-mult-color set-r v) → void? |
| v: real?                           |
+-------------------------------------+
```

色の赤成分の加法値を設定します。

---

## pane%

```
+---------------------+-------------------+
| classpane%: class? |                   |
+---------------------+-------------------+
| superclass: object% |                   |
| extends:            | area-container<%> |
|                     | subarea<%>        |
+---------------------+-------------------+
```

ペインはコンテナであると同時に被包含領域でもあります。ジオメトリ管理デバイスとしてのみ機能します。pane% は panel% オブジェクトのように非表示や無効にはできません。

`pane%` オブジェクトの子管理配置戦略は退化した形です。各子をパネルの唯一の子であるかのように配置します。複数の子に有用なジオメトリ管理は horizontal-pane% と vertical-pane% が提供します。

grow-box-spacer-pane% も参照してください。

Changed in version 1.3 of package `gui-lib`: Changed the placement strategy to
stretch and align children, instead of
placing all children at the top-left
corner.

```
+--------------------------------------------------------------------------------+
| [constructor]                                                                  |
|                                                                                |
| (new pane%                                                                     |
| → (is-a?/c pane%)                                                              |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c    |
| pane%))                                                                        |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                       |
| (is-a?/c panel%) (is-a?/c pane%))                                              |
| vert-margin: spacing-integer? = 0                                             |
| horiz-margin: spacing-integer? = 0                                            |
| border: spacing-integer? = 0                                                  |
| spacing: spacing-integer? = 0                                                 |
| alignment: (list/c (or/c 'left 'center 'right) (or/c 'top 'center 'bottom)) = |
| '(center top)                                                                  |
| (list/c (or/c 'left 'center 'right)                                            |
| (or/c 'top 'center 'bottom))                                                   |
| min-width: (or/c dimension-integer? #f) = #f                                  |
| min-height: (or/c dimension-integer? #f) = #f                                 |
| stretchable-width: any/c = #t                                                 |
| stretchable-height: any/c = #t                                                |
|                                                                                |
| ```racket                                                                      |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                       |
|       (is-a?/c panel%) (is-a?/c pane%))                                        |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (list/c (or/c 'left 'center 'right)                                            |
|         (or/c 'top 'center 'bottom))                                           |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

horiz-margin と vert-margin については subarea<%>、border、spacing、alignment については area-container<%>、min-width 等については area<%> を参照。

---

## panel%

> [image: panel.png]

```
+----------------------+--------------------------+
| classpanel%: class? |                          |
+----------------------+--------------------------+
| superclass: object%  |                          |
| extends:             | area-container-window<%> |
|                      | subwindow<%>             |
+----------------------+--------------------------+
```

パネルはコンテナであると同時に被包含ウィンドウでもあります。主にジオメトリ管理デバイスとして機能しますが、'border は境界付きコンテナを作ります。pane% と異なり panel% は非表示や無効にできます。

`panel%` オブジェクトの子管理配置戦略は退化した形です。各子をパネルの唯一の子であるかのように配置します。複数の子に有用なジオメトリ管理は horizontal-panel% と vertical-panel% が提供します。

Changed in version 1.3 of package `gui-lib`: Changed the placement strategy to
stretch and align children, instead of
placing all children at the top-left
corner.

```
+--------------------------------------------------------------------------------+
| [constructor]                                                                  |
|                                                                                |
| (new panel%                                                                    |
| → (is-a?/c panel%)                                                             |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c    |
| pane%))                                                                        |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                       |
| (is-a?/c panel%) (is-a?/c pane%))                                              |
| style: (listof (or/c 'border 'deleted 'hscroll 'auto-hscroll 'hide-hscroll    |
| 'vscroll 'auto-vscroll 'hide-vscroll)) = null                                  |
| (listof (or/c 'border 'deleted                                                 |
| 'hscroll 'auto-hscroll 'hide-hscroll                                           |
| 'vscroll 'auto-vscroll 'hide-vscroll))                                         |
| enabled: any/c = #t                                                           |
| vert-margin: spacing-integer? = 0                                             |
| horiz-margin: spacing-integer? = 0                                            |
| border: spacing-integer? = 0                                                  |
| spacing: spacing-integer? = 0                                                 |
| alignment: (list/c (or/c 'left 'center 'right) (or/c 'top 'center 'bottom)) = |
| '(center center)                                                               |
| (list/c (or/c 'left 'center 'right)                                            |
| (or/c 'top 'center 'bottom))                                                   |
| min-width: (or/c dimension-integer? #f) = #f                                  |
| min-height: (or/c dimension-integer? #f) = #f                                 |
| stretchable-width: any/c = #t                                                 |
| stretchable-height: any/c = #t                                                |
|                                                                                |
| ```racket                                                                      |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                       |
|       (is-a?/c panel%) (is-a?/c pane%))                                        |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (listof (or/c 'border 'deleted                                                 |
|               'hscroll 'auto-hscroll 'hide-hscroll                             |
|               'vscroll 'auto-vscroll 'hide-vscroll))                           |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (list/c (or/c 'left 'center 'right)                                            |
|         (or/c 'top 'center 'bottom))                                           |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

'border スタイルが指定されると、ウィンドウは細い境界付きで作成されます（その場合パネルのクライアントサイズは総サイズより小さいことがあります）。style に 'deleted があれば非表示で作成され親のジオメトリに影響せず、後から親の add-child で有効化できます。

'hscroll または 'vscroll スタイルが指定されると、対応方向にスクロールバーが付き、その方向のパネル自身のサイズは子の subarea のサイズに制約されません。'auto-hscroll と 'auto-vscroll は 'hscroll と 'vscroll を含意し、内容がはみ出すときだけスクロールバーを表示します。'hide-hscroll と 'hide-vscroll は対応するスクロールバーを常に隠しますが、スクロール可能な領域は維持します。

enabled については window<%>、horiz-margin と vert-margin については subarea<%>、border、spacing、alignment については area-container<%>、min-width 等については area<%> を参照。

Changed in version 1.25 of package `gui-lib`: Added 'hide-vscroll and 'hide-hscroll.

---

## pasteboard%

```
+---------------------------+-----------+
| classpasteboard%: class? |           |
+---------------------------+-----------+
| superclass: object%       |           |
| extends:                  | editor<%> |
+---------------------------+-----------+
```

`pasteboard%` オブジェクトは任意位置のスニップを表示するエディタです。

```
+-------------------------------------------+
| [constructor]                             |
|                                           |
| (new pasteboard%) → (is-a?/c pasteboard%) |
+-------------------------------------------+
```

エディタは editor-canvas% オブジェクトまたは他の表示に取り付けられるまで表示されません。

新しいエディタ用に新しい keymap% オブジェクトが作成されます。get-keymap と set-keymap も参照してください。

新しいエディタ用に新しい style-list% オブジェクトが作成されます。get-style-list と set-style-list も参照してください。

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-pasteboard add-selected snip) → void?    |
| snip: (is-a?/c snip%)                           |
| (send a-pasteboard add-selected x y w h) → void? |
| x: real?                                        |
| y: real?                                        |
| w: (and/c real? (not/c negative?))              |
| h: (and/c real? (not/c negative?))              |
+--------------------------------------------------+
```

他のスニップの選択を外さずにスニップを選択します。座標が与えられると、与えられた矩形（エディタ座標）と交差するすべてのスニップを選択します。

ペーストボードの選択は、他のメソッド呼び出しに応じてシステムが変更することがあり、そのような変更はこのメソッドを経由しません。選択変化の監視には on-select を使ってください。

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-pasteboard after-delete snip) → void? |
| snip: (is-a?/c snip%)                        |
+-----------------------------------------------+
```

このメソッドは augment で精錬します。

仕様:
スニップがエディタから削除されたあと（表示の再描画後）に呼ばれます。after-delete がエディタを変更するときの余分な再描画を避けるには on-delete と begin-edit-sequence を使ってください。

can-delete? and on-edit-sequence も参照してください。

このメソッドが呼ばれるとき、内部ロックは設定されていません。

デフォルト実装: 何もしません。

```
+------------------------------------+
| [method]                           |
|                                    |
| (send a-pasteboard after-insert    |
| snip: (is-a?/c snip%)             |
| before: (or/c (is-a?/c snip%) #f) |
| x: real?                          |
| y: real?                          |
+------------------------------------+
```

このメソッドは augment で精錬します。

仕様:
スニップがエディタへ挿入されたあと（表示の再描画後）に呼ばれます。余分な再描画を避けるには on-insert と begin-edit-sequence を使ってください。

can-insert? and on-edit-sequence も参照してください。

このメソッドが呼ばれるとき、内部ロックは設定されていません。

デフォルト実装: 何もしません。

```
+----------------------------------------------------------+
| [method]                                                 |
|                                                          |
| (send a-pasteboard after-interactive-move event) → void? |
| event: (is-a?/c mouse-event%)                           |
+----------------------------------------------------------+
```

このメソッドは augment で精錬します。

仕様:
ユーザーが対話的なスニップドラッグ（選択中のもの；find-next-selected-snip を参照）を止めたあとに呼ばれます。移動を終了したマウスイベント（通常は button-up）が渡されます。

can-interactive-move? and on-interactive-move も参照してください。

デフォルト実装:
何もしません。

```
+-----------------------------------------------------------+
| [method]                                                  |
|                                                           |
| (send a-pasteboard after-interactive-resize snip) → void? |
| snip: (is-a?/c snip%)                                    |
+-----------------------------------------------------------+
```

このメソッドは augment で精錬します。

仕様:
ユーザーが対話的なスニップリサイズ（現在選択中；find-next-selected-snip を参照）を止めたあとに呼ばれます。snip はリサイズされたスニップです。

can-interactive-resize? and on-interactive-resize も参照してください。

デフォルト実装:
何もしません。

```
+----------------------------------+
| [method]                         |
|                                  |
| (send a-pasteboard after-move-to |
| snip: (is-a?/c snip%)           |
| x: real?                        |
| y: real?                        |
| dragging?: any/c                |
+----------------------------------+
```

このメソッドは augment で精錬します。

仕様:
与えられたスニップがエディタ内で移動したあと（表示の再描画後）に呼ばれます。余分な再描画を避けるには on-move-to と begin-edit-sequence を使ってください。

dragging? が #f でなければ、この移動はドラッグのための一時的な移動でした。

can-move-to? and on-edit-sequence も参照してください。

このメソッドが呼ばれるとき、内部ロックは設定されていません。

デフォルト実装:
何もしません。

```
+----------------------------------+
| [method]                         |
|                                  |
| (send a-pasteboard after-reorder |
| snip: (is-a?/c snip%)           |
| to-snip: (is-a?/c snip%)        |
| before?: any/c                  |
+----------------------------------+
```

このメソッドは augment で精錬します。

仕様:
ペーストボードの前後順でスニップが移動される前（表示の再描画後）に呼ばれます。余分な再描画を避けるには on-reorder と begin-edit-sequence を使ってください。

before? が #t なら snip は to-snip の前へ、そうでなければ後へ移動されました。

can-reorder? and on-edit-sequence も参照してください。

このメソッドが呼ばれるとき、内部ロックは設定されていません。

デフォルト実装:
何もしません。

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-pasteboard after-resize     |
| snip: (is-a?/c snip%)              |
| w: (and/c real? (not/c negative?)) |
| h: (and/c real? (not/c negative?)) |
| resized?: any/c                    |
+-------------------------------------+
```

このメソッドは augment で精錬します。

仕様:
与えられたスニップがリサイズされたあと（表示の再描画後）、または失敗したリサイズ試行のあとに呼ばれます。余分な再描画を避けるには on-resize と begin-edit-sequence を使ってください。

resized? が #f でなければ、スニップのリサイズは成功しました。

can-resize? and on-edit-sequence も参照してください。

このメソッドが呼ばれるとき、内部ロックは設定されていません。

デフォルト実装:
何もしません。

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send a-pasteboard after-select snip on?) → void? |
| snip: (is-a?/c snip%)                            |
| on?: any/c                                       |
+---------------------------------------------------+
```

このメソッドは augment で精錬します。

仕様:
ペーストボード内のスニップが選択または選択解除されたあとに呼ばれます。on-select も参照。選択スニップが削除されて間接的に選択解除されたあとには呼ばれません（after-delete も参照）。

on? が #t なら snip がちょうど選択され、そうでなければ選択が外されたところです。

can-select? and on-edit-sequence も参照してください。

このメソッドが呼ばれるとき、内部ロックは設定されていません。

デフォルト実装:
何もしません。

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-pasteboard can-delete? snip) → boolean? |
| snip: (is-a?/c snip%)                          |
+-------------------------------------------------+
```

このメソッドは augment で精錬します。

仕様:
スニップがエディタから削除される前に呼ばれます。戻り値が #f なら削除は中止されます。

on-delete and after-delete も参照してください。

このメソッドが呼ばれるとき、エディタは書き込み用に内部ロックされています（「内部エディタロック」も参照）。

デフォルト実装:
#t を返します。

```
+------------------------------------+
| [method]                           |
|                                    |
| (send a-pasteboard can-insert?     |
| snip: (is-a?/c snip%)             |
| before: (or/c (is-a?/c snip%) #f) |
| x: real?                          |
| y: real?                          |
+------------------------------------+
```

このメソッドは augment で精錬します。

仕様:
スニップがエディタへ挿入される前に呼ばれます。戻り値が #f なら挿入は中止されます。

on-insert and after-insert も参照してください。

このメソッドが呼ばれるとき、エディタは書き込み用に内部ロックされています（「内部エディタロック」も参照）。

デフォルト実装:
#t を返します。

```
+------------------------------------------------------------+
| [method]                                                   |
|                                                            |
| (send a-pasteboard can-interactive-move? event) → boolean? |
| event: (is-a?/c mouse-event%)                             |
+------------------------------------------------------------+
```

このメソッドは augment で精錬します。

仕様:
ユーザーが対話的なスニップドラッグ（選択中；find-next-selected-snip を参照）を開始したときに呼ばれます。選択中のスニップはすべて移動されます。#f を返すと対話的移動は不許可です。移動を開始したマウスイベント（通常は button-down）が渡されます。

on-interactive-move, after-interactive-move, and interactive-adjust-move も参照してください。

デフォルト実装:
#t を返します。

```
+-------------------------------------------------------------+
| [method]                                                    |
|                                                             |
| (send a-pasteboard can-interactive-resize? snip) → boolean? |
| snip: (is-a?/c snip%)                                      |
+-------------------------------------------------------------+
```

このメソッドは augment で精錬します。

仕様:
ユーザーが対話的なスニップリサイズ（選択中；find-next-selected-snip を参照）を開始したときに呼ばれます。#f を返すと対話的リサイズは不許可です。

snip 引数はリサイズされるスニップです。

after-interactive-resize, after-interactive-resize, and interactive-adjust-resize も参照してください。

デフォルト実装:
#t を返します。

```
+---------------------------------+
| [method]                        |
|                                 |
| (send a-pasteboard can-move-to? |
| snip: (is-a?/c snip%)          |
| x: real?                       |
| y: real?                       |
| dragging?: any/c               |
+---------------------------------+
```

このメソッドは augment で精錬します。

仕様:
スニップがエディタ内で移動される前に呼ばれます。戻り値が #f なら移動は中止されます。

dragging? が #f でなければ、この移動はドラッグのための一時的な移動です。

on-move-to and after-move-to も参照してください。

このメソッドが呼ばれるとき、エディタは書き込み用に内部ロックされています（「内部エディタロック」も参照）。

デフォルト実装:
#t を返します。

```
+---------------------------------+
| [method]                        |
|                                 |
| (send a-pasteboard can-reorder? |
| snip: (is-a?/c snip%)          |
| to-snip: (is-a?/c snip%)       |
| before?: any/c                 |
+---------------------------------+
```

このメソッドは augment で精錬します。

仕様:
ペーストボードの前後順でスニップが移動される前に呼ばれます。戻り値が #f なら並べ替えは中止されます。

before? が #t なら snip は to-snip の前へ、そうでなければ後へ移動されます。

on-reorder and after-reorder も参照してください。

このメソッドが呼ばれるとき、エディタは書き込み用に内部ロックされています（「内部エディタロック」も参照）。

デフォルト実装:
#t を返します。

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-pasteboard can-resize? snip w h) → boolean? |
| snip: (is-a?/c snip%)                              |
| w: (and/c real? (not/c negative?))                 |
| h: (and/c real? (not/c negative?))                 |
+-----------------------------------------------------+
```

このメソッドは augment で精錬します。

仕様:
スニップがエディタ内でリサイズされる前に呼ばれます。戻り値が #f ならリサイズは中止されます。

on-resize and after-resize も参照してください。

このメソッドが呼ばれるとき、エディタは書き込み用に内部ロックされています（「内部エディタロック」も参照）。

デフォルト実装:
#t を返します。

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-pasteboard can-select? snip on?) → boolean? |
| snip: (is-a?/c snip%)                              |
| on?: any/c                                         |
+-----------------------------------------------------+
```

このメソッドは augment で精錬します。

仕様:
ペーストボード内のスニップが選択または選択解除される前に呼ばれます。#f を返すと選択変更は不許可です。選択スニップが削除される（間接的に選択解除される）ときには呼ばれません（can-delete? も参照）。

on? が #t なら snip が選択され、そうでなければ選択が外されます。

on-select and after-select も参照してください。

このメソッドが呼ばれるとき、エディタは書き込み用に内部ロックされています（「内部エディタロック」も参照）。

デフォルト実装:
#t を返します。

```
+------------------------------------------------------------------+
| [method]                                                         |
|                                                                  |
| (send a-pasteboard change-style [style snip]) → void?            |
| style: (or/c (is-a?/c style-delta%) (is-a?/c style<%>) #f) = #f |
| snip: (or/c (is-a?/c snip%) #f) = #f                            |
+------------------------------------------------------------------+
```

snip のスタイルを特定のスタイルに変えるか、スタイルデルタを適用して変えます。snip が #f なら、現在選択されているすべてのスニップが変更されます。

多数のスニップをあるスタイルから別のスタイルへ変えるときは、style-delta% オブジェクトではなく style<%> オブジェクトを渡すことを検討してください。後者の方がはるかに効率的です。

スタイルが与えられた場合: エディタのスタイルリストに style が含まれていなければなりません。そうでなければスタイルは変更されません。

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-pasteboard copy-self-to dest) → void?       |
| dest: (or/c (is-a?/c text%) (is-a?/c pasteboard%)) |
+-----------------------------------------------------+
```

copy-self-to in editor<%> をオーバーライドします。

editor<%> の既定の copy-self-to の作業に加え、ドラッグ可能性、選択可視状態、背景ドラッグによる選択可能性の設定も dest へコピーされます。

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-pasteboard delete) → void?      |
| (send a-pasteboard delete snip) → void? |
| snip: (is-a?/c snip%)                  |
+-----------------------------------------+
```

snip が与えられればそれを削除し、与えられなければ現在選択中のスニップをエディタから削除します。

エディタの内容は、他のメソッド呼び出しに応じてシステムが変更することがあり、そのような変更はこのメソッドを経由しません。内容削除の監視には on-delete を使ってください。

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-pasteboard do-copy time extend?) → void? |
| time: exact-integer?                            |
| extend?: any/c                                  |
+--------------------------------------------------+
```

仕様:
エディタの現在の選択をクリップボードへコピーするために呼ばれます。サブクラスがオーバーライドできるように提供されています。直接呼ばず copy を呼んでください。

Cut and Paste Time Stamps for a discussion of the time argument. If time is outside the platform-specific range of times, an exn:fail:contract exception is raised を参照してください。

デフォルト実装:
Copies the current selection, extending the current clipboard contexts
if extend? is true.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-pasteboard do-paste time) → void? |
| time: exact-integer?                     |
+-------------------------------------------+
```

仕様:
クリップボードの現在内容をエディタへ貼り付けるために呼ばれます。サブクラスがオーバーライドできるように提供されています。直接呼ばず paste を呼んでください。

Cut and Paste Time Stamps for a discussion of the time argument. If time is outside the platform-specific range of times, an exn:fail:contract exception is raised を参照してください。

デフォルト実装:
Pastes.

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-pasteboard do-paste-x-selection time) → void? |
| time: exact-integer?                                 |
+-------------------------------------------------------+
```

仕様:
Unix では X11 セレクション、Windows と Mac OS ではクリップボードの現在内容をエディタへ貼り付けるために呼ばれます。サブクラスがオーバーライドできるように提供されています。直接呼ばず paste-x-selection を呼んでください。

Cut and Paste Time Stamps for a discussion of the time argument. If time is outside the platform-specific range of times, an exn:fail:contract exception is raised を参照してください。

デフォルト実装:
Pastes.

```
+-----------------------------------+
| [method]                          |
|                                   |
| (send a-pasteboard erase) → void? |
+-----------------------------------+
```

エディタからすべてのスニップを削除します。

delete も参照してください。

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send a-pasteboard find-next-selected-snip start) |
| → (or/c (is-a?/c snip%) #f)                       |
| start: (or/c (is-a?/c snip%) #f)                 |
+---------------------------------------------------+
```

start のあとから検索を始め、エディタ内の次の選択スニップを返します（ペーストボード内のスニップ順は「エディタの構造と用語」を参照）。start が #f なら先頭から検索します。これ以上選択スニップがない、または start がペーストボードにない場合は #f を返します。

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-pasteboard find-snip x y [after]) |
| → (or/c (is-a?/c snip%) #f)               |
| x: real?                                 |
| y: real?                                 |
| after: (or/c (is-a?/c snip%) #f) = #f    |
+-------------------------------------------+
```

the frontmost snip (after a given snip) that intersects a given
location. See Editor Structure and Terminology for information about snip order in pasteboards を探します。

x と y 引数はエディタ座標です。after が与えられなければ、x と y の最前面のスニップが使われます。スニップがなければ #f が返されます。

結果が有効なのはエディタが表示されているときだけです（「エディタの構造と用語」を参照）。エディタが表示されるのは get-admin がアドミニストレータを返す（#f でない）ときです。

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-pasteboard get-area-selectable) → boolean? |
+----------------------------------------------------+
```

ペーストボードの背景で選択ボックスをドラッグしてスニップを選択できるかどうかを返します。既定では可能です。

Added in version 1.12 of package `gui-lib`.

```
+--------------------------------+
| [method]                       |
|                                |
| (send a-pasteboard get-center) |
| real?                          |
+--------------------------------+
```

ペーストボード座標でのペーストボードの中心を返します。

第1結果は中心の x 座標、第2結果は y 座標です。

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-pasteboard get-dragable) → boolean? |
+---------------------------------------------+
```

on-default-event のイベント処理でスニップを対話的にドラッグできるかどうかを返します。既定では可能です。

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-pasteboard get-scroll-step) |
| → (and/c real? (not/c negative?))   |
+-------------------------------------+
```

各垂直スクロール位置に対するエディタ位置オフセットを取得します。set-scroll-step も参照してください。

```
+------------------------------------------------------+
| [method]                                             |
|                                                      |
| (send a-pasteboard get-selection-visible) → boolean? |
+------------------------------------------------------+
```

ペーストボード内の選択スニップの縁に選択ドットが描かれるかどうかを返します。既定では描かれます。

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-pasteboard insert snip) → void?            |
| snip: (is-a?/c snip%)                             |
| (send a-pasteboard insert snip before x y) → void? |
| snip: (is-a?/c snip%)                             |
| before: (or/c (is-a?/c snip%) #f)                 |
| x: real?                                          |
| y: real?                                          |
| (send a-pasteboard insert snip x y) → void?        |
| snip: (is-a?/c snip%)                             |
| x: real?                                          |
| y: real?                                          |
| (send a-pasteboard insert snip before) → void?     |
| snip: (is-a?/c snip%)                             |
| before: (or/c (is-a?/c snip%) #f)                 |
+----------------------------------------------------+
```

editor<%> の insert を拡張します。

snip を位置 (x, y) に、before の直前へ挿入します（スニップ順は「エディタの構造と用語」を参照）。before が無いまたは #f なら他のすべてのスニップの後ろに挿入されます。x と y が無ければペーストボードの中心に追加されます。

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-pasteboard interactive-adjust-mouse |
| x: (box/c real?)                           |
| y: (box/c real?)                           |
+---------------------------------------------+
```

仕様:
対話的なドラッグとリサイズ（現在選択中のスニップ；find-next-selected-snip を参照）の間に、現在のマウス位置（エディタ座標）を前処理するために呼ばれます。snip と実際の x、y が（ボックスで）渡され、結果の座標が実際のマウス位置の代わりに使われます。

interactive-adjust-resize も参照してください。

デフォルト実装:
x または y の負の値は 0 に置き換えられます。

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send a-pasteboard interactive-adjust-move |
| snip: (is-a?/c snip%)                     |
| x: (box/c real?)                          |
| y: (box/c real?)                          |
+--------------------------------------------+
```

仕様:
対話的な移動の間（選択中の各スニップについて）に、ユーザーが決めたスニップ位置を前処理するために呼ばれます。snip とマウスが決めた位置（エディタ座標）が（ボックスで）渡され、結果の位置が移動中のグラフィカルフィードバックに使われます。

実際のマウス座標は、位置下のスニップを決める前に interactive-adjust-mouse を通されます。

デフォルト実装:
何もしません。

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-pasteboard interactive-adjust-resize     |
| snip: (is-a?/c snip%)                           |
| width: (box/c (and/c real? (not/c negative?)))  |
| height: (box/c (and/c real? (not/c negative?))) |
+--------------------------------------------------+
```

仕様:
対話的なリサイズの間に、ユーザーが決めたスニップサイズを前処理するために呼ばれます。snip とマウスが決めた高さと幅が（ボックスで）渡され、結果が高さ／幅のフィードバックに使われます。

実際のマウス座標は、位置下のスニップを決める前に interactive-adjust-mouse を通されます。

デフォルト実装:
何もしません。

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-pasteboard is-selected? snip) → boolean? |
| snip: (is-a?/c snip%)                           |
+--------------------------------------------------+
```

指定スニップが現在選択されていれば #t、そうでなければ #f を返します。

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-pasteboard lower snip) → void? |
| snip: (is-a?/c snip%)                 |
+----------------------------------------+
```

the snip one level deeper (i.e., behind one more other snip) in
the pasteboard’s snip order. See Editor Structure and Terminology for information about snip order in pasteboards を移動します。

raise, set-before, and set-after も参照してください。

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-pasteboard move snip x y) → void? |
| snip: (is-a?/c snip%)                    |
| x: real?                                 |
| y: real?                                 |
| (send a-pasteboard move x y) → void?      |
| x: real?                                 |
| y: real?                                 |
+-------------------------------------------+
```

snip を右へ x ピクセル、下へ y ピクセル移動します。snip が無ければ選択中のすべてのスニップを移動します。

ペーストボード内のスニップ位置は、他のメソッド呼び出しに応じてシステムが変更することがあり、そのような変更はこのメソッドを経由しません。位置変化の監視には on-move-to を使ってください。

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-pasteboard move-to snip x y) → void? |
| snip: (is-a?/c snip%)                       |
| x: real?                                    |
| y: real?                                    |
+----------------------------------------------+
```

snip to a given location in the editor を移動します。

ペーストボード内のスニップ位置は、他のメソッド呼び出しに応じてシステムが変更することがあり、そのような変更はこのメソッドを経由しません。位置変化の監視には on-move-to を使ってください。

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-pasteboard no-selected) → void? |
+-----------------------------------------+
```

エディタ内の選択中スニップをすべて選択解除します。

ペーストボードの選択は、他のメソッド呼び出しに応じてシステムが変更することがあり、そのような変更はこのメソッドを経由しません。選択変化の監視には on-select を使ってください。

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send a-pasteboard on-default-char event) → void? |
| event: (is-a?/c key-event%)                      |
+---------------------------------------------------+
```

on-default-char in editor<%> をオーバーライドします。

Delete または Backspace キーに応じて引数なしの delete を呼び、矢印キーに応じて適切なオフセットで move を呼びます。

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-pasteboard on-default-event event) → void? |
| event: (is-a?/c mouse-event%)                     |
+----------------------------------------------------+
```

on-default-event in editor<%> をオーバーライドします。

スニップの選択、ドラッグ、リサイズを行います。

- スニップ上のクリックでそのスニップを選択。Shift クリックで現在の選択にスニップを追加。
- 選択スニップ上のドラッグで選択を移動。
- 選択スニップの隅または辺のドラッグでリサイズ（スニップが許せば）。
- 背景のクリックとドラッグで選択ボックスを描き、交差するスニップを選択。
- 背景のクリックで全選択を解除。

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send a-pasteboard on-delete snip) → void? |
| snip: (is-a?/c snip%)                     |
+--------------------------------------------+
```

このメソッドは augment で精錬します。

スニップがエディタから削除される前、can-delete? で削除が許可されたことを確認したあとに呼ばれます。

このメソッドが呼ばれるとき、エディタは書き込み用に内部ロックされています（「内部エディタロック」も参照）。

```
+------------------------------------+
| [method]                           |
|                                    |
| (send a-pasteboard on-double-click |
| snip: (is-a?/c snip%)             |
| event: (is-a?/c mouse-event%)     |
+------------------------------------+
```

仕様:
ユーザーがエディタ内のスニップをダブルクリックしたときに呼ばれます。クリックされた snip とイベントが渡されます。

デフォルト実装:
snip がイベントを受け付けるならキャレット所有者に指定され、エディタ内のすべてのスニップの選択が外れます。

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-pasteboard on-insert snip before x y) → void? |
| snip: (is-a?/c snip%)                                |
| before: (or/c (is-a?/c snip%) #f)                    |
| x: real?                                             |
| y: real?                                             |
+-------------------------------------------------------+
```

このメソッドは augment で精錬します。

スニップがエディタへ挿入される前、can-insert? で挿入が許可されたことを確認したあとに呼ばれます。

このメソッドが呼ばれるとき、エディタは書き込み用に内部ロックされています（「内部エディタロック」も参照）。

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-pasteboard on-interactive-move event) → void? |
| event: (is-a?/c mouse-event%)                        |
+-------------------------------------------------------+
```

このメソッドは augment で精錬します。

仕様:
ユーザーが対話的なスニップドラッグ（選択中；find-next-selected-snip を参照）を開始したとき、can-interactive-move? で許可を確認したあとに呼ばれます。移動完了後に after-interactive-move が必ず呼ばれます。選択中のスニップはすべて移動されます。開始マウスイベントが渡されます。

interactive-adjust-move も参照してください。

デフォルト実装:
何もしません。

```
+--------------------------------------------------------+
| [method]                                               |
|                                                        |
| (send a-pasteboard on-interactive-resize snip) → void? |
| snip: (is-a?/c snip%)                                 |
+--------------------------------------------------------+
```

このメソッドは augment で精錬します。

仕様:
ユーザーが対話的なスニップリサイズ（選択中；find-next-selected-snip を参照）を開始したとき、can-interactive-resize? で許可を確認したあとに呼ばれます。完了後に after-interactive-resize が必ず呼ばれます。

snip 引数はリサイズされるスニップです。

デフォルト実装:
何もしません。

```
+-------------------------------+
| [method]                      |
|                               |
| (send a-pasteboard on-move-to |
| snip: (is-a?/c snip%)        |
| x: real?                     |
| y: real?                     |
| dragging?: any/c             |
+-------------------------------+
```

このメソッドは augment で精錬します。

仕様:
スニップがエディタ内で移動される前、can-move-to? で許可を確認したあとに呼ばれます。完了後に after-move-to が必ず呼ばれます。

dragging? が #f でなければ、この移動はドラッグのための一時的な移動です。

このメソッドが呼ばれるとき、エディタは書き込み用に内部ロックされています（「内部エディタロック」も参照）。位置情報は再計算されていません。

デフォルト実装:
何もしません。

```
+-------------------------------+
| [method]                      |
|                               |
| (send a-pasteboard on-reorder |
| snip: (is-a?/c snip%)        |
| to-snip: (is-a?/c snip%)     |
| before?: any/c               |
+-------------------------------+
```

このメソッドは augment で精錬します。

仕様:
ペーストボードの前後順でスニップが移動される前、can-reorder? で許可を確認したあとに呼ばれます。完了後に after-reorder が必ず呼ばれます。

before? が #t なら snip は to-snip の前へ、そうでなければ後へ移動されます。

このメソッドが呼ばれるとき、エディタは書き込み用に内部ロックされています（「内部エディタロック」も参照）。

デフォルト実装:
何もしません。

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-pasteboard on-resize snip w h) → void? |
| snip: (is-a?/c snip%)                         |
| w: (and/c real? (not/c negative?))            |
| h: (and/c real? (not/c negative?))            |
+------------------------------------------------+
```

このメソッドは augment で精錬します。

仕様:
エディタがスニップをリサイズする前、can-resize? で許可を確認したあとに呼ばれます。完了後に after-resize が必ず呼ばれます。

このメソッドが呼ばれるとき、エディタは書き込み用に内部ロックされています（「内部エディタロック」も参照）。

スニップ自身がリサイズしたことをペーストボードに通知するには、このメソッドではなく resized を呼ぶ点に注意してください。

デフォルト実装:
何もしません。

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-pasteboard on-select snip on?) → void? |
| snip: (is-a?/c snip%)                         |
| on?: any/c                                    |
+------------------------------------------------+
```

このメソッドは augment で精錬します。

仕様:
ペーストボード内のスニップが選択または選択解除される前、can-select? で許可を確認したあとに呼ばれます。完了後に after-select が必ず呼ばれます。選択スニップが削除されるときには呼ばれません（on-delete も参照）。

on? が #t なら snip が選択され、そうでなければ選択が外されます。

このメソッドが呼ばれるとき、エディタは書き込み用に内部ロックされています（「内部エディタロック」も参照）。

デフォルト実装:
何もしません。

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-pasteboard raise snip) → void? |
| snip: (is-a?/c snip%)                 |
+----------------------------------------+
```

a snip one level shallower (i.e., in front of one more other
snip) in the pasteboard’s snip order. See Editor Structure and Terminology for information about snip order in pasteboards を移動します。

lower, set-before, and set-after も参照してください。

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-pasteboard remove snip) → void? |
| snip: (is-a?/c snip%)                  |
+-----------------------------------------+
```

指定スニップをアンドゥ不可の方法でエディタから取り除きます（スニップはペーストボードから完全に自由になり、他のエディタで使えます）。

delete も参照してください。

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-pasteboard remove-selected snip) → void? |
| snip: (is-a?/c snip%)                           |
+--------------------------------------------------+
```

他のスニップの選択を外さずに snip の選択を外します（現在選択中なら）。

ペーストボードの選択は、他のメソッド呼び出しに応じてシステムが変更することがあり、そのような変更はこのメソッドを経由しません。選択変化の監視には on-select を使ってください。

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-pasteboard resize snip w h) → boolean? |
| snip: (is-a?/c snip%)                         |
| w: (and/c real? (not/c negative?))            |
| h: (and/c real? (not/c negative?))            |
+------------------------------------------------+
```

与えられたスニップのリサイズを試みます。スニップがリサイズを許せば #t、そうでなければ #f を返します。

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-pasteboard set-after snip after) → void? |
| snip: (is-a?/c snip%)                           |
| after: (or/c (is-a?/c snip%) #f)                |
+--------------------------------------------------+
```

snip の深さを変え、after の直後へ移します。after が #f なら最背面へ移します。スニップの前後関係については「エディタの構造と用語」を参照してください。

raise, lower, and set-before も参照してください。

```
+-------------------------------------------------------------+
| [method]                                                    |
|                                                             |
| (send a-pasteboard set-area-selectable allow-drag?) → void? |
| allow-drag?: any/c                                         |
+-------------------------------------------------------------+
```

on-default-event のイベント処理で、ペーストボード背景の選択ボックスドラッグによりスニップを選択できるかどうかを設定します。

Added in version 1.12 of package `gui-lib`.

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-pasteboard set-before snip before) → void? |
| snip: (is-a?/c snip%)                             |
| before: (or/c (is-a?/c snip%) #f)                 |
+----------------------------------------------------+
```

snip の深さを変え、before の直前へ移します。before が #f なら最前面へ移します。

raise, lower, and set-after も参照してください。

```
+------------------------------------------------------+
| [method]                                             |
|                                                      |
| (send a-pasteboard set-dragable allow-drag?) → void? |
| allow-drag?: any/c                                  |
+------------------------------------------------------+
```

on-default-event のイベント処理でスニップを対話的にドラッグできるかどうかを設定します。

```
+------------------------------------------------------+
| [method]                                             |
|                                                      |
| (send a-pasteboard set-scroll-step stepsize) → void? |
| stepsize: (and/c real? (not/c negative?))           |
+------------------------------------------------------+
```

各垂直スクロール位置に対するエディタ位置オフセットを設定します。get-scroll-step も参照してください。

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-pasteboard set-selected snip) → void? |
| snip: (is-a?/c snip%)                        |
+-----------------------------------------------+
```

指定スニップを選択します（他はすべて選択解除）。

ペーストボードの選択は、他のメソッド呼び出しに応じてシステムが変更することがあり、そのような変更はこのメソッドを経由しません。選択変化の監視には on-select を使ってください。

```
+------------------------------------------------------------+
| [method]                                                   |
|                                                            |
| (send a-pasteboard set-selection-visible visible?) → void? |
| visible?: any/c                                           |
+------------------------------------------------------------+
```

ペーストボード内の選択スニップの縁に選択ドットを描くかどうかを設定します。get-selection-visible も参照してください。

---

## popup-menu%

```
+---------------------------+------------------------+
| classpopup-menu%: class? |                        |
+---------------------------+------------------------+
| superclass: object%       |                        |
| extends:                  | menu-item-container<%> |
+---------------------------+------------------------+
```

`popup-menu%` オブジェクトは親なしで作成されます。popup-menu in window<%> または popup-menu in editor-admin% で動的に表示します。

ポップアップメニューはコントロールではありません。ただし choice% コントロールは、ユーザーがポップアップメニュー風のインタフェースで選ぶ単一の値を表示します。

```
+--------------------------------------------------------------------------------+
| [constructor]                                                                  |
|                                                                                |
| (new popup-menu%                                                               |
| → (is-a?/c popup-menu%)                                                        |
| title: (or/c label-string? #f) = #f                                           |
| popdown-callback: ((is-a?/c popup-menu%) (is-a?/c control-event%). ->. any) |
| = (lambda (p e) (void))                                                        |
| ((is-a?/c popup-menu%) (is-a?/c control-event%)                                |
|. ->. any)                                                                    |
| demand-callback: ((is-a?/c popup-menu%). ->. any) = (lambda (p) (void))     |
| font: (is-a?/c font%) = normal-control-font                                   |
|                                                                                |
| ```racket                                                                      |
| ((is-a?/c popup-menu%) (is-a?/c control-event%)                                |
|. ->. any)                                                                   |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

title が #f でなければ、ポップアップメニュー上部の表示タイトルとして使われます。

title に & が含まれると、menu% のタイトルと同様に特別扱いされます。ポップアップメニューのニーモニックは意味を持ちません。

popdown-callback 手続きはポップアップメニューが閉じられたときに呼ばれます。項目選択で閉じられた場合、コールバックは選択項目のコールバックのあとで呼ばれます。引数のイベント型は 'menu-popdown または 'menu-popdown-none です。

demand-callback 手続きは、既定の on-demand メソッドからオブジェクト自身を引数に呼ばれます。

font 引数はポップアップメニュー項目のフォントを決めます。

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-popup-menu get-font) → (is-a?/c font%) |
+------------------------------------------------+
```

ポップアップメニュー作成時に任意で渡す、項目用フォントを返します。

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-popup-menu get-popup-target)                |
| → (or/c (is-a?/c window<%>) (is-a?/c editor<%>) #f) |
+-----------------------------------------------------+
```

ポップアップメニューが現在表示されている文脈を返します。どのウィンドウでもポップアップされていなければ #f です。

context は on-demand メソッドが呼ばれる前に設定され、ポップアップメニューの popdown-callback が戻るまで取り除かれません。

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-popup-menu set-min-width width) → void? |
| width: dimension-integer?                      |
+-------------------------------------------------+
```

popup menu’s minimum width in pixels を設定します。

---

## printer-dc%

```
+---------------------------+-------+
| classprinter-dc%: class? |       |
+---------------------------+-------+
| superclass: object%       |       |
| extends:                  | dc<%> |
+---------------------------+-------+
```

`printer-dc%` オブジェクトはプリンタデバイスコンテキストです。新規作成された printer-dc% は、current-ps-setup の構成から向きなどの情報を取得します。

描画の開始／終了には次のメソッドを必ず使ってください。

- start-doc
- start-page
- end-page
- end-doc

アクティブなページの外で描画メソッドを使おうとすると例外が発生します。

post-script-dc% も参照してください。

printer-dc% インスタンスで end-doc メソッドが呼ばれると、ユーザーはジョブを実際に印刷するかを決めるダイアログを見ることがあります。

```
+-------------------------------------------------------------+
| [constructor]                                               |
|                                                             |
| (new printer-dc% [[parent parent]]) → (is-a?/c printer-dc%) |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f  |
+-------------------------------------------------------------+
```

parent が #f でなければ、end-doc が表示するダイアログ（あれば）の親ウィンドウとして使われることがあります。

---

## radio-box%

> [image: radio-box.png]

```
+--------------------------+------------+
| classradio-box%: class? |            |
+--------------------------+------------+
| superclass: object%      |            |
| extends:                 | control<%> |
+--------------------------+------------+
```

`radio-box%` コントロールは、互いに排他的な項目のひとつをユーザーが選べるようにします。項目は文字列またはビットマップのリストです。

ユーザーが選択中のラジオボタンを変えるたびに、ラジオボックスのコールバック手続きが呼ばれます。コールバックは作成時の初期化引数として渡されます。

```
+-------------------------------------------------------------------------------+
| [constructor]                                                                 |
|                                                                               |
| (new radio-box%                                                               |
| → (is-a?/c radio-box%)                                                        |
| label: (or/c label-string? #f)                                               |
| choices: (or/c (listof label-string?) (listof (is-a?/c bitmap%)))            |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c   |
| pane%))                                                                       |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                      |
| (is-a?/c panel%) (is-a?/c pane%))                                             |
| callback: ((is-a?/c radio-box%) (is-a?/c control-event%). ->. any) =       |
| (lambda (r e) (void))                                                         |
| ((is-a?/c radio-box%) (is-a?/c control-event%)                                |
|. ->. any)                                                                   |
| style: (listof (or/c 'horizontal 'vertical 'vertical-label 'horizontal-label |
| 'deleted)) = '(vertical)                                                      |
| (listof (or/c 'horizontal 'vertical                                           |
| 'vertical-label 'horizontal-label                                             |
| 'deleted))                                                                    |
| selection: (or/c exact-nonnegative-integer? #f) = 0                          |
| font: (is-a?/c font%) = normal-control-font                                  |
| enabled: any/c = #t                                                          |
| vert-margin: spacing-integer? = 2                                            |
| horiz-margin: spacing-integer? = 2                                           |
| min-width: (or/c dimension-integer? #f) = #f                                 |
| min-height: (or/c dimension-integer? #f) = #f                                |
| stretchable-width: any/c = #f                                                |
| stretchable-height: any/c = #f                                               |
|                                                                               |
| ```racket                                                                     |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                      |
|       (is-a?/c panel%) (is-a?/c pane%))                                       |
| ```                                                                           |
|                                                                               |
| ```racket                                                                     |
| ((is-a?/c radio-box%) (is-a?/c control-event%)                                |
|. ->. any)                                                                  |
| ```                                                                           |
|                                                                               |
| ```racket                                                                     |
| (listof (or/c 'horizontal 'vertical                                           |
|               'vertical-label 'horizontal-label                               |
|               'deleted))                                                      |
| ```                                                                           |
+-------------------------------------------------------------------------------+
```

文字列またはビットマップラベルのラジオボタン集合を作成します。choices リストがラベルを指定し、すべて文字列かすべてビットマップで均質でなければなりません。

label に & が含まれると、button% と同様に特別に解析されます。

choices 内の各文字列にも & を含められ、対応するボタンをクリックするニーモニックを作ります（button% と同様）。

choices がビットマップのリストで、ビットマップに同じサイズのマスク（bitmap% の get-loaded-mask を参照）がある場合、ラベルにマスクが使われます。ラベル使用中のビットマップ変更の表示効果は未規定です。

label が文字列ならラジオボックスのラベルとして使われます。そうでなければラベルは表示されません。

callback 手続きは、ユーザーがラジオボタン選択を変えたとき（イベント型 'radio-box）に呼ばれます。

style 引数には、ラジオボタンを縦に並べる 'vertical または横に並べる 'horizontal のいずれかを含めなければなりません。'vertical-label があればラベルはコントロールの上、なければ（任意で 'horizontal-label）左に付きます。'deleted があれば非表示で作成され親のジオメトリに影響せず、後から親の add-child で有効化できます。

既定では最初のラジオボタンが初期選択されます。selection が正または #f なら set-selection に渡して初期選択を設定します。

font はコントロールのフォントを決めます。enabled については window<%>、horiz-margin と vert-margin については subarea<%>、min-width、min-height、stretchable-width、stretchable-height については area<%> を参照。

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-radio-box enable enable?) → void?   |
| enable?: any/c                             |
| (send a-radio-box enable n enable?) → void? |
| n: exact-nonnegative-integer?              |
| enable?: any/c                             |
+---------------------------------------------+
```

enable in window<%> をオーバーライドします。

引数が 1 つだけなら、ラジオボックス全体を有効または無効にします。

引数が 2 つなら、enable? が #f のとき n 番目のラジオボタンを無効にし、そうでなければ有効にします。ラジオボックス全体が無効なら、個々のボタンの有効状態にかかわらずすべてのボタンが無効です。

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-radio-box get-item-label n) → string? |
| n: exact-nonnegative-integer?                |
+-----------------------------------------------+
```

位置でラジオボタンのラベルを取得します。ラジオボタンは 0 から番号付けされます。n が個数以上なら exn:fail:contract 例外が発生します。

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-radio-box get-item-plain-label n) → string? |
| n: exact-nonnegative-integer?                      |
+-----------------------------------------------------+
```

get-item-label と同様ですが、ラベルは文字列でなければならず、ラベル内の & は取り除かれます。

```
+------------------------------------------------------------+
| [method]                                                   |
|                                                            |
| (send a-radio-box get-number) → exact-nonnegative-integer? |
+------------------------------------------------------------+
```

ラジオボックス内のラジオボタンの個数を返します。

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-radio-box get-selection)       |
| → (or/c exact-nonnegative-integer? #f) |
+----------------------------------------+
```

選択中ラジオボタンの位置を取得します。何も選ばれていなければ #f です。ラジオボタンは 0 から番号付けされます。

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-radio-box is-enabled?) → boolean?   |
| (send a-radio-box is-enabled? n) → boolean? |
| n: exact-nonnegative-integer?              |
+---------------------------------------------+
```

is-enabled? in window<%> をオーバーライドします。

引数がなければ、ラジオボックス全体の有効状態を報告します。

そうでなければ、n 番目のラジオボタンが（ラジオボックス全体の無効化とは独立に）無効なら #f、有効なら #t を返します。n が大きすぎると exn:fail:contract 例外が発生します。

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send a-radio-box set-selection n) → void? |
| n: (or/c exact-nonnegative-integer? #f)   |
+--------------------------------------------+
```

位置で選択中ラジオボタンを設定するか、n が #f ならすべて選択解除します（コールバックは呼ばれません）。ラジオボタンは 0 から。n が個数以上なら exn:fail:contract 例外が発生します。

ラジオボックスの選択はユーザーのクリックで変わり得、その変更はこのメソッドを経由しません。選択変化の監視にはコントロールのコールバックを使ってください。

---
