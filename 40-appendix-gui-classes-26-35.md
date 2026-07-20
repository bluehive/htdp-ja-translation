# 付録 D（続き）: GUI クラス参照（26–35）

以下は `extracted/appendix/gui/original_markdown_26` 〜 `35` の日本語訳です。

---

## clipboard-client%

```
+---------------------------------+
| classclipboard-client%: class? |
+---------------------------------+
| superclass: object%             |
+---------------------------------+
```

`clipboard-client%` オブジェクトは、プログラムがクリップボードを掌握し、クリップボードデータへの要求に応えることを可能にします。詳細は `clipboard<%>` を参照してください。

`clipboard-client%` オブジェクトは、現在のクライアントになったときにイベントスペースに関連付けられます。詳細は `set-clipboard-client` を参照してください。

```
+-------------------------------------------------------+
| [コンストラクタ]                                      |
|                                                       |
| (new clipboard-client%) → (is-a?/c clipboard-client%) |
+-------------------------------------------------------+
```

どのデータ形式もサポートしないクリップボードクライアントを生成します。

```
+---------------------------------------------------+
| [メソッド]                                        |
|                                                   |
| (send a-clipboard-client add-type format) → void? |
| format: string?                                  |
+---------------------------------------------------+
```

クリップボードクライアントがサポートするリストに、新しいデータ形式名を追加します。

`format` 文字列は通常 4 文字の大文字です（Mac OS では `format` のうち最初の 4 文字だけが使われます）。たとえば `"TEXT"` は UTF-8 符号化文字列形式の名前です。新しい形式名は、アプリケーション固有およびプラットフォーム固有のデータ形式の通信に使えます。

```
+-------------------------------------------+
| [メソッド]                                |
|                                           |
| (send a-clipboard-client get-data format) |
| → (or/c bytes? string? #f)                |
| format: string?                          |
+-------------------------------------------+
```

このクライアントがクリップボードの現在のクライアントであるあいだに、あるプロセスがクリップボードデータを要求したときに呼ばれます。要求された形式がメソッドに渡され、結果は要求された形式に合うバイト文字列、または要求を満たせない場合は `#f` でなければなりません。

クライアントのリストにあるデータ形式名だけがこのメソッドに渡されます。`add-type` を参照してください。

クリップボードがこのメソッドを呼ぶとき、現在のイベントスペースはクライアントのイベントスペースと同じです。クリップボード要求の時点で現在のイベントスペースがクライアントのイベントスペースでない場合、現在のスレッドはクライアントのイベントスペースのハンドラスレッドであることが保証されます。

```
+--------------------------------------------------------+
| [メソッド]                                             |
|                                                        |
| (send a-clipboard-client get-types) → (listof string?) |
+--------------------------------------------------------+
```

クリップボードクライアントがサポートするデータ形式の名前のリストを返します。

```
+-----------------------------------------------+
| [メソッド]                                    |
|                                               |
| (send a-clipboard-client on-replaced) → void? |
+-----------------------------------------------+
```

クリップボードクライアントがクリップボード所有者から外されたときに呼ばれます（別のクライアントまたは外部アプリケーションがクリップボードを掌握したため）。

---

## clipboard<%>

```
+------------------------------------+
| interfaceclipboard<%>: interface? |
+------------------------------------+
+------------------------------------+
```

単一の `clipboard<%>` オブジェクト `the-clipboard` が、カット＆ペースト用のシステム全体のクリップボードの内容を管理します。

Unix では、第二の `clipboard<%>` オブジェクト `the-x-selection-clipboard` が、システム全体の X11 セレクションの内容を管理します。ただし、`'GRacket:selectionAsClipboard` 環境設定（Preferences を参照）が非ゼロの真値に設定されている場合、`the-clipboard` は常に `the-x-selection-clipboard` と同じになり、システム全体の X11 クリップボードは使われません。

Windows と Mac OS では、`the-x-selection-clipboard` は常に `the-clipboard` と同じです。

クリップボードへデータを入れる方法は二つあります。現在のクリップボード文字列またはバイト文字列を設定する方法と、`clipboard-client%` オブジェクトをインストールする方法です。クライアントがインストールされているとき、クリップボードデータへの要求はクライアントに向けられます。

汎用データは常にバイト文字列としてクリップボードから取得されます。クリップボードデータを取得するとき、データ型文字列がデータ文字列の形式を指定します。利用可能なクリップボード形式は、現在のクリップボード所有者によって決まります。

```
+----------------------------------------------+
| [メソッド]                                   |
|                                              |
| (send a-clipboard get-clipboard-bitmap time) |
| → (or/c (is-a?/c bitmap%) #f)                |
| time: exact-integer?                        |
+----------------------------------------------+
```

現在のクリップボード内容をビットマップとして取得します（Windows、Mac OS）。クリップボードにビットマップが含まれない場合は `#f` を返します。

イベントスペースと現在のクリップボードクライアントについては `get-clipboard-data` を参照してください。

`time` 引数の議論は Cut and Paste Time Stamps を参照してください。`time` がプラットフォーム固有の時刻範囲外の場合、`exn:fail:contract` 例外が送出されます。

```
+--------------------------------------+
| [メソッド]                           |
|                                      |
| (send a-clipboard get-clipboard-data |
| → (or/c bytes? string? #f)           |
| format: string?                     |
| time: exact-integer?                |
+--------------------------------------+
```

現在のクリップボード内容を特定の形式で取得します。要求された形式のデータが含まれない場合は `#f` を返します。

クリップボードクライアントが現在のものでないイベントスペースに関連付けられている場合、データはクライアントのイベントスペース内のコールバックイベント経由で取得されます。1 秒以内に結果が得られない場合、要求は破棄され `#f` が返されます。

`format` については `clipboard-client%` の `add-type` を参照してください。

`time` 引数の議論は Cut and Paste Time Stamps を参照してください。`time` がプラットフォーム固有の時刻範囲外の場合、`exn:fail:contract` 例外が送出されます。

```
+--------------------------------------------------------+
| [メソッド]                                             |
|                                                        |
| (send a-clipboard get-clipboard-string time) → string? |
| time: exact-integer?                                  |
+--------------------------------------------------------+
```

現在のクリップボード内容を単純なテキストとして取得します。クリップボードにテキストが含まれない場合は `""` を返します。

イベントスペースと現在のクリップボードクライアントについては `get-clipboard-data` を参照してください。

`time` 引数の議論は Cut and Paste Time Stamps を参照してください。`time` がプラットフォーム固有の時刻範囲外の場合、`exn:fail:contract` 例外が送出されます。

```
+------------------------------------------------------------+
| [メソッド]                                                 |
|                                                            |
| (send a-clipboard same-clipboard-client? owner) → boolean? |
| owner: (is-a?/c clipboard-client%)                        |
+------------------------------------------------------------+
```

`owner` が現在クリップボードを所有しているなら `#t`、そうでなければ `#f` を返します。

```
+----------------------------------------+
| [メソッド]                             |
|                                        |
| (send a-clipboard set-clipboard-bitmap |
| new-bitmap: (is-a?/c bitmap%)         |
| time: exact-integer?                  |
+----------------------------------------+
```

