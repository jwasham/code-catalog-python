def find_boyer_moore(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(T), len(P)  # introduce convenient notations
    if m == 0: return 0  # trivial search for empty string
    last = {}  # build 'last' dictionary
    for k in range(m):
        last[P[k]] = k  # later occurrence overwrites
    # align end of pattern at index m-1 of text
    i = m - 1  # an index into T
    k = m - 1  # an index into P
    while i < n:
        if T[i] == P[k]:  # a matching character
            if k == 0:
                return i  # pattern begins at index i of text
            else:
                i -= 1  # examine previous character
                k -= 1  # of both T and P
        else:
            j = last.get(T[i], -1)  # last(T[i]) is -1 if not found
            i += m - min(k, j + 1)  # case analysis for jump step
            k = m - 1  # restart at end of pattern
    return -1
