<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/mouse-event_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/mouse-event_.html -->
<!-- Canonical English source for Japanese translation -->

```
+----------------------------+
| classmouse-event%: class? |
+----------------------------+
| superclass: event%         |
+----------------------------+
```

A mouse-event% object encapsulates a mouse event.
Mouse events are primarily processed by
on-subwindow-event in window<%> and
on-event in canvas<%>.

See also Mouse and Keyboard Events.

```
+------------------------------------------------------------------------------+
| [constructor]                                                                |
|                                                                              |
| (new mouse-event%                                                            |
| → (is-a?/c mouse-event%)                                                     |
| event-type: (or/c 'enter 'leave 'left-down 'left-up 'middle-down 'middle-up |
| 'right-down 'right-up 'motion)                                               |
| (or/c 'enter 'leave 'left-down 'left-up                                      |
| 'middle-down 'middle-up                                                      |
| 'right-down 'right-up 'motion)                                               |
| left-down: any/c = #f                                                       |
| middle-down: any/c = #f                                                     |
| right-down: any/c = #f                                                      |
| x: exact-integer? = 0                                                       |
| y: exact-integer? = 0                                                       |
| shift-down: any/c = #f                                                      |
| control-down: any/c = #f                                                    |
| meta-down: any/c = #f                                                       |
| alt-down: any/c = #f                                                        |
| time-stamp: exact-integer? = 0                                              |
| caps-down: any/c = #f                                                       |
| mod3-down: any/c = #f                                                       |
| mod4-down: any/c = #f                                                       |
| mod5-down: any/c = #f                                                       |
|                                                                              |
| ```racket                                                                    |
| (or/c 'enter 'leave 'left-down 'left-up                                      |
|       'middle-down 'middle-up                                                |
|       'right-down 'right-up 'motion)                                         |
| ```                                                                          |
+------------------------------------------------------------------------------+
```

Creates a mouse event for a particular type of event. The event types
are:

- 'enter — mouse pointer entered the window
- 'leave — mouse pointer left the window
- 'left-down — left mouse button pressed
- 'left-up — left mouse button released
- 'middle-down — middle mouse button pressed
- 'middle-up — middle mouse button released
- 'right-down — right mouse button pressed (Mac OS: click with control key pressed)
- 'right-up — right mouse button released (Mac OS: release with control key pressed)
- 'motion — mouse moved, with or without button(s) pressed

See the corresponding get- and set-
methods for information about left-down,
middle-down, right-down, x, y,
shift-down, control-down, meta-down,
alt-down, time-stamp, caps-down, mod3-down,
mod4-down, and mod5-down.

Changed in version 1.1 of package `gui-lib`: Added mod3-down, mod4-down, and mod5-down.

```
+----------------------------------------------------------+
| [method]                                                 |
|                                                          |
| (send a-mouse-event button-changed? [button]) → boolean? |
| button: (or/c 'left 'middle 'right 'any) = 'any         |
+----------------------------------------------------------+
```

Returns #t if this was a mouse button press or release event
(i.e., type 'left-down, 'left-up,
'middle-down, 'middle-up,
'right-down, or 'right-up),
#f otherwise. See also
button-up? and
button-down?.

If button is not 'any, then #t is only returned
if it is a press or release event for a specific button.

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-mouse-event button-down? [button]) → boolean? |
| button: (or/c 'left 'middle 'right 'any) = 'any      |
+-------------------------------------------------------+
```

Returns #t if the event is for a button press (i.e., type 'left-down,
'middle-down, or 'right-down), #f
otherwise.

If button is not 'any, then #t is only returned
if it is a press event for a specific button.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-mouse-event button-up? [button]) → boolean? |
| button: (or/c 'left 'middle 'right 'any) = 'any    |
+-----------------------------------------------------+
```

Returns #t if the event is for a button release (i.e., type 'left-up,
'middle-up, or 'right-up), #f
otherwise. (As noted in Mouse and Keyboard Events, button release events are
sometimes dropped.)

