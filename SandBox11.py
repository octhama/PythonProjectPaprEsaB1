import random

create_perso = input("Voulez-vous créer un personnage ? (O/N) ")
if create_perso == "O":
    persos = []
    perso = {}
    perso['nom'] = input("Nom du personnage : ")
    perso['sexe'] = input("Sexe du personnage : ")
    perso['race'] = input("Race du personnage : ")
    perso['classe'] = input("Classe du personnage : ")
    perso['niveau'] = int(input("Niveau du personnage : "))
    perso['pv'] = int(input("Points de vie du personnage : "))
    perso['dv'] = int(input("Dégâts de l'arme du personnage : "))
    persos.append(perso)
    print(persos)

    perso_to_fight = {}
    perso_to_fight['nom'] = input("Nom du personnage à combattre : ")
    perso_to_fight['sexe'] = input("Sexe du personnage à combattre : ")
    perso_to_fight['race'] = input("Race du personnage à combattre : ")
    perso_to_fight['classe'] = input("Classe du personnage à combattre : ")
    perso_to_fight['niveau'] = random.randint(1, 10)
    perso_to_fight['pv'] = random.randint(1, 100)
    perso_to_fight['dv'] = random.randint(1, 10)
    persos.append(perso_to_fight)
    print(persos)
else:
    print("Ok, au revoir")

while perso['pv'] > 0 and perso_to_fight['pv'] > 0:
    perso['pv'] -= perso_to_fight['dv']
    perso_to_fight['pv'] -= perso['dv']
    print(f"Le personnage {perso['nom']} a subit {perso_to_fight['dv']} de dégats et a maintenant {perso['pv']} PV")
    print(
        f"Le personnage {perso_to_fight['nom']} a subit {perso['dv']} de dégats et a maintenant {perso_to_fight['pv']} PV")
if perso['pv'] <= 0:
    print(f"Le personnage {perso_to_fight['nom']} a gagné")
elif perso_to_fight['pv'] <= 0:
    print(f"Le personnage {perso['nom']} a gagné")
else:
    recommencer = input("Voulez-vous recommencer le combat ? (O/N) ")
    if recommencer == "O":
        perso['pv'] = int(input("Points de vie du personnage : "))
        perso_to_fight['niveau'] = random.randint(1, 10)
        perso_to_fight['pv'] = random.randint(1, 100)
        perso_to_fight['dv'] = random.randint(1, 10)
    else:
        print("Au revoir")
