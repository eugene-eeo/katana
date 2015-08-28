import pytest
from katana.storage import Node, Pair, prepare
from katana.compound import sequence, group, repeat, option, maybe
from katana.term import term


Ta = term('a')
Tb = term('b')
Tc = term('c')
Na = Node('a', 'data')
Nb = Node('b', 'data')
Nc = Node('c', 'data')


def test_sequence():
    s = sequence(Ta, Tb)

    given = prepare([Na, Nb])
    after = Pair([Na, Nb], [])
    assert s(given) == after


def test_group():
    g = group(Ta)
    given = prepare([Na])
    after = Pair([Node(g, [Na])], [])
    assert g(given) == after


def test_repeat():
    r = repeat(Ta)
    given = prepare([Na]*10)
    after = Pair([Na]*10, [])
    assert r(given) == after


def test_option():
    opt = option(Ta, Tb, Tc)
    for node in [Na, Nb]:
        assert opt(prepare([node])) == Pair([node], [])


def test_option_empty():
    with pytest.raises(ValueError):
        assert option(Ta, Tb)(prepare([Nc]))


def test_maybe():
    m = maybe(Ta)
    assert m(prepare([Nb])) == Pair([], [Nb])
    assert m(prepare([Na])) == Pair([Na], [])
