list_of_numbers = [i for i in range(1, 31)]

filtered_list = filter(lambda j: j % 2 == 0 and j <= 20, list_of_numbers)

print(list(filtered_list))
