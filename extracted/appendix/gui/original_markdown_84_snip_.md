<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/snip_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/snip_.html -->
<!-- Canonical English source for Japanese translation -->

```
+---------------------+----------+
| classsnip%: class? |          |
+---------------------+----------+
| superclass: object% |          |
| extends:            | equal<%> |
+---------------------+----------+
```

A direct instance of snip% is uninteresting. Useful snips are
defined by instantiating derived subclasses, but the snip% class defines
the basic functionality. See Implementing New Snips for more information about
deriving a new snip class.

```
+-------------------------------+
| [constructor]                 |
|                               |
| (new snip%) → (is-a?/c snip%) |
+-------------------------------+
```

Creates a plain snip of length 1 with the "Basic" style of
the-style-list.

```
+--------------------------------+
| [method]                       |
|                                |
| (send a-snip adjust-cursor     |
| → (or/c (is-a?/c cursor%) #f)  |
| dc: (is-a?/c dc<%>)           |
| x: real?                      |
| y: real?                      |
| editorx: real?                |
| editory: real?                |
| event: (is-a?/c mouse-event%) |
+--------------------------------+
```

Specification:
Called to determine the cursor image used when the cursor is moved
over the snip in an editor. If #f is returned, a default
cursor is selected by the editor. (See adjust-cursor in editor<%> for more information.)

