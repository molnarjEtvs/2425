import random
def veletlenSzamok(db,tol,ig):
    szamok = []
    for x in range(db):
        vszam = random.randint(tol,ig)
        szamok.append(vszam)
    return szamok

sz = veletlenSzamok(6,10,100)
print(sz)
    