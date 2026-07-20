# 付録：GUI クラス参照（56–65）

**原本範囲:** `original_markdown_56` … `original_markdown_65`  
**対象:** `image-snip%` … `menu-item<%>`  
**原本ディレクトリ:** `extracted/appendix/gui/`

コード、メソッド名、契約、シグネチャは原文のままです。クラス名も英語のままです。

---

## image-snip%

```
+---------------------------+
| classimage-snip%: class? |
+---------------------------+
| superclass: snip%         |
+---------------------------+
```

`image-snip%` はビットマップ画像（通常はファイルから読み込み）を表示できるスニップです。画像ファイルが見つからない場合、「X」入りの箱が描画されます。

```
+------------------------------------------------------------------------------+
| [constructor]                                                                |
|                                                                              |
| (make-object image-snip%                                                     |
| → (is-a?/c image-snip%)                                                      |
| file: (or/c path-string? input-port? #f) = #f                               |
| kind: (or/c 'unknown 'unknown/mask 'unknown/alpha 'gif 'gif/mask 'gif/alpha |
| 'jpeg 'png 'png/mask 'png/alpha 'xbm 'xpm 'bmp 'pict) = 'unknown             |
| (or/c 'unknown 'unknown/mask 'unknown/alpha                                  |
| 'gif 'gif/mask 'gif/alpha                                                    |
| 'jpeg 'png 'png/mask 'png/alpha                                              |
| 'xbm 'xpm 'bmp 'pict)                                                        |
| relative-path?: any/c = #f                                                  |
| inline?: any/c = #t                                                         |
| backing-scale: (>/c 0.0) = 1.0                                              |
| (make-object image-snip% bitmap [mask]) → (is-a?/c image-snip%)              |
| bitmap: (is-a?/c bitmap%)                                                   |
| mask: (or/c (is-a?/c bitmap%) #f) = #f                                      |
|                                                                              |
| ```racket                                                                    |
| (or/c 'unknown 'unknown/mask 'unknown/alpha                                  |
|       'gif 'gif/mask 'gif/alpha                                              |
|       'jpeg 'png 'png/mask 'png/alpha                                        |
|       'xbm 'xpm 'bmp 'pict)                                                  |
| ```                                                                          |
+------------------------------------------------------------------------------+
```

画像スニップを作成します。指定があれば画像ファイルを読み込むか（load-file も参照）、与えられたビットマップを使います。

Changed in version 1.1 of package `snip-lib`: Added the backing-scale argument.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send an-image-snip equal-hash-code-of hash-code) |
| → exact-integer?                                  |
| hash-code: (any/c. ->. exact-integer?)         |
+---------------------------------------------------+
```

an-image-snip の equal? ベースのハッシュコードとして使える整数を返します（other-equal-to? と同じ equal? の概念）。

equal<%> も参照してください。

```
+-------------------------------------------------------------+
| [method]                                                    |
|                                                             |
| (send an-image-snip equal-secondary-hash-code-of hash-code) |
| → exact-integer?                                            |
| hash-code: (any/c. ->. exact-integer?)                   |
+-------------------------------------------------------------+
```

an-image-snip の equal? ベースの二次ハッシュコードとして使える整数を返します（other-equal-to? と同じ equal? の概念）。

equal<%> も参照してください。

```
+---------------------------------------------------------------+
| [method]                                                      |
|                                                               |
| (send an-image-snip get-bitmap) → (or/c (is-a?/c bitmap%) #f) |
+---------------------------------------------------------------+
```

set-bitmap または load-file で設定された、スニップが表示するビットマップを返します。表示するビットマップがなければ #f です。

```
+--------------------------------------+
| [method]                             |
|                                      |
| (send an-image-snip get-bitmap-mask) |
| → (or/c (is-a?/c bitmap%) #f)        |
+--------------------------------------+
```

set-bitmap でインストールされた場合にスニップ表示で使うマスクビットマップを返します。マスクがなければ #f です。

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send an-image-snip get-filename [relative-path]) |
| → (or/c path-string? #f)                          |
| relative-path: (or/c (box/c any/c) #f) = #f      |
+---------------------------------------------------+
```

現在読み込まれている非インラインファイルの名前を返します。ファイルが読み込まれていない、またはインライン（既定）で読み込まれた場合は #f です。

relative-path が #f でなければ、読み込まれたファイルのパスが所有エディタのパスからの相対なら relative-path ボックスに #t が入ります。

```
+-------------------------------------------------------------------------------+
| [method]                                                                      |
|                                                                               |
| (send an-image-snip get-filetype)                                             |
| → (or/c 'unknown 'unknown/mask 'unknown/alpha 'gif 'gif/mask 'gif/alpha 'jpeg |
| 'png 'png/mask 'png/alpha 'xbm 'xpm 'bmp 'pict)                               |
| (or/c 'unknown 'unknown/mask 'unknown/alpha                                   |
| 'gif 'gif/mask 'gif/alpha                                                     |
| 'jpeg 'png 'png/mask 'png/alpha                                               |
| 'xbm 'xpm 'bmp 'pict)                                                         |
|                                                                               |
| ```racket                                                                     |
| (or/c 'unknown 'unknown/mask 'unknown/alpha                                   |
|       'gif 'gif/mask 'gif/alpha                                               |
|       'jpeg 'png 'png/mask 'png/alpha                                         |
|       'xbm 'xpm 'bmp 'pict)                                                   |
| ```                                                                           |
+-------------------------------------------------------------------------------+
```

現在読み込まれている非インラインファイルの読み込みに使った kind を返します。ファイルが読み込まれていない、またはインラインで読み込まれた場合は 'unknown です。

```
+------------------------------------------------------------------------------+
| [method]                                                                     |
|                                                                              |
| (send an-image-snip load-file                                                |
| file: (or/c path-string? input-port? #f)                                    |
| kind: (or/c 'unknown 'unknown/mask 'unknown/alpha 'gif 'gif/mask 'gif/alpha |
| 'jpeg 'png 'png/mask 'png/alpha 'xbm 'xpm 'bmp 'pict) = 'unknown             |
| (or/c 'unknown 'unknown/mask 'unknown/alpha                                  |
| 'gif 'gif/mask 'gif/alpha                                                    |
| 'jpeg 'png 'png/mask 'png/alpha                                              |
| 'xbm 'xpm 'bmp 'pict)                                                        |
| relative-path?: any/c = #f                                                  |
| inline?: any/c = #t                                                         |
| backing-scale: (>/c 0.0) = 1.0                                              |
|                                                                              |
| ```racket                                                                    |
| (or/c 'unknown 'unknown/mask 'unknown/alpha                                  |
|       'gif 'gif/mask 'gif/alpha                                              |
|       'jpeg 'png 'png/mask 'png/alpha                                        |
|       'xbm 'xpm 'bmp 'pict)                                                  |
| ```                                                                          |
+------------------------------------------------------------------------------+
```

file と kind を bitmap% の load-file に渡してファイルを読み込みます。以前 set-bitmap でビットマップが指定されていた場合、そのビットマップ（とマスク）はもう使われません。file が #f なら、現在の画像は削除されます。

'unknown/mask、'gif/mask、または 'png/mask が指定され、読み込んだビットマップオブジェクトにマスクが含まれる（get-loaded-mask を参照）場合、そのマスクがビットマップ描画に使われます（draw-bitmap を参照）。'unknown/alpha、'gif/alpha、'png/alpha も同様にアルファチャンネルを使います。

relative-path? が #f でなく file が相対パスなら、所有エディタのファイル名のパスを使ってファイルが読まれます。画像がインラインでなければ、相対パスとして保存されます。

inline? が #f でなければ、画像の保存やコピー時に画像データがファイルまたはクリップボードへ直接保存されます（ビットマップのマスクがあれば保持）。元のファイル名と kind は記憶されません。

Changed in version 1.1 of package `snip-lib`: Added the backing-scale argument.

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send an-image-snip other-equal-to?    |
| snip: (is-a?/c snip%)                 |
| equal?: (any/c any/c. ->. boolean?) |
+----------------------------------------+
```

an-image-snip と snip の両方がビットマップを持ち、かつビットマップが同じなら #t を返します。いずれかがメインビットマップと同じ寸法のマスクビットマップを持つ場合、マスクも同じでなければなりません（または両方ともマスクなし）。

与えられた equal? 関数（再帰比較用）は使われません。

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send an-image-snip resize w h) → boolean? |
| w: (and/c real? (not/c negative?))        |
| h: (and/c real? (not/c negative?))        |
+--------------------------------------------+
```

snip% の resize をオーバーライドします。

ビットマップは与えられた寸法に収まるよう切り抜かれます。

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send an-image-snip set-bitmap bm [mask]) → void? |
| bm: (is-a?/c bitmap%)                            |
| mask: (or/c (is-a?/c bitmap%) #f) = #f           |
+---------------------------------------------------+
```

スニップが表示するビットマップを設定します。

ビットマップ描画時にオプションのマスクが使われます（draw-bitmap を参照）が、マスクを直接渡すのは非推奨です。マスクを渡さなくてもビットマップの get-loaded-mask がビットマップを返せば、それがマスクとして使われます。

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send an-image-snip set-offset dx dy) → void? |
| dx: real?                                    |
| dy: real?                                    |
+-----------------------------------------------+
```

画像スニップ内のビットマップのグラフィカルオフセットを設定します。

---

## key-event%

```
+--------------------------+
| classkey-event%: class? |
+--------------------------+
| superclass: event%       |
+--------------------------+
```

`key-event%` オブジェクトはキー押下または解放イベントに関する情報を含みます。キーイベントは主に window<%> の on-subwindow-char と canvas<%> の on-char によって処理されます。

キー押下イベントでは、仮想キーコードは get-key-code で得られます。キー解放イベントでは get-key-code は 'release を報告し、仮想キーコードは get-key-release-code で得られます。

Mouse and Keyboard Events も参照してください。

```
+--------------------------------------------------+
| [constructor]                                    |
|                                                  |
| (new key-event%                                  |
| → (is-a?/c key-event%)                           |
| key-code: (or/c char? key-code-symbol?) = #\nul |
| shift-down: any/c = #f                          |
| control-down: any/c = #f                        |
| meta-down: any/c = #f                           |
| alt-down: any/c = #f                            |
| x: exact-integer? = 0                           |
| y: exact-integer? = 0                           |
| time-stamp: exact-integer? = 0                  |
| caps-down: any/c = #f                           |
| mod3-down: any/c = #f                           |
| mod4-down: any/c = #f                           |
| mod5-down: any/c = #f                           |
| control+meta-is-altgr: any/c = #f               |
+--------------------------------------------------+
```

the corresponding get- and set- methods for information about key-code, shift-down, control-down, meta-down, mod3-down, mod4-down, mod5-down, alt-down, x, y, time-stamp, caps-down, mod3-down, mod4-down, mod5-down, and control+meta-is-altgr を参照してください。

get-key-release-code が返す解放キーコードは 'press で初期化されます。

Changed in version 1.1 of package `gui-lib`: Added mod3-down, mod4-down, and mod5-down.
Changed in version 1.2: Added control+meta-is-altgr.

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send a-key-event get-alt-down) → boolean? |
+--------------------------------------------+
```

イベント時に Option（Mac OS）キーが押されていれば #t を返します。Windows で Alt キーが押された場合は Meta 押下として報告されます（get-meta-down を参照）。

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-key-event get-caps-down) → boolean? |
+---------------------------------------------+
```

イベント時に Caps Lock がオンなら #t を返します。

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-key-event get-control-down) → boolean? |
+------------------------------------------------+
```

イベント時に Control キーが押されていれば #t を返します。

Mac OS では、Control キー押下とマウスボタンクリックが組み合わさると、イベントは右ボタンクリックとして報告され、そのイベントの get-control-down は #f を報告します。

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send a-key-event get-control+meta-is-altgr) → boolean? |
+---------------------------------------------------------+
```

