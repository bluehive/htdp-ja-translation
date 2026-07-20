# 付録 D（続き）: GUI クラス参照（86–99）

> **品質注記（ドラフト）:** 本ファイルのクラス参照は機械支援訳を含む。シグネチャ・コードは原文どおり。長いメソッド説明は後日人手校正予定。

本節は Racket GUI ライブラリのクラス・インタフェース参照のうち、`style-delta%` から `window<%>` までを扱う。

ソース: `extracted/appendix/gui/original_markdown_86` … `99`。

コード、メソッド名、契約（contracts）、シグネチャは原文のまま示す。クラス名・インタフェース名もそのままとする。

---

## style-delta%

```
+----------------------------+
| classstyle-delta%: class? |
+----------------------------+
| superclass: object%        |
+----------------------------+
```

`style-delta%` オブジェクトはスタイル変更をカプセル化する。デルタで表現できる変更には次がある。

- フォントファミリの変更
- フォントフェースの変更
- フォントサイズを新しい値へ変更
- 加法的な量だけフォントを拡大
- 乗法的な量だけフォントを拡大、など
- フォントスタイル（normal、italic、slant）の変更
- フォントスタイルのトグル
- 現在 slant なら italic へ変更、など
- フォントウェイトの変更、など
- 下線の変更、など
- 垂直配置の変更、など
- 前景色の変更
- 前景色を暗く／明るくする、など
- 背景色の変更、など
- テキスト背景の透明性の変更

ほとんどのスタイルデルタ設定には `set-delta` メソッドが便利である。高水準のデルタ仕様を取り、内部のデルタ情報を設定する。

スタイルデルタを十分に活かすには、`set-weight-on` などのメソッドで操作できる内部の on/off 設定を理解する必要がある。たとえばフォントウェイトの変更は、内部設定 `weight-on` と `weight-off` で指定する。おおよそ、`weight-on` はウェイト設定が無いときにそれをオンにし、`weight-off` はウェイト設定があるときにそれをオフにする。両者は次のように厳密に相互作用する。

- `weight-on` と `weight-off` の両方が `'base` なら、フォントウェイトは変更されない。
- `weight-on` が `'base` でなければ、ウェイトは `weight-on` に設定される。
- `weight-off` が `'base` でなければ、基底スタイルのウェイトが `weight-off` のとき、ウェイトは `'normal` に戻される。
- `weight-on` と `weight-off` が同じ値なら、その値に関してウェイトがトグルされる。基底スタイルのウェイトが `weight-on` なら `'normal` に変わり、異なるウェイトなら `weight-on` に変わる。
- `weight-on` と `weight-off` が設定されているが異なる値なら、基底スタイルのウェイトが `weight-off` のときにのみ、ウェイトが `weight-on` に変更される。

フォント スタイル、スムージング、下線、配置も同様の方法で機能します。

アライメントオンとアライメントオフに指定できる値は次のとおりです。

- 'base
- 'top
- 'center
- 'bottom

style-on と style-off に指定できる値は次のとおりです。

- 'base
- 'normal
- 'italic
- 'slant

スムージングオンとスムージングオフに指定できる値は次のとおりです。

- 'base
- 'default
- 'partly-smoothed
- 'smoothed
- 'unsmoothed

下線付きオンと下線オフに指定できる値は次のとおりです。

- #f ('base のように動作)
- #t

size-in-pixels-on および
ピクセル単位のサイズオフは次のとおりです。

- #f ('base のように動作)
- #t

transparent-text-backing-on および
透明テキストバックオフは次のとおりです。

- #f ('base のように動作)
- #t

`weight-on`と`weight-off`に指定できる値は次のとおりです。

- 'base
- 'normal
- 'bold
- 'light

スタイルデルタのファミリと面の設定は相互に依存しています。

- デルタの面が #f で、そのファミリーが
'base の場合、顔も家族も修正されません。
デルタ。
- デルタの面が文字列であり、そのファミリーが
'base の場合、面のみがデルタによって変更されます。
- デルタの家族が 'base でない場合、両方の顔が
とファミリーはデルタによって変更されます。デルタの顔が
#f、デルタを適用すると、スタイルの面が次のように設定されます。
#f、家族の設定が選択に優先されるようにします。
フォント。

```
+--------------------------------------------------------------------------------+
| [コンストラクタ]                                                                  |
|                                                                                |
| (make-object style-delta% [change-command])                                    |
| → (is-a?/c style-delta%)                                                       |
| change-command: (or/c 'change-nothing 'change-normal 'change-toggle-underline |
| 'change-toggle-size-in-pixels 'change-normal-color 'change-bold) =             |
| 'change-nothing                                                                |
| (or/c 'change-nothing                                                          |
| 'change-normal                                                                 |
| 'change-toggle-underline                                                       |
| 'change-toggle-size-in-pixels                                                  |
| 'change-normal-color                                                           |
| 'change-bold)                                                                  |
| (make-object style-delta% change-command v)                                    |
| → (is-a?/c style-delta%)                                                       |
| change-command: (or/c 'change-family 'change-style 'change-toggle-style       |
| 'change-weight 'change-toggle-weight 'change-smoothing                         |
| 'change-toggle-smoothing 'change-alignment)                                    |
| (or/c 'change-family                                                           |
| 'change-style                                                                  |
| 'change-toggle-style                                                           |
| 'change-weight                                                                 |
| 'change-toggle-weight                                                          |
| 'change-smoothing                                                              |
| 'change-toggle-smoothing                                                       |
| 'change-alignment)                                                             |
| v: symbol                                                                     |
| (make-object style-delta% change-command v)                                    |
| → (is-a?/c style-delta%)                                                       |
| change-command: (or/c 'change-size 'change-bigger 'change-smaller)            |
| (or/c 'change-size                                                             |
| 'change-bigger                                                                 |
| 'change-smaller)                                                               |
| v: exact-integer?                                                             |
| (make-object style-delta% change-command v)                                    |
| → (is-a?/c style-delta%)                                                       |
| change-command: (or/c 'change-underline 'change-size-in-pixels)               |
| (or/c 'change-underline                                                        |
| 'change-size-in-pixels)                                                        |
| v: any/c                                                                      |
|                                                                                |
| ```racket                                                                      |
| (or/c 'change-nothing                                                          |
|       'change-normal                                                           |
|       'change-toggle-underline                                                 |
|       'change-toggle-size-in-pixels                                            |
|       'change-normal-color                                                     |
|       'change-bold)                                                            |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (or/c 'change-family                                                           |
|       'change-style                                                            |
|       'change-toggle-style                                                     |
|       'change-weight                                                           |
|       'change-toggle-weight                                                    |
|       'change-smoothing                                                        |
|       'change-toggle-smoothing                                                 |
|       'change-alignment)                                                       |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (or/c 'change-size                                                             |
|       'change-bigger                                                           |
|       'change-smaller)                                                         |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (or/c 'change-underline                                                        |
|       'change-size-in-pixels)                                                  |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

初期化引数はに渡されます。
セットデルタ。

```
+------------------------------------------------+
| [メソッド]                                       |
|                                                |
| (send a-style-delta collapse delta) → boolean? |
| delta: (is-a?/c style-delta%)                 |
+------------------------------------------------+
```

加えられる変更を単一のデルタに集約しようとします。
指定されたデルタの後にこのデルタを適用することによって。戻り値が次の場合
#f の場合、実行することはできません。
崩壊する。それ以外の場合、戻り値は #t であり、このデルタは
折りたたまれた変更仕様が含まれます。

```
+-----------------------------------------+
| [メソッド]                                |
|                                         |
| (send a-style-delta copy delta) → void? |
| delta: (is-a?/c style-delta%)          |
+-----------------------------------------+
```

指定されたスタイルデルタの設定をこの設定にコピーします。

```
+----------------------------------------------+
| [メソッド]                                     |
|                                              |
| (send a-style-delta equal? delta) → boolean? |
| delta: (is-a?/c style-delta%)               |
+----------------------------------------------+
```

指定されたデルタが次のデルタと等しい場合、#t を返します。
すべてのコンテキスト、または #f それ以外の場合。

```
+----------------------------------------+
| [メソッド]                               |
|                                        |
| (send a-style-delta get-alignment-off) |
| → (or/c 'base 'top 'center 'bottom)    |
+----------------------------------------+
```

`style-delta%` を参照。

```
+---------------------------------------+
| [メソッド]                              |
|                                       |
| (send a-style-delta get-alignment-on) |
| → (or/c 'base 'top 'center 'bottom)   |
+---------------------------------------+
```

`style-delta%` を参照。

```
+-----------------------------------------+
| [メソッド]                                |
|                                         |
| (send a-style-delta get-background-add) |
| → (is-a?/c add-color<%>)                |
+-----------------------------------------+
```

背景のオブジェクトの加法カラー シフトを取得します (後で適用されます)。
乗算係数)。この add-color<%> オブジェクトを呼び出します
スタイルデルタの加法的な背景カラー シフトを変更するメソッド。

```
+------------------------------------------+
| [メソッド]                                 |
|                                          |
| (send a-style-delta get-background-mult) |
| → (is-a?/c mult-color<%>)                |
+------------------------------------------+
```

背景の乗算カラーシフトを取得します（前に適用されます）
追加要素)。この多色<%> オブジェクトを呼び出します。
スタイルデルタの乗算背景色を変更するメソッド
シフト。

```
+---------------------------------------------------+
| [メソッド]                                          |
|                                                   |
| (send a-style-delta get-face) → (or/c string? #f) |
+---------------------------------------------------+
```

デルタのフォントフェイス文字列を取得します。この文字列が #f であり、
デルタがスタイルに適用される場合、ファミリーは 'base です。
スタイルの顔と家族は変わりません。ただし、顔の場合は、
文字列が #f で、ファミリーが 'base ではない場合、
スタイルのフェイスが #f に変更されます。

`get-family`も参照。

```
+--------------------------------------------------------------------------+
| [メソッド]                                                                 |
|                                                                          |
| (send a-style-delta get-family)                                          |
| → (or/c 'base 'default 'decorative 'roman 'script 'swiss 'modern 'symbol |
| 'system)                                                                 |
| (or/c 'base 'default 'decorative 'roman 'script                          |
| 'swiss 'modern 'symbol 'system)                                          |
|                                                                          |
| ```racket                                                                |
| (or/c 'base 'default 'decorative 'roman 'script                          |
|       'swiss 'modern 'symbol 'system)                                    |
| ```                                                                      |
+--------------------------------------------------------------------------+
```

デルタのフォントファミリを返します。可能な値は次のとおりです。

- 'base — 家族に変化なし
- 'default
- 'decorative
- 'roman
- 'script
- 'swiss
- 'modern (固定幅)
- 'symbol (ギリシャ文字)
- 'system (制御ラベルの描画に使用)

`get-face`も参照。

```
+-----------------------------------------+
| [メソッド]                                |
|                                         |
| (send a-style-delta get-foreground-add) |
| → (is-a?/c add-color<%>)                |
+-----------------------------------------+
```

前景の加法的カラー シフトを取得します (後景に適用されます)。
乗算係数)。この add-color<%> オブジェクトを呼び出します
スタイルデルタの加算前景色シフトを変更するメソッド。

```
+------------------------------------------+
| [メソッド]                                 |
|                                          |
| (send a-style-delta get-foreground-mult) |
| → (is-a?/c mult-color<%>)                |
+------------------------------------------+
```

前景の乗算カラー シフトを取得します（前景に適用されます）。
追加要素)。この多色<%> オブジェクトを呼び出します。
スタイルデルタの乗法前景色を変更するメソッド
シフト。

```
+-------------------------------------------+
| [メソッド]                                  |
|                                           |
| (send a-style-delta get-size-add) → byte? |
+-------------------------------------------+
```

加算フォントサイズ シフトを取得します (乗算係数の後に適用されます)。

```
+--------------------------------------------------------+
| [メソッド]                                               |
|                                                        |
| (send a-style-delta get-size-in-pixels-off) → boolean? |
+--------------------------------------------------------+
```

`style-delta%` を参照。

```
+-------------------------------------------------------+
| [メソッド]                                              |
|                                                       |
| (send a-style-delta get-size-in-pixels-on) → boolean? |
+-------------------------------------------------------+
```

`style-delta%` を参照。

```
+--------------------------------------------+
| [メソッド]                                   |
|                                            |
| (send a-style-delta get-size-mult) → real? |
+--------------------------------------------+
```

乗算フォントサイズ シフトを取得します (加算係数の前に適用されます)。

```
+----------------------------------------------------------------+
| [メソッド]                                                       |
|                                                                |
| (send a-style-delta get-smoothing-off)                         |
| → (or/c 'base 'default 'partly-smoothed 'smoothed 'unsmoothed) |
+----------------------------------------------------------------+
```

`style-delta%` を参照。

```
+----------------------------------------------------------------+
| [メソッド]                                                       |
|                                                                |
| (send a-style-delta get-smoothing-on)                          |
| → (or/c 'base 'default 'partly-smoothed 'smoothed 'unsmoothed) |
+----------------------------------------------------------------+
```

参照
スタイルデルタ%。

```
+---------------------------------------+
| [メソッド]                              |
|                                       |
| (send a-style-delta get-style-off)    |
| → (or/c 'base 'normal 'italic 'slant) |
+---------------------------------------+
```

参照
スタイルデルタ%。

```
+---------------------------------------+
| [メソッド]                              |
|                                       |
| (send a-style-delta get-style-on)     |
| → (or/c 'base 'normal 'italic 'slant) |
+---------------------------------------+
```

`style-delta%` を参照。

```
+-------------------------------------------------------+
| [メソッド]                                              |
|                                                       |
| (send a-style-delta get-transparent-text-backing-off) |
| → boolean?                                            |
+-------------------------------------------------------+
```

`style-delta%` を参照。

```
+------------------------------------------------------+
| [メソッド]                                             |
|                                                      |
| (send a-style-delta get-transparent-text-backing-on) |
| → boolean?                                           |
+------------------------------------------------------+
```

`style-delta%` を参照。

```
+----------------------------------------------------+
| [メソッド]                                           |
|                                                    |
| (send a-style-delta get-underlined-off) → boolean? |
+----------------------------------------------------+
```

`style-delta%` を参照。

```
+---------------------------------------------------+
| [メソッド]                                          |
|                                                   |
| (send a-style-delta get-underlined-on) → boolean? |
+---------------------------------------------------+
```

`style-delta%` を参照。

```
+-------------------------------------+
| [メソッド]                            |
|                                     |
| (send a-style-delta get-weight-off) |
| → (or/c 'base 'normal 'bold 'light) |
+-------------------------------------+
```

`style-delta%` を参照。

```
+-------------------------------------+
| [メソッド]                            |
|                                     |
| (send a-style-delta get-weight-on)  |
| → (or/c 'base 'normal 'bold 'light) |
+-------------------------------------+
```

`style-delta%` を参照。

```
+--------------------------------------------------+
| [メソッド]                                         |
|                                                  |
| (send a-style-delta set-alignment-off v) → void? |
| v: (or/c 'base 'top 'center 'bottom)            |
+--------------------------------------------------+
```

`style-delta%` を参照。

```
+-------------------------------------------------+
| [メソッド]                                        |
|                                                 |
| (send a-style-delta set-alignment-on v) → void? |
| v: (or/c 'base 'top 'center 'bottom)           |
+-------------------------------------------------+
```

`style-delta%` を参照。

```
+--------------------------------------------------------------------------------+
| [メソッド]                                                                       |
|                                                                                |
| (send a-style-delta set-delta [change-command])                                |
| → (is-a?/c style-delta%)                                                       |
| change-command: (or/c 'change-nothing 'change-normal 'change-toggle-underline |
| 'change-toggle-size-in-pixels 'change-normal-color 'change-bold) =             |
| 'change-nothing                                                                |
| (or/c 'change-nothing                                                          |
| 'change-normal                                                                 |
| 'change-toggle-underline                                                       |
| 'change-toggle-size-in-pixels                                                  |
| 'change-normal-color                                                           |
| 'change-bold)                                                                  |
| (send a-style-delta set-delta change-command param)                            |
| (send a-style-delta set-delta                                                  |
| → (is-a?/c style-delta%)                                                       |
| change-command: (or/c 'change-family 'change-style 'change-toggle-style       |
| 'change-weight 'change-toggle-weight 'change-smoothing                         |
| 'change-toggle-smoothing 'change-alignment)                                    |
| (or/c 'change-family                                                           |
| 'change-style                                                                  |
| 'change-toggle-style                                                           |
| 'change-weight                                                                 |
| 'change-toggle-weight                                                          |
| 'change-smoothing                                                              |
| 'change-toggle-smoothing                                                       |
| 'change-alignment)                                                             |
| param: symbol?                                                                |
| (send a-style-delta set-delta change-command param)                            |
| (send a-style-delta set-delta                                                  |
| → (is-a?/c style-delta%)                                                       |
| change-command: (or/c 'change-size 'change-bigger 'change-smaller)            |
| (or/c 'change-size                                                             |
| 'change-bigger                                                                 |
| 'change-smaller)                                                               |
| param: byte?                                                                  |
| (send a-style-delta set-delta change-command on?)                              |
| (send a-style-delta set-delta                                                  |
| → (is-a?/c style-delta%)                                                       |
| change-command: (or/c 'change-underline 'change-size-in-pixels)               |
| (or/c 'change-underline                                                        |
| 'change-size-in-pixels)                                                        |
| on?: any/c                                                                    |
|                                                                                |
| ```racket                                                                      |
| (or/c 'change-nothing                                                          |
|       'change-normal                                                           |
|       'change-toggle-underline                                                 |
|       'change-toggle-size-in-pixels                                            |
|       'change-normal-color                                                     |
|       'change-bold)                                                            |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (or/c 'change-family                                                           |
|       'change-style                                                            |
|       'change-toggle-style                                                     |
|       'change-weight                                                           |
|       'change-toggle-weight                                                    |
|       'change-smoothing                                                        |
|       'change-toggle-smoothing                                                 |
|       'change-alignment)                                                       |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (or/c 'change-size                                                             |
|       'change-bigger                                                           |
|       'change-smaller)                                                         |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (or/c 'change-underline                                                        |
|       'change-size-in-pixels)                                                  |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

デルタを高レベルの仕様で構成します。戻り値
デルタそのものです。

'change-nothing とを除く
'change-normal、このコマンドは一部のみを変更します。
デルタ。したがって、'change-bold を適用してから、
'change-italic はスタイルとスタイルの両方のデルタを設定します。
体重の変化。

change-command 引数は、デルタを変更する方法を指定します。
可能な値は次のとおりです。

- 'change-nothing — すべての変更をリセットします
- 'change-normal — すべてのスタイルとサイズ変更をオフにします
- 'change-toggle-underline — 現在下線が引かれていない領域に下線を付けます、またはその逆も同様です
- 'change-toggle-size-in-pixels — 現在ポイント単位で解釈されている領域のサイズをピクセル単位で解釈します、またはその逆も同様です
- 'change-normal-color — 前景と背景をそれぞれ黒と白に変更します。
- 'change-italic — フォントのスタイルを斜体に変更します
- 'change-bold — フォントの太さを太字に変更します
- 'change-family — フォントファミリを変更します (param はファミリーです。を参照)
フォント％）;こちらも参照
家族を得る
- 'change-style — フォントのスタイルを変更します (param はスタイルです。を参照)
フォント％）
- 'change-toggle-style — フォントのスタイルを切り替えます (param はスタイルです。「」を参照)
フォント％）
- 'change-weight — フォントのウェイトを変更します (param はウェイトです。参照)
フォント％）
- 'change-toggle-weight — フォントのウェイトを切り替えます (param はウェイトです。参照)
フォント％）
- 'change-smoothing — フォントのスムージングを変更します (param はスムージングです。を参照)
フォント％）
- 'change-toggle-smoothing — フォントのスムージングを切り替えます (param はスムージングです。を参照)
フォント％）
- 'change-alignment — 配置を変更します (param は配置です。「パラメータ」を参照)
スタイルデルタ%)
- 'change-size — サイズを絶対値に変更します (param はサイズです)
- 'change-bigger — テキストを大きくします (param は追加量です)
- 'change-smaller — テキストを小さくします (param は追加量です)
- 'change-underline — 下線ステータスを下線付きまたは無地に設定します。
- 'change-size-in-pixels — サイズの解釈をピクセルまたはポイントに設定します

```
+-------------------------------------------------+
| [メソッド]                                        |
|                                                 |
| (send a-style-delta set-delta-background name)  |
| → (is-a?/c style-delta%)                        |
| name: string?                                  |
| (send a-style-delta set-delta-background color) |
| → (is-a?/c style-delta%)                        |
| color: (is-a?/c color%)                        |
+-------------------------------------------------+
```

デルタエンコードの背景色を絶対値と一致するように変更します。
指定された色。つまり、乗算係数を次のように設定します。
get-background-mult の結果に 0.0 が含まれ、結果に加算値が設定されます。
get-background-add を指定した色に追加する
価値観。さらに、透明テキストの裏打ちも無効にします。
transparent-text-backing-on を #f に設定し、
透明テキストバックオフを #t に設定します。
メソッドの戻り値はデルタそのものです。

文字列の色名が指定されている場合については、を参照。
カラーデータベース<%>。

```
+-------------------------------------------------------------------------+
| [メソッド]                                                                |
|                                                                         |
| (send a-style-delta set-delta-face                                      |
| → (is-a?/c style-delta%)                                                |
| name: string?                                                          |
| family: (or/c 'base 'default 'decorative 'roman 'script 'swiss 'modern |
| 'symbol 'system) = 'default                                             |
| (or/c 'base 'default 'decorative 'roman                                 |
| 'script 'swiss 'modern 'symbol 'system)                                 |
|                                                                         |
| ```racket                                                               |
| (or/c 'base 'default 'decorative 'roman                                 |
|       'script 'swiss 'modern 'symbol 'system)                           |
| ```                                                                     |
+-------------------------------------------------------------------------+
```

セットフェイスに似ていますが、家族も同じに設定します
時間。

戻り値は a-style-delta です。

```
+-------------------------------------------------+
| [メソッド]                                        |
|                                                 |
| (send a-style-delta set-delta-foreground name)  |
| → (is-a?/c style-delta%)                        |
| name: string?                                  |
| (send a-style-delta set-delta-foreground color) |
| → (is-a?/c style-delta%)                        |
| color: (is-a?/c color%)                        |
+-------------------------------------------------+
```

デルタ エンコードの前景色を絶対値と一致するように変更します。
指定された色。つまり、乗算係数を次のように設定します。
get-foreground-mult の結果に 0.0 が含まれ、結果に加算値が設定されます。
指定された色の get-foreground-add の
価値観。メソッドの戻り値はデルタそのものです。

文字列の色名が指定されている場合については、を参照。
カラーデータベース<%>。

```
+-----------------------------------------+
| [メソッド]                                |
|                                         |
| (send a-style-delta set-face v) → void? |
| v: (or/c string? #f)                   |
+-----------------------------------------+
```

参照
顔を取得します。こちらも参照
セットデルタフェイス。

```
+----------------------------------------------------------------------------+
| [メソッド]                                                                   |
|                                                                            |
| (send a-style-delta set-family v) → void?                                  |
| v: (or/c 'base 'default 'decorative 'roman 'script 'swiss 'modern 'symbol |
| 'system)                                                                   |
| (or/c 'base 'default 'decorative 'roman 'script                            |
| 'swiss 'modern 'symbol 'system)                                            |
|                                                                            |
| ```racket                                                                  |
| (or/c 'base 'default 'decorative 'roman 'script                            |
|       'swiss 'modern 'symbol 'system)                                      |
| ```                                                                        |
+----------------------------------------------------------------------------+
```

デルタのフォントファミリを設定します。参照
ゲットファミリー。

```
+---------------------------------------------+
| [メソッド]                                    |
|                                             |
| (send a-style-delta set-size-add v) → void? |
| v: byte?                                   |
+---------------------------------------------+
```

追加のフォントサイズ シフトを設定します (適用されます)
乗算係数の後)。

```
+-------------------------------------------------------+
| [メソッド]                                              |
|                                                       |
| (send a-style-delta set-size-in-pixels-off v) → void? |
| v: any/c                                             |
+-------------------------------------------------------+
```

`style-delta%` を参照。

```
+------------------------------------------------------+
| [メソッド]                                             |
|                                                      |
| (send a-style-delta set-size-in-pixels-on v) → void? |
| v: any/c                                            |
+------------------------------------------------------+
```

`style-delta%` を参照。

```
+----------------------------------------------+
| [メソッド]                                     |
|                                              |
| (send a-style-delta set-size-mult v) → void? |
| v: real?                                    |
+----------------------------------------------+
```

乗算フォントサイズ シフトを設定します (加算係数の前に適用されます)。

```
+------------------------------------------------------------------+
| [メソッド]                                                         |
|                                                                  |
| (send a-style-delta set-smoothing-off v) → void?                 |
| v: (or/c 'base 'default 'partly-smoothed 'smoothed 'unsmoothed) |
| (or/c 'base 'default 'partly-smoothed                            |
| 'smoothed 'unsmoothed)                                           |
|                                                                  |
| ```racket                                                        |
| (or/c 'base 'default 'partly-smoothed                            |
|       'smoothed 'unsmoothed)                                     |
| ```                                                              |
+------------------------------------------------------------------+
```

`style-delta%` を参照。

```
+------------------------------------------------------------------+
| [メソッド]                                                         |
|                                                                  |
| (send a-style-delta set-smoothing-on v) → void?                  |
| v: (or/c 'base 'default 'partly-smoothed 'smoothed 'unsmoothed) |
| (or/c 'base 'default 'partly-smoothed                            |
| 'smoothed 'unsmoothed)                                           |
|                                                                  |
| ```racket                                                        |
| (or/c 'base 'default 'partly-smoothed                            |
|       'smoothed 'unsmoothed)                                     |
| ```                                                              |
+------------------------------------------------------------------+
```

