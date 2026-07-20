<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/editor-stream-out-bytes-base_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/editor-stream-out-bytes-base_.html -->
<!-- Canonical English source for Japanese translation -->

```
+---------------------------------------------+
| classeditor-stream-out-bytes-base%: class? |
+---------------------------------------------+
| superclass: editor-stream-out-base%         |
+---------------------------------------------+
```

An editor-stream-out-bytes-base% object can be used to write
editor data into a byte string.

```
+-------------------------------------------+
| [constructor]                             |
|                                           |
| (new editor-stream-out-bytes-base%)       |
| → (is-a?/c editor-stream-out-bytes-base%) |
+-------------------------------------------+
```

Creates an empty stream.

```
+-----------------------------------------------------------+
| [method]                                                  |
|                                                           |
| (send an-editor-stream-out-bytes-base get-bytes) → bytes? |
+-----------------------------------------------------------+
```

Returns the current contents of the stream.
