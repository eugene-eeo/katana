from katana.storage import Pair, Node, prepare


def term(token):
    def fn(pair):
        nodes, seq = pair
        if not seq:
            raise ValueError
        head = seq[0]
        if head.term == token:
            tail = seq[1:]
            return Pair(nodes + [head], tail)
        raise ValueError
    return fn


def sequence(*terms):
    def fn(pair):
        for each in terms:
            pair = each(pair)
        return pair
    return fn


def group(expr):
    def fn(pair):
        p2 = prepare(pair.tail)
        p2 = expr(p2)
        node = Node(fn, p2.nodes)
        return Pair(pair.nodes + [node], p2.tail)
    return fn


def repeat(expr):
    def fn(pair):
        while 1:
            try:
                pair = expr(pair)
            except ValueError:
                break
        return pair
    return fn
