a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter the operation (+, -, *, /): ")
operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: "Division by zero" if b == 0 else a / b
}
result = operations[op](a, b)
print(result)