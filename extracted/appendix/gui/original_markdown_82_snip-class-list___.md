<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/snip-class-list___.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/snip-class-list___.html -->
<!-- Canonical English source for Japanese translation -->

```
+------------------------------------------+
| interfacesnip-class-list<%>: interface? |
+------------------------------------------+
+------------------------------------------+
```

Each eventspace has its own instance of snip-class-list<%>,
obtained with (get-the-snip-class-list). New instances
cannot be created directly. Each instance keeps a list of snip
classes. This list is needed for loading snips from a file. See also
Snip Classes.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-snip-class-list add snipclass) → void? |
| snipclass: (is-a?/c snip-class%)              |
+------------------------------------------------+
```

Adds a snip class to the list. If a class with the same name already
exists in the list, this one will not be added.

```
+------------------------------------+
| [method]                           |
|                                    |
| (send a-snip-class-list find name) |
| → (or/c (is-a?/c snip-class%) #f)  |
| name: string?                     |
+------------------------------------+
```

Finds a snip class from the list with the given name, returning
#f if none is found.

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-snip-class-list find-position class) |
| → exact-nonnegative-integer?                 |
| class: (is-a?/c snip-class%)                |
+----------------------------------------------+
```

Returns an index into the list for the specified class.

```
+-----------------------------------+
| [method]                          |
|                                   |
| (send a-snip-class-list nth n)    |
| → (or/c (is-a?/c snip-class%) #f) |
| n: exact-nonnegative-integer?    |
+-----------------------------------+
```

Returns the nth class in the list, or #f if
the list has n classes or less.

```
+--------------------------------------------------------------+
| [method]                                                     |
|                                                              |
| (send a-snip-class-list number) → exact-nonnegative-integer? |
+--------------------------------------------------------------+
```

Returns the number of snip classes in the list.
