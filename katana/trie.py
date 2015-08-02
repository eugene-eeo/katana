from collections import deque


def longest(tree):
    if tree is None:
        return
    q = deque([([], tree)])
    while q:
        p, t = q.popleft()
        for k in t:
            if k is None:
                yield t[k]
                continue
            d = p + [k], t[k]
            q.append(d)


class Trie(object):
    def __init__(self, data=()):
        self.tree = {}
        for item in data:
            self.insert(item, item)

    def insert(self, seq, end=None):
        t = self.tree
        for k in seq:
            if k not in t:
                t[k] = {}
            t = t[k]
        t[None] = end

    def pos(self, seq):
        t = self.tree
        r = []
        b = []
        for item in seq:
            if item not in t:
                return r
            b.append(item)
            t = t[item]
        r.extend(longest(t))
        return r
