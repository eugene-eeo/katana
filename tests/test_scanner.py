import pytest
from katana.expr import Expr, Token
from katana.parser import Scanner


class TestScanner:
    scanner = Scanner([
        Expr('dollar', r'\$'),
        Expr('number', r'[0-9]+'),
    ])

    def test_scan_complete(self):
        assert self.scanner.scan('$12') == [
            Token('dollar', '$'),
            Token('number', '12'),
        ]

    def test_scan_incomplete(self):
        with pytest.raises(ValueError):
            self.scanner.scan('12#')
