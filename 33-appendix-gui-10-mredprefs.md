# 10 環境設定（Preferences）

**原本:** `extracted/appendix/gui/original_markdown_10_mredprefs.md`  
**Source URL path:** `/gui/mredprefs.html`

`racket/gui/base` ライブラリは、全体設定のためのいくつかの環境設定（preferences）をサポートしています。環境設定は、`find-system-path` が `'pref-file` に対して返す共通ファイルに格納され、値の取得と変更は `get-preference` および `put-preferences` を通じて行えます。`'GRacket:playcmd` 環境設定を除き、`racket/gui/base` ライブラリは以下の各環境設定を起動時に一度だけ読み取ります。

**注意：** 環境設定ファイルは（歴史的経緯により）大文字小文字を区別しないモードで読み取られるため、以下に挙げるシンボルは `|` で囲む必要があります。

GRacket が用いる環境設定名は次のとおりです。

- `'GRacket:default-font-size`  
  環境設定 — スタイルリスト内の基本スタイルの既定フォントサイズ、したがってエディタの既定フォントサイズを設定します。
- `'GRacket:defaultMenuPrefix`  
  環境設定 — Unix 上でメニュー項目ショートカットの既定接頭辞を設定します。`'ctl`、`'meta`、`'alt` のいずれかです。既定は `'ctl` です。この環境設定が `'meta` または `'alt` のとき、メニューラベル中の `&` で導入される下線付きニーモニックは抑制されます。
- `'GRacket:emacs-undo`  
  環境設定 — 真値のとき、エディタのアンドゥが既定で、取り消された操作を含むすべての編集履歴を保持します（Emacs と同様）。特定のエディタの設定は、`editor<%>` の `set-undo-preserves-all-history` メソッドで変更できます。
- `'GRacket:wheelStep`  
  環境設定 — `editor-canvas%` オブジェクトのマウスホイール既定ステップ量を設定します。
- `'GRacket:outline-inactive-selection`  
  環境設定 — 真値のとき、テキストエディタがキーボードフォーカスを持たない場合に、選択領域を輪郭で示します。
- `'GRacket:playcmd`  
  環境設定 — サウンド再生コマンドの書式に用います。詳細は `play-sound` を参照してください。
- `'GRacket:doubleClickTime`  
  環境設定 — ダブルクリックイベントのプラットフォーム固有の既定間隔（ミリ秒）を上書きします。

上記のいずれについても、GRacket 接頭辞付きの名前で環境設定値が見つからない場合は、後方互換のため MrEd 接頭辞付きの名前が試されます。
