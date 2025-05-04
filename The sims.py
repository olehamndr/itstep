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
        if self.car.fuel <= self.car.consumption:
            self.shopping("fuel")
            return
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

def eat(self):
    if self.home.food <= 0:
        self.shoping("food")
    else:
        if self.satiety >= 100:
            return
        else:
            self.satiety += 5
            self.home.food -= 5

def chill(self):
    self.gladness += 10
    self.home.mess += 5

def cleen_home(self):
    self.gladness -= 5
    self.home.mess = 0

def to_repair(self):
    self.money -= 50
    self.car.strenght += 100

def work(self):
    if self.car.drive():
        pass
    else:
        if self.car.fuel <= self.car.consumption:
            self.shopping("fuel")
            return
        else:
            self.to_repair()
            return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

def shopping(self, manage):
    if self.car.drive():
        pass
    else:
        if self.car.fuel <= self.car.consumption:
            manage = "fuel"
        else:
            self.to_repair()
            return
        if manage == "fuel":
            self.car.fuel += 100
            self.money -= 100
            print("I bought fuel")
        elif manage == "food":
            self.home.food += 50
            self.money -=  50
            print("I bought food")
        elif manage == "delicacies":
            self.money -= 10
            self.gladness += 10
            self.satiety += 2
            print("I bought delicacies")

def days_indexes(self, day):
    day = f" Today the {day} of {self.name} 's life "
    print(f"{day:=^50}", "\n")
    human_indexes = self.name + "'s indexes"
    print(f"{human_indexes:^50}", "\n")
    print(f"Money – {self.money}")
    print(f"Satiety – {self.satiety}")
    print(f"Gladness – {self.gladness}")
    home_indexes = "Home indexes"
    print(f"{home_indexes:^50}", "\n")
    print(f"Food – {self.home.food}")
    print(f"Mess – {self.home.mess}")
    car_indexes = f"{self.car.brand} car indexes"
    print(f"{car_indexes:^50}", "\n")
    print(f"Fuel – {self.car.fuel}")
    print(f"Strength – {self.car.strength}")
def is_alive(self):
    if self.satiety < 0:
        print("Dead...")
        return False
    if self.money < -500:
        print("Bankrupt...")
        return False
    if self.gladness < 0:
        print("Depression...")
        return False

def live(self, day):
    if self.is_alive() == False:
        return False
    if self.home == "None":
        print("Settled un the house")
        self.get_home()
    elif self.car == "None":
        self.get_car()
        print(f"I bought a car {self.car.brand}")
    elif self.job == "None":
        self.get_job()
        print(f"Going to get job  {self.job.job}, with salaru {self.jon.salary}")
    self.days_indexes(day)
    if self.satiety < 20:
        print("I am going eat")
        self.eat()
        if self.gladness < 20:
            if self.home.mess > 20:
                print("I will clearn my home")
                self.cleen_home()
            else:
                print("Lets chill")
                self.chill()
        if self.money < -50:
            print("Start working")
            self.work()
        dise = random.randint(1,4)
        if dise == 1:
            print("Lets chill")
            self.chill()
        elif dise == 2:
            print("Start working")
            self.work()
        elif dise == 3:
            print("I will clean my home")
            self.cleen_home()
        elif dise == 4:
            print("Time for treats")
            self.shopping(manage = "delicacies")





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
