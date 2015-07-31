def group(tokens, patterns):
    tokens = list(tokens)
    max_idx = len(tokens) - 1
    b = []
    r = []
    for idx, d in enumerate(tokens):
        t, _ = d
        b.append(t)
        p = patterns.pos(b)
        if b not in p:
            continue

        if len(p) == 1 or idx == max_idx:
            r.append(b)
            b = []
            continue

        # if we have more tokens and using the next
        # token yields a more specific result then
        # we'll use it. This is to ensure that the
        # longer patterns do not get skipped.
        if max_idx >= (idx + 1):
            p2 = patterns.pos(b + [tokens[idx+1][0]])
            if p2 and len(p2) < len(p):
                continue
            if not p2:
                r.append(b)
                b = []
    return r, b
