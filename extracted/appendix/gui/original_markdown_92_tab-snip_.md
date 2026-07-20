<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/tab-snip_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/tab-snip_.html -->
<!-- Canonical English source for Japanese translation -->

```
+--------------------------+
| classtab-snip%: class?  |
+--------------------------+
| superclass: string-snip% |
+--------------------------+
```

An instance of tab-snip% is created automatically when a
tab is inserted into an editor.

```
+---------------------------------------+
| [constructor]                         |
|                                       |
| (new tab-snip%) → (is-a?/c tab-snip%) |
+---------------------------------------+
```

Creates a snip for a single tab, though the tab is initially empty.

Normally, a single tab is inserted into a tab-snip% object
using the insert method.

The tab’s content is not drawn, through it is used when determining
the size of a single character in editors where tabbing is determined
by the character width (see set-tabs); if the content
is a single tab character (the normal case), then the average
character width of snip’s font is used as the tab’s width.
