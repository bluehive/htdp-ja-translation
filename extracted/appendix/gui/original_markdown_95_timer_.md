<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/timer_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/timer_.html -->
<!-- Canonical English source for Japanese translation -->

```
+----------------------+
| classtimer%: class? |
+----------------------+
| superclass: object%  |
+----------------------+
```

A timer% object encapsulates an event-based alarm. To use a
timer, either instantiate it with a timer-callback thunk to
perform the alarm-based action, or derive a new class and override
the notify method to perform the alarm-based
action. Start a timer with start and stop it with
stop. Supplying an initial interval (in
milliseconds) when creating a timer also starts the timer.

Timers have a relatively high priority in the event queue. Thus, if
the timer delay is set low enough, repeated notification for a timer
can preempt user activities (which might be directed at stopping the
timer). For timers with relatively short delays, call yield
within the notify procedure to allow guaranteed event
processing.

See Event Dispatching and Eventspaces for more information about event
priorities.

```
+-----------------------------------------------------+
| [constructor]                                       |
|                                                     |
| (new timer%                                         |
| → (is-a?/c timer%)                                  |
| notify-callback: (-> any) = void                   |
| interval: (or/c (integer-in 0 1000000000) #f) = #f |
| just-once?: any/c = #f                             |
+-----------------------------------------------------+
```

The notify-callback thunk is called by the default
notify method when the timer expires.

If interval is #f (the default), the timer is not
started; in that case, start must be called
explicitly. If interval is a number (in milliseconds), then
start is called with interval and
just-once?.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-timer interval) → (integer-in 0 1000000000) |
+-----------------------------------------------------+
```

Returns the number of milliseconds between each timer expiration (when
the timer is running).

```
+-------------------------------+
| [method]                      |
|                               |
| (send a-timer notify) → void? |
+-------------------------------+
```

Specification:
Called (on an event boundary) when the timer’s alarm expires.

Default implementation:
Calls the notify-callback procedure that was provided when the
object was created.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-timer start msec [just-once?]) → void? |
| msec: (integer-in 0 1000000000)               |
| just-once?: any/c = #f                        |
+------------------------------------------------+
```

Starts (or restarts) the timer. If the timer is already running, its alarm time is not changed.

The timer’s alarm expires after msec milliseconds, at which point
notify is called (on an event boundary). If
just-once? is true, the timer calls its notify
callback when the alarm expires and the timer is stopped. If
just-once? is #f, the timer is re-started when the notify
callback returns; it stops only once stop is called explicitly.

```
+-----------------------------+
| [method]                    |
|                             |
| (send a-timer stop) → void? |
+-----------------------------+
```

Stops the timer. A stopped timer never calls
notify. If the timer has expired but the call to
notify has not yet been dispatched, the call is removed from the event queue.
