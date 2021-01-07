import itertools


a = [1, 2, 3]
b = itertools.permutations(a)
for i in b:
    print(i)
