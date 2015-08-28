from collections import namedtuple
from pyrsistent import pvector


Node = namedtuple('Node', ['term', 'data'])
Pair = namedtuple('Pair', ['nodes', 'tail'])


def prepare(seq):
    return Pair(pvector(), seq)
