<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/editor-overview.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/editor-overview.html -->
<!-- Canonical English source for Japanese translation -->

## 5 Editors

The editor toolbox provides a foundation for two common kinds of
applications:

- Programs that need a sophisticated text editor —
The simple text field control is inadequate for text-intensive
applications. Many programs need editors that can handle multiple
fonts and non-text items.
- Programs that need a canvas with dragable objects —
The drawing toolbox provides a generic drawing surface for plotting
lines and boxes, but many applications need an interactive canvas,
where the user can drag and resize individual objects.

Both kinds of applications need an extensible editor that can handle
text, images, programmer-defined items, and even embedded
editors. The difference between them is the layout of items. The
editor toolbox therefore provides two kinds of editors via two
classes:

- text% — in a text editor, items are
automatically positioned in a paragraph flow.
- pasteboard% — in a pasteboard editor,
items are explicitly positioned and dragable.

This editor architecture addresses the full range of real-world
issues for an editor—including cut-and-paste, extensible file
formats, and layered text styles—while supporting a high level of
extensibility. Unfortunately, the system is fairly complex as a
result, and using the editor classes effectively requires a solid
understanding of the structure and terminology of the editor
toolbox. Nevertheless, enough applications fit one (or both) of the
descriptions above to justify the depth and complexity of the toolbox
and the learning investment required to use it.

A brief example illustrates how editors work. To start, an editor
needs an editor-canvas% to display its contents. Then, we
can create a text editor and install it into the canvas:

```racket
(define f (new frame% [label "Simple Edit"]
                      [width 200]
                      [height 200]))
(define c (new editor-canvas% [parent f]))
(define t (new text%))
(send c set-editor t)
(send f show #t)
```

At this point, the editor is fully functional: the user can type text
into the editor, but no cut-and-paste or undo operations are
available. We can support all of the standard operations on an editor
via the menu bar:

```racket
(define mb (new menu-bar% [parent f]))
(define m-edit (new menu% [label "Edit"] [parent mb]))
(define m-font (new menu% [label "Font"] [parent mb]))
(append-editor-operation-menu-items m-edit #f)
(append-editor-font-menu-items m-font)
(send t set-max-undo-history 100)
```

Now, the standard cut-and-paste operations work and so does undo, and
the user can even set font styles. The editor is created with no undo
history stack, set-max-undo-history is used to set
a non-zero stack, so undo operations can be recorded. The user can
also insert an embedded editor by selecting Insert Text
from the Edit menu; after selecting the menu item, a box
appears in the editor with the caret inside. Typing with the caret in
the box stretches the box as text is added, and font operations apply
wherever the caret is active. Text on the outside of the box is
rearranged as the box changes sizes. Note that the box itself can be
copied and pasted.

The content of an editor is made up of snips. An
embedded editor is a single snip from the embedding editor’s
point-of-view. To encode immediate text, a snip can be a single
character, but more often a snip is a sequence of adjacent characters
on the same line. The find-snip method extracts a snip
from a text editor:

```racket
(send t find-snip 0 'after)
```

The above expression returns the first snip in the editor, which may
be a string snip (for immediate text) or an editor snip (for an
embedded editor).

An editor is not permanently attached to any display. We can take the
text editor out of our canvas and put a pasteboard editor in the
canvas, instead:

```racket
(define pb (new pasteboard%))
(send c set-editor pb)
```

With the pasteboard editor installed, the user can no longer type
characters directly into the editor (because a pasteboard does not
support directly entered text). However, the user can cut text from
elsewhere and paste it into pasteboard, or select one of the
Insert menu items in the Edit menu. Snips are
clearly identifiable in a pasteboard editor (unlike a text editor)
because each snip is separately dragable.

We can insert the old text editor (which we recently removed from the
canvas) as an embedded editor in the pasteboard by explicitly
creating an editor snip:

```racket
(define s (make-object editor-snip% t)); t is the old text editor
(send pb insert s)
```

An individual snip cannot be inserted into different editors at the
same time, or inserted multiple times in the same editor:

```racket
(send pb insert s); no effect
```

However, we can make a deep copy of the snip and insert the copy into
the pasteboard:

```racket
(send pb insert (send s copy))
```

Applications that use the editor classes typically derive new versions
of the text% and pasteboard% classes. For
example, to implement an append-only editor (which allows insertions
only at the end and never allows deletions), derive a new class from
text% and override the
can-insert? and
can-delete? methods:

