<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/scroll-event_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/scroll-event_.html -->
<!-- Canonical English source for Japanese translation -->

```
+-----------------------------+
| classscroll-event%: class? |
+-----------------------------+
| superclass: event%          |
+-----------------------------+
```

A scroll-event% object contains information about a scroll
event. An instance of scroll-event% is always provided to
on-scroll.

See
get-event-type for a list of the scroll event types.

```
+-------------------------------------------------------------------------+
| [constructor]                                                           |
|                                                                         |
| (new scroll-event%                                                      |
| → (is-a?/c scroll-event%)                                               |
| event-type: (or/c 'top 'bottom 'line-up 'line-down 'page-up 'page-down |
| 'thumb) = 'thumb                                                        |
| (or/c 'top 'bottom 'line-up 'line-down                                  |
| 'page-up 'page-down 'thumb)                                             |
| direction: (or/c 'horizontal 'vertical) = 'vertical                    |
| position: dimension-integer? = 0                                       |
| time-stamp: exact-integer? = 0                                         |
|                                                                         |
| ```racket                                                               |
| (or/c 'top 'bottom 'line-up 'line-down                                  |
|       'page-up 'page-down 'thumb)                                       |
| ```                                                                     |
+-------------------------------------------------------------------------+
```

See the corresponding get- and set- methods for
information about event-type, direction, position,
and time-stamp.

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-scroll-event get-direction) |
| → (or/c 'horizontal 'vertical)      |
+-------------------------------------+
```

Gets the identity of the scrollbar that was modified by the event,
either the horizontal scrollbar or the vertical scrollbar, as
'horizontal or 'vertical, respectively. See also
set-direction.

```
+----------------------------------------------------------------------+
| [method]                                                             |
|                                                                      |
| (send a-scroll-event get-event-type)                                 |
| → (or/c 'top 'bottom 'line-up 'line-down 'page-up 'page-down 'thumb) |
| (or/c 'top 'bottom 'line-up 'line-down                               |
| 'page-up 'page-down 'thumb)                                          |
|                                                                      |
| ```racket                                                            |
| (or/c 'top 'bottom 'line-up 'line-down                               |
|       'page-up 'page-down 'thumb)                                    |
| ```                                                                  |
+----------------------------------------------------------------------+
```

Returns the type of the event, one of the following:

- 'top — user clicked a scroll-to-top button
- 'bottom — user clicked a scroll-to-bottom button
- 'line-up — user clicked an arrow to scroll up or left one step
- 'line-down — user clicked an arrow to scroll down or right one step
- 'page-up — user clicked an arrow to scroll up or left one page
- 'page-down — user clicked an arrow to scroll down or right one page
- 'thumb — user dragged the scroll position indicator

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send a-scroll-event get-position) → dimension-integer? |
+---------------------------------------------------------+
```

Returns the position of the scrollbar after the action triggering the
event. See also set-position.

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-scroll-event set-direction direction) → void? |
| direction: (or/c 'horizontal 'vertical)              |
+-------------------------------------------------------+
```

Sets the identity of the scrollbar that was modified by the event,
either the horizontal scrollbar or the vertical scrollbar, as
'horizontal or 'vertical, respectively. See also
get-direction.

```
+---------------------------------------------------------------------------+
| [method]                                                                  |
|                                                                           |
| (send a-scroll-event set-event-type type) → void?                         |
| type: (or/c 'top 'bottom 'line-up 'line-down 'page-up 'page-down 'thumb) |
| (or/c 'top 'bottom 'line-up 'line-down                                    |
| 'page-up 'page-down 'thumb)                                               |
|                                                                           |
| ```racket                                                                 |
| (or/c 'top 'bottom 'line-up 'line-down                                    |
|       'page-up 'page-down 'thumb)                                         |
| ```                                                                       |
+---------------------------------------------------------------------------+
```

Sets the type of the event. See get-event-type
for information about each event type.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-scroll-event set-position position) → void? |
| position: dimension-integer?                       |
+-----------------------------------------------------+
```

Records the position of the scrollbar after the action triggering the
event. (The scrollbar itself is unaffected). See also
get-position.