Control と Meta の組み合わせイベントを Windows で AltGr イベントとして扱うべきなら #t を返します。既定では、Control が左で Alt（Meta として）が右のときに AltGr 扱いが適用されます。

Added in version 1.2 of package `gui-lib`.

```
+---------------------------------+
| [method]                        |
|                                 |
| (send a-key-event get-key-code) |
| → (or/c char? key-code-symbol?) |
+---------------------------------+
```

キーイベントの仮想キーコードを取得します。仮想キーコードは文字、または次の特別キーシンボルのいずれかです。

- 'start
- 'cancel
- 'clear
- 'shift — Shift key
- 'rshift — right Shift key
- 'control — Control key
- 'rcontrol — right Control key
- 'menu
- 'pause
- 'capital
- 'prior
- 'next
- 'end
- 'home
- 'left
- 'up
- 'right
- 'down
- 'escape
- 'select
- 'print
- 'execute
- 'snapshot
- 'insert
- 'help
- 'numpad0
- 'numpad1
- 'numpad2
- 'numpad3
- 'numpad4
- 'numpad5
- 'numpad6
- 'numpad7
- 'numpad8
- 'numpad9
- 'numpad-enter
- 'multiply
- 'add
- 'separator
- 'subtract
- 'decimal
- 'divide
- 'f1
- 'f2
- 'f3
- 'f4
- 'f5
- 'f6
- 'f7
- 'f8
- 'f9
- 'f10
- 'f11
- 'f12
- 'f13
- 'f14
- 'f15
- 'f16
- 'f17
- 'f18
- 'f19
- 'f20
- 'f21
- 'f22
- 'f23
- 'f24
- 'numlock
- 'scroll
- 'wheel-up — mouse wheel up; see get-wheel-steps
- 'wheel-down — mouse wheel down; see get-wheel-steps
- 'wheel-left — mouse wheel left; see get-wheel-steps
- 'wheel-right — mouse wheel right; see get-wheel-steps
- 'release — indicates a key-release event
- 'press — indicates a key-press event; usually only from get-key-release-code

特別キーシンボルは、標準 ASCII 表現を持たない有用なキーを捉えようとします。標準表現があるが自明でないキーもあります。

- #\space — スペースバー
- #\return — Enter または Return キー（全プラットフォーム）。ただしテンキー付近の Enter とは限らない（Unix と Mac OS では 'numpad-enter として報告）
- #\tab — Tab キー
- #\backspace — Backspace キー
- #\rubout — Delete キー

適切な特別キーシンボルまたは ASCII 表現が得られない場合、#\nul（NUL 文字）が報告されます。

'wheel-up、'wheel-down、'wheel-left、'wheel-right イベントは、キーボードフォーカスを持つウィンドウ以外へ送られることがあります。一部のプラットフォームではホイールイベントがキーボードフォーカスではなくマウスポインタ位置に基づいて生成されるためです。

Windows では、Alt なしで Control が押されているとき、ASCII 文字のキーコードは小文字化され、Shift の効果をほぼ打ち消します。Mac OS では、Control または Command が押されているとき Caps Lock の効果なしでキーコードが計算されます。Control の場合、special-control-key で特別扱いを無効にしていれば Caps Lock は通常どおり使われます。Unix では、Alt なしで Control が押されているとき Caps Lock の効果ありでキーコードが計算されます。

get-other-shift-key-code も参照してください。

Changed in version 6.1.0.8 of package `gui-lib`: Changed reporting of numpad Enter
to 'numpad-enter as
documented, instead of
#\u0003.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-key-event get-key-release-code) |
| → (or/c char? key-code-symbol?)         |
+-----------------------------------------+
```

キー解放イベントの仮想キーコードを取得します。キー押下イベントでは結果は 'press です。仮想キーコードの一覧は get-key-code を参照してください。

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-key-event get-meta-down) → boolean? |
+---------------------------------------------+
```

イベント時に Meta（Unix）、Alt（Windows）、または Command（Mac OS）キーが押されていれば #t を返します。

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-key-event get-mod3-down) → boolean? |
+---------------------------------------------+
```

イベント時に Mod3（Unix）キーが押されていれば #t を返します。

Added in version 1.1 of package `gui-lib`.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-key-event get-mod4-down) → boolean? |
+---------------------------------------------+
```

イベント時に Mod4（Unix）キーが押されていれば #t を返します。

Added in version 1.1 of package `gui-lib`.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-key-event get-mod5-down) → boolean? |
+---------------------------------------------+
```

イベント時に Mod5（Unix）キーが押されていれば #t を返します。

Added in version 1.1 of package `gui-lib`.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-key-event get-other-altgr-key-code) |
| → (or/c char? key-code-symbol? #f)          |
+---------------------------------------------+
```

