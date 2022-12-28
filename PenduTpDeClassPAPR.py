# Travail de classe en python pattern représentant le jeu Le Pendu
# superviser pas André NUYENS ESA Namur BAC 1 2022

mot = "oxymore"
tentative = 7
mot_masque = "_" * len(mot)
lettres_proposees = ""

while tentative > 0 and "_" in mot_masque:
    # Print current state of the game
    print(mot_masque)  # affiche le mot masqué à chaque tour de boucle
    print(f"Tentatives restantes: {tentative}")
    print(f"Lettres proposées: {lettres_proposees}")

    lettre = input("Indiquez votre lettre : ")

    # Vérifier si la lettre a déjà été proposée
    while lettre in lettres_proposees:
        lettre = input("Indiquez une lettre non proposée : ")
        lettres_proposees += lettre  # Ajouter la lettre aux lettres déjà proposées
        continue
    # Vérifier si la lettre se trouve dans le mot à deviner
    if lettre in mot:
        for i in range(len(mot)):
            if mot[i] == lettre:
                mot_masque = mot_masque[:i] + lettre + mot_masque[i + 1:]  # remplace-le "_" par la lettre trouvée
    else:
        tentative -= 1  # lettre non trouvée décrémente d'une tentative

# Afficher le résultat final
if "_" not in mot_masque:  # le mot a été trouvé
    exit("Félicitations ! Vous avez trouvé le mot")
else:  # le mot n'a pas été trouvé
    print("Désolé, vous avez perdu. Le mot était : ", mot)
    exit()
