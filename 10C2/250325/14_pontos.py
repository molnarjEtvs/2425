def mosogepRogzites():
    markak = []
    while True:
        marka = input("Add meg a márka nevet: ")
        if not marka:
            break
        markak.append(marka.capitalize())
    return markak

def mosogepElemzes(mosogepek:list):
    db = len(mosogepek)
    print(f"{db} mosógép lett rögzítve")
    sdb = 0
    for mosogep in mosogepek:
        if mosogep.find('s') > -1 or mosogep.find('S') > -1:
        #if mosogep.lower().find('s') > -1
            sdb += 1
    print(f"s betűsek: {sdb} db")
    szoveg = "/".join(mosogepek)
    print(f"Rögzített mosógépek: {szoveg}")

m = mosogepRogzites()
mosogepElemzes(m)