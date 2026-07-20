<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/pasteboard_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/pasteboard_.html -->
<!-- Canonical English source for Japanese translation -->

```
+---------------------------+-----------+
| classpasteboard%: class? |           |
+---------------------------+-----------+
| superclass: object%       |           |
| extends:                  | editor<%> |
+---------------------------+-----------+
```

A pasteboard% object is an editor for displaying snips with
arbitrary locations.

```
+-------------------------------------------+
| [constructor]                             |
|                                           |
| (new pasteboard%) → (is-a?/c pasteboard%) |
+-------------------------------------------+
```

The editor will not be displayed until it is attached to an
editor-canvas% object or some other display.

A new keymap% object is created for the new editor. See also
get-keymap and set-keymap.

A new style-list% object is created for the new editor. See
also get-style-list and set-style-list.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-pasteboard add-selected snip) → void?    |
| snip: (is-a?/c snip%)                           |
| (send a-pasteboard add-selected x y w h) → void? |
| x: real?                                        |
| y: real?                                        |
| w: (and/c real? (not/c negative?))              |
| h: (and/c real? (not/c negative?))              |
+--------------------------------------------------+
```

Selects snips without deselecting other snips. When coordinates are
given, this method selects all snips that intersect with the given
rectangle (in editor coordinates).

The selection in a pasteboard can be changed
by the system in response to other method calls, and such changes do not go through this method; use on-select to
monitor selection changes.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-pasteboard after-delete snip) → void? |
| snip: (is-a?/c snip%)                        |
+-----------------------------------------------+
```

Refine this method with augment.

Specification:
Called after a snip is deleted from the editor (and after the
display is refreshed; use on-delete
and begin-edit-sequence to avoid extra refreshes
when after-delete modifies the editor).

See also can-delete? and on-edit-sequence.

No internals locks are set when this method is called.

Default implementation: Does nothing.

```
+------------------------------------+
| [method]                           |
|                                    |
| (send a-pasteboard after-insert    |
| snip: (is-a?/c snip%)             |
| before: (or/c (is-a?/c snip%) #f) |
| x: real?                          |
| y: real?                          |
+------------------------------------+
```

Refine this method with augment.

Specification:
Called after a snip is inserted into the editor (and after the
display is refreshed; use on-insert
and begin-edit-sequence to avoid extra refreshes
when after-insert modifies the editor).

See also can-insert? and on-edit-sequence.

No internals locks are set when this method is called.

Default implementation: Does nothing.

```
+----------------------------------------------------------+
| [method]                                                 |
|                                                          |
| (send a-pasteboard after-interactive-move event) → void? |
| event: (is-a?/c mouse-event%)                           |
+----------------------------------------------------------+
```

Refine this method with augment.

Specification:
Called after the user stops interactively dragging snips (the ones
that are selected; see find-next-selected-snip). The mouse event that terminated the move
(usually a button-up event) is provided.

See also can-interactive-move? and
on-interactive-move.

Default implementation:
Does nothing.

```
+-----------------------------------------------------------+
| [method]                                                  |
|                                                           |
| (send a-pasteboard after-interactive-resize snip) → void? |
| snip: (is-a?/c snip%)                                    |
+-----------------------------------------------------------+
```

Refine this method with augment.

Specification:
Called after the user stops interactively resizing a snip (the one
that is currently selected; see find-next-selected-snip). The snip argument is the snip
that was resized.

See also can-interactive-resize? and
on-interactive-resize.

Default implementation:
Does nothing.

```
+----------------------------------+
| [method]                         |
|                                  |
| (send a-pasteboard after-move-to |
| snip: (is-a?/c snip%)           |
| x: real?                        |
| y: real?                        |
| dragging?: any/c                |
+----------------------------------+
```

Refine this method with augment.

Specification:
Called after a given snip is moved within the editor (and after the
display is refreshed; use on-move-to
and begin-edit-sequence to avoid extra refreshes
when after-move-to modifies the editor).

