# Fonctions de gestion de cotes des étudiants pour le module de gestion des étudiants
from SandBoxGestEtu.moduleGestEtu.GestEtuList import *


def enregistrer_cote_etudiant_enregistre(dico_etudiant, dico_cotes):
	id_etu = input("Entrez l'ID de l'étudiant : ")  # Demande l'ID de l'étudiant
	nom_matiere = input("Entrez le nom de la matière : ")  # Demande le nom de la matière
	if id_etu in dico_etudiant:  # Si l'ID de l'étudiant est dans le dictionnaire des étudiants
		if id_etu in dico_cotes:  # Si l'ID de l'étudiant est dans le dictionnaire des cotes
			cote_etu = input("Entrez la cote de l'étudiant : ")  # Demande la cote de l'étudiant
			if cote_etu.isdigit():  # Si la cote est un nombre
				dico_cotes[id_etu] = cote_etu  # Ajoute la cote de l'étudiant dans le dictionnaire des cotes
				print("La cote de l'étudiant a été enregistrée avec succès !")
			else:  # Si la cote n'est pas un nombre
				print("La cote de l'étudiant n'a pas été enregistrée !")
		else:  # Si l'ID de l'étudiant n'est pas dans le dictionnaire des cotes
			cote_etu = input("Entrez la cote de l'étudiant : ")  # Demande la cote de l'étudiant
			if cote_etu.isdigit():  # Si la cote est un nombre
				dico_cotes[id_etu] = cote_etu  # Ajoute la cote de l'étudiant dans le dictionnaire des cotes
				print("La cote de l'étudiant a été enregistrée avec succès !")
			else:  # Si la cote n'est pas un nombre
				print("La cote de l'étudiant n'a pas été enregistrée !")
	else:  # Si l'ID de l'étudiant n'est pas dans le dictionnaire des étudiants
		print("L'ID de l'étudiant n'est pas enregistré !")
	
	dico_cotes[id_etu] = [nom_matiere, cote_etu]
	print("La cote de l'étudiant a été enregistrée avec succès !")
	
	while True:
		demande_ajout_cote_fichier = input("Voulez-vous ajouter cette cote dans le fichier ? (O/N) : ")
		if demande_ajout_cote_fichier == "O" or demande_ajout_cote_fichier == "o":
			fichier_cote_etu = open("resources/cote_etu.csv", "a")
			fichier_cote_etu.write(id_etu + ";" + nom_matiere + ";" + cote_etu + "\n")
			fichier_cote_etu.close()
			print("La cote de l'étudiant a été ajoutée dans le fichier avec succès !")
			break
		elif demande_ajout_cote_fichier == "N" or demande_ajout_cote_fichier == "n":
			print("La cote de l'étudiant n'a pas été ajoutée dans le fichier !")
			break
		else:
			print("Veuillez entrer O ou N !")


def enregistrer_cote_etudiant_fichier():
	demande_id_etu = input("Entrez l'ID de l'étudiant dont vous voulez enregistrer la cote : ")
	demande_nom_matiere = input("Entrez le nom de la matière : ")
	demande_cote_etu = input("Entrez la cote de l'étudiant : ")
	with open("resources/cote_etu.csv", "a") as fichier_cote_etu:
		fichier_cote_etu.write(demande_id_etu + ";" + demande_nom_matiere + ";" + demande_cote_etu + "\n")
		print("La cote de l'étudiant a été enregistrée avec succès !")


def enregistrer_cote_etudiant(dico_etudiant, dico_cotes):  # Enregistre une cote d'un étudiant dans le dictionnaire
	demande_type_affichage = input(
		"Voulez-vous afficher les étudiants enregistrés ou les étudiants du fichier ? (E/F/X) : ")
	if demande_type_affichage.lower() == "e":
		afficher_etudiants(dico_etudiant)
	elif demande_type_affichage.lower() == "f":
		afficher_etudiants_fichier()
	elif demande_type_affichage.lower() == "x":
		pass
	else:
		print("Le choix n'existe pas")
	print()
	demande_type_enregistrement = input(
		"Voulez-vous enregistrer la cote d'un étudiant enregistré ou d'un étudiant du fichier ? (E/F/X) : ")
	if demande_type_enregistrement.lower() == "e":
		enregistrer_cote_etudiant_enregistre(dico_etudiant, dico_cotes)
	elif demande_type_enregistrement.lower() == "f":
		enregistrer_cote_etudiant_fichier(dico_etudiant, dico_cotes)
	elif demande_type_enregistrement.lower() == "x":
		pass
	else:
		print("Le choix n'existe pas")


def modifier_cote_etudiant(dico_etudiant, dico_cotes):  # Modifie une cote d'un étudiant dans le dictionnaire des cotes
	id_etu = input("Entrez l'ID de l'étudiant : ")
	if id_etu in dico_etudiant:  # Si l'ID de l'étudiant est dans le dictionnaire des étudiants
		if id_etu in dico_cotes:  # Si l'ID de l'étudiant est dans le dictionnaire des cotes
			cote_etu = input("Entrez la nouvelle cote de l'étudiant : ")
			if cote_etu.isdigit():  # Si la cote est un nombre
				dico_cotes[id_etu] = cote_etu  # Modifie la cote de l'étudiant dans le dictionnaire des cotes
				print("La cote de l'étudiant a été modifiée")
			else:
				print("La cote doit être un nombre")
		else:
			print("L'étudiant n'a pas de cote")
	else:
		print("L'étudiant n'est pas enregistré")


