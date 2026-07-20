<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/Dynamic_Loading.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/Dynamic_Loading.html -->
<!-- Canonical English source for Japanese translation -->

## 11 Dynamic Loading

```
+-------------------------------+-----------------+
|  (require racket/gui/dynamic) | package: `base` |
+-------------------------------+-----------------+
+-------------------------------+-----------------+
```

The racket/gui/dynamic
library provides functions for dynamically accessing the
racket/gui/base library, instead of directly requiring
racket/gui or racket/gui/base.

```
+-----------------------------+
| [procedure]                 |
|                             |
| (gui-available?) → boolean? |
+-----------------------------+
```

Returns #t if dynamic access to the GUI bindings is
available. The bindings are available if
racket/gui/base has been loaded, instantiated, and
attached to the namespace in which racket/gui/dynamic was
instantiated.

```
+---------------------------------+
| [procedure]                     |
|                                 |
| (gui-dynamic-require sym) → any |
| sym: symbol?                   |
+---------------------------------+
```

Like dynamic-require, but specifically to access exports of
racket/gui/base, and only when (gui-available?)
returns true.

The gui-dynamic-require function is intended primarily for
use under a (gui-available?) conditional. It can also be used
as a shorthand for dynamic-require with
'racket/gui/base, but only after ensuring that the bindings
are available. One way to make racket/gui/base
bindings available, so that (gui-available?) returns true, is
through dynamic-require:

```racket
(dynamic-require 'racket/gui/base #f)
```

Unlike require, using dynamic-require delays the
instantiation of racket/gui/base until the run-time
call of dynamic-require. With racket/gui/base
so declared, gui-dynamic-require can be used to access
bindings:

```racket
(define window (new (gui-dynamic-require 'frame%)
                    [label "Frame"]))
(send window show #t)
```
