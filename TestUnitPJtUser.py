import unittest

from PjtUserSuperVersion import check_prenom_nom, check_mdp
from PjtUserSuperVersion import check_email


class MyTestCase(unittest.TestCase):
    def test_check_prenom_nom(self):
        self.assertEqual(check_prenom_nom("John"), True)
        self.assertEqual(check_prenom_nom("John-Paul"), True)
        self.assertEqual(check_prenom_nom("John.Paul"), False)
        self.assertEqual(check_prenom_nom("123"), True)
        self.assertEqual(check_prenom_nom(""), False)

    if __name__ == '__main__':
        unittest.main()


class TestEmailCheck(unittest.TestCase):
    def test_valid_emails(self):
        # Testez des adresses email valides
        self.assertTrue(check_email("utilisateur@domaine.com"))
        self.assertTrue(check_email("utilisateur@domaine.fr"))
        self.assertTrue(check_email("utilisateur@domaine.co.uk"))
        self.assertTrue(check_email("utilisateur.nom@domaine.com"))
        self.assertTrue(check_email("utilisateur-nom@domaine.com"))

    def test_invalid_emails(self):
        # Testez des adresses email non valides
        self.assertFalse(check_email("utilisateur@domaine."))
        self.assertFalse(check_email("utilisateur@.domaine"))
        self.assertFalse(check_email("@domaine.com"))
        self.assertFalse(check_email("utilisateur@"))
        self.assertFalse(check_email(""))


if __name__ == '__main__':
    unittest.main()


class TestCheckMdp(unittest.TestCase):
    def test_valid_mdp(self):
        self.assertTrue(check_mdp("aB123$%"))  # doit retourner True car le mot de passe est valide

    def test_invalid_mdp(self):
        self.assertFalse(
            check_mdp("ab123"))  # doit retourner False car le mot de passe n'a pas au moins 1 caractère spécial
        self.assertFalse(
            check_mdp("ABC123"))  # doit retourner False car le mot de passe n'a pas au moins 1 caractère en minuscules
        self.assertFalse(
            check_mdp("abc123"))  # doit retourner False car le mot de passe n'a pas au moins 1 caractère en majuscules
        self.assertFalse(check_mdp("aBc123"))  # doit retourner False car le mot de passe n'a pas au moins 1 chiffre
        self.assertFalse(check_mdp("aBc"))  # doit retourner False car le mot de passe fait moins de 10 caractères
        self.assertFalse(check_mdp(""))  # doit retourner False car le mot de passe est vide


if __name__ == '__main__':
    unittest.main()
    