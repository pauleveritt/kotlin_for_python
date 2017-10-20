===========
Hello World
===========

Java is installed, our IDE has a project open, we're ready to write some
code. In this step we breeze through a light treatment of many Kotlin
concepts, all from the Python perspective.

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

Here we typed a line of Kotlin code and executed it with ``Cmd-Enter``.
We could have clicked the green play button, which triggers the run action
just like ``Cmd-Enter``. Kotlin evaluated our line, letting Kotlin/Java do
a mountain of machinery behind the scenes.

The REPL can handle multiple lines:

.. image:: REPL_state.png

As this is our first foray into Kotlin, let's analyze this small bit of
code from the Python perspective:

.. code-block:: kotlin

    val msg = "Hello Kotlin"
    print(msg)

- We declare variables with ``var`` (which allows re-assignment) or
  ``val`` (which is like a constant). Python doesn't have ``var``. JavaScript
  ES6 and TypeScript do (``let`` and ``const``.)

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

We can start the same in Kotlin. IntelliJ has created a ``src`` directory
for you. Right-click on that and create a file at ``hello_world.kt``:

.. literalinclude:: ../../src/hello_world/hello_world.kt
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
module scope. For instance, run your program. Kotlin has a bit of a
formal contract to meet when executing an "entry point".

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
similar. Click the Kotlin symbol and select ``Run``:

[screenshot of running it]

.. note::

    IntelliJ prompted us to ``Run 'Hello_worldKT'``. What's
    ``Hello_worldKT``? Answer: To make Java happy, Kotlin generated
    a Java class behind the scenes.

When you clicked this, there was a lag that you don't get in Python.
This the build/compile phases from Java. It's incremental, so it
is faster after the first time.

Now that we've run our program, let's breeze through some
head-to-head comparisons on a few programming language basics.

Quotation Marks
===============

Switching between languages, or even projects, means swinging back
and forth between single versus double quotes for strings. For example,
TypeScript prefers double quotes, but ReactJS ES6 applications prefer
single quotes. And they are both (sort of) JavaScript!

Python's ``PEP 8`` style guide doesn't prefer one or the other, but
most Python projects seem to use single quotes. In fact, Python has
triple quoted strings!

.. code-block:: python

    hello = 'world'         # best
    hello = "world"         # ok
    hello = """
       world"""             # triple

Java (and Kotlin) use a single quote for a single character value and
double quotes for strings.

.. code-block:: kotlin

    val c = 'C'             // single
    val hello = "hello"     // double

Comments
========

Kotlin supports the two familiar styles of comments: end-of-line and
block comments:

.. code-block:: kotlin

    val hello = "world"     // Kotlin line comment
    /*
        Let's leave out
        these lines
    */

IntelliJ as an IDE makes it easy to comment and uncomment lines
and selections with ``Cmd-/``.

Python, of course, only has hashtag ``#`` as the comment symbol,
with no block comments:

.. code-block:: python

    #
    # Python multiline commments
    # have a lot of hashes.

    hello = 'world'  # Python comment

Variables
=========

Python doesn't have any special syntax for declaring a variable. You
just assign something:

.. code-block:: python

    hello = 'world'

Kotlin, though, does. In fact Kotlin has two keywords: one to declare
a read-only *immutable* variable, and one for a *mutable* variable:

.. code-block:: kotlin

    val hello = "world"     // Read-only
    var hello = "world"     // Can be re-assigned

Where's the Java-style type noise? Good news -- Kotlin can infer the type.
The above is the same as being explicit:

.. code-block:: kotlin

    val hello: String = "hello"

Also, like Python, you can initialize a variable without
assigning it:

.. code-block:: kotlin

    var hello

String Templates
================

Python -- the "there should be one way to do things" -- language,
has several ways to do string templates:

.. code-block:: python

    msg = 'World'
    print('Hello %s' % msg)                 # Original
    print('Hello {msg}'.format(msg=msg))    # Python 3 (then 2)
    print(f'Hello {msg}')                   # Python 3.6
    print(f'Hello {msg.upper()}')           # Expressions

