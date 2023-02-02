# Déclaration des indexs (alias) itérant sur les valeurs respectifs 
# maguscule, minuscule, chiffre...
maguscules = 0
minuscules = 0
chiffres = 0
mot_de_passe = input("Entrer votre mot de passe : ")
taille_du_mot_de_passe = len(mot_de_passe)

# Verifier que la la conditon taille du mot de passe est plus petit ou égal à 10
if (taille_du_mot_de_passe <= 10):
    # Tout éléments constituant le mot de passe seront déclarer caratere...
    for caractere in mot_de_passe:
        # Si caractere est en minuscule alors avec minuscules itère sur la chaine de caractère 
        # et pointe que les lettres minuscule (valeurs booléennes retournées)
        if caractere.islower():
            minuscules += 1
            continue
        # Si caractere est en maguscule alors avec maguscules itère sur la chaine de caractère 
        # et pointe que les lettres maguscule (valeurs booléennes retournées)
        if caractere.isupper():
            maguscules += 1
            continue
        # Si caractere est en chiffre alors avec chiffres itère sur la chaine de caractère 
        # et pointe que les chiffres (valeurs booléennes retournées)
        if caractere.isdigit():
            chiffres += 1
            continue
else:
    print("Mot de passe trop long :'(...pas plus de 10 caractères...")
# Verifier si la chaine de caractère contient au minumum 1 minuscule, 1 maguscule, 1 chiffre...
# ...autrement dit qu'il y ait au moins 1 de ces valeurs dans la chaine de caractères...
if (minuscules >= 1 and maguscules >= 1 and chiffres >= 1):
    print("Mot de passe correcte :)")
else:
    print("Mot de passe incorrecte :(")
