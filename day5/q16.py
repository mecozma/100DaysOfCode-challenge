def square_odd(numbers):
    return [i * i for i in numbers if i % 2 != 0]

list_of_numbers = [int(i) for i in input("Type a sequence of comma-separated" +
                                         "numbers:  ").split(",")]

print(square_odd(list_of_numbers))
