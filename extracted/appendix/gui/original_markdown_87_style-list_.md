<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/style-list_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/style-list_.html -->
<!-- Canonical English source for Japanese translation -->

```
+---------------------------+
| classstyle-list%: class? |
+---------------------------+
| superclass: object%       |
+---------------------------+
```

A style-list% object contains a set of style<%>
objects and maintains the hierarchical relationships between them. A
style<%> object can only be created through the methods of a
style-list% object. There is a global style list object,
the-style-list, but any number of independent lists can be
created for separate style hierarchies. Each editor creates its own
private style list.

See Styles for more information.

```
+-------------------------------------------+
| [constructor]                             |
|                                           |
| (new style-list%) → (is-a?/c style-list%) |
+-------------------------------------------+
```

The root style, named "Basic", is automatically created.

```
+------------------------------------------------------+
| [method]                                             |
|                                                      |
| (send a-style-list basic-style) → (is-a?/c style<%>) |
+------------------------------------------------------+
```

This method is final, so it cannot be overridden.

Returns the root style. Each style list has its own root style.

See also Preferences for information about the
'GRacket:default-font-size
preference.

```
+--------------------------------------------------------+
| [method]                                               |
|                                                        |
| (send a-style-list convert style) → (is-a?/c style<%>) |
| style: (is-a?/c style<%>)                             |
+--------------------------------------------------------+
```

Converts style, which can be from another style list, to a style
in this list. If style is already in this list, then style
is returned. If style is named and a style by that name is
already in this list, then the existing named style is returned.
Otherwise, the style is converted by converting its base style
(and shift style if style is a join style) and then creating
a new style in this list.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-style-list find-named-style name) |
| → (or/c (is-a?/c style<%>) #f)            |
| name: string?                            |
+-------------------------------------------+
```

Finds a style by name. If no such style can be found, #f is
returned.

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-style-list find-or-create-join-style |
| → (is-a?/c style<%>)                         |
| base-style: (is-a?/c style<%>)              |
| shift-style: (is-a?/c style<%>)             |
+----------------------------------------------+
```

Creates a new join style, or finds an appropriate existing one. The
returned style is always unnamed. See Styles for more
information.

The base-style argument must be a style within this style
list.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-style-list find-or-create-style |
| → (is-a?/c style<%>)                    |
| base-style: (is-a?/c style<%>)         |
| delta: (is-a?/c style-delta%)          |
+-----------------------------------------+
```

Creates a new derived style, or finds an appropriate existing one.
The returned style is always unnamed. See Styles for more
information.

The base-style argument must be a style within this style
list. If base-style is not a join style, if it has no name,
and if its delta can be collapsed with delta (see
collapse in style-delta%), then the collapsed delta is used in
place of delta, and the base style of base-style is
used in place of base-style; this collapsing and substitution
of base styles is performed recursively.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send a-style-list forget-notification key) → void? |
| key: any/c                                         |
+-----------------------------------------------------+
```

See notify-on-change.

The key argument is the value returned by notify-on-change.

```
+--------------------------------------+
| [method]                             |
|                                      |
| (send a-style-list index-to-style i) |
| → (or/c (is-a?/c style<%>) #f)       |
| i: exact-nonnegative-integer?       |
+--------------------------------------+
```

Returns the style associated with the given index, or #f for
a bad index. See also style-to-index.

```
+------------------------------------+
| [method]                           |
|                                    |
| (send a-style-list new-named-style |
| → (is-a?/c style<%>)               |
| name: string?                     |
| like-style: (is-a?/c style<%>)    |
+------------------------------------+
```

Creates a new named style, unless the name is already being used.

If name is already being used, then like-style is
ignored and the old style associated to the name is
returned. Otherwise, a new style is created for name with
the same characteristics (i.e., the same base style and same style
delta or shift style) as like-style.

The like-style style must be in this style list, otherwise
the named style is derived from the basic style with an empty style
delta.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-style-list notify-on-change f) → any/c |
| f: ((or/c (is-a?/c style<%>) #f). ->. any)  |
+------------------------------------------------+
```

Attaches a callback f to the style list. The callback
f is invoked whenever a style is modified.

Often, a change in one style will trigger a change in several other
derived styles; to allow clients to handle all the changes in a
batch, #f is passed to f as the changing style after a set of
styles has been processed.

The return value from notify-on-change is an
opaque key to be used with forget-notification.

The callback f replaces any callback for which it is
equal?, which helps avoid redundant notifications in case of
redundant registrations. The callback f is retained only
weakly (in the sense of make-weak-box), but it is retained
as long as any value that f impersonates is reachable; for
example, if f represents a function with a contract applied,
then f is retained for notification as long as the original
(pre-contract) function is reachable. The callback f is also
retained as long as the opaque key produced by notify-on-change is reachable.

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send a-style-list begin-style-change-sequence) → void? |
+---------------------------------------------------------+
```

Bracket changes to styles contained in a
style-list% with
begin-style-change-sequence and
end-style-change-sequence to avoid extra work
during the style changes.

Call to begin-style-change-sequence and
end-style-change-sequence can be nested
arbitrarily; changes to styles are not propagated to the
editor<%>s that use this style-list% until
the last call to end-style-change-sequence and
redundant calls are skipped at that point.

Added in version 1.5 of package `snip-lib`.

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-style-list end-style-change-sequence) → void? |
+-------------------------------------------------------+
```

Call to match calls to begin-style-change-sequence.

Added in version 1.5 of package `snip-lib`.

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send a-style-list number) → exact-nonnegative-integer? |
+---------------------------------------------------------+
```

Returns the number of styles in the list.

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-style-list replace-named-style |
| → (is-a?/c style<%>)                   |
| name: string?                         |
| like-style: (is-a?/c style<%>)        |
+----------------------------------------+
```

Like new-named-style, except that if the name is
already mapped to a style, the existing mapping is replaced.

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send a-style-list style-to-index style) |
| → (or/c exact-nonnegative-integer? #f)   |
| style: (is-a?/c style<%>)               |
+------------------------------------------+
```

Returns the index for a particular style. The index for a style’s base
style (and shift style, if it is a join style) is guaranteed to be
lower than the style’s own index. (As a result, the root style’s
index is always 0.) A style’s index can change whenever a new
style is added to the list, or the base style or shift style of
another style is changed.

If the given style is not in this list, #f is returned.
