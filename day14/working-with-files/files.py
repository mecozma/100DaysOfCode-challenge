document = 'lipsum.txt'

with open(document, 'a') as append:
    append.write('\nI added this line!')

with open(document, 'r') as file:
    lines = file.readlines()
    print(lines)
    for line in lines:
        if line != "":
            print(line)
        else:
            pass
