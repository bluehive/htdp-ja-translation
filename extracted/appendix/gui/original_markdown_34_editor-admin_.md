<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/editor-admin_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/editor-admin_.html -->
<!-- Canonical English source for Japanese translation -->

```
+-----------------------------+
| classeditor-admin%: class? |
+-----------------------------+
| superclass: object%         |
+-----------------------------+
```

See Administrators for information about the role of administrators.
The editor-admin% class is never instantiated directly. It
is not even instantiated through derived classes by most programmers;
each editor-canvas% and editor-snip% object
creates its own administrator. However, it may be useful to derive a
new instance of this class to display editors in a new context. Also,
it may be useful to call the methods of an existing administrator
from an owned editor.

To create a new editor-admin% class, all methods described
here must be overridden. They are all invoked by the administrator’s
editor.

```
+-----------------------------------------------+
| [constructor]                                 |
|                                               |
| (new editor-admin%) → (is-a?/c editor-admin%) |
+-----------------------------------------------+
```

Creates a (useless) editor administrator.

```
+-----------------------------------------------------------------+
| [method]                                                        |
|                                                                 |
| (send an-editor-admin get-dc [x y]) → (or/c (is-a?/c dc<%>) #f) |
| x: (or/c (box/c real?) #f) = #f                                |
| y: (or/c (box/c real?) #f) = #f                                |
+-----------------------------------------------------------------+
```

Specification:
Returns either the drawing context into which the editor is displayed,
or the context into which it is currently being drawn. When the
editor is not embedded, the returned context is always the drawing
content into which the editor is displayed. If the editor is not
displayed, #f is returned.

The origin of the drawing context is also returned, translated into
the local coordinates of the editor. For an embedded editor, the
returned origin is reliable only while the editor is being drawn, or
while it receives a mouse or keyboard event.

The x box is filled with the x-origin of the DC in editor coordinates, unless x is #f.
The y box is filled with the y-origin of the DC in editor coordinates, unless y is #f.

See also editor-location-to-dc-location in editor<%> and
dc-location-to-editor-location in editor<%>.

