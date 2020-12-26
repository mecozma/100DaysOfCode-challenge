import math


def half_tuple(param):
    print(param[:math.floor(len(param) / 2)])
    print(param[math.floor(len(param) / 2):])


print(half_tuple((1,2,3,4,5,6,7,8,9,10)))
