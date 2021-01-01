import math

def binary_search(numbers, item):
    start = 0
    end = len(numbers) - 1
    while start < end:
        middle = math.floor((start + end) / 2)
        if item == numbers[middle]:
            return middle
        elif item < numbers[middle]:
            end = middle - 1
        elif item > numbers[middle]:
            start = middle + 1
    return False

numbers = [ i for i in range(0, 21)]

print(binary_search(numbers,5))
