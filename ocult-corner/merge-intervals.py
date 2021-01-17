"""
Example Input        1-10, 15-23, 27-29, 30-40
                     8-12, 21-28

Example Input        8-12, 21-28
                     1-10, 15-23, 27-29, 30-40

Output               1-12, 15-29, 30-40
"""


def join_intervals(*args):
  # Concatenating the strings in order to filter the alphanum characters.
  arguments = args[0] + "," + args[1]
  print(arguments)
  # Split the string where each coma occurs and after split where a dash occurs.
  arguments = [i.split("-") for i in arguments.split(",")]
  print(arguments)
  # Convert each element into an int.
  ar = [list(map(int,i)) for i in arguments]
  # Sort the elements of the list by the first element of each sub list.
  sorted_ar = sorted(ar, key=lambda x: x[0])
  joined_intervals = []
  # Iterate over the list's elements stopping before the last element.
  for i in range(0, len(sorted_ar) - 1, 2):
    current = i
    next = i + 1
    # Check if the intervals are lapping.
    if sorted_ar[current][0] < sorted_ar[next][0] < sorted_ar[current][1] < sorted_ar[next][1]:
      joined_intervals.append([sorted_ar[current][0],sorted_ar[next][1]])
    else:
      joined_intervals.append([sorted_ar[current], sorted_ar[next]])
  return joined_intervals


first = "1-10, 15-23, 27-29, 30-40"
second = "8-12, 21-28"
print(join_intervals(first, second))
