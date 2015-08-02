import re
from collections import deque, namedtuple


class Scanner(object):
    def __init__(self, exprs):
        self.scanner = re.Scanner([
            tuple(e) for e in exprs
        ])

    def scan(self, string):
        tokens, extra = self.scanner.scan(string)
        if extra:
            raise ValueError
        return tokens


Context = namedtuple('Context', 'tokens,buffer')


def parse(tokens, trie):
    nb = []
    tb = []
    tokens = deque(tokens)

    while tokens:
        t = tokens.popleft()
        nb.append(t.name)
        tb.append(t)

        p1 = trie.pos(nb)
        if not p1:
            raise ValueError

        g1 = p1[0]
        ctx = Context(tokens, tb)

        if not g1.fits(ctx):
            continue

        if len(p1) == 1 or not tokens:
            yield g1.callback(ctx)
            tb = []
            nb = []
            continue

        t2 = tokens[idx+1]
        p2 = trie.pos(nb + [t2.name])
        if p2 and len(p2) < len(p1):
            continue
        if not p2:
            yield g1.callback(ctx)
            tb = []
            nb = []
    if nb:
        raise ValueError
