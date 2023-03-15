def pair(n):
    if n == 0:
        return True
    else:
        return impair(n - 1)


def impair(n):
    if n == 0:
        return False
    else:
        return pair(n - 1)


def somme(tab_nbr):
    s = 0
    for nbr in tab_nbr:
        s += nbr
    return s


def somme_recu(tab_nbr):
    if len(tab_nbr) == 0:
        return 0
    else:
        return tab_nbr[0] + somme_recu(tab_nbr[1:])


for i in range(10):
    print(i, "pair : ", pair(i))
    print(i, "impair : ", impair(i))
