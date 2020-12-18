from operator import itemgetter
score = [
  ("Tom",19,80),
  ("John",20,90),
  ("Jony",17,91),
  ("Jony",17,93),
  ("Json",21,85),
]


def sort_tuples(data):
    data.sort(key = itemgetter(0, 1, 2))
    return data

print(sort_tuples(score))
