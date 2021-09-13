=======
Classes
=======

Classes in Kotlin are pretty straighforward, I would say more than Python's as well!

1) Defining a class with a method but no constructor

A simple class (w/o a constructor) can be written like this:

.. code-block:: kotlin

    class Example {
        
    }

To add methods to a class you simply have to write a function within that class!

Example of a class with a method:

.. code-block:: kotlin

    class Example {
        fun sayHi() {
            println("Hi there!")
        }
    }

By default any function/property in a class is public, that means that code outside the class can access the functions/properties of that class.
If we want to make a function be only accessible within the class we have to declare it as private.

.. code-block:: kotlin

    class Example {
        val greeting = "Hi there!"

        private fun sayHi() {
            println(greeting)
        }
    }

Now ``Example.sayHi`` is private, that means that that function is not accessible outside of the Example class.
Whilst ``Example.greeting`` is public, so its accessible outside of the class.

2) Creating instance of a class

To access that method, we have to initialise the class:

.. code-block:: kotlin

    val a = Example()
    a.sayHi()

3) Class variables access in Example via class name

In python to access a class property from within that class we use “self”.

In kotlin (from my understanding) there are two ways to access the class properties from within the class.

First one is to..well..just use the property names normally...that was too simple wasn't it?

Second one is to declare a companion object (its properties are private only) and either use the property names as usual, or use the class name in the same way we use “self” in python:

.. code-block:: kotlin

    class Example {
        companion object {
            val greeting = "Hi there!"
        }

        fun sayHi() {
            println(greeting) // or Example.greeting
        }
    }


4) Constructors && binding constructor arguments to instance attributes (assignment, usage)

A class with a constructor in python looks like:

.. code-block:: python

    class Example:
        def __init__(self, paramOne, paramTwo):
            self.paramOne = paramOne
            self.paramTwo = paramTwo

In the above case it sets as properties the two parameters it's given.

That can be done in kotlin like this:

.. code-block:: kotlin

    class Example(pOne: String, pTwo: String) {
        var paramOne = "placeholder"
        var paramTwo = "placeholder"

        init {
            paramOne = pOne
            paramTwo = pTwo
        }
        // if you know of a better way please PR this in
    }

We can then initialise it like this:

.. code-block:: kotlin

    val f = Example("hi", "there")
    println(f.paramOne)


5) Notes

.. note::

    ? - What happens if I don’t do var in the constructor? It’s unresolved later, but where does it go?


    In fact, Kotlin has a rich, multi-layered approach to construction.

    Our class attribute ``greeting`` is marked as immutable (and *should* be marked with the optional ``private``) as well.

    In some ways, Python is clunkier in this example.
    We have the magic of "dunder" names on important methods, such as the "constructor".

    The symbol of ``self`` is sprinkled in to give the instance scope a placeholder.

    And quite obviously, Kotlin's primary constructor -- right after the class name -- is terse and doesn't require assigning each value to "self".

.. note::

    Python's ``__init__`` is called a constructor, but as its name implies, it is actually an initializer.
    The ``__new__`` method is the factory, it is responsible for creating and returning a new instance for a class.

    Learn more about python's ``__new__`` `here <https://docs.python.org/3/reference/datamodel.html#object.__new__>`_.

More info at https://kotlinlang.org/docs/classes.html
