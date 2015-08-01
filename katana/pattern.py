from collections import deque
from katana.parser import State


class Pattern(object):
    def __init__(self, name, exprs):
        self.name = name
        self.exprs = tuple(exprs)


def resolve(patterns):
    initial = State(None, [])
    pats = {}
    for item in patterns:
        pats[item.name] = item.exprs

    states = {}
    q = deque(pats)
    while q:
        key = q.popleft()
        if key not in states:
            states[key] = State(key, [])
        state = states[key]

        # For each linked pattern in the chain, append the
        # corresponding state object to the current state,
        # else process this state later, when other states
        # are present/resolved.
        for name in pats[key]:
            if name in states:
                state.add(states[name])
                continue
            q.append(key)
            break

    initial.update(states[k] for k in states)
    return initial
