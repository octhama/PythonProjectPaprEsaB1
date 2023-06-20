from SandBoxGestEtu.moduleGestEtu.GestEtuCote import *
from SandBoxGestEtu.moduleGestEtu.GestEtuList import *
from moduleGestEtu.GestEtu import *


# Fonction pour afficher le menu
def afficher_menu():  # Affiche le menu
	print()
	print(" " * 100 + "*" * 5 + " Bienvenue dans le programme de gestion des étudiants " + "*" * 5)  # Décoration du menu
	print(" " * 125 + "*" * 5 + " Menu " + "*" * 5)  # Décoration du menu
	print(" " * 120 + "1. Afficher les étudiants")
	print(" " * 120 + "2. Enregistrer un étudiant")
	print(" " * 120 + "3. Ajouter un étudiant au fichier")
	print(" " * 120 + "4. Ajouter une cote à un étudiant")
	print(" " * 120 + "5. Modifier une cote d'un étudiant")
	print(" " * 120 + "6. Afficher les cotes d'un étudiant")
	print(" " * 120 + "7. Modifier un étudiant")
	print(" " * 120 + "8. Supprimer un étudiant")
	print(" " * 120 + "9. Afficher les étudiants et leurs cotes")
	print(" " * 120 + "10. Quitter")
	print(" " * 125 + "*" * 5 + " Fin du menu " + "*" * 5)  # Décoration du menu
	print()
	try:  # Pour que le programme ne plante pas si l'utilisateur entre autre chose qu'un nombre
		demande_choix = int(input("Entrez votre choix : "))  # Demande le choix de l'utilisateur
		print()  # Saut de ligne
	except ValueError:  # Si l'utilisateur entre autre chose qu'un nombre
		print("Vous devez entrer un nombre")  # Affiche un message d'erreur
		demande_choix = None  # Pour que le programme ne plante pas si l'utilisateur entre autre chose qu'un nombre
	return demande_choix  # Retourne le choix de l'utilisateur


# Fonction d'exécution du programme principal du programme de gestion des étudiants
def main():  # Fonction principale
	dico_etudiant = {}  # Dictionnaire vide (pour les étudiants)
	dico_cotes = {}  # Dictionnaire vide (pour les cotes)
	while True:
		choix_menu = afficher_menu()  # Affiche le menu
		if choix_menu == 1:
			demande_type_affichage = input("Voulez-vous afficher les étudiants enregistrés ou les étudiants du fichier ? (E/F) : ")
			if demande_type_affichage.lower() == "e":
				afficher_etudiants(dico_etudiant)
			elif demande_type_affichage.lower() == "f":
				afficher_etudiants_fichier()
			else:
				print("Le choix n'existe pas")
		elif choix_menu == 2:
			enregistrer_etudiant(dico_etudiant)  # Enregistre un étudiant
		elif choix_menu == 3:
			ajouter_etudiant_fichier()  # Ajoute un étudiant au fichier
		elif choix_menu == 4:
			enregistrer_cote_etudiant(dico_etudiant, dico_cotes)  # Enregistre une cote à un étudiant (dans un fichier)
		elif choix_menu == 5:
			demande_type_modification = input("Voulez-vous modifier une cote d'un étudiant enregistré ou d'un étudiant du fichier ? (E/F) : ")
			if demande_type_modification.lower() == "e":
				modifier_cote_etudiant(dico_etudiant, dico_cotes)  # Modifie une cote d'un étudiant (enregistré)
			elif demande_type_modification.lower() == "f":
				modifier_cote_etudiant_fichier()  # Modifie une cote d'un étudiant (fichier)
			else:
				print("Le choix n'existe pas")
		elif choix_menu == 6:
			afficher_cotes_etudiant(dico_etudiant, dico_cotes)  # Affiche les cotes d'un étudiant
		elif choix_menu == 7:
			demande_type_mod_etu = input("Voulez-vous modifier un étudiant enregistré ou un étudiant du fichier ? (E/F) : ")
			if demande_type_mod_etu.lower() == "e":
				modifier_etudiant_enregistre(dico_etudiant)  # Modifie un étudiant (enregistré)
			elif demande_type_mod_etu.lower() == "f":
				modifier_etudiant_fichier()  # Modifie un étudiant (fichier)
			else:
				print("Le choix n'existe pas")  # Affiche un message d'erreur
		elif choix_menu == 8:
			demande_type_sup_etu = input("Voulez-vous supprimer un étudiant enregistré ou un étudiant du fichier ? (E/F) : ")
			if demande_type_sup_etu.lower() == "e":
				supprimer_etudiant(dico_etudiant)
			elif demande_type_sup_etu.lower() == "f":
				supprimer_etudiant_fichier()
			else:
				print("Le choix n'existe pas")
		elif choix_menu == 9:
			afficher_cotes_fichier()  # Affiche les cotes des étudiants (fichier)
		elif choix_menu == 10:
			quitter = input("Voulez-vous vraiment quitter le programme ? (O/N) : ")
			if quitter.lower() == "o":
				break
			elif quitter.lower() == "n":
				pass
			else:
				print("Le choix n'existe pas")
		else:
			print("Le choix n'existe pas")
	exit("Au revoir")  # Quitte le programme


main()  # Appel de la fonction principale du programme (main)
