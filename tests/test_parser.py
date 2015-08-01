import pytest
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
        ['dollar', '$'],
        ['number', '123'],
    ]
    groups, extra = group_tokens(tokens, patterns)
    assert not extra
    assert groups == [['dollar', 'number']]


def test_group_tokens_prefers_longest(patterns):
    tokens = [
        ['dollar', '$'],
        ['number', '123'],
        ['number', '123'],
    ]
    groups, extra = group_tokens(tokens, patterns)
    assert not extra
    assert groups == [['dollar', 'number', 'number']]


def test_group_tokens_multiple(patterns):
    tokens = [
        ['dollar', '$'],
        ['number', '123'],
        ['number', '123'],
        ['dollar', '$'],
        ['number', '123'],
    ]
    groups, extra = group_tokens(tokens, patterns)
    assert not extra
    assert groups == [
        ['dollar', 'number', 'number'],
        ['dollar', 'number'],
    ]
