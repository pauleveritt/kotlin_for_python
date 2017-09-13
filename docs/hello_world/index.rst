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

Python has an interactive interpreter, aka REPL, which makes it easy to
play around and learn. It's a dynamic language, so this makes sense. As
it turns out, Kotlin (in IntelliJ) has a REPL also.

Opening the Kotlin REPL is easy. You can use the ``Tools | Kotlin`` menu
or search for the action:

.. image:: REPL_open.png

In Python we have the ``Python Console`` tool window, which opens the
Python interpreter in the context of your project. The Kotlin REPL is
the same idea.

Let's type in some code:

.. image:: REPL.png

Here we typed a line of Kotlin code, then executed it with ``Cmd-Enter``.
Kotlin then evaluated it, letting Kotlin/Java do a mountain of machinery
behind the scenes.

The REPL is can handle multiple lines:

.. image:: REPL_state.png

As this is our first foray into Kotlin, let's analyze this small bit of
code from the Python perspective:

.. code-block:: kotlin

    val msg = "Hello Kotlin"
    print(msg)

- We declare variables with ``var`` (which allows re-assignment) or
  ``val`` (which is like a constant). Python doesn't have this. JavaScript
  ES6 and TypeScript do.

- Double quotes for strings, and yes, Kotlin has triple-quoted multiline
  strings

- No semicolons!

- A print function

All in all...looks a lot like Python.

Click the red X to close the REPL and let's start writing some Kotlin code.

.. raw:: html

  <iframe src="https://drive.google.com/file/d/0ByDKocMZdLZLeEZjVDd6MUVDckk/preview"
          width="640" height="480"
          style="margin-bottom: 2em"></iframe>


First File
==========

In Python, we'd make a ``.py`` file and start typing in some code. From
Python's semantics, there are almost no rules about the file itself -- name,
location, etc.

We can start the same in Kotlin. Let's show this. IntelliJ has created a
``src`` directory for you. Right-click on that and create a file at
``hello_world.kt``:

.. literalinclude:: hello_world.kt
    :language: kotlin

Here's the minimum Python file to mimic this functionality:

.. literalinclude:: hello_world_basic.py

The Kotlin file shows the standard Kotlin "entry point": by convention,
the file being executed must have a function named ``main`` which accepts
a single argument, an array of strings. This is a *bit* similar to the
common (but not required) Python run block. For example, this file in
Python might look like this:

.. literalinclude:: hello_world_main.py

Looking at the Kotlin code itself:

- Kotlin uses the ``fun`` keyword to define a function, whereas Python
  uses ``def``

- This special ``main`` function has a contract...it's going to be
  passed an argument

- We see the first hint of typing. It's mandatory in Kotlin...sort of.
  In this case we have an array of strings. With Python 3.6 variable
  annotations for optional type hinting, this would be:

  .. literalinclude:: hello_world_typing.py

- Whereas Python terminates the function line with a colon and uses
  indentation for the block, Kotlin uses the standard curly braces
  syntax

Python's weird ``if __name__`` block is ugly, and reveals a certain
something about packaging being added after-the-fact, but shows
that Python is ready to just let you do damn fool stupid stuff at
module scope. Like run your program. Kotlin has a bit of a formal
contract to meet when executing an "entry point".

.. note::

    Don't like typing the boilerplate? PyCharm has a Live
    Template ``main`` for generating the run block at the
    bottom. So does Kotlin. We'll show this in the video
    for this segment.

We saw strong typing at play in Kotlin. Python of course has
typing, but it is at run time, and is inferred. As we'll see later,
Kotlin lets you skip the syntax by inferring type information,
but it is still at compile time.

Kotlin has another syntactic convenience: you aren't required to
say that the function returns nothing.

Time to run this, which really means, compile and execute. If you're
familiar with PyCharm run configurations and gutter icons, it's
the same:

[screenshot of running it]

Next
====

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
