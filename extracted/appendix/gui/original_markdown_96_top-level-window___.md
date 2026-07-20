<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/top-level-window___.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/top-level-window___.html -->
<!-- Canonical English source for Japanese translation -->

```
+-------------------------------------------+--------------------------+
| interfacetop-level-window<%>: interface? |                          |
+-------------------------------------------+--------------------------+
| implements:                               | area-container-window<%> |
+-------------------------------------------+--------------------------+
```

A top-level window is either a frame% or dialog%
object.

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-top-level-window can-close?) → boolean? |
+-------------------------------------------------+
```

Refine this method with augment.

Called just before the window might be closed (e.g., by the window
manager). If #f is returned, the window is not closed,
otherwise on-close is called and the
window is closed (i.e., the window is hidden, like calling
show with #f).

This method is not called by show.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-top-level-window can-exit?) → boolean? |
+------------------------------------------------+
```

Specification:
Called before on-exit to check whether an
exit is allowed. See on-exit for more
information.

Default implementation:
Calls can-close? and returns the result.

```
+--------------------------------------------------------+
| [method]                                               |
|                                                        |
| (send a-top-level-window center [direction]) → void?   |
| direction: (or/c 'horizontal 'vertical 'both) = 'both |
+--------------------------------------------------------+
```

Centers the window on the screen if it has no parent. If it has a
parent, the window is centered with respect to its parent’s location.

If direction is 'horizontal, the window is centered
horizontally. If direction is 'vertical, the
window is centered vertically. If direction is
'both, the window is centered in both directions.

```
+------------------------------------------------------------+
| [method]                                                   |
|                                                            |
| (send a-top-level-window get-edit-target-object)           |
| → (or/c (or/c (is-a?/c window<%>) (is-a?/c editor<%>)) #f) |
+------------------------------------------------------------+
```

Like
get-edit-target-window, but if an editor
canvas had the focus and it also displays an editor, the editor is
returned instead of the canvas. Further, if the editor’s focus is
delegated to an embedded editor, the embedded editor is returned.

See also get-focus-object.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-top-level-window get-edit-target-window) |
| → (or/c (is-a?/c window<%>) #f)                  |
+--------------------------------------------------+
```

Returns the window that
most recently had the keyboard focus, either the top-level window or
one of its currently-shown children. If neither the window nor any of
its currently-shown children has even owned the keyboard focus,
#f is returned.

See also get-focus-window and
get-edit-target-object.

```
+--------------------------------------------------------+
| [method]                                               |
|                                                        |
| (send a-top-level-window get-eventspace) → eventspace? |
+--------------------------------------------------------+
```

Returns the window’s eventspace.

```
+------------------------------------------------------------+
| [method]                                                   |
|                                                            |
| (send a-top-level-window get-focus-object)                 |
| → (or/c (or/c (is-a?/c window<%>) (is-a?/c editor<%>)) #f) |
+------------------------------------------------------------+
```

Like get-focus-window, but if an editor canvas has the focus and it also
displays an editor, the editor is returned instead of the
canvas. Further, if the editor’s focus is delegated to an embedded
editor, the embedded editor is returned.

See also get-edit-target-object.

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send a-top-level-window get-focus-window) |
| → (or/c (is-a?/c window<%>) #f)            |
+--------------------------------------------+
```

Returns the window that has the keyboard
focus, either the top-level window or one of its children. If neither
the window nor any of its children has the focus, #f is
returned.

See also get-edit-target-window and
get-focus-object.

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send a-top-level-window move x y) → void? |
| x: position-integer?                      |
| y: position-integer?                      |
+--------------------------------------------+
```

Moves the window to the given position on the screen.

A window’s position can be changed
by the user dragging the window, and such changes do not go through this method; use on-move to
monitor position changes.

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-top-level-window on-activate active?) → void? |
| active?: any/c                                       |
+-------------------------------------------------------+
```

Called when a window is activated or
deactivated. A top-level window is activated when the
keyboard focus moves from outside the window to the window or one of
its children. It is deactivated when the focus moves back out of the
window. On Mac OS, a child of a floating frames can have the
focus instead of a child of the active non-floating frame; in other
words, floating frames act as an extension of the active non-frame
for keyboard focus.

The method’s argument is #t when the window is activated,
#f when it is deactivated.

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send a-top-level-window on-close) → void? |
+--------------------------------------------+
```

Refine this method with augment.

Called just before the window is closed (e.g., by the window manager).
This method is not called by show.

See also
can-close?.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-top-level-window on-exit) → void? |
+-------------------------------------------+
```

Specification:
Called by the default application quit handler (as determined by the
application-quit-handler parameter) when the operating
system requests that the application shut down (e.g., when the
Quit menu item is selected in the main application menu
on Mac OS). In that case, this method is called for the most
recently active top-level window in the initial eventspace, but only
if the window’s can-exit? method first
returns true.

Default implementation:
Calls
on-close and then
show to hide the window.

```
+------------------------------------------------------+
| [method]                                             |
|                                                      |
| (send a-top-level-window on-message message) → any/c |
| message: any/c                                      |
+------------------------------------------------------+
```

Specification:
A generic message method, usually called by
send-message-to-window.

If the method is invoked by send-message-to-window, then it
is invoked in the thread where send-message-to-window was
called (which is possibly not the handler thread of the
window’s eventspace).

