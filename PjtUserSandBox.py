def input_information():
    # Vérifie que le nom et le prénom n'ont pas la même longueur
    if len(name) == len(first_name):
        print("Le nom et le prénom ne peuvent pas avoir la même longueur.")
        return

    # Vérifie que le nom et le prénom ne contiennent que des lettres et des traits d'union
    if not all(c.isalpha() or c == "-" for c in name) or not all(c.isalpha() or c == "-" for c in first_name):
        print("Le nom et le prénom ne peuvent contenir que des lettres et des traits d'union.")
        return

    # Vérifie que l'adresse email est au bon format et ne contient pas de caractères spéciaux autres que le "." ou le
    # "-"
    if "." not in email or "@" not in email or not all(c.isalnum() or c == "." or c == "-" or c == "@" for c in email):
        print("L'adresse email n'est pas au bon format ou contient des caractères spéciaux non autorisés.")
        return

    # Vérifie que le login ne contient que des caractères en minuscules et n'a pas de caractères spéciaux
    # Vérifie que le login ne contient que des caractères en minuscules et n'a pas de caractères spéciaux
    if not login.islower() or not all(c.isalpha() or c.isdigit() for c in login):
        print(
            "Le login ne peut contenir que des lettres et des chiffres en minuscules et ne peut pas avoir de "
            "caractères spéciaux.")
        return

    # Vérifie que le mot de passe à au moins 10 caractères et comprend au moins une majuscule, une minuscule,
    # un chiffre et un caractère spécial
    if len(password) < 10 or not any(c.isupper() for c in password) or not any(c.islower() for c in password) \
            or not any(c.isdigit() for c in password) or not any(not c.isalnum() for c in password):
        print("Le mot de passe doit avoir au moins 10 caractères et comprendre au moins une "
              "majuscule, une minuscule, un chiffre et un caractère spécial.")
        return

    # Affiche les éléments précédemment entrés


name = input("Entrez votre nom : ")
first_name = input("Entrez votre prénom : ")
postal_code = input("Entrez votre code postal : ")
email = input("Entrez votre adresse email : ")
login = input("Entrez votre login : ")
password = input("Entrez votre mot de passe : ")

print("Nom : ", input_information(name))
print("Prénom : ", input_information(first_name))
print("Code postal : ", input_information(postal_code))
print("Email : ", input_information(email))
print("Login : ", input_information(login))
print("Mot de passe : ", input_information(password))
