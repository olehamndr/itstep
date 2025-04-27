class human:
    def __init__(self, name="Бодя"):
        self.name = name

class Car:
    def __init__(self, brand="Porsche"):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, human):
        self.passengers.append(human)

    def print_passengers(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passengers: ")
            for i in self.passengers:
                print(i.name)

dima = human("Dmytro")
oleksandr = human("Oleksandr")
car1 = Car("Lamborghini")
car2 = Car()
car2.add_passengers(dima)
car1.add_passengers(oleksandr)
car1.print_passengers()
car2.print_passengers()