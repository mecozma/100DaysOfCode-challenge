def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n -2)

print(fibonacci(7))

fib = lambda x: 1 if x == 1 else 0 if x == 0 else fib(x - 1) + fib(x - 2)
print(fib(7))
