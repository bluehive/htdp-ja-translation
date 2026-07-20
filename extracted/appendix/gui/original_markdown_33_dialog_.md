<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/dialog_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/dialog_.html -->
<!-- Canonical English source for Japanese translation -->

```
+-----------------------+---------------------+
| classdialog%: class? |                     |
+-----------------------+---------------------+
| superclass: object%   |                     |
| extends:              | top-level-window<%> |
+-----------------------+---------------------+
```

A dialog is a top-level window that is modal: while the
dialog is shown, key and mouse press/release events are disabled for
all other top-level windows in the dialog’s eventspace.

```
+--------------------------------------------------------------------------------+
| [constructor]                                                                  |
|                                                                                |
| (new dialog%                                                                   |
| → (is-a?/c dialog%)                                                            |
| label: label-string?                                                          |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f                     |
| width: (or/c dimension-integer? #f) = #f                                      |
| height: (or/c dimension-integer? #f) = #f                                     |
| x: (or/c dimension-integer? #f) = #f                                          |
| y: (or/c dimension-integer? #f) = #f                                          |
| style: (listof (or/c 'no-caption 'resize-border 'no-sheet 'close-button)) =   |
| null                                                                           |
| (listof (or/c 'no-caption 'resize-border                                       |
| 'no-sheet 'close-button))                                                      |
| enabled: any/c = #t                                                           |
| border: spacing-integer? = 0                                                  |
| spacing: spacing-integer? = 0                                                 |
| alignment: (list/c (or/c 'left 'center 'right) (or/c 'top 'center 'bottom)) = |
| '(center top)                                                                  |
| (list/c (or/c 'left 'center 'right)                                            |
| (or/c 'top 'center 'bottom))                                                   |
| min-width: (or/c dimension-integer? #f) = #f                                  |
| min-height: (or/c dimension-integer? #f) = #f                                 |
| stretchable-width: any/c = #t                                                 |
| stretchable-height: any/c = #t                                                |
|                                                                                |
| ```racket                                                                      |
| (listof (or/c 'no-caption 'resize-border                                       |
|               'no-sheet 'close-button))                                        |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (list/c (or/c 'left 'center 'right)                                            |
|         (or/c 'top 'center 'bottom))                                           |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

The label string is used as the dialog’s title in its
title bar. If the dialog’s label is changed (see
set-label), the title bar is updated.

The parent argument can be #f or an existing
frame or dialog. On Windows, if parent is not #f, the
new dialog is always on top of its parent. On Windows and Unix, a
dialog is iconized when its parent is iconized.

If parent is #f, then the eventspace for the new
dialog is the current eventspace, as determined by
current-eventspace. Otherwise, parent’s eventspace
is the new dialog’s eventspace.

If the width or height argument is not #f,
it specifies an initial size for the dialog (in pixels) assuming that
it is larger than the minimum size, otherwise the minimum size is
used. On Windows and Mac OS (and with some Unix window managers)
dialogs are not resizeable.

If the x or y argument is not #f, it
specifies an initial location for the dialog. Otherwise, if no
location is set before the dialog is shown, it is centered (with
respect parent if not #f, the screen otherwise).

The style flags adjust the appearance of the dialog on some
platforms:

- 'no-caption — omits the title bar for the dialog
(Windows)
- 'resize-border — adds a resizeable border around the
window (Windows), ability to resize the window (Mac OS), or grow
box in the bottom right corner (older Mac OS)
- 'no-sheet — uses a movable window for the dialog,
even if a parent window is provided (Mac OS)
- 'close-button — include a close button in the
dialog’s title bar, which would not normally be included (Mac OS)

Even if the dialog is not shown, a few notification events may be
queued for the dialog on creation. Consequently, the new dialog’s
resources (e.g., memory) cannot be reclaimed until some events are
handled, or the dialog’s eventspace is shut down.

For information about the enabled argument, see window<%>. For information about the border, spacing, and alignment
arguments, see area-container<%>. For information about the
min-width, min-height, stretchable-width, and
stretchable-height arguments, see area<%>.

```
+----------------------------------+
| [method]                         |
|                                  |
| (send a-dialog on-subwindow-char |
| receiver: (is-a?/c window<%>)   |
| event: (is-a?/c key-event%)     |
+----------------------------------+
```

Overrides on-subwindow-char in window<%>.

Returns the result of

```racket
(or (send this on-system-menu-char event)
    (send this on-traverse-char event))
```

```
+------------------------------------+
| [method]                           |
|                                    |
| (send a-dialog show show?) → void? |
| show?: any/c                      |
+------------------------------------+
```

Overrides show in top-level-window<%>.

If show? is true, the dialog is shown and all frames (and other
dialogs) in the eventspace become disabled until the dialog is
closed. Furthermore, the method does not immediately return. Instead,
it loops with yield until the dialog is found to be hidden
between calls to yield. An internal semaphore is used with
yield to avoid a busy-wait, and to ensure that the show
method returns as soon as possible after the dialog is hidden.

If show? is false, the dialog is hidden and other
frames and dialogs are re-enabled (unless a different, pre-existing
dialog is still shown).

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send a-dialog show-without-yield) → void? |
+--------------------------------------------+
```

Like (senda-dialogshow#t), but returns
immediately instead of yielding.
