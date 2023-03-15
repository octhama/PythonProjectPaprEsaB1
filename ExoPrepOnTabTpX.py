def verifie_element(x_tab):
    for i in x_tab:
        if i in x_tab:
            return True
        else:
            return False


def check_elem():
    res = []
    for i, elt in enumerate(tab):
        if elt in tab:
            res.append(i)
    return res


def inverse_tab(x_tab):
    for i in x_tab:
        x_tab.reverse()
        return x_tab


def calcul_average(x_tab):
    som_tab = 0
    taille_x_tab = len(x_tab)
    for i in x_tab:
        som_tab += i
    return som_tab / taille_x_tab


# Ecrire une fonction qui permet de calculer la somme des lignes d'une d'une matrice et la sommme des column
# d'une matrice
def somme_matrice(x_matrice):
    som_ligne = 0
    som_colonne = 0
    for i in range(len(x_matrice)):
        som_ligne += i
        for j in range(len(x_matrice)):
            som_colonne += j
    return som_ligne, som_colonne


tab = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tab_2 = []
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
if verifie_element(tab_2):
    print("ok")
else:
    print("pas ok")

print(inverse_tab(tab))

print(calcul_average(tab))

print(somme_matrice(matrice))
