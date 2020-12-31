n = int(input("Type an int:  "))
def five_and_seven(n):
    for i in range(0, n + 1):
        if i % 5 == 0 and i % 7 == 0:
            yield i


for i in five_and_seven(n):
    print(i, end = ",")
