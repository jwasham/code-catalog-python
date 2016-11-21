"""
An implementation of Boyer-Moore-Horspool string searching.
"""
from collections import defaultdict


def boyer_moore_horspool(pattern, text):
    m = len(pattern)
    n = len(text)

    if m > n:
        return -1

    skip = defaultdict(lambda: m)
    found_indexes = []

    for k in range(m - 1):
        skip[ord(pattern[k])] = m - k - 1

    k = m - 1

    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            found_indexes.append(i + 1)

        k += skip[ord(text[k])]

    return found_indexes


if __name__ == '__main__':

    tests = [
        [[8, 25], 'the', 'this is the string to do the search in'],
        [[0, 2, 10], 'co', 'cocochanelco'],
        [[2, 6], 'co', 'mycocacola'],
        [[2, 4, 6, 9], 'co', 'mycococoacola'],
        [[2, 4], 'coco', 'mycococoacola'],
        [[10], 'co', 'lalalalalaco'],
        [[0], 'co', 'colalalalala'],
        [[], 'a', 'zzzzzzzzzzz'],
        [[0], 'a', 'a'],
        [[], 'z', 'a'],
        [[], 'z', 'aa'],
        [[1], 'z', 'az'],
        [[0], 'z', 'za'],
        [[r for r in range(11)], 'z', 'zzzzzzzzzzz'],
        [[5, 6], 'z', 'aaaaazzaaaaa'],
    ]

    for test in tests:
        assert boyer_moore_horspool(test[1], test[2]) == test[0]
