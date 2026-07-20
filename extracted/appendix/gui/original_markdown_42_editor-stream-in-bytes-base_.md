<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/editor-stream-in-bytes-base_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/editor-stream-in-bytes-base_.html -->
<!-- Canonical English source for Japanese translation -->

```
+--------------------------------------------+
| classeditor-stream-in-bytes-base%: class? |
+--------------------------------------------+
| superclass: editor-stream-in-base%         |
+--------------------------------------------+
```

An editor-stream-in-bytes-base% object can be used to
read editor data from a byte string.

```
+----------------------------------------------+
| [constructor]                                |
|                                              |
| (make-object editor-stream-in-bytes-base% s) |
| → (is-a?/c editor-stream-in-bytes-base%)     |
| s: bytes?                                   |
+----------------------------------------------+
```

Creates a stream base that reads from s.
