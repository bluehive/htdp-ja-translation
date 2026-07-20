<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/event_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/event_.html -->
<!-- Canonical English source for Japanese translation -->

```
+-----------------------------+--------------------+
|  (require racket/gui/event) | package: `gui-lib` |
+-----------------------------+--------------------+
+-----------------------------+--------------------+
```

The bindings documented in this section are also provided by the
racket/gui/base library.

Changed in version 7.3.0.1 of package `gui-lib`: Added racket/gui/event
that exports event% and
subclasses.

```
+----------------------+
| classevent%: class? |
+----------------------+
| superclass: object%  |
+----------------------+
```

An event% object contains information about a control,
keyboard, mouse, or scroll event. See also
control-event%,
key-event%,
mouse-event%, and
scroll-event%.

```
+-----------------------------------------------------------+
| [constructor]                                             |
|                                                           |
| (new event% [[time-stamp time-stamp]]) → (is-a?/c event%) |
| time-stamp: exact-integer? = 0                           |
| time: exact-integer?                                     |
+-----------------------------------------------------------+
```
