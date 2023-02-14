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


def translate_morse_word(word):
    translated_word = ""
    for character in word.split(" "):
        if character in code_morse.values():
            for key, value in code_morse.items():
                if character == value:
                    translated_word += key
        else:
            return "Invalid Morse code"
    return translated_word


def translate_morse_phrase(phrase):
    translated_phrase = ""
    words = phrase.split("/")
    for word in words:
        translated_word = translate_morse_word(word)
        if translated_word == "Invalid Morse code":
            return "Invalid Morse code"
        else:
            translated_phrase += translated_word + " "
    return translated_phrase


morse = input("Enter Morse code to translate (use / for words separation): ")

if "/" in morse:
    print(translate_morse_phrase(morse))
else:
    print(translate_morse_word(morse))
