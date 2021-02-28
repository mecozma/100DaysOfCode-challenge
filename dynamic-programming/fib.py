"""
Write a function `fib(n)` that takes a nubmer as an argument.
The function should return the n-th number of Fibonacci sequence.
"""
# Memoization.
# Empty object, keys will be arg to fn, value will be the return value.


def fib(n, memo={}):
    """
    Return the n-th number of a Fibonacci sequence.
        Parameters:
            n (int): A decimal integer.
            memo (obj): An empty object.
        Returns:
            memo[n] (int): The n-th number of of Fibonacci sequence.
    """
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


print(fib(7))
print(fib(50))
