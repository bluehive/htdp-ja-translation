<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/Windowing_Functions.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/Windowing_Functions.html -->
<!-- Canonical English source for Japanese translation -->

## 4 Windowing Functions

### Contents

- 4.1 Dialogs
- 4.2 Eventspaces
- 4.3 System Menus
- 4.4 Global Graphics
- 4.5 Fonts
- 4.6 Miscellaneous

### 4.1 Dialogs

These functions get input from the user and/or display
messages.

```
+------------------------------------------------------------------+
| [procedure]                                                      |
|                                                                  |
| (get-file                                                        |
| message: (or/c label-string? #f) = #f                           |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f       |
| directory: (or/c path-string? #f) = #f                          |
| filename: (or/c path-string? #f) = #f                           |
| extension: (or/c string? #f) = #f                               |
| style: (listof (or/c 'packages 'enter-packages 'common)) = null |
| filters: (listof (list/c string? string?)) = '(("Any" "*.*"))   |
| dialog-mixin: (make-mixin-contract path-dialog%) = (λ (x) x)    |
+------------------------------------------------------------------+
```

Obtains a file pathname from the user via the platform-specific
standard (modal) dialog, using parent as the parent window if
it is specified, and using message as a message at the top of
the dialog if it is not #f.

The result is #f if the user cancels the dialog, the selected
pathname otherwise. The returned pathname may or may not exist,
although the style of the dialog is directed towards selecting
existing files.

If directory is not #f, it is used as the starting
directory for the file selector (otherwise the starting directory is
chosen automatically in a platform-specific manner, usually based on
the current directory and the user’s interactions in previous calls
to get-file, put-file, etc.). If
filename is not #f, it is used as the default filename
when appropriate, and it should not contain a directory path
prefix.

Under Windows, if extension is not #f, the returned path
will use the extension if the user does not supply one; the
extension string should not contain a period. The extension is
ignored on other platforms.

The style list can contain 'common, a
platform-independent version of the dialog is used instead of a
native dialog. On Mac OS, if the style list
contains 'packages, a user is allowed to select a package
directory, which is a directory with a special suffix (e.g.,
“.app”) that the Finder normally displays like a file. If the list
contains 'enter-packages, a user is allowed to select a file
within a package directory. If the list contains both
'packages and 'enter-packages, the former is ignored.

On Windows and Unix, filters determines a set of filters from
which the user can choose in the dialog. Each element of the
filters list contains two strings: a description of the filter
as seen by the user, and a filter pattern matched against file names.
Pattern strings can be a simple “glob” pattern, or a number of glob
patterns separated by a; character. These patterns are not
regular expressions and can only be used with a * wildcard
character. For example, "*.jp*g;*.png".
On Unix, a "*.*" pattern is implicitly replaced with "*".
On Mac OS, suffix names are extracted from all globs that match a
fixed suffix (e.g., two suffixes of "foo" and "bar"
are extracted from a "*.foo;*.bar;*.baz*" pattern), and files
that have any of these suffixes in any filter are selectable; a
"*.*" glob makes all files available for selection.

The dialog-mixin is applied to path-dialog% before
creating an instance of the class for this dialog.

See also path-dialog% for a richer interface.

```
+------------------------------------------------------------------+
| [procedure]                                                      |
|                                                                  |
| (get-file-list                                                   |
| → (or/c (listof path?) #f)                                       |
| message: (or/c label-string? #f) = #f                           |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f       |
| directory: (or/c path-string? #f) = #f                          |
| filename: (or/c path-string? #f) = #f                           |
| extension: (or/c string? #f) = #f                               |
| style: (listof (or/c 'packages 'enter-packages 'common)) = null |
| filters: (listof (list/c string? string?)) = '(("Any" "*.*"))   |
| dialog-mixin: (make-mixin-contract path-dialog%) = (λ (x) x)    |
+------------------------------------------------------------------+
```

Like
get-file, except that the user can select multiple files, and the
result is either a list of file paths or #f.

```
+------------------------------------------------------------------+
| [procedure]                                                      |
|                                                                  |
| (put-file                                                        |
| message: (or/c label-string? #f) = #f                           |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f       |
| directory: (or/c path-string? #f) = #f                          |
| filename: (or/c path-string? #f) = #f                           |
| extension: (or/c string? #f) = #f                               |
| style: (listof (or/c 'packages 'enter-packages 'common)) = null |
| filters: (listof (list/c string? string?)) = '(("Any" "*.*"))   |
| dialog-mixin: (make-mixin-contract path-dialog%) = (λ (x) x)    |
+------------------------------------------------------------------+
```

Obtains a file pathname from the user via the platform-specific
standard (modal) dialog, using parent as the parent window if
it is specified, and using message as a message at the top of
the dialog if it is not #f.

The result is #f if the user cancels the dialog, the selected
pathname otherwise. The returned pathname may or may not exist,
although the style of the dialog is directed towards creating a new
file.

If directory is not #f, it is used as the starting
directory for the file selector (otherwise the starting directory is
chosen automatically in a platform-specific manner, usually based on
the current directory and the user’s interactions in previous calls
to get-file, put-file, etc.). If
filename is not #f, it is used as the default filename
when appropriate, and it should not contain a directory path
prefix.

On Windows, if extension is not #f, the returned path
will get a default extension if the user does not supply one. The extension is derived
from the user’s filters choice if the corresponding pattern is
of the form (string-append"*."an-extension), and the first such
pattern is used if the choice has multiple patterns. If the user’s choice has the pattern
"*.*" and extension is the empty string, then no default extension is added. Finally, if
extension is any string other than the empty string,
extension is used as the default extension when the user’s
filters choice has the pattern "*.*". Meanwhile, the
filters argument has the same format and auxiliary role as for
get-file. In particular, if the only pattern in filters
is (string-append"*."extension), then the result pathname is guaranteed
to have an extension mapping extension.

On Mac OS 10.5 and later, if extension is not
#f or "", the returned path will get a default extension if the
user does not supply one. If filters contains as
"*.*" pattern, then the user can supply any extension that
is recognized by the system; otherwise, the extension on the returned
path will be either extension or other-extension
for any (string-append"*."other-extension) pattern in
filters. In particular, if the only pattern in
filters is empty or contains only (string-append"*."extension), then the result pathname is guaranteed to have an
extension mapping extension.

On Mac OS versions before 10.5, the returned path will get a
default extension only if extension is not #f,
extension is not "", and
filters contains only (string-append"*."extension).

On Unix, extension is ignored, and filters is used
to filter the visible list of files as in get-file.

The style list is treated as for get-file.

The dialog-mixin is applied to path-dialog% before
creating an instance of the class for this dialog.

See also path-dialog% for a richer interface.

```
+---------------------------------------------------------------+
| [procedure]                                                   |
|                                                               |
| (get-directory                                                |
| message: (or/c label-string? #f) = #f                        |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f    |
| directory: (or/c path-string? #f) = #f                       |
| style: (listof (or/c 'enter-packages 'common)) = null        |
| dialog-mixin: (make-mixin-contract path-dialog%) = (λ (x) x) |
+---------------------------------------------------------------+
```

Obtains a directory pathname from the user via the platform-specific
standard (modal) dialog, using parent as the parent window if
it is specified.

If directory is not #f, it is used on some platforms as
the starting directory for the directory selector (otherwise the
starting directory is chosen automatically in a platform-specific
manner, usually based on the current directory and the user’s
interactions in previous calls to get-file,
put-file, etc.).

The style argument is treated as for
get-file, except that only 'common or 'enter-packages can be
specified. The latter
matters only on Mac OS, where 'enter-packages
enables the user to select package directory or a directory within a
package. A package is a directory with a special suffix (e.g.,
“.app”) that the Finder normally displays like a file.

The dialog-mixin is applied to path-dialog% before
creating an instance of the class for this dialog.

See also path-dialog% for a richer interface.

