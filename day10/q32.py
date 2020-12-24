def number_to_dict(number=20):
    dictionary = {i: i**2 for i in range (1, number + 1)}
    for k in dictionary.keys():
        print(k)


number_to_dict()