get-other-shift-key-code を参照してください。

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send a-key-event get-other-caps-key-code) |
| → (or/c char? key-code-symbol? #f)         |
+--------------------------------------------+
```

get-other-shift-key-code を参照してください。

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send a-key-event get-other-shift-altgr-key-code) |
| → (or/c char? key-code-symbol? #f)                |
+---------------------------------------------------+
```

get-other-shift-key-code を参照してください。

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-key-event get-other-shift-key-code) |
| → (or/c char? key-code-symbol? #f)          |
+---------------------------------------------+
```

キーボード写像は環境によって異なるため、キーマップでは Shift キーが実際と逆だった場合にキーボードが生成したであろう結果を知ると有用なことがあります。get-other-shift-key-code はその代替写像を生成し、利用できなければ #f、そうでなければ get-key-code と同じ種類の結果を返します。

get-other-altgr-key-code は Windows と Unix の AltGr（Control と組み合わせた Alt）、または Mac OS の Option について同様の情報を提供します。get-other-shift-altgr-key-code は Shift と AltGr/Option の両方が実際のイベントと異なっていた場合の写像を報告します。

get-other-shift-key-code、get-other-altgr-key-code、get-other-shift-altgr-key-code の結果はすべて Caps Lock オフでのキー写像を報告し、実際のイベントで Caps Lock がオンだったかには依存しません。get-other-caps-key-code は、get-key-code の結果とは逆の Caps Lock 状態として扱った場合の写像を報告します（Caps Lock は通常、効果なしか Shift と同じ効果なので、Caps Lock と他修飾キーのさらなる組み合わせは通常これ以上の代替を生みません）。

代替写像がすべてのイベントで利用できるわけではありません。Windows では ASCII 英字・数字・記号を生成するときに代替写像が報告されます。Mac OS と Unix では代替写像は通常利用できます。

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-key-event get-shift-down) → boolean? |
+----------------------------------------------+
```

イベント時に Shift キーが押されていれば #t を返します。

```
+--------------------------------------------------------+
| [method]                                               |
|                                                        |
| (send a-key-event get-wheel-steps) → nonnegative-real? |
+--------------------------------------------------------+
```

'wheel-up、'wheel-down、'wheel-left、'wheel-right イベントが表すホイールステップ数を返します。システム生成イベントではホイールは常に正、他イベントは常に 0.0 です。

wheel-event-mode in window<%> も参照してください。

Added in version 1.43 of package `gui-lib`.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-key-event get-x) → exact-integer? |
+-------------------------------------------+
```

イベント時のマウスの x 位置を、対象ウィンドウの（クライアント領域）座標系で返します。

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-key-event get-y) → exact-integer? |
+-------------------------------------------+
```

イベント時のマウスの y 位置を、対象ウィンドウの（クライアント領域）座標系で返します。

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-key-event set-alt-down down?) → void? |
| down?: any/c                                 |
+-----------------------------------------------+
```

イベント時に Option（Mac OS）キーが押されていたかどうかを設定します。Windows で Alt が押された場合は Meta 押下として報告されます（set-meta-down を参照）。

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-key-event set-caps-down down?) → void? |
| down?: any/c                                  |
+------------------------------------------------+
```

イベント時に Caps Lock がオンだったかどうかを設定します。

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send a-key-event set-control-down down?) → void? |
| down?: any/c                                     |
+---------------------------------------------------+
```

イベント時に Control キーが押されていたかどうかを設定します。

Mac OS では、Control キー押下とマウスボタンクリックが組み合わさると、イベントは右ボタンクリックとして報告され、get-control-down は #f を報告します。

```
+------------------------------------------------------------+
| [method]                                                   |
|                                                            |
| (send a-key-event set-control+meta-is-altgr down?) → void? |
| down?: any/c                                              |
+------------------------------------------------------------+
```

Windows で Control と Meta の組み合わせを AltGr 組み合わせとして扱うかどうかを設定します。get-control+meta-is-altgr を参照してください。

Added in version 1.2 of package `gui-lib`.

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-key-event set-key-code code) → void? |
| code: (or/c char? key-code-symbol?)         |
+----------------------------------------------+
```

イベントの仮想キーコードを設定します。文字、または get-key-code に列挙される特別シンボルのいずれかです。

```
+------------------------------------------------------+
| [method]                                             |
|                                                      |
| (send a-key-event set-key-release-code code) → void? |
| code: (or/c char? key-code-symbol?)                 |
+------------------------------------------------------+
```

解放イベントの仮想キーコードを設定します。文字、または get-key-code に列挙される特別シンボルのいずれかです。get-key-release-code も参照してください。

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-key-event set-meta-down down?) → void? |
| down?: any/c                                  |
+------------------------------------------------+
```

イベント時に Meta（Unix）、Alt（Windows）、または Command（Mac OS）キーが押されていたかどうかを設定します。

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-key-event set-mod3-down down?) → void? |
| down?: any/c                                  |
+------------------------------------------------+
```

イベント時に Mod3（Unix）キーが押されていたかどうかを設定します。

Added in version 1.1 of package `gui-lib`.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-key-event set-mod4-down down?) → void? |
| down?: any/c                                  |
+------------------------------------------------+
```

イベント時に Mod4（Unix）キーが押されていたかどうかを設定します。

Added in version 1.1 of package `gui-lib`.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-key-event set-mod5-down down?) → void? |
| down?: any/c                                  |
+------------------------------------------------+
```

イベント時に Mod5（Unix）キーが押されていたかどうかを設定します。

Added in version 1.1 of package `gui-lib`.

```
+----------------------------------------------------------+
| [method]                                                 |
|                                                          |
| (send a-key-event set-other-altgr-key-code code) → void? |
| code: (or/c char? key-code-symbol? #f)                  |
+----------------------------------------------------------+
```

