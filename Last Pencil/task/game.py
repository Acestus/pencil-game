number_of_pencils = int(input("How many pencils would you like to use:\n"))
name1 = "Idaho"
name2 = "Leto"
pencil_inventory = ""
first_player= input(f"Who will be first? ({name1}, {name2}):\n")

for i in range(number_of_pencils):
    pencil_inventory += "|"
print(f"\n{pencil_inventory}")
print(f"{first_player} is going first!")