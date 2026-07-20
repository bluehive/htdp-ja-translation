<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/Editor_Classes.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/Editor_Classes.html -->
<!-- Canonical English source for Japanese translation -->

## 7 Editor Classes

Editors:

```
+------------------+
| editor<%>        |
+------------------+
| `|`- text%       |
| `|`- pasteboard% |
+------------------+
```

Editor Snips:

```
+-------------------+
| snip%             |
+-------------------+
| `|`- editor-snip% |
+-------------------+
```

Displays, Administrators, and Mappings:

```
+----------------------------------+
| editor-canvas%                   |
+----------------------------------+
| editor-admin% snip-admin%        |
| `|`- editor-snip-editor-admin<%> |
| editor-wordbreak-map% keymap%    |
+----------------------------------+
```

Streams for Saving and Cut-and-Paste:

```
+--------------------------------------------------+
| editor-data%                                     |
+--------------------------------------------------+
| editor-data-class%                               |
| editor-data-class-list<%>                        |
| editor-stream-in% editor-stream-out%             |
| editor-stream-in-base% editor-stream-out-base%   |
| `|`- editor-stream-in-bytes-base% `|`- editor-s… |
+--------------------------------------------------+
```

Alphabetical:

### Contents

- 7.1 editor<%>
- 7.2 editor-admin%
- 7.3 editor-canvas%
- 7.4 editor-data%
- 7.5 editor-data-class%
- 7.6 editor-data-class-list<%>
- 7.7 editor-snip-editor-admin<%>
- 7.8 editor-snip%
- 7.9 editor-stream-in%
- 7.10 editor-stream-in-base%
- 7.11 editor-stream-in-bytes-base%
- 7.12 editor-stream-out%
- 7.13 editor-stream-out-base%
- 7.14 editor-stream-out-bytes-base%
- 7.15 editor-wordbreak-map%
- 7.16 keymap%
- 7.17 pasteboard%
- 7.18 text%
