import random
class Human:
    def __init__(self, name="Name", job="None", home="None", car="None", pet="None"):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.pet = pet
        self.money = 100
        self.gladness = 50
        self.satiety = 50
def get_home(self):
    self.home = House()

def get_car(self):
    self.car = Auto(brands_of_car)

def get_job(self):
    if self.car.drive():
        pass
    else:
        self.to_repair()
        return
    self.job = Job(job_list)

def get_pet(self):
    self.pet = Pet()

def petting(self):
    if self.pet:
        self.satiety += 10
        self.pet.mood += 5
        print(f"{self.name} stroked {self.pet}")
    else:
        print(f"{self.name} don`t have a pet")




class House:
    def __init__(self):
        self.food = 0
        self.mess = 0

brands_of_car = {
"BMW":{"fuel":100, "strength":100,"consumption": 6},
"Lada":{"fuel":50, "strength":40,"consumption": 10},
"Volvo":{"fuel":70, "strength":150,"consumption": 8},
"Ferrari":{"fuel":80, "strength":120,"consumption": 14},
}
class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption =brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength>0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("Car cannot move")
            return False
job_list = {
"Java developer":{"salary":50, "gladness_less": 10 },
"Python developer":{"salary":40, "gladness_less": 3 },
"C++ developer":{"salary":45, "gladness_less": 25 },
"Rust developer":{"salary":70, "gladness_less": 1 },
}
class Job:
    def __init(self, job_list):
        self.job = random.choise(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

pet_list = {
    "Cat": {"satiety": 70, "mood": 70, "energy": 50},
    "Dog": {"satiety": 60, "mood": 80, "energy": 60},
    "Parrot": {"satiety": 50, "mood": 90, "energy": 40},
    "Hamster": {"satiety": 65, "mood": 75, "energy": 55},
}
class Pet:
    def __init__(self, pet_list):
        self.pet = random.choice(list(pet_list))
        self.satiety= pet_list[self.pet]["pet satiety"]
        self.mood = pet_list[self.pet]["pet mood"]
        self.energy = pet_list[self.pet]["pet energy"]
