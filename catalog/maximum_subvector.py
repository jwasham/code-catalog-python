"""
Compute the maximum subvector of an array of numbers
"""


def maximum_subvector(nums):
    max_so_far = 0
    max_ending_here = 0

    for n in nums:
        max_ending_here = max(max_ending_here + n, 0)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


def main():
    nums = [7, -4, 3, 5, -2, 1, 0, -12, 3, 5, -1, 4, -8]

    max_sub = maximum_subvector(nums)

    print("max: ", max_sub)

    assert max_sub == 11


if __name__ == '__main__':
    main()
