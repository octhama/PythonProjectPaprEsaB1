# Définition de la liste des mots possibles
import random

mots = ["pendu", "ordinateur", "programmation", "python"]

# Choisir un mot au hasard
mot_a_deviner = mots[random.randint(0, len(mots) - 1)]

# Initialiser les variables pour la boucle de jeu
erreurs_restantes = 6
lettres_trouvees = ["_" for lettre in mot_a_deviner]
lettres_deja_proposees = []

# Boucle principale du jeu
while erreurs_restantes > 0 and "_" in lettres_trouvees:
    # Afficher l'état actuel du mot à deviner
    print("Mot à deviner : ", " ".join(lettres_trouvees))

    # Demander à l'utilisateur de proposer une lettre
    lettre = input("Proposez une lettre : ")

    # Vérifier si la lettre a déjà été proposée
    if lettre in lettres_deja_proposees:
        print("Vous avez déjà proposé cette lettre.")
        continue

    # Ajouter la lettre aux lettres déjà proposées
    lettres_deja_proposees.append(lettre)

    # Vérifier si la lettre se trouve dans le mot à deviner
    if lettre in mot_a_deviner:
        # Mettre à jour les lettres trouvées
        for i in range(len(mot_a_deviner)):
            if mot_a_deviner[i] == lettre:
                lettres_trouvees[i] = lettre
    else:
        # Décrémenter le nombre d'erreurs restantes
        erreurs_restantes -= 1

# Afficher le résultat final
if "_" not in lettres_trouvees:
    print("Félicitations ! Vous avez trouvé le mot : ", mot_a_deviner)
else:
    print("Désolé, vous avez perdu. Le mot était : ", mot_a_deviner)
