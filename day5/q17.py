account = 0
question = input("To make a deposit type D, to withdraw money press W, to see"
                 + "the ballance press B to exit the app type exit:  ")
while True:
  if question == "end":
    break
  elif question.upper() == "D":
    value = input("Please type the value you want to deposit:  ")
    account += int(value)
    question = input("To make a deposit type D, to withdraw money press W, to see"
                 + "the ballance press B to exit the app type exit:  ")
  elif question.upper() == "W":
    value = input("Please type the value you want to widraw:  ")
    account -= int(value)
    question = input("To make a deposit type D, to withdraw money press W, to see"
                 + "the ballance press B to exit the app type exit:  ")
  elif question.upper() == "B":
    print("You have $:", account)
    question = input("To make a deposit type D, to withdraw money press W, to see"
                 + "the ballance press B to exit the app type exit:  ")        
  else:
    print("We couldn't process your transaction!")
    question = input("To make a deposit type D, to withdraw money press W, to see"
                 + "the ballance press B to exit the app type exit:  ")
