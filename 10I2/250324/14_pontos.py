def mosogepRogzites():
    markak = []
    while True:
        marka = input("Add meg a márka nevet: ")
        if not marka:
            break
        markak.append(marka)
    return markak

def mosogepElemzes(mosogepek:list):
    db = len(mosogepek)
    print(f"Darabszám: {db} db")
    sdb = 0
    for mosogep in mosogepek:
        if mosogep.find('s') > -1 or mosogep.find('S') > -1:
        #if mosogep.lower().find('s') > -1:
            sdb+=1
    print(f"{sdb} db van s betű")
    szoveg = mosogepek.join("/")
    print(f"Lista elemei: {szoveg}")

m = mosogepRogzites()
mosogepElemzes(m)
