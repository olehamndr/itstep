class student:
    number = 0
    def __init__(self, height=164, name = None):
        self.height = height
        student.number += 1
        self.name = name

    def grow(self, height=3):
        self.height+=height

    def __str__(self):
        return f"Я студент з іменем {self.name} мій зріст {self.height}"
Artem = student(height=170, name = "Artem")
Mark = student(name = "Mark")
print(Artem)
print(Mark)

while Mark.height<=180:
    Mark.grow()

print(Artem)
print(Mark)
print("number of student", student.number)