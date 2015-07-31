import pytest
from katana.grouping import group
from katana.trie import Trie


@pytest.fixture
def patterns():
    return Trie([
        ['dollar', 'number'],
        ['dollar', 'dollar', 'number'],
    ])


def test_group_simple(patterns):
    tokens = [
        ['dollar', '$'],
        ['number', '123'],
    ]
    groups, extra = group(tokens, patterns)
    assert not extra
    assert groups == [['dollar', 'number']]


def test_group_prefers_longest(patterns):
    tokens = [
        ['dollar', '$'],
        ['dollar', '$'],
        ['number', '123'],
    ]
    groups, extra = group(tokens, patterns)
    assert not extra
    assert groups == [['dollar', 'dollar', 'number']]


def test_group_multiple(patterns):
    tokens = [
        ['dollar', '$'],
        ['dollar', '$'],
        ['number', '123'],
        ['dollar', '$'],
        ['number', '123'],
    ]
    groups, extra = group(tokens, patterns)
    assert not extra
    assert groups == [
        ['dollar', 'dollar', 'number'],
        ['dollar', 'number'],
    ]