`style-delta%` を参照。

```
+----------------------------------------------+
| [メソッド]                                     |
|                                              |
| (send a-style-delta set-style-off v) → void? |
| v: (or/c 'base 'normal 'italic 'slant)      |
+----------------------------------------------+
```

`style-delta%` を参照。

```
+---------------------------------------------+
| [メソッド]                                    |
|                                             |
| (send a-style-delta set-style-on v) → void? |
| v: (or/c 'base 'normal 'italic 'slant)     |
+---------------------------------------------+
```

`style-delta%` を参照。

```
+-----------------------------------------------------------------+
| [メソッド]                                                        |
|                                                                 |
| (send a-style-delta set-transparent-text-backing-off v) → void? |
| v: any/c                                                       |
+-----------------------------------------------------------------+
```

`style-delta%` を参照。

```
+----------------------------------------------------------------+
| [メソッド]                                                       |
|                                                                |
| (send a-style-delta set-transparent-text-backing-on v) → void? |
| v: any/c                                                      |
+----------------------------------------------------------------+
```

`style-delta%` を参照。

```
+---------------------------------------------------+
| [メソッド]                                          |
|                                                   |
| (send a-style-delta set-underlined-off v) → void? |
| v: any/c                                         |
+---------------------------------------------------+
```

`style-delta%` を参照。

```
+--------------------------------------------------+
| [メソッド]                                         |
|                                                  |
| (send a-style-delta set-underlined-on v) → void? |
| v: any/c                                        |
+--------------------------------------------------+
```

`style-delta%` を参照。

```
+-----------------------------------------------+
| [メソッド]                                      |
|                                               |
| (send a-style-delta set-weight-off v) → void? |
| v: (or/c 'base 'normal 'bold 'light)         |
+-----------------------------------------------+
```

`style-delta%` を参照。

```
+----------------------------------------------+
| [メソッド]                                     |
|                                              |
| (send a-style-delta set-weight-on v) → void? |
| v: (or/c 'base 'normal 'bold 'light)        |
+----------------------------------------------+
```

`style-delta%` を参照。

---

## style-list%

```
+---------------------------+
| classstyle-list%: class? |
+---------------------------+
| superclass: object%       |
+---------------------------+
```

style-list% オブジェクトには、style<%> のセットが含まれています。
オブジェクトを管理し、オブジェクト間の階層関係を維持します。あ
style<%> オブジェクトは、 のメソッドを通じてのみ作成できます。
style-list% オブジェクト。グローバルスタイルリストオブジェクトがあります。
-style-list ですが、任意の数の独立したリストを使用できます。
個別のスタイル階層用に作成されます。各エディタは独自のを作成します
プライベートスタイルリスト。

詳細については、「スタイル」を参照。

```
+-------------------------------------------+
| [コンストラクタ]                             |
|                                           |
| (new style-list%) → (is-a?/c style-list%) |
+-------------------------------------------+
```

`Basic`という名前のルート スタイルが自動的に作成されます。

```
+------------------------------------------------------+
| [メソッド]                                             |
|                                                      |
| (send a-style-list basic-style) → (is-a?/c style<%>) |
+------------------------------------------------------+
```

このメソッドは final であり、オーバーライドできない。

ルートスタイルを返します。各スタイルリストには独自のルート スタイルがあります。

詳細については、「環境設定」も参照。
'GRacket:デフォルトのフォントサイズ
好み。

```
+--------------------------------------------------------+
| [メソッド]                                               |
|                                                        |
| (send a-style-list convert style) → (is-a?/c style<%>) |
| style: (is-a?/c style<%>)                             |
+--------------------------------------------------------+
```

別のスタイルリストのスタイルを、あるスタイルに変換します。
このリストにあります。スタイルがすでにこのリストにある場合は、スタイル
が返されます。スタイルに名前があり、その名前のスタイルが
すでにこのリストにある場合は、既存の名前付きスタイルが返されます。
それ以外の場合、スタイルはその基本スタイルを変換することによって変換されます。
(style が結合スタイルの場合は、shift style) を作成してから、
このリストの新しいスタイル。

```
+-------------------------------------------+
| [メソッド]                                  |
|                                           |
| (send a-style-list find-named-style name) |
| → (or/c (is-a?/c style<%>) #f)            |
| name: string?                            |
+-------------------------------------------+
```

名前でスタイルを検索します。そのようなスタイルが見つからない場合、#f は
戻ってきました。

```
+----------------------------------------------+
| [メソッド]                                     |
|                                              |
| (send a-style-list find-or-create-join-style |
| → (is-a?/c style<%>)                         |
| base-style: (is-a?/c style<%>)              |
| shift-style: (is-a?/c style<%>)             |
+----------------------------------------------+
```

新しい結合スタイルを作成するか、適切な既存の結合スタイルを検索します。の
返されるスタイルは常に名前がありません。詳細については「スタイル」を参照
情報。

基本スタイル引数は、このスタイル内のスタイルである必要があります
リスト。

```
+-----------------------------------------+
| [メソッド]                                |
|                                         |
| (send a-style-list find-or-create-style |
| → (is-a?/c style<%>)                    |
| base-style: (is-a?/c style<%>)         |
| delta: (is-a?/c style-delta%)          |
+-----------------------------------------+
```

新しい派生スタイルを作成するか、適切な既存のスタイルを検索します。
返されるスタイルには常に名前がありません。詳細については「スタイル」を参照
情報。

基本スタイル引数は、このスタイル内のスタイルである必要があります
リスト。 Base-style が結合スタイルではない場合、名前がない場合、
そして、そのデルタをデルタで折りたたむことができるかどうか (を参照)
style-delta% で折りたたむ)、折りたたまれたデルタは次のように使用されます。
デルタの場所、base-style の基本スタイルは
基本スタイルの代わりに使用されます。この折りたたみと置換
基本スタイルの変更は再帰的に実行されます。

```
+-----------------------------------------------------+
| [メソッド]                                            |
|                                                     |
| (send a-style-list forget-notification key) → void? |
| key: any/c                                         |
+-----------------------------------------------------+
```

`notify-on-change` を参照。

key 引数は、notify-on-change によって返される値です。

```
+--------------------------------------+
| [メソッド]                             |
|                                      |
| (send a-style-list index-to-style i) |
| → (or/c (is-a?/c style<%>) #f)       |
| i: exact-nonnegative-integer?       |
+--------------------------------------+
```

指定されたインデックスに関連付けられたスタイル、または #f を返します。
悪いインデックス。 「スタイルからインデックスへ」も参照。

```
+------------------------------------+
| [メソッド]                           |
|                                    |
| (send a-style-list new-named-style |
| → (is-a?/c style<%>)               |
| name: string?                     |
| like-style: (is-a?/c style<%>)    |
+------------------------------------+
```

名前がすでに使用されている場合を除き、新しい名前付きスタイルを作成します。

名前がすでに使用されている場合、like-style は
無視され、名前に関連付けられた古いスタイルは
戻ってきました。それ以外の場合は、名前に新しいスタイルが作成されます。
同じ特性（つまり、同じ基本スタイルと同じスタイル）
デルタまたはシフト スタイル) を同様のスタイルとして使用します。

類似のスタイル スタイルはこのスタイルリストに含まれている必要があります。そうでない場合
名前付きスタイルは、空のスタイルを含む基本スタイルから派生します。
デルタ。

```
+------------------------------------------------+
| [メソッド]                                       |
|                                                |
| (send a-style-list notify-on-change f) → any/c |
| f: ((or/c (is-a?/c style<%>) #f). ->. any)  |
+------------------------------------------------+
```

コールバック f をスタイルリストにアタッチします。コールバック
f はスタイルが変更されるたびに呼び出されます。

多くの場合、1 つのスタイルの変更が他のいくつかのスタイルの変更を引き起こすことになります。
派生スタイル。クライアントがすべての変更を処理できるようにするため、
バッチでは、#f が一連の処理の後に変更スタイルとして f に渡されます。
スタイルが処理されました。

変更時通知からの戻り値は、
忘れ通知で使用される不透明なキー。

コールバック f は、対象となるコールバックを置き換えます。
等しい?。これは、次のような場合に冗長な通知を回避するのに役立ちます。
重複した登録。コールバック f はのみ保持されます
弱く（弱点を作るという意味で）、しかしそれは保持されます
f が偽装する値が到達可能である限り。のために
たとえば、 f がコントラクトが適用された関数を表す場合、
f は、元のメッセージが保存されている限り、通知用に保持されます。
（契約前）機能に到達可能です。コールバック f も
変更時通知によって生成された不透明なキーが到達可能な限り保持されます。

```
+---------------------------------------------------------+
| [メソッド]                                                |
|                                                         |
| (send a-style-list begin-style-change-sequence) → void? |
+---------------------------------------------------------+
```

に含まれるスタイルへの変更を括弧で囲みます。
スタイルリスト% 付き
begin-style-change-sequence と
余分な作業を避けるための end-style-change-sequence
スタイルチェンジ中。

begin-style-change-sequence を呼び出して、
end-style-change-sequence は入れ子にすることができます
恣意的に;スタイルへの変更は、
editor<%> がこの style-list% を使用するのは次のとおりです
end-style-change-sequence への最後の呼び出しと
冗長な呼び出しはその時点でスキップされます。

パッケージ `snip-lib` のバージョン 1.5 で追加。

```
+-------------------------------------------------------+
| [メソッド]                                              |
|                                                       |
| (send a-style-list end-style-change-sequence) → void? |
+-------------------------------------------------------+
```

begin-style-change-sequence の呼び出しと一致するように呼び出します。

パッケージ `snip-lib` のバージョン 1.5 で追加。

```
+---------------------------------------------------------+
| [メソッド]                                                |
|                                                         |
| (send a-style-list number) → exact-nonnegative-integer? |
+---------------------------------------------------------+
```

リスト内のスタイルの数を返します。

```
+----------------------------------------+
| [メソッド]                               |
|                                        |
| (send a-style-list replace-named-style |
| → (is-a?/c style<%>)                   |
| name: string?                         |
| like-style: (is-a?/c style<%>)        |
+----------------------------------------+
```

new-named-style と同様ですが、名前が次の場合を除きます。
すでにスタイルにマップされている場合は、既存のマッピングが置き換えられます。

```
+------------------------------------------+
| [メソッド]                                 |
|                                          |
| (send a-style-list style-to-index style) |
| → (or/c exact-nonnegative-integer? #f)   |
| style: (is-a?/c style<%>)               |
+------------------------------------------+
```

特定のスタイルのインデックスを返します。スタイルのベースのインデックス
スタイル (結合スタイルの場合はシフト スタイルも) であることが保証されます。
スタイル自身のインデックスよりも低くなります。 (その結果、ルート スタイルの
インデックスは常に 0 です。) スタイルのインデックスは、新しいスタイルが作成されるたびに変更される可能性があります。
スタイルがリストに追加されるか、ベース スタイルまたはシフト スタイルが追加されます。
別のスタイルが変更されます。

指定されたスタイルがこのリストにない場合は、#f が返されます。

---

## style<%>

```
+--------------------------------+
| interfacestyle<%>: interface? |
+--------------------------------+
+--------------------------------+
```

style<%> オブジェクトは描画情報 (フォント、
色、配置など) を階層的に表示します。スタイル<%>
オブジェクトは常に style-list のコンテキスト内に存在します%
オブジェクトであり、style-list% オブジェクト以外によって作成されることはありません。

「スタイル」も参照。

```
+------------------------------------------------------------+
| [メソッド]                                                   |
|                                                            |
| (send a-style get-alignment) → (or/c 'top 'center 'bottom) |
+------------------------------------------------------------+
```

スタイルの配置を返します: 'top、'center、または
'bottom。

```
+--------------------------------------------------+
| [メソッド]                                         |
|                                                  |
| (send a-style get-background) → (is-a?/c color%) |
+--------------------------------------------------+
```

スタイルの背景色を返します。

```
+--------------------------------------------------------------+
| [メソッド]                                                     |
|                                                              |
| (send a-style get-base-style) → (or/c (is-a?/c style<%>) #f) |
+--------------------------------------------------------------+
```

スタイルの基本スタイルを返します。詳細については「スタイル」を参照
情報。基本スタイルのみ戻り値は#fです
リストにあります。

```
+----------------------------------------+
| [メソッド]                               |
|                                        |
| (send a-style get-delta delta) → void? |
| delta: (is-a?/c style-delta%)         |
+----------------------------------------+
```

スタイルが結合ではない場合、デルタを変更し、スタイルのデルタと一致するように変更します。
スタイル。詳細については、「スタイル」を参照。

```
+---------------------------------------------+
| [メソッド]                                    |
|                                             |
| (send a-style get-face) → (or/c string? #f) |
+---------------------------------------------+
```

スタイルのフェイス名を返します。フォント%を参照。

```
+-----------------------------------------------------------------------------+
| [メソッド]                                                                    |
|                                                                             |
| (send a-style get-family)                                                   |
| → (or/c 'default 'decorative 'roman 'script 'swiss 'modern 'symbol 'system) |
| (or/c 'default 'decorative 'roman 'script                                   |
| 'swiss 'modern 'symbol 'system)                                             |
|                                                                             |
| ```racket                                                                   |
| (or/c 'default 'decorative 'roman 'script                                   |
|       'swiss 'modern 'symbol 'system)                                       |
| ```                                                                         |
+-----------------------------------------------------------------------------+
```

スタイルのフォントファミリを返します。フォント%を参照。

```
+-------------------------------------------+
| [メソッド]                                  |
|                                           |
| (send a-style get-font) → (is-a?/c font%) |
+-------------------------------------------+
```

スタイルのフォント情報を返します。

```
+--------------------------------------------------+
| [メソッド]                                         |
|                                                  |
| (send a-style get-foreground) → (is-a?/c color%) |
+--------------------------------------------------+
```

スタイルの前景色を返します。

```
+---------------------------------------------+
| [メソッド]                                    |
|                                             |
| (send a-style get-name) → (or/c string? #f) |
+---------------------------------------------+
```

スタイルの名前を返します。名前がない場合は #f を返します。スタイル名
スタイルの style-list% オブジェクトを通じてのみ設定されます。

```
+-----------------------------------------------------+
| [メソッド]                                            |
|                                                     |
| (send a-style get-shift-style) → (is-a?/c style<%>) |
+-----------------------------------------------------+
```

結合スタイルの場合、スタイルのシフト スタイルを返します。それ以外の場合は、
ルートスタイルが返されます。詳細については、「スタイル」を参照。

```
+---------------------------------+
| [メソッド]                        |
|                                 |
| (send a-style get-size) → byte? |
+---------------------------------+
```

スタイルのフォントサイズを返します。

```
+----------------------------------------------+
| [メソッド]                                     |
|                                              |
| (send a-style get-size-in-pixels) → boolean? |
+----------------------------------------------+
```

スタイルのサイズがポイントではなくピクセル単位の場合は #t を返します。
それ以外の場合は #f 。

```
+----------------------------------------------------------+
| [メソッド]                                                 |
|                                                          |
| (send a-style get-smoothing)                             |
| → (or/c 'default 'partly-smoothed 'smoothed 'unsmoothed) |
+----------------------------------------------------------+
```

スタイルのフォントのスムージングを返します。フォント%を参照。

```
+----------------------------------------------------------+
| [メソッド]                                                 |
|                                                          |
| (send a-style get-style) → (or/c 'normal 'italic 'slant) |
+----------------------------------------------------------+
```

スタイルのフォント スタイルを返します。フォント%を参照。

```
+------------------------------------+
| [メソッド]                           |
|                                    |
| (send a-style get-text-descent dc) |
| → (and/c real? (not/c negative?))  |
| dc: (is-a?/c dc<%>)               |
+------------------------------------+
```

指定された DC でこのスタイルを使用してテキストのディセントを返します。

```
+-----------------------------------+
| [メソッド]                          |
|                                   |
| (send a-style get-text-height dc) |
| → (and/c real? (not/c negative?)) |
| dc: (is-a?/c dc<%>)              |
+-----------------------------------+
```

指定された DC でこのスタイルを使用してテキストの高さを返します。

```
+-----------------------------------+
| [メソッド]                          |
|                                   |
| (send a-style get-text-space dc)  |
| → (and/c real? (not/c negative?)) |
| dc: (is-a?/c dc<%>)              |
+-----------------------------------+
```

指定された DC でこのスタイルを使用するテキストの垂直方向の間隔を返します。

```
+-----------------------------------+
| [メソッド]                          |
|                                   |
| (send a-style get-text-width dc)  |
| → (and/c real? (not/c negative?)) |
| dc: (is-a?/c dc<%>)              |
+-----------------------------------+
```

指定されたスタイルでこのスタイルを使用してスペース文字の幅を返します。
DC。

```
+--------------------------------------------------------+
| [メソッド]                                               |
|                                                        |
| (send a-style get-transparent-text-backing) → boolean? |
+--------------------------------------------------------+
```

テキストを消去せずに描画した場合は、#t を返します。
テキストの背景、または #f それ以外。

```
+------------------------------------------+
| [メソッド]                                 |
|                                          |
| (send a-style get-underlined) → boolean? |
+------------------------------------------+
```

スタイルに下線がある場合は #t を返し、または #f を返します。
それ以外の場合は。

```
+---------------------------------------------------------+
| [メソッド]                                                |
|                                                         |
| (send a-style get-weight) → (or/c 'normal 'bold 'light) |
+---------------------------------------------------------+
```

スタイルのフォントの太さを返します。フォント%を参照。

```
+------------------------------------+
| [メソッド]                           |
|                                    |
| (send a-style is-join?) → boolean? |
+------------------------------------+
```

スタイルが結合スタイルの場合は #t を返し、または #f を返します。
それ以外の場合は。詳細については、「スタイル」を参照。

```
+--------------------------------------------------+
| [メソッド]                                         |
|                                                  |
| (send a-style set-base-style base-style) → void? |
| base-style: (is-a?/c style<%>)                  |
+--------------------------------------------------+
```

スタイルの基本スタイルを設定し、スタイルのフォントなどを再計算します。を参照。
詳細については、スタイルを参照。

```
+----------------------------------------+
| [メソッド]                               |
|                                        |
| (send a-style set-delta delta) → void? |
| delta: (is-a?/c style-delta%)         |
+----------------------------------------+
```

スタイルのデルタを設定し (結合スタイルでない場合)、
スタイルのフォントなど。詳細については、「スタイル」を参照。

```
+----------------------------------------------+
| [メソッド]                                     |
|                                              |
| (send a-style set-shift-style style) → void? |
| style: (is-a?/c style<%>)                   |
+----------------------------------------------+
```

スタイルのシフト スタイル (結合スタイルの場合) を設定し、再計算します。
スタイルのフォントなど。詳細については、「スタイル」を参照。

```
+-----------------------------------------------+
| [メソッド]                                      |
|                                               |
| (send a-style switch-to dc old-style) → void? |
| dc: (is-a?/c dc<%>)                          |
| old-style: (or/c (is-a?/c style<%>) #f)      |
+-----------------------------------------------+
```

指定された描画コンテキストのフォント、ペンの色などを設定します。もし
oldstyle は #f ではなく、
指定されたスタイルとこのスタイルが描画コンテキストに適用されます。

---

## subarea<%>

```
+----------------------------------+---------+
| interfacesubarea<%>: interface? |         |
+----------------------------------+---------+
| implements:                      | area<%> |
+----------------------------------+---------+
```

サブエリア<%>は包含エリア<%>です。

すべての subarea<%> クラスは、次の名前を受け入れます。
インスタンス化引数:

- horiz-margin — デフォルトは 2 です。
control<%> クラスと group-box-panel%、
その他の場合は 0。に渡されました
水平マージン
- vert-margin — デフォルトは 2 です。
control<%> クラスと group-box-panel%、
その他の場合は 0。に渡されました
垂直マージン

```
+--------------------------------------------------+
| [メソッド]                                         |
|                                                  |
| (send a-subarea horiz-margin) → spacing-integer? |
| (send a-subarea horiz-margin margin) → void?     |
| margin: spacing-integer?                        |
+--------------------------------------------------+
```

領域の水平マージンを取得または設定します。これは、
右と左、ジオメトリ管理用。詳細については、「ジオメトリ管理」を参照。
情報。

```
+-------------------------------------------------+
| [メソッド]                                        |
|                                                 |
| (send a-subarea vert-margin) → spacing-integer? |
| (send a-subarea vert-margin margin) → void?     |
| margin: spacing-integer?                       |
+-------------------------------------------------+
```

領域の垂直マージンを取得または設定します。これは、
上部と下部、ジオメトリ管理用。詳細については、「ジオメトリ管理」を参照。
情報。

---

## subwindow<%>

```
+------------------------------------+------------+
| interfacesubwindow<%>: interface? |            |
+------------------------------------+------------+
| implements:                        | subarea<%> |
|                                    | window<%>  |
+------------------------------------+------------+
```

subwindow<%> はコンテナーウィンドウです。

```
+------------------------------------------------------------------------+
| [メソッド]                                                               |
|                                                                        |
| (send a-subwindow reparent new-parent) → void?                         |
| new-parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) |
| (is-a?/c pane%))                                                       |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                               |
| (is-a?/c panel%) (is-a?/c pane%))                                      |
|                                                                        |
| ```racket                                                              |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                               |
|       (is-a?/c panel%) (is-a?/c pane%))                                |
| ```                                                                    |
+------------------------------------------------------------------------+
```

ウィンドウを現在の親から削除し、ウィンドウの子にします。
新しい親。現在の親と新しい親は同じものを持っている必要があります
イベントスペース、および新しい親をその子孫にすることはできません
サブウィンドウ。

サブウィンドウが現在の親内で削除された場合、サブウィンドウは残ります。
新しい親で削除されました。同様に、サブウィンドウが表示されている場合、
現在の親は new-parent に表示されます。

---

## tab-panel%

> [image: tab-panel.png]

```
  +---------------------------+
  | [Tab1] [Tab2] [Tab3]      |  ← 上部のタブ行
  |---------------------------|
  |                           |
  |   パネル内容（縦配置）        |
  |                           |
  +---------------------------+
```


```
+-----------------------------+
| classtab-panel%: class?    |
+-----------------------------+
| superclass: vertical-panel% |
+-----------------------------+
```

タブ パネルはサブウィンドウを 1 列に配置しますが、
パネルの上部にはタブの水平行が含まれます。参照
パネル%も。

tab-panel% クラスは仮想
新しいタブが選択されたときのパネルのコンテンツの交換。代わりに、それは
ユーザーが変更されたことを示すためにコールバック プロシージャを呼び出すだけです
タブの選択。

