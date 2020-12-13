"""
Write a program which will find all such numbers which are divisible by 7 but
are not a multiple of 5, between 2000 and 3200 (both included).The numbers
obtained should be printed in a comma-separated sequence on a single line.
"""

def multiple_of():
    values = [number for number in range(2000, 3201)]
    filtered = []
    for value in values:
        if value % 7 == 0 and not value % 5 == 0:
            filtered.append(value)
    return filtered
print(multiple_of())
