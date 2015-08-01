from collections import namedtuple
from katana.trie import Trie
from katana.parser import group_tokens


Group = namedtuple('Group', 'name,tokens')


class ExprGroup(object):
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

    def get_group(self, tokens):
        names = tuple(t.name for t in tokens)
        group_name = self.index[names]
        return Group(
            group_name,
            tokens,
        )

    def group(self, tokens):
        for each in group_tokens(tokens, self.trie):
            yield self.get_group(each)
