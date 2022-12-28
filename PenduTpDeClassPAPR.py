# Travail de classe en python (Pattern représentant le jeu Le Pendu)
#  Superviser par André NUYENS ESA-Namur BAC-1-INFO-2022
# Pattern complèté par Hasler TEHOU dans le cadre du Travail Individuel en PAPR-ESA-Namur

def check_game_rules(x_tentative, x_mot_masque):
    while x_tentative > 0 and "_" in x_mot_masque:
        return True


def check_lettre_proposees(x_lettre, x_lettre_proposees):
    x_lettre_proposees += x_lettre
    return False


def check_lettre_dans_mot(x_lettre, x_mot):
    if x_lettre in x_mot:
        return True


def check_mot_masque(x_mot_masque):
    if "_" not in x_mot_masque:
        return True
    else:
        return False

# À revoir avec le Professeur!!!
# def remplace_lettre_proposees(x_c, x_mot, x_lettre, x_mot_masque):
#    if x_mot[x_c] == x_lettre:
#        x_mot_masque = x_mot_masque[:x_c] + x_lettre + x_mot_masque[x_c + 1:]


mot = "oxymore"
tentative = 7
mot_masque = "_" * len(mot)
lettres_proposees = ""

while check_game_rules(tentative, mot_masque):
    # Print current state of the game
    print(mot_masque)  # affiche le mot masqué à chaque tour de boucle
    print(f"Tentatives restantes: ", tentative)
    # print("Lettres proposées: ", lettres_proposees)

    lettre = input("Indiquez votre lettre : ")

    # Vérifier si la lettre a déjà été proposée
    while check_lettre_proposees(lettre, lettres_proposees):
        lettre = input("Indiquez une lettre non proposée : ")  # Ajouter la lettre aux lettres déjà proposées
        continue
    # Vérifier si la lettre se trouve dans le mot à deviner
    if check_lettre_dans_mot(lettre, mot):
        for i in range(len(mot)):
            if mot[i] == lettre:
                mot_masque = mot_masque[:i] + lettre + mot_masque[i + 1:]  # remplace-le "_" par la lettre trouvée
    else:
        tentative -= 1  # lettre non trouvée décrémente d'une tentative

# Afficher le résultat final
if check_mot_masque(mot_masque):  # le mot a été trouvé
    exit("Félicitations ! Vous avez trouvé le mot")
else:  # le mot n'a pas été trouvé
    print("Désolé, vous avez perdu. Le mot était : ", mot)
    exit()
