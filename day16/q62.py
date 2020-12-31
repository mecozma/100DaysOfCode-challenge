fib = lambda x: 1 if x == 1 else 0 if x == 0 else fib(x - 1) + fib(x - 2)
numbers = [str(fib(i)) for i in range(1, int(input("Type an int:  ")) + 1)]
print(",".join(numbers))

