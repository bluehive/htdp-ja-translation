<!-- Appendix manual: gui -->
<!-- Source URL path: /gui/Startup_Actions.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/gui/Startup_Actions.html -->
<!-- Canonical English source for Japanese translation -->

## 12 Startup Actions

The racket/gui/base module can be instantiated only
once per operating-system process, because it sets hooks in the Racket
run-time system to coordinate between Racket thread scheduling and GUI
events. Attempting to instantiate it a second time results in an
exception. Furthermore, on Mac OS, the sole instantiation of
racket/gui/base must be in the process’s original
place.

Instantiating racket/gui/base sets two parameters:

- executable-yield-handler — The executable yield
handler is set to evaluate (yieldinitial-eventspace)
before chaining to the previously installed handler. As a
result, the Racket process will normally wait until all
top-level windows are closed, all callbacks are invoked, and all
timers are stopped in the initial eventspace before the process
exits.
- current-get-interaction-input-port — The interaction
port handler is set to wrap the previously installed handler’s
result to yield to GUI events when the input port blocks on
reading. This extension of the default handler’s behavior is
triggered only when the current thread is the handler thread of
some eventspace, in which case current-eventspace is
set to the eventspace before invoking yield. As a
result, GUI events normally can be handled while
read-eval-print-loop (such as run by the plain Racket
executable) is blocked on input.

The thread where racket/gui/base is instantiated also
becomes the handler thread for the initial eventspace. See also
Eventspaces and Threads.
