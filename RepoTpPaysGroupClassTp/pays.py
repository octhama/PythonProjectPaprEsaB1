from utilitaires.pays_dll import *  # Import du module

nom_du_fichier = "ressources/pays.csv"  # Chemin du fichier (str)
f = ouvrir_fichier(nom_du_fichier)  # Ouvrir le fichier (str)
# print(f)
# if not f:
#    exit("Aucun fichier trouvé")

while not f:  # Tant que le fichier n'est pas trouvé
	nom_du_fichier = input("Entrez le chemin du fichier à ouvrir : ")  # Demander le chemin du fichier à ouvrir (str)
	f = ouvrir_fichier(nom_du_fichier)  # Ouvrir le fichier (str)
liste_pays = charger_le_fichier(f)  # Charger le fichier (str)
# print(liste_pays)  # Afficher la liste des pays (str)
# fermer_fichier(f)  # Fermer le fichier (str)

# ouvrir_fichier(nom_du_fichier)
# fermer_fichier(nom_du_fichier)

# (choix_pays_code(liste_pays, 'AW'))  # Afficher le nom du pays correspondant au code entré (str)
# (compte_continent(liste_pays))  # Afficher le dictionnaire avec le nombre de pays par continent (dict)
# (pays_sans_capital(liste_pays))  # Afficher les pays sans capitale (str)
pays_sans_capital(liste_pays)  # Afficher les pays sans capitale (str)
