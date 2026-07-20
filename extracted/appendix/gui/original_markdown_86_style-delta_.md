<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/style-delta_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/style-delta_.html -->
<!-- Canonical English source for Japanese translation -->

```
+----------------------------+
| classstyle-delta%: class? |
+----------------------------+
| superclass: object%        |
+----------------------------+
```

A style-delta% object encapsulates a style change. The changes
expressible by a delta include:

- changing the font family
- changing the font face
- changing the font size to a new value
- enlarging the font by an additive amount
- enlarging the font by a multiplicative amount, etc.
- changing the font style (normal, italic, or slant)
- toggling the font style
- changing the font to italic if it is currently slant, etc.
- changing the font weight, etc.
- changing the underline, etc.
- changing the vertical alignment, etc.
- changing the foreground color
- dimming or brightening the foreground color, etc.
- changing the background color, etc.
- changing text backing transparency

The set-delta method is convenient for most
style delta settings; it takes a high-level delta specification and
sets the internal delta information.

To take full advantage of a style delta, it is necessary to understand
the internal on/off settings that can be manipulated through methods
such as set-weight-on. For example, the font
weight change is specified through the weight-on and
weight-off internal settings. Roughly, weight-on
turns on a weight setting when it is not present and
weight-off turns off a weight setting when it is
present. These two interact precisely in the following way:

- If both weight-on and weight-off are set to 'base,
then the font weight is not changed.
- If weight-on is not 'base, then the weight is set to
weight-on.
- If weight-off is not 'base, then the weight will be set back
to 'normal when the base style has the weight weight-off.
- If both weight-on and weight-off are set to the same
value, then the weight is toggled with respect to that value: if
the base style has the weight weight-on, then weight is changed to
'normal; if the base style has a different weight, it is changed to
weight-on.
- If both weight-on and weight-off are set, but to
different values, then the weight is changed to weight-on
only when the base style has the weight weight-off.

Font styles, smoothing, underlining, and alignment work in an analogous manner.

The possible values for alignment-on and alignment-off are:

- 'base
- 'top
- 'center
- 'bottom

The possible values for style-on and style-off are:

- 'base
- 'normal
- 'italic
- 'slant

The possible values for smoothing-on and smoothing-off are:

- 'base
- 'default
- 'partly-smoothed
- 'smoothed
- 'unsmoothed

The possible values for underlined-on and underlined-off are:

- #f (acts like 'base)
- #t

The possible values for size-in-pixels-on and
size-in-pixels-off are:

- #f (acts like 'base)
- #t

The possible values for transparent-text-backing-on and
transparent-text-backing-off are:

- #f (acts like 'base)
- #t

The possible values for weight-on and weight-off are:

- 'base
- 'normal
- 'bold
- 'light

The family and face settings in a style delta are interdependent:

- When a delta’s face is #f and its family is
'base, then neither the face nor family are modified by
the delta.
- When a delta’s face is a string and its family is
'base, then only face is modified by the delta.
- When a delta’s family is not 'base, then both the face
and family are modified by the delta. If the delta’s face is
#f, then applying the delta sets a style’s face to
#f, so that the family setting prevails in choosing a
font.

