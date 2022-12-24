def mdp_verif(x_mdp):
    """

    :param x_mdp:
    :return:
    """
    if not x_mdp:
        return False
    print(x_mdp.lower())

    if len(x_mdp) < 10:
        return False

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
