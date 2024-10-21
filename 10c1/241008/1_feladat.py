import random
import os
os.system("cls")
db = input("Add meg hány darab számot szeretnél: ")
db = int(db)
szamok = []
for x in range(db):
    szam = random.randint(1,10000)
    szamok.append(szam)
print(szamok)