<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/area___.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/area___.html -->
<!-- Canonical English source for Japanese translation -->

```
+-------------------------------+
| interfacearea<%>: interface? |
+-------------------------------+
+-------------------------------+
```

An area<%> object is either a window or a windowless
container for managing the position and size of other areas. An
area<%> can be a container, a containee, or both. The only
areas without a parent are top-level windows.

All area<%> classes accept the following named instantiation
arguments:

- min-width — default is the initial graphical minimum width; passed to
min-width
- min-height — default is the initial graphical minimum height; passed to
min-height
- stretchable-width — default is class-specific; passed to
stretchable-width
- stretchable-height — default is class-specific; passed to
stretchable-height

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send an-area get-graphical-min-size)   |
| → dimension-integer? dimension-integer? |
| dimension-integer?                      |
+-----------------------------------------+
```

Returns the area’s graphical minimum size as two values: the minimum
width and the minimum height (in pixels).

See Geometry Management for more information. Note that the return value
does not depend on the area’s
min-width and
min-height settings.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send an-area get-parent)               |
| → (or/c (is-a?/c area-container<%>) #f) |
+-----------------------------------------+
```

Returns the area’s parent. A top-level window may have no parent (in
which case #f is returned), or it may have another top-level
window as its parent.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send an-area get-top-level-window)         |
| → (or/c (is-a?/c frame%) (is-a?/c dialog%)) |
+---------------------------------------------+
```

Returns the area’s closest frame or dialog ancestor. For a frame or
dialog area, the frame or dialog itself is returned.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send an-area min-width) → dimension-integer? |
| (send an-area min-width w) → void?            |
| w: dimension-integer?                        |
+-----------------------------------------------+
```

Gets or sets the area’s minimum width (in pixels) for geometry
management.

The minimum width is ignored when it is smaller than the area’s
graphical minimum width, or when it is smaller
than the width reported by
container-size if the area is a container. See Geometry Management for more information.

An area’s initial minimum width is its graphical minimum width. See
also
get-graphical-min-size.

When setting the minimum width, if w is smaller than the
internal hard minimum, an exn:fail:contract exception is raised.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send an-area min-height) → dimension-integer? |
| (send an-area min-height h) → void?            |
| h: dimension-integer?                         |
+------------------------------------------------+
```

Gets or sets the area’s minimum height for geometry management.

The minimum height is ignored when it is smaller than the area’s
graphical minimum height, or when it is smaller
than the height reported by
container-size if the area is a container. See Geometry Management for more information.

An area’s initial minimum height is its graphical minimum height. See
also
get-graphical-min-size.

When setting the minimum height (in pixels); if h is smaller
than the internal hard minimum, an exn:fail:contract exception is raised.

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send an-area stretchable-height) → boolean?       |
| (send an-area stretchable-height stretch?) → void? |
| stretch?: any/c                                   |
+----------------------------------------------------+
```

Gets or sets the area’s vertical stretchability for geometry
management. See Geometry Management for more information.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send an-area stretchable-width) → boolean?       |
| (send an-area stretchable-width stretch?) → void? |
| stretch?: any/c                                  |
+---------------------------------------------------+
```

Gets or sets the area’s horizontal stretchability for geometry
management. See Geometry Management for more information.
