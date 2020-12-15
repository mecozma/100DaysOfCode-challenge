"""
Write a program which accepts a sequence of comma separated 4 digit binary
numbers as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated
sequence.

Example:

0100,0011,1010,1001
Then the output should be:

1010
Notes: Assume the data is input by console.
"""


def is_divisible_by_5():
    values = [i for i in input("Please type the bynaryes comma separated:  ")
              .split(",")]
    are_divided_by_5 = []
    for value in values:
        if int(value,2) % 5 == 0:
            are_divided_by_5.append(value)

    return ",".join(are_divided_by_5)


print(is_divisible_by_5())
