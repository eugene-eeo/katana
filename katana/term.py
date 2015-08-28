from collections import namedtuple


Node = namedtuple('Node', ['term', 'data'])
Pair = namedtuple('Pair', ['nodes', 'tail'])


def prepare(seq):
    return Pair([], seq)


def term(token):
    def fn(pair):
        nodes, seq = pair
        head = seq[0]
        if head.term == token:
            tail = seq[1:]
            node = Node(fn, [head])
            return Pair(nodes + [node], tail)
        raise ValueError
    return fn


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
