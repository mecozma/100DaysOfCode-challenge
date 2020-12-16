def count_upper_lower():
    characters = input("Please type a phrase:  ")
    upper, lower = 0, 0
    for i in characters:
        upper += i.isupper()
        lower += i.islower()
    return f"UPPER CASE: {upper}\nLOWER CASE: {lower}"


print(count_upper_lower())


# Initial solution.
def count_upper_lower_initial():
    characters = input("Please type a phrase:  ")
    upper, lower = 0, 0

    for i in characters:
        if ord(i) >= 97 and ord(i) < 123:
            lower += 1
        elif ord(i) >= 65 and ord(i) < 91:
            upper += 1
    print(f"UPPER CASE: {upper}\nlower case: {lower}")


count_upper_lower_initial()