Default implementation:
Returns #f.

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send a-snip blink-caret dc x y) → void? |
| dc: (is-a?/c dc<%>)                     |
| x: real?                                |
| y: real?                                |
+------------------------------------------+
```

Tells the snip to blink the selection caret. This method is called
periodically when the snip’s editor’s display has the
keyboard focus, and the snip has the editor-local focus.

The drawing context and snip’s locations in drawing context
coordinates are provided.

```
+-------------------------------------------------------------------+
| [method]                                                          |
|                                                                   |
| (send a-snip can-do-edit-operation?                               |
| op: (or/c 'undo 'redo 'clear 'cut 'copy 'paste 'kill 'select-all |
| 'insert-text-box 'insert-pasteboard-box 'insert-image)            |
| (or/c 'undo 'redo 'clear 'cut 'copy                               |
| 'paste 'kill 'select-all                                          |
| 'insert-text-box 'insert-pasteboard-box                           |
| 'insert-image)                                                    |
| recursive?: any/c = #t                                           |
|                                                                   |
| ```racket                                                         |
| (or/c 'undo 'redo 'clear 'cut 'copy                               |
|       'paste 'kill 'select-all                                    |
|       'insert-text-box 'insert-pasteboard-box                     |
|       'insert-image)                                              |
| ```                                                               |
+-------------------------------------------------------------------+
```

See can-do-edit-operation? in editor<%>.

Called when the snip’s editor’s method is called, recursive?
is not #f, and this snip owns the caret.

```
+--------------------------------------+
| [method]                             |
|                                      |
| (send a-snip copy) → (is-a?/c snip%) |
+--------------------------------------+
```

Creates and returns a copy of this snip. The copy
method is responsible for copying this snip’s style (as returned by
get-style) to the new snip.

```
+-------------------------------------------------------------------+
| [method]                                                          |
|                                                                   |
| (send a-snip do-edit-operation                                    |
| op: (or/c 'undo 'redo 'clear 'cut 'copy 'paste 'kill 'select-all |
| 'insert-text-box 'insert-pasteboard-box 'insert-image)            |
| (or/c 'undo 'redo 'clear 'cut 'copy                               |
| 'paste 'kill 'select-all                                          |
| 'insert-text-box 'insert-pasteboard-box                           |
| 'insert-image)                                                    |
| recursive?: any/c = #t                                           |
| time: exact-integer? = 0                                         |
|                                                                   |
| ```racket                                                         |
| (or/c 'undo 'redo 'clear 'cut 'copy                               |
|       'paste 'kill 'select-all                                    |
|       'insert-text-box 'insert-pasteboard-box                     |
|       'insert-image)                                              |
| ```                                                               |
+-------------------------------------------------------------------+
```

See do-edit-operation in editor<%>.

Called when the snip’s editor’s method is called,
recursive? is not #f, and this snip owns the caret.

```
+-----------------------------------------------------------------------+
| [method]                                                              |
|                                                                       |
| (send a-snip draw                                                     |
| dc: (is-a?/c dc<%>)                                                  |
| x: real?                                                             |
| y: real?                                                             |
| left: real?                                                          |
| top: real?                                                           |
| right: real?                                                         |
| bottom: real?                                                        |
| dx: real?                                                            |
| dy: real?                                                            |
| draw-caret: (or/c 'no-caret 'show-inactive-caret 'show-caret (cons/c |
| exact-nonnegative-integer? exact-nonnegative-integer?))               |
| (or/c 'no-caret 'show-inactive-caret 'show-caret                      |
| (cons/c exact-nonnegative-integer?                                    |
| exact-nonnegative-integer?))                                          |
|                                                                       |
| ```racket                                                             |
| (or/c 'no-caret 'show-inactive-caret 'show-caret                      |
|       (cons/c exact-nonnegative-integer?                              |
|               exact-nonnegative-integer?))                            |
| ```                                                                   |
+-----------------------------------------------------------------------+
```

Specification:
Called (by an editor) to draw the snip into the given drawing context
with the snip’s top left corner at location (x,
y) in DC coordinates.

The arguments left, top, right, and bottom
define a clipping region (in DC coordinates) that the snip can use to
optimize drawing, but it can also ignore these arguments.

The dx and dy argument provide numbers that can be
subtracted from x and y to obtain the snip’s location in
editor coordinates (as opposed to DC coordinates, which are used for
drawing).

See Caret Ownership for information about
draw-caret. When draw-caret is a pair, refrain from
drawing a background for the selected region, and if
(get-highlight-text-color) returns a color (instead of #f),
use that color for drawing selected text and other selected foreground elements.

Before this method is called, the font, text color, and pen color for
the snip’s style will have been set in the drawing context. (The
drawing context is not so configured for get-extent or partial-offset.) The draw method must
not make any other assumptions about the state of the drawing
context, except that the clipping region is already set to something
appropriate. Before draw returns, it must restore any
drawing context settings that it changes.

See also on-paint in editor<%>.

The snip’s editor is usually internally locked for
writing and reflowing when this method is called
(see also Internal Editor Locks), and it is normally in a refresh (see
Editors and Threads).

Default implementation:
Draws nothing.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-snip equal-to? snip equal?) → boolean? |
| snip: (is-a?/c snip%)                         |
| equal?: (-> any/c any/c boolean?)             |
+------------------------------------------------+
```

Specification: See equal<%>.

Default implementation: Calls the other-equal-to? method of snip
(to simulate multi-method dispatch) in case snip provides a
more specific equivalence comparison.

```
+------------------------------------------------------+
| [method]                                             |
|                                                      |
| (send a-snip other-equal-to? that equal?) → boolean? |
| that: (is-a?/c snip%)                               |
| equal?: (-> any/c any/c boolean?)                   |
+------------------------------------------------------+
```

Default implementation: Returns (eq?a-snipthat).

```
+-------------------------------------------------------------+
| [method]                                                    |
|                                                             |
| (send a-snip equal-hash-code-of hash-code) → exact-integer? |
| hash-code: (any/c. ->. exact-integer?)                   |
+-------------------------------------------------------------+
```

Specification: See equal<%>.

Default implementation: Returns (eq-hash-codea-snip).

```
+------------------------------------------------------+
| [method]                                             |
|                                                      |
| (send a-snip equal-secondary-hash-code-of hash-code) |
| → exact-integer?                                     |
| hash-code: (any/c. ->. exact-integer?)            |
+------------------------------------------------------+
```

Specification: See equal<%>.

Default implementation: Returns 1.

```
+---------------------------------------------------------------+
| [method]                                                      |
|                                                               |
| (send a-snip find-scroll-step y) → exact-nonnegative-integer? |
| y: real?                                                     |
+---------------------------------------------------------------+
```

Specification:
If a snip contains more than one vertical scroll step (see
get-num-scroll-steps) then this method is called to
find a scroll step offset for a given y-offset into the snip.

Default implementation:
Returns 0.

```
+-----------------------------------------------------------+
| [method]                                                  |
|                                                           |
| (send a-snip get-admin) → (or/c (is-a?/c snip-admin%) #f) |
+-----------------------------------------------------------+
```

Returns the administrator for this snip. (The administrator can be
#f even if the snip is owned but not visible in the editor.)

```
+------------------------------------------------------+
| [method]                                             |
|                                                      |
| (send a-snip get-count) → exact-nonnegative-integer? |
+------------------------------------------------------+
```

Returns the snip’s count (i.e., number of items
within the snip).

```
+---------------------------------------------------------------+
| [method]                                                      |
|                                                               |
| (send a-snip get-grapheme-count) → exact-nonnegative-integer? |
+---------------------------------------------------------------+
```

Returns the number of graphemes in the snip, which is
usually the same result as get-count, but can be
smaller with multiple consecutive items form a grapheme.

Added in version 1.4 of package `snip-lib`.

```
+----------------------------------------------------------------+
| [method]                                                       |
|                                                                |
| (send a-snip grapheme-position n) → exact-nonnegative-integer? |
| n: exact-nonnegative-integer?                                 |
+----------------------------------------------------------------+
```

Returns the number of items in the snip that form the first
n graphemes; or, equivalently, converts from an
grapheme-based position to a item-based position.

When get-count is the same as get-grapheme-count, this method returns n.

Added in version 1.4 of package `snip-lib`.

```
+------------------------------------------------------------------+
| [method]                                                         |
|                                                                  |
| (send a-snip get-extent                                          |
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

Specification:
Calculates the snip’s width, height, descent (amount of height which
is drawn below the baseline), space (amount of height which is
“filler” space at the top), and horizontal spaces (amount of width
which is “filler” space at the left and right). Those values are
returned by filling the w, h, descent,
space, lspace, and rspace boxes.

This method is called by the snip’s administrator; it is not normally
called directly by others. To get the extent of a snip, use
get-snip-location in editor<%>.

A drawing context is provided for the purpose of finding font sizes,
but no drawing should occur. The get-extent and
partial-offset methods must not make any assumptions
about the state of the drawing context, except that it is scaled
properly. In particular, the font for the snip’s style is not
automatically set in the drawing context before the method is
called. (Many snips cache their size information, so
automatically setting the font would be wasteful.) If get-extent or partial-offset changes the drawing
context’s setting, it must restore them before returning. However,
the methods should not need to change the drawing context; only font
settings can affect measurement results from a device context, and
get-text-extent in dc<%> accepts a font% argument for
sizing that overrides that device context’s current font.

The snip’s left and top locations are provided as x
and y in editor coordinates, in case the snip’s size depends
on its location; the x and y arguments are usually
ignored. In a text editor, the y-coordinate is the line’s
top location; the snip’s actual top location is
potentially undetermined until its height is known.

If a snip caches the result size for future replies, it should
invalidate its cached size when size-cache-invalid is
called (especially if the snip’s size depends on any device context
properties).

If a snip’s size changes after receiving a call to
get-extent and before receiving a call to
size-cache-invalid, then the snip must notify its administrator of the size change, so
that the administrator can recompute its derived size information.
Notify the administrator of a size change by call its
resized method.

The snip’s editor is usually internally locked for writing and
reflowing when this method is called (see also Internal Editor Locks).

Default implementation:
Fills in all boxes with 0.0.

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send a-snip get-flags) → (listof symbol?) |
+--------------------------------------------+
```

Returns flags defining the behavior of the snip, a list of the
following symbols:

- 'is-text — this is a text snip derived from
string-snip%; do not set this flag
- 'can-append — this snip can be merged with
another snip of the same type
- 'invisible — an invisible snip
that the user doesn’t see, such as a newline
- 'hard-newline — a newline must follow the snip
- 'newline — a newline currently follows the
snip; only an owning editor should set this flag
- 'handles-events — this snip can handle
keyboard and mouse events when it has the keyboard focus
- 'handles-all-mouse-events — this snip can
handle mouse events that touch the snip or that immediately
follow an event that touches the snip, even if the snip does
not have the keyboard focus (see also
on-goodbye-event)
- 'handles-between-events — this snip handles
mouse events that are between items in the snip
(instead of defaulting to treating mouse clicks as
setting the position or other event handling that happens
at the text% or pasteboard% level)
- 'width-depends-on-x — this snip’s display
width depends on the snip’s x-location within the
editor; e.g.: tab
- 'height-depends-on-y — this snip’s display
height depends on the snip’s y-location within the editor
- 'width-depends-on-y — this snip’s display
width depends on the snip’s y-location within the editor
- 'height-depends-on-x — this snip’s display
height depends on the snip’s x-location within the editor
- 'uses-editor-path — this snip uses its
editor’s pathname and should be notified when the name changes;
notification is given as a redundant call to set-admin

```
+------------------------------------+
| [method]                           |
|                                    |
| (send a-snip get-num-scroll-steps) |
| → exact-nonnegative-integer?       |
+------------------------------------+
```

Specification:
Returns the number of horizontal scroll steps within the snip. For
most snips, this is 1. Embedded editor snips use this method so that
scrolling in the owning editor will step through the lines in the
embedded editor.

Default implementation:
Returns 1.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-snip get-scroll-step-offset offset) |
| → (and/c real? (not/c negative?))           |
| offset: exact-nonnegative-integer?         |
+---------------------------------------------+
```

Specification: If a snip contains more than one vertical scroll step (see
get-num-scroll-steps) then this method is called to
find the y-offset into the snip for a given scroll offset.

Default implementation:
Returns 0.0.

```
+---------------------------------------------------------------+
| [method]                                                      |
|                                                               |
| (send a-snip get-snipclass) → (or/c #f (is-a?/c snip-class%)) |
+---------------------------------------------------------------+
```

Returns the snip’s class, which is used for file saving and
cut-and-paste.

Since this method returns the snip class stored by set-snipclass, it is not meant to be overridden.

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-snip get-style) → (is-a?/c style<%>) |
+----------------------------------------------+
```

Returns the snip’s style. See also set-style.

```
+----------------------------------------------------------+
| [method]                                                 |
|                                                          |
| (send a-snip get-text offset num [flattened?]) → string? |
| offset: exact-nonnegative-integer?                      |
| num: exact-nonnegative-integer?                         |
| flattened?: any/c = #f                                  |
+----------------------------------------------------------+
```

Specification:
Returns the text for this snip starting with the position
offset within the snip, and continuing for a total length of
num items. If offset is greater than the snip’s
count, then "" is returned. If num is greater than the
snip’s count minus the offset, then text from the offset to the end
of the snip is returned.

If flattened? is not #f, then flattened text is returned.
See Flattened Text for a discussion of flattened vs. non-flattened
text.

Default implementation:
Returns "".

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-snip get-text!                      |
| buffer: (and/c string? (not/c immutable?)) |
| offset: exact-nonnegative-integer?         |
| num: exact-nonnegative-integer?            |
| buffer-offset: exact-nonnegative-integer?  |
+---------------------------------------------+
```

Specification:
Like get-text in non-flattened mode, except that the
characters are put into the given mutable string, instead of returned
in a newly allocated string.

The buffer string is filled starting at position
buffer-offset. The buffer string must be at least
num+buffer-offset characters long.

Default implementation:
Calls get-text, except in the case of a
string-snip%, in which case buffer is filled
directly.

```
+------------------------------------+
| [method]                           |
|                                    |
| (send a-snip is-owned?) → boolean? |
+------------------------------------+
```

Returns #t if this snip has an owner, #f otherwise.
Note that a snip may be owned by an editor if it was inserted and
then deleted from the editor, if it’s still in the editor’s undo
history.

```
+--------------------------------------+
| [method]                             |
|                                      |
| (send a-snip match? snip) → boolean? |
| snip: (is-a?/c snip%)               |
+--------------------------------------+
```

Specification:
Return #t if a-snip “matches” snip,
#f otherwise.

Default implementation:
Returns #t if the snip and a-snip are from the
same class and have the same length.

```
+-----------------------------------------------------------+
| [method]                                                  |
|                                                           |
| (send a-snip merge-with prev) → (or/c (is-a?/c snip%) #f) |
| prev: (is-a?/c snip%)                                    |
+-----------------------------------------------------------+
```

Specification:
Merges a-snip with prev, returning #f if the
snips cannot be merged or a new merged snip otherwise. This method
will only be called if both snips are from the same class and both
have the 'can-append flag.

If the returned snip does not have the expected count, its
count is forcibly modified. If the returned snip is
already owned by another administrator, a surrogate snip is created.

The snip’s editor is usually internally locked for reading when this
method is called (see also Internal Editor Locks).

Default implementation:
Returns #f.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-snip next) → (or/c (is-a?/c snip%) #f) |
+------------------------------------------------+
```

Returns the next snip in the editor owning this snip, or #f
if this is the last snip.

In a text editor, the next snip is the snip at the position
following this snip’s (last) position. In a pasteboard,
the next snip is the one immediately behind this
snip. (See Editor Structure and Terminology for information about snip order in pasteboards.)

```
+------------------------------+
| [method]                     |
|                              |
| (send a-snip on-char         |
| dc: (is-a?/c dc<%>)         |
| x: real?                    |
| y: real?                    |
| editorx: real?              |
| editory: real?              |
| event: (is-a?/c key-event%) |
+------------------------------+
```

Specification:
Called to handle keyboard events when this snip has the keyboard focus
and can handle events. The drawing context is provided, as well as
the snip’s location in display coordinates (the
event uses display coordinates), and the snip’s
location in editor coordinates.

The x and y arguments are the snip’s
location in display coordinates. The
editorx and editory arguments are the snip’s
location in editor coordinates. To get event’s x
location in snip coordinates, subtract x from
(sendeventget-x).

See also 'handles-events in get-flags.

Default implementation:
Does nothing.

```
+--------------------------------+
| [method]                       |
|                                |
| (send a-snip on-event          |
| dc: (is-a?/c dc<%>)           |
| x: real?                      |
| y: real?                      |
| editorx: real?                |
| editory: real?                |
| event: (is-a?/c mouse-event%) |
+--------------------------------+
```

Specification:
Called to handle mouse events on the snip when this snip can handle
events and when the snip has the keyboard focus. See on-char for information about the arguments.

The x and y arguments are the snip’s
location in display coordinates. The
editorx and editory arguments are the snip’s
location in editor coordinates. To get event’s x
location in snip coordinates, subtract x from
(sendeventget-x).

See also 'handles-events in get-flags.

Default implementation:
Does nothing.

```
+--------------------------------+
| [method]                       |
|                                |
| (send a-snip on-goodbye-event  |
| dc: (is-a?/c dc<%>)           |
| x: real?                      |
| y: real?                      |
| editorx: real?                |
| editory: real?                |
| event: (is-a?/c mouse-event%) |
+--------------------------------+
```

Specification:
Called to handle an event that is really aimed at another
snip in order to give this snip a chance to clean up
as the mouse moves away. The arguments are the same
as on-event.

This method is called only when the snip has the
'handles-all-mouse-events flag set
(see get-flags and set-flags).

Default implementation:
Calls this object’s on-event method

Added in version 1.1 of package `snip-lib`.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-snip own-caret own-it?) → void? |
| own-it?: any/c                         |
+-----------------------------------------+
```

Specification:
Notifies the snip that it is or is not allowed to display the caret
(indicating ownership of keyboard focus) in some
display. This method is not called to request
that the caret is actually shown or hidden; the draw
method is called for all display requests.

The own-it? argument is #t if the snip owns the
keyboard focus or #f otherwise.

Default implementation:
Does nothing.

```
+----------------------------------------------------------------+
| [method]                                                       |
|                                                                |
| (send a-snip position-grapheme n) → exact-nonnegative-integer? |
| n: exact-nonnegative-integer?                                 |
+----------------------------------------------------------------+
```

Returns the number of graphemes within the snip formed by the
first n items; or, equivalently, converts from an
item-based position to a grapheme-based position.

When get-count is the same as get-grapheme-count, this method returns n.

Added in version 1.4 of package `snip-lib`.

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-snip partial-offset dc x y len) → real? |
| dc: (is-a?/c dc<%>)                            |
| x: real?                                       |
| y: real?                                       |
| len: exact-nonnegative-integer?                |
+-------------------------------------------------+
```

Specification:
Calculates a partial width for the snip, starting from the first snip
item and continuing for len items. The
drawing context and snip’s locations in editor coordinates
are provided. See also get-extent.

The snip’s editor is usually internally locked for writing and
reflowing when this method is called (see also Internal Editor Locks).

Default implementation:
Returns 0.0.

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-snip previous) → (or/c (is-a?/c snip%) #f) |
+----------------------------------------------------+
```

Returns the previous snip in the editor owning this snip, or #f if this
is the first snip.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-snip release-from-owner) → boolean? |
+---------------------------------------------+
```

Specification:
Asks the snip to try to release itself from its owner. If the snip is
not owned or the release is successful, then #t is
returned. Otherwise, #f is returned and the snip remains
owned. See also is-owned?.

Use this method for moving a snip from one editor to another. This
method notifies the snip’s owning editor that someone else really
wants control of the snip. It is not necessary to use this method for
"cleaning up" a snip when it is deleted from an editor.

Default implementation:
Requests a low-level release from the snip’s owning administrator.

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-snip resize w h) → boolean? |
| w: (and/c real? (not/c negative?)) |
| h: (and/c real? (not/c negative?)) |
+-------------------------------------+
```

Specification:
Resizes the snip. The snip can refuse to be resized by returning
#f. Otherwise, the snip will resize (it must call its
administrator’s resized method) and return
#t.

See also on-interactive-resize in pasteboard%.

Default implementation:
Returns #f.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-snip set-admin admin) → void?   |
| admin: (or/c (is-a?/c snip-admin%) #f) |
+-----------------------------------------+
```

Sets the snip’s administrator. Only an administrator should call this
method.

The default method sets the internal state of a snip to record its
administrator. It will not modify this state if the snip is already
owned by an administrator and the administrator has not blessed the
transition. If the administrator state of a snip is not modified as
expected during a sensitive call to this method by an instance of
text% or pasteboard%, the
internal state may be forcibly modified (if the new administrator was
#f) or a surrogate snip may be created (if the snip was
expected to receive a new administrator).

The snip’s (new) editor is usually internally locked for reading when
this method is called (see also Internal Editor Locks).

```
+-----------------------------------+
| [method]                          |
|                                   |
| (send a-snip set-count c) → void? |
| c: (integer-in 1 100000)         |
+-----------------------------------+
```

Specification:
Sets the snip’s count (i.e., the number of items
within the snip) to (max1c). The snip’s grapheme count is
set to be equal to its character count.

The snip’s count may be changed by the system (in extreme
cases to maintain consistency) without calling this method or
set-char-and-grapheme-count.

Default implementation:
Sets the snip’s count and notifies the snip’s administrator
that the snip’s size has changed.

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send a-snip set-char-and-grapheme-count |
| char-c: exact-nonnegative-integer?      |
| grapheme-c: exact-nonnegative-integer?  |
+------------------------------------------+
```

Specification:
Sets the snip’s count to (max1char-c) and its
grapheme count to (max1grapheme-c).

The snip’s count may be changed by the system (in extreme cases to
maintain consistency) without calling this method or set-count.

Default implementation: Sets the snip’s count and notifies the snip’s administrator
that the snip’s size has changed.

Added in version 1.4 of package `snip-lib`.

```
+---------------------------------------+
| [method]                              |
|                                       |
| (send a-snip set-flags flags) → void? |
| flags: (listof symbol?)              |
+---------------------------------------+
```

Specification:
Sets the snip’s flags. See get-flags.

Default implementation:
Sets the snip flags and notifies the snip’s editor that its flags have
changed.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-snip set-snipclass class) → void? |
| class: (is-a?/c snip-class%)             |
+-------------------------------------------+
```

Sets the snip’s class, used for file saving and cut-and-paste.

This method stores the snip class internally; other editor objects may
access the snip class directly, instead of through the get-snipclass method.

```
+---------------------------------------+
| [method]                              |
|                                       |
| (send a-snip set-style style) → void? |
| style: (is-a?/c style<%>)            |
+---------------------------------------+
```

Sets the snip’s style if it is not owned by any editor. See also
get-style and is-owned?.

The snip’s style may be changed by the system without calling this method.

```
+--------------------------------------+
| [method]                             |
|                                      |
| (send a-snip set-unmodified) → void? |
+--------------------------------------+
```

Specification:
Called by the snip’s administrator to notify the snip that its changed
have been saved. The next time snip’s internal state is modified by
the user, it should call modified to report the
state change (but only on the first change after this method is
called, or the first change after the snip acquires a new
administrator).

Default implementation:
Does nothing.

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send a-snip size-cache-invalid) → void? |
+------------------------------------------+
```

Specification:
Called to notify the snip that it may need to recalculate its display
arguments (width, height, etc.) when it is next asked, because the
style or location of the snip has changed.

The snip’s (new) editor is usually internally locked for reflowing
when this method is called (see also Internal Editor Locks).

Default implementation:
Does nothing.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send a-snip split position first second) → void? |
| position: exact-nonnegative-integer?             |
| first: (box/c (is-a?/c snip%))                   |
| second: (box/c (is-a?/c snip%))                  |
+---------------------------------------------------+
```

Specification: Splits the snip into two snips. This is called when a snip has more
than one item and something is inserted between two
items.

The arguments are a relative position integer and two
boxes. The position integer specifies how many
items should be given to the new first snip; the rest go
to the new second snip. The two boxes must be filled with two new
snips. (The old snip is no longer used, so it can be recycled as a
new snip.)

If the returned snips do not have the expected counts, their
counts are forcibly modified. If either returned snip is already
owned by another administrator, a surrogate snip is created.

The snip’s editor is usually internally locked for reading when this
method is called (see also Internal Editor Locks).

Default implementation:
Creates a new snip% instance with position
elements, and modifies a-snip to decrement its count by
position. The nest snip is installed into first and
a-snip is installed into second.

```
+----------------------------------+
| [method]                         |
|                                  |
| (send a-snip write f) → void?    |
| f: (is-a?/c editor-stream-out%) |
+----------------------------------+
```

Writes the snip to the given stream. (Snip reading is handled by the
snip class.) Style information about the snip (i.e., the content of
get-style) will be saved and restored automatically.
