def suite_numerique(n):
    """
    Calcule le n-ième terme de la suite numérique définie par récurrence :
    un+1 = 2*un + 1 pour n >= 0, avec u0 = 0
    """
    if n == 0:
        return 0
    else:
        return 2 * suite_numerique(n - 1) + 1


# Exemple d'utilisation
n = 5
termes = [suite_numerique(i) for i in range(n + 1)]
print(f"Les {n + 1} premiers termes de la suite numérique sont : {termes}")
