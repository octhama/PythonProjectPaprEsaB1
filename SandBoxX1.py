while True:
    mon_fichier = open("NbrePositif", "a")
    mon_fichier_negatif = open("NbreNegatif", "a")
    nbre = int(input("Entrez un nombre positif: "))
    if int(nbre) > 0:
        print("Le nombre est positif. Il est ajouté au fichier.")
        mon_fichier.write(str(nbre) + "\n")
        mon_fichier.close()
        continue
    elif int(nbre) < 0:
        print("Le nombre est négatif. Il est ajouté au fichier.")
        mon_fichier_negatif.write(str(nbre) + "\n")
        mon_fichier_negatif.close()
        continue
    else:
        exit("Erreur. Fin du programme.")
