class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_info(self):
        super().show_info()
        print(f"Department: {self.department}")

class SeniorManager(Manager):
    def __init__(self, name, salary, department, years_experience):
        super().__init__(name, salary, department)
        self.years_experience = years_experience

    def show_info(self):
        super().show_info()
        print(f"Years of Experience: {self.years_experience}")

seniorManager = SeniorManager("Олександр Олексійович", 50000, "IT", 8)
seniorManager.show_info()
