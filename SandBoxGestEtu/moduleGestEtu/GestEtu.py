def afficher_menu():  # Affiche le menu
	print("1. Afficher les étudiants")
	print("2. Enregistrer un étudiant")
	print("3. Ajouter un étudiant au fichier")
	print("4. Modifier un étudiant")
	print("5. Supprimer un étudiant")
	print("6. Quitter")
	print()
	try:
		demande_choix = int(input("Entrez votre choix : "))
	except ValueError:
		print("Vous devez entrer un nombre")
		demande_choix = 0
	return demande_choix


def afficher_etudiants(dico_etudiant):  # Affiche les étudiants
	if dico_etudiant != {}:  # Si le dictionnaire n'est pas vide
		print("Voici les étudiants enregistrés : ")
		for cle, valeur in dico_etudiant.items():
			print(cle, valeur)
	else:
		print("Aucun étudiant n'a été enregistré")


def enregistrer_etudiant(dico_etudiant):  # Enregistre un étudiant
	id_etudiant = input("Entrez l'ID de l'étudiant : ")
	nom = input("Entrez le nom : ")
	prenom = input("Entrez le prénom : ")
	while True:
		try:
			age = int(input("Entrez l'âge : "))
			break
		except ValueError:
			print("Vous devez entrer un nombre")
	sexe = input("Entrez le sexe : ")
	while sexe != "M" and sexe != "F":
		print("Vous devez entrer M ou F")
		sexe = input("Entrez le sexe : ")
	try:
		moyenne = float(input("Entrez la moyenne : "))
	except ValueError:
		print("Vous devez entrer un nombre")
		moyenne = 0
	dico_etudiant[id_etudiant] = [nom, prenom, age, sexe, moyenne]
	print("L'étudiant a été enregistré")
	
	while True:
		demande_ajout_au_fichier = input("Voulez-vous ajouter cet étudiant au fichier ? (O/N) : ")
		if demande_ajout_au_fichier == "O":
			with open("resources/etudiants.txt", "a") as fichier:
				fichier.write(
					id_etudiant + ";" + nom + ";" + prenom + ";" + str(age) + ";" + sexe + ";" + str(moyenne) + " \n")
				print("L'étudiant a été ajouté au fichier")
			break
		elif demande_ajout_au_fichier == "N":
			print("L'étudiant n'a pas été ajouté au fichier")
			break
		else:
			print("Vous devez entrer O ou N")


def ajouter_etudiant_fichier(dico_etudiant):  # Ajoute un étudiant au fichier
	print("Voici les étudiants enregistrés : ")
	for cle, valeur in dico_etudiant.items():
		print(cle, valeur)
	print()
	id_etudiant_a_ajouter = input("Entrez l'ID de l'étudiant à ajouter au fichier : ")
	with open("resources/etudiants.txt", "a") as fichier:
		fichier.write(
			id_etudiant_a_ajouter + ";" + dico_etudiant[id_etudiant_a_ajouter][0] + ";" + dico_etudiant[
				id_etudiant_a_ajouter][1] + ";" + str(dico_etudiant[id_etudiant_a_ajouter][2]) + ";" + dico_etudiant[
				id_etudiant_a_ajouter][3] + ";" + str(dico_etudiant[id_etudiant_a_ajouter][4]) + " \n")
		print("L'étudiant a été ajouté au fichier")


def modifier_etudiant(dico_etudiant):  # Modifie un étudiant
	print("Voici les étudiants enregistrés : ")
	for cle, valeur in dico_etudiant.items():
		print(cle, valeur)
	print()
	id_etudiant_a_modifier = input("Entrez l'ID de l'étudiant à modifier : ")
	print("1. Nom")
	print("2. Prénom")
	print("3. Âge")
	print("4. Sexe")
	print("5. Moyenne")
	print()
	choix_element = int(input("Entrez le numéro de l'élément à modifier : "))
	if choix_element == 1:
		nom = input("Entrez le nouveau nom : ")
		dico_etudiant[id_etudiant_a_modifier][0] = nom
	elif choix_element == 2:
		prenom = input("Entrez le nouveau prénom : ")
		dico_etudiant[id_etudiant_a_modifier][1] = prenom
	elif choix_element == 3:
		age = int(input("Entrez le nouvel âge : "))
		dico_etudiant[id_etudiant_a_modifier][2] = age
	elif choix_element == 4:
		sexe = input("Entrez le nouveau sexe : ")
		dico_etudiant[id_etudiant_a_modifier][3] = sexe
	elif choix_element == 5:
		moyenne = float(input("Entrez la nouvelle moyenne : "))
		dico_etudiant[id_etudiant_a_modifier][4] = moyenne
	else:
		print("L'élément n'existe pas")


def supprimer_etudiant(dico_etudiant):  # Supprime un étudiant
	id_etudiant_a_supprimer = input("Entrez l'ID de l'étudiant à supprimer : ")
	if id_etudiant_a_supprimer in dico_etudiant:
		del dico_etudiant[id_etudiant_a_supprimer]  # Supprime l'étudiant
	else:
		print("L'étudiant n'existe pas")


def main():  # Fonction principale
	dico_etudiant = {}  # Dictionnaire vide
	choix_menu = afficher_menu()  # Affiche le menu
	while choix_menu != 6:
		if choix_menu == 1:
			afficher_etudiants(dico_etudiant)  # Affiche les étudiants
		elif choix_menu == 2:
			enregistrer_etudiant(dico_etudiant)  # Enregistre un étudiant
		elif choix_menu == 3:
			ajouter_etudiant_fichier(dico_etudiant)
		elif choix_menu == 4:
			modifier_etudiant(dico_etudiant)  # Modifie un étudiant
		elif choix_menu == 5:
			supprimer_etudiant(dico_etudiant)  # Supprime un étudiant
		else:
			print("Choix invalide")  # Choix invalide
		choix_menu = afficher_menu()  # Affiche le menu
	exit("Au revoir")  # Quitte le programme
