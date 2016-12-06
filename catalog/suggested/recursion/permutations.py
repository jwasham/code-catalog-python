def permute(chars):
    if len(chars) == 0:
        return [chars]

    char = chars[0]
    permutations = permute(chars[1:])

    np = []

    for p in permutations:
        for i in range(len(p) + 1):
            np.append(p[:i] + char + p[i:])

    return np


def main():
    print(permute("abc"))


if __name__ == '__main__':
    main()