If dragging? is not #f, then this move was a temporary
move for dragging.

See also
can-move-to? and
on-edit-sequence.

No internals locks are set when this method is called.

Default implementation:
Does nothing.

```
+----------------------------------+
| [method]                         |
|                                  |
| (send a-pasteboard after-reorder |
| snip: (is-a?/c snip%)           |
| to-snip: (is-a?/c snip%)        |
| before?: any/c                  |
+----------------------------------+
```

Refine this method with augment.

Specification:
Called before a snip is moved in the pasteboard’s front-to-back snip
order (and after the display is refreshed; use
on-reorder and begin-edit-sequence to avoid extra refreshes when
after-reorder modifies the editor).

If before? is #t, then snip was moved before
to-snip, otherwise snip was moved after to-snip.

See also can-reorder? and on-edit-sequence.

No internals locks are set when this method is called.

Default implementation:
Does nothing.

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-pasteboard after-resize     |
| snip: (is-a?/c snip%)              |
| w: (and/c real? (not/c negative?)) |
| h: (and/c real? (not/c negative?)) |
| resized?: any/c                    |
+-------------------------------------+
```

Refine this method with augment.

Specification:
Called after a given snip is resized (and after the display
is refreshed; use on-resize and
begin-edit-sequence to avoid extra refreshes when
after-resize modifies the editor), or after an
unsuccessful resize attempt was made.

If resized? is not #f, the snip was successfully
resized.

See also can-resize? and on-edit-sequence.

No internals locks are set when this method is called.

Default implementation:
Does nothing.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send a-pasteboard after-select snip on?) → void? |
| snip: (is-a?/c snip%)                            |
| on?: any/c                                       |
+---------------------------------------------------+
```

Refine this method with augment.

Specification:
Called after a snip in the pasteboard is selected or deselected. See
also on-select. This method is not called after
selected snip is deleted (and thus de-selected indirectly); see also
after-delete.

If on? is #t, then snip was just selected,
otherwise snip was just deselected.

See also can-select? and on-edit-sequence.

No internals locks are set when this method is called.

