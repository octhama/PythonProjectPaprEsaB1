code_morse_dico = {'A': '• –', 'B': '– • • •', 'C': '– • – •', 'D': '– • •', 'E': '•', 'F': '• • – •', 'G': '– – •',
                   'H': '• • • •', 'I': '• •', 'J': '• – – –', 'K': '– • –', 'L': '• – • •', 'M': '– –', 'N': '– •',
                   'O': '– – –', 'P': '• – – •', 'Q': '– – • –', 'R': '• – •', 'S': '• • •', 'T': '–', 'U': '• • –',
                   'V': '• • • –', 'W': '• – –',
                   'X': '– • • –', 'Y': '– • – –', 'Z': '– – • •', '.': '• – • – • –', '?': '• • – – • •',
                   '!': '– • – • – –', '@': '• – – • – •'}
mot = input("Entrer le mot à morser : ")
mot_morse = ""
for caractere in mot:
    for cle, valeur in code_morse_dico.items():
        if caractere == cle:
            mot_morse += valeur
print(mot_morse)
inverse_code_morse_dico = {valeur: cle for cle, valeur in code_morse_dico.items()}
mot_morse = input("Entrer le mot morse à décoder : ")
mot = ""    # Initialiser le mot à décoder (str)
mot_morse += " "    # Ajouter un espace à la fin du mot morse pour que la boucle while s'arrête
mot_morse_temp = ""    # Initialiser le mot morse temporaire (str)
while mot_morse != "":
    if mot_morse[0] != " ":
        mot_morse_temp += mot_morse[0]
        mot_morse = mot_morse[1:]
    else:
        mot_morse = mot_morse[1:]
        for cle, valeur in inverse_code_morse_dico.items():
            if mot_morse_temp == cle:
                mot += valeur
        mot_morse_temp = ""
print(mot)
# • • • •–•• • • •– – –• • –

# Auteur: Hasler TEHOU
# Date: 2020-10-20
# • • • •–•• • • •– – –• • –
