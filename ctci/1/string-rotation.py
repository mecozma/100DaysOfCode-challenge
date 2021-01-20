"""
Assume you have a method isSubstring which checks if one word is a substring of
another. Given two strings, s1 and s2, write code to check if s2 is a rotation
of s1 usint only one call su isSubstring.
Example: waterbottle is a rotation of erbottlewat.

Explaination:
    1. If the strings don't have the same length means they can't be a rotation
    of eachother.
    2. Concatenating the first string with itselg will create an instance of
    the other string somewhere in it.
    3. Check if the second string is contained by the variable created in the
    previous step.

    s1s1 = s1 + s1
    s1s1 = erbottlewat + erbottlewat  -> "erbottle[waterbottle]wat"
"""


def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    s1s1 = s1 + s1
    if s2 not in s1s1:
        return False
    return True


print(is_rotation("waterbottle", "erbottlewat"))
