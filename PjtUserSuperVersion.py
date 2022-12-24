# Fonction par variable pour vérifier un prénom
def check_prenom(x_prenom):
    # Vérifie chaque caractère dans le prénom
    caractere_pas_ok = ""
    # Si le caractère n'est pas alphabétique ou numérique, ajoute-le à la chaîne de caractères non valides
    for c in x_prenom:
        if not c.isalnum():
            caractere_pas_ok += c
    # Si la chaîne de caractères non valides est vide, le prénom est valide
    # Sinon, elle contient les caractères non valides du prénom
    return caractere_pas_ok if caractere_pas_ok else True


# Fonction par variable pour vérifier un nom
def check_nom(x_nom):
    # Vérifie chaque caractère dans le nom
    caractere_pas_ok = ""
    for c in x_nom:
        # Si le caractère n'est pas alphabétique ou numérique, ajoute-le à la chaîne de caractères non valides
        if not c.isalnum():
            caractere_pas_ok += c
    # Si la chaîne de caractères non valides est vide, le nom est valide
    # Sinon, elle contient les caractères non valides du nom
    return caractere_pas_ok if caractere_pas_ok else True


# Fonction par variable pour vérifier une adresse
def check_adresse(x_adresse):
    # Si l'adresse est vide, renvoie False
    # Sinon, renvoie True
    if not x_adresse:
        return False
    else:
        return True


# Fonction par variable pour vérifier un email
def check_email(x_email):
    # vérifie si l'email a le bon format
    if '@' in x_email and '.' in x_email:
        # sépare le nom d'utilisateur et le domaine
        aka_utilisateur, dns = x_email.split('@')
        # vérifie si le domaine à au moins un point
        if '.' in dns:
            return True
    return False


# Fonction par variable pour vérifier un login
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


# Fonction par variable pour vérifier un mot de passe
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


# Fonction par variable pour vérifier si deux logins sont égaux
def utilisateur_login_check(utilisateur_x_login, utilisateur_y_login):
    # Renvoie True si les logins sont égaux, False sinon
    if utilisateur_x_login == utilisateur_y_login:
        return True
    else:
        return False


# Séparateur affichant 100 étoiles sur une ligne
print("*" * 100)

while True:
    try:
        # Demande le prénom du premier utilisateur
        utilisateur_1_prenom = input("Entrer le prénom du premier utilisateur: ")
        # Vérifie si le prénom est valide
        if check_prenom(utilisateur_1_prenom) is True:
            print("Prénom valide")
            break
        else:
            print("Prénom invalide, caractères non valides")
    except ValueError:
        continue
print("-" * 100)
while True:
    try:
        # Demande le nom du premier utilisateur
        utilisateur_1_nom = input("Entrer le nom du premier utilisateur: ")
        # Vérifie si le prénom est valide
        if check_nom(utilisateur_1_nom) is True:
            print("Nom valide")
            break
        else:
            print("Nom invalide, caractères non valides")
    except ValueError:
        continue
print("-" * 100)
while True:
    try:
        # Demande l'adresse du premier utilisateur
        utilisateur_1_adresse = int(input("Entrer l'adresse du premier utilisateur: "))
        # Vérifie si l'adresse est enregistrée
        if check_adresse(utilisateur_1_adresse) is True:
            print("Adresse ok")
            break
        else:
            print("Adresse pas ok, enregistrement manquant")
    except ValueError:
        continue
print("-" * 100)
while True:
    try:
        # Demande l'email du premier utilisateur
        utilisateur_1_email = input("Entrer l'email du premier utilisateur: ")
        # Vérifie si l'email est valide
        if check_email(utilisateur_1_email):
            print("Email valide")
            break
        else:
            print("Email non valide")
            print("Email invalide, caractères non valides")
    except ValueError:
        continue
print("-" * 100)
while True:
    try:
        # Demande le login du premier utilisateur
        utilisateur_1_login = input("Entrer le login du premier utilisateur: ")
        # Vérifie si le login est valide
        if check_login(utilisateur_1_login) is True:
            print("Login ok")
            break
        else:
            print("Login invalide, caractères non valides")
    except ValueError:
        continue
