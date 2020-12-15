"""
Write a program that accepts a sequence of whitespace separated words as input
and prints the words after removing all duplicate words and sorting them
alphanumerically.

Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again
Then, the output should be:

again and hello makes perfect practice world
"""


def filter_and_sort():
    # Create a set with all the words in the string. A set has unique values.
    user_input = {i for i in input("Type a phrase here:  ").split(" ")}
    # Convert the set in a list in order to sort it.
    user_input = list(user_input)
    user_input.sort()
    # Join all the elements of the list with a space and return it.
    return " ".join(user_input)


print(filter_and_sort())
