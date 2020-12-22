class Animal:
    name = "Harvey"
    def __init__(self, name=None):
        self.name = name

horse = Animal
print(horse.name)

dog = Animal("Peanut")
print(dog.name)

