# coding: utf-8

# In[ ]:

from pprint import pprint


##
# Compute and return the original string, the sorted
# suffixes, and the actual suffix array --- in that order.
##
def suffixArray(T):
    sufInds = sorted([(T[i:], i) for i in range(len(T))])
    return T, [si[0] for si in sufInds], [si[1] for si in sufInds]


##
# Is the string lhs <= the string rhs up to and including
# the p-th character.
##
def lessEqP(lhs, rhs, p):
    i = 0
    while i < p and lhs[i] == rhs[i]:
        i += 1
    if i == p:
        return True
    else:
        return lhs[i] < rhs[i]


##
# This class represents an LCP value.  It's mainly a class
# because that's the only real way to get reference semantics
# in Python.  If it was just a number, then we couldn't modify
# it when passing it into a function. You wouldn't need this
# hack in a language like C/C++.
##
class LCP(object):
    def __init__(self, length=0, name='var'):
        self.name = name
        self.val = length

    @property
    def length(self):
        return self.val

    @length.setter
    def length(self, value):
        self.val = value


##
# Test if lhs <= rhs up to and inclusing the p-th character
# but also fill in the LCP of these strings based on our
# comparisons.
##
def lessEqPLCP(lhs, rhs, p, lcp):
    i = lcp.length
    while i < p and lhs[i] == rhs[i]:
        i += 1
    if i == p:
        lcp.length = p
        return True
    else:
        lcp.length = max(0, i - 1)
        return lhs[i] < rhs[i]


##
# Following 3 functions are from
# http://nbviewer.ipython.org/github/BenLangmead/comp-genomics-class/blob/master/notebooks/CG_LCP_from_LCP1.ipynb
##
# Simple function calculating LCP of two string
def calcLCP(x, y):
    for i in range(min(len(x), len(y))):
        if x[i] != y[i]: return i
    return min(len(x), len(y))


# Naive way to calculate LCP1 array given string and its suffix array
def naiveLCP1(t, sa):
    return [calcLCP(t[sa[i]:], t[sa[i + 1]:]) for i in range(len(sa) - 1)]


# Calculates (l, c) LCPs and (c, r) LCPs from LCP1 array.  Returns pair where
# first element is list of LCPs for (l, c) combos and second is LCPs for
# (c, r) combos. This function
def precomputeLCPS(lcp1):
    llcp, rlcp = [None] * len(lcp1), [None] * len(lcp1)
    lcp1 += [0]

    def precomputeLcpsHelper(l, r):
        if l == r - 1: return lcp1[l]
        c = (l + r) // 2
        llcp[c - 1] = precomputeLcpsHelper(l, c)
        rlcp[c - 1] = precomputeLcpsHelper(c, r)
        return min(llcp[c - 1], rlcp[c - 1])

    precomputeLcpsHelper(0, len(lcp1))
    return llcp, rlcp


