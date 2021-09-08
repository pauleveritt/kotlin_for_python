=====================
Sequences and Looping
=====================

1) 1..5 vs. range(5) (and “a”..”z”)


2) 2 in range(5) (the in operator)

3) if else vs. if then

4) if “expressions”

.. code-block:: kotlin

    // kotlin
    var maxValue: Int = if (a > b) a else b

.. code-block:: python

    # python
    max_value = a if a > b else b

5) when (aka switch, available in python 3.10 and above)

.. code-block:: kotlin

    // kotlin
    when (x) {
        !in 1..20 -> println(“x is 1”)
        21,22 -> println(“x is 22 or 23”)
        else -> {
            // Some set of lines in a block
            println(“x is greater than 22”)
        }
    }

6) generators, iterators

In python, a simple generator is written like this:

.. code-block:: python

    # python
    def gen():
        for i in range(5):
            yield i

And you can iterate over it like a normal list but w/o a known index.

This can be replicated in kotlin like this:

.. code-block:: kotlin

    val gen = sequence<Int> {
        for (i in 0..4) {
            yield(i)
        }
    }

Beware: there is a huge difference between python's generators and kotlin's.
Python's generators are treated as an instance, whilst the kotlin ones are w/o a state.
What does that mean?
Iterating in a kotlin generator, then stopping the iteration and starting a new one doesn't continue where it left off.

To accomplice the behaviour we want (keeping a state) we have to save the iterator of that generator, and not the generator itself.

Example below:

.. code-block:: kotlin

    val gen = sequence<Int> {
        for (i in 0..4) {
            yield(i)
        }
    }
    val state = gen.iterator()

The ``state`` variable above can keep its state between different loops.

Another big difference is that kotlin's generators don't accept parameters.

But that is easily fixed by making a function that hosts that generator and returns its iterator, like so:

.. code-block:: kotlin

    fun gen(startingIndex: Int = 1, endingIndex: Int = 10): Iterator<Int> {
        return sequence {
            for (i in startingIndex until endingIndex) {
                yield(i)
            }
        }.iterator()
    }
voila!

The above function behaves exactly like a python generator!
