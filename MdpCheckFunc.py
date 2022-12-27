def mdp_verif(x_mdp):
    """

    :param x_mdp: représentant tout mot de passes qui seraient traités par cette fonction
    :return: une première instruction conditionnelle qui renvoie False si aucun mot de passe n'a été encodé.
    La deuxième instruction conditionnelle retourne True si la taille du mot de passe est supérieure ou égale à 10
    caractères. Une boucle itérative examine chaque caractère de la chaine de caractères encodé et faire le compte des
    caractères nécessaire (minuscules, majuscules, chiffres, caractères spéciaux) pour le respect du format du mot
    de passe. Enfin une instruction conditionnelle qui renvoie True si la condition suivante est respecté : minimum des
    minuscules, majuscules, chiffres et caractères spéciaux.
    """
    if not x_mdp:
        return False
    print(x_mdp.lower())

    if len(x_mdp) >= 10:
        return True

    minuscules = 0
    majuscules = 0
    chiffres = 0

    for c in mdp:
        if c.islower():
            minuscules += 1
        elif c.isupper():
            majuscules += 1
        elif c.isdigit():
            chiffres += 1

    if minuscules >= 1 and majuscules >= 1 and chiffres >= 1:
        return True
    else:
        return False


mdp = input("Entrer un mot de passe...")
if mdp_verif(mdp):
    print("Le mot de passe est valide.")
else:
    print("Le mot de passe n'est pas valide.")

print(mdp_verif.__doc__)
