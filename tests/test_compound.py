import pytest
from katana.storage import Node, Pair, prepare
from katana.compound import sequence, group, repeat, option, maybe
from katana.term import term


A = term('a')
B = term('b')
C = term('c')
node = lambda x: Node(x, 'data')


def test_sequence():
    na = node('a')
    nb = node('b')
    s = sequence(A, B)

    given = prepare([na, nb])
    after = Pair([na, nb], [])
    assert s(given) == after


def test_group():
    n = node('a')
    g = group(A)
    given = prepare([n])
    after = Pair([Node(g, [n])], [])
    assert g(given) == after


def test_repeat():
    n = node('a')
    r = repeat(A)
    given = prepare([n]*10)
    after = Pair([n]*10, [])
    assert r(given) == after


def test_option():
    a = node('a')
    b = node('b')
    c = node('c')
    opt = option(A, B, C)
    for item in [a, b]:
        assert opt(prepare([item])) == Pair([item], [])


def test_option_empty():
    c = node('c')
    with pytest.raises(ValueError):
        assert option(A, B)(prepare([c]))


def test_maybe():
    m = maybe(A)
    a = node('a')
    b = node('b')
    assert m(prepare([b])) == Pair([], [b])
    assert m(prepare([a])) == Pair([a], [])