```racket
(define append-only-text%
  (class text%
    (inherit last-position)
    (define/augment (can-insert? s l) (= s (last-position)))
    (define/augment (can-delete? s l) #f)
    (super-new)))
```

### 5.1 Editor Structure and Terminology

The editor toolbox supports extensible and nestable editors by
decomposing an editor assembly into three functional parts:

- The editor itself stores the state of the text or
pasteboard and handles most events and editing operations. The
editor<%> interface defines the core editor functionality,
but editors are created as instances of text% or
pasteboard%.
- A snip is a segment of information within the
editor. Each snip can contain a sequence of characters, a picture,
or an interactive object (such as an embedded editor). In a text
editor, snips are constrained to fit on a single line and generally
contain data of a single type. The snip% class implements a
basic snip and serves as the base for implementing new snips; see
Implementing New Snips. Other snip classes include string-snip% for
managing text, image-snip% for managing pictures, and
editor-snip% for managing embedded editors.
- A display presents the editor on the screen. The
display lets the user scroll around an editor or change editors. Most
displays are instances of the editor-canvas% class, but the
editor-snip% class also acts as a display for embedded
editors.

These three parts are illustrated by a simple word processor. The
editor corresponds to the text document. The editor object receives
keyboard and mouse commands for editing the text. The text itself is
distributed among snips. Each character could be a separate snip, or
multiple characters on a single line could be grouped together into a
snip. The display roughly corresponds to the window in which the
text is displayed. While the editor manages the arrangement of the
text as it is displayed into a window, the display determines which
window to draw into and which part of the editor to display.

Each selectable entity in an editor is an item. In a
pasteboard, all selection and dragging operations work on snips, so
there is a one-to-one correspondence between snips and items. In an
editor, one snip contains one or more consecutive items, and every
item belongs to some snip. For example, in a simple text editor, each
character is an item, but multiple adjacent characters may be grouped
into a single snip. The number of items in a snip is the snip’s
count.

Each place where the insertion point can appear in a text editor is a
position. A text editor with n items contains
n+1 positions: one position before each item, and one position
after the last item.

The order of snips within a pasteboard determines each snip’s drawing
plane. When two snips overlap within the pasteboard, the snip that is
earlier in the order is in front of the other snip (i.e., the former
is drawn after the latter, such that the former snip may cover part
of the latter snip).

When an editor is drawn into a display, each snip and position has a
location. The location of a position or snip is specified
in coordinates relative to the top-left corner of the
editor. Locations in an editor are only meaningful when the editor is
displayed.

#### 5.1.1 Characters and Graphemes

An item corresponds to a Racket
character in an editor with text. Some things that a user would
perceive as a character are composed of multiple Racket characters,
however, such as a pirate-flag emoji (which uses a four-character
encoding) or “e” plus an accent modifier (which also has a single
character representation, but might be represented through those two
characters). A grapheme is an approximation to a
user-perceived character as defined by the Unicode grapheme-cluster
specification. Racket provides support for graphemes though functions like
string-grapheme-count and char-grapheme-step.

Working with graphemes in a text editor requires extra care. Methods
like grapheme-position in text% and position-grapheme in text% convert between item and grapheme indices, but
most operations are based in item positions, and they are generally
not constrained to preserve grapheme-cluster sequences. A grapheme
cluster that is within a single snip will render as a single
grapheme, but a grapheme cluster that spans a snip boundary will be
rendered as two partial graphemes. The insert in text% method
takes optional arguments to trigger the detection of grapheme
sequences that would span the existing and inserted content and
ensure that the sequences are kept together.

A small number of text% methods are grapheme-sensitive by
default: delete, insert of a character,
and move-position.

#### 5.1.2 Administrators

Two extra layers of administration manage the display-editor and
editor-snip connections. An editor never communicates directly with
a display; instead, it always communicates with an editor
administrator, an instance of the editor-admin% class,
which relays information to the display. Similarly, a snip
communicates with a snip administrator, an instance of the
snip-admin% class.

The administrative layers make the editor hierarchy flexible without
forcing every part of an editor assembly to contain the functionality
of several parts. For example, a text editor can be a single
item within another editor; without administrators, the
text% class would also have to contain all the functionality
of a display (for the containing editor) and a snip (for
the embedded editor). Using administrators, an editor class can serve
as both a containing and an embedded editor without directly
implementing the display and snip functionality.

