"""
Write a method to replace all spaces in a string with '%20'. You may assume
that the string has sufficient space at the end to hold the additional
characters, and that you are given the 'true' length of the string.
EXAMPLE:
    Input: 'Mr John Smith'
    Output: 'Mr%20John%20Smith'

"""


def urlfy_string(string):
    url = ""
    if len(string) == 0:
        return False
    for i in string:
        if i == " ":
            url += "%20"
        else:
            url += i
    return url


string = "Mr John Smith"
print(urlfy_string(string))
