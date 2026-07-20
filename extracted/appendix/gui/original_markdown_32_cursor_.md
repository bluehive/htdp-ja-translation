<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/cursor_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/cursor_.html -->
<!-- Canonical English source for Japanese translation -->

```
+-----------------------+
| classcursor%: class? |
+-----------------------+
| superclass: object%   |
+-----------------------+
```

A cursor is a small icon that indicates the location of the mouse
pointer. The bitmap image typically indicates the current mode or
meaning of a mouse click at its current location.

A cursor is assigned to each window (or the window may use its
parent’s cursor; see set-cursor for more
information), and the pointer image is changed to match the window’s
cursor when the pointer is moved over the window. Each cursor object
may be assigned to many windows.

```
+-------------------------------------------------------------------------+
| [constructor]                                                           |
|                                                                         |
| (make-object cursor%                                                    |
| image: (is-a?/c bitmap%)                                               |
| mask: (is-a?/c bitmap%)                                                |
| hot-spot-x: (integer-in 0 15) = 0                                      |
| hot-spot-y: (integer-in 0 15) = 0                                      |
| (make-object cursor% id) → (is-a?/c cursor%)                            |
| id: (or/c 'arrow 'bullseye 'cross 'hand 'ibeam 'watch 'blank 'size-n/s |
| 'size-e/w 'size-ne/sw 'size-nw/se)                                      |
| (or/c 'arrow 'bullseye 'cross 'hand 'ibeam 'watch 'blank                |
| 'size-n/s 'size-e/w 'size-ne/sw 'size-nw/se)                            |
|                                                                         |
| ```racket                                                               |
| (or/c 'arrow 'bullseye 'cross 'hand 'ibeam 'watch 'blank                |
|       'size-n/s 'size-e/w 'size-ne/sw 'size-nw/se)                      |
| ```                                                                     |
+-------------------------------------------------------------------------+
```

The first case creates a cursor using an image bitmap and a mask
bitmap. Both bitmaps must have depth 1 and size 16 by 16
pixels. The hot-spot-x and hot-spot-y arguments
determine the focus point of the cursor within the cursor image,
relative to its top-left corner.

The second case creates a cursor using a stock cursor, specified
as one of the following:

- 'arrow — the default cursor
- 'bullseye — concentric circles
- 'cross — a crosshair
- 'hand — an open hand
- 'ibeam — a vertical line, indicating that clicks
control a text-selection caret
- 'watch — a watch or hourglass, indicating that
the user must wait for a computation to complete
- 'arrow+watch — the default cursor with a watch or
hourglass, indicating that some computation is in progress, but the
cursor can still be used
- 'blank — invisible
- 'size-e/w — arrows left and right
- 'size-n/s — arrows up and down
- 'size-ne/sw — arrows up-right and down-left
- 'size-nw/se — arrows up-left and down-right

If the cursor is created successfully, ok?
returns #t, otherwise the cursor object cannot be
assigned to a window.

```
+--------------------------------+
| [method]                       |
|                                |
| (send a-cursor ok?) → boolean? |
+--------------------------------+
```

Returns #t if the cursor is can be assigned to a window,
#f otherwise.
