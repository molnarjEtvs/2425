import random
import os
os.system('cls')
db = input("Add meg hány db számot szeretnél: ")
db = int(db)
vszamok = []
for x in range(db):
    vszam = random.randint(1,10000)
    vszamok.append(vszam)
print(vszamok)