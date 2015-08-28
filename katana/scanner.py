from re import Scanner
from collections import namedtuple
from katana.storage import Node


RExpr = namedtuple('RExpr', ['regex', 'callback'])


def rexpr(name, regex):
    def callback(scanner, token):
        return Node(name, token)
    return RExpr(regex, callback)


def scan(rexprs, text):
    nodes, rest = Scanner(rexprs).scan(text)
    if rest:
        raise ValueError
    return nodes
