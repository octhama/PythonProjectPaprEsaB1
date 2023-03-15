matrice = [[12, 7],
           [4, 5],
           [3, 8],
           [9, 2],
           [10, 5]]
# avec les lists compréhensions :-)
matrice_transpose_v3 = [[matrice[j][i] for j in range(len(matrice))] for i in range(len(matrice[0]))]
print("Matrice de base : ")
for r in matrice:
    print(r)
    print("Version 3 : ")
for r in matrice_transpose_v3:
    print(r)
