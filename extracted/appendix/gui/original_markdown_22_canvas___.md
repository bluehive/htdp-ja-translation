<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/canvas___.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/canvas___.html -->
<!-- Canonical English source for Japanese translation -->

```
+---------------------------------+--------------+
| interfacecanvas<%>: interface? |              |
+---------------------------------+--------------+
| implements:                     | subwindow<%> |
+---------------------------------+--------------+
```

A canvas is a subwindow onto which graphics and text can be drawn. Canvases also
receive mouse and keyboard events.

The canvas<%> interface is implemented by two classes:

- canvas% — a canvas for arbitrary drawing and
event handling; and
- editor-canvas% — a canvas for displaying
editor<%> objects.

To draw onto a canvas, get its device context via get-dc. There are two basic approaches to updating a canvas:

- Drawing normally occurs during the canvas’s on-paint callback. The canvas% class supports a
paint-callback initialization argument to be called
from the default on-paint method.A canvas’s on-paint method is called
automatically as an event when the windowing system determines
that the canvas must be updated, such as when the canvas is
first shown or when it is resized. Use the refresh method to explicitly trigger an on-paint call from the windowing system. (Multiple refresh
requests before on-paint can be called are
coaleced into a single on-paint call.)Before the windowing system calls on-paint,
it may erase the canvas’s background (see erase), depending on the style of the canvas (e.g., as
determined by the style initialization argument for
canvas%). Even when the canvas’s style suppresses
explicit clearing of the canvas, a canvas may be erased by the
windowing system due to window-moving and -resizing
operations. For a transparent canvas, “erased” means that the
canvas’s parent window shows through.
- Drawing can also occur at any time outside an on-paint call from the windowing system, including from
threads other than the handler thread of the canvas’s
eventspace. Drawing outside an on-paint
callback from the system is transient in the sense that
windowing activity can erase the canvas, but the drawing is
persistent as long as no windowing refresh is needed.Calling an on-paint method directly is the
same as drawing outside an on-paint callback
from the windowing system. For a canvas%, use
refresh-now to force an immediate update of
the canvas’s content that is otherwise analogous to queueing an
update with refresh.

Drawing to a canvas’s drawing context actually renders into an
offscreen buffer. The buffer is automatically flushed to the screen
asynchronously, explicitly via the flush method, or
explicitly via flush-display—unless flushing has been
disabled for the canvas. The suspend-flush method
suspends flushing for a canvas until a matching resume-flush calls; calls to suspend-flush and
resume-flush can be nested, in which case flushing
is suspended until the outermost suspend-flush is
balanced by a resume-flush. An on-paint call from the windowing system is implicitly wrapped with
suspend-flush and resume-flush
calls, as is a call to a paint procedure by refresh-now.

In the case of a transparent canvas, line and text smoothing can
depend on the window that serves as the canvas’s background. For
example, smoothing may color pixels differently depending on whether
the target context is white or gray. Background-sensitive smoothing
is supported only if a relatively small number of drawing commands are
recorded in the canvas’s offscreen buffer, however.

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-canvas accept-tab-focus) → boolean?  |
| (send a-canvas accept-tab-focus on?) → void? |
| on?: any/c                                  |
+----------------------------------------------+
```

Gets or sets whether
tab-focus is enabled for the canvas (assuming that the canvas is
not created with the 'no-focus style for canvas%). When tab-focus is
enabled, the canvas can receive the keyboard focus when the user
navigates among a frame or dialog’s controls with the Tab and
arrow keys. By default, tab-focus is disabled.

When tab-focus is enabled for a canvas% object, Tab, arrow,
Enter, and Escape keyboard events are consumed by a frame’s default
on-traverse-char method. (In addition, a
dialog’s default method consumes Escape key events.) Otherwise,
on-traverse-char allows the keyboard
events to be propagated to the canvas.

For an editor-canvas% object, handling of Tab, arrow, Enter,
and Escape keyboard events is determined by the
allow-tab-exit method.

```
+-------------------------------+
| [method]                      |
|                               |
| (send a-canvas flush) → void? |
+-------------------------------+
```

Like flush-display, but constrained if possible to the canvas.

```
+---------------------------------------+
| [method]                              |
|                                       |
| (send a-canvas get-canvas-background) |
| → (or/c (is-a?/c color%) #f)          |
+---------------------------------------+
```

Returns the color currently used to “erase” the canvas content before
on-paint is called. See also
set-canvas-background.

The result is #f if the canvas was created with the
'transparent style, otherwise it is always a
color% object.

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send a-canvas get-dc) → (is-a?/c dc<%>) |
+------------------------------------------+
```

Gets the canvas’s device context. See dc<%> for more information about
drawing.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-canvas get-scaled-client-size)  |
| → dimension-integer? dimension-integer? |
| dimension-integer?                      |
+-----------------------------------------+
```

Returns the canvas’s drawing-area dimensions in unscaled pixels—that
is, without scaling (see Screen Resolution and Text Scaling) that is
implicitly applied to the canvas size and content.

For example, when a canvas on Mac OS resides on a Retina display, it
has a backing scale of 2, and so the results from
get-scaled-client-size will be twice as large as results from
get-client-size. If the same canvas’s frame is dragged to a
non-Retina screen, its backing scale can change to 1, in
which case get-scaled-client-size and
get-client-size will produce the same value. Whether
a canvas’s backing scale can change depends on the platform.

The size reported by get-scaled-client-size may match
a viewport size for OpenGL drawing in canvas% instance with
the 'gl style. On Mac OS, however, the viewport will match
the scaled size unless the canvas is created with a
gl-config% specification that is adjusted to high-resolution
mode via set-hires-mode. See also
get-gl-client-size in canvas%.

Added in version 1.13 of package `gui-lib`.

```
+--------------------------------------------------------+
| [method]                                               |
|                                                        |
| (send a-canvas min-client-height) → dimension-integer? |
| (send a-canvas min-client-height h) → void?            |
| h: dimension-integer?                                 |
+--------------------------------------------------------+
```

Gets or sets the canvas’s minimum height for geometry management,
based on the client size rather than the full size. The client height
is obtained or changed via
min-height in area<%>, adding or subtracting border and scrollbar sizes as appropriate.

The minimum height is ignored when it is smaller than the canvas’s
graphical minimum height. See Geometry Management for
more information.

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-canvas min-client-width) → dimension-integer? |
| (send a-canvas min-client-width w) → void?            |
| w: dimension-integer?                                |
+-------------------------------------------------------+
```