```
+--------------------------------------------------------------------------------+
| [constructor]                                                                  |
|                                                                                |
| (make-object style-delta% [change-command])                                    |
| → (is-a?/c style-delta%)                                                       |
| change-command: (or/c 'change-nothing 'change-normal 'change-toggle-underline |
| 'change-toggle-size-in-pixels 'change-normal-color 'change-bold) =             |
| 'change-nothing                                                                |
| (or/c 'change-nothing                                                          |
| 'change-normal                                                                 |
| 'change-toggle-underline                                                       |
| 'change-toggle-size-in-pixels                                                  |
| 'change-normal-color                                                           |
| 'change-bold)                                                                  |
| (make-object style-delta% change-command v)                                    |
| → (is-a?/c style-delta%)                                                       |
| change-command: (or/c 'change-family 'change-style 'change-toggle-style       |
| 'change-weight 'change-toggle-weight 'change-smoothing                         |
| 'change-toggle-smoothing 'change-alignment)                                    |
| (or/c 'change-family                                                           |
| 'change-style                                                                  |
| 'change-toggle-style                                                           |
| 'change-weight                                                                 |
| 'change-toggle-weight                                                          |
| 'change-smoothing                                                              |
| 'change-toggle-smoothing                                                       |
| 'change-alignment)                                                             |
| v: symbol                                                                     |
| (make-object style-delta% change-command v)                                    |
| → (is-a?/c style-delta%)                                                       |
| change-command: (or/c 'change-size 'change-bigger 'change-smaller)            |
| (or/c 'change-size                                                             |
| 'change-bigger                                                                 |
| 'change-smaller)                                                               |
| v: exact-integer?                                                             |
| (make-object style-delta% change-command v)                                    |
| → (is-a?/c style-delta%)                                                       |
| change-command: (or/c 'change-underline 'change-size-in-pixels)               |
| (or/c 'change-underline                                                        |
| 'change-size-in-pixels)                                                        |
| v: any/c                                                                      |
|                                                                                |
| ```racket                                                                      |
| (or/c 'change-nothing                                                          |
|       'change-normal                                                           |
|       'change-toggle-underline                                                 |
|       'change-toggle-size-in-pixels                                            |
|       'change-normal-color                                                     |
|       'change-bold)                                                            |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (or/c 'change-family                                                           |
|       'change-style                                                            |
|       'change-toggle-style                                                     |
|       'change-weight                                                           |
|       'change-toggle-weight                                                    |
|       'change-smoothing                                                        |
|       'change-toggle-smoothing                                                 |
|       'change-alignment)                                                       |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (or/c 'change-size                                                             |
|       'change-bigger                                                           |
|       'change-smaller)                                                         |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (or/c 'change-underline                                                        |
|       'change-size-in-pixels)                                                  |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

The initialization arguments are passed on to
set-delta.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-style-delta collapse delta) → boolean? |
| delta: (is-a?/c style-delta%)                 |
+------------------------------------------------+
```

Tries to collapse into a single delta the changes that would be made
by applying this delta after a given delta. If the return value is
#f, then it is impossible to perform the
collapse. Otherwise, the return value is #t and this delta
will contain the collapsed change specification.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-style-delta copy delta) → void? |
| delta: (is-a?/c style-delta%)          |
+-----------------------------------------+
```

Copies the given style delta’s settings into this one.

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-style-delta equal? delta) → boolean? |
| delta: (is-a?/c style-delta%)               |
+----------------------------------------------+
```

Returns #t if the given delta is equivalent to this one in
all contexts or #f otherwise.

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-style-delta get-alignment-off) |
| → (or/c 'base 'top 'center 'bottom)    |
+----------------------------------------+
```

See style-delta%.

```
+---------------------------------------+
| [method]                              |
|                                       |
| (send a-style-delta get-alignment-on) |
| → (or/c 'base 'top 'center 'bottom)   |
+---------------------------------------+
```

See style-delta%.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-style-delta get-background-add) |
| → (is-a?/c add-color<%>)                |
+-----------------------------------------+
```

Gets the object additive color shift for the background (applied after
the multiplicative factor). Call this add-color<%> object’s
methods to change the style delta’s additive background color shift.

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send a-style-delta get-background-mult) |
| → (is-a?/c mult-color<%>)                |
+------------------------------------------+
```

