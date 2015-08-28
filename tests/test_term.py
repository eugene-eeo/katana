import pytest
from katana.storage import Node, Pair, prepare
from katana.term import term, null


@pytest.fixture
def kterm():
    return term('k')


def test_null():
    n = Node('k', 'data')
    given = prepare([n])
    after = given
    assert null(given) == after


def test_term(kterm):
    n = Node('k', 'data')
    given = prepare([n])
    after = Pair([n], [])
    assert kterm(given) == after


def test_term_multiple(kterm):
    n = Node('k', 'data')
    b = Node('b', 'data')
    given = prepare([n,b])
    after = Pair([n], [b])
    assert kterm(given) == after


def test_term_no_match(kterm):
    n = Node('g', 'data')
    given = prepare([n])
    with pytest.raises(ValueError):
        kterm(given)


def test_term_empty_seq(kterm):
    given = prepare([])
    with pytest.raises(ValueError):
        kterm(given)
