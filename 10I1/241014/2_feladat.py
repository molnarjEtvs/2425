import random
import os
os.system("cls")
db = input("Add meg a darab: ")
db = int(db)
tol = input("Add meg a tól értéket: ")
tol = int(tol)
ig = input("Add meg a ig értéket: ")
ig = int(ig)
vszamok = []
for x in range(db):
    vszam = random.randint(tol,ig)
    vszamok.append(vszam)
print(vszamok)