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
    assert grouper.group(tokens) == expected


def test_grouper_extra(grouper):
    with pytest.raises(ValueError):
        grouper.group([
            Token('dollar', '$'),
        ])
