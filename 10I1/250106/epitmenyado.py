import os
os.system("cls")


def ado(adosav:str,alapTerulet:int):
    fizetendo = 0
    if adosav == "A":
        fizetendo = alapTerulet*800
    elif adosav == "B":
        fizetendo = alapTerulet*600
    else:
        fizetendo = alapTerulet*100
    
    if fizetendo < 10000:
        fizetendo = 0

    return fizetendo

epitmenyek = []
f = open("utca.txt","r",encoding="utf-8")
sorszam = 0
for sor in f:
    sor = sor.strip()
    adatok = sor.split(" ")
    if sorszam == 0:
        adosav = {}
        adosav['A'] = int(adatok[0])
        adosav['B'] = int(adatok[1])
        adosav['C'] = int(adatok[2])
        sorszam += 1
    else:
        epitmeny = {}
        epitmeny['adoszam'] = adatok[0]
        epitmeny['utca'] = adatok[1]
        epitmeny['hazszam'] = adatok[2]
        epitmeny['adosav'] = adatok[3]
        epitmeny['m2'] = int(adatok[4])
        epitmenyek.append(epitmeny)
f.close()

db = len(epitmenyek)
print(f"2. feladat. A mintában {db} telek szerepel.")

talalat = False
adoszam = input("3. feladat. Egy tulajdonos adószáma: ")
for egyEpitmeny in epitmenyek:
    if egyEpitmeny['adoszam'] == adoszam:
        print(f"{egyEpitmeny['utca']} {egyEpitmeny['hazszam']}")
        talalat = True
if talalat == False:
    print("Nem szerepel az adatállományban")

savA = {'db':0, 'osszeg':0}
savB = {'db':0, 'osszeg':0}
savC = {'db':0, 'osszeg':0}

for egyEpitmeny in epitmenyek:
    if egyEpitmeny['adosav'] == "A":
        savA['db'] += 1
        savA['osszeg'] += ado('A',egyEpitmeny['m2'])
    elif egyEpitmeny['adosav'] == "B":
        savB['db'] += 1
        savB['osszeg'] += ado('B',egyEpitmeny['m2'])
    else:
        savC['db'] += 1
        savC['osszeg'] += ado('C',egyEpitmeny['m2'])
    