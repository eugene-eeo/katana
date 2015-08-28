from collections import namedtuple


Node = namedtuple('Node', ['term', 'data'])
Pair = namedtuple('Pair', ['nodes', 'tail'])


def prepare(seq):
    return Pair([], seq)
