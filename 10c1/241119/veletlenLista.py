'''
Készítsünk egy olyan függvényt ami véletlen számok listájával tér vissza. Bemeneti paraméterként adjuk meg:
- hány darab számot szeretnénk
- mettől
- meddig 
'''
import random
def lista(db,tol,ig):
    szamok = []
    for _ in range(db):
        szam = random.randint(tol,ig)
        szamok.append(szam)
    return szamok

veletlenSzamok = lista(10,5,400)
print(veletlenSzamok)