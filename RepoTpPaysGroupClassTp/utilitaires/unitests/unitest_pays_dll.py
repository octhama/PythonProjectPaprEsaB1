import unittest
from RepoTpPaysGroupClassTp.utilitaires.pays_dll import *


def charger_fichier():
	nom_du_fichier = "ressources/pays.csv"
	f = ouvrir_fichier(nom_du_fichier)
	liste_pays = charger_le_fichier(f)
	fermer_fichier(f)
	return liste_pays


def test_charger_le_fichier(self):
	liste_pays = charger_fichier()  # Charger le fichier (str)
	self.assertEqual((len(liste_pays)), 249)
	self.assertEqual(self.fichier[0]["Code Alpha-2"], "AF")
	self.assertEqual(self.fichier[-1]["Code Alpha-2"], "ZW")
	self.assertEqual(self.fichier[77], 9)


def test_pays_code(self):
	liste_pays = charger_fichier()
	self.assertIsNone(pays_code(self.fichier, "R2D2"))
	self.assertIsNone(pays_code(self.fichier, "9999"))
	
	self.assertEqual(pays_code(self.fichier, "AF"), "Afghanistan")
	self.assertEqual(pays_code(self.fichier, "ZW"), "Zimbabwe")
	self.assertEqual(pays_code(self.fichier, "ZZ"), "ZZ")


if __name__ == '__main__':
	unittest.main()