Gets the multiplicative color shift for the background (applied before
the additive factor). Call this mult-color<%> object’s
methods to change the style delta’s multiplicative background color
shift.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send a-style-delta get-face) → (or/c string? #f) |
+---------------------------------------------------+
```

Gets the delta’s font face string. If this string is #f and the
family is 'base when the delta is applied to a style,
the style’s face and family are not changed. However, if the face
string is #f and the family is not 'base, then
the style’s face is changed to #f.

See also get-family.

```
+--------------------------------------------------------------------------+
| [method]                                                                 |
|                                                                          |
| (send a-style-delta get-family)                                          |
| → (or/c 'base 'default 'decorative 'roman 'script 'swiss 'modern 'symbol |
| 'system)                                                                 |
| (or/c 'base 'default 'decorative 'roman 'script                          |
| 'swiss 'modern 'symbol 'system)                                          |
|                                                                          |
| ```racket                                                                |
| (or/c 'base 'default 'decorative 'roman 'script                          |
|       'swiss 'modern 'symbol 'system)                                    |
| ```                                                                      |
+--------------------------------------------------------------------------+
```

Returns the delta’s font family. The possible values are

- 'base — no change to family
- 'default
- 'decorative
- 'roman
- 'script
- 'swiss
- 'modern (fixed width)
- 'symbol (Greek letters)
- 'system (used to draw control labels)

See also get-face.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-style-delta get-foreground-add) |
| → (is-a?/c add-color<%>)                |
+-----------------------------------------+
```

Gets the additive color shift for the foreground (applied after the
multiplicative factor). Call this add-color<%> object’s
methods to change the style delta’s additive foreground color shift.

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send a-style-delta get-foreground-mult) |
| → (is-a?/c mult-color<%>)                |
+------------------------------------------+
```

Gets the multiplicative color shift for the foreground (applied before
the additive factor). Call this mult-color<%> object’s
methods to change the style delta’s multiplicative foreground color
shift.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-style-delta get-size-add) → byte? |
+-------------------------------------------+
```

Gets the additive font size shift (applied after the multiplicative factor).

```
+--------------------------------------------------------+
| [method]                                               |
|                                                        |
| (send a-style-delta get-size-in-pixels-off) → boolean? |
+--------------------------------------------------------+
```

See style-delta%.

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-style-delta get-size-in-pixels-on) → boolean? |
+-------------------------------------------------------+
```

See style-delta%.

```
+--------------------------------------------+
| [method]                                   |
|                                            |
| (send a-style-delta get-size-mult) → real? |
+--------------------------------------------+
```

Gets the multiplicative font size shift (applied before the additive factor).

```
+----------------------------------------------------------------+
| [method]                                                       |
|                                                                |
| (send a-style-delta get-smoothing-off)                         |
| → (or/c 'base 'default 'partly-smoothed 'smoothed 'unsmoothed) |
+----------------------------------------------------------------+
```

See style-delta%.

```
+----------------------------------------------------------------+
| [method]                                                       |
|                                                                |
| (send a-style-delta get-smoothing-on)                          |
| → (or/c 'base 'default 'partly-smoothed 'smoothed 'unsmoothed) |
+----------------------------------------------------------------+
```

See
style-delta%.

```
+---------------------------------------+
| [method]                              |
|                                       |
| (send a-style-delta get-style-off)    |
| → (or/c 'base 'normal 'italic 'slant) |
+---------------------------------------+
```

See
style-delta%.

```
+---------------------------------------+
| [method]                              |
|                                       |
| (send a-style-delta get-style-on)     |
| → (or/c 'base 'normal 'italic 'slant) |
+---------------------------------------+
```

See style-delta%.

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-style-delta get-transparent-text-backing-off) |
| → boolean?                                            |
+-------------------------------------------------------+
```

See style-delta%.

```
+------------------------------------------------------+
| [method]                                             |
|                                                      |
| (send a-style-delta get-transparent-text-backing-on) |
| → boolean?                                           |
+------------------------------------------------------+
```

See style-delta%.

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-style-delta get-underlined-off) → boolean? |
+----------------------------------------------------+
```

See style-delta%.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send a-style-delta get-underlined-on) → boolean? |
+---------------------------------------------------+
```

See style-delta%.

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-style-delta get-weight-off) |
| → (or/c 'base 'normal 'bold 'light) |
+-------------------------------------+
```

See style-delta%.

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-style-delta get-weight-on)  |
| → (or/c 'base 'normal 'bold 'light) |
+-------------------------------------+
```