Kotlin also has string templates with expressions:

.. code-block:: kotlin

    msg = "World"
    print("Hello $msg")
    print("Hello ${msg.toUpperCase()}")

Functions
=========

Python functions can be very simple:

.. code-block:: python

    def four():
        return 2 + 2

No curly braces, just indentation. Kotlin's simplest case is pretty close:

.. code-block:: kotlin

    fun four(): Int {
        return 2 + 2
    }

Kotlin adds the curly braces and has to define the return type (which can
be omitted if there is no return value.)

But watch this -- a function *expression*:

.. code-block:: kotlin

    fun four() = 2 + 2

Admit it, that's pretty sexy. Function expressions are a big new idea
which we'll cover later.

Passing in function arguments is straightforward in Python:

.. code-block:: python

    def combine(x, y):
        return x + y

If using Python 3.5+ type hinting, that would be:

.. code-block:: python

    def sum(a: int, b:int) -> int:
        return a + b

How does that compare to Kotlin?

.. code-block:: kotlin

    fun sum(a: Int, b: Int): Int {
        return a + b
    }

Not too shabby. This will be a recurring point: we'll compare Kotlin not
just with "normal" Python, but also against type-hinted-Python.

Control Sequences
=================

Let's take a quick look at things like conditionals and looping.  In
Python, an ``if/then/else`` is straightforward, with use of indentation:

.. code-block:: python

    if a > b:
        return a
    else:
        return b

Kotlin looks quite similar, adding parenthesis (optional in Python) and
braces:

.. code-block:: kotlin

    if (a > b) {
        return a
    } else {
        return b
    }

Let's compare looping over sequences. Simple Python example:

.. code-block:: python

    items = ('apple', 'banana', 'kiwi')
    for item in items:
        print(item)

In Kotlin, we have a different construct for making the sequence. Looping
is similar, though we use a parentheses after ``for``:

.. code-block:: kotlin

    val items = listOf("apple", "banana", "kiwi")
    for (item in items) {
        println(item)
    }

In this case we used ``println``. In Python, the ``print`` function always
makes a newline unless you ask it not to.

Both Python and Kotlin have rich and interesting control structures,
giving both power and terseness. We'll see more later.

Classes
=======

Lots to cover later on this, so for now, let's just view the simplest couple
of cases. The minimum in Python:

.. code-block:: python

    class Message:
        pass

In Kotlin:

.. code-block:: kotlin

    class Message

It's hard to tell which of those have the smaller conceptual density. And
who cares -- they're both tiny! Let's add a constructor, some variables,
and methods. First in Python:

.. code-block:: python

    class Message:
        greeting = 'Hello'

        def __init__(self, person):
            self.person = person

        def say_hello(self):
            return f'{self.greeting} {self.person}'

This class has a "constructor" with one argument, which is assigned as an
instance attribute. The class attribute of ``greeting`` is used in a
method ``say_hello`` which returns an evaluated f-string.

How about the type hinting flavor for Python 3.5+?

.. code-block:: python

    class Message:
        greeting = 'Hello'

        def __init__(self, person: str):
            self.person = person

        def say_hello(self) -> str:
            return f'{self.greeting} {self.person}'


Let's see this in Kotlin:

.. code-block:: kotlin

    class Message(val person: String) {
        val greeting = "Hello"

        fun sayHello(): String {
            return "$greeting $person"
        }
    }

That constructor syntax, right in the middle of the class name line, is
unusual and cool. In fact, Kotlin has a rich, multi-layered approach to
construction. Our class attribute ``greeting`` is marked as immutable
(and *should* be marked with the optional ``private``) as well.

In some ways, Python is clunkier in this example. We have the magic of
"dunder" names on important methods, such as the "constructor". The symbol
of ``self`` is sprinkled in to give the instance scope a placeholder. And
quite obviously, Kotlin's primary constructor -- right after the class
name -- is terse and doesn't require assigning each value to "self".

.. note::

    Python's ``__init__`` is called a constructor, but as its name implies,
    it is actually an initializer. The ``__new__`` method is the factory.
