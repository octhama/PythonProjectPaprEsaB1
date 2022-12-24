mot_de_passe = input("Entrer votre mot de passe : ")
taille_du_mot_de_passe = len(mot_de_passe)
# Initialisation des indexés (alias) itérant sur les valeurs respectives
# majuscule, minuscule, chiffre...
majuscules = 0
minuscules = 0
chiffres = 0
caractere = 0
# Verifier que la condition taille du mot de passe est plus grande ou égale à 10
if taille_du_mot_de_passe >= 10:
    print("Taille du mot de passe correcte")
    # Tous éléments constituant le mot de passe seront déclarer caractere...
    for caractere in mot_de_passe:
        # Si caractere est en minuscule alors avec minuscules itère sur la chaine de caractère
        # et pointe que les lettres minuscules (valeurs booléennes retournées)
        if caractere.islower():
            minuscules += 1
            continue
        # Si caractere est en majuscule alors avec majuscules itère sur la chaine de caractère
        # et pointe que les lettres majuscule (valeurs booléennes retournées)
        if caractere.isupper():
            majuscules += 1
            continue
        # Si caractere est en chiffre alors avec chiffres itère sur la chaine de caractère
        # et pointe que les chiffres (valeurs booléennes retournées)
        if caractere.isdigit():
            chiffres += 1
            continue
else:
    print("Mot de passe trop court :'(...Il faut dix charactères minimum...")
# Verifier si la chaine de caractère contient au minimum 1 minuscule, 1 majuscule, 1 chiffre...
# ...autrement dit qu'il y a au moins 1 de ces valeurs dans la chaine de caractères...
if minuscules >= 1 and majuscules >= 1 and chiffres >= 1:
    print("Mot de passe correcte :)")
else:
    print("Mot de passe incorrecte :(...")
