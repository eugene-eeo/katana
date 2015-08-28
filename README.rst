Katana
======

A razor sharp, experimental parser-combinator library for Python.
It's goals include being composable, easy to understand, and elegant
while being reasonably performant. Katana is being built with a
functional style- immutable data structures, no mutation and
requires the pyrsistent_ library.

Katana requires a strict separation of the tokenisation and
parsing phase; tokenisation is done via regexes and parsing
is simply the grouping of those tokens:

.. code-block:: python

    from katana.scanner import rexpr, scan

    dollar = rexpr(r'\$')
    number = rexpr(r'[0-9]+')
    tokens = scan([dollar, number], '$123')

Then the parsing phase:

.. code-block:: python

    from katana.term import term
    from katana.term import sequence

    dollar_term = term(dollar)
    number_term = term(number)

    parser = sequence(dollar_term, number_term)
    parser(tokens)

.. _pyrsistent: https://github.com/tobgu/pyrsistent
