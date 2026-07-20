<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/slider_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/slider_.html -->
<!-- Canonical English source for Japanese translation -->

> [image: slider.png]

```
+-----------------------+------------+
| classslider%: class? |            |
+-----------------------+------------+
| superclass: object%   |            |
| extends:              | control<%> |
+-----------------------+------------+
```

A slider object is a panel item with a handle that the user can
drag to change the control’s value. Each slider has a fixed minimum
and maximum value.

Whenever the user changes the value of a slider, its callback
procedure is invoked. A callback procedure is provided as an
initialization argument when each slider is created.

```
+------------------------------------------------------------------------------+
| [constructor]                                                                |
|                                                                              |
| (new slider%                                                                 |
| → (is-a?/c slider%)                                                          |
| label: (or/c label-string? #f)                                              |
| min-value: position-integer?                                                |
| max-value: position-integer?                                                |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c  |
| pane%))                                                                      |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                     |
| (is-a?/c panel%) (is-a?/c pane%))                                            |
| callback: ((is-a?/c slider%) (is-a?/c control-event%). ->. any) = (lambda |
| (b e) (void))                                                                |
| init-value: position-integer? = min-value                                   |
| style: (listof (or/c 'horizontal 'vertical 'upward 'plain 'vertical-label   |
| 'horizontal-label 'deleted)) = '(horizontal)                                 |
| (listof (or/c 'horizontal 'vertical 'upward 'plain                           |
| 'vertical-label 'horizontal-label                                            |
| 'deleted))                                                                   |
| font: (is-a?/c font%) = normal-control-font                                 |
| enabled: any/c = #t                                                         |
| vert-margin: spacing-integer? = 2                                           |
| horiz-margin: spacing-integer? = 2                                          |
| min-width: (or/c dimension-integer? #f) = #f                                |
| min-height: (or/c dimension-integer? #f) = #f                               |
| stretchable-width: any/c = (memq 'horizontal style)                         |
| stretchable-height: any/c = (memq 'vertical style)                          |
|                                                                              |
| ```racket                                                                    |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                     |
|       (is-a?/c panel%) (is-a?/c pane%))                                      |
| ```                                                                          |
|                                                                              |
| ```racket                                                                    |
| (listof (or/c 'horizontal 'vertical 'upward 'plain                           |
|               'vertical-label 'horizontal-label                              |
|               'deleted))                                                     |
| ```                                                                          |
+------------------------------------------------------------------------------+
```

If label is a string, it is used as the label for the slider.
Otherwise, the slider does not display its label.

If & occurs in label, it
is specially parsed as for button%.

The min-value and max-value arguments specify the
range of the slider, inclusive. The init-value argument
optionally specifies the slider’s initial value. The sequence
[min-value, init-value, max-value]
must be non-decreasing. Otherwise, an exn:fail:contract exception is raised.

The callback procedure is called (with the event type
'slider) when the user changes the slider’s value.

The style argument must include either 'horizontal for a horizontal
slider going left-to-right, 'upward for
a vertical slider going up, or 'vertical for
a vertical slider going down (but beware that 'vertical might render
with misleading colors on Mac OS, where the system toolkit supports only upward sliders).
If style includes 'plain, the slider does
not display numbers for its range and current value to the user.
If style includes 'vertical-label, then the slider is
created with a label above the control; if style does not include
'vertical-label (and optionally includes 'horizontal-label), then the
label is created to the left of the slider. If style includes 'deleted, then the slider is created as hidden,
and it does not affect its parent’s geometry; the slider can be made active later by calling
parent’s add-child method.

The font argument determines the font for the control. For information about the enabled argument, see window<%>. For information about the horiz-margin and vert-margin
arguments, see subarea<%>. For information about the
min-width, min-height, stretchable-width, and
stretchable-height arguments, see area<%>.

Changed in version 1.73 of package `gui-lib`: Added 'upward as a possible style element.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-slider get-value) → position-integer? |
+-----------------------------------------------+
```

Gets the current slider value.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-slider set-value value) → void? |
| value: position-integer?               |
+-----------------------------------------+
```

Sets the value (and displayed position) of the slider. (The control’s
callback procedure is not invoked.) If value is
outside the slider’s minimum and maximum range, an exn:fail:contract exception is raised.

A slider’s value can be changed
by the user clicking the control, and such changes do not go through this method; use the control callback procedure (provided as an initialization argument) to
monitor value changes.
