<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/mult-color___.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/mult-color___.html -->
<!-- Canonical English source for Japanese translation -->

```
+-------------------------------------+
| interfacemult-color<%>: interface? |
+-------------------------------------+
+-------------------------------------+
```

A mult-color<%> object is used to scale the RGB values of a
color% object. A mult-color<%> object exist only
within a style-delta% object.

See also get-foreground-mult and
get-background-mult.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-mult-color get r g b [a]) → void? |
| r: (box/c real?)                         |
| g: (box/c real?)                         |
| b: (box/c real?)                         |
| a: (or/c (box/c real?) #f) = #f          |
+-------------------------------------------+
```

Gets all of the scaling values.

The r box is filled with the scaling value for the red component of the color.
The g box is filled with the scaling value for the green component of the color.
The b box is filled with the scaling value for the blue component of the color.
The a box is filled with the scaling value for the alpha component of the color, unless a is #f.

Changed in version 1.63 of package `snip-lib`: Added the a optional argument.

```
+-----------------------------------+
| [method]                          |
|                                   |
| (send a-mult-color get-a) → real? |
+-----------------------------------+
```

Gets the multiplicative scaling value for the alpha component of the color.

Added in version 1.63 of package `snip-lib`.

```
+-----------------------------------+
| [method]                          |
|                                   |
| (send a-mult-color get-b) → real? |
+-----------------------------------+
```

Gets the multiplicative scaling value for the blue component of the color.

```
+-----------------------------------+
| [method]                          |
|                                   |
| (send a-mult-color get-g) → real? |
+-----------------------------------+
```

Gets the multiplicative scaling value for the green component of the color.

```
+-----------------------------------+
| [method]                          |
|                                   |
| (send a-mult-color get-r) → real? |
+-----------------------------------+
```

Gets the multiplicative scaling value for the red component of the color.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-mult-color set r g b [a]) → void? |
| r: real?                                 |
| g: real?                                 |
| b: real?                                 |
| a: real? = 1.0                           |
+-------------------------------------------+
```

Sets all of the scaling values.

Changed in version 1.63 of package `snip-lib`: Added the a optional argument.

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-mult-color set-a v) → void? |
| v: real?                           |
+-------------------------------------+
```

Sets the multiplicative scaling value for the alpha component of the color.

Added in version 1.63 of package `snip-lib`.

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-mult-color set-b v) → void? |
| v: real?                           |
+-------------------------------------+
```

Sets the multiplicative scaling value for the blue component of the color.

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-mult-color set-g v) → void? |
| v: real?                           |
+-------------------------------------+
```

Sets the multiplicative scaling value for the green component of the
color.

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-mult-color set-r v) → void? |
| v: real?                           |
+-------------------------------------+
```

Sets the additive value for the red component of the color.
