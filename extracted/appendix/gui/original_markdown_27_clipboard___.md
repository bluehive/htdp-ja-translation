<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/clipboard___.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/clipboard___.html -->
<!-- Canonical English source for Japanese translation -->

```
+------------------------------------+
| interfaceclipboard<%>: interface? |
+------------------------------------+
+------------------------------------+
```

A single clipboard<%> object, the-clipboard,
manages the content of the system-wide clipboard for cut and paste.

On Unix, a second clipboard<%> object,
the-x-selection-clipboard, manages the content of the
system-wide X11 selection. If the 'GRacket:selectionAsClipboard
preference
preference (see Preferences) is set to a non-zero true value,
however, then the-clipboard is always the same as
the-x-selection-clipboard, and the system-wide X11 clipboard
is not used.

On Windows and Mac OS, the-x-selection-clipboard is
always the same as the-clipboard.

Data can be entered into a clipboard in one of two ways: by setting
the current clipboard string or byte string, or by installing a
clipboard-client% object. When a client is installed,
requests for clipboard data are directed to the client.

Generic data is always retrieved from the clipboard as a byte
string. When retrieving clipboard data, a data type string specifies
the format of the data string. The availability of different
clipboard formats is determined by the current clipboard owner.

```
+----------------------------------------------+
| [method]                                     |
|                                              |
| (send a-clipboard get-clipboard-bitmap time) |
| → (or/c (is-a?/c bitmap%) #f)                |
| time: exact-integer?                        |
+----------------------------------------------+
```

Gets the current clipboard contents as a bitmap (Windows, Mac OS),
returning #f if the clipboard does not contain a bitmap.

See
get-clipboard-data for information on eventspaces and the current clipboard client.

See Cut and Paste Time Stamps for a discussion of the time argument. If
time is outside the platform-specific range of times,
an exn:fail:contract exception is raised.

```
+--------------------------------------+
| [method]                             |
|                                      |
| (send a-clipboard get-clipboard-data |
| → (or/c bytes? string? #f)           |
| format: string?                     |
| time: exact-integer?                |
+--------------------------------------+
```

Gets the current clipboard contents in a specific format, returning
#f if the clipboard does not contain data in the requested
format.

If the clipboard client is associated to an eventspace that is not the
current one, the data is retrieved through a callback event in the
client’s eventspace. If no result is available within one second, the
request is abandoned and #f is returned.

See add-type in clipboard-client% for information on
format.

See Cut and Paste Time Stamps for a discussion of the time argument. If
time is outside the platform-specific range of times,
an exn:fail:contract exception is raised.

```
+--------------------------------------------------------+
| [method]                                               |
|                                                        |
| (send a-clipboard get-clipboard-string time) → string? |
| time: exact-integer?                                  |
+--------------------------------------------------------+
```

Gets the current clipboard contents as simple text, returning
"" if the clipboard does not contain any text.

See get-clipboard-data for information on
eventspaces and the current clipboard client.

See Cut and Paste Time Stamps for a discussion of the time argument. If
time is outside the platform-specific range of times,
an exn:fail:contract exception is raised.

```
+------------------------------------------------------------+
| [method]                                                   |
|                                                            |
| (send a-clipboard same-clipboard-client? owner) → boolean? |
| owner: (is-a?/c clipboard-client%)                        |
+------------------------------------------------------------+
```

Returns #t if owner currently owns the clipboard,
#f otherwise.

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-clipboard set-clipboard-bitmap |
| new-bitmap: (is-a?/c bitmap%)         |
| time: exact-integer?                  |
+----------------------------------------+
```

Changes the current clipboard contents to new-bitmap (Windows, Mac OS)
and releases the current clipboard client (if any).

See Cut and Paste Time Stamps for
a discussion of the time argument. If time is outside
the platform-specific range of times, an exn:fail:contract exception is raised.

```
+-----------------------------------------+
| [method]                                |
|                                         |
| (send a-clipboard set-clipboard-client  |
| new-owner: (is-a?/c clipboard-client%) |
| time: exact-integer?                   |
+-----------------------------------------+
```

Changes the clipboard-owning client: sets the client to
new-owner and associates new-owner with the current
eventspace (as determined by current-eventspace). The
eventspace association is removed when the client is no longer the
current one.

See Cut and Paste Time Stamps for a discussion of the time argument. If
time is outside the platform-specific range of times,
an exn:fail:contract exception is raised.

```
+----------------------------------------+
| [method]                               |
|                                        |
| (send a-clipboard set-clipboard-string |
| new-text: string?                     |
| time: exact-integer?                  |
+----------------------------------------+
```

Changes the current clipboard contents to new-text,
and releases the current clipboard client (if any).

See Cut and Paste Time Stamps for
a discussion of the time argument. If time is outside
the platform-specific range of times, an exn:fail:contract exception is raised.
