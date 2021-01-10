# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures.

# Solution 1.
string = "qwerty"


def is_unique(string):
    table = {}
    for i in string:
        if i in table.keys():
            print("There are duplicates characters in the string.")
        else:
            table[i] = 1
    print("All the characters are unique!")


is_unique(string)


# Solution 2.
string2 = "qwertyy"


def is_unique_loop(string):
    for i in range(0, len(string) - 1):
        counter = 0
        for j in range(1, len(string)):
            if string[i] == string[j]:
                counter += 1
        if counter > 1:
            print("There are duplicates characters in the string.")
            return
    print("All the characters are unique!")


is_unique_loop(string2)
