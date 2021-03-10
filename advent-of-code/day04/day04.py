input_data = ""
# Read the input file.
with open('input.txt', 'r') as f:
    for line in f:
        input_data += line

# Split the input data using the new line delimiter.
split_new_line = input_data.split('\n\n')

# Replace the new line characters with white spaces to have the passport on a
# single line.
replace_new_line = [string.replace('\n', ' ') for string in split_new_line]
# Split each passport in order to get a list of lists.
list_format = [string.split() for string in replace_new_line]


# Convert the 2D list to a list of dicts.
def list_to_dict(list_input):
    passports_dict = {}
    for item in list_input:
        key_value = item.split(':')
        k = key_value[0]
        v = key_value[1]
        passports_dict[k] = v
    return passports_dict


# Assign the list to passports variable.
passports = [list_to_dict(i) for i in list_format]


# Find the valid passort.
def find_valid_passport(passport):
    no_valid_passports = 0
    for passport in passports:
        if ("byr" in passport and "iyr" in passport and "eyr" in passport
            and "hgt" in passport and "hcl" in passport and "ecl" in passport
                and "pid" in passport):
            no_valid_passports += 1
    return no_valid_passports


print(find_valid_passport(passports))


# Part two.
