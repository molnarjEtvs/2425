def hosRogzites():
    hosok = []
    while True:
        nev = input("Adj meg egy nevet: ")
        if not nev:
            break
        hosok.append(nev)
    return hosok

def hosErtekeles(hosok:list):
    db = len(hosok)
    print(f"Hősök száma: {db} db")
    harmasok = []
    otosek = []
    hatvagytobb = []
    for hos in hosok:
        if len(hos) == 3:
           harmasok.append(hos)
        elif len(hos) == 5:
            otosek.append(hos)
        elif len(hos)>=6:
            hatvagytobb.append(hos)
    harmasSzoveg = ",".join(harmasok)
    print(f"Három betűsek: {harmasSzoveg}")
    otosSzoveg = ",".join(otosek)
    print(f"Öt betűsek: {otosSzoveg}")
    hatosSzoveg = ",".join(hatvagytobb)
    print(f"Hat vagy több: {hatosSzoveg}")

x = hosRogzites()
hosErtekeles(x)