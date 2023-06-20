# Formulaire de gestion des étudiants (avec enregistrement dans un fichier csv)

# Fonction qui enregistre un étudiant du dictionnaire dans un fichier csv des étudiants
def enregistrer_etudiant(dico_etudiant):  # Enregistre un étudiant
	id_etudiant = input("Entrez l'ID de l'étudiant : ")  # Demande l'ID de l'étudiant
	nom = input("Entrez le nom : ")
	prenom = input("Entrez le prénom : ")
	while True:
		try:  # Vérifie que l'âge est un nombre
			age = int(input("Entrez l'âge : "))
			break
		except ValueError:  # Si l'âge n'est pas un nombre
			print("Vous devez entrer un nombre")  # Affiche un message d'erreur
	sexe = input("Entrez le sexe : ")
	while sexe != "M" and sexe != "F":  # Vérifie que le sexe est M ou F
		print("Vous devez entrer M ou F")
		sexe = input("Entrez le sexe : ")
	try:  # Vérifie que la moyenne est un nombre
		moyenne = float(input("Entrez la moyenne : "))
	except ValueError:  # Si la moyenne n'est pas un nombre
		print("Vous devez entrer un nombre")
		moyenne = 0  # Met la moyenne à 0 par défaut si elle n'est pas un nombre (pour éviter une erreur)
	
	dico_etudiant[id_etudiant] = [nom, prenom, age, sexe, moyenne]  # Ajoute l'étudiant au dictionnaire
	print("L'étudiant a été enregistré")
	
	while True:
		demande_ajout_au_fichier = input("Voulez-vous ajouter cet étudiant au fichier ? (O/N) : ")
		if demande_ajout_au_fichier == "O":  # Si l'utilisateur veut ajouter l'étudiant au fichier
			with open("resources/etudiants.csv", "a") as fichier:  # Ouvre le fichier en mode ajout
				fichier.write(id_etudiant + ";" + nom + ";" + prenom + ";" + str(age) + ";" + sexe + ";" + str(
					moyenne) + " \n")  # Ajoute l'étudiant au fichier
				print("L'étudiant a été ajouté au fichier")
			break
		elif demande_ajout_au_fichier == "N":  # Si l'utilisateur ne veut pas ajouter l'étudiant au fichier
			print("L'étudiant n'a pas été ajouté au fichier")
			break  # Sort de la boucle
		else:
			print("Vous devez entrer O ou N")


# Fonction pour ajouter un étudiant au fichier (sans passer par le dictionnaire)
def ajouter_etudiant_fichier():  # Ajoute un étudiant au fichier
	print("Voici les étudiants enregistrés dans le fichier : ")  # Affiche les étudiants enregistrés dans le fichier
	with open("resources/etudiants.csv", "r") as fichier:
		for ligne in fichier:
			print(ligne)
	print()
	id_etudiant = input("Entrez l'ID de l'étudiant à ajouter au fichier : ")
	nom = input("Entrez le nom : ")
	prenom = input("Entrez le prénom : ")
	while True:  # Demande l'âge de l'étudiant
		try:  # Vérifie que l'âge est un nombre
			age = int(input("Entrez l'âge : "))  # Demande l'âge de l'étudiant
			break
		except ValueError:  # Si l'âge n'est pas un nombre
			print("Vous devez entrer un nombre")
	sexe = input("Entrez le sexe : ")
	while sexe != "M" and sexe != "F":  # Vérifie que le sexe est M ou F
		print("Vous devez entrer M ou F")
		sexe = input("Entrez le sexe : ")
	try:  # Vérifie que la moyenne est un nombre
		moyenne = float(input("Entrez la moyenne : "))
	except ValueError:  # Si la moyenne n'est pas un nombre
		print("Vous devez entrer un nombre")
		moyenne = 0  # Met la moyenne à 0 par défaut si elle n'est pas un nombre
	# Ajoute l'étudiant au fichier
	with open("resources/etudiants.csv", "a") as fichier:
		fichier.write(id_etudiant + ";" + nom + ";" + prenom + ";" + str(age) + ";" + sexe + ";" + str(moyenne) + " \n")
	print("L'étudiant a été ajouté au fichier")


# Fonction pour modifier un étudiant enregistré dans le dictionnaire
def modifier_etudiant_enregistre(dico_etudiant):  # Modifie un étudiant enregistré dans le dictionnaire
	print("Voici les étudiants enregistrés : ")
	for cle, valeur in dico_etudiant.items():  # Pour chaque étudiant enregistré dans le dictionnaire
		print(cle, valeur)  # Affiche l'étudiant avec son ID et ses informations
	print()  # Saut de ligne
	id_etudiant_a_modifier = input("Entrez l'ID de l'étudiant à modifier : ")  # Demande l'ID de l'étudiant à modifier
	print("1. Identifiant")  # Affiche les éléments modifiables
	print("2. Nom")
	print("3. Prénom")
	print("4. Âge")
	print("5. Sexe")
	print("6. Moyenne")
	choix = input("Que voulez-vous modifier ? : ")  # Demande ce que l'utilisateur veut modifier
	if choix == "1":  # Si l'utilisateur veut modifier l'identifiant
		nouvel_id = input("Entrez le nouvel identifiant : ")
		dico_etudiant[nouvel_id] = dico_etudiant.pop(id_etudiant_a_modifier)
		print("L'identifiant a été modifié")
	elif choix == "2":
		nouveau_nom = input("Entrez le nouveau nom : ")
		dico_etudiant[id_etudiant_a_modifier][0] = nouveau_nom
		print("Le nom a été modifié")
	elif choix == "3":
		nouveau_prenom = input("Entrez le nouveau prénom : ")
		dico_etudiant[id_etudiant_a_modifier][1] = nouveau_prenom
		print("Le prénom a été modifié")
	elif choix == "4":
		nouvel_age = int(input("Entrez le nouvel âge : "))
		dico_etudiant[id_etudiant_a_modifier][2] = nouvel_age
		print("L'âge a été modifié")
	elif choix == "5":
		nouveau_sexe = input("Entrez le nouveau sexe : ")
		dico_etudiant[id_etudiant_a_modifier][3] = nouveau_sexe
		print("Le sexe a été modifié")
	elif choix == "6":
		nouvelle_moyenne = float(input("Entrez la nouvelle moyenne : "))
		dico_etudiant[id_etudiant_a_modifier][4] = nouvelle_moyenne
		print("La moyenne a été modifiée")
	else:
		print("Vous n'avez pas entré un choix valide")


