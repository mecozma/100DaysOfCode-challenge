class MyError(Exception):
    def __init__(self, number, message='My custom message.'):
        self.number = number
        self.message = message
        super().__init__(self.message)

num = int(input('Type a number :'))

try:
    if num in range(5, 10):
        raise MyError(num, 'Number between 5 and 9')
    elif num in range(1, 5):
        raise MyError(num, 'Number between 1 and 4')
except MyError as err:
    print(f'The error is: {err.message}')