A snip belongs to at most one editor via a single administrator. An
editor also has only one administrator at a time. However, the
administrator that connects the editor to the standard
display (i.e., an editor canvas) can work with other such
administrators. In particular, the administrator of an
editor-canvas% (each one has its own administrator) can work
with other editor-canvas% administrators, allowing an editor
to be displayed in multiple editor-canvas% windows at the
same time.

When an editor is displayed by multiple canvases, one of the canvases’
administrators is used as the editor’s primary administrator. To
handle user and update events for other canvases, the editor’s
administrator is temporarily changed and then restored through the
editor’s set-admin method. The return value of the
editor’s get-admin method thus depends on the
context of the call.

#### 5.1.3 Styles

A style, an instance of the style<%> interface,
parameterizes high-level display information that is common to all
snip classes. This includes the font, color, and alignment for
drawing the item. A single style is attached to each snip.

Styles are hierarchical: each style is defined in terms of another
style. There is a single root style, named
"Basic", from which all other styles in an editor are
derived. The difference between a base style and each of its derived
style is encoded in a style delta (or simply
delta). A delta encodes changes such as

- change the font family to X;
- enlarge the font by adding Y to the point size;
- toggle the boldness of the font; or
- change everything to match the style description Z.

Style objects are never created separately; rather, they are always
created through a style list, an instance of the
style-list% class. A style list manages the styles,
servicing external requests to find a particular style, and it
manages the hierarchical relationship between styles. A global style
list is available, the-style-list, but new style
lists can be created for managing separate style hierarchies. For
example, each editor will typically have its own style list.

Each new style is defined in one of two ways:

- A derived style is defined in terms of a base style
and a delta. Every style (except for the root style) has a base
style, even if it does not depend on the base style in any way (i.e.,
the delta describes a fixed style rather than extensions to an
existing style). (This is the usual kind of style inheritance, as
found in word processors such as Microsoft Word.)
- A join style is defined in terms of two other styles:
a base style and a shift style. The meaning of a join style
is determined by reinterpreting the shift style; in the
reinterpretation, the base style is used as the root style
for the shift style. (This is analogous to multi-level
styles, like the paragraph and character styles in FrameMaker. In
this analogy, the paragraph style is the base style, and the
character style is the shift style. However, FrameMaker allows only
those two levels; with join styles support any number of levels.)

Usually, when text is inserted into a text editor, it
inherits the style of the preceding snip. If text is inserted into an
empty editor, the text is usually assigned a style called
"Standard". By default, the "Standard" style is
unmodified from the root style. The default style name can be changed
by overriding default-style-name.

The exception to the above is when change-style in text% is
called with the current selection position (when the
selection is a position and not a range). In that case,
the style is remembered, and if the next editor-modifying action is a
text insertion, the inserted text gets the remembered style.

See get-styles-sticky in text% for more information about the
style of inserted text.

### 5.2 File Format

To allow editor content to be saved to a file, the editor classes
implement a special file format called WXME. (The format is
used when cutting and pasting between applications or eventspaces,
too). The file format is not documented, except that it begins
WXME01‹digit›‹digit› ##. Otherwise, the
load-file and save-file methods
define the format internally. The file format is the same for text
and pasteboard editors. When a pasteboard saves its content to a
file, it saves the snips from front to back, and also includes extra
location information. The wxme library provides
utilities for manipulating WXME files.

Editor data is read and written using editor-stream-in% and
editor-stream-out% objects. Editor information can only be
read from or written to one stream at a time. To write one or more
editors to a stream, first call the function
write-editor-global-header to write initialization data into
an output stream. When all editors are written to the stream, call
write-editor-global-footer. Similarly, reading editors from
a stream is initialized with read-editor-global-header and
finalized with read-editor-global-footer. Optionally, to
support streams that span versions of Racket, use
write-editor-version and read-editor-version before
the header operations.

The editor file data format can be embedded within another file, and
it can be extended with new kinds of data. The editor file format can
be extended in two ways: with snip- or content-specific data, and
with editor-specific global data. These are described in the
remainder of this section.

#### 5.2.1 Encoding Snips

