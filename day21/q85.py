a = [12, 24, 35, 70, 88, 120, 155]
b = [0, 4, 5]
c = [value for count, value in enumerate(a) if count not in b]
print(c)
