"""
Calculates the edit distance in 2 strings
"""


def get_edit_distance(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    distances = [[0] * (len1 + 1) for _ in range(len2 + 1)]

    edit_distance = get_edit_distance_util(str1, str2, distances, len1, len2)

    return edit_distance


def get_edit_distance_util(str1, str2, distances, len1, len2):
    for i in range(1, len2 + 1):
        distances[i][0] = i

    for j in range(1, len1 + 1):
        distances[0][j] = j

    for i in range(1, len2 + 1):
        for j in range(1, len1 + 1):
            if str1[j - 1] == str2[i - 1]:
                distances[i][j] = distances[i - 1][j - 1]
            else:
                deletion = distances[i][j - 1] + 1
                insertion = distances[i - 1][j] + 1
                substitution = distances[i - 1][j - 1] + 1
                distances[i][j] = min(deletion, insertion, substitution)

    return distances[len2][len1]


def main():
    assert get_edit_distance("abc", "abcd") == 1
    assert get_edit_distance("abc", "abc") == 0
    assert get_edit_distance("", "") == 0
    assert get_edit_distance("", "a") == 1
    assert get_edit_distance("", "abcde") == 5
    assert get_edit_distance("a", "") == 1
    assert get_edit_distance("a", "ab") == 1
    assert get_edit_distance("a", "bc") == 2
    assert get_edit_distance("abcdef", "fedcba") == 6


if __name__ == '__main__':
    main()