If button is not 'any, then #t is only returned
if it is a release event for a specific button.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-mouse-event dragging?) → boolean? |
+-------------------------------------------+
```

Returns #t if this was a dragging event: type 'motion while a button
is pressed (as reported by get-left-down,
get-middle-down, or
or get-right-down), #f otherwise.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-mouse-event entering?) → boolean? |
+-------------------------------------------+
```

Returns #t if this event is for the mouse entering a window
(i.e., type 'enter),
#f otherwise.

When the mouse button is up, an enter/leave event notifies a window
that it will start/stop receiving mouse events. When the mouse button
is down, however, the window receiving the mouse-down event receives
all mouse events until the button is released; enter/leave events are
not sent to other windows, and are not reliably delivered to the
click-handling window (since the window can detect movement out of
its region via get-x and get-y). See also Mouse and Keyboard Events.

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-mouse-event get-alt-down) → boolean? |
+----------------------------------------------+
```

Returns #t if the Option (Mac OS) key was down for the
event. When the Alt key is pressed in Windows, it is reported as a
Meta press (see get-meta-down).

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-mouse-event get-caps-down) → boolean? |
+-----------------------------------------------+
```

Returns #t if the Caps Lock key was on for the event.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-mouse-event get-control-down) → boolean? |
+--------------------------------------------------+
```

Returns #t if the Control key was down for the event.

On Mac OS, if a control-key press is combined with a mouse button
click, the event is reported as a right-button click and
get-control-down for the event reports
#f.

```
+-------------------------------------------------------------------------------+
| [method]                                                                      |
|                                                                               |
| (send a-mouse-event get-event-type)                                           |
| → (or/c 'enter 'leave 'left-down 'left-up 'middle-down 'middle-up 'right-down |
| 'right-up 'motion)                                                            |
| (or/c 'enter 'leave 'left-down 'left-up                                       |
| 'middle-down 'middle-up                                                       |
| 'right-down 'right-up 'motion)                                                |
|                                                                               |
| ```racket                                                                     |
| (or/c 'enter 'leave 'left-down 'left-up                                       |
|       'middle-down 'middle-up                                                 |
|       'right-down 'right-up 'motion)                                          |
| ```                                                                           |
+-------------------------------------------------------------------------------+
```

Returns the type of the event; see mouse-event% for
information about each event type. See also set-event-type.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-mouse-event get-left-down) → boolean? |
+-----------------------------------------------+
```

Returns #t if the left mouse button was down (but not pressed) during the event.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-mouse-event get-meta-down) → boolean? |
+-----------------------------------------------+
```

Returns #t if the Meta (Unix), Alt (Windows), or Command (Mac OS) key was down for the event.

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-mouse-event get-middle-down) → boolean? |
+-------------------------------------------------+
```

Returns #t if the middle mouse button was down (but not
pressed) for the event. On Mac OS, a middle-button click is
impossible.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-mouse-event get-mod3-down) → boolean? |
+-----------------------------------------------+
```

Returns #t if the Mod3 (Unix) key was down for the event.

Added in version 1.1 of package `gui-lib`.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-mouse-event get-mod4-down) → boolean? |
+-----------------------------------------------+
```

Returns #t if the Mod4 (Unix) key was down for the event.

Added in version 1.1 of package `gui-lib`.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-mouse-event get-mod5-down) → boolean? |
+-----------------------------------------------+
```

Returns #t if the Mod5 (Unix) key was down for the event.

Added in version 1.1 of package `gui-lib`.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-mouse-event get-right-down) → boolean? |
+------------------------------------------------+
```

Returns #t if the right mouse button was down (but not
pressed) for the event. On Mac OS, a control-click combination
is treated as a right-button click.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-mouse-event get-shift-down) → boolean? |
+------------------------------------------------+
```

Returns #t if the Shift key was down for the event.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-mouse-event get-x) → exact-integer? |
+---------------------------------------------+
```

Returns the x-position of the mouse at the time of the event, in the
target’s window’s (client-area) coordinate system.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-mouse-event get-y) → exact-integer? |
+---------------------------------------------+
```

Returns the y-position of the mouse at the time of the event in the
target’s window’s (client-area) coordinate system.

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send a-mouse-event leaving?) → boolean? |
+------------------------------------------+
```

