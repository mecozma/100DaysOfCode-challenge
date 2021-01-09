user_input = input("Type a word:\n")
counter = {}
for i in user_input:
    if i in counter.keys():
        counter[i] += 1
    else:
        counter[i] = 1

sorted_tuple = sorted(counter.items(), key=lambda item: item[1], reverse=True)
for i in sorted_tuple:
    print(f"{i[0]} {i[1]}")
