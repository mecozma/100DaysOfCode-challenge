a = [int(i) for i in input("Type numbers: \n").split(" ")]
b = [int(j) for j in input("Type numbers: \n").split(" ")]
set_a, set_b = set(a), set(b)
sd = set_a.symmetric_difference(set_b)
sd = sorted(list(sd))
for i in sd:
  print(i)
