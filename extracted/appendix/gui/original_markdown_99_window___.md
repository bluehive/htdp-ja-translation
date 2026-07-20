<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/window___.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/window___.html -->
<!-- Canonical English source for Japanese translation -->

```
+---------------------------------+---------+
| interfacewindow<%>: interface? |         |
+---------------------------------+---------+
| implements:                     | area<%> |
+---------------------------------+---------+
```

A window<%> object is an area<%> with a graphical
representation that can respond to events.

All window<%> classes accept the following named instantiation
arguments:

- enabled — default is #t; passed to
enable if #f

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send a-window accept-drop-files) → boolean?            |
| (send a-window accept-drop-files accept-files?) → void? |
| accept-files?: any/c                                   |
+---------------------------------------------------------+
```

Enables or disables drag-and-drop dropping
for the window, or gets the enable state. Dropping is initially
disabled. See also on-drop-file.

```
+---------------------------------------+
| [method]                              |
|                                       |
| (send a-window client->screen x y)    |
| → position-integer? position-integer? |
| position-integer?                     |
| x: position-integer?                 |
| y: position-integer?                 |
+---------------------------------------+
```

Converts local window coordinates to
screen coordinates.

On Mac OS, the screen coordinates start with (0, 0) at the
upper left of the menu bar. In contrast, move in top-level-window<%> considers (0, 0) to be below the menu bar. See also
get-display-left-top-inset.

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-window enable enable?) → void? |
| enable?: any/c                        |
+----------------------------------------+
```

Enables or disables a window so that input events are ignored. (Input
events include mouse events, keyboard events, and close-box clicks,
but not focus or update events.) When a window is disabled, input
events to its children are also ignored.

The enable state of a window can be changed
by enabling a parent window, and such changes do not go through this method; use on-superwindow-enable to
monitor enable state changes.

If enable? is true, the window is enabled, otherwise it is
disabled.

```
+-------------------------------+
| [method]                      |
|                               |
| (send a-window focus) → void? |
+-------------------------------+
```

Moves the keyboard focus to the
window, relative to its top-level window, if the window ever accepts
the keyboard focus. If the focus is in the window’s top-level
window or if the window’s top-level window is visible and floating
(i.e., created with the 'float style), then the focus is
immediately moved to this
window. Otherwise, the focus is not immediately moved, but when the
window’s top-level window gets the keyboard focus, the focus is
delegated to this window.

See also
on-focus.

Note that on Unix, keyboard focus can move to the menu bar
when the user is selecting a menu item.

The current keyboard focus window can be changed
by the user, and such changes do not go through this method; use on-focus to
monitor focus changes.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-window get-client-handle) → cpointer? |
+-----------------------------------------------+
```

Returns a handle to the “inside” of the window for the current
platform’s GUI toolbox. The value that the pointer represents depends
on the platform:

- Windows: `HWND`
- Mac OS: `NSView`
- Unix: `GtkWidget`

See also get-handle.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-window get-client-size)         |
| → dimension-integer? dimension-integer? |
| dimension-integer?                      |
+-----------------------------------------+
```

Gets the interior size of the window in pixels. For a container, the
interior size is the size available for placing subwindows (including
the border margin). For a canvas, this is the visible drawing
area.

The client size is returned as two values: width and height (in pixels).

See also
reflow-container.

```
+----------------------------------------------------------+
| [method]                                                 |
|                                                          |
| (send a-window get-cursor) → (or/c (is-a?/c cursor%) #f) |
+----------------------------------------------------------+
```

Returns the window’s cursor, or #f if this window’s cursor
defaults to the parent’s cursor. See
set-cursor for more information.

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-window get-handle) → cpointer? |
+----------------------------------------+
```

Returns a handle to the “outside” of the window for the current platform’s GUI
toolbox. The value that the pointer represents depends on the
platform:

- Windows: `HWND`
- Mac OS: `NSWindow` for a top-level-window<%> object,
`NSView` for other windows
- Unix: `GtkWidget`

See also get-client-handle.

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-window get-height) → dimension-integer? |
+-------------------------------------------------+
```

Returns the window’s total height (in pixels).

See also
reflow-container.

