<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/editor-snip-editor-admin___.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/editor-snip-editor-admin___.html -->
<!-- Canonical English source for Japanese translation -->

```
+--------------------------------------------------+
| interfaceeditor-snip-editor-admin<%>: interfac… |
+--------------------------------------------------+
+--------------------------------------------------+
```

An instance of this administrator interface is created with each
editor-snip% object; new instances cannot be
created directly.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send an-editor-snip-editor-admin get-snip) |
| → (is-a?/c editor-snip%)                    |
+---------------------------------------------+
```

Returns the snip that owns this administrator (and displays the
editor controlled by the administrator, if any).
