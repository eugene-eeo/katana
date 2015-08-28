from katana.storage import Pair


def null(pair):
    return pair


def term(token):
    def fn(pair):
        nodes, seq = pair
        if not seq:
            raise ValueError
        head = seq[0]
        if head.term == token:
            tail = seq[1:]
            return Pair(nodes + [head], tail)
        raise ValueError
    return fn
