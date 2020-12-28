import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
       return math.pi * self.radius ** 2

circle = Circle(3)
print(circle.area())
