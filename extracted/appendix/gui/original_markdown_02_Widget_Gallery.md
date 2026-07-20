<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/Widget_Gallery.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/Widget_Gallery.html -->
<!-- Canonical English source for Japanese translation -->

## 2 Widget Gallery

This section shows the main widgets available in the Racket Graphical User
Interface Toolkit. Each image is a link to the documentation of the relevant
widget.

[image: button.png]

```racket
(define button (new button%
                    (parent panel)
                    (label "Button")))
```

[image: check-box.png]

```racket
(define check-box (new check-box%
                       (parent panel)
                       (label "Check Box")
                       (value #t)))
```

[image: choice.png]

```racket
(define choice (new choice%
                    (label "Choice")
                    (parent panel)
                    (choices (list "Item 0"))))
```

[image: combo-field.png]

```racket
(define combo-field (new combo-field%
                         (label "Combo")
                         (parent panel)
                         (choices (list "Field"))
                         (init-value "Field")))
```

[image: editor-canvas.png]

```racket
(define editor-canvas (new editor-canvas%
                           (parent panel)
                           (label "Editor Canvas")))
(define text (new text%))
(send text insert "Editor Canvas")
(send editor-canvas set-editor text)
```

[image: gauge.png]

```racket
(define gauge (new gauge%
                   (label "Gauge")
                   (parent panel)
                   (range 100)))
(send gauge set-value 42)
```

[image: group-box-panel.png]

```racket
(define group-box-panel (new group-box-panel%
                             (parent panel)
                             (label "Group Box Panel")))
```

[image: list-box.png]

```racket
(define list-box (new list-box%
                      (label "List Box")
                      (parent (new horizontal-panel%
                                   (parent panel)
                                   (style (list 'border))))
                      (choices (list "Item 0"
                                     "Item 1"
                                     "Item 2"))
                      (style (list 'single
                                   'column-headers))
                      (columns (list "First Column"))))
```

[image: menu-bar.png]

```racket
(define menu-bar (new menu-bar%
                      (parent frame)))
(new menu%
     (label "&File")
     (parent menu-bar))
(new menu%
     (label "&Edit")
     (parent menu-bar))
(new menu%
     (label "&Help")
     (parent menu-bar))
```

[image: message.png]

```racket
(define message (new message%
                     (parent panel)
                     (label "Message")))
```

[image: panel.png]

```racket
(define a-panel (new panel%
                     (parent panel)
                     (style (list 'border))))
(new message%
     (parent a-panel)
     (label "Panel"))
```

[image: radio-box.png]

```racket
(define radio-box (new radio-box%
                       (label "Radio Box")
                       (parent panel)
                       (choices (list "Button 0"
                                      "Button 1"
                                      "Button 2"))))
```

[image: slider.png]

```racket
(define slider (new slider%
                    (label "Slider")
                    (parent panel)
                    (min-value 0)
                    (max-value 100)
                    (init-value 42)))
```

[image: tab-panel.png]

```racket
(define tab-panel (new tab-panel%
                       (parent panel)
                       (choices (list "Tab 0"
                                      "Tab 1"
                                      "Tab 2"))))
```

[image: text-field.png]

```racket
(define text-field (new text-field%
                        (label "Text")
                        (parent panel)
                        (init-value "Field")))
```
