import pytest
from katana.expr import Expr, Scanner, Token


@pytest.fixture
def expr():
    return Expr('dollar', r'\$')


def test_on_match(expr):
    assert expr.on_match('t') == Token('dollar', 't')
    assert expr.on_match('$') == Token('dollar', '$')


@pytest.fixture
def scanner():
    return Scanner([
        Expr('dollar', r'\$'),
        Expr('number', r'[0-9]+'),
    ])


def test_scanner_match_full(scanner):
    assert scanner.match('123') == [Token('number', '123')]
    assert scanner.match('$123') == [
        Token('dollar', '$'),
        Token('number', '123'),
    ]


def test_scanner_match_partial(scanner):
    with pytest.raises(ValueError):
        scanner.match('abc')
