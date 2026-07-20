<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/editor-snip_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/editor-snip_.html -->
<!-- Canonical English source for Japanese translation -->

```
+----------------------------+
| classeditor-snip%: class? |
+----------------------------+
| superclass: snip%          |
+----------------------------+
```

An editor-snip% object is a snip% object that
contains and displays an editor<%> object. This snip class
is used to insert an editor as a single item within
another editor.

```
+-------------------------------------------------------------------+
| [constructor]                                                     |
|                                                                   |
| (new editor-snip%                                                 |
| → (is-a?/c editor-snip%)                                          |
| editor: (or/c (is-a?/c editor<%>) #f) = #f                       |
| with-border?: any/c = #t                                         |
| left-margin: exact-nonnegative-integer? = 5                      |
| top-margin: exact-nonnegative-integer? = 5                       |
| right-margin: exact-nonnegative-integer? = 5                     |
| bottom-margin: exact-nonnegative-integer? = 5                    |
| left-inset: exact-nonnegative-integer? = 1                       |
| top-inset: exact-nonnegative-integer? = 1                        |
| right-inset: exact-nonnegative-integer? = 1                      |
| bottom-inset: exact-nonnegative-integer? = 1                     |
| min-width: (or/c (and/c real? (not/c negative?)) 'none) = 'none  |
| max-width: (or/c (and/c real? (not/c negative?)) 'none) = 'none  |
| min-height: (or/c (and/c real? (not/c negative?)) 'none) = 'none |
| max-height: (or/c (and/c real? (not/c negative?)) 'none) = 'none |
+-------------------------------------------------------------------+
```

If editor is non-#f, then it will be used as the
editor contained by the snip. See also set-editor.

If with-border? is not #f, then a border will be drawn
around the snip. The editor display will be inset in the snip area by
the amounts specified in the -margin arguments. The border
will be drawn with an inset specified by the -inset arguments.

See get-inset and get-margin for information about the inset and margin arguments.

```
+------------------------------------+
| [method]                           |
|                                    |
| (send an-editor-snip adjust-cursor |
| → (or/c (is-a?/c cursor%) #f)      |
| dc: (is-a?/c dc<%>)               |
| x: real?                          |
| y: real?                          |
| editorx: real?                    |
| editory: real?                    |
| event: (is-a?/c mouse-event%)     |
+------------------------------------+
```

Overrides adjust-cursor in snip%.

Gets a cursor from the embedded editor by calling its
adjust-cursor method.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send an-editor-snip border-visible?) → boolean? |
+--------------------------------------------------+
```

Returns #t if the snip has a border draw around it,
#f otherwise.

See also show-border.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send an-editor-snip get-align-top-line) → boolean? |
+-----------------------------------------------------+
```

Reports whether the snip is in align-top-line mode. See
get-extent for more information.

See also set-align-top-line.

```
+----------------------------------------------------------+
| [method]                                                 |
|                                                          |
| (send an-editor-snip get-editor)                         |
| → (or/c (or/c (is-a?/c text%) (is-a?/c pasteboard%)) #f) |
+----------------------------------------------------------+
```

Returns the editor contained by the snip, or #f is there is
no editor.

```
+------------------------------------------------------------------+
| [method]                                                         |
|                                                                  |
| (send an-editor-snip get-extent                                  |
| dc: (is-a?/c dc<%>)                                             |
| x: real?                                                        |
| y: real?                                                        |
| w: (or/c (box/c (and/c real? (not/c negative?))) #f) = #f       |
| h: (or/c (box/c (and/c real? (not/c negative?))) #f) = #f       |
| descent: (or/c (box/c (and/c real? (not/c negative?))) #f) = #f |
| space: (or/c (box/c (and/c real? (not/c negative?))) #f) = #f   |
| lspace: (or/c (box/c (and/c real? (not/c negative?))) #f) = #f  |
| rspace: (or/c (box/c (and/c real? (not/c negative?))) #f) = #f  |
+------------------------------------------------------------------+
```

