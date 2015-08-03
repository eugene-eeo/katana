from collections import namedtuple


Token = namedtuple('Token', 'name,data')
Group = namedtuple('Group', 'name,data')


class Expr(object):
    parent = None

    def __init__(self, name, regex, callback=None):
        self.name = name
        self.regex = regex
        self.callback = (callback or
                         (lambda _, token: Token(self.name, token)))

    def __iter__(self):
        yield self.regex
        yield self.callback


class Pattern(object):
    parent = None

    def __init__(self, name, exprs, callback=None):
        self.name = name
        self.exprs = tuple(exprs)
        for item in self.exprs:
            item.parent = self
        self.callback = (callback or
                         (lambda ctx: Group(self.name, ctx.buffer)))

    def fits(self, ctx):
        return ([g.name for g in self.exprs] ==
                [g.name for g in ctx.buffer])

    def resolve(self, trie):
        trie.insert([b.name for b in self.exprs], self)


class Repeat(Pattern):
    def __init__(self, name, expr):
        expr_name = expr.name
        def callback(ctx):
            buff = []
            while ctx.tokens:
                t = ctx.tokens.popleft()
                if t.name != expr_name:
                    ctx.tokens.appendleft(t)
                    break
                buff.append(t)
            return Group(name, ctx.buffer + buff)
        Pattern.__init__(
            self,
            name,
            [expr],
            callback
        )
