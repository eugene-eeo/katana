import re


class Expr(object):
    def __init__(self, name, regex):
        self.name = name
        self.regex = regex

    def __iter__(self):
        yield self.regex
        yield lambda _, token: self.on_match(token)

    def on_match(self, string):
        return [self.name, string]


class Scanner(object):
    def __init__(self, exprs):
        self.scanner = re.Scanner([
            tuple(e) for e in exprs
        ])

    def match(self, string):
        tokens, extra = self.scanner.scan(string)
        if extra:
            raise ValueError
        return tokens
