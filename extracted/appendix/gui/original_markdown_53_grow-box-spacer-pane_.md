<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/grow-box-spacer-pane_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/grow-box-spacer-pane_.html -->
<!-- Canonical English source for Japanese translation -->

```
+-------------------------------------+
| classgrow-box-spacer-pane%: class? |
+-------------------------------------+
| superclass: pane%                   |
+-------------------------------------+
```

A grow-box-spacer-pane% object is intended for use as a
lightweight spacer in the bottom-right corner of a frame, rather than
as a container. On older version of Mac OS, a
grow-box-spacer-pane% has the same width and height as the
grow box that is inset into the bottom-right corner of a frame. On
Windows, Unix, and recent Mac OS, a grow-box-spacer-pane% has zero width and
height. Unlike all other container types, a
grow-box-spacer-pane% is unstretchable by default.

```
+---------------------------------------------------+
| [constructor]                                     |
|                                                   |
| (new grow-box-spacer-pane%...superclass-args...) |
| → (is-a?/c grow-box-spacer-pane%)                 |
+---------------------------------------------------+
```

See pane% for information on initialization arguments.
