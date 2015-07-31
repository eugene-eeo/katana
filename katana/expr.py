import re


class Expr(object):
    def __init__(self, name, regex):
        self.name = name
        self.regex = re.compile(regex)

    def on_match(self, string):
        return [self.name, string]