print("-" * 100)
while True:
    try:
        # Demande le mot de passe du premier utilisateur
        utilisateur_1_mdp = input("Entrer le mot de passe du premier utilisateur")
        # Vérifie si le mot de passe est valide
        if not check_mdp(utilisateur_1_mdp):
            print("Le mot de passe est valide.")
            break
        else:
            print("Mot de passe invalide")
    except ValueError:
        continue
    utilisateur_1_mdp_cache = "*" * len(utilisateur_1_mdp)

# Séparateur affichant 100 étoiles sur une ligne
print("*" * 100)

while True:
    try:
        # Demande le prénom du second utilisateur
        utilisateur_2_prenom = input("Entrer le prénom du deuxième utilisateur: ")
        # Vérifie si le prénom est valide
        if check_prenom(utilisateur_2_prenom) is True:
            print("Prénom valide")
            break
        else:
            print("Prénom invalide, caractères non valides")
    except ValueError:
        continue
print("-" * 100)
while True:
    try:
        utilisateur_2_nom = input("Entrer le nom du deuxième utilisateur: ")
        if check_nom(utilisateur_2_nom) is True:
            print("Nom valide")
            break
        else:
            print("Nom invalide, caractères non valides")
    except ValueError:
        continue
print("-" * 100)
while True:
    try:
        # Demande l'adresse du second utilisateur
        utilisateur_2_adresse = int(input("Entrer l'adresse du deuxième utilisateur: "))
        # Vérifie si l'adresse est enregistrée
        if check_adresse(utilisateur_2_adresse) is True:
            print("Adresse ok")
            break
        else:
            print("Adresse pas ok, enregistrement manquant")
    except ValueError:
        continue
print("-" * 100)
while True:
    try:
        # Demande l'email du second utilisateur
        utilisateur_2_email = input("Entrer l'email du deuxième utilisateur: ")
        # Vérifie si l'email est valide
        if check_email(utilisateur_2_email):
            print("Email valide")
            break
        else:
            print("Email non valide")
            print("Email invalide, caractères non valides")
    except ValueError:
        continue
print("-" * 100)
while True:
    try:
        # Demande le login du second utilisateur
        utilisateur_2_login = input("Entrer le login du deuxième utilisateur: ")
        # Vérifie si le login est valide
        if check_login(utilisateur_2_login) is True:
            print("Login ok")
            break
        else:
            print("Login invalide, caractères non valides")
    except ValueError:
        continue
print("-" * 100)
while True:
    try:
        # Demande le mot de passe du second utilisateur
        utilisateur_2_mdp = input("Entrer le mot de passe du deuxième utilisateur")
        # Vérifie si le mot de passe est valide
        if not check_mdp(utilisateur_2_mdp):
            print("Le mot de passe est valide.")
            break
        else:
            print("Mot de passe invalide")
    except ValueError:
        continue
    utilisateur_2_mdp_cache = "*" * len(utilisateur_2_mdp)

# Séparateur affichant 100 étoiles sur une ligne
print("*" * 300)

# Vérifie si les logins des deux utilisateurs sont égaux
if utilisateur_login_check(utilisateur_1_login, utilisateur_2_login):
    print("Attention logins similaire !!!")
else:
    print("Logins pas similaire ;)")

print("Les informations du premier utilisateurs ont été bien enregistrer...", "Madame/Monsieur",
      utilisateur_1_prenom, utilisateur_1_nom, "domicilié au", utilisateur_1_adresse, "Namur", "votre email est",
      utilisateur_1_email, "aka", utilisateur_1_login, "et dont le mot de passe est", utilisateur_1_mdp_cache)

print("Les informations du deuxième utilisateurs ont été bien enregistrer...", "Madame/Monsieur",
      utilisateur_2_prenom, utilisateur_2_nom, "domicilié au", utilisateur_2_adresse, "Namur", "votre email est",
      utilisateur_2_email, "aka", utilisateur_2_login, "et dont le mot de passe est", utilisateur_2_mdp_cache)

# Séparateur affichant 100 étoiles sur une ligne
print("*" * 300)
