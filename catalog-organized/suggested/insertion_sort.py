def insertion_sort(A):
    """Sort list of comparable elements into non-decreasing order."""
    for i in range(1, len(A)):  # from 1 to n-1
        cur = A[i]  # current element to be inserted
        j = i  # find correct index j for current
        while j > 0 and A[j - 1] > cur:  # element A[j-1] must be after current
            A[j] = A[j - 1]
            j -= 1
        A[j] = cur  # cur is now in the right place


"""
Tests
"""

from random import shuffle

ex1 = [-5, -2.3, 0, 1, 1, 5, 6, 6.5, 7, 12]
shuffle(ex1)
insertion_sort(ex1)
assert ex1 == [-5, -2.3, 0, 1, 1, 5, 6, 6.5, 7, 12]
