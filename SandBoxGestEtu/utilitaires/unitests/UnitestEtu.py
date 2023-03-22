import unittest
from SandBoxGestEtu.moduleGestEtu.GestEtu import *


class TestMenuPrincipal(unittest.TestCase):
	def test_menu_principal(self):
		self.assertEqual(afficher_menu(), True)


class TestAfficherEtudiants(unittest.TestCase):
	def test_afficher_etudiants(self):
		self.assertEqual(afficher_etudiants(
			{"1": ["Dupont", "Jean", 20, "M", 15.5], "2": ["Durand", "Marie", 21, "F", 16.5],
			 "3": ["Martin", "Pierre", 22, "M", 17.5]}), True)


class TestEnregistrerEtudiant(unittest.TestCase):
	def test_enregistrer_etudiant(self):
		self.assertEqual(enregistrer_etudiant(
			{"1": ["Dupont", "Jean", 20, "M", 15.5], "2": ["Durand", "Marie", 21, "F", 16.5],
			 "3": ["Martin", "Pierre", 22, "M", 17.5]}), True)


class TestModifierEtudiant(unittest.TestCase):
	def test_modifier_etudiant(self):
		self.assertEqual(modifier_etudiant(
			{"1": ["Dupont", "Jean", 20, "M", 15.5], "2": ["Durand", "Marie", 21, "F", 16.5],
			 "3": ["Martin", "Pierre", 22, "M", 17.5]}), True)


class TestSupprimerEtudiant(unittest.TestCase):
	def test_supprimer_etudiant(self):
		self.assertEqual(supprimer_etudiant(
			{"1": ["Dupont", "Jean", 20, "M", 15.5], "2": ["Durand", "Marie", 21, "F", 16.5],
			 "3": ["Martin", "Pierre", 22, "M", 17.5]}), True)


class TestAjouterEtudiantFichier(unittest.TestCase):
	def test_ajouter_etudiant_fichier(self):
		self.assertEqual(ajouter_etudiant_fichier(
			{"1": ["Dupont", "Jean", 20, "M", 15.5], "2": ["Durand", "Marie", 21, "F", 16.5],
			 "3": ["Martin", "Pierre", 22, "M", 17.5]}), True)


if __name__ == '__main__':
	unittest.main()
