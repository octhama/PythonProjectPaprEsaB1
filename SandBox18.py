matrice = [[12, 7],
           [4, 5],
           [3, 8],
           [9, 2],
           [10, 5]]
matrice_transpose_v2 = []
# itérons sur chaque ligne
for i in range(len(matrice[0])):
    t = []
    for line in matrice:
        t.append(line[i])
        matrice_transpose_v2.append(t)
        print("Matrice de base : ")
for r in matrice:
    print(r)
    print("Version 2 : ")
for r in matrice_transpose_v2:
    print(r)
