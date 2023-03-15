def fibonacci(n):
    """
    Calcule les n premiers termes de la suite de Fibonacci.
    """
    # Initialisation des deux premiers termes
    a, b = 0, 1
    # Liste pour stocker les termes de la suite
    fibonacci_list = []
    # Boucle pour calculer les termes suivants et les ajouter à la liste
    for i in range(n):
        fibonacci_list.append(b)
        a, b = b, a + b
    return fibonacci_list


# Exemple d'utilisation
n = 10
fibonacci_list = fibonacci(n)
print(f"Les {n} premiers termes de la suite de Fibonacci sont : {fibonacci_list}")
