class UnionFind:
    def __init__(self, n):
        self._id = list(range(n))
        self._sz = [1] * n

    def _root(self, i):
        j = i
        while j != self._id[j]:
            # compressing path
            self._id[j] = self._id[self._id[j]]
            j = self._id[j]
        return j

    def find(self, p, q):
        return self._root(p) == self._root(q)

    def union(self, p, q):
        i = self._root(p)
        j = self._root(q)
        # merge smaller into larger
        if self._sz[i] < self._sz[j]:
            self._id[i] = j
            self._sz[j] += self._sz[i]
        else:
            self._id[j] = i
            self._sz[i] += self._sz[j]

    def get_roots(self):
        for root in self._id:
            yield root


def main():
    uf = UnionFind(10)
    for (p, q) in [(3, 4), (4, 9), (8, 0), (2, 3)]:
        uf.union(p, q)

    assert uf.get_roots() == [0, 1, 3, 3, 3, 5, 6, 7, 0, 3]

    for (p, q) in [(5, 6), (5, 9), (7, 3)]:
        uf.union(p, q)

    assert uf.get_roots() == [0, 1, 3, 3, 3, 3, 5, 3, 0, 3]

    for (p, q) in [(4, 8), (6, 1)]:
        uf.union(p, q)

    assert uf.get_roots() == [8, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert uf.find(0, 1) is True
    assert uf.get_roots() == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
