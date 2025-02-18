
def bekeres():
    szavak = []
    while True:
        szo = input("Add meg a szót: ")
        if not szo:
            break
        szavak.append(szo.upper())
    return szavak

def megallapitas(szavak:list):
    db = len(szavak)
    print(f"Szavak száma: {db} db")
    dbAI = 0
    for szo in szavak:
        if szo.find('A') >= 0 and szo.find('I') >= 0:
            dbAI += 1

    print(f"a és i betű szerepel {dbAI} db szóban")
    print(f"Első szó: {szavak[0]}, utolsó szó: {szavak[-1]}")

szavak = bekeres()
megallapitas(szavak)