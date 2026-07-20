<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/canvas_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/canvas_.html -->
<!-- Canonical English source for Japanese translation -->

```
+-----------------------+-----------+
| classcanvas%: class? |           |
+-----------------------+-----------+
| superclass: object%   |           |
| extends:              | canvas<%> |
+-----------------------+-----------+
```

A canvas% object is a general-purpose window for drawing and
handling events. See canvas<%> for information about drawing
onto a canvas.

```
+-----------------------------------------------------------------------------+
| [constructor]                                                               |
|                                                                             |
| (new canvas%                                                                |
| → (is-a?/c canvas%)                                                         |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c |
| pane%))                                                                     |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                    |
| (is-a?/c panel%) (is-a?/c pane%))                                           |
| style: (listof (or/c 'border 'control-border 'combo 'vscroll 'hscroll      |
| 'resize-corner 'gl 'no-autoclear 'transparent 'no-focus 'deleted)) = null   |
| (listof (or/c 'border 'control-border 'combo                                |
| 'vscroll 'hscroll 'resize-corner                                            |
| 'gl 'no-autoclear 'transparent                                              |
| 'no-focus 'deleted))                                                        |
| paint-callback: ((is-a?/c canvas%) (is-a?/c dc<%>). ->. any) = void      |
| label: (or/c label-string? #f) = #f                                        |
| gl-config: (or/c (is-a?/c gl-config%) #f) = #f                             |
| enabled: any/c = #t                                                        |
| vert-margin: spacing-integer? = 0                                          |
| horiz-margin: spacing-integer? = 0                                         |
| min-width: (or/c dimension-integer? #f) = #f                               |
| min-height: (or/c dimension-integer? #f) = #f                              |
| stretchable-width: any/c = #t                                              |
| stretchable-height: any/c = #t                                             |
|                                                                             |
| ```racket                                                                   |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                    |
|       (is-a?/c panel%) (is-a?/c pane%))                                     |
| ```                                                                         |
|                                                                             |
| ```racket                                                                   |
| (listof (or/c 'border 'control-border 'combo                                |
|               'vscroll 'hscroll 'resize-corner                              |
|               'gl 'no-autoclear 'transparent                                |
|               'no-focus 'deleted))                                          |
| ```                                                                         |
+-----------------------------------------------------------------------------+
```

The style argument indicates one or more of the following styles:

- 'border — gives the canvas a thin border
- 'control-border — gives the canvas a border that is
like a text-field% control
- 'combo — gives the canvas a combo button that is like
a combo-field% control; this style is intended for use
with 'control-border and not with 'hscroll or
'vscroll
- 'hscroll — enables horizontal scrolling (initially visible but inactive)
- 'vscroll — enables vertical scrolling (initially visible but inactive)
- 'resize-corner — leaves room for a resize control at the canvas’s
bottom right when only one scrollbar is visible
- 'gl — creates a canvas for OpenGL drawing instead of
normal dc<%> drawing; call the get-gl-context method on the result of get-dc; this style is usually combined with
'no-autoclear
- 'no-autoclear — prevents automatic erasing of the
canvas by the windowing system; see canvas<%> for
information on canvas refresh
- 'transparent — the canvas is “erased” by the
windowing system by letting its parent show through; see
canvas<%> for information on window refresh and on the
interaction of 'transparent and offscreen buffering; the
result is undefined if this flag is combined with
'no-autoclear
- 'no-focus — prevents the canvas from accepting the
keyboard focus when the canvas is clicked or when the
focus method is called
- 'deleted — creates the canvas as initially hidden and without affecting
parent’s geometry; the canvas can be made active
later by calling parent’s add-child
method

The 'hscroll and 'vscroll styles create a
canvas with an initially inactive scrollbar. The scrollbars are
activated with either
init-manual-scrollbars or
init-auto-scrollbars, and they can be hidden and re-shown with
show-scrollbars.

The paint-callback argument is called by the default
on-paint method, using the canvas and the DC returned by
get-dc as the argument.

The label argument names the canvas for
get-label, but it is not displayed with the canvas.

