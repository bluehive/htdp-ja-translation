<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/list-box_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/list-box_.html -->
<!-- Canonical English source for Japanese translation -->

> [image: list-box.png]

```
+-------------------------+-----------------+
| classlist-box%: class? |                 |
+-------------------------+-----------------+
| superclass: object%     |                 |
| extends:                | list-control<%> |
+-------------------------+-----------------+
```

A list box allows the user to select one or more string items from a
scrolling list. A list box is either a single-selection control (if
an item is selected, the previous selection is removed) or a
multiple-selection control (clicking an item toggles the item on or
off independently of other selections).

Whenever the user changes the selection in a list box, the list box’s
callback procedure is called. A callback procedure is provided as an
initialization argument when each list box is created.

A list box can have multiple columns with optional column headers. An
item in the list corresponds to a row that spans all columns. When
column headers are displayed, the column widths can be changed by a
user. In addition, columns can optionally support dragging by the
user to change the display order of columns, while the logical order
remains fixed.

List box rows and columns are indexed from 0.

See also choice%.

```
+--------------------------------------------------------------------------------+
| [constructor]                                                                  |
|                                                                                |
| (new list-box%                                                                 |
| → (is-a?/c list-box%)                                                          |
| label: (or/c label-string? #f)                                                |
| choices: (listof label-string?)                                               |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) (is-a?/c panel%) (is-a?/c    |
| pane%))                                                                        |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                       |
| (is-a?/c panel%) (is-a?/c pane%))                                              |
| callback: ((is-a?/c list-box%) (is-a?/c control-event%). ->. any) = (lambda |
| (c e) (void))                                                                  |
| ((is-a?/c list-box%) (is-a?/c control-event%)                                  |
|. ->. any)                                                                    |
| style: (listof (or/c 'single 'multiple 'extended 'vertical-label              |
| 'horizontal-label 'variable-columns 'column-headers 'clickable-headers         |
| 'reorderable-headers 'deleted)) = '(single)                                    |
| (listof (or/c 'single 'multiple 'extended                                      |
| 'vertical-label 'horizontal-label                                              |
| 'variable-columns 'column-headers                                              |
| 'clickable-headers 'reorderable-headers                                        |
| 'deleted))                                                                     |
| selection: (or/c exact-nonnegative-integer? #f) = #f                          |
| font: (is-a?/c font%) = view-control-font                                     |
| label-font: (is-a?/c font%) = normal-control-font                             |
| enabled: any/c = #t                                                           |
| vert-margin: spacing-integer? = 2                                             |
| horiz-margin: spacing-integer? = 2                                            |
| min-width: (or/c dimension-integer? #f) = #f                                  |
| min-height: (or/c dimension-integer? #f) = #f                                 |
| stretchable-width: any/c = #t                                                 |
| stretchable-height: any/c = #t                                                |
| columns: (cons/c label-string? (listof label-string?)) = '("Column")          |
| column-order: (or/c #f (listof exact-nonnegative-integer?)) = #f              |
|                                                                                |
| ```racket                                                                      |
| (or/c (is-a?/c frame%) (is-a?/c dialog%)                                       |
|       (is-a?/c panel%) (is-a?/c pane%))                                        |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| ((is-a?/c list-box%) (is-a?/c control-event%)                                  |
|. ->. any)                                                                   |
| ```                                                                            |
|                                                                                |
| ```racket                                                                      |
| (listof (or/c 'single 'multiple 'extended                                      |
|               'vertical-label 'horizontal-label                                |
|               'variable-columns 'column-headers                                |
|               'clickable-headers 'reorderable-headers                          |
|               'deleted))                                                       |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

If label is not #f, it is used as the list box
label. Otherwise, the list box will not display its label.

If & occurs in label, it
is specially parsed as for button%.

The choices list specifies the initial list of items
to appear in the list box. If the list box has multiple columns,
choices determines the content of the first column, and
other columns are initialized to the empty string.

The callback procedure is called when the user changes the list
box selection, by either selecting, re-selecting, deselecting, or
double-clicking an item. The type of the event provided to the
callback is 'list-box-dclick when the user double-clicks
on an item, or 'list-box otherwise.

The columns list determines the number of columns in the list
box. The column titles in columns are shown only if
style includes 'column-headers. If style
also includes 'clickable-headers, then a click on a header
triggers a call to callback with a
column-control-event% argument whose event type is
'list-box-column; for historical reasons,
'clickable-headers has no effect on Windows and
header clicks are always reported.

The style specification must include exactly one of the
following:

- 'single — Creates a single-selection list.
- 'multiple — Creates a multiple-selection list
where a single click deselects other items and selects a new
item. Use this style for a list when single-selection is common, but
multiple selections are allowed.
- 'extended — Creates a multiple-selection list where a
single click extends or contracts the selection by toggling the
clicked item. Use this style for a list when multiple selections are
the rule rather than the exception.

The 'multiple and 'extended styles determine a
platform-independent interpretation of unmodified mouse clicks, but
dragging, shift-clicking, control-clicking, etc. have
platform-standard interpretations. Whatever the platform-specific
interface, the user can always select disjoint sets of items or
deselect items (and leave no items selected). On some platforms, the
user can deselect the (sole) selected item in a 'single list
box.

If style includes 'vertical-label, then the list box is
created with a label above the control; if style does not include
'vertical-label (and optionally includes 'horizontal-label), then the
label is created to the left of the list box. If style includes 'deleted, then the list box is created as hidden,
and it does not affect its parent’s geometry; the list box can be made active later by calling
parent’s add-child method.

If style includes 'variable-columns, then the number
of columns in the list box can be changed via append-column
and delete-column.

If selection is an integer, it is passed to
set-selection to set the initial selection. The selection must be less than
the length of choices.

The font argument determines the font for the control content,
and label-font determines the font for the control label. For information about the enabled argument, see window<%>. For information about the horiz-margin and vert-margin
arguments, see subarea<%>. For information about the
min-width, min-height, stretchable-width, and
stretchable-height arguments, see area<%>.

It the column-order argument is not #f, it
determines the order in which logical columns are initially displayed. See
set-column-order for more information. If
style includes 'column-headers and
'reorderable-headers, then a user can reorder columns as
displayed (but the display order does not change the logical order of
the columns).

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-list-box append item [data]) → void? |
| item: label-string?                         |
| data: any/c = #f                            |
+----------------------------------------------+
```

Overrides append in list-control<%>.

Adds a new item to the list box with an associated “data” object.
The data object is not displayed in the list box; it is
provided merely as a convenience for use with get-data, possibly allowing a programmer to avoid managing a
separate item-to-data mapping in addition to the list box control.

See also append in list-control<%>.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-list-box append-column label) → void? |
| label: label-string?                         |
+-----------------------------------------------+
```

