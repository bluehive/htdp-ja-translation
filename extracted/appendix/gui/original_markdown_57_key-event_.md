<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/key-event_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/key-event_.html -->
<!-- Canonical English source for Japanese translation -->

```
+--------------------------+
| classkey-event%: class? |
+--------------------------+
| superclass: event%       |
+--------------------------+
```

A key-event% object contains information about a key press
or release event. Key events are primarily processed by
on-subwindow-char in window<%> and
on-char in canvas<%>.

For a key-press event, a virtual key code is provided by
get-key-code. For a key-release event,
get-key-code reports 'release, and a virtual key code is provided by
get-key-release-code.

See also Mouse and Keyboard Events.

```
+--------------------------------------------------+
| [constructor]                                    |
|                                                  |
| (new key-event%                                  |
| → (is-a?/c key-event%)                           |
| key-code: (or/c char? key-code-symbol?) = #\nul |
| shift-down: any/c = #f                          |
| control-down: any/c = #f                        |
| meta-down: any/c = #f                           |
| alt-down: any/c = #f                            |
| x: exact-integer? = 0                           |
| y: exact-integer? = 0                           |
| time-stamp: exact-integer? = 0                  |
| caps-down: any/c = #f                           |
| mod3-down: any/c = #f                           |
| mod4-down: any/c = #f                           |
| mod5-down: any/c = #f                           |
| control+meta-is-altgr: any/c = #f               |
+--------------------------------------------------+
```

See the corresponding get- and set-
methods for information about key-code, shift-down,
control-down, meta-down, mod3-down, mod4-down,
mod5-down, alt-down, x, y,
time-stamp, caps-down, mod3-down,
mod4-down, mod5-down, and control+meta-is-altgr.

The release key code, as returned by get-key-release-code, is initialized to 'press.

Changed in version 1.1 of package `gui-lib`: Added mod3-down, mod4-down, and mod5-down.
Changed in version 1.2: Added control+meta-is-altgr.

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send a-key-event get-alt-down) → boolean? |
+--------------------------------------------+
```

Returns #t if the Option (Mac OS) key was down for
the event. When the Alt key is pressed in Windows, it is reported as
a Meta press (see
get-meta-down).

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-key-event get-caps-down) → boolean? |
+---------------------------------------------+
```

Returns #t if the Caps Lock key was on for the event.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-key-event get-control-down) → boolean? |
+------------------------------------------------+
```

Returns #t if the Control key was down for the event.

On Mac OS, if a Control-key press is combined with a mouse button
click, the event is reported as a right-button click and
get-control-down for the event reports #f.

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send a-key-event get-control+meta-is-altgr) → boolean? |
+---------------------------------------------------------+
```

Returns #t if a Control plus Meta event should be treated as
an AltGr event on Windows. By default, AltGr treatment applies if the
Control key was the left one and the Alt key (as Meta) was the right one—typed
that way on a keyboard with a right Alt key, or produced by a single
AltGr key. See also any-control+alt-is-altgr, which controls
whether other Control plus Alt combinations are treated as AltGr.

Added in version 1.2 of package `gui-lib`.

```
+---------------------------------+
| [method]                        |
|                                 |
| (send a-key-event get-key-code) |
| → (or/c char? key-code-symbol?) |
+---------------------------------+
```

Gets the virtual key code for the key event. The virtual key code is
either a character or a special key symbol, one of the following:

- 'start
- 'cancel
- 'clear
- 'shift — Shift key
- 'rshift — right Shift key
- 'control — Control key
- 'rcontrol — right Control key
- 'menu
- 'pause
- 'capital
- 'prior
- 'next
- 'end
- 'home
- 'left
- 'up
- 'right
- 'down
- 'escape
- 'select
- 'print
- 'execute
- 'snapshot
- 'insert
- 'help
- 'numpad0
- 'numpad1
- 'numpad2
- 'numpad3
- 'numpad4
- 'numpad5
- 'numpad6
- 'numpad7
- 'numpad8
- 'numpad9
- 'numpad-enter
- 'multiply
- 'add
- 'separator
- 'subtract
- 'decimal
- 'divide
- 'f1
- 'f2
- 'f3
- 'f4
- 'f5
- 'f6
- 'f7
- 'f8
- 'f9
- 'f10
- 'f11
- 'f12
- 'f13
- 'f14
- 'f15
- 'f16
- 'f17
- 'f18
- 'f19
- 'f20
- 'f21
- 'f22
- 'f23
- 'f24
- 'numlock
- 'scroll
- 'wheel-up — mouse wheel up; see get-wheel-steps
- 'wheel-down — mouse wheel down; see get-wheel-steps
- 'wheel-left — mouse wheel left; see get-wheel-steps
- 'wheel-right — mouse wheel right; see get-wheel-steps
- 'release — indicates a key-release event
- 'press — indicates a key-press event; usually only from get-key-release-code

