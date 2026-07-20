<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/editor-stream-out-base_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/editor-stream-out-base_.html -->
<!-- Canonical English source for Japanese translation -->

```
+---------------------------------------+
| classeditor-stream-out-base%: class? |
+---------------------------------------+
| superclass: object%                   |
+---------------------------------------+
```

An editor-stream-out-base% object is used by an
editor-stream-out% object to perform low-level writing of
data.

The editor-stream-out-base% class is never instantiated
directly, but the derived class
editor-stream-out-bytes-base% can be instantiated. New
derived classes must override all of the methods described in this
section.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send an-editor-stream-out-base bad?) → boolean? |
+--------------------------------------------------+
```

Returns #t if there has been an error writing to the stream,
#f otherwise.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send an-editor-stream-out-base seek pos) → void? |
| pos: exact-nonnegative-integer?                  |
+---------------------------------------------------+
```

Moves to the specified absolute position in the stream.

```
+---------------------------------------+
| [method]                              |
|                                       |
| (send an-editor-stream-out-base tell) |
| → exact-nonnegative-integer?          |
+---------------------------------------+
```

Returns the current stream position.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send an-editor-stream-out-base write data) → void? |
| data: (listof char?)                               |
+-----------------------------------------------------+
```

Writes data (encoded as Latin-1 characters) to the stream. This method
is implemented by default via write-bytes.

```
+-----------------------------------------------------------+
| [method]                                                  |
|                                                           |
| (send an-editor-stream-out-base write-bytes bstr) → void? |
| bstr: bytes?                                             |
+-----------------------------------------------------------+
```

Writes data to the stream.
