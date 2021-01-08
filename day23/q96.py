#string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
#width = 4
string = input("Pass a string: \n")
width = int(input("Pass an integer: \n"))

while len(string) > 0:
  print(string[0:width])
  string = string[width:]