key code produced by get-other-altgr-key-code を設定します。

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send a-key-event set-other-caps-key-code code) → void? |
| code: (or/c char? key-code-symbol? #f)                 |
+---------------------------------------------------------+
```

key code produced by get-other-caps-key-code を設定します。

```
+----------------------------------------------------------------+
| [method]                                                       |
|                                                                |
| (send a-key-event set-other-shift-altgr-key-code code) → void? |
| code: (or/c char? key-code-symbol? #f)                        |
+----------------------------------------------------------------+
```

key code produced by get-other-shift-altgr-key-code を設定します。

```
+----------------------------------------------------------+
| [method]                                                 |
|                                                          |
| (send a-key-event set-other-shift-key-code code) → void? |
| code: (or/c char? key-code-symbol? #f)                  |
+----------------------------------------------------------+
```

key code produced by get-other-shift-key-code を設定します。

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-key-event set-shift-down down?) → void? |
| down?: any/c                                   |
+-------------------------------------------------+
```

イベント時に Shift キーが押されていたかどうかを設定します。

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-key-event set-wheel-steps steps) → void? |
| steps: nonnegative-real?                        |
+--------------------------------------------------+
```

ホイールイベントのステップ数を設定します。get-wheel-steps を参照してください。

Added in version 1.43 of package `gui-lib`.

```
+--------------------------------------+
| [method]                             |
|                                      |
| (send a-key-event set-x pos) → void? |
| pos: exact-integer?                 |
+--------------------------------------+
```

イベント時のマウスの x 位置を、対象ウィンドウの（クライアント領域）座標系で設定します。

```
+--------------------------------------+
| [method]                             |
|                                      |
| (send a-key-event set-y pos) → void? |
| pos: exact-integer?                 |
+--------------------------------------+
```

イベント時のマウスの y 位置を、対象ウィンドウの（クライアント領域）座標系で設定します。

---

## keymap%

```
+-----------------------+
| classkeymap%: class? |
+-----------------------+
| superclass: object%   |
+-----------------------+
```

`keymap%` オブジェクトは editor<%> オブジェクトがキーボードとマウスの列を拡張可能な任意の関数へ写像するために使います。キーマップはエディタなしでも使えます。keymap% オブジェクトは次を含みます。

- 関数名からイベント処理手続きへの写像
- キーおよびマウス列から関数名への写像

キーマップ内のハンドラ手続きは key-event% または mouse-event% オブジェクトとともに呼ばれます。キーマップの使用文脈（より具体的には handle-key-event または handle-mouse-event への引数）に依存する別の値も渡されます。editor<%> に関連付けられたキーマップでは、追加パラメータは通常、キーボードまたはマウスイベントを受け取った editor<%> オブジェクトです。

```
+-----------------------------------+
| [constructor]                     |
|                                   |
| (new keymap%) → (is-a?/c keymap%) |
+-----------------------------------+
```

an empty keymap を作成します。

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-keymap add-function name func) → void? |
| name: string?                                 |
| func: (any/c (is-a?/c event%). ->. any)     |
+------------------------------------------------+
```

イベントを処理する新しい関数に名前を付けます。handle-key-event、handle-mouse-event、または call-function に応じて呼ばれます。手続きの戻り値は無視されます。

この名前にすでに関数が写像されていた場合、与えられた関数で置き換えられます。

関数が呼ばれるとき、handle-key-event、handle-mouse-event、または call-function に渡された引数が渡されます。エディタに関連付けられたキーマップでは、通常は対象エディタです。

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-keymap is-function-added? fname) → boolean? |
| fname: string?                                     |
+-----------------------------------------------------+
```

fname がこのキーマップに keymap% 経由で追加されていれば #t、そうでなければ #f を返します。

このメソッドは、関数がチェインされたキーマップのいずれかに追加されているかどうかは検査しません。

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-keymap break-sequence) → void? |
+----------------------------------------+
```

キー列の途中にある場合、キーマップの状態をクリアします。たとえばユーザーが Escape を押したあと別ウィンドウへ移った場合、Escape がキーボード列の一部なら、ユーザーが列を完了しないためキーマップ状態をクリアする必要があります。

ブレークコールバック関数は set-break-sequence-callback でインストールできます。

```
+------------------------------+
| [method]                     |
|                              |
| (send a-keymap call-function |
| name: string?               |
| in: any/c                   |
| event: (is-a?/c event%)     |
| try-chain?: any/c = #f      |
+------------------------------+
```

名前付きイベントハンドラを直接呼びます。関数が見つからない、または見つかったハンドラがイベントを処理したくなかった場合は #f を返します。そうでなければイベントハンドラのブール戻り値を返します。

in と event 引数は、キーマップハンドラ手続きが見つかればそれに渡されます。

try-chain? が #f でなければ、このキーマップにチェインされたキーマップも関数名を検索します。関数が見つからず try-chain? が #f の場合、例外も発生しますが、例外ハンドラは脱出できません（「継続とイベントディスパッチ」を参照）。

```
+--------------------------------+
| [method]                       |
|                                |
| (send a-keymap chain-to-keymap |
| next: (is-a?/c keymap%)       |
| prefix?: any/c                |
+--------------------------------+
```

next を a-keymap からチェインします。a-keymap が処理しないイベントを next キーマップが処理します。

prefix? が真なら、同じキー列を両方のキーマップが写像する場合、すでに a-keymap にチェインされた他のキーマップより next が優先されます。あるチェインキーマップが別のキーの接頭辞となるキーを写像する場合、常に短いキー列が使われ、prefix? には依存しません。

chain-to-keymap を使って複数のキーマップを 1 つのキーマップからチェインできます。メインキーマップからチェインされたキーマップがあるとき、メインが処理しないイベントはいずれかが処理するまでチェイン先へ渡されます。キーマップは任意の非巡回グラフでチェインできます。

キーマップのチェインが有用なのは、チェイングループで複数イベント列が正しく扱われるためです。チェインなしでは、イベント列がキーマップに状態を残し、いずれかのキーマップでコールバックが呼ばれたときにリセットが必要になることがあります。この状態は break-sequence で手動クリアできますが、break-sequence を呼ぶと set-break-sequence-callback でインストールしたハンドラも呼ばれます。

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-keymap get-double-click-interval) |
| → (integer-in 0 1000000)                  |
+-------------------------------------------+
```

ダブルクリックのクリック間に許容される最大ミリ秒数を返します。

既定の間隔はプラットフォーム固有の方法で決まりますが、'GRacket:doubleClickTime プリファレンスでグローバルに上書きできます（「Preferences」を参照）。

```
+------------------------------------------------------+
| [method]                                             |
|                                                      |
| (send a-keymap handle-key-event in event) → boolean? |
| in: any/c                                           |
| event: (is-a?/c key-event%)                         |
+------------------------------------------------------+
```

キーボードイベントを処理しようとし、処理された（ハンドラが見つかり真を返した）なら #t、そうでなければ #f を返します。

call-function も参照してください。

```
+--------------------------------------------------------+
| [method]                                               |
|                                                        |
| (send a-keymap handle-mouse-event in event) → boolean? |
| in: any/c                                             |
| event: (is-a?/c mouse-event%)                         |
+--------------------------------------------------------+
```

マウスイベントを処理しようとし、処理された（ハンドラが見つかり真を返した）なら #t、そうでなければ #f を返します。

call-function も参照してください。

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-keymap map-function keyname fname) → void? |
| keyname: string?                                  |
| fname: string?                                    |
+----------------------------------------------------+
```

keyname の文字列エンコード列を使って、入力状態列を関数名へ写像します。keyname の形式はセミコロン区切りの入力状態列で、各状態は修飾子識別子の列に続くキー識別子からなります。

修飾子識別子は次のとおりです。

- s: — 全プラットフォーム: Shift
- c: — 全プラットフォーム: Control
- a: — Mac OS: Option
- m: — Windows: Alt；Unix: Meta；Mac OS: Command（map-command-as-meta-key が #t を返すとき）
- d: — Mac OS: Command
- l: — 全プラットフォーム: Caps Lock
- g: — Windows: Control+Alt を AltGr として；key-event% の get-control+meta-is-altgr を参照
- ?: — 全プラットフォーム: 利用可能なら Shift、AltGr/Option、および／または Caps Lock の逆用で生成された文字への一致を許す；key-event% の get-other-shift-key-code を参照

状態文字列で特定の修飾子が言及されていなければ、その修飾子が押されていてもいなくても一致します。修飾子の前の ~ は、対応する修飾子が押されていない状態にだけ一致させます。状態文字列が : で始まる場合、文字列で言及されていない Shift、Control、Option、Alt、Meta、Command の修飾子が押されていないときだけ一致します。

キー識別子はキーボード上の文字（例: a、2、?）または特別名のいずれかです。特別名は次のとおりです。

- leftbutton （ボタンダウン）
- rightbutton
- middlebutton
- leftbuttondouble （ダブルクリックのボタンダウン）
- rightbuttondouble
- middlebuttondouble
- leftbuttontriple （トリプルクリックのボタンダウン）
- rightbuttontriple
- middlebuttontriple
- leftbuttonseq （ボタンダウンからアップまでの全イベント）
- rightbuttonseq
- middlebuttonseq
- wheelup
- wheeldown
- wheelleft
- wheelright
- esc
- delete
- del （delete と同じ）
- insert
- ins （insert と同じ）
- add
- subtract
- multiply
- divide
- backspace
- back
- return
- enter （return と同じ）
- tab
- space
- right
- left
- up
- down
- home
- end
- pageup
- pagedown
- semicolon （; が列ステップを区切るため）
- colon （: が修飾子を区切るため）
- numpad0
- numpad1
- numpad2
- numpad3
- numpad4
- numpad5
- numpad6
- numpad7
- numpad8
- numpad9
- numpadenter
- f1
- f2
- f3
- f4
- f5
- f6
- f7
- f8
- f9
- f10
- f11
- f12
- f13
- f14
- f15
- f16
- f17
- f18
- f19
- f20
- f21
- f22
- f23
- f24

特別キーワードでは大文字小文字は問いません。ただし 1 文字のキー名では大文字小文字が重要です。さらに 1 文字の ASCII キー名は特別扱いされ、A と s:a はどちらも s:A として扱われます。ただし Windows で m: なしの c: を含む場合、または Mac OS で d: を含む場合、ASCII 文字は s: で大文字化されません。Control なし Alt（Windows）または Command（Mac OS）が Shift の大文字化を打ち消すためです。

1 つの状態がキーマップ（またはキーマップチェイン）内の複数の状態文字列に一致することがあります。その場合、具体性に応じて文字列を順位付けして写像を選びます。押下修飾子をより多く言及する状態文字列が上位で、同じ数なら非押下修飾子をより多く言及する方が上位です。最後に ?: を含み Shift、AltGr/Option、および／または Caps Lock の逆用でのみ一致する文字列は、?: に依存しない一致より下位で、Shift と AltGr/Option の両方の逆用を要する一致はさらに下位です。同じ順位の一致が複数ある場合、任意に選ばれます。

例:

