a = "1234abcdefghij"
strings, integers = 0, 0
for i in a:
    if i.isdigit():
        integers += 1
    else:
        strings += 1
print(f"Strings: {strings}\nIntegers: {integers}")
