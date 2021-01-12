"""
Implement a method to perform basic string compression using the counts of
repeated characters. For example, the string 'aabccccaaa' would become
'a2b1c4a3. If the 'compressed' string would not become smaller than the
original string, your methos should return the original string. You can assume
that the string has only uppercase and lowercasse letters (a-z).:w
"""


def compress_string(string):
    string = string.lower()
    counter = 0
    result = ""
    for i in range(0, len(string)):
        counter += 1
        if i + 1 >= len(string) or string[i] != string[i + 1]:
            result += string[i] + str(counter)
            counter = 0
    if len(result) > len(string):
        return string
    return result


print(compress_string("aabbbccccaaddc"))
print(compress_string("abcdefg"))
