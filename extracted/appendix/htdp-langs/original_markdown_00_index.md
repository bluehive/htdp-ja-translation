<!-- Appendix manual: htdp-langs -->
<!-- Source URL path: /htdp-langs/index.html -->
<!-- Canonical English source for Japanese appendix translation -->

<!-- Extracted from appendix_original_html/htdp-langs/index.html -->
<!-- Canonical English source for Japanese translation -->

# How to Design Programs Languages

The languages documented in this manual are provided by DrRacket to be
used with the How to Design
Programs book.

When programs in these languages are run in DrRacket, any part of the
program that was not run is highlighted in orange and black. These
colors are intended to give the programmer feedback about the parts of
the program that have not been tested. To avoid seeing these colors,
use check-expect to test your program. Of course, just
because you see no colors, does not mean that your program has been
fully tested; it simply means that each part of the program has been run
(at least once).

While these languages are normally selected using the Choose Language dialog
in DrRacket, they can also be accessed using the #lang language
directive as the first line of code in DrRacket or other editors.

- Beginning Student #lang htdp/bsl
- Beginning Student with List Abbreviations #lang htdp/bsl+
- Intermediate Student #lang htdp/isl
- Intermediate Student with lambda #lang htdp/isl+
- Advanced Student #lang htdp/asl

### Contents

- 1.1 Pre-defined Variables
- 1.2 Template Variables
- 1.3 Syntax
- 1.4 Signatures
- 1.4.1 Signature Forms
- 1.4.2 Struct Signatures
- 1.5 Pre-defined Functions
- 1.6 Numbers: Integers, Rationals, Reals, Complex, Exacts, Inexacts
- 1.7 Booleans
- 1.8 Symbols
- 1.9 Lists
- 1.10 Posns
- 1.11 Characters
- 1.12 Strings
- 1.13 Images
- 1.14 Misc
- 1.15 Signatures
- 2.1 Pre-defined Variables
- 2.2 Template Variables
- 2.3 Syntaxes for Beginning Student with List Abbreviations
- 2.4 Common Syntaxes
- 2.5 Signatures
- 2.5.1 Signature Forms
- 2.5.2 Struct Signatures
- 2.6 Pre-defined Functions
- 2.7 Numbers: Integers, Rationals, Reals, Complex, Exacts, Inexacts
- 2.8 Booleans
- 2.9 Symbols
- 2.10 Lists
- 2.11 Posns
- 2.12 Characters
- 2.13 Strings
- 2.14 Images
- 2.15 Misc
- 2.16 Signatures
- 3.1 Pre-defined Variables
- 3.2 Template Variables
- 3.3 Syntax for Intermediate
- 3.4 Common Syntaxes
- 3.5 Signatures
- 3.5.1 Signature Forms
- 3.5.2 Struct Signatures
- 3.6 Pre-defined Functions
- 3.7 Numbers: Integers, Rationals, Reals, Complex, Exacts, Inexacts
- 3.8 Booleans
- 3.9 Symbols
- 3.10 Lists
- 3.11 Posns
- 3.12 Characters
- 3.13 Strings
- 3.14 Images
- 3.15 Misc
- 3.16 Signatures
- 3.17 Numbers (relaxed conditions)
- 3.18 String (relaxed conditions)
- 3.19 Posn
- 3.20 Higher-Order Functions
- 4.1 Pre-defined Variables
- 4.2 Template Variables
- 4.3 Syntax for Intermediate with Lambda
- 4.4 Common Syntaxes
- 4.5 Pre-defined Functions
- 4.6 Signatures
- 4.6.1 Signature Forms
- 4.6.2 Struct Signatures
- 4.7 Numbers: Integers, Rationals, Reals, Complex, Exacts, Inexacts
- 4.8 Booleans
- 4.9 Symbols
- 4.10 Lists
- 4.11 Posns
- 4.12 Characters
- 4.13 Strings
- 4.14 Images
- 4.15 Misc
- 4.16 Signatures
- 4.17 Numbers (relaxed conditions)
- 4.18 String (relaxed conditions)
- 4.19 Posn
- 4.20 Higher-Order Functions
- 4.21 Numbers (relaxed conditions plus)
- 4.22 Higher-Order Functions (with Lambda)
- 5.1 Pre-defined Variables
- 5.2 Template Variables
- 5.3 Syntax for Advanced
- 5.4 Common Syntaxes
- 5.5 Pre-Defined Functions
- 5.6 Signatures
- 5.6.1 Signature Forms
- 5.6.2 Struct Signatures
- 5.7 Numbers: Integers, Rationals, Reals, Complex, Exacts, Inexacts
- 5.8 Booleans
- 5.9 Symbols
- 5.10 Lists
- 5.11 Posns
- 5.12 Characters
- 5.13 Strings
- 5.14 Images
- 5.15 Misc
- 5.16 Signatures
- 5.17 Numbers (relaxed conditions)
- 5.18 String (relaxed conditions)
- 5.19 Posn
- 5.20 Higher-Order Functions
- 5.21 Numbers (relaxed conditions plus)
- 5.22 Higher-Order Functions (with Lambda)
- 5.23 Reading and Printing
- 5.24 Vectors
- 5.25 Boxes
- 5.26 Hash Tables
