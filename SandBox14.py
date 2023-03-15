# Program : SandBox14
# Programmation procédurale sur un jeu de combat
# Version interactive du jeu de combat

from random import randint
from random import choice

choix_creer_un_perso = input("Voulez-vous créer un personnage ? (O/N) ")  # Demande à l'utilisateur s'il veut créer
# un personnage
if choix_creer_un_perso == "O" or choix_creer_un_perso == "o":  # Si l'utilisateur veut créer un personnage
    # Création d'un dictionnaire contenant les caractéristiques des classes avec pdv = dv * niveau
    dico_de_classes = {"Guerrier": {"niveau": 1, "pdv": 0, "dv": 5, "attaque": 5, "defense": 5},
                       "Mage": {"niveau": 2, "pdv": 0, "dv": 10, "attaque": 5, "defense": 5},
                       "Voleur": {"niveau": 3, "pdv": 0, "dv": 15, "attaque": 5, "defense": 5},
                       "Paladin": {"niveau": 4, "pdv": 0, "dv": 20, "attaque": 5, "defense": 5},
                       "Pretre": {"niveau": 5, "pdv": 0, "dv": 25, "attaque": 5, "defense": 5}}

    persos = []  # Liste des personnages créés par l'utilisateur
    mon_perso = {"nom": input("Nom du personnage : "), "sexe": input("Sexe du personnage : "),
                 "race": input("Race du personnage : "), "classe": input(
            "Classe du personnage : ")}  # Dictionnaire des caractéristiques du personnage créé par l'utilisateur
    while mon_perso["classe"] not in dico_de_classes:  # Vérification que la classe est bien dans le dictionnaire
        print("Tu peux être : Guerrier, Mage, Voleur, Paladin ou Pretre")
        mon_perso["classe"] = input("Choisis ta classe favorite parmi les précédente : ")
    mon_perso["niveau"] = dico_de_classes[mon_perso["classe"]]["niveau"]  # Ajout du niveau du personnage dans le
    # dictionnaire
    # Calcul des points de vie du personnage
    mon_perso["pdv"] = dico_de_classes[mon_perso["classe"]]["dv"] * dico_de_classes[mon_perso["classe"]]["niveau"]
    mon_perso["dv"] = dico_de_classes[mon_perso["classe"]]["dv"]  # Ajout des dégâts de l'arme du personnage dans le
    # dictionnaire
    mon_perso["attaque"] = dico_de_classes[mon_perso["classe"]]["attaque"]  # Ajout de l'attaque du personnage dans le
    # dictionnaire
    mon_perso["defense"] = dico_de_classes[mon_perso["classe"]]["defense"]  # Ajout de la défense du personnage dans le
    # dictionnaire
    persos.append(mon_perso)  # Ajout du personnage dans la liste des personnages
    print("Voici les caractéristiques de ton personnage :")  # Affichage des caractéristiques du personnage
    print(mon_perso)  # Affichage des caractéristiques du personnage
else:
    exit("Ok, au revoir ;)")  # Fin du programme