Returns #t if this event is for the mouse leaving a window
(i.e., type 'leave),
#f otherwise.

See entering? for information about enter and
leave events while the mouse button is clicked.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-mouse-event moving?) → boolean? |
+-----------------------------------------+
```

Returns #t if this was a moving event (i.e., type 'motion),
#f otherwise.

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-mouse-event set-alt-down down?) → void? |
| down?: any/c                                   |
+-------------------------------------------------+
```

Sets whether the Option (Mac OS) key was down for the event. When
the Alt key is pressed in Windows, it is reported as a Meta press
(see set-meta-down).

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-mouse-event set-caps-down down?) → void? |
| down?: any/c                                    |
+--------------------------------------------------+
```

Sets whether the Caps Lock key was on for the event.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-mouse-event set-control-down down?) → void? |
| down?: any/c                                       |
+-----------------------------------------------------+
```

Sets whether the Control key was down for the event.

On Mac OS, if a control-key press is combined with a mouse button
click, the event is reported as a right-button click and
get-control-down for the event reports
#f.

```
+------------------------------------------------------------------------------+
| [method]                                                                     |
|                                                                              |
| (send a-mouse-event set-event-type event-type) → void?                       |
| event-type: (or/c 'enter 'leave 'left-down 'left-up 'middle-down 'middle-up |
| 'right-down 'right-up 'motion)                                               |
| (or/c 'enter 'leave 'left-down 'left-up                                      |
| 'middle-down 'middle-up                                                      |
| 'right-down 'right-up 'motion)                                               |
|                                                                              |
| ```racket                                                                    |
| (or/c 'enter 'leave 'left-down 'left-up                                      |
|       'middle-down 'middle-up                                                |
|       'right-down 'right-up 'motion)                                         |
| ```                                                                          |
+------------------------------------------------------------------------------+
```

Sets the type of the event; see mouse-event% for information
about each event type. See also get-event-type.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-mouse-event set-left-down down?) → void? |
| down?: any/c                                    |
+--------------------------------------------------+
```

Sets whether the left mouse button was down (but not pressed) during
the event.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-mouse-event set-meta-down down?) → void? |
| down?: any/c                                    |
+--------------------------------------------------+
```

Sets whether the Meta (Unix), Alt (Windows), or Command (Mac OS) key
was down for the event.

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-mouse-event set-middle-down down?) → void? |
| down?: any/c                                      |
+----------------------------------------------------+
```

Sets whether the middle mouse button was down (but not pressed) for
the event. On Mac OS, a middle-button click is impossible.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-mouse-event set-mod3-down down?) → void? |
| down?: any/c                                    |
+--------------------------------------------------+
```

Sets whether the Mod3 (Unix) key was down for the event.

Added in version 1.1 of package `gui-lib`.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-mouse-event set-mod4-down down?) → void? |
| down?: any/c                                    |
+--------------------------------------------------+
```

Sets whether the Mod4 (Unix) key was down for the event.

Added in version 1.1 of package `gui-lib`.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-mouse-event set-mod5-down down?) → void? |
| down?: any/c                                    |
+--------------------------------------------------+
```

Sets whether the Mod5 (Unix) key was down for the event.

Added in version 1.1 of package `gui-lib`.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send a-mouse-event set-right-down down?) → void? |
| down?: any/c                                     |
+---------------------------------------------------+
```

Sets whether the right mouse button was down (but not pressed) for the
event. On Mac OS, a control-click combination by the user is
treated as a right-button click.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send a-mouse-event set-shift-down down?) → void? |
| down?: any/c                                     |
+---------------------------------------------------+
```

Sets whether the Shift key was down for the event.

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-mouse-event set-x pos) → void? |
| pos: exact-integer?                   |
+----------------------------------------+
```

Sets the x-position of the mouse at the time of the event in the
target’s window’s (client-area) coordinate system.

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-mouse-event set-y pos) → void? |
| pos: exact-integer?                   |
+----------------------------------------+
```

Sets the y-position of the mouse at the time of the event in the
target’s window’s (client-area) coordinate system.
