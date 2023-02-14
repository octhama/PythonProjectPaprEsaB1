import random
from random import choice

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
    print(choice(persos))
else:
    print("Ok, au revoir")

# Ici, je dois créer des personnages et le stocker dans une liste...ensuite je dois choisir un personnage dans
# la liste au hasard et le stocker dans une variable perso_to_fight
# ensuite je dois créer un personnage à combattre et le stocker dans une variable perso_to_fight
# ensuite je dois comparer les pv de perso et perso_to_fight et afficher le gagnant

perso_to_fight = {}
perso_to_fight['nom'] = input("Nom du personnage à combattre : ")
perso_to_fight['sexe'] = input("Sexe du personnage à combattre : ")
perso_to_fight['race'] = input("Race du personnage à combattre : ")
perso_to_fight['classe'] = input("Classe du personnage à combattre : ")
perso_to_fight['niveau'] = random.randint(1, 10)
perso_to_fight['pv'] = random.randint(1, 100)
perso_to_fight['dv'] = random.randint(1, 10)

if perso['pv'] > perso_to_fight['pv']:
    print("Le personnage a gagné !")
else:
    print("Le personnage à combattre a gagné !")
