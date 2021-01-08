import calendar


user_input = [int(i) for i in input("Pass date: yyyy mm dd  \n").split(" ")]
check_day = calendar.weekday(user_input[0], user_input[1], user_input[2])
print(calendar.day_name[check_day].upper())
