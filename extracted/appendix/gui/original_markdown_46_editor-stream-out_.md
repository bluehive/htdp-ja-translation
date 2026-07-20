<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/editor-stream-out_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/editor-stream-out_.html -->
<!-- Canonical English source for Japanese translation -->

```
+----------------------------------+
| classeditor-stream-out%: class? |
+----------------------------------+
| superclass: object%              |
+----------------------------------+
```

An editor-stream-out% object is used to write editor
information to a file or other output stream (such as the
clipboard).

```
+------------------------------------------+
| [constructor]                            |
|                                          |
| (make-object editor-stream-out% base)    |
| → (is-a?/c editor-stream-out%)           |
| base: (is-a?/c editor-stream-out-base%) |
+------------------------------------------+
```

An out-stream base—possibly an
editor-stream-out-bytes-base% object—must be supplied in
base.

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send an-editor-stream-out jump-to pos) → void? |
| pos: exact-nonnegative-integer?                |
+-------------------------------------------------+
```

Jumps to a given position in the stream.

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send an-editor-stream-out ok?) → boolean? |
+--------------------------------------------+
```

Returns #t if the stream is ready for writing, #f otherwise.
Writing to a bad stream has no effect.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send an-editor-stream-out pretty-finish) → void? |
+---------------------------------------------------+
```

Ensures that the stream ends with a newline.
This method is called by
write-editor-global-footer.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send an-editor-stream-out pretty-start) → void? |
+--------------------------------------------------+
```

Writes a “comment” into the stream that identifies the file format.
This method is called by write-editor-global-header.

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send an-editor-stream-out put n v) |
| → (is-a?/c editor-stream-out%)      |
| n: exact-nonnegative-integer?      |
| v: bytes?                          |
| (send an-editor-stream-out put v)   |
| → (is-a?/c editor-stream-out%)      |
| v: bytes?                          |
| (send an-editor-stream-out put v)   |
| → (is-a?/c editor-stream-out%)      |
| v: exact-integer?                  |
| (send an-editor-stream-out put v)   |
| → (is-a?/c editor-stream-out%)      |
| v: real?                           |
+-------------------------------------+
```

Writes v, or n bytes of v.

When n is supplied with a byte-string v, use
get-unterminated-bytes to read the bytes
later. This is the recommended way to write out bytes to
be easily read in later; use get-unterminated-bytes to read the bytes back in.

If n is not supplied and v is a byte string, then
for historical reasons, the actual number of bytes written includes a
#\nul terminator, so use get-bytes instead of get-unterminated-bytes to read the bytes later.

If v is a real?, but not an
exact-integer?, then it is converted to an inexact
number as part of the process of writing it.

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send an-editor-stream-out put-fixed v)  |
| → (is-a?/c editor-stream-out%)           |
| v: (integer-in -9999999999 99999999999) |
+------------------------------------------+
```

Puts a fixed-sized integer into the stream. This method is needed
because numbers are usually written in a way that takes varying
numbers of bytes. In some cases it is useful to temporary write a
0 to a stream, write more data, and then go back and change
the 0 to another number; such a process requires a
fixed-size number.

Numbers written to a stream with put-fixed
must be read with get-fixed-exact
or get-fixed.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send an-editor-stream-out put-unterminated v) |
| → (is-a?/c editor-stream-out%)                 |
| v: bytes?                                     |
+------------------------------------------------+
```

The same as calling put with
(bytes-lengthv) and v.

```
+---------------------------------------------------------------+
| [method]                                                      |
|                                                               |
| (send an-editor-stream-out tell) → exact-nonnegative-integer? |
+---------------------------------------------------------------+
```

Returns the current stream position.
