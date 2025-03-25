def mosogepRogzites():
    markak = []
    while True:
        nev = input("Add meg a márka nevet: ")
        if nev == "":
            break
        markak.append(nev.capitalize())
    return markak

def mosogepElemzes(mosogepek:list):
    db = len(mosogepek)
    print(f"{db} mosógép van ")
    sdb = 0
    for x in mosogepek:
        if x.lower().find('s') > -1:
            sdb += 1
    szoveg = "/".join(mosogepek)
    print(f"Mosógépek: {szoveg}")

valami = mosogepRogzites()
mosogepElemzes(valami)
