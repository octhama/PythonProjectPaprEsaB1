def mdp_verif(x_mdp):
    """
    :param x_mdp: variable en paramètre dans la fonction permettant de récupérer le mot de passe
    :return: pour le premier return l'instruction conditionnelle doit retourner False si la taille du mot de passe n'est
    pas respecté
    :return: le deuxième return de la boucle imbriquant des instructions conditionnelles renvoie chaque élément de la
    chaine de caractère à vérifier si les conditions y référent sont respectés

    Cette fonction vérifie d'abord la longueur du mot de passe. Si le mot de passe a moins de 10 caractères, la fonction
    retourne False, sinon elle parcourt les caractères du mot de passe et utilise les fonctions islower, isupper et
    isdigit de chaque caractère pour vérifier s'il s'agit d'une lettre minuscule, majuscule ou chiffre. Si au moins une
    lettre minuscule, une lettre majuscule et un chiffre sont présents, la fonction retourne True. Sinon, elle retourne
    False.
    """
    print(x_mdp.lower())

    if len(mdp) > 10:
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
    return minuscules and majuscules and chiffres


mdp = input("Entrer un mot de passe...")
if mdp_verif(mdp):
    print("Le mot de passe est valide.")
else:
    print("Le mot de passe n'est pas valide.")

print(mdp_verif.__doc__)
