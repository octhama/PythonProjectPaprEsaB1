# Annee bissextile

annee = int(input("Entrez une annee: "))
if annee % 4 == 0:
    if annee % 100 == 0:
        if annee % 400 == 0:
            print("L'annee est bissextile")
        else:
            print("L'annee n'est pas bissextile")
    else:
        print("L'annee est bissextile")
else:
    print("L'annee n'est pas bissextile")
