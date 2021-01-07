user_answer = input("Type a string:  ")
count_letters = {}

for i in user_answer:
    if i in count_letters.keys():
        count_letters[i] += 1
    else:
        count_letters[i] = 1

for key, value in count_letters.items():
    print(key, value)