Gets or sets the canvas’s minimum width for geometry management, based
on the canvas’s client size rather than its full size. The client
width is obtained or changed via
min-width in area<%>, adding or subtracting border and scrollbar sizes as appropriate.

The minimum width is ignored when it is smaller than the canvas’s
graphical minimum width. See Geometry Management for
more information.

```
+------------------------------------+
| [method]                           |
|                                    |
| (send a-canvas on-char ch) → void? |
| ch: (is-a?/c key-event%)          |
+------------------------------------+
```

Specification:
Called when the canvas receives a keyboard event. See also
Mouse and Keyboard Events.

Default implementation:
Does nothing.

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-canvas on-event event) → void? |
| event: (is-a?/c mouse-event%)         |
+----------------------------------------+
```

Specification:
Called when the canvas receives a mouse event. See also
Mouse and Keyboard Events, noting in particular that certain mouse events
can get dropped.

Default implementation:
Does nothing.

```
+----------------------------------+
| [method]                         |
|                                  |
| (send a-canvas on-paint) → void? |
+----------------------------------+
```

Specification:
Called when the canvas is exposed or resized so that the image in the
canvas can be repainted.

When
on-paint is called in response to a system expose event and only a portion of
the canvas is newly exposed, any drawing operations performed by
on-paint are clipped to the newly-exposed region; however, the clipping region
as reported by
get-clipping-region does not change.

Default implementation:
Does nothing.

```
+-----------------------------------+
| [method]                          |
|                                   |
| (send a-canvas on-tab-in) → void? |
+-----------------------------------+
```

Specification:
Called when the keyboard focus enters the canvas via keyboard
navigation events. The
on-focus method is also called, as usual for a focus change. When the keyboard
focus leaves a canvas due to a navigation event, only
on-focus is called.

See also
accept-tab-focus and
on-traverse-char in top-level-window<%>.

Default implementation:
Does nothing.

```
+--------------------------------------+
| [method]                             |
|                                      |
| (send a-canvas resume-flush) → void? |
+--------------------------------------+
```

See canvas<%> for information on canvas flushing.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-canvas set-canvas-background color) → void? |
| color: (is-a?/c color%)                            |
+-----------------------------------------------------+
```

Sets the color used to “erase” the canvas content before
on-paint is called. (This color is typically associated with the canvas at a
low level, so that it is used even when a complete refresh of the
canvas is delayed by other activity.)

If the canvas was created with the 'transparent style,
an exn:fail:contract exception is raised.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-canvas set-resize-corner on?) → void? |
| on?: any/c                                   |
+-----------------------------------------------+
```

On Mac OS, enables or disables space for a resize tab at the
canvas’s lower-right corner when only one scrollbar is visible. This
method has no effect on Windows or Unix, and it has no effect when
both or no scrollbars are visible. The resize corner is disabled by
default, but it can be enabled when a canvas is created with the
'resize-corner style.

```
+---------------------------------------+
| [method]                              |
|                                       |
| (send a-canvas suspend-flush) → void? |
+---------------------------------------+
```

See canvas<%> for information on canvas flushing.

Beware that suspending flushing for a canvas can discourage refreshes
for other windows in the same frame on some platforms.
