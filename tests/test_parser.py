import pytest
from katana.expr import Token
from katana.parser import group_tokens
from katana.trie import Trie


@pytest.fixture
def patterns():
    return Trie([
        ['dollar', 'number'],
        ['dollar', 'number', 'number'],
    ])


def test_group_tokens_simple(patterns):
    tokens = [
        Token('dollar', '$'),
        Token('number', '123'),
    ]
    groups, extra = group_tokens(tokens, patterns)
    assert not extra
    assert groups == [[t.name for t in tokens]]


def test_group_tokens_prefers_longest(patterns):
    tokens = [
        Token('dollar', '$'),
        Token('number', '123'),
        Token('number', '123'),
    ]
    groups, extra = group_tokens(tokens, patterns)
    assert not extra
    assert groups == [[t.name for t in tokens]]


def test_group_tokens_multiple(patterns):
    tokens = [
        Token('dollar', '$'),
        Token('number', '123'),
        Token('number', '123'),
        Token('dollar', '$'),
        Token('number', '123'),
    ]
    groups, extra = group_tokens(tokens, patterns)
    assert not extra
    assert groups == [
        ['dollar', 'number', 'number'],
        ['dollar', 'number'],
    ]
