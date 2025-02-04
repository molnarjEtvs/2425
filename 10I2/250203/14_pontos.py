
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
    harmasok = []
    otosok = []
    hatEsTobb = []
    for egyHos in hosok:
        if len(egyHos) == 3:
            harmasok.append(egyHos)
        elif len(egyHos) == 5:
            otosok.append(egyHos)
        elif len(egyHos) >= 6:
            hatEsTobb.append(egyHos)
    harmasSzoveg = ",".join(harmasok)
    otosSzoveg = ",".join(otosok)
    hatosSzoveg = ",".join(hatEsTobb)
    print(f"Három betűsek: {harmasSzoveg}")
    print(f"Öt betűsek: {otosSzoveg}")
    print(f"Hat és több {hatosSzoveg}")

h = hosRogzites()
hosErtekeles(h)