import math


x, y = 0, 0
print("Type values using this patternd: UP 5 DOWN 3 LEFT 3 RIGHT 2")
while True:
  user_input = input("Type Direction and steps:  ")
  if user_input == "exit":
    break

  activity = user_input.split(" ")
  direction = activity[0].lower()
  number_steps = int(activity[1])

  if direction == "up":
    y = y + number_steps
  elif direction == "down":
    y = y - number_steps
  elif direction == "right":
    x = x + number_steps
  elif direction ==" left":
    x -= number_steps
  else:
    pass

print(round(math.sqrt(x**2 + y**2)))
