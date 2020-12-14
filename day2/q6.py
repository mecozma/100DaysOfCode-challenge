"""
Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 _ C _ D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:

100,150,180
The output of the program should be:

18,22,24
"""

import math

def apply_formula():
    c = 50
    h = 30
    values = []
    # Create a list of integers with the numbers passed in the input.
    items = [int(i) for i in input("Type numbers separated by comma: ")
             .split(",")]
    for integer in items:
        # Apply the formula to each element of the list.
        integer = math.sqrt(2 * c * integer / h)
        # Round the value of the integer variable.
        integer = round(integer)
        # Convert the variable in a string.
        integer = str(integer)
        # Append the integer to the values list.
        values.append(integer)
        # Join the values of the values list and return it.
    return ",".join(values)

print(apply_formula())