def modifier_cote_etudiant_fichier():
	demande_id_etu_cote = input("Entrez l'ID de l'étudiant dont vous voulez modifier la cote : ")
	print("1. Modifier la matière")
	print("2. Modifier la cote")
	demande_modification = input("Que voulez-vous modifier ? (1/2) : ")
	if demande_modification == "1":
		demande_nouvelle_matiere = input("Entrez la nouvelle matière : ")
		with open("resources/cote_etu.csv", "r") as fichier_cote_etu:
			lignes = fichier_cote_etu.readlines()
		with open("resources/cote_etu.csv", "w") as fichier_cote_etu:
			for ligne in lignes:
				ligne = ligne.strip("\n")
				ligne = ligne.split(";")
				id_etu = ligne[0]
				nom_matiere = ligne[1]
				cote_etu = ligne[2]
				if id_etu == demande_id_etu_cote:
					fichier_cote_etu.write(id_etu + ";" + demande_nouvelle_matiere + ";" + cote_etu + "\n")
					print("La matière a été modifiée avec succès !")
				else:
					fichier_cote_etu.write(id_etu + ";" + nom_matiere + ";" + cote_etu + "\n")
	elif demande_modification == "2":
		demande_nouvelle_cote = input("Entrez la nouvelle cote : ")
		with open("resources/cote_etu.csv", "r") as fichier_cote_etu:
			lignes = fichier_cote_etu.readlines()
		with open("resources/cote_etu.csv", "w") as fichier_cote_etu:
			for ligne in lignes:
				ligne = ligne.strip("\n")
				ligne = ligne.split(";")
				id_etu = ligne[0]
				nom_matiere = ligne[1]
				cote_etu = ligne[2]
				if id_etu == demande_id_etu_cote:
					fichier_cote_etu.write(id_etu + ";" + nom_matiere + ";" + demande_nouvelle_cote + "\n")
					print("La cote de l'étudiant a été modifiée")
				else:
					fichier_cote_etu.write(id_etu + ";" + nom_matiere + ";" + cote_etu + "\n")
	else:
		print("Le choix n'existe pas")


def afficher_cotes_etudiant(dico_etudiant, dico_cotes):  # Affiche les cotes d'un étudiant du dictionnaire des cotes
	# et du dictionnaire des étudiants
	demamnde_type_affichage = input("Voulez-vous afficher les étudiants enregistrés ou les étudiants du fichier ? (E/F/X) : ")
	if demamnde_type_affichage.lower() == "e":
		afficher_etudiants(dico_etudiant)
	elif demamnde_type_affichage.lower() == "f":
		afficher_etudiants_fichier()
	elif demamnde_type_affichage.lower() == "x":
		pass
	else:
		print("Le choix n'existe pas")
	print()
	id_etu = input("Entrez l'ID de l'étudiant : ")  # Demande l'ID de l'étudiant
	demande_type_recherche = input(
		"Voulez-vous rechercher l'étudiant dans les étudiants enregistrés ou dans les étudiants du fichier ? (E/F/X) : ")
	# Recherche l'étudiant dans les étudiants enregistrés ou dans les étudiants du fichier selon le choix de l'utilisateur
	if demande_type_recherche.lower() == "e":
		for cle, valeur in dico_etudiant.items():  # Parcours le dictionnaire des étudiants
			if id_etu == cle:  # Si l'ID de l'étudiant est dans le dictionnaire des étudiants
				if id_etu in dico_cotes:  # Si l'ID de l'étudiant est dans le dictionnaire des cotes
					print("L'étudiant a une cote de", dico_cotes[id_etu], "en", valeur[1])  # Affiche la cote de l'étudiant
					break
				else:  # Si l'ID de l'étudiant n'est pas dans le dictionnaire des cotes
					print("L'étudiant n'a pas de cote")  # Affiche un message d'erreur
					break
			else:  # Si l'ID de l'étudiant n'est pas dans le dictionnaire des étudiants
				print("L'étudiant n'est pas enregistré")  # Affiche un message d'erreur
	# Recherche dans le fichier des cotes si l'ID de l'étudiant n'est pas dans le dictionnaire des étudiants
	elif demande_type_recherche.lower() == "f":
		for ligne in open("resources/cote_etu.csv", "r"):
			ligne = ligne.strip("\n")
			ligne = ligne.split(";")
			if id_etu == ligne[0]:
				print("L'étudiant a une cote de", ligne[2], "en", ligne[1])
				break
	elif demande_type_recherche.lower() == "x":
		pass
	else:
		print("Le choix n'existe pas")


def afficher_cotes_fichier():  # Affiche les cotes du fichier
	with open("resources/cote_etu.csv", "r") as fichier:  # Ouvre le fichier des cotes en lecture
		# Parcours le fichier des cotes et affiche les cotes dès la deuxième ligne
		for ligne in fichier.readlines()[1:]:
			ligne = ligne.strip("\n").split(";")
			print("L'étudiant", ligne[0], "a une cote de", ligne[2], "en", ligne[1])
			
