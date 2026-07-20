<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/area-container___.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/area-container___.html -->
<!-- Canonical English source for Japanese translation -->

```
+-----------------------------------------+---------+
| interfacearea-container<%>: interface? |         |
+-----------------------------------------+---------+
| implements:                             | area<%> |
+-----------------------------------------+---------+
```

An area-container<%> is a container area<%>.

All area-container<%> classes accept the following named
instantiation arguments:

- border — default is 0; passed to
border
- spacing — default is 0; passed to
spacing
- alignment — default is class-specific, such as
'(centertop) for vertical-panel%; the list
elements are passed to
set-alignment

```
+--------------------------------------------------+
| [method]                                         |
|                                                  |
| (send an-area-container add-child child) → void? |
| child: (is-a?/c subwindow<%>)                   |
+--------------------------------------------------+
```

Add the given subwindow to the set of non-deleted children. See also
change-children.

```
+--------------------------------------------------------+
| [method]                                               |
|                                                        |
| (send an-area-container after-new-child child) → void? |
| child: (is-a?/c subarea<%>)                           |
+--------------------------------------------------------+
```

Specification:
This method is called after a new containee area is created with this
area as its container. The new child is provided as an argument to
the method.

Default implementation:
Does nothing.

```
+-----------------------------------------------------------+
| [method]                                                  |
|                                                           |
| (send an-area-container begin-container-sequence) → void? |
+-----------------------------------------------------------+
```

Suspends geometry management in the container’s top-level window
until
end-container-sequence is called. The
begin-container-sequence and
end-container-sequence methods are used to bracket a set of container modifications so that
the resulting geometry is computed only once. A container sequence also
delays show and hide actions by
change-children, as well as the on-screen part of showing via
show until the sequence is complete. Sequence begin and end commands may
be nested arbitrarily deeply.

```
+----------------------------------------------------+
| [method]                                           |
|                                                    |
| (send an-area-container border) → spacing-integer? |
| (send an-area-container border margin) → void?     |
| margin: spacing-integer?                          |
+----------------------------------------------------+
```

Gets or sets the border margin for the container in pixels. This
margin is used as an inset into the panel’s client area before the
locations and sizes of the subareas are computed.

```
+-------------------------------------------------------------------------------+
| [method]                                                                      |
|                                                                               |
| (send an-area-container change-children filter) → void?                       |
| filter: ((listof (is-a?/c subarea<%>)). ->. (listof (is-a?/c subarea<%>))) |
| ((listof (is-a?/c subarea<%>))                                                |
|. ->. (listof (is-a?/c subarea<%>)))                                         |
|                                                                               |
| ```racket                                                                     |
| ((listof (is-a?/c subarea<%>))                                                |
|. ->. (listof (is-a?/c subarea<%>)))                                        |
| ```                                                                           |
+-------------------------------------------------------------------------------+
```

Takes a filter procedure and changes the container’s list of
non-deleted children. The filter procedure takes a list of
children areas and returns a new list of children areas. The new
list must consist of children that were created as subareas of
this area (i.e., change-children
cannot be used to change the parent of a subarea).

After the set of non-deleted children is changed, the container computes
the sets of newly deleted and newly non-deleted children. Newly deleted
windows are hidden. Newly non-deleted windows are shown.

Since non-window areas cannot be hidden, non-window areas cannot be
deleted. If the filter procedure removes non-window subareas,
an exception is raised and the set of non-deleted children is not changed.

```
+----------------------------------------------------------+
| [method]                                                 |
|                                                          |
| (send an-area-container container-flow-modified) → void? |
+----------------------------------------------------------+
```

Call this method when the result changes for an overridden flow-defining method, such as
place-children. The call notifies the geometry manager that the placement of the
container’s children needs to be recomputed.

The
reflow-containermethod only recomputes child positions when the geometry manager
thinks that the placement has changed since the last computation.

```
+----------------------------------------------------------------------------+
| [method]                                                                   |
|                                                                            |
| (send an-area-container container-size info)                               |
| → dimension-integer? dimension-integer?                                    |
| dimension-integer?                                                         |
| info: (listof (list/c dimension-integer? dimension-integer? any/c any/c)) |
| (listof (list/c dimension-integer?                                         |
| dimension-integer?                                                         |
| any/c                                                                      |
| any/c))                                                                    |
|                                                                            |
| ```racket                                                                  |
| (listof (list/c dimension-integer?                                         |
|                 dimension-integer?                                         |
|                 any/c                                                      |
|                 any/c))                                                    |
| ```                                                                        |
+----------------------------------------------------------------------------+
```

