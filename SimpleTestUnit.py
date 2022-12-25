from PjtUserSuperVersion import check_email

assert check_email("utilisateur@domaine.com") == True
assert check_email("utilisateur@domaine.fr") == True
assert check_email("utilisateur@domaine.co.uk") == True
assert check_email("utilisateur.nom@domaine.com") == True
assert check_email("utilisateur-nom@domaine.com") == True
assert check_email("utilisateur@domaine.") == False
assert check_email("utilisateur@.domaine") == False
assert check_email("@domaine.com") == False
assert check_email("utilisateur@") == False
assert check_email("") == False
