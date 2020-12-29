# Importing the sys module in order to get the type of the exception.
import sys
# Print Python's Built-in Expeptions.
# print(dir(locals()['__builtins__']))

# Catching Exceptions in Python.
random_list = ['a', 0, 2]

for entry in random_list:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)

# This can also be done this way.
for i in random_list:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)

# Being more specific.

try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass


# Raising Exceptions in Python.
try:
    a = int(input('Type a positive number: '))
    if a < 0:
        raise ValueError('This is not a positive number!')
except ValueError as err:
    print(err)

# Try with else clause.
try:
    num = int(input('Type a number: '))
    assert num % 2 == 0
except:
    print('Not an even number.')
else:
    reciprocical = 1/num
    print(reciprocical)

