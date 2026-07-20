<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/menu-item_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/menu-item_.html -->
<!-- Canonical English source for Japanese translation -->

```
+--------------------------+-------------------------+
| classmenu-item%: class? |                         |
+--------------------------+-------------------------+
| superclass: object%      |                         |
| extends:                 | selectable-menu-item<%> |
+--------------------------+-------------------------+
```

A menu-item% is a plain string-labelled menu item. Its
parent must be a menu% or popup-menu%. When the
user selects the menu item, its callback procedure is called.

```
+--------------------------------------------------------------------------------+
| [constructor]                                                                  |
|                                                                                |
| (new menu-item%                                                                |
| → (is-a?/c menu-item%)                                                         |
| label: label-string?                                                          |
| parent: (or/c (is-a?/c menu%) (is-a?/c popup-menu%))                          |
| callback: ((is-a?/c menu-item%) (is-a?/c control-event%). ->. any)          |
| shortcut: (or/c char? symbol? #f) = #f                                        |
| help-string: (or/c label-string? #f) = #f                                     |
| demand-callback: ((is-a?/c menu-item%). ->. any) = (lambda (i) (void))      |
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
shown, appended to the end of its parent. The callback
procedure is called (with the event type 'menu) when
the user selects the menu item (either via a menu bar,
popup-menu in window<%>, or popup-menu in editor-admin%).

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
