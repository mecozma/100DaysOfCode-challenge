"""
Write a program which can compute the factorial of a given numbers.The results
should be printed in a comma-separated sequence on a single line.Suppose the
following input is supplied to the program: 8 Then, the output should be:40320
"""
def find_factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i
    return factorial

print(find_factorial(8))


def find_factorial_recursive(number):
    if number == 0:
        return 1
    return number * find_factorial_recursive(number -1)

print("Recursive method", find_factorial_recursive(8))
