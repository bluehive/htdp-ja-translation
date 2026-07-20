<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/add-color___.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/add-color___.html -->
<!-- Canonical English source for Japanese translation -->

```
+------------------------------------+
| interfaceadd-color<%>: interface? |
+------------------------------------+
+------------------------------------+
```

An add-color<%> object is used to additively change the RGB values of
a color% object. An add-color<%> object only exists within a
style-delta% object.

See also get-foreground-add and get-background-add.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send an-add-color get r g b [a]) → void? |
| r: (box/c (integer-in -1000 1000))       |
| g: (box/c (integer-in -1000 1000))       |
| b: (box/c (integer-in -1000 1000))       |
| a: (or/c (box/c real?) #f) = #f          |
+-------------------------------------------+
```

Gets all of the additive values.

The r box is filled with the additive value for the red component of the color.
The g box is filled with the additive value for the green component of the color.
The b box is filled with the additive value for the blue component of the color.
The a box is filled with the additive value for the alpha component of the color, unless a is #f.

Changed in version 1.63 of package `snip-lib`: Added the a optional argument.

```
+-----------------------------------+
| [method]                          |
|                                   |
| (send an-add-color get-a) → real? |
+-----------------------------------+
```

Gets the additive value for the alpha component of the color.

Added in version 1.63 of package `snip-lib`.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send an-add-color get-b) → (integer-in -1000 1000) |
+-----------------------------------------------------+
```

Gets the additive value for the blue component of the color.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send an-add-color get-g) → (integer-in -1000 1000) |
+-----------------------------------------------------+
```

Gets the additive value for the green component of the color.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send an-add-color get-r) → (integer-in -1000 1000) |
+-----------------------------------------------------+
```

Gets the additive value for the red component of the color.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send an-add-color set r g b [a]) → void? |
| r: (integer-in -1000 1000)               |
| g: (integer-in -1000 1000)               |
| b: (integer-in -1000 1000)               |
| a: real? = 0.0                           |
+-------------------------------------------+
```

Sets all of the additive values.

Changed in version 1.63 of package `snip-lib`: Added the a optional argument.

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send an-add-color set-a v) → void? |
| v: real?                           |
+-------------------------------------+
```

Sets the additive value for the alpha component of the color.

Added in version 1.63 of package `snip-lib`.

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send an-add-color set-b v) → void? |
| v: (integer-in -1000 1000)         |
+-------------------------------------+
```

Sets the additive value for the blue component of the color.

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send an-add-color set-g v) → void? |
| v: (integer-in -1000 1000)         |
+-------------------------------------+
```

Sets the additive value for the green component of the color.

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send an-add-color set-r v) → void? |
| v: (integer-in -1000 1000)         |
+-------------------------------------+
```

Sets the additive value for the red component of the color.
