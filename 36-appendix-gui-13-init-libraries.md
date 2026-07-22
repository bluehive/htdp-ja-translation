# 13 初期化ライブラリ

**原本:** `extracted/appendix/gui/original_markdown_13_Init_Libraries.md`  
**Source URL path:** `/gui/Init_Libraries.html`

```
+----------------------------+--------------------+
|  (require racket/gui/init) | package: `gui-lib` |
+----------------------------+--------------------+
+----------------------------+--------------------+
```

`racket/gui/init` ライブラリは、GRacket の既定の起動ライブラリです。`racket/init` と `racket/gui/base` を再エクスポートし、`current-load` を `text-editor-load-handler` を使うよう設定します。

```
+-----------------------------------+--------------------+
|  (require racket/gui/interactive) | package: `gui-lib` |
+-----------------------------------+--------------------+
+-----------------------------------+--------------------+
```

`racket/interactive` に類似しますが、GRacket 向けです。このライブラリは、`(find-config-dir)` 内の `"config.rktd"` ファイルで `'gui-interactive-file` を変更することで差し替えられます。さらに、`(find-system-path 'addon-dir)` に `"gui-interactive.rkt"` が存在する場合は、インストール全体のグラフィカル対話モジュールではなく、そのファイルが実行されます。

このライブラリは、ユーザのホームディレクトリに `(find-graphical-system-path 'init-file)` ファイルが存在すればそれを実行し、`(find-system-path 'init-file)` は使いません。`racket/interactive` と異なり、このライブラリは xrepl を起動しません。

パッケージ `gui-lib` のバージョン 1.27 で追加。
