import random
db = input("Add meg mennyi számot szeretnél: ")
db = int(db)
szamok = []
for x in range(db):
    vszam = random.randint(1,10000)
    szamok.append(vszam)
print(szamok)