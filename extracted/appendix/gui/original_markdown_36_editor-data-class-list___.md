<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/editor-data-class-list___.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/editor-data-class-list___.html -->
<!-- Canonical English source for Japanese translation -->

```
+-------------------------------------------------+
| interfaceeditor-data-class-list<%>: interface? |
+-------------------------------------------------+
+-------------------------------------------------+
```

Each eventspace has an instance of editor-data-class-list<%>,
obtained with (get-the-editor-data-class-list). New
instances cannot be created directly. This list keeps a list of
editor data classes; this list is needed for loading snips from a
file. See also Editor Data.

```
+--------------------------------------------------------+
| [method]                                               |
|                                                        |
| (send an-editor-data-class-list add snipclass) → void? |
| snipclass: (is-a?/c editor-data-class%)               |
+--------------------------------------------------------+
```

Adds a snip data class to the list. If a class with the same name already
exists in the list, this one will not be added.

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send an-editor-data-class-list find name) |
| → (or/c (is-a?/c snip-class%) #f)          |
| name: string?                             |
+--------------------------------------------+
```

Finds a snip data class from the list with the given name, returning
#f if none can be found.

```
+------------------------------------------------------+
| [method]                                             |
|                                                      |
| (send an-editor-data-class-list find-position class) |
| → exact-nonnegative-integer?                         |
| class: (is-a?/c editor-data-class%)                 |
+------------------------------------------------------+
```

Returns an index into the list for the specified class.

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send an-editor-data-class-list nth n)   |
| → (or/c (is-a?/c editor-data-class%) #f) |
| n: exact-nonnegative-integer?           |
+------------------------------------------+
```

Returns the nth class in the list (counting from 0), returning
#f if the list has n or less classes.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send an-editor-data-class-list number) |
| → exact-nonnegative-integer?            |
+-----------------------------------------+
```

Returns the number of editor data classes in the list.
