# Imports --------------------------------------------------------------------------------
from random import randint, choice


# Functions -------------------------------------------------------------------------------


def creation_character():
    character = {'name': input("Enter your character's name \n"),
                 'gender': input("Enter your character's gender : M/F/X\n")}

    # Race
    choice_race = input("Enter your character's race : 1 = Human, 2 = Elf, 3 = Dwarf, 4 = Gnome\n")
    while not choice_race.isdigit() or int(choice_race) not in range(1, 5):
        choice_race = input("Enter your character's race : 1 = Human, 2 = Elf, 3 = Dwarf, 4 = Gnome\n")
    choice_race = int(choice_race)
    if choice_race == 1:
        character["race"] = "Human"
    elif choice_race == 2:
        character["race"] = "Elf"
    elif choice_race == 3:
        character["race"] = "Dwarf"
    elif choice_race == 4:
        character["race"] = "Gnome"
    else:
        print("An error was occurred.")

    # Initialization of lvl, health and hd.
    character['level'] = randint(1, 10)
    character['health'] = 0
    dv = 0

    # Class
    choice_class = input("Enter your character's race : 1 = Warrior, 2 = Priest, 3 = Thief, 4 = Magician\n")
    while not choice_class.isdigit() or int(choice_class) not in range(1, 5):
        choice_class = input("Enter your character's race : 1 = Warrior, 2 = Priest, 3 = Thief, 4 = Magician\n")
    choice_class = int(choice_class)
    if choice_class == 1:
        character["class"] = "Warrior"
        dv = 10
    elif choice_class == 2:
        character["class"] = "Priest"
        dv = 8
    elif choice_class == 3:
        character["class"] = "Thief"
        dv = 6
    elif choice_class == 4:
        character["class"] = "Magician"
        dv = 4
    else:
        print("An error was occurred.")

    # Other characteristics
    character['health'] = randint(int(dv / 2), dv) * character['level']
    character['attack'] = randint(1, 5)
    character['defense'] = randint(1, 3)
    print("Your character is created !\n" + str(character) + "\n")
    return character


def bot_creation():
    gender = ['M', 'F', 'X']  # Be inclusive (LOL)
    race = ['Human', 'Elf', 'Dwarf', 'Gnome']
    cla = ['Warrior', 'Priest', 'Thief', 'Magician']
    random_names = ["Potatoes", "Banana", "Egg man", "Marsupilami", "Monkhu", "Tonkhu", "Sonkhu"]

    # Bot init
    bot = {'name': choice(random_names), 'gender': choice(gender), 'race': choice(race), 'level': randint(1, 10),
           'health': 0,
           'class': choice(cla), 'attack': randint(1, 3), 'defense': randint(1, 3)}
    # Health's bot init
    dv = 0
    if bot['class'] == 'Warrior':
        dv = 10
    elif bot['class'] == 'Priest':
        dv = 8
    elif bot['class'] == 'Thief':
        dv = 6
    elif bot['class'] == 'Magician':
        dv = 4
    bot['health'] = randint(1, dv) * bot['level']
    print("The bot is created !\n" + str(bot) + "\n")
    return bot


def game_generator():
    winner = ""
    game_mode = input("Enter 1 for 1v1 or 2 for 1vCPU :\n")
    while game_mode not in ('1', '2'):
        game_mode = input("Enter 1 for 1v1 or 2 for 1vCPU :\n")
    player_1 = creation_character()
    if game_mode == '1':
        player_2 = creation_character()
    else:
        player_2 = bot_creation()
    print("The battle begin !\n ")
    print("-" * 100)
    print(player_1['name'] + f" ({player_1['gender']}) : " + player_1['race'] + " " + player_1['class'] + ", level " +
          str(player_1['level']) + " // Versus  // " + player_2['name'] + f" ({player_2['gender']}) : " + player_2[
              'race'] + " " +
          player_2['class'] + ", level " + str(player_2['level']))
    print("The battle begin !\n ")
    print("-" * 100)
    if randint(1, 2) != 1:  # Choose first player
        player_2, player_1 = player_1, player_2

    while int(player_1['health']) > 0 and int(player_2['health']) > 0:
        bonus_att = randint(0, 2)
        bonus_def = randint(0, 2)
        player_1['attack'] = int(player_1['attack']) + bonus_att
        player_2['defense'] = int(player_2['defense']) + bonus_def
        print(f"{player_1['name']}'s attack: " + str(player_1['attack']) + ", " + f"{player_2['name']}'s def : " + str(
            player_2['defense']))
        print(
            f"{player_1['name']} attacks {player_2['name']} with a value of {int(player_1['attack']) - int(player_2['defense'])} points \n")
        print("-" * 100)
        if int(player_2['defense']) < int(player_1['attack']):
            player_2['health'] -= (player_1['attack'] - player_2['defense'])
        elif int(player_2['defense']) >= int(player_1['attack']):
            print(f"Extra defense save {player_2['name']}! \n")
            print("-" * 100)
        player_1['attack'] = int(player_1['attack']) - bonus_att
        player_2['defense'] = int(player_2['defense']) - bonus_def
        print(f"{player_2['name']}'s Health = {player_2['health']} \n")
        print("-" * 100)
        if int(player_1['health']) > 0 and int(player_2['health']) > 0:
            still_fight = input("Is that all your skills ? Still want to fight ? if yes, press 'o' else any other key :"
                                "\n")
            if still_fight not in ('o', 'O'):
                player_1['health'] = 0
                print("Fight ends in a forfeit. " + player_2['name'] + " is the winner")
            else:
                # Change player 1 for the next attack
                player_2, player_1 = player_1, player_2
        else:
            if int(player_1['health']) > int(player_2['health']):
                winner = player_1['name']
            else:
                winner = player_2['name']
    return winner


# Main code ------------------------------------------------------------------------------
print("The winner is :" + game_generator())

while True:
    replay = input("Do you want to play again ? Y/N\n")
    if replay in ('Y', 'y'):
        print("The winner is :" + game_generator())
    else:
        exit("Thanks for playing !")


