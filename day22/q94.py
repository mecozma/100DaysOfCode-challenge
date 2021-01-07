def count(heads, legs):
    count = 0
    count = ((legs) - 2 * (heads)) / 2
    return count


heads = 35
legs = 94
rabbits = count(heads, legs)
chickens = heads - rabbits
print(f"Number of chickens: {chickens}\nNumber of rabbits: {rabbits}\n")