Default implementation:
Fills all boxes with 0.0 and returns #f.

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send an-editor-admin get-max-view                    |
| x: (or/c (box/c real?) #f)                           |
| y: (or/c (box/c real?) #f)                           |
| w: (or/c (box/c (and/c real? (not/c negative?))) #f) |
| h: (or/c (box/c (and/c real? (not/c negative?))) #f) |
| full?: any/c = #f                                    |
+-------------------------------------------------------+
```

Specification:
Same as get-view unless the editor is visible
in multiple standard displays. If the editor has multiple
displays, a region is computed that includes the visible
region in all displays.

See get-view.

Default implementation:
Fills all boxes with 0.0.

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send an-editor-admin get-view x y w h [full?]) → void? |
| x: (or/c (box/c real?) #f)                             |
| y: (or/c (box/c real?) #f)                             |
| w: (or/c (box/c (and/c real? (not/c negative?))) #f)   |
| h: (or/c (box/c (and/c real? (not/c negative?))) #f)   |
| full?: any/c = #f                                      |
+---------------------------------------------------------+
```

Specification:
Gets the visible region of the editor within its display (in
editor coordinates), or the overall size of the viewing region in the
editor’s top-level display (for an embedded editor).

If the display is an editor canvas, see also
reflow-container. The viewing area within
an editor canvas is not the full client area of the canvas, because
an editor canvas installs a whitespace border around a displayed
editor within the client area.

The calculation of the editor’s visible region is based on the current
size and scrollbar values of the top-level display. For an
editor canvas display, the region reported by
get-view does not depend on whether the canvas
is hidden, obscured by other windows, or moved off the edge of the
screen.

The x box is filled with the left edge of the visible region in editor coordinates, unless x is #f.
The y box is filled with the top edge of the visible region in editor coordinates, unless y is #f.
The w box is filled with the width of the visible region, which may be larger than the editor itself, unless w is #f.
The h box is filled with the height of the visible region, which may be larger than the editor itself, unless h is #f.

If an editor is fully visible and full? is #f, then
x and y will both be filled with 0.

If full? is a true value, then the returned area is the view
area of the top-level display for the editor. This result
is different only when the editor is embedded in another editor; in
that case, the x and y values may be meaningless,
because they are in the coordinate system of the immediate editor
within the top-level display.

Default implementation:
Fills all boxes with 0.0.

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send an-editor-admin grab-caret [domain]) → void?    |
| domain: (or/c 'immediate 'display 'global) = 'global |
+-------------------------------------------------------+
```

Specification:
Called by the editor to request the keyboard focus. If the request is
granted, then the administered editor’s own-caret
method will be called.

See set-caret-owner for information about the
possible values of domain.

Default implementation:
Does nothing.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send an-editor-admin modified modified?) → void? |
| modified?: any/c                                 |
+---------------------------------------------------+
```

Specification:
Called by the editor to report that its modification state has
changed to either modified or unmodified.

See also set-modified in editor<%>.

Default implementation:
Does nothing.

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send an-editor-admin needs-update  |
| localx: real?                      |
| localy: real?                      |
| w: (and/c real? (not/c negative?)) |
| h: (and/c real? (not/c negative?)) |
+-------------------------------------+
```

Specification:
Called by the editor to request a refresh to its displayed
representation. When the administrator decides that the displayed
should be refreshed, it calls the editor’s refresh
method.

The localx, localy, w, and h
arguments specify a region of the editor to be updated (in editor
coordinates).

Default implementation:
Does nothing.

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send an-editor-admin popup-menu menu x y) → boolean? |
| menu: (is-a?/c popup-menu%)                          |
| x: real?                                             |
| y: real?                                             |
+-------------------------------------------------------+
```

Specification:

Pops up the given popup-menu% object at the specified
coordinates (in this window’s coordinates), and returns after
handling an unspecified number of events; the menu may still be
popped up when this method returns. If a menu item is selected from
the popup-menu, the callback for the menu item is called. (The
eventspace for the menu item’s callback is the administrator’s display’s eventspace.)

While the menu is popped up, its target is set to the top-level editor in this administrator’s display. See
get-popup-target
for more information.

The result is #f if this admin is not connected to
a canvas or the canvas it is connected to does not have an editor,
#t otherwise (independent of whether the
user selects an item in the popup menu).

The menu is displayed at x and y in editor coordinates.

Default implementation:
Returns #f.

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send an-editor-admin refresh-delayed?) → boolean? |
+----------------------------------------------------+
```

Specification:
Returns #t if updating on this administrator’s
display is currently delayed (usually by
begin-edit-sequence in editor<%> in an enclosing editor).

Default implementation:
Returns #f.

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send an-editor-admin resized refresh?) → void? |
| refresh?: any/c                                |
+-------------------------------------------------+
```

Specification:
Called by the editor to notify its display that the
editor’s size or scroll count has changed, so the scrollbars need to
be adjusted to reflect the new size. The editor generally needs to be
updated after a resize, but the editor decides whether the update
should occur immediately. If refresh? is not #f,
then the editor is requesting to be updated immediately.

Default implementation:
Does nothing.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send an-editor-admin scroll-to         |
| localx: real?                          |
| localy: real?                          |
| w: (and/c real? (not/c negative?))     |
| h: (and/c real? (not/c negative?))     |
| refresh?: any/c = #t                   |
| bias: (or/c 'start 'end 'none) = 'none |
+-----------------------------------------+
```

Specification:
Called by the editor to request scrolling so that the given region is
visible. The editor generally needs to be updated after a scroll, but
the editor decides whether the update should occur immediately.

The localx, localy, w, and h
arguments specify a region of the editor to be made visible by the
scroll (in editor coordinates).

If refresh? is not #f, then the editor is requesting
to be updated immediately.

The bias argument is one of:

- 'start — if the range doesn’t fit in the visible area, show the top-left region
- 'none — no special scrolling instructions
- 'end — if the range doesn’t fit in the visible area, show the bottom-right region

The return value is #t if the display is scrolled,
#f if not (either because the requested region is already
visible, because the display has zero size, or because the
editor is currently printing).

If an editor has multiple displays, then if any display
currently has the keyboard focus, it is scrolled. Otherwise, the
“primary owner” of the editor (see call-as-primary-owner) is scrolled.

Default implementation:
Return #f

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send an-editor-admin update-cursor) → void? |
+----------------------------------------------+
```

Specification:
Queues an update for the cursor in the display for this
editor. The actual cursor used will be determined by calling the
editor’s adjust-cursor method.

Default implementation:
Does nothing.
