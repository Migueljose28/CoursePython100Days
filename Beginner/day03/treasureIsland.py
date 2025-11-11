print("""
88                                88                              
88                                88                              
88                                88                              
88,dPPYba,  ,adPPYYba,  ,adPPYba, 88   ,d8  ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 a8"     "" 88 ,a8"  a8P_____88 88P'   "Y8  
88       88 ,adPPPPP88 8b         8888[    8PP""""""" 88          
88       88 88,    ,88 "8a,   ,aa 88`"Yba, "8b,   ,aa 88          
88       88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a `"Ybbd8"' 88          
""")
print("Welcome to Treasure Island. \n Your mission is to find the treasure.")

questions = ("left or right", "swim or wait", "which port")
answer = ("left", "wait", "yellow")
aftereffect = ("Fall into a hole.", "Attacked by trout.")

for ask in questions:
    choice = input(ask + "?")
    i = questions.index(ask)
    if not choice.lower() == answer[i]:
        if ask == questions[-1]:
            if choice.lower() == "red":
                print("Burned by fire")
            if choice.lower() == "blue":
                print("Eaten by beasts")
        else:
            print(aftereffect[i])
        print("Game Over!")
        break
    print("you win")

