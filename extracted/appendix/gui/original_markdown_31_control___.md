<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/control___.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/control___.html -->
<!-- Canonical English source for Japanese translation -->

```
+----------------------------------+--------------+
| interfacecontrol<%>: interface? |              |
+----------------------------------+--------------+
| implements:                      | subwindow<%> |
+----------------------------------+--------------+
```

The control<%> interface is implemented by the built-in
control window classes:

- message%
- button%
- check-box%
- slider%
- gauge%
- text-field%
- radio-box%
- choice%
- list-box%

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-control command event) → void? |
| event: (is-a?/c control-event%)       |
+----------------------------------------+
```

Calls the control’s callback function, passing on the given
control-event% object.
