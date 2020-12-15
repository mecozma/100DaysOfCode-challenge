"""
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

hello world! 123
Then, the output should be:

LETTERS 10
DIGITS 3
"""

def count_alfa_and_digits():
    letters, digits = 0, 0
    input_values = [i for i in input("Please type alphanumeric values:  ")]
    for character in input_values:
        if character.isdigit():
            digits += 1
        elif character.isalpha():
            letters += 1
    return f"LETTERS: {letters}\nNUMBERS: {digits}"


print(count_alfa_and_digits())
