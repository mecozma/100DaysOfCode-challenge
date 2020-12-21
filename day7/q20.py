class Divide:
    def divide_by_seven(number):
        for i in range (0, int(number / 2)):
            yield i * number


for i in Divide.divide_by_seven(int(input("Type a number:  "))):
    print(i)
