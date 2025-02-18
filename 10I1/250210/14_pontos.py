def bekeres():
    szavak = []
    while True:
        szo = input("Add meg szót: ")
        if not szo:
            break
        else:
            szo = szo.upper()
            szavak.append(szo)
    return szavak


def megallapitas(szavak:list):
    db = len(szavak)
    print(f"Szavak száma: {db} db")
    aiDb = 0
    for szo in szavak:
        if szo.find("A") > -1 and szo.find("I") > -1:
            aiDb += 1
    print(f"a és i betű szerepel {aiDb} db szóban ")
    print(f"Első szó: {szavak[0]}, utolsó szó: {szavak[-1]}")

sz = bekeres()
megallapitas(sz)