import numpy


def heap_sort(data):
    heapify(data)
    end = len(data) - 1

    while end > 0:
        data[end], data[0] = data[0], data[end]
        end -= 1
        sift_down(data, 0, end)


def heapify(data):
    length = len(data)

    for i in reversed(range(length // 2)):
        sift_down(data, i, length - 1)


# max-heap for heapsort
def sift_down(data, start, end):
    root = start

    while root * 2 + 1 <= end:
        child = root * 2 + 1
        if child + 1 <= end and data[child] < data[child + 1]:
            child += 1
        if data[root] < data[child]:
            data[root], data[child] = data[child], data[root]
            root = child
        else:
            return


def python_heap_sort(data):
    import heapq

    heap = list(data)

    # min-heap
    heapq.heapify(heap)

    for i in range(len(data)):
        data[i] = heapq.heappop(heap)


if __name__ == '__main__':
    nums = [13, 14, 94, -31, 33, 82, 25, 59,
            94, 65, 23, -1, 0, -146, 45, 27,
            73, 25, 39, 10]
    sort_nums = [-146, -31, -1, 0, 10, 13, 14,
                 23, 25, 25, 27, 33, 39, 45, 59,
                 65, 73, 82, 94, 94]

    # using custom

    copy1 = nums[:]

    heap_sort(copy1)
    print(copy1)
    assert numpy.allclose(copy1, sort_nums)

    # using standard library

    copy2 = nums[:]

    python_heap_sort(copy2)
    print(copy2)
    assert numpy.allclose(copy2, sort_nums)
