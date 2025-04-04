start = int(input("Введіть число, з якого почати: "))
end = int(input("Введіть число, по яке виводити: "))

print("Результат:")
for number in range(start, end + 1):
    print(number)
