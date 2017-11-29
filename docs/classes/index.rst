=======
Classes
=======


1) Defining a class with a method but no constructor, P has “self”

2) Creating instance of class does NOT require new in either

3) Class variables access in P via self or class name

4) P can assign instance attributes whenever it wants (within __ limitations), change types whenever, no concept of public/private

5) Constructors

6) Binding of constructor arguments to instance attributes (assignment, usage)

    ? - What happens if I don’t do var in the constructor? It’s unresolved later, but where does it go?


In fact, Kotlin has a rich, multi-layered approach to
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

8) Kotlin does some magic behind-the-scenes creation of Java classes
   named from the file name, because Java needs classes

