<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/combo-field_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/combo-field_.html -->
<!-- Canonical English source for Japanese translation -->

> [image: combo-field.png]

```
+----------------------------+
| classcombo-field%: class? |
+----------------------------+
| superclass: text-field%    |
+----------------------------+
```

A combo-field% object is a text-field%
object that also resembles a choice% object, because it
has a small popup button to the right of the text field. Clicking
the button pops up a menu, and selecting a menu item typically copies
the item into the text field.

```
+-----------------------------------------------------------------------------+
| [constructor]                                                               |
|                                                                             |
| (new combo-field%                                                           |
| → (is-a?/c combo-field%)                                                    |
| label: (or/c label-string? #f)                                             |
| choices: (listof label-string?)                                            |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c |
| pane%))                                                                     |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                    |
| (is-a?/c panel%) (is-a?/c pane%))                                           |
| callback: ((is-a?/c combo-field%) (is-a?/c control-event%). ->. any) =   |
| (lambda (c e) (void))                                                       |
| ((is-a?/c combo-field%) (is-a?/c control-event%)                            |
|. ->. any)                                                                 |
| init-value: string = ""                                                    |
| style: (listof (or/c 'horizontal-label 'vertical-label 'deleted)) = null   |
| (listof (or/c 'horizontal-label 'vertical-label                             |
| 'deleted))                                                                  |
| font: (is-a?/c font%) = normal-control-font                                |
| enabled: any/c = #t                                                        |
| vert-margin: spacing-integer? = 2                                          |
| horiz-margin: spacing-integer? = 2                                         |
| min-width: (or/c dimension-integer? #f) = #f                               |
| min-height: (or/c dimension-integer? #f) = #f                              |
| stretchable-width: any/c = #t                                              |
| stretchable-height: any/c = #f                                             |
|                                                                             |
| ```racket                                                                   |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                    |
|       (is-a?/c panel%) (is-a?/c pane%))                                     |
| ```                                                                         |
|                                                                             |
| ```racket                                                                   |
| ((is-a?/c combo-field%) (is-a?/c control-event%)                            |
|. ->. any)                                                                |
| ```                                                                         |
|                                                                             |
| ```racket                                                                   |
| (listof (or/c 'horizontal-label 'vertical-label                             |
|               'deleted))                                                    |
| ```                                                                         |
+-----------------------------------------------------------------------------+
```

If label is not #f, it is used as the combo label.
Otherwise, the combo does not display its label.

If & occurs in label, it
is specially parsed as for button%.

The choices list specifies the initial list of items for the
combo’s popup menu. The
append method adds a new item to the menu with a callback to install the
appended item into the combo’s text field. The
get-menu method returns a menu that can be changed to
adjust the content and actions of the combo’s menu.

The callback procedure is called when the user changes the text
in the combo or presses the Enter key (and Enter is not handled by
the combo’s frame or dialog; see
on-traverse-char in top-level-window<%> ). If the user presses Enter, the type of event passed to the callback
is 'text-field-enter, otherwise it is
'text-field.

If init-value is not "", the minimum width of the text item
is made wide enough to show init-value. Otherwise, a built-in
default width is selected.

If style includes 'vertical-label, then the combo is
created with a label above the control; if style does not include
'vertical-label (and optionally includes 'horizontal-label), then the
label is created to the left of the combo. If style includes 'deleted, then the combo is created as hidden,
and it does not affect its parent’s geometry; the combo can be made active later by calling
parent’s add-child method..

The font argument determines the font for the control. For information about the enabled argument, see window<%>. For information about the horiz-margin and vert-margin
arguments, see subarea<%>. For information about the
min-width, min-height, stretchable-width, and
stretchable-height arguments, see area<%>.

```
+---------------------------------------+
| [method]                              |
|                                       |
| (send a-combo-field append l) → void? |
| l: label-string?                     |
+---------------------------------------+
```

Adds a new item to the combo’s popup menu. The given label is used for
the item’s name, and the item’s callback installs the label into the
combo’s text field.

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-combo-field get-menu) → (is-a?/c popup-menu%) |
+-------------------------------------------------------+
```

Returns a popup-menu% that is effectively copied into the
combo’s popup menu when the combo is clicked. Only the labels and
callbacks of the menu’s items are used; the enable state, submenus,
or separators are ignored.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-combo-field on-popup event) → void? |
| event: (is-a?/c control-event%)            |
+---------------------------------------------+
```

Specification:
Called when the user clicks the combo’s popup button. Override this method
to adjust the content of the combo menu on demand.

Default implementation:
Does nothing.
