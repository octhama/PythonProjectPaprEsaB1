# Help source for pattern: 4PAPR ESA 2022 Python-Algo Course by Pr. André NUYENS
# Pattern scripting by Hasler TEHOU aka Octhama

cote = round(float(input("Entrez une cote comprise entre 0 et 20 : ")))
match cote:
    case 0:
        print("échec (%s)" % cote)
    case 1:
        print("échec (%s)" % cote)
    case 2:
        print("échec (%s)" % cote)
    case 3:
        print("échec (%s)" % cote)
    case 4:
        print("échec (%s)" % cote)
    case 5:
        print("échec (%s)" % cote)
    case 6:
        print("échec (%s)" % cote)
    case 7:
        print("échec (%s)" % cote)
    case 8:
        print("échec (%s)" % cote)
    case 9:
        print("échec (%s)" % cote)
    case 10:
        print("réussis sans mention (%s)" % cote)
    case 11:
        print("réussis sans mention (%s)" % cote)
    case 12:
        print("réussis avec satisfaction (%s)" % cote)
    case 13:
        print("réussis avec satisfaction (%s)" % cote)
    case 14:
        print("réussis avec distinction (%s)" % cote)
    case 15:
        print("réussis avec distinction (%s)" % cote)
    case 16:
        print("réussis avec grande distinction (%s)" % cote)
    case 17:
        print("réussis avec grande distinction (%s)" % cote)
    case 18:
        print("réussis avec la plus grande distinction (%s)" % cote)
    case 19:
        print("réussis avec la plus grande distinction (%s)" % cote)
    case 20:
        print("réussis avec la plus grande distinction (%s)" % cote)
    case _:
        print("La côte introduite est mauvaise (%s)" % cote)
