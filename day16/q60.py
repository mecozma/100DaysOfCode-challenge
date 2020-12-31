def compute(n):
    if n > 0:
        return compute(n-1) + 100
    return 0

print(compute(5))
print("*" * 20)
print(compute(0))
