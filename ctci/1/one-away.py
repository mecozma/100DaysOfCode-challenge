"""
There are three types of edits that can be performed on strings:
  insert a character,
  remove a character or
  replace a character.
Given two strings, write a function to check if they are one edit
(or zero edits) away.
Example:
  pale, ple   -> true
  pales, pale -> true
  pale, bale  -> true
  pale, bake  -> false
"""


def one_away(string1, string2):
  if len(string1) > len(string2) + 1 or len(string2) > len(string1) + 1:
    return False
  count = {}
  counter = 0
  for i in string1:
    count[i] = count.setdefault(i, 0)+1
  for j in string2:
    if j in count.keys():
      count[j] -= 1
  for _,v in count.items():
    if v > 0:
      counter += 1
  if counter > 1:
    return False
  return True
  print(count)

print(one_away("pale", "bake"))
