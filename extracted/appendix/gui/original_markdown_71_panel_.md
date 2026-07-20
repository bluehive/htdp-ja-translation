<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/panel_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/panel_.html -->
<!-- Canonical English source for Japanese translation -->

> [image: panel.png]

```
+----------------------+--------------------------+
| classpanel%: class? |                          |
+----------------------+--------------------------+
| superclass: object%  |                          |
| extends:             | area-container-window<%> |
|                      | subwindow<%>             |
+----------------------+--------------------------+
```

A panel is a both a container and a containee window. It serves mainly
as a geometry management device, but the 'border creates a
container with a border. Unlike a pane% object, a panel%
object can be hidden or disabled.

A panel% object has a degenerate placement strategy for
managing its children: it places each child as if it was the only
child of the panel. The horizontal-panel% and
vertical-panel% classes provide useful geometry management
for multiple children.

Changed in version 1.3 of package `gui-lib`: Changed the placement strategy to
stretch and align children, instead of
placing all children at the top-left
corner.

```
+--------------------------------------------------------------------------------+
| [constructor]                                                                  |
|                                                                                |
| (new panel%                                                                    |
| → (is-a?/c panel%)                                                             |
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
| '(center center)                                                               |
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

If the 'border style is specified, the window is created with
a thin border (in which case the client size of the panel may be
less than its total size). If style includes 'deleted, then the panel is created as hidden,
and it does not affect its parent’s geometry; the panel can be made active later by calling
parent’s add-child method.

If the 'hscroll or 'vscroll style is specified, then
the panel includes a scrollbar in the corresponding direction, and
the panel’s own size in the corresponding direction is not
constrained by the size of its children subareas. The 'auto-hscroll
and 'auto-vscroll styles imply 'hscroll and
'vscroll, respectively, but they cause the corresponding scrollbar to
disappear when no scrolling is needed in the corresponding direction;
the 'auto-vscroll and 'auto-hscroll modes assume that
children subareas are placed using the default algorithm for a panel%,
vertical-panel%, or horizontal-panel%. The 'hide-hscroll
and 'hide-vscroll styles imply 'auto-hscroll and
'auto-vscroll, respectively, but the corresponding scroll bar is never
made visible (while still allowing the panel content to exceed its own size).

For information about the enabled argument, see window<%>. For information about the horiz-margin and vert-margin
arguments, see subarea<%>. For information about the border, spacing, and alignment
arguments, see area-container<%>. For information about the
min-width, min-height, stretchable-width, and
stretchable-height arguments, see area<%>.

Changed in version 1.25 of package `gui-lib`: Added 'hide-vscroll and 'hide-hscroll.
