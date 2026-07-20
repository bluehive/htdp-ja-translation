<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/frame_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/frame_.html -->
<!-- Canonical English source for Japanese translation -->

```
+----------------------+---------------------+
| classframe%: class? |                     |
+----------------------+---------------------+
| superclass: object%  |                     |
| extends:             | top-level-window<%> |
+----------------------+---------------------+
```

A frame is a top-level container window. It has a title bar (which
displays the frame’s label), an optional menu bar, and an optional
status line.

```
+--------------------------------------------------------------------------------+
| [constructor]                                                                  |
|                                                                                |
| (new frame%                                                                    |
| → (is-a?/c frame%)                                                             |
| label: label-string?                                                          |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog) #f) = #f                      |
| width: (or/c dimension-integer? #f) = #f                                      |
| height: (or/c dimension-integer? #f) = #f                                     |
| x: (or/c position-integer? #f) = #f                                           |
| y: (or/c position-integer? #f) = #f                                           |
| style: (listof (or/c 'no-resize-border 'no-caption 'no-system-menu            |
| 'hide-menu-bar 'toolbar-button 'float 'metal 'fullscreen-button                |
| 'fullscreen-aux)) = null                                                       |
| (listof (or/c 'no-resize-border 'no-caption                                    |
| 'no-system-menu 'hide-menu-bar                                                 |
| 'toolbar-button 'float 'metal                                                  |
| 'fullscreen-button 'fullscreen-aux))                                           |
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
| (listof (or/c 'no-resize-border 'no-caption                                    |
|               'no-system-menu 'hide-menu-bar                                   |
|               'toolbar-button 'float 'metal                                    |
|               'fullscreen-button 'fullscreen-aux))                             |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (list/c (or/c 'left 'center 'right)                                            |
|         (or/c 'top 'center 'bottom))                                           |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

The label string is displayed in the frame’s title
bar. If the frame’s label is changed (see set-label), the title bar is updated.

The parent argument can be #f or an existing
frame or dialog. On Windows, if parent is not #f,
the new frame is always on top of its parent.
On Windows and Unix (for many window managers), a
frame is iconized when its parent is iconized.

If parent is #f, then the eventspace for the
new frame is the current eventspace, as determined by
current-eventspace. Otherwise, parent’s
eventspace is the new frame’s eventspace.

If the width or height argument is not
#f, it specifies an initial size for the frame (in
pixels) assuming that it is larger than the minimum size,
otherwise the minimum size is used.

If the x or y argument is not #f, it
specifies an initial location for the frame. Otherwise, a
location is selected automatically (tiling frames and dialogs as
they are created).

The style flags adjust the appearance of the frame on
some platforms:

- 'no-resize-border — omits the resizeable border
around the window (Windows, Unix), ability to resize the window (Mac
OS), or grow box in the bottom right corner (older Mac OS)
- 'no-caption — omits the title bar for the frame
(Windows, Mac OS, Unix)
- 'no-system-menu — omits the system menu
(Windows)
- 'toolbar-button — includes a toolbar button on the
frame’s title bar (Mac OS 10.6 and earlier); a click on the toolbar button triggers
a call to on-toolbar-button-click
- 'hide-menu-bar — hides the menu bar and dock when
the frame is active (Mac OS) or asks the window manager to make
the frame fullscreen (Unix)
- 'float — causes the frame to stay in front of all
other non-floating windows (Windows, Mac OS, Unix); on Mac OS, a floating frame
shares the focus with an active non-floating frame; when this style
is combined with 'no-caption, then showing the frame does
not cause the keyboard focus to shift to the window, and on Unix,
clicking the frame does not move the focus; on Windows, a floating
frame has no taskbar button
- 'metal — ignored (formerly supported for Mac OS)
- 'fullscreen-button — includes a button on the
frame’s title bar to put the frame in fullscreen mode (Mac OS 10.7 and later)
- 'fullscreen-aux — allows the frame to accompany
another that is in fullscreen mode (Mac OS 10.7 and later)

Even if the frame is not shown, a few notification events may be
queued for the frame on creation. Consequently, the new frame’s
resources (e.g., memory) cannot be reclaimed until some events are
handled, or the frame’s eventspace is shut down.

For information about the enabled argument, see window<%>. For information about the border, spacing, and alignment
arguments, see area-container<%>. For information about the
min-width, min-height, stretchable-width, and
stretchable-height arguments, see area<%>.

Changed in version 1.1 of package `gui-lib`: Added 'fullscreen-button
and 'fullscreen-aux options
for style.
Changed in version 1.66: Allow a dialog% instance
as parent.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-frame create-status-line) → void? |
+-------------------------------------------+
```

