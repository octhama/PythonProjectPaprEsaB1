# Travail de classe en python pattern représentant le jeu Le Pendu
# superviser pas André NUYENS ESA Namur BAC 1 2022

mot = "oxymore"
tentative = 7
mot_masque = "_" * len(mot)
lettres_proposees = ""
print(mot_masque)
while tentative > 0:
    lettre = input("Indiquez votre lettre : ")
    while lettre in lettres_proposees:
        lettre = input("Indiquez une lettre non proposée : ")
    lettres_proposees += lettre
    if lettre not in mot:  # lettre non trouvée
        tentative -= 1
    else:
        for i in range(len(mot)):
            #  print(mot[i]) || auto incrémentition dans les cases indexées contenant chaque caractère
            if mot[i] == lettre:
                mot_masque = mot_masque[0:i] + lettre + mot_masque[i+1:]
    print(mot_masque)

