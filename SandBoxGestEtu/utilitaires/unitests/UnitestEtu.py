import unittest
from SandBoxGestEtu.moduleGestEtu.GestEtu import *
from SandBoxGestEtu.moduleGestEtu.GestEtuCote import *
from SandBoxGestEtu.moduleGestEtu.GestEtuList import *


def test_enregistrer_etudiant(self):
	dico_etudiant = {}
	self.assertEqual(enregistrer_etudiant(self.dico_etudiant, {"001": ["Dupont", "Jean", "20", "M", "12"]}))
	self.assertEqual(enregistrer_etudiant(self.dico_etudiant, {"002": ["Clement", "Max", "20", "M", "12"]}))


def test_ajouter_etudiant_fichier(self):
	self.assertEqual(ajouter_etudiant_fichier("resources/etudiants.csv", "001", "Dupont", "Jean", "20", "M", "12"))
	self.assertEqual(ajouter_etudiant_fichier("resources/etudiants.csv", "002", "Clement", "Max", "20", "M", "12"))


def test_enregistrer_cote_etudiant(self):
	self.assertEqual(enregistrer_cote_etudiant("resources/cotes.csv", "001", "Philosophie", "12"))
	self.assertEqual(enregistrer_cote_etudiant("resources/cotes.csv", "001", "Mathematiques", "15"))


if __name__ == '__main__':
	unittest.main()
