def group_tokens(tokens, patterns):
    max_idx = len(tokens) - 1
    tb = []
    nb = []
    r = []
    for idx, t in enumerate(tokens):
        nb.append(t.name)
        tb.append(t)
        p = patterns.pos(nb)
        if nb not in p:
            continue

        if len(p) == 1 or idx == max_idx:
            yield tb
            nb = []
            tb = []
            continue

        # if we have more tokens and using the next
        # token yields a more specific result then
        # we'll use it. This is to ensure that the
        # longer patterns do not get skipped.
        if max_idx >= (idx + 1):
            n = tokens[idx+1].name
            p2 = patterns.pos(nb + [n])
            if p2 and len(p2) < len(p):
                continue
            if not p2:
                yield tb
                nb = []
                tb = []
    if nb:
        raise ValueError
