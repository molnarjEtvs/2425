def bekeres():
    szavak = []
    while True:
        szo = input("Add meg a szót: ")
        if not szo:
            break
        szavak.append(szo.upper())
    return szavak

def megallapitas(lista:list):
    db = len(lista)
    print(f"Szavak száma: {db} db")
    dbAI = 0
    for szo in lista:
        if szo.find("A") >= 0 and szo.find("I") >= 0:
            dbAI += 1

    print(f"a és i betű szerepel {dbAI} db szóban")
    print(f"Első szó: {lista[0]} Utolsó szó: {lista[-1]}")

x = bekeres()
megallapitas(x)