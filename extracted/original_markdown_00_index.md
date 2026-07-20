<!-- Extracted from original_html/index.html -->
<!-- Canonical English source for Japanese translation -->

# How to Design Programs, Second Edition

> **Note:** Please send reports about mistakes to authors @ htdp.org

```
+--------------------------------------------------+
| Matthias Felleisen, ⏎ Robert Bruce Findler, ⏎ M… |
+--------------------------------------------------+
+--------------------------------------------------+
```

```
+--------------------------------------------------+
| © 1 August 2014 MIT Press ⏎ This material is co… |
+--------------------------------------------------+
+--------------------------------------------------+
```

```
+-------------------------------------------------+
| Released on Thursday, May 28th, 2026 10:37:57am |
+-------------------------------------------------+
+-------------------------------------------------+
```

### Contents

- Systematic Program Design
- DrRacket and the Teaching Languages
- Skills that Transfer
- This Book and Its Parts
- The Differences
- Acknowledgments from the First Edition
- Acknowledgments
- Arithmetic and Arithmetic
- Inputs and Output
- Many Ways to Compute
- One Program, Many Definitions
- One More Definition
- You Are a Programmer Now
- Not!
- 1 Arithmetic
- 1.1 The Arithmetic of Numbers
- 1.2 The Arithmetic of Strings
- 1.3 Mixing It Up
- 1.4 The Arithmetic of Images
- 1.5 The Arithmetic of Booleans
- 1.6 Mixing It Up with Booleans
- 1.7 Predicates: Know Thy Data
- 2 Functions and Programs
- 2.1 Functions
- 2.2 Computing
- 2.3 Composing Functions
- 2.4 Global Constants
- 2.5 Programs
- 3 How to Design Programs
- 3.1 Designing Functions
- 3.2 Finger Exercises: Functions
- 3.3 Domain Knowledge
- 3.4 From Functions to Programs
- 3.5 On Testing
- 3.6 Designing World Programs
- 3.7 Virtual Pet Worlds
- 4 Intervals, Enumerations, and Itemizations
- 4.1 Programming with Conditionals
- 4.2 Computing Conditionally
- 4.3 Enumerations
- 4.4 Intervals
- 4.5 Itemizations
- 4.6 Designing with Itemizations
- 4.7 Finite State Worlds
- 5 Adding Structure
- 5.1 From Positions to posn Structures
- 5.2 Computing with posn s
- 5.3 Programming with posn
- 5.4 Defining Structure Types
- 5.5 Computing with Structures
- 5.6 Programming with Structures
- 5.7 The Universe of Data
- 5.8 Designing with Structures
- 5.9 Structure in the World
- 5.10 A Graphical Editor
- 5.11 More Virtual Pets
- 6 Itemizations and Structures
- 6.1 Designing with Itemizations, Again
- 6.2 Mixing Up Worlds
- 6.3 Input Errors
- 6.4 Checking the World
- 6.5 Equality Predicates
- 7 Summary
- BSL Vocabulary
- BSL Grammar
- BSL Meaning
- Meaning and Computing
- BSL Errors
- Boolean Expressions
- Constant Definitions
- Structure Type Definitions
- BSL Tests
- BSL Error Messages
- 8 Lists
- 8.1 Creating Lists
- 8.2 What Is ' ( ), What Is cons
- 8.3 Programming with Lists
- 8.4 Computing with Lists
- 9 Designing with Self-Referential Data Definitions
- 9.1 Finger Exercises: Lists
- 9.2 Non-empty Lists
- 9.3 Natural Numbers
- 9.4 Russian Dolls
- 9.5 Lists and World
- 9.6 A Note on Lists and Sets
- 10 More on Lists
- 10.1 Functions that Produce Lists
- 10.2 Structures in Lists
- 10.3 Lists in Lists, Files
- 10.4 A Graphical Editor, Revisited
- 11 Design by Composition
- 11.1 The list Function
- 11.2 Composing Functions
- 11.3 Auxiliary Functions that Recur
- 11.4 Auxiliary Functions that Generalize
- 12 Projects: Lists
- 12.1 Real-World Data: Dictionaries
- 12.2 Real-World Data: iTunes
- 12.3 Word Games, Composition Illustrated
- 12.4 Word Games, the Heart of the Problem
- 12.5 Feeding Worms
- 12.6 Simple Tetris
- 12.7 Full Space War
- 12.8 Finite State Machines
- 13 Summary
- Quote
- Quasiquote and Unquote
- Unquote Splice
- 14 Similarities Everywhere
- 14.1 Similarities in Functions
- 14.2 Different Similarities
- 14.3 Similarities in Data Definitions
- 14.4 Functions Are Values
- 14.5 Computing with Functions
- 15 Designing Abstractions
- 15.1 Abstractions from Examples
- 15.2 Similarities in Signatures
- 15.3 Single Point of Control
- 15.4 Abstractions from Templates
- 16 Using Abstractions
- 16.1 Existing Abstractions
- 16.2 Local Definitions
- 16.3 Local Definitions Add Expressive Power
- 16.4 Computing with local
- 16.5 Using Abstractions, by Example
- 16.6 Designing with Abstractions
- 16.7 Finger Exercises: Abstraction
- 16.8 Projects: Abstraction
- 17 Nameless Functions
- 17.1 Functions from lambda
- 17.2 Computing with lambda
- 17.3 Abstracting with lambda
- 17.4 Specifying with lambda
- 17.5 Representing with lambda
- 18 Summary
- Scope
- ISL for Loops
- Pattern Matching
- 19 The Poetry of S-expressions
- 19.1 Trees
- 19.2 Forests
- 19.3 S-expressions
- 19.4 Designing with Intertwined Data
- 19.5 Project: BSTs
- 19.6 Simplifying Functions
- 20 Iterative Refinement
- 20.1 Data Analysis
- 20.2 Refining Data Definitions
- 20.3 Refining Functions
- 21 Refining Interpreters
- 21.1 Interpreting Expressions
- 21.2 Interpreting Variables
- 21.3 Interpreting Functions
- 21.4 Interpreting Everything
- 22 Project: The Commerce of XML
- 22.1 XML as S-expressions
- 22.2 Rendering XML Enumerations
- 22.3 Domain-Specific Languages
- 22.4 Reading XML
- 23 Simultaneous Processing
- 23.1 Processing Two Lists Simultaneously: Case 1
- 23.2 Processing Two Lists Simultaneously: Case 2
- 23.3 Processing Two Lists Simultaneously: Case 3
- 23.4 Function Simplification
- 23.5 Designing Functions that Consume Two Complex Inputs
- 23.6 Finger Exercises: Two Inputs
- 23.7 Project: Database
- 24 Summary
- Fixed-Size Number Arithmetic
- Overflow
- Underflow
- *SL Numbers
- 25 Non-standard Recursion
- 25.1 Recursion without Structure
- 25.2 Recursion that Ignores Structure
- 26 Designing Algorithms
- 26.1 Adapting the Design Recipe
- 26.2 Termination
- 26.3 Structural versus Generative Recursion
- 26.4 Making Choices
- 27 Variations on the Theme
- 27.1 Fractals, a First Taste
- 27.2 Binary Search
- 27.3 A Glimpse at Parsing
- 28 Mathematical Examples
- 28.1 Newton’s Method
- 28.2 Numeric Integration
- 28.3 Project: Gaussian Elimination
- 29 Algorithms that Backtrack
- 29.1 Traversing Graphs
- 29.2 Project: Backtracking
- 30 Summary
- Concrete Time, Abstract Time
- The Definition of “On the Order Of”
- Why Do Programs Use Predicates and Selectors?
- 31 The Loss of Knowledge
- 31.1 A Problem with Structural Processing
- 31.2 A Problem with Generative Recursion
- 32 Designing Accumulator-Style Functions
- 32.1 Recognizing the Need for an Accumulator
- 32.2 Adding Accumulators
- 32.3 Transforming Functions into Accumulator Style
- 32.4 A Graphical Editor, with Mouse
- 33 More Uses of Accumulation
- 33.1 Accumulators and Trees
- 33.2 Data Representations with Accumulators
- 33.3 Accumulators as Results
- 34 Summary
- Computing
- Program Design
- Onward, Developers and Computer Scientists
- Onward, Accountants, Journalists, Surgeons, and Everyone Else
