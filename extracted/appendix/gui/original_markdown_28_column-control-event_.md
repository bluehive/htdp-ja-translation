<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/column-control-event_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/column-control-event_.html -->
<!-- Canonical English source for Japanese translation -->

```
+-------------------------------------+
| classcolumn-control-event%: class? |
+-------------------------------------+
| superclass: control-event%          |
+-------------------------------------+
```

A column-control-event% object contains information about a
event on an list-box% column header. Except on Windows,
the 'clickable-headers style must be specified when
creating a list-box% for column events to be generated.

```
+--------------------------------------+
| [constructor]                        |
|                                      |
| (new column-control-event%           |
| → (is-a?/c column-control-event%)    |
| column: exact-nonnegative-integer?  |
| event-type: (or/c 'list-box-column) |
| time-stamp: exact-integer? = 0      |
+--------------------------------------+
```

The column argument indicates the column that was clicked.

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send a-column-control-event get-column) |
| → exact-nonnegative-integer?             |
+------------------------------------------+
```

Returns the column number (counting from 0) of the clicked column.

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send a-column-control-event set-column column) → void? |
| column: exact-nonnegative-integer?                     |
+---------------------------------------------------------+
```

Sets the column number (counting from 0) of the clicked column.