Default implementation:
Does nothing.

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-pasteboard can-delete? snip) → boolean? |
| snip: (is-a?/c snip%)                          |
+-------------------------------------------------+
```

Refine this method with augment.

Specification:
Called before a snip is deleted from the editor.
If the return value is #f, then the
delete will be aborted.

See also on-delete and after-delete.

The editor is internally locked for writing when this method is called (see
also Internal Editor Locks).

Default implementation:
Returns #t.

```
+------------------------------------+
| [method]                           |
|                                    |
| (send a-pasteboard can-insert?     |
| snip: (is-a?/c snip%)             |
| before: (or/c (is-a?/c snip%) #f) |
| x: real?                          |
| y: real?                          |
+------------------------------------+
```

Refine this method with augment.

Specification:
Called before a snip is inserted from the editor. If the return value
is #f, then the insert will be aborted.

See also on-insert and after-insert.

The editor is internally locked for writing when this method is called (see
also Internal Editor Locks).

Default implementation:
Returns #t.

```
+------------------------------------------------------------+
| [method]                                                   |
|                                                            |
| (send a-pasteboard can-interactive-move? event) → boolean? |
| event: (is-a?/c mouse-event%)                             |
+------------------------------------------------------------+
```

Refine this method with augment.

Specification:
Called when the user starts interactively dragging snips (the ones
that are selected; see find-next-selected-snip). All of the selected snips will be
moved. If #f is returned, the interactive move is
disallowed. The mouse event that started the move (usually a
button-down event) is provided.

See also on-interactive-move, after-interactive-move, and interactive-adjust-move.

Default implementation:
Returns #t.

```
+-------------------------------------------------------------+
| [method]                                                    |
|                                                             |
| (send a-pasteboard can-interactive-resize? snip) → boolean? |
| snip: (is-a?/c snip%)                                      |
+-------------------------------------------------------------+
```

Refine this method with augment.

Specification:
Called when the user starts interactively resizing a snip (the one
that is selected; see find-next-selected-snip). If #f is returned, the
interactive resize is disallowed.

The snip argument is the snip that will be resized.

See also after-interactive-resize,
after-interactive-resize, and
interactive-adjust-resize.

Default implementation:
Returns #t.

```
+---------------------------------+
| [method]                        |
|                                 |
| (send a-pasteboard can-move-to? |
| snip: (is-a?/c snip%)          |
| x: real?                       |
| y: real?                       |
| dragging?: any/c               |
+---------------------------------+
```

Refine this method with augment.

Specification:
Called before a snip is moved in the editor. If the return value is
#f, then the move will be aborted.

If dragging? is not #f, then this move is a
temporary move for dragging.

See also on-move-to and after-move-to.

The editor is internally locked for writing when this method is called
(see also Internal Editor Locks).

Default implementation:
Returns #t.

```
+---------------------------------+
| [method]                        |
|                                 |
| (send a-pasteboard can-reorder? |
| snip: (is-a?/c snip%)          |
| to-snip: (is-a?/c snip%)       |
| before?: any/c                 |
+---------------------------------+
```

Refine this method with augment.

Specification:
Called before a snip is moved in the pasteboard’s front-to-back snip
order. If the return value is #f, then the reordering will
be aborted.

If before? is #t, then snip is to be moved before
to-snip, otherwise snip is to be moved after
to-snip.

See also on-reorder and after-reorder.

The editor is internally locked for writing when this method is called (see
also Internal Editor Locks).

Default implementation:
Returns #t.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-pasteboard can-resize? snip w h) → boolean? |
| snip: (is-a?/c snip%)                              |
| w: (and/c real? (not/c negative?))                 |
| h: (and/c real? (not/c negative?))                 |
+-----------------------------------------------------+
```

Refine this method with augment.

Specification:
Called before a snip is resized in the editor. If the return value is
#f, then the resize will be aborted.

See also on-resize and after-resize.

The editor is internally locked for writing when this method is called (see
also Internal Editor Locks).

Default implementation:
Returns #t.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-pasteboard can-select? snip on?) → boolean? |
| snip: (is-a?/c snip%)                              |
| on?: any/c                                         |
+-----------------------------------------------------+
```

Refine this method with augment.

Specification:
This method is called before a snip in the pasteboard is selected or
deselected. If #f is returned, the selection change is
disallowed. This method is not called when a selected snip is to be
deleted (and thus de-selected indirectly); see also
can-delete?.

If on? is #t, then snip will be selected,
otherwise snip will be deselected.

See also on-select and after-select.

The editor is internally locked for writing when this method is called (see
also Internal Editor Locks).

Default implementation:
Returns #t.

```
+------------------------------------------------------------------+
| [method]                                                         |
|                                                                  |
| (send a-pasteboard change-style [style snip]) → void?            |
| style: (or/c (is-a?/c style-delta%) (is-a?/c style<%>) #f) = #f |
| snip: (or/c (is-a?/c snip%) #f) = #f                            |
+------------------------------------------------------------------+
```

Changes the style of snip to a specific style or by applying
a style delta. If snip is #f, then all currently
selected snips are changed. If style is #f, then
the default style is used, according to default-style-name.

To change a large collection of snips from one style to another style,
consider providing a style<%> instance rather than a
style-delta% instance. Otherwise, change-style must convert the style-delta% instance to the
style<%> instance for every snip; this conversion consumes
both time and (temporary) memory.

When a style is provided: The editor’s style list must contain style, otherwise
the style is not changed. See also convert in style-list%.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-pasteboard copy-self-to dest) → void?       |
| dest: (or/c (is-a?/c text%) (is-a?/c pasteboard%)) |
+-----------------------------------------------------+
```

Overrides copy-self-to in editor<%>.

In addition to the default copy-self-to in editor<%> work, the
dragability, selection visibility state, and scroll step of
a-pasteboard are installed into dest.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-pasteboard delete) → void?      |
| (send a-pasteboard delete snip) → void? |
| snip: (is-a?/c snip%)                  |
+-----------------------------------------+
```

Deletes snip when provided, or deletes the currently selected
snips from the editor when snip is not provided.

The content of an editor can be changed
by the
system in response to other method
calls, and such changes do not go through this method; use on-delete to
monitor content deletion changes.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-pasteboard do-copy time extend?) → void? |
| time: exact-integer?                            |
| extend?: any/c                                  |
+--------------------------------------------------+
```

Specification:
Called to copy the editor’s current selection into the clipboard.
This method is provided so that it can be overridden by subclasses.
Do not call this method directly; instead, call copy.

See Cut and Paste Time Stamps for a discussion of the time argument. If
time is outside the platform-specific range of times,
an exn:fail:contract exception is raised.

Default implementation:
Copies the current selection, extending the current clipboard contexts
if extend? is true.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-pasteboard do-paste time) → void? |
| time: exact-integer?                     |
+-------------------------------------------+
```

Specification:
Called to paste the current contents of the clipboard into the editor.
This method is provided so that it can be overridden by subclasses.
Do not call this method directly; instead, call paste.

See Cut and Paste Time Stamps for a discussion of the time argument. If
time is outside the platform-specific range of times,
an exn:fail:contract exception is raised.

Default implementation:
Pastes.

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-pasteboard do-paste-x-selection time) → void? |
| time: exact-integer?                                 |
+-------------------------------------------------------+
```

Specification:
Called to paste the current contents of the X11 selection on Unix (or
the clipboard on Windows and Mac OS) into the editor. This
method is provided so that it can be overridden by subclasses. Do
not call this method directly; instead, call paste-x-selection.

See Cut and Paste Time Stamps for a discussion of the time argument. If
time is outside the platform-specific range of times,
an exn:fail:contract exception is raised.

Default implementation:
Pastes.

```
+-----------------------------------+
| [method]                          |
|                                   |
| (send a-pasteboard erase) → void? |
+-----------------------------------+
```

Deletes all snips from the editor.

See also delete.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send a-pasteboard find-next-selected-snip start) |
| → (or/c (is-a?/c snip%) #f)                       |
| start: (or/c (is-a?/c snip%) #f)                 |
+---------------------------------------------------+
```

Returns the next selected snip in the editor, starting the search
after start. (See Editor Structure and Terminology for information about snip order in pasteboards.) If start is #f,
then the search starts with the first snip in the editor (and thus
returns the first selected snip, if any are selected). If no more
selected snips are available, or if start is not in the
pasteboard, #f is returned.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-pasteboard find-snip x y [after]) |
| → (or/c (is-a?/c snip%) #f)               |
| x: real?                                 |
| y: real?                                 |
| after: (or/c (is-a?/c snip%) #f) = #f    |
+-------------------------------------------+
```

Finds the frontmost snip (after a given snip) that intersects a given
location. See Editor Structure and Terminology for information about snip order in pasteboards.

The x and y arguments are in editor coordinates. If
after is not supplied, the frontmost snip at x and
y is returned, otherwise the frontmost snip behind after
is returned. If after is a snip that is not in the pasteboard,
#f is returned.

The result is only valid when the editor is displayed
(see Editor Structure and Terminology). Editors are displayed when
get-admin returns an administrator (not #f).

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-pasteboard get-area-selectable) → boolean? |
+----------------------------------------------------+
```

Returns whether snips can be selected by dragging a selection box in the
pasteboard’s background. By default, area selection
is allowed. See also set-area-selectable.

Added in version 1.12 of package `gui-lib`.

```
+--------------------------------+
| [method]                       |
|                                |
| (send a-pasteboard get-center) |
| real?                          |
+--------------------------------+
```

Returns the center of the pasteboard in pasteboard coordinates.

The first result is the x-coordinate of the center and
the second result is the y-coordinate of the center.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-pasteboard get-dragable) → boolean? |
+---------------------------------------------+
```

Returns whether snips in the editor can be interactively dragged by
event handling in on-default-event: #t
if dragging is allowed, #f otherwise. By default, dragging
is allowed. See also set-dragable.

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-pasteboard get-scroll-step) |
| → (and/c real? (not/c negative?))   |
+-------------------------------------+
```

Gets the editor location offset for each vertical scroll
position. See also set-scroll-step.

```
+------------------------------------------------------+
| [method]                                             |
|                                                      |
| (send a-pasteboard get-selection-visible) → boolean? |
+------------------------------------------------------+
```

Returns whether selection dots are drawn around the edge of selected
snips in the pasteboard. By default, selection dots are on. See also
set-selection-visible.

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-pasteboard insert snip) → void?            |
| snip: (is-a?/c snip%)                             |
| (send a-pasteboard insert snip before x y) → void? |
| snip: (is-a?/c snip%)                             |
| before: (or/c (is-a?/c snip%) #f)                 |
| x: real?                                          |
| y: real?                                          |
| (send a-pasteboard insert snip x y) → void?        |
| snip: (is-a?/c snip%)                             |
| x: real?                                          |
| y: real?                                          |
| (send a-pasteboard insert snip before) → void?     |
| snip: (is-a?/c snip%)                             |
| before: (or/c (is-a?/c snip%) #f)                 |
+----------------------------------------------------+
```

Extends insert in editor<%>.

Inserts snip at location (x,
y) just in front of
before. (See Editor Structure and Terminology for information about snip order in pasteboards.) If before is not
provided or is #f, then snip is inserted behind all
other snips. If x and y are not provided, the snip
is added at the center of the pasteboard.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-pasteboard interactive-adjust-mouse |
| x: (box/c real?)                           |
| y: (box/c real?)                           |
+---------------------------------------------+
```

Specification:
This method is called during interactive dragging and resizing (of the
currently selected snips; see find-next-selected-snip) to preprocess the current mouse
location (in editor coordinates). The snip and actual x
and y coordinates are passed into the method (boxed); the resulting
coordinates are used instead of the actual mouse location.

See also
interactive-adjust-resize.

Default implementation:
A negative value for either x or y is replaced with
0.

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send a-pasteboard interactive-adjust-move |
| snip: (is-a?/c snip%)                     |
| x: (box/c real?)                          |
| y: (box/c real?)                          |
+--------------------------------------------+
```

Specification:
This method is called during an interactive move (for each selected
snip) to preprocess the user-determined snip location for each
selected snip. The snip and mouse-determined locations (in editor
coordinates) are passed into the method (boxed); the resulting
locations are used for graphical feedback to the user during moving.

The actual mouse coordinates are first sent through
interactive-adjust-mouse before determining the
locations passed into this method.

Default implementation:
Does nothing.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-pasteboard interactive-adjust-resize     |
| snip: (is-a?/c snip%)                           |
| width: (box/c (and/c real? (not/c negative?)))  |
| height: (box/c (and/c real? (not/c negative?))) |
+--------------------------------------------------+
```

Specification:
This method is called during interactive resizing of a snip to
preprocess the user-determined snip size. The snip and
mouse-determined height and width are passed into the method (boxed);
the resulting height and width are used for graphical feedback to the
user during resizing.

The actual mouse coordinates are first sent through
interactive-adjust-mouse before determining the
sizes passed into this method.

Default implementation:
Does nothing.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-pasteboard is-selected? snip) → boolean? |
| snip: (is-a?/c snip%)                           |
+--------------------------------------------------+
```

Returns #t if a specified snip is currently selected or
#f otherwise.

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-pasteboard lower snip) → void? |
| snip: (is-a?/c snip%)                 |
+----------------------------------------+
```

Moves the snip one level deeper (i.e., behind one more other snip) in
the pasteboard’s snip order. See Editor Structure and Terminology for information about snip order in pasteboards.

See also raise, set-before,
and set-after.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-pasteboard move snip x y) → void? |
| snip: (is-a?/c snip%)                    |
| x: real?                                 |
| y: real?                                 |
| (send a-pasteboard move x y) → void?      |
| x: real?                                 |
| y: real?                                 |
+-------------------------------------------+
```

Moves snip right x pixels and down y
pixels. If snip is not provided, then all selected snips
are moved.

Snip locations in a pasteboard can be changed
by the system in response to other method calls, and such changes do not go through this method; use on-move-to to
monitor snip position changes.

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-pasteboard move-to snip x y) → void? |
| snip: (is-a?/c snip%)                       |
| x: real?                                    |
| y: real?                                    |
+----------------------------------------------+
```

Moves snip to a given location in the editor.

Snip locations in a pasteboard can be changed
by the system in response to other method calls, and such changes do not go through this method; use on-move-to to
monitor snip position changes.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-pasteboard no-selected) → void? |
+-----------------------------------------+
```

Deselects all selected snips in the editor.

The selection in a pasteboard can be changed
by the system in response to other method calls, and such changes do not go through this method; use on-select to
monitor selection changes.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send a-pasteboard on-default-char event) → void? |
| event: (is-a?/c key-event%)                      |
+---------------------------------------------------+
```

Overrides on-default-char in editor<%>.

Calls delete with no arguments in response to the
Delete or Backspace key, and calls move with
suitable 0/1/-1 arguments in response to an
arrow key.

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-pasteboard on-default-event event) → void? |
| event: (is-a?/c mouse-event%)                     |
+----------------------------------------------------+
```

Overrides on-default-event in editor<%>.

Selects, drags, and resizes snips:

- Clicking on a snip selects the snip. Shift-clicking extends
the current selection with the snip.
- Clicking in the space between snips drags a selection
box; once the mouse button is released, all snips touching the
box are selected. Shift-clicking extends the current selection
with the new snips.
- Double-clicking on a snip calls
on-double-click.
- Clicking on a selected snip drags the selected snip(s) to a new
location.
- Clicking on a hiliting tab for a selected object resizes the
object.

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send a-pasteboard on-delete snip) → void? |
| snip: (is-a?/c snip%)                     |
+--------------------------------------------+
```

Refine this method with augment.

Called before a snip is deleted from the editor, after
can-delete? is called to verify that the
deletion is allowed. The after-delete method is
guaranteed to be called after the delete has completed.

The editor is internally locked for writing when this method is called
(see also Internal Editor Locks). Use after-delete to
modify the editor, if necessary.

```
+------------------------------------+
| [method]                           |
|                                    |
| (send a-pasteboard on-double-click |
| snip: (is-a?/c snip%)             |
| event: (is-a?/c mouse-event%)     |
+------------------------------------+
```

Specification:
This method is called when the user double-clicks on a snip in the
editor. The clicked-on snip and event records are passed to the
method.

Default implementation:
If snip accepts events, it is designated as the caret owner
and all snips in the editor are unselected.

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-pasteboard on-insert snip before x y) → void? |
| snip: (is-a?/c snip%)                                |
| before: (or/c (is-a?/c snip%) #f)                    |
| x: real?                                             |
| y: real?                                             |
+-------------------------------------------------------+
```

Refine this method with augment.

Called before a snip is inserted from the editor, after
can-insert? is called to verify that the
insertion is allowed. The after-insert method is
guaranteed to be called after the insert has completed.

The editor is internally locked for writing when this method is called
(see also Internal Editor Locks). Use after-insert to
modify the editor, if necessary.

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-pasteboard on-interactive-move event) → void? |
| event: (is-a?/c mouse-event%)                        |
+-------------------------------------------------------+
```

Refine this method with augment.

Specification:
Called when the user starts interactively dragging snips (the ones
that are selected; see find-next-selected-snip),
after can-interactive-move? is called to verify
that the move is allowed. The after-interactive-move method is guaranteed to be called after the
move has completed. All of the selected snips will be moved. The
mouse event that started the move (usually a button-down event) is
provided.

See also interactive-adjust-move.

Default implementation:
Does nothing.

```
+--------------------------------------------------------+
| [method]                                               |
|                                                        |
| (send a-pasteboard on-interactive-resize snip) → void? |
| snip: (is-a?/c snip%)                                 |
+--------------------------------------------------------+
```

Refine this method with augment.

Specification:
Called when the user starts interactively resizing a snip (the one
that is selected; see find-next-selected-snip),
after can-interactive-resize? is called to
verify that the resize is allowed. The after-interactive-resize method is guaranteed to be called after the
resize has completed.

The snip argument is the snip that will be resized.

Default implementation:
Does nothing.

```
+-------------------------------+
| [method]                      |
|                               |
| (send a-pasteboard on-move-to |
| snip: (is-a?/c snip%)        |
| x: real?                     |
| y: real?                     |
| dragging?: any/c             |
+-------------------------------+
```

Refine this method with augment.

Specification:
Called before a snip is moved in the editor, after can-move-to? is called to verify that the move is allowed. The
after-move-to method is guaranteed to be called
after the move has completed.

If dragging? is not #f, then this move is a
temporary move for dragging.

The editor is internally locked for writing when this method is called
(see also Internal Editor Locks). Use after-move-to to
modify the editor, if necessary. See also on-interactive-move and interactive-adjust-move.

Default implementation:
Does nothing.

```
+-------------------------------+
| [method]                      |
|                               |
| (send a-pasteboard on-reorder |
| snip: (is-a?/c snip%)        |
| to-snip: (is-a?/c snip%)     |
| before?: any/c               |
+-------------------------------+
```

Refine this method with augment.

Specification:
Called before a snip is moved in the pasteboard’s front-to-back snip
order, after can-reorder? is called to verify
that the reorder is allowed. The after-reorder
method is guaranteed to be called after the reorder has completed.

If before? is #t, then snip is to be moved
before to-snip, otherwise snip is to be moved after
to-snip.

The editor is internally locked for writing when this method is called
(see also Internal Editor Locks). Use after-reorder to
modify the editor, if necessary.

Default implementation:
Does nothing.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-pasteboard on-resize snip w h) → void? |
| snip: (is-a?/c snip%)                         |
| w: (and/c real? (not/c negative?))            |
| h: (and/c real? (not/c negative?))            |
+------------------------------------------------+
```

Refine this method with augment.

Specification:
Called before a snip is resized by the editor, after
can-resize? is called to verify that the resize
is allowed. The after-resize method is
guaranteed to be called after the resize has completed.

The editor is internally locked for writing when this method is called (see
also Internal Editor Locks). Use
after-resize to modify the editor, if necessary.

Note that a snip calls
resized, not this method, to notify the pasteboard that the snip resized
itself.

Default implementation:
Does nothing.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-pasteboard on-select snip on?) → void? |
| snip: (is-a?/c snip%)                         |
| on?: any/c                                    |
+------------------------------------------------+
```

Refine this method with augment.

Specification:
Called before a snip in the pasteboard is selected or deselected,
after can-select? is called to verify that the
selection is allowed. The after-select method is
guaranteed to be called after the selection has completed. This
method is not called when a selected snip is to be deleted (and thus
de-selected indirectly); see also on-delete.

If on? is #t, then snip will be selected,
otherwise snip will be deselected.

The editor is internally locked for writing when this method is called
(see also Internal Editor Locks). Use after-select to
modify the editor, if necessary.

Default implementation:
Does nothing.

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-pasteboard raise snip) → void? |
| snip: (is-a?/c snip%)                 |
+----------------------------------------+
```

Moves a snip one level shallower (i.e., in front of one more other
snip) in the pasteboard’s snip order. See Editor Structure and Terminology for information about snip order in pasteboards.

See also lower, set-before,
and set-after.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-pasteboard remove snip) → void? |
| snip: (is-a?/c snip%)                  |
+-----------------------------------------+
```

Removes the specified snip from the editor in a non-undoable manner
(so the snip is completely free of the pasteboard can be used in
other editors).

See also delete.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-pasteboard remove-selected snip) → void? |
| snip: (is-a?/c snip%)                           |
+--------------------------------------------------+
```