The
generalized notion of a snip allows new snip types to be defined and
immediately used in any editor class. Also, when two applications
support the same kinds of snips, snip data can easily be cut and
pasted between them, and the same data files will be readable by each
program. This interoperability is due to a consistent encoding
mechanism that is built into the snip system.

Graceful and extensible encoding of snips requires that
two issues are addressed:

- The encoding function for a snip can be associated with the snip
itself. To convert a snip from an encoded representation (e.g., as
bytes in a file) to a memory object, a decoding function must be
provided for each type of snip. Furthermore, a list of such decoders
must be available to the high-level decoding process. This decoding
mapping is defined by associating a snip class object to
every snip. A snip class is an instance of the snip-class%
class.
- Some editors may require additional information to be stored
about a snip; this information is orthogonal to the type-specific
information stored by the snip itself. For example, a pasteboard
needs to remember a snip’s location, while a text editor
does not need this information. If data is being cut and pasted from
one pasteboard to another, then information about relative
locations needs to be maintained, but this information
should not inhibit pasting into an editor. Extra data is associated
with a snip through editor data objects, which are
instances of the editor-data% class; decoding requires that
each editor data object has an editor data class, which is
an instance of the editor-data-class% class.

Snip classes, snip data, and snip data classes solve problems related
to encoding and decoding snips. In an application that has no need
for saving files or cut-and-paste, these issues can be safely
ignored.

##### 5.2.1.1 Snip Classes

Each snip can be associated to a snip class. This “class”
is not a class description in the programmer’s language; it is an
object which provides a way to create new snips of the appropriate
type from an encoded snip specification.

Snip class objects can be added to the eventspace-specific
snip class list, which is returned by
get-the-snip-class-list. When a snip is encoded, the snip’s
class name is associated with the encoding; when the snip needs to be
decoded, then the snip class list is searched by name to find the
snip’s class. The snip class will then provide a decoding function
that can create a new snip from the encoding.

If a snip class’s name is of the form
"((lib...) (lib...))",
then the snip class implementation can be loaded on
demand. The name is parsed using read; if the result has the
form ((libstring...)(libstring...)), then the first
element used with dynamic-require along with
'snip-class. If the dynamic-require result is a
snip-class% object, then it is inserted into the current
eventspace’s snip class list, and loading or saving continues using
the new class.

The second lib form in "((lib...) (lib...))"
supplies a reader for a text-only version of the snip. See
Snip Class Mapping for more information on how
such snipclasses work (and generally see the
wxme library).

A snip class’s name can also be just "(lib...)", which is
used like the first part of the two-lib form. However, this
form provides no information for the text-only wxme
reader.

For an example snip implementation and its associated snip-class
implementation, see Implementing New Snips.

##### 5.2.1.2 Editor Data

While a snip belongs to an editor, the editor may store extra
information about a snip in some specialized way. When the snip is to
be encoded, this extra information needs to be put into an
editor data object so that the extra information can be
encoded as well. In a text editor, extra information can be
associated with ranges of items, as well as snips.

Just as a snip must be associated with a snip class to be decoded (see
Snip Classes), an editor data object needs an editor
data class for decoding. Every editor data class object can be added
to the eventspace-specific editor data class list, returned
by get-the-editor-data-class-list. Alternatively, like snip
classes (see Snip Classes), editor data class names
can use the form "((lib...) (lib...))" to enable
on-demand loading. The corresponding module should export an
editor-data-class% object named 'editor-data-class.

To store and load information about a snip or region in an editor:

- derive new classes from editor-data% and
editor-data-class%.
- derive a new class from the text% or
pasteboard% class, and override the get-snip-data and set-snip-data methods and/or the
get-region-data and set-region-data
methods.Note: the get-region-data and set-region-data methods are called for cut-and-paste encoding, but
not for file-saving encoding; see Global Data: Headers and Footers for
information on extending the file format.

#### 5.2.2 Global Data: Headers and Footers

The editor file format provides for adding extra global data in
special header and footer sections. To save and load special header
and/or footer records:

- Pick a name for each header/footer record. This name should not
conflict with any other header/footer record name in use, and no one
else should use these names. All names beginning with “wx” are
reserved for internal use. By tagging extra header and footer records
with a unique name, the file can be safely loaded in an installation that
does not support the records.
- Derive a new class from the text% or
pasteboard% class, and override the write-headers-to-file, write-footers-to-file,
read-header-from-file and/or read-footer-from-file methods.

