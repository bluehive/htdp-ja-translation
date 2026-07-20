<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/text-field_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/text-field_.html -->
<!-- Canonical English source for Japanese translation -->

> [image: text-field.png]

```
+---------------------------+------------+
| classtext-field%: class? |            |
+---------------------------+------------+
| superclass: object%       |            |
| extends:                  | control<%> |
+---------------------------+------------+
```

A text-field% object is an editable text field with an
optional label displayed in front of it. There are two text field
styles:

- A single line of text is visible, and a special control event
is generated when the user presses Return or Enter (when the text field has the
focus) and the event is not handled by the text field’s frame or
dialog (see on-traverse-char in top-level-window<%> ).
- Multiple lines of text are visible, and Enter is not handled
specially.

Whenever the user changes the content of a text field, its callback
procedure is invoked. A callback procedure is provided as an
initialization argument when each text field is created.

The text field is implemented using a text% editor (with an
inaccessible display). Thus, whereas text-field% provides
only get-value and set-value to manipulate the text in a text field, the
get-editor returns the field’s editor, which
provides a vast collection of methods for more sophisticated
operations on the text.

The keymap for the text field’s editor is initialized by calling the
current keymap initializer procedure, which is determined by the
current-text-keymap-initializer parameter.

```
+-----------------------------------------------------------------------------+
| [constructor]                                                               |
|                                                                             |
| (new text-field%                                                            |
| → (is-a?/c text-field%)                                                     |
| label: (or/c label-string? #f)                                             |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c |
| pane%))                                                                     |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                    |
| (is-a?/c panel%) (is-a?/c pane%))                                           |
| callback: ((is-a?/c text-field%) (is-a?/c control-event%). ->. any) =    |
| (lambda (t e) (void))                                                       |
| ((is-a?/c text-field%) (is-a?/c control-event%)                             |
|. ->. any)                                                                 |
| init-value: string? = ""                                                   |
| style: (listof (or/c 'single 'multiple 'hscroll 'password 'vertical-label  |
| 'horizontal-label 'deleted)) = '(single)                                    |
| (listof (or/c 'single 'multiple 'hscroll 'password                          |
| 'vertical-label 'horizontal-label                                           |
| 'deleted))                                                                  |
| font: (is-a?/c font%) = normal-control-font                                |
| enabled: any/c = #t                                                        |
| vert-margin: spacing-integer? = 2                                          |
| horiz-margin: spacing-integer? = 2                                         |
| min-width: (or/c dimension-integer? #f) = #f                               |
| min-height: (or/c dimension-integer? #f) = #f                              |
| stretchable-width: any/c = #t                                              |
| stretchable-height: any/c = (memq 'multiple style)                         |
|                                                                             |
| ```racket                                                                   |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                    |
|       (is-a?/c panel%) (is-a?/c pane%))                                     |
| ```                                                                         |
|                                                                             |
| ```racket                                                                   |
| ((is-a?/c text-field%) (is-a?/c control-event%)                             |
|. ->. any)                                                                |
| ```                                                                         |
|                                                                             |
| ```racket                                                                   |
| (listof (or/c 'single 'multiple 'hscroll 'password                          |
|               'vertical-label 'horizontal-label                             |
|               'deleted))                                                    |
| ```                                                                         |
+-----------------------------------------------------------------------------+
```

If label is not #f, it is used as the text field
label. Otherwise, the text field does not display its label.

If & occurs in label, it
is specially parsed as for button%.

The callback procedure is called when the user changes the
text in the text field or presses the Enter key (and Enter is not
handled by the text field’s frame or dialog; see
on-traverse-char in top-level-window<%>). If the user presses
Enter, the type of event passed to the callback is
'text-field-enter, otherwise it is
'text-field.

If init-value is not "", the graphical minimum size for the
text item is made wide enough to show init-value. Otherwise,
a built-in default width is selected. For a text field in single-line
mode, the graphical minimum size is set to show one line, and only the
control’s width is stretchable by default. For a multiple-line text field, the
graphical minimum size shows three lines of text, and it is stretchable in both
directions by default.

The style must contain exactly one of 'single or
'multiple; the former specifies a single-line field and the
latter specifies a multiple-line field. The 'hscroll style
applies only to multiple-line fields; when 'hscroll is
specified, the field has a horizontal scrollbar and autowrapping is
disabled; otherwise, the field has no horizontal scrollbar and
autowrapping is enabled. A multiple-line text field always has a
vertical scrollbar. The 'password style indicates that the
field should draw each character of its content using a generic
symbol instead of the actual character. If style includes 'vertical-label, then the text field is
created with a label above the control; if style does not include
'vertical-label (and optionally includes 'horizontal-label), then the
label is created to the left of the text field.
If style includes 'deleted, then the text field is created as hidden,
and it does not affect its parent’s geometry; the text field can be made active later by calling
parent’s add-child method..

The font argument determines the font for the control. For information about the enabled argument, see window<%>. For information about the horiz-margin and vert-margin
arguments, see subarea<%>. For information about the
min-width, min-height, stretchable-width, and
stretchable-height arguments, see area<%>.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-text-field get-editor) → (is-a?/c text%) |
+--------------------------------------------------+
```

Returns the editor used to implement the text field.

For a text field, the most useful methods of a text% object
are the following:

- (senda-textget-text) returns
the current text of the editor.
- (senda-texterase) deletes all text from
the editor.
- (senda-textinsertstr) inserts
str into the editor at the current caret position.

```
+-------------------------------------------------------------+
| [method]                                                    |
|                                                             |
| (send a-text-field get-field-background) → (is-a?/c color%) |
+-------------------------------------------------------------+
```

Gets the background color of the field’s editable area.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-text-field get-value) → string? |
+-----------------------------------------+
```

Returns the text currently in the text field.

```
+--------------------------------------------------------+
| [method]                                               |
|                                                        |
| (send a-text-field set-field-background color) → void? |
| color: (or/c (is-a?/c color%) #f)                     |
+--------------------------------------------------------+
```

Sets the background color of the field’s editable area to color
If color is #f sets the background color
to black in dark mode or white if not in dark mode.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-text-field set-value val) → void? |
| val: string?                             |
+-------------------------------------------+
```

Sets the text currently in the text field. (The control’s callback
procedure is not invoked.)

A text field’s value can be changed
by the user typing into the control, and such changes do not go through this method; use the control callback procedure (provided as an initialization argument) to
monitor value changes.
