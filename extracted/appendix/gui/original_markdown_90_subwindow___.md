<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/subwindow___.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/subwindow___.html -->
<!-- Canonical English source for Japanese translation -->

```
+------------------------------------+------------+
| interfacesubwindow<%>: interface? |            |
+------------------------------------+------------+
| implements:                        | subarea<%> |
|                                    | window<%>  |
+------------------------------------+------------+
```

A subwindow<%> is a containee window.

```
+------------------------------------------------------------------------+
| [method]                                                               |
|                                                                        |
| (send a-subwindow reparent new-parent) → void?                         |
| new-parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) |
| (is-a?/c pane%))                                                       |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                               |
| (is-a?/c panel%) (is-a?/c pane%))                                      |
|                                                                        |
| ```racket                                                              |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                               |
|       (is-a?/c panel%) (is-a?/c pane%))                                |
| ```                                                                    |
+------------------------------------------------------------------------+
```

Removes the window from its current parent and makes it a child of
new-parent. The current and new parents must have the same
eventspace, and new-parent cannot be a descendant of
a-subwindow.

If a-subwindow is deleted within its current parent, it remains
deleted in new-parent. Similarly, if a-subwindow is shown in
its current parent, it is shown in new-parent.
