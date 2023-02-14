code_morse = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
    "J": ".---", " K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-",
    "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..", "À": ".-..-", "É": "..-..", "È": ".-..-", "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", ".": ".-.-.-", ",": "--..--",
    "?": "..--..", "'": ".----.", "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-", "&": ".-...",
    ":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-", "_": "..--.-", "\"": ".-..-.",
    "$": "...-..-", "@": ".--.-."
}


def mot_morse(morse):
    mot = ""
    for caractere in morse.split(" "):
        for cle, valeur in code_morse.items():
            if caractere == valeur:
                mot += cle
    return mot


def phrase_morse(morse):
    phrase = ""
    for mot in morse.split("/"):
        phrase += mot_morse(mot) + " "
    return phrase


# input("Entrer le code morse à traduire : ")
# if code_morse.get(input("Entrer le code morse à traduire : ")) is not None:
print(mot_morse(input("Entrer le code morse à traduire en mot : ")))
# else:
# print("Le code morse n'existe pas")
print(phrase_morse(input("Entrer le code morse à traduire en phrase : ")))
