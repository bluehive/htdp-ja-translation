<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/selectable-menu-item___.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/selectable-menu-item___.html -->
<!-- Canonical English source for Japanese translation -->

```
+-----------------------------------------------+-----------------------+
| interfaceselectable-menu-item<%>: interface? |                       |
+-----------------------------------------------+-----------------------+
| implements:                                   | labelled-menu-item<%> |
+-----------------------------------------------+-----------------------+
```

A selectable-menu-item<%> object is a
labelled-menu-item<%> that the user can select. It may also
have a keyboard shortcut; the shortcut is displayed in the menu, and
the default on-subwindow-char method in the menu’s
frame dispatches to the menu item when the shortcut key combination
is pressed.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-selectable-menu-item command event) → void? |
| event: (is-a?/c control-event%)                    |
+-----------------------------------------------------+
```

Invokes the menu item’s callback procedure, which is supplied when an
instance of
menu-item% or
checkable-menu-item% is created.

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send a-selectable-menu-item get-shortcut) |
| → (or/c char? symbol? #f)                  |
+--------------------------------------------+
```

Gets the keyboard shortcut character or virtual key for the menu
item. This character or key is combined with the shortcut prefix,
which is reported by get-shortcut-prefix.

If the menu item has no shortcut, #f is returned.

The shortcut part of a menu item name is not included in the label
returned by get-label.

For a list of allowed key symbols, see get-key-code in key-event%, except that the following are disallowed:
'shift, 'control, 'numlock,
'scroll, 'wheel-up, 'wheel-down,
'release, and 'press.

```
+--------------------------------------------------------------------------------+
| [method]                                                                       |
|                                                                                |
| (send a-selectable-menu-item get-shortcut-prefix)                              |
| → (and/c (listof (or/c 'alt 'cmd 'meta 'ctl 'shift 'option)) (λ (x) (implies   |
| (equal? 'unix (system-type)) (not (and (member 'alt x) (member 'meta x))))) (λ |
| (x) (equal? x (remove-duplicates x))))                                         |
| (and/c (listof (or/c 'alt 'cmd 'meta 'ctl                                      |
| 'shift 'option))                                                               |
| (λ (x) (implies (equal? 'unix (system-type))                                   |
| (not (and (member 'alt x)                                                      |
| (member 'meta x)))))                                                           |
| (λ (x) (equal? x (remove-duplicates x))))                                      |
|                                                                                |
| ```racket                                                                      |
| (and/c (listof (or/c 'alt 'cmd 'meta 'ctl                                      |
|                      'shift 'option))                                          |
|        (λ (x) (implies (equal? 'unix (system-type))                            |
|                        (not (and (member 'alt x)                               |
|                                  (member 'meta x)))))                          |
|        (λ (x) (equal? x (remove-duplicates x))))                               |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

Returns a list of symbols that indicates the keyboard prefix used for the menu
item’s keyboard shortcut. The allowed symbols for the list are the following:

- 'alt — Meta (Windows and X only)
- 'cmd — Command (Mac OS only)
- 'meta — Meta (Unix only)
- 'ctl — Control
- 'shift — Shift
- 'option — Option (Mac OS only)

On Unix, at most one of 'alt and 'meta can be
supplied; the only difference between 'alt and
'meta is the key combination’s display in a menu.

The default shortcut prefix is available from
get-default-shortcut-prefix.

The shortcut key, as determined by get-shortcut, matches a key event using either the normally reported
key code or the other-Shift/AltGr key code (as produced by
get-other-shift-key-code in key-event%, etc.). When the
shortcut key is a key-code symbol or an ASCII letter or digit, then
the shortcut matches only the exact combination of modifier keys
listed in the prefix. For character shortcuts other than ASCII
letters and digits, however, then the shortcut prefix merely
determines a minimum set of modifier keys, because additional
modifiers may be needed to access the character; an exception is
that, on Windows or Unix, the Alt/Meta key press must match the
prefix exactly (i.e., included or not). In all cases, the most
precise match takes precedence; see map-function in keymap%
for more information on match ranking.

An empty list can be used for a shortcut prefix. However, the default
on-menu-char in frame% method checks for menu shortcuts only
when the key event includes either a non-Shift modifier or a Function
key. Thus, an empty shortcut prefix is normally useful only if the
shortcut key is a Function key.

```
+-------------------------------------------------------------+
| [method]                                                    |
|                                                             |
| (send a-selectable-menu-item set-shortcut shortcut) → void? |
| shortcut: (or/c char? symbol? #f)                          |
+-------------------------------------------------------------+
```

Sets the keyboard shortcut character for the menu item. See
get-shortcut for more information.

If the shortcut character is set to #f, then menu item has no
keyboard shortcut.

```
+-------------------------------------------------------------------------------+
| [method]                                                                      |
|                                                                               |
| (send a-selectable-menu-item set-shortcut-prefix prefix)                      |
| → void?                                                                       |
| prefix: (and/c (listof (or/c 'alt 'cmd 'meta 'ctl 'shift 'option)) (λ (x)    |
| (implies (equal? 'unix (system-type)) (not (and (member 'alt x) (member 'meta |
| x))))) (λ (x) (equal? x (remove-duplicates x))))                              |
| (and/c (listof (or/c 'alt 'cmd 'meta 'ctl                                     |
| 'shift 'option))                                                              |
| (λ (x) (implies (equal? 'unix (system-type))                                  |
| (not (and (member 'alt x)                                                     |
| (member 'meta x)))))                                                          |
| (λ (x) (equal? x (remove-duplicates x))))                                     |
|                                                                               |
| ```racket                                                                     |
| (and/c (listof (or/c 'alt 'cmd 'meta 'ctl                                     |
|                      'shift 'option))                                         |
|        (λ (x) (implies (equal? 'unix (system-type))                           |
|                        (not (and (member 'alt x)                              |
|                                  (member 'meta x)))))                         |
|        (λ (x) (equal? x (remove-duplicates x))))                              |
| ```                                                                           |
+-------------------------------------------------------------------------------+
```

Sets a list of symbols to indicates the keyboard prefix used for the
menu item’s keyboard shortcut.

See get-shortcut-prefix for more
information.
