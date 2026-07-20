<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/WXME_Decoding.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/WXME_Decoding.html -->
<!-- Canonical English source for Japanese translation -->

## 9 WXME Decoding

```
+-----------------+---------------------+
|  (require wxme) | package: `wxme-lib` |
+-----------------+---------------------+
+-----------------+---------------------+
```

The wxme library provides tools for
reading WXME editor<%>-format files (see
File Format) without the racket/gui library.

```
+---------------------------------+
| [procedure]                     |
|                                 |
| (is-wxme-stream? in) → boolean? |
| in: input-port?                |
+---------------------------------+
```

Peeks from in and returns #t if it starts with the
magic bytes indicating a WXME-format stream (see
File Format), #f otherwise.

```
+--------------------------------------------------+
| [procedure]                                      |
|                                                  |
| (wxme-port->text-port in [close?]) → input-port? |
| in: input-port?                                 |
| close?: any/c = #t                              |
+--------------------------------------------------+
```

Takes an input port whose stream starts with WXME-format data
and returns an input port that produces a text form of the WXME
content, like the result of opening a WXME file in DrRacket and saving
it as text.

Unlike wxme-port->port, this function may take liberties
with the snips in a way that would render a valid program invalid.
For example, if the wxme stream in contains
a bitmap image, then there may not be a reasonable text-only version
of it and thus wxme-port->port might turn what would have been
a valid Racket program into text that is a syntax error,
Nevertheless, the result may still be useful for human readers or
approximate program-processing tools that run only in a GUI-less context.

If close? is true, then closing the result port closes the
original port.

See Snip Class Mapping for information about the kinds of
non-text content that can be read.

```
+---------------------------------------------------------+
| [procedure]                                             |
|                                                         |
| (wxme-port->port in [close? snip-filter]) → input-port? |
| in: input-port?                                        |
| close?: any/c = #t                                     |
| snip-filter: (any/c. ->. any/c) = (lambda (x) x)     |
+---------------------------------------------------------+
```

Takes an input port whose stream starts with WXME-format data
and returns an input port that produces text content converted to
bytes, and non-text content as “special” values (see
read-char-or-special).

These special values produced by the new input port are different than
the ones produced by reading a file into an editor<%>
object. Instead of instances of the snip%, the special values
are typically simple extensions of object%. See
Snip Class Mapping for information about the kinds of
non-text content that can be read.

If close? is true, then closing the result port close the
original port.

The snip-filter procedure is applied to any special value
generated for the stream, and its result is used as an alternate
special value.

If a special value (possibly produced by the filter procedure) is an
object implementing the readable<%> interface, then the
object’s read-special method is called to produce
the special value.

```
+---------------------------+
| [procedure]               |
|                           |
| (extract-used-classes in) |
| (listof string?)          |
| in: input-port?          |
+---------------------------+
```

Returns two values: a list of snip-class names used by the given
stream, and a list of data-class names used by the stream. If the
stream is not a WXME stream, the result is two empty lists. The
given stream is not closed, and only data for a WXME stream (if
any) is consumed.

```
+----------------------------------------------+
| [procedure]                                  |
|                                              |
| (register-lib-mapping! str mod-path) → void? |
| str: string?                                |
| mod-path: (cons/c 'lib (listof string?))    |
+----------------------------------------------+
```

Maps a snip-class name to a quoted module path that provides a
reader% implementation. The module path must have the form
'(libstring...), where each string
contains only alpha-numeric ASCII characters,.,
_, -, and spaces.

