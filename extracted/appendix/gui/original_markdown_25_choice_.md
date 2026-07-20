<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/choice_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/choice_.html -->
<!-- Canonical English source for Japanese translation -->

> [image: choice.png]

```
+-----------------------+-----------------+
| classchoice%: class? |                 |
+-----------------------+-----------------+
| superclass: object%   |                 |
| extends:              | list-control<%> |
+-----------------------+-----------------+
```

A choice item allows the user to select one string item from a pop-up
list of items. Unlike a list box, only the currently selection is
visible until the user pops-up the menu of choices.

Whenever the selection of a choice item is changed by the user, the
choice item’s callback procedure is invoked. A callback procedure is
provided as an initialization argument when each choice item is
created.

See also list-box%.

```
+------------------------------------------------------------------------------+
| [constructor]                                                                |
|                                                                              |
| (new choice%                                                                 |
| → (is-a?/c choice%)                                                          |
| label: (or/c label-string? #f)                                              |
| choices: (listof label-string?)                                             |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c  |
| pane%))                                                                      |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                     |
| (is-a?/c panel%) (is-a?/c pane%))                                            |
| callback: ((is-a?/c choice%) (is-a?/c control-event%). ->. any) = (lambda |
| (c e) (void))                                                                |
| style: (listof (or/c 'horizontal-label 'vertical-label 'deleted)) = null    |
| (listof (or/c 'horizontal-label 'vertical-label                              |
| 'deleted))                                                                   |
| selection: exact-nonnegative-integer? = 0                                   |
| font: (is-a?/c font%) = normal-control-font                                 |
| enabled: any/c = #t                                                         |
| vert-margin: spacing-integer? = 2                                           |
| horiz-margin: spacing-integer? = 2                                          |
| min-width: (or/c dimension-integer? #f) = #f                                |
| min-height: (or/c dimension-integer? #f) = #f                               |
| stretchable-width: any/c = #f                                               |
| stretchable-height: any/c = #f                                              |
|                                                                              |
| ```racket                                                                    |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                     |
|       (is-a?/c panel%) (is-a?/c pane%))                                      |
| ```                                                                          |
|                                                                              |
| ```racket                                                                    |
| (listof (or/c 'horizontal-label 'vertical-label                              |
|               'deleted))                                                     |
| ```                                                                          |
+------------------------------------------------------------------------------+
```

Creates a choice item. If label is a string, it is used as the
label for the choice item.

If & occurs in label, it
is specially parsed as for button%.

The choices list specifies the initial list of user-selectable
items for the control. The initial set of choices determines the
control’s minimum graphical width (see Geometry Management for more
information).

The callback procedure is called (with the event type
'choice) when the user selects a choice item (or
re-selects the currently selected item).

If style includes 'vertical-label, then the choice item is
created with a label above the control; if style does not include
'vertical-label (and optionally includes 'horizontal-label), then the
label is created to the left of the choice item.
If style includes 'deleted, then the choice item is created as hidden,
and it does not affect its parent’s geometry; the choice item can be made active later by calling
parent’s add-child method.

By default, the first choice (if any) is initially selected. If
selection is positive, it is passed to
set-selection to set the initial choice selection. Although selection normally
must be less than the length of choices, it can be 0
when choices is empty.

The font argument determines the font for the control. For information about the enabled argument, see window<%>. For information about the horiz-margin and vert-margin
arguments, see subarea<%>. For information about the
min-width, min-height, stretchable-width, and
stretchable-height arguments, see area<%>.
