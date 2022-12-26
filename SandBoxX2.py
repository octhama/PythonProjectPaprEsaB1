# Définition des constantes
HAUTEUR_SAPIN = 10

# Dessin de la base du sapin
for i in range(HAUTEUR_SAPIN):
    print(" " * (HAUTEUR_SAPIN - i - 1) + "*" * (2 * i + 1))

# Dessin du tronc du sapin
print(" " * (HAUTEUR_SAPIN - 1) + "*")
