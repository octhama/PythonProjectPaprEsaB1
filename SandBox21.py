from random import randint


# initialisation de mon tableau
def initialize(nbr_elt, _min, _max):
    t = []
    for i in range(nbr_elt):
        t.append(randint(_min, _max))
    return t


def search_elt(t, x):
    for i, elt in enumerate(t):
        if elt == x:
            return i + 1
    return -1


# début du programme
tab = initialize(10, 0, 100)
print(tab)
nombre = int(input("Entrez un nombre entier : "))
print(tab)
res = search_elt(tab, nombre)
if res >= 0:
    print("{0} se trouve en position {1}".format(nombre, res))
else:
    print("L'élément {0} ne se trouve pas dans le tableau".format(nombre))
    # savoir si l'élément existe
    print("L'élément existe ? ", x in tab)
# connaître l'indice où il se trouve :
if x in tab:
    print("L'élément ", x, " se trouve à l'indice ", tab.index(x))
