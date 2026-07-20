<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/snip-class_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/snip-class_.html -->
<!-- Canonical English source for Japanese translation -->

```
+---------------------------+
| classsnip-class%: class? |
+---------------------------+
| superclass: object%       |
+---------------------------+
```

Useful snip classes are defined by instantiating derived subclasses of
snip-class%. A class derived from snip-class%
serves as a kind of “meta-class” for snips; each snip is associated
with an instance of snip-class% as its snip class.
See Implementing New Snips for more information about deriving a new
snip class.

```
+-------------------------------------------+
| [constructor]                             |
|                                           |
| (new snip-class%) → (is-a?/c snip-class%) |
+-------------------------------------------+
```

Creates a (useless) snip class.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-snip-class get-classname) → string? |
+---------------------------------------------+
```

Returns the class’s name, a string uniquely designating this snip
class. For example, the standard text snip classname is
"wxtext". Names beginning with wx are reserved.

A snip class name should usually have the form "((lib...)\n(lib...))" to enable on-demand loading of the class. See
Snip Classes for details.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-snip-class get-version) → exact-integer? |
+--------------------------------------------------+
```

Returns the version of this snip class. When attempting to load a file
containing a snip with the same class name but a different version,
the user is warned.

```
+--------------------------------------------------------+
| [method]                                               |
|                                                        |
| (send a-snip-class read f) → (or/c (is-a?/c snip%) #f) |
| f: (is-a?/c editor-stream-in%)                        |
+--------------------------------------------------------+
```

Specification:
Reads a snip from a given stream, returning a newly created snip as
the result or #f if there is an error.

Default implementation:
Returns #f.

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-snip-class read-header f) → boolean? |
| f: (is-a?/c editor-stream-in%)              |
+----------------------------------------------+
```

Specification:
Called to read header information that may be useful for every snip
read in this class. This method is only called once per editor read
session, and only if the stream contains header information for this
class.

The return value is #f if a read error occurs or anything else
otherwise.

See also write-header.

Default implementation:
Returns #t.

```
+-------------------------------------------------------------+
| [method]                                                    |
|                                                             |
| (send a-snip-class reading-version stream) → exact-integer? |
| stream: (is-a?/c editor-stream-in%)                        |
+-------------------------------------------------------------+
```

Returns the version number specified for this snip class for snips
currently being read from the given stream.

```
+------------------------------------------------+
| [method]                                       |
|                                                |
| (send a-snip-class set-classname name) → void? |
| name: string?                                 |
+------------------------------------------------+
```

Sets the class’s name. See also get-classname.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-snip-class set-version v) → void? |
| v: exact-integer?                        |
+-------------------------------------------+
```

Sets the version of this class. See get-version.

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-snip-class write-header stream) → boolean? |
| stream: (is-a?/c editor-stream-out%)              |
+----------------------------------------------------+
```

Specification:
Called to write header information that may be useful for every snip
written for this class. This method is only called once per editor
write session, and only if the editor contains snips in this class.

When reading the snips back in, read-header will
only be called if write-header writes some data
to the stream.

The return value is #f if a write error occurs or anything else
otherwise.

Default implementation:
Returns #t.
