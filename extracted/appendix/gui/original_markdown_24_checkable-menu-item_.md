<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/checkable-menu-item_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/checkable-menu-item_.html -->
<!-- Canonical English source for Japanese translation -->

```
+------------------------------------+-------------------------+
| classcheckable-menu-item%: class? |                         |
+------------------------------------+-------------------------+
| superclass: object%                |                         |
| extends:                           | selectable-menu-item<%> |
+------------------------------------+-------------------------+
```

A checkable-menu-item% is a string-labelled menu item that
maintains a check mark. Its parent must be a menu% or
popup-menu%. When the user selects the menu item, the
item’s check mark is toggled and its callback procedure is called.

```
+--------------------------------------------------------------------------------+
| [constructor]                                                                  |
|                                                                                |
| (new checkable-menu-item%                                                      |
| → (is-a?/c checkable-menu-item%)                                               |
| label: label-string?                                                          |
| parent: (or/c (is-a?/c menu%) (is-a?/c popup-menu%))                          |
| callback: ((is-a?/c checkable-menu-item%) (is-a?/c control-event%). ->.     |
| any) = (lambda (i e) (void))                                                   |
| ((is-a?/c checkable-menu-item%) (is-a?/c control-event%)                       |
|. ->. any)                                                                    |
| shortcut: (or/c char? symbol? #f) = #f                                        |
| help-string: (or/c label-string? #f) = #f                                     |
| demand-callback: ((is-a?/c menu-item%). ->. any) = (lambda (i) (void))      |
| checked: any/c = #f                                                           |
| shortcut-prefix: (and/c (listof (or/c 'alt 'cmd 'meta 'ctl 'shift 'option))   |
| (λ (x) (implies (equal? 'unix (system-type)) (not (and (member 'alt x) (member |
| 'meta x))))) (λ (x) (equal? x (remove-duplicates x)))) =                       |
| (get-default-shortcut-prefix)                                                  |
| (and/c (listof (or/c 'alt 'cmd 'meta 'ctl                                      |
| 'shift 'option))                                                               |
| (λ (x) (implies (equal? 'unix (system-type))                                   |
| (not (and (member 'alt x)                                                      |
| (member 'meta x)))))                                                           |
| (λ (x) (equal? x (remove-duplicates x))))                                      |
|                                                                                |
| ```racket                                                                      |
| ((is-a?/c checkable-menu-item%) (is-a?/c control-event%)                       |
|. ->. any)                                                                   |
| ```                                                                            |
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

Creates a new menu item in parent. The item is initially
shown, appended to the end of its parent, and unchecked. The
callback procedure is called (with the event type
'menu) when the menu item is selected (either via a
menu bar, popup-menu in window<%>, or popup-menu in editor-admin%).

See set-label for information about
mnemonic &s in label.

If shortcut is not #f, the item has a shortcut. See
get-shortcut for more information.
The shortcut-prefix argument determines the set of modifier
keys for the shortcut; see get-shortcut-prefix.

If help is not #f, the item has a help string. See
get-help-string for more information.

The demand-callback procedure is called by the default
on-demand method with the object itself.

By default, the menu item is initially unchecked. If checked
is true, then check is called so that
the menu item is initially checked.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send a-checkable-menu-item check check?) → void? |
| check?: any/c                                    |
+---------------------------------------------------+
```

Checks or unchecks the menu item.

A menu item’s check state can be changed
by the user selecting the item, and such changes do not go through this method; use the menu item callback procedure (provided as an initialization argument) to
monitor check state changes.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-checkable-menu-item is-checked?) → boolean? |
+-----------------------------------------------------+
```

Returns #t if the item is checked, #f otherwise.
