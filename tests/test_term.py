import pytest
from katana.storage import Node, Pair, prepare
from katana.term import term, sequence, group, repeat, option


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


def test_term_empty_seq():
    t = term('k')
    given = Pair([], [])
    with pytest.raises(ValueError):
        t(given)


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
    after = Pair([Node(g, [n])], [])
    assert g(given) == after


def test_repeat():
    a = term('a')
    n = Node('a', 'data')
    r = repeat(a)
    given = Pair([], [n]*10)
    after = Pair([n]*10, [])
    assert r(given) == after


def test_option():
    a = term('a')
    b = term('b')
    c = term('c')
    na = Node('a', 'data')
    nb = Node('b', 'data')
    nc = Node('c', 'data')
    opt = option(a, b, c)
    for item in [na, nb]:
        assert opt(prepare([item])) == Pair([item], [])


def test_option_empty():
    a = term('a')
    b = term('b')
    nc = Node('c', 'data')
    with pytest.raises(ValueError):
        assert option(a, b)(prepare([nc]))
