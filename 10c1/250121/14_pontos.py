
def macskaRogzites():
    nevek = []
    while True:
        nev = input("Add meg a nevet: ").capitalize()
        if not nev:
            break
        if nev not in nevek:
            nevek.append(nev)
    return nevek

def macskaElemzes(macskaNevek:list):
    db = len(macskaNevek)
    print(f"{db} db macska lett rögzítve")
    inevek = []
    for egyMacska in macskaNevek:
        if egyMacska.find('i') > -1:
            inevek.append(egyMacska)
    szep = ">>"
    iSzoveg = szep.join(inevek)
    print(f"i betűs macskák: {iSzoveg}")
    
m = macskaRogzites()
macskaElemzes(m)
