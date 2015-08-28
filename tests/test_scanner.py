import pytest
from katana.scanner import rexpr, scan
from katana.storage import Node


@pytest.fixture
def dollar():
    return rexpr('dollar', r'\$')


@pytest.fixture
def number():
    return rexpr('number', r'[0-9]+')


def test_rexpr(dollar):
    assert dollar[0] == r'\$'
    assert dollar[1](None, '$') == Node('dollar', '$')


def test_scan(dollar, number):
    assert scan([dollar], '$') == [Node('dollar', '$')]
    assert scan([dollar, number], '$123') == [
        Node('dollar', '$'),
        Node('number', '123'),
        ]


def test_scan_incomplete(dollar):
    with pytest.raises(ValueError):
        scan([dollar], '$1')