Overrides get-extent in snip%.

Calls its editor’s get-extent method, then adds the
editor snip’s margins.

The top space always corresponds to the space of the editor’s top
line, plus the snip’s top margin. Normally, the descent corresponds
to the descent of the editor’s last line plus the snip’s bottom
margin. However, if the snip is in align-top-line mode (see
set-align-top-line), the descent corresponds to
the descent of the top line, plus the height rest of the editor’s
lines, plus the snip’s bottom margin.

If the editor is a text editor, then 1 is normally subtracted
from the editor’s width as returned by get-extent,
because the result looks better for editing. If the snip is in
tight-text-fit mode (see set-tight-text-fit)
then 2 is subtracted from a text editor’s width, eliminating
the two pixels that the text editor reserves for the blinking
caret. In addition, tight-text-fit mode subtracts an amount equal to
the line spacing from the editor’s height. By default, tight-text-fit
mode is disabled.

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send an-editor-snip get-inset l t r b) → void? |
| l: (box/c exact-nonnegative-integer?)          |
| t: (box/c exact-nonnegative-integer?)          |
| r: (box/c exact-nonnegative-integer?)          |
| b: (box/c exact-nonnegative-integer?)          |
+-------------------------------------------------+
```

Gets the current border insets for the snip. The inset sets how much space
is left between the edge of the snip and the border.

The l box is filled with left inset.
The t box is filled with top inset.
The r box is filled with right inset.
The b box is filled with bottom inset.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send an-editor-snip get-margin l t r b) → void? |
| l: (box/c exact-nonnegative-integer?)           |
| t: (box/c exact-nonnegative-integer?)           |
| r: (box/c exact-nonnegative-integer?)           |
| b: (box/c exact-nonnegative-integer?)           |
+--------------------------------------------------+
```

Gets the current margins for the snip. The margin sets how much space
is left between the edge of the editor’s contents and the edge of the
snip.

The l box is filled with left margin.
The t box is filled with top margin.
The r box is filled with right margin.
The b box is filled with bottom margin.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send an-editor-snip get-max-height)           |
| → (or/c (and/c real? (not/c negative?)) 'none) |
+------------------------------------------------+
```

Gets the maximum display height of the snip; zero or 'none
indicates that there is no maximum.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send an-editor-snip get-max-width)            |
| → (or/c (and/c real? (not/c negative?)) 'none) |
+------------------------------------------------+
```

Gets the maximum display width of the snip; zero or 'none
indicates that there is no maximum.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send an-editor-snip get-min-height)           |
| → (or/c (and/c real? (not/c negative?)) 'none) |
+------------------------------------------------+
```

Gets the minimum display height of the snip; zero or 'none
indicates that there is no minimum.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send an-editor-snip get-min-width)            |
| → (or/c (and/c real? (not/c negative?)) 'none) |
+------------------------------------------------+
```

Gets the minimum display width of the snip; zero or 'none
indicates that there is no minimum.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send an-editor-snip get-tight-text-fit) → boolean? |
+-----------------------------------------------------+
```

Reports whether the snip is in tight-text-fit mode. See
get-extent for more information.

See also set-tight-text-fit.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send an-editor-snip resize w h) → boolean? |
| w: (and/c real? (not/c negative?))         |
| h: (and/c real? (not/c negative?))         |
+---------------------------------------------+
```

Overrides resize in snip%.

Sets the snip’s minimum and maximum width and height to the specified
values minus the snip border space. See also set-min-width set-max-width
set-max-height set-min-height.