```
+--------------------------------------------+
| [procedure]                                |
|                                            |
| (string->lib-path str gui?)                |
| → (or/c (cons/c 'lib (listof string?)) #f) |
| (or/c (cons/c 'lib (listof string?))       |
| #f)                                        |
| str: string?                              |
| gui?: any/c                               |
|                                            |
| ```racket                                  |
| (or/c (cons/c 'lib (listof string?))       |
|       #f)                                  |
| ```                                        |
+--------------------------------------------+
```

Returns a quoted module path for str for either
editor<%> mode when gui? is true, or
wxme mode when gui? is #f. For the
latter, built-in mappings and mapping registered via
register-lib-mapping! are used. If str cannot be
parsed as a library path, and if no mapping is available (either
because the class is built-in or not known), the result is
#f.

```
+-------------------------------------------------+
| [parameter]                                     |
|                                                 |
| (unknown-extensions-skip-enabled) → boolean?    |
| (unknown-extensions-skip-enabled skip?) → void? |
| skip?: any/c                                   |
+-------------------------------------------------+
```

A parameter. When set to #f (the default), an exception is raised when
an unrecognized snip class is encountered in a WXME
stream. When set to a true value, instances of unrecognized snip
classes are simply omitted from the transformed stream.

```
+----------------------------------------+
| [parameter]                            |
|                                        |
| (broken-wxme-big-endian?) → boolean?   |
| (broken-wxme-big-endian? big?) → void? |
| big?: any/c                           |
+----------------------------------------+
```

A parameter. Some old and short-lived WXME formats depended on
the endian order of the machine where the file was saved. Set this
parameter to pick the endian order to use when reading the file; the
default is the current platform’s endian order.

```
+------------------------+
| [procedure]            |
|                        |
| (wxme-read in) → any/c |
| in: input-port?       |
+------------------------+
```

Like read, but for a stream that starts with
WXME-format data. If multiple S-expressions are in the
WXME data, they are all read and combined with
'begin.

If racket/gui/base is available (as determined by
gui-available?), then open-input-text-editor is
used. Otherwise, wxme-port->port is used.

```
+-------------------------------------------------------------+
| [procedure]                                                 |
|                                                             |
| (wxme-read-syntax source-v in) → (or/c syntax? eof-object?) |
| source-v: any/c                                            |
| in: input-port?                                            |
+-------------------------------------------------------------+
```

Like read-syntax, but for a WXME-format input stream.
If multiple S-expressions are in the WXME data, they are all
read and combined with 'begin.

If racket/gui/base is available (as determined by
gui-available?), then open-input-text-editor is
used. Otherwise, wxme-port->port is used.

```
+--------------------------------------+
| interfacesnip-reader<%>: interface? |
+--------------------------------------+
+--------------------------------------+
```

An interface to be implemented by a reader for a specific kind of data
in a WXME stream. The interface has two methods:
read-header and read-snip.

```
+--------------------------------------+
| [method]                             |
|                                      |
| (send a-snip-reader read-header      |
| version: exact-nonnegative-integer? |
| stream: (is-a?/c stream<%>)         |
| (send a-snip-reader read-snip        |
| (if text-only?                       |
| bytes?                               |
| any/c)                               |
| text-only?: boolean?                |
| version: exact-nonnegative-integer? |
| stream: (is-a?/c stream<%>)         |
|                                      |
| ```racket                            |
| (if text-only?                       |
|     bytes?                           |
|     any/c)                           |
| ```                                  |
+--------------------------------------+
```

```
+-----------------------------------+
| interfacereadable<%>: interface? |
+-----------------------------------+
+-----------------------------------+
```

An interface to be implemented by values returned from a snip reader.
The only method is read-special.

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-readable read-special                   |
| source: any/c                                  |
| line: (or/c exact-nonnegative-integer? #f)     |
| column: (or/c exact-nonnegative-integer? #f)   |
| position: (or/c exact-nonnegative-integer? #f) |
+-------------------------------------------------+
```

```
+---------------------------------+
| interfacestream<%>: interface? |
+---------------------------------+
+---------------------------------+
```

Represents a WXME input stream for use by
snip-reader<%> instances.

```
+--------------------------------------------------------------------------+
| [method]                                                                 |
|                                                                          |
| (send a-stream read-integer what)                                        |
| → (or/c (integer-in (- (expt 2 31)) (expt 2 31)) (and/c real? inexact?)) |
| (or/c (integer-in (- (expt 2 31)) (expt 2 31))                           |
| (and/c real? inexact?))                                                  |
| what: any/c                                                             |
| what: any/c                                                             |
| what: any/c                                                             |
| what: any/c                                                             |
| what: any/c                                                             |
| what: any/c                                                             |
|                                                                          |
| ```racket                                                                |
| (or/c (integer-in (- (expt 2 31)) (expt 2 31))                           |
|       (and/c real? inexact?))                                            |
| ```                                                                      |
+--------------------------------------------------------------------------+
```

```
+------------------------------------------------+
| [procedure]                                    |
|                                                |
| (read-snip-from-port name who stream) → bytes? |
| name: string?                                 |
| who: any/c                                    |
| stream: (is-a?/c stream<%>)                   |
+------------------------------------------------+
```

Given name, which is expected to be the name of a snipclass,
uses that snipclass to read from the given stream at the current point
in that stream. Returns the processed bytes, much like the
read-snip method.

### 9.1 Snip Class Mapping

When graphical data is marshaled to the WXME format, it is associated
with a snip-class name to be matched with an implementation at load
time. See also Snip Classes.

Ideally, the snip-class name is generated as

```racket
(format "~s" (list '(lib string...)
                   '(lib string...)))
```

where each element of the formated list is a quoted module
path (see module-path?). The strings must contain only
alpha-numeric ASCII characters, plus., _,
-, and spaces, and they must not be "." or
"..".

In that case, the first quoted module path is used for loading
WXME files in graphical mode; the corresponding module must
provide snip-class object that implements the
snip-class% class. The second quoted module path is used by
the wxme library for converting WXME streams
without graphical support; the corresponding module must provide a
reader object that implements the snip-reader<%>
interface. Naturally, the snip-class% instance and
snip-reader<%> instance are expected to parse the same format, but
generate different results suitable for the different contexts (i.e.,
graphical or not).

If a snip-class name is generated as

```racket
(format "~s" '(lib string...))
```

then graphical mode uses the sole module path, and
wxme needs a compatibility mapping. Install one with
register-lib-mapping!.

If a snip-class name has neither of the above formats, then graphical
mode can use the data only if a snip class is registered for the name,
or if it the name of one of the built-in classes: "wxtext",
"wxtab", "wximage", or "wxmedia" (for
nested editors). The wxme library needs a
compatibility mapping installed with register-lib-mapping!
if it is not one of the built-in classes.

Several compatibility mappings are installed automatically for the
wxme library. They correspond to popular graphical
elements supported by various versions of DrRacket, including comment
boxes, fractions, XML boxes, Racket boxes, text boxes, and images
generated by the htdp/image teachpack (or, more
generally, from mrlib/cache-image-snip), and test-case
boxes.

For a port created by wxme-port->port, nested editors are
represented by instances of the editor% class provided by the
wxme/editor library. This class provides a single
method, get-content-port, which returns a port for
the editor’s content. Images are represented as instances of the
image% class provided by the wxme/image
library.

Comment boxes are represented as instances of a class that extends
editor% to implement readable<%>; see
wxme/comment. The read form produces a special comment
(created by make-special-comment), so that the comment box
disappears when read is used to read the stream; the
special-comment content is the readable instance. XML, Racket, and
text boxes similarly produce instances of editor% and
readable<%> that expand in the usual way; see
wxme/xml, wxme/scheme, and
wxme/text. Images from the
htdp/image teachpack
are packaged as instances of cache-image% from the
wxme/cache-image library. Test-case boxes are packaged
as instances of test-case% from the
wxme/test-case library.

#### 9.1.1 Nested Editors

```
+------------------------+---------------------+
|  (require wxme/editor) | package: `wxme-lib` |
+------------------------+---------------------+
+------------------------+---------------------+
```

```
+-----------------------+
| classeditor%: class? |
+-----------------------+
| superclass: object%   |
+-----------------------+
```

Instantiated for plain nested editors in a WXME stream in text
mode.

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send an-editor get-content-port) → input-port? |
+-------------------------------------------------+
```

#### 9.1.2 Images

```
+-----------------------+---------------------+
|  (require wxme/image) | package: `wxme-lib` |
+-----------------------+---------------------+
+-----------------------+---------------------+
```

```
+-------------------------+
| classimage%: class?    |
+-------------------------+
| superclass: image-snip% |
+-------------------------+
```

Instantiated for images in a WXME stream in text mode.
This class can just be treated like image-snip% and should
behave just like it, except it has the methods below in addition
in case old code still needs them. In other words, the methods
below are provided for backwards compatibility with earlier
verisons of Racket.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send an-image get-data) → (or/c bytes? #f) |
+---------------------------------------------+
```

### 9.2 DrRacket Comment Boxes

```
+-------------------------+---------------------+
|  (require wxme/comment) | package: `wxme-lib` |
+-------------------------+---------------------+
+-------------------------+---------------------+
```

```
+-----------------------------------+
| [value]                           |
|                                   |
| reader: (is-a?/c snip-reader<%>) |
+-----------------------------------+
```

A text-mode reader for comment boxes.

```
+-------------------------------+-------------+
| classcomment-editor%: class? |             |
+-------------------------------+-------------+
| superclass: editor%           |             |
| extends:                      | readable<%> |
+-------------------------------+-------------+
```

Instantiated for DrRacket comment boxes in a WXME stream for
text mode.

```
+--------------------------------------------------------------------------------+
| [method]                                                                       |
|                                                                                |
| (send a-comment-editor get-data) → #f                                          |
| method(send a-comment-editor read-special source line column position) → any/c |
| (send a-comment-editor read-special                                            |
| source: any/c                                                                 |
| line: (or/c exact-nonnegative-integer? #f)                                    |
| column: (or/c exact-nonnegative-integer? #f)                                  |
| position: (or/c exact-nonnegative-integer? #f)                                |
+--------------------------------------------------------------------------------+
```

### 9.3 DrRacket XML Boxes

```
+---------------------+---------------------+
|  (require wxme/xml) | package: `wxme-lib` |
+---------------------+---------------------+
+---------------------+---------------------+
```

```
+-----------------------------------+
| [value]                           |
|                                   |
| reader: (is-a?/c snip-reader<%>) |
+-----------------------------------+
```

A text-mode reader for XML boxes.

```
+---------------------------+-------------+
| classxml-editor%: class? |             |
+---------------------------+-------------+
| superclass: editor%       |             |
| extends:                  | readable<%> |
+---------------------------+-------------+
```

Instantiated for DrRacket XML boxes in a WXME stream for text
mode.

```
+----------------------------------------------------------------------------+
| [method]                                                                   |
|                                                                            |
| (send a-xml-editor get-data) → any/c                                       |
| method(send a-xml-editor read-special source line column position) → any/c |
| (send a-xml-editor read-special                                            |
| source: any/c                                                             |
| line: (or/c exact-nonnegative-integer? #f)                                |
| column: (or/c exact-nonnegative-integer? #f)                              |
| position: (or/c exact-nonnegative-integer? #f)                            |
+----------------------------------------------------------------------------+
```

### 9.4 DrRacket Racket Boxes

```
+------------------------+---------------------+
|  (require wxme/scheme) | package: `wxme-lib` |
+------------------------+---------------------+
+------------------------+---------------------+
```

```
+-----------------------------------+
| [value]                           |
|                                   |
| reader: (is-a?/c snip-reader<%>) |
+-----------------------------------+
```

A text-mode reader for Racket boxes.

```
+------------------------------+-------------+
| classscheme-editor%: class? |             |
+------------------------------+-------------+
| superclass: editor%          |             |
| extends:                     | readable<%> |
+------------------------------+-------------+
```

Instantiated for DrRacket Racket boxes in a WXME stream for text
mode.

```
+-------------------------------------------------------------------------------+
| [method]                                                                      |
|                                                                               |
| (send a-scheme-editor get-data) → any/c                                       |
| method(send a-scheme-editor read-special source line column position) → any/c |
| (send a-scheme-editor read-special                                            |
| source: any/c                                                                |
| line: (or/c exact-nonnegative-integer? #f)                                   |
| column: (or/c exact-nonnegative-integer? #f)                                 |
| position: (or/c exact-nonnegative-integer? #f)                               |
+-------------------------------------------------------------------------------+
```

### 9.5 DrRacket Text Boxes

```
+----------------------+---------------------+
|  (require wxme/text) | package: `wxme-lib` |
+----------------------+---------------------+
+----------------------+---------------------+
```

```
+-----------------------------------+
| [value]                           |
|                                   |
| reader: (is-a?/c snip-reader<%>) |
+-----------------------------------+
```

A text-mode reader for text boxes.

```
+----------------------------+-------------+
| classtext-editor%: class? |             |
+----------------------------+-------------+
| superclass: editor%        |             |
| extends:                   | readable<%> |
+----------------------------+-------------+
```

Instantiated for DrRacket text boxes in a WXME stream for text
mode.

```
+-----------------------------------------------------------------------------+
| [method]                                                                    |
|                                                                             |
| (send a-text-editor get-data) → #f                                          |
| method(send a-text-editor read-special source line column position) → any/c |
| (send a-text-editor read-special                                            |
| source: any/c                                                              |
| line: (or/c exact-nonnegative-integer? #f)                                 |
| column: (or/c exact-nonnegative-integer? #f)                               |
| position: (or/c exact-nonnegative-integer? #f)                             |
+-----------------------------------------------------------------------------+
```

### 9.6 DrRacket Fractions

```
+------------------------+---------------------+
|  (require wxme/number) | package: `wxme-lib` |
+------------------------+---------------------+
+------------------------+---------------------+
```

```
+-----------------------------------+
| [value]                           |
|                                   |
| reader: (is-a?/c snip-reader<%>) |
+-----------------------------------+
```

A text-mode reader for DrRacket fractions that generates exact,
rational numbers.

### 9.7 DrRacket Teachpack Images

```
+-----------------------------+---------------------+
|  (require wxme/cache-image) | package: `wxme-lib` |
+-----------------------------+---------------------+
+-----------------------------+---------------------+
```

```
+-----------------------------------+
| [value]                           |
|                                   |
| reader: (is-a?/c snip-reader<%>) |
+-----------------------------------+
```

A text-mode reader for images in a WXME stream generated by the
htdp/image teachpack—or, more generally, by
mrlib/cache-image-snip.

```
+----------------------------+
| classcache-image%: class? |
+----------------------------+
| superclass: object%        |
+----------------------------+
```

Instantiated for DrRacket teachpack boxes in a WXME stream for
text mode.

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send a-cache-image get-argb) → (vectorof byte?) |
+--------------------------------------------------+
```

### 9.8 DrRacket Test-Case Boxes

```
+---------------------------+---------------------+
|  (require wxme/test-case) | package: `wxme-lib` |
+---------------------------+---------------------+
+---------------------------+---------------------+
```

```
+-----------------------------------+
| [value]                           |
|                                   |
| reader: (is-a?/c snip-reader<%>) |
+-----------------------------------+
```

A text-mode reader for DrRacket test-case boxes in a WXME stream. It
generates instances of test-case%.

```
+--------------------------+
| classtest-case%: class? |
+--------------------------+
| superclass: object%      |
+--------------------------+
```

Instantiated for old-style DrRacket test-case boxes in a WXME
stream for text mode.

```
+--------------------------------------------------------+
| [method]                                               |
|                                                        |
| (send a-test-case get-comment) → (or/c #f input-port?) |
+--------------------------------------------------------+
```
