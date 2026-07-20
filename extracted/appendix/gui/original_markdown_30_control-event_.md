<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/control-event_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/control-event_.html -->
<!-- Canonical English source for Japanese translation -->

```
+------------------------------+
| classcontrol-event%: class? |
+------------------------------+
| superclass: event%           |
+------------------------------+
```

A control-event% object contains information about a
control event. An instance of control-event% is always
provided to a control or menu item callback procedure.

```
+--------------------------------------------------------------------------+
| [constructor]                                                            |
|                                                                          |
| (new control-event%                                                      |
| → (is-a?/c control-event%)                                               |
| event-type: (or/c 'button 'check-box 'choice 'list-box 'list-box-dclick |
| 'list-box-column 'text-field 'text-field-enter 'menu 'slider 'radio-box  |
| 'tab-panel 'menu-popdown 'menu-popdown-none)                             |
| (or/c 'button 'check-box 'choice                                         |
| 'list-box 'list-box-dclick 'list-box-column                              |
| 'text-field 'text-field-enter                                            |
| 'menu 'slider 'radio-box 'tab-panel                                      |
| 'menu-popdown 'menu-popdown-none)                                        |
| time-stamp: exact-integer? = 0                                          |
|                                                                          |
| ```racket                                                                |
| (or/c 'button 'check-box 'choice                                         |
|       'list-box 'list-box-dclick 'list-box-column                        |
|       'text-field 'text-field-enter                                      |
|       'menu 'slider 'radio-box 'tab-panel                                |
|       'menu-popdown 'menu-popdown-none)                                  |
| ```                                                                      |
+--------------------------------------------------------------------------+
```

The event-type argument is one of the following:

- 'button — for button% clicks
- 'check-box — for check-box% toggles
- 'choice — for choice% item selections
- 'list-box — for list-box% selections and deselections
- 'list-box-dclick — for list-box% double-clicks
- 'list-box-column — for list-box% column clicks in
a column-control-event% instance
- 'text-field — for text-field% changes
- 'text-field-enter — for single-line text-field% Enter event
- 'menu — for selectable-menu-item<%> callbacks
- 'slider — for slider% changes
- 'radio-box — for radio-box% selection changes
- 'tab-panel — for tab-panel% tab changes
- 'menu-popdown — for popup-menu% callbacks (item selected)
- 'menu-popdown-none — for popup-menu% callbacks (no item selected)

This value is extracted out of a control-event% object with
the
get-event-type method.

See get-time-stamp for information about
time-stamp.

```
+-----------------------------------------------------------------------------+
| [method]                                                                    |
|                                                                             |
| (send a-control-event get-event-type)                                       |
| → (or/c 'button 'check-box 'choice 'list-box 'list-box-dclick 'text-field   |
| 'text-field-enter 'menu 'slider 'radio-box 'menu-popdown 'menu-popdown-none |
| 'tab-panel)                                                                 |
| (or/c 'button 'check-box 'choice                                            |
| 'list-box 'list-box-dclick 'text-field                                      |
| 'text-field-enter 'menu 'slider 'radio-box                                  |
| 'menu-popdown 'menu-popdown-none 'tab-panel)                                |
|                                                                             |
| ```racket                                                                   |
| (or/c 'button 'check-box 'choice                                            |
|       'list-box 'list-box-dclick 'text-field                                |
|       'text-field-enter 'menu 'slider 'radio-box                            |
|       'menu-popdown 'menu-popdown-none 'tab-panel)                          |
| ```                                                                         |
+-----------------------------------------------------------------------------+
```

Returns the type of the control event. See
control-event% for information about each event type symbol.

```
+--------------------------------------------------------------------------------+
| [method]                                                                       |
|                                                                                |
| (send a-control-event set-event-type type) → void?                             |
| type: (or/c 'button 'check-box 'choice 'list-box 'list-box-dclick 'text-field |
| 'text-field-enter 'menu 'slider 'radio-box 'menu-popdown 'menu-popdown-none    |
| 'tab-panel)                                                                    |
| (or/c 'button 'check-box 'choice                                               |
| 'list-box 'list-box-dclick 'text-field                                         |
| 'text-field-enter 'menu 'slider 'radio-box                                     |
| 'menu-popdown 'menu-popdown-none 'tab-panel)                                   |
|                                                                                |
| ```racket                                                                      |
| (or/c 'button 'check-box 'choice                                               |
|       'list-box 'list-box-dclick 'text-field                                   |
|       'text-field-enter 'menu 'slider 'radio-box                               |
|       'menu-popdown 'menu-popdown-none 'tab-panel)                             |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

Sets the type of the event. See
control-event% for information about each event type symbol.
