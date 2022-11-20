import string

name1 = "Idaho"
name2 = "Leto"
possible_values = [1, 2, 3]

def pencil_test(pencils_to_test, number_of_pencils):
    while pencils_to_test not in possible_values:
        pencils_to_test = input("Possible values: '1', '2', or '3'\n")
    while pencils_to_test > number_of_pencils:
        pencils_to_test = input("Too many pencils were taken")

def test_number_of_pencils(number_of_pencils):
    while number_of_pencils not in string.digits or int(number_of_pencils) <= 0:
        if number_of_pencils not in string.digits:
            number_of_pencils = input("The number of pencils should be numeric\n")
        elif int(number_of_pencils) == 0:
            number_of_pencils = input("The number of pencils should be positive\n")
        else:
            number_of_pencils = int(number_of_pencils)


def test_current_player(current_player, name1, name2):
    while current_player not in [name1, name2]:
        if current_player != name1 and current_player != name2:
            current_player = input(f"Choose between '{name1}' and '{name2}'\n")
    return current_player

def take_a_turn(number_of_pencils):
    pencil_test(pencils_to_take, number_of_pencils)
    number_of_pencils -= pencils_to_take



number_of_pencils = (input("How many pencils would you like to use:\n"))
test_number_of_pencils(number_of_pencils)
current_player= input(f"Who will be first? ({name1}, {name2}):\n")
test_current_player(current_player, name1, name2)


while int(number_of_pencils) > 0:
    for i in range(int(number_of_pencils)):
        print("|", end="")
    pencils_to_take = input(f"\n{current_player}\'s turn!\n")
    take_a_turn(number_of_pencils)
    if current_player == name1:
        current_player = name2
    elif current_player == name2:
        current_player = name1
