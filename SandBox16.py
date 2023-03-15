def reorder_word(word):
    word_order = ''
    for i in range(0, len(word), 2):
        word_order += word[i + 1] + word[i]
    return word_order


mot = input("Mot : ")
print(reorder_word(mot))
