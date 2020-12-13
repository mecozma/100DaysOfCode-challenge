"""
With a given integral number n, write a program to generate a dictionary that
contains (i, i x i) such that is an integral number between
1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program: 8
'{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}'
"""

def create_dict(number):
    generated_dict = {}
    for i in range(0, number + 1):
        generated_dict[i] = i * i
    return generated_dict

print(create_dict(8))


# Dictionary comprehension
n = int(input("Type number: " ))
gen_dict = {i : i*i for i in range(1, n+1)}
print("Using comprehension: ", gen_dict)
