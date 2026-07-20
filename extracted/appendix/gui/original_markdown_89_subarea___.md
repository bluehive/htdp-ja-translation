<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/subarea___.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/subarea___.html -->
<!-- Canonical English source for Japanese translation -->

```
+----------------------------------+---------+
| interfacesubarea<%>: interface? |         |
+----------------------------------+---------+
| implements:                      | area<%> |
+----------------------------------+---------+
```

A subarea<%> is a containee area<%>.

All subarea<%> classes accept the following named
instantiation arguments:

- horiz-margin — default is 2 for
control<%> classes and group-box-panel%,
0 for others; passed to
horiz-margin
- vert-margin — default is 2 for
control<%> classes and group-box-panel%,
0 for others; passed to
vert-margin

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-subarea horiz-margin) → spacing-integer? |
| (send a-subarea horiz-margin margin) → void?     |
| margin: spacing-integer?                        |
+--------------------------------------------------+
```

Gets or sets the area’s horizontal margin, which is added both to the
right and left, for geometry management. See Geometry Management for more
information.

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-subarea vert-margin) → spacing-integer? |
| (send a-subarea vert-margin margin) → void?     |
| margin: spacing-integer?                       |
+-------------------------------------------------+
```

Gets or sets the area’s vertical margin, which is added both to the
top and bottom, for geometry management. See Geometry Management for more
information.