- "space" — 修飾キーの状態にかかわらずスペースバーが押されたときに一致
- "~c:space" — スペースバーが押され Control が押されていないときに一致
- "a" — 修飾キーの状態にかかわらず（Shift 以外）a が打たれたときに一致
- ":a" — 修飾キーなしで a が打たれたときにのみ一致
- "~c:a" — a が打たれ Shift も Control も押されていないときに一致
- "c:m:~g:x" — Control と Alt（Windows）または Meta（Unix）が押された状態で x が打たれ、かつ Windows で Control-Alt が AltGr によるものでないときに一致
- ":esc;:c:c" — Escape 押下（修飾なし）に続く Control-C 押下（Control 以外の修飾なし）に一致
- "?:d:+" — 通常 + の生成に Shift が必要でも、Command と + を生成するキーが押されたときに一致

特定のキー列を接頭辞としても完全列としても写像する map-function の呼び出しは例外を発生しますが、例外ハンドラは脱出できません（「継続とイベントディスパッチ」を参照）。

入力状態が名前へ写像される前に、関数名がハンドラへ写像されている必要はありません。呼び出し時に名前でハンドラがディスパッチされます。関数名へ写像されたイベントハンドラは、入力状態から関数名への写像に影響せず変更できます。

Changed in version 1.2 of package `gui-lib`: Added g: and ~g: support.

```
+------------------------------------------------------+
| [method]                                             |
|                                                      |
| (send a-keymap remove-chained-keymap keymap) → void? |
| keymap: (is-a?/c keymap%)                           |
+------------------------------------------------------+
```

keymap が以前にこのキーマップから（chain-to-keymap 経由で）チェインされていた場合、チェイン先リストから取り除かれます。

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-keymap remove-grab-key-function) → void? |
+--------------------------------------------------+
```

set-grab-key-function でインストールしたコールバックを取り除きます。

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-keymap remove-grab-mouse-function) → void? |
+----------------------------------------------------+
```

set-grab-mouse-function でインストールしたコールバックを取り除きます。

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-keymap set-break-sequence-callback f) → void? |
| f: (-> any)                                          |
+-------------------------------------------------------+
```

break-sequence が呼ばれたときに呼び出されるコールバック手続きをインストールします。一度呼ばれるとコールバックはキーマップから取り除かれます。break-sequence が呼ばれる前に別のコールバックがインストールされると、新しいものがインストールされる直前に古いコールバックが呼ばれます。

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-keymap set-double-click-interval n) → void? |
| n: (integer-in 0 1000000)                          |
+-----------------------------------------------------+
```

ダブルクリックのクリック間に許容される最大ミリ秒数を設定します。

```
+--------------------------------------------------------------------------------+
| [method]                                                                       |
|                                                                                |
| (send a-keymap set-grab-key-function f) → void?                                |
| f: ((or/c string? false?) (is-a?/c keymap%) any/c (is-a?/c key-event%). ->. |
| any)                                                                           |
| ((or/c string? false?)                                                         |
| (is-a?/c keymap%)                                                              |
| any/c                                                                          |
| (is-a?/c key-event%)                                                           |
|. ->. any)                                                                    |
|                                                                                |
| ```racket                                                                      |
| ((or/c string? false?)                                                         |
|  (is-a?/c keymap%)                                                             |
|  any/c                                                                         |
|  (is-a?/c key-event%)                                                          |
|. ->. any)                                                                   |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

キーマップが入力を関数名に一致させた、または一致に失敗したあとに呼ばれるコールバック手続きをインストールします。キーボードグラブ関数は一度にひとつだけインストールできます。グラブコールバック付きキーマップに他がチェインされている場合、チェイン先が一致したとき（チェイン先に独自のグラブコールバックがなければ）コールバックが呼ばれます。

一致／非一致コールバックでグラブコールバックが真を返すと、イベントは処理済みとみなされます。一致コールバックで真を返すと、一致したキーマップ関数はキーマップから呼ばれません。

コールバック手続き f は次のように呼ばれます。

```racket
(f str keymap editor event)
```

str 引数は一致コールバックでは関数名、非一致では #f です。keymap 引数は一致したキーマップ（インストール先にチェインされたものかもしれない）またはインストール先のキーマップです。editor と event 引数は一致キーマップ関数に渡されるものと同じです。

キーグラブコールバック関数は remove-grab-key-function で解除します。

```
+--------------------------------------------------------------------------------+
| [method]                                                                       |
|                                                                                |
| (send a-keymap set-grab-mouse-function f) → void?                              |
| f: ((or/c string? false?) (is-a?/c keymap%) any/c (is-a?/c mouse-event%). -> |
|. any)                                                                         |
| ((or/c string? false?)                                                         |
| (is-a?/c keymap%)                                                              |
| any/c                                                                          |
| (is-a?/c mouse-event%)                                                         |
|. ->. any)                                                                    |
|                                                                                |
| ```racket                                                                      |
| ((or/c string? false?)                                                         |
|  (is-a?/c keymap%)                                                             |
|  any/c                                                                         |
|  (is-a?/c mouse-event%)                                                        |
|. ->. any)                                                                   |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

set-grab-key-function と同様ですが、マウスイベント向けです。

---

## labelled-menu-item<%>

```
+---------------------------------------------+--------------+
| interfacelabelled-menu-item<%>: interface? |              |
+---------------------------------------------+--------------+
| implements:                                 | menu-item<%> |
+---------------------------------------------+--------------+
```

`labelled-menu-item<%>` オブジェクトは文字列ラベルを持つ menu-item<%> です（セパレータ以外のメニュー項目）。より具体的には menu-item%（通常項目）、checkable-menu-item%（チェック可能項目）、または menu%（サブメニュー）のインスタンスです。

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-labelled-menu-item enable enabled?) → void? |
| enabled?: any/c                                    |
+-----------------------------------------------------+
```

メニュー項目を有効または無効にします。項目がサブメニュー（またはメニューバー内のメニュー）ならメニュー全体が無効になりますが、各サブメニュー項目の is-enabled? は、項目自体が（サブメニューに加えて）具体的に無効なときだけ #f を返します。

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-labelled-menu-item get-help-string) |
| → (or/c label-string? #f)                   |
+---------------------------------------------+
```

メニュー項目のヘルプ文字列を返します。なければ #f です。

項目にヘルプがあるとき、その文字列がユーザーへのヘルプ情報表示に使われることがあります。

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-labelled-menu-item get-label) → label-string? |
+-------------------------------------------------------+
```

item’s label を返します。

set-label and get-plain-label も参照してください。

```
+-------------------------------------------------------------+
| [method]                                                    |
|                                                             |
| (send a-labelled-menu-item get-plain-label) → label-string? |
+-------------------------------------------------------------+
```

get-label と同様ですが、set-label と同じ方法でラベル内の & とタブ文字が取り除かれます。

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-labelled-menu-item is-enabled?) → boolean? |
+----------------------------------------------------+
```

メニュー項目が有効なら #t、そうでなければ #f を返します。

