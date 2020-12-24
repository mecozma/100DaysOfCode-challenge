def square_keys(number=20):
    dictionary = {key: key**2 for key in range(1, number + 1)}
    return dictionary

print(square_keys())
