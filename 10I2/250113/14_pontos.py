import os
os.system("cls")

def macskaRogzites():
    nevek = []
    while True:
        nev = input("Add meg a macska nevét: ")
        if not nev:
            break
        nev = nev.capitalize()
        if nev not in nevek:
            nevek.append(nev)
    return nevek

def macskaElemzes(macskaNevek:list):
    db = len(macskaNevek)
    print(f"{db}db macska lett rögzítve")
    ibetusek = []
    for nev in macskaNevek:
        if nev.find("i") >= 0:
            ibetusek.append(nev)
    separator = ">>"
    osszefuzve = separator.join(ibetusek)
    print(f"i betűs macskák {osszefuzve}")

#macskaElemzes(macskaRogzites())
macskak = macskaRogzites()
macskaElemzes(macskak)