Adds a new column with title label to the list box, but only
if the list box is created with the 'variable-columns
style. The new column is logically the last column, and it is initially
displayed as the last column.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-list-box delete-column n) → void? |
| n: exact-nonnegative-integer?            |
+-------------------------------------------+
```

Deletes the column with logical position n, but only if the
list box is created with the 'variable-columns style, and
only if the list box currently has more than one column (i.e., the
number of columns can never be zero).

```
+-------------------------------------------------+
| [method]                                        |
|                                                 |
| (send a-list-box get-column-labels)             |
| → (cons/c label-string? (listof label-string?)) |
+-------------------------------------------------+
```

Returns the labels of the list box’s columns, and the number of
returned strings indicates the number of columns in the list box.

```
+---------------------------------------+
| [method]                              |
|                                       |
| (send a-list-box get-column-order)    |
| → (listof exact-nonnegative-integer?) |
+---------------------------------------+
```

Returns the display order of logical columns. Each column is
represented by its logical position in the result list, and the order
of the column positions indicates the display order.

See also set-column-order.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-list-box get-column-width column) |
| dimension-integer?                        |
| dimension-integer?                        |
| dimension-integer?                        |
| column: exact-nonnegative-integer?       |
+-------------------------------------------+
```

Gets the width of the column identified by column (in logical
positions, as opposed to display positions), which must be between 0
and one less than the number of columns.

The result includes the column’s current width as well as its minimum
and maximum widths to constrain the column size as adjusted by a user.

See also set-column-width.

```
+--------------------------------------+
| [method]                             |
|                                      |
| (send a-list-box get-data n) → any/c |
| n: exact-nonnegative-integer?       |
+--------------------------------------+
```

Returns the data for the item indexed by n, or #f
if there is no associated data. List box rows are indexed from 0. If
n is equal to or larger than the number of choices,
an exn:fail:contract exception is raised.

See also append and set-data.

```
+------------------------------------------+
| [method]                                 |
|                                          |
| (send a-list-box get-first-visible-item) |
| → exact-nonnegative-integer?             |
+------------------------------------------+
```

