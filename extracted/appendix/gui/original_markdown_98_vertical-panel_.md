<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/vertical-panel_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/vertical-panel_.html -->
<!-- Canonical English source for Japanese translation -->

```
+-------------------------------+
| classvertical-panel%: class? |
+-------------------------------+
| superclass: panel%            |
+-------------------------------+
```

A vertical panel arranges its subwindows in a single column. See
also panel%.

```
+--------------------------------------------------------------------------------+
| [constructor]                                                                  |
|                                                                                |
| (new vertical-panel%                                                           |
| → (is-a?/c vertical-panel%)                                                    |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c    |
| pane%))                                                                        |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                       |
| (is-a?/c panel%) (is-a?/c pane%))                                              |
| style: (listof (or/c 'border 'deleted 'hscroll 'auto-hscroll 'hide-hscroll    |
| 'vscroll 'auto-vscroll 'hide-vscroll)) = null                                  |
| (listof (or/c 'border 'deleted                                                 |
| 'hscroll 'auto-hscroll 'hide-hscroll                                           |
| 'vscroll 'auto-vscroll 'hide-vscroll))                                         |
| enabled: any/c = #t                                                           |
| vert-margin: spacing-integer? = 0                                             |
| horiz-margin: spacing-integer? = 0                                            |
| border: spacing-integer? = 0                                                  |
| spacing: spacing-integer? = 0                                                 |
| alignment: (list/c (or/c 'left 'center 'right) (or/c 'top 'center 'bottom)) = |
| '(center top)                                                                  |
| (list/c (or/c 'left 'center 'right)                                            |
| (or/c 'top 'center 'bottom))                                                   |
| min-width: (or/c dimension-integer? #f) = #f                                  |
| min-height: (or/c dimension-integer? #f) = #f                                 |
| stretchable-width: any/c = #t                                                 |
| stretchable-height: any/c = #t                                                |
|                                                                                |
| ```racket                                                                      |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                       |
|       (is-a?/c panel%) (is-a?/c pane%))                                        |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (listof (or/c 'border 'deleted                                                 |
|               'hscroll 'auto-hscroll 'hide-hscroll                             |
|               'vscroll 'auto-vscroll 'hide-vscroll))                           |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (list/c (or/c 'left 'center 'right)                                            |
|         (or/c 'top 'center 'bottom))                                           |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

The style flags are the same as for panel%.

For information about the enabled argument, see window<%>. For information about the horiz-margin and vert-margin
arguments, see subarea<%>. For information about the border, spacing, and alignment
arguments, see area-container<%>. For information about the
min-width, min-height, stretchable-width, and
stretchable-height arguments, see area<%>.

```
+-------------------------------------------------------------+
| [method]                                                    |
|                                                             |
| (send a-vertical-panel set-orientation horizontal?) → void? |
| horizontal?: boolean?                                      |
+-------------------------------------------------------------+
```

Sets the orientation of the panel, switching it between
the behavior of the vertical-panel% and that of
the horizontal-panel%.

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-vertical-panel get-orientation) → boolean? |
+----------------------------------------------------+
```

Initially returns #f, but if
set-orientation is called,
this method returns whatever the last value passed to it was.