The gl-config argument determines properties of an OpenGL
context for this canvas, as obtained through the canvas’s drawing
context. See also
get-dc and
get-gl-context in dc<%>.

For information about the enabled argument, see window<%>. For information about the horiz-margin and vert-margin
arguments, see subarea<%>. For information about the
min-width, min-height, stretchable-width, and
stretchable-height arguments, see area<%>.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-canvas get-gl-client-size)      |
| → dimension-integer? dimension-integer? |
| dimension-integer?                      |
+-----------------------------------------+
```

Returns the canvas’s drawing-area dimensions in OpenGL units for a
canvas% instance with the 'gl style.

The result is the same as get-scaled-client-size
in a canvas without the 'gl style or on Windows and Unix. On
Mac OS, the result can be the same as get-client-size if the gl-config% specification provided on
creation does not specify high-resolution mode.

Added in version 1.16 of package `gui-lib`.

```
+---------------------------------------+
| [method]                              |
|                                       |
| (send a-canvas get-scroll-page which) |
| → positive-dimension-integer?         |
| which: (or/c 'horizontal 'vertical)  |
+---------------------------------------+
```

Get the current page step size of a manual scrollbar. The result is
0 if the scrollbar is not active or it is automatic.

The which argument is either 'horizontal or
'vertical, indicating whether to get the page step size of
the horizontal or vertical scrollbar, respectively.

See also
init-manual-scrollbars.

```
+-----------------------------------------------------------+
| [method]                                                  |
|                                                           |
| (send a-canvas get-scroll-pos which) → dimension-integer? |
| which: (or/c 'horizontal 'vertical)                      |
+-----------------------------------------------------------+
```

Gets the current value of a manual scrollbar. The result is always
0 if the scrollbar is not active or it is automatic.

The which argument is either 'horizontal or
'vertical, indicating that the value of the horizontal or
vertical scrollbar should be returned, respectively.

See also
init-manual-scrollbars.

```
+-------------------------------------------------------------+
| [method]                                                    |
|                                                             |
| (send a-canvas get-scroll-range which) → dimension-integer? |
| which: (or/c 'horizontal 'vertical)                        |
+-------------------------------------------------------------+
```

Gets the current maximum value of a manual scrollbar. The result is
always 0 if the scrollbar is not active or it is automatic.

The which argument is either 'horizontal or
'vertical, indicating whether to get the maximum value of the
horizontal or vertical scrollbar, respectively.

See also
init-manual-scrollbars.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-canvas get-view-start)          |
| → dimension-integer? dimension-integer? |
| dimension-integer?                      |
+-----------------------------------------+
```

Get the location at which the visible portion of the canvas
starts, based on the current values of the horizontal and
vertical scrollbars if they are initialized as automatic (see
init-auto-scrollbars). Combined with
get-client-size, an application can
efficiently redraw only the visible portion of the canvas. The
values are in pixels.

