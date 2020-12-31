def is_even(n):
    for i in range(0, n + 1):
        if i % 2 == 0 or i == 0:
            yield str(i)

print(",".join(list(is_even(10))))
