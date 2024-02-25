def generate_tab(nbr, min, max):
    """

    :param nbr: Nombre d'éléments
    :param min: Nombre minimum qu'on retrouve dans le tableau
    :param max: Nombre Maximum qu'on retrouve dans le tableau
    :return: Retourne un tableau de "nbr" élément compris entre [min et max]
    """
    from random import randint
    _tab = []
    for i in range(nbr):
        _tab.append(randint(min, max+1))
    return _tab


def is_in_tab(element, tableau):
    """

    :param element:
    :param tableau:
    :return: Vrai, si l'élément est trouvé, sinon retourne faux
    """
    return element in tableau


tab = generate_tab(10, 0, 5)
print(tab)
print(is_in_tab(4, tab))
