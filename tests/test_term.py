import pytest
from katana.utils import Node, Pair, prepare
from katana.term import term, null


K = term('k')
N = Node('k', 'data')
B = Node('b', 'data')


def test_null():
    given = prepare([N])
    after = given
    assert null(given) == after


def test_term():
    given = prepare([N])
    after = Pair([N], [])
    assert K(given) == after


def test_term_multiple():
    given = prepare([N,B])
    after = Pair([N], [B])
    assert K(given) == after


def test_term_no_match():
    given = prepare([B])
    with pytest.raises(ValueError):
        K(given)


def test_term_empty_seq():
    given = prepare([])
    with pytest.raises(ValueError):
        K(given)
