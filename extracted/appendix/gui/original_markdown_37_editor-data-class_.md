<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/editor-data-class_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/editor-data-class_.html -->
<!-- Canonical English source for Japanese translation -->

```
+----------------------------------+
| classeditor-data-class%: class? |
+----------------------------------+
| superclass: object%              |
+----------------------------------+
```

An editor-data-class% object defines a type for
editor-data% objects. See also Editor Data.

```
+---------------------------------------------------------+
| [constructor]                                           |
|                                                         |
| (new editor-data-class%) → (is-a?/c editor-data-class%) |
+---------------------------------------------------------+
```

Creates a (useless) instance.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send an-editor-data-class get-classname) → string? |
+-----------------------------------------------------+
```

Gets the name of the class. Names starting with wx are reserved for
internal use.

```
+------------------------------------+
| [method]                           |
|                                    |
| (send an-editor-data-class read f) |
| → (or/c (is-a?/c editor-data%) #f) |
| f: (is-a?/c editor-stream-in%)    |
+------------------------------------+
```

Reads a new data object from the given stream, returning #f if
there is an error.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send an-editor-data-class set-classname v) → void? |
| v: string?                                         |
+-----------------------------------------------------+
```

Sets the name of the class. Names starting with wx are
reserved for internal use.

An editor data class name should usually have the form "(lib\n...)" to enable on-demand loading of the class; see
Editor Data for details.
