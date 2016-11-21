def hash_code(s):
    mask = (1 << 32) - 1  # limit to 32-bit integers
    h = 0
    for character in s:
        h = (h << 5 & mask) | (h >> 27)  # 5-bit cyclic shift of running sum
        h += ord(character)  # add in value of next character
    return h
