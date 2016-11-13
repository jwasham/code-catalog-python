import random


def partition(vector, left, right, pivot_index):
    pivot_value = vector[pivot_index]
    # Move pivot to end
    vector[pivot_index], vector[right] = vector[right], vector[pivot_index]
    store_index = left
    for i in range(left, right):
        if vector[i] < pivot_value:
            vector[store_index], vector[i] = vector[i], vector[store_index]
            store_index += 1
    # Move pivot to its final place
    vector[right], vector[store_index] = vector[store_index], vector[right]
    return store_index


def _select(vector, left, right, k):
    """
    Returns the k-th smallest, (k >= 0), element of vector within
    vector[left:right+1] inclusive.
    """
    while True:
        # select pivot_index between left and right
        pivot_index = random.randint(left, right)
        pivot_new_index = partition(vector, left, right, pivot_index)
        pivot_dist = pivot_new_index - left
        if pivot_dist == k:
            return vector[pivot_new_index]
        elif k < pivot_dist:
            right = pivot_new_index - 1
        else:
            k -= pivot_dist + 1
            left = pivot_new_index + 1


def select(vector, k, left=None, right=None):
    """
    Returns the k-th smallest, (k >= 0), element of vector within vector[left:right+1].
    left, right default to (0, len(vector) - 1) if omitted
    """
    if left is None:
        left = 0
    lv1 = len(vector) - 1
    if right is None:
        right = lv1
    assert vector and k >= 0, "Either null vector or k < 0 "
    assert 0 <= left <= lv1, "left is out of range"
    assert left <= right <= lv1, "right is out of range"
    return _select(vector, left, right, k)


if __name__ == '__main__':
    v = [9, 8, 7, 6, 5, 0, 1, 2, 3, 4]
    print([select(v, i) for i in range(10)])
