from scipy.stats import linregress

# import matplotlib.pyplot as plt

tableau = [[40, 41], [38, 45], [66, 56], [80, 79], [62, 57], [38, 41], [16, 13], [72, 71], [43, 45], [61, 56],
           [37, 32], [52, 56], [38, 38], [88, 82], [82, 90], [50, 55], [58, 65], [79, 87], [65, 58], [74, 71]]
# Séparer les deux variables en deux tableaux distincts
x = [row[0] for row in tableau]
y = [row[1] for row in tableau]

# Calculer le coefficient de régression
slope, intercept, r_value, p_value, std_err = linregress(x, y)
print("Le coefficient de régression est:", round(slope, 2))

# Afficher les paramètres "a" et "b"
print("a =", round(slope, 2))
print("b =", round(intercept, 2))

# Tracer les points de données sur un graphique
# plt.plot(x, y, "o")

# Tracer la droite de régression linéaire
# plt.plot(x, slope * x + intercept)

# Afficher le graphique
# plt.show()
