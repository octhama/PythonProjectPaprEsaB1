# mdp = input("Entrer votre mot de passe : ")
# taille_mdp = len(mdp)
# print(taille_mdp)
# print(mdp)
# c = mdp[0]
# print(c)
# nbr_min = mdp.count(c.lower())
# print("nombre de miniscule", nbr_min)
# nbr_maj = mdp.count(c.upper())
# print("nombre de majuscule")
#
#
# if taille_mdp <= 10 and nbr_min <= 1 and nbr_maj <= 1:
#     print("ok")
# else:
#     print("pas ok")


# taille_mdp = len(mdp)

# if taille_mdp <= 10 and mdp.islower():
#     print("Mot de passe correcte")
# else :
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

# Déclaration des indexés itérant sur les valeurs respective majuscules, miniscule, chiffre
# mag = 0
# min = 0
# chf = 0

# #Déclaration des valeurs itérables dans des tableaux de chaînes de caractères majuscules = ["A", "B", "C", "D",
# "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y",
# "Z"] minuscules = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
# "t", "u", "v", "w", "x", "y", "z"] chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#
# elem_1 = majuscules[1]
# print(elem_1)
# elem_2 = majuscules[5]
# print(elem_2)
# elem_3 = chiffres[4]
# print (elem_3)
#
# mot_de_passe = input("Entrer votre mot de passe : ")
# taille_du_mot_de_passe = len (mot_de_passe)
#
# if (taille_du_mot_de_passe <= 10) :
#     for caractere in mot_de_passe :
#         if caractere in minuscules :
#             min += 1
#             continue
#         if caractere in majuscules :
#             mag += 1
#             continue
#         if caractere in chiffres :
#             chf += 1
#             continue
# if (min >= 1 and mag >= 1 and chf >= 1):
#     print("ok")
# else:
#     print("Pas ok")

# Déclaration de variables...

email = input('Entrez une adresse email\n')

# Découper l'adresse email en deux parties : la partie locale et le domaine
local_part, domain = email.split('@')

# Vérifier que la partie locale ne contient que des caractères alphanumériques, des points et des tirets,
# et qu'elle ne commence ni ne se termine pas par un point ou un tiret
for c in local_part:
    if not c.isalnum() and c not in ('.', '-'):
        print("Votre adresse email n'est pas valide : la partie locale de l'adresse contient des caractères non "
              "autorisés")
        exit()
if local_part[0] in ('.', '-') or local_part[-1] in ('.', '-'):
    print("Votre adresse email n'est pas valide : la partie locale de l'adresse contient des caractères non autorisés")
    exit()

# Vérifier que le domaine ne contient que des caractères alphanumériques, des points et des tirets,
# et qu'il ne commence ni ne se termine pas par un point ou un tiret
for c in domain:
    if not c.isalnum() and c not in ('.', '-'):
        print("Votre adresse email n'est pas valide : le domaine de l'adresse contient des caractères non autorisés")
        exit()
if domain[0] in ('.', '-') or domain[-1] in ('.', '-'):
    print("Votre adresse email n'est pas valide : le domaine de l'adresse contient des caractères non autorisés")
    exit()

# Vérifier que le domaine comprend au moins un point et deux parties séparées par ce point
# (par exemple, "example.com")
if '.' not in domain or domain.count('.') > 1 or domain.index('.') == 0 or domain.index('.') == len(domain) - 1:
    print("Votre adresse email n'est pas valide : le domaine de l'adresse est incorrect")
    exit()

# Si aucune erreur n'a été détectée, l'adresse est valide
print("Bravo, votre adresse email est valide")
