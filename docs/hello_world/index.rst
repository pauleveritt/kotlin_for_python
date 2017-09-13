===========
Hello World
===========

Java is installed, our IDE has a project open, we're ready to write some
code. In this step we breeze through a light treatment of many Kotlin
concepts, all from the Python perspective.

Python has a nice handy console/REPL that we can use to just evaluate some
lines. Kotlin does to. Let's start there.

The REPL
========

Opening the Kotlin REPL is easy:

[screenshot showing opening the REPL]

In Python we have the ``Python Console`` tool window, which opens the
Python interpreter, in the context of your project, with some IDE goodness
thrown in. The Kotlin REPL is the same idea.

Let's type in some code:

[screenshot of entering ``println("Hello World")``]

We can type in a line of code and evaluate it, letting Kotlin/Java do a
mountain of machinery behind the scenes. It's statetful as well:

[screenshot of entering ``val x = "Hello World"`` then ``println(msg)``]

This is our first foray into Kotlin. Let's analyze it from

Let's click the red X to close the REPL and start writing some Kotlin code.

First File
==========

In Python, we'd make a ``.py`` file and start typing in some code. From
Python's semantics, there are almost no rules about the file itself -- name,
location, etc.

We can start the same in Kotlin. Let's show this. IntelliJ has created a
``src`` directory for you. Right-click on that and create a file at
``hello_world.kt``:

.. literalinclude:: hello_world.kt

Q: Are there times when src/main/kotlin is important, e.g. Gradle?

- Do the sequence to show printing a line

- Explain the concepts involved



0) The REPL (perhaps start with it?)

1) def vs. fun

2) Importance of “def main” vs. __name__

3) K: required args to main()

4) K has mandatory typing on function args, P implicit & static
    - But both have a type system

5) K has optional return type when Unit (void)

6) print method is the same in both

7) Running: clicking arrow beside the function (but slower first time for Kotlin)

8) Kotlin does some magic behind-the-scenes creation of Java classes named from the file name, because Java needs classes

9) Comparison of “compilation” pipelines

10) Comment syntax

11) Variable definitions: var vs. val (immutable)

11a) …and compiler enforcement

12) Implications of typing when assigning/re-assigning

12a) …and compiler enforcement, vs. Python

13) Explicitly defining a type during declaration: the same

14) Re-assignin immutable via val causes compiler error

15) Calling functions and type checking
