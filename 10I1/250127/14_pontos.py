
def novenyRogzites():
    novenyek = []
    while True:
        noveny = input("Add meg a növény nevét: ")
        if not noveny:
            break
        novenyek.append(noveny.lower())
    return novenyek

def novenyElemzes(nevek:list):
    db = len(nevek)
    print(f"{db} növény van rögzítve!")
    dba = 0
    for nev in nevek:
        if nev.endswith("a") == True:
            dba += 1
    szeparator = ">>>"
    sz = szeparator.join(nevek)
    print(f"Növények: {sz}")

barmi = novenyRogzites()
novenyElemzes(barmi)

