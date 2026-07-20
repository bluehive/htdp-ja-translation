<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/libs.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/libs.html -->
<!-- Canonical English source for Japanese translation -->

## 14 Platform Dependencies

See Platform Dependencies in The Racket Drawing Toolkit for
information on platform library dependencies for
racket/draw. On Unix, GTK+ 3 is used if its libraries
can be found and the `PLT_GTK2` environment is not
defined. Otherwise, GTK+ 2 is used. The following additional system
libraries must be installed for racket/gui/base in
either case:

- `"libgdk-3.0[.0]"` (GTK+ 3) or `"libgdk-x11-2.0[.0]"` (GTK+ 2)
- `"libgdk_pixbuf-2.0[.0]"` (GTK+ 2)
- `"libgtk-3.0[.0]"` (GTK+ 3) or `"libgtk-x11-2.0[.0]"` (GTK+ 2)
- `"libgio-2.0[.0]"` — optional, for detecting interface scaling
- `"libGL[.1]"` — optional, for OpenGL support
- `"libunique-1.0[.0]"` — optional, for single-instance support (GTK+ 2)
