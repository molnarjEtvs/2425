import random
import os
os.system("cls")
db = input("Add meg hány darab számot szeretnél: ")
db = int(db)

tol = input("Add meg a tól értéket: ")
tol = int(tol)

ig = input("Add meg az ig értéket: ")
ig = int(ig)

szamok = []
for x in range(db):
    szam = random.randint(tol,ig)
    szamok.append(szam)
print(szamok)