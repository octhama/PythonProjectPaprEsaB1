import random

creer_un_perso = input("Voulez-vous créer un mon_personnage ? (O/N) ")
if creer_un_perso == "O":
    persos = []
    mon_perso = {}
    mon_perso['nom'] = input("Nom du personnage : ")
    mon_perso['sexe'] = input("Sexe du personnage : ")
    mon_perso['race'] = input("Race du personnage : ")
    mon_perso['classe'] = input("Classe du personnage : ")
    mon_perso['niveau'] = int(input("Niveau du personnage : "))
    mon_perso['pv'] = int(input("Points de vie du personnage : "))
    mon_perso['dv'] = int(input("Dégâts de l'arme du personnage : "))
    mon_perso['attaque'] = int(input("Attaque du personnage : "))
    mon_perso['defense'] = int(input("Défense du personnage : "))
    persos.append(mon_perso)
    print("Voici les caractéristiques de votre personnage :")
    print(mon_perso)
else:
    print("Ok, au revoir")

while True:
    mon_perso_a_combattre = {}
    mon_perso_a_combattre['nom'] = input("Nom du personnage à combattre : ")
    mon_perso_a_combattre['sexe'] = input("Sexe du personnage à combattre : ")
    mon_perso_a_combattre['race'] = input("Race du personnage à combattre : ")
    mon_perso_a_combattre['classe'] = input("Classe du personnage à combattre : ")
    mon_perso_a_combattre['niveau'] = random.randint(1, 10)
    mon_perso_a_combattre['pv'] = random.randint(1, 100)
    mon_perso_a_combattre['dv'] = random.randint(1, 10)
    mon_perso_a_combattre['attaque'] = random.randint(1, 10)
    mon_perso_a_combattre['defense'] = random.randint(1, 10)
    persos.append(mon_perso_a_combattre)
    print("Voici les caractéristiques du personnage à combattre :")
    print(mon_perso_a_combattre)

    print("{} versus {} !".format(mon_perso['nom'], mon_perso_a_combattre['nom']))
    print("Début du combat !")

    while mon_perso['pv'] > 0 and mon_perso_a_combattre['pv'] > 0:
        mon_perso['pv'] -= mon_perso_a_combattre['attaque'] - mon_perso['defense']
        mon_perso_a_combattre['pv'] -= mon_perso['attaque'] - mon_perso_a_combattre['defense']
        print("Dégâts infligés :")
        print("{} a infligé {} dégâts à {}.".format(mon_perso_a_combattre['nom'], mon_perso_a_combattre['attaque'] - mon_perso['defense'],
                                                    mon_perso['nom']))
        print("{} a infligé {} dégâts à {}.".format(mon_perso['nom'], mon_perso['attaque'] - mon_perso_a_combattre['defense'],
                                                    mon_perso_a_combattre['nom']))
        print("Points de vie restants :")
        print("{} a {} PV.".format(mon_perso['nom'], mon_perso['pv']))
        print("{} a {} PV.".format(mon_perso_a_combattre['nom'], mon_perso_a_combattre['pv']))
        if mon_perso['pv'] <= 0:
            print("{} a perdu le combat.".format(mon_perso['nom']))
        else:
            print("{} a gagné le combat.".format(mon_perso['nom']))

        repeat = input("Voulez-vous combattre un autre mon_personnage ? (O/N) ")
        if repeat == "N":
            break
        else:
            continue
