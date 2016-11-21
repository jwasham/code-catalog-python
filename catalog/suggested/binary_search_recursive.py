"""
Binary search, recursive
"""


def binary_search(data, target):
    return binary_search_recur(data, target, 0, len(data) - 1)


def binary_search_recur(data, target, low, high):
    """Return position if target is found in indicated portion of a Python list.

    The search only considers the portion from data[low] to data[high] inclusive.
    """
    if low > high:
        return False  # interval is empty; no match
    else:
        mid = (low + high) // 2
        if target == data[mid]:  # found a match
            return mid
        elif target < data[mid]:
            # recur on the portion left of the middle
            return binary_search_recur(data, target, low, mid - 1)
        else:
            # recur on the portion right of the middle
            return binary_search_recur(data, target, mid + 1, high)


def main():
    nums = [-1024, -681, -73, -24, 6, 7, 16, 22, 22,
            23, 25, 35, 56, 234, 235, 262, 897, 3463,
            9999, 9999, 10000]

    assert binary_search(nums, 16) == 6
    assert binary_search(nums, -1024) == 0
    assert binary_search(nums, 3463) == 17
    assert binary_search(nums, 56) == 12
    assert binary_search(nums, 498) is False
    assert binary_search(nums, 10001) is False
    assert binary_search(nums, 10000) == 20
    assert binary_search(nums, 9999) == 18


if __name__ == '__main__':
    main()
