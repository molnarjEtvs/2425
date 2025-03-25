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
    print(f"{db} db mosógép van rögzítve")
    sdb = 0
    for egy in mosogepek:
        if egy.find('s') > -1 or egy.find('S') > -1:
        #if egy.lower().find('s')>-1:
            sdb += 1
    szoveg = "/".join(mosogepek)
    print(f"Rögzített mosógépek: {szoveg}")


m = mosogepRogzites()
mosogepElemzes(m)