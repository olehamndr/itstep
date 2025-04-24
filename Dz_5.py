class Employee:
    def __init__(self, name="", position="", salary=0):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary_info(self, name="", salary=0):
        return f"Заробітна плата {self.name} : {self.salary}"

    def input_info(self, name="", position="", salary=0):
        self.name = input("Введіть ім'я працівника: ")
        self.position = input("Введіть посаду працівника: ")
        self.salary = int(input("Введіть заробітну плату працівника: "))

Employee = Employee()
Employee.input_info()
print(Employee.get_salary_info())