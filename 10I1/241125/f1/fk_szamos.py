import os
os.system("cls")
szamok = []

f = open("szamok.sza","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    szam = int(sor)
    szamok.append(szam)
f.close()

osszeg = sum(szamok)

#print(f"Összeg: {osszeg}")

p = open("osszeg.txt","w",encoding="utf-8")
p.write(f"Összeg: {osszeg}")
p.close()