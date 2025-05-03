class Human:
    def __init__(self, satiety=50):
        self.satiety = satiety

    def eat(self):
        self.satiety += 25
        food.amount -+ 1
        print(f"human satiety: {self.satiety}")
        print(f"food amount: {food.amount}")

class Food:
    def __init__(self, amount = 3):
        self.amount = amount

human = Human()
food = Food()
human.eat()