The special key symbols attempt to capture useful keys that have no
standard ASCII representation. A few keys have standard
representations that are not obvious:

- #\space — the space bar
- #\return — the Enter or Return key (on all
platforms), but not necessarily the Enter key near the numpad
(which is reported as 'numpad-enter Unix and Mac OS)
- #\tab — the tab key
- #\backspace — the backspace key
- #\rubout — the delete key

If a suitable special key symbol or ASCII representation is not
available, #\nul (the NUL character) is reported.

A 'wheel-up, 'wheel-down, 'wheel-left, or
'wheel-right event may be sent to a window other than the
one with the keyboard focus, because some platforms generate wheel
events based on the location of the mouse pointer instead of the
keyboard focus.

On Windows, when the Control key is pressed without Alt, the key
code for ASCII characters is downcased, roughly cancelling the effect
of the Shift key. On Mac OS, the key code is computed without
Caps Lock effects when the Control or Command key is pressed; in the
case of Control, Caps Lock is used normally if special handling is
disabled for the Control key via special-control-key. On
Unix, the key code is computed with Caps Lock effects when the Control
key is pressed without Alt.

See also get-other-shift-key-code.

Changed in version 6.1.0.8 of package `gui-lib`: Changed reporting of numpad Enter
to 'numpad-enter as
documented, instead of
#\u0003.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-key-event get-key-release-code) |
| → (or/c char? key-code-symbol?)         |
+-----------------------------------------+
```

Gets the virtual key code for a key-release event; the result is
'press for a key-press event. See get-key-code for the list of virtual key codes.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-key-event get-meta-down) → boolean? |
+---------------------------------------------+
```

Returns #t if the Meta (Unix), Alt (Windows), or Command (Mac OS) key was down for the event.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-key-event get-mod3-down) → boolean? |
+---------------------------------------------+
```

Returns #t if the Mod3 (Unix) key was down for the event.

Added in version 1.1 of package `gui-lib`.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-key-event get-mod4-down) → boolean? |
+---------------------------------------------+
```

Returns #t if the Mod4 (Unix) key was down for the event.

Added in version 1.1 of package `gui-lib`.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-key-event get-mod5-down) → boolean? |
+---------------------------------------------+
```

Returns #t if the Mod5 (Unix) key was down for the event.

Added in version 1.1 of package `gui-lib`.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-key-event get-other-altgr-key-code) |
| → (or/c char? key-code-symbol? #f)          |
+---------------------------------------------+
```

See get-other-shift-key-code.

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send a-key-event get-other-caps-key-code) |
| → (or/c char? key-code-symbol? #f)         |
+--------------------------------------------+
```

See get-other-shift-key-code.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send a-key-event get-other-shift-altgr-key-code) |
| → (or/c char? key-code-symbol? #f)                |
+---------------------------------------------------+
```

See get-other-shift-key-code.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-key-event get-other-shift-key-code) |
| → (or/c char? key-code-symbol? #f)          |
+---------------------------------------------+
```

Since keyboard mappings vary, it is sometimes useful in key mappings
for a program to know the result that the keyboard would have
produced for an event if the Shift key had been toggled
differently. The get-other-shift-key-code
produces that other mapping, returning #f if the alternate
mapping is unavailable, otherwise returning the same kind of result
as get-key-code.

The get-other-altgr-key-code method provides the
same information with respect to the AltGr key (i.e., Alt combined
with Control) on Windows and Unix, or the Option key on Mac OS. The get-other-shift-altgr-key-code method
reports a mapping for in tha case that both Shift and AltGr/Option
were different from the actual event.

The get-other-shift-key-code, get-other-altgr-key-code, and get-other-shift-altgr-key-code results all report key mappings where
Caps Lock is off, independent of whether Caps Lock was on for the
actual event. The get-other-caps-key-code method
reports a mapping for in that case that the Caps Lock state was
treated opposite as for the get-key-code
result. (Caps Lock normally has either no effect or the same effect as
Shift, so further combinations involving Caps Lock and other modifier
keys would not normally produce further alternatives.)

Alternate mappings are not available for all events. On Windows,
alternate mappings are reported when they produce ASCII letters,
ASCII digits, and ASCII symbols. On Mac OS and Unix, alternate
mappings are usually available.

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-key-event get-shift-down) → boolean? |
+----------------------------------------------+
```

Returns #t if the Shift key was down for the event.

```
+--------------------------------------------------------+
| [method]                                               |
|                                                        |
| (send a-key-event get-wheel-steps) → nonnegative-real? |
+--------------------------------------------------------+
```

Returns the number of wheel steps represented by a 'wheel-up,
'wheel-down, 'wheel-left, or 'wheel-right
event. For a system-generated event, the value is always positive for
a wheel event, and it is always 0.0 for other events. The
initial value for a newly created key-event% is 0.0.

See also wheel-event-mode in window<%>.

Added in version 1.43 of package `gui-lib`.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-key-event get-x) → exact-integer? |
+-------------------------------------------+
```

Returns the x-position of the mouse at the time of the event, in the
target’s window’s (client-area) coordinate system.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-key-event get-y) → exact-integer? |
+-------------------------------------------+
```

