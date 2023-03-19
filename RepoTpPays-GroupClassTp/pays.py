from utilitaires.pays_dll import ouvrir_fichier, fermer_fichier, charger_le_fichier, choix_pays_code, compte_continent, \
    pays_sans_capital

nom_du_fichier = "ressources/pays.csv"  # Chemin du fichier (str)
f = ouvrir_fichier(nom_du_fichier)  # Ouvrir le fichier (str)
# print(f)
# if not f:
#    exit("Aucun fichier trouvé")

while not f:  # Tant que le fichier n'est pas trouvé
    nom_du_fichier = input("Entrez le chemin du fichier à ouvrir : ")  # Demander le chemin du fichier à ouvrir (str)
    f = ouvrir_fichier(nom_du_fichier)  # Ouvrir le fichier (str)
print(f)  # Afficher le fichier ouvert (str)

liste_pays = charger_le_fichier(f)  # Charger le fichier (str)

for pays in liste_pays:  # Parcourir chaque pays de la liste de dictionnaires (list)
    print(pays)  # Afficher le dictionnaire (dict)

# ouvrir_fichier(nom_du_fichier)
# fermer_fichier(nom_du_fichier)

# print(choix_pays_code(liste_pays, 'AW'))  # Afficher le nom du pays correspondant au code entré (str)
# print(compte_continent(liste_pays))  # Afficher le dictionnaire avec le nombre de pays par continent (dict)
print(pays_sans_capital(liste_pays))  # Afficher les pays sans capitale (str)
