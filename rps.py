def rps():
    get_name1 = input()
    get_name2 = input()
    get_game1 = input()
    get_game2 = input()
    same = "비김"
    if get_game1 == "가위":
        if get_game2 == "가위":
            return same
       	elif get_game2 == "바위":
            return "바위"
        elif get_game2 == "보":
            return "가위"
    elif get_game1 == "바위":
        if get_game2 == "가위":
            return "바위"
       	elif get_game2 == "바위":
            return same
        elif get_game2 == "보":
            return "보"
    elif get_game1 == "보":
        if get_game2 == "가위":
            return "가위"
       	elif get_game2 == "바위":
            return "바위"
        elif get_game2 == "보":
            return same

a=rps()
if a=="비김":
    print("비겼습니다.")
else:
    print(f"{a}가 이겼습니다.")
