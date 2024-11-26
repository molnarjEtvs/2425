import os
os.system("cls")
szamok = []

f = open("szamok.sza","r",encoding="utf-8")
for row in f:
    row = row.strip()
    szam = int(row)
    szamok.append(szam)
f.close()

osszeg = sum(szamok)
print(f"számok összege: {osszeg}")
