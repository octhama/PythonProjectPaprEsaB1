# Sapin de noël

for i in range(1, 11):
    for j in range(1, 11 - i):
        print(".", end="")
    for k in range(1, i + 1):
        print("* ", end="")
    print()
for i in range(1, -11):
    print("*" * 5, end="")
    print()
