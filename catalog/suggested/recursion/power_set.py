def power_set(s):
    return power_set_util(list(s), 0)


def power_set_util(s, index):
    if index == len(s):
        all_subsets = [set()]
    else:
        all_subsets = power_set_util(s, index + 1)
        new_subsets = []
        for subset in all_subsets:
            concat = set(subset)
            concat.add(s[index])
            new_subsets.append(concat)

        all_subsets.extend(new_subsets)

    return all_subsets


def main():
    print(power_set({8, 9, 3}))


if __name__ == '__main__':
    main()
