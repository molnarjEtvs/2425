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
    
    if fizetendo<10000:
        fizetendo = 0
    return fizetendo

epitmenyek = []

seged = 0
f = open("utca.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split(" ")
   
    if seged == 0:
        savok = {}
        savok['A'] = int(adatok[0])
        savok['B'] = int(adatok[1])
        savok['C'] = int(adatok[2])
        seged += 1
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
    print("Nem szerepel az adatállományban.")

savA = {'db':0,'osszeg':0}
savB = {'db':0,'osszeg':0}
savC = {'db':0,'osszeg':0}

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

print(f"A sávba {savA['db']} telek esik, az adó {savA['osszeg']} Ft.")
print(f"B sávba {savB['db']} telek esik, az adó {savB['osszeg']} Ft.")
print(f"C sávba {savC['db']} telek esik, az adó {savC['osszeg']} Ft.")

utcak = {}

for egyEpitmeny in epitmenyek:
    if egyEpitmeny['utca'] not in utcak:
        utcak[egyEpitmeny['utca']] = []

    if egyEpitmeny['adosav'] not in utcak[egyEpitmeny['utca']]:
        utcak[egyEpitmeny['utca']].append(egyEpitmeny['adosav'])

print(f"6. Feladat. A több sávba sorolt utcák: ")
for key in utcak.keys():
    if len(utcak[key])>1:
        print(key)

#f = open("fizetendo.txt","w",encoding="utf-8")
#f.close()


with open("fizetendo.txt","w",encoding="utf-8") as f:
    for egyEpitmeny in epitmenyek:
        f.write(f"{egyEpitmeny['adoszam']} {ado(egyEpitmeny['adosav'],egyEpitmeny['m2'])}\n")