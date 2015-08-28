from katana.storage import Node, Pair, prepare
from katana.term import term, null


def sequence(*terms):
    def fn(pair):
        for each in terms:
            pair = each(pair)
        return pair
    return fn


def group(expr):
    def fn(pair):
        p2 = prepare(pair.tail)
        p2 = expr(p2)
        node = Node(fn, p2.nodes)
        return Pair(pair.nodes + [node], p2.tail)
    return fn


def repeat(expr):
    def fn(pair):
        while 1:
            try:
                pair = expr(pair)
            except ValueError:
                break
        return pair
    return fn


def option(*choices):
    def fn(pair):
        for item in choices:
            try:
                return item(pair)
            except ValueError:
                pass
        raise ValueError
    return fn


def maybe(expr):
    return option(expr, null())