現在のクリップボード内容を `new-bitmap` に変更し（Windows、Mac OS）、現在のクリップボードクライアント（あれば）を解放します。

`time` 引数の議論は Cut and Paste Time Stamps を参照してください。`time` がプラットフォーム固有の時刻範囲外の場合、`exn:fail:contract` 例外が送出されます。

```
+-----------------------------------------+
| [メソッド]                              |
|                                         |
| (send a-clipboard set-clipboard-client  |
| new-owner: (is-a?/c clipboard-client%) |
| time: exact-integer?                   |
+-----------------------------------------+
```

クリップボードを所有するクライアントを変更します。クライアントを `new-owner` に設定し、`new-owner` を現在のイベントスペース（`current-eventspace` が決定）に関連付けます。クライアントが現在のクライアントでなくなったとき、イベントスペースとの関連付けは解除されます。

`time` 引数の議論は Cut and Paste Time Stamps を参照してください。`time` がプラットフォーム固有の時刻範囲外の場合、`exn:fail:contract` 例外が送出されます。

```
+----------------------------------------+
| [メソッド]                             |
|                                        |
| (send a-clipboard set-clipboard-string |
| new-text: string?                     |
| time: exact-integer?                  |
+----------------------------------------+
```

現在のクリップボード内容を `new-text` に変更し、現在のクリップボードクライアント（あれば）を解放します。

`time` 引数の議論は Cut and Paste Time Stamps を参照してください。`time` がプラットフォーム固有の時刻範囲外の場合、`exn:fail:contract` 例外が送出されます。

---

## column-control-event%

```
+-------------------------------------+
| classcolumn-control-event%: class? |
+-------------------------------------+
| superclass: control-event%          |
+-------------------------------------+
```

`column-control-event%` オブジェクトは、`list-box%` の列ヘッダ上のイベントに関する情報を含みます。Windows 以外では、列イベントを生成するために `list-box%` 生成時に `'clickable-headers` スタイルを指定しなければなりません。

```
+--------------------------------------+
| [コンストラクタ]                     |
|                                      |
| (new column-control-event%           |
| → (is-a?/c column-control-event%)    |
| column: exact-nonnegative-integer?  |
| event-type: (or/c 'list-box-column) |
| time-stamp: exact-integer? = 0      |
+--------------------------------------+
```

`column` 引数はクリックされた列を示します。

```
+------------------------------------------+
| [メソッド]                               |
|                                          |
| (send a-column-control-event get-column) |
| → exact-nonnegative-integer?             |
+------------------------------------------+
```

クリックされた列の列番号（0 から数える）を返します。

```
+---------------------------------------------------------+
| [メソッド]                                              |
|                                                         |
| (send a-column-control-event set-column column) → void? |
| column: exact-nonnegative-integer?                     |
+---------------------------------------------------------+
```

クリックされた列の列番号（0 から数える）を設定します。

---

## combo-field%

> [image: combo-field.png]
```
  +--------------------+-+
  | テキスト入力     v |
  +--------------------+-+
```

```
+----------------------------+
| classcombo-field%: class? |
+----------------------------+
| superclass: text-field%    |
+----------------------------+
```

`combo-field%` オブジェクトは、`text-field%` オブジェクトであると同時に `choice%` オブジェクトにも似ています。テキストフィールドの右に小さなポップアップボタンがあるためです。ボタンをクリックするとメニューがポップアップし、メニュー項目を選択すると通常その項目がテキストフィールドにコピーされます。

