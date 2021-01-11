"""
Given two strings, write a method to decide if one is a permutation of the
other.
"""


s1 = "Hello world!"
s2 = "Hello World!"


def check_permutations(string_1, string_2):
    string_1 = string_1.lower()
    string_2 = string_2.lower()
    dict_1 = {}
    if len(string_1) is not len(string_2):
        return False
    for i in string_1:
        if i in dict_1.keys():
            dict_1[i] += 1
        else:
            dict_1[i] = 1

    for i in string_2:
        if i not in dict_1.keys() or dict_1[i] < 0:
            return False
    return True


print(check_permutations(s1, s2))
