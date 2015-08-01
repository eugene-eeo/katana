from collections import namedtuple
from katana.trie import Trie
from katana.parser import group_tokens


Group = namedtuple('Group', 'name,tokens')


class Pattern(object):
    def __init__(self, name, exprs):
        self.name = name
        self.exprs = tuple(exprs)

    def __iter__(self):
        yield self.name
        yield self.exprs


class Grouper(object):
    def __init__(self, data):
        self.trie = Trie()
        self.index = {}
        for name, exprs in data:
            self.index[tuple(exprs)] = name
            self.trie.insert(exprs)

    def parse(self, tokens):
        r = []
        groups, _ = group_tokens(tokens, self.trie)
        for tokens in groups:
            names = tuple(t.name for t in tokens)
            group_name = self.index[names]
            r.append(Group(
                group_name,
                tokens,
                ))
        return r
