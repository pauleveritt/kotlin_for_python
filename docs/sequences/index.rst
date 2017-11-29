=====================
Sequences and Looping
=====================

1) 1..5 vs. range(5) (and “a”..”z”)

2) 2 in range(5) (the in operator)

3) if else vs. if then

4) if “expressions” (Python doesn’t have this) var maxValue:Int = if (a > b) a else b but multiple lines (only the last value is used in the block)

5) when (aka switch)…Python doesn’t have this::

    when (x) {
        !in 1..20 -> println(“x is 1”)
        21,22 -> println(“x is 22 or 23”)
        else -> {
            // Some set of lines in a block
            println(“x is greater than 22”)
        }
    }

6) etc.

generators, iterators
