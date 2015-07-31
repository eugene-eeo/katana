import pytest
from katana.expr import Expr


class TestExpr:
    expr = Expr('number', '[0-9]+')

    def test_match(self):
        assert self.expr.match('123') == ['number', '123']

    def test_match_partial(self):
        assert self.expr.match('12o') == ['number', '12']

    def test_match_nothing(self):
        with pytest.raises(ValueError):
            assert self.expr.match('abc')
