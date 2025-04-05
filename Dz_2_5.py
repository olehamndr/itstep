mark = int(input("Ведіть кількість балів що отримав студент: "))
if mark>=0 and mark<=49:
    print("Незадовільно")
elif mark>=50 and mark<=69:
    print("Задовільно")
elif mark>=70 and mark<=89:
    print("Добре")
elif mark>=90 and mark<=100:
    print("Відмінно")
else:
    print("Кількість балів ведено некоректно")