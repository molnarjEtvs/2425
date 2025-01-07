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

seged = 0
f = open("utca.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split(" ")
    if seged == 0:
        seged += 1
        savok = {}
        savok['A'] = int(adatok[0])
        savok['B'] = int(adatok[1])
        savok['C'] = int(adatok[2])
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
        talalat = True
        print(f"{egyEpitmeny['utca']} {egyEpitmeny['hazszam']}")
    
if talalat == False:
    print("Nem szerepel az adatállományban.")

