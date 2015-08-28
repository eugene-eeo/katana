from collections import namedtuple
from pyrsistent import pvector


Node = namedtuple('Node', ['term', 'data'])
Pair = namedtuple('Pair', ['nodes', 'tail'])


def prepare(seq):
    return Pair(pvector(), pvector(seq))


def parse(expr, tokens):
    nodes, tail = expr(prepare(tokens))
    if tail:
        raise ValueError
    return nodes
