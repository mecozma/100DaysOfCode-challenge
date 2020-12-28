class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length=0):
        # The super() built in function reffers to the supper class Shape.
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2

square = Square(5)
print(square.area())


