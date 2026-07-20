<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/clipboard-client_.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/clipboard-client_.html -->
<!-- Canonical English source for Japanese translation -->

```
+---------------------------------+
| classclipboard-client%: class? |
+---------------------------------+
| superclass: object%             |
+---------------------------------+
```

A clipboard-client% object allows a program to take over
the clipboard and service requests for clipboard data. See
clipboard<%> for more information.

A clipboard-client% object is associated to an eventspace
when it becomes the current client; see
set-clipboard-client for more information.

```
+-------------------------------------------------------+
| [constructor]                                         |
|                                                       |
| (new clipboard-client%) → (is-a?/c clipboard-client%) |
+-------------------------------------------------------+
```

Creates a clipboard client that supports no data formats.

```
+---------------------------------------------------+
| [method]                                          |
|                                                   |
| (send a-clipboard-client add-type format) → void? |
| format: string?                                  |
+---------------------------------------------------+
```

Adds a new data format name to the list supported by the clipboard
client.

The format string is typically four capital letters. (On
Mac OS, only four characters for format are ever used.)
For example, "TEXT" is the name of the UTF-8-encoded string
format. New format names can be used to communicate application- and
platform-specific data formats.

```
+-------------------------------------------+
| [method]                                  |
|                                           |
| (send a-clipboard-client get-data format) |
| → (or/c bytes? string? #f)                |
| format: string?                          |
+-------------------------------------------+
```

Called when a process requests clipboard data while this client is the
current one for the clipboard. The requested format is passed to the
method, and the result should be a byte string matching the requested
format, or #f if the request cannot be fulfilled.

Only data format names in the client’s list will be passed to this
method; see add-type.

When this method is called by the clipboard, the current eventspace is
the same as the client’s eventspace. If, at the point of the
clipboard request, the current eventspace is not the client’s
eventspace, then current thread is guaranteed to be the handler
thread of the client’s eventspace.

```
+--------------------------------------------------------+
| [method]                                               |
|                                                        |
| (send a-clipboard-client get-types) → (listof string?) |
+--------------------------------------------------------+
```

Returns a list of names that are the data formats supported by the
clipboard client.

```
+-----------------------------------------------+
| [method]                                      |
|                                               |
| (send a-clipboard-client on-replaced) → void? |
+-----------------------------------------------+
```

Called when a clipboard client is dismissed as the clipboard owner
(because the clipboard has be taken by another client or by an
external application).
