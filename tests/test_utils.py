import pytest
from pyrsistent import v as Vec
from katana.utils import prepare, parse, Pair, Node
from katana.term import term


def test_prepare():
    given = ['k']
    after = Pair(Vec(), Vec(*given))
    assert prepare(given) == after


def test_parse():
    node = Node('$', '123')
    given = [node]
    after = [node]
    assert parse(term('$'), given) == after


def test_parse_partial():
    node = Node('$', '123')
    given = [node, node]
    with pytest.raises(ValueError):
        parse(term('$'), given)
