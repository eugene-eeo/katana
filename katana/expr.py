import re


class Expr(object):
    def __init__(self, name, regex):
        self.name = name
        self.regex = regex

    def on_match(self, string):
        return [self.name, string]

    def callback(self, _, string):
        return self.on_match(string)


class Scanner(object):
    def __init__(self, exprs):
        self.scanner = re.Scanner([
            (e.regex, e.callback) for e in exprs
        ])

    def match(self, string):
        tokens, extra = self.scanner.scan(string)
        if extra:
            raise ValueError
        return tokens
