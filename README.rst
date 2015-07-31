Katana
======

**Katana** - Razor sharp tokeniser written in Python.

.. code-block:: python

    >>> from katana.expr import Expr, Sequence
    >>> s = Sequence('money', [
    ...     Expr('dollar', r'\$'),
    ...     Expr('number', r'[0-9]+'),
    ... ])
    >>> s.match('$12')
    ['money', [['dollar', '$'], ['number', '12']]]
