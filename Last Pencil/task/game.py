number_of_pencils = int(input("How many pencils would you like to use:\n"))
name1 = "Idaho"
name2 = "Leto"

current_player= input(f"Who will be first? ({name1}, {name2}):\n")


while number_of_pencils > 0:
    pencil_inventory = ""
    for i in range(number_of_pencils):
        pencil_inventory += "|"
    print(f"\n{pencil_inventory}")
    if current_player == name1:
        print(f"{name1}'s turn:")
        number_of_pencils -= int(input())
        current_player = name2
    elif current_player == name2:
        print(f"{name2}'s turn:")
        number_of_pencils -= int(input())
        current_player = name1