def count_words(phrase):
    words = {}
    for i in phrase.split(" "):
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    dict_keys = words.keys()
    sorted_keys = sorted(dict_keys)
    for j in sorted_keys:
        print(f"\n{j}: {words[j]}")


count_words(input("Type a phrase:  "))
