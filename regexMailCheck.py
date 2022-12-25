import re


def check_email(x_email):
    # Si x_email est vide, retourne False
    if not x_email:
        return False

    # Définition de l'expression régulière pour une adresse email valide
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    # Regex for email by Internet Engineering Task Force (IETF) dans la RFC 5322
    # email_regex_1 = r"^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[
    # \x01-\x08\x0b\x0c\x0e-\x1f\ x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[
    # a-z0-9-]*[a-z0-9])?\.)+[a-z0-9]" \ "(?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){
    # 3}(?:25[0-5]|2[0-4][0-9]|[01]?" \ "[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21" Vérifie
    # si l'adresse email respecte l'expression régulière
    if re.match(email_regex, x_email):
        return True
    else:
        return False
