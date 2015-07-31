import pytest
from katana.expr import Expr


@pytest.fixture
def expr():
    return Expr('dollar', r'\$')


def test_on_match(expr):
    assert expr.on_match('t') == ['dollar', 't']
    assert expr.on_match('$') == ['dollar', '$']
