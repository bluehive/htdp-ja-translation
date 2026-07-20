<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/labelled-menu-item___.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/labelled-menu-item___.html -->
<!-- Canonical English source for Japanese translation -->

```
+---------------------------------------------+--------------+
| interfacelabelled-menu-item<%>: interface? |              |
+---------------------------------------------+--------------+
| implements:                                 | menu-item<%> |
+---------------------------------------------+--------------+
```

A labelled-menu-item<%> object is a menu-item<%> with
a string label (i.e., any menu item other than a separator). More
specifically, it is an instance of either menu-item% (a
plain menu item), checkable-menu-item% (a checkable menu
item), or menu% (a submenu).

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-labelled-menu-item enable enabled?) → void? |
| enabled?: any/c                                    |
+-----------------------------------------------------+
```

Enables or disables the menu item. If the item is a submenu (or menu
in a menu bar), the entire menu is disabled, but each submenu item’s
is-enabled? method returns #f
only if the item is specifically disabled (in addition to the
submenu).

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-labelled-menu-item get-help-string) |
| → (or/c label-string? #f)                   |
+---------------------------------------------+
```

Returns the help string for the menu item, or #f if the item
has no help string.

When an item has a help, the string may be used to
display help information to the user.

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-labelled-menu-item get-label) → label-string? |
+-------------------------------------------------------+
```

Returns the item’s label.

See also set-label and
get-plain-label.

```
+-------------------------------------------------------------+
| [method]                                                    |
|                                                             |
| (send a-labelled-menu-item get-plain-label) → label-string? |
+-------------------------------------------------------------+
```

Like get-label, except that
&s and tab characters in the label are stripped in
the same way as for set-label.

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-labelled-menu-item is-enabled?) → boolean? |
+----------------------------------------------------+
```

Returns #t if the menu item is enabled, #f
otherwise.

See also
enable.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-labelled-menu-item on-demand) → void? |
+-----------------------------------------------+
```

Specification:
Normally called when the user clicks on the menu bar containing the
item (before the user sees any menu items), just before the popup
menu containing the item is popped up, or just before inspecting the
menu bar containing the item for a shortcut key binding.
See on-demand in menu-item-container<%> for further details.

A on-demand in menu-item-container<%> method can be overridden
in such a way that the container does not call the
on-demand method of its items.

Default implementation:
Calls the demand-callback procedure that was provided when the
object was created.

```
+----------------------------------------------------------+
| [method]                                                 |
|                                                          |
| (send a-labelled-menu-item set-help-string help) → void? |
| help: (or/c label-string? #f)                           |
+----------------------------------------------------------+
```

Sets the help string for the menu item. Use #f to remove the
help string for an item.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-labelled-menu-item set-label label) → void? |
| label: label-string?                               |
+-----------------------------------------------------+
```

Sets the menu item’s label. If the item has a shortcut, the shortcut
is not affected.

If the label contains & and the window is a control, the
label is parsed specially; on Windows and Unix, the character
following a & is underlined in the displayed menu to
indicate a keyboard mnemonic. Pressing the Alt key with an underlined
character from a menu’s name in the menu bar causes the menu to be
selected (via on-menu-char). When a menu has the
focus, the mnemonic characters are used for navigation without Alt. A
&& in the label is replaced by a literal (non-navigation)
&. On Mac OS, &s in the label are parsed in
the same way as for Unix and Windows, but no mnemonic underline is
displayed. On Mac OS, a parenthesized mnemonic character is
removed (along with any surrounding space) before the label is
displayed, since a parenthesized mnemonic is often used for non-Roman
languages. Finally, for historical reasons, if a label contains a tab character, then the
tab and all remaining characters are hidden in the displayed menu.
All of these rules are consistent with label handling in button%
and other windows.

A & is always preserved in the label returned by
get-label, but never preserved in the
label returned by get-plain-label.
