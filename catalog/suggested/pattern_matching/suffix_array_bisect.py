from bisect import bisect_left, bisect_right

strls = ['a', 'awkward', 'awl', 'awls', 'axe', 'axes', 'bee']

# t = 'This is the world.$'
t = 'banana$'

suffixes = sorted([t[i:] for i in range(len(t))])

print(len(suffixes))
print(suffixes)

# Get range of elements with ‘aw’ as a prefix
st, en = bisect_left(strls, 'aw'), bisect_left(strls, 'ax')
print(st, en)  # output: (1, 4)
