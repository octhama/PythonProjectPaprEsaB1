from random import choice

# Dictionnaire de caractères et de leur code morse
code_morse = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
    "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-",
    "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..", "À": ".-..-", "É": "..-..", "È": ".-..-", "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", ".": ".-.-.-", ",": "--..--",
    "?": "..--..", "'": ".----.", "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-", "&": ".-...",
    ":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-", "_": "..--.-", "\"": ".-..-.",
    "$": "...-..-", "@": ".--.-."
}
# Liste de morse de pays
morse_pays = [
    "-... . .-.. --. .. --.- ..- .",  # BELGIQUE
    "-... ..-.. -. .. -.",  # BENIN
    "-- .- .-. --- -.-.",  # MAROC
    ".- .-.. .-.. . -- .- --. -. .",  # ALLEMAGNE
    "..-. .-. .- -. -.-. .",  # FRANCE
    ". --. -.-- .--. - .",  # EGYPTE
    "-.-. .- -- . .-. --- ..- -.",  # CAMEROUN
    "-.-. .- -. .- -.. .-",  # CANADA
    "..-.. .-. -.-- - .... .-. ..-.. .",  # ERYTHREE
    "-.-. .... .. -. . ",  # CHINE
    "... ..-.. -. ..-.. --. .- .-..",  # SENEGAL
    "... ..- .. ... ... ."  # SUISSE
]
# Liste de morse de phrases
morse_phrases = [".--- .  / ... ..- .. ...  / -. .. -.-. --- .-.. .- ...",
                 ".--- .  / ... ..- .. ...  / ..-.. -- .. .-.. .. .",
                 ".--- .  / ... ..- .. ...  / .. -... .-. .- .... .. -- ",
                 ".--- .  / ... ..- .. ...  / . ... - . .-.. .-.. .",
                 "-. --- ..- ...  / ... --- -- -- . ...  / ..-.. - ..- -.. .. .- -. - ...  / . -.  / -... .- -.-.  / "
                 ".. -. ..-. ---  / .---- ",
                 "-... --- -. .--- --- ..- .-. -....-  / .--- .  / -- -.--. .- .--. .--. . .-.. .-.. .  / -... .. .-.. "]
# Liste de morse de fruits
morse_fruits = [".--. --- -- -- .",  # POMME
                ".-. .- .. ... .. -.",  # ORANGE
                "--- .-. .- -. --. .",  # BANANE
                "-- .- -. --. ..- .",  # MANGUE
                ".- -. .- -. .- ...",  # ANANAS
                ]
# Liste de morse d'animaux
morse_animaux = ["-.-. .... .- - ",  # CHAT
                 "-.-. .... .. . -.",  # CHIEN
                 "-.-. .... .- -- . .- ..-",  # CHAMEAU
                 "-.-. .... . ...- .- .-..",  # CHEVAL
                 "-.-. .... --- ..- . - - . ",  # CHOUETTE
                 ]
# Liste de morse de numéros de GSM
morse_numeros_gsm = ["----- ....- --... -----  / .---- .----  / ..--- ..---  / ...-- ...-- ",
                     "----- ....- ---.. -----  / .---- .----  / ..--- ..---  / ...-- ...-- ",
                     "----- ....- ---.. -----  / ..--- ..---  / ....- -----  / ...-- ...-- ",
                     "----- ....- ----. -----  / ----- -----  / -.... -----  / ...-- ..--- ",
                     "----- ....- ---.. ---..  / ---.. ---..  / -.... --...  / ..--- -.... "]


def morse_en_mot_francais(x_mot_en_morse):  # On définit la fonction qui traduit un mot en morse en français
    """Traduit un mot en morse en français"""
    mot_traduit = ""  # On initialise le mot traduit
    for caractere in x_mot_en_morse.split():  # On découpe le mot en morse en caractères morse
        for cle, valeur in code_morse.items():  # On parcourt le dictionnaire
            if caractere == valeur:  # On cherche le caractère correspondant au code morse
                mot_traduit += cle  # On ajoute le caractère traduit au mot
    return mot_traduit  # On retourne le mot traduit


def phrase_en_morse(x_phrase_en_morse):  # On définit la fonction qui traduit une phrase en morse en français
    """Traduit une phrase en morse en français"""
    phrase_traduite = ""  # On initialise la phrase traduite
    for mot in x_phrase_en_morse.split("/"):  # On découpe la phrase en morse en mots en morse séparés par
        # un "/" (espace)
        phrase_traduite += morse_en_mot_francais(mot) + " "  # On traduit chaque mot et on ajoute un espace à la fin
        # du mot traduit à la phrase traduite
    return phrase_traduite  # On retourne la phrase traduite en français sans le dernier espace en trop à la fin de la
    # phrase traduite (qui est ajouté par la boucle for)


# morse = input("Mot ou phrase en morse : ")
morse = choice(morse_pays)  # On choisit un morse aléatoire dans la liste du morse
if "/" in morse:  # On vérifie si le morse est une phrase ou un mot en morse (si il y a un "/" dans le morse,
    # c'est une phrase)
    print(phrase_en_morse(morse))  # On appelle la fonction qui traduit une phrase en morse en français
else:
    print(morse_en_mot_francais(morse))  # On appelle la fonction qui traduit un mot en morse en français