Deselects snip (if it is currently selected) without
deselecting any other snips.

The selection in a pasteboard can be changed
by the system in response to other method calls, and such changes do not go through this method; use on-select to
monitor selection changes.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-pasteboard resize snip w h) → boolean? |
| snip: (is-a?/c snip%)                         |
| w: (and/c real? (not/c negative?))            |
| h: (and/c real? (not/c negative?))            |
+------------------------------------------------+
```

Attempts to resize a given snip. If the snip allows resizing,
#t is returned, otherwise #f is returned. Using
this method instead of calling the snip’s resize
method directly will make the resize undo-able.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-pasteboard set-after snip after) → void? |
| snip: (is-a?/c snip%)                           |
| after: (or/c (is-a?/c snip%) #f)                |
+--------------------------------------------------+
```

Changes the depth of snip moving it just behind
after. If after is #f, snip is
moved to the back. See Editor Structure and Terminology for information about snip order in pasteboards.

See also raise, lower, and
set-before.

```
+-------------------------------------------------------------+
| [method]                                                    |
|                                                             |
| (send a-pasteboard set-area-selectable allow-drag?) → void? |
| allow-drag?: any/c                                         |
+-------------------------------------------------------------+
```

Set whether snips can be selected by dragging a selection box in the
pasteboard’s background by event handling in on-default-event: a true value allows selection, #f
disallows selection. See also get-area-selectable.

