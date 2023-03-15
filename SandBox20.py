matrice = [[12, 7],
           [4, 5],
           [3, 8],
           [9, 2],
           [10, 5]]
matrice_transpose = [[0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0]]
matrice_transpose_v2 = []
print("Matrice de base : ")
for r in matrice:
    print(r)
    # et une solution pure python :-) Fonction built-in
    matrice_transpose_v4 = zip(*matrice)
    print("Version 4 : ")
for r in matrice_transpose_v4:
    print(r)
