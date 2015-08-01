from collections import deque


def longest(tree):
    if tree is None:
        return []
    r = []
    q = deque([([], tree)])
    while q:
        p, t = q.popleft()
        for k in t:
            if k is None:
                r.append(p)
                continue
            d = p + [k], t[k]
            q.append(d)
    return r


class Trie(object):
    def __init__(self, data=()):
        self.tree = {}
        for item in data:
            self.insert(item)

    def insert(self, seq):
        t = self.tree
        for k in seq:
            if k not in t:
                t[k] = {}
            t = t[k]
        t[None] = None

    def pos(self, seq):
        t = self.tree
        r = []
        b = []
        for item in seq:
            if item not in t:
                return r
            b.append(item)
            t = t[item]
        r.extend(b + k for k in longest(t))
        return r
