import os
os.system("cls")

szamok = []
f = open("szamok.sza","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    szam = int(sor)
    szamok.append(szam)
f.close()

paros = open("parosak.txt","w",encoding="utf-8")
paratlan = open("paratlan.txt","w",encoding="utf-8")
for egyszam in szamok:
    if egyszam%2==0:
        paros.write(f"{egyszam}\n")
    else:
        paratlan.write(f"{egyszam}\n")
paros.close()
paratlan.close()