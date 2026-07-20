<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/editor-wordbreak-map_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/editor-wordbreak-map_.html -->
<!-- Canonical English source for Japanese translation -->

```
+-------------------------------------+
| classeditor-wordbreak-map%: class? |
+-------------------------------------+
| superclass: object%                 |
+-------------------------------------+
```

An editor-wordbreak-map% objects is used with a
text% objects to specify word-breaking criteria for the
default wordbreaking function. See also set-wordbreak-map, get-wordbreak-map, find-wordbreak, and set-wordbreak-func.

A global object the-editor-wordbreak-map is created
automatically and used as the default map for all text%
objects.

A wordbreak objects implements a mapping from each character to a list
of symbols. The following symbols are legal elements of the list:

- 'caret
- 'line
- 'selection
- 'user1
- 'user2

The presence of a flag in a character’s value indicates that the
character does not break a word when searching for breaks using the
corresponding reason. For example, if 'caret is present,
then the character is a non-breaking character for caret-movement
words. (Each stream of non-breaking characters is a single word.)

```
+---------------------------------------------------------------+
| [constructor]                                                 |
|                                                               |
| (new editor-wordbreak-map%) → (is-a?/c editor-wordbreak-map%) |
+---------------------------------------------------------------+
```

All ASCII alpha-numeric characters are initialized with
'(caretlineselection). All other ASCII non-whitespace
characters except - are initialized with
'(line). All ASCII whitespace characters and - are
initialized with null.

```
+---------------------------------------------------------+
| [method]                                                |
|                                                         |
| (send an-editor-wordbreak-map get-map char)             |
| → (listof (or/c 'caret 'line 'selection 'user1 'user2)) |
| char: char?                                            |
+---------------------------------------------------------+
```

Gets the mapping value for char. See
editor-wordbreak-map% for more information.

```
+---------------------------------------------------------------+
| [method]                                                      |
|                                                               |
| (send an-editor-wordbreak-map set-map                         |
| char: char?                                                  |
| value: (listof (or/c 'caret 'line 'selection 'user1 'user2)) |
+---------------------------------------------------------------+
```

Sets the mapping value for char to value. See
editor-wordbreak-map% for more information.