enable も参照してください。

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-labelled-menu-item on-demand) → void? |
+-----------------------------------------------+
```

仕様:
通常、項目を含むメニューバーをユーザーがクリックしたとき（メニュー項目が見える前）、項目を含むポップアップメニューがポップアップする直前、またはショートカットキー束縛のために項目を含むメニューバーを検査する直前に呼ばれます。詳細は menu-item-container<%> の on-demand を参照してください。

menu-item-container<%> の on-demand を、コンテナが項目の on-demand を呼ばないようにオーバーライドできます。

デフォルト実装:
オブジェクト作成時に渡された demand-callback 手続きを呼びます。

```
+----------------------------------------------------------+
| [method]                                                 |
|                                                          |
| (send a-labelled-menu-item set-help-string help) → void? |
| help: (or/c label-string? #f)                           |
+----------------------------------------------------------+
```

メニュー項目のヘルプ文字列を設定します。#f でヘルプ文字列を取り除きます。

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-labelled-menu-item set-label label) → void? |
| label: label-string?                               |
+-----------------------------------------------------+
```

メニュー項目のラベルを設定します。ショートカットがある場合、ショートカットには影響しません。

ラベルに & が含まれ、ウィンドウがコントロールの場合、ラベルは特別に解析されます。Windows と Unix では、& の次の文字が表示メニュー上で下線付きになりキーボードニーモニックを示します。メニューバー内のメニュー名の下線付き文字を Alt とともに押すと、そのメニューが選ばれます（on-menu-char 経由）。メニューがフォーカスを持つとき、ニーモニック文字は Alt なしのナビにも使われます。ラベル内の && はリテラル（ナビでない）& に置き換えられます。Mac OS では Unix/Windows と同様に & が解析されますが、ニーモニック下線は表示されません。Mac OS では括弧付きニーモニック文字（と周囲の空白）が表示前に取り除かれます（非ローマ言語でよく使われるため）。歴史的な理由により、ラベルにタブ文字が含まれると、タブとその後の文字は表示メニューで隠されます。これらの規則は button% や他ウィンドウのラベル扱いと一貫しています。

& は get-label が返すラベルでは常に保持され、get-plain-label が返すラベルでは決して保持されません。

---

## list-box%

> [image: list-box.png]

```
+-------------------------+-----------------+
| classlist-box%: class? |                 |
+-------------------------+-----------------+
| superclass: object%     |                 |
| extends:                | list-control<%> |
+-------------------------+-----------------+
```

リストボックスは、スクロールするリストからユーザーが 1 つ以上の文字列項目を選べるようにします。単一選択コントロール（項目を選ぶと以前の選択が外れる）か、複数選択コントロール（項目クリックが他の選択と独立にオン／オフを切り替える）です。

ユーザーがリストボックスの選択を変えるたびに、コールバック手続きが呼ばれます。コールバックは各リストボックス作成時の初期化引数として渡されます。

リストボックスはオプションの列ヘッダ付きの複数列を持てます。リストの項目は全列にまたがる行に対応します。列ヘッダが表示されているとき、ユーザーが列幅を変更できます。さらに列は、論理順は固定のまま表示順を変えるドラッグをオプションでサポートできます。

リストボックスの行と列は 0 から番号付けされます。

choice% も参照してください。

```
+--------------------------------------------------------------------------------+
| [constructor]                                                                  |
|                                                                                |
| (new list-box%                                                                 |
| → (is-a?/c list-box%)                                                          |
| label: (or/c label-string? #f)                                                |
| choices: (listof label-string?)                                               |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c    |
| pane%))                                                                        |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                       |
| (is-a?/c panel%) (is-a?/c pane%))                                              |
| callback: ((is-a?/c list-box%) (is-a?/c control-event%). ->. any) = (lambda |
| (c e) (void))                                                                  |
| ((is-a?/c list-box%) (is-a?/c control-event%)                                  |
|. ->. any)                                                                    |
| style: (listof (or/c 'single 'multiple 'extended 'vertical-label              |
| 'horizontal-label 'variable-columns 'column-headers 'clickable-headers         |
| 'reorderable-headers 'deleted)) = '(single)                                    |
| (listof (or/c 'single 'multiple 'extended                                      |
| 'vertical-label 'horizontal-label                                              |
| 'variable-columns 'column-headers                                              |
| 'clickable-headers 'reorderable-headers                                        |
| 'deleted))                                                                     |
| selection: (or/c exact-nonnegative-integer? #f) = #f                          |
| font: (is-a?/c font%) = view-control-font                                     |
| label-font: (is-a?/c font%) = normal-control-font                             |
| enabled: any/c = #t                                                           |
| vert-margin: spacing-integer? = 2                                             |
| horiz-margin: spacing-integer? = 2                                            |
| min-width: (or/c dimension-integer? #f) = #f                                  |
| min-height: (or/c dimension-integer? #f) = #f                                 |
| stretchable-width: any/c = #t                                                 |
| stretchable-height: any/c = #t                                                |
| columns: (cons/c label-string? (listof label-string?)) = '("Column")          |
| column-order: (or/c #f (listof exact-nonnegative-integer?)) = #f              |
|                                                                                |
| ```racket                                                                      |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                       |
|       (is-a?/c panel%) (is-a?/c pane%))                                        |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| ((is-a?/c list-box%) (is-a?/c control-event%)                                  |
|. ->. any)                                                                   |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (listof (or/c 'single 'multiple 'extended                                      |
|               'vertical-label 'horizontal-label                                |
|               'variable-columns 'column-headers                                |
|               'clickable-headers 'reorderable-headers                          |
|               'deleted))                                                       |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

label が #f でなければリストボックスのラベルとして使われます。そうでなければラベルは表示されません。

label に & が含まれると、button% と同様に特別に解析されます。

choices リストはリストボックスに最初に表示する項目の初期リストを指定します。複数列の場合、choices は第1列の内容を決め、他の列は空文字列で初期化されます。

callback 手続きは、ユーザーが選択・再選択・選択解除・ダブルクリックのいずれかでリストボックス選択を変えたときに呼ばれます。ダブルクリック時のイベント型は 'list-box-dclick、それ以外は 'list-box です。

columns リストはリストボックスの列数を決めます。columns の列タイトルは style に 'column-headers が含まれるときだけ表示されます。さらに 'clickable-headers があれば、ヘッダのクリックは event-type が 'list-box-column の column-control-event% 引数で callback を呼びます。歴史的な理由により、Windows では 'clickable-headers は効果がなく、ヘッダクリックは常に報告されます。

style 指定には次のうちちょうど 1 つを含めなければなりません。

- 'single — 単一選択リストを作成
- 'multiple — 1 回のクリックで他項目の選択を外し新しい項目を選ぶ複数選択リスト。単一選択が普通だが複数も許す場合に使う
- 'extended — 1 回のクリックでクリックした項目の選択をトグルして選択を拡張／縮小する複数選択リスト。複数選択が原則の場合に使う

'multiple と 'extended は修飾なしマウスクリックのプラットフォーム非依存解釈を決めますが、ドラッグ、Shift クリック、Control クリックなどはプラットフォーム標準の解釈です。プラットフォーム固有のインタフェースにかかわらず、ユーザーは常に非連結な項目集合を選んだり選択を外したりできます。一部のプラットフォームでは 'single リストボックスで（唯一の）選択項目を外すこともできます。

style に 'vertical-label があればラベルはコントロールの上、なければ（任意で 'horizontal-label）左に付きます。'deleted があれば非表示で作成され親のジオメトリに影響せず、後から親の add-child で有効化できます。

style に 'variable-columns があれば、append-column と delete-column で列数を変更できます。

selection が整数なら set-selection に渡して初期選択を設定します。selection は choices の長さ未満でなければなりません。

font はコントロール内容のフォント、label-font はラベルのフォントを決めます。enabled については window<%>、horiz-margin と vert-margin については subarea<%>、min-width 等については area<%> を参照。

column-order が #f でなければ、論理列の初期表示順を決めます。詳細は set-column-order を参照。style に 'column-headers と 'reorderable-headers が含まれると、ユーザーは表示上の列順を変更できます（論理順は変わりません）。

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-list-box append item [data]) → void? |
| item: label-string?                         |
| data: any/c = #f                            |
+----------------------------------------------+
```

append in list-control<%> をオーバーライドします。

関連する「データ」オブジェクト付きの新しい項目をリストボックスに追加します。データオブジェクトは表示されず、get-data と使う便宜のためだけに提供され、プログラマがリストボックスとは別に項目→データ写像を管理せずに済むことがあります。

append in list-control<%> も参照してください。

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-list-box append-column label) → void? |
| label: label-string?                         |
+-----------------------------------------------+
```

リストボックスに空タイトルの列を追加しますが、'variable-columns スタイルで作成された場合に限ります。新しい列は論理的に最後の列で、最初は最後の列として表示されます。

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-list-box delete-column n) → void? |
| n: exact-nonnegative-integer?            |
+-------------------------------------------+
```

論理位置 n の列を削除しますが、'variable-columns スタイルで作成され、かつ現在列が 2 つ以上ある場合に限ります（列数は 0 にはできません）。

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-list-box get-column-labels)             |
| → (cons/c label-string? (listof label-string?)) |
+-------------------------------------------------+
```

リストボックスの列ラベルを返します。返される文字列の個数が列数を示します。

```
+---------------------------------------+
| [method]                              |
|                                       |
| (send a-list-box get-column-order)    |
| → (listof exact-nonnegative-integer?) |
+---------------------------------------+
```

論理列の表示順を返します。各列は結果リスト内の論理位置で表され、列位置の順序が表示順を示します。

