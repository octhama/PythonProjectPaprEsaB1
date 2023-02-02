ensemble_lettre = set(['a', 'b', 'c', 'd'])
ensemble_chiffre = set([1, 2, 3, 4])
if ensemble_lettre.isdisjoint(ensemble_chiffre):
    print("Les deux ensembles sont disjoints")
else:
    print("Les deux ensembles ne sont pas disjoints")
print(ensemble_lettre)
print(ensemble_chiffre)
