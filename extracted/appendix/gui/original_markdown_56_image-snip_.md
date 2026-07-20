<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/image-snip_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/image-snip_.html -->
<!-- Canonical English source for Japanese translation -->

```
+---------------------------+
| classimage-snip%: class? |
+---------------------------+
| superclass: snip%         |
+---------------------------+
```

An image-snip% is a snip that can display bitmap images
(usually loaded from a file). When the image file cannot be found, a
box containing an “X” is drawn.

```
+------------------------------------------------------------------------------+
| [constructor]                                                                |
|                                                                              |
| (make-object image-snip%                                                     |
| → (is-a?/c image-snip%)                                                      |
| file: (or/c path-string? input-port? #f) = #f                               |
| kind: (or/c 'unknown 'unknown/mask 'unknown/alpha 'gif 'gif/mask 'gif/alpha |
| 'jpeg 'png 'png/mask 'png/alpha 'xbm 'xpm 'bmp 'pict) = 'unknown             |
| (or/c 'unknown 'unknown/mask 'unknown/alpha                                  |
| 'gif 'gif/mask 'gif/alpha                                                    |
| 'jpeg 'png 'png/mask 'png/alpha                                              |
| 'xbm 'xpm 'bmp 'pict)                                                        |
| relative-path?: any/c = #f                                                  |
| inline?: any/c = #t                                                         |
| backing-scale: (>/c 0.0) = 1.0                                              |
| (make-object image-snip% bitmap [mask]) → (is-a?/c image-snip%)              |
| bitmap: (is-a?/c bitmap%)                                                   |
| mask: (or/c (is-a?/c bitmap%) #f) = #f                                      |
|                                                                              |
| ```racket                                                                    |
| (or/c 'unknown 'unknown/mask 'unknown/alpha                                  |
|       'gif 'gif/mask 'gif/alpha                                              |
|       'jpeg 'png 'png/mask 'png/alpha                                        |
|       'xbm 'xpm 'bmp 'pict)                                                  |
| ```                                                                          |
+------------------------------------------------------------------------------+
```

Creates an image snip, loading the image file if
specified (see also load-file), or using the
given bitmap.

