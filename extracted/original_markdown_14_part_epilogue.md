<!-- Extracted from original_html/part_epilogue.html -->
<!-- Canonical English source for Japanese translation -->

## Epilogue: Moving On

### Contents

- Computing
- Program Design
- Onward, Developers and Computer Scientists
- Onward, Accountants, Journalists, Surgeons, and Everyone Else

You have reached the end of this introduction to computing and programming,
or program design, as we say here. While there is more to learn about both
subjects, this is a good point to stop, summarize, and look ahead.

### Computing

In elementary school, you learned to calculate with numbers. At first, you
used numbers to count real things: three apples, five friends, twelve
bagels. A bit later, you encountered addition, subtraction,
multiplication, and even division; then came fractions. Eventually, you
found out about variables and functions, which your teachers called
algebra. Variables represented numbers, and functions related
numbers to numbers.

Because you used numbers throughout this process, you didn’t think much of
numbers as a means to represent information about the real world. Yes, you
had started with three bears, five wolves, and twelve horses; but by high
school, nobody reminded you of this relationship.

When you move from mathematical calculations to computing, the step from
information to data and back becomes central. Nowadays, programs process
representations of music, videos, molecules, chemical compounds, business
case studies, electrical diagrams, and blueprints. Fortunately, you don’t
need to encode all this information with numbers or, worse, just
0 and 1; if you had to, life would be unimaginably
tedious. Instead, computing generalizes arithmetic and algebra so that
when you program, you can code—and your programs can compute—with
strings, Booleans, characters, structures, lists, functions, and many more
kinds of data.

