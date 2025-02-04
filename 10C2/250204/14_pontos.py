def hosRogzites():
    hosok = []
    while True:
        hosNev = input("Add meg a hős nevét: ")
        if not hosNev:
            break
        hosok.append(hosNev)
    return hosok

def hosErtekeles(hosok:list):
    db = len(hosok)
    print(f"Hősök száma: {db} db")
    haromBetusek = []
    otBetusek = []
    legalabbHat = []
    for hos in hosok:
        if len(hos) == 3:
            haromBetusek.append(hos)
        elif len(hos) == 5:
            otBetusek.append(hos)
        elif len(hos) >= 6:
            legalabbHat.append(hos)
    szHarom = ",".join(haromBetusek)
    print(f"Három betűsek: {szHarom}")
    szOt = ",".join(otBetusek)
    print(f"Öt betűsek {szOt}")
    szlHat = ",".join(legalabbHat)
    print(f"Legalább 6 betűsek: {szlHat}")

x = hosRogzites()
hosErtekeles(x)