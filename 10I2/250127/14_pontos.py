
def novenyRogzites():
    nevek = []
    while True:
        nev = input("Add meg a növény nevét: ").lower()
        if not nev:
            break
        nevek.append(nev)
    return nevek

def novenyElemzes(n:list):
    db = len(n)
    print(f"{db} növény van rögzítve")
    dba = 0
    for egy in n:
        if egy.endswith('a') == True:
            dba += 1
    print(f"a-ra végződik: {dba} db ")
    szeparator = ">>>"
    szoveg = szeparator.join(n)
    print(f"Növények: {szoveg}")

ve = novenyRogzites()
novenyElemzes(ve)

#novenyElemezes(novenyRogzites())