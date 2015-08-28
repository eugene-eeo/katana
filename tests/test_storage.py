from pyrsistent import v as Vec
from katana.storage import prepare, Pair


def test_prepare():
    given = ['k']
    after = Pair(Vec(), given)
    assert prepare(given) == after
