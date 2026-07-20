<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/message_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/message_.html -->
<!-- Canonical English source for Japanese translation -->

> [image: message.png]

```
+------------------------+------------+
| classmessage%: class? |            |
+------------------------+------------+
| superclass: object%    |            |
| extends:               | control<%> |
+------------------------+------------+
```

A message control is a static line of text or a static bitmap. The
text or bitmap corresponds to the message’s label (see
set-label).

```
+-----------------------------------------------------------------------------+
| [constructor]                                                               |
|                                                                             |
| (new message%                                                               |
| → (is-a?/c message%)                                                        |
| label: (or/c label-string? (is-a?/c bitmap%) (or/c 'app 'caution 'stop))   |
| (or/c label-string? (is-a?/c bitmap%)                                       |
| (or/c 'app 'caution 'stop))                                                 |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c |
| pane%))                                                                     |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                    |
| (is-a?/c panel%) (is-a?/c pane%))                                           |
| style: (listof (or/c 'deleted)) = null                                     |
| font: (is-a?/c font%) = normal-control-font                                |
| color: (or/c #f string? (is-a?/c color%)) = #f                             |
| enabled: any/c = #t                                                        |
| vert-margin: spacing-integer? = 2                                          |
| horiz-margin: spacing-integer? = 2                                         |
| min-width: (or/c dimension-integer? #f) = #f                               |
| min-height: (or/c dimension-integer? #f) = #f                              |
| stretchable-width: any/c = #f                                              |
| stretchable-height: any/c = #f                                             |
| auto-resize: any/c = #f                                                    |
|                                                                             |
| ```racket                                                                   |
| (or/c label-string? (is-a?/c bitmap%)                                       |
|       (or/c 'app 'caution 'stop))                                           |
| ```                                                                         |
|                                                                             |
| ```racket                                                                   |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                    |
|       (is-a?/c panel%) (is-a?/c pane%))                                     |
| ```                                                                         |
+-----------------------------------------------------------------------------+
```

Creates a string or bitmap message initially showing label.
If label is a bitmap, and if the
bitmap has a mask (see get-loaded-mask in bitmap%)
that is the same size as the bitmap, then the mask is used for the
label. Modifying a bitmap while it is used as a label has
an unspecified effect on the displayed label. An 'app,
'caution, or 'stop symbol for
label indicates an icon; 'app is the application
icon (Windows and Mac OS) or a generic “info” icon (X),
'caution is a caution-sign icon, and 'stop is a
stop-sign icon.

If & occurs in label, it is specially parsed;
under Windows and X, the character
following & is underlined in the displayed control to
indicate a keyboard mnemonic. (Under Mac OS, mnemonic underlines are
not shown.) The mnemonic is meaningless for a message (as far as
on-traverse-char in top-level-window<%> is concerned),
but it is supported for consistency with other control types. A
programmer may assign a meaning to the mnemonic (e.g., by overriding
on-traverse-char).

If style includes 'deleted, then the message is created as hidden,
and it does not affect its parent’s geometry; the message can be made active later by calling
parent’s add-child method.

The font argument determines the font for the control. For information about the enabled argument, see window<%>. For information about the horiz-margin and vert-margin
arguments, see subarea<%>. For information about the
min-width, min-height, stretchable-width, and
stretchable-height arguments, see area<%>.

The color argument determines the color of the text label. It
has no effect on symbol and bitmap labels. If it is #f, the
system default text color is used. If it is a string, then the color
is looked up in the-color-database.

If auto-resize is not #f, then automatic resizing is
initially enabled (see auto-resize), and the
message% object’s graphical minimum size is as small as
possible.

Changed in version 1.58 of package `gui-lib`: Added the color argument.

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send a-message auto-resize) → boolean?  |
| (send a-message auto-resize on?) → void? |
| on?: any/c                              |
+------------------------------------------+
```

Reports or sets whether the message%’s min-width and
min-height are automatically set when the label is changed
via set-label.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-message set-label label) → void?       |
| label: (or/c label-string? (is-a?/c bitmap%)) |
+------------------------------------------------+
```

Overrides set-label in window<%>.

The same as set-label in window<%> when label is a
string.

Otherwise, sets the bitmap label for a bitmap message.
Since label is a bitmap, if the
bitmap has a mask (see get-loaded-mask in bitmap%)
that is the same size as the bitmap, then the mask is used for the
label. Modifying a bitmap while it is used as a label has
an unspecified effect on the displayed label. The bitmap label is installed only
if the control was originally created with a bitmap label.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-message set-color color) → void?      |
| color: (or/c #f (is-a?/c color%))            |
| (send a-message set-color color-name) → void? |
| color-name: string?                          |
+-----------------------------------------------+
```

Sets the label’s text color. When color is #f, sets
the label’s text color to the platform default. This method has no
effect if the label is a symbol or a bitmap.

Added in version 1.58 of package `gui-lib`.
Changed in version 1.71: Added support for setting the color to the system default.

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send a-message get-color) → (or/c #f (is-a?/c color%)) |
+---------------------------------------------------------+
```

Returns the current user-specified label color or #f if the
system default is used.

Added in version 1.58 of package `gui-lib`.
