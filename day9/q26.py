def sum_numbers(a, b):
    c = a + b
    return c

numbers = [int(i) for i in input("Type who numbers separate by space: ")
           .split(" ")]


print(sum_numbers(numbers[0], numbers[1]))
