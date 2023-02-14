# Program: SandBox14
# Programmation procédurale sur un jeu de combat

import random

choix_creer_un_perso = input(
    "Voulez-vous créer un personnage ? (O/N) ")  # Demande à l'utilisateur s'il veut créer un personnage
if choix_creer_un_perso == "O":
    persos = []  # Liste des personnages
    mon_perso = {}  # Dictionnaire des caractéristiques du personnage
    mon_perso["nom"] = input("Nom du personnage : ")  # Ajout du nom du personnage dans le dictionnaire
    mon_perso["sexe"] = input("Sexe du personnage : ")  # Ajout du sexe du personnage dans le dictionnaire
    mon_perso["race"] = input("Race du personnage : ")
    mon_perso["classe"] = input("Classe du personnage : ")

    mon_perso["niveau"] = int(input("Niveau du personnage : "))
    while mon_perso["niveau"] < 1 or mon_perso["niveau"] > 10:  # Vérification que le niveau est compris entre 1 et 10
        print("Le niveau doit être compris entre 1 et 10")
        mon_perso["niveau"] = int(input("Niveau du personnage : "))

    mon_perso["pv"] = int(input("Points de vie du personnage : "))
    while mon_perso["pv"] < 1 or mon_perso["pv"] > 100:  # Vérification que les points de vie sont compris entre 1 et 100
        print("Les points de vie doivent être compris entre 1 et 100")
        mon_perso["pv"] = int(input("Points de vie du personnage : "))

    mon_perso["dmg"] = int(input("Dégâts de l'arme du personnage : "))
    while mon_perso["dmg"] < 1 or mon_perso["dmg"] > 10:  # Vérification que les dégâts sont compris entre 1 et 10
        print("Les dégâts de l'arme doivent être compris entre 1 et 10")
        mon_perso["dmg"] = int(input("Dégâts de l'arme du personnage : "))

    mon_perso["attaque"] = int(input("Attaque du personnage : "))
    while mon_perso["attaque"] < 1 or mon_perso["attaque"] > 10:  # Vérification que l'attaque est comprise entre 1 et 10
        print("L'attaque doit être comprise entre 1 et 10")
        mon_perso["attaque"] = int(input("Attaque du personnage : "))

    mon_perso["defense"] = int(input("Défense du personnage : "))
    while mon_perso["defense"] < 1 or mon_perso["defense"] > 10:  # Vérification que la défense est comprise entre 1 et 10
        print("La défense doit être comprise entre 1 et 10")
        mon_perso["defense"] = int(input("Défense du personnage : "))
    persos.append(mon_perso)  # Ajout du personnage dans la liste des personnages
    print("Voici les caractéristiques de votre personnage :")  # Affichage des caractéristiques du personnage
    print(mon_perso)  # Affichage des caractéristiques du personnage
else:
    exit("Ok, au revoir")

while True:
    perso_a_combattre = {}  # Dictionnaire des caractéristiques du personnage à combattre
    perso_a_combattre["nom"] = input("Nom du personnage à combattre : ")
    perso_a_combattre["sexe"] = input("Sexe du personnage à combattre : ")
    perso_a_combattre["race"] = input("Race du personnage à combattre : ")
    perso_a_combattre["classe"] = input("Classe du personnage à combattre : ")
    perso_a_combattre["niveau"] = random.randint(1, 10)
    perso_a_combattre["pv"] = random.randint(1, 100)
    perso_a_combattre["dmg"] = random.randint(1, 10)
    perso_a_combattre["attaque"] = random.randint(1, 10)  # Ajout de l'attaque du personnage à combattre
    perso_a_combattre["defense"] = random.randint(1, 10)  # Ajout de la défense du personnage à combattre
    persos.append(perso_a_combattre)  # Ajout du personnage à combattre dans la liste des personnages
    print("Voici les caractéristiques du personnage à combattre :")  # Affichage des caractéristiques du personnage à
    # combattre
    print(perso_a_combattre)  # Affichage des caractéristiques du personnage à combattre

    print("{} versus {} !".format(mon_perso["nom"], perso_a_combattre["nom"]))
    print("C'est parti pour le combat !")

    while mon_perso["pv"] > 0 and perso_a_combattre["pv"] > 0:  # Tant que les pv des deux personnages sont
        # supérieurs à 0
        # On demande à l'utilisateur de saisir son attaque et sa défense et on calcule les points de vie du personnage à
        # combattre
        print("C'est à", mon_perso["nom"], "de jouer")  # Affiche le nom du personnage qui doit jouer
        attaque = int(input("Quelle est votre attaque ? : "))  # Demande à l'utilisateur de saisir son attaque
        defense = int(input("Quelle est votre défense ? : "))  # Demande à l'utilisateur de saisir sa défense
        perso_a_combattre["pv"] -= attaque - perso_a_combattre[
            "defense"]  # Calcul des points de vie du personnage à combattre en fonction de l'attaque et de la
        # défense du personnage
        print(perso_a_combattre["nom"], "a maintenant", perso_a_combattre["pv"],
              "points de vie")  # Affiche les points de vie du personnage à combattre
        # Si les points de vie du personnage à combattre sont inférieurs ou égaux à 0 alors on sort de la boucle while
        if perso_a_combattre["pv"] <= 0:
            exit("Le combat est terminé !" + "\n" + mon_perso["nom"] + " a gagné !" + " " + perso_a_combattre["nom"] +
                 " est K.O :(")  # Affiche le nom du personnage qui a gagné

        # On génère aléatoirement l'attaque et la défense de l'ennemi et on calcule les points de vie du personnage en
        # fonction de l'attaque et de la défense de l'ennemi et on affiche les points de vie du personnage à combattre
        print("C'est à", perso_a_combattre["nom"], "de jouer")  # Affiche le nom du personnage qui doit jouer
        attaque_ennemi = random.randint(1, 10)  # Génère un nombre aléatoire entre 1 et 10
        print("L'ennemi attaque avec une attaque de", attaque_ennemi)  # Affiche l'attaque de l'ennemi
        defense_ennemi = random.randint(1, 10)  # Génère un nombre aléatoire entre 1 et 10
        print("L'ennemi défend avec une défense de", defense_ennemi)  # Affiche la défense de l'ennemi
        mon_perso["pv"] -= attaque_ennemi - defense  # Calcul des points de vie du personnage en fonction de
        # l'attaque et de la défense du personnage à combattre
        print(mon_perso["nom"], "a maintenant", mon_perso["pv"],
              "points de vie")  # Affiche les points de vie du personnage
        # Si les points de vie du personnage sont inférieurs ou égaux à 0 alors on sort de la boucle while
        if mon_perso["pv"] <= 0:
            exit("Le combat est terminé !" + "\n" + perso_a_combattre["nom"] + " a gagné !" + " " + mon_perso["nom"] +
                 " est K.O :(")  # Affiche le nom du personnage qui a gagné

    continuer = input("Voulez-vous faire un autre combat ? (O/N) ")  # Demande à l'utilisateur s'il veut faire un
    # autre combat
    if continuer == "O":  # Si l'utilisateur veut faire un autre combat
        continue
    else:
        exit("Au revoir !")
