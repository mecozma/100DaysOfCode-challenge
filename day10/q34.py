def square_numbers(number=20):
    square_list = [i**2 for i in range(1, number + 1)]
    print(square_list[0:5])


print(square_numbers())
