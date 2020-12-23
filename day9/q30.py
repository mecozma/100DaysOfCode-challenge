def max_length(s1, s2):
    s1_length = len(s1)
    s2_length = len(s2)
    if s1_length > s2_length:
        print(s1)
    elif s2_length > s1_length:
        print(s2)
    else:
        print(s1)
        print(s2)

max_length("a", "bb")

max_length("aa", "b")

max_length("AAA", "BBB")
