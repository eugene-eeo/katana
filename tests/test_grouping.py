import pytest
from katana.grouping import group
from katana.trie import Trie


@pytest.fixture
def patterns():
    return Trie([
        'abc',
        'def',
        'abcdef',
    ])


def test_group_simple(patterns):
    assert group('abc', patterns) == ([list('abc')], [])
    assert group('def', patterns) == ([list('def')], [])


def test_group_prefers_longest(patterns):
    groups, extra = group(
        'abcdef',
        patterns,
    )
    assert not extra
    assert groups == [list('abcdef')]


def test_group_multiple(patterns):
    groups, extra = group(
        'defabcabcdefabc',
        patterns,
    )
    expected = [list('def'), list('abc'),
                list('abcdef'), list('abc')]
    assert not extra
    assert groups == expected
