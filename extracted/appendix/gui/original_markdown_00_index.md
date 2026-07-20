<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/index.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/index.html -->
<!-- Canonical English source for Japanese translation -->

# The Racket Graphical Interface Toolkit

Matthew Flatt,
Robert Bruce Findler,
and John Clements

```
+----------------------------+--------------------+
|  (require racket/gui/base) | package: `gui-lib` |
+----------------------------+--------------------+
+----------------------------+--------------------+
```

The
racket/gui/base library provides all of the class,
interface, and procedure bindings defined in this manual, in addition
to the bindings of racket/draw and
file/resource.

```
+------------------+--------------------+
| #lang racket/gui | package: `gui-lib` |
+------------------+--------------------+
+------------------+--------------------+
```

The
racket/gui language combines all bindings of the
racket language and the
racket/gui/base and racket/draw modules.

The racket/gui toolbox is roughly organized into two
parts:

- The windowing toolbox, for implementing windows,
buttons, menus, text fields, and other controls.
- The editor toolbox, for developing traditional text
editors, editors that mix text and graphics, or free-form layout
editors (such as a word processor, HTML editor, or icon-based file
browser).

Both parts of the toolbox rely extensively on the
racket/draw drawing library.

### Contents

- 1.1 Creating Windows
- 1.2 Drawing in Canvases
- 1.3 Core Windowing Classes
- 1.4 Geometry Management
- 1.4.1 Containees
- 1.4.2 Containers
- 1.4.3 Defining New Types of Containers
- 1.5 Mouse and Keyboard Events
- 1.6 Event Dispatching and Eventspaces
- 1.6.1 Event Types and Priorities
- 1.6.2 Eventspaces and Threads
- 1.6.3 Creating and Setting the Eventspace
- 1.6.4 Continuations and Event Dispatch
- 1.6.5 Logging
- 1.7 Animation in Canvases
- 1.8 Screen Resolution and Text Scaling
- 4.1 Dialogs
- 4.2 Eventspaces
- 4.3 System Menus
- 4.4 Global Graphics
- 4.5 Fonts
- 4.6 Miscellaneous
- 5.1 Editor Structure and Terminology
- 5.1.1 Characters and Graphemes
- 5.1.2 Administrators
- 5.1.3 Styles
- 5.2 File Format
- 5.2.1 Encoding Snips
- 5.2.1.1 Snip Classes
- 5.2.1.2 Editor Data
- 5.2.2 Global Data: Headers and Footers
- 5.3 End of Line Ambiguity
- 5.4 Implementing New Snips
- 5.5 Flattened Text
- 5.6 Caret Ownership
- 5.7 Cut and Paste Time Stamps
- 5.8 Clickbacks
- 5.9 Internal Editor Locks
- 5.10 Editors and Threads
- 9.1 Snip Class Mapping
- 9.1.1 Nested Editors
- 9.1.2 Images
- 9.2 DrRacket Comment Boxes
- 9.3 DrRacket XML Boxes
- 9.4 DrRacket Racket Boxes
- 9.5 DrRacket Text Boxes
- 9.6 DrRacket Fractions
- 9.7 DrRacket Teachpack Images
- 9.8 DrRacket Test-Case Boxes
