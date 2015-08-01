import pytest
from katana.expr import Token
from katana.group import Pattern, Group, Grouper


@pytest.fixture
def grouper():
    return Grouper([
        Pattern('usd', ['dollar', 'number'])
    ])


def test_grouper_group(grouper):
    tokens = [
        Token('dollar', '$'),
        Token('number', '1'),
    ]
    expected = [Group('usd', tokens)]
    assert list(grouper.group(tokens)) == expected


def test_grouper_get_group(grouper):
    tokens = [
        Token('dollar', '$'),
        Token('number', '1'),
    ]
    assert grouper.get_group(tokens) == Group('usd', tokens)


def test_grouper_extra(grouper):
    with pytest.raises(ValueError):
        list(grouper.group([
            Token('dollar', '$'),
        ]))
