from random import choice

name1 = "John"
name2 = "Jack"
possible_values = ['1', '2', '3']


def test_current_player(current_player, name1, name2):
    while current_player not in [name1, name2]:
        if current_player != name1 and current_player != name2:
            current_player = input(f"Choose between '{name1}' and '{name2}'\n")
    return current_player

def jacks_turn(number_of_pencils):
    jacks_choice = 1
    if number_of_pencils % 4 == 1:
        while int(jacks_choice) > int(number_of_pencils):
            jacks_choice = int(choice(possible_values))
    elif number_of_pencils % 4 == 2:
        jacks_choice = 1
    elif number_of_pencils % 4 == 3:
        jacks_choice = 2
    elif number_of_pencils % 4 == 0:
        jacks_choice = 3
    return jacks_choice




number_of_pencils = input("How many pencils would you like to use:\n")

while True:
    is_Int = True
    try:
        int(number_of_pencils)
    except ValueError:
        is_Int = False
    if is_Int:
        number_of_pencils = int(number_of_pencils)
        if number_of_pencils == 0:
            number_of_pencils = input("The number of pencils should be positive\n")
            continue
        elif number_of_pencils > 0:
            break
        else:
            number_of_pencils = input("The number of pencils should be positive\n")
            continue
    else:
        number_of_pencils = input("The number of pencils should be numeric\n")
        continue


current_player = input(f"Who will be first? ({name1}, {name2}):\n")
current_player = test_current_player(current_player, name1, name2)


while number_of_pencils > 0:
    for i in range(int(number_of_pencils)):
        print("|", end="")

    if current_player == name1:
        pencils_to_take = input(f"\n{current_player}\'s turn!\n")
        while pencils_to_take not in possible_values:
            pencils_to_take = input("Possible values: '1', '2', or '3'\n")
        while int(pencils_to_take) > int(number_of_pencils):
            pencils_to_take = input("Too many pencils were taken\n")
        number_of_pencils = int(number_of_pencils) - int(pencils_to_take)
        current_player = name2
    elif current_player == name2:
        print(f"\n{current_player}\'s turn!")
        jacks_choice = jacks_turn(number_of_pencils)
        print(jacks_choice)
        number_of_pencils = int(number_of_pencils) - int(jacks_choice)
        current_player = name1

print(f"{current_player} won")