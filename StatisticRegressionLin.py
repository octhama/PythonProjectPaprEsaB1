import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt


def importer_tableau_excel(nom_fichier, nom_feuille):
    import xlrd
    wb = xlrd.open_workbook(nom_fichier)
    sh = wb.sheet_by_name(nom_feuille)
    x_tab = []
    for row_num in range(sh.nrows):
        tableau.append(sh.row_values(row_num))
    return tableau


# Créer un tableau de données
tableau = [[40, 41], [38, 45], [66, 56], [80, 79], [62, 57], [38, 41], [16, 13], [72, 71], [43, 45], [61, 56],
           [37, 32], [52, 56], [38, 38], [88, 82], [82, 90], [50, 55], [58, 65], [79, 87], [65, 58], [74, 71]]

# Séparer les deux variables en deux tableaux distincts
x = []
y = []
for elt in tableau:
    x.append(elt[0])
    y.append(elt[1])

# Calculer le coefficient de corrélation linéaire et l'afficher arrondi à 2 chiffres après la virgule
r = linregress(x, y).rvalue
print("Le coefficient de corrélation linéaire est r =", round(r, 2))

# Calculer la droite de régression linéaire et afficher les paramètres "a" et "b"
slope, intercept, r_value, p_value, std_err = linregress(x, y)
print("La droite de régression linéaire est y = {0}x + {1}".format(round(slope, 2), round(intercept, 2)))

# Afficher les paramètres "a" et "b"
print("a =", round(slope, 2))
print("b =", round(intercept, 2))

# Valeur de y sachant que x = 50 pour la Session 1
valeur_session_1 = round(intercept, 2) + round(slope, 2) * 50
print("Valeur de y pour la Session 1 est donc : ", round(valeur_session_1, 2))

# Valeur de x sachant que y = 72 pour la Session 2
valeur_session_2 = (72 - round(intercept, 2)) / round(slope, 2)
print("Valeur de x pour la Session 2 est donc : ", round(valeur_session_2, 2))

# Tracer les points de données sur un graphique
plt.plot(x, y, 'o')
plt.title("Graphique de la regression linéaire de la série statistique courante")
plt.xlabel("Valeurs")
plt.ylabel("Fréquence")

# Tracer la droite de régression linéaire sur le graphique et l'afficher dans la légende du graphique
x_array = np.array(x)
plt.plot(x_array, intercept + slope * x_array, 'r', label='y = {0}x + {1}'.format(round(slope, 2), round(intercept, 2)))

plt.legend(["Nuage de points", "Droite de régression"])

# Afficher le graphique
plt.show()
