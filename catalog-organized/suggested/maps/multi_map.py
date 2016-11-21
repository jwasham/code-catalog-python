class MultiMap:
    """
    A multimap class built upon use of an underlying map for storage.

    This uses dict for default storage.

    Subclasses can override class variable _MapType to change the default.
    That catalog class must have a default constructor that produces an empty map.
    As an example, one might define the following subclass to use a SortedTableMap

    class SortedTableMultimap(MultiMap):
      _MapType = SortedTableMap
    """
    _MapType = dict  # Map type; can be redefined by subclass

    def __init__(self):
        """Create a new empty multimap instance."""
        self._map = self._MapType()  # create map instance for storage
        self._n = 0

    def __len__(self):
        """Return number of (k,v) pairs in multimap."""
        return self._n

    def __iter__(self):
        """Iterate through all (k,v) pairs in multimap."""
        for k, secondary in self._map.items():
            for v in secondary:
                yield (k, v)

    def add(self, k, v):
        """Add pair (k,v) to multimap."""
        container = self._map.setdefault(k, [])  # create empty list, if needed
        container.append(v)
        self._n += 1

    def pop(self, k):
        """Remove and return arbitrary (k,v) pair with key k (or raise KeyError)."""
        secondary = self._map[k]  # may raise KeyError
        v = secondary.pop()
        if len(secondary) == 0:
            del self._map[k]  # no pairs left
        self._n -= 1
        return (k, v)

    def find(self, k):
        """Return arbitrary (k,v) pair with given key (or raise KeyError)."""
        secondary = self._map[k]  # may raise KeyError
        return (k, secondary[0])

    def find_all(self, k):
        """Generate iteration of all (k,v) pairs with given key."""
        secondary = self._map.get(k, [])  # empty list, by default
        for v in secondary:
            yield (k, v)
