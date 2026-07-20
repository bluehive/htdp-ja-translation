<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/menu-bar_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/menu-bar_.html -->
<!-- Canonical English source for Japanese translation -->

> [image: menu-bar.png]

```
+-------------------------+------------------------+
| classmenu-bar%: class? |                        |
+-------------------------+------------------------+
| superclass: object%     |                        |
| extends:                | menu-item-container<%> |
+-------------------------+------------------------+
```

A menu-bar% object is created for a particular
frame% object. A frame can have at most one menu bar;
an exn:fail:contract exception is raised when a new menu bar is created for a frame that
already has a menu bar.

```
+--------------------------------------------------------------------------+
| [constructor]                                                            |
|                                                                          |
| (new menu-bar%                                                           |
| → (is-a?/c menu-bar%)                                                    |
| parent: (or/c (is-a?/c frame%) 'root)                                   |
| demand-callback: ((is-a?/c menu-bar%). ->. any) = (lambda (m) (void)) |
+--------------------------------------------------------------------------+
```

Creates a menu bar in the specified frame. The menu bar is initially
empty. If 'root is supplied as parent, the
menu bar becomes active only when no other frames are shown. A
'root parent is allowed only when
current-eventspace-has-menu-root? returns #t, and
only if no such menu bar has been created before, otherwise
an exn:fail:contract exception is raised.

The demand-callback procedure is called by the default
on-demand method with the object itself.

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send a-menu-bar enable enable?) → void? |
| enable?: any/c                          |
+------------------------------------------+
```

Enables or disables the menu bar (i.e., all of its menus). Each
menu’s is-enabled? method returns
#f only if the menu is specifically disabled (in addition to
the menu bar).

```
+-------------------------------------------------------------+
| [method]                                                    |
|                                                             |
| (send a-menu-bar get-frame) → (or/c (is-a?/c frame%) 'root) |
+-------------------------------------------------------------+
```

Returns the menu bar’s frame, or returns 'root if the menu
bar is shown when no other frames are shown.

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send a-menu-bar is-enabled?) → boolean? |
+------------------------------------------+
```

Returns #t if the menu bar is enabled, #f otherwise.
