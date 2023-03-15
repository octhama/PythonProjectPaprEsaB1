def calcul_exposant(x, k):
    """pre: l'exposant doit être différent de 0 (on pourrait ...)
    post: retourne x puissance k"""
    if k == 1:  # cas de base
        return x
    else:
        if (k % 2) == 0:  # c'est pair
            return pow(calcul_exposant(x, k / 2), 2)
        else:  # c'est impair
            return calcul_exposant(x, k - 1) * x


for i in range(1, 5):
    print(calcul_exposant(5, i))
