"""
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:

without,hello,bag,world
Then, the output should be:

bag,hello,without,world
"""

def reverse_string():
    input_value = [i for i in input("Type a phrase:  ").split(" ")]
    input_value.sort()
    return ",".join(input_value)


print(reverse_string())