When an editor is saved, the methods write-headers-to-file and write-footers-to-file
are invoked; at this time, the derived text% or
pasteboard% object has a chance to save records. To write a
header/footer record, first invoke the begin-write-header-footer-to-file method, at which point the record
name is provided. Once the record is written, call end-write-header-footer-to-file.

When an editor is loaded and a header/footer record is encountered,
the read-header-from-file or read-footer-from-file method is invoked, with the record name as the
argument. If the name matches a known record type, then the data can
be loaded.

See also write-headers-to-file and
read-header-from-file.

### 5.3 End of Line Ambiguity

Because an editor can force a line break even when there is no
newline item, a position alone does not always
specify a location for the caret. Consider the last
position of a line that is soft-broken (i.e., no newline
is present): there is no item between the last
item of the line and the first item of the next
line, so two locations (one end-of-line and one
start-of-line) map to the same position.

For this reason, position-setting and
position-getting methods often have an extra argument. In
the case of a position-setting method, the argument
specifies whether the caret should be drawn at the left or right side
of the page (in the event that the location is doubly
defined); #t means that the caret should be drawn on the
right side. Similarly, methods which calculate a position
from a location will take an extra boxed boolean; the box
is filled with #t if the position is ambiguous and it came
from a right-side location, or #f otherwise.

### 5.4 Implementing New Snips

To support new kinds of content within an editor, derive a subclass of snip%
to implement a new kind of snip.
In deriving a new snip implementation, the following methods of snip%
must be overridden to
create a useful snip:

- get-extent
- draw
- copy
- resize if the snip can be resized by the user
- partial-offset if the snip can contain more than
one item
- split if the snip can contain more than one item
- size-cache-invalid if the snip caches the result to get-extent
- get-text (not required)
- find-scroll-step, get-num-scroll-steps, and get-scroll-step-offset if the snip can contain more than one
scroll position
- set-unmodified if the snip’s internal state can
be modified by the user, and call modified
in the snip’s administrator when the state changes the first
time

If a snip can contain more than one item, then the snip’s count
must be maintained as well.

To define a class of snips that can be saved or cut-and-pasted (see also
Snip Classes):

- Create an instance of snip-class%, implementing the
read method. Export the
snip-class% instance as snip-class from a
module, and use a classname of the form "(lib...)" as
described in Snip Classes.
- For each instance of the snip class, set the snip’s class object
with set-snipclass.
- Override the copy method.
- Override the write method.

In deriving a new snip-class% class:

- Set the classname using set-classname.
- Set the version using
set-version.
- Install the class into the list returned by
get-the-snip-class-list using the
add method. Note that if the same
name is inserted into the same class list multiple times, all
but the first insertion is ignored.

To define a class of snips that read specially with
open-input-text-editor:

- Make your snip% class implement readable-snip<%>.
- Implement the read-special method.

As an example, the following module implements a snip that draws a
circle. Clicking on the snip causes the circle to grow. To enable
copying an instance of the snip from one program/eventspace to
another, the module should be `"main.rkt"` a
`"circle-snip"` directory that is installed as a
`"circle-snip"` package. The snip also has a wxme
reader implementation following it that must be installed as
the file `"wxme-circle-snip.rkt"` in the `"circle-snip"`
directory.

