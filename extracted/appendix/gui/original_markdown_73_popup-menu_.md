<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/popup-menu_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/popup-menu_.html -->
<!-- Canonical English source for Japanese translation -->

```
+---------------------------+------------------------+
| classpopup-menu%: class? |                        |
+---------------------------+------------------------+
| superclass: object%       |                        |
| extends:                  | menu-item-container<%> |
+---------------------------+------------------------+
```

A popup-menu% object is created without a parent. Dynamically
display a popup-menu% with popup-menu in window<%>
or popup-menu in editor-admin%.

A popup menu is not a control. A choice% control,
however, displays a single value that the user selects from a popup
menu. A choice% control’s popup menu is built into the
control, and it is not accessible to the programmer.

```
+--------------------------------------------------------------------------------+
| [constructor]                                                                  |
|                                                                                |
| (new popup-menu%                                                               |
| → (is-a?/c popup-menu%)                                                        |
| title: (or/c label-string? #f) = #f                                           |
| popdown-callback: ((is-a?/c popup-menu%) (is-a?/c control-event%). ->. any) |
| = (lambda (p e) (void))                                                        |
| ((is-a?/c popup-menu%) (is-a?/c control-event%)                                |
|. ->. any)                                                                    |
| demand-callback: ((is-a?/c popup-menu%). ->. any) = (lambda (p) (void))     |
| font: (is-a?/c font%) = normal-control-font                                   |
|                                                                                |
| ```racket                                                                      |
| ((is-a?/c popup-menu%) (is-a?/c control-event%)                                |
|. ->. any)                                                                   |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

If title is not #f, it is used as a displayed title
at the top of the popup menu.

If title contains &, it is handled specially, the
same as for menu% titles. A popup menu mnemonic is not
useful, but it is supported for consistency with other menu labels.

The popdown-callback procedure is invoked when a popup menu is
dismissed. If the popup menu is dismissed without an item being
selected, popdown-callback is given a control-event%
object with the event type 'menu-popdown-none. If the
popup menu is dismissed via an item selection, the item’s callback is
invoked first, and then popdown-callback is given a
control-event% object with the event type
'menu-popdown.

The demand-callback procedure is called by the default
on-demand method with the object itself.

The font argument determines the font for the popup menu’s
items.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-popup-menu get-font) → (is-a?/c font%) |
+------------------------------------------------+
```

Returns the font used for the popup menu’s items, which is optionally
supplied when a popup menu is created.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-popup-menu get-popup-target)                |
| → (or/c (is-a?/c window<%>) (is-a?/c editor<%>) #f) |
+-----------------------------------------------------+
```

Returns the context in which the popup menu is currently displayed, or
#f if it is not popped up in any window.

The context is set before the on-demand method is called, and it is not removed until after the
popup-menu’s callback is invoked. (Consequently, it is also set while
an item callback is invoked, if the user selected an item.)

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-popup-menu set-min-width width) → void? |
| width: dimension-integer?                      |
+-------------------------------------------------+
```

Sets the popup menu’s minimum width in pixels.
