

def hash_string(word, m):
    """
    31 was set by Kernighan & Ritchie, and creates a good distribution on ASCII
    """
    hash = 0
    for c in word:
        hash = (hash * 31 + ord(c))

    return abs(hash % m)


def hash_integer(number, a, b, p, m):
    """
    p is a prime greater than m, the number of slots your hash table will support.
    a and b are randomly chosen integers modulo p with a != 0
    """
    mod_p = (a * number + b) % p

    return abs(mod_p % m)
