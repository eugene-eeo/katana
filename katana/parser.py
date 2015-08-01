class State(object):
    def __init__(self, name, states):
        self.name = name
        self.states = {}
        self.update(states)

    def check(self, group):
        if group.name in self.states:
            return self.states[group.name]
        raise ValueError

    def update(self, states):
        for item in states:
            self.add(item)

    def add(self, state):
        self.states[state.name] = state


def parse_groups(groups, state):
    p = []
    for group in groups:
        state = state.check(group)
        p.append([state, group])
    return p
