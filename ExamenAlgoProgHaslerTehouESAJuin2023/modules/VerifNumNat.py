# Fonctions qui vérifie le numéro national du fichier num_nat.data

def verifnatnumfich():
	"""
	
	:return: Cette fonction permet de vérifier les numéros nationaux qui sont valides en prenant
	en compte les condition défini par l'énoncé
	"""
	try:
		x_fichier = open("resources/num_nat.data", "r")
	except FileNotFoundError:
		print("Le fichier n'existe pas")
	else:
		y_fichier = open("resources/numNatOk.csv", "w")
		for ligne in x_fichier:
			ligne = ligne.strip("\n")
			if len(ligne) == 11 and int(ligne[9:11]) == 97 - int(ligne[0:9]) % 97:
				# print(ligne)
				y_fichier.write(ligne + "\n")
		y_fichier.close()
		x_fichier.close()


def verifsexe():
	"""
	
	:return: Cette fonction permet de vérifier le sexe des numeros nationaux et de les faire correspondre
	"""
	nat_ok_fichier = open("resources/numNatOk.csv", "r")
	nat_ok_sexe_fichier = open("resources/numNatOkAndSexe.csv", "w")
	nat_ok_sexe_fichier = open("resources/numNatOkAndSexe.csv", "w")
	for ligne in nat_ok_fichier:
		ligne = ligne.strip("\n")
		if int(ligne[0]) % 2 == 0:
			# print(ligne, "F")
			nat_ok_sexe_fichier.write(ligne + " F" + "\n")
		else:
			# print(ligne, "M")
			nat_ok_sexe_fichier.write(ligne + " M" + "\n")
	nat_ok_sexe_fichier.close()
	nat_ok_sexe_fichier.close()
	nat_ok_fichier.close()


def nbre_nat():
	"""
	
	:return: Cette fonction permet de faire le compte des numeros nationaux valide et invalide
	"""
	nat_ok_fichier = open("resources/num_nat.data", "r")
	nat_ok = 0
	nat_ko = 0
	for ligne in nat_ok_fichier:
		ligne = ligne.strip("\n")
		if len(ligne) == 11 and int(ligne[9:11]) == 97 - int(ligne[0:9]) % 97:
			nat_ok += 1
		else:
			nat_ko += 1
	print("Le nombre de numero national valide est : ", nat_ok)
	print("Le nombre de numero national invalide est : ", nat_ko)
