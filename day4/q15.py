def compute_value():
    user_input = input("Please type a digit:  ")
    temp_value = str()
    total = 0
    for i in range(4):
        temp_value += user_input
        total += int(temp_value)
    return total

print(compute_value())
