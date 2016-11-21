"""
Generate m random, non-duplicate numbers between 1 and n
Credit to Knuth
"""

import random


def generate_random(count, max_val):
    selected = []

    for i in range(max_val):
        if ((random.random() * max_val) % (max_val - i)) < count:
            selected.append(i + 1)
            count -= 1

    return selected


def main():
    m = 20
    n = 100

    rands = generate_random(m, n)

    print(rands)

    assert len(rands) == m


if __name__ == '__main__':
    main()
