<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/menu-item-container___.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/menu-item-container___.html -->
<!-- Canonical English source for Japanese translation -->

```
+----------------------------------------------+
| interfacemenu-item-container<%>: interface? |
+----------------------------------------------+
+----------------------------------------------+
```

A menu-item-container<%> object is a menu%,
popup-menu%, or menu-bar%.

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-menu-item-container get-items) |
| → (listof (is-a?/c menu-item<%>))      |
+----------------------------------------+
```

Returns a list of the items in the menu, popup menu, or menu bar. The
order of the items in the returned list corresponds to the order as
the user sees them in the menu or menu bar.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-menu-item-container on-demand) → void? |
+------------------------------------------------+
```

Specification:
Called when the user clicks on the container as a menu bar (before the
user sees any menu items, except with Unity’s global menu bar as
noted below), just before the container as a popup menu
is popped up, or just before inspecting the menu bar containing the
item for a shortcut key binding.

If the container is not a menu bar or a popup menu, this method is
normally called via the on-demand
method of the container’s owning menu bar or popup menu, because the
default implementation of the method chains to the
on-demand method of its
items. However, the method can be overridden in a container such that
it does not call the on-demand method
of its items.

On Unix with the Unity window manager using the global menu bar (which
is the default on Ubuntu), racket/gui/base receives no
notification when the user clicks the menu bar. To approximate
on-demand triggered by user clicks of
the menu bar, on-demand is called for
a menu bar whenever its frame% object loses the
keyboard focus. Beware that if keyboard focus was lost because a menu
was clicked, then items added to the clicked menu during an
on-demand invocation may not appear
for the user.

Default implementation:
Calls the demand-callback procedure that was provided when
the object was created, then calls the on-demand method of the contained items.
