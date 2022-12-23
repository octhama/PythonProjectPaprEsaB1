#
# mdp = input("Entrer votre mot de passe : ")
# taille_mdp = len(mdp)
# print(taille_mdp)
# print(mdp)
# c = mdp[0]
# print(c)
# nbr_min = mdp.count(c.lower())
# print("nombre de miniscule", nbr_min)
# nbr_maj = mdp.count(c.upper())
# print("nombre de magiscule", nbr_maj)
#
#
# if taille_mdp <= 10 and nbr_min <= 1 and nbr_maj <= 1:
#     print("ok")
# else:
#     print("pas ok")


#taille_mdp = len(mdp)

# if taille_mdp <= 10 and mdp.islower():
#     print("Mot de passe correcte")
# else:
#     print("Mot de passe incorrecte")

# mdp = input("Entrer votre mot de passe : ")
# taille_mdp = len(mdp)
#
# for i in range(len(mdp)):
#     print(taille_mdp)
#     print(mdp.isupper())
#     print(mdp.islower())
#     print(mdp.isalpha())
#     print(mdp.count(mdp))
#     break

# for c in mdp:
#     c += 1
#     print(mdp[c + 1])
#     nbr_min = mdp.count(c.lower())
#     nbr_maj = mdp.count(c.upper())
#     if nbr_min < 1 and nbr_maj < 1:
#         print("pas ok")
#     else:
#         print("ok")
# print(nbr_min)
# print(nbr_maj)

# Déclaration des indexs itérant sur les valeurs respectifs magiscule, miniscule, chiffre
# mag = 0
# min = 0
# chf = 0

# #Déclaration des valeurs itérables dans des tableaaux de chaînes de caractères
# magiscules = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# miniscules = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#
# elem_1 = magiscules[1]
# print(elem_1)
# elem_2 = magiscules[5]
# print(elem_2)
# elem_3 = chiffres[4]
# print(elem_3)
#
# mot_de_passe = input("Entrer votre mot de passe : ")
# taille_du_mot_de_passe = len(mot_de_passe)
#
# if (taille_du_mot_de_passe <= 10):
#     for caractere in mot_de_passe:
#         if caractere in miniscules:
#             min += 1
#             continue
#         if caractere in magiscules:
#             mag += 1
#             continue
#         if caractere in chiffres:
#             chf += 1
#             continue
# if (min >= 1 and mag >= 1 and chf >= 1):
#     print("ok")
# else:
#     print("Pas ok")

# Déclaration de variables...
mot_de_passe = input("Entrer votre mot de passe : ")
taille_du_mot_de_passe = len(mot_de_passe)
# Initialisation des indexs (alias) itérant sur les valeurs respectifs
# majuscule, minuscule, chiffre...
majuscules = 0
minuscules = 0
chiffres = 0
caractere = 0
# Verifier que la la conditon taille du mot de passe est plus grand ou égal à 10
if (taille_du_mot_de_passe >= 10):
    print("Taille du mot de passe correcte")
    # Tout éléments constituant le mot de passe seront déclarer caratere...
    for caractere in mot_de_passe:
        # Si caractere est en minuscule alors avec minuscules itère sur la chaine de caractère
        # et pointe que les lettres minuscule (valeurs booléennes retournées)
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
# Verifier si la chaine de caractère contient au minumum 1 minuscule, 1 maguscule, 1 chiffre...
# ...autrement dit qu'il y ait au moins 1 de ces valeurs dans la chaine de caractères...
if minuscules >= 1 and majuscules >= 1 and chiffres >= 1:
    print("Mot de passe correcte :)")
else:
    print("Mot de passe incorrecte :(...")