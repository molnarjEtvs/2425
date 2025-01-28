
def novenyRogzites():
    novenyek = []
    while True:
        nev = input("Add meg a növény nevét: ")
        if not nev:
            break
        novenyek.append(nev.lower()) 
    return novenyek

def novenyElemzes(novenyek:list):
    db = len(novenyek)
    print(f"{db} növény van rögzítve")
    dba = 0
    for noveny in novenyek:
        if noveny.endswith("a") == True:
            dba += 1
    print(f"a-ra végződik: {dba} db")
    szep = ">>>"
    egybefuzve = szep.join(novenyek)
    print(f"Növények: {egybefuzve}")
    
x = novenyRogzites()
novenyElemzes(x)

#novenyElemezes(novenyRogzites())