Also sets the minimum and maximum width of the editor owned by the
snip to the given width (minus the snip border space) via
set-max-width and set-min-width.

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send an-editor-snip set-align-top-line tight?) → void? |
| tight?: any/c                                          |
+---------------------------------------------------------+
```

Enables or disables align-top-line mode. See get-extent for more information.

See also get-align-top-line.

```
+-----------------------------------------------------------------+
| [method]                                                        |
|                                                                 |
| (send an-editor-snip set-editor editor) → void?                 |
| editor: (or/c (or/c (is-a?/c text%) (is-a?/c pasteboard%)) #f) |
+-----------------------------------------------------------------+
```

Sets the editor contained by the snip, releasing the old editor in the
snip (if any). If the new editor already has an administrator, then
the new editor is not installed into the snip.

When an editor-snip% object is not inserted in an editor, it
does not have an administrator. During this time, it does not give
its contained editor an administrator, either. The administratorless
contained editor can therefore “defect” to some other
display with an administrator. When a contained editor
defects and the snip is eventually inserted into a different editor,
the snip drops the traitor contained editor, setting its contained
editor to #f.

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send an-editor-snip set-inset l t r b) → void? |
| l: exact-nonnegative-integer?                  |
| t: exact-nonnegative-integer?                  |
| r: exact-nonnegative-integer?                  |
| b: exact-nonnegative-integer?                  |
+-------------------------------------------------+
```

Sets the current border insets for the snip. The inset sets how much
space is left between the edge of the snip and the border.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send an-editor-snip set-margin l t r b) → void? |
| l: exact-nonnegative-integer?                   |
| t: exact-nonnegative-integer?                   |
| r: exact-nonnegative-integer?                   |
| b: exact-nonnegative-integer?                   |
+--------------------------------------------------+
```

Sets the current margins for the snip. The margin sets how much space
is left between the edge of the editor’s contents and the edge of the
snip.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send an-editor-snip set-max-height h) → void?   |
| h: (or/c (and/c real? (not/c negative?)) 'none) |
+--------------------------------------------------+
```

An editor-snip% normally stretches to wrap around the size
of the editor it contains. This method limits the height of the snip
(and if the editor is larger, only part of the editor is displayed).

Zero or 'none disables the limit.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send an-editor-snip set-max-width w) → void?    |
| w: (or/c (and/c real? (not/c negative?)) 'none) |
+--------------------------------------------------+
```

An editor-snip% normally stretches to wrap around the size
of the editor it contains. This method limits the width of the snip
(and if the editor is larger, only part of the editor is displayed). The contained editor’s width limits are not
changed by this method.

Zero or 'none disables the limit.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send an-editor-snip set-min-height h) → void?   |
| h: (or/c (and/c real? (not/c negative?)) 'none) |
+--------------------------------------------------+
```

An editor-snip% normally stretches to wrap around the size
of the editor it contains. This method sets the minimum height of the snip
(and if the editor is smaller, the editor is top-aligned in the snip).

Zero or 'none disables the limit.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send an-editor-snip set-min-width w) → void?    |
| w: (or/c (and/c real? (not/c negative?)) 'none) |
+--------------------------------------------------+
```

An editor-snip% normally stretches to wrap around the size
of the editor it contains. This method sets the minimum width of the snip
(and if the editor is smaller, the editor is left-aligned in the snip). The contained editor’s width
limits are not changed by this method.

Zero or 'none disables the limit.

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send an-editor-snip set-tight-text-fit tight?) → void? |
| tight?: any/c                                          |
+---------------------------------------------------------+
```

Enables or disables tight-text-fit mode. See get-extent for more information.

See also get-tight-text-fit.

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send an-editor-snip show-border show?) → void? |
| show?: any/c                                   |
+-------------------------------------------------+
```

Shows or hides the snip’s border.

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send an-editor-snip style-background-used?) → boolean? |
+---------------------------------------------------------+
```

Returns #t if the snip uses its style’s background and
transparency information when drawing, #f otherwise.

See also use-style-background.

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send an-editor-snip use-style-background use?) → void? |
| use?: any/c                                            |
+---------------------------------------------------------+
```

Causes the snip to use or not used (the default) its style’s
background and transparency information for drawing the background
within the snip’s border.

If use? is #f, the style background and transparency
information is ignored, otherwise is it used.
