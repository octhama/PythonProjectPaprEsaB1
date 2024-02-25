import requests
from bs4 import BeautifulSoup
import csv

# URL de la page à scraper
url = "https://www.ludum.fr/blog/les-100-meilleurs-jeux-de-societe-n313"

# Effectuer une requête GET à l'URL
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Analyser le contenu HTML de la page
    soup = BeautifulSoup(response.text, "html.parser")

    # Initialiser des listes pour stocker les données
    indices = []
    noms = []
    descriptions = []
    editeurs = []
    nombres_joueurs = []
    ages_joueurs = []

    # Initialiser l'indice à 1
    index = 1

    # Trouver les éléments HTML contenant les données que vous souhaitez extraire
    # (Assurez-vous d'adapter ces sélecteurs CSS à la structure de votre page HTML)
    jeux = soup.find_all("div", class_="jeu")

    # Parcourir les jeux trouvés et extraire les données
    for jeu in jeux:
        # Index
        indices.append(index)

        # Nom
        nom = jeu.find("h2", class_="nom").text.strip()
        noms.append(nom)

        # Description
        description = jeu.find("p", class_="description").text.strip()
        descriptions.append(description)

        # Éditeur
        editeur = jeu.find("span", class_="editeur").text.strip()
        editeurs.append(editeur)

        # Nombre de joueurs
        nombre_joueurs = jeu.find("span", class_="nombre_joueurs").text.strip()
        nombres_joueurs.append(nombre_joueurs)

        # Âge du joueur
        age_joueur = jeu.find("span", class_="age_joueur").text.strip()
        ages_joueurs.append(age_joueur)

        # Incrémenter l'indice
        index += 1

    # Écrire les données dans un fichier CSV
    with open("donnees_jeux.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Index", "Nom", "Description", "Éditeur", "Nombre de joueurs", "Âge du joueur"])
        for data in zip(indices, noms, descriptions, editeurs, nombres_joueurs, ages_joueurs):
            writer.writerow(data)
else:
    print("La requête a échoué avec le code de statut:", response.status_code)