#
# An implementation of the worst-case O(N + log M) for pattern search
# in a suffix array.  This algorithm is based off of the presentation in
# "SUFFIX ARRAYS: A NEW METHOD FOR ON-LINE STRING SEARCHES" by Manber & Meyers
#
def superAccelerantSearch(SA, T, W, verbose=True):
    print("===Accelerated Search===\n")
    # length of the pattern
    p = len(W)
    # length of the text AND suffix array
    N = len(T)

    # l is |LCP(W, T_SA[0])|
    l = LCP(calcLCP(W, T[SA[0]:]), 'l')
    # r is |LCP(W, T_SA[N-1])|
    r = LCP(calcLCP(W, T[SA[N - 1]:]), 'r')
    # the LCP arrays we need for efficient search
    LCP1 = naiveLCP1(T, SA)
    LCP_LM, LCP_MR = precomputeLCPS(LCP1)
    if verbose:
        print("LCP1 = [{}]".format(','.join([str(e) for e in LCP1])))
        print("LCP_LM = [{}]".format(','.join([str(e) for e in LCP_LM])))
        print("LCP_MR = [{}]".format(','.join([str(e) for e in LCP_MR])))
    # If l is the entire pattern, OR
    # the suffix is shorter than the pattern but the
    # last character of the pattern is less
    if l.length == p or (len(T[SA[0]:]) > p and W[l.length] <= T[SA[0] + l.length]):
        LW = 0
    elif r.length < p and W[r.length] > T[SA[N - 1] + r.length]:
        LW = N
    else:
        L, R = 0, N
        while R - L > 1:
            M = (L + R) // 2
            if verbose: print("L = {}, R = {} => M = {}".format(L, R, M))
            if l.length >= r.length:
                if verbose: print("(l = {}) >= (r = {}), so we're using LCP_LM".format(l.length, r.length))
                if LCP_LM[M] >= l.length:
                    if verbose:
                        print("\t(calcLCP(T[SA[M]:],T[SA[L]:]) = {}) >= (l = {})".format(
                            LCP_LM[M - 1], l.length))
                    m = l.length + calcLCP(W[l.length:], T[SA[M] + l.length:])
                    print("\tmatched = {}".format(m))
                else:

                    print("\t(LCP_LM[M-1] = {}) < (l = {})".format(
                        LCP_LM[M - 1], T[SA[L]:]), l.length)
                    m = LCP_LM[M - 1]
                    print("\tmatched = {}".format(m))
            else:
                print("(l = {}) < (r = {}), so we're using LCP_MR".format(
                    l.length, r.length))
                if LCP_MR[M - 1] >= r.length:
                    print("\t(LCP_MR[M-1] = {}) >= (r = {})".format(
                        LCP_MR[M - 1], r.length))
                    m = r.length + calcLCP(W[r.length:], T[SA[M] + r.length:])
                    print("\tmatched = {}".format(m))
                else:
                    print("\t(LCP_MR[M-1] = {}) < (r = {})".format(
                        LCP_MR[M - 1], r.length))
                    m = LCP_MR[M - 1]
                    print("\tmatched = {}".format(m))
            if m == p or (len(T[SA[M]:]) > m and W[m] <= T[SA[M] + m]):
                R = M
                r.length = m
                print("Updating R <- (M={}) and r <- (matches={})".format(M, m))
            else:
                L = M
                l.length = m
                print("Updating L <- (M={}) and l <- (matches={})".format(M, m))
        LW = R

    print("===End Accelerated Search===\n")
    return LW


#
# Naive binary search in a suffix array --- O(N * log M) to find
# a pattern.
#
def naiveSearch(SA, T, W):
    print("===Naive Search===\n")
    p = len(W)
    N = len(T)
    if lessEqP(W, T[SA[0]:], p):
        LW = 0
    elif not lessEqP(W, T[SA[N - 1]:], p):
        LW = N
    else:
        L, R = 0, N - 1
        while R - L > 1:
            M = (L + R) // 2
            print("M = {}".format(M))
            if lessEqP(W, T[SA[M]:], p):
                R = M
                print("R = {}".format(R))

            else:
                L = M
                print("L = {}".format(L))

        LW = R
    print("===End Naive Search===\n")
    return LW


# def main():
#     T = 'abracadabra'
#     suffs, sa = suffixArray(T)
#     from pprint import pprint
#     pprint(suffs)
#     pprint(sa)


def main():
    print("Testing suffix array search")
    T = 'abracadabracada$'
    T, suffs, sa = suffixArray(T)
    print("T = {}".format(T))
    print("sorted suffixes of T = {}".format(", ".join(suffs)))
    print("suffix array of T = {}".format(", ".join([str(i) for i in sa])))

    s = ['cada', 'braa', 'abr']
    for P in s:
        print("Searching for position for '{}'".format(P))
        nr = naiveSearch(sa, T, P)
        ar = superAccelerantSearch(sa, T, P)

        assert (nr == ar)
        print("\n")
        print("naive search gives {}".format(nr))
        print("accelerated search gives {}".format(ar))


if __name__ == "__main__":
    main()
