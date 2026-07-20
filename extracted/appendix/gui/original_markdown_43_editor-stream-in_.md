<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/editor-stream-in_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/editor-stream-in_.html -->
<!-- Canonical English source for Japanese translation -->

```
+---------------------------------+
| classeditor-stream-in%: class? |
+---------------------------------+
| superclass: object%             |
+---------------------------------+
```

An editor-stream-in% object is used to read editor
information from a file or other input stream (such as the
clipboard).

```
+-----------------------------------------+
| [constructor]                           |
|                                         |
| (make-object editor-stream-in% base)    |
| → (is-a?/c editor-stream-in%)           |
| base: (is-a?/c editor-stream-in-base%) |
+-----------------------------------------+
```

An in-stream base—possibly an editor-stream-in-bytes-base%
object—must be supplied in base.

```
+----------------------------------------------------------------+
| [method]                                                       |
|                                                                |
| (send an-editor-stream-in get v) → (is-a?/c editor-stream-in%) |
| v: (box/c exact-integer?)                                     |
| (send an-editor-stream-in get v) → (is-a?/c editor-stream-in%) |
| v: (box/c real?)                                              |
+----------------------------------------------------------------+
```

Reads data from the stream, returning itself.
Reading from a bad stream always gives 0.

The v box is filled with the next integer or floating-point value in the stream.

```
+---------------------------------------------------------------+
| [method]                                                      |
|                                                               |
| (send an-editor-stream-in get-bytes [len]) → (or/c bytes? #f) |
| len: (or/c (box/c exact-nonnegative-integer?) #f) = #f       |
+---------------------------------------------------------------+
```

Like get-unterminated-bytes, but the last
read byte is assumed to be a nul terminator and discarded. Use this
method when data is written by a call to put without an explicit byte count, and use
get-unterminated-bytes when data is
written with an explicit byte count.

The len box is filled with the length of the byte string plus one (to indicate the terminator), unless len is #f.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send an-editor-stream-in get-exact)           |
| → (or/c exact-integer? (and/c real? inexact?)) |
+------------------------------------------------+
```

Returns the next number value in the stream. Despite the
name, this method may return an inexact number, but only if
the next element in the stream was actually written as an
inexact number.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send an-editor-stream-in get-fixed v)           |
| → (is-a?/c editor-stream-in%)                    |
| v: (box/c (integer-in -9999999999 99999999999)) |
+--------------------------------------------------+
```

The v box is filled with a fixed-size integer from the stream obtained through
get-fixed-exact.

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send an-editor-stream-in get-fixed-exact) |
| → (integer-in -9999999999 99999999999)     |
+--------------------------------------------+
```

Gets a fixed-sized integer from the stream. See
put-fixed for more information.
Reading from a bad stream always gives 0.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send an-editor-stream-in get-inexact) → real? |
+------------------------------------------------+
```

Returns the next floating-point value in the stream.

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send an-editor-stream-in get-unterminated-bytes [len]) |
| → (or/c bytes? #f)                                      |
| len: (or/c (box/c exact-nonnegative-integer?) #f) = #f |
+---------------------------------------------------------+
```

Returns the next byte string from the stream. This is
the recommended way to read bytes back in from a stream;
use put with two arguments
(passing along the length of the bytes) to write out the bytes
to match this method.

Reading from a bad stream returns #f or #"".

Note that when put is not given a byte
length, it includes an extra byte for a nul terminator; use
get-bytes to read such byte strings.

The len box is filled with the length of the byte string, unless len is #f.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send an-editor-stream-in jump-to pos) → void? |
| pos: exact-nonnegative-integer?               |
+------------------------------------------------+
```

Jumps to a given position in the stream.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send an-editor-stream-in ok?) → boolean? |
+-------------------------------------------+
```

Returns #t if the stream is ready for reading, #f otherwise.
Reading from a bad stream always returns 0 or "".

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send an-editor-stream-in remove-boundary) → void? |
+----------------------------------------------------+
```

See set-boundary.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send an-editor-stream-in set-boundary n) → void? |
| n: exact-nonnegative-integer?                    |
+---------------------------------------------------+
```

Sets a file-reading boundary at n bytes past the current
stream location. If there is an attempt to read past this boundary,
an error is signaled. The boundary is removed with a call to
remove-boundary. Every call to
set-boundary must be balanced by a call to
remove-boundary.

Boundaries help keep a subroutine from reading too much data leading
to confusing errors. However, a malicious subroutine can call
remove-boundary on its own.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send an-editor-stream-in skip n) → void? |
| n: exact-nonnegative-integer?            |
+-------------------------------------------+
```

Skips past the next n bytes in the stream.

```
+--------------------------------------------------------------+
| [method]                                                     |
|                                                              |
| (send an-editor-stream-in tell) → exact-nonnegative-integer? |
+--------------------------------------------------------------+
```

Returns the current stream position.
