class student:
    print("Hello world")

    def __init__(self, height=164):
        self.height = height
Artem = student(height=170)
Mark = student()
print("My height = ", Artem.height)
print("My height = ", Mark.height)
