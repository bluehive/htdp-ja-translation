<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/menu_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/menu_.html -->
<!-- Canonical English source for Japanese translation -->

```
+---------------------+------------------------+
| classmenu%: class? |                        |
+---------------------+------------------------+
| superclass: object% |                        |
| extends:            | menu-item-container<%> |
|                     | labelled-menu-item<%>  |
+---------------------+------------------------+
```

A menu% object is a submenu within a menu% or
popup-menu%, or as a top-level menu in a
menu-bar%.

```
+---------------------------------------------------------------------------+
| [constructor]                                                             |
|                                                                           |
| (new menu%                                                                |
| → (is-a?/c menu%)                                                         |
| label: label-string?                                                     |
| parent: (or/c (is-a?/c menu%) (is-a?/c popup-menu%) (is-a?/c menu-bar%)) |
| (or/c (is-a?/c menu%) (is-a?/c popup-menu%)                               |
| (is-a?/c menu-bar%))                                                      |
| help-string: (or/c label-string? #f) = #f                                |
| demand-callback: ((is-a?/c menu%). ->. any) = (lambda (m) (void))      |
|                                                                           |
| ```racket                                                                 |
| (or/c (is-a?/c menu%) (is-a?/c popup-menu%)                               |
|       (is-a?/c menu-bar%))                                                |
| ```                                                                       |
+---------------------------------------------------------------------------+
```

Creates a new menu with the given label.

If label contains a & or tab characters, they are
handled specially in the same way as for menu-item labels and buttons. See
set-label and button%.

If help-string is not #f, the menu has a help
string. See get-help-string for more
information.

The demand-callback procedure is called by the default
on-demand method with the object itself.
