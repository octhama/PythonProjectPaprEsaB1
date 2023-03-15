matrice = [[12, 7],
           [4, 5],
           [3, 8],
           [9, 2],
           [10, 5]]
matrice_transpose = [[0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0]]
# itérons sur chaque ligne
for i in range(len(matrice)):
    # itérons sur chaque colonne
    for j in range(len(matrice[i])):
        matrice_transpose[j][i] = matrice[i][j]
        print("Matrice de base : ")
for r in matrice:
    print(r)
    print("Version 1 : ")
for r in matrice_transpose:
    print(r)