Default implementation:
Returns #<void>.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send a-top-level-window display-changed) → any/c |
+---------------------------------------------------+
```

Specification: Called when the displays configuration changes.

To determine the new monitor configuration, use
get-display-count, get-display-size,
get-display-left-top-inset, and
get-display-backing-scale.

Note that this method may be invoked multiple times for a single
logical change to the monitors.

Default implementation: Returns #<void>.

```
+-------------------------------------------------------------+
| [method]                                                    |
|                                                             |
| (send a-top-level-window on-traverse-char event) → boolean? |
| event: (is-a?/c key-event%)                                |
+-------------------------------------------------------------+
```

Specification:
Attempts to handle the given
keyboard event as a navigation event, such as a Tab key event that
moves the keyboard focus. If the event is handled, #t is
returned, otherwise #f is returned.

Default implementation:
The following rules determine, in order, whether and how event
is handled:

- If the window that currently owns the focus specifically handles the
event, then #f is returned. The following describes window
types and the keyboard events they specifically handle:
editor-canvas% — tab-exit is disabled (see
allow-tab-exit): all keyboard events, except alphanumeric key events when the Meta
(Unix) or Alt (Windows) key is pressed; when tab-exit is enabled:
all keyboard events except Tab, Enter, Escape, and alphanumeric
Meta/Alt events.canvas% — when tab-focus is disabled (see
accept-tab-focus): all keyboard events, except alphanumeric key events when the Meta
(Unix) or Alt (Windows) key is pressed; when tab-focus is enabled:
no key eventstext-field%, 'single style — arrow key
events and alphanumeric key events when the Meta (Unix) or Alt
(Windows) key is not pressed (and all alphanumeric events on
Mac OS)text-field%, 'multiple style — all
keyboard events, except alphanumeric key events when the Meta (Unix) or
Alt (Windows) key is pressedchoice% — arrow key events and alphanumeric key
events when the Meta (Unix) or Alt (Windows) key is not pressedlist-box% — arrow key events and alphanumeric key
events when the Meta (Unix) or Alt (Windows) key is not pressed
- If event is a Tab or arrow key event, the keyboard focus is
moved within the window and #t is returned. Across platforms,
the types of windows that accept the keyboard focus via navigation
may vary, but text-field% windows always accept the focus,
and message%, gauge%, and panel%
windows never accept the focus.
- If event is a Space key event and the window that currently
owns the focus is a button%, check-box%, or
radio-box% object, the event is handled in the same way as
a click on the control and #t is returned.
- If event is an Enter key event and the current top-level window
contains a border button, the button’s callback is invoked and
#t is returned. (The 'border style for a
button% object indicates to the user that pressing Enter
is the same as clicking the button.) If the window does not contain a
border button, #t is returned if the window with the current
focus is not a text field or editor canvas.
- In a dialog, if event is an Escape key event, the event is
handled the same as a click on the dialog’s close box (i.e., the
dialog’s
can-close? and
on-close methods are called, and the dialog is hidden) and #t is
returned.
- If event is an alphanumeric key event and the current top-level
window contains a control with a mnemonic matching the key (which is
installed via a label that contains &; see
get-label for more information), then the
keyboard focus is moved to the matching control. Furthermore, if the
matching control is a button%, check-box%, or
radio-box% button, the keyboard event is handled in the
same way as a click on the control.
- Otherwise, #f is returned.

```
+----------------------------------------------------------------+
| [method]                                                       |
|                                                                |
| (send a-top-level-window on-system-menu-char event) → boolean? |
| event: (is-a?/c key-event%)                                   |
+----------------------------------------------------------------+
```

Checks whether the given event pops open the system menu in the
top-left corner of the window (Windows only). If the window’s system
menu is opened, #t is returned, otherwise #f is
returned.

```
+---------------------------------+
| [method]                        |
|                                 |
| (send a-top-level-window resize |
| width: dimension-integer?      |
| height: dimension-integer?     |
+---------------------------------+
```

Sets the size of the window (in pixels), but only if the given size is
larger than the window’s minimum size.

A window’s size can be changed
by the user, and such changes do not go through this method; use on-size to
monitor size changes.

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send a-top-level-window set-icon          |
| icon: (is-a?/c bitmap%)                   |
| mask: (is-a?/c bitmap%) = #f              |
| which: (or/c 'small 'large 'both) = 'both |
+--------------------------------------------+
```

Sets the large or small icon bitmap for the window. Future changes to
the bitmap do not affect the window’s icon.

The icon is used in a platform-specific way:

- Windows — the small icon is used for the window’s icon (in the
top-left) and in the task bar, and the large icon is used for
the Alt-Tab task switcher.
- Mac OS — both icons are ignored.
- Unix — many window managers use the small icon in the same way
as Windows, and others use the small icon when iconifying the
frame; the large icon is ignored.

The bitmap for either icon can be any size, but most platforms scale
the small bitmap to 16 by 16 pixels and the large bitmap to 32 by 32
pixels.

If a mask bitmap is not provided, then the entire (rectangular) bitmap
is used as an icon.

If a mask bitmap is provided, the mask must be monochrome. In the mask
bitmap, use black pixels to indicate the icon’s region and use white
pixels outside the icon’s region. In the icon bitmap, use black
pixels for the region outside the icon.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-top-level-window show show) → void? |
| show: any/c                                |
+---------------------------------------------+
```

If the window is already shown, it is moved front of other top-level
windows. If the window is iconized (frames only), it is deiconized.

See also show in window<%>.
