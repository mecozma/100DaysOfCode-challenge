"""
Write a program, which will find all such numbers between 1000 and 3000
(both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence
on a single line.
"""


def are_even():
    numbers_range = [str(i) for i in range(1000, 3001)]
    even_numbers = []
    for number in numbers_range:
        is_even = True
        for letter in str(number):
            if int(letter) % 2 != 0:
                is_even = False
        if is_even:
            even_numbers.append(number)
    return ",".join(even_numbers)


print(are_even())

