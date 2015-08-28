from re import Scanner
from collections import namedtuple
from katana.utils import Node


RExpr = namedtuple('RExpr', ['regex', 'callback'])


def rexpr(regex):
    def callback(scanner, token):
        return Node(r, token)
    r = RExpr(regex, callback)
    return r


def scan(rexprs, text):
    nodes, rest = Scanner(rexprs).scan(text)
    if rest:
        raise ValueError
    return nodes
