<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/separator-menu-item_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/separator-menu-item_.html -->
<!-- Canonical English source for Japanese translation -->

```
+------------------------------------+--------------+
| classseparator-menu-item%: class? |              |
+------------------------------------+--------------+
| superclass: object%                |              |
| extends:                           | menu-item<%> |
+------------------------------------+--------------+
```

A separator is an unselectable line in a menu. Its parent must be a
menu% or popup-menu%.

```
+-------------------------------------------------------+
| [constructor]                                         |
|                                                       |
| (new separator-menu-item% [parent parent])            |
| → (is-a?/c separator-menu-item%)                      |
| parent: (or/c (is-a?/c menu%) (is-a?/c popup-menu%)) |
+-------------------------------------------------------+
```

Creates a new separator in the menu.
