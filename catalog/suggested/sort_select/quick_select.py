import random


def quick_select(S, k):
    """Return the kth smallest element of list S, for k from 1 to len(S)."""
    if len(S) == 1:
        return S[0]
    pivot = random.choice(S)  # pick random pivot element from S
    L = [x for x in S if x < pivot]  # elements less than pivot
    E = [x for x in S if x == pivot]  # elements equal to pivot
    G = [x for x in S if pivot < x]  # elements greater than pivot
    if k <= len(L):
        return quick_select(L, k)  # kth smallest lies in L
    elif k <= len(L) + len(E):
        return pivot  # kth smallest equal to pivot
    else:
        j = k - len(L) - len(E)  # new selection parameter
        return quick_select(G, j)  # kth smallest is jth in G