set-column-order も参照してください。

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-list-box get-column-width column) |
| dimension-integer?                        |
| dimension-integer?                        |
| dimension-integer?                        |
| column: exact-nonnegative-integer?       |
+-------------------------------------------+
```

column（表示位置ではなく論理位置）で識別される列の幅を取得します。0 以上列数未満でなければなりません。

結果には列の現在幅に加え、ユーザー調整時に列サイズを制約する最小幅と最大幅が含まれます。

set-column-width も参照してください。

```
+--------------------------------------+
| [method]                             |
|                                      |
| (send a-list-box get-data n) → any/c |
| n: exact-nonnegative-integer?       |
+--------------------------------------+
```

n で索引付けされた項目のデータを返します。関連データがなければ #f です。行は 0 から。n が選択肢数以上なら exn:fail:contract 例外が発生します。

append and set-data も参照してください。

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send a-list-box get-first-visible-item) |
| → exact-nonnegative-integer?             |
+------------------------------------------+
```

現在リストボックスの先頭にスクロールされている項目のインデックスを報告します。行は 0 から番号付けされます。

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-list-box get-label-font) → (is-a?/c font%) |
+----------------------------------------------------+
```

リストボックス作成時に任意で渡す、コントロールラベル用フォントを返します。

```
+---------------------------------------+
| [method]                              |
|                                       |
| (send a-list-box get-selections)      |
| → (listof exact-nonnegative-integer?) |
+---------------------------------------+
```

現在選択されているすべての項目のインデックスのリストを返します。行は 0 から番号付けされます。

単一選択リストでは、結果は常に null または要素 1 個のリストです。

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-list-box is-selected? n) → boolean? |
| n: exact-nonnegative-integer?              |
+---------------------------------------------+
```

n で索引付けされた項目が選択されていれば #t、そうでなければ #f を返します。行は 0 から。n が選択肢数以上なら exn:fail:contract 例外が発生します。

リストボックスの選択はユーザーのクリックで変わり得、その変更はこのメソッドを経由しません。選択変化の監視にはコントロールのコールバックを使ってください。

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-list-box number-of-visible-items) |
| → exact-positive-integer?                 |
+-------------------------------------------+
```

現在のサイズでユーザーに見えるリストボックス項目の最大数を返します（端数は切り捨て、ただし少なくとも 1）。

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-list-box select n [select?]) → void? |
| n: exact-nonnegative-integer?               |
| select?: any/c = #t                         |
+----------------------------------------------+
```

項目を選択または選択解除します。単一選択リストボックスでは、別の選択肢が選ばれているとその選択は自動的に外れます。複数選択では set-selection と異なり他の選択は保持されます。

select? が #f なら n の項目の選択を外し、そうでなければ選択します。行は 0 から。n が選択肢数以上なら exn:fail:contract 例外が発生します。

リストボックスの選択はユーザーのクリックで変わり得、その変更はこのメソッドを経由しません。選択変化の監視にはコントロールのコールバックを使ってください。

コントロールのコールバック手続きは呼び出されません。

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-list-box set choices0 choices...) → void? |
| choices0: (listof label-string?)                  |
| choices: (listof label-string?)                   |
+----------------------------------------------------+
```

リストボックスをクリアし、新しい項目リストをインストールします。choices0 と choices リストの個数は列数と一致し、すべての choices リストは同じ項目数でなければなりません。そうでなければ exn:fail:contract 例外が発生します。

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-list-box set-column-label   |
| column: exact-nonnegative-integer? |
| label: label-string?               |
+-------------------------------------+
```

column（論理位置）で識別される列のラベルを設定します。0 以上列数未満でなければなりません。

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send a-list-box set-column-order column-order) → void? |
| column-order: (listof exact-nonnegative-integer?)      |
+---------------------------------------------------------+
```

論理列の表示順を設定します。column-order の各要素は論理位置で一意の列を識別し、すべての論理列がリストに含まれなければなりません。

get-column-order も参照してください。

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-list-box set-column-width   |
| column: exact-nonnegative-integer? |
| width: dimension-integer?          |
| min-width: dimension-integer?      |
| max-width: dimension-integer?      |
+-------------------------------------+
```

column（論理位置）で識別される列の幅を設定します。0 以上列数未満でなければなりません。

width は現在の表示幅、min-width と max-width はユーザーがリサイズするときの列幅を制約します。width は min-width 以上 max-width 以下でなければなりません。

列の既定幅はプラットフォーム固有で、リストボックスの最後の列は要求サイズにかかわらずコントロール末尾まで伸びることがあります。

get-column-width も参照してください。

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-list-box set-data n data) → void? |
| n: exact-nonnegative-integer?            |
| data: any/c                              |
+-------------------------------------------+
```

n で索引付けされた項目の関連データを設定します。行は 0 から。n が選択肢数以上なら exn:fail:contract 例外が発生します。

append も参照してください。

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-list-box set-first-visible-item n) → void? |
| n: exact-nonnegative-integer?                     |
+----------------------------------------------------+
```

n で索引付けされた項目がリストボックス表示の先頭になるようスクロールします。行は 0 から。n が選択肢数以上なら exn:fail:contract 例外が発生します。

リストボックスのスクロール位置はユーザーのクリックで変わり得、その変更はこのメソッドを経由しません。プログラムがスクロール位置の変化を検出するには get-first-visible-item をポーリングする以外に方法はありません。

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-list-box set-string n label [column]) → void? |
| n: exact-nonnegative-integer?                        |
| label: label-string?                                 |
| column: exact-nonnegative-integer? = 0               |
+-------------------------------------------------------+
```

論理列 column の n 番目の項目を設定します。行と列は 0 から。n または column が範囲外なら exn:fail:contract 例外が発生します。

---

## list-control<%>

```
+---------------------------------------+------------+
| interfacelist-control<%>: interface? |            |
+---------------------------------------+------------+
| implements:                           | control<%> |
+---------------------------------------+------------+
```

リストコントロールは、ユーザーが選べる文字列項目のリストを与えます。list-control<%> を実装する組み込みクラスは次の 2 つです。

- choice% — ポップアップメニューでリストを提示（一度に 1 項目だけ選択可）
- list-box% — スクロールボックスでリストを提示。style に 'single があれば 1 項目、なければ任意個数を選択可

いずれの場合も、ユーザーが選べる項目集合は動的に変更できます。

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-list-control append item) → void? |
| item: label-string?                      |
+-------------------------------------------+
```

ユーザーが選べる項目リストに新しい項目を追加します。現在の選択は変わりません（空の choice コントロールの場合を除き、そのときは新項目が選ばれます）。

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-list-control clear) → void? |
+-------------------------------------+
```

コントロールからユーザーが選べる項目をすべて取り除きます。

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-list-control delete n) → void? |
| n: exact-nonnegative-integer?         |
+----------------------------------------+
```

n で索引付けされた項目を削除します（0 から）。n が項目数以上なら exn:fail:contract 例外が発生します。