```racket
  #lang racket/base
  (require racket/class
           racket/snip
           racket/format)

  (provide circle-snip%
           (rename-out [circle-snip-class snip-class]))

  (define circle-snip%
    (class snip%
      (inherit set-snipclass
               get-flags set-flags
               get-admin)
      (init-field [size 20.0])

      (super-new)
      (set-snipclass circle-snip-class)
      (send (get-the-snip-class-list) add circle-snip-class)
      (set-flags (cons 'handles-events (get-flags)))

      (define/override (get-extent dc x y
                                   [w #f]
                                   [h #f]
                                   [descent #f]
                                   [space #f]
                                   [lspace #f]
                                   [rspace #f])
        (define (maybe-set-box! b v) (when b (set-box! b v)))
        (maybe-set-box! w (+ 2.0 size))
        (maybe-set-box! h (+ 2.0 size))
        (maybe-set-box! descent 1.0)
        (maybe-set-box! space 1.0)
        (maybe-set-box! lspace 1.0)
        (maybe-set-box! rspace 1.0))

      (define/override (draw dc x y left top right bottom dx dy draw-caret)
        (send dc draw-ellipse (+ x 1.0) (+ y 1.0) size size))

      (define/override (copy)
        (new circle-snip% [size size]))

      (define/override (write f)
        (send f put size))

      (define/override (on-event dc x y editorx editory e)
        (when (send e button-down?)
          (set! size (+ 1.0 size))
          (define admin (get-admin))
          (when admin
            (send admin resized this #t))))))

  (define circle-snip-class%
    (class snip-class%
      (inherit set-classname)

      (super-new)
      (set-classname (~s '((lib "main.rkt" "circle-snip")
                           (lib "wxme-circle-snip.rkt" "circle-snip"))))

      (define/override (read f)
        (define size-b (box 0.0))
        (send f get size-b)
        (new circle-snip% [size (unbox size-b)]))))

  (define circle-snip-class (new circle-snip-class%))
```

This is the `"wxme-circle-snip.rkt"` file:

