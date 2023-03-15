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

# Auteur: Hasler TEHOU
