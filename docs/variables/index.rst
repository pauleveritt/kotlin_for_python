===================
Variables and Types
===================

An immutable variable is written like so:

.. code-block:: kotlin

  val cat: String = "meow"

Kotlin is smart enough to infer the type of the variable in this case, so we can directly write:

.. code-block:: kotlin

  val cat = "meow"

Attempting to re-assign to a val will result in a compile error.

A mutable variable is written like so:

.. code-block:: kotlin
  
  var cat = "meow"

Not re-assigning to a variable will make the compiler
scream at us for using a var when val could be used instead.



Kotlin has a lot of types, but I won't bother to explain them all since they have the same concept.

A number can be in the type of a ``Byte``, a ``Short``, an ``Int``, a ``Float``, a ``Double`` or a ``Long``.

Of course there are more numeric types, but those are not "basic", in other words they are not types you will use often.

As for text, we have ``ByteArray``, ``CharArray``, ``String`` and ``Char``.

.. note::

  A ``ByteArray`` can be decoded using a charset to a string,
  but a ``ByteArray`` can contain things other than text.

Concerning sequences we have ``List``, ``ArrayList`` and ``MutableList``.

A ``List`` is immutable, whilst an ``ArrayList`` is mutable.
And as the name suggests ``MutableList`` is mutable as well.

The closest to python's list is ``ArrayList``.
And you can think of ``List`` as the closest to python's tuples.

Unlike almost any other language, lists in kotlin are not written using square brackets.

Instead you must initialise a list and optionally pass the items as parameters.
Or you can make a muttable list and push items in it.

example:

.. code-block:: kotlin

  listOf(1, 2, 3) // [1, 2, 3]
  
  val myList = mutableListOf()
  
  myList.add(1)
  myList.add(2)
  myList.add(3)
  
  println(myList) // [1, 2, 3]

Like any proper programming language kotlin has ``Boolean`` and they are written in lower case ``true``, ``false``.

Kotlin does have dictionaries, but they are called ``Map`` here.
A ``Map`` is immutable, so if you want to write to it you need to use a ``MutableMap``.

Sadly kotlin doesn't support writing a map in the traditional way, in other words using braces and colons.

Instead the syntax is:

.. code-block:: kotlin

  mapOf("key" to "value") // { "key": "value" }

But, you can still assign a value to a key using square brackets, like so:

.. code-block:: kotlin

  val myMap = mutableMapOf<String, String>()
  myMap["key"] = "value"

For more info on the basic types go to https://kotlinlang.org/docs/reference/basic-types.html#basic-types
