<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/editor-stream-in-base_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/editor-stream-in-base_.html -->
<!-- Canonical English source for Japanese translation -->

```
+--------------------------------------+
| classeditor-stream-in-base%: class? |
+--------------------------------------+
| superclass: object%                  |
+--------------------------------------+
```

An editor-stream-in-base% object is used by an
editor-stream-in% object to perform low-level reading of
data.

The editor-stream-in-base% class is never instantiated
directly, but the derived class editor-stream-in-bytes-base%
can be instantiated. New derived classes must override all of the
methods described in this section.

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send an-editor-stream-in-base bad?) → boolean? |
+-------------------------------------------------+
```

Returns #t if there has been an error reading from the
stream, #f otherwise.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send an-editor-stream-in-base read data) |
| → exact-nonnegative-integer?              |
| data: (and/c vector? (not immutable?))   |
+-------------------------------------------+
```

Like read-bytes, but fills a supplied
vector with Latin-1 characters instead of filling a byte string. This method
is implemented by default via read-bytes.

```
+--------------------------------------------------------+
| [method]                                               |
|                                                        |
| (send an-editor-stream-in-base read-bytes              |
| → exact-nonnegative-integer?                           |
| bstr: (and/c bytes? (not immutable?))                 |
| start: exact-nonnegative-integer? = 0                 |
| end: exact-nonnegative-integer? = (bytes-length bstr) |
+--------------------------------------------------------+
```

Reads bytes to fill the supplied byte string. The return value is the
number of bytes read, which may be less than the number
requested if the stream is emptied. If the stream is emptied, the
next call to bad? must return
#t.

The bytes that are read are stored in bstr starting
at position start and going to at most to
end.

```
+-------------------------------------------------------------+
| [method]                                                    |
|                                                             |
| (send an-editor-stream-in-base read-byte) → (or/c byte? #f) |
+-------------------------------------------------------------+
```

Reads a single byte and return it, or returns #f if no more
bytes are available. The default implementation of this method uses
read-bytes.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send an-editor-stream-in-base seek pos) → void? |
| pos: exact-nonnegative-integer?                 |
+--------------------------------------------------+
```

Moves to the specified absolute position in the stream.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send an-editor-stream-in-base skip n) → void? |
| n: exact-nonnegative-integer?                 |
+------------------------------------------------+
```

Skips past the next n characters in the stream.

```
+--------------------------------------+
| [method]                             |
|                                      |
| (send an-editor-stream-in-base tell) |
| → exact-nonnegative-integer?         |
+--------------------------------------+
```

Returns the current stream position.
