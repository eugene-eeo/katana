from pyrsistent import v as Vec
from katana.utils import prepare, parse, Pair


def test_prepare():
    given = ['k']
    after = Pair(Vec(), Vec(*given))
    assert prepare(given) == after
