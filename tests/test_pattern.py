from collections import deque
from katana.trie import Trie
from katana.expr import Pattern, Expr, Token
from katana.parser import Context


class TestPattern:
    pattern = Pattern('usd', [
        Expr('dollar', r'\$'),
        Expr('number', r'[0-9]+'),
        ])

    def test_fit(self):
        ctx = Context(
            tokens=deque(),
            buffer=[
                Token('dollar', '$'),
                Token('number', '1'),
                ],
            )
        assert self.pattern.fits(ctx)

    def test_resolve(self):
        trie = Trie()
        self.pattern.resolve(trie)
        assert trie.pos(['dollar']) == [self.pattern]
        assert trie.pos(['dollar', 'number']) == [self.pattern]
