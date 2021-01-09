def num_to_pow(num):
    if num == 0:
        return num
    return num + num_to_pow(num - 1)


print(num_to_pow(5))
