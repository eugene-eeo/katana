import pytest
from katana.term import term, prepare, Pair, Node, sequence, group


def test_term():
    t = term('k')
    n = Node('k', 'data')
    given = Pair([], [n])
    after = Pair([n], [])
    assert t(given) == after


def test_term_no_match():
    t = term('k')
    n = Node('g', 'data')
    given = Pair([], [n])
    with pytest.raises(ValueError):
        t(given)


def test_prepare():
    given = ['k']
    after = Pair([], given)
    assert prepare(given) == after


def test_sequence():
    a = term('a')
    b = term('b')
    na = Node('a', 'data')
    nb = Node('b', 'data')
    s = sequence(a, b)

    given = Pair([], [na, nb])
    after = Pair([na, nb], [])
    assert s(given) == after


def test_group():
    a = term('a')
    n = Node('a', 'data')
    g = group(a)
    given = Pair([], [n])
    after = Pair([Node(g, a(given).nodes)], [])
    assert g(given) == after
