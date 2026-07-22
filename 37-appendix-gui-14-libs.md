# 14 プラットフォーム依存関係

**原本:** `extracted/appendix/gui/original_markdown_14_libs.md`  
**Source URL path:** `/gui/libs.html`

`racket/draw` のプラットフォームライブラリ依存関係については、The Racket Drawing Toolkit の Platform Dependencies を参照してください。Unix では、そのライブラリが見つかり、かつ環境変数 `PLT_GTK2` が定義されていなければ GTK+ 3 が使われます。そうでなければ GTK+ 2 が使われます。いずれの場合も、`racket/gui/base` のために次の追加システムライブラリがインストールされている必要があります。

- `"libgdk-3.0[.0]"`（GTK+ 3）または `"libgdk-x11-2.0[.0]"`（GTK+ 2）
- `"libgdk_pixbuf-2.0[.0]"`（GTK+ 2）
- `"libgtk-3.0[.0]"`（GTK+ 3）または `"libgtk-x11-2.0[.0]"`（GTK+ 2）
- `"libgio-2.0[.0]"` — 省略可。インタフェースのスケーリング検出用
- `"libGL[.1]"` — 省略可。OpenGL サポート用
- `"libunique-1.0[.0]"` — 省略可。単一インスタンスサポート用（GTK+ 2）
