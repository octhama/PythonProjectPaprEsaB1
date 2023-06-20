# Fonctions pour afficher, modifier et supprimer les étudiants du dictionnaire d'étudiants enregistrés
def afficher_etudiants(dico_etudiant):  # Affiche les étudiants
	if dico_etudiant != {}:  # Si le dictionnaire n'est pas vide
		print("Voici les étudiants enregistrés : ")
		for cle, valeur in dico_etudiant.items():  # Parcours le dictionnaire d'étudiants enregistrés et affiche les
			# étudiants enregistrés
			print(cle, valeur)  # Affiche les étudiants enregistrés avec leur ID et leurs informations personnelles
	else:  # Si le dictionnaire est vide
		print("Aucun étudiant n'a été enregistré")


# Fonctions pour afficher les étudiants du fichier csv
def afficher_etudiants_fichier():  # Affiche les étudiants du fichier csv
	with open("resources/etudiants.csv", "r") as fichier:  # Ouvre le fichier en mode lecture
		for ligne in fichier.readlines()[1:]:  # Parcours le fichier
			ligne = ligne.strip("\n").split(";")
			print(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4], ligne[5])
	print()  # Affiche une ligne vide pour aérer l'affichage


# Fonctions pour afficher les étudiants et leurs cotes du fichier csv des cotes et du fichier csv des étudiants
def afficher_cotes_etudiants_fichier():  # Affiche les étudiants et leurs cotes du fichier csv des cotes et du fichier
	# csv des étudiants
	with open("resources/etudiants.csv", "r") as fichier_etudiants:  # Ouvre le fichier des étudiants en mode lecture
		with open("resources/cotes.csv", "r") as fichier_cotes:  # Ouvre le fichier des cotes en mode lecture
			for ligne_etudiant in fichier_etudiants:  # Parcours le fichier des étudiants
				for ligne_cote in fichier_cotes:  # Parcours le fichier des cotes
					if ligne_etudiant.split(",")[0] == ligne_cote.split(",")[0]:  # Si l'ID de l'étudiant est égal à l'ID
						# de l'étudiant dans le fichier des cotes
						print(ligne_etudiant.rstrip("\n") + " " + ligne_cote.rstrip("\n"))  # Affiche l'étudiant et ses
						# cotes
						break  # Sort de la boucle for
	print()  # Affiche une ligne vide pour aérer l'affichage
