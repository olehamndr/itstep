number1 = int(input("Enter value from: "))
number2 = int(input("Enter value to: "))
for i in range(number1, number2+1):
    if i % 2 != 0:
        print(i)
