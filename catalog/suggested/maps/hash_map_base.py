from random import randrange  # used to pick MAD parameters

from .map_base import MapBase


class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression.

    Keys must be hashable and non-None.
    """

    def __init__(self, cap=11, p=109345121):
        """Create an empty hash-table map.

        cap     initial table size (default 11)
        p       positive prime used for MAD (default 109345121)
        """
        self._table = cap * [None]
        self._n = 0  # number of entries in the map
        self._prime = p  # prime for MAD compression
        self._scale = 1 + randrange(p - 1)  # scale from 1 to p-1 for MAD
        self._shift = randrange(p)  # shift from 0 to p-1 for MAD

    def _hash_function(self, k):
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)  # may raise KeyError

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)  # subroutine maintains self._n
        if self._n > len(self._table) // 2:  # keep load factor <= 0.5
            self._resize(2 * len(self._table) - 1)  # number 2^x - 1 is often prime

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)  # may raise KeyError
        self._n -= 1

    def _resize(self, c):
        """Resize bucket array to capacity c and rehash all items."""
        old = list(self.items())  # use iteration to record existing items
        self._table = c * [None]  # then reset table to desired capacity
        self._n = 0  # n recomputed during subsequent adds
        for (k, v) in old:
            self[k] = v  # reinsert old key-value pair
