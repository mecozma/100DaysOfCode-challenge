def get_user(email):
    email = email.split('@')
    return email[0]

user_input = input('Type an email address:  ')

print(get_user(user_input))
