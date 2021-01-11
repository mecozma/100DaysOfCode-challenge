"""
Given a string, write a function to check if it is a permutation of a
palindrome. A permutation is a word or a phrase tht is the same forwards and
backwards. A permutation is a rearangement of letters. The palindrome does not
need to be limited to just dictionary words.
EXAMPLE:
    Input: Tact coa
    Output: True (permutations:  taco cat, atco cta, etc.)
"""


def check_palindrome(string):
    string = string.lower()
    hash_table = {char: string.count(char)
                  for char in string if char.isalpha()}
    odd_counter = 0
    for key, value in hash_table.items():
        if value % 2 != 0 and odd_counter == 0:
            odd_counter += 1
        elif value % 2 != 0 and odd_counter != 0:
            return False
    return True


palindrome = "taco cAt"
print(check_palindrome(palindrome))
