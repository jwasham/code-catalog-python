"""
Longest common subsequence
"""


def longest_common_subsequence(s1, s2):
    lengths = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(s1):
        for j, y in enumerate(s2):
            if x == y:
                lengths[i + 1][j + 1] = lengths[i][j] + 1
            else:
                lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])

    # read the substring out from the matrix
    result = []
    x, y = len(s1), len(s2)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x - 1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y - 1]:
            y -= 1
        else:
            assert s1[x - 1] == s2[y - 1]
            result.append(s1[x - 1])
            x -= 1
            y -= 1

    return ''.join(reversed(result))


def main():
    assert longest_common_subsequence('my family', "I'm famous") == 'm fam'
    assert longest_common_subsequence('hello world', "shell corp") == 'hell or'
    assert longest_common_subsequence('just in time, max', "halifax") == 'iax'
    assert longest_common_subsequence('abc', "xyz") == ''
    assert longest_common_subsequence('superman', 'wonder woman') == 'erman'


if __name__ == '__main__':
    main()