```
+--------------------------------------------------------------------------------+
| [procedure]                                                                    |
|                                                                                |
| (message-box                                                                   |
| → (or/c 'ok 'cancel 'yes 'no)                                                  |
| title: label-string?                                                          |
| message: string?                                                              |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f                     |
| style: (listof (or/c 'ok 'ok-cancel 'yes-no 'caution 'stop 'no-icon)) = '(ok) |
| (listof (or/c 'ok 'ok-cancel 'yes-no                                           |
| 'caution 'stop 'no-icon))                                                      |
| dialog-mixin: (make-mixin-contract dialog%) = values                          |
|                                                                                |
| ```racket                                                                      |
| (listof (or/c 'ok 'ok-cancel 'yes-no                                           |
|               'caution 'stop 'no-icon))                                        |
| ```                                                                            |
+--------------------------------------------------------------------------------+
```

See also message-box/custom.

Displays a message to the user in a (modal) dialog, using
parent as the parent window if it is specified. The dialog’s
title is title. The message string can be arbitrarily
long, and can contain explicit linefeeds or carriage returns for
breaking lines.

The style must include exactly one of the following:

- 'ok — the dialog only has an OK button
and always returns 'ok.
- 'ok-cancel — the message dialog has
Cancel and OK buttons. If the user clicks
Cancel, the result is 'cancel, otherwise the
result is 'ok.
- 'yes-no — the message dialog has Yes and
No buttons. If the user clicks Yes, the result
is 'yes, otherwise the result is 'no. Note: instead
of a Yes/No dialog, best-practice GUI design is
to use message-box/custom and give the buttons meaningful
labels, so that the user does not have to read the message text
carefully to make a selection.

In addition, style can contain 'caution to make the
dialog use a caution icon instead of the application (or generic
“info”) icon, 'stop to make the dialog use a stop icon, or
'no-icon to suppress the icon. If style contains
multiple of 'caution, 'stop, and 'no-icon,
then 'no-icon takes precedence followed by 'stop.

The class that implements the dialog provides a get-message
method that takes no arguments and returns the text of the message as
a string. (The dialog is accessible through the
get-top-level-windows function.)

The message-box function can be called in a thread other
than the handler thread of the relevant eventspace (i.e., the eventspace of
parent, or the current eventspace if parent is #f), in which case the
current thread blocks while the dialog runs on the handler thread.

The dialog-mixin argument is applied to the class that implements the dialog
before the dialog is created.

```
+-----------------------------------------------------------------------------+
| [procedure]                                                                 |
|                                                                             |
| (message-box/custom                                                         |
| → (if/c return-the-dialog? (is-a?/c dialog%) (or/c 1 2 3 close-result))     |
| (if/c return-the-dialog?                                                    |
| (is-a?/c dialog%)                                                           |
| (or/c 1 2 3 close-result))                                                  |
| title: label-string?                                                       |
| message: string?                                                           |
| button1-label: (or/c label-string? (is-a?/c bitmap%) #f)                   |
| button2-label: (or/c label-string? (is-a?/c bitmap%) #f)                   |
| button3-label: (or/c label-string? (is-a?/c bitmap%) #f)                   |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f                  |
| style: (listof (or/c 'stop 'caution 'no-icon 'number-order 'disallow-close |
| 'no-default 'default=1 'default=2 'default=3)) = '(no-default)              |
| (listof (or/c 'stop 'caution 'no-icon 'number-order                         |
| 'disallow-close 'no-default                                                 |
| 'default=1 'default=2 'default=3))                                          |
| close-result: any/c = #f                                                   |
| return-the-dialog?: any/c = #f                                             |
| dialog-mixin: (make-mixin-contract dialog%) = values                       |
|                                                                             |
| ```racket                                                                   |
| (if/c return-the-dialog?                                                    |
|       (is-a?/c dialog%)                                                     |
|       (or/c 1 2 3 close-result))                                            |
| ```                                                                         |
|                                                                             |
| ```racket                                                                   |
| (listof (or/c 'stop 'caution 'no-icon 'number-order                         |
|               'disallow-close 'no-default                                   |
|               'default=1 'default=2 'default=3))                            |
| ```                                                                         |
+-----------------------------------------------------------------------------+
```

Displays a message to the user in a (modal) dialog, using
parent as the parent window if it is specified. The dialog’s
title is title. The message string can be arbitrarily
long, and can contain explicit linefeeds or carriage returns for
breaking lines.

The dialog contains up to three buttons for the user to click. The
buttons have the labels button1-label,
button2-label, and button3-label, where #f for a
label indicates that the button should be hidden.

If the user clicks the button labelled button1-label, a 1
is returned, and so on for 2 and 3. If the user closes
the dialog some other way—which is only allowed when style
does not contain 'disallow-close—then the result is the
value of close-result. For example, the user can usually close
a dialog by typing an Escape. Often, 2 is an appropriate value
for close-result, especially when Button 2 is a Cancel
button.

If style does not include 'number-order, the order of
the buttons is platform-specific, and labels should be assigned to
the buttons based on their role:

- Button 1 is the normal action, and it is usually the default
button. For example, if the dialog has an OK button, it is
this one. On Windows, this button is leftmost; on Unix and Mac OS, it is rightmost. (See also
system-position-ok-before-cancel?.) Use this button for
dialogs that contain only one button.
- Button 2 is next to Button 1, and it often plays the role of
Cancel (even when the default action is to cancel, such as
when confirming a file replacement).
- Button 3 tends to be separated from the other two (on
Mac OS, it is left-aligned in the dialog). Use this button only
for three-button dialogs.

Despite the above guidelines, any combination of visible buttons is
allowed in the dialog.

If style includes 'number-order, then the buttons are
displayed in the dialog left-to-right with equal spacing between all
buttons, though aligned within the dialog (centered or right-aligned)
in a platform-specific manner. Use 'number-order sparingly.

The style list must contain exactly one of 'default=1,
'default=2, 'default=3, and 'no-default to
determine which button (if any) is the default. The default button is
“clicked” when the user types Return. If 'default=n
is supplied but button n has no label, then it is equivalent to
'no-default.

In addition, style can contain 'caution,
'stop, or 'no-icon to adjust the icon that appears
in the dialog, the same for message-box.

If return-the-dialog? is a true value, then the dialog
is not shown and is instead returned from message-box/custom.
The dialog responds to these three additional messages (via send):

- get-message This method takes no arguments
and returns the text of the message as
a string.
- set-message This method accepts one string argument
and changes the message of the dialog to the given argument.
- show-and-return-results This method accepts no arguments
and shows the dialog. It returns after the dialog closes, with the result that the
message-box/custom would have returned if return-the-dialog?
had been #false.

The dialog is also accessible through the get-top-level-windows function.

The message-box/custom function can be called in a thread
other than the handler thread of the relevant eventspace (i.e., the eventspace of
parent, or the current eventspace if parent is #f), in which case the
current thread blocks while the dialog runs on the handler thread.

The dialog-mixin argument is applied to the class that implements the dialog
before the dialog is created.

Changed in version 1.53 of package `gui-lib`: Added the return-the-dialog? argument
and the ability to change the dialog box’s message.

```
+-----------------------------------------------------------------------------+
| [procedure]                                                                 |
|                                                                             |
| (message+check-box                                                          |
| → (if/c return-the-dialog? (is-a?/c dialog%) (values (or/c 'ok 'cancel 'yes |
| 'no) boolean?))                                                             |
| (if/c return-the-dialog?                                                    |
| (is-a?/c dialog%)                                                           |
| (values (or/c 'ok 'cancel 'yes 'no) boolean?))                              |
| title: label-string?                                                       |
| message: string?                                                           |
| check-label: label-string?                                                 |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f                  |
| style: (listof (or/c 'ok 'ok-cancel 'yes-no 'caution 'stop 'no-icon        |
| 'checked)) = '(ok)                                                          |
| (listof (or/c 'ok 'ok-cancel 'yes-no                                        |
| 'caution 'stop 'no-icon 'checked))                                          |
| return-the-dialog?: any/c = #f                                             |
| dialog-mixin: (make-mixin-contract dialog%) = values                       |
|                                                                             |
| ```racket                                                                   |
| (if/c return-the-dialog?                                                    |
|       (is-a?/c dialog%)                                                     |
|       (values (or/c 'ok 'cancel 'yes 'no) boolean?))                        |
| ```                                                                         |
|                                                                             |
| ```racket                                                                   |
| (listof (or/c 'ok 'ok-cancel 'yes-no                                        |
|               'caution 'stop 'no-icon 'checked))                            |
| ```                                                                         |
+-----------------------------------------------------------------------------+
```

See also message+check-box/custom.

Like message-box, except that

- the dialog contains a check box whose label is check-label;
- the result is two values: the message-box result, and a
boolean indicating whether the box was checked; and
- style can contain 'checked to indicate that the check box
should be initially checked.
- If return-the-dialog? is a true value, the resulting object
also has a public set-check-label method. That method
accepts a single, label-string? argument and sets the
checkbox’s label to that string.

Changed in version 1.53 of package `gui-lib`: Added the return-the-dialog? argument and
the ability to change the dialog box’s message and check label.

```
+-----------------------------------------------------------------------------+
| [procedure]                                                                 |
|                                                                             |
| (message+check-box/custom                                                   |
| → (or/c 1 2 3 (λ (x) (eq? x close-result)))                                 |
| title: label-string?                                                       |
| message: string?                                                           |
| check-label: label-string?                                                 |
| button1-label: (or/c label-string? (is-a?/c bitmap%) #f)                   |
| button2-label: (or/c label-string? (is-a?/c bitmap%) #f)                   |
| button3-label: (or/c label-string? (is-a?/c bitmap%) #f)                   |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f                  |
| style: (listof (or/c 'stop 'caution 'no-icon 'number-order 'disallow-close |
| 'no-default 'default=1 'default=2 'default=3)) = '(no-default)              |
| (listof (or/c 'stop 'caution 'no-icon 'number-order                         |
| 'disallow-close 'no-default                                                 |
| 'default=1 'default=2 'default=3))                                          |
| close-result: any/c = #f                                                   |
| dialog-mixin: (make-mixin-contract dialog%) = values                       |
|                                                                             |
| ```racket                                                                   |
| (listof (or/c 'stop 'caution 'no-icon 'number-order                         |
|               'disallow-close 'no-default                                   |
|               'default=1 'default=2 'default=3))                            |
| ```                                                                         |
+-----------------------------------------------------------------------------+
```

Like message-box/custom, except that

- the dialog contains a check box whose label is check-label;
- the result is two values: the message-box result, and a
boolean indicating whether the box was checked; and
- style can contain 'checked to indicate that the check box
should be initially checked.

```
+------------------------------------------------------------+
| [procedure]                                                |
|                                                            |
| (get-text-from-user                                        |
| → (or/c string? #f)                                        |
| title: label-string?                                      |
| message: (or/c label-string? #f)                          |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f |
| init-val: string? = ""                                    |
| style: (listof (or/c 'password 'disallow-invalid)) = null |
| validate: (-> string? boolean?)                           |
| dialog-mixin: (make-mixin-contract dialog%) = values      |
+------------------------------------------------------------+
```

Gets a text string from the user via a modal dialog, using
parent as the parent window, if it is specified. The dialog’s
title is title. The dialog’s text field is labelled with
message and initialized to init-val (but init-val
does not determine the size of the dialog).

The result is #f if the user cancels the dialog, the
user-provided string otherwise.

If style includes 'password, the dialog’s text field
draws each character of its content using a generic symbol, instead
of the actual character.

The validate function is called each time the text field changed,
with the contents of the text field. If it returns #f, the background
of the text is colored pink. If 'disallow-invalid is included in
style, the Ok button is disabled whenever the text
background is pink.

The dialog-mixin argument is applied to the class that implements the dialog
before the dialog is created.

```
+-----------------------------------------------------------------+
| [procedure]                                                     |
|                                                                 |
| (get-choices-from-user                                          |
| → (or/c (listof exact-nonnegative-integer?) #f)                 |
| title: label-string?                                           |
| message: (or/c label-string? #f)                               |
| choices: (listof label-string?)                                |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f      |
| init-choices: (listof exact-nonnegative-integer?) = null       |
| style: (listof (or/c 'single 'multiple 'extended)) = '(single) |
+-----------------------------------------------------------------+
```

Gets a list box selection from the user via a modal dialog, using
parent as the parent window if it is specified. The dialog’s
title is title. The dialog’s list box is labelled with
message and initialized by selecting the items in
init-choices.

The style must contain exactly one of 'single,
'multiple, or 'extended. The styles have
the same meaning as for creating a list-box% object. (For
the single-selection style, only the last selection in
init-choices matters.)

The result is #f if the user cancels the dialog, the
list of selections otherwise.

```
+------------------------------------------------------------+
| [procedure]                                                |
|                                                            |
| (get-color-from-user                                       |
| message: (or/c label-string? #f) = #f                     |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f |
| init-color: (or/c (is-a?/c color%) #f) = #f               |
| style: (listof 'alpha) = null                             |
+------------------------------------------------------------+
```

Lets the user select a color though the platform-specific
(modal) dialog, using parent as the parent window if it is
specified. The message string is displayed as a prompt in the
dialog if possible. If init-color is provided, the dialog is
initialized to the given color.

The result is #f if the user cancels the dialog, the selected
color otherwise.

If style contains 'alpha, then the user is present with
a field for filling in the alpha field of the resulting color% object.
If it does not, then the alpha component of init-color is ignored,
and the result always has alpha of 1.0.

```
+------------------------------------------------------------+
| [procedure]                                                |
|                                                            |
| (get-font-from-user                                        |
| message: (or/c label-string? #f) = #f                     |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f |
| init-font: (or/c (is-a?/c font%) #f) = #f                 |
| style: null? = null                                       |
+------------------------------------------------------------+
```

Lets the user select a font though the platform-specific
(modal) dialog, using parent as the parent window if it is
specified. The message string is displayed as a prompt in the
dialog if possible. If init-font is provided, the dialog is
initialized to the given font.

The style argument is provided for future extensions. Currently, style must be the empty list.

The result is #f if the user cancels the dialog, the selected
font otherwise.

```
+------------------------------------------------------------+
| [procedure]                                                |
|                                                            |
| (get-ps-setup-from-user                                    |
| → (or/c (is-a?/c ps-setup%) #f)                            |
| message: (or/c label-string? #f) = #f                     |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f |
| init-setup: (or/c (is-a?/c ps-setup%) #f) = #f            |
| style: null? = null                                       |
+------------------------------------------------------------+
```

Lets the user select a PostScript configuration though a (modal)
dialog, using parent as the parent window if it is
specified. The message string is displayed as a prompt in the
dialog. If init-setup is provided, the dialog is initialized to
the given configuration, otherwise the current configuration from
current-ps-setup is used.

The style argument is provided for future extensions. Currently, style must be the empty list.

The result is #f if the user cancels the dialog,, a
ps-setup% object that encapsulates the selected PostScript
configuration otherwise.

```
+------------------------------------------------------------+
| [procedure]                                                |
|                                                            |
| (get-page-setup-from-user                                  |
| → (or/c (is-a?/c ps-setup%) #f)                            |
| message: (or/c label-string? #f) = #f                     |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f |
| init-setup: (or/c (is-a?/c ps-setup%) #f) = #f            |
| style: null? = null                                       |
+------------------------------------------------------------+
```

Like
get-ps-setup-from-user, but the dialog configures page layout for native printing
with printer-dc%. A dialog is shown only if
can-get-page-setup-from-user? returns #t, otherwise no dialog is shown and the result
is #f.

The parent argument is used as the parent window for a dialog if
it is specified. The message string might be displayed as a
prompt in the dialog. If init-setup is provided, the dialog is
initialized to the given configuration, otherwise the current
configuration from
current-ps-setup is used.

The style argument is provided for future extensions. Currently, style must be the empty list.

The result is #f if the user cancels the dialog, a
ps-setup% object that encapsulates the selected
configuration otherwise.

```
+--------------------------------------------+
| [procedure]                                |
|                                            |
| (can-get-page-setup-from-user?) → boolean? |
+--------------------------------------------+
```

Returns #t if the current platform supports a
page-layout dialog for use with printer-dc% printing.
Currently, all platforms support a page-layout dialog.

### 4.2 Eventspaces

```
+---------------------------------------------------------+
| [procedure]                                             |
|                                                         |
| (make-eventspace [#:suspend-to-kill? suspend-to-kill?]) |
| → eventspace?                                           |
| suspend-to-kill?: any/c = #f                           |
+---------------------------------------------------------+
```

Creates and returns a new eventspace value. The new eventspace is
created as a child of the current eventspace. The eventspace is used
by making it the current eventspace with the
current-eventspace parameter.

If suspend-to-kill? is not #f, then the eventspace’s
handler thread is created using thread/suspend-to-kill.
Otherwise, it is created using thread.

See Event Dispatching and Eventspaces for more information about eventspaces.

Changed in version 1.35 of package `gui-lib`: Added the suspend-to-kill? argument.

```
+------------------------------------+
| [parameter]                        |
|                                    |
| (current-eventspace) → eventspace? |
| (current-eventspace e) → void?     |
| e: eventspace?                    |
+------------------------------------+
```

A parameter (see Parameters) that determines the current eventspace.

See Event Dispatching and Eventspaces for more information about eventspaces.

```
+----------------------------+
| [procedure]                |
|                            |
| (eventspace? v) → boolean? |
| v: any/c                  |
+----------------------------+
```

Returns #t if v is an eventspace value or #f
otherwise.

See Event Dispatching and Eventspaces for more information about eventspaces.

```
+-----------------------------------------------------+
| [parameter]                                         |
|                                                     |
| (event-dispatch-handler) → (eventspace?. ->. any) |
| (event-dispatch-handler handler) → void?            |
| handler: (eventspace?. ->. any)                  |
+-----------------------------------------------------+
```

A parameter (see Parameters) that determines the current event
dispatch handler. The event dispatch handler is called by an
eventspace’s handler thread for every queue-based event to be
processed in the eventspace. The only argument to the handler is the
eventspace in which an event should be dispatched. The event dispatch
handler gives the programmer control over the timing of event
dispatching, but not the order in which events are dispatched within
a single eventspace.

An event dispatch handler must ultimately call the primitive event
dispatch handler. If an event dispatch handler returns without
calling the primitive handler, then the primitive handler is called
directly by the eventspace handler thread.

```
+----------------------------------------+
| [procedure]                            |
|                                        |
| (eventspace-event-evt [e]) → evt?      |
| e: eventspace? = (current-eventspace) |
+----------------------------------------+
```

Produces a synchronizable event (see sync) that is ready when
a GUI event (mouse or keyboard action, update event, timer, queued
callback, etc.) is ready for dispatch in e. That is, the
result event is ready when (yield) for the eventspace
e would dispatch a GUI event. The synchronization result is
the eventspace e itself.

```
+------------------------------+
| [procedure]                  |
|                              |
| (check-for-break) → boolean? |
+------------------------------+
```

Inspects the event queue of the current eventspace, searching for a
Shift-Ctl-C (Unix, Windows) or Cmd-. (Mac OS) key combination. Returns
#t if such an event was found (and the event is dequeued) or
#f otherwise.

```
+------------------------------------------------------+
| [procedure]                                          |
|                                                      |
| (get-top-level-windows)                              |
| → (listof (or/c (is-a?/c frame%) (is-a?/c dialog%))) |
+------------------------------------------------------+
```

Returns a list of visible top-level frames and dialogs in the current
eventspace.

```
+------------------------------------------------+
| [procedure]                                    |
|                                                |
| (get-top-level-focus-window)                   |
| → (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) |
+------------------------------------------------+
```

Returns the top level window in the current eventspace that has the
keyboard focus (or contains the window with the keyboard focus), or
#f if no window in the current eventspace has the focus.

```
+------------------------------------------------+
| [procedure]                                    |
|                                                |
| (get-top-level-edit-target-window)             |
| → (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) |
+------------------------------------------------+
```

Returns the top level window in the current eventspace that is visible
and most recently had the keyboard focus (or contains the window that
had the keyboard focus), or #f if there is no visible window
in the current eventspace.

```
+-----------------------------------+
| [procedure]                       |
|                                   |
| (special-control-key on?) → void? |
| on?: any/c                       |
| (special-control-key) → boolean?  |
+-----------------------------------+
```

For backward compatibility, only. This function was intended to enable
or disable special Control key handling (Mac OS), but it currently
has no effect.

```
+----------------------------------+
| [procedure]                      |
|                                  |
| (special-option-key on?) → void? |
| on?: any/c                      |
| (special-option-key) → boolean?  |
+----------------------------------+
```

Enables or disables special Option key handling (Mac OS). When
Option is treated as a special key, the get-key-code and get-other-altgr-key-code
results are effectively swapped when the Option key is pressed. By
default, Option is not special.

If on? is provided as #f, key events are reported
normally. This setting affects all windows and eventspaces.

If no argument is provided, the result is #t if Option is
currently treated specially, #f otherwise.

```
+----------------------------------------+
| [procedure]                            |
|                                        |
| (any-control+alt-is-altgr on?) → void? |
| on?: any/c                            |
| (any-control+alt-is-altgr) → boolean?  |
+----------------------------------------+
```

Enables or disables the treatment of any Control plus Alt as
equivalent to AltGr (Windows), as opposed to treating only a
left-hand Control plus a right-hand Alt (for keyboard configurations
that have both) as AltGr.

If on? is provided as #f, key events are reported
normally. This setting affects all windows and eventspaces.

If no argument is provided, the result is #t if Control plus Alt is
currently treated as AltGr, #f otherwise.

Added in version 1.24 of package `gui-lib`.

```
+----------------------------------------------------+
| [procedure]                                        |
|                                                    |
| (queue-callback callback [high-priority?]) → void? |
| callback: (-> any)                                |
| high-priority?: any/c = #t                        |
+----------------------------------------------------+
```

Installs a procedure to be called via the current eventspace’s event
queue. The procedure is called once in the same way and under the
same restrictions that a callback is invoked to handle a method.

A second (optional) boolean argument indicates whether the callback
has a high or low priority in the event queue. See
Event Dispatching and Eventspaces for information about the priority of events.

```
+-----------------------+
| [procedure]           |
|                       |
| (yield) → boolean?    |
| (yield v) → any/c     |
| v: (or/c 'wait evt?) |
+-----------------------+
```

Yields control to event dispatching. See
Event Dispatching and Eventspaces for details.

A handler procedure invoked by the system during a call to
yield can itself call yield, creating
an additional level of nested (but single-threaded) event handling.

See also sleep/yield.

If no argument is provided, yield dispatches an unspecified
number of events, but only if the current thread is the current
eventspace’s handler thread (otherwise, there is no effect). The
result is #t if any events may have been handled,
#f otherwise.

If v is 'wait, and yield is called
in the handler thread of an eventspace, then yield starts
processing events in that eventspace until

- no top-level windows in the eventspace are visible;
- no timers in the eventspace are running;
- no callbacks are queued in the eventspace; and
- no menu-bar% has been created for the eventspace
with 'root (i.e., creating a 'root menu bar
prevents an eventspace from ever unblocking).

When called in a non-handler thread, yield returns
immediately. In either case, the result is #t.

Evaluating (yield'wait) is thus similar to
(yield(current-eventspace)), except that it is
sensitive to whether the current thread is a handler thread, instead
of the value of the current-eventspace parameter.

If v is an event in Racket’s sense (not to be confused with
a GUI event), yield blocks on v in the same way as
sync, except that it may start a sync on v
multiple times (but it will complete a sync on v at
most one time). If the current thread is the current eventspace’s
handler thread, events are dispatched until a v sync
succeeds on an event boundary. For other threads, calling
yield with a Racket event is equivalent to calling
sync. In either case, the result is the same that of
sync; however, if a wrapper procedure is associated with
v via handle-evt, it is not called in tail position
with respect to the yield.

Always use (yieldv) instead of a busy-wait loop.

```
+----------------------------------------+
| [procedure]                            |
|                                        |
| (sleep/yield secs) → void?             |
| secs: (and/c real? (not/c negative?)) |
+----------------------------------------+
```

Blocks for at least the specified number of seconds, handling events
meanwhile if the current thread is the current eventspace’s handler
thread (otherwise, sleep/yield is equivalent to
sleep).

```
+-------------------------------------+
| [procedure]                         |
|                                     |
| (eventspace-shutdown? e) → boolean? |
| e: eventspace?                     |
+-------------------------------------+
```

Returns #t if the given eventspace has been shut down by its
custodian, #f otherwise. Attempting to create a new window,
timer, or explicitly queued event in a shut-down eventspace raises
the exn:fail exception.

Attempting to use certain methods of windows and timers in a shut-down
eventspace also raises the exn:fail exception, but the
get-top-level-window in area<%> and
get-eventspace in top-level-window<%> methods work even after the area’s eventspace is shut down.

```
+---------------------------------------------------+
| [procedure]                                       |
|                                                   |
| (eventspace-handler-thread e) → (or/c thread? #f) |
| e: eventspace?                                   |
+---------------------------------------------------+
```

Returns the handler thread of the given eventspace. If the handler
thread has terminated (e.g., because the eventspace was shut down), the
result is #f.

### 4.3 System Menus

```
+-----------------------------------------------------+
| [procedure]                                         |
|                                                     |
| (current-eventspace-has-standard-menus?) → boolean? |
+-----------------------------------------------------+
```

Returns #t for Mac OS when the current eventspace is the
initial one, since that eventspace is the target for the standard
application menus. For any other system or eventspace, the result is
#f.

This procedure is intended for use in deciding whether to include a
Quit, About, and Preferences menu
item in a frame’s menu. On Mac OS, the application
Quit menu triggers a call to a frame’s
on-exit method, the About menu item is controlled by
application-about-handler, and the
Preferences menu item is controlled by
application-preferences-handler.

```
+------------------------------------------------+
| [procedure]                                    |
|                                                |
| (current-eventspace-has-menu-root?) → boolean? |
+------------------------------------------------+
```

Returns #t for Mac OS when the current eventspace is the
initial one, since that eventspace can supply a menu bar to be active
when no frame is visible. For any other system or eventspace, the
result is #f.

This procedure is intended for use in deciding whether to create a
menu-bar% instance with 'root as its parent.

```
+---------------------------------------------------+
| [procedure]                                       |
|                                                   |
| (application-about-handler) → (-> any)            |
| (application-about-handler handler-thunk) → void? |
| handler-thunk: (-> any)                          |
+---------------------------------------------------+
```

When the current eventspace is the initial eventspace, this
procedure retrieves or installs a thunk that is called when the
user selects the application About menu item on Mac OS. The thunk is always called in the initial eventspace’s
handler thread (as a callback).

The default handler displays a generic Racket dialog.

If the current eventspace is not the initial eventspace, this
procedure returns void (when called with zero arguments)
or has no effect (when called with a handler).

```
+-------------------------------------------------+
| [procedure]                                     |
|                                                 |
| (application-file-handler) → (path?. ->. any) |
| (application-file-handler handler-proc) → void? |
| handler-proc: (path?. ->. any)               |
+-------------------------------------------------+
```

When the current eventspace is the initial eventspace, this procedure
retrieves or installs a procedure that is called on Mac OS
and Windows when the application is running and user double-clicks an
application-handled file or drags a file onto the application’s
icon. The procedure is always called in the initial eventspace’s
handler thread (as a callback), and the argument is a filename.

The default handler queues a callback to the
on-drop-file method of the most-recently activated frame in the main eventspace (see
get-top-level-edit-target-window), if any such frame exists and if
drag-and-drop is enabled for that frame. Otherwise, it saves
the filename and re-queues the handler event when the application
file handler is later changed or when a frame becomes active.

On Windows, when the application is not running and a user double-clicks an
application-handled file or drags a file onto the application’s icon,
the filename is provided as a command-line argument to the
application.

On Mac OS, if an application is started *without* files, then
the application-start-empty-handler procedure is called.

If the current eventspace is not the initial eventspace, this
procedure returns void (when called with zero arguments)
or has no effect (when called with a handler).

```
+---------------------------------------------------------+
| [procedure]                                             |
|                                                         |
| (application-preferences-handler) → (or/c (-> any) #f)  |
| (application-preferences-handler handler-thunk) → void? |
| handler-thunk: (or/c (-> any) #f)                      |
+---------------------------------------------------------+
```

When the current eventspace is the initial eventspace, this procedure
retrieves or installs a thunk that is called when the user selects
the application Preferences menu item on Mac OS. The
thunk is always called in the initial eventspace’s handler thread (as
a callback). If the handler is set to #f, the
Preferences item is disabled.

The default handler is #f.

If the current eventspace is not the initial eventspace, this
procedure returns void (when called with zero arguments)
or has no effect (when called with a handler).

```
+--------------------------------------------------+
| [procedure]                                      |
|                                                  |
| (application-quit-handler) → (-> any)            |
| (application-quit-handler handler-thunk) → void? |
| handler-thunk: (-> any)                         |
+--------------------------------------------------+
```

When the current eventspace is the initial eventspace, this procedure
retrieves or installs a thunk that is called when the user requests
that the application quit (e.g., through the Quit menu
item on Mac OS, or when shutting down the machine in Windows). The
thunk is always called in the initial eventspace’s handler thread (as
a callback). If the result of the thunk is #f, then the
operating system is explicitly notified that the application does not
intend to quit (on Windows).

The default handler queues a call to the
can-exit? method of the most
recently active frame in the initial eventspace (and then calls the
frame’s on-exit method if the
result is true). The result is #t if the eventspace is
left with no open frames after
on-exit returns, #f
otherwise.

If the current eventspace is not the initial eventspace, this
procedure returns void (when called with zero arguments)
or has no effect (when called with a handler).

```
+---------------------------------------------------------+
| [procedure]                                             |
|                                                         |
| (application-start-empty-handler) → (-> any)            |
| (application-start-empty-handler handler-thunk) → void? |
| handler-thunk: (-> any)                                |
+---------------------------------------------------------+
```

When the current eventspace is the initial eventspace, this procedure
retrieves or installs a thunk that is called when the user starts
the application on Mac OS without supplying any initial files (e.g.,
by double-clicking the application icon instead of double-clicking
files that are handled by the application).

The default handler re-queues the handler event when the application
start-empty handler is later changed. As a result, if an application
sets both application-start-empty-handler and
application-file-handler, then one or the other is
eventually called.

If the current eventspace is not the initial eventspace, this
procedure returns void (when called with zero arguments)
or has no effect (when called with a handler).

```
+-------------------------------------------------------+
| [procedure]                                           |
|                                                       |
| (application-dark-mode-handler) → (-> any)            |
| (application-dark-mode-handler handler-thunk) → void? |
| handler-thunk: (-> any)                              |
+-------------------------------------------------------+
```

When the current eventspace is the initial
eventspace this procedure retrieves or installs a thunk that
is called under Mac OS when the OS switches to or from dark mode.
See also white-on-black-panel-scheme?.

The default handler does nothing.

If the current eventspace is not the initial eventspace,
this procedure returns void (when called with zero
arguments) or has no effect (when called with a handler).

Added in version 1.68 of package `gui-lib`.

### 4.4 Global Graphics

```
+-------------------------+
| [procedure]             |
|                         |
| (flush-display) → void? |
+-------------------------+
```

Flushes canvas offscreen drawing and other updates onto the
screen.

Normally, drawing is automatically flushed to the screen. Use
flush-display sparingly to force updates to the screen when
other actions depend on updating the display.

```
+-------------------------------------------------+
| [procedure]                                     |
|                                                 |
| (get-display-backing-scale [#:monitor monitor]) |
| → (or/c (>/c 0.0) #f)                           |
| monitor: exact-nonnegative-integer? = 0        |
+-------------------------------------------------+
```

Returns the number of pixels that correspond to one drawing unit on a
monitor. The result is normally 1.0, but it is 2.0
on Mac OS in Retina display mode, and on Windows or Unix it can be a value
such as 1.25, 1.5, or 2.0 when the operating-system
scale for text is changed. See also Screen Resolution and Text Scaling.

On Mac OS or Unix, the result can change at any time. See also
display-changed in top-level-window<%>.

If monitor is not less than the current number of available
monitors (which can change at any time), the is #f. See also
display-changed in top-level-window<%>.

Changed in version 1.2 of package `gui-lib`: Added backing-scale support on Windows.

```
+-----------------------------------------------+
| [procedure]                                   |
|                                               |
| (get-display-count) → exact-positive-integer? |
+-----------------------------------------------+
```

Returns the number of monitors currently active.

On Windows and Mac OS, the result can change at any time.
See also display-changed in top-level-window<%>.

```
+--------------------------------------------------+
| [procedure]                                      |
|                                                  |
| (get-display-depth) → exact-nonnegative-integer? |
+--------------------------------------------------+
```

Returns the depth of the main display (a value of 1 denotes a monochrome display).

```
+-------------------------------------------------------------------------------+
| [procedure]                                                                   |
|                                                                               |
| (get-display-left-top-inset                                                   |
| → (if (= monitor 0) exact-nonnegative-integer? (or/c                          |
| exact-nonnegative-integer? #f))(if (= monitor 0) exact-nonnegative-integer?   |
| (or/c exact-nonnegative-integer? #f))                                         |
| (if (= monitor 0) exact-nonnegative-integer? (or/c exact-nonnegative-integer? |
| #f))                                                                          |
| (if (= monitor 0)                                                             |
| exact-nonnegative-integer?                                                    |
| (or/c exact-nonnegative-integer? #f))                                         |
| (if (= monitor 0) exact-nonnegative-integer? (or/c exact-nonnegative-integer? |
| #f))                                                                          |
| (if (= monitor 0)                                                             |
| exact-nonnegative-integer?                                                    |
| (or/c exact-nonnegative-integer? #f))                                         |
| avoid-bars?: any/c = #f                                                      |
| monitor: exact-nonnegative-integer? = 0                                      |
|                                                                               |
| ```racket                                                                     |
| (if (= monitor 0)                                                             |
|     exact-nonnegative-integer?                                                |
|     (or/c exact-nonnegative-integer? #f))                                     |
| ```                                                                           |
|                                                                               |
| ```racket                                                                     |
| (if (= monitor 0)                                                             |
|     exact-nonnegative-integer?                                                |
|     (or/c exact-nonnegative-integer? #f))                                     |
| ```                                                                           |
+-------------------------------------------------------------------------------+
```

When the optional argument is #f (the default), this function
returns the offset of monitor’s origin from the
top-left of the physical monitor. For monitor 0, on Unix and Windows, the result is
always 0 and 0; on Mac OS, the result is
0 and the height of the menu bar. To position a frame
at a given monitor’s top-left corner, use the negated results from
get-display-left-top-inset as the frame’s position.

When the optional avoid-bars? argument is true, for monitor
0, get-display-left-top-inset function returns the
amount space at the left and top of the monitor that is occupied by
the task bar (Windows) or menu bar and dock (Mac OS). On Unix, for
monitor 0, the result is always 0 and 0.
For monitors other than 0, avoid-bars? has no effect.

If monitor is not less than the current number of available
monitors (which can change at any time), the results are #f
and #f. See also display-changed in top-level-window<%>.

See also Screen Resolution and Text Scaling.

```
+-------------------------------------------------------------------------------+
| [procedure]                                                                   |
|                                                                               |
| (get-display-size                                                             |
| → (if (= monitor 0) exact-nonnegative-integer? (or/c                          |
| exact-nonnegative-integer? #f))(if (= monitor 0) exact-nonnegative-integer?   |
| (or/c exact-nonnegative-integer? #f))                                         |
| (if (= monitor 0) exact-nonnegative-integer? (or/c exact-nonnegative-integer? |
| #f))                                                                          |
| (if (= monitor 0)                                                             |
| exact-nonnegative-integer?                                                    |
| (or/c exact-nonnegative-integer? #f))                                         |
| (if (= monitor 0) exact-nonnegative-integer? (or/c exact-nonnegative-integer? |
| #f))                                                                          |
| (if (= monitor 0)                                                             |
| exact-nonnegative-integer?                                                    |
| (or/c exact-nonnegative-integer? #f))                                         |
| full-screen?: any/c = #f                                                     |
| monitor: exact-nonnegative-integer? = 0                                      |
|                                                                               |
| ```racket                                                                     |
| (if (= monitor 0)                                                             |
|     exact-nonnegative-integer?                                                |
|     (or/c exact-nonnegative-integer? #f))                                     |
| ```                                                                           |
|                                                                               |
| ```racket                                                                     |
| (if (= monitor 0)                                                             |
|     exact-nonnegative-integer?                                                |
|     (or/c exact-nonnegative-integer? #f))                                     |
| ```                                                                           |
+-------------------------------------------------------------------------------+
```

Gets the physical size of the specified monitor in
pixels. On Windows, this size does not include the task bar by
default. On Mac OS, this size does not include the menu bar or
dock area by default.

On Windows and Mac OS, if the optional argument is true and monitor is 0, then
the task bar, menu bar, and dock area are included in the result.

If monitor is not less than the current number of available
monitors (which can change at any time), the results are #f
and #f. See also display-changed in top-level-window<%>.

See also Screen Resolution and Text Scaling.

```
+--------------------------------+
| [procedure]                    |
|                                |
| (is-color-display?) → boolean? |
+--------------------------------+
```

Returns #t if the main display has color, #f
otherwise.

### 4.5 Fonts

```
+-------------------------------------+
| [value]                             |
|                                     |
| menu-control-font: (is-a?/c font%) |
+-------------------------------------+
```

This font is the default for popup-menu% objects.

On Mac OS, this font is slightly larger than
normal-control-font. On Windows and Unix, it is the same
size as normal-control-font.

```
+---------------------------------------+
| [value]                               |
|                                       |
| normal-control-font: (is-a?/c font%) |
+---------------------------------------+
```

This font is the default for most controls, except
list-box% and group-box-panel% objects.

```
+--------------------------------------+
| [value]                              |
|                                      |
| small-control-font: (is-a?/c font%) |
+--------------------------------------+
```

This font is the default for group-box-panel% objects, and it is
a suitable for controls in a floating window and other contexts that
need smaller controls.

On Windows, this font is the same size as
normal-control-font, since the Windows control font is
already relatively small. On Unix and Mac OS, this font is slightly
smaller than normal-control-font.

```
+-------------------------------------+
| [value]                             |
|                                     |
| tiny-control-font: (is-a?/c font%) |
+-------------------------------------+
```

This font is for tiny controls, and it is smaller than
small-control-font on all platforms.

```
+-------------------------------------+
| [value]                             |
|                                     |
| view-control-font: (is-a?/c font%) |
+-------------------------------------+
```

This font is the default for list-box% objects (but not
list box labels, which use normal-control-font).

On Mac OS, this font is slightly smaller than
normal-control-font, and slightly larger than
small-control-font. On Windows and Unix, it is the same size
as normal-control-font.

### 4.6 Miscellaneous

```
+-----------------------------+
| [procedure]                 |
|                             |
| (begin-busy-cursor) → void? |
+-----------------------------+
```

Changes the cursor to a watch cursor for all windows in the current eventspace.
Use end-busy-cursor to revert the cursor back to its previous
state. Calls to begin-busy-cursor and end-busy-cursor can be
nested arbitrarily.

The cursor installed by begin-busy-cursor overrides any
window-specific cursors installed with set-cursor.

See also is-busy?.

```
+----------------------+
| [procedure]          |
|                      |
| (bell) → void?       |
+----------------------+
```

Rings the system bell.

```
+-----------------------------------+
| [procedure]                       |
|                                   |
| (dimension-integer? v) → boolean? |
| v: any/c                         |
+-----------------------------------+
```

Equivalent to (integer-in01000000).

Beware that certain kinds of windows behave badly when larger than
32,000 or so in either dimension on some platforms. Redraw of the
window may be disabled or clipped, for example.

```
+---------------------------+
| [procedure]               |
|                           |
| (end-busy-cursor) → void? |
+---------------------------+
```

See begin-busy-cursor.

```
+-----------------------------------------------------------------------------+
| [procedure]                                                                 |
|                                                                             |
| (file-creator-and-type                                                      |
| filename: path?                                                            |
| creator-bytes: (and/c bytes? #rx#"^....$")                                 |
| type-bytes: (and/c bytes? #rx#"^....$")                                    |
| (file-creator-and-type filename) → (and/c bytes? #rx#"^....$")(and/c bytes? |
| #rx#"^....$")                                                               |
| (file-creator-and-type filename)                                            |
| (and/c bytes? #rx#"^....$")                                                 |
| (and/c bytes? #rx#"^....$")                                                 |
| filename: path?                                                            |
+-----------------------------------------------------------------------------+
```

Gets or sets the creator and type of a file in Mac OS.

The get operation always returns #"????" and #"????" for
Unix or Windows. The set operation has no effect on Unix or
Windows.

```
+-----------------------------------------------------+
| [procedure]                                         |
|                                                     |
| (find-graphical-system-path what) → (or/c path? #f) |
| what: (or/c 'init-file 'x-display)                 |
+-----------------------------------------------------+
```

Finds a platform-specific (and possibly user- or machine-specific)
standard filename or directory. See also find-system-path.

The result depends on what, and a #f result is only
possible when what is 'x-display:

- 'init-file returns the,path to the user-specific
initialization file (containing Racket code). The directory part of
the path is the same path as returned for 'init-dir by
Racket’s find-system-path. The file name is
platform-specific:
Unix and Mac OS: `".gracketrc"`Windows: `"gracketrc.rktl"`
- 'x-display returns a “path” whose string identifies
the X11 display if specified by either the `-display` flag or the
`DISPLAY` environment variable when GRacket starts on Unix. For
other platforms, or when neither `-display` nor `DISPLAY`
was specified, the result is #f.

```
+--------------------------------------------------------------------------+
| [procedure]                                                              |
|                                                                          |
| (get-default-shortcut-prefix)                                            |
| → (case (system-type) [(windows) (list/c 'ctl)] [(macosx) (list/c 'cmd)] |
| [(unix) (list/c (or/c 'alt 'cmd 'meta 'ctl 'shift 'option))])            |
| (case (system-type)                                                      |
| [(windows) (list/c 'ctl)]                                                |
| [(macosx) (list/c 'cmd)]                                                 |
| [(unix) (list/c (or/c 'alt 'cmd 'meta 'ctl 'shift 'option))])            |
|                                                                          |
| ```racket                                                                |
| (case (system-type)                                                      |
|   [(windows) (list/c 'ctl)]                                              |
|   [(macosx)  (list/c 'cmd)]                                              |
|   [(unix)    (list/c (or/c 'alt 'cmd 'meta 'ctl 'shift 'option))])       |
| ```                                                                      |
+--------------------------------------------------------------------------+
```

Returns an immutable list specifying the default prefix for menu
shortcuts. See also
get-shortcut-prefix in selectable-menu-item<%>.

On Windows, the default is '(ctl). On Mac OS, the
default is '(cmd). On Unix, the default is normally
'(ctl), but the default can be changed through the
'GRacket:defaultMenuPrefix
preference low-level preference (see
Preferences).

```
+-------------------------------------------+
| [procedure]                               |
|                                           |
| (get-panel-background) → (is-a?/c color%) |
+-------------------------------------------+
```

Returns a shade of gray.

Historically, the result matched the color of
a panel% background, but panel% backgrounds can vary
on some platforms (e.g., when nested in a group-box-panel%),
so the result is no longer guaranteed to be related to a
panel%’s color.

See get-label-background-color for a closer approximation to
a panel background.

```
+-----------------------------------------------------+
| [procedure]                                         |
|                                                     |
| (get-highlight-background-color) → (is-a?/c color%) |
+-----------------------------------------------------+
```

Returns the color that is drawn behind selected text.

```
+---------------------------------------------------------+
| [procedure]                                             |
|                                                         |
| (get-highlight-text-color) → (or/c (is-a?/c color%) #f) |
+---------------------------------------------------------+
```

Returns the color that is used to draw selected text or #f if
selected text is drawn with its usual color.

```
+-------------------------------------------------+
| [procedure]                                     |
|                                                 |
| (get-label-background-color) → (is-a?/c color%) |
+-------------------------------------------------+
```

Returns an approximation of the color that is likely to appear behind
a control label. This color may not match the actual color of a
control’s background, since themes on some platforms may vary the color
for different contexts.

See also get-label-foreground-color.

Added in version 1.38 of package `gui-lib`.

```
+-------------------------------------------------+
| [procedure]                                     |
|                                                 |
| (get-label-foreground-color) → (is-a?/c color%) |
+-------------------------------------------------+
```

Returns an approximation of the color that is likely to be used for
the text of a control label. This color may not match the actual color
of label text, since themes on some platforms may vary the color for
different contexts.

Comparing the results of get-label-foreground-color and
get-label-background-color may be useful for detecting
whether a platform’s current theme is “dark mode” versus “light
mode.”

Added in version 1.38 of package `gui-lib`.

```
+----------------------------+
| [procedure]                |
|                            |
| (get-window-text-extent    |
| exact-nonnegative-integer? |
| exact-nonnegative-integer? |
| string: string?           |
| font: (is-a?/c font%)     |
| combine?: any/c = #f      |
+----------------------------+
```

Returns the pixel size of a string drawn as a window’s label or value
when drawn with the given font. The optional combine?
argument is as for get-text-extent in dc<%>.

See also get-text-extent in dc<%>.

```
+-------------------------------------------------+
| [procedure]                                     |
|                                                 |
| (graphical-read-eval-print-loop                 |
| eval-eventspace: (or/c eventspace? #f) = #f    |
| redirect-ports?: any/c = (not eval-eventspace) |
+-------------------------------------------------+
```

Similar to read-eval-print-loop, except that none of
read-eval-print-loop’s configuration parameters are used (such
as current-read) and the interaction occurs in a GUI window
instead of using the current input and output ports.

Expressions entered into the graphical read-eval-print loop can be
evaluated in an eventspace (and thread) that is distinct from the one
implementing the graphical-read-eval-print-loop
window (i.e., the current eventspace when
graphical-read-eval-print-loop is called).

If no eventspace is provided, or if #f is provided, an
evaluation eventspace is created using (make-eventspace)
with a new custodian; the eventspace and its threads are be shut down
when the user closes the graphical-read-eval-print-loop
window. If an eventspace is provided, closing the window performs no
shut-down actions on eventspace.

When redirect-ports? is true, the following parameters are
initialized in the created eventspace’s handler thread:

- current-output-port — writes to the frame
- current-error-port — writes to the frame
- current-input-port — always returns eof

The keymap for the read-eval-print loop’s editor is initialized by
calling the current keymap initializer procedure, which is determined
by the
current-text-keymap-initializer parameter.

```
+-----------------------------------+
| [procedure]                       |
|                                   |
| (graphical-system-type) → symbol? |
+-----------------------------------+
```

Returns a symbol indicating the platform native GUI layer on which
racket/gui is running. The current possible values are as
follows:

- 'win32 (Windows)
- 'cocoa (Mac OS)
- 'gtk2 — GTK+ version 2
- 'gtk3 — GTK+ version 3

Added in version 1.15 of package `gui-lib`.

```
+----------------------------------------+
| [procedure]                            |
|                                        |
| (textual-read-eval-print-loop) → void? |
+----------------------------------------+
```

Similar to read-eval-print-loop, except that evaluation uses
a newly created eventspace like graphical-read-eval-print-loop.

The current-prompt-read parameter is used in the current
thread to read input. The result is queued for evaluation and
printing in the created eventspace’s handler thread, which
uses current-eval and current-print. After printing
completes for an interaction result, the next expression in read in
the original thread, and so on.

If an exn:break exception is raised in the original thread
during reading, it aborts the current call to (current-read)
and a new one is started. If an exn:break exception is raised
in the original thread while waiting for an interaction to complete, a
break is sent (via break-thread) to the created eventspace’s
handler thread.

```
+---------------------------------------------------------------------------+
| [procedure]                                                               |
|                                                                           |
| (get-current-mouse-state)                                                 |
| → (is-a?/c point%)(listof (or/c 'left 'middle 'right 'shift 'control 'alt |
| 'meta 'caps))                                                             |
| (is-a?/c point%)                                                          |
| (listof (or/c 'left 'middle 'right 'shift 'control 'alt 'meta 'caps))     |
| (listof (or/c 'left 'middle 'right                                        |
| 'shift 'control 'alt 'meta 'caps))                                        |
|                                                                           |
| ```racket                                                                 |
| (listof (or/c 'left 'middle 'right                                        |
|               'shift 'control 'alt 'meta 'caps))                          |
| ```                                                                       |
+---------------------------------------------------------------------------+
```

> **Note:** On Mac OS 10.5 and earlier, mouse-button information is
not available, so the second result includes only symbols for modifier
keys.

Returns the current location of the mouse in screen coordinates, and
returns a list of symbols for mouse buttons and modifier keys that are
currently pressed.

```
+-----------------------------------+
| [procedure]                       |
|                                   |
| (hide-cursor-until-moved) → void? |
+-----------------------------------+
```

Hides the cursor until the user moves the mouse or clicks the mouse
button. (For some platforms, the cursor is not hidden if it is over
a window in a different eventspace or application.)

```
+-----------------------+
| [procedure]           |
|                       |
| (is-busy?) → boolean? |
+-----------------------+
```

Returns #t if a busy cursor has been installed with
begin-busy-cursor and not removed with
end-busy-cursor.

```
+--------------------------------------+
| [procedure]                          |
|                                      |
| (label->plain-label label) → string? |
| label: string?                      |
+--------------------------------------+
```

Strips shortcut ampersands from label, removes parenthesized
ampersand–character combinations along with any surrounding space,
and removes anything after a tab. Overall, it returns the label as it would
appear on a button on a platform without support for mnemonics.

```
+----------------------------------------------------------+
| [procedure]                                              |
|                                                          |
| (make-gl-bitmap width height config) → (is-a?/c bitmap%) |
| width: exact-positive-integer?                          |
| height: exact-positive-integer?                         |
| config: (is-a?/c gl-config%)                            |
+----------------------------------------------------------+
```

Creates a bitmap that supports both normal dc<%> drawing an
OpenGL drawing through a context returned by get-gl-context in dc<%>.

For dc<%> drawing, an OpenGL-supporting bitmap draws like a
bitmap from make-screen-bitmap on some platforms, while it
draws like a bitmap instantiated directly from bitmap% on
other platforms.

Be aware that on Unix systems, GLX may choose indirect rendering for OpenGL
drawing to bitmaps, which can limit its features to OpenGL 1.4 or below.

```
+-----------------------------------------+
| [procedure]                             |
|                                         |
| (make-gui-empty-namespace) → namespace? |
+-----------------------------------------+
```

Like make-base-empty-namespace, but with
racket/class and racket/gui/base also
attached to the result namespace.

```
+-----------------------------------+
| [procedure]                       |
|                                   |
| (make-gui-namespace) → namespace? |
+-----------------------------------+
```

Like make-base-namespace, but with racket/class and
racket/gui/base also required into the top-level
environment of the result namespace.

```
+-------------------------------------------------------+
| [procedure]                                           |
|                                                       |
| (make-screen-bitmap width height) → (is-a?/c bitmap%) |
| width: exact-positive-integer?                       |
| height: exact-positive-integer?                      |
+-------------------------------------------------------+
```

Creates a bitmap that draws in a way that is the same as drawing to a
canvas in its default configuration.

In particular, on Mac OS when the main monitor is in Retina display
mode, a drawing unit corresponds to two pixels, and the bitmap
internally contains four times as many pixels as requested by
width and height. On Windows, the backing scale
is similarly increased by adjusting the operating-system text scale.
See also get-display-backing-scale.

See also Portability and Bitmap Variants.

```
+-----------------------------------------+
| [procedure]                             |
|                                         |
| (play-sound filename async?) → boolean? |
| filename: path-string?                 |
| async?: any/c                          |
+-----------------------------------------+
```

Plays a sound file. If async? is false, the function does not
return until the sound completes. Otherwise, it returns immediately.
The result is #t if the sound plays successfully, #f
otherwise.

On Windows, MCI is used to play sounds, so file formats such as
`".wav"` and `".mp3"` should be supported.

On Mac OS, Quicktime is used to play sounds; most sound
formats (`".wav"`, `".aiff"`, `".mp3"`) are supported in recent versions of
Quicktime. To play `".wav"` files, Quicktime 3.0 (compatible
with OS 7.5 and up) is required.

On Unix, the function invokes an external sound-playing program—looking
by default for a few known programs (`paplay`, `aplay`, `play`,
`esdplay`, `sndfile-play`, `audioplay`). A
play command can be defined through the 'GRacket:playcmd
preference
preference (see Preferences). The preference can hold a
program name, or a format string containing a single ~a
where the filename should be substituted—and used as a shell
command. (Don’t use ~s, since the string that is used
with the format string will be properly quoted and wrapped in double
quotes.) A plain command name is usually better, since execution is
faster. The command’s output is discarded, unless it returns an
error code, in which case the last part of the error output is
shown.

Changed in version 1.22 of package `gui-lib`: On Windows, added support for multiple
sounds at once and file format such as
`".mp3"`.

```
+----------------------------------+
| [procedure]                      |
|                                  |
| (position-integer? v) → boolean? |
| v: any/c                        |
+----------------------------------+
```

Equivalent to (integer-in-10000001000000).

```
+--------------------------------------------+
| [procedure]                                |
|                                            |
| (positive-dimension-integer? v) → boolean? |
| v: any/c                                  |
+--------------------------------------------+
```

Equivalent to (integer-in11000000).

```
+----------------------------+
| [procedure]                |
|                            |
| (register-collecting-blit  |
| canvas: (is-a?/c canvas%) |
| x: position-integer?      |
| y: position-integer?      |
| w: dimension-integer?     |
| h: dimension-integer?     |
| on: (is-a?/c bitmap%)     |
| off: (is-a?/c bitmap%)    |
| on-x: real? = 0           |
| on-y: real? = 0           |
| off-x: real? = 0          |
| off-y: real? = 0          |
+----------------------------+
```

Registers a “blit” to occur when garbage collection starts and
ends. When garbage collection starts, on is drawn at
location x and y within canvas, if
canvas is shown. When garbage collection ends, the drawing
is reverted. On some platforms, the drawing is reverted by drawing
the off bitmap and on some platforms the drawing is reverted
automatically, without a need for the off bitmap.

The background behind on may or may not be the usual contents
of the canvas, so on
should be a solid image. Neither the canvas’s scale nor its scroll position is
applied when drawing the bitmaps. Only the portion of on within
w and h pixels is used; if on-x and
on-y are specified, they specify an offset within the bitmap
that is used for drawing; similarly off-x and off-y
specify an offset within off.

The blit is automatically unregistered if canvas becomes
invisible and inaccessible. Multiple registrations can be installed
for the same canvas.

See also unregister-collecting-blit.

```
+---------------------------------------------+
| [procedure]                                 |
|                                             |
| (unregister-collecting-blit canvas) → void? |
| canvas: (is-a?/c canvas%)                  |
+---------------------------------------------+
```

Unregisters all blit requests installed for canvas with
register-collecting-blit.

```
+----------------------------------------------+
| [procedure]                                  |
|                                              |
| (send-message-to-window x y message) → any/c |
| x: position-integer?                        |
| y: position-integer?                        |
| message: any/c                              |
+----------------------------------------------+
```

Finds the frontmost top-level window at
(x, y) in global coordinates. If a window is there,
this function calls the window’s on-message method, providing message as the method’s
argument; the result of the function call is the result returned by
the method. If no Racket window is at the given coordinates, or if it
is covered by a non-Racket window at (x, y),
#f is returned.

```
+---------------------------------+
| [procedure]                     |
|                                 |
| (spacing-integer? v) → boolean? |
| v: any/c                       |
+---------------------------------+
```

Equivalent to (integer-in01000).

```
+------------------------------------------------+
| [procedure]                                    |
|                                                |
| (system-position-ok-before-cancel?) → boolean? |
+------------------------------------------------+
```

Returns #t on Windows—indicating that a dialog with
OK and Cancel buttons should place the
OK button on to left of the Cancel button—and
returns #f on Mac OS and Unix.

```
+----------------------------------------+
| [value]                                |
|                                        |
| the-clipboard: (is-a?/c clipboard<%>) |
+----------------------------------------+
```

See clipboard<%>.

```
+----------------------------------------------------+
| [value]                                            |
|                                                    |
| the-x-selection-clipboard: (is-a?/c clipboard<%>) |
+----------------------------------------------------+
```

See clipboard<%>.

```
+------------------------------+
| [procedure]                  |
|                              |
| (label-string? v) → boolean? |
| v: any/c                    |
+------------------------------+
```

Returns #t if v is a string whose length is less than or equal to 200.

This predicate is typically used as the contract for strings that
appear in GUI objects. In some cases, such as the label in a button%
or menu-item% object, the character & is treated specially
to indicate that the following character is used in keyboard navigation. See
set-label in labelled-menu-item<%> for one such example.
In other cases, such as the label on a frame%, & is not
treated specially.

```
+---------------------------------+
| [procedure]                     |
|                                 |
| (key-code-symbol? v) → boolean? |
| v: any/c                       |
+---------------------------------+
```

Returns #t if the argument is a symbol that can be returned by
key-event%’s method get-key-code.
