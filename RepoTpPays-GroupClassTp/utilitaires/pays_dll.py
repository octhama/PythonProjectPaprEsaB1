def ouvrir_fichier(x_chemin_fichier):
    """

    :param x_chemin_fichier: Chemin du fichier à ouvrir (str)
    :return: Retourne le fichier ouvert
    """
    try:  # Essayer d'ouvrir le fichier (str)
        x_fichier = open(x_chemin_fichier, 'r', encoding='UTF-8')  # Ouvrir le fichier en mode lecture (r) (str)
    except FileNotFoundError:  # Si le fichier n'existe pas
        return None  # Retourner None
    return x_fichier  # Retourner le fichier ouvert


def fermer_fichier(x_fichier):
    """

    :param x_fichier: Fichier à fermer
    :return: None
    """
    x_fichier.close()  # Fermer le fichier (str)


def charger_le_fichier(x_fichier):
    """

    :param x_fichier: Fichier à charger (str)
    :return: Retourne une liste de dictionnaires contenant les informations des pays
    """
    resultat = []
    lignes = x_fichier.readline()
    prem_ligne = lignes[0]  # Première ligne du fichier (contient les noms des colonnes) (str)
    for ligne in lignes[1:]:  # Parcourir chaque ligne du fichier (sauf la première) (str)
        pays = {}
        for i, cle in enumerate(prem_ligne.split("|")):  # Parcourir chaque colonne du fichier (str)
            pays[cle] = ligne[i].split("|")  # Ajouter les noms des colonnes comme clés et les valeurs de chaque ligne
            # comme valeurs (str)
            # clés et les valeurs de chaque ligne comme valeurs (str)
        resultat.append(pays)  # Ajouter le dictionnaire à la liste de dictionnaires (list)
    return resultat  # Retourner la liste de dictionnaires (list)


def choix_pays_code(x_list_pays, x_code):
    """

    :param x_list_pays: liste de dictionnaires contenant les informations des pays (list)
    :param x_code: code numérique ou alpha-2 du pays (str)
    :return: Retourne le nom du pays correspondant au code numérique ou alpha-2
    """
    if str(x_code).isnumeric():  # Si le code est numérique
        cle = "Code numérique"  # Utiliser le code numérique comme clé
    else:
        cle = "Code Alpha-2"  # Utiliser le code alpha-2 comme clé
    for pays in x_list_pays:
        if pays[cle] == x_code:  # Si le code du pays est égal au code entré
            return pays['Nom français']  # Retourner le nom du pays (str)
        else:
            return None  # Retourner None si le code n'est pas trouvé (str)


def compte_continent(x_liste_pays):
    dico_continent = {}  # Dictionnaire vide (dict)
    for pays in x_liste_pays:  # Parcourir chaque pays de la liste de dictionnaires (list)
        if pays['Continent'] in dico_continent:  # Si le continent du pays est déjà dans le dictionnaire
            dico_continent[pays['Continent']] += 1  # Ajouter 1 à la valeur du continent du pays
        else:
            dico_continent[pays['Continent']] = 1  # Ajouter le continent du pays au dictionnaire avec une valeur de 1
    return dico_continent  # Retourner le dictionnaire (dict)


def pays_sans_capital(x_liste_pays):
    for pays in x_liste_pays:  # Parcourir chaque pays de la liste de dictionnaires (list)
        if pays['Capital'] == "-":  # Si le pays n'a pas de capitale
            print(pays['Nom français'], end="\t")  # Afficher le nom du pays (str)
    print()  # Retourner à la ligne (str)
    

