import re


class Expr(object):
    def __init__(self, name, regex):
        self.name = name
        self.regex = re.compile(regex)

    def match(self, string):
        m = self.regex.match(string)
        if not m:
            raise ValueError
        start, end = m.span()
        return [self.name, string[start:end]]


class Sequence(object):
    def __init__(self, name, exprs):
        self.name = name
        self.exprs = exprs

    def match(self, string):
        rv = []
        for expr in self.exprs:
            name, match = expr.match(string)
            rv.append([name, match])
            string = string[len(match):]
        return [self.name, rv]
