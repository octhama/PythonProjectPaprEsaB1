def reverse_string(s):
    phrase_inverse = ''
    for caractere in s:
        phrase_inverse = caractere + phrase_inverse
    return phrase_inverse


phrase = input("Mot : ")
if phrase == reverse_string(phrase):
    print("ok")
else:
    print(reverse_string(phrase))