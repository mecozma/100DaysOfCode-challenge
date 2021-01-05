a = [12, 24, 35, 70, 88, 120, 155]
b = [value for count, value in enumerate(a) if count % 2 != 0]
print(b)
