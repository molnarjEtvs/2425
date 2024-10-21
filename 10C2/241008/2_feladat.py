import random
db = input("Add meg mennyi számot szeretnél: ")
db = int(db)

szam1 = input("Add meg a tól értéket: ")
szam1 = int(szam1)

szam2 = input("Add meg a ig értéket: ")
szam2 = int(szam2)

szamok = []
for x in range(db):
    vszam = random.randint(szam1,szam2)
    szamok.append(vszam)
print(szamok)