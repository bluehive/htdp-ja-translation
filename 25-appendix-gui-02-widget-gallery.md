## 2 ウィジェット・ギャラリー

本節では、Racket グラフィカルユーザインタフェース・ツールキットで利用できる主なウィジェットを示します。各画像は、該当するウィジェットのドキュメントへのリンクになっています。

```
  +----------+
  |  Button  |
  +----------+
```
[image: button.png]

```racket
(define button (new button%
                    (parent panel)
                    (label "Button")))
```

```
  [x] Check Box
```
[image: check-box.png]

```racket
(define check-box (new check-box%
                       (parent panel)
                       (label "Check Box")
                       (value #t)))
```

```
  Choice [Item 0 v]
```
[image: choice.png]

```racket
(define choice (new choice%
                    (label "Choice")
                    (parent panel)
                    (choices (list "Item 0"))))
```

```
  Combo [Field    v]
```
[image: combo-field.png]

```racket
(define combo-field (new combo-field%
                         (label "Combo")
                         (parent panel)
                         (choices (list "Field"))
                         (init-value "Field")))
```

```
  +------------------+
  | Editor Canvas    |
  |                  |
  +------------------+
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

```
  Gauge [#######----] 42%
```
[image: gauge.png]

```racket
(define gauge (new gauge%
                   (label "Gauge")
                   (parent panel)
                   (range 100)))
(send gauge set-value 42)
```

```
  +-- Group Box Panel --+
  |                     |
  +---------------------+
```
[image: group-box-panel.png]

```racket
(define group-box-panel (new group-box-panel%
                             (parent panel)
                             (label "Group Box Panel")))
```

```
  List Box
  +----------------+
  | First Column   |
  | Item 0         |
  | Item 1         |
  | Item 2         |
  +----------------+
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

```
  +------+------+------+
  | File | Edit | Help |
  +------+------+------+
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

```
  Message
```
[image: message.png]

```racket
(define message (new message%
                     (parent panel)
                     (label "Message")))
```

```
  +--------+
  | Panel  |
  +--------+
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

```
  Radio Box
  (*) Button 0
  ( ) Button 1
  ( ) Button 2
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

```
  Slider [--|#######] 42
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

```
  +------+------+------+
  | Tab 0| Tab 1| Tab 2|
  +------+------+------+
  |                    |
  +--------------------+
```
[image: tab-panel.png]

```racket
(define tab-panel (new tab-panel%
                       (parent panel)
                       (choices (list "Tab 0"
                                      "Tab 1"
                                      "Tab 2"))))
```

```
  Text [ Field          ]
```
[image: text-field.png]

```racket
(define text-field (new text-field%
                        (label "Text")
                        (parent panel)
                        (init-value "Field")))
```
