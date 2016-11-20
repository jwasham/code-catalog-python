class Node:
    """Lightweight, non-public class for storing a doubly linked node."""

    __slots__ = _element, _prev, _next  # streamline memory

    def __init__(self, element, prev, next):  # initialize node’s fields
        self._element = element  # user’s element
        self._prev = prev  # previous node reference
        self._next = next  # next node reference
