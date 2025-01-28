
def novenyRogzites():
    novenyek = []
    while True:
        nev = input("Add meg a növény nevét: ")
        if not nev:
            break
        novenyek.append(nev.lower())
    return novenyek

def novenyElemezes(lista:list):
    db = len(lista)
    print(f"{db} növény van rögzítve")
    dba = 0
    for elem in lista:
        if elem.endswith('a') == True:
            dba += 1
    print(f"a-ra végződik: {dba} db ")
    szoveg = ">>>".join(lista)
    print(f"Növények: {szoveg}")

x = novenyRogzites()
novenyElemezes(x)