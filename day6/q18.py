import re


def test_password(password):
    regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    pattern = re.compile(regex)
    match = re.search(pattern, password)
    if match:
        print("Match!")
    else:
        print("Invalid password. Try again!")

user_input = input("Type password:  ")
print(test_password(user_input))
