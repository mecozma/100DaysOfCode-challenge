# The class needs to be derived from the Exception class.
class Error(Exception):
    pass

class ValueTooSmallError(Error):
    pass

class ValueTooLargeError(Error):
    pass

# The number to be guessed.
number = 10

while True:
    try:
        i_num = int(input('Enter a number:  '))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print('This value is too small, try again!\n')
    except ValueTooLargeError:
        print('This value is too large, try again!\n')
print(f'Congrats! Your number is: {number}')

# Customizing Exception Classes.
class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """
    def __init__(self, salary, message='Salary is not in (5000, 15000) range'):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

salary = int(input('Enter salary amount: '))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)
