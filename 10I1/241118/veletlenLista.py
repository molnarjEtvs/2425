import random
def veletlenSzamok(db,tol,ig):
    szamok = []
    for x in range(db):
        vszam = random.randint(tol,ig)
        szamok.append(vszam)
    return szamok

x = veletlenSzamok(10,1,100)
print(x)