# Création d'un second personnage si l'utilisateur le souhaite
creer_second_perso = input("Voulez-vous créer un second personnage ? (O/N) ")
if creer_second_perso == "O" or creer_second_perso == "o":
    mon_perso = {"nom": input("Nom du personnage : "), "sexe": input("Sexe du personnage : "),
                 "race": input("Race du personnage : "),
                 "classe": input("Classe du personnage : ")}  # Dictionnaire des caractéristiques du personnage
    while mon_perso["classe"] not in dico_de_classes:  # Vérification que la classe est bien dans le dictionnaire
        print("Tu peux être : Guerrier, Mage, Voleur, Paladin, Pretre")
        mon_perso["classe"] = input("Choisis ta classe favorite parmi les précédente : ")
    mon_perso["niveau"] = dico_de_classes[mon_perso["classe"]]["niveau"]  # Ajout du niveau du personnage dans le
    # dictionnaire
    mon_perso["dv"] = dico_de_classes[mon_perso["classe"]]["dv"]  # Ajout des dégâts de l'arme du personnage dans le
    # dictionnaire
    mon_perso["pdv"] = dico_de_classes[mon_perso["classe"]]["dv"] * dico_de_classes[mon_perso["classe"]][
        "niveau"]  # Ajout des points de vie du personnage dans le dictionnaire en fonction de la classe choisie et du
    # niveau
    mon_perso["attaque"] = dico_de_classes[mon_perso["classe"]]["attaque"]  # Ajout de l'attaque du personnage dans le
    # dictionnaire
    mon_perso["defense"] = dico_de_classes[mon_perso["classe"]]["defense"]  # Ajout de la défense du personnage dans le
    # dictionnaire
    persos.append(mon_perso)  # Ajout du personnage dans la liste des personnages
    print("Voici les caractéristiques de ton personnage :")  # Affichage des caractéristiques du personnage
    print(mon_perso)  # Affichage des caractéristiques du personnage
    print("Voici les noms des personnages créés: ", end="\n")
    for perso in persos:
        print(perso["nom"], end="\n")  # Affichage des noms des personnages créés par l'utilisateur