If the scrollbars are disabled or initialized as manual (see
init-manual-scrollbars), the result is (values00).

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-canvas get-virtual-size)                |
| → (value dimension-integer? dimension-integer?) |
+-------------------------------------------------+
```

Gets the size in device units of the scrollable canvas area (as
opposed to the client size, which is the area of the canvas currently
visible). This is the same size as the client size (as returned by
get-client-size) unless scrollbars are initialized as automatic (see
init-auto-scrollbars).

```
+------------------------------------------------------+
| [method]                                             |
|                                                      |
| (send a-canvas init-auto-scrollbars                  |
| horiz-pixels: (or/c positive-dimension-integer? #f) |
| vert-pixels: (or/c positive-dimension-integer? #f)  |
| h-value: (real-in 0.0 1.0)                          |
| v-value: (real-in 0.0 1.0)                          |
+------------------------------------------------------+
```

Enables and initializes automatic scrollbars for the canvas. A
horizontal or vertical scrollbar can be activated only in a canvas
that was created with the 'hscroll or
'vscroll style flag, respectively.

With automatic scrollbars, the programmer specifies the desired
virtual size of the canvas, and the scrollbars are automatically
handled to allow the user to scroll around the virtual area. The
scrollbars are not automatically hidden if they are unneeded; see
show-scrollbars.

The coordinates for mouse
events (passed to on-event) are not adjusted to
account for the position of the scrollbar;
use the get-view-start method to find suitable
offsets.

See also
init-manual-scrollbars for information about manual scrollbars. The horizontal and vertical
scrollbars are always either both manual or both automatic, but they
are independently enabled. Automatic scrollbars can be
re-initialized as manual, and vice versa.

If either horiz-pixels or vert-pixels is
#f, the scrollbar is not enabled in the corresponding
direction, and the canvas’s virtual size in that direction is the
same as its client size.

The h-value and v-value arguments specify the initial
values of the scrollbars as a fraction of the scrollbar’s range. A
0.0 value initializes the scrollbar to its left/top, while a
1.0 value initializes the scrollbar to its right/bottom.

It is possible to adjust the virtual sizes by calling this function again.

See also
on-scroll and
get-virtual-size.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-canvas init-manual-scrollbars   |
| h-length: (or/c dimension-integer? #f) |
| v-length: (or/c dimension-integer? #f) |
| h-page: positive-dimension-integer?    |
| v-page: positive-dimension-integer?    |
| h-value: dimension-integer?            |
| v-value: dimension-integer?            |
+-----------------------------------------+
```

Enables and initializes manual scrollbars for the canvas. A
horizontal or vertical scrollbar can be activated only in a canvas
that was created with the 'hscroll or
'vscroll style flag, respectively.

With manual scrollbars, the programmer is responsible for managing all
details of the scrollbars, and the scrollbar state has no effect on
the canvas’s virtual size. Instead, the canvas’s virtual size is the
same as its client size.

See also
init-auto-scrollbars for information about automatic scrollbars. The horizontal and vertical
scrollbars are always either both manual or both automatic, but they
are independently enabled. Automatic scrollbars can be re-initialized
as manual, and vice versa.

The h-length and v-length arguments specify the length of
each scrollbar in scroll steps (i.e., the maximum value of each
scrollbar). If either is #f, the scrollbar is disabled in the
corresponding direction.

The h-page and v-page arguments set the number of
scrollbar steps in a page, i.e., the amount moved when pressing above
or below the value indicator in the scrollbar control.

The h-value and v-value arguments specify the initial
values of the scrollbars.

If h-value is greater than h-length or v-value is
greater than v-length, an exn:fail:contract exception is raised. (The page step may be
larger than the total size of a scrollbar.)

See also
on-scroll and
get-virtual-size.

```
+--------------------------------------------------------------+
| [method]                                                     |
|                                                              |
| (send a-canvas make-bitmap width height) → (is-a/c? bitmap%) |
| width: exact-positive-integer?                              |
| height: exact-positive-integer?                             |
+--------------------------------------------------------------+
```

Creates a bitmap that draws in a way that is the same as drawing to the
canvas. See also make-screen-bitmap
and Portability and Bitmap Variants.

```
+----------------------------------+
| [method]                         |
|                                  |
| (send a-canvas on-paint) → void? |
+----------------------------------+
```

Overrides on-paint in canvas<%>.

Calls the procedure supplied as the paint-callback argument when
the canvas% was created.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-canvas on-scroll event) → void? |
| event: (is-a?/c scroll-event%)         |
+-----------------------------------------+
```

Called when the user changes one of the canvas’s scrollbars. A
scroll-event% argument provides information about the
scroll action.

This method is called only when manual
scrollbars are changed (see init-manual-scrollbars),
not automatic scrollbars; for automatic scrollbars,
the
on-paint method is called, instead.

```
+-------------------------------------------------------------------------+
| [method]                                                                |
|                                                                         |
| (send a-canvas refresh-now                                              |
| paint-proc: ((is-a?/c dc<%>). ->. any) = (lambda (dc) (send a-canvas |
| on-paint))                                                              |
| flush?: any/c = #t                                                     |
+-------------------------------------------------------------------------+
```

Calls paint-proc with the canvas’s drawing context to immediately
update the canvas (in contrast to refresh, which merely
queues an update request to be handled at the windowing system’s discretion).

Before paint-proc is called, flushing is disabled for the
canvas. Also, the canvas is erased, unless the canvas has the
'no-autoclear style. After paint-proc returns,
flushing is enabled, and if flush? is true, then
flush is called immediately.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-canvas scroll h-value v-value) → void? |
| h-value: (or/c (real-in 0.0 1.0) #f)          |
| v-value: (or/c (real-in 0.0 1.0) #f)          |
+------------------------------------------------+
```

Sets the values of automatic scrollbars. (This method has no effect on
manual scrollbars.)

If either argument is #f, the scrollbar value is not changed in
the corresponding direction.

The h-value and v-value arguments each specify a fraction
of the scrollbar’s movement. A 0.0 value sets the scrollbar to
its left/top, while a 1.0 value sets the scrollbar to its
right/bottom. A 0.5 value sets the scrollbar to its middle. In
general, if the canvas’s virtual size is v, its client size is
c, and (>vc), then scrolling to p
sets the view start to (floor(*p(-vc))).

See also
init-auto-scrollbars and
get-view-start.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-canvas set-scroll-page which value) → void? |
| which: (or/c 'horizontal 'vertical)                |
| value: positive-dimension-integer?                 |
+-----------------------------------------------------+
```

Set the current page step size of a manual scrollbar. (This method has
no effect on automatic scrollbars.)

The which argument is either 'horizontal or
'vertical, indicating whether to set the page step size of
the horizontal or vertical scrollbar, respectively.

See also
init-manual-scrollbars.

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-canvas set-scroll-pos which value) → void? |
| which: (or/c 'horizontal 'vertical)               |
| value: dimension-integer?                         |
+----------------------------------------------------+
```

Sets the current value of a manual scrollbar. (This method has no
effect on automatic scrollbars.)

The which argument is either 'horizontal or
'vertical, indicating whether to set the value of the
horizontal or vertical scrollbar set, respectively.

The value of the canvas’s scrollbar can be changed
by the user scrolling, and such changes do not go through this method; use on-scroll to
monitor scrollbar value changes.

See also
init-manual-scrollbars and
scroll.

```
+--------------------------------------+
| [method]                             |
|                                      |
| (send a-canvas set-scroll-range      |
| which: (or/c 'horizontal 'vertical) |
| value: dimension-integer?           |
+--------------------------------------+
```

Sets the current maximum value of a manual scrollbar. (This method has
no effect on automatic scrollbars.)

The which argument is either 'horizontal or
'vertical, indicating whether to set the maximum value of the
horizontal or vertical scrollbar, respectively.

See also
init-manual-scrollbars.

```
+--------------------------------+
| [method]                       |
|                                |
| (send a-canvas show-scrollbars |
| show-horiz?: any/c            |
| show-vert?: any/c             |
+--------------------------------+
```

Shows or hides the scrollbars as indicated by
show-horiz? and show-vert?. If
show-horiz? is true and the canvas was not created with
the 'hscroll style, an exn:fail:contract exception is raised. Similarly, if
show-vert? is true and the canvas was not created with
the 'vscroll style, an exn:fail:contract exception is raised.

The horizontal scrollbar can be shown only if the canvas was
created with the 'hscroll style, and the vertical
scrollbar can be shown only if the canvas was created with the
'vscroll style. See also init-auto-scrollbars and init-manual-scrollbars.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-canvas swap-gl-buffers) → void? |
+-----------------------------------------+
```

Calls
swap-buffers
on the result of
get-gl-context
for this canvas’s DC as returned by
get-dc.

The
swap-buffers in gl-context<%>
method acquires a re-entrant lock, so nested calls to
swap-gl-buffers or with-gl-context
on different threads or OpenGL contexts can block or deadlock.

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send a-canvas with-gl-context             |
| thunk: (-> any)                           |
| fail: (-> any) = (lambda () (error....)) |
+--------------------------------------------+
```

Passes the given thunk to
call-as-current
of the result of
get-gl-context
for this canvas’s DC as returned by
get-dc. If get-gl-context
returns #f, then fail is called,
instead.

The
call-as-current in gl-context<%>
method acquires a re-entrant lock, so nested calls to
with-gl-context or swap-gl-buffers
on different threads or OpenGL contexts can block or deadlock.