```
+----------------------------------------------------------------------------+
| [method]                                                                   |
|                                                                            |
| (send a-window get-label)                                                  |
| → (or/c label-string? (is-a?/c bitmap%) (or/c 'app 'caution 'stop) (list/c |
| (is-a?/c bitmap%) label-string? (or/c 'left 'top 'right 'bottom)) #f)      |
| (or/c label-string?                                                        |
| (is-a?/c bitmap%)                                                          |
| (or/c 'app 'caution 'stop)                                                 |
| (list/c (is-a?/c bitmap%)                                                  |
| label-string?                                                              |
| (or/c 'left 'top 'right 'bottom))                                          |
| #f)                                                                        |
|                                                                            |
| ```racket                                                                  |
| (or/c label-string?                                                        |
|       (is-a?/c bitmap%)                                                    |
|       (or/c 'app 'caution 'stop)                                           |
|       (list/c (is-a?/c bitmap%)                                            |
|               label-string?                                                |
|               (or/c 'left 'top 'right 'bottom))                            |
|       #f)                                                                  |
| ```                                                                        |
+----------------------------------------------------------------------------+
```

Gets a window’s label, if any. Control windows generally display their
label in some way. Frames and dialogs display their label as a window
title. Panels do not display their label, but the label can be used
for identification purposes. Messages, buttons, and check boxes can
have bitmap labels (only when they are created with bitmap labels),
but all other windows have string labels. In addition, a message
label can be an icon symbol 'app, 'caution, or
'stop, and a button can have both a bitmap label and a
string label (along with a position for the bitmap).

A label string may contain &s, which serve as
keyboard navigation annotations for controls on Windows and Unix. The
ampersands are not part of the displayed label of a control; instead,
ampersands are removed in the displayed label (on all platforms),
and any character preceding an ampersand is underlined (Windows and
Unix) indicating that the character is a mnemonic for the
control. Double ampersands are converted into a single ampersand
(with no displayed underline). See also
on-traverse-char.

If the window does not have a label, #f is returned.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-window get-plain-label) → (or/c string? #f) |
+-----------------------------------------------------+
```

Like
get-label, except that:

- If the label includes (&c ) for
any character c, then the sequenece and any surrounding
whitespace is removed.
- If the label contains &c for any character c,
the & is removed.
- If the label contains a tab character, then the tab character and all following
characters are removed.

See also button%’s handling of labels.

If the window has
no label or the window’s
label is not a string, #f is returned.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-window get-size)                |
| → dimension-integer? dimension-integer? |
| dimension-integer?                      |
+-----------------------------------------+
```

Gets the current size of the entire window in pixels, not counting
horizontal and vertical margins. (On Unix, this size does not include
a title bar or borders for a frame/dialog.) See also
get-client-size.

The geometry is returned as two values: width and height (in pixels).

See also
reflow-container.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-window get-width) → dimension-integer? |
+------------------------------------------------+
```

Returns the window’s current total width (in pixels).

See also
reflow-container.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-window get-x) → position-integer? |
+-------------------------------------------+
```

Returns the position of the window’s left edge in its
parent’s coordinate system.

See also
reflow-container.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-window get-y) → position-integer? |
+-------------------------------------------+
```

Returns the position of the window’s top edge in its
parent’s coordinate system.

See also
reflow-container.

```
+---------------------------------------+
| [method]                              |
|                                       |
| (send a-window has-focus?) → boolean? |
+---------------------------------------+
```

Indicates whether the window currently has the keyboard focus. See
also
on-focus.

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-window is-enabled?) → boolean? |
+----------------------------------------+
```

Indicates whether the window is currently enabled or not. The result is
#t if this window is enabled when its ancestors are enabled, or
#f if this window remains disable when its ancestors are
enabled. (That is, the result of this method is affected only by calls
to enable for a-window, not by the enable state of
parent windows.)

```
+--------------------------------------+
| [method]                             |
|                                      |
| (send a-window is-shown?) → boolean? |
+--------------------------------------+
```

Indicates whether the window is currently shown or not. The result is
#t if this window is shown when its ancestors are shown, or
#f if this window remains hidden when its ancestors are
shown. (That is, the result of this method is affected only by calls
to show for a-window, not by the visibility of
parent windows.)

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-window on-drop-file pathname) → void? |
| pathname: path?                              |
+-----------------------------------------------+
```

Called when the user drags a file onto the
window. (On Unix, drag-and-drop is supported via the XDND
protocol.) Drag-and-drop must first be enabled for the window with
accept-drop-files.

On Mac OS, when the application is running and user
double-clicks an application-handled file or drags a file onto the
application’s icon, the main thread’s application file handler is
called (see
application-file-handler). The default handler calls the
on-drop-file method of the most-recently activated frame if drag-and-drop is
enabled for that frame, independent of the frame’s eventspace (but
the method is called in the frame’s eventspace’s handler
thread). When the application is not running, the filenames are
provided as command-line arguments.

```
+--------------------------------------+
| [method]                             |
|                                      |
| (send a-window on-focus on?) → void? |
| on?: any/c                          |
+--------------------------------------+
```

Specification:
Called when a window
receives or loses the keyboard focus. If the argument is #t,
the keyboard focus was received, otherwise it was lost.

Note that on Unix, keyboard focus can move to the menu bar
when the user is selecting a menu item.

Default implementation:
Does nothing.

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-window on-move x y) → void? |
| x: position-integer?               |
| y: position-integer?               |
+-------------------------------------+
```

