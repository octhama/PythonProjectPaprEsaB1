def inverse_tableau(t):
    t2 = []
    for elt in t[::-1]:
        t2.append(elt)
    return t2


tab = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(inverse_tableau(tab))