Called to determine the minimum size of a container. See
Geometry Management for more information.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send an-area-container delete-child child) → void? |
| child: (is-a?/c subwindow<%>)                      |
+-----------------------------------------------------+
```

Removes the given subwindow from the list of non-deleted children. See also
change-children.

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send an-area-container end-container-sequence) → void? |
+---------------------------------------------------------+
```

See
begin-container-sequence.

```
+----------------------------------------------------------------+
| [method]                                                       |
|                                                                |
| (send an-area-container get-alignment)                         |
| → (symbols 'right 'center 'left)(symbols 'bottom 'center 'top) |
| (symbols 'right 'center 'left)                                 |
| (symbols 'bottom 'center 'top)                                 |
+----------------------------------------------------------------+
```

Returns the container’s current alignment specification. See
set-alignment for more information.

```
+---------------------------------------+
| [method]                              |
|                                       |
| (send an-area-container get-children) |
| → (listof (is-a?/c subarea<%>))       |
+---------------------------------------+
```

Returns a list of the container’s non-deleted children. (The non-deleted
children are the ones currently managed by the container; deleted
children are generally hidden.) The order of the children in the list
is significant. For example, in a vertical panel, the first child in
the list is placed at the top of the panel.

```
+----------------------------------------------------------------------------+
| [method]                                                                   |
|                                                                            |
| (send an-area-container place-children                                     |
| → (listof (list/c dimension-integer? dimension-integer? dimension-integer? |
| dimension-integer?))                                                       |
| (listof (list/c dimension-integer?                                         |
| dimension-integer?                                                         |
| dimension-integer?                                                         |
| dimension-integer?))                                                       |
| info: (listof (list/c dimension-integer? dimension-integer? any/c any/c)) |
| (listof (list/c dimension-integer?                                         |
| dimension-integer?                                                         |
| any/c                                                                      |
| any/c))                                                                    |
| width: dimension-integer?                                                 |
| height: dimension-integer?                                                |
|                                                                            |
| ```racket                                                                  |
| (listof (list/c dimension-integer?                                         |
|                 dimension-integer?                                         |
|                 dimension-integer?                                         |
|                 dimension-integer?))                                       |
| ```                                                                        |
|                                                                            |
| ```racket                                                                  |
| (listof (list/c dimension-integer?                                         |
|                 dimension-integer?                                         |
|                 any/c                                                      |
|                 any/c))                                                    |
| ```                                                                        |
+----------------------------------------------------------------------------+
```

Called to place the children of a container. See Geometry Management
for more information.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send an-area-container reflow-container) → void? |
+---------------------------------------------------+
```

When a container window is not shown, changes to the container’s
set of children do not necessarily trigger the immediate
re-computation of the container’s size and its children’s sizes
and positions. Instead, the recalculation is delayed until the
container is shown, which avoids redundant computations between a
series of changes. The reflow-container method forces the immediate recalculation of
the container’s and its children’s sizes and locations.

Immediately after calling the reflow-container method, get-size,
get-client-size, get-width,
get-height, get-x, and
get-y report the manager-applied sizes and
locations for the container and its children, even when the
container is hidden. A container implementation can call
functions such as get-size at any time to
obtain the current state of a window (because the functions do
not trigger geometry management).

See also container-flow-modified.

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send an-area-container set-alignment        |
| horiz-align: (symbols 'right 'center 'left) |
| vert-align: (symbols 'bottom 'center 'top)  |
+----------------------------------------------+
```

Sets the alignment specification for a container, which determines how
it positions its children when the container has leftover space (when
a child was not stretchable in a particular dimension).

When the container’s horizontal alignment is 'left, the
children are left-aligned in the container and whitespace is inserted
to the right. When the container’s horizontal alignment is
'center, each child is horizontally centered in the
container. When the container’s horizontal alignment is
'right, leftover whitespace is inserted to the left.

Similarly, a container’s vertical alignment can be 'top,
'center, or 'bottom.

```
+-----------------------------------------------------+
| [method]                                            |
|                                                     |
| (send an-area-container spacing) → spacing-integer? |
| (send an-area-container spacing spacing) → void?    |
| spacing: spacing-integer?                          |
+-----------------------------------------------------+
```

Gets or sets the spacing, in pixels, used between subareas in the
container. For example, a vertical panel inserts this spacing between
each pair of vertically aligned subareas (with no extra space at the
top or bottom).
