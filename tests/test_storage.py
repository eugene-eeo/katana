from katana.storage import prepare, Pair


def test_prepare():
    given = ['k']
    after = Pair([], given)
    assert prepare(given) == after
