<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/group-box-panel_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/group-box-panel_.html -->
<!-- Canonical English source for Japanese translation -->

> [image: group-box-panel.png]

```
+--------------------------------+
| classgroup-box-panel%: class? |
+--------------------------------+
| superclass: vertical-panel%    |
+--------------------------------+
```

A group-box panel arranges its subwindows in a single column, but also
draws an optional label at the top of the panel and a border around
the panel content.

Unlike most panel classes, a group-box panel’s horizontal and vertical
margins default to 2.

```
+--------------------------------------------------------------------------------+
| [constructor]                                                                  |
|                                                                                |
| (new group-box-panel%                                                          |
| → (is-a?/c group-box-panel%)                                                   |
| label: label-string?                                                          |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c    |
| pane%))                                                                        |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                       |
| (is-a?/c panel%) (is-a?/c pane%))                                              |
| style: (listof (or/c 'deleted)) = null                                        |
| font: (is-a?/c font%) = small-control-font                                    |
| enabled: any/c = #t                                                           |
| vert-margin: spacing-integer? = 2                                             |
| horiz-margin: spacing-integer? = 2                                            |
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

Creates a group pane whose title is label.

If style includes 'deleted, then the group panel is created as hidden,
and it does not affect its parent’s geometry; the group panel can be made active later by calling
parent’s add-child method.

The font argument determines the font for the control. For information about the enabled argument, see window<%>. For information about the horiz-margin and vert-margin
arguments, see subarea<%>. For information about the
min-width, min-height, stretchable-width, and
stretchable-height arguments, see area<%>.
