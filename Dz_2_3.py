import random
print("Вам потрібно відгадати випадкове число від 1 до 10 з 3 спроб")
random_number = random.randint(1, 10)
count = 0
user_number = 0
while count<=3:
  user_number = int(input('Ваше число: '))
  count +=1
  if random_number > user_number:
    print("Більше")
  elif random_number < user_number:
    print("Менше")
  elif random_number == user_number:
    print("Ви відгадали число!")
  if count==3:
    print(f"Ви не відгадали число. Було загадано:", random_number)