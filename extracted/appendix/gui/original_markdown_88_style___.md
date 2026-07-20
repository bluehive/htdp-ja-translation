<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/style___.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/style___.html -->
<!-- Canonical English source for Japanese translation -->

```
+--------------------------------+
| interfacestyle<%>: interface? |
+--------------------------------+
+--------------------------------+
```

A style<%> object encapsulates drawing information (font,
color, alignment, etc.) in a hierarchical manner. A style<%>
object always exists within the context of a style-list%
object and is never created except by a style-list% object.

See also Styles.

```
+------------------------------------------------------------+
| [method]                                                   |
|                                                            |
| (send a-style get-alignment) → (or/c 'top 'center 'bottom) |
+------------------------------------------------------------+
```

Returns the style’s alignment: 'top, 'center, or
'bottom.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-style get-background) → (is-a?/c color%) |
+--------------------------------------------------+
```

Returns the style’s background color.

```
+--------------------------------------------------------------+
| [method]                                                     |
|                                                              |
| (send a-style get-base-style) → (or/c (is-a?/c style<%>) #f) |
+--------------------------------------------------------------+
```

Returns the style’s base style. See Styles for more
information. The return value is #f only for the basic style
in the list.

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-style get-delta delta) → void? |
| delta: (is-a?/c style-delta%)         |
+----------------------------------------+
```

Mutates delta, changing it to match the style’s delta, if the style is not a join
style. See Styles for more information.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-style get-face) → (or/c string? #f) |
+---------------------------------------------+
```

Returns the style’s face name. See font%.

```
+-----------------------------------------------------------------------------+
| [method]                                                                    |
|                                                                             |
| (send a-style get-family)                                                   |
| → (or/c 'default 'decorative 'roman 'script 'swiss 'modern 'symbol 'system) |
| (or/c 'default 'decorative 'roman 'script                                   |
| 'swiss 'modern 'symbol 'system)                                             |
|                                                                             |
| ```racket                                                                   |
| (or/c 'default 'decorative 'roman 'script                                   |
|       'swiss 'modern 'symbol 'system)                                       |
| ```                                                                         |
+-----------------------------------------------------------------------------+
```

Returns the style’s font family. See font%.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-style get-font) → (is-a?/c font%) |
+-------------------------------------------+
```

Returns the style’s font information.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-style get-foreground) → (is-a?/c color%) |
+--------------------------------------------------+
```

Returns the style’s foreground color.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-style get-name) → (or/c string? #f) |
+---------------------------------------------+
```

Returns the style’s name, or #f if it is unnamed. Style names
are only set through the style’s style-list% object.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-style get-shift-style) → (is-a?/c style<%>) |
+-----------------------------------------------------+
```

Returns the style’s shift style if it is a join style. Otherwise, the
root style is returned. See Styles for more information.

```
+---------------------------------+
| [method]                        |
|                                 |
| (send a-style get-size) → byte? |
+---------------------------------+
```

Returns the style’s font size.

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-style get-size-in-pixels) → boolean? |
+----------------------------------------------+
```

Returns #t if the style size is in pixels, instead of points,
or #f otherwise.

```
+----------------------------------------------------------+
| [method]                                                 |
|                                                          |
| (send a-style get-smoothing)                             |
| → (or/c 'default 'partly-smoothed 'smoothed 'unsmoothed) |
+----------------------------------------------------------+
```

Returns the style’s font smoothing. See font%.

```
+----------------------------------------------------------+
| [method]                                                 |
|                                                          |
| (send a-style get-style) → (or/c 'normal 'italic 'slant) |
+----------------------------------------------------------+
```

Returns the style’s font style. See font%.

```
+------------------------------------+
| [method]                           |
|                                    |
| (send a-style get-text-descent dc) |
| → (and/c real? (not/c negative?))  |
| dc: (is-a?/c dc<%>)               |
+------------------------------------+
```

Returns the descent of text using this style in a given DC.

```
+-----------------------------------+
| [method]                          |
|                                   |
| (send a-style get-text-height dc) |
| → (and/c real? (not/c negative?)) |
| dc: (is-a?/c dc<%>)              |
+-----------------------------------+
```

Returns the height of text using this style in a given DC.

```
+-----------------------------------+
| [method]                          |
|                                   |
| (send a-style get-text-space dc)  |
| → (and/c real? (not/c negative?)) |
| dc: (is-a?/c dc<%>)              |
+-----------------------------------+
```

Returns the vertical spacing for text using this style in a given DC.

```
+-----------------------------------+
| [method]                          |
|                                   |
| (send a-style get-text-width dc)  |
| → (and/c real? (not/c negative?)) |
| dc: (is-a?/c dc<%>)              |
+-----------------------------------+
```

Returns the width of a space character using this style in a given
DC.

```
+--------------------------------------------------------+
| [method]                                               |
|                                                        |
| (send a-style get-transparent-text-backing) → boolean? |
+--------------------------------------------------------+
```

Returns #t if text is drawn without erasing the
text background or #f otherwise.

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send a-style get-underlined) → boolean? |
+------------------------------------------+
```

Returns #t if the style is underlined or #f
otherwise.

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send a-style get-weight) → (or/c 'normal 'bold 'light) |
+---------------------------------------------------------+
```

Returns the style’s font weight. See font%.

```
+------------------------------------+
| [method]                           |
|                                    |
| (send a-style is-join?) → boolean? |
+------------------------------------+
```

Returns #t if the style is a join style or #f
otherwise. See Styles for more information.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-style set-base-style base-style) → void? |
| base-style: (is-a?/c style<%>)                  |
+--------------------------------------------------+
```

Sets the style’s base style and recomputes the style’s font, etc. See
Styles for more information.

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-style set-delta delta) → void? |
| delta: (is-a?/c style-delta%)         |
+----------------------------------------+
```

Sets the style’s delta (if it is not a join style) and recomputes the
style’s font, etc. See Styles for more information.

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-style set-shift-style style) → void? |
| style: (is-a?/c style<%>)                   |
+----------------------------------------------+
```

Sets the style’s shift style (if it is a join style) and recomputes
the style’s font, etc. See Styles for more information.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-style switch-to dc old-style) → void? |
| dc: (is-a?/c dc<%>)                          |
| old-style: (or/c (is-a?/c style<%>) #f)      |
+-----------------------------------------------+
```

Sets the font, pen color, etc. of the given drawing context. If
oldstyle is not #f, only differences between the
given style and this one are applied to the drawing context.
