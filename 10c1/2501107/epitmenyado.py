import os
os.system("cls")

def ado(adoSav:str,alapTerulet:int):
    fizetendo = 0
    if adoSav == "A":
        fizetendo = alapTerulet*800
    elif adoSav == "B":
        fizetendo = alapTerulet*600
    else:
        fizetendo = alapTerulet*100
    
    if fizetendo<10000:
        fizetendo = 0
    return fizetendo

epitmenyek = []
sorszam = 0
f = open("utca.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split(" ")
    if sorszam == 0:
        sorszam += 1
        adosav = {}
        adosav['A'] = int(adatok[0])
        adosav['B'] = int(adatok[1])
        adosav['C'] = int(adatok[2]) 
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

adoszam = input("3. feladat. Egy tulajdonos adószáma: ")

talalat = False
for egyEpitmeny in epitmenyek:
    if egyEpitmeny['adoszam'] == adoszam:
        print(f"{egyEpitmeny['utca']} {egyEpitmeny['hazszam']}")
        talalat = True
if talalat == False:
    print("Nem szerepel az adatállományban")

savA = {'db':0, 'osszeg': 0}
savB = {'db':0, 'osszeg': 0}
savC = {'db':0, 'osszeg': 0}

for egyEpitmeny in epitmenyek:
    if egyEpitmeny['adosav'] == "A":
        savA['db'] += 1
        savA['osszeg'] += ado("A",egyEpitmeny['m2'])
    elif egyEpitmeny['adosav'] == "B":
        savB['db'] += 1
        savB['osszeg'] += ado("B",egyEpitmeny['m2'])
    else:
        savC['db'] += 1
        savC['osszeg'] += ado("C",egyEpitmeny['m2'])

print(f"5. feladat")
print(f"A sávba {savA['db']} telek esik, az adó {savA['osszeg']} Ft.")
print(f"B sávba {savB['db']} telek esik, az adó {savB['osszeg']} Ft.")
print(f"C sávba {savC['db']} telek esik, az adó {savC['osszeg']} Ft.")