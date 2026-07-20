<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/Init_Libraries.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/Init_Libraries.html -->
<!-- Canonical English source for Japanese translation -->

## 13 Init Libraries

```
+----------------------------+--------------------+
|  (require racket/gui/init) | package: `gui-lib` |
+----------------------------+--------------------+
+----------------------------+--------------------+
```

The
racket/gui/init library is the default start-up
library for GRacket. It re-exports the racket/init and
racket/gui/base libraries, and it sets
current-load to use text-editor-load-handler.

```
+-----------------------------------+--------------------+
|  (require racket/gui/interactive) | package: `gui-lib` |
+-----------------------------------+--------------------+
+-----------------------------------+--------------------+
```

Similar to racket/interactive, but for
GRacket. This library can be changed by modifying
'gui-interactive-file in the
`"config.rktd"` file in (find-config-dir).
Additionally, if the file `"gui-interactive.rkt"`
exists in (find-system-path'addon-dir), it is run
rather than the installation wide graphical interactive
module.

This library runs the
(find-graphical-system-path'init-file) file in
the users home directory if it exists, rather than their
(find-system-path'init-file). Unlike
racket/interactive, this library does not
start xrepl.

Added in version 1.27 of package `gui-lib`.
