import unittest

from ExamenAlgoProgHaslerTehouESAJuin2023.modules.VerifNumNat import verifnatnumfich, verifsexe, nbre_nat


class TestVerifNumNat(unittest.TestCase):
	def test_verifnatnumfich(self):
		"""
		Test unitaire pour la fonction verifnatnumfich
		:return:
		"""
		verifnatnumfich()
		x_fichier = open("resources/numNatOk.csv", "r")
	
	def test_verifsexe(self):
		"""
		Test unitaire pour la fonction verifsexe
		:return:
		"""
		verifsexe()
		x_fichier = open("resources/numNatOkAndSexe.csv", "r")
	
	def test_nbre_nat(self):
		"""
		Test unitaire pour la fonction nbre_nat
		:return:
		"""
		nbre_nat()
		x_fichier = open("resources/num_nat.data", "r")
