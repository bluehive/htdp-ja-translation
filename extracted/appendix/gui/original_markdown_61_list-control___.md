<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/list-control___.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/list-control___.html -->
<!-- Canonical English source for Japanese translation -->

```
+---------------------------------------+------------+
| interfacelist-control<%>: interface? |            |
+---------------------------------------+------------+
| implements:                           | control<%> |
+---------------------------------------+------------+
```

A list control gives the user a list of string items to choose from.
There are two built-in classes that implement
list-control<%>:

- choice% — presents the list in a popup menu (so
the user can choose only one item at a time)
- list-box% — presents the list in a scrolling box,
allowing the use to choose one item (if the style includes
'single) or any number of items

In either case, the set of user-selectable items can be changed
dynamically.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-list-control append item) → void? |
| item: label-string?                      |
+-------------------------------------------+
```

Adds a new item to the list of user-selectable items. The current
selection is unchanged (unless the list control is an empty choice
control, in which case the new item is selected).

```
+-------------------------------------+
| [method]                            |
|                                     |
| (send a-list-control clear) → void? |
+-------------------------------------+
```

Removes all user-selectable items from the control.

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-list-control delete n) → void? |
| n: exact-nonnegative-integer?         |
+----------------------------------------+
```

Deletes the item indexed by n (where items are indexed
from 0). If n is equal
to or larger than the number of items in the control, an exn:fail:contract exception is raised.

Selected items that are not deleted remain selected, and no other
items are selected.

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-list-control find-string s)    |
| → (or/c exact-nonnegative-integer? #f) |
| s: string?                            |
+----------------------------------------+
```

Finds a user-selectable item matching the given string. If no matching
choice is found, #f is returned, otherwise the index of the
matching choice is returned (where items are indexed from 0).

```
+---------------------------------------------------------------+
| [method]                                                      |
|                                                               |
| (send a-list-control get-number) → exact-nonnegative-integer? |
+---------------------------------------------------------------+
```

Returns the number of user-selectable items in the control (which is
also one more than the greatest index in the list control).

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-list-control get-selection)    |
| → (or/c exact-nonnegative-integer? #f) |
+----------------------------------------+
```

Returns the index of the currently selected item (where items are indexed
from 0). If the choice item currently contains no choices or no
selections, #f is returned. If multiple selections are
allowed and multiple items are selected, the index of the first
selection is returned.

```
+------------------------------------+
| [method]                           |
|                                    |
| (send a-list-control get-string n) |
| → (and/c immutable? label-string?) |
| n: exact-nonnegative-integer?     |
+------------------------------------+
```

Returns the item for the given index (where items are indexed from
0). If the provided index is larger than the greatest index in
the list control, an exn:fail:contract exception is raised.

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-list-control get-string-selection)   |
| → (or/c (and/c immutable? label-string?) #f) |
+----------------------------------------------+
```

Returns the currently selected item. If the control currently
contains no choices, #f is returned. If multiple selections
are allowed and multiple items are selected, the first selection is
returned.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-list-control set-selection n) → void? |
| n: exact-nonnegative-integer?                |
+-----------------------------------------------+
```

Selects the item specified by the given index (where items are indexed from
0). If the given index larger than the greatest index in the
list control, an exn:fail:contract exception is raised.

In a list box control, all other items are deselected, even if multiple
selections are allowed in the control. See also
select in list-box%.

The control’s callback procedure is not invoked when this method
is called.

The list control’s selection can be changed
by the user clicking the control, and such changes do not go through this method; use the control callback procedure (provided as an initialization argument) to
monitor selection changes.

```
+------------------------------------------------------+
| [method]                                             |
|                                                      |
| (send a-list-control set-string-selection s) → void? |
| s: string?                                          |
+------------------------------------------------------+
```

Selects the item that matches the given string. If no match
is found in the list control, an exn:fail:contract exception is raised.

In a list box control, all other items are deselected, even if multiple
selections are allowed in the control. See also
select in list-box%.

The control’s callback procedure is not invoked when this method
is called.

The list control’s selection can be changed
by the user clicking the control, and such changes do not go through this method; use the control callback procedure (provided as an initialization argument) to
monitor selection changes.
