import os
os.system("cls")

def macskaRogzites():
    nevek = []
    while True:
        nev = input("Add meg a macska nevét: ").capitalize()
        if not nev:
            break
        #nev = nev.capitalize()
        if nev not in nevek:
            nevek.append(nev)
    return nevek

def macskaElemzes(macskaNevek:list):
    db = len(macskaNevek)
    print(f"{db} db macska lett rögzítve")
    ibetusek = []
    for egyNev in macskaNevek:
        if egyNev.find("i") > -1:
            ibetusek.append(egyNev)
    szep = ">>"
    print(f"i betűs macskák: {szep.join(ibetusek)}")

#macskaElemzes(macskaRogzites())
mnevek = macskaRogzites()
macskaElemzes(mnevek)