import re
from katana.trie import Trie


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


def parse(tokens, trie):
    nb = []
    tb = []
    tokens = list(tokens)
    max_idx = len(tokens) - 1

    for idx, t in enumerate(tokens):
        nb.append(t.name)
        tb.append(t)

        p1 = trie.pos(nb)
        if not p1:
            raise ValueError

        g1 = p1[0]

        if not g1.fits(tb):
            continue

        if len(p1) == 1 or max_idx == idx:
            yield g1.callback(tb)
            tb = []
            nb = []
            continue

        t2 = tokens[idx+1]
        p2 = trie.pos(nb + [t2.name])
        if p2 and len(p2) < len(p1):
            continue
        if not p2:
            yield g1.callback(tb)
            tb = []
            nb = []
    if nb:
        raise ValueError
