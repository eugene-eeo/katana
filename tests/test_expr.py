import pytest
from katana.expr import Expr, Scanner


@pytest.fixture
def expr():
    return Expr('dollar', r'\$')


def test_on_match(expr):
    assert expr.on_match('t') == ['dollar', 't']
    assert expr.on_match('$') == ['dollar', '$']


@pytest.fixture
def scanner():
    return Scanner([
        Expr('dollar', r'\$'),
        Expr('number', r'[0-9]+'),
    ])


def test_scanner_match_full(scanner):
    assert scanner.match('$123') == [['dollar', '$'], ['number', '123']]
    assert scanner.match('123') == [['number', '123']]


def test_scanner_match_partial(scanner):
    with pytest.raises(ValueError):
        scanner.match('abc')
