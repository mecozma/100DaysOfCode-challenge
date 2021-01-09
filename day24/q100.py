user_input = [i for i in input("Pass a phrase: \n").split(" ")]
words_dict = {}
words_list = []
for j in user_input:
    if j in words_dict.keys():
        words_dict[j] += 1
    else:
        words_list.append(j)
        words_dict[j] = 1
for word in words_list:
    print(words_dict[word])
