results = [int(i) for i in input("Please pass scores: ").split(" ")]
# Sort the integers of the list
results = sorted(results)
# Convert the list in a set to remove all the duplicates.
results = set(results)
# Convert the set into a list in order to get the item before last.
results = list(results)
print(results[-2])
