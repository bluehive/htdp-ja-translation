<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/pane_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/pane_.html -->
<!-- Canonical English source for Japanese translation -->

```
+---------------------+-------------------+
| classpane%: class? |                   |
+---------------------+-------------------+
| superclass: object% |                   |
| extends:            | area-container<%> |
|                     | subarea<%>        |
+---------------------+-------------------+
```

A pane is a both a container and a containee area. It serves only
as a geometry management device. A pane%
cannot be hidden or disabled like a panel% object.

A pane% object has a degenerate placement strategy for
managing its children: it places each child as if it was the only
child of the panel. The horizontal-pane% and
vertical-pane% classes provide useful geometry management
for multiple children.

See also grow-box-spacer-pane%.

Changed in version 1.3 of package `gui-lib`: Changed the placement strategy to
stretch and align children, instead of
placing all children at the top-left
corner.

```
+--------------------------------------------------------------------------------+
| [constructor]                                                                  |
|                                                                                |
| (new pane%                                                                     |
| → (is-a?/c pane%)                                                              |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c    |
| pane%))                                                                        |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                       |
| (is-a?/c panel%) (is-a?/c pane%))                                              |
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
| (list/c (or/c 'left 'center 'right)                                            |
|         (or/c 'top 'center 'bottom))                                           |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

For information about the horiz-margin and vert-margin
arguments, see subarea<%>. For information about the border, spacing, and alignment
arguments, see area-container<%>. For information about the
min-width, min-height, stretchable-width, and
stretchable-height arguments, see area<%>.