See style-delta%.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-style-delta set-alignment-off v) → void? |
| v: (or/c 'base 'top 'center 'bottom)            |
+--------------------------------------------------+
```

See style-delta%.

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-style-delta set-alignment-on v) → void? |
| v: (or/c 'base 'top 'center 'bottom)           |
+-------------------------------------------------+
```

See style-delta%.

```
+--------------------------------------------------------------------------------+
| [method]                                                                       |
|                                                                                |
| (send a-style-delta set-delta [change-command])                                |
| → (is-a?/c style-delta%)                                                       |
| change-command: (or/c 'change-nothing 'change-normal 'change-toggle-underline |
| 'change-toggle-size-in-pixels 'change-normal-color 'change-bold) =             |
| 'change-nothing                                                                |
| (or/c 'change-nothing                                                          |
| 'change-normal                                                                 |
| 'change-toggle-underline                                                       |
| 'change-toggle-size-in-pixels                                                  |
| 'change-normal-color                                                           |
| 'change-bold)                                                                  |
| (send a-style-delta set-delta change-command param)                            |
| (send a-style-delta set-delta                                                  |
| → (is-a?/c style-delta%)                                                       |
| change-command: (or/c 'change-family 'change-style 'change-toggle-style       |
| 'change-weight 'change-toggle-weight 'change-smoothing                         |
| 'change-toggle-smoothing 'change-alignment)                                    |
| (or/c 'change-family                                                           |
| 'change-style                                                                  |
| 'change-toggle-style                                                           |
| 'change-weight                                                                 |
| 'change-toggle-weight                                                          |
| 'change-smoothing                                                              |
| 'change-toggle-smoothing                                                       |
| 'change-alignment)                                                             |
| param: symbol?                                                                |
| (send a-style-delta set-delta change-command param)                            |
| (send a-style-delta set-delta                                                  |
| → (is-a?/c style-delta%)                                                       |
| change-command: (or/c 'change-size 'change-bigger 'change-smaller)            |
| (or/c 'change-size                                                             |
| 'change-bigger                                                                 |
| 'change-smaller)                                                               |
| param: byte?                                                                  |
| (send a-style-delta set-delta change-command on?)                              |
| (send a-style-delta set-delta                                                  |
| → (is-a?/c style-delta%)                                                       |
| change-command: (or/c 'change-underline 'change-size-in-pixels)               |
| (or/c 'change-underline                                                        |
| 'change-size-in-pixels)                                                        |
| on?: any/c                                                                    |
|                                                                                |
| ```racket                                                                      |
| (or/c 'change-nothing                                                          |
|       'change-normal                                                           |
|       'change-toggle-underline                                                 |
|       'change-toggle-size-in-pixels                                            |
|       'change-normal-color                                                     |
|       'change-bold)                                                            |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (or/c 'change-family                                                           |
|       'change-style                                                            |
|       'change-toggle-style                                                     |
|       'change-weight                                                           |
|       'change-toggle-weight                                                    |
|       'change-smoothing                                                        |
|       'change-toggle-smoothing                                                 |
|       'change-alignment)                                                       |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (or/c 'change-size                                                             |
|       'change-bigger                                                           |
|       'change-smaller)                                                         |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (or/c 'change-underline                                                        |
|       'change-size-in-pixels)                                                  |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

Configures the delta with high-level specifications. The return value
is the delta itself.

Except for 'change-nothing and
'change-normal, the command only changes part of the
delta. Thus, applying 'change-bold and then
'change-italic sets the delta for both the style and
weight change.

The change-command argument specifies how the delta is changed;
the possible values are:

- 'change-nothing — reset all changes
- 'change-normal — turn off all styles and resizings
- 'change-toggle-underline — underline regions that are currently not underlined, and vice versa
- 'change-toggle-size-in-pixels — interpret sizes in pixels for regions that are currently interpreted in points, and vice versa
- 'change-normal-color — change the foreground and background to black and white, respectively
- 'change-italic — change the style of the font to italic
- 'change-bold — change the weight of the font to bold
- 'change-family — change the font family (param is a family; see
font%); see also
get-family
- 'change-style — change the style of the font (param is a style; see
font%)
- 'change-toggle-style — toggle the style of the font (param is a style; see
font%)
- 'change-weight — change the weight of the font (param is a weight; see
font%)
- 'change-toggle-weight — toggle the weight of the font (param is a weight; see
font%)
- 'change-smoothing — change the smoothing of the font (param is a smoothing; see
font%)
- 'change-toggle-smoothing — toggle the smoothing of the font (param is a smoothing; see
font%)
- 'change-alignment — change the alignment (param is an alignment; see
style-delta%)
- 'change-size — change the size to an absolute value (param is a size)
- 'change-bigger — make the text larger (param is an additive amount)
- 'change-smaller — make the text smaller (param is an additive amount)
- 'change-underline — set the underline status to either underlined or plain
- 'change-size-in-pixels — set the size interpretation to pixels or points

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-style-delta set-delta-background name)  |
| → (is-a?/c style-delta%)                        |
| name: string?                                  |
| (send a-style-delta set-delta-background color) |
| → (is-a?/c style-delta%)                        |
| color: (is-a?/c color%)                        |
+-------------------------------------------------+
```

Makes the delta encode a background color change to match the absolute
color given; that is, it sets the multiplicative factors to
0.0 in the result of get-background-mult, and it sets the additive values in the result
of get-background-add to the specified color’s
values. In addition, it also disables transparent text backing by
setting transparent-text-backing-on to #f and
transparent-text-backing-off to #t.
The return value of the method is the delta itself.

For the case that a string color name is supplied, see
color-database<%>.

```
+-------------------------------------------------------------------------+
| [method]                                                                |
|                                                                         |
| (send a-style-delta set-delta-face                                      |
| → (is-a?/c style-delta%)                                                |
| name: string?                                                          |
| family: (or/c 'base 'default 'decorative 'roman 'script 'swiss 'modern |
| 'symbol 'system) = 'default                                             |
| (or/c 'base 'default 'decorative 'roman                                 |
| 'script 'swiss 'modern 'symbol 'system)                                 |
|                                                                         |
| ```racket                                                               |
| (or/c 'base 'default 'decorative 'roman                                 |
|       'script 'swiss 'modern 'symbol 'system)                           |
| ```                                                                     |
+-------------------------------------------------------------------------+
```

Like set-face, but sets the family at the same
time.

The return value is a-style-delta.

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-style-delta set-delta-foreground name)  |
| → (is-a?/c style-delta%)                        |
| name: string?                                  |
| (send a-style-delta set-delta-foreground color) |
| → (is-a?/c style-delta%)                        |
| color: (is-a?/c color%)                        |
+-------------------------------------------------+
```

Makes the delta encode a foreground color change to match the absolute
color given; that is, it sets the multiplicative factors to
0.0 in the result of get-foreground-mult, and it sets the additive values in the result
of get-foreground-add to the specified color’s
values. The return value of the method is the delta itself.

For the case that a string color name is supplied, see
color-database<%>.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-style-delta set-face v) → void? |
| v: (or/c string? #f)                   |
+-----------------------------------------+
```

See
get-face. See also
set-delta-face.

```
+----------------------------------------------------------------------------+
| [method]                                                                   |
|                                                                            |
| (send a-style-delta set-family v) → void?                                  |
| v: (or/c 'base 'default 'decorative 'roman 'script 'swiss 'modern 'symbol |
| 'system)                                                                   |
| (or/c 'base 'default 'decorative 'roman 'script                            |
| 'swiss 'modern 'symbol 'system)                                            |
|                                                                            |
| ```racket                                                                  |
| (or/c 'base 'default 'decorative 'roman 'script                            |
|       'swiss 'modern 'symbol 'system)                                      |
| ```                                                                        |
+----------------------------------------------------------------------------+
```

Sets the delta’s font family. See
get-family.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-style-delta set-size-add v) → void? |
| v: byte?                                   |
+---------------------------------------------+
```

Sets the additive font size shift (applied
after the multiplicative factor).

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-style-delta set-size-in-pixels-off v) → void? |
| v: any/c                                             |
+-------------------------------------------------------+
```

See style-delta%.

```
+------------------------------------------------------+
| [method]                                             |
|                                                      |
| (send a-style-delta set-size-in-pixels-on v) → void? |
| v: any/c                                            |
+------------------------------------------------------+
```

See style-delta%.

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-style-delta set-size-mult v) → void? |
| v: real?                                    |
+----------------------------------------------+
```

Sets the multiplicative font size shift (applied before the additive factor).

```
+------------------------------------------------------------------+
| [method]                                                         |
|                                                                  |
| (send a-style-delta set-smoothing-off v) → void?                 |
| v: (or/c 'base 'default 'partly-smoothed 'smoothed 'unsmoothed) |
| (or/c 'base 'default 'partly-smoothed                            |
| 'smoothed 'unsmoothed)                                           |
|                                                                  |
| ```racket                                                        |
| (or/c 'base 'default 'partly-smoothed                            |
|       'smoothed 'unsmoothed)                                     |
| ```                                                              |
+------------------------------------------------------------------+
```

See style-delta%.

```
+------------------------------------------------------------------+
| [method]                                                         |
|                                                                  |
| (send a-style-delta set-smoothing-on v) → void?                  |
| v: (or/c 'base 'default 'partly-smoothed 'smoothed 'unsmoothed) |
| (or/c 'base 'default 'partly-smoothed                            |
| 'smoothed 'unsmoothed)                                           |
|                                                                  |
| ```racket                                                        |
| (or/c 'base 'default 'partly-smoothed                            |
|       'smoothed 'unsmoothed)                                     |
| ```                                                              |
+------------------------------------------------------------------+
```

See style-delta%.

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-style-delta set-style-off v) → void? |
| v: (or/c 'base 'normal 'italic 'slant)      |
+----------------------------------------------+
```

See style-delta%.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-style-delta set-style-on v) → void? |
| v: (or/c 'base 'normal 'italic 'slant)     |
+---------------------------------------------+
```

See style-delta%.

```
+-----------------------------------------------------------------+
| [method]                                                        |
|                                                                 |
| (send a-style-delta set-transparent-text-backing-off v) → void? |
| v: any/c                                                       |
+-----------------------------------------------------------------+
```

See style-delta%.

```
+----------------------------------------------------------------+
| [method]                                                       |
|                                                                |
| (send a-style-delta set-transparent-text-backing-on v) → void? |
| v: any/c                                                      |
+----------------------------------------------------------------+
```

See style-delta%.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send a-style-delta set-underlined-off v) → void? |
| v: any/c                                         |
+---------------------------------------------------+
```

See style-delta%.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-style-delta set-underlined-on v) → void? |
| v: any/c                                        |
+--------------------------------------------------+
```

See style-delta%.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-style-delta set-weight-off v) → void? |
| v: (or/c 'base 'normal 'bold 'light)         |
+-----------------------------------------------+
```

See style-delta%.

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-style-delta set-weight-on v) → void? |
| v: (or/c 'base 'normal 'bold 'light)        |
+----------------------------------------------+
```

See style-delta%.
