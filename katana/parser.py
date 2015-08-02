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

        p0 = trie.pos(nb)
        if not p0:
            raise ValueError

        g0 = p[0]
        ok = g0.fits(tb)

        if len(p0) == 1 and ok:
            yield g0.callback(tb)
            tb = []
            nb = []
            continue

        if idx < max_idx:
            t1 = tokens[idx+1]
            t2 = trie.pos(nb + [t1.name])
            if not t2 and ok:
                yield g0.callback(tb)
                tb = []
                nb = []
                continue
    if nb:
        raise ValueError
