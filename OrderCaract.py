def melange_mot(x_mot):  # x_mot = "bonjour"
    mot_melange = ""  # mot_melange = ""
    for i in range(0, len(x_mot), 2):
        mot_melange += x_mot[i:i + 2][::-1]  # mot_melange = "bnuojor"
    return mot_melange  # "bnuojor"


mot = input("Mot : ")  # "bonjour"
print(melange_mot(mot))  # "bnuojor"