# Fonction pour suppression dans le dictionnaire
def supprimer_etudiant(dico_etudiant):  # Supprime un étudiant du dictionnaire
	id_etudiant_a_supprimer = input("Entrez l'ID de l'étudiant à supprimer : ")  # Demande l'ID de l'étudiant à supprimer
	if id_etudiant_a_supprimer in dico_etudiant:
		del dico_etudiant[id_etudiant_a_supprimer]  # Supprime l'étudiant du dictionnaire
	else:
		print("L'étudiant n'existe pas")
	print("L'étudiant a été supprimé")


# Fonction pour suppression dans le fichier csv
def supprimer_etudiant_fichier():  # Supprime un étudiant du fichier csv
	id_etudiant_a_supprimer = input("Entrez l'ID de l'étudiant à supprimer : ")
	with open("resources/etudiants.csv", "r") as fichier:  # Ouvre le fichier csv en mode lecture
		lignes = fichier.readlines()  # Lit toutes les lignes du fichier
		for ligne in lignes:  # Pour chaque ligne du fichier
			if id_etudiant_a_supprimer in ligne:  # Si l'ID de l'étudiant à supprimer est dans la ligne
				lignes.remove(ligne)  # Supprime la ligne
	with open("resources/etudiants.csv", "w") as fichier:  # Ouvre le fichier csv en mode écriture
		for ligne in lignes:
			fichier.write(ligne)
	print("L'étudiant a été supprimé")


# Fonctions pour modifier et supprimer les étudiants du fichier csv
def modifier_etudiant_fichier():  # Modifie un étudiant du fichier csv
	id_etudiant_a_modifier = input("Entrez l'ID de l'étudiant à modifier : ")  # Demande l'ID de l'étudiant à modifier
	print("1. Identifiant")  # Affiche les éléments modifiables
	print("2. Nom")
	print("3. Prénom")
	print("4. Âge")
	print("5. Sexe")
	print("6. Moyenne")
	choix = input("Que voulez-vous modifier ? : ")
	if choix == "1":  # Si l'utilisateur veut modifier l'identifiant
		identifiant = input("Entrez le nouvel identifiant : ")  # Demande le nouvel identifiant
		with open("resources/etudiants.csv", "r") as fichier:  # Ouvre le fichier en mode lecture
			lignes = fichier.readlines()  # Lit toutes les lignes du fichier
		with open("resources/etudiants.csv", "w") as fichier:  # Ouvre le fichier en mode écriture
			for ligne in lignes:  # Parcours le fichier
				if id_etudiant_a_modifier in ligne:  # Si l'ID de l'étudiant à modifier est dans le fichier
					ligne = ligne.replace(id_etudiant_a_modifier, identifiant)  # Remplace l'ID de l'étudiant à modifier
				# par le nouvel identifiant
				fichier.write(ligne)  # Écrit la ligne dans le fichier
	elif choix == "2":
		nom = input("Entrez le nouveau nom : ")
		with open("resources/etudiants.csv", "r") as fichier:
			lignes = fichier.readlines()
		with open("resources/etudiants.csv", "w") as fichier:
			for ligne in lignes:
				if id_etudiant_a_modifier in ligne:
					ligne = ligne.replace(ligne.split(";")[1], nom)
				fichier.write(ligne)
	elif choix == "3":
		prenom = input("Entrez le nouveau prénom : ")
		with open("resources/etudiants.csv", "r") as fichier:
			lignes = fichier.readlines()
		with open("resources/etudiants.csv", "w") as fichier:
			for ligne in lignes:
				if id_etudiant_a_modifier in ligne:
					ligne = ligne.replace(ligne.split(";")[2], prenom)
				fichier.write(ligne)
	elif choix == "4":
		age = input("Entrez le nouvel âge : ")
		with open("resources/etudiants.csv", "r") as fichier:
			lignes = fichier.readlines()
		with open("resources/etudiants.csv", "w") as fichier:
			for ligne in lignes:
				if id_etudiant_a_modifier in ligne:
					ligne = ligne.replace(ligne.split(";")[3], age)
				fichier.write(ligne)
	elif choix == "5":
		sexe = input("Entrez le nouveau sexe : ")
		with open("resources/etudiants.csv", "r") as fichier:
			lignes = fichier.readlines()
		with open("resources/etudiants.csv", "w") as fichier:
			for ligne in lignes:
				if id_etudiant_a_modifier in ligne:
					ligne = ligne.replace(ligne.split(";")[4], sexe)
				fichier.write(ligne)
	elif choix == "6":
		moyenne = input("Entrez la nouvelle moyenne : ")
		with open("resources/etudiants.csv", "r") as fichier:
			lignes = fichier.readlines()
		with open("resources/etudiants.csv", "w") as fichier:
			for ligne in lignes:
				if id_etudiant_a_modifier in ligne:
					ligne = ligne.replace(ligne.split(";")[5], moyenne)
				fichier.write(ligne)
	else:
		print("Choix invalide")
	print("L'étudiant a été modifié")
