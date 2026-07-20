<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/Windowing_Classes.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/Windowing_Classes.html -->
<!-- Canonical English source for Japanese translation -->

## 3 Windowing Classes

Windows and controls:

```
+--------------------------------------------------+
| area<%>                                          |
+--------------------------------------------------+
| `_____________________|_______________`          |
| `|` `|` `|`                                      |
| subarea<%> window<%> area-container<%>           |
| <<<`____|____` `_____|__________` `__|___` `___… |
| `|` `|` `|` `|` `|` `|`                          |
| subwindow<%> `|` `|` `|` `|`                     |
| <<<`______________|___________` `|` `|` `|` `|`… |
| `|` `|` `|` `|` pane% `|`                        |
| control<%> `|` `|` `|` `|`- horizontal-pane% `|` |
| `|`- message% `|` `|` `|` `|`- vertical-pane% `… |
| `|`- button% `|` `|` `|` `|`                     |
| `|`- check-box% `|` area-container-window<%> `|` |
| `|`- slider% `|` `|` `|`                         |
| `|`- gauge% `|` `|` `__________________|`        |
| `|`- text-field% `|` `|` `|`                     |
| `|`- combo-field% `|` `|`-------- panel%         |
| `|`- radio-box% `|` `|` `|`- horizontal-panel%   |
| `|`- list-control<%> `|` `|` `|`- vertical-pane… |
| `|`- choice% `|` `|` `|`- tab-panel%             |
| `|`- list-box% `|` `|` `|`- group-box-panel%     |
| `|` `|`                                          |
| `|` `|`- top-level-window<%>                     |
| `|` `|`- frame%                                  |
| canvas<%> `|`- dialog%                           |
| `|`- canvas%                                     |
| `|`- editor-canvas%                              |
+--------------------------------------------------+
```

Menus:

```
+-----------------------------------------------+
| menu-item<%> menu-item-container<%>           |
+-----------------------------------------------+
| `|` `|`                                       |
| `|`- separator-menu-item% `_____|___`         |
| `|`- labelled-menu-item<%> `|` `|`- menu-bar% |
| `_________|_________` `|` `|`- popup-menu%    |
| `|` `|` `|`                                   |
| `|` menu%                                     |
| `|`                                           |
| `|`- selectable-menu-item<%>                  |
| `|`- menu-item%                               |
| `|`- checkable-menu-item%                     |
+-----------------------------------------------+
```

Events and other:

```
+---------------------------------------+
| event% timer%                         |
+---------------------------------------+
| `|`- key-event% cursor%               |
| `|`- mouse-event%                     |
| `|`- scroll-event% clipboard<%>       |
| `|`- control-event% clipboard-client% |
+---------------------------------------+
```

Alphabetical:

### Contents

- 3.1 area<%>
- 3.2 area-container<%>
- 3.3 area-container-window<%>
- 3.4 button%
- 3.5 canvas<%>
- 3.6 canvas%
- 3.7 check-box%
- 3.8 checkable-menu-item%
- 3.9 choice%
- 3.10 clipboard-client%
- 3.11 clipboard<%>
- 3.12 combo-field%
- 3.13 control<%>
- 3.14 column-control-event%
- 3.15 control-event%
- 3.16 cursor%
- 3.17 dialog%
- 3.18 event%
- 3.19 frame%
- 3.20 gauge%
- 3.21 group-box-panel%
- 3.22 grow-box-spacer-pane%
- 3.23 horizontal-pane%
- 3.24 horizontal-panel%
- 3.25 key-event%
- 3.26 labelled-menu-item<%>
- 3.27 list-box%
- 3.28 list-control<%>
- 3.29 menu%
- 3.30 menu-bar%
- 3.31 menu-item<%>
- 3.32 menu-item%
- 3.33 menu-item-container<%>
- 3.34 message%
- 3.35 mouse-event%
- 3.36 pane%
- 3.37 panel%
- 3.38 popup-menu%
- 3.39 printer-dc%
- 3.40 radio-box%
- 3.41 selectable-menu-item<%>
- 3.42 separator-menu-item%
- 3.43 scroll-event%
- 3.44 slider%
- 3.45 subarea<%>
- 3.46 subwindow<%>
- 3.47 tab-panel%
- 3.48 text-field%
- 3.49 timer%
- 3.50 top-level-window<%>
- 3.51 vertical-pane%
- 3.52 vertical-panel%
- 3.53 window<%>
