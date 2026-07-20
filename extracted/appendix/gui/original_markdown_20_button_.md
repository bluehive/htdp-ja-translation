<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/button_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/button_.html -->
<!-- Canonical English source for Japanese translation -->

> [image: button.png]

```
+-----------------------+------------+
| classbutton%: class? |            |
+-----------------------+------------+
| superclass: object%   |            |
| extends:              | control<%> |
+-----------------------+------------+
```

Whenever a button is clicked by the user, the button’s callback
procedure is invoked. A callback procedure is provided as an
initialization argument when each button is created.

```
+------------------------------------------------------------------------------+
| [constructor]                                                                |
|                                                                              |
| (new button%                                                                 |
| → (is-a?/c button%)                                                          |
| label: (or/c label-string? (is-a?/c bitmap%) (list/c (is-a?/c bitmap%)      |
| label-string? (or/c 'left 'top 'right 'bottom)))                             |
| (or/c label-string?                                                          |
| (is-a?/c bitmap%)                                                            |
| (list/c (is-a?/c bitmap%)                                                    |
| label-string?                                                                |
| (or/c 'left 'top 'right 'bottom)))                                           |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c  |
| pane%))                                                                      |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                     |
| (is-a?/c panel%) (is-a?/c pane%))                                            |
| callback: ((is-a?/c button%) (is-a?/c control-event%). ->. any) = (lambda |
| (b e) (void))                                                                |
| style: (listof (or/c 'border 'multi-line 'deleted)) = null                  |
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
| (or/c label-string?                                                          |
|       (is-a?/c bitmap%)                                                      |
|       (list/c (is-a?/c bitmap%)                                              |
|               label-string?                                                  |
|               (or/c 'left 'top 'right 'bottom)))                             |
| ```                                                                          |
|                                                                              |
| ```racket                                                                    |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                     |
|       (is-a?/c panel%) (is-a?/c pane%))                                      |
| ```                                                                          |
+------------------------------------------------------------------------------+
```

Creates a button with a string label, bitmap label, or both.
If label is a bitmap, and if the
bitmap has a mask (see get-loaded-mask in bitmap%)
that is the same size as the bitmap, then the mask is used for the
label. Modifying a bitmap while it is used as a label has
an unspecified effect on the displayed label. If label is a list, then
the button has both a bitmap and string label, and the
symbol 'left, 'top, 'right, or 'bottom
specifies the location of the image relative to the text on the button.

If & occurs in label (when label includes a
string), it is specially parsed; on Windows and Unix, the character
following & is underlined in the displayed control to
indicate a keyboard mnemonic. (On Mac OS, mnemonic underlines are
not shown.) The underlined mnemonic character must be a letter or a
digit. The user can effectively click the button by typing the
mnemonic when the control’s top-level-window contains the keyboard
focus. The user must also hold down the Meta or Alt key if the
keyboard focus is currently in a control that handles normal
alphanumeric input. The & itself is removed from
label before it is displayed for the control; a &&
in label is converted to & (with no mnemonic
underlining). On Mac OS, a parenthesized mnemonic character is
removed (along with any surrounding space) before the label is
displayed, since a parenthesized mnemonic is often used for non-Roman
languages. Finally, for historical reasons, any text after a tab character is removed on all
platforms. All of these rules are consistent with label handling in
menu items (see set-label). Mnemonic keyboard events are handled by
on-traverse-char (but not on Mac OS).

The callback procedure is called (with the event type
'button) whenever the user clicks the button.

If style includes 'border, the button is drawn with
a special border that indicates to the user that it is the default
action button (see on-traverse-char). If style includes 'multi-line,
the button is drawn in a way that can stretch vertically and accommodate
multiple lines in a text label; currently, this style makes a difference only
on Mac OS, and it is selected automatically when label is a string
that contains #\newline or #\return.
If style includes 'deleted, then the button is created as hidden,
and it does not affect its parent’s geometry; the button can be made active later by calling
parent’s add-child method.

The font argument determines the font for the control. For information about the enabled argument, see window<%>. For information about the horiz-margin and vert-margin
arguments, see subarea<%>. For information about the
min-width, min-height, stretchable-width, and
stretchable-height arguments, see area<%>.

Changed in version 1.47 of package `gui-lib`: Added the 'multi-line style, and made it
selected when label contains #\return.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-button set-label label) → void?        |
| label: (or/c label-string? (is-a?/c bitmap%)) |
| (or/c label-string?                            |
| (is-a?/c bitmap%))                             |
|                                                |
| ```racket                                      |
| (or/c label-string?                            |
|       (is-a?/c bitmap%))                       |
| ```                                            |
+------------------------------------------------+
```

Overrides set-label in window<%>.

The same as set-label in window<%> when label is a
string.

Otherwise, sets the bitmap label for a bitmap button. Since label is a bitmap, if the
bitmap has a mask (see get-loaded-mask in bitmap%)
that is the same size as the bitmap, then the mask is used for the
label. Modifying a bitmap while it is used as a label has
an unspecified effect on the displayed label.
The bitmap label is installed only
if the control was originally created with a bitmap label.

If the button has both a string and a bitmap label, then either can be
set using set-label.
