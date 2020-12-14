"""
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""

class InputOutput:
    def __init__(self):
        self.value = ""

    def get_value(self):
        self.value = input("Plese type the value here:  ")

    def print_value(self):
        print(self.value.upper())


ask_question = InputOutput()
ask_question.get_value()
ask_question.print_value()


