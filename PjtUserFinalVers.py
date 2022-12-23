# Fonction par variable
def check_nom_prenom(x_nom, x_prenom):
    caractere_pas_ok = 0
    for c in x_nom and x_prenom:
        if x_nom == x_prenom or not c.isalnum():
            caractere_pas_ok += c
    return caractere_pas_ok


# Fonction par variable
def check_adresse(x_adresse):
    while x_adresse:
        break
    else:
        print("Adresse non enregistrer veuillez réessayer")
    return True


# Fonction par variable
def check_email(x_email):
    # sépare le nom d'utilisateur et le domaine
    aka_utilisateur, nom_domaine = x_email.split('@')
    # vérifie si l'email a le bon format
    if '@' in x_email and '.' in x_email:
        # vérifie si le domaine a au moins un point
        if '.' in nom_domaine:
            return True
    return False


# Fonction par variable
def check_login(x_login):
    caractere_pas_ok = 0
    for c in x_login:
        if not c.islower() or not c.isalnum():
            caractere_pas_ok += c
    return caractere_pas_ok


# Fonction par variable
def check_mdp(x_mdp):
    if len(x_mdp) > 10:
        return False

    minuscules = 0
    majuscules = 0
    chiffres = 0

    for c in x_mdp:
        if c.islower():
            minuscules += 1
        elif c.isupper():
            majuscules += 1
        elif c.isdigit():
            chiffres += 1
    return minuscules and majuscules and chiffres


nom = input("Entrer un nom :")
prenom = input("Entrer un prénom: ")
adresse = int(input("Entrer une adresse: "))
email = input("Entrer un email: ")
login = input("Entrer votre login: ")
mdp = input("Entrer un mot de mot passe")
mdp_cache = "*" * len(mdp)

if check_nom_prenom(nom, prenom):
    print("Nom et prénom invalide")
else:
    print("Nom et Prénom valide")
if check_adresse(adresse):
    print("Adresse enregistrer")
else:
    print("Adresse non enregistrer veuillez réessayer")
if check_email(email):
    print("Email valide")
else:
    print("Email invalide")
if check_login(login):
    print("Login pas ok")
else:
    print("Login ok")
if check_mdp(mdp):
    print("Le mot de passe est valide.")
else:
    print("Le mot de passe n'est pas valide.")

print("Vos informations ont été bien enregistrer...", "Madame/Monsieur", nom, prenom, "domicilié au", adresse, "Namur",
      "votre email est", email, "aka", login, "et dont le mot de passe est", mdp_cache)
