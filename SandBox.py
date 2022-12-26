#     cote_1 = float(input("Entrer la première cote : "))
#     cote_2 = float(input("Entrer la deuxième cote : "))
#     cote_3 = float(input("Entrer la troisième cote : "))
#     cote_4 = float(input("Entrer la quatrième cote : "))
#     cote_5 = float(input("Entrer la cinquième cote : "))
#
#     if 0 <= cote_1 <= 20 and 0 <= cote_2 <= 20 and 0 <= cote_3 <= 20 and 0 <= cote_4 <= 20 and 0 <= cote_5 <= 20:
#         sum_cote = cote_1 + cote_2 + cote_3 + cote_4 + cote_5
#         moyenne_cote = sum_cote / 5
#         print("La somme cumulé des cotes de l'étudiant est de : ", sum_cote)
#         print("La moyenne de cet étudiant est de : ", moyenne_cote)
#     else:
#         print("Cote invalide veuillez réessayer")

while True:
    cote_1 = float(input("Entrer la première cote : "))
    cote_2 = float(input("Entrer la deuxième cote : "))
    cote_3 = float(input("Entrer la troisième cote : "))
    cote_4 = float(input("Entrer la quatrième cote : "))
    cote_5 = float(input("Entrer la cinquième cote : "))
    if not 0 <= cote_1 <= 20:
        print("Cotes invalident veuillez réessayer :(")
        continue
    if not 0 <= cote_2 <= 20:
        print("Cotes invalident veuillez réessayer :(")
        continue
    if not 0 <= cote_3 <= 20:
        print("Cotes invalident veuillez réessayer :(")
        continue
    if not 0 <= cote_4 <= 20:
        print("Cotes invalident veuillez réessayer :(")
        continue
    if not 0 <= cote_5 <= 20:
        print("Cotes invalident veuillez réessayer :(")
        continue
    else:
        sum_cote = cote_1 + cote_2 + cote_3 + cote_4 + cote_5
        moyenne_cote = sum_cote / 5
        print("Cotes valident ;)...")
        print("La somme cumulé des cotes de l'étudiant est de : ", sum_cote)
        print("La moyenne de cet étudiant est de : ", moyenne_cote)
        break

# while True:
#     cote_1 = float(input("Entrer la première cote : "))
#     cote_2 = float(input("Entrer la deuxième cote : "))
#     cote_3 = float(input("Entrer la troisième cote : "))
#     cote_4 = float(input("Entrer la quatrième cote : "))
#     cote_5 = float(input("Entrer la cinquième cote : "))
#     if not 0 <= cote_1 <= 20 or 0 <= cote_2 <= 20 or 0 <= cote_3 <= 20 or 0 <= cote_4 <= 20 or 0 <= cote_5 <= 20:
#         print("Cotes invalident veuillez réessayer")
#         continue
#     else:
#         sum_cote = cote_1 + cote_2 + cote_3 + cote_4 + cote_5
#         moyenne_cote = sum_cote / 5
#         print("La somme cumulé des cotes de l'étudiant est de : ", sum_cote)
#         print("La moyenne de cet étudiant est de : ", moyenne_cote)
#         break
