class Car:
    def __init__(self, make="", model="", year=0):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        print(self.year, self.make, self.model)

    def input_info(self):
        self.year = input("Enter the car year: ")
        self.make = input("Enter the car brand: ")
        self.model = input("Enter the car model: ")

car = Car()
car.input_info()

count = int(input("For see the car info enter 1, for exit enter 2: "))

if count == 1:
    car.get_info()
elif count == 2:
    print("Goodbye!")
    exit()
else:
    print("Invalid choice. Please try again.")
