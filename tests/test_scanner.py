import pytest
from katana.scanner import rexpr, scan
from katana.storage import Node


dollar = rexpr(r'\$')
number = rexpr(r'[0-9]+')


def test_rexpr():
    assert dollar[0] == r'\$'
    assert dollar[1](None, '$') == Node(dollar, '$')


def test_scan():
    assert scan([dollar], '$') == [Node(dollar, '$')]
    assert scan([dollar, number], '$123') == [
        Node(dollar, '$'),
        Node(number, '123'),
        ]


def test_scan_incomplete():
    with pytest.raises(ValueError):
        scan([dollar], '$1')
