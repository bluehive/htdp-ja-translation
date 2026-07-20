<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/menu-item___.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/menu-item___.html -->
<!-- Canonical English source for Japanese translation -->

```
+------------------------------------+
| interfacemenu-item<%>: interface? |
+------------------------------------+
+------------------------------------+
```

A menu-item<%> object is an element within a menu%,
popup-menu%, or menu-bar%. Operations that affect
the parent — such as renaming the item, deleting the item, or
adding a check beside the item — are accomplished via the
menu-item<%> object.

A menu item is either a separator-menu-item% object (merely
a separator), or a labelled-menu-item<%> object; the latter
is more specifically an instance of either menu-item% (a
plain menu item), checkable-menu-item% (a checkable menu
item), or menu% (a submenu).

```
+-----------------------------------+
| [method]                          |
|                                   |
| (send a-menu-item delete) → void? |
+-----------------------------------+
```

Removes the item from its parent. If the menu item is already deleted,
delete has no effect.

See also restore.

```
+--------------------------------------------------------------------+
| [method]                                                           |
|                                                                    |
| (send a-menu-item get-parent)                                      |
| → (or/c (is-a?/c menu%) (is-a?/c popup-menu%) (is-a?/c menu-bar%)) |
+--------------------------------------------------------------------+
```

Returns the menu, popup menu, or menu bar containing the item. The
parent for a menu item is specified when the menu item is created,
and it cannot be changed.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-menu-item is-deleted?) → boolean? |
+-------------------------------------------+
```

Returns #t if the menu item is deleted from its parent,
#f otherwise.

```
+------------------------------------+
| [method]                           |
|                                    |
| (send a-menu-item restore) → void? |
+------------------------------------+
```

Adds a deleted item back into its parent. The item is always restored
to the end of the parent, regardless of its original position. If the
item is not currently deleted, restore has no
effect.
