<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/check-box_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/check-box_.html -->
<!-- Canonical English source for Japanese translation -->

> [image: check-box.png]

```
+--------------------------+------------+
| classcheck-box%: class? |            |
+--------------------------+------------+
| superclass: object%      |            |
| extends:                 | control<%> |
+--------------------------+------------+
```

A check box is a labeled box which is either checked or unchecked.

Whenever a check box is clicked by the user, the check box’s value is
toggled and its callback procedure is invoked. A callback procedure
is provided as an initialization argument when each check box is
created.

```
+-----------------------------------------------------------------------------+
| [constructor]                                                               |
|                                                                             |
| (new check-box%                                                             |
| → (is-a?/c check-box%)                                                      |
| label: (or/c label-string? (is-a?/c bitmap%))                              |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c |
| pane%))                                                                     |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                    |
| (is-a?/c panel%) (is-a?/c pane%))                                           |
| callback: ((is-a?/c check-box%) (is-a?/c control-event%). ->. any) =     |
| (lambda (c e) (void))                                                       |
| ((is-a?/c check-box%) (is-a?/c control-event%)                              |
|. ->. any)                                                                 |
| style: (listof (or/c 'deleted)) = null                                     |
| value: any/c = #f                                                          |
| font: (is-a?/c font%) = normal-control-font                                |
| enabled: any/c = #t                                                        |
| vert-margin: spacing-integer? = 2                                          |
| horiz-margin: spacing-integer? = 2                                         |
| min-width: (or/c dimension-integer? #f) = #f                               |
| min-height: (or/c dimension-integer? #f) = #f                              |
| stretchable-width: any/c = #f                                              |
| stretchable-height: any/c = #f                                             |
|                                                                             |
| ```racket                                                                   |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                    |
|       (is-a?/c panel%) (is-a?/c pane%))                                     |
| ```                                                                         |
|                                                                             |
| ```racket                                                                   |
| ((is-a?/c check-box%) (is-a?/c control-event%)                              |
|. ->. any)                                                                |
| ```                                                                         |
+-----------------------------------------------------------------------------+
```

Creates a check box with a string or bitmap label. If label is a bitmap, and if the
bitmap has a mask (see get-loaded-mask in bitmap%)
that is the same size as the bitmap, then the mask is used for the
label. Modifying a bitmap while it is used as a label has
an unspecified effect on the displayed label.

If & occurs in label (when label is a string), it
is specially parsed as for button%.

The callback procedure is called (with the event type
'check-box) whenever the user clicks the check box.

If style includes 'deleted, then the check box is created as hidden,
and it does not affect its parent’s geometry; the check box can be made active later by calling
parent’s add-child method.

If value is true, it is passed to
set-value so that the box is initially checked.

The font argument determines the font for the control. For information about the enabled argument, see window<%>. For information about the horiz-margin and vert-margin
arguments, see subarea<%>. For information about the
min-width, min-height, stretchable-width, and
stretchable-height arguments, see area<%>.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-check-box get-value) → boolean? |
+-----------------------------------------+
```

Gets the state of the check box: #t if it is checked, #f
otherwise.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-check-box set-label label) → void?     |
| label: (or/c label-string? (is-a?/c bitmap%)) |
+------------------------------------------------+
```

Overrides set-label in window<%>.

The same as set-label in window<%> when label is a
string.

Otherwise, sets the bitmap label for a bitmap check box.
Since label is a bitmap, if the
bitmap has a mask (see get-loaded-mask in bitmap%)
that is the same size as the bitmap, then the mask is used for the
label. Modifying a bitmap while it is used as a label has
an unspecified effect on the displayed label. The bitmap label is installed only
if the control was originally created with a bitmap label.

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send a-check-box set-value state) → void? |
| state: any/c                              |
+--------------------------------------------+
```

Sets the check box’s state. (The control’s callback procedure is
not invoked.)

The check box’s state can be changed
by the user clicking the control, and such changes do not go through this method; use the control callback procedure (provided as an initialization argument) to
monitor state changes.

If state is #f, the box is
unchecked, otherwise it is checked.