Creates a status line at the bottom of the frame. The width of the
status line is the whole width of the frame (adjusted automatically
when resizing), and the height and text size are platform-specific.

See also set-status-text.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-frame fullscreen fullscreen?) → void? |
| fullscreen?: any/c                           |
+-----------------------------------------------+
```

Puts the frame in fullscreen mode or restores the frame to
non-fullscreen mode. The frame’s show state is not affected.

A frame’s mode can be changed
by the user, and such changes do not go through this method. A program
cannot detect when a
frame has been put in fullscreen mode except by polling is-fullscreened?.

On Mac OS, the frame% must be created with the style
'fullscreen-button for fullscreen mode to work, and Mac OS
10.7 or later is required.

Added in version 1.9 of package `gui-lib`.
Changed in version 1.18: Changed fullscreen with #t
to not imply show on Windows and Mac OS.

```
+-------------------------------------------------------------+
| [method]                                                    |
|                                                             |
| (send a-frame get-menu-bar) → (or/c (is-a?/c menu-bar%) #f) |
+-------------------------------------------------------------+
```

Returns the frame’s menu bar, or #f if none has been created
for the frame.

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send a-frame has-status-line?) → boolean? |
+--------------------------------------------+
```

Returns #t if the frame’s status line has been created,
#f otherwise. See also create-status-line.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-frame iconize iconize?) → void? |
| iconize?: any/c                        |
+-----------------------------------------+
```

Iconizes (minimizes) or deiconizes (restores) the
frame. Deiconizing brings the frame to the front.

A frame’s iconization can be changed
by the user, and such changes do not go through this method. A program
cannot detect when a
frame has been iconized except by polling is-iconized?.

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send a-frame is-fullscreened?) → boolean? |
+--------------------------------------------+
```

Returns #t if the frame is in fullscreen mode, #f
otherwise.

Added in version 6.0.0.6 of package `gui-lib`.

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-frame is-iconized?) → boolean? |
+----------------------------------------+
```

Returns #t if the frame is iconized (minimized), #f
otherwise.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-frame is-maximized?) → boolean? |
+-----------------------------------------+
```

On Windows and Mac OS, returns #t if the frame is
maximized, #f otherwise. On Unix, the result is always
#f.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-frame maximize maximize?) → void? |
| maximize?: any/c                         |
+-------------------------------------------+
```

Specification:
Maximizes or restores the frame on Windows and Mac OS; the
frame’s show state is not affected. On Windows, an iconized frame
cannot be maximized or restored.

A window’s maximization can be changed
by the user, and such changes do not go through this method; use on-size to
monitor size changes.

Default implementation:
If maximize? is #f, the window is restored, otherwise
it is maximized.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-frame modified) → boolean?        |
| (send a-frame modified modified?) → void? |
| modified?: any/c                         |
+-------------------------------------------+
```

Gets or sets the frame’s modification state as reflected to the user.
On Mac OS, the modification state is reflected as a dot in the
frame’s close button. On Windows and Unix, the modification state is
reflected by an asterisk at the end of the frame’s displayed title.

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-frame on-menu-char event) → boolean? |
| event: (is-a?/c key-event%)                 |
+----------------------------------------------+
```

If the frame has a menu bar with keyboard shortcuts, and if the key
event includes a Control, Alt, Option, Meta, Command, Shift, or
Function key, then on-menu-char attempts to match the
given event to a menu item. If a match is found, #t is
returned, otherwise #f is returned.

When the match corresponds to a complete shortcut combination, the
menu item’s callback is called (before
on-menu-char returns).

If the event does not correspond to a complete shortcut combination,
the event may be handled anyway if it corresponds to a mnemonic in the
menu bar (i.e., an underlined letter in a menu’s title, which is
installed by including an ampersand in the menu’s label). If a
mnemonic match is found, the keyboard focus is moved to the menu bar
(selecting the menu with the mnemonic), and #t is returned.

```
+---------------------------------+
| [method]                        |
|                                 |
| (send a-frame on-subwindow-char |
| receiver: (is-a?/c window<%>)  |
| event: (is-a?/c key-event%)    |
+---------------------------------+
```

Overrides on-subwindow-char in window<%>.

Returns the result of

```racket
(or (send this on-menu-char event)
    (send this on-system-menu-char event)
    (send this on-traverse-char event))
```

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-frame on-toolbar-button-click) → void? |
+------------------------------------------------+
```

On Mac OS, called when the user clicks the toolbar button on a
frame created with the 'toolbar-button style.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-frame set-status-text text) → void? |
| text: string?                              |
+---------------------------------------------+
```

Sets the frame’s status line text and redraws the status line. See
also create-status-line.
