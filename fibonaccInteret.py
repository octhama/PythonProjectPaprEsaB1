def fibonacci_interest(P, r, n):
    """
    Calcule le montant total dans un compte d'épargne après n années
    avec un taux d'intérêt annuel composé de r, en utilisant la suite de Fibonacci
    avec le montant initial P comme premier terme.
    """
    a, b = P, P * (1 + r)
    for i in range(n - 1):
        a, b = b, b * (1 + r) + a
    return b


# Exemple d'utilisation
montant_initial = int(input("Entrez le montant initial dans le compte : "))
taux_interet_annuel = 0.05  # 5%
annees = 4
montant_total = fibonacci_interest(montant_initial, taux_interet_annuel, annees)
print("Le montant total dans le compte après", annees, "années est de", montant_total, "euros.")
