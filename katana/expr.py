from collections import namedtuple


Token = namedtuple('Token', 'name,data')
Group = namedtuple('Group', 'name,data')


class Expr(object):
    def __init__(self, name, regex, callback=None):
        self.name = name
        self.regex = regex
        if callback is None:
            callback = lambda _, token: Token(self.name, token)
        self.callback = callback

    def __iter__(self):
        yield self.regex
        yield self.callback


class Pattern(object):
    def __init__(self, name, exprs, callback=None):
        self.name = name
        self.exprs = tuple(exprs)
        if callback is None:
            callback = lambda ctx: Group(self.name, ctx.buffer)
        self.callback = callback

    def fits(self, ctx):
        return (self.exprs == tuple(t.name for t in ctx.buffer))