削除されない選択済み項目は選択のままで、他の項目は選択されません。

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-list-control find-string s)    |
| → (or/c exact-nonnegative-integer? #f) |
| s: string?                            |
+----------------------------------------+
```

与えられた文字列に一致するユーザー選択可能項目を探します。見つからなければ #f、見つかればそのインデックス（0 から）を返します。

```
+---------------------------------------------------------------+
| [method]                                                      |
|                                                               |
| (send a-list-control get-number) → exact-nonnegative-integer? |
+---------------------------------------------------------------+
```

コントロール内のユーザー選択可能項目の数（リストコントロールの最大インデックス + 1）を返します。

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-list-control get-selection)    |
| → (or/c exact-nonnegative-integer? #f) |
+----------------------------------------+
```

現在選択されている項目のインデックス（0 から）を返します。選択肢も選択もなければ #f です。複数選択が許され複数選ばれている場合は最初の選択のインデックスを返します。

```
+------------------------------------+
| [method]                           |
|                                    |
| (send a-list-control get-string n) |
| → (and/c immutable? label-string?) |
| n: exact-nonnegative-integer?     |
+------------------------------------+
```

与えられたインデックス（0 から）の項目を返します。最大インデックスを超えると exn:fail:contract 例外が発生します。

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-list-control get-string-selection)   |
| → (or/c (and/c immutable? label-string?) #f) |
+----------------------------------------------+
```

現在選択されている項目を返します。選択肢がなければ #f です。複数選択が許され複数選ばれている場合は最初の選択を返します。

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-list-control set-selection n) → void? |
| n: exact-nonnegative-integer?                |
+-----------------------------------------------+
```

与えられたインデックス（0 から）で指定された項目を選択します。インデックスが最大を超えると exn:fail:contract 例外が発生します。

リストボックスコントロールでは、複数選択が許されていても他のすべての項目の選択が外れます。list-box% の select も参照してください。

このメソッドが呼ばれてもコントロールのコールバックは呼び出されません。

リストコントロールの選択はユーザーのクリックで変わり得、その変更はこのメソッドを経由しません。選択変化の監視にはコントロールのコールバックを使ってください。

```
+------------------------------------------------------+
| [method]                                             |
|                                                      |
| (send a-list-control set-string-selection s) → void? |
| s: string?                                          |
+------------------------------------------------------+
```

与えられた文字列に一致する項目を選択します。一致がなければ exn:fail:contract 例外が発生します。

リストボックスコントロールでは、複数選択が許されていても他のすべての項目の選択が外れます。list-box% の select も参照してください。

このメソッドが呼ばれてもコントロールのコールバックは呼び出されません。

リストコントロールの選択はユーザーのクリックで変わり得、その変更はこのメソッドを経由しません。選択変化の監視にはコントロールのコールバックを使ってください。

---

## menu-bar%

> [image: menu-bar.png]

```
+-------------------------+------------------------+
| classmenu-bar%: class? |                        |
+-------------------------+------------------------+
| superclass: object%     |                        |
| extends:                | menu-item-container<%> |
+-------------------------+------------------------+
```

`menu-bar%` オブジェクトは特定の frame% オブジェクト用に作成されます。フレームは最大 1 つのメニューバーしか持てず、すでにメニューバーがあるフレームに新しいメニューバーを作ると exn:fail:contract 例外が発生します。

```
+--------------------------------------------------------------------------+
| [constructor]                                                            |
|                                                                          |
| (new menu-bar%                                                           |
| → (is-a?/c menu-bar%)                                                    |
| parent: (or/c (is-a?/c frame%) 'root)                                   |
| demand-callback: ((is-a?/c menu-bar%). ->. any) = (lambda (m) (void)) |
+--------------------------------------------------------------------------+
```

指定フレームにメニューバーを作成します。最初は空です。parent として 'root を渡すと、他フレームが表示されていないときだけメニューバーがアクティブになります。'root 親は current-eventspace-has-menu-root? が #t を返し、かつそのようなメニューバーが未作成のときだけ許され、そうでなければ exn:fail:contract 例外が発生します。

demand-callback 手続きは、既定の on-demand メソッドからオブジェクト自身を引数に呼ばれます。

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send a-menu-bar enable enable?) → void? |
| enable?: any/c                          |
+------------------------------------------+
```

メニューバー（すなわちそのすべてのメニュー）を有効または無効にします。各メニューの is-enabled? は、メニュー自体が（メニューバーに加えて）具体的に無効なときだけ #f を返します。

```
+-------------------------------------------------------------+
| [method]                                                    |
|                                                             |
| (send a-menu-bar get-frame) → (or/c (is-a?/c frame%) 'root) |
+-------------------------------------------------------------+
```

メニューバーのフレームを返します。他フレームが表示されていないときに示されるメニューバーなら 'root を返します。

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send a-menu-bar is-enabled?) → boolean? |
+------------------------------------------+
```

the menu bar is enabled なら #t、そうでなければ #f を返します。

---

## menu-item-container<%>

```
+----------------------------------------------+
| interfacemenu-item-container<%>: interface? |
+----------------------------------------------+
+----------------------------------------------+
```

`menu-item-container<%>` オブジェクトは menu%、popup-menu%、または menu-bar% です。

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-menu-item-container get-items) |
| → (listof (is-a?/c menu-item<%>))      |
+----------------------------------------+
```

メニュー、ポップアップメニュー、またはメニューバー内の項目のリストを返します。返されるリストの順序は、ユーザーがメニューやメニューバーで見る順序に対応します。

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-menu-item-container on-demand) → void? |
+------------------------------------------------+
```

仕様:
ユーザーがコンテナをメニューバーとしてクリックしたとき（Unity のグローバルメニューバーの例外を除き、メニュー項目が見える前）、ポップアップメニューとしてポップアップする直前、またはショートカットキー束縛のために項目を含むメニューバーを検査する直前に呼ばれます。

コンテナがメニューバーでもポップアップメニューでもない場合、このメソッドは通常、所有メニューバーまたはポップアップメニューの on-demand 経由で呼ばれます。既定実装が項目の on-demand へチェインするためです。ただしコンテナでオーバーライドして項目の on-demand を呼ばないようにできます。

Unix で Unity ウィンドウマネージャのグローバルメニューバー（Ubuntu の既定）を使う場合、racket/gui/base はユーザーのメニューバークリック通知を受け取りません。クリックによる on-demand を近似するため、frame% がキーボードフォーカスを失うたびにメニューバーの on-demand が呼ばれます。フォーカス喪失がメニュークリックによる場合、on-demand 中に追加した項目がユーザーに表示されないことがある点に注意してください。

デフォルト実装:
オブジェクト作成時に渡された demand-callback を呼び、続けて含まれる項目の on-demand を呼びます。

---

## menu-item%

```
+--------------------------+-------------------------+
| classmenu-item%: class? |                         |
+--------------------------+-------------------------+
| superclass: object%      |                         |
| extends:                 | selectable-menu-item<%> |
+--------------------------+-------------------------+
```

`menu-item%` は通常の文字列ラベル付きメニュー項目です。親は menu% または popup-menu% でなければなりません。ユーザーが選択するとコールバック手続きが呼ばれます。

```
+--------------------------------------------------------------------------------+
| [constructor]                                                                  |
|                                                                                |
| (new menu-item%                                                                |
| → (is-a?/c menu-item%)                                                         |
| label: label-string?                                                          |
| parent: (or/c (is-a?/c menu%) (is-a?/c popup-menu%))                          |
| callback: ((is-a?/c menu-item%) (is-a?/c control-event%). ->. any)          |
| shortcut: (or/c char? symbol? #f) = #f                                        |
| help-string: (or/c label-string? #f) = #f                                     |
| demand-callback: ((is-a?/c menu-item%). ->. any) = (lambda (i) (void))      |
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
| (and/c (listof (or/c 'alt 'cmd 'meta 'ctl                                      |
|                      'shift 'option))                                          |
|        (λ (x) (implies (equal? 'unix (system-type))                            |
|                        (not (and (member 'alt x)                               |
|                                  (member 'meta x)))))                          |
|        (λ (x) (equal? x (remove-duplicates x))))                               |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

parent 内に新しいメニュー項目を作成します。項目は最初表示され、親の末尾に追加されます。ユーザーが項目を選ぶと callback が（イベント型 'menu で）呼ばれます。

set-label for information about mnemonic &s in label を参照してください。

shortcut が #f でなければ項目にショートカットがあります。詳細は get-shortcut を参照。shortcut-prefix はショートカットの修飾キー集合を決めます（get-shortcut-prefix を参照）。

help が #f でなければ項目にヘルプ文字列があります。詳細は get-help-string を参照。

demand-callback 手続きは、既定の on-demand メソッドからオブジェクト自身を引数に呼ばれます。

---

## menu-item<%>

```
+------------------------------------+
| interfacemenu-item<%>: interface? |
+------------------------------------+
+------------------------------------+
```

`menu-item<%>` オブジェクトは menu%、popup-menu%、または menu-bar% 内の要素です。親に影響する操作——項目の改名、削除、チェックの追加など——は menu-item<%> オブジェクト経由で行います。

メニュー項目は separator-menu-item%（単なる区切り）、または labelled-menu-item<%> です。後者はより具体的に menu-item%、checkable-menu-item%、または menu%（サブメニュー）のインスタンスです。

```
+-----------------------------------+
| [method]                          |
|                                   |
| (send a-menu-item delete) → void? |
+-----------------------------------+
```

親から項目を取り除きます。すでに削除済みなら delete は効果がありません。

restore も参照してください。

```
+--------------------------------------------------------------------+
| [method]                                                           |
|                                                                    |
| (send a-menu-item get-parent)                                      |
| → (or/c (is-a?/c menu%) (is-a?/c popup-menu%) (is-a?/c menu-bar%)) |
+--------------------------------------------------------------------+
```

項目を含むメニュー、ポップアップメニュー、またはメニューバーを返します。親は作成時に指定され変更できません。

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-menu-item is-deleted?) → boolean? |
+-------------------------------------------+
```

メニュー項目が親から削除されていれば #t、そうでなければ #f を返します。

```
+------------------------------------+
| [method]                           |
|                                    |
| (send a-menu-item restore) → void? |
+------------------------------------+
```

削除済み項目を親へ戻します。項目は元の位置にかかわらず常に親の末尾へ復元されます。現在削除されていなければ restore は効果がありません。

---
