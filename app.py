def saisir():
    n = int(input("donner un nombre : "))
    while not(3<=n<=20):
        n = int(input("donner un nombre : "))
    return n


n = saisir()