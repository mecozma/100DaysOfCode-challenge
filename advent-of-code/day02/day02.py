#!/usr/bin/python

"""
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way
down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day.
"Something's wrong with our computers; we can't log in!" You ask if you can i
take a look.

Their password database seems to be a little corrupted: some of the passwords
wouldn't have been allowed by the Official Toboggan Corporate Policy that was
in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of
passwords (according to the corrupted database) and the corporate policy when
that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy
indicates the lowest and highest number of times a given letter must appear for
the password to be valid. For example, 1-3 a means that the password must
contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is
not; it contains no instances of b, but needs at least 1. The first and third
passwords are valid: they contain one a or nine c, both within the limits of
their respective policies.

How many passwords are valid according to their policies?
"""
import re

# Find match.
def find_match(input):
    reg_exp = '(\d+)-(\d+)\s(\w):\s(\w+)'
    capturing_groups = re.match(reg_exp, input).groups()
    low = int(capturing_groups[0])
    high = int(capturing_groups[1])
    char = capturing_groups[2]
    password = capturing_groups[3]
    count_chars = 0
    for i in password:
        if i == char:
            count_chars += 1
    if low <= count_chars <= high:
        return True
    else:
        return False

# Read the file
with open('input.txt', 'r') as file:
    total_matches = 0
    for line in file:
        if find_match(line) == True:
            total_matches += 1
    print(total_matches)

