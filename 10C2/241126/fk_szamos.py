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

i = open("osszeg.txt","w",encoding="utf-8")
i.write(f"Összeg: {osszeg}")
i.close()