Changed in version 1.1 of package `snip-lib`: Added the backing-scale argument.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send an-image-snip equal-hash-code-of hash-code) |
| → exact-integer?                                  |
| hash-code: (any/c. ->. exact-integer?)         |
+---------------------------------------------------+
```

Returns an integer that can be used as a equal?-based hash
code for an-image-snip (using the same notion of equal? as
other-equal-to?).

See also equal<%>.

```
+-------------------------------------------------------------+
| [method]                                                    |
|                                                             |
| (send an-image-snip equal-secondary-hash-code-of hash-code) |
| → exact-integer?                                            |
| hash-code: (any/c. ->. exact-integer?)                   |
+-------------------------------------------------------------+
```

Returns an integer that can be used as a equal?-based
secondary hash code for an-image-snip (using the same notion of
equal? as other-equal-to?).

See also equal<%>.

```
+---------------------------------------------------------------+
| [method]                                                      |
|                                                               |
| (send an-image-snip get-bitmap) → (or/c (is-a?/c bitmap%) #f) |
+---------------------------------------------------------------+
```

Returns the bitmap that is displayed by the snip, whether set through
set-bitmap or load-file. If
no bitmap is displayed, the result is #f.

```
+--------------------------------------+
| [method]                             |
|                                      |
| (send an-image-snip get-bitmap-mask) |
| → (or/c (is-a?/c bitmap%) #f)        |
+--------------------------------------+
```

Returns the mask bitmap that is used for displaying by the snip, if
one was installed with set-bitmap. If no mask
is used, the result is #f.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send an-image-snip get-filename [relative-path]) |
| → (or/c path-string? #f)                          |
| relative-path: (or/c (box/c any/c) #f) = #f      |
+---------------------------------------------------+
```

Returns the name of the currently loaded, non-inlined file, or
#f if a file is not loaded or if a file was loaded with
inlining (the default).

The relative-path box is filled with #t if the loaded file’s path is
relative to the owning editor’s path, unless relative-path is #f.

```
+-------------------------------------------------------------------------------+
| [method]                                                                      |
|                                                                               |
| (send an-image-snip get-filetype)                                             |
| → (or/c 'unknown 'unknown/mask 'unknown/alpha 'gif 'gif/mask 'gif/alpha 'jpeg |
| 'png 'png/mask 'png/alpha 'xbm 'xpm 'bmp 'pict)                               |
| (or/c 'unknown 'unknown/mask 'unknown/alpha                                   |
| 'gif 'gif/mask 'gif/alpha                                                     |
| 'jpeg 'png 'png/mask 'png/alpha                                               |
| 'xbm 'xpm 'bmp 'pict)                                                         |
|                                                                               |
| ```racket                                                                     |
| (or/c 'unknown 'unknown/mask 'unknown/alpha                                   |
|       'gif 'gif/mask 'gif/alpha                                               |
|       'jpeg 'png 'png/mask 'png/alpha                                         |
|       'xbm 'xpm 'bmp 'pict)                                                   |
| ```                                                                           |
+-------------------------------------------------------------------------------+
```

Returns the kind used to load the currently loaded, non-inlined file,
or 'unknown if a file is not loaded or if a file was loaded
with inlining (the default).

```
+------------------------------------------------------------------------------+
| [method]                                                                     |
|                                                                              |
| (send an-image-snip load-file                                                |
| file: (or/c path-string? input-port? #f)                                    |
| kind: (or/c 'unknown 'unknown/mask 'unknown/alpha 'gif 'gif/mask 'gif/alpha |
| 'jpeg 'png 'png/mask 'png/alpha 'xbm 'xpm 'bmp 'pict) = 'unknown             |
| (or/c 'unknown 'unknown/mask 'unknown/alpha                                  |
| 'gif 'gif/mask 'gif/alpha                                                    |
| 'jpeg 'png 'png/mask 'png/alpha                                              |
| 'xbm 'xpm 'bmp 'pict)                                                        |
| relative-path?: any/c = #f                                                  |
| inline?: any/c = #t                                                         |
| backing-scale: (>/c 0.0) = 1.0                                              |
|                                                                              |
| ```racket                                                                    |
| (or/c 'unknown 'unknown/mask 'unknown/alpha                                  |
|       'gif 'gif/mask 'gif/alpha                                              |
|       'jpeg 'png 'png/mask 'png/alpha                                        |
|       'xbm 'xpm 'bmp 'pict)                                                  |
| ```                                                                          |
+------------------------------------------------------------------------------+
```

Loads the file by passing file and kind to
load-file in bitmap%. If a bitmap had previously been specified
with set-bitmap, that bitmap (and mask) will no
longer be used. If file is #f, then the current
image is cleared.

When 'unknown/mask, 'gif/mask, or 'png/mask
is specified and the loaded bitmap object includes a mask (see
get-loaded-mask), the mask is used for drawing the
bitmap (see draw-bitmap). The 'unknown/alpha,
'gif/alpha, or 'png/alpha variants are recommended,
however.

If relative-path? is not #f and file is a
relative path, then the file will be read using the path of the
owning editor’s filename. If the image is not inlined, it will be
saved as a relative pathname.

If inline? is not #f, the image data will be saved
directly to the file or clipboard when the image is saved or copied
(preserving the bitmap’s mask, if any). The source filename and kind
is no longer relevant.

Changed in version 1.1 of package `snip-lib`: Added the backing-scale argument.

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send an-image-snip other-equal-to?    |
| snip: (is-a?/c snip%)                 |
| equal?: (any/c any/c. ->. boolean?) |
+----------------------------------------+
```

Returns #t if an-image-snip and snip both have bitmaps
and the bitmaps are the same. If either has a mask bitmap
with the same dimensions as the main bitmap, then the masks must be
the same (or if only one mask is present, it must correspond to a
solid mask).

The given equal? function (for recursive comparisons) is not
used.

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send an-image-snip resize w h) → boolean? |
| w: (and/c real? (not/c negative?))        |
| h: (and/c real? (not/c negative?))        |
+--------------------------------------------+
```

Overrides resize in snip%.

The bitmap will be cropped to fit in the given dimensions.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send an-image-snip set-bitmap bm [mask]) → void? |
| bm: (is-a?/c bitmap%)                            |
| mask: (or/c (is-a?/c bitmap%) #f) = #f           |
+---------------------------------------------------+
```

Sets the bitmap that is displayed by the snip.

An optional mask is used when drawing the bitmap (see
draw-bitmap), but supplying the mask directly is
deprecated. If no mask is supplied but the bitmap’s
get-loaded-mask method produces a bitmap of the same
dimensions, it is used as the mask; furthermore, such a mask is saved
with the snip when it is saved to a file or copied (whereas a
directly supplied mask is not saved). Typically, however, bm
instead should have an alpha channel instead of a separate mask bitmap.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send an-image-snip set-offset dx dy) → void? |
| dx: real?                                    |
| dy: real?                                    |
+-----------------------------------------------+
```

Sets a graphical offset for the bitmap within the image snip.
