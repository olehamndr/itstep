def culculator(x1, x2, op):
    if op == "+":
        print("result: ",x1 + x2)
    elif op == "-":
        print("result: ",x1 - x2)
    elif op == "*":
        print("result: ",x1 * x2)
    elif op == "/":
        if x2 == 0:
            print("Division by zero")
        else:
            print("result: ",x1 / x2)

a = float(input("Enter number1: "))
b = float(input("Enter number2: "))
operation = input("Enter +, -, /, *: ")
culculator(a, b, operation)