def macskaRogzites():
    nevek = []
    while True:
        nev = input("Add meg a macska nevét: ").capitalize()
        if not nev: #if nev == "":
            break
        if nev not in nevek:
            nevek.append(nev)
    return nevek

def macskaElemzes(macskak:list):
    db = len(macskak)
    print(f"{db} db macska lett rögzítve")
    ibetusek = []
    for egyMacska in macskak:
        if egyMacska.find("i")>-1:
            ibetusek.append(egyMacska)
    szeparator = ">>"
    szoveg = szeparator.join(ibetusek)
    print(f"i betűsek: {szoveg}")

#macskaElemzes(macskaRogzites())

m = macskaRogzites()
macskaElemzes(m)