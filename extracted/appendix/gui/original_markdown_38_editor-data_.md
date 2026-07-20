<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/editor-data_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/editor-data_.html -->
<!-- Canonical English source for Japanese translation -->

```
+----------------------------+
| classeditor-data%: class? |
+----------------------------+
| superclass: object%        |
+----------------------------+
```

An editor-data% object contains extra data associated to a
snip or region in an editor. See also Editor Data.

```
+---------------------------------------------+
| [constructor]                               |
|                                             |
| (new editor-data%) → (is-a?/c editor-data%) |
+---------------------------------------------+
```

The element returned by get-next is initialized
to #f.

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send an-editor-data get-dataclass)      |
| → (or/c (is-a?/c editor-data-class%) #f) |
+------------------------------------------+
```

Gets the class for this data.

```
+------------------------------------+
| [method]                           |
|                                    |
| (send an-editor-data get-next)     |
| → (or/c (is-a?/c editor-data%) #f) |
+------------------------------------+
```

Gets the next editor data element in a list of editor data elements.
A #f terminates the list.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send an-editor-data set-dataclass v) → void? |
| v: (is-a?/c editor-data-class%)              |
+-----------------------------------------------+
```

Sets the class for this data.

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send an-editor-data set-next v) → void? |
| v: (or/c (is-a?/c editor-data%) #f)     |
+------------------------------------------+
```

Sets the next editor data element in a list of editor data elements.
A #f terminates the list.

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send an-editor-data write f) → boolean? |
| f: (is-a?/c editor-stream-out%)         |
+------------------------------------------+
```

Specification:
Writes the data to the specified stream, returning #t if data
is written successfully or #f otherwise.

Default implementation:
Returns #f.