Specification:
Called when the window is moved. (For windows that are not top-level
windows, “moved” means moved relative to the parent’s top-left
corner.) The new position is provided to the method.

Default implementation:
Does nothing.

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-window on-size width height) → void? |
| width: dimension-integer?                   |
| height: dimension-integer?                  |
+----------------------------------------------+
```

Specification:
Called when the window is resized. The window’s new size (in pixels)
is provided to the method. The size values are for the entire window,
not just the client area.

Default implementation:
Does nothing.

```
+----------------------------------+
| [method]                         |
|                                  |
| (send a-window on-subwindow-char |
| receiver: (is-a?/c window<%>)   |
| event: (is-a?/c key-event%)     |
+----------------------------------+
```

Specification:
Called when this window or a child window receives a keyboard event.
The
on-subwindow-char method of the receiver’s top-level window is called first (see
get-top-level-window); if the return value is #f, then the
on-subwindow-char method is called for the next child in the path to the receiver, and
so on. Finally, if the receiver’s
on-subwindow-char method returns #f, the event is passed on to the receiver’s
normal key-handling mechanism.

The event argument is the event that was generated for the
receiver window.

The atomicity limitation on-subwindow-event applies
to on-subwindow-char as well. That is, an insufficiently cooperative
on-subwindow-char method can effectively disable
a control’s handling of key events, even when it returns #f

BEWARE: The default
on-subwindow-char in frame% and
on-subwindow-char in dialog% methods consume certain keyboard events (e.g., arrow keys, Enter) used
for navigating within the window. Because the top-level window gets
the first chance to handle the keyboard event, some events never
reach the “receiver” child unless the default frame or dialog
method is overridden.

Default implementation:
Returns #f.

```
+-----------------------------------+
| [method]                          |
|                                   |
| (send a-window on-subwindow-event |
| receiver: (is-a?/c window<%>)    |
| event: (is-a?/c mouse-event%)    |
+-----------------------------------+
```

Specification:
Called when this window or a child window receives a mouse event.
The
on-subwindow-event method of the receiver’s top-level window is called first (see
get-top-level-window); if the return value is #f, the
on-subwindow-event method is called for the next child in the path to the receiver, and
so on. Finally, if the receiver’s
on-subwindow-event method returns #f, the event is passed on to the
receiver’s normal mouse-handling mechanism.

The event argument is the event that was generated for the
receiver window.

If the on-subwindow-event method chain does not complete
atomically (i.e., without requiring other threads to run) or does not complete
fast enough, then the corresponding event may not be delivered to a target
control, such as a button. In other words, an insufficiently cooperative
on-subwindow-event method can effectively disable a
control’s handling of mouse events, even when it returns #f.

Default implementation:
Returns #f.

```
+-----------------------------------+
| [method]                          |
|                                   |
| (send a-window on-subwindow-focus |
| receiver: (is-a?/c window<%>)    |
| on?: boolean?                    |
+-----------------------------------+
```

Specification:
Called when this window or a child window receives or loses the keyboard focus.
This method is called after the on-focus method of receiver.
The
on-subwindow-focus method of the receiver’s top-level window is called first (see
get-top-level-window), then the
on-subwindow-focus method is called for the next child in the path to the receiver, and
so on.

Default implementation:
Does nothing.

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send a-window on-superwindow-activate active?) → void? |
| active?: any/c                                         |
+---------------------------------------------------------+
```

Specification: Called via the event queue whenever the containing top-level-window<%>
is either activated or deactivated (see on-activate).

Default implementation: Does nothing.

Added in version 1.54 of package `gui-lib`.

```
+--------------------------------------------------------+
| [method]                                               |
|                                                        |
| (send a-window on-superwindow-enable enabled?) → void? |
| enabled?: any/c                                       |
+--------------------------------------------------------+
```

Specification:
Called via the event queue whenever the enable state of a window has
changed, either through a call to the window’s
enable method, or through the enabling/disabling of one of the window’s
ancestors. The method’s argument indicates whether the window is now
enabled or not.

This method is not called when the window is initially created; it is
called only after a change from the window’s initial enable
state. Furthermore, if an enable notification event is queued for the
window and it reverts its enabled state before the event is
dispatched, then the dispatch is canceled.

If the enable state of a window’s ancestor changes while the window is
deleted (e.g., because it was removed with
delete-child), then no enable events are queued for the deleted window. But if
the window is later re-activated into an enable state that is
different from the window’s state when it was de-activated, then an
enable event is immediately queued.

Default implementation:
Does nothing.

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-window on-superwindow-show shown?) → void? |
| shown?: any/c                                     |
+----------------------------------------------------+
```

Specification:
Called via the event queue whenever the visibility of a window has
changed, either through a call to the window’s
show, through the showing/hiding of one of the window’s ancestors, or
through the activating or deactivating of the window or its ancestor
in a container (e.g., via
delete-child). The method’s argument indicates whether the window is now
visible or not.

This method is not called when the window is initially created; it is
called only after a change from the window’s initial
visibility. Furthermore, if a show notification event is queued for
the window and it reverts its visibility before the event is
dispatched, then the dispatch is canceled.

Default implementation:
Does nothing.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-window popup-menu menu x y) → void? |
| menu: (is-a?/c popup-menu%)                |
| x: position-integer?                       |
| y: position-integer?                       |
+---------------------------------------------+
```

Pops up the given popup-menu% object at the specified
coordinates (in this window’s coordinates), and returns after
handling an unspecified number of events; the menu may still be
popped up when this method returns. If a menu item is selected from
the popup-menu, the callback for the menu item is called. (The
eventspace for the menu item’s callback is the window’s eventspace.)

While the menu is popped up, its target is set to the window. See
get-popup-target
for more information.

The menu is popped up within the window at position
(x, y).

```
+---------------------------------+
| [method]                        |
|                                 |
| (send a-window refresh) → void? |
+---------------------------------+
```

Enqueues a window-refresh event to repaint the window; see
Event Types and Priorities for more information
on the event’s priority.

```
+---------------------------------------+
| [method]                              |
|                                       |
| (send a-window screen->client x y)    |
| → position-integer? position-integer? |
| position-integer?                     |
| x: position-integer?                 |
| y: position-integer?                 |
+---------------------------------------+
```

Converts global coordinates to window
local coordinates. See also client->screen for information
on screen coordinates.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-window set-cursor cursor) → void? |
| cursor: (or/c (is-a?/c cursor%) #f)      |
+-------------------------------------------+
```

Sets the window’s cursor. Providing #f instead of a cursor
value removes the window’s cursor.

If a window does not have a cursor, it uses the cursor of its parent.
Frames and dialogs start with the standard arrow cursor, and text
fields start with an I-beam cursor. All other windows are created
without a cursor.

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-window set-label l) → void? |
| l: label-string?                   |
+-------------------------------------+
```

Sets a window’s label. The window’s natural minimum size might be
different after the label is changed, but the window’s minimum size
is not recomputed.

If the window was not created with a label, or if the window was
created with a non-string label, l is ignored.

See
get-label for more information.

```
+------------------------------------+
| [method]                           |
|                                    |
| (send a-window show show?) → void? |
| show?: any/c                      |
+------------------------------------+
```

Shows or hides a window.

The visibility of a window can be changed
by the user clicking the window’s close box, for example, and such changes do not go through this method; use on-superwindow-show or on-close to
monitor visibility changes.

If show? is #f, the window is hidden. Otherwise, the
window is shown.

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send a-window warp-pointer x y) → void? |
| x: position-integer?                    |
| y: position-integer?                    |
+------------------------------------------+
```

Moves the cursor to the given location in the window’s local coordinates.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-window wheel-event-mode)              |
| → (or/c 'one 'integer 'fraction)              |
| (send a-window wheel-event-mode mode) → void? |
| mode: (or/c 'one 'integer 'fraction)         |
+-----------------------------------------------+
```

Gets or sets the mode for mouse-wheel events in the window. Wheel
events are represented as key-event% instances where
get-key-code in key-event% returns 'wheel-up,
'wheel-down, 'wheel-right, or 'wheel-left.
A Window’s wheel-event mode determines the handling of variable
wheel-sized events reported the underlying platform. Specifically, the
wheel-event mode determines the possible values of get-wheel-steps in key-event% for a system-generated event for the window:

- 'one — wheel events are always reported for a single
step, where the window accumulates increments until it reaches
a full step, and where it generates separate events for
multi-step accumulations.
- 'integer — wheel events are always reported as
integer-sized steps, where fractional steps are accumulated and
preserved as needed to reach integer increments.
- 'fraction — wheel events are reported as positive
real values immediately as received from the underlying
platform.

The default wheel-event mode is 'one, except that
editor-canvas% initializes the wheel-event mode to
'integer.

Added in version 1.43 of package `gui-lib`.
