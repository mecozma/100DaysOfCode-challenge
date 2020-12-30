number = input("Type a number:  ")
total = 0
for i in range(1,int(number) + 1):
    total += int(i)/int(i + 1)

print(round(total, 2))
