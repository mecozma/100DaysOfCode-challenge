class Person:
    def __init__(self):
        self.gender = "Unknown"

    def get_gender(self):
        return self.gender


class Male(Person):
    def __init__(self):
        self.gender = "male"


class Female(Person):
    def __init__(self):
        self.gender = "female"


man = Male()
print(man.get_gender())
woman = Female()
print(woman.get_gender())