Classes of data and their functions come with equational laws that explain
their meaning, just like the laws for numbers and their functions. While
these equational laws are as simple as “(+11) evaluates to
2” and “(not#true) equals #false,” you can
use them to predict the behavior of entire programs. When you run a
program, you actually just apply one of its many functions, an act that you
can explain with the beta rule first mentioned in Intermezzo 1: Beginning Student Language. Once the
variables are replaced with values, the laws of data take over until you
have either only a value or another function application. But yes, that’s
all there is to computing.

### Program Design

A typical software development project requires the collaboration of many
programmers, and the result consists of thousands of functions. Over the
life span of such a project, programmers come and go. Hence, the design
structure of programs is really a means of communication among programmers
across time. When you approach code that someone else wrote some time ago,
the program ought to express its purpose and its relationships to other
pieces—because that other person might not be around anymore.

In such a dynamic context, programmers must create programs in a
disciplined manner if they wish to work reasonable numbers of hours or
produce high-quality products. Following a systematic design method
guarantees that the program organization is comprehensible. Others can
then easily understand the pieces and the whole, and then fix bugs or add
new pieces of functionality.

The design process of this book is one of these methods, and you ought to
follow it whenever you create programs you might care about. You start
with an analysis of the world of information and a description of the data
that represents the information. Then you make a plan, a work list of
functions needed. If this list is large, you refine the process in an
iterative manner. You start with a subset of functions that quickly yields
a product with which a client can interact. As you observe these
interactions, you will quickly figure out which elements of your work list
to tackle next.

Designing a program, or only a function, requires a rigorous understanding
of what it computes. Unless you can describe the purpose of a piece of
code with a concise statement, you cannot produce anything useful for
future programmers. Make up, and work through, examples. Turn these
examples into a suite of tests. This test suite is even more important
when it comes to future modifications of the program. Anyone who changes
the code can rerun these tests and reconfirm that the program still works
for the basic examples.

Eventually your program will also fail. Other programmers may use it in an
unanticipated manner. Real-world users may find differences between
expected and actual behavior. Because you have designed the code in a
systematic manner, you will know what to do. You will formulate a failing
test case for your program’s main function. From this one test, you will
derive a test case for each function that the main function
mentions. Those functions that pass their new tests do not contribute to
the failure. One of the others does; on occasion, several might collude to
create a bug. If the broken function composes others, resume the
test creation; otherwise you have found the source of the problem. You
will know that you have fixed the problem when the program as a whole
passes all its tests.

No matter how hard you work, a function or program isn’t done the first
time it passes the test suite. You must find time to inspect it for design
flaws and repetitions of designs. If you find any design patterns, form
new abstractions or use existing abstractions to eliminate these patterns.

If you respect these guidelines, you will produce solid software with
reasonable effort. It will work because you understand why and how it
works. Others who must modify or enhance your software will understand it
quickly because the code communicates its process and its
purpose. Working through this book got you started. Now you must practice,
practice, practice. And you will have to learn a lot more about program
design and computing than a first book can teach.

### Onward, Developers and Computer Scientists

Right now, you might be wondering what to study next. The answer is both
more programming and more computing.

As a student of program design, your next task is to learn how the design
process applies in the setting of a full-fledged programming language. Some
of these languages are like the teaching languages, and the transition will be
easy. Others require a different mind-set because they offer means for
spelling out data definitions (classes and objects) and
for formulating signatures so that they are cross-checked before the
program is run (types). In addition, you will also have to learn how
to scale the design process to the use and production of so-called
frameworks (“stacks”) and components. Roughly speaking, frameworks
abstract pieces of functionality—for example, graphical user interfaces,
database connections, and web connectivity—that are common to many
software systems. You need to learn to instantiate these abstractions, and
your programs will compose these instances to create coherent
systems. Similarly, learning to create new system components is also
inherently a part of scaling up your skills.

> **Note:** Given your knowledge, it is
easy for you to learn Racket, the language behind the teaching
languages in this book. See
“ Realm of Racket ” for
one possible introduction.

As a student of computing, you will also have to expand your understanding
of the computational process. This book has focused on the laws that
describe the process itself. In order to function as a real software
engineer, you need to learn what the process costs, at both a theoretical
level and a practical one. Studying the concept of big-O in some more depth
is a first, small step in this direction; learning to measure and analyze a
program’s performance is the real goal because you will need this skill as
a developer on a regular basis. Above and beyond these basic ideas, you
will also need knowledge about hardware, networking, layering of software,
and specialized algorithms in various disciplines.

### Onward, Accountants, Journalists, Surgeons, and Everyone Else

Some of you wanted to see what computing and programming are all about. You
now know that computing is merely a generalization of calculating, and you
may sense how useful program design is to you. Even if you never
develop programs again, you know what distinguishes a garage programmer
from a serious software developer. When you interact with developers as a
professional, you know that systematic design matters because it affects
your quality of life and the bottom line of your business.

In reality, though, you are likely to “program” again, on a regular basis;
you may just fail to see your activities in this light. Imagine a
journalist for a moment. His story starts with the collection of
information and data, laying it out, organizing it, and adding
anecdotes. If you squint, you’ll see that this is only step one of the
design process. Let’s turn to a family doctor who, after checking up on
your symptoms, formulates a hypothesis of what might affect you. Do you see
step two? Or, think of a lawyer who illustrates the point of an
argument with a number of examples—an instance of step three. Finally, a
civil engineer cross-checks the bridge as it is built to make sure it lives
up to the blueprint and the underlying static calculations. Cross-checking
is a form of testing—step six of the process; it compares actual
measurements with expected values from the predictive calculations. Each of
these professionals develops a system to work effectively and efficiently;
and deep down, this system is likely to resemble the design process
employed in this book.

Now, once you accept that many activities are a form of programming, you
can transfer additional ideas from the design process to your own life. For
example, if you recognize patterns, you may take the little additional time
it takes to create an “abstraction”—a single point of control—to
simplify your future work. So, regardless of whether you become an
accountant or a doctor or something else, remember the design processes
wherever you go and whatever you do.

Exercise Write a short essay on how the design process
may help you with your chosen profession.
