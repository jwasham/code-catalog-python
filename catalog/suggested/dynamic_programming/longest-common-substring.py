"""
Longest common substring
"""


def longest_common_substring(s1, s2):
    m = [[0] * (1 + len(s2)) for _ in range(1 + len(s1))]

    longest, x_longest = 0, 0

    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0

    return s1[x_longest - longest: x_longest]


def main():
    assert longest_common_substring('my family', "I'm famous") == ' fam'
    assert longest_common_substring('hello world', "shell corp") == 'hell'
    assert longest_common_substring('just in time', "halifax") == 'i'
    assert longest_common_substring('abc', "xyz") == ''
    assert longest_common_substring('superman', 'wonder woman') == 'man'


if __name__ == '__main__':
    main()
