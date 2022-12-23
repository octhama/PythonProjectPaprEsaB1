# Fonction par variable
def check_prenom(x_prenom):
    caractere_pas_ok = ""
    for c in x_prenom:
        if not c.isalnum():
            caractere_pas_ok += c
    return caractere_pas_ok


# Fonction par variable
def check_nom(x_nom):
    caractere_pas_ok = ""
    for c in x_nom:
        if not c.isalnum():
            caractere_pas_ok += c
    return caractere_pas_ok


# Fonction par variable
def check_adresse(x_adresse):
    while x_adresse:
        break
    else:
        return False


# Fonction par variable
def check_email(x_email):
    # vérifie si l'email a le bon format
    if '@' in x_email and '.' in x_email:
        # sépare le nom d'utilisateur et le domaine
        aka_utilisateur, nom_domaine = x_email.split('@')
        # vérifie si le domaine à au moins un point
        if '.' in nom_domaine:
            return True
    return False


# Fonction par variable
def check_login(x_login):
    caractere_pas_ok = ""
    for c in x_login:
        if not c.islower() or not c.isalnum():
            caractere_pas_ok += c
    return caractere_pas_ok


# Fonction par variable
def check_mdp(x_mdp):
    taille_mdp = len(x_mdp)

    if taille_mdp < 10:
        return True

    minuscules = 0
    majuscules = 0
    chiffres = 0
    spacechars = 0

    for c in x_mdp:
        if c.islower():
            minuscules += 1
        elif c.isupper():
            majuscules += 1
        elif c.isdigit():
            chiffres += 1
        elif c.isalnum():
            spacechars += 1
    return minuscules and majuscules and chiffres and spacechars


# Fonction par variable
def utilisateur_login_check(utilisateur_x_login, utilisateur_y_login):
    if utilisateur_x_login == utilisateur_y_login:
        return True
    else:
        return False


for i in range(100):
    print("*", end="")
print()

while True:
    try:
        utilisateur_1_prenom = input("Entrer le prénom du premier utilisateur: ")
        if check_prenom(utilisateur_1_prenom):
            print("Prénom invalide")
            continue
    except ValueError:
        continue
    else:
        print("Prénom valide")
        break

while True:
    try:
        utilisateur_1_nom = input("Entrer le nom du premier utilisateur: ")
        if check_nom(utilisateur_1_nom):
            print("Nom invalide")
            continue
    except ValueError:
        continue
    else:
        print("Nom valide")
        break

while True:
    try:
        utilisateur_1_adresse = int(input("Entrer l'adresse du premier utilisateur: "))
        if check_adresse(utilisateur_1_adresse):
            print("Adresse pas ok")
            continue
    except ValueError:
        continue
    else:
        print("Adresse ok")
        break

while True:
    try:
        utilisateur_1_email = input("Entrer l'email du premier utilisateur: ")
        if not check_email(utilisateur_1_email):
            print("Email non valide")
            continue
    except ValueError:
        continue
    else:
        print("Email valide")
        break

while True:
    try:
        utilisateur_1_login = input("Entrer le login du premier utilisateur: ")
        if check_login(utilisateur_1_login):
            print("Login pas ok")
            continue
    except ValueError:
        continue
    else:
        print("Login ok")
        break

while True:
    try:
        utilisateur_1_mdp = input("Entrer le mot de passe du premier utilisateur")
        if check_mdp(utilisateur_1_mdp):
            print("Le mot de passe n'est pas valide.")
            continue
    except ValueError:
        continue
    else:
        print("Le mot de passe est valide.")
        break

utilisateur_1_mdp_cache = "*" * len(utilisateur_1_mdp)

print("*" * 100)

while True:
    try:
        utilisateur_2_prenom = input("Entrer le prénom du deuxième utilisateur: ")
        if check_prenom(utilisateur_2_prenom):
            print("Prénom invalide")
            continue
    except ValueError:
        continue
    else:
        print("Prénom valide")
        break

while True:
    try:
        utilisateur_2_nom = input("Entrer le nom du deuxième utilisateur: ")
        if check_nom(utilisateur_2_nom):
            print("Nom invalide")
            continue
    except ValueError:
        continue
    else:
        print("Nom valide")
        break

while True:
    try:
        utilisateur_2_adresse = int(input("Entrer l'adresse du deuxième utilisateur: "))
        if check_adresse(utilisateur_2_adresse):
            print("Adresse pas ok")
            continue
    except ValueError:
        continue
    else:
        print("Adresse ok")
        break

while True:
    try:
        utilisateur_2_email = input("Entrer l'email du deuxième utilisateur: ")
        if not check_email(utilisateur_2_email):
            print("Email non valide")
            continue
    except ValueError:
        continue
    else:
        print("Email valide")
        break

while True:
    try:
        utilisateur_2_login = input("Entrer le login du deuxième utilisateur: ")
        if check_login(utilisateur_2_login):
            print("Login pas ok")
            continue
    except ValueError:
        continue
    else:
        print("Login ok")
        break

while True:
    try:
        utilisateur_2_mdp = input("Entrer le mot de passe du deuxième utilisateur")
        if check_mdp(utilisateur_2_mdp):
            print("Le mot de passe n'est pas valide.")
            continue
    except ValueError:
        continue
    else:
        print("Le mot de passe est valide.")
        break

utilisateur_2_mdp_cache = "*" * len(utilisateur_2_mdp)

for i in range(100):
    print("*", end="")
print()

if utilisateur_login_check(utilisateur_1_login, utilisateur_2_login):
    print("Login similaire")
else:
    print("Login pas similaire")

print("Les informations du premier utilisateurs ont été bien enregistrer...", "Madame/Monsieur", utilisateur_1_prenom,
      utilisateur_1_nom, "domicilié au", utilisateur_1_adresse, "Namur", "votre email est", utilisateur_1_email, "aka",
      utilisateur_1_login, "et dont le mot de passe est", utilisateur_1_mdp_cache)

print("Les informations du deuxième utilisateurs ont été bien enregistrer...", "Madame/Monsieur", utilisateur_2_prenom,
      utilisateur_2_nom, "domicilié au", utilisateur_2_adresse, "Namur", "votre email est", utilisateur_2_email, "aka",
      utilisateur_2_login, "et dont le mot de passe est", utilisateur_2_mdp_cache)
print("*" * 100)