# Création d'un personnage à combattre si l'utilisateur le souhaite
choix_creer_un_personnage_a_combattre = input("Voulez-vous créer un personnage à combattre ? (O/N) ")
if choix_creer_un_personnage_a_combattre == "O" or choix_creer_un_personnage_a_combattre == "o":
    nom = ["Gandalf", "Aragorn", "Legolas", "Gimli", "Frodon", "Sam", "Gollum", "Sauron", "Saroumane", "Boromir", "Pippin"]
    sexe = ["Homme", "Femme"]
    race = ["Humain", "Elfe", "Nain", "Orc"]
    while True:
        perso_a_combattre = {"nom": choice(nom),
                             "sexe": choice(sexe),
                             "race": choice(race), "classe": choice(
                list(dico_de_classes.keys()))}  # Dictionnaire des caractéristiques du personnage à combattre
        # dictionnaire
        perso_a_combattre["niveau"] = dico_de_classes[perso_a_combattre["classe"]]["niveau"]  # Ajout du niveau du
        # personnage à combattre dans le dictionnaire
        perso_a_combattre["dv"] = dico_de_classes[perso_a_combattre["classe"]]["dv"]  # Ajout des dégâts de l'arme du
        # personnage à combattre dans le dictionnaire
        perso_a_combattre["pdv"] = dico_de_classes[perso_a_combattre["classe"]]["dv"] * dico_de_classes[
            perso_a_combattre["classe"]]["niveau"]
        perso_a_combattre["attaque"] = dico_de_classes[perso_a_combattre["classe"]]["attaque"]  # Ajout de l'attaque du
        # personnage à combattre dans le dictionnaire
        perso_a_combattre["defense"] = dico_de_classes[perso_a_combattre["classe"]]["defense"]  # Ajout de la défense du
        # personnage à combattre dans le dictionnaire
        persos.append(perso_a_combattre)  # Ajout du personnage à combattre dans la liste des personnages
        print("Voici les caractéristiques du personnage à combattre :")  # Affichage des caractéristiques du
        # personnage à combattre
        print(perso_a_combattre)  # Affichage des caractéristiques du personnage à combattre
        print("Voici les noms des personnages créés: ", end="\n")
        for perso in persos:
            print(perso["nom"], end="\n")  # Affichage des noms des personnages créés par l'utilisateur
        choix_perso = input("Quel personnage veux-tu utiliser ? ")
        for perso in persos:
            if perso["nom"] == choix_perso:
                mon_perso = perso
                break
        choix_perso = input("Quel personnage veux-tu combattre ? ")
        for perso in persos:
            if perso["nom"] == choix_perso:
                perso_a_combattre = perso
                break

        # Début du combat entre les deux personnages choisis par l'utilisateur
        print("C'est parti pour le combat !")
        print(f"{mon_perso['nom']} versus {perso_a_combattre['nom']} !")

        while mon_perso["pdv"] > 0 and perso_a_combattre["pdv"] > 0:
            print("C'est à", mon_perso["nom"], "de jouer")  # Affiche le nom du personnage qui doit jouer
            mon_perso["attaque"] = int(input("Puissance d'attaque : "))
            while mon_perso["attaque"] < 1 or mon_perso["attaque"] > dico_de_classes[mon_perso["classe"]]["attaque"]:
                print("Ton attaque doit être comprise entre 1 et", dico_de_classes[mon_perso["classe"]]["attaque"])
                mon_perso["attaque"] = int(input("Puissance d'attaque : "))

            mon_perso["defense"] = int(input("Defense : "))
            while mon_perso["defense"] < 1 or mon_perso["defense"] > dico_de_classes[mon_perso["classe"]]["defense"]:
                print("Ta défense doit être comprise entre 1 et", dico_de_classes[mon_perso["classe"]]["defense"])
                mon_perso["defense"] = int(input("Defense : "))

            defense_ennemi = randint(1, dico_de_classes[perso_a_combattre["classe"]]["defense"])  # Défense de l'ennemi
            # aléatoire entre 1 et la défense de l'ennemi (défense de l'ennemi = 1)

            perso_a_combattre["pdv"] -= mon_perso["attaque"] - defense_ennemi  # Calcul des points de vie du personnage
            # à combattre en fonction de l'attaque du personnage et de la défense de l'ennemi (défense de l'ennemi = 1)

            print(perso_a_combattre["nom"], "a maintenant", perso_a_combattre["pdv"], "points de vie")  # Affiche les
            # points de vie du personnage à combattre ii les points de vie du personnage à combattre sont inférieurs
            # ou égaux à 0 alors on sort de la boucle while
            if perso_a_combattre["pdv"] <= 0:
                print("Le combat est terminé !" + "\n" + mon_perso["nom"] + " a gagné !" + " " +
                      perso_a_combattre["nom"] + " est K.O :'(")  # Affiche le nom du personnage qui a gagné
                break  # Sort de la boucle while
            else:
                print("C'est à", perso_a_combattre["nom"], "de jouer")  # Affiche le nom du personnage qui doit jouer

            # Calcul des points de vie du personnage en fonction de l'attaque, de la défense et des dégâts de
            # l'arme de l'ennemi
            attaque_ennemi = randint(1, dico_de_classes[perso_a_combattre["classe"]]["attaque"])
            print(perso_a_combattre["nom"], "attaque avec une attaque de",
                  attaque_ennemi)  # Affiche l'attaque de l'ennemi
            print(perso_a_combattre["nom"], "a une défense de", defense_ennemi)  # Affiche la défense de
            # l'ennemi
            degats_ennemi = dico_de_classes[perso_a_combattre["classe"]]["dv"]
            print(perso_a_combattre["nom"], "a une arme qui fait", degats_ennemi,
                  "dégâts")  # Affiche les dégâts de l'arme de l'ennemi
            mon_perso["pdv"] -= attaque_ennemi - mon_perso["defense"]  # Calcul des points de vie du personnage en
            # fonction de l'attaque, de la défense et des dégâts de l'arme de l'ennemi

            print(mon_perso["nom"], "a maintenant", mon_perso["pdv"],
                  "points de vie")  # Affiche les points de vie du personnage
            # Si les points de vie du personnage sont inférieurs ou égaux à 0 alors on sort de la boucle while
            if mon_perso["pdv"] <= 0:
                print("Le combat est terminé !" + "\n" + perso_a_combattre["nom"] + " a gagné !" + " " +
                      "Ton personnage" + " " + mon_perso["nom"] + " est K.O :'(")
                break  # Sort de la boucle while
            else:
                continue
        while True:
            choix = input("Voulez-vous recommencer un combat ? (O/N) ")
            if choix == "O" or choix == "o":
                break
            elif choix == "N" or choix == "n":
                exit("Au revoir ;)")
            else:
                print("Veuillez saisir O ou N")
else:
    exit("Au revoir ;)")
