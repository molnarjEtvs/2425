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
paratlan = open("paratlanok.txt","w",encoding="utf-8")
for egySzam in szamok:
    if egySzam%2==0:
        paros.write(f"{egySzam}\n")
    else:
        paratlan.write(f"{egySzam}\n")
paros.close()
paratlan.close()