```
+-----------------------------------------------------------------------------+
| [コンストラクタ]                                                            |
|                                                                             |
| (new combo-field%                                                           |
| → (is-a?/c combo-field%)                                                    |
| label: (or/c label-string? #f)                                             |
| choices: (listof label-string?)                                            |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c |
| pane%))                                                                     |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                    |
| (is-a?/c panel%) (is-a?/c pane%))                                           |
| callback: ((is-a?/c combo-field%) (is-a?/c control-event%). ->. any) =   |
| (lambda (c e) (void))                                                       |
| ((is-a?/c combo-field%) (is-a?/c control-event%)                            |
|. ->. any)                                                                 |
| init-value: string = ""                                                    |
| style: (listof (or/c 'horizontal-label 'vertical-label 'deleted)) = null   |
| (listof (or/c 'horizontal-label 'vertical-label                             |
| 'deleted))                                                                  |
| font: (is-a?/c font%) = normal-control-font                                |
| enabled: any/c = #t                                                        |
| vert-margin: spacing-integer? = 2                                          |
| horiz-margin: spacing-integer? = 2                                         |
| min-width: (or/c dimension-integer? #f) = #f                               |
| min-height: (or/c dimension-integer? #f) = #f                              |
| stretchable-width: any/c = #t                                              |
| stretchable-height: any/c = #f                                             |
|                                                                             |
| ```racket                                                                   |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                    |
|       (is-a?/c panel%) (is-a?/c pane%))                                     |
| ```                                                                         |
|                                                                             |
| ```racket                                                                   |
| ((is-a?/c combo-field%) (is-a?/c control-event%)                            |
|. ->. any)                                                                |
| ```                                                                         |
|                                                                             |
| ```racket                                                                   |
| (listof (or/c 'horizontal-label 'vertical-label                             |
|               'deleted))                                                    |
| ```                                                                         |
+-----------------------------------------------------------------------------+
```

`label` が `#f` でない場合、コンボのラベルとして使われます。そうでなければ、コンボはラベルを表示しません。

`label` に `&` が含まれる場合、`button%` と同様に特別に解析されます。

`choices` リストは、コンボのポップアップメニューの初期項目リストを指定します。`append` メソッドは、追加した項目をコンボのテキストフィールドに入れるコールバック付きでメニューに新しい項目を追加します。`get-menu` メソッドは、コンボのメニューの内容と動作を調整するために変更できるメニューを返します。

コールバック手続きは、ユーザがコンボ内のテキストを変更したとき、または Enter キーを押したとき（かつ Enter がコンボのフレームまたはダイアログで処理されないとき。`top-level-window<%>` の `on-traverse-char` を参照）に呼ばれます。ユーザが Enter を押した場合、コールバックに渡されるイベント型は `'text-field-enter`、それ以外は `'text-field` です。

`init-value` が `""` でない場合、テキスト項目の最小幅は `init-value` を表示できるだけの広さになります。そうでなければ、組み込みの既定幅が選ばれます。

`style` に `'vertical-label` が含まれる場合、コンボはコントロールの上にラベルを付けて生成されます。`style` に `'vertical-label` が含まれない場合（任意で `'horizontal-label` を含めてもよい）、ラベルはコンボの左に生成されます。`style` に `'deleted` が含まれる場合、コンボは非表示として生成され、親のジオメトリに影響しません。後から親の `add-child` メソッドを呼ぶことで有効にできます。

`font` 引数はコントロールのフォントを決めます。`enabled` 引数については `window<%>` を参照してください。`horiz-margin` と `vert-margin` については `subarea<%>` を、`min-width`、`min-height`、`stretchable-width`、`stretchable-height` については `area<%>` を参照してください。

```
+---------------------------------------+
| [メソッド]                            |
|                                       |
| (send a-combo-field append l) → void? |
| l: label-string?                     |
+---------------------------------------+
```

コンボのポップアップメニューに新しい項目を追加します。与えられたラベルが項目名に使われ、項目のコールバックはそのラベルをコンボのテキストフィールドに入れます。

```
+-------------------------------------------------------+
| [メソッド]                                            |
|                                                       |
| (send a-combo-field get-menu) → (is-a?/c popup-menu%) |
+-------------------------------------------------------+
```

コンボがクリックされたときにコンボのポップアップメニューへ実質的にコピーされる `popup-menu%` を返します。使われるのはメニュー項目のラベルとコールバックだけです。有効状態、サブメニュー、区切りは無視されます。

```
+---------------------------------------------+
| [メソッド]                                  |
|                                             |
| (send a-combo-field on-popup event) → void? |
| event: (is-a?/c control-event%)            |
+---------------------------------------------+
```

仕様:
ユーザがコンボのポップアップボタンをクリックしたときに呼ばれます。このメソッドをオーバーライドして、必要に応じてコンボメニューの内容を調整してください。

既定の実装:
何もしません。

---

## control-event%

```
+------------------------------+
| classcontrol-event%: class? |
+------------------------------+
| superclass: event%           |
+------------------------------+
```

`control-event%` オブジェクトは、コントロールイベントに関する情報を含みます。`control-event%` のインスタンスは、常にコントロールまたはメニュー項目のコールバック手続きに渡されます。

```
+--------------------------------------------------------------------------+
| [コンストラクタ]                                                         |
|                                                                          |
| (new control-event%                                                      |
| → (is-a?/c control-event%)                                               |
| event-type: (or/c 'button 'check-box 'choice 'list-box 'list-box-dclick |
| 'list-box-column 'text-field 'text-field-enter 'menu 'slider 'radio-box  |
| 'tab-panel 'menu-popdown 'menu-popdown-none)                             |
| (or/c 'button 'check-box 'choice                                         |
| 'list-box 'list-box-dclick 'list-box-column                              |
| 'text-field 'text-field-enter                                            |
| 'menu 'slider 'radio-box 'tab-panel                                      |
| 'menu-popdown 'menu-popdown-none)                                        |
| time-stamp: exact-integer? = 0                                          |
|                                                                          |
| ```racket                                                                |
| (or/c 'button 'check-box 'choice                                         |
|       'list-box 'list-box-dclick 'list-box-column                        |
|       'text-field 'text-field-enter                                      |
|       'menu 'slider 'radio-box 'tab-panel                                |
|       'menu-popdown 'menu-popdown-none)                                  |
| ```                                                                      |
+--------------------------------------------------------------------------+
```

`event-type` 引数は次のいずれかです。

- `'button` — `button%` のクリック
- `'check-box` — `check-box%` のトグル
- `'choice` — `choice%` の項目選択
- `'list-box` — `list-box%` の選択と選択解除
- `'list-box-dclick` — `list-box%` のダブルクリック
- `'list-box-column` — `column-control-event%` インスタンスにおける `list-box%` の列クリック
- `'text-field` — `text-field%` の変更
- `'text-field-enter` — 単一行 `text-field%` の Enter イベント
- `'menu` — `selectable-menu-item<%>` のコールバック
- `'slider` — `slider%` の変更
- `'radio-box` — `radio-box%` の選択変更
- `'tab-panel` — `tab-panel%` のタブ変更
- `'menu-popdown` — `popup-menu%` のコールバック（項目が選択された）
- `'menu-popdown-none` — `popup-menu%` のコールバック（項目が選択されなかった）

この値は `control-event%` オブジェクトから `get-event-type` メソッドで取り出します。

`time-stamp` については `get-time-stamp` を参照してください。

```
+-----------------------------------------------------------------------------+
| [メソッド]                                                                  |
|                                                                             |
| (send a-control-event get-event-type)                                       |
| → (or/c 'button 'check-box 'choice 'list-box 'list-box-dclick 'text-field   |
| 'text-field-enter 'menu 'slider 'radio-box 'menu-popdown 'menu-popdown-none |
| 'tab-panel)                                                                 |
| (or/c 'button 'check-box 'choice                                            |
| 'list-box 'list-box-dclick 'text-field                                      |
| 'text-field-enter 'menu 'slider 'radio-box                                  |
| 'menu-popdown 'menu-popdown-none 'tab-panel)                                |
|                                                                             |
| ```racket                                                                   |
| (or/c 'button 'check-box 'choice                                            |
|       'list-box 'list-box-dclick 'text-field                                |
|       'text-field-enter 'menu 'slider 'radio-box                            |
|       'menu-popdown 'menu-popdown-none 'tab-panel)                          |
| ```                                                                         |
+-----------------------------------------------------------------------------+
```

コントロールイベントの型を返します。各イベント型記号については `control-event%` を参照してください。

```
+--------------------------------------------------------------------------------+
| [メソッド]                                                                     |
|                                                                                |
| (send a-control-event set-event-type type) → void?                             |
| type: (or/c 'button 'check-box 'choice 'list-box 'list-box-dclick 'text-field |
| 'text-field-enter 'menu 'slider 'radio-box 'menu-popdown 'menu-popdown-none    |
| 'tab-panel)                                                                    |
| (or/c 'button 'check-box 'choice                                               |
| 'list-box 'list-box-dclick 'text-field                                         |
| 'text-field-enter 'menu 'slider 'radio-box                                     |
| 'menu-popdown 'menu-popdown-none 'tab-panel)                                   |
|                                                                                |
| ```racket                                                                      |
| (or/c 'button 'check-box 'choice                                               |
|       'list-box 'list-box-dclick 'text-field                                   |
|       'text-field-enter 'menu 'slider 'radio-box                               |
|       'menu-popdown 'menu-popdown-none 'tab-panel)                             |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

イベントの型を設定します。各イベント型記号については `control-event%` を参照してください。

---

## control<%>

```
+----------------------------------+--------------+
| interfacecontrol<%>: interface? |              |
+----------------------------------+--------------+
| implements:                      | subwindow<%> |
+----------------------------------+--------------+
```

`control<%>` インタフェースは、組み込みのコントロールウィンドウクラスによって実装されます。

- `message%`
- `button%`
- `check-box%`
- `slider%`
- `gauge%`
- `text-field%`
- `radio-box%`
- `choice%`
- `list-box%`

```
+----------------------------------------+
| [メソッド]                             |
|                                        |
| (send a-control command event) → void? |
| event: (is-a?/c control-event%)       |
+----------------------------------------+
```

与えられた `control-event%` オブジェクトを渡して、コントロールのコールバック関数を呼び出します。

---

## cursor%

```
+-----------------------+
| classcursor%: class? |
+-----------------------+
| superclass: object%   |
+-----------------------+
```

カーソルは、マウスポインタの位置を示す小さなアイコンです。ビットマップ画像は通常、現在の位置でのマウスクリックのモードや意味を示します。

カーソルは各ウィンドウに割り当てられます（またはウィンドウは親のカーソルを使うこともあります。詳細は `set-cursor` を参照）。ポインタがそのウィンドウ上を移動すると、ポインタ画像はウィンドウのカーソルに合わせて変わります。各カーソルオブジェクトは多くのウィンドウに割り当てることができます。

```
+-------------------------------------------------------------------------+
| [コンストラクタ]                                                        |
|                                                                         |
| (make-object cursor%                                                    |
| image: (is-a?/c bitmap%)                                               |
| mask: (is-a?/c bitmap%)                                                |
| hot-spot-x: (integer-in 0 15) = 0                                      |
| hot-spot-y: (integer-in 0 15) = 0                                      |
| (make-object cursor% id) → (is-a?/c cursor%)                            |
| id: (or/c 'arrow 'bullseye 'cross 'hand 'ibeam 'watch 'blank 'size-n/s |
| 'size-e/w 'size-ne/sw 'size-nw/se)                                      |
| (or/c 'arrow 'bullseye 'cross 'hand 'ibeam 'watch 'blank                |
| 'size-n/s 'size-e/w 'size-ne/sw 'size-nw/se)                            |
|                                                                         |
| ```racket                                                               |
| (or/c 'arrow 'bullseye 'cross 'hand 'ibeam 'watch 'blank                |
|       'size-n/s 'size-e/w 'size-ne/sw 'size-nw/se)                      |
| ```                                                                     |
+-------------------------------------------------------------------------+
```

第一の場合は、画像ビットマップとマスクビットマップを使ってカーソルを生成します。両方のビットマップは深さ 1、大きさ 16×16 ピクセルでなければなりません。`hot-spot-x` と `hot-spot-y` 引数は、カーソル画像内のフォーカス点を、左上隅からの相対位置で決めます。

第二の場合は、次のいずれかで指定されるストックカーソルを使ってカーソルを生成します。

- `'arrow` — 既定のカーソル
- `'bullseye` — 同心円
- `'cross` — 十字線
- `'hand` — 開いた手
- `'ibeam` — 垂直線。クリックがテキスト選択キャレットを制御することを示す
- `'watch` — 時計または砂時計。計算の完了を待つ必要があることを示す
- `'arrow+watch` — 時計または砂時計付きの既定カーソル。何らかの計算が進行中だがカーソルはまだ使えることを示す
- `'blank` — 不可視
- `'size-e/w` — 左右の矢印
- `'size-n/s` — 上下の矢印
- `'size-ne/sw` — 右上と左下の矢印
- `'size-nw/se` — 左上と右下の矢印

カーソルが正常に生成された場合、`ok?` は `#t` を返します。そうでなければ、そのカーソルオブジェクトはウィンドウに割り当てられません。

```
+--------------------------------+
| [メソッド]                     |
|                                |
| (send a-cursor ok?) → boolean? |
+--------------------------------+
```

カーソルをウィンドウに割り当てられるなら `#t`、そうでなければ `#f` を返します。

---

## dialog%

```
+-----------------------+---------------------+
| classdialog%: class? |                     |
+-----------------------+---------------------+
| superclass: object%   |                     |
| extends:              | top-level-window<%> |
+-----------------------+---------------------+
```

ダイアログはモーダルなトップレベルウィンドウです。ダイアログが表示されているあいだ、ダイアログのイベントスペース内の他のすべてのトップレベルウィンドウでは、キーおよびマウスの押下／解放イベントが無効になります。

```
+--------------------------------------------------------------------------------+
| [コンストラクタ]                                                               |
|                                                                                |
| (new dialog%                                                                   |
| → (is-a?/c dialog%)                                                            |
| label: label-string?                                                          |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f                     |
| width: (or/c dimension-integer? #f) = #f                                      |
| height: (or/c dimension-integer? #f) = #f                                     |
| x: (or/c dimension-integer? #f) = #f                                          |
| y: (or/c dimension-integer? #f) = #f                                          |
| style: (listof (or/c 'no-caption 'resize-border 'no-sheet 'close-button)) =   |
| null                                                                           |
| (listof (or/c 'no-caption 'resize-border                                       |
| 'no-sheet 'close-button))                                                      |
| enabled: any/c = #t                                                           |
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
| (listof (or/c 'no-caption 'resize-border                                       |
|               'no-sheet 'close-button))                                        |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (list/c (or/c 'left 'center 'right)                                            |
|         (or/c 'top 'center 'bottom))                                           |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

`label` 文字列は、タイトルバーにおけるダイアログのタイトルとして使われます。ダイアログのラベルが変更されると（`set-label` を参照）、タイトルバーが更新されます。

`parent` 引数は `#f`、または既存のフレームまたはダイアログです。Windows では、`parent` が `#f` でない場合、新しいダイアログは常に親の上に表示されます。Windows と Unix では、親がアイコン化されるとダイアログもアイコン化されます。

`parent` が `#f` の場合、新しいダイアログのイベントスペースは、`current-eventspace` が決める現在のイベントスペースです。そうでなければ、親のイベントスペースが新しいダイアログのイベントスペースになります。

`width` または `height` 引数が `#f` でない場合、それはダイアログの初期サイズ（ピクセル単位）を指定します。ただし最小サイズより大きい場合に限り、そうでなければ最小サイズが使われます。Windows と Mac OS（および一部の Unix ウィンドウマネージャ）では、ダイアログはリサイズできません。

`x` または `y` 引数が `#f` でない場合、ダイアログの初期位置を指定します。そうでなく、表示前に位置が設定されていない場合は、中央に配置されます（`parent` が `#f` でなければ親に対して、そうでなければ画面に対して）。

`style` フラグは、一部のプラットフォームでダイアログの外観を調整します。

- `'no-caption` — ダイアログのタイトルバーを省略する（Windows）
- `'resize-border` — ウィンドウ周囲にリサイズ可能な枠線を追加する（Windows）、ウィンドウのリサイズを可能にする（Mac OS）、または右下にグローボックスを付ける（古い Mac OS）
- `'no-sheet` — 親ウィンドウが与えられていても、ダイアログに移動可能なウィンドウを使う（Mac OS）
- `'close-button` — 通常は含まれないクローズボタンをダイアログのタイトルバーに含める（Mac OS）

ダイアログが表示されていなくても、生成時に少数の通知イベントがダイアログ用にキューに入ることがあります。そのため、新しいダイアログの資源（メモリなど）は、いくつかのイベントが処理されるか、ダイアログのイベントスペースがシャットダウンされるまで回収できません。

`enabled` 引数については `window<%>` を参照してください。`border`、`spacing`、`alignment` については `area-container<%>` を、`min-width`、`min-height`、`stretchable-width`、`stretchable-height` については `area<%>` を参照してください。

```
+----------------------------------+
| [メソッド]                       |
|                                  |
| (send a-dialog on-subwindow-char |
| receiver: (is-a?/c window<%>)   |
| event: (is-a?/c key-event%)     |
+----------------------------------+
```

`window<%>` の `on-subwindow-char` をオーバーライドします。

次の結果を返します。

```racket
(or (send this on-system-menu-char event)
    (send this on-traverse-char event))
```

```
+------------------------------------+
| [メソッド]                         |
|                                    |
| (send a-dialog show show?) → void? |
| show?: any/c                      |
+------------------------------------+
```

`top-level-window<%>` の `show` をオーバーライドします。

`show?` が真の場合、ダイアログが表示され、イベントスペース内のすべてのフレーム（および他のダイアログ）はダイアログが閉じられるまで無効になります。さらに、メソッドは直ちに戻りません。代わりに、`yield` の呼び出しのあいだにダイアログが非表示であると分かるまで、`yield` でループします。内部セマフォが `yield` とともに使われ、ビジーウェイトを避け、ダイアログが非表示になったらできるだけ早く `show` メソッドが戻るようにします。

`show?` が偽の場合、ダイアログは非表示になり、他のフレームとダイアログは再有効化されます（別の既存ダイアログがまだ表示されている場合を除く）。

```
+--------------------------------------------+
| [メソッド]                                 |
|                                            |
| (send a-dialog show-without-yield) → void? |
+--------------------------------------------+
```

`(send a-dialog show #t)` に似ていますが、yield せずに直ちに戻ります。

---

## editor-admin%

```
+-----------------------------+
| classeditor-admin%: class? |
+-----------------------------+
| superclass: object%         |
+-----------------------------+
```

アドミニストレータの役割については Administrators を参照してください。`editor-admin%` クラスが直接インスタンス化されることはありません。ほとんどのプログラマは派生クラス経由でもインスタンス化しません。各 `editor-canvas%` および `editor-snip%` オブジェクトが自身のアドミニストレータを生成します。ただし、新しい文脈でエディタを表示するためにこのクラスの新しいインスタンスを派生させると有用な場合があります。また、所有するエディタから既存のアドミニストレータのメソッドを呼ぶことも有用な場合があります。

新しい `editor-admin%` クラスを作るには、ここで述べるすべてのメソッドをオーバーライドしなければなりません。それらはすべてアドミニストレータのエディタから呼び出されます。

```
+-----------------------------------------------+
| [コンストラクタ]                              |
|                                               |
| (new editor-admin%) → (is-a?/c editor-admin%) |
+-----------------------------------------------+
```

（役に立たない）エディタアドミニストレータを生成します。

```
+-----------------------------------------------------------------+
| [メソッド]                                                      |
|                                                                 |
| (send an-editor-admin get-dc [x y]) → (or/c (is-a?/c dc<%>) #f) |
| x: (or/c (box/c real?) #f) = #f                                |
| y: (or/c (box/c real?) #f) = #f                                |
+-----------------------------------------------------------------+
```

仕様:
エディタが表示されている描画コンテキスト、または現在描画されているコンテキストを返します。エディタが埋め込まれていないとき、返されるコンテキストは常にエディタが表示されている描画コンテキストです。エディタが表示されていない場合は `#f` が返されます。

描画コンテキストの原点も、エディタのローカル座標に変換されて返されます。埋め込みエディタでは、返される原点が信頼できるのは、エディタが描画されているあいだ、またはマウス／キーボードイベントを受け取っているあいだだけです。

`x` が `#f` でない限り、`x` ボックスにはエディタ座標での DC の x 原点が格納されます。
`y` が `#f` でない限り、`y` ボックスにはエディタ座標での DC の y 原点が格納されます。

`editor<%>` の `editor-location-to-dc-location` および `dc-location-to-editor-location` も参照してください。

既定の実装:
すべてのボックスに `0.0` を入れ、`#f` を返します。

```
+-------------------------------------------------------+
| [メソッド]                                            |
|                                                       |
| (send an-editor-admin get-max-view                    |
| x: (or/c (box/c real?) #f)                           |
| y: (or/c (box/c real?) #f)                           |
| w: (or/c (box/c (and/c real? (not/c negative?))) #f) |
| h: (or/c (box/c (and/c real? (not/c negative?))) #f) |
| full?: any/c = #f                                    |
+-------------------------------------------------------+
```

仕様:
エディタが複数の標準ディスプレイで可視でない限り、`get-view` と同じです。エディタが複数のディスプレイを持つ場合、すべてのディスプレイでの可視領域を含む領域が計算されます。

`get-view` を参照してください。

既定の実装:
すべてのボックスに `0.0` を入れます。

```
+---------------------------------------------------------+
| [メソッド]                                              |
|                                                         |
| (send an-editor-admin get-view x y w h [full?]) → void? |
| x: (or/c (box/c real?) #f)                             |
| y: (or/c (box/c real?) #f)                             |
| w: (or/c (box/c (and/c real? (not/c negative?))) #f)   |
| h: (or/c (box/c (and/c real? (not/c negative?))) #f)   |
| full?: any/c = #f                                      |
+---------------------------------------------------------+
```

仕様:
ディスプレイ内でのエディタの可視領域（エディタ座標）を取得するか、あるいはエディタのトップレベルディスプレイにおける表示領域全体のサイズを取得します（埋め込みエディタの場合）。

ディスプレイがエディタキャンバスの場合は `reflow-container` も参照してください。エディタキャンバス内の表示領域は、キャンバスのクライアント領域全体ではありません。エディタキャンバスはクライアント領域内の表示エディタの周囲に余白の枠を入れるためです。

エディタの可視領域の計算は、トップレベルディスプレイの現在のサイズとスクロールバー値に基づきます。エディタキャンバスディスプレイでは、`get-view` が報告する領域は、キャンバスが非表示か、他のウィンドウに隠れているか、画面端からはみ出しているかには依存しません。

`x` が `#f` でない限り、`x` ボックスにはエディタ座標での可視領域の左端が格納されます。
`y` が `#f` でない限り、`y` ボックスにはエディタ座標での可視領域の上端が格納されます。
`w` が `#f` でない限り、`w` ボックスには可視領域の幅が格納されます（エディタ自体より大きくなり得ます）。
`h` が `#f` でない限り、`h` ボックスには可視領域の高さが格納されます（エディタ自体より大きくなり得ます）。

エディタが完全に可視で `full?` が `#f` の場合、`x` と `y` の両方に `0` が入ります。

`full?` が真の場合、返される領域はエディタのトップレベルディスプレイのビュー領域です。この結果が異なるのは、エディタが別のエディタに埋め込まれているときだけです。その場合、`x` と `y` の値は意味を持たないことがあります。トップレベルディスプレイ内の直接のエディタの座標系にあるためです。

既定の実装:
すべてのボックスに `0.0` を入れます。

```
+-------------------------------------------------------+
| [メソッド]                                            |
|                                                       |
| (send an-editor-admin grab-caret [domain]) → void?    |
| domain: (or/c 'immediate 'display 'global) = 'global |
+-------------------------------------------------------+
```

仕様:
エディタがキーボードフォーカスを要求するために呼びます。要求が認められると、管理下のエディタの `own-caret` メソッドが呼ばれます。

`domain` の取り得る値については `set-caret-owner` を参照してください。

既定の実装:
何もしません。

```
+---------------------------------------------------+
| [メソッド]                                        |
|                                                   |
| (send an-editor-admin modified modified?) → void? |
| modified?: any/c                                 |
+---------------------------------------------------+
```

仕様:
エディタが、自身の変更状態が変更済みまたは未変更に変わったことを報告するために呼びます。

`editor<%>` の `set-modified` も参照してください。

既定の実装:
何もしません。

```
+-------------------------------------+
| [メソッド]                          |
|                                     |
| (send an-editor-admin needs-update  |
| localx: real?                      |
| localy: real?                      |
| w: (and/c real? (not/c negative?)) |
| h: (and/c real? (not/c negative?)) |
+-------------------------------------+
```

仕様:
エディタが、表示中の表現の再描画を要求するために呼びます。アドミニストレータが表示の再描画が必要と判断すると、エディタの `refresh` メソッドを呼びます。

`localx`、`localy`、`w`、`h` 引数は、更新するエディタの領域を指定します（エディタ座標）。

既定の実装:
何もしません。

```
+-------------------------------------------------------+
| [メソッド]                                            |
|                                                       |
| (send an-editor-admin popup-menu menu x y) → boolean? |
| menu: (is-a?/c popup-menu%)                          |
| x: real?                                             |
| y: real?                                             |
+-------------------------------------------------------+
```

仕様:

与えられた `popup-menu%` オブジェクトを指定座標（このウィンドウの座標）でポップアップし、不特定数のイベントを処理した後に戻ります。このメソッドが戻る時点でもメニューはポップアップされたままのことがあります。ポップアップメニューからメニュー項目が選択されると、そのメニュー項目のコールバックが呼ばれます（メニュー項目のコールバックのイベントスペースは、アドミニストレータのディスプレイのイベントスペースです）。

メニューがポップアップされているあいだ、そのターゲットはこのアドミニストレータのディスプレイ内のトップレベルエディタに設定されます。詳細は `get-popup-target` を参照してください。

結果は、この admin がキャンバスに接続されていない、または接続先のキャンバスがエディタを持たない場合は `#f`、それ以外は `#t` です（ユーザがポップアップメニューの項目を選ぶかどうかには依存しません）。

メニューはエディタ座標の `x` と `y` に表示されます。

既定の実装:
`#f` を返します。

```
+----------------------------------------------------+
| [メソッド]                                         |
|                                                    |
| (send an-editor-admin refresh-delayed?) → boolean? |
+----------------------------------------------------+
```

仕様:
このアドミニストレータのディスプレイでの更新が現在遅延されている場合に `#t` を返します（通常は外側のエディタにおける `editor<%>` の `begin-edit-sequence` による）。

既定の実装:
`#f` を返します。

```
+-------------------------------------------------+
| [メソッド]                                      |
|                                                 |
| (send an-editor-admin resized refresh?) → void? |
| refresh?: any/c                                |
+-------------------------------------------------+
```

仕様:
エディタが、サイズまたはスクロール回数が変わったことをディスプレイに通知するために呼びます。スクロールバーを新しいサイズに合わせて調整する必要があります。リサイズ後、エディタは一般に更新が必要ですが、更新を直ちに行うかどうかはエディタが決めます。`refresh?` が `#f` でない場合、エディタは直ちに更新するよう要求しています。

既定の実装:
何もしません。

```
+-----------------------------------------+
| [メソッド]                              |
|                                         |
| (send an-editor-admin scroll-to         |
| localx: real?                          |
| localy: real?                          |
| w: (and/c real? (not/c negative?))     |
| h: (and/c real? (not/c negative?))     |
| refresh?: any/c = #t                   |
| bias: (or/c 'start 'end 'none) = 'none |
+-----------------------------------------+
```

仕様:
与えられた領域が見えるようにスクロールするようエディタが要求するために呼びます。スクロール後、エディタは一般に更新が必要ですが、更新を直ちに行うかどうかはエディタが決めます。

`localx`、`localy`、`w`、`h` 引数は、スクロールによって可視にするエディタの領域を指定します（エディタ座標）。

`refresh?` が `#f` でない場合、エディタは直ちに更新するよう要求しています。

`bias` 引数は次のいずれかです。

- `'start` — 範囲が可視領域に収まらない場合、左上領域を表示する
- `'none` — 特別なスクロール指示なし
- `'end` — 範囲が可視領域に収まらない場合、右下領域を表示する

戻り値は、ディスプレイがスクロールされた場合は `#t`、そうでない場合は `#f` です（要求領域がすでに可視、ディスプレイのサイズがゼロ、またはエディタが現在印刷中、のいずれか）。

エディタが複数のディスプレイを持つ場合、いずれかのディスプレイが現在キーボードフォーカスを持っていればそれがスクロールされます。そうでなければ、エディタの「主所有者」（`call-as-primary-owner` を参照）がスクロールされます。

既定の実装:
`#f` を返します。

```
+----------------------------------------------+
| [メソッド]                                   |
|                                              |
| (send an-editor-admin update-cursor) → void? |
+----------------------------------------------+
```

仕様:
このエディタのディスプレイのカーソル更新をキューに入れます。実際に使われるカーソルは、エディタの `adjust-cursor` メソッドを呼んで決まります。

既定の実装:
何もしません。

---

## editor-canvas%

> [image: editor-canvas.png]
```
  +---------------------------+
  |  エディタ内容の表示領域   |
  |  (text% / pasteboard%)   |
  +---------------------------+
```

```
+------------------------------+-----------+
| classeditor-canvas%: class? |           |
+------------------------------+-----------+
| superclass: object%          |           |
| extends:                     | canvas<%> |
+------------------------------+-----------+
```

`editor-canvas%` オブジェクトは、`text%` または `pasteboard%` オブジェクトを管理・表示します。

```
+-----------------------------------------------------------------------------+
| [コンストラクタ]                                                            |
|                                                                             |
| (new editor-canvas%                                                         |
| → (is-a?/c editor-canvas%)                                                  |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c |
| pane%))                                                                     |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                    |
| (is-a?/c panel%) (is-a?/c pane%))                                           |
| editor: (or/c (or/c (is-a?/c text%) (is-a?/c pasteboard%)) #f) = #f        |
| style: (listof (or/c 'no-border 'control-border 'combo 'no-hscroll         |
| 'no-vscroll 'hide-hscroll 'hide-vscroll 'auto-vscroll 'auto-hscroll         |
| 'resize-corner 'no-focus 'deleted 'transparent)) = null                     |
| (listof (or/c 'no-border 'control-border 'combo                             |
| 'no-hscroll 'no-vscroll                                                     |
| 'hide-hscroll 'hide-vscroll                                                 |
| 'auto-vscroll 'auto-hscroll                                                 |
| 'resize-corner 'no-focus 'deleted                                           |
| 'transparent))                                                              |
| scrolls-per-page: (integer-in 1 10000) = 100                               |
| label: (or/c label-string? #f) = #f                                        |
| wheel-step: (or/c (integer-in 1 10000) #f) = 3                             |
| line-count: (or/c (integer-in 1 1000) #f) = #f                             |
| horizontal-inset: spacing-integer? = 5                                     |
| vertical-inset: spacing-integer? = 5                                       |
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
| (listof (or/c 'no-border 'control-border 'combo                             |
|               'no-hscroll 'no-vscroll                                       |
|               'hide-hscroll 'hide-vscroll                                   |
|               'auto-vscroll 'auto-hscroll                                   |
|               'resize-corner 'no-focus 'deleted                             |
|               'transparent))                                                |
| ```                                                                         |
+-----------------------------------------------------------------------------+
```

キャンバスが `editor` として `#f` で初期化された場合は、後から `set-editor` でエディタをインストールしてください。

`style` リストには次のフラグを含められます。

- `'no-border` — キャンバス周囲の枠線を省略する
- `'control-border` — `text-field%` コントロールに似た枠線を付ける
- `'combo` — `combo-field%` コントロールに似たコンボボタンを付ける。このスタイルは `'control-border`、`'hide-hscroll`、`'hide-vscroll` と組み合わせて使う意図である
- `'no-hscroll` — 水平スクロールを禁止し、水平スクロールバーを隠す
- `'no-vscroll` — 垂直スクロールを禁止し、垂直スクロールバーを隠す
- `'hide-hscroll` — 水平スクロールは許すが、水平スクロールバーを隠す
- `'hide-vscroll` — 垂直スクロールは許すが、垂直スクロールバーを隠す
- `'auto-hscroll` — 不要なとき水平スクロールバーを自動で隠す（`'no-hscroll` または `'hide-hscroll` が指定されていない場合）
- `'auto-vscroll` — 不要なとき垂直スクロールバーを自動で隠す（`'no-vscroll` または `'hide-vscroll` が指定されていない場合）
- `'resize-corner` — スクロールバーが一方だけ表示されているとき、キャンバス右下にリサイズコントロール用の余白を残す
- `'no-focus` — キャンバスがクリックされたときや `focus` メソッドが呼ばれたときに、キーボードフォーカスを受け取らないようにする
- `'deleted` — キャンバスを初期状態で非表示として生成し、親のジオメトリに影響しない。後から親の `add-child` メソッドを呼んで有効にできる
- `'transparent` — 更新前に親ウィンドウの背景を使ってキャンバスを「消去」する。`'transparent` とオフスクリーンバッファリングの相互作用については `canvas<%>` を参照

テキストエディタの垂直スクロールは行に基づきますが、水平スクロールおよびペーストボードの垂直スクロールは、水平ページあたりの固定ステップ数に基づきます。`scrolls-per-page` 引数がこの値を設定します。

与えられた場合、`wheel-step` 引数は `wheel-step` メソッドに渡されます。既定のホイールステップは `'GRacket:wheelStep` 環境設定で大域的に上書きできます。Preferences を参照してください。

`line-count` が `#f` でない場合、`set-line-count` メソッドに渡されます。

`horizontal-inset` が `5` でない場合、`horizontal-inset` メソッドに渡されます。同様に、`vertical-inset` が `5` でない場合、`vertical-inset` メソッドに渡されます。

`enabled` 引数については `window<%>` を参照してください。`horiz-margin` と `vert-margin` については `subarea<%>` を、`min-width`、`min-height`、`stretchable-width`、`stretchable-height` については `area<%>` を参照してください。

```
+----------------------------------------------------------+
| [メソッド]                                               |
|                                                          |
| (send an-editor-canvas allow-scroll-to-last) → boolean?  |
| (send an-editor-canvas allow-scroll-to-last on?) → void? |
| on?: any/c                                              |
+----------------------------------------------------------+
```

最終行スクロールを有効または無効にするか、現在の有効状態を取得します。最終行スクロールが有効な場合、このキャンバスに表示されたエディタは、テキストの最終行がキャンバスの上端に来るまでスクロールできます（下端基準スクロールが有効な場合は下端。`scroll-with-bottom-base` を参照）。既定では、最終行がキャンバスの下端（または上端）に来るまでしかスクロールできません。

```
+----------------------------------------------------+
| [メソッド]                                         |
|                                                    |
| (send an-editor-canvas allow-tab-exit) → boolean?  |
| (send an-editor-canvas allow-tab-exit on?) → void? |
| on?: any/c                                        |
+----------------------------------------------------+
```

エディタキャンバスのタブ終了が有効かどうかを取得または設定します。タブ終了が有効なとき、ユーザは Tab キーと矢印キーでエディタからキーボードフォーカスを外し、Enter/Return キーで既定ボタンを起動し、Escape でダイアログのクローズ動作を起動できます。既定ではタブ終了は無効です。

エディタキャンバスでタブ終了が有効な場合、Tab と Enter のキーボードイベントはフレームの既定の `on-traverse-char` メソッドに消費されます。加えて、ダイアログの既定メソッドは Escape キーイベントを消費します。それ以外の場合、`on-traverse-char` はキーボードイベントをキャンバスへ伝播させます。

```
+-------------------------------------------------------+
| [メソッド]                                            |
|                                                       |
| (send an-editor-canvas call-as-primary-owner f) → any |
| f: (-> any)                                          |
+-------------------------------------------------------+
```

thunk を呼び出してその値を返します。thunk が呼ばれているあいだ、キャンバスがエディタを持つ場合、エディタの `get-admin` メソッドはこのキャンバスのアドミニストレータを返します。このメソッドが有用なのは、エディタが複数のキャンバスに表示されているときだけです。

```
+---------------------------------------------------------+
| [メソッド]                                              |
|                                                         |
| (send an-editor-canvas force-display-focus) → boolean?  |
| (send an-editor-canvas force-display-focus on?) → void? |
| on?: any/c                                             |
+---------------------------------------------------------+
```

強制フォーカスモードを有効または無効にします。強制フォーカスモードでは、キャンバスがキーボードフォーカスを持っていなくても、このキャンバスに表示されたエディタのキャレットまたは選択が描画されます。

```
+----------------------------------------------------------+
| [メソッド]                                               |
|                                                          |
| (send an-editor-canvas get-editor)                       |
| → (or/c (or/c (is-a?/c text%) (is-a?/c pasteboard%)) #f) |
+----------------------------------------------------------+
```

このキャンバスが現在表示しているエディタを返します。エディタを持たない場合は `#f` です。

```
+----------------------------------------+
| [メソッド]                             |
|                                        |
| (send an-editor-canvas get-line-count) |
| → (or/c (integer-in 1 1000) #f)        |
+----------------------------------------+
```

`set-line-count` で設定した行数を返します。最小行数が設定されていない場合は `#f` です。

```
+--------------------------------------------------------+
| [メソッド]                                             |
|                                                        |
| (send an-editor-canvas get-scroll-via-copy) → boolean? |
+--------------------------------------------------------+
```

スクロールがエディタ内容のコピー（および新たに露出した内容の再描画）を引き起こす場合は `#t` を返します。スクロールがエディタキャンバス全体の再描画を引き起こす場合は `#f` を返します。既定は `#f` です。

`on-scroll-to` および `after-scroll-to` も参照してください。

```
+-------------------------------------------------------+
| [メソッド]                                            |
|                                                       |
| (send an-editor-canvas horizontal-inset)              |
| → (integer-in 1 10000)                                |
| (send an-editor-canvas horizontal-inset step) → void? |
| step: (integer-in 1 10000)                           |
+-------------------------------------------------------+
```

キャンバス内でエディタ内容の左右に予約されるピクセル数を取得または設定します。既定は `5` です。

```
+--------------------------------------------------+
| [メソッド]                                       |
|                                                  |
| (send an-editor-canvas lazy-refresh) → boolean?  |
| (send an-editor-canvas lazy-refresh on?) → void? |
| on?: any/c                                      |
+--------------------------------------------------+
```

遅延再描画モードを有効または無効にするか、現在の有効状態を取得します。遅延再描画モードでは、ウィンドウの更新が必要なときに `on-paint` ではなくキャンバスの `refresh` メソッドが呼ばれます。既定では、`editor-canvas%` オブジェクトは遅延再描画モードではありません。

```
+-----------------------------------------------+
| [メソッド]                                    |
|                                               |
| (send an-editor-canvas on-char event) → void? |
| event: (is-a?/c key-event%)                  |
+-----------------------------------------------+
```

`canvas<%>` の `on-char` をオーバーライドします。

`'wheel-up` と `'wheel-down` イベントは垂直スクロールで処理します。それ以外は、あればキャンバスのエディタの `on-char` メソッドにイベントを渡します。

`get-editor` も参照してください。

```
+------------------------------------------------+
| [メソッド]                                     |
|                                                |
| (send an-editor-canvas on-event event) → void? |
| event: (is-a?/c mouse-event%)                 |
+------------------------------------------------+
```

`canvas<%>` の `on-event` をオーバーライドします。

あればキャンバスのエディタの `on-event` メソッドにイベントを渡します。

`get-editor` も参照してください。

```
+----------------------------------------------+
| [メソッド]                                   |
|                                              |
| (send an-editor-canvas on-focus on?) → void? |
| on?: any/c                                  |
+----------------------------------------------+
```

`window<%>` の `on-focus` をオーバーライドします。

ディスプレイのエディタ（あれば）のキャレットを有効または無効にします。

```
+------------------------------------------+
| [メソッド]                               |
|                                          |
| (send an-editor-canvas on-paint) → void? |
+------------------------------------------+
```

`canvas<%>` の `on-paint` をオーバーライドします。

エディタを再描画するか、エディタが表示されていない場合はキャンバスをクリアします。

このメソッドは、キャンバスが `'transparent` スタイルで生成されていない限り、エディタ周囲のマージンをクリアした後に呼ばれますが、エディタ領域自体は自動ではクリアされません。言い換えると、`editor-canvas%` の既定の更新は、`'no-autoclear` スタイルの `canvas%` 更新に似ています。ただしエディタ領域周囲のマージンは常にクリアされます。

```
+--------------------------------+
| [メソッド]                     |
|                                |
| (send an-editor-canvas on-size |
| width: dimension-integer?     |
| height: dimension-integer?    |
+--------------------------------+
```

`window<%>` の `on-size` をオーバーライドします。

キャンバスがエディタを表示している場合、その `on-display-size` メソッドが呼ばれます。

```
+-----------------------------------------+
| [メソッド]                              |
|                                         |
| (send an-editor-canvas scroll-to        |
| localx: real?                          |
| localy: real?                          |
| w: (and/c real? (not/c negative?))     |
| h: (and/c real? (not/c negative?))     |
| refresh?: any/c                        |
| bias: (or/c 'start 'end 'none) = 'none |
+-----------------------------------------+
```

現在表示中のエディタ内の与えられた領域が可視になるようスクロールを要求します。

`localx`、`localy`、`w`、`h` 引数は、スクロールによって可視にするエディタの領域を指定します（エディタ座標）。

`refresh?` が `#f` でない場合、スクロール成功後にエディタは直ちに更新されます。

`bias` 引数は次のいずれかです。

- `'start` — 範囲が可視領域に収まらない場合、左上領域を表示する
- `'none` — 特別なスクロール指示なし
- `'end` — 範囲が可視領域に収まらない場合、右下領域を表示する

戻り値は、ディスプレイがスクロールされた場合は `#t`、そうでない場合は `#f` です（要求領域がすでに可視、ディスプレイのサイズがゼロ、またはエディタが現在印刷中、のいずれか）。

```
+-------------------------------------------------------------+
| [メソッド]                                                  |
|                                                             |
| (send an-editor-canvas scroll-with-bottom-base) → boolean?  |
| (send an-editor-canvas scroll-with-bottom-base on?) → void? |
| on?: any/c                                                 |
+-------------------------------------------------------------+
```

下端基準スクロールを有効または無効にするか、現在の有効状態を取得します。下端基準スクロールがオンの場合、スクロール位置は表示可能領域の上端ではなく下端に揃えた行境界で決まります。最終行スクロールも有効な場合（`allow-scroll-to-last` を参照）、エディタが表示可能領域を埋めなくても、表示領域内で下端揃えになります。

```
+---------------------------------------------------------------+
| [メソッド]                                                    |
|                                                               |
| (send an-editor-canvas set-editor                             |
| edit: (or/c (or/c (is-a?/c text%) (is-a?/c pasteboard%)) #f) |
| redraw?: any/c = #t                                          |
+---------------------------------------------------------------+
```

キャンバスが表示するエディタを設定し、現在のエディタ（あれば）を解放します。新しいエディタがすでに `editor-canvas%` に関連しないアドミニストレータを持つ場合、新しいエディタはキャンバスにインストールされません。

`redraw?` が `#f` の場合、エディタは直ちに描画されません。この場合、後で再描画を強制するものが必要です（例: `on-paint` メソッドの呼び出し）。

キャンバスに `set-line-count` で行数が設定されている場合、キャンバスの最小高さが調整されます。

```
+------------------------------------------------------+
| [メソッド]                                           |
|                                                      |
| (send an-editor-canvas set-line-count count) → void? |
| count: (or/c (integer-in 1 1000) #f)                |
+------------------------------------------------------+
```

キャンバスのグラフィカル最小高さを、特定の行数のテキストを表示できる高さに設定します。行の高さは、表示中のエディタの最初の行の上端と下端の差を測って決めます。最小高さは、キャンバスがエディタを得るまで変更されません。キャンバスのエディタが変わると、最小高さは再計算されます。

行数が `#f` に設定された場合、キャンバスのグラフィカル最小高さは元の値に戻ります。

```
+--------------------------------------------------------------+
| [メソッド]                                                   |
|                                                              |
| (send an-editor-canvas set-scroll-via-copy scroll-via-copy?) |
| → void?                                                      |
| scroll-via-copy?: any/c                                     |
+--------------------------------------------------------------+
```

スクロール時の再描画モードを変更します。`get-scroll-via-copy` も参照してください。

```
+---------------------------------------------------------------+
| [メソッド]                                                    |
|                                                               |
| (send an-editor-canvas vertical-inset) → (integer-in 1 10000) |
| (send an-editor-canvas vertical-inset step) → void?           |
| step: (integer-in 1 10000)                                   |
+---------------------------------------------------------------+
```

キャンバス内でエディタ内容の上下に予約されるピクセル数を取得または設定します。既定は `5` です。

```
+-------------------------------------------------+
| [メソッド]                                      |
|                                                 |
| (send an-editor-canvas wheel-step)              |
| → (or/c (integer-in 1 10000) #f)                |
| (send an-editor-canvas wheel-step step) → void? |
| step: (or/c (integer-in 1 10000) #f)           |
+-------------------------------------------------+
```

`'wheel-up` または `'wheel-down` の `key-event%` によるマウスホイール 1 クリックあたりの垂直スクロールステップ数を取得または設定します。`#f` の値はホイールイベントの特別扱いを無効にします（すなわち、ホイールイベントはキャンバスのエディタに渡されます）。
