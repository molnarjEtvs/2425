
def hosRogzites():
    nevek = []
    while True:
        nev = input("Add meg a hős nevét: ")
        if not nev:
            break
        nevek.append(nev)
    return nevek

def hosErtekeles(nevek:list):
    db = len(nevek)
    print(f"Hősök száma: {db} db")
    harmas = []
    otos = []
    legalabbHat = []
    for nev in nevek:
        if len(nev) == 3:
            harmas.append(nev)
        elif len(nev) == 5:
            otos.append(nev)
        elif len(nev) >= 6:
            legalabbHat.append(nev)
    harmasTxt = ",".join(harmas)
    otosTxt = ",".join(otos)
    legalabbHatTxt = ",".join(legalabbHat)
    print(f"Három betűs: {harmasTxt}")
    print(f"Öt betűs: {otosTxt}")
    print(f"Hat és több: {legalabbHatTxt}")

x = hosRogzites()
hosErtekeles(x)

