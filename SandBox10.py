import random

create_perso = input("Voulez-vous créer un personnage ? (O/N) ")
if create_perso == "O":
    perso = {}
    perso['nom'] = input("Nom du personnage : ")
    perso['sexe'] = input("Sexe du personnage : ")
    perso['race'] = input("Race du personnage : ")
    perso['classe'] = input("Classe du personnage : ")
    perso['niveau'] = int(input("Niveau du personnage : "))
    perso['pv'] = int(input("Points de vie du personnage : "))
    perso['dv'] = int(input("Dégâts de l'arme du personnage : "))

    perso_to_fight = {}
    perso_to_fight['nom'] = input("Nom du personnage à combattre : ")
    perso_to_fight['sexe'] = input("Sexe du personnage à combattre : ")
    perso_to_fight['race'] = input("Race du personnage à combattre : ")
    perso_to_fight['classe'] = input("Classe du personnage à combattre : ")
    perso_to_fight['niveau'] = random.randint(1, 10)
    perso_to_fight['pv'] = random.randint(1, 100)
    perso_to_fight['dv'] = random.randint(1, 10)

    while perso['pv'] > 0 and perso_to_fight['pv'] > 0:
        perso_to_fight['pv'] -= perso['dv']
        print(perso_to_fight['nom'], "a subi", perso['dv'], "points de dégâts. Il lui reste", perso_to_fight['pv'],
              "points de vie.")
        perso['pv'] -= perso_to_fight['dv']
        print(perso['nom'], "a subi", perso_to_fight['dv'], "points de dégâts. Il lui reste", perso['pv'],
              "points de vie.")

    if perso['pv'] > 0:
        print(perso['nom'], "a gagné !")
    else:
        print(perso_to_fight['nom'], "a gagné !")
else:
    print("Ok, au revoir")
