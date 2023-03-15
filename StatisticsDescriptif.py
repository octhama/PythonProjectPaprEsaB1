import matplotlib.pyplot as plt  # Pour tracer les graphiques
from pandas.core.algorithms import mode


# Calculer la moyenne
def trouver_moyenne(x_tab):
    somme = 0
    for x in x_tab:
        somme += x
    return somme / len(x_tab)


# Calculer la médiane
def trouver_mediane(x_tab):
    x_tab.sort()
    if len(x_tab) % 2 == 0:
        return (x_tab[len(x_tab) // 2] + x_tab[len(x_tab) // 2 - 1]) / 2
    else:
        return x_tab[len(x_tab) // 2]


# Calculer la variance
def trouver_variance(x_tab):
    somme = 0
    for x in x_tab:
        somme += (x - trouver_moyenne(x_tab)) ** 2
    return somme / len(x_tab)


# Calculer l'écart-type
def trouver_ecart_type(x_tab):
    return trouver_variance(x_tab) ** 0.5


# Calculer la moyenne et l'écart-type du x_tab
def trouver_moyenne_et_ecart_type(x_tab):
    somme = 0
    for x in x_tab:
        somme += x
    mean = somme / len(x_tab)
    somme = 0
    for x in x_tab:
        somme += (x - mean) ** 2
    std = (somme / len(x_tab)) ** 0.5
    return mean, std


def trouver_coefficient_variation(x_tab):
    return trouver_ecart_type(x_tab) / trouver_moyenne(x_tab)


# Calculer le coefficient d'asymétrie
def trouver_coefficient_asymetrie(x_tab):
    somme = 0
    for x in x_tab:
        somme += (x - trouver_moyenne(x_tab)) ** 3
    return somme / len(x_tab) / trouver_variance(x_tab) ** 1.5


# Calculer le coefficient d'aplatissement
def trouver_coefficient_aplatissement(x_tab):
    somme = 0
    for x in x_tab:
        somme += (x - trouver_moyenne(x_tab)) ** 4
    return somme / len(x_tab) / trouver_variance(x_tab) ** 2 - 3


def trouver_mode(x_tab):
    return mode(x_tab)


def trouver_valeur_min(x_tab):
    return min(x_tab)


def trouver_valeur_max(x_tab):
    return max(x_tab)


def trouver_quartiles(x_tab):
    x_tab.sort()
    if len(x_tab) % 2 == 0:
        q1 = (x_tab[len(x_tab) // 4] + x_tab[len(x_tab) // 4 - 1]) / 2
        q3 = (x_tab[len(x_tab) * 3 // 4] + x_tab[len(x_tab) * 3 // 4 - 1]) / 2
    else:
        q1 = x_tab[len(x_tab) // 4]
        q3 = x_tab[len(x_tab) * 3 // 4]
    return q1, q3


def trouver_valeur_interquartile(x_tab):
    q1, q3 = trouver_quartiles(x_tab)
    return q3 - q1


def importer_tableau_excel(nom_fichier, nom_feuille):
    import pandas as pd
    df = pd.read_excel(nom_fichier, sheet_name=nom_feuille, header=0)
    return df.values.tolist()


# Créer un tableau de données
tab = [5, 17, 19, 13, 10, 17, 17, 19, 14, 5, 5, 9, 20, 7, 12, 18, 19, 15, 12, 1, 14, 10, 9, 13, 7, 20, 19, 17, 16,
       16, 10, 8, 17, 2, 5, 18, 10, 5, 8, 7, 4, 14, 15, 17, 18, 15, 8, 12, 6, 17, 19, 20, 1, 12, 4, 3, 12, 18, 19,
       20, 11, 1, 10, 6, 14, 9, 2, 8, 18, 14, 16, 17, 7, 15, 4, 18, 19, 13, 13, 9, 13, 7, 16, 18, 18, 20, 16, 4, 13,
       15, 8, 14, 6, 18, 11, 2, 16, 16, 8, 17, 20, 7, 11, 8, 19, 19, 19, 1, 6, 10, 16, 15, 7, 5, 4, 6, 7, 4, 2, 19,
       17, 15, 4, 10, 4, 7, 18, 6, 3, 8, 12, 20, 18, 12, 19, 19, 3, 3, 16, 6, 20, 9, 18, 8, 10, 15, 4, 9, 12, 6, 10,
       16, 19, 13, 3, 20, 7, 8, 5, 18, 17, 18, 17, 13, 12, 13, 3, 12, 7, 3, 18, 19, 8, 15, 14, 20, 1, 8, 20, 17, 7,
       8, 16, 9, 6, 20, 18, 12, 17, 20, 14, 20, 13, 6, 11, 16, 3, 13, 11, 16, 16, 5, 11, 19, 20, 20, 20, 18, 16, 2,
       8, 18, 5, 12, 9, 15, 2, 12, 1, 8, 19, 1, 19, 18, 17, 1, 3, 2, 14, 10, 16, 15, 13, 10, 9, 2, 17, 12, 16, 19,
       10, 9, 16, 18, 7, 14, 13, 5, 7, 7, 1, 4, 13, 10, 10, 3, 5, 19, 2, 14, 12, 5, 15, 14, 1, 6, 1, 5, 2, 19, 8,
       18, 2, 9, 4, 11, 12, 4, 13, 4, 8, 12, 6, 18, 14, 6, 11, 8, 15, 3, 13, 11, 5, 13, 8, 14, 19, 14, 10, 13, 17,
       11, 18, 16, 1, 18, 13, 4, 13, 17, 1, 9, 6, 3, 17, 14, 4, 5, 2, 12, 17, 1, 20, 3, 8, 16, 12, 4, 5, 13, 5, 4,
       16, 10, 10, 5, 19, 14, 17, 5, 11, 7, 20, 12, 2, 20, 12, 9, 6, 11, 6, 9, 9, 2, 19, 8, 8, 20, 18, 11, 3, 7, 12,
       7, 15, 5, 2, 20, 5, 14, 14, 17, 17, 12, 4, 14, 7, 12, 6, 10, 16, 1, 9, 3, 18, 13, 10, 7, 16, 8, 7, 2, 1, 6,
       20, 3, 2, 9, 16, 18, 19, 12, 12, 20, 4, 10, 11, 14, 11, 7, 7, 5, 4, 1, 11, 13, 13, 2, 7, 19, 14, 14, 20, 9,
       4, 13, 4, 6, 18, 11, 18, 14, 8, 8, 7, 10, 4, 15, 10, 12, 19, 20, 5, 6, 5, 16, 6, 7, 17, 12, 11, 7, 10, 14, 2,
       13, 15, 20, 15, 18, 9, 13, 10, 7, 2, 6, 12, 3, 16, 16, 11, 10, 5, 18, 20, 4, 3, 16, 2, 12, 12, 5, 13, 13, 4,
       14, 5, 15, 9, 6, 18, 13, 1, 1, 14, 3, 6, 14, 12, 14, 8, 1, 20, 4, 14, 6, 18, 1, 5, 4, 15, 5, 15, 5, 6, 17,
       20, 20, 7, 12, 13, 17, 2, 17, 2, 9, 10, 3, 11, 16, 1, 5, 17, 8, 10, 8, 3, 10, 14, 4, 10, 11, 16, 19, 3, 17,
       17, 1, 3, 6, 4, 4, 20, 6, 15, 12, 17, 18, 17, 3, 11, 16, 17, 5, 8, 4, 3, 2, 19, 11, 10, 10, 5, 18, 16, 12, 5,
       20, 2, 6, 17, 19, 19, 6, 12, 13, 6, 13, 16, 18, 11, 9, 6, 7, 18, 1, 16, 17, 14, 8, 2, 11, 9, 6, 8, 20, 13, 6,
       18, 3, 4, 13, 6, 13, 15, 7, 9, 20, 2, 9, 15, 9, 14, 15, 7]

# Afficher les statistiques
print("Moyenne : ", round(trouver_moyenne(tab), 2))
print("Médiane : ", trouver_mediane(tab))
print("Mode : ", trouver_mode(tab))
print("Coefficient de variation : ", round(trouver_coefficient_variation(tab), 2))
print("Coefficient d'asymétrie : ", round(trouver_coefficient_asymetrie(tab), 2))
print("Coefficient d'aplatissement : ", round(trouver_coefficient_aplatissement(tab), 2))
print("Variance : ", round(trouver_variance(tab), 2))
print("Ecart-type : ", round(trouver_ecart_type(tab), 2))
print("Valeur minimale : ", round(trouver_valeur_min(tab), 2))
print("Valeur maximale : ", trouver_valeur_max(tab))
print("Quartiles : ", trouver_quartiles(tab))
print("Valeur interquartile : ", trouver_valeur_interquartile(tab))

# Graphique de la distribution
plt.hist(tab, bins=20)
plt.title("Distribution des valeurs")
plt.xlabel("Valeurs")
plt.ylabel("Fréquence")

# Afficher la médiane
plt.axvline(trouver_mediane(tab), color='r', linestyle='dashed', linewidth=2)

# Afficher la moyenne
plt.axvline(trouver_moyenne(tab), color='g', linestyle='dashed', linewidth=2)

# Afficher le mode
plt.axvline(trouver_mode(tab), color='c', linestyle='dashed', linewidth=2)

# Afficher le coefficient de variation
plt.axvline(trouver_coefficient_variation(tab), color='m', linestyle='dashed', linewidth=2)

# Afficher le coefficient d'asymétrie
plt.axvline(trouver_coefficient_asymetrie(tab), color='y', linestyle='dashed', linewidth=2)

# Afficher le coefficient d'aplatissement
plt.axvline(trouver_coefficient_aplatissement(tab), color='b', linestyle='dashed', linewidth=2)

# Afficher une ligne pour l'écart-type
plt.axvline(trouver_moyenne(tab) + trouver_ecart_type(tab), color='b', linestyle='dashed', linewidth=2)
plt.axvline(trouver_moyenne(tab) - trouver_ecart_type(tab), color='b', linestyle='dashed', linewidth=2)

# Afficher une ligne pour la variance
plt.axvline(trouver_moyenne(tab) + trouver_variance(tab), color='y', linestyle='dashed', linewidth=2)
plt.axvline(trouver_moyenne(tab) - trouver_variance(tab), color='y', linestyle='dashed', linewidth=2)

# Légende
plt.legend(['Médiane', 'Moyenne', 'Mode', 'Coefficient de variation', 'Coefficient d\'asymétrie',
            'Coefficient d\'aplatissement', 'Ecart-type', 'Variance'])

# Afficher le graphique
plt.show()