Reports the index of the item currently scrolled to the top of the
list box. List box rows are indexed from 0.

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-list-box get-label-font) → (is-a?/c font%) |
+----------------------------------------------------+
```

Returns the font used for the control’s label, which is optionally
supplied when a list box is created.

```
+---------------------------------------+
| [method]                              |
|                                       |
| (send a-list-box get-selections)      |
| → (listof exact-nonnegative-integer?) |
+---------------------------------------+
```

Returns a list of indices for all currently selected items.
List box rows are indexed from 0.

For single-selection lists, the result is always either null or
a list containing one number.

```
+---------------------------------------------+
| [method]                                    |
|                                             |
| (send a-list-box is-selected? n) → boolean? |
| n: exact-nonnegative-integer?              |
+---------------------------------------------+
```

Returns #t if the items indexed by n is selected,
#f otherwise. List box rows are indexed from 0. If n is equal to or
larger than the number of choices, an exn:fail:contract exception is raised.

A list box’s selection can be changed
by the user clicking the control, and such changes do not go through this method; use the control callback procedure (provided as an initialization argument) to
monitor selection changes.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-list-box number-of-visible-items) |
| → exact-positive-integer?                 |
+-------------------------------------------+
```

Returns the maximum number of items in the list box that are visible
to the user with the control’s current size (rounding down if the
exact answer is fractional, but returning at least 1).

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-list-box select n [select?]) → void? |
| n: exact-nonnegative-integer?               |
| select?: any/c = #t                         |
+----------------------------------------------+
```

Selects or deselects an item. For selection in a single-selection list
box, if a different choice is currently selected, it is automatically
deselected. For selection in a multiple-selection list box, other
selections are preserved, unlike
set-selection.

If select? is #f, the item indexed by n is
deselected; otherwise it is selected. List box rows are indexed from 0. If n is
equal to or larger than the number of choices, an exn:fail:contract exception is raised.

A list box’s selection can be changed
by the user clicking the control, and such changes do not go through this method; use the control callback procedure (provided as an initialization argument) to
monitor selection changes.

The control’s callback procedure is not invoked.

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-list-box set choices0 choices...) → void? |
| choices0: (listof label-string?)                  |
| choices: (listof label-string?)                   |
+----------------------------------------------------+
```

Clears the list box and installs a new list of items. The number of
choices0 plus choices lists must match the number of columns, and all
choices lists must have the same number of items, otherwise
an exn:fail:contract exception is raised.

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-list-box set-column-label   |
| column: exact-nonnegative-integer? |
| label: label-string?               |
+-------------------------------------+
```

Sets the label of the column identified by column (in logical
positions, as opposed to display positions), which must be between 0
and one less than the number of columns.

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send a-list-box set-column-order column-order) → void? |
| column-order: (listof exact-nonnegative-integer?)      |
+---------------------------------------------------------+
```

Sets the order in which logical columns are displayed. Each element of
column-order must identify a unique column by its logical
position, and all logical columns must be represented in the list.

See also get-column-order.

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-list-box set-column-width   |
| column: exact-nonnegative-integer? |
| width: dimension-integer?          |
| min-width: dimension-integer?      |
| max-width: dimension-integer?      |
+-------------------------------------+
```

Sets the width of the column identified by column (in logical
positions, as opposed to display positions), which must be between 0
and one less than the number of columns.

The width argument sets the current display width, while
min-width and max-width constrain the width of the
column when the user resizes it. The width argument must be
no less than min-width and no more than max-width.

The default width of a column is platform-specific, and the last
column of a list box may extend to the end of the control independent
of its requested size.

See also get-column-width.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-list-box set-data n data) → void? |
| n: exact-nonnegative-integer?            |
| data: any/c                              |
+-------------------------------------------+
```

Sets the associated data for item indexed by n. List box rows are indexed from 0. If
n is equal to or larger than the number of choices,
an exn:fail:contract exception is raised.

See also append.

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send a-list-box set-first-visible-item n) → void? |
| n: exact-nonnegative-integer?                     |
+----------------------------------------------------+
```

Scrolls the list box so that the item indexed by n is at the
top of the list box display. List box rows are indexed from 0. If n is equal to
or larger than the number of choices, an exn:fail:contract exception is raised.

A list box’s scroll position can be changed
by the user clicking the control, and such changes do not go through this method. A program
cannot detect when the scroll position
changes except by polling get-first-visible-item.

```
+-------------------------------------------------------+
| [method]                                              |
|                                                       |
| (send a-list-box set-string n label [column]) → void? |
| n: exact-nonnegative-integer?                        |
| label: label-string?                                 |
| column: exact-nonnegative-integer? = 0               |
+-------------------------------------------------------+
```

Sets the item indexed by n in logical column column.
List box rows and columns are indexed from 0. If n is
equal to or larger than the number of choices, or if column
is equal to or larger than the number of columns, an exn:fail:contract exception is raised.