```
+--------------------------------------------------------------------------------+
| [コンストラクタ]                                                                  |
|                                                                                |
| (new tab-panel%                                                                |
| → (is-a?/c tab-panel%)                                                         |
| choices: (listof label-string?)                                               |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c    |
| pane%))                                                                        |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                       |
| (is-a?/c panel%) (is-a?/c pane%))                                              |
| callback: ((is-a?/c tab-panel%) (is-a?/c control-event%). ->. any) =        |
| (lambda (b e) (void))                                                          |
| ((is-a?/c tab-panel%) (is-a?/c control-event%)                                 |
|. ->. any)                                                                    |
| style: (listof (or/c 'no-border 'can-reorder 'can-close 'new-button           |
| 'flat-portable 'deleted)) = null                                               |
| (listof (or/c 'no-border                                                       |
| 'can-reorder 'can-close 'new-button                                            |
| 'flat-portable 'deleted))                                                      |
| font: (is-a?/c font%) = normal-control-font                                   |
| enabled: any/c = #t                                                           |
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
| ((is-a?/c tab-panel%) (is-a?/c control-event%)                                 |
|. ->. any)                                                                   |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (listof (or/c 'no-border                                                       |
|               'can-reorder 'can-close 'new-button                              |
|               'flat-portable 'deleted))                                        |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (list/c (or/c 'left 'center 'right)                                            |
|         (or/c 'top 'center 'bottom))                                           |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

選択リストでタブを指定するタブ ペインを作成します。
ラベル。

選択肢内の各文字列にはアンパサンドを含めることができます。
将来的には、対応するタブをクリックするためのニーモニックが作成される可能性があります。あ
二重アンパサンドは単一アンパサンドに変換されます。

コールバック プロシージャが呼び出されます (イベント タイプが指定されています)。
'tab-panel) ユーザーがタブの選択を変更したとき。

スタイルリストに'no-borderが含まれている場合、境界線はありません。
パネルのコンテンツの周囲に描画されます。
スタイルリストに'can-reorderが含まれている場合、
ユーザーはタブをドラッグして順序を変更できる場合があります。その場合、
on-reorder が呼び出されます。並べ替えは常に行われます
'no-border もスタイルに含まれている場合に有効になります。
スタイルリストに'can-closeが含まれている場合、
ユーザーはタブの閉じるアイコンをクリックできる場合があります。その場合、
on-close-request が呼び出されます。クロージングはいつも
'no-border もスタイルに含まれている場合に有効になります。
スタイルリストに 'flat-portable が含まれている場合、または
`PLT_FLAT_PORTABLE_TAB_PANEL` 環境変数
は、ラケット/GUI がロードされたときに定義されます。
スタイルリストには'no-borderも含まれており、その後に
タブ コントロールにはプラットフォームに依存しない実装が使用されます。
'flat-portable フラグは
次のいずれかの場合、事実上 Windows のスタイルに常に組み込まれます。
'can-reorderまたは'can-closeが含まれます。
スタイルリストに 'new-button が含まれている場合、
タブ コントロールにはプラットフォームに依存しない実装が使用されます。
次に、新しいタブ ボタンが最後のタブの右側に追加され、
新しいタブを挿入します。新しいタブボタンをクリックすると、
on-new-request が呼び出されます。
スタイルに 'deleted が含まれる場合、タブ パネルは非表示として作成されます。
また、親のジオメトリには影響しません。タブパネルは、後で呼び出すことでアクティブにすることができます
親の add-child メソッド。

font 引数は、コントロールのフォントを決定します。有効な引数については、「window<%>」を参照。 horiz-margin と vert-margin については、
引数については、subarea<%> を参照。についての情報は、
min-width、min-height、伸縮可能な幅、および
伸縮可能な高さの引数については、 area<%> を参照。

パッケージ `gui-lib` のバージョン 1.55 で変更: 「再注文可能」と「
'スタイルを閉じることができます。
バージョン 1.56 で変更: 「フラットポータブル スタイル」を追加
Windows での並べ替えと終了のサポート付き。
バージョン 1.62 で変更: 「新しいボタン スタイル」が追加されました。

```
+------------------------------------------+
| [メソッド]                                 |
|                                          |
| (send a-tab-panel append choice) → void? |
| choice: label-string?                   |
+------------------------------------------+
```

パネルの最上行のタブの右端にタブを追加します。

ラベル文字列の選択肢には & を含めることができます。
将来)、新しいタブをクリックするためのニーモニックが作成される可能性があります。あ
&& は & に変換されます。

```
+-------------------------------------+
| [メソッド]                            |
|                                     |
| (send a-tab-panel delete n) → void? |
| n: exact-nonnegative-integer?      |
+-------------------------------------+
```

既存のタブを削除します。 n がそれ以上の場合、
パネル上のタブの数に応じて、exn:fail:contract 例外が発生します。

```
+-----------------------------------------------+
| [メソッド]                                      |
|                                               |
| (send a-tab-panel get-item-label n) → string? |
| n: exact-nonnegative-integer?                |
+-----------------------------------------------+
```

タブのラベルを位置ごとに取得します。タブには 0 から番号が付けられます。
n がパネル内のタブの数以上の場合、
exn:fail:contract 例外が発生します。

```
+------------------------------------------------------------+
| [メソッド]                                                   |
|                                                            |
| (send a-tab-panel get-number) → exact-nonnegative-integer? |
+------------------------------------------------------------+
```

パネル上のタブの数を返します。

```
+----------------------------------------+
| [メソッド]                               |
|                                        |
| (send a-tab-panel get-selection)       |
| → (or/c exact-nonnegative-integer? #f) |
+----------------------------------------+
```

現在選択されているタブのインデックス (0 から数えて) を返します。もし
パネルにタブがない場合、結果は #f になります。

```
+------------------------------------------------------+
| [メソッド]                                             |
|                                                      |
| (send a-tab-panel on-reorder former-indices) → void? |
| former-indices: (listof exact-nonnegative-integer?) |
+------------------------------------------------------+
```

このメソッドは augment で拡張する。

ユーザーがドラッグしてタブを並べ替えたときに呼び出されます。これは次の場合に有効になります。
'can-reorder スタイルを含めることで利用できます (おそらく
'no-border) パネルを作成するとき。の
以前のインデックス リスト レポートでは、新しいタブの位置ごとに、
並べ替える前にタブがあった位置。

パッケージ `gui-lib` のバージョン 1.55 で追加。

```
+---------------------------------------------------+
| [メソッド]                                          |
|                                                   |
| (send a-tab-panel on-close-request index) → void? |
| index: exact-nonnegative-integer?                |
+---------------------------------------------------+
```

ユーザーがタブ内のクローズ ボックスをクリックすると呼び出されます (有効になっています)。
'can-close スタイルを含めることで利用可能な場合 (おそらく
パネルを作成するときに'no-border) を付けます。インデックス
引数は、閉じる可能性のあるタブを指定します。

パッケージ `gui-lib` のバージョン 1.55 で追加。

```
+-------------------------------------------+
| [メソッド]                                  |
|                                           |
| (send a-tab-panel on-new-request) → void? |
+-------------------------------------------+
```

ユーザーがタブ パネルの新しいタブ ボタンをクリックすると呼び出されます。
利用可能な場合は、'new-button スタイルを含めることで有効になります。

パッケージ `gui-lib` のバージョン 1.62 で追加。

```
+----------------------------------------+
| [メソッド]                               |
|                                        |
| (send a-tab-panel set choices) → void? |
| choices: (listof label-string?)       |
+----------------------------------------+
```

パネルからすべてのタブを削除し、指定されたタブをインストールします。
ラベル。

```
+---------------------------------------------------+
| [メソッド]                                          |
|                                                   |
| (send a-tab-panel set-item-label n label) → void? |
| n: exact-nonnegative-integer?                    |
| label: label-string?                             |
+---------------------------------------------------+
```

タブ n のラベルを label に設定します。 n が次の値に等しい場合
またはパネル内のタブの数より大きい場合は、exn:fail:contract 例外が発生します。

```
+--------------------------------------------+
| [メソッド]                                   |
|                                            |
| (send a-tab-panel set-selection n) → void? |
| n: exact-nonnegative-integer?             |
+--------------------------------------------+
```

現在選択されているタブをインデックス(0からカウント)で設定します。
n がパネル内のタブの数以上の場合、
exn:fail:contract 例外が発生します。

---

## tab-snip%

```
+--------------------------+
| classtab-snip%: class?  |
+--------------------------+
| superclass: string-snip% |
+--------------------------+
```

tab-snip% のインスタンスは、
タブがエディタに挿入されます。

```
+---------------------------------------+
| [コンストラクタ]                         |
|                                       |
| (new tab-snip%) → (is-a?/c tab-snip%) |
+---------------------------------------+
```

タブは最初は空ですが、単一のタブのスニップを作成します。

通常、単一のタブが tab-snip% オブジェクトに挿入されます。
挿入メソッドを使用します。

タブのコンテンツは描画されず、タブの内容を決定するときに使用されます。
タブ移動が決定されるエディタでの 1 文字のサイズ
文字幅による (set-tabs を参照)。コンテンツの場合
単一のタブ文字 (通常の場合) の場合、平均
snipのフォントの文字幅がタブの幅として使用されます。

---

## text-field%

> [image: text-field.png]

```
  Label [  editable text area  ]
```


```
+---------------------------+------------+
| classtext-field%: class? |            |
+---------------------------+------------+
| superclass: object%       |            |
| extends:                  | control<%> |
+---------------------------+------------+
```

text-field% オブジェクトは、編集可能なテキスト フィールドです。
オプションのラベルがその前に表示されます。テキストフィールドが 2 つあります
スタイル:

- 単一行のテキストが表示され、特別なコントロール イベントが表示されます。
ユーザーが Return キーまたは Enter キーを押したときに生成されます (テキスト フィールドに
フォーカス)、イベントはテキスト フィールドのフレームによって処理されない、または
ダイアログ (top-level-window<%> の on-traverse-char を参照)。
- 複数行のテキストが表示され、Enter キーが処理されない
特に。

ユーザーがテキストフィールドの内容を変更するたびに、そのコールバックが
プロシージャが呼び出されます。コールバック プロシージャは次のように提供されます。
各テキストフィールドが作成されるときの初期化引数。

テキスト フィールドは、text% エディタ (
アクセスできないディスプレイ）。したがって、text-field% が提供するのに対し、
テキストフィールド内のテキストを操作するには get-value と set-value のみを使用します。
get-editor はフィールドのエディタを返します。
より洗練されたメソッドの膨大なコレクションを提供します。
テキストに対する操作。

テキスト フィールドのエディタのキーマップは、
現在のキーマップ初期化プロシージャは、
current-text-keymap-initializer パラメーター。

```
+-----------------------------------------------------------------------------+
| [コンストラクタ]                                                               |
|                                                                             |
| (new text-field%                                                            |
| → (is-a?/c text-field%)                                                     |
| label: (or/c label-string? #f)                                             |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c |
| pane%))                                                                     |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                    |
| (is-a?/c panel%) (is-a?/c pane%))                                           |
| callback: ((is-a?/c text-field%) (is-a?/c control-event%). ->. any) =    |
| (lambda (t e) (void))                                                       |
| ((is-a?/c text-field%) (is-a?/c control-event%)                             |
|. ->. any)                                                                 |
| init-value: string? = ""                                                   |
| style: (listof (or/c 'single 'multiple 'hscroll 'password 'vertical-label  |
| 'horizontal-label 'deleted)) = '(single)                                    |
| (listof (or/c 'single 'multiple 'hscroll 'password                          |
| 'vertical-label 'horizontal-label                                           |
| 'deleted))                                                                  |
| font: (is-a?/c font%) = normal-control-font                                |
| enabled: any/c = #t                                                        |
| vert-margin: spacing-integer? = 2                                          |
| horiz-margin: spacing-integer? = 2                                         |
| min-width: (or/c dimension-integer? #f) = #f                               |
| min-height: (or/c dimension-integer? #f) = #f                              |
| stretchable-width: any/c = #t                                              |
| stretchable-height: any/c = (memq 'multiple style)                         |
|                                                                             |
| ```racket                                                                   |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                    |
|       (is-a?/c panel%) (is-a?/c pane%))                                     |
| ```                                                                         |
|                                                                             |
| ```racket                                                                   |
| ((is-a?/c text-field%) (is-a?/c control-event%)                             |
|. ->. any)                                                                |
| ```                                                                         |
|                                                                             |
| ```racket                                                                   |
| (listof (or/c 'single 'multiple 'hscroll 'password                          |
|               'vertical-label 'horizontal-label                             |
|               'deleted))                                                    |
| ```                                                                         |
+-----------------------------------------------------------------------------+
```

ラベルが#fでない場合、テキストフィールドとして使用されます
ラベル。それ以外の場合、テキストフィールドにはラベルが表示されません。

ラベル内に & が出現すると、
button% のように特別に解析されます。

ユーザーが変更すると、コールバック プロシージャが呼び出されます。
テキストフィールドにテキストを入力するか、Enter キーを押します (Enter キーは押しません)
テキストフィールドのフレームまたはダイアログによって処理されます。参照してください
トップレベルウィンドウ<%>のon-traverse-char)。ユーザーが押した場合
コールバックに渡されるイベントのタイプは次のとおりです。
'text-field-enter、それ以外の場合は
'text-field。

init-value が "" ではない場合、
テキスト項目は、初期値を表示するのに十分な幅に作られています。それ以外の場合は、
組み込みのデフォルト幅が選択されます。単一行のテキストフィールドの場合
モードでは、グラフィックの最小サイズは 1 行を表示するように設定されており、
コントロールの幅はデフォルトで伸縮可能です。複数行のテキストフィールドの場合、
グラフィックの最小サイズは 3 行のテキストを表示し、両方の方向に伸縮可能です。
デフォルトで方向が決まります。

スタイルには、'single または
'multiple;前者は単一行フィールドを指定し、
後者は複数行のフィールドを指定します。 'hscroll スタイル
複数行のフィールドにのみ適用されます。 'hscroll のとき
指定すると、フィールドには水平スクロールバーが表示され、自動折り返しが行われます。
無効。それ以外の場合、フィールドには水平スクロールバーがなく、
自動ラッピングが有効になっています。複数行のテキストフィールドには常に
垂直スクロールバー。 'password スタイルは、
フィールドは、汎用を使用してコンテンツの各文字を描画する必要があります
実際の文字の代わりに記号を使用します。スタイルに 'vertical-label が含まれる場合、テキスト フィールドは次のようになります。
コントロールの上にラベルを付けて作成されます。スタイルに含まれない場合
'vertical-label (オプションで 'horizontal-label も含まれます)、その後、
ラベルはテキストフィールドの左側に作成されます。
スタイルに 'deleted が含まれる場合、テキスト フィールドは非表示として作成されます。
また、親のジオメトリには影響しません。テキストフィールドは、後で呼び出すことでアクティブにすることができます
親の add-child メソッド..

font 引数は、コントロールのフォントを決定します。有効な引数については、「window<%>」を参照。 horiz-margin と vert-margin については、
引数については、subarea<%> を参照。についての情報は、
min-width、min-height、伸縮可能な幅、および
伸縮可能な高さの引数については、 area<%> を参照。

```
+--------------------------------------------------+
| [メソッド]                                         |
|                                                  |
| (send a-text-field get-editor) → (is-a?/c text%) |
+--------------------------------------------------+
```

テキストフィールドの実装に使用されるエディタを返します。

テキストフィールドの場合、text% オブジェクトの最も便利なメソッド
は次のとおりです。

- (send a-text get-text) が返されます
エディタの現在のテキスト。
- (send a-text erase) すべてのテキストを削除します
編集者。
- (send a-text insertstr) 挿入
str をエディタの現在のキャレット位置に入力します。

```
+-------------------------------------------------------------+
| [メソッド]                                                    |
|                                                             |
| (send a-text-field get-field-background) → (is-a?/c color%) |
+-------------------------------------------------------------+
```

フィールドの編集可能領域の背景色を取得します。

```
+-----------------------------------------+
| [メソッド]                                |
|                                         |
| (send a-text-field get-value) → string? |
+-----------------------------------------+
```

現在テキストフィールドにあるテキストを返します。

```
+--------------------------------------------------------+
| [メソッド]                                               |
|                                                        |
| (send a-text-field set-field-background color) → void? |
| color: (or/c (is-a?/c color%) #f)                     |
+--------------------------------------------------------+
```

フィールドの編集可能領域の背景色を color に設定します。
色が #f の場合、背景色を設定します
ダークモードでは黒、ダークモードでない場合は白になります。

```
+-------------------------------------------+
| [メソッド]                                  |
|                                           |
| (send a-text-field set-value val) → void? |
| val: string?                             |
+-------------------------------------------+
```

現在テキストフィールドにあるテキストを設定します。 (コントロールのコールバック
プロシージャは呼び出されません。)

テキストフィールドの値は変更可能です
ユーザーがコントロールに入力することによって行われますが、そのような変更はこのメソッドを経由しません。コントロール コールバック プロシージャ (初期化引数として提供) を使用して、
モニター値が変化します。

---

## text%

```
+---------------------+-----------+
| classtext%: class? |           |
+---------------------+-----------+
| superclass: object% |           |
| extends:            | editor<%> |
+---------------------+-----------+
```

`text%` オブジェクトは標準のテキストエディタである。テキストエディタは、`editor-canvas%` オブジェクトまたは他の表示機構を通じて画面に表示される。

```
+------------------------------------------------------+
| [コンストラクタ]                                        |
|                                                      |
| (new text%                                           |
| line-spacing: (and/c real? (not/c negative?)) = 1.0 |
| tab-stops: (listof real?) = null                    |
| auto-wrap: any/c = #f                               |
+------------------------------------------------------+
```

line-spacing 引数は追加のスペース量を設定します。
(DC 単位で) エディタの各行の間に挿入されます。
エディタが表示されます。この間隔は報告される高さに含まれます
各行の。

タブストップの詳細については、`set-tabs`を参照。

auto-wrap が true の場合、自動折り返しは次の方法で有効になります。
自動折り返し。

新しいエディタ用に新しい keymap% オブジェクトが作成されます。こちらも参照
get-keymap と set-keymap。

新しい style-list% オブジェクトが新しいエディタ用に作成されます。参照
get-style-list と set-style-list も同様です。

```
+----------------------------------------------------+
| [メソッド]                                           |
|                                                    |
| (send a-text after-change-style start len) → void? |
| start: exact-nonnegative-integer?                 |
| len: exact-nonnegative-integer?                   |
+----------------------------------------------------+
```

このメソッドは augment で拡張する。

仕様:
指定された範囲のスタイルが変更された後 (および
表示が更新されます。変更時スタイルを使用する
余分な更新を避けるための begin-edit-sequence
after-change-style がエディタを変更するとき)。

can-change-style も参照。そして編集中のシーケンス。

このメソッドが呼ばれるとき、内部ロックは設定されない。

既定の実装:
何もしない。

```
+----------------------------------------------+
| [メソッド]                                     |
|                                              |
| (send a-text after-delete start len) → void? |
| start: exact-nonnegative-integer?           |
| len: exact-nonnegative-integer?             |
+----------------------------------------------+
```

このメソッドは augment で拡張する。

仕様:
指定された範囲がエディタから削除された後 (および
表示が更新されます。削除時に使用し、
begin-edit-sequence は、次の場合に余分な更新を避けるためのものです。
削除後はエディタを変更します)。

start 引数は開始位置を指定します
削除された範囲の。 len 引数は、次の数を指定します。
削除されたアイテム (つまり、start+len は
削除された範囲の終了位置)。

「削除可能?」も参照。そして編集中のシーケンス。

このメソッドが呼ばれるとき、内部ロックは設定されない。

既定の実装:
何もしない。

```
+----------------------------------------------+
| [メソッド]                                     |
|                                              |
| (send a-text after-insert start len) → void? |
| start: exact-nonnegative-integer?           |
| len: exact-nonnegative-integer?             |
+----------------------------------------------+
```

このメソッドは augment で拡張する。

仕様:
アイテムがエディタに挿入された後 (および
表示が更新されます。挿入時に使用し、
begin-edit-sequence は、次の場合に余分な更新を避けるためのものです。
挿入後はエディタを変更します)。

start 引数は、挿入の位置を指定します。の
len 引数は、全長 (位置単位) を指定します。
挿入されたアイテム。

「缶挿入?」も参照。そして編集中のシーケンス。

このメソッドが呼ばれるとき、内部ロックは設定されない。

既定の実装:
何もしない。

```
+---------------------------------------------+
| [メソッド]                                    |
|                                             |
| (send a-text after-merge-snips pos) → void? |
| pos: exact-nonnegative-integer?            |
+---------------------------------------------+
```

このメソッドは augment で拡張する。

仕様:
エディタ内の隣接するスニップが 1 つに結合された後に呼び出されます。

pos 引数はエディタ内の位置を指定します。
スニップがマージされた場所 (つまり、1 つの古いスニップがその直前にありました)
pos、古いものは pos の直後にあり、新しいスニップはまたがっています
正）。

あわせて merge-with も参照。

既定の実装:
何もしない。

```
+------------------------------------------+
| [メソッド]                                 |
|                                          |
| (send a-text after-set-position) → void? |
+------------------------------------------+
```

このメソッドは augment で拡張する。

仕様:
開始位置と終了位置が移動された後に呼び出されます (ただし、
挿入または削除により位置が移動された場合)。

こちらも参照
編集中のシーケンス。

既定の実装:
何もしない。

```
+-------------------------------------------------+
| [メソッド]                                        |
|                                                 |
| (send a-text after-set-size-constraint) → void? |
+-------------------------------------------------+
```

このメソッドは augment で拡張する。

仕様:
エディタの高さまたは幅の最大値または最小値が設定された後に呼び出されます。
変更されました (表示が更新された後、使用します)
on-set-size-constraint と begin-edit-sequence は、after-set-size-constraint がエディタを変更するときの余分な更新を回避します)。

(このコールバック メソッドが提供されるのは、エディタの最大値を設定するためです。
幅により、行がソフト改行でリフローされる可能性があります。)

can-set-size-constraint? も参照。そして編集中のシーケンス。

既定の実装:
何もしない。

```
+--------------------------------------------+
| [メソッド]                                   |
|                                            |
| (send a-text after-split-snip pos) → void? |
| pos: exact-nonnegative-integer?           |
+--------------------------------------------+
```

このメソッドは augment で拡張する。

仕様:
エディタ内のスニップが 2 つに分割された後に呼び出されます。
スプリットスニップを呼び出すか、その他のアクション中に呼び出します。
挿入するように。

pos 引数はエディタ内の位置を指定します。
切れ目が割れたところ。

既定の実装:
何もしない。

```
+------------------------------------------------+
| [メソッド]                                       |
|                                                |
| (send a-text call-clickback start end) → void? |
| start: exact-nonnegative-integer?             |
| end: exact-nonnegative-integer?               |
+------------------------------------------------+
```

指定された範囲の場合、クリックバックを呼び出すユーザーのクリックをシミュレートします。
位置はクリックバックの領域内にあります。こちらも参照
クリックバック。

```
+------------------------------------------------------+
| [メソッド]                                             |
|                                                      |
| (send a-text can-change-style? start len) → boolean? |
| start: exact-nonnegative-integer?                   |
| len: exact-nonnegative-integer?                     |
+------------------------------------------------------+
```

このメソッドは augment で拡張する。

仕様:
エディタの特定の範囲でスタイルが変更される前に呼び出されます。もし
戻り値が #f の場合、スタイルの変更は次のようになります。
中止されました。

エディタは、この呼び出し中に書き込みのために内部的にロックされます。
メソッド (「内部エディタのロック」も参照)。必要に応じて、after-change-style を使用してエディタを変更します。

`on-change-style`、`after-change-style`、および`on-edit-sequence`も参照。

既定の実装:
#t を返す。

```
+------------------------------------------------+
| [メソッド]                                       |
|                                                |
| (send a-text can-delete? start len) → boolean? |
| start: exact-nonnegative-integer?             |
| len: exact-nonnegative-integer?               |
+------------------------------------------------+
```

このメソッドは augment で拡張する。

仕様:
エディタから範囲が削除される前に呼び出されます。
戻り値が #f の場合、
削除は中止されます。

start 引数は開始位置を指定します
削除する範囲の。 len 引数は、次の数を指定します。
削除する項目 (つまり、start+len は
削除する範囲の終了位置)。

このメソッドの呼び出し中、エディタは書き込みのために内部的にロックされます。
(「内部エディタのロック」も参照)。使用する
必要に応じて、削除後、エディタを変更します。

「削除時」、「削除後」、および「削除時」も参照。
編集中のシーケンス。

既定の実装:
#t を返す。

```
+------------------------------------------------+
| [メソッド]                                       |
|                                                |
| (send a-text can-insert? start len) → boolean? |
| start: exact-nonnegative-integer?             |
| len: exact-nonnegative-integer?               |
+------------------------------------------------+
```

このメソッドは augment で拡張する。

仕様:
項目がエディタに挿入される前に呼び出されます。もし
戻り値が #f の場合、挿入は中止されます。

start 引数は、ポテンシャルの位置を指定します。
挿入します。 len 引数は、全長 (単位:
挿入する項目の位置)。

エディタは、この呼び出し中に書き込みのために内部的にロックされます。
メソッド (「内部エディタのロック」も参照)。挿入後を使用して、
必要に応じてエディタを変更します。

「挿入時」、「挿入後」、および「挿入時」も参照。
編集中のシーケンス。

既定の実装:
#t を返す。

```
+---------------------------------------------------+
| [メソッド]                                          |
|                                                   |
| (send a-text can-set-size-constraint?) → boolean? |
+---------------------------------------------------+
```

このメソッドは augment で拡張する。

仕様:
エディタの最大または最小の高さまたは幅の前に呼び出されます
が変更されます。戻り値が #f の場合、
変更は中止されます。

(このコールバック メソッドが提供されるのは、エディタの最大値を設定するためです。
幅により、行がソフト改行でリフローされる可能性があります。)

on-set-size-constraint、after-set-size-constraint、および on-edit-sequence も参照。

既定の実装:
#t を返す。

```
+----------------------------------------+
| [メソッド]                               |
|                                        |
| (send a-text caret-hidden?) → boolean? |
+----------------------------------------+
```

このエディタでキャレットが非表示の場合は #t を返し、または #f を返します。
それ以外の場合は。

あわせて hide-caret も参照。

```
+---------------------------------------------------------------------+
| [メソッド]                                                            |
|                                                                     |
| (send a-text change-style                                           |
| delta: (or/c (is-a?/c style-delta%) #f)                            |
| start: (or/c exact-nonnegative-integer? 'start) = 'start           |
| end: (or/c exact-nonnegative-integer? 'end) = 'end                 |
| counts-as-mod?: any/c = #t                                         |
| (send a-text change-style style [start end counts-as-mod?]) → void? |
| (send a-text change-style                                           |
| style: (or/c (is-a?/c style<%>) #f)                                |
| start: (or/c exact-nonnegative-integer? 'start) = 'start           |
| end: (or/c exact-nonnegative-integer? 'end) = 'end                 |
| counts-as-mod?: any/c = #t                                         |
+---------------------------------------------------------------------+
```

スタイルデルタを適用して、エディタ内の領域のスタイルを変更します。
または特定のスタイルをインストールします。開始が'startの場合
最後が 'end の場合、現在選択されている
項目が変更されます。それ以外の場合、end が
'end、最初から最後までスタイルが変更されます。
選択の終わり。 MODとしてカウントする場合?は#f、
set-modified は、
スタイルチェンジ。

大量のスニップのコレクションをあるスタイルから別のスタイルに変更するには、
ではなく style<%> インスタンスを提供することを検討してください。
style-delta% インスタンス。それ以外の場合、change-style は style-delta% インスタンスを
すべてのスニップの style<%> インスタンス。この変換により消費されるのは
時間と（一時的な）記憶の両方。

スタイルが提供されている場合: エディタのスタイルリストにはスタイルが含まれている必要があります。それ以外の場合は、
スタイルは変わりません。 「style-list% での変換」も参照。

```
+-----------------------------------------------------------+
| [メソッド]                                                  |
|                                                           |
| (send a-text copy [extend? time start end]) → void?       |
| extend?: any/c = #f                                      |
| time: exact-integer? = 0                                 |
| start: (or/c exact-nonnegative-integer? 'start) = 'start |
| end: (or/c exact-nonnegative-integer? 'end) = 'end       |
+-----------------------------------------------------------+
```

editor<%> でコピーを拡張します。

指定された範囲のテキストをクリップボードにコピーします。延長したら？です
#f ではない場合、古いクリップボードの内容が追加されます。もし
開始が 'start または終了が 'end の場合、
現在の選択範囲の開始/終了が使用されます。

time 引数の詳細については、「タイム スタンプのカット アンド ペースト」を参照。もし
時間がプラットフォーム固有の時間範囲外である、
exn:fail:contract 例外が発生します。

```
+-----------------------------------------------------+
| [メソッド]                                            |
|                                                     |
| (send a-text copy-self-to dest) → void?             |
| dest: (or/c (is-a?/c text%) (is-a?/c pasteboard%)) |
+-----------------------------------------------------+
```

editor<%> で copy-self-to をオーバーライドします。

editor<%> のデフォルトの copy-self-to の動作に加えて、
このエディタのファイル形式、ワードブレーク機能、ワードブレークマップ、
しきい値間のクリック、キャレットの表示状態、上書きモード
state と autowrap ビットマップが dest にインストールされます。

```
+-----------------------------------------------------------+
| [メソッド]                                                  |
|                                                           |
| (send a-text cut [extend? time start end]) → void?        |
| extend?: any/c = #f                                      |
| time: exact-integer? = 0                                 |
| start: (or/c exact-nonnegative-integer? 'start) = 'start |
| end: (or/c exact-nonnegative-integer? 'end) = 'end       |
+-----------------------------------------------------------+
```

editor<%> のカットをオーバーライドします。

指定した範囲をコピーして削除します。延長したら？ではありません
#f、古いクリップボードの内容が追加されます。開始の場合
'start または終了が 'end の場合、現在の
選択の開始/終了が使用されます。

time 引数の詳細については、「タイム スタンプのカット アンド ペースト」を参照。もし
時間がプラットフォーム固有の時間範囲外である、
exn:fail:contract 例外が発生します。

```
+-------------------------------------------------------+
| [メソッド]                                              |
|                                                       |
| (send a-text delete start [end scroll-ok?]) → void?   |
| start: (or/c exact-nonnegative-integer? 'start)      |
| end: (or/c exact-nonnegative-integer? 'back) = 'back |
| scroll-ok?: any/c = #t                               |
| (send a-text delete) → void?                          |
+-------------------------------------------------------+
```

指定した範囲または現在選択されているテキストを削除します（選択されていない場合）。
範囲が提供されます)。開始の場合
'start の場合、開始選択位置は次のようになります。
使用済み。 end が 'back の場合、書記素のみ
前の開始は削除されます。スクロールしても大丈夫ですか？ではありません
#f および開始は現在のキャレットと同じです
位置を指定すると、エディタの表示は次のようになります。
スクロールして新しい選択位置を表示します。

エディタの内容は変更可能
によって
他のメソッドに応答するシステム
呼び出し、そのような変更はこのメソッドを経由しません。削除時を使用して、
コンテンツ削除の変更を監視します。

パッケージ `gui-lib` のバージョン 1.67 で変更: を削除するために「戻る」を変更しました
文字の代わりに書記素。

```
+------------------------------------------------------+
| [メソッド]                                             |
|                                                      |
| (send a-text do-copy start end time extend?) → void? |
| start: exact-nonnegative-integer?                   |
| end: exact-nonnegative-integer?                     |
| time: exact-integer?                                |
| extend?: any/c                                      |
+------------------------------------------------------+
```

仕様:
エディタの領域をクリップボードにコピーするために呼び出されます。この方法
サブクラスによってオーバーライドできるように提供されています。電話しないでください
このメソッドを直接;代わりに、copy を呼び出します。

time 引数の詳細については、「タイム スタンプのカット アンド ペースト」を参照。もし
時間がプラットフォーム固有の時間範囲外である、
exn:fail:contract 例外が発生します。

既定の実装:
データを最初から最後までコピーし、現在のデータを拡張します。
クリップボードのコンテキストを拡張する場合? #fではありません。

```
+-------------------------------------------+
| [メソッド]                                  |
|                                           |
| (send a-text do-paste start time) → void? |
| start: exact-nonnegative-integer?        |
| time: exact-integer?                     |
+-------------------------------------------+
```

仕様:
クリップボードの現在の内容をエディタに貼り付けるために呼び出されます。
このメソッドは、サブクラスによってオーバーライドできるように提供されています。
このメソッドを直接呼び出さないでください。代わりに、paste を呼び出します。

time 引数の詳細については、「タイム スタンプのカット アンド ペースト」を参照。もし
時間がプラットフォーム固有の時間範囲外である、
exn:fail:contract 例外が発生します。

既定の実装:
開始位置に貼り付けます。

```
+------------------------------------+
| [メソッド]                           |
|                                    |
| (send a-text do-paste-x-selection  |
| start: exact-nonnegative-integer? |
| time: exact-integer?              |
+------------------------------------+
```

仕様:
X11 選択の現在の内容を Unix (または
Windows または Mac OS ではクリップボード) をエディタに挿入します。この方法は
サブクラスによってオーバーライドできるように提供されます。電話しないでください
このメソッドを直接;代わりに、paste-x-selection を呼び出します。

time 引数の詳細については、「タイム スタンプのカット アンド ペースト」を参照。もし
時間がプラットフォーム固有の時間範囲外である、
exn:fail:contract 例外が発生します。

既定の実装:
開始位置に貼り付けます。

```
+-----------------------------+
| [メソッド]                    |
|                             |
| (send a-text erase) → void? |
+-----------------------------+
```

エディタの内容を消去します。

あわせて delete も参照。

```
+-------------------------------------------+
| [メソッド]                                  |
|                                           |
| (send a-text extend-position pos) → void? |
| pos: exact-nonnegative-integer?          |
+-------------------------------------------+
```

に基づいて選択を更新します (set-position を参照)。
get-extend-end-position の結果、
get-extend-start-position、および pos。

pos が拡張開始位置と拡張終了位置の前にある場合、
次に、選択範囲は位置から拡張終了位置まで移動します。
後であれば、拡張開始位置から選択します。
posに。

このメソッドを使用して、Shift で変更された移動キーを実装します。
選択範囲を適切に拡張します。

```
+----------------------------------------------------------------+
| [メソッド]                                                       |
|                                                                |
| (send a-text find-line y [on-it]) → exact-nonnegative-integer? |
| y: real?                                                      |
| on-it: (or/c (box/c any/c) #f) = #f                           |
+----------------------------------------------------------------+
```

エディタ内の場所を指定すると、その位置の行を返します。
場所。行には 0 から始まる番号が付けられます。

実際にその行が表示されている場合、オンイットボックスは #t で埋められます。
#f でない限り、この位置にタッチするか、#f にタッチします。 (大きな
十分な y は常に最後の行番号を返しますが、
#f に設定してください。)

結果はエディタが表示されている場合にのみ有効です
(エディタの構造と用語を参照)。エディタは次の場合に表示されます。
get-admin は管理者 (#f ではない) を返します。このメソッドを呼び出すと、たとえエディタが現在リフレッシュ遅延中であっても、位置情報の再計算が強制されることがある（`refresh-delayed?` を参照）。

```
+-----------------------------------------------------------+
| [メソッド]                                                  |
|                                                           |
| (send a-text find-newline                                 |
| → (or/c exact-nonnegative-integer? #f)                    |
| direction: (or/c 'forward 'backward) = 'forward          |
| start: (or/c exact-nonnegative-integer? 'start) = 'start |
| end: (or/c exact-nonnegative-integer? 'eof) = 'eof       |
+-----------------------------------------------------------+
```

find-string と似ていますが、特に段落を検索します
Break (テキストを検索するよりも効率的である可能性があります)。

```
+-----------------------------------------------+
| [メソッド]                                      |
|                                               |
| (send a-text find-next-non-string-snip after) |
| → (or/c (is-a?/c snip%) #f)                   |
| after: (or/c (is-a?/c snip%) #f)             |
+-----------------------------------------------+
```

スニップを指定すると、エディタ内の次のスニップを返します（指定されたスニップの後）
1) それは string-snip% のインスタンスではありません。もし
#f が切り取りとして指定され、結果は最初の非文字列になります。
エディタで切り取ります (存在する場合)。文字列以外の切り取りがその後に見つからない場合は、
一部を省略すると、結果は #f になります。

```
+-------------------------------------------+
| [メソッド]                                  |
|                                           |
| (send a-text find-position                |
| → exact-nonnegative-integer?              |
| x: real?                                 |
| y: real?                                 |
| at-eol: (or/c (box/c any/c) #f) = #f     |
| on-it: (or/c (box/c any/c) #f) = #f      |
| edge-close: (or/c (box/c real?) #f) = #f |
+-------------------------------------------+
```

エディタ内の位置を指定すると、その位置を返します。
場所。

at-eol 引数の説明については、「行末のあいまいさ」を参照。
線が実際にこれに触れている場合、オンイットボックスは #t で埋められます。
位置、または #f、オンでない場合は #f です。

エッジクローズボックスには値が入力されます
ポイントがアイテムの垂直エッジにどれだけ近いかを示します
エッジクローズが#fでない限り、ポイントがアイテム上にあるとき。ポイントが厳密に言うと、
項目の左端の左側、値は -100.0 です。ポイントが または にある場合
項目の右端の右側の値は 100.0 です。それ以外の場合、値は
点が左に最も近い場合は 0 または負、点が左に最も近い場合は正
アイテムの右端に最も近い、
値の大きさは点からエッジまでの距離です
アイテムの。

結果はエディタが表示されている場合にのみ有効です
(エディタの構造と用語を参照)。エディタは次の場合に表示されます。
get-admin は管理者 (#f ではない) を返します。このメソッドを呼び出すと、たとえエディタが現在リフレッシュ遅延中であっても、位置情報の再計算が強制されることがある（`refresh-delayed?` を参照）。

```
+-------------------------------------------+
| [メソッド]                                  |
|                                           |
| (send a-text find-position-in-line        |
| → exact-nonnegative-integer?              |
| line: exact-nonnegative-integer?         |
| x: real?                                 |
| at-eol: (or/c (box/c any/c) #f) = #f     |
| on-it: (or/c (box/c any/c) #f) = #f      |
| edge-close: (or/c (box/c real?) #f) = #f |
+-------------------------------------------+
```

エディタの行内の位置を指定すると、
その場所での位置。行には 0 から始まる番号が付けられます。

at-eol 引数の説明については、「行末のあいまいさ」を参照。
実際にその行が表示されている場合、オンイットボックスは #t で埋められます。
#f でない限り、この位置にタッチするか、#f にタッチします。

については find-position を参照。
エッジクローズ。

結果はエディタが表示されている場合にのみ有効です
(エディタの構造と用語を参照)。エディタは次の場合に表示されます。
get-admin は管理者 (#f ではない) を返します。このメソッドを呼び出すと、たとえエディタが現在リフレッシュ遅延中であっても、位置情報の再計算が強制されることがある（`refresh-delayed?` を参照）。

```
+------------------------------------------------------------------+
| [メソッド]                                                         |
|                                                                  |
| (send a-text find-snip pos direction [s-pos])                    |
| → (or/c (is-a?/c snip%) #f)                                      |
| pos: exact-nonnegative-integer?                                 |
| direction: (or/c 'before-or-none 'before 'after 'after-or-none) |
| s-pos: (or/c (box/c exact-nonnegative-integer?) #f) = #f        |
+------------------------------------------------------------------+
```

指定された位置での切り取りを返すか、適切な場合は #f を返します。
スニップが見つかりません。

位置 pos が次の範囲にある場合
2 つのスニップ。方向はどのスニップを返すかを指定します。方向
次のいずれかになります。

- 'before-or-none — 前のスニップを返します。
位置、または pos が 0 の場合は #f
- 'before — 位置の前の切り取りを返します。
または pos が 0 の場合は最初の切り取り
- 'after — 位置の後のスニップを返します、または
pos が最後の位置の場合は最後のスニップ
- 'after-or-none – 後のスニップを返します。
位置、または pos が最後の位置以上の場合は #f

s-pos ボックスは、s-pos が #f でない限り、返されたスニップの開始位置で埋められます。

```
+-----------------------------------------------------------+
| [メソッド]                                                  |
|                                                           |
| (send a-text find-string                                  |
| → (or/c exact-nonnegative-integer? #f)                    |
| str: non-empty-string?                                   |
| direction: (or/c 'forward 'backward) = 'forward          |
| start: (or/c exact-nonnegative-integer? 'start) = 'start |
| end: (or/c exact-nonnegative-integer? 'eof) = 'eof       |
| get-start?: any/c = #t                                   |
| case-sensitive?: any/c = #t                              |
+-----------------------------------------------------------+
```

エディタで完全に一致する文字列を検索し、その位置を返します。
文字列が見つからない場合は、#f が返されます。

方向引数は 'forward または
'backward、前方検索または後方検索を示します
それぞれ検索してください。前方検索の場合、戻り値は
value は文字列の開始位置です。逆方向検索の場合、
終了位置が返されます。しかし、もし始めたら？です
#f の場合、文字列のもう一方の端の位置は次のようになります。
戻ってきました。

start 引数と end 引数は開始と終了を設定します。
前方検索の位置 (開始 > 終了を使用します)
後方検索）。開始が 'start の場合、検索は
選択範囲の先頭から始まります。終了が'eofの場合、
その後、検索は最後まで続行されるか (前方検索の場合)、開始されます。
(後方検索用) エディタの。

大文字と小文字を区別する場合?が #f の場合、大文字と小文字
各アルファベット文字は同等のものとして扱われます。

```
+------------------------------------------------------------------------+
| [メソッド]                                                               |
|                                                                        |
| (send a-text find-string-embedded                                      |
| → (or/c exact-nonnegative-integer? #f (cons/c (is-a?/c editor<%>)      |
| (flat-rec-contract nested-editor-search-result (or/c (cons/c (is-a?/c  |
| editor<%>) nested-editor-search-result) exact-nonnegative-integer?)))) |
| (or/c exact-nonnegative-integer?                                       |
| #f                                                                     |
| (cons/c                                                                |
| (is-a?/c editor<%>)                                                    |
| (flat-rec-contract                                                     |
| nested-editor-search-result                                            |
| (or/c (cons/c (is-a?/c editor<%>)                                      |
| nested-editor-search-result)                                           |
| exact-nonnegative-integer?))))                                         |
| str: non-empty-string?                                                |
| direction: (or/c 'forward 'backward) = 'forward                       |
| start: (or/c exact-nonnegative-integer? 'start) = 'start              |
| end: (or/c exact-nonnegative-integer? 'eof) = 'eof                    |
| get-start?: any/c = #t                                                |
| case-sensitive?: any/c = #t                                           |
| recur-inside?: (-> (is-a?/c editor-snip%) any/c) = (λ (x) #t)         |
|                                                                        |
| ```racket                                                              |
| (or/c exact-nonnegative-integer?                                       |
|       #f                                                               |
|       (cons/c                                                          |
|        (is-a?/c editor<%>)                                             |
|        (flat-rec-contract                                              |
|         nested-editor-search-result                                    |
|         (or/c (cons/c (is-a?/c editor<%>)                              |
|                       nested-editor-search-result)                     |
|               exact-nonnegative-integer?))))                           |
| ```                                                                    |
+------------------------------------------------------------------------+
```

find-string と同様ですが、埋め込みエディタでも検索できます。
車の位置を表す一連の短所ペアを返します
は、検索が行われるエディタへのパス上のエディタです。
文字列が発生し、その最終 CDR 位置は
検索結果の位置。

埋め込みエディタに遭遇するたびに、内部で再帰しますか?と呼ばれます
editor-snip% オブジェクトを使用します。内部再発の場合は？返品
#fまた、その埋め込みエディタ (およびそれに埋め込まれたエディタ) の結果
スキップされます。

パッケージ `gui-lib` のバージョン 1.80 で変更: 引数 `recursive-internals?` を追加

```
+-----------------------------------------------------------+
| [メソッド]                                                  |
|                                                           |
| (send a-text find-string-all                              |
| → (listof exact-nonnegative-integer?)                     |
| str: non-empty-string?                                   |
| direction: (or/c 'forward 'backward) = 'forward          |
| start: (or/c exact-nonnegative-integer? 'start) = 'start |
| end: (or/c exact-nonnegative-integer? 'eof) = 'eof       |
| get-start?: any/c = #t                                   |
| case-sensitive: any/c = #t                               |
+-----------------------------------------------------------+
```

find-string を使用して、出現する文字列をすべて検索します。もし
出現箇所が見つからない場合は、空のリストが返されます。引数
find-string と同じです。

```
+------------------------------------------------------------------------+
| [メソッド]                                                               |
|                                                                        |
| (send a-text find-string-embedded-all                                  |
| → (listof (or/c exact-nonnegative-integer? (cons/c (is-a?/c editor<%>) |
| (flat-rec-contract nested-editor-search-result (or/c (cons/c (is-a?/c  |
| editor<%>) nested-editor-search-result) (listof                        |
| exact-nonnegative-integer?))))))                                       |
| (listof (or/c exact-nonnegative-integer?                               |
| (cons/c                                                                |
| (is-a?/c editor<%>)                                                    |
| (flat-rec-contract                                                     |
| nested-editor-search-result                                            |
| (or/c (cons/c (is-a?/c editor<%>)                                      |
| nested-editor-search-result)                                           |
| (listof exact-nonnegative-integer?))))))                               |
| str: non-empty-string?                                                |
| direction: (or/c 'forward 'backward) = 'forward                       |
| start: (or/c exact-nonnegative-integer? 'start) = 'start              |
| end: (or/c exact-nonnegative-integer? 'eof) = 'eof                    |
| get-start?: any/c = #t                                                |
| case-sensitive: any/c = #t                                            |
| recur-inside?: (-> (is-a?/c editor-snip%) any/c) = (λ (x) #t)         |
|                                                                        |
| ```racket                                                              |
| (listof (or/c exact-nonnegative-integer?                               |
|               (cons/c                                                  |
|                (is-a?/c editor<%>)                                     |
|                (flat-rec-contract                                      |
|                 nested-editor-search-result                            |
|                 (or/c (cons/c (is-a?/c editor<%>)                      |
|                               nested-editor-search-result)             |
|                       (listof exact-nonnegative-integer?))))))         |
| ```                                                                    |
+------------------------------------------------------------------------+
```

find-string-all と似ていますが、埋め込み文字列も検索します
find-string-embedded のようなエディタ、検索結果を返す
一致したものを含むエディタのリストとして。

パッケージ `gui-lib` のバージョン 1.80 で変更: 引数 `recursive-internals?` を追加

```
+-------------------------------------------------------+
| [メソッド]                                              |
|                                                       |
| (send a-text find-wordbreak                           |
| start: (or/c (box/c exact-nonnegative-integer?) #f)  |
| end: (or/c (box/c exact-nonnegative-integer?) #f)    |
| reason: (or/c 'caret 'line 'selection 'user1 'user2) |
+-------------------------------------------------------+
```

現在のワードブレーク手順を使用して、エディタでワードブレークを検索します。
set-wordbreak-func も参照。

start 引数の内容は開始位置を指定します。
次の単語の先頭まで逆方向に検索します。それはで満たされます
見つかった単語の開始位置。開始の場合
#f、後方検索は実行されません。

end 引数の内容は開始位置を指定します。
次の単語の末尾まで前方検索します。それはで満たされます
見つかった単語の終了位置。終了の場合
#f、前方検索は実行されません。

reason 引数は、その内容に関する詳細情報を指定します。
ワードブレークは次のように使用されます。たとえば、ワードブレイクを移動するために使用される
キャレットは、改行に使用されるワードブレイクとは異なる場合があります。の
reason の可能な値は次のとおりです。

- 'caret — キャレットの移動に適した単語区切りを見つけます
- 'line — 改行に適した単語区切りを見つけます
- 'selection — 最も近い単語を選択するのに適した単語区切りを見つけます
- 'user1 — 他の (組み込みではない) 用途用
- 'user2 — 他の (組み込みではない) 用途用

理性の実際の処理は、現在の状況によって制御されます。
ワードブレイク手順; set-wordbreak-func を参照。
詳細。デフォルトのハンドラーとデフォルトのワードブレーク マップの扱い
'caret、'line、は同じ英数字
そして'selection。英数字以外、スペース、ハイフン以外
文字は改行しませんが、キャレットと選択範囲は分割します。
言葉。たとえば、カンマは、
単語の前にキャレットを移動するかダブルクリックするための前の単語
ただし、コンマは単語と同じ行に置く必要があります (そして
したがって、同じ「行ワード」内でカウントされます）。

```
+---------------------------------+
| [メソッド]                        |
|                                 |
| (send a-text flash-off) → void? |
+---------------------------------+
```

強調表示をオフにして、通常の選択範囲を再び表示します。参照してください
フラッシュオン。このメソッドを呼び出しても効果はありません
点滅がすでにオフになっているとき。

```
+--------------------------------------------+
| [メソッド]                                   |
|                                            |
| (send a-text flash-on                      |
| start: exact-nonnegative-integer?         |
| end: exact-nonnegative-integer?           |
| at-eol?: any/c = #f                       |
| scroll?: any/c = #t                       |
| timeout: exact-nonnegative-integer? = 500 |
+--------------------------------------------+
```

エディタ内の領域を変更せずに一時的にハイライトします。
現在の選択範囲。

at-eol? については、「行末のあいまいさ」を参照。。もし
スクロール？ #f ではない場合、エディタの表示はスクロールされます
必要に応じて、強調表示された領域を表示します。タイムアウトが大きい場合
0 より大きい場合、ハイライトは自動的にオフになります。
指定されたミリ秒数。

あわせて flash-off も参照。

```
+-------------------------------------+
| [メソッド]                            |
|                                     |
| (send a-text get-anchor) → boolean? |
+-------------------------------------+
```

選択範囲が現在自動拡張中の場合は、#t を返します。参照
アンカーもセットします。

```
+-----------------------------------------+
| [メソッド]                                |
|                                         |
| (send a-text get-autowrap-bitmap-width) |
| → (and/c real? (not/c negative?))       |
+-----------------------------------------+
```

最後に set-autowrap-bitmap に渡されたビットマップの幅を返します。
それともゼロ？ビットマップが set-autowrap-bitmap に渡されていない場合、または
#f が最後に渡された場合。

```
+-------------------------------------+
| [メソッド]                            |
|                                     |
| (send a-text get-between-threshold) |
| → (and/c real? (not/c negative?))   |
+-------------------------------------+
```

ユーザーのクリックの意味を決定するために使用される量を返します。もし
クリックが 2 つの位置の間のしきい値内に収まる
項目間のスペースをクリックすると、
どちらかの項目ではなく、項目を選択します。

あわせて set-between-threshold も参照。

```
+-------------------------------------------+
| [メソッド]                                  |
|                                           |
| (send a-text get-character start) → char? |
| start: exact-nonnegative-integer?        |
+-------------------------------------------+
```

位置に続く文字を返します
始めます。文字は非フラット化に対応します
編集者からのテキスト。

開始値が最後の値以上の場合
位置、#\nul が返されます。

```
+-------------------------------------------------------------+
| [メソッド]                                                    |
|                                                             |
| (send a-text get-end-position) → exact-nonnegative-integer? |
+-------------------------------------------------------------+
```

現在の選択範囲の終了位置を返します。参照
ポジションも取得します。

```
+-----------------------------------------+
| [メソッド]                                |
|                                         |
| (send a-text get-extend-start-position) |
| → exact-nonnegative-integer?            |
+-----------------------------------------+
```

選択範囲が拡張されている場合、「拡張」領域の先頭を返します。
現在、シフトキーとカーソル移動キーなどを使用して拡張されています。
それ以外の場合は、get-start-position と同じ値を返します。

```
+---------------------------------------+
| [メソッド]                              |
|                                       |
| (send a-text get-extend-end-position) |
| → exact-nonnegative-integer?          |
+---------------------------------------+
```

選択範囲が拡張されている場合、「拡張」領域の先頭を返します。
現在、シフトキーとカーソル移動キーなどを使用して拡張されています。
それ以外の場合は、get-end-position と同じ値を返します。

```
+-----------------------------------------+
| [メソッド]                                |
|                                         |
| (send a-text get-file-format)           |
| → (or/c 'standard 'text 'text-force-cr) |
+-----------------------------------------+
```

最後に保存またはロードされたファイルの形式を返します。
編集者。 「ロードファイル」も参照。

```
+-----------------------------------+
| [メソッド]                          |
|                                   |
| (send a-text get-line-spacing)    |
| → (and/c real? (not/c negative?)) |
+-----------------------------------+
```

エディタによって各行間に挿入されたスペースを返します。これ
間隔は、報告される各行の高さに含まれます。

```
+---------------------------------------------+
| [メソッド]                                    |
|                                             |
| (send a-text get-overwrite-mode) → boolean? |
+---------------------------------------------+
```

エディタが上書きモードの場合は #t を返し、エディタが上書きモードの場合は #f を返します。
それ以外の場合は。上書きモードは、on-default-char が挿入文字のキーボード入力を処理する方法にのみ影響します。参照
上書きモードも設定します。

```
+---------------------------------+
| [メソッド]                        |
|                                 |
| (send a-text get-padding)       |
| (and/c real? (not/c negative?)) |
| (and/c real? (not/c negative?)) |
| (and/c real? (not/c negative?)) |
| (and/c real? (not/c negative?)) |
+---------------------------------+
```

エディタの左、上、右、下のパディングを返します。
側面（この順序で）。

あわせて set-padding も参照。

```
+---------------------------------------------------------+
| [メソッド]                                                |
|                                                         |
| (send a-text get-position start [end]) → void?          |
| start: (or/c (box/c exact-nonnegative-integer?) #f)    |
| end: (or/c (box/c exact-nonnegative-integer?) #f) = #f |
+---------------------------------------------------------+
```

現在の選択範囲を位置で返します。もし
何も選択されていない場合、開始と終了は
同じ番号であり、その番号が挿入ポイントの位置になります。

「開始位置の取得」も参照。
そして終了位置を取得します。

start が #f でない限り、開始ボックスには選択範囲の開始位置が入力されます。
終了ボックスは、終了が#fでない限り、選択範囲の終了位置で埋められます。

```
+-----------------------------------------+
| [メソッド]                                |
|                                         |
| (send a-text get-region-data start end) |
| → (or/c (is-a?/c editor-data%) #f)      |
| start: exact-nonnegative-integer?      |
| end: exact-nonnegative-integer?        |
+-----------------------------------------+
```

指定された領域に関連付けられた追加データを取得します。参照
詳細については、エディタ データを参照。

エディタ全体がファイルに保存される場合、このメソッドは呼び出されません。
ファイル。このような場合、情報はヘッダーまたは
フッター; 「グローバル データ: ヘッダーとフッター」を参照。

このメソッドはオーバーライドされることを目的としています。デフォルトの set-region-data メソッドには、取得する情報は保存されません。
この方法。

```
+-----------------------------------+
| [メソッド]                          |
|                                   |
| (send a-text get-revision-number) |
| → (and/c real? (not/c negative?)) |
+-----------------------------------+
```

エディタが操作されるたびに増加する不正確な数値を返します。
次のいずれかの方法で変更されます: スニップが挿入されます (「
after-insert)、スニップの削除 (after-delete を参照)、スニップの分割 (after-split-snip を参照)、スニップのマージ (after-merge-snips を参照)、またはスニップのカウントの変更 (これはまれです。を参照)
語った）。

```
+----------------------------------------+
| [メソッド]                               |
|                                        |
| (send a-text get-snip-position snip)   |
| → (or/c exact-nonnegative-integer? #f) |
| snip: (is-a?/c snip%)                 |
+----------------------------------------+
```

指定されたスニップの開始位置を返します。
切り取りがこのエディタにない場合は、#f。

```
+----------------------------------------------------+
| [メソッド]                                           |
|                                                    |
| (send a-text get-snip-position-and-location        |
| snip: (is-a?/c snip%)                             |
| pos: (or/c (box/c exact-nonnegative-integer?) #f) |
| x: (or/c (box/c real?) #f) = #f                   |
| y: (or/c (box/c real?) #f) = #f                   |
+----------------------------------------------------+
```

このメソッドは final であり、オーバーライドできない。

エディタ内のスニップの位置と左上の位置を取得します
コーディネート。スニップが見つかった場合、戻り値は #t です。
それ以外の場合は #f 。

pos が #f でない限り、pos ボックスにはスニップの開始位置が入力されます。
x ボックスは、x が #f でない限り、エディタ座標の切り取りの左の位置で埋められます。
y ボックスは、y が #f でない限り、エディタ座標の切り取りの上部の位置で埋められます。

位置情報要求時：結果はエディタ表示時のみ有効
(エディタの構造と用語を参照)。エディタは次の場合に表示されます。
get-admin は管理者 (#f ではない) を返します。このメソッドを呼び出すと、たとえエディタが現在リフレッシュ遅延中であっても、位置情報の再計算が強制されることがある（`refresh-delayed?` を参照）。

```
+---------------------------------------------------------------+
| [メソッド]                                                      |
|                                                               |
| (send a-text get-start-position) → exact-nonnegative-integer? |
+---------------------------------------------------------------+
```

現在の選択範囲の開始位置を返します。こちらも参照
位置を取得します。

```
+--------------------------------------------+
| [メソッド]                                   |
|                                            |
| (send a-text get-styles-sticky) → boolean? |
+--------------------------------------------+
```

テキストエディタの通常モードでは、スタイル設定は固定されます。と
スティッキー スタイル、文字列または文字がエディタに挿入されるとき、
挿入ポイント (または
テキストがテキストに挿入される場合、挿入ポイントを含むスニップ
終了文字列の切り取り)。あるいは、スタイルを変更する場合は、
キャレット位置にスタイルを設定するために呼び出されます (
は範囲ではありません)、スタイルは記憶されます。エディタがそうでない場合
テキストがキャレットに挿入される前に変更された場合、テキストは
覚えたスタイル。

非スティッキー スタイルでは、エディタに挿入されたテキストは常に
エディタのスタイルリスト内の style は、default-style-name で指定されます。

あわせて set-styles-sticky も参照。

```
+------------------------------------------------------------+
| [メソッド]                                                   |
|                                                            |
| (send a-text get-tabs                                      |
| length: (or/c (box/c exact-nonnegative-integer?) #f) = #f |
| tab-width: (or/c (box/c real?) #f) = #f                   |
| in-units: (or/c (box/c any/c) #f) = #f                    |
+------------------------------------------------------------+
```

現在のタブ位置の配列をリストとして返します。

長さボックスには、タブ配列の長さが入力されます (したがって、返される長さは
リスト)、長さが #f でない限り。
タブ幅ボックスには、タブを超えるタブに使用される幅が入力されます。
tab-width が #f でない限り、タブ配列の終わり。
タブが指定されている場合、単位内ボックスには #t が入力されます。
キャンバス単位、またはスペース幅で指定されている場合は #f (単位内が #f でない場合)。

こちらも参照
タブを設定します。

```
+-----------------------------------------------------+
| [メソッド]                                            |
|                                                     |
| (send a-text get-text                               |
| start: exact-nonnegative-integer? = 0              |
| end: (or/c exact-nonnegative-integer? 'eof) = 'eof |
| flattened?: any/c = #f                             |
| force-cr?: any/c = #f                              |
+-----------------------------------------------------+
```

テキストを最初から最後まで取得します。終了の場合
'eof、開始から終了までの内容が返されます。
エディタの終わり。

平らにしたら？が #f ではない場合、フラット化されたテキストが返されます。
フラット化と非フラット化についての説明は、「フラット化されたテキスト」を参照。
テキスト。

Force-cr の場合は? #f はフラット化されていませんか？ではありません
#f の場合、(ワードラップによる) 自動改行は次のようになります。
実際の改行として戻り文字列に書き込まれます。

```
+-----------------------------------+
| [メソッド]                          |
|                                   |
| (send a-text get-top-line-base)   |
| → (and/c real? (not/c negative?)) |
+-----------------------------------+
```

エディタの上部から配置までの距離を返します。
トップラインのベースライン。この方法は主に次の場合に使用されます。
editor は別のエディタ内のアイテムです。
報告されるベースライン距離には、編集者の距離が含まれます。
上部のパディング (set-padding を参照)。

結果はエディタが表示されている場合にのみ有効です
(エディタの構造と用語を参照)。エディタは次の場合に表示されます。
get-admin は管理者 (#f ではない) を返します。 text% オブジェクトの場合、このメソッドを呼び出すと位置の再計算が強制される可能性があります。
エディタが現在遅延している場合でも、エディタに最大幅が設定されている場合の情報
リフレッシュします （`refresh-delayed?` を参照）。

```
+------------------------------------------------------+
| [メソッド]                                             |
|                                                      |
| (send a-text get-visible-line-range                  |
| start: (or/c (box/c exact-nonnegative-integer?) #f) |
| end: (or/c (box/c exact-nonnegative-integer?) #f)   |
| all?: any/c = #t                                    |
+------------------------------------------------------+
```

現在表示されている（または部分的に）行の範囲を返します。
表示されます）。行には 0 から始まる番号が付けられます。

開始ボックスは、開始が #f でない限り、ユーザーに表示される最初の行で埋められます。
終了ボックスは、終了が #f でない限り、ユーザーに表示される最後の行で埋められます。

エディタが複数のキャンバスで表示されている場合は、すべてのキャンバスが表示されますか?です
#t の場合、計算された範囲には、すべての目に見えるすべての線が含まれます。
と表示されます。それ以外の場合、範囲には表示されている行のみが含まれます。
現在の表示。

結果はエディタが表示されている場合にのみ有効です
(エディタの構造と用語を参照)。エディタは次の場合に表示されます。
get-admin は管理者 (#f ではない) を返します。このメソッドを呼び出すと、たとえエディタが現在リフレッシュ遅延中であっても、位置情報の再計算が強制されることがある（`refresh-delayed?` を参照）。

```
+------------------------------------------------------+
| [メソッド]                                             |
|                                                      |
| (send a-text get-visible-position-range              |
| start: (or/c (box/c exact-nonnegative-integer?) #f) |
| end: (or/c (box/c exact-nonnegative-integer?) #f)   |
| all?: any/c = #t                                    |
+------------------------------------------------------+
```

現在表示されている位置の範囲を返します（または
部分的に表示されます）。

開始ボックスは、開始が #f でない限り、ユーザーに表示される最初の位置で埋められます。
終了ボックスは、終了が #f でない限り、ユーザーに表示される最後の位置で埋められます。

エディタが複数のキャンバスで表示されている場合は、すべてのキャンバスが表示されますか?です
#t の場合、計算された範囲には、表示されているすべての位置が含まれます。
すべてのディスプレイ。それ以外の場合、範囲には表示されるもののみが含まれます。
現在の表示内の位置。

結果はエディタが表示されている場合にのみ有効です
(エディタの構造と用語を参照)。エディタは次の場合に表示されます。
get-admin は管理者 (#f ではない) を返します。このメソッドを呼び出すと、たとえエディタが現在リフレッシュ遅延中であっても、位置情報の再計算が強制されることがある（`refresh-delayed?` を参照）。

```
+---------------------------------------------+
| [メソッド]                                    |
|                                             |
| (send a-text get-wordbreak-map)             |
| → (or/c (is-a?/c editor-wordbreak-map%) #f) |
+---------------------------------------------+
```

標準のワードブレイクで使用されるワードブレイクマップを返します。
機能。 set-wordbreak-map および
詳細については、editor-wordbreak-map% を参照。

```
+----------------------------------------------------------------+
| [メソッド]                                                       |
|                                                                |
| (send a-text grapheme-position n) → exact-nonnegative-integer? |
| n: exact-nonnegative-integer?                                 |
+----------------------------------------------------------------+
```

最初の要素を形成するエディタ内の項目の数を返します。
n 書記素。または、同様に、
書記素ベースの位置から項目ベースの位置へ。

パッケージ `gui-lib` のバージョン 1.67 で追加。

```
+----------------------------------------+
| [メソッド]                               |
|                                        |
| (send a-text hide-caret hide?) → void? |
| hide?: any/c                          |
+----------------------------------------+
```

エディタにキーボードがあるときにキャレットを表示するかどうかを決定します。
集中します。

隠れたら？ #f ではない場合、キャレットまたは選択範囲が強調表示されます
編集者向けに描画されません。編集者は引き続き
キーボード フォーカスはありますが、フォーカスを示すキャレットは描画されません。

「キャレット非表示?」も参照。そしてロックします。

```
+---------------------------------------------------------------------------+
| [メソッド]                                                                  |
|                                                                           |
| (send a-text insert                                                       |
| str: string?                                                             |
| start: exact-nonnegative-integer?                                        |
| end: (or/c exact-nonnegative-integer? 'same) = 'same                     |
| scroll-ok?: any/c = #t                                                   |
| join-graphemes?: any/c = #f                                              |
| (send a-text insert n str start [end scroll-ok? join-graphemes?]) → void? |
| (send a-text insert                                                       |
| n: (and/c exact-nonnegative-integer? (<=/c (string-length str)))         |
| (and/c exact-nonnegative-integer?                                         |
| (<=/c (string-length str)))                                               |
| str: string?                                                             |
| start: exact-nonnegative-integer?                                        |
| end: (or/c exact-nonnegative-integer? 'same) = 'same                     |
| scroll-ok?: any/c = #t                                                   |
| join-graphemes?: any/c = #f                                              |
| (send a-text insert str) → void?                                          |
| str: string?                                                             |
| (send a-text insert n str [join-graphemes?]) → void?                      |
| n: (and/c exact-nonnegative-integer? (<=/c (string-length str)))         |
| (and/c exact-nonnegative-integer?                                         |
| (<=/c (string-length str)))                                               |
| str: string?                                                             |
| join-graphemes?: any/c = #f                                              |
| (send a-text insert snip start [end scroll-ok?]) → void?                  |
| (send a-text insert                                                       |
| snip: (is-a?/c snip%)                                                    |
| start: exact-nonnegative-integer?                                        |
| end: (or/c exact-nonnegative-integer? 'same) = 'same                     |
| scroll-ok?: any/c = #t                                                   |
| (send a-text insert snip) → void?                                         |
| snip: (is-a?/c snip%)                                                    |
| (send a-text insert char) → void?                                         |
| char: char?                                                              |
| (send a-text insert char start [end]) → void?                             |
| char: char?                                                              |
| start: exact-nonnegative-integer?                                        |
| end: (or/c exact-nonnegative-integer? 'same) = 'same                     |
|                                                                           |
| ```racket                                                                 |
| (and/c exact-nonnegative-integer?                                         |
|        (<=/c (string-length str)))                                        |
| ```                                                                       |
|                                                                           |
| ```racket                                                                 |
| (and/c exact-nonnegative-integer?                                         |
|        (<=/c (string-length str)))                                        |
| ```                                                                       |
+---------------------------------------------------------------------------+
```

editor<%> での挿入をオーバーライドします。

テキストまたはスニップを a-text の位置に挿入します
始めます。 n が指定された場合、最初の
str の n 文字が挿入されます。

スニップがある場合：スニップは挿入できません。
複数のエディタ、または 1 つのエディタ内で複数回。として
スニップが挿入されると、その現在のスタイルが次のスタイルに変換されます。
エディタのスタイルリスト。 「変換」も参照。

char が指定されている場合: 文字挿入メソッドの複数の呼び出しはグループ化されます。
このケースのメソッドは通常使用されるため、元に戻す目的で使用されます。
ユーザーのキーストロークを処理するため。ただし、この元に戻すグループ化機能
によって実行される元に戻すグループ化を妨げます。
編集開始シーケンスと
編集シーケンスの終了なので、文字列の挿入
取り消し可能な編集シーケンスでは、代わりにメソッドを使用する必要があります。

start が指定されていない場合、現在の選択範囲の start は次のようになります。
使用されています。現在の選択範囲がアイテムの範囲をカバーしている場合、
選択したテキストが char に置き換えられます。セレクションのスタートです
終了位置は挿入されたファイルの最後に移動されます。
キャラクター。

end が指定されておらず、デフォルトがない場合、
現在の選択範囲の端が使用されます。それ以外の場合、end でない場合
'same、挿入された値は、からの領域を置き換えます。
最初から最後まで、選択範囲は最後まで残ります
挿入されたテキストの。それ以外の場合、挿入位置が
選択範囲の開始/終了位置より前、またはそれと等しい、
次に、選択範囲の開始/終了位置が ずつ増分されます。
strの長さ。

スクロールしても大丈夫ですか？は #f ではなく、start は
現在の選択範囲の開始位置と同じであれば、
エディタの表示がスクロールされて新しい選択内容が表示されます
位置。

書記素に参加する場合?が提供されているが #f ではない、または
挿入する文字が指定されている場合、前後の文字が
挿入されたコンテンツは、
挿入されたコンテンツの先頭または末尾、それらの文字は
挿入されたコンテンツの先頭と末尾に効果的に追加されます。
吸収された文字をカバーするように挿入範囲が調整されます。として
その結果、書記素を形成する文字は確実に配置されます。
書記素が適切にレンダリングされるように、同じ切り取りを行います。それ
調整により、挿入されたスタイルが効果的に変更される可能性があります。
コンテンツ、または新しく形成されたコンテンツに関連する既存のコンテンツ
書記素クラスター

あわせて get-styles-sticky も参照。

```
+-------------------------------------------+
| [メソッド]                                  |
|                                           |
| (send a-text kill [time]) → void?         |
| time: exact-integer? = 0                 |
| (send a-text kill time start end) → void? |
| time: exact-integer?                     |
| start: exact-nonnegative-integer?        |
| end: exact-nonnegative-integer?          |
+-------------------------------------------+
```

editor<%> で kill をオーバーライドします。

指定された領域のテキストを切り取ります。始まりと終わりなら
が指定されていない場合は、選択された領域とすべての空白が
行末がカットされます。空白のみが存在する場合は改行もカットされます
選択範囲と行末の間。

time 引数の詳細については、「タイム スタンプのカット アンド ペースト」を参照。もし
時間がプラットフォーム固有の時間範囲外である、
exn:fail:contract 例外が発生します。

```
+------------------------------------------------------+
| [メソッド]                                             |
|                                                      |
| (send a-text last-line) → exact-nonnegative-integer? |
+------------------------------------------------------+
```

エディタの最後の行の番号を返します。行には番号が付けられています
0 から始まるので、これは行数より 1 つ減ります。
エディタで。

`paragraph-start-position`も参照。
段落を操作します (明示的な改行文字によって決定されます)
行の代わりに (両方の明示的な改行によって決定されます)
文字と自動行折り返し)。

このメソッドを呼び出すと、エディタに最大幅が設定されている場合、たとえエディタが現在リフレッシュ遅延中であっても、位置情報の再計算が強制されることがある（`refresh-delayed?` を参照）。エディタが表示されておらず、かつ最大幅を持つ場合、行区切りは `line-start-position` と同様に計算される（表示がなく最大幅がある場合の特別な扱い）。

```
+-----------------------------------------------------------+
| [メソッド]                                                  |
|                                                           |
| (send a-text last-paragraph) → exact-nonnegative-integer? |
+-----------------------------------------------------------+
```

エディタ内の最後の段落の番号を返します。段落は
0 から始まる番号が付けられているため、これは
エディタの段落数。

このメソッドを呼び出すと、エディタに最大幅が設定されている場合、たとえエディタが現在リフレッシュ遅延中であっても、位置情報の再計算が強制されることがある（`refresh-delayed?` を参照）。

```
+----------------------------------------------------------+
| [メソッド]                                                 |
|                                                          |
| (send a-text last-position) → exact-nonnegative-integer? |
+----------------------------------------------------------+
```

エディタ内の最後の選択位置を返します。これは
エディタ内のアイテムの数も表示されます。

```
+-----------------------------------+
| [メソッド]                          |
|                                   |
| (send a-text line-end-position    |
| → exact-nonnegative-integer?      |
| line: exact-nonnegative-integer? |
| visible?: any/c = #t             |
+-----------------------------------+
```

指定された行の最後の位置を返します。行には 0 から始まる番号が付けられます。

line-1 の行数が少ない場合は、行の終わりが
最後の行が返されます。 line が 0 未満の場合、終了
最初の行の部分が返されます。

行が目に見えない項目 (
改行) と表示されますか? #f ではありません、最初です
非表示の項目の前の位置
戻ってきました。

`paragraph-start-position`も参照。
段落を操作します (明示的な改行文字によって決定されます)
行の代わりに (両方の明示的な改行によって決定されます)
文字と自動行折り返し)。

このメソッドを呼び出すと、エディタに最大幅が設定されている場合、たとえエディタが現在リフレッシュ遅延中であっても、位置情報の再計算が強制されることがある（`refresh-delayed?` を参照）。エディタが表示されておらず、かつ最大幅を持つ場合、行区切りは `line-start-position` と同様に計算される（表示がなく最大幅がある場合の特別な扱い）。

```
+----------------------------------------------------------+
| [メソッド]                                                 |
|                                                          |
| (send a-text line-length i) → exact-nonnegative-integer? |
| i: exact-nonnegative-integer?                           |
+----------------------------------------------------------+
```

指定されたアイテムの数を返します
ライン。行には 0 から始まる番号が付けられます。

このメソッドを呼び出すと、エディタに最大幅が設定されている場合、たとえエディタが現在リフレッシュ遅延中であっても、位置情報の再計算が強制されることがある（`refresh-delayed?` を参照）。エディタが表示されておらず、かつ最大幅を持つ場合、行区切りは `line-start-position` と同様に計算される（表示がなく最大幅がある場合の特別な扱い）。

```
+-------------------------------------------------+
| [メソッド]                                        |
|                                                 |
| (send a-text line-location line [top?]) → real? |
| line: exact-nonnegative-integer?               |
| top?: any/c = #t                               |
+-------------------------------------------------+
```

行番号を指定すると、その行の位置を返します。行には 0 から始まる番号が付けられます。

トップなら？は #f ではありません。
行の先頭が返されます。それ以外の場合は、
行の一番下が返されます。

`paragraph-start-position`も参照。
段落を操作します (明示的な改行文字によって決定されます)
行の代わりに (両方の明示的な改行によって決定されます)
文字と自動行折り返し)。

結果はエディタが表示されている場合にのみ有効です
(エディタの構造と用語を参照)。エディタは次の場合に表示されます。
get-admin は管理者 (#f ではない) を返します。このメソッドを呼び出すと、たとえエディタが現在リフレッシュ遅延中であっても、位置情報の再計算が強制されることがある（`refresh-delayed?` を参照）。

```
+-----------------------------------------------------------------+
| [メソッド]                                                        |
|                                                                 |
| (send a-text line-paragraph start) → exact-nonnegative-integer? |
| start: exact-nonnegative-integer?                              |
+-----------------------------------------------------------------+
```

その行を含む段落の段落番号を返します。
行には 0 から始まる番号が付けられます。段落には 0 から始まる番号が付けられます。

このメソッドを呼び出すと、エディタに最大幅が設定されている場合、たとえエディタが現在リフレッシュ遅延中であっても、位置情報の再計算が強制されることがある（`refresh-delayed?` を参照）。エディタが表示されておらず、かつ最大幅を持つ場合、行区切りは `line-start-position` と同様に計算される（表示がなく最大幅がある場合の特別な扱い）。

```
+-----------------------------------+
| [メソッド]                          |
|                                   |
| (send a-text line-start-position  |
| → exact-nonnegative-integer?      |
| line: exact-nonnegative-integer? |
| visible?: any/c = #t             |
+-----------------------------------+
```

指定された行の最初の位置を返します。行には 0 から始まる番号が付けられます。

line-1 行より少ない場合は、
最後の行が返されます。 line が 0 未満の場合、
最初の行の先頭が返されます。

ラインが目に見えない項目から始まって見える場合は?ではありません
#f、非表示アイテムを通過した最初の位置は
戻ってきました。

`paragraph-start-position`も参照。
段落を操作します (明示的な改行文字によって決定されます)
行の代わりに (両方の明示的な改行によって決定されます)
文字と自動行折り返し)。

このメソッドを呼び出すと、エディタに最大幅が設定されている場合、たとえエディタが現在リフレッシュ遅延中であっても、位置情報の再計算が強制されることがある（`refresh-delayed?` を参照）。

次の条件に該当する場合、行を計算するには:

- エディタは表示されません (エディタの構造と用語を参照)。
- エディタの最大幅が設定されており、
- エディタは一度も閲覧されていません

この場合、このメソッドはエディタの最大幅と自動幅を無視します。
改行を暗示している可能性があります。上記の条件のうち最初の 2 つが当てはまる場合
が true で、エディタが以前に表示されていた場合、このメソッドは
最新の表示からの改行を使用します。
編集者。 (表示シフト改行以降の挿入または削除)
アイテムと同じようにエディタ内で。)

```
+---------------------------------------------------+
| [メソッド]                                          |
|                                                   |
| (send a-text move-position                        |
| code: (or/c 'home 'end 'right 'left 'up 'down)   |
| extend?: any/c = #f                              |
| kind: (or/c 'simple 'word 'page 'line) = 'simple |
+---------------------------------------------------+
```

現在の選択範囲を移動します。

コードに指定できる値は次のとおりです。

- 'home — ファイルの先頭に移動します
- 'end — ファイルの最後に移動します
- 'right — 右に移動
- 'left — 左に移動
- 'up — 上に移動
- 'down — 下に移動します

延長したら？ #f ではない場合、選択範囲は
移動ではなく拡張されました。アンカリングがオンの場合 (get-anchor および set-anchor を参照)、extend?です
実質的に#tを強制されます。 get-extend-start-position も参照。
そして get-extend-end-position を取得します。

kind に指定できる値は次のとおりです。

- 'simple — 1 つの書記素または行を移動します
- 'word — 'right または 'left で動作します
- 'page — 'up または 'down で動作します
- 'line — 'right または 'left で動作します。行の先頭または末尾に移動します

あわせて set-position も参照。

パッケージ `gui-lib` のバージョン 1.67 で変更: 「移動するシンプルモード」を変更しました
項目の代わりに書記素によって左または右に。

```
+-------------------------------------------------+
| [メソッド]                                        |
|                                                 |
| (send a-text on-change-style start len) → void? |
| start: exact-nonnegative-integer?              |
| len: exact-nonnegative-integer?                |
+-------------------------------------------------+
```

このメソッドは augment で拡張する。

仕様:
エディタの特定の範囲でスタイルが変更される前に呼び出されます。
スタイル変更後?ことを確認するために呼び出されます。
変更は大丈夫です。変更後のスタイルメソッドは、
変更が完了した後に呼び出されることが保証されています。

このメソッドの呼び出し中、エディタは書き込みのために内部的にロックされます。
(「内部エディタのロック」も参照)。使用する
必要に応じて、after-change-style を使用してエディタを変更します。

あわせて on-edit-sequence も参照。

既定の実装:
何もしない。

```
+---------------------------------------------+
| [メソッド]                                    |
|                                             |
| (send a-text on-default-char event) → void? |
| event: (is-a?/c key-event%)                |
+---------------------------------------------+
```

editor<%> の on-default-char をオーバーライドします。

以下を処理します。

- 削除とバックスペース — 削除を呼び出します。
- 矢印キー、Page Up、Page Down、Home、End (含む)
シフトされたバージョン) — 選択位置を移動します
移動位置。
- 範囲 (integer->char32) 内のその他の文字
(integer->char255) — 文字を
エディタ (書記素結合モード、挿入を参照)。

通常、エディタの editor-canvas% はマウスを処理することに注意してください。
ホイール イベント ( on-char も参照)。

パッケージ `gui-lib` のバージョン 1.67 で変更: 使用する文字挿入を変更しました
書記素結合モード。

```
+----------------------------------------------+
| [メソッド]                                     |
|                                              |
| (send a-text on-default-event event) → void? |
| event: (is-a?/c mouse-event%)               |
+----------------------------------------------+
```

editor<%> の on-default-event をオーバーライドします。

クリックバックのクリックを追跡します (set-clickback を参照)。
選択を変更します。イベント中は注意してください
キャレットを所有するスニップにディスパッチし、キャレットのクリックを検出します。
このメソッドを呼び出す前にイベント処理を切り取ります。

- クリックバック領域をクリックすると、クリックバックの追跡が開始されます。見る
詳細については、set-clickback を参照。上を移動する
クリックバックするとマウス カーソルの形状が変わります。
- 他の場所をクリックすると、キャレットが最も近い位置に移動します
アイテムの間。 Shift キーを押しながらクリックすると、現在の選択範囲が拡張されます。
- ドラッグすると選択範囲が拡張され、可能であればスクロールします。
選択範囲がエディタの表示領域の外にドラッグされます。

```
+-------------------------------------------+
| [メソッド]                                  |
|                                           |
| (send a-text on-delete start len) → void? |
| start: exact-nonnegative-integer?        |
| len: exact-nonnegative-integer?          |
+-------------------------------------------+
```

このメソッドは augment で拡張する。

仕様:
can-delete の後、エディタから範囲が削除される前に呼び出されますか?削除が正常であることを確認するために呼び出されます。の
after-delete メソッドは後で呼び出されることが保証されています
削除が完了しました。

start 引数は開始位置を指定します
削除する範囲の。 len 引数は、次の数を指定します。
削除する項目 (つまり、start+len は
削除する範囲の終了位置)。

エディタは、この呼び出し中に書き込みのために内部的にロックされます。
メソッド (「内部エディタのロック」も参照)。削除後を使用して、
必要に応じてエディタを変更します。

あわせて on-edit-sequence も参照。

既定の実装:
何もしない。

```
+-------------------------------------------+
| [メソッド]                                  |
|                                           |
| (send a-text on-insert start len) → void? |
| start: exact-nonnegative-integer?        |
| len: exact-nonnegative-integer?          |
+-------------------------------------------+
```

このメソッドは augment で拡張する。

仕様:
項目がエディタに挿入される前、挿入後に呼び出されます。
挿入できますか？挿入が行われたことを確認するために呼び出されます。
わかりました。挿入後のメソッドは確実に呼び出されます。
挿入が完了した後。

start 引数は、挿入の位置を指定します。の
len 引数は、
挿入する項目。

エディタは、この呼び出し中に書き込みのために内部的にロックされます。
メソッド (「内部エディタのロック」も参照)。挿入後を使用して、
必要に応じてエディタを変更します。

あわせて on-edit-sequence も参照。

既定の実装:
何もしない。

```
+-----------------------------------------------------------+
| [メソッド]                                                  |
|                                                           |
| (send a-text on-new-string-snip) → (is-a?/c string-snip%) |
+-----------------------------------------------------------+
```

仕様:
文字列または文字が挿入されると、insert によって呼び出されます。
エディタに入力すると、このメソッドは新しいインスタンスを作成して返します。
string-snip% は、挿入されたテキストを保存します。返された文字列の切り取り
は空です (つまり、そのカウントはゼロです)。

既定の実装:
string-snip% インスタンスを返します。

```
+-----------------------------------------------------+
| [メソッド]                                            |
|                                                     |
| (send a-text on-new-tab-snip) → (is-a?/c tab-snip%) |
+-----------------------------------------------------+
```

仕様:
tab-snip% の新しいインスタンスを作成して返し、
挿入されたタブ。返されたタブ スニップは空です (つまり、そのカウントは
はゼロです）。

既定の実装:
tab-snip% インスタンスを返します。

```
+---------------------------------+
| [メソッド]                        |
|                                 |
| (send a-text on-reflow) → void? |
+---------------------------------+
```

このメソッドは augment で拡張する。

仕様: 場所が変更された後に呼び出され、エディタ用に再計算されます。
既定の実装:
何もしません。

```
+----------------------------------------------+
| [メソッド]                                     |
|                                              |
| (send a-text on-set-size-constraint) → void? |
+----------------------------------------------+
```

このメソッドは augment で拡張する。

仕様:
エディタの高さまたは幅の最大値または最小値が設定される前に呼び出されます。
can-set-size-constraint 後に変更されましたか?に呼ばれます
変更が適切であることを確認します。 after-set-size-constraint メソッドは、次の後に呼び出されることが保証されています。
変更が完了しました。

(このコールバック メソッドが提供されるのは、エディタの最大値を設定するためです。
幅により、行がソフト改行でリフローされる可能性があります。)

あわせて on-edit-sequence も参照。

既定の実装:
何もしない。

```
+--------------------------------------------+
| [メソッド]                                   |
|                                            |
| (send a-text paragraph-end-line paragraph) |
| → exact-nonnegative-integer?               |
| paragraph: exact-nonnegative-integer?     |
+--------------------------------------------+
```

指定された段落の終了行を返します。段落には 0 から始まる番号が付けられます。行には 0 から始まる番号が付けられます。

このメソッドを呼び出すと、エディタに最大幅が設定されている場合、たとえエディタが現在リフレッシュ遅延中であっても、位置情報の再計算が強制されることがある（`refresh-delayed?` を参照）。エディタが表示されておらず、かつ最大幅を持つ場合、行区切りは `line-start-position` と同様に計算される（表示がなく最大幅がある場合の特別な扱い）。

```
+----------------------------------------+
| [メソッド]                               |
|                                        |
| (send a-text paragraph-end-position    |
| → exact-nonnegative-integer?           |
| paragraph: exact-nonnegative-integer? |
| visible?: any/c = #t                  |
+----------------------------------------+
```

指定された段落の終了位置を返します。段落には 0 から始まる番号が付けられます。

段落が段落-1 よりも少ない場合、
最後の段落の終わりが返されます。段落が少ない場合
0 より大きい場合は、最初の段落の終わりが返されます。

段落が非表示項目 (改行など) で終わっている場合
そして見える？ #f、最初の位置ではありません
目に見えないアイテムが返される前に。

```
+----------------------------------------------+
| [メソッド]                                     |
|                                              |
| (send a-text paragraph-start-line paragraph) |
| → exact-nonnegative-integer?                 |
| paragraph: exact-nonnegative-integer?       |
+----------------------------------------------+
```

指定された段落の開始行を返します。段落の場合
最も大きい番号の段落より大きく、その後は編集者の終わり
位置が返されます。段落には 0 から始まる番号が付けられます。行には 0 から始まる番号が付けられます。

このメソッドを呼び出すと、エディタに最大幅が設定されている場合、たとえエディタが現在リフレッシュ遅延中であっても、位置情報の再計算が強制されることがある（`refresh-delayed?` を参照）。エディタが表示されておらず、かつ最大幅を持つ場合、行区切りは `line-start-position` と同様に計算される（表示がなく最大幅がある場合の特別な扱い）。

```
+----------------------------------------+
| [メソッド]                               |
|                                        |
| (send a-text paragraph-start-position  |
| → exact-nonnegative-integer?           |
| paragraph: exact-nonnegative-integer? |
| visible?: any/c = #t                  |
+----------------------------------------+
```

指定された段落の開始位置を返します。段落には 0 から始まる番号が付けられます。

段落が段落-1 よりも少ない場合、
最後の段落の先頭が返されます。

段落が非表示の項目で始まり、表示される場合はどうすればよいですか?です
#f ではなく、非表示項目を通過した最初の位置は
戻ってきました。

```
+----------------------------------------------------------------+
| [メソッド]                                                       |
|                                                                |
| (send a-text paste [time start end]) → void?                   |
| time: exact-integer? = 0                                      |
| start: (or/c exact-nonnegative-integer? 'start 'end) = 'start |
| end: (or/c exact-nonnegative-integer? 'same) = 'same          |
+----------------------------------------------------------------+
```

editor<%> での貼り付けをオーバーライドします。

指定した範囲に貼り付けます。開始が'startの場合、
その場合、現在の選択開始位置が使用されます。もし
開始は 'end、その後、現在の選択範囲が終了します
ポジションが使われます。終了が'sameの場合、
start が end である場合を除き、start は end として使用されます。
'start、この場合、現在の選択は終了します
ポジションが使われます。

time 引数の詳細については、「タイム スタンプのカット アンド ペースト」を参照。もし
時間がプラットフォーム固有の時間範囲外である、
exn:fail:contract 例外が発生します。

```
+----------------------------------+
| [メソッド]                         |
|                                  |
| (send a-text paste-next) → void? |
+----------------------------------+
```

編集者は、最大 30 個の以前のコピーを保持するコピー リングを共同で管理します。
編集者間でコピー（およびカット）を行います。次として呼び出されるとき
貼り付け後のエディタのメソッド、paste-next
メソッドは、以前の貼り付けのテキストを次のデータに置き換えます。
コピー リング。リング ポインタをインクリメントして、次のコピーが行われるようにします。
past-next はさらに古いデータを貼り付けます。

リングポインタが最も近い位置に戻るため、これはコピー「リング」です。
記憶されている最も古いデータが貼り付けられた後に、最近コピーされたデータ。どれでも
カット、コピー、または（通常の）ペースト操作により、コピー リング ポインタがリセットされます
最初に戻ります。

エディタでの前の操作が貼り付けではなかった場合は、
past-next は効果がありません。

```
+----------------------------------------------------------------+
| [メソッド]                                                       |
|                                                                |
| (send a-text paste-x-selection                                 |
| time: exact-integer? = 0                                      |
| start: (or/c exact-nonnegative-integer? 'start 'end) = 'start |
| end: (or/c exact-nonnegative-integer? 'same) = 'same          |
+----------------------------------------------------------------+
```

editor<%> での past-x-selection をオーバーライドします。

指定した範囲に貼り付けます。開始が'startの場合、
その場合、現在の選択開始位置が使用されます。もし
開始は 'end、その後、現在の選択範囲が終了します
ポジションが使われます。終了が'sameの場合、
start が end である場合を除き、start は end として使用されます。
'start、この場合、現在の選択は終了します
ポジションが使われます。

time 引数の詳細については、「タイム スタンプのカット アンド ペースト」を参照。もし
時間がプラットフォーム固有の時間範囲外である、
exn:fail:contract 例外が発生します。

```
+----------------------------------------------------------------+
| [メソッド]                                                       |
|                                                                |
| (send a-text position-grapheme n) → exact-nonnegative-integer? |
| n: exact-nonnegative-integer?                                 |
+----------------------------------------------------------------+
```

によって形成されたエディタ内の書記素の数を返します。
最初の n 項目。または、同様に、
項目ベースの位置から書記素ベースの位置へ。

パッケージ `gui-lib` のバージョン 1.67 で追加。

```
+---------------------------------------------+
| [メソッド]                                    |
|                                             |
| (send a-text position-line start [at-eol?]) |
| → exact-nonnegative-integer?                |
| start: exact-nonnegative-integer?          |
| at-eol?: any/c = #f                        |
+---------------------------------------------+
```

指定された位置を含む行の行番号を返します。行には 0 から始まる番号が付けられます。

`paragraph-start-position`も参照。
段落を操作します (明示的な改行文字によって決定されます)
行の代わりに (両方の明示的な改行によって決定されます)
文字と自動行折り返し)。

at-eol? については、「行末のあいまいさ」を参照。

このメソッドを呼び出すと、エディタに最大幅が設定されている場合、たとえエディタが現在リフレッシュ遅延中であっても、位置情報の再計算が強制されることがある（`refresh-delayed?` を参照）。エディタが表示されておらず、かつ最大幅を持つ場合、行区切りは `line-start-position` と同様に計算される（表示がなく最大幅がある場合の特別な扱い）。

```
+------------------------------------+
| [メソッド]                           |
|                                    |
| (send a-text position-location     |
| start: exact-nonnegative-integer? |
| x: (or/c (box/c real?) #f) = #f   |
| y: (or/c (box/c real?) #f) = #f   |
| top?: any/c = #t                  |
| at-eol?: any/c = #f               |
| whole-line?: any/c = #f           |
+------------------------------------+
```

指定された位置の位置を返します。 「位置-ロケーション」も参照。

x ボックスには、エディタで開始する位置の x 位置が入力されます。
x が #f でない限り、座標。
y ボックスには、
y が #f でない限り、エディタ座標での開始位置。

at-eol? については、「行末のあいまいさ」を参照。

トップなら？位置の上部座標である #f ではありません
が返されます。それ以外の場合は、底部の座標が返されます。
場所が返されます。

上位 y の位置は位置によって異なる場合があります
異なるサイズのグラフィック オブジェクトを使用する場合は、1 行内に配置してください。もし
全行? #f、最小上部位置、または
行全体の最大下部位置が y で返されます。

結果はエディタが表示されている場合にのみ有効です
(エディタの構造と用語を参照)。エディタは次の場合に表示されます。
get-admin は管理者 (#f ではない) を返します。このメソッドを呼び出すと、たとえエディタが現在リフレッシュ遅延中であっても、位置情報の再計算が強制されることがある（`refresh-delayed?` を参照）。

```
+-----------------------------------------+
| [メソッド]                                |
|                                         |
| (send a-text position-locations         |
| start: exact-nonnegative-integer?      |
| top-x: (or/c (box/c real?) #f) = #f    |
| top-y: (or/c (box/c real?) #f) = #f    |
| bottom-x: (or/c (box/c real?) #f) = #f |
| bottom-y: (or/c (box/c real?) #f) = #f |
| at-eol?: any/c = #f                    |
| whole-line?: any/c = #f                |
+-----------------------------------------+
```

位置と場所に似ていますが、両方の「上部」を返します。
そして一度に「最下位」の結果が得られます。

結果はエディタが表示されている場合にのみ有効です
(エディタの構造と用語を参照)。エディタは次の場合に表示されます。
get-admin は管理者 (#f ではない) を返します。このメソッドを呼び出すと、たとえエディタが現在リフレッシュ遅延中であっても、位置情報の再計算が強制されることがある（`refresh-delayed?` を参照）。

```
+------------------------------------+
| [メソッド]                           |
|                                    |
| (send a-text position-paragraph    |
| → exact-nonnegative-integer?       |
| start: exact-nonnegative-integer? |
| at-eol?: any/c = #f               |
+------------------------------------+
```

at-eol? については、「行末のあいまいさ」を参照。

指定された位置を含む段落の段落番号を返します。

```
+--------------------------------------------------------------------+
| [メソッド]                                                           |
|                                                                    |
| (send a-text read-from-file                                        |
| stream: (is-a?/c editor-stream-in%)                               |
| start: (or/c exact-nonnegative-integer? 'start)                   |
| overwrite-styles?: any/c = #f                                     |
| (send a-text read-from-file stream [overwrite-styles?]) → boolean? |
| (send a-text read-from-file                                        |
| stream: (is-a?/c editor-stream-in%)                               |
| overwrite-styles?: any/c = #f                                     |
+--------------------------------------------------------------------+
```

editor<%> でファイルからの読み取りを拡張します。

新しいデータは start で指定された位置、または
開始が'startの場合は現在位置。

```
+--------------------------------------------------+
| [メソッド]                                         |
|                                                  |
| (send a-text remove-clickback start end) → void? |
| start: exact-nonnegative-integer?               |
| end: exact-nonnegative-integer?                 |
+--------------------------------------------------+
```

正確に範囲の開始位置にインストールされているすべてのクリックバックを削除します
終わりに。クリックバックも参照。

```
+-------------------------------------------------------+
| [メソッド]                                              |
|                                                       |
| (send a-text scroll-to-position                       |
| start: exact-nonnegative-integer?                    |
| at-eol?: any/c = #f                                  |
| end: (or/c exact-nonnegative-integer? 'same) = 'same |
| bias: (or/c 'start 'end 'none) = 'none               |
+-------------------------------------------------------+
```

エディタをスクロールして、特定の位置が表示されるようにします。

終了が 'same または開始と等しい場合、位置
スタートが見えるようになります。行末のあいまいさについては、「行末のあいまいさ」を参照。
アトル？

終了が 'same でなく、開始と同じでない場合、
次に、範囲の開始から終了までが表示され、
アトル？無視されます。

指定範囲が表示領域に収まらない場合、バイアス
表示する範囲の端を示します。バイアスがあるとき
'start、範囲の開始が表示されます。いつ
バイアスが 'end の場合、範囲の終わりは
表示されます。それ以外の場合、バイアスは 'none でなければなりません。

エディタがスクロールされると、エディタが再描画され、
値は #t です。それ以外の場合、戻り値は #f です。もし
リフレッシュが遅延します （`refresh-delayed?` を参照）。
スクロール要求は遅延が終了するまで保存されます。巻物は、
これは、scroll-editor-to を呼び出すことによって (即時または後で) 実行されます。

エディタが内部でロックされている場合、スクロールは許可されません。
リフロー (内部エディタのロックも参照)。

システムは、このメソッドを呼び出さずにエディタをスクロールする場合があります。のために
たとえば、エディタを表示するキャンバスでは、エディタが次のようにスクロールされる場合があります。
スクロールバーイベントを処理します。

```
+--------------------------------------+
| [メソッド]                             |
|                                      |
| (send a-text set-anchor on?) → void? |
| on?: any/c                          |
+--------------------------------------+
```

アンカリングをオンまたはオフにします。このメソッドは、影響を与えるか、または
アンカー状態の変化を検出します。こちらも参照
アンカーを取得します。

オンの場合は? #f ではない場合、選択内容は次のようになります。
カーソルキーが使用されると自動的に延長されます（より一般的には、
move-position を使用して選択範囲を移動する場合、または
キープアンカー？ set-position の引数は true 値です)、
それ以外の場合、アンカーリングはオフになります。アンカーリングは自動的に回転します
ユーザーがカーソルの移動以外のことを行う場合はオフになります。

```
+------------------------------------------+
| [メソッド]                                 |
|                                          |
| (send a-text set-autowrap-bitmap bitmap) |
| → (or/c (is-a?/c bitmap%) #f)            |
| bitmap: (or/c (is-a?/c bitmap%) #f)     |
+------------------------------------------+
```

線の終端に描画されるビットマップを設定します。
自動的に改行されます。

ビットマップが #f の場合、自動折り返し インジケーターは描画されません
(これがデフォルトです)。以前に使用されたビットマップ (おそらく
#f) が返されます。

エディタが内部的にロックされている場合、ビットマップの設定は許可されません
リフロー用 (内部エディタのロックも参照)。

```
+-------------------------------------------------------+
| [メソッド]                                              |
|                                                       |
| (send a-text set-between-threshold threshold) → void? |
| threshold: (and/c real? (not/c negative?))           |
+-------------------------------------------------------+
```

ユーザーの意味を判断するために使用されるグラフィック距離を設定します
クリックしてください。クリックが位置のしきい値内にある場合
2 つのアイテムの間にある場合、そのスペースでクリックが登録されます
どちらかの項目ではなく、項目の間で。

こちらも参照
get-between-threshold.

```
+-------------------------------------------------------------------------------+
| [メソッド]                                                                      |
|                                                                               |
| (send a-text set-clickback                                                    |
| start: exact-nonnegative-integer?                                            |
| end: exact-nonnegative-integer?                                              |
| f: (-> (is-a?/c text%) exact-nonnegative-integer? exact-nonnegative-integer? |
| any)                                                                          |
| (-> (is-a?/c text%)                                                           |
| exact-nonnegative-integer?                                                    |
| exact-nonnegative-integer?                                                    |
| any)                                                                          |
| hilite-delta: (or/c (is-a?/c style-delta%) #f) = #f                          |
| call-on-down?: any/c = #f                                                    |
|                                                                               |
| ```racket                                                                     |
| (-> (is-a?/c text%)                                                           |
|     exact-nonnegative-integer?                                                |
|     exact-nonnegative-integer?                                                |
|     any)                                                                      |
| ```                                                                           |
+-------------------------------------------------------------------------------+
```

指定された領域にクリックバックをインストールします。クリックバックがすでに発生している場合
重複する領域にインストールされている場合、このクリックバックが優先されます。

コールバック プロシージャ f は、ユーザーが
クリックバック。 f への引数は、このエディタと開始エディタです。
クリックバックの終了範囲。

hilite-delta スタイルのデルタがクリックバック テキストに適用されます
ユーザーがクリックし、まだマウスを上に置いたままのとき
クリックバック。 hilite-delta が #f の場合、クリックバック
領域のスタイルは、選択時に変更されません。

コールオンダウンの場合は？ #f ではない場合、クリックバックが呼び出されます
ユーザーがマウスボタンをクリックした直後ではなく、
マウスアップイベントの後。 hilite-delta 引数は使用されません
この場合。

あわせて Clickbacks も参照。

```
+------------------------------------------------+
| [メソッド]                                       |
|                                                |
| (send a-text set-file-format format) → void?   |
| format: (or/c 'standard 'text 'text-force-cr) |
+------------------------------------------------+
```

このエディタから保存するファイルの形式を設定します。

法的な形式は次のとおりです。

- 'standard — 標準エディタ ファイル
- 'text — テキスト ファイル
- 'text-force-cr — テキスト ファイル。書くときに変更する
(ワードラップによる) 自動改行から実際の改行への変換

エディタのファイル形式を変更できる
によって
ファイルのロードと保存に応答するシステム
メソッド呼び出し、そのような変更はこのメソッドを経由しません。 on-load-file を使用し、
ファイル保存時
このようなファイル形式の変更を監視します。

```
+----------------------------------------------+
| [メソッド]                                     |
|                                              |
| (send a-text set-line-spacing space) → void? |
| space: (and/c real? (not/c negative?))      |
+----------------------------------------------+
```

エディタによって各行間に挿入される間隔を設定します。これ
間隔は、報告される各行の高さに含まれます。

```
+----------------------------------------------+
| [メソッド]                                     |
|                                              |
| (send a-text set-overwrite-mode on?) → void? |
| on?: any/c                                  |
+----------------------------------------------+
```

上書きモードを有効または無効にします。 get-overwrite-mode を参照。このメソッドは、影響を与えるか、または
上書きモードでの変更を検出します。

```
+------------------------------------------+
| [メソッド]                                 |
|                                          |
| (send a-text set-padding                 |
| left: (and/c real? (not/c negative?))   |
| top: (and/c real? (not/c negative?))    |
| right: (and/c real? (not/c negative?))  |
| bottom: (and/c real? (not/c negative?)) |
+------------------------------------------+
```

エディタ内に描画されるときにエディタのコンテンツを挿入するパディングを設定します。
ディスプレイ。

編集者によって適用されるマージンとは異なります。
表示、パディングは位置でカウントされます
位置情報などの方法で報告される情報。たとえば、左パディングが 17.0 の場合
上部パディングが 9.0 の場合、位置 0 の位置は次のようになります。
(0, 0) ではなく (17.0, 9.0)。パディングもまた、
get-extent によって報告されるエディタのサイズ。

```
+-----------------------------------------+
| [メソッド]                                |
|                                         |
| (send a-text set-paragraph-alignment    |
| paragraph: exact-nonnegative-integer?  |
| alignment: (or/c 'left 'center 'right) |
+-----------------------------------------+
```

段落固有の水平方向の配置を設定します。アライメントはあくまで
で設定されたように、エディタに最大幅がある場合に使用されます。
最大幅を設定します。段落には 0 から始まる番号が付けられます。

この方法は実験的なものです。次の場合にのみ確実に機能します。
段落は結合または分割されていません。段落の結合または分割
アライメント設定を使用すると、設定が転送されます
予期せぬ事態が発生します (ただし、エディタ内の他の段落は安全に実行できます)
分割または統合されます）。エディタの最後の段落が空の場合、
割り当てられた設定は無視されます。

```
+----------------------------------------------+
| [メソッド]                                     |
|                                              |
| (send a-text set-paragraph-margins           |
| paragraph: exact-nonnegative-integer?       |
| first-left: (and/c real? (not/c negative?)) |
| left: (and/c real? (not/c negative?))       |
| right: (and/c real? (not/c negative?))      |
+----------------------------------------------+
```

段落固有の余白を設定します。段落には 0 から始まる番号が付けられます。

段落の最初の行は左端の点によってインデントされます
エディタ内で。段落が改行されている場合 (エディタの場合)
最大幅があります)、後続の行は左からインデントされます
ポイント。エディタに最大幅がある場合、段落の最大幅
行の折り返しの幅は、右のポイントより小さいです。
エディタの最大幅。

この方法は実験的なものです。詳細については、`set-paragraph-alignment`を参照。

```
+-------------------------------------------------------+
| [メソッド]                                              |
|                                                       |
| (send a-text set-position                             |
| start: exact-nonnegative-integer?                    |
| end: (or/c exact-nonnegative-integer? 'same) = 'same |
| at-eol?: any/c = #f                                  |
| scroll?: any/c = #t                                  |
| seltype: (or/c 'default 'x 'local) = 'default        |
+-------------------------------------------------------+
```

エディタで現在の選択内容を設定します。

end が 'same または start 以下の場合、
現在の開始位置と終了位置は両方とも次のように設定されます。
始めます。それ以外の場合は、指定された範囲が選択されます。

at-eol? については、「行末のあいまいさ」を参照。もし
スクロール？ #f ではない場合、表示は次のようになります。
必要に応じてスクロールして選択内容を表示します。

seltype 引数は、X Window System が使用されている場合にのみ使用されます。
選択メカニズムが有効になっています。可能な値は次のとおりです。

- 'default — このウィンドウにキーボード フォーカスがある場合
指定された選択が空ではない場合は、それを現在の X 選択にします
- 'x — 指定された選択範囲が空でない場合、
それは現在の X 選択です
- 'local — 変更しないでください
現在の X の選択

エディタが内部にある場合、位置の設定は許可されません。
リフロー用にロックされています (「内部エディタのロック」も参照)。

システムは、これを呼び出さずにエディタの選択を変更する場合があります。
メソッド (または表示される任意のメソッド)。

あわせて editor-set-x-selection-mode も参照。

```
+-------------------------------------------------------+
| [メソッド]                                              |
|                                                       |
| (send a-text set-position-bias-scroll                 |
| bias: (or/c 'start-only 'start 'none 'end 'end-only) |
| start: exact-nonnegative-integer?                    |
| end: (or/c exact-nonnegative-integer? 'same) = 'same |
| ateol?: any/c = #f                                   |
| scroll?: any/c = #t                                  |
| seltype: (or/c 'default 'x 'local) = 'default        |
+-------------------------------------------------------+
```

set-position と似ていますが、スクロール バイアスを指定できます。

バイアスに指定できる値は次のとおりです。

- 'start-only — 開始位置が表示されていることのみを確認します
- 'start — 範囲が表示領域に収まらない場合は、開始位置を表示します
- 'none — 特別なスクロール命令なし
- 'end — 範囲が表示領域に収まらない場合は、終了位置を表示します
- 'end-only — 終了位置が表示されることのみを保証します

あわせて scroll-to-position も参照。

```
+------------------------------------------------------+
| [メソッド]                                             |
|                                                      |
| (send a-text set-region-data start end data) → void? |
| start: exact-nonnegative-integer?                   |
| end: exact-nonnegative-integer?                     |
| data: (is-a?/c editor-data%)                        |
+------------------------------------------------------+
```

仕様:
特定の領域に関連付けられた追加データを設定します。参照
詳細については Editor Data と get-region-data を参照
情報。

このメソッドは、以下と組み合わせてオーバーライドすることを目的としています。
地域データを取得します。

既定の実装:
何もしない。

```
+-------------------------------------------------+
| [メソッド]                                        |
|                                                 |
| (send a-text set-styles-sticky sticky?) → void? |
| sticky?: any/c                                 |
+-------------------------------------------------+
```

スティッキーについては、`get-styles-sticky`を参照。
スタイル。

```
+------------------------+
| [メソッド]               |
|                        |
| (send a-text set-tabs  |
| tabs: (listof real?)  |
| tab-width: real? = 20 |
| in-units?: any/c = #t |
+------------------------+
```

エディタのタブ配列を設定します。

タブ リストによってタブ配列が決まります。タブ配列
各タブが出現する x 位置を指定します。最後以降のタブ
指定されたタブは固定量のタブ幅で区切られます。もし
ユニット内？が #f ではない場合、キャンバス内でタブが指定されます
単位。それ以外の場合は、スペースの数として指定されます。 (タブの場合
スペースで指定するとグラフィックタブの位置が変わります
タブに使用されているフォントを使用します)。

エディタが内部でロックされている場合、タブの設定は許可されません。
リフロー (内部エディタのロックも参照)。

```
+--------------------------------------------------------------------------------+
| [メソッド]                                                                       |
|                                                                                |
| (send a-text set-wordbreak-func f) → void?                                     |
| f: ((is-a?/c text%) (or/c (box/c exact-nonnegative-integer?) #f) (or/c (box/c |
| exact-nonnegative-integer?) #f) symbol?. ->. any)                            |
| ((is-a?/c text%) (or/c (box/c exact-nonnegative-integer?) #f)                  |
| (or/c (box/c exact-nonnegative-integer?) #f)                                   |
| symbol?                                                                        |
|. ->. any)                                                                    |
|                                                                                |
| ```racket                                                                      |
| ((is-a?/c text%) (or/c (box/c exact-nonnegative-integer?) #f)                  |
|                  (or/c (box/c exact-nonnegative-integer?) #f)                  |
|                  symbol?                                                       |
|. ->. any)                                                                   |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

エディタの単語分割機能を設定します。詳細については、
単語分割関数の引数については、find-wordbreak を参照。

標準のワードブレイク機能はエディタの
どの文字を決定するための editor-wordbreak-map% オブジェクト
言葉を中断する。 editor-wordbreak-map% および
ワードブレイクマップを設定します。

改行時にwordbreak関数が呼び出されるので、
(最大幅があるエディタで) 決定されると、
ワードブレイクが実行する text% メソッドの制約されたセット
関数の呼び出しが許可されます。メンバー関数を呼び出すことはできません
場所や路線に関する情報を使用するもの (
このマニュアルでは「結果はエディタが表示されている場合にのみ有効です」と記載されています。
(エディタの構造と用語を参照)。エディタは次の場合に表示されます。
get-admin は管理者 (#f ではない) を返します。」)、ただし、引き続き呼び出すことができます。
スニップとアイテムを操作するメンバー関数。

```
+-------------------------------------------------+
| [メソッド]                                        |
|                                                 |
| (send a-text set-wordbreak-map map) → void?     |
| map: (or/c (is-a?/c editor-wordbreak-map%) #f) |
+-------------------------------------------------+
```

標準のワードブレイクで使用されるワードブレイクマップを設定します。
機能。詳細については、「editor-wordbreak-map%」を参照。

マップが#fの場合、標準マップ
(the-editor-wordbreak-map) が使用されます。

```
+--------------------------------------+
| [メソッド]                             |
|                                      |
| (send a-text split-snip pos) → void? |
| pos: exact-nonnegative-integer?     |
+--------------------------------------+
```

位置を指定して、以下を含むスニップを分割します。
(存在する場合) 位置が次のようになります。
2つの切り取りの間。スニップは分割を拒否する可能性がありますが、
組み込みの snip クラスは拒否されます。

エディタが内部的にロックされている場合、スニップの分割は許可されません
リフロー用 (内部エディタのロックも参照)。

```
+-----------------------------------------------------------+
| [メソッド]                                                  |
|                                                           |
| (send a-text write-to-file stream [start end]) → boolean? |
| stream: (is-a?/c editor-stream-out%)                     |
| start: exact-nonnegative-integer? = 0                    |
| end: (or/c exact-nonnegative-integer? 'eof) = 'eof       |
+-----------------------------------------------------------+
```

editor<%> でのファイルへの書き込みを拡張します。

開始が 0 で終了が 'eof 負の場合、
その後、コンテンツ全体がストリームに書き込まれます。終了の場合
'eofの場合、内容は最初から書き込まれます
エディタが終わるまで。それ以外の場合は、指定された内容
範囲が書かれています。

---

## timer%

```
+----------------------+
| classtimer%: class? |
+----------------------+
| superclass: object%  |
+----------------------+
```

timer% オブジェクトは、イベントベースのアラームをカプセル化します。を使用するには
タイマー、タイマー コールバック サンクでインスタンス化するか、
アラームベースのアクションを実行するか、新しいクラスを派生してオーバーライドします。
アラームベースの通知を実行する通知メソッド
アクション。 startでタイマーを開始し、で停止します
やめて。初期間隔を指定します (
ミリ秒) タイマーを作成すると、タイマーも開始されます。

タイマーはイベント キュー内で比較的高い優先順位を持っています。したがって、もし
タイマーの遅延が十分に低く設定されており、タイマーの繰り返し通知
ユーザーのアクティビティをプリエンプトすることができます (これは、
タイマー）。遅延が比較的短いタイマーの場合は、yield を呼び出します。
通知プロシージャ内で保証されたイベントを許可する
処理中。

イベントの詳細については、「イベントのディスパッチとイベントスペース」を参照。
優先順位。

```
+-----------------------------------------------------+
| [コンストラクタ]                                       |
|                                                     |
| (new timer%                                         |
| → (is-a?/c timer%)                                  |
| notify-callback: (-> any) = void                   |
| interval: (or/c (integer-in 0 1000000000) #f) = #f |
| just-once?: any/c = #f                             |
+-----------------------------------------------------+
```

デフォルトでは、notify-callback サンクが呼び出されます。
タイマーが期限切れになったときの通知メソッド。

間隔が #f (デフォルト) の場合、タイマーは使用されません。
始めました。その場合、start を呼び出す必要があります
明示的に。間隔が数値 (ミリ秒単位) の場合、
start は間隔を指定して呼び出され、
一度だけ？

```
+-----------------------------------------------------+
| [メソッド]                                            |
|                                                     |
| (send a-timer interval) → (integer-in 0 1000000000) |
+-----------------------------------------------------+
```

各タイマーの有効期限間のミリ秒数を返します (
タイマーが作動中です）。

```
+-------------------------------+
| [メソッド]                      |
|                               |
| (send a-timer notify) → void? |
+-------------------------------+
```

仕様:
タイマーのアラームが期限切れになったときに (イベント境界で) 呼び出されます。

既定の実装:
通知時に提供された通知コールバック プロシージャを呼び出します。
オブジェクトが作成されました。

```
+------------------------------------------------+
| [メソッド]                                       |
|                                                |
| (send a-timer start msec [just-once?]) → void? |
| msec: (integer-in 0 1000000000)               |
| just-once?: any/c = #f                        |
+------------------------------------------------+
```

タイマーを開始 (または再起動) します。タイマーがすでに実行されている場合、アラーム時間は変更されません。

タイマーのアラームは msec ミリ秒後に期限切れになります。その時点で
notify が呼び出されます (イベント境界上で)。もし
一度だけ？ true の場合、タイマーは通知を呼び出します
アラームが期限切れになり、タイマーが停止したときのコールバック。もし
一度だけ？が #f の場合、通知が行われるとタイマーが再スタートします。
コールバックが戻ります。 stop が明示的に呼び出された場合にのみ停止します。

```
+-----------------------------+
| [メソッド]                    |
|                             |
| (send a-timer stop) → void? |
+-----------------------------+
```

タイマーを停止します。停止したタイマーは決して呼び出しません
通知します。タイマーが期限切れになったにもかかわらず、
通知がまだディスパッチされていない場合、呼び出しはイベント キューから削除されます。

---

## top-level-window<%>

```
+-------------------------------------------+--------------------------+
| interfacetop-level-window<%>: interface? |                          |
+-------------------------------------------+--------------------------+
| implements:                               | area-container-window<%> |
+-------------------------------------------+--------------------------+
```

トップレベルのウィンドウはフレーム%またはダイアログ%のいずれかです
オブジェクト。

```
+-------------------------------------------------+
| [メソッド]                                        |
|                                                 |
| (send a-top-level-window can-close?) → boolean? |
+-------------------------------------------------+
```

このメソッドは augment で拡張する。

ウィンドウが閉じられる直前に呼び出されます (ウィンドウの近くなど)
マネージャー）。 #fが返された場合、ウィンドウは閉じられていません。
それ以外の場合は on-close が呼び出され、
ウィンドウが閉じられています (つまり、呼び出しのようにウィンドウが非表示になっています)
#f で表示)。

このメソッドは show によって呼び出されません。

```
+------------------------------------------------+
| [メソッド]                                       |
|                                                |
| (send a-top-level-window can-exit?) → boolean? |
+------------------------------------------------+
```

仕様:
終了前に呼び出され、
退出は許可されます。詳細については、出口を参照
情報。

既定の実装:
通話が終了する可能性がありますか?そして結果を返します。

```
+--------------------------------------------------------+
| [メソッド]                                               |
|                                                        |
| (send a-top-level-window center [direction]) → void?   |
| direction: (or/c 'horizontal 'vertical 'both) = 'both |
+--------------------------------------------------------+
```

親がない場合、ウィンドウを画面の中央に配置します。がある場合は、
親の場合、ウィンドウは親の位置を基準にして中央に配置されます。

方向が 'horizontal の場合、ウィンドウは中央に配置されます
水平方向に。方向が 'vertical の場合、
ウィンドウが垂直方向の中央に配置されます。方向が
'both、ウィンドウは両方向の中央に配置されます。

```
+------------------------------------------------------------+
| [メソッド]                                                   |
|                                                            |
| (send a-top-level-window get-edit-target-object)           |
| → (or/c (or/c (is-a?/c window<%>) (is-a?/c editor<%>)) #f) |
+------------------------------------------------------------+
```

いいね
get-edit-target-window、ただしエディタの場合
Canvas にはフォーカスがあり、エディタも表示されます。エディタは
キャンバスの代わりに返されます。さらに、編集者の焦点が
埋め込みエディタに委任すると、埋め込みエディタが返されます。

あわせて get-focus-object も参照。

```
+--------------------------------------------------+
| [メソッド]                                         |
|                                                  |
| (send a-top-level-window get-edit-target-window) |
| → (or/c (is-a?/c window<%>) #f)                  |
+--------------------------------------------------+
```

ウィンドウを返します。
直近では、トップレベル ウィンドウまたは
現在表示されている子の 1 つ。窓も次のいずれでもない場合は、
現在表示されている子はキーボード フォーカスさえ所有しています。
#f が返されます。

`get-focus-window`および`get-focus-window`も参照。
編集対象オブジェクトを取得します。

```
+--------------------------------------------------------+
| [メソッド]                                               |
|                                                        |
| (send a-top-level-window get-eventspace) → eventspace? |
+--------------------------------------------------------+
```

ウィンドウのイベントスペースを返します。

```
+------------------------------------------------------------+
| [メソッド]                                                   |
|                                                            |
| (send a-top-level-window get-focus-object)                 |
| → (or/c (or/c (is-a?/c window<%>) (is-a?/c editor<%>)) #f) |
+------------------------------------------------------------+
```

get-focus-window と似ていますが、エディタ キャンバスにフォーカスがあり、それも
エディタを表示すると、エディタの代わりにエディタが返されます。
キャンバス。さらに、エディタのフォーカスが埋め込みオブジェクトに委任されている場合、
エディタの場合、埋め込みエディタが返されます。

あわせて get-edit-target-object も参照。

```
+--------------------------------------------+
| [メソッド]                                   |
|                                            |
| (send a-top-level-window get-focus-window) |
| → (or/c (is-a?/c window<%>) #f)            |
+--------------------------------------------+
```

キーボードのあるウィンドウを返します。
最上位ウィンドウまたはその子のいずれかにフォーカスします。どちらでもない場合
ウィンドウもその子もフォーカスを持っていないため、#f は
戻ってきました。

`get-edit-target-window`および`get-edit-target-window`も参照。
フォーカスオブジェクトを取得します。

```
+--------------------------------------------+
| [メソッド]                                   |
|                                            |
| (send a-top-level-window move x y) → void? |
| x: position-integer?                      |
| y: position-integer?                      |
+--------------------------------------------+
```

ウィンドウを画面上の指定された位置に移動します。

ウィンドウの位置は変更可能
ユーザーがウィンドウをドラッグすることによって行われますが、そのような変更はこのメソッドを介しません。移動中に使用する
モニターの位置が変わります。

```
+-------------------------------------------------------+
| [メソッド]                                              |
|                                                       |
| (send a-top-level-window on-activate active?) → void? |
| active?: any/c                                       |
+-------------------------------------------------------+
```

ウィンドウがアクティブ化されたとき、または
非アクティブ化されました。トップレベルウィンドウは、
キーボードのフォーカスがウィンドウの外側からウィンドウまたは次のいずれかに移動します。
その子供たち。フォーカスが元の位置から戻ると無効になります。
窓。 Mac OS では、フローティング フレームの子に
アクティブな非フローティング フレームの子の代わりにフォーカスします。他に
つまり、フローティング フレームはアクティブな非フレームの拡張として機能します。
キーボードフォーカス用。

ウィンドウがアクティブ化されているとき、メソッドの引数は #t ですが、
#f 無効化された場合。

```
+--------------------------------------------+
| [メソッド]                                   |
|                                            |
| (send a-top-level-window on-close) → void? |
+--------------------------------------------+
```

このメソッドは augment で拡張する。

ウィンドウが閉じる直前に呼び出されます (ウィンドウ マネージャーなどによって)。
このメソッドは show によって呼び出されません。

こちらも参照
閉めることができますか？

```
+-------------------------------------------+
| [メソッド]                                  |
|                                           |
| (send a-top-level-window on-exit) → void? |
+-------------------------------------------+
```

仕様:
デフォルトのアプリケーション終了ハンドラーによって呼び出されます (
application-quit-handler パラメータ)
システムがアプリケーションのシャットダウンを要求する（たとえば、
メイン アプリケーション メニューで [終了] メニュー項目が選択されている
Mac OS の場合)。その場合、このメソッドが最もよく呼び出されます。
初期イベントスペースで最近アクティブになったトップレベル ウィンドウですが、
窓から出られるかどうか？まずメソッド
trueを返します。

既定の実装:
電話
閉店後、そしてその後
show ウィンドウを非表示にします。

```
+------------------------------------------------------+
| [メソッド]                                             |
|                                                      |
| (send a-top-level-window on-message message) → any/c |
| message: any/c                                      |
+------------------------------------------------------+
```

仕様:
一般的なメッセージ メソッド。通常は次のように呼び出されます。
ウィンドウにメッセージを送信します。

メソッドが send-message-to-window によって呼び出された場合、
send-message-to-window が実行されたスレッドで呼び出されます。
呼び出されます (これはおそらく、
ウィンドウのイベントスペース）。

既定の実装:
#<void> を返します。

```
+---------------------------------------------------+
| [メソッド]                                          |
|                                                   |
| (send a-top-level-window display-changed) → any/c |
+---------------------------------------------------+
```

仕様: ディスプレイ構成が変更されたときに呼び出されます。

新しいモニター構成を決定するには、次を使用します。
表示数の取得、表示サイズの取得、
get-display-left-top-inset、および
表示バッキングスケールを取得します。

このメソッドは 1 つのメソッドに対して複数回呼び出される可能性があることに注意してください。
モニターへの論理的な変更。

既定の実装: #<void> を返します。

```
+-------------------------------------------------------------+
| [メソッド]                                                    |
|                                                             |
| (send a-top-level-window on-traverse-char event) → boolean? |
| event: (is-a?/c key-event%)                                |
+-------------------------------------------------------------+
```

仕様:
与えられたものを処理しようとします
ナビゲーション イベントとしてのキーボード イベント (Tab キー イベントなど)
キーボードのフォーカスを移動します。イベントが処理される場合、#t は
返されます。それ以外の場合は、#f が返されます。

既定の実装:
次のルールは、イベントが発生するかどうか、およびどのように発生するかを順番に決定します。
処理されます:

- 現在フォーカスを所有しているウィンドウが特に
イベントの場合、#f が返されます。以下にウィンドウを説明します
タイプと、それらが具体的に処理するキーボード イベント:
editor-canvas% — tab-exit が無効になります (「
allowed-tab-exit): すべてのキーボード イベント。ただし、メタの場合の英数字キー イベントを除く。
(Unix) または Alt (Windows) キーが押されました。タブ終了が有効な場合:
Tab、Enter、Escape、英数字を除くすべてのキーボード イベント
Meta/Alt events.canvas% — タブ フォーカスが無効な場合 (「」を参照)
accept-tab-focus): メタの場合の英数字キー イベントを除く、すべてのキーボード イベント
(Unix) または Alt (Windows) キーが押されました。タブフォーカスが有効な場合:
キーなし eventstext-field%、'single スタイル — 矢印キー
Meta (Unix) または Alt キーを押したときのイベントと英数字キー イベント
(Windows) キーが押されていない (およびすべての英数字イベントが押されていない)
Mac OS)テキストフィールド%、'multiple スタイル — すべて
キーボード イベント。メタ (Unix) または
Alt (Windows) キーが押されたときchoice% — 矢印キー イベントと英数字キー
Meta (Unix) または Alt (Windows) キーが押されていないときのイベントlist-box% — 矢印キー イベントと英数字キー
Meta (Unix) または Alt (Windows) キーが押されていないときのイベント
- イベントが Tab キーまたは矢印キー イベントの場合、キーボード フォーカスは
ウィンドウ内で移動すると、#t が返されます。プラットフォーム全体で、
ナビゲーション経由でキーボード フォーカスを受け入れるウィンドウの種類
異なる場合がありますが、text-field% ウィンドウは常にフォーカスを受け入れます。
およびメッセージ%、ゲージ%、およびパネル%
ウィンドウは決してフォーカスを受け入れません。
- イベントがスペースキーイベントであり、現在表示されているウィンドウの場合
フォーカスがボタン%、チェックボックス%、または
radio-box% オブジェクトの場合、イベントは次と同じ方法で処理されます。
コントロールをクリックすると、#t が返されます。
- イベントが Enter キー イベントで、現在のトップレベル ウィンドウの場合
境界ボタンが含まれている場合、ボタンのコールバックが呼び出され、
#t が返されます。 ('border スタイル
button% オブジェクトは、Enter キーを押すことをユーザーに示します。
ボタンをクリックするのと同じです。) ウィンドウに
境界ボタン、現在のウィンドウが存在する場合、#t が返されます。
フォーカスはテキスト フィールドやエディタ キャンバスではありません。
- ダイアログでは、イベントが Escape キー イベントの場合、イベントは
ダイアログのクローズ ボックスをクリックした場合と同じように処理されます (つまり、
ダイアログの
閉めることができますか？そして
閉じるときにメソッドが呼び出され、ダイアログが非表示になります)、#t は
戻ってきました。
- イベントが英数字キーイベントであり、現在のトップレベルの場合
ウィンドウには、キーに一致するニーモニックを持つコントロールが含まれています (
&; を含むラベルを介してインストールされています。見る
詳細については get-label)、その後、
キーボードのフォーカスが一致するコントロールに移動します。さらに、
一致するコントロールはボタン%、チェックボックス%、または
radio-box% ボタンの場合、キーボード イベントは
コントロールをクリックするのと同じ方法です。
- それ以外の場合は、#f が返されます。

```
+----------------------------------------------------------------+
| [メソッド]                                                       |
|                                                                |
| (send a-top-level-window on-system-menu-char event) → boolean? |
| event: (is-a?/c key-event%)                                   |
+----------------------------------------------------------------+
```

指定されたイベントがシステム メニューを開くかどうかを確認します。
ウィンドウの左上隅 (Windows のみ)。ウィンドウのシステムの場合
メニューが開かれている場合は #t が返され、それ以外の場合は #f が返されます。
戻ってきました。

```
+---------------------------------+
| [メソッド]                        |
|                                 |
| (send a-top-level-window resize |
| width: dimension-integer?      |
| height: dimension-integer?     |
+---------------------------------+
```

ウィンドウのサイズ (ピクセル単位) を設定します。ただし、指定されたサイズが
ウィンドウの最小サイズより大きい。

ウィンドウのサイズを変更できる
ユーザーによって変更され、そのような変更はこのメソッドを介しません。オンサイズを使用して
モニターのサイズが変わります。

```
+--------------------------------------------+
| [メソッド]                                   |
|                                            |
| (send a-top-level-window set-icon          |
| icon: (is-a?/c bitmap%)                   |
| mask: (is-a?/c bitmap%) = #f              |
| which: (or/c 'small 'large 'both) = 'both |
+--------------------------------------------+
```

ウィンドウの大小のアイコン ビットマップを設定します。今後の変更点
ビットマップはウィンドウのアイコンには影響しません。

アイコンはプラットフォーム固有の方法で使用されます。

- Windows — 小さなアイコンがウィンドウのアイコンとして使用されます (
左上) とタスク バーにあり、大きなアイコンは次の目的で使用されます。
Alt-Tab タスク スイッチャー。
- Mac OS — 両方のアイコンは無視されます。
- Unix — 多くのウィンドウ マネージャーが同じ方法で小さなアイコンを使用します。
Windows などは、アイコン化するときに小さなアイコンを使用します。
フレーム;大きなアイコンは無視されます。

どちらのアイコンのビットマップも任意のサイズにできますが、ほとんどのプラットフォームでは拡大縮小できます。
小さなビットマップは 16 x 16 ピクセルに、大きなビットマップは 32 x 32 ピクセルに
ピクセル。

マスク ビットマップが提供されていない場合は、(長方形の) ビットマップ全体が
がアイコンとして使われています。

マスク ビットマップが提供される場合、マスクはモノクロである必要があります。マスクの中で
ビットマップ、黒いピクセルを使用してアイコンの領域を示し、白を使用します
アイコンの領域外のピクセル。アイコンのビットマップでは黒を使用します
アイコンの外側の領域のピクセル。

```
+---------------------------------------------+
| [メソッド]                                    |
|                                             |
| (send a-top-level-window show show) → void? |
| show: any/c                                |
+---------------------------------------------+
```

ウィンドウがすでに表示されている場合は、他の最上位レベルの前に移動されます。
窓。ウィンドウがアイコン化されている場合 (フレームのみ)、アイコン化が解除されます。

あわせて show in window<%> も参照。

---

## vertical-pane%

```
+------------------------------+
| classvertical-pane%: class? |
+------------------------------+
| superclass: pane%            |
+------------------------------+
```

垂直ペインでは、サブウィンドウが 1 列に配置されます。 「ペイン%」も参照。

```
+--------------------------------------------------------------------------------+
| [コンストラクタ]                                                                  |
|                                                                                |
| (new vertical-pane%                                                            |
| → (is-a?/c vertical-pane%)                                                     |
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

horiz-margin と vert-margin については、
引数については、subarea<%> を参照。境界線、間隔、配置の詳細については、
引数については、area-container<%> を参照。についての情報は、
min-width、min-height、伸縮可能な幅、および
伸縮可能な高さの引数については、 area<%> を参照。

---

## vertical-panel%

```
+-------------------------------+
| classvertical-panel%: class? |
+-------------------------------+
| superclass: panel%            |
+-------------------------------+
```

垂直パネルでは、サブウィンドウが 1 列に配置されます。参照
パネル%も。

```
+--------------------------------------------------------------------------------+
| [コンストラクタ]                                                                  |
|                                                                                |
| (new vertical-panel%                                                           |
| → (is-a?/c vertical-panel%)                                                    |
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

スタイル フラグは、panel% の場合と同じです。

有効な引数については、「window<%>」を参照。 horiz-margin と vert-margin については、
引数については、subarea<%> を参照。境界線、間隔、配置の詳細については、
引数については、area-container<%> を参照。についての情報は、
min-width、min-height、伸縮可能な幅、および
伸縮可能な高さの引数については、 area<%> を参照。

```
+-------------------------------------------------------------+
| [メソッド]                                                    |
|                                                             |
| (send a-vertical-panel set-orientation horizontal?) → void? |
| horizontal?: boolean?                                      |
+-------------------------------------------------------------+
```

パネルの向きを切り替えて設定します。
垂直パネル%の動作と
水平パネル%。

```
+----------------------------------------------------+
| [メソッド]                                           |
|                                                    |
| (send a-vertical-panel get-orientation) → boolean? |
+----------------------------------------------------+
```

最初は #f を返しますが、
set-orientation が呼び出されます。
このメソッドは、最後に渡された値をすべて返します。

---

## window<%>

```
+---------------------------------+---------+
| interfacewindow<%>: interface? |         |
+---------------------------------+---------+
| implements:                     | area<%> |
+---------------------------------+---------+
```

`window<%>` オブジェクトは、イベントに応答できるグラフィカルな表現を持つ `area<%>` である。

すべての `window<%>` クラスは、次の名前付きインスタンス化引数を受け付ける。

- `enabled` — 既定は `#t`。`#f` のとき `enable` に渡される

```
+---------------------------------------------------------+
| [メソッド]                                                |
|                                                         |
| (send a-window accept-drop-files) → boolean?            |
| (send a-window accept-drop-files accept-files?) → void? |
| accept-files?: any/c                                   |
+---------------------------------------------------------+
```

ドラッグ アンド ドロップによるドロップを有効または無効にします。
ウィンドウの場合、または有効状態を取得します。ドロップは最初は
無効になっています。 「オンドロップファイル」も参照。

```
+---------------------------------------+
| [メソッド]                              |
|                                       |
| (send a-window client->screen x y)    |
| → position-integer? position-integer? |
| position-integer?                     |
| x: position-integer?                 |
| y: position-integer?                 |
+---------------------------------------+
```

ローカルウィンドウ座標を次のように変換します。
画面座標。

Mac OS では、画面座標は (0, 0) から始まります。
メニューバーの左上。対照的に、move in top-level-window<%> は、(0, 0) がメニュー バーの下にあるとみなします。こちらも参照
get-display-left-top-inset。

```
+----------------------------------------+
| [メソッド]                               |
|                                        |
| (send a-window enable enable?) → void? |
| enable?: any/c                        |
+----------------------------------------+
```

入力イベントが無視されるようにウィンドウを有効または無効にします。 (入力
イベントには、マウス イベント、キーボード イベント、およびクローズ ボックスのクリックが含まれます。
(イベントのフォーカスや更新は行いません) ウィンドウが無効になっている場合は、次のように入力します。
その子に対するイベントも無視されます。

ウィンドウの有効状態を変更できます
親ウィンドウを有効にすることによって行われますが、そのような変更はこのメソッドを介しません。 on-superwindow-enable を使用して、
イネーブル状態の変化を監視します。

有効にする場合は? true の場合、ウィンドウは有効になります。それ以外の場合は、
無効になっています。

```
+-------------------------------+
| [メソッド]                      |
|                               |
| (send a-window focus) → void? |
+-------------------------------+
```

キーボードのフォーカスを
ウィンドウが受け入れた場合、最上位ウィンドウを基準としたウィンドウ
キーボードのフォーカス。フォーカスがウィンドウの最上位にある場合
ウィンドウ、またはウィンドウの最上位ウィンドウが表示されていてフローティングであるかどうか
(つまり、'float スタイルで作成された場合)、フォーカスは次のとおりです。
すぐにこちらに移動しました
窓。それ以外の場合、フォーカスはすぐには移動されませんが、
ウィンドウのトップレベルウィンドウがキーボードフォーカスを取得します。フォーカスは
このウィンドウに委任されます。

こちらも参照
ピントが合った状態。

Unix では、キーボードのフォーカスがメニュー バーに移動する可能性があることに注意してください。
ユーザーがメニュー項目を選択しているとき。

現在のキーボード フォーカス ウィンドウを変更できます
ユーザーによって変更され、そのような変更はこのメソッドを介しません。オンフォーカスを使用して
フォーカスの変化を監視します。

```
+-----------------------------------------------+
| [メソッド]                                      |
|                                               |
| (send a-window get-client-handle) → cpointer? |
+-----------------------------------------------+
```

現在のウィンドウの「内側」へのハンドルを返します。
プラットフォームの GUI ツールボックス。ポインタが表す値は依存します
プラットフォーム上:

- Windows: `HWND`
- Mac OS: `NSView`
- Unix: `GtkWidget`

あわせて get-handle も参照。

```
+-----------------------------------------+
| [メソッド]                                |
|                                         |
| (send a-window get-client-size)         |
| → dimension-integer? dimension-integer? |
| dimension-integer?                      |
+-----------------------------------------+
```

ウィンドウの内部サイズをピクセル単位で取得します。コンテナの場合、
内部サイズは、サブウィンドウを配置できるサイズです (
境界マージン）。キャンバスの場合、これは表示される図面です
エリア。

クライアントのサイズは、幅と高さ (ピクセル単位) の 2 つの値として返されます。

こちらも参照
リフローコンテナ。

```
+----------------------------------------------------------+
| [メソッド]                                                 |
|                                                          |
| (send a-window get-cursor) → (or/c (is-a?/c cursor%) #f) |
+----------------------------------------------------------+
```

ウィンドウのカーソルを返します。このウィンドウのカーソルの場合は #f を返します。
デフォルトは親のカーソルです。参照
詳細については、set-cursor を参照。

```
+----------------------------------------+
| [メソッド]                               |
|                                        |
| (send a-window get-handle) → cpointer? |
+----------------------------------------+
```

現在のプラットフォームの GUI のウィンドウの「外側」へのハンドルを返します。
工具箱。ポインタが表す値は、
プラットフォーム:

- Windows: `HWND`
- Mac OS: トップレベルの window<%> オブジェクトの場合は `NSWindow`、
他のウィンドウの場合は `NSView`
- Unix: `GtkWidget`

あわせて get-client-handle も参照。

```
+-------------------------------------------------+
| [メソッド]                                        |
|                                                 |
| (send a-window get-height) → dimension-integer? |
+-------------------------------------------------+
```

ウィンドウの合計の高さ (ピクセル単位) を返します。

こちらも参照
リフローコンテナ。

```
+----------------------------------------------------------------------------+
| [メソッド]                                                                   |
|                                                                            |
| (send a-window get-label)                                                  |
| → (or/c label-string? (is-a?/c bitmap%) (or/c 'app 'caution 'stop) (list/c |
| (is-a?/c bitmap%) label-string? (or/c 'left 'top 'right 'bottom)) #f)      |
| (or/c label-string?                                                        |
| (is-a?/c bitmap%)                                                          |
| (or/c 'app 'caution 'stop)                                                 |
| (list/c (is-a?/c bitmap%)                                                  |
| label-string?                                                              |
| (or/c 'left 'top 'right 'bottom))                                          |
| #f)                                                                        |
|                                                                            |
| ```racket                                                                  |
| (or/c label-string?                                                        |
|       (is-a?/c bitmap%)                                                    |
|       (or/c 'app 'caution 'stop)                                           |
|       (list/c (is-a?/c bitmap%)                                            |
|               label-string?                                                |
|               (or/c 'left 'top 'right 'bottom))                            |
|       #f)                                                                  |
| ```                                                                        |
+----------------------------------------------------------------------------+
```

ウィンドウのラベルがある場合は、それを取得します。コントロール ウィンドウには通常、コントロール ウィンドウが表示されます。
何らかの方法でラベルを付けます。フレームとダイアログはラベルをウィンドウとして表示します
タイトル。パネルにはラベルが表示されませんが、ラベルは使用できます
識別目的のため。メッセージ、ボタン、チェックボックスは、
ビットマップ ラベルがある (ビットマップ ラベルを使用して作成された場合のみ)、
ただし、他のすべてのウィンドウには文字列ラベルが付いています。さらに、メッセージ
ラベルには、アイコン シンボル 'app、'caution、または
'stop、ボタンにはビットマップ ラベルと
文字列ラベル (ビットマップの位置とともに)。

ラベル文字列には & が含まれる場合があり、これは次のように機能します。
Windows および Unix 上のコントロールのキーボード ナビゲーションの注釈。の
アンパサンドは、コントロールの表示ラベルの一部ではありません。代わりに、
表示されたラベルからアンパサンドが削除されます (すべてのプラットフォームで)。
アンパサンドの前の文字には下線が付きます (Windows と
Unix)、その文字がニーモニックであることを示します。
コントロール。二重アンパサンドは単一アンパサンドに変換されます
(下線は表示されません)。こちらも参照
オントラバース文字。

ウィンドウにラベルがない場合は、#f が返されます。

```
+-----------------------------------------------------+
| [メソッド]                                            |
|                                                     |
| (send a-window get-plain-label) → (or/c string? #f) |
+-----------------------------------------------------+
```

いいね
get-label、ただし次の点を除きます。

- ラベルに (&c ) が含まれている場合
任意の文字 c、その後のシーケンスおよび周囲の任意の文字
空白は削除されます。
- ラベルに文字 c の &c が含まれている場合、
&は削除されます。
- ラベルにタブ文字が含まれている場合は、タブ文字とそれに続くすべての文字
文字が削除されます。

button% のラベルの処理も参照。

窓にある場合
ラベルもウィンドウもありません
label が文字列ではない場合、#f が返されます。

```
+-----------------------------------------+
| [メソッド]                                |
|                                         |
| (send a-window get-size)                |
| → dimension-integer? dimension-integer? |
| dimension-integer?                      |
+-----------------------------------------+
```

ウィンドウ全体の現在のサイズをピクセル単位で取得します。
水平方向と垂直方向の余白。 (Unix では、このサイズには
タイトル バーまたはフレーム/ダイアログの境界線)。
クライアントサイズを取得します。

ジオメトリは、幅と高さ (ピクセル単位) の 2 つの値として返されます。

こちらも参照
リフローコンテナ。

```
+------------------------------------------------+
| [メソッド]                                       |
|                                                |
| (send a-window get-width) → dimension-integer? |
+------------------------------------------------+
```

ウィンドウの現在の合計幅 (ピクセル単位) を返します。

こちらも参照
リフローコンテナ。

```
+-------------------------------------------+
| [メソッド]                                  |
|                                           |
| (send a-window get-x) → position-integer? |
+-------------------------------------------+
```

ウィンドウの左端の位置を返します。
親の座標系。

こちらも参照
リフローコンテナ。

```
+-------------------------------------------+
| [メソッド]                                  |
|                                           |
| (send a-window get-y) → position-integer? |
+-------------------------------------------+
```

ウィンドウの上端の位置を返します。
親の座標系。

こちらも参照
リフローコンテナ。

```
+---------------------------------------+
| [メソッド]                              |
|                                       |
| (send a-window has-focus?) → boolean? |
+---------------------------------------+
```

ウィンドウに現在キーボード フォーカスがあるかどうかを示します。参照
また
ピントが合った状態。

```
+----------------------------------------+
| [メソッド]                               |
|                                        |
| (send a-window is-enabled?) → boolean? |
+----------------------------------------+
```

ウィンドウが現在有効かどうかを示します。結果は
#t その祖先が有効になっているときにこのウィンドウが有効になっている場合、または
#f その祖先が無効になっているときにこのウィンドウが無効のままの場合
有効になりました。 (つまり、このメソッドの結果は呼び出しによってのみ影響を受けます。
の有効状態によってではなく、ウィンドウに対して有効にする
親ウィンドウ。)

```
+--------------------------------------+
| [メソッド]                             |
|                                      |
| (send a-window is-shown?) → boolean? |
+--------------------------------------+
```

ウィンドウが現在表示されているかどうかを示します。結果は
#t その祖先が表示されているときにこのウィンドウが表示される場合、または
#f その祖先が表示されたときにこのウィンドウが非表示のままの場合
示されています。 (つまり、このメソッドの結果は呼び出しによってのみ影響を受けます。
の可視性によってではなく、ウィンドウに対して表示する
親ウィンドウ。)

```
+-----------------------------------------------+
| [メソッド]                                      |
|                                               |
| (send a-window on-drop-file pathname) → void? |
| pathname: path?                              |
+-----------------------------------------------+
```

ユーザーがファイルを
窓。 (Unix では、ドラッグ アンド ドロップは XDND 経由でサポートされています)
）まず、ウィンドウに対してドラッグ アンド ドロップを有効にする必要があります。
ファイルのドロップを受け入れます。

Mac OS では、アプリケーションの実行中とユーザー
アプリケーションで処理されるファイルをダブルクリックするか、ファイルを
アプリケーションのアイコン、メインスレッドのアプリケーション ファイル ハンドラーは
呼ばれます（参照
アプリケーションファイルハンドラー)。デフォルトのハンドラーは、
ドラッグ アンド ドロップが有効な場合、最後にアクティブ化されたフレームの on-drop-file メソッド
フレームのイベントスペースとは独立して、そのフレームに対して有効になります（ただし、
メソッドはフレームのイベントスペースのハンドラーで呼び出されます
スレッド）。アプリケーションが実行されていないとき、ファイル名は次のようになります。
コマンドライン引数として指定されます。

```
+--------------------------------------+
| [メソッド]                             |
|                                      |
| (send a-window on-focus on?) → void? |
| on?: any/c                          |
+--------------------------------------+
```

仕様:
ウィンドウのときに呼び出されます
キーボードフォーカスを取得または失います。引数が #t の場合、
キーボード フォーカスは受信されましたが、それ以外の場合は失われます。

Unix では、キーボードのフォーカスがメニュー バーに移動する可能性があることに注意してください。
ユーザーがメニュー項目を選択しているとき。

既定の実装:
何もしない。

```
+-------------------------------------+
| [メソッド]                            |
|                                     |
| (send a-window on-move x y) → void? |
| x: position-integer?               |
| y: position-integer?               |
+-------------------------------------+
```

仕様:
ウィンドウが移動されたときに呼び出されます。 (トップレベルではないウィンドウの場合
ウィンドウの場合、「移動」は親ウィンドウの左上を基準にして移動することを意味します
) 新しい位置がメソッドに提供されます。

既定の実装:
何もしない。

```
+----------------------------------------------+
| [メソッド]                                     |
|                                              |
| (send a-window on-size width height) → void? |
| width: dimension-integer?                   |
| height: dimension-integer?                  |
+----------------------------------------------+
```

仕様:
ウィンドウのサイズが変更されるときに呼び出されます。ウィンドウの新しいサイズ (ピクセル単位)
メソッドに提供されます。サイズの値はウィンドウ全体のものです。
クライアント領域だけではありません。

既定の実装:
何もしない。

```
+----------------------------------+
| [メソッド]                         |
|                                  |
| (send a-window on-subwindow-char |
| receiver: (is-a?/c window<%>)   |
| event: (is-a?/c key-event%)     |
+----------------------------------+
```

仕様:
このウィンドウまたは子ウィンドウがキーボード イベントを受信したときに呼び出されます。
の
受信側のトップレベルウィンドウの on-subwindow-char メソッドが最初に呼び出されます (「
トップレベルウィンドウを取得);戻り値が #f の場合、
on-subwindow-char メソッドは、レシーバーへのパス内の次の子に対して呼び出されます。
など。最後に、受信者の場合、
on-subwindow-char メソッドは #f を返し、イベントは受信側のメソッドに渡されます。
通常のキー処理メカニズム。

イベント引数は、
受信窓。

サブウィンドウイベントのアトミック性制限が適用されます
on-subwindow-char にも。つまり、協調性が不十分である
on-subwind-char メソッドは効果的に無効にできます
#f を返した場合でも、コントロールによるキー イベントの処理

注意: デフォルト
フレーム%のon-subwind-charと
Dialog% メソッドの on-subwindow-char は、使用される特定のキーボード イベント (矢印キー、Enter など) を消費します。
ウィンドウ内を移動するためのものです。トップレベルウィンドウは
キーボード イベントを処理する最初の機会、一部のイベントは処理されない
デフォルトのフレームまたはダイアログを除いて、「受信者」の子に到達します。
メソッドはオーバーライドされます。

既定の実装:
#f を返す。

```
+-----------------------------------+
| [メソッド]                          |
|                                   |
| (send a-window on-subwindow-event |
| receiver: (is-a?/c window<%>)    |
| event: (is-a?/c mouse-event%)    |
+-----------------------------------+
```

仕様:
このウィンドウまたは子ウィンドウがマウス イベントを受信すると呼び出されます。
の
受信側のトップレベルウィンドウの on-subwindow-event メソッドが最初に呼び出されます (「
トップレベルウィンドウを取得);戻り値が #f の場合、
on-subwindow-event メソッドは、受信側へのパス内の次の子に対して呼び出されます。
など。最後に、受信者の場合、
on-subwindow-event メソッドは #f を返し、イベントは
受信機の通常のマウス操作メカニズム。

イベント引数は、
受信窓。

サブウィンドウ上のイベント メソッド チェーンが完了しない場合
アトミックに (つまり、他のスレッドを実行する必要がなく)、または完了しません
十分に速いと、対応するイベントがターゲットに配信されない可能性があります。
ボタンなどのコントロール。言い換えれば、協調性が不十分である
on-subwindow-event メソッドは効果的に
#f を返した場合でも、コントロールによるマウス イベントの処理。

既定の実装:
#f を返す。

```
+-----------------------------------+
| [メソッド]                          |
|                                   |
| (send a-window on-subwindow-focus |
| receiver: (is-a?/c window<%>)    |
| on?: boolean?                    |
+-----------------------------------+
```

仕様:
このウィンドウまたは子ウィンドウがキーボード フォーカスを受け取るか失うときに呼び出されます。
このメソッドは、受信機のオンフォーカス メソッドの後に呼び出されます。
の
受信側のトップレベルウィンドウの on-subwindow-focus メソッドが最初に呼び出されます (「
get-top-level-window)、次に
on-subwindow-focus メソッドは、受信側へのパス内の次の子に対して呼び出されます。
など。

既定の実装:
何もしない。

```
+---------------------------------------------------------+
| [メソッド]                                                |
|                                                         |
| (send a-window on-superwindow-activate active?) → void? |
| active?: any/c                                         |
+---------------------------------------------------------+
```

仕様: 含まれるトップレベルウィンドウ<%>が起動されるたびに、イベントキュー経由で呼び出されます。
アクティブ化または非アクティブ化されます (on-activate を参照)。

既定の実装: 何も行いません。

パッケージ `gui-lib` のバージョン 1.54 で追加。

```
+--------------------------------------------------------+
| [メソッド]                                               |
|                                                        |
| (send a-window on-superwindow-enable enabled?) → void? |
| enabled?: any/c                                       |
+--------------------------------------------------------+
```

仕様:
ウィンドウの有効状態が有効になるたびに、イベント キューを介して呼び出されます。
ウィンドウへの呼び出しを通じて変更されました
Enable メソッド、またはウィンドウのいずれかの有効化/無効化を通じて
先祖たち。メソッドの引数は、ウィンドウが現在表示されているかどうかを示します。
有効かどうか。

このメソッドは、ウィンドウが最初に作成されるときは呼び出されません。それはです
ウィンドウの初期有効状態からの変更後にのみ呼び出されます
状態。さらに、有効通知イベントがキューに入れられている場合、
ウィンドウが表示され、イベントが発生する前に有効な状態に戻ります。
発送された場合、発送はキャンセルされます。

ウィンドウの祖先の有効状態がウィンドウの実行中に変更された場合
削除されました (例: で削除されたため)
delete-child) の場合、削除されたウィンドウのキューにイネーブル イベントは追加されません。しかし、もし
ウィンドウは後で再度アクティブ化され、有効な状態になります。
非アクティブ化されたときのウィンドウの状態とは異なります。
イネーブルイベントはすぐにキューに入れられます。

既定の実装:
何もしない。

```
+----------------------------------------------------+
| [メソッド]                                           |
|                                                    |
| (send a-window on-superwindow-show shown?) → void? |
| shown?: any/c                                     |
+----------------------------------------------------+
```

仕様:
ウィンドウの可視性が確保されるたびに、イベント キューを介して呼び出されます。
ウィンドウへの呼び出しを通じて変更されました
ウィンドウの祖先の 1 つを表示/非表示にすることで表示する、または
ウィンドウまたはその祖先のアクティブ化または非アクティブ化を通じて
コンテナ内（例:
子を削除します）。メソッドの引数は、ウィンドウが現在表示されているかどうかを示します。
見えるか見えないか。

このメソッドは、ウィンドウが最初に作成されるときは呼び出されません。それはです
ウィンドウの初期状態からの変更後にのみ呼び出されます
視認性。さらに、表示通知イベントがキューに入れられている場合、
イベントが発生する前にウィンドウの可視性が元に戻ります。
発送された場合、発送はキャンセルされます。

既定の実装:
何もしない。

```
+---------------------------------------------+
| [メソッド]                                    |
|                                             |
| (send a-window popup-menu menu x y) → void? |
| menu: (is-a?/c popup-menu%)                |
| x: position-integer?                       |
| y: position-integer?                       |
+---------------------------------------------+
```

指定されたポップアップメニュー%オブジェクトを指定された位置にポップアップします。
(このウィンドウの座標内で) 座標を取得し、その後に戻ります
不特定多数のイベントを処理する。メニューはまだあるかもしれない
このメソッドが返されるとポップアップが表示されます。メニュー項目を選択した場合
ポップアップ メニューでは、メニュー項目のコールバックが呼び出されます。 (
メニュー項目のコールバックのイベントスペースはウィンドウのイベントスペースです)。

メニューがポップアップしている間、そのターゲットはウィンドウに設定されます。参照
ポップアップターゲットの取得
詳細については。

メニューはウィンドウ内の位置にポップアップ表示されます
(x、y)。

```
+---------------------------------+
| [メソッド]                        |
|                                 |
| (send a-window refresh) → void? |
+---------------------------------+
```

ウィンドウを再描画するためにウィンドウ更新イベントをキューに入れます。参照してください
イベントのタイプと優先度の詳細については、
イベントの優先順位について。

```
+---------------------------------------+
| [メソッド]                              |
|                                       |
| (send a-window screen->client x y)    |
| → position-integer? position-integer? |
| position-integer?                     |
| x: position-integer?                 |
| y: position-integer?                 |
+---------------------------------------+
```

グローバル座標をウィンドウに変換します
ローカル座標。詳細については、「クライアント -> 画面」も参照。
画面上の座標。

```
+-------------------------------------------+
| [メソッド]                                  |
|                                           |
| (send a-window set-cursor cursor) → void? |
| cursor: (or/c (is-a?/c cursor%) #f)      |
+-------------------------------------------+
```

ウィンドウのカーソルを設定します。カーソルの代わりに #f を提供する
値はウィンドウのカーソルを削除します。

ウィンドウにカーソルがない場合は、その親のカーソルが使用されます。
フレームとダイアログは標準の矢印カーソルとテキストで始まります
フィールドは I ビーム カーソルで始まります。他のすべてのウィンドウが作成されます
カーソルなしで。

```
+-------------------------------------+
| [メソッド]                            |
|                                     |
| (send a-window set-label l) → void? |
| l: label-string?                   |
+-------------------------------------+
```

ウィンドウのラベルを設定します。ウィンドウの自然な最小サイズは次のようになります。
ラベル変更後は異なりますが、ウィンドウの最小サイズ
は再計算されません。

ウィンドウがラベルを使用して作成されなかった場合、またはウィンドウがラベル付きで作成された場合
文字列以外のラベルを使用して作成された場合、l は無視されます。

参照
詳細については、get-label を参照。

```
+------------------------------------+
| [メソッド]                           |
|                                    |
| (send a-window show show?) → void? |
| show?: any/c                      |
+------------------------------------+
```

ウィンドウを表示または非表示にします。

ウィンドウの可視性を変更できます
たとえば、ユーザーがウィンドウのクローズ ボックスをクリックすることによって行われますが、そのような変更はこのメソッドを介しません。 on-superwindow-show または on-close を使用してください
可視性の変化を監視します。

ショーなら？が #f の場合、ウィンドウは非表示になります。それ以外の場合は、
ウィンドウが表示されます。

```
+------------------------------------------+
| [メソッド]                                 |
|                                          |
| (send a-window warp-pointer x y) → void? |
| x: position-integer?                    |
| y: position-integer?                    |
+------------------------------------------+
```

カーソルをウィンドウのローカル座標の指定された位置に移動します。

```
+-----------------------------------------------+
| [メソッド]                                      |
|                                               |
| (send a-window wheel-event-mode)              |
| → (or/c 'one 'integer 'fraction)              |
| (send a-window wheel-event-mode mode) → void? |
| mode: (or/c 'one 'integer 'fraction)         |
+-----------------------------------------------+
```

ウィンドウ内のマウス ホイール イベントのモードを取得または設定します。ホイール
イベントは key-event% インスタンスとして表されます。
key-event% の get-key-code は 'wheel-up を返します。
'wheel-down、'wheel-right、または 'wheel-left。
Windows のホイールイベント モードは変数の処理を決定します
ホイールサイズのイベントでは、基盤となるプラットフォームが報告されました。具体的には、
Wheel-event モードは、ウィンドウのシステム生成イベントに対する key-event% の get-wheel-steps の可能な値を決定します。

- 'one — ホイールイベントは常に単一のイベントについて報告されます。
ステップ。ウィンドウは、到達するまで増分を累積します。
完全なステップ、および個別のイベントを生成する場所
多段階の蓄積。
- 'integer — ホイール イベントは常に次のように報告されます。
整数サイズのステップ。小数ステップが累積され、
整数の増分に達するまで必要に応じて保存されます。
- 'fraction — ホイールイベントは陽性として報告されます
基礎となるものから受け取った直後の実際の値
プラットフォーム。

デフォルトのホイールイベント モードは 'one ですが、
editor-canvas% は、wheel-event モードを次のように初期化します。
'integer。

パッケージ `gui-lib` のバージョン 1.43 で追加。

