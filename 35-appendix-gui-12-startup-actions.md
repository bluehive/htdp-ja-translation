# 12 起動時の動作

**原本:** `extracted/appendix/gui/original_markdown_12_Startup_Actions.md`  
**Source URL path:** `/gui/Startup_Actions.html`

`racket/gui/base` モジュールは、オペレーティングシステムプロセスごとに一度だけインスタンス化できます。これは、Racket のスレッドスケジューリングと GUI イベントを協調させるため、Racket 実行時システムにフックを設定するからです。二度目のインスタンス化を試みると例外が発生します。さらに Mac OS では、`racket/gui/base` の唯一のインスタンス化は、そのプロセスの元の place で行う必要があります。

`racket/gui/base` をインスタンス化すると、次の二つのパラメータが設定されます。

- `executable-yield-handler` — 実行可能ファイル用の yield ハンドラは、以前にインストールされていたハンドラへ連鎖する前に `(yield initial-eventspace)` を評価するよう設定されます。その結果、Racket プロセスは通常、初期イベントスペース内のすべてのトップレベルウィンドウが閉じられ、すべてのコールバックが呼び出され、すべてのタイマが停止するまで待ってから終了します。
- `current-get-interaction-input-port` — 対話ポート用ハンドラは、以前にインストールされていたハンドラの結果を包み、入力ポートが読み取りでブロックするときに GUI イベントへ yield するよう設定されます。この既定ハンドラの拡張は、現在のスレッドがあるイベントスペースのハンドラスレッドである場合にのみ発動し、そのとき `current-eventspace` は yield を呼び出す前にそのイベントスペースに設定されます。その結果、（素の Racket 実行可能ファイルが走らせるような）`read-eval-print-loop` が入力でブロックしているあいだも、通常は GUI イベントを処理できます。

`racket/gui/base` がインスタンス化されたスレッドは、初期イベントスペースのハンドラスレッドにもなります。イベントスペースとスレッドも参照してください。
