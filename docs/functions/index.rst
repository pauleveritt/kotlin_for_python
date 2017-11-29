=========
Functions
=========


Looking at the Kotlin code itself:

- This special ``main`` function has a contract...it's going to be
  passed an argument

- We see the first hint of typing. It's mandatory in Kotlin...sort of.
  In this case we have an array of strings. With Python 3.6 variable
  annotations for optional type hinting, this would be:

  .. literalinclude:: hello_world_typing.py
    :linenos:

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

Kotlin has another syntactic convenience: you aren't required to
say that the function returns nothing.

Function expressions


If using Python 3.5+ type hinting, that would be:

.. code-block:: python
    :linenos:

        def sum(a: int, b:int) -> int:
            return a + b


Not too shabby. This will be a recurring point: we'll compare Kotlin not
just with "normal" Python, but also against type-hinted-Python.
