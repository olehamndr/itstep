#вводити кольори світлофора доки не буде зедлене світло
color = input("Enter red, green or yellow: ")
while color != "green":
    if color == "red":
        print("red - stop")
    elif color == "yellow":
        print("yellow - wait")
    elif color == "green":
        print("green - go")
    else:
        print("error")
    color = input("Enter red, green or yellow: ")
print("green - go")