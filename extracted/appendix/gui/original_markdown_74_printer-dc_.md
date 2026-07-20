<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/printer-dc_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/printer-dc_.html -->
<!-- Canonical English source for Japanese translation -->

```
+---------------------------+-------+
| classprinter-dc%: class? |       |
+---------------------------+-------+
| superclass: object%       |       |
| extends:                  | dc<%> |
+---------------------------+-------+
```

A printer-dc% object is a printer device context. A newly
created printer-dc% object obtains orientation (portrait
versus landscape) and scaling information from the current
ps-setup% object, as determined by the
current-ps-setup parameter. This information can be
configured by the user through a dialog shown by
get-page-setup-from-user.

Be sure to use the following methods to start/end drawing:

- start-doc
- start-page
- end-page
- end-doc

Attempts to use a drawing method outside of an active page raises an exception.

See also post-script-dc%.

When the end-doc method is called on a
printer-dc% instance, the user may receive a dialog
to determine how the document is printed.

```
+-------------------------------------------------------------+
| [constructor]                                               |
|                                                             |
| (new printer-dc% [[parent parent]]) → (is-a?/c printer-dc%) |
| parent: (or/c (is-a?/c frame%) (is-a?/c dialog%) #f) = #f  |
+-------------------------------------------------------------+
```

If parent is not #f, it is may be as the parent window
of the dialog (if any) presented by end-doc.
