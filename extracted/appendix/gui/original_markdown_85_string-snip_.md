<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/string-snip_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/string-snip_.html -->
<!-- Canonical English source for Japanese translation -->

```
+----------------------------+
| classstring-snip%: class? |
+----------------------------+
| superclass: snip%          |
+----------------------------+
```

An instance of string-snip% is created automatically when
text is inserted into a text editor. See also on-new-string-snip in text%.

```
+-----------------------------------------------------------------+
| [constructor]                                                   |
|                                                                 |
| (make-object string-snip% [allocsize]) → (is-a?/c string-snip%) |
| allocsize: exact-nonnegative-integer? = 0                      |
| (make-object string-snip% s) → (is-a?/c string-snip%)           |
| s: string?                                                     |
+-----------------------------------------------------------------+
```

Creates a string snip whose initial content is s, if
supplied, empty otherwise. In the latter case, the optional
allocsize argument is a hint about how much storage space
for text should be initially allocated by the snip.

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-string-snip insert s len [pos]) → void? |
| s: string?                                     |
| len: exact-nonnegative-integer?                |
| pos: exact-nonnegative-integer? = 0            |
+-------------------------------------------------+
```

Inserts s (with length len) into the snip at relative
position pos within the snip.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-string-snip read len f) → void? |
| len: exact-nonnegative-integer?        |
| f: (is-a?/c editor-stream-in%)         |
+-----------------------------------------+
```

Reads the snip’s data from the given stream.

The len argument specifies the maximum length of the text to
be read. (When a text snip is written to a file, the very first
field is the length of the text contained in the snip.) This method
is usually invoked by the text snip class’s read
method.
