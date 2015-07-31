import pytest
from katana.expr import Sequence, Expr


class TestSequence:
    expr = Sequence('money', [
        Expr('dollar', r'\$'),
        Expr('number', r'[0-9]+'),
    ])

    def test_match(self):
        expected = ['money', [['dollar', '$'], ['number', '12']]]
        assert self.expr.match('$12') == expected

    def test_not_all_exprs_matched(self):
        with pytest.raises(ValueError):
            self.expr.match('$')
