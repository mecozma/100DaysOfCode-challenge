def compute_num():
    try:
        num = int(input('Type a number: '))
        return num / 0
    except ZeroDivisionError:
        return 'Could not divide with 0.'
    except:
        return 'All other errors!'


print(compute_num())

