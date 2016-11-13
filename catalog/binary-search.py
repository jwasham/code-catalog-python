"""
Binary search
"""


def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def main():
    nums = [-1024, -681, -73, -24, 6, 7, 16, 22, 22,
            23, 25, 35, 56, 234, 235, 262, 897, 3463,
            9999, 9999, 10000]

    assert binary_search(nums, 16) == 6
    assert binary_search(nums, -1024) == 0
    assert binary_search(nums, 3463) == 17
    assert binary_search(nums, 56) == 12
    assert binary_search(nums, 498) == -1
    assert binary_search(nums, 10001) == -1
    assert binary_search(nums, 10000) == 20
    assert binary_search(nums, 9999) == 18


if __name__ == '__main__':
    main()
