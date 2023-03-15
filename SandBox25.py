# initialisation du dictionnaire
dico = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

# affichage du dictionnaire
print(dico)
# Echange clés & valeurs d'un dictionnaire
dico_inverse = {}
for c, v in dico.items():
    dico_inverse[v] = c
# affichage du dictionnaire inversé
print(dico_inverse)