Added in version 1.12 of package `gui-lib`.

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-pasteboard set-before snip before) → void? |
| snip: (is-a?/c snip%)                             |
| before: (or/c (is-a?/c snip%) #f)                 |
+----------------------------------------------------+
```

Changes the depth of snip moving it just in front of
before. If before is #f, snip is
moved to the front. See Editor Structure and Terminology for information about snip order in pasteboards.

See also raise, lower, and
set-after.

```
+------------------------------------------------------+
| [method]                                             |
|                                                      |
| (send a-pasteboard set-dragable allow-drag?) → void? |
| allow-drag?: any/c                                  |
+------------------------------------------------------+
```

Sets whether snips in the editor can be interactively dragged by event
handling in on-default-event: a true value
allows dragging, #f disallows dragging. See also
get-dragable.

```
+------------------------------------------------------+
| [method]                                             |
|                                                      |
| (send a-pasteboard set-scroll-step stepsize) → void? |
| stepsize: (and/c real? (not/c negative?))           |
+------------------------------------------------------+
```

Sets the editor location offset for each vertical scroll
position. See also get-scroll-step.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-pasteboard set-selected snip) → void? |
| snip: (is-a?/c snip%)                        |
+-----------------------------------------------+
```

Selects a specified snip (deselecting all others).

The selection in a pasteboard can be changed
by the system in response to other method calls, and such changes do not go through this method; use on-select to
monitor selection changes.

```
+------------------------------------------------------------+
| [method]                                                   |
|                                                            |
| (send a-pasteboard set-selection-visible visible?) → void? |
| visible?: any/c                                           |
+------------------------------------------------------------+
```

Sets whether selection dots are drawn around the edge of selected
snips in the pasteboard. See also get-selection-visible.
