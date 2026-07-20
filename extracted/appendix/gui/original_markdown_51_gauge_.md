<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/gauge_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/gauge_.html -->
<!-- Canonical English source for Japanese translation -->

> [image: gauge.png]

```
+----------------------+------------+
| classgauge%: class? |            |
+----------------------+------------+
| superclass: object%  |            |
| extends:             | control<%> |
+----------------------+------------+
```

A gauge is a horizontal or vertical bar for displaying the output
value of a bounded integer quantity. Each gauge has an adjustable
range, and the gauge’s current value is always between 0 and its
range, inclusive. Use set-value to set the value
of the gauge.

```
+-------------------------------------------------------------------------------+
| [constructor]                                                                 |
|                                                                               |
| (new gauge%                                                                   |
| → (is-a?/c gauge%)                                                            |
| label: (or/c label-string? #f)                                               |
| range: positive-dimension-integer?                                           |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c   |
| pane%))                                                                       |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                      |
| (is-a?/c panel%) (is-a?/c pane%))                                             |
| style: (listof (or/c 'horizontal 'vertical 'vertical-label 'horizontal-label |
| 'deleted)) = '(horizontal)                                                    |
| (listof (or/c 'horizontal 'vertical                                           |
| 'vertical-label 'horizontal-label                                             |
| 'deleted))                                                                    |
| font: (is-a?/c font%) = normal-control-font                                  |
| enabled: any/c = #t                                                          |
| vert-margin: spacing-integer? = 2                                            |
| horiz-margin: spacing-integer? = 2                                           |
| min-width: (or/c dimension-integer? #f) = #f                                 |
| min-height: (or/c dimension-integer? #f) = #f                                |
| stretchable-width: any/c = (memq 'horizontal style)                          |
| stretchable-height: any/c = (memq 'vertical style)                           |
|                                                                               |
| ```racket                                                                     |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                      |
|       (is-a?/c panel%) (is-a?/c pane%))                                       |
| ```                                                                           |
|                                                                               |
| ```racket                                                                     |
| (listof (or/c 'horizontal 'vertical                                           |
|               'vertical-label 'horizontal-label                               |
|               'deleted))                                                      |
| ```                                                                           |
+-------------------------------------------------------------------------------+
```

If label is a string, it is used as the gauge label; otherwise
the gauge does not display a label.

If & occurs in label, it is specially parsed;
under Windows and X, the character
following & is underlined in the displayed control to
indicate a keyboard mnemonic. (Under Mac OS, mnemonic underlines are
not shown.) The mnemonic is meaningless for a gauge (as far as
on-traverse-char in top-level-window<%> is concerned),
but it is supported for consistency with other control types. A
programmer may assign a meaning to the mnemonic (e.g., by overriding
on-traverse-char).

The range argument is an integer specifying the maximum value of
the gauge (inclusive). The minimum gauge value is always 0.

The style list must include either 'horizontal,
specifying a horizontal gauge, or 'vertical, specifying a vertical
gauge. If style includes 'vertical-label, then the gauge is
created with a label above the control; if style does not include
'vertical-label (and optionally includes 'horizontal-label), then the
label is created to the left of the gauge. If style includes 'deleted, then the gauge is created as hidden,
and it does not affect its parent’s geometry; the gauge can be made active later by calling
parent’s add-child method.

The font argument determines the font for the control. For information about the enabled argument, see window<%>. For information about the horiz-margin and vert-margin
arguments, see subarea<%>. For information about the
min-width, min-height, stretchable-width, and
stretchable-height arguments, see area<%>.

```
+--------------------------------------------------------+
| [method]                                               |
|                                                        |
| (send a-gauge get-range) → positive-dimension-integer? |
+--------------------------------------------------------+
```

Returns the range (maximum value) of the gauge.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-gauge get-value) → dimension-integer? |
+-----------------------------------------------+
```

Returns the gauge’s current value.

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-gauge set-range range) → void? |
| range: positive-dimension-integer?    |
+----------------------------------------+
```

Sets the range (maximum value) of the gauge.

```
+--------------------------------------+
| [method]                             |
|                                      |
| (send a-gauge set-value pos) → void? |
| pos: dimension-integer?             |
+--------------------------------------+
```

Sets the gauge’s current value. If the specified value is larger than
the gauge’s range, an exn:fail:contract exception is raised.
