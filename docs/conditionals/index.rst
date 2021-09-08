============
Conditionals
============


In python a simple conditional aka an if statement is written like this:

.. code-block:: python
  
  if 1 > 2:
    print("This will never run!")
  else:
    print("This will always run!")

In the above code I print a message under a certain condition, if 1 is bigger than 2.

In kotlin that would be:

.. code-block:: kotlin

  if (1 > 2) {
    println("This will never run!")
  } else {
    println("This will always run!")
  }

As you can see they are pretty darn similar.

I won't explain everything in detail since conditionals are the same in any language (only the operators may change).

Just keep in mind that in kotlin, you must explicitly use a boolean, be it from a comparison or a variable.
You can't pass it a number or empty string and expect it to detect if its ``true`` or ``false``


Oh yeah, to combine conditionals in kotlin we use ``&&`` for ``and`` and ``||`` for ``or``.

Negating a conditional is done with an exclamation mark, like this ``!true`` results in ``false``.