```racket
  #lang racket/base
  (require racket/class
           racket/format
           wxme
           pict)

  (provide reader)

  (define circle-reader%
    (class* object% (snip-reader<%>)
      (define/public (read-header version stream) (void))
      (define/public (read-snip text-only? version stream)
        (define size (send stream read-inexact "circle-snip"))
        (cond
          [text-only?
           (string->bytes/utf-8 (~s `(circle,size)))]
          [else
           (new circle-readable [size size])]))
      (super-new)))

  (define circle-readable
    (class* object% (readable<%>)
      (init-field size)
      (define/public (read-special source line column position)
;; construct a syntax object holding a 3d value that
;; is a circle from the pict library with an appropriate
;; source location
        (datum->syntax #f
                       (circle size)
                       (vector source line column position 1)
                       #f))
      (super-new)))

  (define reader (new circle-reader%))
```

### 5.5 Flattened Text

In plain text editors, there is a simple correlation between
positions and characters. In an editor<%> object,
this is not true much of the time, but it is still sometimes useful
to just “get the text” of an editor.

Text can be extracted from an editor in either of two forms:

- Simple text, where there is one character per
item. Items that are characters are mapped to
themselves, and all other items are mapped to a
period. Line breaks are represented by newline characters
(ASCII 10).
- Flattened text, where each item can map to
an arbitrary string. Items that are characters are still
mapped to themselves, but more complicated items can be
represented with a useful string determined by the item’s
snip. Newlines are mapped to platform-specific character sequences
(linefeed on Unix and Mac OS, and
linefeed–carriage return on Windows). This form is called
“flattened” because the editor’s items have been reduced
to a linear sequence of characters.

### 5.6 Caret Ownership

Within a frame, only one object can contain the keyboard focus. This
property must be maintained when a frame contains multiple editors in
multiple displays, and when a single editor contains other
editors as items.

When an editor has the keyboard focus, it will usually display the
current selection or a line indicating the insertion point; the line
is called the caret.

When an editor contains other editors, it keeps track of caret
ownership among the contained sub-editors. When the caret is taken
away from the main editor, it will revoke caret ownership from the
appropriate sub-editor.

When an editor or snip is drawn, an argument to the drawing method
specifies whether the caret should be drawn with the data or whether
a selection spans the data. This argument can be any of:

- 'no-caret — The caret should not be drawn at
all.
- 'show-inactive-caret — The caret should be drawn
as inactive; items may be identified as the local current selection,
but the keyboard focus is elsewhere.
- 'show-caret — The caret should be drawn to show
keyboard focus ownership.
- (consstartend) — The caret is owned by an
enclosing region, and its selection spans the current editor or snip;
in the case of the snip, the selection spans elements start
through end positions within the snip.

The 'show-inactive-caret display mode is useful for showing
selection ranges in text editors that do not have the focus. This
'show-inactive-caret mode is distinct from 'no-caret
mode; when editors are embedded, only the locally active editor shows
its selection.

### 5.7 Cut and Paste Time Stamps

Methods of editor<%> that use the clipboard — including
copy, cut, paste, and do-edit-operation — consume a time
stamp argument. This time stamp is generally extracted from the
mouse-event% or key-event% object that triggered
the clipboard action. Unix uses the time stamp to synchronize clipboard
operations among the clipboard clients.

All instances of event% include a time stamp, which can be
obtained using get-time-stamp.

If the time stamp is 0, it defaults to the current time. Using 0 as the
time stamp almost always works fine, but it is considered bad manners
on Unix.

### 5.8 Clickbacks

Clickbacks in a text% editor facilitate the
creation of simple interactive objects, such as hypertext. A
clickback is defined by associating a callback function with a range
of items in the editor. When a user clicks on the
items in that range, the callback function is invoked. For
example, a hypertext clickback would associate a range to a callback
function that changes the selection range in the editor.

By default, the callback function is invoked when the user releases
the mouse button. The set-clickback method accepts
an optional argument that causes the callback function to be invoked
on the button press, instead. This behavior is useful, for example,
for a clickback that creates a popup menu.

Note that there is no attempt to save clickback information when a
file is saved, since a clickback will have an arbitrary procedure
associated with it.

### 5.9 Internal Editor Locks

Instances of editor<%> have three levels of internal
locking:

- write locking — When an editor is internally locked for
writing, the abstract content of the editor cannot be changed (e.g.,
insertion attempts fail silently). However, snips in a text editor
can still be split and merged, and the text editor can be changed in
ways that affect the flow of lines. The
locked-for-write? method reports whether an
editor is currently locked for writing.
- flow locking — When a text editor is internally locked for
reflowing, it is locked for writing, the snip content of the editor
cannot change, the location of a snip cannot be computed if it
is not already known (see
locations-computed? in editor<%>), and the editor cannot
be drawn to a display. A request for uncomputed location
information during a flow lock produces undefined results. The
locked-for-flow? method reports whether an
editor is currently locked for flowing.
- read locking — When an editor is internally locked for
reading, no operations can be performed on the editor (e.g., a
request for the current selection position returns an undefined
value). This extreme state is used only during callbacks to its snips
for setting the snip’s administrator, splitting the snip, or merging
snips. The locked-for-read? method reports
whether an editor is currently locked for reading.

The internal lock for an editor is not affected by calls to
lock.

Methods that report location-independent information about an
editor never trigger a lock. A method that reports location
information may trigger a flow lock or write lock if the relevant
information has not been computed since the last modification to the
editor (see locations-computed? in editor<%>). A method
that modifies the editor in any way, even setting the selection
position, can trigger a read lock, flow lock, or write lock.

### 5.10 Editors and Threads

An editor is not tied to any particular thread or eventspace, except
to the degree that it is displayed in a canvas (which has an
eventspace). Concurrent access of an editor is always safe in the
weak sense that the editor will not become corrupted. However, because
editor access can trigger locks, concurrent access can produce
contract failures or unexpected results.

An editor supports certain concurrent patterns
reliably. One relevant pattern is updating an editor in one thread
while the editor is displayed in a canvas that is managed by a
different (handler) thread. To ensure that canvas refreshes are not
performed while the editor is locked for flowing, and to ensure that
refreshes do not prevent editor modifications, the following are
guaranteed:

- When an editor’s refresh method is
called during an edit sequence (which is started by
begin-edit-sequence and ended with
end-edit-sequence), the requested refresh
region is recorded, but the refresh is not performed. Instead, the
refresh is delayed until the end of the edit sequence.
- Attempting to start an edit sequence while a refresh is in
progress blocks until the refresh is complete.
- The on-display-size-when-ready method
calls on-display-size only when the editor
is not being refreshed and only when an edit sequence is not in
progress. In the first case, the
on-display-size call is delegated to the
refreshing thread to be called after the refresh completes. In the
second case, the on-display-size call is
delegated to the edit-sequence thread, to be called when the edit
sequence is complete.

Thus, disabling an editor-canvas% object (using
enable) is sufficient to ensure that a
background thread can modify an editor displayed by the canvas, as
long as all modifications are in edit sequences. The background
modifications will impair canvas refreshes minimally and temporarily,
and refreshes will not impair modifications in the background thread.

A second supported pattern is reading an editor in a background thread
while the editor may be manipulated in other threads. Since no
location-independent reads introduce locks, such reads in
the background thread will not impair other threads. However, other
threads may interfere with the background thread, causing it to
receive erroneous or out-of-date content information. This one-sided
guarantee is useful if the background thread’s work can be discarded
when the editor is modified.
