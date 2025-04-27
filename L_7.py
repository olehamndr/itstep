class human:
    def __init__(self, name="Бодя"):
        self.name = name

class Car:
    def __init__(self, brand="Porsche"):
        self.brand = brand
        self.passagers = []

dima = human("Dmytro")
ihor = human("Ihor")
car1 = Car("Lamborghini")
car2 = Car()