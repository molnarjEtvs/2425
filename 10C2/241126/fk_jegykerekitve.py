import os, math
os.system("cls")

tanulok = []

f = open("tanulok_atlaga.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split(";")
    tanulo = {}
    tanulo['nev'] = adatok[0]
    tanulo['atlag'] = float(adatok[1])
    tanulo['atlagLe'] = math.floor(float(adatok[1]))
    tanulok.append(tanulo)
f.close()

i = open("tanulokkerek.txt","w",encoding="utf-8")
for egyTanulo in tanulok:
    i.write(f"Név: {egyTanulo['nev']}\n")
    i.write(f"Jegy: {egyTanulo['atlagLe']}\n")
    i.write(f"-----------------\n")
i.close()