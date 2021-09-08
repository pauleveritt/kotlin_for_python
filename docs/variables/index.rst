===================
Variables and Types
===================

A read-only variable is written like so:

.. code-block:: kotlin

  val cat: String = "meow"

Kotlin is smart enough to infer the type of the variable in this case, so we can directly write:

.. code-block:: kotlin

  val cat = "meow"

Attempting to re-assign to a val will result in a compile error.

A normal variable is written like so:

.. code-block:: kotlin
  
  var cat = "meow"

Not re-assigning to a variable will make the compiler
scream at us for using a var when val could be used instead.


===================
TODO
===================

Class variables: properties and fields covered in classes

- Types on variables

- Basic types https://kotlinlang.org/docs/reference/basic-types.html#basic-types
