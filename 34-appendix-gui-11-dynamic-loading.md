# 11 動的読み込み

**原本:** `extracted/appendix/gui/original_markdown_11_Dynamic_Loading.md`  
**Source URL path:** `/gui/Dynamic_Loading.html`

```
+-------------------------------+-----------------+
|  (require racket/gui/dynamic) | package: `base` |
+-------------------------------+-----------------+
+-------------------------------+-----------------+
```

`racket/gui/dynamic` ライブラリは、`racket/gui` や `racket/gui/base` を直接 require する代わりに、`racket/gui/base` ライブラリへ動的にアクセスするための関数を提供します。

```
+-----------------------------+
| [手続き]                    |
|                             |
| (gui-available?) → boolean? |
+-----------------------------+
```

GUI 束縛への動的アクセスが利用可能なら `#t` を返します。束縛が利用可能になるのは、`racket/gui/base` が読み込まれ、インスタンス化され、かつ `racket/gui/dynamic` がインスタンス化された名前空間にアタッチされている場合です。

```
+---------------------------------+
| [手続き]                        |
|                                 |
| (gui-dynamic-require sym) → any |
| sym: symbol?                   |
+---------------------------------+
```

`dynamic-require` と同様ですが、特に `racket/gui/base` のエクスポートへアクセスするためのものであり、`(gui-available?)` が真を返すときに限って用います。

`gui-dynamic-require` は、主に `(gui-available?)` 条件の下での利用を想定しています。`'racket/gui/base` に対する `dynamic-require` の短縮形としても使えますが、その場合も束縛が利用可能であることを先に確認する必要があります。`(gui-available?)` が真を返すように `racket/gui/base` の束縛を利用可能にする一つの方法は、`dynamic-require` を用いることです。

```racket
(dynamic-require 'racket/gui/base #f)
```

`require` と異なり、`dynamic-require` を使うと、`racket/gui/base` のインスタンス化は `dynamic-require` の実行時呼び出しまで遅延されます。こうして `racket/gui/base` が宣言されたうえで、`gui-dynamic-require` により束縛へアクセスできます。

```racket
(define window (new (gui-dynamic-require 'frame%)
                    [label "Frame"]))
(send window show #t)
```
