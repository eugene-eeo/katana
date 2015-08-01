import pytest
from katana.trie import Trie


@pytest.fixture
def trie():
    return Trie([
        '1',
        '12',
        '123',
        '1234',
    ])


def ls(*s):
    return [list(k) for k in s]


def test_trie_pos(trie):
    assert trie.pos('1') == ls('1', '12', '123', '1234')
    assert trie.pos('12') == ls('12', '123', '1234')
    assert trie.pos('123') == ls('123', '1234')
    assert trie.pos('1234') == ls('1234')


def test_trie_insert(trie):
    trie.insert('456')
    assert trie.pos('456') == ls('456')
