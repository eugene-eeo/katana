import pytest
from collections import deque
from katana.trie import Trie
from katana.expr import Pattern, Expr, Token, Repeat, Group
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


class TestRepeat:
    pattern = Repeat('monies', TestPattern.pattern)

    @pytest.fixture
    def ctx(self):
        return Context(
            tokens=deque([
                Group('usd', []),
                Group('usd', []),
            ]),
            buffer=[
                Group('usd', []),
            ]
        )

    def test_fit(self, ctx):
        assert self.pattern.fits(ctx)

    def test_callback(self, ctx):
        expected = Group(
            'monies',
            [Group('usd', [])] * 3,
        )
        assert self.pattern.callback(ctx) == expected
        assert not ctx.tokens
