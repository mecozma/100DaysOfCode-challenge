a = [5, 6, 77, 45, 22, 12, 24]
b = [value for count, value in enumerate(a) if count not in range(1, 4)]
print(b)
