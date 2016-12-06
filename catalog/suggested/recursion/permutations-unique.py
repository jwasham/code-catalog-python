"""
Permute a string that may contain duplicate characters, avoiding duplicate permutations.
"""

from collections import Counter


def permute(chars):
    results = []
    char_counts = Counter(chars)
    permute_remainder(char_counts, "", len(chars), results)
    return results


def permute_remainder(char_counts, prefix, remainder, results):
    if remainder == 0:
        results.append(prefix)

    for ch in char_counts:
        if char_counts[ch] > 0:
            char_counts[ch] -= 1
            permute_remainder(char_counts, prefix + ch, remainder - 1, results)
            char_counts[ch] += 1


def main():
    print(permute("aabc"))


if __name__ == '__main__':
    main()
