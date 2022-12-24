# Fonction pour vérifier un prénom
def check_prenom(x_prenom):
    caractere_pas_ok = ""
    # Vérifie chaque caractère dans le prénom
    for c in x_prenom:
        # Si le caractère n'est pas alphabétique ou numérique, ajoute-le à la chaîne de caractères non valides
        if not c.isalnum():
            caractere_pas_ok += c
    # Si la chaîne de caractères non valides est vide, le prénom est valide
    # Sinon, elle contient les caractères non valides du prénom
    return caractere_pas_ok if caractere_pas_ok else True


# Fonction pour vérifier un nom
def check_nom(x_nom):
    caractere_pas_ok = ""
    # Vérifie chaque caractère dans le nom
    for c in x_nom:
        # Si le caractère n'est pas alphabétique ou numérique, ajoute-le à la chaîne de caractères non valides
        if not c.isalnum():
            caractere_pas_ok += c
    # Si la chaîne de caractères non valides est vide, le nom est valide
    # Sinon, elle contient les caractères non valides du nom
    return caractere_pas_ok if caractere_pas_ok else True


# Fonction pour vérifier une adresse
def check_adresse(x_adresse):
    # Si l'adresse est vide, renvoie False
    # Sinon, renvoie True
    return False if not x_adresse else True


# Fonction pour vérifier un email
def check_email(x_email):
    # Vérifie si l'email a le bon format
    if '@' in x_email and '.' in x_email:
        # Sépare le nom d'utilisateur et le domaine
        aka_utilisateur, nom_domaine = x_email.split('@')
        # Vérifie si le domaine à au moins un point
        if '.' in nom_domaine:
            return True
    return False


# Fonction pour vérifier un login
def check_login(x_login):
    caractere_pas_ok = ""
    # Vérifie chaque caractère dans le login
    for c in x_login:
        # Si le caractère n'est pas en minuscule ou n'est pas alphabétique ou numérique, ajoute-le à la chaîne de
        # caractères non valides
        if not c.islower() or not c.isalnum():
            caractere_pas_ok += c
    # Si la chaîne de caractères non valides est vide, le login est valide
    # Sinon, elle contient les caractères non valides du login
    return caractere_pas_ok if caractere_pas_ok else True


# Fonction pour vérifier un mot de passe
def check_mdp(x_mdp):
    # Récupère la longueur du mot de passe
    taille_mdp = len(x_mdp)

    # Si la longueur du mot de passe est inférieure à 10, renvoie True
    if taille_mdp < 10:
        return True

    # Initialise les compteurs pour les différents types de caractères
    minuscules = 0
    majuscules = 0
    chiffres = 0
    spacechars = 0

    # Vérifie chaque caractère dans le mot de passe
    for c in x_mdp:
        if c.islower():
            minuscules += 1
        elif c.isupper():
            majuscules += 1
        elif c.isdigit():
            chiffres += 1
        elif c.isalnum():
            spacechars += 1
    # Si au moins un compteur est supérieur à 0, renvoie True
    # Sinon, renvoie False
    return minuscules and majuscules and chiffres and spacechars


# Fonction pour vérifier si deux logins sont égaux
def utilisateur_login_check(utilisateur_x_login, utilisateur_y_login):
    # Renvoie True si les logins sont égaux, False sinon
    return utilisateur_x_login == utilisateur_y_login


# Affiche 100 étoiles sur une ligne
for i in range(100):
    print("*", end="")
print()

while True:
    try:
        # Demande le prénom du premier utilisateur
        utilisateur_1_prenom = input("Entrer le prénom du premier utilisateur: ")
        # Vérifie si le prénom est valide
        resultat = check_prenom(utilisateur_1_prenom)
        if resultat is True:
            print("Prénom valide")
            break
        else:
            print(f"Prénom invalide, caractères non valides: {resultat}")
    except ValueError:
        continue

while True:
    try:
        # Demande le nom du premier utilisateur
        utilisateur_1_nom = input("Entrer le nom du premier utilisateur: ")
        # Vérifie si le nom est valide
        resultat = check_nom(utilisateur_1_nom)
        if resultat is True:
            print("Nom valide")
            break
        else:
            print(f"Nom invalide, caractères non valides: {resultat}")
    except ValueError:
        continue

while True:
    try:
        # Demande l'adresse du premier utilisateur
        utilisateur_1_adresse = input("Entrer l'adresse du premier utilisateur: ")
        # Vérifie si l
        # Demande le login du premier utilisateur
        utilisateur_1_login = input("Entrer le login du premier utilisateur: ")
        # Vérifie si le login est valide
        resultat = check_login(utilisateur_1_login)
        if resultat is True:
            print("Login valide")
            break
        else:
            print(f"Login invalide, caractères non valides: {resultat}")
    except ValueError:
        continue

while True:
    try:
        # Demande le mot de passe du premier utilisateur
        utilisateur_1_mdp = input("Entrer le mot de passe du premier utilisateur: ")
        # Vérifie si le mot de passe est valide
        if check_mdp(utilisateur_1_mdp):
            print("Mot de passe valide")
            break
        else:
            print("Mot de passe non valide")
    except ValueError:
        continue

while True:
    try:
        # Demande le prénom du second utilisateur
        utilisateur_2_prenom = input("Entrer le prénom du second utilisateur: ")
        # Vérifie si le prénom est valide
        resultat = check_prenom(utilisateur_2_prenom)
        if resultat is True:
            print("Prénom valide")
            break
        else:
            print(f"Prénom invalide, caractères non valides: {resultat}")
    except ValueError:
        continue

while True:
    try:
        # Demande le nom du second utilisateur
        utilisateur_2_nom = input("Entrer le nom du second utilisateur: ")
        # Vérifie si le nom est valide
        resultat = check_nom(utilisateur_2_nom)
        if resultat is True:
            print("Nom valide")
            break
        else:
            print(f"Nom invalide, caractères non valides: {resultat}")
    except ValueError:
        continue

while True:
    try:
        # Demande l'adresse du second utilisateur
        utilisateur_2_adresse = input("Entrer l'adresse du second utilisateur: ")
        # Vérifie si l'adresse est valide
        if check_adresse(utilisateur_2_adresse):
            print("Adresse valide")
            break
        else:
            print("Adresse non valide")
    except ValueError:
        continue

while True:
    try:
        # Demande l'email du second utilisateur
        utilisateur_2_email = input("Entrer l'email du second utilisateur: ")
        # Vérifie si l'email est valide
        if check_email(utilisateur_2_email):
            print("Email valide")
            break
        else:
            print("Email non valide")
            print(f"Login invalide, caractères non valides: {resultat}")
    except ValueError:
        continue

while True:
    try:
        # Demande le mot de passe du second utilisateur
        utilisateur_2_mdp = input("Entrer le mot de passe du second utilisateur: ")
        # Vérifie si le mot de passe est valide
        if check_mdp(utilisateur_2_mdp):
            print("Mot de passe valide")
            break
        else:
            print("Mot de passe non valide")
    except ValueError:
        continue

# Vérifie si les logins des deux utilisateurs sont égaux
if utilisateur_login_check(utilisateur_1_login, utilisateur_2_login):
    print("Les logins sont égaux")
else:
    print("Les logins sont différents")