Returns the y-position of the mouse at the time of the event in the
target’s window’s (client-area) coordinate system.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-key-event set-alt-down down?) → void? |
| down?: any/c                                 |
+-----------------------------------------------+
```

Sets whether the Option (Mac OS) key was down for the event. When
the Alt key is pressed in Windows, it is reported as a Meta press
(see set-meta-down).

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-key-event set-caps-down down?) → void? |
| down?: any/c                                  |
+------------------------------------------------+
```

Sets whether the Caps Lock key was on for the event.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send a-key-event set-control-down down?) → void? |
| down?: any/c                                     |
+---------------------------------------------------+
```

Sets whether the Control key was down for the event.

On Mac OS, if a control-key press is combined with a mouse button
click, the event is reported as a right-button click and
get-control-down for the event reports
#f.

```
+------------------------------------------------------------+
| [method]                                                   |
|                                                            |
| (send a-key-event set-control+meta-is-altgr down?) → void? |
| down?: any/c                                              |
+------------------------------------------------------------+
```

Sets whether a Control plus Meta combination on Windows should be
treated as an AltGr combinations. See get-control+meta-is-altgr.

Added in version 1.2 of package `gui-lib`.

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-key-event set-key-code code) → void? |
| code: (or/c char? key-code-symbol?)         |
+----------------------------------------------+
```

Sets the virtual key code for the event, either a character or one of
the special symbols listed with get-key-code.

```
+------------------------------------------------------+
| [method]                                             |
|                                                      |
| (send a-key-event set-key-release-code code) → void? |
| code: (or/c char? key-code-symbol?)                 |
+------------------------------------------------------+
```

Sets the virtual key code for a release event, either a character or
one of the special symbols listed with get-key-code. See also get-key-release-code.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-key-event set-meta-down down?) → void? |
| down?: any/c                                  |
+------------------------------------------------+
```

Sets whether the Meta (Unix), Alt (Windows), or Command (Mac OS) key
was down for the event.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-key-event set-mod3-down down?) → void? |
| down?: any/c                                  |
+------------------------------------------------+
```

Sets whether the Mod3 (Unix) key was down for the event.

Added in version 1.1 of package `gui-lib`.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-key-event set-mod4-down down?) → void? |
| down?: any/c                                  |
+------------------------------------------------+
```

Sets whether the Mod4 (Unix) key was down for the event.

Added in version 1.1 of package `gui-lib`.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-key-event set-mod5-down down?) → void? |
| down?: any/c                                  |
+------------------------------------------------+
```

Sets whether the Mod5 (Unix) key was down for the event.

Added in version 1.1 of package `gui-lib`.

```
+----------------------------------------------------------+
| [method]                                                 |
|                                                          |
| (send a-key-event set-other-altgr-key-code code) → void? |
| code: (or/c char? key-code-symbol? #f)                  |
+----------------------------------------------------------+
```

Sets the key code produced by get-other-altgr-key-code.

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send a-key-event set-other-caps-key-code code) → void? |
| code: (or/c char? key-code-symbol? #f)                 |
+---------------------------------------------------------+
```

Sets the key code produced by get-other-caps-key-code.

```
+----------------------------------------------------------------+
| [method]                                                       |
|                                                                |
| (send a-key-event set-other-shift-altgr-key-code code) → void? |
| code: (or/c char? key-code-symbol? #f)                        |
+----------------------------------------------------------------+
```

Sets the key code produced by get-other-shift-altgr-key-code.

```
+----------------------------------------------------------+
| [method]                                                 |
|                                                          |
| (send a-key-event set-other-shift-key-code code) → void? |
| code: (or/c char? key-code-symbol? #f)                  |
+----------------------------------------------------------+
```

Sets the key code produced by get-other-shift-key-code.

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-key-event set-shift-down down?) → void? |
| down?: any/c                                   |
+-------------------------------------------------+
```

Sets whether the Shift key was down for the event.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-key-event set-wheel-steps steps) → void? |
| steps: nonnegative-real?                        |
+--------------------------------------------------+
```

Sets the number of steps for a wheel event. See get-wheel-steps.

Added in version 1.43 of package `gui-lib`.

```
+--------------------------------------+
| [method]                             |
|                                      |
| (send a-key-event set-x pos) → void? |
| pos: exact-integer?                 |
+--------------------------------------+
```

Sets the x-position of the mouse at the time of the event in the
target’s window’s (client-area) coordinate system.

```
+--------------------------------------+
| [method]                             |
|                                      |
| (send a-key-event set-y pos) → void? |
| pos: exact-integer?                 |
+--------------------------------------+
```

Sets the y-position of the mouse at the time of the event in the
target’s window’s (client-area) coordinate system.
