<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/Snip_and_Style_Classes.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/Snip_and_Style_Classes.html -->
<!-- Canonical English source for Japanese translation -->

## 6 Snip and Style Classes

```
+------------------------+---------------------+
|  (require racket/snip) | package: `snip-lib` |
+------------------------+---------------------+
+------------------------+---------------------+
```

The racket/snip collection provides the core
snip and style classes *without* depending on
racket/gui/base. This separation enables
libraries that can cooperate with an editor while also working in
contexts that do not have a GUI.

Snips and Administrators:

```
+--------------------------------------------------+
| snip% readable-snip<%>                           |
+--------------------------------------------------+
| `|`- string-snip%                                |
| `|` `|`- tab-snip%                               |
| `|`- image-snip%                                 |
| `|`- editor-snip% `(`not provided by racket`/`s… |
| snip-admin%                                      |
+--------------------------------------------------+
```

Snip Lists:

```
+--------------------+
| snip-class%        |
+--------------------+
| snip-class-list<%> |
+--------------------+
```

Styles:

```
+------------------------------------+
| style<%> style-delta% add-color<%> |
+------------------------------------+
| style-list% mult-color<%>          |
+------------------------------------+
```

Alphabetical:

### Contents

- 6.1 add-color<%>
- 6.2 image-snip%
- 6.3 mult-color<%>
- 6.4 readable-snip<%>
- 6.5 snip%
- 6.6 snip-admin%
- 6.7 snip-class%
- 6.8 snip-class-list<%>
- 6.9 string-snip%
- 6.10 style<%>
- 6.11 style-delta%
- 6.12 style-list%
- 6.13 tab-snip%
