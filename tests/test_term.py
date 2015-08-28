import pytest
from katana.storage import Node, Pair, prepare
from katana.term import term, null


def test_null():
    t = null()
    n = Node('k', 'data')
    given = prepare([n])
    after = given
    assert t(given) == after


def test_term():
    t = term('k')
    n = Node('k', 'data')
    given = prepare([n])
    after = Pair([n], [])
    assert t(given) == after


def test_term_no_match():
    t = term('k')
    n = Node('g', 'data')
    given = prepare([n])
    with pytest.raises(ValueError):
        t(given)


def test_term_empty_seq():
    t = term('k')
    given = prepare([])
    with pytest.raises(ValueError):
        t(given)
